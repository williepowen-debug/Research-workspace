#!/usr/bin/env python3
"""measure.py — the SOLE approved source for reported byte counts, line counts,
and crc32 receipts in PROME work (WQ-140, Will-ruled 2026-08-30).

Semantics (labeled, always):
  bytes  = raw on-disk byte count, identical to `wc -c` (NEVER Python len() of a
           decoded string — that is characters; errors #45/#50 in the ledger).
  lines  = newline count, identical to `wc -l` (a file without a final newline
           has its last fragment uncounted, same as wc).
  crc32           = binascii.crc32 over the full raw bytes.
  crc32_no_final_nl = crc32 over raw bytes with EXACTLY ONE terminating b"\\n"
           stripped if present (the DOCKET/archive convention: "EXCLUDING the
           terminating newline" — one, not all trailing).

Every invocation RE-READS the file at receipt time — a receipt is always about
the bytes on disk NOW, never a figure captured before a later edit (errors
#34/#38: stale byte figures printed before the last edit).

Usage:
  measure.py FILE...            one labeled receipt line per file
  measure.py --json FILE...     same, as a JSON list
  measure.py --identical A B    byte-compare two files: rc 0 identical, 1 not
  measure.py --selftest         falsification set (Unicode · missing final
                                newline · multiple trailing newlines ·
                                post-edit remeasure · wc agreement); rc 0/1
"""
import binascii
import json
import os
import subprocess
import sys
import tempfile


def measure(path):
    with open(path, "rb") as f:
        raw = f.read()
    body = raw[:-1] if raw.endswith(b"\n") else raw
    return {
        "path": path,
        "bytes": len(raw),
        "lines": raw.count(b"\n"),
        "crc32": binascii.crc32(raw) & 0xFFFFFFFF,
        "crc32_no_final_nl": binascii.crc32(body) & 0xFFFFFFFF,
    }


def receipt_line(m):
    return (f"{m['path']}  {m['bytes']} B (wc -c)  {m['lines']} lines (wc -l)  "
            f"crc32 {m['crc32']}  crc32-no-final-nl {m['crc32_no_final_nl']}")


def identical(a, b):
    with open(a, "rb") as f:
        ra = f.read()
    with open(b, "rb") as f:
        rb = f.read()
    return ra == rb


def _wc(flag, path):
    out = subprocess.run(["wc", flag, path], check=True, capture_output=True, text=True)
    return int(out.stdout.split()[0])


def selftest():
    failures = []

    def check(name, got, want):
        if got != want:
            failures.append(f"FAIL {name}: got {got!r}, want {want!r}")
        else:
            print(f"  ok  {name}: {got!r}")

    with tempfile.TemporaryDirectory() as d:
        # Known crc32 test vector (published): "The quick brown fox jumps over the lazy dog"
        p = os.path.join(d, "vector.txt")
        with open(p, "wb") as f:
            f.write(b"The quick brown fox jumps over the lazy dog")
        m = measure(p)
        check("published crc32 vector", m["crc32"], 0x414FA339)
        check("no final newline: bytes", m["bytes"], 43)
        check("no final newline: lines (wc -l semantics)", m["lines"], 0)
        check("no final newline: crc equals no-final-nl crc",
              m["crc32"] == m["crc32_no_final_nl"], True)
        check("agrees with wc -c", m["bytes"], _wc("-c", p))
        check("agrees with wc -l", m["lines"], _wc("-l", p))

        # Unicode: bytes are NOT characters
        p = os.path.join(d, "unicode.txt")
        with open(p, "wb") as f:
            f.write("héllo\n".encode("utf-8"))
        m = measure(p)
        check("unicode: bytes (7, not len()=6 chars)", m["bytes"], 7)
        check("unicode: agrees with wc -c", m["bytes"], _wc("-c", p))
        check("unicode: bytes != character count", m["bytes"] != len("héllo\n"), True)

        # Multiple trailing newlines: strip exactly ONE
        p = os.path.join(d, "multinl.txt")
        with open(p, "wb") as f:
            f.write(b"abc\n\n")
        m = measure(p)
        check("multi-trailing-nl: bytes", m["bytes"], 5)
        check("multi-trailing-nl: strips exactly one",
              m["crc32_no_final_nl"], binascii.crc32(b"abc\n") & 0xFFFFFFFF)

        # Empty file
        p = os.path.join(d, "empty.txt")
        open(p, "wb").close()
        m = measure(p)
        check("empty: bytes", m["bytes"], 0)
        check("empty: crc32", m["crc32"], 0)

        # Post-edit remeasure: a receipt is about the bytes on disk NOW
        p = os.path.join(d, "edit.txt")
        with open(p, "wb") as f:
            f.write(b"before\n")
        m1 = measure(p)
        with open(p, "ab") as f:
            f.write(b"after, longer than before\n")
        m2 = measure(p)
        check("post-edit remeasure: bytes moved", m2["bytes"], 7 + 26)
        check("post-edit remeasure: crc moved", m1["crc32"] != m2["crc32"], True)
        check("post-edit remeasure: agrees with wc -c", m2["bytes"], _wc("-c", p))

        # --identical
        q = os.path.join(d, "edit2.txt")
        with open(p, "rb") as fsrc, open(q, "wb") as fdst:
            fdst.write(fsrc.read())
        check("identical: byte-for-byte copy", identical(p, q), True)
        with open(q, "ab") as f:
            f.write(b"\n")
        check("identical: one extra newline detected", identical(p, q), False)

    if failures:
        print("\n".join(failures))
        print(f"SELFTEST FAIL ({len(failures)} failing)")
        return 1
    print("SELFTEST PASS (all checks)")
    return 0


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--selftest":
        return selftest()
    if argv[0] == "--identical":
        if len(argv) != 3:
            print("usage: measure.py --identical A B", file=sys.stderr)
            return 2
        same = identical(argv[1], argv[2])
        print(f"{'IDENTICAL' if same else 'DIFFER'}  {argv[1]}  {argv[2]}")
        return 0 if same else 1
    as_json = False
    files = argv
    if argv[0] == "--json":
        as_json = True
        files = argv[1:]
    results = [measure(p) for p in files]
    if as_json:
        print(json.dumps(results, indent=2))
    else:
        for m in results:
            print(receipt_line(m))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
