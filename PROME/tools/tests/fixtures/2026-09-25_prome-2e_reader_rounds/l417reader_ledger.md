# L417 gate-citability leg: independent reader ledger (read-only, Opus)

**VERIFIED-WITH-RESIDUE: 1 ❌ · 10 ⚠️ · 10 ✅**

Scope read: ACCEPTANCE_prome_gate_citability_L417.md (conditions 1–9); the uncommitted `git diff` of prome_gate.py and GATES_README.md; `scan_gate_citability`, `citability_detail`, `record_gate_citability` and the call site at prome_gate.py:561; `guard`, `aggregate_rc` and `main()` rendering; the test suite; README L31.
My scripts (all in the scratchpad): `live_cmp.py` (compares the one-liner with the leg on the live ledger), `counterex.py` (CE1–CE10), `errpath.py` (ERROR and exception paths). The boot gate was NOT run.

Test counts: `grep -c 'def test_'` finds 10 tests in test_prome_gate_citability_L417.py and 7 in test_prome_gate_gates.py. Both suites pass under `-W error::ResourceWarning` (Ran 10 OK · Ran 7 OK).

---

## ❌ (1)

**❌1: 3 of the 18 LIVE rows have their letters silently unread, and the detail line hides it (condition 5 fails on the live ledger)**
- **Claim.** When a definition_surface cell is path-like but has no `.md`/`.tsv` token, the leg treats it as "no file", the same as `NONE | prose`. That covers a directory plus a row-id pointer. It raises no ERROR and prints no disclosure. The acceptance file names this exact defect: "a scan that silently skips an unreachable definition_surface reports clean for a letter it never read". Condition 5 exempts only a cell with "no path-like token at all".
- **Artifact.** prome_gate.py:483 (`_DEF_PATH.findall(surf)` → empty ⇒ the loop body never runs) and :462 (`_DEF_PATH`). The live rows affected:
  - GATE-LIQ-069 (`AGENTS/LIQUID/workbook (KB-LIQ-069)`, and its state is **`LIVE — **ARMED 1-of-2`**)
  - GATE-LIQ-072 (`AGENTS/LIQUID/workbook (KB-LIQ-072)`)
  - GATE-FLG-T08 (`AGENTS/FLG/ T-08 register`)
- **Verification.**
  - `python3 $SCRATCH/live_cmp.py` printed `extracted: []` for all three rows.
  - `counterex.py` CE1 built a throwaway `AGENTS/X/KB.tsv` carrying `production UNVERIFIED` behind a row with surf `AGENTS/X (KB-X-1)` and state `LIVE — **ARMED 1-of-2`.
- **Observed.**
  - CE1 → `violations=[] unreachable=[] files=0`, detail `0 hits over 0 files · condition cells: 0`: a real violation read as CLEAN.
  - On the live ledger the detail says `0 hits over 20 files` and never mentions that only 15 of the 18 LIVE rows were read.
  - Today's substance is clean. `grep -rlE 'production UNVERIFIED|realisation UNKNOWN' AGENTS/LIQUID/workbook AGENTS/FLG` returns nothing, so the live 0 is VERIFIED, but it was verified by me and not by the leg.
  - The one-liner has the identical blind spot, so the two agree while both being wrong. Parity is not correctness.
- **Proposed change.**
  - (a) Put rows-read coverage into the detail: `… over M files · K of N LIVE rows' letters read · unread: GATE-…`.
  - (b) Treat a cell whose path-like token resolves to a DIRECTORY (`(root/p).is_dir()`, with the regex widened to catch bare dir paths) as ERROR/unreachable, or at least a named ADVISE. Keep the `NONE | prose` carve-out exactly as condition 5 words it.
  - (c) Separately, have the owners re-point the three cells to the files: LIQUID `workbook/KB.tsv` and FLG `workbook/TRIGGERS.tsv`, both inferred.
  - Add a CE1-shaped test (directory + row-id pointer). Doing (b) alone would turn live boot to rc 2 until (c) lands, so sequence (c) first or ship (b) as ADVISE.

## ⚠️ (10)

