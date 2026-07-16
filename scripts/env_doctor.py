#!/usr/bin/env python3
"""env_doctor.py — boot-time machine-local credential/infra presence check.

The repo travels via git; machine-local infrastructure does not
(PROME/MACHINE_LOCAL.md is the human-readable inventory). This check makes a
missing or misplaced credential a 5-second boot diagnosis instead of a
mid-session discovery (7/2 instance: desktop FRED key absent -> dashboard rows
silently unknown; 13:00 HY timer would have failed).

Presence-only: no network calls, runs <1s. Cwd-proof (paths anchor to this
file, not the launch cwd).

Canon: FORGE/tools/market-data/.env is the SINGLE per-box home for API keys.
systemd user services never read ~/.bashrc, and every FRED/EIA consumer falls
back to this .env (fetch.py _load_dotenv + the 7/1 scrub loaders) - so a key
in ~/.bashrc is pure drift surface: a rotation that updates one home and not
the other leaves a stale key live. This script flags bashrc copies.

Usage: python3 scripts/env_doctor.py [--quiet] [--env-file PATH]
  --quiet     print problems only (exit code still signals)
  --env-file  override the .env path (testing)
Exit: 0 = required keys present; 1 = a required key/file is missing.
"""
import re
import socket
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_ENV_FILE = REPO / "FORGE" / "tools" / "market-data" / ".env"
REQUIRED_KEYS = ["FRED_API_KEY", "EIA_API_KEY", "PJM_API_KEY"]  # expected on EVERY box

# Hostname-keyed expectations for machine-local extras. Only list items whose
# ABSENCE on that box is a problem; boxes intentionally without an item (per
# MACHINE_LOCAL.md) get no entry and no noise.
MACHINE_EXTRAS = {
    "DESKTOP-BC6EF81": [  # desktop (verified 2026-07-02)
        ("kalshi creds (ORACLE lane)", Path.home() / ".config" / "kalshi" / "private_key.pem"),
        ("liquid-hy-watch timer unit", Path.home() / ".config" / "systemd" / "user" / "liquid-hy-watch.timer"),
        ("pre-scrub mirror backup (until public-flip)", Path.home() / "Research-workspace-PRESCRUB-BACKUP-20260630.git"),
    ],
    # "WilliePOwen" (laptop): no extras expected — kalshi/timer absence is by design.
}


def parse_env_names(env_file: Path) -> set:
    names = set()
    for line in env_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            if v.strip():
                names.add(k.strip())
    return names


def main() -> int:
    args = sys.argv[1:]
    quiet = "--quiet" in args
    env_file = DEFAULT_ENV_FILE
    if "--env-file" in args:
        env_file = Path(args[args.index("--env-file") + 1])

    host = socket.gethostname()
    problems = 0
    notes = []

    if not env_file.exists():
        print(f"ENV-DOCTOR ✗ MISSING {env_file} — all FRED/EIA pulls fail; see PROME/MACHINE_LOCAL.md FRED row")
        return 1

    names = parse_env_names(env_file)
    for k in REQUIRED_KEYS:
        if k in names:
            notes.append(f"✓ {k} present in .env")
        else:
            print(f"ENV-DOCTOR ✗ {k} missing/empty in {env_file} — see PROME/MACHINE_LOCAL.md FRED row")
            problems += 1

    # Single-home drift check: keys must live ONLY in the .env.
    bashrc = Path.home() / ".bashrc"
    if bashrc.exists():
        text = bashrc.read_text()
        for k in REQUIRED_KEYS:
            if re.search(rf"^\s*export\s+{k}=", text, re.M):
                print(f"ENV-DOCTOR ⚠ {k} ALSO in ~/.bashrc — two homes = rotation drift; single home is the .env (drop the bashrc line)")

    for label, p in MACHINE_EXTRAS.get(host, []):
        if p.exists():
            notes.append(f"✓ {label}")
        else:
            print(f"ENV-DOCTOR ⚠ [{host}] expected machine-local item ABSENT: {label} ({p})")

    if not quiet:
        for n in notes:
            print(f"ENV-DOCTOR {n}")
        print(f"ENV-DOCTOR: {'CLEAN' if problems == 0 else str(problems) + ' REQUIRED missing'} on {host}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
