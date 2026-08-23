# WALTER → Will · 2026-08-23 · **Rule 6b amendment, ready to apply — needs your word, not my edit**

**Why this is a proposal and not a commit:** rule 6b's letter lives in `MESSAGING/CROSS_SESSION_MESSAGING.md`, a shared Will-gated file, and **that rule's own text names WALTER's declining to write it as the model.** You directed the retune in-session (so rule 3's bar is met — your word, not a relay), but the file was ruled three times in twelve hours with PROME, RAV and DAEDALUS in the loop. **Applying it myself would desync their work and do the thing the file holds up as the counter-example.** Everything on WALTER's side is BUILT and committed; this is the mirror half.

**Already landed (my files, no gate):** `BOARD_CONSUMPTION_SPEC` **v0.20 §3.5.7** (the gate's operational half) · `SIGNAL_PROCESSING_CHECKLIST` **v0.37** Phase 3.5 doorbell step · `CLAUDE.md` IDENTITY 4th question + RULE 13 + boot step 9b · `registry/DOORBELL_LOG.tsv` · `walter_doctor` scaffolding fix.

---

## The one-sentence reason the gate moves

**The two-tier orchestration ruling changed the PRICE behind the doorbell, not its logic.** The remedy went from *wake a whole desk in its own window* (expensive, disruptive, you in the loop) to *a bounded subagent touch that drains the desk's whole inbox* (cheap, day-scoped, inside PROME's existing tier). **A gate calibrated against the old price is now systematically tight, and its errors have inverted: an over-doorbell wastes a cheap touch and is LOUD; an under-doorbell leaves a desk sitting on obligations and is SILENT.**

## Three changes

**① NEW PRECONDITION — P0: the desk must not already be IN-FLIGHT.** Desks now have **three** states, not two: live-in-own-window · dark · running as a PROME subagent. Check `PROME/state/ORCH_LOG.tsv` for an open touch plus `ListAgents`. **P0 fails ⇒ no doorbell.**
> Bought on pilot day one: **SAM was declared dead on a credit-wall failure notice and respawned while ALIVE** — PID 45988, 18 minutes elapsed, writing `STATUS.md` at 10:44:02 / 10:45:09 / 10:45:54, listed live in `ListAgents`. Two sessions briefly on one desk; SAM-2 caught it, wrote nothing, went idle under root Critical Rule #2. **A failure NOTICE is not a death certificate.** A doorbell against an IN-FLIGHT desk invites the same class from the other end.

**② UNIT OF DECISION: ITEM → DESK.** v1 asked *"does this ITEM justify waking a desk?"* — right when the touch cleared one item. Under the whole-inbox drain clause the touch clears **everything**, so the question is *"does this DESK's accumulated state justify a bounded touch?"* **The `action:` item stays the TRIGGER; the backlog becomes the YIELD** (a payload field, never a gate — INFO alone still never fires).

**③ LEG 3 GAINS A SECOND LIMB — 3b, cadence-is-the-deadline.** Keep 3a (named referent) exactly as ruled. Add: *the desk's median inter-session gap ≥7d **and** its oldest unconsumed `action:` item already exceeds that gap.* **For a low-cadence desk the GAP ITSELF is the dated event.**
> This is the direct fix for the blind spot **the ruling itself named**: *"the doorbell selects on the CLOCK; the backlog concentrates on desks with no clock."* v1 could not reach HENRY or BROCK **by construction**. 3b reaches exactly them.
> 🔴 **Gap computed from AUTHORED commits only — never `git log -- AGENTS/<DESK>/`.** That instrument reported HENRY at "94 commits this month" when 12 were HENRY-authored; it overturned a correct thesis on 8/22 and you struck it from 6b on 8/23. Building it into the gate would reproduce the identical error one level down, inside the mechanism the error was about.

## What it scores

Same seven dispatches, 8/22 night: **v1 = 1-of-7** (TERRY only). **v2 ≈ 3-of-7** — TERRY on 3a; **HENRY and BROCK now on 3b**. MARCO still fails (boots daily against a 9/8 date); `-007` still fails for want of any referent. **The two adds are precisely the two desks the ruling identified as the real backlog.** Still marginal by design; the marginality should stay visible.

## What does NOT change

WALTER never spawns (unchanged, ratified) · `action:`/`info:` semantics §3.5.4 (untouched) · the tiered spawn authority (untouched — 6b's re-worded paragraph stands) · **the ⅓ tightener stays UNWIRED** pending a base rate per `CHECK_STANDARD` §12. ⚠️ **v1 and v2 doorbells are TWO POPULATIONS under two price regimes — the 8/28 soak must not pool them**, or a price change reads as drift.

---

## ⚠️ Rider R2 — SETTLED, and my number was wrong

PROME asked me to settle the *"oldest 56d"* I quoted. **It is not the ACTION set and it was never a signal.**

| basis | figure | what it actually is |
|---|---|---|
| oldest unconsumed **ACTION**, `delivery_log.timestamp_routed` | **23d** | ZHAO `SIG-W-20260730-009` — matches PROME's 22d, one day on |
| oldest unconsumed **any role**, same basis | **30d** | ZHAO `SIG-W-20260723-011` |
| the **"56/57d"** I quoted | ⛔ **`AGENTS/DEWEY/inbox/WALTER/README.md`** | **a README**, aged on **mtime** — the one basis root canon forbids keying on |

**A scaffolding file was sitting at the top of the distribution my own telemetry emits, inflating the worst number it reports.** Fixed in `walter_doctor` (`_HANDOFF_SCAFFOLD` skip, matching the exclusion the same file already applied in two other checks — deliberately not widened): **headline went 57d → 35d.** The remaining 35d is a dated batch manifest, still on mtime, left in rather than silently dropped.

**Rider R1 independently confirmed while settling this:** `delivery_log` holds **478 lowercase `action` + 191 uppercase `ACTION` = 669**, and **320 `INFO` + 938 `info`**. A case-sensitive test reads 191 of 669 — RAV's 71% undercount, exactly as flagged. Every count in §3.5.7 and the log normalizes case.

— WALTER

> ⛔ **SUPERSEDED 2026-08-23 (same day, ~13:0x ET) — DO NOT READ AS LIVE.** This proposal was written at **11:05** and its *"needs your word, not my edit"* line was true **of 11:05 only**. Will granted the word in-session hours later — verbatim *"can you just fix both with my permission"* — and **the amendment LANDED in `MESSAGING/CROSS_SESSION_MESSAGING.md` rule 6b ③ (leg 3b, cadence-is-the-deadline).** ⚠️ **Banner added because this file was read as the live status of L3b and produced a false "the gate fired on an unruled leg" escalation on 2026-08-23** — a superseded proposal that still reads as pending is `[[finding_live_claim_in_a_closed_container_is_invisible]]` inverted: a CLOSED claim in a container that still looks OPEN. **Canonical: the rule 6b letter, never this file.**
