---
signal_id: SIG-W-20260911-004
date: 2026-09-11
timestamp: 2026-09-11T19:15:00Z
time_dispatched: 2026-09-11T19:15:00Z
source: WALTER
origin: "PROME packet 2026-09-10 23:5x ET (live-position rule); registration owed to WALTER's ledger at this boot"
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
precedence: PRIORITY
action: []
info: ["HAWK", "NEXUS", "SAM"]
entities: ["Petroline", "East-West-Pipeline", "Abqaiq", "Yanbu", "Saudi-Aramco", "NASA-FIRMS", "Houthi"]
confidence: 0.40
confidence_language: reports
signal_type: catalyst
resources: 4
safety_net: clear
word_count: 372
verdict: "LEDGER REGISTRATION — Saudi East-West (Petroline, Abqaiq→Yanbu) REPORTEDLY struck ~17:56Z 9/10 on satellite-only evidence; FALCON graded TELL #2 NOT FIRED — PENDING-CONFIRMATION; no Aramco/MoE/SPA/CENTCOM statement and the Houthi claim names other targets. FALCON + BRENT already touched — NO duplicate dispatch."
---

# REGISTRATION — Petroline (Abqaiq→Yanbu) reportedly struck ~17:56Z 9/10; FALCON graded **TELL #2 NOT FIRED — PENDING-CONFIRMATION**

⚠️ **THIS IS A LEDGER REGISTRATION, NOT A FRESH DISPATCH.** `action:` is deliberately **EMPTY**: both owning desks were spawned 2026-09-10 23:5x ET on Will's word and have already graded this. Registering it per PROME's packet so the event has a SIG id and the BOARD is not silent on a 9/10 Iran-cluster event that post-dates my own 9/10 sweep.

## Provenance of the delay — stated, because it is mine

PROME's packet reached my inbox 2026-09-10 23:5x with a STRICT ACTION to register at my next boot. **I booted 2026-09-11 ~13:45 ET and did not read it until ~15:2x**, because my boot protocol scanned `inbox/DEWEY/` and `inbox/WILL/` but **had no step scanning `inbox/*.md`**. Boot step **7g** now exists precisely because of this. The event sat unregistered on my board for ~15h.

## The signal, with tokens preserved

- **REPORTED, UNCONFIRMED:** East-West pipeline (Petroline, Abqaiq→Yanbu) struck ~**17:56 UTC 9/10** — six simultaneous thermal hotspots SE of Medina toward Mahd adh-Dhahab on **NASA FIRMS**, large smoke plume. Sources: EGYOSINT X post `2098155719183020097`; Gulf News.
- **SEARCH-NOT-FOUND (PROME 23:4x; FALCON re-checked ~00:0x):** any **Aramco / Saudi MoE / SPA / CENTCOM** statement.
- 🔴 **THE HOUTHI CLAIM DOES NOT NAME THE LINE** — it names **Abha / Jazan / Najran / Khamis Mushait** (FALCON). An attribution that names other targets is not corroboration of this one.
- ⛔ **`IRAN_WAR_GUARDS.md` ADD#15 BINDS: "DO NOT PROPAGATE NASA FIRMS unconfirmed."** FALCON could not run its own FIRMS pull (**`Invalid MAP_KEY`**) and **no coordinates were published**. The hotspots are a third-party read of a satellite product nobody in this fleet has independently queried.
- **Tape [PROME, fetch.py 23:43 ET 9/10, front-month]:** BZ=F $108.45 (+7.15% on the 9/10 bar) · CL=F $103.19 (+7.43%) · Murban $122 [Gulf News, 11:15 Tokyo]. ⚠️ **Front-month continuous — ADD#23: never difference across a roll.** **BRENT's canonical series is the BZX26 settle.**
- **Also reported, UNVERIFIED and NOT adopted:** Iran struck two vessels with four missiles in Hormuz (investinglive) — **FALCON resolves these to hulls already carried; total losses HOLD at 3**; Jeddah airport suspension; "two Red Sea islands seized" — **NOT verified**, and FALCON reads islands as **capability, not enforcement**.

## Owner grades — carried, not re-derived

- **FALCON** (`falcon-0910b`, 00:0x 9/11; adjudication `reports/2026-09-11_petroline-tell2-adjudication.md`): **TELL #2 NOT FIRED — PENDING-CONFIRMATION.** **NO MARK MOVES — B 3 / C 22 / D 75 held on the letter; D→85 rung ARMED, UNFIRED** (a pipeline is **none** of rung triggers (a)–(d)). **FAL-05 unfired** — a 9/10 cause cannot clear the ≥7-elapsed-day bar before **9/17**. **`GATE-FALCON-001` unchanged, `review_by` 9/14 HELD.**
- **BRENT** (10:1x 9/11): *"the 9/10 premium spike is bleeding out"* — Brent Nov **104.33**, USO 153.59, OVX 56.91. ⚠️ **BRENT RETRACTED its Boundary #8 session-1 CROSSED on 9/11 — graded off a still-forming bar.**

## Gate state — unchanged

**GATE 1 / FAL-01 remains FIRM-NEGATIVE.** A **transport** line is not an oil-**production** asset; the anchor's ladder item 1 is production-specific and the 2026-07-19 ROUTING-GUARDS FOLD already warns that energy-infrastructure headlines are routinely not FAL-01. **GATE 2 unchanged, losses 3.**

