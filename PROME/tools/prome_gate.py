#!/usr/bin/env python3
"""
prome_gate.py — PROME's boot/closeout gate: every mechanical check, one verdict block.

WHY (DAEDALUS T2-b, Will-approved 2026-07-28): PROME's protocol mass exceeded
single-session execution capacity — root steps 1c/1d were adopted the same
morning a closeout shipped malformed allowlist rows. Checks kept landing in
PROSE, which competes for session attention; this script is where they land
instead. NEW FLEET-WIDE CHECKS GET ADDED HERE, NOT TO BOOT/CLOSEOUT PROSE.
Precedent: HENRY/LABOR boot.py.

DESIGN CONSTRAINTS (Will-approved, in the 7/28 disposition packet):
  1. ADVISORY vs BLOCKING classes are PRESERVED, never flattened. orphan_check
     and consumer_check are advisory BY DESIGN; flattening everything into one
     FAIL trains alarm fatigue — the disease this program treats. rc=1 only on
     BLOCKING failures.
  2. Every wrapped check stays INDEPENDENTLY RUNNABLE — this is a thin shell
     dispatcher, not a monolith. Each failure prints the owner doc to read.
  3. The T3-a MECHANICAL CORE lives here (dashboard-state emptiness/vintage,
     GATES token vocabulary + ages, DOCKET overdue rows, boot↔closeout symmetry
     diff) so scriptable checks run EVERY BOOT — DAEDALUS's ~21d external sweep
     keeps only the judgment tail a script cannot do.

USAGE
  python3 PROME/tools/prome_gate.py boot        # BOOT.md step-0/3/5 mechanical stack
  python3 PROME/tools/prome_gate.py closeout    # closeout-tail mechanical stack
  (always from repo root: cd "$(git rev-parse --show-toplevel)" first — PAT-031)

rc=0 all blocking gates pass (advisories may still print — read them);
rc=1 at least one BLOCKING gate failed — disposition before proceeding.

MANUAL-JUDGMENT STEPS THIS SCRIPT DOES NOT REPLACE (closeout): memory_index_check
--slug (needs the session's slugs) · consumer_check --old/--new (needs the
superseded values) · the HANDOFF/SCRATCH judgment writes. It prints reminders.
"""
import argparse
import csv
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

GATES_STATES = ("LIVE", "FIRED-UNEXECUTED", "RESOLVED", "LAPSED", "RETIRED")
GATES_AGE_DAYS = 5          # BOOT step-3 rule: LIVE row last_checked >5d → refresh/flag
DASH_STALE_HOURS = 72       # dashboard self-declares red past this

BLOCK, ADVISE = "BLOCKING", "advisory"
results = []                # (severity, name, ok, detail, owner_doc)


def record(severity, name, ok, detail, owner):
    results.append((severity, name, ok, detail, owner))


def run_script(severity, name, cmd, owner, ok_rc=(0,)):
    """Shell out to an independently-runnable check; capture rc + tail."""
    try:
        p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=120)
        ok = p.returncode in ok_rc
        tail = (p.stdout + p.stderr).strip().split("\n")
        detail = f"rc={p.returncode}" + ("" if ok else f" · {tail[-1][:110]}" if tail else "")
    except Exception as e:
        ok, detail = False, f"{type(e).__name__}: {str(e)[:100]}"
    record(severity, name, ok, detail, owner)
    return ok


# ---------------------------------------------------------- T3-a mechanical core

def check_gates_tsv():
    """Token vocabulary + FIRED-UNEXECUTED + LIVE ages. The silent-blank class
    (bare-date cells 7/28, bare ARMED 7/28, SAM-30 7/11) becomes impossible to
    miss: a state cell not LEADING with an enumerated token is a BLOCKING fail."""
    path = ROOT / "PROME/GATES.tsv"
    today = dt.date.today()
    bad_tokens, fired, stale_live = [], [], []
    with open(path, encoding="utf-8") as f:
        rows = [r for r in csv.reader(f, delimiter="\t")
                if r and not r[0].startswith("#") and r[0] != "gate_id"]
    for r in rows:
        gate, state = r[0], (r[5] if len(r) > 5 else "")
        lead = state.split(" ")[0].split("(")[0].strip()
        if not any(state.startswith(t) for t in GATES_STATES):
            bad_tokens.append(f"{gate} leads '{lead[:20]}'")
        if state.startswith("FIRED-UNEXECUTED"):
            fired.append(gate)
        if state.startswith("LIVE") and len(r) > 6:
            m = re.match(r"(\d{4}-\d{2}-\d{2})", r[6])
            if m:
                age = (today - dt.date.fromisoformat(m.group(1))).days
                if age > GATES_AGE_DAYS:
                    stale_live.append(f"{gate} {age}d")
    record(BLOCK, "GATES fired-unexecuted", not fired,
           "; ".join(fired) or "none", "PROME/GATES.tsv (clear or escalate SAME session)")
    record(BLOCK, "GATES token vocabulary", not bad_tokens,
           "; ".join(bad_tokens) or f"{len(rows)} rows all lead with enumerated tokens",
           "PROME/GATES.tsv header STATES line")
    record(ADVISE, f"GATES live-row age ≤{GATES_AGE_DAYS}d", not stale_live,
           "; ".join(stale_live) or "all fresh", "PROME/GATES.tsv (refresh or flag owner)")


