#!/usr/bin/env python3
"""Install the personal agents shortcut, optionally a Windows Desktop launcher.

No agent is started. All destination conflicts are checked before any writes.
Run on each machine after syncing the repository; no shell/profile edits.
"""
from __future__ import annotations

import argparse
import base64
import getpass
import hashlib
import os
from pathlib import Path
import re
import shlex
import sys
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def gui_arguments(root: Path, distro: str, user: str) -> str:
    return subprocess.list2cmdline(['-d', distro, '-u', user, '--exec', 'bash', '-lc',
                                  'exec python3 ' + shlex.quote(str(root / 'scripts/agents_gui.py'))]).replace("'", "''")


def shortcut_files(root: Path, home: Path, desktop: Path | None,
                   distro: str | None, user: str, gui: bool = False) -> list[tuple[Path, str, int]]:
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
    if gui:
        for suffix in ('.py', '.ps1'):
            if not (root / 'scripts' / ('agents_gui' + suffix)).is_file():
                raise ValueError('Desktop app files are missing. Sync the repository first.')
        gui_script = root / 'scripts/agents_gui.py'
        gui_wrapper = '#!/bin/sh\n# Research-workspace graphical agent launcher\nexec python3 ' + shlex.quote(str(gui_script)) + ' "$@"\n'
        files.append((home / '.local/bin/agents-gui', gui_wrapper, 0o755))
        if desktop is not None:
            # Start WSL hidden; its Windows Forms child is the visible app.
            quoted = gui_arguments(root, distro, user)
            ps = ("$ErrorActionPreference='Stop';Add-Type -AssemblyName System.Windows.Forms;try {"
                  "$s=New-Object Diagnostics.ProcessStartInfo;$s.FileName='wsl.exe';"
                  f"$s.Arguments='{quoted}';$s.UseShellExecute=$false;$s.CreateNoWindow=$true;"
                  "$s.RedirectStandardOutput=$true;$s.RedirectStandardError=$true;"
                  "$p=[Diagnostics.Process]::Start($s);$o=$p.StandardOutput.ReadToEndAsync();"
                  "$e=$p.StandardError.ReadToEndAsync();$p.WaitForExit();"
                  "if($p.ExitCode -ne 0){throw ($e.Result+' '+$o.Result)};exit 0"
                  "} catch {[void][Windows.Forms.MessageBox]::Show($_.Exception.Message,'Agent Launcher');exit 1}")
            encoded = base64.b64encode(ps.encode('utf-16le')).decode('ascii')
            batch = ('@echo off\r\nrem Research-workspace graphical agent launcher\r\n'
                     'powershell.exe -NoLogo -NoProfile -NonInteractive -WindowStyle Hidden -EncodedCommand '
                     + encoded + '\r\nif errorlevel 1 pause\r\n')
            files[1] = (desktop / 'Agent Launcher.cmd', batch, 0o644)
    return files


def known_previous(path: Path, previous: dict | None) -> list[str]:
    value = (previous or {}).get(path, [])
    return [value] if isinstance(value, str) else value


def backup_path(path: Path) -> Path:
    data = path.read_bytes()
    suffix = '.terminal-menu.bak' if b'graphical agent launcher' not in data else '.backup-' + hashlib.sha256(data).hexdigest()[:12]
    return path.with_suffix(path.suffix + suffix)


def preflight(files: list[tuple[Path, str, int]], previous: dict | None = None) -> None:
    for path, text, _ in files:
        if path.is_symlink():
            raise ValueError(f'Refusing to replace an existing symlink: {path}')
        if path.exists() and (not path.is_file() or path.read_bytes() != text.encode()):
            if path.is_file() and path.read_bytes() in [t.encode() for t in known_previous(path, previous)]:
                backup = backup_path(path)
                if backup.is_symlink() or (backup.exists() and (not backup.is_file() or backup.read_bytes() != path.read_bytes())):
                    raise ValueError(f'Backup already differs: {backup}')
                continue
            raise ValueError(f'Existing file differs: {path}. Preserve or rename it before installing; nothing overwritten.')


def install(files: list[tuple[Path, str, int]], previous: dict | None = None) -> None:
    preflight(files, previous)
    for path, text, mode in files:
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists() and path.read_bytes() != text.encode():
            if path.is_symlink() or path.read_bytes() not in [t.encode() for t in known_previous(path, previous)]:
                raise ValueError(f'File changed during installation: {path}')
            backup = backup_path(path)
            if not backup.exists():
                with backup.open('xb') as stream:
                    stream.write(path.read_bytes())
            if backup.is_symlink() or backup.read_bytes() != path.read_bytes():
                raise ValueError(f'Backup verification failed: {backup}')
            temporary = path.with_suffix(path.suffix + '.installing')
            with temporary.open('xb') as stream:
                stream.write(text.encode())
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, path)
            print(f'Previous shortcut preserved: {backup}')
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
    parser.add_argument('--gui', action='store_true', help='Install agents-gui and upgrade the known desktop menu shortcut with a backup.')
    args = parser.parse_args(argv)
    try:
        files = shortcut_files(ROOT, Path.home(), args.desktop, args.distro, getpass.getuser(), args.gui)
        previous = {}
        if args.gui and args.desktop:
            previous = {p: t for p, t, _ in shortcut_files(ROOT, Path.home(), args.desktop, args.distro, getpass.getuser())
                        if p == args.desktop / 'Agent Launcher.cmd'}
            # Recognize the exact two preliminary GUI builds, never custom files.
            gui_text = files[1][1]
            encoded = gui_text.split('-EncodedCommand ')[1].split('\r\n')[0]
            target = args.desktop / 'Agent Launcher.cmd'
            previous[target] = [previous[target]]
            quoted = gui_arguments(ROOT, args.distro, getpass.getuser())
            for wait in ('', ' -Wait'):
                old_ps = ("$ErrorActionPreference='Stop';try {Start-Process -FilePath 'wsl.exe' "
                          f"-WindowStyle Hidden -ArgumentList '{quoted}'{wait};exit 0"
                          "} catch {[Console]::Error.WriteLine($_.Exception.Message);exit 1}")
                old_encoded = base64.b64encode(old_ps.encode('utf-16le')).decode('ascii')
                previous[target].append(gui_text.replace(encoded, old_encoded))
        preflight(files, previous)
        if args.dry_run:
            for path, text, _ in files:
                print(f'{path}:\n{text}')
            return 0
        install(files, previous)
        if str(Path.home() / '.local' / 'bin') not in os.environ.get('PATH', '').split(os.pathsep):
            print('The shortcut directory is not on this terminal\'s PATH. Use ~/.local/bin/agents directly or open a new login terminal.')
        print('Run agents-gui for the desktop app.' if args.gui else 'Run agents to open the menu.')
        print('No agents were started by installation.')
        return 0
    except (OSError, ValueError) as exc:
        print(f'Installer: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
