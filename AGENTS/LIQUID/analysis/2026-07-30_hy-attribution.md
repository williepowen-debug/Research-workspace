# HY-widening ATTRIBUTION — who is driving the +19bp

> 🔒 **FROZEN 2026-08-20 — closed-window analysis; not maintained; STATUS + `scripts/boot.py` are canonical. Do NOT cite any level here as current.**
>
> **This memo analyses the CLOSED window 7/22 → 7/29 2026. Every level in it — including `HY OAS 287`, `CCC 1013`, `BB 176`, `B 303` — is a correct measurement OF THAT WINDOW and a dead figure as of today.** **The tape has since round-tripped: the 280 line BROKE on 8/3 and HY printed 273 [FRED 8/19].** The +19bp widening this memo decomposes was **retraced**, so the *level* here is history — **the ATTRIBUTION VERDICT below is what remains live and reusable** (broad DM HY beta 68–84% · AI/data-center 15–30% · **bank/CRE ~0bp, HIGH confidence** · energy ~0bp, LOW confidence on a weak instrument).
>
> *Banner added because `consumer_check --self` flagged three `287` references here as stale-on-a-live-surface. They are not errors — 287 is this memo's SUBJECT — but `analysis/` is a live directory, so a dated level sitting in it is one careless grep away from being read as current. The fix is the banner, not a rewrite: **the numbers stay exactly as measured, and the container now says what they are.***

**LIQUID · 2026-07-30 ~15:30 ET · PROME-spawned, asked by TERRY (TRY-FIRE-001), REGINALD runs the bank-side half in parallel**

**Window:** 7/22 → 7/29 · **US HY OAS 268 → 287 = +19bp** · FRED `BAMLH0A0HYM2`, own pull 2026-07-30 ~15:10 ET. ⚠️ **SUPERSEDED AS A LEVEL — closed window, see FROZEN banner above; HY OAS is 273 [FRED 8/19] and the 280 line broke 8/3. The +19bp was retraced.**
**All three seed figures in the tasking re-pulled and CONFIRMED:** HY 281[7/27]/284[7/28]/287[7/29] ✓ · BB 176 / B 303 / CCC 1013 [7/29] ✓ · d/d 7/28→7/29 BB +1.73% vs CCC +0.80% ✓.

**No thresholds moved. RED owns the sustain ruling and it is untouched here. No trade proposals.**

---

## VERDICT (§d first — the rest is the evidence)

Of the **+19bp**:

| Attribution | bp | share | confidence |
|---|---|---|---|
| **Broad DM HY risk-premium beta** (US + Europe moving together) | **13–16bp** | **68–84%** | Moderate-high |
| **AI / data-center HY cohort** | **3–6bp** | **15–30%** | Moderate |
| **Bank / regional / CRE credit** | **~0bp** | **~0%** | **High** |
| **Energy** | **~0bp** | **~0%** | Low (weak instrument — see §5) |

> **The widening is broad-based developed-market high-yield beta, BB-led and flow-shaped — NOT bank/CRE credit, and NOT mechanically AI-issuer-led either.**
>
> **Both of TERRY's candidate mechanisms fail.** AI credit is unambiguously the most stressed cohort in this tape — it is moving roughly **8× the index** at the issuer level — but at ≤4–6% of index market value it is **too small to be the index's mechanical driver**. And the bank/CRE leg the card was built on is not weak, it is **absent**: KRE is **UP** over the exact widening window.

**⇒ This supports TERRY's NO FIRE, on independent evidence, but for a different reason than TERRY had.** Not *"the mechanism is AI instead of banks"* — rather *"the mechanism is broad beta, and the bank/CRE leg is specifically absent."*

**Single datum that would flip it:** a **bank-side credit instrument** confirming transmission — **IG BBB OAS decoupling upward from the IG index** (today: BBB +4bp vs index +3bp = no discrimination), or REGINALD's bank-CDS / CRE lane widening while KRE holds. Absent that, the bank leg is **absent, not merely unmeasured**.

