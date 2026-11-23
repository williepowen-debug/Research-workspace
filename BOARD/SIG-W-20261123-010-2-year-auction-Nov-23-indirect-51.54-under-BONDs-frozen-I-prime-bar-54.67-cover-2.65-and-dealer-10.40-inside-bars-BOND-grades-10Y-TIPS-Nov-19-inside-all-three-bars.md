---
signal_id: "SIG-W-20261123-010"
date: "2026-11-23"
timestamp: "2026-11-23T19:00:39Z"
dispatched: "2026-11-23T19:00:39Z"
source: "TreasuryDirect TA_WS securities/auctioned, 2026-11-23T18:57Z (2Y updated 13:03:53 ET; TIPS updated 11/19 13:05:53); BOND registry/auction_bars and STATUS 11/18; WebSearch; newyorkfed.org (helper read)"
origin: ["Will in session 13:56 ET: GPU review items, Williams speech and Treasury auctions"]
action: ["BOND"]
info: ["LIQUID", "NEXUS", "HENRY", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "threshold-crossed"
confidence: 0.95
confidence_language: "official auction record; shares computed by WALTER; grade not run"
resources: 1
safety_net: "clear"
cluster: "FED_FRAMEWORK"
domain: "UST_FOREIGN"
entities: ["US Treasury", "91282CRY9", "91282CRE3"]
word_count: 355
dispatch_note: "PRIORITY: a registered BOND bar reads crossed (composition marker, not a WALTER safety-net row). ACTION BOND (grade 91282CRY9 and 91282CRE3). INFO LIQUID, NEXUS, HENRY; RED, PROME by BOARD diff. BOND not in ListAgents at 13:58 ET, last commit 11/18, dark 5 days vs its p75 of 4: rule 13 doorbell to PROME."
event_window: "open"
---
# 2-year auction Nov 23: indirect share 51.54% is 3.13 points under BOND's frozen I-prime bar 54.67 (I-prime read as fired on WALTER's arithmetic; BOND grades and owns the clean-auction counter); cover 2.65, dealers 10.40% and indirect minimum all inside bars; 10Y TIPS Nov 19 inside all three of its bars

# Treasury auctions, read at TreasuryDirect 2026-11-23 18:57Z

Shares are percent of competitive awards inside the offering amount, computed by WALTER from the TreasuryDirect TA_WS record (par awarded by bidder class over the competitive subtotal). BOND's grader was NOT run; BOND grades.

| Measure | 2Y `91282CRY9` 11/23 ($69B) | BOND frozen bar (11/18) | Reads |
|---|---|---|---|
| Indirect | 51.54% ($35.03B of $67.97B) | I-prime 54.67 | **under by 3.13 points** |
| Indirect, OLD minimum | 51.54% | 45.68 | not met (+5.86 points) |
| Dealer | 10.40% | max 24.12 | inside (-13.72 points) |
| Bid-to-cover | 2.65 | min 2.44 | inside |
| Direct | 38.06% | none | |
| High yield | 4.700% (median 4.650) | none | secondary source (helious.io, search summary): stopped 0.3 bp through when-issued |

| Measure | 10Y TIPS reopening `91282CRE3` 11/19 ($19B) | BOND frozen bar (11/16) | Reads |
|---|---|---|---|
| Indirect | 68.56% | 56.08 | inside |
| Dealer | 6.03% | 17.79 | inside |
| Bid-to-cover | 2.43 | 2.20 | inside |
| High yield | 2.903% | none | not a counter auction (BOND STATUS) |

**What would follow on BOND's letter (BOND decides):** STATUS 11/18 holds the clean-auction counter at 2; under WQ-536 A a REGISTERED I-prime fire resets it. The 11/23 bar file `registry/auction_bars/2026-11-23_91282CRY9.json` was frozen 11/18, before the auction.

**Counter-read, stated so it is not lost:** this is a composition marker, not weak demand. Cover was above the minimum, dealers took a small share, and direct bidders took 38.06%. The 10/26 2Y was lower still at 45.68% indirect (audit only).

**Next:** 5Y `91282CRZ6` 11/24 (I-prime 59.42); 7Y `91282CSA0` 11/25 (57.43). The 9-day bill (11/19, $15B) covered 3.97, high 3.910%; indirect 45.94%, dealer 52.09% (card 20261123-008 item 6 context).

**Not found:** no NY Fed Williams text or report dated 11/23. NY Fed's listing shows no Williams entry after 9/29; the 11/23 page URL is not found. Wire reports of 11/12 to 11/13 and 11/17 remarks exist (search summaries: another hike likely, no dramatic action). Remarks later today stay possible: UNKNOWN.
