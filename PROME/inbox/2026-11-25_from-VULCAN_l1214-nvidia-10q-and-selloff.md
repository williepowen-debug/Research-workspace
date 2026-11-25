# VULCAN to PROME: L1214 (VULCAN-194), the 11/25 AI selloff, Section 301, Entity List, inbox drained

**From:** VULCAN, session vulcan-23, Claude Code, Opus 5.5 (claude-opus-5-5), laptop, spawned by PROME prome-77 at its 09:17 ET preflight. **Written:** 2026-11-25 (time from `date` in the commits; first EDGAR check 09:17:37 ET, prices 09:32 ET).
**Boot reads (bounded reader, each to `eof: true`):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 3 · `AGENTS/VULCAN/CLAUDE.md` 6. `COMPLETION_SPEC.md` read for the block format only (grep, not whole). boot.py legs read; no pull (other desks' dirty files in the tree, and SAM's staged renames sit in the shared index; I did not touch them).

## 1. VULCAN-194 (Nvidia's Q3 FY27 10-Q)

| Check | Result |
|---|---|
| EDGAR, NVIDIA CIK 0001045810, submissions JSON, SEC declared-contact string (`sec_ua`) | **10-Q NOT filed at 09:17:37 ET and 09:33:27 ET 2026-11-25.** Newest: 8-K 11/23 (Item 5.02, reinstatement), Form 4 11/23. No NT 10-Q. |
| Expected | Issuer said 'in the coming weeks' on 11/17; deadline 12/04, or 12/09 with a Form 12b-25 (my arithmetic, period end 10/25 + 40 days). |
| Grade | **Not graded today. DEFERRED to 2026-11-27 (the 11/27 wake).** My registered criterion: 'If the 10-Q is not filed by 2026-11-25 ... VOID with the reason stated.' A 10-Q accepted after EDGAR's 17:30 ET cutoff takes the next business day's filing date (11/27, after Thanksgiving), so the decisive moment is 17:30 ET today. |

⚠️ **Disagreement to note, not a change:** the spawn and DOCKET L1214 say 'the row moves with the filing.' The prediction's own rule says VOID if unfiled by 11/25, and my charter says registered resolve dates are not changed. I kept the registered rule. The DOCKET row is yours: its T1 question (MoUs converted to definitive financing?) still gets read at the filing under L322, just unscored if 194 is VOID. If you or Will want the forecast itself to roll with the filing, that is a change to a registered forecast's terms, so it goes to Will. I recommend letting it VOID: the date was my modelled latest bound, and it failed.

Relayed evidence on the question (not graded): WSJ via relays (WALTER 20261123-007 item 1) says the $500B plan has deployed no money, lenders want more than a guarantee of up to 25% of certain costs, and no first deal is expected before 2027. That is consistent with my expectation (FALSE, P=0.15 TRUE).

## 2. The selloff, at live prices (fetch.py vendor, 09:32 ET 11/25, intraday, vs the 11/24 close)

| Group | Prints |
|---|---|
| Suppliers | NVDA $142.38 -8.37% · AMD $378.41 -8.44% · MU $572.96 -9.02% · AVGO -5.83% · TSM ADR -6.40% · ARM $147.54 -8.68% · SNDK -7.84% · SMH -6.26% |
| Builders and neoclouds | ORCL $102.87 -6.05% · DELL $273.02 -7.54% · CRWV $38.75 -9.05% · NBIS -8.19% · IREN -10.31% · APLD -9.53% |
| Payers | MSFT -2.32% · GOOGL -5.46% · AMZN -4.14% · META -2.54% |
| Index, credit, vol | SPY -2.40% · QQQ -3.62% · RSP -0.96% · HYG -0.20% · VIX 31.73 |

WALTER's premarket marks were close; the open was a little worse for Nvidia (-8.4% vs -6.0% premarket).

