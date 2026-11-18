# Read-cap checker, desk-charter ceiling 50,000 B — acceptance record and review (WQ-701 A2)

**Written:** 2026-11-18 10:3x ET · DAEDALUS, Claude Code Opus 5.5, desktop · **Subject:** commit e334fb1c15 (`scripts/read_cap_check.py`, +84/−5), built 11/16 ~23:33 ET against PROME packet 9e02c0d712 (C11), committed unreviewed on Will's word 11/17 19:13 ET to unblock a pull. **Authority for this review:** Will "ok go" 2026-11-18 10:18 ET to the boot report's order.

⚠️ **Order disclosure.** PROME's packet required acceptance conditions written BEFORE the edit. They were not: the build happened 11/16 with no written conditions, and this record writes them on 11/18 after the code is on origin. The conditions below are taken from PROME's packet text, not shaped to the code, and the live cases were run before they were scored.

## Acceptance conditions (from PROME's packet, verbatim in substance)

| # | Condition | Source |
|---|---|---|
| A1 | Explicit mode: a desk's own `AGENTS/<NAME>/CLAUDE.md` graded at 50,000 B | packet "The shape" 1 |
| A2 | Explicit mode: root `CLAUDE.md` and `PROME/CLAUDE.md` stay at 32,550 B | packet "The shape" 1 |
| A3 | Default mode: one advisory line `CHARTER-OVER-CEILING` for a desk charter over 50,000 B; never rc-driving | packet "The shape" 2 |
| A4 | No other behaviour changes | packet "The shape" 3 |
| A5 | Over case and clean case both shown | packet Conditions 1 |
| A6 | Neighbours considered: a sub-agent charter, root, PROME's charter, a desk with no charter | packet Conditions 1 |
| A7 | Sub-agent charters: the checker does not grade them at either number until Will rules | packet Conditions 3 |
| A8 | One independent reader with a counterexample of its own before it is called fixed | packet Conditions 2 |

## Live cases (2026-11-18 ~10:25 ET, HEAD 208bd704ea; raw output in session scratchpad, figures below copied from it)

| Case | Charter bytes | Mode | Verdict on charter row | rc | Meets |
|---|---|---|---|---|---|
| LABOR | 55,603 | explicit | 🔴 OVER THE CAP (102% of 54,250 B cap) | 1 | A1 (cap still binds, unchanged) |
| OSPREY | 55,293 | explicit | 🔴 OVER THE CAP | 1 | A1 |
| FALCON | 51,484 | explicit | ⚠️ over ceiling by 1,484 B, ADVISORY | 0 | A1, A5 over case |
| AEOLUS | 50,695 | explicit | ⚠️ over ceiling by 695 B, ADVISORY | 0 | A1 |
| CARL | 49,162 | explicit | ✅ 98% of ceiling | 0 | A1, A5 clean case |
| DAEDALUS | 16,617 | explicit | ✅ 33% of ceiling | 0 | A1 |
| PROME | `PROME/CLAUDE.md` 28,021 | explicit | 🟡 86% of budget (graded at 32,550) | 0 | A2 |
| root `CLAUDE.md` | 24,449 | explicit (every desk) | 🟡 75% of budget, rotation_due counted | — | A2 |
| FALCON | 51,484 | default | charter line carries `⚠️ CHARTER-OVER-CEILING: 1,484 B over` | **1** | A3 line present — but see F1 |
| CARL | 49,162 | default | no ceiling line | 0 | A3 clean case |
| STUE (CARL sub-agent) | 47,588 | explicit | 🟠 146% of budget (graded at 32,550) | **1** | **A7 NOT MET** — see F2 |
| Self-test | — | `--selftest` | 137/137 legs pass | 0 | — |

Desk with no charter (A6): CATO and RAV have no `CLAUDE.md`; not run live this pass (left to the reader).

## Findings (own)

