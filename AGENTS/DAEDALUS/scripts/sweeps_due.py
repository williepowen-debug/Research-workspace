#!/usr/bin/env python3
"""sweeps_due.py — DAEDALUS recurring-maintenance cadence check.

Reads sweeps/REGISTRY.tsv and prints any ACTIVE sweep whose cadence has elapsed
(today - last_run >= cadence_days). Wired into the DAEDALUS SPAWN PROTOCOL so a
recurring sweep can't silently lapse. Detection only — it never runs a sweep or
touches a file.

Exit contract (CHECK_STANDARD §9, adopted 2026-08-17 self-audit C1 — supersedes
the founding "always 0" contract, which was PAT-110's twin):
    0 = clean (registry read whole, nothing due, self-row current)
    1 = FINDINGS (sweeps DUE and/or DAEDALUS self-row stale)
    2 = CANNOT-CERTIFY (registry missing or any row un-parseable) — dominates.
All output on STDOUT (§8 rule 1 — stderr-only warnings die in wrappers).
The clean line states its perimeter (§2): rows tracked + rows skipped.

Also checks (PAT-050 fix-form, self-audit F8/B6): the DAEDALUS row in
FLEET_MAP.tsv — Last_scored older than SELF_ROW_MAX_DAYS prints a FINDINGS
line. File-readable trigger: re-cutting the row quiets it, no manual reset.

Usage (cwd-proof, self-locating via __file__ — run from anywhere):
    python3 "$(git rev-parse --show-toplevel)/AGENTS/DAEDALUS/scripts/sweeps_due.py"
"""
import csv
import datetime
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REGISTRY = os.path.normpath(os.path.join(HERE, "..", "sweeps", "REGISTRY.tsv"))
FLEETMAP = os.path.normpath(os.path.join(HERE, "..", "FLEET_MAP.tsv"))
SELF_ROW_MAX_DAYS = 5  # the defect recurred at 5d twice (8/12, 8/17) — set from measurement


def check_self_row(today):
    """Return a findings line if the DAEDALUS FLEET_MAP row is stale, else None.
    Returns a CANNOT-CERTIFY marker string on read failure (never silent)."""
    try:
        with open(FLEETMAP, encoding="utf-8") as f:
            for raw in f:
                cells = raw.rstrip("\n").split("\t")
                if cells and cells[0].strip() == "DAEDALUS":
                    # Last_scored is the ISO-date field; locate it positionally (field 5, 0-idx 4)
                    # with a scan fallback so a schema shift fails loud, not wrong.
                    dates = [c.strip() for c in cells if len(c.strip()) == 10 and c.strip()[4] == "-"]
                    if not dates:
                        return "CANNOT-CERTIFY: DAEDALUS FLEET_MAP row has no parseable Last_scored date"
                    last = datetime.date.fromisoformat(dates[0])
                    age = (today - last).days
                    if age >= SELF_ROW_MAX_DAYS:
                        return (f"⏰ SELF-ROW: DAEDALUS FLEET_MAP row Last_scored {age}d old "
                                f"(max {SELF_ROW_MAX_DAYS}d, PAT-050) — re-cut or confirm current")
                    return None
        return "CANNOT-CERTIFY: no DAEDALUS row found in FLEET_MAP.tsv"
    except (OSError, ValueError) as e:
        return f"CANNOT-CERTIFY: FLEET_MAP self-row check failed ({e})"


REPO = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
AGENT_DIR = os.path.normpath(os.path.join(HERE, ".."))   # registry playbook paths are DAEDALUS-relative ("sweeps/X.md")


def playbook_exists(pb):
    """Registry paths are relative to AGENTS/DAEDALUS/ by convention; repo-root is the fallback.
    (First cut of this guard, 2026-09-03, checked repo-root only and fired on two rows whose
    playbooks exist — the selftest had used a repo-relative 'present' path, so it certified the
    wrong base: finding_instrument_reports_clean_against_the_wrong_reference, on a guard 5 min old.)"""
    return os.path.exists(os.path.join(AGENT_DIR, pb)) or os.path.exists(os.path.join(REPO, pb))


