#!/usr/bin/env python3
"""orch_log.py — the STRICT helper for PROME/state/ORCH_LOG.tsv (schema v2, 2026-09-03).

WHY. Codex found (PROME verified, 9/3) that the ledger carried 4 malformed rows (9- and 18-column)
and that the scorecard's zip-padding + int-only parse turned 63 unparseable `drained` cells into
"63 zero-drain touches" — a parseability count labelled as behaviour. Schema v2 (`69ec68d43`) fixed
the rows; this helper keeps them fixed: every row EXACTLY 13 tab-separated columns, four typed cells
(`drained` · `inbox_before` · `inbox_after` · `brief_defect_count`) INTEGER or EMPTY, EMPTY = UNKNOWN,
never 0. Owner of the file: PROME. Owner of this tool: DAEDALUS (repo-root scripts/ grant).

USAGE
  python3 scripts/orch_log.py check                     # validate the whole ledger; rc 0 clean · 2 malformed (rows named)
  python3 scripts/orch_log.py append --date 2026-09-04 --desk SAM --tier subagent --touch 1 \
      --trigger "..." --drained 3 --delivered "..." --zero_capital OK --notes "..." \
      --brief_defects "..." --inbox_before 5 --inbox_after 2 --brief_defect_count 0
      # validates the NEW row and the EXISTING ledger, then appends atomically (.tmp + os.replace).
      # rc 0 appended · 2 refused (nothing written). Omit a typed flag to record EMPTY (= UNKNOWN).
      # L733 (2026-10-20): REFUSES when the ledger holds rows the current view does not count (rows entered without this
      # writer) unless --acknowledge-unobserved K names exactly that delta (echoed into notes); refuses a view ahead of the ledger.
  python3 scripts/orch_log.py view [--window-days 30]   # regenerate PROME/state/ORCH_INFLIGHT.md (L262 (a)); `append` does this as its LAST step
  python3 scripts/orch_log.py rotate --through YYYY-MM  # L262 (c): move rows dated <= YYYY-MM (not IN-FLIGHT) to PROME/archive/ORCH_LOG_<run-month>.tsv
      # under the writer lock; REFUSES (rc 2, nothing written) on: any IN-FLIGHT candidate · a hot or archive file that
      # fails `check` before or after · broken row conservation · a --through month not strictly before the run month.
  python3 scripts/orch_log.py --selftest                # 11 core drills (incl. IN-FLIGHT-by-form) + 10 L262 drills (view · append→view · rotate both paths) + 13 L733 drills (hand row · ack · inode swap · \r)
CONTRACT (CHECK_STANDARD §9): rc 0 · 2 CANNOT-CERTIFY / refused. Never pads, never truncates, never repairs.

L262 (PROME-ruled 2026-09-04, DAEDALUS rule-15 input; Will "L262 go ahead" 9/4 ~10:0x). (a) The VIEW is a typed-only
projection — `date · desk · tier · touch · drained · delivered[:40] · inbox_before · inbox_after` — of (i) every row whose
`delivered` carries IN-FLIGHT and (ii) each desk's LAST `drained>0` touch inside `--window-days` (the rule-6b/leg-3b window is a
DECLARED soak parameter, not a canon constant, so the header prints the window used and names the desks with no such touch
inside it — nothing is hidden by the default). One writer, one lock ⇒ the view cannot drift from the ledger (PAT-113).
(c) ROTATION writes the archive FIRST, then the hot file; if the second replace fails the archive holds an extra copy, which the
scorecard consumer half de-duplicates on (date, desk, touch) and REPORTS — never a silent loss, never a silent double count.
"""
import argparse, datetime, fcntl, os, re, subprocess, sys, tempfile, zlib
import orch_time

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip() or "."
LEDGER = os.path.join(ROOT, "PROME", "state", "ORCH_LOG.tsv")
VIEW = os.path.join(ROOT, "PROME", "state", "ORCH_INFLIGHT.md")
ARCHIVE_DIR = os.path.join(ROOT, "PROME", "archive")
VIEW_COLS = ["date", "desk", "tier", "touch", "drained", "delivered", "inbox_before", "inbox_after"]
DEFAULT_WINDOW_DAYS = 30
COLS = ["date", "desk", "tier", "touch", "trigger", "drained", "delivered", "zero_capital", "notes",
        "brief_defects", "inbox_before", "inbox_after", "brief_defect_count"]
TYPED = {"drained", "inbox_before", "inbox_after", "brief_defect_count"}
N = len(COLS)
# TOUCH-TOKEN CLASSES (ledger header, 2026-09-03 EVE — Codex follow-up, PROME-verified): the `touch`
# cell classifies the ROW. Integer or integer+suffix ("1" · "2b" · "2-CLOSEOUT-PING") = TOUCH, the only
# class touch metrics count; "CLOSE" = CLOSE_SUMMARY (session-close provenance, excluded from touch /
# delivery / zero-drain counts); "N-RESULT" retired 9/3 (collapsed into the touch rows). Any other
# token is a validation problem — a row of unknown class must not be silently counted either way.
RE_TOUCH = re.compile(r"^\d+(?:[A-Za-z-][A-Za-z0-9-]*)?$")


def event_type(fields):
    """'TOUCH' · 'CLOSE_SUMMARY' · None (unknown token) for one 13-field row."""
    t = fields[3].strip()
    if t.upper() == "CLOSE":
        return "CLOSE_SUMMARY"
    if re.match(r"^\d+-RESULT$", t, re.I):
        return None                         # retired 9/3 (collapsed into touch rows) — never a TOUCH by suffix accident
    if RE_TOUCH.match(t):
        return "TOUCH"
    return None


