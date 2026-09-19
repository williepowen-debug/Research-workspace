# INDEPENDENT VERIFICATION — presence reader / spawn_list producer contract
**Reader:** independent (did not write the repair) · **Date:** 2026-09-19 · **Repo:** read-only, zero edits
**Under review:** uncommitted diff in `PROME/tools/` (spawn_list.py `Row` · session_presence.py `_field`/`guarded_main` · prome_gate.py rc=2 rendering)
**Verdict:** ❌ 3 · ⚠️ 6 · ✅ 6 — **IMPLEMENTED, TESTED (author), NOT INDEPENDENTLY VERIFIED.** Two blocking code findings + one blocking record finding.

Every finding below was RUN. Scratch scripts: `/tmp/cx/`. I did not run the author's suite as evidence of anything.

---

## ❌ BLOCKING

### ❌1 — The new blanket rc=2 rendering mislabels a neighbouring gate check that RAN, and prints "establishes nothing" directly above a live Tier-1 spawn candidate
| field | content |
|---|---|
| **claim** | `prome_gate.run_script()` now renders **every** rc=2 as "DID NOT RUN (UNKNOWN execution — establishes nothing)". `spawn_list.py` — the check the gate runs **immediately before** `session_presence` in the same boot — returns rc=2 for a run that completed and produced findings. The repair did not remove the rc collision; it moved it from rc=1 to rc=2. |
| **artifact** | `PROME/tools/prome_gate.py:286` (`state = "DID NOT RUN (UNKNOWN execution — establishes nothing) · " if p.returncode == 2 else ""`) vs `PROME/tools/spawn_list.py:322` (`return 2 if n["UNKNOWN"] else (1 if n["DARK"] else 0)`) and `:319-321` (`⛔ … NEVER spawn on UNKNOWN — fix the read, then re-run. A failed check is not evidence a desk is dark.`). Gate wiring: `prome_gate.py:1275-1278` (spawn_list, ADVISE, ok_rc=(0,)) and `:1282` (session_presence). |
| **verification** | Fixture DOCKET with ONE unparseable owner cell + ONE due row owned by a desk with no self-commit → `python3 PROME/tools/spawn_list.py --docket /tmp/cx/docket_mix.tsv --gates /tmp/cx/gates_empty.tsv --as-of 2026-09-19; echo RC=$?` → then that exact stdout+rc fed through the real `prome_gate.run_script` (`/tmp/cx/e7.py`). |
| **observed** | `RC=2` on `… 2 row(s): DARK 1 · ACTIVE 0 … ⛔ UNKNOWN 1`. Gate renders verbatim:<br>`rc=2 · DID NOT RUN (UNKNOWN execution — establishes nothing) · ⛔ 1 row(s) UNKNOWN: liveness could not be established (failed git log, or an unparseable owner cell). ⛔ NEVER`<br>`       ↳ ⚠️ D:L2  2026-09-19  0  ZZTOP  DARK  no self-commit found in history …`<br>The check ran, listed every due row, and found a **DARK row at its date** — under WQ-184 L0 that IS the Tier-1 spawn trigger — and the summary line above it now tells PROME the result establishes nothing. Rendered **identically** to a genuine did-not-run (CASE D in `/tmp/cx/e5_render.py`). |
| **contradicted canon** | `AGENTS/DAEDALUS/BLUEPRINTS/CHECK_STANDARD.md:80` (RATIFIED): *"0 clean · 1 findings · **2 cannot-certify**"*; `:83` *"rc-2 = the check cannot certify its scope — treat as leg failure"*. rc=2 is **cannot-certify**, not **did-not-run**. `session_presence.py:151` cites "CHECK_STANDARD §9 rc convention" while `:149` restates it as *"rc 2 = the CHECK DID NOT RUN (we did not look)"* — narrower than the standard it cites. `CHECK_STANDARD.md:84`: *"revising a shared check's rc contract means editing the producer AND every rc-keyed consumer in ONE batch… **Survey consumers BEFORE changing the contract**."* The acceptance doc's neighbour table (`ACCEPTANCE…md:26-32`) enumerates no other rc-2 producer. |
| **blast radius** | Other gate-wired rc-2 producers: `scripts/docket_view.py:16-22,33` (rc 2 = ragged DOCKET / missing marker, no write) run at `prome_gate.py:1243,1297`; `PROME/tools/willq_view.py:198,338-339` (rc 2 = "no marker block … run --write first") run at `:1251,1312`; `scripts/position_agreement_check.py:156,160` (**BLOCK** severity) run at `:1211,1291`. Repo-wide, 42 files under `scripts/` + `PROME/tools/` reserve rc 2. |
| **proposed change** | Either scope the new text to the one tool whose rc-2 means did-not-run (pass a flag/`ok_rc`-style parameter per call site), or reword to the standard's own term — "CANNOT-CERTIFY (scope not established; not a pass and not a clean finding)" — and let each tool's own tail explain which. Do not assert "establishes nothing" over another tool's findings. |

