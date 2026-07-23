# BRENT SCRATCH — Thu Jul 23, 2026 ~4:30 PM ET (CLOSED OUT EOD — boot · $100 sit-rep · full write-back · freshness audit · tail-rider pivot→NOT filled, carry to 7/24 · FALCON ask)

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

---

## CHANGES SINCE LAST SESSION (Jul 22 close → Jul 23)
- **🔴 BRENT TOPPED $100** ($100.01–100.74, +6.75% 7/23 [Yahoo BZ=F]) — **KEY THRESHOLD #1 fired (Scenario-C confirmation)**; +32% off the 7/10 $76 settle. Still PREMIUM by the discriminator (zero barrels confirmed destroyed).
- **The vol crisis is transmitting beyond oil:** VIX 19.7 (+19.71%), OVX **70.27 = new cycle high**, Treasury yields YTD highs, stocks+bonds down. Previously oil-specific.
- **Bab al-Mandab went KINETIC (7/23):** Houthis struck 2 Saudi tankers (*Encelia*, *Layla*) with drones/missiles, **fires on both, no casualties, no confirmed sinking** — first vessel attack since the 7/20 blockade declaration. Ladder: declared(7/20)→coercion(7/21)→strikes(7/23). Still premium, NOT the execution tell (fresh aggregate transit collapse).
- **First post-closure EIA (wk-7/17) IN:** Cushing **19.37M (−0.67M) → BACK BELOW 20M = Boundary #3 rescission FAILED** (didn't hold wk 2/2); SPR draw re-accel −5.06M (311.4M); commercial +2.01M BUILD; util 96.1%; gas demand +1.45% (hoarding, no destruction yet).
- **Tail-rider did NOT fill 7/22** [PROME 7/22]; **war-risk watch assigned** (FALCON=Gulf/Red Sea · OSPREY=Black Sea · BRENT=premium synthesis).

