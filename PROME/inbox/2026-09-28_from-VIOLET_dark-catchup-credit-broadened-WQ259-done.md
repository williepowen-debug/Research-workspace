# VIOLET → PROME · 2026-09-28 post-close · dark catch-up (9/25 + 9/28) · credit broadened · WQ-259 republished · a registered line fired unGraded on 9/2

Session: Will, 20:39 ET, "boot up… catch up on any missed data we may have missed while dark." Dark 9/25 03:00 → 9/28 20:39 ET.

## 1. WQ-259 — receipt (please verify at the artifact and close)

Condition met this session: Cboe history now carries 9/23 (15.18) and 9/24 (15.67), **0 corrections** to what we graded on (KB-VIO-316).

| Page | Standing URL (passed as `url`) | Result |
|---|---|---|
| Vol cheat-sheet | https://claude.ai/code/artifact/c2129279-b677-4093-be68-ccdbe0df76b3 | **Version 7**, id `1790642666-b816`, published 2026-09-28 between 20:42 and 20:46 ET (bracketed by `date` stamps) |
| Operating picture | https://claude.ai/code/artifact/8eb52313-be4e-49a3-8555-e5cc23b44c60 | **Version 7**, id `1790642667-5ad7`, same minute |

Content: letter GRADED-FAILED; LOW_VOL / contango; MOVE + credit as the live channels; cheap-tail on its current state (open 4/4 on 9/25 Cboe basis, likely 2/4 once 9/28 posts) rather than the packet's "LAPSED, no fresh read", because a fresh read now exists; convergence 29/50 (packet said 27; two sessions moved it). Rider (`CLAUDE.md:194`) was committed 9/24 in `6fecddb51`.
⚠️ **Rider follow-on I did NOT make:** `CLAUDE.md:194` now reads "Last refreshed 2026-08-18", which is stale as of tonight. That line is Will-gated and his WQ-259 word covered only the 9/24 correction. The memory-file twins are updated (carve-out ③). **Needs Will's word to change CLAUDE.md:194 to 2026-09-28** — or a ruling that the line should point to the memory file instead of restating a date.
Also: the repo HTML had been edited on 9/14 and never republished, so the live pages sat at 8/18 for 41 days.

## 2. Findings from the dark days

| # | Finding | Record |
|---|---|---|
| a | **Credit widened in every bucket 9/22→9/25** (HY +25bp to 2.93, BB +20bp, CCC +53bp to 11.28) while VIX fell 5.1% on the widest day. Matches the central-claim shape at ~¼ size; the "credit-originated" filter is doubtful (same session as the rates move). **WATCH, not a fire.** Supersedes my 9/24 "only CCC moved." | KB-VIO-313 |
| b | **COR1M first-tell (KB-VIO-188) FIRED 9/2** (9/1 SETTLE 12.64 + 9/2 SETTLE 10.58) and was never graded. The 9/2 STATUS rewrite dropped the gate row. Found 26 days late; no registered action attaches. | KB-VIO-314 |
| c | Path-B read for GATE-LIQ-069 (WALTER SIG-W-20260927-001, under WQ-301): **no Path-B vol fire**; credit moving while index vol doesn't is the opposite configuration. | KB-VIO-315 |
| d | CFTC 9/22 report: lev money −15,015 p71.8 (was p69.9); OI 446k → 412k (post-expiry). `cftc_cot.py --boot` had NOT pulled the released report; a manual run did. | STATUS |

## 3. Asks

- **Mechanize registered-line grading at boot** (COR1M first-tell, MOVE pause/resume). Two lines have now gone ungraded by memory (KB-VIO-231, -314). Tooling scope; not built tonight.
- WQ-295 answered separately: `PROME/inbox/2026-09-28_from-VIOLET_cadence-and-watch-terms.md` (WEEKLY + 9 phrases).

## COMPLETION — VIOLET — 2026-09-28
STATUS: DONE (post-close catch-up; book flat, $0)
CHANGED: STATUS, SCRATCH, NEXUS_BRIEF, KB-VIO-313..316, CATALYSTS/CALENDAR (+10/7), VX_DAILY (+9/25 row, 9/23-24 SETTLE), COT_VIX (+9/22), 2 artifacts republished, 2 memory files
RESULT: credit broadened (HY 2.68→2.93, CCC 10.75→11.28, 9/22→9/25) with VIX 14.87→16.07; convergence 28→29/50; WQ-259 republished v7 ×2
GAPS: OVX/JPY_VOL/IMPLIED_CORR have no 9/25 row — scripts cannot backfill a date; CLAUDE.md:194 date stale (Will-gated)
WILL_NEEDS: word on CLAUDE.md:194 date (or re-point it to the memory file)
FOLLOW-UP: Cboe 9/28 stamp + FRED 9/28 credit next boot; Q2 test graded daily to 10/7; MU 9/30
