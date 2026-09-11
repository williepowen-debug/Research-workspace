#!/usr/bin/env python3
"""wq_ledger.py — the append-only EVENT ledger for PROME/WILL_QUEUE.md (WQ-203, Will 2026-09-10).

One row per EVENT (BACKFILL · REGISTERED · RULED · DECLINED · CLOSED · UPDATED); the current state of
WQ-n is its LAST row. Rows are never edited or deleted — a correction is a new UPDATED event.
Every queue row is parsed by `decision_deck.py` (ONE parser in the fleet); this file owns no queue regex.

  backfill   one-time: one BACKFILL event per WQ number the deck sees today (live OPEN + RECENTLY DONE +
             the archives, first-seen-wins as the deck orders them). Refuses if the ledger has rows.
  sync       idempotent: appends an event only where the live queue's state differs from the last event.
  check      rc 0 ok · 1 blocking (schema / vocabulary / dates / order / dup) · 2 unknown execution.
  state      one line per WQ number: the current state (last event).
  --selftest frozen fixture under PROME/tools/tests/fixtures/wq_ledger/ (never the live queue).

Counts are printed by the commands, never typed into prose (measure with `wq_ledger.py state | wc -l`).
`--ledger <path>` points every command at another file — the way to exercise the tool safely (a /tmp copy);
the live registry is the default. The `.crc` sidecar beside the ledger holds `<rows>\t<crc32>` from the last
tool write; `check` verifies BOTH (crc32 is a change detector, not a cryptographic seal — git history of the
committed pair is the outer audit).
"""
from __future__ import annotations
import argparse, csv, datetime as dt, io, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import decision_deck as dd  # noqa: E402  (ROOT, Q, ARCH, parse_open, parse_decided, title_of, strip_md, verbatim_of)

ROOT = dd.ROOT
LEDGER = ROOT / "PROME/registry/WQ_LEDGER.tsv"
FIXTURE = HERE / "tests/fixtures/wq_ledger"
SCHEMA = ["wq", "event", "at", "title", "type", "needed_by", "since", "status_after", "verdict",
          "will_verbatim", "rec", "record", "source", "written_at"]
HEADER = "\t".join(SCHEMA)
EVENTS = {"BACKFILL", "REGISTERED", "RULED", "DECLINED", "CLOSED", "UPDATED"}
STATES = {"OPEN", "ANSWERED-OWED", "BLOCKED", "ANSWERED-BLOCKED", "RULED", "DECLINED", "CLOSED"}
# verdict = the lead token the fleet wrote, kept as written; status_after is the 6-way state it maps to
VERDICTS = {"APPROVE", "RULED", "DECLINE", "CLOSED-BY-PROME", "OVERTAKEN", "RESOLVED", "EXECUTED", "SUPERSEDED", "WITHDRAWN", "TERMINAL", "DONE", "—"}
TERMINAL = {"RULED", "DECLINED", "CLOSED"}


def now_stamp() -> str:
    """The clock, never narrative (ET, minute precision)."""
    try:
        out = subprocess.run(["date", "+%Y-%m-%d %H:%M"], capture_output=True, text=True, check=True).stdout.strip()
        return out
    except Exception:
        return dt.datetime.now().strftime("%Y-%m-%d %H:%M")


def clean(s: str, n: int | None) -> str:
    s = dd.strip_md(s or "").replace("\t", " ").replace("\n", " ").strip()
    return s if n is None or len(s) <= n else s[: n - 1] + "…"


def date_of(s: str, year_hint: int = 2026) -> str:
    """YYYY-MM-DD from a cell: ISO if present, else M/D → the hint year, else EMPTY."""
    m = re.search(r"\d{4}-\d{2}-\d{2}", s or "")
    if m:
        return m.group(0)
    m = re.search(r"\b(\d{1,2})/(\d{1,2})\b", s or "")
    if m:
        return f"{year_hint}-{int(m.group(1)):02d}-{int(m.group(2)):02d}"
    return ""


# ---------------------------------------------------------------- live state (through the deck's parsers)

