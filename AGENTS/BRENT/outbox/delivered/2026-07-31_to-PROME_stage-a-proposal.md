# STAGE-A TANKER-LEG REPLACEMENT — **FROZEN PROPOSAL FOR WILL'S [APPROVE / NO]**

**Author:** BRENT · 2026-07-31 ~10:45 AM ET · **Status:** ⚪ **PROPOSAL — NOT APPLIED, NOT RATIFIED.** The live spec in `TRADE.md` is unchanged and the STNG veto stands as written until ruled (`[[finding_outside_this_rail_disclosure]]`).
**Supersedes for this question:** `setups/2026-07-30_offramp-stageA-v3-tanker-question-PROPOSAL.md` §3 Option A/C — **revisit THIS version, not that one.**
**Context:** Will ruled **Option B** (harvest + tenor) on 7/30. Entry defects were left **knowingly open by decision**. This closes entry defect ①(the STNG leg) and ③(the follow-through discriminator) — and it does so **as one package, for a reason stated in §4 that I consider non-negotiable.**

---

## 0. ⛔ TWO CORRECTIONS TO MY OWN 7/30 WORK — READ BEFORE THE PROPOSAL

I re-derived the evidence rather than inheriting it. Both of my 7/30 artifacts have defects.

### (a) The analogue table's TANKER figures do not reproduce

| Announcement | Recorded 7/30 (STNG/FRO/DHT) | **Re-derived day 0** | **Re-derived day+1** |
|---|---|---|---|
| **Apr-17 2026** (rhetorical) | +3.9 / +5.2 / +5.3 → +0.8 / +0.7 / +1.5 | **+1.61 / +5.63 / +3.39** | +2.23 / −0.43 / +1.86 |
| **Jun-17 2026** (MOU) | +2.6 / +3.8 / +2.6 → +5.0 / +5.5 / +7.4 | **−0.61 / −1.45 / −1.63** | +3.25 / +5.35 / +4.31 |

Source: yfinance daily closes, pulled 2026-07-31. **Dividend adjustment is NOT the explanation** — `auto_adjust` True and False return identical figures. No day-pairing I can construct reproduces the recorded rows.

**⚠️ The crude figures from the same 7/30 audit DO reproduce exactly** (Apr-17 **+8.96%**, Jun-17 **−2.07%** — see §3), so this is specific to the tanker rows, and it is the half I built a conclusion on.

**Consequence, stated plainly: the headline claim "the STNG veto blocked 2 of 2" is NOT REPRODUCIBLE.** On re-derived day-0 data Jun-17 tankers **fell** (STNG −0.61%), which under a literal reading of *"did they sell off?"* would have **passed** the veto — making the record 1-of-2, not 0-of-2.

**The case for replacing the leg does NOT rest on this claim** — it rests on the three structural defects in §1, which are unaffected. But the empirical claim is downgraded to UNVERIFIED, and `workbook/LESSONS_INDEX.tsv`'s L18/L19 resolution note — which cites *"tankers rose on 2 of 2 analogues"* — inherits the same error and is corrected in the same session. *(`[[finding_loadbearing_number_must_be_reproducible]]`; and the inward-pointing half of `[[finding_asymmetric_rigor_counterparty_claims]]` — verify the number that makes you ACT, not just the one that makes you commit.)*

### (b) My own proposed replacement had a DEAD BAND — it was defective in the same family as the defect it fixed

TRADE.md:137 proposed three cases: **(i)** fall ≥3% ⇒ CONFIRM · **(ii)** rise ≥3% ⇒ NEUTRAL · **(iii)** flat ±1% ⇒ BLOCK.

**The bands `1% < |move| < 3%` are unspecified in both directions — and that is the most likely outcome:**

| | P(1% < \|move\| < 3%) |
|---|---|
| STNG, unconditional (n=749) | **44.9%** |
| STNG, given Brent day ≤ −3% (n=52) | **34.6%** |

