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

🔴 VERBATIM IS THE DEFAULT (v3, 2026-08-30 — Codex, reproduced by PROME). v2 near-matched a
missing line against EVERY destination line and exited 0 if anything resembled it. That let a
GENUINELY DELETED line be "explained" by a surviving SIBLING: source with RULE A and RULE B
differing by one word, destination drops B, v2 printed "CONSERVED (no loss)" rc=0 on a 90% match
to A. SIMILARITY TO ANY LINE CANNOT ESTABLISH LINEAGE.

The v2 change had been made to stop a false "content lost" on a benign in-place edit — and that
is the trap worth naming: FIXING A FALSE ALARM BY LOOSENING THE CHECK CONVERTS A NOISY-BUT-SAFE
FAILURE INTO A SILENT-AND-UNSAFE ONE. For a conservation verifier the only acceptable direction
is fail-closed. Two corrections restore it:
  (a) the near-match pool is `added` ONLY — destination lines with no exact source counterpart,
      consumed one-for-one. A line already accounted for by its own exact match cannot also
      explain a different missing line.
  (b) candidates are REPORTED, never accepted. Exit 0 requires --adjudicated: exact old->new
      pairs the CALLER has verified. A bogus pair cannot launder a deletion, because (a) leaves
      the deleted line with no candidate at all.

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

EXIT: 0 = every source line present verbatim or caller-adjudicated · 1 = anything unaccounted
      for (missing outright, OR an unadjudicated candidate edit) · 2 = bad invocation.
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
                    help="similarity above which an UNEXPLAINED destination line is offered as an "
                         "edit CANDIDATE (default 0.75). Candidates are reported, never accepted.")
    ap.add_argument("--adjudicated", metavar="FILE",
                    help="TSV of <old-line>\t<new-line> pairs the CALLER has verified as in-place "
                         "edits. ONLY these are accepted; anything else missing is still LOST. "
                         "Without this, an edited line fails — verbatim is the default.")
    ap.add_argument("--strict-edit", action="store_true",
                    help="deprecated no-op: verbatim-only is now the DEFAULT.")
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
    # 🔴 THE POOL MUST EXCLUDE DESTINATION LINES ALREADY EXPLAINED BY AN EXACT MATCH.
    # v2 near-matched against EVERY destination line, so a DELETED line could be
    # "explained" by its resemblance to a SURVIVING SIBLING and the run exited 0.
    # Reproduced 2026-08-30 (Codex, via PROME): source has RULE A and RULE B differing
    # by one word; destination drops B entirely; v2 printed "CONSERVED (no loss)" rc=0,
    # matching the deleted B against the surviving A at 90%.
    # SIMILARITY TO ANY LINE CANNOT ESTABLISH LINEAGE. The only defensible candidate for
    # "B was edited into X" is an X that NOTHING ELSE accounts for — i.e. the multiset
    # `added` (destination lines with no exact source counterpart), consumed one-for-one.
    pool = list(added.elements())
    cand, lost = [], []
    for line, n in missing.most_common():
        near = difflib.get_close_matches(line, pool, n=1, cutoff=a.edit_threshold)
        if near:
            pool.remove(near[0])          # one destination line explains at most one source line
            cand.append((line, n, near[0]))
        else:
            lost.append((line, n, None))

    # Adjudication: only caller-supplied exact old->new pairs are ACCEPTED as edits.
    adj = set()
    if a.adjudicated:
        for raw in pathlib.Path(a.adjudicated).read_text(errors="replace").split("\n"):
            if "\t" in raw:
                o_, n_ = raw.split("\t", 1)
                adj.add((o_, n_))
    accepted = [(l, n, near) for l, n, near in cand if (l, near) in adj]
    unaccepted = [(l, n, near) for l, n, near in cand if (l, near) not in adj]
    edited = accepted
    # `lost` stays ONLY the truly-unmatched — a line the CONTENT LOST section can honestly
    # say nothing resembles. Unaccepted candidates are unexplained too and block exit 0,
    # but they get their own section: printing them under "nothing resembles them" while
    # showing a 99% match directly above would be a report contradicting itself.

    if unaccepted:
        print(f"\n⚠ CANDIDATE EDITS — {len(unaccepted):,} missing line(s) resemble an otherwise "
              f"unexplained destination line. NOT ACCEPTED and NOT counted as conserved: "
              f"similarity is a hint, never proof of lineage. Verify each pair yourself, then "
              f"pass them via --adjudicated to accept:")
        for i, (line, n, near) in enumerate(unaccepted):
            if i >= a.show:
                print(f"    … and {len(unaccepted)-a.show:,} more")
                break
            sm = difflib.SequenceMatcher(None, line, near)
            ops = [o for o in sm.get_opcodes() if o[0] != "equal"]
            print(f"  [{n}x, {sm.ratio():.0%} match]")
            if ops:
                _, i1, i2, j1, j2 = ops[0]
                print(f"    was …{line[max(0,i1-45):i2+45]}…")
                print(f"    now …{near[max(0,j1-45):j2+45]}…")
            else:
                print(f"    was: {line[:150]}")
                print(f"    now: {near[:150]}")

    if edited:
        print(f"\n✔ ADJUDICATED EDITS — {len(edited):,} line(s) the caller verified as in-place "
              f"changes:")
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

    if lost or unaccepted:
        bits = []
        if lost:
            bits.append(f"{len(lost):,} with no counterpart")
        if unaccepted:
            bits.append(f"{len(unaccepted):,} unadjudicated candidate edit(s)")
        print(f"\n✗ NOT CONSERVED — {' + '.join(bits)} unaccounted for. "
              f"Verbatim is the default: a resemblance does not close the gap. "
              f"Adjudicate real edits explicitly (--adjudicated) or restore the content.")
        return 1

    if edited:
        print(f"\n✅ CONSERVED: every source line is present verbatim, or covered by a "
              f"caller-adjudicated in-place edit ({len(edited)} adjudicated).")
        return 0
    print("\n✅ CONSERVED: every source line appears in the outputs. Nothing lost.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
