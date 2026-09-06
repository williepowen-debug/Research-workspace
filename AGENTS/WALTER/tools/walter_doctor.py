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
  registry_self_lag      WALTER's own REGISTRY row vs WALTER STATUS.md header date
  liaison_enum           LIAISON files on disk (informational)
  delivered_but_unconsumed  inbox/WALTER/ handoff delivered but not moved to processed/ (>N days)
  written_but_undelivered   inbox/WALTER/ handoff committed-local but not on origin (git-derived)
  delivery_claim_vs_git    delivery_log says 'delivered' but git says untracked/gone (2026-07-27 orphan class)
  deep_research_pending_overdue  DEEP_RESEARCH_FLAGGED_LOG row PENDING past its deadline (or stale open >30d)
  dewey_handoff_liveness  DEWEY handoff sitting NEW in inbox/DEWEY/ >1d (backstop-A liveness alarm)
  staleness_sweep_overdue  last STALENESS_SWEEP_*.tsv vs 14d cadence (lifecycle-tagging lapse guard)
  dropzone_pending       unprocessed items in the inbox/WILL/ desktop drop-zone (backstops step 7f)
  boot_protocol_xref     every [→ BP §x] pointer resolves to a real BOOT_PROTOCOL section (and back)
  status_spine_overflow  STATUS.md dated-lead count vs the ~5 cap (protocol §12 spine-trim guard)
  restated_set_drift     prose restatements of a SET/COUNT vs canonical source (3 seeds; see docstring)
  cluster_review_overdue  days since each large cluster's last coherence review (cadence prompt)
  registered_but_unrouted agent has a REGISTRY row but zero ROUTING_TABLE presence
  correction_target_declared  every `signal_type: correction` declares a resolvable `corrects:` (SIG-ID/SELF/EXTERNAL)
  batch_manifest_open    a declared Will-batch left OPEN with un-dispositioned items (the input-side blind spot)
  action_line_rule       an agent on `info:` while the body carries ask-language naming it (§3.5.4, mechanized)
  terry_override_ratio   S1 — TERRY inverted-token override ratio (90d/10%/n≥10) + the 72h revert falsifier
  filed_vs_consumed      S7 — processed/ moves without a consume:<AGENT> declaration are FILED, not CONSUMED (§5.1)
  entities_at_dispatch   `entities:` header present on every signal dated ≥2026-08-19 (FORMAT_SPEC v0.18, never retro)
  index_generated_fresh  BOARD/INDEX.md rowset sha vs a fresh regeneration (WQ-174; pre-cutover = generator --check soak)
  auto_load_budget       CLAUDE.md's UNCONDITIONAL auto-load cost vs the read cap (read_cap_check cannot see it)

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
ACTION_LINE_WINDOW_DAYS = 14   # trailing scan window for check_action_line_rule (#27)
# Accepts an optional trailing annotation like "SIG-W-20260414-010 (re-route)" — deliberate
# semantic content in route_log (DAEDALUS RAV-review FIX 1, 2026-08-02). Still anchored:
# rejects -0011→-001 truncation and anywhere-on-line matches (both RAV fixes survive).
SIG_ID_RE = re.compile(r"^(SIG-W-\d{8}-\d{3})(\s+\(.+\))?$")

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


def _agent_paths(agent: str) -> "tuple[str | None, str]":
    """Resolve (status_relpath | None, dir_relpath) for a registry agent.

    Most desks live at AGENTS/<NAME>/. PROME does NOT: its home is PROME/ at the
    repo root, and root CLAUDE.md forbids recreating AGENTS/PROME/. Every registry
    check hardcoded the AGENTS/ prefix, so the coordinator -- the desk that commits
    most often -- could never raise a lag flag however stale its row got. Found
    2026-08-30 with PROME's row FOUR of its sessions stale and registry_lag printing
    its all-clear line.

    The mechanism is worse than "invisible", and a positive-control probe against the
    pre-patch code is what corrected the first diagnosis (which said `uncheckable`):
    AGENTS/PROME/ HAS commit history -- from the accidental recreations root CLAUDE.md
    warns about ("silently regrows"; twice in 8/27-8/28). So the dir fallback resolved,
    and PROME was graded against the commit dates of an erroneously-recreated directory,
    landing in the `dir_only` INFO bucket that is explicitly "NOT flagged". A wrong
    referent inside a bucket that cannot escalate -- clean scan, wrong object.
    [[finding_instrument_reports_clean_against_the_wrong_reference]]

    Resolved by LOOKING rather than by naming PROME, so a future root-level desk is
    covered without another edit. Returns status_relpath=None when neither location
    has a STATUS.md (RAV/DARWIN/BARON/HERMES/DEWEY as of 8/30) -- those keep the
    existing dir-fallback/uncheckable handling, which is correct for them."""
    nested = REPO / "AGENTS" / agent / "STATUS.md"
    if nested.exists():
        return f"AGENTS/{agent}/STATUS.md", f"AGENTS/{agent}/"
    root = REPO / agent / "STATUS.md"
    if root.exists():
        return f"{agent}/STATUS.md", f"{agent}/"
    return None, f"AGENTS/{agent}/"


def _status_header_date(agent: str) -> "dt.date | None":
    """The agent's OWN self-declared last-update date — the first date directly
    after an 'Updated:' / 'Last Updated:' marker in the first ~25 STATUS.md lines.
    Distinguishes a real self-update from an incidental cross-agent commit that
    merely touched the file (the registry_lag false-positive class, e.g. the 6/19
    REGINALD CORAL-promotion ref-sweep). Returns None if no canonical marker is
    found — caller then falls back to commit-date logic (no regression)."""
    rel, _ = _agent_paths(agent)
    if rel is None:
        return None
    try:
        head = (REPO / rel).read_text(errors="replace").splitlines()[:25]
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


def _registry_row(agent_name: str):
    """Return (tier, updated_date|None) for one REGISTRY row, including WALTER self."""
    with (WALTER / "REGISTRY.tsv").open(errors="replace") as f:
        rdr = csv.reader(f, delimiter="\t")
        header = next(rdr, [])
        try:
            i_up, i_tier, i_agent = (header.index("Updated"),
                                     header.index("Tier"), header.index("Agent"))
        except ValueError:
            return None
        for row in rdr:
            if len(row) <= max(i_up, i_tier, i_agent):
                continue
            if row[i_agent].strip() != agent_name:
                continue
            m = re.search(r"\d{4}-\d{2}-\d{2}", row[i_up])
            updated = dt.date.fromisoformat(m.group(0)) if m else None
            return row[i_tier].strip(), updated
    return None


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
def _missed_weekday_runs(last_run_date, today):
    """Weekdays STRICTLY AFTER last_run_date through today inclusive — i.e. how many
    days the weekday-daily collector was expected to run and (as far as this file
    knows) did not.

    Why this exists: the check previously counted CALENDAR days against a WEEKDAY
    collector, so a Friday run read as 3d stale on Monday and fired a MED every
    single Monday and after every holiday. That trains the reader to dismiss the one
    tier a real collector death appears in. Found at the 2026-08-03 closeout by
    checking `date +%A` before escalating to PROME, and deliberately NOT patched
    that night — shipping an untested guard change is the failure
    `finding_test_the_guard_not_just_the_guarded` exists to prevent.

    ⚠️ KNOWN LIMIT, stated rather than silently accepted: US market holidays are not
    modelled (no holiday calendar dependency, and `finding_holiday_calendar_domain_mismatch`
    warns that the obvious library omits Good Friday anyway). A holiday therefore still
    counts as a missed run. That is the FALSE-POSITIVE direction, which is the correct
    way for this to fail — it over-reports at most a handful of days a year, versus a
    false NEGATIVE that would hide a dead collector."""
    if last_run_date > today:
        return 0
    n, d = 0, last_run_date + dt.timedelta(days=1)
    while d <= today:
        if d.weekday() < 5:
            n += 1
        d += dt.timedelta(days=1)
    return n


