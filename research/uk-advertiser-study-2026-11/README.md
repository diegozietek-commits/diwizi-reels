# UK advertiser measurement study, November 2026

Source of `/guides/google-ads-advertisers-measurement-uk/` on ppcconsultancy.uk (230 sites, 15 sectors, read on 13 Nov 2026).

Order of the scripts:

1. `discover2.py`: Ads Transparency Center (region UK) domain suggestions for trade words, through the DataForSEO SERP API.
2. `select_domains.py 28`: up to 28 UK-looking domains per sector.
3. `verify.py`: confirms each domain had an ad shown in the UK and when (kept: last shown on or after 14 Oct 2026).
4. `analyze.py to_read.json`: reads each home page, its Tag Manager containers, Google tag files and Wix tag list through the DataForSEO On-Page API.
5. `aggregate.py`: writes `summary.json` (overall and by sector).
6. `make_page.py <site dir>`: writes the guide source, the public CSV in `assets/data/` and the Dataset JSON-LD.

The site-level result is deliberately not in this repository, which is public: the site shows sector totals only, and names one well-measured site per sector.

Credentials: `dfs.py` reads a private `.netrc` placed next to it (never commit it). The whole run cost about US$ 1.10.
