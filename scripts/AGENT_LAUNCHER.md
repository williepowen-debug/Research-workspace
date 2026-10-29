# Agent Launcher

Double-click **Agent Launcher.cmd** on the Windows desktop for the graphical
app, or run `agents-gui` from WSL. Search by name or topic, select **Claude Opus**,
**Claude Fable**, **Codex Astra**, or **Codex Sol**, then start a new conversation
or resume. PROME defaults to Fable; CATO defaults to Astra and offers Sol as well.
Other agents retain their Sol default; choose Claude Opus when using Claude. An optional task applies to a new conversation; clear
the task box to enable Resume. Resume opens the selected runtime's saved-session
picker in its terminal. The app stays open for more launches; closing it leaves
the agent windows running.

Choose a **category** on the left, or **All agents**. Search covers all agents; clearing it restores the current
category. Click an agent's name for details and use its checkbox to include it
in a batch. Checked agents stay selected across categories and searches; the
selection count includes hidden agents. **Clear selection** removes all checks.

With multiple agents checked, **Apply edits to all selected agents** defaults on.
Changing the model, typing instructions, or applying a preset updates every checked
agent, including those hidden by search. Model changes preserve each agent's
instructions; instruction changes preserve their models. Mixed settings are labelled
until you replace them. CATO supports Codex only, so a selection containing CATO
offers Astra and Sol for shared model edits.

For an individual override, click its name on **Selected & groups**, choose it in
the **Instructions** agent dropdown, or uncheck **Apply edits to all selected agents**.
The other agents keep their settings. Recheck the option to edit the group again.
Changing selection membership or loading a group restores the shared-edit default
without copying or replacing existing settings.

To save a group, check its agents, choose their runtimes, type a name in
**Saved groups**, and click **Save selected**. Choose that name and click
**Load** next time. Loading restores the checked agents and their runtimes;
it starts nothing. Saving an existing name or deleting a group asks first.
Groups store agent names and runtimes. Task text remains in the current app
window, and loading a group preserves those current task edits.

The **Instructions preset** dropdown offers **Orient and report status**, **Continue
approved work**, **Prepare handoff**, and **CATCH-UP**. **Apply** uses the current editing scope:
all selected agents by default, or the individual agent when overriding.
**Manage...** also offers an explicit apply-to-all-selected action.
The preset fills the task box so you can edit it before launch. Replacing
existing task text asks first. These prompts retain existing assignment and
approval conditions; choosing a preset starts nothing.

**CATCH-UP** asks the desk to boot, update its files with new data within approved
workstreams, drain its inbox, complete authorized owed work, and close out and
report. It preserves approval conditions and returns new or unclear directions
to Will. It is an explicit editable preset; ordinary startup and model defaults
are unchanged.

**Due work:** list badges show overdue, due-today and undated open docket rows.
Choose **Due today / overdue** to filter the list (unknown evidence and undated
work stay visible), or **Due work** in the evidence dropdown to color rows by
due status. Details retain the full description, owner, COVERED annotation and
notes. Counts follow the export's first owner token; secondary consumers and
informed desks are not counted as owners. Will-owned and unmatched-owner rows
are listed separately in PROME's details, without counting them as PROME work.
This uses PROME's `spawn_list.open` v1 export, in Eastern time: **DOCKET only;
GATES is not included**. Owed is not the same as should launch. Missing or failed
evidence says **Due unavailable**, never zero owed.

The existing batch preview also shows dated unresolved PROME touches when found,
including earlier dates. This is a snapshot of `ORCH_INFLIGHT.md`, not proof that
a desk is still running; no listed touch does not establish that it is idle.
The line is advisory and adds no confirmation dialog or live-session inventory.

Saved groups persist for this Windows account at
`%LOCALAPPDATA%\ResearchAgentLauncher\groups.json`; they are local preferences
and do not sync through Git. The previous valid version is retained as
`groups.json.previous` when saving over an existing file. If another app window
saved changes first, use **Load** to refresh before saving again. An unreadable
preferences file is preserved and reported; the normal launcher still works.

For multiple agents, choose shared settings, make any individual overrides,
then click **Review & launch**. The preview lists every checked agent,
runtime, and task; **Cancel** starts nothing. **Launch selected** starts new
conversations in separate windows. Startup requests are handled one at a time,
while the opened conversations run together. A failure is shown in the results
and does not prevent the remaining agents from starting. Successful agents are
unchecked; unsuccessful or cancelled agents stay checked, with no automatic
retry. Runtime/task choices last while this app window is open.

