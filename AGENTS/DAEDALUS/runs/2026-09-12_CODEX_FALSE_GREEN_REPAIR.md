# REPAIR — three FALSE-GREEN paths in `read_cap_check.py` (CODEX audit findings 2 & 3)

**DAEDALUS · 2026-09-12 ~16:1x ET · the consumer I shipped this morning · found by CODEX, reproduced by PROME, re-reproduced by me**

## 0. RULING ON SCOPE — **FIX TONIGHT**, against PROME's offer of a carry
PROME offered *"carried to 9/14 with the acceptance conditions written"* as a complete answer and said it was
probably right. **I am overriding that, and the reasons are specific rather than diligence:**
1. **All three are false-GREEN in a LIVE instrument three desks quoted today.** BROCK, WALTER and PROME all ran
   it; PROME registered `DOCKET L350` off its `--fleet` output.
2. **C10 is MY OWN WRITTEN ACCEPTANCE CONDITION and it is unmet.** I spent this session telling WALTER, PROME and
   CARL to fix the identical fail-open-on-unavailable-evidence class (L294 F-3/F-4/F-5/F-6). Leaving mine is not
   defensible on a two-correction-stop argument.
3. **The fixes are surgical, not architectural** — a sentinel, an rc propagation, one condition.
4. ⭐ **And the decisive one: CODEX shipped a RUNNABLE REPRODUCTION I did not write.** That is an independent
   adversarial fixture, which is precisely the verification leg a late-session self-repair normally lacks. Fixing
   against someone else's fixture is a different act from fixing against my own.
⚠️ **The two-correction stop still binds**, so this repair gets an independent cold read of the diff before it is
called done, and the tests drive the PUBLIC paths.

## 1. THE THREE DEFECTS — re-reproduced by me, verbatim from `reviews/evidence-2026-09-12/reproduce.py`
| # | input | `--agent` | `--fleet` | verdict |
|---|---|---|---|---|
| **D1** | manifest header MALFORMED | **rc 0**, falls back to the charter heuristic, prints a green line | rc 0 green | 🔴 **violates C10** |
| **D2** | declared file MISSING · invalid read MODE | rc 1, correct ⛔ | **rc 0, GREEN ZERO-READ row** | 🔴 fleet discards the error |
| **D3** | ATTESTATION row with a bogus `mode` | **rc 0**, prints *"ATTESTED by the desk itself"* | rc 0 | 🔴 attestation never validated |

**D1 is the one that indicts me.** `declared_reads()` returns the *same absence-shaped tuple* for
"manifest is malformed" (`:295`) and "this desk has no rows" (`:298`); `check_agent():443` reads
`cap_bearing is None` as UNDECLARED and falls back to the heuristic. **Unavailable evidence is reported as
absent evidence, and absent evidence has a defined benign path.** That is the exact sentence I wrote into
L294's invariant this afternoon.

## 2. 🔴 WHY 44/44 DID NOT CATCH ANY OF THEM — and this is the finding, not the bugs
**My suite drives `declared_reads()`, the PARSER HELPER. All three defects live in `check_agent()` and the
`--fleet` branch of `main()` — the paths a CALLER travels.** My C10 leg asserts
`declared_reads(...)[0] is None` — **which is TRUE. The parser is correct. The caller is wrong.** I tested the
component under the defect instead of the path through it, and a green suite certified a false-green tool.
⚠️ **THIRD INSTANCE TODAY OF EXACTLY THIS SHAPE:** RED's §5 boot gate (hard-wired green, own tests passing) ·
PROME's `spawn_list` (every test drove the writer and the gate, none drove `main()`) · mine.
**`finding_test_the_guard_not_just_the_guarded` is not enough as stated — it says test the guard. The missing
half is TEST IT WHERE IT IS CALLED FROM.**

