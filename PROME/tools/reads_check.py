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
ROW_KINDS = ("READ", "ATTESTATION", "BASIS")
BASIS_MODE = "boot-defining"
ROSTER = os.path.join(ROOT, "PROME", "ROSTER.md")
# ROSTER.md is the fleet's single source of truth for membership. Sections that DO carry fleet
# desks vs sections that carry explicit exclusion classes (root CLAUDE.md: ARCHIVE SOURCES ·
# TOOL-CLASS · OFF-FLEET "are not fleet agents — never launch, task, or audit them as such").
ROSTER_INCLUDE = ("ACTIVE", "TIER-2", "TIER 2", "DORMANT", "SPECIAL")
ROSTER_EXCLUDE = ("RETIRED", "ARCHIVE SOURCE", "TOOL-CLASS", "TOOL CLASS", "OFF-FLEET", "OFF FLEET")
AGENT_TOKEN = re.compile(r"^[A-Z][A-Z0-9_]{1,15}$")
# A boot read can legitimately live in ANOTHER REPO. WALTER's step 7e(f) reads Will's phone-dropped
# signals out of the RESEARCH-INTAKE lane (separate repo, pulled --ff-only). Such a row is DECLARED
# for visibility and never byte-graded here — treating it as a missing local file would emit exactly
# the false ❌ that class rows used to, and a false ❌ teaches readers to discount ❌ rows.
EXTERNAL_ROOTS = ("RESEARCH-INTAKE/",)
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
        if kind not in ROW_KINDS:
            errors.append(f"{source}:{n}: row_kind '{kind}' is not one of {ROW_KINDS}")
        elif kind == "BASIS" and mode != BASIS_MODE:
            errors.append(f"{source}:{n}: BASIS row must carry mode '{BASIS_MODE}', got '{mode}'")
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
    # The key EXCLUDES `mode` on purpose. Ruling 1 legitimises the same path under several readers,
    # and the same reader at several BOOT STEPS (PROME reads WILL_QUEUE two ways at steps 5 and 8) —
    # but ONE reader claiming two different modes for one path at ONE step is a contradiction, not a
    # second reading, and the old mode-inclusive key waved it through (cold reader D4).
    seen = {}
    for row in rows:
        key = (row["row_kind"], row["reader"], row["path"], row["source_boot_step"])
        if key in seen:
            prev_line, prev_mode = seen[key]
            if prev_mode == row["mode"]:
                errors.append(f"{source}:{row['_line']}: exact duplicate of line {prev_line}")
            else:
                errors.append(f"{source}:{row['_line']}: CONTRADICTS line {prev_line} — same reader, same path, "
                              f"same boot step, two modes ('{prev_mode}' vs '{row['mode']}'). One step reads a file one way.")
        seen[key] = (row["_line"], row["mode"])
    # EXACTLY ONE ATTESTATION PER READER. Two rows both claiming "manifest-complete" make
    # "complete" ambiguous — and the older one can be the reason a desk reads clean.
    att_by_reader = {}
    for row in rows:
        if row["row_kind"] != "ATTESTATION":
            continue
        att_by_reader.setdefault(row["reader"], []).append(row["_line"])
    for reader, lines in att_by_reader.items():
        if len(lines) > 1:
            errors.append(f"{source}:{lines[-1]}: {reader} has {len(lines)} ATTESTATION rows "
                          f"(lines {', '.join(map(str, lines))}). Exactly one per reader — "
                          f"'complete' cannot mean two different things.")
    # A path cell that escapes the repo is a schema error, not a measurement of something else.
    for row in rows:
        if row["path"].startswith(EXTERNAL_ROOTS):
            continue
        if os.path.isabs(row["path"]) or resolve(row["path"]) is None:
            errors.append(f"{source}:{row['_line']}: path '{row['path']}' is absolute or resolves outside the repo")
    return rows, errors


