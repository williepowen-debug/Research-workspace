# WQ-399 receipt writer — independent read of commit 8bf9a3625

**Reader:** fresh-context independent reader (Opus), commissioned by DAEDALUS. **Started:** 2026-10-08 15:31:46 EDT (from `date`).
**Subject:** `scripts/corrections_boot_check.py` at 8bf9a3625 vs acceptance `design/2026-10-08_WQ399_RECEIPT_WRITER_ACCEPTANCE.md` (W1–W16 + amendment W7b/W10b) and ruling packet `inbox/2026-10-08_from-PROME_WQ-399-RULED-receipt-writer-fields.md`.
**Method:** read-only on the repo; every CLI run uses `--register`/`--receipts` fixtures under the reader's scratchpad (`.../scratchpad/w399_reader`). This file is the only repository write.

## Verdict
**ACCEPT-WITH-RESIDUE — ❌ 1 · ⚠️ 12 · ✅ 24** (closed 2026-10-08 15:35:51 EDT, from `date`).

Every acceptance leg (W1–W16 plus W7b and W10b) holds in the code. All three invariants hold too: the boot check is byte-identical on 45/45 agent tokens, no line of `cmd_check` changed, and nothing is validated after the file opens. `--coverage` and `--write-compliance` are unchanged, and all 108 receipts on disk still parse.

The single ❌ is **outside the AC's letter and already existed in the `--note` path**. A field value carrying `\r` (or U+2028, `\x85`, `\x0c`, any other `str.splitlines()` separator) is **accepted with rc 0**. That desk's **boot check then reads rc 2 CANNOT-EVALUATE** until someone hand-edits the receipts file, and the error message names a garbage `receipt_date` rather than the cause (C10–C10f). W9 refuses `;`, tab and `\n` only. WQ-399 adds three free-text fields at exactly the place where people paste paths. This is a WSL box, and a `"$(cat file)"` from a CRLF file keeps the `\r`. **Recommend a fix before PROME's fleet announcement.** Refuse any value where `len(v.splitlines()) != 1` or that contains `\r`, and treat a whitespace-only value as missing. Apply the same rule to `--note`, then add tab, newline, `\r` and U+2028 legs to the selftest. The fix is small and is the reader's recommendation. The author decides.

The selftest is **38/38, but 5 of its claims are vacuous under mutation**: W9 tab/newline, W11 ordering, the W1–W4 message text, W14 prior-row preservation, and the W15 bad-action half. Each mutant that removed one of these behaviours still passed 38/38 (§2). The shipped behaviour is right in every case (§3–§4), so these are test gaps, not code defects.

