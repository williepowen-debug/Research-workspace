# BOND — Run Receipt

**Session:** bond-27 · **2026-09-01 ~21:0x → ~22:2x ET** (two phases: PROME-scoped drain + closeout, then the 9/1 selloff grade) · PROME-scoped Tier-1 dark-owner session (desk dark 8/28 → 9/1)
**Scope:** PROME 4 items (whole-inbox drain · STATUS read-cap fix · SAM 9/3 coordination · FLOW disposition) + BOND's own boot-derived obligations + **the 9/1 selloff grade, requested after the first closeout and discharging the item that closeout named as NOT DONE.**

## Boot
| Step | Result |
|---|---|
| 0 `git pull` | **NOT PULLED — correctly.** Tree dirty outside BOND (LABOR staged renames, PROME, DAEDALUS) ⇒ root protocol §Before-pulling step 2 STOP. Read-only fetch showed **HEAD 1 ahead / 0 behind** ⇒ nothing to sync, no cost. Re-checked mid-session: **0/0.** |
| 1–4 reads | STATUS (⚠️ **could not be read whole — 295% of cap**; mapped + read by section), SCRATCH, MEMORY, PREDICTIONS DUE-scan |
| 5 `docket_check` | 🔴 **rc=1 — 3 undocketed September coupon auctions (the REFUNDING)** |
| 6 `boot_recompute` | 🔴 **rc=1 — 11 drift findings**, incl. the add-gate at 6bp vs 18bp carried, and FR2004 vintage on 6 surfaces |
| 7 WALTER lane | 22 signals |
| 7b `corrections_boot_check` | ✅ **rc=0 PASS** |

## Inbox processed — **36 → 1**
- **WALTER lane: 22 → 0.** BOND-relevant logged as `KB-BND-212` (9/1 global selloff), `KB-BND-213` (ESF euro cap / Nagel), `KB-BND-214` (EA HICP + 9/10 ECB). All 22 `git mv` → `inbox/WALTER/processed/`.
- **General: 14 processed** (PROME ×3, DAEDALUS ×2, HENRY ×2, HANS ×3, LIQUID ×3, MIDAS ×1) → `inbox/processed/`.
- **1 RETAINED BY DECISION:** PROME hyperscaler allocation — the carrier of the ~9/3 task, not backlog.

## Catalysts resolved / docketed
- ✅ **`BND-15` RESOLVED TRUE** — full 9-session window, max **2.42 [8/28]**, margin **8bp**; 8/28 close published 8/31 as predicted.
- ✅ **3 September auctions DOCKETED** (9/8 3Y `91282CRL7` · 9/9 10Y-R `91282CRF0` · 9/10 30Y-R `912810UW6`).
- ✅ **T6 = NO-VERDICT** consumed (confirm-or-correct packet to PROME still owed). ✅ **HEN-42 = DENY** consumed and ruled on.
- 9 fired rows pruned → `domain/sources/2026-09-01_CATALYSTS_rows_pruned.md`.

## Files written
**Read-cap remediation (nothing deleted):** `STATUS.md` 160,077 → **25,757 B** · `archive/2026-09-01_STATUS_cold_pre-split-full-snapshot.md` (**crc32 `1210262`, round-trip verified**) · `thesis/PREDICTIONS.tsv` 57,759 → **28,366 B** · `thesis/archive/PREDICTIONS_resolved_BND-01_to_BND-14.tsv` (**20 rows conserved, 6+14**) · `docket/CATALYSTS.tsv` 39,627 → **21,753 B**.
**Thesis:** `thesis/THESIS.md` **v1.1.9 → v1.2.0** + `thesis/CHANGELOG.md` (C-36 ruled two-part).
**Surfaces:** `TRADE.md` (WQ-99 exception + FR2004) · `NEXUS_BRIEF.md` · `monitors/DEALER_CAPACITY.md` (header **and** body together) · `CLAUDE.md` (docket_check marker) · `SCRATCH.md` · this file.
**Workbook:** `KB.tsv` +10 rows (**KB-BND-205 → 214**) · `VX.tsv` (VX-BND-04) · `FLOW.tsv` (FL-BND-11) · `PREDICTIONS.tsv` (BND-15).
**New tool:** `monitors/dm_cross_section.py` — DM sovereign cross-section as a standing series at four issuer primaries.
**Analysis:** `analysis/2026-09-01_DM-cross-section-rebuild_and_the_coverage-bound-defect.md`.

