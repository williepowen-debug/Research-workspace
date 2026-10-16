# ACCEPTANCE — BOOT step 5: the five mechanical checks run ONCE (inside the gate), never standalone as well — 2026-10-15

**Written BEFORE the edit** (PROME, session 569fac8d, 20:07 ET by `date`; the fresh window Will asked for at 19:38 ET).
Simplification plan change 1 — `PROME/plans/2026-10-15_simplification-PLAN.md` § FIRST CHANGE; backlog item 1 of
`PROME/reports/2026-10-15_waste-survey.md`. This sitting's ONE process change (WQ-299 R1; WQ-445 unruled at write time). Class: PROCESS.

## Defect, in its own terms
`PROME/BOOT.md` step 5 carries four standalone imperatives — `env_doctor.py --quiet`, `position_agreement_check.py --all --quiet`,
`corrections_boot_check.py PROME` (5b), `firetime_check.py --window 7 --quiet` — and, in the same step, the ONE-SHOT GATE
(`boot_session.py` → `prome_gate.py boot`) which runs each of them again with the same flags (verified read-only 19:36 ET 10/15:
`prome_gate.py` L1652 · L1657 · L1671 · L1683; the board scan at L1659 is already "standalone ONLY if the gate was skipped", step 6).
Two live instructions for one check is the class `finding_correction_beside_an_instruction_leaves_two_live_instructions`:
every boot either runs five checks twice (the 10/15 post-close boot did) or silently skips one copy and must report PARTIAL
(this boot did). The duplicate costs five tool calls and a second print of ~50 firetime flags per boot and carries no information
the gate's log does not.

