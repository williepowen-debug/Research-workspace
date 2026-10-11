# WQ-419 pre-continuation operating snapshot — 2026-10-11

Cold historical preservation; not a current operating instruction. Source: owner closeout 2daea8d59 (README prior 236a091d4).

## STATUS.md

Bytes: 21769 · crc32: c6307121

```markdown
# REGINALD STATUS
**🟠 2026-10-11 SUN (PROME-launched): WQ-414 option B ACCEPTED after independent result read (`1b937462e`).**
- **Bank funding alarm (`REG-T-06`): REVIEW**, with top-four growth contribution and qualified SEC-filer borrower median before escalation. Official run remains **2 of 3 through Q2-2026**; the Q3 debt nowcast never counts. Full procedure → `registry/NOTES.md` §REG-T-06.
- **Authority:** Will's verbatim ruling + bounded launch in `PROME/proposals/2026-10-11_wq414-409-RULED.md`; PROME plan checkpoint P1 consumed (existing panel includes PNC, no new size exclusion). Canonical encode `236a091d4`, delivery `2912cd369`, independently accepted at `1b937462e` (2 reads, zero consequential defects). Exact result → `reports/2026-10-11_WQ414_option-B_result.md`; closeout → `reports/2026-10-11_WQ414_owner-closeout.md`.
- **Boot 10/11:** market figures are dated 10/9 final-for-period, no new session close; FLG RED continues (3 settled closes through 10/9). CFG 10/8 item 5.03 alert = previously documented Series G retirement, routine. No other thresholds, scores or trades changed.
- **Open with Will:** REG-07 VOID before 10/21 (WQ-412) · HBAN sell-or-roll by 10/14 (WQ-302, intent recorded, no fill) · large-bank desk · JWT by 11/05. WQ-414 approval and independent result verification resolved; LIQUID/BOND/WALTER consumption remains unverified.
**Last Updated:** 2026-10-11 Sun, WQ-414 accepted; explicit full-closeout ask received; prior 10/10 header and affected operating text preserved verbatim in `archive/WQ414_operating_snapshot_2026-10-11.md`.

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
| SSFA/NDFI · Private Credit · MFS/Fraud | **Owner-held** (BROCK · HANS · LIQUID); the April cells (🔴🔴 'Ares gated', '£2B') were stale → BLOCK T27 `2f496d31` | → owners |
| CMBS Maturity | $875B total CRE maturing 2026 (MBA *2025 CRE Survey of Loan Maturity Volumes*, released 2026-02-09 — PRIMARY-CITED by HOMER 9/2 at MBA's own text on the newslink.mba.org mirror; 2027 $652B; 2026 is −9% vs $957B in 2025; depositories $396B = the largest lender bucket). $76.6B hard maturity + $400B wall pushed to 2026. No extensions. | 🔴🔴 |
| Federal Layoffs | **Owner-held (LABOR)**; April cell → BLOCK T28 `2f7a5b42` | → LABOR |
| Stagflation Trap | Rate leg at a cycle-high LEVEL; energy leg high. **Live levels → §THRESHOLD STATUS 10Y / 30Y / Brent rows (one source of truth).** The 9/25 narrative read (hike, real-yield-led move, Brent named contracts, KRE drift) → BLOCK T18, crc32 `d372ca3b`. ⛔ HAWK/BRENT/FALCON own oil, BOND owns the curve. | 🔴 |

---

## SIGNAL DASHBOARD → **`STATUS_DASHBOARD.md`** (cold, on-demand — NOT a boot read)

*42 channel rows split out 9/02 (crc `1585e8e9`); live levels stay in §THRESHOLD STATUS. Note → BLOCK T13, crc32 `eb9e9c85`.* Re-check size at any append.

## RESEARCH — POSITION NAMES (pointers to canonical state)

⚠️ **OZK and WAL are PEER AGENTS: read `../OZK/STATUS.md` / `../WAL/STATUS.md`. Their version, EV and PT are never mirrored here.** Full note → `archive/STATUS_rotation_2026-09-24c.md`.
*(→ BLOCK T29, `72424e60`)*

---

## CONVERGENCE MATRIX — Targets & Positions

> **Matrix detail (method notes, runway/reserve legs, per-bank narrative rows) → `STATUS_MATRIX.md` — COLD, on-demand, NOT a boot read; split verbatim 2026-09-24, crc-stamped.** Scores below are the live line; ⚠️ a `0` means clean on the scored channels only, not a clean bill of health. Method + full table → `BANK_EXPOSURE_MATRIX.md`.
> **🔴 FLG 6** *(was LAST)* · **🟠 EGBN 5** · **🟠 AMTB 5** *(absent from v1 entirely)* · VLY 3 · **OZK/WAL/SSB/BKU/SBCF 2** *(WAL was 1st=)* · ZION/MTB/CUBI 1 · **CFG/HBAN 0** *(CFG was 3rd)*.
> 🔴 **FLG price ladder `VX-REG-6.03` RED since 10/7** (band 3 $11.39 broken at **$11.30 [10/7]**; −20.5% vs FROZEN $14.24 at $11.32 [10/9]). **3 settled closes below RED through 10/9**; ladder exhausted (no band beyond RED). Packets PROME + FLG sent 10/7 (`018af9846`). Detector `scripts/vx_ladder_check.py` (exit-code fix `b6544d45d`; today's and NaN bars excluded via `scripts/settled_bars.py`, `8255c2d13`). Matrix score unchanged (price is not an input). *Prior text → BLOCK T21, crc32 `fc6e141e`.*



*Cohort Signal (Hyp A, 6/8) + Life-Sci sector signal: graded and canonical elsewhere → `archive/STATUS_rotation_2026-09-14.md` BLOCKS P+Q; stub → BLOCK T11, crc32 `18724a40`.*

---

## KEY CATALYSTS

*Dates are OWNED by `CALENDAR.md` (earnings dates in its Q3-2026 BANK EARNINGS DATES table, which `scripts/earnings_countdown.py` reads; CUBI + FLG still NOT ANNOUNCED). Read plan → `reports/2026-10-09_Q3_earnings_read_plan.md`. Next: Nano P&A re-check Tue 10/13 · H.4.1 Thu 10/15 / H.8 Fri 10/16 · CFG Fri 10/16 · `REG-T-06` Q3 ~10/29 (est.) · JWT 11/05 · Call Report retrieval 11/07. The prior mirror list → BLOCK T25, crc32 `2288fccd`.*

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

## ⚠️ THRESHOLD STATUS (**10/10 refresh: WAL/KRE/FLG = SETTLED 10/9 closes (two routes); HY/CCC/B/BB FRED 10/8 (10/9 not yet posted, checked 10/10 ~13:5x ET); small-bank borrowings H.8 through 9/30. Claims w/e 10/3, DGS10/30 10/8, VIX/^TNX/Brent 10/9 vendor reads, as before.** Older notes → BLOCK T22, crc32 `7314d335`, and BLOCK T19. Rows not named keep their stated vintage.)

> *(→ BLOCK T30, `597017ec`)*

| Metric | Threshold | Current | Note |
|--------|-----------|---------|------|
| **FHLB advances** | **>$700B, sustain 3 official qtrs; exit <=$650B ×2** | **$810.7B** [6/30/26, FHLB Office of Finance PRIMARY; published 7/30] | 🟠 **`REG-T-06` official run 2 of 3; NOT FIRED. Consequence REVIEW (Will 10/11, WQ-414).** Q4-25 $677B reset; Q1-26 $734B; Q2-26 $810.7B. An official Q3 print >$700B completes REVIEW; 700.0 does not. **Before escalation: top-four growth contribution + qualified SEC-filer borrower median**, with source/endpoints/coverage; missing or incomparable inputs remain incomplete. No numerical breadth cutoff or automatic crisis inference. Nonpositive system growth: signed dollar changes, contribution share NOT-APPLICABLE. Revision/official-count rules → `registry/NOTES.md` §REG-T-06. **10/10 composition evidence:** identified four +$67.5B of +$136.2B par H1 growth (49.5%, incomplete disclosure); original 109-filer median 0%, includes PNC, misses several large banks and non-SEC members; 106-filer +$2.3B is a separate top-three-excluded dollar sum. **Q3 debt nowcast ~ $770B** [10/10 fit, preliminary OF debt through 9/30] does not grade the count. Evidence/caveats → `research/FHLB/README.md`. BOND's `VX-BND-18` gate unchanged. |
| **WAL** | **<$78** | **$74.27** [**Fri 10/9 settled close**, two routes agree] | 🔴 **`REG-T-02` = `FIRED` (cycle 2, since 9/1). Exit run `0-of-3`, COUNTED from `registry/REG_T02_EXIT_LOG.tsv` (28 rows through 10/9), never from here.** Exit = `WAL ≥ 81.90 ×3 CONSECUTIVE closes`; 10/9 is $7.63 / 9.32% short. Sub-78 closes are SUPPRESSED RE-ENTRIES. **Q3 print Mon 10/19 AMC** (call Tue 10/20 12:00 ET). Guards the RH `Dec-18 $70P` (ROLL70) only, not the Fidelity `Dec-18 $65P ×4`. |
| KRE | <$60 | **$69.01** [**Fri 10/9 settled close**, two routes agree]; selloff closing low $68.89 [10/7] | 🟡 **`REG-T-01` = `UN-FIRED`**, $9.01 / 13.1% above the line; −6.9% from 74.11 [9/14]. Sep-30 $60P ×2 SOLD 9/30, rolled to Dec-31 $65P ×2 (Will). `TRY-COND-KREADD` (TERRY) NOT armed on my legs. *Prior WAL/KRE text → BLOCK T23, crc32 `77401802`.* |
| HY OAS | >320 (`REG-T-03`) · >350 (`REG-T-04`) | **315bps** [FRED BAMLH0A0HYM2, **10/8**; ALFRED vintage 10/9, own pull 10:28 ET] | 🟡 **`REG-T-03` GRADED 0-of-3 at the 10/8 cell** (my letter: >320 on 3 consecutive closes): **324 [10/1] = 1 of 3**, **310 [10/2] RESET**, 312 [10/5], 303 [10/6], **309 [10/7] 0**, **315 [10/8] 0** (both ≤320, no run). NOT FIRED. 5bp under 320 (1.6%); RED's FT-02 graded separately. Prior: 17bp under 320 at 10/6, 43bp above the <260 REVIEW line. LIQUID: one tagged print, funding not confirming (SRF $0, SOFR−IORB −3bp [10/1]); X1 CLOSED (LIQUID's). ⚠️ Anchor-drift caveat stands [SIG-723-002]; bank-credit cross-check before reading any HY level as transmission. |
| **CCC/HY ratio** | >3.6× (3 consec) | **3.975×** [CCC **1,252** / HY 315, **10/8**]; 3.977× [1,229/309, 10/7] | 🔴 **HARD-FIRE CONTINUES: above 3.6× on every FRED close since 7/31 (last at or below: 3.542 [7/30]).** 10/7–10/8: CCC +23bp to 1,252 = NEW FRED-window high, HY +6; both legs widening, no CCC-led re-cross ⇒ no escalation by the vector's rule (LIQUID/RED own the tail read). B 308 [10/7] · 315 [10/8]; BB 189 · 194; B held >300 since 9/28, never reached ORANGE 330 (peak 329 [10/1]). Re-entry is LIQUID's (Will 9/26). Full rows → `workbook/VX.tsv` `VX-REG-18.04`/`18.05`. *Prior text → BLOCK T24, crc32 `ec961eab`.* |
| Claims | >300K | **197K** [FRED ICSA w/e **10/3**, API pull 10/9 20:4x ET; next print Thu 10/15] | 🟢 **103K of buffer.** w/e 9/26 **revised 197 → 199K**. Prior chain 198 [9/12] · 198 [9/19, revised from 197] · 197 [9/26, first print]. Sept payrolls +29K, net revisions −60K, U-3 4.2% (WALTER -20261002-001; LABOR's kill did NOT fire). LABOR owns the read. |
| VIX | n/a | **14.84** [**10/9** vendor read]; 15.08 [10/7] | 🟡 Mid-teens through a cycle-high 10Y, HY over 320 for one print and an FLG RED: **not a fear event.** |
| Brent | n/a | **`BZ=F` $104.43** [10/9 vendor read; contract month not re-checked]; $101.46 [10/7] | 🟠 Not re-read on a named contract. HAWK/BRENT/FALCON own the level and the verdict (BRENT settle-window proxies, HEARTBEAT §1). |
| 10Y UST | n/a | **5.24%** [^TNX **10/9** vendor read]; FRED DGS10 **5.22 [10/8]**, 5.28 [10/7] | 🔴 **Cycle high zone, still.** Official 10Y 5.28 [10/2] rose ABOVE its pre-payrolls level after a +29K print; real-yield-led (BOND, HEARTBEAT 10/2). **This is the LEVEL input to my AOCI/NIM/capital channel.** ⛔ BOND owns the curve. |
| **30Y UST** | n/a | **5.60%** [FRED DGS30 **10/8**]; 5.67 [10/7], 5.64 [10/6] | 🔴 Above every September print (5.49 [9/25]); BOND: 30Y real 3.34 = cycle high [10/2 official]. ⛔ BOND owns the series and the high-water claim. |
| **Funding plumbing** | *(`REG-T-08` SOFR−IORB >+15 ×3)* | SOFR−IORB **−3bp** [3.87 − 3.90, **10/8**, WALTER] · RRP **$2.338B** [**10/7**] · **Discount window primary credit $9.965B [Wed 10/7] / $7.701B wk avg** (H.4.1 via WALTER -20261008-049; highest Wednesday since ≥Jan 2024; no registered line; borrowers not named) | 🟢 15bp under `REG-T-08`; quarter-end passed without pressure (−3bp [10/1]). LIQUID owns the structural read. |
| **Financial stress** | *(no registered line)* | **STLFSI4 −0.468** · **NFCI −0.494** [both **10/2**] | 🟡 **STLFSI4 tightened +0.34 in one week (−0.809 [9/25] → −0.468)**, the HY-over-320 week; still on the loose side of zero. NFCI barely moved (−0.510 → −0.494). **Not systemic stress; the direction changed.** |
| **Bank failures, 2026 (FDIC)** | *(no registered line)* | **6** [FDIC Failed Bank List, last updated **9/25**; pulled 10/10]: Metropolitan Capital 1/30 · CB&T West Georgia 5/1 · Kentland 7/10 · Small Business Bank 7/17 · Tioga-Franklin 8/21 · **Nano Banc 9/25** | 🟡 **Most since 2017 (8) by count; ≈ $1.45B assets in total, est. FDIC cost ≈ $243M; none in my 14 or on Will's book.** A count, not a channel: a cohort name failing would be the signal. Re-pull the CSV for the count, never this cell → `reports/2026-10-10_2026_bank_failures_FDIC_list.md`. |
| **Small-bank borrowings (H.8, FHLB + other)** | *(no registered line; 9/29 descriptive bar ≥+5%/month)* | **$314.5B [9/30]**, +$32.9B / **+11.7% in 3 weeks** (281.6 [9/09]); SA, FRED `H8B3094NSMA`, updated 10/9 | 🟠 **Largest 3-week rise in 160 weeks; not a quarter-end pattern (12 prior QEs −4.9% to +1.4%).** ⚠️ **Scale (added 10/10 late PM): the 160-wk window starts after SVB; since 12/2022 it ranks 4th, behind the three SVB weeks (+$290B in the week of 3/15/23 alone). Month-end to month-end Sep: +$17.1B / +5.9% NSA. Large banks +0.9% SA over the same 3 weeks. FHLB system debt +$6.2B in Sep** (nowcast report §4). Small-bank deposits FLAT (5,674 → 5,673); discount window ≤ +$2.9B of it (all banks). ~2/3 shows as cash on SA (+$21.2B), but NOT on NSA (+$5.6B) → precautionary-liquidity read is INFERENCE. Not FHLB-specific, no bank named. Next print Fri 10/16. → report addendum `research/FHLB/reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md`. *(Replaces the 8/05 H.8 deposits row: large +1.28% / small +0.04%, 4wk; git history.)* |

*(→ BLOCK T31, `54808dfd`)*

---

## BOTTOM LINE

**2026-10-09 (Q3 read plan, Will-asked; `reports/2026-10-09_Q3_earnings_read_plan.md`):**
- **Still CONCENTRATED on 6/30 evidence:** named banks with named mechanisms. Total-CRE bad-loan rate down year on year (2.46 → 2.23%). No cheap-deposit flight at 6/30.
- **Multifamily** fell year on year but rose last quarter at FLG / EGBN / CFG. That is individual, not spread.
- **What would make it spread:** only L180 (≥3 of the five mid-pack banks on the original total-CRE basis) or the FL-rail aggregate. Each reads UNKNOWN where missing banks could flip it.
- **Most consequential open question:** that breadth test, which comes from the Call Reports. Retrieval is planned for 11/07, with completeness checked then; the JWT expires 11/05 (Will).
- **Post-6/30 signals pointing the other way** (small-bank borrowings +11.7% in 3 wks to 9/30 with deposits flat; discount window $9.97B [10/7]; size-led selloff; KRE redemptions) name no balance sheet.

*§BOTTOM LINE 2026-10-07 (WQ-318) and 2026-09-29 (attribution) paragraphs, plus the 9/24 rotation pointer → `archive/STATUS_rotation_2026-10-09.md` BLOCK T17, crc32 `6961a43c`. Reports canonical: `reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md` · `reports/2026-09-29_selloff_attribution_and_preprint_observables.md`. Their live claims are carried in the 2026-10-09 entry above.*

**Standing bear ledger → `STATUS_BEAR_LEDGER.md` (COLD, not a boot read).** Prior BOTTOM LINE (9/11, incl. the 9/14 WHAT-CHANGED and watch-list) → `archive/STATUS_rotation_2026-09-24b.md`.

⚠️ **Standing caveat: every instrument this desk owns measures CREDIT or a CLOSED QUARTER.** A non-credit repricing is invisible to it.

## OPEN PROCESS ASKS — dated answers (DAEDALUS 10/8 packets; DONE-WHEN = fixed or answered here)

| Ask | Answer 10/9 | Review by |
|---|---|---|
| *(six DONE rows: Prose-Remedy #1 · F#4 minor · F#4 flags · F#4 neg-res · wiring ⑰ · PR#6 ask 3)* | → BLOCK T32, `2f23b1f6` | — |
| Registry TOKEN `V1V3-ACCELERATE` rename (from F#4 flags) | DEFERRED: coordinated change with WALTER, which reads it (`registry/NOTES.md`) | next registry touch |
| L546 float-tie: `kre_float.py:102`, `si_refresh.py:45` round before compare | DEFERRED to next touch of either file (DAEDALUS: no deadline, LATENT) | next touch |
| *(WALTER -033, DONE 10/9)* | → BLOCK T33, `a100038c` | — |
```