def roster_desks():
    """Fleet membership from PROME/ROSTER.md — the canonical roster, never the filesystem.

    Listing AGENTS/* and calling every directory a desk is the same heuristic this registry exists
    to replace: it invented `.claude` and `_archive` as undeclared desks, and it silently disagrees
    with the exclusion classes root CLAUDE.md defines (ARCHIVE SOURCES · TOOL-CLASS · OFF-FLEET are
    NOT fleet agents). Returns (desks, error) — and on a bad parse returns an ERROR, never a
    filesystem fallback: degrading quietly to the heuristic is how a wrong denominator gets quoted
    as a fleet verdict.
    """
    try:
        with open(ROSTER, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        return set(), f"ROSTER.md unreadable ({exc}) — fleet membership cannot be established"
    desks, including = set(), False
    for line in text.splitlines():
        if line.startswith("#"):
            head = line.lstrip("#").strip().upper()
            if any(k in head for k in ROSTER_EXCLUDE):
                including = False
            elif any(k in head for k in ROSTER_INCLUDE):
                including = True
            continue
        if not including:
            continue
        if line.startswith("|"):                                  # table row: first cell is the name
            first = line.split("|")[1].strip().strip("*").split()
            if first and AGENT_TOKEN.match(first[0]):
                desks.add(first[0])
        else:                                                     # SPECIAL section: **NAME** — ...
            m = re.match(r"\*\*([A-Z][A-Z0-9_]{1,15})\*\*\s*[—-]", line.strip())
            if m:
                desks.add(m.group(1))
    desks.discard("AGENT")                                        # the table header cell
    if len(desks) < 10:
        return desks, (f"ROSTER.md parsed to only {len(desks)} desk(s) — implausible; the section "
                       f"headings or table shape have moved and this parser is wrong. Refusing to "
                       f"report a fleet verdict over a denominator I cannot trust.")
    return desks | {"PROME"}, None


def resolve(path):
    """Repo-relative → absolute, or None if the row points outside the repo.

    `os.path.join(ROOT, "/etc/hostname")` returns "/etc/hostname" — an absolute `path` cell silently
    escapes the repo and gets measured anyway (cold reader case D6: 16 B, 0% of budget, rc=0).
    """
    if os.path.isabs(path):
        return None
    full = os.path.normpath(os.path.join(ROOT, path))
    return full if full.startswith(ROOT + os.sep) else None


def classify(path):
    """What KIND of thing does this row declare? ('file'|'glob'|'dir'|'missing', payload)

    A class row (`AGENTS/*/STATUS.md`) is not an orphan and a directory is not a missing file. Both
    used to fall through to `size_of() is None` and render as `❌ MISSING — path does not exist`
    plus a red FINDING. WALTER caught it on its own verdict: the false ❌ sat beside the one TRUE
    finding, and the cost is not the bytes — a false ❌ teaches readers to discount ❌ rows, which is
    the class this tool most needs believed.
    """
    if path.startswith(EXTERNAL_ROOTS):
        return "external", None
    if any(ch in path for ch in "*?["):
        import glob as _glob
        matches = sorted(m for m in _glob.glob(os.path.join(ROOT, path), recursive=True)
                         if os.path.isfile(m))
        return ("glob", matches) if matches else ("missing", None)
    full = resolve(path)
    if full is None:
        return "missing", None
    if os.path.isdir(full):
        return "dir", sum(len(f) for _, _, f in os.walk(full))
    if os.path.isfile(full):
        return "file", os.path.getsize(full)
    return "missing", None


def size_of(path):
    """Bytes, or None when the row does not name a readable FILE inside the repo.

    A directory answers `getsize` with its inode size (4,096 B = 13% of budget, clean) — reachable
    in practice, since two shipped rows resolve bare `registry/` paths by hand (cold reader D5).
    """
    full = resolve(path)
    if full is None or not os.path.isfile(full):
        return None
    try:
        return os.path.getsize(full)
    except OSError:
        return None


def git_vintage(path):
    """Last COMMIT date for a path (ISO), or None. Commit time, never mtime — root canon: a git sync
    restamps mtime, so an mtime-keyed freshness check fails false-negative."""
    full = resolve(path)
    if full is None:
        return None
    try:
        import subprocess
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", path],
                             cwd=ROOT, capture_output=True, text=True, timeout=10)
        return out.stdout.strip() or None
    except Exception:
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


