#!/usr/bin/env python3
"""table_check.py — flag markdown table rows that carry MORE cells than their header.

WHY THIS EXISTS
---------------
In GitHub-Flavored Markdown a table row may not exceed its header's column count:
the excess cells are dropped from the rendered output with no error and no visual
tell. On 2026-09-12 `PROME/STATUS.md` L21 carried five cells in a three-column
table, so two cells -- one of them a live claim about the closeout dashboard-build
procedure -- were invisible to every rendered read while staying fully visible to a
`cat`. A Claude session reading raw text believed the content had been communicated;
the operator and every Will-facing view never saw it. Neither reader can tell.

Spine audit #13 read that file the same day and missed it, because a spine audit
grades CLAIMS and this defect destroys a claim rather than falsifying one.

Acceptance conditions + the five neighbour categories:
    PROME/tools/tests/ACCEPTANCE_table_check_overcelled_rows.md
Tests: PROME/tools/tests/test_table_check.py

CONTRACT
--------
* Perimeter is DERIVED from `PROME/registry/READS.tsv` (PROME rows, mode=whole),
  never hand-listed -- a hand-list is a second source of truth that goes stale.
* Over-celled rows are the finding. UNDER-celled rows are reported separately and
  never under the same label: markdown pads short rows and nothing is lost.
* `\\|` is not a separator. A pipe inside an inline code span IS one, because GFM
  splits on it -- this check agrees with the RENDERER, not with authorial intent.
* rc 0 clean / rc 1 finding / rc 2 could not establish
  (AGENTS/DAEDALUS/BLUEPRINTS/CHECK_STANDARD.md section 9).
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
READS = ROOT / "PROME/registry/READS.tsv"

_ESCAPED = "\x00"          # stand-in for a literal `\|` while we split
_SEP_RE = re.compile(r"^:?-{1,}:?$")
_FENCE_RE = re.compile(r"^\s*(```|~~~)")


def split_cells(line: str) -> list[str]:
    """Split one markdown table line into its cells, the way a renderer does.

    Escaped pipes are held out of the split; every other pipe separates, code
    spans included. A single leading and a single trailing pipe are structural
    and contribute no cell."""
    s = line.strip().replace("\\|", _ESCAPED)
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.replace(_ESCAPED, "\\|") for c in s.split("|")]


def _is_separator(line: str, width: int) -> bool:
    cells = split_cells(line)
    if len(cells) != width:
        return False
    return all(_SEP_RE.match(c.strip()) for c in cells)


def scan_text(text: str, path: str = "<text>") -> list[dict]:
    """Return one finding dict per malformed row. Pure; no I/O."""
    lines = text.split("\n")
    findings: list[dict] = []
    in_fence = False
    fence_tok = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        m = _FENCE_RE.match(line)
        if m:
            # A fence inside a fence only closes on the same token, so an
            # example block quoting ``` inside ~~~ does not open a real one.
            if not in_fence:
                in_fence, fence_tok = True, m.group(1)
            elif m.group(1) == fence_tok:
                in_fence, fence_tok = False, ""
            i += 1
            continue
        if in_fence or not line.strip().startswith("|"):
            i += 1
            continue
        # Candidate header. A table exists only if the NEXT line is a separator
        # of the same width -- a lone `|`-leading line is prose, not a table.
        width = len(split_cells(line))
        if i + 1 >= len(lines) or not _is_separator(lines[i + 1], width):
            i += 1
            continue
        header_line = i + 1          # 1-indexed, for the report
        j = i + 2
        while j < len(lines) and lines[j].strip().startswith("|"):
            if _FENCE_RE.match(lines[j]):
                break
            cells = split_cells(lines[j])
            if len(cells) > width:
                findings.append({
                    "path": path,
                    "line": j + 1,
                    "header_line": header_line,
                    "width": width,
                    "observed": len(cells),
                    "kind": "OVER",
                    "dropped": [c.strip() for c in cells[width:]],
                })
            elif len(cells) < width:
                findings.append({
                    "path": path,
                    "line": j + 1,
                    "header_line": header_line,
                    "width": width,
                    "observed": len(cells),
                    "kind": "UNDER",
                    "dropped": [],
                })
            j += 1
        i = j
    return findings


def perimeter() -> list[pathlib.Path]:
    """PROME's declared whole-read surfaces, from the attested manifest."""
    out: list[pathlib.Path] = []
    for raw in READS.read_text().split("\n"):
        if raw.startswith("#") or not raw.strip():
            continue
        f = raw.split("\t")
        if len(f) >= 4 and f[0] == "READ" and f[1] == "PROME" and f[3] == "whole":
            out.append(ROOT / f[2])
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("paths", nargs="*",
                    help="files to scan; default = PROME's mode=whole rows in READS.tsv")
    ap.add_argument("--quiet", action="store_true",
                    help="print only findings and the one-line verdict")
    args = ap.parse_args()

    try:
        targets = ([pathlib.Path(p) for p in args.paths] if args.paths else perimeter())
    except OSError as e:
        print(f"⚠️  TABLE-CHECK UNKNOWN — cannot read the manifest {READS}: {e}")
        return 2

    over: list[dict] = []
    under: list[dict] = []
    scanned = 0
    for p in targets:
        try:
            text = p.read_text()
        except FileNotFoundError:
            # A manifest row pointing at nothing is a manifest defect, not a
            # clean scan. Never report "clean" over a surface never opened.
            print(f"⚠️  TABLE-CHECK UNKNOWN — {p}: does not exist (declared in the manifest)")
            return 2
        except OSError as e:
            print(f"⚠️  TABLE-CHECK UNKNOWN — {p}: {type(e).__name__}: {e}")
            return 2
        scanned += 1
        # A path OUTSIDE the repo is a legitimate invocation (a fixture, a
        # `git show` extract under /tmp). `relative_to` raises on those, and
        # the traceback exited 1 -- indistinguishable from a real finding.
        label = str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p)
        for f in scan_text(text, label):
            (over if f["kind"] == "OVER" else under).append(f)

    for f in over:
        print(f"❌ TABLE-CHECK {f['path']}:{f['line']} — {f['observed']} cells in a "
              f"{f['width']}-column table (header L{f['header_line']}); "
              f"{f['observed'] - f['width']} cell(s) DROPPED when rendered:")
        for d in f["dropped"]:
            print(f"      ⤷ {d[:160]}")
    if not args.quiet:
        for f in under:
            print(f"·  TABLE-CHECK {f['path']}:{f['line']} — {f['observed']} cells in a "
                  f"{f['width']}-column table; markdown PADS this, nothing is lost")

    if over:
        print(f"❌ TABLE-CHECK {len(over)} over-celled row(s) across {scanned} file(s) "
              f"— content is invisible in every rendered read; fix the row, not the reader")
        return 1
    print(f"✅ TABLE-CHECK ok {scanned} file(s), no over-celled rows"
          + (f" ({len(under)} short row(s), harmless)" if under else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
