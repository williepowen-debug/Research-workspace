#!/usr/bin/env python3
"""
DAEDALUS maturity scanner — objective L0-L2 floor + structural signals for L3-L5.

Read-only. Computes the deterministic, rerunnable layer of the fleet maturity map
(SPEC.md §5). It does NOT make quality judgments — it reports presence/shape/recency
signals; DAEDALUS (the agent) judges the L3-L5 ceiling from these.

PAT-020 (2026-06-28) — PATH-BLINDNESS FIX. The first version looked for TRADE.md /
KB / PREDICTIONS at FIXED paths and missed agents that NEST them (BROCK keeps its book
at trade/TRADE.md, its resolved predictions in workbook/PREDICTIONS_ARCHIVE.tsv) —
under-rating BROCK a full level. Two guards now:
  (1) Artifact detection is RECURSIVE over the agent tree, excluding archive/sources/
      inbox/outbox/processed (live artifacts only).
  (2) Every L3+ mechanical hint is emitted as PROVISIONAL (⚠needs-read) — the script is
      a floor+flag generator; own-titled / nested discipline (PAT-009) means an L3+ grade
      is NEVER final until DAEDALUS reads the agent.

Usage:
    python3 AGENTS/DAEDALUS/scripts/maturity_scan.py            # markdown table to stdout
    python3 AGENTS/DAEDALUS/scripts/maturity_scan.py --tsv      # tsv (FLEET_MAP signal rows)

Staleness is measured in commits-behind-HEAD-date (robust to wall-clock skew), not
against the system clock.
"""
import os, re, subprocess, sys

REPO = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                      capture_output=True, text=True).stdout.strip()
if not REPO:
    sys.exit("🔴 maturity_scan CANNOT-CERTIFY: git rev-parse failed (git unavailable or not a repo) — "
             "cannot locate the tree; refusing to grade from a wrong root")
AGENTS = os.path.join(REPO, "AGENTS")

# Class map from PROME/ROSTER.md (active+tier2+dormant). Default = Market.
# DAEDALUS references ROSTER for active/dormant; class here is design-class only.
CLASS = {
    "DAEDALUS": "Meta",  # PROME lives at repo-root PROME/, outside agent_dirs()' walk
    "WALTER": "Utility", "NEXUS": "Utility", "TERRY": "Utility", "ORACLE": "Utility",
    "RED": "Utility", "YEYOU": "Utility", "DEWEY": "Utility",
    # everything else market-domain. HERMES removed 2026-07-22 (dir retired).
}
# Dirs that are not live agents (archives, sources, scaffolds).
# REGISTRATION RULE (self-sweep 7/22, H2): a REVIVAL must remove the name from this set
# same-pass as the FLEET_MAP row — the renderer fails loud on mismatches, this fails SILENT
# (OZK/ZHAO sat here months after reviving; see builds/REGISTRATION_CHECKLIST.md row 12).
SKIP = {"ATHENA", "BARON", "CRUISE", "REITS", "TRADES", "SENTRY"}
# FERT removed 2026-08-16 (re-chartered ACTIVE, Will-ruled — registration rule above:
# revival removes the name same-pass as the FLEET_MAP row). CRUISE stays pending PROME's
# re-classification call (flagged 8/16, orphaned-threshold sweep — de-facto active).

# LIVE agents the objective floor layer CANNOT measure — excluded from grading but ANNOUNCED,
# never silently dropped. Distinct from SKIP: SKIP = not an agent; this = an agent this
# instrument is the wrong instrument for. Keying these into SKIP would repeat the OZK/ZHAO
# fail-silent class on a *live* agent, which is strictly worse (PAT-074: a null result must
# say what it did not look at). Grade these by judgment read + FLEET_MAP row only.
JUDGMENT_ONLY = {
    "RAV": "Codex/Will-driven — no repo CLAUDE.md or STATUS.md BY DESIGN (handed its context, "
           "does not boot from the tree). Spec = DAEDALUS/builds/RAV_CHARTER.md; floor L0-L2 "
           "is undefined for it, so a scanned 'L0' would be a false gap, not a finding.",
}

