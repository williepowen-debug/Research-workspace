# BRENT SCRATCH — October 4, 2026 (Sunday evening boot + file-integrity sweep; 21:34–22:21 ET)

## CHANGES SINCE LAST SESSION
- Futures reopened: crude initially rallied on the Houthi Saudi/Khurais claim, then fully faded below Friday vendor references by 21:33 ET; equities modestly green, gold/silver and Treasury futures firmer.
- FALCON's own FIRMS pull establishes fresh heat at the 9/10 corridor spot, but the facility, cause and any production/throughput loss remain UNKNOWN.
- Iraq's state-tanker VLCC is a commercial delivery change, not a Hormuz bypass. The viral IEA 325M figure is cumulative, not a fresh release.
- Qatar's winter LNG warning is JERA CEO Yukio Kani's buyer-side expectation, not a QatarEnergy confirmation; force majeure is through November for Asia and December for Europe.

## WHAT I DID THIS SESSION
- Ran full boot twice: sandbox run exposed DNS non-coverage; networked rerun completed. Live threshold board: Brent futures >$100; HY OAS 3.24% (10/1); retail gas $4.465 (9/28). EIA wk-9/25 complete. Boot remains FINDINGS because tanker-liveness is closed-market/stale, four ACTIVE incident rows need re-verification, and LESSONS_INDEX is stale.
- Pulled named energy contracts and the equity/metals/rates futures complex at 21:33 ET; wrote [evening note](research/2026-10-04_evening-futures/NOTE.md).
- Processed WALTER -016/-010/-011/-014: four board-log rows and four `git mv` archive moves. Corrections check passed (0 unreceipted).
- Swept BRENT files for broken/stale/incomplete state. Fixed the EIA local reader's false-incomplete result for the complete saved wk-9/25 report and added a regression test; repaired nine broken local Markdown links; rotated the stale 10/2 STATUS summary and removed the already-graded OPEC+ event from NEXUS's next-decision block. Full record: [audit report](audits/2026-10-04_file-sweep/REPORT.md).
- Structural checks found one protected defect: frozen `workbook/KB.tsv` has three malformed historical rows (109/114/117). It was not edited. Maintained TSVs, identifiers, corrections, catalyst view, prediction-due and receipt scans are clean within scope. A full recursive navigation scan found 486 deeper archive/evidence links with move-induced relative-path drift; hot surfaces + workbook archives are 183/183 valid.
- Updated STATUS, TRACKER and NEXUS_BRIEF. No threshold, gate, prediction, thesis version or trade state moved. **$0.**
- Git pull was prohibited: PROME and WALTER had uncommitted changes outside BRENT at boot. Local tree may not include an unpulled remote commit.

## NEXT SESSION (dated, future-verifiable)
1. **Mon 10/5:** Aramco November OSPs. Check for Aramco/MoE/SPA identification of the 25.252N 48.103E facility or a throughput/production statement; FIRMS alone never counts.
2. **Mon 10/5 regular session:** confirm broker truth for USO Oct-09 $150C ×1 and VLO ×1; do not infer from the 10/1 capture.
3. **Tue 10/6:** October STEO `COPS_OPEC`; WQ-252 crack-month sitting; SPR exchange bids close 12:00 ET.
4. **Wed 10/7 10:30:** WPSR — Cushing, distillate stocks/exports, SPR draw.
5. **~Thu 10/8:** China product-export guidance after Golden Week.
6. **Fri 10/9:** USO $150C sell-or-roll hard stop 15:00 ET; COT-35B #9 (as-of 10/6) after ~15:30 ET.
7. **Wed 10/14:** IEA OMR and VLO-HELD-01 leg-A suspension date; Thu 10/15 WPSR/BRT-31 first print.
8. **Owed:** four ACTIVE incident rows >60d, nine other aged present-tense rows, and the distinct successor-event gaps named in the audit report; tanker-liveness human stamp; substantive LESSONS_INDEX reconciliation; TRADE/FORGE broker mirror after 10/1.
9. **Routine acceptance:** observe first live runs Thu 10/8, Fri 10/9, Wed 10/14 and Thu 10/15; remove the Thursday routine's six default connectors in the UI; reset UTC schedules for EST on 11/1.

## OPEN THREADS / WATCHES
- 🔴 **Saudi corridor heat:** wait for a counting source naming the facility class and loss. Do not price a production hit from FIRMS.
- 🟠 **US diesel/export policy + G7 release:** 100M is the remaining March commitment over four months; diesel amount/split and actual draw schedule UNKNOWN. Principal denied a ban, but B1's signed-text letter remains live.
- 🟠 **Qatar LNG:** buyer expects no quick recovery; force-majeure dates are established, full-winter outage is not Qatar-confirmed.
- 🟠 **China product halt:** size UNKNOWN pending guidance/data.

## POSITION DECISIONS PENDING
- **USO Oct-09 $150C ×1:** recorded open as of 10/1; Will's hand; sell-or-roll by Fri 10/9 15:00 ET. TERRY's 10/2 lean was SELL, but execution since 10/1 is UNKNOWN.
- **VLO 1 sh:** VLO-HELD-01; Sunday rounded product quotes do not grade the settlement rule. B1 not fired.
- **USO 37 sh:** hand-managed (WQ-200). **WQ-192 STAND DOWN** remains binding.

## MAIL STATE
- **Inbox:** WALTER lane clear; top-level clear.
- **Outbox:** no current send owed. Seventeen 9/8 evidence artifacts remain; two are linked from the market-docket owner-read note, so no bulk move was made.

## WORKBOOK HEALTH
- `workbook/LESSONS_INDEX.tsv` is 10d stale vs STATUS; its 27/27 prose/index structure passes, so this needs a genuine reconciliation rather than a blind timestamp. Frozen `workbook/KB.tsv` rows KB-BRT-109/114/117 have an extra blank field and remain unchanged by rule. The saved EIA report is complete after the reader fix. Audit: `audits/2026-10-04_file-sweep/REPORT.md`.
