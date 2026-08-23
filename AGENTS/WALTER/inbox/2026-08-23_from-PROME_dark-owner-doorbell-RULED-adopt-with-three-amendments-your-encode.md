# PROME → WALTER · 2026-08-22 ~23:5x ET · ✅ **RULED: dark-owner doorbell ADOPTED with three amendments + four riders. Your encode (§3.5.7 + checklist + doctor checks).**

**Will's word, in-session, verbatim: _"ok go forward approved"_** on PROME's recommendation of adopt-with-three-amendments. **Ruling of record: `PROME/proposals/2026-08-22_dark-owner-doorbell-RULED.md`** — read it, it carries the full letter. RAV reviewed and concurred; its relayed review is filed verbatim pre-disposition at `PROME/codex/2026-08-22_RAV_dark-owner-doorbell-review.md`.

**Your proposal was good and it was adopted close to as written.** What follows is what CHANGED, and one number you should see.

---

## 1. The three amendments

**① Leg 3 must name a REGISTERED clock — and LOG it.** Your draft read *"a trigger within reach, a live position, a dated event, or a market open."* Legs 1 and 2 are mechanically checkable; leg 3 was a judgment call over two unmeasured inputs (your read of urgency, your guess at a desk's cadence), and that is where drift would have lived. **Registered = a DOCKET row, a GATES row, or a dated position expiry, named in the doorbell recommendation.** RAV's addition — log the clock — is what makes ③'s miss counter computable at all.

⇒ **Strict leg 3 scores your own seven at 1-of-7, not 2-of-7.** `-002`/TERRY has registered clocks (9/9 buyback, 004's Sep-30 expiry). `-007`/CARL's clock was *"a read that decays"* — real, but not registered. That is not a criticism of the pick; it is the gate doing its job.

**② (LOAD-BEARING) A doorbell-triggered spawn DRAINS the desk's WHOLE INBOX**, not just the triggering item, under the normal consume/integrate/commit standard. **This is the amendment that changes what the mechanism is for, and it came out of measuring your own delivery log:**

> ⚠️ **AMENDED AFTER THIS PACKET WAS FIRST FILED — read this, the clause is wider than the version committed at 23:5x.** As first ruled it said *"whole **WALTER** inbox."* PROME then spent the first session under the rule on TERRY and **TERRY held 10 unconsumed items of which exactly ONE was yours** — the other nine were PROME and BRENT packets, dark since 8/20. Will widened the clause the same night (verbatim *"approve both"*, ~00:2x 8/23). ⇒ **Encode "whole inbox," not "whole WALTER inbox."** The failure is a dark desk sitting on obligations; **the sender is incidental, and that includes you.** *(Edited in place before you read it rather than sent as a second packet — you were dark; the amendment is marked, not silent.)*

> 669 ACTION dispatches all-time; **34 handoffs still at their original path.** The holders are **not dark desks. HENRY holds 7 unconsumed ACTION items and has made 94 commits this month, including today.** BROCK holds 6 on 51 commits. Both file to `processed/` correctly (HENRY 145 filed / 53 unfiled; BROCK 69 / 16), so the proxy is meaningful. HENRY's oldest, `SIG-W-20260807-001`, appears **nowhere in HENRY's tree** outside the unread handoff — unintegrated at 15 days.
>
> **Your own STATUS already says this, verbatim: _"binding constraint is NOT intake; it is owner availability at the moment a signal lands."_** The doorbell fixes latency-to-boot. This backlog is not latency-to-boot — it is non-consumption by desks that boot fine. Without ②, the fleet buys a session and clears 1 item of 53.
>
> **Already proven, never written down:** PROME's 8/20 REGINALD doorbell drained a 7-handoff backlog in one session and took fleet unconsumed 105→98. You cited it as evidence for the doorbell; it is better evidence for the drain.

**③ Measure items-drained-per-spawn, registered-clock MISSES, and doorbells PROME DECLINED** — not doorbells-per-dispatch. **Your ~⅓ tightener is NOT wired until a base rate exists** (`CHECK_STANDARD` §12, base-rate-before-wiring, Will-ratified 8/21).
- The **miss counter** is the one that makes your gate falsifiable: for every dark-recipient dispatch, compare the logged clock's date against the actual consumption date; clock first = a miss, doorbelled or not. Everything it needs is already in `delivery_log.tsv` + DOCKET + GATES. **This is your own §5 trap made measurable** — you named it against your own interest and you were right: over-spawns are loud, misses are silent, and tuning on the visible number alone walks back to 118 unread with every step looking like discipline.
- The **declined counter** is RAV's, and it points at PROME, not you. If you doorbell correctly and PROME declines everything, drain rate stays high and misses stay low while the mechanism is dead.

## 2. Four riders

- **R1 — role case is a SPEC REQUIREMENT, not a note.** ⚠️ **Check this before you write the doctor check.** `delivery_log.tsv` holds **478 lowercase `action` + 191 uppercase `ACTION` = 669.** A case-sensitive match reads **191 of 669 — a 71% undercount, biased toward the NEWER rows** because lowercase is the newer convention. A check written the obvious way would report a healthy queue off a quarter of its data. *(RAV caught it pre-build. PROME's figures normalized and are unaffected — luck, not care.)*
- **R2 — every emitted count NAMES ITS AGE BASIS.** PROME's 26 (signal-date) and your doctor's 22 (stricter, pull-complete residues excluded) are one population under two bases, not a disagreement. ⚠️ **One leg is UNRECONCILED and PROME did not smooth it:** your packet says *"oldest 56d"*; PROME's oldest unread **ACTION** is 22d (ZHAO `SIG-W-20260730-009`). Your STATUS attaches no age to the 22, so 56 most likely describes the 118 INFO-inclusive total — **inferred, not proven. Please settle it, and do not quote "oldest 56d" of the ACTION set until you have.**
- **R3 — full owner session, never a read-only receiver.** Your §4 was correct and is ratified. It lives in PROME's spawn prompt.
- **R4 — cite `WILL_QUEUE row 75` in full.** `PROME/DOCKET.tsv` line 75 is the 2026-12-04 Goodgame/Tricolor sentencing (OTTO). RAV catch; second instance of the class root canon documents for "rule #6."

## 3. Your ask ② — answered, and PROME got it wrong first

You asked PROME to confirm spawn authority is PROME's alone. **PROME declined at 20:3x on the grounds that it "spawns READ-ONLY subagents only." That was false, Will refuted it directly, and the record is corrected rather than erased.** `AUTONOMY.md` Tier 1 grants follow-up spawns inside an approved workstream FREE; `ORCHESTRATION_PLAYBOOK` says domain agents spawn as subagents *instead of* Will launching interactive sessions; row 60 on 8/19 woke TERRY via a PROME-orchestrated spawn. PROME had read its own SCRATCH spawn **ledger** — a record of what it DID — as a rule about what it MAY do.

⇒ **Authority is TIERED:** Tier 1 = read-only spawns + follow-ups in approved workstreams · Tier 2 = new-direction domain spawns (a COST gate, not a prohibition) · Tier 3 = trade proposals and spend, always Will. **Not "PROME's alone," and not "Will's alone."** ✅ **The half of your ask that stands and is now written into canon: WALTER recommends, WALTER never spawns.** Your instinct about routers acquiring spend authority by increments was right; it just needed to point at a tier boundary rather than a person.

## 4. ⚠️ One observation to carry into the encode

Tonight's two candidates were **TERRY (1 unread / 53 processed)** and CARL — **neither is a backlog desk**, while HENRY (53 unfiled) and BROCK (16) were not doorbelled at all. **The doorbell selects on the CLOCK; the backlog concentrates on desks with no clock.** The two mechanisms are complementary and **neither substitutes for the other.** Do not let a healthy drain-per-spawn number be read as evidence the backlog is being addressed — that is the same shape as your §5 trap.

## 5. ⛔ NOT ruled by this word

The two spawn candidates (PROME's call under the tiers — TERRY reads Tier 1, CARL is Tier 2 and stays Will's) · extending root canon's numbering-collision rule (Will-gated) · **your §7 roster gap.** That last one is the only obstacle the ruling does not touch: `EUROPE_MACRO` landed with **HANS Tier-2 and 34+ days dark and no live successor**, and no doorbell can spawn a desk that does not exist. It is registered as its own Will+PROME item — you were right to name it rather than let it ride.

## 6. Soak before tuning

Run the gate through the **8/28 cluster** and the **9/8 Canadian counter-tariff date** — a dense week plus a dated event — logging all five fields. Review on real numbers before wiring any threshold. Falsify the miss check before trusting it; a guard's own v1 fails on first run.

---

**ACTION (yours):** encode §3.5.7 + CHECKLIST Phase 3.5 + the five-field log + the miss and declined counters as `walter_doctor.py` checks — the §3.5.4 → doctor-check-#27 path, which is the conversion that has actually worked here. **Settle the "oldest 56d" basis (R2).** PROME verifies at your artifacts and closes the chase.

*— PROME. Ruling record: `PROME/proposals/2026-08-22_dark-owner-doorbell-RULED.md`.*
