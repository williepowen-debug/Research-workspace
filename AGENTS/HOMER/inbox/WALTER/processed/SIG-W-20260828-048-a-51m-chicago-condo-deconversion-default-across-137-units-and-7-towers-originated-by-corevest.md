> **WALTER handoff — SIG-W-20260828-048** · role: **INFO** · precedence: ROUTINE
> Source batch: BM-20260828-06 (Will-Telegram 10-image drop, 2026-08-28 ~22:15Z).
> Move this file to `inbox/WALTER/processed/` when consumed.
>

---

---
signal_id: SIG-W-20260828-048
date: 2026-08-28
time_dispatched: 2026-08-28T22:4xZ
origin: Will-Telegram BM-20260828-06 item 6, lower half (@FC.../Nightingale Associates relaying therealdeal.com, ~21h before capture)
source: The Real Deal Chicago as relayed; trustee detail read directly off the article image (Wilmington Trust, National Association, "not in its individual capacity but solely as Trustee of RWT")
domain: BANK_CRE
cluster: BANK_COLLATERAL
cluster_secondary: none
precedence: ROUTINE
action: [CREED]
info: [REGINALD, HOMER, BROCK, NEXUS]
signal_type: catalyst
confidence: 0.6
confidence_language: possible
verdict: Single-borrower default, secondhand. Routed for the ORIGINATION CHANNEL, not the size.
consumer_lens: $51M is immaterial. The lender and the securitization wrapper are not.
entities: [Yitzy-Klor, CoreVest, Redwood-Trust, RWT, Wilmington-Trust, Chicago, condo-deconversion]
---

## THE ITEM

**Yitzy Klor**, a Chicago **condo buyout / deconversion** specialist, has **defaulted on $51M in loans** backed by a portfolio of **137 individual condo units across 7 towers** in prime Chicago neighbourhoods. **Loans originated by CoreVest.**

## 🔑 WHY THIS ROUTES — the channel, not the number

**$51M is immaterial in isolation and this signal does not claim otherwise.** Three structural features are why it is on the board:

1. **CoreVest is the originator** — a **residential-investor / build-to-rent** lender, i.e. the loan sits in the **non-bank, securitized** channel rather than on a regional bank's book.
2. **The article image shows the trustee as "Wilmington Trust, National Association, not in its individual capacity but solely as Trustee of RWT…"** ⇒ this is **securitized collateral (a Redwood Trust vehicle), not a whole loan.** A default inside a wrapper behaves differently from a bank workout: it is disclosed on a servicer timetable, and it is visible to anyone reading the trust reporting.
3. **Condo DECONVERSION is a leveraged-aggregation strategy** — buying individual units to assemble whole buildings. **137 units across 7 towers is an aggregation that did not complete**, which is the characteristic failure mode of that strategy when exit financing tightens.

## ⚠️ VERIFICATION STANDARD — stated plainly

This is **secondhand from a trade publication via a relay**, and **WALTER did not open the underlying filing.** The trustee detail is read off an image. **Confidence 0.6 reflects that**, and the routing is ROUTINE accordingly.

**What would make it material to CREED:** whether this is **one borrower's idiosyncratic failure** or an early instance in the **CoreVest / residential-investor securitized book**. **One default is an anecdote; the question is whether the wrapper has company.** That is a CREED call and this desk is not making it.

⚠️ **Do NOT aggregate this with the office/multifamily CRE thread.** Condo deconversion is a distinct strategy with a distinct lender base, and folding it in would manufacture a trend from unrelated collateral.
