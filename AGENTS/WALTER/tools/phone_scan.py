#!/usr/bin/env python3
"""
phone_scan.py — sweep RESEARCH-INTAKE `phone_inbox/` for Will-originated phone signals.

PART B of the phone→fleet ingestion design
(`inbox/2026-07-05_from-PROME_phone-signal-ingestion-design.md`, Will-approved 7/5).

TRANSPORT
---------
Will's iOS Shortcut PUTs a file to the PRIVATE `williepowen-debug/RESEARCH-INTAKE`
repo via the GitHub Contents API:  `phone_inbox/signal_<ts>.md`
GitHub holds it durably — it cannot be dropped the way a Telegram message can.

⚠️ DELIBERATE DEVIATION FROM THE SPEC (§4), Will-approved 2026-07-27
--------------------------------------------------------------------
§4 said to archive consumed signals to `phone_inbox/processed/`. That would mean
WRITING to RESEARCH-INTAKE, which boot step 7e(a) forbids — that repo is READ-ONLY
to WALTER (`pull --ff-only`, never push), and it would have required a second PAT.

Instead: consumed signals are recorded in a seen-file ON OUR SIDE
(`registry/phone_seen.json`), mirroring the existing `intake_seen.json` model that
the spec itself points at. RESEARCH-INTAKE stays append-only from the phone and
read-only to WALTER. No new write permission, no second token, less code.

🔴 THE GOVERNING PRINCIPLE: NEVER SILENTLY DROP A WILL SIGNAL.
-------------------------------------------------------------
This system exists to buy DURABILITY. So every failure mode here SURFACES the file
rather than skipping it: malformed frontmatter, missing/unknown priority, empty
body, wrong `source:`, undecodable bytes, an unexpected filename — all are reported
LOUDLY and still handed to the operator. A filter that silently drops the thing it
was built to guarantee would be worse than no filter.
(Unlike `intake_scan.py`, nothing here is ever "suppressed as still-true": a phone
signal is a one-shot human utterance, not a standing condition.)

DEDUP
-----
Key = filename + sha256 of the raw bytes. Filename alone is not enough — the
Shortcut derives it from a timestamp, so two signals inside the same second would
collide; the content hash keeps them distinct. Once consumed, always consumed.

USAGE
  python3 AGENTS/WALTER/tools/phone_scan.py           # report NEW phone signals
  python3 AGENTS/WALTER/tools/phone_scan.py --mark    # record them as seen (AFTER routing)
"""
import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

LANE = Path("/home/willi/Research-Intake")
WALTER = Path(__file__).resolve().parent.parent

# TEST-ONLY injection points. RESEARCH-INTAKE is read-only to WALTER, so fixtures
# for the malformed-input cases cannot live in the real lane — these let the test
# harness point at a scratch dir without ever writing to that repo.
# Unset in normal operation; the defaults below are what production uses.
PHONE_DIR = Path(os.environ.get("WALTER_PHONE_DIR", LANE / "phone_inbox"))
SEEN = Path(os.environ.get("WALTER_PHONE_SEEN", WALTER / "registry" / "phone_seen.json"))
_TEST_MODE = "WALTER_PHONE_DIR" in os.environ

VALID_PRIORITY = {"🔴", "🟠", "🟡"}
DEFAULT_PRIORITY = "🟡"
SIGNAL_GLOB = "signal_*.md"
MAX_BYTES = 256 * 1024          # a phone signal is text; anything larger is suspect


def load_seen():
    if not SEEN.exists():
        return {"consumed": []}
    try:
        d = json.loads(SEEN.read_text(encoding="utf-8"))
        d.setdefault("consumed", [])
        return d
    except (json.JSONDecodeError, OSError) as e:
        # fail LOUD: a corrupt seen-file must not silently re-fire or silently swallow
        sys.exit(f"REFUSING TO RUN: {SEEN} is unreadable ({e}). Fix or delete it — "
                 f"deleting re-surfaces every phone signal, which is the safe direction.")


