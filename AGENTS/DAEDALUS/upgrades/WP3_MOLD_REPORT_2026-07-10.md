> 🗄 **CLOSED 2026-08-11 (sweep #3 self-scope banner pass) — one-shot execution record, work consumed at the time; historical reference only, cite as history never as current state.**
# WP3 — PHAN Demotion to Dossier — MOLD Report

**Date:** 2026-07-10 · **Editor:** MOLD (DAEDALUS sub-editor) · **Authority:** Will-approved PHAN demotion (DAEDALUS `upgrades/CARL_SUBAGENT_AUDIT_2026-07-10.md`)
**Writable fence honored:** `AGENTS/CARL/sub_agents/PHAN/**` ONLY. CARL LIVE in parallel session; no git commands run (DAEDALUS commits the batch).

---

## 1. Changelist

| File | Action | Lines | Note |
|---|---|---|---|
| `PHAN/DOSSIER.md` | **CREATED** | 191 | New single entry surface — 8 sections, as-of-stamped throughout |
| `PHAN/CLAUDE.md` | edited | +2 | Prepended ⛔ DEMOTED banner (Klarna-warning clause KEPT — file carries Klarna claims at lines 30/46/66) |
| `PHAN/STATUS.md` | edited | +2 | Prepended ⛔ DEMOTED banner (Klarna-warning clause KEPT) |
| `PHAN/workbook/VX.tsv` | edited | +1 | `# FROZEN-VINTAGE` header comment |
| `PHAN/workbook/ML.tsv` | edited | +1 | `# FROZEN-VINTAGE` header comment |
| `PHAN/workbook/FLOW.tsv` | edited | +1 | `# FROZEN-VINTAGE` (points to DOSSIER §2c) |
| `PHAN/workbook/PREDICTIONS.tsv` | edited | +1 | `# FROZEN-VINTAGE` — "rows open, resolution pending CARL" variant |
| `PHAN/workbook/PROVIDER.tsv` | edited | +1 | `# FROZEN-VINTAGE` — flags Affirm/Klarna quarterlies superseded (§6) |
| `PHAN/workbook/COCKROACH.tsv` | **UNTOUCHED** | 0 | Stays LIVE append surface (as directed) |
| `PHAN/workbook/REGULATORY.tsv` | **UNTOUCHED** | 0 | Stays LIVE append surface (as directed) |
| `PHAN/workbook/SCHEMA.tsv` | **UNTOUCHED** | 0 | Schema defs used by both live TSVs; not in freeze list |
| `PHAN/outbox/*` | **UNTOUCHED** | 0 | Legacy handoff + SV preserved as-is (KB-CARL-228 cites the handoff) |

Nothing deleted. No content removed anywhere — freeze is additive banners only.

**Klarna-warning-clause decision:** brief said drop the clause from the CLAUDE.md banner *if* CLAUDE.md carries no Klarna claims. It does (line 30 "Klarna 0.65% provisions rising", line 46 "Klarna post-IPO credit deterioration", line 66 threshold row). Clause **KEPT** on both banners.

---

## 2. Must-carry coverage table

| Audit / brief must-carry item | DOSSIER section | Status |
|---|---|---|
| COCKROACH.tsv (unique fleet asset) | §5 Live ledger index (stays live) + indexed contents | ✅ CARRIED (kept live, not just indexed) |
| REGULATORY.tsv (1033-death + 12-state EWA timeline) | §5 (stays live) + indexed contents | ✅ CARRIED (kept live) |
| Phantom-DTI 35%→47% framework (~12pp gap) | §2a | ✅ CARRIED (STATUS:110-121 + CLAUDE:54-58,144) |
| CFPB-1033-death writeup VERBATIM | §2b | ✅ CARRIED VERBATIM (STATUS:92-108) |
| FLOW-PHAN-01..06 with breakpoints/lags | §2c table + FLOW-06 full detail | ✅ CARRIED (from FLOW.tsv — the version holding breakpoint/lag cols) |
| FLOW-06 ALLY-analog trigger detail (exceeds KB-228) | §2c "FLOW-PHAN-06 full detail" block | ✅ CARRIED FULLY (pathway + mechanism + trigger + evidence) |
| CLAUDE.md threshold table, bands+sources, Current re-labeled build-vintage w/ dates | §3 | ✅ CARRIED (each "Current" → as-of-stamped snapshot; ✅ marks frozen) |
| 7 PREDICTIONS rows w/ April confidences, ⚠ UNRESOLVED, not re-marked | §4 | ✅ CARRIED (P01–P07, April conf, all ⚠ UNRESOLVED, resolution left to CARL) |
| SUPERSEDED-AT-PARENT table (Affirm/Klarna quarterlies, Klarna Q1 profitable refutation, BNPL late 41%, CC 90+ DQ 12.70%→13.1%, ALLY-analog KB-228) | §6 | ✅ CARRIED (all 6 rows) |
| Source list + cadence (NCLC, New Economy Project, Richmond Fed EB-26-05, Chime tracker, + CLAUDE source section) | §7 | ✅ CARRIED (11 sources + catalyst cadence) |
| Refresh protocol (read DOSSIER → append live TSVs → update stamps → flag prediction resolutions to CARL) | §8 | ✅ CARRIED (5-step block) |

**SKIPPED / fabrication-avoided:** none. Every audit must-carry was locatable in the live PHAN files.

**Transcription note surfaced (not a skip):** FLOW numbering diverges between STATUS.md prose (FLOW-04 = "Phantom DTI → Mortgage Surprise") and FLOW.tsv (FLOW-04 = "Fintech Cockroach Cascade"). I carried the FLOW.tsv numbering (has breakpoint/lag columns) as §2c primary, preserved the STATUS "Phantom DTI → Mortgage Surprise" pathway via §2a, and flagged the divergence explicitly in §2c rather than silently reconciling two conflicting schemes.

---

## 3. Scope confirmation

`git status --short` (read-only) confirms this session's changes are **entirely inside `AGENTS/CARL/sub_agents/PHAN/`**:

```
 M AGENTS/CARL/sub_agents/PHAN/CLAUDE.md
 M AGENTS/CARL/sub_agents/PHAN/STATUS.md
 M AGENTS/CARL/sub_agents/PHAN/workbook/FLOW.tsv
 M AGENTS/CARL/sub_agents/PHAN/workbook/ML.tsv
 M AGENTS/CARL/sub_agents/PHAN/workbook/PREDICTIONS.tsv
 M AGENTS/CARL/sub_agents/PHAN/workbook/PROVIDER.tsv
 M AGENTS/CARL/sub_agents/PHAN/workbook/VX.tsv
?? AGENTS/CARL/sub_agents/PHAN/DOSSIER.md
```

Other dirty paths in the tree (DOC/GIG/POLLY/POP CLAUDE.md, DAEDALUS/*, DEWEY/*) pre-date this session — **not touched by MOLD.** COCKROACH.tsv / REGULATORY.tsv / SCHEMA.tsv correctly absent from the modified set. No git mutations performed — DAEDALUS owns the batch commit.
