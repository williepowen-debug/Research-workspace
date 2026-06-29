# BRENT SCRATCH — Mon Jun 29, 2026 (full session: kinetic test → THESIS v5.0 asymmetry-flip → TRADE.md migration)

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

**Session arc (long, multi-turn with Will):** Boot + WALTER drain → reconciled PROME's HOLDS grade + my own pre-reg (`PREREG_20260628`, resolved HOLDS) + HAWK marks (B20/C44/D36) → answered Will's stress-test (SPR/buffer whipsaw, Russia, Hormuz timeline) which **tightened the race** → **executed THESIS v4.4→v5.0 (MAJOR — asymmetry flip to upside-convex; Will chose "Option A")** → **migrated the trade surface to `TRADE.md`** (rewrote the 3-mo-stale Mar version; folded in the convex-arm plan; trimmed STATUS) → completeness pass on TRADE.md. **All committed + pushed** (HEAD 07be21de; git 0/0).

---

## ⚡ NEXT BOOT FIRST MOVES
1. 🔴 **Wed Jul 1 — EIA WPSR (wk-6/26)** — Cushing trajectory: does an **import surge** show up (reopening delivering = race read) or keep draining? + **RESOLVE BRT-08** (gasoline −5% YoY window closed Jun-30) using the still-PENDING datapoint #3 (WGFUPUS2 wk-6/19) + clear WPULEUS3 util. This is a real prediction resolution due — don't leave OPEN-stale.
2. 🔴 **Fri Jul 3 — CFTC COT (Jun-30 data)** — kinetic-week read: short-COVERING (Tier-2 convex-arm lean) vs continued LIQUIDATION (structural holds). Re-pull main ICE Brent net too.
3. 🔴 **~Jul 3 — SPR 172M auth fully withdrawn → DOE re-auth decision** — the buffer-clock deadline.
4. 🔴 **Wed Jul 8 — EIA STEO (July)** — first post-deal price path.
5. 🟠 **CHASE HAWK on HAW-15** (crude-export pivot) — its ledger is Jun-26 (stale on a fast front); the 2026 campaign is trending to export infra (Primorsk/Ust-Luga/Novorossiysk). A confirmed pivot = a **Tier-1 convex-arm trigger**. Also track the reopening 2nd-derivative (P&I resumption / liners-off-Cape / transit durability).

## CHANGES SINCE LAST SESSION (Jun 26 → Jun 29)
- **Jun 27-28 US↔Iran kinetic exchange** (US strikes Iranian military sites; Iran missiles at Kuwait/Bahrain bases; **VLCC Kiku struck by Iranian UAV Jun 27** [CONF web]) = the pre-registered coiled-spring flip-up trigger, fired in full. **Brent FELL to a ~$72 4-mo low instead of snapping** → STRUCTURAL confirmed behaviorally (P 0.63→0.70). Now **$73.53**.
- **Reopening reality is slower than the 75% headline:** weeks-to-MONTHS (Pentagon demining ≤6mo), transit recovery spike-then-fade (HAWK 71→3/day), verified legs (P&I/liners/JWC) still ~0-1/4.
- **Russia = PRODUCT story** (refining 16-yr low, shortages 25+ regions) → crude soft-bearish (freed exports); BUT two rising **bullish-crude** fuses (HAW-15 export-pivot trend, storage saturation).

## WHAT I DID THIS SESSION
- **THESIS v5.0 (MAJOR — asymmetry flip):** risk-skew flipped to **UPSIDE-CONVEX** (positioning reversal, NOT a price-forecast reversal — central forecast stays neutral). Phase-2-short bias RETIRED; two-phase reframe (dominant medium-term risk re-rotated to a **Phase-1 RE-SQUEEZE**, not Phase-2 demand-down); "<$75 = thesis break" RETIRED (=decoupling); thresholds → upside re-arm + <$70-on-demand; risk-factors re-weighted to price-outcome skew. Steelman held in CHANGELOG. **Guardrail: skew flip, not "oil up."**
- **TRADE.md is now the live trade surface** (was 3-mo-stale Mar vintage). Holds positions + the **v5.0 convex-arm plan** (Will's recs: **USO call spread / ~$500 max-loss / pre-negotiated-proposal authority**), tiered triggers, disarm/horizon, the dormant/conditional Phase-2 short, decisions-on-record, cross-agent table, catalyst watch. Trade content pulled OUT of STATUS (1-line pointer). Wired into boot/closeout so it won't re-rot.
- **Earlier today:** drained 5 WALTER sigs → processed; reconciled PROME's HOLDS grade + closed the `PREREG_20260628` loop (RESOLVED HOLDS) + folded in HAWK's B20/C44/D36 marks.

## OPEN THREADS / WATCHES
- 🔴 **The TIMED RACE (tightened):** deficit-closing (reopening + replacement barrels) vs buffer-exhaustion. Near-term (1-2wk) robust = 0.70 hold; **medium-term (1-3mo) up-whipsaw ≈ coin-flip vs gentle-normalization** (Will's stress-test raised it). Leading tells (price lags): reopening 2nd-derivative, P&I resumption, HAW-15, floating-storage builds.
- 🟡 **Convex arm = ARMED, no capital deployed.** Fires on Tier-1 (HAW-15 pivot / reopening-stalls-while-buffers-empty) or Tier-2 (Brent >$75 ×2 closes / durable collapse). Full plan: `TRADE.md`. Will [Approve] at fire.
- 🟡 **Trigger #2 datapoint #3** (gasoline wk-6/19 WGFUPUS2) + util Jun-19 STILL pending since Jun-24 → both feed BRT-08 resolution Jul-1.
- 🟡 **LIQUID HY-Energy-OAS pull** — owed, DEFERRED per Will Jun 20.
- 🟢 **Boot gap:** `scripts/ledger_staleness.py` MISSING (CLAUDE.md says wired Jun-27) — flag PROME. Also consider boot-scanning `PREREG_*.md` for unresolved pre-regs (this session's pre-reg + PROME's carried-item grade weren't surfaced at boot).

## POSITION DECISIONS → see `TRADE.md` (canonical)
- **v5.0 stance: no flat-price length either way; forward = defined-risk long-convexity, deploy-on-trigger.** No capital today. XLE $65C Sep-30 = LAPSE (deep-OTM backstop). Conditional Phase-2 short = DORMANT.

## MAIL STATE
- **Inbox/WALTER:** CLEAR (5 drained → processed/ this session). **Outbox:** none new (HAWK reconciliation via STATUS/NEXUS, not outbox). HAW-15 re-verify flagged via NEXUS_BRIEF WAITING-FOR.

## WORKBOOK HEALTH
- **THESIS v5.0** (header+two-phase reframe+exit+thresholds+risk-factors+footer) + CHANGELOG v5.0 entry. **STATUS v5.0** (trimmed to 222 lines, positions→TRADE.md pointer). **TRADE.md** live (102 lines, complete). **NEXUS_BRIEF v5.0**. SCRATCH (this).
- **GIT:** all committed + pushed this session (5 commits: WALTER+kinetic / reconcile / v4.4-catchup / race-tighten / v5.0-flip / TRADE.md / TRADE-completeness). HEAD 07be21de, origin 0/0.
- **Predictions:** no resolutions this session; **BRT-08 DUE next boot (Jul-1)**. BRT-21 reframed conditional (Phase-2 short demoted). No workbook KB/VX/FLOW rows added (session was thesis/trade-architecture, not new granular data).
