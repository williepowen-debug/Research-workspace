# `daedalus_gate.py` — build record 2026-09-17 (drills run at build; §3(a)/(b)/(e) real cases; re-run at every version)

**Spec:** `design/2026-09-17_DAEDALUS_GATE_SPEC.md` (acceptance set A1–A12 written before the code). **Authority:** Will "approved go ahead" 20:4x ET on CATO `87776263a` step 2. **Version:** first build, HEAD `b6af73050` + working tree.

## What the first real runs found — in the runner itself (PAT-146: a selftest proves what its author enumerated)
| # | Defect | How found | Fix |
|---|---|---|---|
| 1 | PATTERNS_HOT conservation counted **178** rows vs the index's 179 — regex `PAT-\d+\t` missed `PAT-074b` (letter-suffixed ID) | first REAL closeout run: false BLOCKING on a file that regen had just certified 104+75==179 | `PAT-\d+[a-z]?\t`; clean line watched afterwards (`179 rows == 104+75`) |
| 2 | selftest's receipt drill (A3) verified against the CWD repo, not the fixture repo — reported HEAD moved and FAILED | first selftest run | `verify_receipt(path, root=None)`; selftest passes the fixture root |
| 3 | my own drill command read the selftest's rc THROUGH A PIPE (`… \| tail -25; echo $?` printed `rc=0` over a FAIL) — CHECK_STANDARD §14(b) in the author's hand, on the tool built to enforce it | noticed on the printed `selftest rc=0` beside `SELFTEST FAIL` | drills re-run with output to a file and rc read bare |

## Drill results (all bare rc)
| Spec item | Drill | Watched |
|---|---|---|
| A1 omitted/missing step visible | selftest T4 `/nonexistent/check.py` | `❓ T4 UNKNOWN — child not runnable: [Errno 2]…`; overall rc 2 |
| A2 unreadable input stays UNKNOWN | selftest T2 (rc 2) · **REAL:** `boot` B1 — sweeps_due rc 2 (profile_clock CANNOT-EVALUATE HENRY/HOMER/OSPREY) | `❓ B1 UNKNOWN` with the child's own `🔴 sweeps_due CANNOT-CERTIFY` line; boot rc 2 |
| A3 source change invalidates receipt | selftest: fixture repo → `✅ VALID` → file appended → `❌ INVALIDATED — tree changed` | both lines |
| A4 skipped conditional carries a reason | closeout C2 without declaration → `❓ UNKNOWN — UNDECLARED — pass --no-superseded or --superseded OLD NEW`; with `--no-superseded` → `— NOT-APPLICABLE — declared: no figure superseded` | both lines (selftest + real) |
| A5 pipe-proof | selftest T3 prints `✅ clean`, exits 1 | `❌ T3 BLOCKING` — class keyed on rc, not text |
| A6 unrelated work untouched | `git status --porcelain` before/after real boot and real closeout | delta = `?? AGENTS/DAEDALUS/runs/GATE_LOG.tsv` only; PROME's and CATO's dirty paths untouched |
| A7 receipt names what was checked | receipt JSON `steps[]` id·cmd·rc·class·reason·log; perimeter line names B0/B3 (boot) and C10 (closeout) as NOT checked | read |
| A8 DUE ≠ FAIL | selftest `selftest-due` run (CLEAN + DUE) → rc 0 · **REAL:** closeout C3 ledger nudge rc 1 → `⏰ DUE`, did not move rc | both |
| A9 §3(a) flag on a REAL defect | `closeout --complete-since 2026-08-17` (range holds 27 pairing violations incl. `383051aeb`) | `❌ C8 BLOCKING` |
| A10 §3(b) clean on REAL clean cases | `corrections_boot_check DAEDALUS` rc 0 · `read_cap_check --agent DAEDALUS` rc 0 · C1 orphan clean · C5 claim_check clean · C9 STATUS stamped today | `✅` rows |
| A11 no pipe / no `2>/dev/null` | source: every child via `subprocess.run(list, stderr=STDOUT)`; no `shell=True` | grep-verified |
| A12 content check on a diverged origin | selftest: bare origin, push (`CLEAN`), overtake from a clone (`BLOCKING — origin/master ≠ HEAD on 1 path`) | both |

**Overall rc composition watched:** UNKNOWN dominates (boot rc 2 with two CLEAN rows beside it); BLOCKING → 1 (A9 run without the UNKNOWN would be 1 — tonight every closeout carries the profile-clock UNKNOWN, so rc 2 is the honest verdict until the 9/25 profile queue clears it).

## What it does NOT prove (perimeter, §2)
Completion of work beyond complete_check's legs · owner consumption of packets · the truth of any DECLARED value (`--rule-declared`, `--no-superseded`, `--no-memory`) · anything a child's own PASS line disclaims (e.g. read_cap's "heuristic perimeter" until the READS attestation lands). The DECLARED steps are the place the runner can be lied to by its operator; that is why they print as DECLARED, never CLEAN.

## Wiring
Charter SPAWN 5 (`boot`) and SPAWN 9 (`closeout`, then `verify --subject` after safe-push) — pointer edit lands with the compaction commit. Not a shared `scripts/` check ⇒ no CHECKS.tsv row; the BASIS row in the READS declaration names it as boot-defining.
