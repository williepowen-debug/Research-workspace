#!/usr/bin/env python3
"""docket_owed.py — the DOCKET → DAEDALUS hop check (built 2026-10-01, Will "ok approved go ahead").

WHY: four DOCKET rows assigned to DAEDALUS on 9/28–9/29 (L526 · L538 · L546 · L548) never reached
STATUS.md, because nothing at DAEDALUS boot read the DOCKET for rows naming it (the registrar wrote,
no reader was registered — PAT-108's shape one hop over). This check is that reader.

WHAT: every OPEN DOCKET row whose OWNER cell names DAEDALUS, dated within the horizon (default 30d
ahead, past-due always) or session-keyed (non-date span), is checked for a citation `L<n>` in
AGENTS/DAEDALUS/STATUS.md. An uncited row is printed in full-enough form to act on.
  · "open" = `docket_view.state_kind(...) == "PENDING"` — the fleet's one definition, imported,
    never re-derived here (a DECLINED-prefixed state is TERMINAL there, and so here).
  · a row whose DAEDALUS owner segment says "informed" is listed separately and does NOT gate.

rc (CHECK_STANDARD §9):  0 CLEAN  every gating row cited
                         1 DUE    ≥1 gating row uncited (owed: triage it onto the board)
                         2 UNKNOWN DOCKET unreadable/ragged, STATUS unreadable, or the population
                                   is empty (zero rows naming DAEDALUS in ANY state = the owner
                                   column changed shape, not "nothing owed" — PAT-155)
USAGE
  python3 AGENTS/DAEDALUS/scripts/docket_owed.py [--horizon 30] [--as-of YYYY-MM-DD]
          [--docket PATH] [--status PATH]
  python3 AGENTS/DAEDALUS/scripts/docket_owed.py --selftest
PROVES: a cited row number exists in STATUS text. Does NOT prove the row is understood, scheduled
sensibly, or done — a citation is acknowledgement, never completion.
"""
import argparse
import datetime as dt
import os
import re
import subprocess
import sys
import tempfile
from zoneinfo import ZoneInfo

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                      text=True, cwd=os.path.dirname(os.path.abspath(__file__))).stdout.strip()
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import docket_view  # noqa: E402  the fleet's DOCKET parser + open-state definition

AGENT = "DAEDALUS"
STATUS_DEFAULT = os.path.join(ROOT, "AGENTS", AGENT, "STATUS.md")
NAME_RE = re.compile(r"\b%s\b" % AGENT)


def owner_segment(owners):
    """The ' / '-separated owner segment that names the agent (first one), or ''."""
    for seg in re.split(r"\s+/\s+", owners):
        if NAME_RE.search(seg):
            return seg
    return ""


def cited(n, status_text):
    return re.search(r"(?<![\w])L%d(?!\d)" % n, status_text) is not None


def assess(docket_path, status_path, as_of, horizon):
    """Returns (rc, lines)."""
    try:
        rows = docket_view.load_docket(docket_path)
    except (docket_view.DocketError, OSError) as e:
        return 2, [f"DOCKET-OWED UNKNOWN: cannot read DOCKET ({e})"]
    try:
        status = open(status_path, encoding="utf-8").read()
    except OSError as e:
        return 2, [f"DOCKET-OWED UNKNOWN: cannot read STATUS ({e})"]
    named = [r for r in rows if NAME_RE.search(r["owners"])]
    if not named:
        return 2, [f"DOCKET-OWED UNKNOWN: {len(rows)} DOCKET rows parsed, ZERO name {AGENT} in the owner "
                   f"cell in any state — the owner column changed shape; an empty population proves nothing"]
    limit = as_of + dt.timedelta(days=horizon)
    gating, informed, cited_rows, beyond = [], [], [], 0
    for r in named:
        if docket_view.state_kind(r["state"]) != "PENDING":
            continue
        if r["start"] is not None and r["start"] > limit:
            beyond += 1
            continue
        if cited(r["line"], status):
            cited_rows.append(r)
        elif "informed" in owner_segment(r["owners"]).lower():
            informed.append(r)
        else:
            gating.append(r)
    head = (f"DOCKET-OWED [{AGENT}] as-of {as_of} · horizon +{horizon}d · {len(rows)} rows parsed · "
            f"{len(named)} name {AGENT} (any state) · open in window: {len(cited_rows) + len(gating) + len(informed)} "
            f"= {len(cited_rows)} cited + {len(gating)} UNCITED + {len(informed)} informed-only · {beyond} open beyond horizon")
    out = [("⏰ " if gating else "") + head]

    def show(r):
        when = r["span"] if r["start"] is None else (
            r["span"] + (" (PAST)" if (r["end"] or r["start"]) < as_of else ""))
        return (f"  ⏰ L{r['line']} · {when} · role: {owner_segment(r['owners'])[:90]} · "
                f"{r['catalyst'][:110]}")
    if gating:
        out.append(f"⏰ UNCITED in STATUS.md — put each on the board (act · date · or say why not):")
        out += [show(r) for r in sorted(gating, key=lambda r: r["line"])]
    if informed:
        out.append("ℹ️  informed-only (does not gate): " + " · ".join(f"L{r['line']}" for r in informed))
    out.append(f"DOCKET-OWED-RESULT rc={1 if gating else 0} uncited={len(gating)} cited={len(cited_rows)} "
               f"informed={len(informed)}" + ("" if gating else " — CLEAN: every open in-window row naming "
                                              f"{AGENT} is cited in STATUS.md (acknowledged, not done)"))
    return (1 if gating else 0), out


