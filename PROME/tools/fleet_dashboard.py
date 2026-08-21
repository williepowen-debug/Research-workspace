#!/usr/bin/env python3
"""
fleet_dashboard.py — generate the Fleet Ops HTML dashboard (Will-facing artifact).

PURPOSE: one regenerated surface that turns canon state into a scannable picture —
what needs attention, what's blocking, which agents are stale/lagging, what fires
next. Born 2026-07-11 (Will-directed). DESIGN CONTRACT (anti-rot, per auto-memory
finding_passive_surface_rot_push_not_dashboard):
  - GENERATED, never hand-edited: every datum is parsed from its canon owner file
    or computed from git at run time. If you want to change a fact, change canon.
  - POINTS, never owns: every panel cites its owner file; no position/trade data.
  - FAIL LOUD: a parser that breaks renders a visible PARSE-FAILED cell pointing
    at the owner file — never a silently-missing panel.
  - SELF-DECLARING AGE: the page carries its build stamp and warns when viewed
    stale (>24h amber, >72h red).

USAGE:
  python3 PROME/tools/fleet_dashboard.py -o /path/out.html
  (then publish via the Artifact tool — SAME URL each time; the live artifact URL
   is recorded below once minted. Closeout wiring: PROME/CLOSEOUT.md.)

ARTIFACT_URL: https://claude.ai/code/artifact/c884f088-4936-44a0-9232-30851b9427b6
  (minted 2026-07-11. Same-conversation republish of the same file path keeps this
   URL; from any OTHER session pass url="..." to the Artifact tool — else it mints
   a new URL and orphans Will's tab. finding_artifact_redeploy_same_url.
   FAVICON: 🎛️ — recorded 2026-07-20; keep identical on every republish, Will finds
   the tab by its icon.)

V2 (2026-07-16, Will-directed): + "Since last build" delta panel (diffs canon state vs
  the snapshot persisted at the previous build — PROME/tools/dashboard_state.json,
  committed so deltas survive machine switches) and + "Gate distance" tiles (HEARTBEAT
  stress-dashboard levels, as-of stamps preserved, positioned against the FORGE
  market-data config.py bands — bands stay canon-owned, nothing hand-entered here).
"""
import argparse
import datetime as dt
import html
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import agent_freshness  # own-surface age — the grid's health instrument (8/16)

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def sh(args, timeout=15):
    try:
        return subprocess.run(args, capture_output=True, text=True,
                              timeout=timeout, cwd=REPO).stdout.strip()
    except Exception:
        return ""


def read(rel):
    with open(os.path.join(REPO, rel), encoding="utf-8", errors="replace") as f:
        return f.read()


def md_clean(s):
    s = re.sub(r"\[\[([^\]]+)\]\]", r"\1", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    s = re.sub(r"`([^`]+)`", r"\1", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def esc(s):
    return html.escape(s, quote=True)


def trunc(s, n):
    """Word-boundary truncation with a visible ellipsis — never a mid-word chop."""
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0].rstrip(" ,;:—-(")
    return cut + " …"


EMOJI_CLASS = {"🟢": "ok", "🟡": "watch", "🟠": "elev", "🔴": "crit"}


def status_class(text, default="watch"):
    for e, c in EMOJI_CLASS.items():
        if e in text:
            return c
    return default
# Channel cards use default="none" (neutral gray): a missing status emoji in a
# HEARTBEAT channel head renders honestly-unknown, never a guessed yellow —
# the fix belongs in HEARTBEAT (fleet status-key convention), not here.


# ---------------------------------------------------------------- parsers ----

def parse_roster():
    """ROSTER.md ACTIVE / TIER-2 / DORMANT tables -> lists of (name, domain)."""
    text = read("PROME/ROSTER.md")

    def table(section_start, section_end):
        m = re.search(re.escape(section_start) + r"(.*?)" + re.escape(section_end),
                      text, re.S)
        rows = []
        if not m:
            return rows
        for line in m.group(1).splitlines():
            cells = [c.strip().strip("*").strip("`") for c in line.split("|")]
            if len(cells) >= 3 and re.fullmatch(r"\[?`?[A-Z]{2,}", cells[1].split("/")[0][:20] or "x") \
                    and cells[1] not in ("Agent", "Folder") and not set(cells[1]) <= {"-", " "}:
                name = re.sub(r"[^A-Z]", "", cells[1].split(" ")[0])
                if name:
                    rows.append((name, md_clean(cells[2])))
        return rows

    active = table("## ACTIVE", "## TIER-2")
    tier2 = table("## TIER-2", "## DORMANT")
    dormant = table("## DORMANT", "## RETIRED")
    return active, tier2, dormant


def parse_fleet_map():
    """FLEET_MAP.tsv -> {agent: (level, conf)}."""
    out = {}
    for line in read("AGENTS/DAEDALUS/FLEET_MAP.tsv").splitlines():
        p = line.split("\t")
        if len(p) >= 4 and re.fullmatch(r"L\d(?:-prov-L\d)?", p[2].strip()):
            out[p[0].strip()] = (p[2].strip(), p[3].strip())
    return out


def busdays(d0, d1):
    """Weekdays strictly after d0 through d1 — staleness that doesn't age on weekends."""
    n, d = 0, d0
    while d < d1:
        d += dt.timedelta(days=1)
        if d.weekday() < 5:
            n += 1
    return n


def agent_git(name, today):
    """(business_days_since_last_commit_to_dir, commits_30d) — dir-based activity."""
    path = "PROME/" if name == "PROME" else f"AGENTS/{name}/"
    ts = sh(["git", "log", "-1", "--format=%ct", "--", path])
    days = None
    if ts:
        days = busdays(dt.datetime.fromtimestamp(int(ts)).date(), today)
    n = sh(["git", "rev-list", "--count", "--since=30.days", "HEAD", "--", path])
    return days, int(n) if n.isdigit() else 0


def load_parked(today):
    """PROME/tools/dashboard_parked.tsv -> {agent: (until, reason)} for live rows only.
    Expiry-dated like the firetime allowlist: a lapsed row silently stops parking
    (staleness resumes) — parking can never hide a dead agent."""
    out = {}
    path = os.path.join(REPO, "PROME", "tools", "dashboard_parked.tsv")
    if not os.path.exists(path):
        return out
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or line.startswith("agent\t") or not line.strip():
                continue
            p = line.rstrip("\n").split("\t")
            if len(p) < 4:
                continue
            try:
                until = dt.date.fromisoformat(p[1].strip())
            except ValueError:
                continue
            if today <= until:
                out[p[0].strip()] = (until, p[3].strip())
    return out


def inbox_depth(name):
    root = os.path.join(REPO, "AGENTS", name, "inbox")
    if not os.path.isdir(root):
        return 0
    count = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != "processed"]
        count += sum(1 for f in filenames if not f.startswith("."))
    return count


def parse_gates(today):
    rows = []
    for line in read("PROME/GATES.tsv").splitlines():
        if line.startswith("#") or line.startswith("gate_id") or not line.strip():
            continue
        p = line.split("\t")
        if len(p) < 8:
            continue
        gate, _, owner, cond, _, state, last_checked, _ = p[:8]
        consumed_by = p[8].strip() if len(p) > 8 else ""
        head = state.split("(")[0].strip()
        kind = ("crit" if head.startswith("FIRED-UNEXECUTED")
                else "resolved" if head.startswith(("RESOLVED", "LAPSED", "RETIRED"))
                else "live")
        age = None
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})", last_checked.strip())
        if m:
            age = (today - dt.date(*map(int, m.groups()))).days
        rows.append({"gate": gate.strip(), "owner": owner.strip(), "kind": kind,
                     "state": trunc(md_clean(state), 220), "cond": trunc(md_clean(cond), 160),
                     "checked_age": age, "consumed_by": consumed_by})
    return rows


