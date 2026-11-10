# RED → PROME: SoftBank working read challenged; CHG-RED-057 graded early (S62-b)

**Stamp:** 2026-11-10T17:47:52-05:00 (`date`). **Asked:** prome-07 at 17:40 ET, on Will's word at 17:18 ET. $0. No weight, band, threshold, gate letter or card moved: HOLD 72, net-bear 68.
**Record:** `AGENTS/RED/reports/2026-11-10_S62b_softbank_challenge_and_CHG057_grade.md` (every line keyed to a page or owner file). Arithmetic: `AGENTS/RED/reports/2026-11-10_S62b_sb_math.py`.
**Keys:** CHG-RED-057 (`workbook/CHALLENGES.tsv`), ML-RED-330, KB-RED-109, OUTBOX RED-TO-PROME-20261110-078.
**Read by RED at the primary (✔):** SoftBank earnings deck `1e69c9ec` pp.16–18, 23, 71, 79, 82, and accounting deck `2945557a` pp.7–8 (SAM's download, SHA prefixes match). Everything else is cited from SAM, VULCAN, LIQUID and BROCK, not re-read.

## Plain words for Will

SoftBank's numbers are right on its own ruler, but that ruler flatters it. Its leverage measure falls whenever it borrows against its shares, and in Q2 it did that for $12.4B to repay the bridge that funded OpenAI. The leverage figure the working read uses leaves out the $5.4B ABB purchase that SoftBank itself says is coming. Count it and leverage is about 24%. That puts the 25% line at an Arm price of about $166, 8% below 11/10's close. The credit market already prices SoftBank like a single-B company, not the BB+ it is rated.

None of this shows a default, a cancelled campus or a refused loan. It shows less room than "22.7%" suggests, and room that shrinks with each pledge used to make it.

## Verdicts

| Line | Verdict | Evidence (page or source) |
|---|---|---|
| R1 (RED's) "Mostly paper" | **WEAKENED** | The loss is mostly non-cash (SAM). SBG interest was ¥676.4B in H1, **+¥407.2B year on year** (acct p.7 ✔). Q2 interest paid was **¥0.3T in one quarter** (deck p.79 ✔). The cash policy covers bond redemptions only (deck p.23 ✔): ¥5.0T vs ¥1.6T. At the Q2 pace, two years of interest (≈¥2.4T) plus redemptions uses ≈¥4.0T of it |
| 1 = R2: does the LTV hide what a creditor counts? | **WEAKENED** (the numbers hold; the comfort does not) | Margin loans and the Intel and T-Mobile collars are deducted from net debt and netted out of value (deck p.82 items f–i ✔). Q2 "asset monetization" of **¥2.1T** = Intel collar ¥1.2T + Arm margin loan +¥0.8T (deck p.79 ✔). It lowered SoftBank's ratio (about −2.1 points, SAM) and moved $12.4B of claims ahead of the bondholders. Gross creditor view (RED arithmetic): **30.6%** rolled, 31.8% with hybrids at full debt. Steelman: those loans are non-recourse to SBG, and item (j) counts the SVF2 loan in full. The SVF2 loan's cash collateral triggers on a fall in OpenAI's unlisted mark (SAM stack, FILING) |
| R3 (RED's) The headroom leaves out disclosed items | **WEAKENED** | Rolled 22.66% (Arm $145 for 25%) → 22.90% with the settlement (Arm $149) → **24.05% with ABB $5.4B "Q3 onwards" (Arm $166, −8.3%)**. Another $10B debt-funded check would take it to **26.1%**. SVF listed marks since 9/30 are not re-marked even in SoftBank's pro forma (SAM) |
| 2: what CDS 497 knows | **WEAKENED** | At 40% recovery, 497bp ≈ 8.3% a year, ≈34% five-year default, risk-neutral (August 347 ≈ 25%). That is single-B pricing on BB+. CDS references the senior unsecured claim that Q2's secured borrowing pushed back in line. LIQUID's caveat: a US-nexus DTCC sample, ±10bp, before the results |
| 3: deposits, commitments, AEP collateral | **HOLDS on liquidity; WEAKENED on the cushion's definition** | The $6.6B is already paid: an asset at risk, not a cash call. Known calls: ¥140.2B settlement, ABB, the $1.5B unfunded SB Energy commitment, and interest. AEP's "fully collateralize" sits with the campus-side customer, non-recourse to SBG, unless SBG funds SB Energy while the IPO is postponed. SB7's forward commitments are the binding unknown |
| 4: "completely unrelated to PORTS-Pike" | **WEAKENED** | The red box is only on accounting deck p.8 ✔. Earnings deck p.16 and p.18 ✔ head the **whole** $9.5B, including the $2.9B loss, "Advance payments related to PORTS-Pike power generation project and others". The earlier Investor Briefing version said the realignment included "PORTS-Pike power generation project in Ohio" (VULCAN reader). "Not a cancelled campus" HOLDS on every outside record |
| 5: "SoftBank-specific" | **WEAKENED** | Specific in credit 11/6–11/9 (LIQUID). On 11/10 the equity cohort fell as much or more: NVDA −5.47%, IREN −7.85%, NBIS −5.27% vs SFTBY −4.00% (vendor; cause not attributed). NVIDIA guarantees up to $105B of the campus rent. About 70% of SoftBank's rolled holdings value is Arm (net) plus OpenAI: specific in who strains first, not in cause. Against: CoreWeave raised its capex floor and its CDS tightened |
| "No financing has been refused" | **HOLDS on the letter** | Banks refused shares-only terms on the OpenAI loan in July (Reuters relay via SAM). It was funded with an SBG guarantee: pickier, not refused |
| "Re-plan, not a default, not a cancelled campus" | **HOLDS** | SAM and VULCAN at the primaries; the GE Vernova and MHI books show nothing lost |

**Single strongest counter-case:** SoftBank's danger isn't the paper loss. It is a cash interest bill that more than doubled, paid for by pledging the assets that make its leverage ratio look safe. Disclosed commitments alone take it to about 24%. A 10% fall in both Arm and the OpenAI mark breaches its own 25% ceiling (26.0%, RED arithmetic), and credit already prices it a rung or two below its rating.

## Dated observations that decide it

| When (ET) | Watch | Working read is wrong if |
|---|---|---|
| Tonight about 20:15 | DTCC 11/10 CDS (LIQUID) | Above 513, with Oracle and CoreWeave flat |
| 11/10 19:00 → 11/11 01:30 | Tokyo session on the results (SAM) | 9984.T closes below ¥3,400 on volume above 64.8M |
| Any day | Arm close | Below $166 (24.05% case hits 25%); below $145 (SoftBank's own basis) |
| 11/11 → | TDnet | Any new share-backed loan or collar, or an Arm, SoftBank Corp or T-Mobile sale, to defend 25% |
| Any day | OpenAI round or tender | Priced under SoftBank's carried mark (the SVF2 loan's collateral trigger) |
| 11/11 Tokyo hours | JCR or S&P (LIQUID) | JCR below A, or S&P back to Negative |
| ~11/11 | Siemens Energy FY (VULCAN) | A US developer settlement or cancellation line |
| ~11/19 | NVIDIA 10-Q (VULCAN) | SB Energy guarantee reduced or phases re-dated |
| 11/19 | ING loan auction (LIQUID, BROCK) | Pulled, or clears well under par |
| When posted | SoftBank call transcript (SAM) | Gotō on Ohio matches "procure power externally" |
| Any day | EDGAR | SB Energy S-1 withdrawn |

## CHG-RED-057, graded under its own letter (tree `AGENTS/RED/research/2026-11-10_AI_FUNDING_TEST_TREE.md`)

- **SoftBank branch:** the SVF2 loan sits inside the ratio (deck p.82 item j ✔).
  - **Attack 6 goes from FAILED (11/06) to SUCCEEDS ON CAPACITY, not on cause:** 24.05% with ABB and the settlement, and one more $10B debt-funded check breaches 25%.
  - **Attack 4 nets to 0:** +1 for the Intel collar ($7.4B secured, first read at this print); −1 for the $11.9B senior term loan, which is not asset-backed (deck p.79 ✔).
- **CoreWeave branch:** FY2026 capex is $37–39B with the low end raised, "deliver sooner" (8-K Ex 99.1 via VULCAN-191 MISS). DDTL 5.5 ($2.6B) closed; an ATM covers up to 35M shares. **Not the STRONG branch.**
- **RED-31:** Microsoft was not named at this print (per VULCAN). BROCK card 004: a Microsoft cut is not a default on IREN's GPU loan. **Stays OPEN.**
- **Grade: MODERATE, unchanged.**
  - Not-failing holds.
  - "Pickier" gets its first filed developer-side cancellation (SB7's $2.9B), which is also how a squeeze starts.
  - "Rather than" still has no falsifier.
- **Re-review 2026-11-19.**

## Contradiction routed

LIQUID's packet says "S&P BB+/Negative since 3/3" (relay). SoftBank's deck p.71 ✔ says "S&P BB+ Outlook: Negative → Stable (Jul 16)", which agrees with SAM. A packet went to LIQUID's inbox; RED edits nothing of LIQUID's.

**ACTION for PROME:** none asked. RED holds the window.
**Priority:** 🟠

— RED, self-authored, carve-out ①
