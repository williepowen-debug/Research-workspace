# BOND SCRATCH — 2026-07-23 (Thu, multi-pass: boot → general inbox → auction cluster grade)

## ★ AUCTION CLUSTER GRADED 7/23 EVE (Will-tasked) — 3/3 NO-MARKER

Written up in full: `analysis/2026-07-23_grade_7-22-20Y_7-22-40Y-JGB_7-23-TIPS.md`; KB-BND-087.

| Auction | Print | Grade vs FROZEN pre-reg |
|---|---|---|
| **7/22 US 20Y-R** (912810UV8, TD R_20260722_2) | BTC 2.64 · indirect 69.12% · dealer 14.67% · HY 5.163% | **HOLDING** (dealer 14.67 in 12-15 softening band = flag; indirect 69% firmly HOLDING — rules out foreign-exit; +23.6bp above 6/16 = term-premium priced, not buyer-strike) |
| **7/22 40Y JGB** (MOF eresul20260722 via SAM) | BTC 2.83 · HY 3.865% · coupon 3.8% · tail unpublished | **FIRM** (BOND ≥2.50 bar; SAM concurs firm-marginal on their tighter ≥2.8 bar). **Channel-6 transmission NONE** — per pre-reg §4 LEVEL-vs-MOVE guard: 40Y JGB is a 30Y-LEVEL tell, NOT an arm-driver. Enters VX-05, not VX-14. |
| **7/23 10Y TIPS** (91282CRE3, TD R_20260723_3, new issue) | BTC 2.30 · indirect 65.16% · dealer 9.86% · real HY 2.438% | **HOLDING (composition-strong, BTC-borderline)** — cleared +26.9bp above 5/21 (2.169%) with indirect/dealer ratio **6.6x vs 5/21's 5.5x**. Real-money buying at higher yield with LESS dealer help = **arm-#2 REAL-MONEY CORROBORATED**, DFII10 2.39 level NOT dealer-inventory / NOT fragile. |

**Combined read:** three prints, one story — the higher-for-longer regime is clearing supply at price with the foreign/real-money bid intact. No composition break (all 3 long-end indirects >>50%: 20Y 69, TIPS 65, plus 7/9 30Y 77.7). No cross-channel term-premium blow-out (40Y JGB firm = no export to US 30Y). **Composite unchanged 12/35** — VX-05 stays 4, VX-14 stays 3, both corroborated in-band without upgrade. TIPS is the cleanest arm-#2 real-money corroboration available.

**Tail flag (per BND-08 discipline):** WI-tails unpinnable in-env on both US auctions; MOF publishes no avg yield → 40Y tail unpinnable too. Flagged, immaterial (gating legs already clear).

**Position:** TLT puts HOLD, Will NO-ADD 7/16 stands. No new pre-registered add-gate. Live re-arm candidates unchanged: DFII10 >2.5 sustained (11bp away), FOMC 7/28-29 hawkish guidance-tone, weak coupon in 7/27-28 cluster.

**Escalation:** NONE. No 🔴 route-out.

---


**Purpose:** Ephemeral session handoff. Read at boot, rewritten at closeout. Learnings → `MEMORY.md`; thesis → `thesis/THESIS.md`; live state → `STATUS.md`.

---

## CHANGES SINCE LAST SESSION (7/18 Sat eve → 7/23 Thu mid-day)

**Market state (fresh FRED + yfinance 7/22-7/23):**
- 10Y: 4.57 → **4.67** [7/22 DGS10] / live **4.70** [7/23] (+10-13bp/wk); **20bp above the 4.50 arm line**
- 30Y: 5.09 → **5.15** [7/22]; **27-day run above 5.0 = longest since 2007** (per WALTER SIG-723-012)
- 2Y: 4.16 → **4.31** [7/22] (**+15bp/wk = biggest curve mover = the policy-path lead**)
- DFII10: 2.35 → **2.39** SERIES HIGH [7/22]; **11bp from the 2.5 re-arm gate** (LIVE watch)
- T10YIE: 2.24 → **2.28** [7/23]; T5YIFR: 2.21 → **2.27** [7/23] (drifting toward 2.25 band top, still <2.50 red)
- ^MOVE: 68 → 72.66 [7/20 VIOLET GATE re-open] → **80** [7/23] (+18% two weeks)
- TLT: $83.85 → **$83.17** [7/23]
- CME Sept-hike odds: 52% → **80%** in one week (WALTER SIG-723-012)

