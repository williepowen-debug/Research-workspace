# Emergency dispatch message routing: a technical architecture reference

**Emergency calls traverse a layered system of telephony routing, geospatial lookup, structured triage, and computer-aided dispatch—each layer introducing both capability and fragility.** The U.S. 911 infrastructure is mid-transition from circuit-switched E-911 to IP-based NG911 (NENA i3), a shift that replaces tabular routing with geospatial SIP-based call delivery, enables multimedia, and promises resilience through mesh networking. Yet the transition itself creates compound risk: ~23 million wireless 911 calls are misrouted annually under legacy routing, ransomware has struck dozens of dispatch centers, and a **30% nationwide PSAP staffing shortage** strains even well-architected systems. This document covers the full technical stack—from RF signal to dispatched unit—with protocol specifics, standards references, algorithm logic, and failure-mode analysis suitable for designing robust emergency message routing systems.

---

## 1. From caller to PSAP: the routing architecture

### Legacy E-911: circuit-switched routing through selective routers

In legacy Enhanced 9-1-1, emergency calls follow a deterministic path: **Caller → End Office Switch → Selective Router → PSAP**. The Selective Router (SR)—typically a Nortel DMS-100 or equivalent—is a specialized tandem switch that receives all 911 calls from carrier end offices within its serving area. It extracts the **Automatic Number Identification (ANI)** from SS7 Initial Address Messages (carried in the Charge Number parameter) or legacy CAMA trunk MF tones (format: KP-NPD-NXX-XXXX-ST), then queries the **Selective Routing Database (SRDB)** to map that ANI to an **Emergency Service Number (ESN)**. The ESN determines which PSAP trunk group receives the call.

Once the call reaches the PSAP's Customer Premises Equipment (CPE), the system automatically queries the **ALI (Automatic Location Identification) database** over dual-redundant RS-232 serial data links (per NENA-STA-027.3), using STX/ETX framing with block check characters. The ALI database—maintained by LECs and managed by providers like Intrado—returns the caller's name, street address, Class of Service, and coordinates (for wireless Phase II). The **Master Street Address Guide (MSAG)** underpins this entire scheme: it maps street name ranges to ESNs, each ESN encoding the unique combination of law enforcement, fire, and EMS agencies serving that address.

For wireless calls, **Phase I** delivers cell tower sector location and a pseudo-ANI (pANI); **Phase II** adds handset-derived coordinates via an **Emergency Services Routing Key (ESRK)**. The fundamental limitation is that routing depends on the cell tower's location, not the caller's—a flaw that causes systemic misrouting at jurisdictional boundaries.

### NG911 (NENA i3): IP-based geospatial routing

The NENA i3 standard (NENA-STA-010 v3) replaces the entire circuit-switched chain with an all-IP architecture centered on the **Emergency Services IP Network (ESInet)**—a managed, QoS-guaranteed IP network interconnecting PSAPs, carriers, and core services. All calls enter as **SIP INVITE messages** carrying location in the **Geolocation header** (per RFC 6442) as either a PIDF-LO body (location-by-value via `cid:` URI) or a dereferenceable HTTPS URI (location-by-reference).

The core functional elements process calls as follows:

The **Border Control Function (BCF)** acts as a Session Border Controller at the ESInet ingress, performing SIP normalization, TLS/SRTP enforcement, firewall filtering, and media anchoring. The **Emergency Services Routing Proxy (ESRP)**—a SIP proxy often implemented on Kamailio—extracts the caller's location from the SIP INVITE and queries the **Emergency Call Routing Function (ECRF)** via the **LoST protocol (RFC 5222)**. The ECRF performs a **geospatial point-in-polygon query** against GIS-defined PSAP service boundary polygons and returns the destination PSAP's SIP URI. The ESRP then forwards the SIP INVITE accordingly.

**LoST (Location-to-Service Translation, RFC 5222)** is an XML-over-HTTPS protocol. A `<findService>` request contains location (civic or geodetic in PIDF-LO format) and a service URN (`urn:service:sos`). The response returns one or more SIP URIs plus optional service boundary polygons in GML, enabling clients to cache routing decisions until the device crosses a boundary. A **Forest Guide** hierarchy enables cross-domain routing discovery for inter-state and inter-ESInet scenarios.

**PIDF-LO (RFC 4119, RFC 5139, RFC 5491)** is the canonical XML location format. It supports geodetic shapes (Point, Circle, Ellipse, Polygon, Prism in WGS84) and civic address elements (country, A1-A6 administrative divisions, road name, house number, floor, postal code). The `<method>` element indicates derivation (GPS, WiFi, Cell, Manual), and per RFC 5491, entities **must not convert** between civic and geodetic forms before PSAP delivery.

