# Claude Code Prome Handoff
**Updated:** 2026-05-17 (Phase 3 dry run) ET
**Surface:** Claude Code Prome
**Run type:** Phase 3 dry run — readiness audit, no mutating edits outside this file.

> **Hash-refresh note (2026-05-17 evening cleanup pass):** The "Repo Hygiene Snapshot" table below has been updated to current HEAD (`8a44dbe2`). The dry-run report itself was performed at HEAD `e87724e1` and committed as `dddce166`. The "Stale Docs / Contradictions Identified" findings are preserved as the original dry-run record; several have since been addressed in this cleanup pass — see the new "Current Session" section appended at end of file.

---

## Identity / Model Confirmation

**One Prome, two work surfaces — confirmed.**

- Telegram/OpenClaw Prome owns Will-facing conversation, synthesis, approvals, decision rails, external sends.
- Claude Code Prome (this session) owns repo-native implementation: docs, tools, audits, handoffs, scoped edits.
- Shared state lives in `PROME/`, `AGENTS/`, `HEARTBEAT.md`, `MEMORY.md`, etc. No private truth layer. No fork of memory.
- I do **not** message Will directly, execute trades, push commits, or impersonate a separate identity. I am Prome on a different work surface.

Boot reading completed this session: `CLAUDE.md`, `AGENTS.md`, `SOUL.md`, `USER.md`, `PROME/CLAUDE.md`, `PROME/CLAUDE_CODE_PROME.md`, `PROME/CLAUDE_CODE_PROME_PLAN.md`, `PROME/CLAUDE_CODE_PROME_TASKS.md`, `PROME/SYSTEM.md`, `PROME/HANDOFF.md`, `PROME/STATUS.md`, `PROME/TODAY.md`, `HEARTBEAT.md`, `MEMORY.md`, plus cross-reference reads of `PROME/SCRATCH.md`, `PROME/BOOT.md`, `PROME/CLAUDE_CODE_HANDOFF.md` (this file pre-edit), and `AGENTS_DIRECTORY.md`.

---

## Repo Hygiene Snapshot

| Dimension | State |
|---|---|
| Branch | `master` |
| Local HEAD | `8a44dbe2` ("SENTRY: feed update 2026-05-17-2240") |
| `origin/master` | matches HEAD |
| Working tree | clean before this cleanup pass; dirty during the pass itself |
| Recent commit chain | `8a44dbe2` ← `dddce166` ← `e87724e1` ← `728e9f78` ← `270b6d1d` (WALTER closeout → Prome state refresh → handoff clear → Phase 3 dry run record → SENTRY feed update) |
| Phase 0 (planning) | ✅ Complete |
| Phase 1 (bootstrap files) | ✅ Complete — all four scaffold files present |
| Phase 2 (architecture integration) | ✅ Complete — AGENTS_DIRECTORY.md, PROME/SYSTEM.md, PROME/BOOT.md all carry Claude Code Prome references |
| Phase 3 (dry run) | ▶️ Running now |

Scaffold files verified present and coherent:
- `PROME/CLAUDE.md` — bootstrap, identity, one-Prome/two-surfaces, boot sequence, git discipline.
- `PROME/CLAUDE_CODE_PROME.md` — longer operating manual, allowed/ask-first/forbidden lists.
- `PROME/CLAUDE_CODE_PROME_PLAN.md` — architecture rationale.
- `PROME/CLAUDE_CODE_PROME_TASKS.md` — phased task ladder.
- `PROME/CLAUDE_CODE_HANDOFF.md` — this file.

---

## Stale Docs / Contradictions Identified

