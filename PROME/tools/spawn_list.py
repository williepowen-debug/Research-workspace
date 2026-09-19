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
from typing import NamedTuple
from pathlib import Path

ROOT = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip())
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
CAP_PER_BOOT = 4      # WQ-184 leg ② — informational here; PROME enforces at spawn time


# ⛔ ONE interpretation of "is this row still open", imported — never re-implemented here.
# scripts/docket_view.py is the declared authority (this file's own docstring already said so)
# and this module used to carry a SECOND copy of the rule. The two copies happened to agree on
# all 368 live rows when checked 2026-09-13, which is exactly why a divergence would have been
# invisible. The real incident was neither copy: PROME prepared a spawn brief from an ad-hoc
# `$4 ~ /PENDING/` SUBSTRING match, which matches the word PENDING inside TERMINAL rows'
# "prior:" history chains — 77 terminal rows matched, a backlog was fabricated from it, and a
# false premise about a Will-ruled retirement reached a desk. Fixing that with care alone does
# not work; the fix is that the shared reading is the ONLY reading and is easy to call
# (see --open below). (Will, 2026-09-13.)
_DV = ROOT / "scripts"
if str(_DV) not in sys.path:
    sys.path.insert(0, str(_DV))
from docket_view import state_kind            # noqa: E402  — fail LOUD if it moves; never fall back to a local copy


COVERED_SELF = re.compile(r"COVERED:[^·|]*\bPROME\b[^·|]*\b(?:L0 SPAWN|SPAWN|SLATED|SLATE)\b", re.I)


def covered(state_cell: str, notes_cell: str) -> bool:
    """A `COVERED:` annotation suppresses the row as a spawn candidate — EXCEPT when the coverer IS this
    driver: "COVERED: PROME 9/11 boot slate — WATT L0 spawn (SLATED …)" names PROME's own slated spawn, and
    reading that as coverage made the 9/11 boot skip the very rows its closeout had slated (L319 · L323 ·
    L311 · L320 · L124 — found 2026-09-11 11:5x). A PROME-slated spawn is the driver's job, never its excuse."""
    s = state_cell + " " + notes_cell
    if "COVERED" not in s.upper():
        return False
    return not COVERED_SELF.search(s)


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
            r = subprocess.run(cmd, capture_output=True, text=True)
            if r.returncode != 0:
                # FAIL CLOSED. An unread returncode made a failed `git log` indistinguishable from
                # "no commits", and DARK at a due row IS the WQ-184 Tier-1 spawn trigger — so a git
                # failure authorised spawning every owner. Realistic trigger: index.lock contention
                # on the shared .git while several desks commit. (DAEDALUS, L294 sweep, 2026-09-12.)
                hit = ("!ERR", (r.stderr or "").strip().split("\n")[0][:120] or f"git log rc={r.returncode}")
            else:
                for line in r.stdout.split("\n"):
                    parts = line.split("\t", 2)
                    if len(parts) == 3 and pat.match(parts[2]):
                        hit = (parts[0], parts[1]); break
            self._c[desk] = hit
        return self._c[desk]


# ── DESK CADENCE (WQ-269, Will-ruled 2026-09-19 "wire it now"; spec
# AGENTS/DAEDALUS/design/2026-09-08_DESK_CADENCE_SPEC.md) ────────────────────
# ⛔ ANNOTATION ONLY. Cadence NEVER changes a row's class, never suppresses a due
# row, and never touches the exit-code contract (spec §3, §5, §6). It answers
# "is this desk's quiet PLANNED?" beside — never instead of — "is there a due
# obligation?". Planned quiet is not a completed grade.
CADENCE_TOKENS = {"DAILY", "WEEKLY", "MONTHLY", "EVENT-DRIVEN", "ON-DEMAND", "UNDECLARED"}
NO_CLOCK = {"EVENT-DRIVEN", "ON-DEMAND", "UNDECLARED"}


