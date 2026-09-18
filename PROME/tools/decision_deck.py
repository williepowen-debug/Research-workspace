#!/usr/bin/env python3
"""decision_deck.py — Will's Decision Deck (WQ-202, Will-ruled 2026-09-10 11:01 ET).

A PROJECTION of PROME's decision rails into a linked pair (L393, Will-approved 2026-09-15):
  decision_deck.html — Owed + Key; retains the existing private ruling store.
  decision_reference.html — Decided / In-flight / Docket; read-only, no store client.
  Owed      — every OPEN row of PROME/WILL_QUEUE.md in three groups: needs your ruling (soonest first) ·
              answered but your hands/a dated action still owed (a DONE tap closes it) · waiting on others (last)
  Decided   — every DONE row: WILL_QUEUE RECENTLY DONE + PROME/archive/WILL_QUEUE_ROWS_*.md
  In-flight — PROME/ACTIVE_DECISIONS.md live index
  Docket    — PROME/DOCKET.tsv rows whose owner cell names Will (non-terminal)
  Key       — what the ID families are; how tap-to-rule works; the privacy rule
Plain-English blocks come ONLY from PROME/registry/WQ_EXPLAINERS.tsv (sidecar keyed by
row number); a row without one renders "explainer owed" — the page never invents.

Never a second truth: regenerate from the source files (every PROME closeout) and
republish. Tap-to-rule writes to the artifact's `db` store (collection `rulings`), ONE DOCUMENT PER TAP
(L336 B3): the id carries the full millisecond timestamp plus a random suffix, so a change of mind is a
SECOND document, never an overwrite. At pickup the LATEST `ts` for a WQ is the ruling and earlier taps are
history — PROME states which document it consumed;
PROME reads it at boot (Artifact tool read_db) and writes the ruling into the queue.

Usage:  python3 PROME/tools/decision_deck.py [-o PROME/artifacts/decision_deck.html]
        --reference-out PATH  optional reference output (default: sibling decision_reference.html)
        --owed-url URL --reference-url URL  paired native artifact URLs for hosted navigation
        Without hosted URLs the pair uses local relative links; never publish those as hosted links.
        --selftest   parse-shape drills on the live sources (counts + required fields)
"""
from __future__ import annotations
import argparse, datetime as dt, glob, html, json, os, re, subprocess, sys
from pathlib import Path
from urllib.parse import quote

def _root() -> Path:
    """Repo root: git from THIS file's directory (not the caller's cwd), else the file's known depth
    (PROME/tools/decision_deck.py → parents[2]) — importable from any cwd and from a scratch copy."""
    for cwd in (Path(__file__).resolve().parent, Path.cwd()):
        try:
            out = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                                 check=True, cwd=cwd).stdout.strip()
            if out and (Path(out) / "PROME/WILL_QUEUE.md").exists():
                return Path(out)
        except Exception:
            continue
    return Path(__file__).resolve().parents[2]

ROOT = _root()
Q = ROOT / "PROME/WILL_QUEUE.md"
AD = ROOT / "PROME/ACTIVE_DECISIONS.md"
DOCKET = ROOT / "PROME/DOCKET.tsv"
EXPL = ROOT / "PROME/registry/WQ_EXPLAINERS.tsv"
ARCH = sorted(glob.glob(str(ROOT / "PROME/archive/WILL_QUEUE_ROWS_*.md")), reverse=True)
LEDGER = ROOT / "PROME/registry/WQ_LEDGER.tsv"  # WQ-203: the append-only event ledger; Decided reads it FIRST
TERMINAL = re.compile(r"✅|DONE\b|RESOLVED\b|TERMINAL\b|DECLINED\b|RULED\b|EXECUTED\b")

# ---------------------------------------------------------------- helpers

def cells(line: str) -> list[str]:
    return split_cells(line)                             # B1 (9/18): the one split

