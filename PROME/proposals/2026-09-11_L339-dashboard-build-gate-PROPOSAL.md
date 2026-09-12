# L339 — a failed dashboard build leaves the gate certifying old state

**Status:** PROPOSED · **Opened:** 2026-09-11 23:1x ET (`prome-e2`, LAPTOP) · **Owner:** PROME
**Row:** `PROME/DOCKET.tsv` L339 (PENDING, dated 2026-09-12) · **Discipline:** WQ-229 repair-completion
**Lane:** Will 2026-09-11 23:11 — *"Go straight to L339 … Complete this bounded repair and verify both the failed-build case and a successful-build control."*

---

## 1. Acceptance conditions — written BEFORE any edit (WQ-229)

Stated in the defect's own terms, not as a restatement of the reported symptom. These **are** the test list.

| # | Condition |
|---|---|
| **A1** | A **failing build must not leave a passing gate.** After a build that returns rc=1, `prome_gate.py` must report a BLOCKING failure on the dashboard, not a pass. |
| **A2** | The **error list must reach the operator** on the run itself. Today the failing run prints `change baseline unchanged` and emits nothing on stdout or stderr; the errors are unreachable without patching the script. |
| **A3** | The gate must **refuse a `dashboard_state.json` older than the build it is certifying**, rather than reading whatever is on disk. |
| **A4** | **Control:** a successful build ⇒ the gate passes. The repair must not convert the normal path into a false alarm. |
| **A5** | The A3 refusal is keyed to a **content-derived vintage, never mtime.** Measured tonight: the live state file's mtime is `2026-09-11 20:10:20` while its own `built` field reads `2026-09-11 12:33` — an mtime-keyed guard would call it fresh. (Root `CLAUDE.md` Data Hygiene: never key a NEW freshness mechanism on mtime; git sync restamps it.) |
| **A6** | The gate distinguishes **"the last build FAILED"** from **"no build has been attempted"**. Both leave stale state on disk; they are different operator actions, and neither may read as a pass. |
| **A7** | A **`--no-snapshot` preview makes no claim** about the baseline and must not be recorded as either a success or a failure. |

## 2. Neighbours — CONSIDERED, per WQ-229 (consider, not perform)

| Category | Disposition |
|---|---|
| **Ordinary** | The success path — build ok, state written, gate green. **TEST** (= A4). |
| **Overlap** | A run that is both: a build that FAILS while the on-disk state is already current, and a build that SUCCEEDS after a failure (the record must flip back to ok, not latch). **TEST** — this is the category whose miss kept the external-review F1 open. |
| **Wrong owner** | `--no-snapshot` preview runs, which legitimately write no state and must not be mistaken for failures. **TEST** (= A7). |
| **Missing information** | No record on disk at all — a fresh clone, or the first run after this change. Must read UNKNOWN/blocking, never pass. **TEST** (= A6). |
| **Concurrent activity** | **N/A with reason:** Will runs one machine at a time and one closeout per session, so two concurrent builders are not a live shape. Mitigated anyway by writing the record via temp-file + atomic rename, so a torn read is not possible even if it happened. |

## 3. Mechanism — established at the code, reproduced 2026-09-11 23:1x

