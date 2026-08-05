# Roster Migration — PHASE 0 RULING TABLE (draft for Will)

**Drafted:** 2026-08-04 session 4 (PROME) · **Status:** DRAFT — awaiting Will's rulings on Part B
**Basis:** RAV roster-responsibility plan **v4** (Will-ACCEPTED 8/4 eve), Phase 0 §"Decisions to make" + §"Column Ownership" open decision
**Executor contract (Will-ruled 8/4 eve):** Phase 0 = **PROME drafts, Will rules.** Staged execution; each named agent edits its OWN domain.
**Deliverable per plan:** a short ruling table pasteable into `PROME/ROSTER.md` and referenceable by DAEDALUS. Part D below is that table.

⚠️ **This draft is PRE-PREFLIGHT.** The plan orders RAV's targeted preflight *before* the Phase 0 table, and its output explicitly includes *"one list of plan amendments required before edit."* I drafted now because **four of Phase 0's decisions were already ruled 8/4 eve**, so the residue is small and cheap to have ready. **Part B rulings should be treated as amendable by the preflight addendum** — that is the plan's design, not a defect.

---

## PART A — Already ruled 8/4 eve. Recorded, NOT re-asked.

Will ruled all six of the plan's "Will Decisions Needed" points. Restated here so the ruling table is self-contained and DAEDALUS can reference one artifact.

| # | Decision | Ruling |
|---|---|---|
| 1 | Phase 1 labels are **descriptive only** — no change to routing, boot priority, DAEDALUS grading, WALTER delivery, or NEXUS read obligations until a later explicit operational ruling | ✅ **ACCEPTED as written** |
| 2 | **Column ownership split by source of truth** — PROME: human bucket/cadence · DAEDALUS: class/maturity/structural gaps · WALTER: routing/delivery · NEXUS: brief schema + synthesis-read obligations | ✅ **ACCEPTED as written** |
| 3 | **`PROVISIONAL ACTIVE` is not a demotion** — the agent exists and should run; proof criteria are pending | ✅ **ACCEPTED as written** |
| 4 | **Correction propagation is publisher-owned** — WALTER owns BOARD/signal correction linkage; the publishing agent owns downstream propagation of its own corrected figure/tool/state | ✅ **ACCEPTED as codification** of existing root-canon practice (root step 1c), not new doctrine |
| 5 | **Scheduled/off-repo routines need owner state** — routine reads owner-maintained state, carries stale-state alarms, never resolves prediction rows unless explicitly authorized | ✅ **ACCEPTED as codification** of the BRENT routine architecture already in-repo (`AGENTS/BRENT/SCHEDULED_RUNS.md`, built 8/3) |
| 6 | **No new organizing agent yet** — change the ownership map first; create an agent only if the map still leaves recurring work unowned | ✅ **ACCEPTED as written** |

**Also ruled 8/4 eve (binding on everything below):** staged execution, **each named agent executes in its OWN domain**; RAV preflight + Phase 0 + Phase 1 authorized for the **8/6-8/9** window; **Phases 3-4 HELD** for a separate ruling after the preflight addendum.

---

## PART B — Open. Four rulings needed from Will.

### B1. Should the roster explicitly separate domain / organizing-service / review / event-driven / provisional agents?

**PROME recommendation: YES — but the scope is narrower than the plan's diagnosis implies, and that matters for effort.**

The plan's Core Diagnosis says the roster "flattens different kinds of work into one broad active-agent list." **That is true of one bucket, not of the file.** `PROME/ROSTER.md` already separates **TIER-2**, **DORMANT**, **RETIRED**, **ARCHIVE SOURCES**, **SPECIAL**, **TOOL-CLASS INSTRUMENTS**, plus spinout provenance and an explicit-unowned-gaps section.

**The actual flattening is inside `## ACTIVE — persistent domain owners (30)`**, which currently holds true domain owners *and* organizing/service agents *and* event-driven specialists *and* newborns, under a header whose own words say "persistent domain owners."

⇒ **The work is splitting ACTIVE(30), not building a taxonomy from scratch.** Recommend ruling YES on the separation, scoped to that bucket. Cheaper, lower-risk, and it makes the existing header stop lying.

---

### B2. Should cadence and authority be separated everywhere they matter?

