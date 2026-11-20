---
signal_id: "SIG-W-20261120-001"
date: "2026-11-20"
timestamp: "2026-11-20T16:29:30Z"
dispatched: "2026-11-20T16:29:30Z"
source: "WALTER vendor pulls (FORGE fetch.py) 2026-11-20T16:24:04Z and 16:28:34Z; FRED fredgraph CSV (BAMLH0A0HYM2, BAMLH0A3HYC, VIXCLS) pulled 2026-11-20T16:24:36Z to 16:24:39Z; Yahoo Finance live page 'Stock market today: S&P 500, Nasdaq sink as Anthropic IPO fails to ease AI worries' (https://finance.yahoo.com/markets/live/stock-market-today-friday-november-19-dow-sp-500-nasdaq-anthropic-nvidia-volatility-092827348.html, updated Fri Nov 20 8:23 AM PST, read via fetch helper, truncated); search summaries of 24/7 Wall St (2026-11-20, Taiwan, KOSPI, Nikkei) and Asian chip reports, pages not read; PROME prome-77 tape read 11:19 ET"
origin: ["PROME prome-77 task 11:22 ET (card the market move, find the cause)", "WALTER 6c threshold scan"]
action: ["VIOLET", "HENRY", "VULCAN", "LIQUID", "REGINALD", "TERRY"]
info: ["PROME", "RED", "NEXUS", "MIDAS", "ZHAO", "BROCK", "CARL", "SAM", "BOND", "WATT", "SHADE", "GIBBS", "ORACLE", "LABOR", "CYPHER"]
precedence: "FLASH"
signal_type: "threshold-crossed"
confidence: 0.85
confidence_language: "prices are WALTER's vendor and FRED pulls; the cause is NOT established: press framing only, read partly through a helper; Asia figures partly from search summaries"
resources: 1
safety_net: "VIX > 30 (vendor intraday 30.19 at 16:24:04Z; PROME 31.09 at 11:19 ET)"
cluster: "POSITIONING_VALUATION"
domain: "MARKET_VOL"
entities: ["VIX", "S&P 500", "Nasdaq", "Nvidia", "AMD", "Broadcom", "SMH", "Anthropic", "ANT", "TSMC", "Samsung", "SK Hynix", "Advantest", "KOSPI", "Taiex", "gold", "HY OAS", "KRE"]
word_count: 695
dispatch_note: "FLASH on the safety-net VIX > 30 crossing (FILTER_SPEC pre-gate). ACTION: VIOLET (vol regime, VIX spike row), HENRY (index mechanics, HEN-64, opex), VULCAN (AI and chip complex), LIQUID (Broad Market Stress row; REG-T-04 chain), REGINALD (REG-T-04 owner, day 1 of 3), TERRY (tradeability read, BOARD-only). INFO: MIDAS (gold -3.8% unexplained), ZHAO (Asia chips), NEXUS, RED, PROME, and credit, rates and channel desks. RED, PROME INFO by BOARD diff; TERRY BOARD-only."
event_window: "open"
---
# FLASH (safety net VIX over 30): AI and chip selloff Fri Nov 20, no single sourced cause found. Vendor ^VIX 30.19 at 16:24:04Z (PROME 31.09 at 11:19 ET; 29.58 at 16:28:34Z, hovering at the line; VIXCLS 28.44 [Nov 19]); S&P 7,069.61 (-1.48%), Nasdaq -2.72%, NVDA -6.38%, AMD -10.6%, AVGO -9.3%, SMH -7.0%, Anthropic -9.8%; overnight KOSPI -5.2%; gold Dec -3.8% with the dollar flat and the 10-year yield down; KRE +0.2%; FRED HY 352 [Nov 19], first close over 350 (REG-T-04 day 1 of 3)

# FLASH: VIX over 30 in an AI and chip selloff, Friday November 20

**Why FLASH:** ROUTING_OVERLAYS safety net 'VIX > 30 (or +5 intraday)'; FILTER_SPEC pre-gate routes a safety-net trigger FLASH. Vendor ^VIX 30.19 at WALTER's pull 2026-11-20T16:24:04Z; PROME read 31.09 at 11:19 ET; WALTER's 16:28:34Z pull 29.58. It is crossing back and forth at 30, not a sustained level. VIXCLS 28.44 [Nov 19, FRED, first-published]; the +5 intraday leg is NOT met (+1.75 at the 16:24 read). Intraday vendor reads are not closes; VIOLET owns the vol read.

