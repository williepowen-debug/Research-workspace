# Prompt 7 Technical Supplement: Deep-Dive on Scientific Alert Systems

## Source Document
**File:** Real-Time_Scientific_Alert_Systems_Research---0f1b591d-4439-4112-9b0b-7735bf25c26e.pdf
**Date:** 2026-04-06
**Note:** Technical deep-dive with micro-architectural details

---

## ATLAS TDAQ: Micro-Architectural Details

### Data Scale
- **Raw data rate:** 64 PB/s if uncompressed
- **Event size:** ~1.5-1.6 MB per collision
- **Final storage:** ~300-320 MB/s (200-300 Hz)

### Level-1 (L1) Hardware Trigger
- **Implementation:** Custom ASICs and high-speed FPGAs
- **Latency budget:** < 2.5 μs (hard constraint)
- **Buffering:** Analog/digital pipeline memories on front-end electronics
- **Zero-suppression:** Applied during transfer to Readout Buffers (ROBs)
- **Output:** L1 accept → data transferred to ROBs

### Region of Interest (RoI) Mechanism
- **Purpose:** Architectural cornerstone for latency optimization
- **Function:** L1 calculates geographical coordinates of energetic activity
- **L2 data-on-demand:** Requests data only from ROBs matching RoI coordinates
- **Data reduction:** RoI covers ~2% of total detector volume
- **Network latency:** Reduced to < 1 ms

### Level-2 (L2) Trigger
- **Hardware:** Massive farm of commodity CPUs
- **Processing:** ~40 ms per event
- **Input:** 100 kHz
- **Output:** 1-3.5 kHz
- **Key capability:** Fast tracking using Inner Detector (inaccessible to L1)

### Event Filter (EF) / High-Level Trigger (HLT)
- **Processing:** ~4 seconds per event
- **Quality:** Offline-quality reconstruction
- **Input:** Few kHz
- **Output:** 200-300 Hz
- **Modern architecture:** L2 + EF unified into HLT (Run 2/Run 3)
- **Benefit:** Dynamic resource allocation, streamlined deployment

### Micro-Architectural Optimizations

#### Network Transport
- **RDMA over Converged Ethernet (RoCEv2):** Bypasses OS kernel
- **RASHPA architecture:** Zero-copy data redistribution
- **Benefit:** Eliminates CPU interrupts and memory copies

#### Software Framework (Athena)
- **Run 2:** Multiprocessing with copy-on-write (2× memory savings)
- **Run 3:** Fully multithreaded (AthenaMT)
- **Benefit:** Greater memory sharing, minimized context-switching overhead

#### GPU Acceleration
- **CUDA streams:** Non-default streams enable overlap
- **Parallelization:** Host-to-device transfers overlap with kernel execution
- **Benefit:** Minimized idle compute cycles

---

## LIGO: Low-Latency Infrastructure Details

### Calibration Pipeline
- **Photon calibrator (Pcal):** 0.3% uncertainty (O4)
- **Robustness:** Automated state vectors fill missing data with zeros
- **Purpose:** Prevent downstream search algorithm failures

### GraceDB Event States
| Label | Meaning |
|-------|---------|
| INJ | Injection (simulated event) |
| DQV | Data-quality veto |
| EM_READY | Suitable for electromagnetic follow-up |

### Alert Timeline (O4)
- **Median preliminary alert:** 30 seconds from merger
- **Early warning:** Negative latency (before merger) for massive BNS

### Multi-Messenger Coordination
- **GCN/TAN Circulars:** Linked from GraceDB
- **Follow-up reporting:** Structured annotations

---

## ZTF: Broker Ecosystem Details

### Alert Volume
- **Typical night:** 600,000 - 1.2 million alerts
- **Latency goal:** Science-quality alerts within 20 minutes
- **Actual latency:** ~10 seconds after candidate production

