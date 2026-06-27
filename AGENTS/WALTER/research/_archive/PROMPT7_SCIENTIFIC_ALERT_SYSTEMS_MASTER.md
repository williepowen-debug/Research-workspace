# Prompt 7: Scientific Alert Systems - Master Extraction

## Source Document
**File:** compass_artifact_wf_8c5f7b83_c648_46d3_a036_d73d2847f39b_tex---571b6c85-c82a-4b07-88b1-3f54e6626162.md
**Date:** 2026-04-06
**Domain:** Scientific Research Alert Systems (ATLAS, LIGO, ZTF, GCN)

---

## Overview

Three world-class scientific facilities solve the same fundamental problem: extracting rare signals from overwhelming data streams and distributing validated alerts to global communities in real time. Despite operating in radically different domains (particle physics, gravitational waves, optical astronomy), they converge on shared architectural patterns:

1. **Multi-level cascading filters**
2. **False-alarm-rate thresholds as decision boundaries**
3. **Publish-subscribe distribution via Apache Kafka**

---

## Case Study 1: ATLAS TDAQ (CERN)

### The Challenge
- **40 MHz** raw collision rate (every 25 nanoseconds)
- **60 TB/s** total detector throughput
- Must discard **99.99%** of events while preserving rare physics signatures

### Two-Level Trigger Architecture (Run 3)

#### Level-1 (L1) Trigger
- **Hardware:** Custom FPGAs
- **Latency:** < 2.5 microseconds (hard constraint - front-end buffer overflow)
- **Input:** 40 MHz
- **Output:** 100 kHz maximum
- **Data volume:** ~300 GB/s to readout
- **Processing:** Coarse-granularity calorimeter and muon data

#### High-Level Trigger (HLT)
- **Hardware:** ~60,000 CPU cores (2.0 million HepSpec06)
- **Processing time:** ~300 ms per event
- **Input:** 100 kHz
- **Output:** ~3 kHz for permanent storage (~6 GB/s)
- **Overall reduction:** 40,000×
- **Framework:** AthenaMT (multi-threaded, shared memory)

### Run 3 Upgrades
- **eFEX/jFEX/gFEX:** New Feature Extractor processors with 10× finer granularity
- **New Small Wheel:** Micromegas and small-strip TGC technologies
- **L1Topo:** Angular separation and invariant-mass cuts
- **Trigger Level Analysis (TLA):** Record only HLT objects (~6.5 KB vs ~1 MB), enabling 1-10 kHz recording

### False Positive Management
- **Trigger menu:** ~1,500 chains in Run 3
- **Prescale factors:** Configurable at L1 and HLT (N = 1 in N recorded; -1 = disabled)
- **Dynamic adjustment:** TrigMenuRulebook automatically loosens prescales as luminosity decays
- **Working points:** Loose, medium, tight identification + isolation requirements

---

## Case Study 2: LIGO/Virgo/KAGRA (LVK)

### Alert Pipeline Latency (O4)
- **Calibration/transfer:** ~5-10 seconds
- **Median preliminary alert:** 29.5 seconds (down from ~2 min in O3, ~27 min in O2)
- **Early warning:** -3.1 seconds (3.1 seconds BEFORE merger for massive BNS)

### Multi-Pipeline Search Architecture
**Four CBC (compact binary coalescence) pipelines:**
- GstLAL
- PyCBC Live
- MBTA
- SPIIR

**Two burst (unmodeled) pipelines:**
- cWB (coherent WaveBurst)
- oLIB

**New in O4:**
- Aframe (machine learning for binary black holes)

### GraceDB (Gravitational-Wave Candidate Event Database)
- Centralized web service at gracedb.ligo.org
- **Superevent abstraction:** Groups candidates within 1 second into single astrophysical source
- **Preferred event selection:** Based on detector participation and network SNR

### Automated Annotation
- **BAYESTAR:** 3D sky localization (seconds, not MCMC - uses Gaussian quadrature)
- **p_astro classification:** Four categories (BNS, NSBH, BBH, terrestrial)
- **EM-bright properties:** Probability of neutron star component
- **DQR:** Data quality checks

### False Alarm Rate Thresholds (O4)

| Alert Type | FAR Threshold | Rate |
|------------|---------------|------|
| Public preliminary | ≤ 2.3 × 10⁻⁵ Hz | ~2 per day |
| Significant CBC | ≤ 3.9 × 10⁻⁷ Hz | ~1 per month |
| Significant burst | ≤ 3.2 × 10⁻⁸ Hz | ~1 per year |

