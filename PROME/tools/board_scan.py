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
      LOWER id than ones already consumed still surfaces. board_cursor.txt is
      kept as a display high-water mark only.

ONE reader decides routing (`inspect_signal`), and it fails toward PROME: every
line whose key is signal_id / action / info — indented, quoted or capitalised
included — is counted, PROME on ANY action line counts as an action, and any
shape other than one plain `key: [a, b]` line per routing key is a problem.

  A published, UNCONSUMED file with any problem is UNREADABLE: routing unknown,
      a hard stop (rc 1) exactly like an action line, never a silent consume.

  A CONSUMED file whose committed blob changed is compared with the blob it was
      consumed at: PROME newly on action = a late action (rc 1); a problem the
      old blob did not have = UNREADABLE (rc 1); otherwise it is quiet, and a
      change in PROME's routing is listed, not hidden.

The ledger is never rebuilt implicitly. A missing ledger while a cursor exists
is rc 2 (restore it from git). `--seed-from-cursor` is the deliberate first
migration from the old high-water cursor: refused while a ledger exists on
disk or in HEAD, and it never records an action-routed file as consumed.

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
import collections
import fnmatch
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import urllib.parse

REPO = pathlib.Path(__file__).resolve().parents[2]
BOARD = REPO / "BOARD"
CURSOR = REPO / "PROME" / "state" / "board_cursor.txt"
LEDGER = REPO / "PROME" / "state" / "board_consumed.tsv"

SIG_RE = re.compile(r"^SIG-W-(\d{8})-(\d+)")
SHA_RE = re.compile(r"^[0-9a-f]{40,64}$")
KEY_RE = re.compile(r"^[A-Za-z0-9._~%-]+$")       # a ledger key: the file stem, percent-encoded
ME = "PROME"
FLAGS = {"A", "I", "O", "U"}   # action (acked) · info · other · unreadable (acked by hand)
STRICT_KEYS = ("signal_id", "action", "info")    # exactly one plain line each
LEDGER_HEADER = (
    "# PROME/state/board_consumed.tsv — every BOARD signal file board_scan.py has consumed.\n"
    "# One row per FILE: <file stem, percent-encoded><TAB><class><TAB><blob consumed at>  (A = PROME on "
    "action, acknowledged · I = info · O = not routed to PROME · U = unreadable, acknowledged by hand).\n"
    "# Written ONLY by `board_scan.py --advance` / `--seed-from-cursor`; never hand-edit. A file absent "
    "from this list is unconsumed and surfaces at the next scan once it is published (committed).\n")


class ScanError(Exception):
    """The scan cannot run. main() returns rc 2 and nothing is written."""


def parse_front_text(text):
    """Minimal frontmatter reader over file TEXT. Returns {} if there is no closed --- block.

    Kept for --audit and for exempt_gap.py. Routing decisions use inspect_signal(), not this."""
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


class Signal:
    """What one blob says about its routing, read strictly. See inspect_signal()."""

    def __init__(self):
        self.codes = []            # problem codes; [] = complete
        self.action, self.info, self.to = set(), set(), set()
        self.fields = {}
        self.headline = ""

    @property
    def me_action(self):
        return ME in self.action or ME in self.to

    @property
    def cls(self):
        return "A" if self.me_action else "I" if ME in self.info else "O"

    def describe(self):
        return "; ".join(PROBLEM_TEXT.get(c.split("=")[0], c).format(key=c.partition("=")[2]) for c in self.codes)


PROBLEM_TEXT = {
    "unclosed": "no closed frontmatter block at the top of the file",
    "missing": "no {key}: line",
    "nonlist": "{key}: is not a one-line bracketed list",
    "repeated": "{key}: appears more than once",
    "nonstandard": "{key}: is written in a non-standard form (indented, quoted or capitalised)",
    "sid": "signal_id does not match the filename",
    "unparsed-me": f"an action entry names {ME} but not as a readable list element",
    "unstamped": "time_dispatched empty (unstamped)",
}


