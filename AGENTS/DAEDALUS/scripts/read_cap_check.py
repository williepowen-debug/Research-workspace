#!/usr/bin/env python3
"""read_cap_check.py — is a boot-read surface still READABLE WHOLE?

WHY THIS EXISTS (2026-08-23). DAEDALUS's STATUS byte budget was declared 2026-08-17
as 48,000 B, derived from a density snapshot (752 B/line x ~64 lines). That is a
CONSTANT SIZED FROM A PROXY, and it decayed twice over:
  1. density moved (752 -> ~1,489 -> ~1,000 B/line), so the constant silently bought
     half what it was sized for while still reading "satisfied"; and worse,
  2. DENSITY WAS NEVER THE BINDING CONSTRAINT. The real one is the harness single-read
     token cap: past it, a boot read returns a PARTIAL file and the protocol stays
     written while execution quietly degrades to fragments (PAT-111, self-audit F37).
     48,000 B works out to ~88% of that cap -- i.e. the old budget LICENSED a STATUS
     that could not be read whole.

So this check measures against the cap that actually bites, and re-derives rather
than trusting a stored number.

EVIDENCE FOR THE RATIO (both from real Read calls in one session, 2026-08-23):
  (A) TRUNCATION: FLEET_MAP.tsv, 65,725 B -> harness reported "30253 tokens, cap 25000"
      and returned a partial view.  => 2.17 B/token on this file class.
  (B) NON-TRUNCATION: STATUS.md at 46,152 B read WHOLE, so it was under 25,000 tokens
      => its ratio must be >= 1.85 B/token. CONSISTENT with (A).
  Two points, one on each side of the cap. NOT a single-point fit.

⚠️ THE RATIO IS CONTENT-DEPENDENT AND THIS IS ITS WEAKEST LEG. Fleet markdown is dense
(emoji, box-drawing, unicode arrows, bold markers, jargon), which tokenizes far worse
than prose: a naive 4 B/token assumption UNDER-COUNTS tokens by ~1.8x, and under-counting
is the DANGEROUS direction. If a tokenizer becomes available, replace the estimate and
delete this paragraph -- do not keep both.

WHAT A PASS PROVES (PAT-074 / PAT-129 -- state the perimeter, and its edge):
  rc0 means THE NAMED FILES are estimated under the target utilisation of the read cap.
  It does NOT prove: (a) the harness cap is still 25,000 -- that is an OBSERVED constant
  and nothing here re-derives it; (b) the ratio holds for this file's current content;
  (c) any file NOT passed on the command line is fine. This check has no registry and
  enumerates nothing on its own -- it is blind to every surface you do not name.

Exit contract (CHECK_STANDARD §9):
  0 = clean   1 = FINDINGS (at/over target)   2 = CANNOT-CERTIFY (unreadable/missing)

Usage (cwd-proof):
    python3 "$(git rev-parse --show-toplevel)/AGENTS/DAEDALUS/scripts/read_cap_check.py" [FILE ...]
    (DAEDALUS mandated-set + --all tree sweep; the FLEET per-desk tool is scripts/read_cap_check.py --agent/--fleet)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
REPO = os.path.normpath(os.path.join(ROOT, "..", ".."))

# CONSTANTS ARE OWNED BY THE SHARED FLEET TOOL (scripts/read_cap_check.py, P1 Will-approved
# 2026-08-28). Imported, never restated — two copies of 25,000 / 2.17 / 0.60 is the PAT-006 drift
# this very file exists to catch. Import failure is rc 2, never a silent local fallback (PAT-106).
sys.path.insert(0, os.path.join(REPO, "scripts"))
try:
    from read_cap_check import READ_CAP_TOKENS, BYTES_PER_TOKEN, TARGET_UTILISATION  # noqa: E402
except Exception as _e:  # pragma: no cover
    print(f"read-cap check: CANNOT-CERTIFY — shared constants unimportable from scripts/read_cap_check.py ({_e})")
    sys.exit(2)
WARN_UTILISATION = 0.50

# THE MANDATED-READ SET. Must track DAEDALUS CLAUDE.md SPAWN PROTOCOL steps 1-4 plus the
# always-loaded charter. ⚠️ THIS LIST IS ITSELF A REGISTER AND REGISTERS GO INCOMPLETE:
# v1 (2026-08-23, three hours old) shipped with EVOLUTION.md MISSING while EVOLUTION sat at
# 140% of the cap -- a mandated conditional read that the check could not see. The docstring
# correctly warned "blind to every file not named" and the list was still wrong.
# DOCUMENTING A PERIMETER IS NOT THE SAME AS POPULATING IT (PAT-129, refined on its own author).
# That is why --all exists: do not rely on this list alone to answer "did we get it all?"
DEFAULTS = [os.path.normpath(os.path.join(ROOT, f)) for f in (
    "STATUS.md",            # SPAWN step 1
    "FLEET_DIRECTORY.md",   # SPAWN step 2 -- the HOT index. Re-homed 2026-08-23: FLEET_MAP.tsv
                            # was the step-2 read at 121% of the cap, truncating every boot for
                            # ~6 days. Rotating its Gaps narrative to FLEET_MAP_HISTORY.tsv got it
                            # to 43,006 B -- still over, and squeezing further would have deleted
                            # live gap content -- so the register went COLD (read per-agent /
                            # whole at a Production Review) and this generated view became the
                            # read. FLEET_MAP.tsv is deliberately ABSENT from this list now; it is
                            # a cold half, and --all correctly reports it as discovery, not defect.
    "PATTERNS_HOT.md",      # SPAWN step 3
    "EVOLUTION.md",         # SPAWN step 4 (conditional -- still a mandated read when it fires)
    "CLAUDE.md",            # always-loaded charter
)]


def sweep_tree(root):
    """Every .md/.tsv under root except archives -- so the check cannot be blind by omission."""
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in ("archive", "_archive", "reference")]
        for fn in filenames:
            if fn.endswith((".md", ".tsv")):
                out.append(os.path.join(dirpath, fn))
    return sorted(out)

budget_tokens = READ_CAP_TOKENS * TARGET_UTILISATION
budget_bytes = int(budget_tokens * BYTES_PER_TOKEN)


def main(argv):
    args = argv[1:]
    sweep_all = "--all" in args
    args = [a for a in args if a != "--all"]
    if sweep_all:
        paths = sweep_tree(ROOT)
    else:
        paths = args or DEFAULTS
    findings, cannot = [], []
    lines = []
    for p in paths:
        try:
            b = os.path.getsize(p)
        except OSError as e:
            cannot.append(f"{os.path.basename(p)} ({e.__class__.__name__})")
            continue
        tok = b / BYTES_PER_TOKEN
        util = tok / READ_CAP_TOKENS
        if util >= TARGET_UTILISATION:
            mark, over = "🔴", int(b - budget_bytes)
            findings.append(f"{os.path.basename(p)} {util:.0%} of read cap (+{over:,} B over budget)")
        elif util >= WARN_UTILISATION:
            mark, over = "🟠", 0
        else:
            mark, over = "✅", 0
        if not (sweep_all and mark == "✅"):   # sweep mode prints only what needs a look
            shown = os.path.relpath(p, ROOT) if sweep_all else os.path.basename(p)
            # ⚠️ SIZE ALONE IS NOT A DEFECT. Only a MANDATED READ that cannot be read whole is
            # broken; a large cold/on-demand file is the hot-cold split WORKING. Measured on the
            # first --all run: 12 flagged, 3 real -- a ~75% false-positive rate against "is this
            # broken", which is alert fatigue and trains its reader to ignore it (the exact trap
            # flagged in PROME's D3 the same day). So --all LABELS, it does not uniformly alarm.
            tag = " ⟵ MANDATED READ" if os.path.normpath(p) in {os.path.normpath(d) for d in DEFAULTS} else ""
            lines.append(f"  {mark} {shown:<46}{b:>8,} B  ~{tok:>7,.0f} tok  {util:>5.0%} of cap"
                         + (f"  → TRIM {over:,} B" if over > 0 else "") + tag)

    print(f"read-cap check — budget {budget_bytes:,} B "
          f"({budget_tokens:,.0f} tok = {TARGET_UTILISATION:.0%} of the {READ_CAP_TOKENS:,}-tok read cap "
          f"@ {BYTES_PER_TOKEN} B/tok measured)")
    for l in lines:
        print(l)

    if cannot:
        print(f"⚠️  CANNOT-CERTIFY: could not size {len(cannot)} file(s): {', '.join(cannot)}")
        return 2
    if findings:
        if sweep_all:
            mand = [f for f in findings if f.split()[0] in {os.path.basename(d) for d in DEFAULTS}]
            print(f"⚠️  {len(findings)} file(s) over budget, of which {len(mand)} are MANDATED READS "
                  f"(the actual defects): {'; '.join(mand) if mand else 'none'}")
            print("    ⚠️  The rest are DISCOVERY, not verdicts — a large COLD or ON-DEMAND file is the "
                  "hot/cold split WORKING, not a defect. Triage before acting: PATTERNS.tsv and "
                  "FLEET_MAP_HISTORY.tsv are cold halves BY DESIGN; *_READER_REPORTS are single-review "
                  "evidence companions. Ask 'does a mandated read name it?' before trimming anything.")
        else:
            print(f"⚠️  {len(findings)} file(s) AT OR OVER budget — trim, rotate, or relocate: {'; '.join(findings)}")
        print("    ⛔ Do NOT respond by raising the budget: the read cap is not ours to move.")
        return 1
    if sweep_all:
        print(f"✅ all {len(paths)} file(s) under {TARGET_UTILISATION:.0%} of the read cap "
              f"(tree sweep of {ROOT}, archives excluded).")
    else:
        print(f"✅ all {len(paths)} named file(s) under {TARGET_UTILISATION:.0%} of the read cap. "
              f"⚠️ Says nothing about surfaces not named — run --all to sweep the tree.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
