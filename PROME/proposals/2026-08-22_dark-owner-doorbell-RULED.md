# RULED — WALTER dark-owner doorbell (`WILL_QUEUE` row 75)

**Ruled:** 2026-08-22 ~23:5x ET (Sat, S7, laptop) · **Will, in-session, verbatim: _"ok go forward approved"_**
**Presented as:** adopt-with-three-amendments **plus four riders**, on PROME's recommendation, with RAV concurring.
**Scope of this word:** the doorbell gate and its encode. It does **not** rule the two spawn candidates, the roster/successor question, or the root-canon citation extension — each carried separately below.

> ⚠️ **Cite this item as `WILL_QUEUE row 75`, never bare "row 75."** `PROME/DOCKET.tsv` line 75 is the 2026-12-04 Goodgame/Tricolor sentencing (OTTO). RAV-caught; second live instance of the numbering-collision class root canon documents for "rule #6."

---

## What was ruled

**The missing `else` branch of `MESSAGING/CROSS_SESSION_MESSAGING.md` rule 6.** Rule 6 doorbells a live recipient at packet-commit and has no branch for a dark one. **Adopted:** when the ACTION recipient is DARK, WALTER doorbells PROME instead, with a one-line spawn recommendation and its reason. PROME decides.

### The gate — a conjunction of THREE, all required
1. The `action:` recipient is **DARK** (`ListAgents` at packet-commit — the check rule 6 already mandates), **AND**
2. it is an **`action:`** item, not `info:`, **AND**
3. **a REGISTERED clock fires before that desk's likely next boot** — a DOCKET row, a GATES row, or a dated position expiry. **The clock is NAMED AND LOGGED in the doorbell recommendation.**

Any one missing ⇒ it waits for the normal inbox.

**AMENDMENT 1 (leg 3) — why it is not cosmetic.** WALTER's draft leg 3 read *"a trigger within reach, a live position, a dated event, or a market open"* — a judgment call over two unmeasured inputs (WALTER's read of urgency, WALTER's guess at a desk's cadence). Legs 1 and 2 are mechanically checkable; leg 3 was where drift would live. **The strict form scores tonight's dispatches 1-of-7, not WALTER's 2-of-7** (TERRY `-002` has registered clocks — 9/9 buyback, 004's Sep-30 expiry; CARL `-007`'s clock was "a read that decays"). RAV's addition — *log the clock* — is what makes the miss counter computable after the fact; an unlogged clock is an unauditable leg.

**AMENDMENT 2 (the load-bearing one) — a doorbell-triggered spawn DRAINS the desk's whole WALTER inbox**, not just the triggering item, under the normal consume/integrate/commit standard.

> **Measured basis (PROME, this session; RAV reproduced independently).** 669 ACTION dispatches all-time; **34 handoffs still at their original path**, 26 dated ≤8/20. The holders are **not dark desks**: HENRY holds 7 unconsumed ACTION items with **94 commits this month and a commit today**; BROCK holds 6 with 51. Both use `processed/` correctly (HENRY 145 filed against 53 unfiled; BROCK 69 against 16), so the proxy is meaningful there. HENRY's oldest ACTION item, `SIG-W-20260807-001`, appears **nowhere in HENRY's tree** outside the unread handoff — unintegrated at 15 days. **WALTER's own STATUS reaches the same conclusion, verbatim: _"binding constraint is NOT intake; it is owner availability at the moment a signal lands."_**
>
> ⇒ **The doorbell fixes latency-to-boot; the measured backlog is non-consumption by desks that boot fine.** Without amendment 2 the fleet pays for a session and clears one item of fifty-three. With it, the marginal cost is unchanged and the yield becomes the backlog. **Already proven, never written down:** PROME's 8/20 REGINALD doorbell drained a 7-handoff backlog in one session and moved fleet unconsumed 105→98.

**AMENDMENT 3 — measure items-drained-per-spawn, registered-clock MISSES, and doorbells PROME DECLINED.** Not doorbells-per-dispatch. **WALTER's "tighten above ~⅓" self-check is NOT wired until a base rate exists** — `CHECK_STANDARD` §12 (base-rate-before-wiring, Will-ratified 8/21) governs.
- **The miss counter is computable, and it is what makes the gate falsifiable.** For every dispatch where the recipient was dark, compare the logged registered clock's date against the actual consumption date; clock first ⇒ a MISS, whether or not it was doorbelled. All inputs already exist in `delivery_log.tsv` + DOCKET + GATES. **Misses are silent by construction — over-spawns cost money and are visible, misses cost a decision and are not — so tuning on the visible number alone walks the gate back to 118 unread with every step looking like discipline** (WALTER's own §5 trap, named against its own interest).
- **The declined-doorbell counter is RAV's addition and points at PROME.** If WALTER doorbells correctly and PROME declines everything, drain rate stays high and misses stay low while the mechanism is dead. It is the only counter aimed at the coordinator's half of the loop.

