# FERT — Status

**Domain:** Fertilizer supply/price/policy → food-CPI transmission → CF Industries positioning
**Class:** Market domain — EVENT-DRIVEN SPECIALIST (wakes on named triggers; no standing daily desk)
**Last real data refresh:** 2026-11-11 (T4 + T1 wake: DTN 11/11 first-party, IPL tender page primary, AFC w/e 06.11; KB-FERT-139..141). Prior: 2026-11-10 (D:L761 grade: NASS November Crop Production primary, BLS October CPI release + Table 2; KB-FERT-137..138). Prior: 2026-11-05 (D:L578 wake: CF Q3 8-K + call transcript, Mosaic Q3 8-K + call transcript, DTN 11/04 first-party, Pink Sheet November edition, AFC w/e 30.10, Green Markets 10/30, MOFCOM TRQ primary; KB-FERT-113..136). Prior: 2026-11-02 (rock plateau count). **Last price refresh:** 2026-11-11 (DTN 11/11, KB-FERT-141). Build baselines stay at their 10/26 vintages; DATA_ROUTES.md.
**Session wall clock:** 2026-11-11 08:38 Wednesday (boot.py; PROME prome-2b due-row wake G:GATE-FERT-G5 + T1, WQ-184). Runtime Claude Code, Opus 5.5. Inbox: empty at boot, nothing to drain. Prior session: 2026-11-10 13:13 Tuesday (D:L761 grade, closed 19:33 ET).
**Situation Tier:** 🟡 MONITORING — **retail MAP $991 / DAP $950 [DTN 11/11, wk Nov 2–6]**, ninth straight MAP rise, DAP +$9; G5 NOT FIRED 13-of-13, **$9** short. Q4 Tampa sulfur **$615/lt** (−$90, two sources), but Mosaic books **$800–850/ton** through Q4 costs and calls Q4 the trough. CF raised its China read: exports 2–4 Mt above 2025, authorizations "almost nine million tons". Nitrogen channel dead at urea; **ammonia is the firm leg** (Tampa November +$95, retail anhydrous $1,003). **Food at home +0.4% (Oct, BLS SA)**, first month at the +0.4 line since April, led by beef and snacks, cereals and bakery flat. NASS corn yield **179.6** (−1.6), no fertilizer attribution.

---

## Price Panel — benchmark-split (never one row called "urea")

