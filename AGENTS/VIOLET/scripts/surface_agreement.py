#!/usr/bin/env python3
"""Cross-surface agreement — the same number must read the same on every surface.

WHY THIS EXISTS (three recurrences in one day, 2026-09-04)
----------------------------------------------------------
VIOLET publishes the same figures on four surfaces with four different readers:
`STATUS.md` (canonical), `NEXUS_BRIEF.md` (NEXUS reads it INSTEAD of STATUS),
`SCRATCH.md` (my own next boot) and `LAST_COMPLETION.md` (PROME). They are
written at different moments in a session, so they drift — and every existing
check was blind to it:

  · `writeback_order_check.py` compares VINTAGE, never content — it says so.
  · `convergence_score.py` verifies STATUS against ITSELF, never the other three.
  · `closeout_guard.py` aggregates both and returned GREEN over the drift.

Measured on 2026-09-04 after two correction passes that each claimed the class
was swept: the convergence score was live as **29/50** on STATUS and the brief's
header, **26/55** in the brief's own VIEW and in SCRATCH, and LAST_COMPLETION
narrated **"26 → 25"** beside a declared **29/50**. Four surfaces, three numbers,
all green.

🔑 **A summary block is rewritten from memory while the body is rewritten from
data, so the summary is where a corrected number goes to die.** Sweeping the
instances a reviewer quotes does not fix it — that was tried twice here. The only
thing that holds is a check that reads every surface and refuses to agree with
itself.

WHAT IT CHECKS
--------------
For each registered figure: extract every occurrence across the surfaces and
require them to be identical. A figure absent from a surface is fine — silence
is not disagreement. **Two different values IS disagreement, and it fails.**

⚠️ It cannot tell you WHICH value is right; it tells you they cannot all be.
STATUS is canonical by convention, so fix the others to match it — after
re-deriving from the data, never by copying the majority.

Exit codes: 0 = every registered figure agrees; 1 = at least one disagreement.
"""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path

AGENT_DIR = Path(__file__).resolve().parent.parent
REPO = AGENT_DIR.parent.parent

# ⚠️ RE-POINTED 2026-09-06 — the fourth surface was `LAST_COMPLETION.md` until
# the PROME delivery contract re-keyed (spec 2026-08-13; home fixed to
# PROME/inbox/ 2026-09-05) to a DATED memo. 🔑 Freezing the old file without
# re-pointing here would have been WORSE than leaving both alone: a frozen file
# keeps its last-session figures forever, so this BLOCKING check would have
# reported a real-looking cross-surface disagreement at every future closeout —
# a guard manufacturing the exact defect it was built to catch.
SURFACE_SPECS = [
    "STATUS.md", "NEXUS_BRIEF.md", "SCRATCH.md", "PROME/inbox/*_from-VIOLET_*.md",
]


# ⚠️ See writeback_order_check.py: PROME `git mv`s consumed packets to
# `PROME/inbox/processed/`, so a glob on the live inbox alone reports MISSING for
# every memo that was actually DELIVERED. Both locations count.
MEMO_DIRS = ("PROME/inbox", "PROME/inbox/processed")


def resolve(spec: str) -> list[Path]:
    """Spec -> every concrete path it names.

    ⚠️ A glob returns ALL matches and the caller reads them TOGETHER, rather than
    picking one "newest". Two reasons, and the second is the better one:
    ① a date prefix cannot order two packets sent the same day (v1 picked by slug,
      so a 10:4x addendum lost to a 10:2x memo because "a" < "f"); and
    ② **for THIS check, every delivered memo is in scope anyway** — if an addendum
      states a different convergence score or FT-10 count from the memo it amends,
      that is a genuine cross-surface disagreement and exactly what this exists to
      catch. Reading only the "latest" would hide it.
    An empty list means no memo — reported as MISSING, which is correct: a closeout
    that delivered nothing to PROME has an unwritten surface, not an agreeing one."""
    if "*" not in spec:
        return [AGENT_DIR / spec]
    pat = spec.rsplit("/", 1)[-1]
    return [x for d in MEMO_DIRS for x in (REPO / d).glob(pat)]


