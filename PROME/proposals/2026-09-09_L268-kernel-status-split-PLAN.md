# PLAN — DOCKET L268: `KERNEL/IMPLEMENTATION_STATUS.md` chronology → archive; leave a records-derived status file

**Author:** PROME (custodian), 2026-09-09 ~21:4x ET (clock-corrected — first written ~22:1x from narrative, error owned), on Will's word *"go ahead with B and C, then A"* (21:17). **Class:** archival split ⇒ ONE blind read on this PLAN before any edit, ONE on the RESULT (WQ-178 read budget). **Origin:** WQ-171 ② cold read (reader ❌31: a header-only edit on 9/3 left the body contradicting it) + Codex rec 7. **Custody perimeter:** the status doc + two README pointer lines only — NO event, receipt, view, policy, schema or tool is touched.

## The move (mechanical)
- **Source:** `git show HEAD:KERNEL/IMPLEMENTATION_STATUS.md` (HEAD = `0ab1e8e51` at plan time). **Moved block = physical lines 13–246 inclusive** (from `## Session entry` through the end of `## Verification record`), **verbatim**, to `PROME/archive/KERNEL_IMPLEMENTATION_CHRONOLOGY_FROZEN_2026-09-09.md`, under a banner that states: 🧊 FROZEN 2026-09-09 · moved verbatim from `KERNEL/IMPLEMENTATION_STATUS.md` lines 13–246 at `0ab1e8e51` (DOCKET L268) · HISTORY not status — build chronology dated 2026-08-25 → 2026-08-28, whose 9/3 header called it 'through 2026-08-26'; its present-tense lines were falsified by Sitting 1 (2026-08-27) and declared HISTORY on 2026-09-03 · block crc32 = `PROME/tools/measure.py` over the moved bytes (no trailing newline) · "verify by recomputing, never from this banner".
- **Header lines 1–11 (title · Owner · Updated · Latest operator ruling · Current mode · Canonical use) are REWRITTEN records-derived — every field, not two** (the 9/3 header survives at `git show 0ab1e8e51:KERNEL/IMPLEMENTATION_STATUS.md` and is NOT part of the archived block). **Kept verbatim:** lines 247–end (`## Stop conditions`).
- **README pointer fixes (two lines, same commit):** `KERNEL/README.md` L11 *"Live implementation plan and completed work"* → *"Records-derived implementation status (the build chronology is frozen at `PROME/archive/KERNEL_IMPLEMENTATION_CHRONOLOGY_FROZEN_2026-09-09.md`)"*; L108 *"The exact next increment and remaining Gate B sequence are canonical in `IMPLEMENTATION_STATUS.md`."* → *"Gate state, the record set on disk and the open legs are canonical in `IMPLEMENTATION_STATUS.md`; the Gate B increment sequence is history, frozen at the archive it names."* `KERNEL/SPEC.md` L13 *"Current progress and the next implementation increment are canonical in `KERNEL/IMPLEMENTATION_STATUS.md`."* → *"Gate state and the open legs are canonical in `KERNEL/IMPLEMENTATION_STATUS.md`; the build chronology and its increment sequence are frozen at `PROME/archive/KERNEL_IMPLEMENTATION_CHRONOLOGY_FROZEN_2026-09-09.md`."* (three pointer files in one commit: STATUS · README · SPEC).

