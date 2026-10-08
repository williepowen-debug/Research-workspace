#!/usr/bin/env python3
"""R1 corrections-pipeline generic boot leg (FORUM-6 ruling 1, Will-approved 2026-08-17).

Schema handshake: DAEDALUS draft 2026-08-26 -> WALTER CONCUR + A1/A2/A3 same night
(AGENTS/DAEDALUS/inbox/processed/2026-08-26_from-WALTER_R1-handshake-CONCUR-*.md).
Register (WALTER-owned, schema+prune): AGENTS/WALTER/registry/CORRECTIONS.tsv
Receipts (per-desk, append-only):      AGENTS/<X>/registry/corrections_receipts.tsv
                                       (PROME special-case: PROME/registry/... — repo-root desk)

Boot check:    python3 scripts/corrections_boot_check.py <AGENT>
Write receipt: python3 scripts/corrections_boot_check.py <AGENT> --receipt <COR-id> --action <A> [--note "..."]
                 WQ-399 (Will 2026-10-08) required fields per action — refused (rc 2, nothing written) without:
                   APPLIED   --artifact <path#key> [--artifact ...] --validation-ref <path#key|NONE>
                   NO-OP     --scope <text>
                   DEFERRED  --review YYYY-MM-DD   (today or later)
                   CONTESTED (none new)
                 stored as `key=value; ` tokens at the front of the note; no new column.
Coverage:      python3 scripts/corrections_boot_check.py --coverage
Write leg:     python3 scripts/corrections_boot_check.py --write-compliance [--since YYYY-MM-DD]
                   (WQ-393: correction-class BOARD signals with no register row; default since =
                   the 2026-10-08 ruling; rc 0 OK / 1 OWED / 2 CANNOT-EVALUATE incl. empty window)
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
                  f"corrections_boot_check.py {agent} --receipt {cid} --action <A> + WQ-399 fields "
                  f"(APPLIED: --artifact <path#key> --validation-ref <path#key|NONE> · NO-OP: --scope <text> · "
                  f"DEFERRED: --review YYYY-MM-DD)")
        return 1
    print(f"CORRECTIONS-CHECK 0 OK: 0 unreceipted NAMED rows for {agent} "
          f"(register {len(rows)} row(s), {len(all_warn)} ALL-warn, {len(dead_all)} ALL-row(s) past cap "
          f"unreceipted = broadcast expired, not an obligation; receipts on file: {len(receipts)}) — "
          f"PASS covers the register at {reg_path} and this desk's receipts file, nothing else "
          f"(it does not prove a receipt's action was correct or that the correction was applied)")
    return 0


# WQ-399 (Will 2026-10-08 15:27 ET, "399 approve"): the D3/D2 fields ruled 9/17 had no write path —
# `artifact=` on 5/108 receipts, `validation_ref` on 0/108 — because this writer took only a free
# --note (runs/2026-10-08_D7_CLOSURE_SCOPE_REVIEW.md §2; PAT-150 field-level). The writer now refuses
# the receipt without them. Acceptance: design/2026-10-08_WQ399_RECEIPT_WRITER_ACCEPTANCE.md W1–W16.
REQUIRED_FIELDS = {"APPLIED": ("artifact", "validation_ref"), "NO-OP": ("scope",), "DEFERRED": ("review",)}
PTR_RE = re.compile(r"^[^\s#]+#\S.*$")        # path#key; the key may hold spaces ("STATUS.md#BOTTOM LINE")
FLAG = {"artifact": "--artifact <path#key>", "validation_ref": "--validation-ref <path#key|NONE>",
        "scope": "--scope <text>", "review": "--review YYYY-MM-DD"}


# Independent read 2026-10-08 (design/2026-10-08_WQ399_INDEPENDENT_READ.md) ❌ C10: a value carrying
# `\r`, U+2028, `\x85` or `\x0c` was written with rc 0 and then broke that desk's boot check (rc 2,
# misattributed to receipt_date) — `"$(cat f)"` from a CRLF file on this box keeps the `\r`. Any char
# str.splitlines() breaks on, a tab, or `;` is refused in a FIELD; in the free --note such chars are
# replaced by a space (the note's long-standing tab/newline behaviour, widened to every line break).
_BREAKS = "\t\n\r\x0b\x0c\x1c\x1d\x1e\x85\u2028\u2029"
ALLOWED_FIELDS = {"APPLIED": {"artifact", "validation_ref", "scope"}, "NO-OP": {"scope", "artifact"},
                  "DEFERRED": {"review", "scope"}, "CONTESTED": {"scope", "artifact"}}
TOKEN_KEYS = ("artifact", "validation_ref", "scope", "review")
_TOKEN_LEAD = re.compile(r"^\s*(?:%s)=" % "|".join(TOKEN_KEYS))
_REVIEW_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _utf8_ok(v):
    try:
        v.encode("utf-8")
        return True
    except UnicodeEncodeError:
        return False


def receipt_tokens(action, artifacts, validation_ref, scope, review, today, note=""):
    """Validate the WQ-399 fields and return (prefix, clean_note). die2 on any defect, BEFORE the
    receipts file is opened, so a refused receipt never leaves a partial row or creates the file.
    validation_ref / scope / review accept a str or a list (CLI flags append); more than one is refused."""
    def as_list(v):
        return [] if v is None else (list(v) if isinstance(v, (list, tuple)) else [v])
    given = {"artifact": as_list(artifacts), "validation_ref": as_list(validation_ref),
             "scope": as_list(scope), "review": as_list(review)}
    for k, vals in given.items():
        for v in vals:
            if not _utf8_ok(v):
                die2(f"receipt refused: {FLAG[k]} value is not valid UTF-8. Nothing written.")
            if any(c in v for c in _BREAKS + ";"):
                die2(f"receipt refused: {FLAG[k]} value {v!r} contains ';', a tab, a carriage return or another "
                     f"line break (it would break key=value parsing or the receipts file). Nothing written.")
        given[k] = [v.strip() for v in vals if v.strip()]       # whitespace-only = not given
    for k in ("validation_ref", "scope", "review"):
        if len(given[k]) > 1:
            die2(f"receipt refused: {FLAG[k]} given {len(given[k])} times ({given[k]!r}); give it once. Nothing written.")
    missing = [k for k in REQUIRED_FIELDS.get(action, ()) if not given[k]]
    if missing:
        die2(f"receipt refused: {action} requires {' and '.join(FLAG[k] for k in missing)} "
             f"(WQ-399, Will 2026-10-08). Nothing written. Re-run with the field(s); see "
             f"AGENTS/DAEDALUS/design/2026-10-08_WQ399_RECEIPT_WRITER_ACCEPTANCE.md")
    stray = [k for k in TOKEN_KEYS if given[k] and k not in ALLOWED_FIELDS.get(action, set())]
    if stray:
        die2(f"receipt refused: {' and '.join(FLAG[k] for k in stray)} does not belong on a {action} receipt "
             f"(a later parser would read it as evidence). Nothing written.")
    for a in given["artifact"]:
        if not PTR_RE.match(a):
            die2(f"receipt refused: --artifact {a!r} is not path#key (e.g. AGENTS/X/workbook/KB.tsv#KB-X-12). "
                 f"Nothing written.")
    vr = given["validation_ref"][0] if given["validation_ref"] else None
    if vr and vr != "NONE" and not PTR_RE.match(vr):
        die2(f"receipt refused: --validation-ref {vr!r} is neither NONE nor path#key. Nothing written.")
    rv = given["review"][0] if given["review"] else None
    if rv:
        if not _REVIEW_RE.match(rv):
            die2(f"receipt refused: --review {rv!r} is not YYYY-MM-DD. Nothing written.")
        d = parse_day("--review", rv, "cli")
        if d < today:
            die2(f"receipt refused: --review {rv} is before today {today} — a review date already past "
                 f"is not a deferral. Nothing written.")
    note = note or ""
    if not _utf8_ok(note):
        die2("receipt refused: --note is not valid UTF-8. Nothing written.")
    if _TOKEN_LEAD.match(note):
        die2(f"receipt refused: --note may not begin with a field token ({', '.join(k + '=' for k in TOKEN_KEYS)}); "
             f"use the matching flag so the writer validates it. Nothing written.")
    note = "".join(" " if c in _BREAKS else c for c in note)
    lead = {"DEFERRED": "review", "NO-OP": "scope"}.get(action)
    order = ([lead] if lead else []) + [k for k in ("artifact", "validation_ref", "scope", "review") if k != lead]
    parts = [f"{k}={v}" for k in order for v in given[k]]
    return "".join(p + "; " for p in parts), note


def cmd_receipt(agent, reg_path, rcpt_path, cid, action, note, artifacts=None, validation_ref=None,
                scope=None, review=None, today=None):
    rows = load_register(reg_path)
    if cid not in {r["correction_id"].strip() for r in rows}:
        die2(f"receipt refused: {cid} not in register {reg_path} — a receipt must reference a real row")
    if action not in ACTIONS:
        die2(f"action {action!r} not in {ACTIONS} (A3 enum; CONTESTED escalates via PROME rails)")
    prefix, note = receipt_tokens(action, artifacts, validation_ref, scope, review, today or date.today(), note)
    note = prefix + note
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")  # A2: exact-minute, machine-parseable
    new = not rcpt_path.exists()
    rcpt_path.parent.mkdir(parents=True, exist_ok=True)
    with open(rcpt_path, "a") as f:
        if new:
            f.write("\t".join(RECEIPT_HEADER) + "\n")
        f.write("\t".join([stamp, cid, action, note]) + "\n")
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


# WQ-393 (Will 2026-10-08 ~08:44 ET, "393 - approved"): the R1 row is written by the PUBLISHER in
# the same commit as the correcting signal. The L210 grade measured the write leg at 51.4-60.0%
# because the step lived only in prose; this mode is the mechanical half of the re-rule, so a
# missed row is printed by name at the publisher's closeout instead of found by a 30-day audit.
WQ393_RULING_DATE = "2026-10-08"
SIG_FILE_RE = re.compile(r"^(SIG-W-(\d{4})(\d{2})(\d{2})-\d{3})")
TITLE_MARK_RE = re.compile(r"CORRECTION|RETRACT|ERRATUM|ERRATA|WITHDRAW", re.I)
EXEMPT_RE = re.compile(r"not correction-class", re.I)
# A correcting signal named `...-to-YYYYMMDD-NNN-...` identifies the signal it corrects. The desks
# that RECEIVED the wrong figure are that original's action+info; a row targeting only the
# correction's own routing misses them (10/8: BRENT on -1004-011, HENRY on -1008-009).
CORRECTS_RE = re.compile(r"-to-(?:(\d{8})-)?(\d{3})\b")  # same-day form `-to-NNN` = the correcting date
ROUTE_RE = re.compile(r"^(action|info):\s*\[(.*)\]\s*$")


def board_frontmatter(path):
    """signal_type + dispatch_note from the leading '---' block; ({}, False) if there is none."""
    lines = path.read_text(errors="replace").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, False
    fm = {}
    for ln in lines[1:80]:
        if ln.strip() == "---":
            return fm, True
        k, sep, v = ln.partition(":")
        if sep and k.strip() in ("signal_type", "dispatch_note"):
            fm[k.strip()] = v.strip()
    return fm, False


def cmd_write_compliance(board_dir, reg_path, since):
    """Every correction-class BOARD signal dated >= since must have its id in a register pointer.
    Correction-class = frontmatter `signal_type: correction` OR a title marker (either alone
    counts: on 8/27-10/08 21 typed corrections carried no title marker and 5 title-marked ones
    carried another type). Exempt = `not correction-class` in dispatch_note (BOARD_CONSUMPTION_SPEC
    v0.33 §3.6 item 4: an UPDATE that changes no published figure says so there)."""
    rows = load_register(reg_path)
    registered = {}
    for r in rows:
        for sid in re.findall(r"SIG-W-\d{8}-\d{3}", r.get("pointer") or ""):
            registered[sid] = r
    if not board_dir.is_dir():
        die2(f"BOARD dir not found at {board_dir}")

    def recipients(sid):
        hits = sorted(board_dir.glob(f"{sid}-*.md")) or sorted(board_dir.glob(f"{sid}.md"))
        if not hits:
            return None
        got = set()
        for ln in hits[0].read_text(errors="replace").splitlines()[:80]:
            m2 = ROUTE_RE.match(ln.strip())
            if m2:
                got.update(t.strip().strip("\"'").upper() for t in m2.group(2).split(",") if t.strip())
        return got

    short_targets, unresolved = [], 0
    scanned, owed, exempt, ok_rows, no_fm = 0, [], [], 0, 0
    for f in sorted(board_dir.iterdir()):
        m = SIG_FILE_RE.match(f.name)
        if not m or f.suffix != ".md":
            continue
        try:
            d = date(int(m.group(2)), int(m.group(3)), int(m.group(4)))
        except ValueError:
            die2(f"impossible date in BOARD filename {f.name}")
        if d < since:
            continue
        scanned += 1
        fm, closed = board_frontmatter(f)
        if not closed:
            no_fm += 1
        typed = fm.get("signal_type", "").lower() == "correction"
        titled = bool(TITLE_MARK_RE.search(f.name))
        if not (typed or titled):
            continue
        sid = m.group(1)
        basis = "type+title" if typed and titled else ("type" if typed else "title")
        if sid in registered:
            ok_rows += 1
            cm = CORRECTS_RE.search(f.name)
            orig_id = f"{cm.group(1) or sid[6:14]}-{cm.group(2)}" if cm else None
            orig = recipients(f"SIG-W-{orig_id}") if cm else None
            tgt = registered[sid].get("targets") or ""
            if orig is None:
                unresolved += 1
            elif tgt.strip().upper() != "ALL":
                missing = sorted(orig - {t.strip().upper() for t in tgt.split(",") if t.strip()})
                if missing:
                    short_targets.append((sid, registered[sid].get("correction_id", "?"), orig_id, missing))
        elif EXEMPT_RE.search(fm.get("dispatch_note", "")):
            exempt.append((sid, basis))
        else:
            owed.append((sid, basis, f.name))
    if scanned == 0:
        # PAT-155: an empty population passes every universal check. Zero signals in the window
        # means a wrong --since or an unreadable BOARD, never "fully compliant".
        die2(f"0 SIG-W files dated >= {since} in {board_dir} — window or BOARD path wrong; "
             f"an empty population is not compliance")
    corr = ok_rows + len(exempt) + len(owed)
    head = (f"since {since} · {scanned} BOARD signal(s) scanned · {corr} correction-class "
            f"(signal_type: correction OR title marker) · {ok_rows} with a register row · "
            f"{len(exempt)} exempt (dispatch_note 'not correction-class') · "
            f"{no_fm} without a closed frontmatter block (title-only basis) · "
            f"{ok_rows - unresolved} row(s) target-checked against the corrected signal's recipients, "
            f"{unresolved} not checkable (pointer names no '-to-YYYYMMDD-NNN' original, or it is not on BOARD)")
    if owed or short_targets:
        print(f"R1-WRITE 1 OWED: {len(owed)} correction-class signal(s) with NO register row · "
              f"{len(short_targets)} row(s) whose targets miss a recipient of the corrected signal — {head}")
        for sid, basis, name in owed:
            print(f"  ⛔ NO-ROW {sid} [{basis}] {name[:120]}")
        for sid, cid, orig, missing in short_targets:
            print(f"  ⛔ SHORT-TARGETS {cid} ({sid} corrects SIG-W-{orig}): received the wrong figure, "
                  f"not targeted: {','.join(missing)}")
        print("  → NO-ROW: write the row (BOARD_CONSUMPTION_SPEC §3.6 item 4, same commit as the signal), or put "
              "'not correction-class: <why>' in its dispatch_note if it changes no published figure. "
              "SHORT-TARGETS: add the named desks to `targets` (corrected ∪ correcting recipients)")
        return 1
    print(f"R1-WRITE 0 OK: every correction-class signal has a register row and every checkable row "
          f"targets the corrected signal's recipients — {head}")
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
    # --- WQ-399 (Will 2026-10-08 "399 approve"): the receipt writer requires the 9/17 fields.
    # Acceptance W1–W15, design/2026-10-08_WQ399_RECEIPT_WRITER_ACCEPTANCE.md. Every refusal must
    # leave the receipts file byte-identical (or absent) — asserted, not assumed.
    T = date(2026, 10, 8)
    OLD = "\t".join(RECEIPT_HEADER) + "\n2026-09-08T12:00Z\tCOR-20260920-02\tNO-OP\tfree text, old form\n"

    def run_w(action, prior=None, cid="COR-20260920-02", **kw):
        with tempfile.TemporaryDirectory() as td:
            reg = Path(td) / "reg.tsv"
            reg.write_text("# banner\n" + hdr + "\n" + named_live + "\n")
            rcpt = Path(td) / "r.tsv"
            if prior is not None:
                rcpt.write_text(prior)
            before = rcpt.read_bytes() if rcpt.exists() else None
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                try:
                    rc = cmd_receipt("SAM", reg, rcpt, cid, action, kw.pop("note", ""), today=T, **kw)
                except SystemExit as e:
                    rc = e.code
            after = rcpt.read_bytes() if rcpt.exists() else None
            run_w.prefix_ok = (before is None or after is None or after.startswith(before))
            run_w.out = buf
            last = after.decode().rstrip("\n").split("\n")[-1].split("\t") if after else []
            chk_rc = None
            if after is not None:
                with contextlib.redirect_stdout(io.StringIO()):
                    try:
                        chk_rc = cmd_check("SAM", reg, rcpt, T)
                    except SystemExit as e:
                        chk_rc = e.code
            return rc, before == after, (last[3] if len(last) > 3 else None), buf.getvalue(), chk_rc

    A2 = dict(artifacts=["AGENTS/SAM/a.tsv#1", "AGENTS/SAM/b.md#2"], validation_ref="NONE")
    w399 = [
        # (label, action, kwargs, prior, want_rc, want_unchanged, note_check)
        ("W1 APPLIED without --artifact -> 2, file unchanged", "APPLIED", dict(validation_ref="NONE"), OLD, 2, True, None),
        ("W2 APPLIED without --validation-ref -> 2, unchanged", "APPLIED", dict(artifacts=["A/x.tsv#k"]), OLD, 2, True, None),
        ("W3 NO-OP without --scope -> 2, unchanged", "NO-OP", {}, OLD, 2, True, None),
        ("W4 DEFERRED without --review -> 2, file still absent", "DEFERRED", {}, None, 2, True, None),
        ("W5 DEFERRED --review 2026-13-01 -> 2", "DEFERRED", dict(review="2026-13-01"), OLD, 2, True, None),
        ("W5b DEFERRED --review soon -> 2", "DEFERRED", dict(review="soon"), OLD, 2, True, None),
        ("W6 DEFERRED --review before today -> 2", "DEFERRED", dict(review="2026-10-07"), OLD, 2, True, None),
        ("W7 --artifact without # -> 2", "APPLIED", dict(artifacts=["AGENTS/X/STATUS.md"], validation_ref="NONE"), OLD, 2, True, None),
        ("W8 --validation-ref malformed -> 2", "APPLIED", dict(artifacts=["A/x#k"], validation_ref="see notes"), OLD, 2, True, None),
        ("W9 value with ';' -> 2", "NO-OP", dict(scope="a; b"), OLD, 2, True, None),
        ("W10 APPLIED complete -> 0, tokens in order", "APPLIED", dict(A2, note="x"), OLD, 0, False,
         "artifact=AGENTS/SAM/a.tsv#1; artifact=AGENTS/SAM/b.md#2; validation_ref=NONE; x"),
        ("W10b APPLIED, key with spaces (STATUS.md#BOTTOM LINE) -> 0", "APPLIED",
         dict(artifacts=["AGENTS/SAM/STATUS.md#BOTTOM LINE"], validation_ref="NONE"), OLD, 0, False,
         "artifact=AGENTS/SAM/STATUS.md#BOTTOM LINE; validation_ref=NONE; "),
        ("W7b --artifact with empty key (path#) -> 2", "APPLIED", dict(artifacts=["A/x.tsv#"], validation_ref="NONE"), OLD, 2, True, None),
        ("W11 NO-OP complete -> 0, scope first", "NO-OP", dict(scope="AGENTS/SAM/**", note="none carried"), OLD, 0, False,
         "scope=AGENTS/SAM/**; none carried"),
        ("W12 DEFERRED complete -> 0, review first", "DEFERRED", dict(review="2026-10-15", scope="STATUS"), None, 0, False,
         "review=2026-10-15; scope=STATUS; "),
        ("W13 CONTESTED with no fields -> 0 (unchanged)", "CONTESTED", dict(note="disputed"), OLD, 0, False, "disputed"),
        ("W15 unknown COR-id -> 2 (no regression)", "NO-OP", dict(scope="s", cid="COR-20990101-01"), OLD, 2, True, None),
    ]
    # Legs added after the independent read (mutation testing showed W1–W4/W9/W11/W14/W15 vacuous):
    # each refusal must NAME its cause (msg), and every break character is tested, not only ';'.
    MSG = {"W1": "--artifact", "W2": "--validation-ref", "W3": "--scope", "W4": "--review"}
    w399 += [
        ("W9t tab in --scope -> 2", "NO-OP", dict(scope="a\tb"), OLD, 2, True, None),
        ("W9n newline in --scope -> 2", "NO-OP", dict(scope="a\nb"), OLD, 2, True, None),
        ("W9r carriage return in --artifact (CRLF paste) -> 2", "APPLIED", dict(artifacts=["A/x.tsv#k\r"], validation_ref="NONE"), OLD, 2, True, None),
        ("W9u U+2028 in --validation-ref -> 2", "APPLIED", dict(artifacts=["A/x#k"], validation_ref="A/y#k\u2028z"), OLD, 2, True, None),
        ("W9x non-UTF-8 (surrogate) in --scope -> 2, no file created", "NO-OP", dict(scope="a\udcffb"), None, 2, True, None),
        ("W9note CR and U+2028 in --note -> 0, replaced by spaces", "NO-OP", dict(scope="s", note="a\rb\u2028c"), OLD, 0, False, "scope=s; a b c"),
        ("W11b NO-OP scope + artifact -> scope first", "NO-OP", dict(scope="AGENTS/SAM/**", artifacts=["AGENTS/SAM/k.tsv#K1"]), OLD, 0, False,
         "scope=AGENTS/SAM/**; artifact=AGENTS/SAM/k.tsv#K1; "),
        ("W15b bad action -> 2", "APPLY", dict(artifacts=["A/x#k"], validation_ref="NONE"), OLD, 2, True, None),
        ("W17 whitespace-only --scope counts as missing -> 2", "NO-OP", dict(scope="   "), OLD, 2, True, None),
        ("W18 --validation-ref given twice -> 2", "APPLIED", dict(artifacts=["A/x#k"], validation_ref=["p#q", "NONE"]), OLD, 2, True, None),
        ("W19 --review on an APPLIED receipt -> 2 (stray field)", "APPLIED", dict(artifacts=["A/x#k"], validation_ref="NONE", review="2026-10-15"), OLD, 2, True, None),
        ("W20 --note beginning artifact= -> 2 (forged token)", "NO-OP", dict(scope="s", note="artifact=fake#1; x"), OLD, 2, True, None),
        ("W21 --review with a time suffix -> 2", "DEFERRED", dict(review="2026-10-15T23:59Z"), OLD, 2, True, None),
    ]
    print("SELFTEST WQ-399 — the receipt writer requires the 9/17 fields; a refusal writes nothing:")
    for label, action, kw, prior, want, unchanged, note_want in w399:
        kw = dict(kw); cid = kw.pop("cid", "COR-20260920-02")
        got, same, note_got, out, chk_rc = run_w(action, prior, cid=cid, **kw)
        good = got == want and same == unchanged and (note_want is None or note_got == note_want)
        need = MSG.get(label.split()[0])
        if need:         # W1–W4: the refusal names the missing flag and writes nothing
            good = good and need in out and "Nothing written" in out
        if want == 0:    # W14: the old free-text row and the new token row still parse together,
            good = good and chk_rc == 0 and run_w.prefix_ok    # and every prior byte is preserved
        ok = ok and good
        npass += good
        extra = "" if good else f" | unchanged={same} note={note_got!r} check_rc={chk_rc} out={out.strip()[:160]!r}"
        print(f"  {'PASS' if good else 'FAIL'}  {label}: rc={got} (want {want}){extra}")
    total = len(cases) + len(d4) + len(w399)
    print(f"SELFTEST {'0 PASS' if ok else '1 FAIL'}: {npass}/{total} cases")
    return 0 if ok else 1


def main():
    p = argparse.ArgumentParser()
    p.add_argument("agent", nargs="?")
    p.add_argument("--receipt"); p.add_argument("--action"); p.add_argument("--note", default="")
    p.add_argument("--artifact", action="append"); p.add_argument("--validation-ref", action="append")
    p.add_argument("--scope", action="append"); p.add_argument("--review", action="append")
    p.add_argument("--coverage", action="store_true")
    p.add_argument("--write-compliance", action="store_true")
    p.add_argument("--since", default=WQ393_RULING_DATE); p.add_argument("--board")
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--register"); p.add_argument("--receipts"); p.add_argument("--today")
    a = p.parse_args()
    if a.selftest:
        sys.exit(cmd_selftest())
    reg = Path(a.register) if a.register else ROOT / "AGENTS/WALTER/registry/CORRECTIONS.tsv"
    if a.coverage:
        sys.exit(cmd_coverage(ROOT, reg))
    if a.write_compliance:
        board = Path(a.board) if a.board else ROOT / "BOARD"
        sys.exit(cmd_write_compliance(board, reg, parse_day("--since", a.since, "cli")))
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
        # The write path ignores --today: a fixture override must not admit a past --review into a real
        # receipts file (independent read 2026-10-08 ⚠️). Selftests pass `today` to cmd_receipt directly.
        sys.exit(cmd_receipt(a.agent, reg, rcpt, a.receipt, a.action or "", a.note, a.artifact,
                             a.validation_ref, a.scope, a.review, None))
    sys.exit(cmd_check(a.agent, reg, rcpt, today))


if __name__ == "__main__":
    main()
