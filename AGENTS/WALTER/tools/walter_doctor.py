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

Checks:
  version_drift          spec header vs STATE.md §1            (reuses version_drift_check)
  claude_md_version_drift  CLAUDE.md spec-version citations vs spec headers (the boot doc nothing else watched)
  board_reconcile        ToC == section headers == SIG rows == files on disk
  log_reconcile          route_log / delivery_log SIG-ids ↔ BOARD files (orphans / missing)
  cron_liveness          3 boot-triage feeds (step 7c) vs cadence
  intake_liveness        RESEARCH-INTAKE lane liveness.json staleness/health (step 7e consumer backstop)
  cushing_capability     EIA .env / key present → Boundary-#3 (Cushing) auto-fire live (silent-death guard)
  outbox_age             all staged outbox files (REQ-* >14d retry; drafts surfaced)
  registry_staleness     Tier-1 REGISTRY rows with Updated >14d
  registry_lag           REGISTRY date vs agent's last STATUS commit (board-lags-agents)
  liaison_enum           LIAISON files on disk (informational)
  delivered_but_unconsumed  inbox/WALTER/ handoff delivered but not moved to processed/ (>N days)
  written_but_undelivered   inbox/WALTER/ handoff committed-local but not on origin (git-derived)
  deep_research_pending_overdue  DEEP_RESEARCH_FLAGGED_LOG row PENDING past its deadline (or stale open >30d)
  staleness_sweep_overdue  last STALENESS_SWEEP_*.tsv vs 14d cadence (lifecycle-tagging lapse guard)

The two delivery checks mechanize BOARD_CONSUMPTION_SPEC v0.2 §6 (the anti-rot
safeguard for the WALTER Routing v2 delivery layer). Sync/origin state is derived
READ-ONLY from git — PROME never writes a flag (requirement B of the v2 packet).

