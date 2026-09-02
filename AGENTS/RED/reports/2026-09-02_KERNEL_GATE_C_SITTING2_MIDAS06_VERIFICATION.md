# Gate C Sitting 2 — MIDAS-06 independent verification (RED, verifier seat)

**Verifier:** RED (`independent_verifier_actor_id` on `Q-019306a1-4c00-7000-8000-00000000006a`; `resolution.verify` in live grants sha256 `a1fec8198ab9ac41e04da6e445906714fbad193f975ce5a1573362b44aba6f8c`)
**Checked:** 2026-09-02T14:08:30Z (box clock; re-derived at the primaries THIS session, not carried from the 9/1 stop report)
**Ruled window:** `[2026-09-02T14:00:00.000000Z, 2026-09-02T17:00:00.000000Z)` (WQ-103, Will 9/1 18:13 ET)
**Disposition:** **VERIFY — agree with proposed outcome YES.** No basis for `DisputeResolution`.

## 1. The proposal inspected (at the artifact, not the packet)

| | |
|---|---|
| Path | `AGENTS/MIDAS/outbox/kernel/submissions/CMD-01a05d61-fb0b-7e3d-b41e-e8432c3c9f1d.json` |
| Command / actor | `ProposeResolution` / MIDAS, `expected_version` 2, `depends_on` CloseQuestion `CMD-…006c` |
| Resolution | `R-01a05d61-fb0b-7848-a239-6820d48fd4fc`, outcome `YES` |
| File sha256 (re-hashed this session) | `8bb18ca2caaa69cdd91153ead37b7fa91878743aca0812314bb56b605eb88f4a` — matches WQ-149 pin |
| Native refs | TSV row `MIDAS-06` at `a1f1a4c0c…` (row bytes re-hashed → `4af7968f…` ✅) + companion `/resolution` at the same commit (file unchanged in tree, sha256 `c6f63516…` = committed blob ✅) |
| Commit | `b7e839238` 2026-09-01 14:32Z — inside Will's ruled 9/1 window with no minted activation live; **STANDS** under runbook §Carve-out-④ successor scope per DAEDALUS's 9/1 standing ruling, circumstance recorded in the sitting ruling record (R1). RED does not relitigate it here. |
| Stream state at E | `QS-Q-…006a`: v1 QuestionRegistered, v2 QuestionClosed (events commit `879158dc0`). Propose applies at v2 → v3; **RED's Verify carries `expected_version` 3** and is legal only from `RESOLUTION_PROPOSED`. |

## 2. Independent re-derivation of the frozen letter (both legs, both bases)

Letter (Will row-68 NO EDIT) → Kernel mapping: (a) gold ≥ 4340.70 AND DFII10 ≥ 2.40 → YES · (b) gold < 4050 while DFII10 ≥ 2.40 → NO · (c) DFII10 < 2.20 → AMBIGUOUS · (d) residual → AMBIGUOUS.

**Yield leg — the binding one.** FRED `DFII10` CSV pulled this session (`fredgraph.csv?id=DFII10`): 8/24 2.38 · 8/25 2.32 · 8/26 2.34 · 8/27 2.34 · **8/28 2.42** · 8/31 2.44. The observation DATED 2026-08-28 is the graded cell (Will's 8/27 lagged-series class ruling, option (i)); no substitute print was used. **2.42 ≥ 2.40 → PASS.** Not < 2.20 → (c) excluded.

**Gold leg — both bases (L-19).** yfinance daily bars pulled this session via the repo venv:

| Basis | 8/28 close | vs 4340.70 | (a) leg | vs 4050 |
|---|---:|---:|---|---|
| `GC=F` (continuous) | **4478.10** | +137.40 (+3.17%) | PASS | not below → (b) excluded |
| `GCZ26.CMX` (Dec-26 front) | **4529.90** | +189.20 (+4.36%) | PASS | not below → (b) excluded |

Both bases agree in direction, so the basis disagreement clause of the `ambiguity_rule` (→ (d)) is not triggered. No cross-roll delta was taken.

**Branch resolution:** (a) fires on both legs → **YES**. (b) fails on gold; (c) fails on yield; (d) is unreachable once a named branch fires. **Independent verdict = YES = MIDAS's proposed `outcome_value`.**

## 3. Guards honoured
- ⛔ Not verifying a (d) as NO — not applicable, (a) fired; recorded so the guard is visibly checked.
- Projection exclusion stands: P(YES)=0.45 / P(NO)=0.20 / P(AMBIGUOUS)=0.35 from the letter; a binary scorer would falsely read P(NO)=0.55. This verification changes nothing about scoring; the exclusion registry (`projection-exclusions.json`, `OUTCOME_VOCABULARY_MISMATCH`) governs.
- Verifier separation: RED ≠ proposer (MIDAS), RED holds no forecast on this question, RED ≠ PROME (custodian). `_protected_verification` should pass.

## 4. Observations, none verdict-changing
- **Vendor bars move after the fact.** MIDAS's 8/31 grade recorded `GC=F` and `GCZ26` both at 4497.30 on 8/31 (post-roll); today's pull shows 8/31 `GC=F` 4431.10 / `GCZ26` 4481.50. The 8/28 cells are byte-stable across MIDAS's two pulls and mine; the 8/31 cells are not. Nothing graded rides on 8/31, but it is a live instance of KB-088 (no vendor settle) — the CME settlement page remains the registered source of truth for any future gold leg and this seat did not reach it programmatically this session (fetch blocked); the yfinance bars are the second-source read, agreeing with MIDAS's T+1-confirmed bars to the cent.
- 9/1 `GC=F` closed 4348.00 — 7.30 above the (a) gold line. Had the letter graded 9/1 instead of 8/28, the gold leg would have been a coin-flip on basis. Not relevant to this grade; relevant to how close the registered line sits to the tape for any successor row.

## 5. Grant basis for RED's commit (stated, not laundered)
Root carve-out ④ requires a LIVE activation naming RED at commit time. Under PROME's amended sequence (message 9/2 ~10:05 ET) RED authors the command UNSTAGED, PROME mints activation F pinning this file's sha256, and RED commits only after F is live — all five root-④ legs satisfied at the commit instant. The desk grant is additionally keyed to the ruled bounds (runbook §successor scope; WQ-103 record names RED). This is the difference from 9/1, when no packet could be minted because the custodian was absent.

— RED
