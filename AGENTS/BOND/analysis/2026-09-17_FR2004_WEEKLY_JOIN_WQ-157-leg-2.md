# FR2004 × AUCTION JOIN — WQ-157 leg ② / DOCKET L271

**BOND · delivered 2026-09-17 ~13:4x ET, one day ahead of the 9/18 date.**
**Instrument:** `monitors/fr2004_join.py` (selftest 12/12), reusing `grade_auction.bench` so the base rate and the live gate are computed by the same code and cannot drift apart.
**Status of the two premises:** CLOSED 9/14 (`analysis/2026-09-14_FR2004_SBN2022-SBN2024_comparability-probe.md`). **This document is the join itself.**

> # 🔴 HEADLINE: THE PAIRING DOES NOT FILTER — IT INVERTS.
> **Across all five candidate dealer legs, auctions where `I'` fired AND the dealer leg was TRUE are followed by 30Y yields FALLING, while `I'` fires WITHOUT the dealer leg are followed by yields RISING.** A demand-hole signal implies yields UP. **The paired test selects the wrong half.**
>
> ⚠️ **AND THAT CONCLUSION FAVOURS ME, WHICH IS WHY I AM NOT ACTING ON IT.** It argues for the LOOSER standalone test — the one that fires ~2× as often and whose firing confirms this desk's own bear thesis. **The tell this desk wrote down for itself is "the fix helps YOU." It does. I recommend nothing; this goes to Will as WQ-157 leg ② evidence, which is what the letter says.**

---

## 1 · WQ-157's open premise — the verdict it asked for

| Question | Verdict |
|---|---|
| **Ceiling** | **n=244**, not 243. SBN2022 **130** + SBN2024 **114**, direct count at the primary, span 2022-01-05 → 2026-09-02. The docket's 243 predated the 9/2 as-of. **VERIFIED.** |
| **Are the bucket definitions comparable across the SBN2022/SBN2024 boundary?** | **POOLING IS DEFENSIBLE — confidence INFERRED, never VERIFIED.** The 2022–23 hiking/SVB stress half is **RETAINED**, so usable n is 244 and not 113. |

**Why only INFERRED, stated because the letter demanded the verdict either way:** there are **ZERO overlapping as-of dates** (SBN2022 ends 2024-06-26, SBN2024 begins 2024-07-03), so **no direct identity test exists at the API**. The evidence is negative-for-a-break: the boundary w/w moves in the two buckets WQ-157 depends on rank at the **0.4th** (11-21Y) and **0.8th** (>21Y) percentile of their own |w/w| distributions — quieter than 99%+ of weeks.

⚠️ **Level continuity is NECESSARY, NOT SUFFICIENT.** A redefinition that preserved levels — same maturity bounds, changed reporting panel or instrument coverage — passes this test unseen. **NAMED UNCHECKED PRIMARY: the NY Fed's own FR2004 form-revision documentation.** It is the authority and it was not consulted. Per this desk's own rule an absence claim does not upgrade to VERIFIED on a proxy.

---

## 2 · The join

**Convention, declared before the numbers because it is the load-bearing design choice.** Dealer warehousing from an auction is a **POST-auction effect** — the dealer takes the paper at 1PM and the inventory appears in the **next** weekly snapshot. So the join is a **DELTA ACROSS** the auction:

```
PRE   = last FR2004 as-of ON OR BEFORE the auction date
POST  = first FR2004 as-of STRICTLY AFTER the auction date
leg   = f(POST − PRE)
```

**A level-beside-it join would grade the stock the dealer held BEFORE the auction it is meant to be judging — the wrong quantity.** An auction with no POST print is **DROPPED, never imputed**: a publication gap must not decide a market question.

| | |
|---|---:|
| FR2004 weekly prints, pooled | **244** |
| Nominal coupon auctions from 2022-01-05 with a full trailing-12 bar | 228 |
| **Joined (PRE and POST both exist)** | **224** |
| Dropped (no POST print yet) | 4 |

---

## 3 · Base rates

