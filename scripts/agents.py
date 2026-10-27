#!/usr/bin/env python3
"""Will's manual agent launcher. Python standard library only; never auto-launches.

Configuration: scripts/agents.json, read each invocation. The local flock covers
launcher-owned terminal processes only, NOT manually opened or daemon sessions.
No process-name/cwd/quiet-Git heuristic is treated as proof an owner is absent.
"""
from __future__ import annotations

import argparse
import base64
from contextlib import contextmanager
from dataclasses import dataclass, asdict
import fcntl
import getpass
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import signal
import subprocess
import sys
import textwrap
import time
import uuid

ROOT = Path(__file__).resolve().parents[1]
CONFIG = Path(__file__).with_name('agents.json')


class LaunchError(Exception):
    """Actionable user error; no agent should start after this error."""


class Cancelled(Exception):
    """Leaving the menu is a normal exit, including from the desktop shortcut."""


@dataclass(frozen=True)
class Plan:
    name: str
    cwd: Path
    runtime: str
    action: str
    argv: list[str]
    required: list[Path]


def load_config(path: Path) -> list[dict]:
    try:
        data = json.loads(path.read_text())
    except (OSError, ValueError) as exc:
        raise LaunchError(f'Cannot read configuration {path}: {exc}') from exc
    if not isinstance(data, dict) or data.get('version') != 1:
        raise LaunchError(f'{path}: expected configuration version 1.')
    entries = data.get('agents')
    if not isinstance(entries, list) or not entries:
        raise LaunchError(f'{path}: agents must be a nonempty list.')
    names = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise LaunchError(f'{path}: each agent must be an object.')
        for key in ('name', 'path', 'purpose', 'group', 'kind', 'default_runtime'):
            value = entry.get(key)
            if not isinstance(value, str) or not value.strip() or any(ord(c) < 32 for c in value):
                raise LaunchError(f'{path}: invalid or missing {key}.')
        name = entry['name']
        if not re.fullmatch(r'[A-Z][A-Z0-9_-]*', name) or name in names:
            raise LaunchError(f'{path}: invalid or duplicate agent name {name!r}.')
        names.add(name)
        if entry['kind'] not in ('fleet', 'cato', 'project'):
            raise LaunchError(f'{name}: unknown startup kind.')
        if entry['default_runtime'] not in ('sol', 'astra', 'claude'):
            raise LaunchError(f'{name}: unknown default runtime.')
        for key in ('claude_args', 'required'):
            values = entry.get(key, [])
            if not isinstance(values, list) or any(not isinstance(v, str) or not v or '\x00' in v for v in values):
                raise LaunchError(f'{name}: {key} must be a list of nonempty strings.')
        if entry['kind'] == 'project' and not isinstance(entry.get('prompt'), str):
            raise LaunchError(f'{name}: project startup prompt is missing.')
        if entry['kind'] == 'cato' and entry['default_runtime'] != 'astra':
            raise LaunchError('CATO must retain its Astra default.')
    return entries


def resolve_folder(value: str, root: Path = ROOT, home: Path | None = None) -> Path:
    home = home or Path.home()
    if value.startswith('~/'):
        return (home / value[2:]).resolve()
    if value.startswith('~') or Path(value).is_absolute():
        raise LaunchError('Configured paths must be repository-relative or start with ~/ .')
    result = (root / value).resolve()
    if not result.is_relative_to(root.resolve()):
        raise LaunchError(f'Configured repository path escapes the checkout: {value}')
    return result


