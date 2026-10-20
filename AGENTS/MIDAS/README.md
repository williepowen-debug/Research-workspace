# MIDAS metals research directory

Find research and data by metal. These folders are topic indexes and the filing homes for new work; current desk judgments remain in [STATUS.md](STATUS.md).

| Metal | Scope |
|---|---|
| [Gold](gold/README.md) | Gold, GLD, rates, official buying and investment flows |
| [Silver](silver/README.md) | Silver, SLV, industrial demand and physical availability |
| [Platinum](platinum/README.md) | Platinum, PPLT, automotive and industrial demand, supply and flows |
| [Palladium](palladium/README.md) | Palladium, PALL, automotive demand, supply and positioning |
| [Copper](copper/README.md) | Copper, CPER, Chinese demand, mine supply and inventories |
| [Shared studies](shared/README.md) | Ratios, paired metals, shared macro evidence and multi-metal datasets |

## Knowledge bases

Each metal has a focused KB: [gold](gold/KB.tsv), [silver](silver/KB.tsv), [platinum](platinum/KB.tsv), [palladium](palladium/KB.tsv), and [copper](copper/KB.tsv). [Shared KB](shared/KB.tsv) holds multi-metal comparisons and general desk records.

These are generated views of the permanent [knowledge ledger](workbook/KB.tsv), with its original IDs, full facts, source references, confidence, dates and correction history intact. Multi-metal entries appear in each relevant view and in shared; desk-only records appear only in shared. A metal mentioned incidentally does not automatically get a tag. Historical rows retain their original status; read later corrections and STATUS before using a claim as current.

To add knowledge or a correction, append to `workbook/KB.tsv` under [its schema](workbook/SCHEMA.tsv), classify every new ID in [KB_METALS.tsv](KB_METALS.tsv), then run `python3 AGENTS/MIDAS/refresh_metal_kbs.py --refresh` from the Git root. Tag rationale is navigation metadata, not a new research claim. Never edit generated `KB.tsv` views directly. The script needs only Python's standard library and resolves paths from its own location. Run it with `--check` for a read-only content check; boot includes this check in its ledger leg. Unclassified/invalid inputs fail visibly; stale views require review. Views are on-demand reading, not new whole-file boot reads.

## Filing policy

Within each metal, new reports go in `research/` and new evidence in `sources/YYYY-MM-DD_topic/`. Create deeper price, positioning, flow, stock, supply or demand categories when they contain material. Inseparable multi-metal research and source bundles belong in `shared/`, with links from each relevant metal.

[METALS_CATALOG.tsv](METALS_CATALOG.tsv) classifies existing research files, source bundles and desk records. It is navigation metadata, not a second financial ledger. A bundle row covers all its files; mixed bundles are tagged for every covered metal rather than copied or split.

Existing `analysis/`, `reports/` and `sources/` remain canonical for their existing artifacts. Their dated locations are cited by frozen forecasts, scripts, source hashes and other desks. This organization adds topic access without moving those references or changing evidence. New work uses the metal folders; add each new report or source bundle to the catalog and the relevant index.

## Authoritative desk records

- [STATUS.md](STATUS.md): current dated state and convergence scores.
- [THESIS.md](THESIS.md): transmission mechanisms and standing rules.
- [OPEN_ITEMS.md](OPEN_ITEMS.md): existing research obligations.
- [PREDICTIONS.tsv](workbook/PREDICTIONS.tsv): forecast letters and resolutions.
- [SOURCES.md](sources/SOURCES.md): source methods and access limits.
- [SCRATCH.md](SCRATCH.md): session continuity.

These records, the desk scripts, inboxes, shared ledgers and immutable Kernel artifacts retain their established paths. Metal indexes carry links rather than duplicate state. No market data, score, threshold, approval or forecast changes through this organization.
