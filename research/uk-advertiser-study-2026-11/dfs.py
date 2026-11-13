"""Tiny DataForSEO client. Credentials come from the private .netrc next to this file; nothing is printed."""
import json, netrc, os, base64, urllib.request, time
HERE = os.path.dirname(os.path.abspath(__file__))
_l, _, _p = netrc.netrc(os.path.join(HERE, ".netrc")).authenticators("api.dataforseo.com")
_AUTH = "Basic " + base64.b64encode(f"{_l}:{_p}".encode()).decode()
SPENT = 0.0
def call(path, data=None, method=None, tries=4):
    global SPENT
    url = "https://api.dataforseo.com" + path
    body = json.dumps(data).encode() if data is not None else None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=body, method=method or ("POST" if body else "GET"),
                                         headers={"Authorization": _AUTH, "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as r:
                d = json.loads(r.read().decode("utf-8", "replace"))
            SPENT += d.get("cost") or 0
            return d
        except Exception as e:
            err = e
            time.sleep(3 * (i + 1))
    raise RuntimeError(f"{path}: {type(err).__name__}")