### Riders
- **R1 — role case is a NAMED SPEC REQUIREMENT, not a note.** `delivery_log.tsv` holds **478 lowercase `action` + 191 uppercase `ACTION` = 669**. A case-sensitive check reads **191 of 669 — a 71% undercount biased toward the NEWER rows.** A doctor check written the obvious way would report a healthy queue off a quarter of the data. *(RAV caught this pre-build. PROME's figures used `.upper()` and are unaffected — luck, not care.)*
- **R2 — every emitted count NAMES ITS AGE BASIS.** PROME's 26 (signal-date) and WALTER doctor's 22 (stricter, pull-complete residues excluded) are the same population under two bases, not a contradiction. ⚠️ **Still unreconciled, flagged not smoothed:** the packet's *"oldest 56d"* against PROME's oldest unread ACTION at 22d — 56 most likely describes the 118 INFO-inclusive total, but that is **inferred, not proven. Do not quote "oldest 56d" of the ACTION set.**
- **R3 — the spawn is a FULL owner session that can integrate and commit, never a read-only receiver.** Spec §3.5.2: a read-only reader that clears an inbox produces a FALSELY-CLEARED one, strictly worse than an unconsumed one, because the live desk then boots to something that looks handled. Not mechanizable — it lives in the spawn prompt, which is why this belongs to PROME.
- **R4 — citation discipline:** `WILL_QUEUE row 75` in full. Extending root canon's "say which list you mean" rule to cover row-number collisions is **Will-gated and NOT taken here.**

---

## Encode assignments

| # | Change | Owner | Surface |
|---|---|---|---|
| 1 | Gate + amendments + R1/R2/R3 as new **§3.5.7**; CHECKLIST **Phase 3.5** entry | **WALTER** | `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` + checklist |
| 2 | Five-field dispatch log (doorbelled · logged clock · PROME decision · items drained · desk acted) + the **miss sweep** and **declined counter** as `walter_doctor.py` checks | **WALTER** | its own tools — the proven conversion path (§3.5.4 → doctor check #27) |
| 3 | **Three-outcome triage into the AUTO-INJECTED file** | **PROME** | `PROME/CLAUDE.md` Ask-First ⚠️ **critical — see below** |
| 4 | Change-log row | **PROME** | `PROME/AUTONOMY.md` |
| 5 | Rule-6 `else` branch — **drafted by PROME, Will-gated** (shared file; WALTER correctly declined to write it) | **Will** | `MESSAGING/CROSS_SESSION_MESSAGING.md` |

> 🔴 **Why #3 is the one that must not slip.** Tonight's founding error was PROME telling WALTER and Will that *"PROME spawns read-only subagents only"* — false; the grant sat in `AUTONOMY.md`, which is **not boot-read**. `PROME/CLAUDE.md` **is** auto-injected. **If this triage lands only where tonight's rule lived, PROME will mis-state it again the same way.** AUTONOMY's own rule already says log-here-mirror-there, and that rule has been broken once (FORGE grant, 17 days unlogged in both places). `[[finding_scope_boundary_asserted_from_proximity]]`

### The three-outcome triage (PROME's routing, ruled)
1. **Follow-up inside an already-approved workstream** ⇒ **Tier 1, PROME spawns now**, report-before-execute, with the drain mandate.
2. **New direction on a live registered clock** ⇒ **Tier 1 read-only pre-fetch now** (permitted by §3.5.2 — a read-only instance may read and act but **must NOT** mark the item consumed; VULCAN's 2026-07-16 precedent) **+ Tier 2 proposal to Will** for the full session.
3. **Neither** ⇒ normal inbox.
> Any trade recommendation is **Tier 3 and returns to Will** regardless of tier above.

---

## Carried separately — NOT ruled by this word

- **The two candidates.** `SIG-W-20260822-002` → TERRY reads **Tier 1** (follow-up in the approved 004 workstream) and is PROME's to run. `SIG-W-20260822-007` → CARL is a **new direction, Tier 2**, and stays Will's. ⚠️ **The TERRY signal's headline claim is overstated and the correction must travel with it:** it asserts the 30Y *"exactly round-tripped"* to 5.28, but that path mixes three official DGS30 readings (5.28 8/18 · 5.19 8/19 · 5.23 8/20) with a **`^TYX` intraday close** for 8/21. On the one day both are observable, `^TYX` runs ~2bp above DGS30 ⇒ **roughly 7 of the 9bp announcement move has unwound, not 9 of 9.** The 8/21 DGS30 official posts Monday and settles it. Direction holds; "fully unwound / UN-PRICED" overstates it.
- **⚠️ Observation worth carrying:** tonight's doorbell candidates were TERRY (**1 unread / 53 processed**) and CARL — **neither is a backlog desk**, while HENRY (53 unread) and BROCK (16) were not doorbelled at all. **The doorbell selects on the CLOCK; the backlog concentrates on desks with no clock.** The two mechanisms are complementary and **neither substitutes for the other** — do not let a healthy drain-per-spawn number be read as the backlog being addressed.
- **The roster gap (WALTER §7).** A dark desk with **no named successor** cannot be spawned into existence by any of this. Tonight produced a `EUROPE_MACRO` signal (Klarna's guide-down names Germany, its largest market); the domain code shipped 8/18 *because* Europe had no home; **HANS is Tier 2 and 34+ days dark.** This is the only obstacle the ruling does not touch. Own item, Will+PROME.
- **WALTER's ask ②** ("confirm spawn authority is PROME's alone") — **not confirmable as written, but not for the reason PROME first gave.** Authority is **TIERED**: Tier 1 covers read-only spawns and follow-ups in approved workstreams; Tier 2 covers new-direction domain spawns; Tier 3 covers trade proposals and spend. Not "PROME's alone" (Will keeps launch approval on new directions), and not "Will's alone" (PROME's 8/22 error, corrected on Will's challenge). **The half that stands and is now written down: WALTER recommends, WALTER never spawns.**

## Soak before tuning
Run the gate through the **8/28 cluster** (QCEW · MIDAS-06 · NEXUS falsifier · DAEDALUS sweep · BRT-26/COT #3 · T6 last data) **and the 9/8 Canadian counter-tariff date** — a dense week plus a dated event — logging all five fields. Review with real numbers before any threshold is wired. `[[finding_test_the_guard_not_just_the_guarded]]` — falsify the gate before trusting it; a guard's own v1 fails on first run.
