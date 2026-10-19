#!/usr/bin/env python3
"""prome_digest.py — the L2 PRESENCE layer (WQ-184 leg ④ / L293).

Runs Research-workspace's own `PROME/tools/spawn_list.py --horizon 1 --tsv` inside a read-only
clone and posts ONE Telegram message: DUE rows with a DARK owner (what WQ-184 L0 would spawn at
the next PROME boot), rows landing within a day, Will-owned due rows, and the OVERDUE count.
No session, no commit, no spawn. A failure posts a failure line — silence is never a result.

Usage:
  python3 scripts/prome_digest.py --repo rw            # in Actions (secrets from env)
  python3 scripts/prome_digest.py --repo . --dry-run   # local: print, post nothing
Env (Actions secrets): TELEGRAM_BOT_TOKEN · TELEGRAM_CHAT_ID
Exit: 0 posted (or dry-run) · 1 the digest could not be built (a failure line was posted) · 2 the post itself failed
"""
import argparse, datetime as dt, json, os, subprocess, sys, urllib.request, urllib.error
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
TERMINAL = ("RESOLVED", "SUPERSEDED", "TOMBSTONE", "WITHDRAWN", "CANCELLED", "DONE", "CLOSED")


def run_spawn_list(repo: str) -> tuple[str, int]:
    """spawn_list.py exits 1 when a DARK row exists — that is a RESULT, not a failure. rc>=2 or empty = failure."""
    p = subprocess.run([sys.executable, "PROME/tools/spawn_list.py", "--horizon", "1", "--tsv"],
                       cwd=repo, capture_output=True, text=True, timeout=120)
    if p.returncode >= 2 or not p.stdout.strip():
        raise RuntimeError(f"spawn_list rc={p.returncode}: {(p.stderr or p.stdout).strip()[:400]}")
    return p.stdout, p.returncode


def overdue_count(repo: str, today: dt.date) -> int:
    """PENDING rows dated before today with no terminal disposition — docket_view's OVERDUE definition."""
    n = 0
    with open(os.path.join(repo, "PROME", "DOCKET.tsv"), encoding="utf-8") as fh:
        for line in fh:
            if not line or line.startswith("#"):
                continue
            cells = line.rstrip("\n").split("\t")
            if len(cells) < 4:
                continue
            try:
                d = dt.date.fromisoformat(cells[0][:10])
            except ValueError:
                continue
            status = cells[3].strip().upper()
            if d < today and status.startswith("PENDING") and not status.startswith(TERMINAL):
                n += 1
    return n


def build_message(tsv: str, overdue: int, now: dt.datetime) -> str:
    lines = tsv.rstrip("\n").split("\n")
    header = lines[0] if lines else "spawn_list (no header)"
    rows = [l.split("\t") for l in lines[2:] if l.strip()]   # line 1 = column names
    dark, lands, will, other = [], [], [], []
    for r in rows:
        if len(r) < 7:
            other.append(" ".join(r)[:120]); continue
        key, due, _dd, owner, cls, _basis, cat = r[:7]
        key = key.replace("⚠️", "").strip()
        item = f"{key} {owner} {due} — {cat[:90].strip()}"
        c = cls.upper()
        if c == "DARK":
            dark.append(item)
        elif c.startswith("LANDS"):
            lands.append(item)
        elif c.startswith("WILL"):
            will.append(item)
        else:
            other.append(f"{cls}: {item}")
    out = [f"PROME digest · {now:%a %Y-%m-%d %H:%M} ET · {header.replace('spawn_list · ', '')}"]
    out.append("DUE with DARK owner → open PROME; WQ-184 L0 spawns these at the next boot:" if dark
               else "DUE with DARK owner: none")
    out += [f" • {x}" for x in dark]
    if lands:
        out.append("Lands within 1d:"); out += [f" • {x}" for x in lands]
    if will:
        out.append("Will-owned due (WILL_QUEUE, never spawned):"); out += [f" • {x}" for x in will]
    if other:
        out.append("Other:"); out += [f" • {x}" for x in other]
    out.append(f"OVERDUE (PENDING past date, docket_view rule): {overdue}")
    out.append("This job reads only. No session, no commit, no spawn.")
    msg = "\n".join(out)
    return msg if len(msg) <= 3900 else msg[:3850] + "\n…(truncated)"


def post(text: str) -> None:
    token, chat = os.environ.get("TELEGRAM_BOT_TOKEN"), os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat:
        raise RuntimeError("TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID missing from env")
    body = json.dumps({"chat_id": chat, "text": text, "disable_web_page_preview": True}).encode()
    req = urllib.request.Request(f"https://api.telegram.org/bot{token}/sendMessage", data=body,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.loads(resp.read().decode())
    if not payload.get("ok"):
        raise RuntimeError(f"telegram: {payload}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, help="path of the Research-workspace clone")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    now = dt.datetime.now(ET)
    try:
        tsv, _rc = run_spawn_list(a.repo)
        text = build_message(tsv, overdue_count(a.repo, now.date()), now)
        rc = 0
    except Exception as e:  # a failure is a message, never silence
        text = f"PROME digest · {now:%a %Y-%m-%d %H:%M} ET · FAILED to build: {e}"
        rc = 1
    if a.dry_run:
        print(text); return rc
    try:
        post(text)
    except Exception as e:
        print(f"POST FAILED: {e}\n---\n{text}", file=sys.stderr); return 2
    print(text); return rc


if __name__ == "__main__":
    sys.exit(main())
