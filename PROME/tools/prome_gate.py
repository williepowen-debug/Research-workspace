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
# GATES_AGE_DAYS retired 8/9 — the >5d raw-age rule was RETIRED by the 8/7
# consumed_by ruling (forum S2/ABN, Will-adopted); staleness keys on consumed_by.
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
        if state.startswith("LIVE"):
            # consumed_by discipline (forum S2/ABN ruling 8/7, Will-adopted; check
            # re-keyed 8/9 — spine-audit #8 found the ruling propagated to none of
            # its three surfaces): staleness keys on the consumed_by field, NOT raw
            # last_checked age (that >5d rule is RETIRED — it over-reported by design;
            # a LIVE row with a future consumer or PRICE:/EVENT:/NONE is quiet).
            cb = r[8] if len(r) > 8 else ""
            m = re.match(r"(\d{4}-\d{2}-\d{2})", cb)
            if m and dt.date.fromisoformat(m.group(1)) < today:
                stale_live.append(f"{gate} consumer-date {m.group(1)} passed")
            elif not cb.strip():
                stale_live.append(f"{gate} consumed_by EMPTY (required since 8/7)")
    record(BLOCK, "GATES fired-unexecuted", not fired,
           "; ".join(fired) or "none", "PROME/GATES.tsv (clear or escalate SAME session)")
    record(BLOCK, "GATES token vocabulary", not bad_tokens,
           "; ".join(bad_tokens) or f"{len(rows)} rows all lead with enumerated tokens",
           "PROME/GATES.tsv header STATES line")
    record(ADVISE, "GATES consumed_by (consumer passed / cell empty)", not stale_live,
           "; ".join(stale_live) or "all LIVE rows have live consumers or declared NONE",
           "PROME/GATES.tsv (resolve at the consumer, re-date, or declare NONE)")


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
           # ⚠️ 2026-08-08: truncation must ANNOUNCE itself. The 8/3 audit found this
           # check's column-scan bug AND named its 4-item display cap as the mechanism
           # that let false positives crowd out 4 real rows — only the column half was
           # fixed. A silent cap reads as "that's all of them."
           # [[finding_display_filter_gating_safety_net]]
           "; ".join(overdue[:4]) +
           (f" (+{len(overdue)-4} more)" if len(overdue) > 4 else "")
           or "every past-dated PENDING row carries an OVERDUE annotation",
           "PROME/DOCKET.tsv (grade, re-date, or annotate OVERDUE + owner)")


