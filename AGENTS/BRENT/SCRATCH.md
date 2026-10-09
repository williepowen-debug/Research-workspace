# BRENT SCRATCH — October 9, 2026 (4th session: AM boot, housekeeping, Will Q&A; closed 11:2x ET at Will's word)

**Closeout writeback 2026-10-09 ~11:30 EDT.** Claude Code, Opus 5.5 (`claude-opus-5-5`), launched directly by Will; PROME `prome-75` and WALTER `walter-50` coordinated by SendMessage. No pull at boot: origin had nothing new and other desks' work was uncommitted. $0; no trade, threshold, grade or gate change by BRENT.

## CHANGES SINCE LAST SESSION
- **Isaias Cat 3** (120 mph, 959 mb, NHC 7:20 CDT via WALTER -004), ahead of NHC's forecast. Landfall tonight/early Sat, Ocean Springs MS → FL Panhandle; Pascagoula is inside the warning. Shut-in still 62.89% (10/8 survey). Refineries: no cut announced; Chevron's "operational" quote is THURSDAY's. Port of Mobile suspended vessel ops Thu noon.
- **China resumed October product exports at ~3.7 Mt** (Reuters 10/9, unofficial), below September (~4 Mt expected) and August (4.6 Mt actual).
- Hormuz: UKMTO 160-26 hull hit; IRGC claims the "NV Sunshine" LPG strike and threatens ships outside the Strait; GACA confirms the KKIA hits (3 killed, not oil). France's Yanbu protection is still "study phase". Nothing fires.
- Crude flat on the Thursday jump (BZZ26 ~$104); USO $148.81 at 11:14 ET.
- Will ruled boundary #6/#8 (10:29 ET, in WALTER's session) on BRENT's and WALTER's advice. RULINGS § R-2026-10-09-B68.

## WHAT I DID THIS SESSION
- Boot rc=2, then **cleared the boot's only FINDINGS** (LESSONS_INDEX stale): a semantic reconciliation of all 27 lessons found a **real defect**. `,`/`;` separators made L05 invisible to every `--spec` sweep and hid 3 asserts from the conflict scan. Fixed the data and added a `malformed()` lint, falsified first. L18/L19 values aligned to their prose.
- **cot_grade.py Leg-B exact rational compare** (DAEDALUS L546). Rounding was rejected because it would move the letter. Falsified: the old float compare fails an on-edge test. The 9/29 regrade reproduces.
- **SELF-CORRECTION:** Dated Brent (DCOILBRENTEU/RBRTE) at 125–135 is a REAL physical premium, not a feed anomaly. The REGISTRY >$120 line reads above it.
- **SPR basis flag:** the Dallas Fed's ~1.2 mb/d drain is not visible in EIA weekly data (0.06–0.11 mb/d over the last 4 weeks).
- Re-verified 5 aged incident rows (Opus subagent; report `research/2026-10-09_incidents-reverify/`). RF-022 refreshed to 04-21. RF-013 is a DOWNGRADE CANDIDATE pending the FT primary. RF-044 refresh declined.
- Catalysts: pruned 9 graded rows. **China row GRADED.** SPR row stays open (no awards). Added the GAC successor (11/20) and the **#8 switch row (BZZ26 LTD Fri 10/30 → Jan legs Mon 11/2, ICE primary)**.
- Will Q&A: freight/war-risk figures; **structural-cost trade-shape note** (`research/2026-10-09_structural-cost-trade-shape.md`; concept only, TERRY constructs). Curve: WTI−Brent −13.8 → −6.5 (Dec27); diesel crack 104 → 69, vs 2025 −3.6/32. Will stated an escalation view; gave roll facts for the expiring call.
- STATUS rule-5 rotations (89% → 70%), receipts in `archive/`. Inbox 11 consumed = 11 board_log rows.