def int_or_empty(s):
    s = (s or "").strip()
    if s == "":
        return True, None
    if s.lstrip("-").isdigit():
        return True, int(s)
    return False, s


def validate_line(fields, lineno):
    """Return list of problems for one data row (already split on tab)."""
    probs = []
    if len(fields) != N:
        probs.append(f"L{lineno}: {len(fields)} columns (need exactly {N})")
        return probs
    for i, name in enumerate(COLS):
        if name in TYPED:
            ok, v = int_or_empty(fields[i])
            if not ok:
                probs.append(f"L{lineno}: `{name}` = {fields[i][:40]!r} is neither an integer nor EMPTY")
            elif v is not None and v < 0:
                probs.append(f"L{lineno}: `{name}` = {v} is NEGATIVE — typed counts are non-negative (a count below zero is a defect, not a value)")
    if event_type(fields) is None:
        probs.append(f"L{lineno}: `touch` = {fields[3][:30]!r} is neither a TOUCH token (integer[+suffix]) nor CLOSE — unknown event class")
    if not fields[0].strip() or not fields[1].strip():
        probs.append(f"L{lineno}: date/desk empty")
    if fields[0].lstrip().startswith("#") or fields[0] == "date":
        probs.append(f"L{lineno}: `date` = {fields[0][:20]!r} would be read as a comment/header by `check` — the row would be invisible (L733 read R5)")
    cr = [COLS[i] for i, v in enumerate(fields) if "\r" in v]
    if cr:
        probs.append(f"L{lineno}: carriage return inside cell(s) {cr} — `check` reads universal newlines, so a \\r splits the row (L733 CE4)")
    return probs


def check(path=LEDGER, quiet=False):
    try:
        lines = open(path, encoding="utf-8").read().split("\n")
    except OSError as e:
        print(f"ORCH-LOG ✗ rc 2 CANNOT-CERTIFY: {e}"); return 2, []
    probs, rows, header_seen = [], [], False
    for n, ln in enumerate(lines, 1):
        if not ln.strip() or ln.startswith("#"):
            continue
        f = ln.split("\t")
        if f[0] == "date":
            header_seen = True
            if f != COLS:
                probs.append(f"L{n}: header is not schema v2 ({len(f)} cols: {f[:4]}…)")
            continue
        probs += validate_line(f, n)
        rows.append(f)
    if not header_seen:
        probs.append("no `date\\t…` header row found")
    if probs:
        if not quiet:
            print(f"ORCH-LOG ✗ rc 2 — {len(probs)} problem(s) in {os.path.relpath(path, ROOT)} (never padded, never repaired):")
            for p in probs[:20]:
                print("  " + p)
        return 2, rows
    if not quiet:
        print(f"ORCH-LOG ✓ {os.path.relpath(path, ROOT)}: {len(rows)} data rows × {N} columns, typed cells int-or-EMPTY")
    return 0, rows


LOCK_RETRIES = 5
RE_VIEW_COUNT = re.compile(r"source (\S+) \((\d+) data rows\)")


def _locked_open(path, _after_open=None):
    """L733 CE3 (2026-10-20): open + exclusive flock on the file CURRENTLY at `path`. `rotate` replaces the ledger with
    os.replace, so a writer that waited on the OLD inode's lock would write to an unlinked file. After the lock is held,
    compare the descriptor's inode with the path's; on a mismatch, drop it and reopen (bounded). Returns fh or None."""
    for _ in range(LOCK_RETRIES):
        try:
            fh = open(path, "a+", encoding="utf-8")
        except OSError as e:
            print(f"ORCH-LOG ✗ rc 2 — {e}"); return None
        if _after_open:
            _after_open()
        fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            same = os.fstat(fh.fileno()).st_ino == os.stat(path).st_ino
        except OSError:
            same = False
        if same:
            return fh
        fcntl.flock(fh, fcntl.LOCK_UN); fh.close()
    print(f"ORCH-LOG ✗ rc 2 — could not lock the current {os.path.relpath(path, ROOT)} after {LOCK_RETRIES} tries (file replaced repeatedly); nothing written")
    return None


def _view_count(view_path, path):
    """L733 CE1 (2026-10-20): ('missing', None) · ('bad', reason) · ('ok', N) from the view header."""
    if not os.path.exists(view_path):
        return "missing", None
    try:
        head = open(view_path, encoding="utf-8").read(4096)
    except OSError as e:
        return "bad", f"view unreadable: {e}"
    m = RE_VIEW_COUNT.search(head)
    if not m:
        return "bad", "view header carries no `source … (N data rows)`"
    # The header's `source` path is NOT compared here (PROME's stated follow-up, packet 2026-10-15) — count only.
    return "ok", int(m.group(2))


