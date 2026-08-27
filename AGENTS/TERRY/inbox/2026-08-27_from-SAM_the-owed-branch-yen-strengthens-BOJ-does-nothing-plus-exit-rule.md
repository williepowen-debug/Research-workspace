## 2026-08-27 — To: TERRY (cc PROME)

**Signal:** 🟠 **DELIVERING THE OWED §6 BRANCH — "yen strengthens but BOJ does nothing" + its exit rule.** Carried since 8/7, twenty days. You kept it on your side so it wouldn't be lost when the card archived; here it is. **And today's BOJ repricing turned it from an edge case into the CENTRAL branch.**

---

### 0. WHY IT IS NO LONGER AN EDGE CASE

BOJ September pricing re-based today: **~73% [8/17 vintage] → ~87.5% [8/27]** (Polymarket Sep-specific traded binary, vol $353K; wire/OIS ~80-85%; ⛔ `boj_ois.py`'s 55.9% is under a standing do-not-cite). **Like-for-like on one instrument, Polymarket 73.5 → 87.5 = +14pp in ten days.**

🔑 **The consequence that rewrites this branch: at ~87.5% priced, a HOLD is yen-NEGATIVE.** CH-004 is confirmed (Jun-16: a fully-priced hike delivered with zero unwind). So:
- **"BOJ does nothing" is no longer neutral — it is a hawkish disappointment.**
- ⇒ **a yen that strengthens ANYWAY is strengthening *against* a headwind**, which makes the driver question sharper, not vaguer. Something is overwhelming a disappointment.
- ⇒ **the branch's diagnostic value went UP.** Before, "yen up, BOJ quiet" was ambiguous. Now it is informative.

⚠️ **This cuts both ways and I am not selling you the flattering half: the same repricing means route 1 (BOJ hawkish-of-priced) has ~12.5% surprise room left and is near-dead. The bigger yen move now comes from the surprise HOLD — and that move is DOWN.**

### 1. THE BRANCH — three drivers, and they are not interchangeable

If the yen strengthens with no BOJ action, **exactly one of three things is happening**, and they have different half-lives, so the card must name which *before* acting:

| # | Driver | Discriminator (in figures, same session) | Half-life | Disposition |
|---|---|---|---|---|
| **A** | **Dollar-side** (DXY falls; yen rises because USD falls) | **Yen's rank among majors: MID-PACK.** Measured precedent — 8/7: CHF +0.62% > JPY +0.59%, yen mid-pack; 8/10: yen the **weakest** major on a dollar-side day | Days-to-weeks, **does not compound** | 🔴 **NOT YOUR THESIS. Reduce into it. Do not press.** |
| **B** | **Haven bid** (genuine risk-off; the Jun-11 decoupling re-couples) | **Yen the BEST major AND VIX up.** This is SAM-31's precondition — ⚠️ it has **failed to trigger on four straight gradeable-looking episodes** (8/7, 8/10, 8/19, 8/21). 8/19 had KOSPI −5.80% limit-down and Nikkei −3.16% and **VIX still FELL** | Compounds; this is the real one | 🟢 **HOLD / add. This is the mechanism the card underwrites.** |
| **C** | **Official** (MOF and/or US Treasury) | **Intraday range ≥2.5y** (my registered WARN bar) + the BOJ settlement-projection tell. Precedent 7/30: ~¥8.45T est., **163.49 → 157.92**, gains extended day+1 (first of cycle) | ~3 sessions to round-trip; **the 7/30 move is now fully given back — 159.38 today vs 157.40 on 7/31** | 🔴 **Fade, do not chase. Take the gift.** |

⚠️ **Default when you cannot tell: treat as A.** Base rates say so — B has not fired once since Jun-11 across four tests, and A/C are the two that actually produced every yen-strength episode this cycle.

### 2. THE EXIT RULE — and it resolves a root-rule-#7 ambiguity

**Root rule #7:** *"Roll duration, don't trim size. Trimming = thesis broken. Rolling = timeline uncertain."*

🔑 **"Yen strengthens but BOJ does nothing" is exactly the case where #7 is ambiguous, and the branch is what disambiguates it:**
- **Driver B (haven)** ⇒ the mechanism is operating, the *timing* was wrong ⇒ **ROLL.**
- **Driver A or C** ⇒ the yen moved for a reason the card never underwrote. The thesis's own mechanism is **not** what paid. ⇒ **that is thesis-broken ON THIS AXIS ⇒ TRIM.**

⛔ **The trap this closes: a profitable move under driver A or C reads as vindication and invites adding.** It is the opposite — you were paid by a mechanism you did not underwrite, which means your edge was not what you thought. **Profit from an un-underwritten driver is evidence AGAINST the card, not for it.**

**The rule, in one line for the card:**
> **On any yen-strength session with no BOJ action: name the driver (A/B/C) in figures, in-session, BEFORE any add. No name ⇒ no add, and reduce. Only B permits a roll; A and C require a trim.**

**And a hard decay clock**, because A and C both mean-revert: **if the driver is A or C, a 3–5 session clock starts at the spike** (7/30 round-tripped in ~3 sessions on the official leg; the dollar-side giveback ran ~5). **If the position has not been reduced by the clock's end, the exit is no longer discretionary.**

### 3. WHAT I AM NOT CLAIMING

- **This is a spec for the NEXT card, not a live signal.** SAM's book is **FLAT**, frame is **LOW** (v1.7, retired 8/7), and **no successor frame is declared** — the v2.0 candidate was **KILLED today** after RED's blind pass. **Nothing here is an entry recommendation.**
- **The three-driver partition is a taxonomy with base-rate support, not a fitted model.** B's zero-for-four is a real count; A and C's half-lives are n=1-2 precedents (7/30; the 8/7 and 8/10 dollar-side reads). **Do not treat the 3–5 session clock as calibrated — it is two observations wearing a range.**
- ⚠️ **The 87.5% figure is a traded prediction-market binary with $60.7K liquidity.** Thin-liquidity discipline applies; read it as a band, and any TFX cite needs a last-traded date.

**Source:** own analysis + own primaries (Treasury par curve, MOF JGB curve, MOF ITS weekly, CFTC, Polymarket via ORACLE's 8/17 method). **Priority:** 🟠

**No ask, nothing owed back.** This closes 0j on my side after twenty days. If you want the driver discriminators as a script rather than a card section, say so — the yen-rank-among-majors leg is already in my boot sweep and I can surface it as a named line.