def parse_docket(today, horizon=21):
    rows = []
    for line in read("PROME/DOCKET.tsv").splitlines():
        if line.startswith("#") or line.startswith("date\t") or not line.strip():
            continue
        p = line.split("\t")
        if len(p) < 4:
            continue
        m = re.match(r"^(\d{4})-(\d{2})-(\d{2})(?:\.\.(\d{4})-(\d{2})-(\d{2}))?$",
                     p[0].strip())
        if not m:
            continue
        start = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        end = dt.date(int(m.group(4)), int(m.group(5)), int(m.group(6))) if m.group(4) else start
        state = p[3].strip()
        if state.startswith("RESOLVED") or end < today or start > today + dt.timedelta(days=horizon):
            continue
        rows.append({"start": start, "end": end, "span": start != end,
                     "catalyst": md_clean(p[1]), "owners": p[2].strip(),
                     "days_out": (start - today).days})
    rows.sort(key=lambda r: r["start"])
    return rows


def parse_heartbeat():
    text = read("HEARTBEAT.md")
    one = ""
    m = re.search(r"^\*\*One-liner:?\*\*:?\s*(.*)$", text, re.M)
    if m:
        # 8/16 (DAEDALUS sweep-1 URGENT-1): prefer-any-quoted-phrase rendered the
        # single word "SPENT" — an incidental quoted token in the 8/14 one-liner,
        # and a kill-on-sight claim INVERTED against canon — for 6 builds/3 days.
        # A quote wins only when it carries most of the line (the 7/24 fully-
        # quoted-one-liner class); incidental tokens fall through to the full
        # cleaned sentence.
        full = md_clean(m.group(1))
        q = re.search(r'[“"]([^”"]+)[”"]', m.group(1))
        one = q.group(1) if (q and len(q.group(1)) >= 0.6 * len(full)) else full
    split = ""
    # 8/16 (DAEDALUS sweep-1 item 4): NEXUS writes the split with either "/" or
    # "·" — the /-only regex left the panel blank for 17d (~25 builds) after the
    # 7/30 re-anchor switched separators.
    m = re.search(r"Break \d+ [/·] Grind \d+ [/·] Unresolved \d+", text)
    if m:
        split = m.group(0)
    else:
        # 8/21 (PAT-105 second instance): the 8/20 HEARTBEAT re-base writes the
        # split COMPACT — "NEXUS 21/44/35 [8/12]" — with no Break/Grind words at
        # all. Same separator-drift class as the 8/16 fix one branch above; parse
        # the compact form and render it in the worded shape the panel expects.
        m2 = re.search(r"NEXUS (\d+)/(\d+)/(\d+)", text)
        if m2:
            split = f"Break {m2.group(1)} / Grind {m2.group(2)} / Unresolved {m2.group(3)}"
    channels = []
    # tolerate the number inside OR outside the bold ("1. **X**" and "**1. X**"):
    # a HEARTBEAT re-base is a breaking format change to this parser (PAT-069)
    for m in re.finditer(r"^\*{0,2}\d+\.\s*\*{0,2}(.+?)\*\*(.*)$", text, re.M):
        head = m.group(1)
        name = md_clean(head.split("—")[0])
        cls = status_class(head, "none")
        headline = trunc(md_clean(head.split("—", 1)[1] if "—" in head else head), 64)
        body = m.group(2)
        if not body.strip():
            # whole-line-bold heading: body starts on the next line
            after = text[m.end():].lstrip("\n").split("\n", 1)[0]
            if not re.match(r"^\*{0,2}\d+\.\s*\*{0,2}|^#|^>", after):
                body = after
        body = trunc(md_clean(body), 230)
        channels.append({"name": name, "cls": cls, "headline": headline, "body": body})
    ticker = []
    # anchor on the first Brent-carrying line within 8 lines of the heading —
    # never require a blank line after it (the old \n\n anchor overshot the
    # whole section when the re-base removed the blank line)
    m = re.search(r"^## Stress dashboard.*$((?:\n.*){1,8})", text, re.M)
    if m:
        line = next((l for l in m.group(1).splitlines() if "Brent" in l), "")
        ticker = [md_clean(t) for t in line.split(" · ") if t.strip()]
    blocking = []
    m = re.search(r"## Blocking / Pending(.*?)(?=\n## )", text, re.S)
    if m:
        for row in re.finditer(r"^\|\s*(🟠|🟡|🔴|🟢)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$",
                               m.group(1), re.M):
            blocking.append({"cls": EMOJI_CLASS.get(row.group(1), "watch"),
                             "text": md_clean(row.group(2)), "ref": md_clean(row.group(3))})
    stamp = ""
    m = re.search(r"\*\*Base:\*\* (\S+)", text)
    if m:
        stamp = m.group(1)
    return {"one": one, "split": split, "channels": channels, "ticker": ticker,
            "blocking": blocking, "base": stamp}


def parse_pending_will():
    text = read("PROME/SCRATCH.md")
    m = re.search(r"Pending Will:([^.\n]+)", text)
    if not m:
        return []
    # 8/16 (sweep-1 trivia): split on `·` only OUTSIDE parentheses — the card
    # writes grouped sub-items like "(D-1 AAPL · D-10 MAIN≡IRA)", which a bare
    # split rendered as 13 items for 12. Leading "**" residue stripped by
    # md_clean on the FIELD, not the line (the old artifact was the label's
    # bold marker riding into item 1).
    items, depth, cur = [], 0, []
    for ch in m.group(1):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch == "·" and depth == 0:
            items.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    items.append("".join(cur))
    return [md_clean(x.strip().lstrip("*").strip()) for x in items if x.strip()]


def parse_spine_stamp(today):
    m = re.search(r"\*\*Last spine audit:\*\* (\d{4}-\d{2}-\d{2})", read("PROME/STATUS.md"))
    if not m:
        return None, None
    d = dt.date.fromisoformat(m.group(1))
    return d, (today - d).days


# ---------------------------------------------- v2: tiles + build deltas ----

STATE_PATH = os.path.join(REPO, "PROME", "tools", "dashboard_state.json")

# ticker-token prefix (HEARTBEAT stress dashboard) -> SERIES name (FORGE config.py).
# Presentation wiring only — the levels and the bands both stay canon-owned.
# 8/16 (DAEDALUS sweep-1 item 4): tile count had attrited 13→4 across the
# 8/12+8/14 HEARTBEAT re-bases — token renames shipped without a consumer
# re-check (PAT-069's named class). Longer prefixes MUST precede their stems
# (the boundary-guard `break` stops the scan on first prefix hit): VIXCLS
# before VIX, DGS10 alongside 10Y, bare lowercase "claims" LAST as fallback.
TICKER_TILE_MAP = [
    ("Brent", "Brent"), ("HY OAS", "HY OAS"), ("CCC", "CCC OAS"),
    ("DGS10", "10Y Yield"), ("10Y", "10Y Yield"), ("MOVE", "MOVE"),
    ("VIXCLS", "VIX"), ("VIX", "VIX"),
    ("USD/JPY", "USD/JPY"), ("Cushing", "Cushing"), ("WAL", "WAL"), ("OZK", "OZK"),
    ("Init claims", "Init Claims"), ("Cont claims", "Cont Claims"),
    ("SOFR99-IORB", "SOFR-IORB"), ("SOFR-IORB", "SOFR-IORB"),
    ("claims", "Init Claims"),
]


def load_bands():
    """FORGE/tools/market-data/config.py SERIES -> {name: series dict}. Bands = canon."""
    sys.path.insert(0, os.path.join(REPO, "FORGE", "tools", "market-data"))
    import config as md_config
    return {s["name"]: s for s in md_config.SERIES}


