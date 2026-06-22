---
name: finding_edgar_403_user_agent_header
description: "SEC EDGAR / data.sec.gov 403s on WebFetch are a missing-User-Agent problem, not a network block — a declared UA over urllib works"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 193dc131-3678-493a-b2b1-9b4fc7c2f665
---

When `WebFetch` returns HTTP 403 on SEC.gov / `data.sec.gov` / `efts.sec.gov` (the recurring blocker on any bank-filing research — DEWEY hit it across the 6/21 FL-bank run), the cause is **not** a network block or rate limit: SEC requires a **declared User-Agent header** (with contact info) for all programmatic access and rejects generic/absent UAs. A plain `urllib.request` with `headers={"User-Agent": "Research <name> <email>"}` works fine (verified live 2026-06-22 — fetched `data.sec.gov/submissions/CIK*.json`, XBRL `companyconcept`, filing HTML, and EFTS full-text search).

**How to apply:** don't fall back to lower-grade institutional-mirror sources when EDGAR 403s — use a UA-headed script instead. DEWEY's `scripts/` now has the helpers: `edgar_fetch.py` (submissions/filing lists), `edgar_doc.py` (`facts` = XBRL companyconcept for clean NCO/ACL/NPL/CET1 numbers, `doc` = primary-document HTML→text + `--grep` to read 10-Q MD&A geographic-concentration notes directly, `search` = EFTS full-text), and `pdf2text.py` (pdfminer.six wrapper for OIR/Realtors PDFs that WebFetch returns as unparseable binary). Run with `.venv/bin/python3`. SEC also rate-limits ~10 req/s — space bursts or transient 403/timeout can recur.

Related: institutional-mirror financials are [[finding_private_by_construction_unverifiable]]-adjacent (re-mark source-grade when the primary is unread); [[feedback_subagent_web_tools_not_autoloaded]] (confirm a sub-agent actually has WebFetch/WebSearch before trusting a "blocked" report).