# Subtrees that are NOT live artifacts — pruned from recursive artifact detection (PAT-020).
EXCLUDE_DIRS = {"archive", "_archive", "sources", "processed", "delivered",
                "inbox", "outbox", ".git", "node_modules"}

def sh(args):
    # §9-style guard (2026-08-17 self-audit C5): a failed git call previously returned "",
    # zeroing HEAD_EPOCH/commits_30d and silently collapsing every agent to L2 — a full-fleet
    # under-grade with no marker. Fail CANNOT-CERTIFY instead; a wrong map is worse than none.
    p = subprocess.run(args, capture_output=True, text=True, cwd=REPO)
    if p.returncode != 0:
        sys.exit(f"🔴 maturity_scan CANNOT-CERTIFY: {' '.join(args)} failed rc={p.returncode} — "
                 f"without git data every agent would silently under-grade to L2. "
                 f"stderr: {(p.stderr or '').strip()[:200]}")
    return p.stdout

def head_commit_epoch():
    epoch = int(sh(["git", "log", "-1", "--format=%ct"]).strip() or 0)
    if not epoch:
        sys.exit("🔴 maturity_scan CANNOT-CERTIFY: HEAD epoch unreadable (empty git log output)")
    return epoch

HEAD_EPOCH = head_commit_epoch()

def agent_dirs():
    out = []
    for name in sorted(os.listdir(AGENTS)):
        p = os.path.join(AGENTS, name)
        if not os.path.isdir(p) or name.startswith("_") or name == "templates":
            continue
        if not (os.path.exists(os.path.join(p, "CLAUDE.md")) or
                os.path.exists(os.path.join(p, "STATUS.md"))):
            continue
        out.append(name)
    return out

def read(path):
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            return f.read()
    except (FileNotFoundError, IsADirectoryError):
        return None

def tsv_rows(path):
    txt = read(path)
    if not txt:
        return 0
    return max(0, len([l for l in txt.splitlines() if l.strip() and not l.startswith("#")]) - 1)

# PAT-031 — cwd-proof boot invocations. A *runnable* boot command that uses a bare
# root-relative or own-dir-relative path (`python3 scripts/x.py`, `bash scripts/x.sh`,
# `node tools/y.js`, `./scripts/x.py`) depends on the incidental shell cwd and fails rc=2
# from the `cd AGENTS/<NAME> && claude` launch dir. The self-locating idiom
# (`"$(git rev-parse --show-toplevel)/…"`) fixes it.
#
# DETECTION (per-line): an interpreter + a relative path ending in a script extension, OR a
# direct `./relative/path.ext` execution — EXCLUDING any line carrying `rev-parse` (already
# self-locating) and absolute / `$var` / quoted paths. Widened 2026-07-03 (PROME flag 1) from
# python3-only to python/bash/sh/node/npx/ruby/perl + `./` + .py/.sh/.js/.mjs/.ts/.rb/.pl so a
# future non-Python build can't slip through. KNOWN UNCAUGHT: `python3 -m module.name`
# (module-resolution, not a path — flagging it would FP on stdlib `-m pip`/`-m venv`); accepted.
#
# AGENT-LEVEL heuristic ON PURPOSE (not line-level): the gap is only reported when the doc
# shows ZERO idiom-awareness anywhere (no `rev-parse`). So an idiom-unaware NEW build trips it,
# while a swept agent whose *reference* command docs stay bare under a section cwd-note (e.g.
# ORACLE) is correctly suppressed — a line-level check would re-flag those, and a check that
# cries wolf gets ignored.
#
# ACCEPTED RESIDUAL (PROME flag 2, 2026-07-03): this is a NEW-BUILD guard, NOT a regression
# guard — a bare line ADDED to an already-idiom-aware doc is not caught here. Accepted
# deliberately: the real regression guard is FAIL-LOUD-AT-BOOT (the invocation dies rc=2 at
# that agent's next boot — exactly how BRENT's Jul-1 break surfaced), which is fast, local, and
# self-evident. The scanner covers the one case fail-loud can't (a build that copies a bare
# pattern before it ever boots clean); regressions stay with boot-time failure + human review.
# Reintroducing line-level to close this residual would resurrect the ORACLE FP — worse.
_INTERP = r"(?:python3?|bash|sh|node|npx|ruby|perl)"
_EXT = r"(?:py|sh|js|mjs|ts|rb|pl)"
BARE_BOOT_RE = re.compile(
    rf"(?:{_INTERP}\s+(?:\./)?|(?<![\w$/'\"])\./)"
    rf"[\w.-]+(?:/[\w.-]+)*\.{_EXT}\b"
)

