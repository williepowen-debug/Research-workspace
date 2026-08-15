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
import shutil
import socket
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_ENV_FILE = REPO / "FORGE" / "tools" / "market-data" / ".env"
REQUIRED_KEYS = ["FRED_API_KEY", "EIA_API_KEY", "PJM_API_KEY",
                 # FFIEC CDR PWS (added 2026-08-07, Will-registered same day —
                 # gates WAL MI3; REST+JWT, see WAL inbox 8/7 packet for recipe):
                 "FFIEC_CDR_TOKEN", "FFIEC_CDR_USERNAME",
                 # e-Stat app ID (added 2026-08-11, PROME 8/9 packet — gates SAM
                 # cpi_japan.py; key registered "SAM", MACHINE_LOCAL row 24):
                 "ESTAT_APPID"]  # expected on EVERY box

# JWT expiry probe (2026-08-07): the FFIEC token is a 90-day JWT that dies
# SILENTLY at expiry (the ESTAT_APPID class — a dead key looks like a broken
# service). The token is unsigned (alg none) so the exp claim decodes locally
# with no secret handling. Warn at <=14d, count as a REQUIRED problem when
# expired. Undecodable token => warn, never crash (fail-safe, not fail-blind).
JWT_EXPIRY_KEYS = ["FFIEC_CDR_TOKEN"]
JWT_WARN_DAYS = 14


def jwt_expiry_check(env_file, notes):
    """Returns problem count. Prints its own lines (PAT-074: the null case says
    what it checked)."""
    import base64 as _b64, datetime as _dt, json as _json
    problems = 0
    try:
        vals = {}
        for line in env_file.read_text().splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, _, v = line.partition("=")
                vals[k.strip()] = v.strip()
        for key in JWT_EXPIRY_KEYS:
            tok = vals.get(key, "")
            if not tok:
                continue  # absence already reported by the REQUIRED_KEYS pass
            try:
                payload = tok.split(".")[1]
                payload += "=" * (-len(payload) % 4)
                exp = _json.loads(_b64.urlsafe_b64decode(payload))["exp"]
                days = (_dt.datetime.fromtimestamp(exp, _dt.timezone.utc)
                        - _dt.datetime.now(_dt.timezone.utc)).days
                if days < 0:
                    print(f"ENV-DOCTOR ✗ {key} EXPIRED {-days}d ago — regenerate via Will's "
                          f"FFIEC PWS account login (90-day tokens); pulls fail 'Access Denied'")
                    problems += 1
                elif days <= JWT_WARN_DAYS:
                    print(f"ENV-DOCTOR ⚠ {key} expires in {days}d — Will regenerates via his "
                          f"FFIEC PWS account login, then update .env on BOTH boxes")
                else:
                    notes.append(f"✓ {key} valid {days}d more")
            except Exception:
                print(f"ENV-DOCTOR ⚠ {key} present but not a decodable JWT — expiry unknown; "
                      f"verify with a live pull before trusting it")
    except OSError:
        pass
    return problems

# CLI tools expected on EVERY box. Non-fatal (warn only): their absence breaks
# a fleet rule, not a data pull, so it must not trip the FRED-citation gate.
# (name, why, fallback-hint)
EXPECTED_CLIS = [
    ("trash", "rule #11 trash > rm (package: trash-cli)", "use `gio trash <file>` until installed — NEVER rm"),
    # MACHINE_LOCAL row 19 — NB installed ≠ authed (the 7/2 verified trap): this
    # probe catches only a MISSING binary; auth state is in the NOT-checked perimeter.
    ("gh", "GitHub API/PR/secrets ops (plain git still works)", "install + `gh auth login` per MACHINE_LOCAL"),
]

# Expected on EVERY box (unlike host-keyed MACHINE_EXTRAS). Warn tier — the
# Telegram lane is messaging, and BLOCKING stays market-data-scoped (8/7 ruling).
# (label, home-relative glob, consequence) — inventory sweep 2026-08-11.
GLOBAL_EXTRAS = [
    ("telegram channel tokens", ".claude/channels/telegram*",
     "WALTER/PROME Telegram delivery fails (MACHINE_LOCAL row 13)"),
]

# Venv-dep probe (added 2026-07-30, Will-approved — TERRY flag: this script
# reported CLEAN on a box where fetch.py/dashboard.py could not run, because
# the venv layer was never probed; a false-clean in the tool designed to catch
# exactly this). Presence-only by design: a site-packages directory check, no
# imports and no subprocess, so the <1s promise holds. A present-but-broken
# package still passes — the same fidelity trade key-presence already makes.
# REQUIRED deps break market-data pulls (the rule-#4 lean) => BLOCKING, same
# class as a missing FRED key. EXPECTED deps break agent scripts => warn-only.
VENV_DIR = REPO / ".venv"
REQUIRED_VENV_DEPS = ["yfinance", "pandas"]
EXPECTED_VENV_DEPS = ["bs4", "pdfminer"]
# MESSAGING tier (ruled 2026-08-07, built 8/11 — SAM PyYAML outage: 'CLEAN'
# printed on a box where DM v1 could not run): NON-BLOCKING by design — never
# widens the BLOCKING set (its market-data lean is deliberate). PyYAML ships
# as package dir `yaml`. NB: scripts/requirements.txt pins pyyaml but is
# CI-SCOPED (feeds GH Actions, never .venv) — a pin there is NOT coverage.
MESSAGING_VENV_DEPS = [("yaml", "PyYAML — MESSAGING/DM v1 lane dark without it; fix: .venv/bin/pip install pyyaml")]


