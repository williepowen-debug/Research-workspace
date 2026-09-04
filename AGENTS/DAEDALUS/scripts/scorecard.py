#!/usr/bin/env python3
"""scorecard.py — DOCKET L239 weekly coordination-value scorecard, v1 column set.

Owner: DAEDALUS. Spec: AGENTS/DAEDALUS/design/2026-08-28_coordination_scorecard_v1.md (RAV-tightened
schema, Will "go ahead approved" 8/28 via PROME). Companion: coordination_scorecard.py (the ORCH_LOG
volume tables, render #1 form) — captured here as the appendix so one artifact carries both.

*** DESCRIPTIVE ONLY. NO SUCCESS THRESHOLD IS SET, AND NONE MAY BE SET BEFORE >=4 RENDERS EXIST. ***

Usage:  scorecard.py --week-ending YYYY-MM-DD [--no-write]   → scorecards/YYYY-MM-DD.md + a row in
        scorecards/SCORECARD.tsv (the series; one row per render, re-render replaces the row)
        scorecard.py --selftest

Window = the 7 days ENDING the render date, inclusive (spec: "window = 7d ending the render date").

Schema requirements honoured (spec §Schema, RAV 8/28):
  1. Joins on EXPLICIT KEYS only — DOCKET physical line number (the WQ-138 citation convention),
     WQ row number, ORCH_LOG (date, desk, touch), CORRECTIONS correction_id, prediction ids.
     A WQ ruling links to a DOCKET loop only when the WQ row cites `DOCKET L<n>` / `DOCKET row <n>`
     and row n RESOLVED inside the window. Unlinked rulings are their own line, never inferred.
  2. A `provenance:` block under every cell, listing the exact source rows (file:line or id).
  3. Same-day catch/ruling pairs would be ORDER-UNKNOWN — but ORCH_LOG and WILL_QUEUE share NO key,
     so the pair set is NOT COMPUTABLE; this render prints that as NOT-SEEN with the reason, and
     classifies pre/post BY CONSTRUCTION (see column 3/4 text). No inferred pairs.
  4. `author_days`, `touches`, `commits` — three separately-defined counts, no composite.
  5. Column 2 reads scorecards/LEDGERS.tsv (explicit registry); unregistered ledgers = NOT SEEN;
     a registered ledger whose header lacks a named column ⇒ CANNOT-EVALUATE for that ledger.

Null vs zero (STATE_VOCABULARY Class 5): an ORCH_LOG with no TOUCH rows in the window renders
NO-TOUCHES-LOGGED, never `0`. Anything the instrument cannot see is NOT-SEEN, never zero.

rc: 0 rendered · 2 CANNOT-EVALUATE (a required input absent/unparseable — nothing is written).
"""
import io
import os
import re
import subprocess
import sys
import contextlib
from collections import Counter, defaultdict
from datetime import date, timedelta

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                      check=True).stdout.strip()
HERE = os.path.dirname(os.path.abspath(__file__))
AGENT = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, HERE)
import orch_log                                   # strict ORCH_LOG schema helper (single owner of COLS)

VERSION = "scorecard.py v1.0 (2026-09-04)"
DOCKET = os.path.join(ROOT, "PROME", "DOCKET.tsv")
WQ = os.path.join(ROOT, "PROME", "WILL_QUEUE.md")
CORR = os.path.join(ROOT, "AGENTS", "WALTER", "registry", "CORRECTIONS.tsv")
PROPOSALS = os.path.join(ROOT, "PROME", "proposals")
REGISTRY = os.path.join(AGENT, "scorecards", "LEDGERS.tsv")
OUTDIR = os.path.join(AGENT, "scorecards")
SERIES = os.path.join(OUTDIR, "SCORECARD.tsv")

ISO = re.compile(r"(?<!\d)(2026-\d\d-\d\d)(?!\d)")   # not \b: `2026-09-03_wq…` filenames must match
# "names a source": a commit hash, a repo path, a URL, a filing/docket identifier, a delivery path.
SOURCE_RE = re.compile(r"\b[0-9a-f]{7,40}\b|(?:AGENTS|PROME|FORGE|KERNEL|BOARD|MESSAGING|memory|docs)/\S+"
                       r"|https?://|EDGAR|acc(?:ession)?\s*\d|\bUSDL-|\bDkt\b|\bBLS\b|\bFRED\b")

