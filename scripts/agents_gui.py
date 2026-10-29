#!/usr/bin/env python3
"""Native Windows launcher UI and its single-use WSL launch bridge."""
from __future__ import annotations

import argparse
import base64
import getpass
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import uuid

import agents


def windows_path(path: Path) -> str:
    return subprocess.check_output(['wslpath', '-w', str(path.resolve())], text=True).strip()


def catalogue(config: Path) -> list[dict]:
    rows = []
    for entry in agents.load_config(config):
        error = ''
        try:
            agents.validate_plan(agents.build_plan(entry, None, 'new'))
        except agents.LaunchError as exc:
            error = str(exc)
        rows.append({**entry, 'folder': str(agents.resolve_folder(entry['path'])), 'error': error})
    return rows


def launch_request(request: Path) -> int:
    """Reload config and validate on each click; never accept an arbitrary argv."""
    result = request.with_suffix('.result.json')
    try:
        with request.with_suffix('.claimed').open('x'):
            pass
    except FileExistsError:
        return 2  # Never overwrite the first worker's result or launch twice.
    try:
        data = json.loads(request.read_text(encoding='utf-8-sig'))
        context = json.loads(request.with_name('context.json').read_text())
        os.environ['PATH'] = context['path']
        entries = agents.load_config(Path(context['config']))
        entry = next((e for e in entries if e['name'] == data.get('name')), None)
        if entry is None:
            raise agents.LaunchError('Agent is no longer in the configuration. Reopen the app.')
        task = data.get('task') or None
        if task is not None and not isinstance(task, str):
            raise agents.LaunchError('The task must be text.')
        plan = agents.build_plan(entry, data.get('runtime'), data.get('action'), task)
        agents.open_window(plan)
        agents.write_receipt(result, {'ok': True, 'message': f'{agents.window_title(plan)} opened. Continue in its terminal window.'})
        return 0
    except (agents.LaunchError, OSError, ValueError, KeyError, TypeError) as exc:
        agents.write_receipt(result, {'ok': False, 'message': str(exc)})
        return 2


def start_gui(config: Path, smoke_test: bool = False) -> int:
    ps = shutil.which('powershell.exe')
    distro = os.environ.get('WSL_DISTRO_NAME')
    if not ps or not distro:
        raise agents.LaunchError('The desktop app needs Windows with WSL. Use agents for the terminal menu.')
    rows = catalogue(config)
    directory = agents.cache_folder() / 'gui' / uuid.uuid4().hex
    directory.mkdir(parents=True, mode=0o700)
    context = {'config': str(config.resolve()), 'path': os.environ.get('PATH', '')}
    (directory / 'context.json').write_text(json.dumps(context))
    data = {'agents': rows, 'directory': windows_path(directory), 'linux_directory': str(directory),
            'distro': distro, 'user': getpass.getuser(), 'python': sys.executable,
            'bridge': str(Path(__file__).resolve())}
    snapshot = directory / 'catalogue.json'
    snapshot.write_text(json.dumps(data))
    command = [ps, '-NoLogo', '-NoProfile', '-STA', '-ExecutionPolicy', 'Bypass',
               '-File', windows_path(Path(__file__).with_suffix('.ps1')), '-DataFile', windows_path(snapshot)]
    if smoke_test:
        command += ['-SmokeTest']
        print(f'UI test artifacts: {directory}', flush=True)
    # The desktop shortcut has no interactive input. Do not pass its inherited
    # console/input handle through WSL into the Windows PowerShell GUI host.
    code = subprocess.call(command, stdin=subprocess.DEVNULL)
    if smoke_test and code == 0:
        receipt = directory / 'smoke.json'
        if not receipt.is_file():
            raise agents.LaunchError('The native UI test did not return a result.')
        result = json.loads(receipt.read_text(encoding='utf-8-sig'))
        if not result.get('ok'):
            raise agents.LaunchError(result.get('error', 'The native UI test failed.'))
        print('PASS: ' + result['checks'])
    return code


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=agents.CONFIG)
    parser.add_argument('--launch', type=Path, help=argparse.SUPPRESS)
    parser.add_argument('--smoke-test', action='store_true', help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    try:
        return launch_request(args.launch) if args.launch else start_gui(args.config, args.smoke_test)
    except (agents.LaunchError, OSError, subprocess.SubprocessError) as exc:
        print(f'Agent Launcher: {exc}', file=sys.stderr)
        if not args.launch and not args.smoke_test and shutil.which('powershell.exe'):
            message = str(exc).replace("'", "''")
            script = ("Add-Type -AssemblyName System.Windows.Forms;"
                      f"[void][System.Windows.Forms.MessageBox]::Show('{message}','Agent Launcher')")
            encoded = base64.b64encode(script.encode('utf-16le')).decode('ascii')
            subprocess.call(['powershell.exe', '-NoProfile', '-EncodedCommand', encoded])
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
