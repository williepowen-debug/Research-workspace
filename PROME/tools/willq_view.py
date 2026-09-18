#!/usr/bin/env python3
r"""willq_view.py — the GENERATED 'Pending Will' block (WQ-185 ②, Will 2026-09-06 10:12; DOCKET L296).

Source of truth: PROME/WILL_QUEUE.md § OPEN (its own rule 4: the ONLY live copy). This tool renders a
one-line projection of that table into PROME/SCRATCH.md between markers, replacing the hand-maintained
`- **Pending Will:** …` bullet that rotted at every ruling. docket_view.py shape (2026-09-03).

  --write FILE      render into FILE's marked block; on FIRST run replaces the single hand line
                    `- **Pending Will:** …` with the block (the hand copy must DISAPPEAR — Codex 9/6)
  --check FILE      re-render (at the block's own as-of) and diff against FILE's block; rc 1 on drift or
                    on a surviving hand copy outside the markers; never writes
  --dry-run         with --write: print the block, touch nothing
  --queue PATH      WILL_QUEUE.md path (default PROME/WILL_QUEUE.md; fixtures for tests)
  --as-of YYYY-MM-DD
  --selftest        fixture drills: first-run replace · idempotence · needed-by change shows in the
                    block (the acceptance test) · check flags drift · marker-count refusal · zero-row refusal

rc: 0 ok · 1 drift (--check) · 2 refused (markers / unparseable / zero rows / a shifted row / a non-ISO
needed-by) — never pads, never guesses.
2026-09-18 (scratchrot7cold ❌1/❌2, WQ-229 repair): cells split on UNESCAPED pipes only — a `\|` inside a cell
(markdown's literal pipe) is never a column break; a row whose cell count differs from the header's is REFUSED
by name (an unescaped `|` in a cell shifts every column: WQ-263 and WQ-157 rendered as undated `(RULE)` while the
queue dated both 2026-09-19); a needed-by that looks like a date but is not ISO (`9/19`) is REFUSED by name
instead of rendering undated and sorting last under a "dated first" banner (WQ-241/242). Fail closed: a block
the reader cannot trust is never written. The same split is applied at prome_gate.py (3 sites) and
will_brief.py — queue_parser_selftest.py keeps them agreeing.
Parser rules are a deliberate copy of will_brief.parse_actions() / prome_gate.check_will_queue() (no
import coupling — the gate is a blocking boot surface); queue_parser_selftest.py keeps the parsers agreeing.
"""
import argparse, datetime as dt, os, re, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip() or ".")
BEGIN, END = "<!-- WILLQ-VIEW BEGIN -->", "<!-- WILLQ-VIEW END -->"
HAND = re.compile(r"^- \*\*Pending Will:\*\*.*$", re.M)
TOOL = "PROME/tools/willq_view.py"


class WillqError(Exception):
    pass


# Blocked keys on the DOCUMENTED declaration in the NOTES cell only — WILL_QUEUE Rules block: blocked rows carry
# "⛔ waits: <who>" at the START of Notes. 2026-09-10 (WQ-221): a whole-LINE search for "⛔ wait" matched the
# ITEM prose of the row proposing the aged-waits rule ("a ⛔ waits row whose …") and filed it under "waiting on
# others" with no tap controls — Will could not rule it. Prose mentioning a marker is not the marker.
BLOCKED_RE = re.compile(r"^[\*\s]*⛔\s*waits?\b")

# ---- ONE split + ONE date classifier for the WILL_QUEUE table (2026-09-18, ACCEPTANCE_queue_parsers B1/B3/B4) ----
# Copied verbatim into willq_view.py · prome_gate.py · will_brief.py · decision_deck.py (the gate is a blocking boot
# surface: no import coupling by design); queue_parser_selftest.py asserts the four copies and table_check agree.
_ESCAPED_PIPE = "\x00"


def split_cells(line):
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
                       r"|\b\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\b", re.I)  # 19 Sep