def selftest():
    """Guard drill (CHECK_STANDARD §3): a registry row whose playbook path does not exist must
    fire PLAYBOOK MISSING (rc 2); a row whose playbook exists must not. Built 2026-09-03 after
    sweeps/GATE_BASIS_SWEEP.md sat absent for a day behind a row this script read as clean."""
    import tempfile, subprocess
    today = datetime.date.today().isoformat()
    hdr = "task\tcadence_days\tlast_run\tplaybook\tstatus\tresolve_by\tlast_findings\n"
    fails = 0
    with tempfile.TemporaryDirectory() as td:
        reg = os.path.join(td, "R.tsv")
        open(reg, "w", encoding="utf-8").write(hdr + f"Present\t21\t{today}\tscripts/sweeps_due.py\tactive\t\tx\n"
                                                    f"Missing\t21\t{today}\tsweeps/NO_SUCH_PLAYBOOK.md\tactive\t\tx\n")
        p = subprocess.run([sys.executable, os.path.abspath(__file__), "--registry", reg, "--no-profile-clock"],
                           capture_output=True, text=True)
        fire = p.returncode == 2 and "PLAYBOOK MISSING" in p.stdout and "Missing" in p.stdout and "Present" not in p.stdout.split("PLAYBOOK MISSING")[1].split("\n")[0]
        print(f"  {'✓' if fire else '✗'} missing playbook ⇒ rc 2 + PLAYBOOK MISSING names the row (rc={p.returncode})"); fails += not fire
        open(reg, "w", encoding="utf-8").write(hdr + f"Present\t21\t{today}\tscripts/sweeps_due.py\tactive\t\tx\n"
                                                    f"PresentRepoRel\t21\t{today}\tscripts/claim_check.py\tactive\t\tx\n")
        p = subprocess.run([sys.executable, os.path.abspath(__file__), "--registry", reg, "--no-profile-clock"],
                           capture_output=True, text=True)
        clean = p.returncode == 0 and "PLAYBOOK MISSING" not in p.stdout
        print(f"  {'✓' if clean else '✗'} present playbook ⇒ clean, rc 0 (rc={p.returncode})"); fails += not clean
    print("sweeps_due SELFTEST " + ("✓ 2/2" if not fails else f"✗ {fails}/2 FAILED"))
    return 1 if fails else 0


