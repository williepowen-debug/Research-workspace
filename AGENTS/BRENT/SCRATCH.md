# BRENT SCRATCH — Fri Jun 26, 2026 (STRUCTURAL vs COILED-SPRING decision + COT/rig pull + WALTER inbox drain)

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11). Supersedes the Jun-24 SCRATCH.

**Session arc:** Live scoped session (Prome-spawned, HAWK concurrent). Adjudicated the Nuttall/Hedgeye coiled-spring counter (SIG-W-20260626-002) against own live data; pulled + confirmed the two newest catalysts (Baker Hughes rigs, CFTC COT Jun-23 first-true-post-MOU read); drained the full WALTER inbox (6 signals → processed). NO COMMIT this session — Prome commits BRENT dir sequentially to avoid shared-index race with HAWK.

---

## ⚡ NEXT BOOT FIRST MOVES
1. 🔴 **Wed Jul 1 — EIA WPSR (wk-6/26)** — Cushing trajectory at sub-20M (~18M if −1M/wk holds); watch crude draw vs cycle-max pace. Also re-pull WGFUPUS2 (gasoline 4-wk YoY, Trigger #2 datapoint #3 still PENDING from wk-6/19) + WPULEUS3 refinery util Jun-19 — both were unindexed at the Jun-24 run.
2. 🔴 **Re-pull ICE Brent main MM net (Jun-23 data)** — got NYMEX WTI cleanly (+82,872, liquidating) but did NOT cleanly pull main ICE Brent net this session (macromicro 403'd; Brent-Last-Day NYMEX mini only). Need it vs Jun-16 174,807 lots to fully close the discriminator. Try barchart COT or CFTC disaggregated petroleum.
3. 🟠 **~Jul 3 — SPR 172M emergency-release authorization fully withdrawn → DOE re-auth decision** — first tranche exhaustion gate; charged by re-closure risk.
4. 🟠 **Jul 8 — EIA STEO (July)** — first post-deal price-path revision (June STEO $105 closed-Hormuz already superseded by realized ~$73).
5. 🟡 **Verify Hedgeye Japanese crude drawdown** (~360→280M Mar-Jun, Kpler/Commodity Context) — left [UNVERIFIED] this session; directionally consistent w/ tightness.

## CHANGES SINCE LAST SESSION (Jun 24 → Jun 26)
- **Brent $73.57 (−2.56%) / WTI $70.24 (−2.34%) [CONF boot.py Jun-26]** — Brent now ~day-2 BELOW $75 = RED-FT-04 thesis-down level breached. WTI right at $70 threshold.
- **Baker Hughes oil rigs 440 (+7 WoW from 433) [CONF TradingEconomics wk-6/26]** — climbing toward 457 (+50 from trough 407); 17 to go. Supply response building = structural/bearish-medium. BRT-26 intact. (Total US rigs 573 +10.)
- **CFTC COT Jun-23 (first TRUE post-MOU forced-liquidation read) [CONF CFTC]:** NYMEX WTI Light Sweet (067651) MM Long 209,683 / Short 126,811 / **net +82,872** (vs Jun-16 +96,228 → **−13,356 wk**, driven by **long liquidation −10,490**, shorts +2,866). ICE WTI Europe mini MM net −18,387. = **CONTINUED DE-RISKING / FORCED LIQUIDATION, NOT short-covering → STRUCTURAL.**
- **Crack spreads [CONF RBN, Jun]:** COOLED from spring peak — diesel $66(Mar)→$56(Jun), gasoline $46(May)→$40(Jun); still +122%/+104% YoY. Strong but OFF highs ⇒ Nuttall "crack ATH" claim STALE.
- **VLCC tape rolled over:** Frontline −7.67%, DHT −2.38%, STNG −3.82% on Jun-26 → the Jun-22 +82-92% VLCC spike (SIG-004) faded = thin-tape noise, decoupling intact.

## WHAT I DID THIS SESSION
- **Rendered the decision:** sub-$75 = STRUCTURAL base case, **P(holds<$75 over 1-2wk)=0.63, lean STRUCTURAL**, fat re-escalation tail. Written to STATUS Jun-26 PM section (v4.3 minor) w/ full Nuttall adjudication table + flip-conditions each way + HAWK reconciliation hook + XLE stub call.
- **Drained WALTER inbox (6 signals → processed/, board_log rows):** 002 (Nuttall counter, acted/adjudicated); 004 (VLCC spike, noted/faded); 005 (SPR 1983-low, acted/already-integrated); 006 (Iranian tankers, noted); 010 (OFAC license, acted/already-integrated); 011 (Hormuz transit rebound, noted). inbox/WALTER now CLEAR.
- **XLE $65C Sep-30 call:** LAPSE-LEANING HOLD (passive) — premise broken, today's COT = structural = path-to-pay less supported; salvage negligible so nothing to trim; keep as kinetic-tail lottery into a vol spike only.

## NEXT SESSION (dated, future-verifiable)
1. **Wed Jul 1** — EIA WPSR wk-6/26 (Cushing ~18M watch) + clear the 2 PENDING wk-6/19 cells (WGFUPUS2, WPULEUS3).
2. **~Jul 3** — SPR 172M auth exhaustion → DOE re-auth decision gate.
3. **Jul 8** — EIA STEO (July) first post-deal price path.
4. **Each Fri** — CFTC COT: track whether NYMEX WTI MM net continues bleeding toward zero (structural-confirm) or reverses to covering (spring).

## OPEN THREADS / WATCHES
- 🔴 **RED-FT-04 breached** — Brent ~day-2 sub-$75; if it HOLDS through next 1-2wk = structural confirmed (my 0.63 base). Flip-up trigger = confirmed kinetic Hormuz/Gulf energy-infra event.
- 🔴 **Discriminator on next COT** — NYMEX WTI MM net +82,872 still has long to shed; watch toward/through zero (structural) vs short-covering reversal (spring). Need clean ICE Brent main net too.
- 🟠 **Rigs 440 → 457** — 17 from shale-response threshold; supply add building.
- 🔴 **Snap-back tail remains highest of cycle** — record-low stocks (SPR 40yr-low, Cushing breached) + still-net-long WTI = violent snap IF HAWK D-tail fires (Lebanon seam / demining incident). Tail real even though base case structural.
- 🟡 **Trigger #2 datapoint #3** (gasoline 4-wk YoY wk-6/19) still PENDING (WGFUPUS2 unindexed Jun-24); 🟡 refinery util Jun-19 PENDING.
- 🟡 **LIQUID HY-Energy-OAS pull** — owed, DEFERRED per Will Jun 20.

## POSITION DECISIONS PENDING
- **XLE $65C Sep 30** — LAPSE-LEANING HOLD (passive). Premise (sustained $90+ Brent) BROKEN; today's continued-liquidation COT = structural = re-escalation path-to-pay LESS supported. Deep OTM (XLE $53.84 vs $65, ~21%), salvage negligible → nothing to trim. Keep as kinetic-tail lottery; close ONLY into a Lebanon/Hormuz vol spike; else let lapse. Re-arm = confirmed kinetic event.
- **No new flat-price longs** — de-escalation confirmed + de-risking COT + rigs rising = wrong regime to add length.

## MAIL STATE (one line per signal)
- **Inbox/WALTER:** CLEAR — all 6 drained to processed/ this session (002/004/005/006/010/011); board_log updated.
- **Outbox:** none new; HAWK reconciliation hook written into STATUS Jun-26 PM (Prome running HAWK concurrently — routed via STATUS, not outbox).

## WORKBOOK HEALTH
- STATUS updated (Jun-26 PM section + header v4.3); SCRATCH rewritten (this session); board_log +6 rows.
- THESIS: no version bump warranted yet (decision is a confidence-render on existing v4.x inverted-divergence frame, not a phase transition) — consider folding the structural-vs-spring adjudication into THESIS/CHANGELOG next full closeout if base case holds.
- PREDICTIONS: BRT-28 (Cushing <20M) already FIRED Jun-24; no new resolutions this session.
- NEXUS_BRIEF: NOT refreshed this session (scoped live session) — refresh As-of/STATUS-commit stamp next boot.
- **GIT: NOT committed/pushed this session — Prome commits BRENT dir sequentially (HAWK concurrent). Edits left in working tree:** STATUS.md, SCRATCH.md, board_log.tsv, + 6 files git-mv'd to inbox/WALTER/processed/.