| Test | Fires | Rate |
|---|---:|---:|
| **`I'` STANDALONE** (indirect < own trailing-12 P15, STRICT) | 52/224 | **23.2%** |
| **OLD conjunctive** (indirect < min AND dealer > max) | 4/224 | **1.8%** |

### Does pairing filter anything?

| Pairing leg | P(leg \| `I'` fired) | P(leg \| no fire) | Separation | Paired fire rate |
|---|---:|---:|---:|---:|
| long-end TOTAL built (Δ>0) | 69.2% | 59.3% | +9.9pp | 16.1% |
| **long-end TOTAL built >$1B** | **57.7%** | **45.9%** | **+11.8pp** | **13.4%** |
| 11-21Y bucket built | 61.5% | 54.1% | +7.5pp | 14.3% |
| >21Y bucket built | 65.4% | 57.0% | +8.4pp | 15.2% |

**Two-proportion z on the best leg: z=+1.49, two-sided p=0.137 — NOT significant at 0.05.**

⇒ **On its own terms the pairing is weak.** The dealer leg fires after **46–59% of ALL auctions regardless** of composition — it is close to a coin flip — so most of what pairing removes is removed at random. Pairing roughly halves the fire rate (23.2% → 13–16%) largely by discarding fires arbitrarily.

**That was the expected finding. It is not the finding.**

---

## 4 · 🔴 THE FINDING: the paired test is ANTI-PREDICTIVE

The question a kill criterion must survive is not *how often does it fire* but **does firing precede anything**. A composition test that fires and is then followed by yields FALLING is not detecting a demand hole — it is detecting a cheap print that got bought. **This desk registered that exact warning on 2026-09-02** (`MEMORY.md`: *"every indirect-keyed composition failure this desk has carried is followed by TLT UP at the median"*).

**Forward 30Y yield change, +5 sessions after the auction** (`DGS30`, H.15, session closes):

| Group | n | median +5d | % followed by RISING yields |
|---|---:|---:|---:|
| **`I'` FIRED + dealer leg TRUE — the PAIRED kill** | 30 | **−5.0bp** | **27%** |
| `I'` FIRED, dealer leg FALSE | 22 | **+6.5bp** | **68%** |
| no `I'` fire | 172 | +1.0bp | 51% |

**Permutation tests (20,000 resamples, median difference, seed 20260917):**

| Comparison | median diff | p |
|---|---:|---:|
| PAIRED vs `I'`-only-no-leg | **−11.5bp** | **0.009** |
| PAIRED vs no-fire | −6.0bp | **0.030** |
| `I'`-only-no-leg vs no-fire | +5.5bp | 0.058 |

### Robustness — the sign holds across every leg definition tested

| Leg | n paired | med paired | n unpaired | med unpaired | diff | p |
|---|---:|---:|---:|---:|---:|---:|
| long-end TOTAL built >0 | 36 | −4.0 | 16 | +7.0 | −11.0 | **0.015** |
| long-end TOTAL built >$1B | 30 | −5.0 | 22 | +6.5 | −11.5 | **0.009** |
| 11-21Y bucket built | 32 | −1.5 | 20 | +2.0 | −3.5 | 0.356 |
| >21Y bucket built | 34 | −4.0 | 18 | +1.0 | −5.0 | 0.246 |
| long-end built >$2B | 26 | −5.0 | 26 | +4.0 | −9.0 | 0.051 |

**The SIGN is negative in all five. The MAGNITUDE and significance are carried by the long-end TOTAL legs; the per-bucket legs are directionally identical but not significant.** Stated that way rather than as "robust across all definitions," because two of the five are indistinguishable from noise.

**Mechanism — HYPOTHESIS, explicitly not established by this data.** A dealer build after a soft auction may be the absorption that *prevents* the yield rise: the paper found a balance sheet. An `I'` fire *without* a build may mean the paper was distributed at a price, and the price kept moving. **This is a story consistent with the numbers, not a result. Do not cite it as one.**

---

## 5 · ⚠️ LIMITS — read before quoting anything above

