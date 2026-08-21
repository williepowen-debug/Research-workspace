# MARCO STATUS — session 21 block (8/11-8/12), archived 2026-08-21

## 8/11 UPDATE (session 21) — READ FIRST

> ### 🔴 THE SDL-01 COUNT TELL BROKE ON THE LETTER — AND THE STACK SAYS IT DIDN'T
> **Banxico June (CE81 primary, pulled 8/11, 10 days late to MARCO).** SCRATCH s20 pre-registered the grading rule in writing: *"transfer COUNT YoY is the cleanest surviving SDL-01 proxy (May −1.7%; **positive = the tell breaks**)."*
>
> | Jun 2026 | Value | YoY | **2-yr stack (vs Jun'24)** |
> |---|---|---|---|
> | Remittance value | $5,471.8M | **+4.15%** | **−12.11%** |
> | **Transfer count** | **12,972.0k** | **+0.35%** ← breaks the tell | **−12.96%** |
> | Avg transfer | $422 | +3.94% | — |
>
> **Graded as written: the tell BROKE.** June is the **first positive count-YoY in 15 months**, ending a 14-month negative run (Apr'25–May'26). I am not re-deriving a rule after seeing the number.
>
> **And the spec was defective — recorded as a STATUS problem, not a confidence dodge.** Jun'25 was itself **the worst month in the series (−13.27%)**, so the flip is a base effect. On the 2-yr stack the count reads **−12.96% — the deepest of 2026** (Jan −0.26 / Feb −1.25 / Mar +1.12 / Apr −8.60 / May −6.22 / **Jun −12.96**). The stack is **deteriorating while the YoY flips positive.** H1-2026 count −1.83% YoY, **−5.06% on the 2-yr stack**.
>
> ⚠️ **The defect is MARCO's, and it is asymmetric rigor on MARCO's own instruments.** TOUR-01 is framed on a 2-yr stack *specifically because* "the April recovery was base-effect" — MARCO wrote that lesson for Canadian travel and then wrote the remittance tell on bare YoY with **no sustain window and no base guard**. Same failure, different corridor. **The re-spec below is post-hoc and cannot be scored as a confirm.**
> **Re-spec (forward, unscored):** count tell = **2-yr stack ≤ −5%**, needing **2 consecutive prints**; bare YoY is demoted to context. On that spec the tell is **intact and hardening**.

**🔴 July NFP (rel 8/8, read 8/11) — a negative payroll print, and the unemployment rate FELL anyway.**

| Series | Jul 2026 | Move |
|---|---|---|
| Total nonfarm | 158,858k | **−23K MoM — first negative of the cycle**; June revised **+57K → +20K** |
| Unemployment rate | **4.1%** | −0.1pp — **falling while payrolls fall** |
| LFPR 16+ | **61.4%** | new 50-yr low ex-Covid (61.5 → 61.4) |
| Civilian labor force | 169,094k | **−264K MoM / −1,318K YoY** — this is why UR fell |
| L&H employment | 16,931k | **−40K MoM** post-World-Cup; +0.49% YoY |

**🟠 Foreign-born labor force — the Mar→Jul path is the finding, and it is not seasonal.**

| Year | Mar→Jul change | |
|---|---|---|
| 2022 / 2023 / 2024 | **+1.7% / +0.1% / +0.7%** | the normal seasonal path is flat-to-up |
| **2025** | **−4.9%** | anomaly starts here |
| **2026** | **−5.6%** (−1,885K) | intensification, not a step change |

July level **31,516k** — **−550K YoY, −1,002K vs Jul'24**. ⚠️ **Read honestly: the regime began in 2025**, and 2026 is −5.6% against 2025's −4.9%. The 2024 surge has been **fully given back and no more** — Jul'26 sits below Jul'24 (32,518k) and Jul'25 (32,066k) but still **above Jul'23 (30,870k)**.

⚠️ **COUNTER-EVIDENCE, logged against the thesis: less-than-HS LFPR (25+) ROSE to 45.5% in July from 43.1% in June (+2.4pp).** The "accelerating collapse" read (Apr 45.0 → May 44.0 → Jun 43.1) is **not confirmed** — June now looks like a small-sample trough rather than a trend point. This proxy is education-keyed, not nativity-keyed, and it just moved the other way.

⚠️ **NUMERIC-COLLISION TRAP — do not let this resurrect a retracted figure.** Peak-to-current on the foreign-born LF series (Mar'25 33,719k → Jul'26 31,516k) is **−2,203K**, which reads as "2.2M". **It is NOT the retracted "2.2M self-deportations (CBO)"** — that was a disputed DHS claim, killed fleet-wide 7/2. A peak-to-current drawdown on a seasonal NSA series and a deportation count are different quantities. Same class as the LABOR "1.9M" digit collision.

⚠️ **SERIES-IDENTITY CATCH (caught before citing).** `LNU01073413` and `LNU01073395` invert easily — **413 is NATIVE-born (138,719k), 395 is FOREIGN-born (31,516k)**. I first labelled them backwards. Verified three ways: components sum **exactly** to `LNU01000000`; the 395 share is 18.5–18.7% (matching the known foreign-born LF share); and 395's June YoY reproduces MARCO's own carried **−700K**. BLS `catalog=True` returns no titles for these IDs — the identity check is the only guard.

**🟡 OFLC H-2A Q3 FY26 — the print is LATE, not missed.** Live filename discovery (8/11) still returns `FY2026_Q2`; DOL has not published Q3, due ~Aug 1. MAR-11 (>425K, 88%) stays on the 254,688-through-Q2 base, unchanged. *(Boot reported the fetcher FAIL — it was a transient dol.gov ReadTimeout, **not** the hardcoded-filename class that killed it for 101 days. Direct retry succeeded in 13s.)*

**🟠 HAWK: the Canada tariff sentiment shock is FORWARD, not past (packet 8/10).** STATUS carried "Trump 50% Section 338 tariff 7/20" — that was the **proclamation** date. **Effective date is 12:01 a.m. ET Aug 19 — 8 days out.** Separately, a **Section 301 forced-labor action across 60 economies (~99.4% of US imports) has been live since 7/24.** Two windows, opposite phases: the 301 pull-forward is **already inside MARCO's June/July flow data** (so a July volume figure is not a clean demand read), while the Canada pull-forward is **live this fortnight** and will flatter August then reverse. **Do not net them into one "tariff pull-forward" artifact.** ⚠️ HAWK flags an **unresolved** conflict on whether autos are carved out of the 338 annex — verify against the proclamation annex before sizing anything auto-exposed.

**Packets adopted this session:** **CORAL 8/3** — VX-3.01 comes off placeholder at **~$7,136 / $300K dwelling / 2026** (*FL OIR publishes **no** statewide average-premium series at all, only rate-change filings — so the 7/25 "needs OIR primary" blocker was **unsatisfiable as written** and is retired; the four-way aggregator spread was four methodologies, not four disagreements*), **Lakeland ruled a third category** (inland affordability-overflow, 10.8% negative equity — **not** migration-implicated, not Jax/Ocala either), and **Citizens depopulation has STALLED** (PIF 278,061 at 7/24 vs 278,246 at 6/30 = −185 in 3.5 weeks after −29% over five months) → the **8/18** round is the tell. **HOMER 7/31** — "FL #1 for foreclosures" is a **RANK** claim; FL's 2025 level (0.435%) is **~31% below its own 2019** (0.63%) and FL ranked **#8 in 2023**. Qualifier applied to all three MARCO surfaces that carried it.

> ### 🔴 VX STALE SWEEP #2 — all three loaded rows refreshed off primaries, and **two of the three came back AGAINST the thesis**
> Boot flagged 3 stale BREACHED/CRITICAL rows. All three pulled; **loaded-status stale rows now 0.** Two produced findings that cut against MARCO, and one is a spec defect.
>
> **🔴 `TX-03` BREACHED → ELEVATED. The border municipal-revenue terminus is measured and it is GROWING.** TX Comptroller primary (`data.texas.gov` `vfba-b57j`, 11 border cities, live through July): **aggregate YTD +4.75% YoY, 10 of 11 cities positive.** **El Paso +9.7%** — the city Channel 4's frozen snapshot calls a "$55-62M deficit / 60% pension funding" case. **Pharr +5.4%** — the "S&P negative outlook" city. Laredo +0.9%, McAllen +7.2%. Only Edinburg is negative (−5.8%), on a single −43.0% June print against positives in 6 of 7 months — an adjustment artifact, not a collapse.
> **⇒ This is Channel-4 rebuild-condition #2 of the three named on 7/31, now RUN** — the rule was written in advance: *deficits widening + ratings under pressure ⇒ MEDIUM restored; stabilization ⇒ LOW confirmed or channel retired.*
> 🔴 **CORRECTION TO MY OWN FIRST READ (8/12, Will's question forced it — the framing below is the one that stands).** I first wrote that this satisfied the rule and moved the terminus to **LOW-CONFIRMED / RETIRE**. **That is too clean, and the defect is mine: sales-tax receipts are a revenue FLOW; municipal stress is a BALANCE-SHEET condition.** El Paso's "$55-62M deficit / 60% pension funding" are **stock** facts — a city can grow receipts every month and still carry a pension hole and widening spreads. Receipts are a real input to credit; **they do not test it.**
> **⇒ Revised status: condition #2 is RUN and NEGATIVE-for-the-thesis, but it is a WEAKER test than the pre-registration treated it as. The condition that actually tests credit — EMMA/MSRB filings + rating actions — is still UNRUN.** **Do not retire Channel 4 on this alone.** Retiring is defensible only (a) after the EMMA/MSRB leg agrees, or (b) as an explicit **resourcing** call — "not worth further instrumentation" — which must be labelled as such and never as an evidence verdict.
> ⚠️ **Same family as the trap already on MARCO's books twice** (Citizens insurer-side vs household cost; FAIR-Plan exposure vs coverage gap): **a fresh, correctly-pulled number answering an adjacent question to the one the threshold asks.** Third instance.
> What *does* stand: BREACHED was a compound band requiring "sustained decline + business closures + **municipal stress**," and **the revenue leg of municipal stress is measured and absent** — which is why the re-mark to ELEVATED holds.
> ⚠️ **What this does NOT falsify, kept separate:** these are **total** city receipts, not **cross-border shopper share** — total can grow on local spend while the Mexican-shopper component shrinks, which is what this row already said. The 40%→15-28% shopper-share claim is **untouched**. Also nominal (+4.75% vs ~2-3% CPI ≈ +2% real), ~2-month lag, and the **labor/construction leg was NOT refreshed** — carried at 50%, not re-verified.
>
> **🟠 `NV-01` — the bodies-down/dollars-up substitution INVERTED in June, but only for the month.** LVCVA Executive Summary PDF (primary, download+pdfminer): visitors 3,079,800 (−0.5%), but **ADR $156.32 (−4.4%), RevPAR −4.9%, Clark County gaming −0.7%, Strip −1.4%** — every dollar metric negative, where MARCO's carried read was "bodies down, **dollars up**." ⚠️ **Three deflators before anyone re-rates on it:** LVCVA's own note attributes it to a strong convention calendar against a **weak concert calendar**, so the ADR fall is partly **mix**, not demand; **H1 YTD dollars are still positive** (ADR +3.5%, RevPAR +3.5%, gaming +2.5%) — the *month* inverted, the *YTD* has not; and occupancy/ADR come from a ~75%-of-inventory **survey sample** LVCVA warns is variable. **The durable leg is air: −9.3% June, −6.7% YTD, deteriorating from −7.1% April** — the same "$ rides on air" structure as FL. ES-MARCO-07 (>5%) not breached, 3rd read.
> ⚠️ **Band NOT re-marked, deliberately.** This row is *Las Vegas **Canadian** Tourism* and BREACHED rests on the **Canadian** leg (carrier exits, Dec-25 Canadian −42%). **LVCVA publishes no nativity split** — everything above is *total* LAS. Substituting it would be the same similar-name/different-quantity trap as FAIR-Plan-exposure-vs-coverage-gap. **BREACHED is carried on an unrefreshed basis; the Canadian sub-leg needs carrier data and is STALE.**
>
> **🟡 `1.03` — the band is unscorable as written, and that is the finding.** "$X loss" never defines loss against *what*, and three incompatible bases circulate: YoY decline (Tourism Economics **−$8.3B, a 2025 figure** — this is what the carried "$5.7-8.3B" actually was), shortfall vs prior forecast (**$24.6B swing**), and shortfall vs 2019 real (**18% below**, ≈$39B — off the top of every band). Current vintage (US Travel, 5/7/26): 2025 **$175B (−2.4%)**, **2026 forecast $178B (+1.6%)**, visitation +3.4% to 70.6M, full recovery not until **2029**. **On basis (a) — the one the bands were written for — 2026 forecasts a GAIN, which would read NORMAL. I did not re-mark to NORMAL on a forecast**, because MARCO's own realized data disagrees (NTTO Apr overseas −14.1%, YTD −4.3%, ES-MARCO-09 leans FAIL). **Both cannot be right; NTTO June (~8/15) is the resolver.** Confidence cut 70%→50% — not because the world changed, but because the band cannot be scored.
>
> ⚠️ **Two search-layer decoys caught in one sweep, both date-related.** A headline claiming Las Vegas "visitor count drops **11.3%** in June" — the LVCVA primary says **−0.5%**. And a WTTC release reading as current ("US to lose **$12.5BN** in international visitor spend **this year**", spending falling to $169B) — **dated 2025-05-13 and describing calendar 2025.** Both would have shipped as fresh 2026 figures. *(→ `finding_anniversary_article_is_a_consensus_decoy`, now n=2 in a single session.)*

**Infrastructure closed:** DAEDALUS's `ledger_staleness` wiring defect — **measured three times (7/25, 8/4, 8/7) with zero references anywhere under `AGENTS/MARCO/`** — is wired into `boot.py`; `ML.tsv` frozen with a banner (was failing the two-state rule in *both* directions); STATUS footer thesis pointer **v2.0 → v3.1**. PROME's last round-2 straggler (`RESULTS.md:95` "~6pp detection floor") corrected to ~8.8pp.

**🔧 BUILT 8/12 — `scripts/version_drift_check.py`, the "a section-scoped fix does not clear a FILE" guard** (boot step, advisory, 0.1s). This session produced **four** instances of that one failure and three are mechanical: a brief section describing a test as *forthcoming* **11 days after it resolved NULL**; a `git mv` half-committed by path-scoping the destination; and duplicated stamp residue surviving a rewrite of its own line. Three classes ship — **V** canonical-thesis-version drift · **C** duplicated `**Label:**` in one line · **B** staged deletion with no matching add. **🔴 On its first run V found `CLAUDE.md` and `FINDINGS.md` — both boot-loaded — asserting the thesis was v2.5 when it is v3.1, six versions adrift** (same class DAEDALUS flagged 7/10 and which then sat a month). Both fixed. ⚠️ **Two further classes were measured and deliberately NOT built** — forward-language-vs-passed-date (**21/21 false positives**) and resolved-ID-written-as-pending (2/2) — rationale in the module docstring so nobody rebuilds them without re-measuring. Known-FP register is **per-instance, dated and expiring**; a flag is a prompt to LOOK, never a find-replace *(a correctly-dated "v2.7 retired the thermometer" is RIGHT)*. **The 4th instance — the Channel-4 read shipping before I asked what the metric measures — is analytical and no script catches it; it lives in `MEMORY.md`.**