def datelike_not_iso(raw):
    """B3: a needed-by with NO ISO date but a date-LIKE token. B4 (textual / empty) is its complement."""
    t = re.sub(r"\*\*|`", "", raw or "")
    return not _ISO_DATE.search(t) and bool(_DATELIKE.search(t))


def is_separator(cells):
    return bool(cells) and all(re.fullmatch(r":?-+:?", c) for c in cells)

def parse_open(text):
    """OPEN-table rows → [{n, due, due_txt, blocked, kind}] — the gate/brief parser rules, duplicated."""
    if "## OPEN" not in text:
        raise WillqError("no '## OPEN' section")
    section = text.split("## OPEN", 1)[-1].split("\n## ", 1)[0]
    rows, problems, hdr = [], [], None
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        c = split_cells(line)
        if is_separator(c):
            continue
        if hdr is None:
            hdr = len(c)                              # B2: the FIRST table row is the header, whatever its first cell says
            continue
        if len(c) != hdr:                             # B2: tested BEFORE any minimum-width skip, both directions
            name = c[0] if re.match(r"\d", c[0]) else (c[0][:24] or "<blank>")
            problems.append(f"SHIFTED WQ-{name}: {len(c)} cells vs header {hdr} — an unescaped `|` inside a cell shifts every column; write it `\\|`")
            continue
        if not re.match(r"\d", c[0]):
            continue
        lead = re.sub(r"^(?:~~[^~]+~~\s*)+", "", c[1])
        lead = re.sub(r"^[\*\s]+", "", lead)
        if re.match(r"✅|DONE\b|RESOLVED\b|TERMINAL\b|DECLINED\b|CLOSED\b", lead):
            continue  # closed-in-place rows are not open asks (gate's MISFILED rule)
        raw = re.sub(r"\*\*|`", "", c[3]).strip()
        d = re.search(r"\d{4}-\d{2}-\d{2}", raw)
        if not d and datelike_not_iso(raw):           # B3; B4 (textual/empty) falls through with due=None
            problems.append(f"NOT-ISO WQ-{c[0]}: needed-by '{raw[:24]}' is not ISO (WILL_QUEUE rule: hard dates are YYYY-MM-DD) — it would render undated and sort last")
            continue
        blocked = bool(BLOCKED_RE.match(c[6] if len(c) > 6 else ""))
        rows.append({"n": c[0], "due": d.group(0) if d else None,
                     "due_txt": raw, "blocked": blocked,
                     "kind": re.sub(r"\*\*|`", "", c[2]).strip().upper()})
    if hdr is None:
        raise WillqError("no table header row in § OPEN — refusing to guess the columns")
    if problems:
        raise WillqError("; ".join(problems))
    if not rows:
        raise WillqError("OPEN table parsed to zero rows — refusing to write an empty block")
    rows.sort(key=lambda r: (r["blocked"], r["due"] or "9999-99-99", -int(re.match(r"\d+", r["n"]).group(0))))
    return rows


def _due_short(r):
    if r["due"]:
        y, m, d = r["due"].split("-")
        return f"{int(m)}/{int(d)}"
    t = r["due_txt"] or "—"
    t = t.split("(")[0].strip(" —·") or "—"
    return (t[:14] + "…") if len(t) > 15 else t


def render(rows, as_of):
    n_open = len(rows); n_blk = sum(1 for r in rows if r["blocked"])
    items = []
    for r in rows:
        cell = f"WQ-{r['n']} ({_due_short(r)})"
        items.append(("⛔ " + cell) if r["blocked"] else cell)
    line = (f"- **Pending Will (GENERATED from `PROME/WILL_QUEUE.md` § OPEN by `{TOOL}` · as-of {as_of.isoformat()} · "
            f"{n_open} open, {n_blk} blocked — dated first, blocked last; never hand-edit inside the markers):** "
            + " · ".join(items))
    return "\n".join([BEGIN, line, END])


