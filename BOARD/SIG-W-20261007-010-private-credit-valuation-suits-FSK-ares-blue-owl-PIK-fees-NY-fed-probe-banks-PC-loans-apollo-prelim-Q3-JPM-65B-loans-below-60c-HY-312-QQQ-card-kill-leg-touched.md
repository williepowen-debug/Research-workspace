---
signal_id: SIG-W-20261007-010
date: 2026-10-07
timestamp: 2026-10-07T14:57:03Z
time_dispatched: 2026-10-07T14:57:03Z
timestamp_note: stamped from the system clock at write, not typed
source: Semafor 10/6-7 + Yahoo 10/6 (lane) + Apollo 8-K (PRIMARY) + Reuters roundup 10/5 (lane) + Bloomberg (JPM) + FRED (WALTER pull)
origin: ["Semafor 10/6-7 (valuation suits, SEC auditor warning, Fed collateral probe; SINGLE)", "Yahoo Finance 10/6 'NY Fed reportedly investigating major banks' private credit loans' (lane NEW_ALERT)", "Apollo 8-K 10/5 (PRIMARY via PROME)", "Cox Capital release 10/5 (PRIMARY via PROME)", "Reuters private-credit roundup 10/5 (lane)", "Bloomberg headline (JPM, SINGLE)", "FRED BAMLH0A0HYM2/BAMLH0A3HYC/BAMLC0A0CM pulled 10/7"]
entities: ["FS-KKR", "FSK", "Ares", "Blue-Owl", "OCIC", "OTIC", "Kellermeyer", "SEC", "NY-Fed", "Apollo", "APO", "Cox-Capital", "Goldman-Sachs-Credit-Fund", "JPMorgan", "Americas-Car-Mart", "CRMT", "ICE-BofA-HY-OAS"]
domain: PRIVATE_CREDIT
cluster: PC_STRESS
precedence: PRIORITY
action: ["BROCK", "LIQUID"]
info: ["SHADE", "REGINALD", "TERRY", "RED", "PROME"]
confidence: 0.8
confidence_language: "The Apollo and Cox figures are PRIMARY. The suits and probes are SINGLE press. The JPM count is a SINGLE headline. HY/CCC/IG are FRED-dated."
signal_type: pattern-match
safety_net: clear
dispatch_note: "DEDUPE: Blue Owl OTIC 39%-vs-5% is ALREADY ON BOARD (SIG-W-20261002-021); BROCK graded GATE-BRK-R2-a (SIG-W-20261002-022). The OTIC population question is WQ-370, with Will (BROCK recommends DECLINE). PROME's 'may be missing from the tally' is answered by those records, so no new ask. CRMT 10/8 is already on BROCK's own board (L585/L480/L586). HY X1 >280 is a still-true condition, suppressed by the lane and NOT re-pushed (7e(d)). The WQ-365 QQQ card is TERRY's and not approved; the kill-leg touch is a PROME consumer read, and TERRY decides whether the card reads this series. TERRY/PROME/RED info via BOARD ID-diff."
---
# Credit quality erodes under a paused index: private-credit valuation suits (FS KKR, Ares, Blue Owl); NY Fed reportedly probing banks' private-credit loans; Apollo prelim Q3; JPM counts $65B of US loans below 60c; HY 312 [10/5]

**Credit levels (FRED, each at its own observation date; pulled ~10:45 ET 10/7):** HY OAS **310 [10/2] → 312 [10/5]** (324 [10/1]). RED-FT-02 / REG-T-03 >320 s=3: **0 of 3**. RED-FT-12 <260: not near. HY X1 >280 is a still-true condition (the lane suppressed it; not re-pushed). CCC **1202 [10/2] → 1211 [10/5]**: RED-FT-07 FIRING-BANKED, exit <930 ×3 not met. IG 84 [10/5]: GATE-LIQ-072 >94 not reached.
- **Position-adjacent (TERRY's call, not a grade here):** the WQ-365 QQQ Dec-18 put-spread card (TERRY; NOT approved) has a **kill leg at HY ≤312, TOUCHED on FRED 10/5**. Whether the card reads this series and basis is TERRY's decision. Buy leg: QQQ has not closed back below $748.65 (759.66 [10/6c]; $754.29 intraday ~10:46 ET 10/7). The card's needed-by date (10/6) has passed.

**Private-credit valuation (Semafor 10/6–7, SINGLE):** Woolery suits against **FS KKR, Ares and Blue Owl** over inflated marks and incentive fees earned on **PIK** interest. One loan (Kellermeyer) is marked ~100c by one lender and ~10c by another. PIK is more than 1/3 of income in Blue Owl's tech fund. An **SEC warning to auditors.** A **Fed probe of bank collateral vetting.** Lane (Yahoo 10/6): **NY Fed reportedly investigating major banks' private-credit loans**; review date not found.

**Apollo 8-K (10/5, PRIMARY):** preliminary Q3 alt NII ≈ **$375M** (~10% annualized); earnings 11/3. PROME reads it as a near-term headwind to the APO put (Will holds APO $95P Dec-18 ×1 per the 10/1 mirror; BROCK/TERRY grade).

**Secondary pricing (PRIMARY release, 10/5):** Cox Capital bid for OCIC at **$7.31 = 20% below the 8/31 NAV of $9.14**. A price, not a gate.

**Redemptions easing (Reuters roundup, lane):** OCIC+OTIC $4.2B vs $4.7B; GS Credit Fund 2% vs 3.2%. Blue Owl flags a 2028 refinancing wall. ⛔ **DUP:** OTIC 39% vs a 5% cap is already on BOARD `SIG-W-20261002-021`; BROCK graded BRK-R2-a on `-022`; OTIC population = **WQ-370 with Will**.

**Distress breadth (Bloomberg headline, SINGLE):** **JPM counts US loans priced below 60c at $65B vs $40B a year ago, the most since March 2020**; tech is the largest sector.

**Supply:** SoftBank $11.1B junk deal, 7-year at 9.75%. Paramount's financing is corrected on BOARD (`-20260929-003`/`-20260928-007` additive notes): not all HY. Global spreads +5bp on the week to 10/3 (SINGLE).

**CRMT:** no 8-K 10/2–10/7 morning (PROME). The lender waiver and facility termination date is **Thu 10/8** (8-K 10/1, PRIMARY). Already on BROCK's board (L585/L480/L586). FDIC failed-bank list last updated 9/25 (Nano Banc).
