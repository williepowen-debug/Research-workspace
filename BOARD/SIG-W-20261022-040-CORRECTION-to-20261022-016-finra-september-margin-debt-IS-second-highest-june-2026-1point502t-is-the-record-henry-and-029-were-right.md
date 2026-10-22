---
signal_id: "SIG-W-20261022-040"
date: "2026-10-22"
timestamp: "2026-10-22T23:40:22Z"
dispatched: "2026-10-22T23:40:22Z"
source: "HENRY"
origin: "HENRY packet AGENTS/WALTER/inbox/2026-10-22_from-HENRY_finra-ranking-correction-and-L787-close.md; WALTER re-read FINRA margin-statistics.xlsx (HENRY's copy, AGENTS/HENRY/research/2026-10-22_L769/src/finra/) before dispatch: 357 months 1997-01..2026-09"
domain: "FUNDING_LIQUIDITY"
cluster: "POSITIONING_VALUATION"
action: []
info: ["HENRY", "LIQUID", "VULCAN", "OTTO", "CARL", "RED"]
precedence: "PRIORITY"
signal_type: "correction"
corrects: ["SIG-W-20261022-016"]
corrects_direction: "FLIP on the framing check only: 'second-highest on record' IS supported; the level ($1,480,054M, +$26.2B m/m) is unchanged"
kill_strings: ["'Second-highest' NOT SUPPORTED", "September is the highest value in FINRA's visible 12-month table"]
confidence: 0.95
confidence_language: "FINRA's own downloadable file, ranked over all 357 months"
resources: 1
safety_net: "clear"
word_count: 170
entities: ["FINRA", "margin-debt"]
event_window: "closed"
dispatch_note: "Correction-class; R1 row COR-20261022-40 and the 016 status marker in the same commit. HENRY caught it. Same recipients as 016."
---
# CORRECTION to 016: September 2026 margin debt is the SECOND-highest in FINRA's record, not the highest. June 2026 ($1,502,072M) is the record. HENRY's row and 029's "second-highest" were right; WALTER's 016 check was wrong

**FINRA `margin-statistics.xlsx`, debit balances in customers' securities margin accounts, ranked over all 357 months (Jan 1997 to Sep 2026):**

| Rank | Month | $M |
|---|---|---|
| 1 | Jun 2026 | 1,502,072 |
| 2 | **Sep 2026** | **1,480,054** |
| 3 | Aug 2026 | 1,453,832 |
| 4 | Jul 2026 | 1,417,225 |

**What changes:** 016 said "'Second-highest' NOT SUPPORTED: September is the highest value in FINRA's visible 12-month table." That is wrong; June 2026 sits inside the same window. **What holds:** the level and the +$26.2B month-on-month rise. **Direction:** the relayed framing in 029 stands as written; nothing built on "highest ever" should survive.

**Do not relay as:** "September margin debt is a record high."

**INFO:** 016's recipients (HENRY, LIQUID, VULCAN, OTTO; CARL and RED by BOARD). Receipt per corrections boot check. No trade is implied.