def attestation_stale(att, rows=None):
    """Is this attestation older than the boot protocol it claims to have enumerated?

    ⛔ AN ATTESTATION MUST BE A TRIGGER, NOT A SHIELD. `declared_on` gates rc=0, so with no expiry a
    desk attests once, changes its boot protocol for a year, and the tool keeps certifying clean — a
    2019-dated attestation returned READS-CAP 0 (cold reader ❌7). That is the very failure the
    registry's own NO-BYTE-COLUMN argument is built on, committed on the one value that gates the
    verdict. `finding_dated_stamp_is_a_trigger_not_a_shield`.

    The trigger is CONTENT-DERIVED, not a clock: an attestation names the surfaces that DEFINE the
    boot, so a COMMIT to any of them after `declared_on` means the enumeration is out of date.

    ⚠️ ONE FILE IS NOT THE BASIS. A boot is defined by its charter, its protocol doc AND the tools it
    runs — nothing invalidated PROME's attestation when `prome_gate.py` grew a check that reads a new
    file. So the basis is every `BASIS` row the reader declared, plus the attestation's own path; a
    commit to ANY of them after `declared_on` means a new boot dependency may exist that the manifest
    has never seen. A desk that declares no BASIS rows has no dated basis and is treated as stale.

    Returns (stale: bool, reason: str|None).
    """
    basis = [att["path"]] + [r["path"] for r in (rows or [])
                             if r["row_kind"] == "BASIS" and r["reader"] == att["reader"]]
    if len(basis) == 1:
        return True, (f"{att['reader']} declared NO `BASIS` rows — the attestation rests on "
                      f"'{att['path']}' alone, so a change to the charter or to any boot tool would "
                      f"not age it. Declare the boot-defining surfaces.")
    newest, newest_path = None, None
    for path in basis:
        vintage = git_vintage(path)
        if vintage is None:
            return True, (f"basis surface '{path}' has no readable git history (missing, outside the "
                          f"repo, or uncommitted) — nothing dates this claim")
        if newest is None or vintage > newest:
            newest, newest_path = vintage, path
    if newest > att["declared_on"]:
        return True, (f"'{newest_path}' was committed {newest}, AFTER the attestation dated "
                      f"{att['declared_on']} — a boot-defining surface moved, so the enumeration may "
                      f"be missing a dependency. Re-enumerate and re-attest.")
    return False, None


