# rent_breadth_inputs — retained Apartment List inputs for the Rent-decline breadth band

One file per monthly refresh: the **100 roster cities only** (`workbook/RENT_BREADTH_ROSTER.tsv`), all columns, extracted from Apartment List's full city CSV. Each extract reproduces the full file's output exactly (checked by `diff` at filing). Kept so the next refresh can run `--prior-file=` and report revisions; the full files (~2.4MB) are not retained.

| Extract | Full source file | Full-file SHA-256 | Fetched |
|---|---|---|---|
| `Apartment_List_2026_09_roster100.csv` | `Apartment_List_Rent_Estimates_2026_09.csv` | `aa05b458d52facddf5415071f2dc45db781c6b9ff9cba747bd938516a2d3a644` | 2026-09-29 |