def build_plan(entry: dict, runtime: str | None, action: str,
               task: str | None = None, root: Path = ROOT,
               home: Path | None = None) -> Plan:
    runtime = runtime or entry['default_runtime']
    if action not in ('new', 'resume'):
        raise LaunchError('Choose new or resume.')
    if action == 'resume' and task is not None:
        raise LaunchError('--task is for new sessions. Resume first, then type the task.')
    if task is not None and '\x00' in task:
        raise LaunchError('Task text contains a null character.')
    cwd = resolve_folder(entry['path'], root, home)
    name, kind = entry['name'], entry['kind']
    if runtime not in ('sol', 'astra', 'claude'):
        raise LaunchError(f'Unknown runtime: {runtime}')
    if kind == 'cato' and runtime != 'astra':
        raise LaunchError('CATO uses its existing Astra launcher. Omit --sol/--claude.')
    required = [cwd / f for f in entry.get('required', [])]
    if kind in ('fleet', 'cato'):
        required += [root / f for f in ('CLAUDE.md', 'AGENTS.md', 'USER.md')]
    if kind == 'fleet':
        required.append(cwd / 'CLAUDE.md')
    if kind == 'cato':
        required += [cwd / f for f in ('AGENTS.md', 'CHARTER.md', 'CONTINUITY.md', 'launch.sh')]
        if action == 'new':
            argv = ['bash', str(cwd / 'launch.sh')]
            if task is not None:
                argv += ['--', task]
        else:
            argv = ['codex', 'resume', '--model', 'gpt-6-astra', '--sandbox',
                    'workspace-write', '--ask-for-approval', 'on-request',
                    '--add-dir', str(root)]
        return Plan(name, cwd, runtime, action, argv, required)
    if kind == 'project':
        prompt = entry['prompt']
    else:
        prompt = (f'You are {name}. Resolve the Git root. Explicitly read root CLAUDE.md, '
                  'AGENTS.md, and USER.md, then your local CLAUDE.md and any AGENTS.md. '
                  'Follow your startup protocol and recover current work and approvals. '
                  'Report missing dependencies; do not assume Claude-specific tools are available.')
    if task is not None:
        prompt += '\n\nWill\'s task: ' + task
    if runtime == 'claude':
        argv = ['claude', '--dangerously-skip-permissions']
        if action == 'resume':
            argv.append('--resume')
        # Existing runtime-specific model/channel settings travel with both modes.
        argv += entry.get('claude_args', [])
        if action == 'new':
            argv += ['--', prompt]
    else:
        argv = ['codex'] + (['resume'] if action == 'resume' else [])
        argv += ['--model', 'gpt-6.1-sol' if runtime == 'sol' else 'gpt-6-astra',
                 '--dangerously-bypass-approvals-and-sandbox']
        if action == 'new':
            argv += ['--', prompt]
    return Plan(name, cwd, runtime, action, argv, required)


def validate_plan(plan: Plan) -> None:
    if not plan.cwd.is_dir():
        raise LaunchError(f'{plan.name}: folder not found: {plan.cwd}. Install the project on this machine first.')
    for path in plan.required:
        try:
            with path.open('rb') as stream:
                stream.read(1)
        except OSError as exc:
            raise LaunchError(f'{plan.name}: required startup file is unreadable: {path}: {exc}') from exc
    executable = 'codex' if plan.runtime in ('sol', 'astra') else 'claude'
    if shutil.which(executable) is None:
        raise LaunchError(f'{executable} is not on PATH. Install or enable it before launching {plan.name}.')
    if shutil.which(plan.argv[0]) is None:
        raise LaunchError(f'{plan.argv[0]} is not on PATH.')


def cache_folder() -> Path:
    base = Path(os.environ.get('XDG_CACHE_HOME', str(Path.home() / '.cache')))
    if not base.is_absolute():
        raise LaunchError('XDG_CACHE_HOME must be an absolute path.')
    return base / 'research-agent-launcher'


