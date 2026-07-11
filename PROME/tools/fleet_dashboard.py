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
   a new URL and orphans Will's tab. finding_artifact_redeploy_same_url.)
"""
import argparse
import datetime as dt
import html
import os
import re
import subprocess
import sys

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


EMOJI_CLASS = {"🟢": "ok", "🟡": "watch", "🟠": "elev", "🔴": "crit"}


def status_class(text, default="watch"):
    for e, c in EMOJI_CLASS.items():
        if e in text:
            return c
    return default


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


def agent_git(name):
    """(days_since_last_commit_to_dir, commits_30d) — dir-based activity."""
    path = "PROME/" if name == "PROME" else f"AGENTS/{name}/"
    ts = sh(["git", "log", "-1", "--format=%ct", "--", path])
    days = None
    if ts:
        days = (dt.datetime.now() - dt.datetime.fromtimestamp(int(ts))).days
    n = sh(["git", "rev-list", "--count", "--since=30.days", "HEAD", "--", path])
    return days, int(n) if n.isdigit() else 0


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
        head = state.split("(")[0].strip()
        kind = ("crit" if head.startswith("FIRED-UNEXECUTED")
                else "resolved" if head.startswith(("RESOLVED", "LAPSED", "RETIRED"))
                else "live")
        age = None
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})", last_checked.strip())
        if m:
            age = (today - dt.date(*map(int, m.groups()))).days
        rows.append({"gate": gate.strip(), "owner": owner.strip(), "kind": kind,
                     "state": md_clean(state)[:220], "cond": md_clean(cond)[:160],
                     "checked_age": age})
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
    m = re.search(r'"([^"]+)"', text)
    if m:
        one = m.group(1)
    split = ""
    m = re.search(r"Break \d+ / Grind \d+ / Unresolved \d+", text)
    if m:
        split = m.group(0)
    channels = []
    for m in re.finditer(r"^\d+\.\s+\*\*(.+?)\*\*(.*)$", text, re.M):
        head = m.group(1)
        name = md_clean(head.split("—")[0])
        cls = status_class(head, "watch")
        headline = md_clean(head.split("—", 1)[1] if "—" in head else head)
        body = md_clean(m.group(2))[:230]
        channels.append({"name": name, "cls": cls, "headline": headline, "body": body})
    ticker = []
    m = re.search(r"## Stress dashboard.*?\n\n(.+?)\n\n", text, re.S)
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
    return [md_clean(x) for x in m.group(1).split("·") if x.strip()]


def parse_spine_stamp(today):
    m = re.search(r"\*\*Last spine audit:\*\* (\d{4}-\d{2}-\d{2})", read("PROME/STATUS.md"))
    if not m:
        return None, None
    d = dt.date.fromisoformat(m.group(1))
    return d, (today - d).days


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

    # -- fleet rows (active roster, git-computed)
    fleet = []
    for name, dom in active:
        days, c30 = agent_git(name)
        depth = inbox_depth(name)
        lvl, conf = fmap.get(name, ("—", ""))
        if days is None:
            cls, word = "crit", "no git history"
        elif days <= 3:
            cls, word = "ok", f"{days}d ago"
        elif days <= 7:
            cls, word = "watch", f"{days}d ago"
        elif days <= 14:
            cls, word = "elev", f"{days}d — lagging"
        else:
            cls, word = "crit", f"{days}d — cold"
        fleet.append({"name": name, "dom": dom, "days": 999 if days is None else days,
                      "word": word, "cls": cls, "c30": c30, "depth": depth,
                      "lvl": lvl, "conf": conf, "newborn": lvl == "L1"})
    fleet.sort(key=lambda r: -r["days"])

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
    for g in gates:
        if g["kind"] == "live" and g["checked_age"] is not None and g["checked_age"] > 5:
            attn.append(("elev", f"{g['gate']} last checked {g['checked_age']}d ago "
                                 f"(boot rule: refresh at >5d)", "PROME/GATES.tsv"))
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

    # ---------------------------------------------------------------- html --
    def render_channels():
        cards = ""
        for c in hb["channels"]:
            cards += (f'<div class="card {c["cls"]}"><div class="nm">{esc(c["name"])}</div>'
                      f'<div class="hd chip {c["cls"]}">{esc(c["headline"][:60])}</div>'
                      f'<div class="bd">{esc(c["body"])}</div></div>')
        return cards or '<div class="parsefail">⚠ no channels parsed — read HEARTBEAT.md</div>'

    def render_ticker():
        return "".join(f'<span><b>{esc(t.split(" ")[0])}</b> {esc(" ".join(t.split(" ")[1:]))}</span>'
                       for t in hb["ticker"])

    def render_attn():
        if not attn:
            return '<li><span class="chip ok">CLEAR</span> Nothing needs attention right now.</li>'
        out = ""
        for cls, text, src in attn[:14]:
            out += (f'<li><span class="tag {cls}">{esc(cls)}</span>'
                    f'<span>{esc(text)}<span class="src">{esc(src)}</span></span></li>')
        return out

    def render_gates():
        out = ""
        for g in live_gates:
            age = f' · checked {g["checked_age"]}d ago' if g["checked_age"] is not None else ""
            out += (f'<li><span class="tag watch">LIVE</span><span><b>{esc(g["gate"])}</b> '
                    f'<span class="muted">({esc(g["owner"])}{age})</span><br>'
                    f'<span class="muted">{esc(g["cond"][:150])}</span></span></li>')
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
            when = "today" if r["days_out"] == 0 else f'in {r["days_out"]}d'
            out += (f'<li{soon}><span class="d">{esc(d)}</span>'
                    f'<span class="in">{esc(when)}</span><span>{esc(r["catalyst"][:110])}'
                    f'<br><span class="own">{esc(r["owners"])}</span></span></li>')
        return out or "<li class='muted'>nothing in the next 21 days</li>"

    def render_fleet():
        rows = ""
        maxc = max((r["c30"] for r in fleet), default=1) or 1
        for r in fleet:
            nb = ' <span class="chip ok">newborn</span>' if r["newborn"] else ""
            w = max(3, int(64 * min(r["c30"], maxc) / maxc))
            rows += (f'<tr><td class="agent">{esc(r["name"])}{nb}</td>'
                     f'<td class="dom">{esc(r["dom"][:70])}</td>'
                     f'<td class="lvl">{esc(r["lvl"])}</td>'
                     f'<td><span class="chip {r["cls"]}">{esc(r["word"])}</span></td>'
                     f'<td class="num">{r["c30"]}<div class="barwrap">'
                     f'<div class="bar30" style="width:{w}px"></div></div></td>'
                     f'<td class="num">{r["depth"] or "—"}</td></tr>')
        return rows

    spine_chip = (chip("ok", f"spine audit {spine_age}d") if spine_age is not None and spine_age <= 7
                  else chip("elev", f"spine audit {spine_age}d" if spine_age is not None else "spine audit ?"))
    tier2_names = " · ".join(n for n, _ in tier2)
    dormant_names = " · ".join(n for n, _ in dormant)

    return f"""<title>Fleet Ops — PROME</title>
