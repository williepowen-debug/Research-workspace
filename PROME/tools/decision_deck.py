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

# ---- Change A (DOCKET L660, Will 2026-10-09 12:09/12:32/12:35 ET): selectable options, copied VERBATIM from the
# owner card and validated against the OFFERED set at build time. Acceptance: tests/ACCEPTANCE_deck_options_2026-10-09.md.
# Sidecar columns (optional, header-driven): `options` = one block per decision unit, blocks joined by " ;; ",
#   a block = optional "UNIT: " prefix + options joined by " || ", an option = "LABEL = text :: consequence".
#   `options_source` = "<path>#<section number>" (single unit) or "UNIT=<path>#<n> ;; UNIT=<path>#<n>".
# Shape "table": a markdown table inside the numbered section whose FIRST cell is `LABEL` or `LABEL: text`
#   (TERRY's §3 / §7 choice tables). Any other shape ⇒ fail closed: no buttons, a named warning (AC5).
OPTION_LABEL_RE = re.compile(r"^(?:[A-Z]{1,3}(?:-[A-Z]{1,3})?|\d{1,2})$")
_UNIT_PREFIX_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_-]{0,15}):\s+(?=\S)")


def _norm(s: str) -> str:
    """Comparison form: struck text (~~…~~) is ABSENT (a withdrawn card figure never ships as live text — episode 2 E3),
    then markdown stripped, whitespace collapsed."""
    s = re.sub(r"~~.*?~~", "", s or "", flags=re.S)
    s = re.sub(r"(?<![\w*])\*(?!\s)([^*]+?)\*(?![\w*])", r"\1", strip_md(s))   # single-asterisk italics → the text (ep2 read 2 W1)
    return re.sub(r"\s+", " ", s).strip()


_MD_MARKER_RE = re.compile(r"\*\*|~~|`")


def parse_options(cell: str, wq: str = "?") -> list[dict]:
    """`options` cell → [{"unit": str|None, "options": [{"label","text","consequence"}]}].
    A malformed cell is PROME's defect, so it raises (the build fails and names the WQ)."""
    cell = (cell or "").strip()
    if not cell:
        return []
    units = []
    for raw in cell.split(";;"):
        raw = raw.strip()
        if not raw:
            continue
        unit = None
        m = _UNIT_PREFIX_RE.match(raw)
        if m:
            unit, raw = m.group(1), raw[m.end():]
        opts = []
        if raw.strip().startswith(PLAIN_UNIT) and (raw.strip() == PLAIN_UNIT or raw.strip().startswith(PLAIN_UNIT + " ::")):
            # "UNIT: PLAIN :: reason :: APPROVE=<meaning> :: DECLINE=<meaning>" — a declared decision unit whose options
            # are deliberately NOT offered yet (e.g. the owner card is stale and its re-cut is owed); it renders plain
            # Approve/Decline/Later controls under its own decision_id so the row's other unit can still be ruled
            # separately (AC5/AC6). Read 2 ❌X2: a plain verb on a unit must say what it MEANS on that unit, and the tap
            # must store that meaning — so a multi-unit PLAIN block REQUIRES both meanings.
            parts = [x.strip() for x in raw.strip().split("::")]
            reason, meanings = "", {}
            tag = f"WQ-{wq}" + (f".{unit}" if unit else "")
            for x in parts[1:]:
                m2 = re.match(r"^(APPROVE|DECLINE)=(.*)$", x, re.S)
                if m2:
                    if m2.group(1) in meanings:
                        raise ValueError(f"{tag}: duplicate {m2.group(1)}= meaning on a PLAIN unit")
                    if not m2.group(2).strip():
                        raise ValueError(f"{tag}: empty {m2.group(1)}= meaning on a PLAIN unit")
                    meanings[m2.group(1)] = m2.group(2).strip()
                elif not reason and not meanings:
                    reason = x
                else:
                    raise ValueError(f"{tag}: unexpected '::' part '{x[:40]}' on a PLAIN unit (only reason :: APPROVE=… :: DECLINE=…; a '::' inside a meaning is not allowed)")
            if meanings and not ({"APPROVE", "DECLINE"} <= set(meanings)):
                raise ValueError(f"{tag}: a PLAIN unit with meanings must state BOTH APPROVE= and DECLINE=")
            units.append({"unit": unit, "options": [], "plain": True, "reason": reason or "options withheld by PROME",
                          "meanings": meanings})
            continue
        for piece in raw.split("||"):
            piece = piece.strip()
            if not piece:
                continue
            if " = " not in piece:
                raise ValueError(f"WQ-{wq}: option '{piece[:40]}' lacks 'LABEL = text'")
            label, rest = piece.split(" = ", 1)
            label = label.strip()
            if not OPTION_LABEL_RE.match(label):
                raise ValueError(f"WQ-{wq}: option label '{label}' is not a label token (A · R-A · 12)")
            text, _, cons = rest.partition("::")         # "LABEL = text :: consequence"; an empty consequence is allowed syntactically and refused at validation when the card row has cells
            text, cons = text.strip(), cons.strip()
            if not text:
                raise ValueError(f"WQ-{wq}: option {label} has no text")
            if _MD_MARKER_RE.search(text) or _MD_MARKER_RE.search(_PROME_BRACKET_RE.sub("", cons, count=1)):
                raise ValueError(f"WQ-{wq}: option {label} carries markdown markers (** ~~ `) — the sidecar holds plain text copied after markdown-strip")
            opts.append({"label": label, "text": text, "consequence": cons})
        labels = [o["label"] for o in opts]
        if not opts:
            raise ValueError(f"WQ-{wq}: an options block carries no option")
        if len(set(labels)) != len(labels):
            raise ValueError(f"WQ-{wq}: duplicate option labels {labels}")
        units.append({"unit": unit, "options": opts, "plain": False, "reason": ""})
    if len(units) > 1 and any(u["unit"] is None for u in units):
        raise ValueError(f"WQ-{wq}: a row with several decision units must name every unit ('UNIT: …')")
    if len(units) > 1:
        for u in units:
            if u.get("plain") and not ({"APPROVE", "DECLINE"} <= set(u.get("meanings", {}))):
                raise ValueError(f"WQ-{wq}.{u['unit']}: a PLAIN unit on a multi-decision row must state what APPROVE and "
                                 f"DECLINE mean on that unit ('UNIT: PLAIN :: reason :: APPROVE=… :: DECLINE=…')")
    if len({u["unit"] for u in units}) != len(units):
        raise ValueError(f"WQ-{wq}: duplicate decision units")
    return units


def parse_options_source(cell: str) -> dict:
    """`options_source` cell → {unit_or_None: (path, section)}. Malformed entries are skipped (fail closed at validation)."""
    out = {}
    for raw in (cell or "").split(";;"):
        raw = raw.strip()
        if not raw:
            continue
        unit = None
        if "=" in raw and "#" in raw and raw.index("=") < raw.index("#"):
            unit, raw = raw.split("=", 1)
            unit, raw = unit.strip(), raw.strip()
        if "#" not in raw:
            continue
        path, sec = raw.rsplit("#", 1)
        out[unit] = (path.strip(), sec.strip().lstrip("§"))
    return out


def offered_options(path: str, section: str) -> list[dict] | None:
    """The OFFERED set read from the owner artifact: table rows in the numbered section whose first cell is a
    label token (or `LABEL: text`). None when the file, the section or any label-shaped row is missing."""
    try:
        text = (ROOT / path).read_text(encoding="utf-8")
    except OSError:
        return None
    lines = text.splitlines()
    head = re.compile(r"^(#{1,6})\s*§?\s*" + re.escape(section) + r"(?:[.\s:)]|$)")
    start = level = None
    for i, ln in enumerate(lines):
        m = head.match(ln)
        if m:
            start, level = i + 1, len(m.group(1))
            break
    if start is None:
        return None
    body = []
    for ln in lines[start:]:
        hm = re.match(r"^(#{1,6})\s", ln)
        if hm and len(hm.group(1)) <= level:
            break
        body.append(ln)
    out, header, prev_header = [], None, None
    for ln in body:
        if not ln.lstrip().startswith("|"):
            header = None                                # a table ended; the next table brings its own header
            continue
        c = split_cells(ln)
        if is_separator(c):
            header = prev_header                         # the row just above a separator is that table's header
            continue
        prev_header = c
        if len(c) < 2:
            continue
        first = _norm(c[0])
        m = re.match(r"^([A-Z0-9-]{1,7})(?::\s*(.+))?$", first)
        if not m or not OPTION_LABEL_RE.match(m.group(1)):
            continue
        label = m.group(1)
        text = _norm(m.group(2)) if m.group(2) else _norm(c[1])
        rest = c[1:] if m.group(2) else c[2:]            # the row's other cells = the owner's own consequence columns
        hdrs = (header[1:] if m.group(2) else header[2:]) if header else []
        pieces = []
        for k, x in enumerate(rest):
            if not _norm(x):
                continue
            # ep2 read 2 ❌1: with several consequence columns the card's own column header travels with each cell
            # ("forward max loss from here: ~$475 …"), so a loss column is never read as a payoff
            h = _norm(hdrs[k]) if k < len(hdrs) else ""
            pieces.append(f"{h}: {_norm(x)}" if h and len([y for y in rest if _norm(y)]) > 1 else _norm(x))
        out.append({"label": label, "text": text, "cells": " · ".join(pieces)})
    return out or None


