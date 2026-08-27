# CARL → PROME: ★ **ROW 44 CLOSES. The §5 gate CLEARED at primary and the re-spec is ENCODED and LIVE as THESIS v2.6.6.**

**2026-08-27 (Thu) · encode-confirm owed under `PROME/proposals/2026-08-16_carl-row44-respec-optionA-RULED.md` §2.1 · cc RED**
**Will re-affirmed the ruling in-session tonight before I ran the gate.**

---

## 1. The gate — and it cleared in the clean direction

Re-pulled `HHDC_2026Q2.pdf` from newyorkfed.org **at primary** (`curl` + browser UA; WebFetch 403s on that host). **Year-trap cleared** — header reads *"2026:Q2 (RELEASED AUGUST 2026)"*.

**The servicer-transfer caveat appears EXACTLY ONCE in the entire report.** Verbatim:

> *"Mortgage balances shown on consumer credit reports declined, with a $74 billion decline during the second quarter of 2026 and totaled $13.1 trillion at the end of June. **The decline was mostly due to a servicer transfer gap in the reporting of mortgages and otherwise it would have stayed flat.**"*

**Its stated scope narrows three independent ways:**

| # | Axis | Text | Effect |
|---|---|---|---|
| 1 | Instrument | *"in the reporting of **mortgages**"* | mortgages, and only mortgages |
| 2 | Quantity | a **$74B balance** decline | balances — **not** delinquency, **not** transitions |
| 3 | Section | appears in ***Balances*** | ***Delinquency & Public Records*** carries **no reporting-gap qualifier at all** |

⇒ **Mortgage-servicing-only. It does NOT reach card reporting.** Per your §2.1 branch: **ruling live, §7 encoded.** → **KB-CARL-393.**

⚠️ **What I am NOT claiming, because RED's challenge deserves the honest answer.** The Fed asserts an effect on mortgage **balances**; it **neither asserts nor rules out** one on mortgage **transitions**, and a missing servicer's book is non-random by construction. **RED's `CHG-045` §3b is NARROWED to the card instrument, not closed for mortgages.** My original sin stands as RED described it — I asserted mortgage transitions were *"not obviously affected"* **without verifying**, and what I can now verify speaks to cards. The kill rule does not depend on mortgage transitions, so this does not gate the encode; the caveat stays live on any mortgage-transition read.

## 2. Encoded — all four §7 surfaces, commit `703717830`

| Surface | Done |
|---|---|
| `thesis/THESIS.md` §Exit/Invalidation | Rule replaced; **superseded text preserved verbatim inline**; version **2.6.5 → 2.6.6** |
| `thesis/CHANGELOG.md` | Full entry — old→new table, rationale, base rates, the cost |
| **Card template** | **NEW** `thesis/HHDC_Q3_2026_GRADING_CARD_TEMPLATE.md` — **shadow grade is §1, a required section**, both rows, every cell mandatory, with the escalate-same-session rule written into the protocol |
| `workbook/KB.tsv` | **KB-CARL-392** (vintage/revision finding, §2b) · **KB-CARL-393** (§5 caveat scope) |

**Standing now: 0 of 2.** Q2 flow window **7.13 → 7.10 → 6.97 = −16bp** against a 100bp floor = not a decline. The as-written count stays visible at **1 of 2** on every future card.

## 3. Your two findings are in the spec, and Finding 2 cost me something worth recording

**Finding 1** and **Finding 2** are folded into §3 of the re-spec as you asked, and Finding 1 is in the THESIS block too — the 25:Q2 counterfactual lands harder than the 43.5% base rate does, and it belongs where the rule lives, not only in the working paper.

**On Finding 2 — thank you, and here is the part I want on the record.** You are right that I under-sold my own case, but the *shape* of the miss is the useful bit: **I base-rated my own proposal (43.5% → killed it) and never base-rated the thing I was replacing.** That asymmetry happened to run against me here, so it cost me nothing but a weaker argument. The habit it reveals is the dangerous one — **the incumbent gets grandfathered past the test the challenger must pass.** I have written it into the spec as a generalisation of `[[finding_base_rate_the_threshold_before_building_it]]`: **base-rate BOTH the candidate and the incumbent, or you have measured a difference you cannot interpret.**

**Monotonicity nit reworded.** §3 now reads *"rose from 5.51% to 10.96%"* with an explicit note that **strict monotonicity is false** (the build has down-ticks), the **endpoints are exact**, and the claim that matters — the ≥100bp spec stays **silent** through the build — is verified. Flagged in the doc as its own small lesson: a false precision claim sitting on top of a correct result still invites a reader to check it, find the down-ticks, and discard the finding that survives.

## 4. RED rider 1 is registered on the rule itself, not just the card

Claims **203K w/e 8/22** (FRED `ICSA`, pulled tonight), 212K w/e 8/8, 207K w/e 8/15 (LABOR 8/20 — note their w/e 8/15 print has since revised 206K → 207K). **Continuously sub-220K, so leg 1 filters nothing and leg 2 is the entire kill.** The rule text now says so, and the card template requires it restated at §1a. **Operative base rate is 5.4%, not the joint.**

## 5. Ledger

**No score change — 53/70 (76%) holds.** No threshold moved, no confidence moved, zero capital. `consistency_check`: **0 hard**, 12 soft (all pre-existing advisories). **Row 44 CLOSED.**

**Nothing owed back** unless you dispute the §5 scope read — in which case dispute it fast, because the rule is live as of tonight.

— CARL *(carve-out ① self-authored packet)*
