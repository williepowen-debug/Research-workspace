# September 2026 CPI read (D:L672 ④) — cells, CRL-10 path, the deferred signals, tariff bases, income offsets

**Written:** 2026-10-14 23:59 ET (`date`), CARL (Claude Code, Opus 5.5, PROME-spawned Tier 1). **Release:** BLS CPI, September 2026, Wed 2026-10-14 08:30 ET. **Recovery:** written by the session that died in the ~03:08 ET 10/15 crash; uncommitted. The recovery session (10/15 08:05–08:10 ET, `date`) re-checked the CPI cells at FRED (CPIAUCSL 336.3, CPILFESL 338.9, SETB01 376.6, SAF11 321.1, CPIUFDNS 350.905), recomputed §2's required path and base rates (identical), applied the two-number rule to the CRL-10 grade, and made the KB-CARL-506 repair this card names.

## 1. Cells, read by CARL at BLS (public API v1, two queries, 2026-10-14 23:49 ET; the HTML release returned 403 to a generic browser User-Agent — no identity sent, gap recorded per MEMORY M85)
| Series (BLS id) | Sep-26 | Aug-26 | Sep-25 | m/m | y/y |
|---|---:|---:|---:|---:|---:|
| All items SA (CUSR0000SA0) | 336.298 | 334.131 | 324.245 | **+0.649%** (published +0.6) | 3.717% |
| All items NSA (CUUR0000SA0) | 336.940 | 334.980 | 324.800 | +0.585% | **3.738%** (published 3.7) |
| Core SA (CUSR0000SA0L1E) | 338.896 | 337.765 | 330.418 | **+0.335%** (published +0.3) | 2.566% |
| Core NSA (CUUR0000SA0L1E) | 339.287 | 338.041 | 330.804 | +0.369% | **2.564%** (published 2.6) |
| Gasoline SA (CUSR0000SETB01) | 376.558 | 345.169 | 280.658 | **+9.094%** | 34.170% |
| Energy NSA (CUUR0000SA0E) | 341.573 | 329.351 | 283.589 | +3.711% | 20.446% |
| **Food NSA (CUUR0000SAF1) — CRL-10's series** | **350.905** | 350.418 | 342.405 | +0.139% | **2.482%** |
| Food SA (CUSR0000SAF1) | 350.477 | 350.309 | 342.086 | +0.048% | 2.453% |
| Food at home SA (CUSR0000SAF11) | 321.111 | 321.335 | 315.540 | **−0.070%** | 1.766% |
| Food away NSA (CUUR0000SEFV) | 398.783 | 397.868 | 385.451 | +0.230% | 3.459% |
| Beef & veal NSA (CUUR0000SEFC) | 512.606 | 519.096 | 495.239 | −1.250% | 3.507% |
| Coffee NSA (CUUR0000SEFP01) | 299.101 | 297.231 | 279.280 | +0.629% | 7.097% |
| Shelter SA (CUSR0000SAH1) | 431.908 | 430.227 | 418.422 | +0.391% | 3.223% |
| Used cars & trucks SA (CUSR0000SETA02) | 182.176 | 180.965 | 184.869 | +0.669% | −1.457% |
| Real avg hourly earnings, all employees (CES0500000013) | 11.24 | 11.30 | 11.32 | **−0.531%** | **−0.707%** |
| Real avg weekly earnings (CES0500000012) | 386.76 | 388.75 | 387.10 | −0.512% | −0.088% |
| Nominal AHE (CES0500000003) | 37.81 | 37.76 | 36.70 | +0.132% | +3.025% |
Core 3-month annualized on index levels (Jun→Sep): 3.412% (RED's Table-A 1dp basis gives 3.247216%; RED owns FT-08). "Gasoline was over half the monthly headline increase" is BLS release text relayed by WALTER; CARL could not read the HTML release (403) and did not reconstruct the relative-importance weight, so it is carried as **relayed, not verified**.

**Read:** the September squeeze is energy at the pump. Headline +0.65% with gasoline +9.1%; core +0.34% through non-energy items (shelter +0.39, used cars +0.67); food FLAT (SA +0.05%, food-at-home −0.07%). Real hourly pay fell −0.53% in the month and is −0.71% y/y, the household cost squeeze in one number. ⚠️ Shared antecedent: real earnings are nominal pay deflated by this same headline CPI — one datum, not a second consumer signal (NEXUS §2). **COR-20261014-23 (WALTER SIG-W-20261014-023, RED b79c04c9a):** the pump pass-through reached HEADLINE, not core — RED graded CHG-028's September oil-to-core leg NOT MET (airline fares +1.159% vs ≥2.35% bar; a conjunction), and FT-08 FIRED on core 3.247216% annualized (Table A basis). This card already read core as non-energy-driven; CARL carries no `pump_pass_through`-to-core claim.

## 2. CRL-10 (food CPI YoY > 4.0%, Q4 2026) — reachability re-grade 8% → 1% (two-number rule; first draft said 3%)
| Item | Value |
|---|---|
| September food NSA y/y | **2.482%**, third straight decline (3.01 Jun → 2.98 Jul → 2.67 Aug → 2.48 Sep) |
| October 2026 y/y | NOT COMPUTABLE (October 2025 never published — CUUR0000SAF1 and CUUR0000SA0 both lack 2025-M10 at BLS; unchanged) |
| November bar | base Nov-25 341.721 × 1.04 = 355.390 ⇒ needs **+0.637%/mo** compounded Oct–Nov from 350.905 |
| December bar | base Dec-25 343.795 × 1.04 = 357.547 ⇒ needs **+0.627%/mo** compounded Oct–Dec |
| Trailing NSA run rate | +0.112%/mo (3 mo) · +0.197 (6 mo) · +0.205 (12 mo) ⇒ the bar needs ~5.7× the 3-month pace |
| Seasonal norm (2015–24 mean NSA m/m) | Oct +0.303 · Nov −0.057 · Dec +0.185 ⇒ ~+0.12 to +0.14%/mo over the window |
| Unconditional base rate since 1995 (FRED CPIUFDNS, 399 months) | 2-month windows averaging ≥ +0.637%/mo: **19 of 376 = 5.1%**; 3-month ≥ +0.627%/mo: **21 of 374 = 5.6%**; every recent hit is 2022 |
| Cold base rate (recovery session, 2026-10-15 08:09 ET `date`; computed from the base rate alone, not as a move from 8%) | 2-month windows averaging ≥ +0.637%/mo **when the trailing 3-month pace was ≤ +0.2%/mo** (today +0.112): **2 of 182 = 1.1%**; 3-month ≥ +0.627%/mo on the same condition: **2 of 181 = 1.1%** (FRED CPIUFDNS 1995→, consecutive months only) |
| Decision | **8% → 1%**. Written twice per `FORGE/PREDICTION_DISCIPLINE.md` `finding_corrective_inherits_the_anchor_it_corrects`: as a move from the standing 8% the first draft (23:59 ET 10/14, crashed session) said **3%**; cold from the conditional base rate it is **1.1%**. They disagree 2.7× (> ~2×), so the cold number governs and both are recorded; score the 9/11 (8%) and 10/15 (1%) correctives as their own rows at resolution. The cold sample is not conditioned on a fuel shock (diesel +$2.51 y/y) — the one reason it could understate — but September food was flat (SA +0.05%) with that shock already in place. Forced by the BLS September food cell (350.905), the task's own evidence. Mechanism NOT killed (El Niño, diesel freight, beef/coffee sub-channels remain upside tails that act on later prints); this is threshold distance and clock, per `finding_threshold_vs_mechanism`. A CUT, so not the CRL-01/CRL-19 too-aggressive shape. No position is linked to CRL-10. |

## 3. The deferred signals folded here (all were deferred to "the 10/14 CPI read")
**The nine headline-level rows from the 10/10 drain, now read in full at BOARD:**
| Signal | What it says (full read) | Fold |
|---|---|---|
| SIG-W-20261004-003 | WSJ trucking feature; no number | Freight-demand narrative; September food SA +0.05% shows no freight-to-food pass-through yet. No CRL-10 move |
| SIG-W-20261007-003 | EIA Oct STEO: Q4 Brent $105 forecast; East Coast distillate −32% vs 5-yr | Forecast, BRENT owns; diesel tail acts on later food prints |
| SIG-W-20261007-005 | World Bank Pink Sheet: phosphate rock $170 flat; DAP $800.6, urea $407.5 | Fertilizer input flat-to-mixed; no near-term food push. FERT owns. Potash triage-only, untouched |
| SIG-W-20261008-001 | Isaias landfall forecast; 25% Gulf oil shut in (10/7) | Supply shock is fuel, not food, on a 2–3 week lag; FL Panhandle consumer read is CORAL/AEOLUS's insurance channel — no CARL-owned FL metric moved on a forecast |
| SIG-W-20261008-015 | IEA accelerates ~100 mb (no new volume); Cardón fire | BRENT owns; no CRL-10 move |
| SIG-W-20261008-019 | Isaias Cat-2 forecast; FL insurer exposure floor (Citizens 8,882 policies) | As -001; CORAL owns FL exposure |
| SIG-W-20261008-027 | CPC: strong-to-very-strong El Niño through JFM-2027 (>83%); +2.1 = monthly RELATIVE index (corrected 10/10) | The named CRL-10 upside tail; acts on 2027 prints, not the Nov/Dec window at the needed size |
| SIG-W-20261008-035 | Gulf shut-ins 62.89% (1.28 mb/d) 10/8 | Fuel; BRENT owns |
| SIG-W-20261008-042 | Dallas Fed: global refining −up to 10% (6–8 mb/d); pump stays high vs crude | Pump-price persistence supports the energy-squeeze read (V5), not CRL-10 |
**Earlier rows deferred to this read (fully read when logged 10/01–10/10):** SIG-W-20260819-002 · -20260910-020 · -20260914-015 · -20260929-002 (cattle slaughter; beef CPI fell −1.25% m/m in September) · -20260930-006 · -20261001-015 · -20261001-026 · -20261002-002 · -20261002-009 · -20261008-009. All bear on CRL-10 only through diesel→freight→food or a single-day beef shock; September's flat food print folds them: no CRL-10 support beyond the tails above.

## 4. Tariff evidence — the two bases kept separate (SIG-W-20261014-036 / COR-20261014-36)
NY Fed Liberty Street, 2026-10-06, read by CARL at the publisher 2026-10-14 23:5x ET (verbatim): *"The contribution of tariffs peaked in February 2026, at 2.9 percentage points, and is forecast to fall to around zero by August 2026. It then turns negative as the large tariff increases of 2025 drop out of the twelve-month comparison, before turning slightly positive by mid-2027 as the Canadian tariffs pass through. Taken together, the two panels show that tariffs have left consumer goods price levels higher, while their effect on inflation fades."*
| Basis | Model path | CARL use |
|---|---|---|
| **12-month (y/y) goods inflation** | ~0 by Aug-2026 → **NEGATIVE from ~Aug-2026 until mid-2027** → slightly positive by mid-2027 | y/y counter-evidence to tariff-driven inflation acceleration through the Q4 window (incl. CRL-10's) |
| **Price LEVEL** | ~2% higher and edging UP after August (≈half enacted Aug-2026 Canadian tariffs, rest the announced Jan-2027 Canadian autos) | the household squeeze: a persistent, slowly rising level burden, no longer accelerating |
| m/m or 3-month annualized | neither panel directly | not graded from this study |
Perimeter: non-oil consumer goods, services excluded, end-September tariffs held fixed apart from the announced auto step, ~25% pass-through; a research counterfactual, not all-CPI attribution. RED's verdict (10/14) agrees: ADOPT for y/y, ATTACK "spent" for the level. KB-CARL-506 repaired.

## 5. Income offsets and other dated items
- **SSA 2027 COLA 3.6%** (SIG-W-20261014-008): CARL recomputed from BLS CPI-W (CWUR0000SA0) Q3 averages 328.746 / 317.265 = **+3.619%** → 3.6%. Effective with January 2027 Social Security payments (SSI December 31, 2026, per the SSA announcement relayed by WALTER; ssa.gov returned 403 to CARL). Nominal, delayed; it offsets the real-income squeeze for beneficiaries only, from January.
- **NFIB September** (PROME compound-stress evidence; CARL re-read the primary PDF): Optimism 97.9 (−0.8, below the 52-yr 98.0); earnings net −20% (−1); sales net −8% (+1); short-maturity loan rate **8.2% (+0.7pp)**; last loan harder net 3% (unchanged); borrowing regularly 22% (−3); n = 411 usable of 5,000 (membership sample, not a census). ⚠️ The report's response rate is also 8.2% — a coincidence; the loan-rate cell is read from the Credit Conditions text.
- **Diesel** (SIG-W-20261014-014): EIA on-highway 10/12 $6.179 (−$0.020 w/w, +$2.514 y/y); FedEx ground surcharge 28.75% (10/12–18) vs 29.25% — relief at the margin, expensive level.
