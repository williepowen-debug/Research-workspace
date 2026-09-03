#!/usr/bin/env python3
"""
CORAL Boot Sequence — Florida situational card

Modest v1 boot card. This is a situational card, not the full CORAL boot:
read CLAUDE.md and required continuity files before normal execution. Principle:
live pulls for CORAL-owned/Florida-local facts; cross-agent files only for
owned-domain context. This does not rewrite STATUS.md by itself.

Usage:
  python3 AGENTS/CORAL/scripts/boot.py
  python3 AGENTS/CORAL/scripts/boot.py --quick      # skip market price pull
  python3 AGENTS/CORAL/scripts/boot.py --verbose    # include longer snippets
"""

from __future__ import annotations

import re
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
CORAL_DIR = SCRIPTS_DIR.parent
WORKSPACE = CORAL_DIR.parent.parent
FETCH = WORKSPACE / "FORGE" / "tools" / "market-data" / "fetch.py"

PRICE_TICKERS = ["KRE", "WAL", "OZK", "SSB", "SBCF", "BKU", "VLY", "USCB"]
CROSS_AGENT_BRIEFS = [
    ("MARCO", [WORKSPACE / "AGENTS" / "MARCO" / "NEXUS_BRIEF.md", WORKSPACE / "AGENTS" / "MARCO" / "STATUS.md"], ["Status", "VIEW", "CROSS-DOMAIN"]),
    ("REGINALD", [WORKSPACE / "AGENTS" / "REGINALD" / "NEXUS_BRIEF.md", WORKSPACE / "AGENTS" / "REGINALD" / "STATUS.md"], ["Status", "VIEW", "CROSS-DOMAIN"]),
    ("CARL", [WORKSPACE / "AGENTS" / "CARL" / "NEXUS_BRIEF.md", WORKSPACE / "AGENTS" / "CARL" / "STATUS.md"], ["Status", "VIEW", "CROSS-DOMAIN"]),
    ("NEXUS", [WORKSPACE / "AGENTS" / "NEXUS" / "STATUS.md"], ["Regime", "CORAL", "Florida"]),
]

STALE_LIMITS = {
    "STATUS.md": 48,
    "SCRATCH.md": 72,
    "NEXUS_BRIEF.md": 72,
    "thesis/THESIS.md": 720,
    "thesis/CHANGELOG.md": 720,
    "CALENDAR.md": 168,
    "COVERAGE.md": 168,
    "FL_BANK_WATCHLIST.md": 168,
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(WORKSPACE))
    except ValueError:
        return str(path)


_VINTAGE_RE = re.compile(
    r"Last real data refresh:\s*(\d{4})-(\d{2})-(\d{2})", re.IGNORECASE
)


def _vintage_epoch(path: Path) -> float | None:
    """Content-derived vintage: the two-clock header root Data Hygiene (b) wants."""
    try:
        head = path.read_text(errors="replace")[:4000]
    except Exception:
        return None
    m = _VINTAGE_RE.search(head)
    if not m:
        return None
    try:
        return datetime(int(m[1]), int(m[2]), int(m[3])).timestamp()
    except ValueError:
        return None


def _git_commit_epoch(path: Path) -> float | None:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%ct", "--", str(path)],
            cwd=str(WORKSPACE), capture_output=True, text=True, timeout=10,
        )
        if out.returncode == 0 and out.stdout.strip():
            return float(out.stdout.strip())
    except Exception:
        pass
    return None


