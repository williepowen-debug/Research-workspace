# REGINALD STATUS
**🟢 10/10 SAT (Will-launched): CAUGHT UP ON DATA; three overdue process items DONE; no score, threshold or trade moved.**
- **Settled grades:** 10/9 closes graded (WAL $74.27, exit 0-of-3, row 28; FLG 3rd close below RED).
- **Predictions:** REG-03/06/07 instruments named. ⚠️ REG-07's level reading was true at birth, so it grades on the CHANGE from 0.62%; **Will may VOID it before SSB prints 10/21**.
- **DAEDALUS fixes:** F#4 wording fixes + wiring ⑰ done. The `V1V3-ACCELERATE` token rename is deferred because WALTER reads it.
- **Stale tables:** VX 27 rows STALE · FLOW frozen · two June baselines FROZEN-VINTAGE · KB +3.
- **Large-bank desk:** proposal packeted to DAEDALUS (Will-directed).
- **HBAN puts:** Will's word on WQ-302 committed verbatim in POSITIONS (`cb236344f`).
- **Owed at next boot (Will):** ① the 9/7 DAEDALUS packet decision ② the FHLB Atlanta / SF 10-Qs ③ five July threads.
**🟠 10/9 FRI PM — MONITOR REPAIR + Q3 EARNINGS READ PLAN (Will-directed); STRESS STILL CONCENTRATED ON 6/30 EVIDENCE; NO SCORE, THRESHOLD OR TRADE MOVED.**
- **Repair (`8255c2d13`):**
  - OZK's 8-K and insider checks now use the FDIC (they had queried the SEC, where OZK hasn't filed since 2017).
  - **VLY was keyed to Old Republic's SEC ID (74260 → 714310).**
  - FLG / AMTB / CFG / CUBI added. A failed, unparseable or uncovered bank can no longer print an all-clear.
  - The countdown reads the CALENDAR earnings table; unsettled and NaN daily bars are excluded from settled grades.
- **Plan:** `reports/2026-10-09_Q3_earnings_read_plan.md`.
  - Individual-bank deterioration is not cross-bank spread. Only L180 or the FL-rail aggregate can show spread.
  - L180 is graded on the ORIGINAL total-CRE rate. Multifamily is a separate sub-read.
  - Missing banks → UNKNOWN wherever they could flip a breadth verdict.
  - **11/07 = planned Call Report retrieval, completeness checked then.**
- **Baseline (Call Report):**
  - Total-CRE bad-loan rate 2.46% → **2.23%** [6/30/25 → 6/30/26].
  - Multifamily 3.88% → **3.58%**, but **up from 3.23% last quarter**, all at FLG / EGBN / CFG. That is individual, not spread.
  - L180 dry run Q1 → Q2: *c* = 1 (WAL foreclosed property +2.3%).
- **Tape:** 10/9 vendor quotes (settled bars not posted) WAL 74.27 · KRE 69.01 · FLG 11.32 · OZK 44.41, while SPY rose +0.60%.
- **Claims:** 197K [w/e 10/3]; w/e 9/26 revised to 199K.
*Prior headlines (10/9 AM · 10/7 WED) and the archive-pointer chain for 9/29 → 8/10 → `archive/STATUS_rotation_2026-10-09.md` BLOCK T15, crc32 `4546cd82` (read-cap rotation 10/9 PM; recompute before trusting).*
**Last Updated:** **2026-10-10 Sat ~12:4x ET (Will-launched, continuation; closeout)**: 10/9 settled grade · REG-03/06/07 instruments · F#4 + wiring ⑰ · stale tables · large-bank desk packet · WQ-302 verbatim. Prior: **2026-10-09 Fri ~22:xx ET (Will-launched evening session, Opus 5.5)**: boot · WALTER lane 2 → 0 · bounded monitor repair `8255c2d13` · Q3 read plan + Will's clarifications · FL frame A3 · CALENDAR earnings table · read-cap rotation T14–T19. *Stamp chain (10/9 AM and earlier) → BLOCK T16, crc32 `3ba61974`.*

