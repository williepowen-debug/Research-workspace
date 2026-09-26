# DOCKET L321 — HAW-19 capacity-only successor · REGISTRATION FINDING

> ✅ **OVERTAKEN 2026-09-26:** Will ruled **A** (WQ-296, 15:04 ET). R1 below is now **registered as HAW-22** in `thesis/PREDICTIONS.tsv` (KB-HAWK-414), 65% UNCALIBRATED, with the undisclosed-damage warning on the row. This file's verdict is the dated 9/25 record; the filename is kept for pointer stability.

**Written:** 2026-09-25 12:3x ET, HAWK, PROME Tier-1 WQ-184 due-row spawn (prome-2e). **Ruling served:** WQ-212 (Will APPROVE 2026-09-10 20:45Z). It requires a prospective capacity-only successor with separate event/observation windows 2026-10-01 → 2026-12-22, its own disclosure test on the row, and D3 left unparameterized (A.2 satisfiable by (a) alone), registered before 10/1. $0 · no score, confidence or threshold moved · `thesis/PREDICTIONS.tsv` NOT edited.

## Verdict: ⛔ NOT REGISTERED. The successor as proposed and approved CANNOT be registered from this desk. This is a finding for Will, not a slipped deadline.

**Why, in one sentence:** Will approved HAWK's 9/8 proposal. That proposal's measurement is a **dual-vendor (Kpler + Vortexa) daily terminal-loading agreement test**, and its own text says *"Do not register if the required data cannot be obtained."* As of 2026-09-25 neither vendor is reachable, so the approved letter's own stop condition has fired.

## The registration-readiness checklist (from `design/HAW19_MEASUREMENT_DRAFT.md`), checked today

| Requirement | 2026-09-25 state | Token |
|---|---|---|
| Usable Kpler access (terminal crude series, realized-only, snapshot dates) | No credential, connector or env var on this box. `grep -ril "kpler\|vortexa"` over `FORGE/tools/`, `scripts/` returns nothing. No WILL_QUEUE row records an answer to the 9/8 "does the team have a subscription?" question | SEARCH-NOT-FOUND (a subscription held elsewhere is not excluded) |
| Usable Vortexa access, same population and dates | Same | SEARCH-NOT-FOUND |
| One matched 73-observation fixture (28 baseline + 45 post-event days per vendor) with snapshot clocks | Not possible without the above | VERIFIED absent |
| Complete terminal / product / loading-path inventory for both theaters, with dated operator/technical evidence | Not built. Path inventories need operator documentation plus imagery per terminal | VERIFIED absent |
| Probability calibration against a disclosed comparison set (incl. CPC SPM-2, Nov 2025) | Not assembled. The draft 65% is a subjective placeholder | VERIFIED absent |
| Fresh disclosure audit | Can be written (see §R1 below). This is the only item HAWK can close alone | — |

**Consequence:** registering the approved letter today would put an **instrument HAWK cannot read** on the ledger. It would resolve STUCK by construction on 12/22, which is the same class of defect WQ-212 just ruled HAW-19 to be. `[[finding_discovery_instrument_defines_the_claim]]`.

## Why HAWK does not simply register a redesign on its own authority

The 9/8 proposal said *"Narrow/redesign if evidence remains unobtainable."* The approved text also carries the stop condition quoted above. Every feasible redesign **replaces the measured-throughput leg with a disclosure leg** (what operators or sovereigns *declare*). That changes what the claim measures. It is a new instrument, and Will has not seen it. **HAWK drafts it in full below for a one-word ruling; HAWK does not register it.**

## R1 — the redesign, written in full for Will's word (UNREGISTERED DRAFT)

**Proposed ID:** HAW-22 · **Proposed confidence:** 65%, the v2 draft's placeholder carried unchanged. It is a subjective analyst estimate, **not calibrated and with no measured base rate**, and is disclosed as such. ⚠️ It is deliberately NOT raised. R1 has fewer conditions than v2, so a qualifying event is if anything more likely. R1 also grades CONFIRMED on undisclosed destruction, but raising the number on that ground would price in the instrument's blind spot.

