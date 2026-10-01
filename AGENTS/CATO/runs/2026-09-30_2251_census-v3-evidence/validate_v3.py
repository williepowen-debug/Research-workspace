"""CATO's bounded validation of the supplied census, without owner-file writes.

Run from the repository root: python3 -B <this-file> [--replay]
--replay executes the preserved original after changing only its OUT assignment
to a temporary directory, always supplying the exact pinned commit explicitly.
Default run checks counts, calculations and selected source/history witnesses.
Outputs validation.json beside this file. No network or Git mutation.
"""
import collections
import csv
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PIN = "e70f558f4ad685cec394a9cdc2ef6ee622d6b6e0"
HOME = Path(__file__).resolve().parent


def git(*args):
    return subprocess.check_output(["git", *args], text=True)


def table(sha, path):
    text = git("show", f"{sha}:{path}")
    return list(csv.DictReader(io.StringIO(text), delimiter="\t"))


def row(sha, path, wanted):
    for r in table(sha, path):
        key = next((r[k] for k in ("ID", "Pred_ID", "id", "pred_id") if k in r), None)
        if key == wanted:
            return {"commit": sha, "path": path, "row": r}
    raise AssertionError((sha, path, wanted))


def metrics(rows, field):
    n = len(rows)
    outcomes = [r["class"] == "CONFIRMED" for r in rows]
    base = sum(outcomes) / n
    bs = sum((float(r[field]) - y) ** 2 for r, y in zip(rows, outcomes)) / n
    ref = base * (1 - base)
    return {"n": n, "brier": bs, "base_rate": base, "baseline": ref, "skill": 1-bs/ref}


rows = list(csv.DictReader((HOME / "rows_v3.tsv").open(), delimiter="\t"))
by_key = {(r["desk"], r["pred_id"]): r for r in rows}
assert len(by_key) == len(rows) == 534
scored = [r for r in rows if not r["exclusion_reason"]]
matched = [r for r in scored if r["p_first_committed"]]
reasons = collections.Counter(
    r["exclusion_reason"] + (":" + r["sub_reason"] if r["exclusion_reason"] == "open" else "")
    for r in rows if r["exclusion_reason"]
)
assert len(scored) == 235 and len(matched) == 234
assert sum(reasons.values()) == 299
result = {
    "pin": PIN,
    "counts": {"total": len(rows), "scored": len(scored), "excluded": dict(reasons)},
    "metrics": {
        "current_cells_all": metrics(scored, "p_scored"),
        "current_cells_matched": metrics(matched, "p_scored"),
        "purported_first_matched": metrics(matched, "p_first_committed"),
    },
    "scored_without_first": [(r["desk"],r["pred_id"]) for r in scored if not r["p_first_committed"]],
    "distinct_stored_other_statuses": len({r["status_raw"] for r in rows if r["class"] == "OTHER"}),
    "witnesses": {},
}
w = result["witnesses"]
otto = "AGENTS/OTTO/thesis/PREDICTIONS.tsv"
for pid in ("OTTO-04", "OTTO-06", "OTTO-10", "OTTO-29", "OTTO-32"):
    w[pid] = {"census": by_key[("OTTO",pid)], "source": row(PIN,otto,pid)}
assert w["OTTO-32"]["census"]["brier_scored"] == "0.0009"
assert "Brier 0.0225 is counted" in w["OTTO-32"]["source"]["row"]["Result"]
assert w["OTTO-06"]["census"]["exclusion_reason"] == ""
assert "CALIBRATION ELIGIBILITY: NOT ELIGIBLE" in w["OTTO-06"]["source"]["row"]["Result"]
assert "Brier 0.5625 is counted" in w["OTTO-29"]["source"]["row"]["Result"]
for pid, sha in (("OTTO-05","91c301279"),("OTTO-29","0bc51c74d"),("OTTO-30","0bc51c74d")):
    w[pid+"_earlier"] = {"census": by_key[("OTTO",pid)], "source": row(sha,"AGENTS/OTTO/workbook/PREDICTIONS.tsv",pid)}
