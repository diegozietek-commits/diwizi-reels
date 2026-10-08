#!/usr/bin/env python3
"""Tell IndexNow (Bing, Yandex, Seznam, Naver) which pages of a site changed in this publish.

Usage:
    python3 sites/indexnow.py sites/googleadsfreelancer.com --since <git sha> [--wait 900]
    python3 sites/indexnow.py sites/ppcconsultancy.uk --all

--since  compares lastmod.json at that commit with the current one; only pages whose entry changed
         (or are new) are sent. If the commit or the file is not available, every sitemap URL is sent.
--all    sends every URL in dist/sitemap.xml (first run).
--wait   before sending, waits up to N seconds for the new deploy to be live: the key file must
         answer 200 with the key, and the <main> content of every page being sent must match dist/. On
         timeout it sends anyway and says so in the log.

The key is the dist/<32 hex>.txt file that build.py writes. Standard library only, so it runs on a
bare CI runner. It never exits with an error: a failed notice is logged, never fatal to a deploy.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from xml.etree import ElementTree

ENDPOINT = "https://api.indexnow.org/indexnow"
MAX_URLS = 10000
UA = "diwizi-indexnow/1.0 (+https://diwizi.com/)"


def log(msg):
    print(f"[indexnow] {msg}", flush=True)


def find_key(dist):
    for name in sorted(os.listdir(dist)):
        m = re.fullmatch(r"([0-9a-f]{32})\.txt", name)
        if m and open(os.path.join(dist, name), encoding="utf-8").read() == m.group(1):
            return m.group(1)
    return None


def sitemap_urls(dist):
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ElementTree.parse(os.path.join(dist, "sitemap.xml")).getroot()
    return [loc.text.strip() for loc in root.findall("s:url/s:loc", ns)]


def slug_of(url):
    path = re.sub(r"^https?://[^/]+", "", url).strip("/")
    return path or "index"


def dist_file(dist, url):
    slug = slug_of(url)
    return os.path.join(dist, "index.html") if slug == "index" else os.path.join(dist, slug, "index.html")


def previous_lastmod(site_dir, since):
    if not since or set(since) == {"0"}:
        return None
    rel = os.path.relpath(os.path.join(site_dir, "lastmod.json"),
                          subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                                         text=True, cwd=site_dir).stdout.strip() or ".")
    r = subprocess.run(["git", "show", f"{since}:{rel}"], capture_output=True, text=True, cwd=site_dir)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except ValueError:
        return None


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Cache-Control": "no-cache"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception as e:  # network trouble is just "not yet"
        return f"error: {e.__class__.__name__}", b""


def content_hash(html):
    """Hash of <main>...</main>, the visible content that lastmod.json tracks. Cloudflare injects
    scripts (Web Analytics beacon, bot management) before </body>, so the whole file never matches."""
    i, j = html.find(b"<main>"), html.find(b"</main>")
    part = html[i:j] if 0 <= i < j else html.split(b"</body>")[0]
    return hashlib.sha256(part).hexdigest()


def wait_until_live(host, key, urls, dist, seconds):
    key_url = f"https://{host}/{key}.txt"
    want = {u: content_hash(open(dist_file(dist, u), "rb").read()) for u in urls}
    deadline = time.time() + seconds
    while True:
        status, body = fetch(key_url)
        key_ok = status == 200 and body.decode("utf-8", "replace") == key
        stale = []
        if key_ok:
            for u in urls:
                st, b = fetch(u)
                if st != 200 or content_hash(b) != want[u]:
                    stale.append((u, st))
        if key_ok and not stale:
            log(f"deploy is live: key file 200 and matching, <main> of {len(urls)} page(s) matches dist/")
            return True
        if time.time() >= deadline:
            log(f"WARNING: gave up waiting after {seconds}s (key file: {status}, "
                f"{'matches' if key_ok else 'does not match'}; pages not live yet: {len(stale)}). Sending anyway.")
            return False
        time.sleep(15)


def post(host, key, urls):
    ok = True
    for i in range(0, len(urls), MAX_URLS):
        chunk = urls[i:i + MAX_URLS]
        payload = json.dumps({"host": host, "key": key, "keyLocation": f"https://{host}/{key}.txt",
                              "urlList": chunk}).encode("utf-8")
        req = urllib.request.Request(ENDPOINT, data=payload, method="POST",
                                     headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                status, body = r.status, r.read()[:300]
        except urllib.error.HTTPError as e:
            status, body = e.code, e.read()[:300]
        except Exception as e:
            status, body = f"error: {e.__class__.__name__}", str(e).encode()[:300]
        good = status in (200, 202)
        ok = ok and good
        log(f"{host}: POST {len(chunk)} URL(s) -> HTTP {status}{'' if good else ' FAILED'}"
            f"{(' ' + body.decode('utf-8', 'replace')) if body else ''}")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("site_dir")
    ap.add_argument("--since", default="")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--wait", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    site_dir = os.path.abspath(a.site_dir)
    host = os.path.basename(site_dir.rstrip("/"))
    dist = os.path.join(site_dir, "dist")
    key = find_key(dist)
    if not key:
        log(f"{host}: no key file in dist/, nothing sent")
        return
    urls = sitemap_urls(dist)

    if not a.all:
        old = previous_lastmod(site_dir, a.since)
        if old is None:
            log(f"{host}: no previous lastmod.json for '{a.since or '-'}', sending every sitemap URL")
        else:
            new = json.load(open(os.path.join(site_dir, "lastmod.json"), encoding="utf-8"))
            changed = {s for s, v in new.items() if old.get(s) != v}
            urls = [u for u in urls if slug_of(u) in changed]
    if not urls:
        log(f"{host}: no page changed, nothing sent")
        return
    log(f"{host}: {len(urls)} URL(s) to send")
    for u in urls:
        log(f"  {u}")
    if a.dry_run:
        return
    if a.wait:
        wait_until_live(host, key, urls, dist, a.wait)
    post(host, key, urls)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # never break a deploy over a notice
        log(f"ERROR (ignored): {e.__class__.__name__}: {e}")
    sys.exit(0)
