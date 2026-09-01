#!/usr/bin/env python3
"""reads_check.py — validate PROME/registry/READS.tsv and measure what it declares.

WHAT THIS IS. READS.tsv is the DECLARED boot-read manifest (Will-ruled 2026-09-01; built
2026-08-31). This tool is its validator and its measuring instrument. It does NOT own the byte
budget — `scripts/read_cap_check.py` owns the constants and this file imports them, per
READ_CAP.md ("constants live there and nowhere else").

WHAT A PASS PROVES, AND WHAT IT DOES NOT.
  rc=0 means: this desk ATTESTED its manifest complete, AND every cap-bearing row in that manifest
  is under budget. It is a claim about the DECLARATION, not about the desk. If the declaration is
  wrong the verdict is wrong, which is why every row carries `declared_by`.

  ⛔ A DESK WITH NO ATTESTATION ROW CAN NEVER SCORE rc=0. It reports UNKNOWN. Reporting clean over
  a partial perimeter is the exact defect this registry was built to retire
  (`finding_instrument_reports_clean_against_the_wrong_reference`).

RULING 1 IS NOT A DUPLICATE BUG. One path may appear under several readers, and under one reader at
several boot steps. Both are CORRECT and are never flagged.

Exit contract (CHECK_STANDARD §9): 0 clean · 1 FINDINGS · 2 CANNOT-EVALUATE.
  Precedence: a real breach outranks an incomplete perimeter (rc=1), because rc=1 demands action;
  a desk with no breaches and no attestation is rc=2, never rc=0.

Usage (cwd-proof):
    python3 "$(git rev-parse --show-toplevel)/PROME/tools/reads_check.py" --agent WALTER
    python3 "$(git rev-parse --show-toplevel)/PROME/tools/reads_check.py" --fleet
    python3 "$(git rev-parse --show-toplevel)/PROME/tools/reads_check.py" --selftest
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
REGISTRY = os.path.join(ROOT, "PROME", "registry", "READS.tsv")

sys.path.insert(0, os.path.join(ROOT, "scripts"))
try:
    from read_cap_check import BUDGET_BYTES, CAP_BYTES, ROTATE_AT   # single owner of the constants
except Exception as exc:                                      # pragma: no cover - import guard
    sys.stderr.write(f"CANNOT-EVALUATE: could not import constants from scripts/read_cap_check.py: {exc}\n")
    sys.exit(2)

COLUMNS = ["row_kind", "reader", "path", "mode", "source_boot_step",
           "declared_by", "declared_on", "notes"]
CAP_BEARING = {"whole", "programmatic"}
DECLARED_NOT_BEARING = {"scoped", "grep", "summary"}
VALID_READ_MODES = CAP_BEARING | DECLARED_NOT_BEARING
ATTEST_MODE = "manifest-complete"
RETIRED_RE = re.compile(r"^RETIRED-\d{4}-\d{2}-\d{2}$")
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class Row(dict):
    pass


def parse(text, source="READS.tsv"):
    """Return (rows, schema_errors). Comment lines and the header are stripped."""
    rows, errors = [], []
    header_seen = False
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        fields = line.split("\t")
        if not header_seen:
            if fields != COLUMNS:
                errors.append(f"{source}:{n}: header is {fields}, expected {COLUMNS}")
            header_seen = True
            continue
        if len(fields) != len(COLUMNS):
            errors.append(f"{source}:{n}: {len(fields)} fields, expected {len(COLUMNS)}")
            continue
        row = Row(zip(COLUMNS, fields))
        row["_line"] = n
        kind, mode = row["row_kind"], row["mode"]
        if kind not in ("READ", "ATTESTATION"):
            errors.append(f"{source}:{n}: row_kind '{kind}' is not READ or ATTESTATION")
        elif kind == "ATTESTATION" and mode != ATTEST_MODE:
            errors.append(f"{source}:{n}: ATTESTATION row must carry mode '{ATTEST_MODE}', got '{mode}'")
        elif kind == "READ" and mode not in VALID_READ_MODES and not RETIRED_RE.match(mode):
            errors.append(f"{source}:{n}: mode '{mode}' not in {sorted(VALID_READ_MODES)} or RETIRED-<ISO date>")
        if not ISO_RE.match(row["declared_on"]):
            errors.append(f"{source}:{n}: declared_on '{row['declared_on']}' is not ISO YYYY-MM-DD")
        for required in ("reader", "path", "source_boot_step", "declared_by"):
            if not row[required].strip():
                errors.append(f"{source}:{n}: '{required}' is empty")
        rows.append(row)
    if not header_seen:
        errors.append(f"{source}: no header row found")
    # A row is a duplicate only on the WHOLE key. Same path / different reader (ruling 1) and same
    # path / same reader / different boot step are both legitimate and must never be flagged.
    seen = {}
    for row in rows:
        key = (row["row_kind"], row["reader"], row["path"], row["mode"], row["source_boot_step"])
        if key in seen:
            errors.append(f"{source}:{row['_line']}: exact duplicate of line {seen[key]} (same reader, path, mode AND step)")
        seen[key] = row["_line"]
    return rows, errors


def size_of(path):
    try:
        return os.path.getsize(os.path.join(ROOT, path))
    except OSError:
        return None


def attested(rows, agent):
    """A desk's attestation must be the DESK's OWN word: declared_by == reader.

    Matching on `reader` alone defeats the ⛔ rule it is supposed to enforce — anyone can type an
    ATTESTATION row for anyone, and the registry already ships `PROME(from-charter)` rows, so the
    loophole is in live use in the same file. PROME may TRANSCRIBE a desk's attestation (no desk can
    commit inside PROME/), but it then writes the READER's name here and cites the desk's statement
    in notes. `PROME(from-charter)` is inference, never attestation. Found by a blind cold reader
    who constructed the bypass row, 2026-08-31.
    """
    return next((r for r in rows
                 if r["row_kind"] == "ATTESTATION"
                 and r["reader"] == agent
                 and r["declared_by"].strip() == agent), None)


def unsigned_attestations(rows, agent):
    """ATTESTATION rows for `agent` that are NOT the agent's own word — reported, never silently dropped."""
    return [r for r in rows if r["row_kind"] == "ATTESTATION" and r["reader"] == agent
            and r["declared_by"].strip() != agent]


