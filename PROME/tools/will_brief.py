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
    which is judgment (the story, the falsifier, the disagreements) and cannot be
    parsed from a TSV.
  - TWO CLOCKS, SHOWN SEPARATELY. Facts carry the build stamp; the story carries
    BRIEF.md's own WRITTEN stamp. A stale story must READ as stale rather than
    ride the freshness of the generated half.
    [[finding_dated_stamp_is_a_trigger_not_a_shield]]
  - FAIL LOUD. A broken parser renders a visible PARSE-FAILED block naming the
    owner file. Never a silently-missing section — a briefing that quietly drops
    the thing that mattered is worse than no briefing.
  - POINTS, never owns. Money figures come from FORGE/STATUS.md WITH its vintage,
    never re-typed here.
  - JUDGMENT OVER DATA. v2 deliberately inverted the ratio: a page of facts cannot
    be "dumbed down" by removing facts. The cure for density is REPLACING data
    with judgment — and then making that judgment checkable (the falsifier).

V2 (2026-08-03, Will-directed, same day):
  + WHAT CHANGED feed (see CHANGE LOG below) · + FALSIFIER · + DISAGREEMENT
  + decisions/chores split · - pressure chips (4-of-7 channels read "crit": a row
  where the majority is at max has stopped discriminating) · dates 9 -> 5.

CHANGE LOG DESIGN — why an append-only log and not a two-point diff:
  a snapshot diff answers "what changed since the last BUILD", but Will asks
  "what changed since I last LOOKED". Those differ the moment PROME rebuilds
  twice between visits — the second build would silently show an empty delta and
  the real news would be gone. So diffs are APPENDED to PROME/state/brief_changes
  .jsonl with timestamps and the page renders the last N regardless of how many
  builds happened. Dedup is by (kind, text) within a build so a re-run cannot
  double-write [[finding_partial_record_written_as_final_never_heals]].
  Use --no-snapshot for test builds so they never burn the baseline.

USAGE
  python3 PROME/tools/will_brief.py -o /tmp/brief.html
  python3 PROME/tools/will_brief.py --no-snapshot -o /tmp/test.html   # dry run
  (then publish via the Artifact tool — SAME URL every time. From any session
   other than the one that minted it, pass url="..." or it orphans Will's tab.
   [[finding_artifact_redeploy_same_url]])