**Trials factor:** Accounts for multiple independent pipelines (initially 5 for CBC)

### Time-Slide Background Estimation
- PyCBC Live: Time-shifts single-detector triggers by 100 ms multiples
- Light travel time between detectors: ~10 ms
- All coincidences from time-shifts = unphysical (pure noise)
- FAR = count of accidental coincidences with ranking statistic ≥ candidate

### Human Vetting
- **Rapid Response Team:** 600+ LVK members
- **Timeline:** Within 24 hours
- **Outcomes:** Initial alert + GCN Circular, or Retraction
- **Updates:** Bilby parameter estimation over hours to days

---

## Case Study 3: Zwicky Transient Facility (ZTF)

### Scale
- **Median alerts per night:** ~363,000
- **Peak alerts (Galactic plane):** > 1 million
- **End-to-end latency:** ~13 minutes (95th percentile)
- **Kafka distribution:** ~6-10 seconds after generation

### Pipeline
1. **ZOGY algorithm:** Image differencing against deep reference templates
2. **Source extraction + photometric calibration**
3. **Machine-learning vetting (braai)**
4. **Apache Avro serialization:** ~60 KB per alert
   - PSF-fit photometry
   - 30 days detection history
   - Forced photometry
   - Three 63×63 pixel cutouts (science, reference, difference)

### braai (Bogus/Real Adversarial AI)
- **Architecture:** Convolutional neural network
- **Output:** 0-to-1 real/bogus score (`drb` field)
- **Typical thresholds:** 0.3-0.7 depending on purity requirements

### Community Broker Ecosystem

| Broker | Institution | Key Features |
|--------|-------------|--------------|
| **ANTARES** | NOIRLab/Arizona | Multi-wavelength cross-matches (Gaia, SDSS, WISE, Chandra); user-defined Python filters; ~45 alerts/sec across 200 threads |
| **ALeRCE** | Chile | Two-stage ML: CNN stamp classifier (~94% accuracy) → hierarchical random forest light-curve classifier (15 types); ATAT transformer (82.9% F1 across 20 classes) |
| **Lasair** | Edinburgh | SQL-based filtering; Sherlock classification engine; rapid spatial cross-matching |
| **AMPEL** | Berlin/DESY | Four-tier framework (filter → combine → analyze → react); full provenance tracking; ZTF + IceCube multi-messenger |
| **Fink** | France | Apache Spark Structured Streaming; tested at 100,000 alerts/minute (5× LSST rate); ~12 science modules including active-learning SNe classifiers |

### LSST Preparation
- ZTF = ~10% of LSST's expected 10 million alerts/night
- All 7 selected LSST full-stream brokers battle-tested on ZTF

---

## Case Study 4: General Coordinates Network (GCN)

### History
- **1992:** Originated as BACODINE (CGRO tape recorder failure → TDRSS real-time relay)
- **Evolution:** Gamma-ray Coordinates Network → General Coordinates Network (July 2022)

### Two Communication Channels

#### GCN Notices
- **Format:** Automated, machine-readable
- **Latency:** Within seconds of detection
- **Content:** Trigger times, sky coordinates, error regions, significance parameters
- **Modern format:** JSON over Apache Kafka
- **Legacy compatibility:** 160-byte binary packets, VOEvent XML

#### GCN Circulars
- **Format:** Human-written astronomical telegrams
- **Timeline:** Minutes to hours
- **Content:** Observations, analysis, follow-up plans

### Pivotal Moment: GW170817 (August 17, 2017)
| Time | Event |
|------|-------|
| T+0 | Merger |
| T+16s | Fermi-GBM GCN Notice |
| T+27min | LIGO GCN Notice |
| T+40min | GCN Circular (GW/GRB association) |
| T+5.2hr | Refined 3-detector localization (~28 sq deg) |

**Result:** ~70 observatories across 7 continents; paper with ~4,000 co-authors

### Current Interconnections (14+ missions)
- LIGO/Virgo/KAGRA gravitational-wave alerts
- Fermi and Swift gamma-ray triggers
  - Swift BAT: 13-30 seconds
  - Swift XRT: 30-80 seconds
- IceCube Gold/Bronze neutrino alerts (~30-60 seconds)
- Ground-based survey discoveries

### SCiMMA HOPSKOTCH
- Alternative Kafka platform used by LVK
- Complements GCN distribution

---

## Latency Comparison Across Domains

