# CoreWeave evidence maintenance

Will authorized implementation of the October20 organization review. VULCAN owns this company collection; specialist source owners retain their decisions and observation methods.

## Where to write

| File | Role |
|---|---|
| CRWV/KB.tsv | Editable authority for company-specific evidence |
| workbook/KB_GENERAL.tsv | Editable authority for broader AI/semi transmission and mixed fleet context |
| workbook/KB.tsv | Generated combined read view; existing links/readers stay valid |
| CRWV/archive/extracts/KB.tsv | Frozen initial extract; never a current writable source |

Do not renumber or clone an existing KB row into the other authority. Use a reference for cross-domain relevance. A genuinely new observation gets the next global KB-VULCAN ID across both sources; date, as_of, source and confidence retain their meanings under workbook/SCHEMA.tsv. A correction preserves the original claim with an explicit dated qualification and a correction-history link. A new row is not a new independent witness when it reuses the same source.

## Editing and lookup

Run these commands from the repository root; the scripts also locate their desk independently of cwd.

```sh
python3 AGENTS/VULCAN/scripts/kb_catalog.py --find KB-VULCAN-243
python3 AGENTS/VULCAN/scripts/kb_catalog.py --next-id
```

The next-ID command suggests an unused global ID; it does not reserve it across concurrent writers. Recheck before appending. Edit the single appropriate authority, then regenerate and validate:

```sh
python3 AGENTS/VULCAN/scripts/kb_catalog.py --write
python3 AGENTS/VULCAN/scripts/kb_catalog.py --check
python3 AGENTS/VULCAN/scripts/validate_workbook.py --boot
```

The schema declares both authoritative files and the combined view. The validator checks field types and confidence values, cross-source ID uniqueness, source/view equality and preservation of pre-migration permanent IDs. It fails if an authority disappears or a canonical change is omitted from the combined view. Boot leg7 and closeout invoke that same validator. Ledger staleness includes CRWV/KB.tsv through workbook/LEDGER_GLOB. No source is automatically re-dated or fetched.

## Reading guide and archive

The catalogue groups routed signal copies, the DDTL correction family, and exact content duplicates. Differing recipient content remains available in every entry’s aliases. This is a navigation grouping, not a claim that every variant is semantically interchangeable.

```sh
python3 AGENTS/VULCAN/scripts/crwv_library.py --check
python3 AGENTS/VULCAN/scripts/crwv_library.py --write
```

The check verifies frozen source-copy hashes and the generated catalogue/guide. A change to frozen evidence fails; do not regenerate the capture manifest to hide a changed file. New company research should be dated and linked deliberately; new external evidence is not discovered automatically by this script. A deliberate future capture needs a new dated provenance record rather than silently updating the old one.

## Regression checks after reader changes

```sh
python3 AGENTS/VULCAN/scripts/test_kb_catalog.py
python3 AGENTS/VULCAN/scripts/test_validate_workbook.py
```

The migration receipt’s original row hashes certify conservation at migration. They are not a requirement that current facts never receive legitimate amendments. Its original ID inventory prevents accidental deletion of a permanent historical record, including deletion from both an authority and the generated view.
