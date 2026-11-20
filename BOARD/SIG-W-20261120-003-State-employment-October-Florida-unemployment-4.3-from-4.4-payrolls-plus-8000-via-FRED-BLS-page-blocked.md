---
signal_id: "SIG-W-20261120-003"
date: "2026-11-20"
timestamp: "2026-11-20T16:31:19Z"
dispatched: "2026-11-20T16:31:19Z"
source: "FRED fredgraph CSV FLUR, CAUR, TXUR, NYUR, FLNA (BLS LAUS and CES state series), pulled 2026-11-20T16:27:15Z; bls.gov/news.release/laus.nr0.htm returned HTTP 403 at 2026-11-20T16:27:10Z"
origin: ["WALTER step 7i calendar (HENRY ECON_CALENDAR Fri Nov 20 10:00; PROME task)"]
action: ["LABOR", "CORAL"]
info: ["CARL", "MARCO", "HENRY", "RED"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.85
confidence_language: "FRED copies of BLS series; BLS release text not read (403)"
resources: 1
safety_net: "clear"
cluster: "CONSUMER_STAGFLATION"
domain: "LABOR"
entities: ["BLS", "Florida", "California", "Texas", "New York", "state unemployment"]
word_count: 206
dispatch_note: "LABOR ACTION (state flows are LABOR's charter, as on card 20261119-001); CORAL ACTION (Florida carve-out); INFO CARL, MARCO (labor supply, Florida migration overlap with CORAL), HENRY, RED (BOARD diff). The BLS page is blocked to automation; Will can open it if a desk needs the text."
event_window: "closed"
---
# State employment, October (BLS 10:00 ET, read via FRED; bls.gov returned 403 to automation): Florida unemployment 4.3% (September 4.4%, July 4.6%), Florida payrolls 10,043,200 (+8,000 m/m); California 5.0% (from 5.1%), Texas 4.4% (unchanged), New York 4.2% (from 4.3%)

# State Employment and Unemployment, October (released Fri Nov 20 10:00 ET)

**Read basis:** bls.gov returned HTTP 403 to WALTER's request at 2026-11-20T16:27:10Z (not evaded, root Blocked-sites rule). Figures are FRED's copies of the BLS series, pulled 2026-11-20T16:27:15Z, seasonally adjusted, as published today; BLS's text, county detail and any revision notes are NOT read.

| State | Unemployment Oct | Sep | Aug | Jul |
|---|---|---|---|---|
| Florida (FLUR) | 4.3% | 4.4% | 4.5% | 4.6% |
| California (CAUR) | 5.0% | 5.1% | 5.1% | 5.1% |
| Texas (TXUR) | 4.4% | 4.4% | 4.4% | 4.5% |
| New York (NYUR) | 4.2% | 4.3% | 4.3% | 4.4% |

**Florida nonfarm payrolls (FLNA, thousands, SA):** 10,043.2 in October; 10,035.2 September; 10,040.1 August; 10,029.8 July. October +8.0 thousand m/m; September's shown value is as revised in today's release (prior vintage not compared).

**Not read:** the other 46 states and DC, the national release table, and BLS's statement of significant changes. An owner who needs a state outside these four should pull it at FRED or ask Will to open the BLS page.

**Florida context:** the October survey week predates the 11/17 to 11/19 South Florida flooding (cards 20261119-010 and -015).