def status_of_open(r: dict) -> str:
    if r.get("blocked") and r.get("answered"):
        return "ANSWERED-BLOCKED"
    if r.get("blocked"):
        return "BLOCKED"
    if r.get("answered"):
        return "ANSWERED-OWED"
    return "OPEN"


# lead token (as the deck reads it) → (status_after, verdict) — the mapping table of the plan
MAP = {"DECLINED": ("DECLINED", "DECLINE"), "RULED": ("RULED", "RULED"), "APPROVED": ("RULED", "APPROVE"),
       "RATIFIED": ("RULED", "RULED"), "CLOSED": ("CLOSED", "CLOSED-BY-PROME"), "OVERTAKEN": ("CLOSED", "OVERTAKEN"),
       "RESOLVED": ("CLOSED", "RESOLVED"), "EXECUTED": ("CLOSED", "EXECUTED"), "SUPERSEDED": ("CLOSED", "SUPERSEDED"),
       "WITHDRAWN": ("CLOSED", "WITHDRAWN"), "TERMINAL": ("CLOSED", "TERMINAL"), "DONE": ("CLOSED", "DONE"), "": ("CLOSED", "—")}


def status_of_done(r: dict) -> tuple[str, str]:
    """(status_after, verdict) from the LEAD of the record cell, read by `decision_deck.verdict_of`."""
    tok, approve = dd.verdict_of(r.get("record") or "")
    st, verdict = MAP.get(tok, ("CLOSED", "—"))
    if approve and st == "RULED":
        verdict = "APPROVE"
    return st, verdict


def live_state(q_path: Path | None = None, arch: list[str] | None = None) -> dict[str, dict]:
    """wq → the state the deck sees now. Live OPEN wins over decided (a row can be both mid-rotation)."""
    text = (q_path or dd.Q).read_text(encoding="utf-8")
    out: dict[str, dict] = {}
    # The ledger NEVER feeds itself: always parse the PRIMARY sources (queue + archives), never the deck's
    # ledger-first path — otherwise sync re-reads its own truncated cells and drifts (found at install, 9/11).
    for r in dd.parse_decided(q_path=q_path, arch=arch, ledger=Path("/nonexistent")):
        st, verdict = status_of_done(r)
        out[r["n"]] = {
            "wq": r["n"], "title": clean(r["name"], 120), "type": "", "needed_by": "", "since": "",
            "status_after": st, "verdict": verdict,
            "will_verbatim": clean(dd.verbatim_of(r.get("record", "")), 400),
            # Conditions at the end of a ruling are part of the record. The
            # deck prefers this ledger, so truncating here hides those terms.
            "rec": "", "record": clean(r.get("record", ""), None), "source": r.get("source", ""),
            "at": date_of(r.get("done", "")) or date_of(r.get("record", "")),
        }
    for r in dd.parse_open(text):
        out[r["n"]] = {
            "wq": r["n"], "title": clean(dd.item_name(r.get("item", "")), 120), "type": clean(r["kind"], 40),
            "needed_by": r.get("by") or clean(r.get("by_raw", ""), 40), "since": clean(r.get("since", ""), 40),
            "status_after": status_of_open(r), "verdict": "—",
            "will_verbatim": clean(dd.verbatim_of(r.get("item", "") + " " + r.get("notes", "")), 400),
            "rec": clean(r.get("rec", ""), None), "record": "", "source": "WILL_QUEUE.md § OPEN",
            "at": date_of(r.get("since", "")) or (dd.first_date(r.get("item", "")) or ""),
        }
    return out


# ---------------------------------------------------------------- ledger io

def read_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        rd = csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        return [dict(r) for r in rd]


def last_state(rows: list[dict]) -> dict[str, dict]:
    st: dict[str, dict] = {}
    for r in rows:  # file order = time order (append-only)
        st[r["wq"]] = r
    return st


def crc_path(path: Path) -> Path:
    return path.with_suffix(".crc")

