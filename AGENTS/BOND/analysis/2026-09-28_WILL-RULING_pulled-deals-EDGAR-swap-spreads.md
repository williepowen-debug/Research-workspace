# Will's ruling — pulled-deal search, scorecard wording, EDGAR, sign-ups, swap spreads (2026-09-28)

**Recorded:** 2026-09-28 19:27 ET by BOND. **Authority:** Will's own text, pasted into BOND's live session (`bond-d6`) at ~19:2x ET, 9/28. **It adopts CATO's recommendation** `AGENTS/CATO/runs/2026-09-28_1706_active-agent-next-steps.md` § "September 28 — BOND pulled-deal source-check direction" (`648f81720`) and, for swap spreads, CATO's rates review `…_1744_bond-rates-context-review.md` line 92 ("a small reproducible sample with aligned times/conventions and comparison evidence before wiring another monitor").

## Verbatim (as pasted)
> Approve proposing the narrow pulled-deal search to WALTER through the existing intake process.
>
> Distinguish confirmed cancellations/postponements from downsizing and wider pricing. Record the issuer, instrument, market, event date, source and confirmation status; deduplicate repeated stories and relaunches.
>
> Correct the scorecard language: incomplete coverage prevents a zero-withdrawal conclusion, but verified in-scope withdrawals can support the existing trigger. Cite its governing definition; if the count/window is unspecified, bring a prospective definition before automated grading.
>
> Defer the SEC monitor. Before reconsidering it, demonstrate on a small manual sample that launch, pricing, closing and withdrawal records can be matched reliably. Missing filings must remain unresolved.
>
> No SIFMA or FINRA signup for this particular gap, and no paid tracker yet. Any purchase proposal should show cost, coverage, delay and sample withdrawal records unavailable through current sources.
>
> Keep the full daily swap-spread build deferred until the previously proposed small validation establishes comparable timestamps, conventions and credible benchmark agreement.
>
> Scheduled observations and the October 1 refresh / October 2 WQ-317 delivery remain first.

⚠️ **Supersedes** Will's 19:1x instruction "build swap-spread monitor next session": the full build is now DEFERRED behind a small validation.

## BOND disposition, item by item
| # | Item | Done this session | Where |
|---|---|---|---|
| 1 | Propose the narrow pulled-deal search to WALTER via the existing intake process | ✅ packet (query proposal + event spec); WALTER tests and PROME lands, as with `treasury-moves` | `AGENTS/WALTER/inbox/2026-09-28_from-BOND_pulled-deal-search-proposal.md` |
| 2 | Event classes and fields; dedupe | ✅ in that packet's spec | same |
| 3 | Scorecard wording corrected; governing definition cited; prospective definition if count/window unspecified | ✅ wording fixed on STATUS row 4, `KB-BND-358`, the source-check note and `CREDIT_PRIMARY_MARKET.md`. **Governing definition = `monitors/CREDIT_PRIMARY_MARKET.md` § Core Thresholds, "Pulled deals: isolated / multiple lower-quality / blue-chip or clustered HY pulls", plus STATUS matrix row 4's "a pulled-deal cluster". NO count, NO window ⇒ prospective definition below, FOR WILL, not registered; no automated grading until ruled.** | this file § Proposal |
| 4 | SEC monitor deferred; manual-sample precondition; missing filings stay unresolved | ✅ recorded; the "item 2.03 = closed" resolver claim is withdrawn (CATO: 2.03 = any direct financial obligation, not a bond settlement) | source-check note, `KB-BND-358` |
| 5 | No SIFMA/FINRA sign-up, no paid tracker; purchase-proposal criteria | ✅ recorded | source-check note |
| 6 | Full swap-spread build deferred behind a small validation (timestamps, conventions, benchmark agreement) | ✅ SCRATCH NEXT SESSION reordered; the note's "validated on 6 dates" corrected (6 tested, 5 produced rows) | `SCRATCH.md`, swap note |
| 7 | Scheduled observations + 10/1 refresh + 10/2 WQ-317 first | ✅ SCRATCH order | `SCRATCH.md` |

## Proposal — prospective "pulled-deal cluster" definition (FOR WILL; NOT registered, NOT graded)
**Why a proposal and not a rule:** the current wording cannot be graded mechanically. Picking a bar now, with 9/28's anecdotes in view, would be choosing it after seeing the cases. ⚠️ **No base rate exists**: there is no free historical census of withdrawals, so any count below is **unvalidated**, and this desk's rule is that a threshold owes a base rate before its first evaluation.

- **Event (counts):** a CONFIRMED withdrawal, postponement or cancellation of a **USD high-yield corporate BOND** offering (144A or registered) after launch. **Confirmed** = an issuer statement or filing, or ≥2 independent outlets naming the issuer and instrument. **Recorded but NOT counted:** downsizing; pricing wider than initial talk; loans; private-credit vehicles (e.g. CFOs → BROCK); non-USD deals (→ HANS/LIQUID).
- **Dedupe:** one event per issuer per offering; syndicated repeats collapse to the earliest event date; a relaunch keeps the original withdrawal on record, tagged "relaunched <date>".
- **Candidate bars (pick, amend, or keep hand-grading):** *Yellow* ("multiple lower-quality") = ≥2 confirmed events from issuers rated B- or lower within 10 business days · *Red* ("blue-chip or clustered") = ≥3 confirmed events of any rating within 10 business days, OR ≥1 from an issuer rated BB or better.
- **Always:** no hits = incomplete search, **never zero, never "market open"**. Only confirmed in-scope events count toward the trigger.
- **Alternative (BOND's recommendation until a base rate exists):** keep the qualitative wording and **hand-grade with a written rationale per event**, logging every confirmed event so a base rate accumulates. Revisit numeric bars after ~6 months of logged events.