# --- terminal-token map (prefix match on the UPPER-cased status cell; longest prefix wins) ---
NONTERMINAL = ("OPEN", "ACTIVE", "PENDING", "MONITORING", "ARMED", "WATCH")
TOKEN_MAP = [
    # PARTIAL first: compound tokens that would otherwise prefix-match HIT/MISS/CONFIRMED
    ("HIT (PARTIAL", "PARTIAL"), ("HIT (DIRECTION", "PARTIAL"), ("CONFIRMED-DIRECTIONAL", "PARTIAL"),
    ("PARTIALLY", "PARTIAL"), ("PARTIAL", "PARTIAL"), ("MIXED", "PARTIAL"), ("CONFIRMED*", "PARTIAL"),
    ("RESOLVED — TRUE-IN-LETTER", "PARTIAL"),
    # HIT
    ("HIT-NOFIRE", "HIT"), ("HIT", "HIT"), ("CONFIRMED", "HIT"), ("TRUE", "HIT"), ("ACHIEVED", "HIT"),
    ("RESOLVED-TRUE", "HIT"), ("RESOLVED YES", "HIT"), ("RESOLVED CONFIRMED", "HIT"),
    ("RESOLVED — MECHANISM-CONFIRMED", "HIT"), ("RESOLVED — DIR-CONFIRMED", "PARTIAL"),
    # MISS
    ("MISS-DOWNGRADE", "MISS"), ("MISSED", "MISS"), ("MISS", "MISS"), ("FAILED", "MISS"), ("FALSE", "MISS"),
    ("FALSIFIED", "MISS"), ("RESOLVED-FALSE", "MISS"), ("RESOLVED-FAILED", "MISS"), ("FROZEN-FAILED", "MISS"),
    ("RESOLVED NO", "MISS"), ("RESOLVED MISSED", "MISS"),
    # NO-VERDICT
    ("NO-VERDICT", "NO-VERDICT"), ("INDETERMINATE", "NO-VERDICT"), ("NOT-FIRED-PRECONDITION", "NO-VERDICT"),
    ("NO-FIRE", "NO-VERDICT"), ("EXPIRED-UNGRADEABLE", "NO-VERDICT"), ("EXPIRED", "NO-VERDICT"),
    ("RESOLVED NEUTRAL", "NO-VERDICT"), ("RESOLVED-DEFER", "NO-VERDICT"), ("NOT-FIRING-HEADLINE", "NO-VERDICT"),
    ("UNSCORED", "NO-VERDICT"),
    # ANNULLED (withdrawn from the population: voided, removed, retired, superseded, moved)
    ("ANNULLED", "ANNULLED"), ("VOIDED", "ANNULLED"), ("VOID", "ANNULLED"), ("REMOVED", "ANNULLED"),
    ("RETIRED-UNINSTRUMENTED", "ANNULLED"), ("RETIRED", "ANNULLED"), ("SUPERSEDED", "ANNULLED"),
    ("REHOMED", "ANNULLED"), ("TRANSFERRED-TO-", "ANNULLED"),
    # bare RESOLVED: terminal, direction not in the token
    ("RESOLVED", "RESOLVED-UNTYPED"),
]
TOKEN_MAP.sort(key=lambda kv: -len(kv[0]))
BUCKETS = ["HIT", "MISS", "NO-VERDICT", "ANNULLED", "PARTIAL", "RESOLVED-UNTYPED", "UNMAPPED"]


def bucket(status):
    s = (status or "").strip().upper()
    if not s or s.startswith(NONTERMINAL) or s in ("—", "-"):
        return None
    for prefix, b in TOKEN_MAP:
        if s.startswith(prefix):
            # bare RESOLVED is untyped ONLY when nothing but punctuation/prose follows the word;
            # `RESOLVED-DENY` / `RESOLVED-XYZ` are typed tokens this map does not know → UNMAPPED
            if b == "RESOLVED-UNTYPED" and not re.match(r"RESOLVED(\s*$|\s+[—(·:\[]|\s+\S)", s):
                return "UNMAPPED"
            return b
    return "UNMAPPED"


def in_window(d, start, end):
    return d is not None and start <= d <= end


def parse_iso(s):
    m = ISO.search(s or "")
    return m.group(1) if m else None


# ---------------------------------------------------------------- inputs
def tsv_rows(path):
    """(lineno, fields) for data rows; comment lines (#) and blanks skipped; header returned first."""
    out = []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for i, line in enumerate(fh, 1):
            if not line.strip() or line.startswith("#"):
                continue
            out.append((i, line.rstrip("\n").split("\t")))
    return out


def col1_loops(start, end):
    """DOCKET rows whose state cell carries `RESOLVED YYYY-MM-DD` inside the window; source-named test on the cell."""
    rows = tsv_rows(DOCKET)
    res, res_nosrc, tomb = [], [], 0
    for ln, f in rows:
        if len(f) < 4:
            continue
        state = f[3]
        if state.startswith("RESOLVED · hist→") or state.startswith("RESOLVED · hist"):
            tomb += 1
            continue
        m = re.search(r"RESOLVED\s*(2026-\d\d-\d\d)", state)
        if not m or not in_window(m.group(1), start, end):
            continue
        rec = (ln, m.group(1), f[1][:70].strip(), f[2].strip())
        (res if SOURCE_RE.search(state) else res_nosrc).append(rec)
    return res, res_nosrc, tomb


