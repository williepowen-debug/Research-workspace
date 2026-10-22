# OZK CALENDAR

**Last Updated:** 2026-10-22 — Q3 call Stage-2 read (`research/threads/2026-10-22_Q3_CALL_STAGE2_READ.md`); past October rows pruned; 10-Q re-dated ~Thu 11/5 at the FDIC index. Prior 2026-10-21 Stage-1 grade.

*For multi-bank events (cohort earnings, Call Reports, AOCI, FL reinsurance) → `../REGINALD/CALENDAR.md`. Dated rows that PROME tracks: DOCKET L126 (sub-notes reprice), L463 (10/2 read).*

---

## SEPTEMBER – OCTOBER 2026

| Date | Event | What to Check | Threshold / Signal |
|------|-------|---------------|-------------------|
| **Tue Oct 20 (after close) · Wed Oct 21 8:30 ET call** — ✅ **Stage-1 GRADED 10/21**, ✅ **Stage-2 (call) READ 10/22** · DOCKET L520 | Results → `research/threads/2026-10-21_Q3_PRINT_STAGE1_GRADE.md` + `research/threads/2026-10-22_Q3_CALL_STAGE2_READ.md`; card RESULTS appended (`workbook/Q3_2026_SCORING_CARD.md`) | Call added nothing toward stress, closed no leg. Open legs (SM −$313M flow, RaDD reserve/readvance, Sullivan, OREO marks) → Q3 10-Q. Insider blackout lifts after the print: EFR cert 110 had **no filing after 8/14** at 10/22 | Conviction re-grade proposed (P-OZK-7), Will-gated |
| **Tue October20,2026 — original expected repayment (PASSED; outcome UNKNOWN at 10/22)** | **New Economy Assets–Phase1 Issuer LLC / USRE2021-1**, original $2.69136B Amazon warehouse lease ABS. **Original ARD October20,2026; legal final October20,2061** [S&P October18,2021 indexed primary table; June2026 SEC holder schedule] | C5 issuer/date check DONE10/12. Current amendments/payoff/refinancing UNKNOWN; CTSLink NEA20211 lists October20 next report, actual report sign-in. Source/access → `research/threads/2026-10-12_AIMCO_AFFINIUS_CHECK.md` | Unpaid original ARD can trigger early amortization/additional-interest mechanics; **not automatically Affinius corporate default or OZK loss**. Co-lending exposure remains separate |

## NOVEMBER 2026