## NEXT SESSION (dated, future-verifiable)
1. **⚠️ OWED TODAY, NOT DONE (handed to PROME):** COT #9 as-of 10/6 (~15:30 ET Fri 10/9): `cot_grade.py --expect 2026-10-06` + raw `f_disagg.txt`; **grade before the next print (Fri 10/16)**. MMA ~13:00 CDT 10/9 shut-in. 14:28–30 ET settle-window crack (WQ-386 is TERRY's).
2. **USO Oct-9 $150C:** confirm Will's disposition (sold / rolled / expired) and record it in TRADE EXECUTION LOG. If expired ITM, auto-exercise ≈ 100 shares.
3. **Sat 10/10 – Mon 10/12:** Isaias restart read. Grade the CATALYSTS 10/10 row on the REPORT §10 fork. Watch the crack, not crude: a refinery shut WIDENS it, an offshore-only loss compresses it.
4. **10/14:** IEA OMR; November governs WQ-386 through this settle. **Thu 10/15 12:00 ET:** WPSR wk-10/9 = BRT-31 first release + first Isaias print; December governs WQ-386 from 10/15.
5. **10/24:** WQ-264 shadow ends (Saudi resolver). **10/26:** BRT-30. **10/30:** BZZ26 LTD; **11/2** #8 → Jan legs, count restarts.
6. Carried: RF-013 FT/Bashneft primary + re-key; SPR exchange awards; diesel-tax implementation (10/10); Baltic wk-41 (bot-gated; find another route); WQ-252/HEN-46 owner debt; routine deployment parked at CATO.

## OPEN THREADS / WATCHES
- 🔴 Hormuz perimeter widening (IRGC "outside the strait"; Iran: new routes "hostile"; Houthi all-Saudi-facilities threat; Yanbu undefended). Capacity hits, not hull hits, move crude. FALCON owns the ladder. **Trump's no-attack-before-11/3 window** = dated escalation calendar (NYT 3-day plan drafted).
- 🔴 Isaias pre-landfall: Pascagoula/Saraland GAP; LOOP/New Orleans port status UNKNOWN.
- 🟠 Physical-vs-futures: Dated $125–135 vs BZZ26 ~$104. ~$6–7 is month timing [INFERRED]; the rest is prompt scarcity. Daily swings are huge.
- 🟠 Freight/war risk: TD3C $1.22M/day (10/2); war risk 6–10% of hull (FT 10/7–8). Benchmark-vs-fixture gap ($530–600k visible).
- 🟡 Official settlements, current USO weights, quantified Saudi loss: unavailable.

## POSITION DECISIONS PENDING
- **USO Oct-9 $150C ×1: sell-or-roll by 15:00 ET TODAY**, Will's hand, TERRY `MGMT-USO150C-OCT09` (WQ-366). At 11:14 ET: USO $148.81, call $0.23/$0.25 screening; same-strike roll asks Oct-16 $2.98 / Nov-20 $8.85 / Dec-18 $11.55. A Nov/Dec roll exceeds the ~$500 new-risk norm, so a spread-priced roll via TERRY was offered; Will closed without asking, NOT sent.
- USO 37 sh / VLO 1 sh unchanged; VLO exit = TERRY's diesel-crack rule ($109 vs $90.16).

## MAIL STATE (one line per signal)
- Inbox: **clear** (7 WALTER, -008, NEXUS, OSPREY, DAEDALUS consumed; 11 moves = 11 rows).
- Outbox: clear. Sent: OSPREY packet (3.76 not confirmed; 2025 date trap). SendMessage to PROME (ack + closeout memo) and WALTER (#6/#8 advice; switch date).

## WORKBOOK HEALTH
- Boot findings cleared (LESSONS_INDEX). Remaining WARNINGS carried: TANKER-LIVENESS owner-grade, THESIS-WTI-BRENT/DIESEL-CRACK partial coverage, 5 ACTIVE incident rows >60d (re-verified, not refreshable on evidence), 19 present-tense stale (disclosure).
- STATUS 70% of read-cap; NEXUS_BRIEF ~29 KB (89% of budget, rotate next touch).