1. **`PROME/CLAUDE_CODE_HANDOFF.md` was 2 commits stale.** It said local `master` = `origin/master` at `270b6d1d`. Actual HEAD is `e87724e1`. Fixed in this update.
2. **`PROME/STATUS.md` carries the same `270b6d1d` claim** ("Latest Sync / Architecture State" → "GitHub sync ✅ Complete | Pulled cleanly; local `master` = `origin/master` at `270b6d1d`."). STATUS.md is Telegram/OpenClaw-owned; flagging only, not editing.
3. **`PROME/HEARTBEAT.md` Operating Notes** asserts "PROME/SCRATCH.md, PROME/CLAUDE_CODE_HANDOFF.md ... are refreshed / clear-ready as of May 17 10:45 ET." True for SCRATCH.md (post-`e87724e1` clear) but the CLAUDE_CODE_HANDOFF.md was older than the SCRATCH.md until this dry run. Same flag — Telegram/OpenClaw to refresh on its next pass if it matters.
4. **`AGENTS_DIRECTORY.md` runtime table omits RED and OZK from the Claude Code runtime row.** Root `CLAUDE.md` lists `CARL*, REGINALD*, OZK*, SAM*, RED*` (`* = Claude Code`); AGENTS_DIRECTORY.md only lists `REGINALD, CARL, SAM`. Either CLAUDE.md or AGENTS_DIRECTORY.md needs reconciliation. Recommend updating AGENTS_DIRECTORY.md (the directory is younger / more easily reconciled than the root rules file).
5. **`MEMORY.md` "Last Updated: 2026-04-05"** at the top — over a month stale at the index level. Daily entries in `memory/YYYY-MM-DD.md` are fresher; MEMORY.md itself appears curated long-term so the staleness may be intentional. Worth Will/Telegram Prome confirming whether a weekly maintenance pass is overdue.
6. **`PROME/TOSCANINI/QUEUE.md` flagged stale** in SYSTEM.md and STATUS.md ("⚠️ Stale until rebuilt"). Known issue, not a new finding.
7. **`FORGE/STATUS.md` flagged stale** per Prome inbox signal (per SYSTEM.md). Known issue.
8. **Phase 4 first task collision.** `PROME/CLAUDE_CODE_PROME_TASKS.md` Task 4.1 says "Create `PROME/action-cards/TEMPLATE.md`" — but that file **already exists** (alongside `FSK_MAY11_ACTION_CARD.md` and `REGIONAL_BANK_WEEKEND_TRIAGE_MAY9.md`). Phase 4 should be reframed as "audit / refine existing TEMPLATE.md against acceptance criteria" rather than "create from scratch." Flagging so Telegram/OpenClaw Prome knows before assigning Phase 4.
9. **`PROME/HANDOFF.md`** explicitly says the *next* session priority is "install Agents View" — orthogonal to the Phase 3 dry-run path. Not a contradiction (different work, both queued), but Telegram/OpenClaw Prome should be aware that Will may flip between the two streams.

No active blockers preventing Phase 3 → Phase 4 progression. All issues above are documentation hygiene or minor reconciliation, not gating.

---

## What Changed This Session

- Read all required boot files plus cross-reference docs.
- Verified scaffold integrity, git cleanliness, and Phase 2 integration completeness.
- Updated this file (`PROME/CLAUDE_CODE_HANDOFF.md`) with the dry-run report.

## Files Edited

- `PROME/CLAUDE_CODE_HANDOFF.md` (this file) — full rewrite to report Phase 3 dry-run results.

No other files touched. No commits, pushes, stashes, resets, deletes, external messages, or domain-agent edits.

---

## Phase 3 Acceptance Check

| Criterion (from PLAN.md) | Result |
|---|---|
| Understands one-Prome/two-surfaces | ✅ Confirmed at top of this file. |
| Does not try to message Will directly | ✅ No external action attempted. |
| Identifies stale docs and blockers | ✅ See "Stale Docs / Contradictions" section above. |
| Leaves a clean handoff | ✅ This file. |

---

## Decisions Needed from Will

1. **Pass Phase 3 dry run?** If yes, Claude Code Prome can proceed to Phase 4.
2. **Phase 4 scope clarification.** TEMPLATE.md already exists. Want me to (a) audit and refine the existing file against PLAN/TASKS acceptance criteria, or (b) substitute a different bounded first real task (e.g., reconcile AGENTS_DIRECTORY.md runtime row to include RED + OZK)?
3. **Autonomous internal edits going forward?** Current recommendation in PLAN.md: yes for scoped Prome docs; commits still gated on approval.
4. **Commit policy.** Current recommendation: Claude Code Prome leaves uncommitted diffs; Telegram/OpenClaw Prome or Will commits. Confirm or relax.

---

## Risks / Blockers

- **None blocking** the dry run itself.
- **Soft risks:** stale references in STATUS.md / HEARTBEAT.md (commit hash drift), Phase 4 task description vs reality mismatch, AGENTS_DIRECTORY.md / root CLAUDE.md runtime-row contradiction. None of these gate further work; they will compound if not addressed within a few sessions.

---

## Next Suggested Work (post-dry-run)

**Recommended:** Phase 4 audit pass on `PROME/action-cards/TEMPLATE.md`.

- Scope: read the existing TEMPLATE.md, compare against Plan §"Decision Artifact Buildout" + TASKS.md §Task 4.1 acceptance criteria, identify gaps, propose a small refinement diff.
- Why this is the safest next task: bounded to one file, no cross-agent state, exercises the Claude Code Prome edit/handoff loop on real content rather than meta-docs, and resolves the Phase 4 collision noted above.
- Output: a proposed diff plus an updated handoff, no commit until approval.

