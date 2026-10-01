#!/usr/bin/env python3
"""PROME BOARD consumption pass — the PULL that makes a §3.5 exemption sound.

WALTER's BOARD_CONSUMPTION_SPEC §3.5 grants a "pull-complete" exemption (WALTER
stops writing inbox handoffs) ONLY to a recipient that runs a *complete,
ID-level* BOARD disposition pass. §3.5.1 states the reasoning explicitly: the
exemption is sound *only because* the recipient's pass IS the pull, so the
handoff is pure redundancy. No pull -> no exemption. This script is PROME's pull.

Scope: EVERY published BOARD signal PROME has not consumed, not a tier or a
sample (REGINALD was refused the exemption in v0.7 precisely because its scan
was tiered).

TWO DEFINITIONS THIS TOOL RESTS ON (2026-09-30 repair, CATO review RC1 —
acceptance: PROME/tools/tests/ACCEPTANCE_board_scan_publication_2026-09-30.md):

  PUBLISHED = the signal file is committed at HEAD and unmodified in the
      working tree. WALTER stamps a signal in the same command as its commit,
      so the commit is the publication act. A file on disk that is untracked,
      staged or modified is a DRAFT: it is reported as held back and is never
      consumed, whatever flag is passed. BOARD/INDEX.md is NOT read.

  CONSUMED = the file's stem is recorded in PROME/state/board_consumed.tsv.
      The pass is a diff of published files against that ledger, so a signal
      published late with a LOWER id than ones already consumed still
      surfaces. board_cursor.txt is kept as a display high-water mark only.

A published, unconsumed file whose metadata is incomplete (no closed
frontmatter, signal_id missing or not matching the filename, action/info not
bracketed lists, empty time_dispatched) is UNREADABLE: its routing is unknown,
so it is a hard stop (rc 1) exactly like an action line, never a silent consume.

Usage:
    python3 PROME/tools/board_scan.py                 # scan, write nothing
    python3 PROME/tools/board_scan.py --advance       # scan, then record consumption
    python3 PROME/tools/board_scan.py --since 20260724
    python3 PROME/tools/board_scan.py --audit 20260701   # ACTION-line audit

Exit codes: 0 = nothing new or info-only; 1 = PROME is on an ACTION line, a late
action landed on a consumed signal, or a published signal is unreadable (boot
must not proceed past this without dispositioning); 2 = the scan could not run
(no BOARD, git unavailable, ledger unreadable) — nothing is written.
"""
import argparse
import os
import pathlib
import re
import subprocess
import sys
import tempfile

REPO = pathlib.Path(
    subprocess.run(["git", "rev-parse", "--show-toplevel"],
                   capture_output=True, text=True, check=True).stdout.strip())
BOARD = REPO / "BOARD"
CURSOR = REPO / "PROME" / "state" / "board_cursor.txt"
LEDGER = REPO / "PROME" / "state" / "board_consumed.tsv"

SIG_RE = re.compile(r"^SIG-W-(\d{8})-(\d+)")
ME = "PROME"
FLAGS = {"A", "I", "O", "U"}   # action (acked) · info · other · unreadable (acked by hand)
LEDGER_HEADER = (
    "# PROME/state/board_consumed.tsv — every BOARD signal file board_scan.py has consumed.\n"
    "# One row per FILE: <file stem><TAB><class>  (A = PROME on action, acknowledged · I = info · "
    "O = not routed to PROME · U = unreadable, acknowledged by hand).\n"
    "# Written ONLY by `board_scan.py --advance`; never hand-edit. A file absent from this list "
    "is unconsumed and will surface at the next scan once it is published (committed).\n")


class ScanError(Exception):
    """The scan cannot run. Callers return rc 2 and write nothing."""


