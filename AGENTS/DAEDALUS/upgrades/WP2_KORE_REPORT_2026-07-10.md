# WP2 — KORE Report: CARL Sub-Agent Harvest / Freeze / Orphan Hygiene

**Editor:** KORE (working for DAEDALUS) · **Date:** 2026-07-10 · **Fence:** `AGENTS/CARL/sub_agents/` only (CARL LIVE elsewhere)
**Source tasking:** DAEDALUS `upgrades/CARL_SUBAGENT_AUDIT_2026-07-10.md` (META HARVEST-THEN-FREEZE; orphan hygiene item #7)
**Status:** ✅ ALL TASKS COMPLETE. No git add/commit run — DAEDALUS commits the batch.

---

## Changelist

| # | Action | Path(s) | Verification |
|---|--------|---------|--------------|
| 1 | HARVEST — copy digest out | `AGENTS/CARL/sub_agents/META/core/RESEARCH_DIGEST.md` → **new** `AGENTS/DAEDALUS/reference/META_RESEARCH_DIGEST_harvested_2026-07-10.md` (+ provenance header) | `diff` of cp = IDENTICAL; post-header `diff <(tail -n +15 harvested)` vs original = BODY BYTE-IDENTICAL. Header is an HTML comment block (does not render), only addition. |
| 2 | FREEZE banner | `META/CLAUDE.md` (line 1) | Blockquote `⛔ FROZEN 2026-07-10` prepended above `# META …` |
| 3 | FREEZE banner | `META/core/META_DOMAIN_SKELETON_v1.1.md` (line 1) | Prepended above `# META DOMAIN SKELETON` |
| 4 | FREEZE banner (harvest pointer variant) | `META/core/RESEARCH_DIGEST.md` (line 1) | Prepended; last sentence points to the harvested reference copy |
| 5 | ORPHAN MOVE (git mv) | `PHAN/CARL_HANDOFF_20260417.md` → `PHAN/outbox/CARL_HANDOFF_20260417.md` | `git status` = `R` (clean rename, 100%) |
| 6 | ORPHAN MOVE (git mv) | `GIG/CARL_HANDOFF_20260417.md` → `GIG/outbox/CARL_HANDOFF_20260417.md` | `git status` = `R` (clean rename, 100%) |
| 7 | PATH-REF FIX (mechanical, 1 line) | `GIG/STATUS.md` line 313: `**CARL_HANDOFF_20260417.md**` → `**outbox/CARL_HANDOFF_20260417.md**` | Only change to STATUS.md; label text + description unchanged |

Scope check: `git status --short` shows **only** the 7 rows above (5 M/R inside `CARL/sub_agents/{META,PHAN,GIG}` + `DAEDALUS/reference/` untracked). Nothing touched outside the writable set.

---

## Grep results (whole `AGENTS/CARL/` tree, term `CARL_HANDOFF_20260417`)

**Command:** `grep -rn "CARL_HANDOFF_20260417" AGENTS/CARL/`

| File:line | Form | Points to | Disposition |
|-----------|------|-----------|-------------|
| `GIG/STATUS.md:313` | **path-style** (`.md`, KEY DOCS list) | GIG handoff | ✅ In my writable set — **fixed** to `outbox/…` after the move |
| `CARL/outbox/SIG-CARL-REGINALD-20260417-subprime-auto-ABS-gap.md:25` | source **label** (no `.md`): "via GIG CARL_HANDOFF_20260417. KB-CARL-229" | GIG handoff (provenance) | ⚠️ **CARL-lane — NOT edited.** Not a path; move is safe. |
| `CARL/outbox/SIG-CARL-LIQUID-20260417-BNPL-ABS-composition-degradation.md:16` | source **label** (no `.md`): "PHAN CARL_HANDOFF_20260417. KB-CARL-228" | PHAN handoff (provenance) | ⚠️ **CARL-lane — NOT edited.** Not a path; move is safe. |
| `CARL/workbook/KB.tsv:224` (KB-CARL-227) | source label: "PHAN CARL_HANDOFF_20260417" | PHAN | ⚠️ CARL-lane — NOT edited |
| `CARL/workbook/KB.tsv:225` (KB-CARL-228) | source label: "PHAN CARL_HANDOFF_20260417" | PHAN | ⚠️ CARL-lane — NOT edited. **Confirms audit note:** KB-CARL-228 cites the handoff as a *label*, not a path → move safe. |
| `CARL/workbook/KB.tsv:226` (KB-CARL-229) | source label: "GIG CARL_HANDOFF_20260417 citing CUCollector / WolfStreet" | GIG | ⚠️ CARL-lane — NOT edited |
| `CARL/workbook/KB.tsv:227` (KB-CARL-230) | source label: "PHAN CARL_HANDOFF_20260417" | PHAN | ⚠️ CARL-lane — NOT edited |
| `CARL/workbook/KB.tsv:228` (KB-CARL-231) | source label: "POP CARL_HANDOFF_20260417" | POP (not moved) | ⚠️ CARL-lane — NOT edited |
| `CARL/workbook/KB.tsv:229` (KB-CARL-232) | source label: "POP CARL_HANDOFF_20260417" | POP (not moved) | ⚠️ CARL-lane — NOT edited |
| `CARL/workbook/KB.tsv:230` (KB-CARL-233) | source label: "POLLY CARL_HANDOFF_20260417" | POLLY (not moved) | ⚠️ CARL-lane — NOT edited |

**Finding:** The ONLY filesystem-path reference to either moved file was `GIG/STATUS.md:313` (in-scope, fixed). Every other hit is a **provenance source label** (bare `CARL_HANDOFF_20260417`, no `.md`, no directory) inside CARL top-level files (`outbox/`, `workbook/KB.tsv`) — these describe *who produced the finding*, not *where the file lives*, so the moves do not break them. This matches the audit's prediction. No PHAN-side path reference to the PHAN handoff exists anywhere in the tree (its only citation is the KB-CARL-228 label).

### CARL-lane references (for DAEDALUS → CARL routing, do NOT edit from this session)
- `CARL/outbox/SIG-CARL-REGINALD-20260417-subprime-auto-ABS-gap.md:25` — label
- `CARL/outbox/SIG-CARL-LIQUID-20260417-BNPL-ABS-composition-degradation.md:16` — label
- `CARL/workbook/KB.tsv` rows 224–230 (KB-CARL-227 through -233) — labels
- These are all **cosmetic/provenance** and technically still resolve (label form). No action strictly required; if CARL ever wants label→path precision it could append `outbox/` on next KB touch, but there is **no breakage** to fix.

---

## Harvest byte-completeness confirmation

- `cp` of `RESEARCH_DIGEST.md` → reference path: `diff` returned **IDENTICAL**.
- After prepending the provenance header (an HTML `<!-- … -->` comment block, lines 1–13 + blank), `diff <(tail -n +15 harvested) original` returned **BODY BYTE-IDENTICAL**.
- The harvested file = provenance header + verbatim original. Sole surviving copy of the 6-framework methodology digest (Heuer / Nonaka / Boundary Objects / Lab Notebooks / Military C2 / Hospital Handoffs); its six source documents were already pruned from the repo.

---

## FLAG-ONLY (no edit) — HOMER retrieval hazard → DAEDALUS routes to CARL

Per tasking item #4 and audit item #7: HOMER's valid **SV-02** is filed inside `AGENTS/CARL/sub_agents/HOMER/state_vectors/corrected/SV-HOMER-2026-06-08-01.md`. Filing a *live/valid* SV under a `corrected/` (audit-trail) subdir is a **retrieval hazard** — a consumer globbing the normal SV location will miss it. **I did not touch HOMER** (outside this session's fence). DAEDALUS: route to CARL for disposition (relocate to the primary SV path or add a pointer).

---

## Handoff to DAEDALUS

- **Commit:** DAEDALUS commits this batch (pathspecs: `AGENTS/CARL/sub_agents/META/`, `…/PHAN/`, `…/GIG/`, `AGENTS/DAEDALUS/reference/`). The GIG STATUS.md edit + both renames + META banners can go in one CARL-sub-agent-scoped commit; the reference/ harvest is DAEDALUS-owned.
- **No CARL-lane edits pending from me** — the label references need no fix (they resolve as-is).
- **Route to CARL (not me):** (1) HOMER SV-02 retrieval hazard above; (2) optional label→path polish in KB.tsv/outbox if desired (non-breaking, low priority).

*KORE — WP2 complete, delivered before idle.*
