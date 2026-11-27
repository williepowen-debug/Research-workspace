---
signal_id: "SIG-W-20261126-003"
date: "2026-11-27"
timestamp: "2026-11-27T03:34:22Z"
dispatched: "2026-11-27T03:34:22Z"
source: "arabnews.com 'Houthi attack on Saudi Arabia's Jazan refinery kills Nepali worker' (published 2026-11-26T15:19Z, read 2026-11-26 ET); Research-Intake data/2026-11-26/news.json titles (Reuters 20:56Z, Al Jazeera 20:38Z, NBC 20:44Z); search summaries (Cyprus Mail, Archyde)"
origin: ["Research-Intake lane titles (Reuters 20:56Z)", "Arab News page read (published 15:19Z)", "search summaries"]
action: ["FALCON", "BRENT", "HAWK"]
info: ["SAM", "HANS", "OSPREY", "NEXUS", "HENRY", "RED", "PROME"]
precedence: "IMMEDIATE"
signal_type: "event"
confidence: 0.9
confidence_language: "confirms: Saudi Energy Ministry statement as quoted by Arab News; Reuters title only; attribution is the coalition's"
resources: 1
safety_net: "clear"
cluster: "IRAN_HORMUZ"
domain: "GEOPOL_ENERGY"
entities: ["Jazan refinery", "Saudi Aramco", "Saudi Energy Ministry", "Houthis", "Hodeidah", "Red Sea"]
word_count: 445
dispatch_note: "IMMEDIATE: a confirmed hit with a fatality and partial shutdown on a Saudi Red Sea Aramco asset (LAST_COMPLETION resume list item 1 class). Same recipients as 042. Iran pre-dispatch guard: IRAN_WAR_GUARDS.md read whole this session; anchor full sweep 11/23, this is a state change for the ~11/30 sweep. RED, PROME by BOARD diff."
event_window: "open"
---
# Saudi Aramco's Jazan REFINERY (400,000 b/d, Red Sea coast) hit Thu Nov 26: the Energy Ministry says a 'hostile aerial projectile' sparked a fire and some operations were suspended; one Nepali worker killed, several injured; the coalition blames the Houthis; damage assessment under way; not the Jazan PORT hit of Nov 25

# Jazan refinery, Thu Nov 26 (late, carded at the night boot)

| State | Read | Basis |
|---|---|---|
| ATTACKED | Saudi Energy Ministry: the facility was hit by a 'hostile aerial projectile', which sparked a fire | Arab News 11/26 (page read, published 15:19Z) quoting the ministry statement; Reuters title in the lane 20:56Z 'Attack on Saudi Aramco's Jazan refinery kills worker, halts some operations' (page not read) |
| SHUT, partly | 'led to the suspension of some operations'; which units and for how long NOT STATED; no restart timeline found | same; search summaries say the fire was brought under control (outlet not read) |
| DAMAGED | not quantified: 'emergency and technical teams ... complete a damage assessment and safety checks' | Arab News |
| Casualties | one Nepali worker killed, several injured of different nationalities | ministry via Arab News |
| Attribution | ministry did not name the attacker; the coalition says the Houthis did it and that it destroyed a ballistic missile launch platform at Hodeidah used in the attack; no Houthi statement found | Arab News; Cyprus Mail via search summary |
| Capacity | up to 400,000 b/d crude processing (CAPACITY, not a loss figure) | Arab News |

- **Guards applied (IRAN_WAR_GUARDS):** this is the REFINERY, not Jazan PORT (card 20261125-042, minor damage, no casualties): do not merge them. 400,000 b/d is capacity: a loss figure has not been stated by anyone. ATTACKED / SHUT (partly) / DAMAGED (not quantified) are carried separately. The 2019 Abqaiq number does not attach. The guard file's older line 'Jizan shut since 7/27, restart never confirmed' (ADD#19, August) conflicts with 'suspension of some operations' today, which implies units were running: FALCON settles the prior state.
- **Not adjudicated here:** whether a refinery hit moves any FALCON rung (FAL-01 is RESOLVED; the live D 85 to 92 rung covers Gulf-ally PRODUCTION, and refining is not production in this file's record); FALCON grades. Brent effect is BRENT's (CNBC 04:46Z had BZ 94.71 before this event; no later read here; US markets shut Thursday).
- **Late:** public from about 15:19Z (10:19 ET); carded at the night boot: no WALTER session ran on Thanksgiving until 22:22 ET (clock stamp). Same day: Houthi claim on Ras Tanura (card 20261125-008), Jazan port (042), two Italians killed in Kuwait (card 20261126-004).
- **So what:** the Saudi Red Sea side, the bypass for Hormuz, now has a confirmed hit with a fatality on an Aramco processing asset, one day after the port hit. The next things that matter: which units stopped and for how long (Aramco or ministry), and whether Yanbu or Rabigh follows.