@contextmanager
def session_lock(plan: Plan, state_dir: Path | None = None):
    """A local terminal lock, never a declaration of global desk ownership."""
    state_dir = state_dir or cache_folder()
    state_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
    key = hashlib.sha256(str(plan.cwd.resolve()).encode()).hexdigest()
    fd = os.open(state_dir / (key + '.lock'), os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise LaunchError(f'A launcher window already owns {plan.cwd}. Return to that terminal; '
                              'do not start another copy.') from exc
        os.ftruncate(fd, 0)
        os.write(fd, json.dumps({'pid': os.getpid(), 'agent': plan.name,
                                'runtime': plan.runtime, 'folder': str(plan.cwd)}).encode())
        yield
    finally:
        os.close(fd)


def execute(plan: Plan, *, state_dir: Path | None = None, on_started=None) -> int:
    validate_plan(plan)
    with session_lock(plan, state_dir):
        print(f'{plan.name} | {plan.runtime.upper()} | {plan.action} session\nFolder: {plan.cwd}', flush=True)
        print('Sessions opened outside this launcher are not checked.', flush=True)
        # Inherit the terminal; do not pipe model output or turn this into a daemon.
        with subprocess.Popen(plan.argv, cwd=plan.cwd) as child:
            # Ctrl+C belongs to the interactive CLI, not this waiting parent.
            old_int = signal.signal(signal.SIGINT, lambda *_: None)
            old_term = signal.signal(signal.SIGTERM, lambda *_: child.terminate())
            try:
                if on_started is not None:
                    on_started(child.pid)
                code = child.wait()
            finally:
                signal.signal(signal.SIGINT, old_int)
                signal.signal(signal.SIGTERM, old_term)
        return code if code >= 0 else 128 - code


def window_title(plan: Plan) -> str:
    return plan.name + ' - ' + {'sol': 'Codex Sol', 'astra': 'Codex Astra', 'claude': 'Claude'}[plan.runtime]


def window_command(plan: Plan, request: Path) -> list[str]:
    """Windows argv are data, never a CMD program containing the user's task.

    PowerShell starts the Windows app alias on the Windows side. A hex-encoded
    Python bootstrap keeps paths/semicolons out of Terminal's command parser.
    Only paths cross the command line; potentially long task text stays in JSON.
    """
    powershell = shutil.which('powershell.exe')
    if not powershell or not shutil.which('wt.exe'):
        raise LaunchError('Windows Terminal/PowerShell is unavailable. Use --same-window on this machine.')
    distro = os.environ.get('WSL_DISTRO_NAME')
    if not distro:
        raise LaunchError('The WSL distribution is unknown. Use --same-window.')
    script = str(Path(__file__).resolve())
    bootstrap = (f'import runpy,sys;sys.argv=[{script!r},"--window-request",{str(request)!r}];'
                 f'runpy.run_path({script!r},run_name="__main__")')
    win_args = ['-w', 'new', 'new-tab', '--title', window_title(plan), '--suppressApplicationTitle',
                'wsl.exe', '-d', distro, '-u', getpass.getuser(), '--exec', sys.executable,
                '-c', "exec(bytes.fromhex('" + bootstrap.encode().hex() + "'))"]
    # list2cmdline handles Windows argv quoting; single-quote doubling handles
    # the outer PowerShell literal. No interpolated PowerShell expressions.
    argument_line = subprocess.list2cmdline(win_args).replace("'", "''")
    ps = ("$ErrorActionPreference='Stop';try {Start-Process -FilePath 'wt.exe' "
          f"-ArgumentList '{argument_line}' -ErrorAction Stop | Out-Null;exit 0"
          "} catch {[Console]::Error.WriteLine($_.Exception.Message);exit 1}")
    encoded = base64.b64encode(ps.encode('utf-16le')).decode('ascii')
    return [powershell, '-NoLogo', '-NoProfile', '-NonInteractive', '-EncodedCommand', encoded]


def write_receipt(path: Path, value: dict) -> None:
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value))
    os.replace(temporary, path)