| Benchmark (full name) | Unit | Level | As-of | Source authority |
|---|---|---|---|---|
| DTN retail urea, US national avg | **$/ton** | **$662** (−$7 w/w; +11% YoY) | data wk Nov 2–6 2026 | PRIMARY-publisher — DTN 11/11/26, pulled first-party 11/11 |
| NOLA granular urea barge FOB | **$/st** | **$432–438** [Green Markets 10/30 headline] · CF Frost "$430 for Q4 for a short" NOLA [call 11/05, MIRROR]. Intermittent headline levels, not a weekly series. ⚠️ AFC "November barge ~$475 PMT" is AFC's own basis, **not** this $/st FOB benchmark. 🧊 Advanced Turf $385–410 = FROZEN 8/7 vintage | wk to 10/30/26 | PRIMARY headline — Green Markets `KB-FERT-125` |
| India CFR, **lowest OFFER per coast** (IPL 1.7 Mt tender, closed 10/07) | **$/mt CFR** (basis STATED by AFC 10/12) | **$352.10 east / $356.25 west**; IPL countered at these L1s [secondary 10/14]. **~410,000 t secured, awarded CFR NOT STATED** — INFERRED ≤ the counters (`KB-FERT-080`). **No new tender as of 11/11** (IPL tender page, primary); AFC w/e 06.11: India delayed, possibly several weeks (`KB-FERT-139`) | offers 10/07/26 · counters 10/14 | MIRROR — AFC weekly + Bloomberg via Business Standard (`KB-FERT-067`) |
| World Bank Pink Sheet urea, **prill spot FOB Middle East** (series name "Urea, E. Europe"; WB definition since Mar-2022) | **$/mt** | **$420.0** (Oct) ← $407.5 (Sep) ← $390.0 (Aug) ← **$856.9** (Apr) | monthly, Oct 2026 | PRIMARY — WB Pink Sheet dated 11/03/26, read 11/05 |
| Urea FOB **Middle East** (AFC weekly; granular) | **$/mt** | **~$440** · Egypt **~$535** FOB | w/e 10/30/26 | MIRROR — AFC weekly pub 11/02 `KB-FERT-125` |
| Urea **CFR Brazil** non-Chinese (AFC) · Chinese · China **prilled** FOB netback | **$/mt** | Brazil non-Chinese **$480–485** CFR · Chinese **$470–475** CFR · China prilled **$345–350** FOB netback | w/e 10/30/26 | MIRROR — AFC weekly pub 11/02 `KB-FERT-125` |
| India **DAP** CFR · Brazil **MAP** CFR (AFC weekly) | **$/mt** | India DAP **$890–900** · Brazil MAP **$830–850** | w/e 10/30/26 | MIRROR — AFC weekly pub 11/02 `KB-FERT-125` |
| DTN retail **DAP**, US national avg | **$/ton** | **$950** (**+$9 w/w**; +3% YoY) | data wk **Nov 2–6 2026** | PRIMARY-publisher — DTN 11/11/26, pulled first-party 11/11 |
| DTN retail **MAP**, US national avg | **$/ton** | **$991** (**+$4 w/w, +0.41%**; +7% YoY) — **binding leg on G5** | data wk **Nov 2–6 2026** | PRIMARY-publisher — DTN 11/11/26, pulled first-party 11/11 |
| DTN retail **potash**, US national avg *(triage-depth row)* | **$/ton** | **$504** (+3% YoY) | data wk Nov 2–6 2026 | PRIMARY-publisher — DTN 11/11/26 |
| DTN retail **anhydrous** | $/ton | **$1,003** (**−$4 w/w**; +17% YoY) | data wk Nov 2–6 2026 | PRIMARY-publisher — DTN 11/11/26 |
| DTN retail UAN28 / UAN32 / 10-34-0 | $/ton | **$428** / **$484** / **$704** (−$18 / −$10 / −$4 w/w) | data wk Nov 2–6 2026 | PRIMARY-publisher — DTN 11/11/26 |
| NOLA **DAP** / **MAP** barge FOB | $/st | 🧊 FROZEN 8/7 vintage, no free successor → `archive/STATUS_whatchanged_2026-11-11_ROTATED.md` | 8/7/26 | MIRROR — Advanced Turf 8/10/26 |
| Pink Sheet **DAP**, spot FOB US Gulf | $/mt | **$803.1** (Oct) ← $800.6 (Sep), **+0.3%** | Oct 2026 | PRIMARY — WB Pink Sheet 11/03/26 |
| Pink Sheet **TSP**, spot import US Gulf | $/mt | **$692.0** (Oct) ← $690.0 (Sep), **+0.3%** | Oct 2026 | PRIMARY — WB Pink Sheet 11/03/26 |
| Pink Sheet **phosphate rock**, FOB North Africa | $/mt | **$170.0** (Oct) = Sep = Aug = Jul ← $156.9 (Jun) ← $152.5 flat 30 mo (Dec-23–May-26, `KB-FERT-110`) | Oct 2026 | PRIMARY — WB Pink Sheet 11/03/26 |
| **Tampa molten sulfur**, quarterly contract, delivered *(phosphate cost input — `VX-FERT-09`, watch-only, unbanded)* | **$/long ton** | **$615** (Q4, −$90) ← $705 (Q3, record). ⚠️ Contract, not realized cost: Mosaic guides Q4 realized **$800–850/ton** [call, MIRROR] | Q4 2026 | two-sourced — Green Markets 10/30 + Mosaic 8-K 11/03 (`KB-FERT-123`) |
| Pink Sheet **potassium chloride**, granular spot **CFR Brazil** *(triage-depth row)* | $/mt | **$357.5** (Oct) | Oct 2026 | PRIMARY — WB Pink Sheet 11/03/26 |
| **Tampa ammonia**, monthly contract | $/mt CFR | **~$640** (Nov, +$95) — Green Markets $640; AFC $645, $5 open | Nov 2026 | secondary headlines, no settlement document read (`KB-FERT-124`) |

