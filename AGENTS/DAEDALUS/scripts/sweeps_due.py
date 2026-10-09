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
import re
import sys
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
REGISTRY = os.path.normpath(os.path.join(HERE, "..", "sweeps", "REGISTRY.tsv"))
FLEETMAP = os.path.normpath(os.path.join(HERE, "..", "FLEET_MAP.tsv"))
SELF_ROW_MAX_DAYS = 5  # the defect recurred at 5d twice (8/12, 8/17) — set from measurement


def today_et():
    """Dated obligations use Will's Eastern calendar, independent of host timezone."""
    return datetime.datetime.now(ZoneInfo("America/New_York")).date()


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

DIRECTORY = os.path.normpath(os.path.join(HERE, "..", "FLEET_DIRECTORY.md"))


def _last_change(path_rel):
    """Newest of: last commit date (git) and, for a dirty file, today. Returns date or None."""
    import subprocess
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", path_rel], cwd=REPO,
                             capture_output=True, text=True, timeout=20).stdout.strip()
        d = datetime.date.fromisoformat(out) if out else None
        dirty = subprocess.run(["git", "status", "--porcelain", "--", path_rel], cwd=REPO,
                               capture_output=True, text=True, timeout=20).stdout.strip()
        if dirty:
            return today_et()
        return d
    except Exception:
        return None


def check_directory_stale(today):
    """ADDED 2026-09-17 (PR#6 reader R1): render_directory.py was DEAD for two days (9/15 → 9/17)
    after ROSTER gained a section it did not know; its fail-closed guard fired correctly and nobody
    ran it, because its only invocation sites were 'on FLEET_MAP row change' and the Production
    Review. FLEET_DIRECTORY.md is the boot read, so a stale one is my own next boot reading last
    week's map. This line re-derives 'stale' from the artifacts: the directory's own Generated date
    vs the newest change to either of its two sources. Returns a findings line or None."""
    try:
        with open(DIRECTORY, encoding="utf-8") as f:
            head = f.read(4000)
        m = re.search(r"Generated (\d{4}-\d{2}-\d{2})", head)
        if not m:
            return "CANNOT-CERTIFY: FLEET_DIRECTORY.md carries no 'Generated YYYY-MM-DD' stamp"
        gen = datetime.date.fromisoformat(m.group(1))
        srcs = {"AGENTS/DAEDALUS/FLEET_MAP.tsv": _last_change("AGENTS/DAEDALUS/FLEET_MAP.tsv"),
                "PROME/ROSTER.md": _last_change("PROME/ROSTER.md")}
        if any(v is None for v in srcs.values()):
            return "CANNOT-CERTIFY: directory-staleness check could not date a source (git unreadable)"
        newer = [f"{k} changed {v}" for k, v in srcs.items() if v > gen]
        if newer:
            return (f"⏰ DIRECTORY-STALE: FLEET_DIRECTORY.md generated {gen} but "
                    f"{'; '.join(newer)} — run scripts/render_directory.py (boot reads the directory)")
        return None
    except (OSError, ValueError) as e:
        return f"CANNOT-CERTIFY: directory-staleness check failed ({e})"

AGENT_DIR = os.path.normpath(os.path.join(HERE, ".."))   # registry playbook paths are DAEDALUS-relative ("sweeps/X.md")


def playbook_exists(pb):
    """Registry paths are relative to AGENTS/DAEDALUS/ by convention; repo-root is the fallback.
    (First cut of this guard, 2026-09-03, checked repo-root only and fired on two rows whose
    playbooks exist — the selftest had used a repo-relative 'present' path, so it certified the
    wrong base: finding_instrument_reports_clean_against_the_wrong_reference, on a guard 5 min old.)"""
    return os.path.exists(os.path.join(AGENT_DIR, pb)) or os.path.exists(os.path.join(REPO, pb))


def selftest_dated(today):
    """DATED drill (2026-09-04, §3 both paths): a DATED row with a FUTURE resolve_by prints NO ⏰ DUE
    however old its last_run; the same row with a PAST resolve_by fires RESOLVE_BY PASSED; a DATED row
    with no resolve_by is reported un-parseable (rc 2), never silently clean."""
    import subprocess, tempfile
    hdr = "task\tcadence_days\tlast_run\tplaybook\tstatus\tresolve_by\tlast_findings\n"
    fut = (today + datetime.timedelta(days=10)).isoformat(); past = (today - datetime.timedelta(days=3)).isoformat()
    ok_all = True
    with tempfile.TemporaryDirectory() as td:
        pb = os.path.join(td, "PB.md"); open(pb, "w").write("x")
        cases = [("future", f"Dated\tDATED\t2026-01-01\t{pb}\tactive\t{fut}\tx\n", lambda o, rc: "DUE:" not in o and "RESOLVE_BY PASSED" not in o and rc == 0),
                 ("past", f"Dated\tDATED\t2026-01-01\t{pb}\tactive\t{past}\tx\n", lambda o, rc: "RESOLVE_BY PASSED: Dated" in o and "DUE:" not in o),
                 ("no-resolve_by", f"Dated\tDATED\t2026-01-01\t{pb}\tactive\t\tx\n", lambda o, rc: "un-parseable" in o and rc == 2)]
        for name, row, pred in cases:
            reg = os.path.join(td, name + ".tsv"); open(reg, "w").write(hdr + row)
            p = subprocess.run([sys.executable, __file__, "--registry", reg, "--no-profile-clock", "--no-live-checks"], capture_output=True, text=True)
            ok = pred(p.stdout, p.returncode); ok_all &= ok
            print(f"  {'✓' if ok else '✗'} DATED {name}: rc={p.returncode} · {p.stdout.strip().splitlines()[0][:90] if p.stdout.strip() else '(no output)'}")
    return ok_all


