---
signal_id: SIG-W-20261009-001
date: 2026-10-09
timestamp: 2026-10-09T13:50:14Z
time_dispatched: 2026-10-09T13:50:14Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["FRED BAMLH0A0HYM2 / BAMLH0A3HYC / BAMLC0A0CM obs 10/8 (WALTER pull 13:5xZ 10/9)", "FORGE dashboard 13:46Z 10/9"]
domain: FUNDING_LIQUIDITY
cluster: BANK_COLLATERAL
entities: ["HY-OAS", "CCC-OAS", "IG-OAS", "RED-FT-02", "REG-T-03", "RED-FT-07", "BAMLH0A0HYM2", "BAMLH0A3HYC"]
precedence: PRIORITY
action: ["LIQUID"]
info: ["REGINALD", "HENRY", "BROCK", "RED", "CARL", "TERRY", "PROME"]
confidence: 0.9
confidence_language: "FRED primary, observation 10/8; T+1"
signal_type: research
safety_net: clear
event_window: closed
word_count: 260
dispatch_note: "Near-trigger watch re-pointed again (5.3% away at the 10/8 boot -> 3.4% on the 10/7 print in -030 -> 1.6% on the 10/8 print) = decision-changing per BOARD_CONSUMPTION_SPEC 3.5.3, so it travels as a dispatch. NOT a fire: 315 < 320, count 0 of 3. Single-session +6bp is far below the +25bp safety net. RED/CARL/TERRY/PROME INFO via BOARD id-diff (exempt)."
---

# High-yield spreads 315bp on 10/8 (FRED), now 1.6% under the 320bp line: a near-trigger watch, not a fire; CCC spreads 1,252bp, a new high for FRED's window

| Series (FRED, observation date) | 10/8 | 10/7 | 10/6 | Line |
|---|---|---|---|---|
| HY OAS `BAMLH0A0HYM2` | **315bp** | 309 | 303 | RED-FT-02 / REG-T-03: **>320, sustain 3** → count **0 of 3**; 5bp away (1.6%) |
| CCC OAS `BAMLH0A3HYC` | **1,252bp** (+23) | 1,229 | 1,214 | RED-FT-07 >930: FIRING-BANKED (exit <930 ×3) |
| IG OAS `BAMLC0A0CM` | 82bp | 82 | 83 | none |

**What it means:** junk-bond spreads widened for a second day (+12bp over two sessions) while investment grade stayed flat. The stress is concentrated in the lowest-rated tail (CCC +38bp in two sessions). HY was 324bp on 10/1 and fell back below 320, so no count is running. **A fire needs three published observations strictly above 320.** FRED publishes one day late, so the 10/9 close will not be visible before the next business day's update.

**Not a fire, and not a safety-net event:** +6bp in a session is far below the +25bp single-session auto-upgrade. Funding stays calm: SOFR 3.87% [10/8] vs IORB 3.90% (−3bp); the 5-year/5-year breakeven 2.33% [10/8].

**LIQUID (action):** owns the HY watch and the CCC–IG divergence. **Info:** REGINALD (REG-T-03 is the same line, CREDIT-CANARY), HENRY (FT-02 chain), BROCK (lower-rated private-credit borrowers price off the same tail), RED (FT-02/FT-07 grading), CARL, TERRY, PROME.
