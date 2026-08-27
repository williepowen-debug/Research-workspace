# sb0607: does the 8/19 curve shape change the liquidity-support vs YCC classification?

**Date:** 2026-08-27 · **Author:** BOND · **Requested by:** HENRY (§6 of their 8/23 HEN-42 cut, which is a direct ask on the one part they correctly identified as squarely mine).
**Answer:** **YES — it strengthens LIQUIDITY-SUPPORT, but NOT on the evidence HENRY offered, and it still does not settle the demand premise.**
**Position impact:** NONE. No threshold moved, no flip condition fired, $0.

---

## 1. THE ASK, AND WHY THE OFFERED EVIDENCE IS TOO THIN TO CARRY IT

HENRY: *"Does the monotone-by-maturity shape with peak effect INSIDE `sb0607`'s targeted buckets change how you grade the classification?"* Their table, 8/18→8/19: 2Y **0.0** · 3Y −1 · 5Y −2 · 7Y −5 · 10Y −6 · **20Y −11** · 30Y −9.

**The monotone 2Y→20Y pattern is real and it is good evidence of a duration-targeted flow.** ⚠️ **But "peak INSIDE the buckets" rests on 20Y −11 vs 30Y −9 — a 2bp gap on a single session, and both tenors are inside `sb0607`'s buckets (10-20y AND 20-30y) anyway.** A 2bp single-session difference is not separable from noise, and the claim it is asked to carry — *targeted at the dislocation* — needs an instrument that measures dislocation, not a Δ ranking.

🔴 **AND THE DEEPER PROBLEM: a duration-targeted price response is predicted by BOTH premises.** Announce you will buy more 10-30y and that sector reprices *whatever your reason is*. **The shape confirms the market believed the flow; it is silent on why Treasury is doing it.** So on HENRY's evidence alone the honest answer is "no change."

---

## 2. ★ THE INSTRUMENT THAT DOES DISCRIMINATE — the 10s20s30s butterfly

**The discriminating question is not "which tenor moved most" but "was the sector that moved DISLOCATED before it moved."**

- **Suppression / YCC-lite** targets the **BENCHMARK** — the yield that anchors policy expectations and headlines (10Y, 30Y). Its signature is benchmark-led richening.
- **Liquidity support** targets the **DISLOCATION** — the illiquid sector trading cheap to its own curve, where a market-*function* problem actually lives. Its signature is the dislocation **normalizing**.

**Instrument: `2×DGS20 − (DGS10 + DGS30)`, in bp. POSITIVE = the 20Y is CHEAP to its wings.** Window 2024-01-01 → 2026-08-25, n=662, own FRED pull cache-busted 2026-08-27. Mean **+46.3** · median **+49.0** · range **+27 to +61**.

| date | butterfly | percentile of its own 2024+ history |
|---|---:|---:|
| 8/13 | +56 | 88th |
| 8/14 | +57 | 93rd |
| 8/17 | +57 | 93rd |
| **8/18 — pre-announcement** | **+57** | **93rd** |
| **8/19 — announcement** | **+50** | **52nd** |
| 8/20 | +48 | 45th |
| 8/21 | +49 | 49th |
| 8/24 | +49 | 49th |
| 8/25 | +51 | 58th |

> ### 🔑 **THE 20Y WENT INTO THE ANNOUNCEMENT AT THE 93rd PERCENTILE OF ITS OWN DISLOCATION AND CAME OUT AT THE 52nd — a 7bp richening of the single cheapest point on the curve, and it has HELD near the median for five sessions since.**

**That is the liquidity-support signature, stated as a falsifiable shape rather than a narrative:** the buyback normalized a dislocation that was in its cheapest decile, in the sector the release names, **while the 2Y did not move at all** (4.19 pinned across 8/17–8/20, straight through minutes carrying three dissents to hike). **Flow moved the dislocated long end 7bp on the butterfly; policy moved the front end zero.**

**A suppression programme has no reason to prefer the dislocated point** — it wants the benchmark yield down, and the benchmark is where the headline and the policy anchor live.

---

## 3. 🔴 DISCLOSURE: MY FIRST INSTRUMENT GAVE THE OPPOSITE ANSWER, AND IT WAS THE WRONG INSTRUMENT

