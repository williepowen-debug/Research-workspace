#!/usr/bin/env python3
"""Open interactive Kimi with a launch-local desk profile and exact instructions."""
import argparse
import json
import os
import re
import subprocess
import uuid

import agents


def github_environment():
    """Reuse gh's current login in child memory only; never print or persist it."""
    env = os.environ.copy()
    if not env.get('GITHUB_PERSONAL_ACCESS_TOKEN', '').strip():
        try:
            result = subprocess.run(['gh', 'auth', 'token', '--hostname', 'github.com'],
                                    capture_output=True, text=True, timeout=5)
            if result.returncode == 0 and result.stdout.strip():
                env['GITHUB_PERSONAL_ACCESS_TOKEN'] = result.stdout.strip()
        except (OSError, subprocess.TimeoutExpired):
            pass  # Kimi reports the missing credential if its connector needs it.
    return env


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--name', required=True)
    parser.add_argument('--resume', action='store_true')
    parser.add_argument('prompt', nargs='?')
    args = parser.parse_args(argv)
    if not re.fullmatch(r'[A-Z][A-Z0-9_-]*', args.name):
        parser.error('Invalid agent name')
    executable = agents.kimi_executable()
    env = github_environment()
    command = [executable, '--model', agents.KIMI_MODEL, '--yolo']
    if args.resume:
        if args.prompt is not None:
            parser.error('Resume cannot include startup instructions')
        os.execve(executable, command + ['--session'], env)
        return
    if args.prompt is None:
        parser.error('New sessions require startup instructions')
    directory = agents.cache_folder() / 'kimi' / uuid.uuid4().hex
    directory.mkdir(parents=True, mode=0o700)
    instructions = directory / 'instructions.txt'
    instructions.write_text(args.prompt, encoding='utf-8')
    profile = directory / 'agent.md'
    profile.write_text(
        '---\nname: launcher-' + re.sub(r'[_-]+', '-', args.name.lower()).rstrip('-') + '\n'
        'description: Operator-selected research desk session\n---\n\n'
        '${base_prompt}\n\n'
        'This session was opened by Will through Agent Launcher for ' + args.name + '.\n'
        'When Will says Start, first read the prepared instruction file at '
        + json.dumps(str(instructions)) + '. It contains the exact startup instructions '
        'and optional task supplied through the launcher. Follow those instructions and '
        'the canonical repository and desk rules. Recover existing approvals without '
        'inventing new work or permissions. Later user instructions may refine the task.\n',
        encoding='utf-8')
    print('Opening ' + args.name + ' with Kimi K3.1 Pro. Type Start to run your prepared instructions.',
          flush=True)
    os.execve(executable, command + ['--agent-file', str(profile)], env)


if __name__ == '__main__':
    main()