## Leg table (code behaviour; selftest-coverage gaps are separate ⚠️ rows)
| Id | Claim | Command (fixture) | Result | Verdict |
|---|---|---|---|---|
| W1 | APPLIED without `--artifact` → rc 2, names `--artifact` + ruling, file unchanged/absent | C12 `--action APPLIED --note x`, absent dir | rc 2, `APPLIED requires --artifact <path#key> and --validation-ref … (WQ-399, Will 2026-10-08). Nothing written.`, no file, no dir | ✅ |
| W2 | no `--validation-ref` → rc 2, names it | W2cli | rc 2, names `--validation-ref`, unchanged | ✅ |
| W3 | NO-OP without `--scope` → rc 2 | W3cli | rc 2, names `--scope`, unchanged | ✅ |
| W4 | DEFERRED without `--review` → rc 2 | W4cli (no prior file) | rc 2, file still absent | ✅ |
| W5 | unparseable review → rc 2 | selftest W5/W5b; C18 `2026-02-30` | rc 2 `impossible --review`, unchanged | ✅ |
| W6 | review before today → rc 2 | selftest W6; M3 caught by W6 | rc 2 | ✅ (bypassable via `--today`, ⚠️ C11) |
| W7 / W7b | artifact without `#` / empty key → rc 2 | selftest W7/W7b; C16 `#k`; C02 `''` | rc 2, unchanged | ✅ |
| W8 | validation-ref neither NONE nor path#key → rc 2 | selftest W8; C03 `none`; C15 `'NONE '` | rc 2, unchanged | ✅ |
| W9 | `;`, tab, newline in any field → rc 2 | selftest W9 (`;`); W9tab; W9nl | rc 2 all three, unchanged | ✅ letter (the class is wider: ❌ C10) |
| W10 | APPLIED complete → exact note | W10cli | `artifact=a#1; artifact=b#2; validation_ref=NONE; x` | ✅ |
| W10b | key with spaces written verbatim | selftest W10b | rc 0, `…#BOTTOM LINE; validation_ref=NONE; ` | ✅ |
| W11 | NO-OP complete, note starts `scope=` | selftest W11; C09c | starts `scope=` (also with an extra token) | ✅ (ordering unpinned, ⚠️ M4) |
| W12 | DEFERRED complete, starts `review=YYYY-MM-DD; ` | selftest W12; C09e | starts `review=` | ✅ (time suffix admitted, ⚠️ C04) |
| W13 | CONTESTED no fields → rc 0 | W13cli | rc 0, note empty | ✅ |
| W14 | old 4-field file parses; prior rows unaffected | W10cli prefix check; §6 | prior bytes exact prefix: True; boot rc 0; 108 live rows parse | ✅ (unpinned in selftest, ⚠️ M8) |
| W15 | unknown COR-id / bad action → unchanged rc 2 | W15cli; C01, C14, C14b | rc 2, unchanged | ✅ |
| W16 | prior 21 selftest cases pass | `--selftest` | 5/5 header + 16/16 D4 PASS | ✅ |
| INV-1 | boot-check rc contract unchanged | §5, 45 tokens old vs new | 45/45 byte-identical | ✅ |
| INV-2 | nothing in `cmd_check` changes | `git show 8bf9a3625` hunks | no hunk inside `cmd_check` | ✅ |
| INV-3 | validate before open: an rc 2 leaves no partial row | M9 (caught); C12/C12b (no dir created); every rc-2 case in §3 unchanged | holds for every rc-2 path | ✅ |
| REG-cov | `--coverage` unchanged | §5 | identical, 38/38 | ✅ |
| REG-wc | `--write-compliance` unchanged | §5, two windows | identical (rc 0; rc 1 / 11 OWED) | ✅ |
| DISK | existing receipts parse | §6 | 30 files / 108 rows, none rc 2 | ✅ |
| SELF | capable case (old writer accepts fieldless APPLIED) | O3 old code | rc 0, row written; new code rc 2 (C12) | ✅ |

## Findings
| # | Sev | Finding | Evidence |
|---|---|---|---|
| F1 | ❌ | Line-separator characters in a field value (`\r`, U+2028, `\x85`, `\x0c`; anything `str.splitlines()` splits on) are written with rc 0. That desk's boot check then returns **rc 2** until the file is hand-edited, and the message blames `receipt_date`. This already existed via `--note` (O1/O2), and the new fields widen the surface | C10, C10b–f; O1, O2 |
| F2 | ⚠️ | Whitespace-only `--scope '   '` satisfies NO-OP's required field | C05 |
| F3 | ⚠️ | Single-valued flags are last-wins without warning: `--validation-ref p#q --validation-ref NONE` silently stores NONE | C07, C07b |
| F4 | ⚠️ | **Token provenance.** A field given to an action that does not require it is stored as a token: `review=` on APPLIED, `validation_ref=` on NO-OP, the full APPLIED evidence set on DEFERRED. Note text can also forge tokens on any action. A D7 parser cannot tell validated writer tokens from note prose or from tokens that do not belong to the action | C09, C09c, C09e, C13, C13b |
| F5 | ⚠️ | `--today` (documented as a fixture override) now also governs the writer's past-review check, so a past review date can be written to a real file | C11 |
| F6 | ⚠️ | `--review` accepts DATE_RE's `THH:MMZ` suffix and a leading space, and stores both verbatim (AC: `YYYY-MM-DD`) | C04, C04c |
| F7 | ⚠️ | The boot check's own printed remedy, plus the SAM and PROME boot docs, still give `--action <APPLIED\|NO-OP\|DEFERRED\|CONTESTED>` with no fields, and the writer now refuses that for 3 of 4 actions. Fail-closed, and the refusal prints the fix. PROME's announcement is the ruled carrier; the printed remedy in `cmd_check` is frozen by INV-2 | `corrections_boot_check.py BRENT` → `then receipt: … --action <APPLIED\|NO-OP\|DEFERRED\|CONTESTED>`; `AGENTS/SAM/CLAUDE.md:50`; `PROME/BOOT.md:69` |
| F8 | ⚠️ | Non-UTF-8 argv: traceback rc 1, and with no prior file a header-only receipts file is created. It parses clean, so the effect is cosmetic, but a refused write still creates the file | C19, C19c |
| F9 | ⚠️ | Selftest: the W9 tab/newline legs are vacuous (only `;` is tested) | M2 38/38 |
| F10 | ⚠️ | Selftest: the W11 "scope first" leg has one token, so ordering is vacuous | M4 38/38 |
| F11 | ⚠️ | Selftest: W1–W4 never assert the message (flag name + ruling) | M6 38/38 |
| F12 | ⚠️ | Selftest: W14 "prior rows unaffected" is not asserted, and a writer that truncates the file passes 38/38. W15's bad-action half and lower-case `none` are also unpinned | M8, M11, M7 38/38 |