def check_intake_liveness():
    """Health self-alarm for the RESEARCH-INTAKE collection lane (WALTER's consumer
    per PROME 2026-06-29). Reads the on-disk liveness.json (boot step 7e re-pulls
    the lane fresh + runs intake_scan for the significance gate — this check is the
    boot-time backstop that alarms if the collector died).

    Staleness is measured in MISSED WEEKDAY RUNS, not calendar days — the collector
    is weekday-daily, so a Fri→Mon gap is 1 missed run, not 3 (see
    `_missed_weekday_runs`). >2 missed weekday runs = collector likely down → flag PROME."""
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
    age = missed = None
    try:
        lrt = dt.datetime.fromisoformat(lr.replace("Z", "+00:00"))
        now = dt.datetime.now(dt.timezone.utc)
        age = (now - lrt).days
        missed = _missed_weekday_runs(lrt.date(), now.date())
    except (ValueError, AttributeError):
        pass
    if missed is None:
        out.append((MED, "last_run_utc missing/unparseable"))
    elif missed > 2:
        out.append((MED, f"lane STALE — {missed} missed weekday run(s), {age} calendar days "
                        f"(last_run {lr}) — collector likely down; flag PROME "
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
        out.append((INFO, f"lane live (last_run {lr}, {age}d / {missed} missed weekday run(s), "
                        f"{nfeeds} feeds ok); gate via boot-7e intake_scan.py"))
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
        status_rel, dir_rel = _agent_paths(agent)
        commit = _git_last_commit_date(status_rel) if status_rel else None
        if commit is None:
            # No (current) STATUS.md → a dir-level commit is an unreliable proxy:
            # it catches cross-agent / bulk commits that merely touched the dir
            # (e.g. DARWIN's "4/30" was a HANS/MARCO-STATUS + memory-log commit).
            # Surface as INFO, never let it drive a MED/LOW lag flag.
            dcommit = _git_last_commit_date(dir_rel)
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


def check_registry_self_lag():
    """WALTER is intentionally excluded from _registry_rows() so cross-agent
    lag checks do not self-noise. This check covers the remaining blind spot:
    WALTER's own REGISTRY row must not lag its STATUS.md header date silently."""
    row = _registry_row("WALTER")
    if row is None:
        return [(MED, "WALTER missing from REGISTRY.tsv — self row absent")]
    _tier, updated = row
    if updated is None:
        return [(LOW, "WALTER REGISTRY row has no parseable Updated date")]
    status = _status_header_date("WALTER")
    if status is None:
        return [(LOW, "WALTER STATUS.md has no parseable Updated header — self-registry lag unchecked")]
    lag = (status - updated).days
    if lag >= 1:
        sev = MED if lag >= 3 else LOW
        return [(sev, f"WALTER: REGISTRY row {updated.isoformat()} < STATUS header "
                      f"{status.isoformat()} (+{lag}d) → refresh WALTER self row at closeout")]
    return [(INFO, "WALTER self REGISTRY row is current vs STATUS.md header")]


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
DELIVERY_REF = "origin/master"


_EVER_IN_GIT_CACHE = {}
_ORIGIN_PATHS = None          # None = not built yet; False = build FAILED (=> all UNKNOWN)


def _origin_path_set():
    """Every path `DELIVERY_REF` history has ever named, built ONCE per run.

    Added 2026-09-05 with the twin-verification fix: verifying a processed/ twin as well
    as the primary path took this check from ~200 `git log` calls to ~2 PER ROW (≈2,000
    processes, minutes of wall clock). One `git log --name-only` over the whole ref costs
    ~1.2s and answers every lookup. A MISS still falls back to a precise per-path query,
    so the set can only ever cost a slower NEGATIVE, never a false POSITIVE — and a build
    failure returns UNKNOWN for everything rather than a cheap green.
    """
    global _ORIGIN_PATHS
    if _ORIGIN_PATHS is None:
        try:
            r = subprocess.run(["git", "-C", str(REPO), "log", DELIVERY_REF,
                                "--pretty=format:", "--name-only", "--full-history"],
                               capture_output=True, text=True, timeout=120)
            _ORIGIN_PATHS = (set(filter(None, r.stdout.splitlines()))
                             if r.returncode == 0 else False)
        except (OSError, subprocess.SubprocessError):
            _ORIGIN_PATHS = False
    return _ORIGIN_PATHS


def _ever_in_git(relpath: str):
    """Was this path EVER in history REACHABLE FROM origin/master?

    True  = origin saw it, it is gone from disk now -> consumed / cleaned up / retired dir.
    False = origin has NEVER seen it                -> real orphan.
    None  = git could not answer                    -> UNKNOWN, which is NOT delivery.

    A recipient may consume by moving to processed/ OR by DELETING outright (BOND
    drains that way), and a whole inbox dir can be legitimately retired (AGENTS/PROME/
    was declared dead 2026-07-24). Those are the True cases this discriminator exists for.

    🔴 FIXED 2026-09-05 (Codex finding 2), TWO defects in one function:
    (a) `--all` included UNPUSHED LOCAL COMMITS, so a handoff that never reached
        origin read as delivered — while `delivered` is DEFINED as committed AND
        on origin; and
    (b) the exception branch returned True with the comment "fail SAFE: unknown ->
        assume delivered, never cry wolf." That is fail-OPEN, not fail-safe: it
        converts UNAVAILABLE EVIDENCE into PRESUMED DELIVERY, which is the one
        direction that never prompts a re-check. Not crying wolf is not a goal a
        delivery check may trade correctness for.
    `[[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]`
    `[[finding_instrument_reports_clean_against_the_wrong_reference]]`
    """
    if relpath in _EVER_IN_GIT_CACHE:
        return _EVER_IN_GIT_CACHE[relpath]
    paths = _origin_path_set()
    if paths is False:                    # the one-shot build failed
        _EVER_IN_GIT_CACHE[relpath] = None
        return None
    if relpath in paths:                  # positive: answered from the set
        _EVER_IN_GIT_CACHE[relpath] = True
        return True
    try:                                  # miss: confirm the NEGATIVE precisely
        r = subprocess.run(["git", "-C", str(REPO), "log", DELIVERY_REF, "--oneline", "-1",
                            "--", relpath], capture_output=True, text=True, timeout=10)
        val = None if r.returncode != 0 else bool(r.stdout.strip())
    except (OSError, subprocess.SubprocessError):
        val = None   # fail CLOSED: unknown is UNKNOWN, never "delivered"
    _EVER_IN_GIT_CACHE[relpath] = val
    return val


_HANDOFF_SCAFFOLD = {"README.md", ".gitkeep", ".gitignore", ".DS_Store"}


def _handoff_files():
    """Non-processed WALTER delivery handoffs: (path, recipient, relpath).
    Globs AGENTS/*/inbox/WALTER/*.md, excluding anything under processed/.
    Single-machine: every recipient is CC → delivered = committed AND on origin."""
    out = []
    for p in (REPO / "AGENTS").glob("*/inbox/WALTER/*.md"):
        if "/processed/" in p.as_posix():
            continue
        # Scaffolding is not a delivery. Same skip-set this file already applies in
        # check_dropzone_pending + the inbox scan; matched here rather than widened.
        # 2026-08-23: the headline "oldest 57d" in delivered_but_unconsumed was
        # AGENTS/DEWEY/inbox/WALTER/README.md — a README, aged on mtime because it has
        # no delivery_log row. It topped the distribution WALTER quoted to PROME as
        # "oldest 56d" (rider R2). A scaffolding file counted as an unconsumed delivery
        # inflates the worst number the check emits, and mtime is the one basis root
        # canon forbids keying on. `[[finding_mtime_is_corrupted_by_git_sync]]`
        if p.name in _HANDOFF_SCAFFOLD:
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
    'no_origin' (origin ref missing) / 'unknown' (git error).

    🔴 FIXED 2026-09-05 (Codex second pass, HIGH). Neither `git` invocation checked
    its RETURN CODE. A failing `git status` (exit 128, empty stdout) fell through the
    `st.stdout.strip()` test as though the tree were clean; a failing `rev-list` then
    parsed `int("" or "0") == 0` and the function returned **`on_origin`** — a POSITIVE
    DELIVERY VERDICT MANUFACTURED OUT OF A GIT FAILURE. Empty output from a broken
    command is not the same fact as empty output from a working one, and only the exit
    code separates them.

    THE INVARIANT, now applied on every branch here and in every caller: a POSITIVE
    delivery verdict requires SUCCESSFUL origin evidence; unavailable evidence stays
    UNKNOWN all the way through to the final report.
    `[[finding_lenient_parser_reports_unparseable_as_a_behavior]]`
    `[[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]`
    """
    try:
        st = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain", "--",
                             relpath], capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return "unknown"
    if st.returncode != 0:
        return "unknown"
    if st.stdout.strip():
        return "uncommitted"           # untracked or modified
    if origin_ref is None:
        return "no_origin"
    try:  # committed — any commit touching it reachable from HEAD but not origin?
        rl = subprocess.run(["git", "-C", str(REPO), "rev-list", "--count", "HEAD",
                             "--not", "--remotes=origin", "--", relpath],
                            capture_output=True, text=True, timeout=10)
        if rl.returncode != 0 or not rl.stdout.strip():
            return "unknown"
        return "ahead" if int(rl.stdout.strip()) > 0 else "on_origin"
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


def _delivery_routed_dates():
    """{(signal_id, RECIPIENT_UPPER): date} from delivery_log.tsv `timestamp_routed`.

    ⚠️ THE AGE BASIS MUST NOT BE mtime. Root CLAUDE.md forbids keying any freshness
    mechanism on mtime — git sync restamps it and the failure is FALSE-NEGATIVE, i.e.
    it under-reports the backlog, which is the flattering direction and therefore the
    one nobody re-checks. Measured 2026-08-20: three handoffs dispatched 8/19 already
    carried 8/18 mtimes on ONE machine with no switch; serial multi-machine operation
    (the documented model, not a contingency) would break it outright.
    `[[finding_mtime_is_corrupted_by_git_sync]]`"""
    out = {}
    log = WALTER / "routed" / "delivery_log.tsv"
    try:
        rows = log.read_text(encoding="utf-8").splitlines()
    except OSError:
        return out
    for ln in rows[1:]:
        c = ln.split("\t")
        if len(c) >= 3 and c[0].strip():
            out[(c[1].strip(), c[2].strip().upper())] = c[0].strip()[:10]
    return out


def _bare_sig(stem):
    """`SIG-W-20260819-011-long-slug-here` -> `SIG-W-20260819-011`.

    🔴 THE DEFECT THIS EXISTS TO FIX (found 2026-08-20): the unconsumed check built its
    delivery_log lookup key from the FULL FILENAME STEM while delivery_log stores the
    BARE signal id, so the key NEVER matched, every row fell through to role "?", and
    "?" is not "ACTION" — therefore `action_total` was STRUCTURALLY ALWAYS ZERO. The
    check then reported "0 ACTION / N INFO" as a FINDING and downgraded its own severity
    to LOW "all-INFO cc-pile, low-stakes" on that artifact. True figure at discovery:
    73 unconsumed ACTION items. An unconsumed ACTION handoff — which this check's own
    docstring calls "the real risk" — was invisible by construction.
    `[[finding_registry_names_a_concept_tool_resolves_an_instrument]]` (diff the registry
    against the code) + `[[finding_verification_zero_is_ambiguous]]` (a zero that means
    "never in its scope")."""
    m = re.match(r"(SIG-W-\d{8}-\d{3})", stem)
    return m.group(1) if m else stem


# Recipients whose OWN boot scan is a COMPLETE whole-INDEX /BOARD/ diff (dispositions
# every unrecorded SIG-W across all of INDEX) → complete pull; WALTER SKIPS inbox
# delivery to them (BOARD_CONSUMPTION_SPEC §3.5, v0.7, verified 2026-07-04). Any handoff
# in their inbox is a to-ARCHIVE residue, NOT a consume-gap. Verify "complete" (not
# tiered/selective) empirically before adding an agent. REGINALD/SAM are NOT complete.
PULL_COMPLETE = {"CARL", "RED", "PROME", "TERRY"}  # TERRY added 2026-08-26: §3.5.5 falsifier revert (exemption-by-falsifier, not pull-complete-warrant; SPEC v0.21)


_BOARD_LOG_CACHE = {}


def _recipient_board_log(recipient):
    """The recipient's OWN consumption record (`AGENTS/<X>/board_log.tsv`), read raw.
    Empty string when the desk keeps no board_log — which is NOT evidence either way."""
    k = recipient.upper()
    if k not in _BOARD_LOG_CACHE:
        f = REPO / "AGENTS" / recipient / "board_log.tsv"
        try:
            _BOARD_LOG_CACHE[k] = f.read_text(errors="replace") if f.exists() else ""
        except OSError:
            _BOARD_LOG_CACHE[k] = ""
    return _BOARD_LOG_CACHE[k]


def check_delivered_but_unconsumed():
    """A delivered handoff (on origin) sitting >N days without being moved to
    processed/ → the recipient's Phase-2 consume boot-step may not be installed.
    The visible Phase-2-gap telemetry."""
    files = _handoff_files()
    if not files:
        return [(INFO, "no WALTER handoffs in flight")]
    origin = _origin_ref()
    routed_dates = _delivery_routed_dates()
    aged, pull_complete, no_row = [], [], 0
    consumed_not_filed = []
    for p, recipient, relpath in files:
        if _sync_state(relpath, origin) != "on_origin":
            continue  # not delivered yet → written_but_undelivered owns it
        stem = p.name[:-3] if p.name.endswith(".md") else p.name
        sig = _bare_sig(stem)
        routed = routed_dates.get((sig, recipient.upper()))
        if routed:
            try:
                age = _age_days(dt.date.fromisoformat(routed))
            except ValueError:
                age = _age_days(dt.date.fromtimestamp(p.stat().st_mtime))
        else:
            # No delivery_log row (notes, backfilled handoffs) — mtime is the only
            # basis available. Counted, and disclosed in the summary rather than
            # silently mixed in with the properly-dated rows.
            age = _age_days(dt.date.fromtimestamp(p.stat().st_mtime))
            no_row += 1
        if age > N_UNCONSUMED_DAYS:
            # 🔴 CROSS-CHECK THE RECIPIENT'S OWN CONSUMPTION RECORD BEFORE CALLING
            # IT UNCONSUMED (2026-08-23, on Will's challenge: "are you sure these have not
            # been consumed?"). File-position is a PROXY for non-consumption, not a
            # measurement — §5.1 explicitly contemplates a desk integrating content and
            # never filing the handoff, and nothing here would have seen it.
            # `[[finding_delivery_check_is_not_a_knowledge_check]]` — "did it arrive?" and
            # "do they know?" are different questions, and the OWNER's log answers the second.
            # ⚠️ HONEST PROVENANCE: this check was built expecting to find such cases and
            # FINDS ZERO across the whole backlog. The one apparent instance (BRENT
            # SIG-W-20260803-001, "20d unconsumed" while BRENT's board_log recorded it
            # `acted` inside 90 minutes) was a defect in WALTER's own ad-hoc query, which
            # tested whether delivery_log's recorded path EXISTS — and that path already
            # pointed into processed/. The doctor was right; the throwaway script was not.
            # Kept anyway, because a check that returns zero UPGRADES the evidence class:
            # for a desk that keeps a board_log, "unconsumed" is now corroborated by the
            # recipient's own record rather than inferred from where a file sits.
            # ⚠️ ABSENCE FROM A board_log IS NOT PROOF OF NON-CONSUMPTION, and a desk with
            # NO board_log (ZHAO, OTTO, WATT, HANS …) cannot be tested at all — those stay
            # in `aged` as an UPPER BOUND, never as a measurement.
            if sig and sig in _recipient_board_log(recipient):
                consumed_not_filed.append((recipient, sig, age))
            else:
                (pull_complete if recipient.upper() in PULL_COMPLETE else aged).append(
                    (recipient, sig, age))
    # Pull-complete recipients (WALTER skips delivery, §3.5) — residual handoffs are a
    # one-time to-ARCHIVE cleanup by PROME, NOT a consume-gap (+ a re-delivery tripwire).
    pc = []
    if consumed_not_filed:
        c = {}
        for r, _s, _a in consumed_not_filed:
            c[r] = c.get(r, 0) + 1
        pc.append((LOW, "CONSUMED but never filed to processed/ — the recipient's OWN "
                   "board_log records these, so they are filing hygiene, NOT a consume-gap: "
                   + ", ".join(f"{r} {n}" for r, n in sorted(c.items()))
                   + " — excluded from the unconsumed count below (they were being counted)"))
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
    # ⚠️ SCOPE MUST BE ON THE LINE (2026-08-20). This block counts handoffs unconsumed
    # for MORE THAN N_UNCONSUMED_DAYS — a deliberate grace period — but the summary
    # used to read "N delivered-but-unconsumed", which a reader (including WALTER)
    # takes as THE BACKLOG. Found when OSPREY self-reported 8 unprocessed WALTER items
    # while this line said "OSPREY 1": 7 of its 8 were 1-2d old and correctly excluded
    # by the threshold, yet the label implied they did not exist. The number was right
    # for what it measured; the LABEL overstated its scope.
    # `[[finding_verification_zero_is_ambiguous]]` — a check certifies its SCOPE.
    total_in_flight = len(files)
    nr = f", {no_row} on mtime (no delivery_log row)" if no_row else ""
    summary = (f"{len(aged)} unconsumed >{N_UNCONSUMED_DAYS}d across {len(by_rcpt)} agents "
               f"(of {total_in_flight} in flight — the rest are within the grace period, "
               f"NOT evidence they are consumed), oldest {oldest}d — "
               f"{action_total} ACTION / {info_total} INFO: {'; '.join(parts)}"
               f" [age from delivery_log.timestamp_routed{nr}]")
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


# ── delivery_log CLAIM vs git REALITY (the 2026-07-27 orphan class) ───────────
def check_delivery_claim_vs_git():
    """`delivery_log.written_state` says 'delivered' — does git agree?

    WHY THIS EXISTS (2026-07-27): 21 of 25 handoffs for SIG-W-20260727-017..020
    were written to disk, logged `delivered`, and never committed. A computed
    pathspec (`AGENTS/*/inbox/WALTER/`) matched NOTHING — a git pathspec that
    contains a wildcard AND ends at a directory matches no files, and because it
    was piped through `git status` into a shell variable rather than handed to
    `git add`, the one error git would have raised never fired. Every step
    returned success.

    `written_but_undelivered` DID see all 21 — and graded them LOW with the label
    "(mid-session)", i.e. it saw the state and called it normal. That is correct
    for a handoff not yet logged; it is wrong once the LOG ALREADY CLAIMS
    DELIVERED. Nothing compared the two surfaces, so the log and the doctor
    asserted contradictory things about the same files and neither noticed.

    THIS CHECK IS THE COMPARISON. Same family as version_drift / restated_set_drift:
    a claim in one surface tested against the artifact it describes.

    Consumption is SUCCESS, not a miss: a recipient moving the handoff to
    `processed/` legitimately empties the logged path, so a missing file is only a
    failure when no tracked `processed/` twin exists (that is the BROCK case from
    the same session — it consumed two files that were never committed, and they
    survived only because BROCK committed them itself).

    Age-scoped to avoid firing on a statement that is always true: writing a row
    and its file together, then committing minutes later, is the normal flow. A
    row that has crossed a SESSION BOUNDARY still untracked is a different animal.
    """
    log = WALTER / "routed" / "delivery_log.tsv"
    if not log.exists():
        return [(INFO, "no delivery_log.tsv")]
    origin = _origin_ref()
    today_untracked, prior_untracked, lost, stale_path, ahead = [], [], [], [], 0
    unknown_path, unverified = [], []
    seen = set()
    try:
        with log.open(errors="replace") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                state = (row.get("written_state") or "").strip()
                rel = (row.get("handoff_path") or "").strip()
                sig = (row.get("signal_id") or "?").strip()
                rcp = (row.get("recipient") or "?").strip()
                ts = (row.get("timestamp_routed") or "").strip()
                if not rel or state != "delivered" or (sig, rcp) in seen:
                    continue
                seen.add((sig, rcp))
                path = REPO / rel
                if path.exists():
                    sync = _sync_state(rel, origin)
                    if sync == "on_origin":
                        continue
                    if sync == "ahead":
                        ahead += 1
                        continue
                    if sync == "uncommitted":
                        (today_untracked if ts[:10] == TODAY.isoformat()
                         else prior_untracked).append(f"{sig}->{rcp}")
                        continue
                    # 🔴 FIXED 2026-09-05 (Codex second pass): 'unknown' and 'no_origin'
                    # used to fall through a bare `continue` — SILENTLY SKIPPED, after
                    # which the all-clear below announced that EVERY delivered row was
                    # backed. A row we could not check is not a row that passed.
                    unverified.append(f"{sig}->{rcp} [{sync}]")
                    continue
                # Gone from the logged path. That is USUALLY success, not failure:
                #   - recipient moved it to processed/       (the common convention)
                #   - recipient consumed by DELETING it      (BOND drains this way)
                #   - the whole inbox dir was retired        (AGENTS/PROME/, dead 7/24)
                # The only real orphan is a path git has NEVER SEEN. Verified 2026-07-27:
                # a processed/-twin-only test produced 17 false HIGHs on its first run
                # (14 dead-PROME-dir + 3 BOND drains) - every one of which WAS delivered.
                # 🔴 FIXED 2026-09-05 (Codex second pass): a processed/ twin used to pass
                # on DISK EXISTENCE ALONE. An UNTRACKED twin — one that never reached
                # origin — certified the delivery. Existence on this box is not evidence
                # about origin; verify the twin's history exactly like the primary path.
                twin = path.parent / "processed" / path.name
                if twin.exists():
                    twin_hist = _ever_in_git(str(twin.relative_to(REPO)))
                    if twin_hist is True:
                        continue
                    if twin_hist is None:
                        unverified.append(f"{sig}->{rcp} [twin-unverifiable]")
                        continue
                    unverified.append(f"{sig}->{rcp} [twin present but NEVER on {DELIVERY_REF}]")
                    continue
                on_origin_hist = _ever_in_git(rel)   # NOT `seen` — that name is the dedup set above
                if on_origin_hist is True:
                    stale_path.append(f"{sig}->{rcp}")
                    continue
                if on_origin_hist is None:            # git could not answer
                    unknown_path.append(f"{sig}->{rcp} ({rel})")
                    continue
                lost.append(f"{sig}->{rcp} ({rel})")
    except (OSError, csv.Error) as e:
        return [(LOW, f"delivery_log unreadable for claim-vs-git check: {e}")]

    out = []
    if prior_untracked:
        out.append((HIGH, f"{len(prior_untracked)} delivery_log row(s) claim 'delivered' but "
                          f"the file is UNTRACKED and the row PRE-DATES today — the log has "
                          f"been false across a session boundary: "
                          f"{', '.join(prior_untracked[:6])}"
                          f"{' …' if len(prior_untracked) > 6 else ''} — commit by EXPLICIT PATH"))
    if today_untracked:
        out.append((MED, f"{len(today_untracked)} delivery_log row(s) written today claim "
                         f"'delivered' but the file is UNTRACKED — normal mid-dispatch, MUST "
                         f"be committed before closeout: {', '.join(today_untracked[:6])}"
                         f"{' …' if len(today_untracked) > 6 else ''}"))
    if lost:
        out.append((HIGH, f"{len(lost)} delivery_log row(s) claim 'delivered' but the file is "
                          f"GONE with no processed/ twin — content may be lost: "
                          f"{', '.join(lost[:4])}{' …' if len(lost) > 4 else ''}"))
    if ahead:
        out.append((INFO, f"{ahead} handoff(s) committed but not yet on origin — "
                          f"written_but_undelivered owns those"))
    if unknown_path:
        out.append((MED, f"{len(unknown_path)} delivery_log row(s) could NOT be verified against "
                         f"{DELIVERY_REF} (git gave no answer) — these are UNKNOWN, not delivered "
                         f"and not orphaned: {', '.join(unknown_path[:4])}"
                         f"{' …' if len(unknown_path) > 4 else ''}. Fetch and re-run; do not read "
                         f"unavailable evidence as delivery."))
    if unverified:
        out.append((MED, f"{len(unverified)} delivery_log row(s) claim 'delivered' and could NOT "
                         f"be verified against {DELIVERY_REF} — git failed, the origin ref was "
                         f"missing, or a processed/ twin exists only on this disk. UNKNOWN is not "
                         f"a pass: {', '.join(unverified[:4])}"
                         f"{' …' if len(unverified) > 4 else ''}"))
    if stale_path:
        out.append((INFO, f"{len(stale_path)} row(s) point at a path that no longer exists "
                          f"but WAS in git (consumed-by-delete, or a retired inbox dir) — "
                          f"delivery confirmed, path stale; log hygiene, not a gap"))
    if not out:
        return [(INFO, "every 'delivered' delivery_log row is backed by a tracked file "
                       "(or a consumed processed/ twin)")]
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
            disp = (row.get("disposition") or "").strip().upper()
            # Terminal BLACKLIST, not an open-state whitelist. Was `!= "PENDING"`,
            # which silently skipped QUEUED and PARTIAL: on 2026-08-13 two rows
            # (REQ-DEWEY-20260702-007 / -009) sat QUEUED 35d and 30d past their
            # deadlines while this check printed "no overdue deep-research flags".
            # QUEUED is *more* forgotten than PENDING, and the docstring above
            # promises exactly that class. A whitelist misses every open state
            # nobody thought to add; a terminal blacklist over-reports instead,
            # which is the right failure direction for a health check.
            if disp.startswith("RESOLVED") or disp.startswith("DROPPED"):
                continue
            n_pending += 1
            sig = (row.get("signal_id") or "?").strip()
            lbl = disp or "NO-DISPOSITION"
            m = re.search(r"\d{4}-\d{2}-\d{2}", row.get("deadline") or "")
            if m:  # real date deadline → overdue if passed
                try:
                    dl = dt.date.fromisoformat(m.group(0))
                except ValueError:
                    continue
                if dl < TODAY:
                    out.append((MED, f"{sig}: deep-research flag {lbl} past deadline "
                                    f"{dl.isoformat()} ({_age_days(dl)}d overdue) — run it or drop it"))
            else:  # no date (deadline=open/blank) → stale if flagged >30d ago
                fm = re.search(r"\d{4}-\d{2}-\d{2}", row.get("flagged_date") or "")
                if fm and _age_days(dt.date.fromisoformat(fm.group(0))) > 30:
                    out.append((MED, f"{sig}: deep-research flag {lbl} (deadline=open) flagged "
                                    f"{_age_days(dt.date.fromisoformat(fm.group(0)))}d ago — disposition it"))
    if not out:
        return [(INFO, f"no overdue deep-research flags ({n_pending} open)")]
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
    # THE TABLE MOVED (2026-08-30). KEY DESIGN FILES + CANONICAL-SOURCE LOOKUP were split
    # to design/SPEC_OWNERSHIP.md to get the always-loaded CLAUDE.md under the read cap
    # (75,296 -> 51,121 B). This check greps for table ROWS, so after the move it matched
    # nothing and reported "version claims match spec headers" — a VACUOUS PASS. It was
    # not verifying anything; it had run out of things to verify and said OK.
    # ⇒ Scan BOTH files, and FAIL LOUD when zero claims are found anywhere: a check that
    # finds nothing to check must say so, never pass. Silence and success must not render
    # identically. [[finding_verification_zero_is_ambiguous]]
    from version_drift_check import SPECS, spec_version
    srcs, missing = [], []
    for fn in ("CLAUDE.md", "design/SPEC_OWNERSHIP.md"):
        try:
            srcs.append((fn, (WALTER / fn).read_text(errors="replace")))
        except OSError:
            missing.append(fn)
    if not srcs:
        return [(MED, f"neither CLAUDE.md nor design/SPEC_OWNERSHIP.md readable "
                      f"({', '.join(missing)}) — version claims UNVERIFIED, not clean")]
    claude = "\n".join(t for _, t in srcs)
    out, claims = [], 0
    for rel in SPECS:
        base = Path(rel).name
        hv = spec_version(WALTER / rel)
        if hv is None:
            continue
        # | `design/<base>` | **vN.M ...  — filename in cell-1, version leads cell-2
        m = re.search(rf"^\|\s*`?[^|]*{re.escape(base)}[^|]*`?\s*\|\s*\*{{0,2}}v(\d+\.\d+)",
                      claude, re.M)
        if m:
            claims += 1
            if m.group(1) != hv:
                out.append((MED, f"KEY DESIGN FILES row cites {base} at v{m.group(1)} "
                                f"but spec header is v{hv} — update the owning doc"))
    if claims == 0:
        out.append((MED, "ZERO KEY-DESIGN-FILES version claims found in CLAUDE.md or "
                         "design/SPEC_OWNERSHIP.md — the table moved, was renamed, or its "
                         "row format changed. This is NOT a pass: the check has nothing to "
                         "verify. Re-anchor it to wherever the table now lives."))
    elif not out:
        out.append((INFO, f"KEY-DESIGN-FILES version claims match spec headers "
                          f"({claims} claim(s) checked across {len(srcs)} file(s))"))
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

    def log_ids(relpath, field):
        p = WALTER / relpath
        if not p.exists():
            return None
        ids = set()
        malformed = []
        try:
            with p.open(errors="replace") as f:
                for n, row in enumerate(csv.DictReader(f, delimiter="\t",
                                                       quoting=csv.QUOTE_NONE), start=2):
                    sig = (row.get(field) or "").strip()
                    m = SIG_ID_RE.fullmatch(sig)
                    if m:
                        ids.add(m.group(1))
                    else:
                        malformed.append(f"L{n}:{sig or '<blank>'}")
        except (OSError, csv.Error) as e:
            return ids, [f"unreadable: {e}"]
        return ids, malformed

    out = []
    route = log_ids("routed/route_log.tsv", "Signal_ID")
    if route is None:
        # FIX 3 (PAT-060): an absent ledger must be LOUD — silence reads as clean.
        out.append((MED, "route_log.tsv ABSENT — BOARD reconcile did not run"))
    else:
        route, route_bad = route
        if route_bad:
            out.append((MED, f"route_log: malformed Signal_ID field(s): "
                            f"{', '.join(route_bad[:6])}{'…' if len(route_bad) > 6 else ''}"))
        orphan = sorted(route - board_ids)
        missing = sorted(board_ids - route)
        if orphan:
            out.append((MED, f"route_log: {len(orphan)} SIG-id(s) with NO BOARD file "
                            f"({', '.join(orphan[:4])}{'…' if len(orphan) > 4 else ''})"))
        if missing:
            out.append((MED, f"{len(missing)} BOARD file(s) never in route_log "
                            f"({', '.join(missing[:4])}{'…' if len(missing) > 4 else ''})"))
        if not orphan and not missing and not route_bad:
            out.append((INFO, f"route_log reconciles with BOARD ({len(board_ids)} signals)"))
    deliv = log_ids("routed/delivery_log.tsv", "signal_id")
    if deliv is None:
        out.append((MED, "delivery_log.tsv ABSENT — delivery reconcile did not run"))
    else:
        deliv, deliv_bad = deliv
        if deliv_bad:
            out.append((MED, f"delivery_log: malformed signal_id field(s): "
                            f"{', '.join(deliv_bad[:6])}{'…' if len(deliv_bad) > 6 else ''}"))
        d_orphan = sorted(deliv - board_ids)
        if d_orphan:
            out.append((MED, f"delivery_log: {len(d_orphan)} delivered SIG-id(s) with NO "
                            f"BOARD file ({', '.join(d_orphan[:4])})"))
        elif not deliv_bad:
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

    SCOPED TO THREE SEEDS ON PURPOSE (Will-approved 2026-07-16; seed 3 added same day).
    This is NOT a generic
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

    # ── Seed 3: the doctor's own check set ──────────────────────────────────────
    # Canonical = this module's CHECKS list — the strongest possible ground truth
    # (exact, no regex on the canon side). LOWEST-VALUE seed of the three and
    # deliberately labelled as such: a wrong check-count is COSMETIC (nobody acts on
    # it), unlike seeds 1-2 which guard BEHAVIOURAL claims (RULE 10 decides whether a
    # handoff gets written; step 11 runs on every dispatch). Added on near-zero-cost
    # grounds, not value — it caught two real drifts on 2026-07-16 (CLAUDE.md "the 15
    # checks" when there were 18; BP §0.5 enumerating 17, having never been given
    # status_spine_overflow when it landed 7/11).
    names = {n for n, _ in CHECKS}
    claude = _read(WALTER / "CLAUDE.md")
    if claude:
        m = re.search(r"BP §0\.5 for the (\d+) checks", claude)
        if not m:
            out.append((LOW, "CLAUDE.md step 0.5: check-count claim didn't match — "
                             "phrasing changed? re-anchor the regex"))
        elif int(m.group(1)) != len(names):
            out.append((MED, f"CLAUDE.md step 0.5 says 'the {m.group(1)} checks' but CHECKS "
                             f"has {len(names)} — stale restatement"))
    # this module's own docstring "Checks:" block — a 3rd restatement, and it was
    # itself stale (listed 15 of 20) when seed 3 was built. Self-referential on purpose.
    doc = __doc__ or ""
    block = re.search(r"^Checks:\n(.*?)^\n", doc, re.S | re.M)
    if block:
        docnames = set(re.findall(r"^  ([a-z_]+)\s", block.group(1), re.M))
        if docnames and docnames != names:
            miss, extra = names - docnames, docnames - names
            bits = []
            if miss:
                bits.append(f"CHECKS undocumented: {{{', '.join(sorted(miss))}}}")
            if extra:
                bits.append(f"documented but gone: {{{', '.join(sorted(extra))}}}")
            out.append((MED, "walter_doctor module docstring 'Checks:' ≠ CHECKS — " + "; ".join(bits)))

    bp = _read(WALTER / "design/BOOT_PROTOCOL.md")
    if bp:
        sec = re.search(r"^## §0\.5.*?(?=^## §\d)", bp, re.S | re.M)
        if not sec:
            out.append((LOW, "BOOT_PROTOCOL §0.5 span didn't parse — re-anchor before trusting"))
        else:
            listed = set(re.findall(r"^\d+\. \*\*([a-z_]+)\*\*", sec.group(0), re.M))
            if listed and listed != names:
                miss, extra = names - listed, listed - names
                bits = []
                if miss:
                    bits.append(f"CHECKS not enumerated: {{{', '.join(sorted(miss))}}}")
                if extra:
                    bits.append(f"enumerated but not in CHECKS: {{{', '.join(sorted(extra))}}}")
                out.append((MED, "BOOT_PROTOCOL §0.5 enumeration ≠ CHECKS — " + "; ".join(bits)))

    if not out:
        out.append((INFO, f"restated sets match canon (pull-complete = "
                          f"{{{', '.join(sorted(truth))}}}; clusters = {len(clusters)}; "
                          f"checks = {len(names)})"))
    return out


def check_cluster_review_overdue():
    """Has each large cluster been COHERENCE-REVIEWED lately — i.e. when did we last ask
    whether it is still answering one question?

    REPLACES `cluster_softcap_breach` (retired 2026-07-27, Will-approved). What changed
    and why, because the predecessor was not wrong so much as pointed at the wrong thing:

    The old check compared a cluster's live row-count against a `Soft cap` integer. It
    was built to fix a real failure — through v0.3 the taxonomy carried a rotting
    `Current count` column, so AI_INFRA_CAPEX read **3** against a cap of **15** while
    BOARD actually held **23**: a governance rule breached by 8, with nothing surfacing
    it, for ~6 weeks. **That lesson stands and is why this check is still MECHANIZED
    rather than becoming a remembered ritual** (`finding_mechanize_the_cap_not_the_ritual`).

    But the cap fired on the wrong measurement, and on 2026-07-27 that cost us. At 40/40
    the mandated v0.6 evaluation ran and limb (b) FIRED — two of four original angles had
    <2 signals in 60d — which reads at face value as "this cluster is decaying, split it."
    The angles were empty because **WALTER had never collected them** (TrendForce: 0 hits
    across 764 archive rows; Micron's beat never entered intake at all), and the filter
    had been audited clean. **A row count measures your own taxonomy and intake, never the
    domain** (`finding_count_measures_intake_not_domain`) — so the cap was capable of
    recommending a split of a healthy cluster on the strength of a collection gap.

    Two further problems with an absolute threshold: AI_INFRA_CAPEX was the ONLY capped
    cluster while IRAN_HORMUZ ran to 95, CONSUMER_STAGFLATION 103 and BANK_COLLATERAL 94
    uncapped and unremarked; and once size >= cap, EVERY subsequent dispatch re-fires the
    same prompt — noise on a live cluster during an active thesis.

    So this check asks a question that is always TRUE and always ACTIONABLE — *when did we
    last look?* — instead of one that makes a claim about the cluster. It cannot
    misdiagnose, because it does not diagnose; it just says "go evaluate."

    Grading is deliberately asymmetric:
      * MED  — a cluster WAS reviewed and the review has gone stale past REVIEW_DAYS. We
               know the question matters here and we let it rot: that is the real alarm.
      * INFO — large clusters never reviewed at all. Listed compactly, not alarmed, because
               8 simultaneous LOWs on day one is exactly the noise this replaces.

    A prompt, never a rule: it does NOT auto-split, auto-recut or block dispatch. Will
    signs off on any taxonomy change. Reviews live at `design/*AXIS_CHECK*<YYYY-MM-DD>.md`
    and are matched to clusters by CONTENT, not filename — the 7/16 and 7/27 reviews are
    named `AI_CAPEX_AXIS_CHECK_*` while the cluster is `AI_INFRA_CAPEX`, so filename
    matching would silently find nothing."""
    REVIEW_SIZE = 25      # below this, a cluster is too small to warrant periodic review
    REVIEW_DAYS = 30      # a coherence review older than this is stale
    idx = _read(BOARD / "INDEX.md")
    if idx is None:
        return [(LOW, "BOARD/INDEX.md unreadable — cluster review cadence unchecked")]
    live = {n: int(c) for n, c in re.findall(r"^## ([A-Z][A-Z_]+) \((\d+)\)$", idx, re.M)}
    if not live:
        return [(LOW, "no cluster sections parsed from BOARD/INDEX.md")]

    newest = {}   # cluster -> (date, filename)
    for f in sorted((WALTER / "design").glob("*AXIS_CHECK*.md")):
        m = re.search(r"(\d{4}-\d{2}-\d{2})", f.name)
        if not m:
            continue
        try:
            d = dt.date.fromisoformat(m.group(1))
        except ValueError:
            continue
        body = _read(f) or ""
        # A review must DECLARE its subject. Matching on any mention is a false-positive
        # factory: the 2026-07-27 review name-checks IRAN_HORMUZ / CONSUMER_STAGFLATION /
        # BANK_COLLATERAL / POSITIONING_VALUATION purely as peer-size comparisons, which
        # on a naive "name appears in body" match reported all four as freshly reviewed.
        # Caught in test before shipping. Explicit declaration beats inference.
        declared = re.findall(r"^reviews_cluster:\s*([A-Z][A-Z_]+)\s*$", body, re.M)
        if not declared:                                  # fallback: the H1 title only
            h1 = re.search(r"^#\s+(.+)$", body, re.M)
            declared = re.findall(r"[A-Z][A-Z_]{3,}", h1.group(1)) if h1 else []
        for name in declared:
            if name in live and (name not in newest or d > newest[name][0]):
                newest[name] = (d, f.name)

    today = dt.date.today()
    big = {n: c for n, c in live.items() if c >= REVIEW_SIZE}
    out, never = [], []
    for name, count in sorted(big.items()):
        if name not in newest:
            never.append(f"{name} {count}")
            continue
        d, fn = newest[name]
        age = (today - d).days
        if age > REVIEW_DAYS:
            out.append((MED, f"{name} ({count} signals): last coherence review was {age}d ago "
                             f"({fn}) — past the {REVIEW_DAYS}d window. Re-run the "
                             f"CLUSTER_TAXONOMY revisit test (bidirectional: angle count >5, "
                             f"or any original angle <2 signals in 60d). A PROMPT, not a rule "
                             f"— and check whether an empty angle is empty in the DOMAIN or "
                             f"empty in INTAKE before concluding anything."))
        else:
            out.append((INFO, f"{name} ({count}) reviewed {age}d ago ({fn}) — within the "
                              f"{REVIEW_DAYS}d window"))
    if never:
        out.append((INFO, f"large clusters never coherence-reviewed ({len(never)}, >={REVIEW_SIZE} "
                          f"signals): " + " · ".join(sorted(never, key=lambda x: -int(x.split()[-1])))
                          + " — informational, not a backlog; review is cheap and on-demand"))
    if not out:
        out.append((INFO, f"no clusters at or above the {REVIEW_SIZE}-signal review floor"))
    return out


def check_registered_but_unrouted():
    """An agent has a REGISTRY.tsv row but no ROUTING_TABLE presence — i.e. it is
    "registered" but nothing can actually route to it.

    Why it exists (the 2026-07-16 VULCAN/WATT/MIDAS incident): DAEDALUS built three
    agents 7/10-11 and wired NONE of them into routing — zero ROUTING_TABLE rows, no
    mention in any WALTER design doc, no inbox/WALTER/ dir, so none had ever received a
    routed signal. Meanwhile AI_INFRA_CAPEX — the cluster covering VULCAN's exact
    domain — grew to 23 signals routed to HENRY/LIQUID/VIOLET instead. It surfaced only
    because Will happened to ask whether VULCAN should be involved.

    The root cause is structural and WILL recur: REGISTRY and ROUTING_TABLE are separate
    surfaces that drift independently. WALTER's boot step-8 fs-scan adds a REGISTRY row
    for a live-but-unregistered agent (which is what registered all six on 7/16) — but
    **a REGISTRY row is not a routing row**, and nothing reconciled the two. So
    "registered" silently reads as "wired." DAEDALUS wired its 7/12 batch
    (OSPREY/FALCON/HOMER, ROUTING_TABLE v0.17) and missed the 7/10-11 batch; nothing
    caught the asymmetry for 6 days.

    Consequence when unrouted: the agent's own domain accumulates in a cluster it never
    sees, and dispatch invents de-facto domain codes for the orphan lane (7/16: BOTH
    `AI_CAPEX` and `AI_INFRA` appeared as `domain:` headers for the same lane, neither in
    the canonical vocabulary — the exact drift the Domain Vocabulary exists to prevent).

    MED, not HIGH: an unrouted agent is a real gap but not a data-integrity fault, and
    Tier-2/dormant agents are legitimately spawn-on-demand. Scoped to Tier-1 ACTIVE rows
    to avoid alarming on the dormant tail — a dormant agent nobody routes to is fine."""
    reg = _read(WALTER / "REGISTRY.tsv")
    # THE ROUTING CORPUS IS TWO FILES, NOT ONE (2026-08-30). The per-agent carve-outs
    # were split into design/ROUTING_CARVEOUTS.md to get ROUTING_TABLE.md under the read
    # cap (121,557 -> 31,764 B). They are ROUTING LAW, not commentary, so routing
    # PRESENCE must be evaluated over both — reading only the table made this check
    # report OZK and OTTO as UNROUTED within minutes of the split, when OZK is named
    # 5x and OTTO 1x in the carve-outs. A false MED, manufactured by the split itself.
    # ⇒ GENERALISABLE, and it bit twice in one session: A SPLIT RELOCATES CONTENT OUT
    # FROM UNDER EVERY INSTRUMENT THAT READS THE OLD PATH, and each instrument fails
    # independently — read_cap_check needed a CLAUDE.md rewording, this one needed code.
    # Sweep the consumers when you move a file; the checker that stays silent is the
    # dangerous one. [[finding_guard_correctness_and_wiring_are_independent]]
    parts = [_read(WALTER / "design/ROUTING_TABLE.md"),
             _read(WALTER / "design/ROUTING_CARVEOUTS.md")]
    if reg is None or parts[0] is None:
        return [(LOW, "REGISTRY.tsv or ROUTING_TABLE.md unreadable — routing coverage unchecked")]
    if parts[1] is None:
        return [(MED, "design/ROUTING_CARVEOUTS.md unreadable — half the routing corpus is "
                      "missing, so an UNROUTED verdict here would be unsafe. Fix the path, "
                      "do not interpret a clean run.")]
    rt = "\n".join(parts)
    # WALTER routes; PROME/Will/meta + reviewer agents are not routing targets.
    NON_TARGETS = {"WALTER", "PROME", "DAEDALUS", "YEYOU", "DEWEY", "WILL"}
    DORMANT = {"RETIRED", "DORMANT", "ARCHIVE", "GRAY", "GREY"}
    rows = [ln.split("\t") for ln in reg.strip().splitlines()[1:] if ln.strip()]
    unrouted, tier2 = [], []
    for r in rows:
        if len(r) < 9:
            continue
        agent, tier, status = r[0].strip(), r[1].strip(), r[8].strip().upper()
        if agent in NON_TARGETS or not agent:
            continue
        if any(d in status for d in DORMANT):
            continue
        # Presence = the agent is named anywhere in ROUTING_TABLE (a domain row's
        # Action/Backup/Info cell, or a carve sub-section). Deliberately permissive:
        # we are catching TOTAL absence, not auditing row quality.
        if re.search(rf"\b{re.escape(agent)}\b", rt):
            continue
        (unrouted if tier == "1" else tier2).append(agent)
    out = []
    if unrouted:
        out.append((MED, f"registered but UNROUTED — Tier-1 active, zero ROUTING_TABLE presence "
                         f"({len(unrouted)}): {', '.join(sorted(unrouted))} — nothing can route to "
                         f"them; their domain accumulates in a cluster they never see, and dispatch "
                         f"will invent de-facto domain codes. Add a domain code to FORMAT_SPEC "
                         f"(canonical) THEN a ROUTING_TABLE row; a REGISTRY row is not a routing row."))
    if tier2:
        out.append((LOW, f"Tier-2 registered but unrouted ({len(tier2)}): {', '.join(sorted(tier2))} "
                         f"— expected if spawn-on-demand; confirm it is intentional."))
    if not out:
        out.append((INFO, "every active registered agent has ROUTING_TABLE presence"))
    return out


def check_dewey_handoff_liveness():
    """DEWEY backstop-A liveness alarm (Will-approved 2026-07-19, PROME packet
    2026-07-19_from-PROME_dewey-routing-backstop-A). Under constrained-B, the main
    DEWEY session now delivers reports at write-time — create-only pointer stubs into
    each named recipient's inbox — and WALTER shifts from primary router to
    ledger/audit owner + backstop. WALTER's boot step 7d verifies each stub actually
    landed (delivering any DEWEY missed) and closes the DEEP_RESEARCH_FLAGGED_LOG row.

    This check is the liveness net (packet §3): a handoff sitting NEW in inbox/DEWEY/
    beyond ~1 day means the boot-step backstop hasn't run — i.e. the very
    latency/liveness gap the change exists to close is recurring. The per-recipient
    stub verification is the LIVE boot-step's job (step 7d); this is the mechanized
    alarm that a handoff went unprocessed. PROME's own boot scan of inbox/DEWEY/ is
    the final net. Same family as delivered_but_unconsumed / deep_research_pending."""
    d = WALTER / "inbox" / "DEWEY"
    if not d.is_dir():
        return [(INFO, "inbox/DEWEY/ absent — no DEWEY handoff lane")]
    skip = {"processed", "README.md", ".gitkeep", ".gitignore", ".DS_Store"}
    pending = [p for p in d.iterdir()
               if p.is_file() and p.name not in skip and not p.name.startswith(".")]
    if not pending:
        return [(INFO, "inbox/DEWEY/ clear — no unprocessed DEWEY handoffs")]
    out = []
    for p in sorted(pending):
        age = _age_days(dt.date.fromtimestamp(p.stat().st_mtime))
        if age > 1:
            out.append((MED, f"{p.name}: {age}d NEW — run boot step 7d: verify each "
                            f"recipient stub landed (deliver any DEWEY missed) + close the "
                            f"DEEP_RESEARCH_FLAGGED_LOG row + git-mv to processed/"))
        else:
            out.append((INFO, f"{p.name}: {age}d (fresh) — process at boot step 7d"))
    return out



def check_correction_target_declared():
    """FORMAT_SPEC v0.15: `signal_type: correction` REQUIRES a non-empty `corrects` field.

    Keyed on `signal_type`, NOT on `corrects` — deliberately, and this is the whole point.
    The 8/3 sweep first proposed keying on `corrects:` itself; running that showed 1 of 9
    corrections carried the field, so the check would have inspected 11% of the population
    and reported CLEAN forever. A completeness check keyed on the field whose ABSENCE is the
    defect selects for the complement of what it seeks. `signal_type` is what authors
    reliably write (9/9), so it is what we key on.

    Validates the three permitted value forms (SIG-ID list / SELF / EXTERNAL: <target>) and
    resolves every named SIG-ID against a real BOARD file — a corrects: pointing at a
    signal that does not exist is worse than an empty one, because it reads as provenance."""
    if not BOARD.exists():
        return [(LOW, "BOARD/ not found — correction-target check skipped")]
    missing, malformed, unresolved, ok = [], [], [], 0
    ids_on_board = {f.name.split("-2026")[0] for f in BOARD.glob("SIG-W-*.md")}
    ids_on_board = {m.group(0) for f in BOARD.glob("SIG-W-*.md")
                    if (m := re.match(r"SIG-W-\d{8}-\d{3}", f.name))}
    for f in sorted(BOARD.glob("SIG-W-*.md")):
        try:
            head = f.read_text(encoding="utf-8", errors="replace").split("\n---", 1)[0]
        except OSError:
            continue
        if not re.search(r"^signal_type:\s*correction\s*$", head, flags=re.M):
            continue
        sid = (re.search(r"^signal_id:\s*(\S+)", head, flags=re.M) or [None, f.name])[1]
        m = re.search(r"^corrects:\s*(.*)$", head, flags=re.M)
        if not m or not m.group(1).strip():
            missing.append(sid); continue
        val = m.group(1).strip()
        if val == "SELF" or val.startswith("EXTERNAL:"):
            if val.startswith("EXTERNAL:") and not val[len("EXTERNAL:"):].strip():
                malformed.append(f"{sid} (EXTERNAL: with no target)")
            else:
                ok += 1
            continue
        named = re.findall(r"SIG-W-\d{8}-\d{3}", val)
        if not named:
            malformed.append(f"{sid} (value is neither SIG-IDs, SELF, nor EXTERNAL:)"); continue
        dead = [n for n in named if n not in ids_on_board]
        if dead:
            unresolved.append(f"{sid} -> {', '.join(dead)}")
        else:
            ok += 1
    out = []
    if missing:
        out.append((MED, f"{len(missing)} correction signal(s) with NO `corrects:` "
                         f"(FORMAT_SPEC v0.15 requires it): {', '.join(missing)}"))
    if malformed:
        out.append((MED, f"{len(malformed)} malformed `corrects:` value(s): {', '.join(malformed)}"))
    if unresolved:
        out.append((HIGH, f"{len(unresolved)} `corrects:` naming a SIG-ID with no BOARD file "
                          f"— reads as provenance, resolves to nothing: {'; '.join(unresolved)}"))
    if not out:
        out.append((INFO, f"all {ok} correction signal(s) declare a resolvable target "
                          f"(SIG-ID / SELF / EXTERNAL)"))
    return out



def check_batch_manifest_open():
    """An OPEN batch manifest with un-dispositioned items, surfaced before closeout.

    Closes the ONE failure class every other check in this file is structurally blind to:
    all 24 others measure what was DISPATCHED, where it LANDED, and whether it COMMITTED.
    An INPUT that arrives and quietly never becomes anything is invisible to all of them
    (7/31: a 7-image Will batch, 6 processed, the highest-consequence item invisible ~2h
    and surfaced only because Will asked).

    ⚠️ RESIDUAL, stated because a green line here must NOT be read as "nothing was
    dropped": this can only see batches that were DECLARED. An undeclared batch is
    invisible by construction — the same shape as keying a check on the field whose
    absence is the defect. The INFO line says so explicitly rather than reading clean."""
    ledger = WALTER / "registry" / "BATCH_MANIFEST.tsv"
    if not ledger.exists():
        return [(INFO, "no batch manifest yet — NOTE: this cannot see an UNDECLARED batch; "
                       "green here is not evidence that no input was dropped")]
    try:
        lines = ledger.read_text(encoding="utf-8").splitlines()
    except OSError as e:
        return [(MED, f"BATCH_MANIFEST.tsv unreadable ({e})")]
    out, open_n = [], 0
    for i, line in enumerate(lines):
        if not line.strip() or line.startswith("#") or line.startswith("batch_id\t"):
            continue
        f = line.split("\t")
        if len(f) != 8:
            out.append((MED, f"BATCH_MANIFEST.tsv line {i+1}: {len(f)} fields, expected 8 "
                             f"— manifest unparseable, fix by hand"))
            continue
        bid, opened, source, declared, _disp, state, items, _notes = f
        if state != "OPEN":
            continue
        open_n += 1
        try:
            dn = int(declared)
        except ValueError:
            out.append((MED, f"{bid}: declared={declared!r} is not an integer")); continue
        got = set()
        for part in items.split(";"):
            if "=" in part:
                try:
                    got.add(int(part.split("=", 1)[0]))
                except ValueError:
                    pass
        missing = [n for n in range(1, dn + 1) if n not in got]
        age = ""
        try:
            d = dt.datetime.strptime(opened[:10], "%Y-%m-%d").date()
            age = f", opened {(TODAY - d).days}d ago"
        except ValueError:
            pass
        if missing:
            out.append((MED, f"{bid} OPEN with {len(missing)} of {dn} un-dispositioned: "
                             f"{missing} — {source[:60]}{age}. Every item needs a disposition "
                             f"INCLUDING NO-ACTION; run batch_manifest.py --close {bid}"))
        else:
            out.append((LOW, f"{bid} fully dispositioned ({dn}/{dn}) but still OPEN{age} "
                             f"— run --close {bid}"))
    if not out:
        out.append((INFO, "no OPEN batch manifests — NOTE: cannot see an UNDECLARED batch; "
                          "green here is not evidence that no input was dropped"))
    return out



# --- §3.5.4 ACTION-LINE RULE, mechanized (check #27, 2026-08-19, Will-approved) -------
# An ask directed at a named recipient belongs on `action:`, never on `info:` with the
# ask buried in the body. The rule is a SAFETY PRECONDITION for every pull-complete
# exemption (each rests on "never the ACTION owner => zero ACTION-miss risk", which is
# a claim about metadata accuracy), and until now it was enforced by discipline alone.
# It was violated 5x in 90 minutes on 2026-08-19 ("HOMER's call" in the body of
# -019/-020/-021/-022 while HOMER sat on info:) by the same session that correctly
# applied the TERRY gate five times running. That asymmetry is what a machine closes.
# [[finding_mechanize_the_cap_not_the_ritual]]

# Ask-language, not mere mention. A signal that REFERENCES an agent ("HAWK's framing is
# the one to carry") is not an ask; one that ASSIGNS ("HOMER calls it", "ASK to BRENT")
# is. Keyed on possessive/imperative/ownership constructions only -- a bare name match
# would fire on nearly every signal and become alert fatigue, which is the failure mode
# that kills a check faster than a false negative.
_ASK_PATTERNS = [
    # TUNED 2026-08-19 on OBSERVED false positives from the first run (7 flags / 106
    # signals / 14d), per the proposal's own commitment to tune on measurement rather
    # than a pre-guess. Three patterns were dropped and one narrowed:
    #   - "{a}'s ruling|decision|judgement"  -> DROPPED: matched a SOURCE CITATION
    #     ("read directly from ... PROME's ruling packet"), not an ask.
    #   - "{a} owns"                         -> DROPPED: it is how this desk states a
    #     DOMAIN ("RED owns the adversarial view", "VULCAN owns AI_INFRA_CAPEX"), not
    #     how it assigns one. 2 of 2 observed were false. "{a}-owned" is KEPT because
    #     that is registry language ("HOMER-OWNED").
    #   - lowercase "ask"                    -> NARROWED to the uppercase/arrow form
    #     this desk actually uses for asks; lowercase matched PAST-TENSE reporting of
    #     an already-answered ask ("WALTER asked whether ... belongs on BROCK's ...").
    r"{a}'s call\b",
    r"\b{a} (?:calls|rules|should|must|needs to|is asked|adjudicates|certifies|grades)\b",
    r"\b{a}[- ]OWNED\b",
    r"(?:ASK|\u21d2 ASK)[^.\n]{{0,80}}\b{a}\b",
    r"\b{a}\s*[:\u2014-]\s*(?:pull|read|confirm|check|open|rule|grade|verify|decide)",
    r"\brouted to {a}\b",
    r"\b(?:owned by|hands? (?:it )?to) {a}\b",
]


def check_action_line_rule():
    """§3.5.4: an ask aimed at a named recipient must be on `action:`, not `info:`.

    Scans BOARD signals dispatched in the trailing window and flags any agent that sits
    on the `info:` line while ask-language naming it appears in the body.

    ⚠️ RESIDUAL, stated so a green line is not over-read: this detects ASK-LANGUAGE, not
    asks. An ask phrased without any of the registered constructions is invisible here,
    and a legitimate mention that happens to match one will false-positive. It flags at
    LOW and never blocks -- the disposition stays human. Tune on OBSERVED false-positive
    rate, never on a pre-guess."""
    reg = WALTER / "REGISTRY.tsv"
    if not reg.exists():
        return [(MED, "REGISTRY.tsv missing -- cannot resolve agent names")]
    agents = []
    for i, line in enumerate(reg.read_text(encoding="utf-8").splitlines()):
        if i == 0 or not line.strip() or line.startswith("#"):
            continue
        name = line.split("\t")[0].strip()
        if name and name.isupper() and len(name) >= 3:
            agents.append(name)
    if not agents:
        return [(MED, "REGISTRY.tsv parsed to zero agent names")]

    cutoff = TODAY - dt.timedelta(days=ACTION_LINE_WINDOW_DAYS)
    out, scanned = [], 0
    for f in sorted(BOARD.glob("SIG-W-*.md")):
        m = re.match(r"SIG-W-(\d{4})(\d{2})(\d{2})-", f.name)
        if not m:
            continue
        try:
            d = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            continue
        if d < cutoff:
            continue
        try:
            txt = f.read_text(encoding="utf-8")
        except OSError:
            continue
        parts = txt.split("---", 2)
        if len(parts) < 3:
            continue
        fm, body = parts[1], parts[2]
        scanned += 1
        am = re.search(r"^action:\s*\[([^\]]*)\]", fm, re.M)
        im = re.search(r"^info:\s*\[([^\]]*)\]", fm, re.M)
        if not im:
            continue
        on_action = {x.strip() for x in (am.group(1).split(",") if am else []) if x.strip()}
        on_info = {x.strip() for x in im.group(1).split(",") if x.strip()}
        for a in sorted(on_info):
            if a not in agents or a in on_action:
                continue
            for pat in _ASK_PATTERNS:
                mm = re.search(pat.format(a=re.escape(a)), body)
                if mm:
                    frag = " ".join(mm.group(0).split())[:70]
                    out.append((LOW, f"{f.name[:34]}...: {a} is on `info:` but the body carries "
                                     f"ask-language -- \u201c{frag}\u201d. \u00a73.5.4 says an ask "
                                     f"aimed at a named recipient goes on `action:`. Verify, then "
                                     f"re-dispatch to {a} on action if it is a real ask."))
                    break
    if not out:
        return [(INFO, f"no \u00a73.5.4 candidates in {scanned} signal(s) over {ACTION_LINE_WINDOW_DAYS}d "
                       f"-- NOTE: detects ask-LANGUAGE, not asks; an ask phrased outside the "
                       f"registered constructions is invisible here")]
    out.append((INFO, f"scanned {scanned} signal(s) over {ACTION_LINE_WINDOW_DAYS}d"))
    return out



# ── 8/08 forum-carry builds (PROME packet, executed 2026-08-20, Will-directed) ──
TERRY_TOKEN_ADOPTED = "2026-08-20"   # rows before this graded by the legacy TERRY-OVERRIDE
                                     # prefix — a ruling governs the NEXT write, not disk
ENTITIES_ADOPTED = "2026-08-19"      # empirical full-coverage start (34/34 on 8/19);
                                     # mandate ratified FORMAT_SPEC v0.18, 2026-08-20
S7_TOKEN_ADOPTED = "2026-08-20"      # consume:<AGENT> grammar ships (SPEC v0.19 §5.1)


def _git(*args):
    """Run git in the repo root, return stdout (raises on failure)."""
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True,
                          text=True, check=True, timeout=30).stdout

def _delivery_rows():
    """Yield delivery_log rows as dicts keyed by header name. Field-count guarded."""
    path = WALTER / "routed/delivery_log.tsv"
    if not path.exists():
        return
    with path.open(errors="replace") as f:
        rdr = csv.reader(f, delimiter="\t")
        header = next(rdr, [])
        for row in rdr:
            if len(row) != len(header):
                continue
            yield dict(zip(header, row))


def check_terry_override_ratio():
    """S1 — the instrument that can revert TERRY's §3.5.5 routing rule (built 2026-08-20,
    8/08 forum-carry item 2, PROME-accepted inverted-token design).

    INVERTED TOKEN: every `action: TERRY` delivery_log row declares its qualifying test
    by BEGINNING its notes cell with `T-1` / `T-2` / `T-3` (closed vocabulary). Absence
    of a valid leading token IS an override by definition — typos OVER-report, so the
    clause fires early (over-firing costs a read; under-firing costs the guard).
    `TERRY-OVERRIDE` survives as the human-readable reason prefix, no longer load-bearing.
    Rows timestamped before TERRY_TOKEN_ADOPTED are graded by the legacy discriminator
    (TERRY-OVERRIDE prefix = override) — a new grammar must not manufacture violations
    out of rows written before it existed.

    TWO CLOCKS, DELIBERATELY UNHARMONISED (SPEC v0.16): the ratio clause is 90d /
    ratio ≤10% / activation n≥10; the revert FALSIFIER is an event test — ONE
    `action:` item unconsumed >72h, no denominator. Do not harmonise them.
    Violations name the recipient and the specific signals, never a bare count."""
    out = []
    now = dt.datetime.now(dt.timezone.utc)
    window_start = now - dt.timedelta(days=90)
    action_rows, overrides, falsifier = [], [], []
    for r in _delivery_rows():
        if r.get("recipient", "").strip().upper() != "TERRY":
            continue
        if r.get("role", "").strip().lower() != "action":
            continue
        ts_raw = r.get("timestamp_routed", "").strip()
        # 2026-08-26: legacy rows carry the desk's anti-false-precision minute stamps
        # ("...T20:1xZ"). fromisoformat throws on them and v1 SILENTLY SKIPPED the row —
        # the doctor printed "falsifier unfired" while the fired condition stood on disk.
        # Fallback: substitute '0' for the placeholder digit (event tests here run on a
        # 72h clock; sub-hour precision is immaterial). Never skip a TERRY action row.
        try:
            ts = dt.datetime.fromisoformat(ts_raw.replace("Z", "+00:00"))
        except ValueError:
            try:
                ts = dt.datetime.fromisoformat(
                    ts_raw.replace("x", "0").replace("X", "0").replace("Z", "+00:00"))
            except ValueError:
                continue
        notes = r.get("notes", "").strip()
        sig = r.get("signal_id", "?")
        # falsifier leg: an ACTION handoff still sitting in TERRY's inbox past 72h
        path = r.get("handoff_path", "").strip()
        if path and (REPO / path).exists() and (now - ts) > dt.timedelta(hours=72):
            falsifier.append((sig, round((now - ts).total_seconds() / 3600)))
        if ts < window_start:
            continue
        action_rows.append(sig)
        if ts.date().isoformat() >= TERRY_TOKEN_ADOPTED:
            qualifying = bool(re.match(r"T-[123]\b", notes))
        else:
            qualifying = not notes.upper().startswith("TERRY-OVERRIDE")
        if not qualifying:
            overrides.append(sig)
    # 2026-08-26: the falsifier FIRED (SIG-W-20260822-002-CORRECTION, ~78h) and the
    # revert was EXECUTED (SPEC v0.21: TERRY in PULL_COMPLETE, no new deliveries).
    # Non-renewable ⇒ post-revert this leg is a record, not an alarm: report INFO.
    for sig, hours in falsifier:
        out.append((INFO, f"S1 falsifier record: TERRY `action:` item {sig} unconsumed "
                          f"{hours}h (>72h) — falsifier FIRED 2026-08-26, revert to "
                          f"RED-class exemption EXECUTED (SPEC v0.21); residual handoff "
                          f"awaits TERRY's own consume, no action"))
    n = len(action_rows)
    if n >= 10 and overrides and len(overrides) / n > 0.10:
        # Post-revert (2026-08-26, SPEC v0.21) the TERRY action lane is CLOSED — no new
        # rows can be written, so the ratio measures a retired rule. The mandatory
        # read-the-log was performed at the revert (all three named rows adjudicated in
        # the 8/26 TERRY packet). Historical record, not an alarm.
        out.append((INFO, f"TERRY override ratio {len(overrides)}/{n} over the trailing "
                          f"90d window ({', '.join(overrides)}) — lane CLOSED by the "
                          f"§3.5.5 revert 2026-08-26; log read at revert; rolls off with "
                          f"the window"))
    if not out:
        out.append((INFO, f"TERRY lane clean: {n} action row(s) in 90d "
                          f"({len(overrides)} override(s), activation at n≥10), "
                          f"falsifier unfired"))
    return out


def check_filed_vs_consumed():
    """S7 — FILED ≠ CONSUMED made machine-readable (built 2026-08-20, 8/08 forum-carry
    item 3, SPEC v0.19 §5.1). A `git mv` into a processed/ dir is a CONSUMPTION record
    only when the moving commit DECLARES the consuming agent — a `consume:<AGENT>` token
    in the message, or a same-commit append to that dir's `.consumed.tsv`. An undeclared
    move is FILED: every agent commits as one git identity, so authorship cannot
    discriminate (commit 9be6a5ee6 filed six items into TERRY's processed/ that no TERRY
    surface cites). Moves before S7_TOKEN_ADOPTED predate the grammar and are counted as
    an upper bound only, never flagged."""
    out = []
    dirs = ["AGENTS/*/inbox/WALTER/processed", "AGENTS/WALTER/inbox/processed"]
    try:
        commits = _git("log", "--since=90.days", "--format=%H", "--", *dirs).split()
    except Exception as e:
        return [(LOW, f"git log for processed/ moves failed ({e}) — S7 unverifiable")]
    filed_new, filed_old, consumed = [], 0, 0
    for h in commits[:100]:
        try:
            meta = _git("log", "-1", "--format=%ct%x1f%B", h)
            names = _git("diff-tree", "-r", "-M", "--name-status", "--no-commit-id", h)
        except Exception:
            continue
        ct, _, msg = meta.partition("\x1f") if "\x1f" in meta else meta.partition("\u001f")
        # robust split: the unit separator arrives literally
        if "\x1f" not in meta:
            parts = meta.split(chr(31), 1)
            ct, msg = parts[0], (parts[1] if len(parts) > 1 else "")
        cdate = dt.datetime.fromtimestamp(int(ct), dt.timezone.utc).date().isoformat()
        touched = names.splitlines()
        tsv_owners = _consume_ledger_owners(touched)
        for line in touched:
            m = re.match(r"R\d+\t[^\t]+\t(.+)$", line)
            if not m:
                continue
            dest = m.group(1)
            om = re.match(r"AGENTS/([A-Z]+)/inbox/WALTER/processed/", dest) or \
                 re.match(r"AGENTS/(WALTER)/inbox/processed/", dest)
            if not om:
                continue
            owner = om.group(1)
            declared = bool(re.search(rf"consume:{owner}\b", msg, re.I)) or owner in tsv_owners
            if declared:
                consumed += 1
            elif cdate >= S7_TOKEN_ADOPTED:
                filed_new.append((owner, dest.rsplit("/", 1)[-1][:60], h[:9]))
            else:
                filed_old += 1
    for owner, fname, h in filed_new[:8]:
        out.append((LOW, f"FILED not CONSUMED: {fname} moved into {owner}'s processed/ "
                         f"({h}) with no consume:{owner} declaration — if a live {owner} "
                         f"session really consumed it, append to processed/.consumed.tsv"))
    if len(filed_new) > 8:
        out.append((LOW, f"...and {len(filed_new) - 8} more undeclared post-{S7_TOKEN_ADOPTED} moves"))
    if not out:
        out.append((INFO, f"processed/ moves in 90d: {consumed} declared-consumed, "
                          f"{filed_old} pre-grammar (upper bound only, not graded), "
                          f"0 undeclared since {S7_TOKEN_ADOPTED}"))
    return out


def check_entities_at_dispatch():
    """`entities:` mandatory at dispatch (built 2026-08-20, 8/08 forum-carry item 4,
    FORMAT_SPEC v0.18; thread-07 R5). Mandatory-at-dispatch reaches 100% in days where
    archive sweeps never do (the corrects: precedent) — so this scans ONLY signals dated
    on/after ENTITIES_ADOPTED and NEVER asks for retro-fill. Empirical baseline at
    adoption: 34/34 on 8/19, 4/4 on 8/20."""
    out, missing, scanned = [], [], 0
    for p in sorted(BOARD.glob("SIG-W-*.md")):
        m = re.match(r"SIG-W-(\d{4})(\d{2})(\d{2})-", p.name)
        if not m:
            continue
        sdate = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
        if sdate < ENTITIES_ADOPTED:
            continue
        scanned += 1
        head = p.read_text(errors="replace")[:4000]
        if not re.search(r"^entities:", head, re.M):
            missing.append(p.name[:40])
    for name in missing[:6]:
        out.append((LOW, f"{name}...: no `entities:` header on a post-{ENTITIES_ADOPTED} "
                         f"signal — mandatory at dispatch per FORMAT_SPEC v0.18"))
    if not out:
        out.append((INFO, f"all {scanned} signal(s) since {ENTITIES_ADOPTED} declare `entities:`"))
    return out



def check_auto_load_budget():
    """THE COST NO READ-CAP INSTRUMENT WAS MEASURING (added 2026-08-30).

    scripts/read_cap_check.py enumerates the files a BOOT STEP names — it opens
    CLAUDE.md to find those 'read X' lines and never weighs CLAUDE.md itself. But
    CLAUDE.md is loaded UNCONDITIONALLY, on every session, before boot step 0 runs:
    it is the one read no branch can avoid, and it was the largest single surface on
    the desk (75,296 B = 139% of the cap) while every read-cap report said nothing.

    ⇒ The perimeter of a budget check is a CHOICE, and anything outside it is not
    'compliant', it is UNMEASURED. A file can be the biggest cost on the desk and
    absent from the report that ranks costs. [[finding_instrument_reports_clean_against_the_wrong_reference]]

    SCOPE — only AGENTS/WALTER/CLAUDE.md is WALTER's to fix. Root CLAUDE.md and the
    fleet auto-memory index are PROME-owned; they are REPORTED (they are real cost on
    every WALTER session) but never graded against WALTER, per the flag-don't-commit rule."""
    cap, budget = 54_250, 32_550
    own = WALTER / "CLAUDE.md"
    others = [(REPO / "CLAUDE.md", "root CLAUDE.md (PROME-owned)"),
              (Path.home() / ".claude/projects/-home-willi-Research-workspace/memory/MEMORY.md",
               "fleet auto-memory index (PROME-owned)")]
    try:
        n = own.stat().st_size
    except OSError:
        return [(LOW, "AGENTS/WALTER/CLAUDE.md unreadable — auto-load cost UNMEASURED, not clean")]
    parts, total = [], n
    for p, label in others:
        try:
            b = p.stat().st_size
            total += b
            parts.append(f"{label} {b:,} B")
        except OSError:
            parts.append(f"{label} unreadable")
    detail = (f"WALTER CLAUDE.md {n:,} B = {n*100//cap}% of the {cap:,} B cap "
              f"({n*100//budget}% of budget) · unconditional total with "
              f"{' + '.join(parts)} = {total:,} B = {total*100//cap}% of cap")
    if n > cap:
        return [(MED, f"AUTO-LOAD OVER THE CAP — {detail}. This loads on EVERY session before "
                      f"boot step 0 and no read-cap run will show it. Move incident history to "
                      f"design/BOOT_PROTOCOL.md; keep action/condition/failure/pointer.")]
    if n > budget:
        return [(LOW, f"auto-load over budget (under cap) — {detail}")]
    return [(INFO, f"auto-load within budget — {detail}")]


def _processed_owner(path: str):
    """The desk that OWNS a `.../processed/...` path, or None if it is not one."""
    m = (re.match(r"AGENTS/([A-Z]+)/inbox/WALTER/processed/", path) or
         re.match(r"AGENTS/(WALTER)/inbox/processed/", path))
    return m.group(1) if m else None


def _consume_ledger_owners(touched):
    """Owners whose OWN `processed/.consumed.tsv` this commit added-or-modified.

    🔴 ADDED 2026-09-05 (Codex finding 3). The caller previously computed a single
    commit-wide boolean — `any(... processed/.consumed.tsv ...)` over every touched
    path — so a commit that filed a packet into ALPHA's processed/ while appending
    only BETA's ledger counted as a DECLARED consumption FOR ALPHA. BOARD_CONSUMPTION_SPEC
    §432 requires the CONSUMING OWNER's declaration; a receipt written by another desk
    certifies nothing about this one. Extracted to module level so the regression case
    can call it directly. `[[finding_instrument_reports_clean_against_the_wrong_reference]]`
    """
    owners = set()
    for line in touched:
        m = re.match(r"[AM]\t(.+/processed/\.consumed\.tsv)$", line)
        if not m:
            continue
        owner = _processed_owner(m.group(1))
        if owner:
            owners.add(owner)
    return owners


def check_index_generated_fresh():
    """WQ-174 leg 3 (Will "174 - approved" 2026-09-04): BOARD/INDEX.md is a GENERATED projection of
    signal frontmatter. This check regenerates the row-set in memory at every doctor run and
    compares its sha256 to the banner the live file carries — a hand edit, a new signal not yet
    regenerated, or a header change on any signal makes the live file STALE and that is HIGH,
    because a stale generated index is a false certification (the same class as the
    FALSIFICATION_TRIGGERS_SCAN banner-sha rule at boot 6b).

    PRE-CUTOVER (live file has no `rowset_sha256=` banner): runs the generator's --check logic
    read-only and reports LOW on any FAIL (a new hand-only marker, an ID/count mismatch) so the
    soak is measured every day rather than remembered; INFO on PASS. Never writes.
    """
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("gen_board_index", HERE / "gen_board_index.py")
        gbi = importlib.util.module_from_spec(spec); spec.loader.exec_module(gbi)
    except Exception as e:
        return [(MED, f"gen_board_index.py could not be imported ({type(e).__name__}: {e}) — index freshness unchecked")]
    live = (BOARD / "INDEX.md").read_text(errors="replace")
    m = re.search(r"rowset_sha256=([0-9a-f]{64})", live)
    sigs, errors = gbi.load_signals()
    if not m:
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = gbi.check(sigs, errors)
        tail = [l for l in buf.getvalue().splitlines() if l.startswith(("markers:", "ID SET", "COUNT", "SECTION", "TOTAL", "HARD"))]
        if rc:
            return [(LOW, "PRE-CUTOVER soak: gen_board_index --check FAILS vs the hand-maintained INDEX — " + " | ".join(tail)[:400])]
        return [(INFO, "PRE-CUTOVER soak: gen_board_index --check PASS vs the hand-maintained INDEX (cutover target 2026-09-08) — " + " | ".join(tail)[:300])]
    if errors:
        return [(HIGH, f"generated INDEX cannot be re-derived: {len(errors)} signal(s) fail closed — {errors[0]}")]
    _, sha = gbi.render(sigs, live)
    if sha != m.group(1):
        return [(HIGH, f"BOARD/INDEX.md is STALE vs the signal set (banner {m.group(1)[:12]} ≠ current {sha[:12]}) — run `gen_board_index.py --write BOARD/INDEX.md --cutover` and commit; never hand-edit the index")]
    # 🔴 ADDED 2026-09-05 (Codex finding 4). The banner comparison above proves only that
    # the SIGNALS still hash to what the banner claims — BOTH SIDES are derived from the
    # signal files, and NEITHER reads the rows actually sitting in the live index. A hand
    # edit to a row (a changed recipient, a moved precedence) left the banner untouched and
    # this check reported "generated INDEX fresh". A stored hash is not proof that the
    # content beneath it is intact: hash what is THERE, not what SHOULD be there.
    # `[[finding_instrument_reports_clean_against_the_wrong_reference]]`
    marks = gbi.derive_markers(sigs)
    want = sorted(gbi.render_row(sg, marks) for sg in sigs.values())
    have = sorted(l.rstrip() for l in live.splitlines() if l.startswith("| SIG-W-"))
    if have != want:
        ws, hs = set(want), set(have)
        drifted = sorted(hs - ws)[:3]
        missing = len(ws - hs)
        return [(HIGH, f"BOARD/INDEX.md ROWS have DRIFTED from the generated projection while the "
                       f"banner still matches the signal set — i.e. the index was hand-edited under "
                       f"an intact banner ({len(hs - ws)} row(s) present that the generator would not "
                       f"produce, {missing} row(s) it would produce that are absent). "
                       f"First drifted: {drifted[0][:160] if drifted else '(none — rows missing only)'} "
                       f"⇒ regenerate with `gen_board_index.py --write BOARD/INDEX.md --cutover`; never hand-edit.")]
    return [(INFO, f"generated INDEX fresh (rowset {sha[:12]}, {len(sigs)} signals; "
                   f"{len(have)} live rows hashed and matched — banner AND content)")]

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
    ("registry_self_lag", check_registry_self_lag),
    ("liaison_enum", check_liaison_enum),
    ("delivered_but_unconsumed", check_delivered_but_unconsumed),
    ("written_but_undelivered", check_written_but_undelivered),
    ("delivery_claim_vs_git", check_delivery_claim_vs_git),
    ("deep_research_pending_overdue", check_deep_research_pending_overdue),
    ("dewey_handoff_liveness", check_dewey_handoff_liveness),
    ("staleness_sweep_overdue", check_staleness_sweep_overdue),
    ("dropzone_pending", check_dropzone_pending),
    ("boot_protocol_xref", check_boot_protocol_xref),
    ("status_spine_overflow", check_status_spine_overflow),
    ("cluster_review_overdue", check_cluster_review_overdue),
    ("registered_but_unrouted", check_registered_but_unrouted),
    ("correction_target_declared", check_correction_target_declared),
    ("batch_manifest_open", check_batch_manifest_open),
    ("action_line_rule", check_action_line_rule),
    ("terry_override_ratio", check_terry_override_ratio),
    ("filed_vs_consumed", check_filed_vs_consumed),
    ("entities_at_dispatch", check_entities_at_dispatch),
    ("auto_load_budget", check_auto_load_budget),
    ("index_generated_fresh", check_index_generated_fresh),
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
