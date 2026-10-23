# WQ-451 — gold: haven bid vs de-dollarisation vs liquidation — one decomposition instrument (dated letter)

**MIDAS · dated 2026-10-23 (Fri), committed 14:05:12 ET (`a35faa6f8`; times from git, an earlier narrative stamp was wrong) · commission:** PROME packet 2026-10-21 (WQ-451 RULED A, Will 2026-10-21 21:30 ET blanket word). PROME added a third case on 2026-10-23 at Will's request. **No position change.** This letter explains; it does not trade. TERRY constructs any card and Will approves it (root rule #5).
**Instrument code and outputs (frozen at this commit, before any forward grade):** `gold/sources/2026-10-23_wq451/` — `classify.py`, `forward.py`, `stress.py`, `panel.csv`, `*_output.txt`.

## 0. The short answer for Will

Over the last 120 trading sessions, **gold (GLD) has not hedged stock-market stress.** On days when the S&P 500 fell 1% or more, or the VIX rose 2 points or more, GLD rose on only **2 of 12** and averaged **−1.82%**, against the S&P's −1.34%. Over all of 2026 it rose on **6 of 24** such days and averaged −1.42%. Thursday 10/22 is the latest example: stocks fell, bonds rallied, and GLD fell 2.63% while its trust lost 12 tonnes of gold. Gold is still doing what it has done all year — **it falls when real interest rates rise, and on panic days it gets sold along with stocks.** A "haven" day has occurred only 5 times since January 2025, and the most recent was 2026-03-27, none in the last 120 sessions. **So GLD, the book's largest line, should be held as a bet on falling real rates and long-run demand for gold, not as protection for the book's stock and bank put positions on bad days.** The evidence for de-dollarisation (central-bank buying) is real, but it shows up month by month, not day by day, and it has not stopped the 2026 drawdown.

## 1. Correction to the commission's premise

The packet says the registered beta "has the wrong sign over the 9/3→10/15 window (DFII10 ~+50 bp, gold at a record)". **The data do not support that.** From the 9/3 close to the 10/15 close: DFII10 **+36bp** (FRED), GLD **−6.71%**, DXY +3.03%, GLD trust tonnage +0.43t. The beta-implied move is −5.5%, so the cumulative unexplained residual is only **−1.20%** — **the sign was right, and the beta explained most of the move.** GLD's 2026 record close was **$495.90 on 2026-01-29**, not in this window. The wrong-sign episode the fleet remembers is July–August (kill-condition #3 fire, 7/17→8/7), which is history. Flagged to PROME in the delivery packet.

## 2. The instrument

**Baseline:** the current 120-pair GLD/DFII10 beta **−0.1526% per bp** (through 10/16, R² 0.154; `analysis/2026-10-20_GLD-OUTLOOK.md`). The registered −0.16%/bp (10/8) differs by less than its standard error, so it is used only as a cross-check. Daily residual **e = GLD % change − (−0.1526 × ΔDFII10 in bp)**. The threshold K·sd uses K = 1.0 and sd = **1.402%**, the residual standard deviation over the 120 pairs ending 2026-10-21. That window excludes the graded day.

| Class | Rule (daily, all legs same-date closes) | What it means | Lower-frequency confirmation leg |
|---|---|---|---|
| **RATE** | \|e\| ≤ 1.402% | Gold moved as real yields implied | — |
| **HAVEN** | e > +1.402% AND equity stress AND DXY > −0.20% | Gold bid on fear while the dollar is not falling | GLD tonnage up on the day |
| **DE-DOLLARISATION (proxy)** | e > +1.402% AND no equity stress AND DXY ≤ −0.20% | Gold up against a weakening dollar, no panic | **Monthly:** PBoC/SAFE reserve gold change; WGC central-bank net purchases; IMF IFS; **TIC** foreign-official Treasury holdings (falling = supportive) |
| **LIQUIDATION** | e < −1.402% AND equity stress AND GLD tonnes down | Gold sold with risk assets for cash | Weekly COT net long falling; further GLD outflow |
| UNEXPLAINED-UP / -DOWN | \|e\| large, legs don't match a class | Named, not forced into a story | — |

