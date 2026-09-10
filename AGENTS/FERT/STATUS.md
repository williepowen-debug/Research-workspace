# FERT — Status

**Domain:** Fertilizer supply/price/policy → food-CPI transmission → CF Industries positioning
**Class:** Market domain — EVENT-DRIVEN SPECIALIST (wakes on named triggers; no standing daily desk)
**Last real data refresh:** 2026-09-09 (**DTN Progressive Farmer weekly retail article, published 9/9/2026 1:06 PM CDT, data week Aug 31 – Sep 4 2026** — T4 consumed, all eight products read at the publisher)
**Session wall clock:** 2026-09-09 21:05 Wednesday (boot.py)
**Situation Tier:** 🟡 MONITORING — **phosphate stalled at both ends for a fifth week**; nitrogen retail bleed has STOPPED and partly reversed (anhydrous +$15 w/w)

> **Rebuild note.** The FROZEN 2026-03-20 STATUS is archived at `archive/STATUS_2026-03-20_FROZEN.md` — historical only. Every price cell below is benchmark + unit + date + source. **"Urea" alone is not a price.** Grading record: `PROME/research/2026-08-16_fert-revival-assessment.md`.

---

## Price Panel — benchmark-split (never one row called "urea")

| Benchmark (full name) | Unit | Level | As-of | Source authority |
|---|---|---|---|---|
| DTN retail urea, US national avg | **$/ton** | **$655** (**$0 w/w**, +4% YoY) | data wk **Aug 31–Sep 4 2026** | MIRROR — DTN Progressive Farmer 9/9/26 |
| NOLA granular urea barge FOB | **$/st** | **$385–410** ⛔ **FROZEN 8/7 VINTAGE — 33 days; instrument unreachable, see below** | data **8/7/26** | MIRROR — Advanced Turf US Fert Mkt Summary 8/10/26 PDF |
| Urea FOB US Gulf futures (CBOT **JC**), Aug-26 | **$/st** | **$389.50** (−4.75) | **8/17/26** | PRIMARY — CME via Barchart |
| Urea FOB US Gulf futures (CBOT JC), Sep-26 | $/st | $386.00 (−4.00) | 8/17/26 | PRIMARY — CME via Barchart |
| Urea FOB Egypt futures (CBOT **JF**), Sep-26 | **$/mt** | **$442.50** (−2.50) | ~8/15/26 | PRIMARY — CME via Barchart |
| India CFR, **lowest BID** (RCF tender, opened 8/11) | **$/mt** | **$390.25** east / **$393.65** west (Ameropa) | bids **8/11/26**, reported 8/14 | MIRROR — Rural Voice 8/14/26 |
| World Bank Pink Sheet urea, E. Europe prill spot FOB | **$/mt** | **$390.0** (Aug) ← $400.0 (Jul) ← **$856.9** (Apr) | monthly, **Aug 2026** | PRIMARY — WB Pink Sheet, pub 9/2/26 |
| DTN retail **DAP**, US national avg | **$/ton** | **$919** (**+$1 w/w**, +7% YoY) | data wk **Aug 31–Sep 4 2026** | MIRROR — DTN 9/9/26 |
| DTN retail **MAP**, US national avg | **$/ton** | **$959** (**$0 w/w**, +5% YoY) | data wk **Aug 31–Sep 4 2026** | MIRROR — DTN 9/9/26 |
| DTN retail **potash**, US national avg *(triage-depth row)* | **$/ton** | **$493** (+1% YoY) | data wk **Aug 31–Sep 4 2026** | MIRROR — DTN 9/9/26 |
| DTN retail **anhydrous** | $/ton | **$938** (**+$15 w/w, +1.63%**, +22% YoY) | data wk Aug 31–Sep 4 2026 | MIRROR — DTN 9/9/26 |
| DTN retail UAN28 / UAN32 / 10-34-0 | $/ton | **$423** (−$5) / **$455** (−$3) / **$717** (+$2) | data wk Aug 31–Sep 4 2026 | MIRROR — DTN 9/9/26 |
| NOLA **DAP** barge FOB | $/st | $795–798 ⛔ frozen 8/7 vintage | 8/7/26 | MIRROR — Advanced Turf 8/10/26 |
| NOLA **MAP** barge FOB | $/st | $775–785 ⛔ frozen 8/7 vintage | 8/7/26 | MIRROR — Advanced Turf 8/10/26 |
| Pink Sheet **DAP**, spot FOB US Gulf | $/mt | **$793.5** (Aug) ← $781.3 (Jul), **+1.6%** | Aug 2026 | PRIMARY — WB Pink Sheet 9/2/26 |
| Pink Sheet **TSP**, spot FOB US Gulf | $/mt | **$704.4** (Aug) ← $719.5 (Jul), **−2.1%** | Aug 2026 | PRIMARY — WB Pink Sheet 9/2/26 |
| Pink Sheet **phosphate rock** | $/mt | **$170.0** (Aug) = **$170.0** (Jul) ← $156.9 (Jun) ← $152.5 flat 25 mo | Aug 2026 | PRIMARY — WB Pink Sheet 9/2/26 |
| Pink Sheet **potassium chloride** *(triage-depth row)* | $/mt | **$386.9** (Aug) | Aug 2026 | PRIMARY — WB Pink Sheet 9/2/26 |

