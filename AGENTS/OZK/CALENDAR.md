# OZK CALENDAR

**Last Updated:** 2026-10-02 (10/2 read DONE: FLNG rc0 182 filings + one press search empty ⇒ reset HAPPENED, uncontradicted, not filing-confirmed; **Q3 date CONFIRMED — release Tue 10/20 after close, call Wed 10/21 8:30 ET** [OZK release dated 9/30]; the 10/1 'not announced' entry was WRONG — FLNG does not carry press releases; Nov-2 call-notice window row added) · prior 2026-10-01 (Oct 1 reprice row → reset SCHEDULED-UNCONTRADICTED, coupon ≈6.19% from the indenture + 3M Term SOFR [9/29]; 10/2 read narrowed; Jan-1-2027 call window added; Q3-date row re-dated) · prior 2026-09-27 (+PROME DOCKET L520 Q3 workout check on the Q3 row; severity label corrected to 50–65%) · prior 2026-09-24 (full rebuild: forward-only; resolved rows pruned row-by-row against the live queue — 2 kept as live-thread provenance; owed undated checks split out; Q4'26 print + insider window + JWT expiry added; OZK-02/03/04 resolve date corrected from "Feb 27 2027" [a Saturday] to the Q4'26 print ~mid/late Jan 2027). Older header history → `git log -p -- AGENTS/OZK/CALENDAR.md`. | **View:** forward dates + what to check + threshold. Pure table; narrative lives in the owner docs.

*For multi-bank events (cohort earnings, Call Reports, AOCI, FL reinsurance) → `../REGINALD/CALENDAR.md`. Dated rows that PROME tracks: DOCKET L126 (sub-notes reprice), L463 (10/2 read).*

---

## SEPTEMBER – OCTOBER 2026

