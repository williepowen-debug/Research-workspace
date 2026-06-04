# Proposal — Migration Checklist: Shared Folder → Separate Clones

**Status:** REVIEW-NOT-APPLY draft. Execute via Will-and-Prome decision, not unilaterally.
**Author:** SAM, Thu Jun 4 2026
**Pairs with:** `2026-06-04_separate_clones_CLAUDE_md_section.md`
**Execution window:** post-Jun-16 BOJ MPM (calm operational period after dominant catalyst resolves)
**Expected duration:** ~60-90 min from "all agents stopped" to "all agents running on new clones"

---

## TL;DR

1. **Pre-flight:** sanity-check the cross-agent-UNcommitted-read frequency assumption + Will-decide the venv strategy.
2. **RED-first SETUP smoke-test** (clone + venv + boot + one trivial push) to validate mechanics in isolation. NOT mixed-production.
3. **Atomic cutover:** stop ALL agents → create all clones → restart all on new paths in one session. No "some on old, some on new" interim.
4. **Post-migration validation:** boot each agent on new path, verify domain work + cross-agent reads work via the new flow.
5. **Rollback plan:** old shared folder retained read-only for 1 week minimum; if anything breaks, agents revert to old paths.

---

## Pre-flight (BEFORE migration day)

### P1. Sanity-check the cross-agent-UNcommitted-read frequency

**Why this matters:** the proposal claims agents can switch from "read other agent's working tree" → "pull other agent's pushed state" with acceptable friction. That claim is the load-bearing assumption of the whole architecture. **Validate it explicitly before committing to the migration.**

**How to validate:**
1. For 3-5 sessions before migration, agents log every cross-agent file read in MAINTENANCE.md or a temp scratch file. Specifically: filename read, whether the read needed unpushed state, and what the agent would have done if only pushed state were available.
2. Aggregate the logs. If unpushed-state reads are < 10% of total cross-agent reads AND have inbox/outbox alternatives, **proceed.** If unpushed-state reads are > 20% OR have no good alternatives, **rethink before migrating.**

**Note: worktrees don't fix this either.** A worktree per agent gives each its own working tree on a per-branch basis, but cross-agent reads from another worktree still see only committed-to-that-branch state. Worktrees address the staging-area race; they do NOT address the unpushed-state-visibility question. If the sanity-check finds unpushed reads are critical, the answer is "improve inbox/outbox tooling," NOT "use worktrees instead."

### P2. `.venv` strategy decision (Will-call)

Two options. Trade-off honestly:

| Option | Setup cost | Maintenance | Shared-mutable-resource risk |
|---|---|---|---|
| **Per-agent venvs:** each clone gets its own `~/agents/<NAME>/.venv` via a setup script | One-time × N agents (~5-10 min × N) | Dependency bumps require N venv updates; each agent independent | None — full isolation |
| **Shared venv at fixed path:** all clones point to one `/home/willi/.venvs/research` (or similar) | One-time, ~5 min | Dependency bumps land once for everyone; if you upgrade Python, all agents shift together | Reintroduced — `pip install` from any agent affects all; less acute than git-staging but still shared mutable state |

**This is a real Will-decision, not a default.** Per-agent venvs are the cleaner architecture (full isolation, matches the "GitHub is source of truth, agents don't share live state" principle). Shared venv is the lower-touch option (less to maintain, mirrors how `.venv/` works today). The right answer depends on:

- How often dependency bumps happen (more often → shared venv saves real time)
- Whether agents diverge in their dependency requirements (yes → per-agent forced)
- Whether the "no shared mutable state" principle is load-bearing (yes → per-agent)

**Sub-option for shared venv:** "read-only after setup" discipline — venv installed once, locked via `pip freeze > requirements.txt`, no agent runs `pip install` ad-hoc. Eliminates most of the shared-mutable risk. Worth considering.

**Decision must be made BEFORE migration day** — the setup script needs to know which path to write to.

### P3. Setup script ready

Prepare and test (in a throwaway location) the script that creates an agent clone:

```bash
# create_agent_clone.sh <AGENT_NAME>
set -e
AGENT=$1
DEST=~/agents/$AGENT
git clone https://github.com/williepowen-debug/Research-workspace.git $DEST
cd $DEST
# venv setup — fill in based on P2 decision
# either: python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
# or:     ln -s /home/willi/.venvs/research .venv
```

Test against a throwaway agent name in a throwaway directory BEFORE migration day. Catches permissions, shell quirks, git auth issues at low blast radius.

### P4. Required-config inventory

For each agent, list every config / env-var / path assumption baked into their boot sequence or scripts. Examples for SAM:
- `.venv/bin/python3` paths in boot.py, dashboard.py, fetch.py
- Workspace-root references in any script
- MEMORY auto-load path (`~/.claude/projects/...`)
- Per-agent settings.json hooks

Most of these will work if agent launches with the new directory as CWD, but verify don't assume.

### P5. Documentation of agent launch paths

Each agent today launches with CWD = shared folder. Document where each agent SHOULD launch under the new model (`~/agents/SAM/`, etc.) and how their Claude Code session gets pointed there. This is a Will + Prome coordination task — the launch environment is outside this proposal's scope but must align.

