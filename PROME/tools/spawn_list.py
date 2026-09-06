#!/usr/bin/env python3
"""spawn_list.py — the SPAWN-DRIVER instrument (WQ-184 L1). Read-only.

STATUS: LIVE under WQ-184 — Will 2026-09-05 21:42 ET, verbatim "approve WQ-184 with your recs"
(record PROME/proposals/2026-09-05_spawn-driver-RULED.md). Wired into `prome_gate.py boot` (horizon 0)
and `closeout` (horizon 1 weekday / 3 Fri-Sat). The RULE it serves (L0, PROME/CLAUDE.md spawn block):
a registered dated row with a dark owner is a Tier-1 spawn at the first PROME boot on/after its date —
no nod; cap 4 per boot; ACTIVE owner ⇒ consumer read at the owner's artifact first; Will-owned ⇒ queue.
Review sitting 2026-09-19 (DOCKET).

QUESTION IT ANSWERS: which registered dated rows have arrived (or arrive before the next boot) whose
OWNER has no session to run them? Detection already exists in three places (desk boot.py checks,
prome_gate's DOCKET overdue / lands-today checks, docket_view) — none names a spawn candidate. This
does, and only this. It never spawns, never edits.

METHOD (every leg verifiable at the artifact):
  rows      PROME/DOCKET.tsv (key D:L<line>, physical line = the citation key, WQ-138). Live = state_kind
            PENDING per scripts/docket_view.py (PENDING / ★ / RE-DATED / SLID lead tokens); COVERED in state
            or notes = already dispositioned (check_docket_today's convention) → excluded. Undated rows are
            not this instrument's.
            + PROME/GATES.tsv LIVE rows at their review_by (key G:<gate_id>) — prome_gate already BLOCKS on a
            passed INSTRUMENT review_by; this names WHO runs the review, INSTRUMENT and JUDGEMENT alike.
  due       DOCKET date cell end-of-range, or the leading YYYY-MM-DD of GATES review_by, <= today + HORIZON.
            Overdue rows always listed.
  owner     FIRST desk token of the owner cell ("HANS (owner) / PROME (consumer read)" → HANS).
            PROME-owned → PROME does it; Will-owned → WILL_QUEUE, never a spawn.
  liveness  proxy = the owner's newest SELF-COMMIT: newest commit whose SUBJECT begins "<OWNER>:" or
            "<OWNER> ->" (never a path-scoped log — [[finding_path_scoped_git_log_measures_inbound_traffic]]:
            AGENTS/X/ receives other desks' mail). The second leg — harness `ListAgents` in the SAME MINUTE —
            is done in-session by PROME (a script cannot call it): a live desk is DOORBELLED, never spawned
            (PROME/CLAUDE.md desk-spawn preflight, WQ-178).
  class     DARK        owner's last self-commit is BEFORE the row's start date  → Tier-1 due-row spawn candidate
            ACTIVE      owner committed on/after the row's start date           → consumer read at the OWNER's
                        artifact FIRST (the L115 receipt-gap class: graded 8/7, coordinator row PENDING 29d)
            LANDS-IN-k  not yet due; printed with the owner's last-commit age so closeout can SLATE what lands
                        in the gap to the next boot (the spawn waits for the first boot on/after the date)
            PROME-OWNED / WILL-OWNED as above.
  cadence   NOT modelled in v1 — the Class 8 DESK cadence column (STATE_VOCABULARY, Will-approved 8/21,
            "instrument = fleet_triage.py, PROME applies the column") was UNBUILT at 2026-09-05 (VERIFIED:
            no cadence column in PROME/ROSTER.md; fleet_triage.py absent from PROME/tools, scripts,
            AGENTS/DAEDALUS/scripts) — commissioned as WQ-184 leg ⑥ (DOCKET, 2026-09-19). A WEEKLY desk whose
            row lands on its own day reads DARK here; the in-session ListAgents leg and the owner's STATUS
            "next boot" line are the v1 corrective. When the column lands, DARK requires last-commit older
            than the declared cadence.

EXIT: 1 when any DARK candidate exists (the gate prints them as ⚠️ lines), else 0. --selftest: 0 pass / 1 fail.
USAGE: python3 PROME/tools/spawn_list.py [--horizon N] [--tsv] [--as-of YYYY-MM-DD] [--docket PATH|REV:PATH] [--selftest]
"""
import argparse, datetime as dt, re, subprocess, sys
from pathlib import Path

ROOT = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip())
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
CAP_PER_BOOT = 4      # WQ-184 leg ② — informational here; PROME enforces at spawn time


def state_kind(state: str) -> str:
    s = state.strip().upper()
    return "PENDING" if s.startswith(("PENDING", "★", "RE-DATED", "SLID")) else "TERMINAL"


def owner_token(cell: str) -> str:
    c = cell.strip()
    if c.lower().startswith("will"):
        return "WILL"
    m = re.match(r"\**([A-Z][A-Z0-9\-]{2,})", c)
    return m.group(1) if m else "?"


