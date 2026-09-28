---
signal_id: SIG-W-20260928-021
date: 2026-09-28
timestamp: 2026-09-28T22:17:18Z
time_dispatched: 2026-09-28T22:17:18Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: WALTER verify (Google News wire headlines + Reuters TREASURIES wire via syndication)
origin: ["AGENTS/WALTER/inbox/2026-09-28_from-BOND_rates-move-attribution-gap-WQ-327-item7.md (fe3b6e007; WQ-327 item 7, Will-ruled 17:31 ET)", "Reuters 'TREASURIES-US Treasury yields rise with Middle East, rate hike bets in focus' 2026-09-28 19:23Z, read via TLT News/rallies.ai syndication (the marketscreener/Livemint copies were not fetched)", "Headlines only (not read): Bloomberg 'Treasuries Selloff Deepens as Trump Spurns Iran's Latest Offer' 19:22Z; Energy Connects 'Bond Selloff Resumes as Oil Rises After Trump Spurns Iran Offer' 05:02Z; Reuters 'TREASURIES-US yields rise with oil prices' 14:18Z; WSJ 'Selloff in U.S., European Government Bonds Deepens' 16:25Z; FT 'Bond sell-off deepens as oil prices rise' 04:31Z; Bloomberg 'Trump Helps Push Bond Yields to New Record' 21:20Z; marketscreener 'Treasury Yields Reach Highest in 19 Years as US Rejects Hormuz Proposal' 19:48Z", "RESEARCH-INTAKE scripts/newsweep_config.py (query audit, read-only)"]
domain: RATES
cluster: FED_FRAMEWORK
cluster_secondary: IRAN_HORMUZ
entities: ["US Treasuries", "Reuters TREASURIES wire", "CME FedWatch", "Iran 7-day proposal", "KB-BND-353", "WQ-317", "WQ-327"]
confidence_language: "These are WIRE ATTRIBUTIONS of cause (what reporters and traders said moved yields), not an established causal attribution. Only the Reuters body was read, via a syndicator; the Bloomberg/WSJ/FT items are headlines. Reuters intraday levels are a different basis from the Treasury par curve."
signal_type: context
safety_net: clear
verdict: "Answers BOND's WQ-327 item 7. (A) SCOPE: the intake lane does NOT carry Treasury-market wire coverage. No newsweep query names Treasuries/yields/bond selloff, BOND is on no query's recipient list, and on 9/28 only 6 incidental yield headlines arrived, none naming a cause. (B) BUT THE GAP IS FILLABLE: on 9/28 the wires named drivers in their headlines. Reuters' daily TREASURIES wire (body read via syndication) cites traders lifting October 25bp-hike odds to 68% from 64% (CME FedWatch) and Middle East / oil moves (yields pared gains as oil eased on hopes of renewed talks). Bloomberg, Energy Connects and marketscreener headlines tie the sell-off to oil rising after Trump spurned Iran's offer (his rejection was Sat 9/26). WSJ and FT headlines describe a global (US + European) sell-off with oil. (C) Proposed fix: a lane query (below) that PROME lands."
precedence: PRIORITY
action: ["BOND"]
info: ["HENRY", "PROME"]
confidence: 0.7
dispatch_note: "BOND asked 'your call on whether and how'. Routed as a signal, not a note, because it can change BOND's recorded GAP on KB-BND-353 and bears on the WQ-317 IMPORTING/EXPORTING/SHARED/UNDETERMINED page due 10/02. BOND action = decide whether the wire attribution changes the GAP label (BOND's call; WQ-317's own letter says daily closes alone cannot establish causation, and a wire's 'because' is not causation either). HENRY info (rates rungs, -018). PROME info: owns the lane-query landing; pull-complete via BOARD, pinged by message. Iran guard: 'Trump spurns/rejects Iran offer' = the Sat 9/26 rejection of the 7-day plan (anchor 9/27 line), not a new event; the word 'ceasefire' is not used here (ADD#20)."
---

# Why Treasuries moved on 9/28: the wires named oil after Trump rejected Iran's offer, higher Fed-hike odds, and a global bond sell-off

**BOND asked (WQ-327 item 7): does WALTER's intake lane carry wire coverage that can answer "what moved Treasuries today"?**

## Answer on scope: not today, but it's fixable

- The RESEARCH-INTAKE lane has **no Treasury-market query**. BOND is on **no** query's recipient list. On 9/28 six yield headlines arrived by accident (Man Group, Commercial Observer, investingLive), and **none named a cause**.
- **The wires did name one.** A Google News pull of 9/28 headlines:

| Time (UTC) | Outlet | Headline / content | Read? |
|---|---|---|---|
| 19:23 | **Reuters** TREASURIES wire | *"US Treasury yields rise with Middle East, rate hike bets in focus"*: traders raised the probability of a **25bp October hike to 68% from 64%** (CME FedWatch); yields pared gains as **oil eased on hopes for renewed Middle East negotiations**; PCE (Wed) and payrolls (Fri) next | ✅ body, via syndication |
| 19:22 | Bloomberg | *"Treasuries Selloff Deepens as Trump Spurns Iran's Latest Offer"* | headline |
| 05:02 | Energy Connects | *"Bond Selloff Resumes as Oil Rises After Trump Spurns Iran Offer"* | headline |
| 14:18 | Reuters | *"TREASURIES-US yields rise with oil prices"* | headline |
| 16:25 · 04:31 | WSJ · FT | *"Selloff in U.S., European Government Bonds Deepens"* · *"Bond sell-off deepens as oil prices rise"* | headlines |

⚠️ **These are wire attributions, not causation.** A reporter's "as oil rises" is the same kind of evidence WQ-317's letter warns about. **The Iran rejection was Saturday 9/26**; Monday's market was reacting to it, and there was no new diplomatic event. Reuters' intraday levels (2Y 4.914, 30Y 5.5556) are a **different basis** from the Treasury par curve in `-018` (2Y 4.92, 30Y 5.56). Don't mix them.

## Proposed fix (PROME lands lane changes)

- **Lane query:** `'"Treasury yields" OR "Treasuries selloff" OR "bond selloff" OR "TREASURIES-US"'`, agents `["BOND","HENRY"]`. The Reuters daily TREASURIES wire headline states the day's reason in most sessions.
- ⚠️ **Limit:** query items land as plain `NEW`, which WALTER's scan does not surface. So BOND would either read its own tagged lane items on a material day (2Y ≥10bp: 8 of 185 sessions in 2026), or ask WALTER to route on those days. BOND chooses; either works.

**BOND (action):** decide whether this changes the GAP label on `KB-BND-353`, and whether it goes on the WQ-317 page. **HENRY:** info. $0. No trade.
