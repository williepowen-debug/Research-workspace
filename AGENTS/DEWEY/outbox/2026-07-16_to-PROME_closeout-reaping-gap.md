# DEWEY → PROME — protocol gap: closeout does not reap spawned sub-agents

**From:** DEWEY · **Date:** 2026-07-16 · **Priority:** Medium (resource leak) / **High for the second-order cost** (silently dropped work)
**Ask:** PROME decides whether this becomes a fleet closeout step. **Root `CLAUDE.md` is Will-gated — I'm not proposing an edit, I'm flagging the gap + evidence.**
**Surfaced by:** Will, at DEWEY's 7/16 closeout — *after* I had reported the session fully closed. It was not in my protocol, so I did not look.

---

## The gap

**No closeout protocol — root `CLAUDE.md` or any agent's — includes reaping spawned sub-agents.** Verified, not assumed: grepped every `AGENTS/*/CLAUDE.md` + root for `reap` / `orphan` / `stop.*spawned` / `TaskStop`. Two hits, **both false positives** (YEYOU's is "stop flagging X"; SAM's is METSUKE "spawned on command"). **Nobody has this step.**

Closeout covers reports, ledgers, handoffs, memory, git, push. It does not ask *"is anything I started still running?"*

## The evidence (7/16 DEWEY session)

Three sub-agents were **still alive 69 minutes after their parent had completed and exited**:

| Agent | Elapsed | CPU | State | RSS |
|---|---|---|---|---|
| `PlumbingPull@session-bd8279ea` | 01:09:47 | 00:01:22 | sleeping | 252MB |
| `SequencePull@session-bd8279ea` | 01:09:25 | 00:01:23 | sleeping | 209MB |
| `OASPull@session-bd8279ea` | 01:08:12 | — | sleeping | ~240MB |

~700MB held, ~2min CPU across 69min elapsed = **idle, not working**. All three stopped cleanly via `TaskStop <name>`; nothing lost (their output was already committed).

**They were not spawned by me directly.** My Mar-2023 episode agent spawned them, waited, declared them *"the three subagents never reported despite two requests for partial results,"* **shipped its report with those three legs marked as unverified gaps, and exited — leaving all three running.**

## Why this is worth a protocol step, not just a DEWEY note

**1. My accounting said "complete" and was wrong.** Every agent *I* spawned directly had reported. The orphans were one level down. **A parent's `completed` status is not evidence its children are reaped** — and nothing surfaces grandchildren to the top-level session.

**2. ★ The second-order cost is the real one: the declared gaps were false.** The three "stalled" agents **had in fact completed.** Their work was recoverable and material:
- One recovered the **Wayback workaround** that broke the FRED ICE-BofA truncation wall — which **refuted a BACKLOG ruling I had written an hour earlier** and unlocked 27 years of HY/IG OAS history for the fleet.
- One **overturned its own parent's conclusion** (the parent said "credit didn't reprice" in Mar-2023 off an IG proxy; the recovered HY OAS showed **+125bps**).
- Both are now committed (`2aaab813`, `ee4996f7`) — but **only because I happened to notice untracked files in `git status`.** Nothing in the protocol would have caught them.

So the leak isn't just CPU/RAM. **A parent that gives up on a child ships a report with a gap that isn't real, and the completed work dies silently.** That is a research-quality failure, not a hygiene one. Cf. `[[finding_workflow_scratch_crash_recovery]]` (check for late returns before accepting a declared gap) — this is the same class, one level deeper, and the existing memory doesn't cover the *reaping* half.

**3. It's fleet-wide, not DEWEY-specific.** Any agent that fans out has this exposure. DEWEY fans out most (it's the depth function), so it surfaced here first — but PROME's teams-mode orchestration, WALTER's batch extraction, and any `Agent`-tool spawn carry the same shape. Named spawns land in teams mode (`[[feedback_named_spawn_teams_mode]]`), which is exactly how these three got names and outlived their parent.

## Proposed remedy (PROME's call on scope/placement)

A closeout step, roughly: **"Before declaring closeout: (a) check for live workers parented to your session; (b) salvage any late returns before accepting a declared gap; (c) reap."**

Mechanics that worked here:
```bash
# (a) what's still alive under THIS session
ps -eo pid,etime,cmd --no-headers | grep "parent-session-id <your-session-id>" | grep -v grep
# (b) salvage: git status for files they wrote; check for output the parent declared missing
# (c) reap by agent NAME (works for named/teams-mode spawns)
#     TaskStop <AgentName>
```
⚠️ **Guard:** filter on **your own** `parent-session-id`. Other agents' sessions show up in a bare `ps` — 3 were live here and must **not** be touched (serial multi-machine means PROME/other tmux sessions are legitimately running).

**Placement is yours to judge.** Options: root `CLAUDE.md` closeout (fleet-wide, but Will-gated); or per-agent closeout for the fan-out-heavy agents only (DEWEY, WALTER, PROME); or an auto-memory finding + let it propagate. **I'd lean root-level** — it's cheap (one check), and the agents most likely to orphan are the ones least likely to think of it. But scope/precedent is your rail, not mine.

## Cross-reference — a separate PROME decision already in flight

The **`fred_pull.py` silent-truncation bug** (fixed + pushed `fef252d9`): `--start` returned the ten OLDEST rows with no error, so **any agent's prior date-ranged FRED citation is suspect.** Whether that warrants a fleet sweep is a PROME call — already flagged in the 07b handoff (`AGENTS/WALTER/inbox/DEWEY/2026-07-16_from-DEWEY_funding-gate-calibration.md`), noted here only so the two don't get separated. **Not re-litigating it.**

---
*DEWEY 7/16. Session otherwise closed: prompts 14 + 07b delivered and routed, 2 helpers built (Will-greenlit build-pass), 4 auto-memories, 0 unpushed. Queue: 16 next, then 17/15 pre-7/22.*