def parse_front(path):
    """Minimal frontmatter reader. Returns {} if the file has no --- block."""
    out = {}
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return out
    if not text.startswith("---"):
        return out
    end = text.find("\n---", 3)
    if end == -1:
        return out
    for line in text[3:end].splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        k, v = k.strip(), v.strip()
        if v.startswith("[") and v.endswith("]"):
            out[k] = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
        else:
            out[k] = v
    # headline = first markdown H1 after the frontmatter
    m = re.search(r"^# (.+)$", text[end:], re.MULTILINE)
    out["_headline"] = m.group(1).strip() if m else ""
    return out


def sig_key(name):
    m = SIG_RE.match(name)
    return (m.group(1), int(m.group(2))) if m else ("", 0)


def load_cursor():
    if CURSOR.exists():
        return CURSOR.read_text(encoding="utf-8").strip()
    return ""


def clean(s, n=104):
    s = re.sub(r"[*`_]|<[^>]+>", "", s or "").strip()
    s = re.sub(r"\s+", " ", s)
    return s[: n - 1] + "…" if len(s) > n else s


def _names(fm, key):
    """Upper-cased routing names for `key`, or [] when the cell is not a bracketed list."""
    v = fm.get(key)
    return [a.upper() for a in v] if isinstance(v, list) else []


def metadata_problems(path, fm):
    """Why a published file cannot be trusted to say who it is routed to ([] = complete)."""
    if not fm:
        return ["no closed frontmatter"]
    out = []
    m = SIG_RE.match(path.name)
    sid = fm.get("signal_id")
    if not sid:
        out.append("no signal_id")
    elif not m or sid != m.group(0):
        out.append(f"signal_id {sid!r} does not match the filename")
    for key in ("action", "info"):
        if key not in fm:
            out.append(f"no {key}: line")
        elif not isinstance(fm[key], list):
            out.append(f"{key}: is not a bracketed list")
    if not fm.get("time_dispatched"):
        out.append("time_dispatched empty (unstamped)")
    return out


def routing_class(fm):
    """A / I / O from a frontmatter mapping (lenient: a non-list cell routes to nobody)."""
    return "A" if ME in _names(fm, "action") else "I" if ME in _names(fm, "info") else "O"


def publication_state(files):
    """Split on-disk signal files into published names and held-back {name: reason}.

    Published = present in HEAD's tree AND carrying no working-tree or index change.
    Any git failure raises ScanError: an unknown publication state is never read as published.
    """
    def git(*argv):
        try:
            r = subprocess.run(["git", "-C", str(BOARD), *argv], capture_output=True, text=True)
        except OSError as e:
            raise ScanError(f"git could not be run: {e}")
        if r.returncode != 0:
            raise ScanError(f"git {' '.join(argv[:2])} failed: {(r.stderr or r.stdout).strip()[:200]}")
        return r.stdout

    git("rev-parse", "--show-toplevel")
    # paths below are relative to BOARD (ls-tree honours -C; status needs the './' pathspec)
    in_head = {pathlib.PurePosixPath(p).name for p in git(
        "ls-tree", "--name-only", "-z", "HEAD", "--", "./").split("\0") if p}
    dirty = {}
    tokens = git("status", "--porcelain=v1", "-z", "--untracked-files=all", "--", ".").split("\0")
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        i += 1
        if len(tok) < 4:
            continue
        xy, path = tok[:2], tok[3:]
        dirty[pathlib.PurePosixPath(path).name] = xy
        if "R" in xy or "C" in xy:           # rename/copy: the next token is the source path
            if i < len(tokens) and tokens[i]:
                dirty[pathlib.PurePosixPath(tokens[i]).name] = xy
            i += 1
    published, held = set(), {}
    for p in files:
        if p.name in dirty:
            xy = dirty[p.name]
            held[p.name] = "untracked" if xy == "??" else f"uncommitted change ({xy.strip() or xy})"
        elif p.name in in_head:
            published.add(p.name)
        else:
            held[p.name] = "not in HEAD"
    return published, held


