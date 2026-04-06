# Prompt 4: Pub-Sub Broker Architectures — Master Extraction

**Source:** Kafka, RabbitMQ, and NATS compared (Compass Research)
**Date:** 2026-04-06

---

## Core Philosophical Divide

| Broker | Core Philosophy | Best For |
|--------|----------------|----------|
| **Kafka** | Append-only distributed commit log | Durability, replay, event sourcing |
| **RabbitMQ** | Flexible AMQP routing engine | Complex routing, failure handling, DLQs |
| **NATS** | Ultra-lightweight subject-based mesh | Low latency, operational simplicity |

**Key insight:** Not a single broker but a **hybrid architecture** often dominates — NATS for real-time coordination, Kafka for durable event streams, RabbitMQ for complex task routing.

---

## 1. Routing Models

### Kafka: Partitioned Log
- Topic = partitioned, append-only log
- Messages retained by policy (default 7 days, configurable to infinite)
- Multiple consumer groups read independently, each with own offset
- **Unifies pub-sub and work-queue** through single abstraction
- No content-based routing (topic name only)

### RabbitMQ: Exchange-Binding-Queue
- Four exchange types: **direct** (exact match), **fanout** (broadcast), **topic** (wildcards `*`/`#`), **headers** (content-based)
- Headers exchange = only broker-native content-based routing
- Messages **deleted after acknowledgment** — consumed means gone
- `basic.qos` prefetch count critical for fair dispatch (10–20 optimal)

### NATS: Hierarchical Subjects
- Dot-delimited subjects: `orders.us.east.created`
- Wildcards: `*` = one token, `>` = one or more trailing tokens
- Core NATS: fire-and-forget, zero persistence
- **JetStream** adds durability via Streams
- Most expressive topic-based routing of the three

**Multi-agent pattern:** Encode routing dimensions into NATS subject hierarchies: `agent.researcher.task.summarize.priority.high`

---

## 2. Consumer Groups & Load Balancing

| Feature | Kafka | RabbitMQ | NATS |
|---------|-------|----------|------|
| Parallelism ceiling | Partition count | Queue depth | Unlimited |
| Rebalancing | CooperativeStickyAssignor (incremental) | N/A (round-robin) | Instantaneous |
| Ordering guarantee | Per-partition | Per-queue FIFO | Per-subject (JetStream) |
| Scale-out overhead | Rebalance delay | None | Zero |

**Key parameters:**
- Kafka: `session.timeout.ms` (45s), `max.poll.interval.ms` (5min), `heartbeat.interval.ms` (3s)
- RabbitMQ: `prefetch_count` (10–20 optimal), `single-active-consumer` for ordered processing
- NATS: `MaxAckPending` (1,000 default) controls unacknowledged message window

---

## 3. Durability & Replay

| Capability | Kafka | RabbitMQ (Queues) | RabbitMQ (Streams) | NATS JetStream |
|------------|-------|-------------------|--------------------|----------------|
| Message replay | Full (offset reset) | None | Full (offset-based) | Full (sequence/time) |
| Offset storage | `__consumer_offsets` topic | N/A | Server-side | Server-side (durable consumers) |
| Retention modes | Time, size, compaction | Until ack (deleted) | Time, size | Time, size, count, interest, workqueue |
| Resume after disconnect | Yes | Requeue unacked only | Yes | Yes |

**Kafka log compaction:** Retains only latest value per key — essential for materialized views.

**NATS JetStream `DeliverPolicy` options:**
- `DeliverAll`, `DeliverLast`, `DeliverNew`
- `DeliverByStartSequence`, `DeliverByStartTime`
- `DeliverLastPerSubject`
- `ReplayOriginal` — preserves inter-message timing

---

## 4. Backpressure Models

| Broker | Model | Key Mechanism |
|--------|-------|---------------|
| **Kafka** | Pull-based natural backpressure | Consumer fetches at own pace; lag increases but messages retained |
| **RabbitMQ** | Push-based with credit flow | `vm_memory_high_watermark` (40% RAM) blocks publishers; `x-max-length` with overflow behaviors |
| **NATS Core** | Aggressive protection | Slow subscriber buffer fills → messages dropped → disconnection |
| **NATS JetStream** | Pull consumers | `Fetch(N)` for natural backpressure; `MaxAckPending` suspends delivery |

**Critical tuning:**
- Kafka: `max.poll.records` (500), `fetch.min.bytes`, consumer lag monitoring
- RabbitMQ: `prefetch_count`, memory/disk alarms, queue length limits
- NATS: `MaxAckPending`, `FlowControl` for push consumers

---

## 5. Delivery Guarantees

| Guarantee | Kafka | RabbitMQ | NATS JetStream |
|-----------|-------|----------|----------------|
| At-most-once | `acks=0` | `auto_ack=true` | Core NATS; `AckNone` |
| At-least-once | `acks=all` + manual commit (default) | Manual ack + publisher confirms | `AckExplicit` + publisher ack |
| Exactly-once | Idempotent producers + transactions + read_committed | **Not supported natively** | `Nats-Msg-Id` dedup + double ack |

