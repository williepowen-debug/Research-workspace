#!/usr/bin/env python3
"""R1 corrections-pipeline generic boot leg (FORUM-6 ruling 1, Will-approved 2026-08-17).

Schema handshake: DAEDALUS draft 2026-08-26 -> WALTER CONCUR + A1/A2/A3 same night
(AGENTS/DAEDALUS/inbox/processed/2026-08-26_from-WALTER_R1-handshake-CONCUR-*.md).
Register (WALTER-owned, schema+prune): AGENTS/WALTER/registry/CORRECTIONS.tsv
Receipts (per-desk, append-only):      AGENTS/<X>/registry/corrections_receipts.tsv
                                       (PROME special-case: PROME/registry/... — repo-root desk)

Boot check:    python3 scripts/corrections_boot_check.py <AGENT>
Write receipt: python3 scripts/corrections_boot_check.py <AGENT> --receipt <COR-id> \
                   --action APPLIED|NO-OP|DEFERRED|CONTESTED [--note "..."]
Coverage:      python3 scripts/corrections_boot_check.py --coverage
Fixture overrides (SS3 testing, never mutate real files): --register P --receipts P --today YYYY-MM-DD

rc contract (CHECK_STANDARD SS9):
  0  no unreceipted NAMED rows for this desk (ALL-row WARNs may still print — WARN-never-block)
  1  >=1 NAMED row (RETIRED included — WQ-286 ④) naming this desk with no receipt of ANY action from it
     (block-class; EVERY instance printed, count-first). WQ-254 D4(a), Will 2026-09-24:
     a passed date_cap or a DEAD-AT-CAP status NEVER clears a NAMED target's block — such
     rows still BLOCK, labelled DEAD-AT-CAP. date_cap governs ALL-rows only (broadcast
     expiry: past cap = no warn, no block, counted on the INFO line).
     Production acceptance set (CHECK_STANDARD SS3(e), live register 2026-09-24):
     defective = `SAM` (COR-20260826-02, DEAD-AT-CAP, unreceipted -> rc 1);
     clean = `HAWK` (COR-20260828-01, cap passed, NO-OP receipt 2026-09-08 -> rc 0).
     Time-bound: SAM's receipt will flip the defective case; re-pick from the register.
  2  CANNOT-EVALUATE — register absent (expected pre-creation state, loud), required header
     column missing, unparseable date in ANY row (A2: NEVER a silent row-skip),
     unparseable receipts file, or an UNKNOWN AGENT NAME (B, 2026-08-28: a typo'd desk
     token must never read as a clean pass). Loud, never silent-green.
"""
import argparse, csv, io, re, sys
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_COLS = ["correction_id", "date", "corrector", "targets", "pointer", "date_cap", "status"]
ACTIONS = ["APPLIED", "NO-OP", "DEFERRED", "CONTESTED"]
RECEIPT_HEADER = ["receipt_date", "correction_id", "action", "note"]
# A2 (WALTER, bought live 8/26): dates are exact and machine-parseable or the run is
# CANNOT-EVALUATE. Accept YYYY-MM-DD or YYYY-MM-DDTHH:MM(Z). Nothing else.
DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})(?:T\d{2}:\d{2}Z?)?$")


def die2(msg):
    print(f"CORRECTIONS-CHECK 2 CANNOT-EVALUATE: {msg}")
    sys.exit(2)


def parse_day(field, val, where):
    if not val:
        return None
    m = DATE_RE.match(val.strip())
    if not m:
        # A2: an unparseable date is rc=2, never a skipped row.
        die2(f"unparseable {field} {val!r} at {where} — A2: fix the stamp, do not teach the parser prose")
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        die2(f"impossible {field} {val!r} at {where}")


def known_agents(root):
    """Every agent named in the generated FLEET_DIRECTORY.md (all sections: active, tier-2,
    dormant, special) — the same source cmd_coverage reads. Returns None if the directory
    is unreadable (caller then cannot validate and must say so, never pass silently)."""
    fd = root / "AGENTS/DAEDALUS/FLEET_DIRECTORY.md"
    if not fd.exists():
        return None
    names = set()
    for ln in fd.read_text().splitlines():
        m = re.match(r"^\| ([A-Z][A-Z0-9_]+) \|", ln)
        if m and m.group(1) != "Agent":
            names.add(m.group(1))
    return names