def seal(path: Path) -> None:
    """Append-only enforcement (I1): after every tool write, store rows + crc32 of the WHOLE file in a sidecar.
    `check` recomputes; any hand edit, deletion or reorder since the last tool write fails it. The tool itself
    only ever opens the ledger in append mode."""
    import zlib
    raw = path.read_bytes()
    rows = sum(1 for l in raw.split(b"\n")[1:] if l)
    crc_path(path).write_text(f"{rows}\t{zlib.crc32(raw) & 0xffffffff}\n", encoding="utf-8")

def seal_ok(path: Path) -> bool:
    """True when the ledger's bytes match its last tool write (or the ledger does not exist yet)."""
    import zlib
    if not path.exists():
        return not crc_path(path).exists()
    if path.stat().st_size == 0 and not crc_path(path).exists():
        return True
    try:
        rows_s, crc_s = crc_path(path).read_text(encoding="utf-8").split()
        return int(crc_s) == (zlib.crc32(path.read_bytes()) & 0xffffffff)
    except (FileNotFoundError, ValueError):
        return False


class SealBroken(RuntimeError):
    pass


def append(path: Path, events: list[dict]) -> int:
    """Refuses to write over a broken seal — an append would otherwise LAUNDER a tampered prior row
    (result read ❌8). Remedy is never by hand: `git checkout -- <ledger> <ledger>.crc` restores the last
    committed truth, then re-run sync."""
    if not seal_ok(path):
        raise SealBroken(f"seal broken on {path} — restore with `git checkout -- {path} {crc_path(path)}` then re-run sync; never edit by hand")
    if not events:
        return 0
    new = not path.exists() or path.stat().st_size == 0
    with path.open("a", encoding="utf-8", newline="") as f:
        if new:
            f.write(HEADER + "\n")
        for e in events:
            f.write("\t".join((e.get(c, "") or "").replace("\t", " ").replace("\n", " ") for c in SCHEMA) + "\n")
    seal(path)
    return len(events)


def event_row(kind: str, s: dict, at: str | None = None) -> dict:
    e = dict(s)
    e["event"] = kind
    # `at` = the row's own date when it carries one; a BACKFILL of an undated row stays EMPTY (never today)
    e["at"] = at or s.get("at") or ("" if kind == "BACKFILL" else now_stamp()[:10])
    e["written_at"] = now_stamp()
    return e


# ---------------------------------------------------------------- commands

def cmd_backfill(ledger: Path, q_path=None, arch=None) -> int:
    if read_rows(ledger):
        print(f"WQ-LEDGER ✗ rc 1 — {ledger} already has rows; backfill is one-time (use sync)")
        return 1
    live = live_state(q_path, arch)
    events = [event_row("BACKFILL", s) for _, s in sorted(live.items(), key=lambda kv: sort_key(kv[0]))]
    n = append(ledger, events)
    x = cross_count(q_path, arch)
    flag = "" if x == len(live) else f"  ⚠️ CROSS-COUNT MISMATCH: a plain first-cell regex over the same files finds {x} distinct numbers — inspect before trusting the backfill"
    print(f"WQ-LEDGER ✓ backfill → {ledger}: {n} BACKFILL row(s) ({len(live)} distinct WQ numbers seen by the deck; plain-regex cross-count {x}){flag}")
    return 0 if not flag else 1


def cross_count(q_path=None, arch=None) -> int:
    """Parser-independent cross-check: distinct row numbers by a plain first-cell regex over the same files.
    Zero free parameters; it must equal the deck's count or the backfill receipt flags it (plan I3)."""
    files = [q_path or dd.Q] + [Path(f) for f in (dd.ARCH if arch is None else arch)]
    seen = set()
    for f in files:
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\|\s*\**\s*(\d+[a-z]?)\b", line)
            if m and not line.lower().startswith("| #") and not line.lower().startswith("| item"):
                seen.add(m.group(1))
    return len(seen)


