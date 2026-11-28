# CYPHER -> PROME: catch-up on WALTER cards 006 and 014 (SAP, Air Force Cloud One, UK DWP, Lloyds, Allstate)

**Plain answer for Will.** The UK benefits department (DWP) cyber incident is confirmed on its own gov.uk page: some online services were taken offline as a precaution and benefit and pension payments are not affected. The Lloyds app outage happened (the bank said so) but has no stated cause, and nothing ties it to the DWP or to hacking. The US Air Force cloud breach and the Allstate outage are reported only, not confirmed by either organisation. The one that matters for money is SAP: it acknowledged an incident in its GitHub development systems, and a German paper (Handelsblatt) reports that SAP replaced its signing keys (the digital seals that prove software really came from SAP) and stopped its automated builds. SAP has published no customer advisory, and its own statement says it sees no compromise of customer systems. **The one unknown:** which keys were replaced. If they were keys that seal software shipped to customers, banks and insurers that run SAP would have to re-check what they installed (the SolarWinds pattern); if they were internal keys, this is housekeeping. Sent to TERRY for a tradeability read. No escalation trigger fired and no score moved.

Session: PROME prome-80 C6 catch-up wake (Will 2026-11-27 17:59 ET). Boot 19:10 EST, memo 19:22 EST. Runtime Claude Code, Opus 5.5 (claude-opus-5-5). $0. Published statements only; no third-party system probed. Record: `AGENTS/CYPHER/research/2026-11-27_catch-up/RECORD.md`.

## Per-item verdicts

| # | Item | Verdict | Source and its date |
|---|---|---|---|
| 1 | SAP GitHub development environment | **Incident CONFIRMED** (SAP statement quoted by dpa) · SECONDARY. Key exchange and build halt **REPORTED only** (Handelsblatt, company circles). Customer-action advisory **NOT FOUND** | heise 2026-11-27 08:02 (SAP via dpa); news.sap.com read 11/27, no statement; SAP Security Notes November 2026 page read: 35 notes plus 4 GitHub advisories, all 11/10 Patch Day, no out-of-band note after 11/10, none on signing keys, certificates or download integrity; sap.com Trust Center 403 (stopped) |
| 2 | US Air Force Cloud One | **REPORTED only** | Reuters 2026-11-27 (unnamed sources, via search summaries); the Air Force "does not comment on ... specific networks and systems"; Leidos deferred; af.mil 403 and reuters.com refused (stopped) |
| 3 | UK DWP | **CONFIRMED at primary** · PRIMARY-VERIFIED | gov.uk "Temporary disruption to some DWP online services", 27 Nov 2026: "a cyber incident affecting our systems"; payments "not affected"; NCSC and the Government Cyber Coordination Centre; no restoration time; data access not stated |
| 4 | Lloyds Banking Group apps | **Outage CONFIRMED** in the bank's own words · SECONDARY. Cause NOT stated; cyber NOT established | The Register 2026-11-27 12:01 UTC (spokesperson quote; Bank of Scotland status page quote); Lloyds' own pages served an error page; restoration about 13:00-14:00 GMT is WALTER's read, not re-read |
| 5 | Allstate, day 5 | **REPORTED only** | WALTER's TechCrunch 11/25, CBS, Insurance Journal reads; allstatecorporation.com and allstate.com timed out twice |
| 6 | Officials' "no coordination" statements | **REPORTED** (oral answers as reported); WALTER's scope point **CONFIRMED by the dates** | homeland.house.gov 11/18 hearing page and Raia's written testimony (read): the testimony does not address the outages; the remarks (11/18, Clayton 11/22) predate FinCEN 11/24, SAP 11/26-27, Cloud One 11/27, DWP 11/26-27 |
| 7 | Optimizely "Reuters via Wikipedia" | No change: already CYB-INC-073, CONFIRMED at the vendor 11/17 | reuters.com refused the fetch tool |

## Assessment (by CYPHER's written rules)

- **WAVE-2026-10 (PHP2Shell):** nothing here states PHP. Row 8 (bank outage outside Japan) re-read for Lloyds: no PHP tie, NOT-FIRED (note 11/27). Other rows unchanged since 11/26. Stance MECHANICAL unchanged.
- **Scores:** none moved (25/40 raw, 16/40 adjusted). VX-05 stays 4 ORANGE; SAP would add a second independent root only if SAP states customer exposure.
- **Ledger:** five new incident rows 095 to 099. SAP reaches no chokepoint row (ERP is not mapped); no map change on a report with no customer impact stated.
- **Combination watch (WQ-622, logging moves no score):** KB-CYP-151 SAP (`combo:supplier-route-to-banks`), KB-CYP-152 Spiegel's agentic-AI claim (`combo:ai-tooling-entry`), KB-CYP-153 the outage cluster and the scope of the denials (untagged: the proposed `us-outage-cluster` theme still needs your C4 check).
- **N-able lead:** unchanged. Boot leg 10's N-able headlines (11/20-11/25) are the Mail Assure event already on CYB-INC-085 (KEV 11/23 adjudicated). RCA about 12/06; no financial victim named.
- **Docket:** new CATALYSTS row 2026-12-08 (SAP December Patch Day check).

