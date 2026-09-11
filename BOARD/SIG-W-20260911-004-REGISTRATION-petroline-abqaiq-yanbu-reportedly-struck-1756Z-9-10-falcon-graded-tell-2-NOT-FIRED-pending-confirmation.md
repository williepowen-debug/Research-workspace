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
