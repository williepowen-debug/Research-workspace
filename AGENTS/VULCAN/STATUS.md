# VULCAN — STATUS

**Last Updated:** **session spans 2026-09-02 22:47 ET → 2026-09-03 07:1x ET** — stated as a span, not a point, because the clock crossed midnight mid-session and picking one date would be the narrative rather than the clock *(`[[finding_write_timestamps_from_the_clock_not_the_narrative]]`; every `date` call is in the record)*. **Analysis and market reads are 2026-09-02 vintage; the closeout is 2026-09-03.** (**PROME-orchestrated full owner session after 6 dark days.** VULCAN-16 GRADED · MU FQ4 date CONFIRMED at the issuer primary and it REFUTES my own 8/27 re-derivation · S1 YELLOW band TRIPPED on its registered trigger · READ-CAP split executed · inbox 17→0)
**Class:** Market-agent (AI-capex/semi/memory → systemic risk) · **Spawnable by:** PROME or Will · **Maturity:** **L3** (DAEDALUS 8/7 Production Ready)

> ## 📖 WHERE THINGS LIVE — read this before hunting (READ-CAP split, 2026-09-02)
> This file was **117,622 B = 217% of the 54,250 B physical read cap** and a boot `Read` returned a **truncated file with no error**. Split per `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md` rules 16-17 (P1, Will-ruled 2026-08-28).
>
> | Surface | Holds | On the boot path? |
> |---|---|---|
> | **`STATUS.md`** (this file) | **Canonical for SCORE, BAND STATE, FIRED-COUNT, current live read, owed items** | **YES — read whole** |
> | `CHANNEL_DETAIL.md` | The **evidence under** the scores — full per-channel bodies, verbatim at split. **LIVE, not archived.** | No — on-demand, per channel |
> | `THESIS.md` | Per-channel transmission-stage tables | No — on-demand |
> | `workbook/EXIT_PROTOCOL.md` | The kill rail (thesis-kill + channel-kill + rewrite trigger) | No — closeout read |
> | `archive/STATUS_ARCHIVE_2026-08.md` | 8/24 + 8/27 session records, **frozen** | No — history |
>
> ⚠️ **Rule 17 obligation rule:** `CHANNEL_DETAIL.md` is **OFF the boot path.** A new watch, standing rule or owed action written there **does not travel**. Put it here, in `workbook/PREDICTIONS.tsv`, or in `docket/CATALYSTS.tsv` as well.

---

## CONVERGENCE MATRIX (universal 5-pt + local state)

