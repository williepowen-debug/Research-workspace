#!/usr/bin/env python3
"""
will_handbook.py — THE HELM (renamed from "Operator Handbook", Will's word 2026-08-21
— the page outgrew the name once the brief moved in; same URL, same favicon 📖 for
tab continuity). Will's command seat: desk · brief · manual.

Renders PROME/HANDBOOK.md (hand-written manual + curated priorities) plus two
GENERATED live sections — Waiting on you (WILL_QUEUE) and The clock (DOCKET) —
reusing will_brief.py's parsers so the fleet keeps ONE queue-parser family
(gate + brief already agree via queue_parser_selftest; this page IMPORTS the
brief's parser rather than becoming a third copy).

Prior-art line (CHECK_STANDARD draft norm, honored voluntarily): symptom
"Will needs a living cheat-sheet page" searched against MEMORY/INDEX_COLD/
PATTERNS — no existing mechanism; DONOR = will_brief.py (page-generator
pattern, 3rd instance after fleet_dashboard/will_brief).

Usage:
  python3 PROME/tools/will_handbook.py -o /path/out.html
Then publish via the Artifact tool to ARTIFACT_URL below (pass url= from any
session other than the minting one — else it orphans Will's tab).

ARTIFACT_URL: https://claude.ai/code/artifact/ee088d08-bf26-48ab-bad2-7ee9155da12a

Verdict (CHECK_STANDARD §8): keyed on COUNTS returned by the render legs,
never on scraping output for glyphs. rc=0 OK · rc=1 REVIEW (a leg failed or
rendered empty — the page still writes, degraded honestly).
"""
import argparse
import csv
import datetime as dt
import html
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import will_brief as wb  # noqa: E402  (parsers + md_inline; ONE parser family)

ROOT = Path(__file__).resolve().parents[2]
HANDBOOK = ROOT / "PROME" / "HANDBOOK.md"
FLEETOPS_URL = "https://claude.ai/code/artifact/c884f088-4936-44a0-9232-30851b9427b6"

ALERTS = []  # (leg, reason) — the verdict keys on this count


def alert(leg, reason):
    ALERTS.append((leg, reason))


# ---------- HANDBOOK.md parsing ------------------------------------------------

def parse_handbook():
    """Split on '## ' headers → ordered [(title, body)]. Header line 1 + the
    bold preamble are tooling-facing and skipped (everything before first ##)."""
    try:
        text = HANDBOOK.read_text(encoding="utf-8")
    except Exception as e:
        alert("handbook", f"HANDBOOK.md unreadable: {e}")
        return []
    sections = []
    for chunk in re.split(r"(?m)^## ", text)[1:]:
        title, _, body = chunk.partition("\n")
        sections.append((title.strip(), body.strip()))
    if not sections:
        alert("handbook", "HANDBOOK.md parsed to zero sections")
    return sections


def render_table(lines):
    rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lines]
    rows = [r for r in rows if not all(re.fullmatch(r":?-+:?", c or "-") for c in r)]
    if not rows:
        return ""
    head, body = rows[0], rows[1:]
    out = ["<div class='tw'><table><tr>"]
    out += [f"<th>{wb.md_inline(c)}</th>" for c in head]
    out.append("</tr>")
    for r in body:
        out.append("<tr>" + "".join(f"<td>{wb.md_inline(c)}</td>" for c in r) + "</tr>")
    out.append("</table></div>")
    return "".join(out)


def render_body(body):
    """Paragraphs, '- ' bullets, markdown tables. No nesting — by design."""
    out, buf, i = [], [], 0
    lines = body.splitlines()

    def flush():
        if buf:
            out.append("<p>" + wb.md_inline(" ".join(buf)) + "</p>")
            buf.clear()

    while i < len(lines):
        ln = lines[i].strip()
        if ln.startswith("|"):
            flush()
            tbl = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl.append(lines[i]); i += 1
            out.append(render_table(tbl))
            continue
        if ln.startswith("- "):
            flush()
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(lines[i].strip()[2:]); i += 1
            out.append("<ul>" + "".join(f"<li>{wb.md_inline(x)}</li>" for x in items) + "</ul>")
            continue
        if ln:
            buf.append(ln)
        else:
            flush()
        i += 1
    flush()
    return "".join(out)


# ---------- page ---------------------------------------------------------------

