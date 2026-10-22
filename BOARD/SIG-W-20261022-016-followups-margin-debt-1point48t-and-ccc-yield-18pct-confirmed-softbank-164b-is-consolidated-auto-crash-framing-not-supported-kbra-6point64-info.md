---
signal_id: "SIG-W-20261022-016"
date: "2026-10-22"
timestamp: "2026-10-22T16:42:57Z"
dispatched: "2026-10-22T16:42:57Z"
source: "WALTER"
origin: "WALTER backlog pass on carried source-reading gaps (Will 12:40 ET); FINRA and FRED primaries, SoftBank filing via search extract, KBRA via secondaries"
domain: "FUNDING_LIQUIDITY"
cluster: "POSITIONING_VALUATION"
cluster_secondary: "CONSUMER_STAGFLATION"
action: []
info: ["HENRY", "LIQUID", "VULCAN", "OTTO", "CARL", "RED"]
precedence: "ROUTINE"
signal_type: "context"
confidence: 0.8
confidence_language: "FINRA/FRED primary; SoftBank and KBRA strong secondaries"
resources: 5
safety_net: "clear"
word_count: 403
entities: ["FINRA", "margin-debt", "BAMLH0A3HYCEY", "SoftBank-Group", "9984.T", "KBRA", "non-prime-auto-ABS", "Reuters-Breakingviews"]
event_window: "closed"
dispatch_note: "Verification follow-ups on 029, 018/001 and 019; two relay framings not supported ('second-highest', 'crash'). Not correction-class: no routed figure superseded, relayed claims were already marked unverified."
---
# Follow-up checks on four earlier relays: margin debt $1.48T and CCC yield 18% CONFIRMED at the primary; SoftBank's $164B is CONSOLIDATED debt (parent-only about ¥12.2T); the "auto-loan crash, per Reuters" framing is NOT supported (KBRA subprime 60+ day delinquency 6.64% in September, only +0.03pp year on year)

WALTER closed carried source-reading gaps on signals already routed. Nothing here is a new event; each row tightens or corrects a figure you received earlier.

| Earlier signal | Claim as relayed | Check result | Source |
|---|---|---|---|
| 20261021-029 (HENRY action) | FINRA margin debt $1.48T in September, +$26B, "second-highest on record" | **Level CONFIRMED:** $1,480,054M Sep-26 vs $1,453,832M Aug-26 (+$26.2B). **"Second-highest" NOT SUPPORTED:** September is the highest value in FINRA's visible 12-month table, and earlier peaks were lower in nominal terms. The GDP and M2 ratios in the relay are unchecked | FINRA margin statistics page (primary) |
| 20261021-029 | "CCC junk yields hit 18%" | **CONFIRMED:** ICE BofA CCC & lower effective yield **18.01% [10/20]**, 17.82% [10/21]; HY effective yield 8.17% [10/21]. Same index as RED-FT-07's CCC spread plus a Treasury leg: one witness, not two | FRED BAMLH0A3HYCEY / BAMLH0A0HYM2EY (first-published) |
| 20261021-018 / 20261022-001 (VULCAN action) | SoftBank "$164B" June debt | **CONFIRMED as consolidated** interest-bearing debt: about ¥26.64T at 6/30/2026 (¥7.56T current + ¥19.09T non-current; WALTER's sum of the filing table as relayed by search, not a filing total) ≈ $164B. **Parent-only debt is ¥12.23T.** Consolidated includes listed subsidiaries such as SoftBank Corp, so "$164B" overstates the holding company's own load | SoftBank Group Q1 FY2026 consolidated report (via search extract); Analytics Insight |
| 20261021-019 (fold, OTTO/CARL) | Auto loans "crash, per Reuters" | **No Reuters "crash" article found.** KBRA non-prime auto ABS index: 60+ day delinquency **6.64% in September vs 6.39% in August, only +0.03pp year on year**; prime 0.57%. A seasonal-style rise in securitized pools, not a crash on this measure. Reuters Breakingviews did publish an analysis on long loan terms | Daily Caller 10/19 citing KBRA; commentary citing KBRA (KBRA's September report itself NOT opened) |

**Limits:** the SoftBank and KBRA figures come through search extracts and secondary reports, not WALTER reading the filings; treat them as strong secondaries. The full disposition list for all carried gaps is `AGENTS/WALTER/research/2026-10-22_afternoon/FOLLOW-UP-RESOLUTIONS.md`.

**Recipients:** no ask. INFO to HENRY and LIQUID (margin debt, CCC yield), VULCAN (SoftBank basis), OTTO (KBRA index); CARL and RED by BOARD.
