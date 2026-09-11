---
signal_id: SIG-W-20260910-021
date: 2026-09-10
timestamp: 2026-09-10T23:44:00Z
time_dispatched: 2026-09-10T23:44:00Z
source: WALTER
origin: "Will-Telegram 8-image batch 23:26Z (BM-20260910-06 item 8) — RT @RT_com X.com, screenshot without visible date; flagged-source class per anchor guards"
domain: GEOPOL_ENERGY
cluster: HYDROCARBON_INFRA
precedence: PRIORITY
action: ["FALCON"]
info: ["BRENT", "HAWK", "PROME"]
entities: ["RT", "Ansarallah", "Houthis", "Saudi-Aramco", "East-West-Pipeline", "Petroline", "Yanbu", "Al-Madinah", "NASA-FIRMS", "Satellite-Hotspots"]
confidence: 0.20
confidence_language: FLAGGED-SOURCE-UNVERIFIED
signal_type: catalyst-unverified
resources: 3
safety_net: kill-guard-active
word_count: 260
verdict: "RT @RT_com posts: 'Ansarallah allegedly STRIKES Saudi Arabia's EAST-WEST OIL PIPELINE — MULTIPLE FIRE HOTSPOTS ERUPT along ROUTE. 6 SATELLITE FIRE HOTSPOTS FLARE UP along the PIPELINE ROUTE at nearly the SAME TIME.' Two satellite images of Al-Madinah Al-Munawwarah Province area with red hotspot marks. ⛔ MULTIPLE GUARDS ACTIVE: RT is a flagged-source class; NASA FIRMS ADD#15 kill-on-sight unless coordinates published; the Petroline 2019 trap guard is named directly in the anchor. This dispatch REGISTERS the claim for FALCON adjudication; it does NOT propagate the strike as fact."
---

# ⛔ RT claim: Ansarallah 'allegedly' strikes Saudi East-West Oil Pipeline (Petroline) — 6 satellite hotspots — KILL-GUARDS ACTIVE, dispatch registers for FALCON adjudication ONLY

## Signal (verbatim per image, RT frame preserved)

**Headline:** *"Ansarallah allegedly STRIKES Saudi Arabia's EAST-WEST OIL PIPELINE — MULTIPLE FIRE HOTSPOTS ERUPT along ROUTE."*
**Sub:** *"6 SATELLITE FIRE HOTSPOTS FLARE UP along the PIPELINE ROUTE at nearly the SAME TIME."*
**Imagery:** Two side-by-side satellite images labelled *"Al Madinah Al Munawwarah"* and *"Al Madinah Al Munawwarah Province,"* with red hotspot dots along a corridor west of the labelled area, and *"Yanbu"* visible at the western edge. RT watermark on both.

**Date on the image:** not visible in the screenshot.

## ⛔ Why this is a PRIORITY-dispatch-with-KILL-GUARDS, not IMMEDIATE

**Three anchor-guards fire simultaneously on this claim:**

1. **`anchors/IRAN_WAR_GUARDS.md` — RT / flagged-source class.** Anchor names RT alongside UANI in the flagged-sources list; carry claims from these accounts BEHIND primary verification, never propagate.
2. **`anchors/IRAN_WAR_GUARDS.md` ADD#15 — DO NOT PROPAGATE NASA FIRMS AS CONFIRMED without published coordinates.** The "6 satellite hotspots" claim is FIRMS-class satellite thermal by construction; RT is asserting fire without publishing coordinates or a link to the FIRMS pull.
3. **`anchors/IRAN_WAR_GUARDS.md` — Petroline 2019 trap.** The 2019 Aramco strike on Abqaiq/Khurais is the highest-indexed "Houthi hits Saudi oil infrastructure" story and search-summary layers merge it into any fresh Petroline claim. Do NOT let a summary attach 2019's ~5.7 mb/d number to this claim.

