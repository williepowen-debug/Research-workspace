# September 2026 ISM Services — HENRY grade of HEN-48–56 (DOCKET L612)

**Graded:** 2026-10-08 ~08:20 EDT (HENRY, Claude Code desk spawn by PROME `prome-fc`, WQ-389). **Letter:** `research/2026-10-04_ISM-services-owner-adoption/adoption.md` (registered 2026-10-04T20:52:57-04:00, durable commit `2bb57dddb` 21:20:09 EDT). **Release graded:** ISM September 2026 Services PMI Report, scheduled and published Mon 2026-10-05 10:00 EDT.

## 1 — What was and was not prospectively registered (L612's adoption question)

| Item | Before 10:00 EDT 10/5? | Evidence |
|---|---|---|
| Owner ADOPTION of the SOL draft's macro values (6 ranges + 3 directions, HEN-48–56) | ✅ YES — ~13 h before release | Declared 2026-10-04 20:52:57 EDT; commit `2bb57dddb` 2026-10-04 21:20:09 EDT; closeout `a6d92e537` 21:27:18 EDT, on origin (PROME `owner-adoption-review.md`) |
| Market-reaction map (QQQ/SPX/2Y/10Y, 09:58→10:30 window) | ❌ NOT registered — declined as exploratory / APPARATUS-INCOMPLETE | adoption.md § Market route feasibility: no certified capture route; no timer installed |
| Probabilities / confidence coverage | ❌ none (judgmental ranges; `Confidence = UNASSIGNED`) | PREDICTIONS.tsv rows |
| Any amendment after 10/4 21:20 | ❌ none — nothing adopted, amended or registered after release | `git log` on the letter dir and PREDICTIONS.tsv: last write is `2bb57dddb`; `a6d92e537` touched only LAST_COMPLETION + the PROME memo; every later commit under `AGENTS/HENRY/` is another desk's inbox delivery |

**L612 outcome, in its own terms:** the letter's adoption branch was taken prospectively; the no-retroactive-adoption clause was **not engaged** (nothing was adopted after 10:00 EDT 10/5). The market map was **never registered**, so it has no grade — §4 records observations only.

## 2 — First-published values (primary)

ISM's own report PDF `rain202609svcs.pdf` (ismworld.org), retrieved 2026-10-08 12:16:51Z, sha256 `a953539c…8c74`, metadata ModDate 2026-09-30 (before release). Text extract and provenance are in this directory. Corroborated by investingLive at 14:04 GMT 10/5 (10:04 EDT), with all six graded values identical. ISM's HTML report page returned a reCAPTCHA wall and was not read.

| Series | Sep (first print) | Aug | Δ | ISM note |
|---|---|---|---|---|
| Services PMI | **54.9** | 55.4 | −0.5 | 27th month of expansion; 0.8 over its 12-mo avg 54.1 |
| Business Activity | **56.5** | 61.7 | −5.2 | |
| New Orders | **59.8** | 60.9 | −1.1 | |
| Employment | **50.1** | 47.8 | +2.3 | Back in expansion for the first time in three months |
| Supplier Deliveries | **53.2** | 51.3 | +1.9 | Slower deliveries (22nd month) |
| Prices | **74.0** | 72.6 | +1.4 | Highest since July 2022 (74.5); >70 for 6 of 7 months |
| *not graded:* Inventories 57.8 · Backlog 56.6 · New Export Orders 46.9 (−9.4) · Imports 52.9 | | | | |

Consensus: 55.7 (adoption-recorded, single weak calendar source); other secondaries say 55.0 (TradingEconomics) and 55.2 (investingLive). The headline came in under all three, so the size of the miss depends on whose consensus you use.

## 3 — Grades (mechanical, computed from the letter; Decimal arithmetic, published tenths)

| ID | Claim | Actual | Grade | Signed err (act−central) |
|---|---|---|---|---|
| HEN-48 | headline ∈ [54,58], c 56 | 54.9 | ✅ **HIT** | −1.1 |
| HEN-49 | employment ∈ [47,52], c 49.5 | 50.1 | ✅ **HIT** | +0.6 |
| HEN-50 | prices ∈ [70,78], c 74 | 74.0 | ✅ **HIT** | 0.0 |
| HEN-51 | business activity ∈ [58,64], c 61 | 56.5 | ❌ **MISS** (1.5 below the floor) | −4.5 |
| HEN-52 | new orders ∈ [58,65], c 61.5 | 59.8 | ✅ **HIT** | −1.7 |
| HEN-53 | supplier deliveries ∈ [50,55], c 52 | 53.2 | ✅ **HIT** | +1.2 |
| HEN-54 | headline > 55.4 | 54.9 | ❌ **MISS** (−0.5) | — |
| HEN-55 | employment > 47.8 | 50.1 | ✅ **HIT** (+2.3) | — |
| HEN-56 | prices ≥ 70.0 | 74.0 | ✅ **HIT** (+4.0) | — |

