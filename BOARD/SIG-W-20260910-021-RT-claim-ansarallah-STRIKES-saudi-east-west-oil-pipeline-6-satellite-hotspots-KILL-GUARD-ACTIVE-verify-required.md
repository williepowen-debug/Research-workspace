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
