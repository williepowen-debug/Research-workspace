# Independent launcher review — October 29, 2026

I've finished the review. Within the scope you set, I found **no material problem**: ordinary inputs didn't make the launcher run a different command or model, and the folder lock blocked every duplicate launch I tried. I didn't run the real Windows PowerShell form. Its UI logic I only read; the Windows hand-off was simulated by fake executables.

**Reviewer:** Claude, model ID `claude-opus-5-5` (as exposed in my environment).

**Files reviewed (current working tree, SHA256):**
- `scripts/agents.py` — `e551a5f8d04aca55c4d8a14cee1b7ebd9485b91d640a1192cbc792590e902470`
- `scripts/agents_gui.py` — `72f8049278694420915c779e20a45d84bcddc502953d666205f2ea7c5ed63fd0`
- `scripts/agents_gui.ps1` — `860889c1ba1cf18f18a1ea1dd6db69531ea94f509c068009252905ac34c07b89`
- Dependencies I read only as far as needed: `scripts/agents.json`, `AGENTS/CATO/launch.sh` (`ef043402…271c`), and `PROME/tools/spawn_list.py` (`b3441080…e6f5`), which I checked is read-only before running it.

## Test setup
Everything ran under `/tmp/lr_review`:
- **Fake programs:** `codex` and `claude` stand-ins that record their arguments and then sleep, so they hold the lock for a while. `wt.exe` does nothing.
- **Fake `powershell.exe`:** it decodes the real encoded command and splits the `wt.exe` arguments the way Windows does. It records any `;` it finds, since Windows Terminal would treat that as a command separator. Then it runs the Linux side for real with a minimal environment.
- **Lock files** went into a separate test folder (`XDG_CACHE_HOME=/tmp/lr_review/cache`).
- I drove the real `agents_gui.py --launch` path and the terminal `agents.py`, using the real config and the real CATO `launch.sh`. No real agent windows opened, and nothing in the repository was changed.

## Results
- **Task text stays one argument.** I sent 8 hostile task strings through 5 agent/model pairs (WALTER/sol, PROME/claude, CATO/astra, CATO/sol, CYPHER/opus) — 40 launches. The strings were `--model gpt-evil`, `; touch PWN;`, `$(touch PWN2)` with backticks and quotes, backslashes before a quote and at the end, CR/LF with `-- --dangerously`, `%PATH% & calc.exe | ^ ! ;`, `--check` and `-`.
  - All 40 started exactly one CLI. The task arrived intact as the final argument after `--`, or after "Will's task: " in the startup prompt.
  - The model was always the configured one (PROME's "claude" became `fable`; CYPHER's old `--model` setting was dropped in favour of the chosen `opus`).
  - No marker files were created, and no `;` ever reached Windows Terminal.
  - CATO's `launch.sh -- --check` treats `--check` as the prompt, not as a flag.
- **Restrictions hold.**
  - CATO with opus, fable or claude was refused.
  - Unknown models, a non-text model value, the action `exec`, resume plus a task, a lowercase agent name, a non-text task and a NUL character were all refused, and no CLI started.
  - An empty model value falls back to the configured default (Astra for CATO). The UI always sends a model, so this doesn't matter in practice.
- **The lock holds in all three cases:**
  - **Agent already running:** while WALTER was running from the GUI, a second GUI launch, a terminal `--same-window --resume` and a terminal new-window `--astra` were all refused. Only one CLI ran.
  - **Six simultaneous GUI requests for HAWK:** one succeeded and one CLI started.
  - **Terminal same-window and GUI launching HAWK at the same moment:** one CLI started, and the GUI reported "not confirmed".

## Lower-impact limitations (not regressions)
1. **The lock folder depends on each process's environment** (`agents.py:193-197`). Reproduced: GUI launches BRENT, then a terminal run with a different `XDG_CACHE_HOME` launches BRENT again → 2 CLIs running. It isn't live today because `XDG_CACHE_HOME` isn't set on this machine, so both paths use `~/.cache`. It would bite if a shell profile ever set it differently from the environment the GUI bridge runs in.
2. **The lock only lives as long as the waiting Python process** (`agents.py:206`, `:227-234`). The lock handle isn't passed to the CLI, so if the parent dies while the CLI keeps running, the lock is released early. Reproduced with a fake CLI that ignores hangup: send a hangup signal to the BOND window's process group → parent exits, CLI survives, and a second BOND launch succeeds (2 CLIs). I haven't checked whether the real Codex or Claude CLIs survive a window close.
3. **Due-work refresh can change which agent is highlighted.** After a refresh, `agents_gui.ps1:935` rebuilds the list, and `:1146-1150` falls back to the first agent if the previous one is no longer listed (for example under the Due filter). The Start buttons then act on the new agent. The name label does update and Start is disabled during the refresh, so the screen and the launch still agree. The risk is a user clicking Start without noticing the switch.
4. **Some touch records are missed** (`agents_gui.py:104-105`). On today's data, "FALCON pre-fetch (…)" doesn't count toward FALCON, so the batch review shows no touch warning for it. This affects the evidence shown, not what gets launched.
5. **Single-agent Start/Resume launches without a review dialog.** That looks deliberate, and what it launches matches the visible name, model and task.

The due-work snapshot ran against real data in 0.14 s (205 rows, read-only). The refresh path never starts a launch, and refresh and launch block each other in the UI. I found no material regression there.

## Disposition
No material finding within this perimeter. This isn't a claim that the launcher is secure overall: I didn't run the native form or test real CLI hangup behaviour, and limitations 1–2 are real but conditional.

I have finished and no helper work remains.
