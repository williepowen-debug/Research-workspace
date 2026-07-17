# VULCAN — WALTER AI_INFRA_CAPEX axis check: findings + handoff

> ## ⚠️ PROVENANCE — READ BEFORE CITING
> **Written by a READ-ONLY-SPAWNED VULCAN instance on 2026-07-16, WALTER-coordinated (teams-mode).**
> **This is NOT the live VULCAN session's own work.** This instance never ran a VULCAN boot, never ran `boot.py`, never checked a gate live, and never pulled a primary for S1–S4. **All S1–S4 knowledge here is a file read of `STATUS.md` as of 2026-07-12, not independent verification.**
> **Nothing in this document has been applied to the convergence matrix, VX.tsv, KB.tsv, PREDICTIONS.tsv, or STATUS.md.** Every re-mark below is a **RECOMMENDATION for the live VULCAN to ratify or reject.**
> **The composite (11/20) and the S1/S2/S3/S4 scores are untouched by design** — a spawned instance silently re-scoring the canonical matrix is the sibling-drift failure this flag exists to prevent.
> **Live VULCAN: ratify or reject each item below, then delete this banner and fold what survives into your own surfaces.**

**Coordinated by:** WALTER · **Directed by:** Will · **Date:** 2026-07-16
**Tasks:** (1) adjudicate whether WALTER's filter killed the AI_INFRA_CAPEX obsolescence/input-cost angles; (2) close VULCAN's own disclosed obsolescence gap.
**Delivered to WALTER via SendMessage** 2026-07-16 (two reports). This file is the durable record — *file > verbal*.

---

## 1. WHY THIS EXISTS — VULCAN was never wired into WALTER

Until 2026-07-16, VULCAN had **zero rows in WALTER's ROUTING_TABLE, no mention in any WALTER design doc, and no `inbox/WALTER/` directory.** Nothing could route to VULCAN and nothing ever did. Meanwhile the `AI_INFRA_CAPEX` BOARD cluster — VULCAN's exact domain — grew to **23 signals** (real footprint **38**, incl. 15 carrying `cluster_secondary: AI_INFRA_CAPEX`), routed to HENRY / LIQUID / VIOLET instead.

**Fixed 2026-07-16 (all Will-approved, all landed):**

| Change | Status |
|---|---|
| `AI_CAPEX` domain code → **VULCAN action**; VIOLET/HENRY/WATT/RED info. Precedence PRIORITY, **IMMEDIATE on a capex CUT**. Chain `AI_INFRA` | **LANDED** (FORMAT_SPEC v0.14 / ROUTING_TABLE v0.18) |
| `AGENTS/VULCAN/inbox/WALTER/` delivery lane | **LANDED** |
| Micron (CIK 0000723125) added to RESEARCH-INTAKE `edgar_8k` + new `memory-cycle` and `ai-capex` queries | **LANDED, LIVE** (PROME, lane commit `faddb1e`) — VULCAN is the first agent added to the lane's coverage since April |
| CLUSTER_TAXONOMY v0.6 — bidirectional revisit triggers + geography-vs-mechanism `cluster_secondary` guidance (forward-only, grandfathered) | **LANDED** |
| Hyperscalers → `edgar_8k` | **SENT, PENDING** — ⚠️ see §6 constraint |
| VULCAN's proposed 5-axis taxonomy re-cut | **RECORDED, NOT ADOPTED** — needs Will + the live VULCAN |

**VULCAN is NOT on the §3.5 pull-complete exemption list** (only CARL + RED are) — VULCAN receives pushed handoffs from here.

---

## 2. TASK 1 — WALTER's filter: NOT broken. Verdict per angle.

| Angle | Verdict | Confidence |
|---|---|---|
| **Input-cost** | **WALTER's fault — but NOT the filter.** An **INTAKE gap + a CLUSTERING miss.** The gates never saw the news. Explicitly NOT "the domain went quiet" — it's VULCAN's hottest channel | **HIGH** |
| **Obsolescence** | **Never a separate axis in the way the 6/6 frame assumed** — but see §3, where this reasoning was **partially refuted** | **MODERATE** |

### 2.1 The kill-log evidence — 6 relevant kills, 6 correct

