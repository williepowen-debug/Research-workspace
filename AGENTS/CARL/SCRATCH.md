# CARL SCRATCH
**Last session:** 2026-04-17 ~15:30 UTC (Will-directed, post-ALLY Q1)
**Type:** ALLY Q1 2026 earnings processing + CARL-performed FY2024/FY2025 10-K reclassification audit + thesis v2.4→v2.4.1 refinement

**PRIORITY-1:** SYF Q1 Mon Apr 21 — CRL-12 test (NCO >6% guidance ceiling). Apply auto-lender reclassification framework (KB-CARL-225): CLN routing, ACL/mix trajectory, PL vs CareCredit segment mix shift. Different cohort from ALLY (monoline cards, no used-car tail), so ALLY print does NOT pre-judge outcome. Second HY OAS complacency test.

---

## WHAT HAPPENED

1. **Boot** — git synced, read SCRATCH/STATUS/SCHEMA/TEAM, workbook healthy post-AM audit.
2. **ALLY Q1 earnings pulled** via web (Quartr MCP session had died). Press release link via media.ally.com; transcript via Investing.com (au.investing.com/news/transcripts/...-93CH-4369219).
   - Adj EPS $1.11 vs $0.94 est (+18%). Revenue $2.2B (+6% YoY).
   - **Retail auto NCO 1.97%** (-17bps QoQ, -15bps YoY). **5TH consecutive quarter YoY improvement.**
   - **30+ DQ 4.6%** (-17bps YoY). 4th consec qtr improvement.
   - Flow-to-loss "record low." Origination yield 9.6%, apps 4.4M (record +16% YoY), originations $11.5B (+13% YoY).
   - **S-tier origination concentration 41% (declining — "dynamic underwriting")** ← yellow flag
   - Reserves "held flat at $375M reflecting dynamic macro"
   - Mgmt: "Consumer behavior is resilient. There's a disconnect between consumer sentiment and what we're seeing."
   - CET1 10.1% (+60bps YoY). 2026 guide 1.8-2.0% NCO + 3.60-3.70% NIM MAINTAINED.
3. **Will flagged reclassification concern** — REGINALD has found 3-layer reclassification at regional banks (Memo Item 3, NDFI-in-C&I, sub-category relabel at CFG $2.9B, MTB $1.3B). Asked: does ALLY do similar?
4. **Pulled ALLY 10-Ks from EDGAR** — CIK 0000040729. FY2025 10-K (acc 0000040729-26-000005, filed 2026-02-25) and FY2024 10-K (acc 0000040729-25-000006, filed 2025-02-19). Saved to `domain/sources/ally/10k_fy2025/` and `10k_fy2024/` (18MB combined).
5. **Delegated forensic audit to Explore agent** with REGINALD 3-layer framework translated to auto-lender 7-lever toolkit (A-G). Audit persisted at `domain/sources/ally/RECLASSIFICATION_AUDIT_FY2025.md`.
6. **Audit findings — headline clean, cohort dirty:**
   - REGINALD Layers 1-3 **NOT present** at ALLY (not CRE bank, floorplan shrinking, no NDFI analog, no line-item taxonomy shift, no runoff segmentation, no HFI→HFS dumping, no TDR re-aging)
   - Composition-masking **IS present:**
     - Used retail S-tier: 40% → 37% (-3pp)
     - Nonprime (<620): 9.7% → 10.1% (+40bps, +$0.4B to $8.6B)
     - Used retail avg FICO: 707 → 702 (-5pts)
     - **ACL: $3.7B → $3.5B (-$224M / -6%)** ← reserve release into mix downgrade (REGINALD Layer F tell)
     - **CLN issuance: $0.77B → $1.1B (+43% YoY)**, reference pools $7B → $10B (Layer G tail-risk routing)
     - Originations +11% YoY into worsening mix
7. **Thesis revision v2.4 → v2.4.1:** Payment hierarchy NOT invalidated, TIMELINE PUSHED. FY2025 vintage loss window is 2H 2026 / Q1 2027 (18-24 month seasoning lag). Intra-auto K-shape: subprime ABS cracking (EART Class E CE breached) co-exists with near-prime headline-clean — composition-driven, not genuine.
8. **State written up:**
   - KB entries: KB-CARL-222 (Q1 print), -223 (mix shift), -224 (CLN), -225 (auto-lender framework), -226 (payment hierarchy revision). 221→226 rows.
   - VX: VX-CARL-ABS-12 updated (retail auto NCO 1.97% GREEN), added AUTO-MIX-01 (S-tier 37% ORANGE), AUTO-MIX-02 (nonprime 10.1% ORANGE), AUTO-MIX-03 (ACL/portfolio 2.5% ORANGE). 105→108 rows.
   - Red team: `COUNTER_LOG.md` prepended with full Apr 17 entry + reactivation triggers.
   - CHANGELOG: v2.4.1 entry with mechanism revision + CRL-05 85→82%.
   - PREDICTIONS: CRL-05 confidence 85→82% with ALLY counter-evidence note.
   - STATUS: header refreshed, ALLY Near-Prime row expanded (cohort caveat), CRL-05 row updated, catalysts line marked ALLY processed + added Q1 2027 reactivation test.
   - Outbox: `SIG-CARL-REGINALD-20260417-auto-lender-reclassification-translation.md` — full 7-lever framework translation + Ally findings.

