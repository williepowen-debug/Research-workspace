# WAL — STATUS ARCHIVE (cold half of `STATUS.md`)

**Split out 2026-08-28** under the fleet **read-cap byte budget** (root `CLAUDE.md` §Data Hygiene, Will-approved 2026-08-28 P1: a boot-read-whole surface stays under **32,550 B**). `STATUS.md` measured **59,561 B — 110% of the 54,250 B single-read CAP** and physically overflowed the read tool at the 2026-08-28 boot.

⛔ **VERBATIM. Content is byte-identical to what it was in `STATUS.md`; nothing was rewritten, re-dated, or corrected in the move.** `sha256(first16) = 85ff891cf510e997` over the moved block as extracted.

**What lives here (cold — historical print detail and the event log):** the Q1-2026 print snapshot, the V1/V2/V3 vector detail off the Q1 deck, the MGMT 2026 outlook, the research agenda, AOCI exposure, and the RECENT CHANGES event log.
**What stayed hot in `STATUS.md` (live decision surfaces):** the header, POSITIONS, CATALYSTS, CONVERGENCE MATRIX, EXIT RULES, EXPECTED SIGNALS, BOTTOM LINE.

⚠️ **This is COLD, not FROZEN — it is still true, just not boot-read.** Cite it freely as the Q1-vintage record; it carries no live thresholds. The vectors' CURRENT state is the CONVERGENCE MATRIX in `STATUS.md`, and `THESIS.md` owns the version/EV/PT.

⚠️ **The RECENT CHANGES table below is mis-labelled "rolling 30 days" and runs back to March.** Known since 8/7, carried into the archive deliberately rather than silently relabelled — it is an event log, not a 30-day window.

---

## Q1 2026 PRINT SNAPSHOT (Apr 21 AMC)

| Metric | GAAP | Adjusted | Consensus | Read |
|---|---|---|---|---|
| Diluted EPS | $1.65 | $2.22 | $1.73 | GAAP **miss -4.6%**; Adj **beat +28%** |
| Revenue | $1.018B | — | $948.4M | **beat +7.3%** |
| NIM | 3.54% | — | — | +7bps YoY |
| Total NCOs | $208.5M | $56M ex-fraud | — | 1.45% GAAP / **0.39% ex-fraud** annualized |
| Provision for credit losses | $213.2M | — | — | Driven by LAM (full write of remaining balance) |
| Classified assets / total assets | 1.08% | — | 1.17% Q4 25 | -9bps QoQ (lagging buckets cleaning) |
| 30-89d PD accruing | $157M | — | $108M Q4 25 | **+45% QoQ** (leading building 🔴) |
| Special Mention | $403M | — | $325M Q4 25 | **+24% QoQ** (leading building 🔴) |
| CET1 | 11.0% | — | 11.0% Q4 25 | Steady through provision shock |
| TBV / share | $61.14 | — | — | +13.0% YoY (compounder evidence) |
| Deposits | $82.7B | — | $77.1B Q4 25 | **+$5.6B QoQ (+7.2%) — cohort-leading** |
| Loan-to-deposit | 71.5% | — | 76.0% Q4 25 | De-levering funding side |

**Tape on the print (Apr 22 intraday):** -2.04% to $77.83 — briefly breached $78 threshold. Recovered above $78 from Apr 24 onward; Apr 30 risk-on close $81.54.

---

## V2 FRAUD CONFIRMED — $152.5M Q1 CHARGE-OFF (RESOLVED)

| Credit | Q1 Charge-off | Status |
|---|---|---|
| **LAM** (Leucadia Asset Mgmt = Jefferies subsidiary) | $126.4M | RESOLVED — full write of remaining balance |
| **Cantor Group V** | $26.1M | PARTIALLY RESOLVED — ~$46M residual + $13M senior liens |
| **Total** | **$152.5M** | Mgmt labeled "fraud-related" publicly |

LAM was 70% of total Q1 C&I NCOs ($181.4M). Single-credit charge-off at 21bps of the $59B loan book. **V2 chain produced a regional-bank charge-off visible in 8-K text** — clearest single thesis confirmation any cohort reporter delivered in Q1.

---

## V1 OFFICE CONCENTRATION (Slide 12) — STRENGTHENED

| Category | $ Classified | % of Classified | % of HFI Book | Stress | Disproportion |
|---|---|---|---|---|---|
| **Office** | **$407M** | **38%** | ~4% | **18.5%** | **9.5x** 🔴 |
| C&I | $342M | 32% | 48% | — | 0.7x |
| Construction & Land | $128M | 12% | 7% | 3.1% | 1.7x |
| Other / Resi / CRE Investor non-Office | $193M | 18% | — | 0.36-0.40% | <0.3x |

**$946M of $2.2B Office book matures during 2026 (Slide 23).** 90% Suburban / 10% Midtown / 0% CBD. 20% of book at LTV >70%; **12% at LTV >80% ($264M = equity-thin).**

---

## V3 NDFI / WAREHOUSE — REFINED (Slide 24)

| Sub-vector | Status | Evidence |
|---|---|---|
| Aggregate NDFI | **At cohort median** | 7% Ex-Mtg Credit (peer median 6%, avg 8%) — disconfirmed |
| Lender Finance ($2.3B) | **Structurally protected** | 2,000 obligors / 50+ facilities / no single >$30M / 53% advance rate / 1.9-yr duration |
| CLN reference pool | **Shrinking** | $8.5B → $7.9B YoY (-$600M) |
| Mortgage Warehouse & MSR | **Lone confirming sub-vector** | $7.155B (12% of loans, 30x peer median) — sits in C&I, not NDFI |
| Hotel ($4.5B) | **Latent watch** | 0.40% non-Office classified rate; LTV 53%; not currently stressed |

