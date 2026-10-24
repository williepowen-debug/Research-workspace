#!/usr/bin/env python3
"""Bounded CATO result read. Only evidence output and temporary fixtures are written."""
import ast
import csv
import datetime as dt
import hashlib
import io
import json
import subprocess
import tempfile
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
PIN = "3b3e6afa82bc92923b2b8fc5484f6803fbadf5a0"
INSTALL = "748388a3a4ef3c06d6c481dc7f361097c25a3afa"
SOURCE = "PROME/tools/prome_gate.py"
TODAY = dt.date(2026, 10, 23)


def git_bytes(ref, path):
    return subprocess.check_output(["git", "show", f"{ref}:{path}"], cwd=ROOT)


def module(ref):
    text = git_bytes(ref, SOURCE).decode()
    m = types.ModuleType("cato_review_gate")
    m.__file__ = str(ROOT / SOURCE)
    exec(compile(text, m.__file__, "exec"), m.__dict__)
    return m


def digest(data):
    return hashlib.sha256(data).hexdigest()


def ledger(rows, violet=False):
    out = io.StringIO()
    writer = csv.writer(out, delimiter="\t", lineterminator="\n")
    writer.writerow(["date", "event", "expected_vol_impact" if violet else "priority", "notes"])
    writer.writerows(rows)
    return out.getvalue()


def execute(m, contents, today=TODAY, collide=False, bad_log=False):
    with tempfile.TemporaryDirectory(prefix="cato-l628-") as temp:
        root = Path(temp)
        logs = root / "logs"
        logs.mkdir()
        m.ROOT, m.LOG_DIR, m.results = root, logs, []
        m.SUMMONS_LEDGERS = {name: f"{name}.tsv" for name in contents}
        m.SUMMONS_WINDOW_DAYS, m.EMPTY_FORWARD_DAYS = 2, 14
        for name, content in contents.items():
            if content is not None:
                (root / f"{name}.tsv").write_bytes(content.encode() if isinstance(content, str) else content)
        collision = None
        if collide:
            collision = m._check_log_path("desk catalyst summons (BD-02)")
            collision.write_text("earlier evidence\n")
        if bad_log:
            m.LOG_DIR = root / "missing" / "logs"
        # The pre-install function had no injected clock; isolate its datetime module.
        class FixedDate(dt.date):
            @classmethod
            def today(cls):
                return today
        m.dt = types.SimpleNamespace(date=FixedDate, timedelta=dt.timedelta)
        m.check_desk_catalyst_summons()
        severity, name, ok, detail, owner = m.results[-1]
        body = ""
        if "full output: " in detail and "full output: UNAVAILABLE" not in detail:
            body = Path(detail.split("full output: ", 1)[1]).read_text()
        if collision:
            assert collision.read_text() == "earlier evidence\n"
        return dict(severity=severity, name=name, ok=ok, detail=detail,
                    log=body, owner=owner, gate_rc=m.aggregate_rc(m.results, []))


current, before = module(PIN), module(INSTALL + "^")
checks = {}
# Original WP28, with an unrelated forward row suppressing EMPTY-FORWARD noise.
original = {
    "VULCAN": ledger([(f"2026-10-{d:02}", f"old-{d}", "P1", "") for d in range(1, 5)]
                     + [("2026-10-30", "future", "P1", "")]),
    "VIOLET": ledger([("2026-10-24", "VIOLET-WITNESS", "HIGH", "")], violet=True),
}
old_result, new_result = execute(before, original), execute(current, original)
assert "VIOLET-WITNESS" not in old_result["detail"]
assert new_result["detail"].startswith("VIOLET 2026-10-24 [HIGH] VIOLET-WITNESS")
checks["original_WP28_pre_fails_post_passes"] = dict(before=old_result, after=new_result)

# Independent case: dozens of window rows from six registrants, plus missing/unreadable
# ledgers, large backlog and equal-date ties. Expectations come from fixture identities.
mixed = {}
expected = []
for desk in ["LABOR", "VULCAN", "VIOLET", "CYPHER", "GIBBS", "ISHM"]:
    rows = [("2026-09-01", f"old-{desk}-{i}", "P1", "") for i in range(40)]
    for day in range(3):
        for i in range(4):
            event = f"due-{desk}-{day}-{i}"
            rows.append(((TODAY + dt.timedelta(days=day)).isoformat(), event, "HIGH", ""))
            expected.append(event)
    rows.append(("2026-10-26", f"outside-{desk}", "P1", ""))
    mixed[desk] = ledger(rows, violet=desk == "VIOLET")
