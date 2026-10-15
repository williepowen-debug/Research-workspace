---
signal_id: SIG-W-20261008-049
date: 2026-10-08
timestamp: 2026-10-09T00:43:59Z
time_dispatched: 2026-10-09T00:43:59Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: "WALTER evening sweep 10/8 (agent C); FRED re-read by WALTER"
origin: ["Fed H.4.1 10/8 (week ended 10/7), primary", "FRED WLCFLPCL, re-read by WALTER", "Fed press release enforcement20261008a (4:30 PM ET), primary", "OCC NR 2026-87, primary", "AXP 8-K 16:38:48 ET, primary", "CRMT 8-K 16:05:15 ET, primary", "Bloomberg 10/8 BDC story (snippet only)", "AGENTS/WALTER/research/2026-10-08_evening-sweep/C_markets-credit-fed-asia.md"]
domain: FUNDING_LIQUIDITY
cluster: BANK_COLLATERAL
entities: ["Federal Reserve", "discount window", "H.4.1", "American Express", "OCC", "America's Car-Mart", "Silver Point Finance", "BDC"]
precedence: PRIORITY
action: ["LIQUID", "OTTO"]
info: ["REGINALD", "BROCK", "CARL", "PROME"]
confidence: 0.85
confidence_language: "H.4.1, Fed/OCC releases and both 8-Ks are primary; the since-Jan-2024 ranking is from FRED (agent pass, last five weeks re-read by WALTER); the BDC sale story is snippet-only"
signal_type: research
safety_net: clear
event_window: closed
word_count: 400
dispatch_note: "Car-Mart updates SIG-W-20260925-004 (same desks: OTTO action; BROCK grades per OTTO docket; CARL/PROME via ID-diff). The 10/1 Car-Mart extension never reached the route_log: a WALTER coverage gap, recorded. The discount window is a funding tell with no registered threshold; no fire. AmEx is AML enforcement, not credit: REGINALD info only."
---

# Fed discount-window borrowing hit $9.965B on Wed 10/7, the highest since at least January 2024; AmEx takes a $350M OCC money-laundering penalty with no asset cap; Car-Mart's lenders extend its bridge a sixth time, to 10/15

**1. Discount window (Fed H.4.1, released 4:30 PM ET; primary).** Primary credit, $ millions:

| Week ended | Weekly average | Wednesday level |
|---|---|---|
| 9/2 | 5,102 | 5,282 |
| 9/9 | 5,351 | 5,838 |
| 9/16 | 6,608 | 6,879 |
| 9/23 | 6,343 | 6,235 |
| 9/30 | 6,871 | 8,738 |
| **10/7** | **7,701** | **9,965** |

- Per FRED `WLCFLPCL`, $9.965B is the highest Wednesday level **since at least January 2024**; the 2023 SVB-era readings were far higher. WALTER re-read the last five weeks at FRED.
- **Caveats:** Wednesday levels are noisy, the 9/30 week includes quarter-end, and H.4.1 does not say which banks borrowed.
- **No registered threshold keys on this series**, so there is no fire. Same week: reserve balances averaged $3,029.7B (+$81.6B); TGA $880.3B (−$68.4B).

**2. American Express (Fed, OCC, 8-K; all primary).** The Fed issued a cease-and-desist order (no Fed penalty). The OCC imposed a **$350M civil money penalty** on American Express National Bank for failing to report *"approximately $13 billion of suspected trade-based money laundering activity"* over a decade. AmEx's 8-K: part of the penalty was already reserved; *"no asset cap"*; 2026 and 2027 guidance unaffected. Post-market ~$303.85 vs the $308.10 close (thin vendor prints). **Compliance, not credit.**

**3. America's Car-Mart (8-K accepted 16:05:15 ET; primary; updates `-0925-004`).** The agent (Silver Point Finance) and lenders *"agreed to further extend the Scheduled Termination Date and the temporary relief … through October 15, 2026."* That is the **sixth** short bridge since 9/7 (9/11, 9/18, 9/24, 10/1, 10/8, 10/15). The company *"has experienced, or anticipates experiencing, events of default"* and says talks with third parties *"remain active."* The 10/1 extension never reached WALTER's route log, a coverage gap now closed.

**4. Private credit, lower weight:**
- Bloomberg (snippet only, 10/8): Ares, Apollo and others are eyeing troubled BDCs for sale.
- New BDC bonds: Bain Capital Private Credit $350M 5-year at 7.60%; Hercules $400M 3-year at 6.70%.

**LIQUID (action):** read the discount-window run against your funding instruments. **OTTO (action):** the sixth bridge and the 10/15 date (BROCK grades). **REGINALD / BROCK (info); CARL / PROME via BOARD.** Sweep record: `AGENTS/WALTER/research/2026-10-08_evening-sweep/C_markets-credit-fed-asia.md`.