def _inside(val, rng):
    lo, hi = rng
    return (lo is None or val >= lo) and (hi is None or val < hi)


def _band_class(val, s):
    if _inside(val, s["red"]):
        return "crit"
    if _inside(val, s["yellow"]):
        return "watch"
    return "ok"


def _fmt(v):
    if abs(v) >= 1e5:
        return f"{v:,.0f}"
    return f"{v:,.2f}".rstrip("0").rstrip(".")


def _fmt_rng(rng):
    lo, hi = rng
    if lo is None:
        return f"<{_fmt(hi)}"
    if hi is None:
        return f"≥{_fmt(lo)}"
    return f"{_fmt(lo)}–{_fmt(hi)}"


def parse_tiles(hb):
    """Distance tiles: HEARTBEAT ticker levels (as-of stamps kept) vs config bands.
    Guards (v2.1): word-boundary prefix match (VIX3M/VIX must not read as VIX) +
    first-claim-wins per tile (the ticker's primary level precedes derived tokens
    like 'VIX lev-money', which would otherwise overwrite it)."""
    bands = load_bands()
    tiles, claimed = [], set()
    for tok0 in hb["ticker"]:
        # 8/16 fixes (sweep-1 item 4): strip md-bold before prefix match
        # ("**Brent" / "**DGS10**"); split spaced-slash-joined bank tokens
        # ("KRE $x / WAL $y / OZK $z") into candidates — the [as-of] stamp is
        # inherited from the FULL token when a candidate lacks its own.
        stamp_full = re.search(r"\[([^\]]{1,90})\]", tok0)
        subtoks = [t.lstrip("*").strip() for t in tok0.split(" / ")]
        for tok in subtoks:
            for prefix, cname in TICKER_TILE_MAP:
                if not tok.startswith(prefix) or cname not in bands:
                    continue
                if tok[len(prefix):len(prefix) + 1].isalnum() or cname in claimed:
                    break
                rest = tok[len(prefix):].replace(",", "").replace("−", "-")
                # never pull a number out of an instrument label — "(ICE front
                # settle, `BZV26.NYM`)" would yield 26 as the Brent level
                rest = re.sub(r"\([^)]*\)|`[^`]*`", "", rest)
                m = re.search(r"-?\d+(?:\.\d+)?", rest)
                if not m:
                    break
                val = float(m.group(0))
                sfx = re.match(r"\s*([kKM]\b|bps?\b)", rest[m.end():])
                if sfx:
                    u = sfx.group(1)
                    # bp tokens vs percentage-point bands (SOFR99-IORB "+5bp" / red 0.25)
                    val *= 1e3 if u in "kK" else (1e6 if u == "M" else 1e-2)
                s = bands[cname]
                hw = s["direction"] == "higher_worse"
                red_line = s["red"][0] if hw else s["red"][1]
                if red_line:
                    # unit-scale reconcile: HEARTBEAT writes "215k"/"20.04M"; config bands
                    # are in native units (claims raw count, Cushing in millions).
                    for scale in (1, 1e-3, 1e-6, 1e3, 1e6):
                        if 0.05 <= abs(val * scale) / abs(red_line) <= 20:
                            val *= scale
                            break
                    else:
                        break  # magnitudes irreconcilable — no tile, never a wrong one
                gap = (red_line - val) if hw else (val - red_line)
                dist = (f"{_fmt(gap)} to red {_fmt(red_line)}" if gap > 0
                        else f"{_fmt(-gap)} PAST red {_fmt(red_line)}")
                stamp_m = re.search(r"\[([^\]]{1,90})\]", tok) or stamp_full
                stamp = re.split(r"[;—]", stamp_m.group(1))[0].strip()[:14] if stamp_m else "?"
                claimed.add(cname)
                tiles.append({"name": cname, "val": val, "cls": _band_class(val, s),
                              "dist": dist, "dir": "↑ worse" if hw else "↓ worse",
                              "stamp": stamp, "yellow": s["yellow"], "red": s["red"]})
                break
    return tiles


FLEET_WORD = {"ok": "fresh", "watch": "quiet", "elev": "lagging",
              "crit": "cold", "none": "parked"}


def make_snapshot(built, hb, gates, docket, fleet, pending, tiles):
    return {"v": 1, "built": built,
            "one": hb["one"], "split": hb["split"],
            "channels": {c["name"]: c["cls"] for c in hb["channels"]},
            "gates": {g["gate"]: f'{g["kind"]}:{g["state"].split(" ")[0]}'
                      for g in gates},
            "docket": sorted(f'{r["start"].isoformat()} {r["catalyst"][:60]}'
                             for r in docket),
            "fleet": {r["name"]: r["cls"] for r in fleet},
            "pending": pending,
            "levels": {t["name"]: t["val"] for t in tiles}}


def load_prev_snapshot():
    if not os.path.exists(STATE_PATH):
        return None
    try:
        with open(STATE_PATH, encoding="utf-8") as f:
            s = json.load(f)
        return s if s.get("v") == 1 else None
    except Exception:
        return None


def diff_snapshots(prev, cur):
    """Canon-state changes since the previous build, worst class first."""
    d = []
    if prev["one"] != cur["one"] and cur["one"]:
        d.append(("elev", f'Regime one-liner CHANGED → “{cur["one"]}”'))
    if prev["split"] != cur["split"] and cur["split"]:
        d.append(("elev", f'NEXUS split {prev["split"] or "—"} → {cur["split"]}'))
    for n, c in cur["channels"].items():
        p = prev["channels"].get(n)
        if p and p != c:
            d.append((c if c == "crit" else "watch", f"Channel {n}: {p} → {c}"))
    for gid, st in cur["gates"].items():
        p = prev["gates"].get(gid)
        if p is None:
            d.append(("watch", f"NEW gate {gid} ({st.split(':', 1)[0]})"))
        elif p != st:
            cls = "crit" if "FIRED-UNEXECUTED" in st else "watch"
            d.append((cls, f"{gid}: {p} → {st}"))
    prev_dock, cur_dock = set(prev["docket"]), set(cur["docket"])
    for row in sorted(cur_dock - prev_dock):
        d.append(("watch", f"Runway + {row[11:]} ({row[:10]})"))
    for row in sorted(prev_dock - cur_dock):
        d.append(("none", f"Runway − {row[11:]} (passed/resolved/re-dated)"))
    for n, c in cur["fleet"].items():
        p = prev["fleet"].get(n)
        if p and p != c and ("crit" in (p, c) or "elev" in (p, c)):
            d.append(("elev" if c in ("crit", "elev") else "ok",
                      f"{n}: {FLEET_WORD.get(p, p)} → {FLEET_WORD.get(c, c)}"))
    for n, v in cur["levels"].items():
        p = prev.get("levels", {}).get(n)
        if p is not None and p != v:
            d.append(("none", f"{n} {_fmt(p)} → {_fmt(v)}"))
    for p in cur["pending"]:
        if p not in prev["pending"]:
            d.append(("watch", f"Pending-Will + {p}"))
    for p in prev["pending"]:
        if p not in cur["pending"]:
            d.append(("ok", f"Pending-Will resolved − {p}"))
    order = {"crit": 0, "elev": 1, "watch": 2, "ok": 3, "none": 4}
    d.sort(key=lambda x: order.get(x[0], 5))
    return d


def run_rc(script, *args):
    try:
        r = subprocess.run([sys.executable, os.path.join(REPO, "scripts", script), *args],
                           capture_output=True, text=True, timeout=60, cwd=REPO)
        return r.returncode
    except Exception:
        return -1


# ------------------------------------------------------------- html pieces ----

