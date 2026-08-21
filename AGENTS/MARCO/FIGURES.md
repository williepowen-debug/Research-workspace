# MARCO — LOAD-BEARING FIGURE REGISTER

**Created:** 2026-07-31 (session 19) · **Last verification pass:** 2026-07-31

> ## ⚠️ THIS IS A VERIFICATION LOG, NOT A SOURCE OF TRUTH
> Every figure below has a named **canonical owner**. **If this file and the owner disagree, the OWNER WINS and the row here is stale — re-run it.** This file exists to answer one question the owner files cannot: **"when was this number last checked against a primary source, and by what method?"**
>
> Root CLAUDE.md discipline is *one source of truth per metric*. This register does not create a second one — it records **verification state**, and every row points back to where the value actually lives.

**Why it exists.** Session 19 cut a lot: Channel 1 demoted from spine, Channel 4 re-marked, 17 vectors frozen, 1 retracted figure removed. Will's question — *"are we documenting the real/accurate numbers?"* — is the right one, because the failure this register guards against is exactly the one that produced the retraction: **"2.2M self-deportations (CBO)" was a founding figure nobody re-verified for months**, and it propagated fleet-wide because it *looked* authoritative. A number's verification state is as load-bearing as the number ([[finding_loadbearing_number_must_be_reproducible]]).

**Status vocabulary:**
`VERIFIED-PRIMARY` pulled from the issuing source this pass · `CARRIED` asserted on a prior pull, not re-checked this pass · `FROZEN` deliberately not maintained, do not cite as current · `RETRACTED` withdrawn, replacement named · `NO PRIMARY` no live instrument exists

---

## 1. VERIFIED THIS PASS — pulled from the issuing primary 2026-07-31

All five BLS figures reproduced **exactly** to the digit. The VX stale backlog was also fully cleared this pass — **25 stale BREACHED/CRITICAL rows this morning → 0**, every one pulled from a live primary. These are the surviving HIGH-conviction Channel-1 **quantity** claims — the half of Channel 1 that v3.0 explicitly did *not* walk back.