> **Thesis state:** STATUS is thesis-canonical (THESIS retired 8/13). Older carry blocks → `archive/STATUS_rotation_2026-09-02.md` BLOCK N and `archive/STATUS_rotation_2026-09-24b.md`.

---

## THESIS: The Convergence

> *8/20 reconciliation note (the retired eight-channel framing sat here 7 days after THESIS was retired for it) → BLOCK T12, crc32 `ff770d7b`.*
> **LIVE CLAIM: severity is CONCENTRATED, not tier-wide** — of 14 primary-sourced filers, **3 elevated, 8 score ≤2** (`BANK_EXPOSURE_MATRIX.md` v2.0). Concordant with the FL card (4-of-4 REVERT, 8/10) and the Q1 cohort NCO decomposition (Hyp A, 6/8). ⚠️ **The concentration is at DIFFERENT NAMES than assumed — FLG/EGBN/AMTB on instruments; WAL and OZK mid-pack.** ★ **9/26 CRE-specific cut (Will-asked): the three most worth investigating for CRE are FLG · EGBN · OZK. AMTB's score is mostly NON-CRE credit (CRE = 30% of nonaccruals on the Call Report, 5.8% on its own basis), and OZK's $288M of foreclosed CRE is invisible to the matrix credit leg.** → `reports/2026-09-26_CRE_vulnerability_top3.md`. Matrix scores unchanged until the 11/07 re-score. ⚠️ **Only 2 of the 8 channels below are instrumented here; the rest are owner-held** (map → matrix §6).

**Eight channels terminate at regional banks — 2 instrumented here, 6 owner-held (see §6 of the matrix). Channel-level state below is CONSUMED from owners, not re-derived.**