_PROME_BRACKET_RE = re.compile(r"\s*\[PROME:[^\]]*\]\s*$")
PLAIN_UNIT = "PLAIN"


def consequence_source(consequence: str) -> str:
    """The consequence with ONE trailing marked PROME annotation ("[PROME: …]" at the END) removed — what must be
    verbatim from the card. A bracket anywhere else is not an annotation: it stays in the text and fails equality
    (episode 2 E2), so PROME's words can never sit inside the owner's sentence."""
    return _norm(_PROME_BRACKET_RE.sub("", consequence or "", count=1))


def validate_options(wq: str, units: list[dict], sources: dict) -> tuple[list[dict], list[str]]:
    """AC4/AC5: returns (units that may render, warnings). A readable source with a label-for-label or text
    mismatch FAILS THE BUILD (SystemExit names the diff); an unreadable one drops the unit with a warning."""
    keep, warns = [], []
    def plain(u, reason):
        return {"unit": u["unit"], "options": [], "plain": True, "reason": reason, "source": None, "meanings": u.get("meanings", {})}
    # read 2 ⚠️W6 (the ❌4 class, reachable by one sidecar edit): the units the `options` cell declares and the units
    # `options_source` names must agree, or a named unit vanishes and the survivor re-keys to the whole row.
    declared = {u["unit"] for u in units}
    named = {k for k in sources if k is not None}
    if named and (named - declared or (len(units) > 1 and declared - named - {u["unit"] for u in units if u.get("plain")})):
        raise SystemExit(f"DECK REFUSED TO BUILD: WQ-{wq} options_source names units {sorted(named)} but the options cell "
                         f"declares {sorted(x for x in declared if x)} — the two must agree unit-for-unit")
    for u in units:
        key = u["unit"]
        tag = f"WQ-{wq}" + (f".{key}" if key else "")
        if u.get("plain"):
            keep.append(plain(u, u.get("reason") or "options withheld by PROME"))
            continue
        src = sources.get(key) if key in sources else (sources.get(None) if len(units) == 1 else None)
        offered = offered_options(*src) if src else None
        if offered is None:
            why = "no options_source registered" if not src else f"options_source {src[0]}#{src[1]} unreadable (file, section or label-shaped rows missing)"
            if len(units) > 1:
                # episode 2 E1 (read 3 ❌X3): a bare-verb fallback on a multi-decision row would show Will buttons with
                # no stated meaning and store choice.text "" — refuse instead; declare the unit PLAIN with meanings to ship it.
                raise SystemExit(f"DECK REFUSED TO BUILD: {tag} {why} — on a multi-decision row a unit never falls back to bare verbs; "
                                 f"declare it 'UNIT: PLAIN :: reason :: APPROVE=… :: DECLINE=…' or fix the source")
            warns.append(f"{tag}: {why} — options NOT rendered (plain card)")
            keep.append(plain(u, why)); continue
        off = {o["label"]: o["text"] for o in offered}
        cells = {o["label"]: o["cells"] for o in offered}
        deck = {o["label"]: o["text"] for o in u["options"]}
        missing = [l for l in off if l not in deck]
        extra = [l for l in deck if l not in off]
        if missing or extra:
            raise SystemExit(f"DECK REFUSED TO BUILD: {tag} option set differs from the OFFERED set at {src[0]}#{src[1]} — "
                             f"offered-but-missing {missing} · deck-but-not-offered {extra}")
        for o in u["options"]:
            l, t = o["label"], o["text"]
            if not off[l].startswith(_norm(t)):
                raise SystemExit(f"DECK REFUSED TO BUILD: {tag} option {l} text is not a prefix of the offered text at "
                                 f"{src[0]}#{src[1]} — deck '{_norm(t)[:60]}' vs offered '{off[l][:60]}'")
            # ❌2 of read 1 (2026-10-09): the consequence is the CARD's own cells, verbatim; PROME's words live only
            # inside a marked "[PROME: …]" bracket. Anything else is a paraphrase and refuses the build.
            src_text = consequence_source(o["consequence"])
            # read 2 ❌X1: a SUBSTRING test let a partial copy pass (the ⛔ half of a desk-view cell dropped, a max-loss
            # cell omitted, a bracket-only or one-character consequence). The consequence is the WHOLE of the row's
            # remaining cells, verbatim, or nothing ships.
            if src_text != cells[l]:
                raise SystemExit(f"DECK REFUSED TO BUILD: {tag} option {l} consequence is not the WHOLE of the card row's "
                                 f"remaining cells at {src[0]}#{src[1]} (verbatim, in order; PROME words only inside "
                                 f"'[PROME: …]') — deck '{src_text[:70]}' vs cells '{cells[l][:70]}'")
        keep.append({"unit": key, "options": u["options"], "plain": False, "reason": "", "source": src})
    return keep, warns


def options_for(expl_row: dict | None, wq: str) -> tuple[list[dict], list[str]]:
    """Units that render for this row (validated) + warnings. Empty when the sidecar carries no options."""
    if not expl_row or not (expl_row.get("options") or "").strip():
        return [], []
    units = parse_options(expl_row["options"], wq)
    return validate_options(wq, units, parse_options_source(expl_row.get("options_source", "")))


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

DONE_ROW_MIN_CELLS = 3          # title | done | record — done_rows_check.DONE_MIN must agree (tested, never imported; WQ-417 P1)
DONE_ROWS_SKIPPED: list = []    # every numbered done row this parser skipped, by name (AC4) — a silent skip hid two rulings on 2026-10-10


def parse_done_table(text: str, source: str) -> list[dict]:
    """3-col done rows: | **NNN Title** | Done | Record |  (also un-bolded 'NNN Title')."""
    rows = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        c = cells(line)
        m = re.match(r"\s*\**\s*(\d+[a-z]?)\b\s*(.*)", c[0]) if c else None
        if not m or c[0].lower().startswith("item"):
            continue
        if len(c) < DONE_ROW_MIN_CELLS:
            DONE_ROWS_SKIPPED.append({"n": m.group(1), "cells": len(c), "source": source})
            print(f"⚠️ decision_deck: {source} row {m.group(1)} has {len(c)} cell(s) (< {DONE_ROW_MIN_CELLS}) — SKIPPED: "
                  f"invisible to the Decided view and the event ledger; fix the ROW", file=sys.stderr)
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
        else:
            m = re.match(r"\s*\**\s*(\d+[a-z]?)\b", c[0]) if c else None
            if m:                                           # a numbered row too short for either shape: say so (WQ-417 AC4)
                DONE_ROWS_SKIPPED.append({"n": m.group(1), "cells": len(c), "source": source})
                print(f"⚠️ decision_deck: {source} row {m.group(1)} has {len(c)} cell(s) — SKIPPED by parse_archive; fix the ROW", file=sys.stderr)
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

# ---- Change B (Will 2026-10-09 17:06 ET assignment; ruled spec PROME/proposals/2026-10-09_deck-options-and-grouping-RULED.md
# §2d + §3; acceptance PROME/tools/tests/ACCEPTANCE_deck_changeB_2026-10-09.md) ----
_CLOCK_ET = re.compile(r"\b(\d{1,2}:\d{2}(?:[–-]\d{1,2}:\d{2})?\s*(?:ET|EDT|EST))\b")
_MONEY_KIND = re.compile(r"TRADE|\[APPROVE\]|BROKER", re.I)

def clock_of(r: dict) -> str | None:
    """AC-B6 (re-cut at read 1 ❌1): an explicit clock from the row's NEEDED-BY cell ONLY — the Item text
    carries registration/approval stamps that are NOT deadlines (the 10/9 read found four invented ones).
    Ranges (09:45–10:30 ET) are captured whole; a Needed-by holding FURTHER clock-like tokens beyond the
    match gets an ellipsis so one extracted clock never poses as the whole clause (the full cell is in
    the card's detail)."""
    cell = r.get("by_raw") or ""
    m = _CLOCK_ET.search(cell)
    if not m:
        return None
    rest = cell[:m.start()] + cell[m.end():]
    more = re.search(r"\b\d{1,2}:\d{2}\b", rest)
    return m.group(1) + ("\u2026" if more else "")

_RESERVED = {"All", "Trade", "Gate", "Rule", "Hands", "Launch", "Chore"}
_RESERVED_LC = {x.lower() for x in _RESERVED}

def kind_chip(kind: str) -> str:
    """Deterministic Type-cell -> chip map (AC-B1). Order matters: a 'RULE / register a gate' row IS a gate
    decision; money kinds pin separately (AC-B3) whatever their chip."""
    k = kind.upper()
    if "GATE" in k: return "Gate"
    if _MONEY_KIND.search(k): return "Trade"
    if k.startswith("RULE") or "/ RULE" in k or " RULE" in k: return "Rule"
    if "ACTION" in k or "HANDS" in k: return "Hands"
    if "LAUNCH" in k: return "Launch"
    return "Chore"

