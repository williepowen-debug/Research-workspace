# Agent catch-up plan — 2026-10-21 evening (session prome-56b, boot 21:57 ET)

**Owner:** PROME · **Will's word (21:56 ET):** *"I want us to work on getting our agents caught up that need it. First generate a plan. Then you may spawne agents as you see fit and orchestrate them."* That word is the research nod and the usage nod for tonight's wakes; the WQ-184 per-boot cap is read as superseded by it for this session and the reading is stated in the boot report. Every wake is Tier 1 (approved workstream: its own DOCKET/GATES rows and its own inbox); nothing new-direction is commissioned; no trade, threshold or score change is authorized by this plan.

## Who needs catching up — the survey (instruments: `git log -- AGENTS/<X>/ ':(exclude)…/inbox'` for own-work age; `PROME/tools/inbox_census.py` for backlog; DOCKET open rows by owner; `agent_freshness.py` clear-to-brief on each)

| Desk | Own work last | Inbox (top · WALTER lane) | Due / overdue rows | Live window? | Disposition |
|---|---|---|---|---|---|
| LIQUID | 10/19 (2d) | 7 · 32 — largest backlog in the fleet | L568 OVERDUE 10/9 (next step is Will's: name the WQ-404 reader); HY >320 run count owed to HEARTBEAT; GATES LIQ-069/072/076/079 | no | **Wave 1** |
| VIOLET | 10/19 (2d) | 4 · 7 | L667 OVERDUE 10/14 (tooling rider); VIX monthly expiration 10/21 summons | no | **Wave 1** |
| SHADE | 10/15 (6d) | 1 · 3 | L726 + L727 due 10/23 (illiquidity basis · TSR method) | no | **Wave 1** |
| CORAL | 10/15 (6d) | 2 · 4 | GATE-CORAL-MSI-01 weekly reading due 10/22; L227 convergence window (bank rail Q3 re-test, late Oct) | no | **Wave 1** (Florida = top-priority geography) |
| AEOLUS | 10/10 (11d) | 5 · 5 | L650 10/23 (C3 reconcile with WATT); read-cap attestation owed | no | **Wave 2** |
| FLG | 10/01 (20d) | 6 · 2 | L522 Q3 print Fri 10/23 06:00 ET (HARD, issuer PR); T-07/T-08/T-12 re-dated 10/23 | no | **Wave 2** — pre-print frame tonight (frame-before-filing), print read Friday |
| ORACLE | 10/16 (5d) | 2 · 1 | L729 daily $110-oil pull (reads owed 10/20 · 10/21); WQ-453 RULED packet unconsumed (GATES row waits on ORACLE's encode) | no | **Wave 2** |
| GIBBS | 10/20 (1d) | 5 · 2 | L704 OVERDUE 10/19 (37 per-print extractions pending; NTRS printed 10/21, AXP 10/23) | no | **Wave 2** |
| CARL | 10/15 (6d) | 2 · 8 | no dated row; BOARD gap 6 aged action signals (gate ACTION OWED) | no | **Wave 3** (BOARD-gap packet lands tonight regardless) |
| MARCO | 10/14 (7d) | 3 · 3 | none | no | Wave 3 |
| DEWEY | 10/17 (4d) | 9 · 4 | none dated (on-demand desk) | no | Wave 3 / Will's call |
| CREED | 10/01 (20d) | 9 · 28 | L723 '450 Fifth St NW' auction 10/28 | no | ⚖️ **Will's explicit permission required** (ROSTER standing rule) |
| WALTER | 10/21 (live) | — | L755 OVERDUE 10/20 (bookmark exact-ID binding), L334 OVERDUE 10/15 | yes, idle (walter-14) | message the live window with the L755 re-ping; do not spawn |
| BRENT · HENRY · HANS · YURI | 10/21 (live) | — | current | yes (Will's windows) | nothing to add tonight |
| TERRY | 10/20 (1d) | 6 · 0 · WILL 2 | BOARD gap 1 aged signal (HY 331 three closes) | no | packet only |
| Tomorrow-morning wakes (not tonight) | — | — | LABOR L719 08:30 · RED L35 after the 10:00 EGBN call · WATT L717 · BROCK L740 PM · REGINALD/VLY L521 (est.) · 10/23 NEXUS L751, OSPREY L666/L718 | — | next boot's spawn list |
| Fresh, no wake | REGINALD · RED · OZK · OSPREY · LABOR · HAWK · FALCON · FERT · DAEDALUS · CATO · BROCK · WAL · WATT · VULCAN · SAM · NEXUS · MIDAS · BOND · ZHAO · HOMER · CRUISE · OTTO | — | — | — | — |

## Execution
- **Wave 1 now** (four `desk` spawns, Opus, concurrent): LIQUID · VIOLET · SHADE · CORAL. Each: whole-inbox drain (every sender; BOARD rows logged per WALTER's spec), its named rows graded at its own letter, STATUS re-stamped, own full closeout, dated memo to `PROME/inbox/` + COMPLETION block by message.
- **Wave 2** as wave-1 returns are consumed (verified at the commit, not the message): AEOLUS · FLG · ORACLE · GIBBS.
- **Wave 3** if usage allows: CARL · MARCO; DEWEY and CREED on Will's word.
- **PROME between waves:** consume each return at its artifact; ORCH_LOG rows (1-SPAWN → receipt → WQ-249 closeout ask); BOARD-gap packets to CARL and TERRY; WALTER L755 message; closeout.
- **Preflight:** `ListAgents` immediately before each wave; a desk with a live peer session is messaged, never spawned.
- **Cost note for Will:** eight Opus desk sessions in one evening is the heaviest PROME-spawned load since 10/20; Will's 21:56 word is the authorization and he can stop any wave by saying so.