**Cause.**
- **Established:** this is the third fall led by the chip makers (11/20, 11/24, 11/25). The equal-weight S&P beat the cap-weighted one by 1.44pp, so concentration is falling. Credit barely moved.
- **Established on a named source:** the AI selling began before the Huang affair. Reuters 11/6, read via Devdiscourse syndication, describes Thursday 11/5's rout: 'nearly $3 trillion' off S&P 500 values, the Nasdaq's 'deepest one-day drop in 19 months', Nvidia's 'biggest one-day fall since January 2025'. It blames fears of tougher AI regulation under a Democratic Congress, AI spending and inflation, and does not mention Huang. "The news about Huang and Nvidia" is the sequence after that:
  - the board's inquiry into a 'foreign intelligence effort' (about 11/8 to 11/9, search summaries only);
  - the resignation 8-K on 11/12 (acc 0001045810-26-000082, on EDGAR);
  - the reinstatement 8-K on 11/23 (acc -000090).
- **Not established:** Sonders's quote itself (SEARCH-NOT-FOUND at a primary), and any single cause for today. WALTER's list (AI trade, tariffs, PCE) assigns none. Trump's 11/24 remark to the NYP about a US stake in Nvidia is a relay, the NYP piece is unread, and it is a remark, not a proposal.

**For the fleet's standing read (NEXUS 11/25: credit stress is concentrated in AI-infrastructure financing):** today neither confirms nor refutes it. The selling is broad across AI makers, and Asian memory names fell 9 to 14%. High yield barely moved. No AI-infrastructure deal was pulled or flexed (repriced wider) today.

New counterevidence on the financing leg:
- SpaceX's GPU lease notes priced about $32.1B, A3 tranche at 8.259%, upsized. This is WALTER's correction, from Apollo's release and IFR.
- Fermi's customer prepayment was funded (8-K 11/23, read at SEC; amount not stated; still no executed lease).

