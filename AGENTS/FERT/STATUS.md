# FERT — Status

**Domain:** Fertilizer supply/price/policy → food-CPI transmission → CF Industries positioning
**Class:** Market domain — EVENT-DRIVEN SPECIALIST (wakes on named triggers; no standing daily desk)
**Last real data refresh:** 2026-09-17 (**DTN 9/16 retail article — DAP $923 · MAP $962 data wk Sep 7-11, MIRROR via DAEDALUS stranger read**; live fetch.py CF price. *Prior refresh 2026-09-15 = Profercy · NDRC · CF Q2 commentary for T10/G3, still current.* The 9/2 Pink Sheet backbone, the 8/7 NOLA $/st vintage and the 9/9 six-of-eight DTN products are unchanged this spawn.)
**Session wall clock:** 2026-09-17 20:00 Thursday (boot.py)
**Situation Tier:** 🟡 MONITORING — **five prints of stall broken at the DTN retail end, one print in each direction of the compass**: MAP first non-flat print in 5 weeks (+$3 to $962), DAP re-accelerated to +$4 (approach rate now AT the +0.5%/mo the gate was base-rated on — a first). China floors still ratcheting DOWN. One-print observations only; no vector rescore.

> **Rebuild note.** The FROZEN 2026-03-20 STATUS is archived at `archive/STATUS_2026-03-20_FROZEN.md` — historical only. Every price cell below is benchmark + unit + date + source. **"Urea" alone is not a price.** Grading record: `PROME/research/2026-08-16_fert-revival-assessment.md`.

---

## Price Panel — benchmark-split (never one row called "urea")

| Benchmark (full name) | Unit | Level | As-of | Source authority |
|---|---|---|---|---|
| DTN retail urea, US national avg | **$/ton** | **$655** (**$0 w/w**, +4% YoY) — **9/9 vintage carried; 9/16 print UNREAD this spawn** | data wk Aug 31–Sep 4 2026 | MIRROR — DTN Progressive Farmer 9/9/26 |
| NOLA granular urea barge FOB | **$/st** | **$385–410** ⛔ **FROZEN 8/7 VINTAGE — 41 days; instrument unreachable, see below (L398)** | data **8/7/26** | MIRROR — Advanced Turf US Fert Mkt Summary 8/10/26 PDF |
| Urea FOB US Gulf futures (CBOT **JC**), Aug-26 | **$/st** | **$389.50** (−4.75) — carried 8/17 vintage | 8/17/26 | PRIMARY — CME via Barchart |
| Urea FOB US Gulf futures (CBOT JC), Sep-26 | $/st | $386.00 (−4.00) — carried 8/17 vintage | 8/17/26 | PRIMARY — CME via Barchart |
| Urea FOB Egypt futures (CBOT **JF**), Sep-26 | **$/mt** | **$442.50** (−2.50) — carried ~8/15 vintage | ~8/15/26 | PRIMARY — CME via Barchart |
| India CFR, **lowest BID** (RCF tender, opened 8/11) | **$/mt** | **$390.25** east / **$393.65** west (Ameropa) | bids 8/11/26, reported 8/14 | MIRROR — Rural Voice 8/14/26 |
| World Bank Pink Sheet urea, E. Europe prill spot FOB | **$/mt** | **$390.0** (Aug) ← $400.0 (Jul) ← **$856.9** (Apr) | monthly, Aug 2026 | PRIMARY — WB Pink Sheet, pub 9/2/26 |
| DTN retail **DAP**, US national avg | **$/ton** | **$923** (**+$4 w/w, +0.44%**, ~+7% YoY) | data wk **Sep 7–11 2026** | MIRROR — DTN 9/16/26 via DAEDALUS 9/17 stranger read (first-party FERT pull owed) |
| DTN retail **MAP**, US national avg | **$/ton** | **$962** (**+$3 w/w, +0.31%**, ~+5% YoY) — **first non-flat print in 5 weeks; binding leg on G5** | data wk **Sep 7–11 2026** | MIRROR — DTN 9/16/26 via DAEDALUS 9/17 stranger read |
| DTN retail **potash**, US national avg *(triage-depth row)* | **$/ton** | **$493** (+1% YoY) — **9/9 vintage carried; 9/16 print UNREAD this spawn** | data wk Aug 31–Sep 4 2026 | MIRROR — DTN 9/9/26 |
| DTN retail **anhydrous** | $/ton | **$938** (+$15 w/w, +1.63%, +22% YoY) — **9/9 vintage carried; 9/16 print UNREAD this spawn** | data wk Aug 31–Sep 4 2026 | MIRROR — DTN 9/9/26 |
| DTN retail UAN28 / UAN32 / 10-34-0 | $/ton | **$423** / **$455** / **$717** — **9/9 vintage carried; 9/16 prints UNREAD this spawn** | data wk Aug 31–Sep 4 2026 | MIRROR — DTN 9/9/26 |
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

