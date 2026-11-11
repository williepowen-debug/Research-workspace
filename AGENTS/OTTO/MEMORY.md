# OTTO MEMORY

**Updated:** 2026-11-11, s044. Boot navigation and continuity; live metrics belong to STATUS/workbooks. Mistake patterns live in boot-read `LESSONS.md`. Prior memory preserved byte-for-byte in `archive/MEMORY_2026-10-19_pre-s031.md`; old entries are history, not pending work.

## Desk boundaries
- OTTO owns auto-fraud mechanisms, collateral evidence and identification of exposed counterparties. REGINALD owns bank sizing; BROCK owns CRMT financing grades and BDC marks; TERRY constructs trades and Will decides.
- Root/desk charter owns routing and evidence conventions. Use WALTER for new signals; a peer's own ask may receive a direct answer, with a parallel WALTER drop for any firing/new dated fact. Never edit a peer's canonical record.
- Runtime varies by session: s039 ran on Codex, s040 to s044 on Claude Code (Opus 5.5). Identify it at boot; explicitly read startup files and do not assume another runtime's memory auto-loads. Technical permissions do not change research, trade, spending or external-send approvals.

## Reading traps and canonical homes
- `LESSONS.md` is the single desk mistake-pattern reference. Do not recreate its rules here. Calibration and source limitations: `thesis/PREDICTIONS_ARCHIVE.md`; original probabilities come from git first appearance.
- Current scope distinctions: `workbook/PANEL_10D_SCHEMA.md` (collection/distribution/filing clocks, BLAST computed age); `research/2026-10-19_L708/VERDICT.md` (corporate/ABS/equity eligibility); `research/2026-10-19_quickwins/READOUT.md` (September extension caveat and Wilmington custody perimeter).
- Both systemic transmission legs remain disconfirmed. Strong fraud/recovery evidence cannot keep a failed funding/bank-contagion thesis alive. Source figures and dates live in STATUS/THESIS.
- Legal scope: confirmed charges are not adjudicated guilt. Keep narrow Tricolor trustee resignation separate from the broader Wilmington-exit allegation; current owner forecast is in PREDICTIONS, not an old memory bullet.

## Tooling — observed coverage, not permanent guarantees
- SEC: `data.sec.gov/submissions` and archive exhibits work with the configured compliant User-Agent. Avoid the previously blocked browse-edgar HTML route. Saved source documents/hash manifests live with each research result.
- Tricolor Ch.7 Verita: October25 verified augmented TLS thenHTTP403; current access unavailable. Historical working recipe is POST `/document/list/6384` with PageSize2000 and the Go Daddy G2 intermediate added to a CA bundle. WebFetch's certificate failure is not absence of the docket. Never disable TLS verification.
- Kroll and CourtListener docket/REST pages were blocked in the9/30 session. CourtListener SEARCH works unauthenticated through DEWEY's read-only `recap_pull.py search`; use the case number and verify document identity. Tricolor trial is a future docket event in the calendar, not the old October2026 date.
- Equifax edition URLs use full month names. A guessed URL404 does not establish a missing edition. OTTO-10 remains NEEDS_VERIFY until the covering September edition, with its12/15 check.
- CourtListener SEARCH API now 401s anonymously (first seen 10/28; worked through 10/25), so DEWEY's `recap_pull.py search` is dead without a token. Working route: per-docket RSS `https://www.courtlistener.com/docket/<id>/feed/` (newest 30 entries only, so older filings can be missed) + public RECAP storage PDFs. Verita POST worked again 10/28 (space retries). Details: WINTERKORN_MEMORY 10/28, ML-OTTO-344.
- `panel_10d.py` has no argparse: `--help` runs a full refresh. Use `--dry-run`.
- M&T official IR direct requests returned403 on10/19, while the web tool read its official deck/quarterly index and SEC supplied the filed release. Official webcast403; third-party transcript is labelled secondary. Do not claim a primary audio read.
- Fitch paid/full index access was declined10/14; no new account or paid-data authority. March aggregate values retired from hot STATUS; deal-level panel is a different instrument, not a replacement Fitch index.
- Cox Manheim pages: `coxautoinc.com/insights/manheim-used-vehicle-value-index-<month>-2026-trends/` and `...-mid-<month>-2026-trends/` all fetched with a browser User-Agent on 11/06, January to October. The old `site.manheim.com` and `/market-insights/` URLs serve stale copies with HTTP 200, so a 200 there is no evidence about the current month.
- The read-cap scanner flags any charter line with the word "read" next to a ledger name; step 3a is worded around it. `corrections_boot_check.py --scope` refuses a semicolon.
- `ledger_staleness.py --nudge` shows 🔴 on SHELF_ACTIVITY because it is both FROZEN and carries an old Cadence line. Nothing is owed; the banner governs.