**New conversation** and **Resume conversation...** act only on the highlighted
agent and are enabled in individual editing mode. Batch launching starts new conversations;
resume continues through the individual saved-session picker. **Stop remaining**
cancels requests that have not started. The current request may finish. Closing
the launcher cancels queued requests; it never closes opened agent
terminals. Reopen the launcher to load an updated interface.

The app uses native Windows Forms with no extra UI package installation. It
requires Windows PowerShell, WSL, and Windows Terminal. Missing setup is shown
in the list/details and checked again on each launch. Hover over a long status
message to read it in full. A startup acknowledgement confirms only the CLI
process; login and completed agent boot still belong to the agent window.

For the original terminal menu, run `agents` in WSL. Choose an agent, runtime,
and **new** or **resume**.
The selected agent opens in a **separate Windows Terminal window**, titled with
its name and model. The launcher explicitly selects the current WSL distribution
profile (Ubuntu on Will's machine) and runs the CLI inside that distribution,
with the configured Linux account and agent folder. The menu stays open for the next selection. Q closes the
launcher menu without stopping the agent windows. No session starts until you
choose an action. Windows Terminal and WSL are required for the default mode.

The menu uses bold headings, subtle cyan option numbers, muted hints, and
word wrapping sized to the terminal. Runtime and new/resume choices have their
own clear panels. It inherits your terminal's theme without changing settings.
Use `NO_COLOR=1 agents` for plain text; redirected output and basic terminals
automatically omit color codes. Restart an already-open launcher to load updates.

```bash
agents                         # persistent menu; separate agent windows
agents carl                    # choose new/resume; open a new window on Sol
agents carl --opus              # CARL on Claude Opus, choose new or resume
agents prome --fable            # PROME on Claude Fable
agents carl --astra --new       # CARL on Codex Astra
agents stue --sol --new         # start STUE on Sol
agents polly --resume           # choose a saved POLLY Codex conversation
agents cato --new               # existing CATO Astra launcher
agents carl --same-window       # use this terminal instead
agents --same-window            # menu; run here and return after the agent exits
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

Named commands such as `agents carl --new` return after the new window
acknowledges its CLI process. This confirms process startup, not login or a
completed agent boot. If window startup fails or is not confirmed, the launcher
reports it and never retries automatically; inspect the named window first.
Without Windows Terminal, use `--same-window`; there is no silent fallback.

## Activity dates and highlighting

The Agents tab shows the last confirmed **launch here** and the last **saved work**
commit for the selected agent. Choose which source drives the list highlighting:
amber at seven elapsed days, orange at fourteen. Missing or unavailable history
stays neutral; a future timestamp says **Clock ahead**. These colors are browsing
hints, not a schedule or recommendation to launch an agent.

Launch history is machine-local and only covers this launcher. Manual starts and
PROME launches may be absent. Failed/cancelled attempts do not update the last
confirmed launch. Activity keeps the latest 100 attempts plus each agent's latest
confirmed launch; **Reload launch history** picks up other launcher windows' writes.
Older Claude history says **model unrecorded** because it did not capture the model.

Saved work means the latest local Git commit touching the agent folder, excluding
inbox/outbox and configured nested agent folders. It can include another owner's
changes and does not prove the agent ran or completed research. The details include
a date, commit subject/hash, and snapshot time. On **Activity**, **Refresh Git / due**
reloads local Git, docket and unresolved-touch evidence in the background while
preserving checked selections, search, category, models and instructions. If the
highlighted desk stops matching a due-work filter, the list highlights its first
remaining result; check the displayed name before using an individual launch.
Launch buttons
wait for refresh to finish; editing stays available. Failed refreshes are visible
and retain the previous dated snapshot. Configuration changes still require reopening.
Nothing fetches from the network or scans running sessions. The age legend names
the selected evidence source, and the instruction summary has multiple scrollable lines.

Close older launcher windows and reopen after this update so all windows use the
new model choices and history format. Agent terminal sessions can remain open.

## Defaults and scope

- Codex defaults to **gpt-6.1-sol** with full access and approval prompts disabled.
- Claude uses `--dangerously-skip-permissions` and an explicit `--model opus`
  or `--model fable` for both new and resumed conversations. The selection
  overrides older configured Claude model flags, including CYPHER's.
  Legacy `--claude` and saved-group Claude entries resolve to Fable for PROME
  and Opus for other agents. Existing saved groups with explicit Sol keep Sol.
- Codex choices explicitly request `gpt-6.1-sol` or `gpt-6-astra`.
- CATO offers Astra and Sol with **workspace-write / on-request** for both.
  Claude remains unavailable for CATO; selecting Sol does not broaden permissions.
- WALTER's Telegram connection was retired by Will on October 27, 2026.
  New and resumed sessions launch without Telegram channel flags.
- CARL's specialists use their nested folders. Project folders and startup files
  are checked; the launcher never creates missing desks or substitutes another.
- The configuration contains the command sheet's 50 distinct targets plus CATO.
  VIRGIL and ZION are retained references whose folders were absent on the
  installation machine. It is a personal menu, not a new fleet roster, schedule,
  or grant of launch authority. Existing restrictions, including CREED's manual
  permission condition, remain with their owners.

Each agent window holds a local file lock while its interactive child CLI runs.
The menu process does not own that lock and can close independently.
Two launcher windows using the same cache directory cannot simultaneously open
the same resolved folder, even with different runtimes or names. Setting
`XDG_CACHE_HOME` differently between launch environments creates separate locks.
This does **not** detect manually opened
sessions, a Codex task that outlives its terminal, other launchers, or sessions
on another machine. Killing the launcher parent can release the lock while its
child remains alive. A released lock never proves a desk is idle or complete.
Old lock files do not block: the operating system lock, not stored PID text,
determines whether another launcher window holds the folder.

No Git pull, background wake, direct message, global process scan, or automatic
restart occurs. A failed command is reported with its exit code, never retried.

## Files and installation

- `scripts/agents.py`: menu, command construction, and local terminal supervision.
- `scripts/agents_gui.py` and `scripts/agents_gui.ps1`: desktop interface and
  single-use launch requests, using the same validated plans and window backend.
- `scripts/agents.json`: editable launch targets/settings; read on each invocation.
- `scripts/install_agents.py`: creates the local shortcuts; starts no agents.
- `~/.local/bin/agents`: machine-local shortcut, outside Git.
- `~/.local/bin/agents-gui`: machine-local desktop-app command, outside Git.
- `~/.cache/research-agent-launcher/`: local lock files (or under `XDG_CACHE_HOME`).
- `windows/` under that cache: single-use window requests and startup/exit
  receipts. Requests include the command/task text, are private to the user,
  and are not synced through Git. A claimed request is never replayed.
- `gui/` under that cache: private local app snapshots, task requests, and
  results. Configuration is reloaded before each launch; reopen the app to
  refresh its displayed list. These files are not a record of fleet activity.

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
  --gui --desktop /mnt/c/Users/willi/OneDrive/Desktop --distro Ubuntu
```

Add `--dry-run` to inspect exact files before installation. With `--gui`, the
installer upgrades its own exact original desktop menu shortcut, preserving
`Agent Launcher.cmd.terminal-menu.bak` first. Other differing files and symlinks
are refused. Omit `--gui` for a fresh terminal-only installation. Identical installations
are reusable. No shell/profile files are edited. The desktop launcher uses the
specified WSL distribution and installer user's Linux account.

Direct fallback if the shortcut is unavailable:

```bash
python3 ~/Research-workspace/scripts/agents.py
python3 ~/Research-workspace/scripts/agents_gui.py
```

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s scripts/tests -p test_agents_launcher.py -v
```

Tests use isolated projects and fake CLI executables; they never call a model.
For an opt-in native Windows control/screenshot check, run
`python3 scripts/agents_gui.py --smoke-test`. For a full GUI batch-preview and launch test
through Windows Terminal using only fake CLIs, run
`python3 scripts/tests/probe_agents_gui.py`. Both open and close test windows;
they leave their evidence under the printed local cache or temporary directory.
The batch probe checks background refresh with prepared settings preserved,
cancellation, mixed runtimes and separate tasks, two
concurrent fake CLI processes, and continuation after a missing-folder failure.
Dry-run checks paths, required startup files, and executable presence, not account
access, model availability, full runtime behavior, or whether another owner is
running. A real Windows Terminal-to-WSL test passed with a harmless fake CLI,
including an interactive terminal and exact special-character path/task transfer.
The first test exposed WSL shell parsing; the final route uses `wsl.exe --exec`
to bypass that shell. Live model/account startup remains the next observation.

Windows Terminal behavior uses Microsoft's documented
[`-w new`, titles, and `--suppressApplicationTitle`](https://learn.microsoft.com/en-us/windows/terminal/command-line-arguments).
