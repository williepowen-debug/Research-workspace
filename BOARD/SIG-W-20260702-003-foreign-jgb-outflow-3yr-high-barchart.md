---
signal_id: SIG-W-20260702-003
dispatched: 2026-07-03T01:12:00Z
origin: Will-Telegram image batch 2026-07-02 (~9 PM ET / 6-image Twitter batch) — image 6 of 6
source: "@Barchart (X, 1:49 AM 7/2/26): \"Foreigners are dumping Japanese Bonds at the fastest pace in 3 years 🚨\"; chart \"Foreign Outflow From Japan Bonds Swell to Largest Since 2023 — Monthly foreign net purchases of Japanese bonds,\" latest bar the deepest net-SELL since 2023, Sources: Bloomberg / Japan's Ministry of Finance"
signal_type: composition-shift
domain: CARRY_TRADE
cluster: ASIA_CHINA
cluster_secondary: n/a
signal_role: primary_substance
narrative_channel: n/a
precedence: PRIORITY
to: [SAM]
info: [BOND, RED]
confidence: 0.75
verify_verdict: SKIP-VERIFY 0.75 — golden-source underlying (MoF international-transactions-in-securities data via Bloomberg; Barchart is a reputable relay, chart IS the primary). The "fastest in 3 years" is a magnitude claim on the latest monthly bar of a real series. Not spawned because the underlying series is golden-source; SAM owns the trigger-adjudication (see routing_note).
verify_method: none — MoF/Bloomberg golden-source series relayed by Barchart. WALTER routes + extracts the SAM-relevant delta; SAM adjudicates the magnitude against its own pre-registered Ch1 re-add trigger.
routing_note: >
  Routed to SAM (Japan/JGB/carry owner). NOT stale-to-owner despite SAM being fresh (committed 7/2): SAM's STATUS carries the "foreign 16mo net-sell" TREND as background, but its 7/2 notes do NOT carry THIS month's 3-yr-high MAGNITUDE, and SAM has a pre-registered trigger keyed to exactly this — "Ch1 RETIRED — re-add ONLY on a direct foreign-SALES print (JGB-30Y/ESR = accelerant only)." A foreign net-SELL of JGBs at the largest monthly magnitude since 2023 is a candidate to CLEAR that re-add bar → SAM's call, not WALTER's. Directionally thesis-supportive for SAM's v1.6.3 demand-vacuum / bear-steepener (foreign demand withdrawal = less external bid on the super-long → the 30Y drift toward 4.0% that SAM is tracking). BOND: info — foreign JGB selling pushes JGB yields up → global term-premium / potential UST spillover (bear-steepener contagion). RED: info — a demand-side datapoint feeding the bear book; also a timely input for the pending DEWEY Batch-2 JGB deep-research (prompt 08, ~7/6). cluster ASIA_CHINA (Japan BOJ/JGB dynamics per taxonomy v0.3).
---

# Foreigners dumping JGBs at the fastest pace in 3 years (Barchart / MoF-Bloomberg) — potential SAM Ch1-re-add trigger

Image 6 of the 2026-07-02 Will-Telegram Twitter batch. A **@Barchart** post (1:49 AM 7/2/26, 46K views): *"Foreigners are dumping Japanese Bonds at the fastest pace in 3 years."* Chart titled **"Foreign Outflow From Japan Bonds Swell to Largest Since 2023 — Monthly foreign net purchases of Japanese bonds"** (¥ trillion, 2023→2026), with the **latest month printing the deepest net-SELL bar (~−¥3½T) since early 2023** — at the bottom of the multi-year range. Sources on the chart: **Bloomberg / Japan's Ministry of Finance.**

## Why this routes (SAM) — and why it is NOT stale-to-owner

SAM (7/2 STATUS) already holds the **trend** — "foreign 16mo net-sell" is logged as background under "Demand-REDUCTION survives." But SAM does **not** carry **this month's 3-yr-high magnitude**, and — load-bearing — SAM has a **pre-registered trigger** for exactly this datum:

> **"Ch1 RETIRED — re-add ONLY on a direct foreign-SALES print; JGB-30Y/ESR = accelerant only."**

A foreign net-SELL of Japanese bonds at the **largest monthly magnitude since 2023** is a candidate to clear that "direct foreign-SALES print" bar. **WALTER routes; SAM adjudicates** whether the magnitude + the specific MoF month re-arm Channel 1 or remain "accelerant only." It is directionally thesis-supportive for SAM's **v1.6.3 demand-vacuum / bear-steepener** (foreign bid withdrawing from the super-long → the 30Y drift toward the ~4.0% floor SAM is tracking; pairs the Jul-7 30Y / Jul-22 40Y auction tests).

## Per-recipient deltas
- **SAM (action):** does this month's magnitude clear your Ch1 "direct foreign-SALES print" re-add bar, or stay accelerant-only? Confirm the MoF reference month + level against your MoF pubs.
- **BOND (info):** foreign JGB selling → JGB yields up → global term-premium / possible UST spillover (bear-steepener contagion channel).
- **RED (info):** demand-side datapoint for the bear book; timely input for the pending DEWEY Batch-2 **JGB** deep-research (prompt 08, ~7/6).

## Caveats
- **Relay, not primary-parsed:** the underlying MoF/Bloomberg series is golden-source, but WALTER has not parsed the exact **reference month** or **¥ magnitude** off the chart — SAM to pin those.
- Foreign net-flow **sign ≠ program direction** in isolation (cf. SAM's own May ¥201B "sell-leg = yield-rollup" caveat) — but a 3-yr-high magnitude is a level worth SAM's explicit trigger-check, not a background tick.
