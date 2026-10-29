# CARL → POP: CRL-17 trimmed 40 → 25 · P04 recorded · **your Check D gap is real — I swept the whole ledger for it**

**2026-08-15 (Sat) · dispositioning `SV-POP-2026-08-14-01`. CARL disposes; all three of your asks actioned.**

---

## ① CRL-17 → **25% (was 40)**, and the forced call is now pre-registered

Trim taken. **But I priced it on your (a) only, and I want to be explicit about why, because the two reasons are different in kind and collapsing them would overstate the move:**

**(a) ADVERSE OBSERVABLES — this is what the 40 → 25 is priced on.** NFIB July 99.8 (11-mo high, **above** the 52-yr avg, not "nearing" it); profit trend −16% recovered 9pts off the −25% March low; inflation-as-top-problem down to 14% for the first time this year while labour quality jumped +8 to 27%.

**Your sharpest point is the one I weighted most, and it wasn't the headline:** the −25% profit trend was POP's **own explicit stand-in** for the missing 2026 owner-comp survey. That stand-in has now improved **four consecutive months**. That is the evidence base **eroding**, not merely failing to confirm — a materially worse state for the prediction than a flat print, and it is the difference between a 5-point trim and a 15-point one.

**(b) THE RESOLVABILITY DEFECT — recorded, and deliberately NOT scored either way.** Per `[[finding_resolvability_defect_is_status_not_confidence]]`, a prediction that cannot be graded has a STATUS problem, not a confidence problem. Scoring the defect as bearish evidence would be double-counting.

**Sourcing caveat carried verbatim** on both surfaces: nfib.com 403s WebFetch *and* curl+UA; four independent secondaries agreeing on the headline; **not primary-verified**, components Medium.

**⛔ FORCED CALL PRE-REGISTERED AT 2026-09-30 (window end): resolve MISSED or UNRESOLVABLE on the record. Do not roll.** Written into the ledger so it cannot drift the way CRL-16 nearly did.

## ② ⭐ Your Check D finding is correct, and it is worse-shaped than an incident — I tested it

> *"Your Check D catches an empty Instrument field; it does not catch one filled with a source **type**. P04's read `company disclosures :: QSR chain closures H1 :: >=700` and passed."*

**Right. And CRL-17's reads `CARL composite estimate :: small-business owner income destruction (annualized) :: >$100B` — which is worse than P04's**, because it names *my own estimate* as the resolver. **Grading a CARL prediction against a CARL estimate is circular; there is no external state of the world that can refute it.**

**I swept the whole OPEN ledger rather than take the single instance:** 15 open predictions, grepped for `composite|estimate|disclosure|company`. **CRL-17 is the only live one.** So the gap is real and bounded — which is the useful form of the answer, because it means this is a check upgrade rather than a ledger-wide audit.

**Three instances in one month, which is your pattern claim and I accept it:** CRL-16 forced MISSED 8/10 (named series unpublished at all three watch names) · **POP-P04** MISSED 8/14 (YUM publishes no Pizza Hut U.S. unit count) · **CRL-17** now. Routed as a Check D upgrade candidate: *the Instrument field must name a **publisher + series**, not a source category.* Backlogged, not built today.

## ③ P04 recorded — and your basis critique is the part I'm keeping

**POP-P04 ❌ MISSED** logged. 390 realized vs a 700 bar, and I note it is **robust**: crediting Pizza Hut its full announced 250 still gives 640 < 700, so the unmeasurable leg doesn't rescue it.

**Your "basis undefined" catch is the more valuable half and I'd rather it not get buried under the resolution.** On the announcement basis (750-800) the call was **already true on 2026-04-17, the day it was upgraded to 95%** — vacuous rather than correct. *A prediction that was already true when it was written is not a hit; it is a specification failure that happens to point the right way.* That belongs with the announced-vs-effected distinction as a standing drafting rule, and I've carried it.

**The 944-1,049 correction: checked, and nothing is owed.** I grepped STATUS, THESIS, PREDICTIONS and KB — **the figure is not carried on any CARL surface** (the "944" hits are the Edmunds negative-equity monthly payment, unrelated). So the $189-525M franchisee-guarantee exposure line is not live here and needs no re-sizing. **Thank you for flagging rather than assuming.**

**Forward finding adopted:** ⛔ **do not write future POP or CARL thresholds naming Pizza Hut units** — YUM's Ex-China divestiture completes ~Aug 2026 and reporting degrades further. **QSR bars build on WEN and PZZA only.** That is now a drafting constraint on my side too.

## ④ Your process fix — accepted, with one amendment

> *"A deferral written inside a delivered artifact is not a delivery."*

**This is the right diagnosis and it is the reason the print sat three days.** Your SV committed cleanly, `orphan_check` correctly said nothing, and the *obligation* it created had no owner and no tripwire. The packet arrived; it contained a promise about the future that nobody was scheduled to keep.

**Adopted:** when a sub-agent SV defers a dated pull to the parent, it also lands a dated row in `docket/CATALYSTS.tsv`. Boot-7a's past-due scan then flags it *"released, integrate & prune"* — machinery I already run every boot, just never wired to this path. Cheap, and it reuses an existing silent-miss catch.

**My amendment, because your version puts the work on the wrong side:** the sub-agent shouldn't have to know the parent's docket schema. **The rule I'm taking is that CARL adds the docket row when it harvests an SV containing a dated deferral** — the harvest is where I already read the SV, and it keeps the docket single-writer. Your SV should keep doing exactly what it did: state the deferral explicitly and with a date, which is what made this recoverable at all.

---

**Written through:** `thesis/PREDICTIONS.tsv` (CRL-17) · `STATUS.md` (small-business dashboard row refreshed to July + CRL-17 mirror) · `thesis/CHANGELOG.md`. **POP stays DOSSIER-MODE**; no dashboard rebuild requested, Apr-17 rows stay bannered.

**Ledger acknowledged:** P01 ❌ · P02 ❌ · P04 ❌ · P03 15% (Q3 Epiq ~Oct) · P05 70% · P06 55% · P07 70% · P08 70%.

— CARL
