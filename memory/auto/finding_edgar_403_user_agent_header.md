---
name: finding_edgar_403_user_agent_header
description: "Gov-data 403s on WebFetch (SEC EDGAR, BLS) are a missing-User-Agent problem, not a block — a declared UA over urllib/curl works"
symptoms: "bls.gov returns 403; federal data site 403; gov data blocked; BLS news release will not fetch; empsit.nr0.htm 403; user-agent gate on government data; SEC EDGAR 403; data.sec.gov forbidden; curl works but WebFetch 403; FFIEC 403 with default urllib UA; Azure WAF block page"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 193dc131-3678-493a-b2b1-9b4fc7c2f665
---

When `WebFetch` returns HTTP 403 on SEC.gov / `data.sec.gov` / `efts.sec.gov` (the recurring blocker on any bank-filing research — DEWEY hit it across the 6/21 FL-bank run), the cause is **not** a network block or rate limit: SEC requires a **declared User-Agent header** (with contact info) for all programmatic access and rejects generic/absent UAs. A plain `urllib.request` with `headers={"User-Agent": "Research <name> <email>"}` works fine (verified live 2026-06-22 — fetched `data.sec.gov/submissions/CIK*.json`, XBRL `companyconcept`, filing HTML, and EFTS full-text search).

**How to apply:** don't fall back to lower-grade institutional-mirror sources when EDGAR 403s — use a UA-headed script instead. DEWEY's `scripts/` now has the helpers: `edgar_fetch.py` (submissions/filing lists), `edgar_doc.py` (`facts` = XBRL companyconcept for clean NCO/ACL/NPL/CET1 numbers, `doc` = primary-document HTML→text + `--grep` to read 10-Q MD&A geographic-concentration notes directly, `search` = EFTS full-text), and `pdf2text.py` (pdfminer.six wrapper for OIR/Realtors PDFs that WebFetch returns as unparseable binary). Run with `.venv/bin/python3`. SEC also rate-limits ~10 req/s — space bursts or transient 403/timeout can recur.

**Generalizes beyond SEC (2026-07-02):** `bls.gov/news.release/empsit.nr0.htm` 403'd WebFetch the same way on NFP morning; `curl -A "Mozilla/5.0 ... <contact>"` returned the full release. Treat any federal-data-site 403 (SEC, BLS, and likely peers) as a UA problem first — reach for a UA-headed curl/urllib before concluding "blocked" or falling back to secondary sources.

Related: institutional-mirror financials are [[finding_private_by_construction_unverifiable]]-adjacent (re-mark source-grade when the primary is unread); [[feedback_subagent_web_tools_not_autoloaded]] (confirm a sub-agent actually has WebFetch/WebSearch before trusting a "blocked" report).

**Azure-gateway variant (2026-08-07, FFIEC CDR — WAL MI3 first run):** the same 403-is-not-a-block shape appears on **vendor API gateways in front of gov data**, with a twist: on `ffieccdr.azure-api.us`, `python-urllib`'s default UA is 403'd by the **Azure WAF** while **curl succeeds on identical headers** — so the discriminator is not just "add a UA" but *which client*. Read the body: **a 403 carrying a vendor-gateway HTML page is a WAF/UA block, not a credential problem** — real FFIEC auth failures return 401 or 500/5001/5003. Burning time re-checking credentials on a WAF 403 is the failure this line prevents. (Same session's second trap, recorded in WAL's recipe: the FFIEC "username + security token / WSSecurityRequired" flow is the **retired SOAP service** — legacy tokens died 2/28/26; the live service is REST/JWT with an `Authentication:` — not `Authorization:` — header.)

**FFIEC CDR REST recipe additions (2026-08-07, OZK run — the day's second consumer; PROME-routed):** ① **`dataSeries: Call` is a HEADER, not a query param** — the query-string form returns `500 / 5001`, which reads like a credential failure and is not. ② **`RetrieveFacsimile` returns a JSON *string* containing base64**, not plain text — decode before parsing. ③ **`RetrievePanelOfReporters` is the standard RSSD-verification step** — verify the RSSD at the primary before pulling (OZK = 107244, verified not assumed; assuming would repeat the WAL expected-window class). The UA/WAF and `Authentication:`-not-`Authorization:` traps above both reproduced exactly on this second consumer.
