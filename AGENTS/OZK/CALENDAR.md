# OZK CALENDAR

**Last Updated:** 2026-09-27 (+PROME DOCKET L520 Q3 workout check on the Q3 row; severity label corrected to 50–65%) · prior 2026-09-24 (full rebuild: forward-only; resolved rows pruned row-by-row against the live queue — 2 kept as live-thread provenance; owed undated checks split out; Q4'26 print + insider window + JWT expiry added; OZK-02/03/04 resolve date corrected from "Feb 27 2027" [a Saturday] to the Q4'26 print ~mid/late Jan 2027). Older header history → `git log -p -- AGENTS/OZK/CALENDAR.md`. | **View:** forward dates + what to check + threshold. Pure table; narrative lives in the owner docs.

*For multi-bank events (cohort earnings, Call Reports, AOCI, FL reinsurance) → `../REGINALD/CALENDAR.md`. Dated rows that PROME tracks: DOCKET L126 (sub-notes reprice), L463 (10/2 read).*

---

## SEPTEMBER – OCTOBER 2026

| Date | Event | What to Check | Threshold / Signal |
|------|-------|---------------|-------------------|
| **~Sep 30** | Q3 earnings-date announcement (Q2's came 6/30) | GlobeNewswire "Bank OZK" · `scripts/flng_watch.py` | Set the Q3 row below + boot.py `~2026-10-21` to the real date. Not announced as of 9/24; aggregators guess ~10/15 (estimate only) |
| **Oct 1** | **$350M sub notes reprice** (DOCKET L126) — 2.75% fixed → **3M term SOFR + 209bp**, quarterly (Jan/Apr/Jul/Oct 1) [issuer pricing release, GlobeNewswire 2021-09-09] | Pre-reprice refi/redemption notice. Watch = `scripts/flng_watch.py` (FDIC FLNG cert 110 — the only feed that sees an OZK 8-K; baseline FLNG 11981; in every boot.py; PROME runs it at its boots to 10/1). Mgmt: "no plans to redeem or replace." | Drag **≈+$11.2M/yr (≈$0.08 EPS)** at SOFR 3.87% [FRED 9/22; daily SOFR as proxy for 3M term] — was +$12.8M at the older SOFR. Tier 2 −20% for 12mo. Call/notice terms: indenture unread. |
| **Fri Oct 2 AM** | **THE 10/1 READ** (DOCKET L463) | `.venv/bin/python3 AGENTS/OZK/scripts/flng_watch.py` | **rc 0** = no newer filing returned by a schema+coverage-checked response ⇒ reprice **SCHEDULED-UNCONTRADICTED** (never "confirmed"; record rc, row count, date) · **rc 1** = read the filing — a redemption/refi is 🟠 → REGINALD, and it means **recalculate**, not "void": redeem-without-replacement removes the ~$11.2M/yr cost but also the notes' whole remaining Tier 2 (~$280M → $0); a refinance brings a new coupon + new eligibility (THESIS §Invalidation 4) · **rc 2** = UNKNOWN, re-run, never read as quiet |
| **~early Oct** | Pre-Q3 insider blackout begins (~14 days before the print) | FDIC EFR cert 110 (`/api/instdiscl/cert/110`) | Any open-market **buy** = notable (zero since 7/6). Sales before the blackout continue the pattern (CFO + 1 officer sold 8/12-13) |
| **Oct 6** | Bluerock BPRE (ex-TI+) semi-annual roadmap webinar | IQHQ mark / disposition talk (BPRE = IQHQ's largest holder, first-loss equity) | IQHQ markdown or exit language = sponsor-stress context for RaDD — **not a grade**. IQHQ gave Spur Ph I back to Apollo 9/17 [SINGLE-SOURCE] |
| **~mid/late Oct** · PROME **DOCKET L520** (WQ-313 ③): window 10/15–10/31 (ESTIMATE), **CHECK-BY 10/31** | **★ Q3 earnings + call — mgmt's "~92-day" RaDD report-back** (Hamblen 7/22) · **+ Q2 workout follow-through** (`research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md` rows W1–W14): **OREO sale prices vs carrying**, Boston 10 Prospect outcome, RaDD terms, special-mention migration, **buyback execution**. If no OREO sale is priced in Q3, record exactly "no OREO sale priced in Q3" — the delayed-loss hypothesis stays OPEN | RaDD extension terms (executed? curtailment? new equity? mezz?) · **SpecMention $616M reversal rate** (Gleason's churn claim) · NCO vs "back under industry" FY guide · provision "drift down" · $330M pending-sale credit · Boston life sci $169.3M ($330M sale or title) · **Q3 closings promised in the Q2 MC: The Jack recap, Wauwatosa sale** · Baltimore (sale or title) · 8150 Sunset (LOI → contract) · **the 5 SM credits ($529M; the $147M condo at 105.6% LTV)** · the $40.4M C&I modification · FY NCO vs the industry average (mgmt goal to outperform; losses "remaining elevated" vs own history) · debt-on-debt composition | Extension WITH curtailment/paydown = A-solid · extension w/o cure + reserve = B · SpecMention stays or migrates INTO classified = adverse-selection hardens · any IQHQ specific reserve = 🔴 → REGINALD/BROCK/PROME |
| ⚠️ **UNVERIFIED — not actionable** *(was "Oct 2026")* | Affinius Capital "$2.7B bond maturity" — **the event itself is unverified**: issuer, instrument, amount and date have no primary source; possible Affinius / USAA Capital conflation (open since 4/22, TODO C5) | Verify from a primary source (issuer filing / CUSIP) or drop. Separately confirmed: OZK holds $95M of the Affinius-originated 777 Industrial note [KB-203] | Do not interpret news around this date until verified |

## NOVEMBER 2026

| Date | Event | What to Check | Threshold / Signal |
|------|-------|---------------|-------------------|
| **~Nov 1-10** | **Q3 2026 Call Report** (REPDTE 20260930, RSSD 107244) | Re-run `workbook/CALL_REPORT_SERIES.tsv`: **`RIAD5409`** (does debt-on-debt charge-off continue?) · `RCON2746` vs the Q3 10-Q debt-on-debt figure · Memo-10 PV05-09 · past-due basis fork · 30-89 → nonaccrual/OREO transit | **LOG-ONLY — never re-grades.** |
| **Nov 5** | ⏰ **FFIEC CDR JWT expires** | Renewal = **Will action** (PWS login) | Blocks the Q3 Call Report pull if not renewed — check before ~Nov 1 |
| **~early Nov** | Q3'26 10-Q (FDIC-filed) | p.37 debt-on-debt balance · nonaccrual / collateral-dependent marking · subsequent events (RaDD) | Feeds OZK-09's negative-branch sweep leg (3) |

## Q4 2026 PRINT (~mid/late Jan 2027)

| Date | Event | What to Check | Threshold / Signal |
|------|-------|---------------|-------------------|
| **~Jan 16-20, 2027** *(OZK's Q4 prints landed Jan 16-20 in 2023-26)* | **Q4'26 earnings — resolves OZK-02 / 03 / 04, and closes OZK-09's Option-2 window** | OZK-09: cumulative RaDD recognition **≥$140M** through this print absent an executed extension; negative branch resolves only after the 3-leg sweep named in `PREDICTIONS.tsv` (any UNKNOWN leg = STUCK) | ⚠️ **`$140M` here is OZK-09's live threshold — a different role from the dead "$140M EL" (EL is ~$129M since 7/23). Never global-replace it.** Weights A30/B45/C8/D17; OZK-09 **45%** |

---

## OWED CHECKS (undated — overdue or trigger-based)

| Check | Status | Why it matters |
|---|---|---|
| **Campus at Horton post-foreclosure leasing** (downtown SD, 770K SF; lender AllianceBernstein; window was late Jul) | 🔴 **OWED — UNRUN.** 9/24 window search found nothing, which does **not** discharge it | Leasing → RaDD severity lower; still empty → the D-severity band **50–65% ($275–360M)** holds (label corrected 9/27 from "65-70%"). An unrun check moves nothing |
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
