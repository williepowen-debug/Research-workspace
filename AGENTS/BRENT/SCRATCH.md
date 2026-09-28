# BRENT SCRATCH — September 28, 2026 (Monday; brent-d2, three legs: 14:34–15:54 · 16:22–17:2x · evening to 18:24 ET by `date`)

## CHANGES SINCE LAST SESSION
- **Trump on record Sun 9/27** (Bloomberg/Yahoo 17:55 EDT): a diesel export ban is under consideration, *"we may do it"*. No order. WH (anonymous) 9/28: "no decision". Wright: voluntary curbs.
- **Will's six-item scope at ~18:10 ET = WQ-329** (RULINGS § R-2026-09-28-WQ329). TERRY is spawned on the VLO management proposal (DOCKET L535, prep only).
- **FORGE shows USO Sep-30 $159C ×2 OPEN** (bought 9/18, −$921.33). BRENT's TRADE never carried it until this cleanup. WQ-316 is Will's; TERRY recommends SELL; card hard stop Wed 9/30 15:00 ET.

## WHAT I DID THIS SESSION
- **Leg 1 (14:34–15:54):** settle-window proxies; Brent graded-contract RULE; the missed $120 Dated line recorded; COT probe fixed; news sweep. Detail: [archive](archive/STATUS_dated_2026-09-28_1434.md).
- **Leg 2:**
  - post-settle tape;
  - export-ban risk note: breach timings **withdrawn after CATO MR19** (×42 on retail ≠ crack), with corrections sent to WALTER (-016) and TERRY;
  - memory n+3 on `finding_instrument_measures_a_superset_of_the_thesis_subject`.
- **Leg 3 (WQ-329):**
  1. **Assignments routed:** PROME `c3e185152`, WALTER `537ca0e16`. WALTER's R3 test: the lane would have missed Sunday. 6 terms + query **LANDED** (RESEARCH-INTAKE `d5d8c9e`; BRENT concur `590ca37fa`).
  2. **TRADE.md cleanup:** before-image `archive/2026-09-28_cleanup/` (26,511 B, crc32 `7cb1efe4`); holdings refreshed from FORGE; now 14.3 KB (44%). Adds VLO 1 sh, the USO 159C ×2 and an unresolved-broker-facts table. Obligations § 2026-09-28.
  3. **INCIDENTS:** RF-054 Moscow (halted, A-2), RF-055 Novoshakhtinsk (suspended, A-1), RF-056 Ilsky (halt CLAIMED by the attacker side, C-3, MONITORING); RF-050 points to RF-056. HAWK STRIKES has none of the three.
  4. **Measurement** (18:20–18:22): [VLO observables table](research/2026-09-28_vlo-thesis-observables/NOTE.md). Hub NYH−USGC 1.5¢ (bottom decile), Gulf margin $113, 1-day noise ≈ $5. No threshold inferred; 2022 confounded.
  5. **[Phase map](research/2026-09-28_phase-map-this-week.md):** proposals P1–P4 to Will.
  6. **[Entitlements memo](research/2026-09-28_paid-data-entitlements-check.md):** the LSEG and S&P connectors exist but are unauthenticated; the licence is unknown.
  7. **Rotations:** STATUS 91% → 68% (9/28 14:34 block and the 9/07 pointer rotated; 13 graded CATALYSTS rows pruned → `archive/CATALYSTS_pruned_2026-09-28.tsv`, crc32 `325ffc89`). NEXUS 93% → 75%, with VIEW rewritten.
- **$0. No trade, band, grade or thesis change.**

## ⚠️ MY ERRORS / NEAR-MISSES
- **×42 on a retail scenario published as crack breach dates** (CATO MR19). It reached a BOARD headline within ~15 min. Fixed by four corrections; memory n+3.
- **Typed clocks again:** I wrote "19:xx", "~19:0x", "18:4x" and "~18:5x" when `date` read 18:2x. The first three were fixed in my files. The "~18:5x" in `PROME/inbox/processed/…CONCUR-WALTER…` stays (consumed; the commit time is the truth). The memory `finding_a_stamp_written_from_narrative_drifts_from_the_wall_clock` applies.
- The earlier news sweep missed Trump's Sunday line. The lane terms now cover it (~1-day cadence).

## NEXT SESSION (dated, future-verifiable)
1. **Tue 9/29:** last BZX26 GRADED settle (ICE Nov last trade Wed 9/30). HENRY's BRT-12 blind read.
2. **Wed 9/30 ~10:30:**
   - Grade **BRT-29** + **BRT-12** (PREP `setups/2026-09-25_Q3-predictions-grade-PREP.md`).
   - **Cushing:** F-b's second week, graded only on the 9/2 CHANGELOG letter.
   - **Distillate exports** (DOCKET L531): consistent-with, not proof.
   - **Switch to BZZ26:** report M1−M3 as a CALENDAR STEP (phase-map P1 pending Will).
   - Russia diesel-ban decree.
   - After the grade, draft a **Path-B successor** (P3) before the next print.
3. **Wed 9/30 15:00:** USO 159C ×2 hard stop per TERRY's card. Will's hand (WQ-316). Record the outcome in TRADE when a receipt arrives.
4. Read EIA retail wk-9/28. Watch for an export-ban order (IMMEDIATE ⇒ VLO table rows #1–#4 + packets to TERRY/HENRY/WALTER).
5. **Fri 10/2** COT #8 · **Sun 10/4** OPEC+ · **~Mon 10/5** Aramco OSP (Yanbu record-only) · **Tue 10/6** L471 sitting (F1 month) · **Sat 10/24** WQ-264 run ends.
6. INCIDENTS still owed: Kuibyshev + Bashneft-UNPZ 9/22 (hit; processing status unstated; OSPREY packet 9/24). 11 ACTIVE rows past 60d.

## OPEN THREADS / WATCHES
- 🔴 **US diesel export ban:** policy unset; refiner response unknown.
- 🔴 **Yanbu restart:** REPORTED only.
- 🟠 **TERRY's VLO proposal (L535):** returns to Will; BRENT input = the observables table.
- 🟠 **Phase-map P1–P4:** with Will via this session's brief; not filed as WQ rows (PROME's call).
- 🟡 **Data:** ICE gasoil is unavailable (entitlements memo); CME settles are blocked.

## POSITION DECISIONS PENDING
- **WQ-316 (Will): USO Sep-30 $159C ×2, expires Wed.**
- VLO: no rule live; TERRY proposal pending.
- USO 37 sh: no rule (WQ-200 declined).

## MAIL STATE
- **Inbox:** clear. Today: 6 consumed = 6 board_log rows (WALTER -007/-001/-003(deferred)/-008/-010 + the WALTER R3 pointer), all `git mv`'d.
- **Sent in legs 2–3 (all committed):** PROME ×2 (`c3e185152` scope, `590ca37fa` concur) · WALTER ×3 (`6691e5661`, `2d508e43c`, `537ca0e16`) · TERRY ×2 (`4f92f6a15`, `376385da6`). Leg 1's sends are in its archived block. No open outbox.
