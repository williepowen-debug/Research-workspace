# PRE-REGISTRATION — the FUNDING leg of WQ-157's pairing instrument (SOFR−IORB)

**BOND · written and committed 2026-09-17 ~13:5x ET, BEFORE any forward-outcome computation.**
**Scope:** L271 names the pairing instrument as *"FR2004 dealer long-end stock **and/or SOFR−IORB**."* The stock leg was measured and delivered today (`analysis/2026-09-17_FR2004_WEEKLY_JOIN_WQ-157-leg-2.md`). **This registers the funding leg before it is looked at.** Tasked by PROME as a Tier-1 follow-up inside the already-approved WQ-157 workstream — a BUILD, not a ruling; the leg ② ruling stays Will's.

> **WHY THIS DOCUMENT EXISTS AND IS COMMITTED FIRST.** The stock-leg result was startling and it favoured this desk. The single thing that would make a funding-leg result worth anything is that its specification was fixed before its outcome was visible. Everything below is written with the spread's own distribution in hand and **with zero forward returns computed.**

---

## 1 · What has been looked at (declared, so the boundary is auditable)

**LOOKED AT:** the SOFR−IORB spread's own unconditional distribution, 2022-01-05 → 2026-09-16, n=1,172 business days, FRED `SOFR` and `IORB`:

| | bp |
|---|---:|
| min | −21.0 |
| p05 | −12.0 |
| **median** | **−9.0** |
| p90 | 0.0 |
| p95 | +3.0 |
| max | +32.0 |
| mean / sd | −6.65 / 5.65 |

P(spread > 0) = **10.0%** · P(> +2) = 6.7% · P(> +3) = 5.7% · P(> +5) = 3.9%.

**NOT LOOKED AT:** any forward yield or price outcome conditional on any of this; any join of the spread to auction dates; any cross-tab of the spread with `I'` fires.

---

## 2 · The legs, fixed now

`t` = auction date. All in bp, `SOFR − IORB`, FRED, as first published, business days.

| ID | Leg | Rationale |
|---|---|---|
| **F1** | spread **> 0** on `t` | The desk's own existing registered language is *"SOFR−IORB positive"* (`VX-BND-04`, `monitors/DEALER_CAPACITY.md`). F1 is that clause, unchanged. |
| **F2** | spread **> 0 on any day in [t, t+5]** | Funding stress from absorbing an auction is a POST-auction effect, the same logic that made the stock join a delta-across. |
| **F3** | **max** spread over [t, t+5] **> +3** (p95) | A severity version of F2. |
| **F4** | **rose across the auction:** mean[t+1,t+5] − mean[t−5,t−1] **> 0** | A pure delta, matching the stock leg's construction, immune to the level regime. |
| **F5** | spread ≥ its own **trailing-60-business-day 90th percentile** on `t` | Regime-relative, so a structurally tighter or looser era cannot decide it. |

**Primary leg, named now so it cannot be chosen after the fact: F2.** It is the closest funding analogue to the stock leg's delta-across construction while preserving the desk's registered "positive" threshold. F1/F3/F4/F5 are secondary and reported for sign-consistency only.

---

## 3 · Outcome, test and seed — identical to the stock leg, deliberately

- **Outcome:** `DGS30` (H.15, session closes, as first published) change from `t` to `t+5` sessions, in bp. **Secondary:** `t` to `t+20`.
- **Statistic:** median difference between groups.
- **Test:** two-sided permutation, **20,000 resamples, seed 20260917** — the same seed used for the stock leg, so the two are directly comparable and neither was re-seeded to taste.
- **Separation test:** two-proportion z on P(leg | `I'` fired) vs P(leg | not fired).
- **Universe:** the same 224 joined nominal coupon auctions, 2022-01-05 forward.

---

## 4 · Hypotheses, stated as falsifiable claims

**H1 (separation).** P(F2 | `I'` fired) > P(F2 | `I'` did not fire).
**H2 — THE ONE THAT MATTERS.** Among `I'` fires, those WITH F2 are followed by a **HIGHER** median 30Y change at +5d than those WITHOUT it. *That is, the funding leg points the way a demand-hole confirmation should point — the opposite of what the dealer-STOCK leg did (paired −5.0bp vs unpaired +6.5bp, p=0.009).*

**H2 is the claim that would RESCUE pairing.**

---

## 5 · Decision rules, fixed before the numbers

1. **POWER FLOOR, AND IT IS THE LIKELY OUTCOME — SAID OUT LOUD NOW SO A NULL CANNOT BE SPUN LATER.** `I'` fires on 23.2% of auctions; the spread is positive on ~10% of days. **If the two were independent the paired cell would hold ≈2.3% of 224 ≈ 5 auctions.** ⇒ **If the paired cell has n < 10, the result is reported as UNDERPOWERED — NOT as evidence for or against H2, and NOT as "the funding leg fails."** An underpowered cell is a statement about the sample, never about the world.
2. **Multiple comparisons, pre-committed:** five legs ⇒ Bonferroni α = 0.05/5 = **0.01** for any headline claim. Anything between 0.01 and 0.05 is reported as SUGGESTIVE, never as significant.
3. **No leg is added, dropped or re-thresholded after seeing an outcome.** If none of F1–F5 works, that is the finding.
4. **The primary leg is F2 regardless of which leg performs best.** A better-performing secondary leg is reported as exploratory.
5. **No recommendation either way.** This is a build. Leg ② is Will's ruling.

---

## 6 · ⚠️ DIRECTION DISCLOSURE — and it runs the OTHER way this time

The stock-leg result favoured this desk: it argued for a looser standalone kill that fires ~2× as often and confirms BOND's own bear thesis.

**A CONFIRMATION of H2 here would CUT AGAINST that** — it would rescue pairing, keep the kill tight, and undercut the finding this desk delivered four hours ago.

**So the success direction of this test is the one that does NOT flatter me, and the null direction is the one that does.** That asymmetry is stated now, before the numbers, because it is the reason this particular pre-registration is worth committing: **the incentive here is to under-find, and naming that is the only defence against it.**

---

## 7 · What gets published

The result, whichever way it falls, including an underpowered null — with the paired cell's n stated in the first sentence.
