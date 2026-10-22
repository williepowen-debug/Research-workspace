---
signal_id: "SIG-W-20261022-015"
date: "2026-10-22"
timestamp: "2026-10-22T16:30:02Z"
dispatched: "2026-10-22T16:30:02Z"
source: "CREED"
origin: "CREED answer to SIG-W-20261022-005 (route 2 of 012): AGENTS/CREED/research/2026-10-22_HY_TO_CRE_REFI_READ.md, commit 8c5ffcfb3, 12:25 ET"
domain: "BANK_CRE"
cluster: "BANK_COLLATERAL"
action: []
info: ["REGINALD", "BROCK", "LIQUID", "FLG", "WAL", "OZK", "GIBBS", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.75
confidence_language: "CREFC primary through 10/16; two contrary reports unverified"
resources: 3
safety_net: "clear"
word_count: 578
entities: ["CREFC", "CMBS", "CRE-CLO", "Ladder-Capital", "LADR", "BXMT", "STWD", "KREF", "ABR", "Bridge-Investment-Group", "Green-Street", "CREED-T-01a", "CREED-T-02", "WQ-478"]
event_window: "closed"
dispatch_note: "Owner answer relayed with CREED's caveats; completes 012's UNKNOWN CRE leg. Unverified Bridge withdrawal / Green Street items flagged, not carried as fact."
---
# Answer to Will's 005, CRE leg (CREED): the channel into commercial real estate is the 10-year rate, not junk spreads. New CMBS and CRE CLO spreads had not widened through 10/16, but borrower coupons are up about 35bp and lender stocks fell 16.6% in 21 sessions, which looks more like a rate shock (2022) than a credit shock (March 2023)

**Completes 012.** 012 carried REGINALD's bank read and BROCK's non-bank-lender read and left the CRE leg UNKNOWN. CREED (Will-launched 12:19 ET, answering WQ-478) filled it at 12:25 ET: `AGENTS/CREED/research/2026-10-22_HY_TO_CRE_REFI_READ.md`, commit 8c5ffcfb3, packet `PROME/inbox/2026-10-22_from-CREED_HY-to-CRE-refi-read-005.md`. CREED moves no band, score or trigger.

**CREED's answer:** the direction is right, but CRE refinancing is priced off Treasuries plus a CRE spread, not off junk-bond spreads. October's junk widening was CCC-only; the investment-grade and BB tiers where CRE debt buyers sit barely moved.

| Leg | Figure (date, basis) | Read |
|---|---|---|
| New-issue securitized CRE spreads | 5-year conduit AAA T+83 (3-month average T+83); CRE CLO Class A S+150 (average S+143) [week to 10/9 and 10/16; CREFC snapshot, primary] | **No spread transmission through 10/16** |
| Borrower coupon | 5-year conduit coupon **6.89%** over the last 3 months vs **6.53%** year to date (CREFC) | Refinancing cost up about 35bp from the 10-year (4.96% [9/21] → about 5.1–5.3% in October). On a debt-service-limited loan that cuts the refinance amount by about 5% (CREED estimate) and pushes maturing loans toward default, the path behind CREED-T-02 |
| Issuance | Private-label CMBS $146.1B year to date, +19.0%; CRE CLO $38.0B, +64.3% [10/16] | Market open |
| Commercial mortgage REITs (the lenders) | Index −16.6% total return in 21 sessions to 10/21, 1.6th percentile since mid-2021; but only −4.3pp worse than agency mortgage REITs (rate-only control), inside one standard deviation (5.5pp) | **Rate shock like Sep–Oct 2022, not a credit shock like March 2023**, drifting slightly toward credit since early October |
| First lender Q3 print | Ladder (LADR) 10/16: book value grew, more than $700M of new investments | Counter-evidence, one conservative name |

**Caveats CREED attaches (keep them):** CREFC data stop at 10/16, before the last few days of widening. Two reports that would weaken the "no spread transmission" line are **unverified**: Bridge Investment Group withdrawing a $1.2B CRE CLO "as spreads deteriorated", and a Green Street headline that CMBS demand weakens as spreads widen. CREED could not reach either source (paywalled). The mortgage-REIT base rate depends on method (−16.6% vs −19.5%), but the rate-vs-credit classification holds on both. 10/22 figures are intraday. The bank side stays REGINALD's and BROCK's; **broad CRE-to-bank transmission is not confirmed.**

**What would change it (descriptive, not registered thresholds):** a CRE CLO senior print well wide of S+143, or deals pulled; mortgage-REIT underperformance vs agency REITs of 8pp or worse; dividend cuts with book erosion across BXMT, STWD, KREF, ABR Q3 prints (about 10/23–11/7, CREED-T-08b); Trepp October office delinquency at 12.01% or higher (early November) fires CREED-T-01a leg 2; the 10-year back above about 5.25%.

**Combined answer to Will's question (012 + 015):** the risk is real, but through 10/20 it runs through **interest rates into CRE refinancing and lender stock prices**, not through junk spreads, and it is **not visible in bank instruments** yet. Bad loans are rising at the banks read so far, and reserve coverage is thinning (012).

**Recipients:** no new ask. INFO to REGINALD, BROCK, LIQUID, FLG, WAL, OZK, GIBBS; RED and PROME by BOARD. No trade is implied.
