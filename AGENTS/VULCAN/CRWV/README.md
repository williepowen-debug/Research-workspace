# CoreWeave research

VULCAN maintains CoreWeave company evidence here. Start with the current records and correction history; the original October20 collection remains a frozen research archive. Organization changes do not refresh the dates of financial statements, market observations or trade cards.

## Start here

| Need | Read |
|---|---|
| Maintained company evidence | [Company KB](KB.tsv) — authoritative company rows, stable KB-VULCAN IDs |
| Current interpretation | [October20 financing and shareholder analysis](2026-10-20_analysis.md) |
| Withdrawn or qualified claims | [Correction history](CORRECTIONS.md) |
| Sources arranged by question | [Deduplicated reading guide](READING_GUIDE.md) |
| Current desk scores and obligations | [VULCAN STATUS](../STATUS.md) |
| Company thesis and five falsifiers | [Canonical VULCAN TRADE](../TRADE.md) |
| Credit and trade construction | [LIQUID owner sweep](../../LIQUID/research/2026-10-19_sweep/REPORT.md); [TERRY owner card](../../TERRY/setups/CRWV_jan15-put-spread_relief-rally-fade_CONCEPT_2026-10-15.md). Their own dates and qualifications govern. |

## Company topics

The KB IDs below resolve through [company KB](KB.tsv), or `scripts/kb_catalog.py --find <ID>` from the desk. Dates and source qualifications stay in each row; a maintained ledger contains historical observations as well as newer corrections.

| Question | Company KB records | Broader context |
|---|---|---|
| Debt facilities and funding access | 050, 068, 074, 075, 077, 169, 176, 238, 246, 247 | LIQUID owns market grades; BROCK owns private-credit judgments |
| Cash flow, interest and spending | 076, 079, 246, 247 | Distinguish cash PP&E from total investing; apply corrections first |
| Customer concentration and contract economics | 080, 175, 241 | Revenue concentration is not backlog allocation; models are assumptions |
| Power, leases and delivery | 051, 078, 247 | WATT owns power/firmness; general KB231 carries the backup-use date correction |
| Insider transactions | 242 | Tax/plan/proposed/completed transactions differ |
| Index membership and exposure | 202, 243 | Direct weight is not the full indirect AI exposure |

## Authority and upkeep

- [CRWV/KB.tsv](KB.tsv) is the editable company authority. [KB_GENERAL.tsv](../workbook/KB_GENERAL.tsv) holds broader desk evidence. Each ID has exactly one editable home.
- [Legacy KB.tsv](../workbook/KB.tsv) is a **generated combined read view** for existing consumers. Do not edit it. After editing an authoritative source, run `python3 AGENTS/VULCAN/scripts/kb_catalog.py --write` from the Git root.
- [Maintenance instructions](MAINTENANCE.md) cover new IDs, row lookup, regeneration and validation. Boot and closeout validate both authorities and reject a stale combined view or duplicate IDs.
- Company rows retain original dates, sources and confidence. LIQUID market grades and TERRY cards remain authoritative at their owners; references here do not create competing grades or approvals.

## Evidence archive

[Reading guide](READING_GUIDE.md) presents one preferred entry per signal/correction family or distinct source. [Catalogue](CATALOG.json) retains every source alias and differing recipient variant. Exact duplicates and historical/intermediate trade screens stay outside the starting reading path; no original evidence was deleted.

The [original source map](SOURCE_MAP.md), [capture manifest](MANIFEST.json), [capture verification](VERIFICATION.json) and `archive/` describe the October20 14:06 capture:86 source copies and6 frozen ledger extracts. **The archived36-row KB extract is historical, not the maintained company KB.** Its later qualifications are mapped in CORRECTIONS.md. Filing-index rows are not copies of the actual SEC filings.

The [organization review](2026-10-20_organization-review.md) records the proposal before implementation. [KB migration receipt](KB_MIGRATION.json) records unchanged IDs and pre-migration row hashes; subsequent legitimate corrections belong at each row’s authority. The reading guide changes navigation, not the evidentiary independence of repeated routes.

## Research questions still open

Current parent/project cash waterfall, updated principal and lease timing, contract-level delivery/acceptance rights, and a validated equity valuation remain unfinished underwriting. This organization work changes no scores, thresholds, forecasts, monitoring cadence or capital permissions.
