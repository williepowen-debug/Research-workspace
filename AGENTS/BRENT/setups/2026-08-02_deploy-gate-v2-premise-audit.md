# DEPLOY GATE v2 — PREMISE-CHECK AUDIT

**Run:** 2026-08-02 (Sun, pre-open) · **Requested by:** Will · **Verdict: ⛔ MY CONCERN IS REFUTED. THE GATE IS SOUND AND NO SPEC CHANGE IS WARRANTED.**

---

## 0. What I claimed, and why it was worth testing

I flagged to Will that gate v2 might have a structural defect: **the arm is LONG convexity, leg (a) waits for vol decompression, and what decompresses OVX is de-escalation** — so the gate could open *precisely into the tape that kills the thesis*, with no leg asking "is the premise still alive?"

I labelled it a shape, not a defect, and said it needed base-rating before it could bind. **That was the right call, because the base rate does not support it.**

## 1. The spec, verified against `TRADE.md` §DEPLOY GATE v2 (not from memory)

| Leg | Frozen test |
|---|---|
| **(a)** | OVX ≤ **−15.0%** from its running peak **since the arming date**, **close basis** (Will-ruled 7/31) |
| **(b)** | Net debit ≤ **33.0%** of spread width, **live chain at fill** |

Plus: **20-td expiry** · **frame-breaker carve-out** (confirmed destroyed capacity deploys on (b) alone) · **re-ratchet** (peak is a running max ⇒ fresh escalation *raises* the bar) · **Will's [Approve] at fire.**

**✅ My characterisation was accurate on the facts:** there is **no abort leg**. The re-ratchet handles a *worsening* crisis; nothing in the spec handles a *resolving* one.

## 2. Method

**Arming proxy:** Brent 1-day return ≥ +3% (a sharp crude up-move = the war-risk event class this arm arms on). **n=79 events over 1,045 sessions (2022-06 → 2026-07).** For each, I set peak = running max OVX since arming, walked forward 20 td, and fired on the first close with OVX ≤ 0.85 × running peak — the frozen rule, re-ratchet included.

**Comparator:** deploy immediately at arming+1, no gate. **The question is not "does the gate fire?" but "does gating BEAT not gating, for THIS structure?"**

## 3. Results

