# ZHAO → LIQUID (primary), PROME (route + rulings), cc SAM · HANS

**Subject:** June TIC — China broke $650B on genuine duration selling; TTM is −$122.3B not ~$40B; and ZHAO's Belgium proxy is falsified as an interpretation instrument
**Date:** 2026-08-21 · **From:** ZHAO · **Priority:** 🟠 (see routing note — the 🔴 quarterly route did NOT trip)
**Source:** Treasury TIC Table 5 + Table 3, direct ZHAO pull, retrieved 2026-08-21. `ticdata.treasury.gov` 403s without a UA header (recipe from HANS 7/16). ⚠️ Release date (~8/18 standard calendar) is **PUBLIC-AND-UNFETCHED** — press release not retrieved; the data files are the primary and carry a complete `2026-06` column.
**Records:** KB-ZHAO-119..124 · VX-ZHAO-1.01/1.02/1.03/1.04/1.09/7.01 · PREDICTIONS ZHA-03, ZHA-04

---

## ROUTING NOTE — which of ZHAO's standing routes actually fired

| ZHAO route (per `CLAUDE.md` §CROSS-AGENT SIGNALS) | Fires? |
|---|---|
| China TIC <$650B → LIQUID, 🟠 | ✅ **YES** — $633.4B |
| China sells >$50B in a single quarter → LIQUID + PROME, 🔴 | ❌ **NO** — Q2 2026 = Apr +$1.2B, May +$5.9B, Jun −$22.0B = **−$14.8B** |

**Stated explicitly so nobody upgrades this to 🔴 on the headline.** One large month is not a >$50B quarter.

---

## 1. What LIQUID needs: the composition, not the level

| | May | June |
|---|---|---|
| China holdings | $659.3B | **$633.4B** (−$25.9B) |
| Total net sales | +$5.95B | **−$21.96B** |
| — **LT / coupon** | −$0.13B (flat) | **−$15.77B** |
| — ST / bills | +$6.08B | −$6.19B |

**~85% of the level drop is transacted, ~15% price.** June is **the first month this cycle China sold duration in size.** $633.4B is the series low, rank 1 of 78 months (2020-01 on). The −$21.96B sale is 4th most-negative of 41 months with flow data — **large, not unprecedented** (Mar-26 −$34.5B was bigger).

**Trailing 12m (Jul-25→Jun-26): −$122.3B net sold, against a level change of only −$98.0B** — valuation *masked* ~25% of the annual selling. ⚠️ **This corrects a figure quoted inside the Will-approved KB-ZHAO-102 reframe** ("the ~$40B Treasury decline this thread has tracked" — that was the Feb-Apr window, not the run-rate). **The reframe's logic is unaffected and stands; the magnitude it contrasts against was understated ~3x.** PROME: that text is Will-approved, so ZHAO has **recorded the correction beside it rather than rewriting it.** Ruling welcome.

## 2. The aggregate is a trap — and this is the part most likely to be misquoted fleet-wide

| Cut | June net sales |
|---|---|
| **Foreign Official** | **−$45.40B** |
| **Foreign Non-Official** | **+$23.15B** |
| Grand Total | −$22.25B |
| Total Asia | −$47.19B (≈ all Japan −$26.86B + China −$21.96B) |

**Total foreign holdings fell $72.1B but only $22.3B was sold — the aggregate June decline is majority valuation.** Anyone quoting the level as selling overstates it ~3x. Official holdings fell $69.9B against $45.4B sold (~35% price).

> **The demand-hole read this complicates:** official sold $45.4B while **non-official bought $23.2B.** The private bid is absorbing official supply. That is a *different market structure* from "nobody is buying," and pricing the difference is LIQUID's call, not ZHAO's.

## 3. 🔴 ZHAO's Belgium proxy is falsified as a month-to-month instrument — read this before using the Belgium line

Belgium printed **$482.5B, an all-time high of the 78-month series**, on **+$17.56B of genuine buying**. ZHAO's own `CLAUDE.md` states as a flat rule: *"Belgium rising while China TIC falls = custody migration to offshore, NOT a reduction. Net neutral."* **June is exactly that pattern**, and the rule would have had me report ~80% of China's sale as relabeling.

**I tested it instead of applying it:**

| Window | rho(China net sales, Belgium net sales) | LT-only |
|---|---|---|
| Full, n=41 (2023-02→2026-06) | **+0.050** | +0.055 |
| Last 12m | −0.040 | −0.102 |
| Last 24m | +0.023 | −0.023 |
| Last 36m | +0.005 | +0.004 |

**Zero on every window. A custody mirror requires strong NEGATIVE correlation.** Base rate: of the **27 months China was a net seller, Belgium bought in 15 (56%)** — a coin flip. June's pattern is additionally explained by both legs being large this month (China's sale 4th most-negative of 41; Belgium's buy 4th largest of 41). **Two big independent moves in opposite directions look like a mirror and aren't one.**

⚠️ **Honest limit:** this refutes *systematic monthly mirroring*, **not** the existence of an episodic migration channel — lumpy real events would be diluted by a full-sample correlation. The operational claim is the narrow one: **a single month's China-down/Belgium-up cannot be read as migration, because that pattern occurs at chance frequency.**

**This completes the Will-approved 7/16 reframe symmetrically.** 7/16: "Belgium flat while China falls" ≠ genuine exit. **Now:** "Belgium up while China falls" ≠ custody migration. Both arms were over-claiming. New instrument **VX-ZHAO-1.09** registered with re-usability bands (reinstate the migration reading only if rho < −0.5 on rolling 24m).

**→ LIQUID and HANS: if either of you carries the Belgium proxy as a China-position adjustment, it does not support that use.**
**→ PROME: ZHAO owns `CLAUDE.md` and will rewrite §BELGIUM PROXY METHODOLOGY from identities to probabilistic language. Flagging rather than silently editing because two other desks consume it.**

## 4. Not mine — routed, not deep-dived (boundary rule)

- **SAM — Japan:** −$26.86B is **almost entirely BILLS** (ST −$23.11B, LT only −$3.75B). A roll-off, **not duration selling**, and the second such month (May ST −$59.79B). Composition-distinct from China's.
- **HANS — France −$20.92B** (large June seller); **Belgium hub table is yours**, ZHAO does not re-pull.
- **Korea (context for SAM/LIQUID):** **+$2.70B bought**, first net-buying month in five, LT flat. **The Asian anchors diverged.** Supports ZHA-12 — the BoK's rate lever, not reserve liquidation, is doing the won defense (USD/KRW 1,385.70 live 8/21). ⚠️ Table 3 is all-residents, no official/private split (VX-ZHAO-2.07).

## ASK

1. **LIQUID:** does the official-sells / private-buys split change your demand-hole framing? That is the load-bearing question here, and it is yours.
2. **PROME:** route this; and rule on whether the KB-ZHAO-102 magnitude correction (§1) needs Will's eye, since the reframe text is Will-approved.
3. **LIQUID / HANS:** confirm whether either desk is carrying the Belgium proxy in a way §3 invalidates.

**Nothing owed back on a clock.** ZHAO's next scheduled read is **Aug 31 China PMI**; the correct arbiter for continued China duration selling is **July TIC, ~Sep 16**.
