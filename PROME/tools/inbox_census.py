#!/usr/bin/env python3
"""inbox_census.py — count a desk's UNCONSUMED inbox items the way the desk counts them (WQ-178, 2026-09-04).

Usage: python3 PROME/tools/inbox_census.py LABOR [SAM ...]     (repo-root or PROME/ cwd both fine)

Counts FILES only (never directory entries; dotfiles and README* scaffolds skipped), at the top level of AGENTS/<DESK>/inbox/ and separately per lane
subdirectory (e.g. WALTER/), excluding any `processed/` directory at either level. PROME's own surface is
PROME/inbox/ at the repo root (never AGENTS/PROME/). rc 0 always; the numbers are the output.
Origin: 9/4 doorbells quoted every desk one high because `ls | grep -v processed | wc -l` counted the WALTER/ lane
directory as an item (BOND 3→2, VIOLET 7→6, LABOR 2→1+2-lane, SAM 1→0).
"""
import os, sys, subprocess

def item(dp, f):
    # Scaffold files are not packets (2026-11-09: WALTER and CORAL were each quoted a
    # .gitkeep/README/.gitignore as an unread item): dotfiles and README* are skipped.
    return os.path.isfile(os.path.join(dp, f)) and not f.startswith(".") and not f.upper().startswith("README")

def root():
    return subprocess.run(["git","rev-parse","--show-toplevel"],capture_output=True,text=True).stdout.strip()

def census(desk):
    base = os.path.join(root(), "PROME", "inbox") if desk.upper()=="PROME" else os.path.join(root(), "AGENTS", desk.upper(), "inbox")
    if not os.path.isdir(base):
        return desk, None, {}
    top = sorted(f for f in os.listdir(base) if item(base, f))
    lanes = {}
    for d in sorted(os.listdir(base)):
        dp = os.path.join(base,d)
        if os.path.isdir(dp) and d != "processed":
            lanes[d] = sorted(f for f in os.listdir(dp) if item(dp, f))
    return desk, top, lanes

# ── Owner-unconsumed boot line (S1; DOCKET L730, WQ-401, kept as ONE line by WQ-577) ─────────────────────────
# Design: AGENTS/NEXUS/research/2026-10-08_S1_owner-unconsumed-line_DESIGN.md §2 (definitions) and §5 (cases).
# Acceptance: PROME/tools/tests/ACCEPTANCE_owner_unconsumed_boot_line_2026-11-16.md. Read-only: inbox files,
# WALTER's delivery log, the roster text and a liveness callable. No ledger, no state file.
import datetime as _dt
import re as _re
from pathlib import Path as _Path

MIN_DAYS = 7
ACTION_FORMS = ("**ACTION", "ACTION:", "## ACTION", "## Requested action")


def _scaffold(name):
    return name.startswith(".") or name.upper().startswith("README") or ("MANIFEST" in name.upper() and name.lower().endswith(".md"))


def item_date(name):
    """The clock in the FILE NAME (never mtime): a YYYY-MM-DD prefix or SIG-W-YYYYMMDD. None if absent or not a real day."""
    m = _re.match(r"(\d{4})-(\d{2})-(\d{2})", name) or _re.match(r"SIG-W-(\d{4})(\d{2})(\d{2})", name)
    if not m:
        return None
    try:
        return _dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def due_date(text):
    """An explicit header field `due: YYYY-MM-DD` in the first 15 lines; never any other date, never a non-date."""
    for line in text.splitlines()[:15]:
        m = _re.match(r"due:\s*(\d{4})-(\d{2})-(\d{2})\s*$", line.strip())
        if m:
            try:
                return _dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
            except ValueError:
                return None
    return None


def action_typed(text, desk, lane):
    """Top-level packet: a line starting with one of ACTION_FORMS in the first 4,000 bytes.
    Lane file (fallback when the delivery log lacks it): `Role: ACTION`, or front matter `action:` naming the desk."""
    head = text[:4000]
    if not lane:
        return any(line.startswith(ACTION_FORMS) for line in head.splitlines())
    for line in head.splitlines()[:15]:
        if _re.match(r"Role:\s*ACTION\b", line):
            return True
        if line.startswith("action:") and _re.search(r"(?<![A-Za-z0-9_])" + _re.escape(desk) + r"(?![A-Za-z0-9_])", line):
            return True
    return False