CSS = """
:root{
  --paper:#F5F6F7; --panel:#FFFFFF; --ink:#1C2128; --ink2:#5A6472; --line:#DDE2E8;
  --accent:#3D6A8F; --accent-ink:#2E5473;
  --ok:#27754A; --watch:#7E6A00; --elev:#E27429; --crit:#A32B60;
  --ok-bg:#E4F0E9; --watch-bg:#F1ECD6; --elev-bg:#FAE8DA; --crit-bg:#F4DFE9;
  --mono:ui-monospace,'Cascadia Code',Menlo,Consolas,monospace;
}
@media (prefers-color-scheme: dark){:root{
  --paper:#14171B; --panel:#1C2127; --ink:#E6E9ED; --ink2:#98A2AE; --line:#2C333B;
  --accent:#7FA6C9; --accent-ink:#9FBEDA;
  --ok:#348157; --watch:#6E6400; --elev:#D47934; --crit:#B2476B;
  --ok-bg:#1D2E25; --watch-bg:#2C2915; --elev-bg:#332318; --crit-bg:#301B26;
}}
:root[data-theme="dark"]{
  --paper:#14171B; --panel:#1C2127; --ink:#E6E9ED; --ink2:#98A2AE; --line:#2C333B;
  --accent:#7FA6C9; --accent-ink:#9FBEDA;
  --ok:#348157; --watch:#6E6400; --elev:#D47934; --crit:#B2476B;
  --ok-bg:#1D2E25; --watch-bg:#2C2915; --elev-bg:#332318; --crit-bg:#301B26;
}
:root[data-theme="light"]{
  --paper:#F5F6F7; --panel:#FFFFFF; --ink:#1C2128; --ink2:#5A6472; --line:#DDE2E8;
  --accent:#3D6A8F; --accent-ink:#2E5473;
  --ok:#27754A; --watch:#7E6A00; --elev:#E27429; --crit:#A32B60;
  --ok-bg:#E4F0E9; --watch-bg:#F1ECD6; --elev-bg:#FAE8DA; --crit-bg:#F4DFE9;
}
*{box-sizing:border-box;margin:0}
body{background:var(--paper);color:var(--ink);
  font:15px/1.5 -apple-system,'Segoe UI',system-ui,sans-serif;padding:20px 22px 40px}
a{color:var(--accent-ink)}
.mono{font-family:var(--mono);font-variant-numeric:tabular-nums}
h1{font-size:19px;letter-spacing:.4px}
h2{font-size:12px;text-transform:uppercase;letter-spacing:.12em;color:var(--ink2);
  margin-bottom:10px}
.bar{display:flex;flex-wrap:wrap;align-items:baseline;gap:10px 18px;
  border-bottom:2px solid var(--ink);padding-bottom:12px;margin-bottom:16px}
.bar .stamp{font-family:var(--mono);font-size:12.5px;color:var(--ink2)}
#agebadge{font-family:var(--mono);font-size:12px;padding:2px 9px;border-radius:3px;
  background:var(--ok-bg);color:var(--ok);border:1px solid var(--ok)}
#agebadge.aged{background:var(--watch-bg);color:var(--watch);border-color:var(--watch)}
#agebadge.old{background:var(--crit-bg);color:var(--crit);border-color:var(--crit)}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin-left:auto}
.chip{font-family:var(--mono);font-size:11.5px;padding:2px 8px;border-radius:3px;
  border:1px solid;white-space:nowrap}
.ok{color:var(--ok);background:var(--ok-bg);border-color:var(--ok)}
.watch{color:var(--watch);background:var(--watch-bg);border-color:var(--watch)}
.elev{color:var(--elev);background:var(--elev-bg);border-color:var(--elev)}
.crit{color:var(--crit);background:var(--crit-bg);border-color:var(--crit)}
.none{color:var(--ink2);background:var(--paper);border-color:var(--line)}
.card.none{border-left-color:var(--line)}
.muted{color:var(--ink2)}
.regime{margin-bottom:16px}
.oneliner{font-size:16.5px;font-style:italic;margin-bottom:10px;text-wrap:balance}
.oneliner .split{font-style:normal;font-family:var(--mono);font-size:12.5px;
  color:var(--ink2);margin-left:10px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:10px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:4px;
  padding:10px 12px;border-left-width:4px}
.card.ok{border-left-color:var(--ok);background:var(--panel)}
.card.watch{border-left-color:var(--watch);background:var(--panel)}
.card.elev{border-left-color:var(--elev);background:var(--panel)}
.card.crit{border-left-color:var(--crit);background:var(--panel)}
.card .nm{font-weight:600;font-size:13.5px}
.card .hd{font-family:var(--mono);font-size:11.5px;margin:2px 0 6px}
.card .bd{font-size:12.5px;color:var(--ink2);line-height:1.45}
.ticker{overflow-x:auto;white-space:nowrap;background:var(--panel);
  border:1px solid var(--line);border-radius:4px;padding:7px 12px;margin:12px 0 18px;
  font-family:var(--mono);font-size:12.5px}
.ticker span{margin-right:18px;color:var(--ink2)}
.ticker b{color:var(--ink);font-weight:600}
.cols{display:grid;grid-template-columns:minmax(300px,5fr) minmax(380px,7fr);gap:20px}
@media (max-width:920px){.cols{grid-template-columns:1fr}}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:4px;
  padding:14px 16px;margin-bottom:18px}
.attn{list-style:none}
.attn li{display:flex;gap:9px;padding:7px 0;border-top:1px solid var(--line);
  font-size:13px;align-items:flex-start}
.attn li:first-child{border-top:0}
.attn .tag{flex:none;font-family:var(--mono);font-size:10.5px;padding:1px 6px;
  border-radius:3px;border:1px solid;margin-top:2px;text-transform:uppercase;
  letter-spacing:.05em}
.attn .src{display:block;font-family:var(--mono);font-size:11px;color:var(--ink2)}
.runway{list-style:none}
.runway li{display:flex;gap:10px;padding:6px 0;border-top:1px solid var(--line);
  font-size:13px;align-items:baseline}
.runway li:first-child{border-top:0}
.runway .d{flex:none;width:86px;font-family:var(--mono);font-size:12px}
.runway .in{flex:none;width:52px;font-family:var(--mono);font-size:11px;
  color:var(--ink2);text-align:right}
.runway .own{font-family:var(--mono);font-size:11px;color:var(--ink2)}
.runway li.soon .d{color:var(--elev);font-weight:700}
table{border-collapse:collapse;width:100%;font-size:12.5px}
.tablewrap{overflow-x:auto}
th{text-align:left;font-size:10.5px;text-transform:uppercase;letter-spacing:.08em;
  color:var(--ink2);padding:4px 8px 6px;border-bottom:1px solid var(--ink)}
td{padding:5px 8px;border-bottom:1px solid var(--line);vertical-align:top}
td.num{font-family:var(--mono);font-variant-numeric:tabular-nums;text-align:right}
.agent{font-weight:600;white-space:nowrap}
.lvl{font-family:var(--mono);font-size:11px;color:var(--ink2);white-space:nowrap}
.bar30{height:5px;border-radius:2px;background:var(--accent);min-width:2px}
.barwrap{width:64px;background:var(--line);border-radius:2px;margin-top:6px}
.dom{color:var(--ink2);font-size:12px}
.footer{margin-top:20px;padding-top:12px;border-top:1px solid var(--line);
  font-size:11.5px;color:var(--ink2)}
.footer code{font-family:var(--mono)}
.parsefail{color:var(--crit);font-family:var(--mono);font-size:12px}
ul.plain{list-style:none}
ul.plain li{padding:5px 0;border-top:1px solid var(--line);font-size:13px}
ul.plain li:first-child{border-top:0}
.tabs{display:flex;gap:2px;margin-bottom:16px;border-bottom:1px solid var(--line)}
.tabs button{font:inherit;font-size:13px;font-weight:600;letter-spacing:.03em;
  background:none;border:0;border-bottom:3px solid transparent;color:var(--ink2);
  padding:6px 14px 8px;cursor:pointer}
.tabs button[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--accent)}
.tabs button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.gloss{max-width:76ch}
.gloss .panel h3{font-size:14.5px;margin-bottom:6px}
.gloss .panel p{font-size:13.5px;line-height:1.55;margin-bottom:8px}
.gloss .panel p:last-child{margin-bottom:0}
.gloss .own{font-family:var(--mono);font-size:11px;color:var(--ink2)}
.gloss table{font-size:12.5px}
.gloss td:first-child{white-space:nowrap;font-weight:600}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px}
.tile{border:1px solid var(--line);border-left-width:4px;border-radius:4px;
  background:var(--panel);padding:9px 11px}
.tile.ok{border-left-color:var(--ok)}
.tile.watch{border-left-color:var(--watch)}
.tile.elev{border-left-color:var(--elev)}
.tile.crit{border-left-color:var(--crit)}
.tile .tn{font-size:10.5px;text-transform:uppercase;letter-spacing:.07em;
  color:var(--ink2);display:flex;justify-content:space-between}
.tile .tv{font-family:var(--mono);font-size:19px;font-weight:700;margin:1px 0}
.tile .tv .asof{font-size:10.5px;font-weight:400;color:var(--ink2);margin-left:5px}
.tile .td{font-family:var(--mono);font-size:11px;color:var(--ink2);line-height:1.5}
.tile .td b{color:var(--ink)}
"""

