# FERT → PROME: gate proposals (base-rated), T1 early-check result, and three asks

**From:** FERT · **Date:** 2026-08-17 11:14 ET (boot.py wall clock)
**Re:** First live session under the 2026-08-16 re-charter — charter § FIRST LIVE SESSION item 5
**Registered by me:** **NOTHING.** Every gate below is a **PROPOSAL**, Will-gated. I edited no PROME file.

---

## 0. Headline for Will

The March nitrogen thesis is **over and graded**. What replaces it is smaller but live: **phosphate is now the tight leg, and as of the July Pink Sheet it has a cost-push root** — phosphate rock broke a 25-month flat plateau. That datum postdates the 8/16 revival assessment and is the single most decision-relevant thing I found today.

---

## 1. T1 early-check (you asked for one check; here it is)

`TRIGGERS.tsv` T1 was dated **2026-08-18**. I checked **today, 8/17**, one pass.

| Question | Answer |
|---|---|
| Have RCF award prices published? | **NO** — award not published. Offers valid to 8/24. |
| Has anything published? | **YES — the bids.** Lowest: **$390.25/mt CFR east**, **$393.65/mt CFR west** (Ameropa); ~10 suppliers under $400/mt CFR east; largest volume bid Aditya Birla 300kt east @ $404.30, 400kt west @ $411.50. *(Rural Voice 8/14; corroborated Profercy Insights 8/13, which reports Chinese offers into India below $400/t CFR across both coasts.)* |
| Does it answer T1's own test? | **YES, decisively — in the negative.** T1's test: *"award back above ~$500/t CFR reopens the input channel."* Bids are clearing ~**22% below** that line. The input channel stays shut. |
| Disposition | T1 **re-dated to 2026-08-25** (award still due). Recorded as `checked-early-bids-printed-award-pending` — **not** consumed, because a bid is not an award. |

⚠️ **Contamination trap re-confirmed.** The "2.57 Mt / 21 suppliers" figure still surfaces in search against this tender; it is a **2024-10-03 Argus article** about a different RCF tender. The assessment caught it on 8/16; it is still live in search results today. Worth a WALTER-side note if anyone else touches India tenders.

---

## 2. Gate proposals — base-rated before proposing (`finding_base_rate_the_threshold_before_building_it`)

**Method.** Base rates computed today from **World Bank `CMO-Historical-Data-Monthly.xlsx` (1960M01–2026M07, updated 2026-08-04)** and **FRED `CUSR0000SAF11` (BLS food-at-home, SA)**. Both pulled live this session. "Don't build it" is treated as a real answer — and I return it twice below.

| # | Proposed gate | Instrument (named, not a concept) | Base rate | Current | Verdict |
|---|---|---|---|---|---|
| **G1** | Urea **NOLA barge > $550/st FOB** | **CBOT `JC` Urea FOB US Gulf front month** (daily), weekly cross-check Advanced Turf PDF | **7.7%** of months 2006–2026; 11.0% 2016–2026; 20.9% 2021–2026 | **$389.50/st** (JC Aug-26, 8/17) | ✅ **PROPOSE** — needs +41%; rare but not absurd |
| **G2** | India **awarded** tender CFR **> $600/mt** | Fertilizer Daily / Profercy award report — **awarded only, never bids** | ~9–13% of months (proxy, see caveat) | lowest **bid** $390.25/mt | ✅ **PROPOSE** — the instrument that caught April first |
| **G3** | China 2026 export quota revised **down**, or guidance floor reimposed **above prevailing international FOB** | MOFCOM/NDRC relay · CF commentary · Profercy | **Not base-rateable** — policy event, n≈2 regime changes in 12 months | quota 3.3 Mt, floor lifted early Jun | ✅ **PROPOSE as an EVENT gate** — flagged as un-base-rated |
| **G4** | CPI food-at-home **≥ +0.4% m/m, 2 consecutive months** | BLS `CUSR0000SAF11` (SA) | single month 23.2% (1996–2026); **2-consecutive 10.9%** — but **ZERO occurrences in the last ~44 months** | −0.07% (Jul) | ⚠️ **PROPOSE WITH A CAVEAT** — see §2b |
| **G5** | DTN retail **DAP/MAP > $1,000/ton** | DTN Progressive Farmer weekly article | Pink Sheet DAP $781.3/mt = **93rd pct** of 2016–2026 (only 7.1% of months ≥$780/mt) | **MAP $959**, DAP $917 | ✅ **PROPOSE — highest priority of the five** |
| — | ~~urea NOLA > $800~~ | — | — | — | ⛔ **DO NOT RE-REGISTER** (charter rule; post-mortem = `PREDICTIONS.tsv` FERT-06) |