def check_docket_today():
    """CLOSEOUT-ONLY, BLOCKING: PENDING rows landing TODAY, undispositioned.

    WHY (2026-08-03, the leg-(b) routing gap): PROME closed out at 11:10 with
    its own SCRATCH saying "THE ONE THING THAT MATTERS TODAY: BRENT deploy-gate
    leg (a) grades at the 16:00 close" — and PROME was the sole routing path
    between BRENT and TERRY. BRENT's request landed 11:45 and Will's tenor +
    size rulings 12:50, into an inbox nobody was reading. TERRY never got the
    size ruling and logged the item NOT DONE at its own 15:12 closeout.

    Nothing existing could catch it. check_docket_overdue() scans only PAST
    dates; GATES fired-unexecuted needs a gate to have already FIRED; an
    inbox check would have passed (inbox was 0 at 11:10 — the packets had not
    been sent yet). The missing question is the simple one: *is anything
    landing today, and does it need me after I go dark?*

    Cleared the same way overdue rows are — annotate the row. A row is
    dispositioned if its STATUS or NOTES carries COVERED (name who has it), or
    if it has already left PENDING. Deliberately BLOCKING, not advisory: the
    whole failure mode is a true line nobody read. Cheap to satisfy, impossible
    to skip. [[finding_mechanize_the_cap_not_the_ritual]]
    """
    path = ROOT / "PROME/DOCKET.tsv"
    today = dt.date.today().isoformat()
    undispositioned = []
    with open(path, encoding="utf-8") as f:
        for r in csv.reader(f, delimiter="\t"):
            if not r or r[0].startswith("#") or len(r) < 4:
                continue
            if r[3].split("(")[0] != "PENDING":
                continue
            # A row lands today if it is dated today, or is a range spanning it.
            start, end = r[0].split("..")[0], r[0].split("..")[-1]
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", end):
                continue
            if not (start <= today <= end):
                continue
            if "COVERED" in (r[3] + " " + (r[5] if len(r) > 5 else "")):
                continue
            owner = r[2][:28] if len(r) > 2 else "?"
            undispositioned.append(f"{r[1][:44]} [{owner}]")
    record(BLOCK, "DOCKET lands-today dispositioned", not undispositioned,
           "; ".join(undispositioned[:5]) +
           (f" (+{len(undispositioned)-5} more)" if len(undispositioned) > 5 else "")
           or "nothing PENDING lands today",
           "PROME/DOCKET.tsv — for EACH: grade it, or annotate COVERED:<who holds it "
           "after you go dark>. A row whose owner is PROME and that is still PENDING at "
           "closeout is the routing-gap class: say who covers it or do it now.")


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
    # roll always safe).
    def _mmdd(cell):
        m2 = re.search(r"(\d{1,2})/(\d{1,2})", cell)
        if not m2:
            return None
        try:
            d0 = dt.date(today.year, int(m2.group(1)), int(m2.group(2)))
        except ValueError:
            return None
        # Year-roll, BACKWARD ONLY (8/16 rider, deviation from firetime's ±183
        # stated in the write-back): Since/Done cells are PAST-only, so a parse
        # >183d in the future is last year's date (a `12/20` read in January —
        # the false-negative direction the old "revisit in Dec" comment
        # under-scoped). Rolling >183d-past dates FORWARD (firetime's other
        # half) would instead make ancient rows read as future and silence
        # AGING/roll-off — the same false-negative this rider exists to kill.
        if (d0 - today).days > 183:
            try:
                d0 = d0.replace(year=today.year - 1)
            except ValueError:
                pass
        return d0

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
            # MISFILED (8/16, DAEDALUS spec off PROME's queue-look defect
            # report; ruling trail in the two packets): close-in-place is a
            # silent middle state between OPEN and RECENTLY DONE — measured
            # live 8/16 at ~15 of 25 rows, printing a false 25>20 over-cap
            # and a false AGING-47d on a RESOLVED row. A terminal marker
            # LEADING the Item cell (anchored after strikethrough/bold strip,
            # never substring — "blocked until X is RESOLVED" must not match)
            # flags the row-move; excluded from actionable + AGING at once so
            # the count is honest even before the move. Roll-off applies
            # normally once moved — the MISFILED line IS the action.
            item = re.sub(r"^(?:~~[^~]+~~\s*)+", "", cells[1])
            item = re.sub(r"^[\*\s]+", "", item)
            if re.match(r"✅|DONE\b|RESOLVED\b|TERMINAL\b|DECLINED\b", item):
                problems.append(
                    f"MISFILED #{cells[0]} {cells[1][:30]} "
                    "(closed-in-place in OPEN — move to RECENTLY DONE)")
                continue
            d = re.search(r"\d{4}-\d{2}-\d{2}", cells[3])
            if d:
                dd = dt.date.fromisoformat(d.group(0))
                if dd == today:
                    problems.append(f"DUE TODAY #{cells[0]} {cells[1][:36]}")
                elif dd < today:
                    problems.append(f"PASSED #{cells[0]} {cells[1][:36]} (needed {d.group(0)})")
                if not blocked:
                    actionable += 1
            # `^\d` not .isdigit() (8/16, landed WITH the F2 ruling by design —
            # sequenced on the record in the MISFILED write-back): lettered row
            # IDs (32a, 36b…) failed .isdigit() and silently escaped BOTH the
            # actionable count and the 21d age-trip. Post-F2 the escape class
            # is mostly moved out anyway; this closes the hole for the future.
            elif not blocked and re.match(r"\d", cells[0]):
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
           # ⚠️ 2026-08-08: same silent-cap class as check_docket_overdue above —
           # measured live at this boot, 14 roll-off-eligible rows displayed as 4.
           "; ".join(problems[:5]) +
           (f" (+{len(problems)-5} more)" if len(problems) > 5 else "")
           or "stamp current; nothing due today, passed, aging, misfiled, or overdue for roll-off",
           "PROME/WILL_QUEUE.md (act on DUE TODAY; reconcile PASSED; date/decline AGING)")