**⚠️1: A short LIVE row is dropped entirely, including its CONDITION cell**
- **Claim.** A LIVE row with 10 or fewer cells (for example a truncated line with no definition_surface) is dropped wholesale, so its condition cell (the WQ-162 home) is never scanned. `scan_gates_rows` tolerates short rows, so nothing else blocks them either.
- **Artifact.** prome_gate.py:474 `live = [r for r in rows if len(r) > 10 and …]`.
- **Verification.** counterex.py CE4: a 10-cell row, state `LIVE — x`, condition `≥30bp — realisation UNKNOWN`.
- **Observed.** `violations=[] … 0 hits over 0 files · condition cells: 0`. The one-liner would crash with IndexError (fail-loud), so the leg is quieter than the thing it replaces. The live ledger currently has 0 short rows (`live_cmp.py`: `rows with len<=10: []`).
- **Proposed change.** Take every `r[5].startswith("LIVE")` row, always scan `r[3]`, and treat `len(r) <= 10` as an unreachable-surface ERROR.

**⚠️2: A duplicate gate_id hides the second row's lead**
- **Claim.** The violation check resolves the lead via `next(r for r in live if r[0] == g)`, which always returns the FIRST row with that id.
- **Artifact.** prome_gate.py:498.
- **Verification.** counterex.py CE2: row 1 `G-DUP` `LIVE / NOT ARMED — …`, row 2 `G-DUP` `LIVE — armed`, both citing the token file.
- **Observed.** `violations=[]`, detail `… → G-DUP, G-DUP · … all hit rows lead 'LIVE / NOT ARMED —'`. That line is false for row 2.
- **Proposed change.** Store row objects or indices in `files[p]` instead of gate ids. Optionally add a duplicate-gate_id BLOCK to `scan_gates_rows`.

**⚠️3: Only `.md`/`.tsv` letters are recognised**
- **Claim.** A letter in `.json`, `.txt`, `.yaml`, `.csv`, `.py` or `.MD` is not extracted, so the cell reads as "no file" and is silently skipped.
- **Artifact.** prome_gate.py:462 `_DEF_PATH`.
- **Verification.** counterex.py CE3 (`AGENTS/X/spec.json` carrying `realisation UNKNOWN`).
- **Observed.** `0 hits over 0 files`. The README one-liner shares the regex, so it misses the same letters. None exist on the live ledger today.
- **Proposed change.** Fold this into ❌1's fix: any path-like token with an unrecognised extension becomes a named unread row, not silence.

**⚠️4: FIRED-UNEXECUTED rows are out of scope**
- **Claim.** A row whose state is `FIRED-UNEXECUTED` (or any other non-`LIVE` lead) is never checked, even while its letter still carries a token. The rule says "over the LIVE rows", so the leg follows its letter. But the rule's purpose is "may not FIRE", and the leg goes silent at exactly the moment of firing. The fired-unexecuted leg BLOCKs anyway, but without the citability reason, so an operator could clear it by executing.
- **Artifact.** prome_gate.py:474; GATES_README.md L31 ("over the LIVE rows").
- **Verification.** counterex.py CE5.
- **Observed.** `0 hits over 0 files`.
- **Proposed change.** Also scan `FIRED-UNEXECUTED` rows and append the citability reason to the fired BLOCK. This is a scope question for PROME or Will, not a letter defect.

**⚠️5: A token split across a line break is missed**
- **Claim.** The leg matches only a literal single space inside the token. A hard-wrapped markdown line (`production\nUNVERIFIED`) is missed. The one-liner's line-based grep misses it too, so there is parity.
- **Artifact.** prome_gate.py:459.
- **Verification.** counterex.py CE6.
- **Observed.** `0 hits over 1 files`. A fleet-wide case-insensitive, any-separator grep finds only the exact forms (33 × `production UNVERIFIED`, 28 × `realisation UNKNOWN`) and no `realization` or lower-case variants, so the live risk is low.
- **Proposed change.** Use `production\s+UNVERIFIED|realisation\s+UNKNOWN` in the leg. Accept that the one-liner will then diverge on this edge.
- **Code-fence and commented-out occurrences.** These count as hits (fail-loud, not silent). That is acceptable under the rule's letter ("carrying"). The cost: after an owner records the attestation, a letter that keeps the historical words (`~~production UNVERIFIED~~ → attested`) keeps blocking a `LIVE —` re-cut. SPEC_LETTER_STANDARD:31 says the letter carries the query "verbatim", so the attested form will likely keep the token.
- **Proposed change.** Define an attested form (for example `production ATTESTED <date>`) that the scan subtracts, or document "remove the token on attestation".

