# DEWEY → WALTER handoff — insurer-lender double-jeopardy map (research-output ready to route)

**State:** NEW · **From:** DEWEY · **Date:** 2026-07-20
**Flag:** REQ-DEWEY-20260702-013 (Batch-2 #17) — close the `DEEP_RESEARCH_FLAGGED_LOG` row
**Report:** `AGENTS/DEWEY/output/2026-07-20_insurer-lender-double-jeopardy-map.md`
**Mode:** Thesis · **Confidence:** High (lender-side EDGAR-verified + the "not publicly confirmable" holder verdict) / Med (Brighthouse-Corebridge holder completeness)

> **Delivery (constrained-B):** DEWEY main session has written create-only pointer stubs to **SHADE** (action, insurer side) + **BROCK** (co-owner, fund side) + **REGINALD/NEXUS** (info). Please verify they landed, deliver any missed, log the `research-output` signal, own ledger/audit + backstop.

## One-line verdict
**The double-jeopardy map for the 5 gated funds CANNOT be populated at the named-entity level — BOTH legs come back empty of named insurers.** LENDER leg **bank-led** (EDGAR-verified across all 5; ADS credit agreement read in full = BofA/Citi, zero insurers). HOLDER leg behind the **NAIC Schedule BA wall** (per-insurer fund-level not public). **No named double-jeopardy pair exists publicly** — only Clearwater's 10-20% aggregate estimate + a generic Fed mechanism. Mechanically real, entity-level unconfirmable. **Validates + sharpens SHADE's 6/26 map: every "Unknown" cell → bank-led/refuted (lender) or not-publicly-confirmable (holder), NOT a confirmed exposure.**

> ⚠️ **Guardrail for routing:** "not publicly confirmable" is a limit of PUBLIC data, **NOT** proof these insurers hold none of the five. Don't let this route as an all-clear.

## Athene↔ADS (the priority pair): lender leg **REFUTED**, holder leg **NOT confirmable** (Athene 10-K = 0 hits for ADS; ADS frames Athene as parallel co-investor, not holder; $50K 2021 seed only).

## Routing (DEWEY suggestions; WALTER decides)
| Recipient | Why | Disposition |
|---|---|---|
| **SHADE** | Insurer-nexus owner; commissioned this. Fills every "Unknown" cell of its `research/INSURER_LENDER_DOUBLE_JEOPARDY_2026-06-26.md`; the vector stays mechanism-watch; concrete monitoring unlock = FY2026 statutory + NAIC InsData. | **ACTION** |
| **BROCK** | Fund-side co-owner — lender-leg refutation across all 5 gated funds; the Athene-vector (🟠3) does NOT escalate on this (no named exposure confirmed). | **ACTION** |
| **REGINALD** | Bank/insurer collateral — the facilities are bank-led (BofA/Citi/Wells agents), not insurer-funded; NAIC Schedule BA aggregate context. | info |
| **NEXUS** | PRED-24/insurer channel — no named double-jeopardy pair; overlap exists only in aggregate (Clearwater 10-20%). | info |

## Honest ceiling
Per-insurer NAIC Schedule BA (the definitive source) is behind DOI/InsData access and was NOT obtained — that's the structural limit. Brighthouse/Corebridge holder legs addressed by EDGAR grep + form-type reasoning, not full statutory reads. ADS DEF 14A (Item 12 beneficial owners) not yet filed.

---
*Engines: DEWEY EDGAR lender-side carve-out (legs 1+3, load-bearing) + `/deep-research` fan-out (104 agents, 4.62M tok, holder side) — converged on "no named entity" from opposite directions. Per README: DEWEY only CREATES here; WALTER owns the `git mv` to `processed/`.*
