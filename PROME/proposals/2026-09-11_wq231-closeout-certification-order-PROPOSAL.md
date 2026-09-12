# WQ-231 — Closeout certifies a state it then changes

**Status:** PROPOSAL · v2, rewritten 2026-09-11 20:3x ET after a blind plan read scored
**4 ❌ / 10 ⚠️ / 10 ok** and forced a different design. v1 is in this file's git history.
**Raised by:** CODEX external review 2026-09-11 (relayed by Will in session `prome-d2`; no
separate record file — this PROPOSAL is the record). **Plan read:** `coldreader`, Opus, blind.
**Owner:** PROME (its own operating manuals).

---

## The defect

`PROME/.claude/skills/closeout/SKILL.md` orders: **3** state writes + page renders → **6** FINAL
gate → **6b** ARGUS "apply ❌ only" → **7** commit. ARGUS writes to sources after the run that
certified them, and the runner names no return through the gate.

**Correction to v1 (plan-read ❌9).** v1 said the defect was in BOTH the manual and the runner
and quoted *"BLOCKING fails here are fixed before anything is committed"* as CLOSEOUT.md:37.
**That string is not in CLOSEOUT.md at all** (`grep -c 'fixed before'` → 0). It is the RUNNER's,
`SKILL.md:20`. The accurate finding is narrower:

- `CLOSEOUT.md:135` places ARGUS "after Chunks 1–3 writes and **BEFORE committing**";
  `CLOSEOUT.md:37` places the gate "immediately before the commit". **The manual does not order
  the two against each other — it is ambiguous, not wrong.**
- **The runner resolves that ambiguity in the unsafe direction.** The defect is the runner's.

## What the gate actually depends on

Established at the artifact, correcting v1's "the gate reads the rendered pages":

- `prome_gate.py:504` `check_dashboard_state()` reads **`PROME/tools/dashboard_state.json`** — a
  side-effect file written by `fleet_dashboard.py` — **not a rendered page**.
- There is **no Helm and no Decision Deck check in the gate** (the `decision_deck` imports at
  :412/:433/:436 use it as a parser library for the aged-waits check, not as a page check).

⇒ Only ONE of the three Standard+ surfaces must precede the gate, and it must precede it because
it *produces the gate's input*, not because the gate inspects a page.

## The change-feed hazard, corrected (plan-read ❌16)

v1 claimed a second real render "shows Will only the correction — the session's actual changes
are consumed by a build that never shipped." **That is wrong.** `will_brief.py:379-393`:
`CHANGES` is an **append-only log**, and `recent = (existing + added)[-7:]` — the first render's
entries persist and still render. What a second real render actually breaks is narrower: `SNAP`
is overwritten (baseline advances twice), `_persist_state(len(added))` records a second count,
and the once-per-real-rebuild contract in `--no-feed`'s own help text is violated.

**Consequence for the design: re-rendering is less harmful than v1 asserted, so "ordering is the
only safe repair" does not follow.** The order below is still preferred — but because it removes
the need to re-render at all, not because re-rendering would destroy Will's feed.

## Acceptance conditions

- **C1** No artifact that ships is certified by a gate run predating its last write, **for every
  write the closeout procedure itself mandates**. (Bounded deliberately — see Residual below.)
- **C2** No Will-facing surface is *finally* rendered from sources a later mandated step changes.
- **C3** The Helm change-feed advances exactly once per closeout, on the render that ships.
- **C4** `CLOSEOUT.md` and the runner state one order; neither contains an order the other contradicts.
- **C5** A correction found after the gate names what must be redone, and redoing it cannot violate C3.
- **C6** *(dropped — it was a condition on reasoning, not on an order; vacuously satisfiable. The
  substance moves into the Residual paragraph, where it is a statement rather than a test.)*

## Proposed order

Lettered to avoid collision with the runner's live numbering (⚠️18); the transplant renumbers
`SKILL.md` steps 3–8 in one edit.

```
A  state writes (CLOSEOUT Chunks 1-3)
B  ARGUS audit - scope, spawn, apply ❌, ⚠️ to residue        [Standard/Heavy only]
C  root closeout steps 1b-1e - orphan · consumer · ledger · memory-index · claim.
   THEIR WRITES HAPPEN HERE, not after the gate.             [plan-read counterexample (a)]
D  fleet_dashboard.py  -> writes dashboard_state.json = the gate's input
E  FINAL gate. On rc=1, the return path DEPENDS ON WHAT THE FIX CHANGED:
     E1  fix touched a Fleet-dashboard input  -> re-run fleet_dashboard.py, THEN the full gate
     E2  fix touched only other checks' sources -> re-run those checks, THEN the full gate
     E3  loop until rc=0. The gate that counts is the LAST one, run over the CURRENT
         derived state - never a re-read of output generated before the fix.
F  THE HELM + DECISION DECK render, then publish.
G  commit + push
```