**GATE-FERT-G5 — NOT FIRED (5 of 5 prints).** ✅ *Graded 9/17 on the 9/16 DTN print (data wk Sep 7–11 2026) via **MIRROR — DAEDALUS 2026-09-17 stranger read of the article** (gate-basis-sweep-1 packet): **MAP $962, DAP $923**. First-party FERT pull at dtnpf.com was attempted (WebFetch of the /2026/09/16 crops-article index and one direct slug guess) and did not yield the article body this L0 spawn — the publisher SPA is not fetchable this way; a first-party pull is owed at the next full FERT session before locking any downstream inference on the six unread products (urea/anhydrous/UAN28/UAN32/10-34-0/potash). `[[finding_asymmetric_rigor_counterparty_claims]]` observed.* Letter: *DTN retail **DAP OR MAP > $1,000/ton***; instrument = DTN Progressive Farmer weekly retail **$/ton**. ⛔ Never Pink Sheet $/mt, never NOLA $/st — different instruments hundreds of dollars apart and the gate does not name them.

**Print-by-print history + the approach-rate table → `workbook/GATE_GRADES.md`** (split 9/15, read-cap remedy — 9/16 print not yet appended there this spawn; carried in KB-FERT-039 + TRIGGERS T4).

**⚡ NEW read this spawn: the 5-week stall broke, in both legs and at the base-rated rate on DAP.** Six-print approach rate (8/12 → 9/16): MAP net +$3 = **+0.063%/wk ≈ +0.27%/mo** (still below the +0.5%/mo the gate was base-rated on — first non-flat MAP in 5 wks); DAP net +$6 = **+0.13%/wk ≈ +0.52%/mo** (**now AT the base rate — a first**, up from +0.22%/mo through 9/9). Distance-to-line: MAP +3.95% ($38 short), DAP +8.34% ($77 short). **One print does not re-score a vector** (blueprint) — direction change flagged, not scored. If DAP holds ≥+0.5%/mo for one more print, the vector-2 momentum call has to be re-read; if MAP joins on a second consecutive up-print, FERT-12's HOLDING call weakens materially (still ~11 weeks of headroom at this rate).

⛔ **Headline-composition trap from 9/9 stays live and unrefuted this spawn** — the 9/16 headline text and full-panel week-over-week composition are UNREAD (six of eight product prints unpulled by this desk). Do not restate the 9/9 finding under the 9/16 date. `[[finding_headline_keyed_conditional_inherits_its_composition]]`

📌 **Prediction FERT-12 — print 2 of ~11, HOLDING.** MAP $962 ≤ $975 test level ($13 of headroom, was $16 last week); +$3 movement w/w is the first non-flat print, at ~half the +0.5%/mo trajectory the level was calibrated on. Resolve_By 2026-12-02, status stays **OPEN**.

