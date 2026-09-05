# Agent Profile — MARCO

**Built by:** DAEDALUS · **Body:** prior 2026-07-10, **refreshed 2026-09-05** (state + gates re-cut; durable structural knowledge carried)
**Method:** solo read + each named L5 handle re-measured individually + the CORAL overlap reconciled at both artifacts
**Staleness:** >45d → checkpoint **2026-10-20**

---

## 1. Identity
**Florida migration / tourism** — Market class, ACTIVE. The FL sub-desk, deliberately overlapping CORAL (whole-state, 10 pillars). Florida is a top-priority geography for Will. **Spawnable by:** PROME / Will.

## 2. State (2026-09-05)
Last session **2026-09-03** (s25) — *"went to correct three Canada figures and came back having read the Section…"*. STATUS **171 ln**. Substance is strong and unchanged in character: **57-vector VX**, 1,928 probe values re-graded, a self-caught parser twin bug. Rich supporting layer — `FIGURES.md`, `COUPLINGS.md`, `FINDINGS.md`, `DEFERRED.md`, `EXPECTED_SIGNALS.md`, `baselines/`, `sub_agents/`, `handoffs/`, `thesis/PREDICTIONS.tsv` + `scripts/predictions_due.py`.

**⚠️ My prior row said "Dark 10d (8/22)" — false; MARCO ran 9/3.**

## 3. The three named L5 handles — re-measured, and **one of them was never a gate**
| # | Handle | Measured 2026-09-05 | Verdict |
|---|---|---|---|
| 1 | **Labeled BOTTOM LINE** | **0** matches for a labeled heading; the substance sits unlabeled at `Composite :80` / `NET :27` / `Net :146` | **LEGITIMATE GATE — L1 floor** ("Live = STATUS + BOTTOM LINE"). Still unmet. One heading. |
| 2 | **§2 universal 5-pt + Independence handles** | **0** hits in STATUS or VX | **LEGITIMATE — market-blueprint §2 handle.** Still unmet; additive over existing substance, never a replacement. |
| 3 | ~~PREDICTIONS_ARCHIVE / calibration scoreboard~~ | `thesis/PREDICTIONS.tsv` + `predictions_due.py` exist; no archive | 🔴 **STRUCK — this was never a ladder leg.** Market L5 is *clean closeouts · zero YEYOU flags · current*; L3 asks only that **predictions resolve**, which MARCO's ledger does. I appended a row-local expectation and then graded MARCO against it as if it were a gate. |

**Third instance of that defect today** — the same append-a-nice-to-have-then-grade-it error appeared on ORACLE (Brier) and ZHAO (archive/scoreboard). See `EVOLUTION.md` (n).

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

## 5. Grade — **L4 (H) HELD**
| Leg | Verdict | Basis |
|---|---|---|
| L1 STATUS + **labeled** BOTTOM LINE | **FAIL** | substance present, label absent — the one true floor gap |
| L2 structured record accruing | **PASS** | VX 57 vectors, KB, FLOW, ML (in-file FROZEN banner :1), MIGRATION_PROXIES |
| L3 convergence matrix | **PASS** | 57-vector VX with graded probes; §2 *handles* absent (row 2 above) |
| L3 exit rules | **PASS** | present in local form |
| L3 predictions resolving | **PASS** | `thesis/PREDICTIONS.tsv` + a working due-check |
| L3 dated falsification surface | **PASS** | thesis layer |
| L4 signals flowing / consumed | **PASS** | CORAL cites MARCO as canonical by commit hash; handoffs/ + NEXUS_BRIEF live |
| L5 clean closeouts · current | **PASS** | s24 8/22, s25 9/3 |
| L5 zero YEYOU flags | **WAIVED** | no live feed (see `profiles/YEYOU.md`) |

**L5 next-upgrade line:** *two form changes over existing substance — a labeled BOTTOM LINE heading, and the §2 5-pt + Independence handles. Nothing else.* The list is shorter than it was because the third item was mine, not the ladder's.

## 6. Findings
**🟡 F-1 — the shared-figure reconciliation above is MARCO's half too:** `FIGURES.md:77` presents **+411K (2024)** as *the* FL international migration figure with no note that a **2025** print exists showing −57%. One line closes it.
**🟡 F-2 — my prior row carried "Dark 10d (8/22)"**; MARCO ran 9/3. Struck.
**✅ Confirmed still true from the prior pass:** shared `ledger_staleness` IS wired (`scripts/boot.py:54` + rc contract) · `ML.tsv` HAS an in-file FROZEN banner (:1, 2026-08-11) · `VX.tsv` declares `STATE: LIVE` two-state at :1.

## 7. Open
- Citizens STATUS-vs-VX vintage split — still UNVERIFIED, still owed a confirm-read.
- The docket-default-inversion lesson (a proclamation re-setting the effective date in its own operative text) → PROME/DOCKET. Still live.