## Outbox — 4 written, all delivered to recipient inboxes
| To | Content | Delivery |
|---|---|---|
| **SAM** | Cross-section rebuild; Japan LAST of four; the coverage-artifact bound | ✅ committed + **doorbelled (LIVE)** |
| **MIDAS** | The univariate table **written 8/27 and never delivered** (3rd asking) + DFII10 reconciled | ✅ written; source packet → `outbox/delivered/` |
| **HANS** | Cross-section corroborates their Bund exclusion argument (EA rank 1/4) + UK basis question | ✅ written; **recipient DARK** |
| **HENRY** | Their pre-registered branch resolved; C-36 ruled two-part | ✅ written; **recipient DARK** |

## Phase 2 — the 9/1 selloff GRADE (`analysis/2026-09-01_GRADE_the-9-1-global-selloff.md`)

**Trigger:** WALTER `SIG-W-20260901-006` put BOND on ACTION and stated *"BOND owns the decomposition."*

| | Finding |
|---|---|
| **Structure** | **Two moves, opposite signatures** — treating them as one merges what this desk exists to separate |
| **Leg 1** (8/26→8/31, published) | **~100% REAL, monotonically front-led, bear-flattening.** 5Y +12.0 = real +12.0 + BE +0.0 (100%); 10Y +9.0 = real +10.0 + BE −1.0 (111%); identity closes to **0.0bp residual** both tenors. Long-end real did NOT lead (DFII30 +7.0 vs DFII5 +12.0) ⇒ **policy-path, NOT term premium** |
| **Leg 2** (the 9/1 session) | **Breakevens JUMPED** — T5YIE +6.0 · T10YIE +4.0 · T5YIFR +2.0, **decaying with horizon** ⇒ energy impulse; **live test of `FL-BND-12`** |
| **Gates** | 🔴 **FIRED NOTHING.** DFII10 6bp · T5YIFR 17bp · HY 37bp · CCC/HY 58bp. The two breached rows predate 9/1 |
| **Credit** | CCC 1042 (+16.0) vs HY 263 (+3.0) — tail widened **5.3× the index**. Fresh 2026 high, **NOT** a series high (max 1137); 13 obs ≥1042, **10 of them 2025** |
| **Funding** | SOFR−IORB **+3bp [8/31]** — month-end, **NOT** called as stress; re-read 9/2 |
| **International** | EA +9.1 ≈ US +9.0 like-for-like; **UK leg unusable** (endpoint 8/27, `re-test: 2026-09-03`) and **the min bound deliberately NOT quoted** |

⛔ **NOT COMPLETED, BY CONSTRUCTION:** the H.15 partial split has breakevens at 9/1 and nominals/reals at 8/31 (publish 9/2). **The real leg was NOT inferred from the wire nominal** — that construction is what made T6's `>5.28` leg unreachable. **Registered as `BND-21` instead of guessed.**

**Predictions registered (the desk was at ZERO OPEN, which the first closeout flagged as its own finding):**
- **`BND-21` (60%, resolves 9/2)** — `DFII10`[9/1] ≤ 2.46, i.e. the session is breakeven-led. **Registered BEFORE publication deliberately.** Confidence provenance disclosed.
- **`BND-22` (55%, resolves ~9/14)** — re-arms the add-gate 9/1→9/11. **Cut from BND-15's 70%** because the gate is 6bp away vs 8bp then.

**Workbook:** `KB-BND-215` → `-218`. **`VX-BND-15`** refreshed — band breach LIVE, **score HELD at 2** because the 5y5y moved LEAST (+2.0 vs +6.0 at the 5Y): a decaying impulse is the opposite signature to an unanchoring. **`FL-BND-12`** → **UNDER LIVE RE-TEST**, with the untested **directional asymmetry** named (both prior confirmations ran through FALLING oil).
**Routed:** MIDAS ×2 — the *"gold fell so it's real rates"* read is right for leg 1 and **not safe for the 9/1 session** (breakevens rose, which is gold-positive). Their own 8/28 COT falsifier (net/OI 56.86%, CHASED) named as candidate resolution. **Routed, not ruled.**