## MEMORY.md

Bytes: 18939 · crc32: c2116bf4

```markdown
# REGINALD MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate. For verified mistake patterns with prevention rules, see `LESSONS.md`.*

---

## Feedback
- [2026-04-02 ×5] Will: **boot transparency** (say what you read, in what order); **freedom over pre-set priorities** (context not directives; ONE open question, not a ranked top-3); think **long-term infrastructure** (scaling + durability); **position data lives in POSITIONS.md** too; **discrete tasks, approval between each.** Full entries → BLOCK M10, crc32 `2d7441a5`.
- [2026-04-16] Will wants REGINALD to read full source documents (PDFs, 10-Ks) before opining, not just spot-check sections. Caught that I only keyword-searched the earnings release initially. Thoroughness > speed for primary source analysis.
- [2026-04-22] **Iteration philosophy validated:** Write Round 1 with available data, then improve as more data arrives. Will explicitly said "begin with what we have and we will improve on it as we learn more" when public press releases were truncated and he was going to provide supplement PDFs. Don't wait for perfect data to start writing.
- [2026-04-22] **"What I NEED FROM YOU" lists work.** When analysis files end with an explicit gap list, Will reads it and delivers the exact files. Keep these lists concise and specific (filename + what's in it).
- [2026-04-22] **Thesis architecture: "synthesis + pointer" pattern.** THESIS.md carries the synthesized takeaway from sub-docs (2-3 sentences + headline number + pointer), not duplicated detail. Sub-docs (IQHQ_PLAYBOOK, SEVEN_CREDIT_DEEP_DIVE) hold the deep analysis. Changelog tracks THESIS.md only. Filter: thesis-level shifts get changelog entries; evidence accumulation stays in sub-docs + KB rows. Scope guard: if writing a 4th sentence of sub-doc summary in THESIS.md, it belongs in the sub-doc.
- [2026-04-22] **Per-bank CHANGELOG** mirrors `thesis/CHANGELOG.md` format (vX.Y; first entry pins prior as v1.0) — now `../OZK/`, `../WAL/`-owned. → BLOCK M11, crc32 `05b22ac4`.
- [2026-06-02] **Scope-clean sessions:** Will will explicitly fence a session ("REGINALD files only, no messaging, no position decisions/analysis"). When fenced, refreshing facts (prices, dates, FRED data) and marking resolved events is in-scope hygiene; recomputing EV/overvaluation, sending outbox replies, and making roll calls are out. Flag stale-but-load-bearing values (e.g. SCENARIOS spot price) rather than recomputing — "flag don't re-rate."

## Findings + References → **`MEMORY_REFERENCE.md`** (COLD, on-demand — **NOT a boot read**)

*Split out 2026-09-14 verbatim, crc32 `5db54789`, 11241 B, under READ_CAP rule 4(b). Nothing deleted.* **Holds the HOW-TO and LOOKUP half:** SEC EDGAR curl pattern (WebFetch 403s on sec.gov) · FFIEC CDR REST/JWT · FRED via `fetch.py` + the T+1 convention · the `perl -0pe` table-extraction recipe (a naive `sed` collapses 8-K tables) · catastrophic-regex warning · two-route derived-figure check · FDIC BankFind as an independent cross-check · the paywall map · **OZK files NO SEC periodic reports** · the cert/RSSD/CIK table · the WALTER LIAISON record. **Pull it when you are about to fetch a filing or debug an instrument — not at boot.** ⚠️ **Mistake patterns are NOT here — they stay in `LESSONS.md`.**

## Session Notes

⚠️ **Open question (10/10 late PM):** does the late-September jump in smaller banks' borrowing (H.8 `H8B3094NSMA` +$32.9B / +11.7% in 3 weeks to 9/30; deposits flat) **continue, hold or reverse in the Fri 10/16 print (week of 10/7)**, and does any Q3 print show it **with deposits leaving** (the PNC pattern spreading)? **New 10/10:** FHLB system debt rose only +$6.2B in Sep, so most of that borrowing was likely NOT FHLB (or was funded from FHLB liquidity). The OF combined Q3 figure (~10/29) can only flag the FHLB-liquidity case (advances well above ~$770B); per-bank attribution waits for the 11/07 Call Reports.
- The L180 breadth test (11/07 Call Reports) stays the CRE question; it is in the read plan, not here.
*Prior open question + LAST SESSION 10/9 PM (incl. 10/10 AM) + PRIOR SESSION 10/9 AM → `archive/MEMORY_rotation_2026-10-10.md` BLOCK M1, crc32 `1548bf8c`.*

### LAST SESSION — 2026-10-11 Sun, PROME-launched Codex (Sol selected; backend ID UNKNOWN)
**WQ-414:** exact plan `474e09d66`; PROME checkpoint `e71a0fff617d077a76f03860133d621dfef08af5`, P1 applied (keep documented panel incl. PNC). Encoded REVIEW + two breadth measures, official-count/missing/comparison safeguards; no new thresholds or trades. Canonical `236a091d4` + delivery `2912cd369` independently accepted at `1b937462e` (2 reads, zero consequential defects); explicit full-closeout ask received and standard checks completed. Origin confirmation is returned via native closeout receipt. Full artifact `reports/2026-10-11_WQ414_option-B_result.md`.
**Boot:** network retry completed (CFG previously documented 10/8 Series G 5.03 alert); FLG RED unchanged, 3 settled closes through 10/9; markets closed. One inbox assignment; zero WALTER-lane packets. Prior 10/10 bridges and affected current rows preserved verbatim → `archive/WQ414_operating_snapshot_2026-10-11.md`.
### CHANGES SINCE LAST SESSION
(leave blank — next-boot market.py + drift-grep populates)
### NEXT SESSION
**★ NEXT BOOT (set 10/10 PM; Will's three catch-up items are DONE, see LAST SESSION):**
0. **10/10 offered sends:** WQ-414 approval now recorded and implemented under PROME checkpoint; SHADE · BROCK · CFG read-note offers remain pending, outside this repair. Hub `research/FHLB/README.md`. CFG 10/16 context: Delaware Life revolver; no new frozen-frame grade. RED replies only if disputed. NEXUS brief pre-fold preserved in `archive/WQ414_operating_snapshot_2026-10-11.md`; re-check size each append.
1. **Weekly funding read: Thu 10/15 H.4.1 · Fri 10/16 H.8** (`H8B3094NSMA`, `WLCFLPCL`, small-bank deposits + cash, SA AND NSA). Continue / hold / reverse? A deposit decline alongside = the PNC pattern spreading → packet LIQUID + PROME the same session. Bars stay descriptive (base-rate before any registration).
2. **`REG-T-06` WQ-414 option B (Will 10/11):** REVIEW encoding independently accepted at `1b937462e`. At official Q3 publication: >$700B completes 3-quarter run; no nowcast count. Before escalation record top-four growth contribution + documented SEC-filer median (PNC included), endpoints, basis and coverage; missing/incomparable/nonpositive growth handled by `registry/NOTES.md` §REG-T-06. No new breadth threshold. LIQUID/BOND ruling packets + WALTER token notice authored in this delivery; recipient consumption unverified.
3. **REG-07 (WQ-412): Will's VOID-or-grade before SSB prints Wed 10/21 AMC;** without a word, it grades on the CHANGE (scores at 68%).
4. **HBAN puts (WQ-302):** Will sells or rolls by Wed 10/14; write the fill back to POSITIONS from the broker export.
5. **Large-bank desk:** DAEDALUS holds the packet (`32d24f8ff`). Citi / USB / WFC FHLB purpose is that desk's perimeter if built.
6. **BaaS perimeter (NEW thread 10/10):** look up CCB / CASH / GDOT Q3 print dates → CALENDAR; at CCB's Q3 10-Q read partner concentration for Bluevine ($2.1B moving to VLY, close early 2027); ask at VLY's 10/22 call.
*Full 9/29 list (every carried item's text) → `archive/MEMORY_rotation_2026-10-07.md` BLOCK M2, crc32 `401793b1`. Items marked (M2) keep their full text there.*
**🔴 0-Q3. RUN THE Q3 READ PLAN AT EACH PRINT — `reports/2026-10-09_Q3_earnings_read_plan.md` §5 schedule** (CFG **Fri 10/16** first). Grade only the frozen frames: WQ-318 list · CRE top-3 §6 · L35 / L521 · FL frame + A3 · §2.3 AMTB lines. Read the WAL / OZK / FLG desks' grades for their names; the cross-bank row is mine.
- **§2.0 rules govern:** individual ≠ spread · original total-CRE basis, multifamily separate · missing → UNKNOWN · release = provisional.
- **11/07 = planned Call Report retrieval; check completeness FIRST.**
- **Update the §0 judgment only on L180 BROADER or FL-rail TRANSMISSION.**
- **CUBI / FLG dates:** update the CALENDAR earnings table when announced. The countdown reads it, and FLG's T-03 looks 10/16.
**🔴 0a. WAL exit grading:** 10/9 GRADED 10/10 (row 28, 0-of-3). Grade **10/12 onward** from settled bars (`scripts/settled_bars.py WAL`: two routes, today's bar excluded). Count from `registry/REG_T02_EXIT_LOG.tsv` (28 rows through 10/9, 0-of-3). 2-of-3 → packet TERRY.
**🔴 0a-NEW. Tier test each boot:** FRED HY/CCC/B/BB. ⚠️ The cache-busted CSV route FAILED 10/9 (HTTP/2 error / timeout), so the API route (`fetch.py fred`) was used. If HY prints >320 again, START the REG-T-03 count and run the bank-credit cross-check.
**🟢 0-DAEDALUS. DONE 10/10 (Will go-ahead):** REG-03/06/07 instruments named (REG-07 grades on the CHANGE in SSB NPL/loans vs 0.62% base, since its level reading was true at birth; **flagged to Will before 10/21**) · F#4 wording fixes (registry token `V1V3-ACCELERATE` rename DEFERRED, WALTER reads it) · wiring ⑰ VX re-cut · stale tables (VX 27 STALE, FLOW frozen, AOCI/FUNDING FROZEN-VINTAGE, KB +3).
**🟡 0-LIMB. L180's "new foreclosure build" is unquantified.** Read literally (any QoQ rise), WAL met it at Q2 (+2.3%). Print the size beside every grade. A floor is Will's rule to make; don't add one.
**🟠 0-HBAN. `HBAN $16P Oct-16 ×2` ITM — Will rules by Wed 10/14 (WQ-302, card `MGMT-HBAN16P-OCT16`).** Supply the bank-side read if asked; write back the ruling. HBAN prints 10/22, after expiry.
**🟠 0-NEW-PUTS. Fidelity WAL Dec-18 $65P ×4 / OZK Nov-20 $40P ×4 (FORGE D-74):** fills/approval unrecorded; WAL/OZK desks own the position records; TERRY owns any card. My Q3 rows (WQ-318 + CRE top-3) are the thesis reads that bear on them.
**🟠 0a-NANO.** 10/9: P&A **still NOT posted**; FDIC **bid summary posted 10/8** → §3 re-run done (`reports/2026-10-09_nano-banc-bid-summary-and-section3-rerun.md`: retained-pool ≈32–42%). **Re-check P&A Tue 10/13**, then Tuesdays; none by 10/27 → DEWEY records route. On posting: size Pools A/D, place the $97.1M HFS book + WAL O1 DOTs, re-run §2 with pool sizes. Bar date not posted.
**🟠 0a-FL.** ✅ Dates done 10/7 (BKU 10/21 BMO · SSB 10/21 AMC · AMTB 10/22 AMC · SBCF 10/27 AMC; VLY 10/22 BMO). Grade the frozen frame `reports/2026-09-24_FL_bank_rail_Q3_FROZEN_frame.md` at each print; ≥2 TRANSMITS → packet CORAL + PROME the same session.
**🟡 0a-0. FLG ladder is RED and EXHAUSTED** — no band beyond RED. Exit-code defect FIXED `b6544d45d`. **Intraday-bar defect FIXED 10/9 (`8255c2d13`).** Census other frozen-baseline bands into the script (M2) — NOT this cycle (Will: no further tooling expansion).
**🔴 0a-bis (M2).** **11/05 FFIEC JWT expiry (Will), two days before the 11/07 run.** *(As-made packet DONE 10/10 PM; the DAEDALUS VX re-cuts were DONE 10/10 as wiring ⑰, per STATUS §OPEN PROCESS ASKS.)*
**🔴 0a-ter (M2). Carry-premise audit** — the most valuable item on this list; unchanged.
**🟠 2 (M2). Pre-print observables into `boot.py`** — base-rate before building. WQ-318 adds the per-bank observables (NIB average, IB cost, FHLB) but they are quarterly.
**🟠 3 · 4 · 6 · 6d · 6f · 6g · 6h · 6i · 6j · 6k · 7 (M2)** — ~~FHLB Atlanta/SF 10-Qs~~ (DONE 10/10) · OREO vector base-rate; REG-07 re-mark + REG-03/07 re-specs at the Q3 print, deliberately; EGBN runway post-break re-audit; read-cap every closeout; `boot.py` SHORT_INTEREST writes; aged 9/2 items. Unchanged; full text in M2.
**🟢 Done 10/10 PM:** catch-up ①–③ + FHLB follow-ups + write-back pass (LAST SESSION). **🟢 Done 10/9 PM:** monitor repair (OZK FDIC route · VLY CIK · coverage · no false all-clear · countdown · settled bars) · Q3 read plan + Will's clarifications. **🟢 Done 10/7:** 0-CARD (TERRY `TRY-COND-KREADD`, conditional, not armed) · 0-EXP (KRE rolled) · 0-WB · 0-WQ318 · item 1 TRY-FIRE-002 dates · DAEDALUS header · R3 phrases.

**CARRIED LESSONS — behaviour, not record.** *Newest first. Aging rule (9/02): full entry → one-line rule AND the full text goes to `archive/` verbatim + crc in the same pass. ⛔ Never age a lesson by deletion (the 12-21 compressions archived nothing; git history only). Preamble → BLOCK M7, crc32 `8028ecb4`.*
47. **[10/10 eve] In a SendMessage to PROME I typed a commit reference ("ab9b-REGINALD") that no command had printed; I sent the real hash (`8d31de2aa`) one message later.** The same session I keyed two FHLBank CIKs from memory (1325878 = Topeka, 1316220 = CAPE Holding); the filer-name check caught both before use.
   - ⇒ **An identifier (hash, CIK, accession) goes into a message only from a command's output in the same turn; a CIK is used only after the response names the intended filer** (lesson 43; `finding_attribution_authenticates_a_figure_its_named_source_never_produced`).
46. **[10/10 late PM] I sent "largest 3-week rise in 160 weeks" to WALTER, STATUS and Will. The 160-week window began 9/13/2023, just AFTER SVB, whose first week alone was ~9× the move.** I had also measured from a 9/09 trough (+11.7% vs +5.9% month-end to month-end). Both were true, and both made it look bigger.
   - ⇒ **A base-rate window must include the episode that defines the scale (here 2023), or name what it leaves out. Quote the change from a neutral base (month-end), not from the trough.**
45. **[10/10 PM] I told Will "the regionals were flat, so this isn't regional stress" from a 6/30 quarterly print, and checked the weekly H.8 only when he asked whether newer data existed.** It showed small-bank borrowings +11.7% in the three weeks to 9/30, the 160-week max. Same day: my own 9/11 receipt had written "Brier on 55%" against WQ-112(i), ratified ten days before it.
   - ⇒ **Before a "this is not happening" read built on a quarterly print, pull the fastest proxy that could contradict it, and date both.**
   - ⇒ **Before writing a scoring rule into a receipt, read the ratified canon (`FORGE/PREDICTION_DISCIPLINE.md`), not the asking packet's framing.**
44. **[10/10] I turned "I can't see deterioration" into "I expect stabilisation," and called the earnings outlook "mixed" without an expectations baseline.** "Mixed" was the expected result of my own test lines, not results against consensus.
   - ⇒ **Not seeing deterioration is not a forecast.** A relief or decline call needs positive evidence plus the market's expectations baseline.
   - **Alarm levels are confirmations, not preconditions.**
   - **Don't swap one unsupported direction for the opposite one.**
43. **[10/9] My 8-K monitor checked VLY under SEC CIK 74260, which is OLD REPUBLIC INTERNATIONAL, and checked OZK at the SEC, where OZK has not filed since 2017.**
   - **Neither could ever look wrong:** a valid feed for the wrong company, and an empty feed for a non-filer, both read as "no 8-K".
   - **Found at the evening boot, not by any check.**
   - ⇒ **An instrument keyed by an identifier must verify the response NAMES the intended entity, and must treat "nothing ever filed here" as a broken route, not a quiet bank.** `finding_instrument_reports_clean_against_the_wrong_reference`.
41. **[10/7] I pre-registered an expiry as 'lapse worthless, decision-free — no roll' (KRE $60P Sep-30). Will sold and rolled it the next day.** His standing practice (USER.md, 9/30) is to sell or roll before expiry. ⇒ **An expiry pre-registration carries a sell-or-roll branch, never a lapse branch, and the write-back reads the broker record, not my forecast.**
42. **[10/7] A Call-Report deposit cost (interest ÷ RC-K average) reproduced the company figure at 3 of 6 banks and was off by 30–60bp at the other 3.** I had built it as the 'one comparable basis'. ⇒ **Check a derived cross-bank measure against each bank's own figure BEFORE using it as the comparable column; the basis that looks cleaner is not the one that is true.**
40. **[9/27] I adopted a peer's 'correction' (CREED's FLG 17.5%) without re-running it, and it was wrong: it added the charge-offs to a denominator that already contained them. My own evidence pack labelled $2,088M as pre-charge-off.** The FLG desk caught it a day later. ⇒ **A correction to my figure gets the same recompute as the figure itself, before I write 'Accepted'** (`finding_a_correction_pass_is_unreviewed_work`). Same session: I told Will PFBC was unchecked against its filings when my own morning report had its Call Report. **Grep my own reports before describing what I have.**
39. **[9/27] A KB fact sourced from an LLM research pass sat INVERTED for 7 months: `ML-REG-044` said 'Fed C&D March 4, 2025'. The date was the Issuu UPLOAD date of the Fed documents, and March 2025 was the order's TERMINATION.** Caught by a peer desk (WAL), not by me. ⇒ **A regulatory action is cited from the regulator's own record (Fed enforcement CSV / agency release), never from a host that re-posts it; a date on a re-host is the host's date until proven otherwise.** Full evidence → `reports/2026-09-27_nano-banc_legal-leg.md` §1.
38. [9/24] Before an inference about a peer's name leaves my desk, read the primary it rests on or label it `INFERENCE FROM SECONDARY`; a brief compresses — check each compressed claim against its own data before sending (three CATO catches in one brief). Full text → BLOCK M6, crc32 `037ca359`.
37. [9/11] A claim about a PEER's ledger stays SEARCH-NOT-FOUND until you open the owner-declared path; assert a peer's STATE from their FILE, never from packet memory.
36. [9/2] A path in my prompt is a claim about the filesystem: resolve symlinks, and `git ls-files --error-unmatch` before claiming an artifact exists. 36-37 full text → `archive/MEMORY_rotation_2026-09-24c.md`.
35. [9/2] A ruling must ship with its retroactive sweep in the SAME commit; sweep by the SHAPE of the thing (a regex), not the value being retired — a supersession marker hides the prior vintage from a token grep.
34. [9/2] A source name authenticates a figure like an exact level does; asked for a construction you never built, return the NEGATIVE WITH EVIDENCE (schema, columns, n=) — silence reads as latency.
33. [8/28] Self-audit before handoff is a fleet standard — measure whether YOU do it on findings you offer.
32. [8/28] Before proposing a threshold, check which DIRECTION it trips and that the level and sign agree — a kill can be sign-inverted as easily as a confirm.
*Lessons 12-31 are indexed in `archive/MEMORY_rotation_2026-09-24d.md` (which points on to their verbatim archives: `MEMORY_carried_lessons_27-31` crc `05486924`, `…22-26` crc `9148add8`; 12-21 in git history).*
*32-35 aged 2026-09-24 to one-line rules (above); full text + the 8/27 housekeeping flags → `archive/MEMORY_rotation_2026-09-24b.md`.*

(leave blank — next-boot market.py + drift-grep populates)
```