---

## 1. Rating-tier decomposition — and a normalization trap

FRED, 7/22 → 7/29:

| Tier | series | 7/22 | 7/29 | Δbp | Δ% | approx index wt | contribution |
|---|---|---|---|---|---|---|---|
| BB | `BAMLH0A1HYBB` | 157 | 176 | **+19** | **+12.1%** | ~53% | ~10.1bp |
| Single-B | `BAMLH0A2HYB` | 285 | 303 | +18 | +6.3% | ~36% | ~6.5bp |
| CCC & lower | `BAMLH0A3HYC` | 981 | 1013 | **+32** | **+3.3%** | ~11% | ~3.5bp |
| | | | | | | **sum** | **20.1bp vs actual 19.0** (residual −1.1bp) |

Weights are approximate ICE BofA H0A0 rating composition; the −1.1bp residual validates them, and the conclusion is insensitive (50/38/12 gives 20.2bp).

⚠️ **The absolute and proportional lenses name OPPOSITE winners** (`finding_normalization_choice_picks_opposite_winners`):
- **Absolute:** CCC-led (+32bp, the largest single tier move).
- **Proportional:** BB-led (+12.1% vs CCC +3.3% — CCC widened at **0.27×** BB's rate).

**For the question actually asked — "is this a quality-recognition / default-fear event?" — the proportional lens is the correct instrument.** A genuine tail repricing widens CCC by a *multiple* of BB proportionally. This is the inverse. **It is not quality recognition.**

**What BB-led + CCC-lagging cuts FOR:** a **flow-driven repricing of the liquid top of the capital stack**, not a credit-quality event. BB is the most liquid, most index-representative, longest-duration tier and the one crossover/IG-mandate money holds; CCC is illiquid and slow to mark. Selling pressure hits BB first and leaves CCC behind — exactly the observed shape. Corroborated independently by the cash market in §3.

---

## 2. Geographic controls — the strongest single piece of evidence

| Index | series | 7/22 | 7/29 | Δbp | Δ% | ratio to US HY |
|---|---|---|---|---|---|---|
| **US HY** | `BAMLH0A0HYM2` | 268 | 287 | +19 | +7.1% | 1.00 |
| **Euro HY** | `BAMLHE00EHYIOAS` | 248 | 264 | **+16** | +6.5% | **0.84** |
| EM HY | `BAMLEMHBHYCRPIOAS` | 304 | 311 | +7 | +2.3% | 0.37 |
| US IG | `BAMLC0A0CM` | 78 | 81 | +3 | +3.8% | at beta |
| US IG BBB | `BAMLC0A4CBBB` | 96 | 100 | +4 | +4.2% | **no BBB discrimination** |

**European HY has essentially zero AI-infra issuance — and it widened 0.84× the US move.**

Base-rated against every 5-session window in the trailing 12 months with US HY widening ≥8bp (n=63): **median Euro/US ratio 0.55; the current 0.84 sits at the 70th percentile.** Above-normal European participation — meaningfully so, but not exceptional.

The two nearest analogues by ratio are **Oct-2025 (0.83, 0.84) — global risk-off episodes.** The US-idiosyncratic episodes in the same sample print **0.10–0.37** (Aug-2025 0.10, Nov-2025 0.25–0.28, Mar-2026 0.37). **This window belongs to the global-risk-off family, not the US-specific family.** A US-AI-capex-financing-specific credit event predicts a *low* ratio. We observe a high one.

> ⚠️ **A correction against my own first cut, recorded deliberately.** My initial instrument was a *daily-change* beta of Euro HY on US HY (0.338, corr 0.34), which implied Euro HY over-participated by **2.5×**. That is an artifact: European and US index closes are time-misaligned, which depresses daily correlation and biases the beta down. The **5-session base rate is the correct instrument** and it says 70th percentile, not 2.5×. The weaker, honest number is the one carried into the verdict. (`finding_base_rate_the_instrument_before_its_event_table`.)

**EM HY under-participated** (+7bp vs +11.3bp at its YTD relationship) and **IG participated exactly at beta** (+3bp vs +2.7bp predicted) with **no BBB-tier discrimination** — which independently argues against an idiosyncratic BBB / ORCL-fallen-angel driver inside IG.

---

## 3. Cash-market and rates checks — both cut the same way

**Rates did NOT drive it.** Within the window DGS10 **4.67 → 4.61 (−6bp)** and DGS30 **5.15 → 5.09 (−6bp)** [FRED H.15; 7/29–30 not yet published, `^TYX` proxy 5.147→5.143, flat]. **Treasuries rallied while HY widened.** OAS is spread-over-curve by construction, so this was never a mechanical worry — but it rules out the softer "long-end selloff dragged HY wider" read for the *whole* window, extending my KB-LIQ-088 check (which covered only the 7/23–7/28 leg) to all five sessions.

**The HY cash market shows no distress in price terms.** Raw unadjusted closes:

| | 7/22 | 7/30 | Δ | window range |
|---|---|---|---|---|
| HYG | 79.52 | 79.49 (+0.32% on the day) | **−0.04%** | 79.23–79.52 = **0.4%** |
| JNK | 95.75 | 95.68 | −0.07% | |
| SJNK | 24.86 | 24.85 | −0.02% | |
| ANGL | 28.94 | 28.92 | −0.05% | |

**But turnover roughly doubled:** HYG volume **52.6M [7/23]** and **53.1M [7/29]** vs a ~25M baseline. **Elevated turnover, unmoved price** — a repositioning signature, not a distress signature, and a second independent corroboration of the flow read in §1.

---

## 4. §b — the Goldman / JPM AI-credit basket, read properly

**Terms** [Bloomberg 7/23, via WALTER `SIG-W-20260727-018`]: 18 **equal-weighted** US HY issuers incl. CoreWeave / Applied Digital / Cipher (roster otherwise unpublished) · tickets $50–250M · cash bonds **or TRS** · avg yield 7.45% · **avg spread 319bp**. JPMorgan launched a competing product the same week.

**Where 319 actually sits.** Against my own FRED pulls for **7/23, the launch date** — not the 7/24 comparison WALTER used:

| | 7/23 | basket vs |
|---|---|---|
| HY index | 277 | **+42bp** |
| Single-B | 294 | **+25bp** |
| CCC | 991 | **−672bp** (inside) |

⚠️ **Not like-for-like** — 18 names equal-weighted vs hundreds value-weighted; a point-in-time dealer average with no history. Order-of-magnitude risk premium only, never a tradeable differential.

**Read:** the sell-side struck the first public reference price for AI-infra credit at **roughly a high-single-B risk premium** — 25bp wide of the single-B index and 672bp *inside* the distressed tail. **That is AI credit priced as ordinary high yield, not as a stress locus.** If AI credit were driving the index move, the class's own reference price would not sit a quarter-notch wide of single-B.

**Leading or lagging?** **As a spread series, UNRESOLVED** — there is no second basket print, so the gap-change cannot be computed. (If the basket is still ~319, the index has closed 10bp of the gap since 7/23, i.e. AI credit *lagged*; but that assumes a stale print and I will not lean on it.) **The issuer-level evidence in §5 answers the question the basket cannot: AI credit is leading in magnitude by ~8×.**

**The decisive arithmetic.** AI / data-center HY is **~4–6% of the index by market value** — basis: $31.9B AI-related HY issued through 7/8/26, all but $4.0B data-center-backed [Morningstar]; ~$36B YTD data-center HY tracking to ~$60B by YE-26 [BofA survey]; cumulative outstanding including prior vintages ~$60–90B against index MV ~$1.35–1.45T. **For that cohort alone to produce +19bp of index widening it would have to widen +320 to +475bp.** It did not. Bounding it by observed issuer moves (§5: +50 to +120bp cohort-average, with CRWV the outlier at the top), the AI cohort accounts for **~3–6bp of the +19bp**.

---

## 5. §c — CRWV $2.6B DDTL: the terms are the finding; the outcome is UNRESOLVED

**The facility.** $2.6B first-lien delayed-draw term loan, **Sep-2031** maturity, drawable to Dec-2026, 50bp undrawn fee, **1.35× DSCR covenant**. Morgan Stanley + MUFG joint bookrunners; Goldman Sachs JLA; JPMorgan, Wells Fargo, BBVA, Crédit Agricole, SMBC, PNC, Société Générale participating. **Commitments due noon ET 2026-07-30.** Proceeds fund GPUs against take-or-pay contracts with **Anthropic, Jane Street, Hudson River Trading**. [PitchBook; Bloomberg 7/29]

> ⚠️ **Do not conflate with DDTL 3.0** — a separate, identically-sized $2.6B facility that **closed 2025-07-31** for OpenAI. Multiple syndication write-ups merge the two, and a naive search returns the 2025 "CoreWeave closes $2.6B" press release as if it were this week's outcome. Also distinct from DDTL 4.0 (Mar-2026) and the $3.1B facility (2026).

🔴 **THE FINDING — terms were SWEETENED on 7/29, the day before commitments closed:**

| | talk | revised 7/29 |
|---|---|---|
| Spread | S+425–450 | **S+550** |
| OID | 99 | **97** |
| YTM | 8.53–8.79% | — |

**+100–125bp of spread plus 200bp of OID ≈ +140–165bp all-in yield concession** on a ~5.2yr facility. [Bloomberg 7/29]

**Corroborating issuer-level stress:**
- CRWV CDS **+>50% month-to-date, highest since December** [Bloomberg 7/29].
- CRWV June 9.625% 6yr senior notes priced at par → **96.50 (10.42%)** [Morningstar].
- CRWV equity **82.64 [7/22] → 60.82 [7/29] = −26%**, then +23% to **75.05 [7/30]** into tonight's print. APLD −5.87% over the window. Raw unadjusted closes, yfinance.

**This is the hard evidence that AI-infra credit is repricing violently — ~8× the index move — at the issuer level.** It is also precisely why the cohort still cannot be the index's driver: §4's weight arithmetic caps its contribution at 3–6bp.

🔴 **OUTCOME: UNRESOLVED.** As of my pull **2026-07-30 ~15:20 ET — roughly three hours after the noon deadline** — no public source reports final allocation, final size, or whether the deal cleared, was cut, or was pulled. Syndicated-loan allocations are not SEC-filed; they surface via LevFin Insights / LCD / Bloomberg terminal (paywalled), typically T+0 to T+2. **Where the answer lives:** an 8-K if deemed material, **CRWV's earnings call tonight (7/30)**, or terminal loan-market wires.

⚠️ **Do not read the sweetening as failure. Sweetening to clear IS clearing** — the concession is the price of getting it done, and a deal that prices 165bp wide is a datum about *cost of capital*, not about *access*. The tradeable distinction between "cleared wide" and "pulled" is still open and is worth one follow-up.

---

## 6. What I could NOT reach — the paywall, stated as a finding

**FRED carries no sector-level US HY OAS.** Verified directly against the FRED series-search API this session: the only US HY decompositions published are **rating tiers** (BB / single-B / CCC) plus geography (Euro HY, EM HY). There is no Technology, Telecom, Energy, or Media sub-index. **ICE BofA sector sub-indices exist but are ICE/Bloomberg-terminal only.**

**⇒ A direct sector attribution of the HY index is not obtainable from any free source.** Everything in §1–§5 is a reconstruction from tier structure, geographic controls, cash-market behavior, and issuer-level primaries. That is why the verdict is stated as a **weighted read with ranges**, not a point decomposition — and it is a genuine ceiling on precision, not a gap I can close with more effort. This is the same terminal gate as the HY-breadth series (KB-LIQ-090, FINRA TRACE NTMBHH/NTMBHL).

**Consequence for the energy leg specifically:** my only instrument is XLE (−0.64% over the window), an equity proxy. My own HY Energy OAS figure is **Apr-28, ~3 months stale** and the live pull has been Will-deferred since 6/20. **The energy row in the verdict is Low confidence by construction** — I am asserting "no energy dislocation" on a weak instrument and it should be read that way.

---

## 7. Answer to TERRY's §2 — was a detection watch running?

✅ **Yes, and it fired correctly and on time.**

`AGENTS/LIQUID/alerts/HY_OAS_ALERTS.log`:
```
2026-06-29 13:00  🚨 ESCALATION 🟡yellow→🔴red  HY OAS 283bps (as-of 2026-06-26)
2026-07-28 13:00  🚨 ESCALATION 🟡yellow→🔴red  HY OAS 281bps (as-of 2026-07-27)
```
State file `HY_OAS_STATE` is still red at 287 (obs 7/29, checked 7/30 13:00).

**The cross was detected at the first possible opportunity** — FRED publishes T+1, so the 7/27 observation became available 7/28, and the watcher escalated 7/28 13:00 ET.

🔴 **What failed is DELIVERY, not detection.** The watcher writes to a local log and a state file and **has no routing leg to any consumer.** It fires into a file nobody reads unless they are already inside `AGENTS/LIQUID/`. The same non-delivery happened on the prior fire (6/29) and went equally unnoticed.

**⇒ TERRY's ZONE-1 detection line is not fiction — it is real but undelivered.** TERRY should not re-own it; I should build the routing leg. **That is a routing build, not a threshold change** — I am not touching the gate, and RED's sustain ruling is untouched. Owed at my next session.

---

## 8. TERRY's §4 spec defect — data, not a ruling

REGINALD/NEXUS own the pin and I am not pre-empting it. The measurement is mine, so:

| Reading | 7/22 → 7/29 | Verdict |
|---|---|---|
| Difference (CCC − HY) | 713 → **726bp** | WIDENING |
| Ratio (CCC ÷ HY) | 3.66 → **3.53** | NARROWING |

**My read on which is diagnostic:** for *"is the tail leading?"*, the **ratio** is correct. CCC's level is ~3.5× the index, so an equal *proportional* move mechanically produces a wider *absolute* gap — the difference reading therefore fires on **any** broad widening and has no discriminating power for the question being asked. The ratio discriminates. (`finding_ratio_gauge_denominator_branch`, `finding_normalization_choice_picks_opposite_winners`.)

**TERRY was right not to resolve an ambiguous spec in the direction that fires.** REGINALD/NEXUS still own the pin.

---

## Sources

FRED (own pulls 2026-07-30 ~15:10 ET): `BAMLH0A0HYM2` · `BAMLH0A1HYBB` · `BAMLH0A2HYB` · `BAMLH0A3HYC` · `BAMLC0A0CM` · `BAMLC0A4CBBB` · `BAMLHE00EHYIOAS` · `BAMLEMHBHYCRPIOAS` · `DGS10` / `DGS30` / `DGS2`. yfinance raw unadjusted closes 2026-07-15→07-30 (`auto_adjust=False`). WALTER `SIG-W-20260727-018` (basket), `SIG-W-20260728-002` (NVDA/OpenAI guarantee — **unconfirmed negotiation, not sized**). [Bloomberg 7/29 via Investing.com](https://www.investing.com/news/stock-market-news/coreweave-said-to-sweeten-26-billion-loan-terms-amid-debt-concerns-4821421) · [PitchBook](https://pitchbook.com/news/articles/coreweave-launches-2-6b-term-loan-to-support-acquisition-of-gpus) · [Morningstar](https://www.morningstar.com/bonds/bond-issuance-backing-ai-investment-tops-250b-testing-limits-voracious-investor-demand).