def _block_span(text):
    b, e = text.count(BEGIN), text.count(END)
    if (b, e) == (0, 0):
        return None
    if (b, e) != (1, 1):
        raise WillqError(f"marker count BEGIN={b} END={e} — need exactly one of each; refusing to guess an anchor")
    i, j = text.index(BEGIN), text.index(END) + len(END)
    if j < i:
        raise WillqError("END marker precedes BEGIN marker")
    return i, j


def _as_of_in(block):
    m = re.search(r"as-of (\d{4}-\d{2}-\d{2})", block)
    return dt.date.fromisoformat(m.group(1)) if m else None


def do_write(prose_path, queue_path, as_of, dry_run):
    rows = parse_open(Path(queue_path).read_text(encoding="utf-8"))
    block = render(rows, as_of)
    text = Path(prose_path).read_text(encoding="utf-8")
    span = _block_span(text)
    if span is None:
        hands = HAND.findall(text)
        if len(hands) != 1:
            raise WillqError(f"first run needs exactly ONE hand line '- **Pending Will:** …' to replace; found {len(hands)}")
        new = HAND.sub(lambda m: block, text, count=1)
        mode = "first-run (hand line replaced)"
    else:
        i, j = span
        new = text[:i] + block + text[j:]
        mode = "re-render"
    if HAND.search(new.replace(block, "")):
        raise WillqError("a hand copy '- **Pending Will:** …' survives outside the markers — delete it, do not keep two")
    if dry_run:
        print(block); print(f"WILLQ-VIEW (dry-run) {mode}; {len(block.encode())} B; nothing written"); return 0
    if new == text:
        print(f"WILLQ-VIEW ✓ unchanged — block byte-identical ({len(block.encode())} B) in {prose_path}"); return 0
    Path(prose_path).write_text(new, encoding="utf-8")
    print(f"WILLQ-VIEW ✓ wrote {len(block.encode())} B block into {prose_path} ({mode}; file {len(text.encode())} → {len(new.encode())} B)")
    return 0


def do_check(prose_path, queue_path):
    text = Path(prose_path).read_text(encoding="utf-8")
    span = _block_span(text)
    if span is None:
        print(f"WILLQ-VIEW ✗ no marker block in {prose_path} — run --write first"); return 2
    i, j = span; have = text[i:j]
    if HAND.search(text[:i] + text[j:]):
        print(f"WILLQ-VIEW ✗ hand copy '- **Pending Will:** …' survives outside the markers in {prose_path}"); return 1
    as_of = _as_of_in(have) or dt.date.today()
    want = render(parse_open(Path(queue_path).read_text(encoding="utf-8")), as_of)
    if have == want:
        print(f"WILLQ-VIEW ✓ {prose_path} block agrees with {queue_path} § OPEN ({len(have.encode())} B, as-of {as_of})"); return 0
    hv = set(re.findall(r"WQ-\d+ \([^)]*\)", have)); wv = set(re.findall(r"WQ-\d+ \([^)]*\)", want))
    print(f"WILLQ-VIEW ✗ DRIFT in {prose_path}: block says {sorted(hv - wv) or '—'}; queue says {sorted(wv - hv) or '—'} — "
          f"regenerate with `python3 {TOOL} --write {prose_path}`; never edit inside the markers")
    return 1


FIX_Q = """# fixture
## OPEN
| # | Item | Type | Needed by | Since | PROME rec | Notes |
|---|---|---|---|---|---|---|
| 12 | **Dated item** | RULE | 2026-09-12 (before x) | 9/6 | rec | note |
| 8 | **Rule about a ⛔ waits row whose blocker is dark** | RULE | 2026-09-11 | 9/6 | rec | note |
| 11 | **Undated item** | READ | on delivery | 9/5 | rec | note |
| 10 | **Blocked item** | RULE | 2026-09-10 | 9/4 | rec | ⛔ waits: DAEDALUS |
| 9 | ✅ **Closed in place** | RULE | 2026-09-01 | 9/1 | rec | done |
## RECENTLY DONE
"""
FIX_S = "# scratch\n## Operator Card\n- **Now:** x\n- **Pending Will:** WQ-12 (9/12) · WQ-11\n- **Peers:** none\n"