# ---- ONE split + ONE date classifier for the WILL_QUEUE table (2026-09-18, ACCEPTANCE_queue_parsers B1/B3/B4) ----
# Copied verbatim into willq_view.py · prome_gate.py · will_brief.py · decision_deck.py (the gate is a blocking boot
# surface: no import coupling by design); queue_parser_selftest.py asserts the four copies and table_check agree.
_ESCAPED_PIPE = "\x00"


def split_cells(line: str) -> list[str]:
    """table_check.split_cells semantics: `\\|` is a literal pipe, every other pipe separates (code spans included),
    one leading and one trailing pipe are structural. Cells come back stripped."""
    s = line.strip().replace("\\|", _ESCAPED_PIPE)
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.replace(_ESCAPED_PIPE, "\\|").strip() for c in s.split("|")]


_ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
_DATELIKE = re.compile(r"(?<![\w/])\d{1,2}/\d{1,2}(?:/\d{2,4})?(?![\w/])(?!\s+of\b)"      # 9/19 · 9/19/26 — not "2/3 of"
                       r"|\b\d{4}-\d{1,2}-\d{1,2}\b"                                        # 2026-9-19 (unpadded)
                       r"|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2}\b"   # Sept 19
                       r"|\b\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\b"      # 19 Sep
                       r"|\b\d{4}/\d{1,2}/\d{1,2}\b"                                           # 2026/09/19
                       r"|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?\s+\d{4}\b", re.I)  # May 2026


def datelike_not_iso(raw):
    """B3: a needed-by with NO ISO date but a date-LIKE token. B4 (textual / empty) is its complement."""
    t = re.sub(r"\*\*|`", "", raw or "")
    return not _ISO_DATE.search(t) and bool(_DATELIKE.search(t))


def is_separator(cells):
    return bool(cells) and all(re.fullmatch(r":?-+:?", c) for c in cells)

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

def verbatim_of(cell: str) -> str:
    """Will's quoted word from a row cell: the FIRST quote that follows the word 'verbatim' (the fleet's
    recording form *"…"* / "…"); EMPTY when the cell carries none — never a paraphrase (WQ-203 rule 4).
    A desk's quoted words never follow 'verbatim' in a queue row, so the anchor word is the discriminator."""
    m = re.search(r"verbatim[^\"“]{0,40}[\"“]([^\"”]{1,400})[\"”]", cell or "")
    return m.group(1).strip() if m else ""

LEAD_TOKENS = ("DECLINED", "RULED", "CLOSED", "RESOLVED", "EXECUTED", "SUPERSEDED", "WITHDRAWN", "TERMINAL",
               "OVERTAKEN", "RATIFIED", "APPROVED", "DONE")

def verdict_of(record: str, window: int = 140) -> tuple[str, bool]:
    """(lead token, approve-flag) read from the LEAD of a done/record cell — the fleet writes the verdict
    first ("RULED 2026-… — Will APPROVE …", "DECLINED …", "CLOSED … — OVERTAKEN …", "DONE 8/6 …").
    Only the first `window` chars after the struck name count: a token 900 chars in ("doorbells PROME
    declined", "KB-… SUPERSEDED") is narrative, not the verdict (WQ-203 result read ❌10–13).
    Returns ("", False) when the lead carries no token."""
    s = re.sub(r"^\s*(?:~~[^~]+~~\s*)+", "", record or "")
    lead = strip_md(s)[:window].upper()
    m = re.search(r"\b(" + "|".join(LEAD_TOKENS) + r")\b", lead)
    tok = m.group(1) if m else ""
    if not tok and re.search(r"\bWILL APPROVE[DS]?\b|\bAPPROVE[DS]?\b", lead):
        tok = "APPROVED"  # a tap record: "Deck tap … Will APPROVE = …" carries no RULED word, only the verdict
    approve = bool(re.search(r"\bAPPROVE[DS]?\b", lead)) and tok in ("RULED", "APPROVED", "RATIFIED", "DONE")
    if tok == "CLOSED" and "OVERTAKEN" in lead:
        tok = "OVERTAKEN"
    return tok, approve

