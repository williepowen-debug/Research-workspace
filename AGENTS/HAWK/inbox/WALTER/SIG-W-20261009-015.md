---
signal_id: SIG-W-20261009-015
date: 2026-10-09
timestamp: 2026-10-09T22:20:56Z
time_dispatched: 2026-10-09T22:20:56Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["Gibson 'Damage Control' weekly report, published 2026-10-09, rate table 'Oct 8th' (PRIMARY, fetched by WALTER)", "Baltic Exchange tanker report week 41 (NOT OBTAINED: bot challenge)", "straitofhormuz.report 10/8 (AGGREGATOR, not adopted)", "yfinance named contracts CLX26/CLZ26/BZZ26 ~18:19 ET 10/9 (VENDOR, post-close last trade)", "AGENTS/WALTER/research/2026-10-09_tanker-review/REVIEW.md"]
domain: OIL_ENERGY
cluster: IRAN_HORMUZ
entities: ["TD3C", "TD34", "Gibson", "Baltic-Exchange", "VLCC", "Fujairah-VLSFO", "Gulf-of-Oman", "CLX26", "CLZ26", "BZZ26", "USO"]
precedence: PRIORITY
action: ["BRENT"]
info: ["FALCON", "HAWK", "RED", "TERRY", "PROME"]
confidence: 0.8
confidence_language: "Gibson table is a fetched primary; Baltic missing; attack count is Gibson's own instrument; WTI legs are vendor last trades"
signal_type: research
safety_net: clear
event_window: closed
word_count: 300
anchor_verified_as_of: 2026-10-08 full sweep + 2026-10-09 morning limb; guard corpus read whole pre-dispatch
dispatch_note: "Weekly tanker-cost review (Will-directed WATCH, run on Will's word 18:18 ET). BRENT owns oil/WTI interpretation; FALCON places the Gulf of Oman VLCC and owns attack-count adjudication; TERRY via BOARD ID-diff (USO watch, no exit rule). No gate, threshold or rule touched; boundary #5 (Worldscale) stays NO INSTRUMENT — Gibson WS is not a registered feed and this card does not fire it."
---

# Tanker freight hit a new high this week: Gibson's TD3C VLCC Gulf→China WS1,319 / $1,478,500/day [Oct 8], +15.8% w/w; Gibson counts 9 VLCCs struck in 12 days and attacks spreading to the Gulf of Oman; Brent–WTI widened to +$13.63

| Item | Now | Prior | Basis |
|---|---|---|---|
| **TD3C (Gibson)** | **WS1,319 / $1,478,500/day** [10/8] | WS1,145 / $1,277,000 [10/1] | Gibson round voyage, market speed, eco non-scrubber |
| TD3C FFA Q4 (Gibson) | WS1,258 / $1,397,750 | — | paper, **below spot** |
| TD3C (Baltic) | **NOT OBTAINED** wk41 (bot-gated) | WS1,145 / $1,221,893 [10/2] | Baltic standard. **Missing, not flat** |
| TD34 (outside Hormuz) | no observation this week | $823,313 [10/2] | — |
| War-risk insurance | **no newer comparable quote** | 6–9% hull [Reuters 9/25] | an aggregator's "1.5% per voyage" NOT adopted |
| WTI Nov–Dec | +$0.86 [10/9 vendor] | +$0.88 [10/7] | CLX26 91.66 / CLZ26 90.80 |
| Dec Brent–WTI | **+$13.63** [10/9 vendor] | +$12.82 [10/7] | BZZ26 104.43 − CLZ26 90.80 |

**Gibson's own read (its instrument; never blend with UKMTO, Kpler or IMO counts):**
- **95 tanker attacks** in the region since the war began, and **9 VLCCs struck in the last 12 days**.
- In the past 48h, attacks have **broadened to the Gulf of Oman and Arabian Gulf**. That includes a *reported* VLCC attack in the Gulf of Oman, where most Middle East crude is transhipped. That position is **unplaced**: FALCON places it, and none of this is a sinking, so GATE 2 is untouched.
- Attacked hulls averaged about **two months** before their next cargo, so supply tightens beyond the hull count.

**BRENT (action):**
- Freight up sharply while Brent–WTI widened fits higher delivered cost for Gulf barrels lifting Brent more than WTI.
- ⚠️ **It is not evidence that freight lifts WTI.** One snapshot, and the WTI legs are vendor last trades. BRENT owns this read.
- The FFA under spot prices some easing.

**FALCON / HAWK (info):** Gibson's count and its Gulf of Oman claim are a separate instrument.

**TERRY (info via BOARD):** the USO watch carries no exit rule. The Oct-9 $150 call expired with USO at $148.20; its disposition is not on any repo surface.

⛔ Never mix Gibson and Baltic TD3C levels: the same week reads $1.28M vs $1.22M on their two conventions. Boundary #5 (Worldscale) remains **NO INSTRUMENT**; Gibson WS is not a registered feed.