| System | Latency | Dominant Constraint |
|--------|---------|---------------------|
| ATLAS L1 | < 2.5 μs | Front-end buffer depth; speed of light |
| ATLAS HLT | ~300 ms/event | CPU processing; pile-up complexity |
| LIGO preliminary | ~29.5 s | Data calibration/transfer; pipeline processing |
| LIGO early warning | -3.1 s (before merger) | Inspiral signal accumulation |
| Fermi-GBM | ~10-15 s | TDRSS satellite relay |
| Swift BAT | 13-30 s | On-board processing + TDRSS |
| ZTF end-to-end | ~13 min | Image differencing pipeline |
| ZTF Kafka | ~6-10 s | Network transfer |

---

## Three Converging Architectural Principles

### 1. Cascading Filters with Increasing Sophistication
- **ATLAS:** FPGA pattern-matching (μs) → full-event ML classification (ms)
- **LIGO:** Matched-filter detection (s) → BAYESTAR localization → full Bayesian (hours)
- **ZTF:** Image differencing → braai scoring → multi-broker ML (CNNs, random forests, transformers)

**Pattern:** Each stage trades latency for precision

### 2. False-Alarm-Rate Quantification as Universal Decision Metric
- **ATLAS:** Prescale factors; rate-vs-purity optimization curves
- **LIGO:** Explicit FAR thresholds with time-slide background estimation
- **ZTF:** braai score maps to false-positive rate tunable by science programs

**Key insight:** Binary real/false insufficient; quantitative FAR enables downstream thresholding

### 3. Publish-Subscribe Distribution Enabling Community-Scale Science
- **Shift:** Point-to-point protocols → Kafka-based streaming
- **Benefits:**
  - Built-in replication for reliability
  - Consumer-group parallelism for scalability
  - Offset tracking for rewindability
  - High throughput (ZTF: ~80,000 alerts/minute)

**ZTF broker ecosystem:** Single alert stream → 7 independent classification systems, each adding unique value

---

## Technology Stack Convergence

### Serialization
- **Apache Avro:** Compact binary format (ZTF: ~60 KB/alert)
- Benefits: Schema evolution, compactness, language-agnostic

### Distribution
- **Apache Kafka:** Universal choice across GCN, ZTF/ZADS, LIGO/SCiMMA, Rubin
- Replaced legacy VOEvent/VTP (lacked replay, encryption, scaling)

### Machine Learning
- **Real-time inference:** braai (CNN), ALeRCE (CNN + random forest), Fink (Spark Streaming)
- **Graph neural networks:** ATLAS b-tagging (GN1, 2023)
- **Transformers:** ALeRCE ATAT for light-curve classification

### State Management
- **GraceDB:** Label-based state tracking (enabled LIGO's latency improvement)
- **GCN:** 30-year evolution from pager alerts to cloud-native Kafka

---

## Relevance to Agent Message Routing

### Directly Applicable Patterns

| Scientific Pattern | Agent System Analog |
|-------------------|---------------------|
| Cascading filters (L1 → HLT) | Tiered agent triage (signal → classification → action) |
| Prescale factors | Dynamic priority adjustment based on system load |
| FAR thresholds | Confidence scoring for agent-generated alerts |
| Time-slide background | Historical pattern analysis for false-positive estimation |
| Superevent grouping | Multi-source correlation (same event, different agents) |
| Community brokers | Specialized downstream processors (NEXUS, RED, etc.) |
| Kafka consumer groups | Parallel agent processing with offset tracking |
| Avro serialization | Compact, schema-evolvable message format |
| GCN Notices + Circulars | Automated alerts + human-authored analysis |

### Key Insights for Implementation

1. **Latency is domain-specific:** Microseconds for hardware triggers, seconds for alerts, minutes for human vetting
2. **Quantified uncertainty:** FAR/p_astro scores more useful than binary classifications
3. **Redundant pipelines:** Multiple independent detection systems provide robustness
4. **Community brokers:** Downstream specialization without upstream complexity
5. **Replay capability:** Offset tracking enables reprocessing and recovery
6. **Dynamic resource allocation:** TrigMenuRulebook-style adjustment to changing conditions

---

## Summary

Scientific alert systems have evolved into a mature discipline with proven patterns:
- **Hardware → software → ML** cascading filters
- **Quantified false-alarm rates** as decision boundaries
- **Kafka-based pub-sub** for scalable, reliable distribution
- **Community broker ecosystems** for specialized downstream processing

The convergence across ATLAS (particle physics), LIGO (gravitational waves), and ZTF (optical astronomy) demonstrates these patterns are domain-agnostic and applicable to agent message routing architectures.