def append(args, path=LEDGER, view_path=VIEW, window_days=DEFAULT_WINDOW_DAYS, _after_open=None):
    """Validate the new row and the existing ledger, then ONE O_APPEND write under an exclusive lock.
    (First cut used a fixed .tmp + os.replace: atomic in visibility, not safe against two concurrent
    appenders — Codex 9/3. A single small O_APPEND write is atomic per POSIX; the flock makes the
    validate-then-write sequence exclusive too.)"""
    fields = [(getattr(args, c) or "").replace("\t", " ").replace("\r", " ").replace("\n", " ") for c in COLS]
    probs = validate_line(fields, 0)
    if probs:
        print("ORCH-LOG ✗ rc 2 — new row refused: " + "; ".join(probs)); return 2
    ack = getattr(args, "acknowledge_unobserved", None)
    fh = _locked_open(path, _after_open)
    if fh is None:
        return 2
    first_use = False
    with fh:
        try:
            rc, rows = check(path, quiet=True)
            if rc:
                print("ORCH-LOG ✗ rc 2 — refusing to append to a ledger that does not validate (run `check`)"); return 2
            if orch_time.MARKER in fields[8]:
                try:
                    orch_time.validate_correction(fields, rows, datetime.datetime.now(datetime.timezone.utc))
                except (ValueError, TypeError, KeyError) as exc:
                    print(f"ORCH-LOG ✗ rc 2 — invalid time correction: {exc}; nothing written"); return 2
            # L733 CE1: rows entered WITHOUT this writer are named here, never absorbed by the regenerated view.
            state, val = _view_count(view_path, path)
            if state == "missing":
                first_use = True
            elif state == "bad":
                print(f"ORCH-LOG ✗ rc 2 — append REFUSED: {val}; run `orch_log.py view` only after naming any unobserved rows; nothing written"); return 2
            else:
                delta = len(rows) - val
                if delta < 0:
                    print(f"ORCH-LOG ✗ rc 2 — append REFUSED: the view counts {val} rows but the ledger holds {len(rows)} — {-delta} row(s) VANISHED from the ledger (append-only); nothing written"); return 2
                if delta > 0:
                    if ack is None or ack != delta:
                        print(f"ORCH-LOG ✗ rc 2 — append REFUSED: {len(rows)} ledger rows vs the view's {val} — {delta} row(s) entered without this writer; run `check`, name them, then re-run with --acknowledge-unobserved {delta}"
                              + (f" (you passed {ack})" if ack is not None else "") + "; nothing written"); return 2
                    fields[8] = "; ".join(x for x in (f"ACK-UNOBSERVED {delta}", fields[8].strip()) if x)
                elif ack:
                    print(f"ORCH-LOG ✗ rc 2 — append REFUSED: --acknowledge-unobserved {ack} given but the view and ledger agree (0 unobserved); nothing written"); return 2
            fh.seek(0, os.SEEK_END)
            prefix = "" if (fh.tell() == 0 or open(path, "rb").read()[-1:] == b"\n") else "\n"
            fh.write(prefix + "\t".join(fields) + "\n")
            fh.flush(); os.fsync(fh.fileno())
            # L733 CE4: the success line is printed only if the ledger still validates AFTER the write.
            rc_after, rows_after = check(path, quiet=True)
            if rc_after:
                print(f"ORCH-LOG ✗ rc 2 — row appended but the ledger NO LONGER VALIDATES (run `check`); view NOT regenerated"); return 2
            if len(rows_after) != len(rows) + 1:
                print(f"ORCH-LOG ✗ rc 2 — row written but `check` now counts {len(rows_after)} rows, not {len(rows) + 1}: the row is not visible to the instruments; view NOT regenerated"); return 2
            # L262 (a): the view is regenerated HERE, under the same lock, as the last step — one writer, no drift.
            vrc = write_view(path, view_path, window_days, quiet=True)
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)
    print(f"ORCH-LOG ✓ appended 1 row ({fields[0]} {fields[1]} touch {fields[3]}, {event_type(fields)}) — ledger validates after the write"
          + (" · first use: no view existed" if first_use else "")
          + (f" · view regenerated → {os.path.relpath(view_path, ROOT)}" if vrc == 0 else " · ⚠️ ROW APPENDED BUT VIEW NOT REGENERATED — run `orch_log.py view`"))
    return 0 if vrc == 0 else 2


# IN-FLIGHT is a STATE TOKEN and is matched by FORM — the LEADING token of the `delivered` cell — never by keyword
# presence anywhere in the cell. First cut (9/4 morning) was a substring test; PROME found it the same day: the 8/28 MIDAS
# row, DELIVERED, carried "Gold in-flight 13:37" 842 chars into its prose and rendered as in flight (PAT-059's class,
# `finding_marker_word_in_prose_disables_the_scanner_that_reads_for_it` inverted: prose ENABLED the state). Every genuine
# IN-FLIGHT cell in the ledger's history leads with the token (12/12 at 9/4), so the form match loses nothing.
RE_INFLIGHT = re.compile(r"^\s*IN-FLIGHT\b", re.I)


def is_inflight(cell):
    """True only when the `delivered` cell's LEADING token is IN-FLIGHT (state by form, PAT-059)."""
    return bool(RE_INFLIGHT.match(cell or ""))


def _is_inflight(fields):
    return is_inflight(fields[6])


def _split_ledger(path):
    """→ (leading_comment_lines, header_line, data_lines) preserving text byte-exact; None on read error."""
    try:
        text = open(path, encoding="utf-8").read()
    except OSError as e:
        print(f"ORCH-LOG ✗ rc 2 CANNOT-CERTIFY: {e}"); return None
    comments, header, data = [], None, []
    for ln in text.split("\n"):
        if header is None:
            if ln.startswith("#") or not ln.strip():
                comments.append(ln)
            elif ln.split("\t")[0] == "date":
                header = ln
            else:
                data.append(ln)           # pre-header data row: check() will refuse it; keep byte-exact
        elif ln.strip():
            data.append(ln)
    return comments, header, data