def read_text(spec: str) -> str:
    """PATH, or REV:PATH (a git object — the selftest's frozen vintage)."""
    if re.match(r"^[0-9a-f]{7,40}:", spec):
        return subprocess.run(["git", "-C", str(ROOT), "show", spec], capture_output=True, text=True, check=True).stdout
    p = Path(spec)
    return (p if p.is_absolute() else ROOT / p).read_text(encoding="utf-8")


class Liveness:
    def __init__(self, until: str | None):
        self.until, self._c = until, {}

    def last_self_commit(self, desk: str):
        """(date, sha) of the newest commit (optionally --until) whose SUBJECT starts with the desk's name — or None.
        `--grep` matches anywhere in the message (a PROME closeout body line "MIDAS: …" false-matched as a MIDAS
        commit on the 9/5 vintage — caught by the selftest), so the subject is re-checked in Python."""
        if desk not in self._c:
            pat = re.compile(rf"^{re.escape(desk)}( ->|:)")
            cmd = ["git", "-C", str(ROOT), "log", "-n", "40", "--format=%cs\t%h\t%s", "--extended-regexp",
                   f"--grep=^{re.escape(desk)}( ->|:)"]
            if self.until:
                cmd.append(f"--until={self.until}")
            hit = None
            for line in subprocess.run(cmd, capture_output=True, text=True).stdout.split("\n"):
                parts = line.split("\t", 2)
                if len(parts) == 3 and pat.match(parts[2]):
                    hit = (parts[0], parts[1]); break
            self._c[desk] = hit
        return self._c[desk]


def classify(owner, start, due, today, live: Liveness):
    delta = (today - due).days                    # >0 overdue, 0 today, <0 lands in |delta| days
    if owner == "PROME":
        return delta, "PROME-OWNED", "do it, never spawn"
    if owner == "WILL":
        return delta, "WILL-OWNED", "WILL_QUEUE / re-present, never spawn"
    lsc = live.last_self_commit(owner)
    if lsc is None:
        return delta, ("DARK" if delta >= 0 else f"LANDS-IN-{-delta}d"), "no self-commit found in history"
    lsc_date = dt.date.fromisoformat(lsc[0])
    age = (today - lsc_date).days
    if delta >= 0:
        cls = "ACTIVE" if lsc_date >= start else "DARK"
        return delta, cls, f"last self-commit {lsc[0]} ({age}d ago, {lsc[1]}) {'≥' if cls == 'ACTIVE' else '<'} row start {start}"
    return delta, f"LANDS-IN-{-delta}d", f"owner last self-commit {lsc[0]} ({age}d ago, {lsc[1]})"


def collect(docket_text: str, gates_text: str, today: dt.date, horizon_days: int, live: Liveness):
    horizon = today + dt.timedelta(days=horizon_days)
    rows = []
    for ln, raw in enumerate(docket_text.split("\n"), start=1):
        if not raw or raw.startswith("#"):
            continue
        c = raw.split("\t")
        if len(c) < 4 or state_kind(c[3]) != "PENDING":
            continue
        start_s, end_s = c[0].split("..")[0].strip(), c[0].split("..")[-1].strip()
        if not DATE.fullmatch(end_s):
            continue
        due = dt.date.fromisoformat(end_s)
        if due > horizon or "COVERED" in (c[3] + " " + (c[5] if len(c) > 5 else "")):
            continue
        start = dt.date.fromisoformat(start_s) if DATE.fullmatch(start_s) else due
        owner = owner_token(c[2])
        delta, cls, basis = classify(owner, start, due, today, live)
        rows.append((f"D:L{ln}", end_s, delta, owner, cls, basis, re.sub(r"\s+", " ", c[1])[:72]))
    hdr = None
    for raw in gates_text.split("\n"):
        if not raw or raw.startswith("#"):
            continue
        c = raw.split("\t")
        if hdr is None:
            hdr = [h.strip() for h in c]
            continue
        g = dict(zip(hdr, c))
        if not g.get("state", "").strip().upper().startswith("LIVE"):
            continue
        m = DATE.match(g.get("review_by", "").strip())
        if not m:
            continue
        due = dt.date.fromisoformat(m.group(0))
        if due > horizon:
            continue
        owner = owner_token(g.get("owner", ""))
        reg = g.get("registered", "").strip()
        start = dt.date.fromisoformat(reg[:10]) if DATE.match(reg) else due
        delta, cls, basis = classify(owner, start, due, today, live)
        scan = (g.get("scannable", "").split(" ")[0] or "unclassed")
        rows.append((f"G:{g['gate_id']}", m.group(0), delta, owner, cls, basis,
                     f"review_by [{scan}] — {re.sub(chr(9), ' ', g.get('condition', ''))[:56]}"))
    order = {"DARK": 0, "ACTIVE": 1, "PROME-OWNED": 2, "WILL-OWNED": 3}
    rows.sort(key=lambda r: (order.get(r[4], 4), -r[2], r[0]))
    return rows


