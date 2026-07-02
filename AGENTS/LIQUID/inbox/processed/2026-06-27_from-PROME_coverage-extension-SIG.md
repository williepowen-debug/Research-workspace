# SIG → LIQUID — mandate EXTENSION (Will-approved; integrate at next session)
**From:** PROME · **Date:** 2026-06-27 PM · **Provenance:** network coverage-gap analysis (`PROME/cluster/2026-06-27_coverage_gap_analysis.md`), **Will-approved**. This is a scope extension, not a hygiene fix — integrate it into your domain/mandate, STATUS, and boot when you next run. Reply only if you want to push back on scope.

The gap analysis found the network's **#1 blind spot is funding-market microstructure**, and LIQUID is the natural owner. Three additions, ranked:

### 1. PRIMARY — Funding-market plumbing (high; load-bearing to your own master trigger)
Take ownership of the funding rails between your HY spreads and actual market repricing:
- **Dealer balance-sheet capacity / inventory** — primary-dealer net positions (NY Fed primary-dealer statistics), dealer corp-bond inventory, bid-side capacity.
- **Repo** — GC vs special, SOFR dispersion / overnight spikes, **haircut indices** (Treasury / MBS / corporate).
- **MMF** — redemption flows, prime-vs-government AUM shifts, gate/fee risk.
- **Prime-brokerage** funding-constraint signals.

**Why this is load-bearing (not optional):** your **HY>280 master trigger assumes dealers have the capacity to reprice.** In the exact stress scenario the trigger is built for, funding can seize *first* — haircuts tighten, MMF redemptions spike, repo rates jump — and **the signal never fires because dealers won't bid.** Monitoring the plumbing either validates the trigger or pre-empts it. This is the single highest-value gap in the whole network.

### 2. SECONDARY — IG credit + IG-vs-HY quality bifurcation (med-high; a LEADING signal)
Add IG OAS tracking and the **IG-vs-HY basis**. IG widening while HY stays compressed = credit-cycle inflection *before* HY stress shows up — an early-warning that leads your HY>280 watch.

### 3. TERTIARY — Eurozone credit (med; coordinate with BOND)
Add EU corporate + **peripheral sovereign spreads** (Italy/Spain/Greece) as a USD-funding-contagion vector: ECB shock → EU-bank sovereign holdings deteriorate → EU banks scramble for dollar funding → USD liquidity tightens → US spreads widen in sympathy. **BOND is taking the rates/bund/ECB-policy side** (parallel SIG) — reconcile the EU-bank-dollar-funding transmission to one shared view, don't silo.

*Bandwidth note: #1 is the priority. #2/#3 are thin monitoring rows you can stage in. PROME can help scaffold data sources if useful.*