def venv_dep_present(name: str) -> bool:
    for sp in VENV_DIR.glob("lib/python3.*/site-packages"):
        if (sp / name).is_dir() or any(sp.glob(name + "-*.dist-info")):
            return True
    return False


# Hostname-keyed expectations for machine-local extras. Only list items whose
# ABSENCE on that box is a problem; boxes intentionally without an item (per
# MACHINE_LOCAL.md) get no entry and no noise.
MACHINE_EXTRAS = {
    "DESKTOP-BC6EF81": [  # desktop (verified 2026-07-02)
        ("kalshi creds (ORACLE lane)", Path.home() / ".config" / "kalshi" / "private_key.pem"),
        ("liquid-hy-watch timer unit", Path.home() / ".config" / "systemd" / "user" / "liquid-hy-watch.timer"),
        # Retired 2026-08-14 (DAEDALUS, scripts/ lane): the "pre-scrub mirror backup"
        # row keyed on ~/Research-workspace-PRESCRUB-BACKUP-20260630.git. Backup was
        # DELETED 2026-08-14 on Will's ruling (row 17 resolved the public-flip the
        # other way — working repo private by design, demo repo is the public face),
        # so the rollback net had no trigger left and its target held the unscrubbed
        # history. The check would flag missing every desktop boot. Deleted rather
        # than inverted per the ruling's own "nothing left to verify" wording.
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
            print(f"ENV-DOCTOR ✗ {k} missing/empty in {env_file} — restore recipe: PROME/MACHINE_LOCAL.md, the row naming {k}")
            problems += 1

    problems += jwt_expiry_check(env_file, notes)

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

    for label, pat, why in GLOBAL_EXTRAS:
        if list(Path.home().glob(pat)):
            notes.append(f"✓ {label}")
        else:
            print(f"ENV-DOCTOR ⚠ expected item ABSENT on every box: {label} (~/{pat}) — {why}")

    # Venv-dep probe: the layer whose absence produced the 7/30 false-clean.
    if not VENV_DIR.is_dir():
        print(f"ENV-DOCTOR ✗ venv MISSING at {VENV_DIR} — market-data tools cannot self-heal; "
              f"fix: python3 -m venv .venv && .venv/bin/pip install yfinance pandas")
        problems += 1
    else:
        for dep in REQUIRED_VENV_DEPS:
            if venv_dep_present(dep):
                notes.append(f"✓ venv dep `{dep}`")
            else:
                print(f"ENV-DOCTOR ✗ venv dep `{dep}` MISSING — fetch.py/dashboard.py price pulls fail "
                      f"(rule #4); fix: .venv/bin/pip install {dep}")
                problems += 1
        for dep in EXPECTED_VENV_DEPS:
            if venv_dep_present(dep):
                notes.append(f"✓ venv dep `{dep}`")
            else:
                print(f"ENV-DOCTOR ⚠ venv dep `{dep}` missing — some agent scripts break; "
                      f"fix: .venv/bin/pip install {dep if dep != 'pdfminer' else 'pdfminer.six'}")

    # MESSAGING tier — advisory, never counted in `problems` (BLOCKING stays
    # market-data-scoped by the 8/7 ruling).
    if VENV_DIR.is_dir():
        for dep, why in MESSAGING_VENV_DEPS:
            if venv_dep_present(dep):
                notes.append(f"✓ venv dep `{dep}` (MESSAGING tier)")
            else:
                print(f"ENV-DOCTOR ⚠ [MESSAGING, non-blocking] venv dep `{dep}` missing — {why}")

    for cli, why, hint in EXPECTED_CLIS:
        if shutil.which(cli):
            notes.append(f"✓ `{cli}` on PATH")
        else:
            print(f"ENV-DOCTOR ⚠ `{cli}` not on PATH — {why}; {hint}")

    # Perimeter statement (ruled 2026-08-07 — a CLEAN over an unstated scope
    # certifies nothing): printed on every non-quiet run, and on quiet runs
    # whenever something failed, so no verdict ships scope-free.
    perimeter = (f"perimeter — checked: fleet .env keys ({len(REQUIRED_KEYS)}) · FFIEC JWT expiry · "
                 f"~/.bashrc single-home drift · machine extras[{host}] · venv deps "
                 f"(REQUIRED {'/'.join(REQUIRED_VENV_DEPS)} · expected {'/'.join(EXPECTED_VENV_DEPS)} · "
                 f"MESSAGING non-blocking {'/'.join(d for d, _ in MESSAGING_VENV_DEPS)}) · "
                 f"CLIs {'/'.join(c for c, _, _ in EXPECTED_CLIS)} · "
                 f"global extras ({'/'.join(l for l, _, _ in GLOBAL_EXTRAS)}) "
                 f"| NOT checked: agent-local .envs · MESSAGING service state · `gh` auth state "
                 f"(installed ≠ authed) · scripts/requirements.txt (CI-scoped pin file, not .venv coverage)")
    if not quiet:
        for n in notes:
            print(f"ENV-DOCTOR {n}")
    if not quiet or problems:
        print(f"ENV-DOCTOR {perimeter}")
    if not quiet:
        print(f"ENV-DOCTOR: {'CLEAN' if problems == 0 else str(problems) + ' REQUIRED missing'} on {host}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
