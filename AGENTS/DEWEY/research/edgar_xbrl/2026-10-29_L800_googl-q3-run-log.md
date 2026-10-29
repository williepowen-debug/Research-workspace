# L834 / L800: Alphabet Q3 2026 compare run (2026-10-29 10:53–10:55 ET)

**Run by:** DEWEY main session (Claude Code, Opus 5.5, Will-launched boot) with `scripts/edgar_doc.py compare --save`, tool unchanged. **Consumer:** VULCAN (L800 funding-gap re-cut; concept list per `inbox/processed/2026-10-26_from-VULCAN_L834-concepts-confirmed.md`).
**Filing:** Alphabet 10-Q, accession `0001652044-26-000084`, report date 2026-09-30, filed 2026-10-29 (SEC submissions feed, read 2026-10-29 ~10:53 ET). The companyconcept API already carried it at that time.
**Windows:** nine-month, prior 2025-01-01→2025-09-30, current 2026-01-01→2026-09-30, cutoff 2026-10-29. Alphabet's cash-flow statement tags year-to-date windows only (same as META on 10/24), so **no three-month Q3 fact exists in the API; the tool performs no subtraction.**

| Concept (us-gaap) | Prior 9M 2025, USD M | Current 9M 2026, USD M | Saved packet (sha12) |
|---|---:|---:|---|
| NetCashProvidedByUsedInOperatingActivities | 112,311 | 127,149 | `373e8cadc221` |
| PaymentsToAcquirePropertyPlantAndEquipment | 63,596 | 131,953 | `baa3f1b8c8cb` |
| FinanceLeasePrincipalPayments | 394 | 1,950 | `ea67e6484343` |
| PaymentsForRepurchaseOfCommonStock | 39,810 | 0 | `657a7cb16c96` |
| PaymentsOfOrdinaryDividends | 7,513 | 8,167 | `0c2f46a4bfa4` |
| PaymentsOfDividends | FAILED: current 9M missing (tag used through Q1 2026 only) | | none |
| PaymentsOfDividendsCommonStock | FAILED: HTTP 404 (Alphabet does not use this tag) | | none |
| DividendsPreferredStockCash | FAILED: prior 9M missing (preferred first issued 2026) | | none |

Each saved folder is `research/edgar_xbrl/2026-10-29_0001652044_<concept>_USD/`. Four raw responses are byte-identical to the ones saved at ~10:00 ET for the Q2 replay (the API already carried the Q3 filing then; the morning run used cutoff 2026-10-22 on purpose). The new records here use cutoff 2026-10-29.

**Carried limits (the tool's five, verbatim in each packet):** the cutoff is not a historical API snapshot; same concept/unit does not establish accounting comparability; entity-level standard tags only; source statements not independently reconciled; the API carries a fact only after XBRL processing.

**Run-specific observations, not interpretation:**
1. **Tag switch on dividends.** Alphabet's Q3 10-Q moved its cash-flow dividend line from `PaymentsOfDividends` to `PaymentsOfOrdinaryDividends`; the prior-year 7,513 appears under both tags. Whether the 8,167 current figure includes preferred dividends is **not established here** — read the 10-Q cash-flow face before using it as common-only.
2. **Preferred dividend (this morning's flagged gap), facts from the same filing, not compare packets:** `DividendsPreferredStockCash` 234 (9M 2026 = Q3 2026); `DividendsPreferredStock` declared 384 (9M) / 298 (Q3); `PreferredStockDividendRatePercentage` 6.25%; 19,000,000 preferred shares at $1,000 liquidation preference; `ProceedsFromIssuanceOfConvertiblePreferredStock` 19,063 (9M 2026). Source: SEC companyfacts, accession `0001652044-26-000084`, read 2026-10-29 ~10:54 ET.
3. **Buybacks zero** in 9M 2026, consistent with the 10/22 base ("buybacks zero since Q4-25").
4. Both prior and current values come from today's filing (comparatives as presented, not as originally filed).
5. No values were derived, summed or interpreted here. Q3 three-month figures (9M minus H1 from `0001652044-26-000071`), TTM and funding-gap arithmetic stay with VULCAN, labelled derived.

**Still pending:** Amazon Q3 (reports after the close 10/29; 10-Q not in the submissions feed at 10:53 ET). Capital One Q3 10-Q also not yet filed (L567, separate leg).
