#!/usr/bin/env python3
"""split_verify.py — prove a file split lost NOTHING.

WHY THIS EXISTS (2026-08-30, Codex finding 4). Three surfaces were split this day to
get WALTER's boot path under the read cap (IRAN_WAR 263,371->18,590 · ROUTING_TABLE
121,557->31,764 · MEMORY 79,596->46,327). Each split was proved conservative by an
assertion written inline in the one-off migration script, and those scripts are gone.
The PROOF therefore survived only as prose in commit messages — which is evidence a
reader must trust rather than a check a future session can RE-RUN.

⚠️ THE FAILURE THIS PREVENTS IS SILENT. A split that drops content raises no error:
the destination files parse, every size check improves, and the loss is discovered
only when somebody looks for a line that is no longer anywhere. A rotation is exactly
the operation whose success and whose worst failure look identical from the outside.

SEMANTICS — CONSERVATION IS "NO LOSS", NOT "EQUALITY". Destination files legitimately
gain scaffolding (headers, provenance comments, pointer tables), so the test is a
multiset SUBSET test: every line of the original must appear across the outputs at
least as many times as it appeared in the original. Added lines are reported as a
count, never as an error.

Blank lines are ignored by default (--strict-blank to count them): reflowing blank
lines around lifted blocks is normal and is not content loss.

USAGE
  # verify a split whose original is a git object (the normal case, post-commit)
  tools/split_verify.py --orig <rev>:<path> --into <fileA> <fileB> [<fileC> ...]
  # or from a file on disk
  tools/split_verify.py --orig-file /tmp/before.md --into <fileA> <fileB>

EXIT: 0 = nothing lost · 1 = LINES MISSING (names them) · 2 = bad invocation.
"""
import argparse, collections, subprocess, sys, pathlib


def read_git(spec):
    try:
        r = subprocess.run(["git", "show", spec], capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError) as e:
        sys.exit(f"cannot run git: {e}")
    if r.returncode != 0:
        sys.exit(f"git show {spec} failed: {r.stderr.strip()}")
    return r.stdout


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--orig", help="git object, e.g. HEAD~1:path/to/file.md")
    g.add_argument("--orig-file", help="path to the pre-split file on disk")
    ap.add_argument("--into", nargs="+", required=True, help="resulting file(s)")
    ap.add_argument("--strict-blank", action="store_true", help="count blank lines too")
    ap.add_argument("--show", type=int, default=10, help="how many missing lines to print")
    a = ap.parse_args()

    src = read_git(a.orig) if a.orig else pathlib.Path(a.orig_file).read_text(errors="replace")
    dst = []
    for f in a.into:
        p = pathlib.Path(f)
        if not p.exists():
            sys.exit(f"destination missing: {f}")
        dst.append(p.read_text(errors="replace"))

    keep = (lambda s: True) if a.strict_blank else (lambda s: s.strip() != "")
    o = collections.Counter(l for l in src.split("\n") if keep(l))
    d = collections.Counter(l for t in dst for l in t.split("\n") if keep(l))

    missing = o - d          # lines the original had that the outputs do not cover
    added = d - o
    name = a.orig or a.orig_file
    print(f"source      : {name}")
    print(f"destinations: {', '.join(a.into)}")
    print(f"source lines: {sum(o.values()):,} ({len(o):,} distinct)"
          f"{'' if a.strict_blank else '  [blank lines ignored]'}")
    print(f"output lines: {sum(d.values()):,}")
    print(f"added (scaffolding, expected): {sum(added.values()):,}")

    if missing:
        print(f"\n✗ CONTENT LOST — {sum(missing.values()):,} line-instance(s) "
              f"({len(missing):,} distinct) are in the source and in NO output file:")
        for i, (line, n) in enumerate(missing.most_common()):
            if i >= a.show:
                print(f"    … and {len(missing)-a.show:,} more distinct")
                break
            print(f"  [{n}x] {line[:150]}")
        print("\n  A split must be lossless. Re-run the migration; do not hand-patch"
              "\n  the destinations, or the next verification passes over a repaired symptom.")
        return 1

    print("\n✅ CONSERVED: every source line appears in the outputs. Nothing lost.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
