---
signal_id: SIG-W-20260622-011
dispatched: 2026-06-23T03:22:00Z
origin: Will-Telegram 6-image batch 3 2026-06-22 (img #4 primary + Polymarket datum folded from img #1) — @MarineTraffic X post + vessel-crossing map; Karel Mercx Polymarket datum
source: MarineTraffic (by Kpler) — primary vessel-tracking data (X, 6/22); + Karel Mercx Polymarket relay (folded)
signal_type: pattern-match
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
cluster_secondary: HYDROCARBON_INFRA
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: HAWK
info: [BRENT, SAM, RED]
confidence: 0.82
verify_verdict: SKIP-VERIFY — MarineTraffic (Kpler) is a primary vessel-tracking source; the transit counts (71 confirmed 19-21 June, weekend peak 35 on 6/20) are AIS-derived primary data. Polymarket datum (Mercx) carries thin-liquidity-single-print discipline.
routing_note: GEOPOL_ENERGY (Hormuz throughput) → HAWK action; BRENT, SAM, RED info. signal_role cluster_mediating (transit REBOUND/AIS-active-improving vs recovery-FRAGILE/below-pre-crisis/dark-routes/demining-incomplete) → RED auto-cc. **Iran-anchor pre-dispatch check:** IRAN_WAR.md fresh (6/22); this is the most complete transit-count layer of the day — refines the physical-reopening leg WITHOUT flipping state (rebound real but fragile; reconciles the prior snapshots: weekend 6/20 peaked at 35, Mercx's "back to 3 by 6/21" = the fade). Complements SIG-W-20260622-006 (export-flow layer) + SIG-W-20260622-004 (freight layer). Folds the Polymarket "<50% Hormuz-normal-by-July-31" market-implied-timing datum (Mercx, img#1).
---

# Strait of Hormuz crossings rebound but fragile — 71 transits 19-21 June, weekend peak 35; market prices <50% normal-by-July-31

**One line:** MarineTraffic (Kpler): vessel activity through Hormuz increased sharply 19-21 June — **71 confirmed transits, weekend peak of 35 crossings on 20 June**, more vessels transiting with **AIS active** (improving operator confidence) following the blockade lifting. But the recovery is fragile — traffic remains below pre-crisis, many vessels still use Iranian-route/dark patterns, demining is incomplete, and diplomatic uncertainty weighs. Polymarket prices **<50% chance** Hormuz traffic returns to normal by July 31.

## What it is
- **MarineTraffic (primary AIS):** 71 confirmed transits 19-21 June; weekend peak **35 crossings on 20 June**; AIS-active share rising = improving operator confidence; rebound follows blockade lifting + free-passage signals.
- **The fragility caveats (same post):** traffic below pre-crisis; many vessels still on Iranian-route or dark patterns; demining incomplete; diplomatic uncertainty weighs.
- **Market-implied timing (Polymarket via Karel Mercx, folded):** **<50% chance** Strait-of-Hormuz traffic returns to normal by **July 31** — a single thin-liquidity print, but a market-implied reopening-timing read.

## Why it routes (the genuine delta — the transit-count layer)
This is the fullest throughput dataset of the day and it **reconciles the day's conflicting Hormuz snapshots**: the weekend (6/20) peaked at 35 crossings, then faded back to ~3 by 6/21 (Mercx, prior dups) — consistent with a real-but-fragile rebound, not a clean reopening. It complements the export-flow layer (SIG-W-20260622-006 open Iranian flows) and the freight layer (SIG-W-20260622-004 VLCC spike). Net physical-leg read: **rebounding but below pre-crisis, AIS-confidence improving, still 0/4 on the verified liner-carrier/JWC reopening gate.** The market agrees it's not normal — <50% by July 31.

### → HAWK (ACTION)
Your transit-count layer, from a primary tracker: 71 transits / peak 35 (6/20) + rising AIS-active = the rebound is real and confidence is improving — but MarineTraffic itself flags below-pre-crisis + dark-routes + demining-incomplete. This is the data to anchor your reopening-ladder read on (vs the noisier 15→3 / dark-tanker snapshots). The Polymarket <50%-by-July-31 is a useful market-implied benchmark for your timing call. Reconcile the weekend-35-then-3 fade — that IS the fragility.

### → BRENT (INFO)
Transit rebound (71 in 3 days, AIS-active up) = supply-route normalization continuing at the margin — consistent with the flat-price decline. But below pre-crisis + Polymarket <50%-normal-by-July-31 says the market isn't pricing full reopening. Composes with the SPR/Cushing thin-buffer read (SIG-W-20260622-005). Your call on the supply-balance weight.

### → SAM (INFO)
Hormuz throughput rebound = easing Asia crude-supply/route risk at the margin; low-priority context for the regional read.

### → RED (INFO — cluster_mediating auto-cc)
- **Rebound read:** 71 transits / peak 35 / rising AIS-active = the reopening is happening, confidence returning, decoupling holds.
- **Fragility read:** below pre-crisis, weekend-35-faded-to-3, dark-routes persist, demining incomplete, market prices <50% normal-by-July-31 = a fragile, reversible rebound, not a verified reopening.
- Your call on durability.

## Sources
- MarineTraffic @MarineTraffic (X, 6/22) — vessel-crossing data + map.
- Polymarket via Karel Mercx @KarelMercx (X, 6/22, folded from batch-3 img#1).
- Cross-ref: SIG-W-20260622-006 (export flow), SIG-W-20260622-004 (freight), SIG-W-20260621-004 (Hormuz 15→3); IRAN_WAR.md anchor 6/22.