def check_heartbeat_chain():
    """HEARTBEAT amendment-chain length vs the ~5 re-base rule (Cadence section).
    The rule lived in prose on 5+ surfaces and in no script until 2026-07-30
    (DAEDALUS FORGE-audit follow-up, gap (a)) — it held at chain=4 on memory,
    twice. Advisory: warn at 4 (plan the re-base), and at >=5 the rule's own
    trip has occurred. [[finding_mechanize_the_cap_not_the_ritual]]

    ⚠️ 2026-08-04 REPAIR — this check was BLIND from the 7/31 re-base until now.
    v1 matched only `> ## AMENDMENT #N`; the 7/31 re-base changed the house style
    to `> **AMENDMENT #N`, so it counted ZERO against a header that declared
    "Chain: 2" and printed a confident ✅ PASS. A heading-format change silently
    disarmed the one mechanism enforcing the re-base rule.

    Two fixes, because swapping the regex alone would just re-arm the same trap
    the next time the style moves:
      (a) match either style (and any future `#`-heading depth);
      (b) CROSS-CHECK the count against the header's own self-declared
          "Chain: N". The file states the answer in prose; v1 never read it.
          Disagreement is not resolvable from inside this check, so it reports
          UNVERIFIABLE and trips on max(counted, declared) — fail-loud, never a
          confident number it cannot stand behind.
    [[finding_test_the_guard_not_just_the_guarded]] · the "return a confident
    answer where 'cannot evaluate' is the honest one" class (PROME 2026-08-04)."""
    path = ROOT / "HEARTBEAT.md"
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        record(ADVISE, "HEARTBEAT chain length", False, f"unreadable: {e}", "HEARTBEAT.md")
        return
    # Either heading style: "> ## AMENDMENT #1 —" (pre-7/31) or "> **AMENDMENT #1 —" (current).
    counted = len(re.findall(r"^>\s*(?:#{1,6}\s*|\*\*)?AMENDMENT\s*#\d+", text, re.M))
    # The header states the chain in prose: "... Chain: 2." — v1's missing positive check.
    m = re.search(r"^\*\*Amendments append.*?Chain:\s*(\d+)", text, re.M)
    declared = int(m.group(1)) if m else None

    src = "HEARTBEAT.md Cadence section (re-base = draft -> Will approval -> archive verbatim)"
    if declared is not None and declared != counted:
        record(ADVISE, "HEARTBEAT amendment chain (<4)", False,
               f"UNVERIFIABLE — counted {counted} amendment block(s) but the header declares "
               f"Chain: {declared}. One of them is wrong and this check cannot say which: "
               f"either the header is stale or the block format moved again. Tripping on the "
               f"larger ({max(counted, declared)}) so the re-base rule fails LOUD, not silent",
               src + " · reconcile the header stamp against the blocks before trusting either")
        return

    n = counted
    ok = n < 4
    detail = (f"chain at {n} amendment(s)"
              + ("" if declared is None else " (header-declared count agrees)")
              + ("" if ok else " — re-base rule trips at ~5: plan it into the next substantive session"
                 if n == 4 else " — the ~5 trip HAS OCCURRED: re-base (draft->Will->archive-verbatim) is due"))
    record(ADVISE, "HEARTBEAT amendment chain (<4)", ok, detail, src)


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
    # PAT-105 content assertions (8/16, DAEDALUS sweep-1 guard rec, Will "go"):
    # nonemptiness certifies presence, not truth — every live Will-facing
    # failure this window was NONEMPTY (the one-liner rendered "SPENT", a
    # kill-on-sight token). Four cheap truth checks, advisory tier:
    bad = []
    one = (s.get("one") or "").strip().strip('"“”')
    hb_text = ""
    try:
        hb_text = (ROOT / "HEARTBEAT.md").read_text(errors="ignore")
    except OSError:
        pass
    kill_line = next((ln for ln in hb_text.splitlines()
                      if "kill-on-sight" in ln), "")
    if len(one) < 40:
        bad.append(f"one-liner suspiciously short ({len(one)} chars) — token-capture class")
    elif kill_line and one[:60] in kill_line:
        bad.append("one-liner text appears on HEARTBEAT's own kill-on-sight line")
    if not (s.get("split") or "").strip():
        bad.append("NEXUS split EMPTY (separator-drift class, blank 17d once)")
    if len(s.get("levels") or {}) < 6:
        bad.append(f"only {len(s.get('levels') or {})} gate tiles (<6 floor — "
                   "token-rename attrition class, 13→4 once)")
    try:
        import agent_freshness
        wrong = [n for n, cls in (s.get("fleet") or {}).items()
                 if cls == "ok" and n != "PROME"
                 and (agent_freshness.own_surface_age_days(n) or 0) > 7]
        if wrong:
            bad.append("fleet grid says ok but own-surface age >7d: " + ", ".join(wrong))
    except Exception as e:
        bad.append(f"grid-agreement check unavailable ({type(e).__name__})")
    record(ADVISE, "dashboard content assertions (PAT-105)", not bad,
           "; ".join(bad) or "one-liner sane · split populated · tile floor met · grid agrees with freshness",
           "PROME/tools/fleet_dashboard.py (rebuild + fix the parser, never the state file)")


