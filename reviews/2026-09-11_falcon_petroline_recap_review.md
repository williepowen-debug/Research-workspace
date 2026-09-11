# FALCON Petroline and WARRISK recap — evidence review

**Assessment:** the reported official shutdown supports FALCON's event confirmation, but several satellite conclusions exceed the evidence, and the insurance proposal needs a narrower deliverable. Correct the analytical statements before propagating the recap as verified.

Read set: FALCON's two September 11 Petroline reports, the saved four-zone FIRMS CSV, STATUS, EXIT_PROTOCOL, FAL-05, WARRISK, and FRESH_LEG_BASELINE. External checks: AP's account of the ministry statement, NASA FIRMS documentation, and the LMA's current marine page and JWLA-034 circular. No FALCON files were edited or messages sent. This is a targeted recap review, not an audit of the entire war history or a fresh satellite download.

## What is supported

AP independently reports that Saudi Arabia announced the East-West pipeline shutdown following attacks, with the ministry describing it as precautionary. This supports the shutdown headline; this review did not retrieve the ministry's original post. Multiple news relays remain reporting of one official statement, not multiple independent physical measurements. [AP report](https://apnews.com/article/yemen-houthis-iran-mokha-mandeb-shipping-saudi-025d052a14d9481258d51009a76d0bd6).

The earlier FALCON report explicitly registered an operator/ministry statement as a resolver. The later report bases Tell #2 on that resolver, not on satellite geometry. Rejecting the geometry inference after its control failed was appropriate. The registered D→85 rule and FAL-05 distinguish confirmation of a strike from their additional grading conditions; this review does not recommend retrospectively changing those rules.

## Findings and required clarifications

### 1. VERIFIED: the saved observations do not support “still growing 36 hours later”

File: `AGENTS/FALCON/domain/firms/2026-09-11_FIRMS_own-pull_petroline-corridor_four-zones.csv`; report §3.2.

The RIYADH rows begin **2026-09-10 09:30 UTC** and end **2026-09-11 10:51 UTC**: **25 hours 21 minutes**, not 36 hours. The later maximum FRP of 158.5 MW is present; so is the earlier 29.58 MW. Those observations support reporting increased observed maximum FRP, not the stated 36-hour timing or a measured repair duration.

The CSV contains 108 rows for September 10–11 only. It does not preserve the reported 427-row corridor population, September 9 baseline, or terminal-control samples. Consequently those controls cannot be independently reproduced from the cited evidence file alone. Preserve the full response and selection recipe if these controls support the conclusion.

### 2. UNSUPPORTED INFERENCE: first detection is being presented as ignition and attack time

Report §3.3 says the thermal record contradicts the circulating strike time. Its observed time is a satellite acquisition, not a continuous observation of ignition. A report published at 17:56 and an anomaly detected earlier are not themselves contradictory. Moreover, FALCON explicitly cannot locate the detected zones on the pipeline.

Use: **“An anomaly in the selected Riyadh zone was detected by 09:30 UTC; association with the pipeline attack and ignition time remain unestablished.”** Correct any independently identified publication/event-time confusion, but do not substitute another unproven event timestamp.

### 3. UNSUPPORTED INFERENCE: nondetection is treated as proof of no flares and no terminal damage

Report §§3.1 and 3.5 assert that the previous-day blank rules out flares, and terminal observations establish “CLEAN” endpoints and mid-line damage. NASA explains that cloud, smoke, observation gaps and detection limits can hide fires; its thermal-anomaly product does not assign cause. Detections elsewhere in the bounding box do not establish adequate observation at every selected site. [NASA FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq).

Even establishing no active fire at a terminal would not establish that the terminal is undamaged or operating normally. And because the hotspots have not been associated with the pipeline, their persistence cannot yet establish pipeline repair difficulty. The control that defeated the route inference must also constrain every downstream claim depending on that association.

Required next evidence: site-specific coverage/cloud checks, a longer thermal baseline, reliable asset coordinates or independently geolocated imagery, and operator evidence about damage and operations. Until then label the thermal findings as candidate anomalies and remove the definitive damage-location/repair-duration claims.

### 4. DISTINGUISH: an untriggered prediction is not a measurement of zero supply loss

FAL-05 requires specified evidence: a qualifying crude/condensate force majeure; stated qualifying production/export capacity offline for seven elapsed days; or a qualifying terminal-loading suspension. A disruption can exist before those thresholds are met. “FAL-05 not triggered” is therefore not equivalent to “zero barrels lost.”

Use **“Net crude supply loss is unquantified; the registered prediction has not met its failure conditions.”** The 197-day historical claim was not independently audited here. Likewise, do not describe an unsuccessful force-majeure search as proof that no declaration exists.

Report §4.2 also calls the volume limb “CLEARED MANY TIMES OVER” while admitting that the stated-offline-volume evidence needs a better primary. Separate pipeline nameplate capacity, normal routed flow, qualifying offline export/production capacity, and actual net supply loss. Have BRENT reconcile these quantities and FALCON identify the exact qualifying statement before treating duration as the only unresolved limb. Name the shutdown clock's evidentiary start; do not anchor it to an unassociated hotspot.

Preserve original scored probabilities and registered trigger rules. Separately explain whether present risk assessments changed; a frozen score or trigger is not a reason to suppress new evidence from current analysis.

### 5. VERIFIED: JWC provides a useful geographic channel, not a replacement premium series

The official JWLA-034 circular is dated **July 29, 2026**, amends Saudi Arabia and regional waters, and specifies a northern Red Sea boundary at **25.5°N**, consistent with the cited Yanbu location being within the region. [Official circular](https://lmalloyds.com/wp-content/uploads/2025/06/JWLA-034-Saudi-Arabia.pdf).

The LMA states that rating is negotiated between brokers and underwriters; JWC does not set it. A geographic listing change is not a premium observation, and an unchanged listing is not proof that rates stayed flat. Private negotiation also does not establish that premium quotes are never reported or that commercial products cannot supply useful assessments. [LMA marine page](https://lmalloyds.com/specialist_area/marine/).

FALCON's own `domain/FRESH_LEG_BASELINE.md:21` already records JWLA-034, July 29, the 25.5° boundary and Yanbu's inclusion, annotated August 31. The finding may be absent from WARRISK, but it is not new to the desk's recorded knowledge. This is partly a reconciliation/consumption task.

## Recommended assignment

First correct the timing and unsupported thermal inferences in the source report and its summaries, preserving the official-statement confirmation. Retain the raw baseline/control data and identify which assertions remain independently testable.

Then undertake the proposed bounded free-source pass with a specific output: a table separating **geographic listings**, **cover restrictions**, and **dated premium observations**, with source, date, contract/voyage basis and limitations. Reconcile the already-recorded JWC finding. Report which WARRISK questions the free sources actually answer and which remain unknown; do not refresh the premium-data clock using a listing circular. Evaluate any paid source against the remaining question, rather than assuming it contains—or cannot contain—the required number.

The cited Hormuz “7%” is described in the report as a September 6 PortWatch print. Carry that date and the vessel-transit basis into the recap; it is not a same-day measurement of crude flow.
