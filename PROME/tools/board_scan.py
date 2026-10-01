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

  PUBLISHED = the signal file is in HEAD's tree. WALTER stamps a signal in the
      same command as its commit, so the commit is the publication act. Names
      AND content are read from HEAD (git ls-tree / git cat-file), never from
      the working tree: an uncommitted edit, a deleted working copy or a file
      rewritten mid-scan cannot change what was published. A file on disk
      that is NOT in HEAD is a DRAFT: it is reported as held back and is never
      consumed, whatever flag is passed. BOARD/INDEX.md is NOT read.

  CONSUMED = the file's stem is recorded in PROME/state/board_consumed.tsv
      with its class and the blob it was consumed at. The pass is a diff of
      published files against that ledger, so a signal published late with a
      LOWER id than ones already consumed still surfaces, and a consumed signal
      whose committed content later changes is re-examined. board_cursor.txt
      is kept as a display high-water mark only.

A published, unconsumed file whose metadata is incomplete (no closed
frontmatter, signal_id missing or not matching the filename, action/info not
bracketed lists or given twice, empty time_dispatched) is UNREADABLE: its
routing is unknown, so it is a hard stop (rc 1) exactly like an action line,
never a silent consume.

The ledger is never rebuilt implicitly. A missing ledger while a cursor exists
is rc 2 (restore it from git); `--seed-from-cursor` is the one deliberate
migration from the old high-water cursor and refuses to run twice.

Usage:
    python3 PROME/tools/board_scan.py                 # scan, write nothing
    python3 PROME/tools/board_scan.py --advance       # scan, then record consumption
    python3 PROME/tools/board_scan.py --since 20260724
    python3 PROME/tools/board_scan.py --audit 20260701   # ACTION-line audit

Exit codes: 0 = nothing new or info-only; 1 = PROME is on an ACTION line, a late
action landed on a consumed signal, or a published signal is unreadable (boot
must not proceed past this without dispositioning); 2 = the scan could not run
(no BOARD, git unavailable, ledger missing or unreadable, any unexpected
error) — nothing is written.
"""
import argparse
import fnmatch
import os
import pathlib
import re
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[2]
BOARD = REPO / "BOARD"
CURSOR = REPO / "PROME" / "state" / "board_cursor.txt"
LEDGER = REPO / "PROME" / "state" / "board_consumed.tsv"

SIG_RE = re.compile(r"^SIG-W-(\d{8})-(\d+)")
SHA_RE = re.compile(r"^[0-9a-f]{40,64}$")
ME = "PROME"
FLAGS = {"A", "I", "O", "U"}   # action (acked) · info · other · unreadable (acked by hand)
ROUTING_KEYS = ("signal_id", "action", "info")
LEDGER_HEADER = (
    "# PROME/state/board_consumed.tsv — every BOARD signal file board_scan.py has consumed.\n"
    "# One row per FILE: <file stem><TAB><class><TAB><blob consumed at>  (A = PROME on action, "
    "acknowledged · I = info · O = not routed to PROME · U = unreadable, acknowledged by hand).\n"
    "# Written ONLY by `board_scan.py --advance` / `--seed-from-cursor`; never hand-edit. A file absent "
    "from this list is unconsumed and surfaces at the next scan once it is published (committed).\n")


class ScanError(Exception):
    """The scan cannot run. main() returns rc 2 and nothing is written."""


def parse_front_text(text):
    """Minimal frontmatter reader over file TEXT. Returns {} if there is no closed --- block."""
    out = {}
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


def parse_front(path):
    """Minimal frontmatter reader over a working-tree file. Returns {} if the file has no --- block."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}
    return parse_front_text(text)


def sig_key(name):
    m = SIG_RE.match(name)
    return (m.group(1), int(m.group(2))) if m else ("", 0)


def load_cursor():
    if not CURSOR.exists():
        return ""
    try:
        return CURSOR.read_text(encoding="utf-8").strip()
    except (OSError, UnicodeDecodeError) as e:
        raise ScanError(f"cursor file unreadable: {e}")


def clean(s, n=104):
    s = re.sub(r"[*`_]|<[^>]+>", "", s or "").strip()
    s = re.sub(r"\s+", " ", s)
    return s[: n - 1] + "…" if len(s) > n else s


def _names(fm, key):
    """Upper-cased routing names for `key`, or [] when the cell is not a bracketed list."""
    v = fm.get(key)
    return [a.upper() for a in v] if isinstance(v, list) else []


def _front_region(text):
    """The lines a routing key could live on: the frontmatter block, or the file's head if it never closes."""
    body = text.lstrip("﻿")
    if body.startswith("---"):
        end = body.find("\n---", 3)
        if end != -1:
            return body[3:end].splitlines()
    return body.splitlines()[:80]


