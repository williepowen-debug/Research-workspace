# BOND — Run Receipt

**Session:** 2026-07-23 (Thu — boot → general inbox → **auction cluster grade** [Will-tasked, this pass]) · **Overwritten at closeout.**

## ★ Auction cluster (this pass — 3 prints graded vs FROZEN pre-regs)

| Auction | Primary source | BTC | Ind | Dealer | Grade |
|---|---|---:|---:|---:|---|
| 7/22 US 20Y-R (912810UV8) | TD R_20260722_2 | 2.64 | 69.12% | 14.67% | HOLDING (dealer softening flag) |
| 7/22 40Y JGB | MOF eresul20260722 via SAM | 2.83 | — | — | FIRM (BTC-only; tail unpub) |
| 7/23 10Y TIPS (91282CRE3) | TD R_20260723_3 | 2.30 | 65.16% | 9.86% | HOLDING (composition-strong, BTC-borderline; real HY 2.438 = +26.9bp vs 5/21) |

**Full write-up:** `analysis/2026-07-23_grade_7-22-20Y_7-22-40Y-JGB_7-23-TIPS.md`
**KB:** KB-BND-087 (13-col, CRLF via Python)
**VX:** VX-BND-08 refreshed (long-end indirects firm); VX-BND-14 refreshed (TIPS = arm-#2 real-money corroboration)
**STATUS:** state banner + catalyst row updated (both mark 3/3 no-marker)
**Outbox:** none (no 🔴 escalation, no route-out)

---


## Inbox processed (4 consumed → processed/, all classifications integrated)

| File | Action | Why | Workbook rows | STATUS change | Outbox |
|---|---|---|---|---|---|
| `2026-07-16_from-PROME_may-tic-arm3-grade.md` | INTEGRATE | ARM-#3 grade w/ key composition datum (Japan bills real selling) | KB-BND-084; VX-BND-13 note | Catalyst row updated to GRADED FIRED-WEAK; state banner reflects | None (consume-only) |
| `2026-07-18_from-PROME_sat-eve-task-packet.md` | LOG_ONLY | All 4 tasks completed in 7/18 session (SCRATCH confirms: label check, EU reconcile, weld fold, domain-sweep deferred) | None — retrospective | None | None |
| `2026-07-20_from-PROME_zion-call-rate-hike-corroborator.md` | INTEGRATE-light | C-suite corroborator of the real-policy-path label; secondary source, incentive-flagged (asset-sensitive) | KB-BND-085; VX-BND-14 note | Referenced in state banner + VX-14 | None (consume-only per sender) |
| `2026-07-21_from-PROME_rates-vol-channel-confirm.md` | INTEGRATE-light | MOVE re-open 72.66 [7/20] via GATE-VIO-116; adjudicated by VIOLET to fold-into-TRY-FIRE-004, no standalone BOND trade | Folded into KB-BND-083 (7/23 boot) + KB-BND-086 (state refresh) | Dashboard MOVE row updated to 80 [7/23]: 68→72.66→80 trajectory noted | None |

## KB rows appended (this session)
- **KB-BND-084** — May TIC ARM-#3 grade + Japan bills real-selling datum
- **KB-BND-085** — ZION Q2 call policy-path corroborator (with 3 caveats: secondary source, asset-sensitive incentive, verify vs official replay)
- **KB-BND-086** — State refresh 7/17→7/22: 5-day 10Y move decomposition (real 67% / BE 33%), curve still belly-led bear-flattener = SAME regime as KB-BND-080

## VX updated
- **VX-BND-05** (Long-End Duration): fresh readings 10Y 4.67 / 30Y 5.15 / DFII10 2.39; "arm DEEPENED" language; live gates to score 5 enumerated
- **VX-BND-13** (FOI Demand Hole): May TIC composition folded in; mixed-picture read (country-fade REAL, aggregate ABSORBED)
- **VX-BND-14** (Long-end Decomposition): 5-day refresh (real 67% / BE 33%, share down from 86% arm-completing); ZION + Warsh corroborators noted

## STATUS changes
- State banner rewritten (ARM-#2 DEEPENED, fresh dashboard values, ZION + Warsh + Sept-hike 80% context)
- Dashboard rows refreshed: 30Y, 10Y, 2Y, DFII10, ACM TP, T5YIFR, T10YIE, TLT, MOVE
- Catalyst row for 7/16 TIC = ✅ GRADED FIRED-WEAK with datum
- Last-Updated line advanced to 7/23

## Predictions resolved this session
None. BND-01 (HY 350 by end-Jul) remains only OPEN row; in-window till 7/31, currently HY 275 → will NOT resolve TRUE, likely FAILED at 7/31 closeout.

## Deliverables written
- `workbook/KB.tsv` +3 rows (084/085/086)
- `workbook/VX.tsv` — 3 rows edited (05/13/14)
- `STATUS.md` — state banner + 9 dashboard rows + 1 catalyst row
- `SCRATCH.md` — session handoff (this pass)
- `RECEIPT.md` — this file
- 4 inbox files → `processed/` via `git mv`

## Deferred (unchanged from 7/18 SCRATCH)
- HENRY UST structural-demand corpus refresh-or-retire (Mar-vintage; grounds ACM +0.73%) — quiet-day dedicated session
- `PROME/packets/DOMAIN_SWEEP_LENSES.md` sweep — task-3 from 7/18 packet, deferred, still owed

## Git
Session commit will be BOND-only pathspec (`AGENTS/BOND/`), root-cwd, auto-push via `scripts/safe-push.sh`. No writes outside `AGENTS/BOND/`. No outbox routes needed.
