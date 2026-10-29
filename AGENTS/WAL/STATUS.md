# WAL STATUS

**Last Updated: 2026-10-28 ~23:15 ET — catch-up and data refresh (Will, interactive): no 10-Q yet, Q3 Call Report not yet filed, KB expiry review, short interest, EDGAR sweep, First Eagle NDFI joinder, inbox drain.** Thesis **v2.4** / EV **$75.96** / PT **$52–76** / weights / composite **13/25** unchanged; nothing graded since 10/22. KB **260 rows / 20 groups**.

*The 10/22 version of this file is preserved verbatim at `archive/STATUS_before-10-28_2026-10-28.md` (sha256 59f568d3…daca9); earlier history at `archive/STATUS_before-cleanup_2026-10-22.md` and `archive/STATUS_before-Q3-stage1_2026-10-19.md`.*

## BOTTOM LINE (2026-10-28)

Nothing has graded since 10/22. Q3 went against the credit bear: no new office problem loans, losses 30bps, reserves 118% of non-paying loans. What is left of the bear rests on **the $99M appraisal**, which the release, deck and call never mentioned, and on the foreclosed-property / early-warning build (OREO +$39M, special mention +$81M). **The Q3 10-Q is still not on EDGAR (checked 10/28 ~22:40 ET; statutory Mon 11/9) and is the one carrier that decides it.** How each 10-Q outcome moves the weights is **pre-registered** in `Q3_10Q_RESCORE_RULE_2026-10-22.md`: a cure fires the Bear-medium kill (16 → 8); still non-paying or unmentioned trims it 16 → 12; a partial write-down holds 16; a majority loss raises it 16 → 20. The Q3 Call Report (MI3, bank-level NDFI) is not filed yet either: due Fri 10/30, and the FFIEC token expires Thu 11/5. Until then v2.4 stands unchanged.

## LATEST (10/28)

| Item | State | Source |
|---|---|---|
| Q3 10-Q | **Not on EDGAR** at ~22:40 ET 10/28: issuer filings since 9/24 are only the 10/19 8-K and ten 10/19 Form 4s. Statutory Mon 11/9; ledger Resolve_By 11/15 | KB-259; `sources/edgar_sweep_2026-10-28/SWEEP_RECEIPT.md` |
| L171 10-Q frame | **FROZEN 10/22**, unchanged: Office $272.75M; classified $1,091M = nonaccrual $485M + classified accruing $441M + OREO $165M ⇒ 10-Q classified loans expected ~$926M; NCO 30bps; coverage 118.43%; $99M graded off the 10-Q, NO-VERDICT if silent, never benign | `Q3_10Q_GRADING_FRAME_2026-09-24.md` §8 |
| Q3 Call Report (FFIEC) | **Not yet filed**: FFIEC's list of banks that have filed for 9/30 since 10/1 has 2,643 entries and RSSD 3138146 is absent; the 9/30 facsimile returns HTTP 500. The credential works on the laptop (6/30 control re-pull byte-identical). Due Fri 10/30; JWT expires Thu 11/5 | SWEEP_RECEIPT; `workbook/MI3_SERIES.tsv` attention line |
| NDFI (V3) | **First Eagle Private Credit Fund SPV**, 4th amendment dated 10/1 (8-K 10/5): Western Alliance Bank joins as a lender with a **$100M commitment**. The second private-credit SPV joinder in two weeks after Crestline 9/18 (KB-195), the first with WAL's own amount disclosed. A commitment, not a funded balance; exposure direction, not stress; no score change (the 10-Q NDFI table decides) | KB-260 |
| Insider / ownership | 9/24 → 10/28: no Form 144 (newest 6/15), no 13D/G, no open-market buy or sell; the 10/19 Form 4s are routine RSU settlements (KB-252). V4 unchanged | KB-259 |
| Short interest | FINRA 10/15 settlement **6.35M shares (+2.15%)**, the third straight rise (+12.45% since 8/29); days-to-cover 4.68 on higher volume. Dated observation; no squeeze or score read | KB-258 |
| Sell-side | Stephens PT $94 → $88 (10/22, B2 single source, unconfirmed) — no newer item found | KB-253 |
| Courts | Cantor remand + stay relief granted 8/24; WAL §523 suit vs the Stupins, motion-to-dismiss hearing **Wed 12/9**. Makhijani 11/30 / 1/12/2027 dates still **not re-verified**: CourtListener now refuses anonymous access (API 401, search 403; DEWEY saw the same 10/28) | `research/2026-10-22_court-checks.md`; KB-203/254/255 |
| Jefferies / LAM | Unchanged since 10/22 (Jefferies FQ3 10-Q silent on WAL; NY index numbers unknown) | KB-256/257 |
| Housekeeping | KB expiry: all 9 expired rows judged one by one (223–226 superseded post-print; 193/229 superseded by 259/258; 228/246/247 extended with reasons). Inbox: DEWEY ×2 (info) and DAEDALUS WQ-508 (already applied to the charter 10/23 by `d3488e641`; reviewed, not contested) filed to processed. Corrections check rc 0 | KB.tsv header |

