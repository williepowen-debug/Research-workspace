# P6 — EU GAS STORAGE → CRUDE: **KILL-OR-KEEP TEST · PRE-REGISTRATION**

**⛔ WRITTEN BEFORE ANY DATA WAS PULLED. 2026-08-13 ~13:0x ET.** *(Discipline carried from today's P1/P3 work and from `[[finding_prereg_verdict_boundary_must_be_a_number]]`: the verdict rule must be a NUMBER plus a NO-VERDICT band, written before looking, or the outcome gets fitted.)*
**Authority:** Will green-lit P6 as **I** scoped it — the **kill-or-keep** version, not the obvious "build a storage instrument" version.

---

## 1. THE QUESTION — deliberately narrow

> **Does EU gas-storage state transmit to CRUDE — i.e. to BRENT's domain — at all?**
> **Not** "is EU storage low" (it is: 59.32%, lowest for the date in five years). **Not** "does storage matter to gas" (obviously). **Only:** does knowing EU storage state tell me anything about **crude** that I do not already know?

**If NO → KILL:** no BRENT instrument, no level, no registry row; **route the feed and everything I learned this week to its proper owner.**
**If YES → SPEC ONLY:** what instrument, what base rate, numbers to Will **as a proposal**. **Nothing enters a registry either way.**

## 2. MY STATED PRIOR — recorded so the verdict can be checked against it

**I expect KILL.** Two reasons, both pre-existing:
1. **The book has no gas leg.** Every live expression (USO ×3, XLE) is crude/energy-equity.
2. **DR-5's measured result:** a confirmed, FM-backed **17% Qatari LNG supply loss produced NO upward price response for ~3.5 months**; both benchmarks sat ~24% BELOW pre-strike three months on, and transmission arrived ~4 months late **through storage, not spot**. **If a 17% physical loss did not move gas promptly, a storage percentage moving crude is a strong claim.**

⚠️ **A stated prior cuts both ways and that is the point:** it makes a KILL verdict cheap and a KEEP verdict expensive. **I must not let it do the work the data should do** — so the bars below are set to be *passable*, and I commit to reporting a pass if it happens.

## 3. INSTRUMENTS — named before use

| leg | series | source | basis |
|---|---|---|---|
| **Storage state** | EU aggregate fill, `full` field, **% of working gas volume**, gas-day basis | GIE AGSI+ `agsi.gie.eu/api/data/eu` (wired today, `gie:` probe, `total==0` guard, browser-UA caveat) | daily |
| **Crude** | **Dated Brent, `DCOILBRENTEU`, USD/bbl** — the PHYSICAL leg, per my own 8/12 basis canon | FRED | daily |
| **Crude (robustness)** | ICE front-month futures `BZ=F`, USD/bbl | yfinance | daily |
| **Gas control** | TTF `TTF=F`, EUR/MWh | yfinance | daily |

**Why Dated Brent is the primary crude leg:** my own ruled canon says the **physical** spot is the war-premium/physical instrument and futures govern graded machine state. A storage→crude transmission, if real, is a **physical substitution** story (gas-to-oil switching, power-sector fuel choice), so the physical leg is the right test. **Futures are the robustness check, not the headline.**

## 4. ⚑ THE TRANSMISSION MECHANISM I AM TESTING — named, because an unnamed mechanism cannot be falsified

`[[finding_hypothesis_needs_an_instrument_for_its_defining_mechanism]]`

**Mechanism: GAS-TO-OIL SWITCHING.** If EU gas storage is critically low, European power/industry substitutes toward oil products (fuel oil, diesel gensets, crude-burn), which lifts **crude** demand. **This is the ONLY channel by which a storage percentage should reach my domain.** It predicts:
- Storage **deficit** (low fill vs seasonal norm) → crude **UP**, with a lag of **weeks, not days** (procurement/switching is slow).
- The effect should be **stronger in the physical (Dated) leg than in futures**, because switching is a cargo-buying decision.

⛔ **Anything else — "both moved because of the war" — is a SHARED ANTECEDENT, not transmission.** `[[finding_shared_antecedent_independence_test]]`. **That is the single biggest way this test can produce a false KEEP**, and §5's control exists for it.

## 5. THE DISCRIMINATOR — numbers fixed now

**Storage deficit metric:** `DEFICIT(t) = fill%(t) − mean(fill% on the same calendar day, prior available years)` — a **seasonal** deviation, because raw fill% is ~90% seasonality and would produce a spurious correlation with anything trending.

**Test A — level/lag correlation.** Spearman ρ between `DEFICIT(t)` and forward Dated-Brent return over **h ∈ {5, 10, 21, 42} trading days**.
**Test B — the CONTROL that decides false-KEEP.** The same correlation for **TTF**. **If storage predicts TTF but NOT crude, the channel is gas-only and my domain is unaffected.**
**Test C — shared-antecedent guard.** Any crude correlation must **survive** as a partial correlation controlling for TTF. **If crude's relationship to storage runs entirely through gas prices, it is not an independent instrument — it is TTF with extra steps, and TTF is not mine either.**

### ⇒ VERDICT RULE (fixed before looking)

| outcome | condition |
|---|---|
| **KEEP** *(spec only)* | \|ρ\| ≥ **0.35** vs Dated Brent at **any** h ∈ {5,10,21,42}, **AND** the sign matches the mechanism (deficit → crude UP), **AND** it survives the TTF partial (Test C), **AND** n ≥ 200 overlapping observations |
| **NO-VERDICT** | 0.20 ≤ \|ρ\| < 0.35, or the sign is right but Test C kills it, or n < 200 |
| **KILL** | \|ρ\| < **0.20** at every horizon, **or** the sign is backwards, **or** the relationship is entirely explained by TTF |

**⚠️ The 0.35 bar is deliberately LOW for a tradeable signal** — I am not testing "is this a trade," I am testing "does this channel exist at all." **A channel that cannot clear ρ=0.35 in-sample, with overlapping windows inflating the apparent significance, is not a channel I should spend attention on.**

## 6. ⛔ WHAT I ALREADY KNOW WILL LIMIT THIS — stated before, not after

- **Overlapping forward windows inflate significance.** h=42 on daily data is ~42× overlapping. **I will NOT quote a p-value**; ρ and n only. This is why the bar is a *magnitude*, not a significance test.
- **Small n of genuine undershoot episodes** (~2022, 2025, 2026). **If the AGSI history is short, the honest answer is "cannot tell," NOT "no effect."** `[[finding_effect_below_instrument_detection_floor]]` — below the detection floor is **no evidence**, not weak evidence.
- **2022 is a regime unto itself** (Nord Stream). A correlation driven entirely by 2022 is a **single episode**, not a base rate.
- ⛔ **This is a DOMAIN-FIT test, not a threshold build.** My own prohibition stands: **registering a level the day the feed unblocked is exactly the un-base-rated adoption I refuse elsewhere.** Even a KEEP produces a **spec with numbers to Will**, never a registration.

## 7. ROUTING ON KILL — decided now, so the verdict is not a dead end

On KILL the feed goes to its proper owner **with everything I learned this week attached, so the recipient re-learns nothing**:
1. the **`gie:` probe grammar** and that the gate is the **User-Agent, not a key** (the server's error text misnames its own discriminator);
2. the **`total==0` fail-loud guard** — AGSI returns HTTP 200 with an empty payload on malformed queries *and* on UA denial;
3. the **undocumented-keyless caveat** — it can tighten without notice; the free GIE key is the robust path (Will queue row 37, hardening-only);
4. the **DR-4 binding-rule correction**: 90% target over a **flexible 1 Oct – 1 Dec** window with 10% deviation, **NOT a 1 Nov deadline**;
5. the measured state: **59.32% [gas day 8/11], lowest for the date in 5 years, below even 2022; 90% needs 1.49× the four-year best pace; landing zone 77–80%.**

**Recipient named on the verdict, not now** — it depends on whether the residual value is *gas-market* (SAM: Japan/LNG cargo competition) or *climate/demand* (AEOLUS: winter heating demand). ⚠️ **AEOLUS has a live Will-driven session — I will route by PACKET only and touch nothing of theirs.**

---
---

# ⚖️ VERDICT — **KILL** *(run 2026-08-13 ~13:3x ET, against the pre-registration above, unedited)*

## Data actually obtained — better than I feared on n, which removes my main escape hatch

| leg | obs | range |
|---|---:|---|
| GIE AGSI+ EU fill % | **5,702** | 2011-01-01 → 2026-08-11 |
| Dated Brent `DCOILBRENTEU` | 3,950 | 2011 → 2026 |
| `BZ=F` | 3,897 | 2011 → 2026 |
| `TTF=F` | 2,214 | — |
| **DEFICIT observations** (≥3 prior years required) | **4,604** | range **−20.3 … +24.5 pp** |

⇒ **n ≥ 200 is satisfied ~23× over. The "underpowered, cannot tell" escape does NOT apply** — this is a real measurement, not a detection-floor problem.
**Today sits at DEFICIT = −16.91 pp — near the bottom of a 15-year range.** We are testing the channel from inside its most extreme regime.

## TEST A / B / C — pre-registered, full sample

| h | n | **ρ Dated Brent** | ρ `BZ=F` | ρ TTF | **partial (crude \| TTF)** |
|---:|---:|---:|---:|---:|---:|
| 5 | 4,597 | **−0.055** | −0.052 | −0.139 | −0.040 |
| 10 | 4,590 | **−0.082** | −0.072 | −0.186 | −0.066 |
| 21 | 4,575 | **−0.104** | −0.115 | −0.211 | −0.091 |
| 42 | 4,543 | **−0.101** | −0.110 | −0.235 | −0.067 |

**⇒ `|ρ|` vs crude is 0.055–0.104 — BELOW the 0.20 KILL floor at EVERY horizon.** **VERDICT RULE ⇒ KILL.**

✅ **The SIGN is correct** (negative: deeper deficit → higher forward crude), so the mechanism is not backwards — **it is simply far too weak to be an instrument.** Reporting that honestly because it is the half that favours the hypothesis.
✅ **Test B is decisive and points where I expected: storage predicts TTF 2–3× more strongly than crude at every horizon** (−0.139…−0.235 vs −0.055…−0.104). **The channel is GAS-SIDE.**
✅ **Test C: controlling for TTF shrinks crude's already-sub-threshold relationship further** (−0.040…−0.091). **What little crude signal exists runs THROUGH gas prices — it is TTF with extra steps, and TTF is not mine either.**
✅ **Excluding 2022 (Nord Stream) changes nothing:** crude −0.055/−0.076/−0.071 at h=10/21/42. **The result is not a single-regime artifact.**

## ⛔ ADVERSARIAL CHECK — I tried to REFUTE my own KILL, and one cell cleared the bar. Reporting it, and NOT converting it.

A full-sample rank correlation would miss a **threshold effect that only exists at extreme deficits** — which is exactly today's regime. So I cut the tail:

| subsample | h=10 | h=21 | **h=42** |
|---|---:|---:|---:|
| DEFICIT ≤ −8pp (n≈1,255) | −0.191 | −0.208 | −0.126 |
| **DEFICIT ≤ −12pp (n≈738)** | −0.163 | −0.265 | **−0.373 ← clears the 0.35 KEEP bar** |
| *(TTF in the same deepest tail)* | *+0.006* | *−0.084* | *−0.106* |

**On a literal reading, deepest-tail h=42 is a KEEP: |ρ| = 0.373 ≥ 0.35, correct sign, and TTF is ~0 so it survives Test C.**

### ⇒ I am NOT calling it a KEEP. Three reasons, and the third is fatal.

1. **IT WAS NOT PRE-REGISTERED.** My prereg specified the **full sample**. The −8/−12pp cuts are cuts **I invented after seeing the full-sample result** — 2 thresholds × 3 horizons = **6 extra tests**, of which **one** cleared. That is an exploratory search reported as if confirmatory, and it is precisely the anchor-fitting I killed the 35b incumbent band for this week (**`FUEL SPENT` fired on 1 of 8 anchors**). **I will not do to myself what I refused to accept from a band.**
2. **EFFECTIVE n IS ~7, NOT 767.** The deepest tail is **767 overlapping daily rows drawn from SEVEN contiguous episodes**: 2015-03→07 · 2017-01→03 · 2017-05 (1 day) · 2018-02→06 · **2021-05→2022-03 (319 days)** · 2026-01→03 · **2026-05→08 (75 days)**. At a 42-day forward window the rows inside an episode are near-duplicates. **ρ on ~7 episodes is not a base rate.**
3. ⛔ **THE TWO DOMINANT EPISODES ARE THE SHARED-ANTECEDENT CASE MY OWN PREREG NAMED AS THE #1 FALSE-KEEP RISK.** 2021-05→2022-03 (319d) and 2026 (212d combined) are **69% of the tail**, and in *both* crude rose for reasons with **nothing to do with European gas storage** — the post-COVID crude recovery, and the Hormuz cycle. **"Low storage AND rising crude" in those windows is two symptoms of one antecedent, not transmission.** `[[finding_shared_antecedent_independence_test]]`

**⇒ The tail residual is DOCUMENTED AND ROUTED, not adopted.** It is a hypothesis worth someone testing **out-of-sample**; it is not evidence today.

## 📌 FINAL VERDICT

> ### **KILL — no BRENT instrument, no level, no registry row.**
> EU gas storage does **not** transmit to crude at any strength worth my attention. Where it transmits is **gas** (TTF), and the little that reaches crude runs through gas prices. **This is a feed that belongs on another desk.**
> ✅ **This vindicates the scoped-down framing:** the obvious version of P6 would have built a storage instrument on my desk. **The kill-or-keep version cost one part-session and returns a clean negative — and "don't build it" is a real answer.** `[[finding_base_rate_the_threshold_before_building_it]]`
> ⚠️ **What this does NOT say:** it does not say EU storage is unimportant, or that 59.32% is not alarming. It says **it is not BRENT's instrument.** DR-5 already showed the same shape from the other side — a 17% Qatari LNG loss that moved gas prices *down* for 3.5 months.
