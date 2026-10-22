# WAL STATUS

**Last Updated: 2026-10-22 12:30 ET — catch-up, L171 frame freeze, desk sweep, court checks, text cleanup, Q3 thesis fold, re-score rule pre-registered, DAEDALUS D:L793 fixes (Will, interactive).** Thesis **v2.4** / EV **$75.96** / PT **$52–76** / weights / composite **13/25** unchanged. The Q3 evidence is now folded into THESIS and WEAKNESSES as a dated, no-re-mark entry (CHANGELOG 2026-10-22). The re-score is deliberately held until the Q3 10-Q, because the $99M appraisal gates Bear-medium. KB **257 rows / 20 groups**.

*Text cleanup 10/22: this file was rewritten with normal spacing and the superseded history paragraphs (10/19–10/21 headers, prior price lines, coordination and closeout receipts) were moved out. The exact prior text is at `archive/STATUS_before-cleanup_2026-10-22.md` (sha256 028d625a…6eff); earlier history at `archive/STATUS_before-Q3-stage1_2026-10-19.md`.*

## BOTTOM LINE (2026-10-22)

Q3 went against the credit bear: no new office problem loans, losses 30bps, reserves 118% of non-paying loans. What is left of the bear rests on **the $99M appraisal**, which the release, deck and call never mentioned, and on the foreclosed-property / early-warning build (OREO +$39M, special mention +$81M). **The Q3 10-Q (EDGAR ≥ Mon 10/26, statutory Mon 11/9) is the one carrier that decides it.** How each 10-Q outcome moves the weights is now **pre-registered** in `Q3_10Q_RESCORE_RULE_2026-10-22.md`: a cure fires the Bear-medium kill (16 → 8); still non-paying or unmentioned trims it 16 → 12; a partial write-down holds 16; a majority loss raises it 16 → 20. Until then v2.4 stands unchanged.

## TODAY (10/22)

| Item | State | Source |
|---|---|---|
| Q3 10-Q | **Not on EDGAR** at 11:10 ET; no new 8-K since 10/19. Effective earliest Mon 10/26; statutory Mon 11/9 | EDGAR CIK 1212545; KB-217 |
| L171 10-Q frame | **FROZEN 10/22**: dated §8 note, no cell changed. Pre-filing anchors: deck Office $272.75M; release classified total $1,091M = nonaccrual $485M + classified accruing $441M + OREO $165M ⇒ 10-Q classified loans expected ~$926M; NCO 30bps; coverage 118.43%; $99M silent in release, deck and call ⇒ graded off the 10-Q, NO-VERDICT if silent, never benign | `Q3_10Q_GRADING_FRAME_2026-09-24.md` §8 |
| Insider filings | Ten 10/19 Form 4s = 10/15 cash-settled RSU vestings at $74.35 (holdings unchanged) + one director DSU grant. No open-market buy or sell; V4 unchanged | KB-252 |
| Sell-side | Stephens PT **$94 → $88**, Overweight kept, on the 11–12% NII guide. **B2, single source** (WALTER SIG-W-20261022-011 citing Investing.com), not independently confirmed; base mismatch vs MarketBeat's 7/23 Stephens $95. An earlier 10/22 line here said "no target changes found"; that was wrong (the signal landed 11:13:52 ET, after this desk's last inbox listing) | KB-253 |
| Cantor / Stupin courts | Remand of WAL's guaranty claims to LA Superior 25STCV24263 **and** stay relief **both GRANTED 8/24**. WAL filed a §523 nondischargeability suit vs the Stupins 9/15 (8:26-ap-01096); the Stupins moved to dismiss 10/16; **hearing Wed 12/9** | `research/2026-10-22_court-checks.md`; KB-254/255 |
| Jefferies / LAM | Jefferies FQ3 10-Q (filed 10/9) never mentions WAL; a second Point Bonita fraud (Radiant/Sapphire, English High Court). NY index numbers still unknown (NYSCEF blocks automation; Will-side browser search offered) | KB-256/257 |
| Comps | ZION (SIG-W-20261021-009), EGBN (SIG-W-20261021-013), HBAN/VLY/SSB (SIG-W-20261022-011) change no WAL cell; REGINALD owns the cohort | — |
| Housekeeping | Desk sweep → `research/2026-10-22_desk-sweep.md`. Inbox and inbox/WALTER empty when re-listed after processing 011; corrections check rc 0 | — |

