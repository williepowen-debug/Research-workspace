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

**Nothing here was deleted.** Recoverable in place, and via git history regardless.

**Checked and deliberately NOT retired**, despite similar age: `workbook/SCHEMA.tsv` (boot-read enum validation) · `research/2026-04-15_skew_divergence_episodes.md` (cited in the thesis L1 base-rate provenance) · the `credit_vix_lag/` · `regime_patterns/` · `term_structure/` · `crisis_analogs/` corpora (cited by the thesis) · every `workbook/*.csv` and every `scripts/*.py` — **all were reference-checked and all are still referenced.** No orphaned tooling exists in this agent.