**⚠️6: Whole-file scope attributes other sections' tokens to the gate**
- **Claim.** A `§section` pointer into a shared STATUS.md, KB.tsv or REGISTRY.tsv is scanned as the whole file. Live exposure:
  - GATE-FALCON-001 → FALCON/STATUS.md
  - GATE-CORAL-MSI-01 → CORAL/STATUS.md
  - GATE-FERT-G3 → FERT/KB.tsv
  - GATE-BRENT-COT-35B → BRENT/REGISTRY.tsv
  All four lead `LIVE —`, so any desk writing the token about a DIFFERENT letter in those files blocks PROME's boot. This fails loud (false BLOCK) and matches the one-liner.
- **Artifact.** prome_gate.py:483–497.
- **Verification.** counterex.py CE9 (the token sits in an "other thesis" section).
- **Observed.** `VIOLATIONS: G-A → AGENTS/X/STATUS.md (production UNVERIFIED)`.
- **Proposed change.** Accept it as fail-closed, but have the detail print the matching line numbers so the disposition takes one read. Longer term, owners point at dedicated letter files.

**⚠️7: The README exclusion is an exact string**
- **Claim.** `./PROME/GATES_README.md`, `PROME//GATES_README.md`, or an absolute path to the README bypass the exclusion, so the README is scanned and produces a false BLOCK (fail-loud).
- **Artifact.** prome_gate.py:461, 484.
- **Verification.** counterex.py CE7.
- **Observed.** `VIOLATIONS: G-README → ./PROME/GATES_README.md (production UNVERIFIED)`, with 2 hits.
- **Proposed change.** Compare `(root/p).resolve() == (root/"PROME/GATES_README.md").resolve()`.

**⚠️8: The column mapping is hard-coded; the one-liner looks it up**
- **Claim.** The leg uses fixed columns 3/5/10. The one-liner looks them up by header name (`h.index('definition_surface')` and so on). A column insertion in GATES.tsv would silently point the leg at the wrong cell while the one-liner adapts, so the "by-hand recompute" would stop recomputing the same thing.
- **Artifact.** prome_gate.py:477 (`r[0], r[3], r[10]`), :474 (`r[5]`); check_gates_tsv drops the header row at :539.
- **Verification.** `live_cmp.py`, header index check.
- **Observed.** Today the header gives cond 3, state 5, defsurf 10, 12 columns, so the leg is correct now. The same fixed indexing applies to the other GATES legs.
- **Proposed change.** Assert the header positions once in `check_gates_tsv` (ERROR on mismatch) instead of reindexing.

**⚠️9: The README's last sentence contradicts the new MECHANISED clause**
- **Claim.** The README still ends "Mechanising this as a `prome_gate.py boot` leg is DOCKET L417." That future-tense instruction now sits beside the new "MECHANISED 2026-09-25" clause (the finding_correction_beside_an_instruction_leaves_two_live_instructions class). The README also does not say that the one-liner silently DROPS unreachable paths (its `isfile` filter) while the leg ERRORs on them, so the two can legitimately print different totals.
- **Artifact.** GATES_README.md:31, tail of the line.
- **Verification.** `git diff -- PROME/GATES_README.md`.
- **Observed.** Both sentences are present.
- **Proposed change.** Replace the last sentence with a DOCKET L417 CLOSED/record pointer, and add "(the one-liner filters unreachable paths; the leg ERRORs on them)".

**⚠️10: ERROR rendering is visible but misleads on two points**
- **Claim, case 1 (unreachable path).** The leg records BLOCKING `ok=True` with detail `0 hits over 0 files · condition cells: 0`, so it prints a ✅ line, then a separate ERROR line.
- **Claim, case 2 (unreadable file, PermissionError).** The exception escapes the leg. Inside `guard(check_gates_tsv)` it is labelled `check_gates_tsv DID NOT RUN`, even though the six earlier GATES legs already recorded and printed.
- **Artifact.** prome_gate.py:518–524; guard at :388–399; the call sits last, at :561.
- **Verification.** errpath.py.
- **Observed.**
  - Case 1 → `[('BLOCKING', …, True), ('ERROR', 'GATES gate-citability — definition_surface unreachable', False)] rc 2`.
  - Case 2 → `ERROR 'record_gate_citability DID NOT RUN' … rc 2` when guarded directly.
  - `main()` prints `⚠️ INCOMPLETE — NOT A PASS` and `rc=2 = COULD NOT ESTABLISH` for any ERROR row (prome_gate.py:1525–1566), so the rc and the verdict are correct.
