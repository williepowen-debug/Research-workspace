# READ CAP — the fleet byte budget for boot-mandated reads (fleet build standard, P1)

**Owner:** DAEDALUS · **Ruled:** Will, in-session 2026-08-28, verbatim **"P1 approved go ahead"** — wiring-sweep proposal P1, evidence `runs/2026-08-28_WIRING_SWEEP/RUN_RECORD.md §4/§9` · **Instrument:** `scripts/read_cap_check.py --agent <NAME>` (shared; constants live there and nowhere else) · **Kin:** PAT-111 (a mandated read larger than the read instrument's cap silently degrades every boot to fragments) · PAT-086 (a line cap on a surface whose growth mode is bytes is aimed off-axis).

## The rule (STRICT — a wrong reading has a cost)

1. **Any surface a desk's boot protocol tells a session to READ WHOLE stays under the byte budget: 32,550 B** = 60% of the harness single-read cap (25,000 tokens × 2.17 B/token measured on fleet markdown ⇒ cap ≈ 54,250 B; 60% is headroom for the ratio's content-dependence and intra-session growth).
2. **The budget binds ABOVE any owner-set number.** An owner-declared budget may be tighter, never looser (TERRY's self-set 150,000 B was 2.8× the physical cap and passed its own check).
3. **Per surface, never a joint cap.** A joint STATUS+brief cap is not actionable by an owner whose brief is a NEXUS-schema surface (CARL pilot, 8/27).
4. **Owners choose HOW, never WHETHER.** Two remedies are confirmed on three seats (WATT · HENRY · CARL): **(a) two-state rotation** — verbatim, crc-stamped blocks to `archive/`, contiguous-only, never deletion (`STATUS_TWO_STATE_PILOT.md` carries the mechanism and the falsifier); **(b) hot/cold split** — a generated hot index over a cold register (`FLEET_DIRECTORY.md`/`FLEET_MAP.tsv`, `PATTERNS_HOT.md`/`PATTERNS.tsv`, `STATE_VOCABULARY.md`/`_PROVENANCE.md`).
5. **Rotation tiers:** start rotating at **≥75% of budget (24,412 B)**, stop **<70% (22,785 B)** — so a surface does not re-breach the same week (PAT-055 regrowth).
6. ⛔ **Never respond to a breach by raising the budget. The read cap is not ours to move.**
7. **A remedy leaves a DATED RE-TRIGGER, never a leanness claim** *(WALTER 2026-08-28 — `IRAN_WAR.md` line ~30 said "holds ONLY the current verified state" after a 6/28 split; the body regrew to 4.9× the cap underneath it over two months, and every reader had a written reason not to check)*. Write *"Split 2026-06-28; re-check size at any append or on 2026-09-28, whichever first"* — never *"this file holds only …"*. **The header did not become false by being wrong; it became false by being left.** A size remedy that runs once and boasts is worse than none, because it disarms the next check (`finding_header_edit_is_the_edit_most_mistaken_for_maintenance`). `read_cap_check` is the re-trigger for STATUS-class surfaces; a split file names its own.
8. **Rewriting the boot step from "Read X" to "read the header of X" is a PARTIAL fix, not a clean one** *(WALTER)*: the read becomes honest and the file drops off the whole-read list — but it is still over the cap for anyone who needs it whole. The instrument prints such files as `ℹ️ scoped read on an over-cap file` so the partial fix stays visible; the file's own owner still owes a split or a re-trigger under rule 7.
9. **Line counts are not a guard.** A line cap may stay as a style rule; it certifies nothing about readability (BOND 640 B/line · BRENT 905 · VULCAN KB 1,478).

## What binds and what does not

| Surface | Bound by this rule? |
|---|---|
| `STATUS.md` | **Yes, every desk** — root canon makes it the universal boot read |
| Any file a boot step says "Read …" whole (`THESIS.md`, `SCRATCH.md`, `MEMORY.md`, `CALENDAR.md`, a brief) | **Yes** |
| `CLAUDE.md` | **No** — auto-loaded into context, not a Read; large charters cost context, not truncation (watch, don't rotate on this rule) |
| `KB.tsv`, `LESSONS.md`, ledgers read by `grep`/scripts, archives, `*_HISTORY.tsv`, reader reports | **No** — cold/on-demand surfaces are the split WORKING; a large one is discovery, never a defect |
| `memory/auto/MEMORY.md` | **No — a DIFFERENT cap** (25,600 B auto-load, `harness_caps.env`); do not conflate the two constants (`finding_instrument_reports_clean_against_the_wrong_reference`, n=9) |

## Un-rotatable mass (open, P5 — Will's call)
Correction riders preserved verbatim IN PLACE (DELEGATION_TIER rider R2) grow STATUS monotonically on the most-correcting desks (HENRY: ~13 KB in one drain session). Whether "preserved verbatim" may mean *in the archive half with the retirement block + pointer at STATUS* is P5, not ruled here. Until ruled: rotate everything else first; a desk that is over budget on correction mass alone says so in its commit and is not in breach.

## Enforcement
- `scripts/read_cap_check.py --agent <NAME>` at boot (perimeter is a heuristic until R7-stage-2 `READS.tsv` declares each desk's read set; the check prints what it could and could not see); `--fleet` for the table. §9 rc 0/1/2.
- Blueprint REQUIRED element (market/utility/meta variants cite this file); registration checklist row at build.
- Fleet baseline 2026-08-28: **18/39 STATUS over the cap (10:30 measure); fleet boot-read tool at 13:4x: 30/37 desks with ≥1 boot-mandated read over budget, 23 over the cap** — the packets routed that day are the first tranche; the Staleness Sweep (#4 ~9/1) gains this as a grading leg.