def read_cadence(roster_text: str):
    """ROSTER § DESK CADENCE -> {desk: token}. Duplicates and unknown tokens are
    kept as CANNOT-EVALUATE causes rather than resolved — a duplicate roster
    identity must not silently pick one (spec §5)."""
    out, dupes, bad = {}, set(), {}
    sect = roster_text.split("## DESK CADENCE", 1)
    if len(sect) < 2:
        return out, dupes, bad, False
    body = sect[1].split("\n## ", 1)[0]
    for raw in body.split("\n"):
        c = [x.strip() for x in raw.split("|")]
        if len(c) < 4 or not c[1] or c[1].startswith("-") or c[1].startswith("*"):
            continue
        desk, tok = c[1].strip("`* "), c[2].strip("`* ").upper()
        if desk in ("Agent", "Token") or not desk:
            continue
        if desk in out or desk in dupes:
            # ⛔ REMOVE the first pick, do not merely record the clash. Leaving it
            # meant the map silently resolved a duplicate identity while the
            # annotation said CANNOT-EVALUATE — two paths agreeing today and
            # diverging for any future caller (DOCKET L442). Found by the drill.
            out.pop(desk, None); dupes.add(desk); continue
        if tok not in CADENCE_TOKENS:
            bad[desk] = tok; continue
        out[desk] = tok
    return out, dupes, bad, True


def _month_later(d: dt.date) -> dt.date:
    """Same day next calendar month, clamped to that month's last day. Never a
    30-day constant — Jan 31 -> Feb 28/29 (spec acceptance case)."""
    y, m = (d.year + 1, 1) if d.month == 12 else (d.year, d.month + 1)
    import calendar
    return dt.date(y, m, min(d.day, calendar.monthrange(y, m)[1]))


def cadence_note(owner, cad_map, dupes, bad, present, last_date, today):
    """Return a short annotation. ⛔ Every non-evaluable path is NAMED, never a
    silent pass (spec §5)."""
    if owner in ("PROME", "WILL", "?"):
        return "n/a"
    if not present:
        return "CANNOT-EVALUATE (no ROSTER cadence section)"
    if owner in dupes:
        return "CANNOT-EVALUATE (duplicate ROSTER identity)"
    if owner in bad:
        return f"CANNOT-EVALUATE (unknown token {bad[owner]!r})"
    tok = cad_map.get(owner)
    if tok is None:
        return "CANNOT-EVALUATE (desk absent from ROSTER cadence)"
    if tok == "UNDECLARED":
        return "UNDECLARED — CANNOT-EVALUATE (no cadence declared); the due row governs"
    if tok in NO_CLOCK:
        return f"{tok} — no age clock; the due row governs"
    if last_date is None:
        return f"{tok} — CANNOT-EVALUATE (no qualifying owner commit)"
    age = (today - last_date).days
    if tok == "DAILY":
        late = age > 1
    elif tok == "WEEKLY":
        late = age > 7                      # exactly 7 is WITHIN cadence
    else:                                   # MONTHLY
        late = today > _month_later(last_date)
    return f"{tok} — {'REVIEW HINT, past cadence' if late else 'within cadence'} ({age}d)"


def classify(owner, start, due, today, live: Liveness):
    delta = (today - due).days                    # >0 overdue, 0 today, <0 lands in |delta| days
    if owner == "PROME":
        return delta, "PROME-OWNED", "do it, never spawn"
    if owner == "WILL":
        return delta, "WILL-OWNED", "WILL_QUEUE / re-present, never spawn"
    if owner == "?":
        # An unparseable owner cell is a PARSE failure, not a liveness verdict. Letting it fall
        # through would grep for "?", find nothing legitimately, and read DARK — the same fail-open.
        return delta, "UNKNOWN", "owner cell unparseable — cannot resolve a desk; NOT a spawn candidate"
    lsc = live.last_self_commit(owner)
    if lsc is not None and lsc[0] == "!ERR":
        return delta, "UNKNOWN", f"git log FAILED, liveness not established ({lsc[1]}) — NOT a spawn candidate"
    if lsc is None:
        return delta, ("DARK" if delta >= 0 else f"LANDS-IN-{-delta}d"), "no self-commit found in history"
    lsc_date = dt.date.fromisoformat(lsc[0])
    age = (today - lsc_date).days
    if delta >= 0:
        cls = "ACTIVE" if lsc_date >= start else "DARK"
        return delta, cls, f"last self-commit {lsc[0]} ({age}d ago, {lsc[1]}) {'≥' if cls == 'ACTIVE' else '<'} row start {start}"
    return delta, f"LANDS-IN-{-delta}d", f"owner last self-commit {lsc[0]} ({age}d ago, {lsc[1]})"


class Row(NamedTuple):
    """One due obligation. ⛔ APPEND new fields at the END and NEVER positionally unpack the
    whole row downstream — 2026-09-19: adding `cadence` (7th) silently broke
    session_presence.py, which unpacked 7. Named access is the contract; index access is
    grandfathered. Acceptance conditions: PROME/tools/tests/ACCEPTANCE_presence_reader_contract_2026-09-19.md"""
    key: str
    due: str
    delta: int
    owner: str
    cls: str
    basis: str
    cadence: str
    catalyst: str


