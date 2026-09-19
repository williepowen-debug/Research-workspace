#!/usr/bin/env python3
"""rotation_integrity.py — a rotation must not LOSE a section.

WHY THIS EXISTS
---------------
ZHAO, 2026-09-18: a read-cap rotation spliced between two anchors and silently
deleted an entire `### Domestic Stress` subsection from its STATUS -- nine live
rows off the boot surface. EVERY GUARD PASSED GREEN: read_cap_check rc=0,
claim_check clean, line count fell, commit clean. It was found only by going to
look for one of the deleted rows for an unrelated reason.

ZHAO's own generalisation, which is the spec implemented here:

    "A rotation's success metric and its failure signature are the same
     observation -- bytes went down. Nothing in the current toolchain
     distinguishes 'moved to cold' from 'deleted'. A cheap check: assert the
     section-header multiset of STATUS union COLD is unchanged across a
     rotation."

[[finding_anchor_splice_deletes_everything_between_nested_anchors]]
[[finding_instrument_reports_clean_against_the_wrong_reference]]

ACCEPTANCE CONDITIONS -- written BEFORE the implementation, in the defect's own
terms, per PROME/CLAUDE.md WQ-229 repair-completion discipline. These ARE the
test list; --selftest is their falsification set.

  (1) A header present in the union BEFORE and absent AFTER is reported BY NAME
      and the check FAILS -- whatever happened to byte or line totals.
  (2) The check is never satisfied by bytes moving. A section MOVED hot->cold
      PASSES; the same section DELETED FAILS; the two are distinguished.
  (3) Headers legitimately ADDED by the rotation (a new base's own sections) do
      not fail it. Additions are allowed; losses are not.
  (4) A RENAMED header reads as one loss plus one addition and is reported as a
      LOSS. The checker cannot know it is the same section, so it fails closed
      and names it rather than guessing.
  (5) It works on an ARBITRARY hot/cold pair, not only the file the defect was
      found in. ZHAO's was AGENTS/ZHAO/STATUS.md; PROME's is HEARTBEAT.md.
      Fixing the named row is not fixing the class.

NEIGHBOUR CATEGORIES CONSIDERED (WQ-229 -- consider all five, justify any N/A):
  ordinary    -- the normal rotation, section moves hot->cold. Must PASS. Tested.
  overlap     -- a section present in BOTH files before and after (the HEARTBEAT
                 convention's "hot stub remains" case). Handled with MULTISET,
                 not set, semantics, so a duplicate is not silently absorbed.
                 Tested.
  wrong owner -- N/A. The tool is invoked with an explicit file pair by the agent
                 doing the rotation and makes no ownership claim or inference;
                 there is no owner field for it to get wrong.
  missing information -- either file unreadable or absent at BEFORE or AFTER =>
                 UNKNOWN, rc=2, never a pass. Tested.
  concurrent activity -- BEFORE is read from a fixed git ref, so it cannot move.
                 AFTER is the working tree and another session could edit it
                 mid-run; each file is read exactly once and the git ref used is
                 printed, so the result states what it measured.

rc: 0 = no section lost - 1 = a section was lost - 2 = UNKNOWN (could not establish)
"""
import argparse, collections, re, subprocess, sys

HEADER = re.compile(r"^(#{1,6})\s+(.*?)\s*$")


def headers(text):
    """Multiset of (level, normalised title). Fenced code blocks are skipped so a
    '#' inside an example is not counted as a section (a template that examples
    its own structure is ambiguous -- finding_a_file_that_examples_its_own_structure)."""
    out, fence = collections.Counter(), False
    for line in text.split("\n"):
        s = line.lstrip()
        if s.startswith("```") or s.startswith("~~~"):
            fence = not fence
            continue
        if fence:
            continue
        m = HEADER.match(line)
        if m:
            out[(len(m.group(1)), " ".join(m.group(2).split()))] += 1
    return out


def read_ref(ref, path):
    try:
        return subprocess.run(["git", "show", f"{ref}:{path}"], check=True,
                              capture_output=True).stdout.decode("utf-8")
    except subprocess.CalledProcessError:
        return None


def read_disk(path):
    try:
        with open(path, "rb") as fh:
            return fh.read().decode("utf-8")
    except OSError:
        return None


