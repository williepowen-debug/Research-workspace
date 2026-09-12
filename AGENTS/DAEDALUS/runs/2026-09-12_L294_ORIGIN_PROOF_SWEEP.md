# DOCKET L294 — FLEET SWEEP: ORIGIN-PROOF INSTRUMENTS

**DAEDALUS (sweep owner) · 2026-09-12 (Sat) · WALTER's 9/5 ask, PROME-docked · method = WALTER/Codex behavioural**
**THE ONE QUESTION:** for every instrument asserting something about ORIGIN — does it query a remote-tracking
ref after a FRESH fetch, and **what does the verdict become when that evidence-gathering step FAILS?**
**THE INVARIANT:** a positive verdict requires SUCCESSFUL evidence; unavailable evidence stays UNKNOWN through
to the final report.

## METHOD — behavioural, and it superseded a grep census (this mattered)
Every verdict was drilled by **forcing its evidence step to fail** — a fake `git` earlier on `PATH` that makes a
named subcommand exit non-zero, or exit 0 with empty output — against a purpose-built scratch repo with a real
local bare `origin.git`. **Each instrument also got its PASSING CONTROL** (WQ-185, Will 9/6): a successful fetch
must still produce a passing verdict; a guard that always says UNKNOWN is equally broken.
⛔ **No file in the repo was created, edited, moved or committed by the sweep.** All drills ran on copies.

