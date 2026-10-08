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

## Amendment 2 — after the independent read (2026-10-08 15:37 EDT, from `date`)
Read: `design/2026-10-08_WQ399_INDEPENDENT_READ.md`, ACCEPT-WITH-RESIDUE ❌1 ⚠️12 ✅24. Changes, each with a selftest leg:
| Finding | Change | Leg |
|---|---|---|
| ❌ C10: `\r`, U+2028, `\x85`, `\x0c` written rc 0, then the boot check rc 2 | any `str.splitlines()` break, tab or `;` refused in a FIELD; in `--note` replaced by a space | W9t W9n W9r W9u W9note |
| Non-UTF-8 crash left a header-only file | refused before open | W9x |
| Whitespace-only value satisfied a requirement | stripped; empty = missing | W17 |
| Repeated single-value flag, last silently wins | refused if given twice | W18 |
| A field on an action that does not take it was stored | per-action allowed set (APPLIED: artifact, validation_ref, scope · NO-OP: scope, artifact · DEFERRED: review, scope · CONTESTED: scope, artifact); others refused | W19 |
| `--note` could forge a leading token | a note beginning `artifact=`/`validation_ref=`/`scope=`/`review=` is refused | W20 |
| `--review` took a time suffix / leading space | strict `YYYY-MM-DD` after strip | W21 |
| `--today` admitted a past review into a real file | the CLI write path ignores `--today` | (CLI; selftests pass `today` directly) |
| Vacuous legs W1–W4, W9, W11, W14, W15 | message names the flag + "Nothing written"; each break char tested; two-token ordering (W11b); prior bytes preserved on append; bad action (W15b) | as listed |
| Boot-check remedy printed the old command | names the WQ-399 fields per action | — |
Selftest **51/51**. The ❌ was reproduced on `8bf9a3625` (write rc 0, boot check rc 2) and is refused on the new code (rc 2, no file). ~~Live boot check identical to `8bf9a3625` on SAM, HAWK, PROME, DAEDALUS, WALTER and BRENT.~~ ⛔ Overstated, see Amendment 3: rc is identical on all six, but output is byte-identical only on DAEDALUS and WALTER; the rc 1 desks differ on their BLOCK remedy line, which is the intended change. The docs at `AGENTS/SAM/CLAUDE.md:50` and `PROME/BOOT.md:69` still show the old command; PROME's fleet announcement is the ruled carrier.

## Amendment 3 — delta read and declared residue (2026-10-08 15:44 EDT, from `date`)
Delta read `design/2026-10-08_WQ399_DELTA_READ.md`: **ACCEPT-WITH-RESIDUE ❌0 ⚠️10 ✅27**. The first read's ❌ C10 is closed in code (6/6 variants rc 2, file unchanged). Regression over 45 names: rc and stderr identical; the 26 rc 1 desks differ only on the `then receipt:` remedy line (intended). `--coverage` and `--write-compliance` are identical. The invariant "nothing in `cmd_check` changes" is **amended**: only the BLOCK remedy text changed.

**No third correction pass on this file today** (two-correction stop; the parserfix 9/18 precedent). Declared residue, owner DAEDALUS, carried into the **D7 build**, which is where the tokens are first parsed:
| Id | Residue | Why it can wait | Where it is fixed |
|---|---|---|---|
| N06 / F4 | `--note` can still carry a token after the first position (`; artifact=…`) or in another case (`Scope=`) | no reader parses tokens yet | **D7 parser contract: evidence tokens are read ONLY from the leading `key=value; ` run the writer emits (exact-case keys); anything after the first non-token segment is free text.** Optionally the writer also refuses a token anywhere in the note, case-insensitive, at the next touch |
| N08 | `--review` accepts non-ASCII digits (`\d` without `re.ASCII`) | `date.fromisoformat` rejects them, so latent until D7 | next touch: `[0-9]` |
| N02 | CONTESTED now refuses `--review` / `--validation-ref`; the Interface row said "optional tokens if given" | the ruling defines no CONTESTED fields; narrower is the safe side | **Interface row amended:** CONTESTED takes `--scope` / `--artifact` only |
| F7 | `PROME/tools/prome_gate.py:1604` prints the field-less command | PROME's file | PROME's fleet announcement packet names it |
| F12 / W15b | W15b cannot fail (its fields are rejected as stray first); no legs for non-UTF-8 `--note`, the CLI ignoring `--today`, lower-case `none` | code behaves correctly; test gap only | next touch: W15b with no fields, plus three legs |
| minor | zero-width-space-only `--scope` satisfies NO-OP; the remedy's `<A>` omits CONTESTED; docstring says "CONTESTED (none new)" without the `--today` note | cosmetic | next touch |