**Kafka EOS mechanisms:**
- Idempotent producers (`enable.idempotence=true`): PID + sequence numbers for broker dedup
- Transactional producers (`transactional.id`): two-phase commit across partitions
- Read-committed consumers (`isolation.level=read_committed`)
- Cost: few-to-tens ms per transaction commit

**NATS exactly-once publishing:**
- `Nats-Msg-Id` header with dedup window (default 2 min)
- `DiscardNewPerSubject` + `MaxMsgsPerSubject=1` for infinite dedup
- Double acknowledgments prevent lost-ack redelivery

**Design principle:** Design all agents as **idempotent consumers** from day one. At-least-once + idempotent processing = pragmatic sweet spot.

---

## 6. Dead Letter Queues

| Broker | Native DLQ | Implementation |
|--------|-----------|----------------|
| **RabbitMQ** | ✅ Most mature | Dead-letter exchanges (DLX): `x-dead-letter-exchange`, `x-dead-letter-routing-key` |
| **Kafka** | ❌ Application layer | Separate "error topics"; Uber's retry-topic pattern |
| **NATS** | ❌ Advisory-based | `MaxDeliver` exceeded → advisory to `$JS.EVENT.ADVISORY.CONSUMER.MAX_DELIVERIES` |

**RabbitMQ DLX triggers:**
- Message rejection (`basic.reject`/`basic.nack` with `requeue=false`)
- TTL expiry (`expiration`, `x-message-ttl`)
- Queue length overflow
- Quorum queues: `x-delivery-limit` exceeded (default 20 in RabbitMQ 4.0)

**RabbitMQ `x-death` header:** Records queue name, reason, count, timestamp, original routing keys — invaluable for retry logic.

**Uber's multi-level retry pattern (Kafka):**
```
main topic → topic-retry-1 (1 min) → topic-retry-2 (5 min) → topic-dead-letter
```
Each retry level = separate Kafka topic for independent monitoring.

---

## 7. Event Sourcing & Audit Trails

**Kafka as event store:**
- Append-only commit log = architecturally isomorphic to event store
- Every state change = immutable record with sequential offset
- Log compaction maintains "latest state per key" snapshot
- CQRS pattern: commands → Kafka (write side); consumers materialize views (read side)
- Debezium for CDC: stream row-level DB changes into Kafka

**Not suitable:**
- RabbitMQ traditional queues (destructive read)
- RabbitMQ Streams (lacks compaction, stream processing ecosystem)
- NATS JetStream (no log compaction, limited ecosystem)

**GDPR concern:** Immutable logs + data deletion = requires crypto-shredding or periodic log rewriting.

---

## 8. Performance Characteristics

| Metric | Kafka | RabbitMQ | NATS |
|--------|-------|----------|------|
| Throughput | 500K–1M+ msgs/s per node | 20K–50K msgs/s (quorum); 500K with sharding | 15M+ msgs/s (core); 200K–400K (JetStream) |
| Latency | 10–50ms (batching); 2–5ms tuned | ~ms range | **Sub-100µs median** (core) |
| Resource requirements | 8+ vCPU, 16–64 GB RAM | Moderate | **~20 MB static binary**, zero dependencies |
| Operational complexity | High (KRaft in 4.0 reduces) | Moderate | **Minimal** |

---

## 9. Recommended Hybrid Architecture for Multi-Agent Systems

```
┌─────────────────────────────────────────────────────────────┐
│                    AGENT CONTROL PLANE                       │
│                      (NATS Core + JetStream)                 │
│  • Heartbeats, coordination signals                          │
│  • Request-reply service calls                               │
│  • Real-time status updates                                  │
│  • Fire-and-forget ephemeral signals                         │
│  • Short-retention state (JetStream)                         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼ (bridge connectors)
┌─────────────────────────────────────────────────────────────┐
│                    RESEARCH EVENT LOG                        │
│                         (Kafka)                              │
│  • All significant agent actions                             │
│  • Research outputs                                          │
│  • Audit trails (acks=all, replication.factor=3)             │
│  • Infinite retention for event sourcing                     │
│  • Kafka Streams for derived views                           │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    TASK ROUTING LAYER                        │
│                      (RabbitMQ)                              │
│  • Complex task queues with priority                         │
│  • TTL and dead-letter exchanges                             │
│  • Poison message isolation                                  │
│  • Prefetch-based fair dispatch                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 10. Key Design Principles for Multi-Agent Infrastructure

1. **Idempotent consumers by default** — at-least-once + idempotent processing = pragmatic sweet spot
2. **Separate control plane from data plane** — NATS for real-time coordination, Kafka for durable events
3. **Invest in failure handling from day one** — outbox pattern, exponential backoff with jitter, DLQ routing
4. **Use subject hierarchies for flexible routing** — encode dimensions (agent type, priority, region) in NATS subjects
5. **Monitor consumer lag as primary health metric** — especially critical for Kafka

---

## Cross-References

- **Prompt 2 (Military):** Precedence levels map to NATS subject hierarchies + priority encoding
- **Prompt 3 (ATC):** Flight strips as externalized state → Kafka event sourcing pattern
- **Prompt 5 (Intelligence):** To be integrated
- **Prompt 6 (Emergency Dispatch):** To be integrated
- **Prompt 7 (Scientific Teams):** To be integrated