FIX_HEAD = "# fixture\n"


def _fx_row(span, owners, state, cat="cat"):
    return "\t".join([span, cat, owners, state, "art", "notes"]) + "\n"


def selftest():
    fails = total = 0

    def chk(ok, msg):
        nonlocal fails, total
        total += 1
        fails += not ok
        print(f"  {'✓' if ok else '✗'} {msg}")

    asof = dt.date(2026, 10, 1)
    with tempfile.TemporaryDirectory() as td:
        dk, stp = os.path.join(td, "D.tsv"), os.path.join(td, "S.md")
        body = (FIX_HEAD
                + _fx_row("next-DAEDALUS-session", "DAEDALUS (fix) / PROME", "PENDING", "session row")   # L2
                + _fx_row("2026-09-29", "PROME (owner) / DAEDALUS (reader)", "PENDING", "past row")      # L3
                + _fx_row("2026-10-02", "DAEDALUS", "RESOLVED 2026-10-01 (x)", "terminal row")           # L4
                + _fx_row("2026-11-30", "DAEDALUS", "PENDING", "far row")                                # L5
                + _fx_row("2026-10-03", "PROME / DAEDALUS informed", "PENDING", "info row")              # L6
                + _fx_row("2026-10-03", "WALTER", "PENDING", "not mine"))                                # L7
        open(dk, "w", encoding="utf-8").write(body)
        # D1 FIRE: STATUS cites nothing
        open(stp, "w", encoding="utf-8").write("# STATUS\nnothing here; L22 and L300 only\n")
        rc, out = assess(dk, stp, asof, 30)
        txt = "\n".join(out)
        print("    [fire output] " + out[-1])
        chk(rc == 1 and "L2 ·" in txt and "L3 ·" in txt, "D1 FIRE: uncited session-keyed L2 and past-due L3 ⇒ rc 1, both listed")
        chk("(PAST)" in txt, "D1b past-due row is marked (PAST)")
        chk("L4 ·" not in txt, "D3 terminal (RESOLVED) row never listed")
        chk("L5 ·" not in txt and "1 open beyond horizon" in txt, "D4 row beyond the 30d horizon not listed, but counted")
        chk("informed-only (does not gate): L6" in txt and "L6 ·" not in txt, "D5 'informed' row listed separately, does not gate")
        chk("L7 ·" not in txt, "D5b a row not naming DAEDALUS is never listed")
        chk(re.search(r"L2(?!\d)", "L22") is None and not cited(2, "see L22 and L300"), "D6 L2 is not cited by L22 (digit boundary)")
        # D2 CLEAN: STATUS cites L2 and L3
        open(stp, "w", encoding="utf-8").write("# STATUS\nowed: L2 · DOCKET L3/L9\n")
        rc, out = assess(dk, stp, asof, 30)
        print("    [clean output] " + out[-1])
        chk(rc == 0 and "CLEAN" in out[-1], "D2 CLEAN: both cited ⇒ rc 0 and the clean line prints")
        # D7 UNKNOWN: empty population, missing file, ragged
        open(dk, "w", encoding="utf-8").write(FIX_HEAD + _fx_row("2026-10-03", "WALTER", "PENDING"))
        rc, out = assess(dk, stp, asof, 30)
        chk(rc == 2 and "ZERO name" in out[0], "D7 zero rows naming DAEDALUS ⇒ rc 2 UNKNOWN, never CLEAN")
        rc, out = assess(os.path.join(td, "missing.tsv"), stp, asof, 30)
        chk(rc == 2, "D7b missing DOCKET ⇒ rc 2")
        open(dk, "w", encoding="utf-8").write(FIX_HEAD + "2026-10-03\tragged\tDAEDALUS\tPENDING\n")
        rc, out = assess(dk, stp, asof, 30)
        chk(rc == 2, "D7c ragged DOCKET ⇒ rc 2 (docket_view's own refusal)")
        rc, out = assess(dk, os.path.join(td, "nostatus.md"), asof, 30)
        chk(rc == 2, "D7d unreadable STATUS ⇒ rc 2")
    print("DOCKET-OWED SELFTEST " + (f"✓ {total}/{total}" if not fails else f"✗ {fails}/{total} FAILED"))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--horizon", type=int, default=30)
    ap.add_argument("--as-of")
    ap.add_argument("--docket", default=docket_view.DOCKET_DEFAULT)
    ap.add_argument("--status", default=STATUS_DEFAULT)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    as_of = dt.date.fromisoformat(a.as_of) if a.as_of else dt.datetime.now(ZoneInfo("America/New_York")).date()
    rc, out = assess(a.docket, a.status, as_of, a.horizon)
    print("\n".join(out))
    return rc


if __name__ == "__main__":
    sys.exit(main())
