# FERT — Status

**Domain:** Fertilizer supply/price/policy → food-CPI transmission → CF Industries positioning
**Class:** Market domain — EVENT-DRIVEN SPECIALIST (wakes on named triggers; no standing daily desk)
**Last real data refresh:** 2026-09-15 (**Profercy · NDRC index · CF Q2-2026 commentary · live fetch.py prices** — T10/GATE-FERT-G3 re-read, DOCKET L204. *Retail panel below is still the 9/9 DTN vintage; next print 9/16*)
**Session wall clock:** 2026-09-15 10:01 Tuesday (boot.py)
**Situation Tier:** 🟡 MONITORING — **China's export floors are ratcheting DOWN, not constraining**; phosphate stalled at both ends 5 weeks; nitrogen retail bleed stopped (awaiting the 9/16 confirm)

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

⚠️ **Cross-benchmark spreads are real, not error.** DTN retail urea **$655/ton** vs NOLA barge **~$390/st** vs Pink Sheet FOB **$400/mt** — same nutrient, three instruments, **~$265 apart**. The March desk's registered gate died on exactly this. **DTN retail lags international by weeks** — international series are the leading edge for transmission timing.

⛔ **INSTRUMENT AT RISK — the NOLA $/st source has no reachable edition after 2026-08-10 (36 days).** Eight dated Advanced Turf URLs 404 against a working 8/10 control (190,176 B), so the URL convention is intact and this is not drift at my end. **VERIFIED:** editions absent. **INFERRED, not verified:** discontinued or renamed (the site index 403s; no index read) — **SEARCH-NOT-FOUND** is the honest token. **Consequence: every NOLA $/st row above is a frozen 8/7 vintage, and T12's sulfur inputs ride the same PDF and are BLOCKED, not merely unpulled.** Next T5 wake looks for an **alternate** source, not the same URLs. Detail → `workbook/INSTRUMENT_GAPS.md` · `KB-FERT-033`. *(CBOT futures rows are the next-oldest at 8/15–8/17 and were not refreshed this session — out of this spawn's scope.)*

---

## Registered Gates — graded this wake (both watch-only; no capital path)

**GATE-FERT-G5 — NOT FIRED (4 of 4 prints).** ✅ *Graded 9/9 at the publisher against the print itself: "6 of 8 Fertilizer Prices Lower, Led by UAN28", **published 9/9/2026 1:06 PM CDT, data week Aug 31 – Sep 4 2026**. The article EXISTS and was read — this is a graded print, not a re-grade of a stale one.* Letter: *DTN retail **DAP OR MAP > $1,000/ton***; instrument = DTN Progressive Farmer weekly retail **$/ton**. ⛔ Never Pink Sheet $/mt (DAP $793.5), never NOLA $/st (DAP $795–798) — those are different instruments hundreds of dollars apart and the gate does not name them.

**Print-by-print history + the approach-rate table → `workbook/GATE_GRADES.md`** (split 9/15, read-cap remedy).

**Read it as: the binding leg has moved 0.00% toward its line in four prints, and the second leg is approaching at 44% of the rate the gate was base-rated on.** Distance-to-line is unchanged at +4.28% for the third consecutive print, so **a reader watching only the gap would see "no change" and miss that the gate has become materially less likely to fire.** Distance and rate are two different claims. `[[finding_distance_to_a_threshold_is_a_claim_about_its_basis]]`

⛔ **Headline composition trap, recorded because it would flip a careless read of this gate.** The 9/9 headline says *"6 of 8 fertilizer prices lower"* — that is a **month-over-month** claim. **Week-over-week the composition is 3 higher, 2 lower, 3 flat**: DAP +$1, anhydrous +$15, 10-34-0 +$2 higher; UAN28 −$5, UAN32 −$3 lower; MAP, potash, urea flat. **The largest weekly move in the whole panel was UP.** Do not carry the headline count as a weekly count. `[[finding_headline_keyed_conditional_inherits_its_composition]]`

