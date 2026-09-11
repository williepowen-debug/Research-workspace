#!/usr/bin/env python3
"""willq_view.py — the GENERATED 'Pending Will' block (WQ-185 ②, Will 2026-09-06 10:12; DOCKET L296).

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

rc: 0 ok · 1 drift (--check) · 2 refused (markers / unparseable / zero rows) — never pads, never guesses.
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

def parse_open(text):
    """OPEN-table rows → [{n, due, due_txt, blocked, kind}] — the gate/brief parser rules, duplicated."""
    if "## OPEN" not in text:
        raise WillqError("no '## OPEN' section")
    section = text.split("## OPEN", 1)[-1].split("\n## ", 1)[0]
    rows = []
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        c = [x.strip() for x in line.strip("|").split("|")]
        if len(c) < 6 or not re.match(r"\d", c[0]):
            continue
        lead = re.sub(r"^(?:~~[^~]+~~\s*)+", "", c[1])
        lead = re.sub(r"^[\*\s]+", "", lead)
        if re.match(r"✅|DONE\b|RESOLVED\b|TERMINAL\b|DECLINED\b|CLOSED\b", lead):
            continue  # closed-in-place rows are not open asks (gate's MISFILED rule)
        raw = re.sub(r"\*\*|`", "", c[3]).strip()
        d = re.search(r"\d{4}-\d{2}-\d{2}", raw)
        blocked = bool(BLOCKED_RE.match(c[6] if len(c) > 6 else ""))
        rows.append({"n": c[0], "due": d.group(0) if d else None,
                     "due_txt": raw, "blocked": blocked,
                     "kind": re.sub(r"\*\*|`", "", c[2]).strip().upper()})
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