---

## Migration day

### M1. Stop all agents (Will + Prome coordination)

- Will pauses all Claude Code sessions (every local agent + any auto-spawned sub-agents)
- Prome stops on OpenClaw (so it doesn't push from VPS during the cutover and create races against the in-progress migration)
- WALTER stops (signal routing pauses for the duration)

**Verify all stopped:** no active sessions, no pending pushes, all agents' working trees are either clean or have their last work committed + pushed. **Do NOT migrate with uncommitted work outstanding** — that work either belongs in the agent's last commit or it's a half-done thought that needs to land first.

### M2. RED-first SETUP smoke-test (NOT mixed-production)

Per Will's clarification: this is a **mechanics validation**, not a coordination test. Atomic cutover happens for ALL agents at once; RED-first just makes sure the mechanics work before paying the full cutover cost.

Smoke-test steps:
1. Run setup script for RED: `./create_agent_clone.sh RED` → creates `~/agents/RED/`
2. `cd ~/agents/RED && git pull --rebase` → verify pull works clean
3. Set up venv per P2 decision; verify Python + dependencies load
4. `cd ~/agents/RED && .venv/bin/python3 <any RED boot script>` (or manual import of a known module) → verify boot mechanics
5. Create a trivial test commit: `echo "migration test" >> AGENTS/RED/MIGRATION_TEST.md && git commit AGENTS/RED/MIGRATION_TEST.md -m "RED migration smoke-test"`
6. `git push` → verify push lands
7. From a DIFFERENT location (back in the shared folder, or a temp `~/test` clone): `git pull` → verify the RED commit is visible
8. Clean up: remove `MIGRATION_TEST.md` via a follow-up commit

**Pass criteria:** all 7 steps complete with no errors AND the commit + push + pull round-trip works.

**Fail criteria:** any step errors out → STOP the migration, diagnose. Common issues: git auth (push fails), venv path (import error), permissions on `~/agents/`, dependency missing from venv setup script.

**Note on RED choice:** RED was selected because it has minimal cross-agent dependencies — making it the lowest-risk mechanics test. The cross-agent COORDINATION test happens at atomic cutover (M3+), not here.

### M3. Atomic cutover for remaining agents

If RED smoke-test passed, run the setup script for all remaining agents in parallel or rapid sequence:

```bash
for A in SAM HENRY CARL REGINALD OZK; do
  ./create_agent_clone.sh $A &
done
wait
```

(Adjust agent list to current roster; verify against `AGENTS/` directory listing.)

Each clone independently runs the venv setup per P2.

### M4. Per-agent post-cutover validation

For each agent, before declaring it migrated:

1. `cd ~/agents/<NAME> && git pull --rebase` → clean pull
2. Verify agent's boot script runs without errors (boot.py for SAM, equivalent for others)
3. Verify a known cross-agent read works via the new flow — e.g. SAM reads `AGENTS/LIQUID/STATUS.md` (will be the last-pushed version, not live)
4. Commit a trivial post-migration MAINTENANCE.md entry: `git commit AGENTS/<NAME>/MAINTENANCE.md -m "migration day - separate clones architecture live"`
5. Push; verify lands at GitHub

### M5. Update CLAUDE.md root file

Apply the proposed `## Git Protocol` section replacement from the paired proposal. **This is a SHARED file** (CLAUDE.md at repo root), so it must be committed by exactly ONE agent (recommend: Prome, since Prome owns coordination-layer changes) with all other agents idle. The commit hits the new architecture's edge case — the FIRST committed change to a shared file under the new model. Validates that shared-file commits still route through Prome cleanly.

After this commit + push, all agents on their next session-start `git pull --rebase` will pick up the new CLAUDE.md.

### M6. Resume operations

- Will restarts agents one at a time on their new launch paths
- Prome resumes on OpenClaw (already on its own clone — no change for Prome locally; it just sees the new CLAUDE.md on next pull)
- WALTER resumes signal routing

Operations are back live on the new architecture.

---

## Post-migration validation (Day 1 - 7)

### V1. Run a normal multi-agent session

The first session under the new architecture should be a deliberately normal one — agents do their usual work. Watch for:
- Any agent's boot script breaking on a path assumption
- Any cross-agent read needing unpushed state (logged per P1 — should be RARE since pre-flight validated this)
- Any push collision (expected occasionally — verify the `pull --rebase; push` retry works cleanly)

### V2. First push-collision observation

The new architecture's correctness depends on push-collision handling working as advertised. Engineer one deliberately to validate: have two agents both prepare a commit, push in rapid sequence, verify the second one pulls + retries cleanly. This should be a one-time validation, not ongoing testing.

### V3. Cross-agent signal latency check

Today: cross-agent file reads are zero-latency (direct file system access). Under new architecture: cross-agent reads have `git pull` latency (typically <1 sec but depends on network). If any agent's workflow is sensitive to this, surface it for tooling improvement (e.g., periodic background `git pull` daemon).

### V4. Rollback plan retention

Keep the old shared folder at `/home/willi/Research-workspace/` **read-only** for at least 1 week post-migration. If anything breaks badly, agents revert to old launch paths and old protocol. After 1 week clean operation, the old folder can be archived or deleted.

---

## Rollback (if migration fails)

Rollback is straightforward because the old shared folder still has the canonical state:

1. Stop all agents on new clones
2. Re-point Claude Code sessions back to `/home/willi/Research-workspace/`
3. Each agent does `git pull --rebase` to pick up any commits that landed during the migration window
4. Resume on old protocol
5. Delete or archive `~/agents/` clones

**Trigger conditions for rollback** (any one):
- An agent's boot script breaks and can't be quickly fixed
- Cross-agent coordination breaks (e.g., agents can't see each other's pushed work)
- The venv strategy chosen in P2 turns out wrong AND can't be fixed in-session
- Will's call

**Sunset window:** if no rollback triggered within 1 week, the migration is permanent and old shared folder retires.

---

## Where I might be wrong

I am the agent proposing changes to my own operating environment. The bias is real. The Will-and-Prome review IS the bias check. Specific concerns I'd push myself on:

### 1. The pre-flight sanity-check (P1) might surface that the proposal's assumption is wrong

If agents read each other's unpushed state more often than the proposal assumes, the migration introduces real coordination friction that I'm under-counting. **The pre-flight is the load-bearing validation step** — if it shows >20% unpushed-read frequency without inbox/outbox alternatives, the right call is to defer migration and improve cross-agent coordination tooling first.

### 2. The atomic cutover might be more disruptive than I'm framing

I've called the migration "60-90 min." That's optimistic. Realistic edge cases that could blow it up:
- A venv setup issue surfaces on agent 3 of 5, after agents 1 + 2 are already migrated
- A path assumption in some script breaks under the new CWD
- An agent's settings.json or hook references a path that no longer exists
- The shared CLAUDE.md update collides with something Prome is doing

**The pre-flight setup-script test (P3) and RED smoke-test (M2) catch most of these.** But if you encounter one mid-cutover after multiple agents are already converted, the partial-state recovery is harder than the rollback.

**Mitigation:** explicit "if anything looks wrong, rollback NOW, don't try to fix forward" discipline at M3-M5. Better to lose 60 min and try again next week than to operate in a half-migrated state.

### 3. The "no shared mutable state" principle might not actually be what Will values

I've leaned hard on this principle to justify per-agent venvs vs shared venv. But Will hasn't articulated this preference explicitly — I'm extrapolating from the "GitHub is source of truth" framing. **Will may genuinely prefer shared venv for the maintenance simplification, in which case the per-agent venv recommendation is over-engineered.** Letting it be a real Will-decision at P2 (not pre-resolved by me) is the right move.

### 4. RED-first might be wrong for a different reason than I considered

I picked RED for the SETUP smoke-test because of minimal cross-agent dependencies. But RED is ALSO an agent that I (SAM) sometimes route counter-thesis questions to. If the migration breaks RED's ability to receive my outbox signals, I'm the agent affected — biased pilot choice. **A different agent (say, BROCK or LIQUID) might be more neutral.** Counter: those are MORE cross-agent-coupled, so they're worse for smoke-testing (per the proposal's logic). The trade-off is unresolved; Prome may have a better take.

