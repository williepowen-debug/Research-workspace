# CYPHER — DATA ROUTES

*Moved verbatim from `CLAUDE.md` at build (2026-10-22, charter byte budget); boot.py leg numbers then corrected (7 = KEV, 8 = 8-K) after the matrix leg was added. Read when you pull data; re-record reachability when a route changes.*

## DATA ROUTES (reachability recorded at build, 2026-10-22)

| Route | State at build | Use |
|---|---|---|
| **CISA KEV catalog JSON** (`cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json`) | **REACHABLE** — v2026.10.21, 1,754 entries, read 22:3x UTC | Row 2 (confirmed in-the-wild exploitation). `boot.py` leg 7 |
| **SEC EDGAR full-text search** (`efts.sec.gov/LATEST/search-index`, `"Item 1.05"`, form 8-K) | **REACHABLE** (needs a contact User-Agent) — 0 hits 10/15–10/22; positive control 41 in 2024, 18 in 7/01–10/22/2026 | Row 4 (material cybersecurity incident, legally required). `boot.py` leg 8 |
| NVD API 2.0 | REACHABLE (DEWEY pulled Q3 counts) | Disclosure volume. ⚠️ NVD's 2026 severity counts are unusable (scoring backlog): never cite a 2026 "critical CVE" count |
| Vendor advisories · CERT/NCSC pages · Mozilla Bugzilla | Mixed per host | Event confirmation |
| Verisk PCS cyber catastrophe designations | ⛔ subscription — expect `MIRROR-WALLED` | Row 6 (SHADE's consequence) |
| NYDFS industry alerts | 403 to DEWEY on 10/22 | Row 5 — **data an LLM may not reach; tell Will before spending a session on it** |
| X / social posts | Leads only | Never confirmation (guardrail 3) |
