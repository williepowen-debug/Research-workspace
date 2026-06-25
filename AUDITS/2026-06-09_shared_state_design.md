# Shared-State Coordination Layer — Build Plan

**Author:** Claude Code (Will-requested), branch `claude/todays-repo-commits-w96on7`
**Date:** 2026-06-09
**Status:** Design + phased plan. Storage backend deliberately left as a runtime choice (designed both ways). One input pending (structured-substrate inventory) — refines the consolidation-map sizing, marked `[INV]` below.

---

## 0. The reframe that drives this plan

There are **two** problems that got tangled under "shared state":

1. **Git concurrency / races** (shared `.git/index`, the `8ac5bf71` mis-attribution). **Already solved on paper** by SAM's separate-clones-per-agent proposal (CARL-endorsed, slated post-Jun-16). Not re-solved here.
2. **Shared *truth*** — duplication, drift, and concurrency-blindness (agents citing each other as stale; opposite vol reads published the same hour, per the 6/9 coherence audit). **Not solved by anything today** — and separate-clones makes it *worse*, because isolated clones can only see *pushed* state, formalizing the same-day-blindness problem.

**Load-bearing conclusion: the shared-state layer and the separate-clones migration are one project.** The migration's pre-flight gate **P1** (proceed if <10% of cross-agent reads need unpushed state; rethink if >20%) is *driven down* by exactly this layer — if a sibling's state is in a shared store, no agent needs to read another's working tree. Build the state layer to make the migration safe; don't sequence them apart.

---

## 1. Design: two logical layers (storage-agnostic)

The layers are *logical*. The physical backend is a separate, deferrable choice (§3). The schema and the access CLI are identical either way.

### Layer 1 — Canonical current-values store (`STATE`): "what is true right now"

One row per shared metric/threshold/position. Written **once** by the owning agent; referenced (never copied) everywhere else.

| Field | Notes |
|---|---|
| `key` | canonical metric id — `hy_oas`, `vix`, `usdjpy`, `kre`, `pos.fxy` |
| `value` | the number/level |
| `status` | 🟢🟡🟠🔴 |
| `as_of` | ISO-8601 UTC |
| `source` | from `VOCABULARIES.tsv` SOURCE_TAGS (`FRED`, `yfinance`, `CFTC`…) |
| `source_date` | the data's own date (≠ when written) |
| `owner` | owning agent (single-writer-per-key) |
| `note` | ≤1 line context |

**The property that fixes the 6/9 vol conflict: single-writer-per-key.** Vol keys are owned by VIOLET (per Will's 6/6 scope ruling). HENRY *references* `vix`; he cannot write a competing value. The store *enforces* an ownership convention that today is only soft prose. STATUS files render from these rows (`HY OAS {{hy_oas}}, {{hy_oas.note}}`) instead of keeping N drifting copies.

A sibling `thresholds.tsv` holds the Y/O/R bands per key (`key · yellow · orange · red · kill · owner`) — consolidates the threshold tables scattered across every agent's STATUS + HEARTBEAT.

### Layer 2 — Append-only event/signal log (`EVENTS`): "what just happened"

Replaces inbox/outbox + `SIGNALS.md`; generalizes WALTER's BOARD + the fire-ledgers.

| Field | Notes |
|---|---|
| `event_id` | ULID/sortable-unique → **merge-safe across clones** (concurrent appends union cleanly) |
| `ts` | ISO-8601 UTC |
| `type` | `threshold_crossed` \| `signal` \| `prediction_resolved` \| `convergence` \| `position_change` \| `brief_updated` |
| `source_agent` | emitter |
| `to` | recipient chain (canonical agent names, comma-sep) |
| `subject` | metric/claim (canonical where possible) |
| `transition` | `🟢→🟡` etc. (for threshold/status events) |
| `priority` | 🔴🟠🟡 |
| `domain` | NETWORK_GROUPS / BOARD cluster |
| `ref` | link to detail file (BOARD `SIG-W-…`, prediction id, research output) |
| `body` | 1-3 line summary |

**Consumption replaces the inbox file-shuffle:** each agent keeps a **cursor** (`agent · last_event_id · disposition · note`) and reads events after its cursor addressed to it. This is WALTER's existing `board_log.tsv` disposition pattern (`acted|noted|deferred|info-only|skipped`) generalized fleet-wide. No files moved inbox→processed; no HERMES.

### Scope discipline — what does NOT go in shared state

Only **facts agents share** get structured. **Thinking agents do** stays agent-authored prose: analysis, thesis narrative, MEMORY, CHANGELOG, research outputs, NEXUS synthesis. STATUS becomes *rendered facts + agent prose*, not a structured essay. Don't try to schematize judgment.

---

## 2. Why this survives the known failure modes

| Failure mode (documented) | How the design survives it |
|---|---|
| Shared `.git/index` race (`8ac5bf71`) | Orthogonal — fixed by separate-clones. Layer 2 is append-only with unique IDs, so even pre-migration it avoids edit-conflict on a shared file. |
| Push-train cascade | Unaffected; events/values are normal commits that ride the train. Append-only = no rebase conflicts. |
| Pull-stash-lose | Reduced: agents stop reaching into siblings' working trees (that's what P1 measures), so fewer dirty-tree hazards. |
| Concurrency-blindness (6/9 audit) | Layer 1 single-writer-per-key + timestamps surface the conflict; Option B (§3) eliminates it outright. |
| Post-clones same-session blindness | Option A bounds it to push cadence; Option B removes it. Explicit fork for Will. |

