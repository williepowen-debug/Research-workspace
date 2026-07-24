# BOND SCRATCH — 2026-07-23 (Thu, multi-pass session — CLOSED OUT)

**Purpose:** Ephemeral session handoff. Read at boot, rewritten at closeout. Learnings → `MEMORY.md`; thesis → `thesis/THESIS.md`; live state → `STATUS.md`.

**Session shape:** boot → WALTER lane → Will-tasked general inbox → Will-tasked auction grade → Will-tasked research-verified HEN-42 reply v2 → CLOSEOUT.

---

## CHANGES SINCE LAST SESSION (7/18 Sat eve → 7/23 Thu closeout)

**Market state (fresh FRED + yfinance 7/22-7/23):**
- 10Y: 4.57 → **4.67** [7/22] / live **4.70** [7/23] — **20bp above the 4.50 arm line**
- 30Y: 5.09 → **5.15** [7/22] — 27-day run above 5.0 = longest since 2007
- 2Y: 4.16 → **4.31** [7/22] — biggest curve mover = policy-path lead
- **Full real curve 7/17→7/22 belly-led on its own:** DFII5 +10 > DFII7 +9 > DFII10 +8 > DFII20 +6 = DFII30 +6 → **direct evidence AGAINST term-premium expansion** (KB-BND-088)
- Full nominal curve 7/17→7/22: DGS2 +13 = DGS5 +13 = DGS7 +13 > DGS10 +12 > DGS20 +10 > DGS30 +9 = textbook belly-led bear-flattener
- Breakevens moved parallel +3-4bp across curve = ambient shift, no term-structure signal
- DFII10: 2.35 → **2.39** SERIES HIGH — **11bp from the 2.5 re-arm gate** (LIVE watch)
- T5YIFR: 2.21 → **2.27** [7/23], drifting toward 2.25 band top; well below 2.50 red
- ^MOVE: 68 → 72.66 [7/20] → **80** [7/23] (+18% two weeks)
- TLT: $83.85 → **$83.17** [7/23]
- CME Sept-hike odds: 52% → **80%** in one week (WALTER SIG-723-012)
- USDJPY: **163.83** [7/23 SAM] fresh 40-yr low, ORDERLY (SAM ARMED-not-FIRED); Brent **$100.43** through the line (BRENT owns)

**Regime read (hardened from 7/18):** SAME regime — real-rate / higher-for-longer POLICY-PATH-LED. Real-curve belly-led on its own → the label correction (KB-BND-080) is now empirically verified by full-curve real-yield data, not just inferred from nominal shape. Real contribution by tenor: 5Y 77% / 10Y 67% / 20Y 60% / 30Y 67% — real dominant everywhere AND belly-led = ~90-95% policy-path with the ~5-10% margin auction-idiosyncratic (20Y-R dealer 14.67%), NOT systemic term-premium.

---

## WHAT I DID THIS SESSION (multi-pass)

**Pass 1 — Boot (per BOND CLAUDE.md steps 0-7):**
- git pull, STATUS/SCRATCH/MEMORY reads, PREDICTIONS DUE-scan (only BND-01 open, in-window till 7/31), CATALYSTS scan, SCHEMA/VOCABULARIES pre-KB.
- **WALTER lane (4 items):** SIG-W-717-011 (gold sub-$4000 mid-escalation, INFO), SIG-W-720-005 (Warsh testimony hawkish, INFO — confirms my read), SIG-W-721-009 (Japan Jun trade miss, INFO — SAM lane), SIG-W-723-012 (rates repricing, ACTION — my domain). Consolidated boot-integration row **KB-BND-083**, all 4 moved to `WALTER/processed/`.
- Boot report to Will with state-delta table.

**Pass 2 — Will-tasked: general-inbox processing (4 items):**
- `2026-07-16 may-tic-arm3-grade` → INTEGRATE → **KB-BND-084** + VX-BND-13 note. Key datum: Japan T-bills −$59.8B REAL selling (~94% of Japan holdings drop), aggregate foreign LT UST +$53.6B (masked-hole flow-level analog of KB-060).
- `2026-07-18 sat-eve-task-packet` → LOG_ONLY (all 4 tasks completed in 7/18 session).
- `2026-07-20 zion-call-rate-hike-corroborator` → INTEGRATE-light → **KB-BND-085** + VX-BND-14 note (3 caveats: secondary source, ZION asset-sensitive incentive, verify vs official replay).
- `2026-07-21 rates-vol-channel-confirm` → INTEGRATE-light (folded into KB-BND-083; superseded by ^MOVE 80 [7/23]).
- Fresh FRED pull → **KB-BND-086** state-refresh with 5-day decomposition (real 67% / BE 33%).
- STATUS dashboard refresh (9 rows + TIC catalyst).
- **Process incident (self-caught, fixed):** initial commit swept in HENRY's pre-staged files (concurrent-commit-index-race per `finding_concurrent_commit_index_race`). Soft-reset undid it; pathspec-recommit was clean BOND-only (commit `10ddecd6`); HENRY's staged renames stayed untouched.