def check_docket_overdue():
    """PENDING rows whose (end-)date has passed — the row-56 ballot-cert class."""
    path = ROOT / "PROME/DOCKET.tsv"
    today = dt.date.today().isoformat()
    overdue = []
    with open(path, encoding="utf-8") as f:
        for r in csv.reader(f, delimiter="\t"):
            if not r or r[0].startswith("#") or len(r) < 4 or r[3].split("(")[0] != "PENDING":
                continue
            end = r[0].split("..")[-1]
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", end) and end < today:
                # The annotation lives in STATUS — PENDING(OVERDUE-annotated …) — or in
                # NOTES; practice has used both (4 rows vs 2 on 2026-08-03). Scanning only
                # NOTES made every status-annotated row read as unannotated, so the check
                # reported work that was already done and hid the rows that weren't.
                annotation = r[3] + " " + (r[5] if len(r) > 5 else "")
                if "OVERDUE" not in annotation:
                    overdue.append(f"{r[0]} {r[1][:40]}")
    record(ADVISE, "DOCKET overdue-unannotated", not overdue,
           "; ".join(overdue[:4]) or "every past-dated PENDING row carries an OVERDUE annotation",
           "PROME/DOCKET.tsv (grade, re-date, or annotate OVERDUE + owner)")


def check_will_queue():
    """WILL_QUEUE.md — passed needed-by dates on OPEN rows + stale reconcile stamp.
    Born 2026-07-30 (Will-directed): the operator queue decays like any surface,
    and both failure directions are costly — DONE-reads-OPEN nags Will, OPEN-
    reads-DONE silently drops his decision. Flags only what a script can see:
    ISO dates in the Needed-by column and the content-vintage stamp
    (finding_hygiene_commit_rearms_the_staleness_lie — never key on mtime)."""
    path = ROOT / "PROME/WILL_QUEUE.md"
    if not path.exists():
        record(ADVISE, "WILL_QUEUE present", False, "PROME/WILL_QUEUE.md missing",
               "PROME/WILL_QUEUE.md")
        return
    text = path.read_text(encoding="utf-8")
    today = dt.date.today()
    m = re.search(r"^\*\*Last reconciled:\*\*\s*(\d{4}-\d{2}-\d{2})", text, re.M)
    problems = []
    if not m:
        problems.append("no 'Last reconciled: YYYY-MM-DD' stamp")
    else:
        age = (today - dt.date.fromisoformat(m.group(1))).days
        if age > 2:
            problems.append(f"reconcile stamp {m.group(1)} is {age}d old")
    # DAEDALUS W1 (7/30 review): `<` shipped first and printed a green tick while
    # two rows were due THAT NIGHT — a due-today row must flag as DUE TODAY (act
    # now), distinct from PASSED (reconcile). W2: cap counts only ACTIONABLE rows
    # (dated + unblocked); undated unblocked rows age-trip at 21d instead. W5:
    # DONE rows past the ~7d window flag for roll-off (anchor-at-write makes the
    # roll always safe). m/d parses assume the current year — v1, revisit in Dec.
    def _mmdd(cell):
        m2 = re.search(r"(\d{1,2})/(\d{1,2})", cell)
        if not m2:
            return None
        try:
            return dt.date(today.year, int(m2.group(1)), int(m2.group(2)))
        except ValueError:
            return None

    section, actionable = None, 0
    for line in text.splitlines():
        if line.startswith("## "):
            section = "open" if line.startswith("## OPEN") else (
                "done" if line.startswith("## RECENTLY DONE") else None)
            continue
        if not (section and line.startswith("|")):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if section == "open" and len(cells) >= 7:
            blocked = "⛔" in line
            d = re.search(r"\d{4}-\d{2}-\d{2}", cells[3])
            if d:
                dd = dt.date.fromisoformat(d.group(0))
                if dd == today:
                    problems.append(f"DUE TODAY #{cells[0]} {cells[1][:36]}")
                elif dd < today:
                    problems.append(f"PASSED #{cells[0]} {cells[1][:36]} (needed {d.group(0)})")
                if not blocked:
                    actionable += 1
            elif not blocked and cells[0].isdigit():
                actionable += 1
                s = _mmdd(cells[4])
                if s and (today - s).days > 21:
                    problems.append(f"AGING #{cells[0]} {cells[1][:30]} (undated, open {(today - s).days}d)")
        elif section == "done" and len(cells) >= 3 and cells[0] != "Item":
            dn = _mmdd(cells[1])
            if dn and (today - dn).days > 7:
                problems.append(f"ROLL-OFF {cells[0][:30]} (done {(today - dn).days}d ago)")
    if actionable > 20:
        problems.append(f"CAP: {actionable} actionable rows (>20) — PROME over-routing")
    record(ADVISE, "WILL_QUEUE fresh + nothing due/passed/aging", not problems,
           "; ".join(problems[:5]) or "stamp current; nothing due today, passed, aging, or overdue for roll-off",
           "PROME/WILL_QUEUE.md (act on DUE TODAY; reconcile PASSED; date/decline AGING)")


