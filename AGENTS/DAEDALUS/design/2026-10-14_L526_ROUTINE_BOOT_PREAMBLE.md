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
- AC4: a clean, full clone prints `unshallowed=n detached=n ff=0 venv=present`, so the quiet path is watched too (CHECK_STANDARD §3).

**Next:** BRENT drafts the prompt edit against this spec; Will gives the install word; PROME records it; an independent reader checks AC1–AC4 on the first two runs.