def require_known_agent(agent, root):
    """B (HENRY 2026-08-28, PROME-endorsed): `corrections_boot_check.py ZZZNOTANAGENT` returned
    a byte-identical rc=0 OK — a typo'd desk token was indistinguishable from a clean pass on
    the exact surface the 9/26 checkpoint is scored on. Same law as A2 one field over: an
    unparseable date is rc 2, never a silent skip; an unknown agent is rc 2, never a clean pass."""
    names = known_agents(root)
    if names is None:
        die2(f"cannot validate agent {agent!r}: FLEET_DIRECTORY.md missing — regenerate it "
             f"(render_directory.py); a check that cannot name its subject must not pass")
    if agent.upper() not in names:
        die2(f"unknown agent {agent!r} — not in AGENTS/DAEDALUS/FLEET_DIRECTORY.md (any section). "
             f"A typo'd desk token must never read as a clean pass; check the spelling")


def receipts_path(agent, root):
    base = root / "PROME" if agent == "PROME" else root / "AGENTS" / agent
    return base / "registry" / "corrections_receipts.tsv"


def read_tsv(path, required, label):
    try:
        # WALTER house style opens registry files with a '#' banner block before the real
        # header (FALSIFICATION_FIRED_LOG form; CORRECTIONS.tsv ships the same way) — skip
        # every '#' line, then DictReader sees the true header.
        text = "\n".join(l for l in path.read_text().splitlines() if not l.startswith("#"))
        reader = csv.DictReader(io.StringIO(text), delimiter="\t")
        rows = list(reader)
    except Exception as e:
        die2(f"{label} unparseable ({e}) at {path}")
    # Validate the header INDEPENDENT of row count (Codex 2026-09-05, DAEDALUS scripts/ grant).
    # The column check used to be gated on `if rows:`, so a register holding ONLY a header — a
    # WRONG one, or none at all — skipped validation and returned rc=0 / "0 corrections": the
    # check passed on empty, the exact class it exists to catch. `reader.fieldnames` is populated
    # from the header line whether or not any data rows follow, so gate on the header, not the body.
    header = reader.fieldnames
    if header is None:
        die2(f"{label} has no header at {path} — an empty/headerless file cannot be validated; "
             f"parse is by HEADER NAME")
    missing = [c for c in required if c not in header]
    if missing:
        die2(f"{label} header missing required column(s) {missing} at {path} — parse is by HEADER NAME")
    return rows


def load_register(path):
    if not path.exists():
        die2(f"register not found at {path} — WALTER creates it (schema+prune owner); "
             "pre-creation this loud state is CORRECT behavior, not an error to suppress")
    return read_tsv(path, REQUIRED_COLS, "register")


