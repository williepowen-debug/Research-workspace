# Console memory agent ("keeper") — build drafts

**Written:** 2026-10-17 12:47 ET · DAEDALUS (daedalus-6d, desktop) · **For:** PROME (synthesis and Will's decisions), Will (approval and `ant apply`)
**Basis:** Will's brief, verbatim in `PROME/plans/2026-10-17_console-memory-agent-PLAN.md` § 3b (12:42 ET), and PROME's reading of it (§ 3b "What this settles", § 4 revised). PROME commissioned these drafts at 12:43 ET.
**Status:** DRAFT. Nothing applied, nothing created on the Console, $0 spent. These files are `ant apply`-shaped (Managed Agents' version-controlled resource format); applying them is Will's step, in his own terminal.

## What's here

| File | What it creates on the Console | Notes |
|---|---|---|
| `agents/keeper/agent.md` | The agent: Opus 5.5 plus the system prompt (the Markdown body) | Working name **keeper**; the real name is Will's to choose. Tools: read, write, edit, glob, grep, bash, all `always_allow`; web off; **outside systems: none**. |
| `agents/keeper/environment.yaml` | The sandbox | Network `limited` with **zero allowed hosts**: the agent can reach nothing but its own files. |
| `agents/keeper/memory_store-will-memory.yaml` | The memory store, Will's externalized memory | Layout below. |
| `agents/keeper/memory_store-relay-state.yaml` | A small bookkeeping store for the Telegram relay | Never attached to the agent. Holds the lease and the delivery ledger so the desktop and laptop relays share state (relay spec § 5). |
| `agents/keeper/deployment-morning.yaml` | The 06:00 ET daily run | $2 cap per run. **Applied last**, after a manual test run has been reviewed. |

Relay (the Telegram courier): `../CONSOLE_AGENT_TELEGRAM_POLLER_SPEC_2026-10-17.md` (v2). Channel comparison (now decided: Telegram): `../CONSOLE_AGENT_CHANNEL_OPTIONS_2026-10-17.md`.

## Store layout (`will-memory`)

| Path | Written by | Purpose |
|---|---|---|
| `inbox/YYYY-MM-DD/HHMM-<id>.md` | the **relay**, before any model runs | Raw capture, Will's exact words (voice transcribed and marked). The agent appends only a `filed:` line. |
| `threads/<slug>.md` | agent | One live idea: what · state · last_touch · next · captures |
| `parked/<slug>.md` | agent | Parked or killed threads |
| `profile.md` | agent **and Will** | How Will works. His lines win, and each agent line is marked said (quote + date) or INFERRED (+ evidence). |
| `picture.md` | agent, each morning | The agent's synthesis; inferences marked |
| `log/YYYY-MM-DD.md` | agent, 06:00 | The day's brief, exactly as sent |

## Decisions, as they stand

| Plan § 3 | State | Source |
|---|---|---|
| 1 Scope | PERSONAL | PROME's reading of Will's § 3b words |
| 2 Kickoff | Will (Telegram) + 06:00 schedule | same |
| 3 Channel | Telegram, NEW bot, voice included | same |
| 4 Outside systems | **EMPTY.** No MCP servers, no hosts | PROME rec: none at first; Will hasn't named one |
| 5 Model | Opus 5.5 | same |
| Rule (i): profile is Will's to read and edit | **Drafted into the prompt; awaiting Will's confirmation** | plan § 3b |
| Rule (ii): decay/park with a two-word kill | **Drafted (14 days → resurfaced; `kill <slug>`); awaiting Will's confirmation** | plan § 3b/§ 4 |
| Agent name | **OPEN.** "keeper" is a placeholder | Will |

## Where these drafts depart from the plan, and why

1. **bash is ON** (always_allow). ⚠️ This reverses my own 12:39 recommendation ("bash and web off"). Two things need it:
   - **The clock.** A scheduled run has no other source of today's date, and the static kickoff text can't carry one. A brief that misdates itself fails at its one job.
   - **Parking.** Moving a thread into `parked/` is a file move, and the file tools can't delete.

   The risk stays contained: the environment allows **zero network hosts**, so bash can touch only the sandbox and the mounted store, and every store change is a recoverable version. The no-stall property I asked for still holds, because every enabled tool is `always_allow`.
2. **Captures are one file each** (`inbox/YYYY-MM-DD/HHMM-<id>.md`), not one file per day. The relay writes captures and the agent writes filing lines. Separate files mean the two never edit the same file at once, and no single file creeps toward the 100 KB limit.
3. **A second, tiny store** (`keeper-relay-state`) exists so the relay can follow Will between machines (relay spec § 5).
4. ⚠️ **For PROME, a plan-file inconsistency.** Plan § 4 still carries the first draft's bullets beside the revised ones: the `/people/`, `/commitments/`, `/preferences.md` layout and the "commitments due in 7 days" kickoff. A cold reader gets two live layouts. These drafts follow the revised lines (threads/inbox/profile/picture/parked/log). The plan is PROME's to fix.

## Apply sequence, for Will when approved (nothing here runs until then)

0. **`ant` is not installed on this desktop** (checked 2026-10-17). Install it first (Anthropic's CLI; version 1.34.0 or later), then `ant auth login` against the org that holds the $200 credits. Check that `ant auth status` names that org and workspace.
1. From `AGENTS/DAEDALUS/builds/console_agent_2026-10-17/`:
   - `ant apply --dry-run agents/keeper` is the walk check. It must list exactly the five files above.
   - Then `ant apply agents/keeper/agent.md agents/keeper/environment.yaml agents/keeper/memory_store-will-memory.yaml agents/keeper/memory_store-relay-state.yaml`. **Not the deployment yet.**
   - The first run writes `claude-lock.json` (resource IDs) here. Commit it.
2. **Seed `profile.md`** with Will's own brief (plan § 3b, verbatim, dated 2026-10-17) as the first "said" lines, through the Console's memory store page or one SDK `memories.create` call. The agent then starts from his words, not from inference.
3. **Smoke test without Telegram.** Open a session in the Console with `will-memory` attached, send three captures by hand, and check that they land in `threads/` with one-line replies.
4. Build the relay (separate approval, spec v2), create the new bot, and test captures from the phone.
5. **One manual run of the morning brief, before the schedule exists:** a Console session with `will-memory` attached and the deployment's kickoff text. Read the brief and the store it left before trusting the schedule. (A deployment's own manual-run endpoint needs the deployment to exist already, which would also arm the next 06:00. That's why this step uses a plain session.)
6. `ant apply agents/keeper/deployment-morning.yaml`. The schedule is live from the next 06:00.

**Cost guard rails:** $2 per morning run (in the deployment file). The relay sets a $10 cap on each day's interactive session. Budgets pause a session; they never delete anything. Two-week measure (plan § 4): if the agent caught nothing Will would have lost, stop.