## Invariants the result read checks
1. Archive block bytes == source lines 13–246 (crc32 recomputed by `measure.py`, stated in the archive header; the reader recomputes).
2. `git status --short KERNEL/` after the edit shows ONLY `KERNEL/IMPLEMENTATION_STATUS.md`, `KERNEL/README.md` and `KERNEL/SPEC.md`; `ls PROME/archive/KERNEL_IMPLEMENTATION_CHRONOLOGY_FROZEN_2026-09-09.md` exists and is in the same commit.
3. Every pointer to `IMPLEMENTATION_STATUS.md` in `README.md`/`SPEC.md` names something the new file actually carries.
4. The "independent adversarial review of the live interface — OWED" leg survives, worded true (the REMEDIATION doc's State line is the source).
5. Every present-tense claim in the new file names the record it is derived from; the two chronology claims FALSE since Sitting 1 (2026-08-27) (*"no activation document for the real repository exists"*, *"no live command, result, view, or shadow operation has occurred"*) are named as refuted in the header, not silently dropped.
6. `## Stop conditions` verbatim.
7. Test count stated = measured tonight: **220 OK** (`python3 -m unittest discover -s KERNEL/tests -p 'test*.py'`, 2026-09-09 ~21:3x ET; was 207 at the 8/26 freeze).
8. Record counts stated = `ls` tonight: accepted events **19** (2 in `2026/08`, 17 in `2026/09`); rejected receipts **0**; views 4; transcripts 4 (+ `c7_staged_submissions/`).

## Proposed new `KERNEL/IMPLEMENTATION_STATUS.md` (full text)

```markdown
# Kernel v1 Implementation Status

**Owner:** PROME (custodian and builder — never the reviewer of its own build)

**Updated:** 2026-09-09 (DOCKET L268 — WQ-171 ② follow-up + Codex rec 7: the build chronology (increments dated 2026-08-25 → 2026-08-28; its 9/3 header called it 'through 2026-08-26') — increments table, implemented-behaviour list, limitations, the pre-review "next action", the Gate B sequence, the superseded gate table and the 8/26 verification record — moved VERBATIM to `PROME/archive/KERNEL_IMPLEMENTATION_CHRONOLOGY_FROZEN_2026-09-09.md` (block crc32 in that file's header; the last combined version = `git show 0ab1e8e51:KERNEL/IMPLEMENTATION_STATUS.md`). What remains here is derived from the records each line names. Two chronology sentences have been FALSE since Sitting 1 (2026-08-27) — still carried on 9/3 as declared HISTORY — and are not carried here: *"no activation document for the real repository exists"* and *"no live command, result, view, or shadow operation has occurred"* — the sitting records below refute both.) Prior: 2026-09-03 (WQ-171 ②: the three status lines re-derived; the body declared HISTORY). Prior: 2026-08-26.

**Latest operator ruling:** Will 2026-09-02 10:57 ET (WQ-155, *"Approve 155 with your recs"*, record `GATE_C_C8_RULING_2026-09-02.md`): C8 after Sitting 2 = **CONTINUE** · WQ-149 carrier confirmed = F · scoring vocabulary = three-outcome (a), SPEC-GATED pending the data-and-score contract (DOCKET L247 — spec DRAFT landed 2026-09-09, `KERNEL/OUTCOME_VECTOR_PROJECTION_SPEC_DRAFT.md`, review requested). Owed: root carve-out ④ wording (WQ-150). *Prior (2026-08-26): Will authorized the bounded live-interface remediation in-session ("approved - go ahead with the build"); its independent adversarial review remains OWED (`GATE_C_LIVE_INTERFACE_REMEDIATION.md` State line) — the RED (Sitting 1) and DAEDALUS (Sitting 2) C8 reviews are sitting-closeout reviews, a different object.*

**Current mode:** GATE C — BOUNDED SHADOW PILOT SITTINGS (Will-activated per sitting; NO ACTIVATION CURRENTLY LIVE — every activation document named below carries `revoked_at`) — NON-AUTHORITATIVE

**Canonical use:** This file is the records-derived status of the Kernel implementation — gate state, the record set on disk, the open legs, the verification entry. It changes when a record lands (an activation, a sitting closeout, a ruling) or an open leg closes. It carries no build narrative: the chronology is frozen at the archive above; the proposal (`PROME/proposals/2026-08-25_kernel-v1-spec-DRAFT.md`) preserves design and ruling history; the audit records preserve findings.

## Session entry

Read, in order: 1. `KERNEL/README.md` (authority boundary, verification entry point) · 2. `KERNEL/SPEC.md` (implemented-contract pointer) · 3. this file · 4. `PROME/proposals/2026-08-25_kernel-v1-spec-DRAFT.md` when changing behaviour · 5. `KERNEL/GATE_C_C7_RUNBOOK.md` before any sitting.

Before editing, verify a clean `master`, synchronize with `origin/master`, and run `python3 -m unittest discover -s KERNEL/tests -p 'test*.py' -v`. Baseline at this update: **220 tests pass** (2026-09-09; 207 at the 8/26 freeze — the delta is the 8/28 projection-exclusions suite and the sitting-2 additions).

## Authorization boundary (records-derived)

- **Standing, no activation live:** fixture-only work — schemas, policies, registries, validation, replay, rendering, tests; synthetic records; read-only Git-backed native verification against synthetic fixtures. Nothing under `KERNEL/shadow/`, `KERNEL/audit/commands/` or `KERNEL/views/` is written.
- **Under a LIVE, Will-authorized, time-windowed activation document only** (the class every record in § Gate state instantiates): that activation's pinned actor set and command inventory; accepted events and rejected receipts as additions-only; the four registered views by `live_shadow.py --apply`; the governance records the runbook instructs. Custody = PROME per root `CLAUDE.md` § Gate C custody; carve-out ④ for domain desks is INACTIVE outside a live window.
- **Never — Gate D is OUT OF SCOPE:** canonical authority or an authority switch; a submission-directory scan; weakening fail-closed behaviour to make anything pass.

## Gate state (records-derived)

| Gate | State | Records |
|---|---|---|
| A — specification approval | PASSED | approved contract `9bbf9c041` |
| B — fixture implementation | PASSED / CLOSED 2026-08-26 | `CHECKPOINT_12_ACCEPTANCE_REMEDIATION.md`; Will's closure 8/26 |
| C — live shadow activation | **TWO SITTINGS EXECUTED, C8 = CONTINUE at both, NO ACTIVATION LIVE.** Sitting 1, 2026-08-27: `GATE_C_C7_ACTIVATION_2026-08-27.json` + `GATE_C_INCREMENT2_ACTIVATION_{A,C}_2026-08-27.json`; ruling `GATE_C_C8_RULING_2026-08-27.md`. Sitting 2, 2026-09-02: `GATE_C_SITTING2_ACTIVATION_{A..F}_2026-09-02.json` (LIVE-2026-0007…0012); packet `GATE_C_C8_CLOSEOUT_PACKET_2026-09-02.md`; ruling `GATE_C_C8_RULING_2026-09-02.md`. All activations revoked. **Still OWED: the independent adversarial review of the live interface** (`GATE_C_LIVE_INTERFACE_REMEDIATION.md` State line; brief in its § Independent review brief; reviewer ≠ builder). | as named |
| D — authority switch | OUT OF SCOPE | — |

## Records on disk (counts at this update — `ls` reproduces them)

- **Accepted events: 19** — `KERNEL/shadow/events/2026/08/` (2, Sitting 1) + `KERNEL/shadow/events/2026/09/` (17, Sitting 2). Additions-only; any modification is a blocking integrity failure.
- **Rejected receipts: 0** — the registered path `KERNEL/audit/commands/` (root `CLAUDE.md` § Gate C custody) has never been created because no rejection has ever been written; the directory's absence IS the zero (`ls KERNEL/audit` → no such directory).
- **Registered views: 4** at `KERNEL/views/`, renderer `kernel.renderer.2` since Sitting 2. `CALIBRATION.tsv` row `Q-019306a1-4c00-7000-8000-00000000006a` (MIDAS-06) is EXCLUDED `OUTCOME_VOCABULARY_MISMATCH` by design until DOCKET L247's spec passes review and the build re-renders under a ruled activation.
- **Policies:** `KERNEL/policies/` — actors · capability-grants · custody-policy · projection-exclusions (+ dated drafts).
- **Transcripts:** `KERNEL/rehearsals/` — 8/26 live-interface rehearsal · 8/27 pilot (RECOVERED) · 8/27 increment-2 · 9/2 sitting-2; `c7_staged_submissions/`.
- **Sitting governance:** the activation JSONs and packets above, `GATE_C_SITTING2_PREP_2026-08-27.md`, the C8 closeout packets and rulings (8/27, 9/2), `GATE_C_READINESS_PLAN.md` (row advanced to RULED at the 9/2 ruling).

## Open legs

1. Independent adversarial review of the live interface — OWED since 2026-08-26; reviewer ≠ builder; brief = `GATE_C_LIVE_INTERFACE_REMEDIATION.md` § Independent review brief.
2. DOCKET L247 — three-outcome projection vocabulary: spec DRAFT landed 2026-09-09 → review (DAEDALUS, RED alternate) → build → first live consumer MIDAS-06 at the next ruled re-render, never by hand.
3. WQ-150 — root carve-out ④ wording.
4. Schema-v2 multi-outcome forecast family — the follow-on the L247 spec registers (Gate-A-class amendment; not this pass).

## Verification entry

```bash
python3 -m unittest discover -s KERNEL/tests -p 'test*.py'     # 220 OK at 2026-09-09
python3 -m compileall -q KERNEL/tools KERNEL/tests
```

The live-interface commands and the audit / view-reproduction perimeter → `README.md` § Verification and `GATE_C_C7_RUNBOOK.md`. The 8/26 verification record (207-test baseline, fixture-CLI transcript) is in the frozen chronology.

## Stop conditions

Stop and return to Will before proceeding if an implementation step would require:

- a real native record;
- a new governed object or forecast family;
- substantive interpretation by PROME;
- a live agent-directory scan or write;
- a shared/root Git ownership change;
- a messaging, obligation, scheduling, or hosted-runtime feature;
- weakening fail-closed behavior to make a fixture pass.
```

## Declared residue block
**Plan read (coldreader, 2026-09-09 21:4x ET): DO-NOT-EXECUTE, 5 ❌ + 5 ⚠️. All five ❌ FIXED above** (supersession date 9/2 → Sitting 1 2026-08-27 · `KERNEL/audit/commands/` named as never-created, not as a resolving path · the header rewrite declared for all six fields · SPEC.md L13 added to the pointer fixes · archive renamed to its freeze date with the content range stated); ⚠️6 (a line number) fixed as a one-token typo. **⚠️ declared, not fixed (WQ-178):** ⚠️7 the 220-test count names no transcript — the command and its output are recorded in § Result below, no separate record exists · ⚠️8 the gate table names nine activation JSONs; a tenth dated file (`GATE_C_INCREMENT2_ACTIVATION_2026-08-27.json`, the combined increment-2 document) is unnamed there, README says 'ten' · ⚠️9 invariant 2 cannot see the archive — the result read is told to `ls` it · ⚠️10 'MIDAS-06 EXCLUDED' (a calibration ROW state) sits beside README's 'RESOLVED + VERIFIED' (a QUESTION state) without saying they are different objects.

## Result
Executed 2026-09-09 21:5x ET. `KERNEL/IMPLEMENTATION_STATUS.md` = the fenced text above (byte-for-byte, extracted programmatically). Archive `PROME/archive/KERNEL_IMPLEMENTATION_CHRONOLOGY_FROZEN_2026-09-09.md` written; block crc32 3472015315 (zlib in-process; measure.py recompute printed in the session log beside it). README L11 + L108 and SPEC L13 pointers edited as planned. Test-count record (⚠️7): `python3 -m unittest discover -s KERNEL/tests -p 'test*.py'` → `Ran 220 tests … OK` at ~21:3x ET this session. Result read → coldreader, findings appended below.

**Result read (coldreader, 2026-09-09 21:5x ET): FIX — invariants 1 · 3 · 4 · 5 · 6 · 8 VERIFIED (diff empty, 234 lines, measure.py crc32-no-final-nl 3472015315 == banner; pointers resolve; OWED leg true; refuted claims named; Stop conditions verbatim; counts reproduce, `ls KERNEL/audit` → no such directory), 7 UNCHECKABLE (declared ⚠️7), **2 FAILED on timing/scope only** — the read ran pre-commit (the archive was untracked) and the fourth dirty KERNEL path was the L247 spec draft, a different deliverable in the same lane; both satisfied by the commit that carries this line (`git log -1 -- PROME/archive/KERNEL_IMPLEMENTATION_CHRONOLOGY_FROZEN_2026-09-09.md`). Invariant 2 as written should have excepted the L247 file — plan defect, owned. **⚠️ from the result read, declared not fixed:** the nine-vs-ten activation count (⚠️8 carried; README L5 says ten, the gate table names nine — the combined `GATE_C_INCREMENT2_ACTIVATION_2026-08-27.json` is the tenth) · `renderer kernel.renderer.2 since Sitting 2` names no record (the record = the views' own `renderer_version` metadata line + the 8/28 chronology row) · `spec DRAFT landed` read as committed — true at this commit · **`KERNEL/README.md` L5 is a corrupted run-on sentence (`…remain separately gated in [GATE_C_READINESS_PLAN.md](…).rately gated in`), pre-existing and out of this split's scope — carried to the next KERNEL doc pass, SCRATCH carry.** One-word fix applied: `(+ dated drafts)` → `(+ their drafts)`. File closed for the session.