| # | Channel | Score (1–5) | Local state | Independence | Key signal [src, date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| **S1** | AI-capex concentration | **3 🟠** | 🔴 **YELLOW BAND TRIPPED 2026-09-02 — first trip in the retained series.** Mag-7 **33.5528%** (32.98 [8/20] → 32.87 [8/21] → 32.91 [8/26] → **33.55** [9/1]). Capex still being RAISED, not cut: 7/31 cluster FINAL, all four FY26 guides raised, agg ~$735-760B econ vs the $710-725B baseline (VULCAN-01 HIT). NVDA Q2 FY27 rev **$96.221B**, DC **$89.0B**, Q3 guide **$108.0B**. **NOT-FIRED** — the band is a level, the trigger is a conjunction. | S1+S3+S5 share ONE root (an AI-capex ROI disappointment) — **count it once** | Mag-7 **33.5528%** [SPY **fund** weight, holdings as-of **2026-09-01**, issuer-primary, own `tools/mag7.py`, validation `worst-err=0.000%`]; breadth RSP−SPY 63d **+3.70pp** (94.1 pctile) | **≥40% AND breadth ≤ −7.5pp** (conjunction), OR hyperscaler capex **cut** YoY |
| **S2** | Memory cycle | **3 🟠** *(held; justification unchanged from 8/13 — the equity leg stays retracted-as-support and NOT re-armed)* | **PHYSICAL LEG TURNED 8/27 AND IT GRADED VULCAN-16.** DDR5 **$53.93 (−0.12%)**, DDR4 **$91.05 (0.00%)** — the FIRST decline in the retained series (52.70 → 54.10 → 54.17 → **53.93**). ⚠️ **Magnitude is trivial and n=1: the −25% QoQ contract rule is NOT near firing and moved FURTHER from it.** ⚠️ **Two pre-committed readings MISSED (8/27 post-close, 8/28 Fri) — desk dark; next reading Fri 2026-09-04, cadence otherwise intact.** | **Not purely independent** — an AI-capex roll pulls memory demand with it | DDR5/DDR4 spot [TrendForce, Asia close **2026-08-27**]; equity spread **+3.31pp** [8/24 intraday] / **+2.34pp** [8/27 close, reconstructed] | Contract **−25% QoQ sustained**; or the 9/30 pre-specified re-arm rule grading MET |
| **S3** | AI-capex → power demand | **3 🟠** | **SEAM CLOSED 8/13 — adopt verbatim, never net or average: ~55 GW NAMEPLATE interconnection ceiling / ~32 GW FIRM coincident-peak.** Two quantities, not two rival forecasts. 🆕 **A THIRD siting constraint is now named beside credit and power: WATER.** The Colorado ROD cuts the Lower Basin **1.25 maf in each of CY2027 and CY2028 (AZ −760 kaf)** — a **signed schedule, not a projection** — and AZ's Phoenix-corridor DC siting sits on junior-priority CAP water [AEOLUS, 2026-08-27]. | Shares S1's root | 55 GW nameplate / 32 GW firm [VULCAN↔WATT seam, 8/13]; ORCL/NVDA PORTS-Pike phase schedule [NVDA Q2 FY27 10-Q] | Grid-side refusal or curtailment that removes FIRM capacity from a contracted DC build |
| **S4** | Supply-chain / geopolitics | **3 🟠** | **INSTRUMENTED 8/21 — 20 months of retained history; the shape is RE-ACCELERATION, not stress.** TSMC Jul-2026 **NT$467,580M**, +5.6% MoM, +44.7% YoY; **cumulative Jan-Jul YoY +37.0%** (the citable figure — the single-month YoY fires constantly on base effects). Band **no-stress**. 🆕 **CXMT is NOT on the BIS Entity List and a package has been prepared-but-unpublished since June 2026** — no model on this desk prices it [ZHAO, 2026-09-02]. | **The only cleanly independent root** | `tools/tsmc_watch.py` → `workbook/S4_SERIES.tsv`, SEC 6-K primary (CIK 0001046179), 3 zero-free-parameter validations/row | Equipment ban / fab-level cutoff, OR Taiwan kinetic |
| **S5** | **AI-infra financing** *(core since 8/3)* | **3 🟠** *(held — evidence much stronger, no red leg tripped)* | **FILING-PRIMARY AND IT IS A TIME SERIES.** CRWV DDTL ladder at ONE issuer: **SOFR+225** (Mar-26) → **+450** (May-26) → **+550** (Aug-26); recourse debt **$31,405M**, +51.5% in six months, effective rates 9-15%. **NVDA's guarantee book went $3.5B → $108.5B in one quarter (31×)**, starting FY2029 [Q2 FY27 10-Q]. ORCL **$260B** off-BS DC lease commitments + the **$3.3B** lessor guarantee maturing **Sept-2026**. 🆕 NVDA supply-and-capacity commitments ÷ annualised COGS: **1.45× → 2.90× in one quarter** [DEWEY REQ-001, arithmetic accepted]. | **PARTIALLY independent** — the financing-structure/regulatory leg fires on the balance sheet regardless of capex direction; the ROI leg shares S1's root | CRWV Q2 10-Q acc `0001769628-26-000366`; NVDA Q2 FY27 10-Q acc `0001045810-26-000075` | New issue flexes **+150bp or PULLED**, OR a **2nd jurisdiction** writes an IG threshold into a utility tariff, OR a developer **fails to post** mandated collateral |

**Composite: 15/25 — HELD, EIGHTH session (8/13 → 8/21 ×3 → 8/24 → 8/27 → 9/2)** · **S1 3 · S2 3 · S3 3 · S4 3 · S5 3**

> ⚠️ *That per-channel arithmetic line is **machine-read** by `scripts/validate_workbook.py` (boot leg 7), which reconciles it against `workbook/VX.tsv` **and** against the matrix above — three surfaces, because a footer restating a total is a second copy of the state. **Do not delete or reformat it.***
>
> *(9/20 at build → 10/20 → 11/20 → 12/20 on the 8/3 S2 upgrade → 15/25 on the 8/3 S5 promotion → held since. ⚠️ **The denominator changed on 8/3 — 12/20 (60%) and 15/25 (60%) are the same reading.**)*

