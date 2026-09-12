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
