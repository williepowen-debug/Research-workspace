# WAL STATUS

**Last Updated: 2026-11-26 — PROME inbox drain (WQ-206 aged-ask drain; Will 11:38 ET "catching up on any missed signals"): 8 inbox items consumed, 100 expired KB rows judged row by row, TERRY postmortem grades and the PROME KB answer sent, REGINALD's withdrawn Atlas SP figure corrected across WAL files. No weight, score, EV or completed-grade change.** Record: KB297–301; packets `../TERRY/inbox/2026-11-26_from-WAL_postmortem-thesis-grades.md`, `../../PROME/inbox/2026-11-26_from-WAL_stale-KB-rows-answer.md`, `../REGINALD/inbox/2026-11-26_from-WAL_ack-warehouse-rank-and-stale-7155.md`. *Prior update 2026-11-16 (PROME wake) and the 11/11 catch-up: rotated verbatim to `archive/STATUS_rotation_2026-11-26.md`.*

*The 10/22 version of this file is preserved verbatim at `archive/STATUS_before-10-28_2026-10-28.md` (sha256 59f568d3…daca9); earlier history at `archive/STATUS_before-cleanup_2026-10-22.md` and `archive/STATUS_before-Q3-stage1_2026-10-19.md`.*

## CURRENT — PROME inbox drain, November 26

**Price:** WAL **$70.76** at the 11/25 close (vendor; FORGE `fetch.py` and `market_tracker.py`, pulled 11/26 22:29 ET; Thanksgiving, NYSE closed 11/26, half session 11/27), **7.62% under EV $76.60**; KRE $69.83. Since the 11/10 close ($76.30): **WAL −7.26% vs KRE −4.46%**; 60-day beta to KRE **1.31** (1.17 at 11/10); 20-day realized volatility 34.3%. Series A preferred $23.39 (11/10 $24.38). Short interest at the 11/13 settlement **5.23M shares (−6.62%), 4.86% of cover shares**, days-to-cover 5.83. **No WAL-specific fact behind the fall:** EDGAR 10/28–11/26 holds only the 10-Q, the 10/30 dividend 8-K, a 13G/A and nine routine RSU Form 4s (KB-299). No trade is argued here.

**Present assessment:** v2.5 unchanged (2/12/49/30/7, EV $76.60, PT $52–77, composite 13/25). Spot is now 7.6% under the desk's EV. That gap opened on a sector-wide move with higher beta, not on WAL evidence. The EV is the scenario model's output and is no stronger than the open $99M leg and the unscored hotel and refinancing caution. A fall in price alone does not change the weights.

**Inbox 8 → 0** (`PROME/tools/inbox_census.py`; board receipts in `board_log.tsv`):

| Item | Disposition |
|---|---|
| DEWEY 11/18 + 11/26 Plaza Continental, WALTER SIG-W-20261118-011 | Integrated, **KB-297**. #128 'Granting in Part', terms unread. Cash collateral approved on an interim basis through 12/7. Final and status hearings Mon 12/7, 1:30 pm PT; status report due 12/1. #132 Objection (11/23): filer unknown. **H1–H11 NO-VERDICT; Ontario stays B1** |
| PROME 11/18 stale-KB ask | Answered: 100 judged, 78 SUPERSEDED, 22 extended with reasons (6 refreshed at the Q3 10-Q); expiry check now 0 of 124 |
| TERRY 11/20 postmortem thesis grades | Answered: TRY-WAL-ROLL70 **WRONG** for its window (the $99M leg UNRESOLVED, no carrier before 12/18); Sep-18 pair **WRONG** for its window |
| REGINALD 11/25 warehouse/MSR rank + Atlas correction (c324dddc8f) | Integrated, **KB-298**, verified at the Q3 10-Q: mortgage finance **$7,029M**, all current, none criticized, ACL $6.7M; 87.6% of Tier 1 on REGINALD's bank basis, 87.2% on the parent Tier 1 $8,058M. Atlas/PennyMac figure and $9.2B estimate withdrawn in THESIS, FRAUD riders and RETIRED_CLAIMS. Consumer check: 3 REGINALD surfaces still cite WAL's old $7.155B → packet sent |
| WALTER SIG-W-20261118-010 HY OAS 343 | Info only; logged as a context member of `combo:cre-refi-rate-pressure` (KB-291) |
| WALTER SIG-W-20261125-043 NYC rent freeze | Info only; FLG's book, no WAL rent-regulated exposure disclosed |

