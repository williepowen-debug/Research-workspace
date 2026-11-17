# REGINALD -> PROME: items due by 11/20 worked: REG-T-02 token renamed, READS re-attested, L889 companion leg sent to WALTER, charter trims

**Written:** 2026-11-17 11:55 ET (from `date`). **Session:** Will direct ("start the due items now"), Claude Code, Opus 5.5.

| Item | Result |
|---|---|
| V1V3 rename (STATUS open ask, due 11/20) | **DONE.** REG-T-02 `action` = `WAL-PRICE-STRESS`; retired alias `V1V3-ACCELERATE` in `registry/NOTES.md`; `threshold_thesis_ref` fixed. Level, chain, exit, consequence unchanged. Packets: WALTER (four mirrors, `557453d063`), TERRY (procedure line 62, `76c5e48935`); stamps corrected `0bb4971d65`. **PROME:** `PROME/tools/tests/fixtures/desk_attention/PROME/GATES.tsv:16` names the old token; whether the fixture follows is yours (your live GATES.tsv has no hit). |
| ⚠️ Commit incident | My registry edit landed inside **WALTER's** commit `06f187503c` (WALTER built its path list from `git status`; it told me so and did not revert). Diff verified identical to my change; history left as is. Also seen at 11:52 ET: a staged deletion `AGENTS/BRENT/inbox/WALTER/SIG-W-20261117-001.md` in the shared index (WALTER's rename half); not touched. |
| L889 item 2, READS | Re-attested at charter HEAD `f0c32cf856` → `AGENTS/REGINALD/reports/2026-11-17_due-items/READS.attestation.tsv`: ATTESTATION row + one new summary row (`registry/PREDICTION_RESOLVE_BY.tsv`, read by boot.py, uncovered before). **Please register.** |
| L889 item 3, rc 1 | Not mine to clear: WALTER's companion review expired 11/05 (`review_due` in `AGENTS/WALTER/registry/signal_read_companions.json`), so the exception is refused and the 39,509 B source counts at 121%. Packet to WALTER with a long-due-date suggestion. rc stays 1 until WALTER renews or declines. |
| Size re-check (11/20 pointers) | Measured 11/17: every REGINALD read under 75% of budget. MEMORY 74% and DECK_EVIDENCE 74% sit within ~330 B of the trigger; MEMORY clears at my closeout. |
| WQ-678 Changelist B | Applied C01, C02, C03, C06, C07, C08, C09, C10 (wording only); declined C05, C11 with reasons in `f0c32cf856`. |

## COMPLETION — REGINALD — 2026-11-17
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/REGINALD/registry/THRESHOLDS.tsv, registry/NOTES.md, CLAUDE.md, reports/2026-11-17_due-items/READS.attestation.tsv; packets to WALTER (2), TERRY (1)
RESULT: 4 of 5 due-by-11/20 legs done: token renamed with alias (0 consequence changes), READS re-attested with 1 new row, 8 of 10 charter trims applied, sizes all under 75%.
GAPS: read_cap rc 1 stays until WALTER renews the SIG-W-20260619-008 companion review (lapsed 11/05; WALTER's registry).
WILL_NEEDS: None.
FOLLOW-UP: PROME registers the READS rows; WALTER renews or declines the companion and edits four mirrors.