Equity stress means S&P 500 ≤ −1.0% OR VIX +2.0 points or more. Data sources: GLD close and trust tonnes are PRIMARY from the issuer (SPDR archive). DFII10 is FRED MIRROR, with 10/22 = 2.64 taken from the PRIMARY Treasury real curve. DXY, S&P and VIX are Yahoo MIRROR.

**Base rates (2025-01-02 → 2026-10-21, 443 sessions):** RATE 312 · UNEXPLAINED-DOWN 49 · UNEXPLAINED-UP 47 · DE-DOLLAR proxy 24 · LIQUIDATION 11 · HAVEN 5. In the last 120 sessions: RATE 82 · UNEXPLAINED-DOWN 18 · UNEXPLAINED-UP 11 · DE-DOLLAR proxy 6 · LIQUIDATION 3 · **HAVEN 0**.

**Limits, stated plainly:** the beta's R² is 0.15, so about 85% of daily variance is outside the model, and most "classified" days are still noisy. The daily de-dollarisation proxy only shows that the dollar fell, not who bought the gold. Only the monthly legs can confirm official buying. Haven and liquidation have small samples (n = 5 and 11). The thresholds are design choices (1 sd, −1% S&P, +2 VIX, −0.20% DXY), fixed here and not tuned to 10/22. They have **not** been tested out of sample.

## 3. First graded case — Thursday 2026-10-22 → **LIQUIDATION**

| Leg | 10/22 | Source |
|---|---|---|
| GLD | −2.63% ($378.95 → $369.00) | PRIMARY issuer |
| ΔDFII10 | −12bp (2.76 → 2.64) | PRIMARY Treasury real curve |
| Beta-implied GLD move | **+1.83%** | −0.1526 × −12 |
| Residual e | **−4.46%** (3.2 sd) | computed |
| S&P 500 / ΔVIX | −1.21% / +2.35 | MIRROR |
| DXY | −0.17% (not ≤ −0.20) | MIRROR |
| GLD trust tonnes | **−11.98t** | PRIMARY issuer |

All three LIQUIDATION legs pass. It is the **largest** negative residual among the 12 liquidation days on file, narrowly ahead of 2026-02-12 (−4.39%) and 2026-03-03 (−4.31%). Media attributed the day to oil-driven Fed-hike bets. The **2-year Treasury fell 16bp** that day, which rules out a hawkish repricing as the driver.

## 4. Falsifiable letter — what each case predicts, and the figures that kill it

**L1 — Liquidation (10/22).** *Claim:* 10/22 was forced or risk-reduction selling, not a change in gold's long-run demand. *Falsifier, graded at the **2026-11-05 close** (10 sessions; retrieved on the next US business day, 11/06):* the claim is **FALSIFIED** if the S&P 500 closes at or above its 10/21 close **7,757.17** on any session through 11/05 **and** GLD trust tonnes on 11/05 are **≤ 1,035.64t** (another −10t or more beyond 10/22). Stress gone with outflows continuing would mean holders are leaving gold itself. If neither stress clears nor outflows continue, the result is **NOT TESTED**. The claim is **SUPPORTED** if stress clears and tonnes are ≥ 1,045.64t. *No bounce call:* after the 11 prior liquidation days, the 10-session forward residual was positive 64% of the time (mean +3.66%), the same 64% as the unconditional rate. There is no edge to sell.

**L2 — Haven.** *Claim (current):* GLD is **not** a reliable stress hedge for this book. *Falsifier:* over the **next 10 equity-stress days** after 10/22 (any date), the claim is falsified if GLD rises on **6 or more**. Baseline: 2 of 12 in the last 120 sessions, 6 of 24 in 2026. If that happens, re-run `stress.py` and report to TERRY/PROME.

