#!/usr/bin/env python3
"""WALTER doctor — read-only boot/on-demand health scan of the WALTER domain.

Mechanizes the manual audit that surfaced the 2026-06-16 drift (which only ran
because Will asked). Emits a punch-list of directory/infra drift so it's caught
continuously instead of periodically. Composes single-purpose checks; each
returns (severity, message) findings. HIGH/MED = attention needed; LOW/INFO =
surfaced for awareness.

  $ python3 tools/walter_doctor.py
  exit 0  = no HIGH/MED findings (LOW/INFO may still print)
  exit N  = N HIGH+MED findings — see the punch-list

Checks (v1):
  version_drift     spec header vs STATE.md §1            (reuses version_drift_check)
  board_reconcile   ToC == section headers == SIG rows == files on disk
  cron_liveness     3 boot-triage feeds (step 7c) vs cadence
  outbox_age        outbox/REQ-*.md older than 14d
  registry_staleness Tier-1 REGISTRY rows with Updated >14d
  liaison_enum      LIAISON files on disk (informational)

Informational, never a boot gate. Stdlib only. Add checks by appending to CHECKS.
"""
import csv
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WALTER = HERE.parent
REPO = WALTER.parents[1]
BOARD = REPO / "BOARD"
sys.path.insert(0, str(HERE))

HIGH, MED, LOW, INFO = "HIGH", "MED", "LOW", "INFO"
TODAY = dt.date.today()


def _age_days(d: dt.date) -> int:
    return (TODAY - d).days