ARTIFACT_URL: https://claude.ai/code/artifact/76508dac-662b-4da4-a60b-c586e3a472ec
⛔ PAGE RETIRED 2026-08-21 (Will in-session: "lets just run that through the
handbook and retire the standalone") — the URL above carries a retirement
banner pointing at the Operator Handbook, whose brief tab renders BRIEF.md now.
THIS FILE LIVES ON as the parser/state library: will_handbook.py imports
parse_* + update_changes (write=True — the handbook run owns the change-feed
baseline since the same commit). Do NOT run this as a page generator at
closeout; do not delete it (prome_gate's queue-parser selftest reads it).
  (minted 2026-08-03. Same-conversation republish of the same file path keeps this URL.)
  FAVICON: 🧭 — keep identical on every republish; Will finds the tab by its icon.
"""
import argparse
import csv
import datetime as dt
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ET = "ET"


def ell(s, n):
    """Cap s at n chars, appending '…' ONLY when the slice actually shortened.
    A capped string with no suffix tells its reader that's the whole sentence —
    CHECK_STANDARD §4's silent-truncation class, on the rows whose only job is
    Will reading them (DAEDALUS Helm review 2026-08-21)."""
    s = s.strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"
SNAP = ROOT / "PROME/state/brief_snapshot.json"
CHANGES = ROOT / "PROME/state/brief_changes.jsonl"


def _persist_state(n_added):
    """Commit the two machine-written state files this tool exclusively owns.

    WHY THIS EXISTS (2026-08-04, DAEDALUS flag): brief_changes.jsonl is the
    APPEND-ONLY memory behind the brief's "since you last LOOKED" feed. Before
    this, it was committed when somebody remembered -- twice in its whole
    history -- so it sat dirty behind completed closeouts. Gitignoring it was
    the other option offered and is WRONG: the feed would silently empty on a
    machine switch, and an empty feed is indistinguishable from "nothing
    changed" (a false negative, the dangerous direction).

    A hand-commit is not a mechanism, so the generator persists its own state.

    Git discipline (root CLAUDE.md): pathspec commit, explicit paths only,
    never `git add .`/-A, never `git reset`. Fails SAFE and SILENT-ish -- a
    reporting tool must never block or crash on a git problem.
    """
    import subprocess
    paths = [str(p.relative_to(ROOT)) for p in (CHANGES, SNAP) if p.exists()]
    if not paths:
        return
    try:
        dirty = subprocess.run(["git", "status", "--porcelain", "--"] + paths,
                               cwd=ROOT, capture_output=True, text=True, timeout=15)
        if dirty.returncode != 0 or not dirty.stdout.strip():
            return  # nothing to persist, or git unavailable
        msg = (f"PROME brief state: {n_added} change row(s) + snapshot "
               f"(auto-persisted by will_brief.py)")
        r = subprocess.run(["git", "commit", "-m", msg, "--"] + paths,
                           cwd=ROOT, capture_output=True, text=True, timeout=30)
        if r.returncode != 0:
            print(f"  [warn] brief state not committed (harmless, commit it at "
                  f"closeout): {r.stderr.strip().splitlines()[:1]}")
    except Exception as e:
        print(f"  [warn] brief state not committed (harmless): {e}")

# Sections the parser keys on in BRIEF.md.
BRIEF_SECTIONS = ["HEADLINE", "STORY", "QUESTION", "FALSIFIER",
                  "DISAGREEMENT", "POSITION", "WATCH"]

# WILL_QUEUE Type column -> is this a JUDGMENT call or an errand?
# Rationale: approving capital and getting an API key are not the same species,
# and rendering them in one list flattens the urgency of the first.
DECISION_TYPES = {"[APPROVE]", "APPROVE", "LAUNCH", "RULE", "DECISION"}

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


def parse_dates(limit=5):
    """DOCKET.tsv — forward catalysts. PENDING only, today onward, soonest first.
    Cut 9 -> 5 in v2: anything past ~10 days is not a check-in concern."""
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
                    "title": ell(title, 74),
                    "star": "★" in r[1],
                })
    except Exception as e:
        return fail("the clock", "PROME/DOCKET.tsv", f"parse error: {e}") or []
    rows.sort(key=lambda x: (x["date"], not x["star"]))
    grouped, seen = [], {}
    for r in rows:
        if r["date"] in seen:
            seen[r["date"]]["also"] += 1
            # additive key (2026-08-21, Helm <details> expander — Will-directed):
            # collapsed same-day titles kept so renderers can expand the "+N more"
            # instead of dead-ending it; existing consumers unaffected.
            seen[r["date"]]["also_titles"].append(r["title"])
            seen[r["date"]]["star"] = seen[r["date"]]["star"] or r["star"]
            continue
        r["also"] = 0
        r["also_titles"] = []
        seen[r["date"]] = r
        grouped.append(r)
    return grouped[:limit]


def parse_actions():
    """WILL_QUEUE.md OPEN table, SPLIT into decisions vs chores (v2).
    Returns (decisions, chores) — each sorted dated-first."""
    p = ROOT / "PROME/WILL_QUEUE.md"
    try:
        text = p.read_text(encoding="utf-8")
    except Exception as e:
        return fail("what you do", "PROME/WILL_QUEUE.md", f"unreadable: {e}") or ([], [])
    section = text.split("## OPEN", 1)[-1].split("\n## ", 1)[0]
    dec, chore = [], []
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        c = [x.strip() for x in line.strip("|").split("|")]
        # `^\d` not .isdigit() — mirror of prome_gate.py's 8/16 lettered-ID
        # fix (32b-class rows failed .isdigit() and vanished from the brief
        # while the gate counted them: split-brain, RAV catch 8/16). The
        # MISFILED exclusion mirrors the gate's too — a closed-in-place row
        # (terminal marker LEADING the Item cell, anchored after
        # strikethrough/bold strip, never substring) must not render as an
        # open ask. Regexes duplicated deliberately (the gate is a blocking
        # boot surface; no import coupling) — queue_parser_selftest.py is
        # what keeps the two parsers agreeing.
        if len(c) < 6 or not re.match(r"\d", c[0]):
            continue
        item_lead = re.sub(r"^(?:~~[^~]+~~\s*)+", "", c[1])
        item_lead = re.sub(r"^[\*\s]+", "", item_lead)
        if re.match(r"✅|DONE\b|RESOLVED\b|TERMINAL\b|DECLINED\b", item_lead):
            continue
        raw = c[3]
        d = re.search(r"\d{4}-\d{2}-\d{2}", raw)
        kind = re.sub(r"\*\*|`", "", c[2]).strip().upper()
        row = {
            "n": c[0], "item": ell(re.sub(r"\*\*|`", "", c[1]), 70), "kind": kind,
            "due": d.group(0) if d else None,
            "due_txt": ell(re.sub(r"\*\*", "", raw), 26),
            # Blocked keys on the DOCUMENTED marker at the START of the Notes cell.
            # WILL_QUEUE's Rules block: blocked rows carry "⛔ waits: <who>" at the
            # start of Notes. 8/22: bare "⛔" (the caveat glyph) had demoted row 73
            # (RULE, due 2026-08-28) to "in flight". 9/10 (WQ-221): a whole-line
            # "⛔ wait" search matched ITEM prose ("a ⛔ waits row whose …") and
            # filed a rulable row under "waiting on others" with no tap controls.
            "blocked": bool(re.match(r"^[\*\s]*⛔\s*waits?\b", c[6] if len(c) > 6 else "")),
            "rec": ell(re.sub(r"\*\*|`", "", c[5]), 70),
        }
        (dec if kind in DECISION_TYPES else chore).append(row)
    if not dec and not chore:
        fail("what you do", "PROME/WILL_QUEUE.md", "OPEN table parsed to zero rows")
    for lst in (dec, chore):
        lst.sort(key=lambda x: (x["blocked"], x["due"] or "9999"))
    return dec, chore


def parse_money():
    """FORGE/STATUS.md header — account total + cash %, WITH the export vintage."""
    p = ROOT / "FORGE/STATUS.md"
    try:
        head = p.read_text(encoding="utf-8").split("\n## ", 1)[0]
    except Exception as e:
        return fail("the book", "FORGE/STATUS.md", f"unreadable: {e}")
    total = re.search(r"account total:\*\*\s*\$([\d,]+\.\d\d)", head)
    cash = re.search(r"money market\):\*\*\s*\$([\d,]+\.\d\d)\s*\(([\d.]+)%\)", head)
    vint = re.search(r"\*\*Updated:\*\*\s*(\d{4}-\d{2}-\d{2})", head)
    marks = re.search(r"marks = (?:Fri )?(\d{4}-\d{2}-\d{2})", head)
    if not (total and cash and vint):
        return fail("the book", "FORGE/STATUS.md",
                    "header shape changed — account total / cash / Updated not found")
    return {"total": total.group(1), "cash_pct": cash.group(2),
            "vintage": vint.group(1), "marks": marks.group(1) if marks else vint.group(1),
            "age": (dt.date.today() - dt.date.fromisoformat(vint.group(1))).days}


def parse_gates():
    """GATES.tsv — {gate_id: leading state token}. Drives both the blocker alert
    and the change feed (a gate flipping state IS the news)."""
    p = ROOT / "PROME/GATES.tsv"
    try:
        with open(p, encoding="utf-8") as f:
            rows = [r for r in csv.reader(f, delimiter="\t")
                    if r and not r[0].startswith("#") and r[0] != "gate_id"]
    except Exception as e:
        return fail("gates", "PROME/GATES.tsv", f"parse error: {e}") or {}
    return {r[0]: r[5].split(" ")[0].split("(")[0].strip()
            for r in rows if len(r) > 5}


def parse_channels():
    """dashboard_state.json — v2 no longer RENDERS these (4-of-7 read 'crit', so
    the row stopped discriminating), but a channel CHANGING state is still news,
    so it stays wired into the change feed only."""
    p = ROOT / "PROME/tools/dashboard_state.json"
    try:
        return (json.loads(p.read_text()).get("channels") or {})
    except Exception as e:
        return fail("pressure (feed only)", "PROME/tools/dashboard_state.json",
                    f"unreadable: {e}") or {}


# ------------------------------------------------------------- the change feed

def snapshot_now(gates, channels, money, dec, chore, dates):
    return {
        "gates": gates,
        "channels": channels,
        "money": {"total": money["total"], "cash": money["cash_pct"],
                  "vintage": money["vintage"]} if money else {},
        "queue": {r["n"]: r["item"] for r in (dec + chore)},
        "docket": {d["date"]: d["title"] for d in dates},
    }


# Within one build every change shares a timestamp, so "newest first" alone leaves
# ordering to insertion accident — the first cut buried a gate firing under a new
# docket row. Rank decides ties: a gate moving outranks a date being registered.
KIND_RANK = {"gate": 0, "book": 1, "pressure": 2, "queue": 3, "clock": 4}


def diff_snapshots(old, new):
    """Human sentences, not field diffs. Each line must read as news."""
    ch = []
    og, ng = old.get("gates", {}), new.get("gates", {})
    for g, st in ng.items():
        prev = og.get(g)
        if prev is None:
            ch.append(("gate", f"New gate registered: {g} ({st.lower()})."))
        elif prev != st:
            ch.append(("gate", f"{g} moved {prev.lower()} → {st.lower()}."))
    for g in og:
        if g not in ng:
            ch.append(("gate", f"{g} left the ledger."))

    oc, nc = old.get("channels", {}), new.get("channels", {})
    word = {"crit": "critical", "elev": "elevated", "watch": "watching", "none": "quiet"}
    for k, v in nc.items():
        if k in oc and oc[k] != v:
            ch.append(("pressure",
                       f"{k} went {word.get(oc[k], oc[k])} → {word.get(v, v)}."))

    om, nm = old.get("money", {}), new.get("money", {})
    if om and nm and om.get("vintage") != nm.get("vintage"):
        ch.append(("book", f"Fresh broker export ({nm['vintage']}): "
                           f"${nm['total']}, {nm['cash']}% cash."))

    oq, nq = old.get("queue", {}), new.get("queue", {})
    for n, item in nq.items():
        if n not in oq:
            ch.append(("queue", f"Added to your list: {item}"))
    for n, item in oq.items():
        if n not in nq:
            ch.append(("queue", f"Off your list: {item}"))

    od, nd = old.get("docket", {}), new.get("docket", {})
    for d, t in nd.items():
        if d not in od:
            ch.append(("clock", f"New date {d}: {t}"))
    return ch


def update_changes(new_snap, write=True):
    """Append genuinely-new diffs, return the recent feed. First build records a
    baseline and says so rather than inventing history."""
    try:
        old = json.loads(SNAP.read_text()) if SNAP.exists() else None
    except Exception:
        old = None
    now = dt.datetime.now()
    fresh = diff_snapshots(old, new_snap) if old is not None else []
    try:
        existing = [json.loads(l) for l in CHANGES.read_text().splitlines() if l.strip()] \
            if CHANGES.exists() else []
    except Exception as e:
        return fail("what changed", str(CHANGES), f"log unreadable: {e}") or ([], old is None)
    seen = {(e.get("kind"), e.get("text")) for e in existing[-60:]}
    added = [{"ts": now.isoformat(timespec="minutes"), "kind": k, "text": t}
             for k, t in fresh if (k, t) not in seen]
    if write:
        SNAP.parent.mkdir(parents=True, exist_ok=True)
        if added:
            with open(CHANGES, "a", encoding="utf-8") as f:
                for e in added:
                    f.write(json.dumps(e) + "\n")
        SNAP.write_text(json.dumps(new_snap, indent=1, sort_keys=True))
        _persist_state(len(added))
    recent = (existing + added)[-7:]
    recent.sort(key=lambda e: (e.get("ts", ""), -KIND_RANK.get(e.get("kind"), 9)),
                reverse=True)
    return recent, old is None


# ------------------------------------------------------------------ rendering

def md_inline(s):
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
    lines, i = s.splitlines(), 0
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
  --accent:#A62D72; --accent-soft:#F3DFEA;
  --water:#2F5D72;
  --good:#2E6B45; --warn:#9A6612; --crit:#A4342A;
  --warn-bg:#F4E8D4; --crit-bg:#F5E0DC;
  --serif:Georgia,'Iowan Old Style','Palatino Linotype',Palatino,serif;
  --sans:system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;
  --mono:ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace;
}
@media (prefers-color-scheme:dark){
  :root{
    --ground:#0D1418; --panel:#141D22; --line:#26333A; --line-soft:#1C272D;
    --text:#E4E7E5; --text-dim:#9BA6A4; --text-faint:#6F7B79;
    --accent:#E86BA8; --accent-soft:#33202B;
    --water:#6FA3BC;
    --good:#63C185; --warn:#DCA84A; --crit:#EC7166;
    --warn-bg:#2C2313; --crit-bg:#2E1917;
  }
}
:root[data-theme="dark"]{
  --ground:#0D1418; --panel:#141D22; --line:#26333A; --line-soft:#1C272D;
  --text:#E4E7E5; --text-dim:#9BA6A4; --text-faint:#6F7B79;
  --accent:#E86BA8; --accent-soft:#33202B;
  --water:#6FA3BC;
  --good:#63C185; --warn:#DCA84A; --crit:#EC7166;
  --warn-bg:#2C2313; --crit-bg:#2E1917;
}
:root[data-theme="light"]{
  --ground:#EDEBE4; --panel:#F6F4EF; --line:#D3CEC1; --line-soft:#E2DDD1;
  --text:#1B211F; --text-dim:#5C6360; --text-faint:#878D88;
  --accent:#A62D72; --accent-soft:#F3DFEA;
  --water:#2F5D72;
  --good:#2E6B45; --warn:#9A6612; --crit:#A4342A;
  --warn-bg:#F4E8D4; --crit-bg:#F5E0DC;
}
body{margin:0;background:var(--ground);color:var(--text);font-family:var(--sans);
  font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
.wrap{max-width:46rem;margin:0 auto;padding:2.5rem 1.25rem 5rem;
  display:flex;flex-direction:column;gap:2.4rem}
code{font-family:var(--mono);font-size:.9em;background:var(--line-soft);
  padding:.1em .35em;border-radius:3px}

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

section{display:flex;flex-direction:column;gap:.85rem}
h2{font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;margin:0;
  color:var(--text-faint);font-weight:700;display:flex;align-items:center;gap:.6rem}
h2::after{content:"";flex:1;height:1px;background:var(--line)}
.prose{font-family:var(--serif);font-size:1.03rem;line-height:1.68}
.prose p{margin:0 0 .9rem}
.prose p:last-child{margin-bottom:0}
.prose ul{margin:0;padding-left:1.1rem;display:flex;flex-direction:column;gap:.5rem}
.pull{font-family:var(--serif);font-size:1.12rem;line-height:1.5;margin:0;
  padding:.9rem 0 .9rem 1.1rem;border-left:3px solid var(--accent)}

/* what changed --------------------------------------------------------- */
.feed{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}
.ev{display:grid;grid-template-columns:5.2rem 1fr;gap:.85rem;align-items:baseline;
  padding:.5rem 0;border-bottom:1px solid var(--line-soft);font-size:.9rem}
.ev:last-child{border-bottom:none}
.ev .ago{font-family:var(--mono);font-size:.7rem;color:var(--text-faint);
  font-variant-numeric:tabular-nums;white-space:nowrap;text-transform:uppercase;
  letter-spacing:.05em}
.ev.new .ago{color:var(--accent);font-weight:700}
.empty{font-size:.88rem;color:var(--text-dim);font-style:italic}

/* falsifier — the one block that must not look like the others ---------- */
.falsify{background:var(--accent-soft);border-radius:5px;padding:1rem 1.15rem;
  display:flex;flex-direction:column;gap:.5rem}
.falsify .lead{font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--accent);font-weight:700}
.falsify .prose{font-size:.97rem}

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
.sub{font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;
  color:var(--text-dim);font-weight:700;margin:.2rem 0 -.2rem}
.acts{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:.55rem}
.act{display:flex;flex-direction:column;gap:.2rem;padding:.7rem .85rem;
  background:var(--panel);border:1px solid var(--line);border-radius:5px;
  border-left:3px solid var(--line)}
.act.due{border-left-color:var(--crit)}
.act.soon{border-left-color:var(--warn)}
.act.call{border-left-color:var(--accent)}
.act .top{display:flex;flex-wrap:wrap;gap:.5rem;align-items:baseline;
  justify-content:space-between}
.act .name{font-size:.92rem;font-weight:600}
.act .when{font-family:var(--mono);font-size:.7rem;color:var(--text-dim);white-space:nowrap}
.act .rec{font-size:.8rem;color:var(--text-dim)}
.chores{display:flex;flex-direction:column;gap:.3rem;font-size:.86rem;color:var(--text-dim)}
.chore{display:flex;gap:.6rem;align-items:baseline}
.chore .nm{color:var(--text)}
.chore .w{font-family:var(--mono);font-size:.68rem;color:var(--text-faint);white-space:nowrap}

/* money ---------------------------------------------------------------- */
.book{display:flex;flex-wrap:wrap;gap:1.6rem;align-items:flex-end;
  padding:.9rem 1rem;background:var(--panel);border:1px solid var(--line);border-radius:5px}
.stat{display:flex;flex-direction:column;gap:.1rem}
.stat .v{font-family:var(--mono);font-size:1.28rem;font-variant-numeric:tabular-nums;
  font-weight:600;line-height:1.1}
.stat .k{font-size:.66rem;letter-spacing:.12em;text-transform:uppercase;color:var(--text-faint)}
.vint{font-size:.7rem;color:var(--text-faint);font-family:var(--mono);flex-basis:100%}
.vint.stale{color:var(--warn)}

.alert{padding:.8rem 1rem;border-radius:5px;font-size:.88rem;
  background:var(--crit-bg);color:var(--crit);font-weight:600}
.pf{padding:.8rem 1rem;border-radius:5px;background:var(--crit-bg);color:var(--crit);
  font-size:.84rem;font-family:var(--mono)}
footer{font-size:.72rem;color:var(--text-faint);line-height:1.7;
  border-top:1px solid var(--line);padding-top:1.1rem}
footer code{background:none;padding:0;color:var(--text-dim)}
a{color:var(--accent)}
@media (max-width:34rem){
  .day{grid-template-columns:4.2rem 1fr;gap:.6rem}
  .day .in{display:none}
  .ev{grid-template-columns:4.4rem 1fr;gap:.6rem}
  .book{gap:1.1rem}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""


def ago(iso, now):
    try:
        t = dt.datetime.fromisoformat(iso)
    except ValueError:
        return "—"
    mins = (now - t).total_seconds() / 60
    if mins < 90:
        return "just now" if mins < 12 else f"{int(mins)}m ago"
    if mins < 60 * 20:
        return f"{int(mins // 60)}h ago"
    d = (now.date() - t.date()).days
    return "yesterday" if d == 1 else f"{d}d ago"


def render(brief_written, brief, feed, first_build, dates, dec, chore, money, fired):
    now = dt.datetime.now()
    P, A = [], None
    A = P.append

    A(f"<style>{CSS}</style>")
    A('<div class="wrap">')

    head = brief.get("HEADLINE", "")
    A('<header class="mast"><div class="eyebrow">Desk brief</div>')
    A(f"<h1>{md_inline(head) if head else 'No headline written — see PROME/BRIEF.md'}</h1>")
    stale = ""
    if brief_written:
        try:
            wd = dt.datetime.strptime(brief_written.split(" ET")[0].strip(), "%Y-%m-%d %H:%M")
            stale = ' class="stale"' if (now - wd).total_seconds() / 3600 > 20 else ""
        except ValueError:
            pass
    A('<div class="clocks">')
    A(f'<span>Facts rebuilt {now:%b %-d, %-I:%M %p} {ET}</span>')
    A(f'<span{stale}>Story written {html.escape(brief_written or "— NOT STAMPED")}</span>')
    A("</div></header>")

    if fired:
        A(f'<div class="alert">Gate fired and not acted on: {", ".join(html.escape(f) for f in fired)}'
          " — this blocks new work until it is cleared.</div>")

    # ---- 1. decisions waiting on you — FIRST (re-spec Will-ruled 8/16 S4,
    # "Rewire with the re-spec"; DAEDALUS design input 8f0ba7711). One page,
    # one job: if this section says nothing needs you, you're done — everything
    # below is context. Count excludes ⛔-blocked rows (waiting on something
    # else, not on Will).
    n_open = sum(1 for a in dec if not a["blocked"])
    A(f'<section><h2>Decisions waiting on you — {n_open}</h2>')
    if dec:
        A('<ul class="acts">')
        for a in dec:
            cls = " call"
            if a["due"]:
                dd = (dt.date.fromisoformat(a["due"]) - dt.date.today()).days
                cls = " due" if dd <= 0 else (" soon" if dd <= 2 else " call")
            nm = ("⛔ " if a["blocked"] else "") + a["item"]
            A(f'<li class="act{cls}"><div class="top"><span class="name">{html.escape(nm)}</span>'
              f'<span class="when">{html.escape(a["due_txt"]) or "no date"}</span></div>')
            if a["rec"]:
                A(f'<div class="rec">{html.escape(a["rec"])}</div>')
            A("</li>")
        A("</ul>")
    else:
        A('<p class="empty">Nothing needs a decision from you. You are done here — '
          "everything below is context.</p>")
    if chore:
        A('<div class="sub">Errands (no judgment needed)</div><div class="chores">')
        for a in chore:
            A(f'<div class="chore"><span class="nm">{html.escape(a["item"])}</span>'
              f'<span class="w">{html.escape(a["due_txt"]) or "no date"}</span></div>')
        A("</div>")
    A("</section>")

    # ---- 2. what changed (the feed)
    A("<section><h2>What changed</h2>")
    if first_build:
        A('<p class="empty">Baseline recorded. Changes will appear here from the next '
          "rebuild onward — nothing is invented for a first build.</p>")
    elif feed:
        A('<ul class="feed">')
        for e in feed:
            fresh = " new" if ago(e.get("ts", ""), now) in ("just now",) else ""
            A(f'<li class="ev{fresh}"><span class="ago">{html.escape(ago(e.get("ts",""), now))}</span>'
              f'<span>{md_inline(e.get("text",""))}</span></li>')
        A("</ul>")
    else:
        A('<p class="empty">Nothing has moved since the last rebuild.</p>')
    A("</section>")

    # ---- 3. the story + the question + the falsifier
    A("<section><h2>What is going on</h2>")
    A(f'<div class="prose">{md_block(brief.get("STORY",""))}</div>')
    if brief.get("QUESTION"):
        A(f'<p class="pull">{md_inline(" ".join(brief["QUESTION"].split()))}</p>')
    if brief.get("FALSIFIER"):
        A('<div class="falsify"><div class="lead">This is wrong if</div>'
          f'<div class="prose">{md_block(brief["FALSIFIER"])}</div></div>')
    A("</section>")

    # ---- 4. where the desk disagrees — the thing only this system can show
    if brief.get("DISAGREEMENT"):
        A("<section><h2>Where the desk disagrees</h2>")
        A(f'<div class="prose">{md_block(brief["DISAGREEMENT"])}</div></section>')

    # ---- 5. the book
    A("<section><h2>Where you stand</h2>")
    if money:
        vs = " stale" if money["age"] > 4 else ""
        A('<div class="book">')
        A(f'<div class="stat"><span class="v">${money["total"]}</span><span class="k">Account</span></div>')
        A(f'<div class="stat"><span class="v">{money["cash_pct"]}%</span><span class="k">Cash</span></div>')
        A(f'<div class="vint{vs}">Broker export {money["vintage"]} · marks {money["marks"]}'
          f' · {money["age"]}d old — not live, re-check before any fill</div></div>')
    if brief.get("POSITION"):
        A(f'<div class="prose">{md_block(brief["POSITION"])}</div>')
    A("</section>")

    # ---- 6. the clock (+ the hand-written WATCH tail)
    A("<section><h2>What is coming</h2>")
    if dates:
        A('<ol class="days">')
        for d in dates:
            k = " key" if d["star"] or d["days"] <= 1 else ""
            when = dt.date.fromisoformat(d["date"]).strftime("%a %-m/%-d")
            inn = "today" if d["days"] == 0 else ("tomorrow" if d["days"] == 1 else f'{d["days"]}d')
            also = f' <span class="also">+{d["also"]} more</span>' if d["also"] else ""
            A(f'<li class="day{k}"><span class="when">{when}</span>'
              f'<span class="what">{html.escape(d["title"])}{also}</span>'
              f'<span class="in">{inn}</span></li>')
        A("</ol>")
    if brief.get("WATCH"):
        A(f'<div class="prose">{md_block(brief["WATCH"])}</div>')
    A("</section>")

    # (decisions/chores moved to section 1 — the 8/16 re-spec; WATCH rides the
    # clock section above as the hand-written tail of "what is coming")

    if failures:
        A("<section><h2>Broken on this page</h2>")
        for sec, owner, why in failures:
            A(f'<div class="pf">PARSE-FAILED · {html.escape(sec)} — {html.escape(owner)}: {html.escape(why)}</div>')
        A("</section>")

    A('<footer>The story, the falsifier and the disagreements are PROME\'s judgment and carry '
      "their own date. Everything else is generated from canon and owns nothing — if this page "
      "and canon disagree, canon is right and a parser is broken. Money is a broker mirror; "
      "never fill against it.</footer></div>")
    return "\n".join(P)


def main():
    ap = argparse.ArgumentParser(description="Generate Will's briefing page.")
    ap.add_argument("-o", "--out", default="/tmp/will_brief.html")
    ap.add_argument("--no-snapshot", action="store_true",
                    help="dry run: render without burning the change-feed baseline")
    args = ap.parse_args()

    written, brief = parse_brief()
    gates, channels = parse_gates(), parse_channels()
    money, dates = parse_money(), parse_dates()
    dec, chore = parse_actions()
    fired = [g for g, s in gates.items() if s == "FIRED-UNEXECUTED"]

    feed, first = update_changes(snapshot_now(gates, channels, money, dec, chore, dates),
                                 write=not args.no_snapshot)
    page = render(written, brief, feed, first, dates, dec, chore, money, fired)
    Path(args.out).write_text(f"<title>Desk brief</title>\n{page}\n", encoding="utf-8")
    print(f"wrote {args.out} ({len(page)} bytes) · {len(feed)} feed item(s)"
          + (f" · {len(failures)} PARSE-FAILED" if failures else " · clean")
          + (" · DRY RUN (baseline untouched)" if args.no_snapshot else ""))


if __name__ == "__main__":
    main()