**L3 — De-dollarisation.** *Claim:* official-sector buying is a monthly support that has **not** offset the 2026 rate and liquidation drawdowns. *Monthly falsifiers (supporting direction / weakening direction):*
- **PBoC (SAFE) October reserve gold, published ~2026-11-07:** ≥ +10t supports; a change of < +5t, or a pause, weakens. September was +23.02t (PRIMARY, verified 10/20).
- **TIC September, published ~2026-11-18:** foreign-official Treasury holdings falling month on month supports the de-dollarisation leg; rising weakens it. **TIC level and interpretation are ZHAO/SAM's domain.** MIDAS reads only the sign.
- **WGC October central-bank net purchases, published ~early December:** ≥ 50t supports; < 25t weakens. The quarterly 100t floor rule is unchanged.
- *Daily proxy check:* if 3 or more DE-DOLLAR-proxy days occur before 11/30 **and** tonnage rises over the same period, the daily and monthly legs agree. Otherwise they are recorded as not agreeing.

**Grading calendar:** 11/06 (L1); 11/07 (SAFE); 11/18 (TIC); early December (WGC); L2 is graded whenever 10 stress days have accumulated. PROME registers these in GATES once this letter is encoded; until then they are a MIDAS desk letter, not a registered gate.

## 5. Gap 7 — what would change the 10/20 GLD outlook (invalidation lines, not a trade recommendation)

The 10/20 outlook referenced the GLD close of **$379.69 on 10/19**. It called one month (to 11/20) neutral to slightly lower and three months (to 2027-01-20) modestly higher. Both were LOW-confidence ASSUMPTION. Registered sign calls MIDAS-11/12 resolve on their own letters, and nothing here changes them.

| Horizon | Invalidation line (any one triggers) | Current reading | Distance |
|---|---|---|---|
| 1 month, downside | GLD close **< $360.71** (−5.0% vs $379.69): the decline is no longer "slightly lower" | $366.00 intraday 10/23 (−3.6%) | ~1.5% above the line |
| 1 month, upside | GLD close **> $391.08** (+3.0%) | — | +6.9% away |
| 3 months | GLD trust **< 1,035.70t** (−20t vs the 9/30 implied 1,055.70t): the accumulation premise has failed | 1,045.64t (10/22) | 9.94t of room |
| 3 months | DFII10 **≥ 3.00%** on 5 consecutive Treasury prints: the rate-surge condition | 2.64% (10/22) | +36bp |
| 3 months | DXY **≥ 105.0** on 5 consecutive closes: the dollar-surge condition | ~101.8 | +3.1% |
| 3 months | A **second LIQUIDATION-class day** by 11/05 **and** cumulative tonnes ≤ −20t since 9/30: de-risking is continuing | first case 10/22 | — |

If any 3-month line is crossed, MIDAS withdraws the positive lean to neutral and reports it to PROME and TERRY. Note how close the one-month downside line is: **one more −1.5% day breaches it.**

## 6. What this changes and what it does not

- **No score change:** M1 stays 4 pending the $4,050 flip settle, which is UNRESOLVED (see `shared/research/2026-10-23_catch-up.md`). **No position change. No new threshold enters the composite.**
- **For TERRY (if Will asks):** the hedge question has a measured answer: GLD has not offset equity-stress days in 2026. Any card that counts GLD as protection for the QQQ/KRE put book should not count it.
- ZHAO and SAM receive a packet (de-dollarisation leg, TIC sign). BOND owns the DFII10 level.
- Prior desk work on the same question: `analysis/2026-09-11_VECTOR-3-gld-under-an-oil-shock-real-yield-regime.md` (DOCKET L327, Vector 3). This letter adds the liquidation class and the stress-day count; it does not re-grade Vector 3's historical falsifier.