**Price (10/28 close, fetch.py/yfinance pulled 22:36 ET; not Nasdaq-cross-checked): $75.96 (−0.58%)** — SPOT vs EV **0.00%** (delta/EV 75.96); buffer to 81.90 **+7.82%** (delta/spot). KRE $72.11 (−0.65%). Settled closes in REGINALD's exit log (Yahoo = Nasdaq): 10/23 76.12 · 10/26 75.44 · 10/27 76.40 (`../REGINALD/registry/REG_T02_EXIT_LOG.tsv`, read 10/28).

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

- **Moreno Valley recorder:** deed-of-trust instrument/APN missing. His 10/13 response: no results unless REGINALD pulled them; a prior targeted owner search found none. Not re-asked. Ontario B1 does not resolve Moreno Valley. DEWEY 10/28 tested all four lien counties: every route is human-only (San Bernardino reCAPTCHA; Riverside public but scripted submissions fail; Los Angeles/Bellflower has no online index); exact searches in `../DEWEY/output/2026-10-28_nano-loans-passive-records-route.md` §2.
- **FFIEC:** credential re-verified on the laptop 10/28 (6/30 control byte-identical). Q3 not filed yet (deadline Fri 10/30). The JWT expires Thu 11/5, so the pull must land 10/30–11/5 or after the WQ-31 renewal (Sun 11/1 sitting). No new ask.
- **NYSCEF index numbers** (WAL v. Jefferies; Point Bonita v. WAL): Will-side browser search offered 10/22, unanswered.
- **Quartr is a subscription gate, not a re-authentication:** on 10/28 the connector was signed in as Will but refused with "Quartr Pro subscription required" (plan: none). Quartr is a paid source Will already DECLINED (WQ-220, preserved in the WQ-298 paid-data ruling), so this item is closed, not owed: the two B2 call transcripts stay B2, and no grade depends on them.
- **CourtListener:** anonymous API and search now refused (401/403, 10/28). The Makhijani dates need a token, DEWEY's PACER route, or a browser check; not urgent before the 11/30 status conference.
- **Broker evidence:** the 10/22 capture is marks-only (quantities unchanged vs 10/19). Identities and quantities → `POSITIONS.md`; reconciliation → PROME/ANVIL (FORGE D82/D84/D74/D83). Will manages his own expiries (USER.md § No expiry nagging, 10/20); this desk books dispositions from his captures and sends no reminders.

## CONVERGENCE MATRIX — scores preserved

| Vector | Score | Current evidence / next carrier |
|---|---|---|
| V1a MI3 | 1/5 | DISCONFIRMED 8/7; CRE not secured by RE, not the Office book. Q3 Call Report not filed as of 10/28 |
| V1b broadening | 2/5 | Q2 DISCONFIRMED; Q3 DP2 DISCONFIRM final 10/21 (counter 2 of 3). A data point does not by itself trigger a re-score |
| V1b magnitude | 4/5 | Held as prior judgment, not a fresh confirmation. Q3 NCO guide held; $99M appraisal unresolved; favorable coverage vs OREO/SM rise |
| V2 fraud | 5/5 historical | EXCLUDED from composite. Cantor/legal Q3 details PENDING-10-Q; no implied recovery. Court path 10/22: remand + stay relief granted 8/24, §523 hearing 12/9 |
| V3 NDFI | 3/5 | Q2 exposure/history remain KB-146/168/230. The Q3 deck slide 23 (preliminary, rounded, HFI + HFS + eligible-loan basis) does not grade the 10-Q 25.9%-of-HFI test. New 10/28: First Eagle SPV $100M lender joinder 10/1 (KB-260) adds to the exposure-up evidence beside Crestline (KB-195). Borrower attribution and current stress unknown |
| V4 leadership | 3/5 | Held. 10/19 Form 4s routine (KB-252); Form 144 / 13D/G / open-market sweep clean 9/24 → 10/28 (KB-259); LEADERSHIP.md is 3/31 vintage |