## ROADMAP.md

Bytes: 22610 · crc32: be8c805c

```markdown
# REGINALD ROADMAP — "Where are we"
**Updated:** **2026-10-11 (Sun, WQ-414 accepted after independent result read).** Prior affected operating text → `archive/WQ414_operating_snapshot_2026-10-11.md`.
*Stamps 10/10 AM (BLOCK R5, crc32 `3693ce98`) and 10/9 PM · 10/7 · 9/29 (BLOCK R3, crc32 `adb2708f`) rotated VERBATIM → `archive/ROADMAP_rotation_2026-10-10.md`.*
*Stamps 9/27 PM, 9/27 and 9/26 rotated VERBATIM → `archive/ROADMAP_rotation_2026-10-07.md` BLOCK R1, crc32 `ebe14531`.*
*Stamps 9/14 and 9/02 rotated VERBATIM → `archive/STATUS_rotation_2026-09-27.md` BLOCK R1, crc32 `cb6c187f`.*

Persistent state-of-REGINALD tracker across sessions. **SCRATCH** = loose notes, intra-day workspace. **MEMORY.md Session Notes** = session-bridge handoff (what just happened, what's next). **STATUS** = live dashboard. **ROADMAP** = what threads are open, what data we're waiting on, what questions are unresolved, what we want to investigate next, what just got done.

**Maintenance discipline:** Updated at session end before commit. If a thread is moved to RESOLVED, that's the audit trail of what each session shipped. Pruned aggressively — promote to thesis/KB/research or delete; do not just accumulate.

---

## OPEN THREADS
*Active work spanning multiple sessions. Each entry: what / status / next step / last-touched.*

| Thread | Status | Next Step | Last Touched |
|--------|--------|-----------|--------------|
| *(12 aged threads, 4/26 → 6/20)* | CLOSED 2026-09-02 with per-row verdicts → `archive/ROADMAP_aged_threads_2026-09-02.md` (crc32 `a277c281`). Nine had been answered by later work and nobody closed them. | **Rule: a thread that resolves as a side effect of other work does not self-close — closing is the answering session's write-back obligation.** Full row → BLOCK R4, crc32 `03552a2c`. | 2026-09-02 |
| 🟡 **NEW 2026-09-02 — Commercial Chapter-11 filings as a NON-CREDIT / FORWARD bank instrument** *(the one live part extracted from the dead 5/9 pinch-hitter row)* | ⛔ **The 5/9 figure (+42%) is 4 months stale and unusable — do NOT adopt it.** What survives is the INSTRUMENT question, and it is my standing open one: **every gauge this desk owns measures CREDIT and a CLOSED QUARTER**, which is precisely why the 9/1 fire and the 9/2 bounce both came back unsortable at name level. Commercial bankruptcy filings are forward-ish and not sourced from a bank's own closed-quarter print. | **Base-rate BEFORE building** — separation, lead time vs bank credit prints, and whether it moves independently of HY. ⛔ **"Don't build it" is a real answer** and is the likelier one; the failure mode to avoid is adopting a series because it is available rather than because it discriminates. Companion candidates already listed on the blind-spot thread (forward P/TBV dispersion · revision breadth · KRE creation/redemption · short interest · options skew) — ⚠️ **all of those are TTM- or trailing-window-averaged, so they inherit the one-regime defect; this one may not.** | 2026-09-02 |
| *(closed threads)* | 24 RESOLVED rows → `archive/ROADMAP_rotation_2026-09-02.md` BLOCK C (crc32 `1d242fd4`; non-contiguous row-set, named deviation). One had sat RED for ~6 weeks after grading (WAL Q2 frame). | Full row → BLOCK R5, crc32 `101f4efa`. Re-check size at any append. | 2026-09-02 |
| 🔴 **`REG-T-02` exit grading (FIRED 9/1, cycle 2)** | Count lives ONLY in `registry/REG_T02_EXIT_LOG.tsv` (27 rows through 10/8, run `0-of-3`; 10/8 close $75.50, two routes; **10/9 owed from settled bars via `scripts/settled_bars.py WAL`**). Guards the live Dec-18 $70P (ROLL70). TERRY's clause (d) (missing vendor bar = labelled substitute or UNKNOWN, never a holiday) CONCURRED 9/26. | Grade every settled close; 2-of-3 → packet TERRY; exit → UN-FIRED + announce WAL/PROME. | 2026-10-09 |
| 🔴 **CCC/HY escalation (re-arm MET 9/24, sent 9/26)** | Live tier state → STATUS §THRESHOLD STATUS CCC/HY row; re-entry is LIQUID's (Will 9/26). 9/29 row → BLOCK R7, `2ba7bf66` | Tier test each boot (MEMORY 0a-NEW); B ORANGE >330 watch; only a CCC-LED re-cross escalates | 2026-10-10 |
| 🔴 **NEW 2026-09-26 — CRE top-3 (FLG · EGBN · OZK), Will-asked** | Report `reports/2026-09-26_CRE_vulnerability_top3.md` + dossiers + `workbook/CRE_RCN_COHORT.tsv` + `scripts/cre_loss_scenarios.py`. AMTB dropped (non-CRE credit); WAL 4th (the only name accelerating every quarter); VLY 5th. | **FLG ladder `VX-REG-6.03` RED 10/7 ($11.30; packets PROME + FLG `018af9846`; ladder exhausted).** Grade each report §6 'weakens if' line at the Q3 prints (FLG ~10/23, EGBN ~10/21, OZK TBA ~9/30 — ALL ESTIMATES). $133M gap: FLG answered 9/27 — structural (50–73% every period since FY23), location NOT DETERMINABLE, leading reading = loss at exit; bridge §① narrowed, 17.5% 'fix' withdrawn (20.45% stands). Loss bridge → `reports/2026-09-26_CRE_top3_loss_bridge.md` (`scripts/cre_loss_bridge.py`). Metric changes M1–M5 are RECOMMENDATIONS pending Will's word; not applied. | 2026-09-26 |
| 🟠 **NEW 2026-09-27 — Nano Banc failure (9/25): forward reads on a DELIVERED report** | `reports/2026-09-27_nano-banc-failure-forensics.md` (d8010b97f), accepted by PROME. **Shared figure ≈ $120M ≈ 17% [9/22 base] is MINE; CREED/WAL/PROME cite it.** Leading markers at Nano (Memo-3 share 79% of C&I; ALLL/noncurrent 10%) are n=1, NOT adopted. | **10/9: P&A NOT posted; bid summary read → §3 re-run (`reports/2026-10-09_nano-banc-bid-summary-and-section3-rerun.md`). Next P&A check Tue 10/13, then Tuesdays (DOCKET L516).** Bar date (WALTER). Fed OIG MLR ~3/25/27 → grade §2d/§3. If a national MI3-share screen is ever built, base-rate it on the FFIEC bulk RC-C file first. | 2026-09-27 |
| 🟠 **NEW 2026-09-27 (written back 10/07) — VLY: NEITHER + one bank-specific early flag** | Q2: MF past-dues $9.4M → $101.5M, NOO nonaccrual +$20.8M, $108M CRE payment-delay mods, in the same quarter as a disclosed decline in quantitative CRE reserves (categories undisclosed). `KB ML-REG-171`; `reports/2026-09-27_VLY_CRE_transmission.md`. | **At VLY Q3 (est. Thu 10/22, NOT announced; DOCKET L521):** does the MF 30–59 cohort cure or roll; CRE nonaccrual vs $256.1M; re-defaults of the $108M; reserve direction. A CHECKPOINT — deferrals run to ~Q1-27. **+10/10: VLY agreed 9/27 to buy Bluevine for $340M (~$255M cash + ~6.3M shares; 8-K acc 0001193125-26-403391): $2.1B of small-business deposits, close early 2027, ~5% TBV dilution at close** → ask at the 10/22 call how and when the deposits move; see the BaaS thread. | 2026-10-10 |
| 🟡 **NEW 2026-09-27 (written back 10/07) — PFBC ~$60M litigation-dependent NPLs (Nano/Makhijani shared collateral)** | Mostly exited at par in Q2 ($68.4M note sales); ~$60M left, resolution contingent on legal proceedings (SECONDARY call summary). Mark-contagion channel, not solvency. `KB ML-REG-173`. PFBC is OUTSIDE my cohort. | Read PFBC Q3 (date not checked) for the ~$60M; an FDIC sale of Nano liens on shared properties would print a mark (Nano P&A check-by 10/9, DOCKET L516). No TERRY packet (not in Will's book). | 2026-10-07 |
| 🟠 **NEW 2026-09-24 — Cohort AOCI: the rate leg's first FILED test** | All 14 opt out of AOCI (reported CET1 unaffected). ZION is the outlier (AOCI 22% of CET1). Q3 scenario −$2.6B to −$4.3B after-tax (duration ASSUMED). WAL expects to cross $100B by end-Q1 2027. → `reports/2026-09-24_cohort_AOCI_exposure.md` | At the Oct Q3 prints: grade reported AOCI/TBV per bank against the scenario; does KRE's drift track the TBV hit or run ahead of it (MEMORY open question)? | 2026-09-24 |
| 🟠 **`CREED-T-03` level leg has no sourceable parent** (the 3.40% series is absent from the Q1-26 edition) | Unresolved; CREED owns the trigger. | Full reasoning → `archive/ROADMAP_rotation_2026-09-24.md`. | 2026-08-27 |
| 🟠 **Regional CRE OREO +26.4% in one quarter — the only Q2 tell pointing toward recognition, and it is mine** | **NEW 8/27**, routed by CREED out of a clean QBP because CRE OREO on regional balance sheets is my surface. **The Q2 improvement's COMPOSITION splits by bank size:** regionals ($10-250B) grew CRE OREO **$723.9M → $915.3M (+26.4%)** *while their PDNA fell* 1.39→1.22%; the >$250B class did the opposite — OREO **−8.9%** with CRE NCOs **0.14→~0.22% (+57%)**. ⇒ **regionals FORECLOSING, money-centres CHARGING OFF** — one headline, two mechanisms, and the regional one moves the problem ONTO the balance sheet. | ⚠️ **Fence carried verbatim and it is load-bearing: accounting-scale comparison, NOT attribution** — both are stocks, the QBP shows no flow between them, loans also exit PDNA by cure/charge-off/sale/modification. **"Of a size that COULD account for ~18%" — never "did."** ⚠️ **Does NOT move S3** (CREED held it at 2); a 26% move on a $915M stock is not bank transmission. **Next step: watch it into Q3 (~late Nov QBP), and decide whether regional CRE OREO earns a registered vector or stays an on-demand read — base-rate first, "don't build it" is a real answer.** | NEW 2026-08-27 |
| 🟢 **Gate C increment 2 — nothing owed by me** | Commands a1/a2/a6/a7 immutable; precondition ⑦ resolved-blessed 8/27. | Never re-author or edit; a defect is fixed only by a NEW command. Full row → `archive/ROADMAP_rotation_2026-09-24.md`. | 2026-08-27 |
| 🔴 **The blind-spot question — is a credit-only instrument set capable of answering "why are banks moving?"** | **NEW 8/20, and it is the session's real output.** Today's null is only informative if my instruments *could* have found something. Every one of them measures CREDIT (MI3, NDFI, CRE-DQ, NCO, coverage, criticized). A non-credit repricing would produce this exact result and I would never see it. | **9/29: first non-credit / pre-print set BUILT** — weekly H.8 (NDFI loans, small-bank deposits, large time deposits, borrowings, C&I) + H.4.1 primary credit + KRE float + PFF/BIZD legs, report §3; all 🟢 through 9/16–9/23 (NDFI lending +1.1%, no deposit flight, discount window ordinary). **10/10 re-read: 2 of 8 bars CROSSED, both funding-side** (small-bank borrowings +11.7% in 3 wks to 9/30, the 160-week max — ⚠️ a post-SVB window; SVB's first week was +$290B, ~9× this; FHLB debt +$6.2B in Sep; discount window >p90 two weeks, $9.97B [10/7]). Credit-side bars stay 🟢 → banks lining up cash, not credit transmission (FHLB report addendum; WALTER signal to LIQUID). Descriptive bars only — **base-rate before any registration**; wire into `boot.py` as a deliberate task. Still unbuilt: P/TBV dispersion · revision breadth · skew. | 2026-09-29 |
| *(closed thread)* | 8/14 → 9/14 de-rating ATTRIBUTED 9/29 (beta, no bank component) → BLOCK R2, crc32 `454040d4`; Recently Resolved 9/29 PM row carries it. | — | 2026-10-07 |
| 🟠 **`REG-T-06` — Q3 official grade after WQ-414 repair** | **REVIEW**; official run 2 of 3 through Q2; debt nowcast excluded. >$700B ×3 official quarters, exit <=$650B ×2; before escalation both qualified breadth measures. Procedure `registry/NOTES.md` §REG-T-06 | At Q3 publication grade official level and record top-four contribution + documented SEC-filer median (PNC included), endpoints/basis/coverage. Incomplete and nonpositive growth fences apply. Peer packet consumption unverified. Hub `research/FHLB/README.md`. Repair resolved below. | 2026-10-11 |
| 🟠 **NDFI instrument (8/20)** | `workbook/NDFI_COHORT.tsv`, 26 banks at FFIEC primary. LESSONS NDFI entry DONE 8/20. 8/20 row → BLOCK R8, `23401de8` | **Open:** registered vector or on-demand pull (base-rate first); ledger SCHEDULED 11/07 | 2026-10-10 |
| *(5 aged July threads)* | **CLOSED 2026-10-10 (Will-directed)** with per-row verdicts → `archive/ROADMAP_aged_threads_2026-10-10.md` (crc32 `fd8df983`): domain-sweep SUPERSEDED · TX/Sun-Belt MF ANSWERED · BKU warehouse/buyout ANSWERED + SUPERSEDED (NDFI cohort) · ZION muni CLOSED, trigger is AEOLUS's · CCC/HY counter NOT BUILT → `ROADMAP_BACKLOG.md`. | — | 2026-10-10 |
| 🟠 **NEW 2026-10-10 — BaaS / sponsor-bank perimeter (WQ-228, Will-ruled 9/15): OPENED because it had NO live row** | CLAUDE.md DOMAIN SCOPE carries the ruling (watchlist CCB · CASH · GDOT; cadence = each 10-Q/10-K partner-concentration disclosure + event 8-Ks), but no STATUS / ROADMAP / CALENDAR row existed, so nothing would have checked it. **First live lead (10/10):** Bluevine's accounts are FDIC-insured "through Coastal Community Bank" (bluevine.com, read 10/10) with a program-bank sweep behind it; VLY is buying Bluevine ($2.1B deposits, close early 2027). ⇒ **a partner-deposit exit at CCB: VLY's deck says the partner program is TERMINATED at closing (early 1Q27) and deposits move within 180 days (~1H27)**; the on-balance-sheet share at CCB vs swept is UNKNOWN. VLY's motive = funding (97% LDR, $5.3B brokered; `KB ML-REG-188/189`). | **CCB Q3 10-Q:** partner-concentration / Bluevine deposit balance, any disclosed transition · **VLY Q3 call Thu 10/22:** migration timing · **Q3 print dates for CCB / CASH / GDOT: NOT CHECKED** → add to CALENDAR when checked. No trade, gate or threshold (the ruling says so). | 2026-10-10 |
| 🟠 **AOCI final-rule watch** | The proposal is net capital RELIEF for Cat III/IV with a 5-yr phase-in to 2032 (CALENDAR H2-2026 row). | Watch for final-rule publication. Full row → `archive/ROADMAP_rotation_2026-09-24.md`. | 2026-08-20 |
| 🟡 **Life-science strategic-default pattern (N=2: WAL $99M + OZK IQHQ)** | #3 test ran 8/31: EMPTY. 9/02 row → BLOCK R9, `7ad64c53` | **Watch only; do NOT re-raise without a third instance**; a thesis-level move lands on STATUS + `thesis/CHANGELOG.md` | 2026-10-10 |
| 🟠 **Cohort-selection rule — does the up-cap finding change WHO is in the screen? — NEW 8/13, dated carry** | **Flagged, deliberately NOT solved.** The cohort was picked under ratio-era priors: MTB/HBAN/VLY were admitted as *clean large-cap benchmarks*, and the Q2 run then found **MTB holding the cohort's largest absolute MI3 book ($4.95B, ~2x WAL) and HBAN +100% YoY** — the control group is where the dollars went. If the question is "who is most concentrated", the cohort is fine; if it is **"where is hidden CRE pooling"**, the selection rule is measuring the wrong population (`finding_ranked_head_sample_is_not_the_population`). **+9/27 (written back 10/07): PFBC (CRE 357% + uninsured 50%, cert 33539) shares Nano/Makhijani collateral and sits OUTSIDE the 14 — a live example that the cohort cannot see a name the failure forensics found (`KB ML-REG-173`).** Not re-cut mid-instrument because that silently changes what every prior figure means. | **Decide before the 2026Q3 run (CALENDAR 11/07)**, so any change lands on a quarter boundary with BOTH cohorts reported once. Read-path is triple: this row, the CALENDAR 11/07 row, and a note beside `COHORT` in the script itself ("do not silently grow the list") so the next runner meets it at the point of temptation. | NEW 2026-08-13 |
| 🟠 **SUCCESSOR: per-bank item-4 → item-9.a migration series** | ⚠️ At OZK the premise changed: MI3 ≡ PV09 (9.a), and L181 adjudicated LEGITIMATE (9/24): the reported debt-on-debt balance fell; runoff is inferred and a relabel is NOT EXCLUDED. | Re-scope at the 11/07 cohort run: test WHERE each bank's MI3 resides (item 4 vs 9.a) before building a migration series. Full row → `archive/ROADMAP_rotation_2026-09-24b.md`. | 2026-09-24 |


---

## AWAITING DATA
*Known external prints with dates. Order = chronological.*

**Added 2026-07-30 (full inbox pass):**

| Date | Item | Why it's mine |
|------|------|---------------|
| **Q3 + Q4 2026 prints** | **`BRK-31` — BROCK's pre-registered falsifier, 45%, resolves 2027-01-31.** *"≥1 of the 11 mapped banks discloses a PC/NDFI-attributable reserve BUILD, or names a private-credit counterparty in a criticized/classified migration, in its Q3 or Q4 2026 print."* **Invalidation:** Q3 **and** Q4 both release-or-flat with no PC/NDFI attribution **and** CFG's combined book still growing at Q4 → BROCK downgrades bank-warehouse 🔴(4)→🟠(3) and **re-dates the whole transmission thesis.** | **I am the data source that resolves it** — it grades on the bank prints I read. Registered off my 7/25 11-name map, which moved BROCK's NDFI vector 🔴🔴(5)→🔴(4) (first score BROCK has moved since 6/20, and it was a downgrade). **Watch for it at the Q3 prints; don't let it get absorbed into "recognition lag."** |
| *(3 fired/resolved rows)* | ROTATED VERBATIM 2026-10-07 → `archive/ROADMAP_rotation_2026-10-07.md` BLOCK R3, crc32 `6cbd872a` | — |

*(**Fired during the 5/21–6/2 gap, all dispositioned at the 7/17 audit** — 6 rows, 1,317 B, ROTATED VERBATIM 2026-09-02 → `archive/ROADMAP_rotation_2026-09-02.md` BLOCK M, crc32 `eeb45db6`. All six are closed: MI3/FFIEC PDD RESOLVED 8/7 · FDIC QBP Q1 folded · APO Epstein → BROCK, no-material-event · WALTER LIAISON calibration moot under Routing v2 · ROAD-to-Housing → HOMER · FL reinsurance → CORAL, resolved benign.)*
**Forward (from 6/2) — table ROTATED 2026-09-29 → `archive/ROADMAP_rotation_2026-09-29.md` BLOCK R2, crc32 `f623792c`.** Every row was fired or is CALENDAR-owned (claims weekly · AOCI comment closed 6/18 · Jun-18 expiry cleared · capital-rules final rule TBD · WAL Q2 7/21 graded · CRE-DQ-by-tier Q2 graded · IQHQ Aug swept-empty · OZK sub-notes 10/1 · Affinius Oct). **Forward dates live in `CALENDAR.md` only.**

*Still-pending integrations (printed, not yet worked — see OPEN THREADS): OZK 10-Q; APO Q1 (Atlas SP / warehouse); BLS state jobs + NFP (LABOR/CARL primary, check claims).*

---

## OPEN QUESTIONS
*Flagged but not actively worked. Decide before next acting on them.*

| Question | Surfaced | Action Owed |
|----------|----------|-------------|
| ✅ *Two RESOLVED rows (Exit-100% re-anchor, Will 6/19 · SSB $90P provenance, Will 6/19)* | → BLOCK R3, crc32 `5958e5ae` | Both in force: HY <260 = REVIEW trigger (STATUS §EXIT RULES); SSB $90P = real, sold, unrecorded-exit class (LESSONS). |
| *(five low-priority questions, 4/5–5/1: KB.tsv rows 056/057 column drift · HERMES revival · BROCK in SUB_AGENTS.md · 'sector silence' heuristic · MEMORY vs SCRATCH naming)* | 2026-04/05 | Actions owed verbatim in BLOCK R10, `79a78362`; none dated. KB drift: next workbook hygiene pass |

---

## INVESTIGATIONS BACKLOG → **`ROADMAP_BACKLOG.md`** (cold, on-demand — NOT a boot read)

*6,229 B SPLIT OUT 2026-09-02 verbatim, crc32 `6d6ce8a5`, under READ_CAP rule 4(b).* Nothing in it is dated or owed — it is the pull-list for a research session with no urgent catalyst, so every boot was paying for it and almost no session acted on it. **Re-check size at any append, or on 2026-10-02, whichever is first.**

## RECENTLY RESOLVED
*Last ~2 weeks. Top of mind so the audit trail is visible without reading commits.*

| Date | What | Result |
|------|------|--------|
| **2026-10-11** | **WQ-414 registered-procedure repair accepted** | Encode `236a091d4`, delivery `2912cd369`, PROME independent receipt `1b937462e`: 2 reads, zero consequential defects. Nine boundary cases pass; PNC panel preserved. Full closeout explicitly requested; peer consumption unverified. |
| *(9/11 row)* | REG-15 NO-OWNER thread closed 9/11 → `archive/ROADMAP_rotation_2026-10-07.md` BLOCK R4, crc32 `0ab0bf65` | — |
| **2026-10-10 eve** | **External FHLB draft checked + FHLB hub (Will)** | `research/FHLB/` (`8d498d5bd`): 2 reports moved (stubs at old paths), verification (3 ledgers: draft = lead list, not a source), key filing tables, sources (PDFs local-only), 25 crc-stamped copies · RED packet: KRE bull case "$480B" vs OF $676.7B / $810.7B (`b9ca8d708`) · WQ-412 SouthState name fixed by PROME (`3780a92d6`) |
| **2026-10-10 late PM** | **FHLB dig + failures list + sweep (Will)** | Q3 nowcast ≈ $770B from FHLB Office of Finance debt (`ce1245f28`) · six 2026 failures at the FDIC list; `DECK_EVIDENCE` Metropolitan cert 57120 → 57488 (`7cbab9f8e`) · sweep: SVB-scale caveat everywhere, stamps, KB ML-REG-186..188, VLY–Bluevine verified, BaaS thread opened |
| **2026-10-10 PM** | **Will's three catch-up items** | ① DAEDALUS as-made audit: all 20 rows, REG-13 re-formed, REG-07 scoring line corrected (`28c7dd7dd`) · ② FHLB composition: half of H1 growth = four very large banks; `REG-T-06` non-discriminating → WQ ask via PROME; weekly H.8: small-bank borrowings +$32.9B in 3 wks to 9/30 → WALTER signal (`e4916e89a`, `e1fc74154`) · ③ five July threads closed (archive crc `fd8df983`) |
| **2026-10-10** | **Overdue process items (Will go-ahead)** | REG-03/06/07 instruments (REG-07 level reading true at birth → graded on the change; VOID is Will's call) · F#4 wording + wiring ⑰ (V1V3 token rename deferred, WALTER reads it) · VX 27 STALE, FLOW frozen, AOCI/FUNDING FROZEN-VINTAGE, KB +3 · large-bank desk packet `32d24f8ff` |
| **2026-10-09 PM** | **Monitor repair + Q3 read plan (Will-directed)** | OZK 8-K/insider → FDIC (OZK desk route reused) · VLY CIK 74260 (= Old Republic) → 714310 · FLG/AMTB/CFG/CUBI covered · no all-clear on failure (network-blocked live test) · countdown ← CALENDAR table · settled bars only · read plan + §2.0 rules · FL frame A3 · baseline: total-CRE 2.23%, MF 3.58% (Q2 rise at FLG/EGBN/CFG = individual) · L180 dry run *c* = 1 |
| **2026-10-07** | **WQ-318 baseline + L527 catch-up (PROME-spawned, Opus)** | `reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md`: no cheap-deposit flight at 6/30 at any of six; CUBI the one overlap name; pre-committed Q3 list (CFG 10/16 · WAL 10/19 · OZK 10/20 · EGBN 10/21) · 0-WB done (KB +6) · REG-T-03 0-of-3 · FLG RED · WAL Q3 locked → TERRY · inbox 14+19 → 0 · R3 phrases declined (`Nano Banc` covers) |
| *(9/24 + 9/26 rows)* | Rotated VERBATIM 2026-10-10 → `archive/ROADMAP_rotation_2026-10-10.md` BLOCKS R1 `ae15fc12`, R2 `158cd65b` | — |
| *(9/27 PM · 9/29 PM · 9/29 · 9/27 rows)* | Rotated VERBATIM 2026-10-10 PM (2-week rule + read-cap) → `archive/ROADMAP_rotation_2026-10-10.md` BLOCK R4, crc32 `ac6efce7` | — |
| *(rows 2026-09-01 and older)* | **ROTATED VERBATIM** → `archive/ROADMAP_rotation_2026-09-24.md` (2-week rule) and, for 7/17 and older, `archive/ROADMAP_rotation_2026-09-02.md`. | |

---

*Companion files: `MEMORY.md` (curated cross-session memory + session-bridge handoff) | `SCRATCH.md` (loose intra-day notes) | `STATUS.md` (live dashboard) | `CALENDAR.md` (forward dates) | `LESSONS.md` (verified mistake patterns)*
```