def _git_last_commit_date(relpath: str) -> dt.date | None:
    """Date of the last commit touching relpath (relative to repo root).
    Shallow-clone-safe: the tip commit touching a path is always present.
    Returns None if the path has no commits / git unavailable."""
    try:
        r = subprocess.run(
            ["git", "-C", str(REPO), "log", "-1", "--format=%cd",
             "--date=short", "--", relpath],
            capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return None
    out = r.stdout.strip()
    try:
        return dt.date.fromisoformat(out) if out else None
    except ValueError:
        return None


def _registry_rows():
    """Yield (agent, tier, updated_date|None) from REGISTRY.tsv. Shared by the
    registry checks. Skips WALTER (self) and unparseable rows."""
    with (WALTER / "REGISTRY.tsv").open(errors="replace") as f:
        rdr = csv.reader(f, delimiter="\t")
        header = next(rdr, [])
        try:
            i_up, i_tier, i_agent = (header.index("Updated"),
                                     header.index("Tier"), header.index("Agent"))
        except ValueError:
            return
        for row in rdr:
            if len(row) <= max(i_up, i_tier, i_agent):
                continue
            agent = row[i_agent].strip()
            if agent == "WALTER":
                continue
            m = re.search(r"\d{4}-\d{2}-\d{2}", row[i_up])
            updated = dt.date.fromisoformat(m.group(0)) if m else None
            yield agent, row[i_tier].strip(), updated


# ── version drift (reuse the dedicated module) ──────────────────────────────
def check_version_drift():
    from version_drift_check import SPECS, spec_version, state_versions
    out = []
    state = state_versions()
    for rel in SPECS:
        sv = spec_version(WALTER / rel)
        stv = state.get(rel)
        if sv is None:
            out.append((HIGH, f"{rel}: no version token in header"))
        elif stv is None:
            out.append((HIGH, f"{rel}: missing from STATE.md §1"))
        elif sv != stv:
            out.append((HIGH, f"{rel}: STATE §1 says v{stv}, spec header is v{sv}"))
    if not out:
        out.append((INFO, "all core specs match STATE.md §1"))
    return out


# ── BOARD reconciliation ────────────────────────────────────────────────────
def check_board_reconcile():
    out = []
    idx = (BOARD / "INDEX.md").read_text(errors="replace")
    files = len(list(BOARD.glob("SIG-W-*.md")))

    # ToC overview: | [NAME](#..) | N |
    toc = {m.group(1): int(m.group(2))
           for m in re.finditer(r"^\|\s*\[([A-Z_]+)\]\(#[^)]+\)\s*\|\s*(\d+)\s*\|",
                                idx, re.M)}
    toc_total = sum(toc.values())
    declared_total = None
    mt = re.search(r"^\|\s*\*\*TOTAL\*\*\s*\|\s*\*\*(\d+)\*\*", idx, re.M)
    if mt:
        declared_total = int(mt.group(1))

    # section headers: ## NAME (N)  +  actual leading-cell SIG rows per section
    sec_declared, sec_actual = {}, {}
    cur = None
    for line in idx.splitlines():
        h = re.match(r"^##\s+([A-Z_]+)\s*\((\d+)\)", line)
        if h:
            cur = h.group(1)
            sec_declared[cur] = int(h.group(2))
            sec_actual[cur] = 0
            continue
        if cur and re.match(r"^\|\s*\[?SIG-W-\d{8}-\d{3}", line):
            sec_actual[cur] += 1
    actual_total = sum(sec_actual.values())

    # (a) the load-bearing aggregate reconciliation
    nums = {"ToC sum": toc_total, "section rows (actual)": actual_total,
            "SIG files on disk": files}
    if mt:
        nums["TOTAL row"] = declared_total
    if len(set(nums.values())) == 1:
        out.append((INFO, f"BOARD reconciles: {files} signals "
                          f"(ToC = sections = files = TOTAL)"))
    else:
        out.append((HIGH, "BOARD does NOT reconcile: "
                          + " / ".join(f"{k}={v}" for k, v in nums.items())))

    # (b) per-cluster: ToC count vs section-header count vs section actual rows
    for name in sorted(set(toc) | set(sec_declared)):
        t, sd, sa = toc.get(name), sec_declared.get(name), sec_actual.get(name)
        if t is None:
            out.append((MED, f"{name}: in a section header but missing from ToC"))
        elif sd is None:
            out.append((MED, f"{name}: in ToC but no '## {name} (N)' section"))
        elif not (t == sd == sa):
            out.append((MED, f"{name}: ToC={t} / header={sd} / actual rows={sa}"))
    return out


# ── cron-feed liveness (boot step 7c) ───────────────────────────────────────
def check_cron_liveness():
    feeds = [  # (path, cadence label, stale-after days)
        ("FORGE/tools/news-sweep/latest.md", "M-F daily", 3),
        ("FORGE/tools/filing-watch/latest.md", "~daily", 3),
        ("SIGNALS/inbound.md", "2×/day", 2),
    ]
    out = []
    for rel, cadence, limit in feeds:
        p = REPO / rel
        if not p.exists():
            out.append((MED, f"{rel}: MISSING"))
            continue
        age = _age_days(dt.date.fromtimestamp(p.stat().st_mtime))
        if age > limit:
            out.append((MED, f"{rel}: {age}d stale (cadence {cadence}, limit {limit}d) "
                            f"— upstream cron likely down"))
        else:
            out.append((INFO, f"{rel}: {age}d (ok)"))
    return out


# ── outbox queue age (boot step 9) ──────────────────────────────────────────
def check_outbox_age():
    reqs = sorted((WALTER / "outbox").glob("REQ-*.md"))
    if not reqs:
        return [(INFO, "outbox empty")]
    out = []
    for p in reqs:
        age = _age_days(dt.date.fromtimestamp(p.stat().st_mtime))
        sev = MED if age > 14 else INFO
        out.append((sev, f"{p.name}: {age}d old"
                        + (" — retry/escalate (>14d)" if age > 14 else "")))
    return out


# ── REGISTRY staleness (mechanizes the manual stale-agents list) ────────────
def check_registry_staleness():
    rows = list(_registry_rows())
    if not rows:
        return [(LOW, "REGISTRY.tsv header columns not as expected — skipped")]
    stale = [(a, _age_days(up)) for a, tier, up in rows
             if tier == "1" and up and _age_days(up) > 14]
    if stale:
        lst = ", ".join(f"{a} ({d}d)" for a, d in sorted(stale, key=lambda x: -x[1]))
        return [(LOW, f"Tier-1 registry-date >14d ({len(stale)}): {lst} "
                     f"— see registry_lag to tell dormant from lagging")]
    return [(INFO, "all Tier-1 REGISTRY rows ≤14d")]


# ── REGISTRY lag: row date vs the agent's actual last STATUS commit ─────────
def check_registry_lag():
    """The board-lags-agents check (auto-memory finding_board_lags_agents...).
    Compares each agent's REGISTRY `Updated` date against the git commit date of
    its STATUS.md (fallback: agent dir). Registry OLDER than the agent's real
    work = a lagging row → refresh it AND don't direct that (active) agent to
    consume the board. Also separates genuinely-dormant agents (both dates old)
    from lagging ones — the distinction the manual 6/16 audit drew by hand."""
    active_lag, stale_quiet, dormant, uncheckable = [], [], [], []
    for agent, tier, updated in _registry_rows():
        if updated is None:
            continue
        commit = _git_last_commit_date(f"AGENTS/{agent}/STATUS.md") \
            or _git_last_commit_date(f"AGENTS/{agent}/")
        if commit is None:
            uncheckable.append(agent)
            continue
        lag = (commit - updated).days  # >0 = registry behind the agent's last work
        recent = _age_days(commit) <= 14  # agent's own last activity is fresh
        if lag >= 1 and recent:
            active_lag.append((agent, updated, commit, lag))   # ahead of board NOW
        elif lag >= 3:
            stale_quiet.append((agent, updated, commit, lag))  # row behind, agent quiet
        elif _age_days(updated) > 14 and _age_days(commit) > 14:
            dormant.append((agent, _age_days(commit)))

    out = []
    # active + lagging is the load-bearing case (board-lags-agents): MED if ≥3d
    for agent, up, com, lag in sorted(active_lag, key=lambda x: -x[3]):
        sev = MED if lag >= 3 else LOW
        tail = " → refresh row + DON'T direct to board (agent has fresher view)" \
            if sev == MED else " → refresh row"
        out.append((sev, f"{agent}: registry {up.isoformat()} < last commit "
                        f"{com.isoformat()} ({_age_days(com)}d ago, +{lag}d){tail}"))
    # registry behind but the agent itself has gone quiet → just a stale row
    for agent, up, com, lag in sorted(stale_quiet, key=lambda x: -x[3]):
        out.append((LOW, f"{agent}: registry {up.isoformat()} stale (+{lag}d) but agent "
                        f"quiet since {com.isoformat()} ({_age_days(com)}d) → refresh row, low urgency"))
    if dormant:
        lst = ", ".join(f"{a} ({d}d)" for a, d in sorted(dormant, key=lambda x: -x[1]))
        out.append((INFO, f"dormant — registry accurate, not lagging ({len(dormant)}): {lst}"))
    if uncheckable:
        out.append((INFO, f"no committed STATUS, lag uncheckable: {', '.join(sorted(uncheckable))}"))
    if not (active_lag or stale_quiet):
        out.append((INFO, "no registry rows lagging the agents' actual STATUS commits"))
    return out


# ── LIAISON files on disk (boot step 9 glob, informational) ─────────────────
def check_liaison_enum():
    files = sorted((REPO / "AGENTS").glob("*/handoff_WALTER/**/LIAISON.md"))
    if not files:
        return [(INFO, "no LIAISON files found")]
    items = []
    for p in files:
        agent = p.relative_to(REPO / "AGENTS").parts[0]
        closed = "/CLOSED/" in str(p)
        age = _age_days(dt.date.fromtimestamp(p.stat().st_mtime))
        items.append(f"{agent}{'(CLOSED)' if closed else ''} {age}d")
    return [(INFO, f"LIAISON files ({len(files)}): " + " · ".join(items))]


CHECKS = [
    ("version_drift", check_version_drift),
    ("board_reconcile", check_board_reconcile),
    ("cron_liveness", check_cron_liveness),
    ("outbox_age", check_outbox_age),
    ("registry_staleness", check_registry_staleness),
    ("registry_lag", check_registry_lag),
    ("liaison_enum", check_liaison_enum),
]

MARK = {HIGH: "✗", MED: "⚠", LOW: "·", INFO: "✓"}


def main() -> int:
    print(f"WALTER doctor — {TODAY.isoformat()}")
    print("=" * 72)
    attn = 0
    for name, fn in CHECKS:
        try:
            findings = fn()
        except Exception as e:  # a broken check must not hide the others
            findings = [(MED, f"check raised {type(e).__name__}: {e}")]
        print(f"\n[{name}]")
        for sev, msg in findings:
            if sev in (HIGH, MED):
                attn += 1
            print(f"  {MARK[sev]} {sev:<4} {msg}")
    print("\n" + "=" * 72)
    if attn:
        print(f"✗ {attn} item(s) need attention (HIGH/MED). See punch-list above.")
    else:
        print("✓ no HIGH/MED findings — WALTER domain healthy.")
    return attn


if __name__ == "__main__":
    sys.exit(main())
