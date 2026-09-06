# Codex — review of the 9/6 FT-10 / VX_DAILY ledger repair (relayed by Will, Sun 2026-09-06 ~10:5x ET)

**Filed verbatim by PROME (`prome-04`, LAPTOP) 10:5x ET; verification ledger + PROME assessment follow.** Routing: VIOLET packet (two fixes + the holiday reframe) · DAEDALUS packet correction (holiday = session-semantics question) · WQ-188 (VIOLET session order, Will's call) · L294 scope (a third shape: a repair that fails OPEN on its reference source).

---

## Codex, verbatim

> • My assessment: the ledger repair is genuine progress, and PROME's fallback was reasonable for FT-10—but "reconciled today" does not yet mean the data path is reliably protected. I found one reproducible failure worth fixing.
>
> ### The immediate decision is partly superseded
>
> Newer records say you have arranged for RED to run Tuesday and cover Wednesday's close. RED's memo has also arrived, and RED has explicitly ruled Labor Day a non-session that does not break the count. That is recorded in RED's subsequent delivery (Research-workspace/PROME/inbox/processed/2026-09-06_from-RED_ft10-labor-day-ruled-non-session-count-basis-on-the-card-and-a-weight-move-on-the-nfp-retraction.md).
>
> If that arrangement reflects your intentions, there is no need to open VIOLET Tuesday solely to duplicate FT-10 grading. Keep PROME's existing fallback as backup.
>
> I independently fetched CBOE's data: September 3 was 150.63, September 4 151.58. Therefore 2-of-4 is correct; Tuesday can extend to three or reset to zero. Wednesday's close is the earliest qualifying fourth observation, provided both qualify. CBOE SKEW history
>
> One operational distinction matters: being awake Wednesday morning does not cover Wednesday's closing observation. Grade after that dated bar is actually published; do not equate a failed fetch with a below-threshold observation.
>
> ### What genuinely improved
>
> I compared the repaired ledger against fresh downloads of all six CBOE series. All six spot columns match within the script's stated tolerance across the 416-row window, January 8, 2025–September 4, 2026. The four omitted dates are restored.
>
> That is substantial evidence of correction at the canonical artifact—not merely a receipt or agreement between agents. Repaired ledger (Research-workspace/AGENTS/VIOLET/workbook/VX_DAILY.tsv), CBOE historical data
>
> But the scope is agreement with CBOE's current historical files. It does not establish what each file contained when an earlier decision was made, or whether every downstream conclusion has been reconsidered. RED's grading basis explicitly recognizes that vintage limitation (Research-workspace/AGENTS/RED/research/2026-09-02_FT10_GRADING_BASIS_DECLARED.md:64).
>
> ### Three issues deserve attention
>
> 1. HIGH — the repair script can undo its own correction on a source failure.
>
> The current sequence writes Yahoo values into memory first, reconciles against CBOE second, then saves. A CBOE HTTP failure does not prevent saving or a successful exit. Backfill execution path (Research-workspace/AGENTS/VIOLET/scripts/backfill.py:429)
>
> I tested the actual functions with mocked inputs and output, entirely in memory:
>
> - Starting SKEW: 151.58, already marked SETTLE.
> - Hypothetical Yahoo disagreement: 149.00.
> - CBOE returns HTTP 503, either for SKEW alone or all six series.
> - Both cases would save 149.00, retain SETTLE, and return success.
>
> This demonstrates exposure, not an observed production incident.
>
> The simplest fix is to remove Yahoo's write authority over these six canonical columns. CBOE failure should preserve previously verified values and report an incomplete refresh. Yahoo can remain a provisional comparison source. No new monitoring layer is needed.
>
> 2. MEDIUM — "holiday print" has been promoted too quickly into "publisher defect."
>
> The thirteen VIX-only dates are real. Their classification as erroneous "phantoms" is not established.
>
> CBOE's methodology explicitly calculates VIX during global trading hours, and its holiday schedule includes global sessions on days without regular trading. That supplies a plausible legitimate explanation for holiday observations. VIX methodology, §4, CBOE holiday hours
>
> My inference: this may be a session-definition mismatch, not bad source data. I have not established the provenance of every holiday row.
>
> Excluding those dates from a regular-session comparison ledger can be appropriate. Teaching the fleet "orphan VIX = erroneous print" is premature. This is exactly where the system must distinguish detecting an inconsistency from correctly diagnosing it.
>
> 3. MEDIUM — the live consumer remains separate from the repaired ledger.
>
> VIOLET subsequently disclosed that cheap_tail.py still fetches fresh Yahoo data—including SKEW—directly. I verified that at the runtime read (Research-workspace/AGENTS/VIOLET/scripts/cheap_tail.py:86).
>
> Consequently, repairing VX_DAILY.tsv does not protect the live cheap-tail decision surface. VIOLET deserves credit for identifying and explicitly leaving this open. Reconcile that runtime path before relying on its next actionable output; do not require another broad sweep first.
>
> ### What I would tell PROME
>
> > Tuesday coverage appears resolved through RED; retain the fallback as backup. The ledger reconciliation is verified and valuable. Prioritize preventing source-failure overwrites and closing the already-identified cheap-tail runtime exposure. Treat the holiday finding as a session-semantics question until verified, not a confirmed CBOE defect. Keep the September 13 review date unless a live decision requires it sooner.
>
> Overall: better correction quality, but incomplete prevention and downstream protection. The highest-value next step is removing the competing writer—not adding another checker.

---

## PROME verification ledger (five-field; Class 13 tokens)

| # | Claim | Artifact | Check | Observed | Disposition |
|---|---|---|---|---|---|
| 1 | RED ruled Labor Day a non-session; RED runs Tuesday and covers the 9/9 close | `PROME/inbox/processed/2026-09-06_from-RED_ft10-labor-day-ruled-…md` + RED's 10:4x message | read at consume 10:4x | Ruling on the card (36/36 years; ~1 gap per 900 sessions); *"Will confirmed in-session he is running RED on Tue 9/8"* | **VERIFIED** (ruling) · **RELAYED** (the Tuesday session — RED's report of Will's word, not PROME-verified) |
| 2 | ^SKEW 150.63 [9/3] · 151.58 [9/4] | CBOE `SKEW_History.csv` | WALTER 9/5 · VIOLET 9/6 · RED 9/6 · Codex 9/6, all own pulls | four independent pulls agree to the hundredth | **VERIFIED** (by others' pulls; PROME has not fetched — none needed) |
| 3 | **HIGH:** `backfill.py` writes Yahoo first, reconciles second, saves and exits 0 on a CBOE failure | `AGENTS/VIOLET/scripts/backfill.py` `main()` :419–450 · `backfill_spot_cboe` :310–416 · `fetch_cboe_history` :285–308 | `sed -n 400,470p` + grep, 10:5x | `backfill_spot(args.spot_days, rows)` (yfinance → rows) → `backfill_spot_cboe(rows)`; :358 prints *"✗ CBOE VIX history unavailable — CBOE pass SKIPPED (yfinance stands)"*; per-series failure returns `{}` (:286 *"Empty dict on any failure"*) so that column is silently left to yfinance; then `write_merged(header, rows)` and `return 0` | **VERIFIED at the code path** (Codex's mocked runs not re-run by PROME; the path they describe is the one in the file) |
| 4 | RED's basis declares the vintage limitation | `AGENTS/RED/research/2026-09-02_FT10_GRADING_BASIS_DECLARED.md:64` | `sed -n 64p` | §4 VINTAGE: *"SKEW_History.csv is a rewritten-daily file carrying the CURRENT value for every historical date — not a vintage archive"* | **VERIFIED** |
| 5 | `cheap_tail.py` fetches ^VIX/^VVIX/^SKEW fresh from yfinance at run time (Codex :86, VIOLET :92) | `AGENTS/VIOLET/scripts/cheap_tail.py` `pull()` :86–92 | `sed -n 80,95p` | `def pull()` :86 → `yf.Ticker("^SKEW").history(...)` :92; VIOLET SCRATCH item 3 = *"fix this first among the builds"* | **VERIFIED** (both line cites right; VIOLET already queued it; the backfill fail-open is NOT in VIOLET's queue — new) |
| 6 | CBOE computes VIX during Global Trading Hours and its holiday schedule includes GTH sessions on days without regular trading — a legitimate source of holiday VIX rows | CBOE VIX methodology §4 + CBOE holiday hours (not fetched by PROME) | none this pass | plausible mechanism; provenance of each of the 13 rows not established by anyone yet | **INFERRED** — a diagnosis question, not a defect finding |

## PROME assessment (10:5x ET)

- **Agree with all three, and with the order.** ① is the one that can silently undo today's repair the first time CBOE's CDN 503s — the same shape as VIOLET's guard inversion and RED's boot script this morning: a correctly declared reference (CBOE wins) with a fail-OPEN path around it. The fix Codex names is the right one because it removes a WRITER rather than adding a checker (the fleet's own lesson from WQ-140/L294: checks that only print get overridden). ② is a correction to PROME's own packet framing — I sent DAEDALUS "phantom-holiday VIX = CBOE's own" this morning; that promoted a detected inconsistency into a diagnosed defect. The exclusion rule VIOLET built (orphan VIX row, five companions absent ⇒ exclude from a regular-session ledger) stays useful as a session filter; the label "erroneous print" does not, until someone reads CBOE's holiday GTH schedule against the 13 dates. ③ is already in TERRY's inbox as a caveat and in VIOLET's queue as item 3; Codex's addition is sequencing — close it before the window's next actionable output, which lands inside CPI week.
- **On the vintage limit (Codex's caveat on "what genuinely improved"):** correct and already declared by RED (basis §4): reconciliation to CBOE's current file proves the ledger agrees with CBOE NOW; it cannot prove what any earlier grade read. RED's rule — record the grade on the day it is read — is the only defence, and it is why the FT-10 count is graded on the published bar the morning after, not on a fetch.
- **On Tuesday/Wednesday:** RED's Tuesday session is RELAYED; PROME keeps the L0 pre-fetch as backstop. Codex's operational point stands and goes on the operator card: the 9/9 close publishes in the 9/10 file — "live for the 9/9 close" means graded 9/10 morning at the earliest, and a failed fetch is UNKNOWN, never a sub-150 bar.
- **What PROME does with it:** VIOLET packet (both fixes, the reframe, the sequencing) · DAEDALUS packet corrected · WQ-188 to Will: VIOLET's next session is Will-designated for the thesis read; the two fixes are ~30 minutes of builds inside this morning's Will-directed backfill workstream — PROME can spawn them Tier 1 today (follow-up, same direction) or Will's session runs fixes-then-thesis. Rec: PROME spawns today; the exposure sits on a live 4/4 window into CPI.