def render_view(rows, window_days=DEFAULT_WINDOW_DAYS, today=None, source=LEDGER):
    """Typed-only projection (L262 (a)). `rows` = validated 13-field rows."""
    today = today or datetime.date.today()
    cutoff = (today - datetime.timedelta(days=window_days)).isoformat()
    inflight = [r for r in rows if event_type(r) == "TOUCH" and _is_inflight(r)]
    last = {}
    for r in rows:
        if event_type(r) != "TOUCH":
            continue
        ok, v = int_or_empty(r[5])
        if ok and v is not None and v > 0 and r[0] >= cutoff:
            if r[1] not in last or r[0] >= last[r[1]][0]:
                last[r[1]] = r
    desks_all = sorted({r[1] for r in rows if event_type(r) == "TOUCH"})
    none_in_window = [d for d in desks_all if d not in last]
    def cell(r, i):
        v = (r[i] or "").replace("|", "¦").strip()
        return v[:40] if i == 6 else v
    out = ["# ORCH_INFLIGHT — GENERATED in-flight view of `PROME/state/ORCH_LOG.tsv` (DOCKET L262 (a), PROME-ruled 2026-09-04). DO NOT EDIT — regenerated by `scripts/orch_log.py append` (last step, under the writer lock) or `scripts/orch_log.py view`.",
           f"# generated {today.isoformat()} · source {os.path.relpath(source, ROOT)} ({len(rows)} data rows) · window {window_days}d (cutoff {cutoff}; a DECLARED soak parameter — pass --window-days to change; nothing below is hidden by it, see the last line) · typed columns only; `delivered` truncated to 40 chars.",
           "",
           f"## IN-FLIGHT rows ({len(inflight)}) — an open PROME touch: neither live nor dark; never doorbell one (WALTER 9b). Corroborate with ListAgents + write recency; IN-FLIGHT lags a death indefinitely.",
           "", "| " + " | ".join(VIEW_COLS) + " |", "|" + "---|" * len(VIEW_COLS)]
    for r in sorted(inflight, key=lambda r: (r[0], r[1])):
        out.append("| " + " | ".join(cell(r, COLS.index(c)) for c in VIEW_COLS) + " |")
    out += ["", f"## Last `drained>0` touch per desk inside the window ({len(last)} desks) — the leg-3b cadence input (a zero-drain touch never resets a desk's clock)",
            "", "| " + " | ".join(VIEW_COLS) + " |", "|" + "---|" * len(VIEW_COLS)]
    for d in sorted(last):
        r = last[d]; out.append("| " + " | ".join(cell(r, COLS.index(c)) for c in VIEW_COLS) + " |")
    out += ["", f"**Desks with a TOUCH row but NO `drained>0` touch inside {window_days}d ({len(none_in_window)}):** " + (", ".join(none_in_window) if none_in_window else "(none)") + " — absence here proves nothing about liveness (ABSENT-ROW clause); it says the ledger holds no recent drained touch.", ""]
    return "\n".join(out)


def write_view(path=LEDGER, view_path=VIEW, window_days=DEFAULT_WINDOW_DAYS, today=None, quiet=False):
    """Regenerate the view from a ledger that validates. rc 0 · 2 (ledger invalid or write failed; view untouched)."""
    rc, rows = check(path, quiet=True)
    if rc:
        print(f"ORCH-LOG ✗ rc 2 — VIEW NOT REGENERATED: {os.path.relpath(path, ROOT)} does not validate"); return 2
    text = render_view(rows, window_days, today, path)
    try:
        tmp = view_path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.write(text); fh.flush(); os.fsync(fh.fileno())
        os.replace(tmp, view_path)
    except OSError as e:
        print(f"ORCH-LOG ✗ rc 2 — VIEW NOT REGENERATED: {e}"); return 2
    if not quiet:
        n_if = text.count("\n| 20")  # rows in both tables
        print(f"ORCH-LOG ✓ view regenerated → {os.path.relpath(view_path, ROOT)} ({len(text.encode())} B, {n_if} table rows, window {window_days}d)")
    return 0


def guarded_view(path=LEDGER, view_path=VIEW, window_days=DEFAULT_WINDOW_DAYS, acknowledge_unobserved=None):
    """L736: public view cannot erase an unexplained count change. Internal writers use write_view."""
    if acknowledge_unobserved not in (None, 0):
        print("ORCH-LOG rc 2 — view REFUSED: acknowledgment belongs to append, not view; nothing written")
        return 2
    fh = _locked_open(path)
    if fh is None:
        return 2
    with fh:
        try:
            rc, rows = check(path, quiet=True)
            if rc:
                print("ORCH-LOG rc 2 — view REFUSED: repair the invalid ledger first; view unchanged")
                return 2
            state, value = _view_count(view_path, path)
            if state == "bad":
                print(f"ORCH-LOG rc 2 — view REFUSED: {value}; restore a verified view baseline; nothing written")
                return 2
            if state == "ok" and value != len(rows):
                delta = len(rows) - value
                print(f"ORCH-LOG rc 2 — view REFUSED: ledger {len(rows)} rows vs view {value}; delta {delta}; nothing written")
                if delta > 0:
                    print(f"Inspect the extra rows. A legitimate next append requires --acknowledge-unobserved {delta}; do not invent an event to reset the view.")
                else:
                    print("Investigate missing ledger rows before restoring the verified baseline.")
                return 2
            if state == "missing":
                print("ORCH-LOG first use: no view baseline exists; rendering does not establish writer provenance")
            return write_view(path, view_path, window_days)
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)