def load_delivery(repo):
    """{handoff_path: (ET date routed, ROLE)} from WALTER's delivery log; later rows win. Raises if unreadable."""
    from zoneinfo import ZoneInfo
    et, out = ZoneInfo("America/New_York"), {}
    with open(_Path(repo) / "AGENTS/WALTER/routed/delivery_log.tsv", encoding="utf-8", errors="replace") as fh:
        cols = fh.readline().rstrip("\n").split("\t")
        i_ts, i_role, i_path = cols.index("timestamp_routed"), cols.index("role"), cols.index("handoff_path")
        for line in fh:
            c = line.rstrip("\n").split("\t")
            if len(c) <= max(i_ts, i_role, i_path):
                continue
            try:
                stamp = _dt.datetime.fromisoformat(c[i_ts].replace("Z", "+00:00"))
            except ValueError:
                continue
            if stamp.tzinfo is None:
                continue
            out[c[i_path]] = (stamp.astimezone(et).date(), c[i_role].strip().upper())
    return out


def perimeter(roster_text):
    """{DESK: tag} for ROSTER's ACTIVE and TIER-2 tables (tag ''), DORMANT table and SPECIAL entries (tagged).
    Anything else under AGENTS/ is outside the perimeter (retired, archive source, tool class, unlisted)."""
    out, section = {}, None
    for line in roster_text.splitlines():
        if line.startswith("## "):
            head = line[3:].strip()
            section = ("ACTIVE" if head.startswith("ACTIVE") else "TIER-2" if head.startswith("TIER-2") else
                       "DORMANT" if head.startswith("DORMANT") else "SPECIAL" if head.startswith("SPECIAL") else None)
            continue
        if section in ("ACTIVE", "TIER-2", "DORMANT"):
            m = _re.match(r"\|\s*\**([A-Z][A-Z0-9_-]{1,12})\**\s*\|", line)
            if m and m.group(1) not in ("AGENT",):
                out.setdefault(m.group(1), "DORMANT" if section == "DORMANT" else "")
        elif section == "SPECIAL":
            m = _re.match(r"\*\*([A-Z][A-Z0-9_-]{1,12})\*\* — ", line)
            if m:
                out.setdefault(m.group(1), "SPECIAL")
    return out


def desk_backlog(repo, desk, today, delivery):
    """Facts for one desk's inbox: items (unconsumed, not scaffolding, not excluded), aged (>= MIN_DAYS), oldest
    (days, name) among dated items, action (aged ACTION-typed), skipped, excluded, undated."""
    base = _Path(repo) / "AGENTS" / desk / "inbox"
    r = dict(items=0, aged=0, oldest=None, action=0, skipped=0, excluded=0, undated=0)
    if not base.is_dir():
        return None
    entries = [("", f) for f in sorted(base.iterdir()) if f.is_file()]
    for d in sorted(base.iterdir()):
        if d.is_dir() and d.name != "processed":
            entries += [(d.name, f) for f in sorted(d.iterdir()) if f.is_file()]
    for lane, f in entries:
        if _scaffold(f.name):
            r["skipped"] += 1
            continue
        try:
            text = f.read_bytes()[:8000].decode("utf-8", errors="replace")
        except OSError:
            text = ""
        due = due_date(text)
        if due is not None and due >= today:
            r["excluded"] += 1
            continue
        r["items"] += 1
        logged = delivery.get(f"AGENTS/{desk}/inbox/{lane}/{f.name}") if lane else None
        date = logged[0] if logged else item_date(f.name)
        if date is None:
            r["undated"] += 1
            continue
        age = (today - date).days
        if age < MIN_DAYS:
            continue
        r["aged"] += 1
        if r["oldest"] is None or age > r["oldest"][0]:
            r["oldest"] = (age, (lane + "/" if lane else "") + f.name)
        if (logged[1] == "ACTION") if logged else action_typed(text, desk, lane):
            r["action"] += 1
    return r