def report_class_row(row, kind, payload, findings):
    """Render a glob or directory row. A glob IS graded — every match is measured, and the largest
    is what a session actually pays. A directory has no meaningful read size and is declared-only."""
    bearing = row["mode"] in CAP_BEARING
    if kind == "external":
        print(f"  ⇢  {row['path']:<52} {'EXTERNAL':>9}     another repo — declared for visibility, not "
              f"byte-graded here ({row['mode']}, {row['source_boot_step']})")
        return
    if kind == "dir":
        if bearing:
            # You cannot read a directory whole. Declared `summary`/`scoped` it is a legitimate
            # tree-shaped dependency (a parity check); declared cap-bearing it is a bad row.
            print(f"  🔴 {row['path']:<52} {'DIR':>9}     declared `{row['mode']}` — a directory cannot be "
                  f"read whole; use a class row (path/*) or a non-cap-bearing mode ({row['source_boot_step']})")
            findings.append((row, 0))
            return
        print(f"  ▫  {row['path']:<52} {'DIR':>9}     {payload} file(s) under it — a directory has no read size; "
              f"declared so the dependency is visible, never byte-graded ({row['mode']}, {row['source_boot_step']})")
        return
    sizes = [(os.path.getsize(m), os.path.relpath(m, ROOT)) for m in payload]
    biggest, big_path = max(sizes)
    total = sum(sz for sz, _ in sizes)
    over = [ (sz, pth) for sz, pth in sizes if sz >= BUDGET_BYTES ]
    mark = "⚠️ " if (over and bearing) else ("·" if not bearing else "✅")
    print(f"  {mark} {row['path']:<52} {len(sizes):>4} files  largest {biggest:,} B ({biggest/BUDGET_BYTES:.0%}) "
          f"= {big_path}  total {total:,} B  ({row['mode']}, {row['source_boot_step']})")
    if over and bearing:
        for sz, pth in sorted(over, reverse=True):
            findings.append((dict(row, path=pth), sz))
    elif over:
        print(f"       ℹ️  {len(over)} match(es) over budget, excluded by the declared `{row['mode']}` mode — "
              f"largest is {big_path}")


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
    # Every row lands in exactly one bucket or it is UNCLASSIFIED and said so. A bad `mode` used to
    # sit in the denominator and in no bucket, printing "1 declared read(s) = 0 + 0" (cold reader D8).
    unclassified = [r for r in reads if r not in bearing and r not in declared_only and r not in retired]
    basis_rows = [r for r in rows if r["row_kind"] == "BASIS" and r["reader"] == agent]
    unsigned = unsigned_attestations(rows, agent)
    stale, stale_why = attestation_stale(att, rows) if att else (False, None)

    if att and stale:
        stamp = f"⛔ ATTESTATION STALE (dated {att['declared_on']})"
    elif att:
        stamp = f"ATTESTED {att['declared_on']} by {agent} itself"
    else:
        stamp = "⛔ NOT ATTESTED"
    print(f"READS [{agent}] — budget {BUDGET_BYTES:,} B · cap {CAP_BYTES:,} B · perimeter: "
          f"{len(bearing)} cap-bearing + {len(declared_only)} declared-not-bearing = {len(bearing) + len(declared_only)} live read(s)"
          f"{f' (+{len(retired)} RETIRED, not measured)' if retired else ''}"
          f"{f' (+{len(unclassified)} UNCLASSIFIED)' if unclassified else ''}"
          f"{f' · basis {len(basis_rows)} surface(s)' if basis_rows else ''} · manifest {stamp}")
    for row in unsigned:
        print(f"  ⛔ INVALID ATTESTATION line {row['_line']}: signed by '{row['declared_by']}', not by {agent}. "
              f"Only the reader can attest its own manifest — this row does NOT clear the desk.")
    if att and stale:
        print(f"  ⛔ STALE ATTESTATION: {stale_why}")
    # MODE IS SELF-ASSERTED, AND DOWNGRADING IT ERASES A BREACH WITH ONE WORD. Re-declaring the 139%
    # row `summary` took this tool from rc=1 to a clean rc=0 (cold reader D1). No instrument can
    # adjudicate whether contents entered a session's context — so the tool cannot rule, but it must
    # never let the claim pass silently. Every over-budget row excused BY DECLARATION is named, with
    # whoever signed the excuse.
    laundering_risk = [r for r in declared_only if (size_of(r["path"]) or 0) >= BUDGET_BYTES]
    if laundering_risk:
        print(f"  ⚠️  MODE IS A SELF-ASSERTED CLAIM — {len(laundering_risk)} over-budget read(s) are excluded from the "
              f"verdict BY DECLARATION, not by measurement. Verify each against its boot step before quoting rc:")
        for row in laundering_risk:
            print(f"       · {row['path']} ({size_of(row['path']):,} B) declared `{row['mode']}` at {row['source_boot_step']} by {row['declared_by']}")

    findings, missing = [], []
    for row in sorted(bearing, key=lambda r: -(size_of(r["path"]) or 0)):
        kind, payload = classify(row["path"])
        if kind == "missing":
            missing.append(row)
            continue
        if kind in ("glob", "dir", "external"):
            report_class_row(row, kind, payload, findings)
            continue
        size = payload
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
        kind, payload = classify(row["path"])
        if kind == "missing":
            missing.append(row)
            continue
        if kind in ("glob", "dir", "external"):
            report_class_row(row, kind, payload, findings)
            continue
        size = payload
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
    # A manifest that measured NOTHING cannot be a clean bill of health — an attested desk with zero
    # READ rows, or with every row retired, printed rc=0 having checked no file at all (cold reader
    # D3 + D12). Nothing measured is UNKNOWN, exactly like nothing declared.
    if not bearing and not declared_only:
        print(f"❓ READS-CAP UNKNOWN [{agent}]: the manifest declares NO live read"
              f"{' (all rows RETIRED)' if retired else ''} — nothing was measured, so nothing is certified.")
        return 1 if rc else 2
    if not att or stale:
        why = ("has NOT attested its manifest complete" if not att
               else "attested on a date its own boot protocol has since moved past")
        print(f"❓ READS-CAP UNKNOWN [{agent}]: {len(bearing)} cap-bearing row(s) checked, "
              f"but {agent} {why} — this is a partial perimeter, never a clean bill.")
        return max(rc, 1) if rc else 2
    if rc == 0:
        print(f"✅ READS-CAP 0 [{agent}]: all {len(bearing)} cap-bearing read(s) under budget, in a manifest "
              f"{agent} itself attested complete on {att['declared_on']}. "
              f"This grades the DECLARATION, not the desk — a wrong declaration yields a wrong verdict.")
    return rc


