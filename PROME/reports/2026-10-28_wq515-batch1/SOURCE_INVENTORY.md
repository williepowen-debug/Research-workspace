# WQ-515 batch 1: frozen source inventory

Written by the independent Sonnet reader before any BOARD card, handoff packet or owner record was opened. The only artifacts read before freezing: the DEWEY method, transfers.tsv, and the three source files named below. Source file hashes matched transfers.tsv (see REPORT.md section 1).

**Frozen at: 2026-10-28 20:41:47 EDT (2026-10-29T00:41:47Z)**

**Source limitation (applies to every row):** the frozen source artifacts are WALTER's bounded excerpts (SOURCE-CHECKS.md, EART-SOURCE-CHECK.md), each holding one qualifying quote plus locator, not the full issuer document. Findings and caveats below are inventoried only from those excerpts and their locators. The issuer pages were not re-fetched (they may have changed since dispatch). Any field the excerpt does not state is UNKNOWN. Severity weights: 0 = 0, 1 = 1, 2 = 2, 3 = 4.

Source files:
- M = AGENTS/WALTER/research/2026-10-26_morning/SOURCE-CHECKS.md (sha256 e63e3002...1b1e, captured 2026-10-26T16:46:43Z)
- U = AGENTS/WALTER/research/2026-10-26_unwind-search/SOURCE-CHECKS.md (sha256 72a6d245...b097)
- E = AGENTS/WALTER/research/2026-10-26_startup-recovery/EART-SOURCE-CHECK.md (sha256 1c2989c5...38c2)

## SIG-W-20261026-001 (M, section 001), owner BROCK, class contingent/current
- Finding: Meta issuer release of Oct 26 launching an offering of depositary shares (Series A mandatory convertible preferred) plus Class A common stock with forward-sale agreements. Scale and any larger program: UNKNOWN from excerpt.
- Evidence: Meta issuer press release, financing-plan paragraph and forward-sale terms (primary).
- C1 (sev 3, w 4): "has not entered into any agreement". A broader financing plan beyond the launched offering is not contracted. Decision that could change: treating an unexecuted program as committed capital (contingent to current).
- Confidence: UNKNOWN (unstated). Conditions: contingent on future agreements; horizon UNKNOWN. Implication: UNKNOWN beyond owner BROCK.

## SIG-W-20261026-002 (M, section 002), owner BROCK, class contingent/current
- Finding: SpaceX release announcing a $40 billion GPU financing (title); lease details UNKNOWN beyond locator "Transaction Details".
- Evidence: SpaceX issuer release (primary).
- C1 (sev 3, w 4): "Entry into the lease remains subject to certain specified closing conditions". Decision: counting $40B as closed or funded financing (contingent to current).
- Confidence: UNKNOWN. Conditions: closing conditions unspecified in excerpt. Implication: UNKNOWN.

## SIG-W-20261026-003 (M, section 003), owner VULCAN, class contingent/current
- Finding: AP report that Anthropic has made a public IPO filing; terms UNKNOWN beyond the excerpt.
- Evidence: AP secondary report (not the filing).
- C1 (sev 2, w 2): "The amount the company ultimately raises remains uncertain". Decision: sizing or valuation of the raise, and eligible access. Loss changes magnitude, not kind.
- Confidence: UNKNOWN. Conditions: IPO not completed. Implication: UNKNOWN.

## SIG-W-20261026-005 (M, section 005), owner LABOR, class contingent/current
- Finding: Microsoft blog introducing a voluntary exit offer, Oct 26.
- Evidence: Microsoft issuer blog, section "What employees should know" (primary).
- C1 (sev 3, w 4): "This is a time-limited, voluntary program". Decision: reading an opt-in offer as realized layoffs or headcount cuts (kind change; labor-market read).
- Confidence: UNKNOWN. Conditions: acceptance count and deadline not in excerpt. Implication: UNKNOWN.

## SIG-W-20261026-006 (M, section 006), owner BRENT, class contingent/current
- Finding: EQT joint release announcing an acquisition of Range Resources (title).
- Evidence: EQT/Range joint issuer release, Transaction Details (primary).
- C1 (sev 3, w 4): "subject to the receipt of required regulatory approvals and clearances". Decision: treating the combination as completed (combined supply, enterprise value).
- Confidence: UNKNOWN. Conditions: regulatory timing UNKNOWN. Implication: UNKNOWN.

