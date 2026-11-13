"""Turn sites.json into the study's summary: overall shares and one row per sector."""
import json, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(os.path.join(HERE, "sites.json")))
V = json.load(open(os.path.join(HERE, "verified.json")))
NO_BANNER_SIGNAL = {"Wix consent", "Shopify consent"}   # present on every site of those platforms, banner or not
K = [r for r in S if r.get("readable") and not r["parked"] and r["uk_signal"] and r["sector_match"]]
for r in K:
    r["banner"] = bool(r["consent_vendor"]) and r["consent_vendor"] not in NO_BANNER_SIGNAL
    r["grp"] = ("A" if r["ads_conversion"] else "B" if r["ads_tag"] else "C" if (r["ga4"] or r["google_tag_gt"]) else
                "D" if r["any_measurement"] else "H" if r["hidden_tag_signal"] else "E")
def share(rows, f):
    return round(100 * sum(1 for r in rows if f(r)) / len(rows)) if rows else None
def block(rows):
    tel = [r for r in rows if r["tel_link"]]
    return {"n": len(rows), "conv": share(rows, lambda r: r["grp"] == "A"), "ads_tag_no_conv": share(rows, lambda r: r["grp"] == "B"),
            "ga_only": share(rows, lambda r: r["grp"] == "C"), "other_only": share(rows, lambda r: r["grp"] == "D"),
            "hidden": share(rows, lambda r: r["grp"] == "H"), "nothing": share(rows, lambda r: r["grp"] == "E"),
            "ads_tag": share(rows, lambda r: r["ads_tag"]), "ga4": share(rows, lambda r: r["ga4"] or r["google_tag_gt"]), "gtm": share(rows, lambda r: r["gtm"]),
            "meta": share(rows, lambda r: r["meta_pixel"]), "uet": share(rows, lambda r: r["microsoft_uet"]), "banner": share(rows, lambda r: r["banner"]),
            "form": share(rows, lambda r: r["form"]), "tel": share(rows, lambda r: r["tel_link"]), "n_tel": len(tel),
            "call_measured_of_tel": share(tel, lambda r: r["call_measured"]), "call_not_measured_of_tel": share(tel, lambda r: not r["call_measured"]),
            "ads_call_conv_of_tel": share(tel, lambda r: r["ads_call_conversion"]), "call_vendor_of_tel": share(tel, lambda r: bool(r["call_tracking_vendor"])),
            "tel_click_of_tel": share(tel, lambda r: r["tel_click_tag"]), "enhanced": share(rows, lambda r: r["enhanced_conversions"])}
sectors = collections.defaultdict(list)
for r in K: sectors[r["sector"]].append(r)
out = {"overall": block(K), "sectors": {s: block(rows) for s, rows in sorted(sectors.items())},
       "funnel": {"domains_checked": len(V), "active_30d": sum(1 for v in V.values() if (v["last_shown"] or "") >= "2026-10-14"),
                  "readable": sum(1 for r in S if r.get("readable")), "kept": len(K)},
       "platforms": dict(collections.Counter(r["platform"] for r in K).most_common()),
       "last_shown_min": min(V[r["domain"]]["last_shown"] for r in K), "last_shown_max": max(V[r["domain"]]["last_shown"] for r in K),
       "verified_share": share(K, lambda r: V[r["domain"]]["verified"])}
json.dump(out, open(os.path.join(HERE, "summary.json"), "w"), indent=1)
json.dump(K, open(os.path.join(HERE, "kept.json"), "w"))
print(json.dumps(out["overall"])); print(out["funnel"], out["platforms"], out["last_shown_min"], out["last_shown_max"], out["verified_share"])
print(f"{'sector':38} n  conv adsnoc gaonly noth  ga4 banner tel callmeas")
for s, b in sorted(out["sectors"].items(), key=lambda x: -(x[1]["conv"] or 0)):
    print(f"{s:38}{b['n']:3} {b['conv']:4} {b['ads_tag_no_conv']:5} {b['ga_only']:6} {b['nothing']:5} {b['ga4']:4} {b['banner']:5} {b['tel']:4} {b['call_measured_of_tel']}")
best = sorted([r for r in K if r["grp"] == "A" and r["call_measured"] and (r["ga4"] or r["google_tag_gt"]) and r["banner"]], key=lambda r: (-(r["enhanced_conversions"] + r["conversion_linker"] + r["meta_pixel"] + bool(r["call_tracking_vendor"])), r["domain"]))
print("full set:", len(best)); print([(r["domain"], r["sector"]) for r in best[:24]])
