# PHAN CLOSEOUT — the single live closeout contract

> **Run at EVERY session end**, whether Will launched the session or CARL spawned it, including intermediate passes on a multi-pass day. *(Written 2026-10-28, Will-approved, after a fleet comparison ranked PHAN's old closeout 8th of 9: it lacked four root checks, a NOT RUN rule and any automation. It replaces `DOSSIER.md` §8 steps 4–12, which live in git history. Model: the DOC/STUE sub-agent template plus HANS's runner.)*
>
> **Closeout is not finishing the backlog.** Every step below ends **done**, **N/A with a reason**, or **NOT RUN**. A mandatory check not run means a **partial closeout**, and the final report says so. Never report a check as passed that did not run.
>
> **Order: WRITE → RUN → COMMIT → PUSH → POST.** Nothing writes inside PHAN's files after the runner's pre-commit pass, except fixes for what it flagged (then re-run it).

## WRITE

1. **Live ledgers** (`workbook/`):
   - **COCKROACH / REGULATORY:** append new events. A sweep that found nothing gets an explicit `DID_NOT_APPEAR` row. Otherwise a stale data clock can't be told apart from nobody looking.
   - **PROVIDER:** a new reading is a **new row** with As_Of and primary source. Prefix the superseded row's Notes with `SUPERSEDED <date> by …` and never overwrite its values.
   - **Two clocks:** advance `Last real data refresh` **only on real data**; a hygiene pass advances only the no-event clock.
   - **Frozen ledgers** (VX, ML, FLOW) are never appended. Check line endings before any TSV edit: FLOW/ML/VX are CRLF, the rest LF.
2. **`DOSSIER.md`:**
   - Update CURRENT STATE **in place**, never as a new section.
   - Advance the as-of stamps in CURRENT STATE, §3 and §6.
   - Update the **📌 OWED block**: close what you did; add what PHAN or CARL now owes, with the date raised.
   - **Rotation:** if the runner reports the dossier at ≥85% of 32,550 B, move settled narrative and closed rows to `PASSES.md` this session. Never delete.
3. **Predictions:** re-mark confidence with a dated note in `workbook/PREDICTIONS.tsv`. **Never resolve here: PHAN proposes, CARL disposes.** A row due on a scheduled print gets its expectation written **before** the print.
4. **Routing:**
   - A **signal** (a registered threshold firing, a cross-desk trip) goes to **WALTER** (`AGENTS/WALTER/inbox/`), never straight to another desk.
   - **Analysis, rulings asked and docket requests** go to **CARL**: a packet in `outbox/<date>_PHAN-to-CARL_<subject>.md` **plus** a delivery copy at `AGENTS/CARL/inbox/<date>_from-PHAN_<subject>.md`. Root carve-out ① makes committing both yours and mandatory.
   - ⚠️ A packet the recipient has not graded is **delivered, not landed**; say so in the report.
   - If you **superseded a figure other desks may cite**, see step 9's `--superseded` and packet each owner whose **live** surface still carries the old figure. Never edit their files. On a bare 2-significant-figure figure, confirm with a targeted grep (series + figure) before sending anything.
5. **Inbox:** `git mv` each consumed packet to `inbox/processed/` (never bash `mv`). Anything deliberately not actioned gets a dated **PARKED** line in the OWED block. **A packet older than ~30 days: telling its sender outranks actioning it.**
6. **Next run docketed:** the runner shows the next future PHAN row in CARL's `docket/CATALYSTS.tsv`. If a PHAN-relevant event lands before that row (an earnings print, a ruling), ask CARL for a row in your packet. CARL owns the docket, and PHAN has no scheduler; its only wake-up is a row someone else reads.
7. **`PASSES.md`:** write the pass narrative (newest first) **and a closeout record table** (step → result) at the top.
8. **Auto-memory** (only if a transferable lesson was earned): **extend an existing memory before creating one**, under `memory/auto/`. Self-commit the file (root carve-out ③). Pass its slug to the runner.

## RUN

9. **Runner, from anywhere:**
   ```
   python3 AGENTS/CARL/sub_agents/PHAN/scripts/closeout_check.py \
       [--superseded OLD:NEW:SERIES ...] [--memory-slug <slug> ...]
   ```
   - **What it runs:**
     - dossier read cap + rotation trigger
     - TSV column counts + line endings
     - live-ledger two-clock headers
     - inbox re-scan
     - next docket row
     - `claim_check` weekday
     - `orphan_check`
     - `ledger_staleness` (PHAN glob)
     - CARL `consistency_check` (Check E covers PHAN's predictions)
     - fleet `read_cap_check`
     - if flagged: `consumer_check` and the memory checks
   - **🔴 FAILED** → fix and re-run. **⚠️ LOOK** → a decision; record it in the OWED block or the closeout record. **⚪ NOT RUN** → correct only if its condition truly did not apply.
   - It **lists the judgement steps it cannot verify**. A clean run means the steps **executed**, never that the closeout is right.
   - ⚠️ Known: the fleet `read_cap_check --agent PHAN` grades frozen `STATUS.md` until PROME adds PHAN rows to `PROME/registry/READS.tsv` (packet 2026-10-28). The runner flags it as LOOK; the local dossier check is the real one.

## COMMIT · PUSH · POST

10. **Commit** from the repo root, **explicit pathspecs only**:
    - **Allowed paths:** files under `AGENTS/CARL/sub_agents/PHAN/`, packets PHAN authored into another inbox (①), and memory files PHAN authored (③).
    - Modified: `git commit <paths> -m …`. New: `git add <files> && git commit <same files> -F <msg>`.
    - ⛔ **Never:** `git add .`/`-A`, a directory, a pathspec-less commit (it sweeps other sessions' staged files), `--amend`, or `git reset HEAD`.
    - If `.git/index.lock` exists, wait and retry; never delete it.
    - Subject ≤100 chars, figures in the body, `Co-Authored-By` trailer per the session's attribution line.
11. **Push by session type:**
    - **Will-launched** → `bash scripts/safe-push.sh`. The receipt is the line `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).`
    - **CARL-spawned** → commit only; CARL's push carries it. If unsure which you are, you were spawned.
    - ⛔ **Never pipe `safe-push.sh` through `tail`/`head`.** Its failure states differ only in the state line. If you must filter, capture first: `out=$(bash scripts/safe-push.sh 2>&1); rc=$?`.
    - Non-ff → root `CLAUDE.md` step 3 (dirty-path overlap check first; never force).
12. **POST** (Will-launched only): `python3 AGENTS/CARL/sub_agents/PHAN/scripts/closeout_check.py --post`. It proves nothing PHAN-authored is left uncommitted and that no local commit is missing from `origin/master`.

## REPORT

13. **Final report:** state separately
    - (a) **findings persisted**, and where;
    - (b) **checks**: run / not run / failed, plus LOOK decisions;
    - (c) **local commit vs verified push** (quote the receipt);
    - packets **delivered vs graded**.

    Name anything left owed. A partial closeout is reported as partial.

---

*Boot stays in `DOSSIER.md` §8 (BOOT 1–3). Shared fleet canon this file does not restate: root `CLAUDE.md` § Git Protocol and `docs/GIT_WORKTREE_PROCEDURES.md` § Before committing.*
