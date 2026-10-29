# HOMER — Coverage Map

**The map of what HOMER covers, lane by lane: where the number comes from, how fresh the DATA is, how well the lane is built, and what is missing.** `STATUS.md` is the live dashboard; `registry/THRESHOLDS.tsv` grades the bands; the workbook is the record. This file is the map.

*Built 2026-10-28 (Will-approved, after a comparison with CREED/CORAL coverage maps). Not boot-read. Refresh a lane's row when its state changes, not every session.*

**Status discipline (borrowed from CREED/CORAL):** a lane's colour reflects **data vintage and build quality**, never importance. 🟢 fresh data + ledger + band or criterion · 🟡 partial (data exists; gaps, one source, or no band) · 🔴 thin or blocked · ⏳ in flight.

| # | Lane | Primary sources (basis) | Latest data held (as of 2026-10-28) | Ledger | Build | Gaps / next build |
|---|---|---|---|---|---|---|
| 1 | Residential DQ + FC pipeline | ICE First Look (monthly) · ICE Mortgage Monitor (cures) · MBA NDS (quarterly) | ICE Sept (pub 10/27); MBA Q2; Mortgage Monitor Aug data | `PIPELINE.tsv` | 🟢 | Cure Rates band UNGRADED (ICE stopped printing all-loans YoY); MBA NDS primary is 403-gated |
| 2 | Foreclosure filings / starts / REO | ATTOM monthly, mid-year, quarterly, year-end | Aug monthly (pub 9/17); H1; YE-2025 | `PIPELINE.tsv` | 🔴 | **ATTOM issuer paths 403; Sept/Q3 not yet published at 10/28.** The national STARTS band waits on Q3 |
| 3 | FHA / VA / Ginnie policy | HUD mortgagee letters · Ginnie APM · FHFA | ML 2026-08/-11/-12; EO 10/22; Treasury NPRM 10/22 | `PIPELINE.tsv`, `KB_LIVE.tsv` | 🟡 | No implementation tracker beyond docket rows; FHFA score-pricing change lacks a primary release |
| 4 | Non-bank servicers | SEC 8-Ks/10-Qs · rating agencies | KB-HOMER-033 (last full sweep 9/29); UWM prelim Q3 10/23 | `PIPELINE.tsv`, `KB_LIVE.tsv` | 🟡 | Panel not certified complete (SEC index 403 once); no MSR-mark series; ratings checked ad hoc |
| 5 | MF — GSE books | Fannie Monthly Summary + 10-Q · Freddie MVS | Freddie Sept (MVS 10/26); Fannie Aug monthly; Fannie Q3 10-Q (see sweep 10/28) | `MULTIFAMILY.tsv` | 🟢 | Band defect: mod-suppressible headline — provision pairing only quarterly |
| 6 | MF — CMBS book | Trepp monthly DQ + special servicing (issuer PDF) | Sept DQ 8.04% / SS 8.54% | `MULTIFAMILY.tsv` | 🟢 | No 30-day split by type; Oct print pre-registered (`registry/PREREG_2026-10_TREPP_MF_PRINT.md`) |
| 7 | MF — realized marks + named cases | 10-Qs (ABR, BANC) · vendor studies · WALTER feed | Arbor 10-Q (re-read 10/15); BANC HFS; S2; Blackjack | `MULTIFAMILY.tsv` (aggregates) → **cases go to CREED `cases/CASES.tsv`** | 🟡 | Cases routed to CREED from 10/28; no MF-lender Q3 10-Q pass yet (ABR ~early Nov) |
| 8 | Rents + concessions | Apartment List (band) · Zillow · RealPage | Apartment List Oct (39/100); Zillow Sept; RealPage Sept | `MULTIFAMILY.tsv`, `PRICING.tsv` | 🟢 | Three concession populations — never spliced |
| 9 | Mortgage rates + demand | Freddie PMMS · Treasury par curve / H.15 · MBA apps · MND | PMMS 10/22; MBA wk 10/23 | `RATES.tsv` | 🟢 | Spread is a house convention (weekly vs Wednesday close), not MBS OAS; MBA index level is secondary only |
| 10 | Builders | 8-K Ex 99.1 · NAHB HMI · DHI buydown disclosure | PHM/NVR/MTH/CCS Q3; HMI Oct; DHI buydown tracker FQ2/FQ3 | `BUILDER.tsv` | 🟢 | Cancels/incentives rarely disclosed; DHI cost disclosure degrading; TMHC/TPH no longer SEC reporters |
| 11 | Prices + inventory + sales | Case-Shiller · FMHPI · ICE HPI · NAR · Census · Redfin · Realtor.com | CS Aug; FMHPI Aug; NAR Sept; Census Sept; Redfin 10/18 | `PRICING.tsv` | 🟢 | Revisions every release — carry both vintages |
| 12 | Florida (sub-statewide only) | ATTOM metro rates · MIAMI REALTORS · Zillow/ICE metro | Miami-Dade condo Sept; metro drawdowns Sept; ATTOM metro Aug | `STATE_HSG.tsv` | 🟡 | **Statewide figures are CORAL's.** Metro foreclosure rates wait on ATTOM access |
| 13 | Texas | Trustee-sale auction lists (via TRD/CCN) | Oct postings (secondary) | `STATE_HSG.tsv` | 🔴 | Primary list and October MF subtotal unavailable |
| 14 | Nevada / California | — | none current | — | 🔴 | Charter names NV (Las Vegas fallthrough, CC 90+ DQ) and CA (fire-insurance foreclosure pipeline); no source, row or docket entry. Build or de-scope — owner decision |
| 15 | Wealth effect → HENRY | Case-Shiller real · FMHPI · metro drawdowns | first packet 10/28 | packet + NEXUS row | 🟡 | Edge formalized 10/28; trigger rule in charter |

**Thinnest lanes, in order:** 14 (no coverage at all), 2 (ATTOM access), 13 (Texas primary), 4 (servicer panel completeness).
