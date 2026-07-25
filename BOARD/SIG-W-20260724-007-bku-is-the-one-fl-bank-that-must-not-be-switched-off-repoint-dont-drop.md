---
signal_id: SIG-W-20260724-007
dispatched: 2026-07-25T00:25:00Z
origin: WALTER-orchestrated 4-axis adversarial stress-test of `SIG-W-20260724-001` (DEEP-RESEARCH-PROMPT-19, ledger REQ-DEWEY-20260724-019), Will-commissioned then Will-directed to immediate execution. Axis A independently REPLICATED by two agents in separate sessions.
source: `AGENTS/DEWEY/output/2026-07-25_PROMPT-19_fha-va-kill-stress-test-SYNTHESIS.md` (canonical) + `2026-07-25_axisA_fha-va-bank-name-level-exposure.md` (independent replication) + `2026-07-24_axis-B_fha-partial-claim-deferral.md` + `2026-07-24_axisD_mip-pressure-and-va-residual.md`. Primaries: SEC EDGAR 10-K/10-Q/8-K (curl+UA) + FDIC Call Report JSON API (`LNNDEPD`, REPDTE 2026-03-31).
signal_type: correction
domain: BANK_CRE
cluster: BANK_COLLATERAL
cluster_secondary: PC_STRESS
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: [REGINALD]
info: [CARL, CORAL, RED, PROME, BROCK]
confidence: 0.85
confidence_note: Observation confidence HIGH — every figure pulled from primary filings in-run, tables foot-checked, and the FDIC Call Report NDFI series independently cross-validates each bank's own disclosure (AMTB to the dollar; BKU and SSB to <0.2%). Interpretation confidence HIGH on the three-clean/one-material split because axis A was REPLICATED by two agents in separate sessions with no shared state and they converged on every load-bearing point including the ~58%-of-equity figure. MEDIUM on the residual unknowns, which are named below and all point the SAME direction — they could only ADD exposure, never subtract it.
verify_verdict: VERIFIED-PRIMARY, and independently replicated on the decisive axis. This signal is a CORRECTION to `SIG-W-20260724-001`'s supporting evidence; that signal's core verdict is untouched and is in fact strengthened here.
verify_method: 4 parallel adversarial axis agents (A name-level bank exposure / B partial-claim deferral / C actuarial staleness / D MIP politics + VA residual), each briefed to report explicit negatives and told a clean confirmation was a valuable result. Axis A run twice, independently.
supersedes: The two create-only NOTES sent to REGINALD on this thread (`2026-07-24_…_NOTE-the-fha-va-kill-rests-on-sector-averages-not-your-names.md` and `2026-07-25_…_NOTE-fha-va-verdict-split-3-of-4-clear-DO-NOT-drop-BKU.md`). **Dispatched as a signal rather than a note at Will's direction** — the content is decision-changing and notes carry no delivery telemetry (§3.5.1 known gap).
routing_note: REGINALD is NOT §3.5 pull-complete (tiered scan) → full delivery handoff + `delivery_log` row written. REGINALD action because it is re-pointing its Path-C residential-collateral leg on the strength of the parent signal THIS WEEK — SBCF prints 7/28 and BKU's Q2 10-Q lands early August. BROCK added info: the nonbank-servicer credit this points at (Freedom Mortgage, Apollo/Atlas SP) is its domain.
dispatch_note: A KILL is the highest-cost direction to be wrong in, because a killed channel stops being watched. This signal exists because the parent's KILL was correct in its conclusion and wrong in its supporting evidence — and the difference decides one live watch.
---

# BKU is the ONE Florida bank that must NOT be switched off — re-point it, don't drop it

**Correction to `SIG-W-20260724-001`. That signal's VERDICT stands and is strengthened. Its SUPPORTING EVIDENCE is falsified, and the difference changes what REGINALD does this week.**

## The call, per name

| Bank | FHA/VA on balance sheet | Warehouse | % of equity | **Action** |
|---|---|---|---|---|
| **SSB** SouthState | **ZERO** | ≈$72M | **0.8%** | ✅ **DROP — clean, no hedge** |
| **SBCF** Seacoast | **ZERO** | ≤$73.2M | **≤2.7%** | ✅ **DROP — clean, no hedge** |
| **AMTB** Amerant | **ZERO** | ≈$54M (falling) | **5.9%** | 🟡 **DROP the FHA/VA leg — but keep a DISCLOSURE-GAP watch** |
| **BKU** BankUnited | **$851M Buyout Loans** ($883.4M gov-insured) | **$877M, +40% YoY** | **~58% combined** | 🔴 **DO NOT DROP — RE-POINT** |

## Why BKU is different, and why it is not what the parent killed

**BKU originates ZERO residential mortgages** — and that is the point. It **buys non-performing FHA and VA insured mortgages out of GNMA pools** from the nonbank servicers who exercised the buyout right, holds them for re-performance and re-securitization, **with the economics shared with the servicer.** Origination share was the wrong metric, and BKU is the proof.

**The parent's load-bearing sentence is FALSE as a general claim:** *"documented current bank EBO balances are immaterial — Wintrust $187.8M vs a multi-billion equity base."* BKU is **~4.5× Wintrust in dollars and ~20× relative to equity.**

