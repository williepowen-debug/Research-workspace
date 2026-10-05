#!/usr/bin/env python3
"""Run the advancing boot gate once per chosen run directory; retain its evidence."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]


def write_json(path, value):
    temporary = path.with_suffix(".tmp")
    with temporary.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2)
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


def run_once(run_dir, sessions_json=None, charter_mode="explicit"):
    if charter_mode not in ("explicit", "injected"):
        raise ValueError("Invalid charter mode")
    run_dir = Path(run_dir).resolve()
    claim = {"repository": str(ROOT.resolve()), "mode": "boot"}
    try:
        run_dir.mkdir(parents=True, exist_ok=False, mode=0o700)
    except FileExistsError:
        try:
            attempt = json.loads((run_dir / "attempt.json").read_text())
            if not isinstance(attempt, dict) or any(attempt.get(k) != v for k, v in claim.items()):
                raise ValueError("Attempt belongs to another repository or mode")
            done = json.loads((run_dir / "completed.json").read_text())
            if (done.get("repository") != claim["repository"] or
                    type(done.get("returncode")) is not int or
                    not (run_dir / "gate.txt").is_file()):
                raise ValueError("Invalid completion receipt")
            print(f"Saved boot verdict from {attempt.get('attempted_at', 'UNKNOWN time')} "
                  f"rc={done['returncode']}; charter_mode={done.get('charter_mode', 'UNKNOWN')} "
                  f"(saved coverage; requested {charter_mode}); NOT rerun. Read {run_dir / 'gate.txt'}")
            return done["returncode"]
        except (OSError, ValueError, AttributeError) as exc:
            print(f"UNKNOWN: claimed boot has no valid completion ({exc}). Inspect {run_dir}; NOT rerun.")
            return 2
    write_json(run_dir / "attempt.json", {**claim, "charter_mode": charter_mode, "attempted_at": dt.datetime.now(dt.timezone.utc).isoformat()})
    # The ONLY advancing caller: a bare `prome_gate.py boot` is non-advancing since 2026-10-05.
    command = [sys.executable, str(ROOT / "PROME/tools/prome_gate.py"), "boot", "--advance-board",
               "--log-dir", str(run_dir / "checks"), "--charter-mode", charter_mode]
    if sessions_json:
        command += ["--sessions-json", str(Path(sessions_json).resolve())]
    print(f"Boot attempt claimed; full output: {run_dir / 'gate.txt'}", flush=True)
    with (run_dir / "gate.txt").open("x", encoding="utf-8") as output:
        result = subprocess.run(command, cwd=ROOT, stdout=output, stderr=subprocess.STDOUT)
        output.flush()
        os.fsync(output.fileno())
    # A killed child is not a completed verdict. Preserve the claim for inspection.
    if result.returncode < 0:
        print("UNKNOWN: gate interrupted; inspect saved output. NOT retried.")
        return 2
    # L294 F-7 follow-up: the gate's rc=2 means INCOMPLETE — it RAN and reported
    # which checks did not. That is a real verdict with a real report, so it is
    # recorded like any other; suppressing the receipt only replaced the saved
    # verdict with an opaque "no valid completion" on the next call, which is worse.
    # ⚠️ The receipt still prevents a second BOARD-advancing attempt through this
    # directory (BOOT.md's one-shot contract), so after fixing the named input there
    # is no in-session path back to a COMPLETE gate through the same --run-dir.
    # That is a contract question for Will, NOT something to route around here:
    # inventing another run directory is exactly what BOOT.md forbids.
    write_json(run_dir / "completed.json",
               {**claim, "charter_mode": charter_mode, "returncode": result.returncode,
                "incomplete": result.returncode == 2})
    label = ("INCOMPLETE — the gate ran but some checks did NOT; their subjects are "
             "UNKNOWN, not clean" if result.returncode == 2 else "Boot verdict")
    print(f"{label} rc={result.returncode}; read {run_dir / 'gate.txt'} with boot_read.py.")
    return result.returncode


def run_refresh(run_dir, sessions_json=None, charter_mode="explicit"):
    """Fresh mechanical observations after a completed boot; never advance BOARD.

    Keep the original claim/receipt untouched. An incomplete original is not a
    baseline, and fresh read-only observations cannot turn it into one.
    """
    if charter_mode not in ("explicit", "injected"):
        raise ValueError("Invalid charter mode")
    run_dir = Path(run_dir).resolve()
    claim = {"repository": str(ROOT.resolve()), "mode": "boot"}
    try:
        attempt = json.loads((run_dir / "attempt.json").read_text())
        done = json.loads((run_dir / "completed.json").read_text())
        if not isinstance(attempt, dict) or not isinstance(done, dict):
            raise ValueError("Malformed original receipt")
        if any(attempt.get(k) != v or done.get(k) != v for k, v in claim.items()):
            raise ValueError("Original boot belongs to another repository or mode")
        if (type(done.get("returncode")) is not int or done["returncode"] not in (0, 1)
                or done.get("incomplete") is not False or not (run_dir / "gate.txt").is_file()):
            raise ValueError("Original boot incomplete or completion invalid")
        stamp = dt.datetime.fromisoformat(attempt["attempted_at"])
        if stamp.tzinfo is None or stamp > dt.datetime.now(dt.timezone.utc):
            raise ValueError("Original observation time invalid")
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f"UNKNOWN: refresh requires a valid completed original boot ({exc}); NOT run.")
        return 2
    refresh = Path(tempfile.mkdtemp(prefix="refresh-", dir=run_dir))
    receipt = {"repository": str(ROOT.resolve()), "mode": "refresh", "original_run": str(run_dir), "charter_mode": charter_mode,
               "observed_at": dt.datetime.now(dt.timezone.utc).isoformat(), "board_advance": False}
    write_json(refresh / "attempt.json", receipt)
    command = [sys.executable, str(ROOT / "PROME/tools/prome_gate.py"), "refresh",
               "--log-dir", str(refresh / "checks"), "--charter-mode", charter_mode]
    if sessions_json:
        command += ["--sessions-json", str(Path(sessions_json).resolve())]
    print(f"Fresh mechanical refresh; original boot unchanged; full output: {refresh / 'gate.txt'}", flush=True)
    with (refresh / "gate.txt").open("x", encoding="utf-8") as output:
        result = subprocess.run(command, cwd=ROOT, stdout=output, stderr=subprocess.STDOUT)
        output.flush()
        os.fsync(output.fileno())
    if result.returncode not in (0, 1, 2):
        print("UNKNOWN: refresh interrupted or returned an invalid verdict; original boot unchanged.")
        return 2
    write_json(refresh / "completed.json", {**receipt, "returncode": result.returncode,
                                           "incomplete": result.returncode == 2})
    print(f"Fresh mechanical refresh rc={result.returncode}; read {refresh / 'gate.txt'} and named logs. "
          "Manual/private steps still required; this is not a complete boot receipt.")
    return result.returncode


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--charter-mode", choices=("explicit", "injected"), default="explicit",
                    help="Only use injected when root/local context injection is confirmed")
    ap.add_argument("--run-dir", required=True, help="Choose ONCE per boot; reuse on retries")
    ap.add_argument("--sessions-json", help="Optional fresh same-host session_bridge snapshot")
    ap.add_argument("--refresh", action="store_true", help="Fresh non-advancing checks after a completed original boot")
    args = ap.parse_args()
    try:
        return (run_refresh if args.refresh else run_once)(args.run_dir, args.sessions_json, args.charter_mode)
    except (OSError, ValueError) as exc:
        print(f"UNKNOWN: {exc}; inspect the run directory before any further action.")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
