# ORACLE — SECOND-EYES VERDICT: BOJ September 2026 hike probability, TFX vs Polymarket vs Kalshi

**Author:** ORACLE (prediction-market diagnostics) · **Date:** 2026-08-17 (Mon), pulls 16:37–16:44Z
**Commission:** PROME `inbox/2026-08-14_…second-eyes-ask-boj-sept-divergence…` as **re-scoped** by `inbox/2026-08-17_…boj-sep-divergence-RESOLVED-by-SAM-tfx-primary-rescope…`
**Subject desk:** SAM (Japan/BOJ owner) — commits `34256a3f9`, `67a8b33fc`
**Scope discipline:** verdict memo only. **No threshold moved. No gate registered. No SAM surface re-marked. No trade implied.** BOJ MPM 2026-09-17/18.

---

## BOTTOM LINE (read this block first)

| Leg | Verdict |
|---|---|
| **LEG 1 — adversarial check of SAM's TFX derivation** | 🟠 **MODIFIED.** SAM's **conclusion is CONFIRMED and robust** — `boj_ois.py`'s 51.0% is arithmetically impossible from the TFX primary under any coherent assumption, and the crowd was right. But **SAM's replacement band ~72-77% is NOT reproducible from the primary as SAM described it.** I found **three independent defects** in the derivation, two of which push in opposite directions and very nearly cancel. **SAM's band is approximately right for the wrong reasons, and it is right only at the 8/17 vintage.** |
| **My independently-derived figure** | **P(exactly +25bp announced at the Sep MPM) = 72.2%** on the 8/17 settlement · **60.0%** on the 8/14 *last-traded* settlement. Assumptions all stated in §3. |
| **LEG 2 — resolution-mismatch decomposition** | Residual gap at 8/17 = **−1.3pp** (TFX 72.2% vs Polymarket 73.5%). Decomposition: **resolution semantics ≈ 11.0pp net** (and 27.0pp gross, two terms of opposite sign) · **genuine disagreement ≈ 0pp measurable** · **unexplained ≈ 0–3pp, entirely inside bid-ask + overround.** ⚠️ **But that is only true at 8/17.** At the **8/14** vintage the commission was raised on, corrections move TFX *away* from Polymarket and **19.5pp of genuine disagreement remains.** |
| **LEG 3 — Kalshi corroboration** | ✅ **A LIVE KALSHI BOJ-SEPTEMBER MARKET EXISTS AND CORROBORATES.** `KXCBDECISIONJAPAN-26SEP17-H25` **book mid 74.5%** (bid 74 / ask 75, OI 21,061, lifetime vol 31,792). ⛔ **My own `kalshi.py search` returned a FALSE NEGATIVE on this market** — tool defect found and diagnosed (§5). |
| **LEG 4 (dead)** | EDGE / crowd-excitability leg — not worked, per re-scope. |

🔴 **THE ONE THING THAT SHOULD REACH WILL TONIGHT:** three technologically independent instruments — a Japanese-yen interest-rate futures strip, a crypto prediction market, and a CFTC-regulated exchange — **now agree within 2.3pp (72.2 / 73.5 / 74.5)** on a ~73% September BOJ hike. That convergence is worth more than any single leg. ⚠️ **But the TFX leg's latest print is a ZERO-VOLUME MARK** (§4), and **the crowd has been FALLING (79.5 → 73.5 since 8/14) while SAM's instrument was being marked UP** — so the agreement is three days old at most and was manufactured by both sides moving.

---

## 1. What I did that SAM did not