- **F1 — the ruling is applied only in explicit mode; the modes desks actually run still grade a declared desk charter at 32,550 B.** Three desks declare their own charter as a `whole` read in `PROME/registry/READS.tsv` and sit above 32,550 B: HOMER 41,649 · AEOLUS 50,695 · FALCON 51,484. In default mode FALCON's charter row is 🟠 "158% of budget", rc 1, while the same file in explicit mode is ⚠️ advisory, rc 0. HOMER's own closeout runs `read_cap_check.py --agent HOMER` (default mode, `AGENTS/HOMER/CLAUDE.md:222`), so HOMER is blocked at 32,550 B on a 41,649 B charter that Will's ceiling allows. `--fleet` (used by `validate_all.py`) is default mode too. This matches PROME's shape A4 ("no other behaviour changes") and contradicts root § Data Hygiene ("for a desk's `AGENTS/<NAME>/CLAUDE.md` the ceiling is 50,000 B, in place of 32,550 B"). The shape was mine; the gap is mine.
- **F2 — A7 is not met.** A sub-agent charter read explicitly (STUE) is still graded at 32,550 B, rc 1 — the pre-change behaviour. A7 ("graded at neither number") and A4 ("no other behaviour changes") conflict for this case: meeting A7 changes STUE's rc from 1 to 0. The code chose A4 silently; its comment says sub-agent charters "keep BUDGET_BYTES".
- F3 (minor): A8 was not met at commit; this record is where it is met.

## Independent reader

One Opus reader, given the code, the packet and the rule text, not this record's findings. Ledger copied verbatim to `runs/2026-11-18_READ_CAP_REVIEWER_LEDGER.md` (21,345 B, ends `END OF LEDGER`). **Verdict: REJECT as "fixed" in the committed state; no revert needed.** Its own counterexamples: per-hunk mutants (9 of 11 caught; the two that escaped moved the exact 50,000 B and 54,250 B boundaries), path forms (`./`, symlinked root and desk: handled), CATO/RAV rc 2 unchanged, a 45-desk default-mode before/after diff (0 differences), and a `prome_gate` feed.

| Reader finding | Severity | Disposition (2026-11-18) |
|---|---|---|
| Docstring "Will chose a warning, not a block" has no source; on that basis explicit mode stopped failing a charter between 50,000 and 54,249 B (AEOLUS, FALCON flipped fail → pass) | ❌ | **CONFIRMED and FIXED.** Ruling record checked: no such choice; root says the charter "stays under 50,000 B", "in place of 32,550 B". Over the ceiling is now 🟠 over budget, rc 1. Attribution removed and the correction stated in the docstring. My error: an unsourced attribution to Will that loosened a gate |
| `PROME/tools/tests/test_boot_charter_coverage.py:124-131` fails (`0 != 1`): expects a 32,551 B desk charter to fail in explicit mode | ❌ | CONFIRMED, still fails after the fix, by design: under Will's ruling 32,551 B is under the charter ceiling. PROME's file: packet asks PROME to update the expectation (e.g. to 50,000 B) |
| Sub-agent charters still graded at 32,550 B (STUE 47,588 B rc 1); the code settled the A4/A7 conflict silently | ❌ | CONFIRMED (F2). Not changed. The code comment now names the conflict; PROME rules which condition wins |
| A desk charter declared in READS.tsv is graded at 32,550 B in default/injected/fleet mode — same file, two verdicts (15 desks declare their own charter) | ⚠️ | CONFIRMED (F1). Not changed (packet A4). Put to PROME with a conditional offer to build |
| Over-cap charter yields `over_budget=1 rotation_due=0`, tripping `prome_gate`'s order check | ⚠️ | FIXED: a desk charter counts rotation-due at or over its ceiling. CH9 asserts `over_cap ≤ over_budget ≤ rotation_due` |
| `READ_CAP.md` rule 20 still says no instrument applies 50,000 B | ⚠️ | FIXED (lines 32 and 40) |
| Default mode says only "over the ceiling" for a charter that cannot be read whole (LABOR, OSPREY) | ⚠️ | FIXED: the line adds "and over the 54,250 B single-read cap, so it cannot be read whole" (CH8) |
| Exactly 50,000 B printed "over the ceiling by 0 B"; header says all % are of budget | ℹ️ | FIXED: "at or over the ceiling (+0 B)"; header names the charter-row exception |
| Comment "each CH leg watched FAILING on the pre-change file" overstated | ℹ️ | FIXED: comment now says which legs fail there |
| No 75% rotate tier for charters under the ceiling | — | Kept; stated as DAEDALUS's reading (the ruling names a ceiling, no band), put to PROME |

