#!/usr/bin/env python3
"""Merge repo-scoped fleet hooks into current-host Claude user settings.

Preserves unrelated keys/hooks; backups and atomic replacement under a writer lock.
Other machines must run this installer separately after pulling the repository.
"""
import argparse
import copy
import fcntl
import json
import os
from pathlib import Path
import tempfile
import uuid


def install(target, source):
    desired = json.loads(source.read_text(encoding="utf-8"))["hooks"]
    target = target.resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.with_name(target.name + ".fleet-hooks.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        original = target.read_bytes() if target.exists() else None
        data = json.loads(original) if original is not None else {}
        before = copy.deepcopy(data)
        hooks = data.setdefault("hooks", {})
        for event, groups in desired.items():
            existing = hooks.setdefault(event, [])
            for group in groups:
                matcher = group.get("matcher", "")
                for hook in group["hooks"]:
                    matched = False
                    for current_group in existing:
                        if current_group.get("matcher", "") != matcher:
                            continue
                        for index, current in enumerate(current_group.get("hooks", [])):
                            if hook["command"] == current.get("command"):
                                # Same fleet-owned command must use the intended timeout/decision lifecycle.
                                current_group["hooks"][index] = copy.deepcopy(hook)
                                matched = True
                    if matched:
                        continue
                    existing.append(dict(group, hooks=[copy.deepcopy(hook)]))
        if data == before:
            print("Claude fleet hooks already installed: " + str(target))
            return
        mode = target.stat().st_mode & 0o777 if original is not None else 0o600
        if original is not None:
            backup = target.with_name(target.name + ".fleet-backup-" + uuid.uuid4().hex)
            backup.write_bytes(original)
            backup.chmod(mode)
            print("Backup: " + str(backup))
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=target.parent,
                                         prefix=target.name + ".", delete=False) as out:
            json.dump(data, out, ensure_ascii=False, indent=2)
            out.write("\n")
            out.flush()
            os.fsync(out.fileno())
            temporary = Path(out.name)
        temporary.chmod(mode)
        # Other fleet installer invocations are serialized; do not overwrite a non-cooperating edit.
        if (target.read_bytes() if target.exists() else None) != original:
            raise RuntimeError("settings changed during installation; preserved; staged copy at " + str(temporary))
        os.replace(temporary, target)
        print("Installed repo-scoped Claude fleet hooks: " + str(target))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--settings-file", type=Path, default=Path.home() / ".claude/settings.json")
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parent.parent / ".claude/settings.json")
    args = parser.parse_args()
    install(args.settings_file, args.source)