def rotate(through, path=LEDGER, archive_dir=ARCHIVE_DIR, today=None, view_path=VIEW, window_days=DEFAULT_WINDOW_DAYS, _drop_one_for_test=False):
    """L262 (c). Move data rows dated <= `through` (YYYY-MM) that are NOT IN-FLIGHT to
    <archive_dir>/ORCH_LOG_<run-month>.tsv, byte-exact, under the writer lock. Every refusal is rc 2 with NOTHING written."""
    today = today or datetime.date.today()
    run_month = today.strftime("%Y-%m")
    if not re.match(r"^\d{4}-\d{2}$", through or ""):
        print("ORCH-LOG ✗ rc 2 — rotate: --through must be YYYY-MM"); return 2
    if through >= run_month:
        print(f"ORCH-LOG ✗ rc 2 — rotate REFUSED: --through {through} is not strictly before the run month {run_month} (the container is named by the month the rotation RUNS and asserts every row predates it)"); return 2
    fh = _locked_open(path)
    if fh is None:
        return 2
    with fh:
        try:
            rc, rows_before = check(path, quiet=True)
            if rc:
                print("ORCH-LOG ✗ rc 2 — rotate REFUSED: hot ledger does not validate (run `check`); nothing written"); return 2
            parts = _split_ledger(path)
            if parts is None or parts[1] is None:
                print("ORCH-LOG ✗ rc 2 — rotate REFUSED: no header row; nothing written"); return 2
            comments, header, data = parts
            move, keep = [], []
            for ln in data:
                f = ln.split("\t")
                (move if f[0][:7] <= through else keep).append(ln)
            if not move:
                print(f"ORCH-LOG ✗ rc 2 — rotate REFUSED: no rows dated <= {through}; nothing written"); return 2
            time_problem = orch_time.rotation_problem(rows_before, [ln.split("\t") for ln in move])
            if time_problem:
                print(f"ORCH-LOG ✗ rc 2 — rotate REFUSED: {time_problem}; nothing written"); return 2
            stuck = [ln.split("\t") for ln in move if _is_inflight(ln.split("\t"))]
            if stuck:
                print(f"ORCH-LOG ✗ rc 2 — rotate REFUSED: {len(stuck)} candidate row(s) still IN-FLIGHT — " +
                      " · ".join(f"{f[0]} {f[1]} t{f[3]}" for f in stuck[:10]) + "; consume them first; nothing written"); return 2
            first_of_run = run_month + "-01"
            late = [ln for ln in move if ln.split("\t")[0] >= first_of_run]
            if late:
                print(f"ORCH-LOG ✗ rc 2 — rotate REFUSED: {len(late)} candidate row(s) dated >= {first_of_run} (container assert); nothing written"); return 2
            os.makedirs(archive_dir, exist_ok=True)
            arc = os.path.join(archive_dir, f"ORCH_LOG_{run_month}.tsv")
            arc_rows_before = []
            if os.path.exists(arc):
                rc_a, arc_rows_before = check(arc, quiet=True)
                if rc_a:
                    print(f"ORCH-LOG ✗ rc 2 — rotate REFUSED: existing archive {os.path.relpath(arc, ROOT)} does not validate; nothing written"); return 2
                arc_text = open(arc, encoding="utf-8").read()
                if not arc_text.endswith("\n"):
                    arc_text += "\n"
            else:
                arc_text = (f"# ORCH_LOG ARCHIVE — rotation container {run_month} (DOCKET L262 (b), PROME-ruled 2026-09-04). Rows moved VERBATIM from PROME/state/ORCH_LOG.tsv by `scripts/orch_log.py rotate`; same 13-column schema v2 — validate with `python3 scripts/orch_log.py check --ledger <this file>`.\n"
                            f"# ASSERT: every data row is dated < {first_of_run} (named by the month the rotation RAN, never by content month — a container that keeps receiving is the 9/2 census defect). Additions-only; never edit a moved row here.\n"
                            + header + "\n")
            moved_text = "\n".join(move) + "\n"
            crc = zlib.crc32(moved_text.encode("utf-8")) & 0xFFFFFFFF
            arc_text_new = arc_text + f"# rotated {today.isoformat()} --through {through}: {len(move)} row(s), crc32 {crc} over the moved rows' text\n" + moved_text
            if _drop_one_for_test:
                arc_text_new = arc_text + f"# rotated {today.isoformat()} (TEST: one row dropped)\n" + "\n".join(move[1:]) + ("\n" if len(move) > 1 else "")
            nxt = (datetime.date(today.year + (today.month == 12), (today.month % 12) + 1, 1)).isoformat()
            rule7 = (f"# Rotated {today.isoformat()} --through {through}: {len(move)} row(s) (crc32 {crc}) → {os.path.relpath(arc, ROOT)}; "
                     f"re-check size at any append or on {nxt}, whichever first (READ_CAP rule 7).")
            hot_text_new = "\n".join(comments + [rule7, header] + keep) + "\n"
            # validate BOTH results on temp copies before either replace
            with tempfile.TemporaryDirectory() as td:
                ta, th = os.path.join(td, "a.tsv"), os.path.join(td, "h.tsv")
                open(ta, "w", encoding="utf-8").write(arc_text_new); open(th, "w", encoding="utf-8").write(hot_text_new)
                rc_a, arc_rows_after = check(ta, quiet=True)
                rc_h, hot_rows_after = check(th, quiet=True)
            if rc_a or rc_h:
                print("ORCH-LOG ✗ rc 2 — rotate REFUSED: the result would not validate (archive rc %d, hot rc %d); nothing written" % (rc_a, rc_h)); return 2
            if len(rows_before) != len(hot_rows_after) + len(move) or len(arc_rows_after) != len(arc_rows_before) + len(move):
                print(f"ORCH-LOG ✗ rc 2 — rotate REFUSED: row conservation broken (hot {len(rows_before)} → {len(hot_rows_after)} + moved {len(move)}; archive {len(arc_rows_before)} → {len(arc_rows_after)}); nothing written"); return 2
            # commit to disk: archive FIRST (an extra copy is recoverable and reported by the consumer half), hot second
            tmp = arc + ".tmp"
            with open(tmp, "w", encoding="utf-8") as w:
                w.write(arc_text_new); w.flush(); os.fsync(w.fileno())
            os.replace(tmp, arc)
            # L733 read R1 (2026-10-20): the NEW hot file is locked BEFORE it replaces the old one, so an appender that
            # opens the path after the swap waits for this rotate (and its view) instead of locking an unheld inode.
            tmp = path + ".tmp"
            newfh = open(tmp, "w", encoding="utf-8")
            fcntl.flock(newfh, fcntl.LOCK_EX)
            newfh.write(hot_text_new); newfh.flush(); os.fsync(newfh.fileno())
            os.replace(tmp, path)
            print(f"ORCH-LOG ✓ rotated {len(move)} row(s) dated <= {through} → {os.path.relpath(arc, ROOT)} (crc32 {crc}); hot {len(rows_before)} → {len(hot_rows_after)} rows; conservation {len(rows_before)} == {len(hot_rows_after)} + {len(move)} ✓")
            # L733 CE3: regenerate the view BEFORE releasing the locks (old inode and new), so no appender sees the new ledger with the old view.
            try:
                return write_view(path, view_path, window_days, today)
            finally:
                fcntl.flock(newfh, fcntl.LOCK_UN); newfh.close()
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)


