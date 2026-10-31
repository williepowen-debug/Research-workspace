THIRD READ (read 3 of 3, the review-budget ceiling) of the WQ-295 R2 encode episode · independent reader · written 2026-10-31 14:28 EDT (from `date`)
Scope: the result read's ❌1 (COVERED alignment) and ❌2 (fail-closed gate summary) fixes, and what they could have broken nearby. Declared residue (§ 9 plan-read list, result-read ⚠️ R1–R5) is not re-graded.
Versions read: all five files were last written 14:10 ET, before this read began at 14:11. sha256 prefixes: PROME/CLAUDE.md 8c88c16b39211825 · PROME/AUTONOMY.md cedc68542dcec487 · PROME/tools/spawn_list.py a1585a78e03c40a8 · PROME/tools/prome_gate.py 24f416ee444c6dc6 · record 07c6d9e752ccab3b.
Read-only on the repository: I edited, staged, committed, stashed and checked out nothing. Fixtures, outputs and scripts are under scratchpad/wq295-third/ (listed at the end).

VERDICT
- Fix 1 (COVERED alignment): FIXED WITH RESIDUE. The 12 ❌1 desk-days now agree. A literal-reading gap remains, inherited from the WQ-184 neighbour paragraph (⚠️1), and it bites once on real data (VIOLET 10/6–10/9).
- Fix 2 (fail-closed gate summary): NOT FIXED in the defect's own terms. The reproduction (`*`) and A16's letter pass. Five ROSTER edits that keep the heading but lose the table, plus an all-git-failure case, still produce a ✅ "CADENCE-DUE: none" over zero evaluated desks (❌1).
- Overall: HOLD (1 ❌ · 4 ⚠️). The dated-row half of the gate line is unchanged and sound. At the ceiling this calls for a disposition, not a fourth read.