def main():
    global REGISTRY
    if "--selftest" in sys.argv:
        return selftest()
    if "--registry" in sys.argv:
        REGISTRY = sys.argv[sys.argv.index("--registry") + 1]
    no_pc = "--no-profile-clock" in sys.argv
    today = datetime.date.today()
    due, tracked, skipped = [], 0, []
    missing_pb = []   # playbook path in the row does not exist (2026-09-03 guard)
    overdue, skipped_rb = [], []   # resolve_by: dated obligations, independent of cadence
    cannot_certify = False
    try:
        with open(REGISTRY, encoding="utf-8") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                task = (row.get("task") or "").strip()
                if not task or task.startswith("#"):
                    continue
                if (row.get("status") or "active").strip().lower() != "active":
                    continue
                try:
                    last = datetime.date.fromisoformat((row.get("last_run") or "").strip())
                    cad = int((row.get("cadence_days") or "").strip())
                except (ValueError, TypeError):
                    skipped.append(task)
                    continue
                tracked += 1
                pb_path = (row.get("playbook") or "").strip()
                if pb_path and not playbook_exists(pb_path):
                    missing_pb.append((task, pb_path))
                age = (today - last).days
                if age >= cad:
                    due.append((task, age, cad, (row.get("playbook") or "").strip()))

                # ── resolve_by: a DATED OBLIGATION inside a queue row, independent of cadence.
                # ADDED 2026-08-23, and it exists because of a miss it would have caught.
                # The profile-refresh row said, in free text, "AEOLUS FIRST (hard date — service
                # BEFORE Falsification #2 ~8/24)". I ran Falsification #2 on 8/23 without it, and
                # THIS SCRIPT PRINTED "✅ none due" all evening and was correct on its own terms:
                # it read only cadence, and that row's 21d clock (last 8/17) is not due until ~9/7.
                # A dated assertion carried in prose is a string; reading it never evaluates it
                # [[finding_dated_carry_item_has_no_expiry_check]]. This is PAT-115's Resolve_By
                # applied to my OWN register — a fix I built for other people's registers and had
                # never applied here, which is the class-not-instance failure again.
                rb = (row.get("resolve_by") or "").strip()
                if rb:
                    try:
                        rbd = datetime.date.fromisoformat(rb)
                    except ValueError:
                        skipped_rb.append((task, rb))
                    else:
                        if today >= rbd:
                            overdue.append((task, (today - rbd).days, rb,
                                            (row.get("playbook") or "").strip()))
    except OSError:
        print(f"🔴 sweeps_due CANNOT-CERTIFY: registry not readable at {REGISTRY} — "
              f"0 of the registered sweeps were cadence-checked")
        return 2

    for task in skipped:
        print(f"⚠️  sweeps_due: un-parseable row for '{task}' (check last_run/cadence_days) — NOT cadence-checked")
        cannot_certify = True

    for task, rb in skipped_rb:
        print(f"⚠️  sweeps_due: un-parseable resolve_by {rb!r} on '{task}' — that dated obligation is NOT checked")
        cannot_certify = True

    # PLAYBOOK PRESENCE (2026-09-03): a registry row is a POINTER to a procedure; this script read
    # rows only, so sweeps/GATE_BASIS_SWEEP.md was absent for a day behind a row that printed clean
    # (finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit). A sweep with no
    # playbook cannot be run, so it cannot be certified: rc 2, named.
    for task, pb in missing_pb:
        print(f"🔴 PLAYBOOK MISSING: '{task}' → {pb} does not exist — the row reads clean over a file that is not there; write the playbook or pause the row")
        cannot_certify = True

    self_row = check_self_row(today)
    if self_row and self_row.startswith("CANNOT-CERTIFY"):
        print(f"🔴 sweeps_due {self_row}")
        cannot_certify = True
        self_row = None

    if overdue:
        for task, over, rb, pb in sorted(overdue, key=lambda r: r[1], reverse=True):
            print(f"🔴 RESOLVE_BY PASSED: {task} — dated obligation {rb} is {over}d past "
                  f"(this is NOT a cadence miss; the cadence clock may be perfectly fine) → {pb}")
    if due:
        for task, age, cad, pb in sorted(due, key=lambda r: r[1] - r[2], reverse=True):
            print(f"⏰ DUE: {task} — last run {age}d ago (cadence {cad}d, +{age - cad}d over) → {pb}")
    if self_row:
        print(self_row)
    if not due and not overdue and not self_row and not cannot_certify:
        print(f"✅ sweeps: none due ({tracked} tracked, {len(skipped)} skipped, self-row current, "
              f"0 resolve_by passed)")

    if cannot_certify:
        return 2
    if overdue:
        return 1
    # PROFILE CLOCKS (wired 2026-09-01, PR#5): the cheap half of the profile-staleness trigger.
    # Runs as a child so its rc contract stays its own; a fired clock is a dated obligation → rc 1 here.
    if no_pc:
        return 1 if (due or self_row) else 0
    try:
        import subprocess as _sp
        pc = _sp.run([sys.executable, os.path.join(HERE, "profile_clock_check.py"), "--quiet"],
                     capture_output=True, text=True)
        for line in pc.stdout.rstrip("\n").split("\n"):
            if line: print(line)
        if pc.returncode == 2:
            print("🔴 sweeps_due CANNOT-CERTIFY: profile_clock_check rc 2 (see line above)"); return 2
        if pc.returncode == 1: due = due or ["profile clocks"]
    except Exception as e:  # never silently green
        print(f"🔴 sweeps_due CANNOT-CERTIFY: profile_clock_check could not run ({e})"); return 2
    return 1 if (due or self_row) else 0


if __name__ == "__main__":
    sys.exit(main())