The **Location Information Server (LIS)** stores device locations and serves them via the **HELD protocol (RFC 5985)**—an HTTP/HTTPS protocol supporting retrieval by-value (returns PIDF-LO directly) or by-reference (returns a dereferenceable URI). The **Location Validation Function (LVF)**, also a LoST server, validates civic addresses against GIS data before storage. Legacy interworking is handled by the **Legacy Network Gateway (LNG)**, which converts CAMA/SS7 calls to SIP and queries ALI to construct PIDF-LO, and the **Legacy PSAP Gateway (LPG)**, which reverse-converts SIP to legacy signaling for non-upgraded PSAPs.

### Location determination: from cell sectors to floor-level precision

Modern location determination uses a hierarchy of methods. **Cell-ID/sector-based** positioning (100 m urban to several km rural) underpins Phase I routing. **Network-based trilateration** using TDOA (Time Difference of Arrival) across 3+ towers achieves 100–300 m accuracy. **Assisted GPS (A-GPS)** provides 3–15 m outdoor accuracy by supplementing satellite signals with carrier-provided ephemeris data. **WiFi positioning** (10–25 m urban) leverages Apple HELO and Google ELS databases mapping WiFi BSSIDs to coordinates, and is critical indoors where GPS fails. Modern smartphones combine all methods—GPS, WiFi, cell, barometric pressure, Bluetooth beacons—into **hybridized location** solutions.

The FCC's location accuracy mandates (47 CFR § 9.10) require **50-meter horizontal accuracy for 80% of wireless 911 calls** at 90% confidence. Vertical (Z-axis) requirements mandate **±3 meters for 80% of indoor calls** from Z-axis-capable devices, with deployment phased across the top 25 CMAs (by April 2021), top 50 (by April 2023), and nationwide (by April 2025). A March 2025 NPRM (FCC 25-22) proposes requiring Height Above Ground Level (AGL) format rather than Height Above Ellipsoid (HAE), and morphology-specific testing. The **dispatchable location** concept—street address supplemented by floor, suite, or room number—is the FCC's preferred delivery format when technically feasible.

### Jurisdictional routing: why 23 million calls go to the wrong PSAP

Legacy wireless routing's dependence on cell tower location creates systemic misrouting at jurisdictional boundaries. Intrado measured a **12.96% average misroute rate** in a sample of 5 million wireless calls; rates reach 20–50% along boundary zones. In the D.C. region alone, nearly 100,000 calls per year require inter-PSAP transfer, adding up to 40 seconds of delay per transfer. Fatal consequences have been documented: in Denver (July 2022), four 911 calls about a shooting victim were misrouted to a neighboring PSAP, with three callers hanging up during transfer holds.

NG911 geospatial routing fundamentally solves this by routing on the **caller's actual coordinates** rather than tower location. AT&T's deployed location-based routing correctly routes ~80% of calls, with ~10% of those having been previously misrouted. The FCC has proposed mandating location-based routing when horizontal accuracy falls within **165 meters at 90% confidence** (FCC-25-22). Massachusetts reports location-based routing reduced unwanted transfers by over **500,000 minutes per year**.

VoIP introduces additional routing failures: nomadic VoIP services route based on the subscriber's registered address, which may differ from actual location. Documented cases include a Houston VoIP call arriving at Nashville dispatch, and a Connecticut infant death when a Vonage 911 call reached a recorded non-emergency message.

---

## 2. CAD integration and dispatch algorithms

### Data flow from 911 systems into dispatch software

In legacy E-911, call data enters CAD through a serial pipeline called the **ALI spill**. When the PSAP's CPE receives a call and retrieves the ALI record, it forwards structured text (ANI, address, metadata) over RS-232 or TCP/IP to the CAD system, which parses the fields to auto-populate an incident record. NENA-STA-027.3 specifies the protocol: STX/ETX framing, dual-link architecture with 60-second heartbeats, and ACK/NAK reliability.

In NG911, the **Emergency Incident Data Object (EIDO)**, defined in NENA-STA-021, replaces the serial ALI spill with a **JSON-based canonical data structure** transmitted via **Secure WebSocket** connections (NENA-STA-024.1.1-2025). EIDO documents carry an Incident Tracking Identifier (a globally unique URN like `urn:emergency:uid:Incidentid:0:police.state.pa.us`), incident status, dispatch data, person/vehicle information, locations, and additional data. The **Incident Data Exchange (IDX)** functional element aggregates EIDOs from multiple sources into a composite incident representation. EIDO uses NIEM data types for semantic consistency across justice, public safety, and emergency management domains.