CSS = """
*,*::before,*::after{box-sizing:border-box}
:root{
  --ground:#EFEDE6; --panel:#F8F6EF; --line:#D6D2C2; --line-soft:#E4E0D2;
  --ink:#23271F; --dim:#5E6355; --faint:#8B9083;
  --accent:#3E6B4E; --accent-soft:#E1EAE0;
  --warn:#9A6612; --crit:#A4342A; --crit-bg:#F5E0DC;
  --serif:Georgia,'Iowan Old Style','Palatino Linotype',serif;
  --sans:system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',sans-serif;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ground:#12160E; --panel:#1A1F15; --line:#2C3226; --line-soft:#20261B;
  --ink:#E4E7DE; --dim:#9CA394; --faint:#6F766A;
  --accent:#85BC93; --accent-soft:#24301F;
  --warn:#DCA84A; --crit:#EC7166; --crit-bg:#2E1917;
}}
:root[data-theme="dark"]{
  --ground:#12160E; --panel:#1A1F15; --line:#2C3226; --line-soft:#20261B;
  --ink:#E4E7DE; --dim:#9CA394; --faint:#6F766A;
  --accent:#85BC93; --accent-soft:#24301F;
  --warn:#DCA84A; --crit:#EC7166; --crit-bg:#2E1917;
}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);
  font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
.wrap{max-width:46rem;margin:0 auto;padding:2.4rem 1.25rem 5rem;
  display:flex;flex-direction:column;gap:2.1rem}
code{font-family:var(--mono);font-size:.88em;background:var(--line-soft);
  padding:.1em .35em;border-radius:3px}
a{color:var(--accent)}
.mast{border-bottom:2px solid var(--accent);padding-bottom:1rem;
  display:flex;flex-direction:column;gap:.45rem}
.eyebrow{font-size:.68rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--accent);font-weight:700}
.mast h1{font-family:var(--serif);font-weight:400;letter-spacing:-.01em;
  font-size:clamp(1.7rem,5vw,2.3rem);margin:0;text-wrap:balance}
.clocks{font-family:var(--mono);font-size:.72rem;color:var(--faint);
  display:flex;flex-wrap:wrap;gap:.4rem .9rem}
section{display:flex;flex-direction:column;gap:.8rem}
h2{font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;margin:0;
  color:var(--faint);font-weight:700;display:flex;align-items:center;gap:.6rem}
h2::after{content:"";flex:1;height:1px;background:var(--line)}
p,ul{margin:0;font-size:.95rem}
ul{padding-left:1.15rem;display:flex;flex-direction:column;gap:.45rem}
.live{background:var(--panel);border:1px solid var(--line);border-radius:6px;
  padding:1rem 1.15rem;display:flex;flex-direction:column;gap:.75rem}
.live .decision{border-left:3px solid var(--accent);background:var(--accent-soft);
  border-radius:4px;padding:.6rem .8rem;display:flex;flex-direction:column;gap:.15rem}
.live .decision .n{font-family:var(--mono);font-size:.68rem;color:var(--dim)}
.live .decision .t{font-weight:600;font-size:.93rem}
.live .decision .r{font-size:.8rem;color:var(--dim)}
.live .none{font-style:italic;color:var(--dim);font-size:.92rem}
.chore{display:flex;gap:.6rem;align-items:baseline;font-size:.85rem;color:var(--dim)}
.chore .w{font-family:var(--mono);font-size:.68rem;color:var(--faint);white-space:nowrap}
.days{list-style:none;padding:0;display:flex;flex-direction:column}
.days li{display:grid;grid-template-columns:4.6rem 1fr auto;gap:.8rem;
  align-items:baseline;padding:.5rem 0;border-bottom:1px solid var(--line-soft);
  font-size:.9rem}
.days li:last-child{border-bottom:none}
.days .when{font-family:var(--mono);font-size:.76rem;color:var(--dim);white-space:nowrap}
.days .in{font-family:var(--mono);font-size:.68rem;color:var(--faint);white-space:nowrap}
.days li.star .when{color:var(--accent);font-weight:700}
.tw{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:.88rem}
th{text-align:left;font-size:.66rem;text-transform:uppercase;letter-spacing:.08em;
  color:var(--faint);padding:.3rem .6rem .4rem;border-bottom:1px solid var(--ink)}
td{padding:.42rem .6rem;border-bottom:1px solid var(--line-soft);vertical-align:top}
.degraded{background:var(--crit-bg);color:var(--crit);border-radius:5px;
  padding:.7rem .9rem;font-size:.85rem;font-family:var(--mono)}
footer{font-size:.72rem;color:var(--faint);line-height:1.7;
  border-top:1px solid var(--line);padding-top:1rem}
.sum{font-family:var(--mono);font-size:.86rem;color:var(--accent);font-weight:600}
.subhead{font-size:.66rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--faint);font-weight:700;border-top:1px solid var(--line-soft);
  padding-top:.6rem;margin-top:.1rem}
.spawns{display:flex;flex-direction:column;gap:.55rem}
.spawn{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);
  border-radius:5px;padding:.65rem .85rem;display:flex;flex-direction:column;gap:.3rem}
.spawn .top{display:flex;justify-content:space-between;align-items:baseline;gap:.6rem}
.spawn .nm{font-weight:700;font-size:.95rem;letter-spacing:.03em}
.chip{font-family:var(--mono);font-size:.68rem;color:var(--dim);white-space:nowrap;
  border:1px solid var(--line);border-radius:3px;padding:.05rem .45rem}
.chip.warn{color:var(--warn);border-color:var(--warn);font-weight:700}
.spawn .cmd{align-self:flex-start;font-size:.78rem}
.spawn .why{font-size:.84rem;color:var(--dim)}
.hint{font-size:.78rem;color:var(--faint);font-style:italic}
.toc{display:flex;flex-wrap:wrap;gap:.35rem .5rem}
.toc a{font-family:var(--mono);font-size:.72rem;text-decoration:none;color:var(--dim);
  border:1px solid var(--line);border-radius:3px;padding:.15rem .55rem;background:var(--panel)}
.toc a:hover,.toc a:focus-visible{color:var(--accent);border-color:var(--accent)}
.bhead{font-family:var(--serif);font-weight:400;font-size:1.22rem;line-height:1.5;
  margin:0;text-wrap:balance}
.bclocks{font-family:var(--mono);font-size:.7rem;color:var(--faint);
  display:flex;flex-wrap:wrap;gap:.35rem .9rem}
.prose{font-family:var(--serif);font-size:1.01rem;line-height:1.66}
.prose p{margin:0 0 .85rem}.prose p:last-child{margin-bottom:0}
.pull{font-family:var(--serif);font-size:1.08rem;line-height:1.5;margin:0;
  padding:.8rem 0 .8rem 1rem;border-left:3px solid var(--accent)}
.falsify{background:var(--accent-soft);border-radius:5px;padding:.9rem 1.05rem;
  display:flex;flex-direction:column;gap:.45rem}
.falsify .lead{font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--accent);font-weight:700}
.feed{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}
.feed li{display:grid;grid-template-columns:5rem 1fr;gap:.8rem;align-items:baseline;
  padding:.45rem 0;border-bottom:1px solid var(--line-soft);font-size:.88rem}
.feed li:last-child{border-bottom:none}
.feed .ago{font-family:var(--mono);font-size:.68rem;color:var(--faint);
  white-space:nowrap;text-transform:uppercase;letter-spacing:.05em}
.book{display:flex;flex-wrap:wrap;gap:1.4rem;align-items:flex-end;
  padding:.85rem 1rem;background:var(--panel);border:1px solid var(--line);border-radius:5px}
.stat{display:flex;flex-direction:column;gap:.1rem}
.stat .v{font-family:var(--mono);font-size:1.22rem;font-variant-numeric:tabular-nums;
  font-weight:600;line-height:1.1}
.stat .k{font-size:.64rem;letter-spacing:.12em;text-transform:uppercase;color:var(--faint)}
.vint{font-size:.7rem;color:var(--faint);font-family:var(--mono);flex-basis:100%}
.vint.stale{color:var(--warn)}
.tabs{display:flex;gap:2px;border-bottom:1px solid var(--line)}
.tabs button{font:inherit;font-size:.82rem;font-weight:700;letter-spacing:.06em;
  text-transform:uppercase;background:none;border:0;color:var(--faint);
  border-bottom:3px solid transparent;padding:.45rem 1rem .6rem;cursor:pointer}
.tabs button[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--accent)}
.tabs button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
[role="tabpanel"][hidden]{display:none}
[role="tabpanel"]{display:flex;flex-direction:column;gap:2.1rem}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
.board{background:var(--panel);border:1px solid var(--line);border-radius:6px;
  padding:.6rem .9rem;display:flex;flex-direction:column;gap:.35rem;font-size:.84rem}
.board .regime{display:flex;flex-wrap:wrap;gap:.15rem .85rem;align-items:baseline}
.board .regime b{font-weight:600}
.board .asof{font-family:var(--mono);font-size:.68rem;color:var(--faint)}
.board .gline{font-family:var(--mono);font-size:.74rem;color:var(--dim)}
.board .fired{background:var(--crit-bg);color:var(--crit);border-radius:4px;
  padding:.45rem .6rem;font-size:.82rem}
.board .fired .gid{font-family:var(--mono);font-weight:700}
.chip.ran{color:var(--accent);border-color:var(--accent)}
.days details.more{display:inline}
.days details.more summary{cursor:pointer;list-style:none;display:inline;
  font-family:var(--mono);font-size:.68rem;color:var(--accent)}
.days details.more summary::-webkit-details-marker{display:none}
.days .alsorow{font-size:.8rem;color:var(--dim);padding:.15rem 0 .15rem .8rem;
  border-left:2px solid var(--line-soft);margin-top:.25rem}
.in.past{color:var(--warn);font-weight:700}
.postab td{font-size:.84rem}
.postab .pl-neg{color:var(--crit)}.postab .pl-pos{color:var(--accent)}
.postab .gchip{font-family:var(--mono);font-size:.66rem;border:1px solid var(--line);
  border-radius:3px;padding:.02rem .3rem;white-space:nowrap;color:var(--dim)}
.postab .gchip.fired{color:var(--crit);border-color:var(--crit);font-weight:700}
.stalebanner{background:var(--crit-bg);color:var(--crit);border-radius:5px;
  padding:.7rem .9rem;font-size:.85rem;font-family:var(--mono)}
"""

