# BRENT -> PROME: crash-recovery closeout of the 2026-09-16 cross-war oil reassessment

Date: 2026-09-17 ~08:4x ET. Session: PROME-spawned Tier-1 recovery (`prome-ae`, Claude Code) inside the approved cross-war oil workstream, commission `e4b198a71`. Basis read first: `AGENTS/CATO/runs/2026-09-16_2149_crash-recovery.md`. No trade, band, threshold, confidence or standing approval changed; the commission's BRENT deliverable is closed.

## What was committed (exact paths, from the repo root)

| Commit | Content |
|---|---|
| `9ecfd057b` | 18 paths: the 9 crash-preserved modified files (CLAUDE, SCRATCH, STATUS, TRADE, TRACKER, CATALYSTS, CHANGELOG, THESIS v5.9, BRT-29 note) · 2 untracked research files now tracked (`research/2026-09-16_cross-war-oil/REPORT.md`, `VALIDATION.md`) · `board_log.tsv` +5 receipts · `NEXUS_BRIEF.md` C6 banner · 5 inbox packets `git mv`'d to `inbox/processed/` |
| this memo | `PROME/inbox/2026-09-17_from-BRENT_crash-recovery-closeout.md` (carve-out ①) |

## Validation of intent (task step 1)

- All 9 diffs and both untracked files re-read against HEAD. Every passage is a complete sentence with a matching cross-reference (REPORT ↔ EIA.md ↔ TRADE ↔ STATUS ↔ CHANGELOG agree on: net crude loss UNKNOWN; Branch A on the frozen two-print mean −0.8235M/wk; 165C SCREENSHOT-REPORTED/UNKNOWN; loading-premium inference withdrawn; v5.9 = evidence refinement only). **No passage was mid-edit; no HEAD text was substituted for intended text; nothing invented.**
- **Established and corrected from the record:** SCRATCH claimed "report consumption receipts live in REPORT and board_log", but `board_log.tsv` was clean at HEAD and REPORT.md still read "pins will be recorded after sender commits." The crash cut the session before those writes. Filled now: REPORT § Provenance and consumption (OSPREY `ba3898d86` · FALCON `209a063a4`/`7947d0654` · HAWK `b28680b9e`/`584283c5c` · PROME `e4b198a71`/`7c7b33e8a`), 5 `board_log.tsv` rows stamped `2026-09-17T08:41:07-04:00`, 5 archive moves (moved-file count == ledger-row count).
- **Could not establish from disk, so NOT invented:** the 9/16 `NEXUS_BRIEF.md` write (VALIDATION.md promised a "NEXUS STATUS-head pin at closeout"; the file was untouched at HEAD). Applied the C6 option (b) SCOPED-PARTIAL banner over the 9/15 body — derived only from the committed REPORT/EIA/TRADE — rather than a rewrite. If PROME wants a full brief rewrite, that is a fresh desk session, not recovery.

## HAWK synthesis (task step 2) — consumed, changed nothing

`AGENTS/HAWK/research/2026-09-16_cross-war-oil-review.md` at `b28680b9e` read in full. Its decision summary and event table are row-for-row concordant with REPORT.md (no combined lost-crude total; restart = objective not pumping; products evidence stronger, 3.54M bpd export print a counter-signal; no nameplate pooling; Bab ≠ enforced closure; insurance unmeasured); it pins the same OSPREY/FALCON versions and cites BRENT's `de40a30c8`/`f0a0a2a5c`. **No sentence of REPORT.md changed.** Two HAWK rows (Makhachkala fire; St Helena 9/14 hull incident) have no BRENT counterpart and are recorded as not separately assessed — neither carries a crude-loss quantity. Inbox drained whole: 5 → 0 (OSPREY, FALCON, HAWK, PROME×2); WALTER lane 0.

## Facts carried, not re-derived (task step 3)

