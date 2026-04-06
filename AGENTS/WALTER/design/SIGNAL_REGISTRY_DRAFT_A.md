# Signal Registry: Draft Architecture (Prompt A)

## Core Purpose

Central registry for all agent-generated signals with state tracking, automated annotations, and iterative refinement. Replaces scattered mentions in MEMORY.md with queryable, structured records.

---

## Entities

### Signal

The atomic unit of detection.

| Field | Type | Description |
|-------|------|-------------|
| `signal_id` | UUIDv4 | Unique identifier |
| `timestamp` | ISO8601 | When detected (agent-local time) |
| `agent` | string | Source agent (LABOR, CARL, etc.) |
| `signal_type` | enum | Threshold-crossed / Pattern-match / Manual-flag |
| `payload` | JSON | Agent-specific data (price, threshold, context) |
| `confidence` | float | 0.0-1.0 initial confidence |
| `far_estimate` | float | False alarm rate (events/day) if calculable |
| `superevent_id` | UUIDv4 | Nullable; set if grouped |
| `status` | enum | pending / validated / rejected / actioned / stale |
| `created_at` | ISO8601 | Registry insertion time |
| `updated_at` | ISO8601 | Last modification |

**Example:**
```json
{
  "signal_id": "sig-7a3f-9e2b",
  "timestamp": "2026-04-06T14:30:00Z",
  "agent": "LABOR",
  "signal_type": "threshold-crossed",
  "payload": {
    "indicator": "initial_claims",
    "value": 267000,
    "threshold": 250000,
    "shadow_adjusted": true
  },
  "confidence": 0.72,
  "far_estimate": 0.3,
  "superevent_id": null,
  "status": "pending"
}
```

---

### Superevent

Thematic grouping of related signals.

| Field | Type | Description |
|-------|------|-------------|
| `superevent_id` | UUIDv4 | Unique identifier |
| `created_at` | ISO8601 | When first signal triggered grouping |
| `theme` | string | Detected theme (credit-stress, energy-shock, etc.) |
| `signal_ids` | array[UUID] | Contributing signals, time-ordered |
| `status` | enum | forming / active / resolved / false-positive |
| `confidence` | float | Aggregated confidence (calculated) |
| `first_detection` | ISO8601 | Earliest signal timestamp |
| `last_update` | ISO8601 | Most recent signal or annotation |

**Grouping triggers:**
- Time window: signals within 24 hours
- Thematic overlap: keyword match OR embedding similarity > 0.85
- Agent coordination: explicit cross-reference in agent output

---

### Annotation

Iterative additions to signals/superevents.

| Field | Type | Description |
|-------|------|-------------|
| `annotation_id` | UUIDv4 | Unique identifier |
| `target_type` | enum | signal / superevent |
| `target_id` | UUIDv4 | What this annotates |
| `timestamp` | ISO8601 | When added |
| `author` | string | Agent or human (WILL, RED, NEXUS) |
| `annotation_type` | enum | validation / rejection / update / outcome |
| `content` | JSON | Structured data per type |

**Annotation types:**

| Type | Content Schema | Purpose |
|------|---------------|---------|
| `validation` | `{ "confidence_delta": float, "reason": string }` | Confirm signal, adjust confidence |
| `rejection` | `{ "reason": string, "category": string }` | Mark false positive |
| `update` | `{ "field": string, "old": any, "new": any }` | Correct or enrich signal data |
| `outcome` | `{ "position": string, "pnl": float, "lesson": string }` | Track what happened |

---

### Action

Link signals to decisions.

| Field | Type | Description |
|-------|------|-------------|
| `action_id` | UUIDv4 | Unique identifier |
| `signal_id` | UUIDv4 | What triggered this |
| `superevent_id` | UUIDv4 | Nullable; if triggered by grouping |
| `timestamp` | ISO8601 | When decided |
| `decision` | enum | investigate / position / ignore / escalate |
| `position` | JSON | Nullable; if acted (ticker, direction, size, stop) |
| `rationale` | string | Why this decision |
| `outcome` | JSON | Nullable; filled later (exit price, pnl, lesson) |

---

## State Machines

### Signal Lifecycle

