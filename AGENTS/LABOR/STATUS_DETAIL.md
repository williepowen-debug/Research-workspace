# LABOR STATUS — COLD DETAIL (`STATUS_DETAIL.md`)

**Created:** 2026-09-02 (LABOR session, PROME-spawned WQ-156) · **Split from:** `AGENTS/LABOR/STATUS.md` at git `74bfb3cf5`, pre-split **53,375 B / 231 lines / crc32 `4117580199`** (`PROME/tools/measure.py`).
**Why:** READ_CAP rule 1 — a boot-read-whole surface stays under the binding **32,550 B** budget; STATUS.md was **53,375 B = 164% of budget**. Remedy = rule 4(b) **hot/cold split** (owners choose HOW, never WHETHER).

> 🔒 **STATUS.md is CANONICAL for every live figure, band, score and open grade.** This file is the **record**: graded history, per-release evidence, derivations, retired/no-fire thresholds. Every block below is **VERBATIM and contiguous** from the pre-split `STATUS.md`, moved never edited — no figure was changed in the move. Where a block is a table column, the `#`/`Vector` label cells are copied verbatim as row keys.
> ⛔ **Never cite a value from here as current** — if a figure appears both here and in `STATUS.md`, `STATUS.md` wins. Cite this file as *what was written on the day*, with its own date.
> ↩️ **Back-pointer:** `AGENTS/LABOR/STATUS.md` § SPLIT BANNER carries the forward pointer and the section map.
> 📅 **DATED RE-TRIGGER (READ_CAP rule 7 — this is not a leanness claim):** split **2026-09-02**; **re-measure `STATUS.md` at every closeout append and unconditionally on 2026-10-02, whichever first** — `python3 scripts/read_cap_check.py --agent LABOR` + `python3 PROME/tools/measure.py AGENTS/LABOR/STATUS.md`. This file is **on-demand / cold — it is NOT a boot read** and carries no budget of its own; if it ever becomes a boot read it acquires one.

**Section map (original `STATUS.md` line ranges, pre-split):**

| § | Block | Source lines |
|---|---|---|
| `core-tension` | CORE TENSION — full section (table + 8/07 resolution) | L8-28 |
| `matrix-regrade-notes` | CONVERGENCE MATRIX — 8/7 + Jul-2 re-grade basis notes | L31-34 |
| `matrix-evidence` | CONVERGENCE MATRIX — Key Signal + Indep columns (per vector) | L36-52 (Key Signal + Indep columns) |
| `matrix-bearish-shape` | CONVERGENCE MATRIX — shape of the remaining bearish core (8/7) | L55 |
| `cross-domain` | CROSS-DOMAIN CONTEXT (MARCO-owned supply side — not in LABOR score) | L57-61 |
| `signal-dashboard` | SIGNAL DASHBOARD — full section (per-release evidence + primary citations) | L63-89 |
| `thresholds-nofire` | KEY THRESHOLDS — rows that fire nothing (diagnostic / published-only / no-fire) | L100, L105-106, L112 |
| `fed-trap-history` | FED TRAP & THESIS — superseded lede + rotation pointer | L118, L120 |
| `danger-window` | DANGER WINDOW Q3 2026 — graded rows | L126-135 |
| `predictions-resolved` | PREDICTIONS — resolved tables + the 8/07 rotation pointer | L146, L148, L150-159 |
| `exit-rules-history` | EXIT RULES — base-rate rotation pointer + I-1 8/5 verdict | L174, L176 |
| `calendar-graded` | MONITORING CALENDAR — graded rows | L186-187 |
| `pending-history` | PENDING INPUTS — rotation banner + discharged windows | L195, L199-202 |
| `pickup-closed` | NEXT SESSION PICKUP — rotation banner + closed items 0, 0b, 7 | L207, L209-210, L217 |

---

## [COLD] CORE TENSION — full section (table + 8/07 resolution)

*Anchor `core-tension` · moved 2026-09-02 from `STATUS.md` L8-28 · VERBATIM.*

## ⚡ CORE TENSION — FREEZE DEEPENS; DEMAND vs SUPPLY ATTRIBUTION IS THE LIVE QUESTION

| Signal | Reading | Direction |
|--------|---------|-----------|
| 🔴 **NFP July (Aug 7)** | **−23,000** — first negative of the cycle; private **+30K**, government **−53K** | ⬇️🔴 **the count layer broke.** BLS: prior-12-mo avg **+34K**. Revised run 214/148/**63**/**20**/**−23** → 3-mo avg **+20K** |
| 🔴 **Revisions May+Jun (Aug 7)** | **net −103,000** (May 129→**63K**, Jun 57→**20K**) | ⬇️🔴 **revision regime DEEPENING** — −74K in June, −103K in July. Feeds vector 8 + LAB-08 |
| **U-3 / U-6 July** | **4.1%** (↓0.1) / **7.9%** (flat) | ⚠️ **NO-SIGNAL (L-06)**: LF **−264K**, LFPR **61.4%** (↓0.1). U-3 fell on the denominator *again* — 2nd straight month |
| **AHE YoY July** | **3.2%** ($37.62, +2c MoM) — **DECELERATED from 3.5%** | ⬇️🔴 **the wage-scarcity read is gone.** Also **closes the AHE↔ECI wedge from the AHE side** → 1c packets to CARL/HENRY 8/7 |
| 🆕 **Sector detail (Jul) — the deterioration is OFF my axis** | Local gov't education **−50K**; retail trade **−19K** (warehouse clubs/supercenters −21K, gas stations −5K); financial activities **−14K** (**−121K since May-2025 peak**) | ⬇️🔴 **My WARN/tech/AI channel contributed NOTHING.** Routed: retail→CARL, financial→REGINALD. **Local-gov education is un-vectored — candidate vector, see matrix footnote** |
| **🆕 ECI Q2 (7/31)** | Civilian comp **3.4% flat**; wages **3.4→3.2%**; **private wages 3.4→3.1%**; benefits 3.6→**3.8%**, health **6.0%**; **real private wages −0.4%** | ⬇️🔴 **composition-controlled wages DECELERATING while AHE accelerates — 0.4pp wedge, widening.** The AHE signal is a mix artifact; total comp held up by MEDICAL costs, not tightness |
| Claims w/e Aug 22 | **203K**; 4-wk MA **205,500**; CC **1,778K** (w/e Aug 15) | 🟢 realization still at multi-decade lows and **no threshold is near** (T-01 250K, T-02 300K). … |  *[carried: 207]*
| 🆕 **JOLTS July (9/1)** | **Hires 5,054K** (**−278K**), rate **3.4 → 3.2%**; **quits rate 2.0 → 1.9%**; openings **7,271K** (+89K), rate 4.3 → **4.4%**; **layoffs 1,666K, rate 1.1 → 1.0%**. **June revised: openings −177K (7,359 → 7,182K), hires 5,348 → 5,332K** | ⬇️🔴 **THE GAP STOPPED CLOSING FROM THE HIRING SIDE — it reversed.** Openings up *and* hires down = matching **deteriorating**, the mirror image of June's read. Hires-per-opening `5,054/7,271 = 0.695` vs `5,332/7,182 = 0.742` (**−0.047**). **Firing side went QUIETER, not louder (1.0%)** — a low-churn freeze, not a layoff wave |
| 🔴 **Long-term unemployed (Jul)** | **1.8M, 25.5% share** (from 1.9M / 27.3%) — and **BLS says it "changed little over the year"** | ⬇️ **THE YoY ACCUMULATION LEG IS GONE.** This row previously read *"+286K YoY, freeze cost accumulating — strongest new bearish datum."* BLS's own characterization now contradicts that → **vector 6 cut 4 → 3** |
| Household survey | June emp −507K (FT-led −514K); **July 2nd print: unemployed −178K, LF −264K** | ⚠️ **2nd print did NOT confirm a demand story** — the fall is on the participation side again, not a jobs-found side |
| Mfg employment surveys | **The MFG divergence stays closed — all three agreed UP through July, and August holds ≥50 while DECELERATING.** ISM employment **52.8** (Jul) → **51.2** (Aug, **−1.6**, 2nd straight month in expansion); S&P Global flash July employment **rose 1st time in 3 mo**; BLS realized mfg **+5K** (Jul, from +3K Jun) | ⬆️ **The one-layer-up divergence persists: manufacturing surveys expanding while SERVICES surveys contract and the aggregate payroll count goes negative.** Manufacturing is ~8% of payrolls; services is where the count lives. **ISM Svs Aug (Thu 9/3) is the leg that settles vector 3** |
| 🔴 **ISM Svs employment — Jun 51.2 → Jul 47.4 (BOTH graded 8/5–8/7)** | **June 51.2** (+3.3 from 47.9, expansion 1st in 4 mo — *this file wrongly carried 47.4 for June from 7/6 to 8/5*). **July 47.4** (−3.8): *"returned to contraction territory after only one month in expansion"*; below its 12-mo avg 48.7; **"below 50 percent for 12 of the last 18 months"** (ISM Chair) | ⬇️🔴 **THE SURVEY LAYER IS SPLIT, NOT THAWING** — mfg expanding, services back in contraction. … |

**Resolution (2026-08-07) — the honest state after a week that cut both ways.** Three layers, and they now disagree with each other in a specific, statable way. …  *[carried: 4.1% · −23 · +20K · 1.1% · Sep 4]*

---


---

## [COLD] CONVERGENCE MATRIX — 8/7 + Jul-2 re-grade basis notes

*Anchor `matrix-regrade-notes` · moved 2026-09-02 from `STATUS.md` L31-34 · VERBATIM.*

> 🔴 **8/7 re-grade basis (Will-directed, written before the scores):** *hiring intentions thawed, the realized count did not follow, and deterioration broadened into sectors I was not watching.* Four vectors move: **v2 → 1** …
> ⚠️ **UN-VECTORED CHANNEL, flagged not improvised:** **local government education −50,000** — the single largest sector loss in the July print — has **no vector**. …

> **Jul-2 re-grade:** freeze deepened but the *announcement* layer stood down and DOGE/Hormuz faded → honest score **37/75** (15 live vectors after the v6/v9 merge; ≈41/80 like-for-like on the Jun-16 16-vector basis, vs 48/80 then. …

---

## [COLD] CONVERGENCE MATRIX — Key Signal + Indep columns (per vector)

*Anchor `matrix-evidence` · moved 2026-09-02 from `STATUS.md` L36-52, columns `Key Signal` + `Indep` · VERBATIM.*

| # | Vector | Key Signal | Indep |
|---|--------|------------|-------|
| 1 | WARN pipeline | 250,711 wkrs / 2,658 notices [CONF LayoffAlert.org Jul 2]; +3.8%/16d = **PLATEAU** (peak ~2,257/d → ~575/d); T-07 unfired (~17K/mo). Incoming: JBS Souderton PA **1,485** (eff Aug 14). … | Jun-surge cohort **Spirit-led** (MSFT leg RETRACTED Jul 2 PM — zero 2026 MSFT WARN filings; the 8,750 was a VR-offer program, not layoffs); shared w/ v2/v5 history |
| 2 | Sector cuts (announcement flow) | 🔴 **Challenger July 33,429 = the LOWEST MONTHLY TOTAL IN TWO YEARS** (−27% m/m, −46% YoY) → **card §2e "<40K → vector 2 → 1", pre-committed 7/31, executed.** Hiring plans **16,095 in July alone (+47% m/m)**, … | Shares root w/ v5 (AI = top reason inside this flow) — don't double-count |
| 3 | ISM/survey employment | 🔴 **9/1 — MFG LEG MET, SERVICES LEG PENDING; THE VECTOR CANNOT MOVE FOR TWO MORE DAYS AND I AM SAYING SO RATHER THAN SPLITTING THE DIFFERENCE.** **ISM Mfg Aug employment 51.2** (−1.6) is a **2nd consecutive month ≥50**, so the docketed *"≥50 a 2nd month = survey thaw CONFIRMED"* leg **fires on manufacturing** — the 33-month streak break was not a one-print spike. **But v3's own drop-to-1 condition, pre-committed 8/5, requires BOTH ISM surveys >50 in the SAME month**, and **ISM Services August prints Thu 9/3**. Prior: Svs Jul employment **47.4** (−3.8), *"returned to contraction territory after only one month in expansion"* | Survey layer. ⚠️ **No longer independent of vector 4** — hires and survey hiring intentions are the same thaw seen twice; do not double-count. ✅ **Independent of BLS entirely (evidence Type D on the 9/4 map)** |
| 4 | JOLTS hire-rate freeze | 🔴 **9/1 — GRADED ON THE CORRECTED BASIS, NET FIRST AS PRE-COMMITTED, AND IT HOLDS AT 3.** July NET `5,054 − 5,072 = −18K` — **third consecutive negative month** (May −8K, Jun −5K on revised). Gross hires **−278K to 5,054K**, rate **3.4 → 3.2%**. **Base-rated at the primary, 308 months from 2000-12: NET ≤0 in 72 = 23.4%; runs of ≥3 consecutive = 6; the last one ended September 2010.** ⚠️ **TWO DISCOUNTS ON MY OWN FINDING, applied before it travels: (a)** the five prior runs are really **two episodes** (2001–03, 2008–10), not five draws; **(b)** my own frozen map §2 says **JOLTS is ratio-estimated to CES**, so NET is a LEVEL construct and **partly circular** with the negative payrolls it appears to confirm — the licensed independent content is the **rates as shapes**. 🔒 **WHY NO UPGRADE: zero pre-registered bands fired, and I will not move a score on a measure whose bands were never written (L-18).** ✅ **Calibration note, on the reasoning not the outcome:** on 8/7 I refused to cut this vector despite gross hires +96K **because the measure was defective** — the corrected NET was *already* ≤0 in both those months. The hold was right on its own logic | Independent (flow data, not announcements) — ⚠️ **but only PARTIALLY independent of CES; see the 9/4 map §1 leg 7** |
| 5 | AI displacement | ✅ **8/7 — THE AT-RISK FLAG IS RESOLVED AND THE VECTOR SURVIVES ON ITS PRE-COMMITTED TEST.** Card §2e Band A was *"AI share <25% or not #1 → cut to 3."* **Challenger July: AI 10,970 of 33,429 = 32.8%, #1 for … | Level cooled with v2; the *share/persistence* + now hard filings = independent signal |
| 6 | Long-term unemployed / duration | 🔴 **THE ISSUER CONTRADICTED THIS ROW'S OWN BASIS.** July: **1.8M, 25.5% share** (from 1.9M / 27.3%) — and BLS states the LT-unemployed count *"edged … | Same phenomenon as old v9 (duration) — MERGED, counted once |
| 7 | UI exhaustion / CC grind | **CC w/e Aug 15 = 1,778K** [CONF DOL via FRED CCSA, obs 2026-08-15] — **−18K**, and the w/e Aug 8 print revised **DOWN 1,799 → 1,796K**. … | Mechanically downstream of v4 (can't exit unemployment) |
| 8 | BLS data degradation | 🔴 **CUT BY PRE-COMMITMENT ON 8/28 — the vector that escalated on 8/7 is the vector this print refutes, and the reversal was written into BOTH this cell and the frozen card three weeks before the figure … | Independent (measurement layer) |
| 10 | Healthcare cracking | **LAB-13 ❌ FALSIFIED 8/7 → card §2f pre-committed `>+15K → vector 10 → 1`, executed.** July health care **+22,000**, BLS: *"continued its upward trend… but at a slower pace than the average monthly gain over … | Independent sector read |
| 11 | ICE worksite disruption → layoffs | 🔴 **FALSIFICATION TRIGGER MET — dropped on evidence that runs AGAINST my own book, supplied by MARCO 8/21.** This row's own trigger read *"Q3 construction starts/claims show no raid-linked layoffs → drop to … | Narrow demand slice only; supply side excluded by design |
| 12 | **Public-sector employment** *(renamed from "DOGE / federal" 2026-08-07, Will-approved — **rename, NOT a new vector**, so the /75 denominator is unchanged and no published convergence figure moves)* | **Scope widened to state + local, because July's largest single sector loss landed outside the old federal scope: government −53K, of which local … | Independent but spent as a *cyclical* vector |
| 13 | Claims / shadow gap | **203K w/e Aug 22, 4-wk MA 205,500** [DOL/FRED, obs 2026-08-22, pulled 8/27 10:31 ET]. … | Independent (realization layer) |
| 14 | Staffing canaries | **CANARY TRIPLE COMPLETE 3-for-3 RECOVERY — the pre-committed drop-to-1 condition FIRED (KFRC graded 7/31).** MAN Q2 (7/16) RECOVERY (rev +8% beat, … | Company tier ≠ industry (L-01) — **but this time tier and industry AGREE** (TEMPHELPS expanding), which is what makes 3-for-3 weightier than L-01's failure case |
| 15 | Hormuz hiring freeze | **STALE PRICE FIXED 7/9:** truce COLLAPSED 7/7→7/8 (US struck 80+ targets, Iran hit tankers/bases); Brent spiked $78.82 (+6.28%, 7/8), settled **$76.01** `[STALE 2026-07-09 — BRENT owns the live price; do NOT … | BRENT-owned premise |
| 16 | Temp employment (industry) | **TEMPHELPS 2,505.0K (Jul, +3.4K; June revised UP 2,499.2→2,501.6K)** — 4 straight monthly gains, +25.1K over 5 months. … | Overlaps v14 read; industry series is canonical (L-01) |

---

## [COLD] CONVERGENCE MATRIX — shape of the remaining bearish core (8/7)

*Anchor `matrix-bearish-shape` · moved 2026-09-02 from `STATUS.md` L55 · VERBATIM.*

**Shape of the remaining bearish core (rewritten 8/7 — three of the four legs it listed on 8/5 are gone):** (a) 🔴 **Measurement risk — now the LARGEST leg.** Revisions compounding (−74K → −103K), May cut 109K across two vintages, …  *[carried: −23 · 2.0% · 1.1%]*

---

## [COLD] CROSS-DOMAIN CONTEXT (MARCO-owned supply side — not in LABOR score)

*Anchor `cross-domain` · moved 2026-09-02 from `STATUS.md` L57-61 · VERBATIM.*

### CROSS-DOMAIN CONTEXT (MARCO-owned supply side — NOT in LABOR score)

**ICE / immigration supply shock — the signature FIRED AGAIN in July, 2nd consecutive month:** LF **−264K** (after −720K in June), **LFPR 61.4%** (−0.7pp since January), U-3 mechanically down to 4.1%. …  *[carried: −23]*

---

---

## [COLD] SIGNAL DASHBOARD — full section (per-release evidence + primary citations)

*Anchor `signal-dashboard` · moved 2026-09-02 from `STATUS.md` L63-89 · VERBATIM.*

## SIGNAL DASHBOARD  ·  ⚠️ **This header used to read "all verified vs primaries unless tagged." That claim was FALSE for a month** — the ISM Svs June row was two secondary web reads under a `[CONF]` tag (→ L-12). **A header asserting a verification standard the rows don't meet is worse than no header**, so the standard now lives per-row: **`[CONF]` = a NAMED PRIMARY; anything else says what it is.** Rows re-audited 2026-08-05.

| Indicator | Value | Source | Status |
|---|---|---|---|
| 🔴 **NFP July** | **−23,000** — *"Total nonfarm payroll employment changed little in July (-23,000), following an average monthly gain of 34,000 over the prior 12 months"*; private **+30K**, government **−53K** | [CONF] **BLS USDL-26-1291**, *Employment Situation — July 2026*, 8:30 ET 2026-08-07, **primary retrieved direct** (bls.gov 403s WebFetch; UA-header curl succeeds — see BUILD_DEBT) | 🔴 **first negative of the cycle** |
| 🔴 **Revisions May/Jun** | **net −103,000** — *"May was revised down by 66,000, from +129,000 to **+63,000**, and… June was revised down by 37,000, from +57,000 to **+20,000**"* (verbatim). … | [CONF] BLS USDL-26-1291 primary | 🔴 regime **compounding** |  *[carried: −23 · +20K]*
| **U-3 / U-6 July** | **4.1%** (↓0.1; unemployed 6.9M) / **7.9%** (flat) | [CONF] BLS USDL-26-1291 | ⚠️ **NO-SIGNAL per L-06** — see LFPR row |
| **LFPR / EPOP July** | **61.4%** / **58.9%** — BLS: *"changed little"*; *"Since January, the labor force participation rate declined by **0.7 percentage point**"*; LF **−264K** (2nd straight monthly shrink after −720K); unemployed **−178K** | [CONF] BLS USDL-26-1291 | 🔴 supply — **U-3 fell on the denominator again** |
| **AHE July** | **$37.62** (+2 cents MoM); **+3.2% YoY** — *decelerated from 3.5%*. Production/nonsupervisory $32.40 (+4c). **June level revised $37.64 → $37.60** | [CONF] BLS USDL-26-1291 | ⬇️ **supersedes my published 3.5% → 1c packets sent CARL/HENRY 8/7** |
| Workweek July | **34.3 unchanged**; mfg 40.4 unchanged, **overtime −0.1 to 3.1 hrs** | [CONF] BLS USDL-26-1291 | 🟡 — hours did **not** confirm the payroll drop (mfg OT the only tick down) |
| **LT unemployed July** | **1.8M / 25.5% share** — *"edged down over the month… but **changed little over the year**"*. Jobless <5 wks 2.0M, **−344K over the year** | [CONF] BLS USDL-26-1291 | ⬇️ **the YoY-accumulation leg is retracted by the issuer** → vector 6 → 3 |
| 🆕 **Temporary layoff July** | **921,000, +153,000** — *"the number of people on temporary layoff increased by 153,000 to 921,000"*; permanent job losers **little changed at 1.7M** | [CONF] BLS USDL-26-1291 | ⚠️ **LOGGED CARD DEFECT, MOVES NO SCORE.** History defuses it: **Apr 917K, Mar 877K** — inside a range traversed twice this year, off a low June (768K). A bounce, not a break |
| 🔴 **NFP sectors July** | **Local gov't education −50,000** (*"after showing little net change over the prior 12 months"*); **retail trade −19,000** (warehouse clubs/supercenters/general merch **−21K**, gas stations −5K; … | [CONF] BLS USDL-26-1291 primary | 🔴 **the losses are in three sectors I do not vector.** Routed: retail→CARL, financial→REGINALD |
| **Claims w/e Aug 22** | **203K** (−4K); **4-wk MA 205,500** (+1,250). Prior week **w/e Aug 15 revised UP 206 → 207K**. … | [CONF] DOL via FRED ICSA/IC4WSA, obs 2026-08-22, pulled 2026-08-27 10:31 ET (FRED carries the DOL series itself, not a secondary estimate). … | 🟢 ⚠️ **The +1,250 MA rise is 100% the 198K roll-off — NOT information**; both the pivot (198,000) and the size (`(X−198)/4`) were pre-committed in `CATALYSTS.tsv` before the print |
| **Continuing claims w/e Aug 15** | **1,778K** (−18K). Prior **w/e Aug 8 revised DOWN 1,799 → 1,796K**. **Lowest since w/e Jul 18 (1,777K)**; came in under the 1,790K consensus [2ND] | [CONF] DOL via FRED CCSA, obs 2026-08-15, pulled 2026-08-27 10:31 ET | ⚪ **Range-bound 1,777–1,799K holds — this is the THIRD direction-change in five weeks.** Not a trend, and I will not call it one **in either direction**; the 8/13 card's symmetric §5 wording is the standing rule |
| **🆕 ECI Q2 2026 (June ref)** | **Civilian:** comp +0.9% 3-mo SA / **+3.4% 12-mo** (Mar 3.4, Jun-25 3.6); wages +0.9% SA / **3.2%** (Mar 3.4); benefits +1.0% SA / **3.8%** (Mar 3.6). … | [CONF] **BLS USDL-26-1270, "Employment Cost Index — June 2026," 8:30 ET 7/31, Table A transcribed from primary** | 🔴 **composition test → DENY branch**; real wages negative |  *[carried: 1.1%]*
| 🔴 **AHE ↔ ECI wedge — TRAJECTORY CLAIM RETIRED 8/7** | **The June like-for-like pairing STANDS: AHE 3.5% vs ECI private wages 3.1% = 0.4pp.** **What is superseded is "WIDENING"** — July AHE printed … | [CONF] own analysis 8/7 off BLS USDL-26-1270 + **USDL-26-1291** | 🔴→🟡 **mix effect still real; the divergence is no longer growing.** **1c packets sent CARL + HENRY 8/7 with the not-like-for-like caveat on the packet** |  *[carried: 2026-10-30]*
| 🆕 **JOLTS July** | **Hires 5,054K / rate 3.2%** (**−278K MoM**, rate −0.2pp; **June revised 5,348 → 5,332K**); **openings 7,271K / rate 4.4%** (+89K; **June revised DOWN 177K, 7,359 → 7,182K**, rate 4.3%); **quits 3,056K / 1.9%** (from 2.0%); **layoffs & discharges 1,666K / 1.0%** (from 1.1%); total separations 5,072K / 3.2%. **Industry (BLS text): hires −188K in professional & business services; openings +76K durable-goods mfg; the hires rate fell at establishments with 5,000+ employees** | [CONF] BLS *Job Openings and Labor Turnover — July 2026*, released 2026-09-01 10:00 ET; **levels+rates independently re-pulled by me from FRED JTSHIL/JTSTSL/JTSJOL/JTSQUL/JTSLDL + JTSHIR/JTSJOR/JTSQUR/JTSLDR/JTSTSR**, which carry the BLS series itself. **June revision confirmed at FRED before I accepted the relay's figure** | ⬇️🔴 **REVERSAL** (openings↑ hires↓ quits↓) / 🟢 (layoffs 1.0% — firing side went quieter). ⚠️ **Per the 9/4 map §2 this is PARTIALLY dependent on CES — the independent content is the rates as shapes, not the level** |
| 🆕 **ADP July** | **+44K** (cons 70K = MISS; weakest since January); **June revised 98→95K**; services +47K / goods **−3K**; **edu/health +36K = 82% of the total**; financial +10K; P&BS +9K; info +5K; other +6K; **T&T&U −8K; … | [CONF] ADP National Employment Report, PR release 2026-08-05 | 🟡 **LOGGED ONLY — card §2c pre-committed NO re-grade.** Breadth is the story: one sector carried 82% |  *[carried: 4%]*
| 🔴 **ISM Mfg August** | **PMI 54.6** (−1.0 from 55.6; **8th consecutive month of expansion**); 🔴 **Employment 51.2** (−1.6 from 52.8 — **2nd straight month in expansion after a 33-month contraction streak**). Demand legs all softened: **New Orders 53.7 (−3.0), Backlog 51.8 (−3.2), Imports 52.5 (−3.2)**; **Prices 71.1 (flat)**; Supplier Deliveries 59.3 (slower). *July for reference: PMI 55.6, Employment 52.8 (+3.1 from 49.7), highest PMI since May-2022* | [CONF] **ISM® August 2026 Manufacturing PMI® Report, released 2026-09-01 10:00 ET, issuer's own release** (July release, PRIMARY, retrieved 8/5) | 🔴 **The docketed "≥50 a 2nd month" leg FIRES — streak break HOLDS, and it runs AGAINST my book.** LAB-06 already ❌ FALSIFIED 8/3 on this series. ⚠️ **Employment DECELERATED while staying >50** — noted, not scored |
| 🔴 **ISM Svs — Jul GRADED 8/7 (owed since 8/5); Jun row corrected 8/5** | **JULY: PMI 54.1** (+0.1, 25th straight month expanding); 🔴 **Employment 47.4** — *"returned to contraction territory after only one month in expansion with a reading of 47.4 percent, a 3.8-percentage point … | **[CONF] ISM July + June Services PMI releases, PRIMARY** | 🔴 (emp — **back in contraction**) / 🟢 (demand — activity and orders both accelerated). … |  *[carried: 52.8]*
| 🆕 **Challenger July** | **33,429 — lowest monthly total in TWO YEARS** (−27% m/m from 45,849; −46% YoY from 62,075). … | [CONF] **Challenger, Gray & Christmas July 2026 report, issuer's own release** | 🟡 (level, at floor) / 🔴 (AI share persists) — **card §2e Band B → vector 5 holds at 4; level <40K → vector 2 → 1** |  *[carried: 4%]*

*Not currently tracking (last refresh ≤2026-06-23 — demoted 7/24 as monthly-slow):* staffing tier-split, **ASA index**, CPS response. …

---


---

## [COLD] KEY THRESHOLDS — rows that fire nothing (diagnostic / published-only / no-fire)

*Anchor `thresholds-nofire` · moved 2026-09-02 from `STATUS.md` L100, L105-106, L112 · VERBATIM.*

| 🆕 **Constant-participation U-3 — DIAGNOSTIC ONLY, fires nothing** | **5.13%** [July] vs a headline **4.1%** — a **1.03pp** gap, widened monotonically from +0.08pp in January | Holds LFPR at its **Jan-2026** level (62.1%) and re-computes: **the anchor is BLS's own** — USDL-26-1291 says *"Since January, the LFPR declined by 0.7 percentage point"* — not one I picked. … | 🔴 **Published as a diagnostic so the composition effect is visible — deliberately NOT wired to any trigger, and consumers must carry the upper-bound caveat with the number** |
| 🆕 **AHE 12-mo (composition-CONTAMINATED gauge — read beside ECI, never alone)** | **3.2%** [July] (from 3.5%) | **No threshold registered, deliberately** — L-12/ECI established AHE is a mix artifact, so a level on it fires nothing. Carried because it is **published and consumed** (CARL, HENRY) | **1c on any change** — done 8/7 |
| 🆕 **Real earnings (July, printed 8/12)** | **Real AHE all employees −0.1% MoM, −0.2% YoY**; real average *weekly* earnings **+0.1% YoY** (a +0.3% workweek does the work). … | **No LABOR-registered item fires on today's CPI** — checked on the letter, not assumed. AHE deliberately carries no threshold, so a price print cannot move a LABOR trigger | **CARL input (real income), routed as data.** ⛔ **DO NOT NET against the ECI-based "real private wages −0.4% YoY"** — different deflator, universe (all employees vs private wages+salaries), and frequency. … |
| **Government payrolls (TOTAL)** | **−53K** [July], of which **local gov't education −50K** — the **5.7th percentile** of monthly changes since 1990 | 🔴 **BD-17 RESOLVED 2026-08-07 — NO fire threshold, and the data is why.** Government payroll declines carry **no cycle information**: ≤−25K/month separates recession from non-recession by **+5.0pp**; ≤−50K by … | ✅ **Vector 12 RENAMED "public-sector employment" (Will-approved) — no matrix re-base, /75 denominator unchanged.** The July loss is a **fiscal** … |

---

## [COLD] FED TRAP & THESIS — superseded lede + rotation pointer

*Anchor `fed-trap-history` · moved 2026-09-02 from `STATUS.md` L118, L120 · VERBATIM.*

**Thesis state: SUPERSEDED — see the 8/7 header and the grade below.** *(The Jul-2 "stagflation mix sharpened / Fed holds off on hiking" lede and the 7/24 "benign claims are hawkish fuel" block were both **struck as WRONG ON …
> 🔒 **Retired rate-path annotations + the 8/7 policy grade ROTATED 2026-09-01** (read-cap) → `domain/sources/STATUS_ROTATION_2026-09-01_readcap.md` (verbatim, CRC32 `6ec07274`). **Live residue, the only part that governs:**

---

## [COLD] DANGER WINDOW Q3 2026 — graded rows

*Anchor `danger-window` · moved 2026-09-02 from `STATUS.md` L126-135 · VERBATIM.*

## DANGER WINDOW: Q3 2026 (rows graded through **2026-09-01**)

| Window | Cohort / Test | Status |
|---|---|---|
| ✅ 🔴 **Sep 1 — FIRED & GRADED SAME DAY (both, off pre-committed letters)** | **JOLTS July** *(printed a day EARLY vs my `~Sep 2` model)* · **ISM Mfg August** | **JOLTS: ZERO of 4 bands fired** — hires 5,054K (`5,054 − 5,000 = 54K` above T-10) · layoffs 1.0% (`1.2 − 1.0 = 0.2pp` FURTHER away) · openings 7,271K · hires ≪5,500K. **NET `5,054 − 5,072 = −18K`, 3rd straight negative; v4 HOLDS at 3.** **ISM Mfg emp 51.2 = 2nd month ≥50 ⇒ streak break HOLDS (against my book); v3 holds at 2 pending Svs 9/3.** |
| ✅ **Aug 28 — FIRED & GRADED** | **QCEW preliminary benchmark = −79,000** (private −178K, gov't +99K) [CONF BLS USDL-26-1425] — **card §4 BAND E**; vector 8 **4 → 2**, LAB-08 live **15% → 4%**. ⛔ **LAB-08 NOT resolved — the FINAL lands Feb-2027 and scores as-made 65%.** | ✅ **RESOLVED — the largest scheduled item in the book, graded off frozen text** |
| ✅ 🔴 **Aug 5 – Aug 7 — ALL GRADED 8/7 (2 rows collapsed)** | ISM Svs July · Challenger July · claims w/e Aug 1 · **NFP July + U-3** | **ISM Svs emp 47.4** → 8/5 pre-commitment fired, vector 3 holds at 2 ✅ · **Challenger 33,429 / AI 32.8% #1 5th mo** → v5 holds at 4, v2 → 1 · **claims 199K / MA 198,750** Band B, **CC 1,801K first rise in 5 … |  *[carried: 4.1% · 61.4% · −23 · +20K · −264K · 4%]*

---


---

## [COLD] PREDICTIONS — resolved tables + the 8/07 rotation pointer

*Anchor `predictions-resolved` · moved 2026-09-02 from `STATUS.md` L146, L148, L150-159 · VERBATIM.*

*(LAB-13 resolved this session — moved to the resolutions table below.)*
> 🔒 **The 8/07 worked block ROTATED** → `domain/sources/STATUS_ROTATION_2026-09-01_readcap.md` (verbatim, CRC32 `6ec07274`) — **for a reason beyond bytes: it named LAB-08 and LAB-10 as flagged, and both have since moved.** C2-0's own warning is that *a sweep whose worked example is a stale list teaches the answer instead of the procedure* — in a boot-loaded file. It was becoming the defect it prevents.
**Resolved this session (2026-08-07):**

| ID | Prediction | Outcome |
|---|---|---|
| 🔴 **LAB-10** | **70%+ of layoff cohort shows revenue decel** | ❌ **FALSIFIED 2026-08-07** — Band C. … |  *[carried: 0.275]*
| 🔴 **LAB-13** | **Healthcare turns net-negative by July NFP** | ❌ **FALSIFIED 2026-08-07**, graded off the frozen card `docket/graded/GRADING_CARD_20260803_to_0807.md` §2f, band **">+15K → falsified cleanly"**. … |
| 🔴 **LAB-06** | **ISM Mfg Employment <50 through 2026** | ❌ **FALSIFIED 2026-08-03**, graded 8/5 off the frozen pre-registered card `docket/graded/GRADING_CARD_20260803_to_0807.md` §2a, **Band A (≥50.0)**. … |  *[carried: 52.8]*
| **LAB-17** *(prior session 7/31 — kept for context)* | **WARN-cohort claims test: 4-wk MA ≥235K on any print by Aug 6** | ❌ **FALSIFIED Jul 31**, graded off the frozen pre-registered card. Claims w/e Jul 25 = **197K** vs the required **≥327K**; 4-wk MA **202,750**, i.e. **32,250 further from** the bar and falling. … |

**Earlier resolutions (context):** LAB-15 ❌ (NFP May +172K), LAB-14 ❌, LAB-09 ✅, LAB-07 ✅, LAB-05 ❌, LAB-01 ❌ — see ledger.

---

## [COLD] EXIT RULES — base-rate rotation pointer + I-1 8/5 verdict

*Anchor `exit-rules-history` · moved 2026-09-02 from `STATUS.md` L174, L176 · VERBATIM.*

  🔒 **Base-rate derivation ROTATED 2026-09-01** (read-cap) → `domain/sources/STATUS_ROTATION_2026-09-01_readcap.md` (verbatim, CRC32 `6ec07274`) — spec-comparison table, why-v1-broke, the rejection of BD-11's preferred fix, design notes, struck v1. **BD-11 discharged; consumed derivation.** **Adopted row retained: v2 base-rates 58.7% overall / 65.0% in a genuine 2015–19 expansion / 0.0% across the 2025–26 freeze — it fires when the thesis is wrong and stays silent when it is right, the test v1 failed.** 🔴 **LEG C is JOLTS *NET*, not gross hires — a gross flow cannot speak to a net count.**
  - ⚠️ **I-1's 8/5 verdict STANDS on the letter and is NOT re-opened** (2 of 4 landed: hires 5,348K ✓, ISM Mfg 52.8 ✓). …

---

## [COLD] MONITORING CALENDAR — graded rows

*Anchor `calendar-graded` · moved 2026-09-02 from `STATUS.md` L186-187 · VERBATIM.*

| 🔒 **Jun 30 – Aug 28 — 7 graded rows ROTATED 2026-09-01** | read-cap | → `domain/sources/STATUS_ROTATION_2026-09-01_readcap.md` (verbatim, CRC32 `6ec07274`); outcomes also summarised in DANGER WINDOW |
| ✅ 🔴 **Tue Sep 1, 10:00 ET — GRADED SAME DAY** | **JOLTS July** *(docket modeled `~Sep 2`; it landed 9/1 — the modeled-date re-verify rule at B5 is what this row is now evidence for)* + **ISM Mfg August** | 🔒 **Graded band-by-band off the letters pre-committed in `CATALYSTS.tsv`. JOLTS: NO BAND, NO ACTION** — all four un-hit, and the layoffs-rate bar moved *away*. **Corrected-basis NET −18K (3rd consecutive), v4 HOLDS at 3, NET bands now pre-registered for JOLTS Aug (~Oct 6).** **ISM Mfg emp 51.2, 2nd month ≥50 ⇒ "streak break holds" leg fires; v3 pending ISM Svs Thu 9/3.** |

---

## [COLD] PENDING INPUTS — rotation banner + discharged windows

*Anchor `pending-history` · moved 2026-09-02 from `STATUS.md` L195, L199-202 · VERBATIM.*

> 🔒 **Session narrative rotated 2026-08-28 (PROME Wave 2, Will-approved). Full pre-rotation `STATUS.md` — byte-for-byte, contiguous, zero edits, CRC32 `7727ec7e` — at `domain/sources/STATUS_PROSE_ARCHIVE_2026-08-28_pre-rotation.md`. Cite it as history; this file is canonical for every live figure.**
| 7/27–8/17 | HENRY · NEXUS ×2 · PROME ×7 · MARCO ×3 · RED · BOND · CARL · DAEDALUS ×2 · WALTER ×2 · Will 8/6 | ✅ **ALL DISCHARGED.** Still load-bearing: HENRY's 3.5% ECI band adopted; PROME's 7/31 rulings implemented; NEXUS Amendment 10 installed; **L-15 applied** (a non-terminal token replayed one signal six times) |
| 8/27 | RED ×3 | ✅ Discharged on the merits; **the finding was the FILING** — work done ≠ item closed (→ L-22) |
| **8/28** | **RED · DAEDALUS ×2 · LIQUID · WALTER ×7 SIGs** | ✅ **ALL DISCHARGED AND FILED THIS SESSION**, both lanes verified EMPTY by `ls`. Drove: **BD-22 discharged** (boot.py mtime → content-vintage, `--glob '**/*.tsv'` because the prescribed default covered 2 of my 4 ledgers) · **R1 boot line inserted as B5c** · L-24 (4 mechanism claims, 3 peer-caught) · **PROME's show-the-division ruling encoded in OUTPUT RULES** |
| **9/1** | **WALTER ×4 SIGs** (`-20260901-007` ISM Mfg Aug · `-20260901-008` JOLTS Jul · `-20260828-039` Q2 GDP 2nd est · `-20260828-040` UMich Aug final) | ✅ **ALL DISPOSITIONED AND FILED THIS SESSION**, both lanes verified EMPTY by `ls`. Two **acted** (both graded at my own instruments off my own pre-committed letters — PROME graded nothing on my behalf); two **info-only**, terminal per L-16. ⏱️ **Checked rather than assumed: -039/-040 were dispatched 8/28T21:5xZ ≈ 17:5x ET, ~2.5h AFTER my 8/28 closeout at ~15:2x ET — they did NOT sit unseen through a session, and the PENDING-INPUTS "both lanes empty at rotation" claim above was true when written** |

