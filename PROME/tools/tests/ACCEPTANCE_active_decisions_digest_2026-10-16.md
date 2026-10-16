# ACCEPTANCE — BOOT step 3: ACTIVE_DECISIONS read by DIGEST, whole rows only where actionable — 2026-10-16

**Written BEFORE the edit** (PROME, session 8fb641db, 15:15 ET by `date`). Will's session focus (15:08 ET): boot/closeout cost
reduction. Ideas-list row 2026-10-16 "Boot reads: drop ACTIVE_DECISIONS … from the whole-read list"; CATO's 10/16 plan (step 2
scope = entry points; this is the sitting's ONE process change under WQ-299 R1, WQ-445 unruled at write time). Class: PROCESS.

## Defect, in its own terms
`PROME/ACTIVE_DECISIONS.md` (23,812 B at HEAD 903dca0c3, 11 index rows) is a `whole` boot read (READS.tsv row `PROME:BOOT.md-3`).
Of its 11 rows, ONE carries a non-terminal state token this week (OZK/WAL SELL, `WILL_APPROVED` / `BROKER_PENDING`); the other ten are
closed or monitor-only rows kept for their STANDING GUARDS (the Rules section says guards never rotate). The boot therefore reads
~22 KB of guard prose every sitting to find ~1 KB of actionable state, and nothing mechanical reads the table at all — the gate
measures the file's size (`active_decisions_over_budget`, a "scripted-check revisit trigger") and checks GATES, not this index.
The trigger's own wording names the remedy: a scripted check of the index.

## Acceptance conditions (properties, not the symptom)
| # | Category | Condition |
|---|---|---|
| A1 | **Ordinary** | `python3 PROME/tools/active_decisions_digest.py` prints, for EVERY row of § Live Decision Index, one line: decision title · leading state token · the Next cell (bounded) · bytes · class ACTIONABLE or GUARD; a header with the source sha256 (short) and row count; a footer naming `--row <n>` for the whole row. ACTIONABLE = the leading state token is one of the Rules' non-terminal states (DRAFT PROPOSED WILL_APPROVED BROKER_PENDING ORDER_PLACED FILLED POSITION_UPDATED LOGGED DEFERRED); everything else is GUARD. `--row <n>` prints that row whole, byte-exact. |
| A2 | 🔴 **Overlap** | A row whose LEADING token is terminal (CLOSED, RE-BASED, MONITOR_ONLY) but whose State cell carries a non-terminal sub-state later in the text (the TRY-FIRE-004 row: CLOSED … WQ-360 LAPSED …; the Hormuz row: MONITOR_ONLY … FIRED …) is classed by the LEADING token AND the digest line shows the first 72 chars of the State cell so the reader sees the leading token in context; a row whose leading token is non-terminal is ACTIONABLE even when its text says "no fill on file". The test fixture carries both shapes. |
| A3 | **Wrong owner** | Only the table under `## Live Decision Index` is parsed; the Rules bullets, the header and the Next Maintenance section never produce a line; a second pipe table elsewhere in the file is ignored (fixture carries one). `scripts/read_cap_check.py`, `prome_gate.py` and GATES are untouched. |
| A4 | **Missing information** | A row with fewer than six cells, or a file with no `## Live Decision Index` heading, or an empty State cell ⇒ rc=1 and a line naming the row; never a silent skip, never a default class. `--check` is that mode (used by the gate later if adopted; not wired now). |
| A5 | **Concurrent activity** | N/A — a read-only tool with no state; one PROME session on one machine (MACHINE_LOCAL). |
| A6 | **Size** | On the live file the digest is under 3,000 B (`measure.py` on the captured output, recorded below). READS.tsv row `PROME/ACTIVE_DECISIONS.md` flips `whole` → `scoped` with the tool named, so `read_cap_check` stops metering it; `active_decisions_over_budget` can only read 0 afterwards (it keys on cap-bearing rows), which the gate's consistency rule (`0 ≤ over_budget`) accepts. |
| A7 | **Wiring (WIRED/OBSERVED)** | WIRED = BOOT.md step 3 names the digest as the read and "whole row only when ACTIONABLE or when the session will touch the row"; both `/boot` runner copies say the same (parity check); READS.tsv row flipped. OBSERVED = the next ordinary boot reads the digest, not the file, and its report names no lost obligation. Not claimable at this sitting. |

## Smallest reversible edit
New read-only tool + its test file; BOOT.md step 3 (one sentence replaced); boot SKILL.md line 2 (both copies, identical); READS.tsv one
row's mode + notes. CLOSEOUT's symmetry row for ACTIVE_DECISIONS is unchanged (the closeout WRITE is surgical already). Reversal =
`git revert` of one commit.

## Record (filled at implementation)
- IMPLEMENTED 15:2x ET: `PROME/tools/active_decisions_digest.py` (new) · `PROME/tools/tests/test_active_decisions_digest.py` (7 tests, `grep -c 'def test_'`; all pass under `.venv`) · BOOT.md step 3 · both `/boot` runner copies (parity `cmp` OK) · READS.tsv row flipped whole→scoped.
- A6 measured: digest on the live file 2,927 B (`measure.py`, 15:2x ET); `read_cap_check --require-manifest --charter-mode explicit` rc=0, reads=8 (was 9), active_decisions_over_budget=0. BOOT.md 30,043 → 30,480 B (its rotation was already owed; disclosed).
- TESTED: the author's seven. INDEPENDENTLY VERIFIED: pending one Opus read with its own counterexample (WQ-447: a gate-adjacent boot read is a difficult job, not a single-artifact cold read). Not claimable as verified at this sitting until that read returns.
- A7 OBSERVED: not claimable — the next ordinary boot.
