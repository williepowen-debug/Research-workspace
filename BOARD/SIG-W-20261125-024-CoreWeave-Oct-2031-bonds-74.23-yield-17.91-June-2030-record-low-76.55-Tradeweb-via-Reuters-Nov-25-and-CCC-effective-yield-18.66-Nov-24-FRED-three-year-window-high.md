---
signal_id: "SIG-W-20261125-024"
date: "2026-11-25"
timestamp: "2026-11-25T17:52:39Z"
dispatched: "2026-11-25T17:52:39Z"
source: "mlq.ai (helper read 12:52 ET); FRED; X posts and one image; roic.ai refused (403)"
origin: ["X 2125610724885950960 @DeItaone", "X 2125624903496040617 @DarioCpx (quoted post read)", "X 2125394343477612548 @fxevolution (image read)"]
action: ["LIQUID", "VULCAN", "BROCK", "TERRY"]
info: ["SAM", "HENRY", "REGINALD", "NEXUS", "VIOLET", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "indicator"
confidence: 0.75
confidence_language: "reports: one Reuters and Tradeweb chain, secondary; FRED at source"
resources: 1
safety_net: "clear"
cluster: "AI_INFRA_CAPEX"
domain: "AI_CAPEX"
entities: ["CoreWeave", "CCC", "Tradeweb", "FRED"]
word_count: 313
dispatch_note: "PRIORITY. ACTION LIQUID (bond against swap basis), VULCAN (issuer), BROCK (combo:BROCK/ai-financing). TERRY BOARD-only (WQ-745 condition context). RED, PROME by BOARD diff."
event_window: "open"
---
# CoreWeave bonds Nov 25 morning (Tradeweb via Reuters, secondary): Oct 2031 notes 74.23 cents, 17.91% yield; June 2030 notes a record low 76.55; CCC effective yield 18.66% [11/24, FRED], the 2020 crisis-peak comparison is a monthly-chart claim FRED's window cannot test; stock has since bounced to 40.22

# CoreWeave cash bonds and the CCC yield

| Object | Read | Basis |
|---|---|---|
| CoreWeave Oct 2031 notes | down 1.92 to **74.23 cents, 17.91%**; Newsquawk carried the yield at 10:22 ET | Tradeweb via Reuters as relayed by MLQ (read) and @DeItaone; Reuters not read; intraday |
| CoreWeave June 2030 notes | down 3.79 to **76.55, a record low** | same |
| Debt, 10-Q for 9/30 | $41.6B recourse, $5.3B non-recourse; **$11.0B principal due in 2027** | MLQ citing the 10-Q; VULCAN holds the filing |
| Stock | 40.22 at 12:51 ET (-4.7%), from a 37.40 low; -10% at the time of the bond read | vendor; the bonds have not been re-read since the bounce |
| CCC effective yield | **18.66% [11/24]**, 18.48 [11/23], 18.61 [11/20], 18.32 [11/19]: the high of FRED's available window (from 11/2023) | FRED BAMLH0A3HYCEY 12:50 ET |
| 'Above the 2020 crisis peak, highest since 2016' | chart read: 18.48 live monthly bar against a dotted 2020 line; **monthly points, not daily peaks**; FRED here starts 2023-11-27 | UNTESTED. A daily 2020 high may be above it |

- **Killed as an inference:** 'shares are already worth close to zero as far as the credit market is concerned' (@DarioCpx). 74 cents is a distressed price, not a zero-equity mark; it is one commentator's reading.
- **Do not add as independent confirmation of the swaps:** bonds and LIQUID's swap reading (5Y 1,314 clean [11/24], card 022) are two instruments on one name; the 11/25 five-year swap trade was cancelled.
- Outright yield includes the Treasury level; the CCC spread was 1,405 bp [11/24] (card 022).
- **So what:** the cash bonds fell with the swaps in the morning, which fits single-name stress. The test is whether they recover with the stock. WQ-745's conditions are TERRY's; no change is asserted here.
