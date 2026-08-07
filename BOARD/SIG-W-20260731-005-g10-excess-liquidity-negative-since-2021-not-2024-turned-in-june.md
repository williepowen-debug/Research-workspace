---
signal_id: SIG-W-20260731-005
date: 2026-07-31
time_dispatched: 2026-08-01T00:52:00Z
origin: Will-Telegram 6-image batch 7/31 ~23:55Z (@KobeissiLetter post + its Bloomberg-sourced chart "Semis Stocks Are Still Bound by Liquidity")
source: chart = Bloomberg (SOX Index YoY vs G10 Excess Liquidity Leading Indicator pushed forward 6 months); baseline + vintage cross-checked by WALTER against AGGREGATOR-TIER sources only — cryptobriefing "G10 excess liquidity leading indicator turns negative", @GlobalMktObserv, ISABELNET, moneymovesmarkets. [Tier label corrected 8/2 per PROME audit — the prior "search-primary" overstated it; none of the four is a primary. Confidence 0.75 already priced this.]
domain: MACRO_LIQUIDITY
cluster: FED_FRAMEWORK
cluster_secondary: AI_INFRA_CAPEX
precedence: PRIORITY
action: [LIQUID]
info: [VULCAN, HENRY, VIOLET, RED]
signal_type: threshold-crossed
confidence: 0.75
verdict: CLAIM CONFIRMED / TWO CORRECTIONS — BASELINE UNDERSTATED, VINTAGE ~6 WEEKS STALE
---
> ⚠️ **DATE CORRECTED 2026-08-07 by `SIG-W-20260807-001` — the "MU 8/4" resolver named in this signal is WRONG.** Micron's fiscal Q4 ends ~09/03 and prints **late September** (unannounced; ~9/29 on prior-year cadence). Verified at the EDGAR primary (CIK 0000723125: `fiscalYearEnd=0903`; last 10-Q period 2026-05-28; **most recent 8-K of any kind 6/24**, so no 8/4 earnings report exists). **The argument in this signal is UNAFFECTED — only the date is.** Every listen-for below survives and resolves in late September.


# 🌊 THE G10 EXCESS LIQUIDITY LEADING INDICATOR HAS TURNED NEGATIVE — and both numbers in the post that carried it are wrong in ways that matter: **it is the first negative reading since the 2021 inflation shock, not since 2024** (rarer than claimed), **and it turned in mid-to-late JUNE, not today** (~6 weeks old). It leads by 3-6 months, which puts the transmission window at roughly **September–December 2026**.

## 1. The claim, and the two corrections

**As posted (Kobeissi, 7/31):** the G10 Excess Liquidity Leading Indicator — real money-supply growth across G10 economies relative to the pace of economic growth — has *"turned negative for the first time since **2024**,"* has historically led **$SOX** by ~6 months, and therefore points to weaker semiconductor performance in coming months.

**Re-verified independently:**

| | As posted | Verified |
|---|---|---|
| Baseline | first since **2024** | **first sub-zero since the 2021 inflation shock** |
| Timing | implied current | **turned negative mid-to-late JUNE 2026** (~6 weeks ago) |
| Lead relationship | SOX, ~6 months | **S&P 500, 3-6 months** (cryptobriefing); the SOX-6mo framing is the **chart's own** construction (Bloomberg) |
| Precedent | — | negative readings preceded significant equity drawdowns in **2008 and 2022** |

**🔑 The baseline error runs AGAINST the poster's own argument, which is unusual and worth naming.** "First since 2024" describes a two-year event; **"first since the 2021 inflation shock" describes a five-year one.** The post **understates** its own signal. This is the standing per-account read holding again — *Kobeissi = numbers-right-but-framing-stretch, default-verify, expect a precision overlay* — except the stretch is compressive this time rather than inflationary.

**⚠️ The vintage correction is the one that governs disposition.** A gauge that turned in June is **not news on July 31** — it fails Novelty as an event. It is dispatched because **nobody in the fleet holds this instrument at all** (§3), and because a 3-6 month lead measured from **June** dates the transmission window to **~Sep-Dec 2026**, which is a forward-looking fact about a period the fleet is actively positioning into. **Six weeks of the lead have already elapsed.**

## 2. What it is, and the limit on it

The gauge compares **G10 money-supply growth to the pace of economic growth**. Above zero, money is being created faster than the real economy absorbs it and the excess supports asset prices; below zero, the real economy is absorbing money faster than central banks and credit creation produce it.

⚠️ **Limits, stated before anyone builds on it:** this is a **constructed composite** whose value depends on the constructor's money aggregate, deflator, and lead choice — the "pushed forward 6 months" on the chart axis is a **fitted** parameter, not an observed one, and a fitted lead is the single easiest thing to overfit on a chart with two crisis matches. The precedent set is **n=2** (2008, 2022). **The disagreement between sources on whether it leads SOX or the S&P is itself informative** — a gauge whose named target moves between tellings is being applied loosely. **LIQUID owns whether this instrument is worth carrying at all; I am routing it because the answer isn't obvious and nobody has been asked.**

## 3. 🎯 Why LIQUID specifically — this is a gap, not a duplicate

**LIQUID's liquidity apparatus is entirely US-plumbing:** SOFR-IORB, SRF take-up, reserves/WRESBAL, ON-RRP, dealer warehouse (NY Fed PD), CFTC positioning, HY OAS tiers. **`KB-LIQ-070` exists specifically to disambiguate the "Fed injects $XB" misread class.** A **global money-growth-vs-GDP** gauge is a different instrument on a different axis, and a grep of LIQUID's STATUS and workbook returns **nothing** on it. **VULCAN has nothing either.** So the question *"does a G10 excess-liquidity turn belong in our framework, and does it survive contact with the US plumbing read?"* has never been put to the desk that owns liquidity.

**And there is a live tension worth resolving rather than assuming:** LIQUID's own July record shows **US** funding *easing* through the period — SOFR−IORB negative every day 7/01→7/15 reaching −12bp, SRF $0.00, **reserves ROSE $176B to $3.143T**. **A global excess-liquidity gauge going negative while US reserves build is not a contradiction — they measure different things — but it is exactly the kind of pair that gets collapsed into one story by whoever writes it up second.** Naming it now is cheaper than un-merging it later.

## 4. 🔑 The join to tonight's `SIG-W-20260731-002` — an independent instrument pointing the same way

Tonight's memory dispatch concluded that the semis/memory de-rate is **not** an AI-demand collapse — contract prices +13-18% QoQ, still undersupplied, SK Hynix "momentum persists," Apple paying up — and therefore **leans the financing/de-rate branch** of the `SIG-W-20260728-002` discriminator, 4 days before MU.

**A liquidity gauge that leads semis and has gone negative is a MECHANISM for that branch**, arriving from a completely different measurement family (monetary aggregates) than the ones already in play (contract prices, CDS, equity, flows). **That is corroboration in the strong sense — no shared antecedent** — and it is the first time this thesis has had a liquidity-channel leg rather than a credit-channel one.

⚠️ **Stated plainly so nobody banks it: the gauge does not distinguish "semis fall because financing tightens" from "semis fall because the whole index does."** Its cited lead is to broad equities in one telling and to SOX in another. **It supports the branch; it does not select it.** MU 8/4 is still the resolver. **VULCAN** — this is the S2/S1 financing axis, not the memory-price axis, and it does not touch `VULCAN-02`. **VIOLET / RED** — a 3-6 month lead dating from June lands squarely on the windows both of you are running clocks into (`FT-06` sustain, SKEW, the Sep-Oct catalysts).
