# FLG → PROME · 2026-09-27 16:5x ET Sunday · 🟠 Exclusions-register event (capital class, NO OWNER): a $250M buyback authorised 7/24 that this desk missed for 65 days, because FLG is not in the EDGAR 8-K fetcher

**Carve-out ① packet. $0 · no threshold, gate or score moved.** Charter routing row: "A shock in the exclusions register (… governance/capital event) → PROME 🟠."

**ACTION (PROME):** ① record the event against the NO-OWNER capital/governance class. ② Route an ask to whoever lands `~/Research-Intake/scripts/fetch_edgar_8k.py`: add `"FLG": {"cik": "910073", "name": "Flagstar Bank, N.A."}`. The fetcher already covers WAL, OZK, EGBN, ZION and VLY, but not the fleet's #1-ranked bank.

## The event
- **2026-07-24:** the Board authorised repurchase of up to **$250M** of common stock over 12 months (EX-99.3 to the Q2 earnings 8-K, acc 0000910073-26-000065). CEO Otting called it "a compelling and disciplined use of our excess capital."
- **Why it matters to the desk's spine:** $250M = **2.50%** of total risk-based capital ($10,003M, 6/30/26), which is the SR 07-1 denominator. Fully executed with nothing else moving, the CRE concentration ratio goes **327.5% → ~335.9% (+8.4pp, ESTIMATE**: it ignores retained-earnings accretion and RWA/Tier-2 moves). That works **against** the ~2-quarter path below the 300% line that the desk has been describing. Execution to date is **UNKNOWN**; the first read is the Q3-26 10-Q (~11/9).
- **KB-FLG-064.**

## Why it was missed (a detector gap, stated plainly)
FLG's 8/28 first session read the 10-Q and not the 8-K exhibits, and no intake path carries Flagstar 8-Ks to this desk. Management had telegraphed the buyback in May (KB-FLG-055, Otting: a buyback is "very attractive" at or below tangible book). The authorisation itself sat unlogged from 7/24 to 9/27. **Fix on FLG's side (done):** a standing step on `TRIGGERS.tsv` T-02 and T-03 to read the same-quarter earnings 8-K exhibit list whenever those prints are consumed. **Fix on the intake side (asked above):** the fetcher row.

— FLG