════════ 1. Counterexamples (my own) ════════
| # | Probe | How | Observed | Result |
|---|---|---|---|---|
| T1 | 26 constructed COVERED/GATES cases; every desk is WEEKLY and 9 days quiet | scripts/fix1_battery.py: the tool's verdict compared with the charter sentence read literally | 19 cases agree. Among them: form-valid COVERED (notes, state, paren form, overdue, at the +14 edge) → DUE; `NOT COVERED:` and `UNCOVERED` → governs; lowercase "covered by" and a backticked form → governs; one COVERED row plus one plain row → governs; COVERED plus a plain row beyond +14 → DUE; a LIVE GATES row whose text says COVERED → governs; GATES LIVE-WATCH → governs; FIRED-UNEXECUTED → DUE; desk is second owner only → DUE. 7 cases disagree: SELF-SLATE ×2, LAPSED ×2, the September form `COVERED <date> <time>:`, and COVERED in the evidence cell only (tool: governs · text: DUE); `Not yet COVERED:` (tool: DUE · text: governs) | FAILED (literal) → ⚠️1 |
| T2 | 36 real vintages, 9/26–10/31 | scripts/fix1_hist.py: each day's last-commit DOCKET/GATES/ROSTER, liveness `--until` that day | the tool gives 35 CADENCE-DUE desk-days (matches the result read), and all 35 agree with the fixed text, so the 12 ❌1 days are closed. 4 desk-days differ: VIOLET 10/6–10/9, 8–11 days quiet, governed by D:L464 (SELF-SLATE, ACTIVE) | FAILED (literal, real) → ⚠️1 |
| T3 | Live exposure on 10/31 | scan of PENDING rows | 18 form-valid annotations: 8 COVERED, 8 SELF-SLATE, 2 LAPSED. Two WEEKLY desks are governed only by SELF-SLATE rows: DAEDALUS (D:L490 "on Will's slate", 11/06) and BROCK (D:L794 "PROME spawns BROCK…", 11/02). Both are within their clock today | HELD today; exposure named in ⚠️1 |
| T4 | Text against the record | python byte-compare | CLAUDE.md L51 is identical to the § 3a quote: the only occurrence, with a blank line on each side, directly after the WQ-184 paragraph. AUTONOMY L114 (last table row) is identical to § 4b. The § 4a clause occurs once, directly after "(WQ-184 L0, change log 9/05)" | HELD |
| T5 | Against the WQ-184 neighbour | read L49 and L51 together; `git log -S` | Both paragraphs use the same qualifier for the same driver filter. Read together they are coherent: a COVERED row neither wakes a desk through WQ-184 nor blocks a cadence wake, and "LIVE GATES row at review_by" is consistent with "due by +14". The phrase entered CLAUDE.md on 10/05 (39178712a), after the 9/11 self-slate carve-out, so L49 has carried the same literal gap since then | HELD (gap inherited, ⚠️1) |
| T6 | A13's grep after the fix | grep of CLAUDE.md | "a PENDING DOCKET row or a LIVE GATES row": 0 occurrences | FAILED (record) → ⚠️2 |
| T7 | Visibility of the reworded basis | fixture: HAWK with a COVERED row due 10/12, `--as-of 10/07 --horizon 0` | C:HAWK shows "(COVERED rows do not count)" while the output reads "covered-suppressed 0: none". The row appears only at `--horizon 14` | FAILED (visibility) → ⚠️4 |
| G1 | V0: the correct 10/9 ROSTER (rev 96622a349, `--as-of 2026-10-09`) | scripts/fix2_battery.py → summarize_spawn_list | rc 0, ok False, "CADENCE-DUE: C:MARCO, C:HAWK, C:SHADE · UNREACHED: CREED, FLG · … CATO, RAV" | HELD (control) |
| G2 | V1: heading renamed (the ❌2 reproduction); ROSTER path missing (A8) | battery; CLI run with a missing path | ok False, "cadence UNKNOWN …"; the dated rows still print | HELD |
| G3 | V2: a `## Cadence by desk` heading inserted above the desk table | battery | CANNOT-EVALUATE 40, CADENCE-DUE 0, ok TRUE, "CADENCE-DUE: none · cadence CANNOT-EVALUATE: AEOLUS, BOND, …" | FAILED → ❌1 |
| G4 | V3: desk table moved below `## Transmission chain` | battery | same as G3: ok TRUE | FAILED → ❌1 |
| G5 | V4: desk-table rows deleted, header kept | battery | same as G3: ok TRUE | FAILED → ❌1 |
| G6 | V5: `## ACTIVE (34)` renamed `## LIVE DESKS (34)` | battery | 33 desks "not launchable", UNREACHED CREED, ok TRUE; all three owed wakes are gone | FAILED → ❌1 |
| G7 | V6: desk cells written as `[HAWK](../AGENTS/HAWK/)` | battery | CANNOT-EVALUATE 75, ok TRUE | FAILED → ❌1 |
| G8 | Every cadence desk returns "git log FAILED" and the dated rows are PROME-owned only (rc 0) | scripts/fix2_parse.py P16 | ok TRUE, "CADENCE-DUE: none · cadence CANNOT-EVALUATE: HANS, MIDAS, SHADE" | FAILED (less plausible) → ❌1 |
| G9 | `--tsv` runs of V0–V6 | battery | same gate verdicts as the non-tsv runs. The closeout `--tsv` run has no summarizer (ok = rc), so cadence never reaches it, by design | HELD |
| G10 | Count-mismatch forms | P5–P8, P11 | a C: row with "⚠" (no FE0F) or "🔴", a deleted C: row, or the block printed twice with n=1 → UNKNOWN; a C: row with no glyph is still counted | HELD |
| G11 | Two blocks in one body | P9, P10 | `*` first → UNKNOWN; a valid-empty block first, then `*` → ok True (the first CANNOT line wins). Contrived: the gate keeps one process per log | note |
| G12 | Desk names that look like "*"; separators inside a why string | P12, P13; code read | `read_cadence` skips cells starting with `*`, and `roster_classes` requires `[A-Z][A-Z0-9]{2,}`, so no ROSTER desk can produce `*`. A why string containing " · * " (e.g. an unknown token 'WEEKLY · * NOTE') gives a false UNKNOWN over a correct block (fails closed). "): " plus " · " garble the names shown ("ODD, C')") without changing ok | HELD (cosmetic note) |
| G13 | Dated part compared with HEAD's summarize_spawn_list | P-parity: 5 bodies × tsv/non-tsv (DARK+due · ACTIVE · UNKNOWN row · DARK+`*` · empty) | In all 10, HEAD's summary is a prefix of the new one, and new ok equals HEAD ok ∧ no CADENCE-DUE ∧ no `*`. DARK/ACTIVE ids and rc semantics are unchanged | HELD |
| G14 | Test suites | `--selftest` / `--cadence-selftest` / `--cadence-wake-selftest`; test_gate_orch_summary under a pytest shim | 11/11 · PASS · PASS. The spawn-list tests c13 and c17 pass; the one failure is my shim lacking `pytest.skip`, in an orch-closeout test | HELD |
| G15 | Live run on 10/31 | `spawn_list.py --horizon 0` | CADENCE-DUE 0 · UNREACHED CREED/FLG/RED/WAL · CANNOT-EVALUATE CATO/CYPHER/RAV · ok True | HELD |

