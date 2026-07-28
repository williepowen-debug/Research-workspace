#!/usr/bin/env python3
"""
position_agreement_check.py — positive position-surface AGREEMENT check.

Companion to ledger_staleness.py, which compares AGES and therefore passes a
file that is brand new and affirmatively false. Live instance (VIOLET,
2026-07-28, KB-VIO-142): TRADE.md read 'ACTIVE POSITIONS: **None.**' for 17
hours while $287.70 was live into FOMC — and `ledger_staleness.py VIOLET
--trade` returned 'ok +2d'. A staleness check cannot catch a fresh lie; the
missing test is AGREEMENT with the position state STATUS.md declares, not age.
[[finding_freshness_check_cannot_catch_a_fresh_lie]]

Check: every card token (TRY-*) that STATUS.md carries in LIVE context
(FILLED/LIVE/OPEN wording, no past-tense death word) must be NAMED in the
agent's trade/position surface (TRADE.md / trade/TRADE.md / TRADE_BOOK.md /
POSITIONS.md — same glob set as ledger_staleness --trade). A trade surface
asserting 'ACTIVE POSITIONS: None' while STATUS carries a FILLED card fails
loud, as does a frozen-bannered trade surface on an agent with live capital.

Exit code: 1 on any disagreement — this IS a gate, unlike ledger_staleness.
0 when clean, or when the agent has no trade surface / no live card tokens
(nothing to disagree about).

⚠️ SCOPE (v1, stated so nobody reads it as broader): card-token (TRY-*) class
only. Positions carrying no card id — direct Will entries, share lots, the
USO 150/165 tail-rider — are NOT covered. Extending coverage means extending
LIVE_TOKEN_RE or adopting per-agent declared-position lines, not trusting
this check to see what it cannot. Second limit: the check cannot tell "my
position" from "a live position my STATUS discusses" (NEXUS/WALTER mention
live cards in synthesis) — it only gates agents that HAVE a trade surface,
where mentions are overwhelmingly the agent's own book; a synthesis agent
that later adds a TRADE.md may need a mentions-allowlist here.

Usage:
  python3 scripts/position_agreement_check.py VIOLET        # one agent
  python3 scripts/position_agreement_check.py --all         # every AGENTS/*/STATUS.md
  python3 scripts/position_agreement_check.py --all --quiet # print only disagreements
"""
import argparse
import glob
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ledger_staleness import TRADE_GLOBS, is_frozen, resolve_agent_dir  # noqa: E402

# Fleet card-id convention: TRY-FIRE-004, TRY-VIOLET-VIXCS, TRY-FIRE-006, ...
LIVE_TOKEN_RE = re.compile(r"\bTRY-[A-Z]+(?:-[A-Z0-9]+)+\b")

# LIVE context = canonical fill markers (FILLED/rides, any case) plus
# ALL-CAPS "LIVE". Case matters and was derived from both real corpora
# (2026-07-28 first runs): genuine position state is always EMPHASIZED caps —
# "### 🔴 LIVE — `TRY-VIOLET-VIXCS`", "is **LIVE**" — while every observed
# false positive was lowercase prose ("live broker book", "the now-live 004
# book", "closest-to-live"; TERRY, 2 FPs). Case-insensitive \bLIVE\b was
# tried and REVERTED same-day. NOTE "OPEN" is deliberately absent (prose:
# "trial opens", "open for Will").
# DEAD words are PAST-TENSE/VERDICT forms only, deliberately: "MANDATORY EXIT
# 7/30" is a future instruction on a LIVE position and must NOT read as dead
# (the VIXCS card carries exactly that text).
LIVE_FILL_RE = re.compile(r"\b(FILLED|RIDES?)\b", re.IGNORECASE)
LIVE_CAPS_RE = re.compile(r"(?<![\w/-])LIVE(?![\w/-])")  # case-SENSITIVE
DEAD_WORDS_RE = re.compile(
    r"\b(EXITED|CLOSED|EXPIRED|SHELVED|NO-FILL|NO-TRADE|NO[- ]ENTRY|LAPSED|"
    r"RETIRED|WRITTEN[- ]OFF|NOT[- ]FILLED|CANCELLED|ABANDONED)\b",
    re.IGNORECASE,
)
NONE_ASSERT_RE = re.compile(r"ACTIVE\s+POSITIONS?\s*:?\s*\**\s*None\b", re.IGNORECASE)
# Kept tight so a NEIGHBORING card's fill text can't bleed into this token's
# context (a card's own fill marker sits adjacent to its id; far text is noise).
CTX = 160  # chars of context either side of a token mention


