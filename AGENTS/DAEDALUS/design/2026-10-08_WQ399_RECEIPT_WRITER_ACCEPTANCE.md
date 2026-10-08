# WQ-399 — receipt-writer required fields: acceptance conditions (written BEFORE the code)

**Ruling:** WQ-399, Will 2026-10-08 15:27 ET, verbatim *"399 approve"* (PROME packet `inbox/2026-10-08_from-PROME_WQ-399-RULED-receipt-writer-fields.md`). Approves `runs/2026-10-08_D7_CLOSURE_SCOPE_REVIEW.md` §3 steps ① + ② as written. **Written:** 2026-10-08 15:28 EDT (from `date`), committed alone before any code (WQ-229). **Tool:** `scripts/corrections_boot_check.py` `cmd_receipt` (DAEDALUS `scripts/` grant).

## Interface
`--receipt <COR-id> --action <A> [--artifact <path#key>]... [--validation-ref <path#key|NONE>] [--scope <text>] [--review YYYY-MM-DD] [--note <text>]`

| Action | Required | Stored in `note` (prefix, in this order) |
|---|---|---|
| APPLIED | ≥1 `--artifact` AND `--validation-ref` | `artifact=<v>; [artifact=<v>; …] validation_ref=<v>; [scope=<v>;] <note>` |
| NO-OP | `--scope` | `scope=<v>; [artifact=<v>;] <note>` |
| DEFERRED | `--review` | `review=<date>; [scope=<v>;] <note>` |
| CONTESTED | none new (not in the ruling) | optional tokens if given |

The token form matches the receipts already on disk (`key=value; key=value; free text`, e.g. HAWK/HOMER 9/02–9/08). There is no new column and the receipt header is unchanged.

## Acceptance conditions (each a selftest leg; each capable leg must FAIL on the pre-change code)
| Id | Input | Required result |
|---|---|---|
| W1 | APPLIED, no `--artifact` | rc 2, message names `--artifact` and the ruling; receipts file **byte-identical** (or still absent) |
| W2 | APPLIED with `--artifact`, no `--validation-ref` | rc 2, names `--validation-ref`; file unchanged |
| W3 | NO-OP, no `--scope` | rc 2, names `--scope`; file unchanged |
| W4 | DEFERRED, no `--review` | rc 2, names `--review`; file unchanged |
| W5 | DEFERRED, `--review 2026-13-01` / `--review soon` | rc 2 (unparseable date); file unchanged |
| W6 | DEFERRED, `--review` before today | rc 2 (a review date already past is not a deferral); file unchanged |
| W7 | `--artifact` without `#` (e.g. `AGENTS/X/STATUS.md`) | rc 2 (format `path#key`); file unchanged |
| W8 | `--validation-ref` neither `NONE` nor `path#key` | rc 2; file unchanged |
| W9 | any field value containing `;`, tab or newline | rc 2 (would break token parsing); file unchanged |
| W10 | APPLIED complete (two `--artifact`, `--validation-ref NONE`, `--note x`) | rc 0; one row; `note` = `artifact=a#1; artifact=b#2; validation_ref=NONE; x` |
| W11 | NO-OP complete | rc 0; `note` starts `scope=` |
| W12 | DEFERRED complete | rc 0; `note` starts `review=YYYY-MM-DD; ` |
| W13 | CONTESTED with no fields | rc 0 (unchanged behaviour) |
| W14 | an existing 4-field receipts file with old free-text notes | the boot check still parses it; prior rows unaffected by an append |
| W15 | unknown COR-id / bad action | unchanged rc 2 paths (no regression) |
| W16 | existing `--selftest` 21 cases | still pass |

**Invariants:** the boot-check rc contract (CHECK_STANDARD §9) is unchanged; nothing in `cmd_check` changes; validation happens before any file open for append, so rc 2 never leaves a partial row.

**Not in scope:** path-existence checks on `--artifact` (that is D7 leg 1's job at closure time, not the writer's); backfill of the 108 existing rows (③, ruled no); the fleet announcement (PROME carries it).

## Amendment after the conditions commit — 2026-10-08 15:30 EDT (from `date`)
Building turned up one defect in the *conditions*: `path#key` was implemented with a whitespace-free key, which refused `AGENTS/SAM/STATUS.md#BOTTOM LINE`. Markdown section keys routinely contain spaces. **Amended:** the key must be non-empty and start with a non-space character, and may contain spaces (still no `;`, tab or newline, per W9). Two legs added: **W10b** (spaced key → rc 0, written verbatim) and **W7b** (`path#`, empty key → rc 2). Selftest 38/38.
**Capable case (CHECK_STANDARD §3), watched:** the pre-change writer (HEAD `git show HEAD:scripts/corrections_boot_check.py`, loaded with ROOT set to the repo) accepts `--action APPLIED --note x` with no fields: rc 0, row written. The new writer refuses the same input: rc 2, no file created.
