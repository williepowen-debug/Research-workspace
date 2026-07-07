---
name: finding-fdic-securities-filings-api
description: "FDIC securities-filings JSON API (securitiesfilings.fdicconnect.fdic.gov) gives fully scripted access to filings + insider Form 3/4/5 + attachment PDFs for FDIC-supervised banks that don't file with SEC EDGAR (e.g. OZK cert"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 72b0ae62-978e-40f6-92d2-228a30f5b4b0
---

**The old `efr.fdic.gov/fcxweb/efr/` URL redirects to `securitiesfilings.fdicconnect.fdic.gov`** (Angular SPA). Its backing JSON API works with just a browser User-Agent header — no auth (discovered 2026-07-06, OZK session):

- `GET /api/instdiscl/cert/{cert}` — all insider Form 3/4/5 records (filer name, form type, pub date, disclID)
- `GET /api/instdiscl/{disclID}` — per-filing transaction lines: A/D code `asetSctyAcqDspsCde`, shares `asetSctyAcqDspsCnt`, $/sh `asetSctyAcqDspsShrAmt`, post-txn holdings `asetSctyOwnCnt`, txn date `asetSctyTranDte`, footnote text `instDisclOwnrExplTxt`
- `GET /api/instflng/cert/{cert}` — all company filings (8-K/10-Q/10-K/proxy) with attachment metadata (`instFlngId`, `instFlngAtchId`)
- `GET /api/instflng/{instFlngId}/attachment/{atchId}` — **downloads the actual filing PDFs**

**Why it matters:** banks that dissolved their holding companies (OZK, cert #110) file 10-K/10-Q/8-K AND Section 16 insider forms with the FDIC, not SEC EDGAR — every EDGAR-keyed tool silently misses them. This API bypasses both that gap and OZK's 403-blocking IR page (first fruit: the Q1'26 10-Q OZK had never been able to script-pull). Applies to any FDIC-supervised non-EDGAR filer in the coverage universe. Example: `curl -s -A "Mozilla/5.0" "https://securitiesfilings.fdicconnect.fdic.gov/api/instdiscl/cert/110"`.

Related: [[finding_edgar_403_user_agent_header]] (same UA trick, different agency). OZK-local detail → `AGENTS/OZK/MEMORY.md` Findings 7/6 + `INSIDERS/SELLING.md` Pull Log.
