# 2026-08-06 — To: PROME (from the Will-directed 8/6 commit review) — three check extensions, proposal only

**Signal:** The 8/6 review of the 8/4-8/5 window found that nearly every defect was restated-state drift sitting just OUTSIDE the existing checks' scope. Three cheap extensions would have caught most of them. Proposal — route to DAEDALUS for build/ratification per normal check-adoption path; nothing here is installed.
**Priority:** 🟡. Findings basis: `reviews/2026-08-06_opus5-window-commit-review.md`.

## 1. Widen `claim_check`'s default file list (catches: 3 weekday errors this window)

Current scope (root canon 1e) is 13 decision files. The window's weekday errors lived in `AGENTS/*/NEXUS_BRIEF.md` and `AGENTS/*/reports/*.md` "As of:" headers (VIOLET 8/5-as-Tuesday, FALCON 8/2-as-Saturday, HEARTBEAT Amendment #1 8/2-as-Sat) — all outside the list. Proposed: add `AGENTS/*/NEXUS_BRIEF.md` + `HEARTBEAT.md` to the per-agent closeout invocation (reports/ are dated-historical; header-line-only scan would bound noise). The 1e scope note says scope came from measurement — this is new measurement: 3 hits / 0 FPs in those surfaces this window.

## 2. Ratification cross-check (catches: R1, the erased 8/4 proxy run — the window's worst defect)

One-grep shape, same family as `consumer_check`. When a commission packet ratifies proxy runs, the packet's ratify-list count must equal DOCKET's proxy-row count since the agent's last real boot. Sketch (≈30 lines, untested — DAEDALUS to harden):

```python
#!/usr/bin/env python3
"""ratification_check.py AGENT SINCE_DATE PACKET — count DOCKET proxy rows vs packet ratify-list."""
import re, sys
agent, since, packet = sys.argv[1], sys.argv[2], sys.argv[3]
docket = open("PROME/DOCKET.tsv", encoding="utf-8").read().splitlines()
runs = [r for r in docket if agent in r and "proxy" in r.lower()
        and re.search(r"EXECUTED (\d{1,2}/\d{1,2})", r)]
runs = [r for r in runs if re.search(r"20\d\d-\d\d-\d\d", r) and r.split("\t")[0] >= since]
body = open(packet, encoding="utf-8").read()
m = re.search(r"[Rr]atify[^.]*", body)
listed = len(re.findall(r"`[0-9a-f]{7,10}`", m.group(0))) if m else 0
print(f"DOCKET proxy rows since {since}: {len(runs)} | packet ratify-list: {listed}")
sys.exit(0 if listed >= len(runs) else 1)
```

Advisory (exit 1 = look, not block), run by PROME when writing a commission packet. On 8/5 it would have printed `DOCKET: 3 | packet: 2`.

## 3. Closeout stamp/numbering sanity (catches: M3 impossible "date-verified" stamps + M4 session-ID collision)

Two-line addition to closeout discipline (BRENT-class agents with stamped SCRATCH headers): (a) closeout stamp vs commit clock — |delta| > ~2h ⇒ warn (the 8/5 case was ~17h: a "~03:0x ⏰ date-verified" stamp on a 19:59 commit, carried from the prior session); (b) session number = prior SCRATCH's + 1, derived not restated (two closeouts both shipped "SESSION 5"). Could live in a closeout guard script (VIOLET's `closeout_guard.py` is the pattern) or as a checklist line — DAEDALUS's call.

## Not proposed

A general "restated-count" checker (the "~20 rows"/"12 defects"/"two runs" class) — the R1 instance is covered by #2, and the rest is what review passes are for; a generic count-verifier would be all false positives.

— Will-directed review session, 2026-08-06. Tier A mechanical fixes + 4 owner packets are on branch `claude/review-recent-commits-f8lwo2`; this packet is the only Tier C artifact.
