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


def main():
    today = datetime.date.today()
    due, tracked, skipped = [], 0, []
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
    return 1 if (due or self_row) else 0


if __name__ == "__main__":
    sys.exit(main())