- Tricolor auction instrument: Holman files a sworn monthly application by the 10th (¶13: vehicles sold, net sale proceeds); trustee's quarterly Form 1 has asset 52. Verita list dates are unpadded (11/6/2026), the POST takes `DocketNumber` alone, a `/tricolor/document/<id>` link sits in each `court-docket` card. `curl -L` the Go Daddy G2 cert (the plain http URL now redirects, leaving an empty file). Running pdfminer over a Holman PDF whole stalls on the vehicle exhibit, so cap `maxpages=9` or Read the page range.
- James memo endorsements can sit in an encoded font: `(cid:N)` decodes as chr(N+29). `pypdfium2` is not in `.venv`; the Read tool renders PDF pages. `shelf_halt_monitor.py` can exceed 60 s under EFTS limits; give it 180 s.

- NY Fed HHDC workbook map (Q3-2026 file): p.3 balances by type; p.8 auto originations by riskscore (<620 bucket is NOT OTTO-10's Equifax share); p.12 share of balance 90+ by type; p.14 flow into 90+ by type, rounded; p.26 auto flow into 90+ by age with an 'all' column, four-quarter sum, full precision. CARL saves the file under `AGENTS/CARL/research/<date>_HHDC_prep/raw/`; a card's cited path can be wrong, so `find` before calling a source missing.
- Verita: `DocketNumber` blank plus a date range lists every entry newest first; the docket number and `/tricolor/document/<id>` link sit in the HTML card above each `Document Name:` block. The G2 cert fetch must be plain `http://` with `-L`; `https://certificates.godaddy.com` fails its own name check.

## LAST SESSION — s044, 2026-11-11 (Claude Code, Opus 5.5), PROME task from prome-2b, D:L133 + catch-up
- Tricolor §341 set for 11/11 not held: continued to Wed 2027-03-17 10:00 CT (Verita Dkt 1496, filed 11/09, PDF read). PROME registered the successor as DOCKET L1121. WALTER drop committed.
- NY Fed Q3 auto flow into 90+ 3.0232%, series high by 2bp; balance $1.734T; non-contradiction passed, 🟡 held. CRMT eleventh bridge to 11/12 (BROCK). James: government opposition ECF 166/167 filed, titles only, no ruling.
- Fed-hike read (ORACLE's odds): touches no OTTO row, band or prediction. ML-375–382 incl. three combo updates. Inbox 2/2. No score, band, gate, threshold or prediction moved. Convergence 32/50.
- Closeout: research retirement scan run (owed since s043): 15 files to `archive/research_retired_2026-11-11/`. STATUS rotated under 70%, originals cold §23. Consumer check's two 🔴 were false (dated WALTER snapshot; unrelated MKC number in a HENRY CSV).

## NEXT SESSION — keep last
1. **11/12:** CRMT relief expiry (BROCK grades) · EART 2026-5 window closes (OTTO-07; combo:funding-cost review) · WINTERKORN due (7 days). **~11/13** Chu suppression check (sealed 11/06 entry). Read James ECF 166/167 bodies.
2. **~11/15 SDT:** run with Manheim +2, record the second observation (expect NO VERDICT); decide then whether to propose a redesign, stated openly, no credit.
3. **11/16–11/21:** First Brands hearings 11/16, 11/17, 11/18; SDART/BLAST October 10-Ds; trustee's first operating report 11/21.
4. **~11/30:** EART October 10-Ds resolve OTTO-36 (PROME's grade deadline 12/04, DOCKET L990), OTTO-34 path; Ares response (OTTO-33); Tricolor sales deadline. **By 12/10:** Holman November application into `HOLMAN_MONTHLY.tsv`.
5. **12/07 Manheim November** (use `MID_TO_FINAL.tsv` before any mid-month forecast). OTTO-10 ~12/15, OTTO-11 STUCK keep their follow-ups. WINTERKORN PENDING: Dkt 1297 Ex. B facility map. Tricolor §341 3/17/27. WQ-531 still limits court negatives.
