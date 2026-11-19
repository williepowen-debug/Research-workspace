# OTTO MEMORY

**Updated:** 2026-11-19, s048. Boot navigation and continuity; live metrics belong to STATUS/workbooks. Mistake patterns live in boot-read `LESSONS.md`. Prior memory preserved byte-for-byte in `archive/MEMORY_2026-10-19_pre-s031.md`; old entries are history, not pending work.

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
- CourtListener SEARCH API now 401s anonymously (first seen 10/28; worked through 10/25), so DEWEY's `recap_pull.py search` needs a token: restored 11/11 with PROME's desktop token (DEWEY packet, no token in repo). Working route: per-docket RSS `https://www.courtlistener.com/docket/<id>/feed/` (newest 30 entries only, so older filings can be missed) + public RECAP storage PDFs. Verita POST worked again 10/28 (space retries). Details: WINTERKORN_MEMORY 10/28, ML-OTTO-344.
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

## LAST SESSION — s048, 2026-11-19 (Claude Code, Opus 5.5), PROME wake prome-36, D:L1186 (closed on PROME ask 09:46 ET)
- CRMT thirteenth (11/16 → 11/18) and fourteenth (11/18 → Sun 11/22) bridges, BROCK-graded (KB-BRK-501/519), both 8-Ks re-read by OTTO; V9 held 🔴 4, graded. Tenors shortening (last five avg 3.6 d vs 6.4). ML-395–397. Use the EDGAR submissions JSON, not the browse-edgar atom (lagged 11/19).
- NEXUS_BRIEF rewritten (5 NEXUS findings), pinned to 26e7870651. Charter step 7a now WQ-719 A / WQ-721 A: rewrite the brief only when a figure, threshold, send or wait in it changed; no As-of-only refreshes.
- Inbox 6/6: audit item OTTO-06/-09 answered DISAGREE (already uncounted; THESIS L335 mirror fixed 3/8 → 3/9); KB.tsv 8 rows RETIRED; COR-20261117-02 NO-OP. WINTERKORN ran 11/19 (next due ≥11/26): FB 11/17 under advisement (Dkt 4105), D&O 12/15, Tricolor Chu D&O 12/16. WALTER drop committed.
- s047 (11/16): SDT NO VERDICT; SDART/BLAST Oct 5/5 worse YoY, BROAD gap +0.04; FB sale hearing 12/09. Detail ML-390–394.
- Stamp slip: the PROME packet header said "~09:50 ET" when `date` read ~09:45. Type no clock times; take them from `date` in the same command.

## NEXT SESSION — keep last
1. **Mon 11/23 AM:** if PROME wakes OTTO on BROCK's CRMT grade (relief expiry Sun 11/22), apply the same rule: another short bridge = standstill continues (V9 held); a sale agreement, new money, acceleration or a lender petition changes the case. Silence = ungraded, V9 held.
2. **~11/20** Chu suppression re-check; First Brands 11/17 ruling (under advisement) and Kingsbridge (Dkt 3841) re-check; trustee's operating report 11/21. Read James ECF 166/167/168 bodies when reachable.
3. **~11/30:** EART October 10-Ds resolve OTTO-36 (PROME grade deadline 12/04, DOCKET L990) and test BROAD's turn rule alongside the next SDART/BLAST print (~12/15); EART 2026-5 re-check (OTTO-07 candidate); Ares response (OTTO-33); Tricolor sales deadline. **By 12/10:** Holman November application into `HOLMAN_MONTHLY.tsv`.
4. **12/07 Manheim November** (use `MID_TO_FINAL.tsv` before any mid-month forecast). 12/09 FB sale hearing + Chu final pretrial; 12/15 FB D&O; 12/16 Tricolor Chu D&O. SDT redesign question open (state before ~2027-02, no credit). OTTO-10 ~12/15, OTTO-11 STUCK keep their follow-ups. WQ-678 B deferred trims at a non-bounded session.
