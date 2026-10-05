#!/usr/bin/env python3
"""PostToolUse(Edit|Write|MultiEdit) hook — validates a parsed surface the instant it is saved.
Will-approved 2026-08-29 (".claude/ investigate" — item 2). PROME-scoped.

Targets (by path suffix):
  FORGE/STATUS.md   → TERRY's consumer parser `positions_from_forge.py --selftest`
                      (PAT-069: the 7/30 restructure broke the parser SILENTLY — it reported
                      clean while emitting phantom positions; this hook makes that loud at save)
                    + read-cap byte meter (32,550 B) as a WARNING line
  PROME/GATES.tsv   → prome_gate token-vocabulary / fired / review_by checks (read-only funcs)
  PROME/DOCKET.tsv  → prome_gate overdue-annotation check + changed-row byte cap (docket_row_cap.py)

Protocol: stdin JSON {tool_name, tool_input:{file_path}}. exit 2 + stderr = the message is
shown to the model as an error it must fix; exit 0 = silent. Parse failure ⇒ exit 0.
"""
import json, pathlib, subprocess, sys

ROOT = pathlib.Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                   capture_output=True, text=True).stdout.strip() or ".")
READ_CAP = 32_550


def forge_status(p: pathlib.Path) -> list[str]:
    msgs = []
    r = subprocess.run([sys.executable, str(ROOT / "AGENTS/TERRY/scripts/positions_from_forge.py"),
                        "--selftest"], capture_output=True, text=True, cwd=ROOT, timeout=60)
    if r.returncode != 0:
        tail = "\n".join((r.stdout + r.stderr).strip().splitlines()[-8:])
        msgs.append(f"⛔ FORGE/STATUS.md FAILS its consumer parser (positions_from_forge.py --selftest rc={r.returncode}). "
                    f"This is PAT-069 — fix the structure before anything else.\n{tail}")
    size = p.stat().st_size
    if size > READ_CAP:
        msgs.append(f"⚠️ FORGE/STATUS.md is {size:,} B > {READ_CAP:,} B read-whole cap (advisory — hot/cold split owed).")
    return msgs


def prome_gate_checks(which: str) -> list[str]:
    import importlib.util
    spec = importlib.util.spec_from_file_location("pg", ROOT / "PROME/tools/prome_gate.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    if which == "gates":
        m.check_gates_tsv()
    else:
        m.check_docket_overdue()
    return [f"⛔ {name}: {detail}" for (sev, name, ok, detail, owner) in m.results
            if not ok and sev == m.BLOCK] + \
           [f"⚠️ {name}: {detail}" for (sev, name, ok, detail, owner) in m.results
            if not ok and sev == m.ADVISE]


def docket_row_cap() -> list[str]:
    """Changed-row byte cap at save time (rc 0 clean or DORMANT · 1 over · 2 could not establish → advisory).
    Dormant (DOCKET_ROW_CAP_BYTES unset) is silent here by necessity: this hook's exit-0 stderr is not
    shown to the model; the pre-commit hook and the closeout gate carry the notice."""
    r = subprocess.run([sys.executable, str(ROOT / "PROME/tools/docket_row_cap.py"), "--quiet"],
                       capture_output=True, text=True, cwd=ROOT, timeout=60)
    if r.returncode == 1:
        return ["⛔ " + r.stdout.strip()]
    if r.returncode != 0:
        return [f"⚠️ docket_row_cap could not establish (rc={r.returncode}): {(r.stdout + r.stderr).strip()[:200]}"]
    return []


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    if data.get("tool_name") not in ("Edit", "Write", "MultiEdit"):
        return 0
    fp = (data.get("tool_input") or {}).get("file_path", "") or ""
    if not fp:
        return 0
    p = pathlib.Path(fp)
    if not p.is_absolute():
        p = ROOT / p   # PROME launches from PROME/; a cwd-relative path would resolve under PROME/ and fail open (RAV 8/29)
    try:
        if fp.endswith("FORGE/STATUS.md"):
            msgs = forge_status(p)
        elif fp.endswith("PROME/GATES.tsv"):
            msgs = prome_gate_checks("gates")
        elif fp.endswith("PROME/DOCKET.tsv"):
            msgs = prome_gate_checks("docket") + docket_row_cap()
        else:
            return 0
    except Exception as e:
        sys.stderr.write(f"forge_validate: check itself failed ({type(e).__name__}: {e}) — not a verdict on the file\n")
        return 0
    hard = [m for m in msgs if m.startswith("⛔")]
    soft = [m for m in msgs if m.startswith("⚠️")]
    if hard or soft:
        sys.stderr.write("[forge_validate — post-save check on " + p.name + "]\n" + "\n".join(hard + soft) + "\n")
    return 2 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