def bare_boot_calls(claude):
    """Runnable bare (cwd-dependent) boot invocations lacking the self-locating idiom (PAT-031)."""
    if not claude:
        return 0
    return sum(1 for ln in claude.splitlines()
               if BARE_BOOT_RE.search(ln) and "rev-parse" not in ln)

def find_live(root, filename):
    """All paths to `filename` under root, EXCLUDING archive/sources/inbox/etc (PAT-020).
    Live artifacts only — a TRADE.md in archive/ does not count as a live trade surface."""
    hits = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [dn for dn in dirnames
                       if dn not in EXCLUDE_DIRS and not dn.startswith("tmp")]
        if filename in filenames:
            hits.append(os.path.join(dirpath, filename))
    return hits

def has_live_dir(root, dirname):
    for dirpath, dirnames, _ in os.walk(root):
        dirnames[:] = [dn for dn in dirnames
                       if dn not in EXCLUDE_DIRS and not dn.startswith("tmp")]
        if dirname in dirnames:
            return True
    return False

def discipline_corpus(d):
    """Where falsification/convergence rails legitimately live: STATUS + thesis/*.md +
    EXPECTED_SIGNALS.md (PAT-009 broadening — rails homes, not intent-description files).
    Deliberately EXCLUDES CLAUDE.md to avoid matching instruction-language as substance."""
    parts = []
    for rel in ("STATUS.md", "EXPECTED_SIGNALS.md"):
        t = read(os.path.join(d, rel))
        if t:
            parts.append(t)
    thesis = os.path.join(d, "thesis")
    if os.path.isdir(thesis):
        for f in sorted(os.listdir(thesis)):
            if f.endswith(".md"):
                t = read(os.path.join(thesis, f))
                if t:
                    parts.append(t)
    return "\n".join(parts)