def cmd_check(agent, reg_path, rcpt_path, today):
    rows = load_register(reg_path)
    receipts = set()
    if rcpt_path.exists():
        for r in read_tsv(rcpt_path, RECEIPT_HEADER, "receipts"):
            parse_day("receipt_date", r.get("receipt_date", ""), f"{rcpt_path.name} row {r.get('correction_id')}")
            act = (r.get("action") or "").strip().upper()
            if act not in ACTIONS:
                # R1 (independent read 2026-09-24): under D4(a) the receipt is the SOLE discharge of a
                # named target, so a hand-written row with a blank/non-enum action must not clear it.
                # A2 law, one field over: unparseable is rc 2, never a pass.
                die2(f"{rcpt_path.name} row {r.get('correction_id')}: action {act!r} is not one of {ACTIONS} — "
                     "a receipt with no valid action discharges nothing; fix the row (cmd_receipt validates on write)")
            receipts.add(r.get("correction_id", "").strip())
    # WQ-254 D4(a) "A3 semantics" (Will 2026-09-24 14:59 ET; record
    # PROME/proposals/2026-09-24_wq-batch-282-254-261-260-276-RULED.md row 254; spec
    # AGENTS/DAEDALUS/runs/2026-09-17_P4_SITTING_RULING_PACKAGE.md §4 D4):
    #   A passed date_cap NEVER clears a NAMED target's block. It changes the ROW's status
    #   (DEAD-AT-CAP, WALTER's prune) and never the named TARGET's obligation — the target
    #   keeps BLOCKING (rc 1, labelled DEAD-AT-CAP) until a receipt of ANY action exists.
    #   date_cap governs ALL-rows (broadcast expiry: no warn, no block) and row status only.
    # Before this edit, a DEAD-AT-CAP status `continue`d before evaluation and a passed cap
    # `continue`d after an INFO line: SAM passed rc 0 on COR-20260826-02 from 8/28 to 9/24,
    # and after WALTER's 9/24 prune even the INFO line vanished ("0 dead-at-cap").
    named_block, all_warn, dead_named, dead_all, malformed = [], [], [], [], []
    for i, r in enumerate(rows, 2):
        cid = r["correction_id"].strip()
        where = f"{reg_path.name} line {i} ({cid})"
        parse_day("date", r["date"], where)
        cap = parse_day("date_cap", r["date_cap"], where)
        targets = [t.strip().upper() for t in r["targets"].split(",") if t.strip()]
        is_all = targets == ["ALL"]
        mine = is_all or agent.upper() in targets
        if not mine:
            continue
        status = r["status"].strip().upper()
        # WQ-286 ④ (Will 2026-09-24 18:30 ET, "REQUIRE THE RECEIPT"): a RETIRED status used to
        # `continue` here — the owner's closure discharged a named target with no receipt on
        # file (independent read R2, 2026-09-24). It now falls through: like RECEIPTED and
        # DEAD-AT-CAP, only THIS desk's receipt clears a NAMED row. Prune stays WALTER's half.
        if is_all and cap is None:
            # Ruling: date_cap is MANDATORY on ALL-rows. Missing != unparseable, so this
            # WARNS loudly rather than rc=2 (deliberate asymmetry, declared here: the desk's
            # receipts CAN still be evaluated; the schema breach is WALTER's half to fix).
            malformed.append(cid)
        cap_passed = cap is not None and cap < today
        if cid in receipts:
            continue  # a receipt of ANY action discharges THIS desk — the only thing that does, RETIRED included (WQ-286 ④)
        if is_all:
            if status == "DEAD-AT-CAP" or cap_passed:
                dead_all.append(cid)  # broadcast expired: counted, never warned, never blocked
                continue
            all_warn.append((cid, r["pointer"], r["status"], r["date"]))
            continue
        # NAMED row, unreceipted by this desk: BLOCK regardless of cap/status (D4(a)).
        if status == "RETIRED":
            label = "RETIRED — owner-declared closure; a receipt from this desk is still required, WQ-286 (4)"
        elif status == "DEAD-AT-CAP" or cap_passed:
            dead_named.append(cid)  # feeds checkpoint leg (d): dead-at-cap with zero receipts
            label = (f"DEAD-AT-CAP (row status {r['status'].strip() or '<blank>'}; cap "
                     f"{r['date_cap'].strip() or '<none>'} {'passed' if cap_passed else 'not passed'}"
                     f" — a passed cap never discharges a named target, WQ-254 D4(a))")
        else:
            label = r["status"]
        named_block.append((cid, r["pointer"], label, r["date"]))
    dead = dead_named + dead_all
    for cid in malformed:
        print(f"  MALFORMED ALL-row {cid}: date_cap MISSING (mandatory per ruling) — flag WALTER")
    if dead:
        print(f"  INFO {len(dead)} dead-at-cap with no receipt from this desk: {', '.join(dead)}"
              f" — {len(dead_named)} NAMED (still BLOCKING until receipted, WQ-254 D4(a))"
              f" · {len(dead_all)} ALL-row (broadcast expired: no warn, no block)")
    if all_warn:
        print(f"  WARN {len(all_warn)} broadcast ALL-row(s) unreceipted (warn-never-block):")
        for cid, ptr, st, d in all_warn:
            print(f"       {cid} [{st}] {d} -> {ptr}")
    if named_block:
        print(f"CORRECTIONS-CHECK 1 BLOCK: {len(named_block)} NAMED correction(s) unreceipted for {agent}"
              f" ({len(dead_named)} of them DEAD-AT-CAP):")
        for cid, ptr, st, d in named_block:
            print(f"       {cid} [{st}] {d} -> read {ptr}, then receipt: "
                  f"corrections_boot_check.py {agent} --receipt {cid} --action <APPLIED|NO-OP|DEFERRED|CONTESTED>")
        return 1
    print(f"CORRECTIONS-CHECK 0 OK: 0 unreceipted NAMED rows for {agent} "
          f"(register {len(rows)} row(s), {len(all_warn)} ALL-warn, {len(dead_all)} ALL-row(s) past cap "
          f"unreceipted = broadcast expired, not an obligation; receipts on file: {len(receipts)}) — "
          f"PASS covers the register at {reg_path} and this desk's receipts file, nothing else "
          f"(it does not prove a receipt's action was correct or that the correction was applied)")
    return 0