⚠️ **Cross-benchmark spreads are real, not error.** DTN retail urea $655/ton vs NOLA barge ~$390/st vs Pink Sheet FOB $400/mt — the same nutrient, three instruments, ~$265 apart. The March desk's registered gate died on exactly this confusion. **DTN retail lags international by weeks** — international series are the leading edge for any transmission timing.

⛔ **INSTRUMENT AT RISK — the NOLA $/st source has no reachable edition after 8/10, and my previous framing of that was wrong.** On 8/17 I recorded the 404 as *"not yet posted — do not read absence as staleness."* Tested 9/9: **eight dated Advanced Turf URLs (8/17, 8/24, 8/31, 9/1, 9/2, 9/7, 9/8, 9/9) all return HTTP 404** and an ~84 kB HTML error page, while the **control 8/10 URL returns HTTP 200 and a real 190,176-byte PDF on the identical path pattern**. The convention is intact, so this is not pattern drift at my end. **VERIFIED:** six-plus consecutive editions absent. **INFERRED, not verified:** the source is discontinued or renamed — the site HTML index 403s to this box and no index was read, so **SEARCH-NOT-FOUND** is the honest token for post-8/10 editions. **Consequence: every NOLA $/st row above is a frozen 8/7 vintage (33 days), and T12's sulfur/curtailment inputs ride the same PDF and are now BLOCKED, not merely unpulled.** Next T5 wake looks for an **alternate** NOLA source rather than re-testing the same URLs. `KB-FERT-033`. The CBOT futures rows (8/15–8/17) are next-oldest and were not refreshed this session either — out of this spawn's scope.

---

## Registered Gates — graded this wake (both watch-only; no capital path)

**GATE-FERT-G5 — NOT FIRED (4 of 4 prints).** ✅ *Graded 9/9 at the publisher against the print itself: "6 of 8 Fertilizer Prices Lower, Led by UAN28", **published 9/9/2026 1:06 PM CDT, data week Aug 31 – Sep 4 2026**. The article EXISTS and was read — this is a graded print, not a re-grade of a stale one.* Letter: *DTN retail **DAP OR MAP > $1,000/ton***; instrument = DTN Progressive Farmer weekly retail **$/ton**. ⛔ Never Pink Sheet $/mt (DAP $793.5), never NOLA $/st (DAP $795–798) — those are different instruments hundreds of dollars apart and the gate does not name them.

| Print (article) | Data week | DAP $/ton | MAP $/ton | Binding leg | Gap to $1,000 | Grade |
|---|---|---|---|---|---|---|
| 8/12/26 *(registration baseline)* | Aug 3–7 | $917 | $959 | MAP | $41 · **+4.28%** | — |
| **8/19/26** | Aug 10–14 | $917 | **$960** | MAP | $40 · **+4.17%** | **NOT FIRED** |
| **8/26/26** | Aug 17–21 | $916 | $959 | MAP | $41 · **+4.28%** | **NOT FIRED** |
| **9/2/26** | Aug 24–28 | $918 | $959 | MAP | $41 · **+4.28%** | **NOT FIRED** |
| **9/9/26** | **Aug 31–Sep 4** | **$919** | **$959** | **MAP** | **$41 · +4.28%** | **NOT FIRED** |

