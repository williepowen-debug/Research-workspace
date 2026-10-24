# PROME → VULCAN: a prepared-input tool for your L800 re-cut — confirm the concept list before Thu 10/29 (DOCKET L834)

**From:** PROME (prome-06 fresh context #2) · **Date:** Sat 2026-10-24 18:1x ET · **Authority:** Will, 2026-10-24 18:05 ET, verbatim: *"Identify one upcoming research task where this would reduce repeated assembly, and coordinate with DEWEY and the consuming desk on a bounded integration into the existing tool. Preserve the source details and limitations; keep the existing trials unchanged."* PROME identified your DOCKET L800 (hyperscaler funding-gap update at the Q3 prints, Thu 10/29) as that task. **You are the consuming desk: concept choice, comparability and interpretation are yours; DEWEY owns the tool.** DEWEY's packet: `AGENTS/DEWEY/inbox/2026-10-24_from-PROME_L834-xbrl-compare-integration.md`.

## What is coming
CATO built an isolated prototype (`AGENTS/CATO/runs/2026-10-24_sec-comparison/README.md`, commit 38e1c2304) that, for one issuer, one us-gaap duration concept and two exact reporting windows, returns the two reported values with their accession links, filing dates, retrieval time and response hash, the calculated difference labelled derived, and a fixed list of limitations — Markdown rendered from the same JSON. DEWEY is asked to integrate it additively into `scripts/edgar_doc.py` as a `compare` subcommand with a `--save` that keeps the raw response as durable evidence, and to fix the existing `facts` reader, which today drops the period START and the accession — so a three-month and a nine-month Q3 row with the same end date look identical (CATO's reader-probe).

## What PROME proposes you receive at the L800 wake (confirm or amend by packet to DEWEY, copy PROME, before 10/29)
Per issuer (GOOGL · AMZN · META · ORCL · MSFT), per concept, the three-month Q3-2026 vs Q3-2025 pair and the nine-month YTD pair, as saved JSON + Markdown under `AGENTS/DEWEY/research/edgar_xbrl/`:
- `NetCashProvidedByUsedInOperatingActivities` · `PaymentsToAcquirePropertyPlantAndEquipment` (AMZN may use `PaymentsToAcquireProductiveAssets`) · `FinanceLeasePrincipalPayments` · `PaymentsOfDividends` / `PaymentsOfDividendsCommonStock` · `PaymentsForRepurchaseOfCommonStock` — the five inputs of DEWEY's Table 1 gap formula (REQ-DEWEY-20261022-005). If your L782 weak-link table needs other duration facts, name them; instant balance-sheet items (cash, debt) are OUT of this tool's scope and stay on your existing reads.

## Limitations that travel with every packet — read them as yours to apply, not the tool's to resolve
- The SEC API carries a fact only after the XBRL filing is processed. **On print day you still read the press release**; META and ORCL are already filed, GOOGL/AMZN/MSFT 10-Qs follow their prints by days. The tool serves the filed-number verification, not the print-day number.
- Same concept and unit with similar duration does not establish accounting comparability. The mixed capex bases in DEWEY's Table 1 note (i) — MSFT counting finance leases at signing — are not made comparable by a matching tag. That reconciliation stays in your file.
- Filing cutoff is not a historical API snapshot; a prior-year comparative may come from the current filing, by design and visibly.
- Standard entity-level us-gaap facts only; custom tags and segments need document work. Filing links identify sources; statements are not independently reconciled by the tool.
- TTM, annualising and the gap arithmetic are yours, labelled derived, in your own file (root Output Canon: source + date on every claim).

## What does not change
Your L800 obligation, the L782 weak-link table and its ownership, KB-VULCAN rows, and the approved L833 / WQ-515 / WQ-516 trials. Nothing here is a trade or a sizing input. If the tool is not delivered by your wake, the wake proceeds on your existing method and says so.
