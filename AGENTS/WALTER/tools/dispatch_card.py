#!/usr/bin/env python3
"""WALTER card dispatcher: one maintained script for step 11 (BOARD card, create-only handoffs, route_log and
delivery_log rows). Replaces the per-session scratchpad dispatchers (LAST_COMPLETION FOLLOW-UP 5; Will
2026-11-16 19:21 ET: consolidate, cover the demonstrated failures, preserve routing rules).

Usage (from the repository root):
    python3 AGENTS/WALTER/tools/dispatch_card.py CARDS.json [--out DISPATCHED.json] [--check]
CARDS.json is a list of card objects (keys below). Write the JSON with a QUOTED heredoc or the Write tool.
--check validates every card and writes nothing. Then run gen_board_index.py --write BOARD/INDEX.md --cutover.

Card keys: id, slug, title, body, source, origin, action, info, precedence, signal_type, confidence,
confidence_language, cluster, domain, entities, dispatch_note, route_origin, route_summary;
optional safety_net, event_window, extra_fm {key: value}.

Refusals (nothing is written for ANY card in the batch if one card is refused):
  * empty body, or a body with no line other than headings (11/13: handoffs shipped header-only)
  * text that looks shell-damaged: a figure that lost its leading digits after `$` (".8B", " .5 billion")
    or an expanded shell path ("/bin/bash") (11/09: an unquoted heredoc turned "$8B" into "B")
  * a recipient never eligible for signals: CATO (PROME/ROSTER.md, WQ-255, Will 2026-09-26: "without
    automatic launch or signal-routing eligibility"; SIG-W-20261019-012 routed it anyway)
  * TERRY on the INFO line (TERRY is BOARD-only; Rule 10)
  * a recipient with no AGENTS/<NAME>/ directory, a duplicate recipient, or an existing card/handoff path
  * a weekday written beside a date that is not that date's weekday, in title, body, route_summary, source
    or dispatch_note (PROME packet 2026-11-17 20:42 ET on Will's word, WQ-713; test case SIG-W-20261117-014
    "Thu Nov 13", a Friday). The test is the fleet's scripts/claim_check.py weekday check; a bare M/D takes
    the card id's year. The checker guesses years and can be wrong: override with the card key
    "weekday_override": "<stated reason, 10+ characters>", which is printed and written to the front matter.
After writing, every handoff's body is re-read and must equal the BOARD card's body.

Routing rules preserved (CLAUDE.md Rule 10, BOARD_CONSUMPTION_SPEC v0.37):
  * CARL, RED: handoff and delivery row only on ACTION; INFO by BOARD
  * TERRY: BOARD-only, no handoff or row
  * PROME: INFO by BOARD; on ACTION (a registered owner row routes to PROME, e.g. HENRY's put-wall row)
    a create-only packet in PROME/inbox/ plus a delivery row noting board_scan rc 1 is expected
"""
import argparse
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PULL_INFO_ONLY = {"CARL", "RED"}
BOARD_ONLY = {"TERRY"}
NEVER_ROUTE = {"CATO": "PROME/ROSTER.md CATO row (WQ-255, Will 2026-09-26): no signal-routing eligibility"}
REQUIRED = ["id", "slug", "title", "body", "source", "origin", "action", "info", "precedence", "signal_type",
            "confidence", "confidence_language", "cluster", "domain", "entities", "dispatch_note",
            "route_origin", "route_summary"]
DAMAGE = [
    (re.compile(r"(?<![\w$.,])\.\d+\s*(?:B|M|K|T|bn|mn|billion|million|trillion)\b"),
     "a figure that starts with '.' (a shell may have eaten '$<digit>')"),
    (re.compile(r"/bin/(?:ba)?sh\b"), "an expanded shell path ('$0' becomes /bin/bash)"),
]
NOTE = "walter Claude Code; create-only; no recipient state edits. Delivered != consumed."
WEEKDAY_FIELDS = ("title", "body", "route_summary", "source", "dispatch_note")


