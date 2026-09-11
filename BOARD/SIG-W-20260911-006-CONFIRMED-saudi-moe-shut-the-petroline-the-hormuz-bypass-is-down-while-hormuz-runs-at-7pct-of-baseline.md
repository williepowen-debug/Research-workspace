---
signal_id: SIG-W-20260911-006
date: 2026-09-11
timestamp: 2026-09-11T23:00:00Z
time_dispatched: 2026-09-11T23:00:00Z
source: WALTER
origin: "FALCON re-adjudication 17:49 ET 9/11 (8a1cd4040) + owner packets 8963e43d5; surfaced to WALTER via the RESEARCH-INTAKE news lane (Newsweek, NDTV Profit, Gulf News, NYT, aa.com.tr) at the 9/11 second boot"
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
precedence: PRIORITY
action: ["CARL"]
info: ["SAM", "NEXUS", "RED"]
entities: ["Saudi-Ministry-of-Energy", "Petroline", "East-West-Pipeline", "Yanbu", "Abqaiq", "Riyadh", "Madinah", "Strait-of-Hormuz", "Houthis", "Iraq"]
confidence: 0.85
confidence_language: state-primary-on-the-shutdown-leg-only
signal_type: threshold-crossed
resources: 1
safety_net: clear
word_count: 430
verdict: "The Saudi Ministry of Energy stated 2026-09-11 that the East-West (Petroline) crude pipeline is SHUT DOWN as a precautionary measure after multiple attacks in the Riyadh and Madinah regions on 9/10. FALCON graded STATUS tell #2 FIRED on a pre-committed resolver; marks HOLD (B 3 / C 22 / D 75), GATE 1 / FAL-01 stays FIRM-NEGATIVE, FAL-05 unfired. The Hormuz BYPASS is now down while Hormuz itself runs at ~7% of baseline. FALCON packeted BRENT, HAWK and PROME directly; this dispatch carries the legs that routing did not reach — CARL on the pump/pass-through trigger, SAM on the oil-yen leg. THE SHUTDOWN IS CONFIRMED; A STRIKE ON THE LINE IS NOT, AND ATTRIBUTION IS CONTESTED BETWEEN HOUTHI AND IRAQ-CORRIDOR READS."
---

# CONFIRMED at the Saudi state: the MoE SHUT the Petroline. The Hormuz bypass is down while Hormuz runs at ~7% of baseline.

## What the primary actually says

**Saudi Ministry of Energy, statement on X, Fri 2026-09-11** — the **East-West (Petroline)** crude pipeline is **SHUT DOWN *"as a precautionary measure"*** following *"multiple"* attacks in the **Riyadh and Madinah regions** on **Thu 2026-09-10**. Four independent relays.

**This is the primary that two WALTER BOARD rows pre-registered as the resolving condition** (`SIG-W-20260910-021` kill-guard registration; `SIG-W-20260911-004` *"if a primary lands… it routes as a CORRECTION-class item"*). Both rows are annotated additively; neither is rewritten.

## Owner grade — FALCON, carried not re-derived

**FALCON, 17:49 ET 9/11 (`8a1cd4040`), on resolver #1 pre-committed the previous night:**

- **STATUS tell #2 (Yanbu/Petroline): 🔴 FIRED.**
- **Marks HOLD on the letter — B 3 / C 22 / D 75.** The D→85 rung is ARMED but **a pipeline is none of rung triggers (a)–(d).**
- **GATE 1 / FAL-01: FIRM-NEGATIVE, unchanged.** A **transport** line is not an oil-**production** asset.
- **FAL-05: NOT FIRED.** Volume bar (≥100 kbpd) cleared many times over; the **≥7-consecutive-days-ACTUALLY-ELAPSED** bar is not — **earliest 9/17–18.** Force majeure **SEARCH-NOT-FOUND** and one declaration away (route (a) carries no duration bar). **Confidence deliberately unmoved at 55% — an unrealized clock is a STATUS fact, not a probability move.**

## 🔴 THREE GUARDS — read before quoting any of this onward