## COUNTS
| | n |
|---|---|
| Instruments located in the origin/delivery/sync-verdict perimeter | **20** |
| Drilled behaviourally (forced failure **+** passing control) | **14** |
| Individual drill runs | **71** |
| 🔴 **FAIL-OPEN** (positive/actionable verdict on failed or absent evidence) | **6**, across 5 files |
| ✅ FAIL-CLOSED (held under every forced failure) | **8** |
| CANNOT-DRIVE | **1** |
| NOT-APPLICABLE (no origin claim) | **5** |
| Structural shape ② still live (one check's exception kills every later check) | **4 checks in 1 file** |

⚠️ **FALSE ASSURANCE (6) and FALSE ALARM (4 live + 1 historical) ARE COUNTED SEPARATELY AND NEVER POOLED**
— WALTER's 9/6 scope line. The 9/5 nine reported SUCCESS wrongly and failed SILENT; `auto_load_budget`
(`08336d2a9`) INVENTED a violation and failed LOUD. Opposite directions; pooling loses the family's distinction.

## THE GREP CENSUS WOULD HAVE MISSED MOST OF THIS — measured
Not one of the six FAIL-OPENs is findable by grepping the two known shapes (`git log --all`, `except: return True`).
They are: a **missing `returncode` check** (F-4, F-5), an **rc lost to a PIPE** (F-2), a **`glob()` on a missing
directory returning empty and raising nothing** (F-3), a **dereference outside the `try`** (F-6), and **an entire
verification STEP simply absent from a forked copy** (F-1). WALTER said this in the row; it reproduced exactly.

## 🔴 THE SIX FAIL-OPEN DEFECTS
| id | artifact | the defect, in one line | owner |
|---|---|---|---|
| **F-1** | `AGENTS/CARL/scripts/safe-push.sh:78` | An unfixed **fork** of the fleet receipt: steps ①–⑥ byte-identical to canon, **step ⑦b (32 lines of post-push verification) simply missing.** A push that exits 0 without landing prints `Pushed.` rc=0. A/B against canon with the same shim: canon says `NOT PUSHED: HEAD … is NOT on origin/master` rc=1. | **CARL** |
| **F-2** | `scripts/session_banner.sh:17` | `git status` rc lost to a pipe ⇒ `DIRTY=0` ⇒ the **SessionStart hook of every session** prints **"tree clean"** over a dirty tree. | **DAEDALUS — FIXED TODAY** |
| **F-3** | `PROME/tools/prome_gate.py:745,753` | The **BLOCKING** `.claude` parity gate builds its set from `Path.glob()`. Glob on a missing dir yields nothing and raises nothing, so **empty is indistinguishable from "all agree"**: both trees absent → `[BLOCKING] PASS \| 0 definition(s) identical`; dirs renamed in both trees with real byte-drift inside → `PASS \| 1 identical`. Currently **latent** (all 11 real files sit at glob-matching paths). | **PROME** |
| **F-4** | `PROME/tools/agent_freshness.py:55-66` → `prome_gate.py:610` | `git()` never reads `returncode`; `own_surface_age_days` returns `None` on git failure **and** on a desk with no history; the consumer writes `(… or 0) > 7`, so **`None` becomes "0 days old"**. A desk with **zero commits — the most stale state possible — is the one state this check structurally cannot flag.** | **PROME** |
| **F-5** | `PROME/tools/spawn_list.py:107,123` | `git log`'s rc unread ⇒ empty stdout ⇒ verdict **`DARK`** with the reason *"no self-commit found in history"* — a completed-search claim from a search that never ran. ⚠️ **`DARK` at a due row IS the WQ-184 Tier-1 spawn trigger.** `--selftest` **11/11 PASS**: the suite does not cover the git-failure path. | **PROME** |
| **F-6** | `PROME/tools/hooks/git_guard.py:97` | `data.get(...)` dereferenced **outside** the `try`. Hook input that is valid JSON but not an object (`[]`, `null`, `"ok"`, `3`) raises `AttributeError` → **rc=1**, and the PreToolUse contract reserves **rc=2** for blocking, so **rc=1 is non-blocking and the git command runs unlinted.** The identical shape L339-② was hardened against on 9/11, in a file nobody re-checked. | **PROME** |
| **F-7** | `prome_gate.py` `check_gates_tsv:160` · `check_docket_overdue:195` · `check_docket_today:225` · `check_symmetry:620` | Inputs dereferenced outside any `try`; `main():888` wraps nothing ⇒ a missing input **kills every later check and the summary**. **Fail-LOUD, so not false assurance — it is silent LOSS OF COVERAGE.** This is the half of the 9/11 L339-② finding that was fixed only at the reporting check. | **PROME** |

## ✅ WHAT HELD — the fixes are real, and saying so is part of the sweep
`scripts/safe-push.sh` **fail-closed on all three legs** (pre-fetch fail rc=1 · post-fetch fail → `CANNOT-CONFIRM …
the receipt cannot be issued either way` rc=2 · silent no-op push → `NOT PUSHED` rc=1). The reference
implementation is sound. **WALTER's three instruments hold** under every forced failure — `_sync_state` returns
`'unknown'` including on the exact 9/5 rc=0-empty case; `_ever_in_git` returns `None` not `False`;
`reconcile_delivery_log` exits 1 and flips nothing. **WALTER's own regression suite ran: 67/67 behavioural
assertions pass, rc 0**, its §MUTATION section included. **`boot_session.py` fail-closed across 8 drills.**
**The L339 receipt fix holds across 9 drills**, malformed-receipt cases included — ①/② from PROME's packet are
genuinely closed, and I verified that rather than accepting the report.

## ⚠️ THE PIPELINE-`$?` WRAPPER — I RULE IT **INSIDE** L294's PERIMETER
PROME asked me to rule it. **Empirically confirmed:** a stub exiting 1 reports `RC=0` through `| tail -80`, `| head`,
and in a fresh `bash -c` — and through `| grep` it reports rc 1 *for grep's no-match*, the same value for a
different reason, which reads correct and is not.
**Ruling: IN PERIMETER.** L294's invariant is about *verdicts asserted from evidence that was never gathered*. An
invocation that structurally cannot observe its own gate's verdict is that failure at the call site instead of
inside the tool; the tool's honest rc=1 is destroyed by the wrapper just as surely as by an unread `returncode`.
**But the class is NOT a documentation problem.** The census found **ZERO documented recipes** with that shape
(SEARCH-NOT-FOUND across every `.md`/`.sh`/`.py`/`.json`/`SKILL.md`/`BOOT.md`/`CLOSEOUT.md`); every hit is a
*description* of the defect, including my own `CHECK_STANDARD.md:37` which already states the rule and the
mechanics. **The fleet wrote the rule down four times and then shipped two executable instances of it.**
`finding_a_check_that_only_advises_is_overridden_the_control_is_downstream`, applied to prose.
**Executable instances in perimeter: exactly two, both mine, both FIXED TODAY** (F-2 and FA-1). `PIPESTATUS`
appeared in **0** executable files before today.
**Mechanical control proposed, not another sentence:** a one-line lint for any repo `*.sh` that pipes and lacks
`set -o pipefail`. **Prefer promoting an existing control** — it belongs in `validate_all.py`, not a new tool.

## FALSE ALARMS — separate ledger, opposite direction
**FA-1** `verify_push.sh:72` — `git log | grep`: a FAILED log and a no-match log were byte-identical downstream,
both falling through to rc=1 `NOT ON ORIGIN — Your work is still local.` **The tool's own contract reserves rc 2
for exactly that state.** ⚠️ **It survived the `eb6a80d8c` fix because that pass hardened the fetch and the
rev-parse and left the one leg whose failure travelled through a pipe** — `finding_a_guard's_scope_is_narrower_
than_the_failure_it_was_built_for`. **FIXED TODAY.**
**FA-2** `reconcile_delivery_log.ever_in_git` — rc=0-empty → `False` = "origin has NEVER seen it". Safe direction.
**FA-3** `walter_doctor._origin_ref` — a rev-parse failure and a genuinely absent ref both → `'no_origin'` (INFO,
should be LOW `'unknown'`). Severity mis-tier only; the all-clear is still suppressed.
**FA-4** `claim_check.py:119-126 hash_state` — **no UNKNOWN state at all**: any git failure maps to `unreachable`
or `missing`, both of which flag. Fails safe, but produces a defect report where the truth is "git could not answer."

## A FLEET-WIDE LIMITATION, DECLARED NOT GRADED
**`walter_doctor`, `reconcile_delivery_log`, `claim_check`, `spawn_list`, TERRY `boot.py`, YEYOU `boot.py` — NONE
of them fetches.** (`grep -n fetch AGENTS/WALTER/tools/walter_doctor.py` → **SEARCH-NOT-FOUND, at the
owner-declared path.**) They read a **cached** `origin/master`. I checked the DIRECTION for each: a stale cached
ref lacks commits origin has, which makes their verdicts read **worse** than truth (`ahead`, `real orphan`,
`unreachable`, `DARK`) — the false-ALARM direction. The single exception is a rewound origin, which this fleet
never does. **So "no fetch" is a declared limitation, not a defect** — but `_sync_state`'s return token
`on_origin` means "on the last-fetched origin/master", and **no caller says so.**

## THE SECOND SHAPE (WALTER ④) — a check whose REFERENCE nobody re-reads
**`AGENTS/DAEDALUS/scripts/complete_check.py:4-5`, mine, and it is wrong:** it calls `orphan_check` / `claim_check`
/ `safe-push` *"the COMMITTED-checks … all answer 'did files reach origin?'"* — **VERIFIED false for two of three.**
`scripts/orphan_check.sh:56` reads only `git status --porcelain`, purely local, never touches origin; `claim_check`
answers the origin question **only** for its `hash` class, not the weekday/date classes the fleet actually runs it
for. A reader taking that sentence at face value believes origin coverage exists where it does not. No wrong
output from the tool — the defect is in a sentence I wrote. **Mine to fix; carried, see below.**
**`AGENTS/YEYOU/scripts/boot.py:9`** — *"Assumes origin/\* is current"* and nothing verifies it. YEYOU is RETIRED,
so this is a note, not an obligation.

## INCIDENCE — UNKNOWN, PER INSTRUMENT, AND THAT IS THE HONEST ANSWER
WALTER's own caveat, and it governs this whole record: **a drill establishes VULNERABLE BEHAVIOUR, never how
often it fired.** Nothing in this sweep licenses a claim that any of F-1…F-7 ever produced a wrong live verdict.
**No historical incidence is asserted anywhere above.** F-3 is additionally **latent today** by measurement.

## DISPOSITIONS
| id | disposition |
|---|---|
| F-2 · `scripts/session_banner.sh` | **FIXED + DRILLED BOTH DIRECTIONS.** rc captured off the pipe; a failed `git status` now prints `[git status FAILED — dirty-tree state UNVERIFIED; do NOT trust 'tree clean'…]`. Watched: clean case flags 6 dirty paths; capable case prints the new flag. |
| FA-1 · `verify_push.sh` | **FIXED + DRILLED ALL THREE rc STATES** (0 on origin · 1 genuinely absent · **2 when `git log` fails**, previously 1). Second unchecked pipe (`NMATCH`) removed by reusing the already-verified output. |
| F-1 | **PACKET TO CARL.** Rec: replace with a pointer to `scripts/safe-push.sh`, or delete. ⛔ **Do NOT back-port ⑦b into a second copy — two copies is how it diverged.** |
| F-3 · F-4 · F-5 · F-6 · F-7 | **PACKET TO PROME** — `PROME/tools/` is PROME's, not mine. F-5 first: it feeds the spawn driver. |
| The pipefail lint | **Proposed as a `validate_all.py` leg**, not a new tool. Not built today (scope). |
| `complete_check.py` header | **Mine, carried to my next touch** — a correction pass is unreviewed work and I am past the two-correction stop on today's tool set. |