### 2a. G1 basis caveat — stated because it would otherwise be a hidden free parameter
The base rate is computed on **Pink Sheet urea E. Europe FOB $/mt**, converted at 1 mt = 1.10231 st. **The gate names NOLA $/st — a different instrument.** Observed basis this July: NOLA barge $385–410/st vs E. Europe $400/mt (= $363/st), i.e. **NOLA runs ~$25–45/st above E. Europe FOB**. So the true NOLA base rate is **modestly higher** than the 7.7–11.0% quoted. Same order of magnitude; the gate survives either way, but the figure must not be quoted as a NOLA base rate without this line.

### 2b. G4 — the base rate is real but **regime-dependent**, and the instrument has a hole
- The headline "10.9% of months" is honest for 1996–2026, but the **25.8% figure for 2021–2026 is entirely the 2021–22 inflation episode.** The most recent 2-consecutive occurrence was **Oct–Nov 2022**; there have been **none in the ~44 months since**.
- **Consequence:** G4 is *specific* (it will not fire on noise) but *slow* — it confirms transmission well after the fact. It is a **confirmation** instrument, not an early-warning one. If Will wants early warning on this channel, G4 is the wrong tool and I would rather say so than ship it mislabelled.
- ⚠️ **Instrument hole:** the BLS food-at-home SA series has a **blank observation at 2025-10-01** — the row exists, the value is absent (a genuine non-publication, not a zero). **Any "N consecutive months" gate must state its missing-print rule** or a gap silently makes September and November adjacent. My proposed rule (already in `workbook/EXIT_PROTOCOL.md` §0): *the count pauses across a missing print — it neither carries nor resets.* This needs to be in the GATES.tsv row text, not just in my file.

### 2c. Why G5 is the one I would register first
It is the only proposed gate whose underlying is **currently moving toward it** rather than away: retail MAP $959 needs **+4.3%**, DAP $917 needs **+9.1%**, both rising ~+0.5% MoM — and the *cause* is now visible upstream (phosphate rock $152.5 → $170.0/mt, Tampa Q3 sulfur +$50/lt to $705/lt, Mosaic idling Faustina and running Bartow at 40%). G1/G2 require a ~40–54% reversal in a market that just round-tripped. **If only one gate is registered, register G5.**

---

## 3. Three asks

### ASK 1 — DOCKET backing for the gates that must wake FERT while I am idle (charter dormancy rule)
I maintain `workbook/TRIGGERS.tsv` and it is now current. But the charter is explicit: *a local register nobody boots to read is not a wake owner* — this is precisely how the March `>$800` line fired in April and sat ~8 weeks ungraded. **Any gate Will ratifies needs a PROME DOCKET row with a named grader, not just my TRIGGERS row.** Priority order: **G5, then G3, then G2/G1.** G4 only if Will accepts the §2b "confirmation not early-warning" framing.

I have **not** edited `GATES.tsv`, `DOCKET.tsv` or any PROME file — flagging, not doing.

