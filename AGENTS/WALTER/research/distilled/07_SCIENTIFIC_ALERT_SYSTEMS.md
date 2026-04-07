# Prompt 7 Distilled: Scientific Alert Systems — What We Keep

**Source discipline:** Particle physics (ATLAS/CERN), gravitational-wave astronomy (LIGO), optical astronomy (ZTF), multi-messenger coordination (GCN)
**Core question answered:** How do you extract rare, real signals from overwhelming data streams, quantify your confidence, and distribute validated alerts to a global community in real time?

---

## The Big Idea: Cascading Filters with Quantified Confidence

Three world-class scientific facilities — ATLAS, LIGO, and ZTF — independently converged on the same architecture: **tiered filters that trade latency for precision at each stage, with explicit false-alarm-rate quantification instead of binary real/fake classification.**

ATLAS processes 40 million collisions per second and keeps 0.003%. LIGO detects gravitational waves buried in seismic noise. ZTF scans 600,000+ astronomical alerts per night. All three solved the "needle in a haystack at scale" problem the same way:

1. **Fast, cheap filter** — eliminates obvious noise (ATLAS hardware trigger: <2.5 microseconds)
2. **Slower, smarter filter** — applies real analysis to survivors (ATLAS software trigger: ~300ms)
3. **Human vetting** — final judgment on what matters (LIGO Rapid Response Team: within 24 hours)

Each stage is allowed to be wrong — but the error rate is quantified and tracked.

---

## Four Patterns to Implement

### 1. Tiered Rejection (The ATLAS Cascade)

Don't do heavy processing on every signal. Most incoming information is noise — kill it early and cheap, save resources for the real stuff.

| Stage | ATLAS | WALTER |
|-------|-------|--------|
| **Tier 1: Pattern match** | FPGA hardware, <2.5µs, kills 99.75% | Gate 1 of Filter Spec: relevance check. Does this touch our thesis at all? Kill obvious noise instantly. |
| **Tier 2: Full analysis** | 60,000 CPU cores, ~300ms, kills 97% of survivors | Gate 2+3: domain classification + precedence assignment. Which agent, how urgent? |
| **Tier 3: Human judgment** | Physicist review, hours-days | Will reviews FLASH/IMMEDIATE signals. Agents synthesize PRIORITY signals. |

**The critical number:** ATLAS keeps 0.003% of raw input. We should expect to filter aggressively too. If WALTER is routing more than ~20-30% of incoming information, the filter is too loose.

### 2. Confidence Scores, Not Binary Classification (The LIGO Pattern)

LIGO doesn't say "this is real" or "this is fake." It says "this event has a false alarm rate of 1 per month" or "1 per year." Downstream consumers set their own threshold based on their tolerance for false positives.

**Our implementation:** Every signal WALTER produces carries a confidence score (0.0–1.0), already specified in the Signal Format Spec. But the key insight is: **agents should be able to set their own threshold.**

- RED (adversarial) might want to see signals at 0.3 confidence — looking for weak counter-evidence
- REGINALD (position-critical) might only act on signals at 0.7+ — needs high confidence before adjusting bank thesis
- Will scanning the COP sees precedence levels, which reflect WALTER's confidence assessment

Binary "route or don't route" is too blunt. Confidence scores let the same signal mean different things to different consumers.

### 3. Superevent Grouping (The GraceDB Pattern)

LIGO's GraceDB groups multiple detection pipeline outputs — arriving within 1 second of each other — into a single "superevent." Different detectors may see the same gravitational wave slightly differently, but GraceDB recognizes they're all the same event and consolidates them.

**Our translation:** When CARL flags consumer stress from gas prices, BRENT flags oil supply disruption, and LIQUID flags credit widening — all in the same 24-hour window — WALTER should recognize these as ONE convergence event, not three separate signals.

**Implementation:**
- Convergence detection: if 2+ signals from different domains point at the same underlying cause within a time window, group them
- The COP entry is the superevent: "CARL+BRENT+LIQUID convergence: oil→consumer→credit stress chain firing simultaneously [Apr 7]"
- Individual signals still exist in the archive for detail, but the COP shows the grouped picture

This is how convergence becomes VISIBLE rather than requiring someone to manually cross-reference three agent STATUS files.

