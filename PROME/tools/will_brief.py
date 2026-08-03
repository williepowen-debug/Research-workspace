#!/usr/bin/env python3
"""
will_brief.py — generate Will's briefing page (the SIMPLE Will-facing surface).

PURPOSE: the story, not the machine state. Answers "what is the bet, what would
break it, what do I actually do" in ~30 seconds of scanning. Born 2026-08-03
(Will-directed: "a feed I can read... dumbs it down a bit more so I can see the
bigger picture").

NOT a duplicate of fleet_dashboard.py — DIFFERENT AUDIENCE, DIFFERENT QUESTION:
  fleet_dashboard.py -> is anything BROKEN? who is stale? what parses? (PROME/ops)
  will_brief.py      -> what is the BET, what decides it, what do I do? (Will)
Both read the same canon; neither owns a fact. If they ever disagree, canon wins
and the parser is broken.

DESIGN CONTRACT (inherits fleet_dashboard.py's anti-rot contract):
  - GENERATED, never hand-edited. The ONE hand-written input is PROME/BRIEF.md,
    which is judgment (the story) and cannot be parsed from a TSV.
  - TWO CLOCKS, SHOWN SEPARATELY. Facts carry the build stamp; the story carries
    BRIEF.md's own WRITTEN stamp. A stale story must READ as stale rather than
    ride the freshness of the generated half.
    [[finding_dated_stamp_is_a_trigger_not_a_shield]]
  - FAIL LOUD. A broken parser renders a visible PARSE-FAILED block naming the
    owner file. Never a silently-missing section — a briefing that quietly drops
    the thing that mattered is worse than no briefing.
  - POINTS, never owns. Money figures come from FORGE/STATUS.md WITH its vintage,
    never re-typed here.

USAGE
  python3 PROME/tools/will_brief.py -o /tmp/brief.html
  (then publish via the Artifact tool — SAME URL every time. From any session
   other than the one that minted it, pass url="..." or it orphans Will's tab.
   [[finding_artifact_redeploy_same_url]])

ARTIFACT_URL: https://claude.ai/code/artifact/76508dac-662b-4da4-a60b-c586e3a472ec
  (minted 2026-08-03. Same-conversation republish of the same file path keeps this URL.)
  FAVICON: 🧭 — keep identical on every republish; Will finds the tab by its icon.
"""
import argparse
import csv
import datetime as dt
import html
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ET = "ET"

# Sections the parser keys on in BRIEF.md. Order here is render order.
BRIEF_SECTIONS = ["HEADLINE", "STORY", "QUESTION", "POSITION", "WATCH"]

failures = []           # (section, owner_file, reason) -> rendered as PARSE-FAILED


def fail(section, owner, reason):
    failures.append((section, owner, reason))
    return None


# --------------------------------------------------------------- canon parsers

def parse_brief():
    """PROME/BRIEF.md — the hand-written half. Returns (written_stamp, {section: md})."""
    p = ROOT / "PROME/BRIEF.md"
    try:
        text = p.read_text(encoding="utf-8")
    except Exception as e:
        return fail("the story", "PROME/BRIEF.md", f"unreadable: {e}") or (None, {})
    body = text.split("<!-- ", 1)[-1].split("-->", 1)[-1]
    out, written = {}, None
    for m in re.finditer(r"^##\s+([A-Z]+)\s*$(.*?)(?=^##\s+[A-Z]+\s*$|\Z)",
                         body, re.M | re.S):
        name, chunk = m.group(1).strip(), m.group(2).strip()
        if name == "WRITTEN":
            written = chunk.splitlines()[0].strip() if chunk else None
        else:
            out[name] = chunk
    missing = [s for s in BRIEF_SECTIONS if s not in out or not out[s]]
    if missing:
        fail("the story", "PROME/BRIEF.md", f"missing/empty section(s): {', '.join(missing)}")
    if not written:
        fail("story vintage", "PROME/BRIEF.md", "no '## WRITTEN' stamp — cannot date the narrative")
    return written, out