TABS_JS = """
<script>
(function(){
  var KEY='handbook-tab', btns=document.querySelectorAll('.tabs button');
  function show(id){
    btns.forEach(function(b){
      var on=b.dataset.tab===id;
      b.setAttribute('aria-selected',on?'true':'false');
      document.getElementById(b.dataset.tab).hidden=!on;
    });
    try{localStorage.setItem(KEY,id);}catch(e){}
    try{history.replaceState(null,'','#'+id.slice(4));}catch(e){}
  }
  btns.forEach(function(b){b.addEventListener('click',function(){show(b.dataset.tab);});});
  var saved=null; try{saved=localStorage.getItem(KEY);}catch(e){}
  if(saved&&document.getElementById(saved))show(saved);
  // hash deep-link wins over the remembered tab (#desk / #brief / #manual)
  if(location.hash){var h='tab-'+location.hash.slice(1);
    if(document.getElementById(h))show(h);}

  // ---- view-time clocks (build-time relative labels drift on a static page) ----
  var DAY=864e5;
  function midnight(d){return new Date(d.getFullYear(),d.getMonth(),d.getDate());}
  function recompute(){
    var now=new Date();
    document.querySelectorAll('[data-date]').forEach(function(el){
      var t=el.getAttribute('data-date').split('-'),
          d=new Date(+t[0],+t[1]-1,+t[2]),
          n=Math.round((midnight(d)-midnight(now))/DAY),
          chip=el.querySelector('.in:last-child'); if(!chip)return;
      if(n<0){chip.textContent=(-n)+'d PAST';chip.classList.add('past');}
      else{chip.textContent=n===0?'today':(n===1?'tomorrow':'in '+n+'d');chip.classList.remove('past');}
    });
    document.querySelectorAll('[data-ts]').forEach(function(el){
      var t=new Date(el.getAttribute('data-ts')),a=el.querySelector('.ago');
      if(isNaN(t)||!a)return;
      var m=(now-t)/6e4;
      a.textContent=m<12?'just now':(m<90?Math.round(m)+'m ago':
        (m<1200?Math.round(m/60)+'h ago':Math.round(m/1440)+'d ago'));
    });
    var b=document.getElementById('built');
    if(b){var age=(now-new Date(b.getAttribute('data-built')))/36e5;
      var ban=document.getElementById('stale-banner');
      if(age>24&&!ban){ban=document.createElement('div');ban.id='stale-banner';
        ban.className='stalebanner';
        ban.textContent='\\u26a0 This page was built '+Math.round(age)+'h ago \\u2014 a PROME closeout refreshes it. Where it disagrees with canon, canon is right.';
        var w=document.querySelector('.wrap');w.insertBefore(ban,w.children[1]);}
      if(age<=24&&ban)ban.remove();}
  }
  try{recompute();setInterval(recompute,6e4);}catch(e){}
})();
</script>
"""