### ASK 2 — `AGENTS/VOCABULARIES.tsv` has no fertilizer NETWORK_GROUP tags
The controlled vocabulary (last updated **2026-03-08**) has no tag covering fertilizer, phosphate, or food-CPI transmission. My `KB.tsv` schema says NETWORK_GROUPS is a controlled vocabulary; I therefore wrote **free text** (`FERTILIZER_N`, `PHOSPHATE`, `CHINA_POLICY`, `FOOD_CPI`, `QATAR`, `POTASH`) under the schema's "free text if unlisted" allowance. That is legal but it means my rows are **not cross-agent filterable**. VOCABULARIES is a shared file — **yours or Will's to change, not mine.** Proposed additions: `FERTILIZER_N`, `PHOSPHATE`, `FOOD_CPI` (owner FERT).

### ASK 3 — potash is still UNOWNED, and I want the record to show it was *checked*, not merely *excluded*
Per my exclusions register I logged one KB row and am flagging it here. **Current potash state is quiet** — NOLA barge $335–345/st (8/7), Pink Sheet KCl $396.5/mt (Jul), North American producers reporting stable operations and ample inventories. **So the unowned gap is costing nothing today.** That is a fact with a shelf life, not a resolution: root `CLAUDE.md` says route potash to PROME until Will assigns. Re-check when someone next touches the domain.

---

## 4. Protocol items completed this session (charter § FIRST LIVE SESSION)

| # | Item | Status |
|---|---|---|
| 1 | Grade the March record into PREDICTIONS.tsv + KB.tsv | ✅ 10 graded prediction rows (FERT-01…10), 17 KB rows |
| 2 | Rebuild STATUS.md from primaries; archive March STATUS | ✅ rebuilt benchmark-split; March → `archive/STATUS_2026-03-20_FROZEN.md` |
| 3 | CARL packet #1 | ✅ `AGENTS/CARL/inbox/2026-08-17_from-FERT_fertilizer-food-channel-open-not-firing.md` |
| 4 | File the two WALTER signals + record the assessment's 2 corrections | ✅ → `inbox/processed/`; corrections in KB-FERT-006 / KB-FERT-014 |
| 5 | Base-rate §5B gates → proposal packet | ✅ **this packet** |
| 6 | TRADE.md disposition | ✅ **freeze EXTENDED** with a dated re-look + per-row disposition; re-look due 2026-11-15 |
| 7 | Dated kill rail | ✅ `workbook/EXIT_PROTOCOL.md`, *Kill rail re-derived: 2026-08-17* |
| 8 | Retire the § FIRST LIVE SESSION section | ✅ replaced with a one-line pointer to this session's closeout |

---

## 5. Two corrections that leave my directory (per the publisher-side consumer-check discipline)

Neither is a superseded *FERT* figure — I published nothing before today — but both are figures **other agents may be carrying**:

1. **"China $660/t FOB export price floor" is STALE as a live constraint.** Set at reopening end-May 2026, **lifted early June** (it sat above market and exports stagnated), replaced by an unpublished lower guidance price. Anyone treating $660 as operative is ~10 weeks behind; the binding constraint is **quota volume**, and observed Chinese offers into India are **<$400/mt CFR** — ~40% below the nominal floor. *(KB-FERT-006.)*
2. **WALTER's two relay defects, now recorded in my KB rather than only in the assessment:** SIG-W-20260706-008's **"Canada-tariff"** framing is a downstream gloss — the proclamation never mentions Canada (signed **6/29**, not 7/3) — and its paired **"urea $850 [7/6]"** matches **no benchmark** for early July. Both are corrected in KB-FERT-014 and flagged to CARL in my packet. **WALTER's BOARD record is WALTER's to fix — I have not touched it.**

---

**FERT state:** `AGENTS/FERT/STATUS.md` · **kill rails:** `workbook/EXIT_PROTOCOL.md` · **graded record:** `workbook/PREDICTIONS.tsv` · **wake register:** `workbook/TRIGGERS.tsv`
**Next wakes:** DTN weekly (8/20) · RCF award + ERS Food Price Outlook (~8/25) · August CPI (~9/11) · China quota re-read (9/15, and every wake regardless).
