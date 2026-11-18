# Are the nine "professional programmer" changes feasible here?

**Date:** 2026-11-18 · **Repository read at:** `99be3d6dcf` (master, 2026-11-17 22:04 ET), full history · **Read only:** nothing in the repository was changed.
**Builds on** earlier reports in this folder: tests-and-tools, governance (pass 8), coordination-load (incl. the six-suggestions check), running-cost, lessons, exposure, forecast-audit.

## The short answer

All nine are possible, but they are not equally good fits. Your system has already built more of this than the list assumes. There are **about 650 Python tools and checks**, git safeguards that run for every commit, an append-only decision ledger and a typed forecast store. The problem is not missing machinery. **Most bookkeeping is still done by agents following written rules, and the scripts only check afterwards.** Your own history shows the difference: rules a script enforces hold, and rules that rely on an agent remembering come back. The commit-subject rule went from 80% broken to 0% once a hook enforced it. Of 9 lessons that relied on memory, 7 recurred (lessons report).

| # | Change | Verdict | Who can do it | Rough size |
|---|---|---|---|---|
| 1 | Bookkeeping into ordinary programs | **Partly done; worth finishing, one ledger at a time** | PROME + DAEDALUS | Moderate (a few sessions per ledger) |
| 2 | Database for structured data | **Wrong tool as stated.** The right version is one shared forecast layout plus append-only rows. Already designed once (KERNEL) and parked | PROME + DAEDALUS, your ruling on KERNEL | Moderate to hard |
| 3 | Automatic tests for every desk, every model | **Partly done; easy to extend.** Git hooks already run for Codex too. The gap is that the test suite never runs by itself | PROME + DAEDALUS; your OK for a GitHub workflow | Easy to moderate |
| 4 | Secrets and personal data out; private repo | **Mostly ruled by you already.** One urgent item left that only you can do: cancel the leaked keys | **You** | Small for you |
| 5 | Record cost and activity automatically | **Easy.** The counting script already exists | PROME, on each of your two machines | Easy |
| 6 | Fewer desks | **Not worth re-opening.** You declined this on 11/6, and quiet desks cost little | Your call only | n/a |
| 7 | One branch per piece of work | **Not as stated.** A lighter version (each running session gets its own folder) fixes the real problem | PROME, with your OK on the root git rule | Moderate |
| 8 | Short generated startup files | **Partly done.** A full rebuild of 45 charters is not worth it now. Fix the four oversized charters | Desks + DAEDALUS | Moderate if done piecemeal |
| 9 | Broker feed instead of screenshots | **Feasible in two steps.** Fidelity has no public API of its own. Step 1 is a CSV download you already have access to. Step 2 is an optional free read-only aggregator, which needs your sign-up | Step 1: PROME. Step 2: **you** | Step 1 easy, step 2 moderate |

**Suggested order:** cancel the leaked keys (4, yours, today) → 3 → 9 step 1 → 1 → 5 → 2 → 7 → 9 step 2 if you want it → 8 as charters are touched. Leave 6 alone.

I agree with the coordinator that 1, 3 and 9 matter most. Two corrections. On 3, the claim that "hooks only run in Claude" is half right: your git hooks run for Codex as well. On 2, a database is more machinery than you need.

---

## 1. Move bookkeeping into ordinary programs

**What exists.** A lot of it:
- `scripts/tsv_append.py` writes a ledger row safely and refuses a wrong column count.
- `PROME/tools/wq_ledger.py sync` writes decision events from the Will Queue by itself.
- `AGENTS/WALTER/tools/reconcile_delivery_log.py --apply` updates delivery rows after a push.
- `scripts/orch_log.py` checks PROME's session log.
- WALTER has 41 tools, PROME has 54, and the DAEDALUS register lists 60 shared checks.
- ORACLE's data pull already runs as an ordinary scheduled program (a cron job on both machines, `PROME/MACHINE_LOCAL.md` line 32). That proves the pattern works here.

**What is still manual.** The agent writes the row, and a script checks it later.
- WALTER's corrections register is the clearest case. The rule says "write the row in the same commit". Compliance measured **51% and 60% against an 80% bar** before a check was added (BOARD_CONSUMPTION_SPEC v0.33/0.34).
- PROME made **294 of its 660 commits in the week of 11/10 to 11/17 only to touch its own ledgers**: closeout receipts, DOCKET lines, queue rows (six-suggestions report).
- Half of all measured tokens go to the three coordinating desks: PROME 23%, WALTER 17%, DAEDALUS 10% (running-cost report).

**What would change.** For each ledger, one small command does the write ("record closeout receipt for FALCON"), and the prose rule describing how to write the row is deleted. The agent decides; the program does the bookkeeping.

