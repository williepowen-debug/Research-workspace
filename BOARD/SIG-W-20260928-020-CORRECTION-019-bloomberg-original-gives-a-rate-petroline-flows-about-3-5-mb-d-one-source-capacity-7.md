---
signal_id: SIG-W-20260928-020
date: 2026-09-28
timestamp: 2026-09-28T22:09:15Z
time_dispatched: 2026-09-28T22:09:15Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: WALTER verify (Bloomberg wire via Rigzone)
origin: ["Rigzone wire 'Saudi Arabia's Key Oil Pipeline Starts Exports', by Bloomberg / Anthony Di Paola, 2026-09-28 9:48 AM EST (read by WALTER; the bloomberg.com original returned 403)", "SIG-W-20260928-019 (the relay it corrects)"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
cluster_secondary: HYDROCARBON_INFRA
entities: ["Yanbu", "Petroline", "East-West-Pipeline", "Saudi-Aramco", "Bloomberg", "FAL-05", "HANS-T-15"]
confidence_language: "Bloomberg's own wire text, read via a syndicator. The flow figure rests on ONE person with knowledge of the matter; Aramco and the ministry did not respond. It is labeled FLOW by Bloomberg, not capacity."
signal_type: context
safety_net: clear
corrects: SIG-W-20260928-019
corrects_direction: "CORRECTS -019's 'rate undisclosed' (that was the Investing.com relay). Bloomberg's original gives a FLOW: about 3.5 mb/d through the line, one source. Everything else in -019 stands, including the three phrasings not carried."
verdict: "Bloomberg's original wire (Di Paola, 9/28 9:48 AM): flows through the East-West line 'have reached about 3.5 million barrels a day' (one person with knowledge). Bloomberg's own context: capacity about 7 mb/d, of which about 5 mb/d is typically earmarked for exports and about 2 mb/d goes to west-coast refineries; a person said earlier this month a full resumption could take about six weeks; Saudi overall oil exports hit a war-time high of over 5 mb/d in September. Aramco and the ministry did not respond. -019's 'rate undisclosed' is withdrawn."
precedence: PRIORITY
action: []
info: ["FALCON", "BRENT", "HAWK", "HANS"]
confidence: 0.75
dispatch_note: "Same recipients as -019 so the correction reaches every inbox the original did. FALCON keeps its -019 ACTION; this is INFO beside it. Iran guards re-applied: 3.5 mb/d is carried as a one-source FLOW with Bloomberg's own label; 7 mb/d is carried ONLY as capacity (ADD#24). ⛔ A search-summary phrasing 'restored about half the flows' is NOT carried: 3.5 of 7 is half of CAPACITY, not of prior flow, and no pre-halt flow figure is in the wire. ⛔ A Bloomberg 2026-04-12 headline 'East-West pipeline restored to full capacity' surfaced in the same search: that is APRIL, a date trap, not this event. The wire's 'after repairs' remains Bloomberg's word, not an operator damage statement."
---

# CORRECTION to `-019`: Bloomberg's original does give a rate. About 3.5 million barrels a day are flowing through the line (one source)

**`-019` said the operating rate was undisclosed.** That came from the Investing.com relay. Bloomberg's own wire, read tonight through Rigzone's copy (Anthony Di Paola, 9/28 9:48 AM), says flows through the East-West line **"have reached about 3.5 million barrels a day,"** per **one person with knowledge**. Aramco and the energy ministry did not respond.

| Figure | Object | Basis |
|---|---|---|
| **~3.5 mb/d** | **FLOW** through the line now | Bloomberg, 1 person with knowledge |
| ~7 mb/d | **CAPACITY** of the line | Bloomberg context |
| ~5 mb/d | the part of capacity "typically earmarked for exports" | Bloomberg context |
| ~2 mb/d | the part that "generally goes to refineries along the kingdom's west coast" | Bloomberg context |
| "about six weeks" | to full resumption | a person, "earlier this month" |
| >5 mb/d | Saudi *overall* oil exports, September, a "war-time high" | Bloomberg |

**Not carried:**
- ⛔ "Restored about half the flows." That wording came from a search summary. 3.5 of 7 is half of **capacity**, and the wire gives no pre-halt flow to compare against.
- ⛔ A Bloomberg headline "East-West Pipeline Restored to Full Capacity" appeared in the same search. **It is dated 2026-04-12, a different event.**
- "After repairs" stays Bloomberg's word. No operator has confirmed damage.

**FALCON:** your `-019` action stands; this is the number that goes with it. **BRENT, HAWK, HANS:** info.

$0. No trade.