**Price (10/22 intraday, fetch.py ~11:06 ET): $75.82 (+0.36%)** — SPOT vs EV **−0.18%** (delta/EV 75.96); buffer to 81.90 **+8.02%** (delta/spot). Settled 10/21 close **75.55** (yfinance = Nasdaq, REGINALD 10/22 boot); KRE $71.74 (+1.58%) live. Reaction session (yfinance closes): WAL 10/19 73.63 → 10/20 75.30; KRE 69.26 → 70.62. KB-251/252.

## JUDGMENT

Q3 credit actuals weaken the near-term bear: NCO 30bps, Office classified $272.75M (provisional), coverage 118%. Earnings and capital are mixed: NIM improved, but costs, mortgage, guidance and tangible book need qualification. The $99M appraisal was not identified in the release, deck or call: unknown, not benign. No demonstrated expectations gap. A ledger invalidation is not a silent score change; the post-Q3 re-score waits for the 10-Q.

## Q3 FROZEN-FRAME GRADES

All dollar amounts in millions; SEC EX-99.1/EX-99.2, 8-K acc 0001628280-26-066286. Stage 1 → `research/2026-10-19_Q3_STAGE1_GRADE.md`; Stage 2 (call) → `research/2026-10-21_Q3_STAGE2_CALL_GRADE.md`. Read the reports for basis and qualifiers.

