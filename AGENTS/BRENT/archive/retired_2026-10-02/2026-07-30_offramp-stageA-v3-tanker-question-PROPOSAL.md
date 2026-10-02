# THE TANKER QUESTION — OFF-RAMP **STAGE A v3** · **PROPOSAL FOR WILL'S [APPROVE / NO]**

**Author:** BRENT · 2026-07-30 ~5:10 PM ET · **Status:** ✅ **RULED 2026-07-30 — WILL APPROVED OPTION B** (harvest + tenor only; entry left as-is). **Implemented same session** in `TRADE.md`: tenor **60-90 → 21-35 DTE**, and a new mandatory **HARVEST RULE** (H1 hard time stop 8 sessions after entry · H2 take ≥half at −7% · H3 exit in full on any close back above entry). ⚠️ **Options A and C remain LIVE and unruled — entry defects ②③④ are KNOWINGLY OPEN by decision, not oversight**, and are recorded as such in `TRADE.md` so the playbook never reads as ready. **Flagged with the ruling: the harvest rule governs the exit of a trade that, under the unchanged entry spec, may not be enterable — the STNG veto blocked 2 of 2 observed analogues.**
**Governs:** off-ramp round-trip playbook **Stage A (entry)** + **structure/tenor** (`TRADE.md`). Stage B persistence (ratified 7/29) is **untouched**.
**Frozen constants only.** *Investigating the tanker leg turned up three defects behind it, and the tanker leg is the least serious of them.*

---

## 0. ⛔ FIRST — A CORRECTION TO WHAT I TOLD YOU THIS MORNING

I said the STNG leg *"would have been FORBIDDEN to fire on the only real off-ramp this regime has produced."* **That was wrong in an important way: Jun-17 was NOT a real off-ramp.** My own LESSONS #19 records it as **0-of-4 on physical legs** (JWLA-033 not lifted, liners still on Cape, transits dark, demining 30+ days). **This regime has produced ZERO genuine physical reopenings.**

**So I cannot calibrate "real vs fake" on data — the "real" case has never happened.** Both analogues are false-positives on the *physical* test.

**But that turns out to be the wrong test, and the correction is what makes this tractable:**

| | Apr-17 — unilateral minister quote | Jun-17 — **signed** multilateral MOU, 0-of-4 physical |
|---|---|---|
| Brent +3d | **+12.8%** | **−3.1%** |
| Brent +10d | **+19.7%** | **−9.7%** |
| 30d extreme | **+30.6%** | −10.0% then **+21.7%** |
| **Would a crude short have paid?** | **destroyed** | **won decisively for ~2 weeks** |

**⇒ Jun-17 was 0-of-4 on physical verification and the short still won −9.7%.** The correct restatement of the defect: **the gate would have blocked the one trade that would have made money** — not because it demanded reality, but because it demanded the *wrong kind* of evidence.

---

## 1. THE DIAGNOSIS — four layers, and **the tanker leg is #3 in severity**

**① 🔴 WRONG TENOR, AND NO HARVEST RULE AT ALL — the most expensive defect, and it is not about entry.**
The playbook specifies **60-90 DTE**. The one qualifying move **fully round-tripped in 20 days**:

| Days from entry (day+2) | P&L on the underlying |
|---|---|
| trough (day 9, **7 sessions held**) | **−8.1%** |
| hard stop day+10 | **−7.8%** ← captures 96% of the available move |
| day+15 | −2.4% |
| day+17 | **+8.8%** — already a loser |
| day+20 | **+13.1%** |

**A 60-90 DTE bear put spread held to expiry gives back everything and then some.** The playbook has **no profit target, no time stop, no trailing rule** — my auto-memory already flags this exact class (`[[finding_profit_zone_needs_its_own_harvest_rule]]`) and the playbook was written without one.