1. **Small n where it counts.** The decisive split is **30 vs 22**. Everything in §4 rests on those two cells.
2. **MULTIPLE COMPARISONS, UNADJUSTED AND DISCLOSED.** I tested four legs for separation, then ran the forward test on five. **The p=0.009 is not corrected for that.** Under a crude Bonferroni across five legs the threshold would be 0.01 — the best leg survives, the >$2B leg (0.051) would not, and the two bucket legs never did.
3. **Observations are not independent.** Refunding weeks cluster three auctions into five days sharing one FR2004 delta and overlapping forward windows. The effective n is materially below 224.
4. **One regime.** 2022-01-05 → 2026-09-02 is a hiking cycle into a plateau. The buckets do not exist before that — this is a ceiling, not a choice.
5. **One outcome variable, one horizon.** 30Y at +5 sessions. The +20d picture is muddier (paired +2.5, unpaired −0.5, no-fire +4.0), so **the effect is a short-horizon one and may not persist.**
6. **The join reads published as-ofs, never a nowcast.** Four auctions are dropped for want of a POST print.

---

## 6 · 🔴 A LIVE OPERATIONAL CORRECTION — THE 9/15 FIRE IS NOT PAIRABLE ON 9/18

This desk's surfaces have carried *"the kill leg is unevaluable and the FR2004 leg lands TOMORROW 9/18."* **The instrument lands 9/18. The 9/15 fire's own pairing data does not.**

| | |
|---|---|
| 9/15 20Y-R needs PRE | last as-of ≤ 9/15 = **2026-09-09** |
| 9/15 20Y-R needs POST | first as-of > 9/15 = **2026-09-16** |
| Latest **published** as-of | **2026-09-02** |

**The 9/09 as-of is still unpublished at 13:4x on 9/17 (≥15 days' lag), and the POST print the pairing requires — 9/16 — is TWO prints beyond that.** At the observed cadence **the 9/15 `I'` fire cannot be paired until roughly EARLY OCTOBER.**

⇒ **"The kill leg becomes evaluable on 9/18" is wrong and should be corrected on every surface carrying it.** 9/18 is the date the *instrument* exists. The *9/15 fire* stays UNEVALUABLE for about another two weeks — and that is a property of the publisher, not of the market.

---

## 7 · What this desk is and is not asking for

**NOT PROPOSING A CHANGE.** Per L271, leg ② goes to Will as a WQ ask **after** the join lands. It has landed; the ask is PROME's to register and Will's to rule.

**The evidence, stated neutrally:**
- The pairing as conceived (dealer stock building across the auction) **does not separate significantly** (p=0.137) and **inverts the forward relationship** (p=0.009 on the best leg, sign consistent across five).
- The `I'` standalone fires 23.2% and its fires **are** followed by rising yields (68% up at +5d) — the behaviour a demand-hole marker should show.
- **A funding leg was NOT tested.** The letter names *"FR2004 dealer long-end stock **and/or SOFR−IORB**"*; this join covers the stock leg only. **SOFR−IORB is untested and is the obvious next candidate** — it is a *stress* measure rather than an *absorption* measure, and absorption appears to be the thing pointing the wrong way. **A recommendation to drop pairing would be premature while half the letter's own instrument set is unmeasured.**

⚠️ **DIRECTION DISCLOSED, RESTATED HERE BECAUSE IT IS THE MOST IMPORTANT SENTENCE IN THE DOCUMENT: every conclusion above favours a LOOSER kill that fires more often and confirms this desk's own bear thesis. This desk has written down that the tell for a self-serving re-tune is "the fix helps YOU." It does. Nothing is changed on BOND's authority.**

---

## 8 · Reproduce

```
../../.venv/bin/python3 monitors/fr2004_join.py            # join + base rates + forward test
../../.venv/bin/python3 monitors/fr2004_join.py --selftest # 12 assertions
```

Join convention, ceiling, comparability limits and the "separation, not fire rate" instruction are written into the tool's docstring, so they travel with the numbers rather than living only here.