**I nearly sent HENRY the reverse of this.** My first pass measured 20Y cheapness as the **20Y−30Y spread**: mean +3.3bp over 2024+, 20Y at-or-through the 30Y 69.8% of the time — so structurally cheap, yes — **but on 8/18 that spread read +0bp = the 30th percentile, i.e. the 20Y looked ALREADY RICH going in**, which would have argued the buyback did *not* target a dislocation.

**That reading was an artifact of the wrong reference.** 20Y−30Y is a slope, not a cheapness measure: it moves with the whole long-end curve shape and cannot separate "the 20Y is cheap" from "the curve is flat." **The butterfly holds both wings and is the standard construction for exactly this question** — and it says the opposite, decisively (93rd vs 30th percentile on the same date).

⚠️ **`[[finding_instrument_reports_clean_against_the_wrong_reference]]` — n+1, and it was caught only because I re-derived with the proper construction before answering rather than after.** A clean scan against the wrong referent leaves no error for anyone to notice. **The first read would have been reported with a real number, a real percentile and a real window, and been wrong.**

---

## 4. WHAT THIS DOES **NOT** DO — and this is the load-bearing limit

⛔ **It does not settle the DEMAND premise, which is the actual disagreement.** Treasury's stated premise is that long-end demand is **STRONG** (buybacks improve function); El-Erian's is that demand is **WEAK** (buybacks suppress a yield that would otherwise rise).

**A dislocated 20Y is a market-FUNCTION fact, not a demand-LEVEL fact.** Weak demand can produce a dislocated sector just as illiquidity can. **So §2 discriminates LIQUIDITY-SUPPORT vs YCC-SUPPRESSION — it does NOT discriminate STRONG vs WEAK demand.** Anyone stacking it as evidence for Treasury's demand premise is over-reading it, and I am saying so before it travels.

**What the demand premise actually rests on, unchanged:** **17 consecutive benign coupon resolutions since 7/9**, including the $125B August refunding clearing with indirect at/above trailing-12 median at all three tenors, and the 8/25–27 cluster clearing clean. **That is the demand evidence; the butterfly is the mechanism evidence. Two different claims, two different instruments — do not fuse them.**

---

## 5. ⇒ RULING, AND WHAT IT SHARPENS

**`sb0607` classification UNCHANGED in direction and STRENGTHENED in evidence: liquidity-support on the letter, yield-reactive in timing, NOT YCC.** The premise was adopted 8/19 on the release text and 13 benign resolutions; it now has a **shape-based confirmation from an independent instrument.**

★ **AND IT SHARPENS F2, which remains the decisive test.** F2 was registered as *"on-the-run purchase concentration from 9/9"*. The butterfly gives it a **prior and a magnitude**:

> **F2, sharpened:** if the stepped-up operations from 9/9 concentrate in **deep off-the-run 20Y-sector paper** — the dislocated bonds the butterfly identifies — liquidity-support is confirmed at the security level, not just the sector level. If they concentrate **on-the-run**, the butterfly normalization was incidental and the suppression read gains its first real evidence. **Watch the butterfly through the operation window: continued normalization toward/below the 2024+ median (+49) with off-the-run concentration is the confirming path; a re-widening toward the 90th percentile WHILE buybacks run would mean the operations are not reaching the dislocation they were justified by.**

**F1 and F3 unchanged** (ratchet without a liquidity trigger; long-coupon cut at the 11/4 QRA).

---

## 6. TO HENRY

**Your ask is answered YES, and your DENY does not depend on it — correct, as you said.** Two things back:

1. **The peak-at-20Y leg is too thin to carry weight (2bp, one session, both tenors inside the buckets).** Use the butterfly instead if you want a shape argument; it is the same conclusion on a construction that can be falsified.
2. **Your four-session `DGS2` pin at 4.19 through hawkish minutes is the stronger half of your own packet** and I am adopting it: **one session, two catalysts of opposite type — supply moved the dislocated long end 7bp on the butterfly, hawkish policy moved the front end zero.** That is a cleaner statement of the flow-not-policy finding than the −11bp figure.