def file_age(path: Path) -> tuple[float | None, str]:
    """Age with a NON-mtime-primary basis.

    ⛔ mtime is CORRUPTED BY GIT SYNC — a pull restamps every file on the
    receiving box, so an mtime-keyed staleness check reads every ledger as
    FRESH right after a pull and fails FALSE-NEGATIVE (DAEDALUS wiring-sweep
    flag ⑯, 2026-08-28; `finding_mtime_is_corrupted_by_git_sync`).
    Chain, per root CLAUDE.md §Data Hygiene (b): content-derived vintage →
    git-commit time → mtime LAST RESORT (uncommitted files only). The basis is
    printed so a reader can see which clock answered.
    """
    if not path.exists():
        return None, "MISSING"
    epoch, basis = _vintage_epoch(path), "vintage"
    if epoch is None:
        epoch, basis = _git_commit_epoch(path), "git"
    if epoch is None:
        epoch, basis = path.stat().st_mtime, "mtime!"
    age_h = (time.time() - epoch) / 3600
    if age_h < 1:
        return age_h, f"{age_h*60:.0f}m[{basis}]"
    if age_h < 48:
        return age_h, f"{age_h:.1f}h[{basis}]"
    return age_h, f"{age_h/24:.1f}d[{basis}]"


def read_text(path: Path, max_chars: int = 20000) -> str:
    try:
        return path.read_text(errors="replace")[:max_chars]
    except Exception as exc:
        return f"[READ ERROR: {exc}]"


def first_match(text: str, patterns: list[str]) -> str | None:
    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE | re.MULTILINE)
        if m:
            return m.group(1).strip()
    return None


def pending_walter() -> list[Path]:
    inbox = CORAL_DIR / "inbox" / "WALTER"
    if not inbox.exists():
        return []
    return sorted(p for p in inbox.glob("*.md") if p.is_file())


def legacy_inbox_count() -> int:
    inbox = CORAL_DIR / "inbox"
    if not inbox.exists():
        return 0
    return sum(1 for p in inbox.glob("*.md") if p.is_file())


def run_prices() -> tuple[bool, str, float]:
    start = time.time()
    if not FETCH.exists():
        return False, f"fetch.py not found at {rel(FETCH)}", 0.0
    # fetch.py needs yfinance, which lives in the repo venv — not the system python
    # that typically runs boot.py (7/21 fix: price pull failed with ModuleNotFoundError).
    venv_python = WORKSPACE / ".venv" / "bin" / "python3"
    interpreter = str(venv_python) if venv_python.exists() else sys.executable
    cmd = [interpreter, str(FETCH), "price"] + PRICE_TICKERS
    try:
        res = subprocess.run(cmd, cwd=str(WORKSPACE), capture_output=True, text=True, timeout=30)
        out = res.stdout.strip()
        if res.stderr.strip():
            out += "\nSTDERR: " + res.stderr.strip()[:500]
        return res.returncode == 0, out or "[no output]", time.time() - start
    except Exception as exc:
        return False, f"ERROR: {exc}", time.time() - start


def extract_bullets_under(text: str, heading: str, limit: int = 4) -> list[str]:
    # Find a heading line containing heading, then return nearby bullet/table-ish signal lines.
    lines = text.splitlines()
    start = None
    h = heading.lower()
    for i, line in enumerate(lines):
        if h in line.lower() and (line.lstrip().startswith("#") or line.lstrip().startswith("**")):
            start = i + 1
            break
    if start is None:
        return []
    out = []
    for line in lines[start:start + 80]:
        s = line.strip()
        if not s:
            continue
        if s.startswith("#") and out:
            break
        if s.startswith("-") or s.startswith("|") or s.startswith("**Status") or s.startswith("**Signal"):
            out.append(s)
        if len(out) >= limit:
            break
    return out


def cross_agent_summary(verbose: bool) -> list[str]:
    rows = []
    for name, paths, focus in CROSS_AGENT_BRIEFS:
        path = next((p for p in paths if p.exists()), None)
        if path is None:
            rows.append(f"❌ {name}: missing " + " or ".join(rel(p) for p in paths))
            continue
        age_h, age_s = file_age(path)
        text = read_text(path, 40000 if verbose else 16000)
        status = first_match(text, [r"\*\*Status:\*\*\s*([^\n]+)", r"\*\*Signal Status:\*\*\s*([^\n]+)"])
        if status:
            rows.append(f"• {name} ({age_s}): {status}")
        else:
            rows.append(f"• {name} ({age_s}): {rel(path)}")
        if verbose:
            for heading in focus[:2]:
                for bullet in extract_bullets_under(text, heading, 3):
                    rows.append(f"    {bullet[:180]}")
    return rows