## Forward view (SAP only; UNSCORED, no registered row)

About 70%: no customer-action advisory and no customer naming SAP as an entry route by Tue 12/08. Why: SAP's own statement says its evidence shows no downstream compromise of customer systems; swapping keys and halting builds is standard containment; the 2026 cases in this class (SAP npm packages in April, GitHub's internal-repository breach) ended in removal and rotation. About 30%: an out-of-band note revoking a certificate or asking customers to re-verify artifacts, the case where the vector vendor's shares take lasting damage (SolarWinds -17% day one, KB-CYP-003). Horizon 12/08, tail to month-end. What changes it: an SAP note on signing or integrity, a BSI/CISA/NCSC advisory naming SAP, a customer naming SAP artifacts. SAP ADR closed $213.65, +2.04% on 11/27 (fetch.py, read 19:17 ET): not priced as a tail.

## Inbox dispositions

| Item | Disposition |
|---|---|
| SIG-W-20261127-006 (read whole at BOARD; body identical to the inbox copy) | INTEGRATE: CYB-INC-095 to 099, row 8 note, KB-CYP-153; board_log row; filed with `git mv` |
| SIG-W-20261127-014 (read whole at BOARD) | INTEGRATE: CYB-INC-095, KB-CYP-151/152, catalyst 12/08, TERRY packet; board_log row; filed |
| `inbox/PROTOCOL.md` | Standing scaffold (the desk's inbox processing rules, 2026-10-23), not a packet; left in place |

Census (`inbox_census.py`): before, top-level 1 · WALTER 2; after, top-level 1 (PROTOCOL.md) · WALTER 0.

## Could not do

- Blocks, named and not bypassed: sap.com Trust Center 403 · af.mil 403 · bleepingcomputer.com 403 · reuters.com refused by the fetch tool. Allstate's two sites timed out; Lloyds' pages returned an error page. Spiegel, Handelsblatt and WiWo not read directly.
- Not worked (bounded brief; boot REVIEW): leg 5's nine 14-day re-checks (023, 024, 028, 029, 038 and four more) and leg 9's Elmet Group (ELMT) 8-K 8.01 of 11/24. Carried as STATUS resume item 1.
- No pull at boot: the tree carried WALTER's and PROME's uncommitted files (root Git Protocol: another owner's dirty files are a stop).
- Boot reads (bounded reader, each to `eof: true`): root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 3 · `AGENTS/CYPHER/CLAUDE.md` 4. Root `CLAUDE.md` was read whole from the harness injection; its four bounded pages were counted, not re-printed.

Commits: 83ee56c6de (desk files) · 42f49088d3 (TERRY packet) · 91030a9515 (NEXUS brief) · this memo's commit is in the SendMessage receipt.

## COMPLETION — CYPHER — 2026-11-27
STATUS: ✅ DONE (bounded catch-up; two boot REVIEW items carried, named above)
CHANGED: AGENTS/CYPHER/{STATUS.md, NEXUS_BRIEF.md, board_log.tsv, docket/CATALYSTS.tsv, workbook/INCIDENTS.tsv, workbook/KB.tsv, workbook/ESCALATION_WATCH.tsv, research/2026-11-27_catch-up/RECORD.md, archive/STATUS_ARCHIVE_2026-11-27.md}; AGENTS/TERRY/inbox/2026-11-27_from-CYPHER_sap-dev-environment-tradeability.md
RESULT: 2 cards drained (WALTER 2 -> 0); 7 items: DWP CONFIRMED at gov.uk, SAP incident and Lloyds outage CONFIRMED via company words (secondary), Cloud One, Allstate and the denials REPORTED; 5 incident rows (095-099), 3 KB rows, 1 catalyst (12/08); 0 rows fired, 0 scores moved
GAPS: which SAP keys were replaced is unstated by SAP; sap.com Trust Center, af.mil, bleepingcomputer 403 and reuters.com refused (not bypassed); Allstate sites timed out; leg 5 re-checks and Elmet 8-K not worked (bounded brief)
WILL_NEEDS: None.
FOLLOW-UP: TERRY tradeability read on SAP (packet 42f49088d3); CYPHER 12/08 SAP Patch Day check (CATALYSTS); C4 check on proposed theme us-outage-cluster (open since 11/26)