def diff_state(prev: dict | None, cur: dict) -> str | None:
    """Which event (if any) takes the ledger from prev to cur."""
    if prev is None:
        return "REGISTERED"
    if prev["status_after"] != cur["status_after"]:
        if cur["status_after"] in TERMINAL:
            return {"RULED": "RULED", "DECLINED": "DECLINED", "CLOSED": "CLOSED"}[cur["status_after"]]
        return "UPDATED"
    for k in ("needed_by", "verdict", "will_verbatim", "title", "type", "since", "rec", "record"):
        if (prev.get(k) or "") != (cur.get(k) or ""):
            return "UPDATED"
    return None


def cmd_sync(ledger: Path, q_path=None, arch=None) -> int:
    if not seal_ok(ledger):
        print(f"WQ-LEDGER ✗ rc 1 — SEAL BROKEN on {ledger}: nothing appended. Restore: `git checkout -- {ledger} {crc_path(ledger)}`, then re-run sync. Never edit the ledger by hand.")
        return 1
    rows = read_rows(ledger)
    if not rows:
        print("WQ-LEDGER ✗ rc 1 — empty ledger; run backfill first")
        return 1
    prev = last_state(rows)
    live = live_state(q_path, arch)
    events = []
    for wq in sorted(live, key=sort_key):
        kind = diff_state(prev.get(wq), live[wq])
        if kind:
            events.append(event_row(kind, live[wq], at=now_stamp()[:10] if kind != "REGISTERED" else (live[wq].get("at") or now_stamp()[:10])))
    n = append(ledger, events)
    print(f"WQ-LEDGER ✓ sync → {ledger}: {n} event(s) appended (" + ", ".join(f"{e['event']} WQ-{e['wq']}" for e in events) + ")" if n else f"WQ-LEDGER ✓ sync → {ledger}: 0 events (ledger matches the queue)")
    return 0


def cmd_check(ledger: Path) -> int:
    try:
        raw = ledger.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"WQ-LEDGER ✗ rc 1 — {ledger} missing"); return 1
    lines = raw.split("\n")
    probs = []
    if lines[0] != HEADER:
        probs.append("L1: header is not the schema string")
    previous_event = {}; last_written = ""
    for i, l in enumerate(lines[1:], start=2):
        if not l:
            continue
        c = l.split("\t")
        if len(c) != len(SCHEMA):
            probs.append(f"L{i}: {len(c)} columns, expected {len(SCHEMA)}"); continue
        r = dict(zip(SCHEMA, c))
        if r["event"] not in EVENTS: probs.append(f"L{i}: event '{r['event']}' not in vocabulary")
        if r["status_after"] not in STATES: probs.append(f"L{i}: status_after '{r['status_after']}' not in vocabulary")
        if r["at"] and not re.fullmatch(r"\d{4}-\d{2}-\d{2}( \d{2}:\d{2})?", r["at"]): probs.append(f"L{i}: at '{r['at']}' does not parse")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", r["written_at"]): probs.append(f"L{i}: written_at '{r['written_at']}' does not parse")
        elif r["written_at"] < last_written: probs.append(f"L{i}: written_at goes backwards ({r['written_at']} < {last_written})")
        else: last_written = r["written_at"]
        # Several real corrections can share a day, status, and even minute.
        # Reject repeated payloads for the same WQ, not distinct updates. A
        # later return to an earlier state after an intervening change is valid.
        key = tuple(r[c] for c in SCHEMA if c != "written_at")
        if previous_event.get(r["wq"]) == key:
            probs.append(f"L{i}: duplicate event for WQ-{r['wq']}")
        previous_event[r["wq"]] = key
    for l_i, l in enumerate(lines[1:], start=2):
        if l:
            c = l.split("\t")
            if len(c) == len(SCHEMA) and c[8] not in VERDICTS:
                probs.append(f"L{l_i}: verdict '{c[8]}' not in vocabulary")
    try:
        import zlib
        rows_s, crc_s = crc_path(ledger).read_text(encoding="utf-8").split()
        raw = ledger.read_bytes()
        if int(crc_s) != (zlib.crc32(raw) & 0xffffffff):
            probs.append(f"SEAL: the ledger's bytes differ from the last tool write (hand edit, deletion or reorder) — append-only broken; restore: `git checkout -- {ledger} {crc_path(ledger)}` then re-run sync")
        elif int(rows_s) != sum(1 for l in raw.split(b"\n")[1:] if l):
            probs.append("SEAL: sidecar row count disagrees with the file (seal written by something other than the tool)")
    except FileNotFoundError:
        probs.append("SEAL: sidecar .crc missing — every tool write seals; a missing seal means a non-tool write")
    except ValueError:
        probs.append("SEAL: sidecar .crc malformed")
    if probs:
        print(f"WQ-LEDGER ✗ rc 1 — {len(probs)} problem(s) in {ledger}:")
        for p in probs[:40]: print("  " + p)
        return 1
    n = sum(1 for l in lines[1:] if l)
    print(f"WQ-LEDGER ✓ {ledger}: {n} event row(s) × {len(SCHEMA)} columns; append-only order holds")
    return 0


