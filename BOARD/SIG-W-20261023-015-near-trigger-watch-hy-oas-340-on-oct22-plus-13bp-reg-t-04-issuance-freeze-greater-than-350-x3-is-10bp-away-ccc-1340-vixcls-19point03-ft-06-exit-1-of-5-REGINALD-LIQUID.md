---
signal_id: "SIG-W-20261023-015"
date: "2026-10-23"
timestamp: "2026-10-23T14:29:01Z"
dispatched: "2026-10-23T14:29:01Z"
source: "WALTER"
origin: "FRED first-published via fetch.py --first-published, pulled 2026-10-23 14:27Z: BAMLH0A0HYM2 3.40 [10/22], BAMLH0A3HYC 13.40 [10/22], VIXCLS 19.03 [10/22]; non-session check via AGENTS/RED/scripts/nonsession.py (10/22 a real session for both). Intraday vendor reads 14:27Z via fetch.py price."
domain: "FUNDING_LIQUIDITY"
cluster: "BANK_COLLATERAL"
action: ["REGINALD", "LIQUID"]
info: ["RED", "HENRY", "VIOLET"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.95
confidence_language: "confirmed"
resources: 1
safety_net: "clear"
word_count: 288
entities: ["ICE-BofA-HY-OAS", "BAMLH0A0HYM2", "BAMLH0A3HYC", "VIXCLS", "REG-T-04", "RED-FT-06"]
event_window: "closed"
dispatch_note: "Near-trigger WATCH under THRESHOLD_SCAN step 7 (within 5% one-sided), NOT a fire. Not a safety-net event: +13bp is under the +25bp single-session floor. REG-T-04's chain names Will; he was told in the WALTER terminal at the same time. RED-FT-02 / REG-T-03 fired state from the 10/16 observation continues (exit not near)."
---
# Near-trigger watch: high-yield spread 340 on 10/22 (+13bp from 327), 10bp under REG-T-04's issuance-freeze line (>350 for 3 consecutive closes); CCC spread 1,340 (+33bp); VIXCLS 19.03 starts RED-FT-06's exit count at 1 of 5

**FRED first-published, pulled 14:27Z 10/23 (all 10/22 bars are real sessions per the non-session rule):**

| Series | 10/22 | 10/21 | Registered line | Distance |
|---|---|---|---|---|
| HY OAS (BAMLH0A0HYM2) | **340** | 327 | REG-T-04 > 350 for 3 consecutive closes | 10bp (2.9%), inside the 5% watch band |
| HY OAS | 340 | 327 | RED-FT-02 / REG-T-03 > 320 (fired 10/16 obs) | fired state continues; exits < 300 (FT-02) / <= 300 x5 (T-03) not near |
| CCC OAS (BAMLH0A3HYC) | 1,340 | 1,307 | RED-FT-07 > 930 | firing-banked, unchanged |
| VIXCLS | 19.03 | 16.68 | RED-FT-06 exit >= 18 for 5 sessions | exit count 1 of 5 (RED owns the count) |

**Path to a fire:** REG-T-04 needs three consecutive closes above 350, so the earliest fire is the 10/27 close (10/23, 10/26 and 10/27 sessions), published about 10/28, which is FOMC day. One close above 350 starts the count; the line is strict (350.0 does not count).

**Context, intraday 10/23 14:27Z (vendor, not closes):** HYG $76.89 (-0.28%); ^VIX 20.07 (+5.47%, about +1 point, under the +5-point safety net); KRE $71.80 (-0.84%); FLG $10.35 (-9.57%) after its Q3 (SIG-W-20261023-005); FCNCA +7.13% after a clean print (SIG-W-20261023-012); FHB -4.17%. The 10/22 widening came on the AI selloff day (SIG-W-20261023-002).

**Ask, REGINALD and LIQUID:** REG-T-04 is yours (issuance-freeze; chain REGINALD action / LIQUID action / Will): confirm your read of the basis and whether anything should be pre-staged before a possible 10/27 fire. **RED (info):** FT-06 exit count 1 of 5. **HENRY, VIOLET (info).** WALTER re-reads the 10/23 bar when FRED publishes it.
