# Retired 2026-07-30 — VIOLET directory sweep

Retired under the root Data Hygiene rule: **>60 days old AND not boot-read AND not referenced by a live doc** → `git mv` to `archive/`. Every file below was checked for inbound references before moving; the only referrers found were `archive/MAINTENANCE_ARCHIVE.md` (a historical log) and `reports/2026-07-11_threads-sweep.md` (a point-in-time sweep). **Neither is a live reference.**

| File | Vintage | Why retired |
|---|---|---|
| `SIGNAL_TEMPLATE_*.md` ×4 | 2026-04-12 | Outbox signal templates, **0 inbound references, 109 days old.** Superseded by the NEXUS_BRIEF-primary model — `outbox/` is now 🔴-acute only, so per-class templates have no consumer. |
| `2026-06-10_claude_md_REWRITE_DRAFT.md` | 2026-06-10 | **Draft** of a rewrite that shipped. The live `CLAUDE.md` is the artifact. |
| `2026-06-10_signal_intake_REWRITE_DRAFT.md` | 2026-06-10 | Same — `SIGNAL_INTAKE.md` shipped and has since been re-audited (7/30). |
| `2026-06-10_claude_md_condition_report.md` | 2026-06-10 | Audit output, applied. |
| `2026-06-10_root_md_audit.md` | 2026-06-10 | Audit output, applied. |
| `2026-06-10_hedge_flag_pricing_packet.md` | 2026-06-10 | **0 inbound references.** |
| `2026-06-09_packet1_abstain_gate_spec.md` | 2026-06-09 | Implementation spec, **wired into thesis v3.6**; framework is now v3.8. Historical record. |
| `PHASE2_PLAN.md` | 2026-04-15 | Plan, **executed.** Its output — `2024-11_2025-01_cluster_analog.md` — is still live and cited by `MEMORY.md`'s ANALOGS table, and was **not** retired. |

---

## Second batch — same day, PM sweep (research corpus)

The AM sweep covered docs and templates but **never reference-checked `research/` itself.** Doing so retired five more:

| File | Vintage | Why retired |
|---|---|---|
| `2026-03-27_peak_postmortem.md` | 2026-03-27 | 125 days, **0 live referrers.** |
| `2026-04-15_hy_oas_trajectory.md` | 2026-04-15 | 106 days, **0 live referrers.** Credit-lead substance now lives in the thesis § CENTRAL CLAIM. |
| `2026-04-15_vix_target_distribution.md` | 2026-04-15 | 106 days, **0 live referrers.** Superseded by the L1 canonical base-rate table (KB-VIO-079). |
| `2026-05-21_stage2_vs_stage3_verdict.md` | 2026-05-21 | 70 days. **Referenced only by ITSELF.** The verdict survives as a summary in `MEMORY.md`'s session-notes trajectory; the file had no consumer. |
| `2026-04-15_macro_stress_roundup.md` | 2026-04-15 | 106 days. **Chained** — its only referrer was `2026-03-27_peak_postmortem.md`, retired in this same batch. |

⚠️ **THE NAIVE REFERENCE CHECK GAVE THE WRONG ANSWER ON THREE OF THESE, AND IT ERRED TOWARD KEEPING.** A plain "is this filename mentioned anywhere?" grep returned 🔒 KEEP for `macro_stress_roundup` (referrer: another retirement candidate), `stage2_vs_stage3_verdict` (referrer: **itself**), and `apr22_gate_postmortem` (self + a candidate + `KB.tsv`). **Only the last has a genuinely live referrer, and it was correctly kept.** The other two would have been retained forever by a check that cannot see it is reading a closed loop — the `finding_circular_corroboration_via_state_file` class applied to file retention.

**The corrected rule, for whoever runs this next: a reference only counts if the referrer is (a) not the file itself and (b) not also being retired in the same pass.** Retirement is transitive, so the sweep has to be run to a fixed point rather than once.

**Kept on this pass despite age**, and each for a real live referrer: `2024-11_2025-01_cluster_analog.md` (`MEMORY.md` ANALOGS + `KB.tsv`) · `2026-04-15_skew_divergence_episodes.md` (`thesis/VIX_THESIS.md` L1 provenance + `diet_coiled_spring.py`) · `2026-04-16_regime_termination_analysis.md` (`regime_termination.py`) · `2026-04-16_skew_post_fire_trajectory.md` (`skew_trajectory.py`) · `2026-05-03_apr22_gate_postmortem.md` (`KB.tsv`).

---

**Nothing here was deleted.** Recoverable in place, and via git history regardless.

**Checked and deliberately NOT retired**, despite similar age: `workbook/SCHEMA.tsv` (boot-read enum validation) · `research/2026-04-15_skew_divergence_episodes.md` (cited in the thesis L1 base-rate provenance) · the `credit_vix_lag/` · `regime_patterns/` · `term_structure/` · `crisis_analogs/` corpora (cited by the thesis) · every `workbook/*.csv` and every `scripts/*.py` — **all were reference-checked and all are still referenced.** No orphaned tooling exists in this agent.