def parse_heartbeat():
    """HEARTBEAT.md → (base_stamp, [(section, circle)]). The regime strip's source:
    the memo's own per-section severity circles + its Base date. Channels stay
    feed-only by design (v2 call: 4-of-7 read 'crit', stopped discriminating) —
    this does NOT resurrect them; the circles here are the memo's own headline
    judgments, re-read fresh every rebuild."""
    p = ROOT / "HEARTBEAT.md"
    try:
        text = p.read_text(encoding="utf-8")
    except Exception as e:
        alert("regime", f"HEARTBEAT.md unreadable: {e}")
        return None, []
    base = re.search(r"\*\*Base:\*\*\s*(\d{4}-\d{2}-\d{2})", text)
    secs = re.findall(r"^\*\*\d+\.\s+([^—\n]+?)\s*[—-]\s*(🟢|🟡|🟠|🔴)", text, re.M)
    if not secs:
        alert("regime", "HEARTBEAT.md: zero section-circle headings matched — format changed?")
    return (base.group(1) if base else None), secs


def parse_gate_rows():
    """GATES.tsv full rows → (n_live, fired_rows, raw_rows). The change feed already
    carries state FLIPS (wb.parse_gates snapshot diff); this is the STANDING view —
    anything FIRED-* is the single most action-relevant state in the system (fresh
    capital deploys only on a fired trigger) and gets the red strip."""
    p = ROOT / "PROME" / "GATES.tsv"
    try:
        with open(p, encoding="utf-8") as f:
            rows = [r for r in csv.reader(f, delimiter="\t")
                    if r and not r[0].startswith("#") and r[0] != "gate_id" and len(r) > 5]
    except Exception as e:
        alert("gates-strip", f"GATES.tsv parse error: {e}")
        return 0, [], []
    live = sum(1 for r in rows if r[5].split()[0].startswith("LIVE"))
    fired = [{"id": r[0], "state": wb.ell(r[5].split("(")[0], 24),
              "what": wb.ell(re.sub(r"\*\*|`", "", r[4]), 90)}
             for r in rows if r[5].split()[0].startswith("FIRED")]
    return live, fired, rows


_MONTHS = {m: i + 1 for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}


def _expiry_days(txt):
    """'Sep-30' / 'Oct-16' → days from today (year inferred: >60d in the past
    rolls to next year). Returns None when no expiry token is present."""
    m = re.search(r"\b([A-Z][a-z]{2})-(\d{1,2})\b", txt or "")
    if not m or m.group(1) not in _MONTHS:
        return None
    today = dt.date.today()
    d = dt.date(today.year, _MONTHS[m.group(1)], int(m.group(2)))
    if (today - d).days > 60:
        d = d.replace(year=today.year + 1)
    return (d - today).days


