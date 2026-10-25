# Reproduce the June 30 comparison

Run from the repository root with Python 3. Dependencies are Python's standard library; the extractor imports `rows.py` and `soi.py` from the existing BROCK October 23 software project. It does not import or invoke the old `metrics.py`/`cross.py` writers.

Download the six filing HTML bodies linked in REPORT.md and their SEC extracted XBRL instances. The instance is in each accession directory with the HTML stem plus `_htm.xml`. Examples: `arcc-20260630_htm.xml`, `fsk-20260630_htm.xml`. Match the committed SHA-256 hashes before treating a reproduced result as this source version.

Create an input JSON object with keys ARCC, BXSL, FSK, GBDC, HTGC, OBDC; each value has `html` and `xml` filesystem paths. Paths may point anywhere readable. For example:

```json
{"ARCC":{"html":"/tmp/filings/arcc-20260630.htm","xml":"/tmp/filings/arcc-20260630_htm.xml"}}
```

Supply all six keys, then run:

```sh
.venv/bin/python3 AGENTS/BROCK/research/2026-10-25_three-followups/compare.py --inputs /tmp/inputs.json --out /tmp/brock-reproduced
```

The program asserts all six investment FV reconciliations against issuer totals, fails if they do not tie, and writes source-context positions, currency-separated summaries, borrower candidates and narrower disclosed-term candidates. For the original run, input HTML/XML files were under `/tmp/brock-followup-20261025` and `/tmp/brock-20261025-primary`; those temporary locations are not required by the program. The committed `positions.csv` is the compact durable position table. Full HTML row text for reviewed comparisons and named examples is preserved in `review_rows.json`.

Matching is a conservative research screen, not legal instrument certification. Rate families are coarser than reset conventions and maturity is month-level. Unmatched candidates do not prove different instruments; matched candidates do not prove identical rights. HTGC aliases are a separate manual source review in REPORT.md. `liquidity_scenarios.json` contains arithmetic assumptions, not observed October liquidity or forecast probabilities. No original forecast expectations or thresholds are generated or replaced by this script.
