# FERT — Status

**Domain:** Fertilizer supply/price/policy → food-CPI transmission → CF Industries positioning
**Class:** Market domain — EVENT-DRIVEN SPECIALIST (wakes on named triggers; no standing daily desk)
**Last real data refresh:** 2026-09-02 (DTN Progressive Farmer weekly retail, **data wk Aug 24–28**, article 9/2 — three prints read in one wake, clearing a 3-week backlog)
**Session wall clock:** 2026-09-02 22:02 Wednesday (boot.py)
**Situation Tier:** 🟡 MONITORING — nitrogen still bleeding at retail; **phosphate stopped rising** (four flat prints)

> **Rebuild note.** The FROZEN 2026-03-20 STATUS is archived at `archive/STATUS_2026-03-20_FROZEN.md` — historical only. Every price cell below is benchmark + unit + date + source. **"Urea" alone is not a price.** Grading record: `PROME/research/2026-08-16_fert-revival-assessment.md`.

---

## Price Panel — benchmark-split (never one row called "urea")

| Benchmark (full name) | Unit | Level | As-of | Source authority |
|---|---|---|---|---|
| DTN retail urea, US national avg | **$/ton** | **$655** (−5% MoM, +4% YoY) | data wk **Aug 24–28 2026** | MIRROR — DTN Progressive Farmer 9/2/26 |
| NOLA granular urea barge FOB | **$/st** | **$385–410** | data **8/7/26** | MIRROR — Advanced Turf US Fert Mkt Summary 8/10/26 PDF |
| Urea FOB US Gulf futures (CBOT **JC**), Aug-26 | **$/st** | **$389.50** (−4.75) | **8/17/26** | PRIMARY — CME via Barchart |
| Urea FOB US Gulf futures (CBOT JC), Sep-26 | $/st | $386.00 (−4.00) | 8/17/26 | PRIMARY — CME via Barchart |
| Urea FOB Egypt futures (CBOT **JF**), Sep-26 | **$/mt** | **$442.50** (−2.50) | ~8/15/26 | PRIMARY — CME via Barchart |
| India CFR, **lowest BID** (RCF tender, opened 8/11) | **$/mt** | **$390.25** east / **$393.65** west (Ameropa) | bids **8/11/26**, reported 8/14 | MIRROR — Rural Voice 8/14/26 |
| World Bank Pink Sheet urea, E. Europe prill spot FOB | **$/mt** | **$400.0** (Jul) ← from **$856.9** (Apr) | monthly, **Jul 2026** | PRIMARY — WB Pink Sheet, pub 8/4/26 |
| DTN retail **DAP**, US national avg | **$/ton** | **$918** (+7% YoY) | data wk **Aug 24–28 2026** | MIRROR — DTN 9/2/26 |
| DTN retail **MAP**, US national avg | **$/ton** | **$959** (+5% YoY) | data wk **Aug 24–28 2026** | MIRROR — DTN 9/2/26 |
| DTN retail **potash**, US national avg *(triage-depth row)* | **$/ton** | **$493** (+2% YoY) | data wk **Aug 24–28 2026** | MIRROR — DTN 9/2/26 |
| DTN retail anhydrous / UAN28 / UAN32 | $/ton | $923 / $428 / $458 | data wk Aug 24–28 2026 | MIRROR — DTN 9/2/26 |
| NOLA **DAP** barge FOB | $/st | $795–798 | 8/7/26 | MIRROR — Advanced Turf 8/10/26 |
| NOLA **MAP** barge FOB | $/st | $775–785 | 8/7/26 | MIRROR — Advanced Turf 8/10/26 |
| Pink Sheet **DAP**, spot FOB US Gulf | $/mt | **$781.3** (Jul) | Jul 2026 | PRIMARY — WB Pink Sheet 8/4/26 |
| Pink Sheet **phosphate rock** | $/mt | **$170.0** (Jul) ← $152.5 flat May-25→May-26 | Jul 2026 | PRIMARY — WB Pink Sheet 8/4/26 |

⚠️ **Cross-benchmark spreads are real, not error.** DTN retail urea $655/ton vs NOLA barge ~$390/st vs Pink Sheet FOB $400/mt — the same nutrient, three instruments, ~$265 apart. The March desk's registered gate died on exactly this confusion. **DTN retail lags international by weeks** — international series are the leading edge for any transmission timing.

⏳ **Oldest cell on this panel is the NOLA $/st block (data 8/7, art 8/10)** — the Advanced Turf weekly PDF (T5) was NOT pulled this session. Treat the NOLA rows as a 3.5-week-old vintage, not a current read.

---

## Registered Gates — graded this wake (both watch-only; no capital path)

