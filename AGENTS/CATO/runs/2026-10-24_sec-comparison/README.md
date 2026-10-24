# Evidence-bearing SEC comparison — isolated example

This example prepares one recurring task: compare a standard earnings metric across two exact reporting periods. It reuses DEWEY's HTTP transport and returns evidence ready for a desk to interpret. It does not change DEWEY, launch agents, schedule collection or write shared state.

- [Readable example](comparison.md), generated directly from [the structured packet](comparison.json).
- [Raw SEC response](sec-response.json), retrieved October 24, 2026; the packet carries its SHA-256.
- [Existing-reader probe](reader-probe.json): a real producer excerpt demonstrates loss of period start and accession in the current function. The full response is preserved separately.
- [Program](prepare.py) and [author tests](test_prepare.py).

Run from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 AGENTS/CATO/runs/2026-10-24_sec-comparison/prepare.py \
  --snapshot AGENTS/CATO/runs/2026-10-24_sec-comparison/sec-response.json \
  --retrieved-at 2026-10-24T21:43:10.239847+00:00 \
  --cik 0000320193 --concept NetIncomeLoss --unit USD \
  --prior 2025-03-30 2025-06-28 --current 2026-03-29 2026-06-27 \
  --as-of 2026-10-24 --format markdown
```

Omit `--format markdown` for JSON. Omit both `--snapshot` and `--retrieved-at` to retrieve once through DEWEY's existing transport. The live path was tested successfully; the initial sandbox DNS failure returned an explicit unavailable result, then the approved outside-sandbox run succeeded. Output goes to stdout; retain JSON and the raw response when using the result as durable evidence. The prototype does not automatically persist a live response.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s AGENTS/CATO/runs/2026-10-24_sec-comparison -p test_prepare.py -v
```

**Selection:** exact period and unit; latest filing on or before the supplied cutoff. Thus a prior-year comparative may come from the current filing, intentionally and visibly. Conflicting latest records fail. Original-as-reported selection would be a distinct policy. Fiscal labels describe the filing and are retained as metadata; exact start/end dates drive selection. Period lengths must be within seven days, an explicit heuristic which catches quarter-versus-year-to-date confusion but does not prove comparability. No implicit quarter subtraction, currency conversion or alternative metric substitution.

**Limits:** author-tested prototype, not independently reviewed or integrated. Filing cutoff does not reconstruct the API at an earlier date. Standard entity-level US-GAAP duration facts only; custom tags, instant balance-sheet metrics, segment details and accounting changes require further source work. An operator-supplied retrieval timestamp is not independently verified evidence. This saved example was fetched in-session, and its live re-fetch returned the same response hash. The [SEC API documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) describes coverage and warns about differing reporting dates. No claim of measured time savings or better investment decisions.

**Next useful step:** review this packet for a real commissioned filing comparison; if selected for integration, move the additive evidence-preserving implementation into DEWEY's existing tool with owner review and compatibility checks. BROCK's bespoke PIK/nonaccrual comparisons may need custom tags or document extraction; this example does not claim to automate that work or alter the approved L833 trial.