---

## 3. The storage fork — designed both ways (Will's call, deferrable)

**Identical logical schema + identical access CLI (`state.py`).** Only the backend swaps. Build the CLI once; pick/flip the backend later.

### Option A — Git-native files (`STATE/` at repo root)
- `STATE/values.tsv`, `STATE/thresholds.tsv`, `STATE/events.tsv` (append-only), `STATE/cursors/<agent>.tsv`, `STATE/ownership.tsv`, `STATE/triggers.tsv`.
- CLI is a dumb fast local script: `state get hy_oas` · `state set hy_oas 276 --status 🟡 --source FRED` · `state emit --type signal --to SAM …` · `state inbox SAM`.
- **Pro:** git stays the *sole* source of truth; zero new infra; survives ephemeral containers; fully compatible with separate-clones (append-only merges).
- **Con:** cross-clone freshness bounded by push cadence — a sibling's same-session write is invisible until push→pull.

### Option B — VPS-hosted service (same schema)
- Layer 1 + recent Layer 2 in SQLite on the **persistent VPS** (already your coordination hub — PROME/WALTER live there) behind a tiny HTTP/CLI API. Both platforms read/write live.
- VPS snapshots `values.tsv` + appends `events.tsv` to git every N minutes → git remains the **durable** archive.
- **Pro:** kills concurrency-blindness entirely — instant cross-agent, cross-platform, same-session visibility. Directly fixes the thing that burned us 6/9.
- **Con:** philosophy shifts to "git = durable truth, VPS = live truth"; a (small) service to run; local platform needs network to the VPS.

**The CLI abstracts the backend**, so this is genuinely deferrable: ship Option A, and if same-session blindness still hurts after the clones migration, flip the same CLI to Option B without touching any agent's instructions.

---

## 4. Consolidation map — what folds where (mostly reuse, not greenfield)

Already-structured infrastructure that promotes into the two layers:

| Existing artifact | Folds into | Notes |
|---|---|---|
| `HEARTBEAT.md` dashboard + threshold table | Layer 1 `values` + `thresholds` | HEARTBEAT becomes a render |
| Per-agent STATUS dashboards / threshold tables | Layer 1 (reference) | prose analysis stays |
| `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv`, `AGENTS/REGINALD/registry/THRESHOLDS.tsv` | `STATE/triggers.tsv` | the *rule* definitions (metric·op·value·sustain·action·recipients) |
| `WALTER/registry/FALSIFICATION_FIRED_LOG.tsv`, `REG_THRESHOLDS_FIRED_LOG.tsv` | Layer 2 `type=threshold_crossed` | the *firings* |
| inbox/outbox + `AGENTS/SIGNALS.md` | Layer 2 `events` + cursors | retire dead HERMES |
| `BOARD/INDEX.md` + `SIG-W-…` files | Layer 2 events (`ref`→detail file) | detail SIGs stay; INDEX becomes a query; `board_log.tsv` → cursor |
| `AGENTS/VOCABULARIES.tsv` (NETWORK_GROUPS / CANONICAL_ENTITIES / SOURCE_TAGS) | controlled vocab both layers validate against | **already exists** — the namespace is half-built |
| `FORGE/STATUS.md` positions | Layer 1 `pos.*` keys | single canonical position ledger |
| NEXUS brief SENDING / WAITING-FOR tables | *generated* from Layer 2 | "Expected by" deadlock detection becomes a query |
| PROME `FLEET_SCAN.md` §1-4 (health/stale/catalysts) | queries over Layer 1 + git metadata | see §5 |

