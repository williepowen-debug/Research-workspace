# R1 resolver repair — independent result read (corrections_boot_check.py `--write-compliance`)

**Read:** 2026-10-20 · working-tree file vs `scratchpad/cbc_before.py` · repo read-only; fixtures under `scratchpad/reader2/` (harnesses `reader2/rowdiff.py`, `reader2/ce.py`).
**Verdict: PARTIAL.** The live result holds. One latent ❌ in the silent direction, plus five ⚠️.

## Live old vs new, row by row (`reader2/rowdiff.py`, live BOARD + CORRECTIONS.tsv, since 2026-10-08)

| Old → new | Rows |
|---|---|
| unchecked → checked (3) | SIG-W-20261012-025 (corrects 20260828-009), SIG-W-20261014-036 (→20261012-019), SIG-W-20261019-007 (→20261015-020). Each had a frontmatter `corrects:` but no `-to-` filename. Each original is on BOARD and nothing is missing. |
| checked → checked, different original (2) | 20261015-005: same-day 014 → **20261014-018**. 20261015-006: same-day 012 → **20261012-035 + 20261014-006**. This is the 10/16 defect fixed, and both now cover their targets after WALTER's repair. |
| checked → unchecked | **None.** VERIFIED: all 15 old-checked rows are still checked. |
| unchecked in both (15) | All 15 have `corrects: EXTERNAL: …`. Correct by design. |

Old rc=1 (2 SHORT-TARGETS) → new rc=0, with 18 checked and 15 not checkable. This matches the author's claim. `--selftest`: 58/58 PASS.

## Ledger

| id | | claim | command | observed | fix |
|---|---|---|---|---|---|
| CE1 | ❌ | A malformed explicit pointer is not silently dropped | `ce.py` CE1 `corrects: sig-w-20261014-018` and CE1b `corrects: SIG-W-1014-018`, filename `-to-20261014-018`, targets BROCK | old: rc=1, SHORT REGINALD. **new: rc=0, row moves to "not checkable"**, and the valid full-date filename is ignored | This is the silent direction (false-clean). Treat a value as explicit-nonsignal only when it starts with `EXTERNAL:` (every live non-signal value does). Any other value with no valid id, or matching `/sig-w/i` without a valid id, → BAD-POINTER. Latent: no live row has this today. |
| CE2 | ⚠️ | "Explicit first" covers YAML forms | CE2: `corrects:` followed by `  - SIG-W-20261014-018`, filename `-to-014` | The block list is not parsed. `corrects` comes back empty, so the code falls back to the filename and checks the **wrong original** (same-day 014). This is the defect class being repaired. Old behaves the same. | Read block-list lines, or treat an empty `corrects:` key as BAD-POINTER. 0 live empty `corrects:` lines (grep). |
| CE3 | ⚠️ | Packet acceptance "overlap = a correction that corrects a correction" | CE3: C2 corrects C1, and C1 corrects O | Required = C1 ∪ C2 recipients. O's recipients are **not** required (non-transitive). The author's R1c tests two originals, not this case. | Decide and record whether it should be transitive, and add a fixture. The case the packet named is untested. |
| CE4 | ⚠️ | The union only adds real recipients | CE4: correcting `info: [ALL]` · CE4b: correcting `info: [HANS]`, targets BROCK,REGINALD | Both now rc=1. CE4 reports "not targeted: **ALL**". CE4b flags the FYI-only HANS. The message still says "**received the wrong figure**" about correcting-only desks. | The union is by design (WALTER's shape), and no live row is affected (0 ALL routings in the window). Fix the message wording, and map an `ALL` recipient to "targets must be ALL". |
| CE5 | ⚠️ | The filename fallback is "unambiguous only" | CE5: `-to-014-and-20261014-018-x.md`, no frontmatter | Resolves to 014 only. 018's recipients are silently left out and the row counts as **checked**. Old behaves the same. | The lookahead should also reject `-and-`. Alternatively, mark any `-to-…-and-` form unresolved. |
| CE6 | ⚠️ | `corrects:` comes from the leading frontmatter | CE6: frontmatter not closed, body line `corrects: SIG-W-20261013-099` | Body text is read as frontmatter, giving BAD-POINTER "frontmatter `corrects:`". This fails loud and the 80-line parse is pre-existing. | Ignore `corrects` when `closed` is False. |
| CE7 | ⚠️ | Header counts are accurate | CE7: a single BAD-POINTER row | The header says "**1 row(s) target-checked**, 0 not checkable", but nothing was checked. `ok_rows - unresolved` includes the bad_pointer rows. | Subtract `len(bad_pointer)`. |
| P1 | ⚠️ | Matches the acceptance shape in the packet | packet line "explicit pointer that resolves to no file ⇒ rc=2" vs code | The code returns **rc=1** (OWED) with BAD-POINTER. It is defensible, since the pointer is fixable, but it differs from the shape and I found no recorded rationale. | Record why rc 1 in the DAEDALUS disposition packet. |
| CE8 | holds | Quoted/space list variants | `corrects: ' SIG-W-20261014-018 ,SIG-W-20261015-014'`, `signal_type: "correction"` | Both ids resolve, the union is enforced, and ZHAO is flagged | — |
| CE9 | holds | Body ids are not read as pointers | Body says "corrects SIG-W-20261014-018", filename `-to-014` | Same-day 014 is used and the body id is ignored | — |

## Completion state
IMPLEMENTED · TESTED (author 58/58) · this read: live behaviour VERIFIED. **CE1 is STILL UNRESOLVED** and is a latent false-clean path. Do not call the repair verified until CE1 is fixed and has a fixture. CE2 and CE5 are pre-existing defects in the class this repair targets, so they are worth folding into the same episode.
