"""Post tasks to a DataForSEO standard queue endpoint and collect the results."""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dfs
def run(endpoint, tasks, save_path, extract, max_wait=1500):
    ids = {}
    for i in range(0, len(tasks), 100):
        d = dfs.call(f"/v3/serp/google/{endpoint}/task_post", tasks[i:i + 100])
        for t in d["tasks"]:
            if t["status_code"] in (20100, 20000): ids[t["id"]] = t["data"]["tag"]
            else: print("post failed", t["status_code"], t["status_message"], flush=True)
    print("posted", len(ids), "of", len(tasks), "spent", round(dfs.SPENT, 4), flush=True)
    out, pending, t0 = {}, dict(ids), time.time()
    while pending and time.time() - t0 < max_wait:
        time.sleep(30)
        for tid in list(pending):
            try: d = dfs.call(f"/v3/serp/google/{endpoint}/task_get/advanced/{tid}", tries=2)
            except Exception: continue
            t = d["tasks"][0]
            if t["status_code"] == 20000:
                out[tid] = {"tag": pending.pop(tid), "data": extract((t.get("result") or [{}])[0] or {})}
            elif t["status_code"] not in (40601, 40602, 20100):
                out[tid] = {"tag": pending.pop(tid), "data": None, "error": t["status_message"]}
        json.dump(out, open(save_path, "w"))
        print(f"{int(time.time()-t0)}s done {len(out)} pending {len(pending)}", flush=True)
    print("FINISHED done", len(out), "pending", len(pending), "spent", round(dfs.SPENT, 4), flush=True)
    return out
