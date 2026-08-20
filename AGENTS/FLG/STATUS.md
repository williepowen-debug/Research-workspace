# FLG STATUS

> 🔴 **FIRST-LIVE-SESSION BANNER — UNSPENT.** This desk was built 2026-08-20 and **has not yet run a session of its own.** Every figure below is **MIRROR-grade**: extracted from REGINALD or recomputed from that extract, never pulled by FLG at a primary. Run `CLAUDE.md § FIRST LIVE SESSION` before treating any read here as this desk's own work, and strike this banner when it is spent.

**Last Updated:** 2026-08-20 16:33 ET — **BUILD SESSION (DAEDALUS, Will-approved in-session).** Agent created off REGINALD's convergence matrix v2.0 (`75f0dd18b`, 16:04 ET the same day), which ranked FLG **🔴 6/6 — 1st of 14 scored banks** after v1 had ranked it **7th of 7, last**, and which REGINALD reported with no thesis file on the name. Build proposal: `AGENTS/DAEDALUS/builds/FLG_BUILD_PROPOSAL_2026-08-20.md`.

**Class:** Market domain — print-driven single-name specialist · **Level:** L1 at birth *(no FLEET_MAP row yet — ROSTER registration is PROME's and lands first, PAT-047)*

---

## BUILD-SESSION FINDING — the one thing to read

🔴 **The deleveraging may already have bottomed, and nobody had noticed.**

Total loans QoQ across the 11 quarters in `workbook/MI3_FLG.tsv` (FFIEC Call Report, RSSD 694904):

`−0.1 · −2.9 · −1.1 · −10.9 · −5.8 · −3.0 · −4.0 · −1.9 · −3.5 · −0.6 · **+0.9**`

**2026-06-30 is the first positive loan quarter in the series**, and the prior four decelerate monotonically toward zero. All eleven `loans_qoq_pct` cells were recomputed against `total_loans_k` at build and reproduce to 2dp (KB-FLG-014 — the desk's only first-hand row).

**Why it matters:** `workbook/EXIT_PROTOCOL.md` leg **K-1 is the thesis-kill**, and it requires **two consecutive** positive quarters. It is **one print from firing**, resolving at the Q3-2026 Call Report **~2026-11-14**. This surfaced on the same afternoon the cohort ranked FLG its worst name.

**What it is NOT:** a refutation of REGINALD's matrix. The matrix measures concentration and credit quality; this measures balance-sheet direction. Both can be true — that tension is the desk's central open question, not a contradiction to resolve by picking a side.

---

## Position

**NO POSITION** (verified 2026-08-20 against `FORGE/STATUS.md`, reconciled 2026-08-14). Surface: `TRADE.md`.

⚠️ Historically traded: **FLG $13P ×3, $45** (`AGENTS/RED/research/POSITION_RECONCILE_2026-06-10.md:37`) — outcome **UNRECORDED, not zero**. Live print **$13.49, −1.46%, 2026-08-20** (`FORGE/tools/market-data/fetch.py`, pulled at build). The old strike is ~ATM. **Never cite that price after today** — pull live (root Critical Rule 4).

**No position may be proposed before the first-live-session protocol is spent.**

---

## Seed state (all MIRROR-grade — re-verify before load-bearing)

| Read | Value | Source | Grade |
|---|---|---|---|
| CRE concentration (SR 07-1; denom = total risk-based capital) | **327.5%** — above the 300% supervisory line, cohort-worst | REGINALD matrix v2.0 ch.1 | MIRROR |
| Nonaccrual rate (nonaccrual / total loans) | **4.88%** — cohort-worst, ~5.5× median | REGINALD matrix v2.0 ch.2 | MIRROR |
| ACL / nonaccrual coverage | **29%** — cohort-thinnest (AMTB 51%, EGBN 88%) | REGINALD matrix v2.0 | MIRROR |
| Total assets | $111.17B (2023-09-30) → **$87.71B** (2026-06-30), **−21.1%** | `MI3_FLG.tsv` | MIRROR |
| Total loans | $85.92B → **$61.19B**, **−28.8%** | `MI3_FLG.tsv` | MIRROR |
| MI3 `v1_pct` | 5.28% → **3.65%** | `MI3_FLG.tsv` | MIRROR |

**The two instruments point opposite ways.** Concentration and credit quality read cohort-worst; the balance sheet reads eleven quarters of contraction with a falling MI3. That is `THESIS.md` Q1 and Q2.

---

## Open questions (priority order — full form in `THESIS.md`)

| # | Question | State |
|---|---|---|
| **Q1** | Is the concentration ratio measuring risk, or a shrinking denominator? A ratio can RISE while absolute CRE risk FALLS if the easier-to-exit assets ran off first | 🔴 **BLOCKING** — gates every concentration threshold. Routed to REGINALD 2026-08-20 as a question about its instrument, **not** a refutation |
| **Q2** | Has the deleveraging bottomed? | 🔴 **LIVE** — one print from resolution (~2026-11-14) |
| **Q3** | Does the rent-regulation mechanism actually transmit? Stages 1–2 are **entirely un-instrumented** | 🟠 Until instrumented, this desk holds a credit observation, not a causal thesis |

---

## Structural state at build

- **Ledgers live:** `MI3_FLG.tsv` (12 quarters, RSSD 694904, `Verified_By` empty = not FLG-verified) · `KB.tsv` (14 rows: 13 seeded + 1 first-hand) · `TRIGGERS.tsv` (7 rows, all `[EST]`/`RULE`-anchored, **none is a registered gate**) · `PREDICTIONS.tsv` (**empty by design** — a seeded prediction would be the architect's forecast, not this desk's).
- **Kill rail:** `workbook/EXIT_PROTOCOL.md`, stamped `Kill rail re-derived: 2026-08-20`, **PROVISIONAL** (authored against the seed; no thesis exists yet). K-1 flagged one quarter from firing.
- **boot.py:** 4 legs — ledger staleness · predictions-due · triggers-due · **quarter-due** (Call Report clock). All four paths watched at build per `CHECK_STANDARD.md` §3: clean rc=0, due rc=1, missing-register rc=2, fixtures restored byte-identical.
- **Registration:** ROSTER + root canon are **PROME/Will-scoped and OPEN** — packet routed 2026-08-20. No `FLEET_MAP` row until ROSTER lands (PAT-047 order; `render_directory.py`'s co-registration guard fails loud on the reverse).
- **Parent seam:** REGINALD owns the cohort view and a **live FLG price vector** (`VX-REG-6.03`, baseline $14.24 2026-08-12, bands −10/−15/−20%, state GREEN). At $13.49 it sits **−5.3%**, roughly halfway to band 1. ⚠️ **REGINALD-owned — FLG does not edit or grade it** (PAT-063). Re-point/dual-action packeted 2026-08-20.

---

## Next actions (the first-live-session list, in order)

1. **Re-verify the seed at FFIEC CDR** (RSSD 694904), at minimum the two most recent quarters; stamp `Verified_By`.
2. **Recompute the SR 07-1 ratio yourself**, both definitions written out; report the delta against 327.5% whichever way it falls.
3. **Answer Q1** — pull CRE composition + total risk-based capital as dollar levels across 12 quarters. **This gates every threshold.**
4. **Base-rate the 7 `[EST]` triggers** against the series; retire the ones that do not separate. "Don't build it" is a real answer.
5. **Instrument stage 1 or 2** (RGB series / maturity profile) — without one, Q3 stands unanswered and the seat is unjustified.
6. **Re-derive and re-stamp** `EXIT_PROTOCOL.md`; author `THESIS.md` v1.0 only when its five-point bar is met.
7. **Write back:** STATUS + BOTTOM LINE, PROME packet (gate proposals), REGINALD packet (the step-2 reconciliation).

---

## BOTTOM LINE

**FLG exists as a desk because a rebuilt instrument inverted a ranking, and its first act was to find the fact that most complicates that ranking.** The cohort's worst concentration, nonaccruals and reserve coverage sit on a balance sheet that has shrunk 29% in loans over eleven quarters — and whose loan book **turned positive last quarter for the first time in the series**, putting the thesis-kill one print away at ~2026-11-14. The desk therefore opens with a conclusion it did not earn and a mechanism it has not instrumented: stages 1–2 of its own transmission chain have no instrument at all, and every number on this page is MIRROR-grade until re-pulled. **Next: the first live session — re-verify the seed at the primary, answer whether the concentration ratio is measuring risk or a vanishing denominator, and do not register a single threshold until that answer exists.**