⚠️ **Cross-benchmark spreads are real, not error.** DTN retail urea **$662/ton** [wk Nov 2–6] vs NOLA barge **$432–438/st** [10/30 headline] vs Pink Sheet Middle East prill FOB **$420.0/mt** [Oct] — same nutrient, three instruments, **~$225–245 apart**. The March desk's registered gate died on exactly this. **DTN retail lags international by weeks** — international series are the leading edge for transmission timing.

---

## Registered Gates (both watch-only; no capital path)

**GATE-FERT-G5 — NOT FIRED (13 of 13 graded prints).** ✅ *Graded 2026-11-11 09:31 ET on the 11/11 DTN print (data wk Nov 2–6), **first-party**: curl of the dtnpf.com article (datePublished 2026-11-11T13:44Z, posted late): **MAP $991, DAP $950**. `KB-FERT-141`. Graded on review_by.* Letter (home = `workbook/TRIGGERS.tsv` **T4**): *DTN retail **DAP OR MAP > $1,000/ton***; instrument = DTN Progressive Farmer weekly retail **$/ton**, US national average as printed, strictly greater at whole-dollar precision (WQ-351 terms). ⛔ Never Pink Sheet $/mt, never NOLA $/st. **Next review_by 2026-11-18** (proposed: next DTN Wednesday; PROME records it). Print history + rate tables → `workbook/GATE_GRADES.md`.

**⚡ Read this wake:** MAP **+$4** (ninth straight rise), DAP **+$9** (largest DAP step in 14 prints). Distance: MAP **$9 (+0.91%)**, DAP $50. A fire needs $1,001, +$10. First firing print ≈ **12/16** at the mean step (+$2.46/wk), **12/02** at the last two steps (+$4/wk), **11/25** at the fastest step seen (+$5). ⚠️ Against: AFC w/e 06.11 says phosphate demand is weakening and buyers are turning to TSP; Q4 sulfur −$90. For: retail still rising nine prints running; Mosaic sold out Q4. **FERT-13 (55%, unchanged)** forecasts this crossing by 12/31.

**GATE-FERT-G3 — NOT FIRED (both legs; 7th re-read, 2026-11-05, on the consumer date; next re-read proposed 12/03).** Letter: *China 2026 urea export quota revised **DOWN**, OR a guidance floor reimposed **ABOVE prevailing intl FOB***. **Leg 1:** no downward revision found; CF: exports 2–4 Mt above 2025 [8-K 11/04], authorizations "almost nine million tons" [call 11/05, MIRROR]. ✅ "3.3 Mt" = China's urea **IMPORT** quota (`KB-FERT-117`); leg 1 has no published national referent. **Leg 2:** no floor reimposition found; China prilled $345–350/mt FOB netback [AFC w/e 30.10]. ⚠️ Absence rests on free sources. Chinese ammonium sulfate restriction reported on CF's call is another product, no leg (`KB-FERT-128`). Full working → `workbook/GATE_GRADES.md` § G3.

---

## Live Vectors

