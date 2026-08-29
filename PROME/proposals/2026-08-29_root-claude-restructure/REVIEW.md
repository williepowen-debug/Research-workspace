# Root `CLAUDE.md` restructure — DRAFT for RAV review (WQ-120)

**Owner:** PROME · **Written:** 2026-08-29 · **Status:** DRAFT, RAV pass 1 PASSED with two corrections (both applied below: atomic apply, rule-key parity) — Will-ruled *"approved for a proposal draft and RAV review only; do not edit root canon until I rule on the reviewed draft"* (8/29). **Nothing in this folder is live.** Root `CLAUDE.md` is untouched.

## 1. The problem, measured

| | Live root (`981ea5e44`) | Proposed root | Δ |
|---|---|---|---|
| Bytes | **36,062** | **20,085** | −44% |
| ≈ tokens auto-loaded per agent boot (÷4) | ~9,000 | ~5,000 | −4,000 × every session of 33 desks |
| Provenance parentheticals (italic/dated) | ~19% of bytes | ~0% | moved, not deleted |
| Roster names re-listed | 33 + Tier-2 + Special | 0 (pointer) | ROSTER.md is canonical |

Two independent readers said the same thing the same day: PROME's own cold boot (8/29 AM — "the boot is mostly history, not state; the rule wrapped in its biography") and RAV's review (F2 mirror-drift, F3 incident archive).

## 2. Method (the BOOT.md recipe, 8/28, extended)

