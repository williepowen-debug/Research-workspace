---
signal_id: SIG-W-20260929-013
date: 2026-09-29
timestamp: 2026-09-29T19:16:08Z
time_dispatched: 2026-09-29T19:16:08Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: Will-Telegram image (X post @aviancapital) + Will's routing word ("CORAL", msg 4777, 2026-09-29 15:15 ET)
origin: ["Will-Telegram BM-20260929-04 item 6 (msg 4750): X post by @aviancapital ('Avian Capital'), ~5h old at capture: 'Looking at apartments in Ft. Lauderdale ... very clear that CRE (multifamily) is going to blow up big time ... People I know are still having rents raised on them for renewal ... and aggressively ... Vacancy everywhere ... this new development that opened this year (about 7 months ago). Tons of available units. Has to be around 75% vacant ... ($2,100 for a 480 sqft studio) ... the maturity wall is coming for them too'", "Will-Telegram msg 4777 (15:15 ET): 'CORAL' (answer to WALTER's question: route as a lead, yes/no, and to whom)"]
domain: BANK_CRE
cluster: BANK_COLLATERAL
entities: ["Fort Lauderdale", "Broward County", "multifamily", "CORAL", "Avian Capital"]
confidence_language: "ANECDOTE, n=1: one account's walk-through of Fort Lauderdale apartment buildings. The '~75% vacant' figure is the poster's visual estimate of ONE new building; 'vacancy everywhere' is impression, not a count. No data source. Routed as a LEAD on Will's word, not as evidence."
signal_type: manual-flag
safety_net: clear
verdict: "LEAD, not a finding (Will-directed). One account reports, from walking Fort Lauderdale apartment buildings, visible vacancy across the city while landlords keep pushing aggressive renewal increases; one building opened ~7 months ago looks '~75% vacant' to the poster, asking ~$2,100 for a 480 sq ft studio (~$4.38/sq ft/month); it adds 'the maturity wall is coming'. None of it is measured. The check it points to: Fort Lauderdale / Broward multifamily vacancy, concessions and new-supply lease-up against a data source. No fleet desk holds Fort Lauderdale rent data today (checked 9/29)."
precedence: ROUTINE
action: ["CORAL"]
info: []
confidence: 0.3
dispatch_note: "WALTER logged this NO-ACTION at intake (BM-20260929-04 item 6: below the filter bar as evidence) and offered Will the choice; Will answered 'CORAL' (msg 4777). This dispatch supersedes that disposition on the operator's word; the manifest stays closed and this signal records the change. manual-flag -> PRIORITY by default, set to ROUTINE because nothing decays (Will gave no urgency). HOMER NOT added: Will named CORAL only. CORAL is DARK (not in ListAgents) -> DOORBELL_LOG row. Florida is Will's top-priority geography (root CLAUDE.md)."
---

# Will-directed lead: a Fort Lauderdale apartments anecdote (visible vacancy, high asking rents, one new building ~75% vacant). Check it against data

**Will asked for this to go to CORAL as a lead.** It is **one person's walk-through**, not data.

| Claim (the poster's) | What it is |
|---|---|
| "Vacancy everywhere" across Fort Lauderdale apartment buildings | impression, not a count |
| Landlords still raising renewal rents "aggressively" | people the poster knows |
| New building opened ~7 months ago is "~75% vacant" | one building, eyeballed |
| $2,100 for a 480 sq ft studio (~$4.38/sq ft/month) | one asking rent |
| "The maturity wall is coming for them too" | the poster's view |

**The check it points to:** Fort Lauderdale / Broward multifamily **vacancy, concessions and new-supply lease-up** against a real source. No fleet desk holds Fort Lauderdale rent data today; checked 9/29. Related context already on BOARD: `-0928-014` (Redfin August: Miami sellers outnumber buyers 138%, Orlando 121%; for-sale homes, not rentals).

**ACTION (CORAL):** decide whether it's worth a data check, and with what source. Your call. $0.