📌 **Prediction FERT-12 — first in-window print, HOLDING.** MAP $959 ≤ $975 test level ($16 of headroom); print 1 of ~11, Resolve_By 2026-12-02, status stays **OPEN**.

**GATE-FERT-G3 — NOT FIRED (both legs; 5th consecutive re-read).** ✅ *Graded 2026-09-15 at the letter, DOCKET L204 — letter read BEFORE the data.* Letter: *China 2026 urea export quota revised **DOWN**, OR a guidance floor reimposed **ABOVE prevailing intl FOB***. Instruments: MOFCOM/NDRC relay + CF commentary + Profercy. **Full working → `outbox/2026-09-15_from-FERT_G3-china-quota-floor-re-read-DOCKET-L204.md`.**

- **Leg 1 — quota: NOT FIRED.** Standing record **3.3 Mt**. Every current sighting is **level or UP**; leg 1 fires only on a **DOWN**-revision. The 5-sighting *"5–5.5 Mt"* claim is **RESOLVED as a category error** — it sits inside **CF's 4–6 Mt actual-EXPORT projection**, and an export projection is not a quota. Four distinct measures were being conflated under one word (3.3 Mt annual quota · 1.5–1.6 Mt Jun–Aug batch · 2.0–2.6 Mt June estimate · 4–6 Mt CF export projection). `KB-FERT-037`
- **Leg 2 — floor: NOT FIRED, and the direction is the finding.** The floor **ladder**, now dated: **$660/$670/t fob (India $680) [Profercy 5/26]** → **LIFTED early June** → **$500/t fob India reinstated 6/9 [Profercy, named instrument]** → **$430/t prilled · $440/t granular non-India, $500/t India [Woodwell Agro via aggregator — MIRROR]**. CF: floors *"remain in effect, although they have been revised."* **Floors have ratcheted DOWN all year, tracking the market rather than constraining it — the inverse of leg 2's constraint.** `KB-FERT-036`
- **The test, applied.** Prevailing **$443/t** [Fertilizer Daily 9/9, TE value 9/4 — ⚠️ a global index level, **not** a named FOB benchmark]. Non-India floors **$430/$440 sit below it** ⇒ no fire. The **$500 India floor is above it**, and still does not fire on **two independent grounds**: (1) reinstated **6/9**, **before** gate registration **8/17** ⇒ baseline state, not a reimposition; (2) **measured, not assumed** — Egypt FOB was **$560–600/t at the start of June → $450–495/t by 6/11**, so a $500 floor set 6/9 was **at or below** prevailing. **Leg 2 did not fire in June either.**
- **Behaviour stays the more dispositive read, and it now contradicts the $500 India floor outright:** Chinese offers into India **<$400/t CFR across both coasts** [Profercy 8/13]; RCF absorbed **1.78 Mt below $400/t**. **CFR below $400 cannot coexist with an enforced $500 FOB floor** (CFR = FOB + freight) ⇒ that floor is **unenforced or superseded**. Logged **CONTESTED** — I am not asserting which.
- ⛔ **Registration-cell correction for PROME to apply** (Will-gated surface; I do not edit it): the cell's *"$660 floor LIFTED early-June — kill-on-sight as a live constraint"* is **correct as to $660 and incomplete as to the regime.** The floor **mechanism** re-based twice and is live at $430/$440/$500. Proposed replacement text → §7① of the outbox memo.
- **Instruments, exact paths:** Profercy ✅ reached (index + article) · **NDRC** ✅ reached, **SEARCH-NOT-FOUND** Aug–Sep 2026 · **MOFCOM ❌ UNREACHABLE — `ECONNRESET`** (a reachability failure at a named path, **not** an absence) · **CF commentary ⚠️ MIRROR only** (sec.gov 403s to this box; alternate = `ir.cfindustries.com`) · **Barchart `UF*0` ❌ empty ⇒ no live named-benchmark urea print this session.**