GLOSSARY = """
<div class="gloss">
<div class="panel"><h3>How to read this page in 20 seconds</h3>
<p><b>Pending Will</b> = the action is on you. <b>Needs attention</b> = the action is on
the fleet (worst first). <b>Fire ledger</b> = the tripwires armed on your behalf — every
one ends at your desk if it trips. <b>Catalyst runway</b> = what the calendar forces.
<b>Fleet grid</b> = who's healthy, who's drifting. Everything else is context.</p></div>

<div class="panel"><h3>"Gated" vs. a heat color — two different things</h3>
<p>A <b>gate</b> is a specific, pre-registered tripwire: a <i>measured threshold</i> + a
<i>fixed action</i> + a <i>state</i>. Example — <span class="chip watch">GATE-RESHAPE-BC</span>:
condition "HY OAS &gt;280 sustained OR WAL prints 7/21 AMC" → action "the bank-put reshape
proposal comes to you." It's written down <i>before</i> the fact so it can't be rationalized
after.</p>
<p>To call a risk <b>"gated"</b> means we've wired that plumbing — a defined trigger and a
defined response — so a live event produces a clean proposal at your desk instead of a
scramble. (Kharg was an <i>open hole</i> on Fri 7/18; <i>gated</i> by Sat — same risk, now with
a tripwire and a fire path.)</p>
<p>A <b>heat color</b> (green/yellow/orange/red) answers a different question: <i>how hot is
this right now.</i> A risk can be red-hot with no gate, or calm-yellow with a gate armed
underneath it. Gates <i>watch</i>; colors <i>describe</i>. And a gate firing <b>never</b>
executes a trade — it hands you a proposal.</p>
<p class="own">owner: PROME/GATES.tsv (the fire-ledger canon)</p></div>

<div class="panel"><h3>The fire ledger &amp; gate states</h3>
<p>A central register of every pre-registered <i>"if X happens, someone must DO
something"</i> rule — not predictions that merely get graded, only rules that owe an
<b>action</b> (build a packet, arm a trade card, bring you a proposal). PROME scans it at
every boot.</p>
<p>Born 2026-07-09 from a real failure: two VIOLET triggers fired on 7/2 into a frozen
session and the owed hedge-packet sat orphaned for seven days before an audit found it.
The ledger makes that structurally impossible — the watching is centralized even though
the trigger logic stays with the domain agents.</p>
<table><tr><td><span class="chip watch">LIVE</span></td><td>armed tripwire — condition
watched, not yet met</td></tr>
<tr><td><span class="chip crit">FIRED-UNEXECUTED</span></td><td>condition came TRUE and the
owed action hasn't happened — blocks all new PROME work until cleared or escalated to
you. Should never survive a session.</td></tr>
<tr><td><span class="chip ok">RESOLVED</span></td><td>condition tested, verdict landed,
consequence executed (or explicitly not owed)</td></tr>
<tr><td><span class="chip ok">LAPSED</span></td><td>fired but the action window passed —
your call, recorded, not retro-built</td></tr></table>
<p class="own">owner: PROME/GATES.tsv · full trigger logic stays in each owner's KB</p></div>

<div class="panel"><h3>Arm-#1 / #2 / #3</h3>
<p>The three independent <b>arming paths</b> for TERRY's duration/TLT-put fire card
(TRY-FIRE-004). Each is a different way the rates thesis can prove itself: #1 was an
auction-stress test (resolved NOT-FIRED 7/9), #2 is five consecutive 10Y closes ≥4.50,
#3 is foreign official selling in the TIC data. Any single arm completing → TERRY arms
the card → comes to you for [Approve] with the live broker book. "Armed" never means
"traded" — capital moves only on your explicit approval.</p>
<p class="own">owner: AGENTS/TERRY/setups/FLOW-TRIGGER_duration-TLT-put.md</p></div>

<div class="panel"><h3>A card's lifecycle: ARMED &rarr; FIRED &rarr; FILLED</h3>
<p>Three distinct stages — the words are not interchangeable, and only the last one moves
capital.</p>
<table>
<tr><td><span class="chip watch">ARMED</span></td><td>setup conditions met + the trade fully
<i>built</i> (strikes, ladder, $500 cap) — loaded, safety on. Never means "traded."</td></tr>
<tr><td><span class="chip elev">FIRED</span></td><td>the trigger condition crossed — the card
now owes you a proposal (TERRY live-re-marks the strikes against the current book)</td></tr>
<tr><td><span class="chip crit">FILLED</span></td><td>you gave [Approve] against a live broker
book and it executed. <b>You are the trigger, not the tape</b> — nothing reaches here on its
own.</td></tr></table>
<p>Worked example (July 2026, historical): TRY-FIRE-004's arm fired 7/13 → card ARMED. Will
first ruled <b>NO-ADD</b> (7/16 — the book already owned the grind), then approved a $330
re-fire on a clean red-day entry (7/20). Armed ≠ auto-fill in either direction — the fill
returns as a TERRY proposal, and the current card state lives in GATES/FORGE, never in this
example.</p>
<p class="own">owner: AGENTS/TERRY/setups/ (fire cards) · PROME/GATES.tsv (gate rows)</p></div>

<div class="panel"><h3>Break / Grind / Unresolved</h3>
<p><b>NEXUS's regime probability split</b> over the next 2–6 weeks — the one numeric
regime call in the system, deliberately owned by exactly one agent (PROME runs no
competing split, so you always know whose judgment you're reading).</p>
<p><b>Break</b> — the accumulated stress (rates-vol, credit fuel, record equity
complacency) cracks into an actual market repricing. <b>Grind</b> — the calm holds and
the stress dissipates or stays latent. <b>Unresolved</b> — the honest bucket: the window
ends and the tape still hasn't told us. A high Unresolved number means the decisive
tests are still ahead — watch the catalyst runway, not the noise.</p>
<p class="own">owner: AGENTS/NEXUS/STATUS.md (re-anchored after regime-moving events)</p></div>

<div class="panel"><h3>Status colors (fleet-wide key)</h3>
<table>
<tr><td><span class="chip ok">green</span></td><td>none / healthy / fresh</td></tr>
<tr><td><span class="chip watch">yellow</span></td><td>monitoring — armed or aging, no action owed yet</td></tr>
<tr><td><span class="chip elev">orange</span></td><td>elevated — deserves a look this session</td></tr>
<tr><td><span class="chip crit">red</span></td><td>active/critical — blocking or cold; act or escalate</td></tr></table>
<p>Same key everywhere in the repo (STATUS files, HEARTBEAT, this page). Color is never
the only signal — every chip carries its words.</p></div>

<div class="panel"><h3>Needs attention — how it's composed</h3>
<p>Auto-assembled at build time, worst first, from: fired-unexecuted gates · failing
health checks · live gates unchecked &gt;5d · HEARTBEAT blocking rows · active agents
cold (&gt;14d) or lagging (8–14d) · inboxes ≥8 deep · a stale spine audit (&gt;7d).
Nothing is hand-curated; if it's listed, a rule put it there. If this rail is ever
long every day, the thresholds need tuning — tell PROME.</p></div>

<div class="panel"><h3>Fleet grid columns</h3>
<p><b>Maturity</b> (L1–L5, DAEDALUS's scale): L1 scaffold just built → L2 first own
data pulls → L3 predictions resolving on a clock → L4 other agents consume its output
by name → L5 fully self-running periphery. <b>Last activity</b> = <b>business days</b>
("bd") since any commit touched the agent's directory (≤3 fresh · ≤7 aging · 8–14
lagging · &gt;14 cold — weekends don't age anyone). <b>30d commits</b> = volume of recent work.
<b>Inbox</b> = unprocessed items waiting (excludes processed/). <b>newborn</b> = built
within days, no track record yet — low bars are honest, not alarming. <b>parked →
date</b> = quiet by plan until that date (expiry-dated register, PROME/tools/
dashboard_parked.tsv); staleness flagging resumes automatically past the date, and
inbox flags still apply while parked.</p>
<p class="own">owners: PROME/ROSTER.md (classification) · AGENTS/DAEDALUS/FLEET_MAP.tsv (maturity)</p></div>

<div class="panel"><h3>Catalyst runway</h3>
<p>The canonical forward calendar (PROME/DOCKET.tsv) filtered to the next 21 days —
scheduled events that force a test or a decision: data prints, earnings, auctions,
policy meetings, gate-completion dates. Orange dates are ≤3 days out. When the regime
split is heavily "Unresolved," this list is where it resolves.</p></div>

<div class="panel"><h3>Shorthand that appears on this page</h3>
<table>
<tr><td>HY OAS / X1</td><td>high-yield credit spread (bps); &gt;280 sustained is the
pre-registered stress line ("X1"), &lt;260 twice re-kills the axis</td></tr>
<tr><td>HOLD FLAT</td><td>standing posture: no new capital deployed without a fired
trigger + your approval ($500/card max-loss)</td></tr>
<tr><td>COT</td><td>CFTC Commitments-of-Traders positioning data (weekly, Fri 3:30 PM)</td></tr>
<tr><td>[as-of] stamps</td><td>every number carries its observation date — a Friday
vintage shown on Sunday is disclosure, not an error; refresh before acting</td></tr>
<tr><td>fire card</td><td>a pre-built trade construction (TERRY) that sits shelved
until its gate fires — so decision speed never requires decision haste</td></tr>
<tr><td>env / firetime chips</td><td>boot health checks: machine keys present ·
fire-path artifacts free of date-drift/dead pointers (known-benigns allowlisted)</td></tr>
<tr><td>spine audit</td><td>weekly 7-reader (+1 anchor-leg) reconciliation of PROME's core
docs against canon — the age chip shows days since last run (&gt;7d = due)</td></tr></table></div>
</div>
"""