**PROME recommendation: YES, but "where they DIVERGE" — not "everywhere."**

A blanket ruling invites two fields on all ~39 rows, most of which would restate each other (a standing domain owner is `ACTIVE`/`domain authority` — one label carries both). The rows where it earns its keep are the ones where cadence and authority genuinely disagree:

- **TIER-2 / on-demand with real authority** (DEWEY, HANS, OTTO, CREED — spawned rarely, but authoritative in-lane when they run)
- **PROVISIONAL ACTIVE** (standing cadence, authority not yet proven)
- **EVENT-DRIVEN SPECIALIST** (WAL, OZK — cadence is a print calendar, authority is narrow-but-real)
- **SPECIAL** (DAEDALUS, YEYOU, RAV — cadence varies; authority is the whole point)

⇒ Recommend: **separate the two fields only where they diverge; a single label carries both where they don't.** State the rule on the row so a future reader knows the omission is deliberate, not missing.

---

### B3. Should every recurring responsibility require exactly one owner, one artifact, one escalation path?

**PROME recommendation: YES as a registration rule for new/changed responsibilities — with one constraint the plan does not mention, and it is load-bearing.**

⚠️ **Root canon deliberately mandates scoped overlap:**

> *"Scoped overlaps are intentional — reconcile shared metrics to **one figure**, don't silo: **CORAL↔MARCO** (FL migration/tourism) and **AEOLUS↔CORAL** (FL climate/coastal)."*

So a naïve "exactly one owner" ruling would **contradict standing Will-approved canon** and, read literally, would push agents to silo exactly where canon says reconcile.

⇒ Recommend the ruling be worded as: **one owner *of record* per responsibility — meaning one owner accountable for the reconciled figure and one escalation path — which does NOT forbid multiple agents working a shared metric.** Overlap stays legal; ambiguity about *who reconciles and who answers for it* does not.

This is the single wording change I would most want made before Phase 1, because the taxonomy gets written against it.

---

### B4. Column ownership — actual new columns, or a compact responsibility table referenced by existing rows?

