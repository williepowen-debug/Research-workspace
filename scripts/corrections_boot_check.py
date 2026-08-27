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
  1  >=1 unreceipted NAMED row still live (block-class; EVERY instance printed, count-first)
  2  CANNOT-EVALUATE — register absent (expected pre-creation state, loud), required header
     column missing, unparseable date in ANY row (A2: NEVER a silent row-skip), or
     unparseable receipts file. Loud, never silent-green.
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


def receipts_path(agent, root):
    base = root / "PROME" if agent == "PROME" else root / "AGENTS" / agent
    return base / "registry" / "corrections_receipts.tsv"


def read_tsv(path, required, label):
    try:
        # WALTER house style opens registry files with a '#' banner block before the real
        # header (FALSIFICATION_FIRED_LOG form; CORRECTIONS.tsv ships the same way) — skip
        # every '#' line, then DictReader sees the true header.
        text = "\n".join(l for l in path.read_text().splitlines() if not l.startswith("#"))
        rows = list(csv.DictReader(io.StringIO(text), delimiter="\t"))
    except Exception as e:
        die2(f"{label} unparseable ({e}) at {path}")
    if rows:
        missing = [c for c in required if c not in rows[0]]
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
            receipts.add(r.get("correction_id", "").strip())
    named_block, all_warn, dead, malformed = [], [], [], []
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
        if r["status"].strip().upper() in ("RETIRED", "DEAD-AT-CAP"):
            continue  # terminal by owner declaration (A3 in-header enum); prune is WALTER's half
        if is_all and cap is None:
            # Ruling: date_cap is MANDATORY on ALL-rows. Missing != unparseable, so this
            # WARNS loudly rather than rc=2 (deliberate asymmetry, declared here: the desk's
            # receipts CAN still be evaluated; the schema breach is WALTER's half to fix).
            malformed.append(cid)
        if cap is not None and cap < today:
            if cid not in receipts:
                dead.append(cid)  # feeds checkpoint leg (d): dead-at-cap with zero receipts
            continue
        if cid in receipts:
            continue
        (all_warn if is_all else named_block).append((cid, r["pointer"], r["status"], r["date"]))
    for cid in malformed:
        print(f"  MALFORMED ALL-row {cid}: date_cap MISSING (mandatory per ruling) — flag WALTER")
    if dead:
        print(f"  INFO {len(dead)} dead-at-cap with no receipt from this desk: {', '.join(dead)}")
    if all_warn:
        print(f"  WARN {len(all_warn)} broadcast ALL-row(s) unreceipted (warn-never-block):")
        for cid, ptr, st, d in all_warn:
            print(f"       {cid} [{st}] {d} -> {ptr}")
    if named_block:
        print(f"CORRECTIONS-CHECK 1 BLOCK: {len(named_block)} NAMED correction(s) unreceipted for {agent}:")
        for cid, ptr, st, d in named_block:
            print(f"       {cid} [{st}] {d} -> read {ptr}, then receipt: "
                  f"corrections_boot_check.py {agent} --receipt {cid} --action <APPLIED|NO-OP|DEFERRED|CONTESTED>")
        return 1
    print(f"CORRECTIONS-CHECK 0 OK: 0 unreceipted NAMED rows for {agent} "
          f"(register {len(rows)} row(s), {len(all_warn)} ALL-warn, {len(dead)} dead-at-cap; "
          f"receipts on file: {len(receipts)}) — PASS covers the register at {reg_path}, nothing else")
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
        charter = (root / "PROME" if d == "PROME" else root / "AGENTS" / d) / "CLAUDE.md"
        (wired if charter.exists() and "corrections_boot_check" in charter.read_text() else unwired).append(d)
    pct = 100 * len(wired) // len(desks) if desks else 0
    print(f"R1 BOOT-LEG COVERAGE: {len(wired)}/{len(desks)} active+tier-2 desks wired = {pct}% "
          f"(checkpoint 2026-09-26 needs >=80%); register {'EXISTS' if reg_path.exists() else 'NOT YET CREATED (WALTER)'}")
    print(f"  wired: {', '.join(wired) or '(none)'}")
    print(f"  unwired ({len(unwired)}): {', '.join(unwired) or '(none)'}")
    return 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument("agent", nargs="?")
    p.add_argument("--receipt"); p.add_argument("--action"); p.add_argument("--note", default="")
    p.add_argument("--coverage", action="store_true")
    p.add_argument("--register"); p.add_argument("--receipts"); p.add_argument("--today")
    a = p.parse_args()
    reg = Path(a.register) if a.register else ROOT / "AGENTS/WALTER/registry/CORRECTIONS.tsv"
    if a.coverage:
        sys.exit(cmd_coverage(ROOT, reg))
    if not a.agent:
        p.error("agent name required (or --coverage)")
    rcpt = Path(a.receipts) if a.receipts else receipts_path(a.agent, ROOT)
    today = parse_day("--today", a.today, "cli") if a.today else date.today()
    if a.receipt:
        sys.exit(cmd_receipt(a.agent, reg, rcpt, a.receipt, a.action or "", a.note))
    sys.exit(cmd_check(a.agent, reg, rcpt, today))


if __name__ == "__main__":
    main()
