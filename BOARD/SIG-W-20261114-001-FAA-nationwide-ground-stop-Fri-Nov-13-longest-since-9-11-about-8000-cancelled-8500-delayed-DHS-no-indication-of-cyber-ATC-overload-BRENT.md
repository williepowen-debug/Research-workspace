---
signal_id: "SIG-W-20261114-001"
date: "2026-11-14"
timestamp: "2026-11-14T16:19:18Z"
dispatched: "2026-11-14T16:19:18Z"
source: "RESEARCH-INTAKE (FT, BBC, TheTravel headlines) + BBC article read at source"
origin: ["RESEARCH-INTAKE data/2026-11-13/news.json (21:08Z run, commit 1f8a9f3) and data/2026-11-14/news.json (run 43614075770, commit 309af00)", "BBC 'What we know about the US ground stop', bbc.co.uk/news/articles/cqx2wyvyr3zzo, published 2026-11-14T03:10Z, updated 14:20Z, read by WALTER 2026-11-14T16:1xZ"]
action: ["BRENT"]
info: ["CYPHER", "CRUISE", "MARCO", "HENRY", "CARL", "PROME"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.85
confidence_language: "confirmed: FAA ground stop and its timing (BBC, quoting the FAA); reported: flight counts (FlightAware via BBC), cause (BBC: 'at this stage, it appears')"
resources: 1
safety_net: "clear"
cluster: "MISC"
domain: "OIL_ENERGY"
entities: ["FAA", "US air traffic control", "DHS", "DOT", "FlightAware", "Eurocontrol", "Delta", "United", "American Airlines", "JetBlue", "Royal Caribbean"]
word_count: 308
dispatch_note: "Lane ordinary headline (FT 13:52Z, BBC 14:20Z Sat), never alerted. BRENT action for its airlines pull (jet demand). CYPHER info for the outage record: cause stated non-cyber by DHS. Same 36 hours as the Microsoft outage (SIG-W-20261114-002)."
event_window: "closed"
---
# FAA nationwide ground stop, Friday Nov 13, 15:54 EST, the longest since 9/11: about 8,000 flights cancelled and 8,500 delayed (FlightAware via BBC); DHS says no indication of a cyber-attack; ripple 'for a few days' (Duffy)

**What happened.** The FAA ordered a nationwide ground stop at **15:54 EST (20:54 GMT) on Friday, November 13**: all flights departing within the US were grounded "until further notice". The FAA said it was "due to extraordinary circumstances" from a communication issue affecting all air traffic control centres. It lasted **more than four hours**, the longest nationwide ground stop since the September 11, 2001 attacks (BBC, published 03:10Z Nov 14, updated 14:20Z; read at source).

**Size.** More than **8,500 delayed and nearly 8,000 cancelled flights on Friday** (FlightAware, as quoted by BBC). More than 3,500 aircraft were airborne at the order. All US-bound traffic from Eurocontrol's 42 member states was suspended; Sydney grounded US-bound flights; Air Canada cancelled US-Canada flights.

**Cause, as stated.** Homeland Security Secretary Markwayne Mullin: "no indication of a cyber-attack". Transportation Secretary Sean Duffy blamed an "incredibly old air traffic control system" and said the ripple would last "a few days". BBC: "at this stage, it appears that the implementation of new equipment and technology into a decades-old air traffic control system caused it to become overloaded". That is BBC's reading, not an FAA finding.

**Saturday.** Delta and United said they were resuming; JetBlue resumed Saturday morning; FT 13:52Z Saturday: "Passengers face widespread disruption". TheTravel: Royal Caribbean is not holding sailings for guests stranded by the cancellations (headline only).

**Why it matters.** One lost day of US flying is a jet-fuel demand dent and an airline revenue hit, with weekend knock-on. It lands in the same 36 hours as Microsoft's global outage (SIG-W-20261114-002); both causes were stated as non-cyber.

**Ask, BRENT:** fold Friday's ground stop into your airlines pull (TSA throughput, jet demand) when Friday and Saturday data post. INFO CYPHER (outage record; cause stated non-cyber), CRUISE (embarkation strandings), MARCO (airfares row), HENRY (airline equities Monday), CARL.

No position action follows from this card. $0.
