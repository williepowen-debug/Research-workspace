#!/usr/bin/env python3
"""decision_deck.py — Will's Decision Deck (WQ-202, Will-ruled 2026-09-10 11:01 ET).

A PROJECTION of PROME's decision rails into one scrollable page:
  Owed      — every OPEN row of PROME/WILL_QUEUE.md (soonest first; blocked rows last)
  Decided   — every DONE row: WILL_QUEUE RECENTLY DONE + PROME/archive/WILL_QUEUE_ROWS_*.md
  In-flight — PROME/ACTIVE_DECISIONS.md live index
  Docket    — PROME/DOCKET.tsv rows whose owner cell names Will (non-terminal)
  Key       — what the ID families are; how tap-to-rule works; the privacy rule
Plain-English blocks come ONLY from PROME/registry/WQ_EXPLAINERS.tsv (sidecar keyed by
row number); a row without one renders "explainer owed" — the page never invents.

Never a second truth: regenerate from the source files (every PROME closeout) and
republish. Tap-to-rule writes to the artifact's `db` store (collection `rulings`);
PROME reads it at boot (Artifact tool read_db) and writes the ruling into the queue.

Usage:  python3 PROME/tools/decision_deck.py [-o PROME/artifacts/decision_deck.html]
        --selftest   parse-shape drills on the live sources (counts + required fields)
"""
from __future__ import annotations
import argparse, datetime as dt, glob, html, json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                           text=True, check=True).stdout.strip())
Q = ROOT / "PROME/WILL_QUEUE.md"
AD = ROOT / "PROME/ACTIVE_DECISIONS.md"
DOCKET = ROOT / "PROME/DOCKET.tsv"
EXPL = ROOT / "PROME/registry/WQ_EXPLAINERS.tsv"
ARCH = sorted(glob.glob(str(ROOT / "PROME/archive/WILL_QUEUE_ROWS_*.md")), reverse=True)
TERMINAL = re.compile(r"✅|DONE\b|RESOLVED\b|TERMINAL\b|DECLINED\b|RULED\b|EXECUTED\b")

# ---------------------------------------------------------------- helpers

def cells(line: str) -> list[str]:
    return [x.strip() for x in line.strip().strip("|").split("|")]