- **Proposed change.**
  - When the scan has unreachable paths, append `· N unreachable (see ERROR)` to the BLOCK detail.
  - Wrap per-file `read_text` so it becomes an unreachable entry rather than an exception, and call the leg as `guard(record_gate_citability, rows)` so the ERROR names the leg rather than its parent.

## ✅ (10)

| # | Claim | Artifact | Verification | Observed |
|---|---|---|---|---|
| ✅1 | Both suites green | test_prome_gate_citability_L417.py; test_prome_gate_gates.py | `python3 -W error::ResourceWarning -m unittest …` (each) | Ran 10 OK; Ran 7 OK; `grep -c` gives 10 / 7 |
| ✅2 | C1: a NOT ARMED lead with a token file passes and reports the hit | test `test_pass_with_hit_when_lead_is_not_armed` | suite run | `1 hits over 1 files · … (1) → G-A` |
| ✅3 | C2: a `LIVE —` lead is BLOCKING rc 1 and names the gate, file and token | tests `test_fail_on_live_lead`, `test_leg_records_blocking_on_violation` | suite run | `G-B → AGENTS/X/UNVER.md (production UNVERIFIED)`, rc 1 |
| ✅4 | C3: condition-cell hits count; non-LIVE rows are ignored on both surfaces | prome_gate.py:478–482, :474 | suite run | holds |
| ✅5 | C4: the README is never scanned when cited by its exact path; the guard is falsified by the suite | prome_gate.py:461, 484; test `test_guard_falsified_readme_prose_would_fire` | suite run | holds (see ⚠️7 for the path-spelling edge) |
| ✅6 | C5 (part): a missing `.md`/`.tsv` path gives ERROR, rc 2, and names the gate and path; a `NONE \| prose` cell is not an error | prome_gate.py:486–488, 521–524; aggregate_rc :244–250 | errpath.py | `rc 2`; main prints INCOMPLETE (see ❌1 for the directory-pointer gap) |
| ✅7 | C6 N/A is justified: one reader at boot over a committed ledger | ACCEPTANCE C6 | read | accepted |
| ✅8 | C7 output shape: count, file total and hit→row mapping; clean output = `0 hits over M files · condition cells: 0` | prome_gate.py:504–512 | CE2, CE7, CE9 outputs | holds (on a hit, N counts token occurrences while the one-liner lists files; the shapes differ only on a hit, which C7 allows) |
| ✅9 | C8 README: names PROME/GATES_README.md in the never-over-prose clause, points to the leg, keeps the one-liner | GATES_README.md:31 | diff read | holds (residue ⚠️9) |
| ✅10 | C9 live figure and parity. The README one-liner, run exactly as written from the repo root, prints `0 hits over 20 files · condition cells: 0`. `scan_gate_citability` over rows parsed the way check_gates_tsv parses them gives `0 hits over 20 files · condition cells: 0`, unreachable `[]`. The extracted path sets are identical (20 = 20, `same True`), with 18 LIVE rows and 0 short rows. The leg sits after all six other GATES records, so an exception cannot erase them. The record names are unique: grep finds no other consumer of `GATES gate-citability`. A `LIVE / NOT ARMED —` row with a CLEAN file (GATE-LIQ-079 live) is correctly not flagged, since the rule gives NOT ARMED other legitimate causes. `Path(root)/p` with an absolute path reads outside the root (CE8 read a scratch file), but it is read-only, so the harm is limited to a spurious hit. | prome_gate.py:561; GATES.tsv working tree (2 rows modified by another session, which did not affect the result) | one-liner verbatim; live_cmp.py; counterex.py CE8 | as stated |

**Counterexamples of my own:** CE1–CE10 in `counterex.py`. There are six silent misses of a real violation: CE1 (directory pointer, live-shaped), CE2 (duplicate id), CE3 (`.json`), CE4 (short row), CE5 (FIRED-UNEXECUTED, rule-scoped) and CE6 (line wrap). Three are fail-loud false positives: CE7, CE8 and CE9. CE10 (bare basename) correctly gives ERROR.
