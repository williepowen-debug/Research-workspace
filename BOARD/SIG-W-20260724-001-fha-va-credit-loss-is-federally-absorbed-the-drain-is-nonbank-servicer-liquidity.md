---
signal_id: SIG-W-20260724-001
dispatched: 2026-07-24T23:20:00Z
origin: DEWEY deep-research deliverable (WALTER Phase-2.8 flag REQ-DEWEY-20260702-011 / Batch-2 #15, prompt `DEEP-RESEARCH-PROMPT-15-fha-va-loss-waterfall.md`) returned via `AGENTS/WALTER/inbox/DEWEY/` handoff, consumed at WALTER boot step 7d 2026-07-24.
source: DEWEY report `AGENTS/DEWEY/output/2026-07-24_fha-va-loss-waterfall.md`
signal_type: research-output
domain: BANK_CRE
cluster: BANK_COLLATERAL
cluster_secondary: CONSUMER_STAGFLATION
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: [REGINALD]
info: [CARL, CORAL, RED]
confidence: 0.80
confidence_note: Observation confidence HIGH and interpretation confidence HIGH on the load-bearing half — the waterfall mechanics and the federal-absorption verdict are PRIMARY/verbatim-confirmed (Ginnie Mae MBS Guide, HUD Mortgagee Letters + OIG, GAO, FSOC, HUD FY2025 MMI report). Interpretation confidence drops to MEDIUM on the weakest-link RANKING, and DEWEY says why rather than smoothing it: the private nonbanks (Freedom / Lakeview / Carrington) disclose NEITHER their own FHA-DQ rate NOR advance-facility utilization, live 2025-26 rating pages were 403-blocked (KBRA/S&P/Moody's/Fitch), and VA foreclosure counts come from advocacy/press rather than VALERI-primary. The rank order is an inference from disclosed leverage + concentration, not a measured stress reading.
verify_verdict: VERIFIED-PRIMARY on the core (MMI capital ratio 11.47% FY2025 = record, 5.7× the 2% statutory minimum, $188.9B; VA guaranty 25-50%; GSE exposure ~zero; PFSI FHA 60+ DQ 8.0% vs VA 1.7%; PFSI advance-loss provision $4.2M → $20M = 5× YoY; HUD OIG non-reimbursable curtailment $2.09B across 239K properties). No WALTER verify-spawn (Phase 2.8b — DEWEY primary-pull spine, SEC EDGAR 10-Qs + HUD primaries, carve-out-validated).
verify_method: DEWEY primary-pull spine (SEC EDGAR PFSI + RKT 10-Qs, HUD FY2025 MMI report = the three load-bearing quanta) + `/deep-research` fan-out (9 finders / 49 agents / 2.42M tokens / 0 errors; 40 adversarial-verify agents).
deep_research_ref: Closes `DEEP_RESEARCH_FLAGGED_LOG` row REQ-DEWEY-20260702-011 (QUEUED → RESOLVED-LATE / executor DEWEY). Last live Batch-2 prompt.
routing_note: Deep-research output archived per CHECKLIST Phase 2.8b. **DELIVERY ALREADY EXECUTED BY DEWEY at write-time** (Constrained-B, 2026-07-19): create-only stubs landed for REGINALD (action) + CARL / CORAL / RED (info) — **WALTER verified all four landed; CARL and RED had already CONSUMED theirs before this boot.** No duplicate `inbox/WALTER/` handoff and no `delivery_log` row is written for this signal — a second copy would be noise, and the same skip logic as §3.5 applies. This BOARD entry is the ARCHIVE + the discovery surface for the whole-INDEX pullers. REGINALD action because it commissioned this (Path C residential-collateral leg lives or dies on it) and the answer is a KILL on the channel it was watching.
dispatch_note: The prompt's `deliver_by` (7/14, ahead of the 7/16 bank prints) had passed by 10 days at run time — the question survived the miss because the 7/20-21 big-bank prints rested on the CRE credit line, a different channel. This is the exact rot the new `kill_condition:` field (CHECKLIST v0.27, shipped this session) is built to catch.
---

# FHA/VA credit loss is FEDERALLY ABSORBED — kill the bank-LGD channel; the surviving transmission is a servicing-advance LIQUIDITY drain on NONBANK Ginnie servicers
> ⚠️🔴 **CORRECTED 2026-08-18 (retroactive §3.6.1 backfill) by [`SIG-W-20260724-007`](SIG-W-20260724-007-bku-is-the-one-fl-bank-that-must-not-be-switched-off-repoint-dont-drop.md). Additive marker — nothing below is edited. Backfilled at the ~14d staleness sweep because a `corrects:` header points only FORWARD, and the reader who lands HERE never sees it.**
>
> ✅ **WHAT SURVIVES — the VERDICT, and it is STRENGTHENED.** 🔴 **WHAT IS CORRECTED — the SUPPORTING EVIDENCE, and it inverts one action.** This signal's load-bearing sentence — *"documented current bank EBO balances are immaterial — Wintrust $187.8M vs a multi-billion equity base"* — is **FALSE as a general claim.** **BKU (BankUnited) holds $851M of Buyout Loans ($883.4M gov-insured) plus an $877M warehouse (+40% YoY) = ~58% of equity combined — ~4.5× Wintrust in DOLLARS and ~20× relative to EQUITY.** ⇒ **BKU must NOT be switched off — RE-POINT it.** SSB, SBCF and AMTB are clean and do drop (AMTB keeps a disclosure-gap watch). **Origination share was the wrong metric, and BKU is the proof.**


**WALTER routes + extracts the per-recipient delta — this is NOT WALTER re-analysis.**

## 🚩 STRESS-TEST RESULT — added 2026-07-25 (WALTER, PROMPT-19, 4-axis adversarial re-test). **VERDICT SURVIVES AND IS HARDENED. SUPPORTING EVIDENCE FALSIFIED IN 3 PLACES.**

Commissioned by Will as a direct follow-up to this signal. Full record: `AGENTS/DEWEY/output/2026-07-25_PROMPT-19_fha-va-kill-stress-test-SYNTHESIS.md` (ledger `REQ-DEWEY-20260724-019`).

**✅ WHAT SURVIVES — and is now stronger than when dispatched.** The federal-absorption verdict holds, and is corroborated at NAME level by a party with money at stake: **BankUnited holds $851M of BOUGHT-OUT DEFAULTED FHA/VA paper and reserves ZERO against it** — *"the ACL is zero for these loans"* *(BKU FY2025 10-K, on the government guarantee)*. That is better evidence than anything in the original dispatch.

**❌ FALSIFIED #1 — "documented current bank EBO balances are immaterial (Wintrust $187.8M)".** FALSE as a general claim. **BKU: $851M = 28% of equity, plus $877M mortgage warehouse growing 40% YoY = ~58% of equity combined** — 4.5x Wintrust in dollars, ~20x relative to equity. The sector statistics (~5% of Ginnie originations bank-originated; 83-96% nonbank servicing) could not refute an idiosyncratic concentration. **The other three FL names ARE clean, with figures: SouthState 0.8% / Amerant 5.9% / Seacoast <=2.7% of equity, ZERO FHA/VA at all three, ZERO servicing-advance facilities at all four.**

**❌ FALSIFIED #2 — the Urban Institute ">5x foreclosure rates" cushion citation. STRIKE IT.** July-2025 brief whose own text cites **FY2024** (FY2024 and FY2025 are BOTH 11.47% — a coincidence that hid the vintage error), so it rests on **Sept-30-2024 data, ~22 months stale**. It is not a model but a two-step multiplication, and it commits a **flow-vs-stock error**: "2.5% annual losses well below the buffer" holds for ONE year; sustained five (GFC duration) it is 12.5% and EXCEEDS the buffer. It also asserts capital resources are delinquency-insensitive, which is false. **Replace with FHA's own Exhibit II-27 sensitivity ladder + the ">6.07% cash-alone" floor.**

**❌ FALSIFIED #3 — "record 11.47%" should NOT be cited as a clean cash cushion.** **~47% of it is not cash**: 2.99pp NPV projection + ~2.41pp partial-claim receivables/REO, the latter sitting behind a **~58-60% one-year re-default rate** (rising; 2009-2019 avg 46%), with **~40% of Sept-2025 loss-mit recipients on their THIRD option in five years**. The actuarial review mentions "redefault" **once in 381,721 characters** and never models it; the actuary explicitly declines the cost-benefit question. **BUT the magnitude does not threaten the verdict: zero the ENTIRE receivable and 11.47% -> 9.78%, still 4.9x the floor; cash alone is >6.07% of IIF, >3x the floor and growing.**

**🔎 WHAT THE ORIGINAL MISSED ENTIRELY — a richer surface.** FHA publishes a **QUARTERLY Report to Congress (12 U.S.C. 1708(a)(5))** with a statutorily-compelled predicted-vs-actual table. FY2026-Q1: **claim counts -57.4% vs forecast, claim dollars -50.8%, net loss on claims +7.75pp (+30.9%)** — volume deferred, severity deteriorating. **Q2 edition ~3 months OVERDUE.** Also new: **ROAD to Housing Act Sec. 702 (Pub. L. 119-101, law 2026-07-11)** mandates MONTHLY capital-ratio reporting — legally the full actuarial ratio (12 U.S.C. 1711(f)(4)(C)), though with no funding (Sec. 1202), no methodology and no monthly NPV input it will likely arrive as a cash update in the ratio's name. Verified at two primaries incl. the enrolled bill.

**🔻 REFUTED HYPOTHESES (WALTER's own, recorded as refuted):** MIP political self-erosion — **premise wrong**, 2 of 3 historical cuts came AT OR BELOW the statutory floor (2015 at 0.41%), so the ratio does not drive the policy; nothing proposed/enacted for FY2026-27. Post-VASP counterparty growth — **mechanism confirmed, magnitude REFUTED**: BKU's book, the one measurable instance, **SHRANK 19%** across VASP termination.

**⚠️ CORRECTIONS TO THIS SIGNAL'S OWN CITATIONS:** VASP termination instrument is **Circular 26-25-2 (issued 2025-04-23, eff. 2025-05-01)**, not "announced 4/3/25 / Circular 26-23-25". **ML 2025-06 was superseded by ML 2025-12.** The VA advocacy figures carried as leads survive **as counts but NOT as causal evidence** — ~80,000 VA loans were already seriously delinquent **seven weeks BEFORE** VASP terminated, so the gap-attributable increment is ~10,000, not 90,000.

**➡️ ROUTING CONSEQUENCE (delivered to REGINALD 2026-07-25):** switch off **SSB / AMTB / SBCF** with confidence; **DO NOT switch off BKU — re-point it.** Its watch is no longer FHA/VA credit loss (ACL is zero) but (i) warehouse growth + undisclosed counterparty identity, (ii) the 90+ delinquent share inside the buyout book (**+24% QoQ** against a shrinking stock), (iii) resolution-timeline risk that HUD's new waterfall lengthens. **BKU is the fleet's one direct wire between a watched regional bank and the nonbank-servicer credit this signal says to trade instead.**

---

## Verdict (one line)

**SPLIT.** The **credit** loss on FHA/VA is absorbed by federal insurance before it can reach a bank balance sheet — so **REGINALD's "regional bank eats the FHA/VA loan loss" channel is KILLED.** What survives is a **liquidity/servicing-advance drain on nonbank Ginnie Mae servicers**, which reaches banks only second-order as warehouse/EBO financiers — and which points at **Freedom Mortgage and Apollo/Atlas SP**, *not* at the FL-heavy regionals REGINALD actually grades.

## The three things a router needs

1. **Credit loss absorbed — not "mostly," structurally.** The FHA **MMI capital ratio is 11.47%** (FY2025, a record) — **5.7× the 2% statutory minimum**, $188.9B. VA carries a **25-50% guaranty**. GSE exposure is ~zero. Ginnie Mae insulates the investor. **There is no principal-LGD path to banks or the GSEs.**
2. **The drain lands on nonbank Ginnie servicers.** They must advance P&I until resolution *and* fund 90+dpd buyouts at **100% of remaining principal balance**, with **no Fed and no FHLB backstop**. Curtailment is non-reimbursable — HUD OIG counts **$2.09B across 239K properties**. The stress is showing in the disclosures: **PFSI's advance-loss provision went $4.2M → $20M, 5× YoY.** **FHA is the leg, not VA** — PFSI FHA 60+ DQ **8.0%** vs VA **1.7%**.
3. **Weakest-link rank (the tradeable end).** **#1 Freedom Mortgage** — concentration × the highest leverage among peers (2.2×) × an unhedged MSR book; KBRA BB+ / S&P B; **15.5% of the Ginnie delinquent population**; the **$500M 7.875% 2033 notes are the cleanest expression**. **#2 loanDepot** (FY25 −$108M, worsening). **#3 Lakeview/Bayview** (18% of Ginnie DQ population, #2 servicer — but private, Bayview $36B AUM and growing). **PFSI and Rocket/Mr. Cooper (folded 10/1/25, $2.11T serviced) are NOT weak** and are covenant-compliant.

## Why the bank channel actually fails

Banks **exited FHA/VA origination** — roughly **5% of Ginnie originations**. Direct bank rebooking under **ASC 860** exists as a mechanism, but documented bank EBO balances are immaterial (**Wintrust $187.8M against multi-billion equity**). So even the surviving liquidity leg does not arrive at a regional bank in size.

## Per-recipient delta

| Recipient | The delta |
|---|---|
| **REGINALD** (action) | The leg you commissioned this to test is **dead as a bank-LGD story**. Path C keeps a residential-collateral leg, but it now points at **nonbank servicers + Apollo/Atlas SP**, not at BKU/SSB/AMTB/SBCF. Your FL-heavy small-tier watch prints **7/22-28** — this says do not read those prints for an FHA/VA loss channel that cannot reach them. |
| **CARL** (info) | Consumer/foreclosure inflection: **FHA DQ 11.88% Q1-26, highest since Q2-21**; SDQ **+212bps YoY**; FHA-conventional spread **~900bps**. The **VASP-termination gap** (5/1/25 → PCP 6/15/26) is a real VA-foreclosure accelerant. Student-loan default resumption feeds FHA DQ — **aggregate-corroborated, not isolated**, so don't treat it as a clean single-cause. |
| **CORAL** (info) | **FL is the #1 foreclosure state H1-2026** (0.27%, +33% YoY); FHA distress is Sun-Belt-concentrated. FL condo/insurance overlay stays yours and is out of this scope. |
| **RED** (info) | For the beat/miss tree: the tradeable expressions of the FHA/VA leg are **nonbank-servicer credit (Freedom bonds) and Apollo**, NOT regionals — and there is **no confirmed discrete servicer stress event yet.** Mechanism-live, event-not-yet. |

## Honest ceiling (DEWEY's own, carried verbatim in substance)

Waterfall mechanics and the absorbed-credit verdict are primary-confirmed. **The weakest-link ranking is medium-confidence** — private nonbanks disclose neither their own FHA-DQ rate nor advance-facility utilization, and the live rating pages were 403-blocked. **"Federally absorbed" describes where the CREDIT loss lands. It is explicitly NOT an all-clear on servicer liquidity, which is the live risk.**

## Router's note

This is a clean instance of the class where the **classification decides the trade**: the same asset is credit-loss-absorbed (dead to banks) and simultaneously alive on the servicer-advance/liquidity axis. Killing the channel on the first read alone would have thrown away the surviving one.