### ❌2 — A3 holds only for exceptions raised INSIDE `main()`. An import-time crash still exits 1 and still renders as the stale-snapshot verdict
| field | content |
|---|---|
| **claim** | `guarded_main()` lives *inside* the module, so it cannot catch anything raised while the module's own imports execute. Any failure in `session_bridge` / `spawn_list` / `desk_activity` / `session_identity` / the transitive `docket_view` — or a SyntaxError in `session_presence.py` itself — exits **1**, the same not-ok rc=1 verdict a merely-stale snapshot produces. The repaired defect's family is "a sibling module changed"; the next member is "a sibling module will not import", and the guard does not cover it. |
| **artifact** | `PROME/tools/session_presence.py:3-12` (module-level imports) vs `:148-160` (`guarded_main`) and `:163-164`; the anticipated trigger is annotated in the dependency itself — `PROME/tools/spawn_list.py:71`: `from docket_view import state_kind  # noqa: E402 — fail LOUD if it moves; never fall back to a local copy`. |
| **verification** | Faithful sandbox replica (no repo edits): copied `PROME/tools/*.py`, `scripts/*.py`, `PROME/DOCKET.tsv|GATES.tsv|ROSTER.md` into `/tmp/cx/sbx`, `git init`, ran `python3 PROME/tools/session_presence.py` before and after `mv scripts/docket_view.py scripts/_moved_docket_view.py`. Then fed both real stdouts + rc through the live `prome_gate.run_script` (`/tmp/cx/e5_render.py`). |
| **observed** | `rc_with_docket_view=1` (stale snapshot) · `rc_after_move=1` (**ModuleNotFoundError traceback**). Gate renders:<br>CASE A crash → `advisory … ok=False … "rc=1 · ModuleNotFoundError: No module named 'docket_view'"`<br>CASE B stale → `advisory … ok=False … "rc=1 · Full due-row view complete; source/coverage gaps remain UNKNOWN."`<br>Same severity, same rc, same `ok=False`; only the trailing tail text differs — which is exactly the distinction the acceptance doc itself declares insufficient at `ACCEPTANCE…md:22` ("the gate printed the traceback AND assigned the same … verdict"). Secondary confirmation: running the real file with cwd outside a git repo (`cd /tmp && python3 …/session_presence.py`) also exits **1** on the same import, because `spawn_list.py:53` resolves ROOT from `git rev-parse` in the caller's cwd. |
| **proposed change** | Move the guard outside the import surface: a 6-line launcher (`try: import session_presence; rc = session_presence.main() except BaseException: … rc = 2`) invoked by the gate, or wrap the four imports in the same try that returns 2. Until then, state in the acceptance doc that A3 covers runtime-only crashes. |

