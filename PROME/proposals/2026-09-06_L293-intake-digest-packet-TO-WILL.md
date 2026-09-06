# L293 — the L2 PRESENCE layer: RESEARCH-INTAKE → Telegram daily digest (packet to Will)

**From:** PROME (`prome-04`, Sun 2026-09-06 ~10:3x ET) · **To:** Will · **Ruling basis:** WQ-184 leg ④ (Will 9/5 21:42 *"approve WQ-184 with your recs"*, APPROVED in principle) + WQ-185 ④ KEEP (Will 9/6 10:12). DOCKET L293 (dated 9/8) is discharged by this packet; your half is **WQ-187**.

**What it does:** a second, read-only GitHub Actions workflow in the private `williepowen-debug/RESEARCH-INTAKE` repo (the lane you chose 6/29 over a VPS) runs **weekdays ~06:15 ET and Sundays ~08:15 ET**, clones `Research-workspace` read-only, runs `PROME/tools/spawn_list.py --horizon 1 --tsv` exactly as the PROME boot gate does, and posts ONE Telegram message: the DUE rows with a DARK owner (the ones WQ-184 L0 would spawn at the next PROME boot), the rows landing within a day, the Will-owned due rows, and the OVERDUE count. **No session, no commit, no spawn, $0 compute** (Actions minutes on a private repo: ~1 min/run, inside the free tier). If the job fails it posts a failure line — a silent job is a dead job (`[[finding_liveness_gate_keyed_on_an_artifact_that_must_exist_first]]` class), so quiet days still post a one-liner.

**What PROME never sees:** the three secrets. **What PROME cannot do:** commit to the intake repo (outside the `PROME/` grant). On your word I write the two files below into the local clone `/home/willi/Research-Intake/` and you push; or you paste them.

---

## Your hands (in order) — ~15 minutes

1. **Read-only PAT for `Research-workspace`.** GitHub → Settings → Developer settings → Personal access tokens → **Fine-grained** → Generate: Resource owner = you · Repository access = *Only select repositories* → `Research-workspace` · Permissions → Repository → **Contents: Read-only** (Metadata read is added automatically) · expiry: the maximum you are comfortable with (the job posts a failure line when it expires — that is the reminder). Copy the token.
2. **Telegram bot + chat id.** Reuse the Prome bot's token if you already have one on the desktop (`env_doctor`'s "telegram channel tokens" extra names it; `PROME/MACHINE_LOCAL.md` inventory) — otherwise BotFather → `/newbot` → token. Chat id: send the bot any message, then open `https://api.telegram.org/bot<TOKEN>/getUpdates` in a browser and read `chat.id` (a channel id is negative and starts `-100…`; that works too if the bot is a channel admin).
3. **Three repository secrets** in `RESEARCH-INTAKE` → Settings → Secrets and variables → Actions → New repository secret: **`RW_READ_TOKEN`** (step 1) · **`TELEGRAM_BOT_TOKEN`** · **`TELEGRAM_CHAT_ID`**.
4. **Commit the two files** (`.github/workflows/prome_digest.yml` + `scripts/prome_digest.py`, full text below) to `RESEARCH-INTAKE` and push. *(Or say the word and PROME writes them into `/home/willi/Research-Intake/` for you to `git push`.)*
5. **First run by hand:** Actions → `prome-digest` → *Run workflow*. The Telegram message should arrive within ~2 minutes. If nothing arrives, the Actions log's last step says which secret or path failed. Then it runs itself.

Local dry-run without any secret (from the Research-workspace root, prints the message and posts nothing):
```
python3 /home/willi/Research-Intake/scripts/prome_digest.py --repo . --dry-run
```

---

## File 1 — `.github/workflows/prome_digest.yml`

```yaml
name: prome-digest

on:
  workflow_dispatch:          # first run by hand
  schedule:
    # GitHub cron is UTC and does NOT observe DST (same caveat as collect.yml).
    # 10:15 UTC = 06:15 EDT / 05:15 EST  — weekdays, before Will's ~06:00 ET start settles
    # 12:15 UTC = 08:15 EDT / 07:15 EST  — Sunday (the weekend gap the box does not cover)
    - cron: '15 10 * * 1-5'
    - cron: '15 12 * * 0'

permissions:
  contents: read              # this job never writes to either repo

concurrency:
  group: prome-digest
  cancel-in-progress: false

jobs:
  digest:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4          # RESEARCH-INTAKE (for scripts/prome_digest.py)

      - uses: actions/checkout@v4          # Research-workspace, READ-ONLY; full history because
        with:                              # spawn_list.py reads `git log` for owner liveness
          repository: williepowen-debug/Research-workspace
          token: ${{ secrets.RW_READ_TOKEN }}
          path: rw
          fetch-depth: 0

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Build and post the digest
        env:
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
          TELEGRAM_CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
        run: python3 scripts/prome_digest.py --repo rw
```

## File 2 — `scripts/prome_digest.py`

```python
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
```

---

## Notes PROME verified before drafting

- `spawn_list.py --horizon 1 --tsv` prints a one-line header (`spawn_list · as-of … · DARK n · ACTIVE n · lands-ahead n · PROME n · WILL n`), a column line (`key due Δd owner class basis catalyst`) and one tab-separated row per candidate; **rc=1 when a DARK row exists** (that is its L0 signal, not an error) — the script above treats only rc≥2 or empty output as failure. Run at 10:3x ET today it listed L123 BRENT DARK, three LANDS-IN-1d rows and one WILL-owned row.
- Liveness in `spawn_list.py` = `git log` of the clone for the owner's last self-commit (subject-leading desk name), hence `fetch-depth: 0`; a shallow clone would read every desk as DARK.
- The OVERDUE definition mirrors `scripts/docket_view.py`'s header rule (PENDING rows dated before as-of with no terminal disposition); the digest labels it as such. If docket_view's rule changes, this count drifts — it is a convenience figure, the DARK list is the payload.
- DST: GitHub cron is UTC; the ET times shift by an hour in winter (05:15 / 07:15 ET). Acceptable; adjust the cron in November if the weekday post lands before you are up.
- Cost: two checkouts + one Python run ≈ 1 minute per run × 6 runs/week; the Research-workspace full clone is the slow step (~10,200 commits). If it ever exceeds the 10-minute `timeout-minutes`, a failure line posts and `fetch-depth` can be raised to a bounded number (≥ the longest desk cadence gap; 60 days of history has always covered liveness so far).

## What PROME does after your word
Adds the digest to `PROME/MACHINE_LOCAL.md` (machine-independent presence layer, secret names only) and to the Boot Trust Stack tool list; L293 already RESOLVED by this packet; the digest's first real message is the leg-⑥ delivery check at L291 (9/19).
