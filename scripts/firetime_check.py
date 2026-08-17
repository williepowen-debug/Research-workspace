#!/usr/bin/env python3
"""
firetime_check.py — fire-time artifact freshness check.

Decision-path artifacts (proposals, fire cards, trigger sets) embed dates,
pointers, and level claims that rot silently after canon corrections. The
2026-07-01 audit found the bank-put reshape proposal carrying WAL "Jul-30"
for 5 days after the canonical date moved to Jul-16 — in the fire-time
artifact, with the window two weeks out. This is the mechanism that catches
that class BEFORE a catalyst window opens.

Checks per artifact (read-only; flags, never fixes):
  1. POINTERS  — backtick-quoted repo paths resolve on the filesystem.
  2. DATES     — dates in the artifact that match NO row of PROME/DOCKET.tsv
                 but fall within ±45d of a docket date → drift flag (the
                 Jul-30-vs-Jul-16 class). Dates on lines marked as historical
                 annotations ("corrected from", "was", "superseded", "slid",
                 "designed when") are skipped — alert-fatigue control.
                 Only dates within DRIFT_HORIZON_DAYS of today are
                 drift-eligible (see the constant's comment) — a far-future
                 near-miss reads docket sparsity as drift.
  3. ORDERING  — artifact's last git-commit time vs each cited canon doc's
                 last-change time → "artifact predates canon change" flag.

DISCIPLINE RULE (not automatable): any DATE flag ⇒ full logic re-read of the
artifact, not a find-replace — the 7/1 date fix exposed a gate-sequencing
break that no parser catches.

Usage:
  python3 scripts/firetime_check.py PROME/proposals/foo.md [more paths...]
  python3 scripts/firetime_check.py --window 7      # artifacts cited by docket rows <=7d out
  python3 scripts/firetime_check.py --window 7 --quiet   # boot wiring: prints only on flags

Exit codes: 0 = clean · 1 = flags raised · 2 = usage/docket error (fail loud).
Run from anywhere (repo root resolved internally, cwd-proof).
"""
import argparse
import datetime as dt
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCKET = os.path.join(REPO, "PROME", "DOCKET.tsv")
ALLOWLIST = os.path.join(REPO, "scripts", "firetime_allowlist.tsv")

# DATE DRIFT is only meaningful near-term — a drifted copy of an IMMINENT gate
# date. Beyond this horizon, the ±45d near-match reads docket SPARSITY as
# drift: measured 2026-08-16, 14 of 15 boot DATE-DRIFT flags were bare
# historical tokens (Jan/Feb 2026 mentions) year-rolled into 2027, "near" only
# the sparse year-end rows. The year-boundary roll (>183d) always lands past
# this bound, so rolled tokens are inherently excluded. A CORRECT far-future
# date stays quiet regardless via the exact-match (covered_dates) skip.
DRIFT_HORIZON_DAYS = 90

# Dates on a line containing one of these (before the date) are historical
# annotations or vintage stamps, not live claims — skip them.
ANNOTATION_RE = re.compile(
    r"corrected|refreshed|updated|was |superseded|slid|designed when|rolled off|"
    r"archived|resolved|old ", re.I
)

# Option-expiry heuristic: a date preceded (within ~20 chars) by a strike+P/C
# token ("75 P ", "82 P |", "60 P (×2) |") is a contract expiry, not a catalyst date.
OPTION_RE = re.compile(r"\b\d+(?:\.\d+)?\s?[PC]\b[\s|()×x*0-9]*$")

# A line that itself declares a path dead is not a rot signal.
DEAD_OK_RE = re.compile(r"never existed|does not exist|deleted|removed|retired|gone|no longer", re.I)

# Bare (non-backticked) repo paths, e.g. "WILL/trading-journal/current ..."
# (?<!/) guard: owner cells like "REGINALD/PROME/TERRY" are agent lists, not
# paths — a repo-dir token preceded by '/' is mid-list, never a path root.
BARE_PATH_RE = re.compile(
    r"(?<!/)\b(PROME|AGENTS|FORGE|WILL|skills|scripts|memory|docs)/[\w.-]+(?:/[\w.-]+)*")

MONTHS = {m.lower(): i + 1 for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}

# Date patterns seen in fleet docs: 2026-07-16 · Jul-16-26 · Jul-16 · Jul 16 · 7/16
DATE_PATTERNS = [
    (re.compile(r"\b(20\d{2})-(\d{1,2})-(\d{1,2})\b"), "ymd"),
    (re.compile(r"\b([A-Z][a-z]{2})[- ](\d{1,2})-(\d{2})\b"), "mon_d_yy"),
    (re.compile(r"\b([A-Z][a-z]{2})[- ](\d{1,2})\b(?!-)"), "mon_d"),
    (re.compile(r"\b(\d{1,2})/(\d{1,2})\b(?!\d)"), "m_d"),
]


