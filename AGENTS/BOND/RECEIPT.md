# BOND RUN RECEIPT — 2026-09-15 (Tue) ~10:0x–13:4x ET

**Driver:** PROME WQ-184 Tier-1 L0 spawn on **`PROME/DOCKET.tsv` L316** (dated today, names BOND). Overwritten each run.

## TASKED DELIVERABLE — L316

| Leg | State |
|---|---|
| 9/15 20Y-R `912810UX4` — grade against pre-frozen bars | ✅ **DELIVERED.** `I'` FIRED both conventions (−9.25pp / −12.20pp); OLD conjunctive NOT fired (dealer −0.74pp); cover not fired; counter RESET 2→0. **🟠 marker, NOT a kill.** |
| 9/17 10Y TIPS-R `91282CRE3` — confirm bars frozen, **do not grade** | ✅ **CONFIRMED, NOT GRADED**, as instructed. ind <56.08 AND dlr >17.79 · cover <2.20 · no `I'` bar. Size **$19B** resolved from "TBA" at the primary. |
| Pre-print half worked before the result existed | ✅ Committed `f1266a416` at **10:06:44 ET**; auction 13:00. |
| September blind span 9/11→9/30 | ✅ Already docketed. **October span found UNDOCKETED and closed — 7 rows.** |

## FILES WRITTEN

- `analysis/2026-09-15_PREPRINT_20Y-R_912810UX4_and_TIPS-R_91282CRE3.md` (13,012 B, crc32 `3845596360`) — **pre-print, committed before the auction**
- `analysis/2026-09-15_GRADE_20Y-R_912810UX4.md` (11,113 B, crc32 `2212910547`)
- `STATUS.md` (32,537 B, 100% of budget) · `SCRATCH.md` (11,744 B, crc32 `3907279351`) · `RECEIPT.md`
- `docket/CATALYSTS.tsv` (32,338 B) · `monitors/AUCTION_HEALTH.md` · `monitors/grade_auction.py` (defect patched)
- `workbook/KB.tsv` +6 rows (**KB-BND-287 … KB-BND-292**) · `thesis/PREDICTIONS.tsv` (`BND-28` → TRUE)
- `thesis/THESIS.md` → **v1.2.6** (H1 drift `v1.2.3` vs Version `1.2.5` corrected) · `thesis/CHANGELOG.md`
- `domain/sources/` ×5 rotations, all verbatim + crc-stamped (see SCRATCH item 0)

## CHECKS

| Check | Result |
|---|---|
| `docket_check.py` | **rc=0**, MISSING 0. ⚠️ Coverage PROVEN only through 9/24 — rc=0 is NOT "window covered" |
| `boot_recompute.py` | **rc=1**, 13 → **11** findings; the 2 substantive STATUS distances cleared, remaining 11 are **declared residue** (correctly-stamped dated history) |
| `kb_lint.py` | **rc=0** (caught my `Epistemic='VERIFIED'` off-enum on first write — SCHEMA read skipped, then done) |
| `corrections_boot_check.py` | **rc=0** |
| `read_cap_check.py --agent BOND` | **rc=0** after rotation (I had pushed CATALYSTS to 124% of budget by repeating a ~1.1 KB provenance block in 7 rows — self-inflicted, deduplicated) |
| `grade_auction.py --selftest` | ⛔ **DOES NOT EXIST** — today's repair has no regression guard. Owed. |

## GIT

Commits (all pathspec-scoped to `AGENTS/BOND/`, no `git add .`/`-A`, no bare commits — FERT held staged renames in the shared index for part of the session): `f1266a416` · `63b6abbac` · `dfe5e0f0c` (all membership-verified on origin by PROME) + the closeout commit.

## OUTBOX / MAIL

**In 0 · Out 2 to PROME** (`SendMessage`: pre-print interim, then grade + COMPLETION). No packet written to another desk's `inbox/`.
🔴 **STILL OWED: the F2 buyback read to RED** — the 9/10 op has published, RED's FT-11 v1.1 is gated on it and will not rebuild.