def parse_dates(limit=9):
    """DOCKET.tsv — forward catalysts. PENDING only, today onward, soonest first.
    ★ in the title is PROME's own high-signal marker; surfaced as a flag."""
    p = ROOT / "PROME/DOCKET.tsv"
    today = dt.date.today().isoformat()
    rows = []
    try:
        with open(p, encoding="utf-8") as f:
            for r in csv.reader(f, delimiter="\t"):
                if not r or r[0].startswith("#") or len(r) < 4:
                    continue
                if not r[3].startswith("PENDING"):
                    continue
                end = r[0].split("..")[-1]
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", end) or end < today:
                    continue
                title = r[1].split("—")[0].split(" - ")[0].strip()
                rows.append({
                    "date": end,
                    "days": (dt.date.fromisoformat(end) - dt.date.today()).days,
                    "title": title[:74],
                    "owner": (r[2] if len(r) > 2 else "").split("/")[0][:12],
                    "star": "★" in r[1],
                })
    except Exception as e:
        return fail("the clock", "PROME/DOCKET.tsv", f"parse error: {e}") or []
    rows.sort(key=lambda x: (x["date"], not x["star"]))
    # Collapse same-date rows so one heavy day reads as ONE day, not five lines.
    grouped, seen = [], {}
    for r in rows:
        if r["date"] in seen:
            seen[r["date"]]["also"] += 1
            seen[r["date"]]["star"] = seen[r["date"]]["star"] or r["star"]
            continue
        r["also"] = 0
        seen[r["date"]] = r
        grouped.append(r)
    return grouped[:limit]


def parse_actions(limit=6):
    """WILL_QUEUE.md OPEN table — items where WILL is the actor. Dated first."""
    p = ROOT / "PROME/WILL_QUEUE.md"
    try:
        text = p.read_text(encoding="utf-8")
    except Exception as e:
        return fail("what you do", "PROME/WILL_QUEUE.md", f"unreadable: {e}") or []
    section = text.split("## OPEN", 1)[-1].split("\n## ", 1)[0]
    out = []
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        c = [x.strip() for x in line.strip("|").split("|")]
        if len(c) < 5 or not c[0].isdigit():
            continue
        blocked = "⛔" in line
        raw = c[3]
        d = re.search(r"\d{4}-\d{2}-\d{2}", raw)
        item = re.sub(r"\*\*|`", "", c[1])
        out.append({
            "n": c[0], "item": item[:70], "kind": c[2][:9],
            "due": d.group(0) if d else None,
            "due_txt": re.sub(r"\*\*", "", raw)[:26],
            "blocked": blocked,
            "rec": re.sub(r"\*\*|`", "", c[5] if len(c) > 5 else "")[:64],
        })
    if not out:
        fail("what you do", "PROME/WILL_QUEUE.md", "OPEN table parsed to zero rows")
    out.sort(key=lambda x: (x["blocked"], x["due"] or "9999"))
    return out[:limit]


def parse_money():
    """FORGE/STATUS.md header — account total + cash %, WITH the export vintage.
    Never re-typed here; if the header shape changes this fails loud."""
    p = ROOT / "FORGE/STATUS.md"
    try:
        head = p.read_text(encoding="utf-8")[:4000]
    except Exception as e:
        return fail("the book", "FORGE/STATUS.md", f"unreadable: {e}")
    total = re.search(r"account total:\*\*\s*\$([\d,]+\.\d\d)", head)
    cash = re.search(r"money market\):\*\*\s*\$([\d,]+\.\d\d)\s*\(([\d.]+)%\)", head)
    vint = re.search(r"\*\*Updated:\*\*\s*(\d{4}-\d{2}-\d{2})", head)
    marks = re.search(r"marks = (?:Fri )?(\d{4}-\d{2}-\d{2})", head)
    if not (total and cash and vint):
        return fail("the book", "FORGE/STATUS.md",
                    "header shape changed — account total / cash / Updated not found")
    age = (dt.date.today() - dt.date.fromisoformat(vint.group(1))).days
    return {"total": total.group(1), "cash_pct": cash.group(2),
            "vintage": vint.group(1), "marks": marks.group(1) if marks else vint.group(1),
            "age": age}