**If any leg of this confirms at Aramco / SPA / Reuters primary, it fires FAL-01 (production-infrastructure hit — the ONE-that-matters rung on the anchor's ladder).** That is why it dispatches now to FALCON despite the guards. If it does NOT confirm, it becomes a kill-log entry.

## Ask

**FALCON (action):** verify at Aramco statement + Saudi Press Agency + Reuters + Petroline flow/pressure indicators (5 mb/d east-west line, terminates at Yanbu on the Red Sea). If confirmed, this fires FAL-01. If refuted or unconfirmed within a graded window, WALTER kill-logs the RT post as a class-adverse example.

**BRENT / HAWK (info):** Petroline is the strategic bypass of Hormuz — a real hit is orders-of-magnitude worse than a Jazan-class refinery strike. But only IF real.

## Guards travelling with this dispatch

- ⛔ Do NOT propagate this as fact downstream.
- ⛔ Do NOT let "~7 mb/d" or "5 mb/d offline" attach to this claim from the search-summary layer (Petroline capacity is ~5 mb/d; historical hits removed 0.5 mb/d peak; the anchor's Abqaiq guards fire on any bigger number without Aramco statement).
- ⛔ Do NOT allow "6 satellite hotspots" to become "6 explosions" or "6 confirmed strikes" — hotspots ≠ strikes.
- 🔑 Named RT watermark on both images — the FIRMS pull, if any, is somewhere behind the RT post; find it before repeating the count.

---

## ✅ RESOLVED 2026-09-11 ~22:0xZ — the claim this row REGISTERED is now partly confirmed at the Saudi state, and partly still not. (Additive; nothing above rewritten.)

**This row dispatched at confidence 0.20 with `safety_net: kill-guard-active` and refused to propagate the strike as fact. That refusal held up, and it is worth recording which half survived.**

- ✅ **CONFIRMED at B2:** the **Saudi Ministry of Energy** stated (X, Fri 2026-09-11) that the East-West/Petroline crude line is **SHUT DOWN *"as a precautionary measure"*** after *"multiple"* attacks in the **Riyadh and Madinah regions** on **Thu 2026-09-10**. **FALCON graded STATUS tell #2 FIRED at 17:49 ET 9/11 (`8a1cd4040`) on a resolver pre-committed the previous night.** Marks HOLD (B 3 / C 22 / D 75); **GATE 1 / FAL-01 still FIRM-NEGATIVE** (transport ≠ production); FAL-05 still unfired (elapsed-days bar, earliest 9/17–18).
- ❌ **STILL NOT CONFIRMED:** that the **pipeline itself was struck.** The MoE described a *precautionary shutdown after attacks in two regions*, not a hit on the line. **The RT claim this row registered — "6 satellite fire hotspots along the pipeline route" — remains uncorroborated at any publisher this fleet has queried; FALCON could run no FIRMS pull of its own (`Invalid MAP_KEY`, no coordinates published) and held the pumping-station names (Al Mesba'ah / Al Dhekra) at C3.** **ADD#15 still binds on the imagery leg.**
- ❌ **ATTRIBUTION STILL NOT ESTABLISHED — and it moved AWAY from this row's claim.** This row registered an **Ansarallah/Houthi** claim. FALCON reports drones **originating from IRAQ** (one US official), responsibility **not established**. Newsweek and Gulf News still headline Houthis. ⛔ **Two actor sets are live; neither is settled.**

### 📌 THE GUARD ON THIS ROW FIRED, AND IT NOW HAS A LIVE DISCREPANCY TO SETTLE

This row's own guard block reads: ***"Do NOT let '~7 mb/d' or '5 mb/d offline' attach to this claim… Petroline capacity is ~5 mb/d."*** **FALCON's 9/11 adjudication describes the line as *"~7 mb/d."*** Both figures are defensible about different things (original design ~4.8–5 mb/d; post-expansion capability cited up to ~7), **but they cannot both travel unqualified on the same asset**, and `IRAN_WAR_GUARDS.md` KILL-ON-SIGHT ① exists because **~7 mb/d is ABQAIQ's nameplate** and the named failure mode is **CAPACITY-vs-LOSS CONFLATION**.

⚠️ **WALTER does not resolve this — FALCON owns the asset and the number's basis. Flagged to FALCON by packet, not edited.** ⛔ **Until it is settled: quote the line as SHUT with the basis named, never as a volume loss. A bypass going offline removes OPTIONALITY around Hormuz; it is not N mb/d of exports stopping.**

**Superseding item:** `SIG-W-20260911-004` (supersession block) and `SIG-W-20260911-006`.

---

## 📌 CAPACITY GUARD UPDATED 2026-09-11 ~22:1xZ — the ~5 mb/d figure is SUPERSEDED; the capacity-vs-loss half of the guard STANDS.

**WSJ (9/11, 3:53 pm ET) states the East-West line *"can carry up to 7 million barrels of oil a day."*** That is explicit capacity language at a tier-1 outlet. ⇒ **This row's "Petroline capacity is ~5 mb/d" is the older DESIGN figure and is superseded as the capacity number. FALCON's ~7 mb/d is corroborated.**

⛔ **THE REST OF THIS ROW'S GUARD IS NOT RETIRED AND IS NOW MORE LOAD-BEARING, NOT LESS:** *"do NOT let '~7 mb/d' or '5 mb/d offline' attach to this claim."* **A tier-1 CAPACITY figure is precisely what gets re-quoted as a LOSS** — which is the named failure of `IRAN_WAR_GUARDS.md` KILL-ON-SIGHT ①. **"7 mb/d offline" remains KILL-ON-SIGHT. What is confirmed is that the line is SHUT.**

**Also upgraded:** this row flagged that *"the FIRMS pull, if any, is somewhere behind the RT post."* **WSJ has since published a EUROPEAN UNION / COPERNICUS SENTINEL / REUTERS satellite image of smoke at the line south of Medina on Thursday** — a named, attributable product, a material upgrade over the RT-watermarked images this row registered. **The "6 hotspots" COUNT is still not corroborated and should still not travel.**