def inspect_signal(name, text):
    """Read one blob's routing STRICTLY and fail toward PROME.

    Every line whose key normalises to a routing key is counted — whatever its indentation, quoting
    or case — so a second `action` hidden in a nested mapping or behind quotes cannot silently win.
    Names found on ANY such line are unioned. Any shape other than one plain `key: [a, b]` line per
    routing key becomes a problem code."""
    s = Signal()
    closed = False
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            closed = True
            lines = text[3:end].splitlines()
            m = re.search(r"^# (.+)$", text[end:], re.MULTILINE)
            s.headline = m.group(1).strip() if m else ""
    if not closed:
        s.codes.append("unclosed")
        lines = text.lstrip("﻿").splitlines()[:80]     # still look for PROME in the file's head
    count = collections.Counter()
    nonlist, nonstandard, mention = set(), set(), False
    for i, line in enumerate(lines):
        if ":" not in line:
            continue
        rawkey, _, rest = line.partition(":")
        key = rawkey.strip().strip("'\"").strip().lower()
        val = rest.strip()
        if rawkey == rawkey.strip():
            s.fields.setdefault(rawkey, val)
        if key == "to":
            if rawkey != key:
                continue                                    # legacy key: only its plain form routes
        elif key not in STRICT_KEYS:
            continue
        count[key] += 1
        if rawkey != key:
            nonstandard.add(key)
        if key == "signal_id":
            continue
        chunk = [rest]
        for nxt in lines[i + 1:]:
            if nxt[:1].isspace() or nxt.lstrip().startswith("-"):
                chunk.append(nxt)
            else:
                break
        if key in ("action", "to") and re.search(r"\b" + ME + r"\b", " ".join(chunk), re.IGNORECASE):
            mention = True
        if val.startswith("[") and val.endswith("]"):
            getattr(s, key).update(x.strip().strip("'\"").upper() for x in val[1:-1].split(",") if x.strip())
        else:
            nonlist.add(key)
    m = SIG_RE.match(name)
    if count["signal_id"] == 0:
        s.codes.append("missing=signal_id")
    elif not m or s.fields.get("signal_id", "").strip("'\"") != m.group(0):
        s.codes.append("sid")
    for key in ("action", "info"):
        if count[key] == 0:
            s.codes.append(f"missing={key}")
    for key in sorted(nonlist - {"to"}):
        s.codes.append(f"nonlist={key}")
    for key in STRICT_KEYS:
        if count[key] > 1:
            s.codes.append(f"repeated={key}")
        if key in nonstandard:
            s.codes.append(f"nonstandard={key}")
    if mention and not s.me_action:
        s.codes.append("unparsed-me")
    if not s.fields.get("time_dispatched"):
        s.codes.append("unstamped")
    return s


def _git(*argv, stdin=None, ok=(0,)):
    """Run git inside BOARD; any failure is a ScanError (an unknown state is never read as published)."""
    try:
        r = subprocess.run(["git", "-C", str(BOARD), *argv], capture_output=True, input=stdin)
    except OSError as e:
        raise ScanError(f"git could not be run: {e}")
    if r.returncode not in ok:
        msg = (r.stderr or r.stdout).decode("utf-8", "replace").strip()[:200]
        raise ScanError(f"git {argv[0]} failed: {msg}")
    return r


def head_signals():
    """{file name: blob} for every SIG-W-*.md blob directly under BOARD in HEAD's tree."""
    out = {}
    # '-- ./' lists BOARD's own entries without recursing; subdirectories come back as trees.
    listing = _git("ls-tree", "-z", "HEAD", "--", "./").stdout.decode("utf-8", "replace")
    for entry in listing.split("\0"):
        if not entry:
            continue
        meta, _, path = entry.partition("\t")
        parts = meta.split()
        if len(parts) != 3 or parts[1] != "blob" or "/" in path.lstrip("./"):
            continue
        name = pathlib.PurePosixPath(path).name
        if fnmatch.fnmatchcase(name, "SIG-W-*.md"):
            out[name] = parts[2]
    return out


def read_blobs(shas):
    """{blob: text or None} from the object store in one `git cat-file --batch` call (None = not present)."""
    shas = sorted(set(shas))
    if not shas:
        return {}
    raw = _git("cat-file", "--batch", stdin=("\n".join(shas) + "\n").encode()).stdout
    out, pos = {}, 0
    for sha in shas:
        nl = raw.find(b"\n", pos)
        if nl == -1:
            raise ScanError("git cat-file returned a short stream")
        head = raw[pos:nl].decode("ascii", "replace").split()
        if len(head) == 2 and head[1] == "missing":
            out[sha] = None
            pos = nl + 1
            continue
        if len(head) != 3 or head[1] != "blob":
            raise ScanError(f"git cat-file could not read {sha}: {' '.join(head)[:80]}")
        size = int(head[2])
        out[sha] = raw[nl + 1: nl + 1 + size].decode("utf-8", "replace")
        pos = nl + 1 + size + 1
    return out