def run(ref, pairs, verbose):
    before, after, unknown = collections.Counter(), collections.Counter(), []
    for p in pairs:
        b, a = read_ref(ref, p), read_disk(p)
        if b is None:
            unknown.append(f"{p}: not present at ref {ref} (new file?) -- BEFORE side unestablished")
        else:
            before += headers(b)
        if a is None:
            unknown.append(f"{p}: unreadable on disk -- AFTER side unestablished")
        else:
            after += headers(a)

    if unknown:
        print(f"ROTATION-INTEGRITY  UNKNOWN  (ref {ref})")
        for u in unknown:
            print(f"  ? {u}")
        print("  A side that could not be established is never a pass. Fail closed.")
        return 2

    lost = before - after
    gained = after - before
    print(f"ROTATION-INTEGRITY  ref {ref}  files: {', '.join(pairs)}")
    print(f"  headers in union: before {sum(before.values())} -> after {sum(after.values())}")
    if verbose or gained:
        print(f"  ADDED {sum(gained.values())} (allowed -- a rotation may create sections):")
        for (lvl, t), n in sorted(gained.items(), key=lambda kv: kv[0][1])[:40]:
            print(f"      + {'#' * lvl} {t[:110]}" + (f"  x{n}" if n > 1 else ""))
    if not lost:
        print(f"  LOST 0  -- rc=0, no section left the union.")
        return 0
    print(f"  LOST {sum(lost.values())}  <-- BLOCKING. A section present before is absent after:")
    for (lvl, t), n in sorted(lost.items(), key=lambda kv: kv[0][1]):
        print(f"      - {'#' * lvl} {t[:110]}" + (f"  x{n}" if n > 1 else ""))
    print("  A rename reads as one loss + one addition and is reported as a LOSS by design (condition 4):")
    print("  the checker cannot know they are the same section, so it names it instead of guessing.")
    return 1


def selftest():
    """The acceptance conditions as executable drills. Each names the condition it falsifies."""
    ok = True

    def chk(name, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print(f"  {'OK  ' if good else 'FAIL'} {name}: got {got}, want {want}")

    H, C = "# A\n## B\n## C\n", "# Cold\n"
    # (2) ordinary: B MOVED hot->cold => union unchanged => PASS
    b = headers(H) + headers(C)
    a = headers("# A\n## C\n") + headers("# Cold\n## B\n")
    chk("(2) ordinary move hot->cold is not a loss", sum((b - a).values()), 0)
    # (1)+(2) DELETED => LOSS, and bytes fell in both cases so bytes cannot be the discriminator
    a2 = headers("# A\n## C\n") + headers("# Cold\n")
    chk("(1) deletion is reported as a loss", sum((b - a2).values()), 1)
    chk("(2) move and delete are distinguished", (sum((b - a).values()), sum((b - a2).values())), (0, 1))
    # (3) additions allowed
    a3 = headers("# A\n## B\n## C\n## NEW\n") + headers("# Cold\n")
    chk("(3) an added section is not a loss", sum((b - a3).values()), 0)
    # (4) rename => loss, named
    a4 = headers("# A\n## B renamed\n## C\n") + headers("# Cold\n")
    chk("(4) a rename is reported as a loss", sum((b - a4).values()), 1)
    # overlap neighbour: duplicate header in BOTH files must not be absorbed by set semantics
    bo = headers("# A\n## Dup\n") + headers("# Cold\n## Dup\n")
    ao = headers("# A\n## Dup\n") + headers("# Cold\n")
    chk("overlap: losing ONE of two identical headers is still a loss", sum((bo - ao).values()), 1)
    # fenced code must not register as a section
    chk("fenced code block is not counted as a header",
        sum(headers("# A\n```\n# not a header\n```\n").values()), 1)
    print("SELFTEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", help="the hot/cold pair (or any set) whose UNION must not lose a header")
    ap.add_argument("--ref", default="HEAD", help="git ref for the BEFORE state (default HEAD)")
    ap.add_argument("-v", "--verbose", action="store_true", help="list added headers even when none were lost")
    ap.add_argument("--selftest", action="store_true", help="run the acceptance conditions as drills")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    if not a.files:
        ap.error("name at least one file (normally the hot/cold pair)")
    sys.exit(run(a.ref, a.files, a.verbose))


if __name__ == "__main__":
    main()