**Fresh primary reads today** (Q3 10-Q re-fetched from EDGAR; Q3 bank SDF already verified 11/04): CRE non-owner-occupied **office $2,254M** (6/30 $2,139M), $387M of it maturing in the rest of 2026; **hotel $5,295M, LTV 57.6%** (6/30 $4,958M, 54.0%); CRE-NOO 2027 maturities $3,346M (KB-300). Parent CET1 $7,389M / RWA $67,756M = 10.9%, total capital 14.0% (KB-243). This answers the open Basel III question (KB-294 retired; the issuer site was not retried). Bank pledged loans 55.6% of loans; uninsured deposits 39.7% of deposits (KB-301, on a stated basis). Four-quarter average assets $97.1B, $2.9B under the $100B Category IV line (KB-198). CLN reference pools $7.6B (KB-095). Cantor and LAM text restated as in Q2, with no new figure (KB-143, KB-152).

**Material uncertainties:** (1) the $99M life-science loan stays **NO-VERDICT**, with no disclosure since the Q2 call; the next carrier is the Q4 call. (2) The **warehouse-versus-MSR split** of the $7,029M and its borrowers are not disclosed. Fitch's 11/16 review (Negative outlooks on Pennymac, Freedom, Planet) and LIQUID's 11/24 Freedom read are PROME relays that WAL has not read. (3) Plaza #132's filer is unknown. (4) Hotel criticized loans of $185M at 9/30 with $0 nonaccrual (WAL-04).

**Combination watch (7 themes, `combo:` in `workbook/KB.tsv`):** bank-credit-breadth · cantor-collateral-liens (KB-297 added) · cre-refi-rate-pressure (KB-291 updated: KB-300, HY 343) · fraud-ecosystem-names · rate-path-deposit-cost · securities-mark-tbv · **nonbank-mortgage-lenders (opened 11/26, KB-298)**. Charter line added at boot step 7c (class C4: no authority, route or threshold moved).

**Unresolved obligations:** WAL-03 to WAL-07 OPEN; re-pin WAL-03/06 when the Q4 print date is announced. The evidence-based vector/composite review is still owed (carried since 11/04). Will-side items are unchanged (§ OPERATOR DEPENDENCIES). **Next dated triggers:** Tue 12/1 Plaza status report → Mon 12/7 Plaza hearings → Wed 12/9 Stupin §523 hearing → mid-December FOMC → Q4 print (not yet announced).

## Q3 Call Report, November 4 (dated)

The source/access blocker is resolved for this assignment. CATO's complete Q3 SDF verifies against its receipt and WALTER's historical hash (1,792 rows); WAL independently extracted the approved fields. **MI3 21.20% → 19.81%** on the existing item4 basis, below 25%; the 8/7 bear-fast kill remains fired, no new firing. **NDFI nonaccrual $122.456M → $122.497M**, nearly flat; unused commitments **$4.884B → $5.900B (+20.8%)**, contractual capacity rather than funded stress. Modified populations improve on balance; bank mortgage income rebounds while sales fall; bank CET1 **11.5823% → 11.4458%**. These bank measures do not identify the $99M office loan or replace parent earnings/capital. **v2.5 / EV $76.60 / weights, scores and completed grades unchanged.** Details, borrower/hedge/population limits → the new report and KB282–287. Earlier failures and missing-source reports remain dated history.

**Interpretation limits (clarified November 4):** These are **June 30 to September 30** comparisons, not a reading of November conditions. MI3 is CRE-purpose lending **not secured by real estate**, divided by C&I item 4; **25% is WAL's registered thesis threshold, not a regulatory limit**. The fast-bear scenario retains **2%**, rather than being eliminated. Independent extraction verifies the bank's disclosures; overlapping Call Report/10-Q observations are **not two separate credit improvements**. Unchanged weights and scores reflect the bounded extraction scope, **not a fresh full-thesis reaffirmation**; the separate evidence-based assessment remains owed.