def run_window_request(request: Path) -> int:
    """One requested window owns the child process/lock, never the menu."""
    receipt = request.with_name('receipt.json')
    try:
        # A request is single-use even after its CLI exits. Never replay a wake.
        with request.with_name('claimed').open('x'):
            pass
        data = json.loads(request.read_text())
        p = data['plan']
        plan = Plan(p['name'], Path(p['cwd']), p['runtime'], p['action'], p['argv'],
                    [Path(f) for f in p['required']])
        # Restore command lookup, not the caller's entire environment/credentials.
        os.environ['PATH'] = data['path']
        code = execute(plan, state_dir=Path(data['state_dir']),
                       on_started=lambda pid: write_receipt(receipt, {'state': 'started', 'pid': pid}))
        write_receipt(receipt, {'state': 'exited', 'exit_code': code})
    except FileExistsError:
        print('This window request was already claimed; no second agent started.', file=sys.stderr)
        return 2
    except (LaunchError, OSError, ValueError, KeyError, TypeError) as exc:
        write_receipt(receipt, {'state': 'error', 'message': str(exc)})
        print(f'Launcher: {exc}', file=sys.stderr)
        code = 2
    if code and sys.stdin.isatty():
        print(f'Agent window exited with code {code}.')
        try:
            input('Press Enter to close this window. ')
        except (EOFError, KeyboardInterrupt):
            pass
    return code


def open_window(plan: Plan, timeout: float = 10) -> int:
    validate_plan(plan)
    state_dir = cache_folder()
    # Refuse known overlap before opening an unnecessary window. This is only
    # a precheck; the new-window worker acquires the authoritative local lock.
    with session_lock(plan, state_dir):
        pass
    request = state_dir / 'windows' / uuid.uuid4().hex / 'request.json'
    command = window_command(plan, request)  # validate transport before persisting a request
    request.parent.mkdir(parents=True, mode=0o700)
    p = asdict(plan)
    p['cwd'] = str(plan.cwd)
    p['required'] = [str(f) for f in plan.required]
    with request.open('x') as stream:
        os.chmod(request, 0o600)
        json.dump({'plan': p, 'path': os.environ.get('PATH', ''), 'state_dir': str(state_dir)}, stream)
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=15)
    except subprocess.TimeoutExpired as exc:
        raise LaunchError(f'Window request timed out; inspect {window_title(plan)} before retrying. Request: {request.parent}') from exc
    if result.returncode:
        raise LaunchError(f'Window request failed ({result.returncode}): {result.stderr.strip() or result.stdout.strip()}')
    receipt = request.with_name('receipt.json')
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if receipt.exists():
            status = json.loads(receipt.read_text())
            if status.get('state') == 'error':
                raise LaunchError(f'Agent window could not start: {status["message"]}')
            if status.get('state') == 'exited' and status.get('exit_code'):
                raise LaunchError(f'Agent window exited with code {status["exit_code"]}; inspect that window.')
            if status.get('state') in ('started', 'exited'):
                print(f'Opened {window_title(plan)} in a separate window.\n'
                      'CLI process acknowledged; login and agent boot are not verified.')
                return 0
        time.sleep(.05)
    raise LaunchError(f'Window requested but startup is not confirmed. Inspect {window_title(plan)} before retrying. '
                      f'Request: {request.parent}')


def paint(text: str, tone: str = 'accent') -> str:
    """Use the terminal's own palette; keep redirected/plain output escape-free."""
    if not sys.stdout.isatty() or os.environ.get('TERM') == 'dumb' or 'NO_COLOR' in os.environ:
        return text
    codes = {'accent': '36', 'strong': '1', 'muted': '2', 'warning': '33'}
    return f'\033[{codes[tone]}m{text}\033[0m'


def menu_width() -> int:
    return max(20, min(86, shutil.get_terminal_size((80, 24)).columns) - 4)


def menu_text(text: str, tone: str | None = None, indent: int = 2) -> None:
    prefix = ' ' * indent
    wrapped = textwrap.fill(text, width=menu_width() + 2, initial_indent=prefix,
                            subsequent_indent=prefix, break_long_words=False, break_on_hyphens=False)
    print(paint(wrapped, tone) if tone else wrapped)