mixed.update(MISSING=None, UNREADABLE=b"\xff\xfe")
r = execute(current, mixed)
assert all(r["detail"].count(event + " (") == 1 for event in expected)
assert all(event in r["log"] for event in expected)
assert all(f"old-{desk}-{i}" in r["log"] for desk in list(mixed)[:6] for i in range(40))
assert max(r["detail"].index(event) for event in expected) < r["detail"].index("MISSING ledger")
assert r["detail"].index("UNREADABLE unreadable") < r["detail"].index("past-due")
assert "outside-" not in r["detail"] and "(+" not in r["detail"]
assert r["severity"] == "advisory" and r["gate_rc"] == 0 and not r["ok"]
checks["mixed_72_due_240_past_2_unavailable"] = r
for name, options in [("exclusive_log_collision", dict(collide=True)),
                      ("missing_log_directory", dict(bad_log=True))]:
    r = execute(current, mixed, **options)
    assert "full output: UNAVAILABLE" in r["detail"]
    assert all(event in r["detail"] for event in expected)
    checks[name] = r

# Shared logging routine: a prior script result consumes index zero; summons uses one.
with tempfile.TemporaryDirectory(prefix="cato-l628-shared-") as temp:
    current.ROOT, current.LOG_DIR, current.results = Path(temp), Path(temp), []
    current.SUMMONS_LEDGERS = {"ABSENT": "absent.tsv"}
    current.run_script(current.ADVISE, "harmless probe", ["/bin/echo", "known output"], "CATO test fixture")
    current.check_desk_catalyst_summons(today=TODAY)
    names = sorted(p.name for p in Path(temp).glob("*.txt"))
    assert len(names) == 2 and names[0].startswith("00-") and names[1].startswith("01-")
    checks["shared_log_index"] = names

# Real producer records: frozen bytes from all six registrants, not hand-made schemas.
prod = module(PIN).SUMMONS_LEDGERS
snapshots = OUT / "ledgers"
snapshots.mkdir(exist_ok=True)
contents, manifest, expected_real = {}, {}, []
for desk, path in prod.items():
    data = git_bytes(PIN, path)
    (snapshots / f"{desk}.tsv").write_bytes(data)
    contents[desk] = data
    manifest[desk] = dict(path=path, sha256=digest(data))
    for row in csv.DictReader(io.StringIO(data.decode()), delimiter="\t"):
        raw = row.get("date", "").strip()
        try:
            date = dt.date.fromisoformat(raw[:10])
        except ValueError:
            continue
        if TODAY <= date <= TODAY + dt.timedelta(days=2):
            expected_real.append((desk, raw[:10], row["event"][:45]))
r = execute(current, contents)
for desk, date, event in expected_real:
    assert f"{desk} {date}" in r["detail"] and event in r["detail"] and event in r["log"]
checks["frozen_real_producers"] = dict(expected_due=expected_real, manifest=manifest, result=r)

# Retain the already-declared parser/coverage limits; these do not reopen L548.
residue = {}
r = execute(current, {"DESK": ledger([("TBD", "undated", "P1", ""), ("2026-10-30", "near", "P1", "")])})
assert r["ok"] and not r["log"]
residue["undated_with_forward_row_quiet"] = r
r = execute(current, {"DESK": ledger([("2026-02-30", "invalid", "P1", ""), ("2026-10-23", "later_valid", "P1", "")])})
assert "unreadable: ValueError" in r["detail"] and "later_valid" not in r["detail"]
residue["invalid_date_aborts_ledger"] = r

receipt = dict(pin=PIN, installed=INSTALL, source_sha256=digest(git_bytes(PIN, SOURCE)),
               checks=checks, preserved_residue=residue, verdict="ACCEPT-WITH-RESIDUE",
               scope="L548/L628 display repair and WP28; no operational boot or desk launch")
(OUT / "verification.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(dict(verdict=receipt["verdict"], checks=list(checks),
                      real_due_rows=len(expected_real), residue=list(residue)), indent=2))