## Acceptance conditions (properties, not the symptom)
| # | Category | Condition |
|---|---|---|
| A1 | **Ordinary** | After the edit, BOOT.md step 5 names the ONE-SHOT GATE as the single run of the five checks, lists the five by command so a reader knows what the gate covers, and says a standalone run is for a SKIPPED gate or to drill into one named flag. No other line in BOOT.md tells PROME to run any of the five standalone. (`grep -c` on each script name in BOOT.md: every hit sits inside step 5's gate bullet, step 5's reading bullet, step 6's skipped-gate clause, or § Boot-class pointer-only line.) |
| A2 | 🔴 **Overlap** | The RULES that rode on the four displaced bullets — the CAPABILITY class meanings and the "withholds only dependent work / report until RESTORED / WQ follow-up past needed-by → URGENT" clauses; position-agreement "STATUS canonical, fix the trade surface, TRY-* scope, agreement not age"; fire-time "rc=1 always means act, DATE flag = full logic re-read, expiry-dated allowlist"; corrections "rc=1 = a NAMED correction unreceipted → pointer, receipt, commit the receipts file" — SURVIVE in the manual in one place (a reading bullet), because the gate's printed lines carry only part of them (the receipt command and the DATE-flag rule are printed; the class semantics and the URGENT rule are not). Nothing is struck through; the imperatives are REMOVED, not annotated. |
| A3 | **Wrong owner** | `PROME/tools/prome_gate.py` is untouched (blocking/advisory classes and evidence unchanged): `git diff --stat` shows no change under `PROME/tools/` except this acceptance file. The root `.claude/skills/boot/SKILL.md` (Will-gated root copy) is untouched; it already carries no standalone imperative (grep 0 hits, 20:0x ET) and stays byte-identical to the PROME copy (the gate's parity check). |
| A4 | **Missing information** | The `PROME:BOOT.md-5b` anchor that `PROME/registry/READS.tsv` rows 222–224 cite still resolves: the label **5b** stays on the corrections clause so the registry needs no edit. |
| A5 | **Concurrent activity** | N/A — one PROME session on one machine (MACHINE_LOCAL); the edit is to a manual, not a shared ledger. |
| A6 | **Size** | BOOT.md is in the rotate tier (25,797 B, 79% of budget at this boot's read-cap check). The edit must not grow the file; `measure.py` before and after are recorded below. |
| A7 | **Wiring (WIRED/OBSERVED)** | WIRED = A1 holds in the file. OBSERVED = the NEXT boot's report runs the gate once, runs none of the four standalone, and does not have to name a skipped control for them (tonight's boot already showed the single-run shape but under the OLD manual, which is why it reported PARTIAL). Not claimable at this sitting. |

## Smallest reversible edit
BOOT.md step 5: four bullets (Machine capabilities · Position-agreement gate · 5b · Fire-time gate) → the ONE-SHOT GATE bullet
gains a one-sentence list of the five commands and the "never standalone as well" rule; one new bullet "Reading those five
verdicts" carries the surviving rules (A2). Step 6's BOARD clause unchanged. One read (procedure file; the Procedure exception of
`PROME/CLAUDE.md` § Review budget lets the execution check stand as the read; WQ-447: a single-artifact cold read runs on Sonnet).

## Replaces
Four standalone runs per boot (the reviewer's criterion, adopted: *what existing work does this replace?*).

## Measurements (instrument, never prose)
- before: `measure.py PROME/BOOT.md` → recorded in the commit body.
- after: same; must be ≤ before (A6).

## reads: 0

## Result
- before: `PROME/BOOT.md 25797 B · 134 lines · crc32 1913524426` (measure.py, 20:07 ET). after (pre-read): `25794 B · 131 lines · crc32 359668352`. A6 holds.
- A2–A4, A6 ✅ at the read (below); A5 N/A; A7 OBSERVED half PENDING — claimable at the next boot's report only.
- **A1 NARROWED 21:2x ET (CATO SP1, `AGENTS/CATO/runs/2026-10-15_2025_prome-simplification-oversight.md`):** A1's file-wide clause ("no other line in BOOT.md orders any of the five standalone") is **UNMET** — `BOOT.md` line 47 (the no-banner case: run the banner's checks manually) and `scripts/session_banner.sh` lines 45–46 both invoke `env_doctor.py --quiet`, so the capability check can still run beside the gate on a full boot. The disposition is the four removed step-5 repetitions only; the step-0/banner invocation is a separate, pre-existing path kept for its early-disclosure purpose, and any change to it needs its own slot and the relevant ownership boundary. INDEPENDENTLY VERIFIED applies to A2–A4, A6 and to A1 as narrowed; the wider A1 stays STILL UNRESOLVED.
- Correction to the defect paragraph, found by the reader: the old Fire-time bullet said `--quiet`; the gate runs firetime WITHOUT `--quiet` (its flagged lines are the payload). "Same flags" was therefore slightly off for that one check — the gate's run is a superset of the standalone's output, which is the plan's own wording and the reason the standalone was the redundant one.

## reads: 1
- Read 1 (coldreader, model sonnet per WQ-447, 20:08–20:10 ET; ledger scratchpad `coldread_boot_step5.md`, 14 claims, 6 counterexamples) — **RELEASE: 0 ❌ · 5 ⚠️ · 9 ✅**. Disposition: IMPLEMENTED · TESTED (acceptance greps + measure) · INDEPENDENTLY VERIFIED on A2–A4, A6 and A1 AS NARROWED (see the A1 NARROWED line above; the wider A1 is STILL UNRESOLVED) by a reader who did not write the edit; A7 OBSERVED pending.
- W1 applied after the read as a one-character fix (`scope TRY-* cards` → `scope: TRY-* cards`, restoring the old "Scope:" reading; unreviewed by construction, declared here). File after: `measure.py` in the commit body.

## Declared residue (2026-10-15 20:1x ET — the reader's ⚠️ not fixed, per `PROME/CLAUDE.md` § Read budget)
- W2: the old qualifier "(whenever live capital exists)" on position-agreement is gone; the gate runs the check unconditionally, so no behaviour changes.
- W3: the reading bullet's label "the rules the gate's printed lines do not carry" overstates — the gate does print the RESTORED line, the URGENT line, the DATE-flag rule and the receipt command (`prome_gate.py` L1896 · L1905 · L1672 · L1684); the bullet also hand-copies the gate's severities, and lists board_scan among "those five" while its rule sits in step 6. A later process slot may shorten the bullet to only the class semantics; not a meaning change tonight.
- W4: the header stamp reads "20:1x ET" — the house minute-placeholder convention, kept.
- W5 (pre-existing): step 0 line 47 tells the operator to run the banner's checks (incl. `env_doctor`) manually when no SessionStart banner prints, and the gate then runs it again. The new "never standalone as well" rule does not name that no-banner case as its exception. Candidate for the next boot-manual slot; predates this edit.
