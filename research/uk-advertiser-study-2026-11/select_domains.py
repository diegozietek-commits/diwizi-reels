"""From the Transparency Center suggestions, pick up to N UK domains per sector to verify."""
import json, os, re, collections, sys
HERE = os.path.dirname(os.path.abspath(__file__))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 36
res = json.load(open(os.path.join(HERE, "adv_results.json")))
EXCLUDE = re.compile(r"checkatrade|bark\.com|yell\.com|trustatrader|mybuilder|ratedpeople|comparethemarket|moneysupermarket|unbiased|vouchedfor|rightmove|zoopla|onthemarket|gumtree|facebook|yelp|trustpilot|"
                     r"comparemymove|reallymoving|anyvan|shiply|getagent|quotatis|taskrabbit|airtasker|whatclinic|doctify|topdoctors|treatwell|amazon|ebay|indeed|reed\.co|totaljobs|google\.|youtube|wikipedia|directory")
by = collections.defaultdict(dict)   # sector -> domain -> keyword that found it
for r in res.values():
    sector, kw = r["tag"].split("|")
    for it in r.get("data") or []:
        d = (it.get("domain") or "").lower().strip()
        if it["type"] != "ads_domain" or not d: continue
        d = re.sub(r"^www\.", "", d)
        if not re.search(r"\.(co\.uk|uk|com|org\.uk|net|london|scot|wales)$", d) or EXCLUDE.search(d): continue
        by[sector].setdefault(d, kw)
seen, pick = set(), {}
for sector in sorted(by, key=lambda s: len(by[s])):     # smallest sectors choose first
    doms = [d for d in by[sector] if d not in seen]
    doms.sort(key=lambda d: (0 if d.endswith(".uk") else 1, by[sector][d], d))
    # spread the picks across the keywords that found them
    groups = collections.defaultdict(list)
    for d in doms: groups[by[sector][d]].append(d)
    chosen = []
    while len(chosen) < N and any(groups.values()):
        for k in list(groups):
            if groups[k] and len(chosen) < N: chosen.append(groups[k].pop(0))
    for d in chosen: seen.add(d)
    pick[sector] = [{"domain": d, "keyword": by[sector][d]} for d in chosen]
    print(f"{sector:40} suggested {len(by[sector]):3} picked {len(chosen)}")
json.dump(pick, open(os.path.join(HERE, "picked.json"), "w"), indent=1)
print("total picked", sum(len(v) for v in pick.values()))
