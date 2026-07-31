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

All five BLS figures reproduced **exactly** to the digit. These are the surviving HIGH-conviction Channel-1 **quantity** claims — the half of Channel 1 that v3.0 explicitly did *not* walk back.

| Figure | Verified value | Data period | Series / method | Canonical owner |
|---|---|---|---|---|
| **Foreign-born labor force, YoY** | **31,872K vs 32,572K = −700K** | Jun 2026 | BLS API `LNU01073395` | `workbook/VX.tsv` SDL-01 · THESIS Ch.1 |
| **LFPR, 16+** | **61.5%** (yr-ago 62.3) | Jun 2026 | BLS API `LNS11300000` | STATUS dashboard |
| **LFPR, less-than-HS diploma 25+** | **43.1%** (yr-ago 46.2) | Jun 2026 | BLS API `LNS11327659` | STATUS dashboard |
| **Unemployment rate, U-3** | **4.2%** (yr-ago 4.1) | Jun 2026 | BLS API `LNS14000000` | STATUS dashboard |
| **CPI fresh fruits & vegetables, YoY** | **+5.71%** (index 416.849) | Jun 2026 | BLS API `CUUR0000SAF1131` | STATUS dashboard |
| **H-2A certifications, FY26-through-Q2** | **254,688** (+16.9% YoY; Q1 62,367 + Q2 192,321) | FY26 Q2 | OFLC disclosure XLSX, dol.gov direct | `VX.tsv` H2A-01 · MAR-11 |

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
| **"2.2M self-deportations (CBO)"** | Wrong on **count AND source**. It was a *disputed DHS* claim (CMS: "the Two Million Deportation Myth"), **never CBO-modelled**. CBO's own figure is **~290K removals + 30K voluntary (2026-30)**. The false attribution to a neutral authority is what made it stick. | **Foreign-born LF −700K YoY / ~1.0M peak-to-trough** (BLS Table A-7; `LNU01073395`) — verified again 7/31, §1 | thesis v2.6, 7/2 · `VX.tsv` 2.02 lagged until **7/31** |
| **FL L&H wage divergence as a Channel-1 instrument** (+8.75% vs national +3.87%) | **The wage numbers are CORRECT** — the *inference* was wrong. FL's gap is an **Amendment 2** statutory floor rise (7.7% in-window); TX, with maximal immigrant exposure and a floor frozen since 2009, ran *negative*. Compounding: at **+4.88pp** the gap sat **below the ~6pp detection floor** of the series it came from. | **No replacement instrument.** Channel-1 transmission is **UNDEMONSTRATED** (v3.0). The wage figures remain valid as a **CARL-lane statutory-cost** input | v2.8 (7/25) → v3.0 (7/31) |
| **Produce CPI as Channel-1 evidence** | Multi-causal (FL freeze $3.17B + 17% tomato tariff + diesel), then ES-MARCO-08 resolved toward **freight** | F&V **+5.71% YoY** is a *correct* figure (verified §1) — it is simply **not evidence for Channel 1 in either direction** | v2.1 → v2.7 |
| **MAR-17 "FL Citizens exposure >$750B"** | Premise inverted — Citizens is **depopulating**, exposure collapsing not growing | ~**$295.1B** (Jun'25, −43% YoY), PIF **278,246** | INVALIDATED 7/2 |
| **"415K H-2A"** | That was positions **REQUESTED**, not certified — two different metrics | FY25 **certified 398,059**; FY26-thru-Q2 **254,688** | 6/15 |
| **MAR-24 at 45%** (docket copy) | Stale copy; 45% is **MAR-14's** number | **MAR-24 = 60%** | 7/31 |

---

## 5. FROZEN — no accurate current number exists, and that is the honest answer

The 17 border-fiscal vectors were frozen 7/31 at **Feb-2026** vintage. **We do not know the current values.** The figures below are a **historical snapshot** and must not be quoted as current:

> Laredo Mexican-shopper share 51%→13% · McAllen 36%→28% · Nogales residential −43.2% YoY · El Paso $55-62M deficit + 60% pension funded ratio · Pharr S&P negative outlook

**One useful data point on how these aged:** MAR-01 resolved 7/2 and found Nogales residential **still ~−43%** ("stabilizing-soft," median ~$245K) — so that February figure was **approximately still true five months later**. Freezing is a statement that *we stopped verifying*, **not** that the numbers were wrong.

**To get accurate current numbers** (this is the named Channel-4 rebuild): EMMA/MSRB filings + rating actions (El Paso, Pharr, Laredo, Nogales) · TX Comptroller + AZ DOR sales-tax receipts by border city · CBP border-crossing counts.

**`NO PRIMARY` — genuinely unmeasurable on current sources:** CA ag workforce composition (`CA-02`) and ag wage growth (`2.05`). USDA **NASS Farm Labor Survey and DOL NAWS were both canceled (Aug 2025)** — the government deleted the instruments. Candidates: QCEW NAICS 11, OFLC AEWR. ⚠️ **AEWR is an administratively-set floor — it can never evidence scarcity** (that would repeat the Amendment 2 error); only *offers above* it can.

---

## Maintenance

Re-run §1 at each closeout that touches a load-bearing figure, and move rows between §1 and §2 honestly — **a row that says VERIFIED must actually have been pulled that day.** The whole value of this file is that its status column is true; a register that drifts is worse than none, because it manufactures confidence ([[finding_freshness_check_cannot_catch_a_fresh_lie]]).