**RapidSOS** operates as a de facto national **Additional Data Repository**, bridging 600+ million connected devices (Apple iOS 12+, Android, Uber, connected vehicles, wearables, MedicAlert) to PSAPs. Its RAD-E RESTful API enables native CAD integration, delivering supplemental location data within milliseconds—versus the 25–30 seconds typical of legacy Phase II ALI re-bids. Coverage reaches ECCs receiving **99%+ of U.S. 911 calls**.

### Unit recommendation: four tiers of algorithmic sophistication

CAD systems employ a tiered approach to unit selection:

**Tier 1 (static run cards)** uses pre-configured zone-based response templates. Each geographic zone has a fixed response order (e.g., Zone AB241: Station 2 first, then 4, then 1). This requires minimal GIS but cannot adapt to real-time conditions. **Tier 2 (centroid-based)** calculates straight-line distance from unit AVL positions to zone centroids, which can be weighted for terrain obstacles. **Tier 3 (geocoded matching)** translates call addresses to coordinates via street centerline databases and compares against AVL positions. **Tier 4 (network analysis)** uses **routable GIS** with intersection attributes (turn restrictions, one-way streets, divided highways) to compute actual drive-time isochrones, sometimes incorporating real-time traffic data.

Modern CAD platforms (Mark43, CentralSquare, Versaterm, Caliber CAD NG) implement Tier 4 algorithms. Each unit is modeled with capability tags (engine type, hazmat certification, water rescue, K-9, tactical), and the system simultaneously evaluates location, status, capabilities, estimated travel time, and traffic conditions to produce a **ranked shortlist**. Dispatchers retain final selection authority—a deliberate human-in-the-loop design.

**Run cards** define the unit complement per incident type and location. A structure fire might specify 2 engines, 1 ladder, 1 battalion chief, and 1 ambulance. When resources are depleted, systems implement priority queuing (higher-priority incidents claim resources first), **must-cover station monitoring** (if dispatching a unit leaves a station uncovered, the system recommends a move-up unit), and pre-assignment of waiting calls to committed units.

### Multi-agency coordination remains the critical gap

CAD-to-CAD interoperability is the industry's most significant unsolved problem. The National 911 Program's 2022–2023 assessment found that most inter-agency communication still relies on **phone calls, radio, and manual data re-entry**. Emerging solutions include **Data Exchange Hubs (DEHs)** like Denver's EDC deployment (11 agencies sharing incident data via NIEM XML), CentralSquare Unify (integrated with 30+ non-CentralSquare CADs), and RapidDeploy Exchange Link. The EIDO standard is intended as the universal interchange format, but adoption remains early-stage. The **ASAP-to-PSAP** protocol (deployed in ~120 ECCs across 21+ states) enables alarm monitoring companies to send structured alarm data directly to CAD.

---

## 3. Triage protocols and priority-driven dispatch

### Structured interrogation: the MPDS protocol engine

The **Medical Priority Dispatch System (MPDS)**, developed by Dr. Jeff Clawson and published by Priority Dispatch Corporation, is the most widely deployed structured EMD system. Its 36 protocols cover chief complaint categories through a rigid workflow: Case Entry → Chief Complaint Selection → Key Questions → Determinant Code → Response Assignment → Pre-Arrival Instructions.

Each determinant code follows a **number-letter-number format**: the first number (1–36) identifies the protocol card, the letter (Ω/A/B/C/D/E) indicates severity, and the second number specifies the sub-determinant. Optional suffix letters encode clinical detail (e.g., 6-D-1A = Breathing Problems, Delta severity, not alert, asthma history). MPDS version 13.0 contains **1,828 possible determinant codes**, each mapped to a locally configured response.

The six determinant levels drive resource allocation directly. **Echo** (immediately life-threatening, e.g., confirmed cardiac arrest) triggers maximum ALS response with lights-and-sirens. **Delta** (serious/urgent) and **Charlie** (moderate-high) receive ALS hot response. **Bravo** (moderate) may be hot or cold per local policy. **Alpha** (minor) receives BLS cold response. **Omega** (non-emergency) may be referred to nurse triage, urgent care, or alternative services—a critical pathway for system load management.

