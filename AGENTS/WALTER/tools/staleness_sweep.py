#!/usr/bin/env python3
"""BOARD staleness sweep — CANDIDATE GENERATION ONLY, never auto-tags.

Per SIGNAL_FORMAT_SPEC v0.10 Signal Lifecycle section: greps signal bodies for
three structural staleness patterns and emits a candidate list for WALTER
adjudication. Grep patterns WILL have false negatives (framing staleness isn't
always lexical) — acceptable by design; the BOARD/INDEX.md section-preamble
blanket rule covers what the sweep misses.

Patterns:
  P1 forward-date/event language (candidate EVENT-PASSED)
  P2 superseded war-frame language, IRAN_HORMUZ-adjacent (candidate SUPERSEDED)
  P3 trigger/threshold state-claims (candidate SUPERSEDED/FALSIFIED — cross-check
     against FALSIFICATION_FIRED_LOG.tsv / REG_THRESHOLDS_FIRED_LOG.tsv + tape)

Skips signals already carrying a status: field. Output: TSV to stdout
(file, patterns, snippets).

Usage: python3 staleness_sweep.py [--before YYYYMMDD]  (default: all files)
"""
import re
import sys
from pathlib import Path

BOARD = Path(__file__).resolve().parents[3] / "BOARD"

P1 = re.compile(
    r"(expir\w*|deadline|window closes|watch (?:for|over) the next|"
    r"next \d+ (?:weekly )?(?:prints?|sessions?|weeks?)|pricing expected|"
    r"verify against .{0,40}(?:prints?|earnings) when they hit|"
    r"by (?:early |mid-|late )?(?:Apr(?:il)?|May|Jun(?:e)?) \d{1,2})", re.I)
P2 = re.compile(
    r"(ceasefire (?:holding|intact|expires|under)|blockade.{0,25}(?:surviv|lift)|"
    r"largely negotiated|deal (?:imminent|close\b)|rhetoric(?:al)?[- ]only|"
    r"MOU (?:acceptance|suspension)|reopening|talks (?:resum|continu)|"
    r"Project Freedom|Epic Fury)", re.I)
P3 = re.compile(
    r"(RED-FT-\d|REG-T-\d|kill[- ]rule|sustain(?:ed)? trigger|entrenched|"
    r"threshold (?:cross|fire|pierc)\w*|direction[- ]flip)", re.I)


def main():
    before = None
    if "--before" in sys.argv:
        before = sys.argv[sys.argv.index("--before") + 1]
    rows = []
    for f in sorted(BOARD.glob("SIG-W-*.md")):
        date = f.name[6:14]
        if before and date >= before:
            continue
        text = f.read_text(errors="replace")
        if re.search(r"^status:", text, re.M):
            continue  # already lifecycle-tagged
        hits = {}
        for tag, pat in (("P1", P1), ("P2", P2), ("P3", P3)):
            m = pat.findall(text)
            if m:
                flat = [x if isinstance(x, str) else x[0] for x in m]
                hits[tag] = sorted(set(s.strip()[:40] for s in flat))[:4]
        if hits:
            rows.append((f.name, "+".join(sorted(hits)),
                         " | ".join(f"{k}:{';'.join(v)}" for k, v in sorted(hits.items()))))
    print(f"# {len(rows)} candidates of {len(list(BOARD.glob('SIG-W-*.md')))} signals")
    for name, pats, snip in rows:
        print(f"{name}\t{pats}\t{snip}")


if __name__ == "__main__":
    main()