def cmd_receipt(agent, reg_path, rcpt_path, cid, action, note):
    rows = load_register(reg_path)
    if cid not in {r["correction_id"].strip() for r in rows}:
        die2(f"receipt refused: {cid} not in register {reg_path} — a receipt must reference a real row")
    if action not in ACTIONS:
        die2(f"action {action!r} not in {ACTIONS} (A3 enum; CONTESTED escalates via PROME rails)")
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")  # A2: exact-minute, machine-parseable
    new = not rcpt_path.exists()
    rcpt_path.parent.mkdir(parents=True, exist_ok=True)
    with open(rcpt_path, "a") as f:
        if new:
            f.write("\t".join(RECEIPT_HEADER) + "\n")
        f.write("\t".join([stamp, cid, action, (note or "").replace("\t", " ").replace("\n", " ")]) + "\n")
    print(f"RECEIPT WRITTEN: {cid} {action} @ {stamp} -> {rcpt_path}"
          + ("  (file created with header)" if new else ""))
    if action == "CONTESTED":
        print("  CONTESTED: now route the dispute to PROME (escalation rails are PROME's half of R1)")
    try:
        rel = rcpt_path.relative_to(ROOT)
        print(f"  commit it yourself (your pathspec): git add {rel} && git commit ...")
    except ValueError:
        pass  # fixture path outside the repo — no commit hint owed
    return 0


def cmd_coverage(root, reg_path):
    fd = root / "AGENTS/DAEDALUS/FLEET_DIRECTORY.md"
    if not fd.exists():
        die2(f"coverage needs {fd} (generated active-desk list)")
    desks, section = [], None
    for ln in fd.read_text().splitlines():
        if ln.startswith("## "):
            section = ln
        m = re.match(r"^\| ([A-Z]+) \|", ln)
        if m and section and ("ACTIVE" in section or "TIER-2" in section) and m.group(1) != "Agent":
            desks.append(m.group(1))
    wired, unwired = [], []
    for d in desks:
        home = root / "PROME" if d == "PROME" else root / "AGENTS" / d
        # A desk's boot may live in a BOOT.md its charter points to (PROME does this by rule:
        # "new checks go in the script/BOOT.md, CLAUDE.md must not restate"). Scanning only
        # CLAUDE.md under-counted PROME on 2026-08-28 the very hour it wired the line — the
        # coverage instrument's own scan set was narrower than the fleet's boot-surface forms
        # (PAT-084). Scan both; a desk is wired if EITHER names the check.
        surfaces = [home / "CLAUDE.md", home / "BOOT.md"]
        hit = any(f.exists() and "corrections_boot_check" in f.read_text() for f in surfaces)
        (wired if hit else unwired).append(d)
    pct = 100 * len(wired) // len(desks) if desks else 0
    print(f"R1 BOOT-LEG COVERAGE: {len(wired)}/{len(desks)} active+tier-2 desks wired = {pct}% "
          f"(checkpoint 2026-09-26 needs >=80%); register {'EXISTS' if reg_path.exists() else 'NOT YET CREATED (WALTER)'}")
    print(f"  wired: {', '.join(wired) or '(none)'}")
    print(f"  unwired ({len(unwired)}): {', '.join(unwired) or '(none)'}")
    return 0


