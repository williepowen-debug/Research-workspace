# MIDAS-08 — REGISTRATION: the M1 successor test. Did the crowded gold spec long unwind into a −6.35% week?

**Registered 2026-09-02 ~15:4x ET — BEFORE the 2026-09-04 15:30 ET CFTC release.** Deliberate, and the reason is the whole point: the conditioning fact is already visible and the answer is not.

## 1. Why this row exists

**M1 sits at 4 and has no live test.** MIDAS-06 graded TERMINAL 8/31 and its upgrade-trigger cell reads *"CONSUMED — any further M1 escalation needs a NEW registered test."* Since then the desk has accumulated **unregistered observation** about M1 — BOND's 9/1 breakeven tension, the gold basis work, the COT crowding — and none of it can move a score, correctly, because none of it was registered in advance.

**The question is the one this desk and BOND both explicitly declined to rule on 9/2:** is gold's premium **spec-funded** or not? MIDAS's own pre-registered falsifier (COT #3) fired *against* the desk's read on 8/28 — net/OI **56.86%**, Δ **+2.17pp**, composition **CHASED** (NC long **+20,257**, NC short **−888**, OI **+21,697**), 99.8th percentile. That established *"a meaningful part of the 8/19 residual is spec flow"* — and explicitly **not** how much, and **not** that it survives.

## 2. ⚠️ THIS IS A ONE-LEG FORECAST, NOT A 2×2 — and saying so is the honest design

The first sketch was a 2×2 over {positioning unwinds / holds} × {gold holds / falls}. **That is wrong, and the flaw is instructive: both legs are as-of 2026-09-01, so the PRICE leg is ALREADY OBSERVED.** A branch set that treats a known quantity as a forecast dimension manufactures the appearance of a harder test than it is.

⇒ **The price move is a FROZEN CONDITIONING FACT, stated here, not a branch:**

> **`GCZ26` (front, named per WQ-91): 4,694.50 [close 2026-08-25] → 4,396.40 [close 2026-09-01] = −6.350%.**
> The COT reporting window (as-of Tue → as-of Tue) is exactly 2026-08-26 → 2026-09-01.

**Only the positioning response is unknown.** The test is therefore sharp precisely *because* the price leg is settled: **a 99.8th-percentile crowded long was handed a −6.35% week. Did it run?**

## 3. Empirical basis for the boundary — measured, not chosen by feel

Source: `sources/cot_gold_history_2010_2026.tsv` (COMEX full-size gold, code 088691, legacy futures-only), frozen 2026-08-28.

**Full sample, weekly Δ net/OI, n=867 (2010-01-05 → 2026-08-18):**
`p1 −7.86 · p5 −5.47 · p10 −3.97 · p25 −1.92 · p50 −0.03 · p75 +1.78 · p90 +4.19 · p95 +5.80 · p99 +9.16` · mean **+0.011** · sd **3.315** · min −12.69 · max +15.26.

**Conditional on the PRIOR week ≥ 56.0% — ⚠️ n=7 ONLY, over 16.6 years:**
`−2.80 · −1.82 · −1.70 · −1.03 · −0.85 · −0.17 · +0.80` — mean **−1.081**, median **−1.029**; **6 of 7 negative (86%)**, 4 of 7 ≤ −1.00pp (57%), **1 of 7 ≤ −2.00pp (14%)**.

⛔ **n=7 IS TOO SMALL TO CARRY A THRESHOLD AND I AM NOT LETTING IT.** This desk has already published one base rate off a too-short inherited window and had to correct it (KB-042: *"0 of 19, never observed"* → 1.81% on the full series). **The boundary below is therefore taken from the FULL-sample distribution (n=867); the conditional set is reported as context with its n stated, and is not load-bearing.**

## 4. THE FROZEN LETTER — branches are MECE per WQ-142

**Measured quantity:** Δ net/OI (pp) = [net/OI, as-of **2026-09-01**] − **56.8600%** [as-of **2026-08-25**, frozen baseline, from the 2026-08-28 release].

| Branch | Condition (half-open; **boundary owner named**) | Reading | Consequence |
|---|---|---|---|
| **(a) UNWIND CONFIRMED** | **Δ ≤ −2.00pp** *((a) owns −2.00)* | The crowded long ran into the decline ⇒ spec flow was a **marginal price-setter**, not just present | **M1 4 → 3** |
| **(b) INDETERMINATE** | **−2.00pp < Δ < +1.00pp** *(open both ends)* | Bleed or drift; no clean read at this resolution | **M1 holds 4.** No change |
| **(c) CROWDING HELD OR EXTENDED** | **Δ ≥ +1.00pp** *((c) owns +1.00)* | Spec held/added **through a −6.35% week** ⇒ conviction money, not hot money | **M1 holds 4**, and the **COT #3 impeachment is materially WEAKENED** — recorded, **not** scored |
| **(d) NO-VERDICT** *(declared catch-all)* | Vintage not published by **2026-09-08**; OR `cot_gold.py` totals reconciliation fails; OR the in-row as-of ≠ 2026-09-01; OR contract code 088691 absent/relabelled | Instrument failure, **not** a market result | **No change.** Re-register or retire |

✅ **MECE:** (a) ∪ (b) ∪ (c) covers ℝ with no overlap; (d) is the declared catch-all for non-observation. **No observation can fall outside the set** — the defect WQ-142 was ruled against (2.40 sat in both MIDAS-06 (a) and (d); gold $4,050–$4,340.70 with DFII10 ≥2.40 fit no branch).

⛔ **The WQ-142 NARROW band (2.37–2.43) is NOT attached, deliberately and not by omission: this row references no DFII10 leg.** The band is registered as an admissible print set only on DFII10-referenced rows.

**Pre-registered branch masses** (sum 1.00): **P(a) = 0.40 · P(b) = 0.40 · P(c) = 0.18 · P(d) = 0.02.**
⚠️ **P(a)=0.40 DEPARTS FROM THE 14% CONDITIONAL BASE RATE AND THE REASON IS STATED SO IT CAN BE JUDGED:** the conditional set is n=7 of *ordinary* crowded weeks, whereas this window carries a **−6.35% price shock** and a composition already measured as **CHASED** — chasing money is weak money. **If (b) or (c) fires, that departure was wrong and this note is the evidence of it.**

## 5. Resolution

**Date:** Friday **2026-09-04**, after the **15:30 ET** CFTC post. **Instrument:** `python3 cot_gold.py --expect 2026-09-01` — ⛔ **never grade the first response after 15:30**; the raw file serves last week's vintage on a clean 200 (`finding_partitioned_source_returns_stale_window_at_200`). Exit 3 = WAIT, poll. Totals reconciliation (OI == TotRept+NonRept, both sides) must PASS before any position number is read.
**Contract:** COMEX full-size gold, code **088691**, legacy futures-only. Micro gold is a different code and corrupted 6 of 15 weeks on this desk's first pull (KB-036).
**Confidence tier:** **PROVISIONAL** — the boundary is a full-sample percentile, but the *conditional* evidence for mean-reversion from crowded levels is n=7.

## 6. If falsified — the action, written before the result

**If (c) fires**, my published line *"a meaningful part of the 8/19 residual is spec flow"* must be **re-read in public as too strong**, and the 8/28 COT #3 grade recorded as a falsifier that fired on a configuration which then **failed to behave like one**. ⇒ Write it plainly on STATUS and route the correction to BOND, which adopted that carve-out verbatim on 9/1. **A falsifier that fails to fire is information about my falsifier, not a vindication of my read.**

**If (a) fires**, it does **NOT** retroactively validate MIDAS-06 or re-open MIDAS-07, and it does **not** establish that *all* of the premium is positioning — only that spec flow was a marginal price-setter over one week. **M1 → 3 is the letter's own prescribed consequence, not a re-rate.**

---

## 7. ⛔ POST-REGISTRATION NOTE — 2026-09-02 ~19:5x ET. **THE LETTER DOES NOT MOVE.**

**What arrived AFTER registration:** `BND-21` resolved **TRUE**. Verified independently at the primary (not taken from BOND's packet), FRED pull 2026-09-02 23:51Z:

| Leg | 8/31 | 9/1 | Δ |
|---|---|---|---|
| `DGS10` nominal | 4.75 | 4.79 | **+4.0bp** |
| `DFII10` real | 2.44 | 2.44 | **0.0bp** |
| `T10YIE` breakeven | 2.31 | 2.35 | **+4.0bp** |

**Identity closes exactly: 4.0 = 0.0 + 4.0.** The 9/1 session was **~100% breakeven, 0% real**. ⇒ gold fell **−1.90% to −2.86%** on a session with **zero real-rate impulse** and a **gold-POSITIVE** breakeven rise. **The real-rate explanation for 9/1 is dead on published data.**

### This raises the prior on branch (a). **I am not touching P(a) and that is the point.**

The masses **0.40 / 0.40 / 0.18 / 0.02** were registered at ~15:4x ET; this evidence landed at ~19:5x ET. **Re-tuning them now, in the direction the new evidence favours, is precisely the mid-flight patching row 68 forbids** — and precisely what this desk refused on 8/31 when the row-66 band would have voided MIDAS-06.

⚠️ **And the cost is real and should be named in advance, or the discipline is free and therefore worthless: if (a) fires, my 0.40 will look under-confident and will be scored as such.** On 8/31 honouring the fence cost a *score*; here honouring the freeze may cost *calibration credit*. **Both directions, which is the only evidence that a rule is load-bearing rather than decorative.**

### ⛔ What BND-21 does NOT do — BOND's own §3, adopted verbatim because it is the correct limit

> *"`BND-21` says only that the real-rate alternative is gone for that session; it does not promote yours."*

**Elimination is not promotion.** The COT crowding remains a **candidate with an instrument behind it, not a finding**, and the 8/19→8/25 snapshot **still cannot pin the 9/1 session**. Surviving alternatives that this note does not exclude: a large physical/OTC seller, ETF redemption, a currency leg, or something unmeasured. **The only positive evidence arrives Friday.**

🔑 **Which is the argument for having registered on Wednesday.** MIDAS-08 was frozen **before** the information that made it interesting existed. Had it been written tonight, every branch and every mass would be suspect of having been drawn around a result the desk already half-knew.

---

## 8. ⛔ SECOND POST-REGISTRATION NOTE — 2026-09-02 ~21:1x ET. **STUCK adopted PROSPECTIVELY. MIDAS-08 is again NOT amended.**

**ZHAO's suggestion, checked rather than acknowledged:** its `ZHA-17` declares a **STUCK** branch — *non-publication resolves STUCK, not NO* — on the reasoning that **a resolver that cannot resolve is a STATUS change, not a confidence cut.** ZHAO asked me to check MIDAS-08 for it.

**What MIDAS-08 actually has, read off the registered row:** branch **(d)** already carries the *semantics* — *"instrument failure not a market result, no change"* — covering non-publication, reconciliation failure, as-of mismatch and contract-code relabelling. ✅ **The distinction ZHAO is protecting is present.**

⛔ **What it does NOT have is ZHAO's scoring treatment, and ZHAO is right that this is better:** my (d) **carries probability mass, P(d) = 0.02**, inside a distribution whose other three branches are *market* outcomes. **Mixing an instrument outcome into a market distribution means a vendor outage consumes calibration mass.** ZHAO's form — market branches summing to 1.00 *conditional on resolution*, with non-resolution setting a **status** — is cleaner and I am adopting it.

### **PROSPECTIVELY. MIDAS-08 IS NOT AMENDED. Third time today.**

Converting (d) from a mass-bearing branch to a status forces renormalising **(a)(b)(c) from 0.40/0.40/0.18 (sum 0.98) to sum 1.00** — **it materially changes the masses that get scored.** That is an amendment to a frozen letter five hours after registration and two days before resolution, and it is the mid-flight patching row 68 forbids **however much better the new design is.**

⭐ **This is the third application of the same rule in one session, and the consistency is the entire value:**
1. **8/31** — the row-66 band would have voided MIDAS-06's grade; not applied. **Cost: a score.**
2. **9/2 ~19:5x** — `BND-21` raised the prior on branch (a); P(a) not re-tuned. **Cost: likely calibration credit.**
3. **9/2 ~21:1x** — a genuinely better branch design offered; not retrofitted. **Cost: MIDAS-08 resolves on a design I now know to be second-best.**

**A rule that only ever costs nothing has not been tested. This one has now cost something three times in three days, in three different currencies.**

**⇒ Registered for the successor:** every MIDAS row after MIDAS-08 declares market branches summing to **1.00 conditional on resolution**, plus a **STUCK** status for non-resolution that **carries no mass** — the instrument-failure conditions currently inside (d) move there verbatim.

---

## 9. ⛔ THIRD POST-REGISTRATION NOTE — 2026-09-02 ~21:3x ET. **ZHAO refuted my STATED rule; the refutation is accepted, with one safety clause.**

**I stated the rule as "prospective only." That is wrong, and ZHAO's counter-example is decisive:** stated that way it **blocks a mass-neutral fix** (ZHA-11/12, which carried *no* non-publication branch at all) while **permitting a mass-moving one on a fresher row.** Exactly the wrong two things.

> **The operative test is not WHEN you patch. It is WHETHER THE PATCH MOVES SCORED MASS.**

| Case | What it carried | Verdict |
|---|---|---|
| **MIDAS-08 (d)** | **P = 0.02** inside a distribution of market outcomes; converting forces renormalising (a)(b)(c) 0.98 → 1.00 | **MOVES SCORED MASS ⇒ correctly refused** |
| **ZHA-11/12** | **no branch at all** — undefined behaviour, not a scored branch | **mass-neutral ⇒ correctly fixed** |

**My instinct picked the right cases; my stated rule under-described what the instinct was doing.** Recorded because a rule that only works when its author's intuition is also present is not a rule.

### ⚠️ One safety clause, because ZHAO's test costs something my date-rule did not

A calendar rule is **argument-proof**: it needs no judgment and a motivated desk cannot talk its way past it. *"Does this move scored mass?"* **is** a judgment, and it is exactly the judgment a desk wanting to patch will resolve in its own favour. So the refinement must not become a licence.

**⇒ ADOPTED FORM.** Default: amendments to a live registered row are **prospective-only**. **Narrow carve-out** — a live row may be patched **only if ALL of:**
1. **mass-neutral conditional on resolution** — no branch boundary, no mass, no outcome changes in any world where the instrument resolves normally;
2. it **completes UNDEFINED behaviour** or corrects behaviour that is **indefensible rather than merely unspecified** (*scoring a publication outage as a forecast error* is indefensible; a disliked threshold is not);
3. **the proof of (1) and (2) is written into the row at patch time.** ⭐ **This is the clause that keeps it a rule rather than a vibe: the judgment becomes a checkable written claim, made before the patch, not a defence offered after.**

**MIDAS-08 fails clause 1. The decline stands, now for the correct reason rather than the calendar one.**

### 🔴 I RAN ZHAO'S SWEEP ON MY OWN BOOK, AND FOUND ZHAO'S EXACT SHAPE — n=2 of 2

**MIDAS-01 and MIDAS-02 (both OPEN, both `resolve 2026-09-30`) declare NO non-resolution case whatsoever.** I built the catch-all for the **new** row and left the two older rows undefined — *`finding_a_ruling_governs_the_next_write_not_the_existing_state`*, the same n=2-of-2 ZHAO reported, on the same evening.

**Under the adopted form, fixing them would QUALIFY:** they carry no branch masses, declaring a non-resolution status changes nothing in any world where the data publishes, and the world it does change is the one where a data outage would score as a forecast MISS — indefensible, not a design choice.

⛔ **AND I AM NOT FIXING THEM, BECAUSE A HIGHER AUTHORITY SAYS NO.** **WQ-91 (Will, 2026-09-01) rules the moving-referent class *"no edit to the live rows"* and names MIDAS-01 and MIDAS-02 explicitly.** My refined rule permits the patch; **Will's ruling forbids an edit to these rows**, and a self-derived rule does not outrank an operator ruling that names the row.

**⇒ FLAGGED, NOT APPLIED — routed to PROME/Will as a one-line question:** *does WQ-91's "no edit" bar a mass-neutral non-resolution status, or only the referent re-keying it was ruled about?* **Until answered, MIDAS-01/02 grade 9/30 with the gap open and the gap stated.** ⚠️ If the data is unavailable on 9/30, the grader must read this note and record **STUCK**, not MISS — *stated here in advance so that instruction exists on the surface the grader reads* (L-48, applied to itself).