**`[INV]` Effort sizing (pending substrate inventory):** the fraction of "shared truth" already in TSV vs prose-only sets how much is promote-existing vs net-author. Early read: the *facts* are largely already structured (KB/VX/registries/docket/vocabularies); the duplication is that they're *also* restated in prose STATUS. So the work is mostly **redirecting writes + rendering reads**, not authoring new schemas. The inventory will give the exact %; I'll insert it here.

### Two emergent wins (free side effects)

- **Threshold-firing becomes a pure function.** Once values live in Layer 1 and trigger-rules in `triggers.tsv`, a watcher evaluates `values × triggers` → emits Layer 2 `threshold_crossed` events automatically. WALTER's most-reliable mechanism (auto-fire) generalizes to every metric, no per-agent boot-eval.
- **FLEET_SCAN gets cheaper and real-time.** Sections 1-4 (health/stale/catalysts) collapse from "spawn a subagent to read 30 lines × ~30 STATUS files" into queries over `values` + git log. The orchestral layer's read cost drops as a side effect.

---

## 5. Phased plan (sequenced with the separate-clones migration)

**Phase 0 — Now, pre-Jun-16 (git-native, Option A; no migration yet):**
1. Write `state.py` CLI + the six `STATE/*.tsv` schemas + `ownership.tsv` (seed from VOCABULARIES `Domain_Owner`).
2. Migrate `HEARTBEAT.md` + 2-3 pilot agents' dashboards to `state set` / render-from-`state`. (Pilot: SAM + VIOLET + HENRY — the agents whose 6/9 conflict this prevents.)
3. **Double-duty: this *is* the P1 instrumentation.** "Did you `state get` or read a sibling's file?" is exactly the read-logging the clones P1 gate needs. Phase 0 drives P1 toward <10% *and* measures it.

**Phase 1 — With the clones migration, post-Jun-16:**
4. Stand up Layer 2 `events` + cursors; retire inbox/outbox + HERMES; fold BOARD INDEX + fire-ledgers in.
5. Roll the dashboard→`state` change across all agents in the **same** coordinated CLAUDE.md edit as the migration's M5 (one instruction-update, not 14 separate ones).
6. The migration's **V3 "cross-agent signal latency check"** becomes the acceptance test for Layer 2.

**Phase 2 — Optional, only if needed:**
7. If same-session blindness still bites after Phase 1, stand up the VPS service (Option B) behind the unchanged CLI and flip the backend. No agent-facing change.

---

## 6. Risks / honest caveats

- **Instruction-edit drag:** ~14 agents' closeout steps change from "edit dashboard prose" to "`state set`." Mechanical but real — mitigated by bundling with the migration's M5 single edit.
- **Ownership registry needed:** single-writer-per-key requires `ownership.tsv` (who owns `vix`?). Mostly derivable from domain scope + VOCABULARIES `Domain_Owner`; one-time setup, a few genuine arbitration calls for Will.
- **Option A's ceiling:** if Will won't run the VPS service, same-session blindness is *reduced not eliminated* — lean on tighter push cadence + the events log for time-critical signals, and accept the bound.
- **CLI must stay dumb/fast:** a local script, not a heavyweight thing; never a bottleneck in an agent's boot.
- **Don't over-structure:** the temptation will be to schematize analysis too. Hold the line — facts in, judgment stays prose.

---

## 7. Reading status / what produced this

Read for this plan: the coordination machinery (HERMES/inbox-outbox/SIGNALS/NEXUS-briefs/PROME/HEARTBEAT/BOARD/registries), the sync constraints + git-race auto-memories + the separate-clones proposal, and the primary specs (clones P1-P5/M1-M6/V1-V4, NEXUS brief schema R3+amd7, BOARD + fire-ledger column schemas, VOCABULARIES, PROME orchestral rubric). **Pending:** the structured-substrate inventory (workbook TSVs / boot scripts / positions / predictions) — refines §4 sizing only; design and sequencing are complete without it.

*All design; no agent files mutated. Position/trade references illustrative — verify live before any action (root CLAUDE.md rule 4).*