def parse_positions(gate_rows):
    """FORGE/STATUS.md position tables → book-strip rows. Column-NAME driven (two
    schemas live in the file: Ticker|Type|... and Strike|Expiry|... under ###
    ticker headings). CONSERVATIVE BY CONTRACT (PROME FORGE-owner rider, 8/21):
    any surprise → alert + omit, never a quiet wrong number; vintage/staleness is
    rendered from parse_money()'s read of the file's OWN header, never restated
    here (PAT-068). Gate join: first GATES row naming the ticker as a word."""
    p = ROOT / "FORGE" / "STATUS.md"
    try:
        lines = p.read_text(encoding="utf-8").splitlines()
    except Exception as e:
        alert("positions", f"FORGE/STATUS.md unreadable: {e}")
        return []
    out, cols, ticker_ctx, section, skipped = [], None, None, "", 0
    for ln in lines:
        s = ln.strip()
        if s.startswith("## "):
            section = s[3:].split("—")[0].split("(")[0].strip()
            cols, ticker_ctx = None, None
        elif s.startswith("### "):
            m = re.match(r"### \*{0,2}([A-Z]{1,6})\b", s)
            ticker_ctx = m.group(1) if m else None
            cols = None
        elif s.startswith("|"):
            cells = [re.sub(r"\*\*|~~|`|\*", "", c).strip()
                     for c in s.strip("|").split("|")]
            if cols is None:
                if "Qty" in cells and ("Ticker" in cells or "Strike" in cells):
                    cols = {}
                    for i, name in enumerate(cells):
                        cols[name.split()[0] if name else f"_{i}"] = i
                continue
            if all(re.fullmatch(r":?-+:?", c or "-") for c in cells):
                continue
            if len(cells) < max(cols.values()) + 1:
                skipped += 1
                continue

            def g(name):
                return cells[cols[name]] if name in cols else ""

            tick = (g("Ticker") or ticker_ctx or "").split()[0] if (g("Ticker") or ticker_ctx) else ""
            if not re.fullmatch(r"[A-Z]{1,6}", tick):
                continue
            pos = g("Strike") or g("Type") or ""
            exp_txt = g("Expiry") or pos
            pl_raw = g("P&L") or g("P&L%") or ""
            pl = re.search(r"[+\-−]\s?\$?[\d,]+(?:\.\d+)?%?(?:\s*/\s*[+\-−][\d.]+%)?", pl_raw)
            # prefer-LIVE-then-fall-back (PROME v2 nit, 8/21 eve): a dead gate
            # naming the ticker must never read as "watching it" — a RESOLVED/
            # RETIRED chip under that header implies active coverage that isn't
            # there, while the real LIVE watcher may be keyed on a series that
            # never names the ticker string at all (TLT's is DGS10-keyed).
            named = [r for r in gate_rows if re.search(rf"\b{tick}\b", "\t".join(r[:6]))]
            live_g = next((r for r in named if r[5].split()[0].startswith(("LIVE", "FIRED"))), None)
            dead_g = named[0] if named else None
            if live_g is not None:
                gate = {"id": live_g[0], "state": live_g[5].split("(")[0].split()[0], "live": True}
            elif dead_g is not None:
                gate = {"id": dead_g[0], "state": dead_g[5].split("(")[0].split()[0], "live": False}
            else:
                gate = None
            out.append({
                "section": section, "ticker": tick,
                "pos": wb.ell(pos if pos != tick else "Stock", 22),
                "qty": g("Qty"), "pl": pl.group(0).replace(" ", "") if pl else "—",
                "exp_days": _expiry_days(exp_txt),
                "gate": gate,
            })
    if not out:
        alert("positions", "FORGE position tables parsed to ZERO rows — schema changed, strip omitted")
    if skipped:
        alert("positions", f"{skipped} ragged position row(s) skipped — verify FORGE tables")
    return out


def _git_ts(path):
    """Last-commit epoch for a path (0 on any failure — badge simply absent)."""
    try:
        r = subprocess.run(["git", "log", "-1", "--format=%ct", "--", path],
                           capture_output=True, text=True, cwd=ROOT, timeout=10)
        return int(r.stdout.strip() or 0)
    except Exception:
        return 0


def parse_spawns(body):
    """Spawn-queue section contract: `- **NAME** · when · why`, one desk/line."""
    rows = []
    for ln in body.splitlines():
        m = re.match(r"-\s+\*\*([A-Z]+)\*\*\s*·\s*([^·]+?)\s*·\s*(.+)$", ln.strip())
        if m:
            rows.append({"name": m.group(1), "when": m.group(2).strip(),
                         "why": m.group(3).strip()})
    return rows