- `fleet_dashboard.py:1296` writes `dashboard_state.json` **only when `heartbeat_errors` AND `attention_errors` are both empty**; `:1303` returns 1 when either is non-empty.
- ⇒ a failing build **writes the HTML, leaves the previous state file untouched, and returns rc=1 silently.**
- `prome_gate.py:504 check_dashboard_state()` then reads whatever `dashboard_state.json` is on disk: panels-nonempty (BLOCKING) and vintage ≤72h (ADVISE) both pass over the stale file.
- **Reproduced:** rc=1 · stdout `wrote …; change baseline unchanged` · stderr empty · state file mtime **and** sha256 unchanged (`a9e22b8d…`).
- **Current cause of the failing build** (NOT this lane's work): HEARTBEAT carries two amendments, `PROME/HEARTBEAT_DASHBOARD.md` carries one projection ⇒ `heartbeat_projection.py:46` raises *"each HEARTBEAT amendment needs one reviewed dashboard projection."* Authoring Amendment #2's projection is Will-facing regime display text plus a `source_sha256` over the exact amendment paragraph — **separate work, deliberately not started here** (L339 col 6).

## 4. Two defects — NOT conflated (L339 col 2)

- **Defect A (code):** silent failure + the gate certifying stale state. Addressed by this repair.
- **Defect B (procedure):** the closeout runner treats *attempting* the build as sufficient. Confirmed at the text — `PROME/CLOSEOUT.md:55` and `PROME/.claude/skills/closeout/SKILL.md:6` both say to **run** the build; neither requires it to **succeed**. Reordering cannot fix this; the step must require successful production of the gate's input, or explicitly report that this validation branch did not complete.

## 5. Completion note — the four states, kept separate

*(WQ-229 refinement 1: supplied unprompted. Passing my own tests establishes IMPLEMENTED, never VERIFIED — `finding_adoption_is_not_validation`.)*

**IMPLEMENTED.** `fleet_dashboard.py`: `BUILD_PATH` + `write_build_receipt()`; `main()` records **STARTED-NOT-COMPLETED before doing any work**, runs `build()` **and the HTML write** inside one `try`, then records the real outcome only once every required output is finished; prints the error list to stderr on **any** failing run (preview included); writes no receipt at all on `--no-snapshot`.
⛔ **The first committed version (`c6889828f`) used an except-handler around `build()` alone, and that was too narrow twice over** — the HTML write happens after it (reproduced: `-o` into a missing directory raised, the handler never ran, the previous `ok:true` receipt survived, the gate passed), and no handler covers a process kill. Fail-closed-by-default is the only shape that covers both. **I had described this shape in-session and then committed the weaker one** — `[[finding_a_correction_pass_is_unreviewed_work]]`. `prome_gate.py`: `check_dashboard_build_receipt()` called from `check_dashboard_state()` on **both** gate paths (boot `:793`, closeout `:839`); BLOCKING on missing · unreadable · non-object · `ok:false` · stamp mismatch; returns a stale-note prefix prepended to the three checks that read the snapshot.

**TESTED.** `PROME/tools/tests/test_dashboard_build_receipt_L339.py` — **27 tests** (`grep -c 'def test_'`, measured), all passing. Falsified against pre-repair code: **23 of 24 detect the defect** (at the 24-test vintage); the 1 that passes is `test_A4_successful_build_gate_passes`, the control, by design. The 3 tests added in the second correction were falsified against the **committed** `c6889828f`: 2 of 3 detect the hole there, the third is the A7 control that must pass on both paths.
Live end-to-end, real tree: failing build ⇒ rc=1 · stderr carries the error list · state byte-identical (`a9e22b8d…`) · both gates BLOCK. Failing preview ⇒ errors now on stderr, no receipt. Crash ⇒ `ok:false` receipt, gate BLOCKS. Successful-build control ⇒ run in a throwaway `tar` copy with amendment count matched to projection count (**no Will-facing canon authored**): rc=0, empty stderr, both stamps agree, L339 check green, no new false alarm.

**INDEPENDENTLY VERIFIED — partially, and only after a second pass.** A `coldreader` that did not write the fix found **4 ❌ / 7 ⚠️** against v1. One (❌1, the crash path) I had found myself minutes earlier; **three I had not**, and one of those (❌2) was worse than the original defect. All four ❌ are fixed and re-verified above. ⚠️ **The reader has not re-read the corrected code** — its verdict stands against v1, so this line is *reviewed-and-repaired*, not *independently verified at the current artifact*.

**STILL UNRESOLVED.**
- **Defect B (the procedural half) — DELIBERATELY DEFERRED, not blocked.** `PROME/CLOSEOUT.md:55` and `PROME/.claude/skills/closeout/SKILL.md:6` still only require the build to be **run**, never to **succeed**. ⛔ **An earlier draft of this section called the amendment "blocked behind L338." That overstated L338, which requires the rotate-vs-hot/cold DECISION before the next amendment — not completion of the split** (`PROME/STATUS.md`: *"L338 asks PROME to DECIDE, not to perform the reduction"*). Nothing prevents the amendment; making the L338 decision first is a precondition I chose not to discharge inside tonight's bounded lane. The rationale for deferring: `CLOSEOUT.md` measures **30,863 B = 94.8%** of the 32,550 B read cap (`measure.py`), so the amendment should land *after* the rotate-vs-split decision shapes the file rather than push it closer to the ceiling first; and the mechanical guard now enforces the substance at both gates, which per WQ-229 ("prefer promoting or repairing an EXISTING control to adding a new one") is the stronger control. Carried to L338 as a deferral with this rationale, not as a blocker.
- **The build itself still fails**, for the unrelated reason in §3 (Amendment #2 has no projection). ⚠️ **Consequence to state plainly: every gate run now BLOCKS until that projection is authored.** That is the repair working, not a regression — but it has no in-lane remedy, because authoring it is Will-facing regime text plus a `source_sha256` and is explicitly out of lane (L339 col 2).

## 6. Declared residue — un-fixed ⚠️ from the independent read

*Fixed from the read: ❌1 ❌2 ❌3 ❌4, plus ⚠️5 (the mismatch message asserted a direction the code never computed), ⚠️8 (comment contradicted its own code) and ⚠️9 (a live measurement frozen into a source comment — my own violation of § Session Process Controls). Left standing:*

- **⚠️6 — `ok` and `v` read permissively.** `prome_gate.py` uses truthiness on `ok` and never checks `r["v"]`, though the writer emits `v:1`. Benign today: a v2 rename of `attempted` fails closed through the mismatch branch.
- **⚠️7 — the receipt records no output path.** A build to `-o /tmp/x.html` advances state + receipt and passes the gate while the published URL never moves. Consistent with `CLOSEOUT.md:37` ("does not certify the shipped state"), but the check's NAME invites the wider reading.
- **⚠️10 — second consumer unguarded.** `PROME/tools/will_brief.py:301` feeds Will's change feed from `dashboard_state.json` with no receipt awareness. The gate is fixed; the class is not closed at the Will-facing surface. **This is the one worth promoting to a row.**
- **❌4's decision, recorded:** the receipt is **committed alongside the state file**, which is tracked and rewritten ~3×/day. The alternative (gitignore) would block the first boot after every desktop⇄laptop switch. The runner-text half of ❌4 — naming the receipt in `CLOSEOUT.md` step 6 — is blocked behind L338 with Defect B.
