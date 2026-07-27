#!/usr/bin/env python3
"""PROME whole-INDEX BOARD diff-scan — the PULL that makes a §3.5 exemption sound.

WALTER's BOARD_CONSUMPTION_SPEC §3.5 grants a "pull-complete" exemption (WALTER
stops writing inbox handoffs) ONLY to a recipient that runs a *complete
whole-INDEX* BOARD scan. §3.5.1 states the reasoning explicitly: the exemption is
sound *only because* the recipient's BOARD-diff IS the pull, so the handoff is
pure redundancy. No pull -> no exemption. This script is PROME's pull.

Scope: EVERY BOARD signal since the cursor, not a tier or a sample. The
"complete" in whole-INDEX is load-bearing (REGINALD was refused the exemption in
v0.7 precisely because its scan was tiered).

Usage:
    python3 PROME/tools/board_scan.py                 # scan since cursor
    python3 PROME/tools/board_scan.py --advance       # scan, then move cursor
    python3 PROME/tools/board_scan.py --since 20260724
    python3 PROME/tools/board_scan.py --audit 20260701   # ACTION-line audit

Exit codes: 0 = nothing new or info-only; 1 = PROME is on an ACTION line
(boot must not proceed past this without dispositioning).
"""
import argparse
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(
    subprocess.run(["git", "rev-parse", "--show-toplevel"],
                   capture_output=True, text=True, check=True).stdout.strip())
BOARD = REPO / "BOARD"
CURSOR = REPO / "PROME" / "state" / "board_cursor.txt"

SIG_RE = re.compile(r"^SIG-W-(\d{8})-(\d+)")
ME = "PROME"


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--advance", action="store_true", help="write cursor to newest scanned")
    ap.add_argument("--since", default=None, help="YYYYMMDD floor, overrides cursor")
    ap.add_argument("--audit", default=None, help="YYYYMMDD — report every ACTION line for PROME")
    args = ap.parse_args()

    if not BOARD.is_dir():
        print(f"BOARD-SCAN ✗ no BOARD dir at {BOARD}", file=sys.stderr)
        return 2

    files = sorted((p for p in BOARD.glob("SIG-W-*.md")), key=lambda p: sig_key(p.name))
    if not files:
        print("BOARD-SCAN ✗ no signal files found", file=sys.stderr)
        return 2

    if args.audit:
        hits = 0
        for p in files:
            if sig_key(p.name)[0] < args.audit:
                continue
            fm = parse_front(p)
            if ME in [a.upper() for a in fm.get("action", [])]:
                hits += 1
                print(f"  ACTION  {fm.get('signal_id', p.name)}  {clean(fm.get('_headline'))}")
        total = sum(1 for p in files if sig_key(p.name)[0] >= args.audit)
        print(f"\nBOARD-SCAN audit since {args.audit}: {hits} ACTION-line / {total} signals for {ME}")
        return 0

    floor = args.since or load_cursor()
    new = []
    for p in files:
        d, n = sig_key(p.name)
        if args.since:
            if d < args.since:
                continue
        elif floor and p.stem.split("-md")[0][:len("SIG-W-YYYYMMDD-NNN")] <= floor:
            continue
        new.append(p)

    if floor and not args.since:
        new = [p for p in files if f"SIG-W-{sig_key(p.name)[0]}-{sig_key(p.name)[1]:03d}" > floor]

    if not new:
        print(f"BOARD-SCAN ✓ nothing new since {floor or '(no cursor)'}")
        return 0

    action, info, other = [], [], []
    for p in new:
        fm = parse_front(p)
        row = (fm.get("signal_id", p.stem), fm.get("cluster", "?"),
               fm.get("precedence", "?"), clean(fm.get("_headline")))
        acts = [a.upper() for a in fm.get("action", [])]
        infos = [a.upper() for a in fm.get("info", [])]
        (action if ME in acts else info if ME in infos else other).append((row, acts))

    print(f"BOARD-SCAN — {len(new)} new since {floor or '(no cursor)'}  "
          f"[{len(action)} action · {len(info)} info · {len(other)} not-{ME}]")

    if action:
        print(f"\n🔴 {ME} ON ACTION LINE — disposition before proceeding:")
        for (sid, cl, pr, hl), _ in action:
            print(f"   {sid}  [{cl}/{pr}]\n      {hl}")

    if info:
        print(f"\n📋 info-cc ({len(info)}) — owner in brackets:")
        for (sid, cl, pr, hl), acts in info:
            print(f"   {sid} [{','.join(acts) or '—'}] {hl}")

    if other:
        print(f"\n·  {len(other)} not routed to {ME} (listed for completeness):")
        for (sid, cl, pr, hl), acts in other:
            print(f"   {sid} [{','.join(acts) or '—'}] {clean(hl, 80)}")

    if args.advance:
        newest = max(f"SIG-W-{sig_key(p.name)[0]}-{sig_key(p.name)[1]:03d}" for p in new)
        CURSOR.parent.mkdir(parents=True, exist_ok=True)
        CURSOR.write_text(newest + "\n", encoding="utf-8")
        print(f"\ncursor → {newest}")

    return 1 if action else 0


if __name__ == "__main__":
    sys.exit(main())
