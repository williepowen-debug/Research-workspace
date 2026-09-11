# MIDAS — VECTOR 3: is GLD the wrong hedge under an oil-shock / real-yield regime?

**Session:** 2026-09-11 00:3x–01:5x ET (Fri), spawned by PROME (DOCKET L327, executed early on Will's 00:29 word).
**Authority:** Will 2026-09-11 00:21 ET *"Ok can you work on assigning these vectors?"* → PROME vector packet `AGENTS/MIDAS/inbox/2026-09-11_from-PROME_VECTOR-3-…md`.
**Contract:** report-before-execute. **NO card, NO order, no mark/band/threshold moved, no re-grade of MIDAS-06, $0.** Trade construction = TERRY; Will decides.
**Working record for `PROME/inbox/2026-09-11_from-MIDAS_VECTOR-3-is-GLD-the-wrong-hedge-read.md`** (the one page). This file holds the tables the page cites.

---

## 0 · Instrument hygiene FIRST — three of this desk's four standing warnings fired again tonight

⛔ **Every `=F` pointer is STILL on a dying contract, re-verified on 9/10 settled bars.** The contract-identity guard built this session (route (i), PROME-ruled 9/5 + 9/10) grades on the **prior settled session**, never the newest bar:

| pointer | front month | 9/10 vol | front vol | share | `=F` close | front close | spread | state |
|---|---|---:|---:|---:|---:|---:|---:|:--|
| `GC=F` | `GCZ26` | 86 | 164,390 | 0.05% | $4,364.50 | **$4,407.30** | −0.97% | **DYING** |
| `SI=F` | `SIZ26` | 138 | 54,865 | 0.25% | $64.28 | **$64.93** | −1.00% | **DYING** |
| `HG=F` | `HGZ26` | 933 | 48,742 | 1.91% | $6.47 | **$6.55** | −1.22% | **DYING** |
| `PL=F` | `PLV26` | 4 | 28,309 | 0.01% | $1,797.10 | **$1,801.10** | −0.22% | **DYING** |
| `PA=F` | `PAZ26` | 0 | 5,105 | 0.00% | $1,281.30 | **$1,294.70** | −1.03% | **DYING** |

⇒ **The vector packet's `GC=F $4,416 [9/9]` is the dying contract.** `GCZ26` settled **$4,460.70** on 9/9 — a **$44.70 / 1.00%** gap. Not PROME's error: it is the pointer's, and it is exactly the defect KB-112 registered. Every gold figure below names its basis.
⇒ **KB-112's volume-duplication shape reproduced a third time:** the 9/10 row carried 9/9's volume on **all five** front months (`GCZ26` 164,390 both days, `SIZ26` 54,865, `HGZ26` 48,742, `PLV26` 28,309, `PAZ26` 5,105) while both ETFs printed distinct volumes. The self-heal rule held; the guard is built on it.
⚠️ **The packet's `BZ=F $108.45 (+7.15%)` does not reproduce on the settled 9/10 bar.** My pull: **$107.63 [9/10 close]**, 9/9 $101.21 ⇒ **+6.34%**; the 9/11 in-flight bar reads $107.87. $108.45/101.21 = +7.15% exactly, so PROME's figure is an **in-flight tick against the correct 9/9 base** — L-37 class, and `BZ=F` is itself a continuous pointer (same KB-112 class, BRENT's to grade). **The direction and order of magnitude are unaffected; the exact percent is.**

---

## 1 · The two regimes, with figures

**Regime A — real-yield shock (2022).** Real yields rise; gold is a discount-rate asset and pays for it.

| leg | figures |
|---|---|
| DFII10 | −0.97 [2022-01-03] → **+1.74** [2022-11-03] = **+271bp**; full-year +255bp |
| GLD, full year 2022 | $168.33 → $169.64 = **+0.8%** (flat) |
| GLD, oil-peak → yield-peak (2022-03-08 → 2022-11-03) | **−20.73%**, while Brent **−26.03%** and DFII10 **+278bp** |
| gold–DFII10 beta, 2022 | **−0.0615 %/bp** (se 0.0065, t −9.48, R² 0.268, n=248) |

⛔ **The 2022 full-year "+0.8%" is the trap.** Gold looks like it "held" only because the year *opened* inside a war spike. Measured from the oil peak to the real-yield peak — the actual regime leg — **gold lost 20.7% while the oil shock it was supposedly hedging also lost 26%.** Both legs of an oil-shock hedge died in the same eight months.

**Regime B — geopolitical premium with real yields FALLING (2019 Abqaiq, 2024).** Gold pays, modestly.

| event | window | Brent | GLD | ΔDFII10 |
|---|---|---:|---:|---:|
| Abqaiq (attack Sat 2019-09-14) | 9/13 → 9/16 | **+14.61%** | **+0.83%** | **−6bp** |
| Abqaiq, one week | 9/13 → 9/20 | +6.74% | +2.00% | −10bp |
| Iran salvo 2024-10-01 | 9/30 → 10/1 | +2.49% | **+1.05%** | **−8bp** |
| Iran salvo, one week | 9/30 → 10/7 | **+12.76%** | **+0.46%** | **+13bp** |
| Iran/Israel Apr 2024 | 4/11 → 4/19 | −2.73% | +0.56% | +5bp |

⛔ **Even in the FAVOURABLE regime the hedge is thin:** Abqaiq's +14.61% oil day bought **+0.83%** of gold. And the 2024 one-week row is the whole argument in one line — **the same event paid +1.05% on the day real yields fell 8bp and +0.46% over the week they rose 13bp.** The sign of the rate leg, not the size of the oil move, is what pays.

---

## 2 · The discriminator — one table, and it is monotone

**All Brent daily sessions ≥ +3%, 2017-02-28 → 2026-09-10 (n=168), split by the SAME day's ΔDFII10:**

| same-day ΔDFII10 | n | GLD mean | GLD median | GLD > 0 |
|---|---:|---:|---:|---:|
| ≤ −3bp | 42 | **+1.071%** | +1.009% | 34/42 = **81%** |
| −2 … 0bp | 47 | +0.281% | +0.283% | 32/47 = 68% |
| +1 … +5bp | 59 | −0.233% | −0.081% | 27/59 = 46% |
| **> +5bp** | **20** | **−1.063%** | −0.955% | **4/20 = 20%** |
| *(unconditional on those 168 days)* | 168 | +0.138% | +0.239% | 97/168 = 58% |

**Same split, 2026 only, Brent ≥ +2% (n=56):** ΔDFII10 ≤0 → **+0.367%** (13/21 up) · +1…+5bp → **−0.456%** (12/30) · **>+5bp → −2.066%** (1/5).

⇒ **Gold does not hedge oil shocks. Gold hedges the real-rate consequence of an oil shock — and only when that consequence is DISINFLATIONARY/demand-destructive.** When the shock passes through to real yields instead, gold is a losing hedge with a 20% win rate. Spread between the top and bottom bucket: **2.13pp per session.**

**Source:** GLD daily closes + FRED DFII10, both pulled 2026-09-11 00:5xZ via `FORGE/tools/market-data/fetch.py` (`price_history`, `fred_fetch`); GLD history `complete=False` — 80 span-interior missing weekdays over 11.5 years, none inside the 2026 window; pairs are formed only where both series have consecutive observations. **VERIFIED.**

---

## 3 · Which regime is the 9/8–9/10 tape? — **Regime A**

| date | Brent (`BZ=F`) | GLD | ΔDFII10 | bucket |
|---|---:|---:|---:|---|
| 9/8 | $97.92 (+1.68%) | $399.72 (−1.73%) | 2.43, **0bp** | −2…0bp |
| 9/9 | $101.21 (**+3.36%**) | $403.35 (**+0.91%**) | 2.46, **+3bp** | +1…+5bp (gold in the winning 46%) |
| 9/10 | $107.63 (**+6.34%**) | **$396.36 (−1.73%)** | **~+7bp INFERRED** | **> +5bp** (the 20%-win bucket) |
| **9/4 → 9/10** | **+11.79%** | **−2.56%** | 2.43 → ~2.53 | — |

**The 9/10 DFII10 observation is NOT PUBLISHED** (FRED T+1; due ≈9/11 16:15 ET) — **SEARCH-NOT-FOUND at the primary.** Two independent nowcasts:
- **TIP ETF −0.440% [9/10 close].** Regression ΔDFII10(bp) on TIP daily return, 2026-03-16→2026-09-10: **−14.70bp per +1% TIP, R² 0.867, n=122, residual sd 1.32bp** ⇒ **ΔDFII10 +6.9bp ⇒ DFII10 ≈ 2.53.** **INFERRED.**
- TLT −1.162% [9/10] through TLT's own DFII10 beta ⇒ +9.3bp ⇒ ≈2.55. Weaker instrument (R² 0.586); quoted only as corroboration, and it shares a return channel with GLD so it is **not** an independent check of gold's residual.

⛔ **Do not treat these as a DFII10 print.** They are a nowcast with a named falsifier that resolves in ~16 hours.

**2.50 in context — full FRED DFII10 series, 2003-01-02 → 2026-09-09, n=5,926:** 111 observations ≥2.50, **the last on 2023-10-25**, the one before that **2008-11-28**; sample max 3.15 [2008-11-21]. **2.46 [9/9] is only the SECOND 2026 observation ≥2.46** (other: 7/31) **and the second since 2024-01-01.** If the nowcast confirms, 9/10 is the first ≥2.50 print in **23 months** — and it is the book's TLT-put add-gate.

**The most recent comparable, and this desk has already lived it:**
**2026-02-27 → 2026-03-31: Brent +63.29%, GLD −11.05%, DFII10 +28bp.** Tighter: **2026-03-02 → 2026-03-26: Brent +38.94%, GLD −18.24%, DFII10 +32bp.** Six months ago, the identical experiment, and gold lost 18% into a 39% oil spike.

---

## 4 · The current beta — gold is 2.5× as rate-sensitive as it was in 2022

GLD daily % regressed on same-day ΔDFII10 (bp). **Univariate by design** — no DXY control; BOND owns the multi-factor decomposition (the 87.7–91.1%-unexplained figure is a DIFFERENT construction and is not cited here).

| window | n | **beta %/bp** | se | t | R² | GLD total | ΔDFII10 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2022 | 248 | **−0.0615** | 0.0065 | −9.48 | 0.268 | +0.8% | +255bp |
| 2019 | 249 | −0.1373 | 0.0112 | −12.26 | 0.378 | +17.8% | −81bp |
| 2024 | 249 | −0.0711 | 0.0128 | −5.54 | 0.110 | +27.0% | +50bp |
| **2025** | 247 | **−0.0086** | 0.0192 | **−0.45** | 0.001 | +61.5% | −30bp |
| 2026 YTD | 171 | −0.1686 | 0.0432 | −3.90 | 0.083 | +1.3% | +52bp |
| **last ~120 sessions (3/16 → 9/10)** | **122** | **−0.1860** | 0.0398 | **−4.68** | 0.154 | −12.4% | +59bp |
| full sample 2015-03 → 2026-09 | 2,870 | −0.0756 | 0.0037 | −20.18 | 0.124 | +264.3% | +207bp |

⛔ **2025 is the debasement year and its beta is statistically ZERO (t −0.45, R² 0.001) on +61.5% of gold.** That is the regime the fleet's M1 thesis was written in. **It ended.** The 2026 beta is **−0.186 %/bp, 2.5× the 2022 shock beta and 2.5× the 11.5-year sample beta** — gold has re-coupled to real rates *harder than it was coupled during the worst real-yield shock of the modern era*, and it has done so while the debasement story is still being told.

**Cross-asset, same windows:**

| pair | 2022 | 2025 | 2026 YTD | last 120 sess | full sample |
|---|---:|---:|---:|---:|---:|
| corr(GLD, TLT) | +0.334 | +0.037 | +0.158 | **+0.279** | +0.252 |
| beta GLD ~ TLT | 0.251 | 0.061 | 0.523 | **0.784** | 0.277 |
| corr(GLD, Brent) | +0.375 | +0.065 | **−0.106** | **−0.240** | +0.049 |
| beta GLD ~ Brent | 0.123 | 0.045 | −0.054 | **−0.100** | 0.020 |

⇒ **GLD now moves +0.78% per +1% of TLT.** It is a long-duration asset wearing a hard-asset label. And in 2026 it moves **against** Brent (corr −0.24 on 120 sessions, the most negative reading in the sample).

---

## 5 · MIDAS-06 branch (a) DIVERGE under a real-yield shock — **stated on the letter, NOT re-graded**

⛔ **MIDAS-06 is CONSUMED and TERMINAL** — graded **(a) DIVERGE PERSISTS** 2026-08-31 (M1 3→4, composite 7/20→8/20), record `analysis/2026-08-31_midas-06-TERMINAL-GRADE.md`. **Nothing below re-opens it, re-scores it, or moves a band.** This is a state observation about tonight's tape against the frozen letter's own two legs.

Branch (a) = **gold ≥ $4,340.70 AND DFII10 ≥ 2.40.**

**Rate leg — INTACT and STRENGTHENING.** DFII10 **2.46 [FRED obs 9/9, VERIFIED]**, nowcast ~2.53 [9/10, INFERRED]. Distance above the 2.40 key has grown from +2bp at the grade to **+6bp official / ~+13bp inferred**, at a level with 2 prints since 2024.

**Gold leg — decayed to ZERO margin, and it FAILS on the only roll-free basis.**

| basis | reading | vs $4,340.70 | note |
|---|---:|---:|---|
| `GCZ26` 9/10 settle | **$4,407.30** | **+$66.60 / +1.53%** | ⛔ **crosses the Q→Z roll** |
| `GCZ26` de-contangoed at the +1.22% Q→Z artifact this desk measured | $4,354.20 | **+$13.50 / +0.31%** | roll-adjusted |
| **`GLD` — the no-roll arbiter this desk has twice ruled the grading instrument** | **$396.36 [9/10]** vs **$398.47 [8/7]** | **−0.53%** | **BELOW the anchor** |

⛔ **The $4,340.70 key is an 8/7 settle on the THEN-front month**, and this desk's own cross-roll ban fixes the pair (8/20 $4,516.30 = `GCQ26`; 8/26 $4,598.20 = `GCZ26`). **Comparing a `GCZ26` level to it crosses the roll in the FAVOURABLE direction by ~1.2%** — the naive +1.53% margin is mostly contango. On GLD, which has no roll and which the 8/28 arbitration already made the graded instrument, **gold is 0.53% BELOW where branch (a) was anchored.**

**Survival statement for the letter:**
> **Branch (a)'s rate leg is strengthening while its gold leg has decayed to zero-or-negative margin depending on basis. DIVERGE is not being refuted by a gold collapse — it is being CLOSED BY RE-COUPLING, which is precisely what a real-yield shock does to a debasement premium.** The frozen letter graded (a) on 8/31 and that grade stands; the *mechanism* it scored is visibly weakening on new data.

**Registered flip: NOT FIRED.** STATUS's bidirectional flip is *gold below ~$4,050 while DFII10 ≥2.40 ⇒ re-coupled/capped, M1 → 2.* `GCZ26` $4,407.30 is **8.82% above $4,050**. ⇒ **M1 HOLDS 4. Composite 8/20 UNCHANGED. Nothing re-rated tonight.**

---

## 6 · The book question — do the 16 GLD shares hedge or fight?

**Marks `[FORGE/STATUS.md, reconcile vintage 9/10 CLOSE Fidelity + 16:10 Robinhood]` — a mirror, not live, and it stales from the moment it is written.**

| leg | size | mark | value | role |
|---|---:|---:|---:|---|
| **GLD** | 16 sh | $396.36 | **$6,341.76** | basis $373.59, +6.09% / +$364.26; 9/10 day **−$111.84**. **Largest position by value.** |
| USO | 37 sh | $158.38 | $5,860.06 | +29.52% / +$1,335.79; 9/10 day **+$311.17**, the book's mover |
| TBT | 14 sh | $39.51 | $553.14 | 2× inverse UST |
| TLT $77P Sep-30 | ×20 | $0.08 | **$160.00** | basis $231.26, −30.82%; **20 DTE** |

**Per +10bp DFII10, at the last-120-session betas (GLD −0.1860 %/bp; TLT −0.1276 %/bp, t −13.04, R² 0.586):**

| leg | arithmetic | P&L per +10bp |
|---|---|---:|
| GLD 16 sh | $6,341.76 × −0.1860%/bp × 10 | **−$117.96** |
| TBT 14 sh | $553.14 × +0.2552%/bp × 10 (= −2× TLT's beta) | **+$14.12** |
| **shortfall** | | **−$103.84** |
| TLT 77P ×20 | 2,000 notional sh; TLT $80.78 moves −$1.031/sh per +10bp | **unknown — needs the delta** |

🔑 **THE NUMBER: breakeven put delta = $103.84 / (2,000 × $1.031) = |Δ| 0.0504.**

> **If the TLT $77P's delta is shallower than −0.05 per contract, the book is NET LONG DURATION through GLD — despite carrying a sleeve labelled "duration-short."** At a $0.08 mark, $3.78 out of the money, 20 DTE, that sits right on the line.
> ⛔ **This desk does not hold an options chain — the delta is UNKNOWN (SEARCH-NOT-FOUND: no chain in `FORGE/tools/market-data/`). TERRY has it and owns the call.** The verdict below is conditional on it and says so.

**The three-way answer, because "hedge or fight" is the wrong binary:**

| the book's world | USO | TBT + TLT puts | **GLD** | verdict on GLD |
|---|:--:|:--:|:--:|---|
| **oil UP, real yields UP** ← **where we are (9/8–9/10)** | 🟢 win | 🟢 win | 🔴 **lose** | **a drag on a winning book.** 9/10: book +$463.50 / +1.18% *with* GLD −$111.84 |
| oil DOWN, real yields DOWN (Mideast cools) | 🔴 lose | 🔴 lose | 🟢 **win** | **this is the hedge, and it is a real one** — corr(GLD, Brent) −0.24 in 2026, the most negative in the sample |
| **oil DOWN, real yields UP** (fiscal / term-premium repricing with no inflation impulse) | 🔴 lose | 🟢 win | 🔴 **lose** | ⛔ **the unhedged corner — and it is the 2022 corner** |
| oil UP, real yields DOWN | 🟢 win | 🔴 lose | 🟢 win | fine |

⛔ **The 2022 corner is not hypothetical: 2022-03-08 → 2022-11-03 delivered Brent −26.03% AND GLD −20.73% AND DFII10 +278bp simultaneously.** In that corner the only paying leg is a **$713 duration-short sleeve** standing against **$12,201.82** of GLD + USO.

⇒ **The finding is NOT "GLD is the wrong hedge under an oil shock."** It is: **GLD and USO fail TOGETHER in the 2022 corner, and the book has ~$713 of mark defending a ~$12,202 pair against it.** The vector's question points at the wrong pair.

**⚖️ THE SELF-ATTACK — the strongest case FOR the 16 shares, and it is real.**
On 9/10 **gold fell the LEAST of five metals**: GLD **−1.73%** vs SLV −5.30%, CPER −4.90%, PPLT −5.95%, PALL −5.45% [ETF closes, 9/10]. On the explicit front months: `GCZ26` **−1.20%** vs `SIZ26` −5.42%, `HGZ26` −4.93%, `PLV26` −6.14%, `PAZ26` −6.25%. **GSR (`GCZ26`/`SIZ26`) 64.98 [9/9] → 67.88 [9/10] = +2.90 points in ONE session.**
⇒ **Gold IS the defensive metal inside a real-asset liquidation.** It is **not** the defensive asset against a real-yield shock — that is cash and short duration. **Both are true; the book question asks the second one, and answering it with the first is the substitution to refuse.**

---

## 7 · What changes the answer — three numbers and a falsifier

| # | the number | now | flips the read when | who owns it |
|---|---|---|---|---|
| **1** | **DFII10 official print** | **2.46 [9/9]**; ~2.53 [9/10 INFERRED] | **≥ 2.50 on 3 consecutive FRED observations.** 2.50 is the book's TLT-put add-gate AND a 23-month high (last ≥2.50 = 2023-10-25). Sustained ≥2.50 puts this squarely in the 2022 corner and makes GLD's −0.186 beta the book's largest single risk line | **BOND** (real-rate level is BOND-canonical; MIDAS references) |
| **2** | **gold–DFII10 beta, rolling 120 sessions** | **−0.1860 %/bp** (t −4.68) | **≥ −0.08 %/bp** = the 2022 level (−0.0615) and the 11.5-yr sample level (−0.0756). There the 16 shares cost **~$51 per 10bp** instead of $118 and the TBT+put sleeve plausibly covers it | **MIDAS** — re-measure every boot |
| **3** | **TLT $77P delta** | **UNKNOWN** | **vs 0.0504.** Shallower ⇒ the book is net long duration through GLD | **TERRY** |

**FALSIFIER of my own read — name it before it is needed.**
> **Two sessions inside any 10 with ΔDFII10 ≥ +5bp AND GLD ≥ +0.5%.** In the >+5bp bucket gold has won **4 of 20 since 2017** and **1 of 5 in 2026**; two wins in ten sessions says the debasement bid has re-asserted over the discount-rate channel and the −0.186 beta is breaking. At that point the read above is wrong and GLD is doing the job.
> ⚠️ **And the charitable reading of my own work, checked rather than banked: 9/9 is NOT an instance.** Brent +3.36%, GLD **+0.91%**, ΔDFII10 **+3bp** — that lands in the **+1…+5bp** bucket (46% win rate), not the >+5bp one. It is a one-session argument for the other side and it does not clear the bar I just set. *(`finding_a_charitable_reading_of_your_work_is_the_one_to_check`.)*

---

## 8 · Verdict — a READ for TERRY and Will. **Not an order, not a card, not a size.**

> ### **KEEP the 16 GLD shares tonight — and stop calling them a hedge on the duration book.**
>
> **They are two things at once and the two jobs conflict:** the book's **largest long-duration position** (−$118 per +10bp, 8.4× the TBT leg's +$14) *and* its **only real hedge against the energy thesis failing** (corr −0.24 to Brent in 2026). Under an oil shock that passes through to real yields — which is **exactly** the 9/8–9/10 tape — the first job dominates and GLD is a **drag on a winning book**, not a wound: the book made **+$463.50 / +1.18%** on 9/10 *with* GLD down $111.84.
>
> **Why NOT trim tonight, on four grounds:**
> 1. **The registered flip has not fired.** `GCZ26` $4,407.30 is 8.82% above the $4,050 level that would re-rate M1. Trimming on an unregistered read is setting a threshold, which is Will's.
> 2. **Root rule #6 discipline, applied to a sale.** GLD closed **−1.73%** on 9/10 — a red day for this position. The rule's logic (buy protection into strength, not weakness) says selling a long into its own down-move is a chase. *"The window is closing" is a chase, not a break.*
> 3. **The load-bearing rate figure is 16 hours from publishing.** The 9/10 DFII10 observation is a nowcast (~2.53, INFERRED) and resolves at the FRED release ≈9/11 16:15 ET. **Acting on a nowcast that resolves tomorrow is the error this desk has now bought twice off in-flight bars** (L-37, L-50).
> 4. **The delta that decides the arithmetic is TERRY's and is not in hand.**
>
> **REPLACE-WITH-WHAT, if the read is ever acted on — stated so the option is on the table, priced, and NOT proposed:** the job GLD is being asked to do for the *duration* book is done by **cash / short duration**, not by another hard asset; the job it is actually doing well — hedging the energy leg's failure — it keeps. **A swap of gold for silver or PGMs would go the WRONG way** (9/10: SLV −5.30%, PPLT −5.95%, PALL −5.45% vs GLD −1.73%). **No instrument is recommended and no size is named — that is TERRY's construction and Will's approval.**
>
> **What to watch, in priority order:** ① the **9/11 16:15 ET FRED DFII10 print** against 2.50 · ② the **rolling-120 beta** against −0.08 · ③ the **TLT 77P delta** against 0.0504 · ④ the falsifier (2-in-10 sessions of ΔDFII10 ≥+5bp with GLD ≥+0.5%).

---

## 9 · Provenance

| claim class | instrument | pulled | token |
|---|---|---|---|
| GLD / SLV / CPER / PPLT / PALL closes; TLT; TIP; `BZ=F` | `FORGE/tools/market-data/fetch.py` `price_history` / `price_fetch` (yfinance) | 2026-09-11 00:4x–01:1x ET | **VERIFIED** |
| Explicit front months `GCZ26 SIZ26 HGZ26 PLV26 PAZ26` + volumes | same, via the new `check_contract_identity()` guard in `metals_watch.py` | 2026-09-11 00:5x ET | **VERIFIED** |
| DFII10 / DGS10 official observations (to 9/9) | `fetch.fred_fetch("DFII10", limit=7000)` — n=5,926, 2003-01-02 → 2026-09-09 | 2026-09-11 01:0x ET | **VERIFIED** |
| DFII10 9/10 ≈ 2.53 | TIP-return regression, R² 0.867, resid sd 1.32bp | — | **INFERRED** |
| DFII10 9/10 official | FRED — not yet published (T+1) | — | **SEARCH-NOT-FOUND** |
| TLT $77P delta | no options chain in the toolkit | — | **UNKNOWN** |
| Book sizes / marks / basis | `FORGE/STATUS.md`, vintage 9/10 CLOSE Fidelity + 16:10 RH | — | **VERIFIED at the mirror** (a mirror, not live) |
| MIDAS-06 letter, $4,340.70 key, cross-roll ban, GLD-as-arbiter | `AGENTS/MIDAS/STATUS.md`, `analysis/2026-08-31_midas-06-TERMINAL-GRADE.md` | — | **VERIFIED** |
| Q→Z contango artifact +1.22% | MIDAS STATUS M2 cell (own measurement, KB-067) | — | **VERIFIED** |

**Scripts:** the regressions and conditional splits were run from the session scratchpad against a single cached pull (`price_history` 2,900d + `fred_fetch` 7,000 obs); the guard that ships is in `metals_watch.py`. **No market figure in this file was taken from a STATUS file** (root rule #4).