def _stem(name):
    return name[:-3] if name.endswith(".md") else name


def _enc(stem):
    return urllib.parse.quote(stem, safe="-_.~")


def parse_ledger_text(text, where="consumed ledger"):
    """{stem: (class, blob)} from ledger text. Rows split on \\n only; anything unexpected is a ScanError."""
    out = {}
    for n, line in enumerate(text.split("\n"), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) != 3 or not KEY_RE.match(parts[0]) or parts[1] not in FLAGS or not SHA_RE.match(parts[2]):
            raise ScanError(f"{where} line {n} is malformed: {line[:80]!r}")
        stem = urllib.parse.unquote(parts[0])
        if stem in out:
            raise ScanError(f"{where} line {n} repeats {stem[:60]!r}")
        out[stem] = (parts[1], parts[2])
    return out


def load_ledger():
    """Return ({stem: (class, blob)}, exists). Anything unexpected raises ScanError (never guess)."""
    if not LEDGER.exists():
        return {}, False
    try:
        text = LEDGER.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        raise ScanError(f"consumed ledger unreadable: {e}")
    return parse_ledger_text(text, f"consumed ledger {LEDGER}"), True


def ledger_in_head():
    """True when the ledger file exists in HEAD of BOARD's repository (so a lost copy can be restored)."""
    top = pathlib.Path(_git("rev-parse", "--show-toplevel").stdout.decode("utf-8", "replace").strip())
    try:
        rel = LEDGER.resolve().relative_to(top.resolve()).as_posix()
    except ValueError:
        return False
    return _git("cat-file", "-e", f"HEAD:{rel}", ok=(0, 1, 128)).returncode == 0


