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

