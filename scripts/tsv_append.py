#!/usr/bin/env python3
"""Safe TSV row append + integrity check — fleet ledger tool.

Born 2026-07-20 from two printf-format corruption incidents in two days
(WALTER kill_log 7/19 "%-escape ate the tail"; LABOR board_log 7/20 %/<
mangled a row). Root cause: shell printf treats % in DATA as a format
directive when data lands in the format-string position — and market text
is full of %. This tool takes fields as argv, so no format-string hazard
exists by construction. Auto-memory: finding_printf_format_tsv_append_corruption.

Usage:
  append:  python3 scripts/tsv_append.py FILE field1 field2 ... fieldN
           - expected column count = the file's header row (first non-#,
             non-blank line). Field-count mismatch => exit 2, nothing written.
           - embedded tab/newline/CR in any field => exit 2, nothing written
             (fail loud; sanitize upstream deliberately, never silently).
  check:   python3 scripts/tsv_append.py --check FILE
           - lints every data row's column count against the header.
             Inconsistent rows listed => exit 1; clean => exit 0.
             Wire into agent doctors as a ledger-integrity check.

No third-party deps. Append is a single os.write of one encoded line
(atomic for any sane line length on POSIX).
"""
import os
import sys


def read_rows(path):
    with open(path, "r", encoding="utf-8", newline="") as f:
        return f.read().splitlines()


def header_ncols(rows, path):
    for i, line in enumerate(rows):
        if line.strip() and not line.lstrip().startswith("#"):
            return i, len(line.split("\t"))
    sys.exit(f"ERROR: {path}: no header row found (every line blank or #-comment)")


def cmd_check(path):
    rows = read_rows(path)
    hdr_i, ncols = header_ncols(rows, path)
    bad = []
    for i, line in enumerate(rows[hdr_i + 1:], start=hdr_i + 2):  # 1-based lines
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        n = len(line.split("\t"))
        if n != ncols:
            bad.append((i, n, line[:80]))
    if bad:
        print(f"{path}: header has {ncols} cols; {len(bad)} inconsistent row(s):")
        for lineno, n, preview in bad:
            print(f"  line {lineno}: {n} cols | {preview}")
        return 1
    print(f"{path}: OK ({ncols} cols, {sum(1 for r in rows[hdr_i+1:] if r.strip() and not r.lstrip().startswith('#'))} data rows)")
    return 0


def cmd_append(path, fields):
    rows = read_rows(path)
    _, ncols = header_ncols(rows, path)
    if len(fields) != ncols:
        sys.exit(f"ERROR: {path} header has {ncols} cols; you passed {len(fields)} fields. Nothing written.")
    for j, f in enumerate(fields):
        for ch, name in (("\t", "tab"), ("\n", "newline"), ("\r", "CR")):
            if ch in f:
                sys.exit(f"ERROR: field {j+1} contains an embedded {name}. Sanitize upstream. Nothing written.")
    line = "\t".join(fields) + "\n"
    # ensure the file currently ends with a newline so we never weld onto a prior row
    prefix = ""
    with open(path, "rb") as f:
        f.seek(0, os.SEEK_END)
        if f.tell() > 0:
            f.seek(-1, os.SEEK_END)
            if f.read(1) != b"\n":
                prefix = "\n"
    fd = os.open(path, os.O_WRONLY | os.O_APPEND)
    try:
        os.write(fd, (prefix + line).encode("utf-8"))
    finally:
        os.close(fd)
    print(f"appended 1 row ({ncols} cols) -> {path}")
    return 0


def main():
    args = sys.argv[1:]
    if len(args) >= 2 and args[0] == "--check":
        sys.exit(cmd_check(args[1]))
    if len(args) >= 2:
        sys.exit(cmd_append(args[0], args[1:]))
    sys.exit(__doc__)


if __name__ == "__main__":
    main()
