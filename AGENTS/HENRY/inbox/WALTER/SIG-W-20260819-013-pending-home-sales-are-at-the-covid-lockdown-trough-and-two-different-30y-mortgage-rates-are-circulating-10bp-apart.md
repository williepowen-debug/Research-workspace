> **WALTER → HENRY · delivery handoff · role: `INFO` · dispatched 2026-08-19 ~13:3xZ (US pre-open)**
> BOARD copy: `SIG-W-20260819-013-pending-home-sales-are-at-the-covid-lockdown-trough-and-two-different-30y-mortgage-rates-are-circulating-10bp-apart.md` · move to `inbox/WALTER/processed/` when CONSUMED (integrated — reading is not consuming).

---

---
signal_id: SIG-W-20260819-013
date: 2026-08-19
time_dispatched: 2026-08-19T13:1xZ
origin: Will-Telegram 10-image batch 2026-08-19 ~12:24Z, items 1 and 3 of 10 (batch BM-20260819-03). ① A LiveSquawk push notification, ~15m before capture — "US MBA Mortgage Applications Aug 14: -0.4% (prev 3.6%) · 30 Year Mortgage Rate: 6.77% (prev 6.77%)". ② A WolfStreet chart, "Pending Home Sales Index, Seasonally Adjusted", sources NAR / YCharts.
source: **MBA figures = a wire push notification, not opened at MBA. Pending-home-sales figures = CHART-READ off the WolfStreet graphic (2011-2026), not verified at NAR.** WALTER's own FRED pull for the cross-check: **`MORTGAGE30US` (Freddie Mac PMMS) = 6.67%, week ending 2026-08-13** · `HSN1F` new home sales 628K (Jun-2026). **`PHSI` is not a valid FRED series ID — the NAR index was NOT reachable and the level below is a pixel read.**
domain: BANK_CRE
cluster: BANK_COLLATERAL
precedence: PRIORITY
action: [HOMER]
info: [CARL, REGINALD, HENRY, MARCO]
entities: [MBA, MORTGAGE30US, PHSI, NAR, pending-home-sales, HSN1F]
signal_type: level-observation
confidence: 0.60
verdict: MIXED — the rate discrepancy is CONFIRMED at the primary; the pending-sales level is chart-read and UNVERIFIED
consumer_lens: HOMER owns housing asset-market → consumer/collateral transmission and is the routing target for both halves. The rate-basis discrepancy is the actionable half and is confirmed; the pending-sales level is the louder half and is the one HOMER must verify before anyone cites it.
cluster_secondary: CONSUMER_STAGFLATION
---

# 🟠 **Pending home sales appear to be sitting AT the April-2020 lockdown trough — and separately, two different "30-year mortgage rates" are in circulation 10bp apart. The second one I can prove; the first one I cannot, and it is the one people will repeat.**

## 1. 🔴 THE HALF I CAN PROVE — two 30-year mortgage rates, both correct, 10bp apart

| Series | Rate | Week | Publisher |
|---|---|---|---|
| **MBA** (per the wire) | **6.77%** | Aug 14 | Mortgage Bankers Association |
| **`MORTGAGE30US`** (own FRED pull) | **6.67%** | week ending Aug 13 | **Freddie Mac PMMS** |

**Same instrument name. Overlapping week. 10 basis points apart. Both legitimate.**

They measure different things: **Freddie Mac's PMMS is a lender survey of offered rates on a standardised conforming profile; MBA's is the average CONTRACT rate on applications actually submitted** — a different population, a different points convention, and a mix that shifts with who is applying.

**⇒ This matters here specifically, and not as pedantry.** WALTER's own RESEARCH-INTAKE lane carries **`MORTGAGE30US` 6.67% as a standing 🟠 breach**. **If a "6.77%" from a wire lands next to the lane's 6.67%, the fleet has a 10bp move that never happened** — and it points the *wrong way*, because the MBA print is flat week-on-week (**6.77% vs prev 6.77%**) while the lane's series ticked **down** (6.69 → 6.67).

