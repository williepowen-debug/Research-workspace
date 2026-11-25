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

# --- WQ-723 A (2026-11-25): one honest client string, one request, a refusal ends it ---
import subprocess as _sp


def fetch_case(name, stdout, want_path, want_calls=1):
    calls = []

    def fake_run(cmd, **kw):
        calls.append(cmd)
        return _sp.CompletedProcess(cmd, 0, stdout=stdout, stderr=b"")

    real = F.subprocess.run
    F.subprocess.run = fake_run
    try:
        path, tries = F.fetch("https://example.gov/x.htm", TMP)
    finally:
        F.subprocess.run = real
    ua_ok = all("-A" in c and c[c.index("-A") + 1] == "research-bot/1.0" for c in calls)
    no_browser = not any("Mozilla" in " ".join(c) for c in calls)
    ok = (len(calls) == want_calls and ua_ok and no_browser and (path is not None) == want_path)
    print(f"{'PASS' if ok else 'FAIL'}  {name}: {len(calls)} request(s), path {'set' if path else 'None'}, "
          f"tries {tries}")
    if not ok:
        FAILED.append(name)


fetch_case("403 refusal: exactly one request, honest UA, attempt ends", b"Forbidden" * 10 + b"403", False)
fetch_case("200 Akamai stub: one request, no second identity", ("<html>Access Denied</html>" * 100).encode() + b"200", False)
fetch_case("500 server error: no retry either", b"err" + b"500", False)
fetch_case("200 real page: one request, saved", body.encode() + b"200", True)
_src_ok = "Mozilla" not in pathlib.Path(F.__file__).read_text()
print(f"{'PASS' if _src_ok else 'FAIL'}  no browser string anywhere in the module source")
if not _src_ok:
    FAILED.append("browser string still in module source")

print(f"\n{len(FAILED)} failure(s)")
sys.exit(1 if FAILED else 0)