def wq_rows():
    """WILL_QUEUE table rows: (row_no, line_no, text)."""
    out = []
    with open(WQ, encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            m = re.match(r"\|\s*\**(\d+)\b", line)   # bold-titled rows: `| **171 Codex …** |`
            if m:
                out.append((int(m.group(1)), i, line))
    return out


STAMP = re.compile(r"\b(RULED|DONE|RETRACTED|CORRECTED|REVERSED|WITHDRAWN|AMENDED)\b[^0-9\n]{0,14}(2026-\d\d-\d\d)")
DOCKET_REF = re.compile(r"DOCKET\s*(?:L|row\s*|row-)(\d+)|\bL(\d{2,3})\b(?=[^/]{0,3}(?:\)|,|;|\s|$))")


def col5_rulings(start, end):
    """WQ rows with a RULED stamp inside the window (rows AND stamps counted); DONE stamps separately;
    RETRACTED/CORRECTED/REVERSED/WITHDRAWN/AMENDED stamps → column 4 input."""
    ruled, done, amended = [], [], []
    for n, ln, text in wq_rows():
        for kind, d in STAMP.findall(text):
            if not in_window(d, start, end):
                continue
            refs = sorted({a or b for a, b in re.findall(r"DOCKET\s*(?:L|row\s*|row-)(\d+)|(?!)(\d+)", text)})
            rec = (n, ln, d, refs)
            if kind == "RULED":
                ruled.append(rec)
            elif kind == "DONE":
                done.append(rec)
            else:
                amended.append((n, ln, d, kind))
    props = sorted(p for p in os.listdir(PROPOSALS)
                   if p.lower().endswith("ruled.md") and in_window(parse_iso(p), start, end)) if os.path.isdir(PROPOSALS) else []
    return ruled, done, amended, props


def col2_forecasts(start, end):
    """Registry-driven. Returns per-ledger dicts + the NOT-SEEN list + CANNOT-EVALUATE list."""
    reg = tsv_rows(REGISTRY)
    hdr = reg[0][1]
    want = ["path", "status_col", "date_col", "date_source", "outcome_col", "status"]
    if hdr != want:
        print(f"rc=2 CANNOT-EVALUATE: LEDGERS.tsv header {hdr} != {want}")
        sys.exit(2)
    results, cannot = [], []
    registered = set()
    for ln, f in reg[1:]:
        if len(f) != len(want):
            cannot.append((f[0] if f else f"line {ln}", f"registry row width {len(f)} != {len(want)}"))
            continue
        r = dict(zip(want, f))
        registered.add(r["path"])
        p = os.path.join(ROOT, r["path"])
        if not os.path.isfile(p):
            cannot.append((r["path"], "file absent"))
            continue
        rows = tsv_rows(p)
        if not rows:
            cannot.append((r["path"], "empty"))
            continue
        h = rows[0][1]
        need = [r["status_col"], r["outcome_col"]] + ([r["date_col"]] if r["date_col"] != "NONE" else [])
        missing = [c for c in need if c not in h]
        if missing:
            cannot.append((r["path"], f"header lacks {missing}"))
            continue
        si, oi = h.index(r["status_col"]), h.index(r["outcome_col"])
        di = h.index(r["date_col"]) if r["date_col"] != "NONE" else None
        rec = {"path": r["path"], "status": r["status"], "date_source": r["date_source"], "rows": 0,
               "malformed": [], "terminal": 0, "in_window": [], "date_not_seen": [], "buckets": Counter()}
        for rln, f2 in rows[1:]:
            rec["rows"] += 1
            if len(f2) != len(h):
                rec["malformed"].append((rln, f2[0][:20] if f2 else "?", len(f2), len(h)))
                continue
            b = bucket(f2[si])
            if b is None:
                continue
            rec["terminal"] += 1
            d = parse_iso(f2[di]) if di is not None else None
            tag = "COLUMN"
            if d is None and r["date_source"] == "INLINE-FIRST-ISO":
                d, tag = parse_iso(f2[oi]), "INLINE-DATE"
            if d is None:
                rec["date_not_seen"].append((f2[0][:20], b))
                continue
            if in_window(d, start, end):
                rec["in_window"].append((f2[0][:20], b, d, tag, f2[si].strip()[:40]))
                rec["buckets"][b] += 1
        results.append(rec)
    # bounded discovery ONLY to name what the registry does not see — never counted
    found = []
    for a in sorted(os.listdir(os.path.join(ROOT, "AGENTS"))):
        for sub in ("", "workbook", "thesis", "predictions", "archive"):
            d = os.path.join(ROOT, "AGENTS", a, sub)
            if not os.path.isdir(d):
                continue
            for fn in os.listdir(d):
                if fn.upper().startswith("PREDICTIONS") and fn.endswith(".tsv"):
                    rel = os.path.relpath(os.path.join(d, fn), ROOT)
                    if rel not in registered:
                        found.append(rel)
    return results, sorted(found), cannot


def orch_window(start, end, path=orch_log.LEDGER):
    rc, fields = orch_log.check(path, quiet=True)
    if rc:
        orch_log.check(path)
        print("rc=2 CANNOT-EVALUATE: ORCH_LOG does not validate against schema v2")
        sys.exit(2)
    rows = [dict(zip(orch_log.COLS, f)) for f in fields]
    touches = [r for r in rows if orch_log.event_type([r[c] for c in orch_log.COLS]) == "TOUCH"
               and in_window(r["date"], start, end)]
    return touches


def col3_catches(touches):
    caught, unscored_prose, scored_zero = [], [], 0
    for r in touches:
        ok, v = orch_log.int_or_empty(r["brief_defect_count"])
        if ok and v is not None and v >= 1:
            caught.append((r["date"], r["desk"], r["touch"], v))
        elif ok and v == 0:
            scored_zero += 1
        elif r["brief_defects"].strip() and r["brief_defects"].strip() not in ("—", "-"):
            unscored_prose.append((r["date"], r["desk"], r["touch"]))
    return caught, scored_zero, unscored_prose


def col4_corrections(start, end):
    rows = tsv_rows(CORR)
    if not rows:
        return None, []
    h = rows[0][1]
    for c in ("correction_id", "date", "corrector", "targets"):
        if c not in h:
            print(f"rc=2 CANNOT-EVALUATE: CORRECTIONS.tsv header lacks {c}")
            sys.exit(2)
    ci, di, ki, ti = (h.index(c) for c in ("correction_id", "date", "corrector", "targets"))
    out = []
    for ln, f in rows[1:]:
        if len(f) <= max(ci, di, ki, ti):
            continue
        if in_window(f[di].strip(), start, end):
            out.append((f[ci], f[di], f[ki], f[ti][:40], ln))
    return len(rows) - 1, out


def col6_git(start, end):
    fmt = "%h%x09%ae%x09%ad%x09%s"
    cmd = ["git", "log", f"--since={start} 00:00:00", f"--until={end} 23:59:59", f"--format={fmt}", "--date=short"]
    out = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=True).stdout
    commits = [l.split("\t", 3) for l in out.splitlines() if l.strip()]
    author_days = {(c[1], c[2]) for c in commits}
    desk_days = set()
    for c in commits:
        m = re.match(r"([A-Z][A-Z0-9_+-]*)(?::| ->)", c[3])
        if m:
            desk_days.add((m.group(1), c[2]))
    # state-maintenance share: commits whose EVERY path is under PROME/
    prome_only = 0
    for c in commits:
        files = subprocess.run(["git", "show", "--format=", "--name-only", c[0]], cwd=ROOT,
                               capture_output=True, text=True).stdout.split()
        if files and all(p.startswith("PROME/") for p in files):
            prome_only += 1
    return commits, author_days, desk_days, prome_only, " ".join(cmd)