def render_brief_tab(written, brief, feed, first, money, positions):
    """The Desk-brief content as a tab. Decisions section deliberately absent —
    the desk tab owns it (one job per section, even across tabs)."""
    now = dt.datetime.now()
    h = ["<div id='tab-brief' role='tabpanel' aria-label='The brief' hidden>"]
    if brief.get("HEADLINE"):
        h.append("<section>"
                 f"<p class='bhead'>{wb.md_inline(brief['HEADLINE'])}</p>"
                 "<div class='bclocks'>"
                 f"<span>story written {html.escape(written or 'UNDATED')}</span>"
                 "<span>facts on this tab rebuild with the page</span></div></section>")
    h.append("<section><h2>What changed</h2><ul class='feed'>")
    if first:
        h.append("<li><span class='ago'>—</span><span>first build — baseline recorded, "
                 "history starts now</span></li>")
    elif not feed:
        h.append("<li><span class='ago'>—</span><span>nothing has moved since the "
                 "last rebuild</span></li>")
    for e in feed:
        h.append(f"<li data-ts='{html.escape(e.get('ts', ''))}'>"
                 f"<span class='ago'>{html.escape(wb.ago(e.get('ts', ''), now))}</span>"
                 f"<span>{wb.md_inline(e.get('text', ''))}</span></li>")
    h.append("</ul></section>")
    if brief.get("STORY"):
        h.append("<section><h2>What is going on</h2><div class='prose'>"
                 + wb.md_block(brief["STORY"]) + "</div>")
        vint = html.escape((written or "UNDATED").split(" (")[0].strip())
        if brief.get("QUESTION"):
            h.append(f"<p class='pull'>{wb.md_inline(brief['QUESTION'])} "
                     f"<span class='vint'>[as written {vint}]</span></p>")
        if brief.get("FALSIFIER"):
            h.append(f"<div class='falsify'><div class='lead'>This is wrong if "
                     f"<span class='vint'>[as written {vint}]</span></div>"
                     f"<div class='prose'>{wb.md_block(brief['FALSIFIER'])}</div></div>")
        h.append("</section>")
    if brief.get("DISAGREEMENT"):
        h.append("<section><h2>Where the desk disagrees</h2><div class='prose'>"
                 + wb.md_block(brief["DISAGREEMENT"]) + "</div></section>")
    h.append("<section><h2>Where you stand</h2>")
    if money:
        stale = " stale" if money["age"] > 5 else ""
        h.append("<div class='book'>"
                 f"<div class='stat'><span class='v'>${money['total']}</span>"
                 "<span class='k'>Account</span></div>"
                 f"<div class='stat'><span class='v'>{money['cash_pct']}%</span>"
                 "<span class='k'>Cash</span></div>"
                 f"<div class='vint{stale}'>broker export {money['vintage']} · "
                 f"{money['age']}d old — not live, re-check before any fill</div></div>")
    if positions:
        h.append("<div class='tw'><table class='postab'><tr><th>Pos</th><th>Qty</th>"
                 "<th>P&amp;L</th><th>Expiry</th><th>Watching it</th></tr>")
        for p in positions:
            plc = "pl-neg" if p["pl"].startswith(("-", "−")) else ("pl-pos" if p["pl"].startswith("+") else "")
            expd = p["exp_days"]
            exp = ("—" if expd is None else
                   f"<span class='{'pl-neg' if expd <= 14 else ''}'>{expd}d</span>")
            if p["gate"] and p["gate"]["live"]:
                gch = (f"<span class='gchip{' fired' if p['gate']['state'].startswith('FIRED') else ''}'>"
                       f"{html.escape(p['gate']['id'])} {html.escape(p['gate']['state'])}</span>")
            elif p["gate"]:
                gch = (f"<span class='gchip'>no LIVE gate — last: "
                       f"{html.escape(p['gate']['id'])} {html.escape(p['gate']['state'])}</span>")
            else:
                gch = "<span class='gchip'>no gate names it</span>"
            h.append(f"<tr><td><strong>{html.escape(p['ticker'])}</strong> "
                     f"{html.escape(p['pos'])}</td><td>{html.escape(p['qty'])}</td>"
                     f"<td class='{plc}'>{html.escape(p['pl'])}</td>"
                     f"<td>{exp}</td><td>{gch}</td></tr>")
        h.append("</table></div>"
                 "<p class='hint'>Marks inherit the broker-export vintage above — never fill "
                 "against them. 'Watching it' = the first LIVE/FIRED GATES.tsv row naming the "
                 "ticker; a dead gate never renders as watching — 'no LIVE gate' says so and "
                 "names the last one; 'no gate names it' means no registered action-gate "
                 "mentions this position at all.</p>")
    if brief.get("POSITION"):
        h.append("<div class='prose'>" + wb.md_block(brief["POSITION"]) + "</div>")
    h.append("</section>")
    if brief.get("WATCH"):
        h.append("<section><h2>What is coming</h2><div class='prose'>"
                 + wb.md_block(brief["WATCH"]) + "</div>"
                 "<p class='hint'>Dated rows live on Your desk → The clock.</p></section>")
    h.append("</div>")  # /tab-brief
    return "\n".join(h)


