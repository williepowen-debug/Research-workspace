# South Florida → FL-Bank Loss-Transmission: Timing & Leading-Indicator Set

**Date:** 2026-06-21 | **Mode:** Thesis | **Confidence:** Medium
**Brief:** WALTER Prompt A (`DEWEY_PROMPT_A_fl-bank-transmission.md`); deepens the open question left by SIG-W-20260619-008 (S-FL bank-P&L transmission *timing*, not whether the consumer is stressed — that is treated as settled).
**Provenance note:** Reconstructed after a session crash. ~70% of the source-gathering (two academic papers; AMTB/SBCF/BKU Q1'26 financials) was salvaged from the interrupted `/deep-research` workflow scratch; the leading-indicator dashboard, Citizens trajectory, BankUnited exposure, and this synthesis were re-run 2026-06-21. Recovered raw evidence archived in `output/_recovered_2026-06-21_promptA/`.

---

## Key Finding

The ~**winter 2026-27** working call for *acute* FL-bank credit stress is **broadly defensible for the charge-off/reserve-build stage, but the leading edge (rising 30-89 day past-dues) should surface earlier — H2 2026 — and is arguably already flickering** at the two most FL-concentrated names. The transmission runs **insurance/condo cost-shock → household liquidity strain → mortgage & consumer delinquency (~12-month lag from the premium reset) → migration through delinquency buckets → net charge-offs (a further ~2-4 quarters)** [ACADEMIC]. Because the condo-specific cost shock (Citizens commercial/condo-master rate hikes + SB-4-D reserve assessments) is landing *now* (2025-2026), the ~12-month delinquency lag points to deterioration becoming visible **late-2026 into 2027**, with bank charge-offs trailing into 2027. The three highest-signal leading indicators and their current readings:

1. **30-89 day past-dues at FL-concentrated banks** — *already rising YoY*: Seacoast (SBCF) early delinquencies $17.2M → $28.2M YoY; Amerant (AMTB) NPAs 1.38% → 1.93% of assets YoY [PRIMARY-derived].
2. **FL foreclosure starts** — Florida is the **#1 state foreclosure rate** (May 2026); U.S. starts **+12% YoY** (Apr 2026). The front of the pipeline is filling [PRIMARY: ATTOM].
3. **Citizens commercial/condo-master rate trajectory + Miami-Dade condo months-of-supply (~13)** — the insurance/condo channel that *leads* household stress by ~12 months, and it is diverging *worse* even as personal lines heal [PRIMARY: Citizens; NEWS: Insurance Journal].

---

## Evidence

### Transmission-mechanism map (with measured lags)

**Stage 1 — Cost shock to households (landing now).** South Florida condo owners face two simultaneous cost shocks: (a) condo-association **master-policy** premiums and (b) **SB-4-D** milestone-inspection / reserve-funding assessments ($5K-$200K per unit, ranges [UNVERIFIED] law-firm/realtor sources). Citizens' HO-6 (condo-unit) premiums in Miami-Dade rose **~40% over four years vs ~26% CPI** [ACADEMIC: FIU Metro Center via WLRN, end-2024].

**Stage 2 — Cost shock to delinquency (~12-month lag).** The cleanest causal evidence: a Fed/academic study (building on Keys & Mulder 2024) finds **rising home-insurance premiums raise the probability of mortgage delinquency within 12 months of policy renewal, and the effect grows as more time passes since renewal** (Figure 3) [ACADEMIC: insurance-premium/delinquency working paper, ICE McDash data]. A standard-deviation premium increase is associated with **~149,000 additional delinquent mortgages nationally within 12 months**; the same shock raises **credit-card delinquency, credit utilization, and lowers risk scores** — the household-liquidity channel. This is the load-bearing lag estimate: **insurance shock → ~12 months → mortgage delinquency.**

**Stage 3 — Delinquency to charge-off (further ~2-4 quarters).** Mortgage loans migrate through discrete buckets — **current → 30-59 → 60-89 → 90-120 → default (120+ dpd)** — modeled as a Markov transition process [ACADEMIC: OCC, *Estimating Conditional Mortgage Delinquency Transition Matrices*, Chen, single-family 2004-2013]. The paper's practical forecast horizon is **24 months**, and crucially, **up-migration probabilities (to higher delinquency states) rise sharply during stress periods** vs benign periods — i.e., the cascade both lengthens and steepens once stress begins. Banks recognize the loss at the charge-off end of this chain, structurally *lagging* the 30-89 day tripwire by several quarters.

**Net timeline:** cost shock (now) + ~12mo to delinquency (→ H2 2026 / early 2027) + ~2-4 quarters delinquency→NCO (→ 2027) ⇒ **charge-offs concentrated in 2027; early-delinquency tripwires in H2 2026.** This is consistent with — and if anything slightly later than — the ~winter 2026-27 working call for the *acute* phase, while validating that the *leading edge* is a 2026 event.

### FL-bank exposure & credit table (Q1 2026, period ending 3/31/2026)

| Bank | FL / S-FL concentration | 30-89d / early delinq. trend | NPA / NPL trend | NCO (ann.) | Provision | ACL coverage |
|---|---|---|---|---|---|---|
| **AMTB** (Miami HQ; most S-FL-pure) | Core = S/Central FL + Tampa, Houston, NYC; **geo % not disclosed in PR** | 90+ accruing $2.3M (yr-ago $1.0M) — **up YoY** | **NPA 1.93% of assets, up from 1.38% yr-ago** | 0.45% (yr-ago 0.22%) | $7.8M | ACL/NPL **~45% — thin & slipping** |
| **BKU** (Miami Lakes HQ) | **CRE $6.9B, 47% FL** (~$3.2B); 22% multifamily; largest FL-CRE notional of the three | not disclosed | **NPL −26% YoY (improving)** | $36M elevated — **C&I, not FL RE** | ~$24.6M / ~$25M | ACL/NPL **75.9%, up from 59.0%** |
| **SBCF** (Stuart FL HQ) | Primary market FL; **CRE non-owner-occ 224% of RBC** (>100% supervisory flag) | **$28.2M, up from $17.2M yr-ago** | NPL 0.75%, up from 0.57% QoQ / 0.68% yr-ago | 0.11% | $0.8M | ACL/loans 1.39% |

*SBCF also: NIM 3.83%, $39.5M AFS-securities repositioning loss, ~7% annualized organic deposit growth [PRIMARY-derived, confirmed].*
*Other heavy S-FL exposure (private, no public 10-Q): **City National Bank of Florida** — 3,600+ community-association/HOA relationships, active Miami luxury-condo construction lending [INSTITUTIONAL]. Ocean Bank, Banesco USA — S-FL CRE-heavy, no public concentration datapoint (would need FFIEC call reports).*

> **⚠️ Attribution flag:** The `provision $24.6M / ACL-NPL 75.9% (up from 59.0%) / CET1 12.2%` block recovered from the crashed session is **most consistent with BankUnited (BKU), not Amerant** — the prior session appears to have misattributed it to AMTB. BKU's full-year provision guide (~$68M), the NPL-coverage jump, and the C&I-driven loss narrative all fit BKU. **This needs the Q1'26 10-Q to confirm** (SEC.gov WebFetch 403'd; figures are [PRIMARY-derived, INSTITUTIONAL-mirror], not read off EDGAR). Do not propagate the AMTB attribution.

### Leading-indicator dashboard (as-of mid-June 2026)

| Indicator | Current reading | Trend | As-of | Source |
|---|---|---|---|---|
| FL state foreclosure rate (rank) | **#1 worst**, 1 in 2,110 units | worsened from #3 in April | May 2026 | [PRIMARY] ATTOM |
| U.S. foreclosure starts | 28,414 | **+12% YoY** | Apr 2026 | [PRIMARY] ATTOM |
| U.S. foreclosure filings (Q1) | 118,727 | **+26% YoY** | Q1 2026 | [PRIMARY] ATTOM |
| Miami-Dade **condo** months-supply | ~13.2-13.7 mo | deep buyer's market | late-2025/2026 | [NEWS/INSTITUTIONAL] Redfin-derived |
| FL statewide condo/TH months-supply | 8.9 mo | active inventory ↓ YoY | Apr 2026 | [PRIMARY] FL Realtors |
| Miami-Dade condo median price | <$400K | **~ −10% YoY** | Nov 2025 | [NEWS] Redfin |
| FL single-family median price | $420,000 | +1.8% YoY | Apr 2026 | [PRIMARY] FL Realtors |
| FL mortgage-delinquency change | **+99 bps QoQ** (among largest of any state) | worsening | Q4 2025 | [PRIMARY] MBA NDS |
| Citizens policies in force | ~385K (down ~73% from ~1.42M Oct-2023 peak) | depopulating (personal lines healing) | end-2025 | [PRIMARY] Citizens |
| Citizens **personal**-lines 2026 rate | **−2.6%** avg (first cut in years) | easing | eff Jun 2026 | [PRIMARY] Citizens |
| Citizens **commercial/condo-master** 2026 rate | **+10.4%** avg ("below actuarially sound") | **worsening / diverging** | eff late 2026 | [NEWS] Insurance Journal |

**Reading the dashboard:** the *statewide* blends look benign (single-family +1.8%, statewide condo 8.9mo, personal-lines insurance easing) — a textbook **blended-index masking a tail**. Decomposed, the **Miami-Dade condo sub-segment** (~13mo supply, −10% price, master-policy + SB-4-D cost shock) and the **commercial/condo-master insurance channel** are the live stress vectors, and they are the ones that *lead* bank losses.

---

## The two-sided case

**Steelman: transmission is faster / sooner than winter 2026-27.** FL is already the #1 foreclosure state with starts +12% YoY; FL delinquency posted one of the largest state increases in the country (+99bps QoQ, Q4'25); AMTB NPAs and SBCF 30-89d past-dues are *already* rising YoY; the condo cost shock is acute and concentrated, not diffuse. If the ~12-month insurance→delinquency lag is even slightly compressed by the simultaneity of SB-4-D assessments, the early-delinquency signal could be unambiguous by **late 2026**. *Single datapoint that would most move me toward this:* two consecutive quarters of rising **30-89 day past-dues** specifically in FL residential/condo books at AMTB **and** SBCF (not C&I).

**Steelman: it normalizes without a bank-loss event (~70% base).** The visible bank deterioration today is **idiosyncratic, not FL-real-estate-systemic**: BKU's elevated losses are **C&I**, BKU's NPLs actually *fell 26% YoY* with coverage rising to 76%, SBCF's realized NCOs are negligible (0.11%), and the personal-lines insurance market is genuinely healing (Citizens depopulating, 17-18 new carriers, reinsurance softening). Structural backstops — reserve cushions, deposit stickiness, "extend-and-pretend" on CRE, and the rate-cut tailwind to borrowers — can absorb a lot before losses crystallize. *Single datapoint that would most move me toward this:* FL foreclosure starts rolling over **and** Miami-Dade condo months-supply normalizing back toward statewide (~6-8mo) over the next two quarters.

---

## Counter-Evidence & Falsification List

- **The strongest counter to the whole thesis:** the loss that is *actually* elevated right now (BKU, $36M) is **C&I, not FL condo/CRE** — i.e., the visible stress is not (yet) the thesis mechanism. If FL-RE charge-offs stay near zero through 2026 while only C&I moves, the transmission story is unconfirmed.
- **Blended statewide data is benign** — only the Miami-Dade condo decomposition flashes. If the tail does not widen the blend over the next 2 quarters, the "tail" read is wrong.
- **The ~12-month lag is estimated on a national 2022-23 insurance sample**, not FL-condo-master specifically; the analog may not transfer cleanly (the academic sample is single-family mortgages, not condo-association master policies). [ACADEMIC, external-validity caveat]
- **Falsifiers (would push the call later / kill it):** (1) FL foreclosure starts roll over YoY for 2 quarters; (2) AMTB NPAs stabilize/decline next print; (3) SBCF 30-89d past-dues revert toward year-ago; (4) Citizens *commercial* rate trajectory flattens. **Confirmers (would pull it forward):** rising 30-89d past-dues in FL *residential/condo* books at ≥2 of the FL-concentrated banks for 2 consecutive quarters; Citizens commercial/condo-master rates rising again into 2027.

---

## Source Quality Assessment

Mixed-strong. The **lag structure** rests on two solid [ACADEMIC] sources (an insurance-premium→delinquency working paper on ICE McDash data; an OCC transition-matrix paper) — but both are external analogs (national, single-family, 2004-2023), not FL-condo-specific, so the *mechanism* is well-evidenced while the *exact FL-condo lag* is inferred. The **leading indicators** are largely [PRIMARY] (ATTOM, FL Realtors, MBA, Citizens), with the load-bearing Miami-Dade condo months-supply only [NEWS/Redfin-derived]. The **bank financials** are [PRIMARY-derived but INSTITUTIONAL-mirror] — SEC.gov 403'd, so the 10-Q geographic-concentration notes were **not read directly**; the AMTB-vs-BKU attribution and the FL loan-% for AMTB/SBCF are the weakest links. Two-source verification holds for the foreclosure, insurance-split, and SBCF figures.

## References (accessed 2026-06-21)

- ATTOM — U.S. Foreclosure Market Report (Apr/May 2026; FL #1 state, starts +12% YoY) [PRIMARY]
- Florida Realtors Research — Monthly Market Detail, Apr 2026 (condo 8.9mo, SF $420K/+1.8%/44 DOM) [PRIMARY]
- MBA — National Delinquency Survey (Q4 2025 / Q1 2026; FL +99bps) [PRIMARY]
- Citizens Property Insurance Corp. — citizensfla.com (policy count ~385K; personal-lines −2.6%; depopulation >546K in 2025) [PRIMARY]
- Insurance Journal — Citizens commercial-lines +10.4% (Dec 11 2025) [NEWS]
- FIU Metro Center via WLRN — Miami-Dade HO-6 premiums +~40% / 4yr (end-2024) [ACADEMIC]
- Insurance-premium → mortgage-delinquency working paper (ICE McDash; ~149K delinquencies/12mo; Figure 3 dynamic response) [ACADEMIC] — *recovered, full citation/authors to be re-pinned*
- OCC — *Estimating Conditional Mortgage Delinquency Transition Matrices*, Q. Chen et al. (six-state Markov; 24-mo horizon) [ACADEMIC] — *recovered*
- AMTB / BKU / SBCF Q1 2026 earnings releases & 8-K exhibits (via institutional mirrors; EDGAR direct 403'd) [PRIMARY-derived]
- City National Bank of Florida — citynational.com; Commercial Observer (Apr 2026) [INSTITUTIONAL/NEWS]

---

## Process Report

**Searches run:** 3 parallel gap-fill research agents (FL-bank financials; FL foreclosure/housing indicators; Citizens/insurance trajectory), ~38 tool-uses total, all WebSearch/WebFetch functional. Plus salvage of the crashed session's `/deep-research` workflow scratch (2 academic papers + AMTB/SBCF/BKU raw filings).
**Data gaps:** (1) FL/S-FL loan **%** for AMTB and SBCF — not disclosed in press releases, needs the 10-Q MD&A concentration note. (2) Metro-level (Miami/Ft-Lauderdale/WPB) foreclosure rates — only state-level sourced. (3) FL-specific Q1'26 delinquency *level* (only the Q4'25 change). (4) Condo-association delinquency rates & condo-master (vs HO-6 unit) premium % — no primary. (5) SB-4-D reserve-deadline compliance counts — only [UNVERIFIED] secondary.
**Source frustrations:** **SEC.gov EDGAR consistently returned HTTP 403 to WebFetch** — the single biggest limiter; all bank credit figures are institutional-mirror grade and the 10-Q geographic notes are unread. FL Realtors and OIR rate-filing PDFs returned as unparseable binary (the load-bearing commercial-condo "+18.8% uncapped" figure lives in one of these and could NOT be re-confirmed this run; only the +10.4% capped figure is confirmed).
**Confidence in findings:** Medium. The *mechanism and direction* are well-supported; the *precise timing* is inferred from external-analog lags; the *bank-attribution* (BKU vs AMTB) needs 10-Q confirmation.
**If I had more time/tools:** an EDGAR full-text-search / API path (not WebFetch) to read the Q1'26 10-Q concentration notes directly; a PDF-text extractor run on the FL OIR rate filing and FL Realtors condo report; the Redfin Data Center CSV for Miami-Dade condo months-supply; the MBA state-by-state Q1'26 table for the current FL delinquency level.
**Suggestions:** Add an **EDGAR API helper** to `scripts/` (WebFetch is blocked by SEC's 403) — this is a recurring blocker for any bank-filing research. Add a small **PDF-to-text** wrapper for FL OIR / FL Realtors PDFs. Both would have closed 3 of the 5 gaps above.
