# Spine audit #16 — 2026-10-15 (WQ-411 RULED APPROVE by Decision Deck tap 12:00 ET; PROME prome-81)

**Run:** `PROME/tools/spine_audit.workflow.js`, Workflow run `wf_19d31414-f00`, 9 readers (8 spine + 1 DOCKET anchor sampler), 17 files, ~5.4 min, 1.28M subagent tokens. Raw result (every reader's return, verbatim): `RESULT.json` in this directory. Stamp: `PROME/STATUS.md` header; the displaced #15 stamp → `PROME/archive/STATUS_SPINE_AUDIT_PRIORS_2026-10-02.md`.

## Blocking (6) → fixes, all in PROME's lane, same session
| # | File · find | Fix (delete-and-point) |
|---|---|---|
| 1 | `PROME/CLAUDE.md` — the WQ-348 "Done without asking" guard had NO step in BOOT.md step 8, CLOSEOUT.md § Delivery or either runner | BOOT.md step 8 and CLOSEOUT.md § Delivery summary now carry the "Done without asking" line (each C1–C7 act with its commit, or *none*) and the SKIPPED-controls line (headline PARTIAL); both runners point at them; root/PROME skill copies byte-identical |
| 2 | `PROME/CLOSEOUT.md` step 11 still read "the HELM keeps this rule until WQ-382 (b) is ruled" — (b) was RULED B on 10/9 | Step 11, Pre-closeout item 4 and the symmetry row now say: Deck OWED at every Standard+ closeout; the HELM only on Will's word or at a spine audit; Fleet-Ops panels FOLDED (L594). DOCKET L665 + L594 RESOLVED |
| 3 | `PROME/SCRATCH.md` hand lines treated WQ-365/404/411/413 as OPEN after the 12:00–12:03 taps | Lines rewritten from WILL_QUEUE (ruled set + the F2 closures); `{now}` placeholder replaced; the 30th-base bullet re-pointed to the 31st plan |
| 4 | `PROME/SCRATCH.md` DOCKET-VIEW stale (L615/L700 shown live) | `docket_view.py --write` regenerated; `--check-generated` rc=0 |
| 5 | `PROME/ACTIVE_DECISIONS.md` TERRY row carried a WQ-365 revival condition the card denies | Clause replaced with the DECLINE ruling; the broker paragraph re-based to the 10/15 capture; two pointers re-pointed (TERRY packet → processed/; CORAL next grade) |
| 6 | `PROME/DOCKET.tsv` L723 named CREED as a WQ-184 driver — an explicit-permission desk (ROSTER L124/L262) | Owner/state cells now say NOT a WQ-184 driver: PROME reads the 10/28 outcome and asks Will before any CREED launch |

## Minors fixed in the same round
'Chunk 4' section labels → '§ The routine step 10' (GIT_COORDINATION.md ×2, SYSTEM.md ×2) · CLOSEOUT.md step 8 + closeout runner: L473 → L488 as the live cell · CLOSEOUT.md step 7/symmetry: `PROME/BRIEF.md` / `PROME/HANDBOOK.md` path-qualified · BOOT.md header stamp (the 10/09 step-3b rule change named) · STATUS position row re-based to the 10/15 capture · HEARTBEAT amendment #1 (WQ-365 DECLINE; 'since 10/1'; the CFTC date's source) with its companion projection.

## Minors declared, not fixed this round (owner · class)
- Header-stamp ride-under: AUTONOMY.md (10/04 and 10/14 rows), MACHINE_LOCAL.md ("through 9/22" claim; undated desktop safeguards cells), GIT_COORDINATION.md (10/03 edit) — stamp reconciles at their next touch.
- ≥280 vs >280 operator carry in ACTIVE_DECISIONS rows L34/L35 (the Bank-put row already declares the mismatch as the OPEN CATO item) — carry the strict letter at the next rotation.
- ACTIVE_DECISIONS row-size debt (TERRY row 4,731 B vs the ≤2 KB target; Post-FOMC 3,317 B; CORAL 2,210 B) — the 10/10 rotation already records the snapshot-then-rewrite step as owed.
- BOOT.md step 5 bullets do not say they already run inside `prome_gate.py boot` (and the gate runs firetime without `--quiet`) — one clause at the next BOOT touch.
- PROME/CLAUDE.md FREEZE header's "carries a consolidation PROPOSAL" is dated phrasing (WQ-371 RULED 10/8; C4 fold unencoded — DOCKET L647 owns it).
- Pre-closeout item 5 / § Delivery overstate `check_publication_prereqs` (it checks explainer coverage only; viewed/listed legs are judgment) — one clause.
- AUTONOMY.md: the narrow-C8 grant (WQ-369) lives only in the change log; DOCKET L644 (charter propagation) is past date — carried, fail-safe direction.
- DOCKET pointer rot into inbox/processed/ (L342, L701), L606 source cell empty, L155 notes vs status readings — hygiene at the next DOCKET pass.
- SYSTEM.md runtime wording predates WQ-385 — on-demand file; next SYSTEM touch.
- HANDOFF.md: three mentions of the 31st re-base as owed, 'ARGUS L678' as open, '03:08' vs the 03:28 restart — reconciled at this session's closeout per the Handoff Requirement.
- MACHINE_LOCAL.md VIRGIL cell restates assessment detail the ROSTER says lives in its own charter — trim at next touch.
- closeout runner step 2 label under-names 1c-bis / 1d-bis; step 6 names none of step 11's three trigger-gated conditions — runner depth, next runner touch.
- HEARTBEAT §Book/§Thresholds WQ-365 cells — superseded by amendment #1 (not re-written in the base; owner surface wins by its own rule).

## Process note
The fix round is the audit's own (WQ-411 APPROVE); the encodes of WQ-348's guard and WQ-382 (b) are RULED items landing late, not new process. Reads: none beyond the audit's readers (fixes are delete-and-point at rows the readers quoted verbatim); the re-run of `docket_view.py --check-generated` and the skill-parity diff are the mechanical checks.
