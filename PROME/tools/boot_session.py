#!/usr/bin/env python3
"""Run the advancing boot gate once per chosen run directory; retain its evidence."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]


def write_json(path, value):
    temporary = path.with_suffix(".tmp")
    with temporary.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2)
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


def run_once(run_dir, sessions_json=None):
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
                  f"rc={done['returncode']}; NOT rerun. Read {run_dir / 'gate.txt'}")
            return done["returncode"]
        except (OSError, ValueError, AttributeError) as exc:
            print(f"UNKNOWN: claimed boot has no valid completion ({exc}). Inspect {run_dir}; NOT rerun.")
            return 2
    write_json(run_dir / "attempt.json", {**claim, "attempted_at": dt.datetime.now(dt.timezone.utc).isoformat()})
    command = [sys.executable, str(ROOT / "PROME/tools/prome_gate.py"), "boot",
               "--log-dir", str(run_dir / "checks")]
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
    write_json(run_dir / "completed.json", {**claim, "returncode": result.returncode})
    print(f"Boot verdict rc={result.returncode}; read {run_dir / 'gate.txt'} with boot_read.py.")
    return result.returncode


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--run-dir", required=True, help="Choose ONCE per boot; reuse on retries")
    ap.add_argument("--sessions-json", help="Optional fresh same-host session_bridge snapshot")
    args = ap.parse_args()
    try:
        return run_once(args.run_dir, args.sessions_json)
    except (OSError, ValueError) as exc:
        print(f"UNKNOWN: {exc}; inspect the run directory before any further action.")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
