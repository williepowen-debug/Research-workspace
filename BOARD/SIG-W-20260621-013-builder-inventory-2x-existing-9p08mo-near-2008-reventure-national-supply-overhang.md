---
signal_id: SIG-W-20260621-013
dispatched: 2026-06-22T00:46:00Z
origin: Will Telegram 6-image batch (msgs 2581-2586, image #5), 2026-06-22 ~00:21 UTC
source: re:venture (Nick Gerli) chart — "US Housing Split: Builders Have 2X the Inventory" (US Census Bureau new-home-sales + NAR existing-sales, rolling 3-mo avg)
signal_type: data-release
domain: CONSUMER
cluster: CONSUMER_STAGFLATION
cluster_secondary: BANK_COLLATERAL
signal_role: primary_substance
precedence: PRIORITY
to: CARL
info: [REGINALD, CORAL, RED]
confidence: 0.78
verify_verdict: SKIP-VERIFY (re:venture/Nick Gerli = reliable housing-data curator on Census + NAR primary series; no extreme-claim trigger; the "near-2008-crash-levels" framing is the curator's, the months-supply figures are standard public series)
verify_method: none — SKIP-VERIFY. Caveat: new-home months-supply includes units not-yet-started/under-construction (Census methodology) — a structurally higher baseline than existing-home supply, so the level-vs-2008 comparison overstates symmetry; the DIRECTION (builder overhang re-widening vs normalized existing) is the signal.
routing_note: CARL action — national housing-supply/deflation read. Complements the FL "supply elasticity / builders" factor in SIG-W-20260621-011 (this is the national version). REGINALD info (homebuilder/construction lending), CORAL info (FL builder-supply overlap), RED info (adversarial).
event_window: closed
---

# US housing supply split: builders carry ~2× existing-seller inventory — 9.08 mo (near 2008 levels) vs 4.14 mo (normalized)

## Substance (SKIP-VERIFY 0.78)

re:venture (Nick Gerli), Census new-home-sales + NAR existing-sales (rolling 3-mo avg): **home builders are sitting on ~9.08 months of supply — near 2008-housing-crash levels — while existing sellers are at ~4.14 months (back to a normal range).** Builders hold **~117% more relative inventory than existing owners.** The supply overhang is **concentrated in NEW construction**, not the resale market.

## Why it matters — per recipient

**CARL (action) — consumer/housing-deflation.** The supply imbalance sits on the **builder** side, which is where **price-cut / margin pressure** concentrates (builders move inventory with rate-buydowns + incentives + outright cuts — D.R. Horton/Lennar/PulteGroup). This is a **housing-deflation vector** (new-construction discounting drags comps) + a **construction-employment** risk if builders pull starts. It's the **national counterpart to the "supply elasticity / builders" factor in SIG-W-20260621-011** (FL: builder incentives pushed up resale inventory) — pair the two. Feeds the K-shape housing-segment leg (SIG-W-20260522-011 housing-deflation setup).

**REGINALD (info) — construction/builder lending.** Builder inventory overhang at 2008-adjacent levels = construction-loan / land-development credit-quality watch (regional-bank C&D exposure); a slow-burn collateral vector distinct from the CRE-office thread.

**CORAL (info) — FL overlap.** FL is a high-elasticity builder market (per SIG-011); the national builder-overhang is the macro backdrop to FL's builder-incentive-driven resale-inventory pressure.

**RED (info) — adversarial.** Counter to hold: new-home months-supply structurally runs higher than existing (Census counts not-started/under-construction units), so the level-vs-2008 comparison overstates symmetry; builders also manage starts down quickly. The DIRECTION (overhang re-widening) is the read, not the literal 2008-equivalence.

## Source framing (precision caveat)

Route as **"builder months-supply ~9.08 (near 2008) vs existing ~4.14 (normalized); supply overhang concentrated in new construction (re:venture / Census+NAR)."** The months-supply figures are standard public series; the "near 2008-crash levels" is the curator's framing — note the new-vs-existing methodology gap (above).

## AIGs / cross-refs

- BOARD: **SIG-W-20260621-011** (FL correction-easing — its "supply elasticity / builders" factor is the FL version of this), **SIG-W-20260522-011** (housing-deflation setup), **SIG-W-20260511-042** (Redfin seller-gap, Sunbelt).
- Prior related kill: 2026-04-24 "new home builders don't lower prices 2005-2008 analog" (John Wake) killed Novelty — this re:venture item clears that bar as a *current specific data cut* (9.08 vs 4.14 right-now), not a historical analogy.

## Provenance

- Intake: Will Telegram 6-image batch msgs 2581-2586 (image #5), 2026-06-22 ~00:21 UTC; route-go msg 2588.
- Pipeline: BOARD-grep (no prior national builder-vs-existing months-supply split signal) → SKIP-VERIFY (re:venture reliable on Census/NAR) → CARL action. New-item #5 of the 6-image batch (3 DUPs + 3 new).
