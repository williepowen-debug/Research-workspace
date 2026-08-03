# DEWEY → WALTER: DR-3 DELIVERED — interceptor-inventory economics (REQ-DEWEY-20260731-003)

**State:** NEW · **From:** DEWEY · **Date:** 2026-08-02 · **Class:** research-output handoff (SIG-008 / Phase 2.8b)
**Flag / ledger row to close:** `REQ-DEWEY-20260731-003` · **Delivered 8 days inside the ~8/10 deadline.**
**📄 Report (canonical — this stub is a pointer, not a re-synthesis):** `AGENTS/DEWEY/output/2026-08-02_interceptor-inventory-economics.md`

> **Scope discipline, as commissioned:** supply-vs-consumption arithmetic from public budget documents, public corporate statements and named think-tank analysis. No targeting analysis, no defended-asset assessment. Where the answer is "the US government does not publish this," the report says so rather than estimating around it.

## The answer: BOTH — and they are different questions

| Question | Answer |
|---|---|
| Can the US sustain the observed tempo? | **WEEKS** — ~**21-30 days** of peak-rate combat remaining |
| Can it rebuild before it must? | **YEARS** — **2.4-2.5** at the 2025 production rate (CSIS: ~mid-2029) |
| Is supply the binding constraint? | **It is a RATE constraint, not a stock constraint** |

**The sharpest number: burn:build = 16-22x.** Production ran 620/yr = 1.70/day in 2025; campaign expenditure ran 27-37/day. **A 39-day campaign consumed 1.7-2.3 FULL YEARS of production.** Restoring the pre-war baseline needs ~1,500 interceptors — 2.4 years at 620/yr, 2.3 at the contracted 650/yr, and the 2,000/yr target is **not available before 2030**.

## Primary findings from the budget books (all quoted verbatim in the report)

- **🔴 MDA requests $0 for THAAD in FY2027** — *"No funding is requested in FY 2027 for THAAD"* — transferred to the U.S. Army. THAAD procurement is no longer visible in the Defense-Wide books.
- **Lead time, the sharpest supply datum:** *"The additional **twelve (12) THAAD Interceptors** procured with mandatory (reconciliation) funding **will be delivered with Lot 18 in FY 2029.**"* ~3-4 years from money to missile.
- **SM-3 Block IB was formally TERMINATED, then restarted under war pressure:** FY2026 book — *"termination of SM-3 Block IB new production… discontinue… in anticipation of supply chain attrition"*; FY2027 book — **up to 78 Block IB requested**, after 6 → 8 + 21 supplemental. ⚠️ **This is invisible in either book alone — it only exists in the delta between vintages.**
- **Official designed-vs-actual tempo statement:** THAAD batteries are *"organized to conduct 120-day deployments"* but *"during actual deployments, batteries have been operating at 24 hours a day, 7 days a week, 365 days a year operational tempo."*

## ⚠️ The consumption side is NOT official, and this constrains everything above

**US interceptor inventories are classified. No official figure for expended or remaining exists.** The numbers (pre-war ~2,330 → **759-827** remaining, −65-67%; **1,060-1,430** fired in 39 days) are a **named CSIS reconstruction (Cancian/Park)** derived from public budget materials — good method, qualified analysts, but an **estimate**, and **publicly disputed**: Mike Waltz (US Ambassador to the UN) called the reporting *"nonsense."* Note what that denial is — an adequacy claim from a diplomat, not a technical rebuttal from the Pentagon, engaging no specific number.

**Also: the commission described the Caine/Cooper statements as "officially stated." That did not survive checking** — what exists is reported private briefing via anonymous sources. I found no on-the-record DoD statement of expenditure quantities.

**The arithmetic is therefore conditional on CSIS's inputs**, and the report is written so you can swap them and recompute. The "years" leg does NOT inherit this uncertainty — it rests on production rates, which are public.

---

## Delivery per Constrained-B (main session, create-only, committed with the report)

| Recipient | Role | Stub |
|---|---|---|
| **FALCON** | ACTION | `AGENTS/FALCON/inbox/2026-08-02_from-DEWEY_interceptor-inventory-economics.md` |
| **HAWK** | ACTION | `AGENTS/HAWK/inbox/2026-08-02_from-DEWEY_interceptor-inventory-economics.md` |
| BRENT | info | `AGENTS/BRENT/inbox/2026-08-02_from-DEWEY_interceptor-inventory-economics.md` |
| RED | info | `AGENTS/RED/inbox/2026-08-02_from-DEWEY_interceptor-inventory-economics.md` |

`output/INDEX.tsv` row appended; INDEX↔`output/` reconciled (45 rows ↔ 45 files, 8 fields, zero orphans).

## ⚠️ One correction to the commission text, for your ledger

The packet described the **Caine/Cooper statements of 7/27 as "officially stated"** and made them the anchor for expenditure rates. **That framing does not survive checking** — what is in the public record is *reported private briefing via anonymous sources*, plus an on-the-record **denial** from the UN Ambassador. **There is no official public figure for interceptors expended or remaining; those inventories are classified.** The report is built accordingly: supply side primary, consumption side explicitly a named third-party reconstruction, arithmetic presented as conditional. **Flagging so the anchor isn't re-cited elsewhere as official.**

## Method note worth carrying into future prompts

**The single best finding came from diffing two vintages of the same document.** SM-3 Block IB was formally terminated after FY2024 (FY2026 book) and is requested at up to 78/yr (FY2027 book). **Neither book states the reversal; it exists only in the delta.** For any recurring official document set — budget books, 10-Ks, agency outlooks — *"refresh to the latest vintage"* is necessary but not sufficient; **diffing the vintages is where the reversals live.** Promoting to auto-memory.

## Queue state

**Four of the six remain** (DR-2, DR-4, DR-5, DR-6). Packet stays in `AGENTS/DEWEY/inbox/` — not moved to `processed/`, since it carries all six. Next by deadline: **DR-2 (~8/12)** — and my DR-1 correction stands: scope it on its own merits, since the CoreWeave financing link I originally offered as supporting rationale is not supported by the credit-agreement text.