**PROME recommendation: COMPACT table** (which is also the plan's own default: *"Start compact; only add columns if a consumer needs machine readability."*)

**Concrete reason to hold the line here:** the machine-readable consumer **already exists and is owned elsewhere** — `AGENTS/DAEDALUS/FLEET_MAP.tsv` (class/maturity, DAEDALUS-owned) with `FLEET_DIRECTORY.md` generated from it, and `AGENTS/WALTER/REGISTRY.tsv` for routing. Adding class/maturity/routing **columns** to `ROSTER.md` would duplicate three owned sources into a fourth surface as parallel prose — **precisely the failure the plan's own Column Ownership section opens by warning against**, and precisely the drift class that produced the WP-W2 and OZK roster lags.

⇒ Recommend: **compact responsibility note in `ROSTER.md` that says which file owns which fact, and points.** No new columns in Phase 1.

---

## PART C — Three design-affecting facts found while drafting

**C1. ⚠️ `ROSTER.md`'s active list is MIRRORED INTO ROOT `CLAUDE.md`, which is auto-injected fleet-wide — and the plan's file list does not name it.**

Root `CLAUDE.md:26` carries `**Active agents (verified 2026-06-27 …)**: PROME, WALTER, SAM, …` and cites `PROME/ROSTER.md` as the source of truth. The plan's Phase 1 file list says *"root `AGENTS.md` or other mirrored boot-orientation surfaces, **if** they carry active lists."* **Root `CLAUDE.md` does carry one and is not named.**

Two consequences:
1. **Any Phase 1 taxonomy change creates a root-canon mirror obligation, and root `CLAUDE.md` edits are Will-gated.** That is a sequencing fact, not a formality — Phase 1 cannot be fully "descriptive and self-contained in PROME's lane."
2. **This mirror has a measured rot history**: the WP-W2 line read "still open" for **9 days** after its own closing commit, and OZK's revival lagged ROSTER until 7/25. The mirror is exactly the surface that rots when the roster changes.

⇒ Recommend Phase 1 explicitly include **root `CLAUDE.md:26` as a named, Will-gated mirror step**, and that `ROSTER.md` gain a pointer marking it as a known mirror so the next editor cannot miss it.

**C2. ✅ The "Production Review" nit is RESOLVED — my acceptance note was wrong to flag it as unverified.**

It is a real, DAEDALUS-owned cadence: `AGENTS/DAEDALUS/sweeps/PRODUCTION_REVIEW.md`, `upgrades/PRODUCTION_REVIEW_2026-07-22.md`, `FLEET_DIRECTORY.md` is regenerated at each one, and DAEDALUS deliberately wired `canon_check.py` to it. **The next Production Review is 8/5 — tomorrow — and DAEDALUS's STATUS lists it as open.** So the plan's service rule for the roster-health queue is grounded in a live cadence, and that cadence fires the day before the governance window opens. **No amendment needed; the item closes.**

**C3. DAEDALUS already has machine-registered cadence data** — `AGENTS/DAEDALUS/sweeps/REGISTRY.tsv`, cadence-checked at its boot (SPAWN PROTOCOL step 5) via `sweeps_due.py`. The plan's "Service Rules For Owner Queues" table can therefore be **registered into an existing mechanism** rather than living as prose in ROSTER. Worth routing to DAEDALUS at Phase 2 rather than PROME writing a parallel schedule.

---

## PART D — The pasteable ruling table (goes into `PROME/ROSTER.md` once Part B is ruled)

> **ROSTER RESPONSIBILITY MODEL — ruled 2026-08-0X by Will** *(plan: RAV roster-responsibility v4, accepted 8/4)*
>
> **Column ownership — put the fact in the owner file and POINT; do not restate.**
>
> | Fact | Owner file |
> |---|---|
> | Agent existence · human bucket · cadence posture | `PROME/ROSTER.md` *(this file)* |
> | Class / authority type · maturity level · next structural gap | `AGENTS/DAEDALUS/FLEET_MAP.tsv` → generated `FLEET_DIRECTORY.md` |
> | Routing / delivery status | `AGENTS/WALTER/REGISTRY.tsv` + routing table |
> | Synthesis-read requirement · brief schema/order invariants | `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` |
> | Will-facing priority / decision state | `PROME/WILL_QUEUE.md` · `GATES.tsv` · `DOCKET.tsv` · `BRIEF.md` |
> | Off-repo routine schedule / state | PROME if PROME-deployed; **domain owner** for state + alert lines |
>
> **Labels below are DESCRIPTIVE ONLY** — they do not change routing, boot priority, DAEDALUS grading, WALTER delivery, or NEXUS read obligations until an explicit later operational ruling. **`PROVISIONAL ACTIVE` is not a demotion** — it means the agent exists and should run, with proof criteria pending.
>
> **One owner OF RECORD per recurring responsibility** — one accountable owner for the reconciled figure, one artifact, one escalation path. **This does not forbid scoped overlap**; root canon mandates it (CORAL↔MARCO, AEOLUS↔CORAL) — reconcile to one figure, never silo.
>
> **Cadence and authority are separate fields only where they diverge** (TIER-2-with-authority, PROVISIONAL, EVENT-DRIVEN, SPECIAL). Where one label carries both, the omission is deliberate.
>
> ⚠️ **Mirror:** the active list here is mirrored into root `CLAUDE.md:26` (auto-injected fleet-wide, **Will-gated**). Any change to the roster taxonomy owes that mirror a matching edit — this pair has rotted before (WP-W2, 9 days).

---

## What this does NOT do

- Does **not** edit `ROSTER.md`, `_INDEX.md`, `_NETWORK.md`, or root `CLAUDE.md`. Nothing has moved.
- Does **not** make any label operational.
- Does **not** touch Phases 3-4 (HELD).
- Does **not** substitute for RAV's preflight — Part B is explicitly amendable by its addendum.

## Next actions after Will rules Part B

1. PROME packets RAV the **preflight go** (read-only), carrying Part B rulings + Part C as design-affecting facts it should test rather than rediscover.
2. RAV returns the preflight addendum → Part B amended if needed.
3. PROME applies **Phase 1** descriptive taxonomy to `ROSTER.md` / `_INDEX.md` / `_NETWORK.md`, with the root `CLAUDE.md:26` mirror step raised to Will separately.
4. Phase 2 goes to owner agents by task packet — DAEDALUS (incl. the C3 cadence registration), WALTER, NEXUS.
