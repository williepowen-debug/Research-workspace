---
signal_id: "SIG-W-20261023-002"
date: "2026-10-23"
timestamp: "2026-10-23T04:43:23Z"
dispatched: "2026-10-23T04:43:23Z"
source: "X_BOOKMARKS"
origin: "Will X bookmarks 2113337712749301958 (@rdd147 CRWV, 18:32Z 10/22), 2113414387541102972 (@OddStats QQQ, 23:37Z), 2113431765926793562 (@Barchart Korea, 00:46Z 10/23); bodies read in scan output; images not opened. Checked against WALTER vendor pulls 04:39-04:41Z 10/23 (yfinance) and outlet reports via search (Yahoo Finance, Barchart, Benzinga, Quartz)."
domain: "AI_CAPEX"
cluster: "AI_INFRA_CAPEX"
cluster_secondary: "POSITIONING_VALUATION"
action: ["VULCAN"]
info: ["HENRY", "VIOLET", "BROCK", "ZHAO", "PROME", "RED", "TERRY"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.75
confidence_language: "closes are vendor (not exchange-official); the Lam quote is relayed by outlets, not read at the transcript; bookmark claims on dark-pool prints and margin calls are unverified"
resources: 1
safety_net: "clear"
word_count: 268
entities: ["Lam-Research", "LRCX", "SOX", "SMH", "AMD", "Micron", "Nvidia", "CoreWeave", "CRWV", "QQQ", "Kospi", "SK-Hynix", "Samsung-Electronics"]
event_window: "closed"
dispatch_note: "Folds three bookmarks (CRWV dark-pool claim, QQQ drawdown stat, Korea selloff). VULCAN action because the driver is semis substance (Lam supply constraint); CoreWeave credit stays BROCK/LIQUID per the substance-vs-financing carve-out. TERRY on the line because the FORGE 10/22 mirror holds CRWV and QQQ positions; no trade implied."
---
# US chips fell hardest on October22: SOX -6.72% after Lam Research said supply constraints continue into 2027; QQQ -2.86%, CoreWeave -10.1% to $55.60. Asia on 10/23 is mixed, not a second leg down

**What happened (vendor closes, 10/22):** PHLX Semiconductor index (SOX) 10,731.98, -6.72%; SMH $523.35 (-5.99%); AMD $507.93 (-8.10%); Micron $856.49 (-6.26%); Nvidia $212.21 (-4.40%); Broadcom $323.24 (-4.31%); TSMC ADR $412.35 (-4.52%). Nasdaq-100 28,958.69 (-2.90%), QQQ $704.47 (-2.86%), SPY $763.96 (-1.18%). Amazon $250.38 (-4.56%), Oracle $125.54 (-2.78%).

**Why, per outlets (secondhand):** Lam Research's CEO said on its earnings call that supply-chain constraints on certain components continue to limit chipmakers into 2027; Lam fell about 12% (Yahoo Finance, Barchart, Benzinga). Benzinga adds oil and AI-financing worries as background. The call wording is not read at the transcript.

**CoreWeave (CRWV):** closed $55.60 (-10.1%; 10/21 $61.82), intraday low $54.85 at 15:45 ET. Down 39% from $91.72 on 10/06. ⛔ The bookmark's "dark pool prints down to $53 ... someone big is getting margin called" is UNVERIFIED: $53 is below the lit low, off-exchange prints are often late or negotiated, and no source names a margin call. Do not relay it as fact.

**QQQ drawdown stat:** the @OddStats claim (down 7.99% from a peak inside 12 days; next-day returns of the last six cases all negative) is not reproduced and n=6 is not a forecast. WALTER's check: QQQ close $704.47 vs $759.66 [10/06 close] = -7.27% close-to-close; intraday peak and trough not pulled.

**Asia, 10/23 intraday at 04:39Z (not closes):** Kospi 5,486.35 (-0.86%), 21.0% below 6,941.39 [10/06]; SK Hynix +2.21%, Samsung Electronics -0.70%. "Pounded again" overstates today; the drawdown itself is already on the BOARD (SIG-W-20261022-002). Japan is in SIG-W-20261023-003.

**Ask, VULCAN:** decide whether Lam's 2027 supply-constraint statement bears on any of your semis or capex rows, and read the call primary before grading.