**Alternate bounded task (if Will prefers a different first real edit):** reconcile `AGENTS_DIRECTORY.md` runtime table with root `CLAUDE.md` agent list (add RED + OZK to the Claude Code runtime row, or remove them from root if the directory is authoritative). Equally bounded, single-file diff.

**Out of scope for next CC-Prome session:** Toscanini QUEUE rebuild, FORGE/STATUS.md refresh, Agents View install (Will-directed Telegram/OpenClaw thread), trade decision prompts. These belong to Telegram/OpenClaw Prome or are Will-gated.

---

## Rules I Held To This Session

- No commits, pushes, pulls, stashes, resets, or deletes.
- No external messages.
- No edits outside `PROME/CLAUDE_CODE_HANDOFF.md`.
- No domain-agent file edits.
- No persistent-agent spawns (CARL, REGINALD, SAM, RED, BRENT).
- No `git add -A` or `git add .`.
- Read-before-edit honored.

---

## Current Session — Cleanup Pass (2026-05-17 evening ET)

**Run type:** Will-directed self-cleanup; addresses dry-run findings + context refresh.
**HEAD at start:** `8a44dbe2`. Working tree clean before edits.

**Decisions received from Will this session:**
- Phase 3 — PASSED.
- Autonomous internal-edit rights — SCOPED YES. Free within `AGENTS/PROME/` and `PROME/`. Propose-then-approve for other agents' files, root-level CLAUDE.md, shared infrastructure. Approval required for anything outside `~/Research-workspace/`.
- Commit policy — show-diff-then-approve, always for now. Push only on explicit instruction.

**Context update absorbed:**
- Agent View install: ✅ done on this machine + laptop. Persistent dashboard / session manager now operational.
- New active experiment: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. Teams maps more directly than vanilla Agent View onto the chief-of-staff / named-teammates / mailbox / shared-task architecture we've been building. Small bounded test planned, likely later today.
- The "install Agents View" priority in `HANDOFF.md` is superseded — refreshed accordingly.

**Files edited this session (all in autonomous scope):**
- `PROME/STATUS.md` — hash `270b6d1d` → `8a44dbe2`.
- `PROME/TODAY.md` — hash `270b6d1d` → `8a44dbe2`.
- `PROME/HANDOFF.md` — HEAD hash + Clear Handoff section rewritten to "Active Thread" (Agent View done, teams experiment is new thread).
- `PROME/SCRATCH.md` — hash references brought current.
- `PROME/CLAUDE_CODE_HANDOFF.md` (this file) — hash refresh in snapshot table + this Current Session section.
- `PROME/CLAUDE_CODE_PROME_TASKS.md` — Task 4.1 reframed from "Create TEMPLATE.md" to "Audit/refine existing TEMPLATE.md."

**Propose-only (not edited; awaiting approval):**
- `AGENTS_DIRECTORY.md` Runtime row reconciliation (the CARL/REGINALD/OZK/SAM/RED contradiction with root `CLAUDE.md`). Proposal: align AGENTS_DIRECTORY.md to root CLAUDE.md as the more recently-authoritative source. Details in session output.

**Three softer-inconsistency questions answered with recommendations (not acted on):**
- `MEMORY.md` root staleness.
- `AGENTS/PROME/CLAUDE.md` "OpenClaw" framing.
- `AGENTS/PROME/LAST_COMPLETION.md` + trailing-off inboxes.

See conversation log for the full recommendations.

**Next session start:**
- Pull, confirm clean.
- If teams experiment fires today, read this section + `PROME/HANDOFF.md` Active Thread for the latest state.
- The dry-run "Stale Docs / Contradictions Identified" section above is now partially obsolete — items 1, 2, 5 (hash drift) are resolved; item 8 (Phase 4 collision) is resolved; items 3, 4, 6, 7, 9 are unresolved or out of scope for this pass.

---

## Current Session — 2026-05-18 (Orchestral Layer Prototyping)

**Run type:** Will-directed CC-Prome session. Prototype orchestral-layer Step 1 (fleet scan) + Step 4 (revival proxy); retire TOSCANINI; create CLOSEOUT.md; refresh BOOT.md.

**Working tree at start:** clean, synced to origin.
**Working tree at close:** clean within PROME/, AGENTS/PROME/, and root CLAUDE.md scope. `AGENTS/LIQUID/inbox/*_prome-spawned.md` left untracked deliberately — revival proxy outputs for LIQUID to own.

### What landed

1. **TOSCANINI retired + salvaged.** AUTONOMY.md and COMPLETION_SPEC.md promoted to `PROME/`. HUNTING ranking dimensions distilled into a "Ranking criteria for Section 6" subsection of `PROME/ORCHESTRAL_LAYER_DESIGN.md`. Remaining 8 files + `reports/` archived to `PROME/archive/TOSCANINI_2026-03/`. `PROME/TOSCANINI/` removed.

