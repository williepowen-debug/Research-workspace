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
  python3 scripts/orch_log.py view [--window-days 30]   # regenerate PROME/state/ORCH_INFLIGHT.md (L262 (a)); `append` does this as its LAST step
  python3 scripts/orch_log.py rotate --through YYYY-MM  # L262 (c): move rows dated <= YYYY-MM (not IN-FLIGHT) to PROME/archive/ORCH_LOG_<run-month>.tsv
      # under the writer lock; REFUSES (rc 2, nothing written) on: any IN-FLIGHT candidate · a hot or archive file that
      # fails `check` before or after · broken row conservation · a --through month not strictly before the run month.
  python3 scripts/orch_log.py --selftest                # 10 core drills + 9 L262 drills (view · append→view · rotate both paths)
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


def append(args, path=LEDGER, view_path=VIEW, window_days=DEFAULT_WINDOW_DAYS):
    """Validate the new row and the existing ledger, then ONE O_APPEND write under an exclusive lock.
    (First cut used a fixed .tmp + os.replace: atomic in visibility, not safe against two concurrent
    appenders — Codex 9/3. A single small O_APPEND write is atomic per POSIX; the flock makes the
    validate-then-write sequence exclusive too.)"""
    fields = [(getattr(args, c) or "").replace("\t", " ").replace("\n", " ") for c in COLS]
    probs = validate_line(fields, 0)
    if probs:
        print("ORCH-LOG ✗ rc 2 — new row refused: " + "; ".join(probs)); return 2
    try:
        fh = open(path, "a+", encoding="utf-8")
    except OSError as e:
        print(f"ORCH-LOG ✗ rc 2 — {e}"); return 2
    with fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            rc, _ = check(path, quiet=True)
            if rc:
                print("ORCH-LOG ✗ rc 2 — refusing to append to a ledger that does not validate (run `check`)"); return 2
            fh.seek(0, os.SEEK_END)
            prefix = "" if (fh.tell() == 0 or open(path, "rb").read()[-1:] == b"\n") else "\n"
            fh.write(prefix + "\t".join(fields) + "\n")
            fh.flush(); os.fsync(fh.fileno())
            # L262 (a): the view is regenerated HERE, under the same lock, as the last step — one writer, no drift.
            vrc = write_view(path, view_path, window_days, quiet=True)
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)
    print(f"ORCH-LOG ✓ appended 1 row ({fields[0]} {fields[1]} touch {fields[3]}, {event_type(fields)}) — ledger validates"
          + (f" · view regenerated → {os.path.relpath(view_path, ROOT)}" if vrc == 0 else " · ⚠️ ROW APPENDED BUT VIEW NOT REGENERATED — run `orch_log.py view`"))
    return 0 if vrc == 0 else 2


def _is_inflight(fields):
    return "IN-FLIGHT" in (fields[6] or "").upper()


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


def rotate(through, path=LEDGER, archive_dir=ARCHIVE_DIR, today=None, view_path=VIEW, window_days=DEFAULT_WINDOW_DAYS, _drop_one_for_test=False):
    """L262 (c). Move data rows dated <= `through` (YYYY-MM) that are NOT IN-FLIGHT to
    <archive_dir>/ORCH_LOG_<run-month>.tsv, byte-exact, under the writer lock. Every refusal is rc 2 with NOTHING written."""
    today = today or datetime.date.today()
    run_month = today.strftime("%Y-%m")
    if not re.match(r"^\d{4}-\d{2}$", through or ""):
        print("ORCH-LOG ✗ rc 2 — rotate: --through must be YYYY-MM"); return 2
    if through >= run_month:
        print(f"ORCH-LOG ✗ rc 2 — rotate REFUSED: --through {through} is not strictly before the run month {run_month} (the container is named by the month the rotation RUNS and asserts every row predates it)"); return 2
    try:
        fh = open(path, "a+", encoding="utf-8")
    except OSError as e:
        print(f"ORCH-LOG ✗ rc 2 — {e}"); return 2
    with fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
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
            for target, text in ((arc, arc_text_new), (path, hot_text_new)):
                tmp = target + ".tmp"
                with open(tmp, "w", encoding="utf-8") as w:
                    w.write(text); w.flush(); os.fsync(w.fileno())
                os.replace(tmp, target)
            print(f"ORCH-LOG ✓ rotated {len(move)} row(s) dated <= {through} → {os.path.relpath(arc, ROOT)} (crc32 {crc}); hot {len(rows_before)} → {len(hot_rows_after)} rows; conservation {len(rows_before)} == {len(hot_rows_after)} + {len(move)} ✓")
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)
    return write_view(path, view_path, window_days, today)


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
    print("ORCH-LOG SELFTEST " + ("✓ 20/20" if not fails else f"✗ {fails}/20 FAILED")); return 1 if fails else 0


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
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.mode == "check":
        return check(a.ledger)[0]
    if a.mode == "append":
        return append(a, a.ledger, a.view_path, a.window_days)
    if a.mode == "view":
        return write_view(a.ledger, a.view_path, a.window_days)
    if a.mode == "rotate":
        return rotate(a.through, a.ledger, a.archive_dir, None, a.view_path, a.window_days)
    ap.print_help(); return 2


if __name__ == "__main__":
    sys.exit(main())
