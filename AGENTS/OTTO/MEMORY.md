# OTTO MEMORY

**Updated:** 2026-11-06, s043. Boot navigation and continuity; live metrics belong to STATUS/workbooks. Mistake patterns live in boot-read `LESSONS.md`. Prior memory preserved byte-for-byte in `archive/MEMORY_2026-10-19_pre-s031.md`; old entries are history, not pending work.

## Desk boundaries
- OTTO owns auto-fraud mechanisms, collateral evidence and identification of exposed counterparties. REGINALD owns bank sizing; BROCK owns CRMT financing grades and BDC marks; TERRY constructs trades and Will decides.
- Root/desk charter owns routing and evidence conventions. Use WALTER for new signals; a peer's own ask may receive a direct answer, with a parallel WALTER drop for any firing/new dated fact. Never edit a peer's canonical record.
- Runtime varies by session: s039 ran on Codex, s040 to s043 on Claude Code (Opus 5.5). Identify it at boot; explicitly read startup files and do not assume another runtime's memory auto-loads. Technical permissions do not change research, trade, spending or external-send approvals.

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

## LAST SESSION — s043, 2026-11-06 after the close (Claude Code, Opus 5.5), PROME relay of Will's 17:08 ET word
- Close refresh. No score, band, gate, threshold or prediction moved. Convergence 32/50.
- Tricolor auction row refreshed from a May vintage: 9,082 vehicles, $63.09M net through 10/31. Sum ties to the old row at 4/30 to the dollar. Trustee Form 1: $53.78M received at 9/30, $65.0M estimated, ~2,000 cars left. $2.53M gap between the two at 9/30 is unexplained.
- Hertz Q3 10-Q read: 2021-2 $1,000M at 9/30, reason not stated; not fired, not closed. Row's $1,893M was capacity. Routed to LIQUID via WALTER. LIQUID then found OTTO's "extended" left out that all $300M of Class B holders refused (card 051); confirmed at Ex. 10.2, ML-373. Check 12/31: a miss is a scheduled-amortization reset, not the watch's fire.
- James government response due 11/09. Inbox 1/1. Evidence: `research/2026-11-06_close-refresh/READOUT.md`; ML-369–372.

## NEXT SESSION — keep last
1. BROCK CRMT 11/09, James response 11/09 (read the PDF), NY Fed 11/10 (non-contradiction check only; G.19's $1,589.8B is a different perimeter), Tricolor §341 11/11, EART 2026-5 window 11/12, Chu check ~11/13.
2. **~11/15 SDT:** run with Manheim +2, record the second observation (expect NO VERDICT); decide then whether to propose a redesign, stated openly, no credit.
3. **~11/30:** EART October 10-Ds resolve OTTO-36, OTTO-34 path; Ares response (OTTO-33); Tricolor sales deadline. **By 12/10:** Holman November application, add to `HOLMAN_MONTHLY.tsv`.
4. **12/07 Manheim November.** Before any mid-month forecast, use `MID_TO_FINAL.tsv` and add the new pair.
5. WINTERKORN PENDING 11/05: Dkt 1297 Ex. B facility map; WALTER may already hold the Weil wind-down. Hertz item closed by s043. OTTO-10 ~12/15 and OTTO-11 STUCK keep their follow-ups. WQ-531 still limits court negatives.
