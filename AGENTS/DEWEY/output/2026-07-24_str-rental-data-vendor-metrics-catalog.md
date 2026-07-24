# STR / rental-market data-vendor & metrics catalog (+ how to read the signal)
**Date:** 2026-07-24 | **Mode:** Thesis (tooling/reference) | **Confidence:** High (vendor landscape + SFR-REIT disclosures) / Medium (national STR magnitudes — scraped/modeled)

## Key Finding
There is a rich, newly-cheaper STR data landscape, but its core metrics (scraped RevPAR / occupancy / revenue-per-listing) are **the wrong tool for a housing-stress signal**, and the **one metric that would work — parcel-linked STR net-cash-flow-vs-debt-service (DSCR) — is not publicly reachable** (it lives in private-lender books). Read the vendors as a *market-health/host-yield monitor*, not a leading indicator of home prices: the causal literature actually runs the other way (STR entry *raises* prices; STR income *supports* owner solvency), and the current national signal is **normalization, not distress**.

## 1. The vendor landscape — two methodological camps
The camp determines what the data can and cannot see.

| Vendor | Camp | Coverage | Access | What's distinctive |
|---|---|---|---|---|
| **AirDNA** | Scrape-based | 10M+ listings, 120k+ markets (Airbnb+Vrbo) | Paid (priced by market listing-count) | Market standard; Rentalizer (property) + MarketMinder (market). Owned by Alpine Investors; acquired Uplisting (PMS) Jan'24 |
| **Key Data** | **Reservation-based** | 6M+ verified properties, PMS feeds, 40+ KPIs | Paid/enterprise (API/flat file) | **Sees true booking pace, lead time, revenue** — the discriminating forward series |
| **Transparent** | Scrape-based | 26M+ listings global | Enterprise | Owned by **Beyond** (dynamic pricing) — pricing+data consolidation |
| **AllTheRooms** | Scrape-based | Airbnb+Expedia/OTA | Paid | **Acquired by Deckard Technologies Aug'25** (new) |
| **PriceLabs** | Both | Dashboards (scrape) + Portfolio Analytics (real, PMS) + **World STR Index (FREE)** | Free + paid | 3 surfaces; free global index new |
| **Mashvisor** | Scrape-based | US-only, 400+ metros, 10k+ ZIPs | Paid + Airbnb API | US-retail-facing; weekly |
| **AirROI** | Scrape-based | 190+ countries | **FREE global + pay-as-you-go API ($0.01/call) + MCP server** | Cheapest programmatic access; only STR vendor with MCP |
| **Rabbu** | Scrape-based | US-only | Free | Retail-facing |
| Airbnb / Vrbo | Platform-native | Own book | Quarterly shareholder letters (SEC) | The only *transactional* view — but aggregate-only |

**Two disambiguations that trip people up** (both PRIMARY-confirmed):
- **"STR" = CoStar's HOTEL benchmark (STR/STR Global) ≠ short-term rental.** CoStar's STR brand benchmarks *hotels* and does not scrape Airbnb [PRIMARY: CoStar 10-K, 2026-02-26].
- **No CoStar–AirDNA deal exists** (a recurring false rumor). AirDNA is Alpine Investors-owned; CoStar's 2024–25 acquisitions were Visual Lease, Matterport, Domain — not AirDNA.

## 2. The metric set — and the one that matters
Every vendor publishes the same core bundle: **RevPAR, ADR, occupancy, available-listings/supply growth, nights booked, revenue-per-available-listing.**
- **Booking pace / lead time** (forward demand) is the **discriminating class** — carried only by reservation-based feeds (Key Data, PriceLabs Portfolio) + platform-native. Scrape-based vendors *cannot* observe it; they infer booked-vs-blocked from calendar flips (AirDNA's own docs admit they "cannot perfectly distinguish booked and blocked," likely over-stating occupancy).
- **The load-bearing metric is missing from all of them:** STR **DSCR / net-cash-flow-after-mortgage-insurance-HOA-tax** at the parcel level — the actual host-solvency series. It lives in private STR-loan books (DSCR-loan performance) and is **not publicly reachable**. No public dataset breaks out STR/second-home mortgage delinquency or foreclosure either. *This is the single most important gap: without it, "host distress" is inferred from revenue proxies that a supply glut mechanically distorts.*

## 3. What's NEW in the last ~12–18 months
1. **Consolidation:** AllTheRooms→Deckard (Aug'25); Transparent under Beyond; AirDNA→Uplisting (Jan'24).
2. **Newly-free/cheap global data:** PriceLabs **World STR Index** (free, country/state/region RevPAR from 2021); AirROI **free global + $0.01/call API + MCP server**.
3. **Airbnb disclosure regression:** Q1'26 shifted to a blended "Nights and Seats Booked" (lodging+experiences) and **declined to disclose aggregate active-listing change** [PRIMARY: Airbnb Q1'26 Shareholder Letter] — the platform-native supply series got *less* transparent.

## 4. Long-term / SFR-REIT operational metrics (the LTR complement)
Public SFR REITs disclose a consistent set — **blended/new/renewal rent growth, occupancy, turnover, bad-debt %** — in quarterly supplements:

| | INVH Q1'26 | AMH Q1'26 |
|---|---|---|
| Occupancy | 96.3% (Avg Occupancy) | 95.1% (Avg Occupied Days %) |
| Blended rent growth | +1.6% | +2.2% |
| Renewal / New-lease | +3.7% / **−3.0%** | +3.2% / **−0.8%** |
| Bad debt | 0.6% (60bps) | "near historical lows" |
| Same-store NOI | **−0.3% YoY** (opex>rev) | +3.7% |

