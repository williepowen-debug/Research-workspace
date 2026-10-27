#!/usr/bin/env python3
"""Install the personal agents shortcut, optionally a Windows Desktop launcher.

No agent is started. All destination conflicts are checked before any writes.
Run on each machine after syncing the repository; no shell/profile edits.
"""
from __future__ import annotations

import argparse
import getpass
import os
from pathlib import Path
import re
import shlex
import sys

ROOT = Path(__file__).resolve().parents[1]


def shortcut_files(root: Path, home: Path, desktop: Path | None,
                   distro: str | None, user: str) -> list[tuple[Path, str, int]]:
    launcher = root / 'scripts' / 'agents.py'
    if not launcher.is_file():
        raise ValueError(f'Launcher is missing: {launcher}')
    if not (root / 'scripts' / 'agents.json').is_file():
        raise ValueError('Launcher configuration is missing.')
    wrapper = '#!/bin/sh\n# Research-workspace agent launcher shortcut\nexec python3 ' + shlex.quote(str(launcher)) + ' "$@"\n'
    files = [(home / '.local' / 'bin' / 'agents', wrapper, 0o755)]
    if desktop is not None:
        if not desktop.is_dir():
            raise ValueError(f'The Windows Desktop folder does not exist: {desktop}')
        if not distro or not re.fullmatch(r'[A-Za-z0-9_. -]+', distro):
            raise ValueError('Supply the installed WSL distribution with --distro, e.g. Ubuntu.')
        if not re.fullmatch(r'[A-Za-z0-9_.-]+', user):
            raise ValueError('The Linux username cannot be encoded safely in the Windows launcher.')
        if any(c in str(launcher) for c in '\r\n\"\'!%&|<>^'):
            raise ValueError('This repository path cannot be encoded safely in a Windows .cmd launcher.')
        command = f'wsl.exe -d "{distro}" -u "{user}" -- bash -lc "exec python3 \'{launcher}\'"'
        batch = ('@echo off\r\nrem Research-workspace agent launcher shortcut\r\n'
                 'title Agent Launcher\r\n' + command + '\r\n'
                 'if errorlevel 1 (\r\n  echo.\r\n  echo Agent Launcher exited with an error.\r\n  pause\r\n)\r\n')
        files.append((desktop / 'Agent Launcher.cmd', batch, 0o644))
    return files


def preflight(files: list[tuple[Path, str, int]]) -> None:
    for path, text, _ in files:
        if path.is_symlink():
            raise ValueError(f'Refusing to replace an existing symlink: {path}')
        if path.exists() and (not path.is_file() or path.read_bytes() != text.encode()):
            raise ValueError(f'Existing file differs: {path}. Preserve or rename it before installing; nothing overwritten.')


def install(files: list[tuple[Path, str, int]]) -> None:
    preflight(files)
    for path, text, mode in files:
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            # Exclusive creation avoids replacing a file created after preflight.
            fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, mode)
            with os.fdopen(fd, 'wb') as stream:
                stream.write(text.encode())
                stream.flush()
                os.fsync(stream.fileno())
        if path.read_bytes() != text.encode():
            raise ValueError(f'Installed content differs: {path}')
        if mode & 0o111:
            path.chmod(mode)
        print(f'Installed and verified: {path}')


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--desktop', type=Path, help='Existing Windows desktop directory, in WSL form.')
    parser.add_argument('--distro', default=os.environ.get('WSL_DISTRO_NAME'), help='WSL distribution for the desktop shortcut.')
    parser.add_argument('--dry-run', action='store_true', help='Print exact shortcut contents; write nothing.')
    args = parser.parse_args(argv)
    try:
        files = shortcut_files(ROOT, Path.home(), args.desktop, args.distro, getpass.getuser())
        preflight(files)
        if args.dry_run:
            for path, text, _ in files:
                print(f'{path}:\n{text}')
            return 0
        install(files)
        if str(Path.home() / '.local' / 'bin') not in os.environ.get('PATH', '').split(os.pathsep):
            print('The shortcut directory is not on this terminal\'s PATH. Use ~/.local/bin/agents directly or open a new login terminal.')
        print('Run agents to open the menu. No agents were started by installation.')
        return 0
    except (OSError, ValueError) as exc:
        print(f'Installer: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
