#!/usr/bin/env python3
"""
VULCAN closeout check — ONE merged list of every closeout obligation (root CLAUDE.md
§ "At session end" + this desk's CLOSEOUT PROTOCOL), each tagged CHECKED / DELEGATED /
MANUAL. It runs what can be run and prints the MANUAL steps EVERY run.

WHY THIS EXISTS (2026-10-09, Will-directed after a self-review of that day's closeout)
-----------------------------------------------------------------------------------
That closeout ran every step on THIS desk's list and still skipped four obligations:
root 1c (consumers of the superseded 14/25 composite), step 2c (a DONE catalyst row left
in the register), step 4 (no lessons written), and step 4b (a Will ruling on the S5
threshold never reached CLAUDE.md's THRESHOLDS table). Three of the four lived in the GAP
between the two lists. Pattern borrowed, not invented:
  · SAM  `scripts/closeout_check.py` — merge both lists, tag each step's coverage.
  · HANS `scripts/closeout_check.py` — "a checklist with an item omitted does not look
    like a failure; it looks like a shorter checklist" ⇒ report WHICH steps ran.
  · VIOLET `scripts/closeout_guard.py` — BOOT WARNS, CLOSEOUT BLOCKS: a boot REVIEW flag
    that was read and not actioned is indistinguishable from no flag at all.

⛔ A PASS DOES NOT CERTIFY THE CLOSEOUT. It certifies that the mechanical steps ran and
what they returned. Whether STATUS says something TRUE, whether a THESIS reconcile was the
RIGHT reconcile, whether a lesson was worth writing — those are MANUAL by construction and
printed every run so they cannot be skipped silently.

SESSION BASE: the comparison point for "what changed this session" is the last commit
before 00:00 ET today (override with --base <sha>). Working-tree state is compared to it.

Usage:
  python3 AGENTS/VULCAN/tools/closeout_check.py            # run; exit 1 = LOOK
  python3 AGENTS/VULCAN/tools/closeout_check.py --list     # enumerate steps only
  python3 AGENTS/VULCAN/tools/closeout_check.py --base <sha>
  python3 AGENTS/VULCAN/tools/closeout_check.py --selftest # isolated fixtures
  python3 AGENTS/VULCAN/tools/closeout_check.py --reconciliation-key # read-only
Exit: 0 every CHECKED/DELEGATED step passed · 1 a step is FAIL or LOOK · 2 could not run.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, subprocess, sys, tempfile
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

DESK = Path(__file__).resolve().parent.parent
ROOT = DESK.parent.parent
REL = "AGENTS/VULCAN"
ET = ZoneInfo("America/New_York")
SHA = re.compile(r"\b(?=[0-9a-f]*[a-f])[0-9a-f]{7,12}\b")
STATUS_BUDGET = 32550


# ------------------------------------------------------------------ helpers
def git(*a, check=False):
    p = subprocess.run(["git", *a], cwd=str(ROOT), capture_output=True, text=True)
    if check and p.returncode:
        raise RuntimeError(f"git {' '.join(a)}: {p.stderr.strip()[:200]}")
    return p.stdout


def today_et():
    return datetime.now(ET).date()


def session_base(override=None):
    if override:
        return override
    midnight = datetime.combine(today_et(), datetime.min.time(), ET).isoformat()
    sha = git("rev-list", "-1", f"--before={midnight}", "HEAD").strip()
    if not sha:
        raise RuntimeError("no commit before today's midnight ET")
    return sha


def at_base(base, rel):
    return git("show", f"{base}:{REL}/{rel}")


def now_text(rel):
    p = DESK / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


def changed_since(base, rel):
    """Committed OR uncommitted change to the file since base."""
    return bool(git("diff", "--name-only", base, "--", f"{REL}/{rel}").strip())


def added_lines(base, rel):
    out = git("diff", "-U0", base, "--", f"{REL}/{rel}")
    return [l[1:] for l in out.splitlines() if l.startswith("+") and not l.startswith("+++")]


ANALYTICAL = {"STATUS": "STATUS.md", "THESIS": "THESIS.md", "EXIT": "workbook/EXIT_PROTOCOL.md"}
CONTINUITY = {"SCRATCH.md", "NEXUS_BRIEF.md"}


def reconciliation_scope(base, root=None):
    """Bind review to current changed contents, including untracked files/deletions.

    SCRATCH holds the stamp; NEXUS is separately checked and written last. Neither
    may be the sole home of substantive evidence. Ignored files are not records.
    Git failures raise rather than yielding an empty scope and a false pass.
    """
    root = ROOT if root is None else root

    def run(*args):
        return subprocess.run(["git", *args], cwd=root, capture_output=True,
                              check=True).stdout

    resolved = run("rev-parse", "--verify", f"{base}^{{commit}}").decode().strip()
    names = set(run("diff", "--no-renames", "--name-only", "-z", resolved, "--", REL).split(b"\0"))
    names.update(run("ls-files", "--others", "--exclude-standard", "-z", "--", REL).split(b"\0"))
    entries = []
    for raw in sorted(names - {b""}):
        name = os.fsdecode(raw)
        rel = str(Path(name).relative_to(REL))
        if rel in CONTINUITY:
            continue
        path = Path(root) / name
        if path.is_symlink():
            kind, content = "symlink", os.fsencode(os.readlink(path))
        elif path.is_file():
            kind, content = "file", path.read_bytes()
        elif not path.exists():
            kind, content = "deleted", b""
        else:
            raise RuntimeError(f"unsupported reconciliation path: {name}")
        entries.append((rel, kind, hashlib.sha256(content).hexdigest()))
    payload = json.dumps([resolved, entries], ensure_ascii=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest(), {e[0] for e in entries}


def reconciliation_errors(scratch, key, paths):
    """Require one reasoned disposition per analytical record in the TOP block."""
    top = re.split(r"^> # ⛔", scratch, flags=re.M)
    top = top[1] if len(top) > 1 else ""
    errors = []
    for label, path in ANALYTICAL.items():
        lines = re.findall(rf"^RECONCILE {key} {label} (UPDATED|UNCHANGED):[ \t]*(.*)$", top, re.M)
        if len(lines) != 1 or not lines[0][1].strip():
            errors.append(f"{label}: need one current-key disposition with a reason")
        elif lines[0][0] == "UPDATED" and path not in paths:
            errors.append(f"{label}: UPDATED but file does not differ from base")
    return errors


# ------------------------------------------------------- pure parsers (tested)
def parse_composite(status_text):
    """'**S1 3 · S2 2 · S3 3 · S4 3 · S5 4**' + 'Composite: 15/25' -> ({S1:3..}, '15/25')."""
    sc = dict(re.findall(r"\b(S[1-5]) ([1-5])\b(?= ·|\*\*)", status_text.split("## LIVE CHANNEL")[0]))
    m = re.search(r"Composite: (\d+/\d+)", status_text)
    return sc, (m.group(1) if m else None)


def fixed_without_sha(lines):
    """Lines that CLAIM a fix (FIXED/DONE as a verdict word) with no commit sha beside it."""
    out = []
    for l in lines:
        if re.search(r"\*\*(FIXED|DONE)\b|\b(FIXED|DONE)\*\*", l) and not SHA.search(l):
            out.append(l.strip()[:140])
    return out


def prestated_without_public(lines):
    """A 'pre-stated / pre-registered before the outcome' claim must carry the event's
    FIRST PUBLIC time (or 'public: none found'), not just the writing time [L-43]."""
    out = []
    for l in lines:
        if re.search(r"pre-?(stated|registered|committed)", l, re.I) and \
           re.search(r"before (the|any) (outcome|reading|event|print)", l, re.I) and \
           not re.search(r"public", l, re.I):
            out.append(l.strip())   # FULL line: the caller matches the clause against base
    return out


def past_catalyst_rows(tsv_text, today):
    rows = []
    for line in tsv_text.splitlines()[1:]:
        f = line.split("\t")
        try:
            d = date.fromisoformat(f[0].strip()[:10])
        except ValueError:
            continue
        if d < today:
            rows.append(f"{f[0][:10]} {f[1][:60]}")
    return rows


def deferral_covers(status_text, needle, today):
    """True if STATUS names `needle` on a line with 'DEFERRED to YYYY-MM-DD' (date >= today)."""
    for l in status_text.splitlines():
        if needle in l:
            for m in re.finditer(r"DEFERRED to (\d{4}-\d{2}-\d{2})", l):
                if date.fromisoformat(m.group(1)) >= today:
                    return True
    return False


# ----------------------------------------------------------------- the steps
RESULTS = []


def rec(step, src, verdict, detail=""):
    RESULTS.append((step, src, verdict, detail))


def run_cmd(cmd):
    p = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def checks(base):
    t = today_et()
    st_now, st_base = now_text("STATUS.md"), at_base(base, "STATUS.md")
    sc_now, comp_now = parse_composite(st_now)
    sc_base, comp_base = parse_composite(st_base)
    if len(sc_now) != 5:
        rec("1", "desk", "FAIL", f"could not parse 5 channel scores from STATUS composite line (got {sc_now})")
    key, paths = reconciliation_scope(base)
    errors = reconciliation_errors(now_text("SCRATCH.md"), key, paths)
    reconciled = not errors
    rec("1 analytical records reconciled to current contents", "desk",
        "PASS" if reconciled else "FAIL",
        "STATUS / THESIS / EXIT explicitly reconciled; judgment remains manual" if reconciled
        else "; ".join(errors) + f"; key {key}")
    sz = len(st_now.encode())
    over = sz > 0.85 * STATUS_BUDGET
    dfr = over and deferral_covers(st_now, "STATUS read-cap", t)
    hard = sz > STATUS_BUDGET            # over budget: a deferral never covers this
    rec("1 STATUS read-cap headroom", "root Data Hygiene",
        "FAIL" if hard else ("LOOK" if over and not dfr else "PASS"),
        f"{sz:,} B = {100*sz/STATUS_BUDGET:.0f}% of the {STATUS_BUDGET:,} B budget"
        + (" — rotation DEFERRED with a date in STATUS" if dfr and not hard else " (rotate before 100%)"))

    # 2 workbook (validator)
    rc, out = run_cmd([sys.executable, str(DESK / "scripts" / "validate_workbook.py")])
    rec("2 workbook schema + score reconcile", "desk", "PASS" if rc == 0 else "FAIL",
        "validate_workbook.py rc 0" if rc == 0 else out.strip().splitlines()[-1][:120])

    # A score move still needs semantic THESIS review; a cosmetic edit proves nothing.
    moved = {k: (sc_base.get(k), v) for k, v in sc_now.items() if sc_base.get(k) != v}
    rec("2b THESIS reconciled for moved scores", "desk",
        ("MANUAL" if reconciled else "FAIL") if moved else "N/A",
        f"moved {moved}; verify State cells, resolved gates and baselines" if moved else "no channel score moved")

    # 2c register: no past-dated rows left
    past = past_catalyst_rows(now_text("docket/CATALYSTS.tsv"), t)
    rec("2c CATALYSTS past rows archived", "desk", "PASS" if not past else "FAIL",
        "none" if not past else f"{len(past)} past-dated row(s) still live: " + " | ".join(past[:4]))
    # 2c mirror
    if changed_since(base, "docket/CATALYSTS.tsv"):
        ok = changed_since(base, "NEXUS_BRIEF.md")
        rec("2c CLOCK mirror touched when register changed", "desk", "LOOK" if not ok else "MANUAL",
            "register changed; brief NOT changed" if not ok else "register + brief both changed — confirm the event SET matches")

    # Preserve dating of actual EXIT edits; reviewed-unchanged does not refresh vintage.
    ex = now_text("workbook/EXIT_PROTOCOL.md")
    m = re.search(r"Newest entry: (\d{4}-\d{2}-\d{2})", ex)
    if changed_since(base, "workbook/EXIT_PROTOCOL.md"):
        ok = bool(m) and date.fromisoformat(m.group(1)) >= t
        rec("3 EXIT_PROTOCOL freshness line", "desk", "PASS" if ok else "FAIL",
            f"Newest entry {m.group(1) if m else 'MISSING'} vs edited today")
    else:
        rec("3 EXIT_PROTOCOL reconciled without a cosmetic date bump", "desk",
            "PASS" if reconciled else "FAIL", "kill-leg review recorded in current reconciliation" if reconciled
            else "current reconciliation missing; no edit is required if unchanged")

    # 4 SCRATCH
    sc_txt = now_text("SCRATCH.md")
    # count HEADINGS only — prose that MENTIONS the marker is not a banner
    n_first = len(re.findall(r"^> # ⛔ .*READ THIS BLOCK FIRST", sc_txt, re.M))
    top = sc_txt[:300]
    ok = changed_since(base, "SCRATCH.md") and t.isoformat() in top and n_first == 1
    rec("4 SCRATCH top block today, one READ-FIRST", "desk", "PASS" if ok else "FAIL",
        f"top block dated today: {t.isoformat() in top} · READ-FIRST banners: {n_first}")

    # 4b CLAUDE.md self-check: a ruling or a standing-rule change in STATUS must reach the charter
    add_st = added_lines(base, "STATUS.md")
    ruled = [l for l in add_st if new_ruling_lines([l], t)]
    if ruled and not changed_since(base, "CLAUDE.md"):
        rec("4b CLAUDE.md agrees with a ruling made this session", "desk", "FAIL",
            f"{len(ruled)} STATUS line(s) record a ruling; CLAUDE.md unchanged")
    elif ruled:
        rec("4b CLAUDE.md agrees with a ruling made this session", "desk", "MANUAL",
            "CLAUDE.md changed — confirm the THRESHOLDS/FILES rows carry the ruling")
    else:
        rec("4b CLAUDE.md self-check", "desk", "MANUAL", "no ruling detected; still ask the three questions")

    # 5 brief pin == STATUS HEAD, STATUS clean
    br = now_text("NEXUS_BRIEF.md")
    pin = re.search(r"STATUS commit:\*\* ([0-9a-f]{7,})", br)
    head = git("log", "-1", "--format=%h", "--", f"{REL}/STATUS.md").strip()
    st_dirty = bool(git("status", "--porcelain", "--", f"{REL}/STATUS.md").strip())
    ok = pin and head.startswith(pin.group(1)[:7]) and not st_dirty
    rec("5 NEXUS_BRIEF pin == STATUS HEAD (last write)", "desk", "PASS" if ok else "FAIL",
        f"pin {pin.group(1) if pin else 'MISSING'} · STATUS HEAD {head} · STATUS uncommitted: {st_dirty}")

    # record discipline (items 5 + 6 of the 10/09 review)
    fx = fixed_without_sha(add_st + added_lines(base, "SCRATCH.md"))
    rec("rec FIXED/DONE carries a commit sha", "desk 10/09", "LOOK" if fx else "PASS",
        "; ".join(fx[:3]) if fx else "every FIXED/DONE claim added this session carries a sha")
    ps = []
    for f in ("STATUS.md", "SCRATCH.md", "THESIS.md", "docket/CATALYSTS.tsv"):
        old = at_base(base, f)
        for l in prestated_without_public(added_lines(base, f)):
            # a row REWRITTEN this session re-adds its old claims; only a claim whose
            # pre-stated clause is NEW since base is this session's to justify
            m = re.search(r"pre-?(stated|registered|committed).{0,60}", l, re.I)
            if m and m.group(0) in old:
                continue
            ps.append(l)
    rec("rec pre-stated claims carry first-public time", "desk 10/09 [L-43]", "LOOK" if ps else "PASS",
        "; ".join(x[:140] for x in ps[:2]) if ps else "none missing")

    # boot alarms block (VIOLET pattern)
    sys.path.insert(0, str(DESK))
    try:
        import boot  # noqa: E402
        n_due, due = boot.predictions_due()
        rec("BLOCK predictions due resolved", "boot leg 2", "PASS" if not due else "FAIL",
            "none due" if not due else f"{len(due)} due: {due[:2]}")
        for leg, fn, needle in (("S2 series", boot.s2_series_age, "S2_SERIES"),
                                ("MAG7 series", boot.mag7_series_age, "MAG7_SERIES"),
                                ("S4 series", boot.s4_series_age, "S4_SERIES")):
            rc_, _ = fn()
            if rc_ == 0:
                rec(f"BLOCK {leg} fresh", "boot", "PASS", "quiet")
            else:
                frozen = "FROZEN" in (DESK / "workbook" / f"{needle}.tsv").read_text(encoding="utf-8")[:400]
                cov = frozen or deferral_covers(st_now, needle, t)
                rec(f"BLOCK {leg} actioned", "boot", "PASS" if cov else "FAIL",
                    "FROZEN banner" if frozen else ("dated deferral in STATUS" if cov else "boot flagged it; no FROZEN banner and no dated 'DEFERRED to' in STATUS"))
    except Exception as e:  # noqa: BLE001
        rec("BLOCK boot legs", "boot", "FAIL", f"could not import/run boot legs: {type(e).__name__}: {e}")

    # root 1b orphan
    rc, out = run_cmd(["bash", "scripts/orphan_check.sh", "VULCAN"])
    rec("root 1b orphan check", "root", "LOOK" if "[likely YOURS]" in out else "PASS",
        "likely-yours files present" if "[likely YOURS]" in out else "no likely-yours residue")

    # root 1c consumers of a moved composite / score
    if comp_base and comp_now and comp_base != comp_now:
        hits = []
        g = git("grep", "-n", "-I", "-F", comp_base, "--", "AGENTS", "PROME",
                ":!AGENTS/VULCAN", ":!*archive*", ":!*processed*", ":!*_COLD*",
                ":!*/inbox/*")  # a delivered packet is an immutable dated record, not a consumer
        for l in g.splitlines():
            if "VULCAN" in l:
                hits.append(l.split(":")[0])
        hits = sorted(set(hits))

        def owner_inbox(path):
            parts = path.split("/")
            return ROOT / "PROME" / "inbox" if parts[0] == "PROME" else ROOT / "AGENTS" / parts[1] / "inbox"

        def packeted(path):
            # handled = a VULCAN packet dated TODAY sits in (or was consumed from) the owner's inbox
            ib = owner_inbox(path)
            pat = f"{t.isoformat()}_from-VULCAN*"
            return any(ib.glob(pat)) or any((ib / "processed").glob(pat))

        open_ = [h for h in hits if not packeted(h)]
        rec("root 1c consumers of the old composite", "root", "LOOK" if open_ else "PASS",
            (f"{comp_base} -> {comp_now}; owners NOT yet packeted today: {open_[:6]} — packet each OWNER, never edit"
             if open_ else f"{comp_base} -> {comp_now}; {len(hits)} citing file(s), every owner packeted today")
            if hits else f"{comp_base} -> {comp_now}; no live consumer found")
    else:
        rec("root 1c consumer check", "root", "MANUAL",
            "composite unchanged; for any OTHER superseded figure run scripts/consumer_check.py --agent VULCAN --old X --new Y (+ --self)")

    # root 1c-bis / 1e / read-cap
    rc, out = run_cmd([sys.executable, "scripts/ledger_staleness.py", "VULCAN", "--quiet"])
    stale = re.findall(r"([A-Z0-9_]+)\.tsv \(\+\d+d", out)
    uncovered = [n for n in stale if not deferral_covers(st_now, n, t)
                 and "FROZEN" not in (DESK / "workbook" / f"{n}.tsv").read_text(encoding="utf-8")[:400]]
    rec("root 1c-bis ledger staleness", "root (DELEGATED)", "LOOK" if uncovered else "PASS",
        f"stale and NOT frozen/deferred: {uncovered}" if uncovered else
        (f"stale but covered by FROZEN/dated deferral: {stale}" if stale else "quiet"))
    rc, out = run_cmd([sys.executable, "scripts/claim_check.py", "--check", "weekday",
                       f"{REL}/STATUS.md", f"{REL}/SCRATCH.md", f"{REL}/NEXUS_BRIEF.md", f"{REL}/docket/CATALYSTS.tsv"])
    rec("root 1e claim check (weekday)", "root (DELEGATED)", "PASS" if rc == 0 else "LOOK", out.strip().splitlines()[-1][:100])
    rc, out = run_cmd([sys.executable, "scripts/read_cap_check.py", "--agent", "VULCAN"])
    rec("READ-CAP boot reads", "root Data Hygiene (DELEGATED)", "PASS" if rc == 0 else "FAIL", f"rc {rc}")

    # 6 git: tree clean + push status
    dirty = git("status", "--porcelain", "--", REL).strip()
    rec("6 own tree committed", "root 1", "PASS" if not dirty else "FAIL",
        "clean" if not dirty else f"{len(dirty.splitlines())} uncommitted path(s)")
    unpushed = git("log", "--format=%h", "origin/master..HEAD", "--", REL).split()
    deleg = any(re.search(r"push delegated to PROME", l, re.I) for l in add_st + added_lines(base, "SCRATCH.md"))
    if not unpushed:
        rec("root 2 pushed (local origin ref)", "root 2", "PASS", "no VULCAN commit ahead of origin/master (local ref; fetch to refresh)")
    else:
        rec("root 2 pushed (local origin ref)", "root 2", "PASS" if deleg else "FAIL",
            f"{len(unpushed)} VULCAN commit(s) not on origin — " +
            ("push DELEGATED to PROME (recorded); next boot verifies" if deleg else "run scripts/safe-push.sh, or record 'push delegated to PROME <time>'"))

    # MANUAL — printed every run
    for step, what in (
        ("2 KB/VX/FLOW/PREDICTIONS", "every new fact, state change, pathway, forecast logged?"),
        ("2b THESIS content", "does each touched channel's THESIS section AGREE (three questions)?"),
        ("2c CLOCK", "does NEXUS_BRIEF's ⏱️ THE CLOCK hold the same event SET as CATALYSTS.tsv?"),
        ("4 LESSONS", "did the session produce a correction, a defect, or a ruling? ⇒ a LESSONS.md row"),
        ("5 brief content", "does the brief say what STATUS says (status line, routing rows, figures)?"),
        ("7 coordinator COMPLETION", "a coordinator live (ListAgents)? ⇒ SendMessage a COMPLETION block with the shas"),
        ("root 1d memory", "wrote an auto-memory? ⇒ memory_index_check.py --strict --slug <name> + check_memory_length.sh"),
    ):
        rec(step, "MANUAL", "MANUAL", what)


def report():
    w = max(len(r[0]) for r in RESULTS) + 2
    for step, src, v, d in RESULTS:
        mark = {"PASS": "✓", "FAIL": "🔴", "LOOK": "⚠️ ", "MANUAL": "☐", "N/A": "·"}.get(v, "?")
        print(f"  {mark} {v:<6} {step:<{w}} {d}")
    bad = [r for r in RESULTS if r[2] in ("FAIL", "LOOK")]
    ran = sum(1 for r in RESULTS if r[2] in ("PASS", "FAIL", "LOOK"))
    print(f"\n  MECHANICAL: {ran} checked · {len(bad)} FAIL/LOOK · "
          f"{sum(1 for r in RESULTS if r[2] == 'MANUAL')} MANUAL (judgement — yours, every run)")
    print("  ⚠️  A clean run means the mechanical steps PASSED — never that the closeout is right.")
    return 1 if bad else 0



RULING_RE = re.compile(r"Will[- ]ruled|ruled in-session")
DATE_RE = re.compile(r"\b(?:(20\d\d)-(\d\d)-(\d\d)|(\d{1,2})/(\d{1,2}))\b")


def new_ruling_lines(lines, today, window=40):
    """Lines recording a ruling made TODAY. FIXED 2026-10-15: the old test flagged ANY added
    line containing 'Will-ruled', so a STATUS rewrite that RESTATED the 10/09 Firmus ruling
    read as a new, un-chartered ruling (a FAIL every run). A mention counts as OLD only when a
    date EARLIER than today sits within `window` chars of it; a mention with today's date, or
    with NO nearby date, still counts as new — undated fails CLOSED, never silently passes
    [finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]."""
    out = []
    for l in lines:
        for m in RULING_RE.finditer(l):
            seg = l[max(0, m.start() - window): m.end() + window]
            ds = []
            for d in DATE_RE.finditer(seg):
                try:
                    if d.group(1):
                        ds.append(date(int(d.group(1)), int(d.group(2)), int(d.group(3))))
                    else:
                        ds.append(date(today.year, int(d.group(4)), int(d.group(5))))
                except ValueError:
                    continue
            if not ds or today in ds or not any(x < today for x in ds):
                out.append(l)
                break
    return out


def selftest():
    ok = True

    def chk(label, cond):
        nonlocal ok
        print(("  ok   " if cond else "  FAIL ") + label)
        ok = ok and cond

    st = "**Composite: 15/25 — x** · **S1 3 · S2 2 · S3 3 · S4 3 · S5 4**\n## LIVE CHANNEL READS\n S1 9"
    sc, comp = parse_composite(st)
    chk("composite parses 5 scores", sc == {"S1": "3", "S2": "2", "S3": "3", "S4": "3", "S5": "4"})
    chk("composite parses the total", comp == "15/25")
    chk("FIXED without sha is flagged", fixed_without_sha(["(1) thing — **FIXED** (tests pass)"]) != [])
    chk("FIXED with a sha passes", fixed_without_sha(["(1) thing — **FIXED** `4238a1d0b`"]) == [])
    chk("a KB id is NOT mistaken for a sha", fixed_without_sha(["**FIXED** KB-204 2026"]) != [])
    chk("pre-stated w/o public time is flagged",
        prestated_without_public(["🔒 Pre-stated 2026-10-09, before the outcome: X"]) != [])
    chk("pre-stated WITH first-public time passes",
        prestated_without_public(["🔒 Pre-stated 2026-10-09 (first public: none found), before the outcome"]) == [])
    tsv = "date\tevent\n2026-10-08\told row\n2026-10-09\ttoday row\n2026-10-10\tfuture\n"
    chk("past rows: only < today", past_catalyst_rows(tsv, date(2026, 10, 9)) == ["2026-10-08 old row"])
    s = "x S2_SERIES.tsv stale — DEFERRED to 2026-10-16: decide"
    chk("deferral covers when date >= today", deferral_covers(s, "S2_SERIES", date(2026, 10, 9)))
    chk("deferral EXPIRED does not cover", not deferral_covers(s, "S2_SERIES", date(2026, 10, 17)))
    chk("deferral for another file does not cover", not deferral_covers(s, "MAG7_SERIES", date(2026, 10, 9)))
    T = date(2026, 10, 15)
    chk("ruling restated with an OLD date is not new",
        new_ruling_lines(["graded PULLED under the 9/25 rule (Will-ruled 10/09) [KB-209]"], T) == [])
    chk("ruling with TODAY's date is new", new_ruling_lines(["S5 rule (Will-ruled 10/15)"], T) != [])
    chk("ISO today is new", new_ruling_lines(["Will-ruled 2026-10-15: X"], T) != [])
    chk("UNDATED ruling fails closed (new)", new_ruling_lines(["the rule (Will-ruled) governs"], T) != [])
    chk("old + today both near: new", new_ruling_lines(["10/09 rule, Will-ruled again 10/15"], T) != [])
    chk("ruled in-session with old ISO date is not new",
        new_ruling_lines(["Will ruled in-session 2026-10-09 over my qualifier"], T) == [])
    chk("a line with no ruling is ignored", new_ruling_lines(["S5 FIRED 10/09"], T) == [])
    # Real Git fixtures: earlier STATUS edits must not bless later research.
    with tempfile.TemporaryDirectory(prefix="vulcan-reconcile-") as tmp:
        repo = Path(tmp)
        desk = repo / REL
        (desk / "workbook").mkdir(parents=True)

        def g(*args):
            return subprocess.run(["git", *args], cwd=repo, capture_output=True,
                                  text=True, check=True).stdout.strip()

        def write(name, text):
            (desk / name).write_text(text)

        def stamp(key, disposition="UNCHANGED", reason="reviewed; no analytical change"):
            return "> # ⛔ test — READ THIS BLOCK FIRST\n" + "\n".join(
                f"RECONCILE {key} {label} {disposition}: {reason}" for label in ANALYTICAL)

        g("init", "-q")
        g("config", "user.email", "fixture@example.invalid")
        g("config", "user.name", "Isolated fixture")
        for name in ANALYTICAL.values():
            write(name, "original\n")
        g("add", "--", REL)
        g("commit", "-qm", "baseline")
        base = g("rev-parse", "HEAD")
        write("STATUS.md", "earlier unrelated assessment edit\n")
        g("add", "--", f"{REL}/STATUS.md")
        g("commit", "-qm", "earlier STATUS")
        analytical_before = {name: (desk / name).read_bytes() for name in ANALYTICAL.values()}
        evidence_base = g("rev-parse", "HEAD")
        earlier, paths = reconciliation_scope(base, repo)
        old_stamp = stamp(earlier)
        chk("earlier current review can pass", not reconciliation_errors(old_stamp, earlier, paths))
        write("evidence.md", "later substantive evidence\n")
        later, paths = reconciliation_scope(base, repo)
        chk("untracked later evidence invalidates earlier STATUS/review", earlier != later and
            bool(reconciliation_errors(old_stamp, later, paths)))
        evidence_key, evidence_paths = reconciliation_scope(evidence_base, repo)
        chk("evidence-only passes with no STATUS change since base", "STATUS.md" not in evidence_paths and
            not reconciliation_errors(stamp(evidence_key), evidence_key, evidence_paths))
        chk("evidence-only can reconcile without analytical edits",
            not reconciliation_errors(stamp(later), later, paths))
        chk("missing disposition reason fails", bool(reconciliation_errors(stamp(later, reason="  "), later, paths)))
        chk("UPDATED cannot claim an unchanged THESIS/EXIT", bool(reconciliation_errors(stamp(later, "UPDATED"), later, paths)))
        chk("historical matching stamp cannot satisfy current block", bool(reconciliation_errors(
            "> # ⛔ current — READ THIS BLOCK FIRST\n> # ⛔ prior\n" + old_stamp, earlier, paths)))
        g("add", "--", f"{REL}/evidence.md")
        g("commit", "-qm", "later evidence")
        committed, paths = reconciliation_scope(base, repo)
        chk("commit preserves content-bound review key", committed == later)
        write("evidence.md", "corrected evidence\n")
        corrected, paths = reconciliation_scope(base, repo)
        chk("tracked uncommitted correction invalidates review", corrected != committed)
        write("receipt.md", "notification accepted; consumption unknown\n")
        receipt, paths = reconciliation_scope(base, repo)
        chk("receipt-only requires a current review, permits unchanged analytics", receipt != corrected and
            not reconciliation_errors(stamp(receipt), receipt, paths))
        chk("evidence and receipt review leaves all analytical bytes unchanged",
            analytical_before == {name: (desk / name).read_bytes() for name in ANALYTICAL.values()})
        chk("duplicate disposition fails", bool(reconciliation_errors(
            stamp(receipt) + f"\nRECONCILE {receipt} STATUS UNCHANGED: duplicate", receipt, paths)))
        write("SCRATCH.md", stamp(receipt))
        write("NEXUS_BRIEF.md", "derived brief; separate contract\n")
        chk("continuity writes do not self-invalidate key", reconciliation_scope(base, repo)[0] == receipt)
        g("mv", "--", f"{REL}/evidence.md", f"{REL}/renamed.md")
        renamed, paths = reconciliation_scope(base, repo)
        chk("rename changes key", renamed != receipt)
        # Remove a baseline-tracked record through Git, inside the disposable fixture.
        g("rm", "--", f"{REL}/THESIS.md")
        deleted, paths = reconciliation_scope(base, repo)
        chk("deletion represented and invalidates key", deleted != renamed and "THESIS.md" in paths)
        chk("baseline identity bound into key", reconciliation_scope("HEAD", repo)[0] != deleted)
        try:
            reconciliation_scope("not-a-valid-commit", repo)
            bad_base_raised = False
        except subprocess.CalledProcessError:
            bad_base_raised = True
        chk("Git failure cannot yield a passable empty key", bad_base_raised)
    print("SELFTEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--reconciliation-key", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    try:
        base = session_base(a.base)
        if a.reconciliation_key:
            print(reconciliation_scope(base)[0])
            return 0
    except Exception as e:  # noqa: BLE001
        print(f"closeout_check: cannot determine session base: {e}")
        return 2
    print("=" * 78)
    print(f"  VULCAN CLOSEOUT CHECK — {today_et()} · session base {base[:9]}")
    print("=" * 78)
    if a.list:
        print(__doc__)
        return 0
    try:
        checks(base)
    except Exception as e:  # noqa: BLE001
        print(f"  🔴 closeout_check crashed: {type(e).__name__}: {e} — a crash is NOT a pass")
        return 2
    return report()


if __name__ == "__main__":
    sys.exit(main())