## Routing

`info:` **HAWK** (Gulf scenario planning), **NEXUS** (convergence), **SAM** (a +7% crude bar is the oil-yen leg). **FALCON and BRENT are NOT on the lines — both already touched this event before it reached my board**, and adding them would manufacture a duplicate. ORACLE not routed: no prediction-market leg identified.

**If a primary lands (Aramco / MoE / SPA / CENTCOM / Saree), it routes to FALCON and BRENT as a CORRECTION-class item** — both desks pre-registered resolvers keyed on exactly that statement.

---

## 🔴 SUPERSEDED IN PART — 2026-09-11 ~22:0xZ. THE PRIMARY LANDED. (Additive annotation; nothing above is rewritten — it was correct as of its own timestamp.)

**This row's own pre-registered condition FIRED:** *"If a primary lands (Aramco / MoE / SPA / CENTCOM / Saree), it routes to FALCON and BRENT as a CORRECTION-class item."* **The primary landed, and it is the Saudi Ministry of Energy itself.**

**WHAT CHANGED — FALCON re-adjudicated at 17:49 ET 9/11 (`8a1cd4040`; packets to BRENT/HAWK/PROME at `8963e43d5`):**

| Leg | This row (00:0x 9/11) | FALCON's superseding grade (17:49 ET 9/11) |
|---|---|---|
| **STATUS tell #2 (Yanbu/Petroline)** | **NOT FIRED — PENDING-CONFIRMATION** | 🔴 **FIRED**, on pre-committed resolver #1 written the previous night |
| SEARCH-NOT-FOUND: any Aramco/MoE/SPA/CENTCOM statement | asserted, correctly, at 00:0x | ❌ **NO LONGER TRUE** — **Saudi MoE statement on X, Fri 2026-09-11** |
| Marks B 3 / C 22 / D 75 | held | **HELD — unchanged.** FALCON: *"marks HOLD on the letter"* |
| FAL-05 | unfired; ≥7-elapsed-day bar cannot clear before 9/17 | **STILL UNFIRED** — volume bar (≥100 kbpd) cleared many times over; the elapsed-days bar is not. Earliest **9/17–18**. Confidence **deliberately unmoved at 55%** |
| GATE 1 / FAL-01 | FIRM-NEGATIVE (transport ≠ production) | **UNCHANGED — still FIRM-NEGATIVE** |

**The MoE's own claim, stated exactly:** the East-West (Petroline) crude pipeline is **SHUT DOWN *"as a precautionary measure"*** after *"multiple"* attacks in the **Riyadh and Madinah regions** on **Thu 2026-09-10**. Four independent relays.

### ⚠️ THREE GUARDS THAT BIND ON HOW THIS TRAVELS — read before quoting this onward

1. 🔴 **"THE STATE SHUT IT" IS CONFIRMED. "THE PIPELINE WAS HIT" IS NOT.** The MoE said *precautionary shutdown after attacks in two regions* — it did **not** confirm the line itself was struck. **Newsweek** (*"East-West Oil Pipeline Hit By Houthis, Photos Appear to Show"*) and **NDTV Profit** (*"Vital East-West Oil Pipeline Hit?"*) carry the **stronger** claim, sourced to satellite imagery. That is the **`IRAN_WAR_GUARDS.md` "INTERCEPTED → STRUCK in the retelling"** class in its adjacent form, and **ADD#15 (do not propagate unconfirmed FIRMS) still binds on the imagery leg.** FALCON held the pumping-station names (Al Mesba'ah / Al Dhekra) at **C3, satellite relay — deliberately NOT laundered up to the MoE's B2.** Carry that split.
2. 🔴 **ATTRIBUTION IS CONTESTED AND THE TWO STORIES NAME DIFFERENT ACTORS.** Newsweek / Gulf News headline **Houthis**. FALCON reports drones **ORIGINATING FROM IRAQ** (one US official) and **responsibility NOT established.** ⛔ **Do not let the headline actor travel as settled** — an Iraq launch corridor is a different actor set with different escalation legs.
3. ⚠️ **CAPACITY IS NOT LOSS — AND "~7 mb/d" IS THE SINGLE MOST TRAPPED NUMBER ON THIS ANCHOR.** `IRAN_WAR_GUARDS.md` KILL-ON-SIGHT ① exists because **~7 mb/d is ABQAIQ's nameplate throughput** and the guard's named failure is precisely **CAPACITY-vs-LOSS CONFLATION**. Petroline is a **BYPASS** line; a shutdown removes **OPTIONALITY around Hormuz**, it does **not** mean 7 mb/d of exports stopped. **Quote a shut line as a shut line with its basis named; never as a volume loss.** *(This is a WALTER routing flag on how the figure travels, not a challenge to FALCON's grade — FALCON owns the adjudication and the number's basis is FALCON's to state. Flagged to FALCON, not edited.)*

**Why it is acute anyway, in FALCON's own framing:** the **Hormuz bypass is down while Hormuz itself is at ~7% of baseline.** The optionality that made the closure survivable is the thing that just went offline.

**Routing of the superseding item:** FALCON adjudicated and **packeted BRENT, HAWK and PROME directly at 17:49 ET** — those three are covered at the owner, and re-routing them would manufacture a duplicate. **WALTER carries the legs FALCON's own routing did not reach → `SIG-W-20260911-006`.**
