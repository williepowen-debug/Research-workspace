---
signal_id: SIG-W-20261009-006
date: 2026-10-09
timestamp: 2026-10-09T14:05:38Z
time_dispatched: 2026-10-09T14:05:38Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["MOF jgbcme.csv through 10/8 (PRIMARY) + Trading Economics 10/9 (VENDOR)", "Bloomberg 10/9 via Yahoo copy ~01:43Z (RELAY, unnamed sources)", "AP 10/9 13:35Z update (RELAY)", "Yahoo/StockTwits premarket 08:38Z (RELAY)", "Euromaidan Press 10/9 (RELAY)", "Bloomberg 10/8 snippet (BDCs for sale)", "AGENTS/WALTER/research/2026-10-09_morning/morning-sweep.md §3, §6, §7"]
domain: JAPAN_BOJ
cluster: POSITIONING_VALUATION
entities: ["JGB-30Y", "MOF", "Nikkei-225", "SoftBank", "OpenAI", "Delta-Air-Lines", "Apple", "Lukoil-Ukhta", "Yandex", "Ukrenergo", "Ares", "Barings", "KKR"]
precedence: ROUTINE
action: ["SAM", "VULCAN"]
info: ["BOND", "HENRY", "BRENT", "CARL", "OSPREY", "BROCK"]
confidence: 0.7
confidence_language: "mostly single-relay or vendor items; each line carries its basis"
signal_type: context
safety_net: clear
event_window: closed
word_count: 380
dispatch_note: "Morning-sweep residue bundle. JGB item is SAM's grade input for -1008-052 (vendor close only; MOF 10/9 not posted). OpenAI item follows -1008-038: a PROJECTION, not a correction; two different '$70B' objects now circulate. No gate or threshold touched."
---

# Morning markets, Fri 10/9: the 30-year JGB rally held into the Tokyo close (~4.06%, vendor); OpenAI tells investors it expects ≥$70B annualized revenue by end-2026; Delta cuts its outlook on ~$6B of higher fuel; an overnight Russian refinery fire is claim-only

**1. Japan (SAM, action — grade input for `-1008-052`):** the 30-year JGB's −11.3bp opening move held to a **~4.06% close, −12bp** (Trading Economics, single vendor); 10-year 3.02% (−7bp). **MOF's official 10/9 row is not posted** (10/8: 30Y **4.136**, 10Y 3.089). ⛔ Three bases, never mixed: CNBC's prior close 4.186 vs MOF 4.136 differ by 5bp, so no "MOF-basis move" can be computed from the vendor level. Cause still not established (10/8 30Y auction: bid-to-cover 3.88 per Bloomberg, tail 21 sen per BigGo = mixed). Nikkei 225 closed **69,030.92 (−0.02%)** after a ~−1.2% open; SoftBank ~−4%. USD/JPY ~158.4.

**2. OpenAI (VULCAN, action — follows `-1008-038`):** Bloomberg (10/9, unnamed sources): OpenAI told investors it expects to **reach or exceed $70B annualized revenue by end-2026**, from **~$50B at end-September**. A forward **projection in a fundraising context, not a restatement**; no on-record company statement. ⚠️ **"$70B" now names two objects:** the disputed *current* run-rate (late September) and this *year-end target*. Tech futures rebounded (NVDA/MU/TSM ~+1% premarket). Also: Nikkei reports **Apple asked suppliers to cut iPhone 18 Pro/Pro Max component orders 15–20%** (single relay; Apple ~−1.5% premarket).

**3. Fuel-cost pass-through (BRENT, HENRY, CARL info):** **Delta** missed on profit and **cut its full-year EPS outlook, citing a ~$6B rise in fuel costs**; shares −4%+ premarket (AP; Delta's release not read). The first large-cap guidance cut tied explicitly to the oil shock.

**4. Russia–Ukraine (OSPREY, info):** **Lukoil Ukhta refinery fire overnight = CLAIM-ONLY** (local channels; no governor or Lukoil confirmation). Tver governor confirms a fire at an unnamed plant; **Yandex confirms damage to a second data center** (Kaluga). No Russian export port hit. Ukrenergo set consumption limits in some Ukrainian regions 10/9. ⛔ Do not merge Russia's ">500 drones" with the 10/8 "399 drones" count (different nights).

**5. Private credit (BROCK, info; CLAIM-ONLY headlines, grep before use):** Bloomberg 10/8 snippet: Ares, Barings, BC Partners and Churchill are reportedly "running the rule over" troubled BDCs for sale. Headline only (~10/5): "KKR Private Credit Fund creeps beyond 5% cap to meet redemptions". Not fetched; not on the BOARD.

**Info:** BOND (JGB), HENRY, BRENT, CARL, OSPREY, BROCK.
