---
signal_id: SIG-W-20260626-011
dispatched: 2026-06-26T22:32:00Z
origin: Will-Telegram image batch 2026-06-26 (batch 4) — (a) Steve Rattner (@SteveRattner) "Unsold new homes piling up — new-home sales −7.3% May to 580k, supply 10.3 months, tied mid-2022 / most since 2008-09 bust"; (b) Jason Lewris (@jasonlewris) + Parcl "Where Sellers Are Blinking" by-state price-cut map (AZ ~50%, FL high)
source: US Census/HUD New Residential Sales (May 2026) relayed by Rattner; Parcl Labs by-state listing-price-cut share
signal_type: data-release
domain: CONSUMER
cluster: CONSUMER_STAGFLATION
cluster_secondary: BANK_COLLATERAL
signal_role: primary_substance
narrative_channel: n/a
precedence: PRIORITY
to: CARL
info: [CORAL, REGINALD, RED]
confidence: 0.80
verify_verdict: SKIP-VERIFY 0.80 — new-home sales/supply are Census/HUD primary (Rattner relays the official May print); Parcl by-state price-cut share is Parcl Labs proprietary listing data. Objective.
verify_method: Census + Parcl relay; no verify-spawn.
routing_note: housing demand/supply → CARL action per ROUTING_TABLE; CORAL info (FL — 1-in-7 of US listings + the by-state map), REGINALD info (construction/CRE collateral), RED info. cluster CONSUMER_STAGFLATION; cluster_secondary BANK_COLLATERAL. The SUPPLY + BREADTH complement to today's Parcl builder-MSI (SIG-W-20260626-004, price-cut depth) and the builder-inventory thread (SIG-621-013).
---

# Housing glut deepening: new-home supply 10.3 months (2008-tied) + AZ/FL ~50% of listings cutting prices (CARL + CORAL)

**One line:** Two fresh housing datapoints harden the glut: (a) **new-home sales fell 7.3% in May to a 580k annual rate, while months-of-supply jumped to 10.3 — tied with mid-2022 for the most since the 2008-09 housing bust** (Census/HUD via Rattner; >6 months = a buyer's market, 10.3 is deep glut); (b) **roughly every-other home listed in Arizona and Florida is cutting price** (AZ ~50%, FL among the highest; Parcl "Where Sellers Are Blinking" by-state map), and **Florida alone is ~1 in 7 homes for sale nationwide.** The supply + breadth complement to today's builder-MSI (SIG-W-20260626-004, how hard builders cut): now the inventory is 2008-deep and the price-cutting is geographically broad.

> **GRADE: SKIP-VERIFY 0.80, primary_substance.** Census new-home supply at 10.3 months (2008-tied) is the harder number behind the builder-glut thread (SIG-621-013 builder inventory 2× existing; SIG-626-004 Parcl builder fire-sales). The Parcl by-state map adds the breadth: the price-cutting isn't a metro story, it's half of all listings in two big states. CARL owns the demand read; CORAL owns the FL overlay.

## Per-recipient genuine delta

### → CARL (ACTION) — supply at 2008 levels, price-cuts broadening
1. **New-home months-of-supply 10.3 (May), sales −7.3%** = tied with mid-2022 for the most since the 2008-09 bust. Builders are sitting on a growing glut with mortgage rates still elevated — the leading edge of housing-led demand destruction (builders must clear; pairs SIG-626-004 Parcl fire-sales + SIG-621-013 builder inventory 2× existing). This is the hard Census number under the price-cut anecdotes.
2. **Breadth (Parcl by-state):** ~50% of AZ + a high share of FL listings are cutting prices — the price-cutting is broad, not a few soft metros. FL = ~1 in 7 US listings, so FL weakness is nationally material. Is this normal seasonal softening at higher rates, or the housing-deflation leg of your consumer thesis? Your call.

### → CORAL (INFO) — FL is the epicenter of the breadth
FL is over-represented in the price-cut map (high share of listings cutting) AND is ~1 in 7 of all US listings — so FL's demand-normalization (your contained 🟠 read, foreclosures doubling, condo −6.1%, ~18–20% of 2024-vintage underwater) is nationally load-bearing. Reconcile with your "freeze-not-crash / containment" mark (SIG-621-011): a 50%-of-listings price-cut share is the part that does NOT freeze. Pairs with today's Parcl builder-MSI FL cells (SIG-626-004).

### → REGINALD (INFO)
New-home supply at 2008-tied levels + broad price-cutting = collateral-value direction for construction/residential-CRE bank books. Early read on where homebuilder credit + residential-construction-lending exposure is headed. Confirmatory.

### → RED (INFO)
Steelman: (contained) new-home months-supply is volatile and counts not-started/under-construction units (overstates vs existing); 10.3mo ties 2022 (which did NOT bust); price-cuts are seasonal at high rates; AZ/FL are the most over-built Sun Belt markets, not the nation. (leading) supply 2008-tied + half of two big states cutting + builders gluttng = the housing-led demand leg. Hold both; anchor on the Census supply trajectory + whether the cuts broaden beyond the Sun Belt.

## Sources
- Steve Rattner (@SteveRattner, X) 1:27 PM 6/24/26 — new-home sales −7.3% May to 580k annual rate; months-of-supply 10.3, tied mid-2022 / most since 2008-09 bust (US Census Bureau & HUD, New Residential Sales May 2026, via FRED MSACSR).
- Jason Lewris (@jasonlewris, X) — "every other home listed in Arizona and Florida is cutting prices; FL = 1 in 7 homes for sale nationwide"; Parcl Labs "Where Sellers Are Blinking" by-state price-cut-share map (AZ ~50%, TX ~45%, FL high; June 24 2026, ~40 states + DC).