def check_heartbeat_chain():
    """HEARTBEAT amendment-chain length vs the ~5 re-base rule (Cadence section).
    The rule lived in prose on 5+ surfaces and in no script until 2026-07-30
    (DAEDALUS FORGE-audit follow-up, gap (a)) — it held at chain=4 on memory,
    twice. Advisory: warn at 4 (plan the re-base), and at >=5 the rule's own
    trip has occurred. [[finding_mechanize_the_cap_not_the_ritual]]"""
    path = ROOT / "HEARTBEAT.md"
    try:
        n = len(re.findall(r"^> ## AMENDMENT #\d+", path.read_text(encoding="utf-8"), re.M))
    except Exception as e:
        record(ADVISE, "HEARTBEAT chain length", False, f"unreadable: {e}", "HEARTBEAT.md")
        return
    ok = n < 4
    detail = (f"chain at {n} amendment(s)" +
              ("" if ok else " — re-base rule trips at ~5: plan it into the next substantive session"
               if n == 4 else " — the ~5 trip HAS OCCURRED: re-base (draft->Will->archive-verbatim) is due"))
    record(ADVISE, "HEARTBEAT amendment chain (<4)", ok, detail,
           "HEARTBEAT.md Cadence section (re-base = draft -> Will approval -> archive verbatim)")


def check_dashboard_state():
    """The publisher's own blank panels — the 4-day silent regression class.
    BLOCKING on emptiness (a degraded Will-facing page), advisory on vintage."""
    path = ROOT / "PROME/tools/dashboard_state.json"
    try:
        s = json.loads(path.read_text())
    except Exception as e:
        record(BLOCK, "dashboard panels nonempty", False, f"state unreadable: {e}",
               "PROME/tools/fleet_dashboard.py")
        return
    empty = [k for k, v in (("one-liner", s.get("one")), ("channels", s.get("channels")),
                            ("levels", s.get("levels"))) if not v]
    record(BLOCK, "dashboard panels nonempty", not empty,
           ("EMPTY: " + ", ".join(empty)) if empty else "one-liner/channels/levels populated",
           "PROME/tools/fleet_dashboard.py (rebuild; if still empty a parser broke — PAT-069)")
    built = s.get("built", "")
    try:
        age_h = (dt.datetime.now() - dt.datetime.strptime(built, "%Y-%m-%d %H:%M")).total_seconds() / 3600
        record(ADVISE, f"dashboard vintage ≤{DASH_STALE_HOURS}h", age_h <= DASH_STALE_HOURS,
               f"built {built} ({age_h:.0f}h ago)", "regenerate + republish to the RECORDED URL")
    except ValueError:
        record(ADVISE, "dashboard vintage", False, f"unparseable built stamp '{built}'",
               "PROME/tools/fleet_dashboard.py")


