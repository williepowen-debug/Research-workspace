# OZK — GEOGRAPHY

State and metro-level risk mapping. OZK is headquartered in Arkansas but its actual loan book is concentrated in gateway cities and Sun Belt markets. The FDIC counts them in the Dallas district, which creates a false clean signal — the real exposure is in the most stressed CRE markets in the country.

---

## File Instructions

### EXPOSURE_MAP.md
Where the loans actually are. State and metro-level breakdown of OZK's RESG book:
- State/metro, estimated exposure ($), % of RESG
- Asset type concentration per market (life sci, office, multifamily, construction)
- Source: 10-K geographic disclosures, FFIEC Call Report, management commentary

**The core insight:** OZK's FDIC home district (Dallas) looks clean at 0.89% nonfarm noncurrent. But OZK barely lends in Dallas. The actual book is in NY (1.57% noncurrent), Atlanta/FL/GA (1.36%), Chicago, and San Diego — all above-average stress markets. Geography is a hidden risk amplifier.

### MARKET_CONDITIONS.md
Living tracker of local CRE conditions in OZK's key markets:
- Vacancy rates (office, life sci, multifamily) by metro
- Cap rate trends
- Notable distressed sales, foreclosures, or tenant departures
- Construction pipeline (new supply hitting already-weak markets)

**Key metros to monitor:**
- **San Diego (Sorrento Mesa)** — life sci vacancy went from <5% to 35%. IQHQ RaDD, Bioterra, Sterling Bay projects all here.
- **Chicago (Lincoln Yards)** — Sterling Bay seized. Life sci corridor dead.
- **New York** — highest 30-89 day pipeline in country (0.41%). Office stress.
- **Florida/Georgia** — already showing up as noncurrent (Atlanta district 1.36%). Construction-heavy.

Update quarterly at minimum, or when major market reports drop (CBRE, JLL, Cushman, CoStar).

### REGULATORY_DISTRICTS.md
FDIC district-level benchmarks and the extend-and-pretend gap analysis:
- District noncurrent rates vs national
- PDNA/NCO gap (deferred loss recognition signal)
- How OZK's home district classification masks true exposure geography

**The PDNA gap is the geographic version of the ACL melting ice cube.** Dallas has the largest gap in the country (1.69pts) — maximum deferred loss recognition. OZK sits inside that district.

---

## Existing Research (Migrate From)

- `../sources/FDIC_QBP_Q4_GEOGRAPHIC_ANALYSIS.md` — District-level benchmarks, PDNA/NCO gaps, OZK vs WAL geographic read-through. Primary source.
- `../sources/FDIC_QBP_Q4_2025.md` — Raw QBP data with geographic tables.
- `../EARNINGS_PREP.md` — RC-N district benchmarks section (NY 1.57%, Atlanta 1.36%, Dallas 0.89%).
- `../THESIS.md` — Noncurrent concentration by loan type (75.2% in nonfarm nonresidential).
- `../raw/llm_outputs/OZK_CONSTRUCTION_MATURITY_V3.md` — Some geographic breakdowns of construction pipeline.

---

## Key Numbers (Baseline Q4 2025)

| Market | OZK Relevance | Nonfarm Nonres NC Rate | PDNA/NCO Gap | Signal |
|--------|--------------|----------------------|-------------|--------|
| New York | Primary origination | 1.57% | 1.16pts | 🔴 Highest pipeline |
| Atlanta (FL/GA) | Major book | 1.36% | 0.85pts | 🔴 Already noncurrent |
| Dallas (HQ) | Minimal actual lending | 0.89% | 1.69pts | 🟡 False clean — max extend-and-pretend |
| Chicago | Sterling Bay, Lincoln Yards | 1.09% | — | 🔴 Seized assets |
| San Diego | Life sci concentration | — | — | 🔴 35% vacancy, IQHQ, Bioterra |
| National avg | Benchmark | 1.30% | 0.94pts | — |

---

*Thesis → `../THESIS.md` | KB → `../workbook/KB.tsv` | Market → `../MARKET/`*