🔑 **The APPROACH RATE is the finding, and it is stated here as a rate — a gate row shows distance, never rate.**

| Leg | 8/12 baseline | 9/9 print | Move over 28 days | **Realised approach rate** | **Implied time-to-fire at that rate** |
|---|---|---|---|---|---|
| **MAP (binding)** | $959 | $959 | **$0 · 0.00%** | **0.00 %/mo** | **UNDEFINED — the line is never reached** |
| DAP (second) | $917 | $919 | +$2 · +0.218% | **+0.22 %/mo** | **~40.5 months** (≈ early 2030) |
| *G5 base rate at registration* | — | — | — | *~+0.50 %/mo* | *~8.5 months* |

**Read it as: the binding leg has moved 0.00% toward its line in four prints, and the second leg is approaching at 44% of the rate the gate was base-rated on.** Distance-to-line is unchanged at +4.28% for the third consecutive print, so **a reader watching only the gap would see "no change" and miss that the gate has become materially less likely to fire.** Distance and rate are two different claims. `[[finding_distance_to_a_threshold_is_a_claim_about_its_basis]]`

⛔ **Headline composition trap, recorded because it would flip a careless read of this gate.** The 9/9 headline says *"6 of 8 fertilizer prices lower"* — that is a **month-over-month** claim. **Week-over-week the composition is 3 higher, 2 lower, 3 flat**: DAP +$1, anhydrous +$15, 10-34-0 +$2 higher; UAN28 −$5, UAN32 −$3 lower; MAP, potash, urea flat. **The largest weekly move in the whole panel was UP.** Do not carry the headline count as a weekly count. `[[finding_headline_keyed_conditional_inherits_its_composition]]`

📌 **Prediction FERT-12 — first in-window print, HOLDING.** MAP $959 ≤ $975 test level ($16 of headroom); print 1 of ~11, Resolve_By 2026-12-02, status stays **OPEN**.

