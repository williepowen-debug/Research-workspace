# Agent Launcher

Open a WSL terminal and run `agents`, or double-click **Agent Launcher.cmd** on
the Windows desktop. Choose an agent, runtime, and **new** or **resume**.
No model/session starts until you choose an action. Use one terminal per agent.

```bash
agents                         # menu
agents carl                    # CARL, choose new or resume; default Sol
agents carl --claude            # CARL on Claude, choose new or resume
agents stue --sol --new         # start STUE on Sol
agents polly --resume           # choose a saved POLLY Codex conversation
agents cato --new               # existing CATO Astra launcher
agents carl --dry-run           # inspect the command; start nothing
agents --list                  # configured names and missing folders
```

For an explicit task on a new session:

```bash
agents carl --new --task 'Review the latest approved consumer-credit work.'
```

The task is passed as text after the startup instructions, never evaluated as
shell code. Resume opens the selected runtime's own session picker; it never
guesses the newest session. If the agent is already running, return to that
terminal. For a detached tmux terminal, use `tmux ls` and `tmux attach -t NAME`.

## Defaults and scope

- Codex defaults to **gpt-6.1-sol** with full access and approval prompts disabled.
- Claude uses `--dangerously-skip-permissions` and the configured model, except
  CYPHER retains its explicit Claude model from the command sheet.
- CATO keeps its existing **Astra / workspace-write / on-request** policy.
  `--sol` and `--claude` are rejected for CATO instead of changing its policy.
- WALTER retains its Claude Telegram channel option in new and resume modes.
  Running WALTER in Codex does not establish Telegram connectivity.
- CARL's specialists use their nested folders. Project folders and startup files
  are checked; the launcher never creates missing desks or substitutes another.
- The configuration contains the command sheet's 50 distinct targets plus CATO.
  VIRGIL and ZION are retained references whose folders were absent on the
  installation machine. It is a personal menu, not a new fleet roster, schedule,
  or grant of launch authority. Existing restrictions, including CREED's manual
  permission condition, remain with their owners.

The launcher holds a local file lock while its interactive child CLI runs.
Two launcher windows cannot simultaneously open the same resolved folder, even
with different runtimes or names. This does **not** detect manually opened
sessions, a Codex task that outlives its terminal, other launchers, or sessions
on another machine. Killing the launcher parent can release the lock while its
child remains alive. A released lock never proves a desk is idle or complete.
Old lock files do not block: the operating system lock, not stored PID text,
determines whether another launcher window holds the folder.

No Git pull, background wake, direct message, global process scan, or automatic
restart occurs. A failed command is reported with its exit code, never retried.

## Files and installation

- `scripts/agents.py`: menu, command construction, and local terminal supervision.
- `scripts/agents.json`: editable launch targets/settings; read on each invocation.
- `scripts/install_agents.py`: creates the local shortcuts; starts no agents.
- `~/.local/bin/agents`: machine-local shortcut, outside Git.
- `~/.cache/research-agent-launcher/`: local lock files (or under `XDG_CACHE_HOME`).

Repository paths in the configuration are relative to the checkout. Separate
projects use `~/...`, resolved against the current user's home. Configuration
changes take effect next launch. Keep startup instructions in the owning desk.

After syncing the repository to another machine, install its terminal shortcut:

```bash
python3 ~/Research-workspace/scripts/install_agents.py
```

Optional Windows desktop launcher (use that machine's real desktop path and
installed distribution name):

```bash
python3 ~/Research-workspace/scripts/install_agents.py \
  --desktop /mnt/c/Users/willi/OneDrive/Desktop --distro Ubuntu
```

Add `--dry-run` to inspect exact files before installation. Existing differing
files and symlinks are refused rather than overwritten. Identical installations
are reusable. No shell/profile files are edited. The desktop launcher uses the
specified WSL distribution and installer user's Linux account.

Direct fallback if the shortcut is unavailable:

```bash
python3 ~/Research-workspace/scripts/agents.py
```

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s scripts/tests -p test_agents_launcher.py -v
```

Tests use isolated projects and fake CLI executables; they never call a model.
Dry-run checks paths, required startup files, and executable presence, not account
access, model availability, full runtime behavior, or whether another owner is
running. Installation verification checks file contents; it does not prove a
Windows desktop click works. Live use is the next observation.
