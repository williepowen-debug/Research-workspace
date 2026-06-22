# DEWEY scripts/ — backlog

Recurring data-source blockers and tooling asks surfaced by research Process Reports.
Promotion-scan target (CLOSEOUT step 11): when a blocker is hit on **more than one** run, log it here so it gets fixed once instead of re-hit every run. One-line entries; link the report that surfaced it.

| Date added | Blocker / ask | Impact | Status |
|------------|---------------|--------|--------|
| 2026-06-21 | **SEC.gov EDGAR 403s on `WebFetch`** — direct 10-Q/10-K reads blocked; bank figures fall back to institutional mirrors (lower grade). Need an EDGAR full-text-search / API helper in `scripts/` (not WebFetch). | High — recurring on any bank-filing research | **DONE 2026-06-22** — root cause was the missing User-Agent header (SEC blocks generic WebFetch UAs; a declared UA over urllib works). `edgar_doc.py` adds `facts` (XBRL companyconcept — clean NCO/ACL/NPL/CET1 numbers), `doc` (fetch primary doc → HTML-stripped text + `--grep`, i.e. read the 10-Q MD&A geographic-concentration notes directly), `search` (EFTS full-text). All 3 tested live (WALTER, Will-directed). `edgar_fetch.py` (submissions lister) unchanged. |
| 2026-06-21 | **FL OIR / FL Realtors PDFs return as unparseable binary** to `WebFetch` — load-bearing figures (e.g. Citizens uncapped commercial rate, FL Realtors condo detail) unreadable. Need a PDF-to-text wrapper. | Medium | **DONE 2026-06-22** — `pdf2text.py` (pdfminer.six, already in the venv) — URL or local path → text, optional `--grep`/`--pages`. Tested live. Run with `.venv/bin/python3`. Use it to re-confirm the Citizens commercial +18.8% uncapped figure from the OIR rate-filing PDF. |

*Surfaced by: `output/2026-06-21_fl-bank-loss-transmission-timing.md` (Process Report).*