## BOTTOM LINE (2026-10-30 eve) ★

**The Q3 10-Q landed (acc 0001628280-26-068599, 16:38 ET) and does not mention the $99M life-science loan at all** — it even drops the Q2 sentence that named it. Under the frozen frame that is **NO-VERDICT ("nothing anywhere"), never a cure**, and the pre-registered, Will-approved rule maps it to **Bear-medium 16 → 12 (+4 Base) ⇒ v2.5: 2 / 12 / 49 / 30 / 7, EV $75.96 → $76.60, PT $52–77.** The Bear-medium kill did **not** fire; the appraisal question goes to the Q4 call. **WAL-01 is final INVALIDATED** (cross-check 926 + 165 = 1,091 ≥ 272.75) and **WAL-02 is confirmed** at 30bps. Live residual: OREO 22 → 27 properties (one office property taken in Q3), special mention 316 → 397, **hotel franchise finance criticized $75M → $185M** (still no nonaccrual or charge-off); against it, accruing restructured loans fell 164 → 129. Same-day 8-K: common dividend $0.42 → $0.46; **preferred reset to 8.36%** (from 4.25%, ~+$12.3M/yr). Grade: `research/2026-10-30_Q3_10Q_GRADE.md`.

## BOTTOM LINE (2026-10-28) and Q3 FROZEN-FRAME GRADES (10/19–10/21) — rotated

Both superseded/historical blocks moved verbatim on 2026-11-11 to `archive/STATUS_rotation_2026-11-11.md` (sha256 1fc979ad6905…). Stage 1/2 grade files: `research/2026-10-19_Q3_STAGE1_GRADE.md`, `research/2026-10-21_Q3_STAGE2_CALL_GRADE.md`; completed 10-Q grade above.

## LATEST (10/28) — rotated

The 10/28–10/30 item table (10-Q grade, WQ-553 amendment, frame dry run, $99M appraisal prior, workbook and tracker builds, NDFI First Eagle joinder, insider sweep, short interest, sell-side, courts, Jefferies, credit-ratings baseline, leadership, March KB rows, boot kit, housekeeping) moved verbatim on 2026-11-16 to `archive/STATUS_rotation_2026-11-16.md` (sha256 900d082f6153…). Each row keeps its KB/research pointer there.

## PRICE

**Price (11/25 session close, vendor; fetch.py and boot.py 11/26 22:25–22:29 ET; NYSE closed 11/26): $70.76 (+0.47%)**; SPOT vs EV **−7.62% vs v2.5 EV $76.60**; buffer to 81.90 **+15.74%** (delta/spot). KRE $69.83 (+0.10%). REGINALD's REG-T-02 exit log last row 11/24 (close 70.43): run 0 of 3, FIRED (REGINALD grades; read via boot.py).

## JUDGMENT

**11/26:** no new credit evidence; spot $70.76 (11/25 close) is 7.62% under EV after a sector-wide fall, so the 10/30 'no margin of safety either way' line below is out of date on price only. Weights unchanged; see § CURRENT. **10/30 eve:** the 10-Q left the $99M unaddressed, so the rule trimmed Bear-medium by the print/call evidence alone (16 → 12) and the kill stays unfired. Spot ($76.29 10/30 close) now sits ~0.4% below EV: still no margin of safety either way. The next real carriers are the Q4 call (the $99M asked directly), the Q3 Call Report (MI3, Bear-fast) and the hotel franchise finance book, whose criticized balance 2.5×'d in the quarter. *The paragraph below is the 10/22 judgment, kept as dated context.*

Q3 credit actuals weaken the near-term bear: NCO 30bps, Office classified $272.75M (provisional), coverage 118%. Earnings and capital are mixed: NIM improved, but costs, mortgage, guidance and tangible book need qualification. The $99M appraisal was not identified in the release, deck or call: unknown, not benign. No demonstrated expectations gap. A ledger invalidation is not a silent score change; the post-Q3 re-score waits for the 10-Q.