**Conflicts.** Your 10/31 instruction to limit checkers and rules. This change fits it if every conversion **deletes** a prose rule and adds no new check. Converting a ledger is replacing a rule, not adding one. Say so explicitly when PROME brings each one to you.

**Start with:** PROME's closeout receipts and session log (the biggest commit count), then WALTER's corrections register (the measured miss).

## 2. A database for forecasts, decisions, positions and signals

**What exists.**
- Forecasts live in **47 `PREDICTIONS.tsv` files using 26 different column layouts**.
- Decisions live in `PROME/DOCKET.tsv` (1,192 lines), `GATES.tsv` and the Will Queue, which already has an append-only event ledger.
- Signals have WALTER's registers.
- **KERNEL** is a typed, append-only store for questions, forecasts and resolutions. It has JSON schemas, 220 passing tests and three trial runs (17 events accepted on 9/2). It has been **parked since early September**, with its independent security review still owed.

**Is a database the fix?** Not really. Pass 5 found real problems:
- 11 scored calls were logged after the outcome was known.
- Date_Made is unreliable (133 rows entered git more than a week after it).
- IDs were reused and open calls were dropped.

What fixes those is **rows that cannot be edited once written, with a time stamp the agent does not type**. A database is one way to get that. The same result is available inside the files you have: git already records when a row first appeared, and a commit hook can refuse an edit to a probability cell, so a revision has to be a new row. A database would also hide the data from the agents' ordinary file reads and add a server to keep running.

**What would change.** One shared forecast layout, migrated desk by desk. Revisions become new rows. The scorer reads the first git time, not the typed date. This links directly to PROME's no-probability flag due 11/20.

**Decision for you.** Either revive KERNEL for forecasts (it was built for exactly this), or formally retire it. That would remove about 40 governance files that agents still read around. Leaving it half-alive is the worst option.

**Not worth it:** a database for signals or positions. Positions come from the broker (item 9). Signals are text and are read as text.

## 3. Every rule enforced by an automatic test, for every desk and model

**What exists.**
- **Git hooks** in `scripts/githooks/` run on every commit and push, **whichever model is driving git, Codex included**. They check the account-number guard, DOCKET line stability, the subject length and fast-forward-only pushes. They are installed per machine (verified on the laptop 10/8, `MACHINE_LOCAL.md` line 39).
- The **Claude-only** hooks in `.claude/settings.json` are the git-command guard, the FORGE/GATES validator after edits and the clock stamp. Codex sessions do not get those three.
- `scripts/validate_all.py` is the fleet suite runner, and there are about 245 test files. 217 passed in pass 7 once the right packages were present.

**The gap.**
- **Nothing runs the tests by themselves**, and the repo has **no list of the packages they need** (only `MESSAGING/requirements.txt`). Today the LIQUID test file still stops at once on a fresh machine for a missing `yfinance`.
- The high-yield kill-check tests were red for 7 days before anyone noticed. LIQUID reports the fixtures fixed on 11/17 (`3f8693dcce`); I could not re-run them here for that package reason.
- Running `pytest` across the whole repo overwrites a TERRY research dataset (`gas_test.py`).

**What would change**, in this order:
1. Add one `requirements.txt`.
2. Rename or fence off the research scripts named `*_test.py` so a test run cannot overwrite data.
3. Mark the four tests that go red when live data moves.
4. Run `validate_all.py` plus the passing test set **at pre-push**, so it runs for Codex and Claude alike.
5. Optional: a GitHub Actions workflow. It costs nothing on a public repository. Its downside is an email to you on every failure, which works against your request for fewer reports.

**Conflicts.** "Every rule" is too far: there are about 2.2 MB of prose rules, and most cannot be tested mechanically. The useful version is to test **the rules that have a measured repeat miss**. That matches your own bar for a new check: a concrete recurring miss plus your word. PROME's four checks due Fri 11/20 are this kind.

## 4. Secrets and personal data out; private repository

**Already ruled by you.**
- **WQ-455** (10/18 to 10/29): redact to last four going forward, no history rewrite. Your words: "the history is key for the repo at this point for the application purposes."
- **WQ-456** (10/20 to 10/21): balances and positions may stay public, and the commit email was switched to a no-reply address. `scripts/account_guard.py` blocks the full account number on every commit.
- The repo is **still public** (checked today).

I am not suggesting you re-open those rulings.

**Left, and only you can do it:** the exposure sweep found an **OpenAI project key and a Brave Search key** (plus two local tokens) in history since 2/7; whether they still work is unknown. They are not covered by any ruling. Cancelling them in the OpenAI and Brave account pages takes minutes, needs no history rewrite and makes the leaked copies useless. Also optional in GitHub settings: secret scanning and push protection, free on public repos. These would have caught that key.