def _claim_check():
    import importlib.util
    spec = importlib.util.spec_from_file_location("claim_check", ROOT / "scripts" / "claim_check.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def weekday_problems(card):
    """Weekday-beside-date mismatches across the card's text fields, via the fleet checker."""
    cc, year = _claim_check(), int(card["id"][6:10])
    out = []
    for field in WEEKDAY_FIELDS:
        for n, line in enumerate(str(card.get(field, "")).splitlines(), 1):
            out += [f"{field} line {n}: {f[3]}" for f in cc.weekday_flags(field, n, line, year)]
    return out


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def q(v):
    return json.dumps(v, ensure_ascii=False)


def body_lines(body):
    return [ln for ln in body.strip().splitlines() if ln.strip() and not ln.lstrip().startswith("#")]


def plan(card, root, runtime):
    """(errors, plan dict). No file is touched."""
    errs = [f"missing key {k}" for k in REQUIRED if k not in card]
    if errs:
        return errs, None
    sid, body = card["id"], card["body"]
    if not re.fullmatch(r"SIG-W-\d{8}-\d{3}", sid):
        errs.append(f"id {sid!r} is not SIG-W-YYYYMMDD-NNN")
    if not body_lines(body):
        errs.append("body is empty or has headings only")
    for field in ("title", "body", "route_summary"):
        for rx, why in DAMAGE:
            m = rx.search(str(card[field]))
            if m:
                errs.append(f"{field} has {why}: {m.group(0)!r}")
    if re.fullmatch(r"SIG-W-\d{8}-\d{3}", sid):
        wk = weekday_problems(card)
        override = str(card.get("weekday_override", "")).strip()
        if wk and len(override) >= 10:
            for w in wk:
                print(f"WEEKDAY OVERRIDDEN {sid}: {w} (reason: {override})")
        elif wk:
            errs += [f"weekday mismatch, {w} (fix it, or set weekday_override with a stated reason)" for w in wk]
    recips = [(r, "ACTION") for r in card["action"]] + [(r, "INFO") for r in card["info"]]
    names = [r for r, _ in recips]
    for r in sorted({n for n in names if names.count(n) > 1}):
        errs.append(f"{r} appears more than once on action/info")
    for r, role in recips:
        if r in NEVER_ROUTE:
            errs.append(f"{r} on {role}: never routed ({NEVER_ROUTE[r]})")
        if r == "TERRY" and role == "INFO":
            errs.append("TERRY never on INFO (BOARD-only)")
        if r != "PROME" and not (root / "AGENTS" / r).is_dir():
            errs.append(f"no AGENTS/{r}/ directory")
    slug = re.sub(r"[^A-Za-z0-9.]+", "-", card["slug"]).strip("-")
    board_rel = f"BOARD/{sid}-{slug}.md"
    if list((root / "BOARD").glob(f"{sid}-*.md")):
        errs.append(f"a BOARD card for {sid} already exists")
    handoffs = []
    for r, role in recips:
        if r in BOARD_ONLY or (r in PULL_INFO_ONLY and role == "INFO") or (r == "PROME" and role == "INFO"):
            continue
        if r == "PROME":
            rel = f"PROME/inbox/{sid[6:10]}-{sid[10:12]}-{sid[12:14]}_from-WALTER_{sid}.md"
            note = NOTE + " PROME on action by a registered owner row; board_scan rc 1 expected."
        else:
            rel = f"AGENTS/{r}/inbox/WALTER/{sid}.md"
            note = NOTE
        if (root / rel).exists():
            errs.append(f"handoff exists: {rel}")
        handoffs.append((r, role, rel, f"{runtime}; {note}"))
    return errs, dict(card=card, board_rel=board_rel, handoffs=handoffs)


def write(p, root):
    c, ts = p["card"], now()
    body = c["body"].strip()
    fm = ["---", f"signal_id: {q(c['id'])}", f"date: {q(ts[:10])}", f"timestamp: {q(ts)}", f"dispatched: {q(ts)}",
          f"source: {q(c['source'])}", f"origin: {q(c['origin'])}", f"action: {q(c['action'])}",
          f"info: {q(c['info'])}", f"precedence: {q(c['precedence'])}", f"signal_type: {q(c['signal_type'])}",
          f"confidence: {c['confidence']}", f"confidence_language: {q(c['confidence_language'])}",
          "resources: 1", f"safety_net: {q(c.get('safety_net', 'clear'))}", f"cluster: {q(c['cluster'])}",
          f"domain: {q(c['domain'])}", f"entities: {q(c['entities'])}", f"word_count: {len(body.split())}",
          f"dispatch_note: {q(c['dispatch_note'])}", f"event_window: {q(c.get('event_window', 'open'))}"]
    fm += [f"{k}: {q(v)}" for k, v in c.get("extra_fm", {}).items()]
    if str(c.get("weekday_override", "")).strip():
        fm.append(f"weekday_override: {q(str(c['weekday_override']).strip())}")
    fm.append("---")
    (root / p["board_rel"]).write_text("\n".join(fm) + f"\n# {c['title']}\n\n{body}\n", encoding="utf-8")
    rows = []
    for r, role, rel, note in p["handoffs"]:
        hp = root / rel
        hp.parent.mkdir(parents=True, exist_ok=True)
        hp.write_text(f"# {c['id']} — {c['title']}\nBOARD: /{p['board_rel']}\nPriority: {c['precedence']}\n"
                      f"Role: {role}\nFrom: WALTER\nDate: {ts[:10]}\n\n{body}\n", encoding="utf-8")
        rows.append("\t".join([ts, c["id"], r, role, "CLAUDE_CODE", c["precedence"], rel,
                               "written_not_delivered_pending_push", note]))
    route = "\t".join([ts, c["id"], c["route_origin"], c["route_summary"], c["precedence"],
                       ",".join(c["action"]), ",".join(c["info"]), str(c["confidence"])])
    routed = root / "AGENTS" / "WALTER" / "routed"
    with open(routed / "route_log.tsv", "a", encoding="utf-8") as f:
        f.write(route + "\n")
    if rows:
        with open(routed / "delivery_log.tsv", "a", encoding="utf-8") as f:
            f.write("\n".join(rows) + "\n")
    # post-write verification: every handoff carries the card's body verbatim (11/13 header-only failure)
    board_text = (root / p["board_rel"]).read_text(encoding="utf-8")
    board_body = board_text.split("\n---\n", 1)[1].split("\n\n", 1)[1]
    for _, _, rel, _ in p["handoffs"]:
        hb = (root / rel).read_text(encoding="utf-8").split("\n\n", 1)[1]
        if hb != board_body:
            raise RuntimeError(f"handoff body differs from the BOARD card: {rel}")
    return ts, [h[2] for h in p["handoffs"]]


def main(argv=None):
    ap = argparse.ArgumentParser(description="WALTER card dispatcher (step 11)")
    ap.add_argument("cards")
    ap.add_argument("--out")
    ap.add_argument("--check", action="store_true", help="validate only; write nothing")
    ap.add_argument("--root", default=str(ROOT), help=argparse.SUPPRESS)
    ap.add_argument("--runtime", default="walter Claude Code", help="runtime attribution for delivery notes")
    a = ap.parse_args(argv)
    root = Path(a.root)
    cards = json.loads(Path(a.cards).read_text(encoding="utf-8"))
    if isinstance(cards, dict):
        cards = [cards]
    plans, errors = [], []
    ids = [c.get("id") for c in cards]
    for d in sorted({i for i in ids if ids.count(i) > 1}):
        errors.append(f"{d}: id repeated in this batch")
    for c in cards:
        e, p = plan(c, root, a.runtime)
        errors += [f"{c.get('id', '?')}: {x}" for x in e]
        plans.append(p)
    if errors:
        print("REFUSED, nothing written:")
        for e in errors:
            print("  " + e)
        return 2
    if a.check:
        for p in plans:
            print(f"OK {p['card']['id']}  {p['board_rel']}  handoffs: {len(p['handoffs'])}")
        return 0
    out = []
    for p in plans:
        ts, hs = write(p, root)
        print(f"{p['card']['id']} {ts} {p['board_rel']} handoffs: {len(hs)}")
        out.append([p["board_rel"], hs])
    if a.out:
        Path(a.out).write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print("Next: python3 AGENTS/WALTER/tools/gen_board_index.py --write BOARD/INDEX.md --cutover")
    return 0


if __name__ == "__main__":
    sys.exit(main())