════════ 2. Findings ════════
❌1  The gate line still reads ✅ "CADENCE-DUE: none" when no WEEKLY/MONTHLY desk was evaluated. The fix closes only the `*` form of result-read ❌2.
  claim → prome_gate.summarize_spawn_list: the fix comment and message say UNKNOWN when "no desk could be evaluated, or the block's count disagrees with its rows". Record § 9: "❌ 2 … FIXED in summarize_spawn_list (A16)".
  artifact → cadence_wakes emits `*` only when the string "## DESK CADENCE" is absent (read_cadence present=False). In three situations each desk is instead named individually as CANNOT-EVALUATE: the heading survives but the desk table does not parse, the class tables do not parse, or every git log fails. In each, there is no `*` and the counts agree, so the success branch returns `rc == 0 and not due`.
  command → scripts/fix2_battery.py (V2–V6, frozen 10/9 inputs) and scripts/fix2_parse.py (P15, P16).
  observed → V2, V3, V4 and V6 return (True, "… CADENCE-DUE: none · cadence CANNOT-EVALUATE: AEOLUS, BOND, …"). V5 returns (True, "CADENCE-DUE: none · UNREACHED: CREED · …" plus 33 names). The same inputs with the ROSTER intact owe C:MARCO, C:HAWK and C:SHADE. The gate marks ok lines ✅. A16's letter holds, but A16 restates the symptom (`*`), not the property, which is what WQ-229 asks acceptance conditions to state.
  proposed change → key the UNKNOWN on "no launchable WEEKLY/MONTHLY desk reached the clock test" rather than on the `*` token. Either cadence_wakes appends ("*", "cadence section present but no WEEKLY/MONTHLY desk evaluable") whenever the section is present and nothing reached the clock test, or the header prints "evaluated N" and the summarizer returns UNKNOWN when N = 0. Pin V2–V6 and P16 as fixtures. Any such fix lands after the final read, so it must be reported as unreviewed.