**GATE-FERT-G3 — NOT FIRED (both legs; UNCHANGED this wake).** Letter: *China 2026 urea export quota revised **DOWN**, OR a guidance floor reimposed **ABOVE prevailing intl FOB***. Standing every-wake re-read discharged 2026-09-09 21:0x ET. **SEARCH-NOT-FOUND** on any down-revision or floor reimposition at the named sources (MOFCOM/NDRC relays, Profercy Insights, Fertilizer Daily, CF commentary), searched 9/9. There **is** news this wake — it just doesn't fire either leg.
- **Leg 1 — quota:** 3.3 Mt for 2026 on my standing record. **NOT FIRED.**
- **Leg 2 — floor:** $660/t prilled · $670/t granular FOB lifted early June, **replaced** by a lower *unpublished* guidance price days later. **Behaviour remains dispositive and got stronger:** Fertilizer Daily 9/7 reports China shipping **≥1.2 Mt** into India under the RCF tender with cargoes to leave by 9/24, against offers **<$400/mt CFR**. A floor above market stops exports; exports are accelerating. **NOT FIRED.**
- ⚠️ **CONTAMINATION ESCALATION — logged CONTESTED, not re-refuted by reflex.** The *"2026 allowance expanded to roughly 5–5.5 Mt"* claim surfaced a **FOURTH** time, and this time in a **dated trade-press article** (Fertilizer Daily 9/7/26), not a search summary. My record has three times filed it as contamination (China's historical export range; 2025 actual 4.9 Mt). **Two readings are live and I have not settled them:** either the contamination has propagated into trade press, or a genuine up-revision occurred and my flag has been resolved in the wrong direction. A fourth sighting in a better-authority source is exactly when a standing pre-refutation must be re-examined. `[[finding_a_flag_resolved_in_the_wrong_direction_launders_the_defect]]` · `KB-FERT-034`. **This cannot change the G3 grade under either reading** — leg 1 fires only on a **DOWN**-revision, and 5–5.5 Mt is an up-revision — which is why it is logged at triage and not deep-dived. Plausible mechanism: CF projects **4–6 Mt actual** 2026 Chinese exports and 5–5.5 Mt sits inside that band, so an actual-export projection may be being restated as a quota. Needs a MOFCOM/NDRC primary; none reachable.
- ⚠️ **UNVERIFIED LEAD, deliberately NOT used to close the replacement-level gap.** Vendor-blog sources (keyuanfertilizer.com, yantianglobal.com — MIRROR, low authority, no primary) describe a revised guidance of **≥$430/t FOB small particle / ≥$440/t granular for large-volume orders OUTSIDE India**. Even if true it **carves India out explicitly**, so it cannot bind the flow G3 leg 2 is measured against. Do not promote without a primary.

---

## Live Vectors

| # | Vector | Live read (dated) | State | Score /5 | Independence | Next re-read |
|---|---|---|---|---|---|---|
| 1 | **China export regime** | Quota **3.3 Mt for 2026** on my standing record — ⚠️ **now CONTESTED**: a "5–5.5 Mt allowance" claim appeared in dated trade press 9/7 for the 4th time, unreconciled (KB-FERT-034; cannot fire G3 either way). CF projects **4–6 Mt** actual 2026. Price floor $660/$670/t FOB set end-May, **LIFTED early June**, replaced by an unpublished lower guidance price. **Observed behaviour, not the stated floor, is the binding read, and it strengthened 9/7: China shipping ≥1.2 Mt into India, cargoes out by 9/24, offers <$400/mt CFR** [Fertilizer Daily 9/7, Profercy 8/13] | 🟢→🟡 supply RETURNED, **and accelerating** | 2 | High (policy + 3 independent market reads) | **every wake** (T10) |
| 2 | **Phosphate tight leg** | DAP **$919** / MAP **$959** retail [wk Aug 31–Sep 4], FLAT — **5 prints**: MAP 959/960/959/959/**959**, DAP 917/917/916/918/**919**. Net over 28 days: **MAP $0, DAP +$2.** Root also flat: rock $170.0/mt [Aug] = $170.0 [Jul]. Pink Sheet DAP $793.5/mt [Aug], +1.6% | 🟠 ELEVATED *(level)* — **momentum gone at BOTH ends, fifth week** | **3** | Med — four phosphate benchmarks, four directions in August (rock 0.0%, PS DAP +1.6%, PS TSP −2.1%, retail flat) | T4 weekly · T11 monthly |
| 3 | Hormuz transit | Effectively closed; ~1 transit 8/9 vs ~73/day normal [Lloyd's List 8/12]. Alternative routing (Red Sea/Suez) in use where feasible [ATS 8/10] | 🔴 but **priced** | 3 | Med (BRENT/HAWK own the theater) | via OSPREY/FALCON |
| 4 | Nitrogen price level | Round-tripped internationally (Pink Sheet **$856.9/mt Apr → $390.0 Aug, −54.5%**). ⚠️ **NEW 9/9 — the retail bleed STOPPED and partly reversed:** DTN urea **$655 flat w/w** (first flat print after 3 weeks of declines from $678) and **anhydrous $923 → $938, +$15 / +1.63% w/w**, the largest single move in the panel and **upward**. UAN28 −$5 and UAN32 −$3 still falling, so the reversal is **not** uniform across the nitrogen complex. Anhydrous is **+22% YoY**, the highest YoY of the eight. **One print — a stall, not a trend** | 🟢 NORMALISED *(level)* — **but the downward pass-through has stopped; watch for a second print** | 1 | High | T4 weekly · T5 **BLOCKED** |
| 5 | India import demand | RCF 1.7 Mt tender bids opened 8/11; **lowest bids $390.25/$393.65 CFR** — vs $935/$959 awarded April. Demand intact, **price collapsed** | 🟡 | 2 | High | T1 |
| 6 | Food-CPI transmission | July food-at-home **−0.07% m/m / +2.7% y/y** [BLS via FRED CUSR0000SAF11]. ERS forecasts FAH 2.7% (2026) / 2.9% (2027) — **fertilizer not a cited driver** | 🟢 NOT FIRING | 1 | High | T2/T3 |
| 7 | Qatar LNG → fertilizer capacity | **12.8 mtpa** (Trains 4 & 6, Ras Laffan) = **~17%** of Qatar export capacity; missile strikes 3/18–19/26; 3–5 yr repair CONFIRMED. **No primary links this damage to ammonia/urea output** — inference deleted, not carried | 🟡 | 2 | Low (single event, unlinked to N) | on QAFCO/Mesaieed disclosure |
| 8 | European production economics | Gas ~$16.00/MMBtu → theoretical ammonia ~$667/mt FOB, **above prevailing urea FOB = economically shut**. Physical closure count **PAYWALLED**, unresolved since March | 🟡 UNRESOLVED | 2 | Low (proxy only) | on BRENT gas signal |

**Convergence: 16/40** — re-exercised 2026-09-09 and **HELD**. Vector 2 stays at **3**: a fifth flat print neither confirms a top nor restores the cost-push, and one print cannot move a score. Vector 4 stays at **1** on level, but its *read* is materially changed — the retail bleed stopped and anhydrous reversed **+1.63% w/w**; that is a one-print observation and I am explicitly **not** scoring it until a second print. Vector 1's read gained a contested quota figure without changing its score. Was 17/40 before the 9/2 cut of vector 2 from 4→3. **No vector at 5.**

---

## What Changed This Session (2026-09-09 — T4 wake, spawned Tier-1 due-row; DOCKET L266 / GATES GATE-FERT-G5 review_by 2026-09-09)

1. **GATE-FERT-G5 graded on a real 9/9 print: NOT FIRED, 4 of 4.** The article published (9/9/2026 1:06 PM CDT, data wk Aug 31–Sep 4) and was read at the publisher, so this is a graded print, not a stale re-grade. **MAP $959 (binding, +4.28% below $1,000) · DAP $919 (+8.81% below).** All eight products in the price panel above; `KB-FERT-031`.
2. **The approach rate is now measured over 28 days and it is worse than the 9/2 read implied.** Binding leg **MAP: $959 → $959, 0.00%/mo, time-to-fire UNDEFINED.** Second leg **DAP: $917 → $919, +0.22%/mo, ~40.5 months** — **44% of the ~+0.50%/mo the gate was base-rated on** (~8.5 months implied). Distance-to-line has now printed **+4.28% three times running**, so the gap alone shows "no change" while the gate has become materially less likely to fire. That divergence is the finding; the table is in the G5 section. `KB-FERT-032`.
3. **⛔ The headline would have inverted a careless read.** DTN's own headline is *"6 of 8 Fertilizer Prices Lower"* — a **month-over-month** count. **Week-over-week it is 3 higher / 2 lower / 3 flat, and the biggest move in the panel was UP** (anhydrous +$15). A conditional keyed on the headline fires on a composition that refutes it. `[[finding_headline_keyed_conditional_inherits_its_composition]]`
4. **The nitrogen retail bleed stopped.** Urea printed **$655 flat** — its first non-declining print after three weeks of $678 → $655 — and **anhydrous reversed +$15 / +1.63% w/w** to $938 (+22% YoY, the panel's highest). UAN28 (−$5) and UAN32 (−$3) are still falling, so the reversal is **not uniform**. **One print. I did not move vector 4's score on it** and it needs a second print on 9/16 before it is anything.
5. **⛔ The Advanced Turf NOLA instrument is unreachable, and my own prior framing of that was wrong.** On 8/17 I recorded the 404 as *"not yet posted — do not read absence as staleness."* Tested 9/9: **eight dated URLs 8/17→9/9 all 404** while the **control 8/10 URL returns a real 190,176-byte PDF on the identical pattern**. VERIFIED = editions absent; INFERRED = discontinued/renamed (the index 403s, so no index was read). **T5 re-framed INSTRUMENT AT RISK; the NOLA $/st panel rows are a frozen 8/7 vintage (33 days); T12's sulfur inputs ride the same PDF and are now BLOCKED, not merely unpulled.** `KB-FERT-033`
6. **⚠️ The "5–5.5 Mt" China quota claim reached dated trade press — logged CONTESTED, not re-refuted by reflex.** Fourth sighting, first time in an article with a byline and a date (Fertilizer Daily 9/7). My record says 3.3 Mt and has thrice called this contamination. **I have not settled it**, and I did not deep-dive it, because **it cannot fire G3 under either reading** (leg 1 needs a **DOWN**-revision). Plausible mechanism: CF's **4–6 Mt actual-export** projection restated as a quota. `[[finding_a_flag_resolved_in_the_wrong_direction_launders_the_defect]]` · `KB-FERT-034`
7. **G3 behaviour evidence strengthened: China shipping ≥1.2 Mt into India**, cargoes out by 9/24, offers <$400/mt CFR [Fertilizer Daily 9/7]. A floor above market stops exports; exports are accelerating. **Both G3 legs NOT FIRED.** ⚠️ A vendor-blog lead describing a **≥$430/$440 FOB** replacement guidance was found and **deliberately not used** to close the PUBLIC-AND-UNFETCHED replacement-level gap — no primary, and it carves India out explicitly.
8. **T1 not discharged on a third check.** The 9/7 article gives a **volume** (≥1.2 Mt) and restates the already-known lowest **offers** ($390.25/$393.65 CFR). **A bid is not an award and a shipment volume is not a price.** Row held at 9/16, not re-dated.
9. **My own 9/5 G3 confirm had the actor inverted — PROME is right.** I wrote *"India offers <$400/mt CFR"*; the correct actor is **China offering INTO India**. Corrected text returned in the delivery memo for PROME to apply. Root cause worth keeping: **an actor inversion in a price referent survives every unit, level and date check, because the level was correct.**
10. **`workbook/board_log.tsv` did not exist.** The charter §3b declared it installed 2026-09-02; the file was never created, so five months of the consumption record it mandates were unwritten. Created this session with the 9/2 rows reconstructed from `RECEIPT.md` and marked RECONSTRUCTED. *(A declared-installed artifact that was never created passes every prose audit of the charter. `[[finding_record_of_an_action_is_not_the_action]]`)*
11. **A duplicate row in my own Open Instrument Gaps table was removed** — "Phosphate cost-push second source" appeared twice with different staleness counts (one saying "since 8/17", one "since 8/17, 19 days"), which is two live claims about one gap. Merged to one row, now 23 days.

---

## What Changed — prior session (2026-09-05 — T11 wake, spawned; DOCKET L283)

**ROTATED VERBATIM to `archive/STATUS_whatchanged_2026-09-05_ROTATED.md` on 2026-09-09** (read-cap remedy: STATUS was 33,722 B against a 32,550 B budget; two-state rotation, crc-stamped, per Data Hygiene). Headline of that session, kept here as the single load-bearing carry-forward: **the third consecutive Pink Sheet phosphate-rock rise did NOT occur** — rock printed **$170.0/mt for Aug 2026, exactly flat against July** — and a kill-rail paraphrase in this file had drifted **$4.40 looser than the letter** (*"≤$157/mt"* vs the true **$152.5**) and was corrected. Everything else in that block is history; read the archived file for it.

## Open Predictions (the live loop — 2 OPEN, 10 resolved)

| ID | Claim | Instrument + basis | Conf | Resolve_By |
|---|---|---|---|---|
| **FERT-11** | Pink Sheet **phosphate rock re-plateaus at exactly $170.0/mt** for the Sep-2026 data month — neither resuming the break nor reversing it | WB Pink Sheet Oct-2026 edition / `CMO-Historical-Data-Monthly.xlsx` row 2026M09, $/mt, as first published. MECE: >170.0 MISS-HIGH · =170.0 HIT · <170.0 MISS-LOW. Base rate at registration (n=800 months): after a flat month, flat **87.8%** full history / **71.1%** 2006–26 | **72%** | 2026-10-09 |
| **FERT-12** | DTN retail **MAP never prints above $975/ton** on any weekly article 9/9 → 11/25 | DTN Progressive Farmer weekly, US national avg $/ton, as first published; test = max over all in-window prints. $975 = +1.67% from $959, just above the ~+0.5%/mo trajectory G5 was base-rated on. **Print 1 of ~11 logged 9/9: MAP $959 — HOLDING, $16 of headroom** | **78%** | 2026-12-02 |

*Full six-element WQ-162 grading bases, anchor types and if-falsified actions are in `workbook/PREDICTIONS.tsv` — the row is the letter, this table is the pointer.*

---

## Exit Rules / Kill Rail

**Kill rail re-derived: 2026-08-17.** Full protocol + bidirectional flip test: `workbook/EXIT_PROTOCOL.md`.

- **Nitrogen channel — already DEAD** (channel-kill, not thesis-kill). Killed by China's quota resumption, not by demand. Migration path: phosphate leg + CF single-name fundamentals.
- **Phosphate channel — LIVE, but stalled at both ends.** Dies if Pink Sheet phosphate rock prints back at or below **$152.5/mt** — its pre-break plateau level, `EXIT_PROTOCOL.md` §Channel B leg 1 — for **2 consecutive monthly editions** **AND** DTN retail MAP prints **below $900/ton** for 2 consecutive weekly articles. **Neither leg is met, and neither is close:** rock $170.0/mt [Aug] is **11.5% above** the kill level and has moved 0.0% toward it; MAP **$959 [wk Aug 31–Sep 4]** is **6.6% above** its $900 leg and has moved **$0 in 28 days**. ⚠️ **Correction to my own 9/2 wording:** this rail was written here as *"≤$157/mt"*, which is **$4.40 looser than the letter** and would have been satisfied by June's $156.9 — a partial retrace to the break's own starting point reading as a channel kill. The letter is **$152.5**. ⚠️ **And the rail still cannot see what actually happened:** it tests for *reversal*; what occurred at both ends is a *stall*. **"Kill not triggered" is not "thesis intact"** — the honest state is *level held, momentum stopped*. Next root-end read: T11, **2026-10-02** (the World Bank's own stated next update, read 9/5), graded against prediction **FERT-11**.
- **Transmission question — OPEN, not a carried prediction.** Dies if BLS food-at-home m/m stays <+0.4% through the Nov-2026 print (T3/T6) with no upward ERS revision citing inputs.
- **Timing vs mechanism:** the March *timing* claim is graded MISS; the mechanism is **not** refuted (`finding_market_ignoring_is_not_market_refuting`). It is un-instrumented, and re-opening it requires a fresh input shock, not a re-read of the old one.

---

## Named Blind Spots (exclusions register — I do not cover these)

| Excluded | Owner | On sighting |
|---|---|---|
| **Potash supply shock** | ⚠️ **NO LONGER UNOWNED — FERT owns it at TRIAGE DEPTH ONLY** (Will-ruled 2026-08-18; this row was stale from 8/18 until corrected 9/2) | Unchanged in practice: KB row + PROME flag, **no deep-dive, no comparison, no trend adjective**. *(Live: DTN retail potash **$493/ton** [wk **Aug 31–Sep 4**, DTN 9/9 — `KB-FERT-035`]; NOLA barge $335–345/st [8/7, frozen vintage]; Pink Sheet KCl **$386.9/mt** [Aug].)* ✅ **The 8/22 "assert neither" caveat is DISCHARGED (MARCO 9/2, KB-FERT-030):** CBP's §338 Canada HTS enumeration — 1,074 lines across 65 chapters — carries **ZERO Chapter 31 lines** (`3104.*`/`3105.*` checked explicitly). **Mechanism = ABSENCE FROM THE POSITIVE LIST**, read not inferred. ⛔ Carry no further: an increment was **declined**, nothing **relieved** (existing AD/CVD untouched), and this is the **US §338 only** — Canada's 9/8 counter-tariff line list is a separate instrument, **still unread** (canada.ca 404). |
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
| RCF Aug-2026 tender **award** price | **PUBLIC-AND-UNFETCHED → PAYWALLED** | **3rd check 9/9, still unpublished free.** Fertilizer Daily 9/7 adds a **volume** (China ≥1.2 Mt, cargoes out by 9/24) and restates the already-known lowest **offers** ($390.25 CFR east / $393.65 west) — **a bid is not an award and a shipment volume is not a price**, so the gap is unchanged. Argus/Profercy hold it |
| Phosphate cost-push second source | **UNRESOLVED — single-source since 8/17, 23 days; now BLOCKED** | T12's own precondition, never discharged. **Escalated 9/9:** the second read this row demands rides the Advanced Turf weekly PDF, which has no reachable edition after 8/10 (row below) — so this is no longer "not pulled", it is **not obtainable from the named instrument**. With retail flat 5 prints AND the root flat in August, the rock+sulfur cost-push now has **no confirmation at any of the three points it should show up**. Needs a NEW instrument; Mosaic IR is the other half of this row and was not pulled. *(Merged 9/9 from two duplicate rows that carried different staleness counts — two live claims about one gap.)* |
| **Advanced Turf weekly NOLA $/st PDF (T5/T12 instrument)** | **SEARCH-NOT-FOUND after 2026-08-10 — INSTRUMENT AT RISK** | 8 dated URLs (8/17→9/9) return HTTP 404; the **control 8/10 URL returns a real 190,176-byte PDF on the identical pattern**, so the convention is intact. VERIFIED = editions absent. INFERRED, not verified = discontinued or renamed (the site index 403s to this box; no index read). Freezes the NOLA $/st panel at its 8/7 vintage. `KB-FERT-033` |
| BLS Oct-2025 food-at-home print | **MISSING AT SOURCE** | FRED row exists but is **blank** — a real gap, not a zero. Any "N consecutive months" CPI gate must state its missing-print rule |
| Canada 9/8 counter-tariff HTS line list | **PUBLIC-AND-UNFETCHED** | canada.ca complete-list page 404'd on 9/2 (MARCO). Fertiliser is absent from the *named press sectors*, which is **not** an absence from an enumeration. Not load-bearing for any FERT letter — no registered FERT gate names a tariff line |

---

## BOTTOM LINE

**GATE-FERT-G5 is NOT FIRED on a real 9/9 print — the fourth of four — and the finding is the rate, not the level.** The DTN article published (9/9/2026 1:06 PM CDT, data week Aug 31 – Sep 4) and was read at the publisher: **MAP $959/ton, DAP $919/ton, both against a $1,000/ton line.** MAP is the binding leg at **+4.28% below**, and that same +4.28% has now printed **three weeks running** — so the gap says "nothing happened" while what actually happened is that the gate stopped approaching. Measured over the 28 days from the 8/12 registration baseline: **MAP $959 → $959 = 0.00%/mo, implied time-to-fire UNDEFINED**; DAP $917 → $919 = **+0.22%/mo, ~40.5 months**, against the **~+0.50%/mo** the gate was base-rated on (~8.5 months implied). **A row shows distance; only a rate says whether the line is being approached, and this one is not.** Second read of the session: **DTN's own headline is a trap** — *"6 of 8 prices lower"* is month-over-month, while **week-over-week the panel is 3 higher, 2 lower, 3 flat and the largest single move was UP** (anhydrous +$15/+1.63% to $938, +22% YoY), so **the nitrogen retail bleed has stopped after three weeks of decline** — one print, not scored, needs 9/16 to confirm. **GATE-FERT-G3 is NOT FIRED on both legs**, and behaviour got more dispositive: China is shipping **≥1.2 Mt into India** with cargoes out by 9/24 against offers **<$400/mt CFR** [Fertilizer Daily 9/7] — a floor above market stops exports and exports are accelerating. Two honest negatives I am not papering over: the **"5–5.5 Mt quota" claim reached dated trade press on its fourth sighting** and is now logged **CONTESTED** rather than re-refuted by reflex (it cannot fire G3 either way, so it stays at triage), and the **Advanced Turf NOLA instrument has no reachable edition after 8/10** — eight dated URLs 404 while the 8/10 control returns a real PDF — which freezes my NOLA $/st rows at an 8/7 vintage and **blocks**, not merely defers, T12's phosphate cost-push second source. Prediction **FERT-12 is HOLDING** on print 1 of ~11 ($16 of headroom). I wake next on the **DTN weekly 9/16** (G5 again, FERT-12 print 2, and the anhydrous confirm), the **August CPI food-at-home print 9/11**, **T10/G3 review 9/15**, **T1 9/16**, and the next **Pink Sheet 10/02** (grades FERT-11).