**⚠️ A HELD COMPOSITE IS NOT A QUIET SESSION — and this one moved a BAND without moving a SCORE.** S1's yellow line was crossed on its registered instrument. **A band is a level; S1's trigger is a conjunction (≥40% AND breadth ≤ −7.5pp), and breadth is +3.70pp.** Nothing about the yellow trip licenses a score move, and I am not making one.

**Independence note:** an AI-capex ROI disappointment drives S1 (concentration), S3 (power demand) and S5 (financing) at once — **count the shared root ONCE** in any composite-stress call. S4 is the only cleanly independent root. S2 is no longer purely independent.

> 📖 **Full per-channel evidence bodies, verbatim → `CHANNEL_DETAIL.md` §A/§B.** Sub-reads (obsolescence / useful-life; returns-case / commoditization), the disconfirming set, and the inherited cross-agent context live there.

---

## LIVE CHANNEL READS (current dated read per channel — one each, and an empty one is a gap)

*The 8/27 audit found this section had accreted into a historical log while its own heading asserted freshness. It is now **current reads only**; the historical bodies are `CHANNEL_DETAIL.md` §B, verbatim.*

- **S1** — Mag-7 **33.5528%**, breadth **+3.70pp** (94.1 pctile) · **as-of 2026-09-01 holdings, read 2026-09-02** · `tools/mag7.py`, SSGA SPY daily holdings (issuer-primary). **BAND: YELLOW (tripped this session).** 63d sector decomposition: index **+0.55pp** while the AI-hardware layer **subtracted −1.22pp** and REST added **+2.80pp** — the rotation-out-of-AI-hardware read from 8/27 continues and deepened.
- **S2** — DDR5 **$53.93 (−0.12%)** / DDR4 **$91.05 (0.00%)** · **as-of 2026-08-27 Asia close** · TrendForce via `tools/semi_watch.py`. **STALE BY 6 DAYS AND THAT IS ON THE RECORD, NOT PAPERED OVER:** the 8/27 post-close and 8/28 Friday readings were **missed while the desk was dark**. ⚠️ **I deliberately did NOT take an off-cadence reading tonight** — the re-arm rule counts *"3+ consecutive readings"*, so whoever chooses the run times chooses the readings [L-21]. Next pre-committed reading **Fri 2026-09-04**.
- **S3** — **~55 GW nameplate / ~32 GW firm** · **as-of 2026-08-13 seam close** (VULCAN sizes MW, WATT prices the grid). Water constraint added 8/27 (AEOLUS), unpriced by this desk.
- **S4** — TSMC **cumulative Jan-Jul 2026 YoY +37.0%**, band **no-stress** · **as-of the July print, filed ~2026-08-10** · SEC 6-K primary. **Next 6-K ~2026-09-10 (August).**
- **S5** — CRWV DDTL **SOFR+550** · **as-of 2026-08-12 10-Q**; NVDA guarantee book **$108.5B** · **as-of the 2026-08-26 10-Q**. No new-issue flex observed since.

---

## EXIT / INVALIDATION (standing-rule-vs-state triad)

