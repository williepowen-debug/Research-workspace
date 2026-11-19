# WATT — Hoover Dam's summer-2027 capacity loss, sized in power terms

**Written:** 2026-11-19, WATT (Claude Code, Opus 5.5, laptop). **Asked by:** PROME task letter 2026-11-19 10:46 ET ("ADDED TODAY") on AEOLUS's packet `inbox/processed/2026-11-19_from-AEOLUS_hoover-summer-2027-capacity.md` (AEOLUS KB-AEO-281; research `AGENTS/AEOLUS/research/2026-11-19_lake-mead-jan-1-2027-unsigned-agreement.md` §3–4). **Cost:** $0. **Moves:** no score, band, gate, threshold, prediction or charter line.

## The answer

Reclamation's November 24-Month Study takes about **980 MW** of summer peaking capacity out of Hoover for June–August 2027 (about 309 MW available against about 1,290 MW in the same months of 2026). Replacing that capacity at California's own 2027 resource-adequacy benchmark costs roughly **$30–50 million** for three to five summer months (about $60–100 million if summer capacity trades at twice the annual average, which is an assumption); the lost energy is small, about 163 GWh, worth about **$8–11 million** at summer-2026 Palo Verde peak prices. The holders keep paying the fixed **$76.2 million** base charge regardless. Spread over the Western systems that hold it, ~980 MW is about **1% of their combined summer peaks**; the largest single bite is Los Angeles (about 235 MW, about 3.7% of its 6,331 MW summer-2026 peak). **It does not touch WATT's power-price trigger or any WATT row:** every WATT channel is PJM, and Hoover sits in the Western Interconnection, which has no electrical link to PJM's prices. **No investment implication** (handoff below).

## Sizing

| Item | Figure | Source (date) | Status |
|---|---|---|---|
| Hoover capacity, Jun / Jul / Aug 2026 | 1,312.1 / 1,287.9 / 1,275.3 MW (97% units available) | USBR 24-Month Study, Nov 2026, Most Probable, p.17, via AEOLUS (read 11/19) | PRIMARY via AEOLUS; not re-read here |
| Hoover capacity, May–Sep 2027 | 316.6 / 309.3 / 308.0 / 311.4 / 312.6 MW (24% units) | same | same; Reclamation says it blends elevation with unit availability, not separable (AEOLUS §3) |
| **Capacity lost, same months** | Jun −1,002.8, Jul −979.9, Aug −963.9 MW; **mean −982 MW** | computed | ESTABLISHED arithmetic on the study's planning numbers |
| Energy lost, water year 2027 vs 2026 | 2,674.3 → 2,511.6 GWh, **−162.7 GWh (−6.1%)** | same | as above |
| Cross-check: WAPA Desert Southwest (WALC) hydro output, Jul–Aug 2026 | max 1,455 MW, 95th percentile 1,163 MW, mean 465 MW (1,463 hours) | EIA-930 fuel-type data, WALC, WAT, pulled 2026-11-19 (`sources/2026-11-19/eia930-walc-hydro-jul-aug-2026.json`) | ESTABLISHED; WALC hydro also includes Davis and Parker dams, so it bounds Hoover from above |
| Capacity price benchmark | **$10.02/kW-month**, CPUC 2027 forecast RA adder (volume-weighted RA trades for 2027 delivery, Dec 2023–Aug 2026); 2026 final $10.11, 2025 final $11.21 | CPUC Energy Division, "2026 Market Price Benchmarks", Table 1–2 (PDF read 2026-11-19) | ESTABLISHED as an annual average; summer months trade above it (amount not read) |
| **Replacement capacity cost** | 982 MW × $10.02 × 3 months = **$29.5M**; × 5 months = **$49.2M**; at an assumed 2× summer premium **$59–98M** | computed | INFERRED; the premium is an assumption |
| Summer-2026 peak energy price | Palo Verde on-peak day-ahead: Jul $51.27, Aug $69.60/MWh mean (max $100.25); SP15: Jul $36.69, Aug $50.58 | EIA ICE wholesale file `ice_electric-2026.xlsx` (pulled 2026-11-19, delivery through Nov 11) | ESTABLISHED; 2027 forwards not reachable free |
| **Replacement energy cost** | 162.7 GWh × $51–70 = **$8.3–11.3M** | computed | INFERRED (2026 prices applied to 2027) |
| Fixed base charge | $76.2M proposed FY2027 (25.89 mills/kWh); paid by contract share, not output | Federal Register 6/16/2026 via govinfo, via AEOLUS | PRIMARY via AEOLUS. INFERRED: on the study's 2,511.6 GWh the charge works out near 30.3 mills/kWh; WAPA's capacity/energy split not read |

