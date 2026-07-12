# CRL-06 Data Package — Foreclosures >70K/qtr (Q2 2026 target)

**Prepared by:** HOMER (data owner) | **For:** CARL (resolution owner, `AGENTS/CARL/thesis/PREDICTIONS.tsv` CRL-06) | **Date:** 2026-07-12 (HOMER first-boot session)
**Purpose:** Per the promotion ★ ruling (`AGENTS/DAEDALUS/builds/homer_promotion/PROMOTION_REVIEW.md`), HOMER supplies the raw dataset; CARL owns the metric-definition and resolution call. This package assembles every ATTOM figure relevant to the "70K/qtr" threshold, cleanly labeled by metric, with exact source+date on each row.

---

## 1. The core ambiguity

CRL-06's original wording ("Foreclosures exceed 70K/quarter") does not specify which ATTOM series it refers to. ATTOM's quarterly Foreclosure Market Report publishes **three distinct national counts** that differ by an order of magnitude and mean different things:

| Metric | Definition | Q1 2026 value | vs. 70K threshold |
|---|---|---|---|
| **Filings** | Any property with a foreclosure action in the quarter (default notices, scheduled auctions, OR bank repossessions — counts a property once even if it has multiple actions) | **118,727** | CONFIRMED (+69.6%) |
| **Starts** | Properties entering the foreclosure process for the first time in the quarter (subset of filings — earliest-stage count) | **82,631** | CONFIRMED (+18.0%) |
| **REO / Completions** | Properties that completed the foreclosure process and reverted to lender ownership in the quarter (latest-stage, smallest count by construction) | **14,020** | NOT MET (−80.0%) |

**This is not a rounding question — the metric choice is outcome-determinative.** If CRL-06 means filings or starts, Q1 2026 already confirms it (and has since the Apr 16 ATTOM release — this is not a Q2-forward call). If it means REO/completions, the prediction is nowhere close and the mechanism (cure collapse → pipeline conversion) would need another ~2-3 quarters of REO growth at the current +45% YoY pace to close an 80% gap. **HOMER takes no position on which reading is correct — that is explicitly CARL's call** (per ★ ruling) — but flags that "which metric" and "is CRL-06 confirmed" are the same question, not two separate ones.

Source: ATTOM Q1 2026 Foreclosure Market Report, released 2026-04-16 (`AGENTS/HOMER/workbook/KB.tsv` KB-HMR-057; cross-filed `AGENTS/CARL/workbook/KB.tsv` KB-CARL-221).

---

## 2. Full quarterly + monthly dataset (national)

### Quarterly (the threshold's native cadence)

| Period | Filings | Starts | REO | Source |
|---|---|---|---|---|
| Q4 2025 | 58,140 | n/a (not separately reported in this cut) | n/a | ATTOM |
| **Q1 2026** | **118,727** (+6% QoQ, +26% YoY) | **82,631** | **14,020** (+45% YoY) | ATTOM, rel 2026-04-16 |
| Q2 2026 | *pending* | *pending* | *pending* | ATTOM Q2 report — est. ~Jul 16, unconfirmed (see docket) |

### Monthly (component data — used here to build a Q2 run-rate ahead of the formal Q2 release)