## Limits
- The fixture register is one synthetic NAMED row. I did not exercise the live register's ALL-rows through the writer, because the writer checks only that the COR-id exists.
- The old-code comparison used importlib with `ROOT` overridden, as instructed. `prome_gate.py boot`, which wraps the check, was not run. It inherits the check unchanged, but that is inference, not observation.
- I did not test path existence for `--artifact` (out of scope by AC) or concurrent appends (not changed by this commit).
- The mutation set is mine (13 mutants). A mutant that passes shows a leg is vacuous. A mutant that fails does not prove the leg is complete.
- I wrote no receipt to any real file. Every write went to `scratchpad/w399_reader/cx/*` and `…/old/*`. This ledger is the only repository write. Nothing was committed or messaged.

## Working log (appended as the read proceeds)

### 1. Baseline (15:31:47 EDT)
- `git diff 8bf9a3625 -- scripts/corrections_boot_check.py` → empty (working tree = commit under review).
- `python3 scripts/corrections_boot_check.py --selftest` → `SELFTEST 0 PASS: 38/38 cases`, rc 0 (5 header + 16 D4 + 17 WQ-399 legs).

### 2. Mutation test of the selftest (does each leg actually bite?)
Harness `scratchpad/w399_reader/mutate.py`: apply one source mutation to a scratch copy, run `--selftest`, list FAIL legs.

| Mutant | Selftest result | Legs that caught it | Reading |
|---|---|---|---|
| M1 drop the missing-field refusal | 34/38 FAIL | W1 W2 W3 W4 | ✅ capable |
| M2 W9 checks `;` only (tab/newline no longer refused) | **38/38 PASS** | none | ⚠️ W9 tab/newline legs not exercised (only `a; b` is tested) |
| M3 drop review<today check | 37/38 | W6 | ✅ |
| M4 drop NO-OP scope-first ordering | **38/38 PASS** | none | ⚠️ W11 has only one token, so "scope first" is vacuous |
| M5 drop DEFERRED review-first ordering | 37/38 | W12 | ✅ |
| M6 refusal message no longer names the flag or the ruling | **38/38 PASS** | none | ⚠️ W1–W4 "message names `--artifact` and the ruling" is not asserted (rc + bytes only) |
| M7 accept lower-case `none` as validation_ref | **38/38 PASS** | none | ⚠️ (CLI test below shows the shipped code refuses it — behaviour right, unpinned) |
| M8 writer opens `w` and rewrites header → prior rows destroyed | **38/38 PASS** | none | ⚠️ W14 "prior rows unaffected by an append" is NOT asserted — the leg checks only that the boot check parses (chk_rc 0), and the old row and the new row receipt the same COR-id, so losing the old row is invisible |
| M9 validate after `open(..., "a")` | 37/38 | W4 only (the one leg with no prior file) | ✅ capable, but by a single leg |
| M10 drop artifact path#key check | 36/38 | W7 W7b | ✅ |
| M11 drop the writer's action-enum check | **38/38 PASS** | none | ⚠️ W15 "bad action" half not in the selftest (CLI test below shows the path still works) |
| M12 W9 drops `;` | 37/38 | W9 | ✅ |
| M13 treat whitespace-only value as missing (a TIGHTER writer) | 38/38 PASS | n/a | no leg pins whitespace-only behaviour either way |