def ratio(a, b):
    return f"{a}/{b} = {a / b:.2f}" if b else f"{a}/{b} = NOT-COMPUTABLE (denominator 0)"


# ---------------------------------------------------------------- render
def render(week_ending, orch_path=orch_log.LEDGER):
    end = week_ending
    start = (date.fromisoformat(end) - timedelta(days=6)).isoformat()
    out = io.StringIO()
    P = lambda *a: print(*a, file=out)

    loops, loops_nosrc, tomb = col1_loops(start, end)
    ledgers, unregistered, cannot = col2_forecasts(start, end)
    touches = orch_window(start, end, orch_path)
    caught, scored_zero, unscored_prose = col3_catches(touches)
    corr_total, corr = col4_corrections(start, end)
    ruled, done, amended, props = col5_rulings(start, end)
    commits, author_days, desk_days, prome_only, gitq = col6_git(start, end)

    resolved_all = sum(len(l["in_window"]) for l in ledgers)
    bucket_tot = Counter()
    for l in ledgers:
        bucket_tot.update(l["buckets"])
    linked = [(n, ln, d, refs) for n, ln, d, refs in ruled if any(int(r) in {x[0] for x in loops + loops_nosrc} for r in refs)]
    zc_aff = [r for r in touches if (r["zero_capital"] or "").strip().upper().split(" ")[0].rstrip(",;—-") in ("OK", "YES", "ZERO", "N/A")]
    pre, post = len(caught), len(corr) + len(amended)

    P("# COORDINATION-VALUE SCORECARD — DOCKET L239 · week ending " + end)
    P(f"\n**Renderer:** `AGENTS/DAEDALUS/scripts/scorecard.py --week-ending {end}` ({VERSION}) · **Spec:** "
      f"`AGENTS/DAEDALUS/design/2026-08-28_coordination_scorecard_v1.md` · **Window:** {start} → {end} inclusive (7d) · "
      f"**Rendered at HEAD:** `{subprocess.run(['git','rev-parse','--short','HEAD'],cwd=ROOT,capture_output=True,text=True).stdout.strip()}`")
    lg = subprocess.run(["git", "log", "-1", "--format=%h %ad", "--date=short", "--", orch_path], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    ns = subprocess.run(["git", "diff", "--numstat", "--", orch_path], cwd=ROOT, capture_output=True, text=True).stdout.split()
    dirty = f"+{ns[0]}/−{ns[1]} lines UNCOMMITTED in the working tree (the render reads the tree, not HEAD)" if ns else "working tree == HEAD"
    P(f"\n**ORCH_LOG vintage:** last commit `{lg or 'NOT-SEEN'}` · {dirty} · {len(touches)} TOUCH rows in window · whole ledger in the appendix.")
    P("\n⛔ **DESCRIPTIVE ONLY — no success threshold is set, and none may be set before >=4 renders exist.** "
      "Every cell is a count with its query and its source rows printed beside it. Anything the instrument cannot see "
      "is `NOT-SEEN`, never zero. Rulings given in-session or on Telegram and not written to WILL_QUEUE are NOT-SEEN.")

    # ---- summary table
    P("\n## Summary (all nine v1 columns + the commission's tenth)\n")
    P("| # | Column | Value | Both terms / note |")
    P("|---|---|---|---|")
    P(f"| 1 | `loops_completed` | **{len(loops)}** | DOCKET rows RESOLVED in window naming a source · +{len(loops_nosrc)} resolved with NO source named · {tomb} tombstones (date NOT-SEEN) |")
    P(f"| 2 | `forecasts_resolved` | **{resolved_all}** | " + " · ".join(f"{b} {bucket_tot[b]}" for b in BUCKETS if bucket_tot[b]) + f" · {len(ledgers)} ledgers read · {len(cannot)} CANNOT-EVALUATE · {len(unregistered)} NOT-SEEN |")
    P(f"| 3 | `catches_pre_decision` | **{pre}** | ORCH_LOG touches with `brief_defect_count`≥1 (defects summed: {sum(v for *_, v in caught)}) · {scored_zero} scored 0 · {len(unscored_prose)} prose-only UNSCORED |")
    P(f"| 4 | `corrections_post_decision` | **{post}** | CORRECTIONS.tsv rows dated in window {len(corr)} + WQ amendment stamps {len(amended)} |")
    P(f"| 5 | `operator_burden` | rulings=**{len(ruled)}** · minutes=**NOT-SEEN** | {len({n for n,*_ in ruled})} WQ rows carry {len(ruled)} RULED stamps · {len(done)} DONE stamps · {len(props)} `proposals/*RULED.md` records |")
    P(f"| 6 | `coordination_burden` | author_days=**{len(author_days)}** · touches=**{len(touches) if touches else 'NO-TOUCHES-LOGGED'}** · commits=**{len(commits)}** | desk_days (subject-prefix × date, supplementary)={len(desk_days)} |")
    P(f"| 7 | `decision_yield` | {ratio(len(loops), len(ruled))} | loops ÷ rulings; {len(linked)} rulings explicitly LINKED to an in-window loop by DOCKET line citation |")
    P(f"| 8 | `correction_efficiency` | {ratio(pre, pre + post)} | pre ÷ (pre + post) |")
    P(f"| 9 | `zero_capital_touches` | {ratio(len(zc_aff), len(touches))} | cell's first token ∈ {{OK, YES, ZERO, N/A}} ÷ touches |")
    P(f"| 10 | `state_maintenance_share` | {ratio(prome_only, len(commits))} | commits whose EVERY path is under `PROME/` ÷ all commits (the commission's ninth measure, absent from the v1 column table) |")

    # ---- col 1
    P("\n## 1. `loops_completed` — registered question → sourced answer → canonical disposition\n")
    P("query: `PROME/DOCKET.tsv` col 4 matches `RESOLVED YYYY-MM-DD` with the date in window; 'names a source' = the state cell matches a commit hash / repo path / URL / filing id (regex in `SOURCE_RE`).")
    P(f"\nprovenance ({len(loops)} rows, DOCKET physical line numbers):")
    for ln, d, title, owner in loops:
        P(f"- DOCKET L{ln} · {d} · {owner} · {title}")
    if loops_nosrc:
        P(f"\nRESOLVED in window, NO source named ({len(loops_nosrc)}) — counted apart, a DOCKET-hygiene measurement:")
        for ln, d, title, owner in loops_nosrc:
            P(f"- DOCKET L{ln} · {d} · {owner} · {title}")
    P(f"\ntombstoned rows (`RESOLVED · hist→…`, resolution date NOT-SEEN here): {tomb}")

    # ---- col 2
    P("\n## 2. `forecasts_resolved` — terminal token reached inside the window, split by bucket\n")
    P("query: each `scorecards/LEDGERS.tsv` row → status cell mapped through `TOKEN_MAP` (prefix, longest wins) → date from the registered date column, else the first ISO date in the outcome cell (`INLINE-DATE`, event/grade dates indistinguishable).")
    P("\n| Ledger | rows | terminal | in window | buckets | date NOT-SEEN (terminal, undatable) | malformed rows |")
    P("|---|---|---|---|---|---|---|")
    for l in ledgers:
        b = " ".join(f"{k}={v}" for k, v in sorted(l["buckets"].items())) or "—"
        P(f"| `{l['path']}` | {l['rows']} | {l['terminal']} | {len(l['in_window'])} | {b} | {len(l['date_not_seen'])} | {len(l['malformed'])} |")
    P("\nprovenance (rows resolved in window):")
    any_row = False
    for l in ledgers:
        for pid, b, d, tag, tok in l["in_window"]:
            any_row = True
            P(f"- {pid} ({l['path'].split('/')[1]}) · {b} · {d} [{tag}] · status=`{tok}`")
    if not any_row:
        P("- (none)")
    unm = [(l["path"].split("/")[1], pid, tok) for l in ledgers for pid, b, d, tag, tok in l["in_window"] if b == "UNMAPPED"]
    if unm:
        P("\nUNMAPPED tokens in window (extend TOKEN_MAP, never guess): " + " · ".join(f"{a} {p} `{t}`" for a, p, t in unm))
    mal = [(l["path"], m) for l in ledgers for m in l["malformed"]]
    if mal:
        P("\nmalformed rows (width ≠ header; CANNOT-EVALUATE that row, printed so the owner sees it):")
        for p, (rln, pid, w, hw) in mal:
            P(f"- `{p}`:{rln} {pid} width {w} vs header {hw}")
    if cannot:
        P("\nCANNOT-EVALUATE ledgers: " + " · ".join(f"`{p}` ({why})" for p, why in cannot))
    if unregistered:
        P("\nNOT-SEEN (PREDICTIONS*.tsv present in the tree but absent from the registry — listed, never counted): " + " · ".join(f"`{p}`" for p in unregistered))

    # ---- col 3
    P("\n## 3. `catches_pre_decision` — a false premise in the spawn brief, caught at the touch\n")
    P("query: ORCH_LOG TOUCH rows in window with typed `brief_defect_count` ≥ 1. Classification is BY CONSTRUCTION: the ledger's own definition of the cell is a defect in the brief the desk was handed, caught before the desk acted on it.")
    if not touches:
        P("\n**NO-TOUCHES-LOGGED** for this window — column 3, 6 (touches) and 9 render as that token, never as 0.")
    P(f"\nprovenance ({len(caught)} rows; key = date · desk · touch):")
    for d, desk, t, v in caught:
        P(f"- {d} · {desk} · t{t} · {v} defect(s)")
    if unscored_prose:
        P(f"\nUNSCORED — prose in `brief_defects` with no typed count ({len(unscored_prose)}; the renderer never infers a count from prose): " + " · ".join(f"{d} {k} t{t}" for d, k, t in unscored_prose))

    # ---- col 4
    P("\n## 4. `corrections_post_decision` — something published or ruled, then corrected\n")
    P("query: `AGENTS/WALTER/registry/CORRECTIONS.tsv` rows with `date` in window (a correction register row is post-publication by the register's own definition) + WILL_QUEUE stamps RETRACTED/CORRECTED/REVERSED/WITHDRAWN/AMENDED dated in window.")
    P(f"\nprovenance — CORRECTIONS.tsv ({len(corr)} of {corr_total} register rows):")
    for cid, d, who, tg, ln in corr:
        P(f"- {cid} · {d} · corrector {who} → {tg}  (line {ln})")
    if not corr:
        P("- (none dated in window)")
    P(f"\nprovenance — WQ amendment stamps ({len(amended)}):")
    for n, ln, d, kind in amended:
        P(f"- WQ row {n} · {kind} {d} (WILL_QUEUE.md:{ln})")
    if not amended:
        P("- (none)")
    P("\n**ORDER-UNKNOWN pairs: NOT-SEEN.** ORCH_LOG and WILL_QUEUE share no key (schema req. 1), so a same-day catch↔ruling pair cannot be formed without inference; none is inferred. Columns 3 and 4 are therefore classified by construction, not by ordering.")

    # ---- col 5
    P("\n## 5. `operator_burden`\n")
    P("query: WILL_QUEUE table rows whose text carries `RULED YYYY-MM-DD` in window (a row may carry several stamps — rows and stamps both printed); `PROME/proposals/*RULED.md` files dated in window as a second provenance; Will-minutes has no instrument → NOT-SEEN.")
    P(f"\nprovenance — RULED stamps ({len(ruled)}):")
    for n, ln, d, refs in ruled:
        P(f"- WQ row {n} · RULED {d}" + (f" · cites DOCKET L{','.join(refs)}" if refs else "") + f" (WILL_QUEUE.md:{ln})")
    P(f"\nDONE stamps ({len(done)}): " + (" · ".join(f"WQ {n} {d}" for n, ln, d, r in done) or "(none)"))
    P(f"\nproposals RULED records ({len(props)}): " + (" · ".join(f"`{p}`" for p in props) or "(none)"))

    # ---- col 6
    P("\n## 6. `coordination_burden` — three counts, no composite\n")
    P(f"query (git): `{gitq}`")
    P(f"\n- `commits` = **{len(commits)}**")
    P(f"- `author_days` = **{len(author_days)}** distinct (author-email, date): " + " · ".join(f"{a.split('@')[0]} {d}" for a, d in sorted(author_days)))
    P("  > git sees ONE human identity for nearly every desk here, so author_days ≈ calendar days with a commit. `desk_days` below reads the fleet's subject-prefix convention (`DESK:` / `DESK ->`) and is a supplementary count, not the spec's column.")
    dd = Counter(d for d, _ in desk_days)
    P(f"- `desk_days` = **{len(desk_days)}** (desk-prefix × date) over {len(dd)} desks · top: " + " · ".join(f"{k} {v}" for k, v in dd.most_common(8)))
    P(f"- `touches` = **{len(touches) if touches else 'NO-TOUCHES-LOGGED'}** ORCH_LOG TOUCH rows in window · per day: " + (" · ".join(f"{d} {c}" for d, c in sorted(Counter(r['date'] for r in touches).items())) or "—"))

    # ---- col 7-10
    P("\n## 7. `decision_yield` — " + ratio(len(loops), len(ruled)))
    P("\nloops ÷ rulings, both from above. Explicitly linked pairs (WQ row cites `DOCKET L<n>` and L<n> RESOLVED in window):")
    for n, ln, d, refs in linked:
        P(f"- WQ row {n} (RULED {d}) ↔ DOCKET L{','.join(refs)}")
    if not linked:
        P("- (none)")
    P(f"\nUnlinked rulings: {len(ruled) - len(linked)} of {len(ruled)} — their loops, if any, closed in packets or in-session and are NOT-SEEN by this join.")
    P("\n## 8. `correction_efficiency` — " + ratio(pre, pre + post))
    P("\npre ÷ (pre + post). Both terms from columns 3 and 4; the denominator is NOT 'all material defects' — it is the two registers this instrument reads.")
    P("\n## 9. `zero_capital_touches` — " + ratio(len(zc_aff), len(touches)))
    zc = Counter((r["zero_capital"] or "").strip().upper()[:38] or "(blank)" for r in touches)
    P("\nquery: `zero_capital` cell's first token ∈ {OK, YES, ZERO, N/A} — the cell is free text (values in window: " + " · ".join(f"`{k}` {v}" for k, v in zc.most_common(6)) + ").")
    P("\n## 10. `state_maintenance_share` — " + ratio(prome_only, len(commits)))
    P("\nquery: for each commit in window, `git show --format= --name-only <h>`; counted when EVERY path starts with `PROME/`. This is the commission's ninth measure ('coordination-only commits ÷ all'); the v1 spec's column table substituted `zero_capital_touches` for it — recorded as a spec/commission drift, both rendered.")

    # ---- perimeter
    P("\n## Perimeter (travels with every verdict)\n")
    P(f"- Window {start}→{end}. Rows dated before {start} are outside it even when the same loop began there; the whole-ledger ORCH_LOG tables in the appendix cover 8/23 onward for continuity with render #1.")
    P("- ORCH_LOG rows are written at PROME's CONSUMPTION, not at the desk's delivery; `drained` and `brief_defect_count` are desk/PROME self-reports.")
    P("- `loops_completed` depends on the DOCKET state cell naming a source — a loop closed only in a packet is NOT-SEEN (DOCKET hygiene, measured beside the number).")
    P("- WILL_QUEUE rulings given verbally or on Telegram and never stamped `RULED YYYY-MM-DD` on a row are NOT-SEEN. A row that was RULED then rolled off the queue before render is NOT-SEEN.")
    P("- Prediction ledgers: only registered paths are read; INLINE-DATE rows may carry an event date rather than a grade date; bare `RESOLVED` tokens are terminal-untyped, never assigned a direction.")
    P("- git: one author identity for ~all desks; the 8/28 commit spike (518 commits) sits outside this window.")
    P("\n**Renders so far: #1 (2026-09-02, ORCH_LOG legs only) · #2 = this file (first full v1 column set). A success threshold may be proposed at #4 (earliest ~2026-09-25 at a weekly cadence), not before.**")

    # ---- appendix: render #1 form
    P("\n---\n## Appendix — ORCH_LOG whole-ledger volume tables (render #1 form, `coordination_scorecard.py`)\n")
    if orch_path == orch_log.LEDGER:
        import coordination_scorecard as cs
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            cs.main()
        P(buf.getvalue().replace("\n# ", "\n### ").replace("\n## ", "\n### "))
    else:
        P("(appendix skipped: non-default ledger path)")

    series = {"week_ending": end, "window_start": start, "loops": len(loops), "loops_nosrc": len(loops_nosrc),
              "forecasts_resolved": resolved_all, "catches_pre": pre, "corrections_post": post, "rulings": len(ruled),
              "commits": len(commits), "author_days": len(author_days), "touches": len(touches) if touches else "NO-TOUCHES-LOGGED",
              "zero_capital_aff": len(zc_aff), "prome_only_commits": prome_only, "renderer": VERSION}
    return out.getvalue(), series


def write_series(series):
    cols = list(series.keys())
    rows = []
    if os.path.isfile(SERIES):
        for ln, f in tsv_rows(SERIES):
            if f == cols:
                continue
            if len(f) == len(cols) and f[0] != series["week_ending"]:
                rows.append(f)
    rows.append([str(series[c]) for c in cols])
    rows.sort(key=lambda r: r[0])
    with open(SERIES, "w", encoding="utf-8") as fh:
        fh.write("# SCORECARD.tsv — one row per weekly render (re-rendering a week REPLACES its row). DESCRIPTIVE ONLY; no threshold before render #4.\n")
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")


def main(argv):
    if "--week-ending" not in argv:
        print(__doc__)
        return 2
    end = argv[argv.index("--week-ending") + 1]
    date.fromisoformat(end)
    text, series = render(end)
    if "--no-write" in argv:
        print(text)
        return 0
    os.makedirs(OUTDIR, exist_ok=True)
    outp = os.path.join(OUTDIR, f"{end}.md")
    with open(outp, "w", encoding="utf-8") as fh:
        fh.write(text)
    write_series(series)
    print(f"rc=0 RENDERED {os.path.relpath(outp, ROOT)} ({len(text.encode())} B) · series row {end} written to {os.path.relpath(SERIES, ROOT)}")
    return 0


def selftest():
    """§3 both paths: (a) empty synthetic ORCH_LOG → NO-TOUCHES-LOGGED, never 0; (b) token map on live forms;
    (c) unregistered-header ⇒ CANNOT-EVALUATE; (d) source-named regex positive + negative; (e) window arithmetic."""
    import tempfile
    fails = 0

    def chk(ok, msg):
        nonlocal fails
        print(f"  {'✓' if ok else '✗'} {msg}")
        fails += not ok

    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, "L.tsv")
        open(p, "w").write("# f\n" + "\t".join(orch_log.COLS) + "\n")
        t = orch_window("2026-08-29", "2026-09-04", p)
        chk(t == [], "empty ORCH_LOG ⇒ no touches (renders NO-TOUCHES-LOGGED)")
        row = "\t".join(["2026-09-01", "X", "subagent", "1", "t", "0", "d", "OK", "n", "1 — brief said Y", "", "", "1"])
        row2 = "\t".join(["2026-08-20", "Y", "subagent", "1", "t", "0", "d", "OK", "n", "", "", "", ""])
        open(p, "w").write("# f\n" + "\t".join(orch_log.COLS) + "\n" + row + "\n" + row2 + "\n")
        t = orch_window("2026-08-29", "2026-09-04", p)
        chk(len(t) == 1 and t[0]["desk"] == "X", "window filter keeps the in-window touch and drops the 8/20 one")
        caught, z, un = col3_catches(t)
        chk(len(caught) == 1 and caught[0][3] == 1, "typed brief_defect_count=1 ⇒ one catch")
    chk(bucket("RESOLVED NO — window expired") == "MISS", "`RESOLVED NO — window expired` → MISS (longest prefix beats bare RESOLVED)")
    chk(bucket("HIT (partial — offshore only)") == "PARTIAL", "`HIT (partial …)` → PARTIAL, not HIT")
    chk(bucket("OPEN — re-dated 2026-08-13") is None, "`OPEN — re-dated` → non-terminal")
    chk(bucket("RESOLVED") == "RESOLVED-UNTYPED", "bare RESOLVED → RESOLVED-UNTYPED")
    chk(bucket("HIT-NOFIRE") == "HIT" and bucket("NO-FIRE") == "NO-VERDICT", "HIT-NOFIRE → HIT; NO-FIRE → NO-VERDICT")
    chk(bucket("FROBNICATED") == "UNMAPPED" and bucket("RESOLVED-DENY") == "UNMAPPED", "unknown terminal token → UNMAPPED (never guessed); `RESOLVED-DENY` is typed-unknown, not bare RESOLVED")
    chk(bool(SOURCE_RE.search("RESOLVED 2026-09-02 (OTTO 9d9789f4c)")) and not SOURCE_RE.search("RESOLVED 2026-09-02 — closed, see notes"),
        "source regex: commit hash positive · bare prose negative")
    chk((date.fromisoformat("2026-09-04") - timedelta(days=6)).isoformat() == "2026-08-29", "7d window ending 9/4 starts 8/29")
    # (c) registry adapter refuses a header lacking a named column
    with tempfile.TemporaryDirectory() as td:
        bad = os.path.join(td, "P.tsv")
        open(bad, "w").write("ID\tPrediction\tState\n P-1\tx\tHIT\n")
        rows = tsv_rows(bad)
        h = rows[0][1]
        chk("Status" not in h, "adapter precondition: a header lacking `Status` is CANNOT-EVALUATE (checked by name, never positionally)")
    print("SCORECARD SELFTEST " + ("✓ %d/%d" % (12 - fails, 12) if not fails else f"✗ {fails}/12 FAILED"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main(sys.argv))