### ❌3 — The acceptance record (the WQ-229 provenance artifact) misdates the origin commit by five days; the defect window is hours, not days
| field | content |
|---|---|
| **claim** | The record says the field landed on 2026-09-14. Git says 2026-09-19 12:08:59 -0400 — **today**, author date and committer date alike. The claim "it crashed at every boot" therefore describes ~5 hours and at most one or two boots, not 5 days of blind boots. The wrong date has already propagated into the verification brief I was spawned with. |
| **artifact** | `PROME/tools/tests/ACCEPTANCE_presence_reader_contract_2026-09-19.md:10` — *"`40aed8915` (the **2026-09-14** desk-cadence wire, ruled WQ-269) added a 7th element to each row"*. |
| **verification** | `git log -1 --format="as=%as cs=%cs" 40aed8915` and `git show 40aed8915 --format="%h %cs %s" --stat` |
| **observed** | `as=2026-09-19 cs=2026-09-19`, `author_date=2026-09-19 12:08:59 -0400`; subject `PROME: five Will rulings recorded and executed — YURI seated, cadence wired, five rows registered`. |
| **proposed change** | Correct the date in the record and re-state the exposure window in the completion note. A date beside a sha is a load-bearing claim (`finding_exact_level_authenticates_a_wrong_direction` — the correct sha authenticates the wrong date beside it). |

---

## ⚠️ REAL, NOT BLOCKING

### ⚠️1 — The repair converts a LOUD width error into a SILENT wrong column for any non-`Row` row, at rc=0 "clean"
- **claim** — the old 7-way unpack raised `ValueError` on any row of the wrong width (that loudness is what surfaced this very defect). `_field` accepts any row of width ≥ 5 and, when named access is unavailable, silently reads whatever sits at the hard-coded index. Wrong failure direction (`CHECK_STANDARD.md:49` §6).
- **artifact** — `PROME/tools/session_presence.py:65-70`, `:107-108`; live plain-tuple caller: `PROME/tests/test_boot_hardening.py:117` (`[(f"D:L{i}", "2026-09-09", 0, "BRENT", "DARK", "old commit", "due") …]`).
- **verification** — `/tmp/cx/e6_silent.py`: an 8-field **plain tuple** with one field inserted before index 3, passed to `SP.report()`.
- **observed** — `owner read -> 'HIGH'` (true owner `TERRY` at index 4), `class read -> 'TERRY'` (true class `ACTIVE`), **rc = 0**, emitted row `D:L9  2026-09-19  HIGH  TERRY  {…"current_presence": "UNKNOWN"…}` — a phantom desk "HIGH" reported as clean. Not blocking: the production caller (`session_presence.main():133`) always passes `Row` instances, where named access wins.
- **proposed change** — make the index fallback loud: raise (→ rc 2) on a row that is neither a `Row` nor a declared legacy width, or assert `len(row)` against a registered set.

### ⚠️2 — `Row`'s "APPEND at the END" rule is unenforced, and the commit it commemorates INSERTED
- **claim** — `_field`'s index fallback is sound only under append-only evolution; the producer's own history shows the discipline is not followed.
- **artifact** — `PROME/tools/spawn_list.py:235-238` (*"⛔ APPEND new fields at the END"*).
- **verification** — `git show 40aed8915 -- PROME/tools/spawn_list.py | grep -E "^[-+].*rows\.append"`
- **observed** — `- rows.append((…, cls, basis, re.sub(…)[:72]))` → `+ rows.append((…, cls, basis, _note(owner), re.sub(…)[:72]))`: `cadence` was inserted at index 6, **before** `catalyst`. The rule is a comment with no test and no check.
- **proposed change** — a one-line drill in the suite asserting `Row._fields[:8] == (…)` so a future insertion fails the test rather than a future boot.

### ⚠️3 — `main()` still reads the producer row positionally; one file now holds two different readings of the same field
- **claim** — A2's letter ("must not positionally unpack the producer's full row") is met; its stated contract ("Named access is the contract") is not. `report()` and `main()` can disagree about who owns a row.
- **artifact** — `PROME/tools/session_presence.py:135` — `owners = sorted(set(args.desk) | {r[3] for r in rows if r[3] not in ("WILL", "?")} | {"PROME"})`, which is what feeds `desk_activity.desk_path()` / `session_identity.collect()`.
- **verification** — `/tmp/cx/e8_main.py` on a 9-field NamedTuple with a field inserted before `owner`.
- **observed** — `report()'s named read -> TERRY` · `main()'s positional r[3] -> HIGH`. Same row, two owners, one file.
- **proposed change** — route line 135 through `_field(r, "owner", 3)`.