**Tally:** ranges 5/6 HIT; directions 2/3 HIT; mean absolute range error 1.52 points. Component bridge (activity + orders + employment + deliveries)/4 = **54.9 = the headline exactly**, so the 4-component arithmetic held and the error is in the components.

**What the grade says (interpretation, separate from the grade):**
- The **hiring catch-up** call landed: employment 50.1, a direction HIT with a 2.3-point margin. That was the forecast's distinctive claim against soft BLS jobs.
- The **activity** call failed: −4.5 vs central and outside the range. It leaned on S&P's flash ("fastest growth for over five years"), and ISM activity instead fell 5.2. This one miss also decided HEN-54: the headline went down, not up.
- **Prices** came in exactly at central. Cost pressure is the most robust leg (74.0, the highest since July 2022).
- ⚠️ **5/6 is weak evidence of skill.** The ranges were 4–8 points wide, and the same ranges would have contained **17 of 24** prior month-cells (May–Aug, as carried in the August release: headline 4/4 · employment 4/4 · prices 3/4 · activity 2/4 · orders 1/4 · deliveries 3/4; forecast.json). The informative outcomes are the two misses and the employment direction.

## 4 — Timing disclosure: graded after the CHOSEN deadline

The letter chose **2026-10-05 16:00 EDT** as the same-day grading deadline ("cannot silently extend"). This grade is **~64 hours late**: no automatic wake existed, and HENRY was dark until PROME's WQ-389 wake. **This is disclosed here, not silently extended.**
- The letter's NO-VERDICT conditions are *no publication by deadline · wrong month · missing series · ambiguous first vintage*. None applies: the release was published at 10:00 EDT 10/5, inside the window, and the first vintage is fixed by the pre-release PDF plus the 10:04 EDT corroboration. Only the 10/5 first print is used; no later vintage is admitted.
- ⚠️ **Named ambiguity:** the non-owner review wrote *"NO-VERDICT if a qualifying first print cannot be established by deadline"*. Read as **evaluator-timing**, that clause would make all nine rows NO-VERDICT. I read it as **publication-timing**, consistent with the letter's own list. That reading is mine, and the grades above depend on it. If PROME or a reader rules otherwise, all nine flip to NO-VERDICT, and this record keeps the observed values either way.

## 5 — Market-reaction OBSERVATIONS (unregistered map ⇒ NOT a grade; recorded separately as the letter requires)

⚠️ Basis: yfinance 1-minute bars pulled 2026-10-08 08:17 EDT. The bar labels are **not certified observation times** (adoption.md § Market route); vendor index/ETF bars, not exchange prints. Descriptive only.

| Instrument | 09:59 bar close | 10:00 bar close | 10:05 | 10:30 close | 09:59→10:30 |
|---|---|---|---|---|---|
| SPX (^GSPC) | 7,736.21 | 7,729.80 (−0.08%) | 7,741.54 | 7,752.20 | **+0.21%** |
| QQQ | 751.74 | 751.05 (−0.09%) | 751.82 | 753.12 | **+0.18%** |
| 10Y (^TNX index) | 5.307 | 5.307 | 5.296 (−1.1bp) | 5.311 | **+0.4bp** (dip fully round-tripped) |
| TLT | 77.02 | 77.02 | 77.15 (+0.17%) | 77.01 | −0.01% |

Daily, 10/2 → 10/5 closes: SPX 7,722.72 → 7,773.95 (+0.66%) · QQQ +0.88% · RSP +0.66% · KRE −0.55% · TLT −0.48% · Treasury par 2Y 4.83 → 4.84 · 10Y 5.28 → 5.31 · 30Y 5.63 → 5.66 · 30Y real 3.34 → **3.37**.

**Reading (observational):** the headline miss produced a ~1bp yield dip and a −0.08% equity blip, both reversed within 30 minutes. Over the day, yields rose 3bp at 10Y while equities rallied, which fits the hawkish components (prices 74.0, employment >50) outweighing the soft headline. One release cannot attribute this; the day also carried other flows. ⚠️ yfinance's 10/2 SPX close now reads 7,722.72, against 7,722.93 pulled 10/2 16:01 ET: a vendor bar revision of 0.21 pt.

## 6 — Consequences

None to any gate, threshold, capital line or existing letter; the rows themselves carried none. HEN-48–56 → RESOLVED in `workbook/PREDICTIONS.tsv`. Revision watch per the letter: the January 2027 seasonal-factor publication annotates history and never re-grades this first print.
