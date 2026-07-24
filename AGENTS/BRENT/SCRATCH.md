# BRENT SCRATCH — Fri Jul 24, 2026 ~1:15 PM ET (intraday — tail-rider re-quote ADJUDICATED = FILL, routed to TERRY)

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

---

## CHANGES SINCE LAST SESSION (Jul 23 close → Jul 24 ~1:15 PM)
- **Will opened the USO tail-rider re-quote window on today's oil pullback** (Brent $95.60 −5.06%, off yesterday's $100.19 settle — first genuine red day since the 7/21 rider approval). PROME spawned adjudication task.
- **Corrected a stale premise in the spawn packet:** it referenced the "$175C" — that structure was superseded 7/23 by the 150/165 call spread (Option A never filled, break-evens sat beyond our own escalation target). Graded the re-quote against the ACTUAL live instrument.
- **OVX pulled direct (fetch.py's bare `OVX` is broken — delisted error; `^OVX` works):** OVX 65.75 (p94.3), VIX 17.74, ratio 3.70 (p98.2) — cross-checked via VIOLET's `ovx.py --no-log` (read-only, no write to VIOLET's files). **Ratio is FURTHER from the cooldown gate than 7/23's 3.57** (VIX fell faster than OVX); VIOLET's own canary flipped to 🔴 FIRE (oil-led, not broad co-move).
- **Level-trigger: NO** ($95.60 ≠ the $80-82 re-entry band). **Vol-cooldown: NO** (both legs unmet, ratio worse). **Rule #6: YES, cleanly for the first time** (no break-note needed, unlike 7/22/7/23).
- **Fundamentals checked against two fresh gate fires:** FALCON-001 leg-1 kinetic (Bab, 7/22) — FALCON's own 7/23 read says "TIPPING, not confirmed supply-loss" (transits sliding but flowing, bypass holding, Yanbu loadings increasing). OSPREY-001 leg-(b) fired TODAY (CPC day-5, duration not severity — but Kazakh output −21%, Tengiz −56%, named owners Exxon/Chevron refusing terminal calls). No de-escalation falsifier fired anywhere → read = mean-reversion off the spike, not a thesis break.
- **VERDICT: FILL** the 150/165 spread at today's cheaper USO mark ($134.66 vs the $140.69 the ticket was built on) — the OVX gate governs the MAIN arm's capital, not this small pre-approved hedge. Routed to TERRY for live-broker re-mark + Will [Approve].
- **Deliverables:** `outbox/2026-07-24_to-PROME_uso-tail-rider-requote-adjudication.md` (full memo) · `AGENTS/TERRY/inbox/2026-07-24_from-BRENT-via-PROME_uso-tail-rider-shape-ask.md` (self-authored carve-out, committed by me) · STATUS.md 7/24 banner + dashboard refresh (Brent/WTI/OVX/VIX/USO/TLT rows).
- **Did NOT touch HEARTBEAT.md** (PROME rebasing in parallel this session) — proposed the OVX/ratio update + VIOLET-FIRE note in the PROME memo for PROME to fold in.

## PRIOR SESSION — CHANGES Jul 22 → Jul 23 (preserved)
- **🔴 BRENT TOPPED $100** ($100.01–100.74, +6.75% 7/23 [Yahoo BZ=F]) — **KEY THRESHOLD #1 fired (Scenario-C confirmation)**; +32% off the 7/10 $76 settle. Still PREMIUM by the discriminator (zero barrels confirmed destroyed).
- **The vol crisis is transmitting beyond oil:** VIX 19.7 (+19.71%), OVX **70.27 = new cycle high**, Treasury yields YTD highs, stocks+bonds down. Previously oil-specific.
- **Bab al-Mandab went KINETIC (7/23):** Houthis struck 2 Saudi tankers (*Encelia*, *Layla*) with drones/missiles, **fires on both, no casualties, no confirmed sinking** — first vessel attack since the 7/20 blockade declaration. Ladder: declared(7/20)→coercion(7/21)→strikes(7/23). Still premium, NOT the execution tell (fresh aggregate transit collapse).
- **First post-closure EIA (wk-7/17) IN:** Cushing **19.37M (−0.67M) → BACK BELOW 20M = Boundary #3 rescission FAILED** (didn't hold wk 2/2); SPR draw re-accel −5.06M (311.4M); commercial +2.01M BUILD; util 96.1%; gas demand +1.45% (hoarding, no destruction yet).
- **Tail-rider did NOT fill 7/22** [PROME 7/22]; **war-risk watch assigned** (FALCON=Gulf/Red Sea · OSPREY=Black Sea · BRENT=premium synthesis).

## WHAT I DID (Jul 23 EOD session, preserved below)
- **Boot + live sit-rep** (Will-directed): boot.py, live re-quotes (Brent $100, OVX 70.27, USO $140), web-verified the $100 driver set (Red Sea strikes / 12th US strike night / Trump-Pickaxe threat / CPC).
- **STATUS write-back** (commit `947e7370`): new 7/23 banner + full propagation (Overall Status, Price Dashboard refreshed wk-7/10→**wk-7/17 EIA**, OVX/VIX rows, USO $140.35, convergence matrix Bab 4→5 + Brent-price row + TOTAL 62→63/75, KEY OPEN ITEMS #1 EIA resolved, STATE buffers, SUMMARY FOR WILL). 196 lines.
- **Pulled Bab transit data:** freshest aggregate = Lloyd's List 39/wk-7/13-19 (−54% WoW; non-Iran 17 from 53) — PRE-strike vintage → execution NOT yet confirmable off hard data. FALCON's bypass_watch.py state stale (7/10).
- **FALCON fresh-Bab-count ASK sent** (🔴 `inbox/2026-07-23_from-BRENT_fresh-bab-transit-count-request.md` + outbox copy; in commit `947e7370`).
- **Tail-rider PIVOTED A($175C)→150/165 call spread** (commit `60ec48d2`): after A failed to fill 7/22, the 7/23 re-quote (USO $140.69, OVX 70, insurance ~2× repriced) + fresh P(ITM)/break-even math showed both naked calls break even beyond our thesis ($130/$146 vs Scenario-C ~$115-120). Staged order ticket + EXECUTION LOG PENDING row + DECISIONS pivot note. Will placing per ticket.
- **NEXUS_BRIEF** full write-back (Status/Position/As-of/VIEW/CALIBRATION/SENDING-HAWK/WAITING-FOR/NEXT-DECISION/CATALYSTS). **THESIS CHANGELOG** 7/23 entry (no version bump — v5.1 premium structure unchanged).

## NEXT SESSION (dated, future-verifiable)
0. 🔴 **TAIL-RIDER — ADJUDICATED FILL 7/24, routed to TERRY (not yet executed).** Check whether TERRY placed the order and Will [Approve]d before the 4:00 PM ET USO options close today. On fill → replace the PENDING EXECUTION LOG row in TRADE.md + FORGE flag. On no-fill again → decide whether weekend gap risk (no US options trading Sat/Sun, CPC/Bab both live) changes the Monday read.
1. 🔴 **CPC leg-(b) FIRED 7/24 (OSPREY, day-5)** — watch weekend resolution: does the halt resume, or extend into a 2nd week? A 2nd week compounds deferred-barrel count and pushes toward the Nov-2025 structural-tail comparison (still NOT crossed — legs a/c unfired).
2. 🔴 **CFTC COT (as-of 7/21), 3:30 PM ET today** — grade squeeze progression off the frozen ladder (base 119,187; watch cumulative −25K off 129,072 = FUEL-SPENT); ICE-WTI sibling check. **+ Baker Hughes rig count ~7/24: 452 vs 457 — BRT-26 likely FAILS on a +5 print; grade honestly at the print.**
3. 🔴 **FALCON's leg-2** — fresh aggregate Bab transit collapse tell, due ~7/26-29 — the discriminator on whether the pullback stays mean-reversion or the Bab vector tips to confirmed supply-loss.
4. 🟠 **Tue Jul 28 OPEC JMMC · Wed Jul 29 FOMC** (now framing a live oil shock + waking-then-cooling equity vol).
5. 🟡 SAM Japan June trade balance. 🟡 ICE-settle for the curve (stamp backwardation [EST]→[CONF]). 🟡 shuttle-fleet double-count reconcile w/ FALCON. 🟡 HEARTBEAT rebase — check PROME folded the OVX/ratio update + VIOLET-FIRE note from today's memo.

## OPEN THREADS / WATCHES
- 🔴 **Deploy gate** (4 sessions of correct pass-on-chase): OVX/VIX <2.89 AND OVX <44.2 + stabilized pullback. At 3.57/70.27 = further from met than ever.
- 🔴 **Branch-2 gap paths ×2, COT-invisible:** Kharg (flow-anchor: loadings→0) + Bab/Yanbu execution (aggregate-transit tell; now KINETIC as of 7/23 but not yet aggregate-collapse). Tail-rider (150/165 spread) is the insurance — pending fill.
- 🟠 **Premium-vs-supply-loss discriminator** governs: $76→$100 with zero barrels confirmed destroyed = fast round-trip on any Muscat off-ramp. Phrasing: "fires not sinkings," "no destruction YET."
- 🟠 **Buffer thesis weakened:** Cushing back <20M (rescission failed), SPR draw re-accel. Watch export-pull vs domestic (Brent $8+ over WTI) before reading tightness.
- 🟠 **HY energy OAS** (183bps, 6/30 vintage) hasn't repriced the closure — July print ~Aug (LIQUID). Now equity vol (VIX 19.7) is finally transmitting — credit is the last lagging tell.

## POSITION DECISIONS PENDING
- **Tail-rider (150/165 call spread) — ADJUDICATED FILL 7/24, routed to TERRY for live re-mark; NOT YET EXECUTED.** TERRY brings Will a one-line fill for [Approve/No]. On fill → EXECUTION LOG + FORGE flag. Option A ($175C) stays superseded (didn't fill 7/22; naked-call break-evens beyond thesis at 7/23 vol) — flagged as a stale-premise correction in today's memo since the spawn task referenced it.
- **Off-ramp round-trip playbook = RATIFIED, ARMED-PASSIVE** (trigger day = one-line approve). Untouched today — no de-escalation falsifier fired.
- **Convex main arm = ARMED-and-HOT, no capital** (gate unmet, and the ratio leg moved FURTHER from met today — see STATUS 7/24 banner). XLE $65C Sep-30 = LAPSE.
- **GS long-diesel** = third expression option on record (Will/TERRY; diesel scope req dispatched to TERRY 7/21 — still awaiting reply).
- **Awaiting replies:** TERRY (diesel structures + today's tail-rider shape ask) · LIQUID (transport-HY baseline).

## MAIL STATE
- **Inbox processed this session:** OSPREY CPC day-5 fire-alert (`2026-07-24_from-OSPREY-via-PROME_cpc-fire-alert.md`), FALCON Bab leg-1 answer (`2026-07-23_from-FALCON_bab-transit-leg1-answer.md`, read late 7/23, integrated into today's discriminator read). **Outbox:** today's PROME adjudication memo written + delivered. **New packet sent:** TERRY inbox ask (self-authored carve-out, committed by me). LIQUID (7/23 fuel-consumer reframe, in inbox) and AEOLUS (7/22 Bertha shut-ins) still unprocessed — not this session's scope, check next full boot.

## WORKBOOK HEALTH
- **LIVE & current (7/24):** STATUS (199 lines, 7/24 banner + dashboard refresh), TRADE (unchanged — no structure edit needed, re-quote is TERRY's live-chain job), SCRATCH (this). NEXUS_BRIEF/THESIS/CHANGELOG NOT touched this intraday pass (no thesis-level change — mean-reversion read, not a verdict flip) — refresh at next full closeout.
- **FROZEN (bannered, correct):** KB.tsv, VX.tsv, FLOW.tsv, GROUP_MAP.tsv, TIMELINE.md.
- **GIT:** this session's commit(s) — STATUS + SCRATCH (own dir) + TERRY inbox packet (self-authored carve-out); safe-push at end.