**ProQA**, the exclusive software implementation of MPDS, integrates directly with CAD systems. When a determinant code is generated, the associated response configuration transmits automatically to CAD for unit dispatch. Research from the London Ambulance Service (758,695 incidents) found dispatcher overrides of ProQA recommendations were rare (~0.22%) and did not improve patient outcomes. The **LowCode** extension enables Emergency Communication Nurses to further triage Omega-level calls, potentially diverting them from ambulance response entirely. Seattle's nurse navigator program redirects **40% of transferred calls** away from emergency response.

### Fire and police priority systems

Fire departments use **alarm levels** to scale resource deployment. A typical first alarm assignment includes 2–4 engines, 1–2 ladder companies, 1 rescue/squad, and 1 battalion chief (15+ personnel). FDNY's first alarm deploys 3 engines, 2 ladders, and 1 battalion chief; a working fire escalation adds a squad, rescue, and division chief. Each additional alarm roughly doubles cumulative resources. The Incident Commander determines escalation based on fire behavior, structure type, life hazard, and conditions.

**NFPA 1710** sets performance benchmarks for career departments: alarm answering within **15 seconds for 95%** of calls, alarm processing within **64 seconds for 90%**, first engine arrival within **240 seconds (4 minutes) for 90%**, and full first alarm assembly within **480 seconds (8 minutes) for 90%**. NFPA 1221 allows additional processing time for EMD questioning, PAIs, and location determination.

Police dispatch typically uses numeric priority systems (Priority 0–8), where Priority 0 (officer down, active shooter) triggers immediate Code 3 response from all available units, while Priority 5+ calls receive delayed or non-police handling. The IAED's Police Priority Dispatch System (PPDS) mirrors MPDS structure with Omega-through-Echo levels; research shows 46% of PPDS calls classify as Delta.

### Alternative response pathways reshape the dispatch model

The traditional binary dispatch model (police or EMS) is expanding into a multi-pathway system. **CAHOOTS** (Eugene, Oregon, founded 1989) pioneered civilian crisis response: two-person teams (medic + crisis worker) handled ~16,479 calls in 2021 (12% of all calls for service), with only **1.3% requiring police backup**. Denver's **STAR program** expanded from 1 to 8 vans, responding to 38% of eligible calls in 2023, with zero calls requiring police backup during its pilot.

**988 Suicide & Crisis Lifeline integration** represents the newest pathway. NENA-STA-045.1 provides the standard framework for 911/988 interactions. South Sound 911 (Washington) became the first center to embed 988 counselors directly in a 911 communications center (June 2023). MPDS Protocol 25 was completely revised in November 2022 to add explicit Crisis/Alternative Response pathways, with suffix codes routing violent situations to police while channeling non-violent behavioral health calls to alternative responders. Fewer than **2% of 988 contacts** require escalation to emergency services.

The routing logic follows a decision tree: violence/weapons/crime-in-progress → police; life-threatening medical → EMS/fire; behavioral health crisis without safety threat → alternative team (CAHOOTS/STAR/mobile crisis/CIT officer); low-acuity medical → nurse triage. CAD systems flag eligible calls based on nature codes and absence of safety indicators, with standard police/EMS fallback if alternative responders are unavailable.

---

## 4. Failure modes, resilience, and cybersecurity

### Catastrophic single points of failure persist

The most dangerous architectural pattern in emergency dispatch is **concentration of critical functions**. The April 2014 Intrado outage exemplifies this: a single software counter (PTM value) in Intrado's Emergency Call Management Center in Englewood, Colorado, reached its 40-million maximum, preventing unique identifier assignment to incoming calls. This single defect caused **11 million people to lose 911 service for up to 6 hours**, blocked calls to 81 PSAPs across 7 states, and resulted in 6,600+ calls never reaching a dispatcher. The backup facility in Miami required manual failover that took until 6:00 AM to activate.

The CenturyLink December 2018 outage disrupted 911 across **22+ states for 49 hours**, affecting 3.5 million Comcast VoIP customers and causing 75 confirmed failed 911 calls in Texas and Montana alone. In October 2016, a Level 3 technician's erroneous entry (a blank field interpreted as "block all calls") blocked VoIP 911 calls nationwide for 90 minutes.

NG911 architectures promise self-healing mesh redundancy—ESInets must achieve **99.999% availability** and survive total destruction of any single core node. But the transition creates new concentration risks: when one vendor's NGCS serves multiple states (as Intrado's did), IP-based centralization can produce failure modes worse than legacy regional selective routers. Pennsylvania's 2024 NG911 outage—caused by an OS defect disrupting statewide call delivery—demonstrated this directly.

