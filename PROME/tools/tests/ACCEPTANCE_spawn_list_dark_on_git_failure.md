# ACCEPTANCE CONDITIONS — `spawn_list.py` reports DARK on a failed `git log`
**Written 2026-09-12 BEFORE the edit** (WQ-229 repair-completion discipline). Defect raised by DAEDALUS at the 9/12 TOOLING/WIRING sitting (L294 origin-proof sweep), verified by PROME at `PROME/tools/spawn_list.py:107`.

## The defect, in its own terms
`Liveness.last_self_commit()` runs `subprocess.run(...)` and reads **only `.stdout`**. The `returncode` is never inspected. A `git log` that FAILS returns empty stdout ⇒ `hit = None` ⇒ `classify()` returns **`DARK`** with basis *"no self-commit found in history"*.

**Why that is not cosmetic: `DARK` at a due row IS the WQ-184 Tier-1 spawn trigger.** A git failure therefore reads as *"every owner is dark"* and authorises spawning all of them. This is a fail-OPEN in the driver that spawned six desks today.

⚠️ **Not a restatement of the symptom:** the symptom is "wrong class on failure". The defect is **an instrument that cannot distinguish *no evidence* from *could not look*, in a position where the two have opposite consequences.**

## Acceptance conditions — the repair must hold ALL of these
1. **A git failure (rc ≠ 0) MUST NOT produce `DARK`.** It produces a distinct class that does not trigger a spawn.
2. **A genuine empty result (rc = 0, no matching commits) MUST STILL produce `DARK`.** That is a real signal, not an error, and the repair must not blunt it.
3. **The two are distinguishable in the rendered output** — a reader can tell *"never committed"* from *"could not check"* without reading the code.
4. **The unknown state is NOT silently clean:** it is flagged in the output and moves the exit code, so it cannot pass as a quiet all-clear.
5. **`--selftest` covers the failure path.** It currently passes 11/11 *without* exercising it, which is how the defect survived.

## Neighbours CONSIDERED (WQ-229 five categories; consider, not perform)
- **ordinary** — rc=0 with commits ⇒ ACTIVE/DARK by date. Already covered by the 11 existing selftest checks; must stay green (regression).
- **overlap** — a desk with no commits AND a failing git call ⇒ **UNKNOWN wins; the error dominates the absence.** Tested.
- **wrong owner** — `owner_token()` returns `"?"` on an unparseable owner cell; the grep then legitimately finds nothing and the row reads DARK, i.e. a parse failure wearing a liveness verdict. **Same fail-open class, in scope, fixed here.** Tested.
- **missing information** — rc=0 + empty is exactly condition 2; that is the case the repair must NOT break. Tested explicitly.
- **concurrent activity** — **the realistic trigger.** Six desks shared one `.git` today; `git log` failing under `index.lock` contention or a transient object-store error is an rc≠0 case, so condition 1 covers it. This is why the defect matters in practice rather than in principle.

## Incidence on today's spawns — CLOSED, not left unknown
DAEDALUS asserted nothing about today's four L0 spawns. PROME closes it from the saved boot receipt `/tmp/prome-boot-prome-f1/checks/26-spawn-list-*.txt`: **`grep -c 'no self-commit found in history'` = 0**, and **8 of 8 rows carry a real `(Nd ago, <sha>)` basis**. ⇒ **The failure path was NOT taken at the 2026-09-12 boot.** Today's six spawns are unaffected.

## Completion states (WQ-229 — these are distinct and will not be merged)
IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED · STILL UNRESOLVED.