def duplicate_routing_keys(text):
    seen, dup = set(), []
    for line in _front_region(text):
        if line[:1].isspace() or ":" not in line:
            continue
        k = line.partition(":")[0].strip()
        if k in ROUTING_KEYS:
            if k in seen and k not in dup:
                dup.append(k)
            seen.add(k)
    return dup


def raw_action_names_me(text):
    """True when an `action` entry mentions PROME in ANY form (unbracketed, block list, any case)."""
    lines = _front_region(text)
    for i, line in enumerate(lines):
        if re.match(r"\s*action\s*:", line, re.IGNORECASE):
            chunk = [line.partition(":")[2]]
            for nxt in lines[i + 1:]:
                if nxt[:1].isspace() or nxt.lstrip().startswith("-"):
                    chunk.append(nxt)
                else:
                    break
            if re.search(r"\b" + ME + r"\b", " ".join(chunk), re.IGNORECASE):
                return True
    return False


def metadata_problems(name, fm, text):
    """Why a published file cannot be trusted to say who it is routed to ([] = complete)."""
    if not fm:
        return ["no closed frontmatter"]
    out = []
    m = SIG_RE.match(name)
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
    for key in duplicate_routing_keys(text):
        out.append(f"{key}: appears more than once")
    if not fm.get("time_dispatched"):
        out.append("time_dispatched empty (unstamped)")
    return out


def amendment_problems(fm, text):
    """A CONSUMED file whose committed content changed: is its routing still readable? ([] = yes)."""
    out = []
    if not fm:
        out.append("no closed frontmatter after the amendment")
    for key in duplicate_routing_keys(text):
        out.append(f"{key}: appears more than once")
    if raw_action_names_me(text) and ME not in _names(fm, "action"):
        out.append(f"an action entry names {ME} but is not a readable bracketed list")
    return out


def routing_class(fm):
    """A / I / O from a frontmatter mapping (lenient: a non-list cell routes to nobody)."""
    return "A" if ME in _names(fm, "action") else "I" if ME in _names(fm, "info") else "O"


def _git(*argv, stdin=None):
    """Run git inside BOARD; any failure is a ScanError (an unknown state is never read as published)."""
    try:
        r = subprocess.run(["git", "-C", str(BOARD), *argv], capture_output=True, input=stdin)
    except OSError as e:
        raise ScanError(f"git could not be run: {e}")
    if r.returncode != 0:
        msg = (r.stderr or r.stdout).decode("utf-8", "replace").strip()[:200]
        raise ScanError(f"git {argv[0]} failed: {msg}")
    return r.stdout


def head_signals():
    """{file name: blob} for every SIG-W-*.md blob directly under BOARD in HEAD's tree."""
    out = {}
    # '-- ./' lists BOARD's own entries without recursing; subdirectories come back as trees.
    for entry in _git("ls-tree", "-z", "HEAD", "--", "./").decode("utf-8", "replace").split("\0"):
        if not entry:
            continue
        meta, _, path = entry.partition("\t")
        parts = meta.split()
        if len(parts) != 3 or parts[1] != "blob":
            continue
        name = pathlib.PurePosixPath(path).name
        if fnmatch.fnmatchcase(name, "SIG-W-*.md"):
            out[name] = parts[2]
    return out


def read_blobs(shas):
    """{blob: text} read from the object store in one `git cat-file --batch` call."""
    shas = sorted(set(shas))
    if not shas:
        return {}
    raw = _git("cat-file", "--batch", stdin=("\n".join(shas) + "\n").encode())
    out, pos = {}, 0
    for sha in shas:
        nl = raw.find(b"\n", pos)
        if nl == -1:
            raise ScanError("git cat-file returned a short stream")
        head = raw[pos:nl].decode("ascii", "replace").split()
        if len(head) != 3 or head[1] != "blob":
            raise ScanError(f"git cat-file could not read {sha}: {' '.join(head)[:80]}")
        size = int(head[2])
        out[sha] = raw[nl + 1: nl + 1 + size].decode("utf-8", "replace")
        pos = nl + 1 + size + 1
    return out