⚠️ **E1 is the leg v2 omitted.** Re-running the gate alone after a dashboard-input fix
re-checks the STALE `dashboard_state.json`: the gate reads the file, not the sources, so it
would pass on output generated before the fix. Regenerating the derived input is part of the
retry, not a separate courtesy.

**What F buys, stated narrowly:** the feed-bearing surfaces render after the last gate-forced
fix, so **no gate failure occurring at E can oblige a second real render.** That is the whole
claim. It does **not** eliminate second renders from rendering failures, publication failures,
concurrent changes, or writes introduced during git recovery at G. The plan read's counterexample
(b) — the commonest BLOCK classes (`DOCKET lands-today`, the three GATES BLOCKs) are exactly the
Helm's snapshot inputs — is what makes F necessary, and why the Helm cannot sit at D.

**F distinguishes three states and the report names which was reached:** source state VALIDATED
(gate rc=0) → output GENERATED → page PUBLISHED. A publication failure does not invalidate the
gate and must never be reported as a shipped closeout.

**Tiers (⚠️21):** B is Standard/Heavy. D and F are Standard+. Light/Bounce run A · C · E · G;
C1 holds for them because no render occurs.

## Residual — stated, not closed

**C1 cannot be made absolute and this proposal does not claim it is.** Step G can itself surface
writes: a non-ff rebase, or a commit-time fix. `commit_check.py` checks commit intent and paths;
it does **not** establish that shipped content passed the gate, and must not be credited with it.
The bound achieved is: *no write that the closeout procedure itself mandates falls after the gate.*
Writes arising from concurrent activity at push time remain outside it.

⛔ **"The gate certifies the SHIPPED state" is retired as a description** (it is the runner's
current wording, `SKILL.md:20`). What the gate actually establishes: **selected source records
plus the Fleet dashboard's `dashboard_state.json`.** It does not cover the Helm, the Decision
Deck, publication success, or the eventual — possibly rebased — commit. Reports say what passed,
not that everything did.

## Completion state (WQ-229 — four states, never merged)

- **IMPLEMENTED.** The order is in `PROME/CLOSEOUT.md` (rule + reason) and
  `PROME/.claude/skills/closeout/SKILL.md` (sequence), root `.claude` copy synced identical.
- **TESTED.** `prome_gate.py closeout` → ✅ PASS (7 blocking / 17 advisory); skill parity IDENTICAL.
- **INDEPENDENTLY VERIFIED — as TEXT only.** Three blind `coldreader` passes: plan 4 ❌ → result
  3 ❌ → narrow third read 3 ❌, all fixed. Read budget now SPENT; both files closed for the session.
  ⛔ **No closeout has been EXECUTED under this order.** A reading pass verifies pointers; only
  execution verifies executability (`finding_adoption_is_not_validation`). The first real run is the test.
- **STILL UNRESOLVED:**
  - ⛔ **The WQ ledger is covered by no gate check** (`grep -c wq_ledger prome_gate.py` = 0) while the
    Deck's Decided tab reads it. Documented in the return path, **not fixed**. This is a defect with
    no owner-facing guard and it should become a gate check.
  - ⚠️ **The licence the whole order rests on is fragile by construction:** late renders are safe only
    because the gate checks none of `brief_snapshot.json` / `brief_changes.jsonl` / `WQ_EXPLAINERS.tsv`
    / `argus_baseline.json`. Adding a gate check on any of them silently invalidates this ordering.
  - **Declared residue (15 ⚠️, not fixed):** `--no-feed` unnamed in either file though a publication
    retry re-advances the change-feed · the VALIDATED→GENERATED→PUBLISHED tri-state lives only in the
    runner · the rc=1 list names FILES while the Fleet row mandates a published PAGE · blind-reader
    verification (CLOSEOUT L103) has no runner slot · 1d-bis has no runner slot · runner step 1
    (read fleet memories) has no rule behind it · Deck items ①/③ have no runner slot · runner
    disclaims tier logic then carries it · "Standard+" undefined in the tier table · subject-length
    stop rule off by one against its own wrapper (`wc -c` counts the newline) · `plans/…` base-relative
    pointer · HEARTBEAT "ask at every tier" vs Bounce · step 3 regenerates one of SCRATCH's two blocks ·
    L135 vs L37 read as opposed on what the gate buys · "RUN IT AFTER EVERY MANDATED WRITE" reads as N runs.

**Not ruled by Will.** PROME owns these two files; the repair needed no word and none was given.