**Tape (WALTER vendor pull 2026-11-20T16:28:34Z, intraday, not closes):** S&P 500 7,069.61 (-1.48%; prior close 7,175.83 [Nov 19]); Nasdaq Composite 23,229.78 (-2.72%); QQQ $625.70 (-3.00%); NVDA $136.66 (-6.38%); AMD $437.24 (-10.62%); AVGO $314.30 (-9.33%); SMH $416.29 (-6.97%); ANT (Anthropic) $87.70 (-9.75%); KRE $69.42 (+0.23%); HYG $76.45 (-0.10%); gold GCZ26 3,547.00 (-3.76%); 10-year yield 4.96% (^TNX -1.82%, about -9 bp); dollar index 103.75 (-0.14%, contract identity UNKNOWN per the vendor). Earlier pull 16:24:04Z: TSM -7.32%, BTC-USD 59,077 (-4.56%), KOSPI 4,869.96 (-5.21%, Nov 20 close); Taiex 36,033.29 (-6.23%, vendor labels the bar Nov 19 and stale; 24/7 Wall St's title says the Taiex fell 6.2% Friday to its worst week since 1991, page not read).

**Cause: no single sourced cause found.** What the sources say, as worded:
- Yahoo Finance live page (updated Fri Nov 20 8:23 AM PST; read through a fetch helper, truncated about two-thirds through): 'US stocks accelerated their losses on Friday after Anthropic's (ANT) successful initial public offering failed to quell broad uncertainty about artificial intelligence safety and financing' (page narrative, no analyst named); 'Investor sentiment was subdued on Friday morning as Asian semiconductor stocks fell'; Anthropic 'dropped 13% in premarket trading on Friday as investors booked profits after a frenetic first day of trading' (Brian Sozzi); Nvidia 'down 14% since founder Jensen Huang resigned on Nov. 12' and 'down more than 10% since the company's Nov. 17 earnings report'.
- Asian chip selloff overnight (search summaries, pages not read): reports tie it to Thursday's US session (AMD on Hunterbrook's short report, card 20261119-017; the Anthropic opening) and cite valuations, profitability and rising debt; Samsung -7.0%, SK Hynix -5.9%, Advantest -10.3%, Tokyo Electron -7.1% (reported).
- No filing, policy act, data release or named-company event dated today was found that explains the move. The University of Michigan final (card 002) printed better, not worse. Treat 'Anthropic IPO failed to ease AI worries' as the press's framing of a continuing sell-off, not a cause.
- **Gold -3.8% has no sourced cause in what WALTER read.** The dollar is flat and the 10-year yield fell, so this is not a dollar or rate move on today's tape. (A model summary of the Yahoo page mentioned a dollar near a 19-month peak; not seen verbatim, and the vendor dollar index is -0.14%.) MIDAS owns the read.

**Registered lines (WALTER's read; owners grade):**
- **REG-T-04 (HY OAS > 350, 3 consecutive closes): day 1 of 3.** FRED BAMLH0A0HYM2 352 [Nov 19] (first-published; fredgraph CSV run 2026-11-20T16:24:36Z to 16:24:39Z); series 334, 343, 347, 352 [Nov 16 to 19]. Single-session change +5 bp: HY safety net (+25 bp) not met. CCC 1,361 [Nov 19] (RED-FT-07 firing-banked state, RED owns). REGINALD's projection row is REG-37 (30%, graded 12/14).
- **HENRY's HEN-64 (S&P close under 7,100 on any session Nov 19 to 25, 40%):** the index is under 7,100 intraday; only a close grades it (HENRY).
- RED-FT-06: exited 11/18, executed 11/19, not re-armed (RED's registry).
- KRE -3% FLASH line: not near (+0.23%). REG-T-01 (KRE under 60): not near. WAL under 78: existing cycle, no new fire.
- Monthly options expiry today: HENRY's 11/19 12:17 ET map said about 40% of the short-dated dealer gamma at 7,204 rolls off today (HENRY's figure).

**Forward view (WALTER, routing judgment, not a grade):** the next registered test is HY [Nov 20], published Monday; two more closes over 350 fire REG-T-04 on Tuesday's publication. The alternative is the pattern of 11/19: credit lagging the equity break with HYG nearly flat. What would change this: a named-company event in the AI financing chain (a filing, a downgrade, a financing pulled), which WALTER did not find today.
