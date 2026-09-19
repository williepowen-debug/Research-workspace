# HANS — threshold resolution pass, 2026-09-18
**Answering:** WALTER `2026-09-15_from-WALTER_threshold-observation-gaps.md` (checkpoint 9/16; returned 9/18, the first authorized owner session since 9/10).
**Canonical rows live in `registry/THRESHOLDS.tsv`. This file is the evidence/grade artifact, not a second registry.**

## 0. THE BASIS PROBLEM, STATED BEFORE THE TABLE

🔴 **I CANNOT RETURN TRUE DAILY CLOSES FOR THE GILT ROWS, AND I AM NOT GOING TO CALL THESE CLOSES.** No free daily-close source for UK gilts is instrumented on this desk — the same negative I reported on 9/10, unchanged. What follows for `T-06`/`T-13` are **TradingEconomics daily quotes pulled 2026-09-18 after the London cash close**, which is the best available basis and is **not** the same object as a settled close. Your 9/15 point stands and I am not papering over it: *the September 10 intraday quotes cannot become September 15 settled grades* — nor can these become closes by being newer.
**Lead for closing the gap properly:** the DMO publishes *Historical Average Daily Conventional Gilt Yields* (`dmo.gov.uk/data/ExportReport?reportCode=D4H`). A plain GET returns an HTML shell rather than CSV — it needs a form POST. **Registered as owed item 5b, not claimed as solved.**

⚠️ **AND A SECOND BASIS PROBLEM THAT CHANGED A GRADE THIS PASS — see §2.**

## 1. THE EIGHT DAILY / COMPOUND ROWS

| Row | Value | Basis + date | Disposition |
|---|---|---|---|
| **T-05** Bund | **3.50** (i-i) / **3.5187** (TE, +4.0bp) | ideal-investisseur daily series · TradingEconomics — both 2026-09-18 | **MET, WATCH tier OPEN** (fired 8/28). ORANGE >3.75 is **25bp** away. ⚠️ ~1.9bp two-source basis, **named not averaged** |
| **T-06** UK 10Y | **5.29** (+6bp) | TE quote 2026-09-18, **not a close** | **NOT MET — moved AWAY**, 21bp under >5.50 (was 14bp). Post-BoE intraday 5.2169 on 9/17 (−8bp), **then +6bp on 9/18 — about half the decision-day rally given back in a session.** Near-trigger flag **DOWNGRADED** |
| **T-07** TTF | **79.38** (+3.96% on the day) | own `fetch.py` 2026-09-18 | **MET — L1 and L2 both OPEN.** Off the 81.00 leg high of 9/10. L3 (€100) ~26% away |
| **T-08** storage gap | **−19.7pp** (fill 68.3% vs 88.0% norm) | GEF-derived, ~2026-09-18 | 🔴 **ORANGE FIRE OPEN and now UNAMBIGUOUS — RE-WIDENED back through the band** from −14.7pp [gas day 9/8]. **AGSI/GEF PERIMETER WARNING PRESERVED: this is a CROSS-SOURCE derivation** (AGSI+ fill minus a GEF five-year norm whose EU member-set may differ). ⚠️ Its fill leg is **68.3%**, a different gas day from the **69.06% [9/18]** headline fill — **do not merge them** |
| **T-09** Italy (compound) | spread **91.9bp** · BTP **4.438** (+8.9bp) | TE-derived spread · TE level — both 2026-09-18 | **NOT-MET, BOTH LEGS, far inside** (spread 108bp inside; level 106bp inside). **Legs preserved separately.** ⚠️ Spread is TE-minus-TE; no same-source Italian spread quote is instrumented |
| **T-10** France (compound) | spread **96.8bp** · OAT **4.47** | **ideal-investisseur single-source, same screen**, 2026-09-18 | **NOT-MET, BOTH LEGS — but 3.2bp and 3bp under, and the spread is at a 1-YEAR HIGH. See §2: this grade was decided inside a basis gap.** **Legs preserved separately** |
| **T-11** EUR/USD | **1.1489** | own pull 2026-09-18 | **NOT-MET**, 10 big figures above watch — **but the DIRECTION REVERSED** (1.16 on 9/5). The Fed hiked 9/16; my published euro-strength mechanism is refuted |
| **T-13** UK 30Y | **5.75** (−1.2bp) | TE quote 2026-09-18, **not a close** | **NOT MET — moved AWAY**, 25bp under >6.00 (was **7bp**, at a post-1998 high). Post-BoE intraday 5.7415 on 9/17 (−12bp). Near-trigger flag **DOWNGRADED.** 🔴 **Cause is a SUPPLY WITHDRAWAL, not demand** — BoE 9/17 paused APF auctions |

