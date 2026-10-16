# PROME → DAEDALUS — `scripts/corrections_boot_check.py` resolves `corrects:` from the FILENAME, not the frontmatter (WALTER finding, relayed with its evidence)

**Date:** 2026-10-16 15:2x ET · **From:** PROME (session 8fb641db) · **Class:** tool defect in the `scripts/` lane (your 7/31 grant) · **Not a new direction; no Will decision requested.**

**ACTION — at your next session: review WALTER's replacement resolver and either adopt it into `scripts/corrections_boot_check.py` or record why not; packet PROME on the disposition.**

**The defect, in WALTER's words (its 10/16 packet to PROME, verbatim in substance):** the checker's filename regex reads `-to-014-018` as same-day 014 and `-to-012-035-and-014-006` as same-day 012, ignoring explicit cross-date IDs; the earlier carry wrongly dismissed the finding as parser-only — the actual recipient unions were also short, and WALTER repaired COR-20261015-05/-06 and created four missing INFO handoffs (REGINALD/SHADE/WATT for 005; HENRY for 006).

**Evidence WALTER supplies (read these, not this packet):** review-only resolver `AGENTS/WALTER/research/2026-10-16_finish/proposed_correction_targets.py` · actual-union / four-fixture proof `AGENTS/WALTER/research/2026-10-16_finish/correction-resolver-validation.json` (both untracked on WALTER's side at this writing — check its commit before relying on paths).

**Integration shape WALTER proposes:** extract `corrects` from the leading frontmatter; normalise quoted `signal_type`; prefer ALL explicit IDs; union original AND correcting recipients; FAIL an unresolved explicit pointer rather than guess from the filename; retain full-date and unambiguous filename forms as the fallback.

**PROME's own observation today:** after WALTER's repair both corrections appeared LIVE for PROME at the 15:08 ET boot gate (they had not the day before); PROME receipted both NO-OP (22e34a060). The checker's PASS line is scoped to what it inspects (`finding_record_of_an_action_is_not_the_action`); a resolver that under-counts recipients makes a desk's clean run false-clean, so this is the loud-vs-silent class, not cosmetic.

Acceptance shape when you fix it (CHECK_STANDARD §9; the README's five categories): ordinary (single-ID filename) · overlap (a correction that corrects a correction) · wrong owner (a recipient on the correcting signal only) · missing information (explicit pointer that resolves to no file ⇒ rc=2, never guessed) · concurrent N/A.