⚠️1  Fix 1's text and the tool still disagree wherever a form-valid COVERED annotation does not suppress the row, and in the one reverse case.
  claim → CLAUDE.md L51, AUTONOMY L114 and § 6 define an open dated row as "a PENDING DOCKET row not annotated COVERED, or a LIVE GATES row".
  artifact → the tool's governing set is collect(+14d), which drops only rows whose coverage() reason is COVERED. Rows that keep governing: SELF-SLATE and LAPSED annotations (both form-valid under L368 A1), the September form, and annotations outside the state/notes cells. L368's own vocabulary separates the annotation form (A1) from suppression (A2–A4).
  command → scripts/fix1_battery.py; scripts/fix1_hist.py; the live-exposure scan.
  observed → 7 of 26 constructed cases disagree (T1).
    · Real data: VIOLET, 10/6–10/9. D:L464 reads "PENDING (COVERED: VIOLET's next post-close boot …)", a genuine owner coverage. It scores SELF-SLATE only because the clause runs on into the notes cell's "WQ-184 driver" (L368's declared ⚠️5). The text therefore says CADENCE-DUE; the tool says L464 governs, and L464 is ACTIVE, so VIOLET is woken by no path (the result read's ⚠️ R2 case).
    · Live 10/31: DAEDALUS (L490) and BROCK (L794) are exposed but within their clock.
    · The neighbour L49 has carried this gap with the same filter since 10/05, so L51 reads correctly as that neighbour's term of art ("suppressed by coverage()"). § 2's "COVERED-suppressed rows excluded" is the precise reading.
  proposed change → no canon edit (the one further edit is spent). Declare in § 9 that "annotated COVERED" in §§ 3a, 4b and 6 means "suppressed by spawn_list.coverage() (reason COVERED)". List the seven forms and the VIOLET 10/6–10/9 bite, and take them to Will together with the COVERED reading that is already going to him. At the next charter touch, write "not suppressed as COVERED by the driver".

⚠️2  Record § 7 A13 now fails its own grep. Its third verbatim phrase, "a PENDING DOCKET row or a LIVE GATES row", no longer occurs because the ❌1 fix inserted "not annotated COVERED,". § 9 still says "A13 present", which was true only before the fix.
  proposed change → amend A13 to "a PENDING DOCKET row not annotated COVERED, or a LIVE GATES row (amended at the ❌1 fix)".

⚠️3  The summarize_spawn_list docstring still says "ok follows rc exactly as before". Since this change, ok is False at rc 0 in three cases: CADENCE-DUE exists, the block is missing, or the cadence state is UNKNOWN. The old sentence now sits beside new behaviour that contradicts it.
  proposed change → replace that sentence.

⚠️4  The reworded C: basis "(COVERED rows do not count)" and the UNREACHED header point at rows the boot output may not show. covered-suppressed is printed only to the run's horizon (0 at boot), so a COVERED row due in +1 to +14 days, which the cadence wake discounted, appears nowhere (T7).
  proposed change → print COVERED rows out to +14 inside the cadence block, or name where to look (`--horizon 14`).

════════ 3. Verdicts ════════
- Fix 1 (❌1, COVERED alignment): FIXED WITH RESIDUE (⚠️1, ⚠️2, ⚠️4). Text and record match byte for byte, the 12 real desk-days that disagreed are closed, and the paragraph reads coherently against L49.
- Fix 2 (❌2, fail-closed summary): NOT FIXED. The `*` reproduction, the A8 path, the count mismatch and dated-part parity all hold, but the defect's property still fails on V2–V6 and P16 (❌1). ⚠️3 also applies.
- Overall: HOLD. The cadence half of the gate line can still certify ✅ "none" over an empty evaluation on plausible ROSTER edits. The dated rows, rc and the slate are unaffected.

════════ Evidence (scratchpad/wq295-third/) ════════
scripts/fix1_battery.py · scripts/fix1_hist.py → fix1_hist.txt · scripts/fix2_battery.py → fix2_battery.txt · scripts/fix2_parse.py → fix2_parse.txt · fx/roster_1009.md, fx/roster_variant_V0–V6.md, fx/out_V*.txt (each also `_tsv`), fx/out_missing_roster.txt, fx/out_1007.txt, fx/docket_cov_future.tsv, fx/out_cov_future.txt · head/prome_gate_head.py (a HEAD copy used only for parity) · shim/pytest.py · selftest--*.txt · live_h0.txt