def cmd_selftest():
    """Guard-of-the-guard for the 2026-09-05 header-validation fix (CHECK_STANDARD §3: the
    alert must fire on a capable case AND the clean line print on a clean case). Builds temp
    register fixtures and asserts read_tsv validates the header INDEPENDENT of row count — the
    exact defect (wrong/absent header + zero rows) that used to pass rc=0. Rerunnable, no real
    files touched."""
    import tempfile
    header = "\t".join(REQUIRED_COLS)

    def run_check(reg_text):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / "reg.tsv"
            reg.write_text(reg_text)
            rcpt = Path(td) / "absent.tsv"  # intentionally does not exist
            try:
                return cmd_check("DAEDALUS", reg, rcpt, date(2026, 9, 5))
            except SystemExit as e:
                return e.code

    cases = [
        ("capable: WRONG header, NO rows -> 2 (the defect Codex demonstrated)", "foo\tbar\tbaz\n", 2),
        ("capable: NO header at all (empty file) -> 2", "", 2),
        ("clean:   CORRECT header, NO rows -> 0 (valid empty register)", header + "\n", 0),
        ("clean:   '#'-banner + CORRECT header, NO rows -> 0", "# banner\n" + header + "\n", 0),
        ("regress: WRONG header WITH a data row -> still 2 (pre-existing path holds)", "foo\tbar\n1\t2\n", 2),
    ]
    ok = True
    npass = 0
    print("SELFTEST corrections_boot_check.py — header validation is row-count-independent:")
    for label, txt, want in cases:
        got = run_check(txt)
        good = got == want
        ok = ok and good
        npass += good
        print(f"  {'PASS' if good else 'FAIL'}  {label}: rc={got} (want {want})")

    # --- WQ-254 D4(a) "A3 semantics" (Will 2026-09-24): a passed cap NEVER clears a NAMED
    # target's block. Each case asserts the rc AND the output text (must/must-not substrings),
    # because the 9/24 regression was visible only in text ("INFO 1" -> "0 dead-at-cap") while rc
    # stayed 0 both times. Rows are the live register's own shapes (-0826-02 SAM, -0828-01 HAWK).
    import contextlib
    hdr = "\t".join(REQUIRED_COLS + ["summary", "direction"])
    sam_dead = "COR-20260826-02\t2026-08-26\tLIQUID\tSAM\tBOARD/x.md\t2026-08-28\tDEAD-AT-CAP\ts\tWEAKEN"
    sam_live_pastcap = "COR-20260826-02\t2026-08-26\tLIQUID\tSAM\tBOARD/x.md\t2026-08-28\tLIVE\ts\tWEAKEN"
    hawk_row = ("COR-20260828-01\t2026-08-28\tWALTER\tBRENT,FALCON,PROME,TERRY,RED,HAWK,MIDAS\tBOARD/y.md"
                "\t2026-09-11\tRECEIPTED\ts\tWEAKEN")
    all_pastcap = "COR-20260801-01\t2026-08-01\tWALTER\tALL\tBOARD/z.md\t2026-08-15\tLIVE\ts\tHOLD"
    all_live = "COR-20260920-01\t2026-09-20\tWALTER\tALL\tBOARD/z.md\t2026-10-15\tLIVE\ts\tHOLD"
    retired = "COR-20260801-02\t2026-08-01\tWALTER\tSAM\tBOARD/r.md\t2026-08-15\tRETIRED\ts\tHOLD"
    named_live = "COR-20260920-02\t2026-09-20\tWALTER\tSAM\tBOARD/n.md\t2026-10-15\tLIVE\ts\tHOLD"
    dead_nocap = "COR-20260826-03\t2026-08-26\tWALTER\tSAM\tBOARD/w.md\t\tDEAD-AT-CAP\ts\tHOLD"

    def rc_line(cid, action="NO-OP"):
        return f"2026-09-24T19:00Z\t{cid}\t{action}\tselftest"

    def run_d4(agent, reg_rows, rcpt_rows, today=date(2026, 9, 24)):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / "reg.tsv"
            reg.write_text("# banner\n" + hdr + "\n" + "".join(x + "\n" for x in reg_rows))
            rcpt = Path(td) / "rcpt.tsv"
            if rcpt_rows is not None:
                rcpt.write_text("\t".join(RECEIPT_HEADER) + "\n" + "".join(x + "\n" for x in rcpt_rows))
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                try:
                    rc = cmd_check(agent, reg, rcpt, today)
                except SystemExit as e:
                    rc = e.code
            return rc, buf.getvalue()

    d4 = [
        # (label, agent, reg_rows, rcpt_rows, want_rc, must_contain, must_not_contain)
        ("capable: DEAD-AT-CAP NAMED row, unreceipted -> 1 (SAM/-0826-02, the live instance)",
         "SAM", [sam_dead], None, 1,
         ["CORRECTIONS-CHECK 1 BLOCK", "COR-20260826-02 [DEAD-AT-CAP", "INFO 1 dead-at-cap", "1 NAMED"], []),
        ("clean:   same DEAD-AT-CAP row, receipted NO-OP -> 0",
         "SAM", [sam_dead], [rc_line("COR-20260826-02")], 0,
         ["CORRECTIONS-CHECK 0 OK"], ["CORRECTIONS-CHECK 1 BLOCK", "INFO"]),
        ("clean:   same DEAD-AT-CAP row, receipted CONTESTED -> 0 (a receipt of ANY action)",
         "SAM", [sam_dead], [rc_line("COR-20260826-02", "CONTESTED")], 0,
         ["CORRECTIONS-CHECK 0 OK"], ["CORRECTIONS-CHECK 1 BLOCK"]),
        ("capable: cap-passed LIVE NAMED row, unreceipted -> 1 (pre-prune state; was rc 0 + INFO)",
         "SAM", [sam_live_pastcap], None, 1,
         ["CORRECTIONS-CHECK 1 BLOCK", "DEAD-AT-CAP (row status LIVE; cap 2026-08-28 passed", "INFO 1"], []),
        ("capable: DEAD-AT-CAP NAMED row with NO cap, unreceipted -> 1 (status alone never discharges)",
         "SAM", [dead_nocap], None, 1, ["COR-20260826-03 [DEAD-AT-CAP", "cap <none> not passed"], []),
        ("clean:   ALL-row past cap, unreceipted -> 0, no WARN (broadcast expired)",
         "SAM", [all_pastcap], None, 0,
         ["CORRECTIONS-CHECK 0 OK", "1 ALL-row(s) past cap", "0 NAMED", "1 ALL-row (broadcast expired"],
         ["WARN", "CORRECTIONS-CHECK 1 BLOCK"]),
        ("regress: ALL-row cap NOT passed, unreceipted -> 0 WITH WARN (warn-never-block holds)",
         "SAM", [all_live], None, 0, ["WARN 1 broadcast ALL-row", "CORRECTIONS-CHECK 0 OK"], ["CORRECTIONS-CHECK 1 BLOCK"]),
        ("clean:   multi-target cap-passed row, THIS desk receipted -> 0 (HAWK/-0828-01, NO-OP 9/8)",
         "HAWK", [hawk_row], [rc_line("COR-20260828-01")], 0, ["CORRECTIONS-CHECK 0 OK"], ["CORRECTIONS-CHECK 1 BLOCK", "INFO"]),
        ("capable: same multi-target row, OTHER target unreceipted -> 1 (receipts are per-desk)",
         "BRENT", [hawk_row], [], 1, ["CORRECTIONS-CHECK 1 BLOCK", "COR-20260828-01 [DEAD-AT-CAP"], []),
        ("clean:   DEAD-AT-CAP row naming SOMEONE ELSE -> 0 (HAWK is not SAM)",
         "HAWK", [sam_dead], None, 0, ["CORRECTIONS-CHECK 0 OK"], ["CORRECTIONS-CHECK 1 BLOCK", "INFO"]),
        ("capable: RETIRED NAMED row, unreceipted -> 1 (WQ-286 (4): a receipt is still required)",
         "SAM", [retired], None, 1, ["CORRECTIONS-CHECK 1 BLOCK", "COR-20260801-02 [RETIRED"], []),
        ("clean:   RETIRED NAMED row, receipted by this desk -> 0",
         "SAM", [retired], [rc_line("COR-20260801-02")], 0, ["CORRECTIONS-CHECK 0 OK"], ["CORRECTIONS-CHECK 1 BLOCK"]),
        ("clean:   RETIRED ALL-row, future cap -> 0 (ALL-row rules: WARN never block; pinned after the 10/02 read)",
         "SAM", ["COR-20260920-03\t2026-09-20\tWALTER\tALL\tBOARD/a.md\t2026-10-15\tRETIRED\ts\tHOLD"], None, 0,
         ["CORRECTIONS-CHECK 0 OK"], ["CORRECTIONS-CHECK 1 BLOCK"]),
        ("clean:   RETIRED row naming SOMEONE ELSE -> 0",
         "HAWK", [retired], None, 0, ["CORRECTIONS-CHECK 0 OK"], ["CORRECTIONS-CHECK 1 BLOCK"]),
        ("regress: LIVE NAMED row cap in future, unreceipted -> 1 labelled LIVE (pre-existing path)",
         "SAM", [named_live], None, 1, ["COR-20260920-02 [LIVE]", "(0 of them DEAD-AT-CAP)"], ["[DEAD-AT-CAP", "INFO"]),
        ("mixed:   dead named + past-cap ALL + receipted live -> 1, counts split 1 NAMED · 1 ALL",
         "SAM", [sam_dead, all_pastcap, named_live], [rc_line("COR-20260920-02")], 1,
         ["INFO 2 dead-at-cap", "1 NAMED", "1 ALL-row", "1 NAMED correction(s) unreceipted for SAM (1 of them DEAD-AT-CAP)"],
         ["WARN"]),
    ]
    print("SELFTEST WQ-254 D4(a) — a passed cap never clears a NAMED target's block:")
    for label, agent, reg_rows, rcpt_rows, want, must, mustnot in d4:
        got, out = run_d4(agent, reg_rows, rcpt_rows)
        miss = [s for s in must if s not in out]
        bad = [s for s in mustnot if s in out]
        good = got == want and not miss and not bad
        ok = ok and good
        npass += good
        extra = "" if good else f" | missing {miss} | forbidden-present {bad} | output: {out.strip()!r}"
        print(f"  {'PASS' if good else 'FAIL'}  {label}: rc={got} (want {want}){extra}")
    total = len(cases) + len(d4)
    print(f"SELFTEST {'0 PASS' if ok else '1 FAIL'}: {npass}/{total} cases")
    return 0 if ok else 1