def strip_md(s: str) -> str:
    s = re.sub(r"\*\*|`|~~", "", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return s.strip()

def md(s: str) -> str:
    """Tiny inline-markdown → HTML. Escape first, then the fleet's four forms."""
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<span class="ref" title="\2">\1</span>', s)
    s = re.sub(r"~~(.+?)~~", r"<s>\1</s>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)([^*]+?)\*(?![\w*])", r"<em>\1</em>", s)
    return s

def first_date(s: str) -> str | None:
    m = re.search(r"\d{4}-\d{2}-\d{2}", s)
    return m.group(0) if m else None

def title_of(item: str, n: int = 88) -> str:
    """Name = the bold lead of the Item cell, else the first sentence, trimmed."""
    m = re.match(r"\s*(?:~~[^~]+~~\s*)*\*\*(.+?)\*\*", item)
    t = strip_md(m.group(1)) if m else strip_md(item)
    t = re.split(r"(?<=[.?!])\s|\s—\s", t, 1)[0]
    return (t[: n - 1] + "…") if len(t) > n else t

# ---------------------------------------------------------------- sources

def load_explainers() -> dict[str, dict]:
    out = {}
    if not EXPL.exists():
        return out
    lines = EXPL.read_text(encoding="utf-8").splitlines()
    hdr = lines[0].split("\t")
    for l in lines[1:]:
        if not l.strip():
            continue
        c = l.split("\t")
        out[c[0].strip()] = dict(zip(hdr, c))
    return out

def parse_open(text: str) -> list[dict]:
    sec = text.split("## OPEN", 1)[-1].split("\n## ", 1)[0]
    rows = []
    for line in sec.splitlines():
        if not line.startswith("|"):
            continue
        c = cells(line)
        if len(c) < 6 or not re.match(r"\d", c[0]):
            continue
        lead = re.sub(r"^(?:~~[^~]+~~\s*)+", "", c[1])
        lead = re.sub(r"^[\*\s]+", "", lead)
        if re.match(r"✅|DONE\b|RESOLVED\b|TERMINAL\b|DECLINED\b", lead):
            continue  # closed-in-place (mirrors will_brief/prome_gate)
        rows.append({
            "n": c[0], "item": c[1], "kind": strip_md(c[2]), "by_raw": c[3],
            "by": first_date(c[3]), "since": strip_md(c[4]), "rec": c[5],
            "notes": c[6] if len(c) > 6 else "",
            "blocked": bool(re.search(r"⛔\s*wait", line)),
            "name": title_of(c[1]),
        })
    return rows

def parse_done_table(text: str, source: str) -> list[dict]:
    """3-col done rows: | **NNN Title** | Done | Record |  (also un-bolded 'NNN Title')."""
    rows = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        c = cells(line)
        if len(c) < 3:
            continue
        m = re.match(r"\s*\**\s*(\d+[a-z]?)\b\s*(.*)", c[0])
        if not m or c[0].lower().startswith("item"):
            continue
        n, title = m.group(1), strip_md(m.group(2)).rstrip("*").strip()
        rows.append({"n": n, "name": title or f"WQ-{n}", "done": strip_md(c[1]),
                     "record": c[2], "source": source})
    return rows

def parse_done_open_style(text: str, source: str) -> list[dict]:
    """7-col open-style rows carried in an archive (the 8/16 rotation shape)."""
    rows = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        c = cells(line)
        if len(c) < 6 or not re.match(r"^\d+[a-z]?$", c[0]):
            continue
        lead = strip_md(c[1])
        dm = re.search(r"(?:DONE|RULED|RESOLVED|DECLINED|EXECUTED)\s*([0-9/]+)", lead)
        rows.append({"n": c[0], "name": title_of(c[1]), "done": dm.group(1) if dm else "—",
                     "record": c[1], "source": source})
    return rows

def parse_decided() -> list[dict]:
    text = Q.read_text(encoding="utf-8")
    done_sec = text.split("## RECENTLY DONE", 1)[-1].split("\n## ", 1)[0] if "## RECENTLY DONE" in text else ""
    out = parse_done_table(done_sec, "WILL_QUEUE.md § RECENTLY DONE")
    for f in ARCH:
        t = Path(f).read_text(encoding="utf-8")
        src = "archive/" + Path(f).name
        got = parse_done_table(t, src)
        if not got:
            got = parse_done_open_style(t, src)
        out.extend(got)
    seen, uniq = set(), []
    for r in out:  # first seen wins: live table, then newest archive
        if r["n"] in seen:
            continue
        seen.add(r["n"]); uniq.append(r)
    def key(r):
        m = re.match(r"(\d+)", r["n"]); return -int(m.group(1)) if m else 0
    uniq.sort(key=key)
    return uniq

def parse_active() -> list[dict]:
    if not AD.exists():
        return []
    text = AD.read_text(encoding="utf-8")
    sec = text.split("## Live Decision Index", 1)[-1].split("\n## ", 1)[0]
    rows = []
    for line in sec.splitlines():
        if not line.startswith("|"):
            continue
        c = cells(line)
        if len(c) < 6 or c[0].lower().startswith("decision") or set(c[0]) <= {"-", ":"}:
            continue
        rows.append({"name": strip_md(c[0]), "state": c[1], "owner": c[2], "next": c[3],
                     "backstop": c[4], "source": c[5]})
    return rows

def parse_docket(today: dt.date) -> list[dict]:
    if not DOCKET.exists():
        return []
    rows = []
    for i, line in enumerate(DOCKET.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("#") or not line.strip():
            continue
        c = line.split("\t")
        if len(c) < 4 or not re.match(r"\d{4}-\d{2}-\d{2}", c[0]) and "next-" not in c[0]:
            continue
        owner, status = c[2], c[3]
        if "will" not in owner.lower():
            continue
        if re.match(r"\s*(RESOLVED|DONE|WITHDRAWN|CANCELLED|SUPERSEDED)", status, re.I):
            continue
        d = first_date(c[0])
        rows.append({"L": i, "date": c[0], "d": d, "catalyst": c[1], "owner": owner,
                     "status": status, "artifact": c[4] if len(c) > 4 else "",
                     "days": (dt.date.fromisoformat(d) - today).days if d else None})
    rows.sort(key=lambda r: (r["d"] or "9999", r["L"]))
    return rows

# ---------------------------------------------------------------- render

def due_pill(by: str | None, days: int | None, blocked: bool) -> str:
    if blocked:
        return '<span class="pill wait">waits on others</span>'
    if by is None:
        return '<span class="pill soft">no hard date</span>'
    if days is None:
        return f'<span class="pill soft">{html.escape(by)}</span>'
    if days < 0:
        return f'<span class="pill crit">overdue {-days}d · {by}</span>'
    if days == 0:
        return f'<span class="pill crit">due today · {by}</span>'
    if days <= 2:
        return f'<span class="pill warn">{days}d left · {by}</span>'
    return f'<span class="pill ok">{days}d left · {by}</span>'

def render_owed(rows: list[dict], expl: dict, today: dt.date) -> str:
    out = []
    for r in rows:
        days = (dt.date.fromisoformat(r["by"]) - today).days if r["by"] else None
        r["days"] = days
        e = expl.get(r["n"])
        name = e["name"] if e and e.get("name") else r["name"]
        if e:
            block = (
                '<dl class="expl">'
                f'<dt>What it is</dt><dd>{html.escape(e["what"])}</dd>'
                f'<dt>Why it is yours</dt><dd>{html.escape(e["why_yours"])}</dd>'
                f'<dt>If yes</dt><dd>{html.escape(e["if_yes"])}</dd>'
                f'<dt>If no</dt><dd>{html.escape(e["if_no"])}</dd>'
                f'<dt>If nothing</dt><dd>{html.escape(e["if_nothing"])}</dd>'
                '</dl>'
                f'<p class="rec"><span class="lbl">PROME rec</span> {html.escape(e["rec_reason"])}</p>'
            )
        else:
            block = ('<p class="owed-note">Explainer owed — PROME writes the plain-English block at the next touch. '
                     'The row text is below.</p>'
                     f'<p class="rec"><span class="lbl">PROME rec</span> {md(strip_md(r["rec"]))}</p>')
        detail = (
            '<details class="raw"><summary>Row as written in the queue</summary>'
            f'<p><span class="lbl">Item</span> {md(r["item"])}</p>'
            f'<p><span class="lbl">Needed by</span> {md(r["by_raw"])}</p>'
            f'<p><span class="lbl">PROME rec</span> {md(r["rec"])}</p>'
            + (f'<p><span class="lbl">Notes</span> {md(r["notes"])}</p>' if r["notes"] else "")
            + '</details>'
        )
        ctl = "" if r["blocked"] else (
            f'<div class="tap" data-wq="{r["n"]}">'
            '<div class="tapstate" hidden></div>'
            '<div class="tapbtns">'
            f'<button type="button" class="btn approve" data-v="APPROVE" id="ap-{r["n"]}">Approve</button>'
            f'<button type="button" class="btn decline" data-v="DECLINE" id="dc-{r["n"]}">Decline</button>'
            f'<button type="button" class="btn later" data-v="LATER" id="lt-{r["n"]}">Later</button>'
            '</div>'
            f'<input type="text" class="note" id="note-{r["n"]}" placeholder="Note to PROME (optional) — e.g. 200 = 1+3, or a different level" maxlength="400">'
            '</div>'
        )
        out.append(
            f'<article class="card{" blocked" if r["blocked"] else ""}" id="wq-{r["n"]}" data-wq="{r["n"]}">'
            f'<div class="rail"><span class="num">WQ-{r["n"]}</span>{due_pill(r["by"], days, r["blocked"])}{TOGGLE}</div>'
            '<div class="body">'
            f'<div class="meta"><span class="pill type">{html.escape(r["kind"])}</span>'
            f'<span class="since">open since {html.escape(r["since"])}</span></div>'
            f'<h2>{html.escape(name)}</h2>'
            f'{block}{detail}{ctl}'
            '</div></article>'
        )
    return "\n".join(out)

def render_decided(rows: list[dict]) -> str:
    out = []
    for r in rows:
        out.append(
            f'<article class="card done" id="wq-{r["n"]}">'
            f'<div class="rail"><span class="num">WQ-{r["n"]}</span><span class="pill soft" title="{html.escape(r["source"])}">done {html.escape(r["done"])}</span>{TOGGLE}</div>'
            f'<div class="body"><h2>{html.escape(r["name"])}</h2>'
            f'<details class="raw" open><summary>Ruling / record</summary><p>{md(r["record"])}</p></details>'
            '</div></article>'
        )
    return "\n".join(out)

def render_active(rows: list[dict]) -> str:
    out = []
    for i, r in enumerate(rows):
        out.append(
            f'<article class="card flight" id="ad-{i}">'
            '<div class="rail"><span class="num">AD</span>' + TOGGLE + '</div>'
            f'<div class="body"><h2>{html.escape(r["name"])}</h2>'
            f'<p><span class="lbl">State</span> {md(r["state"])}</p>'
            f'<p><span class="lbl">Owner</span> {md(r["owner"])}</p>'
            f'<p><span class="lbl">Next</span> {md(r["next"])}</p>'
            f'<details class="raw"><summary>Backstop and source</summary><p>{md(r["backstop"])}</p><p>{md(r["source"])}</p></details>'
            '</div></article>'
        )
    return "\n".join(out) or '<p class="empty">No live decision rows.</p>'

def render_docket(rows: list[dict]) -> str:
    out = []
    for r in rows:
        pill = due_pill(r["d"], r["days"], False) if r["d"] else f'<span class="pill soft">{html.escape(r["date"])}</span>'
        out.append(
            f'<article class="card docket" id="L{r["L"]}">'
            f'<div class="rail"><span class="num">L{r["L"]}</span>{pill}{TOGGLE}</div>'
            f'<div class="body"><h2>{html.escape(strip_md(r["catalyst"])[:160])}</h2>'
            f'<p><span class="lbl">Owner</span> {md(r["owner"])}</p>'
            f'<p><span class="lbl">Status</span> {md(r["status"][:400])}</p>'
            + (f'<details class="raw"><summary>Full catalyst text</summary><p>{md(r["catalyst"])}</p><p><span class="lbl">Artifact</span> <code>{html.escape(r["artifact"])}</code></p></details>' if len(r["catalyst"]) > 160 or r["artifact"] else "")
            + '</div></article>'
        )
    return "\n".join(out) or '<p class="empty">No docket rows name you.</p>'

TOGGLE = '<button type="button" class="tg" aria-expanded="true" title="Minimize or expand this card"><span class="tg-min">Minimize</span><span class="tg-max">Expand</span></button>'

KEY = """
<section class="key">
<h2>What the numbers are</h2>
<dl class="expl">
<dt>WQ-n</dt><dd>Your queue. A decision or action only you can take. Registered before it is ever asked, so you rule by number. Lives in <code>PROME/WILL_QUEUE.md</code>; done rows roll to <code>PROME/archive/</code>.</dd>
<dt>L-n</dt><dd>A docket row: a dated catalyst, cited by its physical line in <code>PROME/DOCKET.tsv</code>. The Docket tab shows only the rows that name you.</dd>
<dt>AD</dt><dd>A live row of <code>PROME/ACTIVE_DECISIONS.md</code>: a decision that is approved or in motion but not finished. In-flight, not owed.</dd>
<dt>D-n</dt><dd>A discrepancy between the position mirror and your broker, in <code>FORGE/STATUS.md</code>. Some are yours to answer (a fill date), some are a desk's.</dd>
<dt>GATE-…</dt><dd>A registered fire trigger with a written condition and a consequence, in <code>PROME/GATES.tsv</code>. A fired gate produces a proposal; nothing executes on its own.</dd>
<dt>SIG-W-…</dt><dd>A WALTER signal: a news or data item routed to a desk's inbox.</dd>
<dt>Types</dt><dd><strong>[Approve]</strong> a trade or proposal · <strong>RULE</strong> a canon or disposition ruling · <strong>ACTION</strong> your hands · <strong>BROKER</strong> exports and confirms · <strong>LAUNCH</strong> open a desk · <strong>chore</strong> PROME housekeeping parked here so it has a home.</dd>
</dl>
<h2>How a tap works</h2>
<p>Approve, Decline, or Later writes one record to this page's private store: the row number, your verdict, your note, the time. Nothing executes off a tap. At PROME's next boot it reads the store, writes your word into the queue verbatim as <em>"tap via Decision Deck"</em>, and marks the record picked up. The card shows its tap state until the next publish removes it. Trade and spend consequents still follow their own rails; a tap is your word arriving through a page instead of a message.</p>
<h2>The privacy rule</h2>
<p>The page cannot tell who tapped. A tap counts as your word only because this artifact is private to your account. It is never shared. If it were, taps would stop being authenticated and PROME would stop consuming them.</p>
<h2>Where this comes from</h2>
<p>Generated by <code>PROME/tools/decision_deck.py</code> at every PROME closeout from the queue, its archives, the active-decisions index, the docket, and the explainer sidecar <code>PROME/registry/WQ_EXPLAINERS.tsv</code>. A projection, never a second truth: if this page and a source file disagree, the file wins.</p>
</section>
"""

CSS = """
:root{--bg:#F4F6F3;--surface:#FFFFFF;--ink:#1B2422;--muted:#5C6864;--line:#D6DDD8;--chip:#E8EEEB;
--accent:#0E6B68;--accent-ink:#FFFFFF;--warn:#A8650B;--crit:#A33A2C;--ok:#2E7A4B;--wait:#6B6F8A;
--rec:#EAF3F1;--focus:#0E6B68}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#121918;--surface:#1A2321;--ink:#E6ECE9;--muted:#98A5A0;--line:#2C3835;--chip:#24302D;
--accent:#45B5AF;--accent-ink:#0F1A19;--warn:#E0A44A;--crit:#E07A6A;--ok:#6CC08B;--wait:#A6ABC9;--rec:#1E2D2B;--focus:#45B5AF}}
:root[data-theme="dark"]{--bg:#121918;--surface:#1A2321;--ink:#E6ECE9;--muted:#98A5A0;--line:#2C3835;--chip:#24302D;
--accent:#45B5AF;--accent-ink:#0F1A19;--warn:#E0A44A;--crit:#E07A6A;--ok:#6CC08B;--wait:#A6ABC9;--rec:#1E2D2B;--focus:#45B5AF}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 "IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;padding-inline:16px;padding-block:0 64px}
.wrap{max-width:820px;margin:0 auto}
header.top{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding-block:14px 0;margin-inline:-16px;padding-inline:16px}
header.top .wrap{display:flex;flex-direction:column;gap:10px}
.brand{display:flex;align-items:baseline;justify-content:space-between;gap:12px;flex-wrap:wrap}
h1{font:600 26px/1.15 "Fraunces",Georgia,serif;margin:0;letter-spacing:-.01em;text-wrap:balance}
.build{font:12px/1.4 "IBM Plex Mono",ui-monospace,Menlo,monospace;color:var(--muted)}
.tabs{display:flex;gap:4px;overflow-x:auto;scrollbar-width:none}
.tabs::-webkit-scrollbar{display:none}
.tab{appearance:none;border:0;background:transparent;color:var(--muted);font:600 13px/1 "IBM Plex Sans",sans-serif;letter-spacing:.04em;text-transform:uppercase;padding:10px 12px 12px;border-bottom:2px solid transparent;cursor:pointer;white-space:nowrap}
.tab .n{font:500 12px/1 "IBM Plex Mono",monospace;background:var(--chip);color:var(--ink);border-radius:999px;padding:3px 7px;margin-left:6px}
.tab[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--accent)}
.tab:focus-visible,.btn:focus-visible,.note:focus-visible,summary:focus-visible{outline:2px solid var(--focus);outline-offset:2px}
.panel{padding-block:18px}
.panel[hidden]{display:none}
.store{font:13px/1.4 "IBM Plex Mono",monospace;color:var(--muted);margin:0 0 14px;display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.store .dot{width:8px;height:8px;border-radius:50%;background:var(--muted);display:inline-block}
.store.live .dot{background:var(--ok)}
.card{display:flex;flex-direction:column;gap:4px;background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:16px 18px;margin-bottom:14px}
.card.blocked{opacity:.78}
.rail{display:flex;flex-direction:row;flex-wrap:wrap;gap:8px 10px;align-items:center;margin-bottom:6px}
.tg{margin-left:auto;appearance:none;border:1px solid var(--line);background:transparent;color:var(--muted);font:500 11.5px/1 "IBM Plex Mono",monospace;padding:5px 9px;border-radius:999px;cursor:pointer}
.tg .tg-max{display:none}.card.min .tg .tg-min{display:none}.card.min .tg .tg-max{display:inline}
.card.min .body > *:not(h2):not(.meta){display:none}.card.min .body h2{margin-bottom:0}.card.min{gap:0}
.panelbar{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap;margin:0 0 14px}.panelbar .store{margin:0}
.panelctl{display:flex;gap:10px}.lnk{appearance:none;border:0;background:transparent;color:var(--accent);font:600 12px/1 "IBM Plex Sans",sans-serif;cursor:pointer;padding:4px 0;text-decoration:underline;text-underline-offset:3px}
.num{font:600 16px/1 "IBM Plex Mono",monospace;color:var(--accent);letter-spacing:.02em;margin-right:4px}
.pill{display:inline-block;font:500 11.5px/1.3 "IBM Plex Mono",monospace;padding:4px 9px;border-radius:999px;background:var(--chip);color:var(--ink)}
.pill.crit{background:var(--crit);color:#fff}.pill.warn{background:var(--warn);color:#fff}.pill.ok{background:var(--chip);color:var(--ok)}
.pill.wait{color:var(--wait)}.pill.soft{color:var(--muted)}.pill.type{background:var(--chip)}
.meta{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:8px}
.since{font:12px/1.4 "IBM Plex Mono",monospace;color:var(--muted)}
.card h2{font:600 20px/1.25 "Fraunces",Georgia,serif;margin:0 0 12px;letter-spacing:-.005em;text-wrap:balance}
.expl{display:grid;grid-template-columns:128px 1fr;gap:8px 16px;margin:0 0 14px}
.expl dt{font:600 11.5px/1.6 "IBM Plex Sans",sans-serif;letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}
.expl dd{margin:0;max-width:62ch}
.lbl{font:600 11px/1.6 "IBM Plex Sans",sans-serif;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);margin-right:6px}
.rec{background:var(--rec);border-left:3px solid var(--accent);padding:10px 12px;margin:0 0 12px;border-radius:0 4px 4px 0;max-width:70ch}
.owed-note{color:var(--warn);margin:0 0 10px}
details.raw{border-top:1px dashed var(--line);padding-top:8px;margin-top:4px;font-size:13.5px;color:var(--muted)}
details.raw summary{cursor:pointer;color:var(--ink);font-weight:600;font-size:13px}
details.raw p{margin:8px 0;line-height:1.55;overflow-wrap:anywhere}
details.raw code,.expl code,.key code{font:12.5px/1.4 "IBM Plex Mono",monospace;background:var(--chip);padding:1px 5px;border-radius:3px}
.ref{border-bottom:1px dotted var(--muted)}
.tap{margin-top:12px;border-top:1px solid var(--line);padding-top:12px;display:flex;flex-direction:column;gap:10px}
.tapbtns{display:flex;gap:8px;flex-wrap:wrap}
.btn{appearance:none;border:1px solid var(--line);background:var(--surface);color:var(--ink);font:600 13.5px/1 "IBM Plex Sans",sans-serif;padding:10px 16px;border-radius:4px;cursor:pointer;min-width:96px}
.btn.approve{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
.btn.decline{border-color:var(--crit);color:var(--crit)}
.btn:disabled{opacity:.45;cursor:not-allowed}
.note{border:1px solid var(--line);background:var(--bg);color:var(--ink);padding:9px 11px;border-radius:4px;font:14px/1.4 "IBM Plex Sans",sans-serif;width:100%}
.tapstate{font:13px/1.5 "IBM Plex Mono",monospace;padding:8px 10px;border-radius:4px;background:var(--chip)}
.tapstate.sent{color:var(--ok)}.tapstate.err{color:var(--crit)}
.grp{font:600 12px/1.6 "IBM Plex Mono",monospace;color:var(--muted);letter-spacing:.04em;margin:18px 0 8px}
.empty{color:var(--muted)}
.key h2{font:600 19px/1.25 "Fraunces",Georgia,serif;margin:18px 0 8px}
.key p{max-width:68ch}
.toast{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);background:var(--ink);color:var(--bg);padding:10px 14px;border-radius:6px;font:13.5px/1.4 "IBM Plex Sans",sans-serif;opacity:0;transition:opacity .2s;pointer-events:none;max-width:90vw}
.toast.on{opacity:1}
@media (max-width:560px){.expl{grid-template-columns:1fr;gap:2px 0}.expl dd{margin-bottom:8px}}
@media (prefers-reduced-motion:reduce){.toast{transition:none}}
"""

JS = r"""
(function(){
  var BUILD = document.body.dataset.build;
  var toastEl = document.getElementById('toast');
  function toast(m){ toastEl.textContent = m; toastEl.classList.add('on'); clearTimeout(toast.t); toast.t = setTimeout(function(){toastEl.classList.remove('on');}, 2600); }
  // tabs
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.tab'));
  var panels = Array.prototype.slice.call(document.querySelectorAll('.panel'));
  function show(id){
    tabs.forEach(function(t){ t.setAttribute('aria-selected', t.dataset.for===id ? 'true':'false'); });
    panels.forEach(function(p){ p.hidden = p.id!==id; });
    try{ localStorage.setItem('deck.tab', id); }catch(e){}
  }
  tabs.forEach(function(t){ t.addEventListener('click', function(){ show(t.dataset.for); }); });
  var start = 'owed';
  try{ var s = localStorage.getItem('deck.tab'); if (s && document.getElementById(s)) start = s; }catch(e){}
  if (location.hash && /^#wq-/.test(location.hash)) { var el = document.querySelector(location.hash); if (el) start = el.closest('.panel').id; }
  show(start);
  // minimize / expand cards (remembered per card in this browser)
  function setMin(card, on, remember){
    card.classList.toggle('min', on);
    var b = card.querySelector('.tg'); if (b) b.setAttribute('aria-expanded', on ? 'false' : 'true');
    if (remember) { try{ localStorage.setItem('deck.min.' + card.id, on ? '1' : '0'); }catch(e){} }
  }
  Array.prototype.slice.call(document.querySelectorAll('.card')).forEach(function(card){
    var on = false; try{ on = localStorage.getItem('deck.min.' + card.id) === '1'; }catch(e){}
    if (on) setMin(card, true, false);
    var b = card.querySelector('.tg'); if (b) b.addEventListener('click', function(){ setMin(card, !card.classList.contains('min'), true); });
  });
  Array.prototype.slice.call(document.querySelectorAll('.lnk[data-all]')).forEach(function(b){
    b.addEventListener('click', function(){
      var panel = b.closest('.panel'); var on = b.dataset.all === 'min';
      Array.prototype.slice.call(panel.querySelectorAll('.card')).forEach(function(c){ setMin(c, on, true); });
    });
  });
  // tap-to-rule
  var storeLine = document.getElementById('store');
  var buttons = Array.prototype.slice.call(document.querySelectorAll('.btn'));
  buttons.forEach(function(b){ b.disabled = true; });
  function setState(wq, cls, text){
    var card = document.getElementById('wq-'+wq); if(!card) return;
    var st = card.querySelector('.tapstate'); if(!st) return;
    st.className = 'tapstate ' + cls; st.textContent = text; st.hidden = false;
  }
  function fmt(iso){ try{ return new Date(iso).toLocaleString(undefined,{month:'numeric',day:'numeric',hour:'numeric',minute:'2-digit'}); }catch(e){ return iso; } }
  if (!(window.claude && window.claude.use)) { storeLine.textContent = 'Tap-to-rule is off in this view (no runtime). Reading only.'; return; }
  storeLine.textContent = 'Connecting to the ruling store…';
  window.claude.use('db').then(function(db){
    if (!db) { storeLine.textContent = 'Tap-to-rule unavailable in this view. Reading only; rule by message instead.'; return; }
    storeLine.classList.add('live'); storeLine.innerHTML = '<span class="dot"></span> Ruling store connected. A tap is your word; PROME picks it up at its next boot.';
    buttons.forEach(function(b){ b.disabled = false; });
    var col = db.collection('rulings');
    col.onSnapshot(function(snap){
      var latest = {};
      snap.docs.forEach(function(d){ var x = d.data() || {}; if (!x.wq) return; if (!latest[x.wq] || (x.ts||'') > (latest[x.wq].ts||'')) latest[x.wq] = x; });
      Object.keys(latest).forEach(function(wq){
        var x = latest[wq];
        var when = x.ts ? fmt(x.ts) : '';
        if (x.consumed) setState(wq, 'sent', 'Ruled by tap ' + when + ': ' + x.verdict + (x.note ? ' — ' + x.note : '') + ' · picked up by PROME');
        else setState(wq, 'sent', 'Tapped ' + when + ': ' + x.verdict + (x.note ? ' — ' + x.note : '') + ' · awaiting PROME pickup');
      });
    }, function(e){ storeLine.textContent = 'Ruling store error: ' + (e && e.code ? e.code : 'unknown'); });
    buttons.forEach(function(b){
      b.addEventListener('click', function(){
        var wrap = b.closest('.tap'); var wq = wrap.dataset.wq; var verdict = b.dataset.v;
        var note = (document.getElementById('note-'+wq) || {}).value || '';
        var ts = new Date().toISOString();
        var id = wq + '-' + ts.replace(/[^0-9]/g,'').slice(0,14);
        b.disabled = true;
        col.doc(id).set({wq: wq, verdict: verdict, note: note.trim(), ts: ts, build: BUILD, consumed: false, source: 'decision-deck'})
          .then(function(){ toast('Recorded: WQ-' + wq + ' ' + verdict); setState(wq, 'sent', 'Tapped ' + fmt(ts) + ': ' + verdict + (note ? ' — ' + note.trim() : '') + ' · awaiting PROME pickup'); b.disabled = false; })
          .catch(function(e){ b.disabled = false; var c = (e && e.code) || 'error'; setState(wq, 'err', 'Not recorded (' + c + '). Rule by message instead.'); toast('Not recorded: ' + c); });
      });
    });
  }).catch(function(){ storeLine.textContent = 'Tap-to-rule unavailable in this view. Reading only.'; });
})();
"""

def build(today: dt.date, out: Path) -> dict:
    text = Q.read_text(encoding="utf-8")
    expl = load_explainers()
    owed = parse_open(text)
    owed.sort(key=lambda r: (r["blocked"], r["by"] or "9999-99-99"))
    decided = parse_decided()
    active = parse_active()
    docket = parse_docket(today)
    sha = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=ROOT).stdout.strip()
    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    build_id = f"{sha}·{stamp}"
    actionable = [r for r in owed if not r["blocked"]]
    missing = [r["n"] for r in owed if r["n"] not in expl]
    page = f"""<title>Decision Deck</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>{CSS}</style>
<header class="top"><div class="wrap">
<div class="brand"><h1>Decision Deck</h1><span class="build">built {html.escape(stamp)} · {html.escape(sha)} · {len(actionable)} owed</span></div>
<div class="tabs" role="tablist">
<button type="button" class="tab" role="tab" data-for="owed" id="tab-owed">Owed<span class="n">{len(actionable)}</span></button>
<button type="button" class="tab" role="tab" data-for="decided" id="tab-decided">Decided<span class="n">{len(decided)}</span></button>
<button type="button" class="tab" role="tab" data-for="flight" id="tab-flight">In-flight<span class="n">{len(active)}</span></button>
<button type="button" class="tab" role="tab" data-for="docket" id="tab-docket">Docket<span class="n">{len(docket)}</span></button>
<button type="button" class="tab" role="tab" data-for="key" id="tab-key">Key</button>
</div></div></header>
<main class="wrap">
<section class="panel" id="owed" role="tabpanel"><div class="panelbar"><p class="store" id="store"><span class="dot"></span> Reading only.</p><span class="panelctl"><button type="button" class="lnk" data-all="min">Collapse all</button><button type="button" class="lnk" data-all="max">Expand all</button></span></div>{render_owed(owed, expl, today)}</section>
<section class="panel" id="decided" role="tabpanel" hidden><div class="panelbar"><p class="store">Every ruled or done row, newest first. Your word is quoted verbatim where it was recorded.</p><span class="panelctl"><button type="button" class="lnk" data-all="min">Collapse all</button><button type="button" class="lnk" data-all="max">Expand all</button></span></div>{render_decided(decided)}</section>
<section class="panel" id="flight" role="tabpanel" hidden><div class="panelbar"><p class="store">Approved or in motion, not finished. Nothing here is owed by you unless a card says so.</p><span class="panelctl"><button type="button" class="lnk" data-all="min">Collapse all</button><button type="button" class="lnk" data-all="max">Expand all</button></span></div>{render_active(active)}</section>
<section class="panel" id="docket" role="tabpanel" hidden><div class="panelbar"><p class="store">Dated catalysts whose owner cell names you.</p><span class="panelctl"><button type="button" class="lnk" data-all="min">Collapse all</button><button type="button" class="lnk" data-all="max">Expand all</button></span></div>{render_docket(docket)}</section>
<section class="panel" id="key" role="tabpanel" hidden>{KEY}</section>
</main>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script>document.body.dataset.build={json.dumps(build_id)};</script>
<script>{JS}</script>
"""
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    return {"owed": len(owed), "actionable": len(actionable), "decided": len(decided), "active": len(active),
            "docket": len(docket), "explainers_missing": missing, "bytes": len(page.encode()), "out": str(out)}

def selftest() -> int:
    today = dt.date.today()
    rc = 0
    def chk(name, ok, detail=""):
        nonlocal rc
        print(("  ✅ " if ok else "  ❌ ") + name + (f" — {detail}" if detail else ""))
        if not ok: rc = 1
    o = parse_open(Q.read_text(encoding="utf-8"))
    chk("OPEN parses to ≥1 row", len(o) >= 1, f"{len(o)} rows")
    chk("every OPEN row has n/kind/rec", all(r["n"] and r["kind"] and r["rec"] for r in o))
    chk("no OPEN row number duplicates", len({r["n"] for r in o}) == len(o))
    d = parse_decided()
    chk("DECIDED parses to ≥20 rows across live + archives", len(d) >= 20, f"{len(d)} rows")
    chk("DECIDED numbers unique", len({r["n"] for r in d}) == len(d))
    chk("no number appears in both OPEN and DECIDED", not ({r["n"] for r in o} & {r["n"] for r in d}),
        str({r["n"] for r in o} & {r["n"] for r in d}))
    a = parse_active()
    chk("ACTIVE_DECISIONS parses to ≥1 row", len(a) >= 1, f"{len(a)} rows")
    k = parse_docket(today)
    chk("DOCKET Will-owner rows parse", len(k) >= 1, f"{len(k)} rows")
    chk("docket rows carry a physical line number", all(r["L"] > 2 for r in k))
    e = load_explainers()
    chk("explainer sidecar has the 8 columns", all(len(v) == 8 for v in e.values()), f"{len(e)} rows")
    chk("md() escapes HTML before styling", md("<b>x</b> **y**") == "&lt;b&gt;x&lt;/b&gt; <strong>y</strong>")
    print("SELFTEST", "PASS" if rc == 0 else "FAIL")
    return rc

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--out", default=str(ROOT / "PROME/artifacts/decision_deck.html"))
    ap.add_argument("--today", default=None, help="YYYY-MM-DD (default: system date)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    today = dt.date.fromisoformat(a.today) if a.today else dt.date.today()
    r = build(today, Path(a.out))
    print(json.dumps(r, indent=1))