def parse_channels():
    """dashboard_state.json — the domain heat map, already canon-derived."""
    p = ROOT / "PROME/tools/dashboard_state.json"
    try:
        s = json.loads(p.read_text())
    except Exception as e:
        return fail("pressure", "PROME/tools/dashboard_state.json", f"unreadable: {e}") or {}
    order = {"crit": 0, "elev": 1, "watch": 2, "none": 3}
    ch = s.get("channels") or {}
    return dict(sorted(ch.items(), key=lambda kv: (order.get(kv[1], 9), kv[0])))


def parse_gate_blockers():
    """GATES.tsv — FIRED-UNEXECUTED is the one state that must never sit quietly."""
    p = ROOT / "PROME/GATES.tsv"
    try:
        with open(p, encoding="utf-8") as f:
            rows = [r for r in csv.reader(f, delimiter="\t")
                    if r and not r[0].startswith("#") and r[0] != "gate_id"]
    except Exception as e:
        return fail("gates", "PROME/GATES.tsv", f"parse error: {e}") or []
    return [r[0] for r in rows if len(r) > 5 and r[5].startswith("FIRED-UNEXECUTED")]


# ------------------------------------------------------------------ rendering

def md_inline(s):
    """Minimal, deliberately dumb markdown: **bold** and `code` only."""
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


