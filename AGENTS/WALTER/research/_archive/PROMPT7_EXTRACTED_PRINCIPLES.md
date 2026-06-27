# Prompt 7: Scientific Alert Systems — Extracted Principles for WALTER

## What Matters for Signal Routing Architecture

### 1. Cascading Filter Architecture (The ATLAS Pattern)

**The Pipeline:**
- **Level-1 (Hardware):** 40 MHz → 100 kHz in <2.5 μs — FPGA pattern matching, coarse granularity
- **High-Level Trigger (Software):** 100 kHz → 1 kHz in ~300 ms — full event reconstruction, ML classification
- **Storage:** Only ~0.003% of raw data preserved

**Key Principle:** Each stage trades latency for precision. Hardware eliminates obvious noise; software handles nuance.

**WALTER Analog:**
| ATLAS Stage | WALTER Equivalent |
|-------------|-------------------|
| L1 Trigger (FPGA, <2.5 μs) | Signal detection rules (pattern matching) |
| HLT (60K CPU cores, ~300 ms) | Agent classification + triage |
| Permanent storage (~1 kHz) | NEXUS synthesis + MEMORY persistence |

**Critical Insight:** Don't do heavy processing on every signal. Tiered rejection preserves resources for high-value analysis.

---

### 2. False Alarm Rate (FAR) as Decision Boundary (The LIGO Pattern)

**LIGO's Thresholds:**

| Alert Type | FAR Threshold | Expected Rate |
|------------|---------------|---------------|
| Public preliminary | ≤ 2.3 × 10⁻⁵ Hz | ~2/day |
| Significant CBC | ≤ 3.9 × 10⁻⁷ Hz | ~1/month |
| Significant burst | ≤ 3.2 × 10⁻⁸ Hz | ~1/year |

**Method:** Time-slide background estimation — shift single-detector triggers by 100ms multiples, count accidental coincidences.

**WALTER Analog:** Signal confidence scores with explicit false-positive rate estimation, not binary classification.

**Key Principle:** Quantified uncertainty enables downstream threshold tuning. Binary real/bogus insufficient.

---

### 3. Event Store with State Annotations (The GraceDB Pattern)

**GraceDB Structure:**
- Centralized web service (gracedb.ligo.org)
- **Superevent abstraction:** Groups candidates within 1 second into single astrophysical source
- **State labels:** `INJ` (injection), `DQV` (data quality veto), `EM_READY` (suitable for follow-up)
- **Automated annotations:** BAYESTAR (3D localization), p_astro classification (BNS/NSBH/BBH/terrestrial)

**WALTER Analog:** Central message registry with:
- Signal grouping (same event, multiple agents)
- Status flags (pending/validated/rejected/actioned)
- Confidence annotations (FAR, source reliability)
- Iterative refinement (updates over time)

**Key Principle:** Preserve uncertainty and provenance. Don't pretend early decisions are final.

---

### 4. Community Broker Ecosystem (The ZTF Pattern)

**ZTF Scale:**
- 600K–1.2M alerts/night
- End-to-end latency: ~13 minutes
- Kafka distribution: ~6–10 seconds after generation

**Broker Ecosystem (7+ independent processors):**

| Broker | Institution | Specialization |
|--------|-------------|----------------|
| ANTARES | NOIRLab/Arizona | Multi-wavelength cross-matches (Gaia, SDSS, WISE, Chandra) |
| ALeRCE | Chile | Two-stage ML: CNN → random forest → transformer |
| Lasair | Edinburgh | SQL-based filtering, Sherlock classification |
| AMPEL | Berlin/DESY | Four-tier framework (filter → combine → analyze → react) |
| Fink | France | Apache Spark, 100K alerts/minute tested |

**Key Principle:** Single alert stream → multiple independent downstream processors, each adding unique value.

**WALTER Analog:** Core signal stream → specialized agents (NEXUS, RED, LIQUID, etc.) with domain-specific filtering.

---

### 5. Dual-Channel Communication (GCN Pattern)

**GCN Structure:**
- **Notices:** Automated, machine-readable, seconds latency (JSON over Kafka, legacy 160-byte binary, VOEvent XML)
- **Circulars:** Human-written, minutes to hours (astronomical telegrams)

**Pivotal Example: GW170817 (Neutron Star Merger)**
| Time | Event |
|------|-------|
| T+0 | Merger |
| T+16s | Fermi-GBM GCN Notice |
| T+27min | LIGO GCN Notice |
| T+40min | GCN Circular (GW/GRB association) |
| T+5.2hr | Refined localization (~28 sq deg) |