### ⚠️4 — The author's suite never exercises the gate half of the repair; A3 is a claim about the boot SUMMARY verified at `session_presence`'s exit code
- **claim** — A3 is worded about the *boot summary*; the only A3 test is a subprocess that monkeypatches `SP.main` and reads an rc. `prome_gate.run_script` is never imported or called anywhere in the suite. This is how ❌1 got through.
- **artifact** — `PROME/tools/tests/test_presence_reader_contract.py:61-70`; `ACCEPTANCE…md:18` ("The boot summary DISTINGUISHES…").
- **verification** — `grep -n "prome_gate\|run_script" PROME/tools/tests/test_presence_reader_contract.py`
- **observed** — no match. `finding_record_of_an_action_is_not_the_action` — the passing test is scoped to what it inspects, not to the condition's subject.
- **proposed change** — one drill that calls `run_script` with stub commands exiting 0/1/2 and asserts the three rendered strings differ from one another AND that a rc-2-with-findings tool is not described as establishing nothing.

### ⚠️5 — `_field`'s `str()` coercion and `getattr` fallback have two latent traps
- **claim** — (a) a named field whose legitimate value is `None` yields the literal string `"None"`, which flows on into `evidence()`; (b) `getattr` on a plain tuple for a name that collides with a tuple method returns a bound method, which `str()` happily renders as data. Neither name is in use today ({key,due,owner,cls}), so this is latent, not live.
- **artifact** — `PROME/tools/session_presence.py:67-70`.
- **verification** — `/tmp/cx/e1_field.py`.
- **observed** — `_field(Row(…owner=None…),'owner',3) -> 'None'` (and then `evidence()` builds `AGENTS/None` and emits a desk row for a desk called "None"); `_field(plain,'index',3) -> '<built-in method index of tuple object at 0x…>'`; `_field(plain,'count',3) -> '<built-in method count …>'`. Also: for a row where the named read returns `None` but position N holds a different field, the fallback returns the **wrong field's value** — `_field(reordered,'owner',3) -> 'ACTIVE'`.
- **proposed change** — use a sentinel (`getattr(row, name, _MISSING)`) so a legitimate `None` is not treated as "field absent", and reject non-str fallbacks.

### ⚠️6 — Category 5 (concurrent activity) N/A is correct about the row shape and wrong about the repair as shipped
- **claim** — the justification at `ACCEPTANCE…md:32` reasons only about the producer/consumer **row shape** ("independent of how many sessions are live") — true. But the repair also changed an **rc contract and its rendering**, and the documented realistic trigger for the mislabelled rc=2 state is literally concurrency.
- **artifact** — `ACCEPTANCE…md:32` vs `PROME/tools/spawn_list.py:121-125` — *"FAIL CLOSED… Realistic trigger: **index.lock contention on the shared .git while several desks commit**"* → `classify()` returns class `UNKNOWN` (`spawn_list.py:222-223`) → `render()` returns 2 (`:322`) → ❌1's mislabel.
- **verification** — reading the two artifacts + ❌1's run.
- **observed** — concurrent desk commits are the production route into the exact state the new rendering describes as "DID NOT RUN … establishes nothing". The N/A dismissal is scoped to half of what shipped.
- **proposed change** — re-word category 5 to N/A **for the row shape**, TEST for the rc contract.

---

## ✅ CHECKED AND SOUND (things I tried that did NOT break)