def report_agent(rows, agent, errors):
    reads = [r for r in rows if r["row_kind"] == "READ" and r["reader"] == agent]
    att = attested(rows, agent)
    if not reads and not att:
        print(f"❓ READS [{agent}]: NO DECLARED ROWS — this desk's perimeter is UNKNOWN, not clean.")
        print("   → the reader declares its own manifest: packet PROME/inbox/ with reader · path · mode · source_boot_step")
        return 2

    bearing = [r for r in reads if r["mode"] in CAP_BEARING]
    declared_only = [r for r in reads if r["mode"] in DECLARED_NOT_BEARING]
    retired = [r for r in reads if RETIRED_RE.match(r["mode"])]
    unsigned = unsigned_attestations(rows, agent)
    stamp = f"ATTESTED {att['declared_on']} by {agent} itself" if att else "⛔ NOT ATTESTED"
    # Retired rows are counted separately and never folded into the measured total: an earlier
    # version said "manifest of N declared read(s) is under budget" while N included rows it had
    # measured nothing about.
    print(f"READS [{agent}] — budget {BUDGET_BYTES:,} B · cap {CAP_BYTES:,} B · perimeter: "
          f"{len(bearing)} cap-bearing + {len(declared_only)} declared-not-bearing = {len(bearing) + len(declared_only)} live read(s)"
          f"{f' (+{len(retired)} RETIRED, not measured)' if retired else ''} · manifest {stamp}")
    for row in unsigned:
        print(f"  ⛔ INVALID ATTESTATION line {row['_line']}: signed by '{row['declared_by']}', not by {agent}. "
              f"Only the reader can attest its own manifest — this row does NOT clear the desk.")

    findings, missing = [], []
    for row in sorted(bearing, key=lambda r: -(size_of(r["path"]) or 0)):
        size = size_of(row["path"])
        if size is None:
            missing.append(row)
            continue
        pct = size / BUDGET_BYTES
        # A flat ✅ up to 100% is itself a clean-report failure: it renders 98%-of-budget and
        # 13%-of-budget identically. READ_CAP.md rule 5 puts the rotation tier at ≥75%.
        if size >= CAP_BYTES:
            mark, tail = "🔴", "  OVER THE PHYSICAL CAP"
        elif size >= BUDGET_BYTES:
            mark, tail = "⚠️ ", "  OVER BUDGET"
        elif pct >= ROTATE_AT:
            mark, tail = "🟠", f"  ROTATE-TIER (≥{ROTATE_AT:.0%} of budget, READ_CAP.md rule 5)"
        else:
            mark, tail = "✅", ""
        print(f"  {mark} {row['path']:<52} {size:>9,} B  {pct:>5.0%} of budget   ({row['mode']}, {row['source_boot_step']}){tail}")
        if size >= BUDGET_BYTES:
            findings.append((row, size))
    for row in declared_only:
        size = size_of(row["path"])
        if size is None:
            missing.append(row)
            continue
        # Two DIFFERENT dispositions, and collapsing them over-claims against ledgers:
        #   scoped  → READ_CAP.md rule 8. A scoped read that replaced a whole read is a PARTIAL fix:
        #             honest about the operation, but the file is still over budget for anyone who
        #             needs it whole, so the owner still owes a split or a dated re-trigger.
        #   summary/grep → READ_CAP.md "what binds" table: a ledger read by a script or by grep is a
        #             cold/on-demand surface. "A large one is discovery, never a defect" — the split
        #             is WORKING, and demanding a split here would be the instrument over-claiming.
        if size < BUDGET_BYTES:
            note = ""
        elif row["mode"] == "scoped":
            # Rule 8 governs a step DOWNGRADED from a whole read — there the file is still over
            # budget for anyone who needs it whole. It does NOT govern an index over an archive that
            # was never read whole (BOARD/INDEX.md). The tool cannot tell those apart, so it asks the
            # question and hands it to the owner rather than asserting a debt it cannot establish.
            note = (f"  ❓ {size/BUDGET_BYTES:.0%} of budget — not a breach (scoped). RULE-8 QUESTION FOR THE OWNER: "
                    f"if this step was downgraded from a whole read, a split or dated re-trigger is still owed; "
                    f"if the surface is a cold index by design, nothing is owed.")
        else:
            # "nothing owed" full stop would collapse the two defect axes the registry header
            # forbids collapsing — and it did, on the one row whose notes say a rewrite IS owed.
            note = (f"  ℹ️  {size/BUDGET_BYTES:.0%} of budget — cold/on-demand class, NOT a cap breach and nothing owed "
                    f"ON CAP GROUNDS (READ_CAP.md 'what binds'). ⚠️ Protocol accuracy is a SEPARATE axis this tool "
                    f"cannot grade — read the row's notes before concluding nothing is owed.")
        print(f"  ·  {row['path']:<52} {size:>9,} B   {row['mode']:<12} ({row['source_boot_step']}){note}")
    for row in missing:
        print(f"  ❌ {row['path']:<52} {'MISSING':>9}     path does not exist ({row['source_boot_step']}) — orphan row or a retired boot step")

    rc = 0
    if errors:
        rc = 1
    if findings or missing:
        rc = 1
        for row, size in findings:
            over = "OVER THE PHYSICAL CAP" if size >= CAP_BYTES else "over budget"
            print(f"  🔴 FINDING: {row['path']} is {size:,} B — {over} on a `{row['mode']}` read declared by {row['declared_by']}")
        for row in missing:
            print(f"  🔴 FINDING: {row['path']} is declared by {row['declared_by']} and does not exist")
    if not att:
        print(f"❓ READS-CAP UNKNOWN [{agent}]: {len(bearing)} cap-bearing row(s) checked, "
              f"but {agent} has NOT attested its manifest complete — this is a partial perimeter, never a clean bill.")
        return max(rc, 1) if rc else 2
    if rc == 0:
        print(f"✅ READS-CAP 0 [{agent}]: all {len(bearing)} cap-bearing read(s) under budget, in a manifest "
              f"{agent} itself attested complete on {att['declared_on']}. "
              f"This grades the DECLARATION, not the desk — a wrong declaration yields a wrong verdict.")
    return rc