**GATE-FERT-G5 — NOT FIRED (3 of 3 prints).** Letter: *DTN retail **DAP OR MAP > $1,000/ton***; instrument = DTN Progressive Farmer weekly retail $/ton. ⛔ Never Pink Sheet $/mt, never NOLA $/st.

| Print (article) | Data week | DAP $/ton | MAP $/ton | Binding leg | Gap to $1,000 | Grade |
|---|---|---|---|---|---|---|
| 8/12/26 *(registration baseline)* | Aug 3–7 | $917 | $959 | MAP | $41 · **+4.28%** | — |
| **8/19/26** | Aug 10–14 | $917 | **$960** | MAP | $40 · **+4.17%** | **NOT FIRED** |
| **8/26/26** | Aug 17–21 | $916 | $959 | MAP | $41 · **+4.28%** | **NOT FIRED** |
| **9/2/26** | Aug 24–28 | **$918** | $959 | MAP | $41 · **+4.28%** | **NOT FIRED** |

🔑 **The level barely moved; the APPROACH RATE collapsed — and that is the finding.** MAP is net **$0** and DAP net **+$1** across three weeks. G5 was base-rated at registration on a **~+0.5% MoM** cost-push; **realised ≈ 0.0% MoM**. Implied time-to-fire went from **~8.5 months** at the assumed rate to **undefined**. A gate can sit at an unchanged distance and still have become far less likely to fire — distance-to-line and rate-of-approach are two different claims, and only the first is visible in the row.

**GATE-FERT-G3 — NOT FIRED (both legs).** Letter: *China 2026 urea export quota revised **DOWN**, OR a guidance floor reimposed **ABOVE prevailing intl FOB***.
- **Leg 1 — quota:** 3.3 Mt for 2026, **UNCHANGED**; no revision found in either direction (SEARCH-NOT-FOUND on a down-revision at MOFCOM/NDRC relays, CF commentary, Profercy).
- **Leg 2 — floor:** $660/t prilled · $670/t granular FOB lifted early June, **replaced** by a lower *unpublished* guidance price days later. Prevailing intl urea **~$415–445/mt** late Aug; Chinese offers into India **<$400/mt CFR** both coasts [Profercy 8/13]. **Behaviour is dispositive:** a floor above market stops exports, and exports are not stopped.
- ⛔ **"Quota expanded to 5–5.5 Mt" is a contamination** — that is China's *historical export range* (2025 actual 4.9 Mt), not a 2026 quota revision.

---

## Live Vectors