def next_calendar(days: int = 90) -> list[str]:
    path = CORAL_DIR / "CALENDAR.md"
    if not path.exists():
        return ["❌ CALENDAR.md missing"]
    rows = []
    for line in read_text(path, 20000).splitlines():
        s = line.strip()
        if not s.startswith("|") or "---" in s or "Date" in s:
            continue
        # Calendar uses human dates/ranges, not ISO. Show unresolved forward rows.
        if "✅" in s or "DONE" in s:
            continue
        rows.append(s)
    return rows[:8] or ["No unresolved calendar rows found"]


def print_header(now: datetime) -> None:
    print("\n" + "#" * 72)
    print(f"#{'CORAL BOOT SEQUENCE':^70}#")
    print(f"#  {now.strftime('%A, %B %d, %Y  %H:%M'):^66}#")
    print("#" * 72)


def main() -> int:
    quick = "--quick" in sys.argv
    verbose = "--verbose" in sys.argv
    now = datetime.now()
    start = time.time()

    print_header(now)

    print("\n== CONTINUITY / STALENESS ==")
    for name, limit_h in STALE_LIMITS.items():
        path = CORAL_DIR / name
        age_h, age_s = file_age(path)
        if age_h is None:
            icon = "❌"
        elif age_h > limit_h:
            icon = "⚠️"
        else:
            icon = "✅"
        print(f"{icon} {name:<22} age={age_s:<7} limit={limit_h}h")

    status = read_text(CORAL_DIR / "STATUS.md", 6000)
    sig = first_match(status, [r"\*\*Signal Status:\*\*\s*([^\n]+)"])
    updated = first_match(status, [r"\*\*Last Updated:\*\*\s*([^\n]+)"])
    if updated or sig:
        print("\n== CORAL STATUS SNAPSHOT ==")
        if updated:
            print(f"Last Updated: {updated}")
        if sig:
            print(f"Signal Status: {sig}")

    print("\n== WALTER / MAIL ==")
    pending = pending_walter()
    print(f"Pending WALTER handoffs: {len(pending)}")
    for p in pending[:10]:
        first = first_match(read_text(p, 2500), [r"\*\*Signal:\*\*\s*([^\n]+)", r"^#\s*(.+)$"])
        print(f"  • {p.name}" + (f" — {first}" if first else ""))
    print(f"Legacy inbox .md files: {legacy_inbox_count()}")

    if quick:
        print("\n== MARKET PRICES ==\n⏩ skipped (--quick)")
    else:
        print("\n== MARKET PRICES — FL BANK / REGIONAL CONTEXT ==")
        ok, out, elapsed = run_prices()
        print(out)
        print(f"Price pull: {'OK' if ok else 'FAIL'} ({elapsed:.1f}s)")

    print("\n== CROSS-AGENT CONTEXT — READ, DON'T RE-OWN ==")
    for row in cross_agent_summary(verbose):
        print(row)

    print("\n== ACTIVE / NEXT CORAL CALENDAR GATES ==")
    for row in next_calendar(90):
        print(row)

    print("\n== BOOT NOTES ==")
    print("• Live-source pulls here are limited to CORAL/local bank market context.")
    print("• MARCO/REGINALD/CARL/NEXUS are read as context owners; reconcile before copying shared metrics.")
    print("• Script is read-only and does not replace full CLAUDE.md boot reads.")
    print("• Update STATUS/SCRATCH/NEXUS_BRIEF during closeout, not boot.")
    print(f"\nTotal boot time: {time.time() - start:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