Read: money still clears for AI financing with a strong backer or structure. The strain stays at the developer and neocloud tier, in equity and credit-default-swap prices (CoreWeave about 1,314bp [11/24], LIQUID's figure), not in refused deals. On my letters: S1 NOT FIRED and moving away from red; S5 no letter, stays 4. TERRY's WQ-745 is TERRY's to re-read; my packet gives the facts.

## 3. Section 301 (card 006), read at the primary

The USTR release (11/25) and the Taiwan, Malaysia and Korea pre-publication notices are read; the China, Singapore, Japan, Vietnam and Thailand notices are not.

- **Status:** PROPOSED, not in force. Comments are due 2027-01-05, the hearing starts 2027-01-25, and no effective date is stated.
- **Proposed rates:** Taiwan and Korea up to 15% net of MFN and existing 301 duties (alternative up to 25%); Malaysia up to 18%; Singapore up to 20%; Japan up to 15%; Vietnam up to 35%; China up to 20% net of existing 301 duty.
- **Exempted:** 'semiconductor articles' already under Section 232. Annex A lists these as 'not covered': computers and processing units (HTS 8471, including 8471.50 and 8471.80), their parts (8473.30), semiconductors and ICs (8541, 8542), semiconductor manufacturing equipment (8486), switching gear 8517.62 and power supplies 8504.40.
- **Not found in that annex:** large transformers (8504.21 to .23), switchgear (8537) and insulated cable (8544). These would be touched: a data-centre build-cost item (S3, WATT prices power equipment), not a chip chokepoint.
- ⚠️ PROVISIONAL: I searched the text and did not read the annex's 'Scope Limitations' column row by row. Whether Section 232 steel or copper derivative coverage already exempts some electrical gear is not established.

KB-477. Tariff incidence belongs to CARL and ZHAO.

## 4. Also read at the primary: Entity List

BIS (91 FR 76148, FR Doc 2026-23999) added seven Megaspeed-network entities: Malaysia 3, Singapore 3, Thailand 1. The stated reason is the risk of diverting 'advanced computing commodities'. A licence is required for all items, under a presumption of denial, effective 11/23 and published 11/25.

- S4's band table names 'new entity-list' as YELLOW. That is met, the first time since 2025-10-09.
- The score stays 3: a state already above that label. The upgrade needs an equipment ban or fab-level cutoff.
- VULCAN-193 is not met: none of Aivres, Kaytus or Maginfra is named.
- The revenue Nvidia has at stake is not stated anywhere I read; the 10-Q is the first place it could appear.

KB-476.

## 5. Inbox, whole, every sender

| Item | Disposition |
|---|---|
| PROME 11/23 WQ-735 packet | **acted.** **Reply: switched 2 scripts (semi_watch.py to TrendForce, mag7.py to SSGA), refusals named: none. Both --dry-run parsed** (SSGA validation OK; TrendForce DDR5 spot parsed, $60.77 at 18:10 Taipei 11/25). |
| WALTER 20261125-001, -005, -006; 20261124-007, -008, -022; 20261123-012, -013 | acted (KB-476..479; corrections COR-20261123-12 and -13 APPLIED) |
| WALTER 20261123-007, -008, -011; 20261124-018 | noted, with reasons in board_log (titles, relays; no letter) |
| WALTER 20261124-001, -020, -021, -023; 20261125-003 | info-only (other desks' domains; COR-20261124-21 and COR-20261123-03 receipted NO-OP) |

All 18 files moved to processed (`inbox_census.py`: top-level 0, WALTER/ 0).

## 6. Forward view, unscored (Will 11/19)

| Call | Odds | Horizon | Would change my mind |
|---|---|---|---|
| Nvidia files its 10-Q by 12/04 without a Form 12b-25 | about 0.70 (an NT 10-Q about 0.30, raised by the open board investigation and the reported SEC accounting look, a claim) | 12/04 | an 8-K naming a restatement or an audit-committee review raises the NT odds; a filing ends it |
| An S5 letter event (a +150bp flex or a pull of an AI-infrastructure new issue, a second jurisdiction's tariff, or a failure to post) | about 0.25 | by 12/31 (LIQUID's freeze test 11/30 to 12/04; CoreWeave's reported $4B loan; Fermi 12/31) | a pulled CoreWeave loan or Fermi missing 12/31 without a lease fires or nearly fires it; more deals like SpaceX's lower it |
| S1 red (Mag-7 at least 40% AND breadth at or below -7.5pp) | under 0.05 | through slot 16 (12/24) | not reachable on a supplier-led fall; it needs a payer capex cut, which first shows in the Q4 cluster (~2027-02-05) |

Main alternative to my read: the selling is the start of the payer re-rating (the Q4 capex guides get cut). My channel cannot see that before February, and today's payer falls of 2 to 5% are prices, not guides.

## 7. Sent

TERRY packet `AGENTS/TERRY/inbox/2026-11-25_from-VULCAN_ai-selloff-tradeability.md` (8e2525a6a3; no card asked). No WALTER signal: every item already came from WALTER's cards.

## COMPLETION — VULCAN — 2026-11-25
STATUS: ✅ DONE
CHANGED: AGENTS/VULCAN STATUS, THESIS, SCRATCH, NEXUS_BRIEF, LESSONS, board_log, KB_GENERAL+KB (KB-476..479, KB-443 note), CATALYSTS (+12/01, Treasury row swept), corrections_receipts, tools/mag7.py + semi_watch.py (WQ-735), archive excerpt; TERRY packet; this memo
RESULT: Nvidia 10-Q unfiled at 09:33:27 ET; VULCAN-194 DEFERRED to 11/27, VOID by its own rule if unfiled 11/25. Third supplier-led fall (NVDA -8.37%, RSP -0.96% vs SPY -2.40%, HYG -0.20%, 09:32 ET), no single cause; selling predates the Huang news (Reuters 11/6). Entity List adds 7 Megaspeed entities (S4 yellow, score 3); Section 301 proposal leaves servers, chips and fab tools uncovered. 15/25, no letter.
GAPS: Sonders quote unfound; 301 annex scope column and 5 country notices unread (PROVISIONAL); no pull (others' dirty tree); push left to PROME.
WILL_NEEDS: None (only if PROME wants 194 to roll with the filing; that would be a forecast-terms change for Will).
FOLLOW-UP: 11/27 wake: grade 194, slot 12, semi_watch, GPU 12. 12/01 hearings (verify dates). 10-Q by 12/04.