def report_fleet(rows, errors):
    # `.claude` and `_archive` are not desks. Counting them inflates the UNKNOWN denominator —
    # a small instance of measuring against the wrong reference, in the tool built to stop that.
    desks = {"PROME"} | {d for d in os.listdir(os.path.join(ROOT, "AGENTS"))
                         if os.path.isdir(os.path.join(ROOT, "AGENTS", d))
                         and not d.startswith((".", "_"))}
    declared = {r["reader"] for r in rows}
    att = {a for a in declared if attested(rows, a)}
    undeclared = sorted(desks - declared)
    print(f"READS FLEET — {len(rows)} row(s) · {len(declared)} desk(s) with declarations · "
          f"{len(att)} validly ATTESTED · {len(undeclared)} desk(s) with NO declaration")
    per_agent = []
    for agent in sorted(declared):
        per_agent.append(report_agent(rows, agent, []))
        print()
    print(f"⛔ NOT A FLEET VERDICT. {len(undeclared)} desk(s) have declared nothing and are UNKNOWN, "
          f"not clean: {', '.join(undeclared) if undeclared else '(none)'}")
    # PRECEDENCE, and the docstring's contract: a REAL BREACH outranks an incomplete perimeter.
    # `max(rc, 2)` inverted it — WALTER's live 139%-of-budget breach exited 2 (CANNOT-EVALUATE), so a
    # gate keyed on the stated contract read "tool couldn't evaluate" over a finding. Found by the
    # blind cold reader, 2026-08-31.
    if errors or 1 in per_agent:
        return 1
    if undeclared or 2 in per_agent:
        return 2
    return 0


