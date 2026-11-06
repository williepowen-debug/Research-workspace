#!/usr/bin/env python3
"""PROME-only Claude asyncRewake hook. Exit 2 emits a packet-pointer reminder.

No sockets, agent launches, Git mutations, receipt writes or background retry of
response publication. A listener belongs to the Claude process that started it.
"""
import fcntl
import json
import os
from pathlib import Path
import re
import sys
import sqlite3
import time

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from notifications import Notifications, process_identity, session_parent, interactive_parent


def run(payload, root, state, *, parent=None, poll=5, lifetime=43200, interactive=None):
    if Path(payload.get('cwd','')).resolve() != (root/'PROME').resolve():
        return 0
    session = payload.get('session_id')
    if not isinstance(session,str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,100}',session):
        return 0
    queue = Notifications(state)
    event = payload.get('hook_event_name')
    if event == 'SessionEnd':
        queue.end(session)
        return 0
    if event not in {'SessionStart','PostToolUse','Stop'}:
        return 0
    parent = parent or session_parent()
    if parent is None or not (interactive_parent(parent) if interactive is None else interactive):
        return 0  # Cannot claim a live session from a test/unknown caller.
    watcher = process_identity(os.getpid())
    if watcher is None or not queue.claim(session,watcher,replace=event=='SessionStart'):
        return 0
    with (queue.state/'notification-listener.lock').open('a') as lock:
        deadline = time.monotonic()+15
        while True:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX|fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if time.monotonic() >= deadline:
                    return 0
                time.sleep(min(poll, .25))
        end = time.monotonic()+lifetime
        while time.monotonic()<end and process_identity(parent['pid']) == parent:
            if not queue.heartbeat(session,watcher):return 0
            notices = queue.pending(session)
            if notices:
                # Fixed paths/IDs only: user text is not injected as instructions.
                valid=[]
                for notice in notices:
                    if (re.fullmatch(r'[0-9a-f]{32}', notice['id'])
                            and re.fullmatch(r'[0-9a-f]{64}',notice['sha'])
                            and notice['packet'] in {f"PROME/inbox/decisions-{notice['id']}-from-CATO.md",
                                                     f"PROME/inbox/processed/decisions-{notice['id']}-from-CATO.md"}):
                        valid.append(notice)
                if valid:
                    queue.attempted(session,[n['id'] for n in valid])
                    print('Decisions app: published answers await your read. This is notification only, not an approval or read receipt. '
                          'Run the existing owner intake, review conditions and possible chat conflicts, and read each ruling back to Will.\n'
                          +'\n'.join(n['packet']+' (event SHA256 '+n['sha']+')' for n in valid),file=sys.stderr,flush=True)
                    return 2
            time.sleep(poll)
        return 0


def main():
    try:
        raw=sys.stdin.read(200001)
        if len(raw)>200000:return 0
        payload=json.loads(raw)
        if not isinstance(payload,dict):return 0
        return run(payload,HERE.parents[4],HERE/'local-state')
    except (OSError,ValueError,TypeError,KeyError,sqlite3.Error):
        return 0  # Do not block unrelated owner work or report false notification.


if __name__=='__main__':raise SystemExit(main())