## NEXUS_BRIEF.md

Bytes: 20633 · crc32: d093c29a

```markdown
# REGINALD — NEXUS Brief

**Status:** 🔴 on the LEVEL and 🔴 on the MACRO INPUT, 🟠 on the MECHANISM. **`REG-T-02` FIRED since 2026-09-01 (cycle 2), still FIRED through the 10/9 close:** 28 closes graded, none qualifying, run **`0-of-3`**; latest **WAL $74.27 [10/9 settled, two routes]** (exit ≥81.90 ×3; count lives in `registry/REG_T02_EXIT_LOG.tsv`). **`REG-T-03` (HY >320 ×3) 0-of-3** at the 10/8 cell — 309 [10/7], 315 [10/8]; 324 [10/1] was one print. CCC 1,252 [10/8] = FRED-window high. **FLG ladder `VX-REG-6.03` RED** since the 10/7 close $11.30; 3 settled closes below RED through 10/9 ($11.32). Matrix unchanged. **Nano Banc (10/9):** FDIC bid summary posted 10/8 (P&A not yet) — Sunwest bought Pools B/C at 82.30%/80.17% of book, 0.85% deposit premium, no loss-share; shared figure ≈$120M ≈17% [9/22] unchanged, retained-pool allocation ≈32–42% (desk scenario) → `reports/2026-10-09_nano-banc-bid-summary-and-section3-rerun.md`.

**WAL quarantine (cutover 7/25):** WAL thesis/predictions/positions are **`../WAL/`-owned — no WAL figure is restated here**; read `../WAL/STATUS.md`. REGINALD keeps the matrix row + cohort context. New via WAL 8/7 (consume-with-fences): **the V1a MI3 falsifier finally RAN and came back PLATEAUED <24%**, and WAL's NDFI share made a new high — **both under WAL's explicit "weights UNCHANGED pending Will's rulings" fence; do not consume WAL's scores as settled.**

**Domain:** Regional banks (watchlist + KRE) — convergence terminus for CRE, NDFI, private-credit, labor, stagflation channels; peer coordination with CREED/BROCK/CORAL/OZK/WAL (all top-level).

> **★ TRANSFERABLE DISCRIMINATOR (EGBN grade — the one other desks should take):** **coverage thinning has TWO causes with OPPOSITE meanings** — ACL failing to keep pace with *incoming* problem credits (bear, under-provisioning) vs ACL *consumed by outgoing realized losses* (de-risking). Same arithmetic, opposite conclusion. Companion adopted 8/10 (HOMER's version for delinquency rates): **when a DQ headline improves, check the provision line in the same filing** — Fannie MF SDQ "improved" to 0.60% via modification while its MF provision rose +49% QoQ.

**As of:** **2026-10-11 (Sun, WQ-414 encode after PROME plan checkpoint) · STATUS pin: same closeout commit; acceptance `1b937462e`.** **Everything FHLB → `research/FHLB/` (README first).** Will approved REVIEW; encode `236a091d4` + delivery `2912cd369` independently accepted at `1b937462e`; explicit full-closeout ask received. Closed-market data remain dated 10/9. External FHLB draft remains a lead list, not a source; fabricated Council quote and reversed GAO/Delaware Life findings rejected. CFG Fri 10/16 first; concentration view unchanged. Full pre-fold preserved verbatim → `archive/WQ414_operating_snapshot_2026-10-11.md`.

## VIEW

- **★ FHLB + WEEKLY FUNDING (10/10 PM) — what other desks should take:**
  - (1) **The Q2 FHLB build is a big-bank story:** by borrower type (OF Q2 CFR Table 3) commercial banks +$121.4B, insurers +$25.0B (share 27.0 → 24.9%), credit unions + savings institutions −$13.7B; about half of H1's +$136.2B (par) is PNC +27.4 · Citi +20.0 · USB +14.0 · WFC +6.0; three districts (Pittsburgh, NY, Cincinnati) are 73.5%. The original matched 109-filer panel median is 0% and includes PNC; the separate 106-filer sum excluding the top three movers is +$2.3B. The panel omits several large banks and non-SEC members; it is not system breadth. Atlanta +6.9%; SF −10.6%. **Why:** Citi says growth funding in its own 10-Q; USB borrowed and held cash (INFERENCE); WFC is growth; **only PNC replaced deposits that left** (credit clean).
  - (2) **`REG-T-06` now means REVIEW (Will 10/11, WQ-414):** >$700B on 3 consecutive **official quarterly** advances; exit <=$650B on 2 official quarters. Current official run remains **2 of 3** through Q2. Before escalation record **top-four growth contribution + qualified matched SEC-filer borrower median**, endpoints, basis and coverage (PNC included). Missing/incomparable breadth stays incomplete; zero/negative aggregate growth has no contribution percentage. No new cutoff or automatic crisis inference. Procedure → `registry/NOTES.md` §REG-T-06. **Q3 debt nowcast ≈$770B (±2 sd $728–813B)** is an in-sample fit using preliminary debt data, **never an official count**; liquidity drawdown can break it. Dated model → `research/FHLB/reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md`. Historical automatic-alarm wording preserved; independent result accepted (`1b937462e`).
  - (3) **Weekly H.8 to 9/30:** smaller banks' borrowings (FHLB + other) **+$32.9B / +11.7% in 3 weeks, the largest rise in 160 weeks** (⚠️ that window starts AFTER SVB, whose first week was **+$290B in one week**, ~9× this; month-end Sep +5.9% NSA; large banks +0.9%), not a quarter-end pattern; **FHLB system debt rose only +$6.2B in Sep vs banks' H.8 borrowings +$54.5B** (repo/fed funds, FHLB liquidity drawdown, or large members paying down: not separable yet); deposits flat; discount window above its 60-week p90 for two weeks ($9.97B [10/7]). Credit-side bars quiet (non-bank lending growing, no line draws). **Read: banks lining up cash, not credit transmission (INFERENCE; no bank named; FHLB share unknown; the cash leg holds on SA but not NSA).** Next H.8 Fri 10/16. → `research/FHLB/reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md`.
- **★ Q3 READ PLAN (10/9) — what other desks should take:**
  - (1) **Individual ≠ spread.** Worse numbers at FLG/EGBN/OZK/AMTB are severity at named banks. A spread needs L180 (≥3 of 5 mid-pack, total-CRE bad-loan RATE on the Call Report basis: nonaccrual + 90+ over construction + MF + NOO, or a foreclosure build) or the FL-rail aggregate.
  - (2) **Keep total CRE and multifamily apart.** At 6/30 total CRE was 2.23% (2.46% a year earlier). Multifamily was 3.58%, down year on year but **up from 3.23% in Q2, all at FLG/EGBN/CFG**; mid-pack multifamily was flat or falling.
  - (3) **Release figures are provisional;** a bank missing at the 11/07 retrieval makes a breadth verdict UNKNOWN wherever it could flip it.
  - (4) **Dry run Q1→Q2:** *c* = 1, WAL on a literal foreclosure-build limb (+2.3%; that limb is unquantified).
- **★ WQ-318 FUNDING vs NON-BANK EXPOSURE (10/7) — what other desks should take:** (1) **at 6/30 no cheap-deposit flight at any of six banks** — NIB share flat (within 0.5pp) or up YoY; interest-bearing deposit cost −27 to −52bp over four quarters; uninsured share UP at 5 of 6 while brokered share FELL at 6 of 6 (run-prone share grew, market-funded share shrank). (2) **CUBI is the overlap name:** NDFI 34.1% of loans (PC slice 19.96%), IB deposit cost 3.54% (highest), FHLB +72% YoY, brokered 21%, uninsured 44%. (3) **Unfunded NDFI ≈ drawn at CFG ($22.5B) and OZK ($3.3B)** — draw capacity, not a forecast. (4) **Rate-sensitivity figures are INCOMPARABLE** (static vs dynamic, shock vs ramp, beta stated only by WAL); every bank's own model has NII up with rates, but **FLG's short-rate-only scenario has the opposite sign** — the 9/16 hike was a short-end move. (5) The six hold ~3% of system FHLB advances and ~6% of Q2's growth — **`REG-T-06`'s build is not in this set.** ⚠️ A Call-Report deposit cost does not reproduce company figures at CUBI/OZK/EGBN. → `reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md`.
- **★ CRE→BANK TRANSMISSION (9/27 PM) — what other desks should take:** (1) **At 6/30 the 14-bank cohort's CRE bad-loan rate FELL** (2.46% → 2.23%; H1 CRE NCO $528M → $452M), and deterioration sits at named banks (only OZK jumped). **Breadth is tested at the MID-PACK Q3 prints** (WAL/VLY/SSB/BKU/SBCF; DOCKET L180), not at the top three. (2) **Workout FUNDING is UNDISCLOSED for ~all exit dollars** (FLG, OZK, EGBN, VLY): 'par payoffs show the refi market is open' is an INFERENCE (CREED). (3) **Hardship-modification tables are NOT comparable across banks**: OZK booked $0 CRE against 37 RESG extensions. (4) **FLG's 47% past-due on 12-month MF modifications is a delinquency LEVEL in a changing population, NOT a cohort failure rate** (Will 20:49); the issuer's $29M/$286M 'subsequently defaulted' are UNRECONCILED. (5) **VLY Q2:** multifamily 30–89 $9.4M → $101.5M + $108M of 8-month CRE payment deferrals + a quantitative CRE reserve decline. Q3 (est. 10/22) is a CHECKPOINT; deferrals run to ~Q1-27. (6) **FLG NYC rent-regulated recognised loss = 20.45%** of original ((351+76)/2,088); the '17.5%' is withdrawn. Files: `reports/2026-09-27_cross-bank_CRE_transmission.md` · `reports/2026-09-27_VLY_CRE_transmission.md`.
- **★ NANO BANC (9/27) — what other desks should take:** (1) **its CAPITAL loss was litigation-DOMINANT alongside credit deterioration** (2025 legal expense $46.3M the largest charge in a −$75.3M loss; provision $16.7M; composition, not an exact bridge), **its DIF loss is CRE assets** — two different mechanisms; don't merge them. (2) **The early warnings were on the Call Report two years out:** Memo-3 CRE-finance-not-secured-by-RE = **79% of C&I [12/31/23]** (my cohort max ~24%), and ALLL/noncurrent fell 109% → 10% while noncurrent rose. **n=1 — not an adopted screen.** (3) **'Fed C&D 3/4/2025' (my Feb KB row) was INVERTED** — an Issuu upload date; the Fed C&D (1/18/2022) was TERMINATED 3/20/2025. If you carried it, correct it. (4) '$108M BANC+EFSC' is three lenders incl. Nano — not citable per bank.
- **★ SELLOFF ATTRIBUTION (9/29 evening) — what other desks should take:** the regional drawdown is TWO legs with different causes: **8/14→9/14 = market + small-cap beta, financials contributed +0.1%** (a 5-factor OLS, R² 0.63); **9/15→9/29 = the financials SECTOR (−5.0 of −5.9 log-%) led by the largest banks** — inside my 14-bank cohort return sorted on ASSET SIZE (ρ −0.72), not on AOCI (−0.30), NDFI (−0.2/−0.3) or my credit score (+0.48, wrong way). KBWB −7.4% / IAT −7.7% vs KRE −5.8%. **⇒ bank EQUITY repricing concentrated in incumbents' size, consistent with the rate/AOCI leg in DOLLARS or with NEXUS's candidate Root B; NOT a regional-credit event** (FLG/VLY excepted — credit-shaped, both legs). Pre-print set saw no transmission through 9/16–9/23. ⚠️ **Through 9/30 two FUNDING bars crossed** (first bullet); the credit bars are still quiet.
- **★ CCC/HY + TIER TEST — STATE AS OF 10/7 (9/29 bullet in the 10/7 snapshot):** every tier widened 9/28 → 10/1 (HY 302 → **324**, B 309 → **329**, BB 183 → 204, CCC 1,146 → **1,215 = FRED-window high**), then HY/B/BB retraced by 10/6 (303 / 302 / 185) while CCC held 1,214. **`REG-T-03` 0-of-3 (one tagged print); B never reached ORANGE 330.** The ratio's rise to **4.007×** is HY-tightening-led = denominator form ⇒ no re-escalation (9/26 escalation stands; Will 9/26: re-entry is LIQUID's). Funding did not confirm (SOFR−IORB −3 to 0bp; SRF $0). STLFSI4 tightened +0.34 to −0.468 [10/2]. ⚠️ HY sits downstream of bank credit in my chain — cross-check before calling transmission.
- **MI3/OZK carry-forward fences:** cohort cells reproduced; **37.6% remains withdrawn**. MI3 time-series steps and cross-bank denominator differences constrain interpretation; OZK’s −64% is dominated by a single-quarter memo-designation step, so de-risking remains **UNRESOLVED**. WAL’s PLATEAUED level verdict stays under its owner’s unchanged-weights fence; secured office books are separate. Three full 8/13 detail bullets preserved verbatim in `archive/WQ414_operating_snapshot_2026-10-11.md` (§NEXUS_BRIEF); sources `reports/2026-08-13_MI3_cohort_rerun.md` and `workbook/MI3_COHORT.tsv`.
- *Three 8/13 bullets (UP-CAP migration retired · THESIS doc retired, STATUS canonical · MI3 screen hardened) moved verbatim to `archive/NEXUS_BRIEF_snapshot_2026-10-07.md`; their facts are unchanged and still hold.*
- *GSE MF (8/27: "improving" RETRACTED, the book is deteriorating with a modification-suppressed headline) and Labor (8/27 claims read) bullets moved verbatim to `archive/NEXUS_BRIEF_snapshot_2026-10-10.md`. Live levels: GSE MF in STATUS §THESIS CRE row (HOMER-owned, 9/26); claims 197K [w/e 10/3] in STATUS (LABOR owns the read).*
- **Tariff guard on utilization data** (HAWK): 301 live since 7/24, 338 Canada since 8/19 — C&I line-utilization reads spanning these dates carry a tariff artifact in BOTH directions (CALENDAR standing guard).
- **UWM / non-bank servicer channel (HOMER 9/29):** Fitch cut UWM to B+ on 8/7 (found 53 days late; HOMER's Class A fired); Citi MSR line $1.875B drawn at 6/30 (not a regional). My bank-side read (warehouse lines at WAL/BKU) folds into WQ-318's NDFI/warehouse column, not a separate thread.
- **FL residential undertone:** SBCF residential nonaccrual +136%/6mo (small base, ~0.9% of book) — consistent with HOMER's REO-conversion phase signature and MARCO's re-timed FL-$ hole (flatten-and-extend into Q1-Q2 2027; capacity tell ~Sep 15 schedule filings).

## CALIBRATION

- **Conviction (decomposed):** direction-H on the *concentration* shape (5 independent confirmations; cross-bank Q2 CRE bad-loan rate FELL 2.46% → 2.23%; WQ-318 adds: funding not breaking at 6/30) · timing-M (resolvers: the 10/16–10/27 prints, then the 11/07 Call Report run) · level — my live level claims are threshold distances: **WAL $3.73 under $78 [10/9] (FIRED), HY 5bp under 320 [10/8] (0-of-3), B 15bp over 300 [10/8], claims 103K under 300K, KRE $9.01 over $60 [10/9], FLG through RED.**
- **Diverge from market by:** less than at any point this year, and honestly so — the narrowing was driven by my own grades, not the tape. Where I still diverge: the market reads benign GSE MF headlines and clean small-tier prints at face value; I carry both as composition-masked (modification suppression; definitional NPA exclusions at BKU).
- **Uncertain about:** (1) **whether the bank-equity leg is now running AHEAD of credit** (HY half-retraced while KRE/FLG/OZK kept falling) — a non-credit repricing my instruments cannot see, or credit about to re-widen into the prints; (2) whether CFG's +$3.85B Q2 FHLB draw is brokered substitution (INFERENCE) or funding pressure; (3) the cause of OZK's −4.31% on 10/6 (none found); (4) the MI3 cohort-selection rule, decide before 11/07; (5) **whether the small-bank borrowing step-up continues (10/16 H.8), how much of it is FHLB, and whether a Q3 print shows it with deposits leaving.**
- **Failure patterns to mind:** a detector that exists only as a TSV cell has no lag guarantee — the FLG band-1 break sat 8 days, the band-2 break was caught at the first boot (zero lag) once `vx_ladder_check.py` existed (census every other frozen-baseline band into it); a broker chart's last print at the bell is not the vendor close (WAL $75.21 vs $75.76 on 9/29 — grade the settled bar, label the other); a correction to my figure gets the same recompute as the figure (lesson 40).

## CROSS-DOMAIN

**SENDING:**

| To | Signal | Priority | Mechanism |
|----|--------|----------|-----------|
| PROME + FLG | `VX-REG-6.03` RED on the 10/7 close (sent `018af9846`); ladder exhausted | 🟠 | Registered routing; matrix unchanged |
| PROME | WQ-318 delivered (`a033c799c`) + memo; register CFG 10/16 / CUBI grading rows | 🟠 | Report + KB ML-REG-176..180 |
| TERRY | WAL Q3 LOCKED Mon 10/19 AMC (`fe37dd785`); `TRY-COND-KREADD` REGINALD arm NOT met (`db3565b15`) | 🟠 | Packets; cards are TERRY's |
| WALTER → OZK | OZK closed below the OZK desk's <$45 band 10/6 + 10/7 (signal lane, `db3565b15`) | 🟡 | OZK grades its own band |
| BROCK | BRK-31 grading input at Q3/Q4 prints — *I am the data source* | 🟠 | PC/NDFI-attributable reserve builds |
| PROME · LIQUID · BOND · WALTER | WQ-414 REVIEW encode `236a091d4`; result + ruling/interface packets | 🟠 | Independent acceptance `1b937462e`; recipient consumption unverified; peer gates unchanged |
| WALTER → LIQUID | Small-bank borrowings +11.7% in 3 wks to 9/30 (signal lane, `e1fc74154`) | 🟠 | Descriptive bar, not a registered trigger |
| PROME | WQ-414 prior nowcast evidence (`047ef11d4`), now governed by approved REVIEW | 🟠 | Official quarterly count only; debt nowcast excluded |
| WALTER → LIQUID | AMENDMENT to the signal: SVB scale (+$290B in one week) + FHLB debt +$6.2B in Sep (`b680ef50d`) | 🟠 | Routed WITH the original as `SIG-W-20261010-007` (WALTER `40b424536`; LIQUID action) |
| DAEDALUS | H2 as-made receipt complete, 20 rows (`28c7dd7dd`) | 🟡 | For its 10/12 sitting |
| PROME · RED | WQ-412 named SSB "State Street" (`8d31de2aa`; PROME fixed `3780a92d6`) · RED's KRE bull case cites FHLB "$480B" vs OF $676.7B/$810.7B (`b9ca8d708`) | 🟡 | Corrections; owners edit their own files |

**WAITING FOR:**

| From | Input | Expected | How it changes my view |
|------|-------|----------|------------------------|
| Will | FFIEC JWT renewal before **2026-11-05** | before Nov | The 11/07 Call Report run (MI3 + WQ-318 F1/F3/N confirm) dies without it |
| CFG · WAL · OZK · EGBN | Q3 releases 10/16 · 10/19 · 10/20 · 10/21 | Oct | Grades the WQ-318 rows on their named lines |
| FLG · CUBI | Q3 date announcements | Oct | Locks their WQ-318 grading dates |
| Will | REG-07 VOID-or-grade (WQ-412) | before 10/21 | Decides whether REG-07 grades |
| FDIC | Nano Banc Sunwest P&A posting (NOT posted 10/9) | re-check Tue 10/13 | Re-runs forensics §3 (L516) |
| Broker (PROME/ANVIL) | Activity view for the new Fidelity WAL $65P / OZK $40P (D-73/74) | — | Records entry dates; cards stay TERRY's |

## NEXT DECISION POINT

- **What:** **the Q3 read plan's frames, one per print, CFG first (Fri 10/16)**: WQ-318 rows (UP/DOWN/INCONCLUSIVE per bank), CRE §6 lines, L35/L521, FL frame + A3, AMTB non-CRE lines. **The §0 judgment moves only on L180 BROADER or FL-rail TRANSMISSION.** Plus `REG-T-02` exit grading every settled close (0-of-3, 28 rows through 10/9), the tier test on each FRED cell, and the weekly funding read (H.4.1 Thu 10/15, H.8 Fri 10/16).
- **When:** 10/16 · 10/19 · 10/20 · 10/21 (+ FLG/CUBI TBA); every close; FRED each morning ~10:15 ET.
- **Falsifier context:** the expected modal outcome is INCONCLUSIVE at most banks (declared deposit programs at WAL/EGBN, OZK's pre-announced cost inflection) — written in advance so it can be wrong. An UP row at CUBI or CFG is the result that would change the view.

## FORWARD CATALYSTS (next 2-6 weeks)

| Date | Event | Threshold / Signal |
|------|-------|---------------------|
| 🔴 **Every close** | `REG-T-02` EXIT grading (WAL ≥81.90 ×3) | 0-of-3 (28 rows); 10/9 $74.27 is 9.3% short |
| 🟠 **Daily ~10:15 ET** | FRED HY/B/BB/CCC (cache-busted CSV) | HY >320 restarts `REG-T-03`'s count; B ORANGE >330 |
| 🟠 **Thu 10/15** | Claims (197K [w/e 10/3]) | >300K = ORANGE banks → RED (far) |
| 🟠 **Thu 10/15 · Fri 10/16** | H.4.1 discount window · H.8 small-bank borrowings/deposits | Step-up continues / reverses; a deposit decline alongside = the PNC pattern spreading |
| 🟠 **Tue 10/13** | Nano Banc P&A posted? (L516; bid summary read 10/9) | Size Pools A/D; re-run §2 |
| 🔴 **Fri 10/16** | **CFG Q3** — first WQ-318 grade | IB cost ≥2.18%, NIB ≤20%, FHLB >$7.32B, capital call + PC >$15.46B |
| 🔴 **Mon 10/19 AMC** | **WAL Q3** (call Tue 10/20 12:00) | WQ-318 WAL row; WAL desk frame (L170); AOCI vs scenario |
| 🔴 **Tue 10/20 AMC** | **OZK Q3** (call 10/21 08:30) | OREO sale prices vs 95–100% marks; COIBD ≥3.34%; L520 |
| 🟠 **Wed 10/21 → Tue 10/27** | EGBN · SSB (10/21 AMC) · BKU (10/21 BMO) · VLY (10/22 BMO) · AMTB (10/22 AMC) · SBCF (10/27 AMC) · FLG/CUBI TBA | L35 · L521 · FL rail frozen frame · L180 breadth at 11/07 |
| 🔴 **Nov 5 → Sat Nov 7** | FFIEC JWT expiry (Will) → **planned Q3 Call Report retrieval, completeness checked then** | L180 breadth (UNKNOWN rule) · cohort-selection rule decided BEFORE the run |
| 🟠 **~Thu 10/29 (est.) → Nov** | FHLB Q3 report → `REG-T-06` leg 3 (>700 completes REVIEW; **nowcast ≈ $770B is excluded**) · FHLBank 10-Qs · FDIC Q3 QBP (~11/25) | Both qualified breadth measures before escalation; a miss >$40B vs nowcast ⇒ check FHLBank liquidity drawdown |

---

*Brief format follows NEXUS_BRIEF schema (R3 + amendments 7, 10). Created 2026-07-09; rebuilt 2026-08-10. Folded 2026-10-11 as session’s LAST operating write-back after final STATUS acceptance write (same closeout commit); prior full brief → `archive/WQ414_operating_snapshot_2026-10-11.md`. Earlier fold history remains in that full snapshot.*
```