def collect(docket_text: str, gates_text: str, today: dt.date, horizon_days: int, live: Liveness, roster_text: str = ""):
    horizon = today + dt.timedelta(days=horizon_days)
    cad_map, dupes, bad, present = read_cadence(roster_text)
    def _note(owner):
        lsc = live.last_self_commit(owner) if owner not in ("PROME", "WILL", "?") else None
        ld = dt.date.fromisoformat(lsc[0]) if (lsc and lsc[0] != "!ERR") else None
        return cadence_note(owner, cad_map, dupes, bad, present, ld, today)
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
        if due > horizon or covered(c[3], c[5] if len(c) > 5 else ""):
            continue
        start = dt.date.fromisoformat(start_s) if DATE.fullmatch(start_s) else due
        owner = owner_token(c[2])
        delta, cls, basis = classify(owner, start, due, today, live)
        rows.append(Row(f"D:L{ln}", end_s, delta, owner, cls, basis, _note(owner), re.sub(r"\s+", " ", c[1])[:72]))
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
        rows.append(Row(f"G:{g['gate_id']}", m.group(0), delta, owner, cls, basis, _note(owner),
                        f"review_by [{scan}] — {re.sub(chr(9), ' ', g.get('condition', ''))[:56]}"))
    order = {"UNKNOWN": 0, "DARK": 1, "ACTIVE": 2, "PROME-OWNED": 3, "WILL-OWNED": 4}
    rows.sort(key=lambda r: (order.get(r[4], 4), -r[2], r[0]))
    return rows


def render(rows, today, horizon_days, tsv: bool) -> int:
    n = {k: sum(1 for r in rows if r[4] == k) for k in ("UNKNOWN", "DARK", "ACTIVE", "PROME-OWNED", "WILL-OWNED")}
    lands = sum(1 for r in rows if r[4].startswith("LANDS"))
    cne = sum(1 for r in rows if str(r[6]).startswith("CANNOT-EVALUATE"))
    print(f"spawn_list · as-of {today} · horizon +{horizon_days}d · {len(rows)} row(s): DARK {n['DARK']} · ACTIVE {n['ACTIVE']} · "
          f"lands-ahead {lands} · PROME {n['PROME-OWNED']} · WILL {n['WILL-OWNED']}"
          + (f" · \u26d4 UNKNOWN {n['UNKNOWN']} (liveness NOT established — never a spawn)" if n["UNKNOWN"] else ""))
    print("key\tdue\tΔd\towner\tclass\tbasis\tcadence\tcatalyst")
    for r in rows:
        line = "\t".join(str(x) for x in r)
        print(("\u26d4 " if r[4] == "UNKNOWN" else "⚠️ " if r[4] == "DARK" else "") + line)
    if not tsv:
        print(f"\nREAD (WQ-184 L0): DARK = Tier-1 due-row spawn after an in-session ListAgents check (live desk ⇒ doorbell); "
              f"cap {CAP_PER_BOOT}/boot, beyond → slate to Will. ACTIVE = read the owner's artifact FIRST — the row may already "
              "be graded (receipt gap). \u26d4 CADENCE IS AN ANNOTATION ONLY — it never changes a class, never hides a due "
              "row and never moves the exit code; PLANNED QUIET IS NOT A COMPLETED GRADE, and CANNOT-EVALUATE is not a pass.")
    if n["UNKNOWN"]:
        print(f"\n\u26d4 {n['UNKNOWN']} row(s) UNKNOWN: liveness could not be established (failed git log, or an "
              "unparseable owner cell). \u26d4 NEVER spawn on UNKNOWN \u2014 fix the read, then re-run. A failed check is "
              "not evidence a desk is dark.")
    return 2 if n["UNKNOWN"] else (1 if n["DARK"] else 0)


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
    # Second frozen vintage: DOCKET at ffe54ea19 (the 2026-09-11 01:3x closeout, pushed 09:32), liveness bounded to
    # 2026-09-11 10:00 — the rows the closeout SLATED carry "COVERED: PROME 9/11 boot slate … L0 spawn" and must
    # still be candidates (the 11:5x finding); rows COVERED by a consumer read (L264/L265 class) stay absent.
    today2 = dt.date(2026, 9, 11)
    live2 = Liveness(until="2026-09-11 10:00 -0400")
    d2 = read_text("ffe54ea19:PROME/DOCKET.tsv"); g2 = read_text("ffe54ea19:PROME/GATES.tsv")
    q0 = {r[0]: r[4] for r in collect(d2, g2, today2, 0, live2)}
    checks += [
        ("9/11 vintage: D:L319 (WATT) present — 'COVERED: PROME … L0 spawn (SLATED …)' is the driver's own slate, not coverage", "D:L319" in q0),
        ("9/11 vintage: D:L323 (VULCAN) present for the same reason", "D:L323" in q0),
        ("9/11 vintage: D:L319 + D:L323 read DARK (owners' last self-commit before the row's 9/11 start)", q0.get("D:L319") == "DARK" and q0.get("D:L323") == "DARK"),
        ("9/11 vintage: D:L260 (BROCK) still DARK", q0.get("D:L260") == "DARK"),
    ]
    ok = True
    for name, passed in checks:
        print(("✅ " if passed else "❌ ") + name)
        ok &= passed
    print(f"selftest {'PASS' if ok else 'FAIL'} {sum(p for _, p in checks)}/{len(checks)}")
    return 0 if ok else 1