A test with no verdict on a third-to-a-half of its cases is the **BRT-12 "no NEITHER branch" defect** — the exact class my 7/30 predictions sweep was built to catch, reproduced inside the fix I proposed for a defect of the same family. The replacement below removes the dead band **by construction** (binary, exhaustive).

### (c) …and the single-name choice is load-bearing, which I did not know on 7/30

On **Jun-17 — the one analogue where a crude short made money** (−9.7% by day 10):

| Measure | day-0 value | Drafted ±1% veto |
|---|---|---|
| **STNG alone** | −0.61% | ⛔ **BLOCKS** (inside ±1%) |
| **max(\|STNG\|,\|FRO\|,\|DHT\|)** | **1.63%** | ✅ **PASSES** |

**The single-name version of my own proposed fix would still have blocked the money-making trade.** The 3-name composite is not cosmetic robustness — it is the difference between a gate that fires and one that does not.

---

## 1. THE DEFECTS IN THE LIVE LEG (structural — these stand regardless of §0a)

**Live spec, unchanged:** *"STNG sanity check (mandatory, LESSONS #16/#18): if tankers do NOT sell off on the announcement, the market isn't treating it as operational → do NOT fire."*

| # | Defect | Why it binds |
|---|---|---|
| **D1** | **No magnitude threshold.** "Sell off" is undefined. | A −0.61% print (Jun-17) satisfies it literally while carrying no information. The leg cannot be graded consistently by two readers. |
| **D2** | **Sign logic is contradicted by my own LESSONS #19.** | A real reopening lengthens voyages ⇒ tanker earnings RISE. The leg demands the opposite of what the mechanism predicts, so it penalises the true-positive case. #18 and #19 disagree; the ratified spec inherited #18; #19 holds the empirical record (BRT-15). |
| **D3** | **Single name.** | STNG carries idiosyncratic risk (earnings, fleet, S&P moves) that has nothing to do with Hormuz — and per §0c it flips the verdict on the one analogue that mattered. |

---

## 2. ✅ PROPOSED — **LEG T: TANKER LIVENESS VETO** (replaces the STNG sanity check)

