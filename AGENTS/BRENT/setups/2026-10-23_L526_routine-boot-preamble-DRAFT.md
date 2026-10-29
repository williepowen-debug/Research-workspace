# L526 — routine boot preamble: BRENT's DRAFT prompt edit (NOT INSTALLED)

> **INSTALLED 2026-10-28 23:46 ET (WQ-510 A, Will "510 A approve").** The fenced block below went live in all four routines with `<date>` filled as 2026-10-28; nothing else changed. Receipt: [install report](../audits/2026-10-28_L526-preamble-install/REPORT.md). The text below is the unchanged draft, kept as the approved record.

**Drafted:** 2026-10-23 15:53 ET (from `date`) by BRENT (live session). **Row:** `PROME/DOCKET.tsv` L526. **Spec:** `AGENTS/DAEDALUS/design/2026-10-14_L526_ROUTINE_BOOT_PREAMBLE.md` (commit 4d179ddb1). **Install:** Will's word only. PROME presents this draft as a WQ row. $0; no threshold, route or authority change.

## Which file the routine actually reads
The routines read their **live cloud prompts** at claude.ai/code/routines (four IDs in `SCHEDULED_RUNS.md` § Live routines). The repo holds only saved after-images: `audits/2026-10-02_routine-install/after_{monday,wednesday,thursday,friday}.txt`. Their sha256 prefixes match the registry today (0ef41c90ae9d270e, 7661136cc643482b, 0ff0bf2627d1e8ef, 68e0cd26f0f8952c). The live prompts were last verified 10/02 and the 10/04 saved correction is still UNVERIFIED live, so this draft edits the saved images. Live text could differ.

## The edit: insert this block in all four prompts, directly after the first paragraph ("You are BRENT …")

```
BOOT PREAMBLE (L526, installed <date> on Will's word). Run before ANY read or write, in this order. Every step is fail-loud; never force, never reset, never rebase.
1. If .git/shallow exists: git fetch --unshallow origin. Otherwise: git fetch origin.
2. If HEAD is detached: git checkout master.
3. git merge --ff-only origin/master. If that is not a fast-forward, STOP: print `git rev-list --left-right --count master...origin/master`, write nothing, commit nothing, push nothing, and end the run with that line as your report.
4. If .venv/bin/python is not executable: python3 -m venv .venv && .venv/bin/pip install -r AGENTS/BRENT/scripts/routine-requirements.txt. If that file is missing or the install fails, STOP and name the failure; do not install packages ad hoc into the system interpreter.
5. First line of your output file AND of your final report: PREAMBLE: unshallowed=<y/n> detached=<y/n> ff=<commits fast-forwarded> venv=<present|rebuilt>
Use .venv/bin/python3 for every repo script after this preamble.
```

## Where the spec meets how the routine really boots (said, not adapted silently)
| Spec line | Reality | Handling in the draft |
|---|---|---|
| Step 4 "the routine's pinned requirements" | **No requirements file existed.** That gap is the first finding. The 10/16 Friday run worked around it by installing openpyxl into the system python (its own §header) | Draft file `scripts/routine-requirements.txt` (pins from the desktop .venv, 10/23). Step 4 forbids the ad hoc system-python install |
| Step 3 "write nothing" | The prompts' existing Git line says "Follow current root Git Protocol". Its pull safeguards assume a shared dirty tree, which a fresh container doesn't have | No conflict. The preamble runs first. Root protocol still governs the closeout push and the non-ff recovery (session-end step 3) |
| Step 5 receipt "in the routine's output" | Outputs are `demand_destruction/data/*_YYYY-MM-DD.md` plus the run report | Put on line 1 of both, so a reader of either sees it. AC4 (quiet path) is watched the same way |
| Step 3 fail case | On a diverged master the routine would still need to report, and it can't write a file | Its final report is the only output. **Open question for PROME:** does a no-write run reach anyone? If no one reads routine run reports, AC2 is invisible. Proposed: Will checks the routine run log for the first two runs (the spec's independent reader) |

## Not checked (carried from the spec, still open)
- Whether the false fork recurred after 9/28. I did not read routine run logs.
- Why the container arrives shallow (likely a default shallow clone; UNVERIFIED).
- This session lists a `RemoteTrigger` tool among its deferred tools. The 10/04 report said no routine-control capability existed. I did NOT load or call it: installing is Will's word. If it works, it could also close the 10/04 live-prompt reconciliation that is still open. That one is PROME's to test.

## Acceptance (unchanged from spec, WQ-229): AC1–AC4 checked by an independent reader on the first two runs after install.
