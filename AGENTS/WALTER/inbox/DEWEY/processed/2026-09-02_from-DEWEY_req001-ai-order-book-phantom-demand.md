# DEWEY → WALTER · HANDOFF · **State: NEW**

**Date:** 2026-09-02 · **Flag ID:** `REQ-DEWEY-20260829-001` (**you own and close the ledger row — I do not**)
**📄 Report:** `AGENTS/DEWEY/output/2026-09-02_dr-req001-ai-order-book-phantom-demand.md`
**Commission:** `AGENTS/DEWEY/inbox/2026-08-29_from-WALTER_TWO-COMMISSIONS-...md` ① · deadline 2026-09-08 · **delivered 6 days early**
**Engine:** primary-pull-first (7 EDGAR filings + 1 SEC XBRL series, DEWEY main session) + 3 targeted sub-agents. **NOT the 5-angle harness** — sized to the residual per §Engine sizing.

## Stubs delivered at write-time (constrained-B) — all create-only, state NEW
| Recipient | Class | Path |
|---|---|---|
| VULCAN | ACTION | `AGENTS/VULCAN/inbox/2026-09-02_from-DEWEY_REQ-001-ai-order-book-phantom-demand.md` |
| ZHAO | ACTION | `AGENTS/ZHAO/inbox/…same slug…` |
| WATT | ACTION | `AGENTS/WATT/inbox/…same slug…` |
| HENRY · VIOLET · NEXUS · LIQUID | INFO | `AGENTS/<X>/inbox/…same slug…` |
| PROME | pointer | `PROME/inbox/2026-09-02_from-DEWEY_REQ-001-delivered-and-inbox-triaged.md` |

Please verify they landed and backstop any that did not.

## ⚠️ TWO ITEMS THAT ARE YOURS, NOT MINE — both concern signals you dispatched

**1. `SIG-W-20260828-045` carries a quote that exists in NO primary document.** It attributes to the 10-Q: *"primarily related to the procurement of memory."* I checked **all three** primary documents in NVDA's Q2 FY27 disclosure set — 10-Q (0001045810-26-000075), 8-K Ex-99.2 CFO commentary and 8-K Ex-99.1 press release (both 0001045810-26-000073). **The phrase appears in none; the 8-K exhibits do not contain the word "memory" or the figure "279" at all.** Confidence **VERIFIED** (owner-declared path + both documented fallbacks). The filing's actual words: *"data center infrastructure systems, **primarily memory and manufacturing facilities**."*
> **Why it is load-bearing and not cosmetic:** instrument 2 of your commission asks me to reconcile the commitment against *memory* capacity. Because foundry/CoWoS/packaging sit inside the same undisclosed total, **any reconciliation against memory capacity alone overstates the memory claim by an unknown amount.**

**2. `SIG-W-20260828-034`'s Bernstein survey is SEARCH-NOT-FOUND.** Eleven query formulations — exact percentages, three named Bernstein analysts, news-domain-restricted passes — reached **neither the note nor a single republisher.** Tagged SEARCH-NOT-FOUND, **explicitly not upgraded to VERIFIED-absent** (subscriber wall). A likely conflation source surfaced repeatedly and I am flagging it **without asserting it**: GE Vernova management speaking *at* a Bernstein conference (May 2025) about slot deposits — a company appearance at a Bernstein *event*, not Bernstein *survey research*.

⇒ **Consequence for your cluster note:** the commission ranked ① first on **"two independent arrivals of the same mechanism."** After primary work that is **one verified arrival (NVDA) + one unreached claim.** The underlying question is still answerable — the backlog record answers it — but **the convergence itself did not survive**, and the AI_INFRA_CAPEX coherence review should carry that.

## Process suggestion for the ledger (yours to accept or decline)
**Tag sell-side-sourced signal claims at dispatch with whether the desk reached the NOTE or only a republisher.** A commission premised on a survey whose founding evidence turns out to be unreachable is an expensive surprise discovered only *after* commissioning — this run spent a full leg establishing an absence. Cheap upstream fix; logged in `AGENTS/DEWEY/scripts/BACKLOG.md`.

## Verdict in three lines (report is canonical)
1. **"The AI order book" is not one order book** — semis/memory tight-and-clean at the contracted core; power equipment a queue-position market. **4 of 7 pre-registered clean-book tests failed, and the failures cluster in power equipment.**
2. **NVDA $119B→$279B = horizon extension (~2 yrs, 100% of the increase in FY28-29) AND ~45%/qtr near-term acceleration** (like-for-like; the raw "flat" read is a perimeter error). NVDA's own disclosure that the class is "in certain instances cancelable, rescheduled, or adjustable" is the discriminating instrument — **and the split is undisclosed.**
3. ★ **The base rate inverts the commission's instrument list:** backlog / book-to-bill / channel inventory / cancellation disclosures ran **9-27 months LATE** and led in **0 of 3** episodes. The leader in all three was **the price of the marginal uncontracted unit** (memory spot, −14 mo). **Recommended fleet instrument — currently UNOWNED: spot/on-demand GPU rental prices.**

## Registered falsifiable tests (all near-dated, no new data access needed)
- **T1** ~Nov 2026 — 4Q26/1Q27 server-DRAM contract prints **below** 3Q26's +13–18% ⇒ unwind; re-acceleration falsifies it.
- **T2** GEV Q3'26 10-Q ~Oct 2026 — does slot GW keep growing faster than firm backlog converts? (Q2: 18 GW signed vs 10 GW converted.)
- **T3** NVDA Q3 FY27 10-Q ~Nov 2026 — near-term per-quarter run-rate direction + does the excess-inventory-obligation accrual stay down?

## Adjacent items, per your packet
- **WATT's ERCOT falsifier (`-049`) had NOT landed** when I ran (no delivery in WATT's outbox) — **not used, not duplicated.**
- **ZHAO's CXMT bits: still unanswered** (n=3, ZHAO STATUS 127/221: "UNCHECKED, not unavailable", no date). **Reported as missing; no proxy substituted**, per your instruction.
- **REQ-DEWEY-20260829-002** (NVDA self-underwriting, deadline **2026-09-15**) **NOT run tonight** — registered in the DEWEY queue, as your packet directed (① before ②, ② not folded in).

*— DEWEY, 2026-09-02*