def report_fleet(rows, errors):
    # Membership comes from the canonical ROSTER, never from listing AGENTS/. A prefix filter on
    # directory names is still a heuristic — it happened to drop `.claude` and `_archive`, and it
    # would still count a RETIRED or ARCHIVE-SOURCE folder as a live desk owing a declaration.
    desks, roster_err = roster_desks()
    if roster_err:
        print(f"❓ CANNOT-EVALUATE — no fleet denominator: {roster_err}")
        return 2
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
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", small, "whole", "T:1")), "T", lambda rc: rc == 0))
    # 3. a cap-bearing read over budget is a FINDING even when attested
    cases.append(("attested desk with an over-budget whole read is rc=1",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", big, "whole", "T:1")), "T", lambda rc: rc == 1))
    # 4. ruling 1: one path under two readers is CORRECT, never a duplicate
    cases.append(("same path under two readers is not a duplicate",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", small, "whole", "T:1"),
                        r("READ", "U", small, "whole", "U:1")), "T", lambda rc: rc == 0))
    # 5. one path, one reader, two different boot steps is also correct
    cases.append(("same path, same reader, two boot steps is not a duplicate",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", small, "summary", "T:1"),
                        r("READ", "T", small, "scoped", "T:8")), "T", lambda rc: rc == 0))
    # 6. a SCOPED read on an over-cap file is not a breach (READ_CAP.md rule 8)
    cases.append(("scoped read on an over-cap file is not a breach",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", big, "scoped", "T:1")), "T", lambda rc: rc == 0))
    # 7. a declared path that does not exist is a FINDING, not a silent skip
    cases.append(("orphan path is a finding",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", "PROME/NO_SUCH_FILE.md", "whole", "T:1")), "T", lambda rc: rc == 1))
    # 8. an exact duplicate row IS an error
    cases.append(("exact duplicate row is a schema error",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", small, "whole", "T:1"),
                        r("READ", "T", small, "whole", "T:1")), "T", lambda rc: rc == 1))
    # 9. a bad mode is a schema error
    cases.append(("unknown mode is a schema error",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", small, "skimmed", "T:1")), "T", lambda rc: rc == 1))
    # 10. a non-ISO declared_on is a schema error
    cases.append(("non-ISO declared_on is a schema error",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        f"READ\tT\t{small}\twhole\tT:1\tX\t8/31\tselftest"), "T", lambda rc: rc == 1))

    # ---- negative controls added after the 2026-08-31 blind cold read (it built #11 by hand) ----
    # 11. ⛔ THE BYPASS: an attestation for T signed by someone else must NOT clear T.
    cases.append(("attestation signed by another desk does NOT clear the reader",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0", by="PROME"),
                        r("READ", "T", small, "whole", "T:1")), "T", lambda rc: rc == 2))
    # 12. and the from-charter form specifically, since the registry ships rows carrying it
    cases.append(("PROME(from-charter) can never attest",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0", by="PROME(from-charter)"),
                        r("READ", "T", small, "whole", "T:1")), "T", lambda rc: rc == 2))
    # 13. RETIRED rows are not measured, so they must not pad the "all N under budget" claim: a
    #     manifest whose ONLY row is retired has measured nothing and cannot be a clean bill of health.
    cases.append(("a manifest of only RETIRED rows measures nothing",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", big, "RETIRED-2026-08-01", "T:1")), "T",
                  lambda rc: rc == 2, "declares NO live read"))

    # ---- second cold-read round, 2026-08-31: cases the reader found MISSING, not ones I chose ----
    # 14. ⛔ MODE-FLIP LAUNDERING: re-declaring the over-budget row `summary` erased the breach.
    #     The tool cannot adjudicate mode, so rc=0 stands — but the excuse must be NAMED in output.
    cases.append(("a breach excused by mode is named, not silently dropped",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", big, "summary", "T:1")), "T",
                  lambda rc: rc == 0, "MODE IS A SELF-ASSERTED CLAIM"))
    # 15. an attested desk with ZERO read rows measured nothing and cannot be clean
    cases.append(("attested desk with no reads is UNKNOWN",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0")), "T", lambda rc: rc == 2))
    # 16. one reader, one path, one STEP, two modes = a contradiction (not ruling 1's second reading)
    cases.append(("two modes for one path at one step is a contradiction",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", small, "whole", "T:1"),
                        r("READ", "T", small, "summary", "T:1")), "T", lambda rc: rc == 1))
    # 17. a directory answers getsize with 4,096 B and used to pass as a small clean file
    cases.append(("a directory is not a file",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", "PROME/registry", "whole", "T:1")), "T", lambda rc: rc == 1))
    # 18. an absolute path escapes the repo and got measured anyway
    cases.append(("a path outside the repo is a schema error",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", "/etc/hostname", "whole", "T:1")), "T", lambda rc: rc == 1))
    # 19. ⛔ AN ATTESTATION IS A TRIGGER, NOT A SHIELD: a 2019 date certified rc=0 forever.
    cases.append(("an attestation older than the protocol it enumerated is STALE",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", small, "whole", "T:1")).replace("\t2026-08-31\tselftest\nBASIS",
                                                                       "\t2019-01-01\tselftest\nBASIS"),
                  "T", lambda rc: rc == 2))
    # 20. a row_kind typo used to make the row VANISH from the perimeter while rc was right for
    #     the wrong reason — the count must not silently shrink.
    cases.append(("a row_kind typo does not silently shrink the perimeter",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("Read", "T", big, "whole", "T:1")), "T", lambda rc: rc == 1))

    # ---- third round, 2026-08-31: the six negative tests the reviewer named ----
    # 21. a CROSS-AGENT oversized read is a finding on the READER's manifest (ruling 1's whole point)
    cases.append(("a cross-agent oversized read is a finding on the reader",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                       r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", "AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv", "whole", "T:6b")),
                  "T", lambda rc: rc == 1))
    # 22. `programmatic` is CAP-BEARING — an oversized one is a breach, unlike `summary`
    cases.append(("a programmatic oversized read is a breach",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                       r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", big, "programmatic", "T:1")), "T", lambda rc: rc == 1))
    # 23. two attestations for one reader make "complete" ambiguous
    cases.append(("two attestations for one reader is a schema error",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("ATTESTATION", "T", "PROME/CLAUDE.md", ATTEST_MODE, "T:0b"),
                        r("READ", "T", small, "whole", "T:1")), "T", lambda rc: rc == 1))
    # 24. ⛔ A NEW BOOT DEPENDENCY must age an existing attestation: the basis moved after the date.
    cases.append(("an attestation predating a change to its BASIS is stale",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                       r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("BASIS", "T", "PROME/tools/reads_check.py", BASIS_MODE, "T:0"),
                        r("READ", "T", small, "whole", "T:1")).replace(
                            "\t2026-08-31\tselftest\nBASIS", "\t2020-01-01\tselftest\nBASIS"),
                  "T", lambda rc: rc == 2))
    # 25. an attestation with NO declared basis cannot age at all, so it is never clean
    cases.append(("an attestation with no BASIS rows is stale by construction",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("READ", "T", small, "whole", "T:1")), "T", lambda rc: rc == 2))
    # 26. a class row is EXPANDED and graded, never rendered as a missing file (WALTER's false ❌)
    cases.append(("a glob class row is expanded, not reported missing",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                       r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", "AGENTS/*/STATUS.md", "scoped", "T:8")), "T",
                  lambda rc: rc == 0, "files  largest"))

    # 27. a cross-repo read is declared, never rendered as a missing local file
    cases.append(("an external-repo read is declared, not reported missing",
                  sheet(r("ATTESTATION", "T", "PROME/BOOT.md", ATTEST_MODE, "T:0"),
                        r("BASIS", "T", "PROME/CLAUDE.md", BASIS_MODE, "T:0"),
                        r("READ", "T", "RESEARCH-INTAKE/phone_inbox/signal_*.md", "whole", "T:7e")),
                  "T", lambda rc: rc == 0, "EXTERNAL"))

    import io, contextlib
    passed = failed = 0
    for case in cases:
        name, text, agent, expect = case[0], case[1], case[2], case[3]
        rows, errors = parse(text, "selftest")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = report_agent(rows, agent, errors)
        ok = expect(rc)
        # Some cases assert on OUTPUT, not just the exit code: an rc alone cannot show whether a
        # claim was named or silently dropped.
        if ok and len(case) > 4:
            probe = case[4]
            ok = ("all 0 cap-bearing read(s)" in buf.getvalue()) if "0 cap-bearing" in probe \
                else (probe in buf.getvalue())
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
        # `--agent` with no value raised IndexError and exited outside the declared 0/1/2 contract
        # (cold reader D11). A check that crashes has not returned CANNOT-EVALUATE; it has returned
        # nothing a caller can branch on.
        idx = argv.index("--agent") + 1
        if idx >= len(argv) or argv[idx].startswith("--"):
            print("❓ CANNOT-EVALUATE: --agent requires a desk name, e.g. --agent WALTER")
            return 2
        return max(report_agent(rows, argv[idx], errors), 1 if errors else 0)
    return report_fleet(rows, errors)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