## FIVE THINGS THAT MATTER

1. Nonaccrual 562 → 485, but OREO 126 → 165; combined 688 → 650 (−38, versus −77 for nonaccrual alone). Special mention 316 → 397; classified accruing 440 → 441. No cash cure or loan migration is inferred from net stocks.
2. EPS 2.45 vs 2.36; PPNR 419.1 vs 412.4; pretax 339.1 vs 332.0; tax 61.9 vs 63.2. Vendor consensus basis and dates unmatched: no certified beat.
3. NII +10.7, NIM +4bp; mortgage 84.7 → 79.5 (origination 55.7, servicing 23.8). Expense ex-deposit costs 404.1 → 429.7; salary +21.8. The three ECR/referral-line total 234.2 → 223.7; those savings overlap the deposit-expense reduction, so never add them twice. Funding analysis → REGINALD.
4. The Q3 comparative reclassifies customer derivatives/FX into commercial fees: Q2 FV is now 8.3 vs 12.8 in the October 14 screen; net income unchanged. On the new presentation, PPNR less security sale/FV = 401.8 vs 401.1. This is not issuer-adjusted EPS nor the old 8.98 screen; the hedge/persistence bridge is unknown.
5. AOCI −451 → −786; TCE 6,906 → 6,720; TBV 63.24 → 62.22; parent CET1 11.0% → 10.9% (preliminary; CET1 capital $7,389M disclosed). Buyback $92.1M on track but consumes capital. NII guide 12–14% → 11–12%; fees 13–17% → 18–21%; expense 7–11% → 7–10%; deposit growth $6B → $3.5–4B.

**Earnings bridge** (`research/2026-10-19_Q3-recurring-earnings-bridge.md`, KB-245–247): visible-gain-screen pretax 320.7 → 321.8 vs reported 332.0 → 339.1. On a consistent basis the guide midpoint is roughly flat net. The literal ex-deposit cost guide needs Q4 ≤ 405.1 vs 429.7, a 24.6 decline; the call answered Q4 ex-deposit expense −5–7% and the fee guide all-in, Q4 mortgage ~$70M (KB-250). Guide exclusions, cost persistence and MSR cash hedges remain unknown, not a miss. **Full read** (`research/2026-10-19_Q3_FULL_READ.md`, KB-243/244): loan provision 80.8 minus HTM release 0.8 ties consolidated 80.0; loan ACL build 35.0. **Weakness-study contribution** (`research/2026-10-19_broader-bank-stress-context.md`): NCO 30bps, coverage 118%, broadly stable deposits and lower borrowings do not confirm spreading bank stress; SM +81, OREO +39, securities marks and mix costs remain cautions.

## OPERATOR DEPENDENCIES

- **Moreno Valley recorder:** deed-of-trust instrument/APN missing. His 10/13 response: no results unless REGINALD pulled them; a prior targeted owner search found none. Not re-asked. Ontario B1 does not resolve Moreno Valley. DEWEY 10/28 tested all four lien counties: every route is human-only (San Bernardino reCAPTCHA; Riverside public but scripted submissions fail; Los Angeles/Bellflower has no online index); exact searches in `../DEWEY/output/2026-10-28_nano-loans-passive-records-route.md` §2.
- **FFIEC — source dependency resolved for this assignment:** 11/04 CATO authenticated Q2/Q3 HTTP 200 sources were verified and copied durably by WAL; independent extraction complete. Earlier local HTTP 500/403 attempts and desktop-token observations remain dated history. This result does not certify renewed-token installation on both machines or close PROME's other WQ-31 credential tasks; no credential request is needed to finish this extraction.
- **NYSCEF index numbers** (WAL v. Jefferies; Point Bonita v. WAL): Will-side browser search offered 10/22, unanswered.
- **Quartr is a subscription gate, not a re-authentication:** on 10/28 the connector was signed in as Will but refused with "Quartr Pro subscription required" (plan: none). Quartr is a paid source Will already DECLINED (WQ-220, preserved in the WQ-298 paid-data ruling), so this item is closed, not owed: the two B2 call transcripts stay B2, and no grade depends on them.
- **CourtListener:** anonymous API and search now refused (401/403, 10/28). The Makhijani dates need a token, DEWEY's PACER route, or a browser check; not urgent before the 11/30 status conference.
- **Broker evidence:** the 10/22 capture is marks-only (quantities unchanged vs 10/19). Identities and quantities → `POSITIONS.md`; reconciliation → PROME/ANVIL (FORGE D82/D84/D74/D83). Will manages his own expiries (USER.md § No expiry nagging, 10/20); this desk books dispositions from his captures and sends no reminders.