| Leg | Result | Remaining carrier |
|---|---|---|
| **WAL-02**, prior 50% | **INVALIDATED**: company NCO 0.30% = 30bps ≤ 40; 45.8 = gross 48.0 − recoveries 2.2. No Q3 fraud item identified; the 9M exclusions are historical Q1 | TSV Status/Date_Resolved/Outcome written 10/19; **10-Q confirm pending (§2 precedence)** |
| **WAL-01**, prior 25% | **INVALIDATED, PROVISIONAL**: slide 13 explicitly Office 25% × classified 1,091 = **272.75**; ±5.455 rounding band does not include 500 | TSV remains OPEN with a provisional Outcome/Notes; final 10-Q cross-check vs classified loans + OREO |
| Office direction, W4 | 272.75 + 25.7 gross CRE-NOO losses = 298.45 < ~316 at Q2 | Funded Office balance absent; committed 3.1B not interchangeable. No both-falling claim |
| Migration, N=2 | 0 explicitly identified new credits; topic addressed on slides 13/24 and in the call's classified commentary ⇒ **DISCONFIRM DP2 of 3 — FINAL (Stage 2, 10/21)** | RETIRE broadening counter **2 of 3**. SM +81 ("actively migrate to special mention") is early warning, not a §3 count. Not proof that no loan migrated |
| Peaked-NCO guide | **GUIDE HELD**: 45.8 < 55.0 and 30 < 37bps | Printed total result stands |
| $99M letter | **PENDING-10-Q**: not mentioned in release, deck or call (0 hits, two transcripts) | 10-Q frame §4; never C, never reserve-zero |
| Mgmt ~500 NPL basis | 485 nonaccrual printed; call: "485 … exceeding the expectations outlined in our guidance update"; the 567 basis never stated | **NOT-PRINTED ⇒ PENDING-10-Q — final for the print** (management's beat claim recorded, non-gating) |
| Coverage / RETIRE leg | **MET**: issuer 118% ACL/nonaccrual; 574.4 / 485 = 118.43% | Funded 512.8 + unfunded 61.6; 10-Q confirmation |
| Six credits | **MET**, 4 of 6; call: sold outside the bank, no seller financing (Herndon) | Credits 5/6 open at 9/30: one ~completed post-quarter, one scheduled early December; losses unstated. $60M LOI not mentioned |
| Full NPL | 485 + 58 = 543 before the accruing-restructured line | Full total and coverage PENDING-10-Q; guarantees have a separate basis |
| Non-credit falsifier | **NOT TRIGGERED**: 10/20 WAL +2.27%, KRE +1.96%, WAL − KRE +0.30pp | Nothing further graded (§10.2 Step 1) |

N diagnostics: NIM 3.57%, no N1 breach. Total deposit cost (N2) not printed; the 2.76% interest-bearing figure is the wrong basis. TBV 62.22 < 63.24: N3 breach. Lower NII and deposit guide: N4 breach. Raised fee guide and lower expense guide are favorable; loans log only.

## FIVE THINGS THAT MATTER

1. Nonaccrual 562 → 485, but OREO 126 → 165; combined 688 → 650 (−38, versus −77 for nonaccrual alone). Special mention 316 → 397; classified accruing 440 → 441. No cash cure or loan migration is inferred from net stocks.
2. EPS 2.45 vs 2.36; PPNR 419.1 vs 412.4; pretax 339.1 vs 332.0; tax 61.9 vs 63.2. Vendor consensus basis and dates unmatched: no certified beat.
3. NII +10.7, NIM +4bp; mortgage 84.7 → 79.5 (origination 55.7, servicing 23.8). Expense ex-deposit costs 404.1 → 429.7; salary +21.8. The three ECR/referral-line total 234.2 → 223.7; those savings overlap the deposit-expense reduction, so never add them twice. Funding analysis → REGINALD.
4. The Q3 comparative reclassifies customer derivatives/FX into commercial fees: Q2 FV is now 8.3 vs 12.8 in the October 14 screen; net income unchanged. On the new presentation, PPNR less security sale/FV = 401.8 vs 401.1. This is not issuer-adjusted EPS nor the old 8.98 screen; the hedge/persistence bridge is unknown.
5. AOCI −451 → −786; TCE 6,906 → 6,720; TBV 63.24 → 62.22; parent CET1 11.0% → 10.9% (preliminary; CET1 capital $7,389M disclosed). Buyback $92.1M on track but consumes capital. NII guide 12–14% → 11–12%; fees 13–17% → 18–21%; expense 7–11% → 7–10%; deposit growth $6B → $3.5–4B.

**Earnings bridge** (`research/2026-10-19_Q3-recurring-earnings-bridge.md`, KB-245–247): visible-gain-screen pretax 320.7 → 321.8 vs reported 332.0 → 339.1. On a consistent basis the guide midpoint is roughly flat net. The literal ex-deposit cost guide needs Q4 ≤ 405.1 vs 429.7, a 24.6 decline; the call answered Q4 ex-deposit expense −5–7% and the fee guide all-in, Q4 mortgage ~$70M (KB-250). Guide exclusions, cost persistence and MSR cash hedges remain unknown, not a miss. **Full read** (`research/2026-10-19_Q3_FULL_READ.md`, KB-243/244): loan provision 80.8 minus HTM release 0.8 ties consolidated 80.0; loan ACL build 35.0. **Weakness-study contribution** (`research/2026-10-19_broader-bank-stress-context.md`): NCO 30bps, coverage 118%, broadly stable deposits and lower borrowings do not confirm spreading bank stress; SM +81, OREO +39, securities marks and mix costs remain cautions.

## OPERATOR DEPENDENCIES

- **Moreno Valley recorder:** deed-of-trust instrument/APN missing; reCAPTCHA requires Will. His 10/13 response: no results unless REGINALD pulled them; a prior targeted owner search found none. Not re-asked. Ontario B1 does not resolve Moreno Valley.
- **FFIEC:** existing credential verified 10/14 by 8 authenticated historical downloads. No Q3 attempt yet; the prior HTTP 500 is not non-disclosure. JWT expiry 11/5 and the WQ-31 ~11/1 renewal remain; no immediate credential ask.
- **NYSCEF index numbers** (WAL v. Jefferies; Point Bonita v. WAL): Will-side browser search offered 10/22, unanswered.
- **Quartr re-authentication:** needed to check the two B2 call transcripts against issuer audio; no grade depends on it.
- **Broker evidence:** the 10/22 capture is marks-only (quantities unchanged vs 10/19). Identities and quantities → `POSITIONS.md`; reconciliation → PROME/ANVIL (FORGE D82/D84/D74/D83). Will manages his own expiries (USER.md § No expiry nagging, 10/20); this desk books dispositions from his captures and sends no reminders.

## CONVERGENCE MATRIX — scores preserved

| Vector | Score | Current evidence / next carrier |
|---|---|---|
| V1a MI3 | 1/5 | DISCONFIRMED 8/7; CRE not secured by RE, not the Office book. Q3 FFIEC not retrieved |
| V1b broadening | 2/5 | Q2 DISCONFIRMED; Q3 DP2 DISCONFIRM final 10/21 (counter 2 of 3). A data point does not by itself trigger a re-score |
| V1b magnitude | 4/5 | Held as prior judgment, not a fresh confirmation. Q3 NCO guide held; $99M appraisal unresolved; favorable coverage vs OREO/SM rise |
| V2 fraud | 5/5 historical | EXCLUDED from composite. Cantor/legal Q3 details PENDING-10-Q; no implied recovery. Court path 10/22: remand + stay relief granted 8/24, §523 hearing 12/9 |
| V3 NDFI | 3/5 | Q2 exposure/history remain KB-146/168/230. The Q3 deck slide 23 (preliminary, rounded, HFI + HFS + eligible-loan basis) does not grade the 10-Q 25.9%-of-HFI test. Borrower attribution and current stress unknown |
| V4 leadership | 3/5 | Held. 10/19 Form 4s routine (KB-252); no Form 144 sweep; LEADERSHIP.md is 3/31 vintage |

Composite 13/25; weights 2/16/45/30/7 unchanged (THESIS owns them). No independent funding/peer/severity baseline built.

## EXIT RULES

*Kill rail re-derived: 2026-10-22 (against the Q3 print/call grades; the post-10-Q weight mapping is pre-registered in `Q3_10Q_RESCORE_RULE_2026-10-22.md`).*

| Rule | Condition / carrier | State |
|---|---|---|
| Bear-medium KILL | 0 new Office migrations AND benign $99M appraisal; deck/call/10-Q | **NOT FIRED**: leg (a) 0 migrations met at Q3; leg (b) appraisal PENDING-10-Q |
| Bear-fast KILL | MI3 < 25%, FFIEC | **FIRED 8/7**, reflected in v2.4; Q3 untested |
| Bear CONFIRM | WAL-01 Office > 500 or WAL-02 NCO > 40 | **NOT FIRED** on Stage-1 data; 01 provisionally invalid, 02 invalid with 10-Q confirm pending |
| Thesis RETIRE | Broadening disconfirmed 3 times AND coverage > 100% AND benign appraisal | **NOT FIRED**: counter **2 of 3**; coverage leg met 118%; appraisal PENDING-10-Q |
| GATE-REG-T02 (PROME gate) | Close < 78 | **TERMINAL** since 9/1; never re-fire on a sub-78 quote. REGINALD's registry trigger REG-T-02 (same letters, separate object) is carried FIRED by REGINALD |
| Robinhood exit guard | GATE-TERRY-ROLL70-EXIT, official close ≥ 81.90 × 3 | REGINALD's owner log last row 10/13, read 10/19; no fresh count claimed. Contract scope → POSITIONS |

## NEXT CARRIERS

| When | Required work |
|---|---|
| Q3 10-Q (EDGAR ≥ Mon 10/26; statutory Mon 11/9; ledger Resolve_By 11/15) | Run the frozen L171 frame verbatim: subsequent events first; $99M (§4); WAL-01 cross-check; WAL-02 confirm/correct; full NPL; OREO count/valuation; NDFI 25.9% test; Cantor tie-out and legal paragraphs; hotel O1–O8. Carried from the call: Office funded/criticized bridge, NDFI borrowers, total deposit cost, AOCI/CET1 RWA bridge. **Then the post-Q3 re-score, applying `Q3_10Q_RESCORE_RULE_2026-10-22.md` verbatim**, and register forward Q4 predictions |
| Q3 FFIEC, when retrieved (call reports due ~10/30; REGINALD cohort screen due 11/7, D:L180) | MI3 and same-quarter bank NDFI/commitment/modification/mortgage/capital; June/December semiannual fields not expected at Q3. `workbook/MI3_SERIES.tsv` is FROZEN at Q2 — un-freeze or add a successor row |
| **Wed 12/9/2026 11:00 AM** | WAL v. Stupin §523 (8:26-ap-01096): motion-to-dismiss hearing + status conference |
| Mon 11/30/2026 · Tue 1/12/2027 | Makhijani status conference / trial (KB-203) — **not re-verified** 10/22 (RECAP Docs 93–98 have no text) |

## OWNERS / CONTINUITY

**Positions → `POSITIONS.md` only**; no current mark or P&L mirrored here. TERRY's 65P management card supersedes the old note; the December 16 duty is DISCHARGED. The Fidelity 70P does not inherit the Robinhood guard or stop. Funding, peers and severity → REGINALD reports; no repeat study. The DEWEY 10/14 P&A artifact was consumed: a generic template cannot settle named-loan ownership; Ontario branch unchanged, the other three U. **Delivery:** own report + dated root PROME packet; native owner presence/notification/consumption UNKNOWN unless a session confirms it. Exact-path local commits; foreign work requires pull/push deferral. The NEXUS brief is pinned after the final STATUS commit. Frozen frames and SCENARIOS unchanged.
