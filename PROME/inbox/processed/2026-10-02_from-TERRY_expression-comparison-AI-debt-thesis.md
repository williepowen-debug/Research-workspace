# TERRY → PROME · 2026-10-02 Fri 11:1x ET · FIRST CUT — which instrument best expresses Will's AI-debt thesis at ≤ $500 / ~2 months?

**⚠️ FIRST CUT, labelled as such:** written BEFORE the VULCAN, LIQUID and BROCK evidence replies. Packets were sent at `2e2464917`, LIQUID and BROCK were doorbelled, and replies are asked for by Mon 10/05 08:30 ET. The final version lands before Monday's open.
**Commission:** Will 11:09 ET, *"commission it"* (PROME packet, read in full). **A comparison, not a card. `$0` MOVED · NO ORDER · NOTHING APPROVED · no card registered.**
**Basis:**
- Option quotes are yfinance **screening** marks pulled 11:11–11:13 ET; the last trades are ~10:45–10:55, so roughly 15 minutes old. Fidelity governs.
- History uses FRED ICE BofA HY OAS. FRED carries only **3 years (from 2023-10-03)**, so: **746 bars** for the regression and **4 episodes** for the episode table (construction rule #19).
- Payoffs are **at expiry, intrinsic, with the scenario move held to expiry**. That's a comparison device, not a forecast. Positions are as of the 10/1 capture.

## The one fact that frames everything

**The thesis's chain is already half-run: the stressed names have re-priced, and the index has not.** (yfinance, 52-week highs, 272 bars)

| | ORCL | CRWV | APO | IWM | RSP | HYG | **QQQ** |
|---|---|---|---|---|---|---|---|
| vs its 52-week high | **−55.5%** | **−38.1%** | −24.2% | −8.3% | −5.8% | −2.8% | **−0.7%** |
| In THIS widening (HY 270 → 324, 9/10 → 10/1) | −9.7% | −0.6% | **−10.6%** | −2.8% | −1.6% | −1.8% | **+4.8%** |

**What that means for QQQ puts:** they bet on the one link that has not happened yet, the strain reaching the index. QQQ is also the row that contains the least of the stressed thing:
- **Oracle is NYSE-listed, so it is not in QQQ.**
- The megacaps that dominate QQQ (NVDA ≈ 8.5%, MSFT ≈ 6.0%, MU ≈ 4.75%) fund capex largely from cash flow.

## PROME's HYG claim, TESTED (not adopted)

The claim: HYG puts work poorly because spread widening and falling Treasury yields offset.

- **Regression:** daily HYG total return = −0.029%/bp ΔHY OAS − 0.034%/bp Δ5Y, **R² 0.60** (746 bars, 2023-10 → 2026-09). The two legs are about equal in size per bp, so a fall in yields **can** cancel a widening.
- **20-session windows with HY ≥ +50bp** (n = 28, overlapping): median Δ5Y **−14bp**, median HYG TR **−1.11%**, median QQQ **−8.65%**. The offset shows up in the median.

**But it depends on the regime. The four distinct episodes:**

| Episode | HY | 5Y | HYG | QQQ | IWM | ORCL | KRE | APO |
|---|---|---|---|---|---|---|---|---|
| 2024-07-08 → 08-05 (soft payrolls, growth scare) | 320 → 393 | **falling** (−61bp over the max window) | **+0.3%** | −12.5% | 0.0% | −11.6% | +9.2% | −14.5% |
| 2025-03-07 → 04-04 (tariff shock) | 297 → 445 | −37bp | −2.9% | −13.9% | −11.8% | −17.3% | −14.0% | −17.9% |
| 2026-03-02 → 03-30 | 303 → 346 | rising | −1.8% | −8.1% | −9.0% | −7.0% | −5.6% | +3.3% |
| **2026-09-01 → 09-29 (now: hikes, term premium)** | 265 → 308 | **rising (+54bp)** | **−2.2%** | **+4.4%** | −3.7% | −2.5% | −3.3% | −9.6% |

⇒ **PROME's claim is TRUE in a growth scare** (2024-07: HYG +0.3% while HY widened 73bp) **and FALSE in the current rate-led regime** (Sept 2026: HYG −2.2% while QQQ rose 4.4%). ⚠️ **Today's soft payrolls, with yields falling, is the 2024-07 shape.** If credit keeps widening from here **as a growth scare**, the offset comes back and HYG puts lose their edge. If it widens **on rates and supply**, HYG is the instrument that has actually paid.

## The comparison (Dec-18-2026 on every row; ≤ $500 all-in incl. $0.65/contract)

| # | Row | Structure, live cost | Max loss / max gain | Break-even | **RIGHT, transmits** (2025-03 / 2026-03 analogs) | **RIGHT, index lags** (the 9/10 → 10/1 pattern) | **WRONG** (credit retraces, rally) | Holds the stressed thing? | Liquidity | Correlation with the held sleeve* (60d / 250d) | Biggest thing against it |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **QQQ** (WQ-365 baseline; long strike at 97% of spot) | **725/705 ×1** · 16.43 − 11.81 = **$4.62 ⇒ $463.30** (QQQ $749.05, 11:13) | $463 / **$1,537** | $720.38 (−3.8%) | −8% ⇒ **+$1,537** (full) | +4.8% ⇒ **−$463** | **−$463** | **Least** (Oracle out; cash-funded megacaps) | Best (0.5–0.8% wide; OI 3.9k–25k) | 0.42 / 0.33 | It lost in the live episode; the base rate says a failed breakout usually stops near −4% |
| 2 | **IWM** (breadth, indebted small caps) | **273/263 ×2** · 5.89 − 3.63 = 2.26 ⇒ **$454.60** (IWM $281.43) | $455 / **$1,545** | $270.73 (−3.8%) | −9% ⇒ **+$1,545** | −2.8% ⇒ **−$455** (just short of the strike) | −$455 | **Middle** (indebted small caps; AI-light) | Very good (OI 10k–90k) | **0.58 / 0.63** | Duplicates the bank / credit sleeve; IV 18.6% vs 13.2% realized ⇒ rich |
| 2b | RSP | 200/190 ×3 ⇒ **$483.90 worst** (mid ≈ $300) | — | — | — | — | — | Middle | ⛔ **FAILS** (most strikes 30–100% wide, OI in the tens) | 0.71 / 0.66 | Untradeable at size; IWM is the breadth row |
| 3 | **ORCL** | **130/115 ×1** · 8.40 − 3.60 = **$4.80 ⇒ $481.30** (ORCL $141.16) | $481 / **$1,019** | $125.19 (−11.3%) | −17% ⇒ **+$803** | −9.7% ⇒ **−$228** | −$481 | **Yes**: the fallen-angel leg of GATE-LIQ-069 (S&P BBB−) | Good (2–3% wide; OI 8k–20k) | **0.30 / 0.08** | Already −55.5%. Shorting after the fall into IV 52.7% |
| 4 | **CRWV** | **80/65 ×1** · 7.15 − 2.31 = **$4.84 ⇒ $485.30** (CRWV $89.68) | $485 / **$1,015** | $75.15 (−16.2%) | −25% ⇒ **+$789** · −11.4% (2026-03) ⇒ −$430 | −0.6% ⇒ −$485 | −$485 | **Most**: the CDS leg of GATE-LIQ-069 | OK (4–6% wide; OI 3k–6k) | **0.19 / 0.12** | Realized vol 97% vs IV 72% (options cheap), but it needs −16% to break even. A lottery |
| 5 | **HYG** (credit directly) | **77/75 ×7** · 1.23 − 0.58 = 0.65 ⇒ **$464.10** (HYG $77.10) | $464 / **$936** | $76.34 (**−1.0%**) | −2.9% ⇒ **+$936** · −1.8% ⇒ +$439 | **−1.8% ⇒ +$439** | +0.3% (2024-07) ⇒ −$464 | **Yes, credit itself** (its AI share is unknown; LIQUID asked) | OI huge (190k–800k), but **5–8% wide**: ≈ $35 of slippage on 7 lots, plus $9.10 fees | 0.51 / 0.53 | Loses in a growth scare (yields falling = today's payroll shape). **IV 9.0% vs 3.3% realized ⇒ paying ~3× realized vol** |
| 6 | **What he holds** | KRE 60P ×5 $260 · KRE 65P ×2 $266 · APO 95P $130 · HBAN 16P ×2 $150 · WAL 70P (Robinhood) $195 · KRE 25P $0 ⇒ **≈ $1,001** at the 10:37 bids (+ the QQQ short-dated puts) | sunk; forward = the marks | — | KRE −14% / APO −18% (2025-03 shape) pays | **APO −10.6%, KRE −4.7% in THIS episode, i.e. the held sleeve is where the thesis is already showing** | marks decay | Yes: banks + private credit | Mixed (APO 95P 0.85 wide; KRE 60P OI fine) | — | APO 95P is −17% OTM; KRE 60P is −15% OTM. Deep strikes need a 2025-03-size move |
| 7 | **Nothing new** | $0 | $0 / $0 | — | misses the move, but the sleeve still pays | sleeve pays | **saves the premium** | — | — | — | **Will's own 6/26 rule points here: no registered trigger with a capital path has fired** |

\*Held-sleeve proxy = equal-weight daily returns of KRE / APO / HBAN / WAL (yfinance, 272 bars).
Scenario moves come from the episode table. ORCL's "−17%" = 2025-03 and CRWV's "−25%" = a stated stress scenario (CRWV has no 2025-03 history; it listed 3/2025). Max gains are net of cost.

**N_eff:** **only ORCL and CRWV raise N_eff above 1.** Their correlation with the held sleeve is 0.08–0.30, versus 0.33–0.71 for every other row. **But they raise it by betting on a different, narrower thing:** that specific AI names fail, not that the strain reaches equities broadly. QQQ, IWM and HYG are all the sleeve's antecedent (credit stress reaching equities) in another wrapper.

**Fired triggers (Will 6/26: fresh capital only on a fired trigger with a capital path):** **none, on any row.**
- GATE-LIQ-069 is 2-of-2 FIRED, but its consequent is a discriminator re-run plus a NEXUS flag, **not capital**. I checked `PROME/GATES.tsv` line 4, and it agrees with PROME's reading.
- HY 324 crossed LIQUID's **send** line, which is a send, not a buy. KILL_MEMO ">320 sustained" is not met (one print). X1 is **CLOSED / DON'T-SIZE**.
- WQ-365 carries its **own** pre-registered trigger and is PENDING Will.

**Dated events inside a Dec-18 expiry, per row** (secondary calendar via yfinance unless noted):
- **ORCL** earnings **Thu 12/10**: after a 12/04-style time stop, before expiry. Hold through it = a gap bet (construction rule #18 logic).
- **CRWV** **Wed 11/11**.
- **NVDA** 11/17 · **MSFT** 10/28 (VULCAN's ~10/28 hyperscaler cluster) · **APO** 11/3.
- **HYG** goes ex-distribution ~11/2 and ~12/1 (~$0.34–0.44 each; already in the put's forward).

## Ranking and lean (first cut)

| Rank | Row | Why |
|---|---|---|
| **1** | **Nothing new today** (row 7) | No fired trigger with a capital path (Will's 6/26 rule). The book already holds ≈ $1.0k on the same antecedent, and it is that sleeve (APO −10.6%, KRE −4.7%) that is moving with the thesis now. VULCAN's evidence is not in. Buying now buys after a +1.4% QQQ day into a rate-relief tape |
| **2** | **QQQ, but only as WQ-365, conditional** | QQQ's weakness is that it is the furthest from the stressed thing and moved the wrong way in this episode. **That is exactly what WQ-365's trigger (a) fixes:** it buys only after QQQ itself fails its breakout, i.e. only once the index starts transmitting. If transmission comes, it has the largest payoff (2024-07 / 2025-03 / 2026-03: −8% to −14%). Best liquidity |
| **3** | **HYG 77/75**, as a CANDIDATE for its own conditional card | The tightest link to "credit leads". **It is the only row that paid in the live episode's pattern** (+$439 at −1.8%). It needs only −1.0% to break even. Against it: it **loses in a growth scare**, which is today's payroll shape (2024-07: HYG +0.3%), and it pays ~3× realized vol. A card would need its own trigger: e.g., HY ≥ 321 on two cells **AND the 5Y not falling** over the same window, so that it buys only the regime in which HYG works |
| 4 | IWM 273/263 | A real breadth expression with good liquidity, but it mostly re-buys the sleeve (correlation 0.6), its IV is rich, and in this episode it fell short of its strike |
| 5 | ORCL / CRWV | The tightest to the stressed names and the only N_eff gain. But they are already down 55% and 38%, earnings gaps both ways sit inside the horizon (CRWV 11/11, ORCL 12/10), and CRWV needs −16% to break even. **Not a card on current evidence** |
| ✗ | RSP | Options untradeable at this size |

**Desk lean: NONE today.** Keep **WQ-365** as the QQQ vehicle; its trigger already demands the transmission QQQ lacks.
- **If Will wants a credit-direct expression**, the desk's next card would be **HYG 77/75 ×7 conditional on HY persistence AND non-falling 5Y yields**. PROME takes that to Will; it is not registered here.
- **One structural idea, offered and not built:** a regime-split pair, **IWM 273/263 ×1 (≈ $227) + HYG 77/75 ×4 (≈ $265) ≈ $492**. HYG pays in rate-led widening, IWM in a growth scare. It's one $500 card on one antecedent, so **N_eff stays 1**. It only diversifies *which regime* pays.

## What would change the lean

| Evidence | Moves toward |
|---|---|
| LIQUID's 10/2 HY cell (Mon ~10:15) ≥ 321, so HY is persisting, **with the 5Y flat or up** | the HYG conditional card (rank 3 → 2) |
| HY persisting **with the 5Y falling** and QQQ closing back below $748.65 (a growth-scare shape) | WQ-365 arms on its own letter (QQQ rank 2 → 1) |
| VULCAN: a dated capex-cut or financing-failure signal at a QQQ constituent (MSFT 10/28, NVDA 11/17) | QQQ / WQ-365 strengthens; ORCL / CRWV only if the name-level CDS or concession data from LIQUID confirms |
| LIQUID: material AI / data-centre share of the HY index | HYG's "holds the stressed thing" improves |
| BROCK: APO / ARES is the cleanest equity read of credit leading | an APO or ARES put row gets built in the final version (the held APO 95P is −17% OTM) |
| HY back ≤ 312 | everything → NONE; WQ-365's kill line |

## v1.1 · 11:1x ET: LIQUID (`a431862ac`) and BROCK (`0a04cad71`) answers folded in. VULCAN still pending (after-close wake)

| Point | Evidence (owner's artifact) | Effect on the comparison |
|---|---|---|
| **Where the AI-credit stress sits** | LIQUID: **CRWV 5Y CDS ≈ 847bp [9/24]** (DTCC, ISDA model; +222 to +427bp vs the 7/06 anchor) plus **ORCL S&P BBB− [7/9]**, one notch above HY, with no forced-sell event yet. **The stress sits in single-name CDS and one rating ladder, not in cohort bonds** (BB tightened while CRWV CDS blew out) | It confirms that CRWV / ORCL are the rows that **hold** the stressed thing. The stress is single-name, which is what the low correlation (0.08–0.30) already shows |
| **HYG basis** | LIQUID: HYG tracks **iBoxx (OAS 291.7) vs ICE 324 [10/1]**, a ~32bp gap. Effective duration **3.32y**, so match to the 5Y (as done here) | My regression used ICE OAS and the 5Y. The basis gap is now stated. Not re-run |
| **HYG offset, by LIQUID's own episode scan** | 5 widenings ≥ 50bp: the offset **held** in 2024-08 (5Y −53bp, HYG −0.84% on +91bp) and 2025-04 (−61bp, −2.99% on +202bp). It **failed** in the current episode: **+64bp with the 5Y +61bp ⇒ HYG −2.60% TR ≈ −4.1% per 100bp, vs ≈ −1.5% per 100bp in 2025-04** | **It independently agrees with TERRY's test:** PROME's claim is true in growth scares and false in the rate-shock regime we are in. HYG row unchanged |
| **Does HYG hold the AI debt?** | LIQUID: AI / DC ≈ **4–6% of HY index market value** (INF). For that cohort alone to move the index +19bp it would need **+320 to +475bp**. HYG's holdings of CRWV / APLD are **UNKNOWN** (CSV unreachable). ORCL is IG, so it is not in HYG unless it becomes a fallen angel | **HYG holds the broad HY beta, not the AI cohort.** Its "holds the stressed thing" cell becomes **"credit, yes; AI debt, ≈ 4–6%"**. HYG expresses "credit leads", and expresses "AI debt" only weakly |
| **APO** | BROCK: on his record the APO 95P expresses **private credit / credit widening, NOT AI debt**. APO's AI link is as **financier** (it led the $35B Broadcom facility 6/9), which is **fee-positive until a loss shows**, so it partly cuts against the put. No AI/DC lending share is on record for any manager (software share is the proxy: ARCC 22.0%, FSK 17.7%) | The held sleeve's row-6 claim *"the thesis is already showing there"* is **narrowed:** the sleeve shows the **credit-widening** leg, not the AI-debt leg |
| **QQQ vs credit, a counterpoint to this memo's framing** | BROCK: 9/24→10/1 APO −5.26% vs QQQ +0.13%, but **on 250-day history QQQ's correlation to ΔHY (−0.55) beats APO's (−0.33) at about half the volatility**. The current decoupling is **n = 1** | ⚠️ **This weakens "QQQ is the furthest from the stressed thing" as a statistical claim.** Day to day, QQQ has tracked HY widening *better* than APO over a year. The current divergence is one episode. **The ranking is unchanged**, because WQ-365's trigger waits for QQQ to actually move with credit, but the "half-run chain" framing is about **this** episode, not a law |
| **Dates** | LIQUID: GATE-LIQ-069 review 10/15 · OCIC Q3 ~late Oct · FOMC 10/28 · 079 bands 10/31 · QRA / buyback end ~11/4 · CRWV Q3 + BDC marks early–mid Nov · LIQ-07 resolves 11/6–11/10. BROCK: **BX Q3 Thu 10/22 09:00 (V)** · APO Q3 ~11/3–11/5 (EST.) · **BCRED Q4 tender letter ~12/03** (could fire GATE-BRK-R2 (a)) | All inside a Dec-18 expiry. **The ORCL agency action is undated:** the likeliest next step is Moody's Baa2 → Baa3, which is not yet a fallen-angel event |

**Net of v1.1: ranking and lean UNCHANGED (NONE today; WQ-365 conditional; HYG a candidate; ORCL / CRWV no card).** Two descriptions get **narrower**:
- HYG = "credit leads", **not** "AI debt" (≈ 4–6% AI).
- The held APO / KRE sleeve = the credit-widening leg, **not** the AI-debt leg.

⇒ **No row in the book or in this table expresses the AI-DEBT leg itself, except single-name CRWV / ORCL.** That is the honest gap, and VULCAN's reply is the input that decides whether it deserves a card.

## COMPLETION — TERRY — 2026-10-02 (expression comparison, FIRST CUT)
STATUS: ⚠️ PARTIAL (v1.1: LIQUID + BROCK folded in; VULCAN pending — final before Mon 10/05 open)
CHANGED: PROME/inbox/2026-10-02_from-TERRY_expression-comparison-AI-debt-thesis.md; evidence packets AGENTS/{LIQUID,BROCK,VULCAN}/inbox/2026-10-02_from-TERRY_expression-comparison-evidence-ask.md; WQ-365 card (a1) wording fix
RESULT: 7 rows at ≤$500 Dec-18 (QQQ 725/705 $463 · IWM 273/263×2 $455 · ORCL 130/115 $481 · CRWV 80/65 $485 · HYG 77/75×7 $464 · held sleeve ≈$1.0k · nothing). HYG offset claim TRUE in growth scares (2024-07 HYG +0.3%), FALSE in the current rate-led widening (9/2026 HYG −2.2%, QQQ +4.4%); regression R² 0.60, 746 bars. ORCL −55.5% / CRWV −38.1% off highs vs QQQ −0.7%. Only ORCL/CRWV raise N_eff (corr 0.08–0.30). No fired capital trigger on any row. Lean NONE today; WQ-365 stays the QQQ vehicle; HYG conditional (HY persistence + non-falling 5Y) is the next card candidate.
GAPS: VULCAN not yet replied (LIQUID a431862ac + BROCK 0a04cad71 folded, no ranking change); FRED HY only 3y (4 episodes); quotes ~15 min old; earnings dates secondary (yfinance); HYG AI share unknown; payoffs at-expiry intrinsic.
WILL_NEEDS: None today (comparison only); WQ-365 stays pending; a possible HYG conditional card would go to Will via PROME.
FOLLOW-UP: Final version before Mon 10/05 open with VULCAN/LIQUID/BROCK replies + LIQUID's 10/2 HY cell; record Will's fills on doorbell.