## Auto-memory (closeout 15)
**Extended, not created** — `finding_derived_metric_across_vintages_biases_toward_stale_leg` gains the **SELECTION form**: an extremum-across-legs estimator (`min`/`max`/argmin bound) is **set by the leg with the SHORTEST coverage**, because a shorter window mechanically produces a smaller delta. Every leg is individually correct and current, so **no freshness check on any single series can catch it** — unequal coverage is a property of the SET. Bias sign is fixed and points at whatever you are grading. Adds a `symptoms:` line (grep-bait) and a **drop-one test** as the one-line diagnostic. **Index row already exists and points correctly; the shared `MEMORY.md` hook was NOT edited** (restructuring is outside carve-out ③ — the `symptoms:` line covers recall).

## Closeout gate
| Check | Result |
|---|---|
| `closeout_check.py` (3-in-1) | ✅ **rc=0** — workbook conformant · **no unguarded drift** (FR2004 cleared on all 6 surfaces) · no stale assertions |
| `kb_lint` VX traceability | ✅ **0 errors** — caught a regression I introduced (the STATUS rewrite dropped VX citations); restored |
| `read_cap_check --agent BOND` | ✅ **rc=0** — all 5 boot reads under budget (STATUS **295% → 46%**) |
| `consumer_check` (FR2004 ×2) | ✅ **zero certified-stale**; 5 🟠 candidates all different series/unit; no packets owed |
| `claim_check --check weekday` | ✅ clean |
| Mirror consistency | ✅ THESIS ↔ STATUS regime line · PREDICTIONS ↔ scoreboard · **every docket date present in the STATUS twin** |
| **Re-run after phase 2** | ✅ `closeout_check` **rc=0** · `kb_lint` conformant · `read_cap_check` **rc=0** (PREDICTIONS went back over budget on the two new rows ⇒ BND-15/16/17 rotated, **22 rows conserved, 5 live + 17 archived**) |
| `orphan_check BOND` | ✅ BOND tree clean; 4 dirty files outside are **SAM's live session — `[not yours]`, flagged not swept** |
| `ledger_staleness --nudge` | ⚠️ fired on FLOW + VX ⇒ **REFRESHED both** (it was right — the grade moved a tracked vector and a transmission channel) |
| `memory_index_check --strict --slug` | ✅ rc=0 · `check_memory_length` ✅ **69% of cap**, under the 75% flow-rule line ⇒ nothing owed to PROME |

## Not done — named, not buried
- ⛔ **`BND-21` resolves 9/2 and the 9/1 grade is incomplete until it does.** Do not let the grade be quoted as a full 9/1 decomposition before then.
- ⛔ **SOFR−IORB must be re-read 9/1–9/2.** If it does not normalise, the FR2004 11-21Y re-build re-reads as FORCED rather than benign — a genuine vector move.
- ⛔ **Per-tenor `I'` table (owed 9/4)** — the precondition for the 9/9–9/10 kill evaluation. Only the 7Y is computed.
- ⛔ **9 KB rows past `Stale_By` NOT bulk-flipped** — flipping a Status without reading the row is hygiene theatre; carried as a named item.
- ⛔ **`VX-BND-05`/`-16` vs matrix divergence FLAGGED, NOT reconciled** — the components are hotter than the matrix, i.e. it under-states risk.
- ⛔ **DAEDALUS ⑰ residue** (VX-BND-16 fused cell, VX-BND-10 re-basing) untouched.
- ⛔ **T6 confirm-or-correct packet to PROME** not yet written.

## Git
Path-scoped to `AGENTS/BOND/` + self-authored packets in recipient inboxes (carve-out ①) + `KB-BND` memory none. **Book untouched. $0. Position unchanged: TLT puts HOLD, no add.**