V3 reduced from "major thesis pillar" to "quality-of-names question on the 2,000 lender-finance obligors." Mortgage warehouse counterparty transmission lands at Apollo Atlas SP, not WAL (`../REGINALD/domain/WAREHOUSE_EXPOSURE.md`).

---

## MGMT 2026 OUTLOOK (Slide 17) — KEY TENSIONS

| Metric | Guide | Q1 Actual | Tension |
|---|---|---|---|
| NCO ex-LAM/Cantor | 25-35bps | **39bps** | 🔴 Above guide top. Q2-Q4 must avg 22-33bps to hold. |
| NII | +11-14% (sans 2 cuts) | tracking | 🟢 Variable-rate book benefits |
| Non-interest income | **+20-25%** (raised from +2-4%) | $252.6M (+97% YoY) | 🟢 Juris real driver |
| Deposit costs | **$650-700M** (raised from $535-585M) | tracking | 🟠 ECR pressure on fewer cuts |

---

## RESEARCH AGENDA — POST-v2

**V1 (Office single-point):**
- [ ] Q1 Call Report MI3 trajectory (May 1-10) — ≥25% confirms V1 acceleration
- [ ] CRE Non-Owner Occupied charge-off composition ($27.7M Q1 = largest in 5 quarters; 5Q TTM 64bps annualized)
- [ ] Office classified detail by property type — of $407M, how much is CBD-adjacent vs suburban?
- [ ] Office maturity schedule by quarter (Q2-Q4 26 breakdown of $946M)

**V2 (Jefferies/MFS — RESOLVED, but follow-ups):**
- [ ] Other Jefferies / Leucadia-era credits inventory — DEF 14A pass + Q&A transcript review
- [ ] Cantor residual recovery posture (~$46M + $13M senior liens)
- [x] V2 chain confirmation — RESOLVED Apr 21 ($152.5M LAM + Cantor)
- [x] Jefferies Q1 transmission — RESOLVED Mar 25 (JEF EPS $0.70 vs $0.91, $17M MFS losses, V2 confirmed at JEF P&L)

**V3 (NDFI/Warehouse — refined):**
- [ ] Lender Finance fund-level concentration (top 10 fund exposures, default rates) — resolves remaining quality-of-names question
- [ ] Mortgage Warehouse counterparty list — verify Apollo Atlas SP exclusion stands
- [x] NDFI cohort comparison — RESOLVED via Slide 24 (cohort median)
- [x] CLN pool size trend — RESOLVED via Slide 13 ($600M YoY shrinkage)

**Macro / cross-channel:**
- [ ] Hotel sub-portfolio NCO trajectory ($4.5B latent — Q2-Q3 migration watch)
- [ ] Updated insider filings — any Form 4s post-print
- [ ] Investor Day May 12 thesis-vector response

---

## AOCI EXPOSURE

Cat III/IV mandatory unrealized AFS loss recognition phasing in. Same AOCI dynamic as OZK — separate capital drain from credit losses, two simultaneous bleeds. Comment period closes **Jun 18**. Industry aggregate $49.5B hit across 21 banks.

---

## RECENT CHANGES (rolling 30 days)

*⚠️ Table is mis-labelled — it says "rolling 30 days" but the body runs back to March. Flagged 8/7, not restructured this session (out of scope); treat it as a rolling **event log**, not a 30-day window.*