def cmd_state(ledger: Path) -> int:
    st = last_state(read_rows(ledger))
    for wq in sorted(st, key=sort_key):
        r = st[wq]
        print(f"WQ-{wq}\t{r['status_after']}\t{r['verdict']}\t{r['at']}\t{r['title'][:70]}")
    return 0


def sort_key(n: str):
    m = re.match(r"(\d+)([a-z]?)", n)
    return (int(m.group(1)), m.group(2)) if m else (10**9, n)


# ---------------------------------------------------------------- selftest (frozen fixture, never the live queue)

def selftest() -> int:
    fq = FIXTURE / "WILL_QUEUE.md"; fa = [str(FIXTURE / "WILL_QUEUE_ROWS_2026-09-01_rolloff.md")]
    if not fq.exists():
        print("WQ-LEDGER ✗ rc 2 — fixture missing: " + str(fq)); return 2
    ok = True
    def chk(name, cond, detail=""):
        nonlocal ok
        print(("  ✓ " if cond else "  ✗ ") + name + (f" — {detail}" if detail else ""))
        ok = ok and bool(cond)
    with tempfile.TemporaryDirectory() as td:
        led = Path(td) / "WQ_LEDGER.tsv"
        chk("backfill runs", cmd_backfill(led, fq, fa) == 0)
        rows = read_rows(led)
        chk("backfill = 4 WQ numbers from the fixture (2 open + 1 recently done + 1 archived)", len(rows) == 4, f"{len(rows)}")
        st = last_state(rows)
        chk("open row → OPEN", st.get("901", {}).get("status_after") == "OPEN")
        chk("answered row → ANSWERED-OWED with the verbatim word", st.get("902", {}).get("status_after") == "ANSWERED-OWED" and "go ahead" in st.get("902", {}).get("will_verbatim", ""))
        chk("recently-done DECLINE → DECLINED", st.get("903", {}).get("status_after") == "DECLINED")
        chk("archived RULED → RULED / APPROVE", st.get("904", {}).get("status_after") == "RULED" and st["904"]["verdict"] == "APPROVE")
        chk("second backfill refused", cmd_backfill(led, fq, fa) == 1)
        n0 = len(read_rows(led)); cmd_sync(led, fq, fa); n1 = len(read_rows(led))
        chk("sync on an unchanged queue appends 0 rows (I5)", n1 == n0, f"{n1 - n0}")
        # mutate a copy of the fixture: 901 gets ruled
        fq2 = Path(td) / "WILL_QUEUE.md"
        txt = fq.read_text(encoding="utf-8").replace("| 901 | **Fixture open row",
              "| 901 | **Will APPROVED 2026-09-11 12:00 ET, verbatim *\"yes do it\"* — hands owed. Fixture open row")
        fq2.write_text(txt, encoding="utf-8")
        cmd_sync(led, fq2, fa); rows = read_rows(led)
        chk("a ruled lead appends exactly one UPDATED/RULED-class event", len(rows) == n1 + 1, f"{len(rows) - n1}")
        chk("…and the new state is ANSWERED-OWED (still OPEN in the table = hands owed)", last_state(rows)["901"]["status_after"] == "ANSWERED-OWED")
        cmd_sync(led, fq2, fa)
        chk("sync twice after the change appends 0 (I5)", len(read_rows(led)) == n1 + 1)
        chk("check passes on the fixture ledger", cmd_check(led) == 0)
        bad = led.read_text(encoding="utf-8").replace("\tBACKFILL\t", "\tBOGUS\t", 1); bp = Path(td) / "bad.tsv"; bp.write_text(bad, encoding="utf-8"); seal(bp)
        chk("check FAILS on a bad event token alone (sealed copy — the vocabulary leg, not the seal, fires)", cmd_check(bp) == 1)
        # laundering: a tampered prior row must NOT be re-sealed by the next append
        raw = led.read_text(encoding="utf-8"); led.write_text(raw.replace("Fixture open row", "Fixture open row TAMPERED", 1), encoding="utf-8")
        chk("sync REFUSES to append over a broken seal (no laundering, ❌8)", cmd_sync(led, fq2, fa) == 1 and "TAMPERED" in led.read_text(encoding="utf-8") and cmd_check(led) == 1)
        led.write_text(raw, encoding="utf-8")
        chk("restored bytes pass check again (the remedy is restore, never repair)", cmd_check(led) == 0)
        # lead classifier: tokens deep in a cell are narrative, not the verdict (❌10–13)
        cases = [("**RULED 2026-09-01 — Will APPROVE, verbatim *\"ok go forward approved\"* … later the doorbells PROME declined …", ("RULED", "APPROVE")),
                 ("**CLOSED 2026-09-10 18:0x ET by PROME — OVERTAKEN, no ruling needed … Will DECLINED them as WQ-200", ("CLOSED", "OVERTAKEN")),
                 ("**RULED 2026-09-10 20:16 ET — Will APPROVE (tap) … KB-CRU-042 SUPERSEDED", ("RULED", "APPROVE")),
                 ("~~old name~~ **DONE 8/6 — ran as a spawn** rather than self-approve an escalation", ("CLOSED", "DONE")),
                 ("**DECLINED 2026-09-10 — Will DECLINE (tap), note verbatim: *\"no\"*", ("DECLINED", "DECLINE")),
                 ("Deck tap 2026-09-10 12:42 ET (16:42Z): Will APPROVE = the confirmation asked for; consumed", ("RULED", "APPROVE")),
                 ("UNGATED self-rulable (DELEGATION_TIER landed); owner told 8/12 — left per its own clause", ("CLOSED", "—"))]
        chk("lead classifier: 7 adversarial cells map by their LEAD, not by a token deep in the cell",
            all(status_of_done({"record": rec}) == want for rec, want in cases), str([status_of_done({"record": rec}) for rec, _ in cases]))
        # append-only seal: a hand edit of a prior row must fail check
        raw = led.read_text(encoding="utf-8"); edited = raw.replace("Fixture open row", "Fixture open row EDITED", 1)
        led.write_text(edited, encoding="utf-8")
        chk("check FAILS after a hand edit of a prior row (I1 seal)", cmd_check(led) == 1)
        led.write_text(raw, encoding="utf-8")
        chk("check passes again once the bytes are restored", cmd_check(led) == 0)
        # isolation: the fixture run must never see the LIVE registry ledger through the deck
        chk("live_state ignores any ledger (primary sources only)", "ledger" not in {s["source"] for s in live_state(fq, fa).values()})
    print("WQ-LEDGER selftest " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", nargs="?", choices=["backfill", "sync", "check", "state"])
    ap.add_argument("--ledger", default=str(LEDGER))
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    led = Path(a.ledger)
    try:
        if a.cmd == "backfill": return cmd_backfill(led)
        if a.cmd == "sync": return cmd_sync(led)
        if a.cmd == "check": return cmd_check(led)
        if a.cmd == "state": return cmd_state(led)
    except Exception as e:  # rc 2 = unknown execution, never a silent 0
        print(f"WQ-LEDGER ✗ rc 2 — EXCEPTION {type(e).__name__}: {e}"); return 2
    ap.print_help(); return 2


if __name__ == "__main__":
    sys.exit(main())
