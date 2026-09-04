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
  python3 scripts/orch_log.py --selftest                # 10 drills: width · types · non-negative · EMPTY · event classes · append round-trip/refusals
CONTRACT (CHECK_STANDARD §9): rc 0 · 2 CANNOT-CERTIFY / refused. Never pads, never truncates, never repairs.
"""
import argparse, fcntl, os, re, subprocess, sys, tempfile

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip() or "."
LEDGER = os.path.join(ROOT, "PROME", "state", "ORCH_LOG.tsv")
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


def append(args, path=LEDGER):
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
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)
    print(f"ORCH-LOG ✓ appended 1 row ({fields[0]} {fields[1]} touch {fields[3]}, {event_type(fields)}) — ledger validates")
    return 0


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
        rc = append(ns, p); rows_after = open(p).read().count("\n") - 2
        drill("append: validated row appended, ledger still validates", rc == 0 and rows_after == 2 and check(p, quiet=True)[0] == 0)
        ns.drained = "two"; rc = append(ns, p); drill("append: non-integer drained REFUSED, nothing written", rc == 2 and open(p).read().count("\n") - 2 == 2)
        open(p, "w").write(hdr + good + "\n" + "bad\trow\n"); ns.drained = "1"; rc = append(ns, p)
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
    print("ORCH-LOG SELFTEST " + ("✓ 10/10" if not fails else f"✗ {fails}/10 FAILED")); return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("mode", nargs="?", choices=["check", "append"])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--ledger", default=LEDGER)
    for c in COLS:
        ap.add_argument(f"--{c}", default="")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.mode == "check":
        return check(a.ledger)[0]
    if a.mode == "append":
        return append(a, a.ledger)
    ap.print_help(); return 2


if __name__ == "__main__":
    sys.exit(main())