def render(rows, today, horizon_days, tsv: bool) -> int:
    n = {k: sum(1 for r in rows if r[4] == k) for k in ("DARK", "ACTIVE", "PROME-OWNED", "WILL-OWNED")}
    lands = sum(1 for r in rows if r[4].startswith("LANDS"))
    print(f"spawn_list · as-of {today} · horizon +{horizon_days}d · {len(rows)} row(s): DARK {n['DARK']} · ACTIVE {n['ACTIVE']} · "
          f"lands-ahead {lands} · PROME {n['PROME-OWNED']} · WILL {n['WILL-OWNED']}")
    print("key\tdue\tΔd\towner\tclass\tbasis\tcatalyst")
    for r in rows:
        line = "\t".join(str(x) for x in r)
        print(("⚠️ " if r[4] == "DARK" else "") + line)
    if not tsv:
        print(f"\nREAD (WQ-184 L0): DARK = Tier-1 due-row spawn after an in-session ListAgents check (live desk ⇒ doorbell); "
              f"cap {CAP_PER_BOOT}/boot, beyond → slate to Will. ACTIVE = read the owner's artifact FIRST — the row may already "
              "be graded (receipt gap). Cadence not modelled (header).")
    return 1 if n["DARK"] else 0


def selftest() -> int:
    """Frozen vintage: DOCKET at 9d2fa3f1b (2026-09-05 18:53 ET, before the 19:4x spawns), liveness bounded to
    2026-09-05 19:40. Expected at horizon 0: exactly one DARK (D:L280 MIDAS-08, due 9/4 — the row Will's word ran
    that night); D:L239 (DAEDALUS, committed earlier 9/5) ACTIVE; D:L264/L265 (BRENT) ABSENT because COVERED; D:L17 WILL.
    At horizon 3: D:L283 (FERT T11, dated 9/8) and G:GATE-FALCON-001 (review_by 9/8) LAND — TERRY's L115 (dated 9/11)
    appears at neither. The selftest caught the first proxy defect (body-line false match) on its first run."""
    today = dt.date(2026, 9, 5)
    live = Liveness(until="2026-09-05 19:40 -0400")
    d = read_text("9d2fa3f1b:PROME/DOCKET.tsv")
    g = read_text("9d2fa3f1b:PROME/GATES.tsv")
    r0 = {r[0]: r[4] for r in collect(d, g, today, 0, live)}
    r3 = {r[0]: r[4] for r in collect(d, g, today, 3, live)}
    checks = [
        ("horizon-0 DARK set == {D:L280} (MIDAS's last SUBJECT-commit before 19:40 was 8/31)", {k for k, v in r0.items() if v == "DARK"} == {"D:L280"}),
        ("D:L239 ACTIVE (DAEDALUS committed 9/5 before 19:40)", r0.get("D:L239") == "ACTIVE"),
        ("D:L264 + D:L265 ABSENT — COVERED-annotated (consumer read registered), not spawn candidates", "D:L264" not in r0 and "D:L265" not in r0),
        ("D:L17 WILL-OWNED", r0.get("D:L17") == "WILL-OWNED"),
        ("D:L283 LANDS-IN-3d at horizon 3 (FERT's DOCKET row is dated 9/8; the desk clock said 9/4)", r3.get("D:L283") == "LANDS-IN-3d"),
        ("D:L115 (dated 9/11) absent at horizon 3", "D:L115" not in r3),
        ("GATES leg: G:GATE-FALCON-001 (review_by 9/8, JUDGEMENT) LANDS-IN-3d; none at horizon 0",
         r3.get("G:GATE-FALCON-001") == "LANDS-IN-3d" and not any(k.startswith("G:") for k in r0)),
    ]
    ok = True
    for name, passed in checks:
        print(("✅ " if passed else "❌ ") + name)
        ok &= passed
    print(f"selftest {'PASS' if ok else 'FAIL'} {sum(p for _, p in checks)}/{len(checks)}")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--horizon", type=int, default=0, help="days ahead (boot 0; closeout 1 weekday / 3 Fri-Sat)")
    ap.add_argument("--tsv", action="store_true")
    ap.add_argument("--as-of", help="YYYY-MM-DD: sets today AND bounds the liveness git log (--until)")
    ap.add_argument("--docket", default="PROME/DOCKET.tsv", help="PATH or REV:PATH")
    ap.add_argument("--gates", default="PROME/GATES.tsv", help="PATH or REV:PATH")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    today = dt.date.fromisoformat(a.as_of) if a.as_of else dt.date.today()
    live = Liveness(until=(a.as_of + " 23:59") if a.as_of else None)
    rows = collect(read_text(a.docket), read_text(a.gates), today, a.horizon, live)
    return render(rows, today, a.horizon, a.tsv)


if __name__ == "__main__":
    sys.exit(main())