> **The THESIS-kill and CHANNEL-kill conditions live in `workbook/EXIT_PROTOCOL.md`** (authored 8/13, discharging the L3 requirement). This table is the **firing STATE**; that file is what kills the thesis. Neither restates the other.
>
> **🔴 THESIS-KILL: 1 of 3 legs currently satisfied** — leg 3, *"memory stays healthy,"* is TRUE right now. *(Legs: FY27 aggregate capex guide ≥ +40% YoY · Mag-7 ≤28% held 3+ months · memory stays healthy.)* **Re-read leg by leg 2026-09-02: still 1 of 3.** Leg 2's gap **WIDENED** this session — Mag-7 moved 32.91% → 33.55%, i.e. **further from** the ≤28% kill level, not nearer.
>
> ⚠️ **DATED REWRITE TRIGGER — RE-DATED THIS SESSION.** It fires on the FIRST of {MU FQ4 · 2026-09-30 · 2026-11-15}. **MU FQ4 is now CONFIRMED 2026-09-30**, so the first two legs COINCIDE and the trigger date is **2026-09-30**. *(It had been ~9/22 on my own erroneous derivation — see the correction below. A "whichever is FIRST" trigger inherits every leg's date.)*

| Channel | Standing rule | Current state @ level | FIRED? |
|---|---|---|---|
| S1 | Mag-7 **≥40%** weight AND breadth collapse (RSP−SPY 63d **≤ −7.5pp**), OR hyperscaler capex **cut** YoY | Mag-7 **33.5528%** [holdings 9/1] · breadth **+3.70pp** (94.1 pctile) · capex guides RAISED, not cut | **NOT FIRED** — level in YELLOW, conjunction far from met |
| S1 — LEADING INDICATOR *(7/22, KB-034)* | lease pauses + equipment-order cancellations soften BEFORE headline guide cuts | MSFT walked ~2GW leases + equipment cancellations; **stays ARMED** | ARMED, not fired |
| S2 | DRAM/NAND contract **−25% QoQ sustained** | Opposite sign and the margin re-widened: NVDA supply+capacity commitments **$119B → $279B** in one quarter | **NOT FIRED — moved FURTHER from firing** |
| S2 — LEADING INDICATOR | *(armed 8/3 · DISARMED 8/13 · disarm UPHELD 8/21 on a better reason · RE-GRADED EARLY 8/24 against the pre-specified rule — still DISARMED)* | **DISARMED.** Pre-specified re-arm rule grades **2026-09-30** on the rolling-1mo `spread_aicompute_minus_memory_pp` basis | DISARMED |
| S3 | datacenter compute→MW demand outstrips grid (with WATT) | **Seam CLOSED 8/13 — adopt verbatim, never net or average:** ~55 GW nameplate / ~32 GW firm | NOT FIRED |
| S4 | equipment ban / fab-level cutoff OR Taiwan kinetic | US eased (H200-China); Taiwan tightening; **TSMC cum YoY +37.0%, no stress.** ⚠️ **A prepared-but-unpublished BIS package on CXMT/SMIC-sub/YMTC is the live binary** [ZHAO 9/2] | NOT FIRED |
| **S5** *(core since 8/3)* | new issue flexes **+150bp or PULLED**, OR a **2nd jurisdiction** writes an IG threshold into a utility tariff, OR a developer **fails to post** mandated collateral | **DDTL 5.5 cleared at SOFR+550** — a ladder, not a flex-vs-talk print; **1 jurisdiction** (Wisconsin PSC, below-A- collateral rule); no failure to post | NOT FIRED |
| **S1 sub-read** (obsolescence) | ≥2 of 4 change useful-life → promote to channel **OR** MSFT shortening alone (override) | **0 of 4, ALL SEC-primary-verified.** ⚠️ **Was NOT lane-armed** — PROME's `edgar_8k` lane is `type=8-K` only and classifies by item code without reading exhibits. **Partly closed 8/27 by `tools/edgar_watch.py`**, which sweeps 10-K/10-Q too | NOT FIRED |
| **S1 sub-read** (returns-case / commoditization) | hyperscaler stock FALLS on a capex RAISE in ≥2 of the cluster prints, OR mgmt cites inference-price / open-weight / ROI pressure | GOOGL −5% AH on a RAISE (7/22); the pattern did not repeat across the cluster | NOT FIRED |

**Fired-count: 0 of 5 channels** (all five carry VULCAN-owned live reads; none at trigger). **Leading-indicator count: 1 of 2 armed** — S1's lease/order-pullback layer stays ARMED; S2's stays DISARMED.

**🔄 LIVE BIDIRECTIONAL FLIP — 🔴 RESOLVER DATE CORRECTED 2026-09-02.**
**Next resolver: MU FQ4 FY26 — CONFIRMED Wednesday 2026-09-30, 2:30 p.m. Mountain (16:30 ET), issuer press release dated 2026-08-26.** ~~*was "~2026-09-29" here and "~9/22" in OPEN — this file disagreed with itself for six days, and both figures were wrong*~~.
**Test: does the LTA/presold ceiling show up in Micron's gross margin?**
- **Confirms the bearish read** → GM expansion **stalls** (≤84.6% GAAP) or FQ1 guided below FQ4 on the same basis ⇒ the ceiling is real; the maker does not capture the rent.
- **Falsifies it** → GM expands **≥+2.0pp (≥86.6%)** *and* FQ1 guided at-or-above ⇒ "presold" is a **moat**, not a ceiling; **retract KB-055's framing and correct WALTER, CARL and HENRY**, all of whom got the ceiling version.
- Governed by **`VULCAN-12`'s registered text** (NO-VERDICT band + GAAP-vs-non-GAAP basis discipline live there). ⚠️ **Never compare a non-GAAP guide to a GAAP actual.**
- 🔴 **GRADEABILITY WARNING, and it is the opposite of what I told myself on 8/27:** VULCAN-02, -11, -12 and -14 all resolve **2026-09-30**, and MU's results now land **after the close on that same day.** Real headroom is **~0 hours, not the "~6-13 days" my 8/27 re-derivation claimed.** Any grade needing the FQ4 print is a **2026-10-01** action at the earliest. Registered in `docket/CATALYSTS.tsv`.

---

## OPEN ON VULCAN (next session)

**0-2026-09-02. THE BOARD.** **MU FQ4 — CONFIRMED 2026-09-30 16:30 ET** (resolves VULCAN-02/-11/-12 inputs; all four 9/30 rows grade **10/01 at the earliest**) · **TSMC August 6-K ~2026-09-10** (run `tools/tsmc_watch.py`; cite the CUMULATIVE) · **ORCL Q1 FY27 print + 10-Q, window opens 2026-09-08, typical ~9/11** (the $3.3B lessor guarantee: refinanced / extended / paid?) · **ORCL $3.3B lessor guarantee matures Sept-2026** · **S2 re-arm rule grades 2026-09-30** · **self-grade CHECKS 1-3 due 2026-09-11** · **PJM IRAS at FERC ~2026-10-12** (WATT owns the grade) · VULCAN-08 + VULCAN-10 (2027-02-15). **Kill-rail rewrite trigger: 2026-09-30.**

**0a-2026-09-02. WHAT THIS SESSION PUT ON THE NEXT ONE.**
1. **Fri 2026-09-04 — `tools/semi_watch.py` post-close.** Pre-committed cadence; two readings already missed. **Run it regardless of what the tape is doing.**
2. **The 9/30 stack is now a 10/01 stack.** Do not grade VULCAN-02/-11/-12/-14 on 9/30 evening assuming the MU print is in hand unless it actually is.
3. **The GPU-rental / compute-spot instrument** — ownership with PROME. 🔴 **SPEC AMENDED 2026-09-03 BEFORE PROME RULED: WATT inverted the TIER and it inverts the sign** — H100 **1-year contract +40%** ($1.70 Oct-25 → $2.35 Mar-26) while **on-demand medians were flat-to-down**. **But the fix is NOT the contract tier** (DEWEY's base rate measured contracted/backlog measures as leading in **zero** of 3 episodes): **register BOTH tiers AND THE SPREAD, and publish the PANEL at every reading.** A flat lead against a +40% lag is either a genuine leading divergence or a broken panel, and **only the spread-plus-panel distinguishes them** (hyperscaler H100 medians **$6.26-9.34** vs marketplace **$1.95-2.58** — 3-6× for the same silicon). 🔑 **WATT reached my pre-declared composition-weighting blocker from the DATA side while I reached it from the DESIGN side.** ⚠️ **Do not grade either tier alone; no threshold on the level until the panel is stable across ≥3 readings.** 🔴 **2026-10-05: CME + Silicon Data list cash-settled Compute Futures on NYMEX** — an exchange-settled index is composition-controlled by construction, so that is the date the panel problem becomes tractable. Registered in `docket/CATALYSTS.tsv`; **supersedes KB-031's 7/22 'NO regulated futures' binary**, which nothing here was watching for the flip of.
4. **DAEDALUS's three boot-wiring flags, encode-or-decline:** ① boot step 8 (channel liveness) has **no leg in `boot.py`** — it is silent by construction; ② `THESIS.md` is in **no boot loop**; ③ `docket/CATALYSTS.tsv` is **excluded from leg-1 staleness**. **Declined-for-now on ② and ③ with reasons; ① is accepted and queued.**
5. **`CLAUDE.md` is 59,354 B — over the 54,250 B physical cap.** Not bound by READ-CAP (auto-loaded, not a `Read`) but it costs context every boot. **Watch, don't rotate.**
6. 🟠 **`workbook/PREDICTIONS.tsv` is 49,252 B = 91% of cap — over the 60% BUDGET, under the CAP. DEFERRED, and this is the "why not" DAEDALUS's packet asks for in writing.**
   - **It is READABLE. The defect class the read cap exists to stop — a boot `Read` silently returning a truncated file — does not apply here.** It is a headroom warning, not a breach.
   - **The remedy is already my own declared design** (`CLAUDE.md` §PREDICTIONS: *"resolved rows → archive with post-mortems"*) and has simply never been executed: **8 of 16 rows are resolved.** Archiving them roughly halves the file.
   - 🔴 **DEFERRED FOR A STATED REASON, NOT FORGOTTEN: an archival split is one of the four operations PROME's session process controls require a PRE-EDIT COLD READ for**, and this session has already executed one large split. Doing a second, unreviewed, at the end of a long session is the exact shape of `[[finding_a_correction_pass_is_unreviewed_work]]`.
   - ⚠️ **The specific risk to check in that cold read:** STATUS's triad cites **VULCAN-07**'s gate as a live sub-read standing rule (*"≥2 of 4 → promote"*, state *0 of 4*) while the row itself is resolved. **A resolved row can still be carrying a live standing rule** — `[[finding_live_claim_in_a_closed_container_is_invisible]]`. **Archive by row, never by status.**

**0b-2026-09-02. WHAT I OWE, AND TO WHOM.**
✅ *Delivered this session:* **VULCAN-16 graded** · **the MU date correction to VIOLET and PROME** (my number was wrong, VIOLET's was closer) · **the GPU-instrument ownership answer to PROME (WATT cc)** · **DEWEY's REQ-001 accepted with the semis half contested on one point** · **AEOLUS's water ask answered (declined an instrument, with the reason)** · **NEXUS amendment-9 revert executed**.
❌ *Still owed, named as owed:* **the compute-spot-index baseline** (deferred since 7/22 — DEWEY's base-rate finding now makes it the single highest-value open instrument on this desk, but ownership is PROME's call) · **the hyperscaler long-dated-issuance check** (KB-096, one query) · **the QQQ variant of the sector-within-index leg** (blocker NAMED: Invesco 406s its whole domain — PUBLIC-BUT-UNFETCHED, not unavailable).
📌 *Not mine, do not chase:* company-level DRAM capacity modelling is a **PROME coverage gap**, not a VULCAN mandate (8/21 scope fence). ZHAO keeps WFE bindingness and has now answered it.

> 📖 **The superseded 8/13 and 8/21 OPEN blocks, verbatim → `CHANNEL_DETAIL.md` §D.**

---

## BOTTOM LINE

**As of 2026-09-02.** AI-capex is still **accelerating, not rolling** — hyperscaler guides were raised across the 7/31 cluster, NVDA guided Q3 to **$108.0B**, and its supply-and-capacity commitments went **$119B → $279B in one quarter**. So S1 stays **NOT-FIRED** and all five channels hold at **3 (composite 15/25, eighth session)**. **The one thing that moved is a BAND, not a score: Mag-7 concentration crossed the 33% yellow line to 33.5528% while breadth narrowed 5.00 → 3.70pp** — the second consecutive reading with both legs of the red conjunction moving the same adverse way. ⚠️ **n=2 is not "sustained" by this desk's own rule and I am not calling it that.**

**The single most important channel reading is S2, and it is a physical one:** DRAM spot printed its **first decline in the retained series** on 8/27 (DDR5 −0.12%), which **graded VULCAN-16 REFUTED on its escape clause** — while being far too small to move the −25% contract rule, which sits **further** from firing than it did a month ago. **The de-risking call survived on the equity leg and the "not memory-specific" ground died on the physical one.** ZHAO's CXMT answer closes the other half: the supply threat is the **Nanya shape, not the China-is-adding-supply-now shape** — volume bits land 2H2027-2028, outside the window — so **S2's shortage premise survives inside 9/30, on a wide error bar rather than a clean finding.**

**What's next:** the board is now genuinely dated. **TSMC August ~9/10**, **ORCL from 9/8**, and then a **single hard 9/30 node** where MU FQ4 prints after the close and four predictions plus the kill-rail rewrite trigger all come due. **The honest headline of this session is a correction, not a finding:** my own 8/27 "better derivation" moved MU's date **eight days the wrong way**, away from a date the issuer had already announced the day before, and it did so while telling me the change had moved in my favour.

> ⚠️ **What is NOT changing, said explicitly because a held score reads as a quiet one:** no score moved, no threshold was set or moved, no band was retuned, no capital path was proposed. The S1 yellow trip is the **registered instrument reporting its own registered level** — not a judgment.