## CONVERGENCE MATRIX — scores preserved

| Vector | Score | Current evidence / next carrier |
|---|---|---|
| V1a MI3 | 1/5 | Q3 retest **19.8072%** vs Q2 21.2042%, existing item4 basis, below 25%; prior 8/7 disconfirmation/kill remains. CRE not secured by RE, not the Office/$99M book. Source verified/extracted 11/04; no score change |
| V1b broadening | 2/5 | Q2 DISCONFIRMED; Q3 DP2 DISCONFIRM final 10/21 (counter 2 of 3). A data point does not by itself trigger a re-score |
| V1b magnitude | 4/5 | Held as prior judgment, not a fresh confirmation. Q3 NCO guide held; $99M appraisal unresolved; favorable coverage vs OREO/SM rise |
| V2 fraud | 5/5 historical | EXCLUDED from composite. Auditor-nexus support weakened 10/28 (KB-071/072/076 superseded; RSM 2025 inspection clean on ACL, KB-268). Cantor Q3 disclosure NARROWED in the completed 10/30 grade; residual/allowance unresolved, no implied recovery. Court path 10/22: remand + stay relief granted 8/24, §523 hearing 12/9 |
| V3 NDFI | 3/5 | Q3 bank nonaccrual **$122.497M** vs $122.456M (rate ~0.774%); unused commitments **$5.900B**, +20.8%, not funded draws. Share 25.723% HFI vs 25.943% Q2, dollars slightly up, consistent with completed 10-Q MIXED. Borrower/loss attribution remains unknown; no score change. KB283–284. **11/26:** mortgage finance $7,029M (warehouse + MSR loans), all current, none criticized; REGINALD ranks WAL first of 14 banks against Tier 1 (KB-298). That is a concentration, not stress; no score change |
| V4 leadership | 3/5 | Held. 10/19 Form 4s routine (KB-252); Form 144 / 13D/G / open-market sweep clean 9/24 → 10/28 (KB-259). LEADERSHIP.md refreshed 10/28 (KB-261–264): Curley's stated reason is a CEO role elsewhere, RSM re-ratified, board 15 → 13; the March "repositioning" reading has weakened, residual is the June Gibbons/Mucha sales. Score re-judged at the re-score |

Composite 13/25; current scenario weights → THESIS. No Call Report-driven change; no independent funding/peer/severity baseline built.

## EXIT RULES

*Kill rail re-derived: 2026-10-22 (against the Q3 print/call grades; the post-10-Q weight mapping is pre-registered in `Q3_10Q_RESCORE_RULE_2026-10-22.md`). Re-checked 10/28: no carrier has landed since, no state changed.*

