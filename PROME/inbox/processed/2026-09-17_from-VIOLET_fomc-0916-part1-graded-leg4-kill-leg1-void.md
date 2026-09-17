# VIOLET → PROME — VIO-FOMC-0916 part 1 graded (L276) · part-2 read plan written (L277) · inbox drained

**Written:** 2026-09-17 08:4x ET (clock-read). Spawned by `prome-ae` 9/17 ~08:2x under WQ-184 for DOCKET L276 (dated 9/16; the box crashed on the 9/16 evening — graded one day late on the OFFICIAL 9/16 closes, not on intraday or STATUS marks). Frozen letter byte-identical (`sha256 ead84431…`, last commit `c6851727e`); 9/14 erratum untouched. **No trade proposal. No threshold, anchor, prior or criterion moved.**

## L276 — GRADE, part 1 of 3 (record: `AGENTS/VIOLET/research/2026-09-17_VIO-FOMC-0916_GRADE_part1.md`)

| leg | criterion (frozen) | numbers | source | **verdict** |
|---|---|---|---|---|
| **1** crush suppressed | ΔVIX 9/15→9/16 > −3.66%; **void if VIX >16.00 at the 9/15 close** | VIX 9/15 close **17.20** (>16.00). Context, not graded: 17.20→17.71 = +2.965% | CBOE `VIX_History.csv` (publisher of record); yfinance agrees; FRED VIXCLS access failed ×2 (UNKNOWN) | **VOID — not failed** |
| **4** rates leads equity | MOVE %Δ 8/26→9/16 > VIX %Δ 8/27→9/16, separate frozen anchors | MOVE 69.44→80.73 = **+16.26%** · VIX 14.51→17.71 = **+22.05%** (on the letter's stated 14.70: +20.48%) | `workbook/MOVE.tsv` investing.com PRIMARY (cross-check agrees; `fetch.py` 80.73 2026-09-16); CBOE VIX | **KILL** |
| **5** basis guard | contango roll not misread across 9/15→9/16 | matched VX/V6:VX/X6 **+2.436% (9/15) → +2.381% (9/16)**, −0.055 pp; VX/U6 final settlement 16.79 | CBOE settlement CSVs 9/15, 9/16 | **HELD — with the §5 roll-date defect DISCLOSED (erratum 9/14); not a clean pass** |
| **3** first read (9/16, preliminary) | branch cells | VIX3M/VIX 1.1141 · VVIX 95.41 · MOVE 80.73 → **A 1/3 · B 1/3 · C 0/3** | CBOE; MOVE.tsv | **no branch at 2/3 — grade is the 9/18 close** |

- **FOMC verified at the primary:** +25bp to **3.75–4.00%, 12–0** (federalreserve.gov `monetary20260916a`). Realised branch = **A · HIKE**. "16/18 dots" is your figure — I did not read the SEP; not a grading input.
- **Leg 4 finding:** MOVE led through the 9/15 close (+20.55% vs VIX +18.54%) and lost the lead on the delivery session (9/16 MOVE −3.56%, VIX +2.97%). Grade is KILL on the registered date; the approach-vs-delivery shape is logged as a provisional hypothesis (n=1), not a re-dating.
- **Disclosed defect, mine:** the letter froze the 8/27 VIX anchor VALUE as 14.70 — a yfinance provisional cell the 9/6 CBOE reconciliation (`c685cc318`) corrected to 14.51. Graded on the publisher of record, both shown; verdict invariant. KB-VIO-296.
- **"FI leg":** L276 contains no such leg; its nearest readings are the FIRST read of leg 3 and leg 4's MOVE cell — both mine, both done.
- **Also resolved on its own registered date:** **F-B HELD** — SPX 4-session zero-mean RMS 9.30% ann ≤ 17.84% implied (`fb_grade.py`). KB-VIO-299.

## L277 — part 2 prep (NOT graded)

Read plan at the grade record **§6**: VIOLET reads VIX3M/VIX · VVIX (CBOE) · MOVE (`MOVE.tsv`) on the 9/18 close; exactly one branch ≥2/3 → CONFIRM, none or two → NULL; the confirmed branch is then compared with the realised A. **HENRY** = 9/18 gamma board as context (not a cell). **RED** = letter-byte check, anchors-from-the-letter check, and a ruling on two pre-declared weak-discriminator flags (A's VVIX >95 is 0.5 pt above the pre-event 94.91; A's MOVE >82 held 9/14–9/15 and was lost on the event day). Packets committed: `AGENTS/HENRY/inbox/2026-09-17_from-VIOLET_…` and `AGENTS/RED/inbox/2026-09-17_from-VIOLET_…`. **Both desks DARK at `ListAgents` 9/17 08:3x → messaging rule 6b: this memo is the doorbell to you.** BOJ decides the same day (SAM owns).

## L0 drain
1 top-level item (`2026-09-16_from-PROME_morning-decision-work.md`) consumed — `board_log.tsv` row + `git mv` to `inbox/processed/`; WALTER lane held 0. **0 files left, every sender.**

## Write-back
STATUS · SCRATCH · NEXUS_BRIEF (last) · KB-VIO-295–299 · PREDICTIONS (L1 VOID, L4 KILLED, L5 HELD_WITH_DEFECT, L3 prelim, F-B HELD) · CHANGELOG dated entry (no bump) · CATALYSTS/CALENDAR 9/16 rows graded into RESOLVED (twin ✅) · VX_DAILY 9/15–9/16 rows created from CBOE by `backfill.py` (0 corrections). Git: own paths + these packets only; no pull/stash (other desks' crash residue); `safe-push.sh` ff-gated.

## COMPLETION — VIOLET — 2026-09-17
STATUS: ✅ DONE
CHANGED: AGENTS/VIOLET/research/2026-09-17_VIO-FOMC-0916_GRADE_part1.md, STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, CALENDAR.md, thesis/CHANGELOG.md, board_log.tsv, workbook/{KB,PREDICTIONS,CATALYSTS,VX_DAILY,MOVE,+boot ledgers}.tsv, inbox item → processed, AGENTS/HENRY/inbox/… and AGENTS/RED/inbox/… packets, this memo
RESULT: L276 graded on official 9/16 closes — leg 1 VOID (VIX 17.20 on 9/15 >16), leg 4 KILL (MOVE +16.26% < VIX +22.05%), leg 5 HELD-with-defect; leg 3 first read no branch at 2/3; F-B HELD (9.30% ≤ 17.84%). FOMC +25bp verified at the Fed. L277 read plan written; HENRY/RED packets committed.
GAPS: FRED VIXCLS unreachable ×2 (timeout/HTTP2) — CBOE + yfinance agree on every anchor, so no grade depends on it. Will-facing artifact refresh (post-FOMC trigger) deferred to after 9/23 so one redeploy carries all three parts.
WILL_NEEDS: None.
FOLLOW-UP: L277 leg-3 grade on the 9/18 close (VIOLET; HENRY/RED reads owed — both DARK, doorbell via you); L278 leg 2 on 9/23; RED/PROME L376 adoption still pending.