**Result:** ~70 observatories, paper with ~4,000 co-authors

**WALTER Analog:**
- **Notices:** Automated agent alerts (Kafka/JSON)
- **Circulars:** Human-authored summaries (Telegram briefings, POSITIONS.md updates)

---

### 6. Machine Learning at Scale

**Real-Time Inference:**
- **braai (ZTF):** CNN for real/bogus classification (0–1 score)
- **ALeRCE:** CNN stamp classifier (~94% accuracy) → hierarchical random forest → ATAT transformer (82.9% F1)
- **Fink:** Apache Spark Structured Streaming, 100K alerts/minute tested
- **Aframe (LIGO O4):** ML for binary black hole detection

**WALTER Analog:** ML-based signal classification at ingestion, with confidence scores preserved through pipeline.

---

### 7. Technology Stack Convergence

**Serialization:** Apache Avro (compact binary, schema evolution, ~60 KB/alert)

**Distribution:** Apache Kafka (universal choice across GCN, ZTF, LIGO, Rubin)
- Benefits: Built-in replication, consumer-group parallelism, offset tracking for rewindability

**State Management:** Label-based tracking (GraceDB), 30-year evolution from pager alerts to cloud-native

**WALTER Analog:**
- Avro or JSON for serialization
- Kafka for distribution (or equivalent with offset tracking)
- Central registry with state labels

---

### 8. Latency vs. Precision Trade-offs

| System | Latency | Constraint |
|--------|---------|------------|
| ATLAS L1 | <2.5 μs | Hardware buffer overflow |
| ATLAS HLT | ~300 ms | CPU processing |
| LIGO preliminary | ~29.5 s | Calibration/transfer |
| LIGO early warning | -3.1 s (before merger) | Signal accumulation |
| ZTF end-to-end | ~13 min | Image differencing |
| ZTF Kafka | ~6–10 s | Network transfer |

**Key Principle:** Different stages optimize for different latency budgets. Don't force uniform timing.

**WALTER Analog:**
- Sub-second signal detection (pattern rules)
- Seconds for agent routing
- Minutes for synthesis and human briefing

---

## What We Can Ignore

| Scientific-Specific | Why Not Needed |
|---------------------|----------------|
| Hardware FPGA triggers | Software-based detection sufficient |
| Time-slide background estimation | Historical pattern analysis different domain |
| 3D sky localization | Financial signals don't have spatial coordinates |
| Gravitational-wave inspiral physics | No signal accumulation over time |
| Optical image differencing | No pixel data in financial signals |
| Multi-wavelength cross-matching | No electromagnetic spectrum analog |
| IAU Circulars / ATELs | Domain-specific publication formats |

---

## Key Architectural Decisions for WALTER

1. **Cascading filters:** Yes — tiered rejection (signal → classification → action)
2. **FAR-based thresholds:** Yes — confidence scores, not binary classification
3. **Central event store:** Yes — GraceDB model with annotations and state labels
4. **Broker ecosystem:** Yes — specialized downstream processors
5. **Dual-channel (machine + human):** Yes — automated alerts + authored briefings
6. **ML at ingestion:** Yes — real-time classification with confidence preservation
7. **Kafka-based distribution:** Yes — with offset tracking for replay
8. **Dynamic resource allocation:** Yes — adjust processing depth based on signal volume

---

## Unique Contributions from Prompt 7

| Pattern | Source | WALTER Application |
|---------|--------|-------------------|
| Superevent grouping | LIGO GraceDB | Multi-agent correlation (same event, different signals) |
| Time-slide background | LIGO PyCBC | Historical false-positive rate estimation |
| RealBogus scoring | ZTF braai | Signal reliability 0–1 scale |
| Consumer-group parallelism | ZTF Kafka | Parallel agent processing |
| Offset rewind | Kafka | Message replay for recovery |
| TLA (Trigger Level Analysis) | ATLAS Run 3 | Record only derived objects, not full payload |
| TrigMenuRulebook | ATLAS | Dynamic prescale adjustment based on load |

---

*Extracted from: PROMPT7_SCIENTIFIC_ALERT_SYSTEMS_MASTER.md + PROMPT7_SCIENTIFIC_ALERT_SYSTEMS_SUPPLEMENT.md*
*Date: April 6, 2026*