| # | Vector | Live read (dated) | State | Score /5 | Independence | Next re-read |
|---|---|---|---|---|---|---|
| 1 | **China export regime** | **CF 8-K 11/04:** exports 2–4 Mt above 2025, about 6.9–8.9 Mt on CF's own base (FERT arithmetic). **Call 11/05, MIRROR:** authorizations "almost nine million tons"; Bohn doubts all ships in 2026. Prior CF 4–6 Mt. ⚠️ Chinese trade tally 9/28: allowance 5–6 Mt; gap unresolved (`KB-FERT-116`). Jan–Sep about 3.88 Mt, two relays added (`KB-FERT-127`). Floors **not binding** on prilled: $340–350/mt FOB [AFC w/e 06.11, re-read 11/11]. New: ammonium sulfate restriction reported, sulfur-linked (`KB-FERT-128`). Fire path (AFC 10/12, conditional): a domestic urea price rise "could prompt renewed intervention" | 🟢→🟡 supply RETURNED and **larger than CF thought** | **1** — card rule met, 2 → 1 (C1 raised above 6 Mt) | High (policy + market reads) | **every wake** (T10 → 12/03) |
| 2 | **Phosphate tight leg** | DAP **$950** / MAP **$991** retail [wk Nov 2–6, DTN 11/11 first-party]. **14 prints:** MAP 959/960/959/959/959/962/967/970/974/979/981/983/987/**991**, DAP 917/917/916/918/919/923/925/926/934/934/937/939/941/**950**. Net over 91 days: **MAP +$32 (+3.34%), DAP +$33 (+3.60%)**. **Root:** rock **$170.0/mt** flat four months; Pink Sheet Gulf DAP **$803.1/mt**; Q4 Tampa sulfur **$615/lt** (−$90). **Mosaic Q3 (8-K 11/03):** production 1,289 kt vs 1,433 kt Q2; Q4 sales guide 1.3–1.6 Mt, no production guide; DAP $838/tonne FOB plant; curtailing the **South Fort Meade and Miski Mayo mines**. **Call, MIRROR:** Q4 realized sulfur $800–850/ton, phosphate EBITDA trough; Q4 sold out; Florida operating rate low- to mid-60%; global shipments down ~20 Mt. **Counter:** AFC w/e 30.10 and 06.11: buyers resisting, demand weakening, TSP substitution | 🟠 ELEVATED *(level)* — **retail still rising; curtailment now issuer-stated; sulfur relief reaches earnings Q1 2027** | **3** — **HELD** by card: $615 is neither ≥$705 nor ≤$605, no production guide, no restart | Med | T11 **12/02** · T4 **11/18** · T12 **12/31** |
| 3 | Hormuz transit | Still effectively closed: **4 of 88** total transits, 2 tankers Oct 18 [PortWatch via FALCON STATUS 10/26, `KB-FERT-106`] — FALCON owns the count; no verified permanent corridor. UN fertilizer corridor **not activated** (none found 10/28; 10/14 conditional detail → archive 11/11, `KB-FERT-076`). ~600,000 mt urea reportedly awaiting passage [AFC 9/18] | 🔴 but **priced** | 3 | Med (BRENT/HAWK own the theater) | via OSPREY/FALCON |
| 4 | Nitrogen price level | Pink Sheet urea (prill FOB Middle East) **$856.9/mt Apr → $390.0 Aug → $420.0 Oct**. Retail urea **$662** (−$7), anhydrous **$1,003** (−$4), UAN32 $484 (−$10), UAN28 $428 (−$18) [DTN 11/11]. **Ammonia is the firm leg:** Tampa November ~$640/mt CFR, +$95; NW Europe $710–730/mt CFR [AFC w/e 30.10]. Urea "under pressure" until India [AFC]; CF: market "in pause", about 10% above last year, positive into H1 2027; Middle East urea exports about half normal (issuer estimate, `KB-FERT-120`). CF realized $/short ton Q3 vs Q2: ammonia $532/$677, urea $423/$593, UAN $322/$441 | 🟢 NORMALISED *(urea level)* — ammonia firmer, urea waiting on India | 1 | High | T11 **12/02** · T4 **11/18** |
| 5 | India import demand | **IPL 1.7 Mt tender**: lowest offers **$352.10/mt CFR East** / **$356.25/mt CFR West** [AFC 10/12]; IPL countered at these L1s [secondary 10/14]. ⛔ A counter is a bid, not an award. **Outcome:** ~410,000 t of 1.7 Mt; Chinese suppliers declined ~$320–325/mt FOB netbacks [AFC w/e 16.10, single MIRROR]; **awarded CFR NOT STATED** (`KB-FERT-080`). **Next:** not issued as of 11/11 (IPL tender page, PRIMARY); AFC w/e 06.11: delayed, possibly several weeks; China prilled $340–350/mt FOB, high Chinese inventories (`KB-FERT-139`; the 10/30 ~2.5 Mt / $370–375 expectation is SUPERSEDED). CF: imports over 10 Mt in 2026. Re-open line = **G2 = AWARDED CFR > $600/mt** (`EXIT_PROTOCOL.md` §1A) | 🟢 *(level; ~41% below the $600 RED edge)* | 2 — HELD: no stated award price | High | T1 **11/18** |
| 6 | Food-CPI transmission | **October** food at home **+0.4% m/m SA** as BLS published (index-derived **+0.443%**, 322.535 vs 321.111); **12-month NOT PUBLISHED** (Oct 2025 not collected) [BLS release + Table 2 via WebFetch, PRIMARY; index FRED MIRROR, `KB-FERT-138`]. Groups: beef +0.9, snacks +1.0, dairy +0.6, produce +0.6, **cereals and bakery 0.0**, beverages −0.3. Run: Jun +0.19 · Jul −0.07 · Aug +0.04 · Sep −0.07 · **Oct +0.44**; earlier 2026 at the line: Feb +0.44, Apr +0.68. ERS **10/23**: FAH annual-average forecasts **2.3% (2026) / 1.0% (2027)**, down from September 2.4% / 1.8%; fertilizer not cited (`KB-FERT-083`) | 🟠 ORANGE on its own band (0.4–0.6 ×1, `VX-FERT-06`) — composition not grain-led, fertilizer causation NOT ESTABLISHED | **2** — 1 → 2 per the frozen card; ⚠️ composition disagrees (cereals flat) | High | T2 **11/24 VERIFIED** · T3 Nov CPI **12/10** |
| 7 | Qatar LNG → fertilizer capacity | **12.8 mtpa** (Trains 4 & 6, Ras Laffan) = **~17%** of Qatar export capacity; missile strikes 3/18–19/26; 3–5 yr repair CONFIRMED. **No primary links this damage to ammonia/urea output** — inference deleted, not carried | 🟡 | 2 | Low (single event, unlinked to N) | on QAFCO/Mesaieed disclosure |
| 8 | European production economics | **CF 8-K 11/04:** an estimated **37%** of Europe's nameplate ammonia capacity "reportedly" offline or reduced in October; about 35% of Trinidad ammonia permanently shutting. **Call, MIRROR:** "our estimates of 35%"; Bohn: closures 12–18 months sooner. AFC w/e 30.10: about one-third, TTF forward reportedly above €100/MWh. Yara 10/22: own run rate 270,000 t, consultants 25–28% (`KB-FERT-104`). ⚠️ 37% vs 270,000 t **is not a comparison**: share of industry nameplate including part-load units vs one producer's tonnes. CF sells into this tightness (`KB-FERT-119`). FERT's own margin calc stays withdrawn (`KB-FERT-090`) | 🟡 → curtailment EVIDENCED, wider read | 2 — HELD by card: level clears 25%, "own data" not established; deck source unread | Med | on BRENT gas signal · CF deck if reachable |

**Convergence: 16/40** — V6 1 → 2 on 11/10 under the frozen NASS-CPI card (October food at home at +0.4%); all other vectors held. Prior 15/40 from 11/05 (V1 2 → 1). No vector at 5.

---

## Current Work — 2026-11-11

- **11/11, G:GATE-FERT-G5 + T1 wake (PROME prome-2b, WQ-184):** DTN 11/11 graded first-party, MAP $991 / DAP $950, **G5 NOT FIRED 13 of 13**, $9 short (KB-FERT-141); India: no new tender (IPL page primary), AFC says delayed (KB-FERT-139). Potash triage cells logged (KB-FERT-140). Rotated TRIGGERS and STATUS under 70% of budget (`archive/*_2026-11-11*`). No trade, card, gate, band or threshold changed.
- **⏭ NEXT:** **Sun 11/15** — TRADE.md re-look + EXIT_PROTOCOL re-derivation (D:L579); clean the stale September-values block near EXIT_PROTOCOL lines 90–97, which contradicts the file's own banner. **Wed 11/18** — DTN print (G5, T4; MAP $9 short) + India tender check (T1). **Tue 11/24** — ERS (T2). **Thu 12/10** — November CPI (T3).

Prior notes: 11/05–11/10 entries → `archive/STATUS_whatchanged_2026-11-11_ROTATED.md`; 10/28 session → `reports/2026-10-28_wake.md`; older → `archive/STATUS_whatchanged_*_ROTATED.md`.

---

## Open Predictions (the live loop — 5 OPEN, 12 resolved)

**OPEN:** **FERT-13** 55%, MAP > $1,000 by 12/31 · **FERT-14** 58%, Pink Sheet urea November > $420.0/mt, resolve 12/15 · **FERT-15** 42%, next India tender L1 > $375/mt CFR on either coast, resolve 1/08, VOID if no bids by 12/31 · **FERT-16** 40%, DTN anhydrous > $1,050/ton by 12/31 · **FERT-17** 40%, China calendar-2026 urea exports ≥ 7.0 Mt, resolve 2/15/27. ❌ FERT-12 MISS 10/14 · ✅ FERT-11 HIT 10/07. Calibration → `workbook/PREDICTIONS_SCOREBOARD.md` (n=2 resolved, mean Brier 0.343). ⚠️ **FERT-05** (March charter) is a provisional MISS with its window open to 12/31: final grade after the December CPI (mid-Jan 2027); the boot scan cannot see it. *Letters, grading bases and post-mortems live in `workbook/PREDICTIONS.tsv`.*

---

## Exit Rules / Kill Rail

**Kill rail re-derived: 2026-08-17.** Durable rules + bidirectional flip test: **`workbook/EXIT_PROTOCOL.md`**. STATUS carries only the **live distance to each leg**:

- **Nitrogen channel — DEAD** (channel-kill, not thesis-kill; killed by China's quota resumption, not demand). Migration path: phosphate leg + CF single-name. Re-open test (awarded India CFR above G2, or 2 consecutive NOLA prints above G1) **not met**: the NOLA leg is **ungradeable week to week** while T5 is retired, so the channel can re-open only via an **India AWARD > $600/mt CFR (G2)**. Last tender: any award books at or below the counters, **~41% below $600** (INFERRED; detail in V5); no follow-on tender as of 11/11; AFC w/e 06.11 says delayed, possibly weeks (`KB-FERT-139`); T1 → 11/18.
- **Phosphate channel — LIVE.** Kill needs **BOTH**: Pink Sheet rock ≤ **$152.5/mt** ×2 consecutive editions **AND** DTN retail MAP < **$900/ton** ×2 consecutive articles. **Neither met, neither close:** rock **$170.0/mt [Oct]** = 11.5% above its leg (flat four editions); MAP **$991 [wk Nov 2–6]** = 10.1% above its leg and moving away (ninth up-print). ⚠️ The rail tests for reversal; what is happening is the opposite at the retail end and a stall at the root. Next root read T11 **12/02**; next retail read T4 **11/18**.
- **Transmission question — OPEN, not a carried prediction.** Dies if BLS food-at-home m/m prints **<+0.4% in each of Nov, Dec 2026 and Jan 2027** (releases 12/10, 1/13/27, 2/11/27) with no upward ERS revision citing inputs (WQ-665 B + WQ-666 A, Will 11/10). **Live distance:** Oct **+0.4%** BLS SA (+0.443% index) — **at the line**, first time since April; cereals and bakery 0.0, so not grain-led. A window month at +0.4% or more keeps it OPEN and FERT brings Will a fresh window; no automatic roll. ERS **10/23** 2027 forecast 1.0%, no inputs cited. Next: ERS **11/24 VERIFIED**, CPI **12/10 · 1/13/27 · 2/11/27** (BLS verified; D:L1102/L1105/L1106).
- **Timing vs mechanism:** the March *timing* claim is graded **MISS**; the mechanism is **not** refuted — it is **un-instrumented**, and re-opening it needs a fresh input shock.

---

## Named Blind Spots (exclusions register — I do not cover these)

Canonical register → `CLAUDE.md` §Exclusions. Live state only:

| Excluded | Owner | On sighting |
|---|---|---|
| **Potash supply shock** | ⚠️ **FERT owns it at TRIAGE DEPTH ONLY** (Will-ruled 2026-08-18) | KB row + PROME flag. **No deep-dive, no comparison, no trend adjective.** *Live triage cells: DTN retail potash **$504/ton** [wk Nov 2–6, DTN 11/11]; AFC w/e 06.11: Brazil granular MOP **$350–375/mt CFR**, SE Asia standard MOP **$370–415/mt CFR**, SE Asia granular MOP **$425–435/mt CFR** (`KB-FERT-140`); NOLA potash **$340–350/st FOB** [Green Markets 10/30 teaser]; Mosaic call 11/04: logistics disrupted roughly 1.5 Mt of Baltic potash shipments in Q4 (`KB-FERT-129`); Pink Sheet potassium chloride, granular spot CFR Brazil **$357.5/mt** [Oct] `KB-FERT-114`. Older potash reads (Uralkali, Belarus/Klaipėda, Canpotex) → `archive/STATUS_whatchanged_2026-11-11_ROTATED.md`; `KB-FERT-087/111/046/070`.* ✅ CBP's §338 Canada enumeration carries **zero Chapter 31 lines** (`KB-FERT-030`). ⛔ **US §338 only**; Canada's 9/8 counter-tariff list is a separate, still-unread instrument |
| Clean-ammonia / ammonia-as-fuel demand | NO OWNER | KB row + PROME flag. Sighting 11/05: CF low-carbon premium a little over $20 per ton (`KB-FERT-136`) |
| Qatar QAFCO/Mesaieed physical damage | OSPREY/FALCON | Consume their signal; I own the **capacity consequence** only |

---

## Open Instrument Gaps — load-bearing only (full register → `workbook/INSTRUMENT_GAPS.md`)

| Item | Class | Note |
|---|---|---|
| **NOLA $/st weekly LEVEL (T5)** | **🧊 RETIRED-PENDING-REPLACEMENT — WQ-257, Will 2026-09-26** | Advanced Turf dead after 8/10; headlines give a level only when quoted (9/25 $450–455; 10/02 "$430s"; Oct 9 "$430" in a secondary). CME/Barchart/Yahoo refuse this box. `KB-FERT-041`/`047` |
| **India tender awards, same-day** | LABELLED INFERENCE — WQ-466 C | Offers reached free relays in ~1 day (Bloomberg 10/8 → Business Standard 10/9); **counters** reached a free secondary the same day (10/14); a separately stated official **awarded price** is not recovered. Argus/IFDC links offers to secured volume (cutoff 10/13); review at T1 **11/18** (no new tender as of 11/11), keeping inference label. `KB-FERT-071/086` |
| Phosphate cost-push second source | **Q4 SULFUR READ · curtailment ISSUER-STATED** | Q4 Tampa $615/lt two-sourced (`KB-FERT-123`). Mosaic names the South Fort Meade and Miski Mayo mines (`KB-FERT-121`); capacity still unstated; WARN dates stay MIRROR (`KB-FERT-108`) |
| China export series + floor primary | **PARTIAL** | 3.3 Mt basis **RESOLVED** at MOFCOM (`KB-FERT-117`). Official Customs HS 310210 not reached; running total is two added relays (`KB-FERT-127`). CF's "almost nine" has no published sum behind it. Current floor level unverified |

---

## BOTTOM LINE

Retail MAP rose a ninth straight week to **$991/ton** and DAP jumped **$9 to $950** (DTN, week of Nov 2–6), so G5 is still not fired but MAP is now **$9** short of the $1,000 line; at recent steps the first firing print lands between 11/25 and 12/16. India has not issued its next urea tender and AFC says it may slip by weeks, so the nitrogen channel stays dead with nothing to grade. October food at home printed +0.4% but not grain-led (V6 2, convergence 16/40). Next wakes: TRADE re-look **11/15**, DTN and India **11/18**, ERS **11/24**, CPI **12/10**.