def is_pinned(r: dict, days: int | None) -> bool:
    """The ruled §2d amendment: due today/overdue · an explicit ET clock · money-moving Type.
    Pinned cards stay visible under EVERY chip, saved ones included; chips filter only the rest."""
    # read 1 ❌4: the ruling says ANY card — a blocked due/money card pins too (it has no tap controls,
    # but it must never vanish under a chip).
    return (days is not None and days <= 0) or bool(clock_of(r)) or bool(_MONEY_KIND.search(r.get("kind") or ""))

def due_pill(by: str | None, days: int | None, blocked: bool, blocker: str | None = None, clock: str | None = None) -> str:
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
    ck = ("" if not clock else (f" · {clock[:-1]}\u2026" if clock.endswith("\u2026") else f" · {clock}"))
    if days < 0:
        return f'<span class="pill crit">overdue {-days}d · {by}{ck}</span>'
    if days == 0:
        return f'<span class="pill crit">due today · {by}{ck}</span>'
    if days <= 2:
        return f'<span class="pill warn">{days}d left · {by}{ck}</span>'
    return f'<span class="pill ok">{days}d left · {by}{ck}</span>'

def render_unit(wq: str, unit: dict, multi: bool) -> str:
    did = f"{wq}.{unit['unit']}" if multi else wq
    head = (f'<div class="unit-h"><span class="did">{html.escape(did)}</span></div>' if multi else "")
    if unit.get("plain"):
        # a declared unit without offered options: today's plain controls under ITS OWN decision_id (❌4 of read 1);
        # each verb carries its stated meaning on this unit (❌X2 of read 2), stored with the tap as `choice.text`.
        mean = unit.get("meanings") or {}
        meaning_html = "".join(
            f'<p class="olbl">{html.escape(v.title())} — <span class="otext" data-for="{v}">{html.escape(mean[v])}</span></p>'
            for v in ("APPROVE", "DECLINE") if mean.get(v))
        return (
            f'<section class="tap unit" id="tap-{html.escape(did, quote=True)}" data-wq="{html.escape(wq, quote=True)}" data-did="{html.escape(did, quote=True)}">'
            f'{head}<p class="src">No choice buttons on this decision yet — {html.escape(unit.get("reason") or "")}.{" Approve / Decline / Later rule this decision only." if multi else ""}</p>'
            f'{meaning_html}'
            '<div class="tapstate" hidden></div>'
            '<div class="tapbtns">'
            f'<button type="button" class="btn approve" data-v="APPROVE" id="ap-{html.escape(did, quote=True)}">Approve</button>'
            f'<button type="button" class="btn decline" data-v="DECLINE" id="dc-{html.escape(did, quote=True)}">Decline</button>'
            f'<button type="button" class="btn later" data-v="LATER" id="lt-{html.escape(did, quote=True)}">Later</button>'
            '</div>'
            f'<input type="text" class="note" id="note-{html.escape(did, quote=True)}" placeholder="Note to PROME (optional)" maxlength="400">'
            '</section>'
        )
    path, sec = unit["source"]
    opts = "".join(
        f'<li class="opt" data-label="{html.escape(o["label"], quote=True)}">'
        f'<button type="button" class="btn choice" data-v="CHOICE" data-label="{html.escape(o["label"], quote=True)}" id="ch-{html.escape(did, quote=True)}-{html.escape(o["label"], quote=True)}">{html.escape(o["label"])}</button>'
        f'<div><p class="olbl">{html.escape(o["label"])} — <span class="otext">{html.escape(o["text"])}</span></p>'
        + (f'<p class="cons"><b>Then:</b> <span class="ocons">{html.escape(o["consequence"])}</span></p>' if o["consequence"] else '<p class="cons"><span class="ocons"></span></p>')
        + '</div></li>'
        for o in unit["options"])
    return (
        f'<section class="tap unit" id="tap-{html.escape(did, quote=True)}" data-wq="{html.escape(wq, quote=True)}" data-did="{html.escape(did, quote=True)}">'
        f'{head}<p class="src">Options copied from <code>{html.escape(path)}</code> §{html.escape(sec)} · labels, texts and consequences checked verbatim against the card at build; a [PROME: …] bracket is PROME\'s note</p>'
        f'<ul class="opts">{opts}</ul>'
        '<div class="tapstate" hidden></div>'
        '<div class="tapbtns">'
        f'<button type="button" class="btn later" data-v="LATER" id="lt-{html.escape(did, quote=True)}">Later</button>'
        f'<input type="text" class="note" id="note-{html.escape(did, quote=True)}" placeholder="Note to PROME (optional) — e.g. A, but after the 10/14 CPI print" maxlength="400">'
        '</div></section>'
    )


# read 2 ❌1: the guard keys on MARKERS, not meaning — restated contract: every MARKED caveat renders on
# the front; the marker set errs toward showing; FORWARD RULE (acceptance closing): PROME marks any
# decision-relevant caveat in a sidecar what/why cell with ⚠️ or the word "caveat".
_CAVEAT = re.compile(r"⚠|⛔|caveat|known[- ]unknown|unobserved|not proof|overrides your|does not yet show", re.I)