### 5. Race-frequency forecast is the biggest unknown

The proposal's urgency depends on assumed race-frequency-as-scale. Tonight's `8ac5bf7` is the first observed race. If the trajectory is "races stay at 1 every 3 months even at 10 agents," the migration cost may exceed savings. If the trajectory is "races scale O(N²)," the migration is overdue. **I don't have enough observation data to forecast this confidently — Prome's coordination layer sees more cross-agent interactions and has better data than I do.** Prome's read on race-frequency-as-scale is the right primary input.

### 6. I might be missing operations beyond agent-scope

This proposal is scoped to local agents (SAM, HENRY, CARL, etc.). It doesn't address:
- WALTER's signal routing (does WALTER's separate clone affect inbox/outbox delivery?)
- Prome's existing separate-clone setup (does Prome's clone path coordinate with the new local-agent clones?)
- FORGE (does the trade execution layer have its own path requirements?)
- The shared `.venv` that scripts use (resolved in P2, but the broader tools dir question is unresolved)

**These are Prome's coordination scope, not SAM's.** I'm flagging that they exist but not solving them. The migration plan above is incomplete without Prome's review of the operations layer.

---

## Recommendation

Land this checklist as a Will-and-Prome decision at the post-Jun-16 calm session. **Pre-flight (P1, P2, P3, P4, P5) must complete BEFORE migration day** — they're not optional and they're not in-line with M-steps. Migration day execution then becomes mechanical if pre-flight passed cleanly.

If pre-flight surfaces the cross-agent unpushed-read problem (P1) at >20% frequency, recommend deferring migration entirely until cross-agent coordination tooling (inbox/outbox refinement, agent-to-agent SendMessage discipline) is mature enough to absorb that traffic.

Until migration: **pathspec commits are the tonight discipline** (race-safe within shared folder), no further architecture work needed.