**▸ The gate is very fireable.** **81.9%** fire within 20 td (59/72), median **10 sessions** to fire. *(The old gate's alleged unfireability was already established as false; this confirms v2 did not inherit it.)*

**▸ The de-escalation tilt I suspected is REAL:**

- Crude at the fire session, vs its arming level: **median −1.85%**
- **62.7% of fires (37/59) occur with crude BELOW where it was when the arm armed**

**⇒ So the mechanism I described exists. It just isn't harmful — and that is the whole finding.**

**▸ THE PAYOFF TEST REFUTES THE CONCERN. A convex long needs the RIGHT TAIL, not the median** — so I tested `P(max Brent gain ≥ X within the structure's life)`, which is what gets a vertical paid:

| Horizon | Threshold | **GATED** | Immediate | **Gate edge** |
|---|---|---|---|---|
| 42d | +5% | 67.2% | 62.0% | **+5.3pp** |
| 42d | +10% | 43.1% | 45.1% | −2.0pp |
| 42d | **+15%** | **39.7%** | 29.6% | **+10.1pp** |
| 63d | +5% | 70.4% | 64.7% | **+5.7pp** |
| 63d | +10% | 53.7% | 51.5% | +2.2pp |
| 63d | **+15%** | **44.4%** | 35.3% | **+9.2pp** |

**▸ And it delivers its stated purpose:** OVX at arming **median 55.0** → at fire **median 47.8** (**−11.1%**); **83.1%** of fires enter at lower vol than the arming session.

**▸ Cost of waiting, stated honestly:** Brent's peak gain between arming and fire is **+3.81%** median while crude *at* the fire session is **−1.85%** ⇒ you give back ~**5.7%** of crude move by waiting. **You are paid for it in vol and in a fatter right tail.**

**▸ Robustness — the edge is not an artifact of my arming proxy:**

| Arming threshold | n | Fire rate | Gated | Immediate | Edge |
|---|---|---|---|---|---|
| ≥+2.0% | 155 | 76.2% | 36.9% | 30.0% | +6.9pp |
| ≥+2.5% | 113 | 81.1% | 41.6% | 33.0% | +8.6pp |
| ≥+3.0% | 79 | 81.9% | 44.4% | 35.3% | +9.2pp |
| ≥+4.0% | 40 | 94.3% | 45.2% | 38.2% | +6.9pp |
| ≥+5.0% | 19 | 100.0% | 46.2% | 28.6% | +17.6pp |

Positive at **every** threshold, and across decompression depths **−10% (+10.9pp) / −15% (+9.2pp) / −20% (+3.2pp)**. *(The −25% row shows +42pp on a 36% fire rate — n≈13, noise; I do not carry it.)*

## 4. ⛔ Verdict — and the counterfactual, which is the point

**MY CONCERN DOES NOT SURVIVE. The gate is sound, fireable, delivers cheaper vol, and measurably IMPROVES the right tail this structure depends on. No spec change is warranted and I am not proposing one.**

**★ Had Will ruled on my framing instead of asking for the test, the "fix" would have been to add a premise-abort leg — TIGHTENING a gate that is adding ~+9pp of right-tail edge, with 9 sessions left on the clock, on a hypothesis that fails its own base rate.** That is **the wrong repair to the wrong defect** — the identical error I made on LESSONS #21(a), when I told Will the old cooldown gate was "unfireable by construction" and it had been met on 50.4% of the prior year. **n=2 on this pattern now: an escalation is an assertion, and I keep sending them before base-rating them.**

## 5. ✅ What DOES survive — and it is not a spec defect

**The base rate validates the gate for DIPS. It is silent on TERMINAL RESOLUTION, because the sample contains none.**

Every pullback in 1,045 sessions is a **dip within a continuing regime**. **There is no instance of a closed chokepoint genuinely reopening** — the same **n=0** that already limits Stage-A ("zero genuine physical reopenings, real-vs-fake is UNCALIBRATED"). So the +9pp edge is evidence that *buying the dip inside a live crisis works*; it is **not** evidence about *deploying into a crisis that is actually ending*.

**The live instance points the same way and is worth stating precisely:** `TRADE.md:94` records that **7/28 would have satisfied leg (a)** (OVX 57.15 = −17.1%) — the deepest de-escalation day of the cycle, on the pause. **That pause was not terminal; it broke in 4 days.** So even the one near-fire on record is a *dip*, not a resolution — consistent with the base rate, not a counterexample to it.

**⇒ The correct control already exists and it is not a threshold: Will's [Approve] at fire.** The gate was never designed to adjudicate the premise; the human ruling is. **The only gap is INFORMATIONAL — nothing requires the fire packet to state the premise's condition.**

## 6. The one thing I am proposing (narrow, no spec change, no threshold)

**A disclosure requirement on the fire packet, not a new leg:**

> **If leg (a) fires while a de-escalation claim is live, the deploy packet must state, in figures and before the fill: (i) the current Stage-A leg-(i) status (is there an INSTRUMENT, or only guidance?), (ii) the latest Hormuz transit count against the 88/day baseline, and (iii) whether the OVX decompression came from a resolving crisis or an ordinary dip. Will approves or declines with that in front of them.**

This costs nothing, changes no frozen number, cannot loosen the gate, and closes the only gap the audit actually found. **Per #21(b) — a spec repair is not direction-neutral — I checked: this is direction-NEUTRAL because it adds information, not permission.**

## 7. 🔴 Live, and it is close

**OVX 63.04 (7/31 close) · line ≤58.62 · needs a further −7.01%.**

- P(single session OVX ≤ −7.01%): **5.9%** unconditional (62/1044)
- P(2-session cumulative): **14.2%** unconditional
- ⚠️ **Those are UNCONDITIONAL and therefore understate it badly. Conditional on a deal headline it is far higher: OVX fell −10.9% in ONE session on 7/27, on the last pause.**

**⇒ Leg (a) is plausibly one deal-headline session from firing, inside a 9-session window.** The disclosure in §6 should be in place before Monday's close, not after leg (a) fires.

## 8. Limitations, stated because they bound the verdict

1. **Arming proxy ≠ the real arming condition.** A generic +3% Brent day is not a Tier-2 confirmed physical re-closure. **n=79 proxies vs n=1 of the real thing.**
2. **I tested Brent spot moves, not USO option P&L.** "Max gain ≥15%" is a proxy for "the spread got paid," not the spread's actual return; real P&L also depends on strike placement, theta and the vol path.
3. **Not a clean causal test.** OVX-based entry timing and Brent forward returns share a common driver (crisis dynamics); this measures association.
4. **⚠️ The binding one: n=0 on terminal chokepoint reopening.** §5 rests on this and it is why the verdict is "no spec change," not "the gate is safe in all states."
5. Single data source (yfinance) for both series; the OVX close basis matches the Will-ruled convention.