Every semi/memory/obsolescence/input-cost row across all 270 rows of `AGENTS/WALTER/filtered/kill_log.tsv`:

| Date | What | Gate | Judgment |
|---|---|---|---|
| 04-19 | Capex/CFO 92% hyperscaler chart | Novelty 1.00 | ✅ CORRECT — intra-batch dup of dispatched SIG-419-030 |
| 06-27 | Apple/CXMT DRAM (FirstSquawk) | Novelty 0.97 | ✅ CORRECT — hard dup of SIG-627-018, routed same morning |
| 06-27 | ex-AI Q1 GDP −1.1% decomposition | Novelty 0.97 | ✅ CORRECT — dup of SIG-627-017; ROI/macro, not input-cost |
| 07-10 | "memory is the commodity this cycle / **DDR5 consumer pricing rolling over**" | Novelty + Credibility 0.75 | ⚠️ CORRECT KILL — see below |
| 07-10 | Cycle diagram + Financelot "memory up only on $MU earnings" (6/25) | Novelty 0.80 | ✅ CORRECT — stale + evergreen re-send |
| 06-28 | Housing-stock depreciation (CXCarroll) | Novelty 0.40 | ✅ CORRECT — housing, not GPU |

**Zero filter failures.**

**The 7/10 DDR5 row — the only near-miss, and it exonerates the gates twice:**
- It claimed DDR5 ***consumer*** pricing rolling over. **VULCAN's S2 trigger series is the *server contract* price** (TrendForce 2Q26: DRAM +58-63% QoQ, NAND +70-75% QoQ). Consumer spot ≠ server contract — the fleet's `proxy_segment_masks_trigger_series` class. **Even if true, it does not touch the S2 trigger.**
- Unquantified advocacy, no source figure → killing on Credibility is right.
- **But WALTER's own kill note reads: *"informal watch-item for HENRY (AI/semi). Not dispatched."*** Dated **2026-07-10 — the day VULCAN was built.** Not a filter fault; the wiring gap, visible in WALTER's own log.

### 2.2 The S2 contradiction — resolved. Two mechanisms, both UPSTREAM of the filter.

**Mechanism 1 — INTAKE GAP (decisive).** VULCAN's S2 read is built on:

| Source | Date | Datum | In `/BOARD/` (494) | In `kill_log` (270) |
|---|---|---|---|---|
| **TrendForce** press releases | 3/31, 6/1, 6/22/26 | DRAM +58-63% / NAND +70-75% QoQ | **0** | **0** |
| **Micron FQ3 FY26** earnings release | 6/24/26 | Rev **$41.46B** vs $32.75-34.25B guide; DRAM +207% YoY; CEO: can fill only **50-67%** of demand | **0 as a signal** (3 passing mentions inside other signals) | **0** |

**Zero and zero.** The largest single input-cost datum in the domain — a ~$7-9B guidance beat confirming a structural supply deficit — **never entered WALTER at all.** Not killed. Never seen. **There is no filter verdict on a document the filter never received.**

**Why:** WALTER's intake = Will's Telegram drops + the RESEARCH-INTAKE lane (EIA / EDGAR-8K / Treasury / CFTC / FRED / newssweep). Company earnings releases and trade-research price prints sit outside all six. **VULCAN's S2 is built from primaries WALTER did not ingest.** → fixed, §1.

**Mechanism 2 — CLUSTERING MISS.** The memory signals *are* on the BOARD, filed by **geography** not **mechanism**:

| Signal | Content | Filed under |
|---|---|---|
| SIG-W-20260626-001 | 🔴 KOSPI AI/semi crash, **Samsung/SK Hynix −9%**, circuit breakers | **ASIA_CHINA** |
| SIG-W-20260628-005 | KOSPI 5 halts; Goldman leveraged **Samsung/SK Hynix** ETF loop | **ASIA_CHINA** |
| SIG-W-20260702-007 | KOSPI new low; driver = **SK Hynix −11.5% / Samsung −8.5%** | **ASIA_CHINA** |
| SIG-W-20260627-002 | **SanDisk NAND** monthly RSI 99.01, "most overbought ever" | **POSITIONING_VALUATION** |
| SIG-W-20260627-018 | Apple/**CXMT DRAM** | AI_INFRA_CAPEX, but `domain: ASIA_CONTAGION` |

**Four of five S2-relevant BOARD signals sit outside the cluster whose count was used to declare the angle decayed.** → CLUSTER_TAXONOMY v0.6 addresses this forward-only.

**Count correction (VULCAN → WALTER):** WALTER's single "input-cost" signal, SIG-W-20260627-018 (Apple/CXMT), **is not a clean input-cost signal** — its domain header is `ASIA_CONTAGION`, its payload is a Pentagon-blacklist export-control story (**S4 as much as S2**), and its input-cost content is one clause. **The input-cost axis had effectively ZERO clean signals in the cluster, not one.**

---

## 3. TASK 2 — the obsolescence gap VULCAN disclosed. **Part A = NO.**

**VULCAN's disclosed gap (task 1, verbatim):** *"I have zero obsolescence coverage… If a hyperscaler extended server useful-life in a Q2 10-Q and you missed it, that's a real (b) I am not equipped to see."*

**Tested. Verdict: NO — no in-window datum WALTER should have caught. WALTER's clean bill stands honestly, not by default.**

### 3.1 The mechanism is the CALENDAR — the disclosure channel was shut for the whole window

| Date | Event | vs. the 5/11→7/16 window |
|---|---|---|
| **4/30/26** | **GOOGL + AMZN file Q1 CY26 10-Qs** | **11 days BEFORE the window opens** |
| 5/11 → 7/16 | *(no hyperscaler 10-Q filed)* | **the window — channel CLOSED** |
| **7/22 – 7/30** | GOOGL 7/22 · MSFT + META 7/29 · AMZN 7/30 | **AFTER the window closes** |

**The window contains zero hyperscaler 10-Q filings.** Nothing existed to route.

### 3.2 Every material obsolescence datum is PRE-window

| Change | Name | Effect | Date |
|---|---|---|---|
| 4→6 yrs | MSFT | — | **FY22 Q4** |
| 4→6 yrs | GOOGL | −$3.9B dep / +$3.0B NI / **+$0.24 EPS** | **2023** |
| 4→4.5→5→5.5 | META | **−$2.9B** FY25 dep | **through 2024-25** |
| 5→6 yrs | ORCL | −$733M opex / **+$573M NI** | **FQ1 FY25** |
| **6→5 yrs (SHORTENED)** | **AMZN** | **$920M charge / −$700M op income**; cited "increased pace of technology development, particularly AI/ML" | **eff. 1/1/2025** |
| Burry: **$176B** understatement 2026-28 across GOOGL/AMZN/META/MSFT/ORCL | — | claim, not disclosure | **Nov 2025** |
| **Rubin full production** (the generation-reset) | NVDA | availability H2 2026 | **CES, Jan 2026** |

**Strongest evidence for the negative:** Silicon Analysts, *"Hyperscaler AI Capex 2026: $434B Trailing Four Quarters, D&A Lag, Debt Wave"* (`siliconanalysts.com/analysis/hyperscaler-ai-capex-depreciation-wall-2026`), **published 7/10/26 — six days inside the window, on precisely this question — reports NO new useful-life change May–July 2026.** A specialist source, in-window, on-topic, finding nothing. About as strong as a negative gets.

**Evidence deliberately NOT used — secondary GPU pricing.** Sources are GPU brokers / SEO farms quoting **mutually contradictory numbers for the same part** (H100 SXM5 2026: $25-35K, $6-15K, *and* $18-22K). Incentive-flagged sellers (`incentive_flag_source_weighting`). Real directional drift exists and Rubin is a real cadence compression (Hopper 2022 → Blackwell 2024 → **Rubin 2026** → Rubin Ultra 2027), **but there is no citable in-window datum. Not manufactured.**

**Intake-gap vs filter-miss: NEITHER. It's the calendar. WALTER didn't miss it — it hadn't happened yet.**

---

## 4. THE DURABLE FINDING — obsolescence is a REAL HOLE, not a sub-facet

> **⚠️ This section REVERSES what this instance told WALTER in task 1. The reversal is the finding.**

**WALTER's challenge (correct, and it killed VULCAN's own argument):** *"if useful-life assumptions are disclosed quarterly in 10-Qs, that IS an observable series with a cadence — which would undercut your own structural argument."*

**Conceded.** The task-1 claim *"obsolescence has no independent observable series"* is **REFUTED**. It **is** a series; it **has** a cadence (quarterly, in the PP&E/depreciation footnote). The correct explanation for the 5/11→7/16 silence is **not** "no series" — it is **"quarterly series, window fell between prints."** Same surface, entirely different mechanism.

**And the demotion argument fails on a second leg — the ROI angle zeroes depreciation out by construction:**

**SIG-W-20260604-014** (FT/Panmure Liberum, *"Only Amazon clears a positive return under the most generous assumptions"*) — the flagship ROI signal — computes revenue ÷ capex with, per WALTER's own verify-research record, verbatim:

> *"operating costs, **depreciation**, power, salaries, interest ALL set to zero."*

**The ROI angle's best signal explicitly excludes depreciation.** Combined with the folding test (§5): **neither ROI nor financing captures obsolescence. It is a genuine hole in the frame, not a sub-facet to demote.**

### 4.1 Why it is worth instrumenting — the wedge (the real find)

> **The useful-life assumption is the precise wedge between VULCAN's S1 FCF read and reported EPS.**
>
> - **FCF is depreciation-INSENSITIVE** — D&A is a non-cash add-back. *This is exactly why S1's "FCF compression is universal, all 4 names, same quarter" read is robust.*
> - **Earnings are depreciation-SENSITIVE.**
>
> So the useful-life assumption is the **exact variable that lets capex-driven deterioration show up in CASH but not in EPS.**
> **S1 today measures both ends — capex and FCF — and nothing about the wedge between them. That is the hole.**

### 4.2 RECOMMENDATION (live VULCAN ratifies — NOT applied)

**Instrumented S1 sub-read + a pre-registered promotion trigger. NOT a new channel, NOT S5.**

**Why not a channel yet:**
- Depreciation shares S1's **antecedent AND its catalyst** (the same 7/22-7/31 earnings cluster). Per VULCAN's own independence discipline — *count the shared root once* — **a channel that can only fire when S1 fires is not independent.**
- **S5 is already spoken for** (AI-infra financing, tier-2, not yet promoted).
- Promoting on **zero in-window evidence** would be exactly the drift the #1 channels-first guard forbids.

**Proposed instrumentation:**

| Name | `useful_life_assumption` | Vintage | Re-verified since? |
|---|---|---|---|
| MSFT | 6y | FY22 Q4 | **No** |
| GOOGL | 6y | 2023 | **No** |
| META | 5.5y | 2024-25 | **No** |
| AMZN | 5y (subset) | eff. 1/1/2025 | **No** |
| ORCL | 6y | FQ1 FY25 | **No** |

- **Read the PP&E/depreciation footnote at each 10-Q.**
- **Threshold — note the DIRECTION ASYMMETRY:**
  - Any **extension** → 🟠 **earnings-quality flag** (flatters EPS, zero cash effect).
  - Any **shortening** → 🔴 **management conceding economic life < book life** — the AMZN 1/1/25 precedent, and by far the more informative direction.
  - **4 of 5 names extended; AMZN alone shortened. A SECOND shortening is the signal.**
- **Pre-registered promotion trigger:** **≥2 names change useful-life at 7/22-7/31 → promote to a channel. 0-1 → stays an S1 sub-read**, and the "never-a-separate-axis" read is confirmed **empirically instead of structurally.** **Resolves on the clock in 6 days** — same catalyst as VULCAN-03 (GOOGL 7/22) and VULCAN-01/06 (7/29-31). **Count the capex root once.**

⚠️ **The trigger is NOT armed by any instrument — see §6.**

---

## 5. TWO RETRACTIONS — both favored WALTER; WALTER independently verified both

**These are in VULCAN's own record, not just WALTER's. The lesson is in `LESSONS.md` (L-08).**

| # | The task-1 claim | The evidence | Status |
|---|---|---|---|
| **i** | *"`cluster_secondary` is unused here"* — recommended WALTER start using it | **199 tags in active use** across the taxonomy (WALTER's own recount: **192 signals**): BANK_COLLATERAL 33 · CONSUMER_STAGFLATION 28 · POSITIONING_VALUATION 25 · FED_FRAMEWORK 20 · PC_STRESS 19 · IRAN_HORMUZ 15 · **AI_INFRA_CAPEX 15** · HYDROCARBON_INFRA 11 · ASIA_CHINA 11. WALTER had already shipped it | **RETRACTED** — inferred "unused" from the *primary*-cluster count without grepping the field |
| **ii** | *"obsolescence content is FOLDED INTO the financing signals (SIG-626-008 FCF crater, SIG-626-031 Oracle −$23.7B) — so WALTER's axis count was wrong a second way"* | Grep for `depreciat\|useful.life\|obsolescen\|amortiz\|D&A`: **SIG-626-008 → 0 hits. SIG-626-031 → 0 hits. SIG-627-017 → 0 hits.** | **RETRACTED — WALTER's axis count was RIGHT.** A structural guess, asserted while holding zero obsolescence coverage, never checked |

**The failure mode, named:** *in task 1 this instance demanded receipts from WALTER while shipping a hypothesis as an argument.* The filter adjudication was evidence-based and survived; the two claims made **from priors** both failed. **Asymmetric rigor is the lesson.** → `LESSONS.md` L-08.

---

## 6. ⚠️ CONSTRAINT — the 7/22-7/31 trigger is NOT armed. Do not assume coverage.

**WALTER checked the RESEARCH-INTAKE lane fetcher and reports:**

> **It is `type=8-K` ONLY and classifies by item code without reading exhibits — so it will NOT catch a 10-Q footnote.**

**Consequences for the live VULCAN:**
- The Micron `edgar_8k` addition **does** arm the **S2** memory lane (MU files an 8-K on earnings — first live test: **Micron FQ4 ~8/4/26**).
- It does **NOT** arm the **§4.2 useful-life trigger**. A useful-life change lives in a **10-Q PP&E footnote** — invisible to an 8-K item-code classifier.
- **The 7/22-7/31 useful-life read needs a DEWEY deep-research pull or the live VULCAN doing it by hand.** **It will not arrive by itself.**
- **Do not write "covered" against this in STATUS.** It is not.

---

## 7. BACKLOG READ — ~3 months of VULCAN's own domain, never delivered

**Did the routing gap cost us anything? Mostly untidy — with one genuine loss.** S1/S2/S4 reads are unchanged: S2 was built from **better primaries** (TrendForce/Micron) than anything on the BOARD, and S1's capex baseline came from filings. **The BOARD didn't hold VULCAN's domain — it held the MARKET'S REACTION to VULCAN's domain.** That is a real distinction and mostly explains why the gap was survivable.

### 7.1 The one that moves a channel — S3

**SIG-W-20260704-007** (PJM EEA2 grid emergency, 7/3/26; `cluster: CLIMATE_MACRO`, `cluster_secondary: AI_INFRA_CAPEX`; → AEOLUS, HENRY; conf 0.85):

- **DOE §202(c) authorizes PJM to curtail data centers ≥50MW on 15-minute notice.** Combined with the repo's own 7/16 PROME finding (**Manual 13 codification, 6/24 MRC = curtailment is now a PERMANENT tool**), this is a mechanism S3 does not have: **datacenter load is now POLICY-INTERRUPTIBLE.**
- **RECOMMENDED S3 framing correction — NAMEPLATE vs FIRM (live VULCAN to apply):** curtailability drives a wedge between **nameplate** interconnection demand and **firm deliverable** load. **WoodMac's 55GW utility-self-report is a nameplate-ish number; curtailable load is a different asset.** S3's **direction is UNAFFECTED** (guided capex still supports the PJM-official 32GW path, not 55GW) — **but the framing needs nameplate-vs-firm added, or the comparison is between incommensurable quantities.** Feeds VULCAN-06 (resolves 7/31) and the WATT seam reconcile.
- **Discipline worth adopting:** the signal's own verify-research refinement — ***heat = the TRIGGER, AI/data-center load = the STRUCTURAL AMPLIFIER***, explicitly NOT "AI caused the grid emergency." VULCAN was at risk of that overclaim. Pairs with L-02 (mechanism ≠ thermometer).

### 7.2 The disconfirming trio VULCAN did NOT hold — the steelman against its own S1

**The most valuable thing in the backlog is not new bear evidence. It is the disconfirming set.**

| Signal | Content | Why it cuts against S1 |
|---|---|---|
| **SIG-W-20260521-013** | NVDA 5/20 print **absorbed CLEAN** — post-print IV crushed **below 20d realized**, **no tail bid**, vol surface "decisively faded the catalyst" (conf 0.85) | The market **faded** the AI catalyst. Direct counter to S1 fragility |
| **SIG-W-20260622-009** | **Record SOXL outflow / record SOXS inflow** — leveraged-ETF traders flipped bearish on semis (conf 0.75) | Semi bearishness is **already crowded** |
| **SIG-W-20260702-016** | GS Prime Book: hedge funds de-grossed US tech at a **~−4σ record** (wk ending 6/25) — **record selling, NO cascade** (conf 0.75) | **Record de-grossing WITHOUT a cascade** — the concentration unwind may be **partly pre-positioned**, a real argument against the trade's asymmetry |

**Per RED discipline (present the strongest bull case): this trio is it, and S1 did not have it.** Recommend the live VULCAN fold it into S1's exit triad as standing counter-evidence.

### 7.3 S5-adjacent (for whenever S5 is promoted)

**SIG-W-20260622-002** — Bain Capital Euro CLO 2018-1 DAC **Class F → 'D'**: first **European CLO 2.0 rated-tranche default**, AI-software-loan channel **realizing** (conf 0.82, → BROCK). A realized credit event in the AI channel.

---

## 8. TAXONOMY — the 4-angle frame (RECORDED, NOT ADOPTED)

The 6/6 lock: *"4-angle agreement [financing + obsolescence + input-cost + ROI] is load-bearing; revisit only if angles fragment beyond 4 distinct axes."* WALTER's 7/16 classification of all 23: **financing 13 (~57%) · ROI ~5 · obsolescence 1 (stale since 5/11) · input-cost 1 · power 2 · muni/fiscal 1.** It didn't fragment — **it CONCENTRATED.** The written trigger did not fire, but its premise is dead.

**VULCAN's proposed re-cut (5 axes) — RECORDED, needs Will + the live VULCAN:**

| 6/6 angle | Proposal | Reasoning |
|---|---|---|
| Financing | **keep** — the real one (57%) | The mechanism by which capex actually gets cut. **S1's gate** |
| ROI | **keep** | The demand-side question |
| **Obsolescence** | ~~demote to sub-facet of ROI~~ → **NO. Keep as its own hole; instrument it** | **REVISED per §4** — ROI zeroes depreciation by construction; financing has 0 hits. Neither captures it |
| **Input-cost** | **promote + rename → "memory / supply-cost cycle"** | The one angle with a genuine independent price series and its own live trigger (contract −25% QoQ) |
| **Power** | **formalize** — already 2 signals; VULCAN's S3; now WATT's lane | A real axis, absent from the original 4 |
| **Muni/fiscal** | keep as a spillover facet of financing | |

**Caveat honored by WALTER and restated here:** VULCAN's S1-S4 is a **transmission** frame (`event → mechanism → repricing`); WALTER's is a **question** frame (*"does the buildout continue?"*). **They are different objects — forcing a merge breaks both. Arrive at any re-cut by the reasoning above, NOT by deference to VULCAN's frame, which is merely a month newer.**

**Also recommended and LANDED (CLUSTER_TAXONOMY v0.6):** the 6/6 revisit trigger was **one-directional** — it fires on fragmentation and **structurally cannot detect concentration**, the failure mode that actually occurred. Per the BRENT bidirectional-flip discipline: *"revisit if angle count >5 **OR any original angle falls below 2 signals in 60d**."* **Under that rule WALTER would have fired on 6/27 without Will having to ask.**

**On the split:** WALTER decided **KEEP** + cap **15→40**. VULCAN concurs — severing financing from capex substance would **cut S1's gate in half**, since financing stress is the mechanism by which capex gets cut. (WALTER's own honest counter — *HYDROCARBON_INFRA at 23 uncapped isn't proof 23 is fine* — is the right worry but doesn't change the call.)

---

## 9. CONFIDENCE + WHAT WOULD CHANGE MY MIND

| Claim | Confidence | What flips it |
|---|---|---|
| WALTER's gates are clean (6/6 kills correct) | **HIGH** | A killed row mis-scored here |
| Input-cost = intake gap + clustering miss, not filter | **HIGH** | A TrendForce/Micron item in any WALTER feed log that was then killed. Checked BOARD + kill_log + route_log: **zero** |
| **Part A = NO, no in-window (b)** | **HIGH — bounded, see below** | A dated 5/11→7/16 disclosure missed here |
| Filing-calendar mechanism (window has zero 10-Qs) | **HIGH** | It's a calendar; independently verifiable |
| Obsolescence not folded (WALTER's count was right) | **HIGH** | Direct grep, 0/0/0 |
| §4.2 sub-read not channel | **MODERATE — resolves on the clock 7/22-7/31** | ≥2 names changing useful-life next week |

**⚠️ WHAT THIS INSTANCE COULD NOT SEE — the live VULCAN should close these:**

1. **No EDGAR full-text pass over the four 10-Qs.** The Part-A NO rests on **trade press + one in-window specialist source**. A *quiet* estimate change disclosed only in a footnote could evade a press-based search. **Mitigant:** the only filings that could carry one (4/30) are out-of-window anyway, so this cannot convict WALTER *for the window as posed*. **But fleet memory says EDGAR FTS refutes trade-press negatives (`finding_edgar_fts_refutes_tradepress_negatives`) — the belt-and-braces version is an EDGAR FTS pass. Flagged, not done.**
2. **A change already decided internally and undisclosed until 7/22** is unknowable by construction (`private_by_construction_unverifiable`).
3. **This instance holds no live gate state.** All S1-S4 knowledge is a 7/12 file read.

---

## 10. RECOMMENDATION LEDGER — live VULCAN to ratify/reject

| # | Recommendation | Target surface | Status |
|---|---|---|---|
| R-01 | **Instrument the useful-life sub-read under S1** — 5 per-name baselines (§4.2), extension = 🟠 / **shortening = 🔴**, read the 10-Q PP&E footnote | STATUS S1 + THESIS S1 | **RECOMMENDED — not applied** |
| R-02 | **Pre-register the promotion trigger:** ≥2 names change useful-life at 7/22-7/31 → promote to a channel; 0-1 → stays a sub-read | `PREDICTIONS.tsv` (next free VULCAN-NN) | **RECOMMENDED — not applied** |
| R-03 | **S3 framing: add NAMEPLATE-vs-FIRM.** DOE §202(c) + Manual 13 codification = datacenter load is policy-interruptible. **Direction unaffected; framing incomplete** | STATUS S3 + THESIS S3 + VULCAN-06 | **RECOMMENDED — not applied** |
| R-04 | **Fold the disconfirming trio into S1's exit triad** as standing counter-evidence (§7.2) | STATUS exit triad | **RECOMMENDED — not applied** |
| R-05 | **KB rows** for the 5 useful-life baselines + the AMZN shortening precedent + the PJM §202(c) curtailment mechanism | `workbook/KB.tsv` | **RECOMMENDED — not applied** |
| R-06 | **Do NOT demote obsolescence into ROI** (reverses this instance's own task-1 advice) | taxonomy position | **RECOMMENDED — not applied** |
| R-07 | **Arm the 7/22-7/31 useful-life read by hand or via DEWEY** — the lane will NOT catch a 10-Q footnote (§6) | SCRATCH pickup | **RECOMMENDED — not applied** |
| R-08 | **Close the EDGAR FTS gap** on the four 10-Qs (§9 item 1) | next session | **RECOMMENDED — not applied** |

**Matrix scores (S1 3 / S2 2 / S3 3 / S4 3, composite 11/20) DELIBERATELY UNTOUCHED.** No recommendation above changes a score on this instance's authority.

---

*Sources for §3: Silicon Analysts 7/10/26 (hyperscaler depreciation wall); footnote brief (hyperscaler depreciation schedules / AI capex circularity); Deep Quarry (GPU useful lives; Amazon server-lifespan revision); Goldman Sachs GPU-useful-life sensitivity (via secondary); Q2 2026 earnings calendars. Company figures (MSFT/GOOGL/META/ORCL/AMZN useful-life changes + $ effects) are secondary-sourced — **the live VULCAN should re-verify against the filings before any of these becomes a KB row.***
