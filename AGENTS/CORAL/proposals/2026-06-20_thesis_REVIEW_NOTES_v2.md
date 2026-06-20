# CORAL Thesis Rails — Review Notes v2

**Drafted:** 2026-06-20  
**Files under review:**
- `AGENTS/CORAL/proposals/2026-06-20_thesis_THESIS_DRAFT_v2.md`
- `AGENTS/CORAL/proposals/2026-06-20_thesis_CHANGELOG_DRAFT_v2.md`

---

## What changed from v1

- Changed install-path assumption to mature-agent layout:
  - `AGENTS/CORAL/thesis/THESIS.md`
  - `AGENTS/CORAL/thesis/CHANGELOG.md`
- Reduced live metric clutter in THESIS. Exact values now belong mostly in `STATUS.md`, `workbook/KB.tsv`, `workbook/VX_Vectors.md`, and `workbook/FLOW_Pathways.md`.
- Kept CHANGELOG standalone; no changelog history embedded inside THESIS.
- Sharpened the bank-upgrade rail:
  - no 🔴 bank-transmission upgrade unless at least two FL-exposed banks show synchronized deterioration, or one pure canary like USCB shows condo-association stress with corroborating consumer/collateral data.
  - defined deterioration as NPL/NPA migration, realized NCOs, specific reserve builds, classified/current reclass migrating to nonaccrual/loss, USCB condo-association stress, or association bankruptcy/receivership cluster with bank corroboration.
- Kept the insurance split explicit: personal/reinsurance easing does **not** equal condo/commercial master-policy easing.
- Moved SSB short retirement mostly to CHANGELOG; THESIS keeps only a one-sentence calibration warning.
- Added “What belongs where” so future CORAL sessions do not duplicate thesis, status, vectors, flow mechanics, handoff, and NEXUS surfaces.
- Preserved MARCO / REGINALD / CARL / NEXUS ownership boundaries.

---

## Recommended install plan if Will/Prome approve

1. Create thesis directory:
   - `mkdir -p AGENTS/CORAL/thesis`
2. Copy/install:
   - `AGENTS/CORAL/proposals/2026-06-20_thesis_THESIS_DRAFT_v2.md` → `AGENTS/CORAL/thesis/THESIS.md`
   - `AGENTS/CORAL/proposals/2026-06-20_thesis_CHANGELOG_DRAFT_v2.md` → `AGENTS/CORAL/thesis/CHANGELOG.md`
3. Update `AGENTS/CORAL/CLAUDE.md` boot/closeout/file-map language so CORAL:
   - reads `thesis/THESIS.md` at boot for durable mechanism/rails,
   - reads/updates `thesis/CHANGELOG.md` only on thesis-level changes,
   - does **not** duplicate thesis history inside STATUS.
4. Update references only — do not paste the full thesis into live docs:
   - `AGENTS/CORAL/STATUS.md`: add short thesis/version pointer in header/read-first block.
   - `AGENTS/CORAL/NEXUS_BRIEF.md`: update thesis version/path line.
   - Optional `SCRATCH.md`: note install completed during that session only.
5. Leave live metric levels in their owner docs:
   - `STATUS.md` for current dashboard.
   - `workbook/KB.tsv` for permanent facts.
   - `workbook/VX_Vectors.md` for indicator state.
   - `workbook/FLOW_Pathways.md` for mechanics.
6. Commit install with pathspec scoped to `AGENTS/CORAL/` after verifying no other live files were unintentionally changed.

---

## Open questions for review

| Question | Why it matters | Suggested owner |
|---|---|---|
| Is the bank-upgrade rail strict enough, or should USCB alone be sufficient only with explicit association-loan deterioration? | Avoids another premature bank-expression error. | Prome / REGINALD |
| Should THESIS name specific banks beyond USCB as examples, or leave bank lists to `FL_BANK_WATCHLIST.md`? | Specificity helps execution but can stale the durable thesis. | Prome / REGINALD |
| Does the “personal/reinsurance vs condo/commercial” insurance split need a standard short label for all agents? | Prevents future “insurance easing” compression error. | Prome / NEXUS |
| Should MARCO be formally assigned live owner of condo inventory/tourism/migration metrics, with CORAL referencing? | Prevents divergent duplicate values. | MARCO + CORAL |

---

## Caveats

- v2 remains proposal/draft work only. It does not install final thesis rails or modify live CORAL files.
- v2 intentionally removes most exact metric values from THESIS; they remain in current CORAL live files.
- The older `workbook/FLOW_Pathways.md` still contains legacy target/timing language around VLY and older Q1/Q3 framing. If thesis rails are installed, a later cleanup pass should reconcile FLOW to the thesis split without deleting useful mechanics.