```
PENDING → VALIDATED → ACTIONED
   ↓         ↓
REJECTED   STALE
```

| Transition | Trigger | Actor |
|------------|---------|-------|
| `pending` → `validated` | RED review, cross-agent corroboration, or threshold confidence | System / RED |
| `pending` → `rejected` | RED flags false positive, or superevent resolved as noise | RED / System |
| `validated` → `actioned` | Will approves position, or agent auto-executes per AUTONOMY tier | WILL / Agent |
| `validated` → `stale` | 7 days without action, or thesis shift makes irrelevant | System |
| `pending` → `stale` | 14 days without validation | System |

### Superevent Lifecycle

```
FORMING → ACTIVE → RESOLVED
    ↓
FALSE-POSITIVE
```

| Transition | Trigger |
|------------|---------|
| `forming` → `active` | 2+ signals with confidence > 0.6, or explicit agent escalation |
| `forming` → `false-positive` | All constituent signals rejected |
| `active` → `resolved` | Position closed, or 30 days since last signal |

---

## API Sketch

### Write Operations

```
POST /signals
  Body: Signal (without signal_id, status="pending")
  Response: { signal_id, status }

POST /signals/{id}/annotations
  Body: Annotation
  Response: { annotation_id, new_status }

POST /superevents
  Body: { signal_ids, theme }
  Response: { superevent_id }

POST /actions
  Body: Action
  Response: { action_id }
```

### Read Operations

```
GET /signals?agent=LABOR&status=pending&since=2026-04-01
GET /signals/{id}
GET /signals/{id}/annotations
GET /signals/{id}/actions

GET /superevents?status=active&theme=credit-stress
GET /superevents/{id}
GET /superevents/{id}/signals
GET /superevents/{id}/timeline

GET /actions?outcome=null&since=2026-03-01
```

### Aggregation Queries

```
GET /metrics/signals?by=agent&since=2026-01-01
GET /metrics/superevents?by=theme&status=resolved
GET /metrics/far?agent=LABOR&signal_type=threshold-crossed
```

---

## Storage Options

| Option | Pros | Cons |
|--------|------|------|
| **SQLite** (single file) | Zero infra, portable, ACID | No concurrency, single-node |
| **PostgreSQL** | Robust, JSON support, queryable | Requires setup, overkill? |
| **JSONL files** | Human-readable, git-friendly | No querying, slow at scale |
| **LiteFS** (SQLite + replication) | Best of both worlds | Fly.io dependency |

**Recommendation:** Start with SQLite single file in `PROME/registry/signals.db`. Migrate to PostgreSQL if query complexity justifies it.

---

## Integration Points

### Existing Files

| Current | Maps To |
|---------|---------|
| `HEARTBEAT.md` threshold table | Query: `SELECT * FROM signals WHERE status='pending'` |
| `MEMORY.md` signal narratives | `annotations` with author=NEXUS, type=summary |
| `POSITIONS.md` | `actions` with decision=position |
| `AGENTS/{name}/STATUS.md` | Query: `SELECT * FROM signals WHERE agent={name}` |

### Agent Workflow Changes

**Current:** Agent detects → writes to STATUS.md → NEXUS reads → updates HEARTBEAT

**Proposed:** Agent detects → POST /signals → Registry handles routing → NEXUS queries for synthesis

**Benefits:**
- Agents don't need to know about each other's files
- NEXUS has queryable dataset instead of parsing markdown
- RED can filter by confidence before reviewing
- Will can see full provenance of any signal

---

## Open Questions

1. **Embedding similarity for grouping:** What model? Where does it run? (Defer to Prompt B)
2. **FAR calculation:** What historical data do we have? (Defer to Prompt C)
3. **Agent adoption:** Migration path from STATUS.md writing to API calls?
4. **Concurrency:** Multiple agents posting simultaneously — SQLite sufficient?
5. **Backup/audit:** Git-track the SQLite file? Separate audit log?

---

## Next Steps

1. Review this draft
2. Decide on storage backend
3. Implement minimal version (Signal + Annotation tables, no Superevent yet)
4. Test with LABOR signals for 1 week
5. Iterate before rolling out to all agents

---

*Draft A — Signal Registry Architecture*
*Date: April 6, 2026*