**Claim (DECLARED-capacity-loss, not measured throughput):** Between **2026-10-01 00:00 UTC and 2026-10-31 23:59 UTC** (EVENT window), no crude-oil export terminal in either theater (Russia/Ukraine-linked or Iran/Gulf-linked) sustains NEW physical damage that meets ALL of:
1. **Damage:** confirmed physical damage at a named crude-export terminal. Confirmation means an operator or sovereign primary, or two independent Tier-1 outlets each citing a named source. A claim is not a confirmation.
2. **Path, A.2(a) only (D3 unparameterized):** the damaged unit is, or disables, the terminal's **only operable crude loading path**. Either the sole berth/SPM, or a shared bottleneck (feed pipeline, pump station, tank farm manifold) that serves every berth. Evidence must be operator or technical documentation. **If the path inventory cannot be established, the candidate is UNRESOLVED and never counted as absent.**
3. **Declared irreversibility:** by **2026-12-21 23:59 UTC** (OBSERVATION cutoff), the operator, sovereign or a named technical assessor publishes a **damage-attributed force majeure** or a **restoration estimate of ≥90 days**.
- **Explicit non-fires:** security or threat closures without damage (e.g. CPC's harbormaster stop, Nov 2025); refinery/products terminals; gas/LNG/condensate/GTL; pipeline damage upstream of the terminal fence; hull or cargo losses; sanctions actions. Damage that occurs before 2026-10-01 does not qualify, even if disclosed in-window.
- **Resolution 2026-12-22 (IMMOVABLE anchor):** **FAILED** if any candidate meets 1+2+3. **CONFIRMED** only on a dated search log: FALCON and OSPREY ledgers, operator press pages (Transneft, CPC, Aramco, NIOC/NIOC-affiliates, SOMO, ADNOC, KPC), and the WALTER lane for the event window, with a final search between 12/15 and 12/21. **UNRESOLVED-CANDIDATE** (no verdict, no calibration credit) if any candidate meets 1+2 but 3 is neither met nor excluded at cutoff.
- ⚠️ **What this letter measures, stated on the row:** it measures **disclosed** irreversible loss. A terminal destroyed and never declared (the base case for Transneft, which rarely publishes force majeure) can make the row CONFIRM wrongly. The UNRESOLVED-CANDIDATE band catches the case where damage is confirmed but not declared. It **cannot** catch the case where damage is undisclosed. That is the price of dropping the vendor leg, and Will should decide knowing it.

**Disclosure test, contemporaneous (what HAWK has read as of 2026-09-25 that bears on crude-export terminals):** the Saudi Petroline shutdown (pipeline, MoE 9/11; Reuters dates it 9/13) and a restart reported 9/22 by three unnamed sources "at a low rate", Aramco no comment (WALTER SIG-W-20260924-002/-010). Rubio attributed Petroline to Kataib Hezbollah on 9/22. Houthi missiles at Yanbu/Taif 9/24 were **intercepted** per the coalition, with no established impact (SIG-015). Novorossiysk 9/9 was a fuel-oil/products terminal (OSPREY correction 9/15). Hormuz hull hits 9/18–9/23 caused no terminal damage. CPC SPM-2 (Nov 2025) is a known component-damage case. **All of these predate the event window and none qualifies.** Their existence is disclosed because they shape the 65%. The Gulf war is active, and Houthi fire at Yanbu shows a Red Sea terminal is inside the target set. That is the main reason the number is not higher.

## Ask (for PROME to carry to Will)

**⚖️ One decision, needed by 2026-09-30 so any registration still precedes the 10/1 window:**
- **(A) Register R1 as written** (HAWK registers on the word, same session). *HAWK's recommendation:* it keeps a prospective capacity claim on the book with the disclosure caveat on its face.
- **(B) Register no successor.** HAW-19 closes 9/30 as DEFECTIVE INSTRUMENT and the capacity question goes unforecast until vendor access exists.
- **(C) Buy or confirm vendor access,** then register the v2 letter later with fresh windows. This is a spend question (Tier 3), not HAWK's.

Nothing on DOCKET L321 is re-dated by HAWK. PROME owns that cell. Suggested state: *NOT MET — finding delivered 9/25, successor blocked on data; Will's A/B/C owed by 9/30.*

KB-HAWK-412.