| # | Vector | Live read (dated) | State | Score /5 | Independence | Next re-read |
|---|---|---|---|---|---|---|
| 1 | **China export regime** | Quota **3.3 Mt for 2026**; ~**2.0–2.5 Mt** allocated Jun–Aug; CF projects **4–6 Mt** actual 2026. Price floor **$660/$670/t FOB set end-May, LIFTED early June** (was above market, exports stalled), replaced by an unpublished lower guidance price. **Observed behaviour, not the stated floor, is the binding read:** Chinese offers into India **<$400/t CFR** [Profercy 8/13, ATS 8/10] | 🟢→🟡 supply RETURNED | 2 | High (policy + 3 independent market reads) | **every wake** (T10) |
| 2 | **Phosphate tight leg** | DAP **$918** / MAP **$959** retail [wk Aug 24–28], **+7%/+5% YoY and FLAT, not rising** — 4 prints: MAP 959/960/959/959, DAP 917/917/916/918. Pink Sheet DAP $781.3/mt = 93rd pct of 2016–2026 [Jul]. Rock $170.0/mt [Jul] | 🟠 ELEVATED *(level)* — but **momentum gone** | **3** ↓ | Med — the 4 benchmarks no longer agree on *direction*; rock/sulfur say up, retail says flat | T4 weekly |
| 3 | Hormuz transit | Effectively closed; ~1 transit 8/9 vs ~73/day normal [Lloyd's List 8/12]. Alternative routing (Red Sea/Suez) in use where feasible [ATS 8/10] | 🔴 but **priced** | 3 | Med (BRENT/HAWK own the theater) | via OSPREY/FALCON |
| 4 | Nitrogen price level | Round-tripped internationally (Pink Sheet **$856.9/mt Apr → $400.0 Jul, −53%**) and **still bleeding at retail**: DTN urea $678 → **$655**/ton, UAN28 $446 → **$428**, anhydrous $964 → **$923** over 3 wks. Lagged pass-through, not new info | 🟢 NORMALISED | 1 | High | T4/T5 weekly |
| 5 | India import demand | RCF 1.7 Mt tender bids opened 8/11; **lowest bids $390.25/$393.65 CFR** — vs $935/$959 awarded April. Demand intact, **price collapsed** | 🟡 | 2 | High | T1 |
| 6 | Food-CPI transmission | July food-at-home **−0.07% m/m / +2.7% y/y** [BLS via FRED CUSR0000SAF11]. ERS forecasts FAH 2.7% (2026) / 2.9% (2027) — **fertilizer not a cited driver** | 🟢 NOT FIRING | 1 | High | T2/T3 |
| 7 | Qatar LNG → fertilizer capacity | **12.8 mtpa** (Trains 4 & 6, Ras Laffan) = **~17%** of Qatar export capacity; missile strikes 3/18–19/26; 3–5 yr repair CONFIRMED. **No primary links this damage to ammonia/urea output** — inference deleted, not carried | 🟡 | 2 | Low (single event, unlinked to N) | on QAFCO/Mesaieed disclosure |
| 8 | European production economics | Gas ~$16.00/MMBtu → theoretical ammonia ~$667/mt FOB, **above prevailing urea FOB = economically shut**. Physical closure count **PAYWALLED**, unresolved since March | 🟡 UNRESOLVED | 2 | Low (proxy only) | on BRENT gas signal |

**Convergence: 16/40** (was 17/40 — vector 2 cut 4→3 on the direction disagreement). No vector at 5.

---

## What Changed This Session (2026-09-02 — first wake since 8/17; 16 days dark)

1. **The phosphate cost-push is not reaching retail.** Four consecutive DTN prints with MAP net $0 and DAP net +$1. The upstream story (rock $152.5 → $170.0/mt, Tampa sulfur +$50/lt to $705/lt, Mosaic idles) is **unchanged and now unconfirmed at the retail end** — and it was always **single-source** (one trade distributor, T12), a caveat I wrote at registration and did not discharge this session. **The thing I was most confident about three weeks ago is the thing that stopped happening.**
2. **A candidate mechanism, deliberately not promoted to an explanation.** Morocco's OCP returned to the US market after the June CVD suspension, first **54,000 mt** landed in New Orleans [DTN 8/19]. My own KB-FERT-014 logged that suspension as a *policy* fact; it is now producing *physical import supply* into exactly the market that stopped rising. Direction and timing both fit — but **one shipment against a national retail average is not the tonnage arithmetic**, and I have not done it. Recorded as a hypothesis with a named instrument.
3. **Relative tightness widened on the wrong leg.** MAP/urea went 1.415 → **1.464** — entirely because urea fell $678 → $655. The numerator never moved. "Phosphate tightness increased" is true of the ratio and **false of the phosphate level**; quoting the ratio alone inverts the cause.
4. **Two contamination traps caught, one of them against my own file.** (a) "China quota expanded to 5–5.5 Mt" is China's *historical export range*, not a revision. (b) A partial snippet read as the China guidance floor being *removed outright*, which would have falsified my STATUS wording — the fuller passage says lifted-then-**replaced** days later. **My existing claim was correct and was nearly overwritten by a shorter quote of the same source.**
5. **YoY compressed fast while the level sat still** — DAP +12%→+11%→+8%→+7%, MAP +8%→+7%→+6%→+5%. That is the **year-ago base rising**, not a level decline. Do not read the YoY column as a price move.
6. **Structural, not price-bearing:** CHS + OCP North America preparing the first US phosphate plant since 1984 (Louisiana), claimed to cut import dependency >48% [DTN 9/2]. Multi-year build; it cannot move a weekly retail print. Companies' own figure, relayed.

---

## Exit Rules / Kill Rail

**Kill rail re-derived: 2026-08-17.** Full protocol + bidirectional flip test: `workbook/EXIT_PROTOCOL.md`.

- **Nitrogen channel — already DEAD** (channel-kill, not thesis-kill). Killed by China's quota resumption, not by demand. Migration path: phosphate leg + CF single-name fundamentals.
- **Phosphate channel — LIVE, but weakening.** Dies if Pink Sheet phosphate rock prints back ≤$157/mt for 2 consecutive monthly editions **AND** DTN retail MAP prints below $900/ton — i.e. the July cost-push reverses at both the root and the retail end. **Neither leg is met** (rock $170.0/mt Jul; MAP $959). ⚠️ **But the kill rail as written cannot see what actually happened this month:** it tests for *reversal*, and what occurred is a *stall*. Four flat prints move the channel toward irrelevance without moving either kill leg. **Do not read "kill not triggered" as "thesis intact"** — the honest state is *level held, momentum lost*. Next Pink Sheet (T11, 9/4) is the root-end read that decides whether this is a pause or a top.
- **Transmission question — OPEN, not a carried prediction.** Dies if BLS food-at-home m/m stays <+0.4% through the Nov-2026 print (T3/T6) with no upward ERS revision citing inputs.
- **Timing vs mechanism:** the March *timing* claim is graded MISS; the mechanism is **not** refuted (`finding_market_ignoring_is_not_market_refuting`). It is un-instrumented, and re-opening it requires a fresh input shock, not a re-read of the old one.

---

## Named Blind Spots (exclusions register — I do not cover these)

| Excluded | Owner | On sighting |
|---|---|---|
| **Potash supply shock** | ⚠️ **NO LONGER UNOWNED — FERT owns it at TRIAGE DEPTH ONLY** (Will-ruled 2026-08-18; this row was stale from 8/18 until corrected 9/2) | Unchanged in practice: KB row + PROME flag, **no deep-dive, no comparison, no trend adjective**. *(Live: DTN retail potash **$493/ton** [wk Aug 24–28], +2% YoY; NOLA barge $335–345/st [8/7]; Pink Sheet KCl $396.5/mt [Jul] — quiet.)* ⛔ **Correction carried from PROME 8/22:** "potash is EXCLUDED from §338" is **NOT primary-supported** — the operative text carves out only §232 articles and WTO civil aircraft. Potash may merely be absent from the annex's positive list: same practical effect, **different mechanism — assert neither**. |
| Clean-ammonia / ammonia-as-fuel demand | NO OWNER | KB row + PROME flag |
| Qatar QAFCO/Mesaieed physical damage | OSPREY/FALCON | Consume their signal; I own the capacity consequence only |

---

## Open Instrument Gaps (honest classification)

| Item | Class | Note |
|---|---|---|
| RCF tender **award** (vs bids) | **PUBLIC-AND-UNFETCHED** | Offers valid to 8/24; award due days. T1 re-dated 8/25 |
| European 2026 plant-closure count | **PAYWALLED** | Argus/ICIS/CRU. Unresolved since March; **not load-bearing** for transmission |
| "$800M EBITDA per $50/ton urea" (CF) | **GENUINELY UNAVAILABLE** | Not disclosed, not reproducible. **Do not carry** |
| March "$516 baseline" | **GENUINELY UNAVAILABLE** | No benchmark/date reconciles. **RETIRED this session** |
| Qatar ammonia/urea capacity impact | **PUBLIC-AND-UNFETCHED** | QAFCO/Mesaieed disclosures not pulled |
| China guidance price, post-June level | **PUBLIC-AND-UNFETCHED** | Re-checked 9/2, still unfetched. Scope now precise: the floor was lifted early June and **replaced** days later — it is the *replacement level* that is missing, not the whole regime. Behaviour (offers <$400/mt CFR) shows it is not binding, so this gap is **not load-bearing** for G3 |
| RCF Aug-2026 tender **award** price | **PUBLIC-AND-UNFETCHED → PAYWALLED** | 2nd check 9/2, still unpublished free. Shipments must complete by 9/24, which *implies* an award exists. Argus/Profercy hold it |
| Phosphate cost-push second source | **UNRESOLVED — single-source since 8/17** | T12's own precondition, never discharged. Now material: retail went flat, so the rock/sulfur driver is unconfirmed at the consuming end |
| BLS Oct-2025 food-at-home print | **MISSING AT SOURCE** | FRED row exists but is **blank** — a real gap, not a zero. Any "N consecutive months" CPI gate must state its missing-print rule |

---

## BOTTOM LINE

Both registered gates graded **NOT FIRED** this wake: G5 on three DTN prints (MAP $959–960, DAP $916–918 against the $1,000/ton line), G3 on both legs (quota 3.3 Mt unchanged, no floor above a market where Chinese offers land under $400/mt CFR). The single most important read is a **correction to my own last session**: phosphate retail has been **flat for four consecutive prints** — MAP net $0, DAP net +$1 — so the cost-push I called the live tight leg on 8/17 is **not reaching the retail end**, and G5's approach rate fell from the ~+0.5%/mo it was base-rated on to roughly zero, which changes the gate's odds without changing its distance. The phosphate *level* still holds at the 93rd percentile and the kill rail is nowhere near tripping, but the rail tests for *reversal* and what happened is a *stall*, so "not killed" is not "intact" — and the likeliest cause, Moroccan OCP tonnage arriving post-CVD-suspension, is a hypothesis I have named but not measured. I wake next on the Pink Sheet (9/4 — the root-end read that calls pause-or-top), the Advanced Turf NOLA PDF and sulfur inputs (9/7), the DTN weekly (9/9), and the August CPI food-at-home print (9/11).
