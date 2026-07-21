# DEWEY → WALTER handoff — research-output ready to route

**State:** NEW · **From:** DEWEY · **Date:** 2026-07-20
**Flag:** SIG-W-20260720-001 (WALTER Phase-2.8, Will-directed same-session — UBS/Nationwide insurance-wrapped PC deep-dive)
**Report:** `AGENTS/DEWEY/output/2026-07-20_insurance-wrapped-private-credit-ubs-nationwide.md`
**Mode:** Thesis · **Confidence:** High (deal tranching · NAIC trajectory · the date correction) / Med (guarantor entity + wrap instrument) / **Low–GAP (Nationwide concentration — not public)**

> **Delivery note (constrained-B, Will 2026-07-19):** DEWEY main session has **already written create-only pointer stubs** into the named recipients' inboxes: **SHADE, BROCK, NEXUS** (action) + **LIQUID, REGINALD** (info). Please **verify they landed and deliver any I missed**, log the `research-output` signal, and own the ledger/audit + backstop. This is the **first DEWEY run under constrained-B** — the DEWEY-lane README is pre-constrained-B (single-entry-point wording); CLAUDE.md 7/19 supersedes it. Flagging the README as a light refresh candidate.

---

## One-line verdict

**The UBS/Nationwide deal is CONFIRMED exactly as reported — a $500M CFO (8 evergreen PC funds) tranched $375M A2-Moody's insured senior + $125M first-loss equity, Nationwide Mutual guaranteeing so the senior sells as IG at <1% RBC vs ~30% direct — but it stays a PRE-MORTEM: no wrapped-tranche downgrade, no wrap-provider downgrade, no forced-sale has printed (distinct from the fund/BDC-level downgrades already happening).** Two load-bearing catches: (1) the **guaranteeing Nationwide entity is not public** and determines whether the wrap is A1 (Life) or A2 (P&C); (2) the tasking's **"A2 IFS 2026-01-20" is a vintage error** — the A2 is a **Nov-2023 P&C** action (Life affirmed A1); no Jan-2026 action exists.

## Confirmed spine
- **$500M / $375M A2-senior / $125M equity** — confirmed exactly [Bloomberg 4/7 via Yahoo syndication]. Equity = 25% first-loss subordination *ahead of* the senior guarantee (insurer takes tail, not first-loss).
- **NAIC partly ENACTED, not just proposed:** SVO 3-notch tool **eff 2026-01-01** (names CFOs + rated-note feeders); CLO RBC factors **adopted** (WG 6/23 → cmte 7/8) **eff YE-2026** (11.77% thin-tranche surcharge on sub-Baa3 BSL ≤4% thick; 45% residuals; senior IG eased); collateral-loan RBC adopted 6/11 **eff YE-2027**; Bessent–NAIC convening **5/7** = engagement only, no rule, nothing after 5/8 [Treasury sb0493 + NAIC.org primaries].
- **Nationwide-as-guarantor** is named only in **LATER syndication**, NOT the 4/7 wire — provenance nuance before it's cited as primary.

## Routing (DEWEY suggestions; WALTER decides)

| Recipient | Why | Disposition |
|---|---|---|
| **SHADE** | PE-insurer nexus owner — this is the wrap mechanism itself. Needs: the guarantor-entity ambiguity (A1 Life vs A2 P&C), the date correction, the 5 named tripwires (esp. T5 Nationwide Schedule-BA concentration = a SHADE statutory-filing check), and the model-vs-wave distinction (UBS wrap ≠ Apollo/Athene captive). | **ACTION** |
| **BROCK** | Private-credit owner — the underlying is 8 evergreen PC funds; T2 (first CFO/rated-feeder TRANCHE downgrade) and T4 (fund-gate on the underlying) are BROCK monitorables; NAIC RBC trajectory governs whether the wrap wave accelerates or gets capital-charged. | **ACTION** |
| **NEXUS** | PRED-24 indirect channel — the wrap is the "credit's honest mark hasn't printed yet" thesis in structured form: IG label over opaque illiquid collateral, wrapped-level stress NOT yet observed while fund-level stress is. | **ACTION (PRED-24)** |
| **LIQUID** | Credit-transmission — the capital-arbitrage (<1% vs ~30% RBC) is a spread/demand engine for IG; NAIC RBC dates are repricing catalysts. | info |
| **REGINALD** | Bank/insurer collateral surface — UBS (bank) originates + de-risks via an unaffiliated insurer guarantee; the concentration question bears on insurer-sector collateral. | info |

## Counter-evidence (carry it)
The Oliver Wyman/BILTIR "not systemic" voice was **NOT directly evidenced** — carry as unverified analyst posture, steelmanned in the report (§Counter-Evidence): idiosyncratic risk-transfer onto a $8.98T-industry / large-mutual balance sheet, real 25% equity subordination, small/nascent, regulators already tightening. **It breaks on the one unmeasurable fact — how much wrapped paper concentrates on how few guarantors (Q3/T5) — which is not public.** Credible only if concentration resolves benign; currently unfalsified, not confirmed.

## Honest ceiling
Deal mechanics rest on **Bloomberg-syndicated secondary** (Yahoo/GuruFocus/ZeroHedge) — **the two Bloomberg primaries were NOT recovered** (archive.ph CAPTCHA, Wayback zero-snapshot on the 7/19 feature, GuruFocus/SeekingAlpha 403). Exact wrap instrument, guaranteeing entity, Nationwide concentration, AG-55/bond-definition status, and whether 7/19 = a second deal all remain **documented gaps**, not silent drops.

---
*Engines: full `/deep-research` fan-out (98 agents, 4.24M tok, ~12 min, 0 err, 22/25 claims confirmed) + DEWEY primary-pull carve-out (deal figures, NAIC dates, Treasury/NAIC primaries, Nationwide rating tier-split + date fix) + a focused residual pass (Nationwide capacity, wave breadth). Per README: DEWEY only CREATES here; WALTER owns the `git mv` to `processed/`.*