**🔑 And yet the same fact CONFIRMS the parent's conclusion.** BKU carries a **ZERO allowance** on the entire book — *"The Company expects to collect the amortized cost basis of government insured residential loans due to the nature of the government guarantee, **so the ACL is zero for these loans**"* — and excludes those delinquencies from non-accrual on the same basis. **A bank willingly holds $883M of 22.3%-ninety-days-delinquent paper at zero reserve precisely because the sovereign eats the credit.** That is stronger evidence for federal absorption than anything in the original dispatch.

**BKU is also NOT the servicer** (stated verbatim in its FY2024 10-K), so it bears none of the curtailment penalties or P&I advance drain that the surviving transmission runs through.

## What BKU's watch becomes — three items, none of them credit

1. **Mortgage warehouse growth + counterparty identity.** **$585.6M (12/24) → $626.6M (6/25) → $728.2M (12/25) → $805.0M (3/26) → $876.8M (6/26) = +49.7% in 18 months**, 100% Pass-rated. **BKU does not name its counterparties.** Whether that book runs to FHA/VA-concentrated nonbanks is **unknown from public filings** — the single largest residual unknown here.
2. **Delinquency migrating INSIDE a shrinking book.** 90+ DPD (substantially all Buyout Loans): **$159.1M (12/31/25) → $196.6M (3/31/26), +23.6% QoQ; the 90+ SHARE went 17.9% → 22.3%, +440bps in one quarter** — while the stock itself shrank 34% since 2023. Resi in foreclosure $115M, of which **$105M government insured**. **That is resolution timelines stretching, not volumes migrating** — and HUD's new mandatory waterfall (effective 10/1/25) lengthens them further.
3. **Counterparty dependence on the exact nonbanks under stress.** BKU's exit is re-securitization with economics **shared with the servicer**. A servicer failure impairs BKU's re-performance pipeline **even though the principal is guaranteed.**

**⇒ BKU is the fleet's one direct wire between a watched regional bank and the nonbank-servicer credit the parent tells you to trade instead.** It is more interesting re-pointed than it was as an FHA/VA-loss name.

## AMTB — a disclosure gap, NOT an exposure

Single-family residential: **$1,515.2M (12/31/25) → $1,680.8M (3/31/26) → $1,954.2M (6/30/26) = +29.0% in six months**, against **$914.4M of equity**. A **NEW Q1-26 risk factor** confirms it is deliberate: *"increased our exposure to residential mortgage loans through portfolio acquisitions and expect to further expand this exposure… in 2026."* AMTB calls the paper jumbo/nonconforming and discloses **no government-insured balance anywhere.**

**The gap: AMTB does not break out government-insured within a book growing 29% per half-year — so FHA/VA-adjacent paper entering it would not be separately visible.** De minimis today. **Trigger: the Q2-2026 10-Q (~August) loan-composition note — does a government-insured line item appear?** This is "not disclosed ≠ zero," not evidence of exposure.

## Two things NOT to carry forward

- **The post-VASP counterparty-growth inference is REFUTED at magnitude.** The mechanism is real (post-termination, bought-out VA loans stay with the servicer instead of being sold to VA), but BKU is the one place it was measurable — and its book went the **other way: −19% across the four quarters spanning VASP termination.**
- **The VA advocacy figures survive as counts but NOT as causal evidence.** ~80,000 VA loans were **already seriously delinquent seven weeks BEFORE VASP terminated** — the gap-attributable increment is ~10,000, not 90,000. Cite instead: **MBA NDS Q1-2026 — VA foreclosure rate at its highest since Q2 2017, VA DQ ~225bp above conventional.**

## Confidence note: this axis was REPLICATED

Axis A was accidentally run **twice** — two agents, separate sessions, no shared state. **They converged on every load-bearing point:** same verdict, same BKU exception, same ~58%-of-equity, same zero-ACL insight, zero counterparty hits in both directions in both runs. They also each closed the other's gap — one reached the FFIEC Call Report the other couldn't; the other found the AMTB disclosure gap the first missed. **The finding that changes your action rests on two independent primary-sourced derivations, not one.**

## Named limits — all point the same direction

- **Four of five heaviest ex-VASP nonbanks (Village Capital, The Money Source, Planet Home, CrossCountry) have NO EDGAR presence** → their warehouse-lender lists are **unverifiable, not absent.**
- **Ginnie Mae's issuer directory was unreachable** (site rebuilt as a JS app ~7/14) → issuer negatives rest on filings + SSB/AMTB's explicit Fannie/Freddie-only language.
- **BKU's 6/30/26 gov-insured figure (~$0.87B) is chart-derived**; exact number lands with the **Q2 10-Q, early August**.
- **No discrete nonbank-servicer stress event as of 7/24.** **Two traps excluded:** a loanDepot "downgrade" circulating this month is a **Goldman equity Sell / price-target cut — NOT a credit action**; a "Fitch downgrades Finance of America" headline is **October 2023 recirculating** (FOA's 2026 posture is the opposite).

**Every one of these could only ADD exposure, never subtract it.**

## Also useful to your Q2 work

FHA publishes a **QUARTERLY Report to Congress** (12 U.S.C. 1708(a)(5)) carrying a statutorily-compelled predicted-vs-actual table that nobody in the fleet was citing: **claim counts −57.4% vs forecast while net loss on claims runs +7.75pp (+30.9%) above it** — volume deferred, severity deteriorating. **The Q2 edition is ~3 months OVERDUE.** Richer than the annual capital-ratio headline, and a nearer catalyst.
