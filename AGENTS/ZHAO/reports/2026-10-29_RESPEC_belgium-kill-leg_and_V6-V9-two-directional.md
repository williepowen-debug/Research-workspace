# RE-SPEC — thesis-kill Belgium leg · Vectors 6 & 9 two-directional (2026-10-29, Will-approved desk sweep step 4)

Written OUTSIDE the letter that graded the old leg (ZHA-18, graded 10/16), per KB-159. Data: TIC Table 3 (slt_table3.txt, pulled 2026-10-29); the CFETS USD/CNY central-parity series from chinamoney.com.cn (primary; 925 fixings 2023-01-03 → 2026-10-29, fetched in paced quarterly requests); USD/CNY market close from yfinance CNY=X. Series saved: `reports/2026-10-29_fixgap_series.csv`.

## 1. Thesis kill — the Belgium leg is RETIRED and replaced by a China flow leg

**Old letter (in force 2026-03 → 2026-10-29):** *Belgium <10% YoY for 2 prints AND China >$700B for 3 prints* · *fiscal >5% GDP with LGFV full backstop.*

**Why the Belgium leg goes:** it carries no information about China. rho(China, Belgium net sales) = +0.067, n=43 (VX-ZHAO-1.09; proxy falsified 8/21). Its YoY form also fires on its own base: KB-159, the Aug print was SATISFIED-ON-BASE-EFFECT. A kill leg must separate the "China selling" state from the "not selling" state, and this one separates nothing. The Aug-26 tally ("1 of 2") is VOID. It is not carried into the new leg.

**New letter — the thesis "China is a persistent net seller of Treasuries" is KILLED only when ALL of the legs below are met:**

| Leg | Instrument | Fires when | Status 10/29 |
|---|---|---|---|
| **F (flow, NEW)** | China, Mainland, TIC Table 3 `for_treas_net` (total incl. bills, $M), **summed over the trailing 6 reference months**. Each month is taken **as first published** in the release that first carries it; later revisions are noted and never re-grade (FROZEN-ON-REVISABLE, WQ-175). | the 6-month sum is **≥ +$2,000M on 2 consecutive monthly releases**. A sum in **[−$2,000M, +$2,000M)** is NO-VERDICT and **resets** the count; a sum **< −$2,000M** is non-qualifying and resets the count. Ties: integer $M, so +2,000 exactly qualifies. | **−$71.5B (Aug-26)**: far |
| **L (level, wording clarified)** | China, Mainland holdings, TIC Table 5 / Table 3 `for_treas_pos` | **> $700.0B on 3 CONSECUTIVE releases**. The old text said "3 prints"; the stricter, consecutive reading is adopted here. | **$590.7B**: far |
| **S (fiscal, unchanged)** | NPC / MoF official figures | stimulus > 5% of GDP with a full LGFV backstop | not met |

**Base rate of leg F (2023-02 → 2026-08, n = 38 six-month windows):** the sum was ≥ +$2,000M **once** (Feb-2025, +$5.0B) and **never on 2 consecutive releases**. Leg F therefore very rarely false-fires inside a selling regime. ⚠️ **Limit:** the whole sample sits inside the selling regime, so the leg's *hit rate* in a genuine regime change is **unmeasured**. It is specified to the mechanism (selling stops), not fitted to a past ending. With n = 38 overlapping windows, the effective sample is far smaller (`finding_overlapping_window_inflates_the_base_rate`).

**Belgium afterwards:** FYI level only, as before. Belgium returns as evidence **only** if rho < −0.5 on a rolling 24 months (VX-ZHAO-1.09) **and** a fresh registration is made. It is never automatically restored to the kill.

## 2. Vectors 6 & 9 — two-directional

**Problem (KB-168, 9/18):** both vectors measured defence against DEPRECIATION only, so they read 🟢 1 whether the PBOC was idle or actively holding back a rising yuan.

### Vector 6 — PBOC currency-management intensity → `VX-ZHAO-2.10`
- **Instrument:** g20 = the 20-fixing mean of (CFETS fix ÷ prior-day USD/CNY market close − 1), in %. **Sign: + = fix set WEAKER than the market** (resisting appreciation, tag **A**). **− = fix set STRONGER** (defending against depreciation, tag **D**).
- **Score by |g20|:** <0.25 → 1 · 0.25–0.50 → 2 · 0.50–1.00 → 3 · 1.00–1.50 → 4 · ≥1.50 → 5.
- **Base-rate shares, 2023-02 → 2026-10 (n ≈ 900):** 34% / 21% / 18% / 14% / 14%.
- **History:** 2024 mean −0.89 (D), low −1.89 on 2024-07-12. 2026 mean +0.46 (A), **record A +0.90 on 2026-09-17**. Positive in every month since Dec-2025.
- **Now: g20 = +0.519 ⇒ 3·A.** ⚠️ **This sits 0.019 points above the 2/3 line, inside the market-leg noise:** 91 of 922 vendor closes are stale repeats. Read it as "2–3·A", direction solid.

### Vector 9 — USD/CNY pressure → `VX-ZHAO-2.11`
- **Instrument:** c60 = % change of the CFETS fix over 60 fixings (primary series, no vendor leg). **− = yuan appreciating (A). + = depreciating (D).**
- **Score by |c60|:** <1 → 1 · 1–2 → 2 · 2–3 → 3 · 3–4 → 4 · ≥4 → 5.
- **Base-rate shares:** 62% / 24% / 10% / 2% / 2%.
- **Now: c60 = −1.11% ⇒ 2·A.**
- **Unchanged:** the 7.30 depreciation route to HENRY/LIQUID (CLAUDE.md signal table, `VX-ZHAO-2.01`).

### How the vectors enter the 28/60 total (a design choice — flagged to Will)
The convergence total measures transmission of **China UST-selling stress**. **D-side** management (selling dollars to hold the yuan up) is that stress. **A-side** management means the state is accumulating dollars, which is the opposite sign for the selling thesis. ⇒ **The total counts the D-side score only. An A-side score is shown, e.g. "3·A", and NOT added.** So the total stays 28 today. A two-sided shadow total is shown beside it (28 + 2 + 1 = **31**).

⚠️ **A-side intensity still matters, through a different channel:** a record fix-weaker-than-market streak alongside a ~$1T trade surplus is the textbook currency-manipulation grievance. That is **trade-war fuel (HAWK/HENRY), not UST-selling stress.** It is stated here as a channel, not measured.

## 3. Owed after this
- A primary market leg for g20 (the CFETS 16:30 close) to replace the stale-prone yfinance close.
- Add the fix pull to boot.py (one paced request per boot).
- CLAUDE.md charter text for V6/V9 is untouched: the charter sits 25 B under its cap.
