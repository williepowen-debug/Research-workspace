# L526 — BRENT cloud-routine false fork: root-cause the class (boot-preamble spec)

**Written:** 2026-10-14 20:46 ET · **Row:** `PROME/DOCKET.tsv` L526 (DAEDALUS boot-protocol blueprint · BRENT routine owner · PROME registrar) · **Recurrences on record:** 9/11 · 9/18 · 9/21 · 9/25 · 9/28. In each, the container booted with HEAD detached, `.git/shallow` present and local `master` with no merge-base against a fresh `origin/master`; on 9/25 and 9/28 there was also no `.venv/`. Each was resolved by hand: unshallow → checkout master → `merge --ff-only`.

## What I checked tonight (and did not)
- `AGENTS/BRENT/SCHEDULED_RUNS.md` (the off-repo prompt mirror) carries **no** unshallow, ff-only or venv-rebuild step (grep: 0 hits). The 10/02 install was the 9/9 timing/publication repair, not this. The class is still unencoded.
- **NOT checked:** whether the false fork recurred after 9/28. Its 10/05 and 10/09 routine commits landed, but I did not read their logs. Also NOT checked: why the cloud container arrives shallow. A shallow default clone in the routine environment is the likely cause, but it is UNVERIFIED.

## Spec — the routine's boot preamble (BRENT owns the text; installing it in the cloud routine is Will's word, as on 10/02)
Run before any read or write, in this order. Every step is fail-loud. The preamble never forces and never resets.
1. `test -f .git/shallow && git fetch --unshallow origin` (otherwise `git fetch origin`).
2. If HEAD is detached: `git checkout master`.
3. `git merge --ff-only origin/master`. **If it is not a fast-forward, STOP and report:** print `git rev-list --left-right --count master...origin/master`, write nothing, publish nothing. The routine must never merge, rebase or force a diverged master on its own.
4. `test -x .venv/bin/python || (python3 -m venv .venv && .venv/bin/pip install -r <the routine's pinned requirements>)` — the requirements file is BRENT's to name; if none exists, that gap is the first finding.
5. Receipt line in the routine's output: `PREAMBLE: unshallowed=<y/n> detached=<y/n> ff=<behind count> venv=<present|rebuilt>`. That line is the canary: five recurrences were invisible except by hand.

## Acceptance (WQ-229 — written before the edit)
- AC1: a shallow, detached container boots to `master == origin/master` with no human step, and the receipt says so.
- AC2: a diverged master (a local commit not on origin) stops at step 3, with the counts printed and nothing written.
- AC3: a missing `.venv/` is rebuilt, or the run stops and names the missing requirements file.
- AC4 (restated 2026-10-31, see Amendment 1): the quiet path is watched on a fixture. A full, non-shallow clone on `master` at the `origin/master` tip with `.venv/` present runs the installed preamble text and prints `unshallowed=n detached=n ff=0 venv=present` (plus the post-merge HEAD short-sha field WQ-543 (b) appends once installed; that field's name is BRENT's). In the hosted container the healthy line is `detached=y ff=<n> venv=rebuilt`, and AC1 governs it, not AC4 (CHECK_STANDARD §3).

**Next:** BRENT drafts the prompt edit against this spec; Will gives the install word; PROME records it; an independent reader checks AC1–AC4 on the first two runs. *(Historical next step from 10/14; the current state lives at DOCKET L526.)*

## Amendment 1 — 2026-10-31 09:29 EDT (AC4 restated; DAEDALUS, PROME prome-34 spawn on DOCKET L526)
**Why:** the original AC4 assumed the hosted container could arrive clean. Three hosted runs on two routines show it cannot: each booted detached at the origin tip with local `master` frozen at `c5ced3676` (2026-10-27) and no `.venv/` — Thu 10/29 03:55Z `ff=262` (reader-verified), Thu 10/29 18:18Z `ff=591` (reader-inferred), Fri 10/30 ~20:16Z `ff=846` (`AGENTS/BRENT/demand_destruction/data/friday_2026-10-30.md` line 5, commit 4f3936da7; equals `git rev-list --count c5ced3676..e4e8000f1`, the origin tip between 16:16:19 and 16:22:23 ET, INFERRED because the file does not name its start commit). That is reader finding #11 (`PROME/reports/2026-10-29_L526-AC-reader.md`). WQ-543's record (`PROME/proposals/2026-10-29_wq543-preamble-text-RULED.md` § Execution) assigns this restatement to DAEDALUS when #11 holds after the Friday run.
**Superseded text (verbatim, no longer the condition):**
> - AC4: a clean, full clone prints `unshallowed=n detached=n ff=0 venv=present`, so the quiet path is watched too (CHECK_STANDARD §3).

**Observed 2026-10-31 13:28Z (fixture, scratchpad clone of the local repository at 9e75c2c5e, the preamble steps translated literally into shell):** clean fixture → `PREAMBLE: unshallowed=n detached=n ff=0 venv=present` (rc 0) on the installed text, and the same line plus `head=9e75c2c5e` on the WQ-543 text (`head=` is my stand-in name for the (b) field). Alert controls on the same fixture: detached at the tip with `master` at `c5ced3676` → `detached=y ff=991` on both texts (expected 991 by `rev-list`); `.venv/` removed → `venv=rebuilt`. Both lines watched. ⚠️ Limit: the fixture runs a shell translation; the hosted executor is a model reading prose, so this proves what the text's commands print on a clean clone, not that the routine will print it. State: TESTED by the spec author, not INDEPENDENTLY VERIFIED.
