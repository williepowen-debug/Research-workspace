# Root `CLAUDE.md` restructure — DRAFT for RAV review (WQ-120)

**Owner:** PROME · **Written:** 2026-08-29 · **Status:** DRAFT — Will-ruled *"approved for a proposal draft and RAV review only; do not edit root canon until I rule on the reviewed draft"* (8/29). **Nothing in this folder is live.** Root `CLAUDE.md` is untouched.

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
2. **Two files can drift.** Provenance is keyed by root section heading; a section renamed in root orphans its provenance block. Mitigation: `scripts/consumer_check.py --mirror-map` gains a root↔provenance heading-parity check (proposed test 3) — mechanism, not vigilance.
3. **Placeholders `<YOU>` / `<YOUR_NAME>`** are both used in the live root; the draft keeps both where live had them rather than normalizing, so existing greps match. A follow-up could normalize under its own row.
4. **The Gate C custody paragraph** (root §Git Protocol) is kept near-verbatim — it is dense but every clause is a rule reconciled 8/27 with Will's own wording; trimming it is not this draft's business.
5. **WALTER's auto-push exception** still cites `BOARD_CONSUMPTION_SPEC` §7, which DAEDALUS D1 found contradicted by WALTER's own file; that is a WALTER reconcile, recorded in provenance, not resolved here.

## 5. Tests before any root edit (Will rules on the reviewed draft first)

1. **Token survival** — every backticked token, date and byte constant in live root appears in `CLAUDE.proposed.md ∪ CANON_PROVENANCE.proposed.md` (script run 8/29: 0 missing after the placeholder restore). Re-run at apply time against the then-live root.
2. **Blind cold reader** (CLOSEOUT Chunk 1 rec-2): a fresh Explore-class agent reads ONLY the proposed root and answers ~15 ground-truth rule questions whose answers live in the live root (where do PROME requests go · what do you never `git add` · which carve-out lets you commit a memory file · what is the read cap · what happens on a non-ff · may you renumber rule 6 · where is the roster · what is potash's depth …). Target 15/15; any miss = the rule moved too far.
3. **Heading parity** — every `##` section in root has a matching block in provenance (and vice-versa); scriptable, ~10 lines, proposed as a `consumer_check --mirror-map` extension.
4. **Read-cap** — proposed root is 20,085 B: under the 32,550 B budget for the first time (the live root is not formally in the read-cap perimeter because it is auto-loaded, but the budget is the right yardstick).
5. **Mirror walk** — `PROME/SYSTEM.md` → Canonical → Mirrors rows that cite root line numbers or section wording get re-pointed in the same commit (root is canonical for 6 rows).

## 6. Apply plan (only after Will's ruling on the reviewed draft)

1. `docs/CANON_PROVENANCE.md` committed FIRST (so root's pointer never dangles).
2. Root replaced whole — `git commit CLAUDE.md docs/CANON_PROVENANCE.md -F msg` via `commit_check.py`; message names WQ-120 and the ruling verbatim.
3. Tests 1–5 run and recorded in the commit message; cold-reader transcript filed under this folder.
4. `PROME/SYSTEM.md` mirror rows + `PROME/CLAUDE.md` step-1 wording ("root is auto-injected") checked the same sitting.
5. Root's own header line tells every future amender: *rule → root; why → provenance; diff → git log.*

## 7. Ask of RAV

Read `CLAUDE.proposed.md` as a cold agent would. Name any rule that lost force, any why that should have stayed inline, and any provenance block that should not exist at all (deleting is allowed — this draft errs toward keeping).