### Data Format (Avro)
- **Size:** ~60 KB per alert
- **Contents:**
  - PSF-fit photometry
  - 30 days detection history
  - Forced photometry
  - Three 63×63 pixel cutouts (science, reference, difference)

### RealBogus (rb) Score
- **Range:** 0-1
- **Interpretation:** Closer to 1 = more reliable detection
- **Usage:** Science programs tune thresholds to purity requirements

### Kafka Patterns
- **Partitioning:** Parallel processing
- **Replication:** Built-in reliability
- **Offset rewind:** Replay streams, recover from outages
- **Mirroring:** IPAC → University of Washington

---

## Generalized Design Template (5-Step Pattern)

1. **Cheapest possible first-pass rejection near the instrument**
   - ATLAS: L1 hardware trigger
   - LIGO: Low-latency calibration + online searches
   - ZTF: Image differencing (minimal upstream rejection)

2. **Preserve uncertainty and provenance instead of pretending early decisions are final**
   - ATLAS: Prescale factors, working points
   - LIGO: FAR, p_astro, state labels
   - ZTF: RealBogus scores, history, crossmatches

3. **Expose candidate state through a machine-readable event store**
   - ATLAS: HLT output to permanent storage
   - LIGO: GraceDB with REST/JSON APIs
   - ZTF: Kafka streams with Avro serialization

4. **Let downstream brokers or specialist consumers perform domain-specific filtering**
   - ATLAS: Mostly internal (physics analysis groups)
   - LIGO: Multi-messenger observers via GCN
   - ZTF: ANTARES, Lasair, ALeRCE, AMPEL, Fink

5. **Support both automated streams and human-readable circulars for follow-up coordination**
   - ATLAS: Internal documentation + data release
   - LIGO: GCN Notices + GCN Circulars
   - ZTF: Kafka alerts + ATELs/TNS

---

## Key Metrics Summary

| System | Input Rate | Output Rate | Latency | Key Innovation |
|--------|-----------|-------------|---------|----------------|
| ATLAS L1 | 40 MHz | 100 kHz | < 2.5 μs | Hardware FPGAs, RoI mechanism |
| ATLAS HLT | 100 kHz | ~1 kHz | ~300 ms/event | Multithreaded AthenaMT |
| LIGO | Continuous strain | ~1-2 alerts/day | ~30 s | GraceDB state management |
| ZTF | 47 sq deg images | ~1M alerts/night | ~10 s | Kafka + broker ecosystem |

---

## Relevance to Agent Message Routing: Technical Insights

### Latency vs. Precision Trade-offs
- **Ultra-low latency (< 1 ms):** Hardware-based, coarse-grained (ATLAS L1)
- **Low latency (seconds):** Software-based, statistical confidence (LIGO)
- **Moderate latency (minutes):** Full reconstruction, community distribution (ZTF)

### State Management Patterns
- **GraceDB model:** Central registry with annotations and state transitions
- **Kafka model:** Distributed log with offset tracking for replay
- **Hybrid:** Combine both for reliability + flexibility

### Confidence Scoring
- **FAR (False Alarm Rate):** Quantified uncertainty for downstream thresholding
- **RealBogus:** ML-based confidence for filtering
- **Prescale factors:** Rate-control mechanism

### Scalability Patterns
- **Horizontal scaling:** CPU farms (ATLAS HLT), Kafka partitions (ZTF)
- **Vertical scaling:** GPU acceleration, RDMA networking
- **Dynamic allocation:** Unified HLT resources, auto-scaling brokers

---

## Implementation Recommendations for Agent Systems

1. **Tiered processing pipeline** matching latency requirements
2. **Central event registry** with annotation support (GraceDB-style)
3. **Quantified confidence scores** preserved through pipeline
4. **Kafka-based distribution** with offset tracking for reliability
5. **Broker ecosystem** for domain-specific downstream processing
6. **Dual-format output:** Machine-readable (JSON/Avro) + human-readable (circulars)
7. **Dynamic resource allocation** based on load and priority
8. **State labels** for event lifecycle management
