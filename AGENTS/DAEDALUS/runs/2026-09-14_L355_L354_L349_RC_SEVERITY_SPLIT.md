# 2026-09-14 — L355 + L354 + L349: the read-cap severity split and the D1 reason channel

**Desk:** DAEDALUS · **Spawn:** PROME WQ-184 Tier-1 L0 (`prome-e9`) · **Rows:** DOCKET L355 🔴 · L354 🟠 · L349 🟠
**Method:** acceptance conditions written BEFORE any edit (WQ-229). Conditions are the test list.

---

## 0. WHY THESE THREE ARE ONE PIECE OF WORK

L355's carried condition ⑤ says it in terms: *"L354's false-RED in the same pass or explicitly not — they are
one piece of work: B2 cannot hold while an advisory is indistinguishable from a defect inside the child."*

That is the whole diagnosis. `read_cap_check.check_agent` computes

    rc = 1 if (n_over_budget or problems) else 0

over a `problems` list that is FLAT — three heterogeneous classes share one bucket and one severity:

| class | example | what it is | today |
|---|---|---|---|
| bad mode | `mode 'wholee'` not in the vocabulary | **manifest defect** | rc 1 |
| missing file | declared read does not exist on disk | **manifest defect** | rc 1 |
| executable declared cap-bearing | BROCK's `ledger_staleness.py` as `programmatic` | **ADVISORY — the check explicitly declines to adjudicate** (*"Not reclassified here — the declaration is the reader's"*) | rc 1 ← **L354's false RED** |

And `rc` is a THREE-STATE token carrying a ONE-BIT reason. So downstream:

- **L355:** D1 receives rc 1 and a `0/37 over BUDGET` summary, cannot tell backlog from defect, reads the
  zero counts and returns **PASS**. The registered leg certifies a run that found something.
- **L354:** a desk with a legitimate `programmatic` declaration can never be green, and as WQ-236's rollout
  proceeds the advisory starts driving fleet rc 1 for desks that are fine.

One cause, two opposite-direction symptoms. Fixing either alone leaves the other's mechanism intact.

---

## 1. ACCEPTANCE CONDITIONS (written before editing; these ARE the test list)

Six carried in DOCKET L355, plus three the mirror rows add. In the DEFECT's own terms, not the symptom's.

**C1 — the verdict comes from a machine-readable reason the CHILD emits, never re-derived from prose.**
D1 must not infer *why* rc was what it was. The child states it. A prose totals line is not a reason channel:
it says what was found, never what class it belongs to.

**C2 — manifest defects and size-backlog findings are distinguishable and treated differently.**
Collapsing them in EITHER direction is a defect. (Making every rc 1 blocking is the forbidden fix — it erases
the intentional advisory treatment of the 5/37 over-budget desks and converts a size backlog into a boot blocker.)

**C3 — the mapping over {0,1,2} × {defect, no defect} is explicit and TOTAL. No cell left to inference.**
Including the cells that *should be impossible*: an impossible cell is a CONTRADICTION between the child's rc
and the child's own reason, and must fail closed, never silently pick one.

**C4 — advisory / delta-keyed backlog behaviour preserved EXACTLY**, verified by diffing D1 before and after
on the live fleet. Before-image captured prior to the first edit:
`D1 → [ADVISORY, delta-keyed] 5/37 desk(s) over BUDGET · 0/37 over CAP`, `--fleet` rc 1, selftest 59/59.

**C5 — L354's false RED fixed in the same pass** (the severity split), not a patch: advisories must not drive
rc, and must still print and still be countable downstream. An advisory nobody can see is not a severity split,
it is a deletion.

**C6 — tested AT THE PROCESS BOUNDARY with a STUBBED CHILD across every cell** — not at the parser, not at the
helper. The defect lives in what crosses `subprocess.run`, so the test must cross `subprocess.run`.

