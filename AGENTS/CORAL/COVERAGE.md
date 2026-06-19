# CORAL — Florida Coverage Map

**The master index of the 10 Florida pillars CORAL owns.** Per-pillar: what it covers, the key metrics/owner docs, current live read, and data freshness. This is the structural skeleton — STATUS.md is the live dashboard, this is the map of the territory. Update the "Live read" + "As of" each time a pillar moves.

*Last refreshed: 2026-06-19 (comprehensive-scope build-out + full 10-pillar research sweep synthesized — `research/SWEEP_2026-06-19.md`).*

**Maturity legend:** 🟢 well-covered (fresh data + workbook) · 🟡 partial (some data, gaps) · 🔴 thin/stub (needs build-out) · ⏳ research in flight

---

| # | Pillar | Scope | Key metrics / owner docs | Live read (as of) | Maturity |
|---|--------|-------|--------------------------|-------------------|----------|
| 1 | **Condo crisis** | SIRS (SB 4-D/HB 913), reserve gaps, assessments, blacklist, receivership, terminations | KB ML-CORAL-010; VX blacklist/assoc-distress; `research/`; *Biscayne 21* | Reserve mandate live 1/1/26; assessments $25K-$400K/unit; blacklist 1,400+; Biscayne 21 termination test (6/19) | 🟢 |
| 2 | **Housing — single-family** | Statewide+metro price, inventory mo, DOM, price cuts, FL metros leading US correction | `research/SWEEP_2026-06-19.md` P2; FL Realtors | SF median $420K (+1.8%); 4.7mo supply; correction **Gulf-Coast-concentrated** (Cape Coral −10%, North Port; Tampa SF +2.5%); 43% of listings cut; FL Realtors flags "inflection point" | 🟢 |
| 3 | **Housing — condo/townhouse** | Inventory, vintage vs luxury price, foreclosure by metro | KB ML-CORAL-009; `research/REFRESH_2026-06-19.md` | 8.9mo statewide; Miami-Dade 12.9 / Broward 11.0 / PB 8.2; price −6.1% YoY, 92% of mkts down (Apr 2026) | 🟢 |
| 4 | **Commercial real estate** | FL office/retail/industrial vacancy + repricing; multifamily occ/rent/transactions | `research/SWEEP_2026-06-19.md` P4; CREED natl | **CRE distress is condo/residential-specific, NOT commercial-wide:** Miami office 12.5% (tightest in US); retail ~4.1%/industrial mostly healthy (Miami industrial softening) | 🟢 |
| 5 | **Insurance** | Citizens count/assessment/depop, OIR carriers, premiums, reinsurance, tort reform | KB ML-CORAL-013; VX-CORAL-INS-02 | Citizens 294K (−64% YoY, May); 8.7-8.8% rate cut 6/1; reinsurance −15-20%; litigation −35%, 17 new carriers; premium $7.1K (+181% vs natl) but falling. **Channel EASING** | 🟢 |
| 6 | **FL banks** | Watchlist (SSB/SBCF/BKU/VLY-FL/AMTB/USCB/BAFN), capital/NCO/NPL/CRE conc → REGINALD | **`FL_BANK_WATCHLIST.md`**; KB ML-CORAL-011/012/018 | Q1 2026: none breaking on credit (NCOs 9-14bps). New stress: AMTB (ACL 46% of NPLs), BAFN (loss+dilution). USCB = condo-assoc canary (clean now). SSB short retired | 🟢 |
| 7 | **Migration & demographics** | Net domestic+intl migration, Census components, metro flows, out-migration drivers | KB ML-CORAL-002/015; `research/SWEEP_2026-06-19.md` P7 | Net domestic +22,517 (−93%, now #8); intl +178,674 but −57% YoY & −75% projected; **natural change NEGATIVE**; out-migration ~510K to GA/TX/NC | 🟢 |
| 8 | **Tourism & snowbird** | Visitor volume, Canadian/intl arrivals, Orlando/TDT, hotel occ/ADR, L&H jobs | KB ML-CORAL-016; `research/SWEEP_2026-06-19.md` P8 (reconcile w/ MARCO) | 143.3M 2025 record but Q1'26 −1.0%; **Canadian −12.1%** (capacity deleted, SW FL hit); overseas +8.5% (record) offsets; Epic Universe + TDT $384.6M record | 🟢 |
| 9 | **State fiscal & policy** | Property-tax reform (Nov-2026 ballot), budget+sales tax, condo legislation, insurance law | KB ML-CORAL-017; `research/SWEEP_2026-06-19.md` P9 | **🔴 Property-tax amendment on Nov-3-2026 ballot** (homestead $50K→$250K; −$8.4B local rev); budget deficits FY28-29 −$8.1B; condo HB913 relief valves (loans/2yr pause) | 🟢 |
| 10 | **Coastal & climate** | Hurricane season, sargassum, flood/SLR → coastal RE + insurance tax | VX-CORAL-SARG-01; `sources/Sargassum_2026_FL_Briefing.md` | 2026 hurricane ~avg (CSU 14/7/3); sargassum record-tier belt, SE FL "high" (6/19) | 🟢 |

---

## Cross-pillar convergence (the CORAL edge)

The point of owning all ten is seeing them **stack on the same geography**. Live examples:
- **SE FL Atlantic coast (Miami-Dade/Broward/PB/Keys)** carries the deepest condo inventory (pillar 3) + sargassum amenity tax (pillar 10) + the FL bank books exposed to it (pillar 6) — all at once.
- **The household cash drain** = special assessments (pillar 1) + insurance cost (pillar 5) + property tax (pillar 9) stacking on the same owner → forced selling (pillars 2/3) → out-migration (pillar 7) → demand hole that loops back to housing.
- **Tourism (pillar 8)** + **migration (pillar 7)** are the demand engine; when both soften, the whole real-estate + bank stack (pillars 2-6) loses its tailwind.

## Build-out backlog (priority order)
1. ✅ DONE 6/19 — Pillars 7/8/9 synthesized from the research sweep; Pillar 6 expanded into `FL_BANK_WATCHLIST.md`; Pillar 2 stood up.
2. **Per-metro convergence view** (Miami / Tampa / Orlando / Jax / SW FL) — pull pillars 2/3/4/7/8 into a single metro-by-metro grid. The SW-FL Gulf Coast (Cape Coral/Naples/North Port) is the clearest convergence cluster (snowbird loss + SF correction + migration). Next build.
3. Workbook deepening — give pillars 7/8/9 their own VX vectors with thresholds (currently in KB + SWEEP only).
4. Q2 2026 earnings re-test (~late Jul) — the bank-leg canaries (USCB condo-assoc, AMTB ACL coverage).
5. Nov 3 2026 — property-tax amendment vote (pillar 9) outcome + market reaction.