def read(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return None


def live_tokens(status_text):
    """Tokens with at least one PER-MENTION live context: a fill marker (or
    caps-LIVE) with no death word in that SAME context window.
    Per-mention, not aggregated across mentions, deliberately: a global
    any-death-kills rule was tried and REVERTED same-day — one stray prose
    'closed' ('closed the loop' class) in 1 of 13 TRY-FIRE-004 mentions
    vetoed a card with three clean FILLED contexts (TERRY, 2026-07-28).
    Death words only veto the mention they co-occur with ('FILLED ... later
    EXITED' in one breath = dead; fleet practice annotates state changes
    adjacent to the fill record, so an exited card's mentions carry their
    own death word)."""
    live = set()
    for m in LIVE_TOKEN_RE.finditer(status_text):
        ctx = status_text[max(0, m.start() - CTX): m.end() + CTX]
        if ((LIVE_FILL_RE.search(ctx) or LIVE_CAPS_RE.search(ctx))
                and not DEAD_WORDS_RE.search(ctx)):
            live.add(m.group(0))
    return sorted(live)


def check_agent(agent_dir):
    """Returns (name, findings:list[str], checked:bool)."""
    name = os.path.basename(agent_dir.rstrip("/"))
    status_text = read(os.path.join(agent_dir, "STATUS.md"))
    if status_text is None:
        return name, [], False
    tokens = live_tokens(status_text)
    if not tokens:
        return name, [], True  # nothing live-declared -> nothing to disagree about
    surfaces = []
    for gp in TRADE_GLOBS:
        surfaces.extend(glob.glob(os.path.join(agent_dir, gp)))
    if not surfaces:
        return name, [], True  # no designated trade surface -> out of scope
    findings = []
    for surf in sorted(set(surfaces)):
        rel = os.path.relpath(surf, REPO)
        text = read(surf) or ""
        if is_frozen(surf):
            findings.append(
                f"{rel} carries a FROZEN/static banner while STATUS declares live "
                f"card(s) {', '.join(tokens)} — a live book's position surface cannot be frozen"
            )
            continue
        if NONE_ASSERT_RE.search(text):
            findings.append(
                f"{rel} asserts 'ACTIVE POSITIONS: None' while STATUS declares live "
                f"card(s) {', '.join(tokens)} — the fresh-lie class, fail loud"
            )
        for tok in tokens:
            if tok not in text:
                findings.append(
                    f"{rel} never names {tok}, which STATUS carries as LIVE/FILLED"
                )
    return name, findings, True


def main():
    ap = argparse.ArgumentParser(
        description="Positive check: trade surface must AGREE with STATUS's live positions (age is not agreement)."
    )
    ap.add_argument("agent", nargs="?", help="agent name (VIOLET) or path (AGENTS/VIOLET)")
    ap.add_argument("--all", action="store_true", help="scan every AGENTS/* with a STATUS.md")
    ap.add_argument("--quiet", action="store_true", help="print only disagreements")
    args = ap.parse_args()

    if args.all:
        dirs = sorted(os.path.dirname(p) for p in glob.glob(os.path.join(REPO, "AGENTS", "*", "STATUS.md")))
    elif args.agent:
        d = resolve_agent_dir(args.agent)
        if not d:
            print(f"error: agent dir not found for '{args.agent}'", file=sys.stderr)
            return 2
        dirs = [d]
    else:
        ap.print_help()
        return 2

    total = 0
    for d in dirs:
        name, findings, checked = check_agent(d)
        if findings:
            total += len(findings)
            for f in findings:
                print(f"🔴 [{name}] {f}")
        elif not args.quiet and checked:
            print(f"[{name}] agree ✓")
    if total:
        print(f"→ {total} position-surface disagreement(s). STATUS is canonical; fix the trade surface, not this check.")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
