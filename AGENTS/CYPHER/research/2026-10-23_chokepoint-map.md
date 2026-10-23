# CYPHER — Chokepoint map: method, first build, first match (2026-10-23)

**Origin:** Will, CYPHER terminal 2026-10-23 13:40 ET, verbatim *"instead of us chasing the puck as things are reported randomly we should be trying to deduce where the problems will come from"*; option **A, "build it this session"** (13:41 ET).
**Ledger:** `workbook/CHOKEPOINTS.tsv` (32 rows). **Evidence:** three read-only research passes (session scratchpad files A_cores / B_platforms / C_infra, 2026-10-23; no system scanned or probed), plus CYPHER's own reads of the Mozilla bug thread, the OpenJDK trust store, the ConnectWise advisory page and Kiteworks' GitHub advisories.

## 1. Method

| Step | What | Why |
|---|---|---|
| 1 | **Map the shared nodes**: suppliers and utilities many US financial institutions depend on. For each: reliance count with basis, public stack, precedent, where the first public sign appears, and which boot leg would see it | Five past waves: money damage ran through ONE shared node (ICBC FS 2023, MOVEit 2023, CDK 2024, Change Healthcare 2024, TruStage 2026); widespread flaws in general stayed "loud and small" (KB-CYP-001) |
| 2 | **Match every new threat against the map first.** Question: "which chokepoint's public stack does this reach?", not "how loud is it?" | Turns intake from chasing reports into triage; most items should resolve to NONE-KNOWN in a minute |
| 3 | **Register each deduction as a dated prediction** (named instrument, hard resolve date, dated negative search) | The guard against finding risk everywhere (charter § RECORDED DISAGREEMENT; R0 on 2026-12-17 grades whether this beats DEWEY's WALTER-watch alternative) |

**Limits:** public sources only. 15 of 32 rows are `UNKNOWN-STACK`: no core or digital-banking vendor publishes its language/runtime. That is the honest default, not an all-clear. Names are suppliers; no exposed-bank list exists or will be written (guardrail 2).

## 2. What the map shows (deductions, each with its evidence)

| # | Deduction | Evidence | Confidence |
|---|---|---|---|
| D1 | **File-transfer products are the repeat door.** About one mass exploitation a year, several BEFORE the vendor's advisory | Accellion FTA 2020-21, GoAnywhere 2023, MOVEit 2023, Cleo 2024, GoAnywhere 2025 (exploited ~9/10, advisory 9/18) — CHK-12..15 | High on the pattern (5 events, 6 years, SECONDARY counts); the base rate is ours, not a published one |
| D2 | **Market-plumbing cyber hits land one ring OUT from the utility.** Every documented disruption AT a designated FMU or the Fed was non-cyber; both cyber cases hit a client or vendor | Fed 2021 operational error, DTCC 2026 erroneous trades, CME 2025 cooling, TCH 2023 human error, Visa 2018 hardware vs ICBC FS 2023 (BNY client), ION 2023 (FCM vendor) — CHK-21..31 | Medium (n=2 cyber cases) |
| D3 | **Ring one's biggest node is Broadridge:** fixed-income trade processing for 21 of the 25 primary dealers, >$15T/day (FY2025 10-K, search excerpt — open the primary before citing). An ICBC-FS-type event there touches 21 dealers at once. No incident found | CHK-29 | Medium on reach; the figure is VIA-SEARCH |
| D4 | **The IT-provider (MSP) layer into small banks and credit unions is live NOW** | ConnectWise Cloud Backup / Storm-0940: 162-173 tenants with unauthorized sign-ins (Huntress), financial services among the targeted sectors, restoration "by the end of this weekend" (ConnectWise 10/23 14:00Z); Axcient took a PHP-based partner portal offline 10/21-22 for PHP2Shell — CHK-16 | High that the channel is touched; nothing yet shows a bank harmed (1 of 88 bank/CU breach notices names an IT-provider route, KB-CYP-020) |
| D5 | **Private suppliers have no filing trigger, so their trouble surfaces late** | CSI, Corelation, Candescent (1,300+ FIs, vendor claim), TruStage, Marquis, Finastra, Kaseya, Cleo, ION: no SEC 8-K. Marquis 2025: first public sign = state AG breach portals ~3 months after the attack (CHK-10) | High |
| D6 | **Single-cloud common modes are growing** | Alkami entirely on AWS (301 FIs, 10-K); Q2 migrating to AWS (457); DTCC and OCC core clearing moving to AWS (SEC no-objection 2025, 2022); CME clearing to Google Cloud; Jack Henry Platform and Candescent on Google Cloud | High on the facts; go-live of the FMU migrations UNKNOWN. Mostly an outage (non-cyber) channel |
| D7 | **Java runtimes nobody updates are the eMudhra exposure tail** | OpenJDK cacerts carries the emSign G3 root AND the Comodo AAA root that cross-signed the weak-key intermediates; JSSE does not check revocation by default; GoAnywhere's installers bundle their own JRE (CHK-13). Fixed by Oracle's 10/21 update (CVE-2026-91403) — but only where someone applies it | High on the mechanism (FL-CYP-20); exploitation none reported (CISA SSVC 10/23) |

## 3. First match — current threats against the map (2026-10-23)

| Threat | Chokepoints reached | Wave_Touch | Next check |
|---|---|---|---|
| **PHP2Shell** (CVE-2026-109618/-109619) | CHK-32 perimeter appliances (Palo Alto: PAN-OS, Panorama, WF-500 affected, no exploitation known, hotfixes 10/26-10/30); CHK-16 (Axcient portal remediated, no compromise); CHK-15 Kiteworks only IF it runs PHP | POSSIBLE / CONFIRMED-touch / POSSIBLE | Kiteworks runtime statement (highest-value open cell); Palo Alto 10/30 |
| **eMudhra / Java** (CVE-2026-91403) | CHK-13 GoAnywhere (bundled JRE); CHK-14 Cleo (Java inferred only) | POSSIBLE / POSSIBLE (weak) | Did Fortra ship the trust update? (Fortra site is 403 to us) |
| **ConnectWise / Storm-0940** (CYB-INC-018) | CHK-16 directly; CHK-20 (M365/Entra) reached through it | CONFIRMED | Catalyst 10/26; client notices and state AG portals over the next 1-3 months (D5 lag) |
| **Cores, digital banking, FMUs** | No current threat maps to any public stack | UNKNOWN-STACK / NONE-KNOWN | — |

**Read:** today's wave touches the map at its EDGES (perimeter appliances, the MSP layer, file-transfer Java tails), not at a core processor or a market utility. That fits the mechanical (Log4Shell) reading of WAVE-2026-10, with one caveat that matters: **the MSP channel is a confirmed live compromise with a late-surfacing victim shape**, and that is the MOVEit shape in a different product.

## 4. Candidate predictions (NOT registered — need Will's word, as CYP-01/02 did)

| ID | Prediction | Desk odds | Resolves on |
|---|---|---|---|
| CYP-03 (cand.) | By 2026-12-31, a US bank, credit union, or core/digital-banking vendor publicly states that ConnectWise or another MSP/RMM tool was the entry route of a confirmed incident | 15% | State AG breach portals (Maine, California, Washington) + SEC 8-K legs 8/9 + named news search, dated search inside 12/24-12/31 |
| CYP-04 (cand.) | Between 2026-10-24 and 2027-04-30, CISA KEV lists a NEW CVE (published after 2026-10-23) in MOVEit Transfer, GoAnywhere MFT, Cleo Harmony/VLTrader/LexiCom or Kiteworks | 35% | CISA KEV JSON, dateAdded in window, vendorProject/product match; dated search 2027-04-24..30 |

Base rates: CYP-03 — 1 of 88 CA/WA bank/CU notices since 2023 name an IT-provider route (DEWEY), against 162-173 confirmed compromised tenants in this campaign with finance among the targeted sectors. CYP-04 — about one KEV-grade event a year across these four product families 2020-2025 (D1), so ~40% for six months; shaded down because two of the four are under heavy post-incident scrutiny.

## 5. Gaps carried

- Fiserv and FIS (the two largest cores) publish no client count; only survey shares (KC Fed 2024 on 2022/2020 data).
- No finance-specific reliance figure exists for any cross-industry platform (Treasury 2/2023 says regulators lack the data).
- Unreadable first-signal surfaces: Fortra, Cleo support, Kaseya helpdesk (403); CrowdStrike tech alerts (login); OCC, CME, SWIFT (403); DTCC notices (JS + 404 PDFs). The only machine-readable operator status page found is the Fed's (`app.frbservices.org/app/status/serviceStatus.do`) — a candidate boot leg, not built today.
- VIA-SEARCH figures (Broadridge, OCC, CME, Visa/Mastercard, BNY tri-party) are excerpts; open the primary before any is cited in a packet.
- Not covered: Velera (ex-PSCU/Co-op), COCC, FedComp, Sharetec, Google Cloud, Zelle/EWS, CLS, ICE Clear Credit.