def item_name(item: str, n: int = 120) -> str:
    """The item's NAME for a ledger: the first bold span that is not a ruling stamp ("Will APPROVED …",
    "RULED …", "DECLINED …", "CLOSED …"); falls back to title_of."""
    for m in re.finditer(r"\*\*(.+?)\*\*", item or ""):
        t = strip_md(m.group(1)).strip()
        if not re.match(r"(?:Will\s+)?(?:APPROVED|RULED|DECLINED|CLOSED|RATIFIED|SCHEDULE RATIFIED|DONE)\b", t):
            t = re.split(r"(?<=[.?!])\s|\s—\s", t, 1)[0]
            return (t[: n - 1] + "…") if len(t) > n else t
    return title_of(item, n)

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

# Blocked keys on the DOCUMENTED declaration in the NOTES cell only — WILL_QUEUE Rules block: blocked rows carry
# "⛔ waits: <who>" at the START of Notes. 2026-09-10 (WQ-221): a whole-LINE search for "⛔ wait" matched the
# ITEM prose of the row proposing the aged-waits rule ("a ⛔ waits row whose …") and filed it under "waiting on
# others" with no tap controls — Will could not rule it. Prose mentioning a marker is not the marker.
BLOCKED_RE = re.compile(r"^[\*\s]*⛔\s*waits?\b")
BLOCKER_RE = re.compile(r"⛔\s*waits?:\s*(?:the\s+)?([A-Z][A-Z0-9_-]{2,})")

def is_blocked(notes: str) -> bool:
    return bool(BLOCKED_RE.match(notes or ""))

def blocker_of(notes: str) -> str | None:
    """The desk named in the wait declaration (first ALL-CAPS token after "⛔ waits:"), else None."""
    m = BLOCKER_RE.match((notes or "").lstrip("* "))
    return m.group(1) if m else None