1. **"THE STATE SHUT IT" IS CONFIRMED. "THE PIPELINE WAS HIT" IS NOT.** The MoE described a **precautionary shutdown after attacks in two regions** — not a hit on the line. **Newsweek** (*"East-West Oil Pipeline Hit By Houthis, Photos Appear to Show"*) and **NDTV Profit** carry the stronger claim off **satellite imagery**. That is the `IRAN_WAR_GUARDS.md` **"INTERCEPTED → STRUCK in the retelling"** class in its adjacent form; **ADD#15 (do not propagate unconfirmed FIRMS) binds on the imagery leg.** FALCON held the pumping-station names (**Al Mesba'ah / Al Dhekra**) at **C3, satellite relay — deliberately NOT laundered to the MoE's B2.**
2. **ATTRIBUTION IS CONTESTED AND THE HEADLINE ACTOR IS NOT THE REPORTED ONE.** Newsweek / Gulf News headline **Houthis**; FALCON reports drones **originating from IRAQ** (one US official) with **responsibility NOT established**. ⛔ Two actor sets are live. An Iraq launch corridor is a different escalation ladder.
3. **CAPACITY IS NOT LOSS, AND THE FIGURE IS IN DISPUTE INSIDE OUR OWN RECORD.** `SIG-W-20260910-021` guarded **Petroline capacity at ~5 mb/d**; FALCON's write-up says **~7 mb/d**. ⚠️ `IRAN_WAR_GUARDS.md` KILL-ON-SIGHT ① exists because **~7 mb/d is ABQAIQ's nameplate**, and its named failure is **CAPACITY-vs-LOSS CONFLATION**. **A shut bypass removes OPTIONALITY around Hormuz; it is NOT N mb/d of exports stopping.** **FALCON owns the asset and the basis — flagged by packet, not resolved here.** ⛔ **Quote it as SHUT with the basis named. Never as a volume.**

## Why this is acute even with every mark held

**The bypass existed to survive a Hormuz closure. Hormuz is at ~7% of baseline (5–11 transits/day vs the canonical 88/day), and the bypass is now offline.** That is a reduction in *optionality* at the exact moment the optionality was the thing being relied on. **No registered bar moved and none is asserted to have moved.**

## Routing — and why these four

**FALCON packeted BRENT, HAWK and PROME directly at 17:49 ET (`8963e43d5`). Those three are covered AT THE OWNER; re-routing them would manufacture a duplicate** (the same discipline `SIG-W-20260911-004` applied to FALCON and BRENT). **WALTER carries only what that routing did not reach:**

