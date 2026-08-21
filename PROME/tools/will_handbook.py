#!/usr/bin/env python3
"""
will_handbook.py — Will's Operator Handbook page (the third Will-facing page).

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
import datetime as dt
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import will_brief as wb  # noqa: E402  (parsers + md_inline; ONE parser family)

ROOT = Path(__file__).resolve().parents[2]
HANDBOOK = ROOT / "PROME" / "HANDBOOK.md"

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
.tabs{display:flex;gap:2px;border-bottom:1px solid var(--line)}
.tabs button{font:inherit;font-size:.82rem;font-weight:700;letter-spacing:.06em;
  text-transform:uppercase;background:none;border:0;color:var(--faint);
  border-bottom:3px solid transparent;padding:.45rem 1rem .6rem;cursor:pointer}
.tabs button[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--accent)}
.tabs button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
[role="tabpanel"][hidden]{display:none}
[role="tabpanel"]{display:flex;flex-direction:column;gap:2.1rem}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
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
  }
  btns.forEach(function(b){b.addEventListener('click',function(){show(b.dataset.tab);});});
  var saved=null; try{saved=localStorage.getItem(KEY);}catch(e){}
  if(saved&&document.getElementById(saved))show(saved);
})();
</script>
"""


def render(sections, dec, chore, dates):
    now = dt.datetime.now().astimezone()
    prio = next((b for t, b in sections if t.lower().startswith("top priorities")), None)
    manual = [(t, b) for t, b in sections if not t.lower().startswith("top priorities")]

    h = ["<title>Operator Handbook</title>", f"<style>{CSS}</style>", "<div class='wrap'>"]
    h.append(
        "<header class='mast'><div class='eyebrow'>PROME · field manual</div>"
        "<h1>Operator Handbook</h1><div class='clocks'>"
        f"<span>rebuilt {now:%b %-d, %-I:%M %p} ET</span>"
        "<span>live sections generated from WILL_QUEUE / DOCKET</span>"
        "</div></header>")

    for leg, reason in ALERTS:
        h.append(f"<div class='degraded'>⚠ {html.escape(leg)}: {html.escape(reason)}</div>")

    h.append("<nav class='tabs' role='tablist'>"
             "<button role='tab' data-tab='tab-desk' aria-selected='true'>Your desk</button>"
             "<button role='tab' data-tab='tab-manual' aria-selected='false'>The manual</button>"
             "</nav>")
    h.append("<div id='tab-desk' role='tabpanel' aria-label='Your desk'>")

    # -- live: waiting on you ---------------------------------------------------
    h.append("<section><h2>Waiting on you — "
             f"{len(dec)} decision{'s' if len(dec) != 1 else ''}</h2><div class='live'>")
    if dec:
        for d in dec:
            due = f" · {html.escape(d['due_txt'])}" if d["due_txt"].strip("—- ") else ""
            h.append("<div class='decision'>"
                     f"<span class='n'>row {html.escape(d['n'])} · {html.escape(d['kind'])}{due}</span>"
                     f"<span class='t'>{wb.md_inline(d['item'])}</span>"
                     f"<span class='r'>{wb.md_inline(d['rec'])}</span></div>")
    else:
        h.append("<div class='none'>Nothing needs a ruling right now.</div>")
    for c in chore:
        h.append(f"<div class='chore'><span>{wb.md_inline(c['item'])}</span>"
                 f"<span class='w'>{html.escape(c['due_txt'])}</span></div>")
    h.append("</div></section>")

    # -- curated priorities -----------------------------------------------------
    if prio is not None:
        h.append("<section><h2>Top priorities — PROME-curated</h2>"
                 + render_body(prio) + "</section>")

    # -- the clock --------------------------------------------------------------
    h.append("<section><h2>The clock — next dated things</h2><ul class='days'>")
    for r in dates:
        d = dt.date.fromisoformat(r["date"])
        also = f" <span class='in'>+{r['also']} more</span>" if r["also"] else ""
        rel = "today" if r["days"] == 0 else ("tomorrow" if r["days"] == 1 else f"in {r['days']}d")
        h.append(f"<li class='{'star' if r['star'] else ''}'>"
                 f"<span class='when'>{d:%a %-m/%-d}</span>"
                 f"<span>{html.escape(r['title'])}{also}</span>"
                 f"<span class='in'>{rel}</span></li>")
    if not dates:
        h.append("<li><span class='when'>—</span><span>clock parsed empty — see canon</span><span></span></li>")
    h.append("</ul></section>")
    h.append("</div>")  # /tab-desk

    # -- the manual -------------------------------------------------------------
    h.append("<div id='tab-manual' role='tabpanel' aria-label='The manual' hidden>")
    for title, body in manual:
        h.append(f"<section><h2>{wb.md_inline(title)}</h2>{render_body(body)}</section>")
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

    out = Path(a.out)
    out.write_text(render(sections, dec, chore, dates), encoding="utf-8")
    n = len(ALERTS)
    if n:
        print(f"handbook: REVIEW — {n} ⚠️  ({'; '.join(l for l, _ in ALERTS)}) · wrote {out} ({out.stat().st_size}B)")
        return 1
    print(f"handbook: OK · wrote {out} ({out.stat().st_size}B) · "
          f"{len(sections)} manual sections · {len(dec)} decisions · {len(dates)} clock rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
