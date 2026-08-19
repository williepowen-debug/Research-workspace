# PLAYBOOK — FLOW-TRIGGER cards (physical supply-interruption class)

**Created 2026-08-18 (TERRY), on Will's RETIRE ruling for `TRY-FIRE-006`.**
**Status: DESIGN PATTERN, NOT A CARD. Nothing here is armable, nothing here has a position, nothing here expires.**

> **Why this file exists.** `TRY-FIRE-006` (Kharg-strand → USO call spread) was retired 2026-08-18 after 32 days unfired. **The card decayed; the DESIGN did not.** The numbers, the concentration guard and the clock rotted — the trigger logic and its anti-false-fire guards were correct on the day they were written and are still correct now. **Retiring a card should not delete cross-agent work that cost real effort to produce.** Extracted here so the next supply-interruption card starts from the finished version of this thinking instead of re-deriving it.
>
> ⛔ **Do NOT copy `006`'s numbers, concentration table, strikes, or dates from here or from the archived card. Those are exactly the parts that rotted.** Copy the STRUCTURE.

---

## 1. ⭐ The corroborator-anchored + veto pattern (FALCON, 2026-07-18)

**The problem it solves:** the obvious trigger for "exports stopped" is "the loadings series printed ≈ZERO." **That is a false-fire generator**, because the only pullable series (IMF PortWatch `port2164` `export_tanker`) is **AIS-based and ~90% blind to a dark fleet** — it prints literal ZERO for entire NORMAL months (Jan/May/Jul-2026 all 0). **A zero-loadings primary would be TRUE right now, with no strand.**

**The pattern:**

| role | instrument |
|---|---|
| **PRIMARY (causes the fire)** | ≥1 **dark-fleet-capable corroborator**, sustained ≥2 days, not vetoed — war-risk/P&I withdrawal *specific to the facility*, an official suspension/seizure declaration, a dark-fleet-capable tanker-tracking read, or an owner-agent tripwire |
| **VETO ONLY (can kill a fire, never cause one)** | the AIS/PortWatch series |

⇒ **Never let a blind instrument be the trigger. Let it be the refutation.**

## 2. ⭐ The one-directional-bias rule (TERRY, 2026-08-18 — the generalisation the 7/18 inversion implied but never stated)

**A measurement bias has a FIXED SIGN, but whether it is protective or dangerous is a property of the TEST it feeds, not of the instrument.**

AIS **under-counts**. Therefore:

| print | as a FIRE test | as a RETIRE test |
|---|---|---|
| **NONZERO** | ✅ strong — **vetoes** a fire (flow demonstrably continuing) | ✅ strong — **sufficient to retire** (if a 90%-blind instrument sees it, it is real) |
| **ZERO** | 🔴 worthless — can never **cause** a fire | 🔴 worthless — can never **keep a card alive** |

🔴 **The failure mode this closes — "FAILURE TO RETIRE":** the 7/18 inversion fixed the FIRE side and left the RETIRE side standing, so a **zero** print silently functioned as evidence the strand persisted. **Absence of visible resumption is NOT evidence of continued interruption.** ⚠️ **A guard fixed on one side reads exactly like a guard on every side.**
⇒ **Because a retire trigger can therefore be SILENT, any card using this pattern needs a dated clock as the retire clause's backstop.** *(General form: [[finding_measurement_bias_sign_is_fixed_harm_direction_is_not]], WALTER.)*

## 3. ⛔ Never anchor on the chokepoint transit count (PROME denominator ruling, 2026-07-17)

- A **≤18/day transit print fires on 86.6% of ALL crisis days** — near-zero discriminating power.
- **A collapsed transit count is NOT a collapsed export volume.** Bypass routing + STS transfers move crude *without* appearing in chokepoint counts — this is the reconciler between an 11% transit print and ZERO lost barrels.
- ⚠️ **Transits and facility loadings are DIFFERENT QUANTITIES.** A signal impeaching one does not automatically impeach the other — *but* if both are AIS-derived, the **instrument-class** impeachment reaches both. **Say which you mean.**

## 4. Executability — audit the trigger against instruments you actually HAVE

🔴 **`006`'s decisive lesson.** Its primary listed four corroborator doors. **One — the dark-fleet-capable tanker read (Kpler/Vortexa) — is not available to this fleet:** no API, no credential, no fetcher; it appears in `AGENTS/FALCON/SOURCES.md` as a website, and reaches us only as second-hand routed estimates explicitly labelled *"estimates, not measurements."*

⇒ **The card read as four independent doors and had three, and the missing one was the only QUANTITATIVE door** — so in practice it could fire only on an official declaration or an insurance notice. **Nobody wrote that down for 32 days.**
⭐ **Before registering any trigger: for each named corroborator, state HOW WE PULL IT. A door we cannot open is not a door.** *(`[[finding_executability_is_a_separate_audit_axis]]`.)*

## 5. The antecedent gate (BRENT proposed, PROME endorsed, 2026-07-27)

**The shared falsifier cannot be graded FIRED on price action alone.** *(Added after the book came within one relay of exactly this: Brent −6.8% and TLT rallying on a two-night pause was relayed as "splitting, oil leg firing"; BRENT ruled it categorically wrong — the antecedent never happened.)*
⇒ **A price move consistent with an event is not the event.** Name the antecedent, require it observed, and grade the legs only after.

## 6. Rule-#6 pre-documentation for gap-continuation buys

A supply-loss fire day is **violently GREEN** (oil gapping up = USO green), and **calls-on-a-green-day is a root-rule-#6 break.** Root rule #6 is a **mean-reversion entry-timing** rule; a supply-loss gap-continuation is explicitly **not** a mean-reversion entry.
⇒ **Pre-authorise the break IN THE CARD, in advance, with the reasoning** — never argue it at fire, when urgency and opportunity feel identical from the inside. *(Governed by the Will-ratified break test, `RISK_RULES` § "Breaking root rule #6".)*

## 7. ⚠️ Pre-locked layers rot — the meta-lesson, and it is the reason `006` died rather than being extended

A card's ZONE-1 is **written calm and read under pressure**, which is exactly why any figure inside it decays *while looking authoritative*. **Both `006` rot instances were hardcoded counts** (a concentration guard and a fire-time position line), 7/17 → 8/18, and a stale concentration guard **does not fail loudly — it PASSES.**

- ⛔ **NEVER hardcode a position figure in a pre-locked layer.** Point at the live source (`positions_from_forge.py`), not a number.
- ⛔ **NEVER write a relative clock (`~30d`).** A tilde has no fire date, so **nothing can be late against it** and no boot check can flag it. **One absolute date.**
- ⚠️ **Archiving a card removes it from `ledger_sweep` check A** — so **reconcile every surface BEFORE archiving**, or the move silently ends the only thing that would catch drift.
- 🔑 **And weigh this when deciding whether to keep a pre-built card at all:** the value proposition is *"don't re-derive under pressure."* If the pre-locked layer has demonstrably rotted, **the card is no longer buying what it claims**, and a fresh build on live numbers is strictly better than firing a stale one.