**C7 (L349) — a read-cap flag on a GENERATED file must name a routing target, or say honestly that it cannot.**
The remedy paragraph already exists; what is missing is WHO. `finding_imperfect_level_to_the_right_owner_beats_
a_perfect_one_to_nobody`.

**C8 (L355's added rule) — no three-state rc contract in the tree may be collapsed by `||` / truthiness at a
call site I own.** Writing `rc 0/1/2` in a docstring does not make callers three-valued; only a call site that
names the states is.

**C9 — no live-checkout test.** Two live-state test defects in two sessions, one of which deleted a real canon
file. Every fixture is frozen and tempdir-local.

---

## 2. NEIGHBOURS CONSIDERED (five categories — consider, not perform)

| category | applies? | disposition |
|---|---|---|
| **ordinary** | YES | the 5/37 over-budget fleet, 0 manifest defects — the live case. C4's before/after diff IS this test. |
| **overlap** | YES — **and this is the one that would have been missed** | a desk that is BOTH over budget AND manifest-defective, and a desk that is over budget AND carries an advisory. The severity split must not let the size finding mask the defect or the defect mask the size finding. Tested as its own boundary cell. |
| **wrong owner** | YES | the generated-file case (L349): the flag is raised at the READER's desk and the remedy belongs to the SOURCE's owner. C7. |
| **missing information** | YES | the child emits no reason line at all (an old copy of the tool, a truncated pipe). D1 must fail CLOSED — CANNOT-CERTIFY — never fall back to parsing prose, because the prose fallback is exactly today's defect. |
| **concurrent activity** | N/A — justified | `READS.tsv` being half-written mid-run is already handled and already tested (❌F2, the `n_assessed == 0` suppression added 2026-09-12); this repair does not touch that path, and the new reason line is emitted from the same already-computed counters, so it cannot disagree with them. |

---

## 3. RESULT — per condition

| # | condition | verdict | evidence |
|---|---|---|---|
| C1 | reason from the CHILD, never re-derived | **MET** | `read_cap_check` emits `READ-CAP-RESULT v1 …` as its last line; `validate_all.leg_read_cap_fleet` parses only that. ⛔ **No fallback to the prose regex** — a fallback would restore the defect silently on an older child. |
| C2 | defects vs backlog distinguishable, treated differently | **MET** | `problems` rows are typed `P_DEFECT` / `P_ADVISORY`; counts travel separately (`desks_with_manifest_defect`, `desks_over_budget`, `desks_with_advisory`). Defect ⇒ FINDINGS, never delta-gated. Backlog ⇒ ADVISORY, delta-gated. |
| C3 | mapping over {0,1,2} × {defect,no defect} explicit and TOTAL | **MET** | `classify_read_cap()` — the table is in its docstring and every cell returns, including the two CONTRADICTION cells (rc 0 with defects; rc 1 naming no reason) and an out-of-contract rc. |
| C4 | advisory/delta behaviour preserved EXACTLY | **MET — and proven under a PINNED comparison, not a live diff** (see §3a) | old and new D1 driven against identical stub children: **1 of 5 cells changed, and it is the reported defect.** |
| C5 | L354's false RED fixed in the same pass | **MET** | `rc = 1 if (n_over_budget or defects)` — advisories no longer drive rc, still print, still count. A legitimate `programmatic` declaration can now be green. |
| C6 | tested at the PROCESS BOUNDARY with a stubbed child, every cell | **MET** | 14 new boundary drills in `validate_all --selftest`; each writes a stub child and runs it through `subprocess.run`. Selftest 24 → **36 drills**. |
| C7 | a generated-file flag names a routing target or says it cannot | **MET, and wider than the row** (see §3b) | `generated_sources()` + the `➜ ROUTE TO:` branch. Live: WALTER's flag on RED's file now routes **to RED** and names both source paths. |
| C8 | no three-state rc collapsed by `\|\|` at a call site I own | **MET for committed text; MECHANISED for ephemeral** (see §3c) | census: **0 true committed offenders**; `pipeline_rc_guard.py` gains a second recogniser. |
| C9 | no live-checkout test | **MET** | every fixture is a tempdir; the old-vs-new comparison runs `git show HEAD:` copies in the scratchpad. Nothing under the checkout was mutated to run a test. |

### 3a. C4 — why the before/after diff is PINNED, not a live re-run

The row asks for a diff of D1 "before and after on the live fleet." **That comparison is not sound today and
I am saying so rather than performing it and reporting the number.** TERRY and RED are live in this session:
between my first and second `--fleet` runs, TERRY's `TRADE_BOOK.md` crossed budget (101%) and WALTER's worst
file changed, moving the fleet 5/37 → 6/37 with no code change of mine. A two-timepoint live diff would have
attributed a concurrent desk's edit to my repair.

So C4 was verified the way it should be: **both implementations driven against IDENTICAL stub children**,
old loaded from `git show HEAD:scripts/validate_all.py`.

| cell | OLD D1 | NEW D1 | |
|---|---|---|---|
| rc 1 + manifest defect + `0/37` summary | `PASS` | `FINDINGS` | ← **the defect, and the ONLY change** |
| rc 0 + clean + `0/37` summary | `PASS` | `PASS` | unchanged |
| rc 1 + backlog AT baseline 6 | `ADVISORY` | `ADVISORY` | unchanged |
| rc 1 + backlog ABOVE baseline (9) | `FINDINGS` | `FINDINGS` | unchanged |
| rc 2 | `CANNOT-CERTIFY` | `CANNOT-CERTIFY` | unchanged |

**1 of 5 cells changed behaviour.** Live D1 before `[ADVISORY, delta-keyed] 5/37`; after `[ADVISORY,
delta-keyed] 6/37` — same state, same shape, the count moved because TERRY moved.

### 3b. C7 — the live instance was ALREADY printing, one tier below where the fix was built

L349 was registered as *"fix BEFORE the instrument starts printing at scale."* Reading the live instance
instead of the row's description of it: `AGENTS/RED/registry/FALSIFICATION_TRIGGERS_SCAN.tsv` is **30,691 B
= 94% of budget → 🟡, rc 0**, and `grade()` hands it the words `rotate-tier (≥75% of budget)`.

⇒ **The inapplicable remedy was already being printed, and at rc 0 the 2026-09-12 generated branch could not
reach it** — that branch sits inside `if rc:`, so it only ever fired on an over-budget file. A caveat that
waits for the file to go over budget arrives after the owner has acted on the advice it was meant to qualify.
`finding_scan_keyed_on_naming_reads_local_form_as_absence`: the branch was keyed on the two marks someone had
named, and the third mark carries the same remedy word. **A remedy word, not a severity, is what needs the
caveat.** Fixed: tier set is 🔴/🟠/🟡 and the block is hoisted out of the rc branch.

### 3c. C8 — the audit found ZERO committed offenders, and that is the finding

31 tools reserve rc 2. A census over every committed `.md`/`.sh`/`.py`/`.tsv`/`.json` returned **28 raw
matches** of a two-valued idiom near one of their names. On inspection, **true positives = 0**:

- **prose and data rows** (KB.tsv, PATTERNS.tsv, DOCKET.tsv, READS.tsv notes cells) that merely contain `||`;
- **cwd guards** — `(cd "$(git rev-parse --show-toplevel)" && python3 …/boot.py)` at CARL, LIQUID, OZK — where
  the `&&` PRECEDES the tool and consumes no verdict;
- **correctly-labelled quotations of the defect inside its own diagnosis** (my 9/12 run record §10, and the
  memory file), which are the record of the error, not a recipe.

⛔ **I am not reporting "28 call sites."** The headline count and the finding differ by the whole of the
finding. The result is that the class lives in **ephemeral shell typed at the moment of use** — the identical
conclusion the 2026-09-12 pipeline census reached, which is why the fix belongs in the existing PreToolUse
hook and not in a new repo lint. ⚠️ **PAT-083: the two censuses share a corpus, so they are NOT independent
evidence that the repo is clean.** They establish where the class lives; nothing more.

`scripts/pipeline_rc_guard.py` gains a second recogniser rather than a new tool being built
(*prefer promoting or repairing an EXISTING control*). Selftest 19 → **32 drills**.

### 3d. Two defects the new drills found in my own work, recorded because they are the useful part

1. **A leg that contradicted itself.** I wrote `('python3 scripts/validate_all.py || echo done', False,
   "CLEAN?? — see note: validate_all IS three-state, so this MUST fire")` — want=False beside a note saying
   it must fire. The drill failed and that is how I found it.
2. **I walked into this file's own documented trap.** My first segment splitter was `[;&]{1,2}`, so
   `bash verify_push.sh "$s" >/dev/null 2>&1 || …` was cut at the `&` of `2>&1` and the segment became the
   string `1` — the recogniser missed the verbatim real instance. **The OTHER recogniser in the same file
   carries a capitalised warning about exactly this**, from its own v1, four lines above the code I wrote.
   `[[finding_naming_a_caveat_can_substitute_for_fixing_it]]` — reading a hazard note is not the act of
   applying it. Third occurrence of the `&`-in-redirection trap in this one file, second by the author of
   the warning. **The drill that caught it is the one driving the instance VERBATIM rather than a paraphrase.**

Also corrected: two pre-existing D1 drills pinned a child that **cannot exist** — a stub printing `9/37 over
BUDGET` while exiting 0. The real tool exits 1 whenever a desk is over budget. Under the new total mapping
that shape is a CONTRADICTION, correctly; the drills were re-cut to emit rc 1, which is what the child does.

---

## 4. COMPLETION NOTE — four states, not merged

- **IMPLEMENTED** — all of C1–C9. Child severity split + reason channel; parent total mapping; generated-file
  routing at three tiers; guard recogniser #2.
- **TESTED (by me, against my own conditions)** — `read_cap_check --selftest` 59 → **71/71**;
  `validate_all --selftest` 24 → **36/36**; `pipeline_rc_guard --selftest` 19 → **32/32**; live
  `--fleet` and a full live `validate_all` run; FP measurement on 851 committed candidate lines.
  ⭐ **Falsified, not just passed:** the old implementation was loaded from `git show HEAD:` and driven
  through the same boundary — the rc1+defect cell returns `PASS` on the old code and `FINDINGS` on the new,
  so the drills demonstrably fail on the pre-fix code. A suite that passes on both versions tests nothing.
- **INDEPENDENTLY VERIFIED — NO.** Every test here is the author's. `finding_adoption_is_not_validation`.
  **L355 and L354 are CONSEQUENTIAL by the WQ-229 test** — they touch a registered gate leg and a
  fleet-wide instrument, and L355 is a defect that has ALREADY RECURRED (the 9/12 repair was partial).
  ⇒ **They require an independent reader who devises a counterexample of their own before this is called
  fixed.** Requested of PROME; until that happens the correct label is IMPLEMENTED + TESTED.
- **STILL UNRESOLVED** — (a) `pipeline_rc_guard.py` remains **UNWIRED**: wiring a PreToolUse hook edits
  `.claude/settings.json`, which is not mine. Both recognisers are dormant until PROME or Will wires it —
  `finding_guard_correctness_and_wiring_are_independent`. (b) The **Python-source** form of the three-state
  collapse (`if subprocess.run(...).returncode:`) is out of a Bash hook's perimeter and is pinned as such in
  the drills; it is uncovered and would need a repo lint. (c) The `THREE_STATE_TOKENS` list is derived by a
  rerunnable command, not self-maintaining — a tool that gains an rc 2 and is not added is a dormant leg.
  Re-run at each Wiring Sweep.