| Date | Event | What to Check | Threshold / Signal |
|------|-------|---------------|-------------------|
| **Sep 30 ✅** *(corrected 10/2)* | Q3 earnings-date announcement — **made 9/30** (GlobeNewswire, dateline "LITTLE ROCK, Ark., Sept. 30, 2026"): release **Tue 10/20 after close**, call **Wed 10/21 7:30 CT / 8:30 ET** | ⚠️ The 10/1 entry here ("not announced as of 10/1 12:15 ET — FLNG quiet") was WRONG: the date release and the 10/1 dividend release (+$0.01 to $0.49) are both ABSENT from FDIC FLNG at 10/2 08:31 ET — FLNG does not carry press releases, so a quiet FLNG never answers a press-release question | Q3 row below + boot.py set to the real date (10/2) |
| **Oct 1 ✅ (SCHEDULED-UNCONTRADICTED · DOCKET L126 RESOLVED 10/1)** | **$350M sub notes reset** (DOCKET L126) — 2.75% fixed → **CME 3M Term SOFR + 209bp, Actual/360**, quarterly (Jan/Apr/Jul/Oct 1) [indenture, FDIC FLNG 5869, read 10/1] | FLNG rc 0 at 10/1 12:14 ET (none after 11981); no press. ⚠️ A call needs holder notice 10–60 days ahead via DTC — it need not be filed, so rc 0 is never "confirmed" | **Coupon ≈6.19%** (3M Term SOFR 4.09580% on 9/29, the INFERRED T−2 fixing; SINGLE-SOURCE print; 9/24–9/30 range 6.164–6.186%) ⇒ **≈+$12.3M/yr pre-tax, ≈$0.09 EPS** (was ≈+$11.2M — overnight-SOFR proxy + 30/360). Tier 2 −20% for 12mo. VERIFY at the Q3 10-Q (OZK is its own calculation agent). → `research/threads/2026-10-01_SUBNOTES_RESET.md` |
| **Fri Oct 2 ✅ (done 08:31 ET)** | **THE 10/1 READ** (DOCKET L463) | `flng_watch.py` **rc 0** at 08:31 ET — **182 filings returned, 182 unique ids, newest id 11981** (the 8/5 10-Q), schema + coverage OK; `--selftest` 11/11 PASS · one press search (sub-notes redemption/refinancing/notice): **nothing** on these notes; OZK's own 9/30 and 10/1 releases do not mention them | **Reset HAPPENED — contractual, uncontradicted, NOT filing-confirmed:** no call notice found in FLNG or press, and a 10/1 call needed holder notice by 9/21. Coupon ≈6.19% ⇒ ≈+$12.3M/yr pre-tax (Oct 1 row). The rate itself is VERIFIED only at the Q3 10-Q (~early Nov row) → `research/threads/2026-10-01_SUBNOTES_RESET.md` §5 |
| **~early Oct** | Pre-Q3 insider blackout begins (~14 days before the print) | FDIC EFR cert 110 (`/api/instdiscl/cert/110`) | Any open-market **buy** = notable (zero since 7/6). Sales before the blackout continue the pattern (CFO + 1 officer sold 8/12-13) |
| **Oct 6** | Bluerock BPRE (ex-TI+) semi-annual roadmap webinar | IQHQ mark / disposition talk (BPRE = IQHQ's largest holder, first-loss equity) | IQHQ markdown or exit language = sponsor-stress context for RaDD — **not a grade**. IQHQ gave Spur Ph I back to Apollo 9/17 [SINGLE-SOURCE] |
| **Tue Oct 20 (after close) · Wed Oct 21 8:30 ET call** *(CONFIRMED 10/2 from OZK's 9/30 release; was ~mid/late Oct estimate)* · PROME **DOCKET L520** (WQ-313 ③), CHECK-BY 10/31 | **★ Q3 earnings + call — mgmt's "~92-day" RaDD report-back** (Hamblen 7/22) · **+ Q2 workout follow-through** (`research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md` rows W1–W14): **OREO sale prices vs carrying**, Boston 10 Prospect outcome, RaDD terms, special-mention migration, **buyback execution**. If no OREO sale is priced in Q3, record exactly "no OREO sale priced in Q3" — the delayed-loss hypothesis stays OPEN | RaDD extension terms (executed? curtailment? new equity? mezz?) · **SpecMention $616M reversal rate** (Gleason's churn claim) · NCO vs "back under industry" FY guide · provision "drift down" · $330M pending-sale credit · Boston life sci $169.3M ($330M sale or title) · **Q3 closings promised in the Q2 MC: The Jack recap, Wauwatosa sale** · Baltimore (sale or title) · 8150 Sunset (LOI → contract) · **the 5 SM credits ($529M; the $147M condo at 105.6% LTV)** · the $40.4M C&I modification · FY NCO vs the industry average (mgmt goal to outperform; losses "remaining elevated" vs own history) · debt-on-debt composition | Extension WITH curtailment/paydown = A-solid · extension w/o cure + reserve = B · SpecMention stays or migrates INTO classified = adverse-selection hardens · any IQHQ specific reserve = 🔴 → REGINALD/BROCK/PROME |
| ⚠️ **UNVERIFIED — not actionable** *(was "Oct 2026")* | Affinius Capital "$2.7B bond maturity" — **the event itself is unverified**: issuer, instrument, amount and date have no primary source; possible Affinius / USAA Capital conflation (open since 4/22, TODO C5) | Verify from a primary source (issuer filing / CUSIP) or drop. Separately confirmed: OZK holds $95M of the Affinius-originated 777 Industrial note [KB-203] | Do not interpret news around this date until verified |

## NOVEMBER 2026

| Date | Event | What to Check | Threshold / Signal |
|------|-------|---------------|-------------------|
| **Nov 2 → Dec 22** | Sub-notes **Jan-1-2027 par-call holder-notice window** (Fiscal Agency Agmt §8: 10–60 days before the call date; subject to regulatory approval) | `flng_watch.py` at boot + a press search near 11/2 and mid-Dec — a notice need not be FDIC-filed | A call = 🟠 → REGINALD + PROME and **recalculate** (removes ≈$12.3M/yr cost AND the notes' ~$280M Tier 2; THESIS §Invalidation 4). Mgmt Q2'26: "no plans to replace them" |
| **~Nov 1-10** | **Q3 2026 Call Report** (REPDTE 20260930, RSSD 107244) | Re-run `workbook/CALL_REPORT_SERIES.tsv`: **`RIAD5409`** (does debt-on-debt charge-off continue?) · `RCON2746` vs the Q3 10-Q debt-on-debt figure · Memo-10 PV05-09 · past-due basis fork · 30-89 → nonaccrual/OREO transit | **LOG-ONLY — never re-grades.** |
| **Nov 5** | ⏰ **FFIEC CDR JWT expires** | Renewal = **Will action** (PWS login) | Blocks the Q3 Call Report pull if not renewed — check before ~Nov 1 |
| **2026-11-02 → 2026-12-22** | Notice window for a par call on the **2027-01-01** interest date (10–60 days' notice) | `flng_watch.py` (in boot.py) + press | A call = recalculate per THESIS §Invalidation 4; quiet = the floater runs another quarter |
| **~early Nov** | Q3'26 10-Q (FDIC-filed) | p.37 debt-on-debt balance · **the sub notes' floating rate** (VERIFIES the ≈6.19% reset — OZK is its own calculation agent) · nonaccrual / collateral-dependent marking · subsequent events (RaDD) | Feeds OZK-09's negative-branch sweep leg (3) |

## Q4 2026 PRINT (~mid/late Jan 2027)

| Date | Event | What to Check | Threshold / Signal |
|------|-------|---------------|-------------------|
| **~Jan 16-20, 2027** *(OZK's Q4 prints landed Jan 16-20 in 2023-26)* | **Q4'26 earnings — resolves OZK-02 / 03 / 04, and closes OZK-09's Option-2 window** | OZK-09: cumulative RaDD recognition **≥$140M** through this print absent an executed extension; negative branch resolves only after the 3-leg sweep named in `PREDICTIONS.tsv` (any UNKNOWN leg = STUCK) | ⚠️ **`$140M` here is OZK-09's live threshold — a different role from the dead "$140M EL" (EL is ~$129M since 7/23). Never global-replace it.** Weights A30/B45/C8/D17; OZK-09 **45%** |

---

## OWED CHECKS (undated — overdue or trigger-based)

| Check | Status | Why it matters |
|---|---|---|
| **Campus at Horton post-foreclosure leasing** (downtown SD, 770K SF; lender AllianceBernstein; window was late Jul) | 🔴 **OWED — UNRUN · CHECK-BY 2026-10-14** (set 10/1). 9/24 + 9/27 searches found nothing, which does **not** discharge it; lane phrase `Campus at Horton` live since 10/1 (RESEARCH-INTAKE 52b3ae6) is RECALL-UNPROVEN and discharges nothing | Leasing → RaDD severity lower; still empty → the D-severity band **50–65% ($275–360M)** holds (label corrected 9/27 from "65-70%"). An unrun check moves nothing |
| **SD County Recorder — RaDD assignments / notices** | ⚪ UNKNOWN since the 8/31 sweep | The one leg of the Aug-window sweep never run |
| **Aimco v. IQHQ** (Del. Chancery, $50M) — motion-to-dismiss ruling | 🟡 No ruling found (as of 9/24 search); needs a direct docket pull (courts.delaware.gov) | Sponsor-pressure context |

---

## RESOLVED — kept only as provenance for live threads

*Everything else resolved Apr–Sep was pruned 2026-09-24 (row-by-row against `STATUS.md` Open Items + `TODO.md`); outcomes live in STATUS, the scoring card, POSITIONS, the sweep threads, and git history.*

| Date | Event | Outcome | Live thread it feeds |
|------|-------|---------|---------|
| **May–Jun ✅** | Bluerock Q1'26 NAV marks (IQHQ) | No fresh Q1'26 markdown found — documented IQHQ marks are H2-2025 vintage (Bluerock >$700M exposure, −4.4% to $6.28; Highland −23% to $7.72; T.Rowe $4.92; Altegris $2.26) | Oct 6 BPRE webinar; STATUS Open Item 4 |
| **Aug 31 ✅** | IQHQ RaDD Aug-2026 maturity window | **SWEPT AND EMPTY** — FDIC FLNG zero Aug filings but the 8/5 10-Q (keyword-clean); press ×3 empty; recorder leg UNKNOWN. Quiet close = v1.5's pre-registered path; resolves nothing under the Option-2 ruling → `research/threads/IQHQ_AUG_WINDOW_CLOSE_SWEEP.md` | Q3 call report-back; OZK-09 |

*Pruning rule: resolved rows are removed at the next update unless a live thread travels them (then they sit here with the thread named).*
