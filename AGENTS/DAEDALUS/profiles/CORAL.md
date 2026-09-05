# Agent Profile — CORAL

**Built by:** DAEDALUS · **Body:** prior 2026-07-22, **refreshed 2026-09-05**
**Method:** solo read + named blockers re-measured + the MARCO overlap reconciled at both artifacts
**Staleness:** 30-day clock (its own, tighter than fleet default) → checkpoint **2026-10-05**

---

## 1. Identity
**Florida, whole-state, 10 pillars** (real estate · insurance · banks · migration · tourism · fiscal · labor · climate). Market class, ACTIVE. Deliberately overlaps MARCO (FL migration/tourism sub-desk) and AEOLUS (FL climate/coastal). Florida is a top-priority geography for Will.

## 2. State (2026-09-05)
Last session **2026-09-02** (PROME-orchestrated full owner session). **⚠️ My prior row said "dark 9d since 8/23" — superseded; CORAL ran 9/2.**
- **Read-cap split executed 9/2**, and cleanly documented: `STATUS.md` = state/colours/live levels/owed actions (boot-read whole, **161 ln**) · `STATUS_DETAIL.md` = the evidence rows behind each datum. The file map is stated at the top of STATUS, which is the right form.
- **`thesis/THESIS.md` v1.1** — rails bumped 8/23 (Will-approved), and it carries **`Next falsify grade: 2026-11-15`**: a falsification surface with a *dated* next grade, which is the leg most desks leave open-ended.
- **⭐7 Trepp gap CLOSED** — the WALTER self-audit found CORAL had received none of five Trepp signals it owned; cycle 2 landed 9/2 and CORAL reported **the zeros, as asked** (no FL asset named anywhere in the August print). Reporting a clean negative against an explicit ask is the right behaviour and it is recorded here as such.

## ⚖️ THE CORAL↔MARCO SHARED FIGURE — reconciled 2026-09-05, and it is NOT the discrepancy it looks like

Root `CLAUDE.md` makes CORAL↔MARCO a deliberate overlap (*"reconcile shared metrics to one figure, don't silo"*), and **FL international migration** has sat flagged UNRECONCILED on both map rows. Measured today:

| Desk | Surface | Figure | Vintage stated? |
|---|---|---|---|
| **MARCO** | `workbook/VX.tsv` `VX-MARCO-3.04` → `FIGURES.md:77` | **+411K international** (offset −63K domestic) | ✅ **2024**, "STALE BY DESIGN — next print ~late 2026" |
| **CORAL** | `STATUS_DETAIL.md:49` Migration (7) pillar | **+178,674**, "but **−57% YoY**" | ❌ **none on the intl figure** |

**They are the same series at different vintages, and they are arithmetically consistent:**
`178,674 / 411,000 = 0.4347` ⇒ **−56.5% YoY**, against CORAL's stated **−57%**. CORAL is carrying the **2025** print; MARCO's canonical row is the **2024** print. **The numbers corroborate each other — they do not conflict.**

⚠️ **I nearly shipped the opposite finding.** On first read this looks like CORAL carrying a figure **2.3× smaller** than the desk it explicitly names as canonical — a headline cross-desk defect. The reconciling term was sitting inside CORAL's own cell (`−57% YoY`) and I had to do the arithmetic to see it. `[[finding_apparent_confabulation_is_often_a_baseline_mismatch]]` — check the baseline before crying discrepancy.

**So what IS the real defect? A missing vintage stamp, not a wrong number.**
1. **CORAL's intl figure carries no year and no source.** The row's *"canonical per MARCO commit `a95631b7`"* annotation attaches to the **domestic** figure beside it (which does carry "2025 annual Census"), so a reader naturally reads the pointer as covering both. It does not.
2. **MARCO's `FIGURES.md:77` presents +411K (2024) as *the* FL international migration figure** with no note that a 2025 print exists showing −57%. MARCO's canonical number is a year behind what CORAL already holds.
3. **Neither surface points at the other**, so the overlap reads as an unreconciled discrepancy to any third party — which is exactly what happened to me.

**⇒ The reconciliation the root rule asks for is one line on each side, not a data fix:** CORAL stamps its intl figure `+178,674 (2025)` and names its source; MARCO's row notes the 2025 print beside the 2024 baseline it is stale-by-design against. **Neither desk has a wrong number and neither owes the other a correction.**

## 4. The L4 gate — one leg is discharged, and one has been mis-framed as blocked
| Leg from my prior row | Status 2026-09-05 |
|---|---|
| **MARCO migration reconciled to ONE figure** | ✅ **DISCHARGED by this pass** (§3). No data fix was needed on either side — a vintage stamp each. |
| **Citizens next observable ≈ early Sep** | ⏳ due now; check at CORAL's next session |
| **The flat-by-design TRADE ruling (Will)** | 🔴 **MIS-FRAMED — see below** |

**🔴 F-1 — CORAL's L4 has been gated on a ruling nobody was going to produce, when the desk can make the surface itself.** My row has carried *"L4 on: the flat-by-design TRADE ruling (Will)"* since July. That is **PAT-080** — *a gate leg no one can clear is a hold, not a standard.* Compare the precedent I applied to **ZHAO today**: ZHAO gets **ADAPTED-PASS** on the L4 TRADE leg because it *has* a `TRADE.md` that is **FROZEN with an explicit unfreeze condition** — a declared, readable no-book-by-design surface. **CORAL has no TRADE surface at all**, so there is nothing for a grader to adapt-pass and nothing for Will to ratify.
**⇒ The cheap path is not a ruling. It is a one-page declared-flat TRADE surface in ZHAO's form** — *"no position by design; here is the condition under which that changes"* — which CORAL can write itself, and which turns Will's ruling from a blocker into a confirmation. Same precedent family as CARL / LIQUID / MIDAS.

## 5. Grade — **L3 (H) HELD**, with the L4 path re-specified
| Leg | Verdict | Basis |
|---|---|---|
| L1–L2 floor | **PASS** | STATUS + BOTTOM LINE; ledgers accruing |
| L3 convergence matrix | **PASS** | 10-pillar grid, per-pillar colour + evidence rows in the cold half |
| L3 exit rules | **PASS** | thesis rails v1.1, two rail changes 8/23 |
| L3 predictions resolving | **PASS** | 4 passed catalysts RESOLVED (CSU, NHC, FL-bank 10-Qs) |
| L3 **dated** falsification surface | **PASS** ⭐ | `Next falsify grade: 2026-11-15` — dated, not open-ended; **and the rails were graded for the first time ever on 8/23 (1.5/6 HOLD)** |
| **L4 TRADE feeding proposals** | **FAIL — but re-specified** | no TRADE surface exists; the fix is CORAL's to write, not Will's to rule (F-1) |
| L4 signals flowing / consumed | **PASS** | REGINALD grid consumption confirmed (§FEEDS TO); MARCO cites CORAL's lane |
| L5 | **not reached** | — |

**L4 next-upgrade line:** *write the declared-flat TRADE surface in ZHAO's form (no position by design + the explicit condition that changes it) — CORAL's to author. Then Citizens' early-Sep observable. The MARCO reconciliation is done.*

## 6. Carried, still open
- **Amendment 3 ruling — still unlocated** (item E, the **oldest un-worked item** on the desk; Judge David Frank, 2nd Judicial Circuit). Certified for the Nov-3-2026 ballot, so it has a hard clock.
- **Both improving thermometers are MIX statistics** (⭐4 lesson) — keep in view whenever a pillar colour improves.
