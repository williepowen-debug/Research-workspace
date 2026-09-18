# `daedalus_gate.py` — thin runner over the existing boot/closeout checks (spec + acceptance set, written BEFORE the code)

**Authority:** Will "approved go ahead" 2026-09-17 20:4x ET on CATO `87776263a` step 2 ("one thin runner, reusing the current checks … a wrapper that merely prints a green aggregate is insufficient"). **Owner:** DAEDALUS. **Home:** `AGENTS/DAEDALUS/scripts/daedalus_gate.py` (agent-local; not a `scripts/` shared check, so no CHECKS.tsv row — it is invoked by this desk's own charter, SPAWN 5 and 9).

**PRIOR-ART LINE (CHECK_STANDARD §13):** symptom "boot/closeout steps run from a remembered list; no record of what applied, ran, failed or stayed unknown" searched against `MEMORY.md`, `INDEX_COLD*.md`, `PATTERNS_HOT.md` (bodies grepped) — HITS: PAT-125 (a boot sequence is an untested guard) · `finding_mechanize_the_cap_not_the_ritual` · PAT-110 (always-0 shared check) · PAT-167 (three-state rc carrying a one-bit reason is defeated at every call site) · PAT-131 (reporting gated on an orthogonal state) · CHECK_STANDARD §14(b) (a pipe reports the last command's rc). In-fleet prior art: `PROME/tools/prome_gate.py` (record/guard/severity classes) and `PROME/tools/boot_session.py` (one receipt per run directory). Not novel; this is their DAEDALUS-local form, deliberately smaller.

## 1. What it is, and is not
- An ORCHESTRATOR. It invokes the checks the charter already names, each as a direct subprocess (no shell, no pipe), captures each child's **native rc** and log, maps rc → a **class** using that child's OWN documented contract, and writes a receipt. It adds two read-only checks of its own that no child covers (PATTERNS_HOT conservation; STATUS stamped today) and records two declarations (consumer-check scope; rule-declared-this-session).
- It does **not** commit, push, regenerate, rotate, or edit any file outside its receipt directory and `runs/GATE_LOG.tsv` (one appended row per real run). Commit and push stay separate, by hand, per root Git Protocol.
- A green aggregate is not its output. Its output is the per-step table plus a §2 perimeter line.

## 2. Classes (five, kept distinct — CATO's requirement)
| Class | Meaning | Moves rc? |
|---|---|---|
| `CLEAN` | child rc 0 | no |
| `DUE` | child reports OWED WORK (sweeps_due rc 1 = a sweep is due; orphan_check `[likely YOURS]`; ledger nudge rc 1; consumer_check 🔴 owners; memory-length rc 1/2 = flag PROME) | **no** — listed loudly; the closeout message must carry it |
| `ADVISORY` | child rc 1 whose contract says advisory (claim_check; read_cap at BOOT) | no |
| `BLOCKING` | child rc 1 whose contract means a defect the desk must fix before closing (corrections unreceipted; read_cap at CLOSEOUT; complete_check pairing/symmetry/placement; memory_index_check --strict; verify_push NOT-ON-ORIGIN; PATTERNS_HOT conservation broken) | rc → 1 |
| `UNKNOWN` | child rc 2, child missing/unrunnable/timeout, an UNDECLARED conditional, or a runner-internal read failure | rc → 2 (**dominates**, §9) |
| `NOT-APPLICABLE` | a conditional step skipped under an EXPLICIT declaration, reason printed | no |
| `ENUMERATED` / `DECLARED` | listings (inbox, git state) and operator declarations — recorded, not graded | no |

Overall rc: **2** if any UNKNOWN · else **1** if any BLOCKING · else **0**. DUE never lowers to "clean" and never raises to "fail"; it is the third thing.

## 3. Step registry (in the SCRIPT — the charter names the runner, the runner owns the list)
BOOT: git-state (fetch · ahead/behind · dirty-outside-own-dir) → `sweeps_due.py` → `corrections_boot_check.py DAEDALUS` → inbox enumerate (with positive control: the directory exists and was listed) → `read_cap_check.py --agent DAEDALUS` (ADVISORY at boot).
CLOSEOUT: `sweeps_due.py` (self-row · directory-stale) → `orphan_check.sh DAEDALUS` → consumer_check (declaration-gated) → `ledger_staleness.py --nudge DAEDALUS` → memory (`memory_index_check --strict --slug` per declared slug, or `--no-memory`; `check_memory_length.sh` always) → `claim_check.py --check weekday <existing paths>` → PATTERNS_HOT conservation (read-only) → `read_cap_check.py --agent DAEDALUS` (BLOCKING) → `complete_check.py` → STATUS stamped today → rule-declared (DECLARED).
VERIFY (post-push): `verify_push.sh "<subject>"` → content check: every path of the located commit compared `origin/master:<p>` vs `HEAD:<p>` by sha256.

## 4. Receipt
`<receipt-dir>/<UTC-stamp>_<mode>.json` + `logs/<step>.txt`. Fields: mode · ts · HEAD · **fingerprint** (sha256 over HEAD + `git diff HEAD -- AGENTS/DAEDALUS scripts` + sorted untracked list under AGENTS/DAEDALUS + sha256 of the runner file) · steps[] {id, name, cmd, rc, class, reason, log, finding lines} · counts by class · perimeter line. `verify-receipt <path>` recomputes the fingerprint: `VALID` or `INVALIDATED (head|tree|runner changed)`. Default receipt-dir = the session scratchpad (`$CLAUDE_SCRATCHPAD` or `/tmp/claude-1000/daedalus-gate/`); receipts are NOT committed — the one-row `runs/GATE_LOG.tsv` append is the committed trace (date · mode · HEAD7 · rc · counts · receipt sha8).

## 5. Acceptance set — each item names its drill; §3(a)/(b)/(e) real cases named by path
| # | Requirement (CATO) | Drill | Expected |
|---|---|---|---|
| A1 | an omitted mandatory step is visible | selftest: registry entry whose command path does not exist | row printed `UNKNOWN — child not runnable`, rc 2 |
| A2 | missing/unreadable input stays UNKNOWN | selftest child exits 2; REAL: tonight's `sweeps_due` (profile_clock rc 2 on HENRY/HOMER/OSPREY) | `UNKNOWN`, rc 2; the real run prints the child's own CANNOT-CERTIFY line |
| A3 | a source change invalidates the receipt | selftest: temp git repo → receipt → modify a file → `verify-receipt` | `INVALIDATED (tree changed)`; unchanged → `VALID` |
| A4 | a skipped conditional carries a reason | closeout without `--no-superseded`/`--superseded` → UNKNOWN `UNDECLARED`; with `--no-superseded` → `NOT-APPLICABLE — declared: no figure superseded` | both lines watched |
| A5 | a failing child cannot be hidden by a pipe | selftest child prints `✅ clean` and exits 1 | class keyed on rc → BLOCKING, not on text |
| A6 | unrelated active work untouched | `git status --porcelain` before/after a real closeout run: identical except `runs/GATE_LOG.tsv` | diff shows only that path |
| A7 | a positive receipt names exactly what was checked | receipt.steps lists id · cmd · rc · class for every registry entry; perimeter line names judgment steps as NOT checked | read the JSON |
| A8 | child rc semantics preserved (DUE ≠ FAIL) | REAL: `sweeps_due` rc 1 when a sweep is DUE (reproduce with `--registry` fixture inside selftest) | class `DUE`, overall rc unchanged by it |
| A9 | §3(a) flag line on a REAL defect | `complete_check.py --since 2026-08-17` range containing the known pairing violation `383051aeb` | BLOCKING row with the child's violation line |
| A10 | §3(b) clean line on a REAL clean case | tonight's `corrections_boot_check DAEDALUS` rc 0; `read_cap_check` rc 0 | CLEAN rows |
| A11 | §14 no pipe, no `2>/dev/null` on an absence-bearing scan | code review of the runner: every child via `subprocess.run(list)` with stderr merged into the log | grep the source |
| A12 | verify content check catches a divergent path | selftest: temp repo with a bare "origin", push, then amend a file on origin's branch | `BLOCKING — origin/master:<p> ≠ HEAD:<p>` |

Selftest is `--selftest`; the real-case drills (A2, A6, A8-real, A9, A10) are run by hand at build and their output pasted into the build record `runs/2026-09-17_DAEDALUS_GATE_BUILD.md`.

## 6. Perimeter line (§2) — printed on every run
`GATE <mode> rc=<n> · checked: <k> steps [<ids>] · NOT checked: <judgment ids> · proves nothing about: completion of work beyond complete_check's legs, owner consumption of packets, the truth of any DECLARED value, or anything a child's own PASS line disclaims.`