def check_symmetry():
    """T2-c: a boot-read surface isn't wired until its CLOSEOUT symmetry row
    exists (paired-write or explicitly one-way). BOOT absorbed 4 gates in 48h
    the table never learned about — growth must register at the slow surface."""
    boot = (ROOT / "PROME/BOOT.md").read_text(errors="ignore")
    close = (ROOT / "PROME/CLOSEOUT.md").read_text(errors="ignore")
    seq = boot.split("## Boot Sequence", 1)[-1].split("## Conditional Modules")[0]
    boot_reads = set(re.findall(r"`((?:PROME/)?[A-Z][A-Za-z_]+\.(?:md|tsv))`", seq))
    sym = close.split("## Boot↔Closeout symmetry", 1)[-1].split("\n## ", 1)[0]
    missing = sorted(s for s in boot_reads
                     if Path(s).name not in sym and s not in sym)
    record(ADVISE, "boot↔closeout symmetry", not missing,
           ("boot-reads with no symmetry row: " + ", ".join(missing)) if missing
           else f"{len(boot_reads)} boot-read surfaces all registered",
           "PROME/CLOSEOUT.md symmetry table (add paired-write row or declare one-way)")


# ----------------------------------------------------------------------- modes

def mode_boot():
    run_script(BLOCK, "env_doctor", [sys.executable, "scripts/env_doctor.py", "--quiet"],
               "PROME/MACHINE_LOCAL.md")
    run_script(BLOCK, "position_agreement", [sys.executable, "scripts/position_agreement_check.py",
               "--all", "--quiet"], "owner STATUS is canonical; fix the trade surface")
    run_script(BLOCK, "board_scan", [sys.executable, "PROME/tools/board_scan.py", "--advance"],
               "BOARD action line ⇒ disposition before proceeding (§3.5.4)")
    run_script(ADVISE, "firetime (owner-routed flags persist)", [sys.executable,
               "scripts/firetime_check.py", "--window", "7", "--quiet"],
               "scripts/firetime_allowlist.tsv · DATE flag = full logic re-read, never find-replace")
    check_gates_tsv()
    check_docket_overdue()
    check_will_queue()
    check_heartbeat_chain()
    check_dashboard_state()
    check_symmetry()


def mode_closeout():
    run_script(BLOCK, "position_agreement", [sys.executable, "scripts/position_agreement_check.py",
               "--all", "--quiet"], "owner STATUS is canonical")
    check_gates_tsv()          # FIRED-UNEXECUTED must never leave a session
    check_docket_overdue()
    check_will_queue()
    check_heartbeat_chain()    # the ~5-amendment re-base rule, mechanized (was prose-only on 5 surfaces)
    check_dashboard_state()    # Standard+ closeouts regenerate; this catches a skipped one
    run_script(ADVISE, "orphan_check (advisory by design)", ["bash", "scripts/orphan_check.sh", "PROME"],
               "[likely YOURS] = commit per carve-out ① · [not yours] = flag, never sweep")
    record(ADVISE, "MANUAL: memory_index_check", True,
           "if you wrote/edited an auto-memory: scripts/memory_index_check.py --strict --slug <name> (root step 1d)",
           "root CLAUDE.md carve-out ③")
    record(ADVISE, "MANUAL: consumer_check", True,
           "if you superseded a published number: scripts/consumer_check.py --old <v> --new <v> (root step 1c); "
           "canon/threshold change ⇒ add --mirror-map (T1-b)",
           "root CLAUDE.md step 1c + PROME/SYSTEM.md Mirror Map")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("mode", choices=["boot", "closeout"])
    args = ap.parse_args()

    (mode_boot if args.mode == "boot" else mode_closeout)()

    blocking_fail = [r for r in results if r[0] == BLOCK and not r[2]]
    print(f"\n{'='*70}\n  PROME GATE · {args.mode.upper()} · "
          f"{'🔴 BLOCKED' if blocking_fail else '✅ PASS'} "
          f"({sum(1 for r in results if r[0]==BLOCK)} blocking / "
          f"{sum(1 for r in results if r[0]==ADVISE)} advisory)\n{'='*70}")
    for sev, name, ok, detail, owner in results:
        mark = "✅" if ok else ("🔴" if sev == BLOCK else "⚠️ ")
        print(f"  {mark} [{sev:8}] {name}: {detail}")
        if not ok:
            print(f"       → {owner}")
    print(f"{'='*70}")
    if blocking_fail:
        print(f"  🔴 {len(blocking_fail)} BLOCKING gate(s) failed — disposition before new work.\n")
        return 1
    print("  ✅ all blocking gates pass — advisories above are judgment calls, read them.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
