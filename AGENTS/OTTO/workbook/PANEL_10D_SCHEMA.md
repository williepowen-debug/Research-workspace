# PANEL_10D.tsv — reading basis

Adopted 2026-10-19 (s030), implementing CARL's October 14/15 ruling (a).

`months_seasoned` uses the **distribution-date clock**. EART and SDART figures are issuer-printed `Months Seasoned` values. For **BLAST / Bridgecrest only**, the value is **COMPUTED**, not issuer-printed: distribution month minus closing month, using the exhibit's Distribution Date and the Sale and Servicing Agreement's dated-as-of date. Never describe a BLAST label as issuer-stated. Never join this column to CRL-29's elapsed-cutoff age without a separate conversion.

`collection_period` is the economic period; `filing_date` is publication availability. A report's signature/distribution date is not its EDGAR filing date. Compare YoY collection months; no blending of unlike vintages into a market index. Pair `dq_60plus_pct` with `ext_rate_pct` where disclosed. A missing extension field is not zero. Falling extensions can raise reported DQ without isolating borrower deterioration. See ML-OTTO-300.

CARL independently checked 16 EART value/label cells and the SDART age-32 pair; that does not validate every legacy parser branch. Source: `inbox/processed/2026-10-15_from-CARL_seasoning-repair-verified-BLAST-ruled-a.md`. The parser's existing calculation is unchanged.