def selftest():
    n = 0; fails = []
    def ok(cond, name):
        nonlocal n; n += 1
        if not cond: fails.append(name)
    with tempfile.TemporaryDirectory() as td:
        q = Path(td, "Q.md"); s = Path(td, "S.md"); q.write_text(FIX_Q); s.write_text(FIX_S)
        as_of = dt.date(2026, 9, 6)
        rows = parse_open(q.read_text())
        ok([r["n"] for r in rows] == ["8", "12", "11", "10"], "parse+sort")
        ok(any(r["n"] == "8" and not r["blocked"] for r in rows), "prose-mention of the wait marker is NOT blocked (WQ-221)")
        ok([r["n"] for r in rows][-1] == "10", "blocked sorts last")
        ok(all(r["n"] != "9" for r in rows), "closed-in-place row excluded")
        do_write(str(s), str(q), as_of, False); t1 = s.read_text()
        ok(BEGIN in t1 and END in t1 and "WQ-12 (9/12)" in t1 and "⛔ WQ-10 (9/10)" in t1 and "WQ-8 (9/11)" in t1 and "⛔ WQ-8" not in t1, "first-run write")
        ok(not HAND.search(t1.replace(t1[t1.index(BEGIN):t1.index(END) + len(END)], "")), "hand copy gone")
        ok(do_check(str(s), str(q)) == 0, "check clean after write")
        do_write(str(s), str(q), as_of, False); ok(s.read_text() == t1, "idempotent")
        q.write_text(FIX_Q.replace("2026-09-12 (before x)", "2026-09-14 (moved)"))
        ok(do_check(str(s), str(q)) == 1, "check flags drift after a needed-by change")
        do_write(str(s), str(q), as_of, False); t2 = s.read_text()
        ok("WQ-12 (9/14)" in t2 and "WQ-12 (9/12)" not in t2, "ACCEPTANCE: changed needed-by shows in the block")
        s.write_text(t2 + "\n- **Pending Will:** stale hand copy\n")
        ok(do_check(str(s), str(q)) == 1, "check flags a surviving hand copy")
        s.write_text(t2 + "\n" + BEGIN + "\n")
        try:
            do_write(str(s), str(q), as_of, False); ok(False, "marker-count refusal")
        except WillqError:
            ok(True, "marker-count refusal")
        q.write_text("# fixture\n## OPEN\n| # | Item | Type | Needed by | Since | rec | Notes |\n|---|---|---|---|---|---|---|\n## RECENTLY DONE\n")
        try:
            parse_open(q.read_text()); ok(False, "zero-row refusal")
        except WillqError:
            ok(True, "zero-row refusal")
        # 2026-09-18 — scratchrot7cold ❌1/❌2 and their neighbours (WQ-229: ordinary rows = the fixture above)
        def rows_of(extra):
            return parse_open(FIX_Q.replace("## RECENTLY DONE", extra + "\n## RECENTLY DONE"))
        r = rows_of("| 13 | **Math `P(leg \\| fired)` in the body** | RULE | 2026-09-19 (sitting) | 9/6 | rec | note |")
        ok(any(x["n"] == "13" and x["due"] == "2026-09-19" for x in r), "escaped pipe keeps the column and the date (r5 ❌1)")
        for extra, want, name in [
            ("| 14 | **Math P(leg | fired) unescaped** | RULE | 2026-09-19 | 9/6 | rec | note |", "WQ-14", "unescaped pipe REFUSED by row (r5 ❌1)"),
            ("| 15 | **Short date** | RULE | 9/19 | 9/6 | rec | note |", "WQ-15", "short-form needed-by REFUSED by row (r5 ❌2)"),
            ("| 16 | **Overlap `a \\| b`** | RULE | 9/19 (sitting) | 9/6 | rec | note |", "not ISO", "OVERLAP neighbour: escaped pipe AND short date — refused on the date, columns intact"),
        ]:
            try:
                rows_of(extra); ok(False, name)
            except WillqError as e:
                ok(want in str(e), name)
        r = rows_of("| 17 | **Textual date** | RULE | at HEN-46's resolution, or later | 9/6 | rec | note |\n| 18 | **Empty date** | RULE |  | 9/6 | rec | note |")
        ok(any(x["n"] == "17" and x["due"] is None for x in r) and any(x["n"] == "18" and x["due"] is None for x in r), "MISSING-INFORMATION neighbour: textual / empty needed-by stay allowed")
        # 2026-09-18 SECOND repair (parserfixcold A2/A3/A4 ❌) — ACCEPTANCE_queue_parsers B2/B3/B4/B7, the reader's own counterexamples
        for extra, want, name in [
            ("| 19 | **mdy** | RULE | 9/19/26 | 9/6 | rec | note |", "NOT-ISO WQ-19", "B3 m/d/yy refused by name"),
            ("| 20 | **unpadded** | RULE | 2026-9-19 | 9/6 | rec | note |", "NOT-ISO WQ-20", "B3 unpadded ISO refused by name"),
            ("| 21 | **month name** | RULE | Sept 19 | 9/6 | rec | note |", "NOT-ISO WQ-21", "B3 month-name day refused by name"),
            ("| 23 | **five cells** | RULE | 2026-09-19 | 9/6 |", "SHIFTED WQ-23", "B2 FEWER cells than the header refused by name (the first repair dropped it silently)"),
            ("| 26 | **nine cells** | RULE | 2026-09-19 | 9/6 | rec | a | b | c |", "SHIFTED WQ-26", "B2 MORE cells than the header refused by name"),
        ]:
            try:
                rows_of(extra); ok(False, name)
            except WillqError as e:
                ok(want in str(e), name)
        r = rows_of("| 22 | **fraction** | RULE | when 2/3 of the legs have filled | 9/6 | rec | note |\n| 24 | **empty notes** | RULE | 2026-09-19 | 9/6 | rec||")
        ok(any(x["n"] == "22" and x["due"] is None for x in r), "B4 a fraction followed by 'of' is textual — allowed, no alarm")
        ok(any(x["n"] == "24" and x["due"] == "2026-09-19" for x in r), "B1 trailing `||` = an EMPTY last cell (7 cells) — allowed")
        q_id = FIX_Q.replace("| # | Item |", "| ID | Item |").replace("## RECENTLY DONE", "| 25 | **shifted under an ID header** | RULE | 2026-09-19 | 9/6 | rec | a | b |\n## RECENTLY DONE")
        try:
            parse_open(q_id); ok(False, "B2 a header spelled `| ID |` still arms the count check")
        except WillqError as e:
            ok("SHIFTED WQ-25" in str(e), "B2 a header spelled `| ID |` still arms the count check")
        try:
            parse_open("# f\n## OPEN\nno table here\n## RECENTLY DONE\n"); ok(False, "MISSING-INFORMATION: no header row refused")
        except WillqError as e:
            ok("header" in str(e), "MISSING-INFORMATION: no header row refused")
    print(f"willq_view selftest: {n - len(fails)}/{n} PASS" + (f" — FAIL: {fails}" if fails else ""))
    return 0 if not fails else 2


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", metavar="FILE"); ap.add_argument("--check", metavar="FILE")
    ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--queue", default=str(ROOT / "PROME/WILL_QUEUE.md"))
    ap.add_argument("--as-of"); ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    as_of = dt.date.fromisoformat(a.as_of) if a.as_of else dt.date.today()
    try:
        if a.write:
            return do_write(a.write, a.queue, as_of, a.dry_run)
        if a.check:
            return do_check(a.check, a.queue)
    except WillqError as e:
        print(f"WILLQ-VIEW ✗ refused: {e}"); return 2
    ap.print_help(); return 2


if __name__ == "__main__":
    sys.exit(main())
