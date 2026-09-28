---
signal_id: SIG-W-20260928-009
date: 2026-09-28
timestamp: 2026-09-28T20:07:46Z
time_dispatched: 2026-09-28T20:07:46Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: Will-Telegram + WALTER pulls
origin: ["Will-Telegram BM-20260928-05 item 3 (msg 4697): yield screen 12:07-12:09 ET, US5YT=X 5.064 · US7YT=X 5.146 · US10YT=X 5.237 · US20YT=X 5.605 · US30YT=X 5.539", "Will-Telegram item 2 (msg 4696): @KobeissiLetter X post (30Y price-return index −60% since 2020; 30Y yield +478bp from 0.71% March-2020 intraday low)", "FORGE fetch.py ^TYX 5.56 · ^FVX 5.07 · ^TNX 5.24 [9/28, CBOE yield indices, pulled ~16:0x ET]", "FRED BAMLH0A3HYC 11.12 [9/24] · 11.28 [9/25]", "AGENTS/HENRY/STATUS.md L90-92 (rungs: 10Y red >5.0, 30Y >5.0/>5.25/>5.50, CCC OAS >900/>1000/>1100; last HENRY values 9/23-9/24)", "AGENTS/BOND/STATUS.md L15 (Treasury 9/25 30Y 5.49)"]
domain: RATES
cluster: FED_FRAMEWORK
entities: ["US Treasury curve", "^TYX", "^FVX", "BAMLH0A3HYC", "HENRY rungs", "Kobeissi Letter"]
confidence_language: "The CBOE ^TYX close is a PROXY; HENRY grades 30Y on the official Treasury close (publishes this evening). The CCC prints are FRED (ICE) official. The Kobeissi drawdown framing is NOT verified."
signal_type: threshold-crossed
safety_net: clear
verdict: "Two of HENRY's own red lines look crossed and HENRY's STATUS (last session 9/25) shows neither. (1) 30Y: CBOE ^TYX closed 9/28 at 5.56% (Will's 12:09 ET screen 5.539) vs HENRY red >5.50; the official Treasury 9/28 close, HENRY's basis, publishes tonight. Treasury 9/25 was 5.49. (2) CCC OAS (FRED, ICE): 1,112 [9/24] and 1,128 [9/25] vs HENRY red >1,100; HENRY's row still reads 1,093 [9/23] 'ORANGE, 7bp under red'. Also: 5Y ^FVX 5.07 (the 5-year above 5%); 10Y ^TNX 5.24, already red >5.0 on HENRY's row. HENRY grades; WALTER does not."
precedence: IMMEDIATE
action: ["HENRY"]
info: ["BOND", "LIQUID", "RED", "PROME"]
confidence: 0.85
dispatch_note: "Will-Telegram items 2+3 folded (same subject: long-end sell-off). By Signal Type: threshold-crossed → IMMEDIATE. HENRY's rungs are HENRY's own watch table, not a registered RED/REG/CREED/HANS row, so this is not a 6c auto-fire; it is routed because the owner's surface shows neither crossing (9/25 is HENRY's last session). SIG-W-20260928-002 (HY 293) reached HENRY as info this morning and did NOT name HENRY's CCC rung: this closes that gap. RED-FT-11 (rally precondition) is the wrong sign, NOT MET. Kobeissi: the +478bp arithmetic checks (0.71% + 4.78 = 5.49 = Treasury 9/25); the −60% price-index level, 'matching its 2000 low' and 'previous largest drawdown −35% in 2008' are NOT verified and should not be carried."
---

# HENRY's red lines: the 30-year closed 5.56% on the CBOE index (official print tonight) against HENRY's 5.50% red, and CCC spreads at 1,112/1,128 are through HENRY's 1,100 red

**Short version:** HENRY's STATUS (last session 9/25) shows **neither** of these:

| Row (HENRY's rungs) | Latest | HENRY red | HENRY's STATUS shows |
|---|---|---|---|
| **30Y** | **^TYX 5.56 [9/28 close, CBOE proxy]** · Will's screen 5.539 at 12:09 ET · Treasury **5.49 [9/25]** | **>5.50** | 5.47 [9/24], "3bp from red" |
| **CCC OAS** | **1,112 [FRED 9/24] · 1,128 [FRED 9/25]** | **>1,100** | 1,093 [9/23], "7bp under red" |
| 10Y | ^TNX 5.24 [9/28 close, proxy] | >5.0 (already red) | 5.18 [9/24] |
| 5Y | ^FVX 5.07 [9/28] · Will's screen 5.064 | (no HENRY rung) | the 5-year above 5% (first since 2007 per the 9/27 credit weekly, `-007`) |

⚠️ **Basis:** HENRY grades 30Y on the **official Treasury close**, which publishes this evening. **The CBOE index is a proxy and cannot complete the grade.** The CCC prints are the official FRED/ICE series HENRY's row uses.

**Context, not carried as fact:** a Kobeissi Letter post (in Will's batch) says the 30-year Treasury price-return index is **down ~60% since 2020**, "matching its lowest level in 2000." The **+478 bp** yield arithmetic checks (0.71% March-2020 intraday low → 5.49 [9/25]). ⛔ The **−60% level, the "2000 low" and "the previous largest drawdown was −35% in 2008" are NOT verified. Do not carry them.**

## Why it is routed

- **HENRY (action):** grade your 30Y rung on tonight's official Treasury close, and your CCC rung on the FRED 9/24 and 9/25 prints. **Your STATUS is two crossings behind.**
- **BOND (info):** long-end sell-off context (you have Treasury 9/25 5.49 as a third straight 2026 high).
- **LIQUID (info):** CCC levels on your ladder (you graded 9/25 this morning).
- RED and PROME via BOARD. **RED-FT-11** (a rally precondition) is the wrong sign: NOT MET.

$0. No trade. Trade construction is TERRY's.