def parse_date_token(kind, groups, default_year):
    try:
        if kind == "ymd":
            return dt.date(int(groups[0]), int(groups[1]), int(groups[2]))
        if kind == "mon_d_yy":
            mon = MONTHS.get(groups[0].lower())
            return dt.date(2000 + int(groups[2]), mon, int(groups[1])) if mon else None
        if kind == "mon_d":
            mon = MONTHS.get(groups[0].lower())
            return dt.date(default_year, mon, int(groups[1])) if mon else None
        if kind == "m_d":
            m, d = int(groups[0]), int(groups[1])
            if 1 <= m <= 12 and 1 <= d <= 31:
                return dt.date(default_year, m, d)
    except (ValueError, TypeError):
        return None
    return None


def load_docket():
    """Return (rows, dates): rows = list of dicts; dates = set of every date any row covers."""
    if not os.path.exists(DOCKET):
        print(f"ERROR: canonical docket missing at {os.path.relpath(DOCKET, REPO)} — "
              f"fail-loud, not silently clean.", file=sys.stderr)
        sys.exit(2)
    rows, covered = [], set()
    with open(DOCKET, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#") or line.startswith("date\t"):
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            span = parts[0].strip()
            m = re.match(r"^(\d{4})-(\d{2})-(\d{2})(?:\.\.(\d{4})-(\d{2})-(\d{2}))?$", span)
            if not m:
                continue
            start = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
            end = (dt.date(int(m.group(4)), int(m.group(5)), int(m.group(6)))
                   if m.group(4) else start)
            row = {"start": start, "end": end, "catalyst": parts[1].strip(),
                   "owners": parts[2].strip(), "state": parts[3].strip(),
                   "artifacts": [a.strip() for a in (parts[4].split("+") if len(parts) > 4 else [])
                                 if a.strip() and a.strip() != "-"]}
            rows.append(row)
            d = start
            while d <= end:
                covered.add(d)
                d += dt.timedelta(days=1)
            # SLID rows: their old date is also "known" (annotated), don't drift-flag it.
            slid = re.match(r"SLID\((\d{4})-(\d{2})-(\d{2})\)", row["state"])
            if slid:
                covered.add(dt.date(int(slid.group(1)), int(slid.group(2)), int(slid.group(3))))
    return rows, covered


def load_allowlist():
    """Expiry-dated known-benign suppressions (scripts/firetime_allowlist.tsv).

    Row: artifact <TAB> pattern <TAB> expires <TAB> added <TAB> reason.
    Missing file = empty list (allowlist is optional). Malformed rows fail loud
    to stderr and suppress nothing — a broken allowlist must never hide flags.
    """
    rows = []
    if not os.path.exists(ALLOWLIST):
        return rows
    with open(ALLOWLIST, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.rstrip("\n")
            if not line or line.startswith("#") or line.startswith("artifact\t"):
                continue
            parts = line.split("\t")
            if len(parts) < 5:
                print(f"WARNING: allowlist line {n} malformed (<5 cols) — ignored, "
                      f"nothing suppressed by it.", file=sys.stderr)
                continue
            try:
                expires = dt.date.fromisoformat(parts[2].strip())
            except ValueError:
                print(f"WARNING: allowlist line {n} bad expires date {parts[2]!r} — "
                      f"ignored, nothing suppressed by it.", file=sys.stderr)
                continue
            rows.append({"artifact": parts[0].strip(), "pattern": parts[1].strip(),
                         "expires": expires, "added": parts[3].strip(),
                         "reason": parts[4].strip(), "line": n})
    return rows


def apply_allowlist(rel, flags, allow_rows, today):
    """Split flags into (kept, suppressed) for one artifact; expired rows re-flag."""
    kept, suppressed = [], []
    live = [r for r in allow_rows if r["artifact"] == rel and today <= r["expires"]]
    expired = [r for r in allow_rows if r["artifact"] == rel and today > r["expires"]]
    for f in flags:
        row = next((r for r in live if r["pattern"] in f), None)
        if row:
            suppressed.append((f, row))
        else:
            kept.append(f)
    # An expired row whose pattern still matches a flag has NOT been re-verified —
    # keep the flag AND announce the expiry so the row gets renewed or deleted.
    for r in expired:
        if any(r["pattern"] in f for f in flags):
            kept.append(f"ALLOWLIST EXPIRED {r['expires']}: row (line {r['line']}) for "
                        f"pattern {r['pattern']!r} — re-verify the claim, then renew or delete")
    return kept, suppressed


def git_time(path):
    try:
        out = subprocess.run(["git", "-C", REPO, "log", "-1", "--format=%ct", "--", path],
                             capture_output=True, text=True, timeout=10).stdout.strip()
        return int(out) if out else None
    except Exception:
        return None


# A first path segment that reads as a hostname ("cftc.gov", "www.federalreserve.gov")
# marks the token as an external URL, not a repo path (PROME 8/8, class 1: the CFTC
# raw-COT endpoint flagged DEAD POINTER). Bias toward flagging: the skip applies
# ONLY when no repo entry of that name exists, so a real repo dir can never be
# waved through by looking host-like.
HOST_RE = re.compile(r"^[\w-]+(?:\.[\w-]+)*\.[A-Za-z]{2,6}$")

# A line carrying a URL/domain is quoting an external-host path fragment beside
# its host ("cftc.gov `dea/newcot/deafut.txt`" — RAV/PROME 8/16 class B): a
# backticked token on such a line that fails ALL resolution bases is part of the
# URL, not a dead repo path. Scan-scope note: a genuinely dead repo pointer
# sharing a line with a URL is waved through by this — narrow by construction
# (guard is tested only AFTER resolution fails; a live repo path on a URL line
# resolves and never reaches it).
URL_LINE_RE = re.compile(r"https?://|www\.|\b[\w-]+\.(?:gov|com|org|net|edu|io)\b")


def extract_repo_paths(text):
    """Backtick-quoted repo-relative paths with a file extension."""
    out = set()
    for tok in re.findall(r"`([^`\n]{4,120})`", text):
        tok = tok.strip().rstrip(".,;:")
        if re.match(r"^[A-Za-z0-9_][\w./-]*\.(md|tsv|py|sh|json|txt|csv)$", tok) and "/" in tok:
            if tok.startswith(("http", "~", "$")):
                continue
            first = tok.split("/", 1)[0]
            if HOST_RE.match(first) and not os.path.exists(os.path.join(REPO, first)):
                continue  # external URL written without a scheme
            out.add(tok)
    return sorted(out)


def check_artifact(path, docket_rows, covered_dates, today):
    rel = os.path.relpath(path, REPO) if os.path.isabs(path) else path
    full = path if os.path.isabs(path) else os.path.join(REPO, path)
    flags, infos = [], []
    # Target-level lifecycle retry (same class as the cited-pointer fix below,
    # one level up): a DOCKET row cites an artifact; the owner git-mv's it to
    # processed/ (inbox) or delivered/ (outbox) when actioned. Check the moved
    # file rather than flagging UNREADABLE — a missing artifact in NEITHER
    # lifecycle home still fails loud.
    if not os.path.exists(full):
        head, base = os.path.split(full)
        for sub in ("processed", "delivered"):
            twin = os.path.join(head, sub, base)
            if os.path.exists(twin):
                infos.append(f"artifact filed to {sub}/ — checked there (update the docket "
                             f"artifact cell at next touch)")
                full = twin
                rel = os.path.relpath(twin, REPO)
                break
    try:
        text = open(full, encoding="utf-8", errors="replace").read()
    except OSError as e:
        return [f"UNREADABLE: {e}"], []

    # 1. Pointer resolution — backticked paths + bare repo-dir-prefixed tokens,
    #    line-by-line so lines that declare a path dead don't flag.
    #    A pointer is LIVE if it resolves against the repo root OR the citing
    #    artifact's own directory — agents write paths relative to their own
    #    dir (`workbook/X.tsv` inside AGENTS/<NAME>/ = AGENTS/<NAME>/workbook/X.tsv).
    #    Root-only resolution produced ~14 false DEAD flags at the 7/16 boot
    #    (HENRY-verified class; fixed 7/16 Will-approved).
    art_dir = os.path.dirname(full)
    # Resolution bases — each may legitimately anchor a relative cite:
    #   repo root · the citing file's own dir · EVERY ancestor dir up to the
    #   repo root (subsumes the 7/17 AGENTS/<NAME>/ home base, and covers
    #   session-dir cites like FORUM/<session>/<group>/x.md citing a sibling
    #   group — RAV/PROME 8/16 class C-1) · the SENDER's home for packets
    #   named from-<AGENT> (a packet in the recipient's inbox writes paths
    #   relative to the sender's own dir — the HOMER case, class C-2).
    bases = [REPO, art_dir]
    _d = os.path.dirname(art_dir)
    while _d.startswith(REPO) and _d not in bases:
        bases.append(_d)
        _d = os.path.dirname(_d)
    _m_sender = re.search(r"from-([A-Z]+)", os.path.basename(full))
    if _m_sender:
        _sender_home = os.path.join(REPO, "AGENTS", _m_sender.group(1))
        if os.path.isdir(_sender_home) and _sender_home not in bases:
            bases.append(_sender_home)

    def _resolves(p):
        return any(os.path.exists(os.path.join(b, p)) for b in bases)

    # inbox→processed/ / outbox→delivered/ lifecycle (PROME 8/8, class 2, n≥5;
    # delivered/ leg added 8/16 for symmetry with the target-level retry above —
    # the TERRY arm-packet case): a report cites a packet; the owner git-mv's it
    # to processed/ (inbox) or delivered/ (outbox) when actioned; the citation
    # "dies" BECAUSE the system worked. Before declaring a pointer dead, retry
    # with each lifecycle dir inserted before the basename — resolves ⇒ designed
    # disposition, reported as a · note (never a ⚠️ flag).
    def _lifecycle_twin(p):
        head, base = os.path.split(p)
        if not base or head.rstrip("/").endswith(("processed", "delivered")):
            return None
        for sub in ("processed", "delivered"):
            twin = os.path.join(head, sub, base) if head else os.path.join(sub, base)
            if _resolves(twin):
                return sub
        return None

    dead, moved = set(), {}
    for line in text.splitlines():
        if DEAD_OK_RE.search(line):
            continue
        for p in extract_repo_paths(line):
            if not _resolves(p):
                if URL_LINE_RE.search(line):
                    continue  # external-host fragment quoted beside its domain (class B)
                sub = _lifecycle_twin(p)
                if sub:
                    moved[p] = sub
                else:
                    dead.add(p)
        for m in BARE_PATH_RE.finditer(line):
            tok = m.group(0).rstrip(".,;:/")
            if any(c in tok for c in "<>{}*$") or tok in dead or tok in moved:
                continue
            segs = tok.split("/")
            # Extension-less token whose tail segments are all CAPS/digits is an
            # agent/owner list or acronym prose ("PROME/LIQUID/WALTER",
            # "skills/MCP", "memory/2026-07-08"), not a path claim — skip.
            # Title-case tails are the same class ("PROME/Will synthesis" —
            # owner notation, RAV/PROME 8/16 class A ×4): repo dirs are
            # lowercase or ALL-CAPS, so a Title-case segment reads as a NAME.
            # Lowercase-leading segments (inbox, tools, workbook) stay live.
            if (not re.search(r"\.\w{2,4}$", tok)
                    and all(re.fullmatch(r"[A-Z0-9_-]+|[A-Z][A-Za-z0-9_-]*", s)
                            for s in segs[1:])):
                continue
            prefix2 = "/".join(segs[:2])
            full_missing = bool(re.search(r"\.\w{2,4}$", tok)) and not _resolves(tok)
            prefix_missing = len(segs) >= 2 and not _resolves(prefix2)
            if full_missing and _lifecycle_twin(tok):
                moved[tok] = _lifecycle_twin(tok)
            elif prefix_missing or full_missing:
                dead.add(tok if full_missing else prefix2)
    for p in sorted(dead):
        flags.append(f"DEAD POINTER: `{p}` does not exist")
    for p in sorted(moved):
        infos.append(f"cited packet now in {moved[p]}/ — designed disposition, not rot: `{p}`")

    # 2. Date drift vs docket — FUTURE dates only (past dates are provenance,
    #    not fire-path claims), skipping option expiries and annotation lines.
    default_year = today.year
    seen = set()
    for line in text.splitlines():
        for pat, kind in DATE_PATTERNS:
            for m in pat.finditer(line):
                # Prediction-ID guard: "LAB-10/11" (= LAB-10 and LAB-11) parses
                # as Oct-11 via the bare m/d pattern. An UPPERCASE-run + hyphen
                # immediately before the token is an ID list, not a date claim.
                # Lowercase prefixes stay live ("pre-7/23" is a real date).
                if kind == "m_d" and re.search(r"[A-Z]{2,}-$", line[: m.start()]):
                    continue
                d = parse_date_token(kind, m.groups(), default_year)
                # Year-boundary roll for bare tokens (no year written): a date
                # >~6 months off is on the wrong side of a year boundary — a Dec
                # run must read "Jan 5" as next year, an early-Jan run must read
                # "Dec 28" as last year. Explicit-year kinds never roll.
                if d is not None and kind in ("mon_d", "m_d"):
                    try:
                        if (today - d).days > 183:
                            d = d.replace(year=d.year + 1)
                        elif (d - today).days > 183:
                            d = d.replace(year=d.year - 1)
                    except ValueError:
                        pass  # Feb-29 roll into a non-leap year: keep as parsed
                # Strictly-future dates only: past/today tokens are vintage
                # stamps and provenance, not fire-path claims.
                if d is None or d in seen or d <= today or d in covered_dates:
                    continue
                # Horizon bound: a far-future date is not a fire-path claim
                # for this boot — see DRIFT_HORIZON_DAYS.
                if (d - today).days > DRIFT_HORIZON_DAYS:
                    continue
                before = line[: m.start()]
                if ANNOTATION_RE.search(before):
                    continue  # historical annotation / vintage stamp
                if OPTION_RE.search(before[-20:]):
                    continue  # option contract expiry, not a catalyst date
                near = sorted(
                    (r for r in docket_rows
                     if abs((d - r["start"]).days) <= 45 or abs((d - r["end"]).days) <= 45),
                    key=lambda r: min(abs((d - r["start"]).days), abs((d - r["end"]).days)))
                if near:
                    seen.add(d)
                    names = "; ".join(f"{r['catalyst']} ({r['start']})" for r in near[:2])
                    if len(near) > 2:
                        names += f" (+{len(near) - 2} more rows in ±45d)"
                    flags.append(f"DATE DRIFT: artifact says {d} ({m.group(0)!r}) — matches no "
                                 f"docket row but is near: {names}. VERIFY + full logic re-read.")

    # 3. Canon-ordering: artifact older than a canon doc it cites
    art_t = git_time(rel)
    if art_t:
        for p in extract_repo_paths(text):
            if not os.path.exists(os.path.join(REPO, p)):
                continue
            canon_t = git_time(p)
            if canon_t and canon_t > art_t:
                days = (canon_t - art_t) / 86400.0
                infos.append(f"predates cited `{p}` by {days:.0f}d — re-read if load-bearing")
    return flags, infos


def main():
    ap = argparse.ArgumentParser(description="Fire-time artifact freshness check.")
    ap.add_argument("paths", nargs="*", help="artifact path(s), repo-relative or absolute")
    ap.add_argument("--window", type=int, help="check artifacts cited by docket rows <=N days out")
    ap.add_argument("--quiet", action="store_true", help="print only when flags raised (boot wiring)")
    args = ap.parse_args()

    today = dt.date.today()
    rows, covered = load_docket()

    targets = list(args.paths)
    if args.window is not None:
        horizon = today + dt.timedelta(days=args.window)
        for r in rows:
            if r["state"].startswith("RESOLVED"):
                continue
            if today <= r["end"] and r["start"] <= horizon:
                targets.extend(a for a in r["artifacts"] if a not in targets and a.endswith(".md"))
    if not targets:
        if not args.quiet:
            print(f"firetime_check: no artifacts to check "
                  f"(window={args.window}: no docket rows in range cite artifacts).")
        return 0

    allow_rows = load_allowlist()
    total_flags, total_suppressed = 0, 0
    for t in targets:
        flags, infos = check_artifact(t, rows, covered, today)
        rel = os.path.relpath(t, REPO) if os.path.isabs(t) else t
        flags, suppressed = apply_allowlist(rel, flags, allow_rows, today)
        total_flags += len(flags)
        total_suppressed += len(suppressed)
        if args.quiet and not flags:
            continue
        status = "⚠️ " if flags else "✅"
        print(f"{status} {t}")
        for f in flags:
            print(f"    ⚠️  {f}")
        if not args.quiet:
            for f, r in suppressed:
                print(f"    ◦  allowlisted (expires {r['expires']}): {f}")
            for i in infos:
                print(f"    ·  {i}")
    if total_suppressed and not args.quiet:
        print(f"\n◦ {total_suppressed} known-benign flag(s) suppressed by "
              f"scripts/firetime_allowlist.tsv (expiry-dated; expired rows re-flag).")
    if total_flags:
        print(f"\n→ {total_flags} flag(s). Rule: a DATE flag means FULL LOGIC RE-READ "
              f"of the artifact (a date fix can break gate sequencing), never a find-replace.")
    return 1 if total_flags else 0


if __name__ == "__main__":
    sys.exit(main())