<style>{CSS}</style>
<div class="bar">
  <h1>FLEET OPS · PROME</h1>
  <span class="stamp mono">{esc(now_iso)} ET · HEARTBEAT base {esc(hb["base"])}</span>
  <span id="agebadge" data-generated="{esc(now_iso_utc)}">built just now</span>
  <div class="chips">
    {chip("ok" if env_rc == 0 else "crit", "env " + ("✓" if env_rc == 0 else "✗"))}
    {chip("ok" if fire_rc == 0 else "crit", "firetime " + ("✓" if fire_rc == 0 else "✗"))}
    {spine_chip}
  </div>
</div>

<section class="regime">
  <div class="oneliner">“{esc(hb["one"])}”<span class="split">{esc(hb["split"])}</span></div>
  <div class="cards">{panel_guard("regime", "HEARTBEAT.md", render_channels)}</div>
  <div class="ticker">{panel_guard("ticker", "HEARTBEAT.md", render_ticker)}</div>
</section>

<div class="cols">
<div>
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


def main():
    global now_iso_utc
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--out", default="/tmp/fleet_dashboard.html")
    args = ap.parse_args()
    now = dt.datetime.now()
    now_iso_utc = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    html_out = build(now.date(), now.strftime("%Y-%m-%d %H:%M"))
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"wrote {args.out} ({len(html_out)//1024}KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