## SIG-W-20261026-007 (M, section 007), owner FALCON, class contingent/current
- Finding: Iran says officials from Saudi Arabia, Turkey and Pakistan will visit Tehran for security talks (URL title); AFP/BSS via TBS.
- Evidence: single wire report relaying an Iranian statement (secondary).
- C1 (sev 2, w 2): "He did not specify when the meeting would take place". Decision: treating the meeting as scheduled or having occurred.
- C2 (sev 1, w 1): the report is an earlier one; a later AP report separately updates in-person status (locator). Decision: staleness of status.
- Confidence: UNKNOWN. Conditions: meeting date unspecified. Implication: UNKNOWN.

## SIG-W-20261026-009 (M, section 009), owner ISHM (also CARL), class inference/measurement
- Finding: Dallas Fed Texas Manufacturing Outlook Survey, October (URL), diffusion-index based.
- Evidence: Dallas Fed survey page, methodology (primary).
- C1 (sev 2, w 2): index is "subtracting the percentage of respondents reporting a decrease from the percentage reporting an increase". It measures net breadth of respondents, not level or magnitude of output. Decision: reading index values as magnitudes or national output.
- Confidence: UNKNOWN. Conditions: Texas respondents only (inferred from survey name; scope not in excerpt). Implication: UNKNOWN.

## SIG-W-20261026-010 (M, section 010), owner HANS, class inference/measurement
- Finding: Germany Ifo business climate, October, Capital Economics rapid response.
- Evidence: secondary analyst note; only the accessible lead was read.
- C1 (sev 2, w 2): "discrepancy between the weak hard data and stronger surveys". Survey improvement is not confirmed by hard data. Decision: treating the survey rise as real activity improvement.
- C2 (sev 1, w 1): full analysis is subscriber-only; only the lead was read (partial secondary source). Decision: confidence in the analyst's reasoning.
- Confidence: UNKNOWN. Conditions: UNKNOWN. Implication: UNKNOWN.

## SIG-W-20261026-012 (U), owner SAM (also LIQUID, HENRY), class inference/measurement
- Finding (LIQUID paragraph): the large Brazilian move is not accompanied by comparably large selling in sampled US credit ETFs or every sampled carry currency; carry currency moves mixed.
- Evidence: LIQUID report cross-market check (owner bytes hash d7e76dfe...); ETF prices and currency moves.
- C1 (sev 3, w 4): this "weakens a simple universal carry-unwind story at this time; it cannot identify or rule out specific yen-funded Brazil losses". Market direction does not identify causal unwinding (also stated in the WQ515 note). Decision: concluding that no carry unwind occurred, or that one did (inference to measurement).
- C2 (sev 2, w 2): ETF prices include duration, currency, distributions and market/NAV effects; HYG/LQD gains cannot prove OAS compression or open primary financing. Decision: credit-market access read.
- C3 (sev 2, w 2): EMB includes Brazil, so it is neither a clean ex-Brazil control nor independent contagion proof. Decision: contagion read.
- C4 (sev 2, w 2): "No synchronized BRL/JPY funding return or new carry probability is graded". Decision: recipient quoting a carry probability or funding return (share/probability).
- C5 (sev 1, w 1): SAM's latest consulted STATUS is dated Oct 20 and is not a peer confirmation of today. Decision: SAM's own view is not represented.
- Confidence: stated qualitatively ("at this time", weakens, not proves). Conditions: sampled instruments only, point-in-time. Implication: LIQUID's own conclusion that universal carry-unwind story is weakened.

## SIG-W-20261027-001 (E), owner CARL, class inference/measurement
- Finding: SEC 8-K (EART 2026-4) Item 1.01 defines August 31, 2026 as the closing date; underwriting agreement dated August 26; the August 28 footnote refers to a prior 8-K filing, not the closing. (Correction of an earlier date.)
- Evidence: SEC EDGAR 8-K and exhibit list (primary).
- C1 (sev 3, w 4): "The source is a completed historical transaction, not evidence of uninterrupted current financing access". Decision: using a closed Aug 31 deal as proof that the ABS market is currently open (historical to current).
- C2 (sev 1, w 1): the review resolves only the closing-date correction; the owner source packet (OTTO READOUT) stays pending for its separate pricing and Ally deltas. Decision: assuming the packet is otherwise verified.
- Confidence: UNKNOWN (stated as verified against primary). Conditions: historical. Implication: correct the date; owner CARL.

## Totals frozen
Caveats inventoried: 17 (sev 3: 6, w 4 each = 24; sev 2: 7, w 2 each = 14; sev 1: 4, w 1 each = 4; sev 0: none listed). Total weight 42. By transfer: 001:1, 002:1, 003:1, 005:1, 006:1, 007:2, 009:1, 010:2, 012:5, 2027-001:2.
