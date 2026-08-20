# FLG STATUS

> 🔴 **FIRST-LIVE-SESSION BANNER — UNSPENT.** This desk was built 2026-08-20 and **has not yet run a session of its own.** Every figure below is **MIRROR-grade**: extracted from REGINALD or recomputed from that extract, never pulled by FLG at a primary. Run `CLAUDE.md § FIRST LIVE SESSION` before treating any read here as this desk's own work, and strike this banner when it is spent.

**Last Updated:** 2026-08-20 16:33 ET — **BUILD SESSION (DAEDALUS, Will-approved in-session).** Agent created off REGINALD's convergence matrix v2.0 (`75f0dd18b`, 16:04 ET the same day), which ranked FLG **🔴 6/6 — 1st of 14 scored banks** after v1 had ranked it **7th of 7, last**, and which REGINALD reported with no thesis file on the name. Build proposal: `AGENTS/DAEDALUS/builds/FLG_BUILD_PROPOSAL_2026-08-20.md`.

**Class:** Market domain — print-driven single-name specialist · **Level:** L1 at birth *(no FLEET_MAP row yet — ROSTER registration is PROME's and lands first, PAT-047)*

---

## 🔴 START HERE — the desk's read changed on build night

**The load-bearing figure on this name is 29% ACL/nonaccrual COVERAGE — not the composite 6/6, and not the 4.88% nonaccrual rate.**

DAEDALUS challenged REGINALD's channel-1 instrument at build (could the SR 07-1 ratio be rising on a shrinking denominator?). REGINALD tested it at the primary the same evening and **REFUTED it** (`fb1f68659`, matrix §3b, verified at artifact): CRE numerator **−32.2%** ($48.33B → $32.76B), capital **flat −2.6%**, ratio **−143pp, falling in all 11 quarters**. **But the answer redirected the desk**, and REGINALD asked explicitly that FLG start from the redirect rather than the composite:

| Channel | Level | Trajectory | Read |
|---|---|---|---|
| CRE concentration | 327.5%, above the 300% line | **−143pp, ~2 quarters from crossing below 300%** | ⬇️ **DE-RISKING — not deterioration** |
| Nonaccrual rate | 4.88%, cohort-worst | **past peak, 5.49% → 4.88%** | ⬇️ improving |
| **ACL / nonaccrual coverage** | **29%, cohort-thinnest** | **87% → 29%, monotonic; ACL$ down 8 of 8 quarters, $1.27B → $0.87B** | 🔴 **THE LIVE SIGNAL** |

The reserve is drawing down **~1.7× faster than the problem book resolves**, against a still-**$3.0B** nonaccrual book. **Two of the three 🔴 legs that created this desk are improving; only reserves are deteriorating.** The open discriminator (`THESIS.md` Q2b, now the desk's primary question): a reserve falls either because losses were *taken and disposed* (healthy) or *released against an unresolved book* (not) — same arithmetic, opposite conclusions. **Pull the ACL roll-forward first.**

⚠️ **Instrument gap this exposed:** the desk shipped with the coverage *ratio* and no **ACL in dollars** — a ratio alone cannot tell those two stories apart. `EXIT_PROTOCOL.md` K-3 now carries the dollars instrument and has been promoted to the primary leg.

---

## BUILD-SESSION FINDING — the flow half

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
| ACL / nonaccrual coverage | **29%** — cohort-thinnest (AMTB 51%, EGBN 88%); **verified at primary 8/20, monotonic from 87%** | REGINALD matrix v2.0 §3b | **PRIMARY-VERIFIED** |
| Total assets | $111.17B (2023-09-30) → **$87.71B** (2026-06-30), **−21.1%** | `MI3_FLG.tsv` | MIRROR |
| Total loans | $85.92B → **$61.19B**, **−28.8%** | `MI3_FLG.tsv` | MIRROR |
| MI3 `v1_pct` | 5.28% → **3.65%** | `MI3_FLG.tsv` | MIRROR |

**The two instruments point opposite ways.** Concentration and credit quality read cohort-worst; the balance sheet reads eleven quarters of contraction with a falling MI3. That is `THESIS.md` Q1 and Q2.

---

## Open questions (priority order — full form in `THESIS.md`)

| # | Question | State |
|---|---|---|
| ~~**Q1**~~ | ~~Is the concentration ratio measuring risk, or a shrinking denominator?~~ | ✅ **ANSWERED + REFUTED same evening at the primary** — capital held flat, so the artifact is impossible here. Concentration thresholds UNBLOCKED (base-rate against a *falling* series). The answer redirected the desk to coverage |
| **Q2b** | Why is the reserve falling ~1.7× faster than the problem book resolves? Taken-and-disposed, or released against an unresolved book? | 🔴 **NEW PRIMARY QUESTION** — needs the Call Report ACL roll-forward (provision / charge-offs / recoveries), in no FLG ledger yet |
| **Q2** | Has the deleveraging bottomed? | 🔴 **LIVE** — one print from resolution (~2026-11-14) |
| **Q3** | Does the rent-regulation mechanism actually transmit? Stages 1–2 are **entirely un-instrumented** | 🟠 Until instrumented, this desk holds a credit observation, not a causal thesis |

---

## Structural state at build

- **Ledgers live:** `MI3_FLG.tsv` (12 quarters, RSSD 694904, `Verified_By` empty = not FLG-verified) · `KB.tsv` (14 rows: 13 seeded + 1 first-hand) · `TRIGGERS.tsv` (7 rows, all `[EST]`/`RULE`-anchored, **none is a registered gate**) · `PREDICTIONS.tsv` (**empty by design** — a seeded prediction would be the architect's forecast, not this desk's).
- **Kill rail:** `workbook/EXIT_PROTOCOL.md`, stamped `Kill rail re-derived: 2026-08-20`, **PROVISIONAL** (authored against the seed; no thesis exists yet). K-1 flagged one quarter from firing.
- ⚠️ **Known always-red flag, do NOT silence it:** `boot.py` leg 1 reports `MI3_FLG.tsv +52d behind STATUS` and will keep doing so, growing to ~135d, every session between quarterly filings. **Expected by construction** — the data clock is the Call Report's own vintage and bumping it would launder freshness (PAT-044). Design-vs-neglect boundary is the **next-due date (~2026-11-20)**, written in the ledger's own header. Root cause is a registered fleet gap now at **n=2**: STATE_VOCABULARY Class 8 has no SCHEDULED/PERIODIC cadence token (REGINALD hit it the same day on `NDFI_COHORT.tsv` and correctly refused to mis-declare). DAEDALUS owns the token; draft at the ~8/28 wiring sweep.
- **boot.py:** 4 legs — ledger staleness · predictions-due · triggers-due · **quarter-due** (Call Report clock). All four paths watched at build per `CHECK_STANDARD.md` §3: clean rc=0, due rc=1, missing-register rc=2, fixtures restored byte-identical.
- **Registration:** ROSTER + root canon are **PROME/Will-scoped and OPEN** — packet routed 2026-08-20. No `FLEET_MAP` row until ROSTER lands (PAT-047 order; `render_directory.py`'s co-registration guard fails loud on the reverse).
- **Parent seam:** REGINALD owns the cohort view and the matrix row. `VX-REG-6.03` was **RULED DUAL-ACTION 2026-08-20 evening** (REGINALD + FLG): **FLG is ON the action line, does NOT edit the row, and DOES act on a fire.** Baseline **FROZEN not rolling** — bands are absolute **$12.82 / $12.10 / $11.39**. At $13.49 the vector sits −5.3%, **53% of the way to band 1** (plain GREEN under-reported that; REGINALD sharpened the token). Tie-break on any disagreed FLG figure: **the primary**, not either ledger.

---

## Next actions (the first-live-session list, in order)

1. **Re-verify the seed at FFIEC CDR** (RSSD 694904), at minimum the two most recent quarters; stamp `Verified_By`.
2. **Recompute the SR 07-1 ratio yourself**, both definitions written out; report the delta against 327.5% whichever way it falls.
3. ~~Answer Q1~~ ✅ **DONE 8/20 by REGINALD at the primary — refuted.** Replaced by: **answer Q2b — pull the ACL roll-forward** (provision / charge-offs / recoveries, 8 quarters) and settle whether the reserve drawdown is disposition or release. **This is now the desk's first analytical job.**
4. **Base-rate the 7 `[EST]` triggers** against the series; retire the ones that do not separate. "Don't build it" is a real answer.
5. **Instrument stage 1 or 2** (RGB series / maturity profile) — without one, Q3 stands unanswered and the seat is unjustified.
6. **Re-derive and re-stamp** `EXIT_PROTOCOL.md`; author `THESIS.md` v1.0 only when its five-point bar is met.
7. **Write back:** STATUS + BOTTOM LINE, PROME packet (gate proposals), REGINALD packet (the step-2 reconciliation).

---

## BOTTOM LINE

**FLG was created because a rebuilt instrument ranked it the cohort's worst bank, and within hours of existing it had helped overturn two of the three readings that justified it.** The desk's own build found the loan book turning positive for the first time in eleven quarters; its challenge to REGINALD's concentration instrument was tested at the primary and **refuted** — capital held flat, so the ratio's 143pp fall is real de-risking, not a denominator artifact — and nonaccruals turned out to be past peak. **What survives is narrower, better evidenced, and genuinely alarming: reserve coverage has fallen 87% → 29% monotonically, with ACL down in all eight quarters, drawn down roughly 1.7× faster than the problem book resolves against a $3.0B nonaccrual pile.** So the desk opens pointed at one live signal instead of three, and it opens knowing the difference matters: a reserve that falls because losses were taken and disposed is healthy, and one released against an unresolved book is not — same arithmetic, opposite conclusions, and FLG cannot yet tell them apart because it shipped with a coverage ratio and no ACL-in-dollars series. **Next: pull the ACL roll-forward and settle Q2b before anything else** — then re-verify the seed at FFIEC CDR, base-rate the seven `[EST]` triggers against a *falling* concentration series, and instrument stages 1–2, which still have no instrument at all. Watches: Q3-2026 Call Report ~2026-11-14 (K-1 one print from firing, DOCKET-registered) · `VX-REG-6.03` dual-action, absolute bands $12.82/$12.10/$11.39, currently 53% of the way to band 1.

