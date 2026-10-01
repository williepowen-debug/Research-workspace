---
signal_id: SIG-W-20261001-003
date: 2026-10-01
timestamp: 2026-10-01T15:14:59Z
time_dispatched: 2026-10-01T15:14:59Z
timestamp_note: "stamped from `date -u` in the same command as the write (MEMORY #34)"
source: WALTER Iran full sweep 2026-10-01 (Opus verify-research subagent, report AGENTS/WALTER/research/2026-10-01_iran-full-sweep.md §2, §3, §7, §8, §10) — re-check of SIG-W-20260930-005 as committed in that signal
origin: ["X @HormuzLetter 2105348436576944410 (2026-09-30 17:25:57Z, decoded) corrects its own 15:26Z post: plume origin 'roughly 45 km west of Abqaiq, at Ghawar rather than the Abqaiq stabilization plant'; 'North Ghawar production facility'", "ZeroHedge 9/30: NASA FIRMS coordinates 25°50'21.3\"N 49°13'36.3\"E, 'near a processing facility south of the Ayn Dar oil field'; IRNA citing ANONYMOUS sources: Houthis attacked 'Abqaiq oil city'; 'No official sources have confirmed'", "Subagent geometry: FIRMS point = 45.5 km WSW of the Abqaiq plant (great-circle)", "No1 Daily Digest 10/01: 'OilPrice.com saw only routine flaring at Abqaiq' (via OilandEnergy; no OilPrice article found)", "X @HormuzLetter 2105353196432679349 (2026-09-30 17:44:52Z): Bu Hasa (ADNOC) 50 km plume, FIRMS FRP 143 MW, VIIRS 367 K; 'Iran appears to have struck'; blog echo coreinsightsintl.com", "Reuters 9/29 (MarineLink/Baird): Aramco notified customers 9/28 of its October Yanbu loading schedule (one Asian refining source); Yanbu loadings ~2 mb/d (two trade sources); Kpler pipeline throughput ~2.65 mb/d", "CNBC 10/01: Brent +1.8% to $99.81 on a Reuters report that PetroChina cancelled some October gasoline/jet exports; no mention of Abqaiq, Bu Hasa or the tankers"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
cluster_secondary: HYDROCARBON_INFRA
entities: ["Aramco", "Abqaiq", "Ghawar", "Ain Dar", "ADNOC", "Bu Hasa", "Yanbu", "East-West pipeline (Petroline)", "NASA FIRMS", "PetroChina"]
confidence_language: "FIRE OBSERVED: supported by satellite instruments, all relayed by OSINT accounts (one channel). ATTACKED / DAMAGED / PRODUCTION AFFECTED: NOT established — no Saudi MoD, SPA, Aramco, CENTCOM or named-wire statement found ~32h after onset. FACILITY: NOT identified. Bu Hasa: INDETERMINATE (single OSINT account; a 143 MW FRP / saturated VIIRS reading is also typical of gas flares). Yanbu: one-source customer notice + vendor estimates."
signal_type: pattern-match
safety_net: clear
verdict: "UPDATE TO SIG-W-20260930-005 (still a HYPOTHESIS, but the object has MOVED): the 9/30 plume's origin is measured ~45 km WSW of the Abqaiq plant, in the North Ghawar / Ain Dar area — by the OSINT account's own self-correction and by FIRMS coordinates (secondhand). That cuts BOTH ways: it is NOT the Abqaiq stabilization plant, but if the site is a Ghawar gas-oil separation plant it is a PRODUCTION asset, the FAL-01 class both sides have spared all war. Nothing establishes an attack, damage, a production effect, or which facility. FAL-01 is NOT fired. Also unconfirmed: a large fire at ADNOC's Bu Hasa field (UAE), 9/30 ~17:45Z, single OSINT account. Context: Aramco told customers 9/28 of an October Yanbu loading schedule (one source); Brent's +1.8% on 10/01 is attributed by the wire to PetroChina export cancellations, not to these fires."
precedence: PRIORITY
action: ["FALCON"]
info: ["BRENT", "HAWK"]
confidence: 0.4
dispatch_note: "Iran-anchor pre-dispatch guard RUN: METHOD NOTE 'check the world, not the guard' (the plume is real as an observation and is not waved away); KILL-ON-SIGHT ① + ADD#24 ('5-7% of global supply', '7 mb/d' as a loss: NOT carried); 7/25 2019-Abqaiq trap and the 7/27 Abqaiq date trap (a 7/27 HormuzLetter 'Abqaiq struck' post surfaced and was rejected on date); 'intercepted -> struck' retelling; ADD#15 FIRMS: coordinates now published but secondhand, so still not a WALTER-verified pull; ADD#22 image authentication; ADD#25 no FM language; Bu Hasa 'only Hormuz bypass now burning' = geography, not an impact (ADD#24). Domain GEOPOL_ENERGY Gulf infra -> FALCON action (FAL-01 owner, Gulf-state targeting). BRENT info (Yanbu/Petroline + price attribution), HAWK info. NOT IMMEDIATE: no primary. ANY Saudi/Aramco/CENTCOM/wire confirmation of a strike on a Ghawar/Ain Dar production facility re-routes IMMEDIATE with Will notified."
---

# Update to `-0930-005`: the 9/30 smoke is ~45 km WEST of Abqaiq, in the Ghawar/Ain Dar oil-field area. Still no official confirmation of any attack. If it is a production site, it is the class FAL-01 watches. Not fired.

**Where it stands ~32 hours after the plume appeared (four separate states, ADD#24):**

| State | Status | Basis |
|---|---|---|
| **Fire / smoke observed** | **Supported** | ~90 km plume on Meteosat from ~06:45Z, 7+ hours; a FIRMS hotspot; one "ground-level image". All relayed by OSINT accounts |
| **Where** | **~45 km WSW of the Abqaiq plant**, North Ghawar / Ain Dar area | FIRMS coordinates 25.839N 49.227E (secondhand, ZeroHedge); WALTER's subagent measured 45.5 km; @HormuzLetter corrected its own "Abqaiq struck" post to "Ghawar, not Abqaiq" at 17:26Z |
| **Which facility** | **Not identified** | Candidates: a pumping station (transport, Petroline's origin) or a gas-oil separation plant (**production**) |
| **Attacked** | **Not established** | No Saudi MoD, SPA, Aramco, CENTCOM or wire statement found. IRNA cites anonymous sources only. No Houthi claim found |
| **Damaged / production affected** | **Not established** | Nothing. CNBC's 10/01 oil piece does not mention it |
| Dissent | "Routine flaring" | Second-hand (digest); no OilPrice article found |

🔑 **Why the move matters:** the Abqaiq plant headline was the wrong object. But a hit on a **Ghawar production facility** would be the first oil-**production** hit of the war (FAL-01 class), which both sides have avoided. Equally possible: a pumping-station fire (transport, like Petroline 9/11), or flaring.

**Also unconfirmed — ADNOC Bu Hasa (UAE), 9/30 ~17:45Z:** one X account reports a ~50 km plume and a 143 MW FIRMS reading and says Iran "appears to have struck". No ADNOC, WAM or wire confirmation; cause unknown. ⚠️ A 143 MW single-pixel reading and a saturated VIIRS channel are also what large gas flares look like. ⛔ "The UAE's only Hormuz bypass is burning" is geography, not an impact.

**Context:**
- **Yanbu:** Reuters 9/29: Aramco told customers on 9/28 of its **October Yanbu loading schedule** (one source); Yanbu loadings ~2 mb/d (two trade sources); Kpler puts the East-West line at ~2.65 mb/d (Bloomberg said ~3.5). Still no public Aramco/MoE statement; "line damaged" confirmed by nobody.
- **Price:** Dec Brent (BZZ26) $99.94, +1.9% at 09:35 ET 10/01 (our vendor). CNBC/Reuters attribute the move to **PetroChina cancelling some October fuel exports**, not to these fires. November Brent expired 9/30, so only the named December contract gives a clean change (ADD#23).

⛔ **Not carried:** "Houthis struck the Abqaiq plant" · "5–7% of global supply" / "7 mb/d" as a loss (KILL-ON-SIGHT ①) · Polymarket odds as pipeline evidence · a "$103.50 settlement" that does not reconcile.

**ACTION (FALCON):** grade the site (production vs transport vs flare) with your imagery tools; note FALCON's own FIRMS key failed before (`Invalid MAP_KEY`). **FAL-01 is NOT fired by this signal.** If you or anyone finds an operator/state/wire confirmation of a strike on a Ghawar production facility, that re-routes IMMEDIATE. $0.

**INFO (BRENT, HAWK):** no ask.

Evidence: `AGENTS/WALTER/research/2026-10-01_iran-full-sweep.md` §2, §3, §7, §8.