def load_ledger():
    """Return ({stem: (class, blob)}, exists). Anything unexpected raises ScanError (never guess)."""
    if not LEDGER.exists():
        return {}, False
    try:
        text = LEDGER.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        raise ScanError(f"consumed ledger unreadable: {e}")
    out = {}
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) != 3 or not SIG_RE.match(parts[0]) or parts[1] not in FLAGS or not SHA_RE.match(parts[2]):
            raise ScanError(f"consumed ledger {LEDGER} line {n} is malformed: {line[:80]!r}")
        out[parts[0]] = (parts[1], parts[2])
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
    _atomic_write(LEDGER, LEDGER_HEADER + "".join(f"{s}\t{c}\t{b}\n" for s, (c, b) in rows))
    if consumed:
        d, n = max(sig_key(s) for s in consumed)
        _atomic_write(CURSOR, f"SIG-W-{d}-{n:03d}\n")


def _stem(name):
    return name[:-3] if name.endswith(".md") else name


def _scan(args):
    if not BOARD.is_dir():
        raise ScanError(f"no BOARD dir at {BOARD}")

    on_disk = {p.name for p in BOARD.glob("SIG-W-*.md")}

    if args.audit:
        files = sorted((BOARD / n for n in on_disk), key=lambda p: (sig_key(p.name), p.name))
        if not files:
            raise ScanError("no signal files found")
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

    head = head_signals()
    if not head and not on_disk:
        raise ScanError("no signal files found")
    held = sorted(on_disk - set(head))
    names = sorted(head, key=lambda n: (sig_key(n), n))
    cursor = load_cursor()
    consumed, ledger_exists = load_ledger()

    seeded = None
    if args.seed_from_cursor:
        if ledger_exists:
            raise ScanError(f"--seed-from-cursor refused: {LEDGER} already exists (the migration runs once)")
        if not cursor or not SIG_RE.match(cursor):
            raise ScanError("--seed-from-cursor needs a valid cursor file to seed from")
    elif not ledger_exists and cursor:
        raise ScanError(
            f"consumed ledger {LEDGER} is MISSING while a cursor exists — restore it from git "
            f"(it is the record of what was consumed); only a first migration may run --seed-from-cursor")

    def content(name_list):
        blobs = read_blobs(head[n] for n in name_list)
        return {n: blobs[head[n]] for n in name_list}

    if args.seed_from_cursor:
        ck = sig_key(cursor)
        low = [n for n in names if sig_key(n) <= ck]
        texts = content(low)
        seeded = []
        for n in low:
            cls = routing_class(parse_front_text(texts[n]))
            consumed[_stem(n)] = (cls, head[n])
            if cls == "A":
                seeded.append(n)
        save_state(consumed)
        print(f"consumed ledger SEEDED from the cursor: {len(low)} published file(s) at or below {cursor}; "
              f"{len(seeded)} of them name {ME} on their action line and are recorded as already dispositioned:")
        for n in seeded:
            print(f"   {_stem(n)[:88]}")

    if args.since:
        cand = [n for n in names if sig_key(n)[0] >= args.since]
    else:
        cand = [n for n in names if _stem(n) not in consumed]
    cand_set = set(cand)
    changed = [n for n in names if _stem(n) in consumed and consumed[_stem(n)][1] != head[n]]
    texts = content(sorted(cand_set | set(changed)))
    front = {n: parse_front_text(t) for n, t in texts.items()}

    # consumed signals whose committed content has changed since they were consumed
    late, amended_bad, amended_quiet = [], [], []
    for n in changed:
        problems = amendment_problems(front[n], texts[n])
        if problems:
            amended_bad.append((n, problems))
        elif consumed[_stem(n)][0] != "A" and ME in _names(front[n], "action"):
            late.append(n)
        else:
            amended_quiet.append(n)
    recheck = {n for n, _ in amended_bad} | set(late)

    action, info, other, unreadable = [], [], [], []
    for n in cand:
        if n in recheck:
            continue                                   # shown once, in its own block below
        fm = front[n]
        row = (fm.get("signal_id", _stem(n)), fm.get("cluster", "?"),
               fm.get("precedence", "?"), clean(fm.get("_headline")))
        acts = _names(fm, "action")
        problems = [] if _stem(n) in consumed else metadata_problems(n, fm, texts[n])
        if problems:
            unreadable.append((n, problems))
        else:
            cls = routing_class(fm)
            (action if cls == "A" else info if cls == "I" else other).append((n, row, acts))

    since_label = cursor or "(no cursor)"
    shown = len(action) + len(info) + len(other) + len(unreadable)
    hold = len(action) + len(late) + len(unreadable) + len(amended_bad)

    def show_tail():
        if amended_quiet:
            print(f"\n·  {len(amended_quiet)} consumed signal(s) amended since consumption — "
                  f"{ME}'s routing unchanged")
        if held:
            print(f"\n⏸  {len(held)} uncommitted file(s) HELD BACK — not published, not consumed; "
                  f"each surfaces once committed:")
            for name in held:
                print(f"   {name[:96]}")

    def record(pairs):
        for stem, cls, blob in pairs:
            consumed[stem] = (cls, blob)

    refresh = [(_stem(n), "A" if consumed[_stem(n)][0] == "A" else routing_class(front[n]), head[n])
               for n in amended_quiet]

    if not shown and not hold:
        print(f"BOARD-SCAN ✓ nothing new since {since_label}")
        show_tail()
        if args.advance and refresh:
            record(refresh)
            save_state(consumed)
        return 0

    print(f"BOARD-SCAN — {shown} new since {since_label}  "
          f"[{len(action)} action · {len(info)} info · {len(other)} not-{ME}"
          + (f" · {len(unreadable)} UNREADABLE" if unreadable else "")
          + (f" · {len(late)} late action" if late else "")
          + (f" · {len(amended_bad)} amended UNREADABLE" if amended_bad else "") + "]")

    if action:
        print(f"\n🔴 {ME} ON ACTION LINE — disposition before proceeding:")
        for _, (sid, cl, pr, hl), _ in action:
            print(f"   {sid}  [{cl}/{pr}]\n      {hl}")

    if late:
        print(f"\n🔴 ACTION ADDED to {len(late)} signal(s) ALREADY CONSUMED — disposition before proceeding:")
        for n in late:
            fm = front[n]
            print(f"   {fm.get('signal_id', _stem(n))}  [{fm.get('cluster', '?')}/{fm.get('precedence', '?')}]"
                  f"\n      {clean(fm.get('_headline'))}")

    if unreadable or amended_bad:
        print(f"\n🔴 {len(unreadable) + len(amended_bad)} PUBLISHED signal(s) UNREADABLE — routing unknown; "
              f"open the file, then tell WALTER:")
        for n, problems in unreadable:
            print(f"   {n[:96]}\n      {'; '.join(problems)}")
        for n, problems in amended_bad:
            print(f"   {n[:96]}  (consumed earlier, amended since)\n      {'; '.join(problems)}")

    if info:
        print(f"\n📋 info-cc ({len(info)}) — owner in brackets:")
        for _, (sid, cl, pr, hl), acts in info:
            print(f"   {sid} [{','.join(acts) or '—'}] {hl}")

    if other:
        print(f"\n·  {len(other)} not routed to {ME} (listed for completeness):")
        for _, (sid, cl, pr, hl), acts in other:
            print(f"   {sid} [{','.join(acts) or '—'}] {clean(hl, 80)}")

    show_tail()

    if args.advance:
        if hold and not args.ack_actions:
            # S3 crash-safety (7/28 live incident, fixed 8/9): consuming past an
            # undispositioned ACTION line + a crash before disposition = orphaned
            # signal. Withhold; every line re-surfaces next scan.
            print(f"\n⚠️  cursor NOT advanced — {hold} ACTION / UNREADABLE line(s) above are "
                  f"undispositioned. After dispositioning, re-run with "
                  f"--advance --ack-actions to move the cursor.")
        else:
            new = [(_stem(n), cls, head[n])
                   for group, cls in ((action, "A"), (info, "I"), (other, "O"))
                   for n, _, _ in group if _stem(n) not in consumed]
            new += [(_stem(n), "U", head[n]) for n, _ in unreadable]
            new += [(_stem(n), "A", head[n]) for n in late]
            new += [(_stem(n), "U", head[n]) for n, _ in amended_bad]
            record(new + refresh)
            save_state(consumed)
            print(f"\ncursor → {load_cursor()}  ({len(new)} consumed; ledger {len(consumed)} files)")

    return 1 if hold else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--advance", action="store_true", help="record what this scan consumed")
    ap.add_argument("--ack-actions", action="store_true",
                    help="with --advance: also consume ACTION lines and UNREADABLE files "
                         "(use ONLY after dispositioning them)")
    ap.add_argument("--since", default=None,
                    help="YYYYMMDD floor: list published signals from that date, consumed or not")
    ap.add_argument("--audit", default=None, help="YYYYMMDD — report every ACTION line for PROME")
    ap.add_argument("--seed-from-cursor", action="store_true",
                    help="ONE-TIME migration: build the consumed ledger from the old high-water cursor "
                         "(refused once a ledger exists)")
    args = ap.parse_args()
    try:
        return _scan(args)
    except ScanError as e:
        print(f"BOARD-SCAN ✗ cannot run — {e} (nothing consumed)", file=sys.stderr)
        return 2
    except Exception as e:   # an unexpected failure must never look like an action-line stop (rc 1)
        print(f"BOARD-SCAN ✗ cannot run — unexpected {type(e).__name__}: {e} (nothing consumed)",
              file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
