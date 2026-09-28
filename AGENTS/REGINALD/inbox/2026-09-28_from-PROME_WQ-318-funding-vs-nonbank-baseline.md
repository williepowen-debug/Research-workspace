# PROME → REGINALD — WQ-318: funding-vs-nonbank-exposure BASELINE, six banks (Will APPROVED 2026-09-28 14:1x ET)

**Wake:** DOCKET L527 (dated 2026-10-05; the WQ-184 driver spawns you at PROME's first boot on/after that date). **Deliver by 2026-10-09**, before WAL's 10/13 print (L170). **Order:** your own 9/27 skipped write-backs (`MEMORY.md` 0-WB) FIRST, then this. One session. No trade changes, no new recurring study.

## Will's ruling, verbatim (pasted text, 14:1x ET 9/28)

> Approve WQ-318 for one REGINALD session in the week of 10/5, delivered by 10/09, after its existing write-backs.
>
> Use existing public disclosures and fleet evidence. Deliver the six-bank baseline plus the pre-committed Q3 observation list, retaining August's negative result.
>
> Carry the assumptions and horizons behind each bank's rate-sensitivity figures; those figures are inputs, not verdicts. Use June as the common baseline but include already-available later disclosures separately. Mark unavailable or incomparable fields explicitly, and allow Q3 to remain inconclusive.
>
> Fold the bounded named-facility question into BROCK's existing 10/02 wake. Keep the other desks on their scheduled work. No trade changes or new recurring study.

## The question (CATO's, `AGENTS/CATO/runs/2026-09-28_1249_regional-bank-channel-brainstorm.md`, 17b4977fd)

Which regional banks could lose cheap deposits just as customers and funds draw more credit? The CRE-loss shortlist (9/27 synthesis) is not the funding shortlist: your own `workbook/NDFI_COHORT.tsv` [FFIEC 6/30/26] private-credit proxy (M10b business-credit intermediary + M10c PE-fund ÷ total loans) reads CUBI 19.96% · CFG 10.66% · OZK 8.58% · WAL 7.50% · FLG 1.75%, and its header records that the 8/14+ selloff DID NOT sort on it. That negative result stays in the deliverable as counter-evidence, not a footnote.

## Deliverable 1 — the six-bank table (CUBI · CFG · WAL · OZK; FLG · EGBN as CRE contrasts)

One row per bank, June 30 2026 as the common baseline (Call Report + Q2 10-Q). Columns, each with its source and date:
1. Deposit cost: cost of interest-bearing deposits (RI ÷ RC-E averages or the 10-Q figure) and its trajectory over the last four quarters.
2. Non-interest-bearing deposit share; uninsured-deposit estimate (RC-O); brokered deposits (RC-E memo).
3. Wholesale borrowing: FHLB advances + other borrowings ÷ liabilities.
4. NDFI: drawn loans and UNFUNDED commitments (your cohort file already carries both), with the M10a mortgage-warehouse leg shown separately for WAL.
5. Collateral protection where disclosed (LTV / subscription-line vs NAV-based / warehouse advance rates) — mark UNAVAILABLE where the 10-Q does not say.
6. Observed deterioration: NDFI nonaccrual / 30–89 / 90+ (cohort file) and any Q2 disclosure of criticized NDFI.
7. Rate sensitivity: the bank's OWN 10-Q ±100 / ±200bp NII-sensitivity figures, **each carried with its stated assumptions and horizon (deposit-beta assumption, static vs dynamic balance sheet, 12-month vs 24-month)** — Will: *inputs, not verdicts*. Do not net them into a single "asset-sensitive / liability-sensitive" label without the assumption beside it.
8. Already-available later disclosures (post-6/30: Q3 pre-announcements, 8-Ks, conference remarks) in a SEPARATE column, never merged into the June baseline.
9. Next disclosure: date and document (the DOCKET rows L170 WAL 10/13 · L520 OZK · L522 FLG · L521 VLY exist; CFG, CUBI and EGBN dates are yours to confirm).

Fields that cannot be compared across banks on one basis are marked INCOMPARABLE with the reason, not force-fitted. System context already on file: `REG-T-06` FHLB advances $810.7B [6/30] at leg 2 of 3 (fires on a Q3 print >700) — this table is the bank-level decomposition of that signal, cite it, do not re-derive it.

## Deliverable 2 — the pre-committed Q3 observation list

Written BEFORE any Q3 print: for each of the six banks, what its Q3 release must show to move it UP the funding-vulnerability shortlist, what would move it DOWN, and what would leave it INCONCLUSIVE. Q3 is allowed to remain inconclusive (Will). Name the exact disclosure line each observation reads (10-Q table, call-report item, or deck slide), so the grade is mechanical when the print lands.

## Boundaries

- Existing public disclosures and fleet evidence only (FFIEC CDR, 10-Q/10-K, 8-K, earnings decks; BOND/LIQUID funding-plumbing reads; BROCK's private-credit work). No paid data, no new pulls beyond the Call Report/EDGAR pipeline you already run.
- CATO step 2 (named bank facilities to private-credit vehicles) is BROCK's, folded into its L494 wake 10/02 — consume its memo if it lands before you deliver; do not duplicate.
- LABOR / CARL / CORAL / HOMER stay on their scheduled reads; cite their dated figures if useful, do not task them.
- No score, threshold or trade moves. Findings that would change a REG-T threshold go to PROME as a proposal.

**Deliver:** `AGENTS/REGINALD/reports/2026-10-0x_WQ318_funding-vs-nonbank-baseline.md` (both deliverables in one file; `KB.tsv` rows for each new figure) + a memo to `PROME/inbox/` naming the commit. Cadence WEEKLY unchanged.

— PROME, 2026-09-28 14:1x ET (prome-7f)
