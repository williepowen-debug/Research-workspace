# BROCK — charter provenance

Incident history and reasons moved VERBATIM out of `CLAUDE.md` on 2026-10-30 (DAEDALUS profile refresh item 10: charter was 31,274 B = 96% of the read budget). Not boot-read. Every rule stayed in the charter; only the history moved. Earlier charter history: `git log -p -- AGENTS/BROCK/CLAUDE.md`.

## § 11b — 11b (closeout step 11b, full text as of 2026-10-30)

- **11b. Memory-index check [ALWAYS *if you wrote or edited a memory this session*, before step 12]:** `python3 "$(git rev-parse --show-toplevel)/scripts/memory_index_check.py" --strict --slug <the memory you wrote>` (repeat `--slug` per memory). **Exit 1 = YOUR index row names a memory git will not ship — commit the file (or fix the ignore rule for the GITIGNORED class) and re-run before committing.** ⚠️ **Use the `--slug` form, NOT bare `--strict`.** Bare `--strict` fails on the WHOLE index, which is a fleet/CI gate — at an agent closeout it will **block you on another agent's orphan that carve-out ③ forbids you to commit.** BROCK hit exactly that within an hour of shipping `--strict`: 5 orphans from two other live sessions failed its own closeout on files it was excluded from touching. **A gate that fails on something you cannot fix trains you to bypass the gate** — which is the same inertia that left the always-exit-0 version unused. The full index is still printed either way; `--slug` only narrows what may FAIL the run. ⚠️ **Why this is mandatory rather than advisory:** `MEMORY.md` is a SHARED file every agent touches, so *your* index row rides out on whoever commits next, while your memory FILE needs a deliberate `git add` that no other rule requires. The index reaches origin and the content does not — and on the other machine `MEMORY.md`, which loads at every boot, then advertises a memory whose file is absent. **That is worse than the memory never existing, because the index makes the gap look covered.** *(Installed 2026-07-27 after n=6 orphaned memories from 4 agents in one day. The detector already existed and was correct every time — but it always exited 0 and **nothing invoked it**. `--strict` + this line are the two halves of that fix. Do not "simplify" this to the non-strict form: the whole failure was a detector that could not fail.)* ⚠️ **`orphan_check.sh` will NOT cover you here** — it classifies by PATH, so everything under `memory/auto/` reads `[not yours]` regardless of who authored it. BROCK took that label at face value about a memory it had written itself, twice in one session (LESSONS #23-adjacent).

## § 6 — Closeout step 6 adoption note

*(Adopted 2026-10-02 from CREED; the retired rule was "≤250 lines, 280 trigger, SCRATCH-split", which could not fire: STATUS reached 90% of budget at 136 lines. Pre-split bytes: `archive/STATUS_PRESPLIT_2026-10-02.md`.)*

## § Signal — Signal Protocol correction note

*(Corrected 2026-09-03 on DAEDALUS's fleet census — this line had instructed direct SIGNAL delivery, which contradicts root `CLAUDE.md` §Direct Messaging v1 "never route signals around WALTER" and `MESSAGING/CROSS_SESSION_MESSAGING.md` §2 rule 4. Root canon wins. Residue of the 2026-06-30 HERMES-retirement template, propagated to ~20 desks; 10 still carried it at the census.)*

## § Boot-5 — Boot step 5 board_log size note

(2026-10-02: 112,887 B, and growing every session; this charter used to quote 89,476 B, which had gone stale)

## § Boot-3 — Boot step 3 BANK_BDC_MATRIX note

*(BANK_BDC_MATRIX: **decision CLOSED — FROZEN 2026-07-04**, banner in file; the old "owner to confirm" wording was stale by two months and presented a settled call as open — corrected 2026-09-03, LESSONS #27. Invocation cwd-proofed 2026-07-01.)*

## § Exit-1 — EXIT §1 WQ-106 why bullet

> - **Why:** my own 8/28 base-rate memo (`domain/sources/2026-08-28_SESSION_CATCHUP_ADJUDICATIONS.md` §1③) measured `<260` closing **exactly once in three years (n=787, 259 on 2025-01-22), longest run 1 session, 3-consecutive zero times** — a kill that was never reachable in its own sample. **A label was corrected on Will's word; no threshold was moved.**

## § Exit-4 — EXIT §4 template lines (expired)

- Q2 2026 earnings = next major resolution event (~late April/May)
- If no new stress signal by Jun 2026, reassess thesis freshness

## § Outbox-row — Doc Ownership outbox row

| **outbox/** | Cross-agent signals (one file per signal). Acute/threshold/resolution/insight only — see Outbox Protocol + messaging-overhaul caveat. | Self-notes; routine STATUS-only updates. |