## Who loses it, and where

Shares are AEOLUS's arithmetic on the 2011 Hoover Power Allocation Act schedules A+B (INFERRED by AEOLUS's helper); the balancing-area column is **this desk's general knowledge, not checked at a primary**.

| Holder | Share | Share of ~982 MW | Balancing area of its load (unverified) | Summer-2026 peak of that area (EIA-930) | Bite |
|---|---:|---:|---|---:|---:|
| Los Angeles (LADWP) | 23.9% | ~235 MW | LDWP | 6,331 MW (Sep 10) | ~3.7% |
| Arizona Power Authority | 18.4% | ~181 MW | Arizona (WALC/SRP/APS customers) | SRP 8,987; APS 9,437 MW | small, spread over many small utilities |
| Colorado River Commission of Nevada | 18.4% | ~181 MW | NEVP (NV Energy South) | 9,806 MW (Aug 9) | ~1.8%; NV Energy says Hoover is ~2% of its energy (via AEOLUS) |
| Southern California Edison | 13.5% | ~133 MW | CAISO | 49,959 MW (Sep 10) | ~0.3% |
| MWD (aqueduct pumping) | 12.05% | ~118 MW | CAISO | same | MWD can shift pumping hours; how much is unknown |
| Anaheim, Riverside, Vernon, Pasadena, Glendale, Burbank, Boulder City, Schedule D tribes | 13.75% | ~135 MW | CAISO / LDWP / WALC | — | Boulder City relies on Hoover for ~38% of its power (via AEOLUS) |

Combined non-coincident summer-2026 peaks of CAISO, LDWP, NEVP, APS, SRP and WALC: about 86,400 MW (EIA-930, `sources/2026-11-19/eia930-west-ba-summer2026-peaks.json`); ~982 MW is about 1.1%.

**What replaces it:** INFERRED, the same things that serve the Desert Southwest summer evening peak now: gas peakers and combined-cycle units, imports, and the batteries that have grown fastest in CAISO and Arizona. The capacity has to be contracted (resource adequacy in California, bilateral elsewhere) before summer 2027. Which holder buys what is not public in anything read.

## Does it touch WATT's trigger or rows?

| WATT surface | Touched? | Why |
|---|---|---|
| P1 letter (PJM price) | No | PJM-RTO only; Western Interconnection is electrically separate |
| P2 (PJM capacity), P3 (PJM data-center demand), P4 (PJM spark spread) | No | PJM only |
| WATT-08 to WATT-17 | No | none keys on the West |
| A gas link | Weak, INFERRED | ~1 GW of extra Western gas burn on summer peaks is small next to national summer gas burn; BRENT owns gas |

Logged as `combo:WATT/west-hydro` (KB-WATT-223) with a review date; nothing is scored.

## Established, inferred, unknown

- **ESTABLISHED:** Reclamation's planning numbers; the computed loss; the CPUC capacity benchmark; summer-2026 Western peak prices; Western balancing-area peaks.
- **INFERRED:** replacement costs (2026 prices applied to 2027; summer premium assumed); holders' balancing areas; what replaces the capacity.
- **UNKNOWN:** how much of the loss is elevation versus scheduled unit outages (AEOLUS could not separate them); Desert Southwest summer-2027 forward prices (ICE forwards are paid data); each holder's hedge or contract position; whether a wet Upper Basin winter or an April study review restores some of it.

## Trade-assessment handoff (WQ-696)

**This supports no investment implication I can name.** What the evidence implies: about a gigawatt of summer peaking capacity has to be bought elsewhere in the West for summer 2027, at a cost of tens of millions of dollars spread mostly over public power agencies (LADWP, Arizona Power Authority, Colorado River Commission of Nevada, MWD, small cities) and, for the one listed holder (SCE, owned by Edison International), about 0.3% of its system's peak, which passes through to customers. Horizon: contracting through spring 2027; delivery May–September 2027. What would invalidate it: a December–April study path that keeps Lake Mead above 1,035 ft, or Reclamation showing that much of the loss is maintenance it can reschedule. Unknown: Western summer-2027 forward prices and how much of this they already carry (the study is public). The only market channel is a marginal bid on Desert Southwest summer power and gas, too small against the market and not reachable with a free price, so no packet goes to TERRY.