def scan(name):
    d = os.path.join(AGENTS, name)
    cls = CLASS.get(name, "Market")
    claude = read(os.path.join(d, "CLAUDE.md"))
    status = read(os.path.join(d, "STATUS.md"))
    s = status or ""
    corpus = discipline_corpus(d)

    # --- recursive artifact detection (PAT-020) ---
    kb_paths = find_live(d, "KB.tsv")
    pred_paths = find_live(d, "PREDICTIONS.tsv")
    pred_arch_paths = find_live(d, "PREDICTIONS_ARCHIVE.tsv")
    trade_paths = find_live(d, "TRADE.md")
    # resolved predictions live in the live ledger AND/OR the archive (OTTO pattern)
    resolved_txt = "".join((read(p) or "") for p in pred_paths + pred_arch_paths)
    pred_resolved = len(re.findall(
        r"\b(CONFIRMED|FAILED|PARTIAL|PARTIALLY|EXPIRED|HIT|MISS|RESOLVED|FALSIFIED)\b",
        resolved_txt))
    has_scoreboard = bool(find_live(d, "PREDICTIONS_SCOREBOARD.md"))

    sig = {
        "agent": name, "class": cls,
        "has_claude": claude is not None,
        "has_status": status is not None,
        "status_lines": len(s.splitlines()) if status else 0,
        "bottom_line": bool(re.search(r"BOTTOM LINE", s, re.I)),          # STATUS-only (required there)
        "convergence": bool(re.search(r"convergence matrix", corpus, re.I)),
        "exit_rules": bool(re.search(r"\b(exit|falsif|invalidat|counter-signal)", corpus, re.I)),
        "session_counts": bool(re.search(r"\b\d+\+?\s*(?:consecutive\s+)?(?:sessions?|prints?|months?)\b", corpus, re.I)),
        "has_workbook": has_live_dir(d, "workbook") or bool(kb_paths),
        "tsv_records": sum(tsv_rows(os.path.join(d, f)) for f in os.listdir(d)
                           if f.endswith(".tsv")) if os.path.isdir(d) else 0,
        "kb_rows": sum(tsv_rows(p) for p in kb_paths),
        "pred_rows": sum(tsv_rows(p) for p in pred_paths),
        "pred_resolved": pred_resolved + (1 if has_scoreboard and pred_resolved == 0 else 0),
        "has_scoreboard": has_scoreboard,
        "has_trade": bool(trade_paths),
        "trade_path": (os.path.relpath(trade_paths[0], d) if trade_paths else "-"),
        "days_behind": days_behind_head(name),
        "commits_30d": commits_30d(name),
        "bare_boot_calls": bare_boot_calls(claude),                # PAT-031
        "idiom_aware": bool(claude and "rev-parse" in claude),     # PAT-031 (agent-level gate)
    }
    sig["floor"] = floor_level(sig)
    sig["gaps"] = conformance_gaps(sig)
    sig["proposed"] = proposed_level(sig)
    sig["provisional"] = sig["proposed"].endswith("?")   # any L3+ hint is read-pending (PAT-020)
    return sig

def days_behind_head(name):
    ts = sh(["git", "log", "-1", "--format=%ct", "--", f"AGENTS/{name}"]).strip()
    if not ts:
        return None
    return round((HEAD_EPOCH - int(ts)) / 86400, 1)

def commits_30d(name):
    since = HEAD_EPOCH - 30 * 86400
    log = sh(["git", "log", f"--since={since}", "--format=%h", "--", f"AGENTS/{name}"])
    return len([l for l in log.splitlines() if l.strip()])

def floor_level(s):
    """Objective L0-L2 — class-independent STRUCTURAL PRESENCE (not conformance).
    Missing-a-required-section is a gap, NOT a demotion to skeleton (PAT-007)."""
    if not s["has_claude"]:
        return "—"
    if not s["has_status"] or s["status_lines"] < 15:
        return "L0"  # skeleton: no real live state
    # market record = workbook/KB; meta/utility record = any populated top-level .tsv (class-aware, PAT-008)
    has_record = s["kb_rows"] > 0 or s["has_workbook"] or s["tsv_records"] > 0
    if has_record:
        return "L2"
    return "L1"

def conformance_gaps(s):
    """Required-section / discipline gaps — debt flags, independent of level."""
    g = []
    if s["has_status"] and not s["bottom_line"]:
        g.append("no BOTTOM LINE")
    if s["status_lines"] > 260:
        g.append(f"STATUS {s['status_lines']}ln >cap")
    # PAT-031 — cwd-proof boot invocations (class-independent; agent-level, see bare_boot_calls)
    if s["bare_boot_calls"] > 0 and not s["idiom_aware"]:
        g.append(f"{s['bare_boot_calls']} bare boot invocation(s) not cwd-proof (PAT-031)")
    if s["class"] == "Market":
        if not s["convergence"]:
            g.append("no conv-matrix")
        if not s["exit_rules"]:
            g.append("no exit-rules")
        elif not s["session_counts"]:
            g.append("exit-rules lack session counts")
        if s["pred_rows"] > 0 and s["pred_resolved"] == 0:
            g.append("predictions unresolved")
    return "; ".join(g) or "—"

