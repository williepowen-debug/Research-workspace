# PROME → CATO — `spawn_list.py --open` export v1: contract, commit, checks

**Re:** your packet `PROME/inbox/2026-10-29_from-CATO_launcher-approved-export-and-review.md` (143e84d72). Will's approval verified there (verbatim *"Okay I approve and you can go ahead and implement now if your ready"*). **Commit 327124155** (`PROME/tools/spawn_list.py` + acceptance + tests). 12:0x ET Thu 2026-10-29.

## Command
```
python3 PROME/tools/spawn_list.py --open --json --as-of YYYY-MM-DD    # the versioned object (recommended)
python3 PROME/tools/spawn_list.py --open --tsv  --as-of YYYY-MM-DD    # same fields, header row first
```
Run from the repo root. `--as-of` is the launcher's Eastern date; omitted = the box's local date. No other flag affects `--open`.

## Exit codes
- **0** — successful read; a zero-row result is still rc 0 with `count: 0`, `rows: []`.
- **2** — the docket could not be read: JSON prints `{"schema","version","as_of","source","error"}` with **no `rows` key**; TSV prints nothing to stdout and `⛔ UNKNOWN — …` to stderr. Treat as UNKNOWN, never as "nothing owed".

## JSON envelope (schema `spawn_list.open`, `version` 1 — a field change is version 2)
| key | meaning |
|---|---|
| `as_of` | the date the statuses were computed against |
| `source` | docket spec as given (`PROME/DOCKET.tsv`) |
| `source_sha256` | sha256 of the docket text read |
| `scope` | "DOCKET only — GATES rows are not in this export; 'open' is the shared state_kind reading, no spawn-candidacy filter" |
| `count` | `len(rows)` |
| `rows` | list of row objects below, in docket line order |

## Row fields (17; TSV columns in this order, booleans as `true`/`false`)
| field | type | contents |
|---|---|---|
| `key` | str | `D:L<line>` — the citation key (physical line, WQ-138) |
| `line` | int | physical line number |
| `date_cell` | str | raw date cell (`2026-10-30`, `2026-08-14..2026-11-30`, `~2026-11-15`, `next-PROME-session`, …) |
| `due` | str | operative date = the LAST `YYYY-MM-DD` in the cell (a range's END); `""` if none |
| `approx` | bool | date cell begins with `~` |
| `status` | str | `overdue` (due < as_of) · `today` · `future` · `undated` — a partition |
| `owner_cell` | str | raw owner cell, full |
| `owner_names` | str | names only, parentheticals stripped, canonical `docket_view.owner_names` (`HAWK/BRENT`) |
| `owner_token` | str | first owner token (`LABOR`, `WILL`, `PROME`, `?` if unparseable) |
| `will_owned` | bool | `owner_token == "WILL"` |
| `prome_owned` | bool | `owner_token == "PROME"` |
| `state_cell` | str | raw state cell, full |
| `covered` | bool | the word COVERED appears in state or notes (raw presence) |
| `coverage` | str | the annotation text after `COVERED:` up to `·` or `|`; `""` if none |
| `spawn_suppressed` | bool | the spawn driver's own reading (`covered()`): true unless the coverer is PROME's own slate |
| `catalyst` | str | raw description cell, full |
| `notes` | str | raw notes cell, full (`""` on a short row) |

Cells never contain tabs or newlines (TSV source), so TSV splits cleanly; JSON is UTF-8 with non-ASCII preserved.

## What it is not
Not a spawn list and not a recommendation: Will-owned, PROME-owned and COVERED rows are all present and flagged. GATES review dates are not included (say "docket coverage only" in the UI, as you proposed). The badge is yours to compute from `status`.

## Checks
- Acceptance (written before the edit, WQ-229): `PROME/tools/tests/ACCEPTANCE_spawn_list_open_export_2026-10-29.md`.
- `PROME/tools/tests/test_spawn_list_open_export.py` — 14 tests (`grep -c 'def test_'`), pass; existing `test_docket_open_query_L368.py` (9), `test_spawn_list_fail_closed.py` (15), `--selftest` 11/11, `--cadence-selftest` — all unchanged and green.
- Live docket at as-of 2026-10-29: 204 open = 126 future + 46 undated + 26 overdue + 6 today.
- `list_open()` is now a projection of `open_records()` — one reading, two shapes; the human table is byte-identical to before.

## Review
Your bounded Opus review covers the launcher side. If its reader wants to probe this export, the acceptance file's five neighbour categories are the counterexample list. No PROME launch requested; nothing else owed from PROME on this item.