⚠️ **DAEDALUS gate-basis-sweep-1 ASK on this gate — LOGGED, dispositioned to PROME.** OPERATOR-MISMATCH inside the letter: registered base rate is Pink Sheet DAP $/mt monthly, letter fires on DTN retail $/ton weekly. **Grade unaffected; letter needs recomputation on DTN retail (or CONTEXT relabel) + geography + $1,000 tie convention, by 9/30.** Deferred to next full FERT session (not L0 drain scope; Will-gated surface). Packet: `outbox/2026-09-17_from-FERT_L310-G5-9-16-grade-plus-DAEDALUS-ASK-disposition.md`.

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
| 2 | **Phosphate tight leg** | DAP **$923** / MAP **$962** retail [wk Sep 7–11, DTN 9/16 MIRROR via DAEDALUS 9/17]. **6 prints:** MAP 959/960/959/959/959/**962**, DAP 917/917/916/918/919/**923**. Net over 35 days: **MAP +$3 (+0.31%), DAP +$6 (+0.65%)** — first non-flat MAP in 5 wks, DAP re-accelerated. Root still flat: rock $170.0/mt [Aug] = $170.0 [Jul]. Pink Sheet DAP $793.5/mt [Aug], +1.6% | 🟠 ELEVATED *(level)* — **retail momentum re-emerging one print into wk 6, root still flat** | **3** | Med — four phosphate benchmarks, four directions in August; the retail leg just diverged from the flat root | T4 weekly · T11 monthly |
| 3 | Hormuz transit | Effectively closed; ~1 transit 8/9 vs ~73/day normal [Lloyd's List 8/12]. Alternative routing (Red Sea/Suez) in use where feasible [ATS 8/10] | 🔴 but **priced** | 3 | Med (BRENT/HAWK own the theater) | via OSPREY/FALCON |
| 4 | Nitrogen price level | Round-tripped internationally (Pink Sheet **$856.9/mt Apr → $390.0 Aug, −54.5%**). ⚠️ **NEW 9/9 — the retail bleed STOPPED and partly reversed:** DTN urea **$655 flat w/w** (first flat print after 3 weeks of declines from $678) and **anhydrous $923 → $938, +$15 / +1.63% w/w**, the largest single move in the panel and **upward**. UAN28 −$5 and UAN32 −$3 still falling, so the reversal is **not** uniform across the nitrogen complex. Anhydrous is **+22% YoY**, the highest YoY of the eight. **One print — a stall, not a trend** | 🟢 NORMALISED *(level)* — **but the downward pass-through has stopped; watch for a second print** | 1 | High | T4 weekly · T5 **BLOCKED** |
| 5 | India import demand | RCF 1.7 Mt tender bids opened 8/11; **lowest bids $390.25/$393.65 CFR** — vs $935/$959 awarded April. Demand intact, **price collapsed** | 🟡 | 2 | High | T1 |
| 6 | Food-CPI transmission | July food-at-home **−0.07% m/m / +2.7% y/y** [BLS via FRED CUSR0000SAF11]. ERS forecasts FAH 2.7% (2026) / 2.9% (2027) — **fertilizer not a cited driver** | 🟢 NOT FIRING | 1 | High | T2/T3 |
| 7 | Qatar LNG → fertilizer capacity | **12.8 mtpa** (Trains 4 & 6, Ras Laffan) = **~17%** of Qatar export capacity; missile strikes 3/18–19/26; 3–5 yr repair CONFIRMED. **No primary links this damage to ammonia/urea output** — inference deleted, not carried | 🟡 | 2 | Low (single event, unlinked to N) | on QAFCO/Mesaieed disclosure |
| 8 | European production economics | Gas ~$16.00/MMBtu → theoretical ammonia ~$667/mt FOB, **above prevailing urea FOB = economically shut**. Physical closure count **PAYWALLED**, unresolved since March | 🟡 UNRESOLVED | 2 | Low (proxy only) | on BRENT gas signal |

**Convergence: 16/40** — HELD across 9/9 and 9/17. Vector 2 stays at **3**: the 9/16 print puts the first non-flat DAP+MAP week on the board and takes DAP's approach rate to the +0.5%/mo the gate was base-rated on — but a *one-print* re-acceleration is symmetric with the *one-print* reversal 9/9 noted for anhydrous (still unmeasured this spawn), and neither moves a score. Vector 4's anhydrous reversal from 9/9 was not confirmed or refuted by the 9/16 data available today (DAEDALUS's stranger read named only DAP+MAP; the other six DTN products remain UNREAD by this desk this spawn). Vector 1 unchanged since 9/15 T10 grade. Was 17/40 before the 9/2 cut of vector 2 from 4→3. **No vector at 5.**

---

## What Changed This Session (2026-09-17 — T4 wake, WQ-184 L0 due-row Tier-1 spawn one day after G5 consumer date lapsed; DOCKET L310 / GATES review_by re-dated 9/17 L408 → 2026-09-23)

**The graded read is in §Registered Gates; the memo + DAEDALUS ASK disposition is `outbox/2026-09-17_from-FERT_L310-G5-9-16-grade-plus-DAEDALUS-ASK-disposition.md`. Neither is restated here.** What this L0 drain actually changed:

1. **G5 graded NOT FIRED, 5th consecutive on the 9/16 DTN print.** MAP $962 / DAP $923; MAP binding leg, +3.95% short. MIRROR authority — DAEDALUS stranger read; first-party FERT pull owed at next full session. `KB-FERT-039`
2. **The 5-week retail-phosphate stall broke.** MAP first non-flat in 5 wks (+$3); DAP re-accelerated to +0.52%/mo — now AT the +0.5%/mo the gate was base-rated on, first time. Direction change flagged, NOT scored (one print never moves a vector).
3. **FERT-12 print 2 HOLDING.** MAP $962 ≤ $975 test level, $13 headroom (was $16). Row STAYS OPEN.
4. **DAEDALUS ASK on G5 LOGGED and dispositioned to PROME** — OPERATOR-MISMATCH in registered base rate, letter recomputation deferred to next full FERT session, 9/30 deadline as DAEDALUS set. Grade today is unaffected.
5. **L398 unchanged:** Advanced Turf PDF instrument dark 41 days. Recommendation to PROME (outbox memo): **freeze NOLA $/st panel + mark T5 RETIRED-PENDING-REPLACEMENT**; investigate alternates (Argus, Fertilizer Daily, Green Markets, Fertilizer Week) at next full session.
6. **Six of eight DTN 9/16 product prints UNREAD by this desk** (urea/anhydrous/UAN28/UAN32/10-34-0/potash) — DAEDALUS back-solve reported only DAP+MAP. 9/9 vintages carried under explicit "9/16 UNREAD" cell labels. Anhydrous reversal from 9/9 is neither confirmed nor refuted today.
7. **Five due triggers deliberately not worked and NOT re-dated** (T1/T3/T5/T8/T12) — only T4 moved (→9/23). Session-9/15 principle: a re-dated row you didn't work is a false all-clear.
8. **⛔ WQ-140 in-session correction, count 1/2:** KB-FERT-039 first draft carried a fabricated anhydrous $953/+$15 figure (my inference, not DAEDALUS's read); caught pre-commit, corrected in-row. Second edit to KB.tsv this session would trip the two-correction stop.

---

## What Changed — prior sessions

**2026-09-15** → **T10 wake / G3 re-read** (previous session). Carry-forward: **GATE-FERT-G3 NOT FIRED both legs, 5th consecutive** — China floors ratcheting DOWN all year ($680 → $500/t fob India, $660/$670 → $430/$440 elsewhere); the *"5–5.5 Mt"* figure resolved as a **category error** inside CF's 4–6 Mt EXPORT projection; standing quota record holds **3.3 Mt**. MOFCOM ECONNRESET; Barchart empty. Rule earned: *a tonnage figure without its measure-type is malformed on sight.* Full working → `outbox/2026-09-15_from-FERT_G3-china-quota-floor-re-read-DOCKET-L204.md`.
**2026-09-09** → `archive/STATUS_whatchanged_2026-09-09_ROTATED.md`. Carry-forward: **G5 NOT FIRED 4-of-4; the approach RATE — MAP 0.00%/mo, DAP +0.22%/mo vs +0.50%/mo base-rated — was the finding, not the level**; the Advanced Turf NOLA instrument went dark after 8/10. *This week both approach-rate numbers moved.*
**2026-09-05** → `archive/STATUS_whatchanged_2026-09-05_ROTATED.md`. Carry-forward: **the third consecutive Pink Sheet phosphate-rock rise did NOT occur** — rock printed **$170.0/mt Aug, flat vs July**.

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
- **Phosphate channel — LIVE, direction of retail leg just changed one print.** Kill needs **BOTH**: Pink Sheet rock ≤ **$152.5/mt** ×2 consecutive editions **AND** DTN retail MAP < **$900/ton** ×2 consecutive articles. **Neither met, neither close:** rock **$170.0/mt [Aug]** = **11.5% above** the leg, moved **0.0%** toward it; MAP **$962 [wk Sep 7–11]** = **6.9% above** its leg, moved **+$3 in the past week** (first non-flat print in 5 wks). ⚠️ **The rail tests for reversal; what happened five weeks in a row was a stall, and the sixth week is one print of the opposite move.** The honest state is **level held, momentum re-emerged one print into the cost side**. Next root read T11 **10/02**, graded against **FERT-11**; next retail read T4 **9/23** (also FERT-12 print 3).
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

**GATE-FERT-G5 is NOT FIRED for the fifth consecutive DTN print, but the finding this week is that the 5-week stall broke in both directions of the compass in one print — MAP $959 → $962 (+$3, first non-flat move in 5 weeks) and DAP $919 → $923 (+$4, taking DAP's approach rate to +0.52%/mo, the +0.5%/mo the gate was originally base-rated on and the first print at that rate).** The verdict rests on a **MIRROR** — DAEDALUS's 2026-09-17 stranger read of the DTN 9/16 article, since the publisher SPA did not yield the article body via WebFetch this spawn and only DAP + MAP were reported by DAEDALUS's back-solve, so **six of eight product prints for this data week remain UNREAD by this desk** (urea, anhydrous, UAN28, UAN32, 10-34-0, potash — the 9/9 vintages are carried under an explicit "9/16 print UNREAD" label on every cell, not silently). **One print does not re-score a vector** and I am explicitly not re-scoring V2 — but the direction change is the read, and if MAP prints up a second time on 9/23 the phosphate leg's convergence-2 score revisits, as does FERT-12's headroom (still $13). **DAEDALUS caught a real OPERATOR-MISMATCH inside the G5 letter** — its registered 93rd-pct base rate is on Pink Sheet DAP $/mt monthly, not on DTN retail $/ton weekly which is the letter's actual fire condition; the *grade* is unaffected, the *letter* needs recomputation on DTN retail (or a CONTEXT relabel) by 9/30, and the letter is a Will-gated surface so this is dispositioned to PROME rather than edited unilaterally, deferred to my next full session as out-of-scope for a L0 drain. **L398 (Advanced Turf PDF dead 41 days)** is unchanged this spawn — recommended state: freeze the NOLA $/st panel with a permanent banner, mark T5 RETIRED-PENDING-REPLACEMENT, investigate alternates (Argus, Fertilizer Daily, Green Markets, Fertilizer Week) at the next full session; two watches down on one dependency, both blocked, both explicitly documented. **T3 (Aug CPI), T1 (RCF award), T8 (NASS harvest), T12 (phosphate margin inputs, rides dead T5) — deliberately not worked and not re-dated this L0 drain** (session-9/15 principle: a re-dated row you didn't work is a false all-clear). Next wakes: **T4 9/23** (G5 print 6 + FERT-12 print 3 + first chance to confirm/refute today's momentum change + a chance to log the six unread products), **Pink Sheet T11 10/2** (FERT-11 resolves ≤ one week later), **T10/G3 10/15**.