AGE_JS = """
(function(){
  var el=document.getElementById('agebadge');
  var t=Date.parse(el.getAttribute('data-generated'));
  function tick(){
    var h=(Date.now()-t)/36e5;
    var label=h<1?'built '+Math.round(h*60)+'m ago':'built '+(h<48?Math.round(h)+'h':Math.round(h/24)+'d')+' ago';
    el.textContent=label;
    el.className=h>72?'old':(h>24?'aged':'');
    el.id='agebadge';
    if(h>24) el.textContent=label+' — refresh before trusting';
  }
  tick(); setInterval(tick,600000);
})();
(function(){
  var tabs=document.querySelectorAll('.tabs button');
  tabs.forEach(function(b){b.addEventListener('click',function(){
    tabs.forEach(function(x){
      var on=x===b;
      x.setAttribute('aria-selected',on?'true':'false');
      document.getElementById(x.getAttribute('data-view')).hidden=!on;
    });
  });});
})();
"""


def chip(cls, text):
    return f'<span class="chip {cls}">{esc(text)}</span>'


def panel_guard(title, owner, fn):
    """Render a panel body; on parser failure render a loud pointer to canon."""
    try:
        return fn()
    except Exception as e:
        return (f'<div class="parsefail">⚠ PARSE FAILED ({esc(type(e).__name__)}: '
                f'{esc(str(e)[:120])}) — read {esc(owner)} directly.</div>')


