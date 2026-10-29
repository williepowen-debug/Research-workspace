# GIG CLOSEOUT — the single live closeout contract

> **Run at EVERY session end**, whether Will launched the session or CARL spawned it, including intermediate passes on a multi-pass day. *(Written 2026-10-28, Will: "adopt and improve the close out now", after a fleet comparison found GIG's closeout was two lines: no git step, no NOT RUN rule, no fleet checks, no rotation. Adapted from PHAN's `CLOSEOUT.md`. **Interim:** if CARL adopts PHAN's shared sub-agent runner proposal, GIG moves to it and this file points there.)*
>
> **Closeout is not finishing the backlog.** Every step below ends **done**, **N/A with a reason**, or **NOT RUN**. A mandatory check not run means a **partial closeout**, and the final report says so. Never report a check as passed that did not run.
>
> **Order: WRITE → RUN → COMMIT → PUSH → POST.** Nothing writes inside GIG's files after the runner's pre-commit pass, except fixes for what it flagged (then re-run it).

## WRITE

1. **`STATUS.md`** (the whole-read boot surface):
   - Restamp `**Last Updated:**` with the date from `date`, never from memory, **even on a no-change session**.
   - Update the top tables in place. Then **search the whole file for the old wording** of anything you changed; a correction in one section leaves the old claim live in another.
   - **Rotation:** at **≥75% of 32,550 B**, move settled sections **verbatim** to `archive/STATUS_ARCHIVE_<YYYY-MM>.md` with a `bytes= crc32=` stamp per block and a one-line pointer left behind. **Before cutting, prove every figure cited as current survives outside the cut.** Never delete.
2. **Live ledgers** (`workbook/` PLATFORM, DRIVER_ECONOMICS, VX, ML, PREDICTIONS):
   - A new reading is a **new row** (As_Of + primary source). A changed reading on an existing row gets a dated `||` note; never overwrite history silently.
   - **Two clocks on row 1:** advance `Last real data refresh` **only on real data**; a hygiene pass advances only `Last hygiene/no-event check`.
   - A withdrawn read is corrected **where it was written** (the row's Notes), not only in STATUS.
   - All GIG ledgers are **LF**, one header row after the row-1 banner, equal column counts.
   - **FLOW.tsv is FROZEN, AV_TRACKER.tsv is RETIRED:** never append or edit.
3. **Predictions** (`workbook/PREDICTIONS.tsv`): grade only on the series in the row's **Instrument** cell. A window that passed without its print is `DUE-UNRESOLVED [DATA-NEEDED: <print>]`. A row due on a scheduled print gets its expectation written **before** the print. **GIG proposes, CARL disposes:** resolutions, closures and successors go to CARL as asks.
4. **State vector:** if anything moved, write `state_vectors/SV-GIG-<date>-NN.md` (template in `CLAUDE.md`). Put every ruling you need under a **`CARL must rule on:`** heading. When CARL rules, append `CARL rulings applied <date>: …` to that SV. The runner lists asks with no recorded ruling.
5. **Routing:** a **signal** (a registered threshold firing, a cross-desk trip) goes to **WALTER** (`AGENTS/WALTER/inbox/`), never straight to another desk. **Analysis and asks that CARL must act on before its next harvest** also go as a packet to `AGENTS/CARL/inbox/<date>_from-GIG_<subject>.md`, committed by GIG (root carve-out ①). A packet CARL has not acted on is **delivered, not landed**.
6. **Inbox:** `git mv` each consumed packet to `inbox/processed/` (never bash `mv`). Anything deliberately not actioned gets a dated **PARKED** note in STATUS. A packet older than ~30 days: telling its sender outranks actioning it.
7. **Next run docketed:** the runner shows the next future GIG row in CARL's `docket/CATALYSTS.tsv` and flags it if still `UNVERIFIED`. CARL owns the docket; ask in your SV or packet.
8. **Auto-memory** (only if a transferable lesson was earned): extend an existing memory before creating one, under `memory/auto/`; self-commit it (carve-out ③); pass its slug to the runner.

## RUN

9. **Runner, from anywhere:**
   ```
   python3 AGENTS/CARL/sub_agents/GIG/scripts/closeout_check.py \
       [--superseded OLD:NEW:SERIES ...] [--memory-slug <slug> ...]
   ```
   - **What it runs:** STATUS read cap + rotation trigger · STATUS restamped today · archive bytes/CRC32 integrity · TSV column counts, LF, no blank lines · two-clock headers · frozen/retired ledgers bannered and unedited · OPEN predictions inside their window · CARL rulings asked and unrecorded · inbox re-scan · next docket row (+ UNVERIFIED flag) · `claim_check` weekday · `orphan_check` · `ledger_staleness` (GIG glob) · CARL `consistency_check` Check E · fleet `read_cap_check --agent GIG` · if flagged: `consumer_check` and memory checks.
   - **🔴 FAILED** → fix and re-run. **⚠️ LOOK** → a decision; record it in STATUS or the SV. **⚪ NOT RUN** → correct only if its condition truly did not apply.
   - It **lists the judgement steps it cannot verify.** A clean run means the steps **executed**, never that the closeout is right.

## COMMIT · PUSH · POST

10. **Commit** from the repo root, **explicit pathspecs only**: files under `AGENTS/CARL/sub_agents/GIG/`, packets GIG authored into another inbox (①), memory files GIG authored (③). Modified: `git commit <paths> -F <msg>`. New: `git add <files> && git commit <same files> -F <msg>`. ⛔ Never `git add .`/`-A`, a directory, a pathspec-less commit, `--amend`, or `git reset HEAD`. Subject ≤100 chars, figures in the body, `Co-Authored-By` trailer.
11. **Push by session type:** **Will-launched** → `bash scripts/safe-push.sh`; the receipt is `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).` **CARL-spawned** → commit only; CARL's push carries it. If unsure which you are, you were spawned. ⛔ Never pipe `safe-push.sh` through `tail`/`head`; capture first: `out=$(bash scripts/safe-push.sh 2>&1); rc=$?`. Non-ff → root `CLAUDE.md` step 3 (overlap check first; never force).
12. **POST** (Will-launched only): re-run the runner with `--post`. It proves nothing GIG-authored is uncommitted and no GIG-touching commit is missing from `origin/master`.

## REPORT

13. **Final report**, stated separately: (a) findings persisted, and where; (b) checks run / not run / failed, plus LOOK decisions; (c) local commit vs verified push (quote the receipt); packets delivered vs acted on. Name anything left owed. A partial closeout is reported as partial.
