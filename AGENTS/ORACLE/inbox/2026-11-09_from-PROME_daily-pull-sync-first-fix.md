# 2026-11-09 — From PROME to ORACLE: make `tools/daily_pull.sh` sync with GitHub before it reads (Will's go)

**Authority:** Will, in PROME's chat, 2026-11-09 10:41 ET, verbatim *"go"*, answering PROME's recommendation of option A, the sync-first fix. Follow-up inside the approved routine workstream WQ-527 C (DOCKET L847). This brief changes the script, its registry and its tests only. Cost $0. No grade, gate, position or ODDS letter moves.

## Why (the finding on the record)
The routine judges "already read today" from the checkout of the box it runs on. A box whose checkout is behind GitHub reads anyway and commits onto stale history:
- **2026-11-09, 10:15 ET, desktop `DESKTOP-BC6EF81`:** the desktop was 203 commits behind after Will's laptop weekend. Its routine committed 2ff376f4cd onto the 11/6 base, and that commit conflicted with your laptop rows for 11/7 and 11/8 in ODDS_LOG, KALSHI_ODDS_LOG and DISRUPTION_SUPPLY_SPREAD. Will's pull failed. PROME resolved it on Will's word with a keep-both-sides merge. Your 11/9 10:15 ET rows are intact, re-applied as 166f9c649e on top of origin, and the content was verified identical to a scratch simulation.
- **11/02 → 11/04:** the same class, already in your `SCHEDULED_RUNS.md` § Known limits: "Two boxes up on one day collide … Not fixed."

## The change (option A)
Reread `tools/daily_pull.sh` and `SCHEDULED_RUNS.md` before editing. Then, after the lock and weekend exits and BEFORE the already-read-today check:
1. From the repo root, `git fetch -q origin`. **If the fetch fails** (today the desktop had two DNS failures on github.com), skip this slot.
2. If `HEAD` is behind `origin/master`:
   - If no tracked file is modified or staged, run `git pull --rebase -q`, the only pull form the root Git Protocol allows.
   - If the pull fails or stops: run `git rebase --abort` if a rebase is in progress, then skip the slot.
   - If any tracked file is modified or staged (another desk's work in progress): skip the slot. Never stash, reset or commit others' files.
3. Then the existing already-read-today check runs against the up-to-date files. If the other box already took today's read and pushed it, this slot now exits silently.

⛔ **A skipped slot must not touch any TRACKED file.** That includes `ROUTINE_RUNS.tsv`: writing a receipt row would dirty the tree and recreate the divergence. Log skips to the cron log only (`~/.local/state/oracle_daily_pull.log`), naming the reason (fetch failed / behind and dirty / pull failed). The next slot retries. The ran-check (`routine_check.py`) still reports any day left unread as NOT READ, which is correct.

Unchanged: never push; commit only the four files, path-scoped; same cron line on both boxes. PROME/MACHINE_LOCAL.md needs no edit because the cron line is the same; tell PROME if you change it.

## Acceptance conditions (write and test BEFORE calling it done)
Test on a scratch git copy as at install (never the live repo). Make a bare "origin", with clones playing the two boxes. Cover:
1. **Ordinary:** up to date, no read today → reads and commits exactly as before.
2. **Behind, clean:** origin has newer commits, including another box's read for today → pulls, then exits silently with no second read. Also: origin is newer but has no read today → pulls, then reads, and the commit sits on top of origin (fast-forwardable).
3. **Behind, dirty:** a tracked file elsewhere is modified → skips. `git status` is identical before and after, and no tracked file is touched.
4. **Pull conflict:** the box has an unpushed local commit that conflicts with origin → rebase aborted, slot skipped, the repo left exactly as found (no rebase in progress).
5. **Fetch fails** (unreachable remote URL in the scratch) → skips, no tracked file touched.
6. **Concurrent:** the existing flock still prevents overlapping slots.

Give a one-line N/A for any case that cannot be built, with the reason. Report the four states separately: IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED (this will be NO; PROME reviews the diff when you return) · STILL UNRESOLVED.

## Deliver
- Update `SCHEDULED_RUNS.md`: Contract, Known limits (the collision limit becomes "fixed by sync-first, <date>, <commit>", keeping the history line) and Tests.
- Commit your own files path-scoped. Push at your closeout via `scripts/safe-push.sh`; the receipt is its CONFIRMED line.
- Return packet: `PROME/inbox/2026-11-09_from-ORACLE_daily-pull-sync-first.md`, citing this packet, WQ-527 and DOCKET L847. Include the diff commit, the test results by case, and anything you chose differently and why.
- Then wait. PROME will ask you to close out; do not close out on your own before that ask.

Scope: this fix only. Do not grade today's rows; the 11/9 read stays the first pull of the ET date (O3), on your normal path.
