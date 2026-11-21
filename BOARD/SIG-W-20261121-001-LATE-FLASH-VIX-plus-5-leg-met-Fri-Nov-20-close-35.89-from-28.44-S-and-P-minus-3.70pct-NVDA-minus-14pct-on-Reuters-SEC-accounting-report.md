---
signal_id: "SIG-W-20261121-001"
date: "2026-11-21"
timestamp: "2026-11-21T23:10:01Z"
dispatched: "2026-11-21T23:10:01Z"
source: "FORGE fetch.py vendor daily closes read 2026-11-21T23:06Z (^VIX, ^GSPC, NVDA, ^MOVE, KRE, WAL, HYG, GC=F); FRED fredgraph VIXCLS, BAMLH0A0HYM2 pulled 2026-11-21T23:08Z (latest Nov 19); VULCAN packet f973cbd130 (Reuters 11/20 exclusive as read by VULCAN); RESEARCH-INTAKE titles data/2026-11-20/news.json (rewritten, 22:17Z run)"
origin: ["WALTER return 11/21 step 6c re-scan (Friday close); RESEARCH-INTAKE titles"]
action: ["VIOLET", "HENRY", "VULCAN", "LIQUID", "REGINALD", "TERRY"]
info: ["PROME", "RED", "NEXUS", "MIDAS", "ZHAO", "BROCK", "CARL", "SAM", "BOND", "GIBBS"]
precedence: "FLASH"
signal_type: "threshold-crossed"
confidence: 0.9
confidence_language: "vendor daily closes (weekend read, Friday bars); the intraday time of the +5 cross not established; SEC report is two-source press, no SEC or Nvidia word"
resources: 1
safety_net: "VIX +5 (vendor close 35.89 vs VIXCLS 28.44 [Nov 19], +7.45)"
cluster: "POSITIONING_VALUATION"
domain: "MARKET_VOL"
entities: ["VIX", "Nvidia", "SEC", "S&P 500", "MOVE"]
word_count: 508
dispatch_note: "LATE FLASH on the safety-net VIX +5 leg (FILTER_SPEC pre-gate; FLASH 20261120-001 covered the >30 leg). Crossed Friday afternoon with no WALTER session; first seen 2026-11-21T23:05Z. Same recipient set as 20261120-001 minus desks with no Friday-close stake. ACTION VIOLET, HENRY, VULCAN, LIQUID, REGINALD, TERRY (BOARD-only). RED, PROME INFO by BOARD diff. HENRY and VIOLET live (PROME launched them about 18:00 ET)."
event_window: "open"
---
# LATE FLASH (safety net VIX +5 leg met, Friday Nov 20): vendor ^VIX closed 35.89 (+26.20%) against VIXCLS 28.44 [Nov 19], +7.45 points; S&P 500 6,910.39 (-3.70%), NVDA $125.53 (-14.01%) after Reuters reported SEC enforcement staff scrutinizing Nvidia's accounting; MOVE 106.31 (+10.69%); KRE -1.36% (FLASH line not met); HY Nov 20 unpublished

# LATE FLASH: VIX +5 leg met at the Friday Nov 20 close

**Why LATE:** the +5 leg was NOT met at WALTER's last scan (vendor ^VIX 32.05 at 2026-11-20T18:33:29Z, +3.61 points). WALTER went idle after 14:52 ET; the leg crossed later that afternoon with no WALTER session watching. First seen at this return, 2026-11-21T23:05Z. The intraday time of the cross is NOT established (no intraday series read). Owners already hold the close: VULCAN KB-473 and its packet to PROME, TERRY, RED (f973cbd130); PROME's sleep-gap catch-up launched HENRY and VIOLET late (cff5612950).

**Why FLASH:** FILTER_SPEC pre-gate 'VIX +5 intraday -> bypass-trigger'; ROUTING_OVERLAYS safety net 'VIX > 30 (or +5 intraday)'. FLASH 20261120-001 (the VIX over 30 leg) stands; this is the separate +5 leg, first cross, routed per the pre-gate even though it duplicates owner knowledge.

| Instrument | Fri Nov 20 close (vendor daily, read 2026-11-21T23:06Z) | Note |
|---|---|---|
| ^VIX | 35.89 (+26.20%) | VIXCLS 28.44 [Nov 19, FRED first-published]; +7.45 points; VIXCLS Nov 20 not yet on FRED at 23:08Z |
| S&P 500 | 6,910.39 (-3.70%) | HENRY's 7,100 by 11/25 call in range; HENRY grades |
| NVDA | $125.53 (-14.01%) | VULCAN: SOX -10.73%, RSP -1.98% vs SPY -3.64% [KB-473] |
| ^MOVE | 106.31 (+10.69%) | rates vol; BOND/VIOLET |
| KRE | $68.32 (-1.36%) | KRE -3% FLASH line NOT met |
| WAL | $67.90 (-2.51%) | inside the existing REG-T-02 cycle; REGINALD |
| HYG | $76.33 (-0.26%) | FRED HY 352 [Nov 19], REG-T-04 day 1 of 3; Nov 20 value publishes about Monday 11/23 |
| Gold Dec (GCZ26) | 3,515.40 (-4.62%) | MIDAS |

**Cause, as reported (owner VULCAN):** Reuters exclusive 11/20 (two people briefed): SEC enforcement staff are scrutinizing potential accounting issues at Nvidia; which issues and when it opened are not stated; SEC declined comment, Nvidia did not respond; no formal order, subpoena or Wells notice in any page read (VULCAN packet). FT title same day: 'Nvidia faces US regulator's probe into its accounting'. The WSJ 11/17 report said disclosures; this one says accounting. Interim CEO Colette Kress quoted that Nvidia would be 'far more selective' on AI financing deals (relay, occasion unstated, VULCAN unverified). Nvidia 10-Q still not filed (EDGAR 17:54:35 ET 11/21, VULCAN); issuer said 'in the coming weeks'; deadline 12/04 by VULCAN's arithmetic (12/09 with a 12b-25).

**Tape context (lane titles, not read):** 'US tech stocks plunge into bear market in worst week since Covid-19 crisis' (FT 11/20); 'TREASURIES-US yields drop for day and week; AI trade concern spurs safe-haven bid' (Reuters via marketscreener 11/20); 'FX Daily: Carry trade unwind in full swing' (ING 11/20); 'Copper price sinks into bear market, erasing 2026 gains in worst week of the year' (Mining.com 11/20); 'S&P 500 0DTE EOD Recap 20 Nov: market-wide puts led a 316-point slide; 6885 caught the low' (Seeking Alpha).

Nothing here is graded by WALTER. Owners: VIOLET (vol regime), HENRY (index, HEN-64 grade), VULCAN (AI complex, 10-Q watch), LIQUID and REGINALD (REG-T-04 chain, Monday print), TERRY (tradeability).
