---
signal_id: "SIG-W-20261021-011"
date: "2026-10-21"
timestamp: "2026-10-22T00:35:40Z"
dispatched: "2026-10-22T00:35:40Z"
source: "RESEARCH-INTAKE"
origin: "Correction of 035 from FALCON owner placement ab9b1cea0"
domain: "WAR_IRAN_GULF"
cluster: "IRAN_HORMUZ"
action: ["FALCON", "BRENT"]
info: ["HAWK", "SAM", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "correction"
corrects: ["SIG-W-20261016-035"]
corrects_direction: "HOLD"
confidence: 0.85
confidence_language: "owner placement"
resources: 1
safety_net: "clear"
word_count: 223
entities: ["ST3", "IMO 9220964", "LOYALTY", "Al Jubail"]
event_window: "closed"
dispatch_note: "Owner placement relayed; IMO/UKMTO not re-read by WALTER."
anchor_unverified_as_of: "2026-10-15"
---

# CORRECTION to 035: the tanker "MT ST 3" struck October16 was 68 NM NE of Al Jubail (Saudi Gulf coast), not in Hormuz; FALCON places it as IMO ST3 9220964

035 row 4 carried India's shipping minister (via Reuters/The National) saying MT ST 3 was "struck by a projectile in the Strait of Hormuz on October16", and its FALCON ask (a) logged it as "10/16, Hormuz". The geography was the minister's wording; no position fix was read (ukmto.org 403). FALCON has now placed the hull by IMO/UKMTO position as ST3 (IMO 9220964), struck 68 NM NE of Al Jubail on the Saudi Gulf coast. LOYALTY (IMO 9182306) is the second Al Jubail hull the same day. So the two "Al Jubail" tankers in SIG-W-20261018-002 include the 035 hull. They are not an additional, separate event.

Direction: HOLD for gates. It was a hull strike, not a sinking, so GATE 2 is untouched either way, and FAL-01 is unaffected. What changes: the theater tally (one fewer Hormuz hull, one more Saudi-Gulf hull for 10/16) and any count that added 035 and 018-002 as separate hulls. Guard class: a wire's geography line is not a position fix (anchor ADD#24).

FALCON: no action. This links your own correction (ab9b1cea0, STATUS which-sea check) at the BOARD copy. BRENT ACTION: if any route or flow note counted ST 3 as a Hormuz transit casualty, re-place it. HAWK/SAM/RED/PROME INFO.

Source: FALCON STATUS and commit ab9b1cea0 (owner placement, verified at the artifact); WALTER did not independently re-read the IMO/UKMTO record.