## Correction build (2026-11-18, uncommitted at writing; commit named in the packet)

- Self-test **140/140** (was 137; +CH7 boundaries 49,999 / 50,000 / CAP−1 / CAP, +CH8 default over-cap text, +CH9 gate order). CH2 now expects rc 1.
- **Mutants, each watched failing:** M1 restore the rc-neutral ⚠️ band → CH2, CH7 fail (138/140) · M2 ceiling `>` for `>=` → CH7 (139/140) · M3 cap `>` for `>=` in the charter grader → CH7 · M4 old rotation_due → CH2, CH9 · M5 drop the cannot-be-read-whole text → CH8.
- **Live, explicit mode:** FALCON 51,484 B rc 1 · AEOLUS 50,695 B rc 1 · LABOR 55,603 B rc 1 over_cap 1 · CARL 49,162 B rc 0 · PROME rc 0 (unchanged) · DAEDALUS rc 0 · HOMER rc 1, from its `thesis/THESIS.md` 33,312 B (102% of budget), not the charter (✅ 83% of ceiling).
- **Callers:** `daedalus_gate.py` closeout maps rc 1 → BLOCKING, so FALCON/AEOLUS/LABOR/OSPREY charters fail their explicit-mode runs until trimmed. That is the pre-build behaviour for them, now at the right number. The desks' trims are already owed (WQ-701 A2 follow-through; the outside review's item H).

## Open for PROME (packet)

1. Sub-agent charters: A4 (no change, 32,550 B) or A7 (graded at neither number)?
2. Declared desk charters in default/fleet mode: grade at 50,000 B too (one-line change; HOMER's default-mode closeout would stop failing on its charter)? Offered as conditional: "if yes, build it with the same review".
3. PROME's own test expectation (above).
4. No rotation band under the ceiling: confirm or rule.

**Diff-only follow-up read (fresh Opus reader, 2026-11-18 ~10:37 ET):** **ACCEPT-WITH-RESIDUE**, no ❌. Ledger copied verbatim to `runs/2026-11-18_READ_CAP_FOLLOWUP_LEDGER.md`. Selftest 140/140; its own mutants (rotation_due revert → CH2, CH9; text removal → CH8; `>` for `>=` → CH7) all caught. Counterexamples: a charter declared AND read explicitly is one row (49,999 ✅ rc 0 · 50,000 and 54,249 🟠 rc 1 · 54,250 🔴); `prome_gate.summarize_read_cap` accepts over-cap, 50,000 and 49,999 results (the pre-correction file would have raised on a charter-only over-budget desk); quiet mode clean; 98 real-repo runs before/after: machine lines changed only in explicit mode, only for the four charters over 50,000 B (AEOLUS and FALCON rc 0 → 1; LABOR and OSPREY +1 rotation_due); default mode unchanged; `--fleet` four advisory-text lines. Residue: ⚠️ F1 (declared charter graded at budget in default mode; AEOLUS's line said "rc unchanged" while that row drove rc 1 — wording corrected to "this advisory does not change rc (a charter DECLARED as a whole read is still graded at the budget in this mode)", selftest 140/140 after); ℹ️ cosmetics (the explicit-mode summary line for a 🔴 charter does not repeat "cap"; 49,999 B rounds to "100% of ceiling"; header suffix prints on every run).

**Verdict after correction:** ACCEPT-WITH-RESIDUE. The three first-review ❌ items: one FIXED (the unsourced attribution and the loosened gate), one routed to its owner (PROME's stale test), one awaiting PROME's ruling (sub-agent charters).
