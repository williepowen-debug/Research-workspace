# NISABA: Will's Console thinking companion (experiment)

**Updated:** 2026-10-17 13:27 ET · DAEDALUS · **Mode:** experiment. Will, 13:11 ET: "lets try somethings and see if any of it feels good or sticks". Light process: no gates and no phased plan.
**Discussion:** `FORUM/keeper/` (PROME · DAEDALUS · DEWEY). **Plan:** `PROME/plans/2026-10-17_console-memory-agent-PLAN.md`. **Research:** `AGENTS/DEWEY/output/2026-10-17_keeper-thinking-companion-research.md`.

## Use it today
1. In the Console, **Create agent**: paste **`console-panel-nisaba.yaml`** (this folder) into the Agent config panel.
   - If the panel rejects the tool block, set the switches by hand: read, write, edit, glob, grep and bash **on**, each "always allow"; web search and web fetch **off**.
2. **Environment:** cloud. Networking **limited**, **no allowed hosts**, MCP servers off, package managers off (`agents/nisaba/environment.yaml`).
3. **Memory store:** create `nisaba-memory` and paste the `description:` from `agents/nisaba/memory_store-nisaba-memory.yaml`.
   - Optional: seed `profile.md` with Will's own words from the plan § 3b.
4. **Start session** with `nisaba-memory` attached read-write. Set a session budget, e.g. $5, as cheap insurance. Then talk to it.

## Files

| File | What it is |
|---|---|
| `agents/nisaba/agent.md` | **Current: the companion prompt (v4)**, the single source |
| `console-panel-nisaba.yaml` | GENERATED from agent.md by `render_console_panel.py`, the thing you paste. Re-run the script after any agent.md edit. After a Console edit, "Export as code" and fold the change back into agent.md. |
| `agents/nisaba/clerk-v1.md` | The first, capture-and-file "clerk" prompt, kept for comparison |
| `agents/nisaba/environment.yaml`, `memory_store-nisaba-memory.yaml` | Sandbox (no network) and the memory store |
| `agents/nisaba/parked-*.yaml` | The 06:00 schedule and the relay's bookkeeping store. **Parked, not in v1.** Renamed so `ant apply` ignores them. |

Later, only if it sticks:
- **Telegram capture from the phone:** `../CONSOLE_AGENT_TELEGRAM_POLLER_SPEC_2026-10-17.md` (designed for the clerk; trim before use).
- **A schedule:** un-park the deployment and rewrite its kickoff for the companion.
- **Moving it onto Will's own system:** the prompt is this text file; the memory is plain text files that can be downloaded from the Console.

**Code path** (optional): `ant apply agents/nisaba/agent.md agents/nisaba/environment.yaml agents/nisaba/memory_store-nisaba-memory.yaml` from this folder. `ant` isn't installed on the desktop yet. History of the earlier clerk-era README: git log of this file (528d63b1f).