Informational, never a boot gate. Stdlib only. Add checks by appending to CHECKS.
"""
import csv
import datetime as dt
import json
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

# Single-machine (desktop CC) since 2026-06-26 — OpenClaw/VPS cut. Every agent
# runs as a Claude Code session on the one shared repo, so a delivered handoff =
# committed AND on origin for ALL recipients (no platform split). The former
# _cc_agents()/REGISTRY-Platform-column derivation + OPENCLAW branches are gone.
# Source: BOARD_CONSUMPTION_SPEC v0.6 §3.3 (design/OPENCLAW_CUTOVER_PLAN.md).


# delivered handoff older than this (days) without being consumed → flag
N_UNCONSUMED_DAYS = 2


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


_UPDATED_RE = re.compile(r"(?i)\b(?:last\s+)?updated\b[\s:*]*?(\d{4}-\d{2}-\d{2})")


def _status_header_date(agent: str) -> "dt.date | None":
    """The agent's OWN self-declared last-update date — the first date directly
    after an 'Updated:' / 'Last Updated:' marker in the first ~25 STATUS.md lines.
    Distinguishes a real self-update from an incidental cross-agent commit that
    merely touched the file (the registry_lag false-positive class, e.g. the 6/19
    REGINALD CORAL-promotion ref-sweep). Returns None if no canonical marker is
    found — caller then falls back to commit-date logic (no regression)."""
    p = REPO / "AGENTS" / agent / "STATUS.md"
    try:
        head = p.read_text(errors="replace").splitlines()[:25]
    except OSError:
        return None
    for line in head:
        m = _UPDATED_RE.search(line)
        if m:
            try:
                return dt.date.fromisoformat(m.group(1))
            except ValueError:
                continue
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
    # These 3 cron feeds are KNOWN-DARK — superseded by the RESEARCH-INTAKE lane
    # (boot step 7e; see CLAUDE.md step 7c). They are NOT live inputs, so staleness
    # is EXPECTED, not a failure → emit INFO, not MED (removes the false-MED that
    # fired every boot; fix per the 2026-07-03 arch/infra audit). A feed going
    # FRESH again surfaces as "(ok) — REVIVED?" = the signal to re-integrate it.
    feeds = [  # (path, cadence label, stale-after days)
        ("FORGE/tools/news-sweep/latest.md", "M-F daily", 3),
        ("FORGE/tools/filing-watch/latest.md", "~daily", 3),
        ("SIGNALS/inbound.md", "2×/day", 2),
    ]
    out = []
    for rel, cadence, limit in feeds:
        p = REPO / rel
        if not p.exists():
            out.append((INFO, f"{rel}: absent (known-dark; superseded by RESEARCH-INTAKE lane, 7e)"))
            continue
        age = _age_days(dt.date.fromtimestamp(p.stat().st_mtime))
        if age > limit:
            out.append((INFO, f"{rel}: {age}d stale — known-dark, superseded by RESEARCH-INTAKE lane (7e); not a live input"))
        else:
            out.append((INFO, f"{rel}: {age}d (ok) — REVIVED? re-integrate as a live input if intended"))
    return out


# ── RESEARCH-INTAKE lane liveness (boot step 7e) ────────────────────────────
def check_intake_liveness():
    """Health self-alarm for the RESEARCH-INTAKE collection lane (WALTER's consumer
    per PROME 2026-06-29). Reads the on-disk liveness.json (boot step 7e re-pulls
    the lane fresh + runs intake_scan for the significance gate — this check is the
    boot-time backstop that alarms if the collector died). Staleness >2 calendar
    days (weekday-daily cadence, spans a weekend) = collector likely down → flag PROME."""
    lane = Path("/home/willi/Research-Intake")
    lv = lane / "liveness.json"
    seen = WALTER / "registry" / "intake_seen.json"
    out = []
    if not lv.exists():
        out.append((MED, f"lane not found ({lv}) — RESEARCH-INTAKE not cloned/reachable; "
                        f"consumer wiring (boot 7e) can't run"))
        return out
    try:
        live = json.loads(lv.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        out.append((MED, f"liveness.json unreadable: {type(e).__name__}: {e}"))
        return out
    lr = live.get("last_run_utc", "")
    try:
        age = (dt.datetime.now(dt.timezone.utc)
               - dt.datetime.fromisoformat(lr.replace("Z", "+00:00"))).days
    except (ValueError, AttributeError):
        age = None
    if age is None:
        out.append((MED, "last_run_utc missing/unparseable"))
    elif age > 2:
        out.append((MED, f"lane STALE {age}d (last_run {lr}) — collector likely down; flag PROME "
                        f"(exception-only; boot 7e re-pulls, this is the on-disk backstop)"))
    if live.get("status") not in ("ok", None):
        out.append((MED, f"lane status={live.get('status')}"))
    degraded = [f for f, j in live.get("jobs", {}).items() if j.get("status") not in ("ok", None)]
    if degraded:
        out.append((MED, f"feed(s) degraded: {', '.join(degraded)}"))
    if not seen.exists():
        out.append((LOW, "intake_seen.json missing — onset-dedup baseline not seeded "
                        "(run tools/intake_scan.py --mark; first boot would push all still-true conditions)"))
    if not out:
        nfeeds = len(live.get("jobs", {}))
        out.append((INFO, f"lane live (last_run {lr}, {age}d, {nfeeds} feeds ok); "
                        f"gate via boot-7e intake_scan.py"))
    return out


# ── outbox queue age (boot step 9) ──────────────────────────────────────────
def check_outbox_age():
    """ALL staged outbox files, not just REQ-*.md — the REQ-only glob made staged
    drafts (e.g. DEWEY prompts) invisible and mis-reported the outbox as "empty"
    while items sat there. REQ-* keep the >14d retry/escalate semantics; other
    staged drafts surface informationally (LOW only if very stale)."""
    files = sorted(p for p in (WALTER / "outbox").glob("*")
                   if p.is_file() and p.name != ".gitkeep" and not p.name.startswith("."))
    if not files:
        return [(INFO, "outbox empty")]
    out = []
    for p in files:
        age = _age_days(dt.date.fromtimestamp(p.stat().st_mtime))
        if p.name.startswith("REQ-"):
            sev = MED if age > 14 else INFO
            out.append((sev, f"{p.name}: {age}d old (REQ)"
                            + (" — retry/escalate (>14d)" if age > 14 else "")))
        else:
            sev = LOW if age > 30 else INFO
            out.append((sev, f"{p.name}: {age}d old (staged draft)"
                            + (" — >30d unspawned, review/clear?" if age > 30 else "")))
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
    active_lag, stale_quiet, dormant, dir_only, uncheckable, incidental = \
        [], [], [], [], [], []
    for agent, tier, updated in _registry_rows():
        if updated is None:
            continue
        status_exists = (REPO / "AGENTS" / agent / "STATUS.md").exists()
        commit = _git_last_commit_date(f"AGENTS/{agent}/STATUS.md") if status_exists else None
        if commit is None:
            # No (current) STATUS.md → a dir-level commit is an unreliable proxy:
            # it catches cross-agent / bulk commits that merely touched the dir
            # (e.g. DARWIN's "4/30" was a HANS/MARCO-STATUS + memory-log commit).
            # Surface as INFO, never let it drive a MED/LOW lag flag.
            dcommit = _git_last_commit_date(f"AGENTS/{agent}/")
            if dcommit is None:
                uncheckable.append(agent)
            elif (dcommit - updated).days >= 3:
                dir_only.append((agent, updated, dcommit, (dcommit - updated).days))
            continue
        lag = (commit - updated).days  # >0 = registry behind the agent's last work
        header = _status_header_date(agent)
        # False-positive guard: a commit can touch STATUS.md without the agent
        # self-updating (cross-agent ref-sweep / bulk commit). If the agent's OWN
        # declared header date hasn't advanced past the registry, that commit is
        # incidental — NOT a real lag (the 6/19 REGINALD CORAL-promotion case).
        if lag >= 1 and header is not None and header <= updated:
            incidental.append((agent, updated, commit, header))
            continue
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
    if dir_only:
        lst = ", ".join(f"{a} (dir +{lag}d vs {up.isoformat()})"
                        for a, up, com, lag in sorted(dir_only, key=lambda x: -x[3]))
        out.append((INFO, f"no STATUS.md — dir-fallback unreliable (may be cross-agent "
                          f"commits), NOT flagged: {lst}"))
    if incidental:
        lst = ", ".join(f"{a} (commit {com.isoformat()} but STATUS hdr {hd.isoformat()} ≤ reg {up.isoformat()})"
                        for a, up, com, hd in sorted(incidental))
        out.append((INFO, f"incidental STATUS touch, not a real lag ({len(incidental)}): {lst}"))
    if uncheckable:
        out.append((INFO, f"no committed activity, lag uncheckable: {', '.join(sorted(uncheckable))}"))
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


# ── delivery layer: handoff discovery + git-derived sync state ──────────────
def _handoff_files():
    """Non-processed WALTER delivery handoffs: (path, recipient, relpath).
    Globs AGENTS/*/inbox/WALTER/*.md, excluding anything under processed/.
    Single-machine: every recipient is CC → delivered = committed AND on origin."""
    out = []
    for p in (REPO / "AGENTS").glob("*/inbox/WALTER/*.md"):
        if "/processed/" in p.as_posix():
            continue
        recipient = p.relative_to(REPO / "AGENTS").parts[0]
        out.append((p, recipient, str(p.relative_to(REPO))))
    return out


def _origin_ref():
    """First existing origin head ref, or None (fresh/shallow clone)."""
    for ref in ("origin/master", "origin/main"):
        try:
            r = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--verify",
                                "--quiet", ref], capture_output=True, text=True, timeout=10)
        except (OSError, subprocess.SubprocessError):
            return None
        if r.returncode == 0 and r.stdout.strip():
            return ref
    return None


def _sync_state(relpath: str, origin_ref) -> str:
    """READ-ONLY git derivation of a handoff's delivery/sync state (requirement B).
    Returns: 'uncommitted' / 'ahead' (committed, not on origin) / 'on_origin' /
    'no_origin' (origin ref missing) / 'unknown' (git error)."""
    try:
        st = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain", "--",
                             relpath], capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return "unknown"
    if st.stdout.strip():
        return "uncommitted"           # untracked or modified
    if origin_ref is None:
        return "no_origin"
    try:  # committed — any commit touching it reachable from HEAD but not origin?
        rl = subprocess.run(["git", "-C", str(REPO), "rev-list", "--count", "HEAD",
                             "--not", "--remotes=origin", "--", relpath],
                            capture_output=True, text=True, timeout=10)
        return "ahead" if int(rl.stdout.strip() or "0") > 0 else "on_origin"
    except (OSError, subprocess.SubprocessError, ValueError):
        return "unknown"


# ── delivered-but-unconsumed (BOARD_CONSUMPTION_SPEC v0.2 §6.1) ─────────────
def _delivery_roles():
    """{(signal_id, RECIPIENT_UPPER): ROLE_UPPER} from delivery_log.tsv — lets the
    unconsumed check split ACTION (the real risk) from the INFO cc-pile (low-stakes
    per the 2026-06-23 delivery-telemetry calibration finding)."""
    out = {}
    log = WALTER / "routed" / "delivery_log.tsv"
    try:
        rows = log.read_text(encoding="utf-8").splitlines()
    except OSError:
        return out
    for ln in rows[1:]:
        c = ln.split("\t")
        if len(c) >= 4:
            out[(c[1].strip(), c[2].strip().upper())] = c[3].strip().upper()
    return out


# Recipients whose OWN boot scan is a COMPLETE whole-INDEX /BOARD/ diff (dispositions
# every unrecorded SIG-W across all of INDEX) → complete pull; WALTER SKIPS inbox
# delivery to them (BOARD_CONSUMPTION_SPEC §3.5, v0.7, verified 2026-07-04). Any handoff
# in their inbox is a to-ARCHIVE residue, NOT a consume-gap. Verify "complete" (not
# tiered/selective) empirically before adding an agent. REGINALD/SAM are NOT complete.
PULL_COMPLETE = {"CARL", "RED"}


def check_delivered_but_unconsumed():
    """A delivered handoff (on origin) sitting >N days without being moved to
    processed/ → the recipient's Phase-2 consume boot-step may not be installed.
    The visible Phase-2-gap telemetry."""
    files = _handoff_files()
    if not files:
        return [(INFO, "no WALTER handoffs in flight")]
    origin = _origin_ref()
    aged, pull_complete = [], []
    for p, recipient, relpath in files:
        if _sync_state(relpath, origin) != "on_origin":
            continue  # not delivered yet → written_but_undelivered owns it
        age = _age_days(dt.date.fromtimestamp(p.stat().st_mtime))
        if age > N_UNCONSUMED_DAYS:
            sig = p.name[:-3] if p.name.endswith(".md") else p.name
            (pull_complete if recipient.upper() in PULL_COMPLETE else aged).append(
                (recipient, sig, age))
    # Pull-complete recipients (WALTER skips delivery, §3.5) — residual handoffs are a
    # one-time to-ARCHIVE cleanup by PROME, NOT a consume-gap (+ a re-delivery tripwire).
    pc = []
    if pull_complete:
        cnt = {}
        for r, _s, _a in pull_complete:
            cnt[r] = cnt.get(r, 0) + 1
        pc = [(LOW, "pull-complete agents (WALTER skips delivery per §3.5) have handoffs to "
               "ARCHIVE not consume: " + ", ".join(f"{r} {n}" for r, n in sorted(cnt.items()))
               + " — bulk-`git mv` to processed/ (one-time; if NEW, WALTER mis-delivered)")]
    if not aged:
        return pc + [(INFO, f"all delivered handoffs consumed or ≤{N_UNCONSUMED_DAYS}d old "
                      f"({len(files)} in flight)")]
    # Collapse to a role-split summary (ACTION = the real risk; INFO cc-pile =
    # low-stakes per the 2026-06-23 delivery-telemetry calibration) — one line,
    # not one per item, so genuine boot findings aren't buried under the cc-pile.
    roles = _delivery_roles()
    by_rcpt, action_total = {}, 0
    for recipient, sig, age in aged:
        role = roles.get((sig, recipient.upper()), "?")
        a, i, mx = by_rcpt.get(recipient, (0, 0, 0))
        if role == "ACTION":
            a += 1
            action_total += 1
        else:
            i += 1
        by_rcpt[recipient] = (a, i, max(mx, age))
    oldest = max(x[2] for x in aged)
    parts = [f"{r} {by_rcpt[r][0] + by_rcpt[r][1]}"
             + (f"({by_rcpt[r][0]}A/{by_rcpt[r][1]}I)" if by_rcpt[r][0] else "")
             for r in sorted(by_rcpt, key=lambda r: -(by_rcpt[r][0] * 100 + by_rcpt[r][1]))]
    info_total = len(aged) - action_total
    summary = (f"{len(aged)} delivered-but-unconsumed across {len(by_rcpt)} agents, "
               f"oldest {oldest}d — {action_total} ACTION / {info_total} INFO: "
               f"{'; '.join(parts)}")
    if action_total:
        return pc + [(MED, summary + " — ACTION items are the risk; install recipient "
                      "consume boot-step (CC self-apply set) to clear")]
    return pc + [(LOW, summary + " — all-INFO cc-pile, low-stakes; clears when the "
                  "consume boot-step is installed")]


# ── written-but-undelivered (BOARD_CONSUMPTION_SPEC v0.2 §6.2, git-derived) ──
def check_written_but_undelivered():
    """Handoff committed locally but not reachable from origin = not delivered (the
    recipient's next pull can't see it). Single-machine: all recipients are CC."""
    files = _handoff_files()
    if not files:
        return [(INFO, "no WALTER handoffs awaiting delivery")]
    origin = _origin_ref()
    out = []
    for p, recipient, relpath in sorted(files, key=lambda x: x[1]):
        sync = _sync_state(relpath, origin)
        if sync == "on_origin":
            continue                                   # delivered (reachable on pull)
        if sync == "no_origin":
            out.append((INFO, f"{recipient}: {p.name} — origin ref unavailable, "
                              f"sync state underivable"))
        elif sync == "unknown":
            out.append((LOW, f"{recipient}: {p.name} — git sync state unknown"))
        elif sync == "ahead":
            out.append((MED, f"{recipient}: {p.name} committed but NOT on origin — "
                            f"recipient can't pull it (needs §3.4 scoped-push)"))
        else:  # uncommitted
            out.append((LOW, f"{recipient}: {p.name} written, uncommitted (mid-session)"))
    if not out:
        return [(INFO, "all WALTER handoffs delivered (on origin)")]
    return out


# ── deep-research candidate flag overdue (CHECKLIST Phase 2.8 / proposal §5i) ─
def check_deep_research_pending_overdue():
    """DEEP_RESEARCH_FLAGGED_LOG rows still PENDING past their deadline (or stale
    `open` >30d). Closes the loop the `deadline` column opens — a flagged-then-
    forgotten candidate can't pass its deadline silently until the next formal
    review. Reads the ledger TSV directly (no header-field dependency — the proof
    the deferred FORMAT_SPEC field isn't needed for v1). Surfaced in the boot reply
    (CLAUDE.md spawn-protocol step 0.5). Same family as delivered_but_unconsumed."""
    ledger = WALTER / "registry" / "DEEP_RESEARCH_FLAGGED_LOG.tsv"
    if not ledger.exists():
        return [(INFO, "no DEEP_RESEARCH_FLAGGED_LOG.tsv yet")]
    out, n_pending = [], 0
    with ledger.open(errors="replace") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if (row.get("disposition") or "").strip().upper() != "PENDING":
                continue
            n_pending += 1
            sig = (row.get("signal_id") or "?").strip()
            m = re.search(r"\d{4}-\d{2}-\d{2}", row.get("deadline") or "")
            if m:  # real date deadline → overdue if passed
                try:
                    dl = dt.date.fromisoformat(m.group(0))
                except ValueError:
                    continue
                if dl < TODAY:
                    out.append((MED, f"{sig}: deep-research flag PENDING past deadline "
                                    f"{dl.isoformat()} ({_age_days(dl)}d overdue) — run it or drop it"))
            else:  # no date (deadline=open/blank) → stale if flagged >30d ago
                fm = re.search(r"\d{4}-\d{2}-\d{2}", row.get("flagged_date") or "")
                if fm and _age_days(dt.date.fromisoformat(fm.group(0))) > 30:
                    out.append((MED, f"{sig}: deep-research flag PENDING (deadline=open) flagged "
                                    f"{_age_days(dt.date.fromisoformat(fm.group(0)))}d ago — disposition it"))
    if not out:
        return [(INFO, f"no overdue deep-research flags ({n_pending} PENDING)")]
    return out


# ── CLAUDE.md spec-version citations (the auto-loaded boot doc nothing else watched) ─
def check_claude_md_version_drift():
    """version_drift_check guards spec headers vs STATE.md §1, but nothing watched
    CLAUDE.md — the most-read doc — so its 'BOARD_CONSUMPTION_SPEC v0.2' KEY-DESIGN-
    FILES row sat 4 versions stale (caught only by the 2026-06-27 6-agent self-audit).
    Scoped to the ONE unambiguous current-version-claim location: a KEY DESIGN FILES
    table row whose first cell is `design/<SPEC>.md` and whose description cell LEADS
    with `vN.M`. Historical 'feature X landed in FORMAT_SPEC v0.8' provenance (the
    CANONICAL-SOURCE table — filename in one cell, version in another) is deliberately
    NOT matched, so the check stays low-noise (a noisy check gets ignored)."""
    from version_drift_check import SPECS, spec_version
    try:
        claude = (WALTER / "CLAUDE.md").read_text(errors="replace")
    except OSError:
        return [(LOW, "CLAUDE.md unreadable — skipped")]
    out = []
    for rel in SPECS:
        base = Path(rel).name
        hv = spec_version(WALTER / rel)
        if hv is None:
            continue
        # | `design/<base>` | **vN.M ...  — filename in cell-1, version leads cell-2
        m = re.search(rf"^\|\s*`?[^|]*{re.escape(base)}[^|]*`?\s*\|\s*\*{{0,2}}v(\d+\.\d+)",
                      claude, re.M)
        if m and m.group(1) != hv:
            out.append((MED, f"CLAUDE.md KEY DESIGN FILES row cites {base} at v{m.group(1)} "
                            f"but spec header is v{hv} — update the boot doc"))
    if not out:
        out.append((INFO, "CLAUDE.md KEY-DESIGN-FILES version claims match spec headers"))
    return out


# ── log↔BOARD reconciliation (route_log / delivery_log audit trails) ─────────
def check_log_reconcile():
    """board_reconcile checks INDEX↔files; this checks the AUDIT TRAILS that prove a
    signal actually routed/delivered. Orphan (logged, no BOARD file) or missing
    (BOARD file, never logged) = drift nothing else catches. delivery_log only covers
    post-2026-06-17 (Routing v2), so we check subset-containment, not raw counts."""
    board_ids = set()
    for p in BOARD.glob("SIG-W-*.md"):
        m = re.match(r"(SIG-W-\d{8}-\d{3})", p.name)
        if m:
            board_ids.add(m.group(1))

    def log_ids(relpath):
        p = WALTER / relpath
        if not p.exists():
            return None
        ids = set()
        for line in p.read_text(errors="replace").splitlines()[1:]:
            m = re.search(r"SIG-W-\d{8}-\d{3}", line)
            if m:
                ids.add(m.group(0))
        return ids

    out = []
    route = log_ids("routed/route_log.tsv")
    if route is not None:
        orphan = sorted(route - board_ids)
        missing = sorted(board_ids - route)
        if orphan:
            out.append((MED, f"route_log: {len(orphan)} SIG-id(s) with NO BOARD file "
                            f"({', '.join(orphan[:4])}{'…' if len(orphan) > 4 else ''})"))
        if missing:
            out.append((MED, f"{len(missing)} BOARD file(s) never in route_log "
                            f"({', '.join(missing[:4])}{'…' if len(missing) > 4 else ''})"))
        if not orphan and not missing:
            out.append((INFO, f"route_log reconciles with BOARD ({len(board_ids)} signals)"))
    deliv = log_ids("routed/delivery_log.tsv")
    if deliv is not None:
        d_orphan = sorted(deliv - board_ids)
        if d_orphan:
            out.append((MED, f"delivery_log: {len(d_orphan)} delivered SIG-id(s) with NO "
                            f"BOARD file ({', '.join(d_orphan[:4])})"))
        else:
            out.append((INFO, f"delivery_log: all {len(deliv)} delivered SIG-ids have a "
                            f"BOARD file (post-6/17 coverage)"))
    return out


# ── Cushing/Boundary-#3 capability (silent-death of a wired auto-fire) ───────
def check_cushing_capability():
    """Boot step-6c claims Cushing (ROUTING_TABLE Boundary #3, <20M → IMMEDIATE) is
    auto-scanned, but the EIA key lives in a gitignored machine-local .env that does
    not survive a box change — so the trigger goes silently dark (reads N/A). Cheap
    file probe (no 30s dashboard pull) so the silent-death becomes a loud boot flag."""
    env = REPO / "FORGE" / "tools" / "market-data" / ".env"
    if not env.exists():
        return [(MED, "Cushing/Boundary-#3 DARK: FORGE/tools/market-data/.env missing "
                     "(EIA key gone — step-6c Cushing scan reads N/A)")]
    try:
        if "EIA_API_KEY" not in env.read_text(errors="replace"):
            return [(MED, ".env present but no EIA_API_KEY → Cushing/Boundary-#3 scan dark")]
    except OSError:
        return [(LOW, ".env unreadable — Cushing capability unverifiable")]
    return [(INFO, "EIA key present (Cushing/Boundary-#3 scan live)")]


# ── staleness-sweep cadence (lifecycle tagging keeping pace with BOARD growth) ─
def check_staleness_sweep_overdue():
    """The SUPERSEDED/FALSIFIED/EVENT-PASSED sweep runs ad-hoc; nothing alarmed when
    it lapsed. Cadence codified here at 14d (was an open design decision). Backstop is
    the INDEX section-preamble blanket-discount, so MED not HIGH."""
    sweeps = sorted((WALTER / "registry").glob("STALENESS_SWEEP_*.tsv"))
    if not sweeps:
        return [(LOW, "no STALENESS_SWEEP records yet")]
    m = re.search(r"\d{4}-\d{2}-\d{2}", sweeps[-1].name)
    if not m:
        return [(INFO, "staleness sweep present (undated filename)")]
    age = _age_days(dt.date.fromisoformat(m.group(0)))
    if age > 14:
        return [(MED, f"staleness sweep {age}d overdue (last {m.group(0)}, cadence 14d) "
                     f"— stale-frame BOARD signals may sit untagged")]
    return [(INFO, f"staleness sweep {age}d ago (last {m.group(0)}, ≤14d)")]


# ── boot-protocol cross-ref integrity (lean-checklist ↔ rationale-doc split) ─────
def check_boot_protocol_xref():
    """The CLAUDE.md boot checklist points to per-step rationale in
    design/BOOT_PROTOCOL.md via [→ BP §x] tags. Two synced docs drift: a renumbered
    step or renamed §x silently orphans a pointer. Mechanize it (same philosophy as
    claude_md_version_drift) — every pointer must resolve to a real section, and every
    section should be pointed-to. Added 2026-06-28 (PROME review of the split)."""
    claude = WALTER / "CLAUDE.md"
    bp = WALTER / "design" / "BOOT_PROTOCOL.md"
    try:
        ctext = claude.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return [(LOW, "CLAUDE.md unreadable — boot-protocol xref unverifiable")]
    ptrs = set(re.findall(r"\[→ BP §(\S+?)[\]\s]", ctext))
    if not bp.exists():
        if not ptrs:
            return [(INFO, "no boot-protocol split in use (no [→ BP §x] pointers)")]
        return [(MED, f"{len(ptrs)} [→ BP §x] pointer(s) but design/BOOT_PROTOCOL.md is MISSING")]
    btext = bp.read_text(encoding="utf-8", errors="replace")
    secs = set()
    for h in re.findall(r"^## §(.+?)\s+—", btext, flags=re.M):
        for part in h.split("/"):  # combined headers like "§5 / §10" carry § on each part
            secs.add(part.strip().lstrip("§").strip())
    dangling = sorted(p for p in ptrs if p not in secs)
    orphan = sorted(s for s in secs if s not in ptrs)
    out = []
    if dangling:
        out.append((MED, f"boot-protocol xref: {len(dangling)} pointer(s) resolve to NO section: "
                         f"{', '.join('§' + d for d in dangling)} — fix the [→ BP §x] tag or the "
                         f"BOOT_PROTOCOL header"))
    if orphan:
        out.append((LOW, f"boot-protocol xref: {len(orphan)} section(s) with no inbound pointer: "
                         f"{', '.join('§' + o for o in orphan)} (orphaned rationale)"))
    if not out:
        out.append((INFO, f"boot-protocol xref clean ({len(ptrs)} pointers ↔ {len(secs)} sections)"))
    return out


def check_dropzone_pending():
    """Surface unprocessed items in the WILL desktop drop-zone (inbox/WILL/).
    Backstops boot step 7f — even if boot skips the scan, an unprocessed drop
    self-alarms here (the 7/6+7/8 'items sat invisible 2 days' failure class)."""
    dz = WALTER / "inbox" / "WILL"
    out = []
    if not dz.is_dir():
        out.append((LOW, "inbox/WILL/ drop-zone absent — scaffold not present"))
        return out
    skip = {"processed", ".gitignore", ".gitkeep", ".DS_Store", "README.md"}
    pending = sorted(
        p.name for p in dz.iterdir()
        if p.name not in skip and not p.name.startswith(".")
    )
    if pending:
        shown = ", ".join(pending[:8]) + (" …" if len(pending) > 8 else "")
        out.append((MED, f"{len(pending)} item(s) waiting in inbox/WILL/ drop-zone — "
                         f"process per CHECKLIST (image-batch/OCR fan-out), never auto-dispatch: {shown}"))
    else:
        out.append((INFO, "inbox/WILL/ drop-zone empty"))
    return out


def check_status_spine_overflow():
    """STATUS.md keeps only the ~5 most recent dated leads; older ones roll to
    SESSION_LOG.md at closeout (protocol §12). Nothing mechanized the cap, so the
    spine silently grew to 12 leads / 100KB by 2026-07-11 (a string of Tier-1
    closeouts each deferred the trim). Count the leads so the bloat self-alarms
    instead of rotting — LOW a few over (legit between Tier-2 trims), MED once
    clearly bloated. Added 2026-07-11 (Will-directed boot/closeout sweep)."""
    status = WALTER / "STATUS.md"
    try:
        text = status.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return [(LOW, "STATUS.md unreadable — spine count unverifiable")]
    n = len(re.findall(r"^(?:> )?\*\*Updated:\*\*", text, flags=re.M))
    CAP = 5
    if n > CAP + 3:
        return [(MED, f"STATUS.md has {n} dated leads (cap ~{CAP}) — roll the oldest "
                     f"{n - CAP} to SESSION_LOG.md at closeout (protocol §12 spine-bloat guard)")]
    if n > CAP:
        return [(LOW, f"STATUS.md has {n} dated leads (soft cap {CAP}) — trim the oldest "
                     f"{n - CAP} at the next full closeout")]
    return [(INFO, f"STATUS.md spine at {n} lead(s) (≤{CAP})")]


def _read(p: Path) -> str | None:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def _agents_in(span: str) -> set[str]:
    """Extract agent-name tokens from a prose span. Agent names are UPPER_SNAKE, >=3
    chars; drop the connective words that share that shape."""
    return {t for t in re.findall(r"\b[A-Z][A-Z_]{2,}\b", span)
            if t not in {"NOT", "AND", "SKIPPED", "BOARD", "ACTION", "INFO", "WALTER"}}


def check_restated_set_drift():
    """version_drift + claude_md_version_drift compare a canonical source to a
    restatement — but both only watch VERSION NUMBERS. A doc that restates a SET or a
    COUNT in prose drifts invisibly to them. Two live instances found 2026-07-16 in one
    session: (a) CLAUDE.md RULE 10 — the rule read at dispatch time — still advertised
    the §3.5 exemption as '(v0.7) currently CARL' when it had been CARL + RED since v0.8
    (7/09, 7 days stale); (b) CLAUDE.md boot step 11 said a signal's cluster 'MUST be 1
    of the 11' when CLIMATE_MACRO made it 12 on 6/28 (18 days stale, in the step run on
    every dispatch). Same class as the two version checks, one datum-type over.

    SCOPED TO TWO SEEDS ON PURPOSE (Will-approved 2026-07-16). This is NOT a generic
    'scan prose for stale claims' — that isn't buildable and would be overselling. It
    checks only registered (canonical -> restatement-site) pairs, so a NEW restatement
    somewhere else is invisible until added here. Adding a seed = add a SEEDS entry.

    HISTORY IS THE TRAP, not detection: changelogs legitimately say 'as of v0.26 —
    CARL + RED' and STATE legitimately says 'pairs BOARD_CONSUMPTION_SPEC v0.8'. Those
    are correct RECORDS of a past state and must not be flagged. Every regex below is
    therefore anchored to a distinctive CURRENT-claim phrasing rather than to a bare
    name/number, and changelog spans are excluded. Same lesson as boot_protocol_xref,
    where a doc's own example pointer read as a real dangling reference."""
    out = []

    # ── Seed 1: the §3.5 pull-complete exemption set ────────────────────────────
    # Canonical = this module's own PULL_COMPLETE constant (what the code actually does).
    truth = set(PULL_COMPLETE)
    sites = [
        (WALTER / "CLAUDE.md", "RULE 10",
         r"pull-complete recipients \(currently ([^)]*)\)"),
        (WALTER / "design/SIGNAL_PROCESSING_CHECKLIST.md", "Phase 3.5 exemption note",
         r"§3\.5 exemption list \(\*\*([^*]+)\*\*"),
    ]
    for path, label, pat in sites:
        text = _read(path)
        if text is None:
            out.append((LOW, f"{path.name} unreadable — {label} exemption claim unverifiable"))
            continue
        m = re.search(pat, text)
        if not m:
            out.append((LOW, f"{path.name} {label}: no pull-complete claim matched — "
                             f"phrasing changed? re-anchor the regex or drop the seed"))
            continue
        claimed = _agents_in(m.group(1))
        if claimed != truth:
            out.append((MED, f"{path.name} {label} claims pull-complete = "
                             f"{{{', '.join(sorted(claimed))}}} but PULL_COMPLETE is "
                             f"{{{', '.join(sorted(truth))}}} — stale restatement"))

    # Canonical prose home: the spec's own "Current exemption list" bullets. Span-scoped
    # so the adjacent "NOT exempt — REGINALD/SAM" bullet can't be miscounted as members.
    spec = _read(WALTER / "design/BOARD_CONSUMPTION_SPEC.md")
    if spec is not None:
        m = re.search(r"\*\*Current exemption list:\*\*(.*?)\*\*Doctor:\*\*", spec, re.S)
        if m:
            listed = set()
            for line in m.group(1).splitlines():
                if line.lstrip().startswith("- **") and "NOT exempt" not in line:
                    b = re.match(r"\s*- \*\*([A-Z][A-Z_]{2,})\*\*", line)
                    if b:
                        listed.add(b.group(1))
            if listed and listed != truth:
                out.append((MED, f"BOARD_CONSUMPTION_SPEC §3.5 'Current exemption list' = "
                                 f"{{{', '.join(sorted(listed))}}} but PULL_COMPLETE is "
                                 f"{{{', '.join(sorted(truth))}}} — spec and code disagree"))

    # ── Seed 2: the cluster set ─────────────────────────────────────────────────
    # Canonical = CLUSTER_TAXONOMY's numbered table (`| N | **NAME** | ...`).
    tax = _read(WALTER / "design/CLUSTER_TAXONOMY.md")
    if tax is None:
        out.append((LOW, "CLUSTER_TAXONOMY.md unreadable — cluster-set claims unverifiable"))
    else:
        clusters = set(re.findall(r"^\|\s*\d+\s*\|\s*\*\*([A-Z][A-Z_]+)\*\*", tax, re.M))
        if not clusters:
            out.append((LOW, "CLUSTER_TAXONOMY.md: canonical numbered table didn't parse — "
                             "structure changed? re-anchor before trusting this seed"))
        else:
            n = len(clusters)
            # (a) the taxonomy's own heading restates the count
            m = re.search(r"^## The (\d+) clusters", tax, re.M)
            if m and int(m.group(1)) != n:
                out.append((MED, f"CLUSTER_TAXONOMY heading says '{m.group(1)} clusters' but its "
                                 f"own canonical table lists {n} — self-inconsistent"))
            # (b) CLAUDE.md dispatch step 11 restates the count
            claude = _read(WALTER / "CLAUDE.md")
            if claude:
                m = re.search(r"MUST be 1 of the (\d+) in `CLUSTER_TAXONOMY\.md`", claude)
                if not m:
                    out.append((LOW, "CLAUDE.md step 11: cluster-count claim didn't match — "
                                     "phrasing changed? re-anchor the regex"))
                elif int(m.group(1)) != n:
                    out.append((MED, f"CLAUDE.md step 11 (run on EVERY dispatch) says a cluster "
                                     f"MUST be 1 of {m.group(1)} — canonical taxonomy has {n}"))
            # (c) BOARD INDEX sections must be exactly the taxonomy set
            idx = _read(BOARD / "INDEX.md")
            if idx:
                sections = set(re.findall(r"^## ([A-Z][A-Z_]+) \(\d+\)$", idx, re.M))
                if sections and sections != clusters:
                    extra, missing = sections - clusters, clusters - sections
                    bits = []
                    if extra:
                        bits.append(f"INDEX has un-taxonomied {{{', '.join(sorted(extra))}}}")
                    if missing:
                        bits.append(f"taxonomy has un-sectioned {{{', '.join(sorted(missing))}}}")
                    out.append((MED, "BOARD INDEX cluster sections ≠ CLUSTER_TAXONOMY: " + "; ".join(bits)))

    if not out:
        out.append((INFO, f"restated sets match canon (pull-complete = "
                          f"{{{', '.join(sorted(truth))}}}; clusters = {len(clusters)})"))
    return out


CHECKS = [
    ("version_drift", check_version_drift),
    ("claude_md_version_drift", check_claude_md_version_drift),
    ("restated_set_drift", check_restated_set_drift),
    ("board_reconcile", check_board_reconcile),
    ("log_reconcile", check_log_reconcile),
    ("cron_liveness", check_cron_liveness),
    ("intake_liveness", check_intake_liveness),
    ("cushing_capability", check_cushing_capability),
    ("outbox_age", check_outbox_age),
    ("registry_staleness", check_registry_staleness),
    ("registry_lag", check_registry_lag),
    ("liaison_enum", check_liaison_enum),
    ("delivered_but_unconsumed", check_delivered_but_unconsumed),
    ("written_but_undelivered", check_written_but_undelivered),
    ("deep_research_pending_overdue", check_deep_research_pending_overdue),
    ("staleness_sweep_overdue", check_staleness_sweep_overdue),
    ("dropzone_pending", check_dropzone_pending),
    ("boot_protocol_xref", check_boot_protocol_xref),
    ("status_spine_overflow", check_status_spine_overflow),
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
