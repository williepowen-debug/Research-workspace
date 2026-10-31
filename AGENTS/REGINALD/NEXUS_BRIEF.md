# REGINALD — NEXUS Brief

**Status:** Concentrated bank risk. HY tightened to 314bp [10/28] without REG-T-04 ever firing (peak 340); the widening was BANK-ABSENT and has partly reversed. The 10-year (~5.0%), not HY, moves regionals. Q3: problem loans up at 7 of 10 names (the signal kept); falling reserve coverage DROPPED as a predictor on DEWEY's base rate (L801, 10/30); the Florida books hold on every read cell. WAL's Q3 10-Q (10/30) confirms NCO 0.30%, no fraud: the WAL-source stand-down leg is NOT FIRED, final for Q3.
**Domain:** Regional-bank comparison, FHLB advances, hidden CRE and sponsor-bank balance-sheet risk.
**As of:** 2026-10-31 09:38 ET, PROME-spawned L857 (FFIEC Q3 borrowing short list) | STATUS commit: a7d9d76ea

## CROSS-DOMAIN

**October31 L857** (`reports/2026-10-31_L857/REPORT.md`):
- **Who borrowed in Q3 (FFIEC Call Reports, 134 of the 139 banks holding 75% of Q2 small-bank borrowings):** the frozen small universe, excluding probable acquirers, **cut borrowing −$5.70B net while deposits rose +$39.20B**. Among these banks more borrowing was repaid than added (51 of 127 increased); the frozen concentration verdict is still ungraded. Santander absorbed Webster on 8/20, so its +$10.70B is mostly inherited (pro forma +$6.72B, deposits up).
- **6 frozen-rule flags, all funding-mix shifts at the issuer:** Regions (commercial balances moved to off-balance-sheet products), Renasant (public-fund outflow, loan growth), Simmons (brokered → FHLB), The Bancorp (secured lines fund fintech loan growth; BaaS sponsor), Bank of Hawaii (public-fund runoff), Israel Discount NY (private). **No TERRY route:** the concentration verdict needs the FDIC posting (~mid/late Nov). LIQUID context only.
- **No score, threshold or probability change.** 4 banks unfiled (East West, HSBC USA, First Hawaiian, Beacon).

**October30 L801** (`reports/2026-10-30_L801/REPORT.md`):
- **Coverage-decline leg DROPPED as a predictor** (weight zero, descriptive only). DEWEY: problem loans up AND coverage down preceded a ≥25bp charge-off jump within 4 quarters in **2 of 10 episodes vs 25% of all quarters**; in 2007–10 coverage change did not sort later losses (ρ −0.06) once the problem-loan rise was counted. ⚠️ ~3 loss cycles; CECL makes today's coverage look safer than history; 'collateral covers it' has a poor record at failed banks.
- **Problem-loan leg KEPT** (7 of 10 up [10/23]; 2007–10 ρ +0.46). Coverage becomes a question about loans called safe on collateral: FLG $1,571M carries no allowance and its exits are now 87.5% payoff/disposition, 1.6% cure (FLG desk roll-forward). Graded by loss on exit at the FLG 10-Q (~Nov 6–9). No peer base rate for cure share exists (Y-14Q, non-public).
- **No score, threshold or probability change.** The matrix coverage POINT (a level) stays frozen until the 11/07 S1-vs-S2 test. Q3 Call Reports not yet at FDIC (0 rows 10/30 09:09 ET). HY 314 [10/28], CCC/HY 4.16× on the denominator.