def render_owed(rows: list[dict], expl: dict, today: dt.date, warnings: list[str] | None = None) -> str:
    out = []
    # AC-B1 chip bar: kind chips from the Type cell; domain chips ONLY from the sidecar's declared `domains`
    # column (PROME-declared convenience labels, never owner classifications). Counts are card counts.
    kinds: dict[str, int] = {}
    doms: dict[str, int] = {}
    reserved = _RESERVED
    for r in rows:                                     # counts cover ALL rows incl. blocked (supersedes AC-B1's
        kinds[kind_chip(r["kind"])] = kinds.get(kind_chip(r["kind"]), 0) + 1   # "non-blocked" — blocked cards render under chips too)
        e0 = expl.get(r["n"])
        for d in ((e0.get("domains") or "") if e0 else "").replace("·", " ").split():
            if d.lower() in _RESERVED_LC:                 # read 1 ⚠️4 + read 2 ⚠️7: case-insensitive collision guard
                if warnings is not None:                  # would double a chip — dropped loudly, never rendered
                    warnings.append(f"WQ-{r['n']}: domain token {d!r} collides with a reserved chip name — dropped")
                continue
            doms[d] = doms.get(d, 0) + 1
    chip_order = [k for k in ("Trade", "Gate", "Rule", "Hands", "Launch", "Chore") if k in kinds]
    chips = "".join(f'<button type="button" class="chipbtn" data-chip="{k}">{k}<span class="n">{kinds[k]}</span></button>' for k in chip_order)
    chips += "".join(f'<button type="button" class="chipbtn dom" data-chip="{html.escape(d, quote=True)}">{html.escape(d)}<span class="n">{doms[d]}</span></button>' for d in sorted(doms))
    if chips:
        npin = sum(1 for r in rows if (r["_pin"] if "_pin" in r else is_pinned(r, (dt.date.fromisoformat(r["by"]) - today).days if r["by"] else None)))
        out.append('<div class="chipbar" title="Filters are a convenience: anything due, clocked or money-moving stays PINNED and visible under every chip. Domain labels are PROME-declared.">'
                   f'<button type="button" class="chipbtn on" data-chip="All">All</button>{chips}'
                   + (f'<span class="chipnote">{npin} pinned card(s) stay visible, each on top of its group, under every chip — except \'Waiting on others\', the one whole-group view without them</span>' if npin else '') + '</div>')
    # Change C (WQ-407 A, ACCEPTANCE_deck_changeC_2026-10-09.md): view switch + presets + the two overviews +
    # the peek shell. The table/grid rows carry the SAME data-attrs as cards so one filter governs all views;
    # clicking a row/tile relocates the REAL card node into the peek (AC-C4) — never a copy.
    GRPLBL = {"owed": "you", "answered": "hands owed", "blocked": "waiting"}
    trows, tiles = [], []
    for r in rows:
        g = "blocked" if r["blocked"] else ("answered" if r.get("answered") else "owed")
        d = (dt.date.fromisoformat(r["by"]) - today).days if r["by"] else None
        pn = r["_pin"] if "_pin" in r else is_pinned(r, d)   # same fallback as the card (the selftest renders without build's pre-pass)
        e1 = expl.get(r["n"])
        nm = (e1["name"] if e1 and e1.get("name") else r["name"])
        dm = " ".join(x for x in ((e1.get("domains") or "").replace("·", " ").split() if e1 else []) if x.lower() not in _RESERVED_LC)
        attrs = (f'data-wq="{r["n"]}" data-kchip="{kind_chip(r["kind"])}" data-dom="{html.escape(dm, quote=True)}"'
                 f' data-pin="{"1" if pn else "0"}" data-due="{html.escape(r["by"] or "9999-12-31", quote=True)}"'
                 f' data-grp="{g}" data-since="{html.escape(r["since"], quote=True)}"')
        pill = due_pill(r["by"], d, r["blocked"], r.get("blocker"), clock_of(r))
        trows.append(f'<tr class="ovrow" {attrs} tabindex="0"><td class="c-wq">WQ-{r["n"]}</td>'
                     f'<td class="c-pin">{"📌" if pn else ""}</td><td class="c-title">{html.escape(nm)}</td>'
                     f'<td class="c-who">{GRPLBL[g]}</td><td class="c-kind">{kind_chip(r["kind"])}</td>'
                     f'<td class="c-due">{pill}</td><td class="c-since">{html.escape(r["since"])}</td></tr>')
        tiles.append(f'<button type="button" class="ovtile" {attrs}><span class="t-top"><span class="num">WQ-{r["n"]}</span>'
                     f'{"<span class=\"pill pin\">PINNED</span>" if pn else ""}</span>{pill}'
                     f'<span class="t-kind">{kind_chip(r["kind"])} · {GRPLBL[g]}</span><span class="t-title">{html.escape(nm)}</span></button>')
    out.append(
        '<div class="viewbar">'
        '<span class="vb-lbl">View</span>'
        '<button type="button" class="vbtn on" data-view="list">List</button>'
        '<button type="button" class="vbtn" data-view="table">Table</button>'
        '<button type="button" class="vbtn" data-view="board">Board</button>'
        '<span class="vb-lbl vb-sep">Show</span>'
        '<button type="button" class="pbtn on" data-preset="all" title="Every card">Everything</button>'
        '<button type="button" class="pbtn" data-preset="today" title="Pinned + due today/overdue only">My action today</button>'
        '<button type="button" class="pbtn" data-preset="waiting" title="The blocked group only — the one view where pinned cards of other groups are absent, by design">Waiting on others</button>'
        '</div>'
        '<div class="ov ovtable" hidden><table><thead><tr>'
        '<th data-sort="wq" title="Plain ascending by number — pinned-first applies on the Deadline sort only">WQ</th><th title="Pinned">📌</th><th>Decision</th><th>Who acts</th><th>Type</th>'
        '<th data-sort="due" class="sorted" title="Default — pinned first, then date">Deadline</th><th title="Not sortable — these dates carry no year">Open since</th>'
        '</tr></thead><tbody>' + "".join(trows) + '</tbody></table></div>'
        '<div class="ov ovgrid" hidden>' + "".join(tiles) + '</div>'
        '<p class="ovempty" hidden></p>'
        '<aside id="peek" hidden><div class="peekbar">'
        '<button type="button" class="pk" id="pk-prev" title="Previous card">←</button>'
        '<button type="button" class="pk" id="pk-next" title="Next card">→</button>'
        '<span class="pk-pos" id="pk-pos"></span>'
        '<button type="button" class="pk" id="pk-close" title="Close (Esc)">Close ✕</button>'
        '</div><div id="peekbody"></div></aside>'
        '<div id="listwrap">')
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
        units, warns = ([], []) if r["blocked"] or r.get("answered") else options_for(e, r["n"])
        if warnings is not None:
            warnings.extend(warns)
        if len(units) == 1 and units[0].get("plain") and not units[0].get("meanings"):
            units = []                                   # a single declared-but-plain unit without meanings IS today's plain card (AC5)
        # AC-B5 (re-cut at read 1 ❌2/⚠️11): the front = the decision, If yes / If no (what the buttons DO,
        # beside the buttons), If nothing, the rec, and EVERY caveat. Only What-it-is / Why-it-is-yours move
        # behind Background — and ONLY when they carry no caveat marker; a card whose background text holds
        # ⚠/⛔/"caveat" renders in FULL on the front (fail toward showing, never toward hiding).
        if e and units and all(u.get("options") for u in units):
            bg_src = e["what"] + " " + e["why_yours"]
            if _CAVEAT.search(bg_src):
                block = (
                    '<dl class="expl">'
                    f'<dt>What it is</dt><dd>{html.escape(e["what"])}</dd>'
                    f'<dt>Why it is yours</dt><dd>{html.escape(e["why_yours"])}</dd>'
                    f'<dt>If nothing</dt><dd>{html.escape(e["if_nothing"])}</dd></dl>'
                    f'<p class="rec"><span class="lbl">PROME rec</span> {html.escape(e["rec_reason"])}</p>'
                )
            else:
                bg = (f'<dt>What it is</dt><dd>{html.escape(e["what"])}</dd>'
                      f'<dt>Why it is yours</dt><dd>{html.escape(e["why_yours"])}</dd>')
                block = (
                    f'<dl class="expl"><dt>If nothing</dt><dd>{html.escape(e["if_nothing"])}</dd></dl>'
                    f'<p class="rec"><span class="lbl">PROME rec</span> {html.escape(e["rec_reason"])}</p>'
                    f'<details class="more"><summary>Background — what it is · why it is yours</summary>'
                    f'<dl class="expl">{bg}</dl></details>'
                )
        elif e:
            bg_src = e["what"] + " " + e["why_yours"]
            if _CAVEAT.search(bg_src):
                block = (
                    '<dl class="expl">'
                    f'<dt>What it is</dt><dd>{html.escape(e["what"])}</dd>'
                    f'<dt>Why it is yours</dt><dd>{html.escape(e["why_yours"])}</dd>'
                    f'<dt>If yes</dt><dd>{html.escape(e["if_yes"])}</dd>'
                    f'<dt>If no</dt><dd>{html.escape(e["if_no"])}</dd>'
                    f'<dt>If nothing</dt><dd>{html.escape(e["if_nothing"])}</dd></dl>'
                    f'<p class="rec"><span class="lbl">PROME rec</span> {html.escape(e["rec_reason"])}</p>'
                )
            else:
                bg = (f'<dt>What it is</dt><dd>{html.escape(e["what"])}</dd>'
                      f'<dt>Why it is yours</dt><dd>{html.escape(e["why_yours"])}</dd>')
                block = (
                    '<dl class="expl">'
                    f'<dt>If yes</dt><dd>{html.escape(e["if_yes"])}</dd>'
                    f'<dt>If no</dt><dd>{html.escape(e["if_no"])}</dd>'
                    f'<dt>If nothing</dt><dd>{html.escape(e["if_nothing"])}</dd></dl>'
                    f'<p class="rec"><span class="lbl">PROME rec</span> {html.escape(e["rec_reason"])}</p>'
                    f'<details class="more"><summary>Background — what it is · why it is yours</summary>'
                    f'<dl class="expl">{bg}</dl></details>'
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
        if units:
            ctl = "".join(render_unit(r["n"], u, len(units) > 1) for u in units)
            if len(units) > 1:
                ctl = f'<div class="tapstate rowstate" id="rowstate-{r["n"]}" hidden></div>' + ctl
        elif r.get("answered") and not r["blocked"]:
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
        pin = r["_pin"] if "_pin" in r else is_pinned(r, days)
        dom = " ".join(d for d in ((e.get("domains") or "").replace("·", " ").split() if e else [])
                       if d.lower() not in _RESERVED_LC)   # read 2 ❌3: the card attr honors the same guard
        pin_pill = '<span class="pill pin" title="Due, clocked or money-moving: visible under every filter">PINNED</span>' if pin else ""
        out.append(
            f'<article class="card{" blocked" if r["blocked"] else ""}" id="wq-{r["n"]}" data-wq="{r["n"]}"'
            f' data-kchip="{kind_chip(r["kind"])}" data-dom="{html.escape(dom, quote=True)}" data-pin="{"1" if pin else "0"}" data-due="{html.escape(r["by"] or "", quote=True)}">'
            f'<div class="rail"><span class="num">WQ-{r["n"]}</span>{due_pill(r["by"], days, r["blocked"], r.get("blocker"), clock_of(r))}{pin_pill}{TOGGLE}</div>'
            '<div class="body">'
            f'<div class="meta"><span class="pill type">{html.escape(r["kind"])}</span>'
            f'<span class="since">open since {html.escape(r["since"])}</span></div>'
            f'<h2>{html.escape(name)}</h2>'
            f'{block}{detail}{ctl}'
            '</div></article>'
        )
    out.append('</div>')                                  # /listwrap (Change C)
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
<p>Approve, Decline, or Later writes one record to this page's private store: the row number, your verdict, your note, the time. Nothing executes off a tap. When a decision has named choices, the card shows one button per choice in the owner desk's own words, copied from its card and checked against it at build; a tap records the exact label, text and consequence you saw, and the full set shown. A row that holds two decisions records each on its own. At PROME's next boot it reads the store, writes your word into the queue verbatim as <em>"tap via Decision Deck"</em>, and marks the record picked up. The card shows its tap state until the next publish removes it. Trade and spend consequents still follow their own rails; a tap is your word arriving through a page instead of a message.</p>
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
.chipbar{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 4px}
.chipbtn{font:500 12.5px/1 "IBM Plex Mono",monospace;background:var(--chip);color:var(--ink);border:1px solid var(--line);border-radius:999px;padding:7px 12px;cursor:pointer}
.chipbtn .n{margin-left:6px;color:var(--muted)}
.chipbtn.on{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}.chipbtn.on .n{color:var(--accent-ink)}
.chipnote{font:11.5px/1.4 "IBM Plex Mono",monospace;color:var(--muted);align-self:center}
.viewbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:10px 0 4px}
.vb-lbl{font:600 11px/1.4 "IBM Plex Sans",sans-serif;letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}
.vb-sep{margin-left:10px}
.vbtn,.pbtn{font:500 12.5px/1 "IBM Plex Mono",monospace;background:var(--surface);color:var(--ink);border:1px solid var(--line);border-radius:4px;padding:7px 11px;cursor:pointer}
.vbtn.on,.pbtn.on{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.ovhide{display:none}
.ovtable{margin:12px 0}.ovtable table{width:100%;border-collapse:collapse;background:var(--surface);border:1px solid var(--line);border-radius:6px}
.ovtable th{font:600 11px/1.5 "IBM Plex Sans",sans-serif;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);text-align:left;padding:9px 10px;border-bottom:1px solid var(--line);cursor:default}
.ovtable th[data-sort]{cursor:pointer}.ovtable th.sorted{color:var(--accent)}
.ovtable td{font:13.5px/1.45 "IBM Plex Sans",sans-serif;padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}
.ovrow{cursor:pointer}.ovrow:hover td,.ovrow:focus-visible td{background:var(--chip)}
.c-wq{font:600 13px/1.4 "IBM Plex Mono",monospace;color:var(--accent);white-space:nowrap}
.c-title{max-width:34ch}.c-kind,.c-who,.c-since{font:12px/1.5 "IBM Plex Mono",monospace;color:var(--muted);white-space:nowrap}
.ovgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px;margin:12px 0}
@media (max-width:560px){.ovgrid{grid-template-columns:repeat(2,minmax(0,1fr))}.ovtile{padding:9px}}
.ovempty{color:var(--muted);font-size:14px;margin:12px 0}
.ovtile{display:flex;flex-direction:column;align-items:flex-start;gap:7px;text-align:left;background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:12px;cursor:pointer;font:inherit;color:var(--ink)}
.ovtile:hover,.ovtile:focus-visible{border-color:var(--accent)}
.t-top{display:flex;gap:8px;align-items:center}.t-kind{font:11.5px/1.4 "IBM Plex Mono",monospace;color:var(--muted)}
.t-title{font:600 14.5px/1.35 "IBM Plex Sans",sans-serif;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
#peek{position:fixed;top:0;right:0;width:min(600px,100vw);height:100vh;overflow:auto;background:var(--bg);border-left:1px solid var(--line);z-index:9;padding:14px 16px;box-shadow:-6px 0 24px rgba(0,0,0,.18)}
.peekbar{display:flex;gap:8px;align-items:center;margin-bottom:10px;position:sticky;top:0;background:var(--bg);padding:4px 0;z-index:1}
.pk{font:600 13px/1 "IBM Plex Mono",monospace;background:var(--surface);color:var(--ink);border:1px solid var(--line);border-radius:4px;padding:8px 12px;cursor:pointer}
#pk-close{margin-left:auto}.pk-pos{font:12px/1.4 "IBM Plex Mono",monospace;color:var(--muted)}
#peekbody .card{display:flex !important;margin-bottom:0}
.chiphide{display:none}
.pill.pin{background:var(--warn);color:#fff}
.asof{font:12px/1.5 "IBM Plex Mono",monospace;color:var(--muted);margin:6px 0 0}
details.more{margin:8px 0 0}details.more summary{cursor:pointer;font:500 13px/1.5 "IBM Plex Sans",sans-serif;color:var(--muted)}
.unit{gap:10px}.unit+.unit{margin-top:14px}
.unit-h .did{font:600 12px/1.4 "IBM Plex Mono",monospace;color:var(--accent)}
.src{font:12px/1.5 "IBM Plex Mono",monospace;color:var(--muted);margin:0;overflow-wrap:anywhere}
.opts{display:grid;gap:8px;margin:0;padding:0;list-style:none}
.opt{display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:start;border:1px solid var(--line);border-radius:6px;padding:10px;min-width:0}
.opt .btn.choice{min-width:44px;padding:8px 10px;font:600 13px/1 "IBM Plex Mono",monospace;border-color:var(--accent);color:var(--accent);background:transparent}
.opt.chosen{border-color:var(--accent);box-shadow:inset 0 0 0 1px var(--accent)}
.opt.chosen .btn.choice{background:var(--accent);color:var(--accent-ink)}
.opt .olbl{font-weight:600;margin:0}.opt .cons{margin:2px 0 0;color:var(--muted);font-size:14px}.opt .cons b{color:var(--ink);font-weight:600}
.card.ruled-choice{background:var(--tint-ok);border-color:var(--tint-ok-line)}.card.ruled-choice .tapstate{color:var(--ok)}
.tapstate.rowstate{border:1px dashed var(--line);background:transparent;margin-top:12px}
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
  // Change B chips + Change C views/presets/peek (WQ-407 A; ACCEPTANCE_deck_changeC_2026-10-09.md).
  // ONE filter governs cards, table rows and tiles: show = presetAllows && (pinnedNow || chip match).
  // Pinned exemption stays STRUCTURAL (read first) — only the explicit 'Waiting on others' preset, a
  // whole-group view, omits pinned cards of other groups (stated on its button).
  var bar = document.querySelector ? document.querySelector('.chipbar') : null;
  if (bar) {
    var chips = Array.prototype.slice.call(bar.querySelectorAll('.chipbtn'));
    var pbtns = Array.prototype.slice.call(document.querySelectorAll('.pbtn'));
    var chipKey = 'deck.chip.' + document.body.dataset.view;
    var presetKey = 'deck.preset.' + document.body.dataset.view;
    var curChip = 'All', curPreset = 'all';
    function etToday(){ try { return new Intl.DateTimeFormat('en-CA',{timeZone:'America/New_York',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date()); } catch(e){ var d = new Date(); return d.getFullYear() + '-' + ('0'+(d.getMonth()+1)).slice(-2) + '-' + ('0'+d.getDate()).slice(-2); } }
    function allUnits(){ return Array.prototype.slice.call(document.querySelectorAll('#owed .card, #owed .ovrow, #owed .ovtile')); }
    var applyFilters = function(chipVal, preset, save){
      if (save === undefined) save = true;
      curChip = chipVal; curPreset = preset;
      chips.forEach(function(c){ c.classList.toggle('on', c.dataset.chip === chipVal); });
      pbtns.forEach(function(b){ b.classList.toggle('on', b.dataset.preset === preset); });
      var todayLocal = etToday();
      allUnits().forEach(function(el){
        var pinNow = el.dataset.pin === '1' || (el.dataset.due && el.dataset.due <= todayLocal);
        var presetOk = preset === 'all' ? true
                     : preset === 'today' ? (pinNow)
                     : (el.dataset.grp ? el.dataset.grp === 'blocked' : el.classList.contains('blocked'));
        var chipOk = pinNow || chipVal === 'All' || el.dataset.kchip === chipVal ||
          (' ' + (el.dataset.dom || '') + ' ').indexOf(' ' + chipVal + ' ') >= 0;
        if (preset === 'waiting') chipOk = true;           // the whole-group view ignores chips
        el.classList.toggle('chiphide', !(presetOk && chipOk));
      });
      refreshGroups();
      var emptyEl = document.querySelector('.ovempty');
      if (emptyEl) {
        var anyVisible = allUnits().some(function(el){ return !el.classList.contains('chiphide'); });
        emptyEl.hidden = anyVisible;
        if (!anyVisible) {                                 // read 2 ❌1: the note names the CAUSE and counts LIVE — nothing baked
          var nCards = document.querySelectorAll('#owed .card').length;
          emptyEl.textContent = 'Nothing matches this view — ' +
            (preset === 'waiting' ? '"Waiting on others" shows only the blocked group, and it is empty right now.' :
             preset === 'today' ? 'nothing is pinned or due today under this filter.' : 'this filter hides every card.') +
            ' Tap Everything to see all ' + nCards + ' cards.';
        }
      }
      refreshPeekPos();                                    // read 1 ⚠️11: the position line follows the live view
      if (save) { try{ localStorage.setItem(chipKey, chipVal); localStorage.setItem(presetKey, preset); }catch(e){} }
    };
    function refreshGroups(){                              // read 1 ❌7: re-run after any relocation too
      Array.prototype.slice.call(document.querySelectorAll('#owed .grp')).forEach(function(g){
        var el = g.nextElementSibling, any = false;
        while (el && !(el.classList && el.classList.contains('grp'))) {
          if (el.classList && el.classList.contains('card') && !el.classList.contains('chiphide')) { any = true; break; }
          el = el.nextElementSibling;
        }
        g.classList.toggle('chiphide', !any);
      });
    }
    chips.forEach(function(c){ c.addEventListener('click', function(){ applyFilters(c.dataset.chip, curPreset); }); });
    pbtns.forEach(function(b){ b.addEventListener('click', function(){
      var blankNow = !allUnits().some(function(el){ return !el.classList.contains('chiphide'); });
      // read 3 ❌1: from a blank page, Everything is the escape hatch the note names — it resets the chip
      // too, so "see all N cards" is literally what the tap shows.
      applyFilters(blankNow && b.dataset.preset === 'all' ? 'All' : curChip, b.dataset.preset);
    }); });
    var sv = 'All', sp = 'all';
    try{ var s2 = localStorage.getItem(chipKey); if (s2 && chips.some(function(c){ return c.dataset.chip === s2; })) sv = s2;
         var s3 = localStorage.getItem(presetKey); if (s3 === 'today' || s3 === 'waiting') sp = s3; }catch(e){}
    applyFilters(sv, sp);
    if (!allUnits().some(function(el){ return !el.classList.contains('chiphide'); })) {
      applyFilters(sv, 'all', false);                      // read 1 ❌5: a saved view may never open a BLANK page
    }
    if (location.hash) { var tgt = document.getElementById(location.hash.slice(1)); if (tgt && tgt.classList && tgt.classList.contains('chiphide')) applyFilters('All', 'all', false); }

    // --- view toggle (AC-C1) ---
    var vbtns = Array.prototype.slice.call(document.querySelectorAll('.vbtn'));
    var ovTable = document.querySelector('.ovtable'), ovGrid = document.querySelector('.ovgrid');
    var listWrap = document.getElementById('listwrap');
    var viewKey = 'deck.viewmode.' + document.body.dataset.view;
    var curView = 'list';
    function setView(v, save){
      curView = v;
      vbtns.forEach(function(b){ b.classList.toggle('on', b.dataset.view === v); });
      if (ovTable) ovTable.hidden = (v !== 'table');
      if (ovGrid) ovGrid.hidden = (v !== 'board');
      if (listWrap) listWrap.classList.toggle('ovhide', v !== 'list');
      closePeek();                                       // read 1 ⚠️12: a view switch always closes the peek — its order belongs to one view
      if (save === undefined || save) { try{ localStorage.setItem(viewKey, v); }catch(e){} }
    }
    vbtns.forEach(function(b){ b.addEventListener('click', function(){ setView(b.dataset.view); }); });
    var v0 = 'list'; try{ var vs = localStorage.getItem(viewKey); if (vs === 'table' || vs === 'board') v0 = vs; }catch(e){}

    // --- table sort (AC-C2 as re-cut): due default (pinned first), wq; open-since is not sortable ---
    function sortTable(key){
      if (!ovTable || !ovTable.querySelector) return;
      var tb = ovTable.querySelector('tbody'); if (!tb) return;
      var rows = Array.prototype.slice.call(tb.querySelectorAll('.ovrow'));
      var todayS = etToday();
      function pinNowOf(el){ return el.dataset.pin === '1' || (el.dataset.due && el.dataset.due <= todayS); }
      rows.sort(function(a, b){
        if (key === 'wq') return parseInt(a.dataset.wq, 10) - parseInt(b.dataset.wq, 10);
        var p = pinNowOf(b) - pinNowOf(a);                 // read 1 ⚠️10: the sort's pin = the filter's pin
        return p !== 0 ? p : String(a.dataset.due).localeCompare(String(b.dataset.due));
      });
      rows.forEach(function(r){ tb.appendChild(r); });
      Array.prototype.slice.call(ovTable.querySelectorAll('th[data-sort]')).forEach(function(h){ h.classList.toggle('sorted', h.dataset.sort === key); });
    }
    if (ovTable && ovTable.querySelectorAll) Array.prototype.slice.call(ovTable.querySelectorAll('th[data-sort]')).forEach(function(h){ h.addEventListener('click', function(){ sortTable(h.dataset.sort); }); });

    // --- the peek (AC-C4): relocate the REAL card node; return it to its exact slot on close ---
    var peek = document.getElementById('peek'), peekBody = document.getElementById('peekbody'), pkPos = document.getElementById('pk-pos');
    var peekAnchor = null, peekedCard = null, peekedWasMin = false;
    function refreshPeekPos(){
      if (!peekedCard || !pkPos) return;
      var ord = visOrder(), i = ord.indexOf(peekedCard.dataset.wq);
      pkPos.textContent = (i >= 0 ? (i + 1) + ' of ' + ord.length + ' in view' : 'WQ-' + peekedCard.dataset.wq + ' (filtered out of this view)');
    }
    function visOrder(){
      var src = curView === 'table' ? '#owed .ovrow' : '#owed .ovtile';
      return Array.prototype.slice.call(document.querySelectorAll(src)).filter(function(el){ return !el.classList.contains('chiphide'); }).map(function(el){ return el.dataset.wq; });
    }
    function closePeek(){
      if (!peekedCard) return;
      if (peekAnchor && peekAnchor.parentNode) { peekAnchor.parentNode.insertBefore(peekedCard, peekAnchor); peekAnchor.parentNode.removeChild(peekAnchor); }
      peekedCard.classList.remove('peeked');
      if (peekedWasMin) peekedCard.classList.add('min');   // read 1 ❌4: a minimized card goes back minimized
      peekAnchor = null; peekedCard = null; peekedWasMin = false;
      if (peek) peek.hidden = true;
      refreshGroups();                                     // read 1 ❌7: headings recount after the node returns
    }
    function openPeek(wq){
      var card = document.getElementById('wq-' + wq); if (!card || !card.parentNode || !peekBody) return;
      closePeek();
      peekAnchor = document.createComment ? document.createComment('peek-' + wq) : null;
      if (peekAnchor) card.parentNode.insertBefore(peekAnchor, card);
      peekBody.appendChild(card);                          // the SAME node — taps/options/tapstate all live (AC-C4)
      peekedWasMin = card.classList.contains('min');
      card.classList.add('peeked'); card.classList.remove('min');
      peekedCard = card; peek.hidden = false;
      var ord = visOrder(), i = ord.indexOf(wq);
      if (pkPos) pkPos.textContent = (i >= 0 ? (i + 1) + ' of ' + ord.length + ' in view' : 'WQ-' + wq);
    }
    function peekStep(dir){
      if (!peekedCard) return;
      var ord = visOrder(), i = ord.indexOf(peekedCard.dataset.wq);
      var nx = ord[i + dir]; if (nx !== undefined) openPeek(nx);
    }
    allUnits().forEach(function(el){
      if (el.classList.contains('card')) return;
      var act = function(){ openPeek(el.dataset.wq); };
      el.addEventListener('click', act);
      el.addEventListener('keydown', function(ev){ if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); act(); } });
    });
    var pkPrev = document.getElementById('pk-prev'), pkNext = document.getElementById('pk-next'), pkClose = document.getElementById('pk-close');
    if (pkPrev) pkPrev.addEventListener('click', function(){ peekStep(-1); });
    if (pkNext) pkNext.addEventListener('click', function(){ peekStep(1); });
    if (pkClose) pkClose.addEventListener('click', closePeek);
    if (document.addEventListener) document.addEventListener('keydown', function(ev){
      if (!peekedCard) return;
      var tg = ev.target;                                  // read 1 ❌3: never hijack keys while the operator types
      if (tg && (tg.tagName === 'INPUT' || tg.tagName === 'TEXTAREA' || tg.isContentEditable)) return;
      if (ev.key === 'Escape') closePeek();
      else if (ev.key === 'ArrowLeft') peekStep(-1);
      else if (ev.key === 'ArrowRight') peekStep(1);
    });
    setView(v0, false);
    sortTable('due');
    // read 1 ❌6: a deep link still lands when the saved view hides the list — open the card in the peek
    if (location.hash && curView !== 'list') {
      var dlCard = document.getElementById(location.hash.slice(1));
      if (dlCard && dlCard.classList && dlCard.classList.contains('card') && dlCard.dataset.wq) openPeek(dlCard.dataset.wq);
    }
  }
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
  // Change A (L660): a tap wrap is a whole card (`.tap`, data-did = the WQ) or ONE decision unit inside a card
  // (`.tap.unit`, data-did = "<wq>.<UNIT>"); state is keyed by decision id, the tint by the card.
  function wrapOf(did){ return document.getElementById('tap-'+did); }
  function cardOf(did, wrap){ var c = wrap && wrap.closest ? wrap.closest('.card') : null; return c || document.getElementById('wq-'+String(did).split('.')[0]); }
  var TINT_TS = {};
  function setState(did, cls, text, verdict, label, ts){
    var wrap = wrapOf(did); var card = cardOf(did, wrap); if(!card) return;
    // episode 2 E6: a document with NO unit on a multi-unit card goes to the card-level line, never into a unit
    var rowline = document.getElementById('rowstate-' + String(did).split('.')[0]);
    var st = (wrap && wrap.querySelector && wrap.querySelector('.tapstate')) || rowline || card.querySelector('.tapstate'); if(!st) return;
    st.className = 'tapstate ' + cls + (st === rowline ? ' rowstate' : ''); st.textContent = (st === rowline ? 'Whole-row tap (no unit): ' : '') + text; st.hidden = false;
    // the card tint follows the LATEST document by ts among the card's units and row, not iteration order
    var ck = card.id || String(did); var t = ts || '';
    if (cls === 'sent' && verdict && t >= (TINT_TS[ck] || '')) {
      TINT_TS[ck] = t;
      card.classList.remove('ruled-approve','ruled-decline','ruled-later','ruled-choice');
      card.classList.add('ruled-' + String(verdict).toLowerCase());
    } else if (cls === 'err') { card.classList.remove('ruled-approve','ruled-decline','ruled-later','ruled-choice'); }
    if (wrap && wrap.querySelectorAll) { var opts = wrap.querySelectorAll('.opt'); for (var i = 0; i < opts.length; i++) { opts[i].classList.toggle('chosen', !!label && opts[i].dataset.label === label); } }
  }
  function fmt(iso){ if (typeof iso !== 'string') return ''; try{ return new Date(iso).toLocaleString('en-US',{month:'numeric',day:'numeric',hour:'numeric',minute:'2-digit',timeZone:'America/New_York'}) + ' ET'; }catch(e){ return iso; } }
  function describe(x){ if (x.choice && x.choice.text) { return (x.verdict === 'CHOICE' ? 'CHOICE ' + x.choice.label : String(x.verdict)) + ' — ' + x.choice.text; } return String(x.verdict); }
  if (!(window.claude && window.claude.use)) { storeLine.textContent = 'Tap-to-rule is off in this view (no runtime). Reading only.'; return; }
  storeLine.textContent = 'Connecting to the ruling store…';
  window.claude.use('db').then(function(db){
    if (!db) { storeLine.textContent = 'Tap-to-rule unavailable in this view. Reading only; rule by message instead.'; return; }
    storeLine.classList.add('live'); storeLine.innerHTML = '<span class="dot"></span> Ruling store connected. A tap is your word; PROME picks it up at its next boot.';
    buttons.forEach(function(b){ b.disabled = false; });
    var col = db.collection('rulings');
    col.onSnapshot(function(snap){
      var latest = {};
      snap.docs.forEach(function(d){ var x = d.data() || {}; var k = x.decision_id || x.wq; if (!k) return; if (!latest[k] || (x.ts||'') > (latest[k].ts||'')) latest[k] = x; });
      Object.keys(latest).forEach(function(k){
        var x = latest[k];
        var when = x.ts ? fmt(x.ts) : '';
        var lab = x.choice && x.choice.label;
        // AC-B7: three stages, each stamped. ① recorded ② received by PROME (receipt, NEVER execution)
        // ③ disposition — rendered ONLY when PROME's pickup wrote it; the page never invents one.
        if (x.consumed) {
          var stampv = x.consumed_at || x.picked_up || x.pickup;   // consumed_at is what pickups actually write (store-verified 10/9)
          var fs = (typeof stampv === 'string' && fmt(stampv)) || '(pickup stamp not recorded)';   // read 2 ⚠️8: a non-string stamp never renders blank
          var by = (typeof x.consumed_by === 'string' && x.consumed_by) ? ' (' + x.consumed_by + ')' : '';
          var tail;
          if (typeof x.disposition === 'string' && x.disposition) {
            tail = ' · ③ Disposition recorded' + (typeof x.disposition_ts === 'string' ? ' ' + fmt(x.disposition_ts) : '') + ': ' + x.disposition;
          } else if (typeof x.recorded_as === 'string' && x.recorded_as) {
            tail = ' · ③ Recorded in the queue as: ' + x.recorded_as + ' — execution follows that record, never the tap itself';   // read 2 ⚠️9 + DP6
          } else {
            tail = ' · receipt is not execution — a disposition shows here only once PROME records one';
          }
          setState(k, 'sent', '② Received by PROME' + by + ' ' + fs + ' — ① recorded ' + when + ': ' + describe(x) + (x.note ? ' — ' + x.note : '') + tail, x.verdict, lab, x.ts);
        }
        else setState(k, 'sent', '① Recorded ' + when + ': ' + describe(x) + (x.note ? ' — ' + x.note : '') + ' · awaiting PROME pickup', x.verdict, lab, x.ts);
      });
    }, function(e){ storeLine.textContent = 'Ruling store error: ' + (e && e.code ? e.code : 'unknown'); });
    buttons.forEach(function(b){
      b.addEventListener('click', function(){
        var wrap = b.closest('.tap'); var wq = wrap.dataset.wq; var did = wrap.dataset.did || wq; var verdict = b.dataset.v;
        var note = (document.getElementById('note-'+did) || {}).value || '';
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
        var doc = {wq: wq, verdict: verdict, note: note.trim(), ts: ts, build: BUILD, consumed: false, source: 'decision-deck'};
        var label = null;
        if (wrap.classList && wrap.classList.contains('unit')) {
          // a decision UNIT: the exact terms shown travel with the tap (AC3) — label, text, consequence, and the whole set
          var opts = Array.prototype.slice.call(wrap.querySelectorAll('.opt'));
          doc.decision_id = did;
          doc.options_shown = opts.map(function(o){ return {label: o.dataset.label, text: (o.querySelector('.otext') || {}).textContent || ''}; });
          if (verdict === 'CHOICE') {
            label = b.dataset.label;
            var li = b.closest('.opt');
            doc.choice = {label: label, text: ((li && li.querySelector('.otext')) || {}).textContent || '', consequence: ((li && li.querySelector('.ocons')) || {}).textContent || ''};
          } else if (verdict === 'APPROVE' || verdict === 'DECLINE') {
            // a PLAIN unit: the verb's stated meaning on THIS unit travels with the tap (read 2 ❌X2)
            var mt = wrap.querySelector('.otext[data-for="' + verdict + '"]');
            doc.choice = {label: verdict, text: (mt && mt.textContent) || '', consequence: ''};
          } else { doc.choice = null; }
        }
        var shown = describe(doc);
        col.doc(id).set(doc)
          .then(function(){ toast('Recorded: WQ-' + did + ' ' + shown); setState(did, 'sent', '① Recorded ' + fmt(ts) + ': ' + shown + (note ? ' — ' + note.trim() : '') + ' · awaiting PROME pickup · the LATEST tap rules', verdict, label, ts); for (var i2 = 0; i2 < sibs.length; i2++) { sibs[i2].disabled = false; } })
          .catch(function(e){ for (var i3 = 0; i3 < sibs.length; i3++) { sibs[i3].disabled = false; } var c = (e && e.code) || 'error'; setState(did, 'err', 'Not recorded (' + c + '). Rule by message instead.', null, null, ts); toast('Not recorded: ' + c); });
      });
    });
  }).catch(function(){ storeLine.textContent = 'Tap-to-rule unavailable in this view. Reading only.'; });
})();
"""

JS = UI_JS + RULING_JS


OWED_ARTIFACT_URL = "https://claude.ai/code/artifact/16655022-6e00-4cea-9916-7cb0ff304bca"


def _artifact_url(value: str) -> str:
    # Two native forms (2026-09-22): the legacy /code/artifact/<UUID> and the current
    # /artifact/<short id> the host now issues for new artifacts. Each is returned in its
    # OWN form — the short id is case-sensitive, so it is never lower-cased or rewritten.
    match = re.fullmatch(r"https://claude\.ai/code/artifact/([0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12})/?", value)
    if match:
        return "https://claude.ai/code/artifact/" + match[1].lower()
    match = re.fullmatch(r"https://claude\.ai/artifact/([A-Za-z0-9]{16,40})/?", value)
    if match:
        return "https://claude.ai/artifact/" + match[1]
    raise ValueError("Hosted links must be native https://claude.ai/code/artifact/<UUID> or https://claude.ai/artifact/<id> URLs")


HOSTED_REFERENCE_STATE = Path(__file__).resolve().parents[1] / "state" / "deck_reference_hosted.json"


def _hosted_reference_note(path: Path | None = None) -> str:
    """WQ-382 (a), Will 2026-10-08: the reference page republishes only on Will's word or at a spine
    audit, so the Owed page's link must say how old the HOSTED reference is. Reads the state file the
    republishing sitting maintains; a missing/unreadable file renders UNKNOWN on the page, never silence."""
    path = HOSTED_REFERENCE_STATE if path is None else path
    tail = "refreshes on Will's word or at a spine audit"
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        built, version = str(data["built"]).strip(), str(data["version"]).strip()
        if not built or not version:
            raise ValueError("empty built/version")
        return f"hosted build {built} ({version}); {tail}"
    except (OSError, ValueError, KeyError, TypeError):
        return f"hosted build UNKNOWN (state file missing or unreadable); {tail}"


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
    for r in owed:                                        # read 1 ❌3: pin BEFORE the sort so pinned cards sit
        d = (dt.date.fromisoformat(r["by"]) - today).days if r["by"] else None   # AT THE TOP of their group
        r["_pin"] = is_pinned(r, d)                       # (the ruled three groups stay; §2d "at the top")
    owed.sort(key=lambda r: (r["blocked"], bool(r.get("answered")), not r["_pin"], r["by"] or "9999-99-99"))
    decided, active, docket = parse_decided(), parse_active(), parse_docket(today)
    sha = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=ROOT).stdout.strip()
    from zoneinfo import ZoneInfo
    stamp = dt.datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M") + " ET"  # AC-B8 (read 1 ⚠️9: explicit TZ)
    build_id = f"{sha}·{stamp}"
    actionable = [r for r in owed if not r["blocked"] and not r.get("answered")]
    answered = [r for r in owed if not r["blocked"] and r.get("answered")]
    missing = [r["n"] for r in owed if r["n"] not in expl]
    option_warnings: list[str] = []
    owed_html = render_owed(owed, expl, today, option_warnings)   # AC4: a mismatch raises SystemExit BEFORE any write
    for w in option_warnings:
        print(f"⚠️ decision_deck: {w}", file=sys.stderr)
    option_rows = sorted({r["n"] for r in owed if (expl.get(r["n"]) or {}).get("options", "").strip()}, key=lambda n: int(re.match(r"\d+", n).group(0)))
    owed_panels = [
        ("owed", "Owed", len(actionable), _panelbar('<span class="dot"></span> Reading only.', store=True)
         + f'<p class="asof">Built {html.escape(stamp)} · figures carry their own observation dates — a freshly built page does not refresh them; an undated figure is a defect to report.</p>'
         + (f'<p>{len(answered)} answered — hands or a dated action still owed.</p>' if answered else "")
         + (owed_html or '<p class="empty">Nothing owed.</p>')),
        ("key", "Key", None, KEY),
    ]
    reference_panels = [
        ("decided", "Decided", len(decided), _panelbar('Every ruled or done row, newest first. Your word is quoted verbatim where it was recorded.') + render_decided(decided)),
        ("flight", "In-flight", len(active), _panelbar('Approved or in motion, not finished. Nothing here is owed by you unless a card says so.') + render_active(active)),
        ("docket", "Docket", len(docket), _panelbar('Dated catalysts whose owner cell names you.') + render_docket(docket)),
    ]
    page = _page("Decision Deck", "owed", owed_panels,
                 f'<a class="lnk" href="{html.escape(reference_link, quote=True)}">Reference: Decided · In-flight · Docket</a> <span class="build">— {html.escape(_hosted_reference_note())}</span>', build_id, stamp, sha)
    reference = _page("Decision reference", "reference", reference_panels,
                     f'<a class="lnk" href="{html.escape(owed_link, quote=True)}">Back to Owed decisions</a>', build_id, stamp, sha)
    # ⛔ F2 (L423 fourth independent read, 2026-09-19) — REFUSE TO WRITE A BLANK DECK.
    # A header-width change in WILL_QUEUE.md made `parse_open` return [] while three rows
    # were dated TODAY, and this build rendered `<p class="empty">Nothing owed.</p>` onto
    # WILL'S LIVE DECISION SURFACE. The only signal was stderr; Will reads the HTML.
    # The ≥1-row assertion already existed at selftest() and the build never called it —
    # a control that exists and is not wired is not a control
    # ([[finding_guard_correctness_and_wiring_are_independent]]).
    # ⚠️ The CONTRACT is also wrong and is registered separately: acceptance B8 licenses
    # "skipped with one named failure" for the Deck, which is exactly the state B3 forbids
    # ("the Deck is Will's live surface … it must not go dark over one cell"). This guard
    # implements B3; B8 needs amending by its owner.
    # An EMPTY queue is a real state, so the refusal is scoped to the INCOHERENT one:
    # zero parsed rows while the source plainly contains rows.
    if not owed:
        import re as _re
        raw = Q.read_text(encoding="utf-8")
        sect = raw.split("## OPEN", 1)[-1].split("\n## ", 1)[0]
        looks_populated = len(_re.findall(r"^\|\s*\d+\s*\|", sect, _re.M))
        if looks_populated:
            raise SystemExit(
                f"DECK REFUSED TO BUILD: parse_open() returned 0 rows while § OPEN contains "
                f"{looks_populated} row-shaped lines. Writing would publish 'Nothing owed.' over "
                f"live dated asks on Will's decision surface. Fix the table (most likely a header-"
                f"width change or an unescaped pipe) and re-run. ⛔ Refusing is correct here: a "
                f"blank deck is indistinguishable from a clear one.")

    # Construct both outputs before writing. The normal candidate freeze covers the pair.
    for path, content in ((out, page), (reference_out, reference)):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return {"owed": len(owed), "actionable": len(actionable), "answered_hands": len(answered), "decided": len(decided), "active": len(active),
            "docket": len(docket), "explainers_missing": missing, "options_rows": option_rows,
            "options_warnings": option_warnings, "done_rows_skipped": DONE_ROWS_SKIPPED, "bytes": len(page.encode()), "out": str(out),
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
    ncol = len(EXPL.read_text(encoding="utf-8").splitlines()[0].split("\t")) if EXPL.exists() else 0
    chk("explainer sidecar header is 10 or 11 columns and every row matches it", ncol in (10, 11) and all(len(v) == ncol for v in e.values()), f"{len(e)} rows · {ncol} columns")
    # Change A (L660): every OPEN row with options validates against its owner artifact; ≥1 options row and ≥1 plain row covered
    opt_rows, plain_rows, opt_fail, opt_warn = [], [], [], []
    for r in o:
        if r["blocked"] or r.get("answered"):
            continue
        ex = e.get(r["n"])
        if ex and (ex.get("options") or "").strip():
            try:
                units, warns = options_for(ex, r["n"])
                opt_warn.extend(warns)
                if any(u.get("options") for u in units):
                    opt_rows.append(r["n"])
            except (SystemExit, ValueError) as err:
                opt_fail.append(f"WQ-{r['n']}: {err}")
        else:
            plain_rows.append(r["n"])
    chk("options rows validate against their owner artifacts (label-for-label, text prefix)", not opt_fail, " · ".join(opt_fail)[:300] or f"{len(opt_rows)} row(s): {opt_rows}")
    chk("options rows render (no unit dropped by an unreadable source)", not opt_warn, " · ".join(opt_warn)[:300] or "none dropped")
    if ncol == 10 and opt_rows:
        chk("≥1 options row AND ≥1 plain row in the live OPEN set (AC8)", bool(plain_rows), f"options {opt_rows} · plain {len(plain_rows)}")
    elif ncol == 10:
        chk("options WITHHELD on every row (10-column sidecar, no options cell filled) — the page renders plain cards", True, f"plain {len(plain_rows)}")
    chk("md() escapes HTML before styling", md("<b>x</b> **y**") == "&lt;b&gt;x&lt;/b&gt; <strong>y</strong>")
    # Change B (AC-B10): pins + chips on the live sources
    today0 = dt.date.today()
    live = [r for r in o if not r["blocked"]]
    owes_pin = [r["n"] for r in live if ((dt.date.fromisoformat(r["by"]) - today0).days <= 0 if r["by"] else False) or _MONEY_KIND.search(r["kind"] or "") or clock_of(r)]
    pinned = [r["n"] for r in live if is_pinned(r, (dt.date.fromisoformat(r["by"]) - today0).days if r["by"] else None)]
    chk("every due-today/overdue, clocked or money row is pinned (AC-B3)", set(owes_pin) <= set(pinned), f"pin-owed {owes_pin} vs pinned {pinned}")
    page_html = render_owed(live, e, today0, [])
    chk("chip bar renders when ≥1 non-blocked row exists (AC-B1)", ('class="chipbar"' in page_html) == bool(live))
    import re as _re
    bgs = _re.findall(r'<details class="more">.*?</details>', page_html, _re.S)
    bad_bg = [b[:60] for b in bgs if _re.search(r"⚠|⛔|caveat|known[- ]unknown", b, _re.I)]
    chk("no caveat marker hides behind a Background expander (read 1 ❌2)", not bad_bg, "; ".join(bad_bg)[:200] or f"{len(bgs)} backgrounds clean")
    chk("every pinned card carries data-pin=1 on card+row+tile (AC-B3/C2/C3)", page_html.count('data-pin="1"') == 3 * len(pinned), f"{page_html.count('data-pin=' + chr(34) + '1' + chr(34))} rendered vs 3×{len(pinned)} pinned")
    # Change C (AC-C1–C4): the overviews, the view bar and the peek shell render; counts line up.
    # ⚠️ This selftest renders the NON-BLOCKED live rows only (its own fixture choice); the real build
    # passes every row, blocked included — the counts below compare against the list actually rendered.
    chk("view bar + presets render (AC-C1/C5)", all(x in page_html for x in ('class="viewbar"', 'data-view="table"', 'data-view="board"', 'data-preset="today"', 'data-preset="waiting"')))
    chk("table rows == rendered rows (AC-C2; selftest renders non-blocked)", page_html.count('class="ovrow"') == len(live), f"{page_html.count('class=' + chr(34) + 'ovrow' + chr(34))} vs {len(live)}")
    chk("grid tiles == rendered rows (AC-C3; same basis)", page_html.count('class="ovtile"') == len(live), f"{page_html.count('class=' + chr(34) + 'ovtile' + chr(34))} vs {len(live)}")
    chk("peek shell + listwrap render (AC-C4)", all(x in page_html for x in ('id="peek"', 'id="peekbody"', 'id="pk-prev"', 'id="listwrap"')))
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
    from zoneinfo import ZoneInfo as _ZI
    today = dt.date.fromisoformat(a.today) if a.today else dt.datetime.now(_ZI("America/New_York")).date()
    try:
        r = build(today, Path(a.out), reference_out=Path(a.reference_out) if a.reference_out else None,
                  owed_url=a.owed_url, reference_url=a.reference_url)
    except ValueError as error:
        ap.error(str(error))
    print(json.dumps(r, indent=1))
