# CRL-29 / CARL-AUTO-OUTFLOW-01 — preparation, not grading

**October 12, 2026. Authority:** Will's instruction to verify and work PROME's recommendations. Existing August27 registration and October20 first-grade carrier remain unchanged.
**Stage:** Source/data preparation complete for the minimum panel. Grading specification needs clarification before a panel verdict. No forecast, threshold or grade changed.

## Prepared sources

Retrieved nine EX99.1 observations for three registered subprime trusts across two vintages. SEC submissions identify the trust CIK and filing, the human document index identifies the EX99.1, and the certificate itself verifies trust identity and collection dates. The wrapper is never substituted for the certificate.

| Trust / CIK | Contractual cutoff | Matched age 26 / 27 / 28 collection months | Primary cutoff evidence |
|---|---|---|---|
| AMCAR2024-1 /2020251 | April14,2024 | June / July / August2026 | [Underwriting agreement](https://www.sec.gov/Archives/edgar/data/1347185/000119312524146061/d774289dex11.htm), assets paragraph |
| AMCAR2023-2 /1987878 | August3,2023 | October / November / December2025 | [Underwriting agreement](https://www.sec.gov/Archives/edgar/data/1987878/000119312523235242/d459678dex11.htm), assets paragraph |
| EART2024-1 /2005087 | January7,2024 | March / April / May2026 | Retrieved certificate, Initial Purchase / Cutoff Date row |

The age anchor uses AMCAR2024-1's latest available August collection. Three ages supply a baseline and two consecutive changes. Ages are elapsed months from contractual cutoff; matching calendar dates would defeat the registered control. This age comparison does not eliminate calendar seasonality, underwriting or servicer differences. It is a small fixed panel, not a market index.

Evidence under `2026-10-12_followup/`:
- `auto-access.json`: accession/index/exhibit URLs, read times, bytes and hashes for 13 certificates plus the frozen control.
- `auto-extracted.tsv`: 13 source-verified observations, including the nine age-matched inputs and four recovered August EART certificates.
- `auto-age-match.tsv`: exact nine-row age/period/source join; no outcomes assigned.
- `auto-cutoffs.tsv`: cutoff dates and locators.
- `*-fields.txt`: field and column excerpts. Full HTML is retained locally under the existing repository ignore rule.
- `scripts/prepare_auto_outflow_extract.py`: offline extraction, hash/identity/period checks and source-backed selftest.

The earlier SEC403 failures are genuine historical observations. Current direct retrieval succeeds. All four September29 EART filings now have accessible August certificates, with collection dates read from the document. That clears the retrieval blocker; full V2 YoY/base/double-match/cure work remains for October14. No L4 cure grade is inferred from successful access.

## Extraction traps resolved

1. **Field numbers vary by trust.** AMCAR2024-1 uses loss115/extension127; AMCAR2023-2 uses loss113/extension125. Match the label/formula, preserve the actual reference. The registration's numbers are a worked-document locator, not interchangeable cells.
2. **AMCAR loss has Original / Previous / Current columns.** The current monthly loss is the final column; Original is zero. Reading the first number would manufacture zero loss. Source-backed checks independently pin August2026 current loss to $4,185,064 versus previous $3,883,159, not original zero.
3. **Normalize loss:** current net losses ÷ beginning pool ×12×100 yields annualized percent, as registered. Keep raw USD, denominator and monthly period. Do not compare raw-dollar runoff or cumulative losses to the0.77pp band.
4. **Seasoning labels differ.** EART2024-1's issuer labels are one above elapsed months from cutoff; AMCAR's transaction month matches elapsed age here. Both labels are retained; matching uses the registered cutoff basis.
5. **DQ percentage denominators differ.** AMCAR's published bucket percentages reproduce against beginning pool; Exeter's reproduce against ending pool. USD bucket balances and both pool balances are retained. Never silently pool those percentages.
6. **Prior date label repaired:** the4.57% extension/7.40% annualized-loss source in KB395 is June2026 collection, filed July31. The registration called it July; its frozen dispersion/thresholds are not recomputed here.

Frozen EART2022-3 CNL control reproduces27.58%. Every extracted61–90/91–120 percentage reproduces its disclosed denominator within printed rounding. The selftest checks differing field numbers, correct Current-column selection, rejection of a missing column, and period/hash mismatch refusal. A parser control does not replace the exhibit-resolution and identity checks.

## Grading blockers found in the existing letter

The preparation preserves the exact≥3 trusts /≥2 vintages, matched-cutoff-age,≥2 consecutive months,0.77pp loss and0.47pp extension bands, October20 first read and November HHDC recheck. It does not choose a favorable outcome.

| Unspecified or inconsistent item | Why it can change the verdict | Required review |
|---|---|---|
| “Stock down” does not name one bucket/denominator | The letter cites several DQ buckets; AMCAR/Exeter printed percentages use different denominators. Dollar runoff is also not a rate decline. | Pin the exact stock series and denominator before grading. Both published buckets and raw inputs are available. |
| No panel decision/aggregation rule | Three trusts can give different answers; no registered unanimity, majority, weighting or exemplar rule exists. | Pin a per-trust reporting and panel-decision rule; do not invent a mean or vote after observing results. |
| A and D overlap; the four bands are not an exhaustive partition | Synthetic example: stock down, loss+0.80pp, extensions+0.50pp satisfies bothA andD. Stock up/loss+0.80pp/extensions flat satisfies none. | Resolve precedence and uncovered cases. The explicit “both channels ambiguous” instruction argues against selectingA whenD also holds, but no new encoding is made here. |

These are specification issues, not source-access failures. No panel grade is issued now. Proposed interpretations or a revised letter return through PROME/Will; the registered row and frozen source-window evidence remain intact. RED receives this preparation/clarification packet because CHG-RED-049 is the originating challenge. WALTER receives source-access/measurement evidence for dedupe and owner routing.