def parse_open(text: str) -> list[dict]:
    sec = text.split("## OPEN", 1)[-1].split("\n## ", 1)[0]
    rows, hdr = [], None
    for line in sec.splitlines():
        if not line.startswith("|"):
            continue
        c = cells(line)
        if is_separator(c):
            continue
        if hdr is None:                                  # B2: the FIRST table row is the header
            hdr = len(c)
            if hdr != 7:                                 # B8: width is a contract — one warning, the table skipped, never indexed
                print(f"⚠️ decision_deck: § OPEN header has {hdr} columns (the table is 7) — table skipped", file=sys.stderr)
            continue
        if hdr != 7:
            continue
        if len(c) != hdr:                                # B2: skipped BY NAME on stderr — the Deck never renders a shifted row
            print(f"⚠️ decision_deck: SHIFTED row WQ-{c[0][:8]} ({len(c)} cells vs header {hdr}) skipped — an unescaped | inside a cell; write it \\|", file=sys.stderr)
            continue
        if not re.match(r"\d", c[0]):
            continue
        lead = re.sub(r"^(?:~~[^~]+~~\s*)+", "", c[1])
        lead = re.sub(r"^[\*\s]+", "", lead)
        if re.match(r"✅|DONE\b|RESOLVED\b|TERMINAL\b|DECLINED\b", lead):
            continue  # closed-in-place (mirrors will_brief/prome_gate)
        if datelike_not_iso(c[3]):                       # B3: rendered undated WITH a named warning; AFTER the closed-in-place skip (parity)
            print(f"⚠️ decision_deck: NOT-ISO needed-by on WQ-{c[0]}: '{c[3][:24]}' — renders undated; write YYYY-MM-DD", file=sys.stderr)
        rows.append({
            "n": c[0], "item": c[1], "kind": strip_md(c[2]), "by_raw": c[3],
            "by": first_date(c[3]), "since": strip_md(c[4]), "rec": c[5],
            "notes": c[6] if len(c) > 6 else "",
            "blocked": is_blocked(c[6] if len(c) > 6 else ""),
            "blocker": blocker_of(c[6] if len(c) > 6 else ""),
            # ANSWERED (Will 2026-09-10 12:42 "these WQ that I have answered already should be moved out of OWED"):
            # the row already carries Will's word and stays OPEN only for his HANDS or a dated action —
            # lead reads APPROVED/RULED/RATIFIED, or the Type cell says RULED/APPROVED. Never a ruling ask.
            "answered": bool(re.match(r"(?:Will\s+)?(?:APPROVED|RULED|SCHEDULE\s+RATIFIED|RATIFIED)\b", lead)
                             or re.search(r"\b(?:RULED|APPROVED)\b", strip_md(c[2]))),
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
        struck = re.match(r"\s*~~([^~]+)~~", c[1])  # an archived open-style row keeps its NAME struck through
        rows.append({"n": c[0], "name": strip_md(struck.group(1)).strip() if struck else title_of(c[1]), "done": dm.group(1) if dm else "—",
                     "record": c[1], "source": source})
    return rows

def parse_ledger_decided(ledger: Path) -> list[dict]:
    """WQ-203: terminal-state rows from the event ledger (last event per WQ wins). Empty list if absent."""
    if not ledger.exists():
        return []
    last: dict[str, dict] = {}
    with ledger.open(encoding="utf-8") as f:
        hdr = f.readline().rstrip("\n").split("\t")
        for line in f:
            c = line.rstrip("\n").split("\t")
            if len(c) != len(hdr):
                continue
            r = dict(zip(hdr, c)); last[r["wq"]] = r
    out = []
    for n, r in last.items():
        if r.get("status_after") not in ("RULED", "DECLINED", "CLOSED"):
            continue
        out.append({"n": n, "name": r.get("title") or f"WQ-{n}", "done": r.get("at", "")[:10] or "—",
                    "record": r.get("record") or r.get("will_verbatim") or "",
                    "source": "ledger ← " + (r.get("source") or "?")})
    return out

def parse_archive(text: str, source: str) -> list[dict]:
    """An archive can carry BOTH shapes in one file (the 8/16 rotation does): dispatch PER LINE —
    a bare-number first cell with ≥6 cells is an open-style row; a '**NNN Title**' first cell with 3 cells
    is a done-table row. (Before 2026-09-11 the file-level `if not got:` fallback let 29 open-style rows
    through parse_done_table as garbage — WQ-203 plan read ❌3.)"""
    done_lines, open_lines = [], []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        c = cells(line)
        if len(c) >= 6 and re.match(r"^\d+[a-z]?$", c[0]):
            open_lines.append(line)
        elif len(c) >= 3:
            done_lines.append(line)
    return parse_done_table("\n".join(done_lines), source) + parse_done_open_style("\n".join(open_lines), source)

def parse_decided(q_path: Path | None = None, arch: list[str] | None = None, ledger: Path | None = None) -> list[dict]:
    """Decided rows: the WQ-203 ledger FIRST (terminal states), then the live RECENTLY DONE table, then the
    archives — archives are history and cover only a WQ number the ledger lacks (transition safety)."""
    q_path = q_path or Q; arch = ARCH if arch is None else arch; ledger = LEDGER if ledger is None else ledger
    text = q_path.read_text(encoding="utf-8")
    done_sec = text.split("## RECENTLY DONE", 1)[-1].split("\n## ", 1)[0] if "## RECENTLY DONE" in text else ""
    out = parse_ledger_decided(ledger)
    out.extend(parse_done_table(done_sec, "WILL_QUEUE.md § RECENTLY DONE"))
    for f in arch:
        out.extend(parse_archive(Path(f).read_text(encoding="utf-8"), "archive/" + Path(f).name))
    seen, uniq = set(), []
    for r in out:  # first seen wins: ledger, then the live table, then newest archive
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

_DARK_CACHE: dict[str, int | None] = {}
def days_dark(desk: str | None) -> int | None:
    """Days since the desk's last self-commit (subject "DESK:" / "DESK ->"); None if no desk or no commit found.
    WQ-221 (Will 2026-09-10): the wait pill names the blocker + days dark, so an aged wait is visible on the deck."""
    if not desk:
        return None
    if desk not in _DARK_CACHE:
        try:
            # SUBJECT only: `git --grep` matches every line of a message, so a PROME body line beginning
            # "BROCK L260 …" read as a BROCK self-commit (0d dark for a desk dark 2d — found 2026-09-11 building
            # the WQ-221 gate check; `finding_path_scoped_git_log_measures_inbound_traffic`: match the SUBJECT).
            log = subprocess.run(["git", "log", "-4000", "--format=%ct\t%s"], cwd=ROOT, capture_output=True,
                                 text=True, timeout=20).stdout
            out = next((ln.split("\t", 1)[0] for ln in log.splitlines()
                        if re.match(rf"{re.escape(desk)}( |:)", ln.split("\t", 1)[1] if "\t" in ln else "")), "")
            _DARK_CACHE[desk] = int((dt.datetime.now(dt.timezone.utc).timestamp() - int(out)) // 86400) if out else None
        except Exception:
            _DARK_CACHE[desk] = None
    return _DARK_CACHE[desk]

def due_pill(by: str | None, days: int | None, blocked: bool, blocker: str | None = None) -> str:
    if blocked:
        if blocker:
            dd = days_dark(blocker)
            tail = f" · dark {dd}d" if dd is not None else ""
            return f'<span class="pill wait">waits on {html.escape(blocker)}{tail}</span>'
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
    seen = set()
    for r in rows:
        grp = "blocked" if r["blocked"] else ("answered" if r.get("answered") else "owed")
        if grp not in seen:
            seen.add(grp)
            label = {"owed": "Needs your ruling", "answered": "Answered — your hands or a dated action still owed",
                     "blocked": "Waiting on others — nothing owed by you"}[grp]
            out.append(f'<p class="grp">{label}</p>')
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
        if r.get("answered") and not r["blocked"]:
            ctl = (
                f'<div class="tap" data-wq="{r["n"]}">'
                '<div class="tapstate" hidden></div>'
                '<div class="tapbtns">'
                f'<button type="button" class="btn approve" data-v="DONE" id="dn-{r["n"]}">Done — hands complete</button>'
                f'<button type="button" class="btn later" data-v="LATER" id="lt-{r["n"]}">Later</button>'
                '</div>'
                f'<input type="text" class="note" id="note-{r["n"]}" placeholder="Note to PROME (optional)" maxlength="400">'
                '</div>'
            )
        else:
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
            f'<div class="rail"><span class="num">WQ-{r["n"]}</span>{due_pill(r["by"], days, r["blocked"], r.get("blocker"))}{TOGGLE}</div>'
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
            f'<div class="rail"><span class="num">WQ-{r["n"]}</span><span class="pill soft" title="{html.escape(r["source"])}">done {html.escape(r["done"])}{" · ledger" if r["source"].startswith("ledger") else ""}</span>{TOGGLE}</div>'
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
--rec:#EAF3F1;--focus:#0E6B68;--tint-ok:#EEF6F0;--tint-ok-line:#B9D9C4;--tint-no:#FAEFED;--tint-no-line:#E4C3BD;--tint-later:#F1F2EC;--tint-later-line:#D3D6C8}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#121918;--surface:#1A2321;--ink:#E6ECE9;--muted:#98A5A0;--line:#2C3835;--chip:#24302D;
--accent:#45B5AF;--accent-ink:#0F1A19;--warn:#E0A44A;--crit:#E07A6A;--ok:#6CC08B;--wait:#A6ABC9;--rec:#1E2D2B;--focus:#45B5AF;--tint-ok:#182521;--tint-ok-line:#2F4C3D;--tint-no:#271C1B;--tint-no-line:#5A3631;--tint-later:#1E2422;--tint-later-line:#3A423F}}
:root[data-theme="dark"]{--bg:#121918;--surface:#1A2321;--ink:#E6ECE9;--muted:#98A5A0;--line:#2C3835;--chip:#24302D;
--accent:#45B5AF;--accent-ink:#0F1A19;--warn:#E0A44A;--crit:#E07A6A;--ok:#6CC08B;--wait:#A6ABC9;--rec:#1E2D2B;--focus:#45B5AF;--tint-ok:#182521;--tint-ok-line:#2F4C3D;--tint-no:#271C1B;--tint-no-line:#5A3631;--tint-later:#1E2422;--tint-later-line:#3A423F}
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
.card.ruled-approve{background:var(--tint-ok);border-color:var(--tint-ok-line)}.card.ruled-decline{background:var(--tint-no);border-color:var(--tint-no-line)}.card.ruled-later{background:var(--tint-later);border-color:var(--tint-later-line)}
.card.ruled-approve .tapstate{color:var(--ok)}.card.ruled-decline .tapstate{color:var(--crit)}
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

UI_JS = r"""
(function(){
  // tabs
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.tab'));
  var panels = Array.prototype.slice.call(document.querySelectorAll('.panel'));
  function show(id){
    tabs.forEach(function(t){ t.setAttribute('aria-selected', t.dataset.for===id ? 'true':'false'); });
    panels.forEach(function(p){ p.hidden = p.id!==id; });
    try{ localStorage.setItem(tabKey, id); }catch(e){}
  }
  tabs.forEach(function(t){ t.addEventListener('click', function(){ show(t.dataset.for); }); });
  var start = panels.length ? panels[0].id : '';
  var tabKey = 'deck.tab.' + document.body.dataset.view;
  try{ var s = localStorage.getItem(tabKey); if (panels.some(function(p){return p.id===s;})) start = s; }catch(e){}
  if (location.hash) { var el = document.getElementById(location.hash.slice(1)); var panel = el && el.closest('.panel'); if (panel) start = panel.id; }
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
})();
"""

RULING_JS = r"""
(function(){
  var BUILD = document.body.dataset.build;
  var toastEl = document.getElementById('toast');
  function toast(m){ toastEl.textContent = m; toastEl.classList.add('on'); clearTimeout(toast.t); toast.t = setTimeout(function(){toastEl.classList.remove('on');}, 2600); }
  // tap-to-rule
  var storeLine = document.getElementById('store');
  var buttons = Array.prototype.slice.call(document.querySelectorAll('.btn'));
  buttons.forEach(function(b){ b.disabled = true; });
  function setState(wq, cls, text, verdict){
    var card = document.getElementById('wq-'+wq); if(!card) return;
    var st = card.querySelector('.tapstate'); if(!st) return;
    st.className = 'tapstate ' + cls; st.textContent = text; st.hidden = false;
    card.classList.remove('ruled-approve','ruled-decline','ruled-later');
    if (cls === 'sent' && verdict) card.classList.add('ruled-' + String(verdict).toLowerCase());
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
        if (x.consumed) setState(wq, 'sent', 'Ruled by tap ' + when + ': ' + x.verdict + (x.note ? ' — ' + x.note : '') + ' · picked up by PROME', x.verdict);
        else setState(wq, 'sent', 'Tapped ' + when + ': ' + x.verdict + (x.note ? ' — ' + x.note : '') + ' · awaiting PROME pickup', x.verdict);
      });
    }, function(e){ storeLine.textContent = 'Ruling store error: ' + (e && e.code ? e.code : 'unknown'); });
    buttons.forEach(function(b){
      b.addEventListener('click', function(){
        var wrap = b.closest('.tap'); var wq = wrap.dataset.wq; var verdict = b.dataset.v;
        var note = (document.getElementById('note-'+wq) || {}).value || '';
        var ts = new Date().toISOString();
        // L336 B3 (external audit F4): the id truncated the timestamp to SECONDS and the write is doc().set(),
        // so two taps on one WQ inside one second targeted the SAME document and the second overwrote the
        // first. Only the clicked button was disabled, leaving the opposite verdict live — so APPROVE then
        // DECLINE 0.8 s apart left one document reading DECLINE, with no trace that APPROVE had happened.
        // Every tap now gets its own document: full millisecond timestamp plus a random suffix. Disabling a
        // control is a UX courtesy and is NEVER the uniqueness guarantee.
        var rand = Math.random().toString(36).slice(2, 8);
        var id = wq + '-' + ts.replace(/[^0-9]/g,'') + '-' + rand;
        // disable BOTH verdicts on this card while a write is in flight — courtesy, not correctness
        var sibs = wrap.querySelectorAll('button[data-v]');
        for (var si = 0; si < sibs.length; si++) { sibs[si].disabled = true; }
        col.doc(id).set({wq: wq, verdict: verdict, note: note.trim(), ts: ts, build: BUILD, consumed: false, source: 'decision-deck'})
          .then(function(){ toast('Recorded: WQ-' + wq + ' ' + verdict); setState(wq, 'sent', 'Tapped ' + fmt(ts) + ': ' + verdict + (note ? ' — ' + note.trim() : '') + ' · awaiting PROME pickup · the LATEST tap rules', verdict); for (var i2 = 0; i2 < sibs.length; i2++) { sibs[i2].disabled = false; } })
          .catch(function(e){ for (var i3 = 0; i3 < sibs.length; i3++) { sibs[i3].disabled = false; } var c = (e && e.code) || 'error'; setState(wq, 'err', 'Not recorded (' + c + '). Rule by message instead.'); toast('Not recorded: ' + c); });
      });
    });
  }).catch(function(){ storeLine.textContent = 'Tap-to-rule unavailable in this view. Reading only.'; });
})();
"""

JS = UI_JS + RULING_JS


OWED_ARTIFACT_URL = "https://claude.ai/code/artifact/16655022-6e00-4cea-9916-7cb0ff304bca"


def _artifact_url(value: str) -> str:
    match = re.fullmatch(r"https://claude\.ai/code/artifact/([0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12})/?", value)
    if not match:
        raise ValueError("Hosted links must be native https://claude.ai/code/artifact/<UUID> URLs")
    return "https://claude.ai/code/artifact/" + match[1].lower()


def _page(title: str, view: str, panels: list[tuple[str, str, int | None, str]],
          nav: str, build_id: str, stamp: str, sha: str) -> str:
    tabs = "".join(f'<button type="button" class="tab" role="tab" data-for="{key}" id="tab-{key}">{label}'
                   + (f'<span class="n">{count}</span>' if count is not None else "") + '</button>'
                   for key, label, count, _ in panels)
    body = "\n".join(f'<section class="panel" id="{key}" role="tabpanel"{" hidden" if i else ""}>{content}</section>'
                       for i, (key, _, _, content) in enumerate(panels))
    script = JS if view == "owed" else UI_JS
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>{CSS}</style></head><body data-view="{view}" data-build="{html.escape(build_id, quote=True)}">
<header class="top"><div class="wrap"><div class="brand"><h1>{title}</h1><span class="build">built {stamp} · {sha}</span></div>
<nav aria-label="Decision views">{nav}</nav><div class="tabs" role="tablist">{tabs}</div></div></header>
<main class="wrap">{body}</main><div class="toast" id="toast" role="status" aria-live="polite"></div>
<script>{script}</script></body></html>
"""


def _panelbar(text: str, *, store: bool = False) -> str:
    return ('<div class="panelbar"><p class="store"' + (' id="store"' if store else '') + '>' + text +
            '</p><span class="panelctl"><button type="button" class="lnk" data-all="min">Collapse all</button>'
            '<button type="button" class="lnk" data-all="max">Expand all</button></span></div>')


def build(today: dt.date, out: Path, *, reference_out: Path | None = None,
          owed_url: str | None = None, reference_url: str | None = None) -> dict:
    reference_out = reference_out or out.with_name("decision_reference.html")
    if out.resolve() == reference_out.resolve() or (out.exists() and reference_out.exists() and os.path.samefile(out, reference_out)):
        raise ValueError("Owed and reference outputs must be different files")
    if bool(owed_url) != bool(reference_url):
        raise ValueError("Provide both --owed-url and --reference-url, or neither for local viewing")
    if owed_url:
        owed_link, reference_link = _artifact_url(owed_url), _artifact_url(reference_url)
        if owed_link == reference_link:
            raise ValueError("Owed and reference must use distinct native artifact IDs")
        if owed_link != OWED_ARTIFACT_URL:
            raise ValueError("Keep Owed at the existing ruling artifact to preserve its store")
        link_mode = "hosted"
    else:
        owed_link = quote(os.path.relpath(out.resolve(), reference_out.resolve().parent), safe="/")
        reference_link = quote(os.path.relpath(reference_out.resolve(), out.resolve().parent), safe="/")
        link_mode = "local"
    text = Q.read_text(encoding="utf-8")
    expl = load_explainers()
    owed = parse_open(text)
    owed.sort(key=lambda r: (r["blocked"], bool(r.get("answered")), r["by"] or "9999-99-99"))
    decided, active, docket = parse_decided(), parse_active(), parse_docket(today)
    sha = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=ROOT).stdout.strip()
    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    build_id = f"{sha}·{stamp}"
    actionable = [r for r in owed if not r["blocked"] and not r.get("answered")]
    answered = [r for r in owed if not r["blocked"] and r.get("answered")]
    missing = [r["n"] for r in owed if r["n"] not in expl]
    owed_panels = [
        ("owed", "Owed", len(actionable), _panelbar('<span class="dot"></span> Reading only.', store=True)
         + (f'<p>{len(answered)} answered — hands or a dated action still owed.</p>' if answered else "")
         + (render_owed(owed, expl, today) or '<p class="empty">Nothing owed.</p>')),
        ("key", "Key", None, KEY),
    ]
    reference_panels = [
        ("decided", "Decided", len(decided), _panelbar('Every ruled or done row, newest first. Your word is quoted verbatim where it was recorded.') + render_decided(decided)),
        ("flight", "In-flight", len(active), _panelbar('Approved or in motion, not finished. Nothing here is owed by you unless a card says so.') + render_active(active)),
        ("docket", "Docket", len(docket), _panelbar('Dated catalysts whose owner cell names you.') + render_docket(docket)),
    ]
    page = _page("Decision Deck", "owed", owed_panels,
                 f'<a class="lnk" href="{html.escape(reference_link, quote=True)}">Reference: Decided · In-flight · Docket</a>', build_id, stamp, sha)
    reference = _page("Decision reference", "reference", reference_panels,
                     f'<a class="lnk" href="{html.escape(owed_link, quote=True)}">Back to Owed decisions</a>', build_id, stamp, sha)
    # Construct both outputs before writing. The normal candidate freeze covers the pair.
    for path, content in ((out, page), (reference_out, reference)):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return {"owed": len(owed), "actionable": len(actionable), "answered_hands": len(answered), "decided": len(decided), "active": len(active),
            "docket": len(docket), "explainers_missing": missing, "bytes": len(page.encode()), "out": str(out),
            "reference_out": str(reference_out), "reference_bytes": len(reference.encode()), "link_mode": link_mode}

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
    ap.add_argument("--reference-out", help="default: decision_reference.html beside Owed output")
    ap.add_argument("--owed-url", help="existing private Owed artifact URL; requires --reference-url")
    ap.add_argument("--reference-url", help="private reference artifact URL; requires --owed-url")
    ap.add_argument("--today", default=None, help="YYYY-MM-DD (default: system date)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    today = dt.date.fromisoformat(a.today) if a.today else dt.date.today()
    try:
        r = build(today, Path(a.out), reference_out=Path(a.reference_out) if a.reference_out else None,
                  owed_url=a.owed_url, reference_url=a.reference_url)
    except ValueError as error:
        ap.error(str(error))
    print(json.dumps(r, indent=1))