**Regime read (unchanged from 7/18 relabel):** SAME regime — real-rate / higher-for-longer POLICY-PATH-LED. Curve still belly-led bear-flattener (2Y +13 > 10Y +12 > 30Y +9 over 7/17→7/22). Decomposition of 5-day 10Y +12bp move = **DFII10 +8bp (67%) + T10YIE +4bp (33%)** — real DOWN from 86% (arm-completing) but still DOMINANT; BE share GROWING (Brent $86+ CPI-path pass-through pricing).

**7/9 30Y auction anomaly (WALTER-flagged):** cleared 5.058% w/ BTC 2.44 no tail = **record yield WITHOUT demand failure** (threshold_vs_mechanism intact). Cuts against a foreign-demand-strike read.

## WHAT I DID THIS SESSION

1. **Boot** (per BOND CLAUDE.md steps 0-7): git pull, STATUS/SCRATCH/MEMORY reads, PREDICTIONS DUE-scan (only BND-01 open, in-window till 7/31), CATALYSTS scan, SCHEMA/VOCABULARIES pre-KB-write. Live FRED + yfinance pulls.
2. **WALTER lane** (4 items, boot step 7): SIG-W-717-011 (gold sub-$4000 mid-escalation, INFO), SIG-W-720-005 (Warsh testimony hawkish, INFO — confirms my read), SIG-W-721-009 (Japan Jun trade miss, INFO — SAM lane), SIG-W-723-012 (rates repricing, ACTION — my domain). Logged one consolidated boot-integration row KB-BND-083, moved all 4 to `WALTER/processed/`.
3. **Boot report to Will** — state delta table + read.
4. **Will tasked: general-inbox processing** — 4 items:
   - `2026-07-16 may-tic-arm3-grade` → INTEGRATE → KB-BND-084 + VX-BND-13 note. Datum: **Japan T-bills −$59.8B REAL selling** (~94% of Japan holdings drop), aggregate foreign LT UST +$53.6B (masked-hole flow-level analog of KB-060).
   - `2026-07-18 sat-eve-task-packet` → LOG_ONLY (all 4 tasks completed in 7/18 session, retrospective consumption).
   - `2026-07-20 zion-call-rate-hike-corroborator` → INTEGRATE-light → KB-BND-085 + VX-BND-14 note (with 3 caveats: secondary source, ZION asset-sensitive incentive, verify vs official replay).
   - `2026-07-21 rates-vol-channel-confirm` → INTEGRATE-light (MOVE 72.66 [7/20], VIOLET adjudicated fold-into-TRY-FIRE-004, no BOND trade; already superseded by KB-BND-083's ^MOVE 80 [7/23]).
5. **STATUS refresh**: state banner + 9 dashboard rows + TIC catalyst row = ✅ GRADED FIRED-WEAK.
6. **VX updates**: VX-BND-05 (long-end DEEPENED, live gates to score 5 enumerated), VX-BND-13 (mixed-picture read), VX-BND-14 (5-day decomposition refresh 67/33).
7. RECEIPT.md rewritten. SCRATCH.md (this file).

## NEXT SESSION (dated, future-verifiable)

1. **Mechanical grades this week (pre-regs frozen):**
   - **7/22 20Y reopening + 40Y JGB** → `setups/2026-07-16_prereg_7-22-20Y_7-23-10YTIPS.md` + `setups/2026-07-18_prereg_7-22-40Y-JGB.md`. **RESULTS PENDING PULL** — did not fetch this session; grade next boot from TreasuryDirect primary (US 20Y CUSIP 912810UV8) + MOF (40Y JGB).
   - **7/23 10Y TIPS (today, later)** — real-money referendum on DFII10 series-high 2.39. Grade off TreasuryDirect primary.
2. **DFII10 2.5 re-arm watch** — 2.39 [7/22], **11bp away**. Live gate to VX-BND-05 → 5.
3. **FOMC 7/28-29** — arm falsifier live test. Hold ~90% priced; **guidance TONE is the event.** Frozen thresholds `analysis/2026-07-18_fed-path-map_fomc-7-28.md`: arm BREAKS on 2Y<3.85 + DFII10<2.15 + 10Y<4.35 sustained (dovish repricing). Currently DEEP-LIT against (2Y 4.31 / DFII10 2.39 / 10Y 4.67).
4. **BND-01 end-of-window resolution** (7/31) — HY OAS 275 vs 350 threshold. Currently FAR from arming; will resolve FAILED.
5. **DEFERRED** (still owed): HENRY UST structural-demand corpus refresh-or-retire (Mar-vintage) — grounds ACM +0.73% level.
6. **DEFERRED** (still owed): `PROME/packets/DOMAIN_SWEEP_LENSES.md` — task-3 from 7/18 packet.
7. **7/27 (Mon) 2Y+5Y same-day + 7/28 7Y** — compressed month-end cluster; indirect-fade trend test (VX-BND-13 → 4 candidate if repeat <60).

## OPEN THREADS / WATCHES

- 🔴 DFII10 → 2.5 (11bp away, live) · 🔴 FOMC 7/28-29 guidance TONE · 🟠 30Y sustain-above-5 (27d and counting) · 🟠 T5YIFR drift 2.21→2.27 (through 2.25 band top) · 🟠 MOF actual FX intervention (FL-BND-11; USDJPY ~162, Japan Jun trade miss adds yen pressure) · 🟢 EU peripheral benign (BTP 83, trigger 200) · 🟡 CCC non-retrace (970)
- 🟡 Verify ZION quotes vs official replay before making load-bearing (KB-BND-085 caveat)

## POSITION DECISIONS

- **TLT puts: HOLD** — arm-#2 already RESOLVED-ARMED (Will NO-ADD 7/16, $500 banked). Arm has DEEPENED, not just held (10Y +12bp/wk to 4.67; DFII10 series high) — but per rule that a resolved-armed decision does not re-open without a NEW pre-registered trigger, no add-fill. Live re-arm candidates:
  - (a) DFII10 >2.5 sustained (11bp away) → automatic re-open per exit rules
  - (b) FOMC 7/28-29 hawkish repricing (guidance TONE) → new gate
  - (c) Weak auction 7/22 20Y or 7/23 TIPS → new gate
- HYG puts: stay closed. HY 275 flat.
- No new BOND trade rec (scoped).

## MAIL STATE

- **Inbox (general):** EMPTY (4 consumed → `processed/`).
- **Inbox WALTER:** EMPTY (4 consumed at boot → `WALTER/processed/`).
- **Outbox:** No new routes this session (all 4 inbox items were consume-only per senders).
- **NEXUS_BRIEF.md:** state banner needs a light refresh to reflect ARM-#2 deepening + DFII10 series-high 2.39; not urgent (framing unchanged, values only). Owed next session.

## CLOSEOUT (this pass — full BOND protocol steps 9-17)

- **9 STATUS:** refreshed (banner + 9 dashboard rows + TIC catalyst row); composite unchanged at 12/35 (no vector score changes — long-end 4 and dealer 3 both hold).
- **10 Workbook + PREDICTIONS:** KB-BND-084/085/086 appended CRLF-preserved via Python (no shell-printf `%` corruption per printf_format finding). PREDICTIONS DUE-scan clean (BND-01 in-window). VX-05/13/14 updated.
- **11 Thesis:** no version bump needed — this session is EVIDENCE ACCUMULATION under the 7/18 v1.1.2 label correction, not a regime change or conviction shift. The deepening of arm-#2 is IN the thesis.
- **12 Forward state:** CATALYSTS.tsv unchanged (TIC row updated in STATUS mirror). No fired rows to prune (7/22 20Y + 7/23 TIPS pending grade next session).
- **13 SCRATCH:** rewritten (this file).
- **14 RECEIPT:** overwritten.
- **15 Promotion scan:** no new auto-memory candidate (KB-BND-086 real 67% / BE 33% is under the existing `finding_curve_shape_policypath_vs_termpremium` lens; the ZION corroborator is a specific datum, not a transferable lesson).
- **16 Mirror-consistency:** THESIS ↔ STATUS dashboard/matrix reads consistent (composite still 12/35, all vectors reconciled to KB rows). PREDICTIONS ↔ STATUS scoreboard: BND-12 FALSE, BND-11 TRUE, BND-01 OPEN (all mirror-clean).
- **17 Git:** BOND-only pathspec, root-cwd, auto-push via safe-push.sh.

## WORKBOOK / PUSH HEALTH

- KB.tsv: 084/085/086 appended (CRLF preserved via Python append, per `finding_printf_format_tsv_append_corruption`). Confirmed via `tail -3 | cut -f1`.
- VX.tsv: 3 rows edited (05/13/14) with Last_Updated = 2026-07-23.
- No commits yet this session; single BOND-scoped commit at closeout, safe-push.sh auto-push.