**For item 9:** any new broker credential must live outside the repo, in a file on your machines that git ignores.

## 5. Record cost and activity automatically

**What exists.** RED's `usage_by_desk.py` (11/05) already reads the Claude and Codex session files on a machine and totals tokens and sessions by desk. It ran once, on the desktop only, which is why the laptop desks show near zero.

**What would change.** Run it on a schedule, the same way ORACLE's pull runs, on **both** machines. Have it append one row per desk per day to a small ledger. No report, no brief line: the numbers are there when you ask. Tokens are not dollars, and your plan does not bill by token, so the useful readings are share by desk and "did we hit the usage limit". The limit cost you BRENT's 11/2 and 11/4 runs.

**Size:** easy. It needs a PROME session on each machine to install it.

## 6. Start small: fewer desks

You declined the fleet shrink on 11/6 (WQ-599: "no to the fleet shrinking"). The measured case for it is also weak on cost: the 19 quietest desks used **7.7% of tokens**, while coordination used 50%. And "prove its worth" cannot yet be measured by forecasts: **no desk's forecasting edge clears zero** (per-desk score report), mostly because samples are small.

**Verdict:** not worth re-proposing. If you want the idea at all, use it only for new desks: give the next new desk a dated review ("keep or fold at 60 days") as part of the build, and keep it off the existing roster.

## 7. One branch per piece of work

**Why the full version does not fit.**
- Desks deliver to each other by committing files into inboxes on `master`.
- WALTER pushes urgent signals straight to `master`.
- Every boot pulls `master`.

Separate branches would hold deliveries back until someone merges them. Merging would fall on PROME or you, which adds decision load.

**The real problem it would solve:** all running sessions share one folder. Git refuses to pull while any desk has unsaved changes, and that is why batching PROME's ledger edits to closeout was ruled out in the six-suggestions check.

**Lighter fix:** give each running session its **own working folder of the same repository** (git calls this a "worktree"). Each one still commits straight to `master` and pushes with `safe-push.sh`. Desks stop blocking each other's pulls, and the shared-index rules (`docs/GIT_WORKTREE_PROCEDURES.md` items 4 to 4c) mostly fall away.

**Cost.** A change to the root git protocol (your OK). Each extra folder takes disk space, as the full clone is large. And every tool that assumes one folder has to be checked.

**Size:** moderate. Worth doing after items 1 and 3.

## 8. Short generated startup files

**What exists.**
- Charters are hand-written: **45 of them, 1.26 MB, median 24 KB**. Four are over your 50,000-byte charter cap: LABOR 55.6 KB, OSPREY 55.3 KB, FALCON 51.5 KB, AEOLUS 50.7 KB. Two of those are past the size where a single read gets cut off.
- Parts of the startup are already generated by script: `active_decisions_digest.py`, `decision_deck.py`, `will_brief.py`, `docket_view.py`, `spawn_slate.py`.

**Why a full rebuild is not worth it now.** Generating the "current state" part is easy. The hard part is deciding which rules each charter can drop. That is the prose-rule sweep pass 8 suggested, and changing rules here is very expensive: one 4 KB trim took about 94 KB of paperwork.

**Verdict:** bring the four oversized charters under the cap first. Then, when a desk's charter is next touched, move its live state out into a generated header. Do not open a fleet-wide project.

## 9. A direct broker feed instead of screenshots

**Today.** You post Fidelity screenshots, PROME transcribes them, ANVIL reconciles and commits. There were nine reconciles from 10/15 to 11/10, and the mirror has stopped at the **11/10 intraday capture**.