- 🔴 **CARL — `action:`.** The **Iran-cluster CARL-info override** carve-out (May 6 2026) lists *"explicit kinetic event with supply-disruption mechanism — vessel-strike, refinery-hit, **port-closure** — kinetic-actually-affecting-supply, not posture-only"* as a firing trigger. **A state-ordered shutdown of the primary Hormuz bypass is that trigger, not posture.** **ASK: does this change the pump/diesel pass-through read (Vector #5 / #12, KB-CARL-259's 3–4d Iran-regime transmission lag)?** ⚠️ **Context you already hold — do not double-count:** diesel is already on the board at `SIG-W-20260910-020` (US diesel futures $216/bbl, highest in history) and `SIG-W-20260910-005` (Aug PPI diesel +24.1%); **the FT's *"US diesel hits record $6 a gallon"* is the retail leg of ground you already have, and is NOT dispatched separately.**
- **SAM — `info:`.** Oil-yen leg, per the `GEOPOL_ENERGY` info line. Japan is a Gulf-crude importer and the yen is mid-intervention; **no ask.**
- **NEXUS — `info:`.** Convergence only; `SIG-W-20260911-004` already routed NEXUS on the unconfirmed version and this is its resolution. **No ask.**
- **RED — `info:`.** A pre-committed resolver written the night before produced the grade, and **FALCON moved no mark and no confidence on a fired tell** — that is registered-instrument discipline, which is RED's standing interest. **No ask.** (Exempt recipient; BOARD ID-diff is its channel per §3.5.8.)

**No safety-net upgrade:** VIX 15.84 [9/11], HY OAS 270bp [9/10 FRED print] −1bp. Nothing engaged.

---

## 🆕 ADDENDUM — 2026-09-11 ~23:5xZ. TIER-1 WIRE CORROBORATION ARRIVED, AND IT SETTLES GUARD ③. (Will-Telegram batch BM-20260911-02, items 2 and 3.)

**Two tier-1 outlets, independently, within ~90 minutes of each other:**

- **WSJ, Summer Said / Georgi Kantchev / Saleh al-Batati — "Saudi Arabia Shuts Down Pipeline That Was a Crucial Hormuz Bypass," updated Sept 11 2026 3:53 pm ET.** Standfirst: *"The East-West pipeline—**which can carry up to 7 million barrels of oil a day**—came under attack as Middle East violence continued to flare."* **Lead image: a satellite photo of smoke rising from an area of the East-West pipeline south of Medina on Thursday — credited EUROPEAN UNION / COPERNICUS SENTINEL / REUTERS.**
- **Bloomberg, Devika Krishna Kumar — "Saudi Shuts Oil Pipeline That Bypasses Hormuz After Attacks," Sept 11 2026 2:46 pm EDT, updated 4:28 pm EDT.**

### ✅ GUARD ③ (the capacity figure) IS SETTLED — in FALCON's favour, and on the right basis

**WSJ states the line *"can carry up to 7 million barrels of oil a day."*** That is **explicit CAPACITY language** — *"can carry up to"* — at a tier-1 outlet. ⇒ **FALCON's "~7 mb/d" is CORROBORATED AS A CAPACITY FIGURE.** `SIG-W-20260910-021`'s "~5 mb/d" guard is the **older design figure** and is **superseded as the capacity number** (annotated on that row).

⛔ **THE OPERATIVE HALF OF THE GUARD SURVIVES INTACT AND IS NOT RETIRED: capacity is still not loss.** WSJ says what the line *can carry*, not what stopped. **A shut bypass removes optionality around Hormuz; it is not 7 mb/d of exports ceasing.** ⚠️ **KILL-ON-SIGHT ① still fires on any rendering of this as "7 mb/d offline," and that rendering is now MORE likely, not less, because a tier-1 capacity figure is exactly what gets re-quoted as a loss.**

### 🟠 GUARD ① (shut vs hit) MOVES BUT DOES NOT FULLY CLEAR

**WSJ asserts the pipeline *"came under attack"* and publishes a Copernicus Sentinel image, via Reuters, of smoke at the line south of Medina.** ⇒ **This is a material upgrade on the imagery leg — a named, attributable satellite product from a tier-1 wire, not the unattributed FIRMS hotspots ADD#15 was written against.** **The "attacks occurred at/near the line" claim is now carried by two tier-1 outlets.**

⚠️ **BUT THE MoE ITSELF STILL ONLY SAYS "PRECAUTIONARY SHUTDOWN AFTER ATTACKS IN THE RIYADH AND MADINAH REGIONS."** **No Saudi statement confirms damage TO THE LINE, and no operator has quantified any.** ⇒ **Carry "attacked, per WSJ/Bloomberg + Copernicus imagery; shut precautionarily, per the MoE; damage to the line NOT established by any operator."** ⛔ **Still do not write "the pipeline was destroyed/disabled."** **FALCON owns any upgrade of the damage leg.**

### ⚪ GUARD ② (attribution) IS UNCHANGED — neither wire settles it

**Neither headline attributes the attack.** WSJ says *"as Middle East violence continued to flare"*; Bloomberg says *"After Attacks."* **Newsweek/Gulf News still say Houthis; FALCON still reports drones originating from IRAQ, responsibility not established.** ⛔ **Two actor sets remain live.**

📌 **Geography note, consistent across all sources and worth keeping:** the smoke is **south of Medina**, which matches the `SIG-W-20260911-004` FIRMS description (SE of Medina toward Mahd adh-Dhahab) and FALCON's C3 pumping-station read (Al Mesba'ah / Al Dhekra). **Three independent descriptions of the same geography is corroboration of LOCATION, not of damage.**

**Routed onward:** the capacity resolution is packeted to FALCON (asset owner) as an update to tonight's flag; **no mark, gate or count moves on this addendum, and none is asserted to.**
