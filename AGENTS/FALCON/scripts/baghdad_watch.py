#!/usr/bin/env python3
"""
baghdad_watch.py — Boot-time Baghdad / Green Zone security-alert monitor.

Watches the unfired CONFIRM-D discriminator #5: Iran-aligned PMF/Kataib
Hezbollah backlash — rockets/drones on the Green Zone / US Embassy Baghdad /
US positions in Iraq (STATUS.md:69,82; inbox/WALTER/processed/
SIG-W-20260628-003.md:16 — the inverted Iraq tail flagged 6/28).

Source: US Embassy Baghdad security-alert RSS
(https://iq.usembassy.gov/category/alert/feed/) — verified live 200 on
2026-07-10 with a browser User-Agent (site blocks default fetchers).
ACLED = phase-2 backup (free registration, ~7-10d lag); the Washington
Institute militia-attack tracker died Dec-2024.

FLAG-NOT-FIRE: this script never declares the discriminator fired. Kinetic-
keyword hits print "REVIEW" — disposition is HAWK's judgment call.

Exit codes (HAWK has no standing multi-rc convention — frozen boot.py used
0/1 — so per build spec):
  0 = quiet, or new generic/caution alerts only
  1 = new REVIEW-flagged alert(s) — possible D-discriminator event
  2 = fetch/parse failure (fail LOUD; never fabricate or silently skip)

State: baghdad_watch_state.json alongside this script (committed — seen
GUIDs + last-run travel across machines). Cwd-proof via Path(__file__).

Built by DAEDALUS 2026-07-10 (Will-approved, Tier-3 gap #5 — see
AGENTS/DAEDALUS/outbox/2026-07-10_to-PROME_tier3-gaps-and-power-agent-memo.md)
"""
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

FEED_URL = "https://iq.usembassy.gov/category/alert/feed/"
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
STATE_PATH = Path(__file__).resolve().parent / "baghdad_watch_state.json"
KINETIC = re.compile(r"\b(drone|rocket|missile|mortar|uas|attack|militia|"
                     r"strike|idf|indirect fire)\w*", re.IGNORECASE)
SILENCE_DAYS = 30


def fetch_items():
    req = urllib.request.Request(FEED_URL, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        root = ET.fromstring(resp.read())
    items = []
    for it in root.iter("item"):
        get = lambda tag: (it.findtext(tag) or "").strip()
        pub = None
        if get("pubDate"):
            try:
                pub = parsedate_to_datetime(get("pubDate"))
            except (ValueError, TypeError):
                pass
        items.append({"title": get("title"), "link": get("link"),
                      "guid": get("guid") or get("link"), "pub": pub,
                      "desc": get("description")})
    return items


def main():
    try:
        items = fetch_items()
    except Exception as e:
        print(f"baghdad_watch: FETCH/PARSE FAILURE — {e!r}\n"
              f"Feed: {FEED_URL}\nDo NOT assume quiet; verify channel "
              f"manually (embassy on ordered departure).", file=sys.stderr)
        return 2

    state = {"seen": [], "last_run": None}
    if STATE_PATH.exists():
        state = json.loads(STATE_PATH.read_text())
    seen = set(state["seen"])
    first_run = state["last_run"] is None

    new = [it for it in items if it["guid"] not in seen]
    review = 0
    for it in new:
        stamp = it["pub"].strftime("%Y-%m-%d") if it["pub"] else "undated"
        if KINETIC.search(f"{it['title']} {it['desc']}"):
            review += 1
            print(f"⚠️ NEW ALERT — REVIEW: possible D-discriminator event "
                  f"[{stamp}] {it['title']}\n   {it['link']}")
        else:
            print(f"ℹ️ new alert (generic/caution) [{stamp}] {it['title']}\n"
                  f"   {it['link']}")

    # Feed-silence signal: newest pubDate >30d old is itself a signal.
    dates = [it["pub"] for it in items if it["pub"]]
    if dates:
        newest = max(dates)
        age = (datetime.now(timezone.utc) - newest).days
        if age > SILENCE_DAYS:
            print(f"🔇 Feed silence: newest embassy alert is {age}d old "
                  f"({newest:%Y-%m-%d}). Quiet OR drawdown artifact (embassy "
                  f"on ordered departure) — verify channel is live.")
    else:
        print("🔇 Feed returned no dated items — verify channel manually.")

    if new:
        print(f"Baghdad channel: {len(new)} new alert(s) — {review} flagged "
              f"REVIEW{' (first run: baseline init)' if first_run else ''}")
    else:
        newest_it = max((it for it in items if it["pub"]),
                        key=lambda it: it["pub"], default=None)
        last = (f"{newest_it['pub']:%Y-%m-%d} ({newest_it['title']})"
                if newest_it else "unknown")
        print(f"Baghdad channel: QUIET — last embassy alert {last}, 0 new")

    seen.update(it["guid"] for it in new)
    state = {"seen": sorted(seen)[-500:],
             "last_run": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    STATE_PATH.write_text(json.dumps(state, indent=1) + "\n")
    return 1 if review else 0


if __name__ == "__main__":
    sys.exit(main())