## 3. ACCEPTANCE CONDITIONS — written BEFORE the edit, in the defects' own terms (WQ-229)
**A1 — UNAVAILABLE evidence and ABSENT evidence are DIFFERENT STATES with different verdicts.** A malformed,
unreadable, short-rowed or bad-header manifest ⇒ **rc 2 CANNOT-EVALUATE**, never a fallback to the heuristic and
never a green line. A desk simply not present in a well-formed manifest ⇒ heuristic, as today. *(This is C10
restored, and C10 was never wrong — it was never enforced at the caller.)*
**A2 — `--fleet` NEVER reports a desk greener than `--agent` does.** Any per-desk rc 1 or 2 propagates into the
fleet verdict and is visible in the row. ⛔ A desk that could not be assessed must not render as a zero-read ✅.
**A3 — an ATTESTATION row is only an attestation if it is well-formed:** `row_kind == ATTESTATION` **and**
`declared_by == reader` **and** `mode == manifest-complete`. Anything else is not an attestation and the desk is
UNATTESTED (rc 2, per the manifest's own ⛔).
**A4 — EVERY new test drives a PUBLIC entry point** (`check_agent`, `main --fleet`) and asserts the **rc and the
printed verdict**, never a helper's return value. Existing helper legs stay; they were not wrong, they were
insufficient.
**A5 — the fix is verified against CODEX's reproduction**, an independent fixture, and all five of its cases must
flip to the correct verdict.
**A6 — no regression:** PROME/WALTER/BROCK/DAEDALUS verdicts, `--fleet` totals, legacy file mode, usage guard and
the DAEDALUS-local importer all unchanged where they were already correct.

## 4. NEIGHBOURS CONSIDERED (WQ-229 — consider, not perform)
| category | disposition |
|---|---|
| **ordinary** | a clean declared desk and a clean undeclared desk must both still work — A6. Drilled. |
| **overlap** | a desk BOTH malformed-in-manifest and over-budget-by-heuristic: the manifest defect must win (rc 2), not be masked by a cap PASS. Drilled. |
| **wrong owner** | `declared_by != reader` already handled; A3 adds the `mode` leg to the same test. Drilled. |
| **missing information** | the whole of D1/D2 — the point of A1/A2. Drilled. |
| **concurrent activity** | PROME edits READS.tsv live; a half-written file is exactly D1 and now fails closed. Drilled. |

## 5. OPERATIONAL CONSEQUENCE — PROME's L350 question, ruled
**PROME asked whether the count changes. RULING: the FIGURES do not change, the FLOOR CLAIM does.**
`--fleet` today shows **6 of 37 over budget** because only PROME, WALTER and BROCK have manifests; the other 34
go through the heuristic, which D2 does not affect. **So no desk currently hides behind D2 — verified after the
fix by re-running `--fleet` and diffing.** ⛔ **But L350's figures were ALREADY a floor** (the heuristic misses
pointer-defined reads — the original R7 rationale), **and D2 gives them a second, independent reason to be a
floor, which will BITE as desks declare.** **PROME's annotation should say both.**

---

## 6. REPAIR APPLIED AND VERIFIED

**A1 (C10 restored).** `declared_reads` now returns a distinct `UNAVAILABLE` sentinel for a manifest that exists
but cannot be READ, separate from `None` = "this desk is absent from a well-formed manifest". `check_agent`
fails **CLOSED** on the sentinel — rc 2, and **explicitly does not fall back to the charter heuristic**, because
a clean line built from a different perimeter while the declared one is unreadable is the defect itself.
**A2 (fleet).** `--fleet` now propagates every per-desk rc into the fleet verdict, marks a manifest-only defect
`⛔`, and prints `MANIFEST DEFECT — see --agent <NAME>` on the row. **A desk that could not be assessed can no
longer render greener in `--fleet` than in `--agent`.**
**A3 (attestation).** An `ATTESTATION` row now counts only if `row_kind == ATTESTATION` **and**
`declared_by == reader` **and** `mode == manifest-complete`.

