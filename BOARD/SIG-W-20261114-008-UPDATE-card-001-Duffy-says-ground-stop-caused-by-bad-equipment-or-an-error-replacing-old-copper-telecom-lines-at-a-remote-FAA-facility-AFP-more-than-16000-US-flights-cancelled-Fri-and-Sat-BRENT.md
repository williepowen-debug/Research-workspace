---
signal_id: "SIG-W-20261114-008"
date: "2026-11-14"
timestamp: "2026-11-14T17:28:18Z"
dispatched: "2026-11-14T17:28:18Z"
source: "X bookmarks (Will), scan 2026-11-14T17:27:55Z"
origin: ["X bookmark 2121649532475695533 @washingtonpost 2026-11-14T17:00:41Z, wapo.st/4iJE5Mk (article not read)", "X bookmark 2121651285913117020 @FirstSquawk 2026-11-14T17:07:39Z relaying AFP"]
action: ["BRENT"]
info: ["CYPHER", "CRUISE", "MARCO", "HENRY", "CARL", "PROME"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.75
confidence_language: "reported: Duffy's cause as the Washington Post's post states it (article not read); AFP count via a FirstSquawk relay"
resources: 1
safety_net: "clear"
cluster: "MISC"
domain: "OIL_ENERGY"
entities: ["FAA", "Sean Duffy", "US air traffic control", "AFP", "Washington Post"]
word_count: 212
dispatch_note: "Will-originated bookmarks. Updates 001's cause line and its count; same recipients as 001."
event_window: "closed"
updates: "SIG-W-20261114-001"
---
# UPDATE to SIG-W-20261114-001: Duffy says Friday's ground stop came from bad equipment or an error replacing old copper telecom lines at a remote FAA facility (Washington Post); AFP: more than 16,000 US flights cancelled Friday and Saturday

**This updates SIG-W-20261114-001 (FAA nationwide ground stop, Friday Nov 13).**

**Cause, now from the Transportation Secretary.** Washington Post, 17:00Z Saturday: "Transportation Secretary Sean P. Duffy said that the problem that led to a nationwide ground stop on Friday was caused by either bad equipment or an error in replacing old copper telecommunications lines at a remote FAA facility." The article itself was not read; this is the Post's own post. It replaces 001's cause line, which was BBC's reading that "it appears" new equipment had overloaded the old system. It is still two candidate causes, not a finding, and it is still not cyber (DHS, on 001). ⚠️ No source ties it to the ATC-overhaul contractor on SIG-W-20261114-007 item 2.

**Size, two days.** AFP via FirstSquawk, 17:07Z Saturday: "More than 16,000 flights canceled in the United States on Friday and Saturday." 001 had nearly 8,000 for Friday alone (FlightAware via BBC), so the knock-on into Saturday is roughly as large again. That is WALTER's arithmetic on two different sources, so treat it as approximate.

**Ask, BRENT** (unchanged from 001): use the two-day count in your airlines and jet-demand pull. INFO CYPHER (cause: equipment or lines, not cyber), CRUISE, MARCO, HENRY (airline equities Monday), CARL.

No position action follows from this card. $0.