def selftest():
    hdr = "# fixture\n" + "\t".join(COLS) + "\n"
    good = "\t".join(["2026-09-03", "SAM", "subagent", "1", "t", "3", "d", "OK", "n", "", "5", "2", "0"])
    empty = "\t".join(["2026-09-03", "HOMER", "subagent", "1", "t", "", "IN-FLIGHT", "OK", "n", "", "", "", ""])
    fails = 0
    def drill(name, ok):
        nonlocal fails; fails += not ok; print(f"  {'✓' if ok else '✗'} {name}")
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, "L.tsv")
        open(p, "w").write(hdr + good + "\n" + empty + "\n")
        rc, rows = check(p, quiet=True); drill("clean v2 ledger (incl. EMPTY typed cells) ⇒ rc 0", rc == 0 and len(rows) == 2)
        open(p, "w").write(hdr + good + "\n" + "\t".join(["2026-09-03", "X", "s", "1", "t", "3", "d", "OK", "n", "", "5", "2"]) + "\n")
        rc, _ = check(p, quiet=True); drill("12-column row ⇒ rc 2 (never padded)", rc == 2)
        open(p, "w").write(hdr + good.replace("\t3\t", "\t3 (partial)\t") + "\n")
        rc, _ = check(p, quiet=True); drill("prose in `drained` ⇒ rc 2 (never coerced to 0)", rc == 2)
        open(p, "w").write(hdr + good + "\n")
        ns = argparse.Namespace(**{c: "" for c in COLS}); ns.date = "2026-09-04"; ns.desk = "MIDAS"; ns.tier = "subagent"; ns.touch = "2"; ns.drained = "0"
        rc = append(ns, p, view_path=os.path.join(td, "V.md")); rows_after = open(p).read().count("\n") - 2
        drill("append: validated row appended, ledger still validates", rc == 0 and rows_after == 2 and check(p, quiet=True)[0] == 0)
        ns.drained = "two"; rc = append(ns, p, view_path=os.path.join(td, "V.md")); drill("append: non-integer drained REFUSED, nothing written", rc == 2 and open(p).read().count("\n") - 2 == 2)
        open(p, "w").write(hdr + good + "\n" + "bad\trow\n"); ns.drained = "1"; rc = append(ns, p, view_path=os.path.join(td, "V.md"))
        drill("append to a malformed ledger REFUSED", rc == 2)
        # 9/3 EVE hardenings
        open(p, "w").write(hdr + good.replace("\t3\t", "\t-3\t") + "\n")
        rc, _ = check(p, quiet=True); drill("NEGATIVE typed count ⇒ rc 2", rc == 2)
        close = "\t".join(["2026-08-28", "PROME", "session", "CLOSE", "t", "0", "d", "OK", "n", "", "", "", ""])
        open(p, "w").write(hdr + good + "\n" + close + "\n")
        rc, rows = check(p, quiet=True); kinds = [event_type(r) for r in rows]
        drill("CLOSE row accepted and classified CLOSE_SUMMARY; touch row TOUCH", rc == 0 and kinds == ["TOUCH", "CLOSE_SUMMARY"])
        open(p, "w").write(hdr + good.replace("\t1\tt\t", "\t1-RESULT\tt\t") + "\n")
        rc, _ = check(p, quiet=True); drill("retired '1-RESULT' token ⇒ rc 2 (unknown class, never silently counted)", rc == 2)
        drill("TOUCH token forms: 1 · 2b · 2-CLOSEOUT-PING all TOUCH", all(RE_TOUCH.match(t) for t in ("1", "2b", "2-CLOSEOUT-PING")) and not RE_TOUCH.match("CLOSE"))
        drill("IN-FLIGHT by FORM: leading token (with/without suffix) ⇒ in flight; a prose mention mid-cell in a DELIVERED row ⇒ NOT (PROME 9/4, MIDAS 8/28)",
              is_inflight("IN-FLIGHT (re-pinged 15:0x)") and is_inflight("IN-FLIGHT") and is_inflight("  in-flight 08:3x")
              and not is_inflight("✅ DELIVERED touch-1 ~11:0x … Gold in-flight 13:37 …") and not is_inflight("") and not is_inflight("OK — was IN-FLIGHT earlier"))
        # ---------- L262 drills (2026-09-04) — CHECK_STANDARD §3: alert path AND clean path, each watched
        T = datetime.date(2026, 10, 2)
        hot = os.path.join(td, "H.tsv"); vp = os.path.join(td, "V.md"); ad = os.path.join(td, "archive")
        r = lambda d, desk, t, dr, dl: "\t".join([d, desk, "subagent", t, "trig", dr, dl, "OK", "n", "", "", "", ""])
        open(hot, "w").write(hdr + r("2026-08-23", "SAM", "1", "3", "OK") + "\n" + r("2026-09-20", "HOMER", "1", "", "IN-FLIGHT") + "\n"
                             + r("2026-09-28", "MIDAS", "1", "0", "OK") + "\n" + r("2026-09-29", "BOND", "2", "4", "OK") + "\n"
                             + "\t".join(["2026-09-30", "PROME", "session", "CLOSE", "t", "0", "d", "OK", "n", "", "", "", ""]) + "\n")
        rc = write_view(hot, vp, 30, T, quiet=True); v = open(vp).read()
        drill("view: IN-FLIGHT row listed; drained>0 row inside 30d listed as cadence row", rc == 0 and "| 2026-09-20 | HOMER |" in v and "| 2026-09-29 | BOND |" in v)
        drill("view: zero-drain touch is NOT a cadence row; desk named in the no-touch line; CLOSE row never listed",
              "| 2026-09-28 | MIDAS |" not in v and "MIDAS" in v.split("NO `drained>0` touch")[1] and "| 2026-09-30 | PROME |" not in v)
        drill("view: drained>0 touch OLDER than the window is not a cadence row (SAM 8/23 vs 30d)", "| 2026-08-23 | SAM |" not in v and "SAM" in v.split("NO `drained>0` touch")[1])
        cur = open(hot).read(); open(hot, "w").write(cur.replace("IN-FLIGHT", "consumed 9/21"))   # read FIRST: open(...,"w") truncates before an inline read runs
        write_view(hot, vp, 30, T, quiet=True); v2 = open(vp).read()
        drill("view: consuming the IN-FLIGHT row (cell edited) removes it at the next regeneration", "| 2026-09-20 | HOMER |" not in v2)
        ns2 = argparse.Namespace(**{c: "" for c in COLS}); ns2.date = "2026-10-01"; ns2.desk = "ZHAO"; ns2.tier = "subagent"; ns2.touch = "1"; ns2.delivered = "IN-FLIGHT"
        before = open(vp).read(); rc = append(ns2, hot, view_path=vp)
        drill("append regenerates the view as its last step (new IN-FLIGHT row visible without a separate `view` call)", rc == 0 and open(vp).read() != before and "| 2026-10-01 | ZHAO |" in open(vp).read())
        # rotate — refusal paths first, each proving NOTHING was written
        snap = open(hot).read()
        open(hot, "w").write(snap.replace("consumed 9/21", "IN-FLIGHT")); snap_if = open(hot).read()
        rc = rotate("2026-09", hot, ad, T, vp, 30)
        drill("rotate REFUSES on an IN-FLIGHT candidate: rc 2, hot byte-identical, no archive created", rc == 2 and open(hot).read() == snap_if and not os.path.exists(os.path.join(ad, "ORCH_LOG_2026-10.tsv")))
        rc = rotate("2026-10", hot, ad, T, vp, 30)
        drill("rotate REFUSES --through == run month (container assert): rc 2, nothing written", rc == 2 and open(hot).read() == snap_if and not os.path.isdir(ad) or (os.path.isdir(ad) and not os.listdir(ad)))
        open(hot, "w").write(snap_if + "bad\trow\n")
        rc = rotate("2026-09", hot, ad, T, vp, 30)
        drill("rotate REFUSES a hot ledger that fails check: rc 2, nothing written", rc == 2 and not (os.path.isdir(ad) and os.listdir(ad)))
        open(hot, "w").write(snap)                     # HOMER consumed → rotatable
        rc = rotate("2026-09", hot, ad, T, vp, 30, _drop_one_for_test=True)
        drill("rotate REFUSES on broken row conservation (test hook drops one moved row): rc 2, hot byte-identical", rc == 2 and open(hot).read() == snap and not (os.path.isdir(ad) and os.listdir(ad)))
        rc = rotate("2026-09", hot, ad, T, vp, 30)
        arc = os.path.join(ad, "ORCH_LOG_2026-10.tsv"); ht = open(hot).read()
        rc_a, ar = check(arc, quiet=True); rc_h, hr = check(hot, quiet=True)
        drill("rotate SUCCEEDS: 5 rows (incl. CLOSE) → archive named by RUN month, both files validate, conservation 6 == 1 + 5, rule-7 line in hot, view regenerated",
              rc == 0 and rc_a == 0 and rc_h == 0 and len(ar) == 5 and len(hr) == 1 and "# Rotated 2026-10-02 --through 2026-09: 5 row(s)" in ht and "re-check size at any append or on 2026-11-01" in ht and "2026-10-01\tZHAO" in ht and "| 2026-10-01 | ZHAO |" in open(vp).read())
        open(hot, "w").write(ht + r("2026-09-30", "SAM", "3", "2", "OK") + "\n")
        rc = rotate("2026-09", hot, ad, T, vp, 30); rc_a, ar2 = check(arc, quiet=True)
        drill("rotate into an EXISTING archive appends (header once), validates, conservation 5 → 6", rc == 0 and rc_a == 0 and len(ar2) == 6 and open(arc).read().count("\ndate\t") == 1)
        # ---------- L733 drills (2026-10-20) — CE1 hand row · CE3 inode swap · CE4 carriage return; alert AND clean paths
        lp = os.path.join(td, "L733.tsv"); lv = os.path.join(td, "L733.md")
        def ns3(**kw):
            n = argparse.Namespace(**{c: "" for c in COLS}); n.date = "2026-10-20"; n.desk = "SAM"; n.tier = "subagent"; n.touch = "1"; n.drained = "1"
            n.acknowledge_unobserved = None
            for k, v in kw.items(): setattr(n, k, v)
            return n
        open(lp, "w").write(hdr + good + "\n")
        rc = append(ns3(), lp, lv); drill("L733 first use (no view) ⇒ rc 0, view created", rc == 0 and os.path.exists(lv))
        rc = append(ns3(desk="BOND"), lp, lv); drill("L733 writer-only sequence ⇒ rc 0 (view count follows)", rc == 0 and check(lp, quiet=True)[1].__len__() == 3)
        open(lp, "a").write(good + "\n"); snap = open(lp).read()
        rc = append(ns3(desk="HAND1"), lp, lv); drill("L733 CE1: hand row then append ⇒ rc 2, NOTHING written", rc == 2 and open(lp).read() == snap)
        rc = append(ns3(desk="HAND2", acknowledge_unobserved=2), lp, lv); drill("L733 wrong --acknowledge-unobserved K ⇒ rc 2, nothing written", rc == 2 and open(lp).read() == snap)
        rc = append(ns3(desk="ACK", notes="n"), lp, lv, ); rc = append(ns3(desk="ACK", notes="n", acknowledge_unobserved=1), lp, lv)
        drill("L733 correct --acknowledge-unobserved 1 ⇒ rc 0, notes carry ACK-UNOBSERVED 1", rc == 0 and "ACK-UNOBSERVED 1; n" in open(lp).read())
        rc = append(ns3(desk="X", acknowledge_unobserved=1), lp, lv); drill("L733 ack given when view and ledger agree ⇒ rc 2", rc == 2)
        txt = open(lp).read(); open(lp, "w").write(txt.rsplit(good + "\n", 1)[0] + txt.rsplit(good + "\n", 1)[1]); snap = open(lp).read()
        rc = append(ns3(desk="Y"), lp, lv); drill("L733 view AHEAD of ledger (row vanished) ⇒ rc 2, nothing written", rc == 2 and open(lp).read() == snap)
        write_view(lp, lv, quiet=True); vt = open(lv).read(); open(lv, "w").write(vt.replace(os.path.relpath(lp, ROOT), "PROME/state/OTHER.tsv"))
        rc = append(ns3(desk="Z"), lp, lv); drill("L733 view header naming another source is NOT compared (count-only, PROME's follow-up) ⇒ rc 0 when counts agree", rc == 0)
        open(lv, "w").write("# no count here\n"); rc = append(ns3(desk="Z"), lp, lv); drill("L733 view header without a count ⇒ rc 2", rc == 2)
        write_view(lp, lv, quiet=True)
        rc = append(ns3(desk="CR", notes="line1\r\nline2\rline3"), lp, lv)
        drill("L733 CE4: \\r in --notes is neutralised; ledger still validates", rc == 0 and check(lp, quiet=True)[0] == 0 and "\r" not in open(lp, newline="").read())
        drill("L733 CE4: validate_line rejects a cell containing \\r", bool(validate_line(["2026-10-20", "SAM", "s", "1", "t", "1", "d", "OK", "a\rb", "", "", "", ""], 1)))
        n_before = len(check(lp, quiet=True)[1])
        swapped = []
        def swap():   # CE3: the ledger is replaced ONCE (as one rotate does) between the writer's open and its lock
            if swapped: return
            swapped.append(1); t = open(lp).read(); tmp = lp + ".swap"; open(tmp, "w").write(t); os.replace(tmp, lp)
        rc = append(ns3(desk="SWAP"), lp, lv, _after_open=swap)
        drill("L733 CE3: inode replaced between open and lock ⇒ writer relocks; row lands in the CURRENT file", rc == 0 and len(check(lp, quiet=True)[1]) == n_before + 1 and "\tSWAP\t" in open(lp).read())
        open(lp, "w").write(hdr + good + "\n"); write_view(lp, lv, quiet=True); snap = open(lp).read()
        rc = append(ns3(date="#x", desk="HID"), lp, lv); drill("L733 R5: a `#`-leading date is refused (would be invisible to check), nothing written", rc == 2 and open(lp).read() == snap)
        open(lp, "a").write(good + "\n"); rc = append(ns3(desk="E", acknowledge_unobserved=1), lp, lv)
        drill("L733 R8: ack with empty notes has no dangling separator", rc == 0 and "\tACK-UNOBSERVED 1\t" in open(lp).read())
    total = 21 + 15
    print("ORCH-LOG SELFTEST " + (f"✓ {total}/{total}" if not fails else f"✗ {fails}/{total} FAILED")); return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("mode", nargs="?", choices=["check", "append", "view", "rotate"])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--ledger", default=LEDGER)
    ap.add_argument("--view-path", default=VIEW)
    ap.add_argument("--window-days", type=int, default=DEFAULT_WINDOW_DAYS)
    ap.add_argument("--through", default="", help="rotate: YYYY-MM (rows dated <= this month move); must be before the run month")
    ap.add_argument("--archive-dir", default=ARCHIVE_DIR)
    for c in COLS:
        ap.add_argument(f"--{c}", default="")
    ap.add_argument("--acknowledge-unobserved", type=int, default=None, dest="acknowledge_unobserved",
                    help="append: K rows were entered without this writer since the last view; K must equal the delta (echoed into notes)")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.mode == "check":
        return check(a.ledger)[0]
    if a.mode == "append":
        return append(a, a.ledger, a.view_path, a.window_days)
    if a.mode == "view":
        return guarded_view(a.ledger, a.view_path, a.window_days, a.acknowledge_unobserved)
    if a.mode == "rotate":
        return rotate(a.through, a.ledger, a.archive_dir, None, a.view_path, a.window_days)
    ap.print_help(); return 2


if __name__ == "__main__":
    sys.exit(main())