**October28 catch-up** (`reports/2026-10-28_boot/REPORT.md`, commit `db025d223`):
- **HY / REG-T-04 (DOCKET L818): NOT FIRED.** 338 → 330 → 318 [10/23–10/27]; BB and B lead the tightening, so no transmission widening. CCC/HY 4.15× rises on the denominator: no escalation (LIQUID owns re-entry).
- **SBCF Q3:** FL 8-K cell HOLDS (criticized+classified 2.90% vs ≥3.20%); NPL −15%; an $8.4M reserve on one acquired loan is unexplained. **FL frame: no cell transmits at any of the four names; aggregate PROVISIONAL to the 10-Qs (~11/14).** CORAL consumes.
- **Funding (LIQUID context):** small-bank borrowings $316.4B SA [w/e 10/14], **+11.8% in 6 weeks** (97.5th pct since 2010) from a low level (4.55% of assets, 18th pct). It mostly funds loan growth; ~3/4 of new deposits are core money. Not a run. Raw Q3 change is only +$4.3B (Q3 normally falls ~3.5%), and the late-September rebound (+10.4%) is second only to 2022. No KRE forward edge, and the aggregate 'borrowing up, deposits down' pattern has **no track record** (13 episodes since 1985; the same evening's 'watch deposits' advice is retracted). The per-bank screen is FROZEN for the FDIC Q3 posting (~mid/late Nov) → `reports/2026-10-28_small-bank-borrowing-deep-dive.md` §10–§13.
- **BaaS (CARL):** Coastal holds ~$447M of Bluevine deposits [9/25] ≈ 9% of its deposits, leaving in 1H27 when Valley closes. Funding, not credit. CARL's WQ-228 join fields accepted.
- **Nano (L516):** P&A still unposted; DEWEY found no passive route tonight. FDIC-R held the Ontario lien as of 10/2 (one loan). An FDIC inquiry needs Will and is not recommended.
- **FLG:** a director bought 10,000 shares at $10.14 on 10/27 (Form 4). Ladder RED, −28.8%.
- **Correction:** CFG $12.852B is March 31, not June 30 (BROCK). My 10/21 row was wrong; KB ML-REG-251.


**October23 afternoon (Will):**
- **Learning review** (`reports/2026-10-23_historical-learning-review.md`): method improved, judgment unproven.
- **REG-08 and REG-10 regraded FAILED → CONFIRMED**, originals kept (`5e0e8b301`; PROME DOCKET L824). REGINALD Brier 0.162 (n = 8): too few to show skill.
- **11/07 ranking test frozen** (retrospective, not blind). The matrix coverage point is now labelled an untested indicator; scores unchanged.
- **REG-T-04 single-issuer disclosure rider** (WQ-512, `8452f2af7`): CSC/Optimum is 0.47% of HYG.
- **TERRY:** the rate prop on KRE is the last 4 weeks only; the proposed alarms show no forward edge since 2006 (`9938ffae5`).

**October23 catch-up** (`reports/2026-10-23_boot/REPORT.md`, commit `c6bb09ab0`):
- **HY / REG-T-04 (PROME ask, packet `012e5c08c`, consumed by PROME at `c3600e8ed`):** 340bp [10/22], run 0 of 3; earliest fire 10/27 close. Broad repricing ⇒ the bank lane shows as **drawn balances** (C&I, NDFI lender/fund finance), not regional credit losses. ⚠️ Issuance: earlier 'freeze under way on volume' WITHDRAWN (corrected 10/23 eve on DEWEY `AGENTS/DEWEY/output/2026-10-23_hy-issuance-window-october.md`): narrowed and expensive, not shown shut; the lock-out is on price at CCC. Will added a single-issuer attribution rider to REG-T-04 (CSC/Optimum).
- **10-year falsifier:** KRE −0.72% per +10bp 10-year vs +0.02% per +10bp HY (corr −0.36 / +0.07; R² 0.13, weak). A falling 10-year falsifies a regional-bank put; a wide HY print does not confirm one. In `TRADE.md` §4 for TERRY's cards.
- **FLG Q3:** missed; 0 of 4 readable CRE 'weakens if' lines met (NAL $2,817M, RR criticized $4,402M, loss ratio 20.7%), criticized +$670M; FLG stays #1. FLG desk owns the print grade.
- **AMTB:** FL frame HOLDS final. **CUBI:** WQ-318 INCONCLUSIVE; fund finance +$456M, its top grower (NDFI lane, BROCK).
- **FL aggregate:** AMTB HOLDS final, SSB HOLDS provisional, BKU HOLDS-PENDING-P, SBCF prints 10/27 — still PROVISIONAL (CORAL consumes).

**October22 catch-up** (`reports/2026-10-22_catchup/REPORT.md`, commit `6e3914cb2`):
- **Will's HY question (SIG-W-20261022-005):** BANK-ABSENT 9/21→10/20. The October leg is CCC-only (+112bp, BB −2bp). Bank pref basket −2.0% vs PFF −3.9% (dividend-adjusted); KRE −1.9% vs KBWB −5.7%.
- **Routes:** ① NDFI is BROCK's; ② CMBS is CREED's, UNKNOWN (not launched, WQ-478).
- **Q3 at primary:**
  - SSB clean; REG-27 at 0.57% is not met, row OPEN.
  - VLY early flag strengthens: CRE reserves released again; construction nonaccrual 9.1→39.3M.
  - EGBN Prince George's $56.0M → nonaccrual, re-extended to 12/21/26, no cash.
  - BKU CRE criticized −$53.9M. HBAN NCO 0.31%. ZION NCO 0.02%, rank 1 unchanged.
- **FL frame:** SSB HOLDS provisional, BKU HOLDS-PENDING-P; aggregate UNKNOWN.
- **H.4.1 descriptive lines:** >~12.9B / >~15.7B. Not registered.

**New predictions (Will-approved 10/22):** REG-28 EGBN 4Q maturities stay bank-held (65%) · REG-29 ≥4 of 6 banks' Q4 NCO above Q3 (45%, tests the appraisal-refresh recognition read) · REG-30 VLY non-accrual ≥$511.4M (60%). Resolve-by dates are 10-K deadlines (Mar 2027).

**Communication fixes (Will-approved, D:L793, 10/22):** REGINALD is now the obliged consumer of the OZK and WAL pair channels (WQ-484), with an ACK at each boot and boot.py listing unACKed entries. NOT-FIRED trade ideas route to TERRY. Exit rail re-derived. **CREED (launched 12:19)** answered Will's CRE leg: a rate shock, not credit; CMBS spreads flat through 10/16. Bank side stays BANK-ABSENT.

**Appraisal-discount cohort test (Will, 10/22):** `reports/2026-10-22_appraisal-discount_cohort_test.md`. 12/14 banks publish no discount-to-appraisal; realized resolution haircuts run ~13–22%. Extensions still trigger re-appraisal, so Q4–Q1 appraisal-driven write-downs are likely. FLG ties H1 MF/CRE charge-offs of $193M to 'appraisals received'. EGBN: no trade from this desk.

**EGBN Q4 wall (Will, 10/22):** `reports/2026-10-22_EGBN_Q4_maturity_wall.md`. ~$525M matures 10/27–12/30 ($146.9M criticized + $378.6M pass). The criticized-four gross loss is ~$8–31M (≤$1.02 of the $38.00 TBV/share). Q3 behaviour was extend-not-exit. ⚠️ The DC $20.5M appraisal was printed at $24.5M (Q2) and $13.5M (Q3) with the same date.

**AI-agent banking doc (Will):** `reports/2026-10-22_AI-agent-banking-doc_analysis.md`. Deposit run-speed / margin story, not credit. The doc is AI-generated and secondary-heavy; VLY "acquired Bluevine" is wrong (the deal is pending).

**Startup October21:** two WALTER owner relays (001 funding correction,003 Boston outcome) read and disposed INFO_ONLY; correction receipted. No new research grade or route. Boot limits→`reports/2026-10-21_boot/RECEIPT.md`.

**Audit October21:** three general packets integrated. Approved REG-27 encoded OPEN at15% before SSB release, original20 prediction rows preserved. OZK coupon correction applied. Remaining Q3/research/document debt→`reports/2026-10-21_owed-items/REPORT.md`; audit completion does not clear that work.

**SENDING — prior routes retain their dates; new packets committed, consumption unverified:**

| To | Signal | Priority | Mechanism |
|----|--------|----------|-----------|
| PROME | 10/28 catch-up memo: L818 NOT FIRED, L516 unposted, FL frame provisional (`db025d223`) | 🟠 | Memo + report; no trade, no gate move |
| CARL · ISHM · DEWEY | WQ-228 joins accepted (`a6caf49aa`) · C&I boundary (`1500962a7`) · FHA/VA pointer + Nano ask (`228cfa31a`; DEWEY answered `41c72f558`) | 🟡 | CARL/ISHM liveness UNKNOWN; packets committed |
| PROME | 10/23 REG-T-04 bank-lane reading + 10-year falsifier (`012e5c08c`); PROME filed it as consumed on L818 (`c3600e8ed`) | 🟠 | Asks (1)–(2); no trade, no gate move |
| PROME | 10/22 catch-up packet (`6e3914cb2`) + forum post (`db50f620c`); PROME acknowledged receipt by message | 🟠 | 005 answer, GATE-REG-27, D:L521, HBAN/ZION reads |
| PROME · OZK | October21 audit packets (`1d84633ca`), consumption unverified | 🟡 | Approved prediction encode, stale coordinator obligations with delivery evidence, coupon consumer carries; no new score or trade |
| PROME · OZK · WAL · WALTER | October20 backlog report and dated inbox packets | 🟠 | Primary Boston failed sale/foreclosure; weekly funding partly reverses; secondary WAL external-disposal evidence. No owner grade changed or recipient read asserted |
| PROME + FLG | `VX-REG-6.03` RED on the 10/7 close (sent `018af9846`); ladder exhausted | 🟠 | Registered routing; matrix unchanged |
| PROME | WQ-318 delivered (`a033c799c`) + memo; register CFG 10/16 / CUBI grading rows | 🟠 | Report + KB ML-REG-176..180 |
| TERRY | WAL Q3 LOCKED Mon 10/19 AMC (`fe37dd785`); `TRY-COND-KREADD` REGINALD arm NOT met (`db3565b15`) | 🟠 | Packets; cards are TERRY's |
| WALTER → OZK | OZK closed below the OZK desk's <$45 band 10/6 + 10/7 (signal lane, `db3565b15`) | 🟡 | OZK grades its own band |
| BROCK | BRK-31 grading input at Q3/Q4 prints — *I am the data source* | 🟠 | PC/NDFI-attributable reserve builds |
| SHADE · BROCK · PROME | 10/11 insurer handoffs + CFG read-note (WQ-419) | 🟠 | PROME accepted 9451933aa/c7f945a95; peer reads unverified; Citizens current draw unknown |
| PROME · LIQUID · BOND · WALTER | WQ-414 REVIEW encode `236a091d4`; result + ruling/interface packets | 🟠 | Independent acceptance `1b937462e`; recipient consumption unverified; peer gates unchanged |
| WALTER → LIQUID | Small-bank borrowings +11.7% in 3 wks to 9/30 (signal lane, `e1fc74154`) | 🟠 | Descriptive bar, not a registered trigger |
| PROME | WQ-414 prior nowcast evidence (`047ef11d4`), now governed by approved REVIEW | 🟠 | Official quarterly count only; debt nowcast excluded |
| WALTER → LIQUID | AMENDMENT to the signal: SVB scale (+$290B in one week) + FHLB debt +$6.2B in Sep (`b680ef50d`) | 🟠 | Routed WITH the original as `SIG-W-20261010-007` (WALTER `40b424536`; LIQUID action) |
| DAEDALUS | H2 as-made receipt complete, 20 rows (`28c7dd7dd`) | 🟡 | For its 10/12 sitting |
| PROME · RED | WQ-412 named SSB "State Street" (`8d31de2aa`; PROME fixed `3780a92d6`) · RED's KRE bull case cites FHLB "$480B" vs OF $676.7B/$810.7B (`b9ca8d708`) | 🟡 | Corrections; owners edit their own files |

**WAITING FOR:**

| From | Input | Expected by | Why it matters / change in view |
|---|---|---|---|
| WAL / OZK / FLG owners and existing issuer disclosures | Q3 outcomes, exact funding inputs and loan recovery/recognition | Existing CALENDAR windows | REGINALD owns cross-bank comparison; specialist judgments remain theirs. OZK primary Q3 consumed here; call/filing remain pending. WAL call SECONDARY consumed; exact F3/N pending. |
| EGBN existing disclosures | Cash, concessions, new funding, retained exposure and incremental recognition for four cases | Existing Q3 read | A disappearing category or extension is not demonstrated repayment; no independent property match yet. |
| Existing Fed releases / REGINALD | Does small-bank borrowing persist after the October14 high? | H.4.1 October29 / H.8 October30 | Prior releases read; latest small-bank borrowing partly reverses with deposits up. No new registered monitor |
| FDIC | Nano P&A; absent at October28 22:28 ET (page Last Updated 10/19) | Weekly re-check from November3 (L516) | Re-run forensics on actual schedules; January20,2027 bar date; no external send without Will. |
| PROME / Will | REG-27 shared registration / existing WQ-454.REGT06 ruling | SSB print /before October30 respectively | REG-27 encoded under approved A; PROME shared GATES record pending consumption. REG-07 VOID. REG-T-06 publication basis alone remains Will-owned; as-written CFR governs. |
| Will / existing FFIEC run | JWT renewal; cohort-selection/completeness | November5 renewal /November7 planned retrieval | Missing bank capable of flipping breadth → UNKNOWN; no silent cohort expansion. |
| Will / PROME / TERRY | Existing contract ownership/card evidence at FORGE D-74/D-77; structural source→POSITIONS | Existing records only | Broker holdings are not research/trade approval; disposition remains unknown without broker evidence. No expiry reminder. |

## VIEW

- Severity remains concentrated rather than tier-wide; current scores/method→STATUS and BANK_EXPOSURE_MATRIX. CRE-specific shortlist and formal instrument ranking are different questions. Only two transmission channels are locally instrumented; upstream channels remain owner-held.
- October20 OZK Boston sale failed: $37.3M charge-off and $132M retained property; loan-stock decline is not cash cleanup. WAL call supplies management-reported external disposals without seller financing (SECONDARY, unnamed loans). Both funding/nonbank grades remain INCONCLUSIVE. Sources and original expectation outcomes→`reports/2026-10-20_backlog-followthrough.md`.
- Eagle's four cash outcomes are UNKNOWN. No independently matched borrower/property payoff; July restructuring/storage-payoff expectations are SECONDARY. Q1 appraisal tables conflict; not a quantified-loss conclusion. Source/access limits→`research/EGBN/README.md`.
- M&T reported income covers recognized provisions, not independently demonstrated complete economic losses or earnings collectibility. Distributions/book rebuilding constrain retention earlier; sustainable earnings/current consensus/vendor EPS basis and valuation edge remain unresolved. → October20 M&T report.
- June compound-risk, securities-duration and funding work are dated baselines, not current bank clearance. Missing durations at WAL/FLG/VLY, joint capital/loss model and pricing edge remain unresolved. Property recovery, new expense, retained exposure and regulatory capital must be matched, not added indiscriminately.
- FHLB totals do not name troubled borrowers or prove regional-bank funding stress. REG-T-06 is REVIEW under WQ-414; official quarterly level and both qualified breadth measures govern. A debt nowcast cannot grade an official count; nonpositive growth has no contribution percentage. Procedure→registry/NOTES.md. Latest weekly small-bank borrowing partly reverses on SA/NSA bases while deposits rise and cash falls. Primary-credit borrowing rises separately; no named-bank/FHLB attribution. Revision bridge and source basis in October20 follow-through.
- Historical composition discriminator survives: thinner allowance coverage can mean new problem loans or allowances consumed by realized cleanup, with opposite implications. GSE delinquency improvement through modification is not cure; pair it with provision direction. Tariff guard: C&I utilization across 301 since7/24 and338 Canada since8/19 carries artifacts in both directions. UWM bank-side work stays within WQ-318, not a new thread; Florida residential undertone retains its small-base qualification in prior evidence.

## CALIBRATION

- **Conviction (decomposed):** direction-H on the *concentration* shape (5 independent confirmations; cross-bank Q2 CRE bad-loan rate FELL 2.46% → 2.23%; WQ-318 adds: funding not breaking at 6/30) · timing-M (resolvers: the 10/16–10/27 prints, then the 11/07 Call Report run) · level — **current threshold distances and dated observations→STATUS §THRESHOLD STATUS; WAL remains FIRED, HY CREDIT-CANARY-FIRED with BANK-ABSENT cross-check, FLG RED.** June figures do not clear October funding/capital; no demonstrated joint valuation edge.
- **Diverge from market by:** less than at any point this year, and honestly so — the narrowing was driven by my own grades, not the tape. Where I still diverge: the market reads benign GSE MF headlines and clean small-tier prints at face value; I carry both as composition-masked (modification suppression; definitional NPA exclusions at BKU).
- **Uncertain about:** (1) **whether the bank-equity leg is now running AHEAD of credit** (HY half-retraced while KRE/FLG/OZK kept falling) — a non-credit repricing my instruments cannot see, or credit about to re-widen into the prints; (2) whether CFG's +$3.85B Q2 FHLB draw is brokered substitution (INFERENCE) or funding pressure; (3) magnitude attributable to OZK news (owner found Oct6 short-bridge disclosure; Oct12 executed-extension primary now consumed, causal share unmeasured); (4) the MI3 cohort-selection rule, decide before 11/07; (5) **whether the latest partial borrowing reversal persists; FHLB-specific attribution remains unknown and the latest H.8 does not show deposits leaving.**
- **Failure patterns to mind:** a detector that exists only as a TSV cell has no lag guarantee — the FLG band-1 break sat 8 days, the band-2 break was caught at the first boot (zero lag) once `vx_ladder_check.py` existed (census every other frozen-baseline band into it); a broker chart's last print at the bell is not the vendor close (WAL $75.21 vs $75.76 on 9/29 — grade the settled bar, label the other); a correction to my figure gets the same recompute as the figure (lesson 40).


**Calibration vintage:** prior conviction/divergence frame retained; weekly-funding uncertainty updated with the latest outcome. No re-estimated probability, specialist prior or valuation edge. Current levels are dated in STATUS; eligible exit log caught up through October20, state unchanged. Pre-open stock quotes datedOctober20, settled WAL/KRE independently matched; credit observations stillOctober19. No fresh bank-transmission attribution.

## NEXT DECISION POINT

Use existing Q3 disclosures to append outcomes to original expectations under BANK_RESEARCH_STANDARD. Current issuer dates/status→CALENDAR; exact unresolved inputs→MEMORY NEXT SESSION and October20 catch-up. Next: Eagle October21/22 named-loan outcomes, OZK October21 call and later filings; WAL filing-only F3/N. Weekly funding and eligible settled-bar catch-up completed here. §0 judgment moves only on L180 BROADER or FL-rail TRANSMISSION; approved REG-27 now OPEN15%, with no numerical breadth cutoff or new monitor. REG-T-06 official publication basis remains Will-owned; REG-27 approval is executed, shared registration carrier remains PROME-owned. Original modal INCONCLUSIVE expectation and CUBI/CFG falsifiers remain in the archived original, not retroactively re-written.

## WATCH (next 2–6 weeks)

| Existing event | Date owner | Test / boundary |
|---|---|---|
| Bank Q3 releases/calls/filings and FL frame | CALENDAR issuer-confirmed table | L35/L521/L520/L170; WQ-318 rows, CRE weakens-if lines, AMTB non-CRE and FL frozen frame/A3. No grade inferred from elapsed time. |
| Settled exit log and FRED tier test | Existing daily cadence | Exit count→registry/REG_T02_EXIT_LOG.tsv; no unsettled bars or missing-data-as-holiday. REG-T-03 already fired, evaluate follow-through/exit rather than restart. |
| Nano P&A /RED and CARL reviews | CALENDAR /MEMORY | October27 P&A; October23 CET1/AOCI; October26 fintech join. Existing obligations, no completion inferred. |
| FHLB official publication and borrower disclosures | CALENDAR /registry NOTES /WILL_QUEUE | Highlights October30 versus CFR November13 remains the existing instrument discrepancy. Official count only; both breadth measures before escalation. |
| FFIEC Q3 run and later QBP | CALENDAR | Renewal/cohort choice before existing November7 run; completeness checked at retrieval, later QBP remains dated. |

**Preservation:** Original contiguous blocks B01–B06 → `archive/2026-10-20_organisation-cleanup_NEXUS_BRIEF.md`; exact source-line/section map and verified CRCs → `reports/2026-10-20_organisation-cleanup/RECEIPT.md`. Re-check size at any append or on 2026-11-20, whichever first.
**Cleanup:** PROME accepted the charter review and registered the boot reads (`55cfb3982`). Grading-frame pointer restored; both handoff dependencies closed. Cleanup itself changed no economic observation or trade. Current research refresh→October20 backlog report. Acceptance→`reports/2026-10-20_organisation-cleanup/ACCEPTANCE.md`. WALTER retains its historical BOARD size remedy.