| Figure | Verified value | Data period | Series / method | Canonical owner |
|---|---|---|---|---|
| **Foreign-born labor force, YoY** | **31,872K vs 32,572K = −700K** | Jun 2026 | BLS API `LNU01073395` | `workbook/VX.tsv` SDL-01 · THESIS Ch.1 |
| **LFPR, 16+** | **61.5%** (yr-ago 62.3) | Jun 2026 | BLS API `LNS11300000` | STATUS dashboard |
| **LFPR, less-than-HS diploma 25+** | **43.1%** (yr-ago 46.2) | Jun 2026 | BLS API `LNS11327659` | STATUS dashboard |
| **Unemployment rate, U-3** | **4.2%** (yr-ago 4.1) | Jun 2026 | BLS API `LNS14000000` | STATUS dashboard |
| **CPI fresh fruits & vegetables, YoY** | **+5.71%** (index 416.849) | Jun 2026 | BLS API `CUUR0000SAF1131` | STATUS dashboard |
| **H-2A certifications, FY26-through-Q2** | **254,688** (+16.9% YoY; Q1 62,367 + Q2 192,321) | FY26 Q2 | OFLC disclosure XLSX, dol.gov direct | `VX.tsv` H2A-01 · MAR-11 |
| **FL median days on market** | **78 days** (+8.3% vs pre-COVID Jun 2017-19 mean of 72; YoY −2.5%) | Jun 2026 | Realtor.com RDC Inventory Core Metrics, econdata S3 | `VX.tsv` FL-03 |
| **Canadian intent — 'flights to florida'** | index 46.8 = **−7.2% vs Jun'24** | Jun 2026 | Google Trends, geo=CA, all-categories | `VX.tsv` GTR-01 |
| **Canadian intent — 'florida' [Travel cat]** | index 29.2 = **−43.8% vs Jun'24** → BREACHED | Jun 2026 | Google Trends, geo=CA, **category 67** | `VX.tsv` GTR-01 |
| **Austin ZHVI** | **$426,944**, −5.71% YoY, −26.6% from Jun-2022 peak, **41 consecutive months of YoY decline** | Jun 2026 | Zillow ZHVI metro (repeat-value, SA) | `VX.tsv` TX-02 |
| **FL vs Snowbelt price spread** | FL metros median **−2.66%** vs Snowbelt **+3.68%** = **+6.34pp** | Jun 2026 | Zillow ZHVI, 16 FL vs 20 Snowbelt metros | `VX.tsv` 3.02 |
| **CA FAIR Plan policies in force** | **696,562** (+8% since Sep'25) | Jun 2026 | CA FAIR Plan key statistics (cfpnet.com) | `VX.tsv` CA-01 |
| **CA FAIR Plan total exposure** | **$768B** (+11% since Sep'25) | Jun 2026 | CA FAIR Plan key statistics | `VX.tsv` CA-01 ⚠️ *insurer-side exposure ≠ coverage gap — do not substitute* |

**⚠️ Basis traps caught while verifying these — both would have produced a WRONG re-mark:**
- **Google Trends: keyword AND category are load-bearing.** A first pull used `'florida vacation'` / all-categories and returned **+36.2% vs 2024**; the founding series is `'florida'` filtered to **Travel (cat 67)**, which returns **−43.8%**. **The correct basis reversed the sign of the conclusion.** The index is also *relative 0-100 within a single pull* — never compare across pulls.
- **Austin / house prices: median ≠ repeat-value index.** TX-02 previously carried a median SALE price ($435K); the refresh uses **ZHVI**, a repeat-value index that controls for transaction mix (CORAL documents the same preference). **Levels are not comparable across the two**; direction and duration are.
- **CA FAIR Plan: insurer-side exposure ≠ coverage gap.** CA-01's BREACHED band is written on a **>$500B coverage gap**; FAIR Plan **exposure** ($768B) is what the residual insurer covers, not what is left uninsured. Substituting one for the other would falsely trip BREACHED — the identical trap already documented for FL (VX-3.01 household cost vs VX-SFE-03 Citizens exposure, which moved *opposite* ways).
- **FL days on market: compare the SAME MONTH.** The old CRITICAL mark rested on "+41% vs Mar 2024" — March (58 days) is peak selling season, June is slow, so cross-month comparison manufactures ~30pp. The carried "98 days (Nov)" also **did not reproduce** (Realtor.com Nov'25 = 81), meaning the old row mixed metrics. Baseline is now pinned to **pre-COVID same-month**.

**Two notes on the above, so nobody re-derives them wrong:**
- The **−700K** is a *year-over-year* comparison of a **NSA** series. The **~1.0M** figure also carried in THESIS is a **peak-to-trough** measure (Mar'25→Feb'26), not the same statistic. **Both are correct; they are different measures.** Do not average, sum, or substitute them.
- The less-than-HS LFPR is quoted in STATUS against the **49.0% series high (Jul'25)**, not against the year-ago month (46.2%). Both comparisons are valid — **state which one you mean.**

---

## 2. CARRIED — asserted but NOT re-verified this pass

Live and load-bearing, last pulled on the date shown. Not suspect — simply not re-checked today. **Anyone citing these should know the vintage.**

| Figure | Value | Data period | Last pulled | Canonical owner |
|---|---|---|---|---|
| Canadian visitors, 2-yr stack | −28.7% (auto −29.6%, **air −25.0%**) | Jun 2026 | 2026-07-25 (StatCan Daily, rel 7/13) | `VX.tsv` 1.01 |
| Mexico remittances | $5,611M, +3.8% YoY, **transfer count −1.7% YoY** | May 2026 | 2026-07-01 (Banxico) | `VX.tsv` 2.08 · **June print due Aug 1** |
| FL condo inventory | 8.1 months (median $305K, +1.7% YoY) | Jun 2026 | 2026-07-25 (FL Realtors, via CORAL) | `VX.tsv` FL-02 |
| FL Citizens policies-in-force | 278,246 (rate cut eff. 7/1) | Jun 30 2026 | 2026-07-25 (CORAL correction) | CORAL owns; `VX.tsv` SFE-03 mirrors |
| FL Citizens exposure | ~$295.1B (−43% YoY) | Jun 2025 | 2026-07-02 | CORAL owns |
| FLL passengers | 2,255,277, −10.7% YoY / −26.1% 2-yr | May 2026 | 2026-07-25 (Broward PDF, pdfminer) | `VX.tsv` 1.04 |
| MIA passengers | +0.52% YoY (intl +3.52%, dom −1.75%) | May 2026 | 2026-07-25 | `VX.tsv` 1.04 |
| NFP / payrolls | +57K (May revised to +129K) | Jun 2026 | 2026-07-02 | STATUS dashboard |
| Enforcement funding | ~$70B, ICE + parts of CBP, through Jan 2029 | Signed Jun 10 2026 | 2026-06-10 | THESIS Ch.1 ⚠️ *sub-split $38B/$26B is the pre-trim PROPOSAL — never cite as enacted* |

**Known blocked / unavailable:** MCO passenger counts (flymco JS-rendered, re-verified blocked 7/25 → BTS T-100 is the only path; blocks MAR-24 **and** MAR-22).

---

## 3. STALE BY DESIGN — correct, but awaiting a scheduled print

Not rot. These update on a fixed cadence and are current *as of their last release*.

| Figure | Value | Period | Next print | Owner |
|---|---|---|---|---|
| **FL net domestic migration** | **+22,517** (93% collapse from 310,892 in 2022; FL #1 → #8) | 2025 annual | Census, ~late 2026 | `VX.tsv` 3.03 |
| Net migration estimate (CBO) | −290K to −525K | 2025 | ~late 2026 | `VX.tsv` 2.04 |
| FL international migration | +411K (2024) | 2024 | ~late 2026 | `VX.tsv` 3.04 |
| TX net domestic migration | +219K (2022) → **+67K (2024)** = 69% collapse; still positive | 2024 | ~late 2026 | `VX.tsv` TX-04 |
| Canada tourism index | ~0.72 (2025 trips ÷ 2019) | 2025 annual | ~early 2027 | `VX.tsv` CTI-01 — ⚠️ overlaps 1.01; **1.01 is the live Canadian read** |

**Sub-annual FL migration proxies** (`workbook/MIGRATION_PROXIES.tsv`): FLHSMV licence inflow **+3.0% H1-2026**, voter-reg net **−0.8% (May)**. **DIRECTION TELLS ONLY — different bases; never restate as the canonical level.**

---

## 4. RETRACTED — and what the accurate number is instead

**This is the section that matters most for "are we documenting the real numbers."**

| Retracted claim | Why it was wrong | ✅ The accurate figure | Fixed |
|---|---|---|---|
| **"2.2M self-deportations (CBO)"** | Wrong on **count AND source**. It was a *disputed DHS* claim (CMS: "the Two Million Deportation Myth"), **never CBO-modelled**. CBO's own figure is **~290K removals + 30K voluntary (2026-30)**. The false attribution to a neutral authority is what made it stick. | **Foreign-born LF −700K YoY / ~1.0M peak-to-trough** (BLS Table A-7; `LNU01073395`) — verified again 7/31, §1 | thesis v2.6, 7/2 · `VX.tsv` 2.02 lagged until **7/31** · 🔴 **`VX.tsv` 2.01 lagged until 2026-08-21** — see below |
| **FL L&H wage divergence as a Channel-1 instrument** (+8.75% vs national +3.87%) | **The wage numbers are CORRECT** — the *inference* was wrong. FL's gap is an **Amendment 2** statutory floor rise (7.7% in-window); TX, with maximal immigrant exposure and a floor frozen since 2009, ran *negative*. Compounding: at **+4.88pp** the gap sat far inside the dispersion of the series it came from — pooled cross-state sd **5.88pp**, giving a **~11.53pp** band around any single state's gap (≈0.4 sd). | **No replacement instrument.** Channel-1 transmission is **UNDEMONSTRATED** (v3.0). The wage figures remain valid as a **CARL-lane statutory-cost** input | v2.8 (7/25) → v3.0 (7/31) |
| **"~6pp detection floor"** as a general rule for state-CES gaps | **Right conclusion, wrong statistic, wrong scope — and it shipped to two agents.** 6.15pp is 1.96×SE for a **stratum-mean difference across 6–8 states**: a significance threshold, not a power MDE (that is **8.78pp**), and not a rule about any single state's gap (band **~11.53pp**). Sent to CARL as a general state-CES caution and to LABOR beside the LAB-17 convergence. | **Size a gap against the dispersion of the statistic you actually computed.** Stratum difference → 8.78pp at 80% power; single state → ~11.53pp. Corrections sent CARL + LABOR 7/31 eve | 7/31 eve (PROME audit) |
| **"median 6-month within-state swing 3.2pp"** | Reproduces under **no** definition tried — median range 4.02, mean range 4.44, within-state sd 1.48, median \|MoM step\| 1.29, E&H variants 1.23–4.82. Propagated to 7 surfaces + the LABOR packet. | **4.02pp** = median 6-month range, TTU control, 14 scored states (`scripts/fl_diagnostic_score.py`). Conclusion survives: 4.02 ≪ 5.88 cross-state sd | 7/31 eve (PROME audit) |
| **"the FL diagnostic behaves exactly as a floor-driven story predicts"** (CARL packet, 7/31) | **Inverted its own pre-registration.** `PREREG` §3 said FL DID **≈ 0** confirms Amendment 2; actual **+6.89pp**. The MISS was printed but never scored, then the failure was cited as confirmation. Also asserted "stable in every month of 2026" — false; June is **+2.96pp** above the Jan–May mean. | **MISS.** Amendment 2 stays the best account of FL's raw gap **on statutory grounds only**; FL's cell is inside the noise (+1.25 sd; AL +7.61, LA +12.00 beat it with no floor step). **Forward $14→$15 Sep-30-2026 impulse unaffected** | 7/31 eve (PROME audit) |
| **Produce CPI as Channel-1 evidence** | Multi-causal (FL freeze $3.17B + 17% tomato tariff + diesel), then ES-MARCO-08 resolved toward **freight** | F&V **+5.71% YoY** is a *correct* figure (verified §1) — it is simply **not evidence for Channel 1 in either direction** | v2.1 → v2.7 |
| **MAR-17 "FL Citizens exposure >$750B"** | Premise inverted — Citizens is **depopulating**, exposure collapsing not growing | ~**$295.1B** (Jun'25, −43% YoY), PIF **278,246** | INVALIDATED 7/2 |
| **"415K H-2A"** | That was positions **REQUESTED**, not certified — two different metrics | FY25 **certified 398,059**; FY26-thru-Q2 **254,688** | 6/15 |
| **MAR-24 at 45%** (docket copy) | Stale copy of **MAR-24's own** prior confidence — its note records `65→55 (May 31)→45 (session 9)`, later raised to 60. *(This row previously said "45% is MAR-14's number" — wrong provenance, corrected 7/31 eve after PROME audit; MAR-14 is at **20%** since the v3.0 mark-down and was never 45.)* | **MAR-24 = 60%** · MAR-14 = 20% | 7/31 · provenance fixed 7/31 eve |

---

### ⚠️ 8/21 — a retraction OF MY OWN, and the register should carry it: I withdrew a real figure

**Claim withdrawn:** *"NV Gaming's −6.99% July percentage-fee figure is a partial-vs-full-month artifact; not adopted."*

**Why it was wrong:** I reasoned from a footnote on ONE side (*"collections are through July 21"*) without checking whether the same convention governs the comparison basis. **It does** — the prior month's release carries the identical note (*"through June 23"*). A limitation disclosed on one side is not evidence the other side lacks it.

**Test that settles it, run on review:** a one-sided truncation would produce a systematic directional skew. Across FY26's twelve monthly prints the **mean is +7.09%, six of twelve negative, full year +5.07%** — no skew, so no asymmetry.

| | |
|---|---|
| **✅ The accurate figure** | **−6.99% is REAL.** And it carries no signal: σ across those twelve prints is **14.04pp** (−12.35% to +33.80%), so this is a **−1.0σ move**, with **2 of 12** months at least as negative |
| **What still stands** | The July value is genuinely *"through July 21"* and *"subject to revision"*; `TAX-01`'s ELEVATED→NORMAL de-mark holds, **on base-rate grounds** |
| **Reached** | `VX-TAX-01`, STATUS, SCRATCH, the tail-clear archive doc, **and the NEXUS brief** (consumer surface — explicit re-read notice issued). **No packet to another agent carried it** — the claim post-dated all six dispatches |
| **Fixed** | 2026-08-21, same session, on self-review |

⚠️ **The standing lesson is uncomfortable and belongs in this register: the error was produced BY the correction discipline, not despite it.** I was pattern-matching to the basis-trap family this very file catalogues, and the pattern fired on a case where it did not apply. **Apply the same evidentiary standard to a WITHDRAWAL that you would to an adoption.**

### 🔴 8/21 — the retraction had ONE more survivor, and it was in a BREACHED row

**`VX-MARCO-2.01` (Immigration Enforcement Activity) still asserted *"The 2.2M STOCK loss (SDL-01) irreversible regardless"* as live text on 2026-08-21** — **51 days** after the 7/31 PROME audit corrected the *same* figure in `VX-MARCO-2.02`, and **50 days** after the fleet-wide retraction landed at v2.6 on 7/2.

**Why it survived a sweep that was looking for exactly this.** The 7/31 audit found the figure in 2.02 and fixed it there. 2.01 is the adjacent row in the same file, same domain (`WFD`), same `BREACHED` status — and it was **67 days stale**, so no refresh pass had reopened it. **A fix clears the ROW you are looking at, not the LEDGER** — the same class as MARCO's own *"a fix clears the REGION I am looking at, not the FILE"* lesson, one level up: there the unit was a file, here it is a **row within a file that was itself the subject of the sweep.**

**What makes this worse than a stale number:** 2.01 is `BREACHED` + `HIGH` priority, i.e. **exactly the class that gets cited**, and the retracted figure was doing load-bearing work in the sentence (*"irreversible regardless"* — the clause that made the enforcement-flow argument self-sustaining).

| | |
|---|---|
| **Retracted text removed** | "The 2.2M STOCK loss (SDL-01) irreversible regardless" |
| **✅ Accurate replacement** | **~1.0M realized foreign-born LF decline / ~1.5M population** — live figure `VX-MARCO-SDL-01`, 31,516k Jul'26, −550K YoY (BLS `LNU01073395`, pulled 8/11) |
| **Scope check run** | `grep -rn "2\.2M"` across all MARCO surfaces (excl. `inbox/`, `domain/sources/`, `_archive`): **13 hits, 12 correctly-labelled historical/retraction records** (this register, `CHANGELOG` old-view, `MAINTENANCE` resolution log, `THESIS` "was cited", `SCRATCH` numeric-collision warning). **2.01 was the only surviving LIVE assertion.** |
| **Fixed** | 2026-08-21, session 22 |

⚠️ **Standing consequence:** a retraction sweep must enumerate the **vector ledger by ID**, not stop at the row that produced the hit. And the arrest-rate leg of 2.01 (*"500-600+/day; 65K detained"*, Jun-15 vintage) was **NOT** re-verified this pass — it is the band-scoring input, so 2.01's `BREACHED` mark now rests on an **unrefreshed rate** and is labelled carried-not-confirmed.

## 5. FROZEN — no accurate current number exists, and that is the honest answer

The 17 border-fiscal vectors were frozen 7/31 at **Feb-2026** vintage. **We do not know the current values.** The figures below are a **historical snapshot** and must not be quoted as current:

> Laredo Mexican-shopper share 51%→13% · McAllen 36%→28% · Nogales residential −43.2% YoY · El Paso $55-62M deficit + 60% pension funded ratio · Pharr S&P negative outlook

**One useful data point on how these aged:** MAR-01 resolved 7/2 and found Nogales residential **still ~−43%** ("stabilizing-soft," median ~$245K) — so that February figure was **approximately still true five months later**. Freezing is a statement that *we stopped verifying*, **not** that the numbers were wrong.

**To get accurate current numbers** (this is the named Channel-4 rebuild): EMMA/MSRB filings + rating actions (El Paso, Pharr, Laredo, Nogales) · TX Comptroller + AZ DOR sales-tax receipts by border city · CBP border-crossing counts.

**`NO PRIMARY` — genuinely unmeasurable on current sources:** CA ag workforce composition (`CA-02`) and ag wage growth (`2.05`). USDA **NASS Farm Labor Survey and DOL NAWS were both canceled (Aug 2025)** — the government deleted the instruments. Candidates: QCEW NAICS 11, OFLC AEWR. ⚠️ **AEWR is an administratively-set floor — it can never evidence scarcity** (that would repeat the Amendment 2 error); only *offers above* it can.

---

## Maintenance

Re-run §1 at each closeout that touches a load-bearing figure, and move rows between §1 and §2 honestly — **a row that says VERIFIED must actually have been pulled that day.** The whole value of this file is that its status column is true; a register that drifts is worse than none, because it manufactures confidence ([[finding_freshness_check_cannot_catch_a_fresh_lie]]).