def selftest():
    """Guard drill (CHECK_STANDARD §3): a registry row whose playbook path does not exist must
    fire PLAYBOOK MISSING (rc 2); a row whose playbook exists must not. Built 2026-09-03 after
    sweeps/GATE_BASIS_SWEEP.md sat absent for a day behind a row this script read as clean."""
    import tempfile, subprocess
    today = today_et().isoformat()
    hdr = "task\tcadence_days\tlast_run\tplaybook\tstatus\tresolve_by\tlast_findings\n"
    fails = 0
    with tempfile.TemporaryDirectory() as td:
        reg = os.path.join(td, "R.tsv")
        open(reg, "w", encoding="utf-8").write(hdr + f"Present\t21\t{today}\tscripts/sweeps_due.py\tactive\t\tx\n"
                                                    f"Missing\t21\t{today}\tsweeps/NO_SUCH_PLAYBOOK.md\tactive\t\tx\n")
        p = subprocess.run([sys.executable, os.path.abspath(__file__), "--registry", reg, "--no-profile-clock", "--no-live-checks"],
                           capture_output=True, text=True)
        fire = p.returncode == 2 and "PLAYBOOK MISSING" in p.stdout and "Missing" in p.stdout and "Present" not in p.stdout.split("PLAYBOOK MISSING")[1].split("\n")[0]
        print(f"  {'✓' if fire else '✗'} missing playbook ⇒ rc 2 + PLAYBOOK MISSING names the row (rc={p.returncode})"); fails += not fire
        open(reg, "w", encoding="utf-8").write(hdr + f"Present\t21\t{today}\tscripts/sweeps_due.py\tactive\t\tx\n"
                                                    f"PresentRepoRel\t21\t{today}\tscripts/claim_check.py\tactive\t\tx\n")
        p = subprocess.run([sys.executable, os.path.abspath(__file__), "--registry", reg, "--no-profile-clock", "--no-live-checks"],
                           capture_output=True, text=True)
        clean = p.returncode == 0 and "PLAYBOOK MISSING" not in p.stdout
        print(f"  {'✓' if clean else '✗'} present playbook ⇒ clean, rc 0 (rc={p.returncode})"); fails += not clean
    dated_ok = selftest_dated(today_et())
    fails += not dated_ok
    print("sweeps_due SELFTEST " + ("✓ 5/5" if not fails else f"✗ {fails}/5 FAILED"))
    return 1 if fails else 0


def main():
    global REGISTRY
    if "--selftest" in sys.argv:
        return selftest()
    if "--registry" in sys.argv:
        REGISTRY = sys.argv[sys.argv.index("--registry") + 1]
    no_pc = "--no-profile-clock" in sys.argv
    today = today_et()
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
                # DATED (2026-09-04): a one-shot sweep whose contract is its resolve_by date, not a
                # cadence. The Wiring Sweep row carried cadence_days=7 as a declared PLACEHOLDER "so
                # sweeps_due can see it" and fired ⏰ DUE at every boot 7d after its last run while its
                # real date (resolve_by 9/14) sat ten days out — a false DUE that I reported to Will at
                # boot as a distinct weekly sweep. A placeholder number is a claim the tool cannot tell
                # from a real one; the token makes the contract machine-readable and the resolve_by
                # branch below carries the whole clock. A DATED row with NO resolve_by is un-parseable.
                cad_raw = (row.get("cadence_days") or "").strip()
                if cad_raw.upper() == "DATED":
                    if not (row.get("resolve_by") or "").strip():
                        skipped.append(task + " [DATED row without resolve_by]")
                        continue
                    tracked += 1
                    cad = None
                    pb_path = (row.get("playbook") or "").strip()
                    if pb_path and not playbook_exists(pb_path):
                        missing_pb.append((task, pb_path))
                else:
                    try:
                        last = datetime.date.fromisoformat((row.get("last_run") or "").strip())
                        cad = int(cad_raw)
                    except (ValueError, TypeError):
                        skipped.append(task)
                        continue
                    tracked += 1
                if cad is not None:
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

    # --no-live-checks (2026-09-17): the selftests drill REGISTRY logic on a temp registry; the two
    # live-surface checks (own FLEET_MAP row age, directory staleness) read the real tree and had the
    # selftest failing 2/5 whenever the self-row was stale — a regression test pinned to a live surface.
    no_live = "--no-live-checks" in sys.argv
    self_row = None if no_live else check_self_row(today)
    dir_stale = None if no_live else check_directory_stale(today)
    if dir_stale and dir_stale.startswith("CANNOT-CERTIFY"):
        print(f"🔴 sweeps_due {dir_stale}")
        cannot_certify = True
        dir_stale = None
    if self_row and self_row.startswith("CANNOT-CERTIFY"):
        print(f"🔴 sweeps_due {self_row}")
        cannot_certify = True
        self_row = None

    if overdue:
        for task, over, rb, pb in sorted(overdue, key=lambda r: r[1], reverse=True):
            if over == 0:
                print(f"⏰ DUE TODAY: {task} — dated obligation {rb} (Eastern date; no intraday deadline specified) → {pb}")
            else:
                print(f"🔴 RESOLVE_BY PASSED: {task} — dated obligation {rb} is {over}d past "
                      f"(this is NOT a cadence miss; the cadence clock may be perfectly fine) → {pb}")
    if due:
        for task, age, cad, pb in sorted(due, key=lambda r: r[1] - r[2], reverse=True):
            print(f"⏰ DUE: {task} — last run {age}d ago (cadence {cad}d, +{age - cad}d over) → {pb}")
    if self_row:
        print(self_row)
    if dir_stale:
        print(dir_stale)
        self_row = self_row or dir_stale   # a stale boot read is a dated obligation → rc 1 below
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