def md_block(s):
    """Paragraphs + '- ' bullets. No nesting, no tables — by design."""
    out, buf = [], []
    def flush():
        if buf:
            out.append("<p>" + md_inline(" ".join(buf)) + "</p>")
            buf.clear()
    lines = s.splitlines()
    i = 0
    while i < len(lines):
        ln = lines[i].strip()
        if ln.startswith("- "):
            flush()
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append("<li>" + md_inline(lines[i].strip()[2:]) + "</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        if not ln:
            flush()
        else:
            buf.append(ln)
        i += 1
    flush()
    return "\n".join(out)


CSS = """
*,*::before,*::after{box-sizing:border-box}
:root{
  /* Nautical chart: buff land, deep water, magenta = the navigational warning.
     Magenta is the accent because that is literally what it signals on a chart. */
  --ground:#EDEBE4; --panel:#F6F4EF; --line:#D3CEC1; --line-soft:#E2DDD1;
  --text:#1B211F; --text-dim:#5C6360; --text-faint:#878D88;
  --accent:#A62D72; --accent-soft:#F2DDE9;
  --water:#2F5D72;
  --good:#2E6B45; --warn:#9A6612; --crit:#A4342A;
  --good-bg:#E2EDE5; --warn-bg:#F4E8D4; --crit-bg:#F5E0DC;
  --serif:Georgia,'Iowan Old Style','Palatino Linotype',Palatino,serif;
  --sans:system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;
  --mono:ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace;
}
@media (prefers-color-scheme:dark){
  :root{
    --ground:#0D1418; --panel:#141D22; --line:#26333A; --line-soft:#1C272D;
    --text:#E4E7E5; --text-dim:#9BA6A4; --text-faint:#6F7B79;
    --accent:#E86BA8; --accent-soft:#3A1F2E;
    --water:#6FA3BC;
    --good:#63C185; --warn:#DCA84A; --crit:#EC7166;
    --good-bg:#16291E; --warn-bg:#2C2313; --crit-bg:#2E1917;
  }
}
:root[data-theme="dark"]{
  --ground:#0D1418; --panel:#141D22; --line:#26333A; --line-soft:#1C272D;
  --text:#E4E7E5; --text-dim:#9BA6A4; --text-faint:#6F7B79;
  --accent:#E86BA8; --accent-soft:#3A1F2E;
  --water:#6FA3BC;
  --good:#63C185; --warn:#DCA84A; --crit:#EC7166;
  --good-bg:#16291E; --warn-bg:#2C2313; --crit-bg:#2E1917;
}
:root[data-theme="light"]{
  --ground:#EDEBE4; --panel:#F6F4EF; --line:#D3CEC1; --line-soft:#E2DDD1;
  --text:#1B211F; --text-dim:#5C6360; --text-faint:#878D88;
  --accent:#A62D72; --accent-soft:#F2DDE9;
  --water:#2F5D72;
  --good:#2E6B45; --warn:#9A6612; --crit:#A4342A;
  --good-bg:#E2EDE5; --warn-bg:#F4E8D4; --crit-bg:#F5E0DC;
}
body{margin:0;background:var(--ground);color:var(--text);font-family:var(--sans);
  font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
.wrap{max-width:46rem;margin:0 auto;padding:2.5rem 1.25rem 5rem;
  display:flex;flex-direction:column;gap:2.5rem}
code{font-family:var(--mono);font-size:.9em;background:var(--line-soft);
  padding:.1em .35em;border-radius:3px}
.num{font-family:var(--mono);font-variant-numeric:tabular-nums}

/* masthead ------------------------------------------------------------- */
.mast{display:flex;flex-direction:column;gap:.5rem;
  border-bottom:2px solid var(--accent);padding-bottom:1rem}
.eyebrow{font-size:.68rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--accent);font-weight:700}
.mast h1{font-family:var(--serif);font-size:clamp(1.5rem,4.5vw,2rem);line-height:1.25;
  margin:0;font-weight:400;text-wrap:balance;letter-spacing:-.01em}
.clocks{display:flex;flex-wrap:wrap;gap:.4rem .9rem;font-size:.72rem;
  color:var(--text-faint);font-family:var(--mono)}
.clocks .stale{color:var(--warn);font-weight:700}

/* generic block -------------------------------------------------------- */
section{display:flex;flex-direction:column;gap:.85rem}
h2{font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;margin:0;
  color:var(--text-faint);font-weight:700;
  display:flex;align-items:center;gap:.6rem}
h2::after{content:"";flex:1;height:1px;background:var(--line)}
.prose{font-family:var(--serif);font-size:1.03rem;line-height:1.68}
.prose p{margin:0 0 .9rem}
.prose p:last-child{margin-bottom:0}
.prose ul{margin:0;padding-left:1.1rem;display:flex;flex-direction:column;gap:.5rem}
.pull{font-family:var(--serif);font-size:1.12rem;line-height:1.5;margin:0;
  padding:.9rem 0 .9rem 1.1rem;border-left:3px solid var(--accent);color:var(--text)}

/* clock ---------------------------------------------------------------- */
.days{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}
.day{display:grid;grid-template-columns:4.6rem 1fr auto;gap:.85rem;align-items:baseline;
  padding:.62rem 0;border-bottom:1px solid var(--line-soft)}
.day:last-child{border-bottom:none}
.day .when{font-family:var(--mono);font-size:.78rem;color:var(--text-dim);
  font-variant-numeric:tabular-nums;white-space:nowrap}
.day .what{font-size:.92rem;line-height:1.4}
.day .in{font-family:var(--mono);font-size:.7rem;color:var(--text-faint);white-space:nowrap}
.day.key .what{font-weight:600}
.day.key .when{color:var(--accent);font-weight:700}
.day .also{color:var(--text-faint);font-size:.78rem}

/* actions -------------------------------------------------------------- */
.acts{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:.6rem}
.act{display:flex;flex-direction:column;gap:.2rem;padding:.7rem .85rem;
  background:var(--panel);border:1px solid var(--line);border-radius:5px;
  border-left:3px solid var(--line)}
.act.due{border-left-color:var(--crit)}
.act.soon{border-left-color:var(--warn)}
.act .top{display:flex;flex-wrap:wrap;gap:.5rem;align-items:baseline;
  justify-content:space-between}
.act .name{font-size:.92rem;font-weight:600}
.act .when{font-family:var(--mono);font-size:.7rem;color:var(--text-dim);white-space:nowrap}
.act .rec{font-size:.8rem;color:var(--text-dim)}

/* pressure ------------------------------------------------------------- */
.chips{display:flex;flex-wrap:wrap;gap:.4rem}
.chip{display:inline-flex;align-items:center;gap:.4rem;font-size:.76rem;
  padding:.28rem .6rem;border-radius:99px;border:1px solid var(--line);
  background:var(--panel);color:var(--text-dim)}
.chip .dot{width:.5rem;height:.5rem;border-radius:99px;background:var(--text-faint);flex:none}
.chip.crit{background:var(--crit-bg);color:var(--crit);border-color:transparent;font-weight:600}
.chip.crit .dot{background:var(--crit)}
.chip.elev{background:var(--warn-bg);color:var(--warn);border-color:transparent}
.chip.elev .dot{background:var(--warn)}
.chip.watch .dot{background:var(--water)}
.chip.none .dot{background:var(--good)}

/* money ---------------------------------------------------------------- */
.book{display:flex;flex-wrap:wrap;gap:1.6rem;align-items:flex-end;
  padding:.9rem 1rem;background:var(--panel);border:1px solid var(--line);border-radius:5px}
.stat{display:flex;flex-direction:column;gap:.1rem}
.stat .v{font-family:var(--mono);font-size:1.28rem;font-variant-numeric:tabular-nums;
  font-weight:600;line-height:1.1}
.stat .k{font-size:.66rem;letter-spacing:.12em;text-transform:uppercase;color:var(--text-faint)}
.vint{font-size:.7rem;color:var(--text-faint);font-family:var(--mono);flex-basis:100%}
.vint.stale{color:var(--warn)}

/* alerts / failures ---------------------------------------------------- */
.alert{padding:.8rem 1rem;border-radius:5px;font-size:.88rem;
  background:var(--crit-bg);color:var(--crit);border:1px solid transparent;font-weight:600}
.pf{padding:.8rem 1rem;border-radius:5px;background:var(--crit-bg);color:var(--crit);
  font-size:.84rem;font-family:var(--mono);border:1px solid transparent}
footer{font-size:.72rem;color:var(--text-faint);line-height:1.7;
  border-top:1px solid var(--line);padding-top:1.1rem}
footer code{background:none;padding:0;color:var(--text-dim)}
a{color:var(--accent)}
@media (max-width:34rem){
  .day{grid-template-columns:4.2rem 1fr;gap:.6rem}
  .day .in{display:none}
  .book{gap:1.1rem}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""


def render(brief_written, brief, dates, acts, money, channels, fired):
    now = dt.datetime.now()
    P = []
    A = P.append

    A(f"<style>{CSS}</style>")
    A('<div class="wrap">')

    # ---- masthead: headline is the ONE thing, per the "summary before detail" rule
    head = brief.get("HEADLINE", "")
    A('<header class="mast">')
    A('<div class="eyebrow">Desk brief</div>')
    A(f"<h1>{md_inline(head) if head else 'No headline written — see PROME/BRIEF.md'}</h1>")
    stale_story = ""
    if brief_written:
        try:
            wd = dt.datetime.strptime(brief_written.split(" ET")[0].strip(),
                                      "%Y-%m-%d %H:%M")
            hrs = (now - wd).total_seconds() / 3600
            stale_story = ' class="stale"' if hrs > 20 else ""
        except ValueError:
            pass
    A('<div class="clocks">')
    A(f'<span>Facts rebuilt {now:%b %-d, %-I:%M %p} {ET}</span>')
    A(f'<span{stale_story}>Story written {html.escape(brief_written or "— NOT STAMPED")}</span>')
    A("</div></header>")

    if fired:
        A(f'<div class="alert">Gate fired and not acted on: {", ".join(html.escape(f) for f in fired)}'
          " — this blocks new work until it is cleared.</div>")

    # ---- the story
    A("<section>")
    A("<h2>What is going on</h2>")
    A(f'<div class="prose">{md_block(brief.get("STORY", ""))}</div>')
    if brief.get("QUESTION"):
        A(f'<p class="pull">{md_inline(" ".join(brief["QUESTION"].split()))}</p>')
    A("</section>")

    # ---- the book
    A("<section><h2>Where you stand</h2>")
    if money:
        vs = " stale" if money["age"] > 4 else ""
        A('<div class="book">')
        A(f'<div class="stat"><span class="v">${money["total"]}</span>'
          '<span class="k">Account</span></div>')
        A(f'<div class="stat"><span class="v">{money["cash_pct"]}%</span>'
          '<span class="k">Cash</span></div>')
        A(f'<div class="vint{vs}">Broker export {money["vintage"]} · marks {money["marks"]}'
          f' · {money["age"]}d old — not live, re-check before any fill</div>')
        A("</div>")
    if brief.get("POSITION"):
        A(f'<div class="prose">{md_block(brief["POSITION"])}</div>')
    A("</section>")

    # ---- the clock (real sequence -> ordered list is honest here)
    A("<section><h2>What is coming</h2>")
    if dates:
        A('<ol class="days">')
        for d in dates:
            k = " key" if d["star"] or d["days"] <= 1 else ""
            when = dt.date.fromisoformat(d["date"]).strftime("%a %-m/%-d")
            inn = "today" if d["days"] == 0 else ("tomorrow" if d["days"] == 1
                                                  else f'{d["days"]}d')
            also = (f' <span class="also">+{d["also"]} more</span>' if d["also"] else "")
            A(f'<li class="day{k}"><span class="when">{when}</span>'
              f'<span class="what">{html.escape(d["title"])}{also}</span>'
              f'<span class="in">{inn}</span></li>')
        A("</ol>")
    A("</section>")

    # ---- what you do
    A("<section><h2>What needs you</h2>")
    if acts:
        A('<ul class="acts">')
        for a in acts:
            cls = ""
            if a["due"]:
                dd = (dt.date.fromisoformat(a["due"]) - dt.date.today()).days
                cls = " due" if dd <= 0 else (" soon" if dd <= 2 else "")
            A(f'<li class="act{cls}"><div class="top">'
              f'<span class="name">{html.escape(a["item"])}</span>'
              f'<span class="when">{html.escape(a["due_txt"]) if a["due_txt"] else "no date"}</span>'
              "</div>")
            if a["rec"]:
                A(f'<div class="rec">{html.escape(a["rec"])}</div>')
            A("</li>")
        A("</ul>")
    if brief.get("WATCH"):
        A(f'<div class="prose">{md_block(brief["WATCH"])}</div>')
    A("</section>")

    # ---- pressure
    if channels:
        A("<section><h2>Where the pressure is</h2><div class=\"chips\">")
        label = {"crit": "critical", "elev": "elevated", "watch": "watching", "none": "quiet"}
        for name, st in channels.items():
            A(f'<span class="chip {html.escape(st)}"><span class="dot"></span>'
              f"{html.escape(name)} · {label.get(st, st)}</span>")
        A("</div></section>")

    if failures:
        A("<section><h2>Broken on this page</h2>")
        for sec, owner, why in failures:
            A(f'<div class="pf">PARSE-FAILED · {html.escape(sec)} — {html.escape(owner)}: '
              f"{html.escape(why)}</div>")
        A("</section>")

    A("<footer>")
    A("The story is written by PROME and carries its own date — it is judgment, not data. "
      "Everything else is generated from canon at build time and owns nothing: "
      "<code>PROME/DOCKET.tsv</code>, <code>PROME/WILL_QUEUE.md</code>, "
      "<code>PROME/GATES.tsv</code>, <code>FORGE/STATUS.md</code>. "
      "If this page and canon disagree, canon is right and the parser is broken.<br>"
      "Money figures are a broker mirror and go stale from the moment they are written — "
      "never fill against them. "
      "Rebuild: <code>python3 PROME/tools/will_brief.py</code> then republish to the same URL.")
    A("</footer></div>")
    return "\n".join(P)


def main():
    ap = argparse.ArgumentParser(description="Generate Will's briefing page.")
    ap.add_argument("-o", "--out", default="/tmp/will_brief.html")
    args = ap.parse_args()

    written, brief = parse_brief()
    page = render(written, brief, parse_dates(), parse_actions(), parse_money(),
                  parse_channels(), parse_gate_blockers())
    Path(args.out).write_text(
        f"<title>Desk brief</title>\n{page}\n", encoding="utf-8")
    print(f"wrote {args.out} ({len(page)} bytes)"
          + (f" · {len(failures)} PARSE-FAILED block(s)" if failures else " · clean"))


if __name__ == "__main__":
    main()