def load_ledger():
    """Return ({stem: flag}, exists). A malformed row raises ScanError (never guess)."""
    if not LEDGER.exists():
        return {}, False
    try:
        text = LEDGER.read_text(encoding="utf-8")
    except OSError as e:
        raise ScanError(f"consumed ledger unreadable: {e}")
    out = {}
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) != 2 or not SIG_RE.match(parts[0]) or parts[1] not in FLAGS:
            raise ScanError(f"consumed ledger {LEDGER} line {n} is malformed: {line[:80]!r}")
        out[parts[0]] = parts[1]
    return out, True


def _atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def save_state(consumed):
    rows = sorted(consumed.items(), key=lambda kv: (sig_key(kv[0]), kv[0]))
    _atomic_write(LEDGER, LEDGER_HEADER + "".join(f"{s}\t{f}\n" for s, f in rows))
    if consumed:
        d, n = max(sig_key(s) for s in consumed)
        _atomic_write(CURSOR, f"SIG-W-{d}-{n:03d}\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--advance", action="store_true", help="record what this scan consumed")
    ap.add_argument("--ack-actions", action="store_true",
                    help="with --advance: also consume ACTION lines and UNREADABLE files "
                         "(use ONLY after dispositioning them)")
    ap.add_argument("--since", default=None, help="YYYYMMDD floor: list published signals from that date, consumed or not")
    ap.add_argument("--audit", default=None, help="YYYYMMDD — report every ACTION line for PROME")
    args = ap.parse_args()

    if not BOARD.is_dir():
        print(f"BOARD-SCAN ✗ no BOARD dir at {BOARD}", file=sys.stderr)
        return 2

    files = sorted((p for p in BOARD.glob("SIG-W-*.md")), key=lambda p: (sig_key(p.name), p.name))
    if not files:
        print("BOARD-SCAN ✗ no signal files found", file=sys.stderr)
        return 2

    if args.audit:
        hits = 0
        for p in files:
            if sig_key(p.name)[0] < args.audit:
                continue
            fm = parse_front(p)
            if ME in _names(fm, "action"):
                hits += 1
                print(f"  ACTION  {fm.get('signal_id', p.name)}  {clean(fm.get('_headline'))}")
        total = sum(1 for p in files if sig_key(p.name)[0] >= args.audit)
        print(f"\nBOARD-SCAN audit since {args.audit}: {hits} ACTION-line / {total} signals for {ME}")
        return 0

    try:
        published, held = publication_state(files)
        consumed, ledger_exists = load_ledger()
    except ScanError as e:
        print(f"BOARD-SCAN ✗ cannot run — {e} (nothing consumed, nothing written)", file=sys.stderr)
        return 2

    cursor = load_cursor()
    pub_files = [p for p in files if p.name in published]
    front = {p.name: parse_front(p) for p in pub_files}

    seeded = 0
    if not ledger_exists and cursor:
        # Migration from the high-water cursor: every PUBLISHED file at or below it was consumed
        # under the old scheme. A file at or below it that is NOT published stays unconsumed.
        ck = sig_key(cursor)
        for p in pub_files:
            if sig_key(p.name) <= ck:
                consumed[p.stem] = routing_class(front[p.name])
                seeded += 1

    if args.since:
        cand = [p for p in pub_files if sig_key(p.name)[0] >= args.since]
    else:
        cand = [p for p in pub_files if p.stem not in consumed]
    cand_stems = {p.stem for p in cand}
    # a consumed signal that has since gained PROME on its action line
    late = [p for p in pub_files
            if p.stem in consumed and p.stem not in cand_stems
            and consumed[p.stem] != "A" and ME in _names(front[p.name], "action")]

    action, info, other, unreadable = [], [], [], []
    for p in cand:
        fm = front[p.name]
        row = (fm.get("signal_id", p.stem), fm.get("cluster", "?"),
               fm.get("precedence", "?"), clean(fm.get("_headline")))
        acts = _names(fm, "action")
        problems = [] if p.stem in consumed else metadata_problems(p, fm)
        if problems:
            unreadable.append((p, problems))
        else:
            cls = routing_class(fm)
            (action if cls == "A" else info if cls == "I" else other).append((p, row, acts))

    since_label = cursor or "(no cursor)"

    def show_held():
        if held:
            print(f"\n⏸  {len(held)} unpublished file(s) HELD BACK — not consumed; each surfaces once committed:")
            for name in sorted(held):
                print(f"   {name[:88]}  [{held[name]}]")

    if not cand and not late:
        print(f"BOARD-SCAN ✓ nothing new since {since_label}")
        show_held()
        if args.advance and seeded:
            save_state(consumed)
            print(f"\nconsumed ledger seeded from the cursor: {seeded} published file(s) at or below {cursor}")
        return 0

    print(f"BOARD-SCAN — {len(cand)} new since {since_label}  "
          f"[{len(action)} action · {len(info)} info · {len(other)} not-{ME}"
          + (f" · {len(unreadable)} UNREADABLE" if unreadable else "")
          + (f" · {len(late)} late action" if late else "") + "]")

    if action:
        print(f"\n🔴 {ME} ON ACTION LINE — disposition before proceeding:")
        for _, (sid, cl, pr, hl), _ in action:
            print(f"   {sid}  [{cl}/{pr}]\n      {hl}")

    if late:
        print(f"\n🔴 ACTION ADDED to {len(late)} signal(s) ALREADY CONSUMED — disposition before proceeding:")
        for p in late:
            fm = front[p.name]
            print(f"   {fm.get('signal_id', p.stem)}  [{fm.get('cluster', '?')}/{fm.get('precedence', '?')}]"
                  f"\n      {clean(fm.get('_headline'))}")

    if unreadable:
        print(f"\n🔴 {len(unreadable)} PUBLISHED signal(s) UNREADABLE — routing unknown; open the file, "
              f"then tell WALTER:")
        for p, problems in unreadable:
            print(f"   {p.name[:88]}\n      {'; '.join(problems)}")

    if info:
        print(f"\n📋 info-cc ({len(info)}) — owner in brackets:")
        for _, (sid, cl, pr, hl), acts in info:
            print(f"   {sid} [{','.join(acts) or '—'}] {hl}")

    if other:
        print(f"\n·  {len(other)} not routed to {ME} (listed for completeness):")
        for _, (sid, cl, pr, hl), acts in other:
            print(f"   {sid} [{','.join(acts) or '—'}] {clean(hl, 80)}")

    show_held()

    hold = len(action) + len(late) + len(unreadable)
    if args.advance:
        if hold and not args.ack_actions:
            # S3 crash-safety (7/28 live incident, fixed 8/9): consuming past an
            # undispositioned ACTION line + a crash before disposition = orphaned
            # signal. Withhold; every line re-surfaces next scan.
            print(f"\n⚠️  cursor NOT advanced — {hold} ACTION / UNREADABLE line(s) above are "
                  f"undispositioned. After dispositioning, re-run with "
                  f"--advance --ack-actions to move the cursor.")
            if seeded:
                save_state(consumed)
                print(f"consumed ledger seeded from the cursor: {seeded} published file(s) at or below {cursor}")
        else:
            for p, _, _ in action:
                consumed[p.stem] = "A"
            for p in late:
                consumed[p.stem] = "A"
            for p, _ in unreadable:
                consumed[p.stem] = "U"
            for group, flag in ((info, "I"), (other, "O")):
                for p, _, _ in group:
                    if consumed.get(p.stem) != "A":
                        consumed[p.stem] = flag
            save_state(consumed)
            print(f"\ncursor → {load_cursor()}  ({len(cand) + len(late)} consumed; ledger {len(consumed)} files)")

    return 1 if hold else 0


if __name__ == "__main__":
    sys.exit(main())