def menu_header(title: str, subtitle: str) -> None:
    print()
    menu_text(title, 'strong')
    menu_text(subtitle, 'muted')
    print('  ' + paint('-' * menu_width(), 'muted'))


def menu_choice(key: str, title: str, detail: str = '') -> None:
    prefix = f'  {key:>2}  '
    lines = textwrap.wrap(title, width=max(14, menu_width() - 4),
                          break_long_words=False, break_on_hyphens=False) or ['']
    print(paint(prefix, 'accent') + lines[0])
    for line in lines[1:]:
        print(' ' * len(prefix) + line)
    if detail:
        menu_text(detail, 'muted', indent=6)


def runtime_label(runtime: str) -> str:
    return {'sol': 'Codex Sol', 'astra': 'Codex Astra', 'claude': 'Claude'}[runtime]


def show_agents(entries: list[dict], root: Path = ROOT) -> None:
    groups = list(dict.fromkeys(e['group'] for e in entries))
    title = groups[0] if len(groups) == 1 else 'All agents'
    menu_header(title, 'Choose a number or type an agent name.')
    group = None
    for index, entry in enumerate(entries, 1):
        if entry['group'] != group:
            group = entry['group']
            if len(groups) > 1:
                print()
                menu_text(group, 'strong')
        missing = '' if resolve_folder(entry['path'], root).is_dir() else '  [folder missing]'
        menu_choice(str(index), entry['name'] + missing, entry['purpose'])
    print()
    menu_text('B  Back to groups    Q  Quit', 'muted')


def ask(prompt: str) -> str:
    try:
        answer = input('\n  ' + paint(prompt, 'accent')).strip()
    except (EOFError, KeyboardInterrupt):
        raise Cancelled from None
    if answer.lower() in ('q', 'quit', 'exit'):
        raise Cancelled
    return answer


def choose_agent(entries: list[dict], same_window: bool = False) -> dict:
    groups = list(dict.fromkeys(entry['group'] for entry in entries))
    shown = None
    redraw = True
    while True:
        if redraw:
            if shown is None:
                menu_header('Agent Launcher', 'Choose an agent by name, or browse a group.')
                for index, group in enumerate(groups, 1):
                    menu_choice(str(index), group)
                print()
                menu_text('A  All agents    Q  Quit', 'muted')
                menu_text('Agents run in this window.' if same_window else 'Each agent opens in its own window.', 'muted')
            else:
                show_agents(shown)
            redraw = False
        answer = ask('Agent or group > ' if shown is None else 'Agent > ').upper()
        for entry in entries:
            if entry['name'] == answer:
                return entry
        if shown is not None and answer.isdigit() and 1 <= int(answer) <= len(shown):
            return shown[int(answer) - 1]
        if shown is not None and answer == 'B':
            shown, redraw = None, True
            continue
        if shown is None:
            if answer == 'A':
                shown = entries
            elif answer.isdigit() and 1 <= int(answer) <= len(groups):
                shown = [e for e in entries if e['group'] == groups[int(answer) - 1]]
            if shown is not None:
                redraw = True
                continue
        menu_text('Choose a listed number or agent name, or Q to quit.', 'warning')


def choose_runtime(entry: dict) -> str:
    if entry['kind'] == 'cato':
        return 'astra'
    default = entry['default_runtime']
    menu_header(entry['name'] + ' / Runtime', entry['purpose'])
    menu_choice('S', 'Codex Sol', 'Default' if default == 'sol' else '')
    menu_choice('C', 'Claude', 'Default' if default == 'claude' else '')
    print()
    menu_text(f'Enter  Use {runtime_label(default)}    Q  Quit', 'muted')
    while True:
        value = ask('Runtime > ').lower()
        if not value: return default
        if value in ('c', 'claude'): return 'claude'
        if value in ('s', 'sol'): return 'sol'
        menu_text('Choose C, S, or Enter.', 'warning')