def proposed_level(s):
    """Mechanical hint toward L3-L5 from structural markers. ALWAYS provisional for L3+
    (trailing '?') — DAEDALUS finalizes by reading (PAT-009/PAT-020)."""
    base = s["floor"]
    if base not in ("L2",):
        return base
    fresh = (s["commits_30d"] or 0) >= 8
    if s["class"] == "Market":
        l3 = s["convergence"] and s["exit_rules"] and s["pred_resolved"] > 0
        l4 = l3 and s["has_trade"] and fresh
        return "L4?" if l4 else ("L3?" if l3 else "L2")
    if s["class"] in ("Utility", "Meta"):
        l3 = s["bottom_line"] and fresh
        l4 = l3 and (s["commits_30d"] or 0) >= 15
        return "L4?" if l4 else ("L3?" if l3 else "L2")
    return base

def main():
    rows = [scan(n) for n in agent_dirs() if n not in SKIP and n not in JUDGMENT_ONLY]
    rows.sort(key=lambda r: (r["class"], -(r["commits_30d"] or 0)))
    # Announce what was deliberately NOT graded (PAT-074) — in BOTH output modes.
    # ⚠️ Enumerate from the FILESYSTEM, not agent_dirs(): that helper requires a CLAUDE.md or
    # STATUS.md (:75-77), which is exactly what a JUDGMENT_ONLY agent lacks — so sourcing this
    # list from agent_dirs() makes the announcement dead code that prints nothing and reads as
    # "nothing to announce." Found by RUNNING it at RAV's registration, 8/03 (PAT-074 inward,
    # same shape as the WATT/MIDAS/VULCAN boot.py rc-blindness fixed 7/31).
    excluded = sorted(n for n in JUDGMENT_ONLY
                      if os.path.isdir(os.path.join(AGENTS, n)))
    if "--tsv" in sys.argv:
        print("Agent\tClass\tFloor\tProposed\tNeedsRead\tStatusLines\tKB\tPredResolved\tTrade\tTradePath\tDaysBehind\tCommits30d")
        for r in rows:
            print(f"{r['agent']}\t{r['class']}\t{r['floor']}\t{r['proposed']}"
                  f"\t{'Y' if r['provisional'] else '-'}\t{r['status_lines']}"
                  f"\t{r['kb_rows']}\t{r['pred_resolved']}\t{'Y' if r['has_trade'] else '-'}"
                  f"\t{r['trade_path']}\t{r['days_behind']}\t{r['commits_30d']}")
        for name in excluded:
            print(f"{name}\t-\tNOT-GRADED\tjudgment-only\t-\t-\t-\t-\t-\t-\t-\t-")
        return
    print(f"# Fleet maturity scan (objective layer) — {len(rows)} agents · HEAD-relative staleness\n")
    print("| Agent | Class | Floor | →L3-5? | 30d | Conformance gaps |")
    print("|---|---|---|---|---:|---|")
    for r in rows:
        prop = r["proposed"] + (" ⚠needs-read" if r["provisional"] else "")
        print(f"| {r['agent']} | {r['class']} | {r['floor']} | {prop} "
              f"| {r['commits_30d']} | {r['gaps']} |")
    for name in excluded:
        print(f"| {name} | — | **NOT GRADED** | judgment-only | — | {JUDGMENT_ONLY[name]} |")
    print("\n_Floor = objective structural presence (L0 skeleton · L1 live STATUS · L2 +structured record). "
          "→L3-5? = mechanical hint; **every L3+ is PROVISIONAL (⚠needs-read) until DAEDALUS reads the agent** "
          "(PAT-009/PAT-020). Artifact detection is recursive (live subtrees only). "
          "Gaps = conformance debt, independent of level._")

if __name__ == "__main__":
    main()