| Date | Event | What to Check | Threshold / Signal |
|------|-------|---------------|-------------------|
| **Nov 2 → Dec 22** | Sub-notes **Jan-1-2027 par-call holder-notice window** (Fiscal Agency Agmt §8: 10–60 days before the call date; subject to regulatory approval) | `scripts/flng_watch.py` at boot + a press search near 11/2 and mid-Dec — a notice need not be FDIC-filed | A call = 🟠 → REGINALD + PROME and **recalculate** (removes ≈$12.0M/yr cost at the issuer's 6.14% AND the notes' ~$280M Tier 2; THESIS §Invalidation 4). Mgmt Q2'26: "no plans to replace them" |
| **~Nov 1-10** | **Q3 2026 Call Report** (REPDTE 20260930, RSSD 107244) | Re-run `workbook/CALL_REPORT_SERIES.tsv`: **`RIAD5409`** (does debt-on-debt charge-off continue?) · `RCON2746` vs the Q3 10-Q debt-on-debt figure · Memo-10 PV05-09 · past-due basis fork · 30-89 → nonaccrual/OREO transit | **LOG-ONLY — never re-grades** predictions. **THESIS invalidation 8** (added 10/22): `RIAD5409` YTD still $42,437K = fired; check-by Mon 11/16 · **OZK-10** (35%, Q3 increment >0) resolves on the same pull, RESOLVE_BY 11/16 |
| **Nov 5** | ⏰ **FFIEC CDR JWT expires** | Renewal = **Will action** (PWS login) | Blocks the Q3 Call Report pull if not renewed — check before ~Nov 1 |
| **2026-11-02 → 2026-12-22** | Notice window for a par call on the **2027-01-01** interest date (10–60 days' notice) | `scripts/flng_watch.py` (in boot.py) + press | A call = recalculate per THESIS §Invalidation 4; quiet = the floater runs another quarter |
| **~Thu Nov 5** *(re-dated 10/22: Q3 10-Qs filed 11/5/2024 and 11/5/2025, FDIC index; D:L763 carries 11/6)* | Q3'26 10-Q (FDIC-filed) | p.37 debt-on-debt balance · sub-notes rate (issuer already printed **6.14%** for Q4-26 in Q3 MC p.35 — the 10-Q is a second confirmation) · **SM −$313M credit flow** · **RaDD reserve / readvance** · Sullivan · OREO roll-forward · nonaccrual / collateral-dependent marking · subsequent events | Feeds OZK-09's negative-branch sweep leg (3) · **THESIS invalidation 6** (added 10/22): ≥$200M of the SM decline to pass/payoff = fired; not itemized = UNKNOWN; check-by Mon 11/16 |

## Q4 2026 PRINT (~mid/late Jan 2027)

| Date | Event | What to Check | Threshold / Signal |
|------|-------|---------------|-------------------|
| **~Jan 16-20, 2027** *(OZK's Q4 prints landed Jan 16-20 in 2023-26)* | **Q4'26 earnings — resolves OZK-02 / 03 / 04 / 11 / 12 (11 + 12 RESOLVE_BY 2027-03-01, the 10-K deadline), and closes OZK-09's Option-2 window** | OZK-09: cumulative RaDD recognition **≥$140M** through this print absent an executed extension; negative branch resolves only after the 3-leg sweep named in `workbook/PREDICTIONS.tsv` (any UNKNOWN leg = STUCK) | ⚠️ **`$140M` here is OZK-09's live threshold — a different role from the dead "$140M EL" (EL is ~$129M since 7/23). Never global-replace it.** Weights A30/B45/C8/D17; OZK-09 **45%** |

---

## OWED CHECKS (undated — overdue or trigger-based)

| Check | Status | Why it matters |
|---|---|---|
| **Horton post-foreclosure current occupancy** | **Bounded work DONE 10/12; result UNRESOLVED**; original 10/14 checkpoint retained. Dated Q1 office primary is a forecast; listings/older retail not current lease execution | `research/threads/2026-10-12_HORTON_BOUNDED_CHECK.md`. New dated Propco/broker/tenant evidence can resolve via normal lane; no fresh vacancy/comp-severity claim |
| **SD County Recorder — signed RaDD instrument/covenants** | **UNKNOWN — 403 on 10/12 web open**, no native browser exposed | Issuer 10/12 8-K establishes execution October 9 to December 2029; recording number/title (including whether Sixth Modification), rate/covenants/redraw budget not independently read. Useful corroboration, not a blocker to the execution finding |
| **Aimco v. IQHQ** — motion/ruling status | **UNKNOWN10/12:** official2026 opinion searches IQHQ/Aimco return no results; full Chancery docket is **File & ServeXpress**, unavailable. Search outcome is not docket certification | C3 public leg DONE; exact case number/motion/order remain access gaps. No $50M judgment asserted → `research/threads/2026-10-12_AIMCO_AFFINIUS_CHECK.md` |

---

## RESOLVED — kept only as provenance for live threads

*Everything else resolved Apr–Sep was pruned 2026-09-24 (row-by-row against `STATUS.md` Open Items + `TODO.md`); outcomes live in STATUS, the scoring card, POSITIONS, the sweep threads, and git history.*

| Date | Event | Outcome | Live thread it feeds |
|------|-------|---------|---------|
| **Oct 9 execution / Oct 12 disclosure ✅** | RaDD bridge outcome (DOCKET L635) | Executed extension to December 2029, fresh $100M; WQ-395 extension leg MET; OZK-09 OPEN/STUCK on recognition attribution | `research/threads/2026-10-12_RADD_BRIDGE_OUTCOME.md`; L520 accounting resolver |
| **June30 / August28 filing · read October12** | BPRE newer IQHQ marks obtained | June common equity **$317,371,980**, subsequent footnote **$270,611,845**, derived **−14.73%**; exact subsequent valuation day undisclosed. **Supersedes H2'25-only desk state**, not an October event | `research/threads/2026-10-12_IQHQ_FUNDING_AND_MARKS.md`; no class-specific price or OZK loss inferred |
| **Aug 31 ✅** | IQHQ RaDD Aug-2026 maturity window | **SWEPT AND EMPTY** — FDIC FLNG zero Aug filings but the 8/5 10-Q (keyword-clean); press ×3 empty; recorder leg UNKNOWN. Quiet close = v1.5's pre-registered path; resolves nothing under the Option-2 ruling → `research/threads/IQHQ_AUG_WINDOW_CLOSE_SWEEP.md` | Q3 call report-back; OZK-09 |
| **Oct 1 ✅** | $350M sub-notes reset to CME 3M Term SOFR + 209bp, Act/360 (DOCKET L126 RESOLVED 10/1; 10/2 read L463: uncontradicted, not filing-confirmed) | Coupon ≈6.19% ⇒ ≈+$12.3M/yr pre-tax *(desk estimate of 10/1; superseded by the issuer's 6.14% / ≈$12.0M, Q3 MC p.35)* → `research/threads/2026-10-01_SUBNOTES_RESET.md` | ~early Nov Q3 10-Q (VERIFY the rate) · Nov 2 → Dec 22 call-notice window |
| **Oct 6 ✅ · written summary read10/12** | Bluerock BPRE semi-annual roadmap webinar | Held **4:00PM ET, after close**. October7 written replay summary read; whole video/Q&A unavailable. September30 IQHQ equity weights **5.3% warrant-exercised +2.6% gross assets**, not unit-price marks | Funding/marks artifact; pipeline and valuation-basis qualifiers retained |

*Pruning rule: resolved rows are removed at the next update unless a live thread travels them (then they sit here with the thread named).*
