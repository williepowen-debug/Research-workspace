"""Independent, isolated review probes for CREED c6b0731c9. No owner writes."""
import csv
import io
import json
import pathlib
import subprocess
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[3]
REV = "c6b0731c9"


def git_file(path, rev=REV):
    return subprocess.check_output(["git", "show", f"{rev}:AGENTS/CREED/{path}"], cwd=REPO)


def read_rows(raw):
    return list(csv.DictReader((l for l in raw.decode().splitlines() if l and not l.startswith("#")), delimiter="\t"))


with tempfile.TemporaryDirectory(prefix="cato-creed-probe-") as tmp:
    home = pathlib.Path(tmp) / "AGENTS/CREED"
    paths = ["scripts/threshold_scan.py", "scripts/creed_selfcheck.py", "registry/THRESHOLDS.tsv",
             "registry/CREED_T_FIRED_LOG.tsv", "STATUS.md", "COVERAGE.md", "README.md", "CLAUDE.md", "thesis/THESIS.md"]
    paths += subprocess.check_output(["git", "ls-tree", "--name-only", REV, "AGENTS/CREED/workbook/"], cwd=REPO, text=True).splitlines()
    paths = [p.removeprefix("AGENTS/CREED/") for p in paths]
    for path in paths:
        dest = home / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(git_file(path))
    history = home / "workbook/VX_HISTORY.tsv"
    original = history.read_bytes()
    header = ["Vector_ID", "Date", "Value", "Status", "Notes", "Role", "Basis"]
    base = [["VX-CREED-1.01", f"2025-{m:02}", "11.5", "ORANGE", "fixture", "CANONICAL", "Trepp headline"] for m in range(1, 12)]

    def encode(rows, fields=header):
        out = io.StringIO()
        writer = csv.writer(out, delimiter="\t", lineterminator="\n")
        writer.writerow(fields)
        writer.writerows(rows)
        return out.getvalue().encode()

    def run(label, raw, expected):
        history.write_bytes(raw)
        scan = subprocess.run(["python3", str(home / "scripts/threshold_scan.py")], text=True, capture_output=True)
        check = subprocess.run(["python3", str(home / "scripts/creed_selfcheck.py")], text=True, capture_output=True)
        lines = [l.strip() for l in scan.stdout.splitlines() if "n=" in l and "VX-CREED-1.01" in l or "FAIL-LOUD" in l]
        print(json.dumps({"case": label, "expected": expected, "counter": lines, "scan_rc": scan.returncode,
                          "selfcheck_rc": check.returncode, "selfcheck_history": [l.strip() for l in check.stdout.splitlines() if "[history]" in l]}))

    run("live snapshot", original, "real sample 8 months; selfcheck clean")
    run("11 months", encode(base), "n=11, not due")
    duplicate = base[0].copy(); duplicate[5] = "DUPLICATE"
    run("11 plus excluded duplicate", encode(base + [duplicate]), "n=11, not due")
    december = base[0].copy(); december[1] = "2025-12"
    run("12 months", encode(base + [december]), "n=12, due")
    context = december.copy(); context[5] = "CONTEXT"
    run("11 plus context provider", encode(base + [context]), "n=11, not due")
    run("missing Role with data", encode([r[:5] for r in base], header[:5]), "fail loud")
    run("empty history", b"", "fail loud, not zero observations")
    run("header only without Role", encode([], header[:5]), "fail loud, not zero observations")
    daily = december.copy(); daily[1] = "2025-11-30"
    run("11 months plus same-month dated row", encode(base + [daily]), "reject mixed cadence; not 12 monthly observations")
    other = december.copy(); other[6] = "different denominator/provider"
    run("11 months plus different basis", encode(base + [other]), "reject mixed basis; not 12 comparable observations")
    malformed = december.copy(); malformed[1] = "2025-13"
    run("11 months plus impossible month", encode(base + [malformed]), "reject invalid observation period")
    no_basis = december.copy(); no_basis[6] = ""
    run("11 months plus blank basis", encode(base + [no_basis]), "reject missing basis")
    run("conflicting canonical duplicate", encode(base + [base[0][0:2] + ["99"] + base[0][3:]]), "selfcheck rejects; counter must not certify valid observations")
    history.write_bytes(original)
    for path in ["workbook/KB.tsv", "workbook/VX.tsv", "workbook/VX_HISTORY.tsv"]:
        (home / path).write_bytes(git_file(path, REV + "^"))
    old = subprocess.run(["python3", str(home / "scripts/creed_selfcheck.py")], text=True, capture_output=True)
    print(json.dumps({"case": "pre-fix data with new check", "rc": old.returncode,
                      "findings": [l.strip() for l in old.stdout.splitlines() if "[schema]" in l or "[band-vs-status]" in l or "[history]" in l]}))