1. **Every paragraph classified** RULE (stays) · PROVENANCE (moves to `docs/CANON_PROVENANCE.md`) · MIRROR (collapses to a pointer at the owner). Nothing deleted — provenance text moved verbatim where it was prose, condensed only where root's own text was already a summary.
2. **Rules keep a one-clause WHY only where the why makes the rule believed** (carve-out ③ "index rides out, file doesn't"; non-ff "property of the commit graph"; rule #6 break test). Everything else points.
3. **Stable APIs untouched:** Critical Rules 1–11 numbers and text (rule 3's PSEC example → provenance; all else verbatim); step numbers 1b/1c/1c-bis/1d/1e and 0–5/4b in the git recipes; carve-out numerals ①–④; "root rule #N" citation discipline.
4. **Every command, path and constant survives.** Token check (backticked tokens in live root = 122): 92 remain in the proposed root verbatim; 17 moved to provenance (commit hashes, memory slugs, incident records); 13 were placeholder-spelling variants (`<YOU>` vs `<YOUR_NAME>`) — restored to the live spelling so agents' greps still hit. Dates/constants: 33 in live root, 33 present across the pair. Script: `REVIEW.md` §5 test 1.
5. **Roster paragraph → pointer.** ROSTER.md already declares itself canonical and root already said "never re-list it here" — the list was violating its own rule (RAV F2). The potash rule stays as one sentence pointing at FERT (it is a behavior rule, not history).

## 3. What changes behaviorally

**Nothing.** Every rule an agent could act on in the live root is present with the same force in the proposed root. The differences a reader would notice:
- Reasons are one hop away (`docs/CANON_PROVENANCE.md`, keyed by root section, root order) instead of inline.
- The document reads as rules, so it primes an agent to *follow* rather than to *re-argue* — the priming effect Will and PROME discussed 8/29 AM.
- `docs/CANON_PROVENANCE.md` becomes the place to argue a rule's basis, and the place a future amendment writes its reason (root gets the rule, provenance gets the why, `git log -p` gets the diff).

## 4. Known trade-offs (RAV — please weigh)

1. **A rule without its incident is easier to weaken.** Mitigation: the one-clause whys kept on the load-bearing rules (§2.2), and provenance is one link away. Counter-view: the live root's incident prose has not prevented re-litigation either (the non-ff rule was re-argued 8/29 with the history in place).
2. **Two files can drift.** Mitigation = rule-KEY parity (test 3): every provenance block carries a `key:` + a `root-anchor:` phrase that must survive verbatim in root; a rule deleted or reworded in root breaks its anchor. Mechanism, not vigilance. *(Pass-1 proposed heading parity; RAV: too weak — a block can keep its heading while describing a removed rule. Strengthened.)*
3. **Placeholders `<YOU>` / `<YOUR_NAME>`** are both used in the live root; the draft keeps both where live had them rather than normalizing, so existing greps match. A follow-up could normalize under its own row.
4. **The Gate C custody paragraph** (root §Git Protocol) is kept near-verbatim — it is dense but every clause is a rule reconciled 8/27 with Will's own wording; trimming it is not this draft's business.
5. **WALTER's auto-push exception** still cites `BOARD_CONSUMPTION_SPEC` §7, which DAEDALUS D1 found contradicted by WALTER's own file; that is a WALTER reconcile, recorded in provenance, not resolved here.

## 5. Tests before any root edit (Will rules on the reviewed draft first)

1. **Token survival** — every backticked token, date and byte constant in live root appears in `CLAUDE.proposed.md ∪ CANON_PROVENANCE.proposed.md` (script run 8/29: 0 missing after the placeholder restore). Re-run at apply time against the then-live root.
2. **Blind cold reader** (CLOSEOUT Chunk 1 rec-2): a fresh Explore-class agent reads ONLY the proposed root and answers ~15 ground-truth rule questions whose answers live in the live root (where do PROME requests go · what do you never `git add` · which carve-out lets you commit a memory file · what is the read cap · what happens on a non-ff · may you renumber rule 6 · where is the roster · what is potash's depth …). Target 15/15; any miss = the rule moved too far. **RUN 2026-08-29 15:1x: 16/16 correct** (transcript → `COLD_READER_2026-08-29.md` in this folder). The reader's ambiguity list produced 7 clarity fixes applied to the draft (bare 'rule 6/6b' → 'messaging rule 6/6b' with its home named · 1d cap number restored · non-ff overlap check given a METHOD · receipt line made literally matchable · 'don't commit shared files' gains the carve-out forward-pointer · `LEDGER_GLOB` given its path · ④ names the activation surface) — 6 of the 7 were inherited from the live root, i.e. the restructure fixed ambiguities the live root has carried.
3. **Rule-key parity (strengthened per RAV pass 1 — heading parity was too weak: a block can keep its heading while describing a removed or renamed rule).** Every provenance block carries a stable `key:` (e.g. `critical-rule-6`, `git-carveout-3`, `git-step-1c`, `data-read-cap`) AND a `root-anchor:` — a short phrase that must appear verbatim in root. The test asserts every anchor is present in root and every root section has ≥1 keyed block; a rule deleted or reworded in root breaks its anchor and fails the test. Keys live in provenance only — root gains no bytes. Scriptable, ~20 lines, proposed as a `consumer_check --mirror-map` extension; keys are already in `CANON_PROVENANCE.proposed.md` (pass-1 revision).
4. **Read-cap** — proposed root is 20,085 B: under the 32,550 B budget for the first time (the live root is not formally in the read-cap perimeter because it is auto-loaded, but the budget is the right yardstick).
5. **Mirror walk** — `PROME/SYSTEM.md` → Canonical → Mirrors rows that cite root line numbers or section wording get re-pointed in the same commit (root is canonical for 6 rows).

## 6. Apply plan (only after Will's ruling on the reviewed draft) — corrected per RAV pass 1 (8/29)

1. **ONE atomic commit** — root `CLAUDE.md`, `docs/CANON_PROVENANCE.md`, and every required mirror (`PROME/SYSTEM.md` mirror-map rows, `PROME/CLAUDE.md` step-1 wording) land together through `commit_check.py`; message names WQ-120 and the ruling verbatim. *(Pass-1 draft said "provenance first, then both" — `commit_check` would have refused the unchanged provenance file on the second commit, and an intermediate half-applied state is exactly what atomicity avoids. RAV's preference adopted.)*
2. Tests 1–5 run BEFORE the commit and recorded in its message; cold-reader transcript filed under this folder.
3. Root's own header line tells every future amender: *rule → root; why → provenance; diff → git log.*
4. Rollback = `git revert` of the one commit (atomic ⇒ one revert restores the whole prior state).

## 7. Ask of RAV

Read `CLAUDE.proposed.md` as a cold agent would. Name any rule that lost force, any why that should have stayed inline, and any provenance block that should not exist at all (deleting is allowed — this draft errs toward keeping).