assert w["OTTO-05_earlier"]["source"]["row"]["Confidence"] == "60%"
assert w["OTTO-05_earlier"]["census"]["p_first_committed"] == "0.48"
assert w["OTTO-29_earlier"]["source"]["row"]["Confidence"] == "75%"
assert w["OTTO-29_earlier"]["census"]["p_first_committed"] == "0.80"
w["VULCAN-01"] = {
    "census": by_key[("VULCAN","VULCAN-01")],
    "source": row("c5c055f82","AGENTS/VULCAN/workbook/PREDICTIONS.tsv","VULCAN-01"),
}
assert w["VULCAN-01"]["census"]["first_commit_date"] == "2026-09-06"
assert w["VULCAN-01"]["source"]["row"]["made"] == "2026-07-10"
birth = git("log",PIN,"--reverse","--format=%H","--","AGENTS/BOND/thesis/PREDICTIONS.tsv").splitlines()[0]
w["BND-01_birth"] = {
    "census": by_key[("BOND","BND-01")],
    "first_source_commit": birth,
    "source": row(birth,"AGENTS/BOND/thesis/PREDICTIONS.tsv","BND-01"),
    "predecessor": row(birth+"^","AGENTS/BOND/workbook/PREDICTIONS.tsv","BND-01"),
}
assert birth.startswith(by_key[("BOND","BND-01")]["first_commit_sha"])
assert by_key[("BOND","BND-01")]["first_seen_is_file_birth"] == "0"
# Ordinary population controls: the rotated rows really exist and retain the
# numeric cells/statuses extracted. This does not verify external outcomes.
for pid in ("BND-01","BND-18","BND-29"):
    r = by_key[("BOND",pid)]
    source = row(PIN,r["file"],pid)
    assert source["row"]["Confidence"] == r["confidence_raw"]
    assert source["row"]["Status"] == r["status_raw"]
    w[pid+"_rotation_control"] = source
result["bond_population"] = dict(collections.Counter(r["class"] for r in rows if r["desk"]=="BOND"))

tour = "AGENTS/MARCO/sub_agents/TOURISM/workbook/PREDICTIONS.tsv"
raw = list(csv.reader(io.StringIO(git("show",PIN+":"+tour)),delimiter="\t"))
header = raw[0]
for fields in raw[1:]:
    if fields[0] in ("TOUR-02","TOUR-04"):
        w[fields[0]+"_schema"] = {"path":tour,"header":header,"fields":fields,"census":by_key[("MARCO/TOURISM",fields[0])]}
        assert len(fields) == 6 and len(header) == 7
        assert by_key[("MARCO/TOURISM",fields[0])]["status_raw"] == "2026-05-31"

if "--replay" in sys.argv:
    with tempfile.TemporaryDirectory(prefix="cato-census-v3-") as temp:
        original = (HOME / "census_v3.py").read_text()
        lines = original.splitlines(keepends=True)
        assert sum(line.startswith("OUT = ") for line in lines) == 1
        code = "".join(f"OUT = {str(Path(temp)) + '/'!r}\n" if line.startswith("OUT = ") else line for line in lines)
        runner = Path(temp) / "portable.py"
        runner.write_text(code)
        run = subprocess.run([sys.executable,"-B",str(runner),PIN],capture_output=True,text=True,check=True)
        result["replay_byte_equal"] = {
            name: (Path(temp)/name).read_bytes() == (HOME/name).read_bytes()
            for name in ("rows_v3.tsv","summary_v3.tsv","provenance_v3.txt")
        }
        assert all(result["replay_byte_equal"].values())
        (HOME / "replay-stdout.txt").write_text(run.stdout)
(HOME / "validation.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({k:v for k,v in result.items() if k != "witnesses"},indent=2))
print("Selected witnesses and assertions reproduced; full evidence in validation.json.")