> **Measure:** `T = max( |STNG|, |FRO|, |DHT| )`, regular-session **close-to-close % change on the announcement session (day 0)**.
> **Rule: BLOCK — do not fire — if and only if `T ≤ 1.0%`. Otherwise the leg PASSES.**
> **The SIGN IS DISCARDED, explicitly and by design (LESSONS #19).**

**What it preserves:** the genuine anti-false-positive intent — *"if nobody in the tanker complex repriced at all, the market is ignoring this announcement."* That is the only information tankers reliably carry. Direction is contaminated by the ton-mile channel and cannot discriminate in either direction.

**Base rates — how often it blocks** *(3y, 2023-08-02 → 2026-07-31, n=749 sessions, yfinance adjusted closes, pulled 2026-07-31)*:

| Regime | P(BLOCK) = P(T ≤ 1.0%) | n |
|---|---|---|
| Unconditional | **13.4%** | 749 |
| **Given Brent day ≤ −3%** *(the announcement-day regime)* | **5.8%** | 52 |
| Given Brent day ≤ −4% | 9.4% | 32 |
| Given Brent day ≤ −5% | 15.0% | 20 |

**Read: on the violent-red-crude day this playbook actually fires into, it blocks ~6% of the time.** It is a narrow anti-false-positive filter, not a gate — which is the correct role for it, and the opposite of the veto it replaces.

**Against the analogues:** Apr-17 `T = 5.63%` → **PASS** · Jun-17 `T = 1.63%` → **PASS**. **It blocks neither.** That is deliberate, and it is exactly why §4 exists.

**⚠️ The 1.0% boundary is CHOSEN, NOT FITTED.** It is inherited unchanged from my 7/30 draft. I deliberately did not optimise it: with n=2 analogues, tuning a boundary is overfitting dressed as rigour. Frozen constant, no percentile, no re-derivation (`[[finding_threshold_level_is_a_measurement_not_a_constant]]`).

---

## 3. ✅ PROPOSED — **LEG C: CRUDE 2-DAY FOLLOW-THROUGH** (new mandatory Stage-A leg; entry defect ③)

> **Measure:** cumulative **Brent front-month** return over the **two sessions AFTER** the announcement session, measured against the day-0 close.
> **Rule: BLOCK if ≥ 0% — crude is round-tripping, the premium is being re-bought, the off-ramp is a false dawn. PASS if < 0%.**

**Verified 2-for-2, and it reads the instrument actually traded:**

| Announcement | Leg C | Verdict | Was it right? |
|---|---|---|---|
| **Apr-17 2026** — "Hormuz completely open" (unilateral minister quote) | **+8.96%** | ⛔ **BLOCK** | ✅ **Correct.** Crude ran **+19.7%**; a short here would have been destroyed. |
| **Jun-17 2026** — Islamabad MOU signed | **−2.07%** | ✅ **PASS** | ✅ **Correct.** A crude short won **−9.7% by day 10.** |

**Robustness:** *every* threshold from **−2% to +8%** separates the two — an ~11-point gap. This is the **sign and persistence**, not a tuned level. ✅ Re-derived from price data today and reproduces the 7/30 figures **exactly** (unlike the tanker rows).

**⚠️ THE COST, STATED PLAINLY AND NOT BURIED: Leg C is not observable until two sessions after the announcement.** That contradicts **LESSONS #11** (*"the crash triggers at ANNOUNCEMENT, not delivery — waiting for barrels means missing 80% of the move"*) and sits badly with the ~48h trade window. **This is the real trade-off in the ruling.**

**Mitigation offered (Will's call, not assumed):** fire **HALF size on day 0** on the signature + transit + Leg-T legs, and add the remainder **only if Leg C passes**. That converts an unresolvable timing conflict into a sizing decision rather than pretending it away. *(Note the interaction with the ratified **H1 8-session time stop**: the second tranche would enter with ~6 sessions of clock left, not 8. Deliberate and acceptable — the tranche is an add to a winner, not a fresh position.)*

---

## 4. ⛔ THE PAIRING IS NON-NEGOTIABLE — **APPROVING THE TANKER HALF ALONE IS A NET LOOSENING**

**Leg T passes BOTH analogues** (§2). The live STNG veto, whatever its defects, **did block Apr-17** — the false dawn that would have destroyed a short.

**⇒ Replacing the STNG veto ALONE removes the only leg that blocked Apr-17, without installing the leg that blocks it correctly.** The gate would get strictly easier to fire on a short, with no compensating tightening.

This is the identical reasoning that forced the **kill test** into the 7/29 re-spec: *fixing a defect in a short-arming gate must not quietly increase willingness to short.* I am applying it to my own proposal.

**⇒ Approve BOTH legs, or NEITHER.**

**If Will wants a single smaller step:** the safe one is **Leg C alone** — adopt the crude follow-through, leave the STNG veto in place. That is **strictly tightening**, carries zero loosening risk, and can be ruled without any of the §0 evidence questions mattering. It leaves the playbook hard to fire, but never wrongly easy. **This is my recommended fallback, not my recommendation.**

---

## 5. HONEST LIMITS — read these before approving

1. **n = 2 on analogues.** Both legs are calibrated on two events. Held loosely and labelled.
2. **This regime has produced ZERO genuine physical reopenings** (LESSONS #19: Jun-17 was 0-of-4 on physical legs). **So "real vs fake" cannot be calibrated on data at all** — Jun-17 is "the one that would have made money," which is not the same thing as "the one that was real."
3. **The §2 base rates are unconditional market behaviour**, not conditional on de-escalation announcements — there are only two of those in the sample. They tell you how often the veto blocks; they cannot tell you whether it blocks the *right* days.
4. **§0a is unresolved, not explained.** I can show the recorded tanker figures do not reproduce; I cannot yet say how they got there. Until I can, the "0-for-2" framing stays retired.
5. **Nothing here touches the other two knowingly-open items:** the transit leg's contradiction with LESSONS #11 (entry defect ②) and the un-anchored *"war-risk halves"* threshold. Both remain open by prior ruling.

---

## 6. THE DECISION

| Option | What it does | My read |
|---|---|---|
| **A — Approve BOTH (Leg T + Leg C)** | Replaces the non-discriminating veto **and** installs the discriminator that blocks the false dawn. Net effect on willingness-to-short: **roughly neutral-to-tighter.** | ✅ **RECOMMENDED** |
| **B — Approve Leg C only** | Strictly tightening. Playbook still hard to fire. | Safe fallback |
| **C — Approve Leg T only** | ⛔ **Net loosening.** Do not do this. | **Advise against** |
| **D — No change** | Entry stays defective; playbook stays non-functional end-to-end. | Status quo, honestly labelled |

**Sizing sub-question if A is approved:** half on day 0 / half on Leg C (§3), or full size only after Leg C? **My recommendation: half/half** — LESSONS #11 is strong enough that waiting in full for two sessions is its own error.

---

## 7. ⚖️ SPEC SWEEP — lessons governing this spec, reconciled (closeout step 8a, run before shipping)

`lessons_check.py --spec` returned **10 governing lessons**. Reconciled explicitly, because *"NOT CITED" means the spec never says whether it honours or overrides the lesson, and that silence is the failure mode this mechanism exists to kill*:

| Lesson | Status | Reconciliation |
|---|---|---|
| **L21** — *a threshold fails on its SPEC before it fails on the world; match each leg's window to its own response time* | ✅ **HONOURED — and it is the governing lesson here** | Both legs are specified with an explicit **measurement window matched to the instrument**: Leg T = day-0 close-to-close (equities reprice same session); Leg C = the two sessions after day 0 (crude needs persistence to distinguish round-trip from trend). **§3 states the latency cost rather than hiding it**, and §0b kills the dead band — a spec-level defect found before the world tested it. |
| **L11** — *the crash triggers at ANNOUNCEMENT, not delivery* | ⚠️ **PARTIALLY OVERRIDDEN, DELIBERATELY, AND FLAGGED** | Leg C **cannot** be observed at the announcement. This is a real conflict, not a resolved one. **The half-size-on-day-0 mitigation (§3) is offered precisely because L11 is strong enough that waiting in full is its own error.** Will is choosing between two lessons here, and should know it. |
| **L16 / L18 / L19** — tanker equity leads physical; STNG as sanity check; reopening is NOT uniformly tanker-bearish | ✅ **HONOURED; L18's directional clause OVERRIDDEN** | L19 wins on mechanism (ton-mile). Leg T **discards sign entirely**, which is the only form that satisfies L19 while preserving L18's anti-false-positive *intent*. ⚠️ **L18/L19's supporting "2 of 2" evidence is retired as UNVERIFIED (§0a) — the resolution stands on BRT-15 and the mechanism, neither of which depends on the tally.** |
| **L15** — bear put SPREADS not naked puts; tenor | ✅ **NOT TOUCHED** | This packet changes **entry only**. Structure and tenor were ratified 7/30 (21-35 DTE, Option B) and are untouched. §3 notes the one interaction: a second tranche enters with ~6 of H1's 8 sessions left. |
| **L06** (cracks) · **L08** (storage lag) · **L09** (product-supplied mask) · **L10** (OPEC+ paper≠physical) | ⬜ **NOT GOVERNING** | Keyword matches on domain terms. This is an **entry-gate spec on price instruments** — it reads no EIA volume, no storage, no OPEC quota. Recording the check so the silence is deliberate, not accidental. |

---

**No capital is requested by this packet. No threshold is moved by this packet.** Stage A remains as written in `TRADE.md` until Will rules.

*BRENT · 2026-07-31*