def _atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as fh:
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
    text = LEDGER_HEADER + "".join(f"{_enc(s)}\t{c}\t{b}\n" for s, (c, b) in rows)
    # the writer may never emit a ledger its own reader rejects or reads differently
    if parse_ledger_text(text, "the ledger about to be written") != dict(consumed):
        raise ScanError("the ledger about to be written does not read back as the consumed set")
    _atomic_write(LEDGER, text)
    ids = [sig_key(s) for s in consumed if SIG_RE.match(s)]
    if ids:
        d, n = max(ids)
        _atomic_write(CURSOR, f"SIG-W-{d}-{n:03d}\n")


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

    if args.seed_from_cursor:
        if ledger_exists:
            raise ScanError(f"--seed-from-cursor refused: {LEDGER} already exists (the migration runs once)")
        if ledger_in_head():
            raise ScanError(f"--seed-from-cursor refused: {LEDGER} is in HEAD — restore it with git, do not re-seed")
        if not cursor or not SIG_RE.match(cursor):
            raise ScanError("--seed-from-cursor needs a valid cursor file to seed from")
    elif not ledger_exists and cursor:
        raise ScanError(
            f"consumed ledger {LEDGER} is MISSING while a cursor exists — restore it from git "
            f"(it is the record of what was consumed); only a first migration may run --seed-from-cursor")

    cache = {}

    def texts_for(shas):
        need = [x for x in shas if x not in cache]
        cache.update(read_blobs(need))
        return cache

    def sig(name):
        return inspect_signal(name, texts_for([head[name]])[head[name]])

    if args.seed_from_cursor:
        ck = sig_key(cursor)
        low = [n for n in names if sig_key(n) <= ck]
        texts_for(head[n] for n in low)
        left = []
        for n in low:
            cls = sig(n).cls
            if cls == "A":
                left.append(n)                # never consumed by a seed: it surfaces below
            else:
                consumed[_stem(n)] = (cls, head[n])
        save_state(consumed)
        print(f"consumed ledger SEEDED from the cursor: {len(low) - len(left)} published file(s) at or below "
              f"{cursor}; {len(left)} more name {ME} on their action line and are NOT recorded — they are "
              f"listed below for acknowledgement.")

    changed = [n for n in names if _stem(n) in consumed and consumed[_stem(n)][1] != head[n]]
    texts_for([head[n] for n in changed] + [consumed[_stem(n)][1] for n in changed])
    resurfaced = {n for n in changed if cache[consumed[_stem(n)][1]] is None}   # the consumed blob is gone

    if args.since:
        cand = [n for n in names if sig_key(n)[0] >= args.since]
    else:
        cand = [n for n in names if _stem(n) not in consumed or n in resurfaced]
    texts_for(head[n] for n in cand)

    # consumed signals whose committed content changed: compare against the blob they were consumed at
    late, amended_bad, quiet, rerouted = [], [], [], []
    for n in changed:
        if n in resurfaced:
            continue
        new = sig(n)
        old = inspect_signal(n, cache[consumed[_stem(n)][1]])
        introduced = [c for c in new.codes if c not in old.codes]
        if introduced:
            bad = Signal()
            bad.codes = introduced
            amended_bad.append((n, bad.describe()))
        elif new.me_action and not old.me_action:
            late.append(n)
        else:
            quiet.append(n)
            if new.cls != old.cls:
                rerouted.append((n, old.cls, new.cls))
    recheck = {n for n, _ in amended_bad} | set(late)

    action, info, other, unreadable = [], [], [], []
    for n in cand:
        if n in recheck:
            continue                                   # shown once, in its own block below
        s = sig(n)
        row = (s.fields.get("signal_id", _stem(n)), s.fields.get("cluster", "?"),
               s.fields.get("precedence", "?"), clean(s.headline))
        acts = sorted(s.action | s.to)
        fresh = _stem(n) not in consumed or n in resurfaced
        if fresh and s.codes:
            unreadable.append((n, s.describe()))
        else:
            (action if s.cls == "A" else info if s.cls == "I" else other).append((n, row, acts, fresh))

    since_label = cursor or "(no cursor)"
    shown = len(action) + len(info) + len(other) + len(unreadable)
    hold = (sum(1 for a in action if a[3]) + len(late) + len(unreadable) + len(amended_bad))
    class_name = {"A": "action", "I": "info", "O": "not routed", "U": "unreadable"}

    def show_tail():
        same = len(quiet) - len(rerouted)
        if same:
            print(f"\n·  {same} consumed signal(s) amended since consumption — {ME}'s routing unchanged")
        if rerouted:
            print(f"\n·  {len(rerouted)} consumed signal(s) amended and {ME}'s routing CHANGED:")
            for n, was, now in rerouted:
                print(f"   {sig(n).fields.get('signal_id', _stem(n))}  {class_name[was]} → {class_name[now]}"
                      f"  {clean(sig(n).headline, 70)}")
        if held:
            print(f"\n⏸  {len(held)} uncommitted file(s) HELD BACK — not published, not consumed; "
                  f"each surfaces once committed:")
            for name in held:
                print(f"   {name[:96]}")

    refresh = [(_stem(n), sig(n).cls, head[n]) for n in quiet]

    def record(rows):
        for stem, cls, blob in rows:
            consumed[stem] = (cls, blob)

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
        for _, (sid, cl, pr, hl), _, _ in action:
            print(f"   {sid}  [{cl}/{pr}]\n      {hl}")

    if late:
        print(f"\n🔴 ACTION ADDED to {len(late)} signal(s) ALREADY CONSUMED — disposition before proceeding:")
        for n in late:
            s = sig(n)
            print(f"   {s.fields.get('signal_id', _stem(n))}  [{s.fields.get('cluster', '?')}/"
                  f"{s.fields.get('precedence', '?')}]\n      {clean(s.headline)}")

    if unreadable or amended_bad:
        print(f"\n🔴 {len(unreadable) + len(amended_bad)} PUBLISHED signal(s) UNREADABLE — routing unknown; "
              f"open the file, then tell WALTER:")
        for n, why in unreadable:
            print(f"   {n[:96]!r}\n      {why}")
        for n, why in amended_bad:
            print(f"   {n[:96]!r}  (consumed earlier, amended since)\n      {why}")

    if info:
        print(f"\n📋 info-cc ({len(info)}) — owner in brackets:")
        for _, (sid, cl, pr, hl), acts, _ in info:
            print(f"   {sid} [{','.join(acts) or '—'}] {hl}")

    if other:
        print(f"\n·  {len(other)} not routed to {ME} (listed for completeness):")
        for _, (sid, cl, pr, hl), acts, _ in other:
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
                   for n, _, _, fresh in group if fresh]
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
                    help="first migration only: build the consumed ledger from the old high-water cursor "
                         "(refused while a ledger exists on disk or in HEAD)")
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