**② 🔴 STAGE A DEMANDS PHYSICAL VERIFICATION FOR A TRADE WHOSE MONEY IS MADE AT THE ANNOUNCEMENT — this directly contradicts my own LESSONS #11.**
LESSONS #11: *"Phase 2 price crash triggers at ANNOUNCEMENT, not delivery… Position SHORT before reopening is confirmed — waiting for barrels to arrive means missing 80% of the move."* **Stage A requires transits >35/day sustained 2 days.** On Jun-17 transits were **dark** and the short won −9.7% anyway. **The spec and the lesson are in direct opposition, and the spec won.** *(Third such contradiction found today — #18 vs #19, #11 vs Stage A, and the same-week falsifier vs #21(b).)*

**③ 🟠 THE STNG LEG IS NON-DISCRIMINATING.** Tankers rose on **both** (Apr-17 STNG +3.9%; Jun-17 +2.6%/+5.0%). ⚠️ **Fair to the leg: on Apr-17 blocking was the RIGHT call — but only by accident, because it blocks everything.** A check that always says no is correct whenever the answer is no, and carries no information either way.

**④ 🟠 The transit leg (>35/day ×2 sessions) is the same error as ②** — a lagging physical confirmation gating a trade that must be on before confirmation exists.

---

## 2. WHAT ACTUALLY DISCRIMINATED — and it is already half in the spec

**(a) The announcement's INSTITUTIONAL QUALITY — Stage A leg (i), which works.** Apr-17 was a *unilateral Iranian minister quote*, contradicted by concurrent state action. Jun-17 was a **signed multilateral instrument with a named counterparty and an explicit blockade-lift commitment.** That distinction separated the two cleanly and it is already leg (i).

**(b) 🆕 CRUDE'S OWN 2-DAY FOLLOW-THROUGH — the discriminator I did not have.**

| | day+2 reading | must |
|---|---|---|
| **Apr-17** | **+9.0%** | BLOCK ✅ |
| **Jun-17** | **−2.1%** | FIRE ✅ |

**2-for-2, where the tanker check was 0-for-2 — and it reads the instrument being TRADED rather than a second-order proxy.**

⚠️ **Robustness check, because n=2 demands one:** **every threshold from −2% to +8% separates the two cases** — an **11-percentage-point gap**. This is not a tuned number; the signal is *the sign and persistence of the move*, not the level. A knife-edge fit would have separated at one value only.

---

## 3. ✅ PROPOSED — **STAGE A v3**

**▸ ENTRY (both required):**

| Leg | **FROZEN test** |
|---|---|
| **(i) Institutional quality** *(unchanged — it is the real discriminator)* | Signature / sovereign-action class: **named counterparty + signed instrument + explicit closure-or-blockade commitment.** A unilateral minister statement does **NOT** qualify (the Apr-17 bar). |
| **(ii) 🆕 Follow-through** *(REPLACES the transit leg and the STNG veto at entry)* | **At the close of day +2, Brent must be ≤ −1.0% below the announcement-day close.** Fire that close; do **not** fire on the headline. |

**▸ 🆕 HARVEST — MANDATORY, and this is the highest-value change in the proposal:**
- **HARD TIME STOP: exit no later than 8 trading sessions after entry** (≈ day+10 from the announcement). **Non-negotiable, regardless of P&L.**
- **PROFIT TARGET: take ≥half off at −7.0% on Brent from entry.**
- **STOP: exit in full on any close back ABOVE the entry level** — the round-trip has begun.

**▸ STRUCTURE:** tenor **21-35 DTE** (was 60-90). ⚠️ **Shorter tenor raises theta and gamma risk — accepted deliberately**, because the 60-90 DTE structure was mismatched to a trade with a **9-session** life, and mismatch cost more than theta will.

**▸ STNG — DEMOTED from veto to informational.** Keep the read on the card, but it **cannot block a fire**. If you prefer to keep a tanker veto, the only version with power is the **dispersion form**: veto **only** when tankers are **flat (±1%)** on a claimed operational reopening (nobody believes it); a tanker **rally** is the ton-mile channel per LESSONS #19 and is **not** disconfirming.

**▸ 🔻 Per the #21(b) rule (a spec repair is not direction-neutral): this LOOSENS entry, so it ships with tightenings.** Removing two entry vetoes makes a **short**-arming gate easier to satisfy. Paired against it: **(1)** a mandatory hard time stop that did not exist; **(2)** a profit target that did not exist; **(3)** an above-entry stop that did not exist; **(4)** a **2-day delay** before any capital moves, which is itself a real filter — it is what blocks Apr-17. **Net: entry is easier, but the position can no longer be held into a round-trip, which is how the one historical case actually lost money.**