def build(today, now_iso):
    active, tier2, dormant = parse_roster()
    fmap = parse_fleet_map()
    hb = parse_heartbeat()
    gates = parse_gates(today)
    docket = parse_docket(today)
    pending = parse_pending_will()
    spine_d, spine_age = parse_spine_stamp(today)
    env_rc = run_rc("env_doctor.py", "--quiet")
    fire_rc = run_rc("firetime_check.py", "--window", "7", "--quiet")
    try:
        tiles = parse_tiles(hb)
        tiles_err = None
    except Exception as e:
        tiles, tiles_err = [], f"{type(e).__name__}: {str(e)[:120]}"
    prev = load_prev_snapshot()

    # -- fleet rows (active roster, git-computed; staleness in BUSINESS days)
    parked = load_parked(today)
    fleet = []
    for name, dom in active:
        days, c30 = agent_git(name, today)
        # 8/16 (DAEDALUS sweep-1 URGENT-3): dir-traffic counted commits INTO the
        # agent's tree, so inbound packets read as agent health — grid said
        # all-31 "ok" while gate-wired agent_freshness read 8 STALE>7d (the
        # NEXUS 8/12 instrument defect). The grid now keys on the same
        # instrument the gate trusts: own-surface age (non-inbox), CALENDAR
        # days. agent_git stays for the 30d activity count only.
        if name == "PROME":
            # PROME's home is PROME/, not AGENTS/PROME (tree removed 7/24) —
            # the shared helper hardcodes AGENTS/<name> and returns None here.
            ts = agent_freshness.git("log", "-1", "--format=%ct", "--",
                                     "PROME", ":(exclude)PROME/inbox")
            own = (dt.datetime.now().timestamp() - int(ts)) / 86400 if ts else None
        else:
            own = agent_freshness.own_surface_age_days(name)
        days = None if own is None else round(own)
        depth = inbox_depth(name)
        lvl, conf = fmap.get(name, ("—", ""))
        is_parked = name in parked
        if is_parked:
            until, _ = parked[name]
            cls, word = "none", f"parked → {until.month}/{until.day}"
        elif days is None:
            cls, word = "crit", "no git history"
        elif days <= 3:
            cls, word = "ok", f"{days}d (own)"
        elif days <= 7:
            cls, word = "watch", f"{days}d (own)"
        elif days <= 14:
            cls, word = "elev", f"{days}d own — lagging"
        else:
            cls, word = "crit", f"{days}d own — cold"
        fleet.append({"name": name, "dom": dom, "days": 999 if days is None else days,
                      "word": word, "cls": cls, "c30": c30, "depth": depth,
                      "lvl": lvl, "conf": conf, "newborn": lvl == "L1",
                      "parked": is_parked})
    # stalest first; parked sink to the bottom (intentionally quiet ≠ needs eyes)
    fleet.sort(key=lambda r: (r["parked"], -r["days"]))

    # -- needs-attention items (composed, worst first)
    attn = []
    for g in gates:
        if g["kind"] == "crit":
            attn.append(("crit", f"{g['gate']} is FIRED-UNEXECUTED — clear or escalate "
                                 f"before any new work", "PROME/GATES.tsv"))
    if fire_rc != 0:
        attn.append(("crit", "firetime_check flagging (rc≠0) — a fire-path artifact "
                             "has a real defect (allowlist filters known-benigns)", "scripts/firetime_check.py"))
    if env_rc != 0:
        attn.append(("crit" if env_rc == -1 else "elev",
                     "env_doctor failing — machine-local keys/infra; fix before "
                     "citing FRED-dependent levels", "scripts/env_doctor.py"))
    # 8/16 (DAEDALUS sweep-1 item 12): the >5d raw-age rule was RETIRED by the
    # 8/7 forum ruling (consumed_by keys LIVE-row staleness) — the audit
    # re-keyed three surfaces and missed this fourth; ~8 stale-age flags were
    # firing here off the dead rule. Semantics mirror prome_gate's check:
    # NONE-declared rows are fine; flag an empty/undated cell or a passed
    # consumer date.
    # Semantics MIRROR prome_gate.check_gates_tsv exactly (one rule, two
    # surfaces): flag a PASSED leading consumer-date or an EMPTY cell; a
    # non-empty undated cell (PRICE:/EVENT:/NONE classes) is quiet.
    for g in gates:
        if g["kind"] != "live":
            continue
        cb = g["consumed_by"]
        mcb = re.match(r"(\d{4})-(\d{2})-(\d{2})", cb)
        if mcb and dt.date(*map(int, mcb.groups())) < today:
            attn.append(("elev", f"{g['gate']} consumer date {mcb.group(0)} PASSED — "
                                 "re-point or resolve (8/7 ruling)", "PROME/GATES.tsv"))
        elif not cb:
            attn.append(("elev", f"{g['gate']} consumed_by EMPTY (required since 8/7)",
                         "PROME/GATES.tsv"))
    for b in hb["blocking"]:
        if b["cls"] in ("crit", "elev"):
            attn.append((b["cls"], b["text"], b["ref"]))
    for r in fleet:
        if r["cls"] == "crit" and not r["newborn"]:
            attn.append(("crit", f"{r['name']} cold — {r['word']} (active roster)",
                         f"AGENTS/{r['name']}/STATUS.md"))
        elif r["cls"] == "elev":
            attn.append(("elev", f"{r['name']} lagging — {r['word']}",
                         f"AGENTS/{r['name']}/STATUS.md"))
    for r in fleet:
        if r["depth"] >= 8:
            attn.append(("watch", f"{r['name']} inbox at {r['depth']} — drain owed",
                         f"AGENTS/{r['name']}/inbox/"))
    if spine_age is not None and spine_age > 7:
        attn.append(("elev", f"Spine audit stale ({spine_age}d) — run "
                             "spine_audit.workflow.js", "PROME/STATUS.md"))
    for b in hb["blocking"]:
        if b["cls"] == "watch":
            attn.append(("watch", b["text"], b["ref"]))
    order = {"crit": 0, "elev": 1, "watch": 2}
    attn.sort(key=lambda a: order.get(a[0], 3))

    live_gates = [g for g in gates if g["kind"] == "live"]
    recent_resolved = [g for g in gates if g["kind"] == "resolved"
                       and g["checked_age"] is not None and g["checked_age"] <= 7]

    cur_snapshot = make_snapshot(now_iso, hb, gates, docket, fleet, pending, tiles)
    delta = diff_snapshots(prev, cur_snapshot) if prev else None

    # ---------------------------------------------------------------- html --
    def render_channels():
        cards = ""
        for c in hb["channels"]:
            cards += (f'<div class="card {c["cls"]}"><div class="nm">{esc(c["name"])}</div>'
                      f'<div class="hd chip {c["cls"]}">{esc(c["headline"][:60])}</div>'
                      f'<div class="bd">{esc(c["body"])}</div></div>')
        return cards or '<div class="parsefail">⚠ no channels parsed — read HEARTBEAT.md</div>'

    def render_ticker():
        if not hb["ticker"]:
            return '<div class="parsefail">⚠ no ticker parsed — read HEARTBEAT.md stress dashboard</div>'
        return "".join(f'<span><b>{esc(t.split(" ")[0])}</b> {esc(" ".join(t.split(" ")[1:]))}</span>'
                       for t in hb["ticker"])

    def render_attn():
        if not attn:
            return '<li><span class="chip ok">CLEAR</span> Nothing needs attention right now.</li>'
        out = ""
        for cls, text, src in attn[:14]:
            out += (f'<li><span class="tag {cls}">{esc(cls)}</span>'
                    f'<span>{esc(text)}<span class="src">{esc(src)}</span></span></li>')
        if len(attn) > 14:
            out += (f'<li><span class="tag none">+{len(attn) - 14}</span>'
                    f'<span class="muted">more items not shown — no silent caps; '
                    f'see owner files</span></li>')
        return out

    def render_gates():
        out = ""
        for g in live_gates:
            age = f' · checked {g["checked_age"]}d ago' if g["checked_age"] is not None else ""
            out += (f'<li><span class="tag watch">LIVE</span><span><b>{esc(g["gate"])}</b> '
                    f'<span class="muted">({esc(g["owner"])}{age})</span><br>'
                    f'<span class="muted">{esc(trunc(g["cond"], 150))}</span></span></li>')
        for g in recent_resolved:
            word = g["state"].split(" ")[0]
            out += (f'<li><span class="tag ok">DONE</span><span class="muted">'
                    f'<b>{esc(g["gate"])}</b> — {esc(word)} (last 7d)</span></li>')
        return out or "<li class='muted'>no gates registered</li>"

    def render_pending():
        if not pending:
            return "<li class='muted'>none parsed — see PROME/SCRATCH.md cautions</li>"
        return "".join(f'<li>{esc(p)}</li>' for p in pending)

    def render_runway():
        out = ""
        for r in docket:
            d = r["start"].strftime("%a %-m/%-d") + ("+" if r["span"] else "")
            soon = ' class="soon"' if r["days_out"] <= 3 else ""
            if r["days_out"] < 0:
                when = "live now"       # multi-day window already in progress
            elif r["days_out"] == 0:
                when = "today"
            else:
                when = f'in {r["days_out"]}d'
            out += (f'<li{soon}><span class="d">{esc(d)}</span>'
                    f'<span class="in">{esc(when)}</span><span>{esc(trunc(r["catalyst"], 110))}'
                    f'<br><span class="own">{esc(r["owners"])}</span></span></li>')
        return out or "<li class='muted'>nothing in the next 21 days</li>"

    def render_tiles():
        if tiles_err:
            return (f'<div class="parsefail">⚠ PARSE FAILED ({esc(tiles_err)}) — read '
                    f'HEARTBEAT.md stress dashboard + FORGE/tools/market-data/config.py.</div>')
        if not tiles:
            return ('<div class="parsefail">⚠ no ticker↔band matches parsed — read '
                    'HEARTBEAT.md stress dashboard.</div>')
        out = ""
        for t in tiles:
            out += (f'<div class="tile {t["cls"]}"><div class="tn"><span>{esc(t["name"])}'
                    f'</span><span>{esc(t["dir"])}</span></div>'
                    f'<div class="tv">{esc(_fmt(t["val"]))}'
                    f'<span class="asof">[{esc(t["stamp"])}]</span></div>'
                    f'<div class="td"><b>{esc(t["dist"])}</b><br>'
                    f'y {esc(_fmt_rng(t["yellow"]))} · r {esc(_fmt_rng(t["red"]))}</div></div>')
        return out

    def render_delta():
        if prev is None:
            return ('<li><span class="tag none">FIRST</span><span class="muted">'
                    'first tracked build — deltas begin next build</span></li>')
        if not delta:
            return ('<li><span class="tag ok">NONE</span><span class="muted">'
                    'no canon-state changes since the last build</span></li>')
        word = {"ok": "done", "none": "info"}
        out = ""
        for cls, text in delta[:16]:
            out += (f'<li><span class="tag {cls}">{esc(word.get(cls, cls))}</span>'
                    f'<span>{esc(text)}</span></li>')
        if len(delta) > 16:
            out += (f'<li><span class="tag none">+{len(delta) - 16}</span>'
                    f'<span class="muted">more deltas not shown — no silent caps</span></li>')
        return out

    def render_fleet():
        rows = ""
        maxc = max((r["c30"] for r in fleet), default=1) or 1
        for r in fleet:
            nb = ' <span class="chip ok">newborn</span>' if r["newborn"] else ""
            # sqrt scale: PROME's coordinator volume shouldn't flatten everyone
            # else to slivers — perceptual, not proportional (labels carry truth)
            w = max(3, int(64 * (min(r["c30"], maxc) / maxc) ** 0.5))
            rows += (f'<tr><td class="agent">{esc(r["name"])}{nb}</td>'
                     f'<td class="dom">{esc(trunc(r["dom"], 70))}</td>'
                     f'<td class="lvl">{esc(r["lvl"])}</td>'
                     f'<td><span class="chip {r["cls"]}">{esc(r["word"])}</span></td>'
                     f'<td class="num">{r["c30"]}<div class="barwrap">'
                     f'<div class="bar30" style="width:{w}px"></div></div></td>'
                     f'<td class="num">{r["depth"] or "—"}</td></tr>')
        return rows

    spine_chip = (chip("ok", f"spine audit {spine_age}d") if spine_age is not None and spine_age <= 7
                  else chip("elev", f"spine audit {spine_age}d" if spine_age is not None else "spine audit ?"))
    # empty-panel tripwire (DAEDALUS 7/28 audit): a parser regression must show as
    # a header chip, never as a quiet page — finding_silent_blank_evades_review
    empty_panels = [n for n, v in (("one-liner", hb["one"]), ("channels", hb["channels"]),
                                   ("ticker", hb["ticker"]), ("tiles", tiles)) if not v]
    panels_chip = (chip("crit", f'{len(empty_panels)} panel(s) EMPTY: {", ".join(empty_panels)}')
                   if empty_panels else "")
    tier2_names = " · ".join(n for n, _ in tier2)
    dormant_names = " · ".join(n for n, _ in dormant)

    page = f"""<title>Fleet Ops — PROME</title>
<style>{CSS}</style>
<div class="bar">
  <h1>FLEET OPS · PROME</h1>
  <span class="stamp mono">{esc(now_iso)} ET · HEARTBEAT base {esc(hb["base"])}</span>
  <span id="agebadge" data-generated="{esc(now_iso_utc)}">built just now</span>
  <div class="chips">
    {chip("ok" if env_rc == 0 else "crit", "env " + ("✓" if env_rc == 0 else "✗"))}
    {chip("ok" if fire_rc == 0 else "crit", "firetime " + ("✓" if fire_rc == 0 else "✗"))}
    {spine_chip}
    {panels_chip}
  </div>
</div>

<nav class="tabs" role="tablist">
  <button role="tab" aria-selected="true" data-view="view-ops">Operations</button>
  <button role="tab" aria-selected="false" data-view="view-gloss">Glossary</button>
</nav>

<div id="view-ops" role="tabpanel" aria-label="Operations">
<section class="regime">
  <div class="oneliner">{f'“{esc(hb["one"])}”' if hb["one"] else '<span class="parsefail">⚠ one-liner not parsed — read HEARTBEAT.md</span>'}<span class="split">{esc(hb["split"])}</span></div>
  <div class="cards">{panel_guard("regime", "HEARTBEAT.md", render_channels)}</div>
  <div class="ticker">{panel_guard("ticker", "HEARTBEAT.md", render_ticker)}</div>
</section>

<div class="panel"><h2>Gate distance — HEARTBEAT levels vs FORGE bands</h2>
  <div class="tiles">{panel_guard("tiles", "HEARTBEAT.md + FORGE config.py", render_tiles)}</div>
  <p class="muted" style="font-size:11.5px;margin-top:9px">Levels come from the HEARTBEAT
  stress dashboard with their [as-of] stamps — a stale stamp means canon needs refreshing,
  not this page. Bands come from <code>FORGE/tools/market-data/config.py</code> (canon
  absolute thresholds); gate-specific trigger lines (e.g. the 4.50 arm-#2 rule) live in the
  fire ledger below and are not restated here.</p></div>

<div class="cols">
<div>
  <div class="panel"><h2>Since last build{esc(" — vs " + prev["built"]) if prev else ""}</h2>
    <ul class="attn">{panel_guard("delta", "PROME/tools/dashboard_state.json", render_delta)}</ul></div>
  <div class="panel"><h2>Needs attention</h2>
    <ul class="attn">{render_attn()}</ul></div>
  <div class="panel"><h2>Pending Will</h2>
    <ul class="plain">{panel_guard("pending", "PROME/SCRATCH.md", render_pending)}</ul></div>
  <div class="panel"><h2>Fire ledger — live gates</h2>
    <ul class="attn">{panel_guard("gates", "PROME/GATES.tsv", render_gates)}</ul></div>
</div>
<div>
  <div class="panel"><h2>Catalyst runway — next 21 days</h2>
    <ul class="runway">{panel_guard("runway", "PROME/DOCKET.tsv", render_runway)}</ul></div>
  <div class="panel"><h2>Fleet — {len(fleet)} active (stalest first)</h2>
    <div class="tablewrap"><table>
      <tr><th>Agent</th><th>Domain</th><th>Maturity</th><th>Last activity</th>
      <th>30d commits</th><th>Inbox</th></tr>
      {panel_guard("fleet", "PROME/ROSTER.md", render_fleet)}
    </table></div>
    <p class="footer" style="margin-top:10px;border:0;padding:0">Tier-2 (spawn as needed):
    {esc(tier2_names)} &nbsp;·&nbsp; Dormant: {esc(dormant_names)}</p></div>
</div>
</div>
</div>

<div id="view-gloss" role="tabpanel" aria-label="Glossary" hidden>{GLOSSARY}</div>

<div class="footer">
  Generated surface — <b>points into canon, never owns it</b>. Owner files win on any
  disagreement: <code>HEARTBEAT.md</code> (regime) · <code>PROME/GATES.tsv</code> (gates) ·
  <code>PROME/DOCKET.tsv</code> (catalysts) · <code>PROME/ROSTER.md</code> +
  <code>AGENTS/DAEDALUS/FLEET_MAP.tsv</code> (fleet) · <code>AGENTS/&lt;NAME&gt;/STATUS.md</code>
  (agent state). Position/trade data excluded by design (position truth is off-repo).
  Market levels carry their [as-of] stamps — weekend/stale vintages are shown, not hidden.
  Regenerate: <code>python3 PROME/tools/fleet_dashboard.py</code> → republish (same URL).
</div>
<script>{AGE_JS}</script>
"""
    return page, cur_snapshot


def main():
    global now_iso_utc
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--out", default="/tmp/fleet_dashboard.html")
    args = ap.parse_args()
    now = dt.datetime.now()
    now_iso_utc = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    html_out, snap = build(now.date(), now.strftime("%Y-%m-%d %H:%M"))
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(html_out)
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(snap, f, indent=1, sort_keys=True)
        f.write("\n")
    print(f"wrote {args.out} ({len(html_out)//1024}KB) + state snapshot "
          f"({os.path.relpath(STATE_PATH, REPO)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
