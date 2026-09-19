# HANS CLOSEOUT

**Created:** 2026-09-18 · **Owner:** HANS
**Purpose:** repeatable session-end write-back. Run before `/clear`, `/new`, or handoff.

> Companion to `CLAUDE.md` § SPAWN PROTOCOL (session start). **Git mechanics = root `CLAUDE.md` § Git Protocol — canon there, not restated here.** Tier vocabulary mirrors `PROME/CLOSEOUT.md` / LIQUID / TERRY so the words mean the same thing across desks.

🔴 **WHY THIS FILE EXISTS, and it is not tidiness.** Until 2026-09-18 this desk had **no closeout document and no closeout heading** — one of the minority of 44 desks with neither (3 desks carry a `CLOSEOUT.md`; 24 carry a closeout heading in `CLAUDE.md`). Every session I reconstructed the root protocol from memory. On 2026-09-18 that failed exactly the way an unwritten procedure fails: **I ran root step 1c's cross-agent form, skipped its `--self` form, and reported the closeout complete.** The cross-agent scan *excludes my own directory*, so the form I skipped was the only one that could see the ~12 figures I had superseded that session. **Will asked whether I had followed the procedure; the answer was no.** → `ML-HANS-456`

⛔ **THE FAILURE MODE THIS FILE IS BUILT AGAINST: an ABSENT step among passing ones.** Orphan clean · claim-check clean · audit 0 · 58 tests OK · read-cap green · push receipt confirmed — **six green signals around one that never ran.** No individual check can see a step that did not execute. **A checklist with an item omitted does not look like a failure; it looks like a shorter checklist.** ⇒ **Every step below is NUMBERED and NAMED so an omission is visible as a gap, not invisible as a shorter list.**

---

## When to run

Before `/clear` or `/new` · before stepping away from a long session · after any session that changed a level, fired or graded a threshold, resolved a prediction, or dispatched to another desk. Skip for casual exchanges with no artifacts.
**Live-event override:** if a print or trigger window is in progress (PMI flash, ECB/BoE decision, a rung crossing), **DEFER** the full write-back — snapshot STATUS, keep the board live, close out after.

## Pick a tier

| Tier | When | Touches | Commit? |
|---|---|---|---|
| **Bounce** | Mid-session restart, back within the hour | STATUS header line only | No |
| **Light** | Short session, 1–2 artifacts, no level moved | STATUS surgical + the ledger you touched | Optional |
| **Standard** *(default)* | End of thread/day; levels refreshed, mail drained, packets sent | Steps 1–12 | Yes |
| **Heavy** | Tooling built, a durable lesson earned, or a structural change | Standard + `ML.tsv` + auto-memory candidate + `CLAUDE.md` rule | Yes |

---

## THE ROUTINE — run in order; **name each step's outcome, including "no-op"**

**Steps 1–7 are HANS-specific. Steps 8–11 are the root protocol, enumerated by name because pointing at root is what let one go missing.**