---

## Live Vectors

| # | Vector | Live read (dated) | State | Score /5 | Independence | Next re-read |
|---|---|---|---|---|---|---|
| 1 | **China export regime** | Quota **3.3 Mt for 2026**, standing record **UNCHANGED** — the *"5–5.5 Mt"* claim (5th sighting) is **RESOLVED as a category error**: it sits inside **CF's 4–6 Mt actual-EXPORT projection**, not the quota series `KB-FERT-037`. Floor **ladder now dated**: $660/$670 (India $680) [Profercy 5/26] → LIFTED early June → **$500/t fob India reinstated 6/9 [Profercy]** → **$430/$440 non-India, $500 India** [MIRROR]; CF: floors *"remain in effect, although revised."* **Floors ratcheting DOWN = tracking the market, not constraining it** `KB-FERT-036`. **Observed behaviour stays the binding read: China shipping ≥1.2 Mt into India, offers <$400/mt CFR** [Fertilizer Daily 9/7, Profercy 8/13] — which **contradicts the $500 India floor outright** | 🟢→🟡 supply RETURNED, **floors following price down** | 2 | High (policy + 3 independent market reads) | **every wake** (T10 → 10/15) |
| 2 | **Phosphate tight leg** | DAP **$919** / MAP **$959** retail [wk Aug 31–Sep 4], FLAT — **5 prints**: MAP 959/960/959/959/**959**, DAP 917/917/916/918/**919**. Net over 28 days: **MAP $0, DAP +$2.** Root also flat: rock $170.0/mt [Aug] = $170.0 [Jul]. Pink Sheet DAP $793.5/mt [Aug], +1.6% | 🟠 ELEVATED *(level)* — **momentum gone at BOTH ends, fifth week** | **3** | Med — four phosphate benchmarks, four directions in August (rock 0.0%, PS DAP +1.6%, PS TSP −2.1%, retail flat) | T4 weekly · T11 monthly |
| 3 | Hormuz transit | Effectively closed; ~1 transit 8/9 vs ~73/day normal [Lloyd's List 8/12]. Alternative routing (Red Sea/Suez) in use where feasible [ATS 8/10] | 🔴 but **priced** | 3 | Med (BRENT/HAWK own the theater) | via OSPREY/FALCON |
| 4 | Nitrogen price level | Round-tripped internationally (Pink Sheet **$856.9/mt Apr → $390.0 Aug, −54.5%**). ⚠️ **NEW 9/9 — the retail bleed STOPPED and partly reversed:** DTN urea **$655 flat w/w** (first flat print after 3 weeks of declines from $678) and **anhydrous $923 → $938, +$15 / +1.63% w/w**, the largest single move in the panel and **upward**. UAN28 −$5 and UAN32 −$3 still falling, so the reversal is **not** uniform across the nitrogen complex. Anhydrous is **+22% YoY**, the highest YoY of the eight. **One print — a stall, not a trend** | 🟢 NORMALISED *(level)* — **but the downward pass-through has stopped; watch for a second print** | 1 | High | T4 weekly · T5 **BLOCKED** |
| 5 | India import demand | RCF 1.7 Mt tender bids opened 8/11; **lowest bids $390.25/$393.65 CFR** — vs $935/$959 awarded April. Demand intact, **price collapsed** | 🟡 | 2 | High | T1 |
| 6 | Food-CPI transmission | July food-at-home **−0.07% m/m / +2.7% y/y** [BLS via FRED CUSR0000SAF11]. ERS forecasts FAH 2.7% (2026) / 2.9% (2027) — **fertilizer not a cited driver** | 🟢 NOT FIRING | 1 | High | T2/T3 |
| 7 | Qatar LNG → fertilizer capacity | **12.8 mtpa** (Trains 4 & 6, Ras Laffan) = **~17%** of Qatar export capacity; missile strikes 3/18–19/26; 3–5 yr repair CONFIRMED. **No primary links this damage to ammonia/urea output** — inference deleted, not carried | 🟡 | 2 | Low (single event, unlinked to N) | on QAFCO/Mesaieed disclosure |
| 8 | European production economics | Gas ~$16.00/MMBtu → theoretical ammonia ~$667/mt FOB, **above prevailing urea FOB = economically shut**. Physical closure count **PAYWALLED**, unresolved since March | 🟡 UNRESOLVED | 2 | Low (proxy only) | on BRENT gas signal |

**Convergence: 16/40** — re-exercised 2026-09-09 and **HELD**. Vector 2 stays at **3**: a fifth flat print neither confirms a top nor restores the cost-push, and one print cannot move a score. Vector 4 stays at **1** on level, but its *read* is materially changed — the retail bleed stopped and anhydrous reversed **+1.63% w/w**; that is a one-print observation and I am explicitly **not** scoring it until a second print. Vector 1's read gained a contested quota figure without changing its score. Was 17/40 before the 9/2 cut of vector 2 from 4→3. **No vector at 5.**

---

## What Changed This Session (2026-09-15 — T10 wake, spawned Tier-1 due-row; DOCKET L204 / GATE-FERT-G3 review_by 2026-09-15)

**The graded read is in §Registered Gates; the full working with every source + date and the §7 ASK to PROME is `outbox/2026-09-15_from-FERT_G3-china-quota-floor-re-read-DOCKET-L204.md`. Neither is restated here** (read-cap split 9/15). What this session actually changed:

1. **G3 graded NOT FIRED both legs, 5th consecutive — grade unmoved, leg 2's BASIS moved.** The post-June replacement floor closed at a **named** instrument (**$500/t fob India, 6/9 [Profercy]**) — the gap I *declined* to close from vendor blogs on 9/9. `KB-FERT-036`
2. **The "5–5.5 Mt" contamination resolved as a *category error*** — it sits inside CF's **4–6 Mt actual-EXPORT** projection; an export projection is not a quota. Record holds **3.3 Mt**. ⛔ **Rule earned: a tonnage figure without its measure-type is malformed on sight.** `KB-FERT-037`
3. **⛔ A five-month-stale headline ("China Cuts 2026 Urea Export Quota", dateline 2026-04-24) was caught by dateline before it could fire leg 1.** Charter rule (c), same class as the 2024 Argus piece.
4. **Inbox drained 2/2, both verified against LIVE prices rather than relayed** — NG=F **$2.95**, HO=F **$210.00/bbl** ⚠️ *on HOX26, not the 1st-continuous contract the record was quoted on.* **The drain produced the carry-forward read: Henry Hub under $3 against European producers curtailing on high gas = the US nitrogen cost advantage widening at both ends at once** — constructive for CF on the cost side. `KB-FERT-038`. Record diesel flagged **forward** into the 9/16 G5 read, not scored today.
5. **Limits stated, not papered over:** **MOFCOM ECONNRESET** — the one named instrument with no successful read (reachability failure, **not** an absence; NDRC *was* reached = true SEARCH-NOT-FOUND). **Barchart empty ⇒ no live named-benchmark urea print.** **Four due triggers (T3/T5/T8/T12) not worked and deliberately NOT re-dated** — only T10 moved (→10/15); *a re-dated row you didn't work is a false all-clear.*
6. **STATUS rotated under its read cap.** It arrived at **94% of budget** and this session's content pushed it to 100%. Split out: `workbook/INSTRUMENT_GAPS.md` · `workbook/GATE_GRADES.md` · exit-rail narrative → `workbook/EXIT_PROTOCOL.md`. **Detail moved, not reworded.**

---

## What Changed — prior sessions

**2026-09-09** → `archive/STATUS_whatchanged_2026-09-09_ROTATED.md` (rotated 9/15). Carry-forward: **G5 NOT FIRED 4-of-4; the approach RATE — MAP 0.00%/mo, DAP +0.22%/mo vs +0.50%/mo base-rated — is the finding, not the level**; the Advanced Turf NOLA instrument went dark after 8/10.
**2026-09-05** → `archive/STATUS_whatchanged_2026-09-05_ROTATED.md` (rotated 9/9). Carry-forward: **the third consecutive Pink Sheet phosphate-rock rise did NOT occur** — rock printed **$170.0/mt Aug, flat vs July**.

---

## Open Predictions (the live loop — 2 OPEN, 10 resolved)

| ID | Claim | Instrument + basis | Conf | Resolve_By |
|---|---|---|---|---|
| **FERT-11** | Pink Sheet **phosphate rock re-plateaus at exactly $170.0/mt** for the Sep-2026 data month — neither resuming the break nor reversing it | WB Pink Sheet Oct-2026 edition / `CMO-Historical-Data-Monthly.xlsx` row 2026M09, $/mt, as first published. MECE: >170.0 MISS-HIGH · =170.0 HIT · <170.0 MISS-LOW. Base rate at registration (n=800 months): after a flat month, flat **87.8%** full history / **71.1%** 2006–26 | **72%** | 2026-10-09 |
| **FERT-12** | DTN retail **MAP never prints above $975/ton** on any weekly article 9/9 → 11/25 | DTN Progressive Farmer weekly, US national avg $/ton, as first published; test = max over all in-window prints. $975 = +1.67% from $959, just above the ~+0.5%/mo trajectory G5 was base-rated on. **Print 1 of ~11 logged 9/9: MAP $959 — HOLDING, $16 of headroom** | **78%** | 2026-12-02 |

*Full six-element WQ-162 grading bases, anchor types and if-falsified actions are in `workbook/PREDICTIONS.tsv` — the row is the letter, this table is the pointer.*

---

## Exit Rules / Kill Rail

**Kill rail re-derived: 2026-08-17.** Durable rules + bidirectional flip test + the 9/2–9/9 reasoning: **`workbook/EXIT_PROTOCOL.md`** (narrative moved there 9/15, read-cap split). STATUS carries only the **live distance to each leg**:

- **Nitrogen channel — DEAD** (channel-kill, not thesis-kill; killed by China's quota resumption, not demand). Migration path: phosphate leg + CF single-name.
- **Phosphate channel — LIVE, stalled at both ends.** Kill needs **BOTH**: Pink Sheet rock ≤ **$152.5/mt** ×2 consecutive editions **AND** DTN retail MAP < **$900/ton** ×2 consecutive articles. **Neither met, neither close:** rock **$170.0/mt [Aug]** = **11.5% above** the leg, moved **0.0%** toward it; MAP **$959 [wk Aug 31–Sep 4]** = **6.6% above** its leg, moved **$0 in 28 days**. ⚠️ **The rail tests for *reversal*; what happened is a *stall*** — "kill not triggered" is **not** "thesis intact"; the honest state is **level held, momentum stopped**. Next root read T11 **10/02**, graded against **FERT-11**.
- **Transmission question — OPEN, not a carried prediction.** Dies if BLS food-at-home m/m stays **<+0.4%** through the Nov-2026 print (T3/T6) with no upward ERS revision citing inputs.
- **Timing vs mechanism:** the March *timing* claim is graded **MISS**; the mechanism is **not** refuted — it is **un-instrumented**, and re-opening it needs a fresh input shock, not a re-read of the old one.

---

## Named Blind Spots (exclusions register — I do not cover these)

Canonical register → `CLAUDE.md` §Exclusions. Live state only:

| Excluded | Owner | On sighting |
|---|---|---|
| **Potash supply shock** | ⚠️ **FERT owns it at TRIAGE DEPTH ONLY** (Will-ruled 2026-08-18) | KB row + PROME flag. **No deep-dive, no comparison, no trend adjective.** *Live triage cells: DTN retail potash **$493/ton** [wk Aug 31–Sep 4, DTN 9/9]; NOLA barge **$335–345/st** [8/7, frozen vintage]; Pink Sheet KCl **$386.9/mt** [Aug]. `KB-FERT-035`.* ✅ The 8/22 "assert neither mechanism" caveat is **DISCHARGED** — CBP's §338 Canada enumeration carries **zero Chapter 31 lines**, read not inferred (`KB-FERT-030`, MARCO 9/2). ⛔ **US §338 only**; Canada's 9/8 counter-tariff list is a separate, still-unread instrument |
| Clean-ammonia / ammonia-as-fuel demand | NO OWNER | KB row + PROME flag |
| Qatar QAFCO/Mesaieed physical damage | OSPREY/FALCON | Consume their signal; I own the **capacity consequence** only |

---

## Open Instrument Gaps — load-bearing only (full register → `workbook/INSTRUMENT_GAPS.md`)

**Split to the workbook 2026-09-15** (read-cap remedy). The full 11-row classified register lives there; these three are the ones that move a read:

| Item | Class | Note |
|---|---|---|
| **Advanced Turf weekly NOLA $/st PDF (T5/T12 instrument)** | **SEARCH-NOT-FOUND after 2026-08-10 — INSTRUMENT AT RISK, 36 days** | 8 dated URLs 404 against a working 8/10 control (190,176 B). Freezes the **NOLA $/st** panel at its 8/7 vintage **and** blocks T12's phosphate cost-push second source — **two watches down on one dependency.** Needs a replacement instrument; none found. Flagged to PROME 9/15. `KB-FERT-033` |
| Phosphate cost-push second source | **UNRESOLVED — single-source since 8/17, 29 days; BLOCKED** | Rides the dead Advanced Turf PDF above. With retail flat 5 prints **and** rock flat in August, the rock+sulfur cost-push has **no confirmation at any of the three points it should show up.** Mosaic IR is the unpulled other half |
| China guidance price, post-June level | **PARTIALLY RESOLVED 9/15** | **$500/t fob India reinstated 2026-06-09 [Profercy — headline read, body not opened]**; current $430/$440 non-India + $500 India is **MIRROR only**. Residual gap = a **MOFCOM/NDRC primary** nobody has (MOFCOM ECONNRESETs from this box). **Not load-bearing for G3** — behaviour (<$400/t CFR) settles the grade either way |

---

## BOTTOM LINE

**GATE-FERT-G3 is NOT FIRED on both legs for the fifth straight re-read, and the finding is the direction rather than the grade: China's urea export floors have ratcheted DOWN all year — $680 → $500/t fob India, $660/$670 → $430/$440 elsewhere — so the floor is *following* the market down instead of constraining it, the exact inverse of what leg 2 watches for.** The replacement level I refused to take from vendor blogs on 9/9 closed properly this pass at a named instrument (**$500/t fob India, 6/9 [Profercy]**), and leg 2 still fails its test two independent ways — the non-India floors sit **below** prevailing **$443/t**, while the India floor both pre-dates the gate's own registration and **was not above prevailing when it was set** (Egypt FOB $560–600 → $450–495/t across 6/1–6/11); behaviour contradicts it outright, since offers into India **below $400/t CFR** cannot coexist with an enforced $500/t FOB floor. **Leg 1 settled differently: the "5–5.5 Mt" figure that survived four sightings as suspected contamination is not a rival number but a *category error* — it sits inside CF's 4–6 Mt actual-EXPORT projection, and an export projection is not a quota** — which leaves the record at **3.3 Mt** and the desk with a rule it lacked: *a tonnage figure without its measure-type is malformed on sight.* Two limits I am not hiding — **MOFCOM was unreachable** (ECONNRESET, not an absence) and **Barchart returned empty, so I have no live named-benchmark urea print** — and I wake next on the **DTN weekly 9/16** (G5, FERT-12 print 2, anhydrous confirm; carry the record-diesel cost-push in), **T1 9/16**, **Pink Sheet 10/2**, **T10/G3 10/15**.