def parse_signal(path):
    """Parse one phone signal. NEVER raises for content reasons — returns warnings instead."""
    warn = []
    try:
        raw = path.read_bytes()
    except OSError as e:
        return {"path": path, "warn": [f"UNREADABLE: {e}"], "priority": DEFAULT_PRIORITY,
                "ts": None, "body": "", "sha": "", "source": None}

    sha = hashlib.sha256(raw).hexdigest()[:16]
    if len(raw) > MAX_BYTES:
        warn.append(f"OVERSIZE: {len(raw)} bytes (>{MAX_BYTES}) — truncated for display")
        raw = raw[:MAX_BYTES]
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("utf-8", errors="replace")
        warn.append("NOT VALID UTF-8 — decoded with replacement chars; body may be garbled")

    priority, ts, source, body = DEFAULT_PRIORITY, None, None, text

    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)\Z", text, re.DOTALL)
    if not m:
        warn.append("NO FRONTMATTER — whole file treated as body (format contract §5 not met)")
    else:
        fm, body = m.group(1), m.group(2)
        for line in fm.splitlines():
            if ":" not in line:
                continue
            k, _, v = line.partition(":")
            k, v = k.strip().lower(), v.strip()
            if k == "priority":
                if v in VALID_PRIORITY:
                    priority = v
                elif v:
                    warn.append(f"UNKNOWN priority {v!r} — defaulted to {DEFAULT_PRIORITY}")
            elif k == "ts":
                ts = v
            elif k == "source":
                source = v
        if source is None:
            warn.append("frontmatter has no `source:` — expected `phone`")
        elif source != "phone":
            warn.append(f"`source: {source}` is not `phone` — did something else write here?")
        if ts is None:
            warn.append("frontmatter has no `ts:`")

    if not body.strip():
        warn.append("EMPTY BODY — the signal carries no text")

    return {"path": path, "warn": warn, "priority": priority, "ts": ts,
            "body": body.strip(), "sha": sha, "source": source}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mark", action="store_true",
                    help="record the currently-listed signals as consumed (run AFTER routing)")
    args = ap.parse_args()

    print("PHONE-SIGNAL scan — RESEARCH-INTAKE/phone_inbox/")
    print("=" * 64)
    if _TEST_MODE:
        print(f"⚠️  TEST MODE — reading {PHONE_DIR} (NOT the live lane)")

    if not _TEST_MODE and not LANE.exists():
        sys.exit(f"lane missing at {LANE} — is RESEARCH-INTAKE cloned?")

    if not PHONE_DIR.exists():
        print("\n[status] `phone_inbox/` does not exist in the lane yet.")
        print("         PART A (Will's PAT + iOS Shortcut) has not been enacted, OR")
        print("         no signal has ever been sent. This is NOT an error.")
        print("         The sweep is live and will pick up the first signal automatically.")
        return 0

    seen = load_seen()
    consumed = set(seen["consumed"])

    files = sorted(PHONE_DIR.glob(SIGNAL_GLOB))
    # anything in phone_inbox/ that ISN'T a signal_*.md — surface, never consume
    strays = [p for p in sorted(PHONE_DIR.iterdir())
              if p.is_file() and p not in files and p.name not in {".gitkeep", "README.md"}]

    new, already = [], 0
    for p in files:
        sig = parse_signal(p)
        if f"{p.name}:{sig['sha']}" in consumed:
            already += 1
        else:
            new.append(sig)

    print(f"\n[files] {len(files)} signal file(s) · {already} already consumed · "
          f"{len(new)} NEW · {len(strays)} stray")

    if strays:
        print("\n⚠️  STRAY FILES in phone_inbox/ (not `signal_*.md`) — surfaced, NOT consumed:")
        for p in strays:
            print(f"     {p.name}")

    if not new:
        print("\n[NEW phone signals — 0]  (nothing to route)")
        return 0

    print(f"\n[NEW phone signals to ROUTE — {len(new)}]")
    print("Route each through the NORMAL signal-processing path (filter → BOARD →")
    print("handoff → delivery_log), tagged `source: phone`, carrying the priority hint.")
    print("These are WILL-ORIGINATED. Do not kill on Novelty without reading the body.\n")

    for i, s in enumerate(new, 1):
        print(f"  {i}. {s['path'].name}   priority {s['priority']}   ts {s['ts'] or '—'}")
        for w in s["warn"]:
            print(f"     ⚠️  {w}")
        preview = s["body"].replace("\n", " ")
        print(f"     │ {preview[:300]}{'…' if len(preview) > 300 else ''}")
        print()

    if args.mark:
        for s in new:
            consumed.add(f"{s['path'].name}:{s['sha']}")
        seen["consumed"] = sorted(consumed)
        SEEN.parent.mkdir(parents=True, exist_ok=True)
        SEEN.write_text(json.dumps(seen, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"--mark: recorded {len(new)} signal(s) as consumed → {SEEN.name}")
    else:
        print("After routing, run:  python3 AGENTS/WALTER/tools/phone_scan.py --mark")

    return 0


if __name__ == "__main__":
    sys.exit(main())
