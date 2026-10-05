# Prompt 4 Distilled: Pub/Sub Broker Architectures — What We Keep

**Source discipline:** Software engineering (Kafka, RabbitMQ, NATS compared)
**Core question answered:** How do mature message broker systems handle routing, durability, backpressure, and failure — and which patterns translate to a file-based multi-agent system?

---

## The Big Idea: Separate Control Plane from Data Plane

The most important insight isn't about any single broker — it's that production systems split messaging into separate concerns:

| Concern | What Handles It | Our Translation |
|---------|----------------|-----------------|
| **Real-time coordination** | NATS (sub-100µs, fire-and-forget) | Push notifications for FLASH/IMMEDIATE |
| **Durable event log** | Kafka (append-only, replayable) | Signal archive — signals/ directory as immutable log |
| **Complex task routing** | RabbitMQ (exchanges, DLQs, priority queues) | Agent-specific routing with failure handling |

We don't need any of these technologies. We need the **pattern**: lightweight pings for urgent coordination, a persistent archive for durability and replay, and structured routing logic for complex dispatch.

---

## Five Patterns to Implement

### 1. Idempotent Consumers (From All Three)

Design every agent to handle receiving the same signal twice without harm. At-least-once delivery + idempotent processing = the pragmatic sweet spot. This matters because our file-based system has no built-in deduplication — an agent could read the same signal on two consecutive boots.

**Implementation:** Signal IDs (SIG-W-YYYYMMDD-NNN) serve as dedup keys. Agents track processed signal IDs in their STATUS or internal state.

### 2. Pull-Based Backpressure (From Kafka)

Kafka's consumers fetch at their own pace — if they fall behind, the lag grows but messages aren't lost. The broker doesn't force-feed.

**Our translation:** Agents read the COP and signal archive at boot, at their own pace. WALTER doesn't push everything into inboxes that overflow. The signal archive IS the durable log. Agents pull what they need. Only FLASH/IMMEDIATE gets pushed.

**Why this matters:** During a crisis (Kharg Island strike, earnings week), signal volume spikes. If WALTER pushes everything to every inbox, agents drown. Pull-based means agents consume what they can handle.

### 3. Dead Letter Handling (From RabbitMQ)

When a signal fails to process — agent not available, can't parse, conflict with existing state — it shouldn't disappear. RabbitMQ routes failed messages to a Dead Letter Exchange with full metadata about why it failed.

**Our translation:** Signals that WALTER can't route (no matching agent, ambiguous domain, below confidence threshold) go to a `filtered/` log with the reason for filtering. This is the Kill Log from the Filter Spec — now reinforced by DLQ patterns.

**Key metadata to preserve:** Signal ID, rejection reason, timestamp, confidence score at time of filtering.

### 4. Subject Hierarchies for Flexible Routing (From NATS)

NATS encodes routing dimensions into dot-delimited subjects: `agent.researcher.task.summarize.priority.high`. Wildcards match patterns without explicit routing rules.

**Our translation:** Signal file naming encodes routing dimensions:
```
SIG-W-20260407-003_CREDIT_IMMEDIATE_LIQUID.md
```
Domain, precedence, and primary recipient are visible from the filename alone. Agents can glob for their signals without reading every file.

### 5. Consumer Group Parallelism (From Kafka)

Multiple consumers in the same group split work — each message processed by exactly one consumer. Multiple groups each get a full copy.

**Our translation:** ACTION recipients (one agent processes, produces output) vs INFO recipients (multiple agents all read, no single owner). This maps directly to the TO:/INFO: pattern from Military Messaging.

---

## The Append-Only Log Insight

Kafka's most powerful property: the log is append-only and immutable. Events can't be edited after writing. This gives you:

- **Complete audit trail** — every signal ever produced is preserved
- **Replay capability** — new agents can "catch up" by reading history
- **Event sourcing** — current state is derived from the event sequence

**Our translation:** The `signals/` directory IS the append-only log. Once a signal file is written, it's never modified — only annotated (via state labels in the registry) or superseded (by a new signal). This is already how we planned the Signal Archive in the COP architecture.

**Log compaction analog:** Periodically, WALTER writes a "snapshot" to COP.md — the latest state per domain, derived from the signal log. Agents read the snapshot at boot instead of replaying every signal.

---

## Delivery Guarantee: At-Least-Once + Idempotent

| Guarantee | How It Works | Our Applicability |
|-----------|-------------|-------------------|
| At-most-once | Fire and forget, may lose messages | Too risky for financial signals |
| At-least-once | Confirm delivery, may duplicate | **Our target** — simple, reliable |
| Exactly-once | Transactional, expensive | Overkill for our scale |

At-least-once means: WALTER writes the signal to the archive, writes push notifications for urgent items, and trusts that agents will process them. If an agent processes the same signal twice (e.g., reads archive + gets push notification), the idempotent design means no harm done.

---

## Failure Modes That Will Bite Us

### 1. Unbounded Log Growth
Kafka retention policies prevent disk exhaustion. Our signals/ directory will grow indefinitely.
**Fix:** Age-out policy — signals older than N days move to an `archive/` subdirectory. COP.md always has the current state.

### 2. No Backpressure Signal
Kafka tracks consumer lag as a health metric. We have no equivalent — WALTER doesn't know if an agent is falling behind.
**Fix:** Agent STATUS.md should record "last signal processed" timestamp. WALTER checks this at boot to detect stale agents.

### 3. Missing Acknowledgment
We have no built-in ack mechanism for file reads. WALTER writes a signal — did the agent read it?
**Fix:** For FLASH/IMMEDIATE, require explicit acknowledgment (agent writes to outbox or updates STATUS). For ROUTINE/PRIORITY, delivery is presumed on next boot.

---

## What We Don't Need From Pub/Sub

- Kafka partition management, replication factors, ISR settings — no distributed system
- RabbitMQ exchange topology (direct, fanout, topic, headers) — file-based routing is simpler
- NATS subject wildcards at the protocol level — glob patterns serve the same purpose
- Consumer group rebalancing algorithms — agents don't compete for partitions
- AMQP/MQTT wire protocol details — no network protocol layer
- Performance benchmarks (15M msgs/s, sub-100µs latency) — irrelevant at our scale
- KRaft consensus, quorum queues, Raft — no distributed consensus needed
- GDPR crypto-shredding for immutable logs — not applicable

---

*Distilled from PROMPT4_PUBSUB_MASTER.md | April 7, 2026*