| Rule | Condition / carrier | State |
|---|---|---|
| Bear-medium KILL | 0 new Office migrations AND benign $99M appraisal; deck/call/10-Q | **NOT FIRED**: leg (a) 0 migrations met at Q3; leg (b) appraisal NO-VERDICT after the 10-Q, carried to the Q4 call |
| Bear-fast KILL | MI3 < 25%, FFIEC | **FIRED 8/7**, reflected in v2.4; Q3 retest **19.8072% < 25%** on 11/04, same existing rail; no new firing |
| Bear CONFIRM | WAL-01 Office > 500 or WAL-02 NCO > 40 | **NOT FIRED** on the completed 10/30 grade; WAL-01 and WAL-02 INVALIDATED FINAL. Forward Q4 predictions WAL-03 to WAL-07 registered 11/16 (OPEN); this rule's letter is unchanged |
| Thesis RETIRE | Broadening disconfirmed 3 times AND coverage > 100% AND benign appraisal | **NOT FIRED**: counter **2 of 3**; coverage leg met 118%; appraisal NO-VERDICT after the 10-Q, carried to the Q4 call |
| GATE-REG-T02 (PROME gate) | Close < 78 | **TERMINAL** since 9/1; never re-fire on a sub-78 quote. REGINALD's registry trigger REG-T-02 (same letters, separate object) is carried FIRED by REGINALD |
| Robinhood exit guard | GATE-TERRY-ROLL70-EXIT, official close ≥ 81.90 × 3 | **RETIRED 2026-11-05** (WQ-610 A, Will 11:03 ET; `PROME/GATES.tsv`, read 11/26): card TRY-WAL-ROLL70 dead by Will 10/29. This line read 'FIRED' through 11/16 and was stale. REGINALD's registry trigger REG-T-02 is a separate object, still FIRED by REGINALD. Contract scope → POSITIONS |

## NEXT CARRIERS

| When | Required work |
|---|---|
| $99M appraisal / Q4 call (date not set) | Ask status at 9/30, whether the appraisal was received, and value vs carrying. The Q3 10-Q is already graded NO-VERDICT; never repeat that grade. WAL-07 resolves by the FY2026 10-K (2027-03-01) |
| Q3 Call Report | **DONE 11/04:** complete primary source verified and independently extracted; no retrieval/extraction remainder. Next MI3 data is the existing standing quarterly Q4 Call Report pull; June/December semiannual fields retain their frequency. Borrower attribution, parent bridges and other carried work are separate conditions, not missing Q3 extraction. |
| Next FINRA settlement (~mid-December; calendar not verified) | Log in MARKET_TRACKER (`scripts/market_tracker.py --write`). **DONE 11/26:** 11/13 settlement 5,228,513 shares, 4.86% of cover shares |
| Mid-December FOMC (date per the Fed calendar; not verified here) | 0 / 25 / 50bp decides how far the hike goes past the guide's assumed +25bp (KB-289). Its earnings effect falls mostly in Q1 2027; read it against the Q4 total deposit cost and the ECR line |
| Q4 print date announcement | Re-pin WAL-03/06 Resolve_By (EXPECTED-EVENT anchors) |
| **Tue 12/1** · **Mon 12/7 1:30 pm PT** | Plaza Continental: debtor's status report (#129), then the final cash-collateral and status hearings (#130). DEWEY reads. Apply the H1–H11 sheet (KB-297): a final order with terms, a sale motion with a price, or #132 identified as a secured-lender objection would be the first economic evidence; a sale order or price is H8 |
| **Wed 12/9/2026 11:00 AM** | WAL v. Stupin §523 (8:26-ap-01096): motion-to-dismiss hearing + status conference |
| Mon 11/30/2026 · Tue 1/12/2027 | Makhijani status conference / trial (KB-203) — **not re-verified** (10/22: RECAP Docs 93–98 had no text; 10/28: CourtListener refuses anonymous access) |

## OWNERS / CONTINUITY

**Positions → `POSITIONS.md` only**; no current mark or P&L mirrored here. TERRY's 65P management card supersedes the old note; the December 16 duty is DISCHARGED. The Fidelity 70P does not inherit the Robinhood guard or stop. Funding, peers and severity → REGINALD reports; no repeat study. The DEWEY 10/14 P&A artifact was consumed: a generic template cannot settle named-loan ownership; Ontario branch unchanged, the other three U. **Delivery:** own report + dated root PROME packet; native owner presence/notification/consumption UNKNOWN unless a session confirms it. Exact-path local commits; foreign work requires pull/push deferral. The NEXUS brief is pinned after the final STATUS commit. Frozen frames and SCENARIOS unchanged.