### 3. Counterexamples (CLI, fixtures only) — 15:32:49–15:33:33 EDT
Harness `scratchpad/w399_reader/cx.py` (+ `batch1.py`, `batch2.py`): fresh dir per case, fixture register with one LIVE NAMED SAM row `COR-20260920-02`, prior receipts file = header + one old free-text NO-OP row (unless stated). Command shape: `python3 scripts/corrections_boot_check.py SAM --register <fx>/reg.tsv --receipts <fx>/r.tsv --receipt COR-20260920-02 --action <A> …`; then the boot check re-run on the same fixture. "unchanged" = receipts bytes identical before/after.

| # | Input | rc | File | Written note / output | Boot check after | Verdict |
|---|---|---|---|---|---|---|
| C01 | `--action applied` (lower case) + valid fields | 2 | unchanged | `action 'applied' not in [...]` | 0 | ✅ refused (writer is case-strict; reader upper()s — pre-existing asymmetry, harmless direction) |
| C02 | `--artifact ''` | 2 | unchanged | `--artifact '' is not path#key` | 0 | ✅ (caught by format, not by "missing" — message still adequate) |
| C03 | `--validation-ref none` | 2 | unchanged | `'none' is neither NONE nor path#key` | 0 | ✅ |
| C04 | DEFERRED `--review 2026-10-08T23:59Z` | **0** | row | `review=2026-10-08T23:59Z; ` | 0 | ⚠️ AC/ruling say `--review YYYY-MM-DD`; DATE_RE's time suffix is admitted and stored verbatim — a D7 parser expecting a bare date gets a timestamp |
| C04b | `--review 2026-10-08` (= today) | 0 | row | `review=2026-10-08; ` | 0 | ✅ boundary "today or later" holds (unpinned in selftest) |
| C04c | `--review ' 2026-10-15'` (leading space) | **0** | row | `review= 2026-10-15; ` | 0 | ⚠️ validated on the stripped value, stored unstripped |
| C05 | NO-OP `--scope '   '` (whitespace only) | **0** | row | `scope=   ; ` | 0 | ⚠️ the required field is satisfied by nothing — W3 passes vacuously on blank text |
| C05b | `--artifact 'a/b.md#k   '` | 0 | row | `artifact=a/b.md#k   ; ` | 0 | ⚠️ trailing space stored in the key (minor) |
| C06 | `--artifact a/b.md#k#2 --validation-ref x/y.md#a#b` | 0 | row | stored verbatim | 0 | ✅ acceptable (split on first `#`) |
| C07 | `--scope FIRST --scope SECOND` | **0** | row | `scope=SECOND; ` | 0 | ⚠️ argparse last-wins: FIRST silently dropped, no warning |
| C07b | `--validation-ref p#q --validation-ref NONE` | **0** | row | `validation_ref=NONE; ` | 0 | ⚠️ a real validation pointer silently replaced by NONE (last wins) |
| C08 | `--scope 'STATUS · KB · predictions'` | 0 | row | stored verbatim | 0 | ✅ |
| C09 | APPLIED + `--review 2026-12-01` | **0** | row | `artifact=a#1; validation_ref=NONE; review=2026-12-01; ` | 0 | ⚠️ leak: an APPLIED row carries a `review=` token (AC table lists no review for APPLIED); a token-keyed reader can read it as deferred |
| C09b | APPLIED + `--review 2026-01-01` | 2 | unchanged | `--review … before today … not a deferral` | 0 | ⚠️ an irrelevant field on the wrong action is validated and refuses the receipt (wording speaks of a deferral) — fail-closed, so harmless |
| C09c | NO-OP + `--validation-ref NONE` | 0 | row | `scope=s; validation_ref=NONE; ` | 0 | ⚠️ leak (not in AC table for NO-OP) |
| C09d | CONTESTED + `--artifact a#1 --review 2026-12-01` | 0 | row | `artifact=a#1; review=2026-12-01; ` | 0 | ✅ AC: "optional tokens if given" |
| C09e | DEFERRED + `--artifact --validation-ref --scope` | 0 | row | `review=2026-12-01; artifact=a#1; validation_ref=NONE; scope=s; ` | 0 | ⚠️ leak: a DEFERRED row carries the full APPLIED evidence token set |
| **C10** | NO-OP `--scope $'AGENTS/SAM/STATUS.md\r'` (CRLF paste) | **0** | row written | `scope=AGENTS/SAM/STATUS.md\r; ` | **2** `unparseable receipt_date '; '` | ❌ writer accepts, file then fails the desk's own BOOT check (CANNOT-EVALUATE) until hand-edited; message does not name the cause |
| C10b | `--scope $'a b'` | 0 | row | U+2028 inside | **2** `unparseable receipt_date 'b; '` | ❌ same class (`read_tsv` uses `str.splitlines()`, which splits on \r \v \f \x1c-\x1e \x85    ) |
| C10c | `--scope $'a\x85b'` | 0 | row | | **2** | ❌ same class |
| C10d | `--scope $'a\x0cb'` | 0 | row | | **2** | ❌ same class |
| C10e | `--artifact $'a/b.md#k\r'` | 0 | row | | **2** | ❌ same class via the artifact key (`\S.*` admits \r) |
| C10f | `--scope $'x\ry'`, no prior file | 0 | created | | **2** | ❌ same class on first receipt |
| C11 | DEFERRED `--review 2021-01-01 --today 2020-01-01` | **0** | row | `review=2021-01-01; ` | 0 | ⚠️ W6 bypass: the fixture-only `--today` override now also governs the writer's "past review" check, and nothing stops it on a real receipts path |
| C12 | APPLIED `--note x`, receipts path in a NON-EXISTENT dir | 2 | absent | `APPLIED requires --artifact … and --validation-ref … (WQ-399, Will 2026-10-08). Nothing written.` | n/a | ✅ no file, no dir created (`dir_created=False`) |
| C12b | `--artifact nohash`, non-existent dir | 2 | absent | format message | n/a | ✅ no dir created |
| C13 | NO-OP `--scope s --note 'artifact=FAKE#1; validation_ref=NONE; real note'` | 0 | row | `scope=s; artifact=FAKE#1; validation_ref=NONE; real note` | 0 | ⚠️ note text forges writer tokens; indistinguishable from validated tokens (FAKE#1 never validated — here it is well-formed, but `--note 'artifact=nohash; '` would equally pass) |
| C13b | CONTESTED `--note 'artifact=FAKE#1; validation_ref=NONE; '` | 0 | row | an APPLIED-shaped token set on a CONTESTED row, none validated | 0 | ⚠️ same |
| C14 | `--action 'APPLIED '` | 2 | unchanged | not in enum | 0 | ✅ |
| C14b | `--action ''` | 2 | unchanged | not in enum | 0 | ✅ (W15 bad-action half, CLI-confirmed) |
| C15 | `--validation-ref 'NONE '` | 2 | unchanged | | 0 | ✅ |
| C16 | `--artifact '#k'` | 2 | unchanged | | 0 | ✅ |
| C17 | `--review 9999-12-31` | 0 | row | | 0 | ⚠️ no upper bound — an indefinite "deferral" is a NO-OP in disguise (not in AC; noted only) |
| C18 | `--review 2026-02-30` | 2 | unchanged | `impossible --review` | 0 | ✅ |
| C19 | NO-OP `--scope $'a\xffb'` (non-UTF-8 argv), no prior file | **1** (traceback) | **created, header only** | `UnicodeEncodeError … surrogates not allowed` | 1 (the obligation is simply still open) | ⚠️ not an rc-2 path, but a refused write still creates the file (header written, then the row's encode raises). Header-only file parses clean, so harm is cosmetic |
| C19b | same, prior file | 1 | unchanged | same traceback | 0 | ✅ no partial row |

**Pre-change comparison for C10 and the W1 capable case (`git show 8bf9a3625^:scripts/corrections_boot_check.py` → `scratchpad/w399_reader/old_cbc.py`, run via importlib with `m.ROOT` set; `oldrun.py`):**
- O1 old writer `--note $'x\ry'` → write rc 0; boot check after rc 2 `unparseable receipt_date 'y'`. O2 `--note $'a b'` → same, rc 2. **So C10 is a pre-existing hole in the `--note` path** that WQ-399 neither opened nor closed — but the build adds three new free-text fields exactly where people paste paths (WSL box, CRLF files exist), and W9's own rationale ("would break parsing") is the class C10 belongs to. New `--note` with `\r` is still unguarded on the new code (same `.replace("\t"," ").replace("\n"," ")`).
- O3 old writer, APPLIED with no fields → rc 0, row written (the capable case — reproduces the author's claim). O4 old writer rejects `--artifact` as an unrecognized argument (argparse rc 2), so CLI-level W5–W9 cannot "fail on pre-change code" in a meaningful sense; capability for those legs is shown by the mutation table instead.

### 4. CLI confirmation of the AC legs (15:34:42 EDT, `batch4.py`, same fixture shape)
- W2 → rc 2 `APPLIED requires --validation-ref <path#key|NONE> (WQ-399, Will 2026-10-08). Nothing written.`, unchanged. W3 → rc 2 `NO-OP requires --scope <text> (WQ-399 …)`, unchanged. W4 (no prior file) → rc 2 `DEFERRED requires --review YYYY-MM-DD (WQ-399 …)`, file still absent. W1 → C12 above (names `--artifact` and the ruling).
- W9 tab: `--scope $'a\tb'` → rc 2 `contains ';', a tab or a newline`, unchanged. W9 newline: `--artifact $'a#1\nx'` → rc 2, unchanged. (Behaviour right; the selftest does not pin these — M2.)
- W10: two `--artifact`, `--validation-ref NONE`, `--note x` → rc 0, note `artifact=a#1; artifact=b#2; validation_ref=NONE; x` (exact AC string).
- W13: CONTESTED, no fields → rc 0, note empty.
- W14: after the W10 append, the prior file bytes are an exact prefix of the new file (`prior bytes are an exact prefix: True | rows after: 2`), boot check rc 0.
- W15: unknown COR-id → rc 2 `not in register`, unchanged; bad action → C01/C14/C14b.

### 5. Regression (15:34:21 EDT) — new file vs `git show 8bf9a3625^:scripts/corrections_boot_check.py` loaded via importlib with `m.ROOT = Path('/home/willi/Research-workspace')`, `sys.argv=[...]; m.main()` (`scratchpad/w399_reader/oldrun.py`)
| Surface | Population | Result |
|---|---|---|
| Boot check `corrections_boot_check.py <AGENT>` | 45 tokens = 43 FLEET_DIRECTORY agents ∪ 30 desks with receipts files ∪ {`ZZZNOTANAGENT`, `hawk`} | **45/45 byte-identical** (rc + stdout + stderr). New-code rc tally: 0×18 · 1×26 · 2×1 (ZZZNOTANAGENT only) |
| Named six | SAM rc 1 · HAWK rc 1 · PROME rc 1 · DAEDALUS rc 0 · WALTER rc 0 · BRENT rc 1 | identical old vs new for each |
| `--coverage` | live | identical, rc 0, `38/38 active+tier-2 desks wired = 100%` |
| `--write-compliance` (default since 2026-10-08) | live BOARD | identical, rc 0 `R1-WRITE 0 OK` |
| `--write-compliance --since 2026-09-01` | live BOARD | identical, rc 1 `11 correction-class signal(s) with NO register row` |
| Diff hunks | `git show 8bf9a3625 -- scripts/corrections_boot_check.py` | hunks touch docstring, a new block after `cmd_check`'s `return 0`, `cmd_receipt`, selftest, `main` — **no line inside `cmd_check` changed** |

### 6. Existing receipts on disk (15:34:31 EDT)
30 files (`AGENTS/*/registry/corrections_receipts.tsv` + `PROME/registry/…`), **108 rows**; all 30 desks ran the new boot check without rc 2 (§5). 0 rows with >4 columns, 0 `\r` bytes, 0 `splitlines()`-only separators. Rows already carrying writer-style tokens: `artifact=` 5, `scope=` 4 (matches the ruling's "5/108"). **No existing receipt fails to parse.**