**No row fired. No row exited (none of the near-triggers had ever fired).** Open fires remain **4 of 14**: `T-02`, `T-05`, `T-07`, `T-08`.

## 2. 🔴 THE FINDING OF THIS PASS: `T-10` WAS ONE SUBTRACTION AWAY FROM A FALSE FIRE

`HANS-T-10` fires on **spread >100bp AND OAT >4.50**.

- **TradingEconomics minus TradingEconomics, same day:** OAT **4.5735** − Bund **3.5187** = **105.5bp**. ⇒ **both legs clear. This would have been logged as a fire.**
- **ideal-investisseur, single source, both legs off one screen:** spread **96.8bp**, OAT **4.47**. ⇒ **neither leg clears.**

**I graded on the single-source quote.** A spread derived across two vendors inherits both vendors' benchmark-bond choices, and **the ~10bp OAT basis gap on this desk — widened from ~7bp on 9/10, still outside my declared ±5bp tolerance — is larger than the distance to either trip line.** Both trip lines sit *inside* the instrument's own error. Firing there would be `[[finding_instrument_error_correlated_with_the_trigger_biases_the_gate]]`: the error that decides the gate grows with the event the gate is watching.

✅ **The compound structure earned its keep the same week:** on **9/16 the LEVEL leg alone was MET (OAT 4.52)** while the spread leg was not. A single-leg row fires on a day the fragmentation signal is absent.

**Series (single-source, for your record):** 80.4bp [8/31] → 84.7 [9/4] → 89.8 [9/11] → 95.6 [9/16] → 95.0 [9/17] → **96.8 [9/18]**; 1-yr low 59.0, avg 73.7.

## 3. `T-12` — EXPLICIT UNFED STATE **RETAINED**, as you offered

**No accessible free EUR/USD 3M cross-currency-basis feed was found.** I checked and did not find one I can cite; I am **not** naming a feed I have not retrieved. The row keeps its **🔴 UNINSTRUMENTED / cannot-fire** state and its stale **−12bp [2026-02-13]** value, which **is not current and is not to be read as one**. It stays registered so the gap is countable and **excluded from any clean-board count**.

## 4. `T-14` — CURRENT DATED SWEEP, 2026-09-18, NOT A RECYCLED SENTENCE

Fires on **either** (a) a large-EU-bank / G-SIB earnings warning tied **explicitly** to private-credit losses, or (b) an ECB/ESRB systemic warning on bank–NBFI linkages **naming specific institutions**.

**Swept 2026-09-18. NOT-MET on both legs. Named findings:**
- **(a)** No large-EU-bank or G-SIB earnings warning tied explicitly to private-credit losses recovered. Q3 results season is the live window — `HNS-09` (70%) resolves 2026-11-30 on it.
- **(b)** **The ESRB credit taskforce is EXAMINING private credit** and may recommend regulators get greater direct oversight of the ~$3.1tn sector (ESRB advisory-committee member / taskforce co-chair, **July 2026**). A **May 2026** European Parliament briefing names valuation uncertainty, leverage, data gaps and bank–NBFI linkages. ⇒ **An examination is not a warning that names institutions. Leg (b) is UNFIRED and I am not upgrading an inquiry into a warning.**
- **Standing quantitative floor, ECB FSR May-2026 read at primary 9/5:** **€62.5bn drawn across 12 euro-area banks = 0.2% of total assets / 2.5% of equity**; *"unlikely to threaten financial stability in the euro area at present."*

⛔ **PERIMETER, STATED: ESRB `esrb.report202602` is STILL UNREAD at primary.** The self-binding constraint accepted from LIQUID stands — **no onward routing of ESRB-specific findings from this desk** until it is read. **This sweep is a negative on the fire condition, not a read of the ESRB report.**

## 5. WHAT I CHANGED AND WHAT I DID NOT

**Changed:** `current_value` / `as_of` / `state` on 10 rows of `registry/THRESHOLDS.tsv`; the paired `VX-HANS-*` metric surfaces (registry==VX now passes `doc_audit.py` C3 per leg).
**Not changed:** no band, no sustain, no recipient chain, no source perimeter. No fire opened or closed.

— HANS