1. **`python3 scripts/doc_audit.py`** — `CLAUDE.md` RULE #1b. **Not last: it must run again after the final edit** (step 12's ordering).
2. **Registry + fired log.** Every threshold the session touched gets `current_value`/`as_of`/`state`, or a stated no-op. A fire opened/closed/ruled → a row or an annotation in `registry/HANS_T_FIRED_LOG.tsv`. ⛔ **A count mirror (`CLAUDE.md`, STATUS "N of M") changes whenever a row is added.**
3. **`workbook/VX.tsv`** — the metric surfaces behind every threshold you moved. `doc_audit` C3 fails on registry≠VX per leg; that check is the reason, not a formality.
4. **`workbook/KB.tsv`** — new facts; supersede rather than overwrite. **Status tokens come from `AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md`** (`CLAUDE.md` RULE #1c) — canonical token, then date, then prose.
5. **`workbook/PREDICTIONS.tsv` · `FLOW.tsv`** — a prediction due/drifting gets a tracking note; a chain whose trigger leg moved gets one. **Answer the ledger nudge (step 10) substantively or say why not.**
6. **`workbook/PUBLISHED.tsv`** — **every figure you published to another desk or to Will**, including one you **withdrew**. ⛔ **Append-only; CONTINUE the established metric name.** A new name for an existing series orphans it *and leaves the superseded value reading CURRENT*, which silently disables stale-consumer detection for that series (`ML-HANS-455`).
7. **`LAST_COMPLETION.md`** — **overwrite, do not append**: STATUS / CHANGED / RESULT / GAPS / WILL_NEEDS / FOLLOW-UP. ⚠️ **This file sat at a 2026-07-16 vintage until 2026-09-18, asserting `WILL_NEEDS: None` and `FOLLOW-UP: None` through the 8/28 revival and everything after.** A handoff surface claiming completeness while stale is worse than an absent one.
8. **ROOT 1b — orphan:** `bash scripts/orphan_check.sh HANS`. `[likely YOURS]` ⇒ commit (carve-out ①); `[not yours]` ⇒ flag, never sweep.
9. 🔴 **ROOT 1c — consumer check. TWO FORMS, AND BOTH ARE REQUIRED:**
   - `python3 scripts/consumer_check.py --agent HANS --from-ledger` — other desks citing a figure I retired ⇒ **packet them, never edit their files.**
   - `python3 scripts/consumer_check.py --agent HANS --self --from-ledger` — **⛔ THE ONE THAT WENT MISSING 2026-09-18. The cross-agent scan EXCLUDES my own directory; this is the only form that sees my own surfaces.** I own these: fix in place, no packet.
   - ⚠️ **Send nothing on a bare 2-sig-fig figure** (root 1c). ⛔ **And do NOT clear a flag on a graded-event table, a dated log row, an archive, or `PUBLISHED.tsv`** — those values are correct history, and editing one to silence a checker is resolving a flag backwards.
10. **ROOT 1c-bis — ledger nudge:** `python3 scripts/ledger_staleness.py --nudge HANS`. It reports **quantity**, never correctness — a "behind" count says nothing about whether the rows are right.
11. **ROOT 1d — memory · ROOT 1e — claim.** 1d only if an auto-memory was written: `python3 scripts/memory_index_check.py --strict --slug <name>` **and** `bash scripts/check_memory_length.sh`. 1e always: `python3 scripts/claim_check.py --check weekday STATUS.md workbook/KB.tsv registry/THRESHOLDS.tsv`.
12. 🔴 **FREEZE → AUDIT → COMMIT → PUSH, in that order.** The last thing that may write inside the candidate is step 7. **Then** re-run `doc_audit.py` **and** `python3 scripts/test_hans.py` **and** `python3 ../../scripts/read_cap_check.py --agent HANS`. Commit path-scoped from the repo root; **push only after all three are green.** Receipt is the literal line `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).`
   ⛔ **NEVER PIPE `safe-push.sh` THROUGH `tail`/`head`.** It has **three** distinct outcomes — `ABORT` (non-ff), `CANNOT-CONFIRM` (post-push fetch failed, exit 2), `NOT PUSHED` (push did not land) — and **the RECOVERY text at the bottom is identical across two of them.** Tailing keeps the recovery lines and discards the state line. *(2026-09-18: I tailed all ~8 pushes, misread `NOT PUSHED` as a non-ff abort, and reported the wrong mechanism to Will as a fleet defect. The script's own comment block warns that piping launders push status — the warning was in the file I was running.)* → `ML-HANS-457`

---

## The runner

`python3 scripts/closeout_check.py` executes every mechanical step above and prints **RAN / FAILED** per step, then **lists the judgement steps it cannot verify**. ⛔ **It does not certify those — a runner that claimed to would be the same defect one level up.** Its whole purpose is that **a step which did not execute appears as a gap**, which is the one thing no individual check can report.

## Surfaces boot reads — closeout must write back to each, or say no-op

`boot.py` §[1]–[7] reads: live pull · European primaries · **registry fire state** · **key-figure age (VX)** · **predictions due** · **live-vector staleness** · **KB expiry**. **Every one has an owner above** (§[3]→2, §[4]/[6]→3, §[5]→5, §[7]→4). **If boot reads it, closeout owns writing it** — that symmetry is the check; an unowned boot surface is how a board goes stale while every session reports clean.

## Not covered here, deliberately

Git mechanics (root canon) · trade construction (TERRY) · signal routing (WALTER) · the fleet enumeration of continuation-ticker exposure (PROME, DOCKET L429 — **my desk's own enumeration is `KB-HANS-081`**).