def check_symmetry():
    """T2-c: a boot-read surface isn't wired until its CLOSEOUT symmetry row
    exists (paired-write or explicitly one-way). BOOT absorbed 4 gates in 48h
    the table never learned about — growth must register at the slow surface."""
    boot = (ROOT / "PROME/BOOT.md").read_text(errors="ignore")
    close = (ROOT / "PROME/CLOSEOUT.md").read_text(errors="ignore")
    seq = boot.split("## Boot Sequence", 1)[-1].split("## Conditional Modules")[0]
    # T2-c v1 (DAEDALUS ruling 7/28, shipped 8/9): harvest ONLY lines carrying an
    # explicit `Read` directive (case-sensitive word). Mention-harvesting registered
    # pointers and even retirement notices as reads (the TODAY.md phantom class).
    # Contract: a mandatory boot read carries the word "Read" on its line in BOOT.md.
    boot_reads = set()
    for ln in seq.splitlines():
        if re.search(r"\bRead\b", ln):
            boot_reads.update(re.findall(r"`((?:PROME/)?[A-Z][A-Za-z_]+\.(?:md|tsv))`", ln))
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
    # 8/14 Will-directed: agent staleness reads come from ground truth, not narrative.
    # rc=1 = unread from-agent packets sit in PROME/inbox — PROME's model of those
    # agents is stale regardless of what SCRATCH's spawn-queue prose says.
    run_script(ADVISE, "agent freshness (ground-truth vs narrative)", [sys.executable,
               "PROME/tools/agent_freshness.py", "--gate"],
               "run agent_freshness.py --agent <NAME> before ANY launch brief; drain first")
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
    check_docket_today()       # the pre-fire analogue: don't go dark before today's items
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
    # 8/16 (RAV addition, Will-approved): the two WILL_QUEUE parsers duplicate
    # their visibility regexes by design — this synthetic-row test is what
    # keeps them agreeing (the lettered-ID fix shipped to the gate only and
    # the brief silently diverged; this would have caught it same-day).
    run_script(ADVISE, "queue-parser selftest (gate vs will_brief)",
               [sys.executable, "PROME/tools/queue_parser_selftest.py"],
               "PROME/tools/queue_parser_selftest.py")


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