def cadence_selftest() -> int:
    """DAEDALUS's acceptance cases (spec § 'Acceptance cases for PROME's implementation'),
    implemented as drills rather than re-described. Written by the DESIGNER before the
    implementation existed, which is the WQ-229 shape — the conditions are not the author's own."""
    ok = True
    def chk(name, got, want):
        nonlocal ok
        good = (want in got) if isinstance(want, str) else want(got)
        ok &= good
        print(f"  {'OK  ' if good else 'FAIL'} {name}\n        -> {got}")
    R = ("## DESK CADENCE\n| Agent | Cadence | x |\n|---|---|---|\n"
         "| ALPHA | WEEKLY | - |\n| BETA | MONTHLY | - |\n| GAMMA | EVENT-DRIVEN | - |\n"
         "| DELTA | ON-DEMAND | - |\n| EPS | UNDECLARED | - |\n| ZETA | HOURLY | - |\n"
         "| DUP | WEEKLY | - |\n| DUP | DAILY | - |\n\n## NEXT\n")
    cm, du, bad, pres = read_cadence(R)
    chk("roster parses; duplicate REMOVED from the map, not silently resolved",
        f"map={sorted(cm)} dupes={sorted(du)} bad={bad}",
        lambda g: "DUP" not in g.split("dupes=")[0] and "DUP" in g and "HOURLY" in g)
    T = dt.date(2026, 3, 10)
    chk("WEEKLY at exactly 7d is WITHIN cadence",
        cadence_note("ALPHA", cm, du, bad, pres, T - dt.timedelta(days=7), T), "within cadence")
    chk("WEEKLY at 8d is a REVIEW HINT",
        cadence_note("ALPHA", cm, du, bad, pres, T - dt.timedelta(days=8), T), "REVIEW HINT")
    chk("MONTHLY Jan 31 -> Feb 28 clamp, not a 30-day constant",
        cadence_note("BETA", cm, du, bad, pres, dt.date(2026, 1, 31), dt.date(2026, 2, 28)), "within cadence")
    chk("MONTHLY Jan 31 -> Mar 1 is past cadence",
        cadence_note("BETA", cm, du, bad, pres, dt.date(2026, 1, 31), dt.date(2026, 3, 1)), "REVIEW HINT")
    chk("EVENT-DRIVEN makes NO age claim",
        cadence_note("GAMMA", cm, du, bad, pres, T - dt.timedelta(days=400), T), "no age clock")
    chk("ON-DEMAND makes NO age claim",
        cadence_note("DELTA", cm, du, bad, pres, T - dt.timedelta(days=400), T), "no age clock")
    chk("UNDECLARED is named CANNOT-EVALUATE, matching ROSTER's own wording",
        cadence_note("EPS", cm, du, bad, pres, T, T), "CANNOT-EVALUATE")
    chk("unknown token -> named CANNOT-EVALUATE",
        cadence_note("ZETA", cm, du, bad, pres, T, T), "CANNOT-EVALUATE")
    chk("duplicate identity -> named CANNOT-EVALUATE, no silent pick",
        cadence_note("DUP", cm, du, bad, pres, T, T), "duplicate")
    chk("desk absent from roster -> named CANNOT-EVALUATE",
        cadence_note("NOBODY", cm, du, bad, pres, T, T), "CANNOT-EVALUATE")
    chk("no cadence section at all -> named CANNOT-EVALUATE",
        cadence_note("ALPHA", *read_cadence("## OTHER\n"), None, T), "no ROSTER cadence section")
    chk("no qualifying owner commit -> CANNOT-EVALUATE, never 'within'",
        cadence_note("ALPHA", cm, du, bad, pres, None, T), "CANNOT-EVALUATE")
    chk("PROME/WILL rows are n/a, not evaluated",
        cadence_note("PROME", cm, du, bad, pres, None, T), "n/a")
    print("cadence selftest", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def list_open(docket_text, today):
    """Every DOCKET row still OPEN by the SHARED lead-token reading — no spawn-candidacy filter.

    This exists because "what is still owed" and "what should PROME spawn" are different
    questions, and answering the first with the second's machinery is what hid three due rows
    on 2026-09-13 (DOCKET L368). It is also the query to reach for when preparing a brief:
    the alternative PROME actually reached for was an ad-hoc substring match that read 77
    TERMINAL rows as open and put a false premise into a desk's instructions.

    Returns (line_no, date_cell, owner, overdue, description) for open rows only.
    """
    out = []
    for i, line in enumerate(docket_text.split("\n"), 1):
        if not line.strip() or line.startswith("#"):
            continue
        c = line.split("\t")
        if len(c) < 4:
            continue
        if state_kind(c[3]) != "PENDING":
            continue
        m = DATE.findall(c[0])
        due = m[-1] if m else ""                      # a range's END is the operative date
        out.append((i, c[0], c[2], due and due <= today.isoformat(), c[1]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--horizon", type=int, default=0, help="days ahead (boot 0; closeout 1 weekday / 3 Fri-Sat)")
    ap.add_argument("--tsv", action="store_true")
    ap.add_argument("--as-of", help="YYYY-MM-DD: sets today AND bounds the liveness git log (--until)")
    ap.add_argument("--docket", default="PROME/DOCKET.tsv", help="PATH or REV:PATH")
    ap.add_argument("--gates", default="PROME/GATES.tsv", help="PATH or REV:PATH")
    ap.add_argument("--roster", default="PROME/ROSTER.md", help="PATH or REV:PATH — owner-declared cadence")
    ap.add_argument("--open", action="store_true",
                    help="list every DOCKET row still OPEN by the shared lead-token reading, with no "
                         "spawn-candidacy filtering. USE THIS WHEN PREPARING A BRIEF. It answers 'what is "
                         "still owed', which is a DIFFERENT question from 'what should PROME spawn' — the "
                         "COVERED suppression that governs the latter is wrong for the former and hides "
                         "assigned work that has not happened yet (DOCKET L368).")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--cadence-selftest", action="store_true",
                    help="DAEDALUS's delivered acceptance cases for the cadence reader (WQ-269)")
    a = ap.parse_args()
    if a.cadence_selftest:
        sys.exit(cadence_selftest())
    if a.selftest:
        return selftest()
    today = dt.date.fromisoformat(a.as_of) if a.as_of else dt.date.today()
    if a.open:
        rows = list_open(read_text(a.docket), today)
        overdue = sum(1 for r in rows if r[3])
        print(f"DOCKET open rows (shared lead-token reading) · as-of {today} · "
              f"{len(rows)} open · {overdue} due or overdue")
        print("⚠️  NOT a spawn list — no COVERED filtering. 'Owed' != 'PROME should spawn it'.")
        for ln, date_cell, owner, is_overdue, desc in rows:
            print(f"  {'DUE ' if is_overdue else '    '}L{ln:<4} {date_cell:<24.24} "
                  f"{owner[:26]:<26.26} {desc[:64]}")
        return 0
    live = Liveness(until=(a.as_of + " 23:59") if a.as_of else None)
    # ⛔ THE CADENCE READ MUST NEVER BE ABLE TO KILL THE READER. Found by the failure-path
    # check the spec demands (§5, "preserve the reader's existing exit-code contract"): an
    # unreadable ROSTER took read_text() down with it, printing ZERO due rows and moving rc
    # 0 -> 1. A missing ANNOTATION source was suppressing the OBLIGATIONS it annotates —
    # a clean-looking board with every due row gone, which is the worst possible direction.
    # Degrade to "no cadence section" (-> named CANNOT-EVALUATE) and render the rows.
    try:
        roster_text = read_text(a.roster)
    except BaseException as e:
        roster_text = ""
        print(f"\u26a0\ufe0f  cadence source unreadable ({a.roster}: {type(e).__name__}) — "
              "every row below reads CANNOT-EVALUATE for cadence; due rows are UNAFFECTED", file=sys.stderr)
    rows = collect(read_text(a.docket), read_text(a.gates), today, a.horizon, live, roster_text)
    return render(rows, today, a.horizon, a.tsv)


if __name__ == "__main__":
    sys.exit(main())