SELFTEST_HEADER = "\t".join(COLUMNS)


def selftest():
    """Falsification set — every case is one the checker must NOT get wrong.
    A guard's own v1 fails on first run; this is where that gets found."""
    big = "PROME/GATES.tsv"          # 52,308 B at build time — over budget AND over cap
    small = "USER.md"                # 4,126 B
    cases = []

    def sheet(*lines):
        return SELFTEST_HEADER + "\n" + "\n".join(lines)

    # `by` defaults to the reader — an attestation is the reader's own word. The old fixture signed
    # every row "X", which is precisely the loophole the cold reader exploited, so the fixtures were
    # encoding the bug they were meant to catch.
    def r(kind, rd, p, m, s, by=None):
        return f"{kind}\t{rd}\t{p}\t{m}\t{s}\t{by or rd}\t2026-08-31\tselftest"

    # 1. an UNATTESTED desk with zero breaches must never score 0
    cases.append(("unattested desk with no breaches is UNKNOWN, not clean",
                  sheet(r("READ", "T", small, "whole", "T:1")), "T", lambda rc: rc == 2))
    # 2. the same sheet WITH an attestation is clean
    cases.append(("attested desk with no breaches is clean",
                  sheet(r("ATTESTATION", "T", "T/BOOT.md", ATTEST_MODE, "T:0"),
                        r("READ", "T", small, "whole", "T:1")), "T", lambda rc: rc == 0))
    # 3. a cap-bearing read over budget is a FINDING even when attested
    cases.append(("attested desk with an over-budget whole read is rc=1",
                  sheet(r("ATTESTATION", "T", "T/BOOT.md", ATTEST_MODE, "T:0"),
                        r("READ", "T", big, "whole", "T:1")), "T", lambda rc: rc == 1))
    # 4. ruling 1: one path under two readers is CORRECT, never a duplicate
    cases.append(("same path under two readers is not a duplicate",
                  sheet(r("ATTESTATION", "T", "T/BOOT.md", ATTEST_MODE, "T:0"),
                        r("READ", "T", small, "whole", "T:1"),
                        r("READ", "U", small, "whole", "U:1")), "T", lambda rc: rc == 0))
    # 5. one path, one reader, two different boot steps is also correct
    cases.append(("same path, same reader, two boot steps is not a duplicate",
                  sheet(r("ATTESTATION", "T", "T/BOOT.md", ATTEST_MODE, "T:0"),
                        r("READ", "T", small, "summary", "T:1"),
                        r("READ", "T", small, "scoped", "T:8")), "T", lambda rc: rc == 0))
    # 6. a SCOPED read on an over-cap file is not a breach (READ_CAP.md rule 8)
    cases.append(("scoped read on an over-cap file is not a breach",
                  sheet(r("ATTESTATION", "T", "T/BOOT.md", ATTEST_MODE, "T:0"),
                        r("READ", "T", big, "scoped", "T:1")), "T", lambda rc: rc == 0))
    # 7. a declared path that does not exist is a FINDING, not a silent skip
    cases.append(("orphan path is a finding",
                  sheet(r("ATTESTATION", "T", "T/BOOT.md", ATTEST_MODE, "T:0"),
                        r("READ", "T", "PROME/NO_SUCH_FILE.md", "whole", "T:1")), "T", lambda rc: rc == 1))
    # 8. an exact duplicate row IS an error
    cases.append(("exact duplicate row is a schema error",
                  sheet(r("ATTESTATION", "T", "T/BOOT.md", ATTEST_MODE, "T:0"),
                        r("READ", "T", small, "whole", "T:1"),
                        r("READ", "T", small, "whole", "T:1")), "T", lambda rc: rc == 1))
    # 9. a bad mode is a schema error
    cases.append(("unknown mode is a schema error",
                  sheet(r("ATTESTATION", "T", "T/BOOT.md", ATTEST_MODE, "T:0"),
                        r("READ", "T", small, "skimmed", "T:1")), "T", lambda rc: rc == 1))
    # 10. a non-ISO declared_on is a schema error
    cases.append(("non-ISO declared_on is a schema error",
                  sheet(r("ATTESTATION", "T", "T/BOOT.md", ATTEST_MODE, "T:0"),
                        f"READ\tT\t{small}\twhole\tT:1\tX\t8/31\tselftest"), "T", lambda rc: rc == 1))

    # ---- negative controls added after the 2026-08-31 blind cold read (it built #11 by hand) ----
    # 11. ⛔ THE BYPASS: an attestation for T signed by someone else must NOT clear T.
    cases.append(("attestation signed by another desk does NOT clear the reader",
                  sheet(r("ATTESTATION", "T", "T/BOOT.md", ATTEST_MODE, "T:0", by="PROME"),
                        r("READ", "T", small, "whole", "T:1")), "T", lambda rc: rc == 2))
    # 12. and the from-charter form specifically, since the registry ships rows carrying it
    cases.append(("PROME(from-charter) can never attest",
                  sheet(r("ATTESTATION", "T", "T/BOOT.md", ATTEST_MODE, "T:0", by="PROME(from-charter)"),
                        r("READ", "T", small, "whole", "T:1")), "T", lambda rc: rc == 2))
    # 13. RETIRED rows are not measured, so they must not pad the "all N under budget" claim: a
    #     manifest whose ONLY row is retired has measured nothing and cannot be a clean bill of health.
    cases.append(("a manifest of only RETIRED rows measures nothing",
                  sheet(r("ATTESTATION", "T", "T/BOOT.md", ATTEST_MODE, "T:0"),
                        r("READ", "T", big, "RETIRED-2026-08-01", "T:1")), "T",
                  lambda rc: rc == 0, "the ✅ line must claim 0 cap-bearing reads, never 1 declared read"))

    import io, contextlib
    passed = failed = 0
    for case in cases:
        name, text, agent, expect = case[0], case[1], case[2], case[3]
        rows, errors = parse(text, "selftest")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = report_agent(rows, agent, errors)
        ok = expect(rc)
        if ok and len(case) > 4 and "0 cap-bearing" in case[4]:
            ok = "all 0 cap-bearing read(s)" in buf.getvalue()
        print(f"  {'✅' if ok else '❌'} {name} → rc={rc}")
        passed, failed = passed + ok, failed + (not ok)
    print(f"\nselftest: {passed}/{passed+failed} pass")
    return 0 if not failed else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()
    try:
        with open(REGISTRY, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        print(f"❓ CANNOT-EVALUATE: {REGISTRY} unreadable ({exc})")
        return 2
    rows, errors = parse(text)
    for err in errors:
        print(f"  ❌ SCHEMA {err}")
    if "--agent" in argv:
        agent = argv[argv.index("--agent") + 1]
        return max(report_agent(rows, agent, errors), 1 if errors else 0)
    return report_fleet(rows, errors)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
