# CoreWeave (CRWV) — VULCAN research library

Organized 2026-10-20T14:06:11-04:00, at Will's request. This is the local entry point for CoreWeave financing, customer, capex and power-dependency research. It contains **86 source copies** and **6 focused ledger extracts**, including **36 VULCAN knowledge-base entries** (34 literal company matches plus two linked context/correction records). [Full source map](SOURCE_MAP.md) · [content-hash manifest](MANIFEST.json).

**Authority and freshness:** copies under `archive/` are FROZEN reference snapshots, not automatically updated mirrors. Their original research/data dates still apply. Check the original owner before using a market quote, trade card or changed ruling. Consolidation does not independently validate a claim. Historical instructions in copied packets/prompts are records, not new assignments or approvals.

## Read these first

1. **Corrected financing mechanism:** [DEWEY’s DDTL 4.0 correction](archive/documents/AGENTS/VULCAN/inbox/processed/2026-08-02_from-DEWEY_DR1-CORRECTION-ddtl4-mechanism.md). The earlier GPU-depreciation → automatic borrowing-base reduction claim was withdrawn. The filed cash-flow/power-cost provisions and their scope matter.
2. **Power-exposure correction:** [WATT’s withdrawn unhedged-power inference](archive/documents/AGENTS/VULCAN/inbox/processed/2026-10-15_from-WATT_KB047-hedge-inference-withdrawn-PJM-emergency-no-backup-gen.md). Do not assume a material unhedged share. Its backup-use negative is supported only through October13; October14 is UNKNOWN (VULCAN KB-231/KB-220 amendment).
3. **Company thesis and five falsifiers:** [VULCAN trade-thesis snapshot](archive/documents/AGENTS/VULCAN/TRADE.md) · [canonical original](../TRADE.md). This is a conditional company thesis, not an order or verified current position record.
4. **Capital structure and context:** [DEWEY July9 company research](archive/documents/AGENTS/DEWEY/output/2026-07-09_coreweave-neocloud-credit.md). Historical Q1 baseline; apply subsequent corrections and Q2 updates rather than treating July numbers as current.
5. **Latest captured credit-owner detail:** [LIQUID October19 sweep](archive/documents/AGENTS/LIQUID/research/2026-10-19_sweep/REPORT.md) · [canonical original](../../LIQUID/research/2026-10-19_sweep/REPORT.md). Distinguish dated HYG evaluations, observed DTCC cash upfronts and model-derived spread estimates.
6. **Trade construction:** [TERRY’s January put-spread card snapshot](archive/documents/AGENTS/TERRY/setups/CRWV_jan15-put-spread_relief-rally-fade_CONCEPT_2026-10-15.md) · [canonical original](../../TERRY/setups/CRWV_jan15-put-spread_relief-rally-fade_CONCEPT_2026-10-15.md). TERRY owns structure; Will decides. This captured card predates VULCAN’s B reconciliation, so use current owner records for the ruling and trigger state. Existing-position documents are historical records, not reminder instructions.

## Where to find the company detail

| Question | Local starting point | Original authority / caveat |
|---|---|---|
| Individual debt facilities and guarantees | [KB extract](archive/extracts/KB.tsv): KB-074, KB-075, KB-077; DEWEY research/correction above | Filed terms versus press OID/YTM must stay separate; recourse and non-recourse facilities are not interchangeable. |
| Interest, cash flow and capital expenditure | KB-076, KB-079 | Same-period, same-basis comparisons. Interest and net loss being similar does not prove interest alone caused the loss. Property/equipment purchases differ from total investing cash flow. |
| Customer concentration and backlog timing | KB-080 | Revenue concentration is not necessarily backlog concentration. Backlog is not cash or guaranteed profit; retain recognition timing and redactions. |
| Leases and power-dependent capacity | KB-078, KB-051; corrected WATT packet above | Executed-but-not-commenced leases differ from funded debt; unhedged exposure and firm rights require evidence. |
| Later financing and dilution | KB-169; dated company/source packets in the source map | Cheap convertible coupon is not a directly comparable new unsecured or secured borrowing rate. |
| Bond and CDS stress | KB-218, KB-238; LIQUID sweep/benchmark materials | Market source clocks, exact coupon/maturity, evaluation versus execution, and conversion-model limits travel with each figure. |
| Contract-return models and insider sales | WALTER October20 documents in the source map; KB-241/242 in the local KB extract | Stylized model arithmetic is not a measured company return. Tax/plan/proposed sales do not establish motive. KB-241 is explicitly included despite lacking a literal company-name match. |
| Direct QQQ weight and contribution | [October20 QQQ analysis snapshot](archive/documents/AGENTS/VULCAN/reports/2026-10-20_catchup/QQQ.md) | Dated issuer weight and approximate current-basket reconstruction; not total indirect AI exposure. |
| Filing history | [CRWV-only EDGAR extract](archive/extracts/EDGAR_SEEN.tsv) | Frozen filing index, not the filings themselves. `first_seen_utc` and `filed` are different clocks. |
| Rental-price observations | [CoreWeave vendor extract](archive/extracts/GPU_SERIES.tsv) | Dated panel observations; no new threshold or monitoring cadence created here. |

## Current state versus unfinished underwriting

At organization time, VULCAN's canonical score remains S5=4, composite15/25. Will selected and retained Volta reading B; a separate score proposal remains pending. The copied specialist documents can contain older unresolved A/B wording. Use [STATUS](../STATUS.md) and the [committed ruling](../outbox/2026-10-20_wq441-B-ruling-score-proposal.md) for that distinction.

This library improves recovery of existing evidence; it does not complete a reconciled current debt/maturity schedule, contract-level cash-versus-capex timing, project-versus-parent cash waterfall, or a validated company valuation. Those remain research questions. No scores, thresholds, forecasts or trade permissions changed while assembling the folder.

## Organization and upkeep

- `archive/documents/`: verbatim document copies, retaining original repository paths for provenance.
- `archive/data/`: dated supporting data snapshots from company-focused source paths.
- `archive/extracts/`: filtered, frozen VULCAN ledger records; the original ledgers remain canonical.
- `SOURCE_MAP.md`: local copy and original path side by side, plus owner-tool links.
- `MANIFEST.json`: source/copy hashes, capture time, byte size, original owner and whether the source differed from committed HEAD.

The copies retain original text and relative links; use the source map's original link if an embedded relative link lacks a copied target. No original document was moved or edited. Future authorized CoreWeave-specific research can be saved here and linked from the index; shared desk records and specialist tools keep their existing ownership. Any future snapshot refresh should be explicit and dated, preserving relevant correction history. No automatic refresh service was installed.
