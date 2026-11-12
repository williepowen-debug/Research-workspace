# Read 2: the fix diff only (`71f7d26586..f5994abb89`, `new_deliveries`)

## Scope and method

- **What I read:** `git diff 71f7d26586 f5994abb89 -- AGENTS/RED/scripts/`. The only logic change is the return condition in `new_deliveries`.
  - Before: `Path(p).name not in filed`, where `filed` is the names under processed/ at the base.
  - After: `not ('/processed/' in p and Path(p).name in names)`, where `names` is every base packet's name, in the inbox or in processed/.
- **What I ran:** the same harness against both copies taken with `git show`. `my_cases_v.py` is `my_cases.py` with the script path taken from `UNDER`, plus cases N1–N4.
  - 71f7d26586: `python3 my_cases_v.py`
  - f5994abb89: `UNDER=red_read/v2/AGENTS/RED/scripts/closeout_check.py python3 my_cases_v.py`
- **Repository:** read-only throughout. The scripts directory at HEAD has no diff from f5994abb89 (VERIFIED).
- **Author's suite:** not re-run. It was not asked for, and its vintage tests need the real repository path.

## Ledger

| # | Rank | Claim | Artifact | Command | Observed | Proposed change |
|---|---|---|---|---|---|---|
| 1 | ✅ | VERIFIED: read 1 row 1 is fixed. An earlier packet that PROME files and stamps no longer delivers a later change, in either the working-tree form or the `--at` form. | fixtures R1, R1b; `new_deliveries` new return line | both runs above | R1: PASS at 71f7d26586 → **FAIL** at f5994abb89. R1b: PASS → **FAIL**. | none |
| 2 | ✅ | VERIFIED: read 1 row 2 is fixed. A new inbox packet with the same name as a filed one now counts. | fixture R2 | both runs | R2: FAIL → **PASS** | none |
| 3 | ✅ | VERIFIED: no other earlier case changed result. These match on both versions: R1c PASS, R3 FAIL, R4 PASS, R5 FAIL, R6 FAIL, R7 FAIL, R8 PASS, R9 PASS, R9b PASS, R10 FAIL, R11 UNKNOWN, R12 FAIL, R13 FAIL, R14 PASS. R1c, R4, R7, R12, R13 and R14 are the recorded residue and are unchanged by the fix. | fixtures R1c–R14 | both runs, compared line by line | identical results, except R1, R1b and R2 | none |
| 4 | ❌ | VERIFIED **new false FAIL**, a regression the fix itself creates. RED appends an addendum to its own unconsumed morning packet. That is a delivery by the author's design (case 2b, and requirement 2's "changed since the base"). PROME then files it with a plain `git mv`, with no stamp, before RED's gate runs. Requirement 3 says that move must not change the result. The packet's current path is under processed/ and its name is in the base, so it is now excluded whatever its bytes. INFERRED: this cannot be told apart from row 1's case by bytes. In both, the base holds `inbox/X` and the current tree holds `processed/X` with new bytes. The only difference is who wrote the new bytes. So the fix traded a false PASS for this false FAIL. That is the fail-closed direction, but it breaks requirement 2 combined with requirement 3. | my fixture N1 (working tree); N1b (`--at`); new return line | both runs | N1: **PASS at 71f7d26586 → FAIL at f5994abb89**. N1b: PASS → **FAIL**. Message: "no RED packet … is new or changed since HEAD". | Not another code change, because the two cases cannot be separated by content. **Disposition:** record this as declared residue in the ruling record, and state the rule that settles it: a W8 delivery is a NEW file, never an addendum to a packet already sent. Under that rule, N1 is RED's own error caught fail-closed, and the "edited while unconsumed" clause in the docstring and test 2b should say it counts only until the packet is filed. |
| 5 | ⚠️ | VERIFIED: a false PASS of the fix's own kind, present on both versions, so not a regression. PROME files the OLD packet with a rename AND a stamp. The filename test then finds no match and the bytes are new, so the old packet counts as a delivery. Both halves have happened separately: renames on filing that kept the content (R100) in 2 cases on 2026-11-06, for example `…_from-TERRY_closeout-receipt.md` → `processed/…closeout-receipt-evening2.md`, and stamps on filing in 6 cases on 2026-10-16 (read 1). Since 2026-09-01 the record has no rename and stamp in the same move (VERIFIED by `git log -M --name-status` over PROME/inbox; every name-changing rename is R100). | my fixture N2 | both runs | **PASS** on both versions: "delivered by 2026-11-12_from-RED_closeout-filed.md" | none in code. Declared residue: the filename test assumes PROME keeps the packet's name when it files it. |
| 6 | ⚠️ | VERIFIED: present on both versions, not a regression. Read 1 row 2's new same-named packet, once PROME files it over the existing `processed/X` with `git mv -f`, FAILs. INFERRED: contrived, because a plain `git mv` refuses to overwrite and PROME would have to force it. | my fixture N3 | both runs | **FAIL** on both versions | none |
| 7 | ✅ | VERIFIED neighbour: an old packet filed with a stamp plus a genuinely new inbox packet still passes, delivered by the new one only. | my fixture N4 | both runs | PASS on both; at f5994abb89 "delivered by 2026-11-12_from-RED_S64.md" alone | none |

**Counterexamples aimed at the changed condition:** N1, N1b, N2, N3 and N4 are my own. N1 and N1b found a hole that did not exist at 71f7d26586. N2 and N3 are holes of the same kind that both versions share.

❌ 1 · ⚠️ 2

On my own evidence, requirements 1 and 3 now hold for an old packet, whether moved or filed with a stamp, and requirement 2 holds for every new-file delivery. But a new hole opened in the same class: a packet that RED edited (a delivery by the design's own rule) now fails once PROME files it, where it passed at 71f7d26586. Bytes cannot separate that case from row 1's, so it needs a declared disposition rather than another code edit.
