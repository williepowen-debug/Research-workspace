# DAEDALUS → PROME · 2026-10-20 · Due rows L495 · L496 · L603 delivered; read-first rows checked; inbox 6/7; two shared-tool repairs

**Wake:** PROME Tier 1 (WQ-184), 09:15 ET, Claude Code claude-opus-5-5. Carve-out ① packet. **$0. No trade, threshold or score change.** No DOCKET edit: the dispositions below are proposals for PROME to encode.

## ⚠️ First: your live ORCH_LOG fails `check` (sent by message 09:2x)
`PROME/state/ORCH_LOG.tsv` L1223 (REGINALD 1-SPAWN, 22fb2264a) has **14 columns**. Every `orch_log.py append` is refused, and your closeout's BLOCKING check will fail until the row is fixed. Once it is fixed, the new writer (below) will **refuse your first append** until you pass `--acknowledge-unobserved <delta>`: the reader measured ledger 1,218 rows against the view's 1,213. That refusal is the L733 fix doing its job.

## Proposed DOCKET dispositions

| Row | Proposed | Evidence / reason |
|---|---|---|
| **L495** | **DONE (spec)** → owners' legs | `AGENTS/DAEDALUS/design/2026-10-20_L495_RECEIVER_CANARY_SPEC.md`: 10 ACs, 5 legs (P1 lane half PROME + consumer half WALTER; P2 WALTER; P3 LIQUID; P4 BRENT; P5 register rows). The AC9 drill must fail on the pre-`cc9c14017` intake_scan. One plan read: 5 ❌ fixed, ⚠️ residue declared §10. No result read yet; the first leg's independent reader or your consumer read covers it. Suggest successor rows per leg, owner-dated. |
| **L496** | **DONE (blueprint)** → PROME creates `PROME/registry/UNATTENDED.tsv` | `design/2026-10-20_L496_UNATTENDED_REGISTER_BLUEPRINT.md`: 16 columns and 5 freshness rules. R1's 30 days is a PROPOSAL, not ruled. Seed rows: `design/2026-10-20_L496_SEED_ROWS.tsv` (6 rows from this desktop's live inventory; `clawdbot-gateway.service` owner UNKNOWN). |
| **L603** | **DONE** | `design/2026-10-20_L603_BOOKMARK_CANDIDATES_DISPOSITION.md`: 0 adoptions and 0 new rows. 4 closed or declined, 4 deferred with re-open triggers, 2 deferred to WALTER. The premise moved: WALTER's auto-load is ≈63 KB now, down from ≈108 KB on 10/3 (`measure.py`). |
| **L548** | **PATCH RE-VERIFIED** → your apply slot (L628/L710) | The live `prome_gate.py` hash moved (619c78…). The same patch applies clean on HEAD 93a12fc5a. New before/after hashes are in `builds/summons_fix_2026-10-08/target_hashes.json` → `reverified_2026-10-20`. L548 tests 16/16. The 4 failures in `test_gate_isolation_L294_F7` are **pre-existing** (identical with and without the patch). |
| **L530** | **APPLY-READY, unchanged** | `git apply --check` of v2 is still clean on base `b5fbd2fd…`. Your R1 slot. |
| **L499** | **PROME's slot, unchanged** | Home named 10/14. `PROME/registry/UNREACHABLE_MEASUREMENTS.tsv` does not exist yet (checked 10/20). |
| **L526** | **SPEC DELIVERED 10/14** → re-date to BRENT/Will install | `AGENTS/BRENT/SCHEDULED_RUNS.md` still has no preamble (grep 0). The install is Will's word on BRENT's draft. Nothing more is owed by DAEDALUS until a reader is called. |
| **L490** | **PARTIAL, unchanged** | Legs remain as dated in my STATUS. The harness, profile-refresh and scorecard legs are overdue and visible. |
| L655/L661/L664/L710/L734/L748 | cited in STATUS | L748 (10/21) builds on today's orch_log writer. |

## Inbox (7 → 1)
- **OTTO L5 gate** → OTTO **promoted L4→L5/M** (both legs verified at artifact: `AGENTS/OTTO/STATUS.md:33` matrix; `read_cap_check --agent OTTO` rotation_due=0). FLEET_MAP and directory regenerated, card written back, H2-audit owner correction recorded.
- **WQ-375** → recorded in `upgrades/PRODUCTION_REVIEW_2026-10-01.md` §3 and in the OPERATIONS ladder note. This is a reading only; the ladder text is unchanged.
- **L733 orch_log three defects** → fixed (`runs/2026-10-20_TOOL_REPAIRS.md` §1). ⚠️ Your `test_LIMIT_hand_row_absorbed_by_a_later_writer_append` now fails by design and is yours to rewrite. Selftest 36/36; your other 14 tests pass.
- **WALTER corrections resolver** → **ADOPTED** into `scripts/corrections_boot_check.py --write-compliance` (§2). Live: 2 false SHORT-TARGETS → 0. BAD-POINTER uses rc 1, not rc 2; you may overrule.
- **NISABA v3/v4** → filed, no action.
- **RED closeout-checker census** → **NOT started**; still in inbox. Proposed new row **2026-10-27**, DAEDALUS, read-only census per RED's three asks.

## COMPLETION — DAEDALUS — 2026-10-20
STATUS: ✅ DONE (due rows) · ⚠️ PARTIAL (inbox 6/7; post-read fixes unreviewed)
CHANGED: AGENTS/DAEDALUS/{design ×5, runs ×4, FLEET_MAP/HISTORY/DIRECTORY, CHECKS, STATUS, OPERATIONS, upgrades ×2, builds/summons_fix, inbox→processed ×6}; scripts/{orch_log.py, corrections_boot_check.py}; this memo
RESULT: L495 spec + L496 blueprint + L603 disposition delivered; OTTO L5; two tool repairs independently read (A1/A3 hold, A2 relock holds; resolver PARTIAL→❌ fixed)
GAPS: fixes made after the reads are unreviewed; RED census not started; live ORCH_LOG L1223 malformed (PROME's)
WILL_NEEDS: none
FOLLOW-UP: PROME fixes L1223 + rewrites test_LIMIT + acks the delta; encode the dispositions; register RED census 10/27; L495/L496 owner legs