def render(sections, dec, chore, dates, brief_tab_html, board):
    now = dt.datetime.now().astimezone()

    def take(prefix):
        return next((b for t, b in sections if t.lower().startswith(prefix)), None)

    prio, spawn_body, runs = take("top priorities"), take("spawn queue"), take("runs itself")
    special = ("top priorities", "spawn queue", "runs itself")
    manual = [(t, b) for t, b in sections
              if not t.lower().startswith(special)]
    spawns = parse_spawns(spawn_body) if spawn_body else []
    if spawn_body and not spawns:
        alert("spawns", "Spawn-queue section present but zero rows matched the format contract")

    # split queue rows: needs your word NOW vs in-flight (blocked / already ruled)
    live_dec = [d for d in dec if not d["blocked"] and not re.search(r"✅|RULED", d["item"])]
    inflight = [d for d in dec if d not in live_dec]

    h = ["<title>The Helm</title>", f"<style>{CSS}</style>", "<div class='wrap'>"]
    n_w, n_s = len(live_dec), len(spawns)
    summary = (f"{n_w} word{'s' if n_w != 1 else ''} needed · "
               f"{n_s} desk{'s' if n_s != 1 else ''} to spawn")
    h.append(
        "<header class='mast'><div class='eyebrow'>PROME · the operator's seat</div>"
        "<h1>The Helm</h1>"
        f"<div class='sum'>{html.escape(summary)}</div>"
        "<div class='clocks'>"
        f"<span id='built' data-built='{now.isoformat(timespec='minutes')}'>rebuilt {now:%b %-d, %-I:%M %p} ET</span>"
        "<span>live sections generated from WILL_QUEUE / DOCKET</span>"
        f"<a href='{FLEETOPS_URL}'>Fleet Ops →</a>"
        "</div></header>")

    for leg, reason in ALERTS:
        h.append(f"<div class='degraded'>⚠ {html.escape(leg)}: {html.escape(reason)}</div>")

    # -- the board: regime + gates (page-level — visible from every tab) --------
    hb_base, hb_secs = board["base"], board["secs"]
    h.append("<div class='board'>")
    if hb_secs:
        h.append("<span class='regime'>"
                 + " ".join(f"<span><b>{html.escape(n)}</b> {c}</span>" for n, c in hb_secs)
                 + f"<span class='asof'>HEARTBEAT base {html.escape(hb_base or 'UNDATED')}"
                   " · circles are the memo's own headline severities</span></span>")
    for fg in board["fired"]:
        h.append(f"<div class='fired'><span class='gid'>{html.escape(fg['id'])}</span> "
                 f"{html.escape(fg['state'])} — {html.escape(fg['what'])}</div>")
    h.append(f"<span class='gline'>{board['live']} gates LIVE · "
             + (f"{len(board['fired'])} FIRED — act or escalate, never leave standing"
                if board["fired"] else "none fired")
             + " · flips land in The brief → What changed</span></div>")

    h.append("<nav class='tabs' role='tablist'>"
             "<button role='tab' data-tab='tab-desk' aria-selected='true'>Your desk</button>"
             "<button role='tab' data-tab='tab-brief' aria-selected='false'>The brief</button>"
             "<button role='tab' data-tab='tab-manual' aria-selected='false'>The manual</button>"
             "</nav>")
    h.append("<div id='tab-desk' role='tabpanel' aria-label='Your desk'>")

    # -- live: waiting on you ---------------------------------------------------
    h.append("<section><h2>Waiting on you — "
             f"{n_w} need{'s' if n_w == 1 else ''} your word</h2><div class='live'>")
    if live_dec:
        for d in live_dec:
            due = f" · {html.escape(d['due_txt'])}" if d["due_txt"].strip("—- ") else ""
            h.append("<div class='decision'>"
                     f"<span class='n'>row {html.escape(d['n'])} · {html.escape(d['kind'])}{due}</span>"
                     f"<span class='t'>{wb.md_inline(d['item'])}</span>"
                     f"<span class='r'>{wb.md_inline(d['rec'])}</span></div>")
    else:
        h.append("<div class='none'>Nothing needs a ruling right now.</div>")
    if inflight or chore:
        h.append("<div class='subhead'>In flight — comes back to you when a desk finishes its half</div>")
    for d in inflight:
        h.append(f"<div class='chore'><span>{wb.md_inline(d['item'])}</span>"
                 f"<span class='w'>{html.escape(d['due_txt'])}</span></div>")
    for c in chore:
        h.append(f"<div class='chore'><span>{wb.md_inline(c['item'])}</span>"
                 f"<span class='w'>{html.escape(c['due_txt'])}</span></div>")
    h.append("</div></section>")

    # -- spawn queue ------------------------------------------------------------
    if spawns:
        # freshness badge: these rows are hand-written standing-state assertions
        # (Class 10's shape) — badge any desk that COMMITTED after the row was
        # written, so a satisfied row can't silently pose as pending.
        hb_ts = _git_ts("PROME/HANDBOOK.md")
        h.append(f"<section><h2>Spawn queue — {n_s} desks, decay order</h2>"
                 "<div class='spawns'>")
        for s in spawns:
            chip = "chip warn" if s["when"].lower().startswith("before") else "chip"
            ran = ""
            d_ts = _git_ts(f"AGENTS/{s['name']}")
            if hb_ts and d_ts > hb_ts:
                ran = (f"<span class='chip ran'>desk ran "
                       f"{dt.datetime.fromtimestamp(d_ts):%-m/%-d %-I:%M%p} — "
                       "row may be satisfied</span>")
            h.append("<div class='spawn'>"
                     f"<div class='top'><span class='nm'>{html.escape(s['name'])}</span>"
                     f"<span class='{chip}'>{html.escape(s['when'])}</span></div>"
                     f"<code class='cmd'>cd AGENTS/{html.escape(s['name'])} &amp;&amp; claude</code>"
                     f"<div class='why'>{wb.md_inline(s['why'])}{' ' + ran if ran else ''}</div></div>")
        h.append("</div><p class='hint'>Launch from the desk's own folder, then say "
                 "“please boot up.” Each desk closes itself out when done.</p></section>")

    # -- curated priorities -----------------------------------------------------
    if prio is not None:
        h.append("<section><h2>Top priorities — PROME-curated</h2>"
                 + render_body(prio) + "</section>")
    if runs is not None:
        # hand-written dated rows rot after their date passes; annotate, don't hide
        today = dt.date.today()
        ann = []
        for ln in runs.splitlines():
            mds = re.findall(r"\b(\d{1,2})/(\d{1,2})\b", ln)
            if (ln.strip().startswith("-") and mds
                    and all(dt.date(today.year, int(a), int(b)) < today for a, b in mds
                            if 1 <= int(a) <= 12 and 1 <= int(b) <= 31)):
                ln = ln.rstrip() + " *(date passed — hand-written row, refreshes at PROME's next closeout)*"
            ann.append(ln)
        h.append("<section><h2>Runs itself — no window needed</h2>"
                 + render_body("\n".join(ann)) + "</section>")

    # -- the clock --------------------------------------------------------------
    h.append("<section><h2>The clock — next dated things</h2><ul class='days'>")
    for r in dates:
        d = dt.date.fromisoformat(r["date"])
        also = ""
        if r["also"]:
            inner = "".join(f"<div class='alsorow'>{html.escape(t)}</div>"
                            for t in r.get("also_titles", []))
            also = (f" <details class='more'><summary>+{r['also']} more</summary>{inner}</details>"
                    if inner else f" <span class='in'>+{r['also']} more</span>")
        rel = "today" if r["days"] == 0 else ("tomorrow" if r["days"] == 1 else f"in {r['days']}d")
        h.append(f"<li class='{'star' if r['star'] else ''}' data-date='{r['date']}'>"
                 f"<span class='when'>{d:%a %-m/%-d}</span>"
                 f"<span>{html.escape(r['title'])}{also}</span>"
                 f"<span class='in'>{rel}</span></li>")
    if not dates:
        h.append("<li><span class='when'>—</span><span>clock parsed empty — see canon</span><span></span></li>")
    h.append("</ul></section>")
    h.append("</div>")  # /tab-desk

    # -- the brief --------------------------------------------------------------
    h.append(brief_tab_html)

    # -- the manual -------------------------------------------------------------
    h.append("<div id='tab-manual' role='tabpanel' aria-label='The manual' hidden>")
    slugs = [re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:40] for t, _ in manual]
    h.append("<nav class='toc'>" + " ".join(
        f"<a href='#s-{s}'>{wb.md_inline(t.split('—')[0].split('[')[0].strip())}</a>"
        for s, (t, _) in zip(slugs, manual)) + "</nav>")
    for s, (title, body) in zip(slugs, manual):
        h.append(f"<section id='s-{s}'><h2>{wb.md_inline(title)}</h2>{render_body(body)}</section>")
    h.append("</div>")  # /tab-manual

    h.append(TABS_JS)
    h.append("<footer>The manual half is hand-written canon (<code>PROME/HANDBOOK.md</code>) "
             "and changes only when a convention changes — its claims carry their own dates. "
             "The live sections regenerate at every PROME closeout from the same files the "
             "Desk brief reads; if this page and canon disagree, canon is right. "
             "Money is a broker mirror; never fill against it.</footer></div>")
    return "\n".join(h)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--no-feed", action="store_true",
                    help="test build: do NOT advance the change-feed state "
                         "(write=False) — the feed must advance exactly once "
                         "per real rebuild, and a test render is not a rebuild")
    a = ap.parse_args()

    sections = parse_handbook()
    try:
        dec, chore = wb.parse_actions()
    except Exception as e:
        alert("queue", f"parse_actions raised: {e}"); dec, chore = [], []
    try:
        dates = wb.parse_dates(limit=6)
    except Exception as e:
        alert("clock", f"parse_dates raised: {e}"); dates = []

    # board strip + positions (all fail-loud into ALERTS, never a quiet absence)
    try:
        hb_base, hb_secs = parse_heartbeat()
    except Exception as e:
        alert("regime", f"parse_heartbeat raised: {e}"); hb_base, hb_secs = None, []
    try:
        n_live, fired, gate_rows = parse_gate_rows()
    except Exception as e:
        alert("gates-strip", f"parse_gate_rows raised: {e}"); n_live, fired, gate_rows = 0, [], []
    try:
        positions = parse_positions(gate_rows)
    except Exception as e:
        alert("positions", f"parse_positions raised: {e}"); positions = []
    board = {"base": hb_base, "secs": hb_secs, "live": n_live, "fired": fired}

    # Brief tab — through the brief's own parsers. write=True since 2026-08-21
    # (Will's word: standalone page RETIRED, "run that through the handbook"):
    # THIS run now owns the change-feed baseline — the ownership transferred
    # here the same commit the standalone stopped regenerating, so exactly one
    # writer exists at all times (the cursor-advance class, both directions).
    try:
        written, brief = wb.parse_brief()
        money = wb.parse_money()
        gates, channels = wb.parse_gates(), wb.parse_channels()
        feed, first = wb.update_changes(
            wb.snapshot_now(gates, channels, money, dec, chore, dates),
            write=not a.no_feed)
        brief_tab = render_brief_tab(written, brief, feed, first, money, positions)
    except Exception as e:
        alert("brief", f"brief legs raised: {e}")
        brief_tab = ("<div id='tab-brief' role='tabpanel' hidden>"
                     "<div class='degraded'>brief tab failed to build — "
                     f"{html.escape(str(e))}</div></div>")

    out = Path(a.out)
    out.write_text(render(sections, dec, chore, dates, brief_tab, board), encoding="utf-8")
    n = len(ALERTS)
    if n:
        print(f"handbook: REVIEW — {n} ⚠️  ({'; '.join(l for l, _ in ALERTS)}) · wrote {out} ({out.stat().st_size}B)")
        return 1
    print(f"handbook: OK · wrote {out} ({out.stat().st_size}B) · "
          f"{len(sections)} manual sections · {len(dec)} decisions · {len(dates)} clock rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
