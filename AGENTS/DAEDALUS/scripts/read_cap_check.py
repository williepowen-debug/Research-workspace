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
"""
import os
import sys

READ_CAP_TOKENS = 25_000      # OBSERVED from a live truncation message, 2026-08-23
BYTES_PER_TOKEN = 2.17        # MEASURED, provenance (A) above -- re-measure on any truncation
TARGET_UTILISATION = 0.60     # headroom for ratio error + intra-session growth
WARN_UTILISATION = 0.50

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULTS = [os.path.normpath(os.path.join(HERE, "..", f))
            for f in ("STATUS.md", "PATTERNS_HOT.md", "FLEET_MAP.tsv")]

budget_tokens = READ_CAP_TOKENS * TARGET_UTILISATION
budget_bytes = int(budget_tokens * BYTES_PER_TOKEN)


def main(argv):
    paths = argv[1:] or DEFAULTS
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
        lines.append(f"  {mark} {os.path.basename(p):<18}{b:>8,} B  ~{tok:>7,.0f} tok  {util:>5.0%} of cap"
                     + (f"  → TRIM {over:,} B" if over > 0 else ""))

    print(f"read-cap check — budget {budget_bytes:,} B "
          f"({budget_tokens:,.0f} tok = {TARGET_UTILISATION:.0%} of the {READ_CAP_TOKENS:,}-tok read cap "
          f"@ {BYTES_PER_TOKEN} B/tok measured)")
    for l in lines:
        print(l)

    if cannot:
        print(f"⚠️  CANNOT-CERTIFY: could not size {len(cannot)} file(s): {', '.join(cannot)}")
        return 2
    if findings:
        print(f"⚠️  {len(findings)} file(s) AT OR OVER budget — trim, rotate, or relocate: {'; '.join(findings)}")
        print("    ⛔ Do NOT respond by raising the budget: the read cap is not ours to move.")
        return 1
    print(f"✅ all {len(paths)} named file(s) under {TARGET_UTILISATION:.0%} of the read cap. "
          f"⚠️ Says nothing about surfaces not named on the command line.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
