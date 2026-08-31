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
import argparse, collections, difflib, subprocess, sys, pathlib


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
    ap.add_argument("--edit-threshold", type=float, default=0.75,
                    help="similarity above which a missing line is EDITED, not LOST (default 0.75)")
    ap.add_argument("--strict-edit", action="store_true",
                    help="fail on edited-in-place lines too (use when the split must be byte-verbatim)")
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

    # EDITED-IN-PLACE vs GONE. A subset test cannot tell "this line was deleted" from
    # "this line was edited in the same commit" — both are simply absent. Reporting an
    # edit as CONTENT LOST is not a harmless false alarm: the remediation text says
    # "re-run the migration", which for a benign edit is WRONG ADVICE, and a verifier
    # that cries loss on routine edits is one nobody believes when loss is real.
    # (Found 2026-08-30 by PROME re-running this tool over the CLAUDE.md slim commit:
    # one "lost" line was the doctor step's "30 checks" -> "31 checks" edit.)
    # ⇒ Near-match each missing line against the outputs and SHOW BOTH TEXTS, so the
    # reader judges rather than trusts the classifier. Conservative by construction:
    # anything below the threshold stays LOST, and --strict-edit restores verbatim-only.
    pool = [l for t in dst for l in t.split("\n") if keep(l)]
    edited, lost = [], []
    for line, n in missing.most_common():
        near = difflib.get_close_matches(line, pool, n=1, cutoff=a.edit_threshold)
        (edited if near else lost).append((line, n, near[0] if near else None))

    if edited:
        print(f"\n⚠ EDITED IN PLACE — {len(edited):,} line(s) changed rather than moved. "
              f"NOT content loss; verify each is the change you intended:")
        for i, (line, n, near) in enumerate(edited):
            if i >= a.show:
                print(f"    … and {len(edited)-a.show:,} more")
                break
            sm = difflib.SequenceMatcher(None, line, near)
            # SHOW THE DIFFERING REGION, NOT THE HEAD. On a 99%-match line the change is
            # usually far from the start, so printing line[:150] renders two identical-
            # looking strings and teaches the reader nothing — a decorative report.
            # Window on the first non-equal opcode instead.
            ops = [o for o in sm.get_opcodes() if o[0] != "equal"]
            print(f"  [{n}x, {sm.ratio():.0%} match]")
            if ops:
                _, i1, i2, j1, j2 = ops[0]
                lo, hi = max(0, i1 - 45), i2 + 45
                lo2, hi2 = max(0, j1 - 45), j2 + 45
                print(f"    was …{line[lo:hi]}…")
                print(f"    now …{near[lo2:hi2]}…")
                if len(ops) > 1:
                    print(f"    ({len(ops)} differing region(s); showing the first)")
            else:
                print(f"    was: {line[:150]}")
                print(f"    now: {near[:150]}")

    if lost:
        print(f"\n✗ CONTENT LOST — {sum(n for _, n, _ in lost):,} line-instance(s) "
              f"({len(lost):,} distinct) are in the source, and NOTHING in the outputs "
              f"resembles them:")
        for i, (line, n, _) in enumerate(lost):
            if i >= a.show:
                print(f"    … and {len(lost)-a.show:,} more distinct")
                break
            print(f"  [{n}x] {line[:150]}")
        print("\n  A split must be lossless. Re-run the migration; do not hand-patch"
              "\n  the destinations, or the next verification passes over a repaired symptom.")
        return 1

    if edited and a.strict_edit:
        print("\n✗ --strict-edit: edited lines fail. This split was required to be verbatim.")
        return 1
    if edited:
        print(f"\n✅ CONSERVED (no loss): every source line is present or accounted for as an "
              f"in-place edit ({len(edited)} edited).")
        return 0
    print("\n✅ CONSERVED: every source line appears in the outputs. Nothing lost.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
