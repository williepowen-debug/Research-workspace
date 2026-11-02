# DEWEY -> VULCAN: Amazon Q3 2026 compare packets saved (L834 / L800)
**Date:** 2026-11-02 09:0x ET | **State:** NEW | **Row:** D:L834 / D:L800

- **Pointer:** `AGENTS/DEWEY/research/edgar_xbrl/2026-11-02_L800_amzn-q3-run-log.md` (table + limits + face reads); packets under `research/edgar_xbrl/2026-11-02_0001018724_*`. Filing: 10-Q acc `0001018724-26-000040`, filed 2026-10-30.
- **Amazon tags THREE-MONTH cash-flow facts** (unlike META/GOOGL): Q3 rows are reported, no subtraction needed.
- **USD M, 2026 vs 2025 [PRIMARY, XBRL]:** OCF Q3 42,422 vs 35,525 · 9M 113,841 vs 85,055 · purchases of P&E (`PaymentsToAcquireProductiveAssets`, the untested tag: carries both windows) Q3 77,259 vs 35,095 · 9M 175,670 vs 92,297 · finance-lease principal Q3 433 vs 351 · 9M 1,296 vs 1,172.
- **Refused by the tool (no proxy):** `PaymentsToAcquirePropertyPlantAndEquipment` and `PaymentsForRepurchaseOfCommonStock` (prior 9M missing); both dividend tags 404. The cash-flow face carries no repurchase and no dividend line (document read, not a packet).
- ⚠️ **Two face lines outside the confirmed list, not packets:** "Proceeds from property and equipment sales and incentives" Q3 1,381 vs 867, 9M 3,482 vs 2,446; "Principal repayments of financing obligations" Q3 107 vs 82, 9M 281 vs 276. Gross vs net capex and whether financing obligations count are your call.
- **ACTION (yours):** L800 arithmetic, labelled derived. With this leg all five Q3 legs are pulled; COF stays at L567.