[PRIMARY: INVH Q1'26 Supplemental Sch 3b, 2026-04-29; AMH Q1'26 8-K/10-Q]. Reads as **normalization** — renewals positive, new-lease negative under supply, bad debt low. **Tricon is now a data gap** (Blackstone take-private 2024 — removes ~38k Sunbelt homes from visibility). Provider indices corroborate a supply-driven soft landing: Zillow ZORI SFR **+1.1% YoY**, Realtor.com **−1.5%** (35th straight monthly decline), John Burns SFR **+1.4%**. **Shadow supply** (failed STR→LTR conversion) is **not a disclosed line item** anywhere — inference-only from negative new-lease growth in STR-heavy metros.

## 5. How to read the signal (the interpretive caveat — do not skip)
- **National = normalization, not distress.** Supply growth decelerated 6.9%→4.7%→~2.7%; RevPAR turned **positive** (+2.1–3.4%); the ~50% revenue-per-listing crashes were **2022–23** mean-reversion off the 2021 blowout, not fresh 2024–26 distress. AirDNA frames 2026 as a recovery year.
- **Distress is metro-specific:** Dallas (all 5 AirROI oversaturation signals, supply +34%, occ 45%), Las Vegas, Austin, Nashville (RevPAR −9.8% YoY), FL Gulf leisure. Florida is **bifurcated** (Miami resilient 1/5 signals; Gulf-coast glutted).
- **Revenue-per-listing is a denominator trap:** a supply glut *mechanically* lowers revenue-per-listing (more listings) even with flat/rising aggregate demand, while zero-booking listings churn out of the "active" denominator — so RevPAL overstates "distress" in exactly the oversupplied markets.

## Counter-Evidence (why the leading-indicator thesis fails)
- **No study establishes STR revenue as a *leading* indicator of home prices.** Peer-reviewed causal work runs opposite: STR *entry* raises prices ~0.026%/1% listings [ACADEMIC: Barron/Kung/Proserpio, Marketing Science 2021]; higher STR density → *lower* foreclosure, STR income *supports* solvency [ACADEMIC: J. Housing Economics 2026].
- Sunbelt "declines first" is a **composition effect** (discretionary/investor buyers cut first — concurrent, shared macro drivers: 7% mortgages, migration reversal, building glut), not demonstrated STR-revenue causation.
- **Regulation is a co-equal forced-exit driver** (e.g. NYC LL18), confounding revenue-attribution of inventory build.
- Both adversarial verifiers this run returned REFUTED / PARTIALLY_SUPPORTED on the leading-indicator claim.

## Source Quality Assessment
Vendor landscape + SFR-REIT disclosures: **High** (primary filings + vendor product docs). National STR magnitudes: **Medium** — AirDNA primary metro pages 403'd on WebFetch, so metro figures lean on secondary aggregators (AirROI/Rabbu/StaySTRA) whose per-listing $ diverge 30–50% by active-listing definition; directions consistent, magnitudes soft. National occupancy is genuinely contested between providers (AirDNA ~55–57% annual vs AirROI ~50% spring-2025 — seasonal-point vs annual-average + methodology).

## References
- AirDNA (airdna.co, 2026 Outlook Dec'25); Key Data (keydatadashboard.com); PriceLabs World STR Index; AirROI; Transparent/Beyond; Mashvisor; Rabbu; AllTheRooms/Deckard
- CoStar Group 10-K (2026-02-26); Airbnb Q1'26 Shareholder Letter (SEC/IR, 2026-05)
- INVH Q1'26 Earnings Release & Supplemental (2026-04-29); AMH Q1'26 8-K/10-Q (2026-04-30); Tricon 6-K (Blackstone take-private)
- Zillow ZORI; Realtor.com June'26 Rent Report; Apartment List; CoStar/Apartments.com; John Burns SFR Index
- Barron/Kung/Proserpio (Marketing Science 2021); "Short-term vs medium-term rentals…foreclosure" (J. Housing Economics 2026); Campbell/Giglio/Pathak (AER 2011)

## Process Report
**Engine:** fan-out Run 1 (7 agents / ~396K tok / 0 err / ~6.4 min): 5 finders (vendor catalog, SFR-REIT metrics, stress-signal, forced-selling, Florida) + 2 adversarial verifiers.
**What worked:** the vendor two-camp taxonomy + the "DSCR is the missing load-bearing metric" insight + the SFR-REIT primary disclosures came back clean; both verifiers converged on refuting the leading-indicator framing.
**Data gaps:** no public STR/second-home mortgage delinquency or DSCR-loan performance (the load-bearing host-solvency series); no ZIP-level STR-density × for-sale-inventory merge (AirDNA ZIP data paywalled); no rigorous cash-flow-negative host-share survey; vendor subscription price points gated.
**Source frustrations:** AirDNA blog + metro pages + ScienceDirect full-text 403'd on WebFetch → metro magnitudes via secondary aggregators (→ BACKLOG: AirDNA primary access / Redfin Data Center ZIP files would upgrade several Medium confidences).
**If I had more time/tools:** a DEWEY primary pull on Redfin Data Center (metro/ZIP inventory+DOM) + FHFA metro HPI would firm the metro distress magnitudes; the DSCR gap is structural (private data).
**This report is the TOOLING deliverable.** The FL carrying-cost transmission (the better-supported housing channel surfaced in Leg E) is being pulled separately as a CORAL-routed memo (re-scoped Run 2).
