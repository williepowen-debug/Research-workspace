# VULCAN → PROME: delivery 1, WALTER card SIG-W-20261117-007 (BIS chip rule), read at primaries; HOLD for the print

**Session:** prome-19 assignment, Claude Code, Opus 5.5 (claude-opus-5-5); session id not exposed. Booted from the Git root: root CLAUDE.md, AGENTS.md, USER.md, desk CLAUDE.md read; no desk AGENTS.md. boot.py: none due; the push of 11/16's commits has landed (leg 10); carried EDGAR model FAILs only. Not pulled, not pushed (your instruction).

## 1. What the rule is (primary)

Federal Register public inspection, FR Doc 2026-23529, "Addressing Remote Access to Advanced Semiconductors", interim final rule, filed 2026-11-16 16:15 ET, **publishes and takes effect 2026-11-19**; comments due 60 days after (2027-01-18). Read whole for these points (copy and sha256 in my reports folder):

| Leg | Scope | Licence policy |
|---|---|---|
| Data centers anywhere (new § 744.24) | chips to a data center giving more than 12,000,000 aggregate TPP to companies headquartered in China, Macau or other D:5 destinations; existing service needs a licence within 90 days (to 2027-02-17); recommender systems excluded | case-by-case |
| Five countries (§ 742.6) | Indonesia, Malaysia, Singapore, Thailand, Brazil; US-headquartered buyers exempt if the exporter files monthly § 743.10 reports | case-by-case, on each country's enforcement |
| Foundries and packagers | fewer ways round the presumption for chip designers in licensed destinations | — |
| AI Diffusion Rule | formally rescinded ("never been enforced") | — |

Savings clause: en-route shipments may complete within 30 days (to 2026-12-19). Chips covered: ECCN 3A090 (except .c), 4A090 and the .z items. No Entity List additions, no equipment ban, no fab cutoff; Nvidia is not named. The rule's preamble itself says an entity is served "on behalf of" when it is "the exclusive or primary (greater than 50 percent of total compute) remote end user" (a reading of the existing § 744.23 control).

**Nvidia's own statements:** no 8-K since 11/12 (EDGAR 12:02 ET). One newsroom release on 11/17, which creates a board National Security and Export Control Oversight Committee (chair Suzanne Nora Johnson; meets at least quarterly) and names no customer, country, rule, revenue or outlook. No on-record comment to CNBC.

**The 50% claim: CLAIM ONLY.** CNBC (11/17, two unnamed sources) says Nvidia "would not sell" to customers renting more than 50% of their GPUs to Chinese companies, "for now", and warned buyers about the PROPOSED Remote Access Security Act. The FT has 51%, for future contracts. Nvidia has not confirmed either. "Nvidia stopped selling" is **NOT ESTABLISHED**.

## 2. Against my written rules

- **What moved:** nothing. Composite 15/25 (S1 3 · S2 2 · S3 3 · S4 3 · S5 4); fired count 1 of 5; no prediction resolved.
- **S4:** the bands are yellow for an Entity List addition, orange for an equipment ban and red for a fab cutoff. The rule is none of these: it is a chip and data-center licence, and the band table has no row for that. I invented none. S4 stays 3. The kill condition (controls net loosen for two quarters) moves further from being met. What would move S4: an equipment ban, a fab cutoff or Taiwan kinetic action, which are unchanged.
- **S1 safety/demand sub-read: NOT FIRED.** It was registered on 9/29 as the AI-safety branch ("an ENACTED safety law reaches a compute contract"). This rule is a national-security export control, and it takes effect only on 11/19. ⚠️ STATUS's shorter wording, "an ENACTED law or rule that caps or licenses frontier training compute", could be read literally to include it. I have recorded that alternative reading. Widening the branch to cover export controls would be Will's decision, not mine. I am not asking for it.
- **S1, S5 and VULCAN-17, -189, -190, -192:** untouched. US-headquartered buyers are exempt, and the rule contains no payer capex figure. A rule is none of VULCAN-192's legs (a), (b) or (c). NVDA's fall lowers the Mag-7 weight, which is graded at slot 11 on 11/20.
- **Tonight's release:** the quarter ended 10/25, before the rule; the Q4 outlook spans its first weeks. My 11/17 CATALYSTS statement stays exactly as committed. Any outlook or CFO wording on the rule, the five countries, remote access or China will be quoted under its existing items (a) and (c). ⚠️ Silence on the rule is not evidence that it has no effect, and I will not grade it as such.

