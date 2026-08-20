---
name: finding_subtotal_column_in_a_flattened_table_triple_counts
description: An API that flattens a printed table can carry SUBTOTALS in a per-row column; summing it silently over-counts, and the only tell is a total that does not reconcile
metadata:
  type: reference
---

Treasury's Fiscal Data API (`v1/debt/mspd/mspd_table_3_market`) returns one row per security with an `outstanding_amt` field. **It is not a per-security value.** The MSPD is a *printed table*, and the API preserves its layout: the Outstanding column is populated on the rows where the paper report printed a **subtotal**. Summing `outstanding_amt` across security rows gives **$91.6T** against a stated Total Marketable of **$31.455T** — a ~3× over-count that produces entirely plausible-looking numbers.

**What actually works:** `issued_amt + redeemed_amt + inflation_adj_amt` (redeemed is negative in this feed). That reconciles to the feed's own `Total Marketable` row within **0.012%**, the residual being the maturity-less Federal Financing Bank line.

**Why this generalizes past Treasury:** any API that is a thin wrapper over a *published report* rather than a normalized database can carry this shape — subtotal rows, running balances, section headers, and footnote rows sharing a schema with the data rows. Row count alone never reveals it. `[[finding_ragged_row_tolerance_hides_schema_change]]` is the sibling on the write side.

**How to apply:**
1. **Never sum a column before reconciling it to a stated total** that the source itself publishes. The over-count here was 3× and every individual value looked reasonable.
2. **Prefer a component construction over a convenience column** when the source gives both — components are per-row by construction; a summary column may not be.
3. **Validate against a DIFFERENT primary, not just internal consistency.** The construction above was confirmed by matching the August QRA/TBAC deck's independently stated "$7.0 trillion" bills outstanding and "22.2%" bills share to the decimal. Internal reconciliation proves arithmetic; a second primary proves meaning. `[[finding_crosscheck_with_free_parameter_validates_nothing]]`
4. **State the perimeter in the delivery** — total marketable vs privately-held (SOMA in or out) moves the answer, and a recipient benchmarking against the other one will read a real difference as an error.

*(Found 2026-08-19 computing Treasury WAM from the MSPD primary, 2001→2026, to test a relayed "WAM is near multi-decade highs" claim.)*
