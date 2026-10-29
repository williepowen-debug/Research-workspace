---
signal_id: "SIG-W-20261029-042"
date: "2026-10-29"
timestamp: "2026-10-29T17:49:56Z"
dispatched: "2026-10-29T17:49:56Z"
source: "x-bookmark (Will) @nypost 2115765732671701035; Reuters via NY Post 10/29 07:18 ET"
origin: ["x-bookmark 2115765732671701035 @nypost 2026-10-29T11:20Z", "https://nypost.com/2026/10/29/us-news/pentagon-treating-military-base-freezer-malfunctions-as-suspected-cyberattack-officials-say/ (Reuters byline; WALTER curl 10/29)"]
domain: "CYBER"
cluster: "CYBER"
action: ["CYPHER"]
info: ["HANS", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.7
confidence_language: "Reuters, four anonymous officials; Pentagon and Army CID on-record statements confirm an investigation, not a cause; attack NOT confirmed"
entities: ["Pentagon", "Cyber-Command", "Army-CID", "Defense-Commissary-Agency", "Fort-Huachuca", "Danfoss", "Copeland"]
resources: 2
safety_net: "clear"
event_window: "closed"
word_count: 209
dispatch_note: "Will bookmark. BOARD grep: French refrigeration attack carded SIG-W-20261012-011 (CYPHER CYB-INC-003); the US commissary failures (8/26-27) have no card and no CYPHER row. Every cyber claim routes to CYPHER (v0.48). Ask: CYPHER decides whether to open an incident row and whether it links to CYB-INC-003. Delivery and consumption separate."
---
# Reuters 10/29: Pentagon treats the late-August military commissary freezer failures as a suspected hack; a Cyber Command unit and Army CID (working with French police on the October supermarket attack) are involved. No cause or attacker confirmed

- **Source:** Reuters, carried by NY Post 10/29 07:18 ET; **four anonymous officials** say the failures are treated as a suspected hack.
- **On the record:** the Pentagon says a Cyber Command unit is "working in close coordination with interagency and law enforcement partners"; the Army Criminal Investigation Division says its Cyber Field Office is involved and is working with French law enforcement on "the refrigeration outages in Europe".
- **Scope:** at least **six** commissaries (on-base grocery stores) hit in late August per Reuters' review of base posts; at Fort Huachuca (8/26) the units "went into defrost" overnight, temperatures raised, not just switched off. Earlier secondary counts of ~14 sites are not confirmed.
- **Link (not established):** the French supermarket refrigeration attack 10/11-12 (~700 stores, Danfoss and Copeland remote modules, `SIG-W-20261012-011`, CYPHER CYB-INC-003). Reuters could not say how far the probe has got or whether anyone is blamed.

Why it matters: if confirmed, a second national-scale attack on refrigeration controllers, this time US military; vendor exposure (Danfoss, Copeland) is shared with US grocery chains. Today it is a suspicion, not a finding.

ACTION CYPHER: open or decline an incident row; say whether it links to CYB-INC-003. Info: HANS (French leg), RED, PROME (no fleet owner for food cold chain).
