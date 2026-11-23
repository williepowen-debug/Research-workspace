---
signal_id: "SIG-W-20261123-029"
date: "2026-11-23"
timestamp: "2026-11-23T22:08:02Z"
dispatched: "2026-11-23T22:08:02Z"
source: "clearinghouse.net; TheStreet Pro, GV Wire, FXEmpire, Newsquawk 11/23; FRED; PR Newswire 302947323; apartmentlist.com 10/28; ers.usda.gov; richmondfed.org; tradingeconomics (helper reads 2026-11-23)"
origin: ["Step 7i release sweep"]
action: ["CARL", "ISHM", "HOMER"]
info: ["FERT", "PROME"]
precedence: "ROUTINE"
signal_type: "context"
confidence: 0.75
confidence_language: "mixed; item 1 rests on one tracker, item 2 on secondary relays"
resources: 1
safety_net: "clear"
cluster: "CONSUMER_STAGFLATION"
domain: "CONSUMER_CREDIT"
entities: ["AFT-v-ED", "S&P Global", "CFNAI", "Fannie Mae", "Apartment List", "ICE"]
word_count: 297
dispatch_note: "Small-items card (10.6). ACTION CARL item 1 (confirm), ISHM 2 and 3, HOMER 4 and 5; INFO FERT; PROME by BOARD diff. BM-20261123-05 not opened: release sweep, items listed here."
event_window: "open"
---
# Small items, release sweep Nov 23: student-loan case AFT v. ED stipulated to dismissal Nov 18 (one tracker, filing unseen); flash PMI sub-detail; Fannie October summary out, figures not obtained; Apartment List 'November' is October data; ICE First Look and ERS not out

# Small items (helper page reads unless marked)

| # | Item | Owner | combo |
|---|---|---|---|
| 1 | AFT v. Department of Education (D.D.C. 1:25-cv-00802): 'on November 18, 2026, all parties submitted a stipulation to dismiss the case without prejudice' (clearinghouse.net, document 71). The 11/23 status conference therefore may not have happened; no 11/23 entry or backlog figure found. CourtListener refused (403); filing unseen. Do not confuse with Havens v. ED (injunction denied 11/18, search summary) | CARL: confirm at the docket | combo:CARL/student-loans |
| 2 | Flash PMI November (secondary: TheStreet Pro, GV Wire, FXEmpire, Newsquawk, 11/23): services new orders weakest since July; factory orders slightly faster; exports fell for the first time in four months; factory jobs second-strongest since July 2021; input costs cooled a second month; selling prices slowed from October's largest rise since August 2022; Williamson about 3% annualized Q4 GDP. Sub-index values not seen. Adds to 20261123-019 | ISHM | combo:ISHM/flash-detail |
| 3 | CFNAI October -0.06 (card 007 item 7 repeat); MA3 -0.05 (September +0.01, revised from +0.03); production -0.07, consumption and housing -0.06 (secondary); 41 of 85 positive | ISHM | combo:ISHM/regional-activity |
| 4 | Fannie Mae October monthly summary: PUBLISHED 11/23 16:05 ET (PR Newswire notice); figures not obtained (fanniemae.com refused). Freddie October not out (index page) | HOMER | combo:HOMER/gse-monthly |
| 5 | Apartment List 'November 2026' report (published 10/28) carries OCTOBER data: rent $1,384, -0.3% m/m, +0.1% y/y, vacancy 7.0%. The end-November edition is not out; HOM-06 is not resolved | HOMER | combo:HOMER/rents |
| 6 | ICE First Look October: no copy found (page lists September as current). ERS Food Price Outlook: due 11/24. Richmond Fed: due 11/24, not out early | HOMER, FERT, ISHM | none |