2. **Step 1 (fleet scan) prototype — v1 + v2.** First test of the context-discipline-via-subagent pattern. v1 produced rough but useful output; v2 incorporated six explicit fixes (two-column staleness, dormant pre-filter, merged loops, explicit HUNTING math, math discipline, as-of price labels). v2 is production-ready; lives at `PROME/FLEET_SCAN.md`.

3. **Step 4 (revival proxy) prototype — LIQUID.** First Step 4 run. Foreground general-purpose subagent (NOT teams mode) briefed as revival proxy for 32d-stale LIQUID. Produced revival packet + STATUS draft in `AGENTS/LIQUID/inbox/` with PROVENANCE preamble + `prome-spawned` filename suffix. Headline diagnostic: bear thesis migrated PLUMBING → DURATION (10Y +30bps over 32d, TLT broke 🔴, while HY OAS only -5bps). April SOFR-IORB scare was mechanical tax-day TGA, not structural.

4. **Live dashboard refresh.** `python3 FORGE/tools/market-data/dashboard.py` after activating venv. Score 10 CRITICAL. Key prints: HY OAS 280 (+4, 20bps from 260 kill), Brent $109.30 (BRENT's intraday $102 was a swing, not the close — HEARTBEAT held), 10Y 4.59 broke 🔴, TLT $83.56 broke 🔴, APO $134.07 (🔴→🟢 zone change), VIX 17.82, BIZD $12.52.

5. **CLOSEOUT.md created + BOOT.md cleaned.** First standardized CC-Prome closeout procedure: 4 chunks (state files / memory / residuals / git+report), scope tiers (Light/Standard/Heavy), file-ownership reference, skip rules. BOOT.md patched in 5 places to remove TOSCANINI drift and integrate new orchestral-layer surfaces.

### Files edited (within autonomous scope)

| File | Action |
|---|---|
| `PROME/ORCHESTRAL_LAYER_DESIGN.md` | Added "Ranking criteria for Section 6" subsection |
| `PROME/STATUS.md` | Pending Work table refreshed; Active Decision Layer refreshed; Next Best Action rewritten |
| `PROME/SCRATCH.md` | Full rewrite for closeout |
| `PROME/CLAUDE_CODE_HANDOFF.md` (this file) | Appended this session entry |
| `PROME/BOOT.md` | 5 edits: Doc Ownership table, Boot Sequence steps 4 & 8, Toscanini section → Orchestral Layer section, On-Demand line |
| `PROME/AUTONOMY.md` | NEW (salvaged from `TOSCANINI/`) |
| `PROME/COMPLETION_SPEC.md` | NEW (salvaged from `TOSCANINI/`) |
| `PROME/CLOSEOUT.md` | NEW (standardized closeout procedure) |
| `PROME/FLEET_SCAN.md` | v1 + v2 written by `fleet-scanner` subagent |
| `PROME/archive/TOSCANINI_2026-03/` | NEW dir with 8 files + `reports/` subdir |
| `AGENTS/PROME/CLAUDE.md` | Boot sequence step 4 & 6 retargeted; Key Files table refreshed |

**Will-approved shared-file edit (one):**
- Root `CLAUDE.md` — Key Directories table phrase "TOSCANINI governance" → "FLEET_SCAN, ORCHESTRAL_LAYER_DESIGN, AUTONOMY"

**Untracked-by-design (NOT staged):**
- `AGENTS/LIQUID/inbox/LIQUID_REVIVAL_PACKET_2026-05-18_prome-spawned.md`
- `AGENTS/LIQUID/inbox/LIQUID_STATUS_DRAFT_2026-05-18_prome-spawned.md`
- These are revival-proxy outputs for LIQUID to own. Real LIQUID integrates and commits on next boot per agent-file-isolation rule.

### Commits

- Mid-session: `5558d180` — "PROME: retire TOSCANINI; orchestral fleet-scan v2 prototype" (after rebase over upstream `1cdd9443`)
- Closeout: separate commit

### Decisions made by Will this session

- ✅ Spawn fleet-scanner v1 with prescribed brief
- ✅ Iterate to v2 with six explicit fixes
- ✅ TOSCANINI retire + 6-step salvage approved
- ✅ Root CLAUDE.md TOSCANINI mention fixed
- ✅ Commit salvage + v2 fleet-scan mid-session (durability against 529 overload)
- ✅ Run live dashboard
- ✅ Spawn LIQUID revival proxy (Step 4 prototype)
- ✅ CLOSEOUT.md adopted as drafted
- ✅ BOOT.md items 1-6 patched
- Deferred: BOOT.md medium-priority items (agent ID table reconciliation, git protocol example tightening) → dedicated maintenance session
- Deferred: fold v3 fleet-scan feedback into design doc → next session

### Risks / Blockers

- **None blocking** the closeout itself.
- **Soft:** HEARTBEAT.md prices are 1-day stale (today's dashboard not propagated; shared file, Will-approval gate). OZK STATUS still shows pre-roll posture (hygiene; OZK refreshes own STATUS).
- **Pattern-level open question:** Revival-proxy files in another agent's inbox sit untracked until target agent boots. If that delay is long, they live in working-tree limbo. Worth a v3 design-doc note.

### Step 4 (revival proxy) — pattern feedback for v2 of the pattern

Surfaced by the LIQUID proxy run, parked here for fold-in:
1. **Directional semantics** — brief should state kill-level direction ("kill = bull floor; rising OAS = thesis healing").
2. **Time series in pass-through** — proxy had 4 HY OAS data points across 32d; future briefs should include 5-7-point series.
3. **Sweep-file triage** — inbox sweep files contain many signals; brief should call for sweep-internal triage when sweeps dominate.
4. **Closeout authorization** — proxy unsure whether to declare April SOFR-IORB "resolved mechanical"; brief should authorize/disauthorize closeout of prior open questions.

### Next Suggested Work

Open with Will at session start:
- **HENRY revival proxy** (Step 4 prototype #2; NVDA Tuesday catalyst pressure), OR
- **BROCK revival proxy** (Step 4 alt; APO sustained $130+, FSK fresh-premium blocker), OR
- **Fold v3 fleet-scan feedback into ORCHESTRAL_LAYER_DESIGN.md first** (~15 min), then revival.

Will-direction carries from FLEET_SCAN.md Section 7: SAM FXY Tranche 2 (FXY $57.80 below forfeit band), APO Jun/Dec puts hold/roll, FSK fresh-premium discussion, WAL Q1 10-Q integration.

### Rules I Held To

- No commits outside `PROME/`, `AGENTS/PROME/`, and Will-approved root `CLAUDE.md`.
- No `git add -A` or `git add .`.
- No edits to other agents' files (LIQUID revival proxy outputs left untracked for LIQUID to own).
- No persistent-agent spawns. (LIQUID revival was via proxy — does NOT spawn LIQUID itself, writes to LIQUID's inbox for next-boot integration.)
- No trades. No external messages.
- Read-before-edit honored.
- Behavior-language used in state files (not hash references) per cross-session memory.

---

## Current Session — 2026-05-19 (v3 brief spec + HENRY + BROCK revivals)

### What landed

Full session narrative in `PROME/SCRATCH.md`. One-line referents:
- Live Monday dashboard pull (essentially unchanged from Friday close)
- HENRY revival proxy (Step 4 #2) — pattern generalized to market-structure agent; returned framing-precision overlay as new artifact type
- HENRY framing-precision note — Will-authorized cross-agent inbox write; new artifact type canonized
- v3 brief spec folded into `PROME/ORCHESTRAL_LAYER_DESIGN.md` (9 items, 7-section consolidation, 3 of 4 open questions resolved)
- BROCK revival proxy (Step 4 #3) — first exercise of v3 brief spec; surfaced position-specific vs broad-thesis trigger conflation + WALTER NDFI scope-correction REQ
- LIQUID end-to-end revival-proxy validation (real LIQUID booted, integrated, committed 3× during session)

### Files edited (within autonomous scope)

- `PROME/SCRATCH.md` — full rewrite (this session's state)
- `PROME/STATUS.md` — surgical update (Pending Work, Active Decision Layer, Next Best Action)
- `PROME/CLAUDE_CODE_HANDOFF.md` — this entry
- `PROME/ORCHESTRAL_LAYER_DESIGN.md` — header status + Prototype path Steps 1/2/4 + new Revival-proxy v3 brief spec section + Open questions resolution
- `AGENTS/HENRY/inbox/HENRY_REVIVAL_PACKET_2026-05-18_prome-spawned.md` — proxy output, untracked
- `AGENTS/HENRY/inbox/HENRY_STATUS_DRAFT_2026-05-18_prome-spawned.md` — proxy output, untracked
- `AGENTS/HENRY/inbox/HENRY_FRAMING_NOTE_2026-05-18_prome-spawned.md` — Prome-authored framing overlay, untracked
- `AGENTS/BROCK/inbox/BROCK_REVIVAL_PACKET_2026-05-19_prome-spawned.md` — proxy output, untracked
- `AGENTS/BROCK/inbox/BROCK_STATUS_DRAFT_2026-05-19_prome-spawned.md` — proxy output, untracked
- `memory/2026-05-19.md` — daily session log (new)

### Decisions Will made this session (retrospective audit)

- Dashboard first, then HENRY revival.
- Endorsed "trap clinching" concept; rejected "2 of 3 firing" literal count; flag as framing-precision note to HENRY's inbox.
- Per-instance cross-agent inbox write authorization for HENRY framing note (NOT durable; default-forbidden rule still applies).
- Fold v3 feedback into ORCHESTRAL_LAYER_DESIGN.md before next revival.
- BROCK revival next (first v3-spec exercise).
- Closeout after BROCK; defer VIOLET pair to next session.
- Fix doc-ownership overlap + CLOSEOUT spec drift during closeout (post-audit follow-up commit).

### Decisions needed from Will (forward-looking)

See `PROME/SCRATCH.md` §Next Planned Work for live carries (APO put hold/roll/cut after BROCK memo; FSK fresh-premium; SAM FXY Tranche 2; WAL 10-Q integration; VIOLET pair decision).

### Risks / Blockers

- **None blocking** the closeout itself.
- **Soft:** HEARTBEAT.md prices remain 1+ day stale; OZK STATUS still pre-roll posture (hygiene). APO put decision genuinely overdue, surfaces to Will once BROCK boots and writes the domain memo — do not pre-empt.
- **Pattern-level:** three sets of revival packets (LIQUID 5/18, HENRY 5/18, BROCK 5/19) sitting untracked. If real-agent boot is long-delayed for any of them, packets live in working-tree limbo. The longer this latency, the staler the packet's tape pass-through becomes — worth a v4 design-doc note on packet shelf-life.

### v4 design inputs returned this session (parked for next ORCHESTRAL update)

From BROCK proxy:
1. **Position-specific vs broad-thesis trigger distinction** — explicit in §2 spec
2. **Outbox scan** (peer outboxes for outstanding REQs ≤14d) — add to read budget
3. **Sponsor-bifurcation diagnostic** as new artifact type (parent-level leverage/flexibility tell from sponsor responses)
4. **Decoupling-within-complex flag** as new artifact type (alt-mgr equity decoupling from underlying vehicle stress)

### Next Suggested Work

Open with Will at session start:
- **VIOLET revival proxy** (Step 4 #4) — pairs with HENRY for NVDA 5/20 read-through; second exercise of v3 brief spec on a vol agent
- Will-decision carries: APO put hold/roll/cut (post-BROCK memo, needs execution mark), FSK fresh-premium (data ready), SAM FXY Tranche 2, WAL 10-Q integration (REGINALD-owned)
- v4 brief-spec items defer to a maintenance pass unless next revival surfaces same issues

### Rules I Held To

- No commits outside `PROME/`, `AGENTS/PROME/`.
- No `git add -A` or `git add .`.
- No edits to other agents' files except the Will-authorized HENRY framing note (per-instance only).
- No persistent-agent spawns (HENRY + BROCK revivals via proxy; do NOT spawn the real agents).
- No trades. No external messages.
- Read-before-edit honored.
- Behavior-language in state files (not hash references) per cross-session memory.
- Sub-agent prompt discipline applied: decision-lead, scoped read budget, verdict-first deliverables, COMPLETION block required.
- Chunked closeout updates (3 state files sequenced, not batched).

---

## Current Session — 2026-05-19 PM (BOND teams-mode spawn experiment)

### What landed

Full narrative in `PROME/SCRATCH.md`. One-line referents:
- Live Monday dashboard pull (post-morning-closeout) — corroborates BOND's 12:10 signal
- **BOND spawned in teams mode** (first domain-agent teams-spawn) — alive, handshake refined two-track frame + flagged **5/21 10Y reopening** as second-leg thesis-escalation gate
- Teams-view troubleshooting: `Shift+Down` didn't work; diagnosed WSL2 tmux env propagation gap; `~/.claude/settings.json` updated with `"teammateMode": "tmux"`
- Restart pending: Will exits Claude Code + relaunches from inside `prome` tmux session; BOND respawn validates the fix

### Files edited (within autonomous scope)

- `PROME/SCRATCH.md` — full rewrite (afternoon session state)
- `PROME/STATUS.md` — surgical update (Pending Work + Active Decision Layer + Next Best Action)
- `PROME/CLAUDE_CODE_HANDOFF.md` — this entry
- `memory/2026-05-19.md` — appended afternoon log
- `~/.claude/settings.json` — **outside repo** — added `"teammateMode": "tmux"` key

### Decisions Will made this session

- Spawn BOND in teams mode (real BOND closed; no concurrency)
- Pursue teams-view visibility (vs accepting in-process invisibility)
- Light closeout (despite short session) — preserves 5/21 10Y leg, settings change, teams findings

### Decisions needed from Will (forward-looking)

See `PROME/SCRATCH.md` §Next Planned Work — TLT/20Y-10Y watch card scope; live carries (APO, FSK, FXY Tranche 2, WAL 10-Q, HEARTBEAT refresh) unchanged.

### Risks / Blockers

- **None blocking** the closeout itself.
- **Settings change unvalidated until restart.** If BOND respawn doesn't land in a pane, we need to re-diagnose (TMUX env propagation specifically, or in-process fallback).
- **Lifecycle question open:** how long do teams-mode teammates persist when idle? Worth testing — relevant for overnight survival to tomorrow's auction. Safer plan: respawn each session.
- **5/21 10Y reopening** is a new second-leg test BOND introduced; not yet propagated to HEARTBEAT or PREDICTIONS_MONITOR. Will-approval gate for HEARTBEAT.

### v_next design inputs returned this session

From BOND teams-mode experiment:
1. **Named-spawn proves teams-mode works for domain agents.** Boot via standard agent CLAUDE.md + IDENTITY reconstitution from files. No identity loss — fresh Claude reads same files as terminal-launched session.
2. **`teammateMode: auto` unreliable on WSL2.** Even with TERM=tmux-256color and Claude Code launched from inside a tmux session, the pane-split didn't fire. Explicit `teammateMode: tmux` required.
3. **No attach-from-separate-terminal exists.** Teammate views are always through the lead session (in-process cycle or tmux pane spawned by lead).
4. **One-shot subagent agentIds aren't resumable.** Foreground non-named spawns get cleaned up after their turn. Use named spawns (teams mode) when you want multi-turn.
5. **Commit-channel marking:** suggested `BOND (via teams):` prefix for commits from teams-spawned domain agents — audit trail for teams vs terminal channel. Not yet enforced; pattern only.

### Next Suggested Work

Open with Will at next-session start:
- **Respawn BOND** with same boot prompt — validate the tmux pane lands
- **TLT/20Y-10Y two-leg watch card** scope discussion (BOND already has the trigger criteria sharpened)
- Live Will-decision carries unchanged (see SCRATCH)

### Rules I Held To

- No commits outside `PROME/`, `AGENTS/PROME/`, plus `~/.claude/settings.json` (which is outside the repo — not a commit, just a local config write authorized by Will)
- No `git add -A` or `git add .`
- No edits to other agents' files (BOND teams-spawn was authorized to write to AGENTS/BOND/ but didn't — held at handshake)
- No persistent-agent spawns (BOND not on do-not-spawn list; teams-mode spawn validated)
- No trades. No external messages.
- Read-before-edit honored.
- Behavior-language in state files (not hash references).
- Chunked closeout updates (3 state files sequenced).

---

## Current Session — 2026-05-20 PM → 2026-05-21 (BOND post-auction read + background build-out + matrix v2 draft)

### What landed

Full narrative in `PROME/SCRATCH.md`. One-line referents:
- **5/20 20Y post-auction read** — BOND teams-mode respawn. Verdict: no orange escalation. Tail verified 0bp via verify-research sub-agent (ZH source). Commit `4eb21894` pushed. Posterior shift on 5/21 base-rate.
- **5-artifact BOND build-out** — WI sourcing playbook, auction history dataset (v1 + v2 enriched with `tail_vs_cmt_bps` + `indirect_pct_of_competitive`), cross-tenor base-rates analysis, escalation matrix backtest. Background sub-agents; PROVENANCE preambles + `_prome-spawned` suffixes.
- **Will-authorized inbox signal to BOND** — consolidated addendum reframing the 5/13 30Y (11th-pctile BTC) as the real May-refunding outlier vs the 20Y BOND had been focused on.
- **Matrix v2 draft via teams-mode DRAFT-ONLY pattern** — new artifact type. Iterative Will + Prome review through SendMessage over ~5 turns. Q1/Q3 resolved with BOND pushback on Prome misframings; Q2 parked; Q4 deferred-with-conditional-rule; Q5 open.

### Files edited (within autonomous scope)

- `PROME/SCRATCH.md` — full rewrite
- `PROME/STATUS.md` — surgical update (Pending Work table + Active Decision Layer + Next Best Action)
- `PROME/CLAUDE_CODE_HANDOFF.md` — this entry
- `memory/2026-05-21.md` — daily session log (new)
- 1 auto-memory entry (sub-agent backstops Prome reasoning errors — see MEMORY.md index)

### Files written by sub-agents (untracked-by-design; BOND owns commits)

- `AGENTS/BOND/research/WI_SOURCING_PLAYBOOK_prome-spawned.md`
- `AGENTS/BOND/data/auction_history_prome-spawned.csv` + `auction_history_v2_prome-spawned.csv` + `refresh_auction_history_prome-spawned.py` + `AUCTION_HISTORY_README_prome-spawned.md`
- `AGENTS/BOND/analysis/CROSS_TENOR_BASE_RATES_prome-spawned.md`
- `AGENTS/BOND/analysis/ESCALATION_MATRIX_BACKTEST_prome-spawned.md`
- `AGENTS/BOND/proposals/MATRIX_V2_DRAFT_prome-spawned.md`
- `AGENTS/BOND/inbox/SIG-PROME-BOND-2026-05-20_dataset-30Y-reframe_prome-spawned.md` (Will-authorized cross-agent inbox write)

### Decisions Will made this session

- Approve Tier A + Tier B BOND background tasks (then lay off, per "manageable amounts" framing)
- Approve push of BOND 5/20 20Y commit `4eb21894` (explicit authorization)
- Q1 indirect threshold → (c) per-tenor percentile, indirect-of-offering <15th-pctile trailing-12mo
- Q2 dealer-as-TRIM → park as future research thread (~3 weeks post-deploy)
- Q3 TLT puts budget → (c) middle path: 2-contract budget; 3rd contract via Will-touch ad-hoc
- Q4 deployment timing → DEFERRED with three-branch conditional rule resolving on today's 1pm 10Y print
- Q5 v2-native backtest re-run → OPEN, pair with Q4 branch
- Per-instance cross-agent inbox write authorization for SIG-PROME-BOND-2026-05-20 (NOT durable)

### Decisions needed from Will (forward-looking)

See `PROME/SCRATCH.md` §Next Planned Work. Q5 resolution after Q4 branch resolves. Live carries unchanged (APO, FSK, FXY Tranche 2, WAL 10-Q, HEARTBEAT refresh).

### Risks / Blockers

- **None blocking** closeout itself.
- **Soft:** 5/12 10Y fire under v2 is 0.5pp margin (tight); future near-boundary prints need explicit margin annotation. HEARTBEAT.md still ~3 days stale (Will-approval gate).
- **Pattern-level:** 5 BOND artifacts sitting untracked. Lower latency than prior revival packets — BOND was just here, his next boot is today (5/21 12:30 PM ET for auction prep). Working-tree-limbo risk is minimal.

### v_next design inputs returned this session

From the matrix v2 draft pattern:
1. **DRAFT-ONLY teams-mode spawn pattern.** New artifact type: domain agent spawned in teams mode, briefed to draft-only (NO live state file edits), output to `proposals/` subdir, iterative Will + Prome review via SendMessage over multiple turns. Worth canonizing alongside revival proxy + framing-precision overlay.
2. **Sub-agent pushback as backstop on Prome reasoning errors.** BOND caught a math error in Prome's Option-C synthesis (Q1) and pushed back with better domain framing. The "ask the domain expert to steelman" turn produced strictly better outcomes than Prome + Will alone. Saved as auto-memory.
3. **Conditional-rule deferral for branching decisions.** When a decision depends on a near-term data point (today's 10Y print), pre-committing a branched rule lets the data resolve mechanically rather than re-asking the question. Avoids second-decision overhead.
4. **5/12 10Y "false negative" framing.** The threshold-vs-percentile distinction caught BOND's matrix as having a systematic blind spot in long-end tenors. Lesson: per-tenor baselines diverge enough that flat thresholds embed a hidden uniformity assumption.

### Next Suggested Work

Open with Will at next-session start:
- **Pre-1 PM ET (today):** respawn BOND for pre-auction tape pull
- **Post-1 PM ET (today):** respawn BOND for post-auction verdict — mandatory dual-grade format → resolves Q4
- **Then:** Q5 decision (v2-native backtest re-run pre-deploy?) → v2 deployment in matching window
- Live Will-decision carries unchanged

### Rules I Held To

- No commits outside `PROME/` and `AGENTS/PROME/`.
- No `git add -A` or `git add .`.
- No edits to other agents' files except the Will-authorized SIG-PROME-BOND inbox signal (per-instance only).
- No persistent-agent spawns (BOND OK in teams mode + as sub-agent target).
- No trades. No external messages.
- Read-before-edit honored.
- Behavior-language in state files (not hash references).
- Chunked closeout updates (state files sequenced).
- DRAFT-ONLY discipline maintained for matrix surgery (no live AUCTION_HEALTH / STATUS / TRADE edits to BOND files).
- Math error in Q1 framing surfaced openly to Will before sending to BOND (didn't hide the correction).