### Ransomware forces dispatch centers to pen and paper

Between 2016–2018, **184 cyberattacks hit public safety agencies**, with 42 directly or indirectly targeting 911 centers and 24 involving ransomware. The pattern is consistent: ransomware encrypts CAD systems, forcing dispatchers to manual operations while phone and radio systems typically survive.

Notable incidents include Henry County, Tennessee (June 2016, one of the first 911 ransomware attacks, 3 days on paper), Baltimore (March 2018, CAD down for ~24 hours), Bucks County, Pennsylvania (January 2024, Akira ransomware, 650,000 population affected, lost CLEAN/NCIC database access), and a 2024 DragonForce attack disrupting dispatch in six South Bay California cities simultaneously. The attack surface is expanding: CAD systems are the most frequently targeted component, and stolen data (caller PII, law enforcement records) enables secondary crimes including extortion and swatting.

**Telephony Denial of Service (TDoS)** attacks pose a distinct threat. In October 2016, an 18-year-old distributed a mobile botnet via Twitter that compromised 1,000+ phones, causing them to continuously dial 911 and overwhelming centers in 12 states. Legacy selective routers have **"very limited capability to mitigate any kind of TDoS attack"** (NENA-INF-045.1-2022) because no front-end call filtering is possible. NG911 specifies TDoS mitigation mechanisms, but they are not yet widely deployed.

CISA's key recommendations for 911 cybersecurity include MFA implementation as first priority, immutable backup strategies, annual penetration testing, software bill of materials tracking, vendor security evaluations, and adoption of the NIST Cybersecurity Framework. NG911 grant programs now require PSAPs to demonstrate cybersecurity capabilities.

### System overload and the staffing crisis

Major incidents generate massive call surges against a backdrop of chronic understaffing. NENA reports a **~30% average staffing shortage** nationwide; a survey of 774 PSAPs found 166 centers with 30–49% vacancy and 13 with 70%+ vacancy. Training takes 3–18 months for new dispatchers, making rapid surge capacity impossible. Some communities report 911 hold times of **up to 20 minutes**.

Legacy systems have fixed CAMA trunk counts—when all trunks are busy, callers receive busy signals. NG911 enables automated overflow routing to backup PSAPs, but receiving centers often lack local geographic knowledge and dispatch coordination. During Hurricane Helene, North Carolina PSAPs routed calls to centers four hours away by car; dispatchers improvised coordination using Google Sheets. Wireless Priority Service (WPS) and Government Emergency Telecommunications Service (GETS) provide priority access for authorized personnel but cannot expand system capacity.

The FCC now requires providers to notify PSAPs within **30 minutes** of discovering a 911 outage (FCC 22-88). NENA recommends all redundant systems be tested monthly, and facilities should maintain backup PSAP arrangements, 72-hour power sustainability, and publicly available 10-digit administrative numbers. The trend toward PSAP consolidation (from 7,485 in 2013 to 5,748 in 2021) improves resource pooling but creates larger single points of failure requiring dedicated georedundancy.

---

## 5. The multimedia and smart-sensor frontier

### Text, video, and real-time text reach PSAPs

Text-to-911 volume grew from ~1,000 messages in 2014 to **507,969 in 2021** across 38 states, though texts remain under 0.1% of all 911 contacts. SMS messages route through carrier Short Message Service Centers to Text Control Centers (operated by vendors like Intrado), which present conversations to PSAPs via web interfaces or CPE integration. Key limitations include cell-sector-level location only (no GPS with SMS), no multimedia support, and store-and-forward latency.

**Real-Time Text (RTT, RFC 4103)** represents a fundamental improvement over both TTY (45.45 baud Baudot code) and SMS. RTT transmits text character-by-character over RTP using T.140 encoding, enabling full-duplex simultaneous voice and text, full Unicode, and integration within SIP sessions. The FCC mandated RTT support on IP-based wireless networks (4G LTE, 5G) with phased rollout through June 2021, and 2024 rules require location-based routing for RTT to 911. Direct-to-PSAP RTT eliminates the TRS relay intermediary, reducing communication latency from ~30 seconds to near-instantaneous.