Composite 13/25; weights 2/16/45/30/7 unchanged (THESIS owns them). No independent funding/peer/severity baseline built.

## EXIT RULES

*Kill rail re-derived: 2026-10-22 (against the Q3 print/call grades; the post-10-Q weight mapping is pre-registered in `Q3_10Q_RESCORE_RULE_2026-10-22.md`). Re-checked 10/28: no carrier has landed since, no state changed.*

| Rule | Condition / carrier | State |
|---|---|---|
| Bear-medium KILL | 0 new Office migrations AND benign $99M appraisal; deck/call/10-Q | **NOT FIRED**: leg (a) 0 migrations met at Q3; leg (b) appraisal PENDING-10-Q |
| Bear-fast KILL | MI3 < 25%, FFIEC | **FIRED 8/7**, reflected in v2.4; Q3 untested |
| Bear CONFIRM | WAL-01 Office > 500 or WAL-02 NCO > 40 | **NOT FIRED** on Stage-1 data; 01 provisionally invalid, 02 invalid with 10-Q confirm pending |
| Thesis RETIRE | Broadening disconfirmed 3 times AND coverage > 100% AND benign appraisal | **NOT FIRED**: counter **2 of 3**; coverage leg met 118%; appraisal PENDING-10-Q |
| GATE-REG-T02 (PROME gate) | Close < 78 | **TERMINAL** since 9/1; never re-fire on a sub-78 quote. REGINALD's registry trigger REG-T-02 (same letters, separate object) is carried FIRED by REGINALD |
| Robinhood exit guard | GATE-TERRY-ROLL70-EXIT, official close ≥ 81.90 × 3 | REGINALD's owner log last row 10/27, read 10/28: run 0 of 3, state FIRED (REGINALD grades; this desk claims no count). Contract scope → POSITIONS |

## NEXT CARRIERS

| When | Required work |
|---|---|
| Q3 10-Q (not on EDGAR at 10/28 ~22:40 ET; statutory Mon 11/9; ledger Resolve_By 11/15) | Run the frozen L171 frame verbatim: subsequent events first; $99M (§4); WAL-01 cross-check; WAL-02 confirm/correct; full NPL; OREO count/valuation; NDFI 25.9% test; Cantor tie-out and legal paragraphs; hotel O1–O8. Carried from the call: Office funded/criticized bridge, NDFI borrowers, total deposit cost, AOCI/CET1 RWA bridge. **Then the post-Q3 re-score, applying `Q3_10Q_RESCORE_RULE_2026-10-22.md` verbatim**, and register forward Q4 predictions |
| Q3 Call Report (not filed at 10/28; due Fri 10/30; **retry Sat 10/31 or later, before the JWT expires Thu 11/5**; REGINALD cohort screen due 11/7, D:L180) | Re-run `scripts/ffiec_wal_retrieve_20261014.py` for 2026-09-30 into a new dated `sources/ffiec_*` folder. MI3 and same-quarter bank NDFI/commitment/modification/mortgage/capital; June/December semiannual fields not expected at Q3. `workbook/MI3_SERIES.tsv` is LIVE but behind (attention-held 10/28): append the Q3 row |
| ~Thu 11/5 | OZK Q3 10-Q (per OZK STATUS): re-read the owner pointer behind KB-228 (sponsor-support peer); no OZK figure mirrored |
| ~Tue 11/10 | FINRA 10/30 settlement short interest (KB-258 successor; verify the FINRA calendar first) |
| **Wed 12/9/2026 11:00 AM** | WAL v. Stupin §523 (8:26-ap-01096): motion-to-dismiss hearing + status conference |
| Mon 11/30/2026 · Tue 1/12/2027 | Makhijani status conference / trial (KB-203) — **not re-verified** (10/22: RECAP Docs 93–98 had no text; 10/28: CourtListener refuses anonymous access) |

## OWNERS / CONTINUITY

**Positions → `POSITIONS.md` only**; no current mark or P&L mirrored here. TERRY's 65P management card supersedes the old note; the December 16 duty is DISCHARGED. The Fidelity 70P does not inherit the Robinhood guard or stop. Funding, peers and severity → REGINALD reports; no repeat study. The DEWEY 10/14 P&A artifact was consumed: a generic template cannot settle named-loan ownership; Ontario branch unchanged, the other three U. **Delivery:** own report + dated root PROME packet; native owner presence/notification/consumption UNKNOWN unless a session confirms it. Exact-path local commits; foreign work requires pull/push deferral. The NEXUS brief is pinned after the final STATUS commit. Frozen frames and SCENARIOS unchanged.
