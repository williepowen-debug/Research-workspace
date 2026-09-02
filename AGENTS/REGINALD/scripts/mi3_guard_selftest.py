#!/usr/bin/env python3
"""Falsifier for the MI3 screen's guards — run the falsifier BEFORE trusting the guard.

A guard nobody has seen FAIL is an assumption, not a control. This asserts each
guard trips on the exact defect it exists to catch, that a DECLARED restatement is
still allowed through, and that the live 56-row output produces no false positive.

Usage: python3 AGENTS/REGINALD/scripts/mi3_guard_selftest.py    (exit 0 = all pass)
Reads the committed MI3_COHORT.tsv; makes no network calls and writes nothing.
"""
import copy
import csv
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("mi3", HERE / "mi3_cohort_screen.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

results = []


def load():
    rows = [{k: (v if v != "" else None) for k, v in r.items()}
            for r in csv.DictReader(m.decomment(open(m.OUT_TSV).read().splitlines()),
                                    delimiter="\t")]
    for r in rows:
        for c in ("v1_pct", "v1a_pct"):
            if r.get(c) is not None:
                r[c] = float(r[c])
        if r.get("mi3_k") is not None:
            r["mi3_k"] = int(r["mi3_k"])
    return rows


def expect_trip(label, fn):
    try:
        fn()
        results.append((False, label + " — guard did NOT trip"))
    except m.GuardTripped:
        results.append((True, label))


def expect_pass(label, fn):
    try:
        fn()
        results.append((True, label))
    except m.GuardTripped as e:
        results.append((False, f"{label} — wrongly blocked: {e}"))


def main():
    rows = load()
    if len(rows) != len(m.COHORT) * len(m.QUARTERS):
        print("selftest needs a full committed MI3_COHORT.tsv", file=sys.stderr)
        return 2

    def mut(**kw):
        r = copy.deepcopy(rows)
        r[5].update(kw)
        return r

    expect_trip("T1 blank ratio on a scored row (the fabricated-clean-result class)",
                lambda: m.schema_guard(mut(v1_pct=None)))
    expect_trip("T2 status=OK with no v1a (the 031/RCFD resolver regressed)",
                lambda: m.schema_guard(mut(v1a_pct=None)))
    expect_trip("T3 unscored status still carrying numbers (a None printed as 0)",
                lambda: m.schema_guard(mut(status="NOT-REPORTED")))
    expect_trip("T4 status outside the state vocabulary",
                lambda: m.schema_guard(mut(status="FINE")))
    expect_trip("T5 coverage short by one bank-quarter (silent drop)",
                lambda: m.coverage_guard(copy.deepcopy(rows)[:-1]))

    # ⚠️ The mutated row MUST be one that EXISTS in the prior committed vintage, or the
    # guard correctly classifies it NEW and the test silently passes on a false negative.
    # Found 2026-08-13 when the grid was extended to 12 contiguous quarters: row[0] became
    # a brand-new quarter and T6 stopped tripping. A positional pick is not a stable
    # selector once the row set can grow — select by MEMBERSHIP in the prior vintage.
    prior_keys = set(m.load_prior())
    target = next((i for i, r in enumerate(rows)
                   if (r["ticker"], r["quarter"]) in prior_keys
                   and r["status"] in m.SCORED_STATUSES), None)
    if target is None:
        print("selftest cannot run T6/T7: no overlap with the prior committed vintage",
              file=sys.stderr)
        return 2

    def restated():
        r = copy.deepcopy(rows)
        r[target]["v1_pct"] = 37.6
        r[target]["mi3_k"] = 999999
        return r

    expect_trip("T6 published cell stops reproducing, UNDECLARED (the 37.6% class)",
                lambda: m.repro_guard(restated(), m.load_prior(), ""))
    expect_pass("T7 same restatement, DECLARED with a reason — allowed and recorded",
                lambda: m.repro_guard(restated(), m.load_prior(), "FFIEC amended filing"))

    def clean():
        m.coverage_guard(rows)
        m.schema_guard(rows)
        m.repro_guard(copy.deepcopy(rows), m.load_prior(), "")

    expect_pass("T8 the live committed output passes all three guards (no false positive)",
                clean)

    for ok, label in results:
        print(("  ✅ " if ok else "  ❌ ") + label)
    bad = sum(1 for ok, _ in results if not ok)
    print(f"\n{len(results) - bad}/{len(results)} passed")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
