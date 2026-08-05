# Roster Migration — PHASE 0 RULING TABLE

**Status:** ✅ **RULED 2026-08-04 (session 4), Will in-session. Phase 0 is CLOSED.**
**Drafted by:** PROME · **Basis:** RAV roster-responsibility plan **v4** (Will-ACCEPTED 8/4 eve)
**Executor contract (Will-ruled 8/4 eve):** Phase 0 = PROME drafts, Will rules. Staged execution; **each named agent executes in its OWN domain.**
**This artifact is the single reference for Phase 0.** DAEDALUS, WALTER, NEXUS and RAV cite this file rather than reconstructing the rulings from packets.

⚠️ **Amendable by RAV's preflight addendum.** The plan orders the targeted preflight before Phase 1 edits, and its output explicitly includes *"one list of plan amendments required before edit."* These rulings are **ruled, not frozen** — if the preflight surfaces a fact that breaks one, it returns to Will rather than being worked around.

---

## PART A — Ruled 8/4 eve (the plan's six "Will Decisions Needed")

| # | Decision | Ruling |
|---|---|---|
| 1 | Phase 1 labels are **descriptive only** — no change to routing, boot priority, DAEDALUS grading, WALTER delivery, or NEXUS read obligations until an explicit later operational ruling | ✅ **ACCEPTED as written** |
| 2 | **Column ownership split by source of truth** — PROME: human bucket/cadence · DAEDALUS: class/maturity/structural gaps · WALTER: routing/delivery · NEXUS: brief schema + synthesis-read obligations | ✅ **ACCEPTED as written** |
| 3 | **`PROVISIONAL ACTIVE` is not a demotion** — the agent exists and should run; proof criteria are pending | ✅ **ACCEPTED as written** |
| 4 | **Correction propagation is publisher-owned** — WALTER owns BOARD/signal correction linkage; the publishing agent owns downstream propagation of its own corrected figure/tool/state | ✅ **ACCEPTED as codification** of existing root-canon practice (root step 1c) |
| 5 | **Scheduled/off-repo routines need owner state** — routine reads owner-maintained state, carries stale-state alarms, never resolves prediction rows unless explicitly authorized | ✅ **ACCEPTED as codification** of the BRENT routine architecture already in-repo (`AGENTS/BRENT/SCHEDULED_RUNS.md`) |
| 6 | **No new organizing agent yet** — change the ownership map first | ✅ **ACCEPTED as written** |

**Binding on everything below:** staged execution, each named agent edits its OWN domain; RAV preflight + Phase 0 + Phase 1 authorized for **8/6-8/9**; **Phases 3-4 HELD** for a separate ruling after the preflight addendum.

---

## PART B — Ruled 2026-08-04 session 4

### ✅ B1 — Bucket separation: YES, **scoped to the ACTIVE bucket only**

> **Will:** *"Yes, but scope Phase 1 to splitting the misleading ACTIVE bucket. Do not rebuild the whole taxonomy across all roster categories."*

**Target:** the current `## ACTIVE — persistent domain owners (30)` header/bucket, which mixes **domain owners · organizing/service agents · review lanes · event-driven specialists · provisional/newborn agents** under a header whose own words claim "persistent domain owners."

**Explicitly OUT of Phase 1 scope:** TIER-2, DORMANT, RETIRED, ARCHIVE SOURCES, SPECIAL, TOOL-CLASS INSTRUMENTS, spinout provenance, coverage-notes, transmission chain. Already separated; **not to be restructured.**

### ✅ B2 — Cadence vs authority: separate **only where they diverge or can mislead**

> **Will:** *"Do not blanket-add two fields to every row."*

**Apply explicitly to:**
- Tier-2 agents with **real authority** in-lane
- **SPECIAL / meta / review** agents (DAEDALUS, YEYOU, RAV)
- **`PROVISIONAL ACTIVE`** rows
- **`EVENT-DRIVEN SPECIALIST`** rows
- **any row where routing cadence differs from decision authority**

Where a single label carries both truthfully, **leave it single** — the Part D rule makes that omission legibly deliberate rather than missing.

### ✅ B3 — "one owner **of record**" (wording amended from "exactly one owner")

> **Will:** *"Standing canon's scoped overlap remains legal."*

**Ruled wording, to be used verbatim downstream:**

> **Every recurring responsibility or shared figure needs one owner of record, one accountable artifact, and one escalation path; overlap is allowed where agents reconcile to the owner-of-record figure/state rather than siloing.**

**Why the amendment was needed:** a literal "exactly one owner" would have contradicted standing root canon — *"Scoped overlaps are intentional — reconcile shared metrics to one figure, don't silo"* (CORAL↔MARCO, AEOLUS↔CORAL) — and would have pushed agents to silo precisely where canon says reconcile. **Phase 1 taxonomy is written against the ruled wording, not the plan's original.**

### ✅ B4 — Compact table, **no new columns**

> **Will:** *"Do not add new class/maturity/routing columns to ROSTER in Phase 1 unless a real consumer needs machine readability. Avoid duplicating FLEET_MAP/FLEET_DIRECTORY/WALTER registry state into another live roster surface."*