**Pass 3 — Will-tasked: auction cluster grade (7/22-23):**
- Pulled TreasuryDirect TA_WS API for **7/22 US 20Y-R** (R_20260722_2) + **7/23 10Y TIPS** (R_20260723_3).
- **40Y JGB via SAM** (MOF eresul20260722 in SAM STATUS 7/23 boot note; my in-env MOF fetch 404'd on EN calendar URL).
- Graded all 3 vs FROZEN pre-regs → **3/3 NO-MARKER** (full write-up `analysis/2026-07-23_grade_7-22-20Y_7-22-40Y-JGB_7-23-TIPS.md`; **KB-BND-087**).
- STATUS + VX-BND-05/08/14 refreshed.
- **HENRY inbox item landed mid-session** (`from-HENRY_HEN-42-policy-path-rotation-your-auctions-are-the-discriminator`) → wrote initial reply v1 → committed `44726880`.

**Pass 4 — Will-tasked: research then reply to HENRY (v2):**
- Pulled full FRED curve 7/17→7/22 across DFII5/7/10/20/30 + DGS2/5/7/10/20/30.
- Cross-checked LIQUID KB-LIQ-086 for independence-test.
- Verified fleet auto-memory `finding_curve_shape_policypath_vs_termpremium` says what I attributed.
- **Rewrote outbox v2 in place** (same filename per artifact-redeploy discipline; v1 preserved in git `44726880`).
- **KB-BND-088** documenting the research findings; VX-BND-14 refreshed with full-curve evidence.
- Two verdict revisions: (a) 85/15 → ~90-95% policy-path (real curve itself belly-led = direct evidence, not inference); (b) "3-way convergence" → really 2-way (LIQUID uses SAME FRED curve + SAME discriminator = NOT orthogonal to HENRY; honest count is 2 routes + 1 shared-antecedent reading).

**Pass 5 — Closeout (this pass):**
- CATALYSTS.tsv pruned (8 fired rows removed from STATUS table + TSV cleaned; kept 7/2 FR2004 as PENDING-pull tracker + 7/22-23 as freshly-resolved).
- STATUS refreshed for stale JGB/USDJPY/Brent rows (cited SAM + BRENT with domain-owner attribution per fleet convention).
- SCRATCH (this file) + RECEIPT rewritten.

---

## NEXT SESSION (dated, future-verifiable)

1. **Mon 7/27 2Y+5Y (same day) + Tue 7/28 7Y** — THE most consequential upcoming test. Both HENRY's HEN-42 discriminator AND BOND's own falsifier gate for the CONFIRM I just delivered:
   - **HEN-42 CONFIRM if:** clean stops with front-end still leading (belly indirect stays firm, no 2Y outright tail)
   - **HEN-42 DENY if:** tail at the belly, esp. w/ indirect fade extending the June-cluster (VX-13 → 4 candidate)
   - **BOND's falsifier for CONFIRM:** belly ind <55% AND 2Y outright TAIL >2bp AND dealer >18% → re-open term-premium tilt
   - Pre-pull 7/26 (Sun eve) if PROME hasn't already loaded the pre-reg
2. **FOMC 7/28-29** — arm-#2 falsifier live test. Hold ~90% priced; **guidance TONE is the event.** Frozen thresholds `analysis/2026-07-18_fed-path-map_fomc-7-28.md`: arm BREAKS on 2Y<3.85 + DFII10<2.15 + 10Y<4.35 sustained.
3. **DFII10 2.5 re-arm watch** — 2.39 [7/22], **11bp away**. Live gate to VX-BND-05 → 5.
4. **BOJ 7/31** — FL-BND-11 FX leg; SAM owns primary.
5. **BND-01 end-of-window resolution** (7/31) — HY OAS 275 vs 350. Currently far from arming; will resolve FAILED.
6. **DEFERRED (still owed):** FR2004 as-of 6/24/7/1/7/8/7/15 prints (NY Fed API caps pre-2026 in-env — needs a workaround or Will/PROME flag); HENRY UST structural-demand corpus refresh (Mar-vintage); `PROME/packets/DOMAIN_SWEEP_LENSES.md` sweep.
7. **NEXUS_BRIEF light refresh** — carry the KB-BND-088 curve-shape data-verified verdict (v2 HEN-42 reply hardening); values-only, framing unchanged.

## OPEN THREADS / WATCHES

- 🔴 DFII10 → 2.5 (11bp away, LIVE) · 🔴 FOMC 7/28-29 guidance TONE · 🔴 7/27-28 auction cluster (HEN-42 + BOND falsifier)
- 🟠 30Y sustain-above-5 (27d and counting) · 🟠 T5YIFR drift 2.21→2.27 (through 2.25 band top) · 🟠 MOF actual FX intervention (USDJPY 163.83, 165 = next MOF line)
- 🟢 EU peripheral benign (BTP 83, trigger 200) · 🟡 CCC non-retrace (970)
- 🟡 Verify ZION quotes vs official replay before making load-bearing (KB-BND-085 caveat)
- 🟡 FR2004 in-env access — 4 prints owed, primary API not reaching 2026 data

## POSITION DECISIONS

- **TLT puts: HOLD** — arm-#2 RESOLVED-ARMED (Will NO-ADD 7/16 stands; $500 banked). Arm has DEEPENED (10Y +12bp/wk to 4.67; DFII10 series high) BUT no new pre-registered add-gate has fired. Live re-arm candidates:
  - (a) DFII10 >2.5 sustained (11bp away)
  - (b) FOMC 7/28-29 hawkish repricing on guidance TONE
  - (c) Weak coupon in 7/27-28 cluster (2Y+5Y+7Y)
- HYG puts: stay closed. HY 275 flat.
- No new BOND trade rec (scoped).

## MAIL STATE

- **Inbox (general):** EMPTY (5 total consumed this session → `processed/`: 4 PROME items in pass 2, 1 HENRY item in pass 3).
- **Inbox WALTER:** EMPTY (4 consumed at boot → `WALTER/processed/`).
- **Outbox:** 1 new — `2026-07-23_to-HENRY_HEN-42-confirm-with-caveat.md` (v2 data-verified; v1 preserved in git 44726880).
- **NEXUS_BRIEF.md:** light-refresh owed next session (KB-BND-088 hardens the label correction).

## CLOSEOUT (this pass — full BOND protocol steps 9-17)

- **9 STATUS:** refreshed (banner + 9 dashboard rows + TIC/auction catalyst rows + calendar pruned + 3 stale rows domain-owner-attribution refreshed). Composite unchanged at **12/35** (VX-05 stays 4, VX-14 stays 3, both corroborated in-band).
- **10 Workbook + PREDICTIONS:** 6 KB rows appended this session (083 boot / 084 TIC / 085 ZION / 086 state-refresh / 087 auction grades / 088 full-curve research); CRLF-preserved via Python (no shell-printf `%` corruption). VX-05/08/13/14 updated (4 rows). PREDICTIONS DUE-scan clean at close (BND-01 in-window till 7/31; will resolve FAILED at 7/31 close).
- **11 Thesis:** no version bump — this session is evidence ACCUMULATION under v1.1.2 (7/18 label correction). The full-curve real-yield-belly-led evidence (KB-BND-088) hardens v1.1.2 empirically; a v1.1.3 doc-update to CHANGELOG on next session would be appropriate but not urgent.
- **12 Forward state:** CATALYSTS.tsv pruned (removed 8 fired rows: 7/2 sizes announcement, 7/5 OPEC+, 7/7-9 refunding, 7/8 minutes, 7/10 ARM-#2 leg, 7/13 ARM-#2 close, 7/14 CPI, 7/15 PPI); kept 7/22-23 with resolution marker (prune ~7/30); 7/2 FR2004 kept as PENDING-pull tracker. STATUS calendar mirrored.
- **13 SCRATCH:** rewritten (this file).
- **14 RECEIPT:** overwritten.
- **15 Promotion scan:** no new auto-memory promotion — the independence-test lesson from pass 4 is exactly what `finding_shared_antecedent_independence_test` already covers (cited in v2 reply); the full-curve real-yield-belly-led evidence is a specific instance of `finding_curve_shape_policypath_vs_termpremium` (also cited).
- **16 Mirror-consistency check:** THESIS ↔ STATUS dashboard/matrix consistent (composite 12/35, all vectors reconciled to KB rows). PREDICTIONS ↔ STATUS scoreboard: BND-11 TRUE, BND-12 FALSE, BND-01 OPEN (all mirror-clean). Full-curve KB-BND-088 findings mirrored into VX-BND-14 notes.
- **17 Git:** BOND-only pathspec commits this closeout, root-cwd, auto-push via `scripts/safe-push.sh`.

## WORKBOOK / PUSH HEALTH

- KB.tsv: 6 rows appended session-total (083-088), CRLF preserved via Python append. Confirmed via `tail | cut -f1`.
- VX.tsv: 4 rows edited (05/08/13/14) with Last_Updated = 2026-07-23.
- **Commits this session:** `10ddecd6` (inbox drain), `44726880` (auction grades + HEN-42 v1), `5f30b542` (HEN-42 v2 + full-curve research), + this closeout commit. All BOND-only pathspec. Bad first commit swept HENRY files → soft-reset + re-committed clean (single incident, caught + fixed same turn).
- safe-push ff-gated, non-ff → pull --rebase (already fast-forwarded twice this session behind concurrent LIQUID commits).