def owner_unconsumed(repo, today, last_self_commit, roster_text, delivery=None):
    """Desks DARK >= MIN_DAYS (no self-commit) that hold inbox items aged >= MIN_DAYS. A backlog fact, never a
    launch authorization. `last_self_commit(desk)` -> (iso date, sha) | None | ("!ERR", message)  [spawn_list.Liveness].
    A git error or an unfound self-commit is UNKNOWN for that desk: never dark, never clean."""
    repo = _Path(repo)
    log_read = True
    if delivery is None:
        try:
            delivery = load_delivery(repo)
        except (OSError, ValueError):
            delivery, log_read = {}, False
    roster = perimeter(roster_text)
    if not roster:
        raise ValueError("no ACTIVE, TIER-2, DORMANT or SPECIAL desk parsed from the roster")
    out = dict(hits=[], unknown=[], outside=[], searched=0, items=0, skipped=0, excluded=0, log_read=log_read, as_of=today.isoformat())
    for d in sorted((repo / "AGENTS").iterdir()):
        desk = d.name
        if not d.is_dir() or not _re.fullmatch(r"[A-Z][A-Z0-9_-]*", desk):
            continue
        b = desk_backlog(repo, desk, today, delivery)
        if b is None:
            continue
        if desk not in roster:
            if b["aged"]:
                out["outside"].append((desk, b["aged"]))
            continue
        out["searched"] += 1
        out["items"] += b["items"]; out["skipped"] += b["skipped"]; out["excluded"] += b["excluded"]
        if not b["aged"]:
            continue
        live = last_self_commit(desk)
        if not live or live[0] == "!ERR":
            out["unknown"].append(desk)
            continue
        try:
            dark = (today - _dt.date.fromisoformat(live[0])).days
        except ValueError:
            out["unknown"].append(desk)
            continue
        if dark < MIN_DAYS:
            continue
        tag = roster[desk]
        out["hits"].append(dict(desk=desk, tag=tag, items=b["items"], aged=b["aged"], oldest=b["oldest"], dark=dark,
                                last=live, action=0 if tag == "DORMANT" else b["action"]))
    out["hits"].sort(key=lambda h: (-(h["action"] > 0), -h["oldest"][0], h["desk"]))
    return out


def render_owner_unconsumed(r, shown=8):
    """ONE line. ACTION-bearing desks first; at most `shown` desks named, the rest counted."""
    parts = []
    for h in r["hits"][:shown]:
        tag = f" [{h['tag']}]" if h["tag"] else ""
        act = f" · {h['action']} ACTION ≥{MIN_DAYS}d (WQ-206 class, CANDIDATE only)" if h["action"] else ""
        parts.append(f"{h['desk']}{tag} {h['items']} item(s) · oldest {h['oldest'][0]}d · dark {h['dark']}d{act}")
    if len(r["hits"]) > shown:
        parts.append(f"+{len(r['hits']) - shown} more desk(s)")
    tail = (f"searched {r['searched']} desks · {r['items']} items · {r['skipped']} scaffold file(s) skipped · "
            f"{r['excluded']} excluded by a due: date")
    if r["unknown"]:
        tail += " · liveness UNKNOWN (git error or no self-commit found): " + ", ".join(r["unknown"])
    if r["outside"]:
        tail += " · outside the roster perimeter, aged items: " + ", ".join(f"{d} {n}" for d, n in r["outside"])
    if not r["log_read"]:
        tail += " · WALTER's delivery log unread, file-name dates used"
    return ("; ".join(parts) if parts else "none") + " — " + tail


def main(argv):
    if not argv:
        print(__doc__); return 0
    for desk in argv:
        d, top, lanes = census(desk)
        if top is None:
            print(f"{d.upper():<10} inbox: NOT FOUND"); continue
        lane_s = " · ".join(f"{k}/ {len(v)}" for k,v in lanes.items()) or "no lanes"
        print(f"{d.upper():<10} top-level {len(top):>3} · {lane_s}   (files only; processed/ excluded)")
        for f in top: print(f"           - {f}")
        for k,v in lanes.items():
            for f in v: print(f"           - {k}/{f}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
