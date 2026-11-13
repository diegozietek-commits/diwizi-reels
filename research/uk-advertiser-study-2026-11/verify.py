"""Confirm in the Transparency Center that each picked domain had ads shown in the UK, and when."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dfsqueue as q
HERE = os.path.dirname(os.path.abspath(__file__))
pick = json.load(open(os.path.join(HERE, "picked.json")))
tasks = [{"target": x["domain"], "location_code": 2826, "depth": 20, "tag": f"{sector}|{x['domain']}"} for sector, xs in pick.items() for x in xs]
print("tasks", len(tasks), flush=True)
def ext(r):
    its = [i for i in (r.get("items") or []) if i.get("type") == "ads_search"]
    last = max([i.get("last_shown") or "" for i in its] or [""])
    first = min([i.get("first_shown") or "9" for i in its] or [""])
    names = sorted({i.get("title") for i in its if i.get("title")})
    return {"ads": len(its), "last_shown": last[:10], "first_shown": first[:10], "advertisers": names[:3], "verified": any(i.get("verified") for i in its),
            "formats": sorted({i.get("format") for i in its if i.get("format")})}
q.run("ads_search", tasks, os.path.join(HERE, "verify_results.json"), ext)
