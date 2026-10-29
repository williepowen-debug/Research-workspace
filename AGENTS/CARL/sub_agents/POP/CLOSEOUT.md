# POP CLOSEOUT — the single live closeout contract

> **Run at EVERY session end**, whether Will launched the session or CARL spawned it, including intermediate passes on a multi-pass day. *(Written 2026-10-29, Will: "make sure POP close out protocol is updated ... compare contrast to other mature agents". A fleet comparison found POP's closeout was a 5-line list with no git step, no NOT RUN rule, no fleet checks and no docket step. Adapted from PHAN's and GIG's `CLOSEOUT.md` (10/28) and the DOC/STUE template. The earlier list lives in git history.)*
>
> **Runner:** POP has none yet, deliberately. PHAN's proposal for one shared sub-agent runner (`AGENTS/CARL/inbox/2026-10-28_from-PHAN_shared-subagent-closeout-runner-proposal.md`) is pending at CARL. If CARL adopts it, POP moves to it and this file points there. **Until then every check in RUN is executed by hand and its exit code reported.** A check that is missing from your report counts as not run, even if the list looks shorter.
>
> **Closeout is not finishing the backlog.** Every step below ends **done**, **N/A with a reason**, or **NOT RUN**. A mandatory check not run means a **partial closeout**, and the final report says so. Never report a check as passed that did not run.
>
> **Order: WRITE → RUN → COMMIT → PUSH → REPORT.** Nothing writes inside POP's files after the RUN pass, except fixes for what it flagged (then re-run).

## WRITE

1. **`STATUS.md`** (the whole-read boot surface, dossier-mode):
   - Restamp the `**Last touched:**` line from `date`, never from memory, **even on a no-change session**. Advance `**Last real data refresh:**` only when the **dashboard rows** were re-pulled. A dated addendum carries its own date and does not move that clock.
   - New findings go in a dated **ADDENDUM** block that points to its state vector. The Apr-17 dashboard rows are not edited in place until a full refresh lifts the banner.
   - Then **search the whole file for the old wording** of anything this session changed (a graded prediction, a corrected figure, a status flip). Fix any survivor still written as current; leave clearly historical lines alone.
   - **Read cap:** STATUS stays under **32,550 B**, and at ≥75% it rotates. Move settled addenda **verbatim** to `archive/STATUS_ARCHIVE_<YYYY-MM>.md` with a `bytes= crc32=` stamp, and leave a one-line pointer behind. **Before cutting, prove every figure cited as current survives outside the cut.** Never delete.
2. **Ledgers (`workbook/`):**
   - **VX, ML, SECTOR, TARIFF are MIXED VINTAGE** (banner of 2026-10-28): the row's own date column governs. Every row you touch gets today's date in that column. A row you looked at but could not refresh keeps its old date. Never bump a date over an untouched cell.
   - **ML is append-only**: a new observation is a new `ML-POP-NN` row. That includes a **searched-not-found** row for anything looked for and not found, so the next pass does not re-search blind.
   - SECTOR/TARIFF: a new reading is a **new row**; a superseded row gets a dated `[SUPERSEDED <date> by …]` in its Notes, never a silent overwrite.
   - **FLOW.tsv and PREDICTIONS.tsv still carry the STALE-VINTAGE 2026-04-17 banner.** Edit PREDICTIONS only per step 3; FLOW is not edited without a full refresh.
   - Every TSV: **LF only**, one banner line plus one header, **equal column counts** (VX 13 · ML 17 · SECTOR 11 · TARIFF 10 · PREDICTIONS 10 · FLOW 14). Check with `awk -F'\t' 'NR>1{print NF}' <file> | sort | uniq -c` and `grep -c $'\r' <file>`.
   - Each figure's **basis** goes in the cell: the series ID, primary vs secondary, field dates. A secondary figure says so.
3. **Predictions (`workbook/PREDICTIONS.tsv`):** grade only on the series in the row's **Instrument** cell. A window that passed without its print is `DUE-UNRESOLVED [DATA-NEEDED: <print>]`. **Never overwrite Confidence at grading**; the as-made figure stays. A row due on a scheduled print gets its expectation written **before** the print. **POP proposes, CARL disposes:** resolutions, re-marks and successors go to CARL as asks. Nested thresholds on one series must be monotone **across** POP and CARL ledgers (P06 vs CRL-15).
4. **State vector:** if anything moved, write `state_vectors/SV-POP-<date>-NN.md`. Put every ruling you need under a **`CARL must rule on:`** heading. When CARL rules, append `CARL rulings applied <date>: …` to that SV.
5. **Routing:** a **signal** (a registered threshold firing, a cross-desk trip) goes to **WALTER** (`AGENTS/WALTER/inbox/`), never straight to another desk. Asks CARL must act on before its next harvest go as a packet: `AGENTS/CARL/inbox/<date>_from-POP_<subject>.md`, committed by POP (root carve-out ①). Say in one line whether a finding changes CARL's score or only its context; the call is CARL's. A packet CARL has not acted on is **delivered, not landed**.
6. **Inbox:** `git mv` each consumed packet to `inbox/processed/` (never bash `mv`). Anything deliberately not actioned gets a dated **PARKED** note in STATUS. A packet older than ~30 days: telling its sender outranks actioning it.
7. **Next run docketed:** POP is dossier-mode with no scheduler. Its only wake-up is a row in CARL's `docket/CATALYSTS.tsv`. Confirm every POP-relevant dated read has a row there: NFIB monthly (~2nd Tue), Census BFS (~mid-month), Epiq AACER monthly, Fed SLOOS quarterly, FRED DRBLACBS quarterly, the SBA FY file, and any court/closure deadline POP is tracking. If one is missing, ask CARL in the packet; CARL owns the docket.
8. **Auto-memory** (only if a transferable lesson was earned): extend an existing memory before creating one, under `memory/auto/`; self-commit it (carve-out ③).

## RUN (by hand until a runner exists; report each exit code)

From the repo root (`cd "$(git rev-parse --show-toplevel)"`). ⛔ Never read an exit code through `tail`/`head`; capture it: `out=$(cmd 2>&1); rc=$?`.

| # | Check | Command | Condition |
|---|---|---|---|
| 9a | Weekday claims | `python3 scripts/claim_check.py --check weekday <every dated file changed>` | always |
| 9b | Orphans | `bash scripts/orphan_check.sh CARL` — commit only POP-authored items; never sweep another session's files | always |
| 9c | Ledger staleness | `python3 scripts/ledger_staleness.py CARL --glob 'sub_agents/POP/workbook/*.tsv'` | always |
| 9d | Read cap | `python3 scripts/read_cap_check.py --agent POP` (if it cannot resolve a sub-agent, measure `wc -c STATUS.md` against 32,550 B and say so) | always |
| 9e | CARL consistency | `.venv/bin/python3 AGENTS/CARL/scripts/consistency_check.py --quiet --warn-only` — Check E is the cross-ledger monotonicity check (P06 vs CRL-15) | if PREDICTIONS.tsv changed; otherwise optional |
| 9f | Consumers | `python3 scripts/consumer_check.py --agent CARL --old <old> --new <new>` (+ `--self`) | only if a figure **others cite** was corrected; confirm series and unit; never on a bare 2-3 sig-fig number. ⚠️ `--self` is **unrunnable for sub-agents** (10/29: resolves `AGENTS/POP`, fails closed with "nothing scanned"). Report it NOT RUN with that reason, and scan POP's own files by `grep` instead |
| 9g | Memory | `python3 scripts/memory_index_check.py --strict --slug <slug>` + `bash scripts/check_memory_length.sh` | only if auto-memory written |
| 9h | 60-day retirement | root Data Hygiene sweep of `domain/sources/` | always; an unfinished reference review is NOT a completed sweep |
| 9i | TSV integrity | step 2's `awk`/`grep` pair on every TSV touched | if a TSV changed |

**🔴 fail** → fix and re-run. **⚠️ finding** → a decision; record it in STATUS or the SV. A clean run means the steps **executed**, never that the closeout is right.

## COMMIT · PUSH

10. **Commit** from the repo root, **explicit pathspecs only**: files under `AGENTS/CARL/sub_agents/POP/`, packets POP authored into another inbox (①), memory files POP authored (③). For modified files: `git commit -F <msg> -- <paths>`. For new files: `git add <files> && git commit -F <msg> -- <same files>`. Write the message file in the scratchpad via a **quoted** heredoc. ⛔ Never `git add .`/`-A`, a directory, a pathspec-less commit (the shared index may hold another desk's staged renames), `--amend`, or `git reset HEAD`. Subject ≤100 chars, figures in the body, `Co-Authored-By` trailer.
11. **Push by session type:** **Will-launched** → `bash scripts/safe-push.sh`. The receipt is the line `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).` **CARL-spawned** → commit only; CARL's push carries it. If unsure which you are, you were spawned. Non-ff → root `CLAUDE.md` step 3 (overlap check first; never force).

## REPORT

12. **Final report**, stated separately: (a) findings persisted, and where; (b) checks run / not run / failed, with each exit code; (c) local commit vs verified push (quote the receipt); packets delivered vs acted on. Name anything left owed. A partial closeout is reported as partial.