---

## 4. HONEST LIMITS — read these before approving

- **The entry rule is n=2. The harvest rule is n=1.** One qualifying event in the sample. **This is calibration on a single trade and should be held loosely.**
- **The 11-point separation is the strongest thing here** — it means the *direction* of the discriminator is robust even though the *sample* is tiny.
- **The time stop is the one rule that cannot really be overfit:** it does not try to find the top, only to refuse to hold past a known reversal zone. If it is wrong it costs upside, not capital.
- **Zero true positives exist.** A genuine physical reopening has never occurred in this regime, so **no rule proposed here has ever been tested against one.** If a real reopening behaves differently from a signed-but-unverified one — plausibly a *larger and more durable* move — the time stop will cut it early. **I would rather cut a real one early than hold a fake one into a +21% reversal**, but that is a judgement and it is yours.
- **What I did NOT change:** vehicle (USO bear put spread, never naked — LESSONS #15), **~$500 max defined risk**, Stage B persistence + kill test (ratified 7/29), and your **[Approve] at fire**.

---

## 5. THE DECISION

| | Option |
|---|---|
| **A — [APPROVE] Stage A v3 as written** | Institutional-quality + 2-day follow-through entry; mandatory harvest (8-session stop / −7% target / above-entry stop); 21-35 DTE; STNG demoted to informational. **My recommendation.** |
| **B — Approve the HARVEST + TENOR only; leave entry as-is** | Fixes defect ① (the expensive one) and leaves ②③④. **Defensible if you want one change at a time — and it captures most of the money.** |
| **C — Approve v3 but KEEP a tanker veto** in the dispersion form (veto only on flat ±1%). |
| **D — [NO]** | Playbook stands. ⚠️ Then it is knowingly carrying a 60-90 DTE structure on a ~9-session trade with no exit rule, and I will label it that way on every surface rather than let it read as ready. |

**Recommendation: A.** If you want to move in one step instead, **B is the high-value half** — the harvest rule is worth more than the entry rule, because the historical case shows the trade was won by day 9 and *lost by being held.*

---
*Pre-registered before any deployment. The playbook remains ARMED-PASSIVE and unchanged until ruled. No capital moves on this document.*

---

# ADDENDUM — 2026-07-30 ~7:15 PM ET · **FALCON ANSWERED THE GATE-2 QUESTION, AND OPTIONS A/C SHOULD BE RE-READ BEFORE ANY FUTURE RULING. THE ANCHOR I PROPOSED WAS THE WRONG ONE.**

**Status of this addendum:** not a new ask. **Will ruled Option B; A and C remain live and unruled. This records that the A/C design is now MATERIALLY BETTER than what was on the table when B was chosen** — so if A/C is ever revisited, revisit *this* version, not §3 above.

## 1. The answer: YES, materially — but narrower, capped, and on a different instrument

**The closure is OVER-DETERMINED — four independent layers, and the 7/29 wave touched only one:**

| Layer | Degraded? |
|---|---|
| ① Declaratory closure (IRGC) | ❌ a statement needs no hardware |
| ② **Kinetic enforcement** (coastal surveillance, ASMs, fast boats) | ✅ **the only layer hit** |
| ③ **MINES already in the water** | ❌ **you cannot bomb a minefield clear** — multi-week MCM op, not an Iranian decision |
| ④ **The US naval blockade** | ❌ it is **American**, still in full effect |

**⇒ Three of four layers survive intact. That is the cap.** My "enforcement degradation → reopening" framing **over-stated the mechanism.**

**But the hole is real and FALCON confirmed rather than softened it:** the two closures bind **different traffic** — the US blockade targets **Iranian** barrels; Iran's closure targets **everyone else's**. So degrading Iranian enforcement can let **non-Iranian traffic resume with no sovereign act and nothing to announce.** Shape: **a grind, not a snap** — ~11% toward **30-50%** of baseline over **weeks**, ceilinged by the mines. **A step-change to near-normal is NOT this mechanism — look for a deal you missed.**
**Magnitude [FALCON, judgment not calculation, labelled as such]: P(sustained transit recovery >50% of baseline for 10+ days, absent any signature, within 30 days) ≈ 15-20%, up from ~5%.**

## 2. ⛔ MY PROPOSED ANCHOR WAS WRONG — war-risk LEADS, transit count LAGS

§3 above proposed replacing the transit leg with crude's own follow-through, and treating transits as the physical anchor. **The causal chain runs the other way:**

> enforcement degraded → a few hulls test → **no attacks over time** → **war-risk premia FALL** → more hulls → **transit count climbs**

**A transit-count gate watches the LAST link.** Ordered ladder, most-leading first: **(1) Hormuz hull premium falling while West-Coast-Saudi stays flat at ~0.1%** — *already instrumented in FALCON's `workbook/WARRISK.tsv`, boot-gated at 7 days, nothing to build* · **(2) JWC/Lloyd's listed-areas revision or P&I clubs re-entering** · (3) mine-clearance progress · (4) transit count *(PortWatch, lags 5-8d on top of all of it)*.

## 3. 🔑 THE DESIGN FIX I DID NOT HAVE — a non-sovereign institutional anchor

I framed the problem as *"Stage A needs a signature, and this mechanism produces recovery without one."* FALCON's answer:

> **A JWC/Lloyd's listing revision or a P&I club re-entry is a DATED, PUBLISHED, VERIFIABLE INSTITUTIONAL ACT THAT IS NOT A SOVEREIGN ACT.**

It restores exactly the properties I wanted from the signature requirement — **discrete, dated, hard to fake, hard to reverse quietly** — without requiring any government to announce anything. **This is strictly better than the transit-only entry in §3**, because it keeps the gate from having to compensate entirely through a persistence test. **If A/C is revisited, THIS is the Stage A-bis anchor, not crude follow-through alone.**

## 4. ⚠️ Two guards that must ship with it

- **NEGATIVE CONTROL:** a transit recovery **with war-risk premia still at 7.5-10% of hull is NOT normalisation** — it is escorted convoys, state-directed traffic, or risk-tolerant operators taking a rate. **Must not fire Stage A-bis.** *"Hulls are moving" ≠ "the market believes it is safe."*
- **TWO-WAY READ — the premium may go UP first.** Stripped of standoff enforcement, Iran's cheap residual options are **mines and unattributable attacks** — the two things insurers fear most. **A rising Hormuz premium after 7/29 does NOT refute the mechanism**; it means Iran substituted toward the passive layer and the reopening is *further* away.

## 5. 🔴 THE PAIRED TIGHTENING — and the false-fire that makes it non-negotiable

Per LESSONS #21(b), removing the sovereign-act requirement **loosens a short-arming gate** and must ship with a tightening. FALCON found the specific thing it must be tightened against, live:

> **A UKMTO advisory reading "the Strait of Hormuz is now open and blockade operations have ceased," threat level lowered to "moderate," ranks HIGH in a July-2026 search on exactly this question. It is dated 18 JUNE 2026** — the MOU era. **The blockade resumed 14 July and is live today.**

**Why it is the worst possible false-fire for this gate:** it is **UKMTO — an institutional primary**, so it passes every source-quality filter I have; it has **exactly the semantic shape Stage A-bis would key on**; and **it requires no sovereign act, so dropping the signature requirement removes the one thing that currently catches it.**

**⇒ PAIRED TIGHTENING (adopted into any future A/C): every institutional/advisory input to Stage A-bis must be DATE-VERIFIED AT THE PRIMARY, and the advisory's OWN PUBLICATION DATE must fall inside the arming window — not merely that the text was retrieved during it.**

⚠️ **THIRD INSTITUTIONAL-GRADE DATELINE FALSE-FIRE IN THREE DAYS** — April-2026 Petroline (FALCON→me), Sept-2019 Abqaiq (me→FALCON), now June-2026 UKMTO (FALCON→me). **All three from sources that pass every quality filter. The failure mode is not source grade, it is DATELINE — and it is now a pattern, not a coincidence.**