Native video-to-911 is emerging through two vectors. **Google's Android Emergency Live Video** (launched 2025–2026) enables dispatchers to request opt-in, end-to-end encrypted live video during 911 calls. **Carbyne's c-Live platform** provides video, chat, and conferencing to 400M+ people worldwide, with 1M+ video minutes annually delivered to call centers. RapidSOS UNITE adds video capability across its 5,000+ partner agencies. AT&T's i3-compliant ESInet delivers photo and video natively in EIDO format. The NG911 architecture supports multimedia through SIP's SDP media negotiation—the same SIP session can carry voice, video, and RTT simultaneously.

### IoT and smart city data streams feed dispatch intelligence

The EU's **eCall** mandate (April 2018) requires all new passenger vehicles to automatically dial 112 upon crash detection, transmitting a **Minimum Set of Data** (≤140 bytes per EN 15722): VIN, GNSS coordinates, direction of travel, timestamp, passenger count, and vehicle type. The European GNSS Agency estimates eCall speeds emergency response by **40% in urban areas and 50% in rural**, averting ~2,500 deaths annually. **NG-eCall (RFC 8147)** extends this over SIP/IMS networks. The U.S. lacks a federal eCall equivalent, relying on voluntary services (OnStar, Toyota Safety Connect) and RapidSOS integration with telematics providers; APCO and NENA are jointly developing a **Vehicle Emergency Data Set (VEDS)** standard.

Acoustic gunshot detection systems (SoundThinking/ShotSpotter, deployed in 85+ cities) use AI-powered sensor arrays to detect, classify, and geolocate gunfire within seconds, feeding alerts directly into CAD for automatic incident creation. Smart building systems increasingly pipe structured data to ESInets: IP-connected fire alarm panels transmit zone-specific alarm data, AI-enabled cameras detect unholstered weapons and trigger automated lockdowns, and Building Information Models provide responders with floor-by-floor navigation. Apple Watch fall detection (Series 4+) and crash detection (Series 8+) automatically call 911 with location data after detecting impacts via accelerometer, gyroscope, barometer, and microphone fusion.

### Standards convergence enables the NG911 data ecosystem

The interoperability stack converging around NG911 includes several key standards. **NENA-STA-006** defines the GIS Data Model (road centerlines, address points, PSAP boundaries, emergency service boundaries) that underpins all geospatial routing via the ECRF. **NENA-STA-021/024** define EIDO and its WebSocket-based conveyance—the pivotal interchange format bridging call handling, CAD, inter-agency communication, and IoT data. **NIEM** provides the common data dictionary (XML/JSON) ensuring semantic consistency across public safety, justice, and emergency management domains; EIDO incorporates NIEM data types directly. **APCO Project 25 (TIA-102 series)** standardizes interoperable digital land mobile radio across its Common Air Interface, Inter-RF Subsystem Interface, and Console Subsystem Interface. **CAP (OASIS CAP v1.2)** provides the XML format for emergency alerts distributed through IPAWS/EAS/WEA.

The end-to-end NG911 data flow connects these standards: a device's SIP INVITE carries PIDF-LO location through the BCF to the ESRP, which queries the ECRF against NENA GIS data. Call-handling creates an EIDO-JSON document conveyed to CAD via WebSocket. Additional data (crash telemetry, medical profiles, building sensors) attaches via RFC 7852 SIP Call-Info headers. Inter-agency sharing uses NIEM-conformant EIDO. Field responders receive dispatch data over P25 radio and FirstNet broadband MDTs.

---

## Conclusion: designing for reliability, speed, and graceful degradation

Three architectural principles emerge from this analysis. First, **geospatial routing is non-negotiable**: the shift from tabular MSAG/SRDB lookups to ECRF point-in-polygon queries eliminates the ~23 million annual misroutes inherent in tower-based routing, and the LoST/PIDF-LO/SIP stack provides the protocol foundation. Second, **every layer must assume failure**: the Intrado, CenturyLink, and Pennsylvania outages demonstrate that IP-based centralization can produce catastrophic correlated failures worse than legacy regional isolation. Georedundant NGCS deployments with automatic (not manual) failover, monthly failover testing, and maintained 10-digit fallback numbers are minimum requirements. Third, **the data interchange problem is harder than the routing problem**: while EIDO and NIEM provide the schema, actual CAD-to-CAD interoperability remains the industry's most significant gap, and the heterogeneous vendor landscape means that Data Exchange Hubs and middleware will bridge systems for years before native EIDO adoption reaches critical mass. Systems architects should design for protocol-level resilience (SIP re-INVITE for location updates, WebSocket reconnection for EIDO streams, P25 fallback for data channel loss) while treating cybersecurity as a first-class architectural concern—not an afterthought layered onto dispatch infrastructure that was designed for a pre-internet threat model.