| Month | Filings | Starts | REO Completions | Source |
|---|---|---|---|---|
| Mar 2026 | 45,921 (+18% MoM, +28% YoY) | — | 5,229 (+28% MoM) | ATTOM, rel ~mid-Apr |
| Apr 2026 | 42,430 (−8% MoM, +18% YoY) | 28,414 (+12% YoY) | 5,098 (+42% YoY) | ATTOM, rel 2026-05-14 |
| May 2026 | 40,355 (−5% MoM, +14% YoY) | **27,304** (−4% MoM, +13% YoY) | **4,092** (−20% MoM, +6% YoY) | ATTOM, rel 2026-06-11 (verified live this session — matches HOMER's inherited PIPELINE.tsv row exactly) |
| Jun 2026 | *not yet released as of 2026-07-12* | *not yet released* | *not yet released* | — |

**Q2 run-rate build (Apr+May actuals, June pending):**
- **Starts:** 28,414 + 27,304 = **55,718** for 2 of 3 months. Q1's full-quarter starts total was 82,631 (~27,544/mo average). If June starts land near the Apr-May average (~27,700-28,000), Q2 starts would total **~83,400-83,700** — comfortably above 70K and roughly flat-to-up vs. Q1. **On a starts basis, Q2 is tracking a second consecutive >70K quarter.**
- **Filings:** 42,430 + 40,355 = 82,785 for 2 of 3 months. Extrapolated Q2 total (using Mar's 45,921 as a rough June proxy, adjusted for the recent MoM deceleration): **~118K-123K** — also tracking flat-to-up vs. Q1's 118,727.
- **REO:** 5,098 + 4,092 = 9,190 for 2 of 3 months. May's −20% MoM deceleration is a genuine directional question — if it continues, Q2 REO could come in below Q1's 14,020 (would be the first QoQ deceleration in the REO-conversion trend that CARL's thesis has been citing as "pipeline converting, not just accumulating"). **This is the one leg of the three where Q2 direction is NOT yet locked** — worth flagging to CARL as the actual open question, more than the metric-definition ambiguity itself.

---

## 3. State-level color (FL/TX, CARL's priority states)

| State | Metric | Q1 2026 | May 2026 (monthly) | Source |
|---|---|---|---|---|
| TX | FC Starts | 10,617 (#1 nationally) | 3,590 (#1 nationally, monthly) | ATTOM |
| FL | FC Starts | 10,099 (#2 nationally) | 3,315 (#2 nationally, monthly) | ATTOM |
| FL | REO | 1,014 (+108% YoY — greatest % rise nationally) | — | ATTOM |
| FL | FC Rate | 1 in 750 HU (#1 Q1) | 1 in 2,110 HU (worst rate nationally, May) | ATTOM |

---

## 4. What HOMER verified this session (2026-07-12)

- ATTOM's Q1 2026 figures (118,727 filings / 82,631 starts / 14,020 REO) were checked for internal consistency across HOMER's and CARL's own files (STATUS.md, CLAUDE.md, ROADMAP.md, CHANGELOG.md, PREDICTIONS.tsv, KB.tsv) — all consistent, no copy-drift found. The "82,631" figure is confirmed to be the **starts** count specifically, not a separate/ambiguous number.
- ATTOM's May 2026 monthly report (filings 40,355, starts 27,304, REO 4,092) was independently confirmed live via ATTOM's own published report (attomdata.com) — matches HOMER's inherited PIPELINE.tsv row exactly on the filings figure; the starts (27,304) and REO (4,092) monthly figures were pulled fresh this session and did not previously exist as national rows in HOMER's workbook (only state-level leader figures were present) — now added.
- No June 2026 monthly report exists yet as of 2026-07-12 (ATTOM's cadence runs ~11 days after month-end; June would be expected ~Jul 11-14). No confirmed Q2 quarterly report date found either — the Jul 16 docket date is a pattern-based estimate (Q1 released Apr 16, ~16 days post-quarter-end), not a confirmed press release.

---

## 5. Recommendation to CARL (data owner's observation, not a resolution call)

If CRL-06 is read on a **starts** or **filings** basis, the honest state is: **already confirmed since April 16, 2026** (Q1's release), not a Q2-forward test. Q2's ATTOM release (whenever it lands) would be a *second* confirming data point, not the first — worth clarifying in CARL's own framing since the prediction is currently carried as "OPEN, 78%, Q2 2026" as if resolution were still pending. If CRL-06 is read on a **REO/completions** basis, it remains genuinely open and the May deceleration (−20% MoM) is the one thread worth watching into June/Q2.