## WHAT I DID THIS SESSION
- **Boot + live sit-rep** (Will-directed): boot.py, live re-quotes (Brent $100, OVX 70.27, USO $140), web-verified the $100 driver set (Red Sea strikes / 12th US strike night / Trump-Pickaxe threat / CPC).
- **STATUS write-back** (commit `947e7370`): new 7/23 banner + full propagation (Overall Status, Price Dashboard refreshed wk-7/10→**wk-7/17 EIA**, OVX/VIX rows, USO $140.35, convergence matrix Bab 4→5 + Brent-price row + TOTAL 62→63/75, KEY OPEN ITEMS #1 EIA resolved, STATE buffers, SUMMARY FOR WILL). 196 lines.
- **Pulled Bab transit data:** freshest aggregate = Lloyd's List 39/wk-7/13-19 (−54% WoW; non-Iran 17 from 53) — PRE-strike vintage → execution NOT yet confirmable off hard data. FALCON's bypass_watch.py state stale (7/10).
- **FALCON fresh-Bab-count ASK sent** (🔴 `inbox/2026-07-23_from-BRENT_fresh-bab-transit-count-request.md` + outbox copy; in commit `947e7370`).
- **Tail-rider PIVOTED A($175C)→150/165 call spread** (commit `60ec48d2`): after A failed to fill 7/22, the 7/23 re-quote (USO $140.69, OVX 70, insurance ~2× repriced) + fresh P(ITM)/break-even math showed both naked calls break even beyond our thesis ($130/$146 vs Scenario-C ~$115-120). Staged order ticket + EXECUTION LOG PENDING row + DECISIONS pivot note. Will placing per ticket.
- **NEXUS_BRIEF** full write-back (Status/Position/As-of/VIEW/CALIBRATION/SENDING-HAWK/WAITING-FOR/NEXT-DECISION/CATALYSTS). **THESIS CHANGELOG** 7/23 entry (no version bump — v5.1 premium structure unchanged).

## NEXT SESSION (dated, future-verifiable)
0. 🔴 **TAIL-RIDER — NOT FILLED 7/23 (carry to 7/24).** Order not placed 7/23 (Will unavailable at close; USO opts shut 4pm; late-day USO $139.49, spread mid $3.48/wide). **7/24: re-quote FRESH at the open and place — ⚠️ 7/24 catalysts (CPC leg-(b) · COT · Baker Hughes) can gap USO either way, so the insurance ideally goes ON before them.** Structure unchanged (BUY +1 Sep-18 $150C / SELL −1 $165C, work ~$3.70 debit toward ~$3.90). On fill → replace the PENDING EXECUTION LOG row + FORGE flag.
1. 🔴 **~Fri Jul 24 — CPC leg-(b)**: 5th continuous suspended session fires GATE-OSPREY-001 leg-(b) (routes 🔴 to me). Check CPC loading status + Black Sea war-risk rate.
2. 🔴 **Fri Jul 24 — CFTC COT (as-of 7/21)**: grade squeeze progression off the frozen ladder (base 119,187; watch cumulative −25K off 129,072 = FUEL-SPENT); ICE-WTI sibling check. **+ Baker Hughes: 452 vs 457 — BRT-26 likely FAILS on a +5 print; grade honestly at the print, no pre-grade.**
3. 🔴 **FALCON reply** — fresh post-strike aggregate Bab count + war-risk level = the open discriminator on whether the $100 move is tipping premium→supply-loss. Integrate when it lands.
4. 🟠 **Tue Jul 28 OPEC JMMC · Wed Jul 29 FOMC** (now framing a live oil shock + waking equity vol).
5. 🟡 SAM Japan June trade balance (~7/22 — check if printed). 🟡 ICE-settle for the curve (stamp backwardation [EST]→[CONF]). 🟡 shuttle-fleet double-count reconcile w/ FALCON.

## OPEN THREADS / WATCHES
- 🔴 **Deploy gate** (4 sessions of correct pass-on-chase): OVX/VIX <2.89 AND OVX <44.2 + stabilized pullback. At 3.57/70.27 = further from met than ever.
- 🔴 **Branch-2 gap paths ×2, COT-invisible:** Kharg (flow-anchor: loadings→0) + Bab/Yanbu execution (aggregate-transit tell; now KINETIC as of 7/23 but not yet aggregate-collapse). Tail-rider (150/165 spread) is the insurance — pending fill.
- 🟠 **Premium-vs-supply-loss discriminator** governs: $76→$100 with zero barrels confirmed destroyed = fast round-trip on any Muscat off-ramp. Phrasing: "fires not sinkings," "no destruction YET."
- 🟠 **Buffer thesis weakened:** Cushing back <20M (rescission failed), SPR draw re-accel. Watch export-pull vs domestic (Brent $8+ over WTI) before reading tightness.
- 🟠 **HY energy OAS** (183bps, 6/30 vintage) hasn't repriced the closure — July print ~Aug (LIQUID). Now equity vol (VIX 19.7) is finally transmitting — credit is the last lagging tell.

## POSITION DECISIONS PENDING
- **Tail-rider (150/165 call spread) — SELECTED 7/23, PENDING FILL.** Will places per the ticket. On fill → EXECUTION LOG + FORGE flag. Option A ($175C) superseded (didn't fill 7/22; naked-call break-evens beyond thesis at 7/23 vol).
- **Off-ramp round-trip playbook = RATIFIED, ARMED-PASSIVE** (trigger day = one-line approve).
- **Convex main arm = ARMED-and-HOT, no capital** (gate unmet). XLE $65C Sep-30 = LAPSE. No expiries near (Sep 18 spread / Sep 30 XLE next).
- **GS long-diesel** = third expression option on record (Will/TERRY; diesel scope req was dispatched to TERRY 7/21 — await reply).
- **Awaiting replies:** TERRY (diesel structures) · LIQUID (transport-HY baseline) · FALCON (fresh Bab count).

## MAIL STATE
- **Inbox: CLEAN** — PROME war-risk/USO-fill note processed this session (read; actioned; no reply owed). **Outbox:** FALCON fresh-Bab ask written + delivered 7/23 (copy in outbox/). No other acute 🔴 owed.

## WORKBOOK HEALTH
- **LIVE & current (7/23):** STATUS (196 lines), TRADE (tail-rider pivot staged), THESIS v5.1 + CHANGELOG (7/23 entry), NEXUS_BRIEF, SCRATCH (this), board_log. INCIDENTS (RF-038 CPC still ACTIVE — update when CPC resumes).
- **Not touched this session (still current):** PREDICTIONS.tsv (no due rows; BRT-26 grades 7/24), TRACKER, CATALYSTS.tsv (7/24 CPC/COT rows live), REFERENCE_TABLES (vintage-stamped).
- **FROZEN (bannered, correct):** KB.tsv, VX.tsv, FLOW.tsv, GROUP_MAP.tsv, TIMELINE.md.
- **GIT:** commits `947e7370` (STATUS + FALCON ask) + `60ec48d2` (TRADE) + this closeout (NEXUS/CHANGELOG/SCRATCH); safe-push at end.
