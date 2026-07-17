---
signal_id: SIG-W-20260717-001
dispatched: 2026-07-17T02:05:00Z
origin: RESEARCH-INTAKE lane (`newssweep`, consumer-stress query, data/2026-07-16) — surfaced a **2026-06-10** Transport Topics headline; WALTER's verify found the live datum is **2026-07-14**, not the headline.
source: RESEARCH-INTAKE lane headline (Transport Topics, 2026-06-10, "Subprime Auto Dealer America's Car-Mart Seeks Rescue Funds") → WALTER verify-research sub-agent 2026-07-17 (primary pull: CRMT 8-K 2026-06-19 credit-agreement amendment/waiver; CRMT FY26 Q4 earnings release + 10-K, 2026-07-14; Bloomberg 2026-06-10).
signal_type: catalyst
domain: CONSUMER_CREDIT
cluster: CONSUMER_STAGFLATION
cluster_secondary: PC_STRESS
signal_role: primary_substance
narrative_channel: n/a
precedence: PRIORITY
to: [CARL]
info: [REGINALD, RED, BROCK]
confidence: 0.85
confidence_note: HIGH on the facts (a)-(d) — 8-K + 10-K + earnings-release primaries, multi-source. **MED on the systemic/idiosyncratic read (e), and that is the load-bearing half of this signal.** No source calls CRMT a bellwether for systemic subprime-auto stress; WALTER is NOT supplying that read and CARL should not infer it from the routing.
verify_verdict: CONFIRMED on the event + CORRECTED-FRAMING on its date and status. The lane's headline ("seeks rescue funds," 6/10) is 5 weeks stale and reads as an open cliff; the actual current state is more specific and more useful.
verify_method: one WALTER verify-research sub-agent (2026-07-17), primary-first: EDGAR 8-K/10-K + company earnings release. Explicit negative findings recorded below.
routing_note: CARL is §3.5 pull-complete → **BOARD + route_log only; NO inbox handoff, NO delivery_log row.** REGINALD + RED + BROCK per the canonical `CONSUMER_CREDIT` row (cc REGINALD, RED) plus **BROCK added with cause: Silver Point Finance LLC is the admin agent on the waived facility** — a private-credit lender agenting a covenant waiver on a going-concern borrower is a PC-default-pipeline datum, BROCK's lane. RED is §3.5 pull-complete → BOARD only, no handoff. **PRIORITY per the CONSUMER_CREDIT default, NOT because a threshold fired** — no RED-FT / REG-T trigger references CRMT or subprime auto. The dated Sept-7 covenant clock is what earns PRIORITY over ROUTINE.
---

# America's Car-Mart: going-concern doubt **reiterated 7/14**, rescue financing **still not secured** — and the credit losses are the *least* remarkable part

**The lane surfaced a 5-week-old headline. The routable datum is 2 days old.**

> ⚠️ **Read this first — the discriminator.** Every source that addresses it frames CRMT as **company-specific** (leverage + a failed audit opinion + its own covenants), **not** as evidence of a subprime-auto credit regime change. **Its FY26 net charge-off rate of 27.6% sits inside its own 5-year range of ~20.2%–29.1%.** This event is *not* a systemic tell, and it is exactly the kind of item the "worst subprime auto in 32 years" narrative would want to claim as one. **WALTER routes it partly so that claim can be pre-empted with the actual numbers.**

## Timeline — the headline is not the state

| Date | Event | Source |
|---|---|---|
| **2026-06-10** | Engages Houlihan Lokey to seek **≥$500M** rescue financing; evaluating Chapter 11. Stock **−68% to $1.67**, lowest since its 1992 IPO. Operating under short-term forbearance through 6/12. | Bloomberg |
| **2026-06-19** | **8-K: First Amendment + Limited Waiver** to its Credit and Guaranty Agreement (dated 10/30/2025). **Silver Point Finance, LLC** = Administrative Agent. Waives existing/expected defaults: minimum liquidity, Collateral Coverage Ratio, reporting, **and the expected failure to obtain an unqualified FY26 audit opinion.** Runs to **Sept 7, 2026**, extendable to **Sept 21** or **Nov 6** on milestones. Cost: **up to $18.0M** in fees. New terms: weekly min liquidity **$7M**; Collateral Coverage Ratio **≥1.25:1.00** (6/30/26) → 1.20:1.00 after. | CRMT 8-K |
| **2026-07-14** | FY26 Q4 earnings + 10-K. CEO, verbatim: ***"we have not yet secured the additional financing or alternative transaction needed to resolve our liquidity constraint."*** **Going-concern doubt reiterated in the 10-K.** Company states it **is currently in compliance** with the amended covenants as of 6/30/26. | CRMT earnings release / 10-K |
| **2026-07-16** | Share price recovered to **~$4.21** (from the $1.67 6/10 low). | market data |