L318/L305 Branch A is owner-graded and PROME-consumed (CATALYSTS L318 row annotated). USO Sep-16 165C: expiry date passed 2026-09-16; TRADE.md row now says disposition is Will's hands (WQ-169), sold/expired/assigned NOT inferred. FOMC 9/16 +25bp to 3.75–4.00% carried from PROME's brief. Post-FOMC live check 08:38 ET (named contracts, `fetch.py`): BZX26 $101.62 (−3.98%) — agrees with PROME's 08:2x $101.97 to within intraday drift; CLX26 $94.85; BZF27 $95.07 ⇒ Nov WTI−Brent −$6.77, Nov−Jan +$6.55. Intraday, no registered line crossed, no gate graded. ⚠️ **Instrument note for the fleet:** continuous `BZ=F` printed $98.09 (−7.31%) with contract UNKNOWN — its longName resolves to *Brent Crude Oil Last Day Financial*; a vendor roll artifact, flagged in STATUS/REPORT so nobody reads it as a WTI>Brent flip against tracker line 10.

## Closeout checks (task step 6)

orphan_check BRENT: 0 `[likely YOURS]`; `[not yours]` = CARL/MARCO/BOND/PROME live residue, untouched · claim_check weekday: 5 files clean · read_cap BRENT rc=0 (pre-existing 🟡 TRADE.md 25,027 B = 77% rotate-tier advisory — flag only, not from this session) · corrections_boot_check BRENT: 0 unreceipted · ledger_staleness --nudge: TRADE.md + CATALYSTS.tsv refreshed in-commit; LESSONS_INDEX/INCIDENTS/REGISTRY deliberately untouched (no new lesson, primary-confirmed incident or registration) · consumer_check: not run — no figure superseded this session (the 9/16 session's Cushing/COT scans are recorded in VALIDATION.md) · calendar re-rendered `--write`, view unchanged beyond the 9/16 row. **Not touched:** CARL/VIOLET/HAWK/BOND/MARCO dirty paths, `PROME/state/ORCH_LOG.tsv`. No pull, no stash, no `--amend`, no `reset`.

## Push

`scripts/safe-push.sh` runs immediately after this memo's commit; the receipt line (or a non-ff abort) is reported in the SendMessage to `prome-ae`, not here. At memo time: `master...origin/master [ahead 2]` on a fresh fetch — `cc84d10ed` (PROME's, unpushed at spawn) + `9ecfd057b`.

## COMPLETION — BRENT — 2026-09-17
STATUS: ✅ DONE
CHANGED: AGENTS/BRENT/{CLAUDE,SCRATCH,STATUS,TRADE,NEXUS_BRIEF}.md, board_log.tsv (+5), demand_destruction/TRACKER.md, docket/CATALYSTS.tsv, thesis/{THESIS,CHANGELOG}.md, thesis/prediction_notes/BRT-29.md, research/2026-09-16_cross-war-oil/{REPORT,VALIDATION}.md (new), inbox/processed/ (5 moves), this memo
RESULT: Crash-preserved 9/16 reassessment committed intact in 1 exact-path commit (9ecfd057b, 18 paths) with sender pins for 5 inputs filled, 5 board_log receipts, inbox 5→0. HAWK synthesis b28680b9e consumed: concordant, 0 sentences of REPORT.md changed. Thesis v5.9 = evidence refinement; 0 probability/band/threshold/approval changes.
GAPS: 9/16 NEXUS_BRIEF write was never on disk — replaced by a C6 SCOPED-PARTIAL banner, not a rewrite (a rewrite is a fresh desk session). TRADE.md at 77% read budget is a pre-existing rotate-tier flag, not addressed (out of recovery scope).
WILL_NEEDS: None new — USO Sep-16 165C disposition already sits at WQ-169.
FOLLOW-UP: Sep 17–18 Saudi resolver/WQ-234 window and Fri 9/18 rigs+COT (COT as-of 9/15) remain on the existing docket — unchanged. WQ-249 closeout ask: BRENT is idle after delivery and answers on receipt.
