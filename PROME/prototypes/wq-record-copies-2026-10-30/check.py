#!/usr/bin/env python3
"""Mechanical layer of the WQ-record comparison (design copies only).

Checks per copy: JSON parses · validates against CATO's draft schema (Draft 2020-12 + FormatChecker)
· unit ids belong to the parent wq · unit/source/choice ids unique · every source_id / option_id /
affected_unit_id / supersedes reference resolves · recommended option exists · every source path exists
in the working tree AND (when a commit is given) the commit exists and contains that path · wq_id matches
the file name. Structural validity is not an authority check (README § Semantic invariants).
Usage: python3 check.py <schema.json> <copy.json>... ; exit 1 on any failure.
"""
import hashlib, json, os, subprocess, sys
import jsonschema
from jsonschema import Draft202012Validator, FormatChecker

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()

def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def commit_has_path(commit, path):
    r = subprocess.run(["git", "cat-file", "-e", f"{commit}:{path}"], cwd=ROOT, capture_output=True)
    return r.returncode == 0

def check(schema, path):
    fails = []
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        return [f"JSON parse: {e}"]
    v = Draft202012Validator(schema, format_checker=FormatChecker())
    for err in sorted(v.iter_errors(d), key=lambda e: list(e.path)):
        fails.append(f"schema: {list(err.path)}: {err.message[:160]}")
    wq = d.get("wq_id")
    if os.path.basename(path) != f"WQ-{wq}.json":
        fails.append(f"file name does not match wq_id {wq}")
    src_ids = [s["id"] for s in d.get("sources", [])]
    if len(set(src_ids)) != len(src_ids):
        fails.append("duplicate source ids")
    unit_ids = [u["id"] for u in d.get("units", [])]
    if len(set(unit_ids)) != len(unit_ids):
        fails.append("duplicate unit ids")
    for u in d.get("units", []):
        uid = u["id"]
        if not uid.startswith(f"{wq}."):
            fails.append(f"{uid}: unit id not under wq {wq}")
        cids = [c["id"] for c in u["proposal"]["choices"]]
        if len(set(cids)) != len(cids):
            fails.append(f"{uid}: duplicate choice ids")
        rec = u["proposal"]["recommendation"]
        if rec["option_id"] is not None and rec["option_id"] not in cids:
            fails.append(f"{uid}: recommended option {rec['option_id']} not among choices {cids}")
        for sid in u["proposal"]["source_ids"] + u["disposition"]["source_ids"]:
            if sid not in src_ids:
                fails.append(f"{uid}: source_id {sid} unresolved")
        r = u["disposition"]["ruling"]
        if r:
            if r["source_id"] not in src_ids:
                fails.append(f"{uid}: ruling.source_id {r['source_id']} unresolved")
            for sid in r["proposal_source_ids"]:
                if sid not in src_ids:
                    fails.append(f"{uid}: ruling.proposal_source_ids {sid} unresolved")
            if r["selected_option_id"] is not None and r["selected_option_id"] not in cids:
                fails.append(f"{uid}: selected option {r['selected_option_id']} not among choices")
        for ft in u["follow_through"]:
            if ft["source_id"] not in src_ids:
                fails.append(f"{uid}: follow_through.source_id {ft['source_id']} unresolved")
        if u["supersedes_unit_id"] is not None and u["supersedes_unit_id"] not in unit_ids:
            fails.append(f"{uid}: supersedes {u['supersedes_unit_id']} unresolved")
    for c in d.get("corrections", []):
        if c["source_id"] not in src_ids:
            fails.append(f"correction source_id {c['source_id']} unresolved")
        for a in c["affected_unit_ids"]:
            if a not in unit_ids:
                fails.append(f"correction affects unknown unit {a}")
    for s in d.get("sources", []):
        p = s["path"]
        if ".." in p.split("/") or p.startswith("/"):
            fails.append(f"source {s['id']}: path outside the workspace form: {p}")
            continue
        if not os.path.exists(os.path.join(ROOT, p)):
            fails.append(f"source {s['id']}: path missing in working tree: {p}")
        if s["commit"] and not commit_has_path(s["commit"], p):
            fails.append(f"source {s['id']}: commit {s['commit'][:9]} does not contain {p}")
    return fails

def main():
    schema_path, copies = sys.argv[1], sys.argv[2:]
    schema = json.load(open(schema_path, encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    print(f"schema {os.path.basename(schema_path)} sha256 {sha256(schema_path)} — valid for its dialect")
    rc = 0
    for c in copies:
        f = check(schema, c)
        print(f"{os.path.basename(c)} sha256 {sha256(c)}: {'PASS' if not f else 'FAIL'}")
        for x in f:
            print("   ❌", x); rc = 1
    sys.exit(rc)

if __name__ == "__main__":
    main()