## STATUS CHANGES
| Item | Change |
|------|--------|
| THESIS | v2.4 → **v2.4.1** (payment hierarchy timeline pushed) |
| CRL-05 confidence | 85% → **82%** |
| VX-CARL-ABS-12 | PENDING → **1.97% GREEN** (Ally Q1) |
| VX rows | 105 → **108** (+3 mix-shift trackers) |
| KB entries | 221 → **226** (+5) |
| STATUS Ally row | "🟢 Stable" → **"🟢⚠️ headline / 🟠 cohort"** |
| Outbox | 0 → **1** (REGINALD auto-lender framework) |
| red_team/COUNTER_LOG.md | ALLY Apr 17 entry added (top) |
| Convergence | 58/60 (unchanged — ALLY data is mechanism-level refinement, not vector) |

---

## NEXT SESSION SHOULD

### IMMEDIATE (this session / Mon 4/21)
1. **SYF Q1 Mon Apr 21 — CRL-12 NCO >6% test.** Apply auto-lender reclassification framework:
   - ACL trajectory vs mix composition (CareCredit vs Private Label segment shift?)
   - CLN/ABS expansion (monoline card trust data)
   - Originations growth vs underwriting commentary
   - If SYF also comes in benign headline + hidden cohort deterioration = SAME pattern as ALLY, thesis preservation mode. If SYF genuinely weak, validates CRL-12.
2. **COF Q1 Apr 21** — same framework; different book (domestic card + auto).
3. **Monitor git status before commit** — REGINALD has untracked PDFs in CFG/FITB/MTB/PNC/RF sources. Only stage CARL files.
4. **Commit CARL changes** — KB.tsv, VX.tsv, STATUS.md, SCRATCH.md, thesis/CHANGELOG.md, thesis/PREDICTIONS.tsv, red_team/COUNTER_LOG.md, outbox/SIG-CARL-REGINALD-20260417..., domain/sources/ally/ (2 10-K HTML + audit MD).

### UPCOMING (this week)
5. **Apr 21 Mon** — SYF Q1, COF Q1, DHI Q2
6. **Apr 23 Wed** — PHM Q1, AXP Q1 (apply auto-lender framework to AXP too)
7. **Apr 25 Fri** — UMich Apr Final (47.6 confirmed?)
8. **Apr 26** — FL UI Wave 2 peak

### UPCOMING (next 2 weeks)
9. **Apr 28** — Case-Shiller Feb, Rithm/NewRez Q1 (testable "DQ reverse" claim)
10. **Late Apr** — Fannie MF March DQ (CRL-03 GFC breach test, 0.74 → 0.80%)
11. **Late Apr / early May** — PennyMac Q1 (FHA DQ >7.5%?)
12. **May 28** — AFT/MOHELA status conference

### BACKLOG (no deadline)
13. **March 10-D ABS filings** (~Apr 20-25) — SDART/EART/AMCAR/HAROT/Ally March collection data. Cross-check against Ally Q1 cohort commentary.
14. **ALLY Q2 earnings** (~Jul) — first early-signal check on FY2025 cohort seasoning. If NCO stops improving on unchanged macro = payment hierarchy reactivation signal.
15. **BNPL_STRESS refresh** (16 days stale) — spawn PHAN
16. **STATE_DIFFUSION refresh** — non-FL states still 16 days stale

---

## OUTBOX (1 signal, awaiting delivery/integration — messaging overhaul pending)
| File | To | Summary |
|------|----|---------|
| SIG-CARL-REGINALD-20260417-auto-lender-reclassification-translation.md | REGINALD | 7-lever auto-lender translation of 3-layer bank reclassification framework + ALLY Q1 findings (mix shift, ACL release, CLN +43%); suggests applying to SYF Mon Apr 21 |

## INBOX (0 items, clean)

---

## WORKBOOK HEALTH
| TSV | Rows | Last Modified | Note |
|-----|------|---------------|------|
| KB | **226** | **Apr 17 (PM)** | +5 (ALLY Q1 + FY2024/25 mix + CLN + framework + hierarchy revision) |
| VX | **108** | **Apr 17 (PM)** | +3 AUTO-MIX trackers, ABS-12 updated |
| FLOW | 22 | Apr 17 (AM) | OK |
| PREDICTIONS | 18 | **Apr 17 (PM)** | CRL-05 85→82% |
| STATE_DIFFUSION | 63 | Apr 17 (AM) | FL refreshed, others stale |
| ABS_BASELINE | 67 | Apr 16 | OK |
| BNPL_STRESS | 44 | Apr 1 | **16 days stale — spawn PHAN** |
| TRENDS | 40 | Apr 6 | 11 days stale |
| ML | 67 | Apr 7 | 10 days stale |

---

## URGENT

- **SYF Mon Apr 21 is critical.** If SYF also prints clean headline, apply reclassification framework same as ALLY — look for ACL/mix divergence in the supplement. Don't take headline at face value. CRL-12 outcome depends on whether supplement reveals composition masking.
- **ALLY Q2 earnings (~Jul) is first early-signal test** on the v2.4.1 timeline-push claim. If NCO pauses improvement on unchanged macro, FY2025 cohort seasoning faster than expected.
- **Q1 2027 is the thesis reactivation test** for payment hierarchy pathway — 18 months past FY2025 origination. Mark calendar.
- **ALLY is the FIRST real-time test of the payment hierarchy cascade.** First test was "headline FAIL, cohort PASS." Honest read: thesis weakened at headline, preserved at cohort. Treat this as legit counter-evidence, not dismiss it.
