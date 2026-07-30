# LESSONS #21(a) — COOLDOWN-GATE RE-SPEC · **PRE-REGISTERED PROPOSAL FOR WILL'S [APPROVE / NO]**

**Author:** BRENT · **Date:** 2026-07-30 Thu ~2:40 PM ET · **Status:** ✅ **RULED 2026-07-30 — WILL APPROVED OPTION A** (sequenced gate, −15% decompression, ≤33%-of-width debit cap, 20-td expiry, frame-breaker carve-out). **Implemented same session** in `TRADE.md` §DEPLOY GATE v2 (canonical) and swept across STATUS / NEXUS_BRIEF / THESIS / LESSONS. **Live at ratification:** 10 of 20 td used, arm expires ~2026-08-13; post-arm OVX peak 68.97; OVX 63.46 = −8.0%; **leg (a) NOT MET (needs ≤58.62).** ⚠️ **Applied PROSPECTIVELY — 7/28 would have fired leg (a) but predates the ruling; no retroactive fire claimed.**
**Governs:** the **convex MAIN arm** deploy gate (`TRADE.md` § ACTIVE TRADE PLAN — v5.0 CONVEX ARM). **Does NOT touch** the off-ramp playbook (#21(b), ratified 7/29) or the filled Branch-2 tail-rider.
**All numbers below are FROZEN CONSTANTS, never rolling percentiles** — per #21(a) itself.

---

## 0. ⛔ FIRST: THE CLAIM I ESCALATED TO YOU WAS FALSE. RETRACTING IT BEFORE PROPOSING ANYTHING.

I told you the gate *"may be unfireable by construction — oil vol does not return to the 40s while the strait is shut, so the main arm's gate may never release capital while the thesis is alive."* I called it **"a dead switch."**

**I tested it today instead of asserting it again. It is not true.**

| Test | Result |
|---|---|
| Gate `{ratio <2.89 AND OVX <44.2}` met, last 1 year | **50.4% of sessions** (127 of 252) |
| Gate met, last 3 years | **74.5%** |
| **Last session the FULL gate was open** | **2026-07-06 — 18 sessions ago**, mid-crisis |
| Distinct open-windows in 3y | 23 · median 3 sessions · 9 lasted ≥5 sessions |

**The gate fires constantly. I had it exactly backwards, and I escalated it to you as a dead switch.** Had you ruled on my framing, the fix would have been *"lower the OVX number"* — which would have been the wrong repair to the wrong defect, and would have loosened a capital gate for no reason. **The real defect is different, and worse.**

---

## 1. THE ACTUAL DEFECT — the gate and the arm's own trigger are **MUTUALLY EXCLUSIVE BY CONSTRUCTION**

The arm **arms on escalation**. The cooldown gate **opens on calm**. Requiring both *simultaneously* requires an escalation event during a vol lull.

| Over 753 sessions (3y) | Gate open |
|---|---|
| Days in an **escalation regime** (Brent +15% over 20d) — 38 days | **0 of 38 = 0.0%** |
| All other days — 715 days | **78.5%** |

**Zero. Not "rare" — zero.** `corr(OVX, 20-day crude move) = +0.483`: the same event that arms the trade is the event that shuts the gate.

**The July window shows it in miniature, and the timing is almost comic:**

| Date | Brent | OVX | Vol gate |
|---|---|---|---|
| 6/30 – 7/06 | $71.6 – $73.2 | 40.3 – 43.2 | ✅ **OPEN** |
| 7/07 | $74.16 | 47.59 | ❌ shut |
| 7/11-12 | — | — | **← FORMAL HORMUZ CLOSURE** |
| 7/16 (arm CONFIRMED) | $84.23 | 55.91 | ❌ shut |
| 7/23 (Brent tops $100) | $100.69 | 68.97 | ❌ shut |

**The gate slammed shut three sessions before the event the arm exists to capture, and has not reopened since.** In the entire 11-session post-arm window the OVX minimum was **55.9** against a required **<44.2** — the gate was not close, and could not have been.

⇒ **The correct diagnosis is not "the threshold is too low." It is that a simultaneity requirement was imposed on two anti-correlated conditions.** No choice of number fixes that.

---

## 2. A DEEPER PROBLEM: **the gate prices a risk this structure already neutralises**

The cooldown gate is a proxy for *"is convexity expensive right now?"* **For the structure the plan actually mandates, that proxy is largely void.**

LESSONS #15 requires a **vertical call spread, never a naked call**, precisely *because a spread neutralises vega*. **Then I gated the spread on a vega proxy.** Black-Scholes at the spec's own moneyness (long ~5% OTM / short ~15% OTM, 60 DTE):

| IV | Net debit (% of spread width) | R:R |
|---|---|---|
| 35% | 24.5% | 3.08x |
| **44.2%** ← the gate line | **27.9%** | **2.58x** |
| **63.8%** ← today | **31.7%** | **2.15x** |
| 90% | 33.3% | 2.00x |
| 120% (2026's OVX high) | 33.3% | 2.00x |

**From the gate line to today's vol — a +44% move in OVX — the debit rises just +13.5%, and above ~90% IV it stops rising at all** (a vertical's value asymptotes to a fixed fraction of its width). **The gate blocks 100% of capital over a ~13.5% cost difference.**

*For contrast, the naked 150C the plan forbids goes **+140%** over the same vol move. **The vol gate is correctly specified — for the instrument LESSONS #15 bans.***

⚠️ **I am not claiming vol is irrelevant.** R:R still degrades 2.58x → 2.15x, and there is a **real** high-vol cost the model does not capture: **wider bid/ask and worse fills** — evidenced live when Option A failed to fill on 7/22-23. That deserves a control. It does not deserve a binary vol threshold.

---

## 3. WHY THE TWO OBVIOUS FIXES DON'T WORK — I tested both and both failed

- **❌ "Lower the OVX number."** Fixes nothing. The gate already opens 50% of the time; the problem is *when*.
- **❌ "Swap the vol proxy for a don't-chase price proxy."** I built the candidate — *Brent ≤ +10% above its trailing 20-day low* — and it fires on **0.0% of escalation days**, identical to the vol gate. **Any metric measuring "the move hasn't happened yet" is 0% on days the move is happening.** *(This is the finding that killed my own preferred replacement. Recording it because it constrains every future proposal in this class.)*

⇒ **The fix cannot be a better simultaneous condition. It must break the simultaneity.**

---

## 4. ✅ THE PROPOSAL — **SEQUENCE the two conditions instead of requiring them at once**

**Stage 1 — ARM (unchanged).** Tier-1 / Tier-2 event conditions fire exactly as today. This creates a **dated, expiring** armed state.

**Stage 2 — DEPLOY.** Within **20 trading days** of arming, on the **first** session satisfying **both**:

| Leg | Frozen test | What it controls |
|---|---|---|
| **(a) Vol decompression** | **OVX ≤ −15% from its running peak measured since the arming date** | "Don't buy the panic tick" — *relative to this crisis*, not to a calm-market absolute |
| **(b) Structure economics** | **Net debit ≤ 33% of spread width** (⇔ R:R ≥ 2.0:1), from a **live chain** at fill | The thing the vol legs were proxying for, measured directly. Also catches bad strike selection and blown-out spreads |

**Expiry:** if neither fires inside 20 td, **the arm EXPIRES un-deployed** and requires a **fresh** Tier-1/Tier-2 event to re-arm.
**Frame-breaker carve-out:** a **confirmed destroyed-capacity event** (clean FAL-01 / named-major with confirmed capacity loss / vessel SUNK) deploys on leg **(b) alone**. That is a regime change, not a chase.
**Unchanged:** vehicle (USO), structure (vertical call spread, 60-90 DTE, ~5%/~15% OTM), **max loss ~$500 defined**, and **your [Approve] at fire.** *This proposal changes the vol condition and nothing else about what the arm is.*

### What it would have done — post-arm window (armed 7/16)

| Rule | First fire | Entry | vs USO today ($127.47) |
|---|---|---|---|
| **OVX −15% from post-arm peak** | **7/28** | USO **$120.49** (OVX 57.2, Brent $84.09) | **+5.8%** |
| OVX −12% | 7/27 | USO $124.76 | +2.2% |
| OVX −20% | **never fired** (max decomp −17.1%) | — | — |
| **OLD vol gate** | **never fired, 11 of 11 sessions** | — | — |
| *(actual discretionary 7/24 fill)* | *7/24* | *USO $136.69* | *−6.7%* |

**−15% fired once, at the window's low.** ⚠️ **That is suspiciously good and I am flagging it as likely overfit — n = 1 window.** The robust claim is weaker and is the one I stand behind: **−10%, −12% and −15% all beat the discretionary fill, and the old gate produced no entry at all.** The *sequencing concept* is what the evidence supports; the exact threshold is a judgement call.

### 🔻 Per #21(b): this LOOSENS a gate, so it ships with THREE tightenings

My own ratified rule — *"a latency repair is not direction-neutral; pair a loosening with a tightening"* — applies here, and I will not slip this through as a bug-fix:

1. **The arm now EXPIRES (20 td).** v1 had **no expiry** — "ARMED-and-HOT" could persist indefinitely. This is the biggest tightening in the package.
2. **A structural-economics floor (b) is entirely NEW.** v1 had no test of what the trade actually costs.
3. **The decompression peak is measured from the arming date and RE-RATCHETS** — a fresh escalation raises the peak and therefore raises the bar. **The gate self-tightens in a worsening crisis.**

---

## 5. HONEST LIMITATIONS — what I could not resolve

- **Flat-IV model.** I priced both legs at one IV. Real chains have **skew**, and call skew steepens in a crisis, which would make the short leg richer and the spread **cheaper** than modelled — i.e. the bias runs *in favour* of my argument, so leg (b) should be graded on a **live chain**, never on this model. Leg (b) is written that way.
- **n = 1 backtest window.** One post-arm window. Not a strategy backtest.
- **Black-Scholes on USO** is approximate (contango decay, ETF tracking).
- **The bid/ask cost in high vol is real and unmodelled** — leg (b) partially catches it (a blown-out spread fails the debit cap) but it is not a full answer.
- **What I am NOT re-opening:** the pre-positioned "cheap convexity starter" — you **declined** that on Jun 29 in favour of deploy-on-trigger, and the XLE $65C stub demonstrated the decay risk. Not re-litigating a closed decision.

---

## 6. THE DECISION

**⚠️ This re-spec would NOT fire today** (decompression is −7.7%, needs −15%). **I am not writing a gate to fit the tape, and you can check that: under the proposed rule the arm stays un-deployed right now.**

| | Option |
|---|---|
| **A — [APPROVE] as written** | Sequenced gate, **−15%** decompression, ≤33%-of-width debit cap, 20 td expiry, frame-breaker carve-out. **My recommendation.** |
| **B — Approve with −12%** | Fires more readily (would have entered 7/27). Choose if you want *higher deployment probability*; the cost is a slightly worse average entry. |
| **C — [NO]** | Gate stays as written. **Then please make that ruling explicit** — the arm's capital is currently governed by a condition that has fired on 0 of 38 escalation days in three years, and I would rather carry a deliberate "we accept this arm may not deploy" than an unexamined defect. |
| **D — Retire the main arm** | Legitimate. The Branch-2 tail-rider is filled and live; the main arm has never deployed. Cleaner than carrying an armed state that never releases. |

**My recommendation: A.** The diagnosis is not the one I brought you a week ago — **the gate fires often, just never when it matters** — and sequencing is the only structural answer to two anti-correlated conditions.

**Whatever you rule, I will not quietly relax this to fit the tape** — and if you rule **C**, I will state on every surface that the arm is knowingly gated by a condition that does not fire on escalation, rather than let it read as ordinary discipline.

---
*Pre-registered before any deployment. Frozen constants only. Supersedes nothing until Will's explicit ruling; the gate as written remains in force in the meantime.*
