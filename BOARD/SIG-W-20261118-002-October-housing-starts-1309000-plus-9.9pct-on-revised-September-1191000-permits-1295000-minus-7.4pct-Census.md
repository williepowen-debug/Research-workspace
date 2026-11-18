---
signal_id: "SIG-W-20261118-002"
date: "2026-11-18"
timestamp: "2026-11-18T15:19:18Z"
dispatched: "2026-11-18T15:19:18Z"
source: "U.S. Census Bureau, New Residential Construction, October 2026, https://www.census.gov/construction/nrc/current/index.html (read 2026-11-18 about 15:16Z); FRED HOUST, PERMIT"
origin: ["Step 7i calendar catch-up: HENRY/domain/ECON_CALENDAR.md row 'Wed Nov 18 08:30 Housing starts Oct Census'; no BOARD card or owner record found at boot"]
action: ["HOMER"]
info: ["CARL", "REGINALD"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.95
confidence_language: "issuer primary read; composition reading is arithmetic on the published figures, HOMER interprets"
resources: 1
safety_net: "clear"
cluster: "BANK_COLLATERAL"
domain: "HOUSING"
entities: ["U.S. Census Bureau", "HUD", "housing starts", "building permits", "housing completions"]
word_count: 219
dispatch_note: "Housing carve-out (Jul 12): national housing supply -> HOMER action, CARL info (consumer read), REGINALD info (bank collateral). PRIORITY: release-day print, no registered threshold found in HOMER's files for starts or permits. Carded about 1 h 50 min after release (desktop boot at 10:11 ET). CARL INFO by BOARD; TERRY BOARD-only."
event_window: "closed"
---
# October housing starts 1,309,000 SAAR, +9.9% (±16.8%, not significant) on a revised September 1,191,000 (HOMER carried 1,221,000); single-family 864,000 (+4.0%), 5+ units 433,000; permits 1,295,000 (-7.4%), single-family permits 772,000 (-8.7%); completions 1,272,000 (Census, released Wed Nov 18 08:30 ET)

# New residential construction, October 2026 (Census, released 2026-11-18 08:30 ET)

**Source read:** census.gov/construction/nrc/current/index.html, fetched 2026-11-18 about 15:16Z (primary). FRED HOUST 1,309.0 and PERMIT 1,295.0 for 2026-10 agree.

| Series (SAAR) | October | September (revised) | Change | Year on year |
|---|---|---|---|---|
| Starts, total | 1,309,000 | 1,191,000 | +9.9% (±16.8%, not statistically significant) | +2.8% (±16.5%) vs 1,273,000 |
| Starts, single-family | 864,000 | 831,000 | +4.0% (±9.0%) | n/a |
| Starts, 5+ units | 433,000 | n/a in text read | n/a | n/a |
| Permits, total | 1,295,000 | 1,398,000 | -7.4% | -8.7% vs 1,418,000 |
| Permits, single-family | 772,000 | 846,000 | -8.7% | n/a |
| Permits, 5+ units | 475,000 | n/a | n/a | n/a |
| Completions, total | 1,272,000 | 1,194,000 | +6.5% (±13.2%) | -10.4% (±11.6%) vs 1,419,000 |

**What the reader should check (HOMER's call):** September starts are revised DOWN to 1,191,000 from the 1,221,000 HOMER carries, so the October jump is partly off a lower base. Of the +118,000 total move, single-family is +33,000; the rest sits in multifamily (HOMER's standing composition-mask check, KB-HOMER-013). Permits, the forward leg, fell 7.4%, single-family permits 8.7%: starts up, permits down. None of the starts changes is statistically significant at Census's 90% interval.
