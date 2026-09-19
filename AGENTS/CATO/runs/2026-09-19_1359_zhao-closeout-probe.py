"""Read-only checks of ZHAO's committed closeout, pinned to its reported revision.

These check record properties and reproduce conflicting text; they do not validate
legal interpretation. Primary-source assessment is in the accompanying review.
"""
import csv
import io
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REV = "c0092ebad059e69ee54dccf9058ecead65e6b2aa"
BASE = "a7e284a4b^"


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True)


def read(path, rev=REV):
    return git("show", f"{rev}:{path}")


def rows(path, rev=REV):
    return list(csv.DictReader(io.StringIO(read(path, rev)), delimiter="\t"))


def check(label, condition):
    print(f"{'PASS' if condition else 'FAIL'}: {label}")
    if not condition:
        raise AssertionError(label)


print("Pinned revision:", REV)
pred = "AGENTS/ZHAO/workbook/PREDICTIONS.tsv"
check("prediction ledger byte-for-byte unchanged during reviewed session", read(pred) == read(pred, BASE))
for row in rows(pred):
    if row.get("Pred_ID") in {"ZHA-16", "ZHA-18"}:
        print("Prediction:", {k: row.get(k) for k in ("Pred_ID", "Status", "Resolve_By")})

kbpath = "AGENTS/ZHAO/workbook/KB.tsv"
old = {r["ID"]: r for r in rows(kbpath, BASE)}
new = {r["ID"]: r for r in rows(kbpath)}
check("KB-172 through KB-176 present", all(f"KB-ZHAO-{n}" in new for n in range(172, 177)))
parent, original = new["KB-ZHAO-166"], old["KB-ZHAO-166"]
check("KB-166 status CORRECTED", parent["Status"] == "CORRECTED")
check("KB-166 original Fact preserved verbatim", parent["Fact"] == original["Fact"])
check("KB-166 original Notes preserved verbatim after correction", parent["Notes"].endswith(original["Notes"]))
check("KB-166 correction appears before original Notes", parent["Notes"].index("CORRECTED") < parent["Notes"].index(original["Notes"]))

for path in [kbpath, "AGENTS/ZHAO/workbook/FLOW.tsv", "AGENTS/ZHAO/docket/CATALYSTS.tsv"]:
    data = list(csv.reader(io.StringIO(read(path)), delimiter="\t"))
    check(f"TSV widths: {path}", all(len(r) == len(data[0]) for r in data[1:] if r))
cats = rows("AGENTS/ZHAO/docket/CATALYSTS.tsv")
check("all catalyst date_class values in reader enum", all(r.get("date_class", "").strip() in {"", "confirmed", "external", "estimated", "modeled"} for r in cats))

status = "AGENTS/ZHAO/STATUS.md"
brief = "AGENTS/ZHAO/NEXUS_BRIEF.md"
last_status = git("log", "-1", "--format=%H", REV, "--", status).strip()
last_brief = git("log", "-1", "--format=%H", REV, "--", brief).strip()
print("Last STATUS / brief commits:", last_status, last_brief)
check("STATUS commit is ancestor of final brief commit", subprocess.run(["git", "-C", str(ROOT), "merge-base", "--is-ancestor", last_status, last_brief]).returncode == 0)
check("brief commit timestamp >= STATUS timestamp", int(git("show", "-s", "--format=%ct", last_brief)) >= int(git("show", "-s", "--format=%ct", last_status)))
for path in [status, brief]:
    data = read(path)
    print("Size:", path, len(data.splitlines()), "lines,", len(data.encode()), "bytes")

for path, before, prefix, archive in [
    (status, "a89c6cce6^", "*(9/18 — the 11/10 escalation", "AGENTS/ZHAO/archive/STATUS_COLD_20260918b.md"),
    (brief, "068e753c7^", "- **⚠️ 9/18 — AND ZHAO BROKE", "AGENTS/ZHAO/archive/NEXUS_BRIEF_PIVOT_HISTORY_20260919.md"),
    (brief, "fad167a5a^", "**Recent thesis pivot:**", "AGENTS/ZHAO/archive/NEXUS_BRIEF_PIVOT_HISTORY_20260919.md"),
]:
    line = next(l for l in read(path, before).splitlines() if l.startswith(prefix))
    check(f"rotated line preserved verbatim: {prefix}", line in read(archive))
    check(f"live file points to archive: {path}", Path(archive).name in read(path) or "COLD_20260918b" in read(path))

print("\nConflicting live brief passages (full individual lines):")
for number in [17, 18, 19, 28, 69, 92, 93, 98]:
    print(f"{brief}:{number}: {read(brief).splitlines()[number-1]}")
decision = "PROME/inbox/2026-09-19_from-ZHAO_DECISION-battery-leg-allocation.md"
print("\nBattery decision excerpt:")
for number, line in enumerate(read(decision).splitlines(), 1):
    if "three legs" in line or "equipment + anode only" in line or "artificial-graphite" in line:
        print(f"{decision}:{number}: {line}")
print("Cathode / 正极 mentioned in decision:", any(t in read(decision).lower() for t in ["cathode", "正极"]))
print("\nRESULT: mechanical checks passed; reproduced semantic conflicts require owner correction.")