def main():
    p = argparse.ArgumentParser()
    p.add_argument("agent", nargs="?")
    p.add_argument("--receipt"); p.add_argument("--action"); p.add_argument("--note", default="")
    p.add_argument("--coverage", action="store_true")
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--register"); p.add_argument("--receipts"); p.add_argument("--today")
    a = p.parse_args()
    if a.selftest:
        sys.exit(cmd_selftest())
    reg = Path(a.register) if a.register else ROOT / "AGENTS/WALTER/registry/CORRECTIONS.tsv"
    if a.coverage:
        sys.exit(cmd_coverage(ROOT, reg))
    if not a.agent:
        p.error("agent name required (or --coverage)")
    # R4 (independent read 2026-09-24): the token was uppercased for validation but not for the
    # receipts path or the printed remedy — `hawk` got a false BLOCK and a command that would have
    # written AGENTS/hawk/registry/. Normalise ONCE, here, before anything derives from it.
    a.agent = a.agent.strip().upper()
    require_known_agent(a.agent, ROOT)
    rcpt = Path(a.receipts) if a.receipts else receipts_path(a.agent, ROOT)
    today = parse_day("--today", a.today, "cli") if a.today else date.today()
    if a.receipt:
        sys.exit(cmd_receipt(a.agent, reg, rcpt, a.receipt, a.action or "", a.note))
    sys.exit(cmd_check(a.agent, reg, rcpt, today))


if __name__ == "__main__":
    main()