**What Fidelity offers individuals** (checked 2026-11-18; no account details were used in any lookup):
- **No public developer API for retail customers.** Fidelity shares data only through its consent system (Fidelity Access) with approved aggregators.
- **CSV download from the website.** The positions page can be downloaded as a CSV file. The repo proves it: a Fidelity "Portfolio_Positions" CSV was committed in May. The exposure sweep flagged that file because it **contains the full account number**. Any CSV route must keep the raw file off the repo.
- **SnapTrade Personal**, an aggregator:
  - Free for personal use ([snaptrade.com/personal](https://snaptrade.com/personal)).
  - Lists Fidelity as **read-only**, data up to 24 hours old, after about 2 business days' approval ([broker access guide](https://docs.snaptrade.com/docs/broker-access-guide.md); [Fidelity guide](https://snaptrade.com/blogs/connect-fidelity-account-holdings)).
  - Has a read-only connector that plugs into Claude ([MCP server docs](https://docs.snaptrade.com/docs/mcp-server)).
  - ⚠️ Sources disagree on whether you approve on Fidelity's site or hand over your Fidelity password ([Open Banking Tracker](https://openbankingtracker.com/snaptrade/fidelity) says password). They also disagree on whether Fidelity is enabled on the free personal plan (5 vs 20 connections stated). You would need to check this in their sign-up before relying on it.
- **Unofficial scrapers** (e.g. the `fidelity-api` Python package, [PyPI](https://pypi.org/project/fidelity-api/)) drive a browser with your password and can place orders. **Not recommended.**

**Step 1, easy, PROME can build:** you click "download" on the Fidelity positions and activity pages and save the two files to a fixed folder **outside** the repo. A script reads them, keeps the last four digits only, and updates `FORGE/STATUS.md` through the existing ANVIL reconcile. This replaces screenshot transcription. It is exact to the cent, with no transcription errors, and needs nothing from Fidelity but the button. Robinhood also offers a downloadable statement, but it is less convenient. That would need checking.

**Step 2, optional, only you:** sign up for SnapTrade Personal, approve read-only access for the IRA, and store the key on your machines outside the repo. Then the mirror refreshes daily with no action from you. This is an outside company holding read access to your IRA, so it is your call. Your existing protections (PIN and phone check on new devices) are unaffected by a read-only link.

---

## Copy-paste block for PROME

```
From Will, 2026-11-18. Outside read-only feasibility review of nine "professional programmer" changes
(report: feasibility/2026-11-18_nine-programmer-changes-feasibility.md, repo read at 99be3d6dcf).
Treat this as a work order in the order below. Each item keeps my 10/31 bar: no net new rules or checks;
every conversion must name the prose rule it deletes. Bring me one ⚖️ block per item that needs my word.
Do not start anything after item C until the Fri 11/20 checks are done.

A. (Mine, no action for you except a reminder in your next brief) I will revoke the OpenAI project key and
   Brave Search key found in config/openclaw-multiagent.json5 history (exposure report item 1), and consider
   GitHub secret scanning + push protection. No history rewrite (WQ-455 stands).

B. Tests that run themselves (DAEDALUS builds, you review):
   1. Add one root requirements.txt covering what the test files import (yfinance, pandas, jsonschema,
      scipy, openpyxl, matplotlib, PyYAML at least).
   2. Stop research scripts named *_test.py from being collected as tests (TERRY gas_test.py overwrites
      data/gas_closes.csv when pytest collects it). Rename or add a pytest config; do not delete.
   3. Mark the tests that read live desk files (SAM boot_corrections, LABOR prediction_deadlines,
      PROME closeout, VULCAN) so "data moved" is not reported as "code broke".
   4. Re-run AGENTS/LIQUID/scripts/test_alert_srf_repair.py with packages installed and confirm 25/25.
   5. Propose to me: run validate_all.py plus the passing test set from scripts/githooks/pre-push so
      Claude and Codex sessions both hit it. Tell me the run time. Do NOT add a GitHub Actions workflow
      without asking me (it emails on failure).

C. Broker CSV instead of screenshots (step 1 only):
   Build a script that reads Fidelity's downloaded Positions CSV and Activity CSV from a fixed folder
   OUTSIDE the repo (git-ignored path on each machine, recorded in MACHINE_LOCAL.md), masks the account
   to last four, and produces the reconcile input ANVIL already uses. The raw CSV must never be committed
   (account_guard should refuse it anyway; test that). Tell me exactly which two download buttons to press.
   Do not sign me up for any aggregator. SnapTrade Personal (read-only, free) is a later question for me.

D. Bookkeeping by program, one ledger at a time. Start with closeout receipts and ORCH_LOG (294 of your
   660 commits 11/10–11/17 were ledger-only), then WALTER's CORRECTIONS.tsv write step. For each: one
   command does the write, the prose instruction is deleted, show me the bytes removed.

E. Usage record: schedule RED's usage_by_desk.py (AGENTS/RED/research/2026-11-05_op-scale_usage/) daily on
   BOTH machines like ORACLE's daily_pull, appending to one TSV. No report and no brief line; I will ask.

F. Forecasts: bring me one decision — revive KERNEL for forecast rows, or retire it — with your
   recommendation. Separately propose one shared PREDICTIONS.tsv layout (there are 26 layouts across 47
   files) where a revision is a new row and the scorer uses the first git time, not the typed Date_Made.

G. Later, needs my OK on the root git rule: one working folder (git worktree) per running session, still
   committing to master via safe-push. Bring a short proposal after B–E land, with disk cost per machine.

H. Charters: bring LABOR, OSPREY, FALCON and AEOLUS under the 50,000-byte cap by moving history out.
   No fleet-wide charter rebuild.

Not doing: re-opening the fleet size (WQ-599 stands), a private repo (WQ-455/456 stand), a database
server, or branch-per-task with merges.
```
