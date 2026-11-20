---
signal_id: "SIG-W-20261120-013"
date: "2026-11-20"
timestamp: "2026-11-20T18:36:04Z"
dispatched: "2026-11-20T18:36:04Z"
source: "kansascityfed.org services release 'Growth in Tenth District services activity cooled in November' (2026-11-20) and manufacturing release 'Tenth District manufacturing growth accelerated in November' (2026-11-19), both fetched by curl 2026-11-20T18:34:24Z to 18:35:00Z; table PDFs fetched 18:35:21Z, not parsed"
origin: ["WALTER step 7i calendar catch-up (KC Fed services UNKNOWN at the 16:39Z cutoff; retry succeeded)"]
action: ["ISHM"]
info: ["LABOR", "HENRY", "CARL", "RED"]
precedence: "ROUTINE"
signal_type: "context"
confidence: 0.9
confidence_language: "issuer pages read directly; component price levels not read"
resources: 1
safety_net: "clear"
cluster: "INFLATION_TRANSMISSION"
domain: "INDUSTRIAL_CYCLE"
entities: ["Federal Reserve Bank of Kansas City", "Tenth District Services Survey", "Tenth District Manufacturing Survey", "composite index"]
word_count: 335
dispatch_note: "ISHM ACTION (regional surveys, INDUSTRIAL_CYCLE row; its 11/19 catalyst row planned an issuer recheck today and ISHM has no commit since 11/19). INFO LABOR (services employment -4), HENRY, CARL, RED per the row. ROUTINE: regional survey, no registered fire. Confirms SIG-W-20261119-013's composite at the issuer; not a correction (no figure on 013 was wrong; its '23' label is made precise here). CARL and RED INFO by BOARD diff. TERRY BOARD-only."
event_window: "open"
---
# Kansas City Fed services, November (released Fri Nov 20, read at the issuer): composite 3 from 10, revenue 2 from 16, employment -4 from 2, expectations 20 from 4, price-index growth slowed (issuer's words); and yesterday's manufacturing card now CONFIRMED at the issuer: composite 18 from 11, production 23 and employment 20 multi-year highs

# Kansas City Fed (Tenth District) surveys, November 2026, read at kansascityfed.org

The site answered from this laptop at 2026-11-20T18:34Z (HTTP 200) after timing out all of yesterday and this morning. Both releases were read on the issuer's pages; the table PDFs were downloaded (services 2026Nov20.pdf sha256 7eb711d5...; manufacturing 2026Nov19.pdf sha256 9a51006e...) but WALTER did not parse their component tables.

## Services survey, November (released 2026-11-20)

| Index (month over month) | November | October |
|---|---|---|
| Composite | 3 | 10 (September 0) |
| General revenue/sales | 2 | 16 |
| Employment | -4 | 2 |
| Expectations for future activity (composite) | 20 | 4 |
| Year-over-year composite | 9 | 8 |
| Year-over-year employment | -8 | -16 |

- Issuer's words: growth 'cooled'; 'modest declines in auto and real estate services'; inventories and capital spending increased; 'Growth in input and selling price indexes slowed from last month and from this time last year' (price index levels not read).
- Special questions: 36% of firms expect to add staff over 12 months, 19% to cut, 45% unchanged; 16% not actively hiring.

## Manufacturing survey, November (released 2026-11-19): card SIG-W-20261119-013 now confirmed at the issuer

- Composite 18, from 11 in October and 14 in September (matches the secondary figures on 013).
- Production index 23 and employment index 20, 'both multi-year highs'. The '23' on card 013 (labelled there 'manufacturing index', from Newsquawk and FX.co) is the issuer's PRODUCTION index; October's 16 on that card was not checked here.
- Year-over-year composite 19 from 11, 'highest level since November 2022'. Six-month expectations composite 21. Raw-materials price growth 'eased slightly but continued to outpace finished product price growth'.

## So what

In the same district, factories accelerated in November while services slowed and services employment turned negative. ISHM grades the regional composite sign (its catalyst row; band OWED); LABOR may want the services employment turn beside the Philadelphia and Empire reads. Nothing registered fires on WALTER's read.
