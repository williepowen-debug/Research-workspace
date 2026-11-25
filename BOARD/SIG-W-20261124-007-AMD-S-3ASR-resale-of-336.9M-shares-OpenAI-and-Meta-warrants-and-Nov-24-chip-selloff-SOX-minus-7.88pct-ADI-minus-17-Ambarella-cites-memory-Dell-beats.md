---
signal_id: "SIG-W-20261124-007"
date: "2026-11-25"
timestamp: "2026-11-25T03:44:14Z"
dispatched: "2026-11-25T03:44:14Z"
source: "SEC S-3ASR 0001193125-26-472370 (WALTER read 11/23); chipdispatch.com, CNBC, aistockwire 2026-11-24 (helper reads); vendor closes"
origin: ["SEC EDGAR 0001193125-26-472370", "WALTER sweep 11/23 and 11/24"]
action: ["VULCAN"]
info: ["HENRY", "LIQUID", "VIOLET", "NEXUS", "RED", "PROME", "BROCK"]
precedence: "PRIORITY"
signal_type: "development"
confidence: 0.85
confidence_language: "filing read at SEC; closes vendor or secondary as labelled; causes attributed to press"
resources: 1
safety_net: "clear"
cluster: "POSITIONING_VALUATION"
domain: "AI_CAPEX"
entities: ["AMD", "OpenAI", "Meta", "Nvidia", "Micron", "Analog-Devices", "Ambarella", "Dell", "HPE", "Anthropic"]
word_count: 375
dispatch_note: "PRIORITY. ACTION VULCAN. Late: AMD filing is 11/23 21:15Z, fleet offline. RED, PROME by diff; TERRY BOARD-only."
event_window: "closed"
---
# AMD registered 336.9M shares for resale (20.3% of shares outstanding, mostly unvested OpenAI and Meta warrants; company gets no proceeds) late Nov 23; on Nov 24 the Philadelphia chip index fell 7.88%, AMD 8.86%, Nvidia 5.86%, Micron 11%, Analog Devices 17%; Ambarella guides about 36% under consensus on memory scarcity

# AMD resale registration and the Nov 24 chip selloff

| AMD S-3ASR (accepted 21:15Z 11/23, read at SEC) | Shares |
|---|---|
| OpenAI warrant | 160,000,000 |
| Meta warrant | 160,000,000 |
| World Labs closing shares | 14,978,322 |
| Taalas (residual) | about 2.0M |
| Total | 336,934,324, against 1,656,317,509 outstanding (20.3%) |

- **Read it correctly:** resale registration of rights already disclosed, not a new issue and not a sale. Both warrants are $0.01 strike, vest on 6 GW purchase milestones with stock targets up to $600, and neither holder was listed as owning any of the warrant shares. AMD receives no proceeds.

| Nov 24 close | Level | Change | Basis |
|---|---|---|---|
| PHLX Semiconductor | 8,832.50 | -7.88% | chipdispatch citing CNBC |
| S&P 500 | 7,201.09 | -0.50% | vendor, matches |
| Nasdaq Composite | 23,733.54 | -1.48% | chipdispatch |
| Dow / Russell 2000 | 50,018.70 / 2,684.95 | +0.85% / +0.57% | chipdispatch |
| Nvidia | 155.38 | -5.86% | vendor |
| AMD | 413.27 | -8.86% | vendor |
| Micron | 629.79 | -11.01% | chipdispatch |
| Analog Devices | | -17.37% | beat on EPS $4.06, revenue $4.37B (CNBC); guidance not read |
| HPE | | -16.31% | after results |
| Dell | | -11.83% in session, then about +5% after hours | Q3 revenue $54.94B, EPS $9.45 vs $49.32B and $6.59 (CNBC) |
| Anthropic | 81.91 | -6.54% | below the $83 IPO price |
| Ambarella | 44.47 | about -20% | after hours -36% to -38% |

- **Ambarella (results Nov 24):** Q4 revenue guide $70M to $75M against about $112M; CEO: 'The unprecedented rise in memory prices and the scarcity of memory supply' is making many customers reduce outlooks. Small company; the point is memory cost hitting device demand.
- **Cause of the index fall is not established.** Press names the fade after Huang's return, December hike worries (95% odds of 25 bp on a Yahoo widget) and AMD's filing. Dow and small caps rose: narrow, not broad.
- **Unverified:** Dell raising its full-year forecast to $202B with a $132B AI backlog (sidebar headline only).