## 3. Routing

- **ZHAO:** packet with the rule's primary facts and its clocks (11/19, 12/19, 2027-01-18, 2027-02-17). China's response and those clocks are ZHAO's; I have not graded MOFCOM's statement. No HAWK packet: there is no Taiwan geopolitical or kinetic content, and the foundry leg's semiconductor consequence is mine.
- **TERRY:** tradeability packet (WQ-696 form). Size unknown; the exemption covers the largest buyers; on its own it supports no investment implication before tonight. It is context for T1. The post-print packet follows.

## Inbox drained (5 of 5, WALTER lane; general inbox 0)

| Card | Disposition |
|---|---|
| 20261117-007 | acted: KB-446/447, packets |
| 20261117-006 | noted: Nvidia titles consumed; TrendForce reports NAND spot −20% in two weeks (titles), a lead, not the contract letter; HSBC loan and Firmus logged; KB-448 |
| 20261117-009 | noted: HSBC's roughly $300M loan piece sold in the mid-80s is a secondary sale, not a new-issue flex or pull; Jupiter identity INFERRED; KB-448 |
| 20261116-012 | noted: Altman relay logged to the ai-demand theme, KB-448 |
| 20261117-008 | skipped: cyber, CYPHER's |

Neighbour rows (boot leg 6): CYPHER's 11/18 row 9 is HENRY's grade on cyber names, so no VULCAN letter. ZHAO's 11/18 BIS re-check is ZHAO's look; it publishes to me on an Entity List package, and today's rule is not one. Neither was registered.

## Forecast scorer (your 78994ce38a)

- **Layout:** `AGENTS/VULCAN/archive/PREDICTIONS_RESOLVED_2026-09.tsv`, `-10.tsv` and `-11.tsv` are the only resolved-forecast files. Each sits beside a `.README.md` that the `.tsv` pattern correctly skips. All three carry the live ledger's 11-column header (id … resolution), with no CRLF line endings.
- **Rotations:** each month's resolved rows have gone to a new `PREDICTIONS_RESOLVED_<YYYY-MM>.tsv` with the same columns. That is my standing practice, not a written rule; I will tell you before changing it.
- **My count today: 16 resolved rows** (8 + 4 + 4), matching STATUS (16 resolved, 6 open in `workbook/PREDICTIONS.tsv`). **Your record says 19.** 16 plus the three header lines is 19, so the 19 may be a line count; please check that the tool's own count is 16.
- **Do not glob this file:** `MEMORY_CYCLE/S2_PREDICTIONS.tsv` mirrors five already-archived IDs (VULCAN-02, -04, -11, -12, -16) with a 12th column `source_file`. It is a view, not a ledger.

## COMPLETION — VULCAN — 2026-11-17 (delivery 1)
STATUS: ✅ DONE (delivery 1; holding for delivery 2)
CHANGED: AGENTS/VULCAN/{workbook/KB_GENERAL.tsv, workbook/KB.tsv, STATUS.md, THESIS.md, board_log.tsv, SCRATCH.md, archive/STATUS_EXCERPTS_2026-11-17.md, reports/2026-11-17_bis-remote-access/README.md + sources PDF, inbox/WALTER/* → processed}; AGENTS/ZHAO/inbox/2026-11-17_from-VULCAN_bis-remote-access-rule-primary.md; AGENTS/TERRY/inbox/2026-11-17_from-VULCAN_bis-chip-rule-before-nvda-print.md; this memo
RESULT: Rule read at the Federal Register primary (FR 2026-23529, effective 11/19, four legs, 12,000,000 aggregate TPP line, five countries, US-headquartered exemption); Nvidia's only statement is a committee release; 50% claim CLAIM ONLY. 0 scores, bands, gates or predictions moved (15/25); 3 KB rows (446-448); 5 of 5 cards dispositioned; scorer count 16, not 19.
GAPS: The Megaspeed joint statement was not re-read (WALTER read it whole; no letter keys on it). The Tom's Hardware body was unreachable, which does not matter because CNBC was read. STATUS is at 90% of its read budget, and rotation is owed at closeout.
WILL_NEEDS: None.
FOLLOW-UP: HOLD; delivery 2 after the 8-K Item 2.02 lands (about 16:20 ET): statement row, TERRY packet, PROME packet.
