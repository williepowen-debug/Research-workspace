# Prome Cleanup Plan — 2026-05-07

**Mode:** read-only audit completed; this file is the control tracker for cleanup execution.

## Executive Diagnosis

The workspace problem is not mostly storage clutter. It is **authority drift**: multiple “current state” files disagree, several live queues are Mar/Apr-era stale, and newer WALTER/BOARD work has become fresher than Prome root files.

Most important finding: **HEARTBEAT.md, PROME/TODAY.md, PROME/STATUS.md, PROME/POSITIONS.md, FORGE/STATUS.md, and FORGE/ACTIVE_TRADES.md are not reliable current-state authorities without refresh.** Agent STATUS files and BOARD/WALTER are fresher.

## Ground Truth Sources Found

| Surface | State | Action |
|---|---:|---|
| `AGENTS/*/STATUS.md` | freshest agent state; many updated May 4-6 | use as primary read source |
| `BOARD/INDEX.md` + `BOARD/SIG-W-*` | fresh through May 6 | preserve; likely signal ground truth |
| `AGENTS/WALTER/` | fresh through May 6 | preserve; do not prune casually |
| `PROME/HANDOFF.md` | fresh May 5 | use as boot handoff |
| `PROME/SCRATCH.md` | Apr 30; partially stale | rewrite after cleanup pass |
| `HEARTBEAT.md` | Apr 12; contradicts later handoff | demote or rewrite |
| `PROME/TODAY.md` | Apr 17 | rewrite or archive daily stale copy |
| `PROME/STATUS.md` | Apr 17 | regenerate from agent STATUS mtimes/inboxes |
| `PROME/archive/TOSCANINI_2026-03/QUEUE.md` | Historical | retired Toscanini queue archive; do not use as live state |
| `PROME/archive/TOSCANINI_2026-03/WILL_QUEUE.md` | Historical | retired Will-needs archive; live blockers now belong in `PROME/ACTIVE_DECISIONS.md` / `PROME/STATUS.md` |
| `PROME/POSITIONS.md` | Apr 2 | stale; replace with current snapshot workflow |
| `FORGE/ACTIVE_TRADES.md` | Mar 25 | stale; refresh only with Will/account data |
| `FORGE/STATUS.md` | Mar 26 | stale; likely not an authority |

## Current Live Snapshot From Audit

Market dashboard compact run on 2026-05-07 returned:
- HY OAS 277 🟢
- CCC OAS 911 🟡
- Brent $96.85 🟡
- Gas weekly $4.45 🔴
- USD/JPY 156.25 🟡
- Initial claims 200K; shadow-adjusted 255K
- KRE $70.71 🟢
- APO $129.53 🟡
- WAL $83.33 🟢
- VIX 17.37 🟢

Dashboard exited code 1 due red breach behavior, not necessarily script failure.

## Subagent State

- Active subagents: **none**.
- SCRATCH/HEARTBEAT references to running NEXUS/HANS subagents are stale.

## Unprocessed Inbox Backlog

| Agent | Count | Notes |
|---|---:|---|
| SHADE | 7 | old Mar/Apr but domain-critical insurance items |
| LABOR | 6 | old Apr claims/sweep signals |
| PROME | 5 | includes WALTER stale FORGE refresh request + Hermes batch |
| ZHAO | 3 | petrodollar/offshore signals |
| SAM | 2 | Walter liquidity + rig count |
| REGINALD | 2 | fresh May 4/6 WAL/CARL signals; persistent agent, don't edit casually |
| HANS | 2 | old Europe signals |
| HERMES | 2 | old delivery inputs |
| LIQUID | 1 | Apr 20 IMF liquidity |
| FERT/CRUISE/CREED | 1 each | probably setup/legacy |

## Cleanup Priorities

### Phase 1 — Re-establish Command Surface
**Goal:** make Prome boot into trustworthy state again.

1. Rewrite `PROME/SCRATCH.md` from this audit.
2. Replace `PROME/TODAY.md` with May 7 current state.
3. Regenerate `PROME/STATUS.md` from agent status mtimes + inbox backlog.
4. Mark `HEARTBEAT.md` explicitly stale/abandoned or rewrite it as thin pointer to agent STATUS files.
5. Update `PROME/HANDOFF.md` only after current cleanup completes.

**Risk:** low. Internal docs only.

### Phase 2 — Queue Surgery
**Goal:** remove March-era false urgency.

1. Completed: retired Toscanini files live under `PROME/archive/TOSCANINI_2026-03/`; do not rebuild them as live state.
2. Rebuild live queue with only May-relevant items:
   - OBDC/APO decision context
   - KRE roll timing/current chain if still relevant
   - WALTER → RED/BRENT/NEXUS requests
   - stale agent refresh list
3. Review `WILL_QUEUE.md`; mark W-002 and W-006 completed, drop/refresh expired APO Apr item.

**Risk:** medium. Queue semantics affect what gets surfaced to Will.

### Phase 3 — Inbox Triage
**Goal:** process signals without losing domain evidence.

Order:
1. PROME inbox first — tells us what the system itself asked for.
2. REGINALD fresh May files — read-only summary only; persistent agent owns folder.
3. LIQUID Apr 20 IMF signal.
4. SHADE backlog — insurance is still thesis-relevant.
5. LABOR/ZHAO/SAM old backlog — triage into processed/archive if superseded.
6. HERMES/HANS/FERT/CRUISE/CREED — likely archive/setup cleanup.

**Rule:** move to `processed/` only after summarizing relevance or confirming superseded.

### Phase 4 — Position/Forge Authority Reset
**Goal:** stop stale position docs from misleading decisions.

1. Do not trust `PROME/POSITIONS.md` or `FORGE/ACTIVE_TRADES.md` for current sizing.
2. Add visible stale banner until Will/account snapshot refresh is available.
3. If Will provides current screenshot/export, rebuild positions once.
4. Make one owner doc for positions; other docs should reference it.

**Risk:** high if we infer trades. Do not infer current holdings.

### Phase 5 — Structural Hygiene
**Goal:** reduce future cold-boot drag.

Candidates:
- Archive/demote inactive agents: DARWIN already in `_archive`; verify references removed.
- Clarify duplicate/inactive dirs: `RESEARCHER`, `BUFFER`, `EARNINGS`, `FOREX`, `REITS`, `TRADES`, root-level `CREED/DOC`.
- Add `archive/README.md` policy if missing.
- Keep large research outputs; do not delete. Storage is not the problem.

## Do-Not-Touch Without Care

- `AGENTS/CARL`, `AGENTS/REGINALD`, `AGENTS/SAM`, `AGENTS/RED`, `AGENTS/BRENT`: persistent/Claude-managed or active WALTER liaising. Read before edit; prefer inbox/self-contained signal over direct mutation.
- `BOARD/` and `AGENTS/WALTER/`: current signal pipeline; preserve.
- `FORGE/ACTIVE_TRADES.md`: do not rewrite without current account data.

## Recommended Starting Action

Start with **Phase 1**. It gives immediate cognitive relief and prevents stale boot state from poisoning every later decision. Then do Phase 2 queue surgery before touching individual agent inboxes.