---

## [COLD] NEXT SESSION PICKUP — rotation banner + closed items 0, 0b, 7

*Anchor `pickup-closed` · moved 2026-09-02 from `STATUS.md` L207, L209-210, L217 · VERBATIM.*

> 🔒 **Session narrative rotated 2026-08-28 (PROME Wave 2, Will-approved). Full pre-rotation `STATUS.md` — byte-for-byte, contiguous, zero edits, CRC32 `7727ec7e` — at `domain/sources/STATUS_PROSE_ARCHIVE_2026-08-28_pre-rotation.md`. Cite it as history; this file is canonical for every live figure.**
0. 🔒 **9/1 SLATE CLOSED — both catalysts graded same-day off pre-committed letters, and the pre-commitments did the work.** **(a) JOLTS July** (a day early): zero of four bands fired; corrected-basis NET `5,054 − 5,072 = −18K`, third consecutive negative; **v4 HOLDS at 3** because no registered band fired (L-18). **(b) ISM Mfg Aug employment 51.2**, 2nd month ≥50 ⇒ streak break HOLDS — **against my book**; **v3 holds at 2 pending ISM Svs Thu 9/3**, whose branch is pre-committed above. ⛔ **No score moved on either print. That is the correct outcome, not an absence of work.**
0b. 🔒 **8/28 CLOSED — both slate items graded off frozen text, band by band.** **(a) QCEW prelim −79,000** (private **−178,000**, gov't **+99,000**) [CONF BLS USDL-26-1425] …  *[carried: 4% · 65%]*
7. ✅ **STATUS ROTATED 2026-08-28** from **145,676 B (269% of the ~54,250 B Read cap — my own boot was truncating it silently)**. Prose only; every live threshold, figure, pointer and corrected-claim sentinel retained and re-verified.

---

## [COLD] Superseded by the 2026-09-02 session

*Anchor `session-superseded-20260902` · moved 2026-09-02 at the C1 write-back · VERBATIM, exactly as they stood at the end of the 9/1 session.*

### Header stamp — 2026-09-01 session (`STATUS.md` L2, post-split L2)

**Last Updated:** 2026-09-01 ~20:5x ET *(session LIVE — PROME-spawned, WQ-146 summoned-owner slot for the 9/1–9/4 catalyst cluster)* · 🔒 **BOOT: `spine_check` PASS on claims (init obs 2026-08-22 == FRED, cont 2026-08-15 == FRED); both inbox lanes drained to EMPTY, verified by `ls`.** 🔴 **TODAY'S GRADE ×2, both off pre-committed letters. ① JOLTS July printed 9/1 — a day EARLIER than my docket modeled (`~2026-09-02`). ZERO of four pre-committed bands fired: hires 5,054K is 54K ABOVE the T-10 5.0M arm line · layoffs rate 1.0% is 0.2pp FURTHER from the ≥1.2% escalate bar · openings 7,271K vs the <7,000K floor · hires nowhere near 5,500K. Corrected-basis NET (BD-11) `5,054 − 5,072 = −18K`, THIRD consecutive negative month (May −8K, Jun −5K rev). **VECTOR 4 HOLDS AT 3** — no registered band fired and I will not move a score on a measure whose bands were never written (L-18). ② **ISM Mfg Aug employment 51.2** = 2nd consecutive month ≥50 ⇒ the docketed *"≥50 a 2nd month"* leg fires, the 33-month streak break HOLDS — **bearish-thesis-negative, recorded as such**. **Vector 3 holds at 2 for two more days**: its drop-to-1 needs BOTH ISM >50 in the SAME month and Services prints Thu 9/3. 📌 **Forward: Wed Sep 2 OPM RIF final rule effective · Thu Sep 3 claims (LAB-17 read PRE-REGISTERED, frozen bands, roll-off `(X−200)/4`) · 🔴 Fri Sep 4 NFP August. READ `docket/INDEPENDENCE_MAP_20260904_NFP.md` FIRST: nine legs are FOUR evidence types.**

### C2-0 stale-high-confidence sweep — the 2026-09-01 run + the 8/07 rotation pointer

> 🔴 **C2-0 STALE-HIGH-CONFIDENCE SWEEP — RE-RUN 2026-09-01. RESULT: ZERO ROWS TRIP IT.** Re-derived from `workbook/PREDICTIONS.tsv` rather than read off a list, exactly as C2-0 requires. The four OPEN rows are **LAB-03 7% · LAB-12 30% · LAB-08 4% live · LAB-11 50%** — **all below the ≥60% bar, so gates #3/#5/#12/#13 have nothing to sweep.** *(LAB-08 scores AS-MADE at 65%; its 4% is the live diagnostic and the sweep bar reads the live value.)*

### EXIT RULES — KELYA Jul-2 print narrative

- **KELYA position rules** — TRADE.md §2-3. Jul-2 print: §2 re-arm letter technically fired (NFP <100K + revisions no longer trending up) but U-3 leg inverted (fell, supply-artifact) and market shrugged (KELYA $13.00 −0.84%). …

### BOTTOM LINE — 2026-09-01 (the 9/1 double grade)

**🟠 Two catalysts landed on 9/1 and neither moved a score — because both were pre-committed, and the honest reading of both runs against my own book.**

**JOLTS July** (which printed a day earlier than my docket modeled). **Zero of four pre-committed bands fired:** hires **5,054K** is `5,054 − 5,000 = 54K` *above* the T-10 arm line; the layoffs rate printed **1.0%**, moving `1.2 − 1.0 = 0.2pp` *further* from the escalate bar that was one of only two live revival paths for the break thesis; openings **7,271K**; hires nowhere near 5,500K. **Vector 4 holds at 3.**

**The one genuinely new thing, stated with its discounts attached.** On the corrected BD-11 basis, **JOLTS NET = `5,054 − 5,072` = −18K, the third consecutive negative month** (May −8K, Jun −5K revised). Base-rated by me at the primary across **308 months**: NET ≤0 in **72 = 23.4%**, runs of ≥3 consecutive = **6**, and **the previous one ended September 2010**. ⚠️ **But the five prior runs are really two episodes, and my own frozen independence map says JOLTS is ratio-estimated to CES — so this is *partly circular* with the negative payrolls it looks like it confirms.** The licensed independent content is the **rates as shapes**: openings rate up 4.3→4.4 while the hires rate fell 3.4→3.2, hires-per-opening `5,054/7,271 = 0.695` vs `5,332/7,182 = 0.742`. **Matching is deteriorating while the firing side goes quieter — a deeper low-churn freeze, not a layoff wave.**

**ISM Mfg August employment 51.2** is a second consecutive month ≥50, so the docketed *"streak break holds"* leg fires. **That is bearish-thesis-negative and it is recorded as such.** Vector 3 cannot move until **ISM Services prints Thu 9/3** — its drop-to-1 needs both surveys >50 in the *same* month — and that branch is now written down before the figure.

**Nothing is near a threshold on the realization layer.** Claims **203,000** (w/e Aug 22), 4-wk MA **205,500**, CC **1,778K**. T-01 is 44,500 away on the MA basis, T-02 97K, Kill B 0 of 5.

**Next — 🔴 Wed Sep 2 OPM RIF final rule effective (a MECHANISM change; vector 12 moves only if separations appear in UCFE or the federal payroll line, never on coverage) · Thu Sep 3 claims, LAB-17 read PRE-REGISTERED with the roll-off term `(X − 200)/4` computed before the level · 🔴 Fri Sep 4 NFP August — read `docket/INDEPENDENCE_MAP_20260904_NFP.md` FIRST and grade by the FOUR evidence types, not the nine legs.** ⛔ **The attribution bar still stands: no agent carries a demand-vs-supply attribution from me before 9/4.**

---

### PENDING INPUTS + NEXT SESSION PICKUP — as they stood at the end of the 2026-09-01 session

| — | — | 🟢 **NOTHING UNPROCESSED. Both lanes verified empty by `ls` at 2026-09-01 ~20:5x ET.** |

1. 🔴 **OWED — base-rate the CORRECTIVE, not just the original.** The 8/07 reprice cut 65% → 35% *citing my 0-for-4 threshold record as its reason* — and **35/4 = 8.75×** the honest post-print 4%. **Even the corrective was anchored to the number it corrected** (L-25). My scoreboard scores only AS-MADE values, so a mis-calibrated repricing step is **wrong on no ledger anywhere.** Add a scored CORRECTIVE column at the next §D pass.
2. 🔴 **ATTRIBUTION STILL OPEN. No agent may carry a demand-vs-supply attribution from me before NFP Fri Sep 4.** A benchmark restates the **March-2026 level**; it says nothing about which side moved. Warsh adopting the supply read is **testimony, not measurement**.
3. 🔴 **NFP 9/4 — read the INDEPENDENCE MAP first:** `docket/INDEPENDENCE_MAP_20260904_NFP.md`. Today RED-22, Warsh's cites and LAB-08 were **one chain read three times**. Grade 9/4 by evidence **TYPES**, not desks.
4. 🔒 **LAB-17 claims read for Thu 9/3 is PRE-REGISTERED** in the same docket file — frozen letter, thresholds before the number.
5. ✅ **v4 PRE-COMMITMENT DISCHARGED 9/1** — graded NET-first as written, HOLDS at 3, and **NET bands are now PRE-REGISTERED for JOLTS August (~Oct 6)** so the next read is gradable rather than improvised: **NET >0 ⇒ v4 → 2 · NET ≤0 a 4th month ⇒ v4 → 4 · NET ≤0 but hires rate back ≥3.4% ⇒ HOLD 3.** ⚠️ **v3's ISM-Svs branch is likewise pre-committed above, before Thursday's figure.** The **un-vectored channel** (local-gov't education **−50,000**) stays open; a 16th vector re-bases the /75 denominator, so not mid-session.
6. **Live build debt:** **BD-19** (standing re-datable weekly-claims card template) · **BD-21** (card branch-partition check, L-18) · **BD-23** (nothing in my boot reads the regulatory record — Federal Register API, OPM+DOL two-agency poll). **BD-02, BD-18, BD-20, BD-22, BD-24 discharged.**

---

### Rows compacted at the 2026-09-02 write-back (verbatim originals)

**Header stamp — first 9/2 draft, superseded same session** (`STATUS.md` L2):

**Last Updated:** 2026-09-02 ~20:2x ET *(session LIVE — PROME-spawned, WQ-156 summoned-owner slot for the 9/3–9/4 catalyst cluster; continues the 9/1 WQ-146 session)* · 🔒 **BOOT: `spine_check` PASS (init obs 2026-08-22 == FRED, cont 2026-08-15 == FRED) · B5b: zero unconsumed cards at boot · corrections rc=0 · WALTER lane EMPTY by `ls`.** 📐 **STATUS HOT/COLD SPLIT EXECUTED TODAY (BD-25 discharged): 53,375 B → this file; the cold half is `STATUS_DETAIL.md`, verbatim, census-verified 232/232 lines.** 🔒 **TWO FROZEN CARDS WRITTEN TONIGHT, BEFORE THE FIGURES: `docket/GRADING_CARD_20260903_ISM_SERVICES.md` (Svs employment: >50 ⇒ v3→1 · =50.0 ⇒ HOLD · <50 ⇒ HOLD; boundary case closed) and `docket/graded/GRADING_CARD_20260904_NFP.md` (pre-computed: freeze-thaw LEG A needs Aug **≥+303K** · T-06 U-3 leg needs **≥4.3%** · **T-03 fires on a FLAT EPOP 58.9** because the 3-mo referent rolls to May 59.2 · T-04 at ≤58.8 · LEG B needs ≥59.2 · Kill A CANNOT fire at any value).** 📌 **No score moved today — no labour data printed.** 🔴 **Forward: Thu 9/3 08:30 claims w/e Aug 29 (letter frozen at `docket/INDEPENDENCE_MAP_20260904_NFP.md` §4, roll-off term `(X−200)/4`) + 10:00 ISM Svs · 🔴 Fri 9/4 08:30 NFP August.**

**PREDICTIONS — LAB-12 row as it stood 9/1** (`STATUS.md` L99):

| LAB-12 | U-3 ≥5.0% Q3-Q4 | **30%** | Q3-Q4 | 🔴 **8/7 — ITS THESIS IS NOW SATISFIED ON A COMPOSITION-CONTROLLED BASIS WHILE ITS LETTER IS NOWHERE NEAR, AND I AM NOT TOUCHING IT.** Headline U-3 is **4.1%** and falling; **constant-participation U-3 is … | 🔒 **9/1: CONSIDERED AND HELD AT 30% — recording the non-move so it is distinguishable from not having looked.** JOLTS July cuts both ways and neither leg is denominated in U-3: hires rate 3.4→3.2% and NET −18K are mildly supportive; **layoffs rate 1.1→1.0% is against** (you do not get to 5.0% without the firing side waking), and ISM Mfg employment 51.2 is against. **Per L-06 the letter of this prediction is graded on a gauge I have demoted**, so a JOLTS flow read cannot move it in either direction. No reprice ⇒ L-25's write-it-twice rule does not fire.

**MONITORING CALENDAR — OPM RIF row as it stood 9/1** (`STATUS.md` L129):

| 🟡 **Wed Sep 2** | **OPM Final Rule "Reduction in Force" takes effect** (FR doc 2026-15665) | 🔒 **PRE-COMMITTED 9/1, before the date: this is a MECHANISM change, not a threshold, and vector 12 does NOT move on the rule alone.** BD-17 measured that government payroll declines carry no cycle information (≤−50K/mo separates recession from non-recession by **+0.0pp**). **It moves only if separations SHOW UP in UCFE (federal-employee UI, baseline 444) or the federal payroll line (baseline +2K [June]).** ⛔ **Press coverage of the rule is not evidence of separations** |

**PENDING INPUTS — CARL row, first 9/2 draft** (`STATUS.md` L141):

| 9/1 | **CARL** (`ANSWER — yes it reconciles… a benchmark is a LEVEL revision, not a path claim`) | ✅ **DRAINED 2026-09-02.** INFO, **STILL LIVE**: his caveat is adopted verbatim — the QCEW retail **−154.6K** is a **base correction, not an acceleration signal**, and no LABOR figure moves on it. His one free ask is **answered and closed** (packet `AGENTS/CARL/inbox/2026-09-02_from-LABOR_…`): **prebmk.t01 publishes at supersector level only — "Retail trade" is the finest retail cut there is, no warehouse-clubs/supercenters line. Stop looking monthly.** |

**PICKUP item 1, first 9/2 draft** (`STATUS.md` L149):

1. 🔴 **THE SLATE IS FROZEN — grade off the cards, in this order.** Thu 9/3 **08:30 claims w/e Aug 29** → `docket/INDEPENDENCE_MAP_20260904_NFP.md` §4 (compute `(X−200)/4` **before** the level; report roll-off separately). Thu 9/3 **10:00 ISM Services August** → `docket/GRADING_CARD_20260903_ISM_SERVICES.md`. Fri 9/4 **08:30 NFP August** → `docket/graded/GRADING_CARD_20260904_NFP.md`, and read **§1–3 of the independence map first**: grade by the **four evidence TYPES**, never by leg or desk count.

**PICKUP item 4, first 9/2 draft** (`STATUS.md` L152):

4. 🔴 **OWED — base-rate the CORRECTIVE, not just the original.** The 8/07 reprice cut 65% → 35% *citing my 0-for-4 threshold record as its reason* — and **35/4 = 8.75×** the honest post-print 4%. **Even the corrective was anchored to the number it corrected** (L-25). Carried unchanged from 9/1; not started.

**PICKUP item 6, first 9/2 draft** (`STATUS.md` L154):

6. **Live build debt:** **BD-19** (standing re-datable weekly-claims card template) · **BD-21** (card branch-partition check, L-18) · **BD-23** (nothing in my boot reads the regulatory record) · 🆕 **BD-26** (no payrolls vector in the matrix — declared on the NFP card §5, to be settled in a dedicated re-grade session, **never on print day**). **BD-25 DISCHARGED 9/2** (STATUS hot/cold split).

**BOTTOM LINE "What changed", first 9/2 draft** (`STATUS.md` L160):

**What changed.** `STATUS.md` went **53,375 B → 24,7xx B** (measured, `PROME/tools/measure.py`), against a **binding 32,550 B** read-cap budget it had been **164%** of — an over-cap boot surface returns a **partial file with no error**, so the tail (NEXT SESSION PICKUP, BOTTOM LINE) was the part at risk of never being read. The cold half is `STATUS_DETAIL.md`: verbatim, contiguous, census-verified **232 of 232 source lines** accounted for exactly once. **No figure was changed in the move.**

**BOTTOM LINE "The three letters", first 9/2 draft** (`STATUS.md` L162):

**The three letters.** Claims w/e Aug 29 was already frozen (`INDEPENDENCE_MAP` §4, bands + the `(X−200)/4` roll-off term). ISM Services and NFP were not, and both are multi-loaded, so both got cards tonight. **The NFP card is where the work is:** it pre-computes that **freeze-thaw LEG A needs ≥+303,000** (the 3-mo-average leg binds, not the headline leg), that **Kill A cannot fire at any August value**, and — the live one — that **T-03 fires on a FLAT EPOP of 58.9%**, because the three-month referent rolls from April 59.1 to **May 59.2**. **That is the closest threshold in the book and it fires on no deterioration at all.**

---

**KEY THRESHOLDS — JOLTS NET row, full 9/1 text** (`STATUS.md` L67):

| 🆕 **JOLTS NET (hires − separations)** *(added 8/7 — the measure BD-11's leg 3 should always have used)* | **−18K** [July: `5,054 − 5,072`]; **Jun −5K** (revised, was −3K); May **−8K**; Apr +177K, Mar +158K | **>0 in both of the 2 most recent reference months = freeze-thaw v2 LEG C** — ✗ **not met, and it moved FURTHER away**: both of the two most recent months are negative and July is the most negative of the three | 🟠 CARL+HENRY. 🔴 **THIRD consecutive negative month. Base-rated by me at the primary over 308 months (2000-12 → 2026-07): NET ≤0 in 72 = 23.4%; runs of ≥3 consecutive = 6; the previous run ended September 2010 — this is the first 3-month run in ~16 years.** ⚠️ **Honest discounts: the 5 prior runs are 2 episodes (2001–03, 2008–10), and JOLTS is ratio-estimated to CES so this is partly circular with the negative payrolls.** The older conditional row still stands unchanged: gross hires rose in 66 months since 2015 and net was ≤0 in only 2 of them (May+Jun 2026) — **July does NOT join that set, because gross hires FELL** |  *[carried: 2.0% · 1.1%]*

---

## [COLD] JOLTS NET — base-rate basis and its discounts

*Anchor `jolts-net-basis` · moved 2026-09-02 from the KEY THRESHOLDS JOLTS-NET row `Fires` cell · VERBATIM.*

🟠 CARL+HENRY. 🔴 **THIRD consecutive negative month. Base-rated by me at the primary over 308 months (2000-12 → 2026-07): NET ≤0 in 72 = 23.4%; runs of ≥3 consecutive = 6; the previous run ended September 2010 — this is the first 3-month run in ~16 years.** ⚠️ **Honest discounts: the 5 prior runs are 2 episodes (2001–03, 2008–10), and JOLTS is ratio-estimated to CES so this is partly circular with the negative payrolls.** The older conditional row still stands unchanged: gross hires rose in 66 months since 2015 and net was ≤0 in only 2 of them (May+Jun 2026) — **July does NOT join that set, because gross hires FELL**

---

---

## `pending-drained-20260902`

**Rotated out of `STATUS.md` 2026-09-04 (read-cap: the hot half hit 32,617 B against the 32,550 B budget after the NFP grade). VERBATIM — no figure changed in the move. Both windows were already DRAINED on 9/3; this is discharged history.**

| Window | From | State |
|---|---|---|
| 9/2 | **PROME** (WQ-159 RULED: T-03 stands, no retune) | ✅ **DRAINED 9/3.** RULING consumed at boot; nothing to edit — T-03 exactly as registered. Card `docket/graded/GRADING_CARD_20260904_NFP.md` item 4 already states the consequence: FLAT Aug EPOP 58.9 fires T-03 tomorrow. Filed → `processed/`. |
| 9/2 | **PROME** (Canada counter-tariffs 9/8 corrected at primary: CA$27.6B, three tiers 15/25/50%, §338+§232 perimeter) | ✅ DRAINED 9/3 — 🔴 **but the "zero hits" claim in this cell was FALSE and I caught it 9/4: `docket/CATALYSTS.tsv:3` carried "~$28B" the whole time.** The 9/3 grep evidently did not cover the TSV. **Figure corrected 9/4 to the primary (CA$27.6B, three tiers 15/25/50%).** Lesson: a self-audit that reports ZERO must name the file set it searched — an unstated perimeter reads as "everywhere." My CATALYSTS row for 9/8 is a WATCH only; ag equipment + pulp & paper are my named US-exporter employment lanes. HAW-21 grades the instrument 9/15. Filed → `processed/`. |

> 🔴 **One live carry-forward was deliberately LEFT on the hot half rather than rotated with these rows:** the Canada cell asserted *"No LABOR surface carried '~$28B' … verified by grep, zero hits."* **That was false** — `docket/CATALYSTS.tsv:3` carried it until 2026-09-04, when the figure was corrected to the primary (CA$27.6B, three tiers 15/25/50%). A correction must not rotate to cold in the same breath as the claim it corrects.

---

## `calendar-graded-20260903`

**Rotated out of `STATUS.md` 2026-09-04 (read-cap: the hot half hit 32,667 B against the 32,550 B budget after the BOND pending row). VERBATIM — no figure changed in the move. Both were graded off frozen cards on 9/3 with no score movement, and both are superseded as "latest print" by the 9/4 NFP grade.**

| Date | Item | Action |
|---|---|---|
| ✅ 🟢 **Thu Sep 3 08:30** | **Initial claims w/e Aug 29** | **206K single / MA 207.2K, CC 1,779K (w/e Aug 22).** INDEPENDENCE_MAP §4 band **186–229K = NO BAND / NO ACTION.** Mechanical `(206−200)/4 = +1.5K` matches realised +1.7K MA move within a prior-week revision. Kill-B 0/5; vector 13 held at 2. **No packet travels; attribution bar unchanged.** |
| ✅ 🟢 **Thu Sep 3 10:00** | **ISM Services PMI August** | **Employment 47.8** (+0.4, 2nd month contraction); Headline PMI 55.4 (§2b NO-ACTION); Business Activity 61.7; New Orders 60.9. Band **<50.0 ⇒ vector 3 HOLDS at 2** (survey layer split). No score moves; no packet travels. Card `git mv`'d to `docket/graded/`. |

---

## `rotated-20260904`

**Rotated out of `STATUS.md` 2026-09-04 — the THIRD rotation that day.** L-27, L-28, LAB-18, LAB-19 and the LAB-12 reprice took the hot half to **33,681 B against the 32,550 B budget**; the header was trimmed 1,380 → 822 B and these two rows moved. **VERBATIM — no figure changed.** Both remain live in substance; only their prose is cold.

**matrix vector 12 (full row incl. the 8/07 rename justification)**

| 12 | **Public-sector employment** *(renamed from "DOGE / federal" 2026-08-07, Will-approved — **rename, NOT a new vector**, so the /75 denominator is unchanged and no published convergence figure moves)* | **1** ⚪ | flat | ✅ **GRADED 9/4 off NFP card §3e: federal payrolls Aug −5K (ex-USPS −3.3K) [Table B-1] vs the ≤−25K T-13 MoM bar ⇒ does NOT fire; v12 HOLDS at 1.** No UCFE check triggered — and per **BD-17** the payroll line alone would not have moved the vector even had it fired. Total government **+35K** (local gov't education +42K). Re-fire needs a new federal RIF authority, **or** a state/local decline that persists 3+ months **and** coincides with an EPOP drawdown — i.e. only when it stops being idiosyncratic |


**PENDING INPUTS 9/4 BOND row (full)**

| 9/4 | **BOND** (reply to my July-revision retraction) | ✅ **CONSUMED 9/4.** BOND grepped **all nine** of its live surfaces: **zero hits** — no BOND surface reasons from a negative July; `KB-BND-112` correctly left as a dated record. 🔴 **Returned a contradiction that is NOT mine to resolve:** two relayed Sept Fed-path figures point opposite ways two days apart — *"Sept HIKE ~65–68% priced"* (BOND STATUS, wires via WALTER 9/1) vs *"50bp-CUT repricing, CME ~74.5%"* (`SIG-W-20260903-004`, 9/3). ⛔ **Rate-path pricing is HENRY/ORACLE instrument class, explicitly not mine** (see FED TRAP row). **Routed to PROME 9/4, not adjudicated here.** BOND registered BND-24 off my print. |

**KEY THRESHOLDS EPOP row — the 9/4 grade narrative (verbatim, rotated same day)**

| T-03 CARL+HENRY; T-04 HENRY+REGINALD. 🔴 **GRADED 9/4 off card §3d — BOTH MOVED AWAY. T-03 did NOT fire** (needed ≤58.9; printed **59.1**; 3m −0.1 vs the −0.3 bar) **· T-04 did NOT fire, and its 6-month leg — which WAS satisfied at July (−0.5) — is now UNSATISFIED (−0.2).** ⛔ **This was the card's headline pre-commitment ("a FLAT 58.9 print fires T-03", WQ-159 RULED 9/2). EPOP rose instead. The closest live threshold in the book missed, and I am recording it as a loss for this book.** LEG B (≥59.2) short by **0.1pp**, down from 0.3pp. |

---

## `pending-inputs-20260904`

**The whole PENDING INPUTS section, rotated verbatim out of `STATUS.md` 2026-09-04** (4th rotation that day; the hot half could not hold it). **No figure changed.** Every window here is drained/consumed; live obligations were already carried in PICKUP.


> 🔒 **Rotation banner + discharged windows 7/27–9/1 → `STATUS_DETAIL.md` § `pending-history`** (verbatim, L195 · L199-202).


| Window | From | State |
|---|---|---|
| 9/2 | **PROME** ×2 (WQ-159 T-03 ruling · Canada counter-tariff correction) | ✅ **BOTH DRAINED 9/3; rows rotated to `STATUS_DETAIL.md` § `pending-drained-20260902` 9/4 (verbatim).** 🔴 **Carry-forward that must NOT rotate away: the Canada row's "zero hits" self-claim was FALSE — `docket/CATALYSTS.tsv:3` carried "~$28B"; corrected 9/4 to CA$27.6B.** |
| 9/2 | **PROME** (OBLIGATION-DIFF ask: after the split, verify no OPEN obligation is orphaned in `STATUS_DETAIL.md`) | 🟡 **PARKED to 2026-09-05, fold-by day-after-NFP.** ~10min task requiring `git show HEAD~N:AGENTS/LABOR/STATUS.md` diff. Not blocking the two graded prints or NFP tomorrow. Filed → `processed/` with dated PARKED entry in NEXT SESSION PICKUP #7. |
| 9/2 | **DAEDALUS** (route-around WALTER — `AGENTS/LABOR/CLAUDE.md` lines 121/291 read "signal directly", should route SIGNALS via WALTER) | 🟡 **PARKED to 2026-09-05.** Small CLAUDE.md amendment; DEFECT INSIDE A RULE THAT NEVER FIRES (has never been exercised as written). Not blocking anything. Filed → `processed/` with NEXT SESSION PICKUP #7 entry. |
| 9/4 | **BOND** (reply to my retraction) | ✅ **CONSUMED.** BOND grepped **all nine** live surfaces: **zero hits**. 🔴 Returned a Sept Fed-path contradiction (hike ~65–68% vs 50bp-cut ~74.5%, two days apart) — **not my instrument class; routed to PROME 9/4, now with ORACLE.** Full row → `STATUS_DETAIL.md` § `rotated-20260904`. |
| — | — | 🟢 **Live inbox lanes empty by `ls` at 2026-09-03 ~12:1x ET.** |




<a id="lab08-reprice-path"></a>
## § `lab08-reprice-path` — rotated from STATUS.md 2026-09-07 (verbatim, no figure changed)

Moved to buy read-cap headroom; the live 4% / as-made 65% stay on STATUS. Row as it stood:

| LAB-08 | BLS benchmark revision >500K downward | 🔧 **4%** *(live diagnostic; **scores AS-MADE at 65%**)* · **Status: `OPEN` — due Q1-2027** | 🔴 **GRADED-BUT-NOT-RESOLVED 2026-08-28 off card §4 BAND E.** Path: **65% as-made (2026-02-18) → 35% (8/07, 21d pre-print, gate #14 unforced arithmetic) → 15% (8/27 11:12, BLS-primary verification) → 4% (8/28, … |  *[carried: −79,000 · 0.61 · 0.95 · 6.33 · 0.275 · 0.65]* |


<a id="pickup-rotated-20260907"></a>
## § `pickup-rotated-20260907` — PICKUP items rotated from STATUS.md 2026-09-07 (verbatim, no figure changed)

Rotated for read-cap headroom; items 2 and 7 were CLOSED, item 5(b) completed 9/7. Text as it stood:

2. 🔴 **CARD-DESIGN DEFECT, L-18 class, logged not fixed:** NFP card §3b's U-3×LFPR table does not PARTITION — the realized cell (U-3 ≤4.1 with LFPR **UP**) had no pre-committed assignment, and the card's ≤4.1 row assumed LFPR *down*. Zero score was taken. **Every future card's band set must be checked for exhaustion on the axis it grades, not just for the branches the thesis expects** (L-17: the branch that "cannot happen" is the one you forgot to enumerate). Fold into `LESSONS.md` as L-27 next session.

5. 🟡 **PARKED, fold-by 2026-09-05 (tomorrow):** (a) **OBLIGATION-DIFF pass** on the BD-25 split per PROME 9/2 packet; (b) **DAEDALUS route-around fix** — amend `CLAUDE.md` L121/L291 to route SIGNALS via WALTER, then re-run `walter_route_check.py` for rc=0. Both deliberately deferred past the NFP window; **the window is now closed, so these are due.**

7. 🟢 **Attribution bar LIFTED 9/4** (card §6) — released by TYPE: two independent witnesses (Type-A CES, Type-B CPS) agreed on strength, household side on a **growing** labor force.


<a id="calendar-graded-20260907"></a>
## § `calendar-graded-20260907` — MONITORING CALENDAR graded rows rotated from STATUS.md 2026-09-07 (verbatim)

Rotated for read-cap headroom. All three were GRADED and closed; no figure changed in the move.

| ✅ 🟡 **Wed Sep 2** | **OPM RIF final rule effective** (FR 2026-15665) | 🔒 **PRE-COMMITTED 9/1, held 9/2: MECHANISM change, not a threshold. Vector 12 does NOT move on the rule, nor on a federal payroll line alone (BD-17) — only if separations also appear in UCFE.** Test frozen on the NFP card §3e. *Full row → `STATUS_DETAIL.md` § `session-superseded-20260902`.* |

| ✅ 🟢 **Thu Sep 3** ×2 | **Initial claims w/e Aug 29 · ISM Services PMI August** | **206K / MA 207.2K, CC 1,779K** → NO-ACTION band; **ISM Svs Emp 47.8** → v3 HOLDS at 2. Both graded off frozen cards, both NO score movement. **Full rows → `STATUS_DETAIL.md` § `calendar-graded-20260903`** (rotated 9/4, verbatim). |

| ✅ 🔴 **Fri Sep 4 08:30** | **NFP August** — **GRADED off `docket/graded/GRADING_CARD_20260904_NFP.md`** (frozen 9/2, ~36h ahead) | **+162,000 · U-3 4.1% unchanged · LFPR 61.6% (+0.2) · EPOP 59.1% (+0.2) · LF +683K · Jun/Jul revised +55,000 net (Jul −23K → +21K).** Card §3a band **+150K–302K ⇒ NO VECTOR MOVES.** **NOTHING FIRED**: Kill A 0/3 · T-06 both legs ✗ · **T-03 ✗ (needed ≤58.9, printed 59.1)** · T-04 ✗ · T-08 ✗ · T-13 ✗ · LAB-12 unresolved. **Moved: v8 restore counter 0→1 of 2** (net revisions ≥0). **Score 29/75 UNCHANGED.** Both questions the row asked are answered — **−23K did NOT survive revision, and the labor force STOPPED shrinking (+683K).** |

<a id="payroll-revision-bias"></a>
## § `payroll-revision-bias` — rotated from STATUS.md 2026-09-07 (verbatim, no figure changed)

📐 **PAYROLL REVISION BIAS — MEASURED 2026-09-07, MOVES NO THRESHOLD** (ALFRED build, WQ-175 ② / DOCKET L274; ledger `workbook/PAYROLL_VINTAGES.tsv`, 44 ref months 2023-01→2026-08; reconstruction validated **5/5** at PINNED vintages). Will's *"consistently revised lower"* is **CONFIRMED with a sign and a size:** first→current mean **−66.0K**, `−66.0/10.3 = −6.4` t, **35/44 = 79.5% DOWN** (sign P=5.3e-05); **first→third −33.5K** (`−33.5/8.8 = −3.8`, 28/39, **stage-OK only** — 2025-09/10/11 excluded, the lapse-disrupted releases where the 3rd AVAILABLE vintage ≠ BLS's 3rd ESTIMATE). ⚠️ **BY REGIME: NOT DETECTED — which is NOT the same as absent.** first→third `diff −3.4K / SE 18.7 ⇒ t = −0.18`, 95% CI **[−40K, +33K]**; first→current CI **[−61K, +34K]**. **n=13 vs 24 leaves economically large effects unresolved — say "this sample did not detect one," never "there is none."**

<a id="pickup-1b-20260907"></a>
## § `pickup-1b-20260907` — PICKUP 1b as it stood before the 2026-09-07 discharge session (verbatim)

1b. 🆕 **DAEDALUS parity packet 2026-09-07 consumed (F1–F12).** DONE: **F1** brief reordered to schema amendment 12 (CROSS-DOMAIN byte 55,629 → **2,953**, verbatim, byte-multiset conserved) · **F5** both 9/25 obligations docketed · **F10** route-around leg A closed. ⏳ **DATED CARRY-FORWARD, next closeout:** ACTION 3 (6 undated SENDING rows + footer pin at `NEXUS_BRIEF.md:149`) · **4** (EXIT RULES kill-rail date stamp + Kill A run → 63/31/21/162, add EXIT RULES to C1's sweep) · **6** (BD-21 re-book n≥3, build the pre-freeze band-exhaustion check **before the 9/25 Oct-2 card freeze**) · **7** (strip ✅ from BD-14/BD-26, re-date 5 passed triggers) · **10** (`BUILD_DEBT.md` has TWO opposite discharge rules at `:10` and `:55`; 9 of 25 rows malformed vs the 6-col header) · **11** (**4 SCORED** `PREDICTIONS.tsv` rows carry the WALKED-DOWN confidence with no as-made mark — LAB-02/06/13/17 — **plus the OPEN row LAB-08**; five cells, four scored. *DAEDALUS COR-20260907-01 corrected its own "5 of 12 scored"; verified here — LAB-08 prints `OPEN`.*) · **12** (scoreboard §B/§D vintage drift). **F2 charter batch is WILL-GATED — propose as ONE batch; edit nothing in `CLAUDE.md` first.** ⚠️ **F2 is SEVEN contradictions, not eight** — the *"8 frameworks vs 10"* item is **withdrawn** (`:256` reads "8 primary + 2 supplementary" = 10 = `:292`; verified here, not relayed). **Drop it before proposing.**

<a id="open-prediction-basis"></a>
## § `open-prediction-basis` — LAB-12 / LAB-18 / LAB-19 derivations rotated from STATUS.md 2026-09-07 (verbatim, no figure changed)

**LAB-12 — as it stood in STATUS.md before the 2026-09-07 rotation:**

| LAB-12 | U-3 ≥5.0% Q3-Q4 | 🔧 **8%** *(live; **scores AS-MADE 60%**)* | Q3-Q4 | 🔴 **REPRICED 30% → 8% on 9/4, gate #13-driven, ~2h after I held it at 30%.** Needs 4.1% → ≥5.0% = **0.9pp in ~4 prints**; base rate `11/302 = 3.64%` ex-covid 2000+ (4.78% incl covid) ⇒ **30/3.64 = 8.2×**. I wrote *"mechanism cuts both ways"* on the row and left the number — **gate #13's unpriced-update pattern, committed while quoting gate #13.** Conditioning worsens it: U-3 flat on LF **+683K** = absorption. 8% = base rate + the one genuine bull leg (a re-expanding LF is the denominator condition letting U-3 rise if hiring stalls). **L-25 echo — trigger was Will asking, not a check of mine.** |

**LAB-18 — as it stood in STATUS.md before the 2026-09-07 rotation:**

| **LAB-18** 🆕 | **T-03 fires (EPOP 3-mo decline ≥0.3pp) on ≥1 of the 2026 prints** | **15%** | Sep–Nov obs | 🔒 **Registered 9/4 because the miss exposed that this call was NEVER a prediction** (L-28). **THRESHOLD call ⇒ capped far below 60 per gate #3** (0-for-4 zone). N=3, bars ROLL: **Sep ≤58.7 · Oct ≤58.6 · Nov ≤58.8** (referents Jun 59.0 / Jul 58.9 / Aug 59.1) = moves of −0.4/−0.5/−0.3 from 59.1. EPOP recent \|MoM\| mean **0.113**, max 0.3 ⇒ the firing move is **3–4× typical**; ≤−0.4 is **0/23** recent, `8/318 = 2.52%` since 2000. `0.85^(1/3) = 0.947` ⇒ ~5.3%/draw, and overlapping windows make 15% if anything generous. **Defeat: EPOP ≥58.9 through Nov.** |

**LAB-19 — as it stood in STATUS.md before the 2026-09-07 rotation:**

| **LAB-19** 🆕 | **The Jun/Jul LF contraction REVERSED, not paused: LF MoM >0 in ≥2 of the 3 remaining 2026 prints** | **60%** | Sep–Nov obs | 🔒 **MECHANISM call (3-for-3 zone) — the deliberate counterpart to LAB-18, and it tests MY OWN CORE TENSION in the direction that would refute it.** Base rate `P(LF MoM>0)`: `203/317 = 64.0%` (2000+), **`11/22 = 50.0%` last 23mo**; ≥2-of-3 at p=.50 ⇒ 50%, at p=.64 ⇒ `0.64³+3(0.64²)(0.36) = 70.4%`. **60% sits between** — +683K is the largest LF gain in the sample and real regime evidence, but it is **one** observation. ⚠️ **≥2-of-3 is not survive-all — gate #12's per-draw cap does not bind here.** 🔴 **If TRUE, my CORE TENSION needs rewriting, said at registration.** |

<a id="matrix-graded-20260907"></a>
## § `matrix-graded-20260907` — CONVERGENCE MATRIX graded narrative rotated from STATUS.md 2026-09-07 (verbatim, no figure changed, no score changed)

**Vector 6 — as it stood in STATUS.md before the 2026-09-07 rotation:**

| 6 | Long-term unemployed / duration | **3** 🟠 | flat | ✅ **GRADED 9/4 off NFP card §3e.** Aug LT share **27.0%** (1.9M) [BLS USDL-26-1435], up from Jul 25.5% — a **+1.5pp jump that lands EXACTLY ON the >27% restore bar without crossing it.** ⛔ **v6 HOLDS at 3**: `27.0` is not `>27`, and the conjunction's second leg (YoY comparison turning positive, re-established from BLS's own text) is **absent from the release** — so the knife-edge never had to be adjudicated. **Not rounding up.** Drop-to-2 (<24% ×2) nowhere near. |

**Vector 8 — as it stood in STATUS.md before the 2026-09-07 rotation:**

| 8 | BLS data degradation | **2** 🟡 | flat | ✅ **GRADED 9/4 off NFP card §3c: net revisions Jun+Jul = +55,000 ≥ 0 ⇒ restore-to-3 counter 0 → 1 OF 2.** Score HOLDS at 2 (restore needs TWO consecutive; leg 2 is the Oct 2 print). 🔒 **Restore-to-3 (unchanged, pre-committed): two consecutive prints with net revisions ≥0.** Restore-to-4 would need the Feb-2027 FINAL to come in … |  *[carried: −79,000 · −178,000 · +99,000 · −154.6 · +135.1 · +87K · 4% · 2.0%]*

**Vector 12 — as it stood in STATUS.md before the 2026-09-07 rotation:**

| 12 | **Public-sector employment** *(renamed 8/07; rename NOT a new vector — /75 unchanged. Basis → `STATUS_DETAIL.md` § `rotated-20260904`)* | **1** ⚪ | flat | ✅ **GRADED 9/4 off NFP card §3e: federal payrolls Aug −5K (ex-USPS −3.3K) [Table B-1] vs the ≤−25K T-13 MoM bar ⇒ does NOT fire; v12 HOLDS at 1.** No UCFE check triggered — and per **BD-17** the payroll line alone would not have moved the vector even had it fired. Total government **+35K** (local gov't education +42K). Re-fire needs a new federal RIF authority, **or** a state/local decline that persists 3+ months **and** coincides with an EPOP drawdown — i.e. only when it stops being idiosyncratic |

<a id="claim-retraction-20260805"></a>
## § `claim-retraction-20260805` — the 7/6 half-retracted ISM/WARN claim, rotated from the STATUS.md header 2026-09-07 (verbatim)

🔴 **[7/6 CLAIM — HALF RETRACTED 2026-08-05]** This line read: *"ISM Services employment **47.4** (sub-50, ~4th straight mo...) + an 8-firm big-tech WARN wave now corroborate the freeze on the **survey AND hard-filing layers**."* …

<a id="thresholds-retired-basis"></a>
## § `thresholds-retired-basis` — KEY THRESHOLDS rows rotated from STATUS.md 2026-09-07 (verbatim, no figure changed, no band changed)

**U-3 — as it stood in STATUS.md before the 2026-09-07 rotation:**

| 🔴 **U-3 — DEMOTED TO A REPORTED GAUGE 2026-08-07 (BD-15). It no longer carries a trigger.** | **4.1%** [Aug · obs 2026-08-01, BLS USDL-26-1435] — **UNCHANGED**, on **LFPR 61.6% (+0.2pp) and a labor force that GREW +683K to 169,777K** | ~~≥4.7% = T-03~~ · ~~≥5.0% = T-04~~ **BOTH RETIRED.** Measured 1990-2026: a U-3 **level** bar at 4.7% fired in **65.4% of ALL months** and separated recession from non-recession by only **+12.9pp**; at 5.0%, … | **Still reported** because the Fed and the market watch it — but LABOR fires nothing off it. Triggers moved to **EPOP**, below |

**EPOP — as it stood in STATUS.md before the 2026-09-07 rotation:**

| 🆕 **EPOP (employment-population ratio) — the trigger gauge as of 8/7** | **59.1%** [Aug · obs 2026-08-01, Summary Table A] — **ROSE +0.2pp**; **3m −0.1pp** (vs May 59.2) **· 6m −0.2pp** (vs Feb 59.3) | **T-03 🟠 = EPOP fell ≥0.3pp over 3 months** (base 11.7%, in-rec 64.5%, out 7.6% = **+56.9pp**) · **T-04 🔴 = EPOP fell ≥0.5pp over 6m AND ≥0.3pp over … | T-03 CARL+HENRY; T-04 HENRY+REGINALD. 🔴 **GRADED 9/4 — BOTH MOVED AWAY, and this was the card's headline call. T-03 ✗** (needed ≤58.9, printed **59.1**) **· T-04 ✗, its 6-month leg went SATISFIED (−0.5) → UNSATISFIED (−0.2).** Next bars roll: **Sep ≤58.7 · Oct ≤58.6 · Nov ≤58.8** → now registered as **LAB-18, 15%**. Loss recorded, not re-read. Narrative → `STATUS_DETAIL.md` § `rotated-20260904`. |

**JOLTS-layoffs-rate — as it stood in STATUS.md before the 2026-09-07 rotation:**

| 🆕 **JOLTS layoffs & discharges rate** *(added 8/5 — the card called this "the most important bear signal of the week and the one my dashboard under-weights," and it was right that it was missing)* | **1.0%** (1,666K) [July, BLS 9/1] — **DOWN from 1.1%**, and now at the **bottom** of the 1.0–1.2% range it has held all year | **≥1.2% = the firing side waking → escalate CARL + REGINALD same-day.** One of only **two** live revival paths for the break thesis. 🔴 **9/1: it moved AWAY — `1.2 − 1.0 = 0.2pp` of distance, up from 0.1pp. I am recording this as a loss for my own book, because that is what it is** | 🔴 CARL+REGINALD |  *[carried: 250K]*

<a id="thresholds-rotated-20260907b"></a>
## § `thresholds-rotated-20260907b` — further KEY THRESHOLDS rows rotated from STATUS.md 2026-09-07 (verbatim, no figure or band changed)

**JOLTS-NET — as it stood in STATUS.md before the 2026-09-07 (second) rotation:**

| 🆕 **JOLTS NET (hires − separations)** | **−18K** [July: `5,054 − 5,072`]; **Jun −5K** (revised, was −3K); May **−8K**; Apr +177K, Mar +158K | **>0 in both of the 2 most recent reference months = freeze-thaw v2 LEG C** — ✗ **not met, and it moved FURTHER away**: both of the two most recent months are negative and July is the most negative of the three | 🟠 CARL+HENRY. 🔴 **THIRD consecutive negative month.** Base-rate, discounts and the 66-month conditional → `STATUS_DETAIL.md` § `jolts-net-basis` — **licensed use: a rare run, partly circular with CES; the rates-as-shapes are the independent content.** |  *[carried: 2.0% · 1.1%]*

**JOLTS-GROSS — as it stood in STATUS.md before the 2026-09-07 (second) rotation:**

| JOLTS hires **(GROSS — demoted 8/7, read beside NET below, never alone)** | **5,054K / rate 3.2%** [July, BLS 9/1] | <5.0M sustained 2+ mo = T-10 — **NOT met, and the distance is small: `5,054 − 5,000 = 54K` above the arm line, on a print that fell 278K.** A single further month of this size crosses it · ~~>5,500K = freeze-thaw leg 3~~ **RETIRED 8/7 — leg 3 is now JOLTS NET, see below** · ~~>5,300K = card I-1 condition~~ retired with the card | 🟠 CARL+HENRY. ⚠️ **A gross flow cannot speak to net employment — do not cite this row without the NET row** |

**ECI — as it stood in STATUS.md before the 2026-09-07 (second) rotation:**

| **🆕 ECI (composition-controlled wage gauge)** | **Civilian comp 3.4% / private wages 3.1%** [Q2, BLS 7/31] | **≥3.6% = wage-pressure premise REAL** (supply-artifact framing weakens) · **≤3.4% flat-or-down while AHE accelerates = COMPOSITION** (supply-shrink corroborated) · **3.5% = INDETERMINATE** ⚠️ *(this middle … | **DENY branch FIRED 7/31.** Feeds FED TRAP, LAB-12, → CARL (real-income) + HENRY (policy-path). … |  *[carried: 2026-10-30]*

**NFP — as it stood in STATUS.md before the 2026-09-07 (second) rotation:**

| NFP (revised series, L-02) | **+162K** [Aug, USDL-26-1435]; revised run 214/148/63/**31**/**21**/**162**; **3-mo avg +71.3K** `(31+21+162)/3 = 214/3`. 🔴 **Jul revised −23K → +21K (+44K) and Jun +20K → +31K (+11K): the July NEGATIVE PRINT DID NOT SURVIVE REVISION.** | ≥200K ×3 consecutive = **Kill A** (dead — zero of last 3) · **<100K + U-3 jump ≥0.2pp = T-06** | Kill A → PROME/FORGE; T-06 🟠 CARL+REGINALD+HENRY. ✅ **GRADED 9/4: Kill A 0 of 3 (31/21/162) — cannot fire · T-06 BOTH LEGS FAIL** (NFP +162K ≥100K ✗; U-3 4.1% vs the ≥4.3% bar ✗). Card §3a band **+150K–302K ⇒ NO VECTOR MOVES; single-month leg alone met.** … |

**CC — as it stood in STATUS.md before the 2026-09-07 (second) rotation:**

| **Continuing claims** | **1,779K** [w/e Aug 22 · obs 2026-08-22] — **fourth direction-change in six weeks**; range-bound 1,777-1,799K holds | Vector-7 drop-to-2 needs **<1,750K ×4wk** (**29K away**; still no sustained direction, and it needs FOUR consecutive weeks of which there are **ZERO**). … | vector 7 — **kept as a COST/duration gauge, which is what it actually measures; it is not an early-warning instrument and will not be used as one** |

<a id="exit-rules-graded-20260907"></a>
## § `exit-rules-graded-20260907` — rotated from STATUS.md 2026-09-07 (verbatim, no figure changed)

**freeze-thaw-v2-state:**

  🔴 **v2 live state 2026-09-04 (GRADED on NFP August): NOT FIRED — but EVERY LEG MOVED TOWARD FIRING and the honest read is that this book got weaker today.**
  > **LEG A ✗ — and the card ORDERED this recompute before reading August (L-02).** The frozen bar was **≥+303K** on the old Jun/Jul vintage; the upward revisions moved it to **`(31 + 21 + X)/3 ≥ 100` ⇒ X ≥ +248K**. August **+162K ⇒ short by 86K**. Single-month leg **met** (162 ≥ 150); **3-mo-avg leg fails** (71.3 < 100). A conjunction, and I am not relaxing it.
  > **LEG B ✗ — EPOP 59.1 vs the ≥59.2 bar, short 0.1pp** (was 0.3pp away at July).
  > **LEG C ✗ — JOLTS NET −18K [Jul] / −5K [Jun rev]**, unrefreshed; next test JOLTS August ~Oct 6 on the v4 bands already pre-registered.

**pattern-of-the-day:**

1c. 🔴 **THE PATTERN OF THE DAY, AND IT IS THE SAME ONE — n=6 now, and the sixth was inside my own calibration record.** L-29 (written this morning, n=5): *every defect was in the sentence NAMING what a figure was a figure OF, never in the figure.* **Instance 6, found this session:** `PREDICTIONS_SCOREBOARD.md` verified its as-made confidences against **`PREDICTIONS.tsv`** — a ledger that did not exist until **2026-03-04**, whose `Date_Made` is a bulk-seed placeholder. Every figure in it was correct; the claim *"this is the as-made value"* was not. **4 of 12 rows were scored at a walked-down number. Mean Brier 0.299 → 0.342.** ⇒ `[[finding_instrument_reports_clean_against_the_wrong_reference]]` **n=25**.

<a id="pickup-rotated-20260907b"></a>
## § `pickup-rotated-20260907b` — PICKUP detail rotated from STATUS.md 2026-09-07 PM (verbatim)

**PICKUP 1e:**

1e. ✅ **WITHDRAWN 2026-09-07 — there was no canon conflict; I mis-read WQ-112 as either/or.** WQ-112 specifies **BOTH** books: the latest dated pre-resolution mark governs *scoring*, and the original `Date_Made` confidence is **retained and reported separately as first-call calibration**. ⇒ **`0.342` is correct and stays — it is the FIRST-CALL CALIBRATION figure**, which is exactly what it measures. 🔴 **The operative half, which I would have got wrong:** WQ-112 (ii) requires a re-mark to have landed in the machine field **with its date**; **today's backfilled dates are git reconstructions, not contemporaneous receipts, so they do NOT retroactively confer latest-mark eligibility on the pre-2026-09-07 book.** That book is unavailable to me — and it would be much better than 0.342, which is why I should be slow to claim it. **Forward-only:** every re-mark from today goes into the field in WQ-112 form at the moment it is made. *(Caught by CODEX; withdrawal packeted to PROME.)*

**PICKUP 6:**

6. **Live build debt: BD-19 · BD-23 · BD-26.** 🔧 **BD-21 and BD-30 REMOVED — discharged 2026-09-07** by `scripts/card_partition_check.py`. ⚠️ **Recorded honestly: BD-21 was first marked discharged on a checker that CODEX then broke 5-for-5** (a single band certified as a partition; strict/inclusive boundary values unowned or double-owned; an unreadable row ignored; a decimal axis blind to a missing 4.2). **It is discharged now on a v2 that carries boundary inclusivity, integer-unit arithmetic, an UNPARSEABLE finding, and a PASS unreachable unless coverage actually ran — with CODEX's five cases as permanent members of the suite (20 tests).** 🔴 **New live card defect the v2 found: `docket/graded/GRADING_CARD_20260828_QCEW.md` bands `450–700K` and `≥700K` BOTH claim 700,000** — the card that carried LAB-08. Frozen card, so it is recorded as a card defect, never edited.

**PICKUP 1b — as it stood before the 2026-09-07 PM rotation:**

1b. 🔧 **DAEDALUS parity packet (F1–F12) — TWO ACTIONS REMAIN OPEN, both Will-gated: ACTION 8 (charter batch) and ACTION 4's THIRD LEG (see 1b-bis). Ten are discharged.** Earlier 9/7: **F1** brief reordered · **F5** 9/25 obligations docketed · **F10** route-around closed. This session: **4** *(STATUS half only — see the caveat below)* · **6** (`card_partition_check.py`, **BD-21 + BD-30 discharged**) · **7** · **10** · **11** · **12**. **ACTION 3 required TWO attempts** — the first (`f8aa3589c`) dated the six SENDING rows correctly but left the footer pin reading `Aug 27` / `6f00305ab` **while adding a sentence saying it had been repointed**; caught by CODEX, fixed with a post-condition that re-reads the file and asserts header-pin == footer-pin. 🔒 Pre-discharge text → `STATUS_DETAIL.md` § `pickup-1b-20260907`.

**PICKUP 1c — as it stood before the 2026-09-07 PM rotation:**

1c. 🔴 **THE PATTERN OF THE DAY — n=7, and instance 7 is the one to keep.** L-29 (AM): *the defect is in the sentence NAMING what a figure is a figure OF.* **Instance 7:** told to date six SENDING rows at *lines 81–88*, I dated **lines 75–81 of the reordered file — which are under `## VIEW`** — then defended it with blob hashes and a diff, all correct and all about the wrong section. ⇒ **A line number is a COORDINATE INTO A VERSION, not an address; and the more evidence you can produce for an edit, the less it tells you WHAT you edited.** Real SENDING rows now carry **send receipts** (11 rows, 0 undated). 🔒 → `LESSONS.md` **L-30**; memory **n=26**.

**PICKUP 1e — pre-2026-09-07-PM rotation:**

1e. ✅ **WITHDRAWN — no canon conflict; I mis-read WQ-112 as either/or. It specifies BOTH books.** ⇒ **`0.342` stays, labelled FIRST-CALL CALIBRATION**, which is what it measures. 🔴 **The operative constraint: WQ-112 (ii) needs the re-mark in the machine field WITH its date, so today's backfilled git reconstructions do NOT confer latest-mark eligibility on the pre-9/7 book.** That book is unavailable — and it would be much better than 0.342, which is why I should be slow to claim it. **Forward-only from today.** *(CODEX; withdrawal packeted.)* 🔒 → `STATUS_DETAIL.md` § `pickup-rotated-20260907b`.

**PICKUP 1b — pre-2026-09-07-PM rotation:**

1b. 🔧 **DAEDALUS parity (F1–F12): TEN discharged. TWO open, both Will-gated — ACTION 8 (charter batch) and ACTION 4's third leg.** 🔒 Per-action trail → `STATUS_DETAIL.md` § `pickup-1b-20260907`.

**PICKUP 6b — pre-2026-09-07-PM rotation:**

6b. 🔴 **NEW, AND IT IS A REAL GAP NOT A STAMP: six `NEXUS_BRIEF` SENDING rows have NO delivery artifact.** Correcting my own overstated `sent` receipts (CODEX) — a brief-publication commit proves the row was *written*, not *delivered* — I searched every recipient inbox and my outbox across **2026-06-25→07-26** and found **nothing** for the CARL · CARL/REGINALD · MARCO · REGINALD · HENRY · PROME/FORGE rows. **Either they went via a live session that leaves no file, or the SENDING table has been asserting sends that never happened.** Rows relabelled `first recorded in brief … ⚠️ delivery NOT established`. **Owed: resolve which, and if undelivered, actually send them.**

**PICKUP 6 — pre-2026-09-07-17:0x rotation:**

6. **Live build debt: BD-19 · BD-23 · BD-26.** **BD-21 + BD-30 discharged on `card_partition_check.py` v3.1** — declared discharged prematurely THREE times (CODEX broke v1/v2/v3). 🔴 **DAEDALUS then found it RED on every real card with TWO findings FALSE** — root cause broader than their examples: **coverage run over a PARTIAL band set manufactures gaps by construction.** Fixed (`COVERAGE-NOT-RUN`; `= 50.0 exactly` and `+150K to +302K` now parse; a 1-numeric-cell column is no longer an axis). ✅ **First real card now PASSES — ISM 9/3, a genuine partition checked by eye.** Of 9 cards: **1 clean · 4 DEFECT · 4 UNVERIFIED.** 23 self-tests + 4000-case membership (**scope stated: integer boundaries, precision 1 only**).

**PICKUP 1c — pre-2026-09-07-17:0x rotation:**

1c. 🔴 **PATTERN OF THE DAY — n=7 wrong-reference, none self-caught, three review rounds.** Sharpest: told to date six SENDING rows at *lines 81–88*, I dated **75–81 of the reordered file — under `## VIEW`** — then defended it with blob hashes and a diff, all correct and all about the wrong section. ⇒ **A line number is a COORDINATE INTO A VERSION, not an address; and the more evidence you can produce for an edit, the less it tells you WHAT you edited.** 🔒 → `LESSONS.md` **L-30**; memory **n=26**.

<a id="review-rounds-20260907"></a>
## § `review-rounds-20260907` — PICKUP narrative from the 2026-09-07 review rounds (verbatim)

**PICKUP 6:**

6. **Live build debt: BD-19 · BD-23 · BD-26.** **BD-21 + BD-30 discharged on `card_partition_check.py`** — declared discharged prematurely 3× (CODEX broke v1/v2/v3; DAEDALUS then found it RED on every real card with 2 findings FALSE). 🔑 **Root cause: coverage over a PARTIAL band set manufactures gaps by construction.** ✅ **Gate is now a PRODUCTION ACCEPTANCE SET, not "one card passed"** (DAEDALUS): valid partition passes · known gap fails · known overlap fails · a declared `kind=trigger-ladder` is not judged as a partition at all — **that declaration names a table TYPE and asserts nothing about the trigger logic.** Evidence: **23 self-tests + 4000-case membership (scope: integers, precision 1) + 4-case acceptance**; ISM 9/3 LINT-CLEAN. 🔒 Detail → `STATUS_DETAIL.md` § `pickup-rotated-20260907b`.

**PICKUP 6c:**

6c. 🔧 **CHARTER CLAIM — I told Will `CLAUDE.md` was untouched; `082342069` edited it at 12:14 TODAY** (earlier LABOR session, WALTER route fix, +475 B — what pushed the file from AT-cap to **OVER** the 54,250 B cap). True of my session, **false of the day, in a Will-gated packet** — n=8 of the wrong-reference class. Correction sent (`2026-09-07d`). ✅ **DAEDALUS WITHDREW C4 at ~17:2x and rules the route edit RETAINED** — so the gate question is closed and no revert is owed; **the SCOPE ERROR in my packet stands on its own and is not withdrawn.** ⏳ C6 (`scripts/tests/*.py` `sys.exit` at import breaks `pytest`) is a FILES-table clause ⇒ in the batch.

**PICKUP 6d:**

6d. 🔒 **ALFRED "pre-registered" HAD NO RECEIPT — corrected, forward-only.** `alfred_vintages.py:39` read *"PRE-REGISTERED BEFORE ANY BIAS WAS COMPUTED"*, but the classifier and `PAYROLL_VINTAGES.tsv` ship in **one commit (`e96453b45`)**, so nothing external proves the order. **Pre-registration is a claim about ORDER and only a commit can establish it** — the same defect as *"falsified before adoption"* and *"verified in git"*, third form today. Header + ledger annotated. **Rule: commit the spec in its OWN commit before computing the result.** *(DAEDALUS; the measured figures are unaffected.)*

<a id="pickup-superseded-wq193"></a>
## § `pickup-superseded-wq193` — PICKUP items superseded by the WQ-193 closeout rewrite (verbatim)

**PICKUP 6:**

6. **Live build debt: BD-19 · BD-23 · BD-26.** ✅ **BD-21 + BD-30 discharged.** `card_partition_check.py` gate is a **production acceptance set** (valid partition passes · known gap fails · known overlap fails · a declared `kind=trigger-ladder` is not judged as a partition — that names a table TYPE, never "trigger logic verified"). Evidence: **23 self-tests · 4000-case membership (scope: integers, precision 1) · 4-case acceptance.** Declared discharged prematurely 3× before this. ⏳ **C6 → the charter batch.**

**PICKUP 6b:**

6b. 🔴 **SIX `NEXUS_BRIEF` SENDING ROWS HAVE NO DELIVERY ARTIFACT.** Correcting my own overstated `sent` receipts (CODEX): a brief commit proves the row was *written*, not *delivered*. Searched every recipient inbox + my outbox **2026-06-25→07-26** — **nothing** for the CARL · CARL/REGINALD · MARCO · REGINALD · HENRY · PROME/FORGE rows. Relabelled `first recorded in brief … ⚠️ delivery NOT established`. **Owed: establish which, and send them if they never went.**

**PICKUP 6c:**

6c. 🔧 **Two of my own claims corrected today, both order/scope claims with no receipt.** (a) I told Will `CLAUDE.md` was untouched — **`082342069` edited it 12:14 today** (+475 B, what took the file OVER the cap); true of my session, false of the day, in a Will-gated packet. **DAEDALUS withdrew C4 and retains the route edit, so no revert is owed — the scope error stands.** (b) **ALFRED's "PRE-REGISTERED" has no receipt** — classifier and results share commit `e96453b45`; header + ledger annotated. **Rule: commit the spec in its OWN commit before computing the result.** 🔒 Both → `STATUS_DETAIL.md` § `review-rounds-20260907`.

**PICKUP 1c:**

1c. 🔴 **PATTERN OF THE DAY — n=8, none self-caught, across FOUR review rounds (CODEX ×3, DAEDALUS ×2).** Every instance: a statement true of the object I checked, presented as a statement about the object the reader cares about. Today's forms: *verified in git* (wrong artifact) · *falsified before adoption* (self-authored suite) · *pre-registered* (no commit receipt) · *nothing has been edited* (my session, not the day) · **and the sharpest, dating rows at `lines 75–81` because a packet said 81–88, without checking which section that is.** ⇒ **A coordinate is not an address, and evidence that an edit happened is not evidence the right thing was edited.** 🔒 → `LESSONS.md` **L-30**; memory **n=26**.

**PICKUP 1b:**

1b. 🔧 **DAEDALUS parity (F1–F12): TEN discharged; TWO open, both Will-gated — ACTION 8 (charter batch, now incl. C6) + ACTION 4's third leg.** 🔒 → `STATUS_DETAIL.md` § `pickup-1b-20260907`.

**PICKUP 1d:**

1d. 🔴 **CHARTER BATCH STILL WILL-GATED — nothing in `CLAUDE.md` has been edited and nothing will be before Will's word.** **F2 = SEVEN contradictions** (the *"8 frameworks vs 10"* item is withdrawn — `:256` reads "8 primary + 2 supplementary" = 10 = `:292`, verified here, not relayed). **ACTION 4's third leg belongs in this batch, not in a unilateral edit**: adding EXIT RULES to C1's sweep list is a `CLAUDE.md` change, and `CLAUDE.md` is **AT the 54,250 B single-read cap** — so the batch must be a hot/cold split, not an append. Proposal owed to Will.

**PICKUP 1:**

1. 🔴 **READ-CAP AT THE WALL — `STATUS.md` 32,481 B = 99.8% of the 32,550 B budget, 69 B of headroom.** Rotating the LAB-08 reprice narrative to `STATUS_DETAIL.md` today bought **82 B** — which is BD-25's own point: the per-session shave is a **tax, not a fix**. **Escalated 9/4; structural answer is WQ-179, ruling 2026-09-11.** ⛔ **Next session: rotate BEFORE writing, and do not shave further pending the ruling.** Never raise the budget — not ours to move.

**PICKUP 1e:**

1e. ✅ **WITHDRAWN — no canon conflict.** WQ-112 specifies BOTH books ⇒ **`0.342` stays, labelled FIRST-CALL CALIBRATION.** 🔴 **Latest-mark scoring is unavailable for the pre-9/7 book: backfilled git dates are reconstructions, not contemporaneous receipts** — and that book would be better than 0.342, which is why I am slow to claim it. Forward-only. 🔒 → `STATUS_DETAIL.md` § `pickup-rotated-20260907b`.

**PICKUP 3:**

3. 🔒 **PRE-REGISTERED, UNTOUCHED:** v4 JOLTS-August NET bands (~Oct 6) — NET >0 ⇒ v4 → 2 · NET ≤0 a 4th month ⇒ v4 → 4 · NET ≤0 but hires rate ≥3.4% ⇒ HOLD 3. **v8 restore-to-3 = leg 1 of 2 BANKED 9/4 (+55K); leg 2 is the Oct 2 print.**

**PICKUP 4:**

4. 🔴 **OWED, carried unchanged — base-rate the CORRECTIVE, not just the original.** The 8/07 reprice cut 65% → 35% citing my 0-for-4 threshold record, and **35/4 = 8.75×** the honest post-print 4% (L-25). Not started.

**PICKUP 5:**

5. 🟡 **PARKED (a) STILL OWED — OBLIGATION-DIFF pass on the BD-25 split** (PROME 9/2 packet), fold-by was 9/5, now 2d late. **(b) route-around fix ✅ DONE 9/7**, `walter_route_check.py` clean on both LABOR rows.

**PICKUP 2:**

2. ✅ **CLOSED — card-partition defect folded to `LESSONS.md` L-27.** Full text → `STATUS_DETAIL.md` § `pickup-rotated-20260907`.

**PICKUP 7:**

7. ✅ **CLOSED — attribution bar lifted 9/4** by TYPE (Type-A CES + Type-B CPS agreed). Full text → `STATUS_DETAIL.md` § `pickup-rotated-20260907`.

---

## § `pickup-rotated-20260907c` — PICKUP items closed at the 2026-09-07 card session (verbatim, no figure changed)

1. ✅ **WQ-193 DELIVERED 2026-09-07 — charter split executed, sha `27a5fb87a`.** `CLAUDE.md` **55,019 → 50,485 B** (from 769 B OVER the 54,250 B cap to **3,765 B under**); new on-demand `CHARTER_DETAIL.md`, confirmed outside the boot perimeter. Both censuses clean (text + obligation; 76 clauses all located); the one fix pass caught a stray `**` my own edit introduced. **Due 9/9, met with 2 days spare.** 🔒 Memo → `PROME/inbox/2026-09-07e_from-LABOR_WQ-193-DELIVERED…`.

1b-bis. ✅ **ACTION 4 IS COMPLETE — all three legs.** The STATUS-side legs were done 9/7 (kill-rail date stamp; Kill A run refreshed to **63/31/21/162**), and the third leg — *EXIT RULES named in C1's spine-token sweep list* — **landed in the WQ-193 charter split and is live at `CLAUDE.md:77`** (verified by reading the line, 2026-09-07). 🔧 **This item previously read "half done… WILL-GATED in the charter batch… Do not read ACTION 4 as closed" — that was written before the split and was never updated when the split shipped the edit.** The EXIT RULES banner in § EXIT RULES is therefore no longer the only mechanism carrying the obligation; the charter rule is. *(`[[finding_record_of_an_action_is_not_the_action]]` inverted — here the action happened and the record still said it had not.)*

9. 🔒 **C2-0 SWEEP RE-RUN AT THIS CLOSEOUT, re-derived from `workbook/PREDICTIONS.tsv` — ZERO rows trip it.** Six OPEN: LAB-03 7% · LAB-08 4% · LAB-11 50% · LAB-12 8% · LAB-18 15% · **LAB-19 60%**. ⚠️ **LAB-19 clears the ≥60% bar but FAILS the staleness leg — registered 2026-09-04, three days ago** — so gates #3/#5/#12/#13 have nothing stale to sweep. *(Saying zero, and saying why, per C2-0's own instruction not to read a hardcoded list.)*

---

## § `bottom-line-rotated-20260907c` — BOTTOM LINE narrative from the 2026-09-04 NFP grade, rotated 2026-09-07 (verbatim, no figure changed)

**🟠 AUGUST NFP WAS GRADED OFF TEXT FROZEN ~36 HOURS AHEAD, AND THE CARD'S HEADLINE CALL MISSED. Nothing fired. Score unchanged at 29/75. The value of the session is that the miss is legible: T-03 was pre-committed to fire on a flat 58.9 EPOP, EPOP rose to 59.1, and I am recording that as a loss rather than re-reading the band.**

**The count layer is healing and I have to say so.** August **+162,000**; June **+20K → +31K** and July **−23K → +21K**, net **+55,000** upward. **The negative July print did not survive revision** — which retires "second consecutive negative print" as a live branch. Revised run **214/148/63/31/21/162**, 3-mo avg **71.3K**. LEG A's bar was recomputed on the revised vintage *before* August was read (L-02, as the card ordered): **+303K → +248K**, and **+162K missed by 86K**. Single-month leg met, 3-mo-avg leg failed — a conjunction, unrelaxed.

**The household survey is the real story, and it cuts against this book.** U-3 held **flat at 4.1% while the labor force GREW +683K** (LFPR 61.4 → 61.6, EPOP 58.9 → 59.1, employed +569K, part-time-for-economic-reasons −414K). That is the **mirror image** of the June/July immigration-signature pattern the CORE TENSION is built on — the supply-shrink confound that made those two months uninterpretable is **absent from this print**. Every freeze-thaw leg moved toward firing: LEG B is now 0.1pp away, down from 0.3pp.

**Two witnesses, not nine legs** (INDEPENDENCE_MAP §2). Payrolls + private (+127K derived) + revisions + sector lines + AHE are **ONE Type-A (CES) witness**; U-3 + LFPR + EPOP + LT-share + PTER are **ONE Type-B (CPS) witness**. Type C (UI) and Type D (ISM) did not print today. **Both moved the same direction — toward strength — and it is the first time in this book they have agreed on the strong side.** ⛔ **The attribution bar is now LIFTED**; the attribution that travels is named by TYPE, not desk count.

**Two things held the line honestly.** Long-term unemployed share jumped 25.5% → **27.0%**, landing *exactly on* the >27% restore bar without crossing it — v6 holds at 3, and the conjunction's absent second leg (YoY turning positive) meant the knife-edge never had to be adjudicated. And **card §3b does not partition**: the realized U-3×LFPR cell (≤4.1 with LFPR **up**) was never enumerated, so I took **zero score movement** and logged the defect rather than writing a band on print day (L-17/L-18).

2. ✅ **CLOSED 2026-09-07 — the six undelivered `NEXUS_BRIEF` SENDING rows are DISPOSITIONED, and the answer is SEND NOTHING, on the merits.** Each was assessed against today's state (Will-directed) and **not one should be sent as written**: CARL's L&H −61K is a superseded June figure · **CARL/REGINALD's U-3 point was already delivered by a better packet** (the 8/07 EPOP re-spec is in both recipients' `inbox/processed/`, verified) · MARCO's supply signature is **contested by my own current book** (LF +683K; LAB-19) · HENRY's row **cites a threshold retired 8/07** · REGINALD's and PROME/FORGE's conclusions survive but their figures are three vintages stale. 🔑 **A delivery backlog decays — five of six are wrong to send TODAY for reasons unrelated to whether they went out THEN.** Full table + reasoning → `NEXUS_BRIEF.md` § CROSS-DOMAIN.

6. 📅 **9/11 WQ-179** (read-cap) — this batch is its **third** structural instance (LABOR STATUS · STUE STATUS · LABOR charter). **9/14** broader conventions; **do not let them hold up authorized maintenance.**
7. 🔒 **Today's repair history — n=8 wrong-reference defects over four review rounds, none self-caught — is recorded ONCE:** `LESSONS.md` **L-30** + `STATUS_DETAIL.md` § `review-rounds-20260907`. **Not restated here.**

**BOTTOM LINE tail rotated 2026-09-07 PM (verbatim):**

Earlier the same day, **WQ-193 executed** (charter split; `CLAUDE.md` from 769 B over the cap to 3,765 B under; both censuses clean), and **the calibration record corrected against my own favour — 4 of 12 predictions were scored at a walked-down confidence, so mean Brier is 0.342, not 0.299, and the ≥60% threshold record is 0-for-5.** **Eight wrong-reference defects were found in my work across four review rounds and I self-caught none of them**; all eight are one shape — a statement true of the object I checked, presented as a statement about the object the reader cares about. That is recorded once, in `LESSONS.md` L-30.

**PICKUP 5 — Amendment 1 narrative, rotated 2026-09-07 PM (verbatim):**

🔧 **AMENDMENT 1, PRE-PRINT (CODEX), frozen original untouched — the bands omitted TWO existing rules, now independent axes:** **(a)** vector 13's `<200,000 ×4` counter keys on **200,000**, not a band edge — a **197K** print is band B "NO ACTION" *and* starts that counter 1 of 4; **(b)** T-01 is **MA-basis** and can fire here — **`X > 383,000`** ⇒ **X ≥ 384,000 fires T-01 AND T-02**, and band E's routing had **omitted CARL**. **No threshold moved.** Three boundaries sit inside band B — never read one band as the whole verdict. 🔧 **AMENDMENT 1 then took a second CODEX pass:** the T-01 bound is a function of the *retained three weeks* and therefore **revises** — `X > 1,000,000 − (W2+W3+W4)` is the pre-commitment and `383,000/384,000` is only its value on the frozen vintage (**a 617→618K revision moves the bound to 382,000 and a 383K print then fires T-01**). I had written the regenerate-on-revision rule for §3 in the same session I hard-coded a revisable bound in A1.2. Also corrected: my hand-proofs claimed exhaustion *"at any precision"* — false for two of the three (**199,500** and **383,500** are uncovered); they hold **on the whole-thousand grid DOL publishes**, which is narrower than I claimed.

**BOTTOM LINE 9/7 governance lead, rotated 2026-09-07 19:2x (verbatim):**

**🔧 2026-09-07 — NO MARKET DATA MOVED, NO VECTOR SCORED, SCORE UNCHANGED 29/75.** The day's output was preparation and repair. **The 9/10 claims card is frozen three days ahead of its print**, built from a new reusable template (`docket/TEMPLATE_claims_card.md`, BD-19 discharged), bands A–E partition-verified with 0 defects. 🔴 **The card's first act was to refute the docket that spawned it:** the pre-computed mechanical term read `(X−200)/4` and is `(X−212)/4` — w/e Aug 8 is 212K, and the 200K was w/e Aug 1, which had already rolled off — **so on a 206K repeat the docket said the 4-week MA would RISE 1,500 when it will FALL 1,500.** Sign inverted at the modal outcome, and it was BD-19's own predicted failure mode, sitting in the docket. A second find: STATUS's claims run carried **203K** for w/e Aug 22 where FRED now has **204K** — an **unfollowed revision**, not a typo (203K was the 8/27 as-published value), and the third consecutive claims card to catch a revision STATUS had not followed. **B2a cannot see this class — it compares observation DATES, not VALUES.** Earlier: **WQ-193 executed** and **calibration corrected against my own favour — mean Brier 0.342; ≥60% threshold record 0-for-5.** **Eight wrong-reference defects, none self-caught** → L-30.

3b. ⚠️ **READ-CAP: both boot surfaces are back under budget but with little headroom — `STATUS.md` 31,689 B and `LESSONS.md` 28,717 B against 32,550 B.** Adding L-31 pushed LESSONS over and forced rotation 4 in-session. **Assume the next substantive append to either one needs a rotation in the same session.**

---

## § `pickup-closed-20260907-closeout` — PICKUP as it stood at the 2026-09-07 closeout, before the forward-slate rewrite (verbatim)

## NEXT SESSION PICKUP

> 🔒 **Rotation banner + closed items (9/1, 8/28 slates) → `STATUS_DETAIL.md` § `pickup-closed`.** Items 1–3 of the 9/3 slate CLOSED 9/4 (NFP graded; attribution bar lifted).

1. ✅ **WQ-193 DELIVERED 2026-09-07** — charter split, sha `27a5fb87a`, both censuses clean. Full entry → `STATUS_DETAIL.md` § `pickup-rotated-20260907c`.
2. ✅ **CLOSED 2026-09-07 — the six undelivered `NEXUS_BRIEF` SENDING rows are DISPOSITIONED: SEND NOTHING, on the merits.** Each was assessed against today's state (Will-directed); **not one should be sent as written** — one was already delivered by a better packet (the 8/07 EPOP re-spec, verified in both recipients' `inbox/processed/`), one cites a threshold retired 8/07, one is contested by my own current book, the rest carry stale figures under surviving conclusions. 🔑 **A delivery backlog decays.** Full table → `NEXUS_BRIEF.md` § CROSS-DOMAIN; reasoning → `STATUS_DETAIL.md` § `pickup-rotated-20260907c`.
3. 🔴 **OWED, still not started — base-rate the CORRECTIVE, not just the original** (L-25; `35/4 = 8.75×`). *(L-25 demoted to the LESSONS cold index this session, rotation 4; rule retained, worked case in `archive/`.)*
3b. ⚠️ **READ-CAP: both boot surfaces run with almost no headroom** (STATUS ~32.4K, LESSONS ~31.2K vs the 32,550 B budget). **Assume every substantive append needs a rotation in the SAME session** — it did four times today. Detail → `STATUS_DETAIL.md`.
4. **Near-term build priorities: BD-19 ✅ discharged this session · BD-23 · BD-26 · BD-31 🆕 (🟠 — I escalated it to 🔴 and CODEX correctly showed the escalation conflated *automation coverage* with *grading risk*; returned to 🟠).** ⚠️ **These are the near-term ones, NOT the whole register — `BUILD_DEBT.md` carries 15 LIVE rows** and is the source of truth. *(Relabelled 2026-09-07, Will-directed: the line read "Live build debt: BD-19 · BD-23 · BD-26", which presented three near-term items as the entire live set — the same subset-as-whole shape as the eight L-30 defects.)* BD-21 + BD-30 discharged; the checker gate is a 4-case production acceptance set (23 self-tests · 4000-case membership, scope: integers/precision 1 · acceptance). ⛔ **Checker work CLOSED — bounded role, evidence matches it.**
5. ✅ **NEXT: Thu 9/10 08:30, claims w/e Sep 5 — CARD IS FROZEN, 3 days ahead** (`docket/GRADING_CARD_20260910_claims.md`, built from the new `docket/TEMPLATE_claims_card.md`; **BD-19 discharged**). Bands A–E partition-verified, 0 defects. 🔴 **The card's first act was to refute its own docketed setup: the mechanical term was `(X−200)/4` and is `(X−212)/4`** — w/e Aug 8 is 212K, and the 200K is w/e Aug 1 which had already rolled off — **which inverts the sign of the MA move at the modal print** (a 206K repeat: docket said MA +1,500, truth −1,500). `CATALYSTS.tsv` corrected. 🔧 **AMENDMENT 1 + AMENDMENT 1b, both PRE-PRINT (CODEX), frozen original untouched — the bands omitted two EXISTING rules (vector 13's `<200,000 ×4` counter; T-01's MA basis, which also fires CARL), and the T-01 bound was then found to be REVISABLE like §3's.** Live form: **`X > 1,000,000 − (W2+W3+W4)`** — regenerate at the print; `383,000/384,000` is only the frozen-vintage value. Hand-proof scope corrected to the whole-thousand grid. **No threshold moved.** Full narrative → `STATUS_DETAIL.md`; bands → the card. **At grade time: recompute §3 on the as-published vintage FIRST, grade all three axes independently, then `git mv` the card to `docket/graded/` AND build the 9/17 card in the same session** (C2a's recurring-print trigger). Pre-committed and unchanged: `763 / 20,000 = 3.8%` of the L-08 detection floor, **26× below it; no national claims move is attributed to that cohort in any week.**
6. 📅 **9/11 WQ-179** (read-cap) · **9/14** broader conventions — **do not let them hold up authorized maintenance.** 7. 🔒 **Today's repair history (n=8 wrong-reference defects, none self-caught) is recorded ONCE** in `LESSONS.md` L-30. Both items in full → `STATUS_DETAIL.md` § `pickup-rotated-20260907c`.
9. 🔒 **C2-0 SWEEP RE-RUN THIS CLOSEOUT, re-derived from `workbook/PREDICTIONS.tsv` — ZERO rows trip it.** Six OPEN; the only one clearing the ≥60% bar (LAB-19, 60%) **fails the staleness leg** — registered 2026-09-04. Full derivation → `STATUS_DETAIL.md` § `pickup-rotated-20260907c`.
8. 🔒 **PRE-REGISTERED, UNTOUCHED:** v4 JOLTS-August NET bands (~Oct 6) — NET >0 ⇒ v4 → 2 · NET ≤0 a 4th month ⇒ v4 → 4 · NET ≤0 but hires rate ≥3.4% ⇒ HOLD 3. **v8 restore-to-3: leg 1 of 2 banked 9/4 (+55K); leg 2 is the Oct 2 print.**

1b-bis. ✅ **ACTION 4 COMPLETE — all three legs.** The third leg (EXIT RULES in C1's sweep list) shipped in the WQ-193 split and is live at `CLAUDE.md:77`, verified by reading the line 2026-09-07; this item had still read *"half done… WILL-GATED"*. Full entry → `STATUS_DETAIL.md` § `pickup-rotated-20260907c`.


---

# § ROTATIONS — 2026-09-10 claims-grade closeout

> ⛔ **Moved, never edited. No figure changed, no score changed, no band changed.** Each block below is the text `STATUS.md` carried immediately before the 2026-09-10 rotation. **`STATUS.md` wins on any live figure** — cite these as what was written on the day, with their own dates.
> **Why rotated:** the 9/10 grade appended to a file with ~660 B of headroom against the binding **32,550 B** READ_CAP budget, so rotation was required in the SAME session — exactly as PICKUP item 6 warned on 9/7. Post-rotation `STATUS.md` = **32,540 B**, i.e. **10 B of headroom**. ⚠️ **That is not lean, it is at the line** — the next append needs a rotation before it, not after.

## § `thresholds-rotated-20260910` — KEY THRESHOLDS rows as they stood at the 2026-09-07 closeout (verbatim, rotated from STATUS.md 2026-09-10)
### row: `Initial claims (4-wk MA basis)` as it stood at the 2026-09-07 closeout

| Initial claims (4-wk MA basis) | **206K / MA 207,250** [w/e Aug 29 · obs 2026-08-29] | <230K drift · 230-250K accelerating (vec 13→3) · **>250K sustained 4+wk = T-01** · **251-300K single = ARM T-01 provisional** · **>300K single = T-02 FIRE** | T-01 🔴 CARL+REGINALD; T-02 🔴 REGINALD (ORANGE→RED)+HENRY. **9/3: 206K single, 42,750 below T-01 on MA basis, 94K below T-02. No fire, no arm.** Run: 200/212/207/**204**/**206**. 🔧 **CORRECTED 2026-09-07 — this read `203`.** STATUS's own MA forces it: `829,000 − 212,000 − 207,000 − 206,000 = 204,000`, and FRED `ICSA` confirms 204,000 [w/e Aug 22]. **RESOLVED as an UNFOLLOWED REVISION, not a typo:** w/e Aug 22 was published at **203,000** on 8/27 (`NEXUS_BRIEF` VIEW row + `workbook/PUBLISHED.tsv` row 59) and has since been revised to **204,000**. The MA (207,250) tracked the revision because `boot.py` refreshes it from FRED `IC4WSA`; the run digit did not, because it was hand-carried from the 8/27 print. **So the auto-refreshed and hand-carried halves of the same row disagreed by 250 and nothing compared them.** 🔴 **Third consecutive claims card to catch a revision STATUS had not followed** (8/13, 8/20, 9/10) — that is a pattern, not three incidents. ⚠️ **B2a cannot catch this class — it compares observation DATES, not VALUES.** Found by the 9/10 card's §1 reconciliation, which is now a template fill-step. |  *[carried: 42,750 · 94K]*

### row: `Initial claims (bull side)` as it stood at the 2026-09-07 closeout

| Initial claims (bull side) | **206K — 21K above the line** | ≤185K ×5 clean sessions = Kill B. **9/3: count stays 0 of 5** — 206K does not start it. Distance WIDENED 3K on this print (18K → 21K). Direction noted honestly; the count is what governs and it is zero | exit-all check |

### row: `Continuing claims` as it stood at the 2026-09-07 closeout

| **Continuing claims** | **1,779K** [w/e Aug 22 · obs 2026-08-22] — **fourth direction-change in six weeks**; range-bound 1,777-1,799K | Vector-7 drop-to-2 needs **<1,750K ×4wk** (**29K away**, and **ZERO** of the four consecutive weeks banked) | vector 7 — **a COST/duration gauge, which is what it actually measures; it is NOT an early-warning instrument and will not be used as one** |


 — verbatim, rotated from STATUS.md 2026-09-10 (no figure changed, no score changed)

📐 **PAYROLL REVISION BIAS — MEASURED 2026-09-07, MOVES NO THRESHOLD** (ALFRED, WQ-175 ② / DOCKET L274; ledger `workbook/PAYROLL_VINTAGES.tsv`). Headline: first→current mean **−66.0K** (`−66.0/10.3 = −6.4` t), **35/44 = 79.5% DOWN**; first→third **−33.5K** stage-OK. ⚠️ **BY REGIME: NOT DETECTED ≠ absent** — CI **[−40K, +33K]**. 🔒 Full derivation + exclusions → `STATUS_DETAIL.md` § `payroll-revision-bias`.

---

## § `calendar-graded-20260910` — MONITORING CALENDAR rows for Sep 4 / Sep 10, before and at the grade (verbatim, rotated from STATUS.md 2026-09-10)
### As they stood BEFORE the 2026-09-10 grade


| 🟡 **Fri Sep 4** | **MSFT/Xbox WARN cohort separations effective** (TX 158 + WA 605 = **763**) | ⛔ **PRE-COMMITTED, INDEPENDENCE_MAP §4: `763 / 20,000 = 3.8%` of the L-08 national detection floor — **26× below it**. I will NOT attribute any national claims move to this cohort in ANY week.** Falls in the w/e Sep 5 week (prints Thu 9/10). Logged, unattributable by construction. |
| 🔴 **Thu Sep 10 08:30** | **Initial claims w/e Sep 5** + CC w/e Aug 29 | 🔒 **CARD FROZEN 2026-09-07, 3 days ahead** → `docket/GRADING_CARD_20260910_claims.md` (first built from the new `docket/TEMPLATE_claims_card.md`). Bands A–E **partition-verified** (`card_partition_check.py`, 0 defects). 🔴 **Roll-off corrected: w/e Aug 8 = 212K rolls off ⇒ mechanical term `(X − 212)/4`, so the MA FALLS below a 212K print.** The docket carried `(X−200)/4`, which inverted the sign at the modal outcome. **Recompute on the as-published vintage BEFORE reading the level (L-02).** |

### STATUS header line as it stood at the 2026-09-07 closeout

**Last Updated:** 2026-09-07 ~18:1x ET *(Labor Day, market closed)* · 🔧 **NO MARKET DATA MOVED; NO VECTOR SCORED; SCORE UNCHANGED 29/75.** ✅ **9/10 CLAIMS CARD FROZEN 3 DAYS AHEAD** (+ Amendment 1, pre-print) off a new template — **BD-19 discharged.** 🔴 **The card refuted its own docket: mechanical term was `(X−200)/4`, is `(X−212)/4` — sign-inverting at the modal print.** See BOTTOM LINE. 🔴 **CALIBRATION CORRECTED AGAINST MY OWN FAVOUR: 4 of 12 predictions were scored at a walked-down confidence — mean Brier 0.299 → 0.342, ≥60% threshold record 0-for-5, not 0-for-4.** **Eight wrong-reference defects found across four review rounds, none self-caught** (recorded once → `LESSONS.md` L-30).

### The graded rows as first written on 2026-09-10, before compression

### MONITORING CALENDAR graded rows Sep 4 / Sep 10 — verbatim, rotated from STATUS.md 2026-09-10

| ✅ **Fri Sep 4** | MSFT/Xbox WARN cohort separations effective (763) | **CLOSED 9/10 — LAPSED-LOW, as pre-committed and without re-reading the outcome.** `763 / 20,000 = 3.8%` of the L-08 floor, `20,000 / 763 = 26.2×` below it ⇒ **no part of the w/e Sep 5 move is attributed to it in EITHER direction.** Claims were flat; that is not evidence the cohort was absorbed. `docket/WARN_COHORT.tsv` rows closed. |
| ✅ **Thu Sep 10 08:30 — GRADED** | Initial claims w/e Sep 5 **206K** + CC w/e Aug 29 **1,774K** | **BAND B / NO ACTION on all five axes; nothing fired, nothing armed, no packet routed** (§7 pre-committed: bands A/B ⇒ STATUS only). Card → `docket/graded/GRADING_CARD_20260910_claims.md` §9. 🔴 **The card's A1.2 regeneration clause fired on its FIRST live use and its named hypothetical occurred to the unit:** retained sum revised `617,000 → 618,000`, T-01 bound moved `383,000 → 382,000`. A 383,000 print would now fire T-01 **and require CARL**; the frozen number would have missed it. |



---

## § `matrix-rotated-20260910` — CONVERGENCE MATRIX vectors 3 / 6 / 10 / 12 graded narrative (verbatim, rotated from STATUS.md 2026-09-10)

### CONVERGENCE MATRIX vector 3 — verbatim, rotated from STATUS.md 2026-09-10 (no figure changed, no score changed)

| 3 | ISM/survey employment | **2** 🟡 | flat | ✅ **GRADED 9/3 off frozen card (`docket/graded/GRADING_CARD_20260903_ISM_SERVICES.md`).** Svs Aug Emp **47.8** [+0.4 from Jul 47.4, 2nd month contraction] < 50 ⇒ **v3 HOLDS at 2**, survey layer stays SPLIT (Mfg Aug 51.2 vs Svs Aug 47.8). Drop-to-1 condition (both surveys >50 same month) NOT met and now further from the line on the Svs side. |  *[carried: 51.2 · 47.8]*

### CONVERGENCE MATRIX vector 6 — verbatim, rotated from STATUS.md 2026-09-10 (no figure changed, no score changed)

| 6 | Long-term unemployed / duration | **3** 🟠 | flat | ✅ **GRADED 9/4.** Aug LT share **27.0%** (1.9M) [USDL-26-1435], up from 25.5% — lands **EXACTLY ON the >27% restore bar without crossing it**. ⛔ **v6 HOLDS at 3**: `27.0` is not `>27`, and the conjunction's second leg is **absent from the release**. **Not rounding up.** Drop-to-2 (<24% ×2) nowhere near. 🔒 → `STATUS_DETAIL.md` § `matrix-graded-20260907`. |

### CONVERGENCE MATRIX vector 10 — verbatim, rotated from STATUS.md 2026-09-10 (no figure changed, no score changed)

| 10 | Healthcare cracking | **1** ⚪ | flat | ✅ **GRADED 9/4: health care Aug +13K [USDL-26-1435] — POSITIVE ⇒ T-08 does NOT fire, v10 HOLDS at 1.** Decelerating hard (+13K vs 12-mo avg **+32K**, and the average itself fell +36K→+32K) — recorded, but **there is no band for deceleration and I will not improvise one.** Net-neg aggregate print → T-08 fires CARL/REGINALD, restore 4 |

### CONVERGENCE MATRIX vector 12 — verbatim, rotated from STATUS.md 2026-09-10 (no figure changed, no score changed)

| 12 | **Public-sector employment** *(renamed 8/07; /75 unchanged)* | **1** ⚪ | flat | ✅ **GRADED 9/4: federal payrolls Aug −5K (ex-USPS −3.3K) [Table B-1] vs the ≤−25K T-13 bar ⇒ does NOT fire; v12 HOLDS at 1.** Per **BD-17** the payroll line alone would not have moved the vector even had it fired. Re-fire needs a new federal RIF authority, **or** a state/local decline persisting 3+ months **and** coinciding with an EPOP drawdown. 🔒 → `STATUS_DETAIL.md` § `matrix-graded-20260907`. |



---

## § `exit-rules-rotated-20260910` — EXIT RULES Kill A bullet + sweep banner, and the LAB-03 / LAB-18 / LAB-19 / C2-0 rows (verbatim, rotated from STATUS.md 2026-09-10)

### EXIT RULES Kill A bullet — verbatim, rotated from STATUS.md 2026-09-10 (no figure changed)

- **Kill A (bull falsification): NFP ≥+200K ×3 consecutive, revised series (L-02).** 🔧 **RUN REFRESHED 2026-09-04 vintage: 63 / 31 / 21 / 162** — zero of the last 3 qualify (`162 ≥ 200` ✗). Dormant. *(This bullet carried the Jul-2 vintage `214 / 148 / 129 / 57` until 2026-09-07 while `§ KEY THRESHOLDS` in the same file carried the 9/4 revised run — same verdict, split stamps, DAEDALUS F4. The verdict never diverged, which is why nothing caught it.)* Standing rule unchanged.

### EXIT RULES sweep banner — verbatim, rotated from STATUS.md 2026-09-10 (no figure changed)

> ⚠️ **SWEEP THIS SECTION AT EVERY C1** — Kill A carried the Jul-2 vintage for 9 weeks while the same file's KEY THRESHOLDS carried the 9/4 one (DAEDALUS F4). ⛔ **The matching `CLAUDE.md` C1 edit is NOT made — it is Will-gated in the charter batch.** Until Will rules, this banner is the only thing carrying the obligation, which is exactly the weaker of the two mechanisms; treat it as a reminder, not a control.

### C2-0 sweep line — verbatim, rotated from STATUS.md 2026-09-10 (no figure changed)

> 🔒 **C2-0 STALE-HIGH-CONFIDENCE SWEEP — RE-RUN 2026-09-02, re-derived from `workbook/PREDICTIONS.tsv`, not read off a list. RESULT: ZERO ROWS TRIP IT** (LAB-03 7% · LAB-08 4% live · LAB-12 30% · LAB-11 50% — all below the ≥60% bar, so gates #3/#5/#12/#13 have nothing to sweep). The 9/1 run and the rotated 8/07 worked block → `STATUS_DETAIL.md` § `predictions-resolved` and § `session-superseded-20260902`.

### LAB-18 row — verbatim, rotated from STATUS.md 2026-09-10 (no figure changed)

| **LAB-19** 🆕 | **The Jun/Jul LF contraction REVERSED, not paused: LF MoM >0 in ≥2 of the 3 remaining 2026 prints** | **60%** | Sep–Nov obs | 🔒 **MECHANISM call (3-for-3 zone) — the deliberate counterpart to LAB-18, and it tests MY OWN CORE TENSION in the direction that would refute it.** 60% sits between the 2000+ and last-23mo base rates. ⚠️ **≥2-of-3 is not survive-all — gate #12 does not bind here.** 🔴 **If TRUE, my CORE TENSION needs rewriting, said at registration.** 🔒 Base rates → `STATUS_DETAIL.md` § `open-prediction-basis`. |

### LAB-19 row — verbatim, rotated from STATUS.md 2026-09-10 (no figure changed)

> 🔒 **Resolved-prediction tables (LAB-10 · LAB-13 · LAB-06 · LAB-17 + earlier resolutions) and the 8/07 sweep-block rotation pointer → `STATUS_DETAIL.md` § `predictions-resolved`** (verbatim, L146 · L148 · L150-159). Ledger of record stays `workbook/PREDICTIONS.tsv`.

### LAB-03 row — verbatim, rotated from STATUS.md 2026-09-10 (no figure changed)

| LAB-08 | BLS benchmark revision >500K downward | 🔧 **4%** *(live diagnostic; **scores AS-MADE at 65%**)* · **Status: `OPEN` — due Q1-2027** | 🔴 **GRADED-BUT-NOT-RESOLVED 2026-08-28** off card §4 BAND E. 🔒 Full reprice path (65→35→15→4%) + carried figures → `STATUS_DETAIL.md` § `lab08-reprice-path` (verbatim, rotated 2026-09-07). |

---

## § `pickup-rotated-20260910` — NEXT SESSION PICKUP + BOTTOM LINE as they stood at the 2026-09-07 closeout (verbatim, rotated from STATUS.md 2026-09-10)
## NEXT SESSION PICKUP

> 🔒 **Closed items (WQ-193 delivered · the six SENDING rows · ACTION 4 · the 9/7 repair history) → `STATUS_DETAIL.md` § `pickup-closed-20260907-closeout`.** This slate is FORWARD work only.

1. 🔴 **THE CLOCK ITEM — Thu 9/10 08:30, claims w/e Sep 5. Card is FROZEN 3 days ahead** (`docket/GRADING_CARD_20260910_claims.md` + Amendments 1/1a/1b, all pre-print; built from `docket/TEMPLATE_claims_card.md`). **Grade order, pre-committed:** ① recompute **BOTH** window-derived quantities on the AS-PUBLISHED vintage *before* reading the level — §3's `ΔMA(X) = (X − 212,000)/4` **and** A1.2's T-01 bound `X > 1,000,000 − (W2+W3+W4)` (frozen value 383,000; **void if the window revises**) · ② grade **three independent axes** — §2 single-print bands A–E, A1.1 vector-13 `<200,000` counter, A1.2 T-01 MA basis · ③ write the outcome into KEY THRESHOLDS + the calendar row · ④ **`git mv` the card to `docket/graded/` AND build the 9/17 card in the same session** (C2a's recurring-print trigger). ⚠️ **MSFT/Xbox cohort (763) is in this week and is NOT attributed in either direction:** `763 / 20,000 = 3.8%` of the L-08 floor, `20,000 / 763 = 26.2×` below it.
2. 📅 **PROME commission L302 — four instruments, due 2026-09-16** (packet in `inbox/processed/`; ACK `PROME/inbox/2026-09-07f`). Order: Indeed operational audit (`VX-LAB-1.04` carries a **182-day-old** figure) → LAB-19 age decomposition → private weekly hours (B-4) → state claims breadth, FL first. **Each item states the decision it could change, including against my thesis, BEFORE any build.** ⛔ Do not assume postings lead hires — test it on my own history; if it does not lead, say so and the row stays diagnostic.
3. 📅 **9/25 — Oct-2 NFP card freeze owed** (`card_required_check.py` flags it MISSING when run at that date — verified). Also 9/25: ALFRED payroll vintage table (WQ-175 ②). **9/11 WQ-179 · 9/14 conventions — do not let them hold up authorized maintenance.**
4. 🔴 **OWED, still not started — base-rate the CORRECTIVE, not just the original** (L-25; `35/4 = 8.75×`). **L-32 is the second instance of this class and it is now n=2 in 10 days** — the trigger to build is a comparative TIMING/performance claim.
5. **Live build debt — `BUILD_DEBT.md` is the register (15 LIVE rows); near-term: BD-23 · BD-26 · BD-31.** BD-19 discharged 9/7. ⛔ BD-26 (no payrolls vector) settles at a full matrix re-grade, **never on a catalyst morning.**
6. ⚠️ **READ-CAP: both boot surfaces run with almost no headroom** — STATUS ~32.4K, LESSONS ~31.2K against the 32,550 B budget. **Assume every substantive append needs a rotation in the SAME session**; it did five times on 9/7.
7. 🔒 **PRE-REGISTERED, UNTOUCHED:** v4 JOLTS-August NET bands (~Oct 6) — NET >0 ⇒ v4 → 2 · NET ≤0 a 4th month ⇒ v4 → 4 · NET ≤0 but hires rate ≥3.4% ⇒ HOLD 3. **v8 restore-to-3: leg 1 banked 9/4 (+55K); leg 2 is the Oct 2 print.**
8. 🔒 **C2-0 SWEEP RE-DERIVED AT THIS CLOSEOUT from `workbook/PREDICTIONS.tsv` (not read off a list) — ZERO rows trip it.** Six OPEN: LAB-03 7% · LAB-08 4% · LAB-11 50% · LAB-12 8% · LAB-18 15% · LAB-19 60%. Only LAB-19 clears the ≥60% bar and it **fails the staleness leg** (registered 2026-09-04, 3 days).
9. 🔒 **C5 RETIREMENT CHECK RUN — nothing eligible, and the reasons are recorded so it is not re-litigated:** `STATUS_archive_20260702.md` (67d, 0 refs inside LABOR) **is referenced from `AGENTS/CORAL/inbox/processed/` — moving it breaks a path another desk has logged**, so it stays; `ARCH_REPORT_20260626.md` has 0 refs repo-wide but its last commit is **45 days**, under the 60-day bar on the git clock (the preferred clock — mtime is restamped by sync).

## BOTTOM LINE

**🔧 2026-09-07 — NO MARKET DATA MOVED, NO VECTOR SCORED, SCORE UNCHANGED 29/75.** The domain read is unchanged from the 9/4 grade: claims **206K / MA 207,250** [w/e Aug 29], CC **1,779K**, U-3 **4.1%** on a labor force that grew **+683K**, NFP **+162K**. Nothing fired; nothing is close except freeze-thaw **LEG B, 0.1pp away**.

**The day's output was preparation and repair, and it is worth what it caught.** The **9/10 claims card is frozen three days ahead** off a new reusable template (**BD-19 discharged**), bands partition-verified, 0 defects. 🔴 **The card refuted the docket that spawned it:** the pre-computed mechanical term read `(X−200)/4` and is **`(X−212)/4`** — on a 206K repeat the docket said the 4-week MA would *rise* 1,500 when it will *fall* 1,500. **Sign inverted at the modal outcome, and it was BD-19's own predicted failure mode sitting in the docket.** Two further finds: STATUS carried an **unfollowed revision** (203K→204K, w/e Aug 22 — `B2a` compares obs DATES, not VALUES, so it cannot see this class), and the bands **omitted two existing decision rules** (vector 13's `<200,000` counter; T-01's MA basis, which also routes **CARL** — previously omitted from band E).

🔴 **THE HONEST TALLY, COUNTED RATHER THAN ASSERTED** *(I first wrote "ten" here without dividing — the exact L-32 trigger, caught in the same closeout that recorded it).* **CODEX pass 1: 6 · CODEX pass 2: 5 · PROME: 1 ⇒ `6+5+1 = 12` found by others. Self-caught: 2. Total `12+2 = 14`; self-caught share `2/14 = 14%`.** The two I found were the frozen-half edit and a latent `CARD:`-matching-inside-`NOCARD:` bug — **both surfaced by checks I had just written, neither by re-reading my own prose.** *(Separately, the 9/7 morning session's 8 wrong-reference defects, none self-caught, are recorded once in L-30 and are NOT re-counted here.)* ⇒ **L-31** (a DERIVED parameter ages on a different clock than the level it came from, and only the level has a freshness check) and **L-32** (the rule I broke sat in my own charter, written after the identical break 10 days earlier — it failed because the number was an *aside*, had no external source so recall replaced measurement, and ran in my favour).

🔒 **The 9/4 NFP-grade narrative** (headline call missed; count layer healing; household survey cutting against this book) → `STATUS_DETAIL.md` § `bottom-line-rotated-20260907c`.

**Next — Thu Sep 10 08:30, claims w/e Sep 5.** Grade off the frozen card: recompute **both** window-derived quantities on the as-published vintage first, grade **three independent axes**, then archive the card and build the 9/17 one in the same session. **Pre-committed and unchanged: the MSFT/Xbox cohort is `763 / 20,000 = 3.8%` of the L-08 floor, `20,000 / 763 = 26.2×` below it — not attributed in either direction.** Then PROME's L302 commission (9/16), the Oct-2 NFP card freeze (9/25), JOLTS August (~Oct 6) and **NFP September Fri Oct 2**, which supplies leg 2 of vector 8's restore counter.


---

## § `pickup-rotated-20260910b` — NEXT SESSION PICKUP items 6-8 as first written on 2026-09-10 (verbatim, rotated from STATUS.md 2026-09-10)

### NEXT SESSION PICKUP items 6-8 — verbatim, rotated from STATUS.md 2026-09-10

6. 🔴 **STILL NOT STARTED — base-rate the CORRECTIVE, not just the original** (L-25; `35/4 = 8.75×`). L-32 is the second instance; trigger to build is a comparative TIMING/performance claim.
7. **Live build debt — `BUILD_DEBT.md`; near-term BD-23 · BD-26 · BD-31 · BD-13.** ⚠️ **BD-13 (WA ESD primary for the MSFT 605 never pulled) is now CLOSED-BY-LAPSE, not discharged** — the cohort lapsed LOW so the primary no longer matters for attribution, but the row was carried as "verified" on two secondaries for 13 days and that defect is unfixed in kind.
8. 🔒 **PRE-REGISTERED, UNTOUCHED:** v4 JOLTS-August NET bands (~Oct 6) — NET >0 ⇒ v4 → 2 · NET ≤0 a 4th month ⇒ v4 → 4 · NET ≤0 but hires rate ≥3.4% ⇒ HOLD 3. **v8 restore-to-3: leg 1 banked 9/4 (+55K); leg 2 is the Oct 2 print.**

---

## § `hotcold-split-inventory` — STATUS.md header navigation block — the full HOT/COLD inventory and dated re-trigger (verbatim, rotated from STATUS.md 2026-09-10)

### STATUS.md header navigation block (HOT/COLD split + dated re-trigger) — verbatim, rotated 2026-09-10

> 🔒 **HOT/COLD SPLIT 2026-09-02 — cold half is `AGENTS/LABOR/STATUS_DETAIL.md`.** This file (`STATUS.md`) is the **HOT half and is canonical for every live figure, band, score and open grade**. Moved to the cold half, **verbatim and contiguous, no figure changed**: CORE TENSION (full) · the matrix `Key Signal`+`Indep` evidence columns and its re-grade notes · SIGNAL DASHBOARD (full) · no-fire/diagnostic threshold rows · DANGER WINDOW graded rows · resolved predictions · graded calendar rows · discharged inbox windows · closed pickup items. **Read it on demand — it is NOT a boot read.**
> 📅 **DATED RE-TRIGGER (READ_CAP rule 7):** split 2026-09-02 at **53,375 B → this file**; **re-measure at every closeout append and unconditionally on 2026-10-02, whichever first** (`python3 scripts/read_cap_check.py --agent LABOR`). Budget **32,550 B** (binding, root CLAUDE.md Data Hygiene); rotate again at ≥24,412 B. *This is a dated re-trigger, not a claim that the file is lean.*
 — verbatim, rotated from STATUS.md 2026-09-10



---

## § `bottom-line-rotated-20260910` — BOTTOM LINE paragraphs (card regenerations / Canada row) as first written on 2026-09-10 (verbatim, rotated from STATUS.md 2026-09-10)

### BOTTOM LINE paragraphs (card-regenerations · Canada row) — verbatim, rotated from STATUS.md 2026-09-10

**THE CARD EARNED ITS KEEP ON THE REGENERATIONS, NOT THE GRADE.** ✅ **A1.2's clause fired on its FIRST live use and the hypothetical it wrote three days earlier occurred to the unit:** it said *"if the retained sum revises 617,000 → 618,000, the bound moves to `X > 382,000`"*; w/e Aug 29 revised 206→207, the sum went 617,000 → 618,000, and the T-01 bound moved **383,000 → 382,000**. A 383,000 print would now fire T-01 **and require CARL**, where the frozen number would have missed it. 🔧 **And the same step found a NEW defect in my own card:** §3 has two computed columns on **two clocks** — `ΔMA` depends only on `R` (unmoved, exact) while `MA_next` depends on the retained sum (moved, so **every row rotted by +250**). The card said "regenerate §3's table" without saying which half could rot. **That is L-31 — a derived parameter ages on a different clock than the level it came from — realized ONE PRINT after L-31 was written.** Fixed forward in the 9/17 card; the template fix is still owed (PICKUP 4).

🔴 **THE CANADA ROW: GRADED, AND THE HONEST ANSWER IS "NO EVIDENCE", NOT "NO EFFECT".** Counter-tariffs on CA$27.6B took effect 9/8; **no WARN filing and no announced furlough at any US agricultural-equipment or pulp-and-paper exporter cites them.** ⚠️ **Tagged SEARCH-NOT-FOUND, explicitly NOT verified-absent** — the search was bounded web only and **four state WARN primaries are named and unchecked** (IL/MN/IA/WI). **Two days has no power anyway:** WARN's 60-day rule puts a 9/8-caused separation at ~Nov 7, and the framework's WARN→claims lag is a further 6 weeks. **Re-docketed 2026-10-08.** 🔴 **The one finding that cuts against the easy read: every named layoff the search returned runs the OTHER way** — RYAM Témiscaming, ~400–425 workers, caused by **US** tariffs on **Canadian** goods. That is Canadian employment, it is not mine, and importing it as counter-tariff evidence would be a sign error on the transmission leg.

---


## `wq214-vintage-sweep-installed-20260910`
**2026-09-10 18:0x ET — rotated verbatim from `STATUS.md` NEXT SESSION PICKUP item 9 at the closeout that wrote it (C1 rotate rule; the hot half was 746 B over the 32,550 B budget with it in place).**

✅ **WQ-214 LANDED (Will-approved, Decision Deck tap 2026-09-10 20:42Z; PROME packet `inbox/processed/2026-09-10_from-PROME_WQ-214-RULED-…`).** `CLAUDE.md` C1 now carries the **EXIT-RULES VINTAGE SWEEP as an unconditional step** — a sibling bullet to the conditional SPINE-TOKEN SWEEP, which could not cover it: **an input vintage rolls even when no LABOR series "changed"**, so the conditional sweep never fired on the defect it was standing next to. Bought by DAEDALUS F4 — Kill A carried a 9-week-stale NFP vintage while KEY THRESHOLDS in the same file carried the current one.

The `STATUS.md:101` reminder banner is **retired** (line number verified at the file before the edit). It had said, of itself, *"this banner is the only thing carrying the obligation: a reminder, not a control."* That is now false in the good direction — the obligation is a charter control and the banner's own stated condition for retirement was met.

**First live run of the control, same session:** 4/4 rails current, no repair owed — stamped on the § EXIT RULES header.

**Also this session:** a duplicated `LAB-18` row (two copies, the second lacking the *"3–4× typical EPOP MoM"* sizing clause) was removed from the PREDICTIONS table. Measure the file with `scripts/read_cap_check.py --agent LABOR`, never from a figure written here — a self-describing byte count is stale at the next edit (root canon, § Session Process Controls).

**Per-rail enumeration, rotated VERBATIM from the `STATUS.md` § EXIT RULES header stamp at the same closeout (hot half was 499 B over budget with it inline):**

🔧 **VINTAGE SWEEP (C1, now UNCONDITIONAL — WQ-214): run 2026-09-10 18:0x ET, 4/4 rails CURRENT, no repair owed.** Kill A on the 9/4 NFP vintage (63/31/21/162; next NFP 10/02) · Kill B on claims w/e Sep 5 (206K, `206−185 = 21,000` above the line, 0 of 5) · FREEZE-THAW v2 legs A/B/C on 9/4 NFP + Aug EPOP 59.1 + Jul/Jun-rev JOLTS (next JOLTS ~10/06) · break-confirm on the 206,000 4-wk MA. **First run of the control; it found nothing, which is the outcome a control is allowed to have.**


---

## § `pickup-rotated-20260917` — NEXT SESSION PICKUP as it stood at the 2026-09-10 closeout (verbatim, rotated from STATUS.md 2026-09-17; no figure changed)

## NEXT SESSION PICKUP

> 🔒 **The 2026-09-07 slate (items 1/4/6/8/9 as written) → `STATUS_DETAIL.md` § `pickup-rotated-20260910`.** This slate is FORWARD work only.

1. 🔴 **THE CLOCK ITEM — Wed 9/16, PROME commission L302, four instruments.** ✅ **NOW ON `docket/CATALYSTS.tsv`** (registered 9/10 off PROME's packet — before this it lived only in a STATUS line and `catalyst_countdown.py`, which iterates by DATE, could not see it; **third instance of the DAEDALUS F5 class**). Order: Indeed operational audit (`VX-LAB-1.04`, 182-day-old figure) → LAB-19 age decomposition → private weekly hours (B-4) → state claims breadth, **FL first**. **Each item states the decision it could change, INCLUDING against my thesis, BEFORE any build.** ⛔ Do not assume postings lead hires — test it on my own history; if it does not lead, say so and the row stays diagnostic.
2. 📅 **Thu 9/17 08:30 — claims w/e Sep 12. Card is FROZEN** (`docket/graded/GRADING_CARD_20260917_claims.md`). **Grade order, pre-committed:** ① regenerate the **THREE** window-derived quantities on the as-published vintage *before* reading the level — §3's `ΔMA` term, §3's **`MA_next` column** (it rots independently — that is this week's find), §5a's T-01 bound `X > 1,000,000 − (W2+W3+W4)`, frozen at **383,000** · ② grade **four axes** (§2 · §5a · §5b · §5c) separately · ③ write the outcome into KEY THRESHOLDS + the calendar row · ④ **`git mv` the card to `docket/graded/` AND build the 9/24 card in the same session.** ⛔ **No WARN cohort is registered for the w/e Sep 12 week** — if one appears, size it against the L-08 floor (~20,000) BEFORE the print, not after.
3. 📅 **9/25 ×2 — Oct-2 NFP card freeze + ALFRED payroll vintage table (WQ-175 ②).** The card must satisfy gate #14 and **enumerate BOTH LFPR directions at every U-3 level** (L-27 partition defect). Recompute freeze-thaw LEG A on the revised vintage BEFORE reading September (L-02).
4. 🆕 **9/10 FIND — TEMPLATE FIX OWED, and it is small: split `ΔMA` from `MA_next` everywhere a card computes them.** They depend on different inputs (`R` vs the retained sum) and therefore age on different clocks; the 9/10 card presented them as one object and `MA_next` went stale by +250 on a 1,000-unit revision while `ΔMA` was exact. **Already applied to the 9/17 card §3; not yet applied to `docket/TEMPLATE_claims_card.md`.** → **L-31 realized ONE PRINT after L-31 was written**, which is the argument for mechanizing rather than remembering.
5. 📅 **2026-10-08 — Canada counter-tariff US-exporter employment re-check #1** (re-dated from 9/8 today after a NO-EVIDENCE grade). **Named and unchecked: IL DCEO, MN DEED, IA Workforce Development, WI DWD WARN primaries.** ⚠️ **The grade is SEARCH-NOT-FOUND, not verified-absent** — upgrading it requires those four primaries, per the fleet rule that a broader grep is not an upgrade.
6. 🔴 **STILL NOT STARTED — base-rate the CORRECTIVE, not just the original** (L-25; `35/4 = 8.75×`; L-32 is instance n=2). Trigger to build = a comparative TIMING/performance claim. **Build debt → `BUILD_DEBT.md`; near-term BD-23 · BD-26 · BD-31 · BD-13.** ⚠️ **BD-13 is CLOSED-BY-LAPSE, not discharged** — the MSFT 605 lapsed LOW so its WA-ESD primary no longer matters for attribution, but the row was carried as *"verified"* on two secondaries for 13 days and that defect is unfixed in kind. 🔒 Full text → `STATUS_DETAIL.md` § `pickup-rotated-20260910b`.
7. 🔒 **PRE-REGISTERED, UNTOUCHED:** v4 JOLTS-August NET bands (~Oct 6) — NET >0 ⇒ v4 → 2 · NET ≤0 a 4th month ⇒ v4 → 4 · NET ≤0 but hires rate ≥3.4% ⇒ HOLD 3. **v8 restore-to-3: leg 1 banked 9/4 (+55K); leg 2 is the Oct 2 print.**
8. 🔒 **C2-0 SWEEP RE-RUN 9/10 from `workbook/PREDICTIONS.tsv` — ZERO rows trip it.** Six OPEN: LAB-03 7% · LAB-08 4% · LAB-11 50% · LAB-12 8% · LAB-18 15% · LAB-19 60%. Only LAB-19 clears ≥60% and it fails the 60-day staleness leg (registered 9/4). 🔧 **BUT the as-made values moved today:** LAB-03 scores **as-made 65%** and LAB-11 **as-made 55%** at resolution (DAEDALUS H2, re-derived at the artifact). **LAB-03 is therefore a ≥60% threshold row in a book that is 0-for-5 there** — the live 7% protects nothing.
9. ✅ **9/10 EVE — WQ-214 LANDED: the EXIT-RULES VINTAGE SWEEP is now an UNCONDITIONAL C1 step; the `:101` banner is retired.** First run: **4/4 rails current**. Nothing further owed before 9/17 claims. 🔒 → `STATUS_DETAIL.md` § `wq214-vintage-sweep-installed-20260910`.

## § `bottom-line-rotated-20260917` — BOTTOM LINE as it stood at the 2026-09-10 closeout (verbatim, rotated from STATUS.md 2026-09-17; no figure changed)

## BOTTOM LINE

**✅ 2026-09-10 — CLAIMS GRADED, NOTHING FIRED, SCORE UNCHANGED 29/75.** Initial claims **206,000** [w/e Sep 5, DOL 9/10 08:30, primary] — **flat WoW** on a prior revised up 1,000; 4-wk MA **206,000** (−1,500); continuing claims **1,774,000** [w/e Aug 29] (−1,000, prior revised down 4,000); IUR **1.2%**. **BAND B / NO ACTION on all five pre-committed axes** — single-print, vector-13 counter, T-01 MA basis, continuing-claims, Kill B. **Zero fired, zero armed, no packet routed**, exactly as §7 pre-committed for bands A/B. **The realization channel still has not turned, and one flat week is not evidence that it won't.**

🔴 **THE MA FELL 1,500 WHILE THE LEVEL DID NOT MOVE, AND THAT IS ARITHMETIC.** `R` = w/e Aug 8 = 212,000 left the window: `ΔMA = (206,000 − 212,000)/4 = −1,500`, which is what DOL published, to the unit. **The docketed term `(X−200)/4` would have said `+1,500` — the sign inversion the 9/7 card predicted, realized at the modal print.** ⚠️ **Next week is not comparable and a reader will think it is:** the roll-off becomes 207,000, so an identical 206K print gives ΔMA **−250** — `1,500/250 = 6.0×` smaller — which would read as "improvement slowing" and is nothing of the kind.

**THE CARD EARNED ITS KEEP ON THE REGENERATIONS, NOT THE GRADE.** ✅ **A1.2's clause fired on its FIRST live use and the hypothetical it wrote three days earlier occurred to the unit:** retained sum `617,000 → 618,000`, T-01 bound **`383,000 → 382,000`**. A 383,000 print would now fire T-01 **and require CARL**, where the frozen number would have missed it. 🔧 **The same step found a NEW defect in my own card:** §3 has two computed columns on **two clocks** — `ΔMA` depends only on `R` (unmoved, exact) while `MA_next` depends on the retained sum (moved ⇒ **every row rotted by +250**). The card said *"regenerate §3's table"* without saying which half could rot. **That is L-31 realized ONE PRINT after L-31 was written.** Fixed forward in the 9/17 card; the template fix is still owed (PICKUP 4).

⛔ **TWO THINGS I AM DELIBERATELY NOT CLAIMING.** ① **The "card catches a revision STATUS had not followed" count stays at THREE** (8/13, 8/20, 9/10) — today's two revisions arrived **with** the release, so STATUS could not have followed them and did not fail to. Counting them would inflate a self-critical statistic in the *flattering* direction. ② **The MSFT/Xbox cohort (763) is not attributed in either direction:** `763 / 20,000 = 3.8%` of the L-08 floor, `20,000 / 763 = 26.2×` below it. **Claims were flat — that is not evidence the cohort was absorbed, and a rise would not have been evidence it wasn't.**

🔴 **THE CANADA ROW: GRADED, AND THE HONEST ANSWER IS "NO EVIDENCE", NOT "NO EFFECT".** Counter-tariffs on CA$27.6B took effect 9/8; **no WARN filing and no announced furlough at any US ag-equipment or pulp-and-paper exporter cites them.** ⚠️ **Tagged SEARCH-NOT-FOUND, explicitly NOT verified-absent** — bounded web search only, with **four state WARN primaries named and unchecked** (IL/MN/IA/WI). **Two days has no power anyway:** WARN's 60-day rule puts a 9/8-caused separation at ~Nov 7, and the WARN→claims lag is a further 6 weeks. **Re-docketed 2026-10-08.** 🔴 **The finding that cuts against the easy read: every named layoff the search returned runs the OTHER way** — RYAM Témiscaming, ~400–425 workers, caused by **US** tariffs on **Canadian** goods. That is Canadian employment, not mine; importing it as counter-tariff evidence would be a sign error on the transmission leg.

**Next — Wed 9/16 the L302 commission (now on the ledger, where a boot can see it), then Thu 9/17 claims off the frozen card.** Then the Oct-2 NFP card freeze and ALFRED vintage table (9/25), JOLTS August (~Oct 6), and **NFP September Fri Oct 2**, which supplies leg 2 of vector 8's restore counter.

## § `thresholds-rotated-20260917` — KEY THRESHOLDS claims rows + header + calendar row + PENDING INPUTS line + matrix v7/v13 rows as they stood 2026-09-10 (verbatim, rotated from STATUS.md 2026-09-17; no figure changed)

### STATUS header line as it stood at the 2026-09-10 closeout
**Last Updated:** 2026-09-10 18:0x ET *(eve: WQ-214 installed; WALTER lane drained)* · prior 11:1x ET *(claims print day; PROME-spawned WQ-184 L0 due-row session)* · ✅ **CLAIMS w/e Sep 5 GRADED off the frozen card: 206K → BAND B / NO ACTION on all five axes; ZERO of five pre-committed conditions fired. SCORE UNCHANGED 29/75; NO VECTOR MOVED.** 🔴 **The 4-wk MA fell 1,500 on a FLAT level — mechanical, not signal.** ✅ **The card's A1.2 regeneration clause fired on its first live use and its 9/7 hypothetical occurred to the unit.** 🔧 **New defect found AT GRADE: §3's two computed columns age on two clocks — `ΔMA` survived, every `MA_next` value rotted by +250 (L-31, one print after L-31 was written).** ✅ **9/17 card FROZEN 7d ahead · inbox DRAINED 5/5 · Canada counter-tariff row GRADED (no US-exporter employment evidence, SEARCH-NOT-FOUND) and re-docketed 2026-10-08.** See BOTTOM LINE.

### KEY THRESHOLDS — initial claims (MA basis) row, 2026-09-10 vintage
| Initial claims (4-wk MA basis) | **206K / MA 206,000** [w/e Sep 5 · obs 2026-09-05 · **DOL 2026-09-10**] | <230K drift · 230-250K accelerating (vec 13→3) · **>250K sustained 4+wk = T-01** · **251-300K single = ARM T-01 provisional** · **>300K single = T-02 FIRE** | T-01 🔴 CARL+REGINALD; T-02 🔴 REGINALD (ORANGE→RED)+HENRY. ✅ **GRADED 9/10 → BAND B / NO ACTION, ZERO fired** (card `docket/graded/GRADING_CARD_20260910_claims.md`). `250,000 − 206,000 = 44,000` below T-01 on MA basis (**gap WIDENED 1,250**); `300,000 − 206,000 = 94,000` below T-02. Run **200/212/207/204/207/206** *(w/e Aug 29 revised 206→207 WITH this release)*. 🔴 **MA −1,500 on a FLAT level is mechanical:** `ΔMA = (206,000 − 212,000)/4 = −1,500`, matching DOL exactly; the docketed `(X−200)/4` said **+1,500**. ⚠️ Next week the term is **`(X − 207,000)/4`** ⇒ same 206K gives **−250**. 🔒 9/7 unfollowed-revision narrative → `STATUS_DETAIL.md` § `thresholds-rotated-20260910`. |

### KEY THRESHOLDS — initial claims (bull side) row, 2026-09-10 vintage
| Initial claims (bull side) | **206K — `206,000 − 185,000 = 21,000` above the line** | ≤185K ×5 clean sessions = Kill B. **9/10: count stays 0 of 5.** Distance UNCHANGED from 9/3 (level flat) | exit-all check |

### KEY THRESHOLDS — continuing claims row, 2026-09-10 vintage
| **Continuing claims** | **1,774K** [w/e Aug 29 · obs 2026-08-29 · DOL 2026-09-10] — −1,000 WoW on a prior **revised DOWN 4,000** (1,779K → 1,775K); 4-wk MA 1,779K (−1,750); IUR **1.2%** | Vector-7 drop-to-2 needs **<1,750K ×4wk** (`1,774,000 − 1,750,000 = **24,000** away`, **ZERO** of four banked) | vector 7 — **a COST/duration gauge; NOT an early-warning instrument and will not be used as one.** ⚠️ **True WoW move is −1,000, not −5,000** — the 29K distance published 9/7 was against a 1,779K since revised to 1,775K |

### MONITORING CALENDAR — the Sep 17 forward row as written 2026-09-10
| 🔴 **Thu Sep 17 08:30** | **Initial claims w/e Sep 12** + CC w/e Sep 5 | 🔒 **CARD FROZEN 2026-09-10, 7 days ahead** → `docket/graded/GRADING_CARD_20260917_claims.md` (built at the closeout that graded the 9/10 card — C2a's recurring trigger). Partition check: **4 tables, 1 verified, 3 hand-proved, 0 DEFECTS.** 🔴 **Roll-off week CHANGES: `R` = w/e Aug 15 = 207K ⇒ term `(X − 207,000)/4`.** T-01 MA bound **`X > 383,000`** — **re-solve at the print.** |

### PENDING INPUTS — drained line as written 2026-09-10
> 🟢 **DRAINED 2026-09-10 — both lanes empty by `ls`.** All 5 items consumed this session (3 top-level: DAEDALUS as-made H2, PROME L302 ledger gap, HAWK Canada perimeter; 2 WALTER: SIG-W-20260908-006/-009, `board_log.tsv` rows written, files `git mv`d to `processed/`). 🔒 Prior windows → `STATUS_DETAIL.md` § `pending-inputs-20260904`.

### CONVERGENCE MATRIX rows v7 / v13 as they stood 2026-09-10
| 7 | UI exhaustion / CC grind | **3** 🟠 | flat | CC <1,750K × 4 wk → exhaustion pipeline draining, drop to 2 |
| 13 | Claims / shadow gap | **2** 🟡 | flat | >250K sustained → T-01 🔴 CARL/REGINALD; **<200K ×4 → drop to 1 (count now 0 of 4 — RESET, the streak died at w/e Aug 1's revision to 200K)** |  *[carried: 207 · −23 · 300K · 1.1%]*

## § `calendar-graded-20260917` — claims w/e Sep 12 GRADED off `docket/graded/GRADING_CARD_20260917_claims.md` (written 2026-09-17 08:4x ET)

**Primary:** DOL/ETA news release, embargo line *"8:30 A.M. (Eastern) Thursday, September 17, 2026"* — text extracted from the release PDF (`https://www.dol.gov/ui/data.pdf`, fetched 08:30–08:34 ET), never from a summary of it (see L-33).

| Series | As published 9/17 | Prior (as published) | Change |
|---|---|---|---|
| Initial claims SA, w/e Sep 12 (advance) | **196,000** | 206,000 (**unrevised**) | **−10,000** |
| 4-wk MA SA | **203,250** | 206,000 (unrevised) | **−2,750** |
| Initial claims NSA | 152,286 | 176,916 | −24,630 (−13.9%); seasonal factors expected −16,515 (−9.3%) |
| Yr-ago SA / NSA (w/e Sep 13 2025) | 233,000 / 195,433 | — | — |
| Continuing claims SA, w/e Sep 5 (advance) | **1,730,000** | 1,769,000 (**revised DOWN 5,000** from 1,774,000) | **−39,000** |
| CC 4-wk MA SA | 1,761,250 | 1,777,750 (rev. down 1,250 from 1,779,000) | −16,500 |
| Insured unemployment rate SA / NSA | **1.1%** / 1.0% | 1.2% / 1.1% | −0.1 / −0.1 |
| CC NSA | 1,577,344 | 1,671,605 | −94,261 (−5.6%); expected −58,374 (−3.5%) |
| Yr-ago CC SA / NSA | 1,925,000 / 1,759,884 | — | — |
| UCFE / UCX initial (w/e Sep 5) | 398 / 495 | 388 / 409 | +10 / +86 |

**State colour (w/e Sep 5, from the release):** largest increases MI +2,075 · CA +1,967 · WA +952 · NJ +686 · NE +606; largest decreases NY −3,790 · KY −778 · AR −367 · RI −200 · HI −197. **Florida in neither list.**

### ① Regeneration on the as-published vintage (card §4 order, BEFORE reading the level)
- Window `W1/W2/W3/W4` = w/e Aug 22 **204,000** · Aug 29 **207,000** · Sep 5 **206,000** (unrevised) · Sep 12 **196,000**. `(204,000 + 207,000 + 206,000 + 196,000)/4 = 813,000/4 = 203,250` ✅ equals DOL's MA to the unit.
- `R` = w/e Aug 15 = 207,000, unmoved ⇒ **`ΔMA = (196,000 − 207,000)/4 = −2,750`** ✅ matches DOL's published −2,750 exactly.
- Retained sum `W2+W3+W4 = 617,000`, **unchanged** (no retained week revised) ⇒ §3's `MA_next` column and §5a's T-01 bound **`X > 383,000` both stood** — the first week since the card series began that nothing was void at the print.

### ② Four axes graded separately
| Axis | Reading | Band | Pre-committed assignment | Result |
|---|---|---|---|---|
| §2 single print | 196,000 | **B** (186,000–229,000) | NO ACTION | ✅ no action, no packet |
| §5a T-01 MA basis | 196,000 vs bound 383,000 | **T01-a** | T-01 does NOT fire | ✅ MA 203,250; `250,000 − 203,250 = 46,750` away, **widened 2,750** |
| §5b vector-13 `<200,000` | 196,000 ≤ 199,000 | **V13-a** | counter **0 → 1 of 4** | 🔧 **STATE CHANGE** — score unmoved (drop-to-1 needs 4 consecutive; a ≥200,000 print RESETS) |
| §5c continuing claims | 1,730,000 < 1,750,000 | **CC-1** | vector-7 count **0 → 1 of 4** | 🔧 **STATE CHANGE** — `1,750,000 − 1,730,000 = 20,000` inside the bar; score unmoved |
| Kill B (band A) | 196,000 > 185,000 | — | count stays **0 of 5** | `196,000 − 185,000 = 11,000` above the line (was 21,000) |
| T-02 (band E) | — | — | — | `300,000 − 196,000 = 104,000` away |
| LAB-03 (7%) | — | — | — | `250,000 − 196,000 = 54,000` away; **confidence not moved** |

**Routing per §7:** bands A/B and CC-1 are STATUS-only. **Nothing routed, nothing armed.** Two counters at 1-of-4 are two weeks from nothing; **one week is not a streak, in either direction.**

**What the level is and is not.** 196,000 is the **third print ≤196,000 in 120 weeks** (189,000 w/e Jul 18 · 190,000 w/e Apr 25 · 196,000 w/e Sep 12; FRED ICSA, 120 obs). The NSA drop (−13.9%) overshot the seasonal expectation (−9.3%) by 4.6pp — that is the entire SA decline, and **NSA/YoY grade nothing on this card.** A benign print is not hawkish fuel (7/29 FOMC grade); it is nothing.

### ③ 9/24 card built in the same session (C2a recurring trigger)
`R` = w/e Aug 22 = **204,000** ⇒ **`ΔMA = (X − 204,000)/4`**; retained `207,000 + 206,000 + 196,000 = 609,000` ⇒ **T-01 MA bound `X > 391,000`** (was 383,000 — moved 8,000 because a 196,000 replaced a 204,000 in the retained trio). Modal repeat 196,000 ⇒ `MA_next = (609,000 + 196,000)/4 = 201,250`, `ΔMA = −2,000`. **Counters carried onto the card: v13 1 of 4 · v7 1 of 4 · Kill B 0 of 5.**

### Shadow-adjusted basis — what PROME's dashboard shows and why LABOR does not quote it
`FORGE/tools/market-data/config.py` L116-119 carries `"shadow_adj": {"label": "est w/ shadow adj", "add": 55000}` on the Init Claims row — a **flat +55,000 constant added to the FRED level** (206,000 + 55,000 = 261,000 on 9/16; 196,000 + 55,000 = **251,000** today). **SEARCH-NOT-FOUND** for any derivation of the 55,000 in `STATUS.md`, `STATUS_DETAIL.md`, `workbook/KB.tsv` (grep `shadow` · `55,000` · `55K`; the only "shadow" row is KB-LAB-076, federal separations, unrelated). **LABOR's bands are denominated in the RAW SA advance figure and every LABOR figure is RAW SA.** ⚠️ **251,000 sits in MY band D (251,000–300,000 = ARM T-01 provisional)** — a reader who grades the adjusted display against LABOR's bands will arm a trigger that the instrument did not fire. Asked PROME (memo 9/17) to source the constant or retire the parallel display.

## § `l302-instruments-20260917` — the four-instrument COMMISSION (DOCKET L302), cold detail (written 2026-09-17 08:4x ET)

**Rule carried on every item (PROME packet 9/7, Codex):** the decision this evidence could change — INCLUDING against LABOR's thesis — written before any build; history and arithmetic here, current reading + decision consequence on the boot path only. **Disposition vocabulary:** built / diagnostic / declined-with-reason. **All four land DIAGNOSTIC; none earns a band (L-15: base-rate a threshold before building it — none is base-rated yet).**

### ① Indeed postings — OPERATIONAL AUDIT (disposition: DIAGNOSTIC, tracker VERIFIED LIVE; VX row SUPERSEDED)
| Audit item | Finding | Source |
|---|---|---|
| Feed | `github.com/hiring-lab/job_postings_tracker` raw CSV, no auth; national + state files pulled 2026-09-17 08:3x ET | tracker run + direct curl |
| Latest observation | **2026-09-11** (pulled 9/17 = **6-day lag**); series starts 2020-02-01, n=2,415 daily obs | `aggregate_job_postings_US.csv` |
| Units | SA index, **% change vs Feb-1-2020 = 100**, **7-day trailing average**; national splits `new postings` (flow, ≤7d on Indeed) from `total postings` (stock); states carry ONE blended index | repo README §Methodology |
| Revision behaviour | **Whole history re-seasonally-adjusted**: Bundesbank daily-SA method adopted Nov 2024; projected seasonal factors for the current year come from the preceding 3 years ⇒ **every series revises when factors are re-estimated**; README: *"Historical numbers have been revised and may differ from previously reported values"* | README |
| FRED mirror | `IHLIDXUS` 2026-09-11 = **103.15** — identical to the repo's total-postings value ⇒ same feed, FRED adds nothing | `fetch.py fred IHLIDXUS` |
| Refresh cadence | weekly per README (commit-date probe via GitHub API returned no dates this session — NOT verified; cadence is README-stated) | — |
| Consumers (fleet grep) | `AGENTS/LABOR/workbook/VX.tsv` (FROZEN) · `AGENTS/LABOR/workbook/KB.tsv` · `AGENTS/CARL/workbook/KB.tsv` (mentions) · LABOR `CLAUDE.md`. **No live STATUS/brief on any desk cites it** | grep STATUS/NEXUS_BRIEF/CLAUDE/workbook fleet-wide |

**Current reading (2026-09-11):** national **total postings 103.15** (Δ1wk +0.74pt · Δ4wk +1.37pt · **YoY −0.19%** vs 103.35 on 2025-09-12) · **new postings 96.81** (Δ1wk −0.71 · Δ4wk −0.37 · **YoY −13.62%** vs 112.07) · **Florida 105.58** (Δ4wk +1.38pt; YoY in the memo table). **VX-LAB-1.04 carried −5.9% YoY at 2026-03-09** — 192 days stale; on today's vintage the total-postings YoY at 2026-03-06 reads −0.5%, so the frozen row's figure is not even reproducible on the revised series. **VX is FROZEN — the row is retired by supersession here, not edited.**

**The test PROME ordered, run on my own history — do postings LEAD hires?** Monthly-average Indeed total postings vs JOLTS hires (`JTSHIL`), **3-month log changes, 2022-01..2026-07**, Pearson r by lead (positive k = postings earlier):
| k (postings lead hires by) | −3 | −2 | −1 | 0 | **+1** | +2 | +3 |
|---|---|---|---|---|---|---|---|
| total postings, r (n) | +0.14 (52) | +0.05 (53) | +0.05 (54) | +0.18 (55) | **+0.31 (54)** | +0.20 (53) | +0.12 (52) |
| new postings, r (n) | +0.16 (52) | +0.13 (53) | +0.08 (54) | +0.14 (55) | +0.10 (54) | −0.07 (53) | −0.06 (52) |
**Verdict: a weak 1-month lead in the STOCK series (r = +0.31 ⇒ `r² = 0.096`, under 10% of variance) and NO lead in the FLOW series.** ⛔ **Postings do not usefully lead hires on this history; the row stays DIAGNOSTIC and cannot carry a T-10 / vector-4 band.** Decision it could change: none, mechanically — but the reading is informative in BOTH directions and both are recorded: **against the thesis**, the postings STOCK is flat YoY (−0.2%) and rising 4 weeks running (national +1.37pt, FL +1.38pt) — employers are NOT withdrawing postings, which is not what a deepening freeze looks like; **for it**, the FLOW is −13.6% YoY while the stock holds ⇒ postings are staying open longer (slower filling), which is the low-hire signature. **Neither half is scored.**

### ② Labor-supply AGE DECOMPOSITION of the +683K LF move (disposition: DIAGNOSTIC — tests and narrows, does not establish cause)
CPS, SA, thousands, FRED pulled 2026-09-17 (BLS Employment Situation, USDL-26-1435 vintage). ⚠️ **Each age series is seasonally adjusted independently, so cohorts do not sum to the total; the residual is stated.**

| Cohort | LF May | Jun (Δ) | Jul (Δ) | **Aug (Δ)** | LFPR May → Aug | Emp Jul → Aug |
|---|---|---|---|---|---|---|
| Total 16+ (`CLF16OV`) | 170,078 | 169,358 (**−720**) | 169,094 (−264) | **169,777 (+683)** | 61.8 → 61.6 | +569 (`CE16OV`) |
| 16–19 (`LNS11000012`) | 6,269 | 6,221 (−48) | 6,121 (−100) | 6,254 (**+133**) | 35.7 → 35.7 | −7 |
| 20–24 (`LNS11000036`) | 15,592 | 15,615 (+23) | 15,534 (−81) | 15,688 (**+154**) | 70.5 → 70.9 | +140 |
| **25–54 prime (`LNS11000060`)** | **109,201** | **108,393 (−808)** | 108,549 (+156) | **108,577 (+28)** | **83.9 → 83.4** | **−6** |
| 55+ (`LNS11024230`) | 39,005 | 39,095 (+90) | 38,927 (−168) | 39,253 (**+326**) | 37.1 → 37.2 | +354 |
| Cohort sum vs total | — | −743 vs −720 (resid −23) | −193 vs −264 (resid −71) | **+641 vs +683 (resid +42)** | — | — |

**What it narrows.** The June **−720K** was a **PRIME-AGE** event (−808K, LFPR 83.9 → 83.3). The August **+683K** was **NOT** prime-age (+28K; LFPR 83.4, still **0.5pp below May**) — it was **55+ (+326K, LFPR 36.9 → 37.2)** and **under-25 (+287K)**. **Prime-age LF is `109,201 − 108,577 = 624K` below its May level; the cohort that contracted has not recovered.** So the aggregate REVERSED while the composition says the contraction STANDS — these are different cohorts moving, not one move retracing. ⚠️ **Sampling error binds:** BLS's Technical Note puts the 90% CI on the monthly change in household employment at roughly ±600K; a single cohort-month is inside noise, and only the 3-month prime-age level change (−624K) approaches the edge. **Decision it could change:** LAB-19 (60%, MECHANISM) resolves on the AGGREGATE letter (LF MoM >0 in ≥2 of Sep/Oct/Nov) and **the letter stands** — but this decomposition says LAB-19 can resolve TRUE while my CORE TENSION's supply-shrink premise is still intact at prime age, so **the prime-age LF level is now reported beside LAB-19 at every NFP as a diagnostic line, and a TRUE LAB-19 will NOT by itself rewrite the tension.** **Against the thesis:** prime-age LF back ≥109,000K with U-3 flat would mean the supply confound is gone AND demand absorbed it — the bull read; the bar is `109,000 − 108,577 = 423K` of prime-age re-entry.

**Breakeven payroll, assumptions explicit (an ESTIMATE, not a gauge):** `CNP16OV` grew `(275,415 − 274,955)/4 = 115K/mo` Apr→Aug. LF at constant LFPR 61.6%: `115 × 0.616 = 70.8K/mo`; employment at constant U-3 4.1%: `70.8 × 0.959 = 67.9K/mo` ⇒ **household-basis breakeven ≈ 68K/mo.** Assumptions: (a) published CNP growth embeds the Jan-2026 population control and does NOT observe intra-year immigration changes; (b) LFPR and U-3 constant; (c) no CES/CPS adjustment (multiple jobholders, self-employed, agriculture) — payroll breakeven is the same order, ~65–75K. **Under a low-net-migration assumption (CNP ≈ 60–70K/mo), breakeven ≈ 35–45K.** ⇒ **August +162K exceeds breakeven by `162 − 68 = 94K` (published-pop basis) to `162 − 40 = 122K` (low-migration basis).** PROME's correction of the brainstorm figure is confirmed: +162K clears a 30K breakeven by MORE than it clears a 100K one, not less.

### ③ Aggregate private weekly HOURS (Table B-4; disposition: DIAGNOSTIC row added to the release assessment, shared revision exposure)
| Series | Aug 2026 | Jul | May (3m) | Aug 2025 | MoM | 3m (ann.) | YoY |
|---|---|---|---|---|---|---|---|
| `AWHAE` index of aggregate weekly hours, ALL employees, total private (2007=100) | **117.2** | 116.8 | 116.7 | 115.8 | **+0.34%** | +0.43% (≈+1.7% ann.) | **+1.21%** |
| `AWHI` same, production & nonsupervisory (2002=100) | 124.7 | 124.6 | 124.8 | 123.5 | +0.08% | −0.08% | +0.97% |
| Cross-check `USPRIV × AWHAETP` (M hrs) | `135,752 × 34.4 = 4,669.9` | `135,625 × 34.3 = 4,651.9` | — | `134,937 × 34.2 = 4,614.8` | **+0.39%** | — | **+1.19%** ✅ |
**Decomposition of the August gain:** employment `135,752/135,625 − 1 = +0.09%` × workweek `34.4/34.3 − 1 = +0.29%` — **three-quarters of the hours gain is the workweek tick, and 0.1 hr is the publication unit, so it flips on revision.** ⚠️ **SHARED REVISION EXPOSURE: same CES sample as NFP — every L-02 revised-series rule applies; recompute on the revised vintage before reading any month.** **Decision it could change:** Kill A / the "employers using more or less labor" read. Hours +1.2% YoY with the hires RATE at 3.2% = **more hours from the same workers** — consistent with BOTH a freeze (no churn) and healthy demand without churn; **it cannot discriminate between them and earns no band.** Recorded against the thesis: total private labour input is RISING, not contracting.

### ④ State initial-claims BREADTH, Florida first (disposition: DIAGNOSTIC; primary = ETA 539)
**Source:** `https://oui.doleta.gov/unemploy/csv/ar539.csv` (ETA 539 weekly state claims, 13.4 MB, 112,287 rows, pulled 2026-09-17 08:3x ET; field `c3` = state UI initial claims, NSA; `rptdate` = filing week). **Latest state week = w/e 2026-09-05** — state data lag the national advance by one week; **FRED's `FLICLAIMS` (5,510 w/e Sep 5) is the same series two units off (5,508 in the 539 file — one late-count revision).** Breadth = states whose 4-wk-avg NSA initial claims are UP vs the same 4 weeks a year earlier (NSA needs a YoY basis; a WoW count is seasonal noise). 51 jurisdictions (50 + DC; PR/VI excluded).

| Week ending | States UP YoY (4wk avg) | | Week ending | States UP |
|---|---|---|---|---|
| 2026-06-13 | 11/51 | | 2026-08-01 | 13/51 |
| 06-20 | 11/51 | | 08-08 | 13/51 |
| 06-27 | 13/51 | | 08-15 | **8/51** |
| 07-04 | 15/51 | | 08-22 | 9/51 |
| 07-11 | 13/51 | | 08-29 | 8/51 |
| 07-18 | **19/51 (peak)** | | **09-05** | **9/51** |
| 07-25 | 14/51 | | single-week basis 09-05 | 19/51 |

**Sum of states w/e Sep 5: 175,155 vs 203,025 yr-ago = −13.7% YoY.** Worst 4wk YoY: DE +73.1% (465 vs 268 — a tiny base) · VT +23.7% · HI +21.5% · **NY +4.3%** · CO +4.3%; falling most: KY −56.0% · ND −43.9% · CT −40.2% · IL −32.6% · TX −25.3%.
**Florida:** 4wk `5,462 vs 5,956 = −8.3% YoY`; single week `5,508 vs 5,802 = −5.1%`; last 8 weeks 6,281 → 6,003 → 5,545 → 5,796 → 5,678 → 5,205 → 5,458 → 5,508 vs yr-ago 6,329 → 6,347 → 6,248 → 6,448 → 6,139 → 6,165 → 5,719 → 5,802 — **below year-ago in all 8 weeks.** Peers: TX −25.3% · CA −4.9% · GA −12.3% · WA −4.7%.
**Decision it could change:** vector 13's count and T-01 on the MA basis — **breadth is NARROWING (19 → 9 of 51 since mid-July), not widening; a claims wave shows in breadth before the national MA, and it is absent.** **Against the thesis, and it is the clearer half.** Florida is not a rising state — the FL row for CORAL/MARCO is "falling YoY, in line with the national −13.7%". ⚠️ **Not base-rated:** what breadth count preceded prior national-MA rises is NOT measured — **no band until it is (BD-33).**


## § `status-line-rotated-20260917` — the `**Status:**` lede + 7/6 retraction pointer as they stood 2026-09-10 (verbatim, rotated from STATUS.md 2026-09-17; no figure changed)
**Status:** 🟠 **HIRING INTENTIONS THAWED; THE REALIZED COUNT DID NOT FOLLOW — AND ON 9/1 THE INTENTIONS LEG STOPPED LEADING TOO.** July JOLTS: openings flat-to-up (7,271K, rate 4.3→4.4%) while **hires fell 278K and the hires RATE went 3.4 → 3.2%**. …  *[carried: 4.1% · 61.4% · −23 · +20K · −720K · 97K · 4% · 5,054 · 7,271 · 1.9% · 1.0% · −18K · 51.2 · 47.4]*
🔒 **[7/6 CLAIM — HALF RETRACTED 2026-08-05]** — the ISM-survey half (L-12); the WARN-filing half stands. → `STATUS_DETAIL.md` § `claim-retraction-20260805`.


<a id="calendar-graded-20260924"></a>
## § `calendar-graded-20260924` — claims w/e Sep 19 graded off the frozen card (written 2026-09-24)
**Primary:** DOL/ETA release, embargo line *"8:30 A.M. (Eastern) Thursday, September 24, 2026"*, `https://www.dol.gov/ui/data.pdf`, text extracted from the saved binary (sha256 prefix `4705665b`). Retained-week cross-read: `oui.doleta.gov/unemploy/wkclaims/report.asp` r539cy national table (w/e Aug 15 207,000 · Aug 22 204,000 · Aug 29 207,000). Graded 14:4x ET by a PROME-spawned WQ-184 session; LABOR was dark at 08:30.

| Quantity | Value | Arithmetic |
|---|---|---|
| Initial claims w/e Sep 19 (advance) | **197,000** | DOL: *"a decrease of 1,000 from the previous week's revised level"* |
| w/e Sep 12 revised | 198,000 (was 196,000) | DOL: *"revised up by 2,000"* |
| w/e Sep 5 revised | 207,000 (was 206,000) | release table column + identity `816,000 − (204,000 + 207,000 + 198,000) = 207,000` |
| 4-wk MA | **202,250** | `(207,000 + 207,000 + 198,000 + 197,000)/4 = 809,000/4` ✅ |
| Revised prior MA | 204,000 (was 203,250) | `(204,000 + 207,000 + 207,000 + 198,000)/4 = 816,000/4` ✅ |
| `ΔMA` | **−1,750** | `(197,000 − 204,000)/4` — card §3, exact |
| T-01 MA bound (re-solved) | `X > 388,000` (frozen 391,000) | `1,000,000 − (207,000 + 207,000 + 198,000)` |
| Continuing claims w/e Sep 12 | **1,719,000** (+2,000) | prior revised 1,730,000 → 1,717,000; 4-wk MA 1,744,000 |
| NSA initial | 163,811 (+6.7% WoW vs seasonal +6.8%) | YoY `163,811/180,992 − 1 = −9.5%` — colour only |

**Axes:** §2 band **B** NO ACTION · §5a **T01-a** (does not fire) · §5b **V13-a ⇒ 1 → 2 of 4** (week 1 still `<200,000` at 198,000) · §5c **CC-1 ⇒ 1 → 2 of 4** · Kill B 0 of 5. **Routing: none.** **Score 29/75 unchanged.** Card: `docket/graded/GRADING_CARD_20260924_claims.md` §9.

<a id="status-rotated-20260924"></a>
## § `status-rotated-20260924` — STATUS.md surfaces superseded by the 9/24 grade (verbatim as they stood 2026-09-17, rotated 2026-09-24; no figure changed)

**Header lines 2–3:**
**Last Updated:** 2026-09-17 08:4x ET *(claims print day; PROME-spawned WQ-184 L0 due-row session; DOCKET L302 commission DELIVERED)* · ✅ **CLAIMS w/e Sep 12 GRADED off the frozen card: 196K → BAND B / NO ACTION on the single-print axis — but TWO COUNTERS STARTED: vector-13 `<200K` 0 → 1 of 4 · vector-7 `CC <1,750K` 0 → 1 of 4 (CC 1,730K, −39K). SCORE UNCHANGED 29/75; NO VECTOR MOVED; NOTHING ROUTED.** 🔴 **MA −2,750 = `(196,000 − 207,000)/4`, DOL to the unit; no retained week revised.** ✅ **L302 FOUR INSTRUMENTS DELIVERED — all DIAGNOSTIC, none earns a band; 3 of 4 cut AGAINST this book · 9/24 card FROZEN · inbox DRAINED 6/6.** See BOTTOM LINE.
**Status:** 🟠 **LOW-FIRE / LOW-HIRE, REALIZATION CHANNEL STILL QUIET.** Claims 196K (band B) · JOLTS hires rate 3.2%, NET −18K (3rd negative month) · NFP Aug +162K · U-3 4.1% on LFPR 61.6%. **9/17: prime-age LF still 624K below May while the aggregate rebounded — the supply confound narrowed, not resolved.** 🔒 Prior lede (9/1 JOLTS) + the 7/6 half-retraction pointer → `STATUS_DETAIL.md` § `status-line-rotated-20260917`.

**Matrix v7 / v13 rows:**
| 7 | UI exhaustion / CC grind | **3** 🟠 | flat | CC <1,750K × 4 wk → exhaustion pipeline draining, drop to 2. ✅ **9/17: CC 1,730,000 [w/e Sep 5] ⇒ count 0 → 1 OF 4** — one week is not a streak, and CC revises (w/e Aug 29 went 1,774K → 1,769K) |
| 13 | Claims / shadow gap | **2** 🟡 | flat | >250K sustained → T-01 🔴 CARL/REGINALD; **<200K ×4 → drop to 1 — ✅ 9/17: 196,000 ⇒ count 0 → 1 OF 4** (any ≥200K print RESETS; the prior streak died at w/e Aug 1's revision). 🔧 **L302 ④: state breadth 9/51 UP YoY, narrowing since 19/51 mid-Jul — diagnostic, cuts against** |  *[carried: 207 · −23 · 300K · 1.1%]*

**KEY THRESHOLDS — claims rows:**
| Initial claims (4-wk MA basis) | **196K / MA 203,250** [w/e Sep 12 · obs 2026-09-12 · **DOL 2026-09-17**] | <230K drift · 230-250K accelerating (vec 13→3) · **>250K sustained 4+wk = T-01** · **251-300K single = ARM T-01 provisional** · **>300K single = T-02 FIRE** | T-01 🔴 CARL+REGINALD; T-02 🔴 REGINALD (ORANGE→RED)+HENRY. ✅ **GRADED 9/17 → BAND B / NO ACTION on §2; §5b V13-a ⇒ vector-13 counter 0 → 1 OF 4** (card `docket/graded/GRADING_CARD_20260917_claims.md` §9). `250,000 − 203,250 = 46,750` below T-01 on MA basis (**gap WIDENED 2,750**); `300,000 − 196,000 = 104,000` below T-02. Run **204/207/206/196**, prior UNREVISED; `813,000/4 = 203,250` ✅ DOL. 🔴 **`ΔMA = (196,000 − 207,000)/4 = −2,750`, DOL to the unit.** 3rd print ≤196K in 120 wks. NSA/YoY = colour, graded by nothing. ⚠️ **Next week `R` = w/e Aug 22 = 204,000 ⇒ `(X − 204,000)/4`; T-01 MA bound `X > 391,000`.** ⛔ **LABOR quotes RAW SA only — the dashboard's +55,000 'shadow adj' (`config.py`) is not a LABOR basis; 251K would sit in MY band D.** 🔒 Full grade → `STATUS_DETAIL.md` § `calendar-graded-20260917`. |
| Initial claims (bull side) | **196K — `196,000 − 185,000 = 11,000` above the line** | ≤185K ×5 clean sessions = Kill B. **9/17: count stays 0 of 5.** Distance NARROWED 10,000 from 9/10 | exit-all check |
| **Continuing claims** | **1,730K** [w/e Sep 5 · obs 2026-09-05 · DOL 2026-09-17] — **−39,000 WoW** on a prior **revised DOWN 5,000** (1,774K → 1,769K); 4-wk MA 1,761,250 (−16,500); IUR **1.1%** (−0.1) | Vector-7 drop-to-2 needs **<1,750K ×4wk** — ✅ **9/17: CC-1 ⇒ count 0 → 1 OF 4** (`1,750,000 − 1,730,000 = 20,000` inside the bar) | vector 7 — **a COST/duration gauge; NOT an early-warning instrument and will not be used as one.** ⚠️ CC revises every week (w/e Aug 29: 1,774K → 1,769K) — read the as-published prior; one week is not a streak |

**PREDICTIONS — both LAB-03 rows (the first was a stale duplicate carried since 7/31; removed from the hot half 9/24):**
| LAB-03 | Claims breach 250K | **7%** (from 10) | Q2-Q3 | 7/31: MA 202,750, **down 5 straight weeks**. LAB-17 — the one *dated* mechanism carrying this — resolved ❌ **on sizing, not on a mistimed lag**, so there is no rescheduled version of it. Held above zero only for the Aug-28 QCEW benchmark + the undated severance-exhaustion channel. |
| LAB-03 | Claims breach 250K | **7%** *(🔧 **scores AS-MADE 65%** — re-derived 9/10)* | Q2-Q3 | 🔴 **9/10: MA 206,000, `250,000 − 206,000 = 44,000` away. Unmoved by a band-B print.** ⚠️ **The live 7% protects nothing: at resolution this is a ≥60% THRESHOLD row, the bucket where I am 0-for-5.** Held above zero only for the undated severance-exhaustion channel. |

**C2-0 note:**
> 🔒 **C2-0 STALE-HIGH-CONFIDENCE SWEEP — RE-RUN 2026-09-10 from `workbook/PREDICTIONS.tsv`, re-derived not read off a list. RESULT: ZERO ROWS TRIP IT.** Only LAB-19 (60%) clears the ≥60% bar and it fails the 60-day staleness leg (registered 9/4). 🔧 **As-made values moved today: LAB-03 → 65%, LAB-11 → 55%** (DAEDALUS H2, re-derived at the artifact). 🔒 Prior runs → `STATUS_DETAIL.md` § `predictions-resolved`.

**EXIT RULES banner:**
## EXIT RULES (recalibrated Jul 2) · **Kill rail re-derived: 2026-09-04** [BLS USDL-26-1435] · 🔧 **VINTAGE SWEEP (C1, unconditional per WQ-214): run 2026-09-10 18:0x ET — 4/4 rails CURRENT on the 9/10 vintage, no repair owed.** 🔒 Per-rail enumeration → `STATUS_DETAIL.md` § `wq214-vintage-sweep-installed-20260910`.

**Calendar row (9/24, pre-grade):**
| 🔴 **Thu Sep 24 08:30** | **Initial claims w/e Sep 19** + CC w/e Sep 12 | 🔒 **CARD FROZEN 2026-09-17, 7 days ahead** → `docket/GRADING_CARD_20260924_claims.md`. 🔴 **Roll-off `R` = w/e Aug 22 = 204,000 ⇒ term `(X − 204,000)/4`.** T-01 MA bound **`X > 391,000`** — re-solve at the print. **Counters LIVE on the card: v13 `<200K` 1 of 4 (any ≥200K RESETS) · v7 `CC <1,750K` 1 of 4.** |

**NEXT SESSION PICKUP — the 2026-09-17 slate:**
> 🔒 **The 2026-09-10 slate (items 1–9 as written) → `STATUS_DETAIL.md` § `pickup-rotated-20260917`.** This slate is FORWARD work only.

1. 📅 **Thu 9/24 08:30 — claims w/e Sep 19. Card is FROZEN** (`docket/GRADING_CARD_20260924_claims.md`). **Grade order, pre-committed:** ① regenerate the THREE window-derived quantities on the as-published vintage before reading the level — `ΔMA = (X − 204,000)/4`, the `MA_next` column (retained 609,000), the T-01 bound `X > 391,000` · ② grade four axes separately (§2 · §5a · §5b · §5c) — **two counters are LIVE: v13 `<200K` 1 of 4 (≥200,000 RESETS to 0) · v7 `CC <1,750K` 1 of 4 (≥1,750,000 RESETS)** · ③ write outcome into KEY THRESHOLDS + matrix v7/v13 + calendar · ④ `git mv` the card to `docket/graded/` AND build the 10/1 card in the same session. ⛔ No WARN cohort registered for w/e Sep 19; size any that appears against the L-08 floor (~20,000) BEFORE the print.
2. 📅 **9/25 ×2 — Oct-2 NFP card freeze + ALFRED payroll vintage table (WQ-175 ②).** Card must satisfy gate #14, enumerate BOTH LFPR directions at every U-3 level (L-27), recompute freeze-thaw LEG A on the revised vintage BEFORE reading September (L-02) — **and now carry two L302 DIAGNOSTIC rows, no bands: `AWHAE` aggregate private hours (Aug 117.2, +0.34% MoM, +1.21% YoY; same CES sample ⇒ same revision exposure) and prime-age LF level (Aug 108,577K, `109,201 − 108,577 = 624K` below May) reported beside LAB-19.**
3. 🆕 **L302 FOLLOW-THROUGH — all four instruments landed DIAGNOSTIC (cold detail `STATUS_DETAIL.md` § `l302-instruments-20260917`).** (a) **BD-33** — state-breadth script (`ar539.csv`, ETA 539 primary) lives in scratch; promote to `tools/state_claims_breadth.py` and **base-rate breadth vs prior national-MA rises BEFORE any band** (L-15). (b) **BD-34** — `job_postings_tracker.py` prints no YoY; add national total/new + FL YoY. **VX-LAB-1.04 (−5.9% YoY, 2026-03-09) is SUPERSEDED — total postings YoY −0.19% at 2026-09-11; VX is FROZEN, so the supersession lives here and in PUBLISHED.tsv, never as an edit to VX.** (c) Lead test on my own history: **r = +0.31 at +1 month (`r² = 0.096`) — no usable T-10 lead; diagnostic only.**
4. 🔴 **SHADOW-ADJUSTED DASHBOARD FIGURE — NOT A LABOR BASIS.** `FORGE/tools/market-data/config.py` adds a flat **+55,000** to ICSA ("est w/ shadow adj"); **SEARCH-NOT-FOUND** for its derivation in any LABOR ledger. On today's print it displays **251,000 — inside my band D (ARM T-01).** Asked PROME (memo 9/17) to source or retire it. **Until ruled: every LABOR figure and packet says RAW SA, explicitly.**
5. 📅 **2026-10-08 — Canada counter-tariff US-exporter employment re-check #1.** Named and unchecked: IL DCEO · MN DEED · IA Workforce Development · WI DWD WARN primaries. Grade is SEARCH-NOT-FOUND, not verified-absent; upgrading requires those four primaries.
6. 🔴 **STILL NOT STARTED — base-rate the CORRECTIVE, not just the original** (L-25; L-32 n=2). **BD-32 template fix still owed** (split `ΔMA` from `MA_next` in `docket/TEMPLATE_claims_card.md` — applied by hand on the 9/17 and 9/24 cards, not yet in the template). Near-term debt: BD-23 · BD-26 · BD-31 · BD-32 · BD-33 · BD-34 · BD-35.
7. 🔒 **PRE-REGISTERED, UNTOUCHED:** v4 JOLTS-August NET bands (~Oct 6) — NET >0 ⇒ v4 → 2 · NET ≤0 a 4th month ⇒ v4 → 4 · NET ≤0 but hires rate ≥3.4% ⇒ HOLD 3. **v8 restore-to-3: leg 1 banked 9/4 (+55K); leg 2 is the Oct 2 print.** LAB-19 resolves on the AGGREGATE letter (LF MoM >0 in ≥2 of Sep/Oct/Nov) — **a TRUE will not by itself rewrite CORE TENSION while prime-age LF sits 624K below May (item 2).**
8. 🔒 **C2-0 SWEEP RE-RUN 9/17 from `workbook/PREDICTIONS.tsv` — ZERO rows trip it; no confidence moved this session.** Six OPEN: LAB-03 7% (as-made 65%) · LAB-08 4% · LAB-11 50% (as-made 55%) · LAB-12 8% (as-made 60%) · LAB-18 15% · LAB-19 60% (registered 9/4, fails the 60-day leg). LAB-03 due 2026-09-30: `250,000 − 196,000 = 54,000` away with two prints left — **resolve ❌ at the 10/1 print unless a ≥250K print lands; do not re-arm it.**
9. 🆕 **L-33 (9/17) — a fetch tool's SUMMARY of a primary returned figures the document does not contain** (213,000 / 216,000 / 1,641,000 for a PDF that says 206,000 / 207,000 / 1,774,000 — the 9/10 release, fetched pre-embargo). Caught only by extracting the saved binary. **Standing guard: every fetched primary is text-extracted from the saved file; a summary is a READER and is never quoted. BD-35 mechanizes it.**

**BOTTOM LINE as of 2026-09-17:**
## BOTTOM LINE

**✅ 2026-09-17 — CLAIMS GRADED, NOTHING FIRED, SCORE UNCHANGED 29/75 — BUT TWO COUNTERS ARE NOW RUNNING.** Initial claims **196,000** [w/e Sep 12, DOL 9/17 08:30, primary PDF text] — **−10,000 WoW on an UNREVISED prior**; 4-wk MA **203,250** (−2,750); continuing claims **1,730,000** [w/e Sep 5] (**−39,000**, prior revised down 5,000 to 1,769,000); IUR **1.1%**. **Band B / NO ACTION on the single-print axis; T-01 (MA basis, `46,750` away), T-02 (`104,000` away) and Kill B (`11,000` above) untouched.** The two counters — **vector-13 `<200K` at 1 of 4** and **vector-7 `CC <1,750K` at 1 of 4** — are the pre-committed readings of §5b and §5c, both need four consecutive weeks, and **both RESET on one print the other way.** Nothing routed; §7 says bands A/B and CC-1 are STATUS-only.

🔴 **THE MA MOVE IS ARITHMETIC AGAIN, AND THIS WEEK THE CARD WAS EXACT.** `R` = w/e Aug 15 = 207,000: `ΔMA = (196,000 − 207,000)/4 = −2,750`, which is what DOL published, to the unit. **No retained week revised, so for the first time nothing on the card was void at the print** — §3's `MA_next` and §5a's bound (383,000) both stood. Next week `R` = 204,000 and the T-01 bound moves to **391,000** because a 196,000 replaced a 204,000 in the retained trio. ⚠️ **A reader will call −10,000 a "sharp improvement." The NSA drop (−13.9%) overshot the seasonal factor (−9.3%) by 4.6pp; that gap IS the whole SA decline, and one week of it grades nothing.**

🔴 **L302 — FOUR INSTRUMENTS DELIVERED, ALL DIAGNOSTIC, AND THREE OF FOUR CUT AGAINST THIS BOOK.** ① **Indeed:** feed live (obs 9/11), total postings **103.15 (YoY −0.19%)**, new postings **96.81 (YoY −13.62%)**, FL **105.58** rising 4 weeks; the postings→hires lead on my own 2022–26 history is **r = +0.31 at +1 month (`r² = 0.096`)** — **no usable lead, row stays diagnostic; VX-LAB-1.04's −5.9% is superseded.** ② **Age decomposition:** the June **−720K** was prime-age (**−808K**); the August **+683K** was **55+ (+326K) and under-25 (+287K), prime-age only +28K** — **prime-age LF is 624K below May; the cohort that contracted has not recovered.** LAB-19 resolves on the aggregate letter regardless; a TRUE will not rewrite CORE TENSION on its own. Breakeven ≈ **68K/mo** on published population growth (`115 × 0.616 × 0.959`), 35–45K under low migration — **+162K clears either.** ③ **Aggregate private hours (`AWHAE`) 117.2, +0.34% MoM, +1.21% YoY** — three-quarters of it the 0.1-hr workweek tick; same CES sample as NFP, same revision exposure; more hours from the same workers fits BOTH a freeze and healthy demand, so no band. ④ **State breadth (ETA 539, w/e Sep 5): 9 of 51 states up YoY on a 4-wk basis, down from 19 at the mid-July peak; sum of states −13.7% YoY; Florida −8.3% YoY (5,462 vs 5,956), below year-ago in all of the last 8 weeks.** A claims wave shows in breadth first, and it is absent.

⛔ **TWO THINGS I AM DELIBERATELY NOT CLAIMING.** ① **The shadow-adjusted 251,000 on PROME's dashboard is not mine and I am not grading it** — it is ICSA + a flat 55,000 from `config.py` with no derivation in any LABOR ledger; against MY bands it would read ARM T-01, which the instrument did not do. ② **"Postings are rising, so hiring will follow"** — the lead test says the stock series explains under 10% of hires variance one month ahead; I will not cite Indeed as a T-10 lead in either direction.

**Next — Thu 9/24 claims off the frozen card (counters 1 of 4 ×2), Fri 9/25 the Oct-2 NFP card freeze + ALFRED vintage table (now carrying the hours and prime-age LF diagnostic rows), JOLTS August (~Oct 6) on v4's pre-registered NET bands, and NFP September Fri Oct 2 (v8 leg 2; LAB-03 resolves at the 10/1 claims print).**