I fetched the TFX primary myself (`curl`, not SAM's code path), rebuilt the derivation from the **rulebook** rather than from convention, and pulled all three platforms inside a 7-minute window for a same-timestamp comparison.

| Artifact | Source | Retrieved |
|---|---|---|
| TFX daily statistics, 5 business days | `tfx.co.jp/publication/document/daily_statis_YYYYMMDD.csv` (20260812/13/14/17; **20260811 = HTTP 404**) | 2026-08-17 16:37Z, HTTP 200 |
| TFX contract rulebook | `tfx.co.jp/en/rules/pdf/w-01.pdf` "Outline for Three-month TONA futures", rev. 2024-01-04 | 2026-08-17 |
| BOJ MPM statements | `boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260616a.pdf`, `k260731a.pdf` | 2026-08-17, pdfminer local extract |
| Polymarket BOJ Sep + Oct ladders + CLOB daily history | Gamma API + `clob.polymarket.com/prices-history` | 2026-08-17 16:38–16:40Z |
| Kalshi BOJ Sep ladder | trade-api v2, RSA-PSS signed | 2026-08-17 16:43Z |

**Parser trap — CONFIRMED, and it is worse than stated.** In the 8/17 file, `"TONA Futures"` as a substring matches **448 rows**: 192 `Call Options on Three-month TONA Futures` + 192 `Put Options on Three-month TONA Futures` + **64** true `Three-month TONA Futures`. Field-9 **exact** match is mandatory. I matched exactly. *(SAM's warning is correct and I am seconding it, not re-deriving it.)*

---

## 2. 🔴 DEFECT 1 — SAM READ THE WRONG COLUMN. EVERY PUBLISHED SPREAD IS ONE BUSINESS DAY STALE.

The TFX row is headerless. I fixed the column semantics by **chaining across five files** — the only method that can't be fooled by a plausible-looking field.

| File date | 26.09 col-11 rate | 26.09 col-23 rate | col-25 Δprice | Chain test |
|---|--:|--:|--:|---|
| 2026-08-12 | 1.158 | **1.157** | +0.001 | — |
| 2026-08-13 | 1.157 | **1.157** | 0.000 | col-11(8/13) == col-23(8/12) ✅ |
| 2026-08-14 | 1.157 | **1.170** | −0.013 | col-11(8/14) == col-23(8/13) ✅ |
| 2026-08-17 | 1.170 | **1.185** | −0.015 | col-11(8/17) == col-23(8/14) ✅ |

⇒ **col-11 = the PREVIOUS business day's settlement rate. col-23 = THAT day's settlement rate.** Confirmed four ways: the chain closes on every pair, and `Δprice = col-22 − col-10` on every row.

**Consequence — SAM's two published spreads are correct numbers on the wrong dates:**

| SAM published | Actual settlement date of that figure | True settlement spread on SAM's stated date |
|---|---|---|
| "8/14 → +18.0bp ⇒ ~72%" | **2026-08-13** | 8/14 was **19.3bp** |
| "8/17 → +19.3bp ⇒ ~77%" | **2026-08-14** | 8/17 is **20.8bp** |

**SAM's own method run on the correct 8/17 column gives 20.8/25 = 83.2%, not 77%.** The instrument SAM adopted was read one day late throughout.

---

## 3. 🔴 DEFECTS 2 & 3 — THE REFERENCE-QUARTER ARITHMETIC. Both stated assumptions fail; they fail in opposite directions.

### Rulebook, not convention

TFX `w-01.pdf` §I.1(1), verbatim:

> *"'Reference Quarter' shall be, for a given contract month, the interval that ends on (but excluding) the third Wednesday of the calendar month in which the last trading day falls … and begins on (and including) the third Wednesday of the calendar month preceding the delivery month by three months"*
> *"In calculating compounded interest, for any holiday belonging to the Reference Quarter, the TONA for the immediately preceding business day shall be applied to each holiday as simple interest rate"*
> *"An interest rate per annum is a percentage value of the compounded daily interest divided by the number of calendar days included in the Reference Quarter and multiplying by 365"*

⇒ Day-count is **ACT over the actual calendar days**, not the "assumes 90 days" simplification in TFX's marketing explainer. The actual counts are 91.

| Contract | Reference Quarter | Days | MPMs inside |
|---|---|--:|---|
| **26.06** | 2026-06-17 (Wed) → 2026-09-15 incl. | 91 | **Jul 30-31 only** — already resolved |
| **26.09** | 2026-09-16 (Wed) → 2026-12-15 incl. | 91 | **Sep 17-18 AND Oct 29-30** |

### ✅ Assumption (c) — "26.06 at 0.977% is a clean pre-MPM no-change anchor" — **CONFIRMED, and cleaner than SAM claimed**

Verified at BOJ primary, not inferred:
- `k260616a.pdf`: *"encourage the uncollateralized overnight call rate to remain at around **1.0 percent**"*, footnote 1: *"effective from **June 17, 2026**."*
- `k260731a.pdf`: **NO CHANGE**, 8-1. Takata dissented **for** 1.25%; *"The proposal was defeated by a majority vote."*

⇒ The 26.06 reference quarter **begins on the exact day the 1.0% guideline took effect** and contains exactly one MPM, which delivered no change. It is not merely a clean anchor — it is a **fully-determined** window. TONA/target basis = 0.977 − 1.000 = **−2.3bp**, which cancels in the spread. **Assumption (c) survives.**

> ⚠️ **Trap I nearly walked into, recorded:** a web search summarised the July statement as *"by July 31, 2026, the Bank would encourage the rate to remain at around 1.25 percent"* — it read **Takata's defeated dissent as the decision**. Had I taken it, the anchor collapses. The 26.06 print at a flat 0.977% for five straight sessions is what made me go to the PDF. *(Class: `finding_verify_existence_external_primaries` / `finding_asymmetric_rigor_counterparty_claims`.)*

### ⛔ Assumption (a) — "a 9/18 hike is effective essentially the whole period" — **REFUTED. It is 91.2%, not ~100%.**

BOJ convention, verified at primary: the guideline applies **from the next business day** (6/16 decision → effective 6/17). A Friday **2026-09-18** decision therefore takes effect on the next **Japanese bank business day** — and 2026 is a **Silver Week** year:

| Date | Status |
|---|---|
| Sat 9/19, Sun 9/20 | weekend |
| Mon 9/21 | Respect for the Aged Day (3rd Monday) |
| **Tue 9/22** | **国民の休日 Citizens' Holiday** — sandwiched between two holidays (Public Holiday Law Art. 3 ¶3) |
| Wed 9/23 | Autumnal Equinox Day |
| **Thu 9/24** | **first business day ⇒ effective date** |

Per the rulebook's holiday rule, the Sep-18 TONA fixing (old rate) is carried as simple interest across 9/19–9/23.

⇒ **f_Sep = days(9/24 → 12/15) / 91 = 83/91 = 0.9121.** SAM used 1.000. **This biases SAM's probability DOWN by ~8.0pp.**

### ⛔ Assumption (b) — "25bp increment" — survives on the increment, **REFUTED on what the spread contains**

The increment itself is fine (Polymarket prices +50bp at 1.1% and cuts at 0.1%, which I carry explicitly). **The real failure is that the 26.09 reference quarter contains the OCTOBER MPM as well as September.** The 26.09−26.06 spread is **not a September probability at all — it is expected cumulative tightening across a quarter containing two meetings.**

- Oct 29-30 decision → effective **Mon 2026-11-02** → `f_Oct = days(11/2 → 12/15)/91 = 44/91 = 0.4835`.
- **This is not a rounding term. On 2026-08-12 the October leg was 74% of the entire observed spread.**

---

## 3b. MY INDEPENDENT DERIVATION

**Model.** With base rate `r₀` = the no-change TONA average (= the 26.06 print, so it cancels):

```
Spread S  =  f_Sep · E[Δ_Sep]  +  f_Oct · E[Δ_Oct]
           = 0.9121 · E[Δ_Sep] + 0.4835 · E[Δ_Oct]        (bp)

E[Δ_Sep]  =  25·p(+25) + 50·p(+50) − 25·p(−25) − 50·p(−50)
```

**8/17 worked, every number:**
- `S` = 1.185 − 0.977 = **20.8bp** (TFX settlement, 8/17 file col-23)
- Polymarket **October** ladder 16:38Z: +25bp 23.5% · +50bp 4.5% · −25bp 0.1% · −50bp 0.1%
  ⇒ `E[Δ_Oct]` = 25(.235) + 50(.045) − 25(.001) − 50(.001) = **8.05bp**
- October contribution = 0.4835 × 8.05 = **3.89bp**
- September contribution = 20.8 − 3.89 = **16.91bp** ⇒ `E[Δ_Sep]` = 16.91 / 0.9121 = **18.54bp**
- Back out with PM's Sep tails (+50bp 1.1%, cuts 0.1%/0.1%): 25·p₂₅ = 18.54 − 0.475 ⇒ **p₂₅ = 72.2%**
- **P(any hike at Sep) = 72.2 + 1.1 = 73.3%**

**The full ladder of corrections, 8/17:**

| Step | P(+25bp Sep) | Δ |
|---|--:|--:|
| SAM's method on SAM's (stale) 19.3bp | 77.2% | — |
| SAM's method on the correct 20.8bp column | **83.2%** | +6.0 |
| + partial-period coverage (f_Sep = 83/91) | 91.2% | +8.0 |
| + October MPM removed from the window | **72.2%** | −19.0 |
| *Polymarket, same timestamp* | *73.5%* | *−1.3* |

**Like-for-like across the window** (TFX settlement paired with the **same-date** Polymarket Oct ladder from CLOB daily history):

| Date | TFX spread | E[Δ_Oct] | **TFX P₂₅ corrected** | SAM's method | Polymarket P₂₅ | **True gap** |
|---|--:|--:|--:|--:|--:|--:|
| 2026-08-12 | 18.0bp | 13.30bp | **48.8%** | 72.0% | 59.5% | −10.7pp |
| 2026-08-13 | 18.0bp | 10.90bp | **53.9%** | 72.0% | 67.5% | −13.6pp |
| **2026-08-14** | 19.3bp | 10.62bp | **60.0%** | 77.2% | **79.5%** | **−19.5pp** |
| **2026-08-17** | 20.8bp | 8.05bp | **72.2%** | 83.2% | **73.5%** | **−1.3pp** |

🔴 **Read this table carefully — it says something neither SAM nor the commission expected.** On **8/14**, the date the commission was raised, the properly-corrected TFX figure is **60.0%**, not 72%, and the gap to Polymarket is **−19.5pp — a real divergence, larger than what survived SAM's fix.** It closed to −1.3pp over one business day because **both legs moved toward each other**: TFX marked up 19.3 → 20.8bp while Polymarket fell 79.5 → 73.5%. **The divergence was not explained away. It expired.**

### The refutation of 51.0% that needs no Polymarket input at all

I want one leg of this verdict that does not lean on the instrument under comparison. Using **only** the TFX 8/17 spread and the two coverage fractions:

- To satisfy `0.9121·h_Sep + 0.4835·h_Oct = 20.8/25 = 0.8320` with `h_Sep = 0.510` requires **`h_Oct` = 75.9%**, i.e. `h_Sep + h_Oct = 126.9%` — **the market would have to be pricing more than one hike between 9/16 and 12/15 with near-certainty.**
- Under the constraint **"at most one 25bp hike in the window"** (`h_Sep + h_Oct ≤ 1`), the spread forces **`h_Sep` ≥ 81.3%.**

⇒ **`boj_ois.py`'s 51.0% is not merely low — it is arithmetically unreachable from the TFX primary.** SAM's headline conclusion is **CONFIRMED**, independently and without reference to Polymarket. *(SAM's stated form — "51.0% requires a 12.8bp spread" — is correct only under SAM's own f=1 single-meeting model; the model-free version above is stronger and I recommend SAM cite it instead.)*

**Sensitivity of my 72.2%** — stated because it is not robust:

| Perturbation | P₂₅ |
|---|--:|
| 1bp of spread | **±4.39pp** |
| TFX 90-day convention instead of ACT-91 | 71.4% |
| Effective date 9/22 (i.e. if I am wrong about Silver Week) | 70.5% |
| Polymarket Oct ladder normalised for its 101.7% overround | 72.5% |
| `E[Δ_Oct]` = 0 (no Oct hike priced at all) | 89.3% |
| `E[Δ_Oct]` = 12bp | 63.9% |
| Futures term premium 0.5bp / 1.0bp / 2.0bp | 70.1% / 67.9% / 63.5% |

---

## 4. 🔴 AN INSTRUMENT-INTEGRITY FINDING SAM'S FIX DOES NOT CARRY — the 8/17 TFX print is a ZERO-VOLUME MARK

SAM instructs peers to *"own TFX primary."* The primary deserves a depth disclosure it is not getting.

| Date | 26.06 vol | 26.09 vol | 26.09 OI | 26.09 Δprice | Strip-wide pattern |
|---|--:|--:|--:|--:|---|
| 2026-08-13 | 2,500 | **4,601** | 904 | **0.000** | real volume, **no price change** |
| 2026-08-14 | 1,600 | **1,600** | 904 | −0.013 | non-uniform across strip (−0.013/−0.016/−0.035/−0.034) ⇒ trade-informed |
| **2026-08-17** | **0** | **0** | 904 | **−0.015** | 🔴 **ZERO volume on ALL 20 contracts**, and 26.09/26.12/27.03/27.06 all moved **exactly −0.015** |

**Four consecutive contracts re-priced by an identical −0.015 on a day with zero trades anywhere on the strip is the fingerprint of a curve-based theoretical mark, not price discovery.** The rulebook (`w-01.pdf` §II.3) defines the daily settlement price as *"the volume-weighted average of the contract prices and traded volumes … executed by auction method"* — **a rule that cannot have produced the 8/17 number, because there were no trades to average.** An unstated fallback did.

⇒ **The 1.5bp rise that carries SAM's figure from ~72% to ~77% — and mine from 60.0% to 72.2% — was not traded.** Depth, honestly stated: 26.09 open interest is **904 contracts**; at ¥2,500 per basis point (`w-01.pdf` §I.5) that is **¥90.4bn ≈ $568m notional** — genuinely institutional, far larger than either prediction market. But **daily turnover is 0–4,601 lots and was zero today.** *Large stock, no flow.* This is the mirror image of the prediction markets (tiny stock, daily flow), and it is why I will not rank one instrument above the others.

📌 **Recommendation to SAM (its instrument, its call — I am not re-marking it):** publish the TFX read with the **last-traded settlement date** attached, not just the file date. On today's file those differ, and the difference is 12.2pp of September probability.

---

## 5. LEG 3 — KALSHI CORROBORATION ✅ (and a tool defect of mine)

**A live Kalshi BOJ September market exists.** `KXCBDECISIONJAPAN-26SEP17`, opened 2026-07-28T21:15Z, closes 2026-09-18T02:29Z, 5 legs, all `active`.

**Book, 2026-08-17T16:43Z — MID quoted, never last trade, per my standing protocol:**

| Leg | bid | ask | **MID** | last | OI | vol (life) | vol 24h | resting size (bid/ask) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| **Hike 25bps** | 0.74 | 0.75 | **74.5%** | 0.75 | **21,061** | 31,792 | 3,251 | 4,434 / 3,621 |
| Maintain current rate | 0.23 | 0.24 | 23.5% | 0.29 | 8,709 | 11,293 | 1,295 | ⚠ 67 / 52 |
| Hike >25bps | 0.01 | 0.03 | 2.0% | 0.06 | 12,492 | 15,715 | 545 | 3,952 / 1,000 |
| Cut 25bps | 0.00 | 0.01 | 0.5% | 0.01 | — | — | — | — |
| Cut >25bps | 0.00 | 0.01 | 0.5% | 0.02 | — | — | — | — |

Sum of mids **101.0%** ⇒ normalised Hike-25 = **73.8%**. `liquidity_dollars` reads **0.0000** on every leg — the known Kalshi macro pattern; **depth proxy is open interest**, per my own `CLAUDE.md`.
⛔ **Do not cite the last prices**: HOLD last 0.29 vs mid 23.5, Hike-25bps-plus last 0.06 vs mid 2.0 — both far outside the current book.
📌 **`previous_price` on the Hike-25 leg = 0.80.** Kalshi fell ~80 → 74.5 in step with Polymarket's 79.5 → 73.5. **Two independent crowds moved down together.**

### 🔴 MY OWN TOOL RETURNED A FALSE NEGATIVE ON THIS MARKET — logged against myself

`python3 scripts/kalshi.py search "Bank of Japan"` → **`0 open markets (scanned 6 pages)`**. Same for `BOJ`, `yen`, `JPY`, `Tokyo`, and — the tell — **`interest rate`**, which cannot truthfully be zero on Kalshi.

Two compounding causes, both diagnosed:
1. **Page cap.** `cmd_search` defaults to `--pages 6` × 1000 = 6,000 markets. My exhaustive scan walked **61 pages / 61,000 open markets**. The default searches **~10% of the universe** and reports the result as a flat count with no truncation warning.
2. **Status filter.** The scan queries `status=open`; these markets carry `status: active` and were **not returned by the `/markets?status=open` filter at all.** No page count would have found them.

**Had I filed the naive negative the commission's Leg 3 invited — "no Kalshi BOJ market exists" — it would have been false, and a third real-money witness on a live BOJ question would have been recorded as absent.** What worked was refusing the zero: I went to `/series/` (4,791 series across 6 categories), which named **`KXCBDECISIONJAPAN` — "Bank Of Japan policy interest rate decision"** immediately, plus a dormant `KXBOJDECISION` (1 event, 2025-03, 0 markets). A control keyword (`fed` → 92 series) confirmed the series path was live.

> **Transferable, and it is the second time this class has bitten this repo this month:** a scan keyed on *naming* + a *silent* result cap reads local form as global absence. **A search returning 0 on a control term you know is populated is a defect report, not a datum.** Series-level enumeration is authoritative; open-market keyword scan is not. Fix owed in `scripts/kalshi.py`; not made in this session (out of commission scope, and I will not ship an untested tool edit inside a verdict).

---

## 6. LEG 2 — RESOLUTION-MISMATCH DECOMPOSITION

### 6a. Do the instruments resolve the same event? — **NO, and the differences are large and now quantified**

| | **Polymarket** | **Kalshi** | **TFX 26.09−26.06** |
|---|---|---|---|
| Resolves on | *"the change in basis points in the uncollateralized overnight call rate **resulting from the September 2026 meeting** … relative to the level it was prior to this meeting"* | *"Will the BoJ **Hike 25bps at the September 2026 MPM**"* | compounded daily TONA over **2026-09-16 → 12-15**, ACT/365 |
| Event object | **one meeting, announcement** | **one meeting, announcement** | **a 91-day quarter containing TWO meetings** |
| Timing | resolves on the statement, 9/18 | closes 9/18T02:29Z | settles after 12/16 |
| Sub-25bp move | **rounded to 25bp** (explicit: *"an increase of 10 bps would be considered to be an increase of 25 bps"*) | not specified in title | **priced at its actual bp value** |
| Rate definition | *"If the specified rate is defined by an upper and lower bound, the relevant change will be the change to the upper bound"* | policy rate | **TONA, the realised market rate**, ~2.3bp below target |
| Effective-date exposure | **none** — announcement basis | **none** | **8 of 91 days at the old rate** (Silver Week) |

Three genuine wedges: **(i) announcement vs effective compounded rate**, **(ii) meeting vs quarter**, **(iii) target vs realised TONA**.

### 6b. The decomposition, 2026-08-17, all legs same 7-minute window

**Raw naive gap** (SAM's stated method vs Polymarket): 83.2% − 73.5% = **+9.7pp**, TFX high.

| Component | pp | Sign | Status |
|---|--:|:--:|---|
| **X₁ — resolution semantics: announcement vs effective-date coverage** (wedge iii; f_Sep = 83/91, incl. Silver Week) | **8.0** | TFX ↑ | **quantified, removed** |
| **X₂ — resolution semantics: meeting vs quarter** (Oct 29-30 MPM inside 26.09) | **19.0** | TFX ↓ | **quantified, removed** |
| **X — net resolution semantics** | **11.0** | TFX ↓ | ⇒ 83.2% → **72.2%** |
| **Y — genuine disagreement** | **≈ 0** | — | **0pp measurable at 8/17** |
| **Z — unexplained residual** | **1.3** | TFX low | see below |

**Z = 1.3pp, and it does not survive contact with microstructure:**

| Z-component | Effect |
|---|---|
| Polymarket bid/ask **0.72 / 0.75** on the Sep leg | mid carries **±1.5pp** — **the entire residual sits inside one spread** |
| Polymarket Sep ladder sums **97.8%** (underround) | normalised PM = **75.2%** → residual **widens to −3.0pp** |
| Kalshi ladder sums **101.0%** (overround) | normalised Kalshi = 73.8% |
| Polymarket rounds sub-25bp moves **up** to 25bp; TFX pays actual bp | ≤ **+1pp** toward Polymarket. Bounded, not priced — no sub-25bp outcome is listed |
| Futures **term premium** over pure expectations | **unquantified, one-directional.** 0.5–1.0bp ⇒ TFX 70.1–67.9% ⇒ residual **−3.4 to −5.6pp**. I cannot resolve this and will not pretend to |
| TFX 8/17 settlement is a **zero-volume mark** (§4) | ±1.5bp of non-traded measurement noise = **±6.6pp** |

**Verdict on Leg 2:** at 8/17, **resolution semantics explains essentially all of the raw gap**; **genuine disagreement between the crowd and the swap/futures market is 0pp measurable**; the 1.3pp residual is smaller than the bid-ask spread of the instrument it is measured against and is therefore **not a finding**. ⚠️ **The honest caveat is the term-premium wedge**: it is the one component I could not measure, it runs one way, and at a plausible 1bp it would reopen a ~6pp gap with **TFX below the crowd**.

### 6c. ⚠️ …and the same decomposition at the 8/14 vintage says the opposite

| 8/14, like-for-like | Value |
|---|--:|
| SAM's method on the correct 8/14 column | 77.2% |
| **X — resolution semantics (net)** | **−17.2pp** |
| **TFX corrected** | **60.0%** |
| Polymarket 8/14 | **79.5%** |
| **Y — genuine disagreement** | **19.5pp** |

⇒ **On 8/14 the corrections move TFX AWAY from Polymarket, and a 19.5pp genuine disagreement remains.** SAM's original instinct — *"either a real edge or a real defect, and I can't yet say which"* — was **better calibrated than the resolution that replaced it**. There was a real gap on 8/14. It is gone on 8/17 because the crowd came down 6pp and the futures were marked up 1.5bp on no trades. **Nobody was vindicated; the question expired.**

---

## 7. THE THREE-PLATFORM READ (2026-08-17, 16:37–16:44Z)

| Instrument | P(+25bp at Sep MPM) | Basis | Depth |
|---|--:|---|---|
| **Polymarket** (Gamma, mid) | **73.5%** (bid .72 / ask .75); normalised **75.2%** | announcement, meeting | vol $100.5K · ⚠ liq $7.8K |
| **Kalshi** `…-26SEP17-H25` (book mid) | **74.5%** (bid .74 / ask .75); normalised **73.8%** | announcement, meeting | **OI 21,061** · vol 31,792 · 24h 3,251 |
| **TFX 26.09−26.06** (my derivation, 8/17 file) | **72.2%** | compounded TONA, quarter | ⚠ **0 lots traded 8/17**; OI 904 (¥90.4bn) |
| **TFX**, last-**traded** settlement (8/14) | **60.0%** | same | 1,600 lots |
| *SAM published* | *~72–77% band* | — | — |
| *`boj_ois.py` / centralbank.watch* | ⛔ *51.0%* | — | **refuted, §3b** |

**Max spread among the three live reads: 2.3pp.** Any-hike: PM 74.6% · Kalshi 76.5% · TFX 73.3%.

---

## 8. VERDICTS, ASSUMPTIONS, AND WHAT I COULD NOT SETTLE

### Leg 1 — **MODIFIED**

| SAM's claim | My finding |
|---|---|
| `boj_ois.py`'s 51.0% is wrong | ✅ **CONFIRMED** — and I strengthened it: unreachable from the primary under *any* October assumption satisfying "≤1 hike," which needs no Polymarket input |
| Polymarket and the JGB 2Y were right; the aggregator was the lone dissenter | ✅ **CONFIRMED in direction** (2Y is SAM's instrument, not mine — not adjudicated here) |
| Cite ~72–77% as a band, own TFX primary | 🟠 **MODIFIED** — the band is not reproducible as described. Correct value is **72.2% (8/17 mark) / 60.0% (8/14 last traded)**. SAM's band is right at 8/17 by the cancellation of a +6.0pp column error, a +8.0pp coverage error and a −19.0pp meeting-contamination error |
| Assumption (a) 26.09 covers ~the whole period | ⛔ **REFUTED** — 83/91 = 91.2%; Silver Week pushes the effective date to Thu 9/24 |
| Assumption (b) 25bp increment | 🟠 **survives on the increment; the window contains a SECOND MPM**, which is the derivation's central defect (74% of the 8/12 spread) |
| Assumption (c) 26.06 a clean anchor at 0.977% | ✅ **CONFIRMED at BOJ primary, and stronger than stated** |
| Parser trap (exact product match) | ✅ **CONFIRMED** — 448 substring matches vs 64 true rows |
| *"the conclusion survives all three [assumptions]"* | ⛔ **the CONCLUSION survives; the NUMBER does not.** Two of three assumptions are wrong by 8.0pp and 19.0pp |

### Leg 2 — **RESOLUTION-MISMATCH, at 8/17**
**X (resolution semantics) = 11.0pp net / 27.0pp gross · Y (genuine disagreement) = 0pp measurable · Z (unexplained) = 1.3pp, inside bid-ask.**
**At 8/14: X = 17.2pp · Y = 19.5pp · Z ≈ 0.** The gap was real then and is gone now.

### Leg 3 — **CORROBORATED** (Kalshi mid 74.5%), plus an ORACLE tool defect logged.

### Assumptions I had to make — every one, named

1. **Polymarket's October ladder is per-meeting/unconditional**, not cumulative-from-today. *Basis for it:* the Oct ladder is the near-mirror of the Sep ladder (Sep +25 73.5 / no-change 23.0; Oct no-change 73.5 / +25 23.5), which is coherent as "one hike this autumn, most likely September" and incoherent under a cumulative reading. The resolution text (*"the amount of basis points the upper bound … is changed by versus the level it was prior to the … October 2026 meeting"*) supports it. **Not independently verified with Polymarket.** This is the single largest borrowed input in my derivation.
2. **My Sep figure is a hybrid, not a pure TFX read** — it takes the October term from Polymarket and then compares the output to Polymarket. **It is therefore not fully independent.** The §3b bound is the independent leg, and it is the one I would put weight on.
3. BOJ effective date = **next Japanese bank business day** (verified on the 6/16→6/17 precedent, one observation; the convention is longstanding but I checked one instance).
4. TONA/target basis (−2.3bp) is **constant across a hike**. If it shifts 1bp, ±4.4pp.
5. **Zero term premium in the 26.09 contract.** Almost certainly false in some degree; one-directional; unquantified.
6. October probabilities held flat within each trading day (CLOB daily closes vs TFX settlement times are not synchronised — TFX settles ~15:30 JST, Polymarket is 24h).
7. No unscheduled BOJ move inside either window.
8. Sep 16 / Dec 16 / Jun 17 2026 are not Japanese bank holidays (checked; the rulebook shifts the window if they are).

### What I could NOT settle
- **The term premium.** The one wedge that could reopen a real gap, and it runs against the crowd.
- **Why TFX moved 1.5bp on zero volume.** The published settlement rule cannot produce it; the fallback is unstated in `w-01.pdf`.
- **Whether the 8/14 19.5pp gap was crowd overshoot or futures staleness.** Both legs then moved toward each other, which is consistent with either. **Unresolvable after the fact — and that is the reason to run this check *before* the gap closes, not after.**

---

## 9. WHAT THIS CHANGES FOR CONSUMERS (routing only — nothing re-marked)

| Audience | Message |
|---|---|
| **SAM** (owner) | **Keep the do-not-cite on 51.0% — it is refuted independently and model-free.** But the **~72-77% band is not reproducible as described**: the column is one business day stale, f_Sep is 0.9121 not 1.0, and the 26.09 window contains the October MPM. Corrected: **72.2% (8/17) / 60.0% (8/14 traded)**. **Attach the last-TRADED settlement date to any TFX figure** — today the file date and the traded date differ by 12.2pp of probability. |
| **Anyone citing a Sep-BOJ number tonight** | **~73%** is the defensible figure — it is where all three instruments sit (72.2 / 73.5 / 74.5). ⚠️ It is **falling**, not rising: 79.5 → 73.5 (Polymarket) and ~80 → 74.5 (Kalshi) since 8/14. **Anyone carrying "~79-80%" from the 8/14 packets is 6pp stale.** |
| **BOND** | Kalshi now has a **live, real-OI BOJ policy market** (`KXCBDECISIONJAPAN`) — a second real-money BOJ witness that did not exist on my board. Worth pinning. |
| **PROME** | Two ORACLE-side defects logged against myself: the `kalshi.py` search false negative (§5, fix owed) and the fact that **my own board carried no Kalshi BOJ market while one had been open since 7/28** — a coverage miss of 20 days. |

---

## 10. STANDING LESSONS (candidates for promotion; not written to memory this session)

1. **A headerless numeric feed must be column-fixed by chaining across dates, never by plausibility.** Every candidate column here held a plausible rate; only the cross-file chain (`col-11(t) == col-23(t−1)`) identified which was current. The wrong column was internally consistent, produced a believable number, and moved in the right direction — it was wrong by one business day for a week.
2. **Two errors of opposite sign look like a correct method.** SAM's +8.0pp coverage error and −19.0pp meeting-contamination error left a band that brackets the right answer *on one date*. **A result agreeing with an external witness is not evidence the derivation is sound** — it can be evidence that the errors cancelled at today's parameter values. They did not cancel on 8/12 (−10.7pp) or 8/14 (−19.5pp).
3. **A search returning 0 on a control term you know is populated is a defect report, not a datum.** `kalshi.py search "interest rate"` → 0 was the tell that saved the Kalshi leg. Enumerate the registry, don't keyword the population.
4. **A settlement price is not a traded price.** A whole futures strip re-marked by an identical increment on zero volume is a curve mark. Publish the last-traded date beside any level derived from a thin listed contract.
5. **A divergence that closes is not a divergence that was explained.** Both legs moved toward each other in one session; the 8/14 question is now permanently unresolvable. Second-eyes work has a shelf life.

---

*Reproduce: TFX `daily_statis_{20260812,13,14,17}.csv` fields 9 (exact `Three-month TONA Futures`), 10 (contract), 23 (settlement rate), 25 (Δ), 26 (volume), 28 (OI). Spread = 26.09 − 26.06. `P₂₅ = ((S − 0.4835·E[Δ_Oct])/0.9121 − 0.475)/25`. Polymarket: Gamma `/markets?slug=…` + CLOB `/prices-history?fidelity=1440`. Kalshi: `/series/?category=Economics` → `KXCBDECISIONJAPAN` → `/markets?event_ticker=KXCBDECISIONJAPAN-26SEP17`.*
