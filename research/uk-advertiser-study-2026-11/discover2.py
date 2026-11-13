"""Find UK advertisers by sector in Google's Ads Transparency Center (domain suggestions for trade words)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dfsqueue as q
HERE = os.path.dirname(os.path.abspath(__file__))
CITIES = ["london", "manchester", "birmingham", "leeds", "bristol"]
SECTORS = {
    "Solicitors": (["solicitors", "solicitor", "conveyancing", "lawyers", "familylaw", "legal"], ["solicitors", "law"]),
    "Accountants": (["accountants", "accountancy", "accounting", "bookkeeping", "accountant", "tax"], ["accountants", "accounting"]),
    "Dentists": (["dental", "dentist", "dentistry", "smile", "implants", "orthodontics"], ["dental", "dentist"]),
    "Private healthcare and physiotherapy": (["physio", "physiotherapy", "clinic", "osteopath", "chiropractic", "podiatry"], ["physio", "clinic"]),
    "Plumbing and heating": (["plumbers", "plumbing", "heating", "boiler", "boilers", "plumber"], ["plumbers", "plumbing"]),
    "Electricians": (["electrician", "electrical", "electricians", "electrics", "rewire", "evcharger"], ["electrician", "electrical"]),
    "Roofing": (["roofing", "roofers", "roofs", "roofer", "guttering", "flatroof"], ["roofing", "roofers"]),
    "Estate and letting agents": (["estateagents", "lettings", "estates", "estateagent", "property", "homes"], ["estateagents", "lettings"]),
    "Mortgage and financial advice": (["mortgage", "mortgages", "financial", "wealth", "pensions", "financialplanning"], ["mortgage", "mortgages"]),
    "IT support": (["itsupport", "itservices", "computers", "networks", "managedit", "cyber"], ["itsupport", "computers"]),
    "Removals": (["removals", "removal", "movers", "moving", "manandvan", "storage"], ["removals", "movers"]),
    "Home improvement": (["lofts", "loft", "kitchens", "bathrooms", "builders", "driveways"], ["kitchens", "builders"]),
    "Cleaning": (["cleaning", "cleaners", "carpetcleaning", "ovencleaning", "windowcleaning", "clean"], ["cleaning", "cleaners"]),
    "Pest control": (["pestcontrol", "pest", "pests", "pestsolutions", "wasp", "vermin"], ["pestcontrol", "pest"]),
    "Locksmiths and drainage": (["locksmith", "locksmiths", "locks", "drainage", "drains", "drain"], ["locksmith", "drainage"]),
}
tasks = []
for sector, (terms, city_terms) in SECTORS.items():
    kws = list(terms) + [t + c for t in city_terms for c in CITIES] + [c + t for t in city_terms[:1] for c in CITIES]
    for kw in kws:
        tasks.append({"keyword": kw, "location_code": 2826, "tag": f"{sector}|{kw}"})
print("tasks", len(tasks), flush=True)
q.run("ads_advertisers", tasks, os.path.join(HERE, "adv_results.json"),
      lambda r: [{"type": i["type"], "domain": i.get("domain"), "title": i.get("title"), "advertiser_id": i.get("advertiser_id"),
                  "location": i.get("location"), "verified": i.get("verified"), "approx_ads_count": i.get("approx_ads_count")} for i in (r.get("items") or [])])
