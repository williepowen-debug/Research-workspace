# HAWK -> PROME: crash-recovery closeout of the 2026-09-16 cross-war oil synthesis

Date: 2026-09-17 ~08:3x ET. Session: PROME-spawned Tier-1 recovery (`prome-ae`, Claude Code) inside the approved cross-war oil workstream, commission `e4b198a71`. Basis read first: `AGENTS/CATO/runs/2026-09-16_2149_crash-recovery.md`. No trade, band, threshold, confidence or standing approval changed; the commission is closed.

## What was committed (exact-path commits, from the repo root)

| Commit | Content |
|---|---|
| `b28680b9e` | 19 paths: final report `research/2026-09-16_cross-war-oil-review.md` (WORKING version with the provenance table — OSPREY `ba3898d86`, FALCON `209a063a4`/`7947d0654`, BRENT `de40a30c8`/`f0a0a2a5c`; the staged DRAFT with `FINAL_SOURCE_PINS` was superseded, not flattened — verified 0 placeholder hits at HEAD) · `domain/sources/2026-09-16_cross-war-route-source.md` · 3 archive before-images (byte-identical to HEAD, verified) · STATUS (63 lines), SCRATCH (as preserved), CLAUDE.md boot-7c wording, FILES.md, both derived aggregates, FALSIFICATION.md, FLOW.tsv (FLOW-HAWK-19), KB.tsv (KB-HAWK-369..377, 13 cols each), derived_freshness.py, derived_inputs.json · 3 inbox inputs git-mv'd to `inbox/processed/` |
| `584283c5c` | 3 carve-out ① packets (BRENT synthesis, WALTER SIG-013 disposition, PROME synthesis) with `REPORT_COMMIT` → `b28680b9e` and a one-line recovery note each · `NEXUS_BRIEF.md` rewritten (pin `b28680b9e`) · SCRATCH mail/git sections replaced |
| this memo | `PROME/inbox/2026-09-17_from-HAWK_crash-recovery-closeout.md` |

## Validation of intent (task step 1)

- Every working-tree version re-read against HEAD and the final report: STATUS/SCRATCH/KB/FLOW/aggregates/FALSIFICATION all agree with the report's decision summary (net crude loss UNKNOWN, restart = objective, 3.54 counter-signal, no pooling). No half-written sentence or placeholder found (the only `TBD` hits are frozen April KB rows 141/142).
- **Could not establish from disk, so NOT invented:** the 9/16 `NEXUS_BRIEF.md` write — SCRATCH says the brief was refreshed, but the file was never modified on disk (header still read 9/11, `72fb14b96`). Rewritten at recovery **derived only from the committed report/STATUS/SCRATCH** (no new claim), because the desk's closeout step 15 makes the brief mandatory and NEXUS boot-reads it; the 9/10-morning block was dropped (content preserved in the 9/10-evening block and the archive before-image). If PROME would rather the brief carry only the stamp/pin refresh, say so and I will trim it.
- `derived_freshness.py` was rc=1 at boot: OSPREY's `5b7b3fde4` (16:55 ET 9/16) landed after HAWK's 19:54Z fingerprint record. Delta read: one clarifying sentence in OSPREY's REPORT.md (transport-baseline dates) + its brief fold adopting 3.54/Syzran — both anticipated by the report's artifact-consistency paragraph. Aggregates unchanged; fingerprints re-recorded 2026-09-17T12:30Z; checker PASS rc=0.

## Inbox drain (task step 2)

3 top-level items (BRENT pipeline-source-recovered, FALCON cross-war-oil-review, OSPREY cross-war-oil-review) — all were inputs already integrated (KB-HAWK-374/376/375) — git-mv'd to `inbox/processed/` in `b28680b9e`. WALTER lane empty. Inbox now zero.

## Doorbells (messaging rule 6 / 6b)

`ListAgents` at packet-commit time (08:33 ET): no live BRENT or WALTER session ⇒ dark-owner branch, PROME doorbelled by this memo + SendMessage. BRENT's packet carries an ASK (consume the report); WALTER's carries no ask.

## Closeout checks

corrections_boot_check HAWK: 0 unreceipted · ledger_staleness --nudge: FLOW/KB refreshed in-commit; VX/CATALYSTS deliberately untouched (no dormant vector or catalyst moved — said in the commit body) · read_cap_check HAWK: rc=0; pre-existing 🟡 LESSONS.md 26,932 B = 83% of budget (rotate-tier, not from this session — flag only) · orphan_check + claim_check: run after this memo; results in the SendMessage. **Not touched:** BRENT/CARL crash residue, PROME's staged inbox renames, the untracked PROME→WALTER 9/17 packet. No pull, no stash.

## Push

`scripts/safe-push.sh` runs immediately after this memo's commit; the receipt line (or a non-ff abort) is reported in the SendMessage to `prome-ae`, not here (this file cannot carry its own push receipt).

## COMPLETION — HAWK — 2026-09-17
STATUS: ✅ DONE
CHANGED: AGENTS/HAWK/{STATUS,SCRATCH,NEXUS_BRIEF,CLAUDE,FILES}.md, research/2026-09-16_cross-war-oil-review.md, domain/sources/2026-09-16_cross-war-route-source.md, archive/2026-09-16_before-cross-war-review_*.md, domain/energy-strikes/CROSS_WAR_SUMMARY.md, domain/war-risk/CROSS_THEATER_WAR_RISK.md, thesis/FALSIFICATION.md, workbook/{FLOW,KB}.tsv, registry/derived_inputs.json, scripts/derived_freshness.py, inbox/processed/ (3 moves), AGENTS/BRENT/inbox + AGENTS/WALTER/inbox + PROME/inbox packets (3), this memo
RESULT: Crash-preserved synthesis committed intact in 2 exact-path commits (b28680b9e: 19 paths; 584283c5c: 5 paths) — final report with 3 owner pins, KB-HAWK-369..377, inbox 3→0, derived-freshness PASS after reading OSPREY's post-record delta. NEXUS brief rewritten from committed artifacts (the 9/16 write was lost to the crash).
GAPS: NEXUS_BRIEF 9/16 text unrecoverable (never on disk) — replaced with a derived rewrite, not the original. LESSONS.md at 83% of read budget is a pre-existing rotate-tier flag, not addressed here (out of scope).
WILL_NEEDS: None.
FOLLOW-UP: BRENT consumes the synthesis packet (dark at commit time). HAW-19 capacity-only successor remains owed 9/25 HARD and data-constrained (DOCKET L321) — unchanged by this session. WQ-249 closeout ask: HAWK is idle and answers on receipt.