| Date | Event |
|---|---|
| **Aug 23** | **SESSION #4 — PROME-orchestrated bounded touch (two-tier wave 3). Mechanical before creative, and it found two live errors on this file.** ★ **① The Aug-21 $77.5P write-back: SOLD 8/18, NOT lapsed.** Determined from this desk's own records first (POSITIONS.md + `FORGE/STATUS.md` D-18 + Will's in-session word via TERRY) rather than from the packet that prompted it. **P&L UNRECORDED, not zero** → *DISPOSITION RESOLVED / P&L UNRESOLVED, pending broker export.* **REGINALD's tape-grade of LAPSED rebutted and returned** — his arithmetic was right ($79.67 close ⇒ 2.72% OTM) and answered the wrong question; a tape read cannot see a sale it has no visibility of (root rule #4). ★ **② Two stale figures killed on this very file:** the **“SIX consecutive down sessions”** claim (refuted by PROME/TERRY on **8/20**, sat live here for 3 days — the truth is **FOUR**, 8/17→8/20, and the run **ended Friday** on a **+0.66%** close) and the **Price-discipline exit-rule cell reading “🟢 $83.11, buffer +$5.11”** — a **July-vintage** figure that survived every session since, sitting ~100 lines below a header calling the buffer the tightest in the record. **Both are the same class: a derived cell nobody re-reads because the headline above it is fresh** (`finding_header_edit_is_the_edit_most_mistaken_for_maintenance`). ③ Inbox **3 → 0**. ④ Four-fossil sweep executed under the amended root retirement rule — **3 archived, EARNINGS_PREP HELD** (fails the rule: `CLAUDE.md`, a live protocol doc, classes it a frozen calibration record). ⑤ EARNINGS_PREP banner rider **filed as NEW text** — the 8/20 wording is unrecoverable and was deliberately **not** reconstructed. **Zero thesis/threshold/probability/score moves; no trade action; nothing Will-gated touched.** |
| **Aug 20** (2) | **LIVE NEWS SWEEP + CORE-FILE SWEEP.** ★ **Clean negative: NOTHING in the 8/13-8/20 window explains the grind to the period low** — no 8-K since 7/30, no analyst action after late-July, no litigation development, no company release, **and not the cohort** (KRE +0.03% vs WAL −0.44% same session). Name-specific, no identified catalyst, buffer **+2.6%** — tightest in the record. ★ **Substantive find: WAL is EXPANDING CRE and CRE-adjacent private credit** — Urban Standard Capital facility grown to **$200M** across 3 funds (from $40M in 2020) for **TRANSITIONAL CRE**, borrower estimates ~$800M of lending power [Commercial Observer 8/4, **B2**]; institutional CRE origination team build-out incl. **office**, construction/bridge/mini-perm nationwide [Businesswire **6/22** — a secondary aggregator mis-dated this to August; verified before logging]. **Third independent line against V3's downgrade rationale; NOT score-moving on B2/B3.** KB 177→180 |
| **Aug 20** | **★★ v2.4 SHIPPED + THE FULL 8/12 WILL-RULED BATCH EXECUTED (session #3, 13d dark).** Bear-fast **10%→2%** on its own falsifier's disconfirmation; **bear-medium HELD 16%** (the freed weight was NOT laundered into the other bear); Base 45 / Bull 30; **EV $73.92→$75.96, PT $52-76**; ⛔ **total bear 26%→18%, it FELL.** ★ **Overvaluation 12.4%→5.4% — margin of safety nearly closed**, and now two-sided (EV +$2.04 AND price −$3.06). ⚠️ **Sep-18 cores sit BELOW EV** ($67.5P −$8.46, $70P −$5.96) → routed TERRY/Will, not actioned. Spec repairs **P2/P3/P4/P8/P9** in a separate R3-compliant edit. **REG-15 encoded + scored RESOLVED-FAILED** (orphaned 7d in the row-43 seam). **POSITIONS.md phantom fixed** ($77.5P carried LIVE 2d past Will's sold-confirm, 1d before expiry). **EDGAR sweep 8/7→8/20:** no 8-K since 7/30, no new 144, 9 Form 4s = 100% RSU mechanic (zero code-P); ★ **T. Rowe −20.8% → 5.8%, Invesco RE-CROSSED +12.5% → 5.4%** (both event-dated 6/30, verified NOT the Vanguard-restructuring class); implied shares out **−1.7%** = buyback-consistent |
| **Aug 7** | **Q2 10-Q PRIMARY READ (UNFRAMED)** — filing landed 7/31 into a dark period → **frame leg VOID, recorded not patched**. Six tie-outs run; **NDFI grew to 25.9% of HFI, refuting KB-WAL-121 and V3's downgrade rationale**; **v2.3.1 does NOT fire**; WAL-01 bucket question **widened to three candidates** with no 10-Q instrument; Jefferies **countersuit NOT disclosed**, complaint **amended May-26** with 3 new causes; OREO office property count **15→22**. KB 145→**163**. 8-K 7/30 (routine div $0.42) + two 7/31 13Gs (**Vanguard entity restructuring, not accumulation**) read. **Zero moves — 6 proposals to Will/PROME.** → `Q2_10Q_READ_2026-08-07.md` |
| **May 11 PM** | **Tape broke $78 threshold — close $76.95 (-6.04%).** First sub-$78 close since Apr 22-23. Whole regional cohort red (VIX +6.92%). Investor Day prep file `INVESTOR_DAY_PREP_2026-05-12.md` shipped — 5-bucket listening framework + pre-registered decision tree. WALTER SIG-W-20260511-023 confirms V2.1 leading-vs-lagging framing from lagging side. |
| May 11 AM | V2.0 → V2.1 ship post RED CHG-RED-025 OVER-CORRECTED. M2 + M4 full accept; M1/M3/M5/M6 partial. V1 weight restored pending MI3 mid-May; Bear split into Bear-fast 12% + Bear-slow 23%; Jun-conditional EV table; $65P Jun close-rec WITHDRAWN → HOLD-or-ROLL-TO-SEP. |
| **May 1** | THESIS v2.0 released — "compounder with concentrated CRE tail risk" framing supersedes v1 "fast-transmission failure." `CHANGELOG.md` created. |
| Apr 30 | Risk-on tape close $81.54 (+2.35%). Holds above $78 threshold. |
| Apr 24 | Round 2 deep-mine — deck + press release synthesis files in `sources/q1_2026/` (~1,200 lines). Slide 12 Office single-point reading corrected to 38% / 9.5x disproportion. Slide 23 $946M maturity wall surfaced. Slide 24 NDFI cohort-median finding closes V3 outlier framing. |
| Apr 22 | Round 1 analysis (`Q1_2026_ANALYSIS.md`) — V2 fraud labeled in 8-K. Tape -2.04% to $77.83 intraday (briefly breached $78). |
| **Apr 21** | **Q1 2026 print AMC** — V2 RESOLVED in 8-K: LAM $126.4M + Cantor $26.1M = $152.5M charge-off. Mgmt-labeled "fraud-related." GAAP EPS $1.65 (miss); Adj $2.22 (beat). $50.5M security-sales gain absorbed LAM charge. |
| Mar 31 | `LEADERSHIP.md` complete — CFO Idnani (JPM FIG, 20yr MD) profile, board risk additions Dec 2025 (Clarke Starnes III ex-Truist CRO), Guggenheim on Risk not Audit. |
| Mar 26 | Analyst downgrades: Weiss Buy→Hold; Barclays PT $105→$90; WFC PT $83→$79. |
| Mar 25 | JEF Q1: EPS $0.70 vs $0.91 (-23%); $17M MFS losses; SMFG walked back. V2 chain confirmed at JEF P&L (4 weeks before WAL Q1 print delivered the regional-bank-side confirmation). |

---



---

## SESSION-HEADER NARRATIVE (moved from `STATUS.md` preamble, 2026-08-28)

**Why moved:** the `STATUS.md` header had grown to **15,485 B — 48% of the entire 32,550 B read-cap budget** for a dashboard header. The *state* lines (price, thesis, KB counts, boot block) stayed hot in `STATUS.md`; the per-session NARRATIVE moved here. ⛔ **VERBATIM, `sha256(first16) = a088662c983d83f7`.** The canonical home for session narrative is `MEMORY.md` (handoff) and `CHANGELOG.md` (thesis moves) — this is the header's own copy, preserved rather than deleted.

**Last Updated:** 2026-08-28 (**WAL session #5** — Will-directed file sweep: *"anything dated, stale, broken, incomplete."* ★ **① THE TAPE RE-BASED AND THE BUFFER IS NOW THE TIGHTEST IN THE RECORD** — last official close **$78.71 [Thu 8/27, −1.12%]**, gap **$0.71 = −0.90% required move (Δ÷close) / +0.91% above the line (Δ÷threshold)**; ★★ **8/27 BREACHED $78 INTRADAY to $77.13**, deepest since 5/11, and 8/25 touched **$78.00 exactly** — **recorded here for the first time; neither fires the CLOSE-based rule.** `$79.67 / +$1.67 / −2.10% / +2.14% / 4.9% / "~2% away"` are all DEAD. ② **A dated peer read-across nearly expired unnoticed: OZK's IQHQ RaDD Aug-2026 maturity** sits in this file's EXPECTED SIGNALS and is cited 4× in `THESIS.md` at weighted EL ~$140M — **its window closes Mon 8/31 and WAL had never written what it would DO with either outcome.** Now instrumented. ③ **KB integrity: the 8/20 MI3 sweep killed `KB-WAL-001` and left its three dependents ACTIVE** — `-002` ($2.73B MI3 amount = a 12/31/25 value; 6/30/26 is $2.55B, −6.4%), `-003` and `-007` (True-CRE ~59% / **CRE-Tier1 474%, a regulatory-red-line claim**), all 120d past their own `Stale_By` and all derived from the superseded figure. ④ **Five broken refs repointed** — every one a 7/25 promotion residue pointing at REGINALD paths; **34 days silently dead**, two of them 8/13 REGINALD files this desk cites in THESIS and had never read. **Zero thesis/probability/weight moves; no trade action.** Prior: 2026-08-23 (**WAL session #4** — PROME-orchestrated bounded touch, two-tier wave 3. **WAL session #4** — PROME-orchestrated bounded touch, two-tier wave 3. ★ **① THE Aug-21 $77.5P WRITE-BACK: disposition = SOLD 2026-08-18, NOT lapsed** — three sessions before its own expiry, on Will's in-session word (artifact `FORGE/STATUS.md` **D-18**); **P&L still UNRECORDED, not zero**, pending broker-export confirm. REGINALD's 8/23 tape-grade of *LAPSED* **rebutted at the artifact and returned**; the 2.72%-OTM figure is recorded as a **counterfactual**, not this leg's outcome. ② **Tape re-based to the Fri 8/21 close $79.67 (+0.66%)** — the down-run **BROKE at four** (8/17–8/20), and the **“six consecutive down sessions” claim this file carried is REFUTED and swept** (PROME/TERRY 8/20 packet: 8/14 printed **+0.71%**). Threshold distance re-derived from the named close per the `REG-T-02` kill-on-sight rule. ③ Inbox drained **3 → 0**; ④ four-fossil sweep executed under the amended root retirement rule (Will-ruled 8/21) — **3 archived, EARNINGS_PREP HELD with its reason**; ⑤ EARNINGS_PREP banner rider **filed** (new text, self-authored — the 8/20 wording is unrecoverable and was NOT reconstructed). **Zero thesis/threshold/probability/score moves; no trade action.** Prior: 2026-08-20 (**WAL session #3** — 13-day dark-period catch-up + the full 8/12 Will-ruled batch EXECUTED. ★★ **① v2.4 SHIPPED**: MI3's disconfirmation re-marked — **bear-fast 10%→2%**, freed 8pp to Base 45/Bull 30, **bear-medium HELD 16**; **EV $73.92→$75.96, PT $52-76**; ⛔ **anti-ratchet verified, total bear 26%→18% (FELL)**; ★ **overvaluation 12.4%→5.4% — the margin of safety is nearly closed**, and the Sep-18 cores now sit BELOW EV ($67.5P by $8.46, $70P by $5.96 — routed to TERRY/Will, not actioned). ② **Spec-repair pass P2/P3/P4/P8/P9** — WAL-01 re-instrumented off the VOID 'Schedule O' cite to the Q3 deck slide + a NO-VERDICT band; WAL-02 invalidation repaired to an exhaustive Q3-only partition; **v2.3.1 REJECTED** (leg (a) moot, leg (b) a one-way ratchet); MI3 basis SPLIT-RULED; v2.1 implication column RETIRED. Zero weights moved in that edit (rider R3). ③ **REG-15 ENCODED + SCORED RESOLVED-FAILED** — the row-43 transfer was orphaned 7 days, owned by nobody; basis fork closed on the row's own 'Memo3/C&I' wording. ④ **POSITIONS.md phantom fixed** — Aug-21 $77.5P was carried LIVE 2 days past Will's 8/18 sold-confirm, 1 day before expiry. ⑤ **EDGAR catch-up**: no 8-K since 7/30, no new Form 144; 9 Form 4s = 100% the monthly RSU mechanic (zero code-P, zero discretionary); ★ **two REAL 5%-holder 13Gs — T. Rowe −20.8% to 5.8%, Invesco RE-CROSSED +12.5% to 5.4%**; implied shares out −1.7% (buyback-consistent). Prior: 2026-08-07 (**WAL session #2**, PROME-directed spawn — TWO deliverables. ★★ **① V1a MI3 RAN FOR THE FIRST TIME EVER** after Will cleared the FFIEC CDR blocker same day: **Q1-26 23.88% · Q2-26 21.20%**, both in the frozen `<24%` **PLATEAUED** band → **bear-fast KILL FIRED**, **~Sep 1 time-box DISSOLVED**; 12-quarter series shows MI3 **never reached 25% in any quarter** → `MI3_FIRST_RUN_2026-08-07.md`. **10% weight NOT re-allocated — v2.4 proposal P7, Will-gated.** ② **Q2 10-Q PRIMARY READ, UNFRAMED**: filing landed **7/31**, a week before the ~Aug 7-10 window, into a 13-day dark period → **the pre-registration frame leg is EXPIRED-UNWRITTEN / VOID**, no backdated frame written. Six tie-outs run [2 resolved · 2 partial · 2 not resolvable]; **v2.3.1 condition evaluated → DOES NOT FIRE**; 8-K + two 13Gs read. **KB 145→170.** Zero threshold/probability/score moves beyond the two pre-registered MI3 exit-rule outcomes. Full read → `Q2_10Q_READ_2026-08-07.md`. Prior: 7/25 **WAL session #1** — first solo session post-promotion: Q2 KB ingest [22 rows, 105→127] + standup handles RATIFIED/RE-SCORED. Prior: 7/22 Q2 Stage-2 post-call, REG-24/25 → 25%/50%, W5 letter (B) FINAL, grades → `../REGINALD/reports/2026-07-21_WAL_Q2_grade.md` + `../REGINALD/reports/2026-07-22_WAL_Q2_stage2_grade.md`)) | **Thesis:** **v2.4 (8/20 — MI3-disconfirmation re-mark: Bear-fast 2, Bear-med 16 HELD, Base 45, Bull 30, Tail 7; EV $75.96, PT $52-76, overvaluation 5.4%; total bear 18%)** *(prior v2.3 7/25: Bear-med 16, EV $73.92, PT $52-74, overvaluation 12.4%)* "Concentrated CRE Tail Risk Actualizing on Q2 Timeline" (`THESIS.md` **v2.4**, `SCENARIOS.md` **v2.4** — see its 7/17 position-truth banner, `CHANGELOG.md`, drill findings `../REGINALD/research/WAL_10Q_DRILL_2026-05-21.md`)
**Price:** **$78.71** (**2026-08-27 CLOSE**, **−1.12%** — the last OFFICIAL close; today 8/28 is still trading. `scripts/market.py` → Yahoo `WAL`, regular-session close, pulled 2026-08-28 13:58 ET) | **Threshold:** $78 | **Buffer:** **+$0.71 — TIGHTEST IN THE RECORD** — ⛔ **state the basis, never a bare percent** (`REG-T-02` kill-on-sight, `../REGINALD/registry/NOTES.md`): **−0.90% is the move WAL must MAKE from $78.71** (Δ÷close, and the owner registry's canonical figure); **+0.91% is how far $78.71 sits ABOVE $78** (Δ÷threshold). ⚠️ **DEAD FIGURES — do not carry forward: “$79.67 / +$1.67 / −2.10% / +2.14%” (8/21 close, killed 8/28); “~2% away”; “+2.6%” (8/20 intraday); “+1.47%” (8/20 close); “2.00%” (never correct).** ⚠️ **LIVE INTRADAY IS NOT A CLOSE:** WAL printed **$78.34 at 13:58 ET on 8/28** (gap $0.34 = −0.43% required move / +0.44% above the line) — recorded as an intraday print ONLY, because this desk has already been burned once by writing a 14:4x pull as if it were the close (8/20, the close came in $0.90 lower). **Today's close is not yet knowable.** ★ **THE WEEK 8/24→8/27 — no close has breached, but the tape is SITTING on the line:** 8/24 **$78.39** (−1.61%, low $78.18) · 8/25 **$79.63** (+1.58%, low **$78.00 exactly**) · 8/26 **$79.60** (−0.04%) · 8/27 **$78.71** (−1.12%, low **$77.13**). ★★ **8/27 BREACHED $78 INTRADAY BY $0.87 — the deepest breach since 2026-05-11, and it is recorded here for the first time.** Three of four sessions had lows at-or-below $78.18. ⚠️ **Still no identified catalyst** (no 8-K since 7/30 as of the 8/20 sweep; the 8/20→8/28 window is **UNSWEPT** — do not read "no catalyst" as verified for it). **It is now MOSTLY but not purely name-specific:** 8/21→8/27 WAL **−1.21%** vs KRE −0.68%, ZION −0.34%, OZK +0.04%, **EGBN −2.20%** — real cohort softness with WAL at the weak end at ~2× KRE, but WAL is not the worst name; the **$77.13 intraday is WAL-only** (KRE did nothing like it), as is today's −0.55% vs KRE −0.09% at 12:43 ET. ⛔ **A CLOSE below $78 FIRES the threshold → signal REGINALD + PROME 🔴, and it fires REGARDLESS OF EV** (the model says the Sep-18 cores expire worthless at EV $75.96; both are true and neither resolves the other). **Per `PROME/GATES.tsv` GATE-REG-T02 + the owner registry, `REG-T-02` was re-graded UN-FIRED at the 8/21 close and NO close since has fired it, so the next sub-$78 close is still the FIRST FIRE OF A NEW CYCLE (no duplicate-suppression). REGINALD owns the gate and grades it at the close; WAL owns the position context.** **Overvaluation at the 8/27 close: 3.62%** (EV $75.96 vs $78.71; was 4.9% at the 8/21 close).
**Status:** 🔴 SHORT THESIS ACTIVE + B1 + B3 FIRED + V4 — 10-Q subsequent-event disclosed $99M life-science office sponsor walk-away (late April, previously *pass* → substandard/non-accrual). Same strategic-default mechanic as IQHQ (OZK). Chief Banking Officer Stephen Curley (head of National Business Lines) resigned same week. Market reacted ~10% on 5/11-5/15 (Simply Wall St 5/14). **REG-24 25% / REG-25 50% / REG-26 RESOLVED-DISCONFIRMED 7/21** (Stage-2 re-grade 7/22 post-call — canonical `workbook/PREDICTIONS.tsv`; Q2 verdict NOT-surprise-tier, W5 letter (B) FINAL — $99M in nonaccrual $0 charged off, brought CURRENT end-June, appraisal pending; grind INTACT-but-NARROWED). **v2.3 (7/25 — ⛔ SUPERSEDED by v2.4 on 2026-08-20; this cell read “CURRENT” for 3 days after the bump, struck 8/23):** post-Q2 re-mark — Bear-medium 25→**16**, Bear-fast 12→10, Base 35→40, Bull 27; EV $68.93 → **$73.92**; PT **$52-74**; Base/Bull ranges lifted $74-82/$86-94; **overvaluation 18.8%→12.4%, margin of safety COMPRESSED**. *(Prior* **v2.2.1 (6/8 AM), superseded:** *Bear-medium 30→25 on loss-absorption channel only (macro-NIM tailwind softening: 20Y clean + Waller pivot); EV $67.98 → $68.93; PT $50-68.)* **Cohort NCO decomp (6/8 PM) → Hyp A genuine cohort improvement** — WAL bear now idiosyncratic, "sharpen to WAL-specific" EARNED; Bear-medium stays 25 (no revert); positions/PT/predictions UNCHANGED (`../REGINALD/research/COHORT_NCO_DECOMP_2026-06-08.md`). **V2 inventory test CLEAN** (10-Q has only LAM + Cantor V; WAL escalated to active litigation against Jefferies parent in NY Supreme Court Mar 2026). **V3 NDFI cohort-median CONFIRMED via 10-Q breakout** ($14.93B / 25.2% of HFI). ★★ **V1a MI3 PRIMARY FALSIFIER HAS NOW RUN (8/7) — AND IT DISCONFIRMS.** Q1-26 **23.88%** / Q2-26 **21.20%**, both <25% → **bear-fast KILL FIRED**; the 24.2% baseline reproduces exactly (12/31/25 = 24.24%) so the basis is identical. **12 quarters show MI3 never once reached 25%.** ⚠️ **V1a ≠ V1** — MI3 is CRE *not secured by real estate*; the $99M, the office book and the appraisal are in the **secured** book and are untouched. v2.1 calibration table graded as frozen, then preserved. Q2 print **Tue Jul 21 AMC** (confirmed 7/9; grading frame pre-registered → `Q2_GRADING_FRAME_2026-07-21.md`) is the binary second-data-point test (one Office migration or many?).
> ### ✅ RAISE WITH WILL AT BOOT — **BLOCK CLEARED 2026-08-20. Nothing is waiting on Will.**
> **All three blockers were RULED by Will in-session 2026-08-12** (batch — `PROME/proposals/2026-08-12_rule-batch-RULED.md`, WILL_QUEUE rows 32b/42/43) **and all three are now EXECUTED by WAL session #3 on 2026-08-20.** Struck here per the boot-block rule that a cleared blocker must not rot into background noise — the *record* lives in `CHANGELOG.md` (v2.4 + the spec-repair entry), not in this block.
> ~~**1c** bear-fast's 10% weight (P7)~~ ✅ **EXECUTED — v2.4, 10%→2%, total bear 26%→18% (FELL, anti-ratchet satisfied).** ~~**2** the two prediction-spec defects (P2/P3)~~ ✅ **EXECUTED — WAL-01 re-instrumented, WAL-02 partition made exhaustive.** ~~**3** ratify-or-reject v2.3.1 (P4)~~ ✅ **EXECUTED — REJECTED, retired not repaired.** *(Also cleared same session: P8 MI3 basis split-ruled · P9 v2.1 implication column retired · REG-15 encoded+scored · fence-② ruled.)*
>
> ⏱ **ONE dated item survives, and it is NOT actionable today: the FFIEC PWS JWT expires 2026-11-05.** Regeneration is a **Will action** via his PWS login; it is already on `PROME/WILL_QUEUE.md` row 31 (the ~Nov 1 credential sitting). **It lands INSIDE the Q3 10-Q window (10/24-11/10)**, so a lapse would re-dark MI3 exactly when the Q3 re-test is due. **Raise it at boot from ~mid-October, not before.**
> ✅ **CORRECTED 2026-08-20 — the machine direction in the prior block was BACKWARDS.** It read *"the desktop box has no credentials yet."* The opposite is true: FFIEC creds are **present and verified on the DESKTOP (`DESKTOP-BC6EF81`)** and **MISSING on the LAPTOP (`WilliePOwen`)** — `PROME/MACHINE_LOCAL.md` carries a same-day 8/7 correction note saying its own first write had the boxes backwards, and this surface inherited the pre-correction version and never got the fix. **MI3 is DESKTOP-only, and this session is on the desktop, so MI3 is runnable now.**

**KB:** ⏱ *[SUPERSEDED as a live figure, PRESERVED as history — scope-stamped 2026-09-02: an AS-AT-2026-08-28 snapshot and correct as history. Live count is **187 rows / 20 distinct Group values** — `STATUS.md` owns it. ⛔ Do NOT re-date this cell: re-dating a figure inside an archived snapshot rewrites the record, which is the defect, not the fix. The "16 groups" token was ALREADY wrong when archived — measured 20 on 9/2.]* **183 rows / 16 groups** (**8/28 session #5: rows 181-183** — the 15-days-late integration of REGINALD's 8/13 MI3 cohort re-run, which `THESIS.md` had been citing by a BROKEN path: WAL is **#1 of 14 on the legacy v1 basis (21.20%) and #3 on the uniform v1a basis (8.99%)** because WAL's item-9 book is **57.6% of its own base**, the highest in the cohort; ★ **the two-desk item-9 fork — WAL 9.17% vs REGINALD 8.99% — RAISED AND RULED THE SAME DAY, IN WAL'S FAVOUR:** REGINALD (owner of the cross-bank surface) ruled **v1a = MI3 ÷ (item 4 + item 9.a)**, dropping 9.b, on empirical grounds — at OZK he found `RCONPV09` **≡** `RCON2746` to the dollar across 6 of 6 quarters, so **MI3 IS a 9.a mirror**, not a distribution. **WAL's 9.17% stands as ruled-canonical.** ⚠️ **But the cohort RANK is now UNVERIFIED, not merely stale** — all 14 ratios recompute upward by each bank's own 9.b size, so EGBN and MTB move too; **do not cite "#3 of 14" until his 11/07 refresh.** ⛔ **No re-grade at either desk** — the bear-fast KILL fires on the v1 basis it was registered against; and MI3 **dollars +14% YoY** while the ratio fell. **Also re-marked: KB-WAL-002/-003/-007 ACTIVE → SUPERSEDED**, the three dependents the 8/20 MI3 sweep missed. Prior **8/20 session #3: rows 171-180** — EDGAR dark-period sweep [two REAL 5%-holder 13Gs: T. Rowe −20.8%→5.8%, Invesco re-crossed +12.5%→5.4%; implied shares −1.7%; Aug insider sweep zero-signal; dividend; Jefferies countersuit re-verified no-change] + **first-ever NDFI nonaccrual $122.5M** + live-news-sweep rows [Urban Standard CRE private-credit facility →$200M; institutional CRE build-out; ★ clean negative on the tape]. **KB-WAL-001 and -127 flipped to SUPERSEDED** in the core-file sweep. Prior 8/7: ★★ **MI3 first-ever run, rows 164-170** + **Q2 10-Q primary read, rows 146-163** — acc 0001628280-26-051418 + 8-K 7/30 + two 13Gs 7/31; data clock 13d→0d · 7/25: Q2 cycle 106-127 off 8-K acc 0001628280-26-049001 · insider sweep 128-133 · news sweep 134-139 · Q1 10-Q primary 140-145; per `KB_INDEX.md`) | **Consensus:** Mod Buy (cohort median) | **Assets:** **$98.7B** (6/30/26 10-Q; was carried as "~$90B+")



---

## BOTTOM-LINE SESSION HISTORY (moved from `STATUS.md`, 2026-08-28)

*"What session #1 changed (7/25)" and "What session #2 changed (8/7)" — per-session narrative that had accumulated inside the live BOTTOM LINE. ⛔ **VERBATIM, `sha256(first16) = 67df28f01f2e01f4`.** The BOTTOM LINE's CURRENT read stayed hot in `STATUS.md`; only the retrospectives moved.*

**What session #2 changed (8/7) — a falsifier finally ran, a grading leg was lost, and a convergence rationale was refuted:**
0. ★★ **THE BIG ONE: V1a MI3 ran for the first time in the thesis's life, and it disconfirmed.** Will cleared the FFIEC CDR blocker the same day; the pull returned **both** available quarters plus 10 of history. **Q1-26 23.88% · Q2-26 21.20% — concordant, both in the frozen `<24%` PLATEAUED band → bear-fast KILL FIRED and the ~Sep 1 time-box DISSOLVED.** The 24.2% baseline reproduced exactly (12/31/25 = 24.24%), so the grade sits on the identical basis to the number the thesis was built on. ★ **The 12-quarter series then reframed the question entirely: MI3 has NEVER reached 25% — all-time high 24.24%, never within 76bps of its own trigger — and since 2025Q1 it oscillates with no trend.** The "growing from 15.5%, fastest in cohort" premise was a two-endpoint artifact spanning **six** quarters that the thesis recorded as **two**. **The 10% weight was NOT re-allocated** (un-pre-registered; the frozen implication column is v2.1-vintage and would raise total bear on a disconfirmation) → **v2.4 proposal P7.** ⚠️ **V1a ≠ V1 — the secured office book is untouched by this.**
1. ⛔ **A grading leg was lost, and is recorded as lost.** The Q2 10-Q filed **7/31**, seven days before the expected window opened, into a 13-day dark period. The frame owed as mandate ★1 was never written, so the leg is **EXPIRED-UNWRITTEN / VOID** — no backdated frame, no graded Q2-10-Q outcome, ever. The deadline lived only in `MEMORY.md` `NEXT SESSION`, a surface that is worthless if no session boots; **a frame owed against an externally-scheduled filing needs an instrument that fires without a WAL session.**
2. ★ **The best catch: V3's downgrade rationale does not survive the primary.** NDFI reached **25.9% of HFI — a new high** — with **all three sub-lines growing QoQ** and PE funds (the "de-emphasised" line) growing **fastest at +15.6%**. The 7/25 cut to 1/5 rested on a call-sourced "shrinking" claim the filing contradicts. **The score was NOT moved** — it goes to Will as proposal P1.
3. ⚖️ **The v2.3.1 condition was evaluated and does NOT fire** — and leg (a) turned out **unfalsifiable as written**, the third instance of a WAL rule naming an instrument that cannot carry its datum (after MI3-is-not-a-10-Q-line and the non-existent "Schedule O").
4. ⚠️ **WAL-01 got worse, not better.** The tie-out meant to *resolve* the bucket question **widened** it — three candidate buckets, no 10-Q that publishes office-classified at all, and a void half-spec.
5. **Zero threshold, probability, score and prediction-spec moves.** Everything decision-shaped left as a proposal (P1-P6).

**What session #1 changed (7/25):** the narrative "everything funnels to Q3" was **wrong on timing** — the nearest forward event is the **Q2 10-Q ~Aug 7-10**, which carries three owed tie-outs and was absent from both the catalyst and expected-signals tables; and the **~Aug FFIEC window** now carries an armed **time-box** that forces a bear-fast disposition call ~Sep 1 rather than letting a fourth quarter pass on an untestable premise. Separately, the seeded convergence matrix collapsed two mechanisms moving in opposite directions into one score: **broadening died (2/5) while realization on the known tail strengthened (4/5, on a new 5-quarter-high $32.0M CRE-NOO charge-off)** — the split is now explicit so no cross-agent reader takes "the bear mostly died" from a single number. Live-bear composite restated **13/25** (the seeded 15/25 double-counted V2's closed arc).



---

## CATALYSTS — RESOLVED/PAST ROWS (moved from `STATUS.md`, 2026-08-28)

*The struck-through past-event rows from §CATALYSTS. The section's own header already said **"past events ✅, forward only below the line"** — this move finally makes that true. ⛔ **VERBATIM, `sha256(first16) = f95c8386ecab9a44`.** Several carry hard-won grading records (the VOID Q2-10-Q frame leg, the MI3 first run, the $77.5P sold-not-lapsed disposition) — **cite them as the calibration record; none carries a live threshold.***

| Date | Event | What it tested |
|---|---|---|
| ~~May 1-10~~ | Q1 Call Report filings (FFIEC) | ✅ PASSED WITHOUT INTEGRATION — MI3 test (≥25%) still un-run, FFIEC PDD overdue (ROADMAP thread) |
| ~~May 12~~ ✅ | WAL Investor Day | Findings shipped `INVESTOR_DAY_FINDINGS_2026-05-12.md` (E=B3 FIRED; Q&A hunt still open) |
| ~~Jun 18~~ ✅ | $85P + $65P expiry; AOCI comment closed | All Jun-18 cleared per Will 6/19; capital-rules final rule pending |
| ~~Jul 17~~ ✅ | Jul-17 $65P expiry | Lapsed OTM at $81.88 (broker-confirm owed) |
| ~~Tue Jul 21 AMC~~ ✅ | **Q2 print** (call Wed 7/22 noon) | ✅ GRADED in two stages off the frozen frame. NOT-surprise-tier, NO FIRE. REG-26 DISCONFIRMED; W5 letter **(B)** FINAL; WAL-01/02 → 25%/50% |
| ~~🟠 ~Aug 7-10~~ **FILED Fri Jul 31** ✅ | **Q2 10-Q** (acc 0001628280-26-051418) | ⛔ **FRAME LEG = EXPIRED-UNWRITTEN → VOID.** The filing landed **7 days before the expected window opened**, into a 13-day dark period (no WAL commit 7/25→8/7). The pre-registration frame owed as MEMORY mandate ★1 was **never written**, so per WAL's own ratified principle — ***"a frame written after the filing is not a frame"*** — **no backdated frame was written and no graded Q2-10-Q outcome exists or ever will.** ✅ **Read UNFRAMED 8/7 instead:** six tie-outs → **(a) RESOLVED, refutes KB-WAL-121** · (b) PARTIAL · **(c) EPS leg RESOLVED A1, consensus leg structurally unresolvable** · **(d) NOT RESOLVED, ambiguity WIDER** · **(e) RESOLVED AS A NEGATIVE** · (f) NOT RESOLVABLE. Full → `Q2_10Q_READ_2026-08-07.md` |
| ~~7/30~~ ✅ | 8-K acc 0001628280-26-051146 | Routine: common div **$0.42** (pay 8/27, record 8/13) + preferred Series A. **Flat QoQ, +10.5% YoY.** Materiality NIL (KB-WAL-161) |
| ~~7/31~~ ✅ | Two SCHEDULE 13Gs | ★ **NOT accumulation** — a **Vanguard legal-entity restructuring** (two newly-CIK'd LLCs, 5.01% + 5.02%, same signatory/day, event date 6/30, passive 13d-1(b)). ⚠️ **Do NOT add the two percentages** — overlapping affiliates named in both (KB-WAL-160) |
| ~~🔴 ~Aug (Q2 window)~~ ✅ **RUN 2026-08-07** | **FFIEC Q2 Call Report PDD** | ✅ **V1a MI3 FIRST-EVER TEST EXECUTED — DISCONFIRMING.** Q1-26 **23.88%** · Q2-26 **21.20%**, both <25% → **bear-fast KILL FIRED**, **~Sep 1 time-box DISSOLVED**. Blocker cleared by Will same day (CDR account registered 8/7). **Now a standing quarterly pull** — next: Q3-2026 Call Report ~Oct-Nov |
| ~~Fri Aug 21~~ ✅ **DISPOSITIONED 8/23** | **Aug-21 $77.5P ×1 expiry date** | ⛔ **Did NOT resolve as an expiry — the leg was SOLD 2026-08-18**, three sessions earlier, on Will's in-session word (`FORGE/STATUS.md` **D-18**; canonical `POSITIONS.md`). ⚠️ **P&L UNRECORDED, not zero** — date + proceeds pending the next broker export (ANVIL). *Counterfactual for the record only: WAL closed **$79.67 [8/21]**, so a held $77.5P finishes **2.72% OTM**.* Peer tape-grade of *LAPSED* rebutted |

---

## ROTATED FROM `STATUS.md` 2026-09-02 (WAL session #6) — CONVERGENCE MATRIX rationale

**Verbatim, unedited. `sha256(first16) = e6f7bfb0b3557920`.** Rotated under the read-cap byte budget (`scripts/read_cap_check.py --agent WAL`); STATUS was at 32,850 B against a 32,550 B budget. **COLD, not frozen and not retracted** — the V1b split it argues for is live in STATUS §CONVERGENCE MATRIX and the composite is unchanged at 11/25.

**★ Why the split matters (the substantive change this pass makes):** the seeded single "V1b — Office migration @ 2/5" conflated two mechanisms that moved in **opposite directions** at Q2, and THESIS v2.3 itself separates them — *"the bear's broadening mechanism is disconfirmed for Q2; its magnitude mechanism is deferred, not dead."* A single 2/5 reads as "the bear mostly died," which is wrong: broadening died (2), realization on the known tail got **stronger** (4, on a new 5-quarter-high charge-off). Any cross-agent reader of a one-line composite would have taken the wrong signal. *Not additive with THESIS weights — this is the lossy cross-agent comparison handle, not a probability.*
