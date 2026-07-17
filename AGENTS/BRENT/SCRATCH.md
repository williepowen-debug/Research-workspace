# BRENT SCRATCH — Thu Jul 16, 2026 (teams-session: RE-ARM ADJUDICATION on the formal Hormuz closure)

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

**Session arc:** PROME spawned me (teams-mode) to adjudicate the energy re-arm after the fleet was OFFLINE 7/13-15 through the 7/11-12 formal Hormuz closure. Delivered: (1) **RE-ARM CONFIRMED** (fragile-watch → 🔴 ACTIVE); (2) **deploy read = PASS-ON-CHASE**; (3) **MSG-001 CLOSED** (Direct Messaging v1 first live test — convergence matrix re-scored 44→53/70); (4) **enlarged packet items a-e resolved**; (5) full inbox drain. Adjudication memo → `outbox/2026-07-16_to-PROME_rearm-adjudication.md`, SendMessage'd to PROME.

---

## ⚡ NEXT BOOT FIRST MOVES
1. 🔴 **CFTC COT Fri 7/17 ~3:30 PM ET (positions as-of 7/14)** — FIRST post-closure print. **GRADE MECHANICALLY against the frozen pre-reg: `setups/2026-07-17_COT-grade-and-FAL02-prereg.md`.** Primary metric = WoW change in MM GROSS SHORTS (WTI-phys, base 129,072): **COILED** ΔShorts ≥ −7,000 (fuel intact, re-entry conviction HIGHEST) · **IGNITING** −7K to −25K (burning, re-entry moderate) · **FUEL SPENT** ≤ −25,000 (consumed, re-entry DOWNGRADED). ICE Brent leg when published. → write grade to STATUS COT + TRADE re-entry read.
1b. 🔴 **FAL-02 oil-side (wind-down 00:01 ET 7/17)** — observe BINDING vs ALREADY-PRICED per the same pre-reg file (lean: already-priced); hand to FALCON's resolver, don't write its dir. Re-entry proposal to Will ONLY on a stabilized ~$80-82 pullback / vol-cooldown.
2. 🔴 **Deploy watch — the arm is ARMED-and-HOT, no capital.** Deploy trigger flips from "unpriced tail" to "vol-cooldown re-entry": a RED-day / pullback toward ~$80-82 that STABILIZES with the closure still in force = the clean convex entry (OVX ~61 now = too rich to chase). If Will wants blockade→Scenario-C tail NOW, small further-OTM ~$200 tranche only, live broker book (rule #4).
3. 🔴 **Baker Hughes ~7/17** (445, 12 to 457) · 🔴 **EIA WPSR wk-7/17 (rel 7/22)** — FIRST post-closure inventory read (Cushing hold >20M? crude draws accelerate? — the wk-7/10 data was PRE-closure vintage).
4. 🟠 **FAL-01 escalation watch** — named-major facility hit (Aramco/ADNOC/Kharg) OR vessel SUNK = clean FAL-01 fire = Scenario-C accelerant. KOC 7/12 was borderline (held open, concur w/ FALCON).
5. 🟡 **Japan June trade balance ~7/22** (SAM-routed, PROME_ROUTING_2026-07-11) — demand-side read on whether the oil regime is destroying importer demand; auto-relevant to my convergence matrix. Watch-set addition, SAM holds level work.
6. 🟡 **OPEC JMMC Tue 7/28 · FOMC Wed 7/29 · July CPI (carries the oil shock — June printed cool).**

## CHANGES SINCE LAST SESSION (Jul 10 → Jul 16) — the formal closure
- **7/11-12 Iran FORMALLY closed Hormuz** (IRGC fired on GFS Galaxy 7/11; US 3rd strike wave ~140 targets; Qatar blanket maritime suspension — first Gulf state; KOC platform hit). Ceasefire fully collapsed; US blockade element too (CNBC 7/15).
- **Brent +14%:** settles 7/13 $83.30 → 7/14 $84.73 → 7/15 $84.95 → 7/16 $84.23 → 7/17 $86.88 live. All >>$75. (⚠️ prior "$78.85 [7/13]" was a Mon intraday SPOT quote mislabeled as a settle — corrected 7/17 per FALCON; high-water settle $84.95, zero settles >$85.)
- **Transits COLLAPSED** to 10/88 (11%) 7/12 [PortWatch] — physical confirmation of the closure.
- **OVX ~61** (crisis-level oil vol) — the deploy-killer.
- EIA wk-7/10 (PRE-closure vintage): Cushing back >20M (20.04M, wk 1 of 2 for Boundary #3 rescission); SPR 316.5M 43-yr low; gas YoY −1.06%; pump $3.855.

## WHAT I DID THIS SESSION
- **RE-ARM ADJUDICATION** → CONFIRMED decisively (≥3 fresh legs beyond war-risk anchor + level >>$75; two standalone CONFIRM paths). Graded against the 7/10 DENY baseline, settlement basis, FALCON FRESH_LEG conventions. STATUS top banner + full memo. Recommend HEARTBEAT 🟡→🔴 (PROME owns the amendment).
- **DEPLOY = PASS-ON-CHASE** — missed the cheap 7/11-13 window (offline); OVX 61 vol-rich; +13% happened; green day (rule #6). Arm ARMED-and-HOT. TRADE.md updated (header + CURRENT STANCE + plan status).
- **MSG-001 (v1 first live test)** — receipt ACCEPTED→INTEGRATED (both validated clean), matrix re-scored 44→53/70 against CURRENT regime (7/8-10 state superseded, noted in receipt), message git-mv'd to processed. Tooling friction: NONE material (validate rc-0, PyYAML present, receipt engine clean) — minor UX notes only, reported to PROME.
- **Packet items a-e** → STATUS "🟠 7/16 ENLARGED-PACKET ITEMS" section: KOC borderline/hold-open, GCC 6.7 Mbpd reconciled (flow-vs-asset), Russia 4.22M (HAW-15 unfired), COT spring-fuel confirmed (next 7/17), FRESH_LEG_BASELINE adopted.
- **Convergence matrix** re-scored (Hormuz/Gulf/Brent/Tanker/Ceasefire/Curve all ↑ to 5; kinetic cluster maxed).
- **Inbox DRAINED** — MSG-001 + 3 routing files (7/11, 7/12, DAEDALUS threshold-fix) → processed. WALTER inbox already clean (0).

## OPEN THREADS / WATCHES
- 🔴 **Deploy decision** sits with Will (proposal in memo §2; pass-on-chase, or small tranche if he wants tail-now).
- 🔴 **COT 7/17** — squeeze-ignition test.
- 🟡 **LIQUID:** HY OAS calm 272 [7/14] has NOT repriced the closure — the key LAGGING credit tell to watch.
- 🟡 **Curve structure** — contango→backwardation flip is [EST] (M1-M3 ~+$3-5); stamp [CONF] if an ICE-settle source appears.
- 🟡 **GROUP_MAP.tsv +115d stale** (freeze-or-refresh — deferred again this session).

## POSITION DECISIONS → see `TRADE.md` (canonical)
- **v5.0 stance holds: no flat-price length either way; forward = defined-risk long-convexity.** Arm = 🔴 ARMED-and-HOT (re-arm CONFIRMED) but NO capital — deploy = pass-on-chase at $86/green/OVX-61. XLE $65C Sep-30 = LAPSE. Conditional Phase-2 short = DORMANT.

## MAIL STATE
- **Inbox: CLEAN** (drained MSG-001 + 3 routing files → processed; WALTER 0). **Outbox:** `2026-07-16_to-PROME_rearm-adjudication.md` (delivered via SendMessage + file). **Receipt:** `messages/receipts/MSG-PROME-20260714-001__BRENT.md` (INTEGRATED, validated).

## WORKBOOK HEALTH
- **LIVE & current (7/16):** STATUS (re-arm banner + re-scored matrix 53/70 + packet items + dashboard), TRADE (re-arm/pass-on-chase), SCRATCH (this), adjudication memo, MSG-001 receipt. **THESIS v5.0 unchanged** (the re-arm confirms the pre-registered up-tail; no restructure — the skew was already upside-convex). Consider a THESIS/CHANGELOG note next session logging "Phase-1 re-squeeze realized 7/12."
- **FROZEN:** KB.tsv, VX.tsv, FLOW.tsv, TIMELINE.md. **STALE (deferred):** GROUP_MAP.tsv +115d.
- **GIT:** committed local (pathspec AGENTS/BRENT/ only). Rides push-train — do NOT push per task (PROME owns closeout push).
