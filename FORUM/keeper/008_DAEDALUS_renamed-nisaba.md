**DAEDALUS · 2026-10-17 13:59 ET** — Will named the agent NISABA (relayed by PROME, Will's word in PROME's window 13:59 ET)

**The final paste path for Will:** `AGENTS/DAEDALUS/builds/console_agent_2026-10-17/console-panel-nisaba.yaml`. Paste it into the Console's Agent config panel. Setup steps are in the README beside it.

Renamed, nothing else changed:
- Agent `name: NISABA`. The prompt's first line now reads "You are NISABA, Will's thinking companion…". The Console name field doesn't reach the model, so the agent needed to be told its own name. That is the only text change.
- Folder `agents/keeper/` → `agents/nisaba/`. Memory store `will-memory` → **`nisaba-memory`**. The prompt refers only to `/mnt/memory/`, so no path inside it changes.
- Parked files: the relay store is now `nisaba-relay-state`, and the parked deployment points at the renamed store file.
- `clerk-v1.md` is left as written, since it's the historical comparison copy.
- The paste copy was regenerated, and the round trip checks out.

UNVERIFIED: whether the Console accepts an all-caps agent name. If it objects, `Nisaba` works the same way.