- **✅a A1 against the REAL due-row set (my own run, not the suite).** `python3 PROME/tools/session_presence.py` → rc=0; `grep -c "^D:L\|^G:"` → **18** evidence lines; `python3 PROME/tools/spawn_list.py --horizon 0 --tsv` → `18 row(s)`. Counts agree, completion marker `Full due-row view complete` present, no traceback.
- **✅b A5 guarantees intact.** `spawn_authorized` is hard-coded `False` at all three emit sites (`session_presence.py:62, 95, 110`); the real run emits `"spawn_authorized": false` 21×, zero `true`. The only `offline` hit in the whole output is the disclaimer line 6 ("quiet files do not mean an offline desk"). No `"ABSENT"`. The repair grants no authority it did not have and asserts no absence.
- **✅c `Row` is tuple-compatible for every consumer I could find (I enumerated them myself, ignoring the brief's list).** `grep -rln "import spawn_list\|spawn_list\."` → 8 files. Ran all of them: `PROME/tests/test_boot_hardening.py` **OK 11 tests** (and its fixture is a legacy **7-field plain tuple** — the backward-compat path works), `PROME/tests/test_presence_activity.py` **OK 12**, `PROME/tools/tests/test_spawn_list_fail_closed.py` **PASS 15/15**, `PROME/tools/tests/test_docket_open_query_L368.py` **OK 9**, `AGENTS/CATO/runs/2026-09-19_1725_prome-boot-fixes-probe.py` **rc=0, `producer width: 8`, all three cases complete**, `reviews/evidence-2026-09-12/argus_recheck.py` **rc=0**. Nothing broke. (CATO's files read and run only — not edited.)
- **✅d No new green.** `run_script`'s `ok_rc=(0,)` is unchanged (`prome_gate.py:272, 281`); rc=2 is still `ok=False` and still flags. The repair adds no path where a non-zero becomes a pass. The gate's pass/fail behaviour is unchanged — ❌1 is a *text* defect, but the text is what PROME reads.
- **✅e A speculation I chased and killed:** "a crash AFTER `report()` printed the complete table would be labelled DID NOT RUN". `main():144-145` dereferences `d["complete"]`; I checked `desk_activity.py:129` and `:131` — **both** construction branches set `"complete"`, so the KeyError I was hunting is not reachable there. Reported as a null result because I ran it.
- **✅f argparse/usage errors already agree with the new contract by accident.** `ap.error()`/`--bad-flag` raise `SystemExit(2)`, which is a `BaseException` and slips past `except Exception` — landing on rc=2 anyway. Correct outcome, but it is luck, not design: a sibling that calls `sys.exit(1)` would land on rc=1. (Checked: none of `session_bridge.py`, `desk_activity.py`, `session_identity.py` calls `sys.exit`; `scripts/docket_view.py:658` does, but only under `__main__`.)

---

## Completion-note states (WQ-229 four states, not merged)
- **IMPLEMENTED** — yes: `Row`, `_field`, `guarded_main`, gate rendering all present and exercised.
- **TESTED** — yes, against the author's own conditions.
- **INDEPENDENTLY VERIFIED** — **NO.** Three blocking findings stand: the rc=2 collision was moved rather than removed (❌1), A3 does not cover the import surface (❌2), and the record misdates the incident (❌3).
- **STILL UNRESOLVED** — ❌1, ❌2, ❌3 and ⚠️1 (loud→silent inversion) are unaddressed by the diff as it stands.

---

## PROCESS NOTE — the repair was COMMITTED mid-verification
- **claim** — WQ-229's CONSEQUENTIAL clause: *"goes to an independent reader BEFORE it is called fixed."* The diff I was asked to verify was committed while I was verifying it, under a subject that asserts the fix.
- **artifact** — `git log --oneline` → `61c857b1c PROME: repair the spawn_list -> session_presence contract; **a crash no longer reads as a clean UNKNOWN**`.
- **verification** — `git log -3 -- PROME/tools/{session_presence,prome_gate,spawn_list}.py`; `git show HEAD:PROME/tools/session_presence.py | md5sum` vs `md5sum PROME/tools/session_presence.py`.
- **observed** — both `51103a546775c01866da2792ed29cefb`: the committed state is byte-identical to what I verified, so **every finding above applies to HEAD**. But ❌2 falsifies the commit subject's own claim for the import-time half — a crash in any of the four sibling imports still exits 1 and still reads as the ordinary UNKNOWN verdict.
- **proposed change** — none to the tree (I am read-only). Note it in the completion note: the independent read landed after the commit, so `finding_adoption_is_not_validation` applies to the commit subject as written.