| Channel | Mechanism | Status |
|---------|-----------|--------|
| CRE | 70% of CRE at regionals, 70-94% loss severity confirmed. **Apr 2026: dual-stress now — Office plateau 11.69% +141bps YoY + Multifamily +56bps to 7.71% (NEW vector); GSE MF (HOMER, issuer primary, refreshed 9/26): Freddie MF DQ **0.64% [Aug]**, fourth straight rise off a 0.42% Feb trough, above HOMER's >0.50% RED · Fannie MF SDQ **0.61% [Jul]**, rising off 0.58% [May] (its fall from 0.78% was a loan MODIFICATION, not a cure; pair GSE DQ with the filer's provision direction) · Trepp CMBS MF DQ **7.69% [Aug]**, flat. The GSE-improving/CMBS-deteriorating asymmetry is GONE; compare directions, not levels (0.6% vs 7.7%).** | 🔴 |
| Hidden CRE | Cohort MI3 re-run shipped 8/13 (56 primary bank-quarters) → `reports/2026-08-13_MI3_cohort_rerun.md` + `workbook/MI3_COHORT.tsv`. v1a basis ruled 4+9.a (8/28); **rank citations DO-NOT-CITE until the 11/07 Q3 re-run.** Full cell → `archive/STATUS_rotation_2026-09-24b.md`. | 🟠 |
| SSFA / NDFI | $4.2T industry-wide NDFI (+35% YoY); hidden CRE Layer 2 | 🔴🔴 |
| Private Credit | Ares gated (5% cap, 11.6% requests), Apollo 45¢/$1, bad PIK 6.4%, MS projects 8% default | 🔴🔴 CRITICAL |
| MFS/Fraud | £2B double-pledging — Barclays/Jefferies/Apollo. Cantor $270M ring. | 🔴 |
| CMBS Maturity | $875B total CRE maturing 2026 (MBA *2025 CRE Survey of Loan Maturity Volumes*, released 2026-02-09 — PRIMARY-CITED by HOMER 9/2 at MBA's own text on the newslink.mba.org mirror; 2027 $652B; 2026 is −9% vs $957B in 2025; depositories $396B = the largest lender bucket). $76.6B hard maturity + $400B wall pushed to 2026. No extensions. | 🔴🔴 |
| Federal Layoffs | DOGE 307K+ confirmed. DC corridor stress ACTIVE. | 🔴 |
| Stagflation Trap | Rate leg at a cycle-high LEVEL; energy leg high. **Live levels → §THRESHOLD STATUS 10Y / 30Y / Brent rows (one source of truth).** The 9/25 narrative read (hike, real-yield-led move, Brent named contracts, KRE drift) → BLOCK T18, crc32 `d372ca3b`. ⛔ HAWK/BRENT/FALCON own oil, BOND owns the curve. | 🔴 |

---

## SIGNAL DASHBOARD → **`STATUS_DASHBOARD.md`** (cold, on-demand — NOT a boot read)

*42 channel rows split out 9/02 (crc `1585e8e9`); live levels stay in §THRESHOLD STATUS. Note → BLOCK T13, crc32 `eb9e9c85`.* Re-check size at any append.

## RESEARCH — POSITION NAMES (pointers to canonical state)

⚠️ **OZK and WAL are PEER AGENTS: read `../OZK/STATUS.md` / `../WAL/STATUS.md`. Their version, EV and PT are never mirrored here.** Full note → `archive/STATUS_rotation_2026-09-24c.md`.
*(The Apr-30/May-vintage OZK and 7/25-vintage WAL blocks that sat here were REMOVED 2026-08-20 — both were flagged stale at the 7/17 audit and both duplicate a peer's canonical surface. Git history retains them.)*

---

## CONVERGENCE MATRIX — Targets & Positions

> **Matrix detail (method notes, runway/reserve legs, per-bank narrative rows) → `STATUS_MATRIX.md` — COLD, on-demand, NOT a boot read; split verbatim 2026-09-24, crc-stamped.** Scores below are the live line; ⚠️ a `0` means clean on the scored channels only, not a clean bill of health. Method + full table → `BANK_EXPOSURE_MATRIX.md`.
> **🔴 FLG 6** *(was LAST)* · **🟠 EGBN 5** · **🟠 AMTB 5** *(absent from v1 entirely)* · VLY 3 · **OZK/WAL/SSB/BKU/SBCF 2** *(WAL was 1st=)* · ZION/MTB/CUBI 1 · **CFG/HBAN 0** *(CFG was 3rd)*.
> 🔴 **FLG price ladder `VX-REG-6.03` RED since 10/7** (band 3 $11.39 broken at **$11.30 [10/7 close]**, −20.6% vs FROZEN $14.24; band 1 $12.82 broke 9/16, band 2 $12.10 broke 9/28). **Packets PROME + FLG sent 10/7 (`018af9846`)** per the 9/24 registration; the ladder is exhausted (no band beyond RED). Detector: `scripts/vx_ladder_check.py` (exit-code defect FIXED `b6544d45d` 9/24 — DAEDALUS Prose-Remedy #1, verified 10/9). ✅ **Intraday-bar defect FIXED 10/9 (`8255c2d13`):** today's (ET) bar and any NaN bar are now always excluded via `scripts/settled_bars.py`. A clock filter alone would have failed, because the 10/9 bar still read NaN at 20:3x ET. Settled count = 2 closes below RED through 10/8; 10/9 NOT GRADED until settled. Matrix score unchanged (price is not an input).



*Cohort Signal (Hyp A, 6/8) + Life-Sci sector signal: graded and canonical elsewhere → `archive/STATUS_rotation_2026-09-14.md` BLOCKS P+Q; stub → BLOCK T11, crc32 `18724a40`.*

---

## KEY CATALYSTS

*Dates are OWNED by `CALENDAR.md` — **earnings dates in its Q3-2026 BANK EARNINGS DATES table** (CUBI + FLG NOT ANNOUNCED at 10/9 21:2x ET). Read plan → `reports/2026-10-09_Q3_earnings_read_plan.md`. The four-row mirror that sat here (capital-rules final rule TBD · IQHQ Aug · OZK sub-notes Oct 1 · Affinius Oct) → BLOCK T8, crc32 `6e2cf1ef`. Next (10/7, issuer-announced): CFG Fri 10/16 · WAL Mon 10/19 AMC · OZK Tue 10/20 AMC · EGBN/SSB Wed 10/21 AMC, BKU 10/21 BMO · VLY 10/22 BMO, AMTB 10/22 AMC · SBCF 10/27 AMC · FLG/CUBI TBA · Nano P&A NOT posted 10/9 (bid summary posted 10/8) → re-check **Tue 10/13** · JWT 11/05 · MI3 run 11/07.*

---

## CROSS-AGENT TRIGGERS

> ⛔ **THIS TABLE CARRIES THE ROUTING, NEVER THE LEVEL — every level is canonical in §THRESHOLD STATUS above. Duplicating a level IS the drift vector; point at the owner, never restate.** *(9/02 de-dup rationale + worked example → BLOCK T6, crc32 `1b7dacdf`; the example is quoted live in `NEXUS_BRIEF.md`.)* `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]`

| Condition | Level | Routing on fire |
|---|---|---|
| Claims >300K | → §THRESHOLD STATUS | LABOR → all ORANGE banks escalate to RED |
| HY OAS >320bps (`REG-T-03`) | → §THRESHOLD STATUS | CARL → credit transmission confirmed. ⚠️ **A wide HY print is NOT self-evidently bank transmission** — run the bank-credit cross-check first (`reports/2026-07-30_bank-side-HY-attribution.md`; the 7/27-29 sustain was `BANK-ABSENT`). |
| HY OAS >350 (`REG-T-04`) | → §THRESHOLD STATUS | LIQUID + Will → issuance freeze |
| ⚠️ HY OAS <260 | → §THRESHOLD STATUS | **REVIEW trigger, NOT auto-exit** (re-anchored 6/19, Will-confirmed). Anchor-drift: the thesis narrowed to WAL-idiosyncratic + CRE; broad HY does not print it. |
| **CCC/HY >3.6× (3 consec)** — `VX-REG-18.04`, **MINE** (PROME 8/28) | → §THRESHOLD STATUS | LIQUID/BROCK → tail-decoupling. ⛔ **The vector's own rule decides escalation, not the level: HY-tightening-led = denominator artifact = NO escalate; only a CCC-LED re-cross escalates.** Escalation STOOD DOWN 8/13 (Will). Full definition → `research/CCC_HY_TRIPWIRE_2026-06-25.md`. |
| CLO AAA >165bps · iTraxx Sr Fin >100bps | **[STALE — no vintage; do not cite]** | LIQUID → BDC transmission (LIQUID-owned, ask don't re-derive) · HANS → EU→US contagion (a DATA-SOURCE gap, not an instrument-identification one). Rows → BLOCK T10, crc32 `9867efbc`. |
| SOFR−IORB >+15bps (`REG-T-08`) | → §THRESHOLD STATUS | LIQUID → FHLB spike. See §THRESHOLD STATUS §Funding plumbing for the structural read (the repo-to-IORB cushion has been consumed; it changes the CONVERSION RATE, not any level). |

## FRAMEWORKS (detail in workbook/)

*Pointer-only, collapsed to one line 2026-08-23 to hold the 250-line cap — zero data lost, these were four file paths:* **Dual Failure Channels (A=CRE, B=PC/NDFI)** → `workbook/CHANNELS.md` · **CRE 3-Layer Architecture** → `workbook/CRE_ARCHITECTURE.md` · **8 Convergence Channels** → `workbook/CONVERGENCE.md` ⚠️ *(eight-channel framing is RETIRED as a thesis claim — see §THESIS; the file is history)* · **NDFI/Whalen Research** → `workbook/NDFI_RESEARCH.md`.

---

## SUB-AGENTS & PEER COORDINATION

*Peer snapshot table (CREED/BROCK/CORAL/BELT/RENO rows, Apr–Jul vintages) → BLOCK T7, crc32 `8e07393b`. **Read each peer's own `STATUS.md`** (`../CREED/`, `../BROCK/`, `../CORAL/`, `../OZK/`, `../WAL/`, `../FLG/`). Two fences travel with any CREED cite: ① the `$875B` 2026 maturity wall is MINE (MBA, ALL-CRE), not CREED's CMBS-only figure (~9× apart); ② CREED's DQ/SS are RATES, WALTER's 'distress −$3.49B' is a BALANCE.*

---

## PREDICTIONS

> **Single source of truth: `workbook/PREDICTIONS.tsv`** (20 rows, REG-01…REG-26; REG-16/21/22/23 → OZK 4/24; REG-24/25 → WAL 7/25 as WAL-01/02, OPEN to the Q3 10-Q; REG-26 RESOLVED-DISCONFIRMED 7/21). `REG-07` re-mark and `REG-03` re-spec are OWED at the Q3 print (MEMORY 6/6d). *Prior text → BLOCK T9, crc32 `eb89e2c3`.*

---

## EXIT RULES

> **Anchor-drift rule (Will-confirmed 6/19, in force):** HY <260 is a **REVIEW trigger, not an auto-exit**; the real exit is re-anchored to the CRE channel (CMBS-DQ, bank CRE-DQ, WAL NCO). Full note → `archive/STATUS_rotation_2026-09-24c.md`.

- **Exit 50%:** Claims <240K sustained + CBRE >-5%
- **~~Exit 100%: HY OAS <260bps~~ → REVIEW trigger** (broad-credit stand-down; re-examine WAL-specific + CRE channel before any exit — do NOT auto-exit on broad HY)
- **Exit 100% (still auto):** BTFP 2.0 announced (genuine systemic backstop = thesis broken)
- **NEW — CRE-channel exit anchors (the thesis's actual confirmation lane):** WAL Q2 NCO ex-fraud comes in <25bps AND no Office classified migration (REG-24/25 both fail) → bear thesis disconfirmed at source; OR Office CMBS-DQ flows reverse (new-delinquency MoM negative 2 prints running) + bank CRE-DQ tier-creep reverses.

---

## ⚠️ THRESHOLD STATUS (**10/9 PM refresh: claims w/e 10/3 and DGS10/DGS30 10/8 (FRED API); VIX/^TNX/Brent 10/9 vendor reads; WAL/KRE 10/9 = vendor quotes, NOT settled. The 10/9 AM refresh note (settled 10/8 closes; FRED 10/8 via ALFRED; SOFR/discount window via WALTER) and older vintages → BLOCK T19, crc32 `cebafa60`.** Rows not named keep their stated vintage.)

> *Refreshed 8/20 after this block sat at a **7/24 vintage for 27 days** — the exact defect LESSON 15 names ("the surface you cite from memory is the one that rots"). Every row below is re-pulled, not carried.*

| Metric | Threshold | Current | Note |
|--------|-----------|---------|------|
| **FHLB advances** | **>$700B, sustain 3 qtrs** | **$810.7B** [6/30/26, FHLB Office of Finance] | 🟠 **`REG-T-06` LEG 2 OF 3, does not fire.** Q4-25 $677B (reset) · Q1-26 $734B · Q2-26 $810.7B. **A Q3 print >700 FIRES (~late Oct/early Nov).** Pittsburgh +111% = PNC alone (n=1, benign purpose); not a trip of BOND's ungradeable `VX-BND-18` leg. Full cell → `archive/STATUS_rotation_2026-09-24c.md`. |
| **WAL** | **<$78** | **$75.50** [**Thu 10/8 CLOSE**, +1.55%; two routes]; **10/9 $74.27 CLOSE, settled, two routes agree (graded 10/10: row 28, 0-of-3, 9.32% short)** | 🔴 **`REG-T-02` = `FIRED` (cycle 2, since 9/1). Exit run `0-of-3` — COUNT FROM `registry/REG_T02_EXIT_LOG.tsv` (27 rows through 10/8), never from here.** Exit = `WAL ≥ 81.90 ×3 CONSECUTIVE closes`; 10/8 is $6.40 / 7.81% short. Closes 9/30–10/6: 75.10 · 75.70 · 76.38 · 76.02 · 76.09 — all SUPPRESSED RE-ENTRIES. **Q3 print LOCKED Mon 10/19 AMC** (call Tue 10/20 12:00 ET). Guards the RH `Dec-18 $70P` (ROLL70) only — not the NEW Fidelity `Dec-18 $65P ×4`. |
| KRE | <$60 | **$69.59** [**Thu 10/8 CLOSE**]; **10/9 $69.01 CLOSE** (settled, two routes agree, 10/10); 10/7 $68.89 (closing low of the selloff) | 🟡 **`REG-T-01` = `UN-FIRED`**, $8.89 / 12.9% above the line. Path 69.83 [9/29] · 69.44 · 69.95 · 70.78 · 70.39 · 70.07 · **68.89** = new closing low of this selloff in my 9/14→10/7 series (−7.0% from 74.11 [9/14]). The Sep-30 $60P ×2 was SOLD 9/30 and rolled to Dec-31 $65P ×2 (Will). `TRY-COND-KREADD` (TERRY) NOT armed on my legs. |
| HY OAS | >320 (`REG-T-03`) · >350 (`REG-T-04`) | **315bps** [FRED BAMLH0A0HYM2, **10/8**; ALFRED vintage 10/9, own pull 10:28 ET] | 🟡 **`REG-T-03` GRADED 0-of-3 at the 10/8 cell** (my letter: >320 on 3 consecutive closes): **324 [10/1] = 1 of 3**, **310 [10/2] RESET**, 312 [10/5], 303 [10/6], **309 [10/7] 0**, **315 [10/8] 0** (both ≤320, no run). NOT FIRED. 5bp under 320 (1.6%); RED's FT-02 graded separately. Prior: 17bp under 320 at 10/6, 43bp above the <260 REVIEW line. LIQUID: one tagged print, funding not confirming (SRF $0, SOFR−IORB −3bp [10/1]); X1 CLOSED (LIQUID's). ⚠️ Anchor-drift caveat stands [SIG-723-002]; bank-credit cross-check before reading any HY level as transmission. |
| **CCC/HY ratio** | >3.6× (3 consec) | **3.975×** [CCC **1,252** / HY 315, **10/8**]; 3.977× [1,229/309, 10/7] | 🔴 **HARD-FIRE CONTINUES. 10/7–10/8: CCC +38bp to 1,252 = NEW FRED-window high, HY +12, ratio flat-to-down — both legs widening, no re-cross ⇒ no escalation by the vector's rule (LIQUID/RED own the tail read). B 308 [10/7] · 315 [10/8]; BB 189 · 194.** Prior 10/6 read: ratio 4.007× — and the ratio's 10/2→10/6 RISE is HY-TIGHTENING-LED (HY 324 → 303 while CCC held 1,202–1,215) = the denominator form, so NO escalation by the vector's own rule.** CCC **1,215 [10/1] = FRED-window high**. B 302 [10/6] (316 · 316 · **329 [10/1]** · 312 · 314 · 302): held >300 seven prints, never reached ORANGE 330. BB 185 (peak 204 [10/1]). Re-arm ESC escalated 9/26; not repeated (Will 9/26: re-entry is LIQUID's). BROCK 10/2: CCC/BB compressed 6.780 → 6.077, tail not leading. Full rows → `workbook/VX.tsv` `VX-REG-18.04`/`18.05`. |
| Claims | >300K | **197K** [FRED ICSA w/e **10/3**, API pull 10/9 20:4x ET; next print Thu 10/15] | 🟢 **103K of buffer.** w/e 9/26 **revised 197 → 199K**. Prior chain 198 [9/12] · 198 [9/19, revised from 197] · 197 [9/26, first print]. Sept payrolls +29K, net revisions −60K, U-3 4.2% (WALTER -20261002-001; LABOR's kill did NOT fire). LABOR owns the read. |
| VIX | n/a | **14.84** [**10/9** vendor read]; 15.08 [10/7] | 🟡 Mid-teens through a cycle-high 10Y, HY over 320 for one print and an FLG RED: **not a fear event.** |
| Brent | n/a | **`BZ=F` $104.43** [10/9 vendor read; contract month not re-checked]; $101.46 [10/7] | 🟠 Not re-read on a named contract. HAWK/BRENT/FALCON own the level and the verdict (BRENT settle-window proxies, HEARTBEAT §1). |
| 10Y UST | n/a | **5.24%** [^TNX **10/9** vendor read]; FRED DGS10 **5.22 [10/8]**, 5.28 [10/7] | 🔴 **Cycle high zone, still.** Official 10Y 5.28 [10/2] rose ABOVE its pre-payrolls level after a +29K print; real-yield-led (BOND, HEARTBEAT 10/2). **This is the LEVEL input to my AOCI/NIM/capital channel.** ⛔ BOND owns the curve. |
| **30Y UST** | n/a | **5.60%** [FRED DGS30 **10/8**]; 5.67 [10/7], 5.64 [10/6] | 🔴 Above every September print (5.49 [9/25]); BOND: 30Y real 3.34 = cycle high [10/2 official]. ⛔ BOND owns the series and the high-water claim. |
| **Funding plumbing** | *(`REG-T-08` SOFR−IORB >+15 ×3)* | SOFR−IORB **−3bp** [3.87 − 3.90, **10/8**, WALTER] · RRP **$2.338B** [**10/7**] · **Discount window primary credit $9.965B [Wed 10/7] / $7.701B wk avg** (H.4.1 via WALTER -20261008-049; highest Wednesday since ≥Jan 2024; no registered line; borrowers not named) | 🟢 15bp under `REG-T-08`; quarter-end passed without pressure (−3bp [10/1]). LIQUID owns the structural read. |
| **Financial stress** | *(no registered line)* | **STLFSI4 −0.468** · **NFCI −0.494** [both **10/2**] | 🟡 **STLFSI4 tightened +0.34 in one week (−0.809 [9/25] → −0.468)**, the HY-over-320 week; still on the loose side of zero. NFCI barely moved (−0.510 → −0.494). **Not systemic stress; the direction changed.** |
| **Bank H.8 deposits** | *(no registered line)* | Large **+1.28%** / small **+0.04%** [4wk to 8/05] | 🟠 **Real divergence: large banks gathered $155.3B, small banks $2.5B.** A level fact predating 8/14, not a catalyst. CRE loans **still growing** ($3,111→$3,124B), so no aggregate CRE crunch. |

*(**Macro read of 7/9** — 1,680 B, wholly superseded by §BOTTOM LINE §WHAT CHANGED 8/27 → 9/1 — ROTATED VERBATIM 2026-09-02 → `archive/STATUS_rotation_2026-09-02.md` BLOCK G. Its one still-live claim, the rate LEVEL as the durable bank-transmission leg, is carried in the 10Y/30Y rows above and in §THESIS.)*

---

## BOTTOM LINE

**2026-10-09 (Q3 read plan, Will-asked; `reports/2026-10-09_Q3_earnings_read_plan.md`):**
- **Still CONCENTRATED on 6/30 evidence:** named banks with named mechanisms. Total-CRE bad-loan rate down year on year (2.46 → 2.23%). No cheap-deposit flight at 6/30.
- **Multifamily** fell year on year but rose last quarter at FLG / EGBN / CFG. That is individual, not spread.
- **What would make it spread:** only L180 (≥3 of the five mid-pack banks on the original total-CRE basis) or the FL-rail aggregate. Each reads UNKNOWN where missing banks could flip it.
- **Most consequential open question:** that breadth test, which comes from the Call Reports. Retrieval is planned for 11/07, with completeness checked then; the JWT expires 11/05 (Will).
- **Post-6/30 signals pointing the other way** (discount window $9.965B [10/7], size-led equity selloff, KRE redemptions) name no balance sheet.

*§BOTTOM LINE 2026-10-07 (WQ-318) and 2026-09-29 (attribution) paragraphs, plus the 9/24 rotation pointer → `archive/STATUS_rotation_2026-10-09.md` BLOCK T17, crc32 `6961a43c`. Reports canonical: `reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md` · `reports/2026-09-29_selloff_attribution_and_preprint_observables.md`. Their live claims are carried in the 2026-10-09 entry above.*

**Standing bear ledger → `STATUS_BEAR_LEDGER.md` (COLD, not a boot read).** Prior BOTTOM LINE (9/11, incl. the 9/14 WHAT-CHANGED and watch-list) → `archive/STATUS_rotation_2026-09-24b.md`.

⚠️ **Standing caveat: every instrument this desk owns measures CREDIT or a CLOSED QUARTER.** A non-credit repricing is invisible to it.

## OPEN PROCESS ASKS — dated answers (DAEDALUS 10/8 packets; DONE-WHEN = fixed or answered here)

| Ask | Answer 10/9 | Review by |
|---|---|---|
| Prose-Remedy #1: strike 'exit-code defect still owed' (STATUS, MEMORY) | **DONE 10/9** (fix `b6544d45d` verified at the commit) | — |
| Falsification #4 minor: `REG_T02_EXIT_LOG.tsv` header clock | **DONE 10/9** (header now 10/9) | — |
| Falsification #4 flags: CLAUDE.md:24 eight-channel line · `domain/NDFI_HIDDEN_CRE_HYPOTHESIS.md` banner · DECK_EVIDENCE redirect · WAL <$78 label (CLAUDE.md:280, thresholds.py:25, registry) · LESSONS.md:29 | **DONE 10/10** except the registry TOKEN `V1V3-ACCELERATE`: renaming it is DEFERRED to a coordinated change with WALTER, which reads it; the reason is in `registry/NOTES.md` | registry token: next registry touch |
| Falsification #4 neg-res: instruments for REG-03 / REG-06; **name SSB Q3 line REG-07 grades on** | **DONE 10/10.** REG-03 and REG-07 instruments are in their Notes cells; REG-06 is in `registry/NOTES.md` (the row is Kernel-pinned). ⚠️ REG-07's level reading was already true at birth (SSB NPL/loans 0.62% [12/31/25]), so it grades on the CHANGE; that reading decides the grade (flagged to Will) | — |
| Wiring ⑰: VX rows :9/:23/:37/:39 re-cut; :39 → live SAM surface or CANNOT-FIRE; Medallia one figure with BROCK | **DONE 10/10:** 5.01 / 8.01 / 14.01 RETIRED; 14.03 RETIRED + CANNOT-FIRE (its SAM row does not exist); 17.01 is now a pointer to BROCK `VX-BRK-003` (49.5¢ [6/30/26]) | — |
| PR#6 ask 3 (9/17): disposition the 9/7 as-made packet | **DONE 10/10 PM.** All 20 rows re-derived by text; REG-13 re-formed; the 9/11 REG-07 scoring line corrected to WQ-112(i); REG-10 registered after its outcome, kept scored. Receipt `registry/NOTES.md`; DAEDALUS packeted | — |
| L546 float-tie: `kre_float.py:102`, `si_refresh.py:45` round before compare | DEFERRED to next touch of either file (DAEDALUS: no deadline, LATENT) | next touch |
| WALTER -033 (WQ-399): receipt line in my boot card | **DONE 10/9** (CLAUDE.md step 9c carries the WQ-399 fields) | — |
