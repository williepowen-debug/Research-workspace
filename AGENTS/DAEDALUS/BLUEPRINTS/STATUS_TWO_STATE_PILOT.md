# STATUS TWO-STATE — pilot spec (WATT · HENRY · CARL, 2026-08-08 → 2026-08-22)

**Owner:** DAEDALUS · **Created:** 2026-08-07 · **Status:** PILOT CONFIRMED (Will, in-session, forum slate S6).
**Provenance:** `FORUM/2026-08-07_system-review/06_proposals/02_DAEDALUS_proposal-set.md` §P3 · `/04_DAEDALUS_amendments.md` §4 (the joint-pair amendment and the two-jobs caveat are NEXUS's, adopted) · `02_repair-burden/08_NEXUS_canon-mass-reply.md` (the 36.6% natural experiment).
**Text mode:** STRICT (`BLUEPRINTS/STRICT_TEXT.md`).
**⚠️ FLEET ROLLOUT IS A SEPARATE WILL RULING, GATED ON THE PILOT GRADE. This file governs three agents for two weeks.**

## The rule

`STATUS.md` is the one major surface exempt from the two-state discipline root canon imposes on every workbook ledger and trade surface (FROZEN, or LIVE with a bounded current block). This pilot removes the exemption for three agents.

**LIVE `STATUS.md` carries current state only. Superseded content rotates to a dated archive file. The archive is never deleted and always greppable.**

## THE CAP — 60 KB (61,440 bytes) on the STATUS + brief PAIR

**Measure:** `wc -c AGENTS/<X>/STATUS.md AGENTS/<X>/NEXUS_BRIEF.md` — the total. Advisory band at **48 KB (80%)**, matching the soft/hard tier `check_memory_length.sh` already uses.

**Bytes, not lines** (PAT-086). The exemplar is in this pilot: **CARL's first six lines are 23,885 bytes — 17% of the file in 2% of the lines.** Any line-count cap reads that as nothing.

**The pair, not STATUS alone** (NEXUS). Capping STATUS alone relocates the narrative into the brief, which is already happening: **SAM's brief is 39,809 bytes against a 36,377-byte STATUS — 109%, a second copy rather than a summary** — and NEXUS read it as exemplary on 2026-08-07 because no instrument measures artifact length. This fleet's characteristic failure is not that fixes fail; it is that the defect moves to the new surface.

**Derivation of 60 KB, stated so a grader can attack it:**
1. **Livable today.** 12 of 30 ACTIVE agents are already under 60 KB with no changes, including two L4s (RED 49,015 · HAWK 44,833) and two L3s (OSPREY 32,520 · MIDAS 32,208). The cap asks nobody to do something no functioning agent does.
2. **Binding.** The ACTIVE-agent median pair is ~68 KB, so the cap binds on the majority. A cap above the median changes nothing.
3. **Sufficient for outside readers.** NEXUS runs full cross-agent re-anchors off 592,484 bytes of brief covering 1,614,581 bytes of STATUS — **36.6%** — and its own instrumented quality metric (`brief-gap`) has fired once in 30 events, on the one agent that is brief-less by design.
4. **Real on the tail.** CARL −64%, HENRY −34%, WATT −11%.
5. **Boot arithmetic.** 60 KB ≈ 15K tokens. With root canon (27,838 bytes) and an agent's own instructions, boot lands ≈26-33K tokens against a measured median of ~42K today.

**What 60 KB is NOT derived from:** any judgment about how much state an agent *should* have. It is an outcome bound. An agent that cannot meet it and says why has produced a pilot result, not a failure.

## THE LIVE BLOCK — what stays

| Section | Content |
|---|---|
| Header | Agent · `Last updated: YYYY-MM-DD` · pair bytes at last closeout |
| **CURRENT STATE** | Convergence matrix, live reads, active thresholds, open predictions — each dated and sourced |
| **OPEN ITEMS** | What is owed, by whom, by when |
| **BOTTOM LINE** | 2-4 sentences (unchanged — existing per-agent placement convention stands) |
| **ARCHIVE POINTER** | One line naming the archive path |

## ROTATION MECHANICS

1. Identify superseded content by class (below).
2. **Append it VERBATIM** to `AGENTS/<X>/status_archive/STATUS_ARCHIVE_<YYYY-MM>.md` (monthly file — fewer files, still greppable). This directory is NEW and is **not** `archive/`, which is the destination for the root-canon >60-day research-retirement rule.
3. Delete the rotated text from `STATUS.md`.
4. Add the one-line archive pointer to the LIVE block.
5. `git add` the archive file; commit `STATUS.md` and the archive **in one path-scoped commit**, so the move is one atomic diff a reader can follow.

> **⚠️ Do NOT rotate by `git mv STATUS.md status_archive/…` and writing a fresh STATUS.md.** That variant restarts `STATUS.md`'s git history, and `ledger_staleness.py` falls back to git-commit time when a content-vintage token is absent — so a rotated file would read as zero days old (`finding_hygiene_commit_rearms_the_staleness_lie`). Keep `STATUS.md` in place; move the content, not the file.

### The three content classes — measured in this pilot, they are not the same shape

My P3 assumed one mass (session narrative). Measurement on 2026-08-07 says three, and the pilot is stronger for containing all three:

| Class | What it is | Pilot instance |
|---|---|---|
| **A — dated session sections** | Superseded per-session narrative, often already self-labelled | **HENRY** — 19,305 bytes (32%) at lines 8-63; two of the three sections already read `GRADED / SUPERSEDED` |
| **B — appended header block** | A masthead that accreted retellings (`finding_status_spine_staleness_under_appended_top`) | **CARL** — 23,885 bytes in six lines |
| **C — dated state rows past their own review date** | Dashboard/matrix rows carrying a read nobody has refreshed | **CARL** — a 63,784-byte signal dashboard. Rotate only rows whose own stated review date has passed; a current row is state, not narrative |

**WATT is the control and carries none of the three.** Its 47,242 bytes sit in 87 lines — **543 bytes per line** — which is density, not accretion. **If WATT finds nothing to rotate, that is a valid and useful pilot result: it bounds the rule's scope to agents whose mass is accreted rather than dense.** Do not manufacture a rotation to hit a number.

## FALSIFIER — grade 2026-08-22

> **If a piloted agent, within two weeks, re-derives something the archive already held, or re-asks a question the archive already answered, the cap is too tight and the number moves.**

**Reported by the piloted agents themselves, not by DAEDALUS.** One line each into their own STATUS or a packet to PROME: what was rotated (bytes), pair size before and after, and whether they hit the falsifier. **I do not grade the pilot on files I would have an incentive to read favourably** — I proposed the cut and would run the fleet sweep.

Second failure condition, on the mechanism rather than the agents: **if the pair total falls while the brief's share rises, the narrative relocated and the joint cap did not bind.** Measure both legs separately at grading, never only the total.

## What does NOT change

Nothing about an owner's obligations, thresholds, predictions, kill rails, brief schema, boot steps or closeout steps. **The archive is one `git mv` away and greppable.** An agent needs its own narrative to reconstruct why it believes what it believes (NEXUS) — this pilot moves that narrative, it does not remove it. **STATUS is doing two jobs and only one of them needs 142 KB.**

---

## PILOT RESULTS — WATT seat, 2026-08-17 (reported 5 days early; both packets verified)

**Rotation #1: over-cap-solved-LEGITIMATELY** — 10,902 B / 6 blocks rotated verbatim (67,485 → 52,799 vs the 61,440 pair cap); falsifier NOT hit (nothing archived was re-derived or re-asked); every rotated block superseded by a later read in the same file. **Session-end final: 61,572 / 61,440 — 132 B OVER after FOUR rotations, remaining content is live state.** WATT correctly refused a fifth rotation (trimming live content corrupts the pilot in the direction that looks like success — the spec's own rule). **Verdict: the 60 KB pair cap does not fit this seat's throughput.** Disposition under the 2026-08-17 Will-ratified byte-tier convention: the budget is the OWNER'S to set locally — WATT raises its seat budget with the measured rationale; the pilot's mechanism (rotation-not-deletion, crc, falsifier) is CONFIRMED WORKING, the parameter was wrong, not the machine.

**Scanner-design finding (load-bearing for the fleet sweep):** my pilot scoping predicted WATT had "nothing to rotate" off a scan keyed on dated section HEADINGS — WATT's accretion lived inside prose BLOCKQUOTES self-labelled "retained for continuity." Density and accretion are INDEPENDENT properties; a FORM-keyed instrument returns a claim about the pattern set, not the population, and fails toward "clean" so nobody re-checks (second FORM mis-read of this same agent in two weeks — PAT-078 was the first). **Rotation targets are defined by SUPERSESSION SEMANTICS, not structural form.** Cheap proxies that would have caught it: any block containing a date older than the file's Last-Updated stamp; any block whose own text says "prior / retained / superseded / for continuity."

**Amendment-10 v2 candidate (WATT-declared exception, one hygiene-only STATUS write after the fold + one empty "noop" commit on shared history, both declared not papered over):** "fold after the last STATUS write that changes FLEET-FACING content; a declared hygiene-only write after is permitted." Adopt at next pilot touch.
