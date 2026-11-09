# PROME state simplification — brainstorm and phased plan (PROPOSAL, not ruled)

**Asked by:** Will, PROME chat 2026-11-09 13:43 ET, verbatim *"lets have you brainstorm a plan for how we could best address this."* (following "Is this organized properly? Should we have a better system for this to make it easier for Prome?"). Author: PROME prome-6f. Status: brainstorm for Will's direction; nothing approved, nothing changed.

## 1. The problem, measured 2026-11-09 (`PROME/tools/measure.py`)

| Boot read | Size | What it mostly holds |
|---|---|---|
| PROME/SCRATCH.md | 20,467 B | ~6 lines of live to-do inside carried notes, rotation stamps and archive pointers |
| HEARTBEAT.md | 21,712 B | market picture (useful) + kill-on-sight lists + amendments |
| PROME/STATUS.md | 12,509 B | restrictions (useful) + a pointer index |
| PROME/HANDOFF.md | 5,472 B | last 5 sessions, each pointing back to SCRATCH |
| PROME/state/CALENDAR.md | 10,661 B | generated; works |
| PROME/BOOT.md + BOOT_MODULES.md | 24,389 + 21,480 B | the procedure itself |
| Charters (root + PROME CLAUDE.md) | 24,241 + 28,024 B | rules |
| PROME/WILL_QUEUE.md | 166,894 B | not read whole; gate + generated view |

Fleet: 48 agent directories, 43 STATUS files, 31 NEXUS_BRIEF files with no common header format.
This morning's boot took about 25 tool steps and still reported PARTIAL (six reads cut short or done by reasoning).

**Failure modes seen today:** (1) the same fact in several hand-written files that drift; (2) live state buried in history; (3) no one view of the fleet — PROME stitches DOCKET, GATES, ORCH_LOG, spawn slate, inbox and git; (4) a known defect sat as a note (SCRATCH: "ORACLE routine runs on both boxes and collides") until it broke Will's pull; (5) plans made mid-session live only in chat until closeout; (6) Will-launched sessions are invisible to PROME's records unless Will says so.

## 2. Principles
1. **One fact, one home.** Every other place shows it through a generated view, never a hand copy.
2. **Hand-written state is short and current.** History goes to the dated daily notes (`memory/YYYY-MM-DD.md`), which already exist.
3. **PROME reads views; ledgers feed views.** DOCKET, GATES, WILL_QUEUE and ORCH_LOG stay as the structured records.
4. **Write as you go.** A plan made at 13:00 is in the file at 13:00, not reconstructed at closeout.
5. **Fewer checks, more visibility** (Will 10/31). A view that shows "due, no answer" beside each desk replaces a check that has to be run and dispositioned.

## 3. Options considered

| Option | What | Verdict |
|---|---|---|
| A. Discipline only | Keep the files; write SCRATCH as you go | Free, start today; does not fix overlap or fleet visibility |
| B. Fleet board only | A generated one-page view of every desk | Biggest single win, low risk; does not fix PROME's own file sprawl |
| C. Board + one NOW page + prune | B, then merge HANDOFF, SCRATCH ★NEXT and the STATUS queue into one short NOW page, then cut duplicate boot steps | **Recommended**, in phases |
| D. Dashboard or app | A hosted page | No: Will reads only chat (10/31); the Helm was retired for this reason (WQ-461) |
| E. Give fleet state to NEXUS | NEXUS already reads every brief weekly | No: weekly is too slow, and NEXUS's job is market synthesis, not PROME's bookkeeping |

## 4. Target shape — boot reads four short things plus the gate

| Page | Hand or generated | Holds | Replaces |
|---|---|---|---|
| **NOW.md** (cap about 6 KB) | Hand, PROME, written as things happen | Ranked next actions; open threads with owner and when; "message X after Y" schedule; Will's standing words as a pointer list | HANDOFF, SCRATCH ★NEXT and carry blocks, STATUS work queue |
| **FLEET.md** | Generated at boot and closeout | One line per desk (section 5) | Spawn slate top block, SCRATCH desk lines, PROME's stitching |
| **CALENDAR.md** | Generated (exists) | Dated obligations | — |
| **HEARTBEAT.md** | Hand, PROME | Market picture and kill-on-sight | — (trim later, separately) |
| Gate output + inbox | Generated | Problems, unread packets | — |

STATUS keeps only its Restrictions (binding rules). The pending-Will line and the book line move to NOW, still generated.

## 5. Fleet board design (Phase 1)

A script builds `PROME/state/FLEET.md` from sources that already exist, no new files asked of desks:
- `PROME/ROSTER.md` → who is active, dormant or special
- `git log` → last commit per desk directory: date and subject
- `PROME/DOCKET.tsv` → open rows per owner, overdue count, next due date
- `PROME/GATES.tsv` → live rows per owner, any past review
- `PROME/state/ORCH_LOG.tsv` → PROME's last touch and closeout state (asked→receipt, went dark)
- `PROME/tools/inbox_census.py` → unread count per desk, oldest item age
- the desk brief (`NEXUS_BRIEF.md`) → first status line and its last-refresh date, where a recognisable one exists; otherwise "brief: no header"

One line per active desk, e.g.:
`BRENT · last commit 11/9 12:12 "reopen read…" · due: L1089 today · gates: 2 live · inbox 0 · PROME touch 11/9 spawn, open · brief 11/6: "Energy WAIT retained"`

Sorted: anything due or unanswered first. It is a view, not a gate: nothing blocks, nothing needs a written disposition.
Live sessions (ListAgents) cannot be read by a script; PROME adds a "live now" marker by hand at boot, or the board just omits it.

## 6. Phases

| Phase | What | Who | Needs Will's word? | Measure |
|---|---|---|---|---|
| 0 (today) | Write the next-steps and message schedule into SCRATCH as they happen; record today's boot as the baseline | PROME | No | Baseline: about 25 steps, PARTIAL with 6 skipped |
| 1 | Build FLEET.md generator plus tests; PROME reads it beside the old reads for one week | DAEDALUS (fleet architect), one session, $0 | Yes, to commission | Does the board answer "what is each desk doing / owing" without other reads? |
| 2 | NOW.md replaces HANDOFF, SCRATCH ★NEXT/carry and the STATUS queue. Every SCRATCH carry line is mapped to a DOCKET row, NOW, or explicitly archived, so nothing is dropped. BOOT, CLOSEOUT and the PROME charter are updated. | PROME drafts; independent read | Yes (canon and charter) | Boot steps, skipped controls, places a fact is written |
| 3 | Prune boot reads and checks made redundant by 1 and 2. Each removal is listed with what it used to catch. | PROME proposes, Will rules per item | Yes, per removal | Boot steps and time vs baseline |

## 7. Risks
- **Transition loses an obligation.** Mitigation: the Phase 2 mapping table; nothing leaves SCRATCH without a named new home.
- **Desk briefs are inconsistent.** Mitigation: the board leans on structured sources first; the brief line is a bonus.
- **Canon churn.** Mitigation: one phase at a time; Phase 1 changes no rules.
- **The board becomes another file to maintain.** It is generated, never hand-edited, like CALENDAR.

## 8. Open questions for Will
1. Commission Phase 1 (DAEDALUS builds the board)?
2. Agree the Phase 2 direction (one NOW page replacing HANDOFF, SCRATCH and the STATUS queue), with the actual text coming back for your word?
3. Anything you want on each desk's line (e.g. its held positions or its current conviction)?