# Display label -> resolved path. Labels stay short so the report columns line up.
SURFACES = [spec.split("/")[-1] if "*" not in spec else "PROME memo"
            for spec in SURFACE_SPECS]
RESOLVED = dict(zip(SURFACES, (resolve(s) for s in SURFACE_SPECS)))

# name -> (value regex, REQUIRED CONTEXT within ±CTX chars, human hint)
# ⚠️ The context requirement is not decoration. v1 matched a bare `N/50|55|60`
# and flagged "October 30/35/60 calls" — an OPTION STRIKE LIST — as a convergence
# score on three surfaces. A cross-surface checker that cries wolf is one you
# switch off, which would leave the class it exists for uncovered.
CTX = 90
FIGURES = {
    "convergence score": (
        re.compile(r"\b(\d{1,2}/(?:50|55|60))\b"),
        re.compile(r"convergence", re.I),
        "STATUS § CONVERGENCE MATRIX is canonical; the scale is declared there",
    ),
    "thesis rows since v4.0": (
        re.compile(r"\b(\d{1,3})\s+(?:KB\s+)?rows? since\b", re.I),
        None,
        "recompute with scripts/thesis_bump_check.py — never restate from memory",
    ),
    "FT-10 sustain count": (
        # WORD form only. `\d/4` also matches the DATE "9/4", which is on every
        # surface in this desk's files — a second false positive of exactly the
        # kind the CTX note above describes.
        re.compile(r"\b(\d)\s+of\s+4\b", re.I),
        re.compile(r"FT-10|sustain", re.I),
        "RED-owned; CBOE bars only",
    ),
}

# Retrospective prose legitimately quotes a superseded number. These markers, in
# the 120 chars before a match, mean "this is history" — the same exclusion the
# CANARY_MAP matcher needs, for the same reason.
HISTORY = re.compile(
    r"prior|was\b|until|superseded|read \"|previously|corrected from|"
    r"→|->|instead of|not\b|no longer|used to|earlier|stale", re.I)


def occurrences(text: str, rx: re.Pattern, ctx: re.Pattern | None) -> set[str]:
    found = set()
    for mo in rx.finditer(text):
        window = text[max(0, mo.start() - CTX): mo.end() + CTX]
        if ctx is not None and not ctx.search(window):
            continue                     # not this figure — see the CTX note above
        if HISTORY.search(text[max(0, mo.start() - 120):mo.start()]):
            continue
        found.add(mo.group(1))
    return found


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args(argv)

    texts = {}
    for s in SURFACES:
        paths = [p for p in RESOLVED.get(s, []) if p.exists()]
        if not paths:
            print(f"  🔴 {s} IS MISSING — cannot certify cross-surface agreement.")
            return 1
        # Multiple memos are read TOGETHER — see resolve(). Newest first so the
        # ±CTX windows never straddle a file boundary.
        texts[s] = "\n\n".join(
            p.read_text(encoding="utf-8") for p in sorted(paths, reverse=True))

    problems = []
    for name, (rx, ctx, hint) in FIGURES.items():
        per = {s: occurrences(t, rx, ctx) for s, t in texts.items()}
        seen = set().union(*per.values())
        if len(seen) <= 1:
            if not a.quiet:
                v = next(iter(seen)) if seen else "—"
                print(f"  ✓ {name:26s} {v}")
            continue
        problems.append((name, per, hint))

    for name, per, hint in problems:
        print(f"\n  🔴 {name.upper()} DISAGREES ACROSS SURFACES:")
        for s in SURFACES:
            if per[s]:
                print(f"     {s:20s} {', '.join(sorted(per[s]))}")
        print(f"     → {hint}")
        print(f"     ⚠️  This check cannot say which is right — only that they cannot all be.")

    if problems:
        print(f"\n  🔴 CROSS-SURFACE DISAGREEMENT — {len(problems)} figure(s). "
              f"Fix the non-canonical surfaces by RE-DERIVING, not by copying.")
        return 1
    if not a.quiet:
        print("\n  ✓ every registered figure reads the same on every surface.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