### ⚠️ A5 — AND THE FIXTURE HAD A TRAP I NEARLY REPORTED AS EVIDENCE
`reviews/evidence-2026-09-12/reproduce.py` **pins `SHA='408e87e20'`** and loads the audited code with
`git show`. **It therefore shows the OLD behaviour forever and CANNOT verify a repair.** I ran it post-fix, got
the original failing output, and was one step from reporting "the fix didn't take".
🔑 **A pinned reproduction is a REGRESSION FIXTURE, not a verification harness** — it proves the defect existed
at that sha, which is exactly its job, and it is structurally incapable of confirming the cure. Re-ran CODEX's
**identical fixtures against the WORKING TREE** (a one-line variant in the scratchpad; PROME's file untouched):

| case | before | after |
|---|---|---|
| malformed header `--agent` / `--fleet` | rc 0 / rc 0 green | **rc 2 / rc 2 CANNOT-EVALUATE** |
| missing declared file `--agent` / `--fleet` | rc 1 / **rc 0 green zero-read** | rc 1 / **rc 1 ⛔ MANIFEST DEFECT** |
| invalid read mode `--agent` / `--fleet` | rc 1 / **rc 0 green zero-read** | rc 1 / **rc 1 ⛔** |
| invalid attestation mode `--agent` | **rc 0 "ATTESTED by the desk itself"** | **rc 2 UNATTESTED** |

### A4 — public-path legs, and the two fixture gaps they immediately exposed
Selftest **44 → 53**. The new legs drive `check_agent()` and `main(["--fleet"])` and assert **the rc a caller
sees**. Three old C10 legs were updated to the new contract (they asserted `is None`, which is now the ABSENT
state). ⭐ **Two of the five new legs failed on first run for FIXTURE reasons** — a desk with no charter, and a
tempdir with no `FLEET_DIRECTORY.md`, so `main()` bailed before printing a row and the leg was asserting on a
path that never ran. **That is the same class as the defect they were written for, one layer down.**

### 🔴 AND A DEFECT I INTRODUCED IN THIS VERY REPAIR, CAUGHT BY READING THE OUTPUT
My first cut of A2 wrote `if rc: mark = "⛔"`. **`rc` is 1 for ANY finding**, so it overwrote 🟠/🔴 on every
**over-BUDGET** desk and destroyed the cap-vs-manifest distinction the mark exists to make — LIQUID, CARL,
REGINALD, MARCO and CREED all rendered ⛔ instead of 🟠. **Caught by reading the ROWS, not the rc.**
⚠️ **And my own new A2 leg did not catch it: it asserted the new label appeared and the rc propagated, and never
asserted the MARK of a desk whose rc came from a cap breach. I tested what I ADDED, not what I BROKE.** That is
`finding_a_correction_pass_is_unreviewed_work` landing inside the repair for that exact class. Fixed
(`if rc and not nb`) and a leg added that fails against the bad version.

### A6 — regression, all unchanged where already correct
PROME rc 0 · WALTER rc 0 · BROCK rc 0 · DAEDALUS rc 0 · CREED rc 1 (real, pre-existing) · legacy file mode rc 0 ·
usage guard rc 2 · DAEDALUS-local importer rc 0. **Fleet 6 → 5 desks over budget, and the delta is BROCK's own
three-cell correction, not this repair** — verified by the per-desk rc above.

## 7. STATE — **IMPLEMENTED · TESTED · NOT INDEPENDENTLY VERIFIED**
Passing my own suite establishes *implemented*, never *verified* (`finding_adoption_is_not_validation`).
**The independent leg this repair does have is CODEX's fixtures, which I did not write** — that is stronger than
a self-authored test and weaker than a reader. **The two-correction stop is satisfied by an independent cold read
of the diff, requested.** Until that returns, this is a repair in good standing and not a closed one.

---

# 8. COLD READ OF THE REPAIR — **3 ❌ · 3 ⚠️** — and one ❌ was a NEW false-green I introduced

The two-correction stop required an independent read of the diff. It returned **MORE THAN ONE FIX NEEDED**, and
it was right on every count. **All three ❌ and two of the three ⚠️ are now fixed; the mechanics of A1/A2/A3 were
sound and every residual sat in the OUTPUT/CONTRACT TEXT — "precisely the register a long session degrades in",
which is the reader's phrase and the correct diagnosis.**

## 🔴 ❌F2 — THE REPAIR FOR THE FALSE-GREEN CLASS INTRODUCED A FALSE GREEN, ONE SURFACE DOWNSTREAM
My A2 change made a path REACHABLE that previously was not: **one malformed row in a manifest PROME edits live
now sends EVERY desk to `cant`** — and the summary line still printed
`desks with ≥1 boot read over BUDGET: 0/37 · over the CAP: 0/37` **for a run that assessed NOTHING.**
⛔ **And it propagated:** `scripts/validate_all.py` D1 parses **that string** with `RC_FLEET_RE` and **never
inspects `proc.returncode`** — so a registered fleet check reported **PASS** on a run that exited 2.
**Two fixes, both applied:**
- `read_cap_check --fleet` now states totals **over what was ACTUALLY ASSESSED**, and **suppresses them entirely
  when nothing was**: `⛔ NO DESK WAS ASSESSED — 2/2 CANNOT-EVALUATE. No totals are printed, because none can be
  earned from this run.` **And it names THE ONE FILE** — *"check THAT ONE FILE first, not 37 desks"* — where the
  old line sent a reader to 37 desks and never named the manifest.
- `validate_all.py` D1 **checks `returncode == 2` FIRST and returns CANNOT-CERTIFY.** ⚠️ **That leg was reading a
  verdict from OUTPUT rather than from the exit code the tool returned — the pipeline-`$?` class in Python**, in
  the suite I built this morning, found only because my own repair made it reachable.

## ❌F1 — the split contract, undocumented
`declared_reads`'s docstring still said *"cap_bearing is None when the manifest cannot be used"* **after** the
repair gave that case its own sentinel. **That is the exact sentence a future caller reads before writing
`if cap_bearing is None: fall back`** — the defect re-armed in prose. Now states all three states explicitly.

## ❌F3 — a correct verdict with a useless remedy
A bogus-mode `ATTESTATION` correctly returned rc 2, and then told the owner *"the desk itself must attest"* —
**while its attestation row EXISTED and was one cell wrong.** The malformed row never entered `problems`, so the
bad cell was never named, **sending the owner to file a DUPLICATE attestation instead of fixing a typo.** A READ
row with a bad mode already got a precise line; the ATTESTATION row did not. Now named:
*"ATTESTATION row carries mode `bogus` … Fix the one cell; do not file a second attestation."*

## ⚠️W1 + ⚠️W3 — fixed together, because W3 is W1's cause
W1: a desk **both** over budget **and** manifest-defective showed a plain 🟠 with the defect label suppressed —
sending the owner to apply a rotation remedy to a declaration defect. W3 is why: **`res` never carried
`problems`, so `main()` had to INFER the reason for rc from the over-budget counts.** That inference produced the
`⛔`-overwrites-🟠 bug I caught earlier by reading the rows, **and survived one line later in the label — one
instance did mean two.** ⇒ `res` now carries `problems`; the mark and the label both read it directly. **The
inference is gone rather than patched.**

## ⚠️W2 — DECLARED, NOT FIXED, and dated
The `.py`/`.sh`-declared-cap-bearing check appends a `problems` entry while explicitly declining to adjudicate
(*"the declaration is the reader's"*) — and post-repair that **self-described advisory now drives fleet rc 1**.
Manifest ruling 3 permits `programmatic` for a file whose contents genuinely enter context, **so a legitimate
declaration can never be green.** ⛔ **That is the mirror failure — a FALSE RED — and a guard that cries wolf
gets ignored.** **Zero desks hit it today; it bites as desks declare.** ⇒ **Needs a severity split: advisory
findings must not enter the rc.** Carried to **9/14** with the other structural items; not attempted at the end
of this session, which is the register the reader just warned me about.

## VERIFICATION AFTER THE REPAIR
**CODEX fixtures vs the WORKING TREE: all 8 invocations correct** (malformed → rc 2/2 · missing file → 1/1 ·
invalid mode → 1/1 · invalid attestation → 2/2). **Selftest 44 → 59**, with six new legs driving PUBLIC paths and
asserting what a caller or a downstream parser sees. **Regression:** PROME/WALTER/BROCK/DAEDALUS rc 0 ·
CREED/LIQUID rc 1 (real, pre-existing) · fleet rc 1, five 🟠 rows unchanged and correctly marked · legacy rc 0 ·
usage rc 2 · local importer rc 0 · **`validate_all` 12 PASS, A9 green at 59/59, D1 advisory at 5/37.**

## STATE — **IMPLEMENTED · TESTED · COLD-READ ONCE · ONE ⚠️ CARRIED**
The cold read is the independent leg; its ❌ are closed and its W2 is declared and dated. **This file is now
CLOSED for the session** — it has had a repair, an independent read, and one ❌-fix pass, and a further edit is
the unreviewed-correction-pass this discipline exists to stop.

---

# 9. ⚠️ THE D1 REPAIR IS **PARTIAL** — rc 1 still collapses to PASS. **CARRIED to 9/14 (DOCKET L355). NO CODE TONIGHT.**

**CODEX re-audit, PROME-reproduced, and I reproduced it a third time before agreeing.** Drove
`leg_read_cap_fleet` directly with an **IDENTICAL summary line** in all three cases, varying only the child's
returncode:

| child rc | D1 state |
|---|---|
| 0 | PASS |
| **1** | **PASS** ← the remaining false-green |
| 2 | CANNOT-CERTIFY ← my repair, working |

**THE PATH:** a missing declared file produces a **manifest defect, rc 1, and ZERO over-budget files.** D1 reads
those zero counts and returns PASS, **dropping the defect.** It is the same shape I fixed at rc 2 — *a verdict
taken from the summary line rather than from the exit code* — **surviving at the next value up.**

## 🔑 CODEX's framing is right, and it is the lesson I reached one layer in on this same file hours ago
`res` never carried `problems`, so `main()` **inferred** why rc was 1 — and that inference produced the mark bug
**and** survived one line later in the label. I removed the inference rather than patching it.
**THIS IS THE SAME DEFECT AT THE PROCESS BOUNDARY.** D1 re-derives a reason from a **human-readable summary**
because the child **does not pass one across**. ⇒ **The structural fix is the one I already chose: PASS THE
REASON, NEVER RE-DERIVE IT — applied to the subprocess boundary rather than to a call.**

## ⛔ WHY I AM NOT FIXING IT TONIGHT — and why that is not inconsistent with overriding the earlier carry
Both calls turned on the same facts, which differ:

| | the READS repair (fixed) | this D1 partial (carried) |
|---|---|---|
| live or latent? | **LIVE** — three desks quoted the output that day | **LATENT** — verified: **0 manifest defects fleet-wide today**, D1 reports **ADVISORY 5/37 not PASS**, and `validate_all` is **still UNWIRED** into any boot or closeout step |
| my own written condition unmet? | **yes, C10** | no |
| independent fixture available? | **yes, CODEX's** | not for the fix |
| my defect rate on this file tonight | unknown | **demonstrated: I introduced a defect INSIDE the third repair** |

**The base rate is now against me on this file**, PROME asked explicitly and more strongly than last time, and the
path is latent. **A dated carry is the right answer and I am taking it.**

## ⛔ AND THE TRAP IN THE OBVIOUS FIX, which is why this needs a sitting and not ten minutes
**DO NOT make every rc 1 blocking.** That erases the **intentional advisory** treatment of the 5 over-budget
desks — all legitimate size backlog — and converts a backlog into a boot blocker. **That is the false-RED
direction, and I already have one carried and dated (W2/L354). Two false-REDs out of one repair would be worse
than the false-green they replaced.**

## ACCEPTANCE CONDITIONS FOR 9/14 — written now, in the defect's own terms (WQ-229)
**B1 — D1's verdict is derived from a MACHINE-READABLE reason the child EMITS, never re-derived from prose.**
The summary line is a human surface; a parser reading it for a verdict is the defect, at any rc value.
**B2 — MANIFEST DEFECTS and SIZE-BACKLOG FINDINGS are DISTINGUISHABLE in D1's output and get DIFFERENT
treatment.** A missing declared file is a defect someone must fix; 5 desks over budget is a tracked backlog.
Collapsing them in either direction is a defect: PASS on the first is a false green, BLOCKING on the second is a
false red.
**B3 — rc 1 never collapses to PASS**, and **rc 0 never becomes a finding.** The mapping is explicit and total
over {0,1,2} × {manifest defect present, absent}; **no cell is left to inference.**
**B4 — the advisory/delta-keyed behaviour of the size-backlog leg is PRESERVED EXACTLY** — 5/37 today stays
ADVISORY against its recorded baseline. Verified by diffing D1's output before and after on the live fleet.
**B5 — W2 is fixed in the same pass or explicitly not:** the `.py`/`.sh` advisory currently drives fleet rc 1, so
a self-described advisory is already blocking. **B2 cannot be satisfied while an advisory is indistinguishable
from a defect inside the child**, so these two are one piece of work, not two.
**B6 — tested at the PROCESS boundary**: drive `leg_read_cap_fleet` with a stubbed child across every (rc ×
reason) cell and assert the state, exactly as PROME's reproduction does. **Not at the parser. Not at the helper.**

**Registered: `PROME/DOCKET.tsv` L355 (9/14), beside L353 and L354.** Not riding on a message.

## RESIDUE THAT STAYS RESIDUE, restated so it is not absorbed
`scripts/pipeline_rc_guard.py` is **UNWIRED** (Will's call — wiring edits `.claude/settings.json`, not mine) and
**misses `set +o pipefail; <gate> | tail; echo "RC=$?"`** and **a command whose comment merely mentions
PIPESTATUS**. Both are recogniser gaps in a tool nothing depends on yet. **Not fixed, not absorbed, carried.**

---

# 10. 🔴 SIXTH INSTANCE, AT SHUTDOWN, IN MY OWN HAND — I COLLAPSED rc 2 INTO rc 1 AGAIN

Running the final pre-shutdown check I wrote a throwaway loop:
```
bash verify_push.sh "$s" >/dev/null 2>&1 || { f=$((f+1)); echo "  NOT ON ORIGIN: $s"; }
```
**It reported 32 of 32 commits NOT ON ORIGIN.** All 32 are on origin.

**`verify_push.sh` returns rc 2 CANNOT-CERTIFY — correctly — for a subject match older than its 60-minute
window**, because an old match is not evidence THIS session's work was pushed. That is a contract I wrote into
that file, in capitals, after it false-alarmed on its own second use. **My `||` treated every non-zero as
failure, collapsing CANNOT-CERTIFY into NOT-ON-ORIGIN.**

⛔ **This is the identical collapse I fixed in `validate_all` D1 two hours earlier, and carried as L355 because
it survived at the next rc value up.** Sixth instance in one session. And the sequence is the damning part:
**I wrote the three-state contract · I fixed the collapse in one tool · I found it surviving in another · I
registered a DOCKET row for it · and then I wrote it again, myself, in the last command of the session.**

**Ground truth, established properly:** `git merge-base --is-ancestor` on spot-checked commits → all ON ORIGIN;
`git log origin/master..HEAD` → **0 commits ahead.** Nothing was at risk; the alarm was mine.

🔑 **THE FINDING, and it is the one that should outlive every tool in this record: a three-state rc contract is
defeated by `||`, `and`, `if not`, and every other two-valued idiom in the language — so ANY three-state contract
is one careless line from being two-state at every call site, including its author's.** Writing `rc 0/1/2` in a
docstring does not make callers three-valued; **only a caller that names the states can be.** ⇒ Wherever rc 2
means CANNOT-CERTIFY, the call site must test `-eq 0`, `-eq 1`, `-eq 2` explicitly, never truthiness.
**That is the general form of L355 and it is bigger than L355.** Carried to 9/14 with it.

*(Recorded at shutdown rather than dropped. `finding_a_correction_pass_is_unreviewed_work` — and the corollary
this session earned six times over: the register that degrades is not the code, it is the throwaway line beside
the code.)*
