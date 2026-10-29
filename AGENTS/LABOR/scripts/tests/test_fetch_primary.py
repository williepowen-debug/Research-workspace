#!/usr/bin/env python3
"""
fetch_primary.py offline regression tests (BD-35, 2026-10-28).

Run:  .venv/bin/python3 AGENTS/LABOR/scripts/tests/test_fetch_primary.py
Exit: 0 all pass, 1 any fail. No network: every case reads a file written here.

What the tool must never do is let a figure through that the document does not
contain, or treat a wall/stub/garbage body as the document. The 2026-09-17 incident
(L-33) is case 1: the real release said 206,000; the summarizer said 213,000.
"""
import sys, pathlib, tempfile, io, contextlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import fetch_primary as F

FAILED = []
TMP = pathlib.Path(tempfile.mkdtemp())


def run(name, content, args, want_rc, want_text=None, suffix=".html"):
    p = TMP / f"{len(FAILED)}_{abs(hash(name))}{suffix}"
    p.write_bytes(content if isinstance(content, bytes) else content.encode())
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = F.main(["--file", str(p)] + args)
    out = buf.getvalue()
    ok = rc == want_rc and (want_text is None or want_text in out)
    print(f"{'PASS' if ok else 'FAIL'}  {name}: rc {rc} (want {want_rc})")
    if not ok:
        FAILED.append(name); print(out)


body = ("<html><body><p>TRANSMISSION OF MATERIALS IN THIS RELEASE IS EMBARGOED UNTIL 8:30 A.M. "
        "(Eastern) Thursday, September 17, 2026</p><p>In the week ending September 12, the advance "
        "figure for seasonally adjusted initial claims was 206,000, a decrease of 1,000 from the "
        "previous week's revised level of 207,000. Insured unemployment was 1,774,000.</p>"
        + "<p>filler text for length. </p>" * 80 + "</body></html>")

run("L-33 replay: fabricated 213,000 is NOT FOUND", body, ["--expect", "213,000"], 1, "NOT FOUND  213,000")
run("real figures FOUND", body, ["--expect", "206,000", "--expect", "1,774,000"], 0, "FOUND      206,000")
run("token boundary: 774,000 must not match inside 1,774,000", body, ["--expect", "774,000"], 1)
run("token boundary: 06,000 must not match inside 206,000", body, ["--expect", "06,000"], 1)
run("date line printed", body, [], 0, "September 17, 2026")
run("Akamai-style stub rejected", "<html><body>Access Denied. Reference #18.ab</body></html>" * 60, [], 2, "UNKNOWN")
run("tiny body rejected", "<html>ok</html>", [], 2, "stub")
run("random bytes rejected", bytes(range(256)) * 12, [], 2, "UNKNOWN", suffix=".pdf")
run("plain-text release accepted", "THE EMPLOYMENT SITUATION -- SEPTEMBER 2026\nTotal nonfarm payroll employment changed little (+29,000).\n" * 30, ["--expect", "29,000"], 0, suffix=".txt")
run("missing file is UNKNOWN", b"", [], 2)

print(f"\n{len(FAILED)} failure(s)")
sys.exit(1 if FAILED else 0)