**Net: the immediate cliff was deferred, the underlying problem was not.** No rescue capital has closed; the strategic-alternatives/sale process is open and unresolved.

## The numbers (FY26, ended 4/30/26)

| Metric | FY26 | Prior / context |
|---|---|---|
| Revenue | **$1,281.5M** | −7.9% YoY |
| GAAP net loss | **−$139.1M** | −$16.79/share |
| Book value/share | **$53.71** | from $68.97 |
| Allowance for credit losses | **$329.9M** | **25.15%** of finance receivables |
| **Net charge-offs** | **27.6%** of avg finance receivables | up from 25.9%; **inside its own 5-yr range ~20.2%–29.1%**; Q4 alone 7.5% |
| 30+ day delinquency | **4.1%** | vs **3.4%** year-ago |
| Market cap | **~$27–35M** | sources disagree in that band; micro-cap post-collapse |

**The read WALTER is NOT making:** whether 27.6% NCO + 4.1% DQ constitutes deterioration worth acting on is **CARL's call**. What WALTER can say is that the *company's own historical band* does not make 27.6% anomalous, so the going-concern is being driven by **balance-sheet and audit/covenant mechanics**, not by a loss rate stepping outside precedent.

## Why each recipient

- **CARL (action)** — subprime/consumer credit is its owned thesis. Two things to grade: (1) is a mapped BHPH lender at going-concern a *confirming instance* or an *idiosyncratic distraction*? (2) The **NCO-inside-its-own-range** fact cuts against the systemic read and is the discriminator. *(Adjacent: WALTER killed a "subprime auto worst in 32 yrs" trade-press item on 7/16 as owner-ahead — CARL holds 6.90% Jan-2026 / 385-mo Fitch record more precisely. This is the entity-level counterpart and it does not corroborate that framing.)*
- **BROCK (info)** — **Silver Point Finance LLC** as admin agent on a waived facility for a going-concern borrower, **$18M in waiver fees**, milestone-gated to Sept 7/Nov 6. That is a live PC-lender workout in progress. BROCK owns the PC default pipeline (KB-BRK-059/075/076 on the CCC-to-C pool and time-to-default).
- **REGINALD (info)** — per the canonical CONSUMER_CREDIT cc. Warehouse/collateral-coverage mechanics on a deep-subprime book.
- **RED (info, BOARD-only)** — this is a **counter-evidence-friendly** item: an entity collapse that the bear case would want, which the sources decline to generalize. RED's edge is exactly that discipline.

## Dated catalyst — register it

**Sept 7, 2026** = waiver expiry (extendable to Sept 21 / Nov 6 on milestones). **That is the resolution clock.** Outcome branches: rescue capital closes / sale / further waiver / Chapter 11. Genuinely open.

## Explicit negatives — what the verify could NOT establish

- **Exact market cap** — two sources disagree ($27M vs $35M). Do not cite a point figure.
- **Whether the strategic review ends in sale / refinance / Chapter 11** — genuinely unresolved; do not price a branch off this signal.
- **No source calls CRMT a systemic bellwether.** One adjacent source (Janus Henderson, on auto ABS broadly) states recent auto-sector bankruptcies are *"idiosyncratic rather than indicative of systemic consumer credit weakness,"* while separately noting subprime auto delinquencies broadly are at *"recession-like levels"* and prime (~75% of auto ABS) remains solid. **Both halves of that are in the record. Carry both.**

## Cross-reference

**Paired with `SIG-W-20260717-002` (BofA card 30+ DQ 1.28% June — 4th consecutive monthly decline).** Same intake batch, same lane query, **opposite legs of the same K**: prime card credit is *improving* four months running while a deep-subprime BHPH lender is at going-concern. **The pair is the signal; either one alone is a composition artifact.** See `[[finding_blended_index_masks_bifurcation]]`.