def choose_action(entry: dict, runtime: str, same_window: bool = False) -> str:
    destination = 'This terminal window' if same_window else 'New, separate terminal window'
    menu_header(entry['name'] + ' / ' + runtime_label(runtime), destination)
    menu_choice('1', 'Start a new session', 'Load startup instructions and current duties.')
    print()
    menu_choice('2', 'Resume a saved session', 'Choose a conversation from the session picker.')
    print()
    menu_text('Already running? Return to its existing window.', 'muted')
    menu_text('Q  Quit without launching', 'muted')
    while True:
        value = ask('Action > ').lower()
        if value in ('1', 'new'): return 'new'
        if value in ('2', 'resume'): return 'resume'
        menu_text('Choose 1, 2, or Q.', 'warning')


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Launch a named agent with its saved settings. No agents start in --list/--dry-run.')
    parser.add_argument('agent', nargs='?', help='Agent name, e.g. CARL (case-insensitive).')
    runtimes = parser.add_mutually_exclusive_group()
    runtimes.add_argument('--sol', action='store_const', const='sol', dest='runtime')
    runtimes.add_argument('--claude', action='store_const', const='claude', dest='runtime')
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument('--new', action='store_const', const='new', dest='action')
    actions.add_argument('--resume', action='store_const', const='resume', dest='action')
    windows = parser.add_mutually_exclusive_group()
    windows.add_argument('--same-window', action='store_true', help='Run here instead of opening a new window.')
    windows.add_argument('--new-window', action='store_true', help='Open a separate Windows Terminal window (default).')
    parser.add_argument('--task', help='Task to append after startup instructions (new sessions only).')
    parser.add_argument('--list', action='store_true', help='List configured agents without launching.')
    parser.add_argument('--dry-run', action='store_true', help='Validate and print the command without running it; defaults to new.')
    parser.add_argument('--config', type=Path, default=CONFIG, help='Use another launch configuration.')
    parser.add_argument('--window-request', type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if args.window_request:
        return run_window_request(args.window_request)
    try:
        entries = load_config(args.config)
        if args.list:
            show_agents(entries)
            return 0
        menu = not args.agent and sys.stdin.isatty() and not args.dry_run
        while True:
            try:
                if args.agent:
                    entry = next((e for e in entries if e['name'] == args.agent.upper()), None)
                    if entry is None:
                        raise LaunchError(f'Unknown agent {args.agent!r}. Use agents --list.')
                else:
                    if not sys.stdin.isatty():
                        raise LaunchError('Open an interactive terminal for the menu, or give an agent name and --new/--resume.')
                    entry = choose_agent(entries, args.same_window)
                runtime = args.runtime
                if runtime is None and not args.agent:
                    runtime = choose_runtime(entry)
                action = args.action
                if action is None:
                    if args.dry_run:
                        action = 'new'
                    elif sys.stdin.isatty():
                        action = choose_action(entry, runtime or entry['default_runtime'], args.same_window)
                    else:
                        raise LaunchError('Specify --new or --resume outside an interactive terminal.')
                plan = build_plan(entry, runtime, action, args.task)
                validate_plan(plan)
                if args.dry_run:
                    print(f'DRY RUN — {plan.name}, {plan.runtime}, {plan.action}; no session started.\n'
                          f'Destination: {"this window" if args.same_window else "new Windows Terminal window"}\n'
                          f'cd {shlex.quote(str(plan.cwd))} && {shlex.join(plan.argv)}\n'
                          'Checked: folder, required startup files, executable on PATH. '
                          'Not checked: window transport, login, model access, running owners, or live boot.')
                    return 0
                code = execute(plan) if args.same_window else open_window(plan)
                if not menu:
                    return code
                print('\nReady to open another agent window.\n')
            except (LaunchError, OSError) as exc:
                if not menu:
                    raise
                print(f'Launcher: {exc}\n', file=sys.stderr)
    except Cancelled:
        print('\nLauncher closed. Existing agent windows keep running.')
        return 0
    except (LaunchError, OSError) as exc:
        print(f'Launcher: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
