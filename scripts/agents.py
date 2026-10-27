#!/usr/bin/env python3
"""Will's manual agent launcher. Python standard library only; never auto-launches.

Configuration: scripts/agents.json, read each invocation. The local flock covers
launcher-owned terminal processes only, NOT manually opened or daemon sessions.
No process-name/cwd/quiet-Git heuristic is treated as proof an owner is absent.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from dataclasses import dataclass
import fcntl
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


def execute(plan: Plan) -> int:
    validate_plan(plan)
    with session_lock(plan):
        print(f'{plan.name} | {plan.runtime.upper()} | {plan.action} session\nFolder: {plan.cwd}', flush=True)
        print('Sessions opened outside this launcher are not checked.', flush=True)
        # Inherit the terminal; do not pipe model output or turn this into a daemon.
        with subprocess.Popen(plan.argv, cwd=plan.cwd) as child:
            # Ctrl+C belongs to the interactive CLI, not this waiting parent.
            old_int = signal.signal(signal.SIGINT, lambda *_: None)
            old_term = signal.signal(signal.SIGTERM, lambda *_: child.terminate())
            try:
                code = child.wait()
            finally:
                signal.signal(signal.SIGINT, old_int)
                signal.signal(signal.SIGTERM, old_term)
        return code if code >= 0 else 128 - code


def show_agents(entries: list[dict], root: Path = ROOT) -> None:
    print('AGENT LAUNCHER\n')
    group = None
    for index, entry in enumerate(entries, 1):
        if entry['group'] != group:
            group = entry['group']
            print(group)
        missing = '' if resolve_folder(entry['path'], root).is_dir() else ' [folder missing]'
        print(f'  {index:2}. {entry["name"]:<10} {entry["purpose"]}{missing}')
    print('\nChoose a number or name. Q quits. Defaults: Sol; CATO uses Astra.')


def ask(prompt: str) -> str:
    try:
        answer = input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        raise Cancelled from None
    if answer.lower() in ('q', 'quit', 'exit'):
        raise Cancelled
    return answer


def choose_agent(entries: list[dict]) -> dict:
    groups = list(dict.fromkeys(entry['group'] for entry in entries))
    print('AGENT LAUNCHER\nType an agent name, or choose a group:\n')
    for index, group in enumerate(groups, 1):
        print(f'  {index}. {group}')
    print('\nA = All agents, Q = Quit')
    shown = None
    while True:
        answer = ask('\nAgent or group: ' if shown is None else '\nAgent (B = Back): ').upper()
        for entry in entries:
            if entry['name'] == answer:
                return entry
        if shown is not None and answer.isdigit() and 1 <= int(answer) <= len(shown):
            return shown[int(answer) - 1]
        if shown is not None and answer == 'B':
            return choose_agent(entries)
        if shown is None:
            if answer == 'A':
                shown = entries
            elif answer.isdigit() and 1 <= int(answer) <= len(groups):
                shown = [e for e in entries if e['group'] == groups[int(answer) - 1]]
            if shown is not None:
                show_agents(shown)
                continue
        print('Choose a listed number or agent name, or Q to quit.')


def choose_runtime(entry: dict) -> str:
    if entry['kind'] == 'cato':
        return 'astra'
    default = entry['default_runtime']
    while True:
        value = ask(f'Runtime: [Enter] {default.upper()}, C = Claude, S = Sol: ').lower()
        if not value: return default
        if value in ('c', 'claude'): return 'claude'
        if value in ('s', 'sol'): return 'sol'
        print('Choose C, S, or Enter.')


def choose_action() -> str:
    print('If this agent is already running, return to its existing terminal.')
    while True:
        value = ask('1 = Start new session, 2 = Resume saved session, Q = Quit: ').lower()
        if value in ('1', 'new'): return 'new'
        if value in ('2', 'resume'): return 'resume'
        print('Choose 1, 2, or Q.')


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Launch a named agent with its saved settings. No agents start in --list/--dry-run.')
    parser.add_argument('agent', nargs='?', help='Agent name, e.g. CARL (case-insensitive).')
    runtimes = parser.add_mutually_exclusive_group()
    runtimes.add_argument('--sol', action='store_const', const='sol', dest='runtime')
    runtimes.add_argument('--claude', action='store_const', const='claude', dest='runtime')
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument('--new', action='store_const', const='new', dest='action')
    actions.add_argument('--resume', action='store_const', const='resume', dest='action')
    parser.add_argument('--task', help='Task to append after startup instructions (new sessions only).')
    parser.add_argument('--list', action='store_true', help='List configured agents without launching.')
    parser.add_argument('--dry-run', action='store_true', help='Validate and print the command without running it; defaults to new.')
    parser.add_argument('--config', type=Path, default=CONFIG, help='Use another launch configuration.')
    args = parser.parse_args(argv)
    try:
        entries = load_config(args.config)
        if args.list:
            show_agents(entries)
            return 0
        if args.agent:
            entry = next((e for e in entries if e['name'] == args.agent.upper()), None)
            if entry is None:
                raise LaunchError(f'Unknown agent {args.agent!r}. Use agents --list.')
        else:
            if not sys.stdin.isatty():
                raise LaunchError('Open an interactive terminal for the menu, or give an agent name and --new/--resume.')
            entry = choose_agent(entries)
        runtime = args.runtime
        if runtime is None and not args.agent:
            runtime = choose_runtime(entry)
        action = args.action
        if action is None:
            if args.dry_run:
                action = 'new'
            elif sys.stdin.isatty():
                action = choose_action()
            else:
                raise LaunchError('Specify --new or --resume outside an interactive terminal.')
        plan = build_plan(entry, runtime, action, args.task)
        validate_plan(plan)
        if args.dry_run:
            print(f'DRY RUN — {plan.name}, {plan.runtime}, {plan.action}; no session started.\n'
                  f'cd {shlex.quote(str(plan.cwd))} && {shlex.join(plan.argv)}\n'
                  'Checked: folder, required startup files, executable on PATH. '
                  'Not checked: login, model access, running owners, or live boot.')
            return 0
        return execute(plan)
    except Cancelled:
        print('\nNo agent started.')
        return 0
    except (LaunchError, OSError) as exc:
        print(f'Launcher: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