The machine-readable consumers already exist and are owned elsewhere: `AGENTS/DAEDALUS/FLEET_MAP.tsv` → generated `FLEET_DIRECTORY.md`, and `AGENTS/WALTER/REGISTRY.tsv`. ROSTER gets a **compact pointer note**, not copies.

---

## PART C — Design-affecting facts

### ⚠️ C1 — ACCEPTED: root `CLAUDE.md` mirror is a **named, Will-gated Phase 1 step**

> **Will:** *"Name root `CLAUDE.md` active-list mirror as an explicit Will-gated Phase 1 step. PROME may packet the needed mirror edit, but should not silently move root canon/auto-injected boot surfaces."*

`ROSTER.md`'s active list is mirrored at **root `CLAUDE.md:26`** (`**Active agents (verified 2026-06-27 …)**: PROME, WALTER, SAM, …`), which is **auto-injected fleet-wide** and cites `PROME/ROSTER.md` as its source of truth. The plan's Phase 1 file list said *"root `AGENTS.md` or other mirrored boot-orientation surfaces, **if** they carry active lists"* — root `CLAUDE.md` does, and was not named.

⇒ **Phase 1 is therefore NOT fully self-contained in PROME's lane.** The mirror edit is **drafted by PROME and ruled by Will, never applied silently.**

**Rot history on this exact pair** (why it earns a named step, not a footnote): the WP-W2 line read "still open" for **9 days** after its own closing commit `37ee2748e`; OZK's dormant→ACTIVE revival lagged ROSTER until 7/25.

### ✅ C2 — CLOSED: the "Production Review" nit was PROME's error, not a plan defect

PROME's acceptance packet flagged *"Production Review cadence name unverified in-repo."* **That was wrong.** It is a real DAEDALUS-owned cadence: `AGENTS/DAEDALUS/sweeps/PRODUCTION_REVIEW.md`, `upgrades/PRODUCTION_REVIEW_2026-07-22.md`, `FLEET_DIRECTORY.md` regenerated at each one, `canon_check.py` deliberately wired to it. **Next: 8/5**, open on DAEDALUS's STATUS. **Will accepted the correction; no amendment.**

### 🔁 C3 — Route to DAEDALUS at Phase 2, do not re-implement

DAEDALUS already carries **machine-registered cadence data** — `AGENTS/DAEDALUS/sweeps/REGISTRY.tsv`, cadence-checked at its boot via `sweeps_due.py` (SPAWN PROTOCOL step 5). The plan's "Service Rules For Owner Queues" should be **registered into that existing mechanism**, not written as parallel prose in ROSTER. PROME does not build a competing schedule.

---

## PART D — Pasteable block for `PROME/ROSTER.md`

> ### ROSTER RESPONSIBILITY MODEL — ruled 2026-08-04 by Will
> *(source: RAV roster-responsibility plan v4, accepted 8/4; rulings: `PROME/proposals/2026-08-04_roster-phase0-ruling-table-RULED.md`)*
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
> | Off-repo routine schedule / state | PROME if PROME-deployed; **domain owner** for state + registered alert lines |
>
> **Ownership rule:** every recurring responsibility or shared figure needs **one owner of record, one accountable artifact, and one escalation path**; **overlap is allowed** where agents reconcile to the owner-of-record figure/state rather than siloing.
>
> **Labels are DESCRIPTIVE ONLY** — they do not change routing, boot priority, DAEDALUS grading, WALTER delivery, or NEXUS read obligations until an explicit later operational ruling. **`PROVISIONAL ACTIVE` is not a demotion** — the agent exists and should run; proof criteria are pending.
>
> **Cadence and authority are separate fields only where they diverge or could mislead** — Tier-2-with-real-authority, SPECIAL/meta/review, `PROVISIONAL ACTIVE`, `EVENT-DRIVEN SPECIALIST`, and any row where routing cadence differs from decision authority. Elsewhere one label carries both, **deliberately**.
>
> ⚠️ **MIRROR — Will-gated:** this file's active list is mirrored into root `CLAUDE.md:26`, which is **auto-injected fleet-wide**. Any roster-taxonomy change owes that mirror a matching edit, **drafted by PROME and ruled by Will — never applied silently.** This pair has rotted before (WP-W2 read "still open" 9 days past its own closing commit; OZK lagged to 7/25).

---

## Phase 1 scope, fixed by these rulings

**IN:** split `## ACTIVE — persistent domain owners (30)` into truthful buckets · add the Part D block · apply the B2 cadence/authority split on qualifying rows only · mark provisional and event-driven rows · align `AGENTS/_INDEX.md` + `AGENTS/_NETWORK.md` (governance/review topology marked separate from market transmission).

**OUT:** every other ROSTER section · new columns · any operational effect · Phases 3-4 · silent root-canon edits.

## Next actions

1. ✅ **DONE 8/4** — PROME packeted RAV the preflight go carrying these rulings + C1 → `AGENTS/RAV/inbox/2026-08-04_from-PROME_preflight-GO-phase0-RULED.md`.
2. RAV returns the preflight addendum → amendments back to Will if any ruling breaks.
3. PROME applies Phase 1 in-scope edits; **root `CLAUDE.md:26` mirror drafted and raised to Will separately.**
4. Phase 2 → owner agents by task packet (DAEDALUS incl. C3, WALTER, NEXUS).