## research/FHLB/README.md

Bytes: 8974 · crc32: 756b6405

```markdown
# FHLB research hub (REGINALD)

*Built 2026-10-10 (Sat ~20:3x ET) on Will's direction: "consolidate it all into one centralized area. Even if we just copy the data/files over there." Owner: REGINALD. **Re-check this map at any append, or on 2026-11-07 (the Q3 Call Report run), whichever is first.***

**Alarm-history caveat (2026-10-11):** the 2026-10-10 reports, copied proposals and row snapshots retain their dated, as-made EARLY-CRISIS discussion. Those sections describe the pre-ruling letter; current operation is REVIEW under `registry/NOTES.md` §REG-T-06. Never use a preserved copy to grade today's consequence.

**Start here.** Everything the fleet has on the Federal Home Loan Banks (FHLBs) is either IN this folder or listed below with its path. Two kinds of file live here:

- **Canonical (edit here):** `reports/`, `verification/`, `data/KEY_PRIMARY_TABLES.md`, `sources/SOURCES.md`, this README.
- **Copies (never edit here):** `copies/` and `data/DESK_ROWS_SNAPSHOT_2026-10-10.md`. Each copy opens with a 2-line banner naming its source path, commit and crc32; `copies/MANIFEST.tsv` lists all 25. Their figures are as of each source's own date. To refresh a copy, re-copy the source; to fix a figure, fix the SOURCE.

## The questions

| # | Question | Where it stands (2026-10-10; re-check) | Read |
|---|---|---|---|
| Q1 | **Is FHLB borrowing a sign of regional-bank stress?** | **WQ-414 option B approved 10/11: REVIEW**, REVIEW after >$700B on 3 consecutive official quarterly advances; exit <=$650B on 2 official quarters. Before escalation: top-four growth contribution + qualified matched SEC-filer borrower median. Missing/incomparable breadth stays explicit; no breadth cutoff or automatic crisis inference. Procedure: `registry/NOTES.md` §REG-T-06. Official run remains 2 of 3 through Q2; debt nowcast excluded. The 10/10 composition evidence is dated and incomplete; no system-wide borrower median. Original question row → `archive/WQ414_operating_snapshot_2026-10-11.md`. | `registry/NOTES.md` §REG-T-06 · `reports/…_Q2_composition…` · `reports/…_Q3_nowcast…` |
| Q2 | **What is inside the total?** | By borrower type at 6/30/26: commercial banks 56.4% · insurers 24.9% · credit unions 9.1% · savings institutions 8.2%. Insurer dollars are a record ($202.8B) but their share fell from 27.0% at Q1. | `verification/…` · `data/KEY_PRIMARY_TABLES.md` |
| Q3 | **The insurer channel (Athene, Delaware Life) and its bank links** | Real, owned by **SHADE** (insurers) / **BROCK** (private credit). Losses in an insurer failure land mainly on policyholders and guaranty funds; the FHLB's protection there rests on **state** law and holding the collateral, not the federal §10(e) lien. Bank links are small and named: Citizens $450M revolver to Delaware Life (status after YE2025 unknown) · Truist and Fifth Third paused Delaware Life sales · WAL = 13% of FHLB San Francisco's book (YE2025). | `verification/…` ledgers B and C · `data/KEY_PRIMARY_TABLES.md` |
| Q4 | **Is the 2023 lifeline tighter for a weak bank?** | **Unknown (inference only).** FHFA AB 2024-03 (active) tells FHLBanks to lend on the member's condition, not just collateral; the FHLBanks' own Council calls it "procyclical". **No public evidence** of an actual pullback; FHFA-OIG calls member credit risk "abated" for FY2026. | `verification/…` ledger C (R1–R3) |
| Q5 | **Where did September's small-bank borrowing come from?** | Small banks' borrowings +$32.9B in 3 weeks to 9/30 (H.8), but FHLB system debt rose only +$6.2B in September ⇒ mostly NOT FHLB, or FHLB-funded from its own liquidity. Open. | `reports/…_Q3_nowcast…` §4 · STATUS H.8 row |

## Folder map

| Path | What |
|---|---|
| `reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md` | **Canonical.** Who borrowed in H1 (district XBRL, named members, borrower-side breadth), the 2020–26 base rate of the >$700B letter. *Moved here 2026-10-10; a forwarding stub sits at the old `AGENTS/REGINALD/reports/` path.* |
| `reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md` | **Canonical.** Q3 advances nowcast from Office of Finance debt (≈ $770B, ±2 sd $728–813B), H.8 vs FHLB gap. *Moved; stub at old path.* |
| `verification/2026-10-10_external_report_verification.md` | Claim-by-claim check of Will's external draft: bottom line + three ledgers (EDGAR, Delaware Life, regulatory/system). |
| `data/KEY_PRIMARY_TABLES.md` | District top-borrower tables (Des Moines, Indianapolis, San Francisco, Chicago), Athene and Delaware Life borrowing room. |
| `data/DESK_ROWS_SNAPSHOT_2026-10-10.md` | COPY: every FHLB row in THRESHOLDS · VX · KB · FLOW · PREDICTIONS · registry NOTES, verbatim, with re-extract commands. |
| `sources/SOURCES.md` | Every primary document: URL or SEC accession, date, local file. |
| `sources/*.pdf` | 17 PDFs (Office of Finance CFRs, GAO, FHFA, FHFA-OIG, Council letter, Iowa code). **Local-only (gitignored here)**; re-download on another machine from SOURCES.md. |
| `sources/FHLB_Risk_Research_Report_Reconciled.docx` (+ `_TEXT.md`) | Will's external draft. **A lead list, not a source** (see verification). |
| `copies/REGINALD/` | 14 copies of desk material: Feb-2026 haircut research and monitoring design, Feb readings, CFG Q1 "FHLB flipped", the frozen FHLB-dependency scoring proposal, the PNC/Pittsburgh attribution (8/23), the WQ-318 per-bank funding baseline + script, BOND's two FHLB packets, my WQ-414 packets to PROME, my 10/10 signal + amendment. |
| `copies/fleet/` | 11 copies from other desks: OTTO (WAL FHLB & liquidity) · OZK (pledged loans) · SHADE (Athene funding mix; BROCK→SHADE Delaware Life packet) · BROCK→HAWK (5/1) · BOND (rotated catalyst rows) · FORGE (PE-insurer cascade, frozen corpus; T-bill/repo) · RED (KRE bull case) · WAL (stale earnings prep) · CORAL (Seacoast funding). |
| `copies/MANIFEST.tsv` | Source path, commit, crc32, bytes and a one-line note per copy. |

## Live surfaces that stay where they are (tools and boot checks read them there)

| Surface | Holds |
|---|---|
| `STATUS.md` §THRESHOLD STATUS: FHLB row, small-bank borrowings row | **the live level** (one source of truth; never restate it here) |
| `registry/THRESHOLDS.tsv` `REG-T-06`, `REG-T-08` · `registry/NOTES.md` | the alarm letters |
| `workbook/VX.tsv` `VX-REG-7.01` (live) · `7.02` / `7.03` (**STALE since 2026-02**) | tracking vectors |
| `workbook/KB.tsv` (17 FHLB rows, ML-REG-009 … 186) | knowledge base |
| `CALENDAR.md` (~10/29 Q3 figure row; weekly funding row) · `ROADMAP.md` (`REG-T-06` thread) | dates and threads |

## Next dates

| Date | What |
|---|---|
| Thu 10/15 · Fri 10/16 | Fed H.4.1 (discount window) · H.8 (small-bank borrowings, week of 10/7): Q5 |
| **Sun 10/11 ruling; result read pending** | **WQ-414 option B approved; REG-T-06 REVIEW encoded.** Independent result read + explicit closeout precede completion; original 10/24 decision deadline is superseded. |
| ~Thu 10/29 (estimate) | Office of Finance Q3 combined advances; grade against the ≈ $770B nowcast (a miss >$40B ⇒ check FHLBank liquidity drawdown) |
| early–mid Nov | FHLBank Q3 10-Qs (top-borrower tables); Athene Q3 10-Q; OF monthly debt file for October |
| 2026-11-05 · 11-07 | FFIEC token expiry (Will) · Q3 Call Report run (per-bank FHLB advances) |

## Known bad figures in older material (do not cite)

- **"FHLB at $480B" (Feb–Apr 2026)**, in `copies/fleet/RED__KRE_BULL_CASE.md` (Pillar 10) and this desk's April WALTER liaison notes. The Office of Finance shows **$694.0B at 3/31/25 and $676.7B at 12/31/25**. The $480B basis is unknown. RED owns its file.
- **The external draft's** San Francisco JPMorgan >10% claim (that was YE2024), "$14.7B credit unions" (matches MBS investments), the Council of FHLBanks quote (fabricated), "Indianapolis most insurer-heavy" (Des Moines is), insurer membership 7.7% (9.7–9.9%), commercial-bank share ~48% (56.4%). Detail → `verification/`.
- `VX-REG-7.02` haircuts and `7.03` pledging: STALE since 2026-02; haircut schedules are not public.

## Not copied: incidental mentions

On 2026-10-10, **138 files in this desk** and **340 elsewhere in the fleet** (excluding `AGENTS/_archive/`) mention the FHLB. Most are one-line references inside bank notes, status rotations or routing logs; they were indexed by command, not copied. List them with (from the repo root):

```
grep -rli 'FHLB\|Federal Home Loan' --include=*.md --include=*.tsv --include=*.py AGENTS PROME FORGE | grep -v 'AGENTS/REGINALD/research/FHLB/'
```

Copy any of them in on request; add a row to `copies/MANIFEST.tsv` with the same banner format.

## Who owns what next door

SHADE: insurer lenders (Athene, Delaware Life; `T-SHADE-01`) · BROCK: private credit and the APO Dec-18 $95P vehicle question · LIQUID: funding plumbing (SOFR−IORB, discount window) · BOND: the curve; its FHLB vectors were shelved 8/18 · WAL / OZK / FLG desks: each bank's own FHLB use.
```
