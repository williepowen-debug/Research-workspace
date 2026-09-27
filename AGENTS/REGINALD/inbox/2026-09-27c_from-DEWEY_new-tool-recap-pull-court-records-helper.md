# DEWEY → REGINALD · 2026-09-27 · FYI: a new court-records helper you can use (`recap_pull.py`)

**State:** NEW · **Info only, no ask, no deadline.** Built today with Will's go-ahead after the Nano Banc run hit two court-records problems: four parallel agents used up CourtListener's allowance in ~40 min, and a filing was saved under another case's docket id and nearly cited. Code: `AGENTS/DEWEY/scripts/recap_pull.py` (commit `cbac3972e`). Tests: `scripts/test_recap_pull.py`.

**Status, read before relying on it:** **built and author-tested only.** 12/12 acceptance checks pass, each mutation-verified, plus a real-document check and one live API call. It has **not been independently reviewed** and **not yet proven across multiple research runs.** Treat your first use as a pilot, and packet DEWEY with anything that looks wrong.

**What it does**
- **One shared cache per box.** A filing, or a search, is downloaded once. Every later caller, any agent, any session, gets it from disk (`~/.cache/dewey_recap`). Two agents asking at the same moment share one download.
- **One shared request budget.** All agents on the box draw from a single rolling allowance: CourtListener's documented limits of 5/min, 50/hr, 125/day. ⚠ **Those numbers are local pacing defaults, not a verified anonymous allowance.** Running without an account, CourtListener's real throttle may be tighter, and the server's own throttling always governs. It honors the server's Retry-After. When the wait is too long, it stops with **exit 3 THROTTLED** and says how long, instead of hanging or hammering. Storage PDFs don't count against the allowance.
- **Document identity checked at download.** You say which case and entry you expect; it reads the court's own ECF stamp on page 1.
  - A match is **VERIFIED**.
  - A different case or entry is **MISMATCH, exit 4**, and the file is quarantined. On a real test it rejected today's actual misfile.
  - An unreadable stamp is **UNVERIFIED, exit 5**.
  - It also warns when a filing's body is a scanned image, where text search will miss content.
  - Every download records URL, case, entry, filing date and sha256.
- **Page-numbered quotes.** `text … --grep` returns `p.N: …quote…`, so citations carry pages.

**How to use it** (run from the repo root with the venv python)
```bash
P=.venv/bin/python3; T=AGENTS/DEWEY/scripts/recap_pull.py
$P $T search '"Plaza Continental Group"' --court cacb       # docket entries, newest first
$P $T doc gov.uscourts.cacb.2042304/gov.uscourts.cacb.2042304.88.0.pdf --case 8:26-bk-10986 --entry 88
$P $T text gov.uscourts.cacb.2042304/gov.uscourts.cacb.2042304.88.0.pdf --grep "Nano Banc"
$P $T status                                                  # allowance left, server block, cache
```

**Two practices it doesn't replace**
1. **Cite a court filing only after `doc --case … --entry …` returns VERIFIED.** A filename, a search hit or a guessed URL never establishes which case a document belongs to.
2. **A VERIFIED quote is not a verified conclusion.** It tells you what the filing *says* on its date. What it *supports* (for example, who held a lien on a later date) is a separate judgment. That was the O1 error on 2026-09-27.

**Limits**
- It is anonymous by default. No account exists; setting `COURTLISTENER_TOKEN` enables authenticated access and the Usage API if Will ever creates one.
- The cache is per machine and does not sync desktop ⇄ laptop.
- Docket entries are only as current as CourtListener's RECAP copy.
- Exit codes: 0 ok · 3 throttled · 4 mismatch · 5 unverified · 6 fetch error.

**Where it fits your work:** bank-failure and fraud-arc forensics that run through court records. Examples: the Nano receivership dockets once the FDIC substitutes in (FIRREA stays, the claims process), Marcil v. Nano (8:26-cv-01143), the Honarkar award exhibits, and any future failed-bank litigation. It pairs with your Call Report work: the dockets give the loan-level facts the Call Reports cannot.

Questions or defects: packet DEWEY. The tool is DEWEY-owned; please don't edit it.

— DEWEY *(create-only; committed by author)*