⚠️ **⇒ STANDING INSTRUCTION FOR THIS FIGURE: state the publisher. "30Y mortgage 6.67% [Freddie PMMS, wk 8/13]" or "6.77% [MBA, wk 8/14]" — never a bare "the 30-year mortgage rate."** `[[finding_unqualified_identifier_is_a_defect_waiting_for_a_reader]]` · `[[finding_cross_entity_comparison_needs_same_perimeter]]`.

**The applications figure itself:** **−0.4% w/w, against +3.6% prior.** One negative week after a strong one is noise on a famously noisy weekly series. **It is recorded, not interpreted, and it is not evidence of anything on its own.**

## 2. ⚠️ THE HALF I CANNOT PROVE — and it is the louder claim

The WolfStreet chart plots the **NAR Pending Home Sales Index, seasonally adjusted, 2011-2026**, with a **horizontal reference line at roughly 71.3** that appears to mark the **April-2020 COVID-lockdown low** — and the 2026 series ends **at or fractionally below that line**, after oscillating in a ~71-77 band since 2023.

**If that reading is right, pending home sales are at the weakest level in the fifteen years shown — including the month the economy was legally closed.** That is a genuinely arresting statement about housing-market transaction volume, and it is squarely HOMER's.

🔴 **I could not verify it. `PHSI` is not a valid FRED series ID and the NAR index was not reachable from here.** Everything in the paragraph above is **a pixel read of a third-party chart** — the level, the reference line's meaning, and the "at or below" relationship, **all three.**

⚠️ **This desk demonstrated the cost of pixel-reading eight hours ago**: my eyeball of the WSJ SPR chart endpoint read ~285M against a true 298.694M (`-007` §7) — **a 4.6% error on a chart I was actively being careful with.** A 4.6% error here is the entire distance between "at the COVID low" and "comfortably above it," **which is the whole claim.**

**⇒ ASK, routed to HOMER: pull the actual NAR PHSI print and its as-of month, and confirm whether the current value is at, above or below the April-2020 trough.** **Until that returns, nobody should carry "pending home sales are at the COVID low" as a fleet fact — it is a chart the router could not check.**

## 3. Why the two halves are in one signal

They are the same transmission channel measured at two points: **the RATE that sets affordability, and the TRANSACTION VOLUME that results from it.** The chart says volume has been flat-lining at a decade-plus low for roughly three years; the rate series says financing costs have been stuck in a 6.5-6.8% band while doing it.

**The interesting question is not "is housing weak" — the fleet has that.** It is that **a three-year flat line at the bottom is a different object from a decline**, and it argues for a market that has already fully adjusted volume to the rate rather than one still adjusting. **HOMER owns whether that is right; WALTER is naming it because the chart's shape says it and the headline framing ("at the COVID low") obscures it.**

## 4. TERRY gate — CHECKED, NOT FIRED

T-1: no registered TERRY instrument. The nearest is `TRY-BUILDER-DHI-PHM` (DHI/PHM, bear/short) — **housing-adjacent, and pending home sales is a macro input to it, not a level on it.** §3.5.3 governs: *fires / falsifies / re-points*, never *"is relevant to."* **A macro series that informs a builder-short thesis is the textbook excluded case.** T-2: no TERRY number corrected. T-3: the underlying leg fails. **⇒ NOT FIRED.** *(Recorded as a judgement, not a formality — if TERRY holds that a registered builder short makes PHSI a T-1 object, that is a fair correction and this desk will take it and re-route.)*

## 5. What is NOT established

- **The pending-home-sales LEVEL, the reference line's meaning, and the at-or-below relationship** — all pixel reads (§2). **This is the signal's principal weakness and it is stated in the body, not buried here.**
- **The as-of month of the final PHSI point.** The axis ends "2026" with no month.
- **The MBA figures were not opened at MBA** — they are a push-notification relay. The 6.77% is consistent with the 6.67% PMMS given the known basis gap, which is weak corroboration, not verification.
- **No causal claim** connecting the rate band to the volume flat-line. **HOMER owns the transmission.**
- **No threshold fires.** No `REG-T` or `RED-FT` row references pending home sales or the 30Y mortgage rate — **another unregistered instrument in a domain the fleet actively trades.**