### 4. Community Broker Ecosystem (The ZTF Pattern)

ZTF produces one alert stream. Seven independent broker systems — each run by different institutions with different specializations — consume that same stream and add their own analysis. ANTARES cross-matches against X-ray catalogs. ALeRCE runs ML classifiers. Fink does streaming analytics.

**Our translation:** WALTER produces one signal stream (the archive + COP). Downstream agents are specialized "brokers":

| ZTF Broker | Our Agent | Specialization |
|-----------|-----------|---------------|
| ANTARES (cross-match) | NEXUS | Cross-domain synthesis |
| ALeRCE (ML classifier) | RED | Adversarial classification |
| Lasair (SQL filtering) | REGINALD | Bank-specific filtering |
| AMPEL (filter→analyze→react) | CARL | Consumer chain analysis |

Single stream in, specialized analysis out. Adding a new agent = adding a new broker. No upstream changes needed.

---

## The Dual-Channel Communication Pattern (GCN)

The General Coordinates Network runs two parallel channels:
- **Notices:** Automated, machine-readable, arrives in seconds (JSON over Kafka)
- **Circulars:** Human-written analysis, arrives in minutes to hours

The pivotal moment: when LIGO detected the neutron star merger GW170817, the automated Notice went out in 16 seconds. The human-written Circular (explaining what it meant) followed in 40 minutes. Result: 70 observatories across 7 continents coordinated follow-up observations. 4,000 co-author paper.

**Our translation:**
- **Notice = push notification:** Automated, terse, seconds. "HY OAS crossed 320. IMMEDIATE."
- **Circular = COP entry or Telegram briefing:** Human-authored context. "HY OAS crossing 320 matters because it breaks the complacency narrative LIQUID has been tracking. Combined with the Blackstone gate breach, this suggests credit stress is no longer contained to private markets."

Both channels serve different needs. The notice triggers action. The circular provides understanding.

---

## Failure Modes That Will Bite Us

### 1. Prescale Drift
ATLAS dynamically loosens its trigger thresholds as beam luminosity decays — accepting more events when the system can handle it. But if thresholds aren't tightened back when conditions change, noise floods in.
**Our risk:** WALTER loosens filters during quiet periods ("let's see more signals"), then a crisis hits and the system is overwhelmed.
**Fix:** Filter thresholds are invariant to system load (per the ESI triage distillation). Adjust MINIMIZE level, not filter sensitivity.

### 2. Alert Fatigue from Low-Confidence Signals
ZTF's braai classifier produces a 0-1 score. If you set the threshold at 0.3, you get volume but lots of garbage. At 0.7, you get purity but miss marginal events.
**Our risk:** Routing too many 0.3-0.5 confidence signals trains agents to ignore WALTER's output.
**Fix:** Default routing threshold at 0.5+. Below that, signal exists in archive but doesn't appear on COP or get pushed. Agents who want lower-confidence signals can browse the archive directly.

### 3. Superevent Over-Grouping
GraceDB uses a 1-second time window. Too wide and you group unrelated events. Too narrow and you miss related ones.
**Our risk:** WALTER sees "credit" in two signals on the same day and calls it convergence when they're actually unrelated.
**Fix:** Convergence requires shared CAUSAL mechanism, not just topical overlap. Gas price spike + consumer DQ rise = convergence (causal chain). Bank earnings miss + JOLTS update = coincidence (different chains). WALTER must trace the transmission chain, not just match keywords.

---

## What We Don't Need From Scientific Alert Systems

- FPGA hardware trigger design — software-only system
- Time-slide background estimation — no statistical noise floor to measure
- 3D sky localization, gravitational-wave inspiral physics — no spatial coordinates
- Optical image differencing, PSF-fit photometry — no pixel data
- Multi-wavelength cross-matching catalogs (Gaia, SDSS, WISE) — no electromagnetic spectrum
- Apache Avro serialization specifics — markdown files are our format
- Kafka partition/replication tuning — already covered in Prompt 4
- IAU Circulars, ATELs, VOEvent XML — domain-specific publication formats

---

*Distilled from PROMPT7_SCIENTIFIC_ALERT_SYSTEMS_MASTER.md + PROMPT7_EXTRACTED_PRINCIPLES.md + PROMPT7 supplements | April 7, 2026*
