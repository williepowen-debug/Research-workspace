# AEOLUS · SEISMIC — baseline dossier

**First read: 2026-08-13** (folder created same day). **Status: 🟡 event-triggered watch — no trigger currently fired.**

> **Last real data refresh: 2026-08-27**  ·  **Source + trigger audit run 2026-08-27**

---

## 🔴 AUDIT 2026-08-27 — sources verified, and TWO M7+ EVENTS WERE SITTING UNASSESSED

**Audited the way the charter says to — by checking the triggers and sources still RESOLVE, never by entry count.**

**All three sources return HTTP 200** (USGS significant_month.geojson · USGS volcanoApi/elevated · GVP WeeklyVolcanoRSS). **The instruments are sound.**

⚠️ **But the feed carried 13 significant events in 30 days, including two M7+ that this folder had never graded:**

| Date | Event | PAGER | S-2 verdict |
|---|---|---|---|
| **2026-08-14** | **M7.7** — 68 km NNW of Ende, **Indonesia** | YELLOW | **NOT FIRED** — low insured density, limited-impact alert, 51 felt reports, no tsunami, no insured-loss estimate located |
| **2026-08-10** | **M7.4** — San José del Palmar, **Colombia** | 🔴 **RED** | **NOT FIRED** — but on stated grounds, not asserted ones |

🔑 **The Colombia grading is the one that needed doing properly.** A **RED** PAGER alert is USGS's highest impact level, and the 8/13 dossier disposed of it in half a clause (*"both M7+ events in low-insured-density areas"*). **PAGER RED estimates FATALITIES and TOTAL ECONOMIC loss — not INSURED loss.** Colombian insurance penetration is ~2–3% of GDP, so a red economic alert does **not** imply the **>$10B insured** figure S-2 requires. **PERIL AND LOSS ARE DIFFERENT INSTRUMENTS** — the same discipline `hurricane/` and `wildfire/` carry, applied here. **If a credible insured-loss figure surfaces → REGINALD.**

🔴 **AND THE M7.7 IS THE REAL FINDING: it occurred ONE DAY AFTER the 8/13 dossier and went unassessed for 13 days.**
**`seismic/` is exempt from the #1 guard's *standing-live-read* obligation — that exemption is correct and I am not proposing to change it.** But **the exemption is from maintaining a standing read, NOT from grading a trigger-relevant event when one occurs.** Nothing in my boot sequence distinguishes those two things, so a folder whose *quiet* is expected also stays quiet when it should not be.
⇒ **Rule adopted: the seismic source audit runs whenever the folder is touched, and its FIRST question is "did any qualifying event occur since the last audit?" — not "is the dossier stale?"** Entry count still proves nothing; **an ungraded M7+ does.**

**S-1 · S-3 · S-4 · S-5: unchanged, NOT FIRED** (no VEI 5+ / stratospheric SO₂; no >48 h aviation closure; no named energy asset; Great Sitkin still WATCH/ORANGE at *High* not *Very High* threat).

---

> *(superseded header) **Last real data refresh: 2026-08-13**  ·  **Dossier written: 2026-08-13**
> *Two-clock header (PAT-044) — `scripts/ledger_staleness.py` reads the first line. **The data date, not the edit date**: a hygiene edit must NOT bump it.*
> **Observations → `seismic/workbook/SERIES.tsv`** · findings → central `workbook/KB.tsv` · synthesis → `STATUS.md`. **Flow is one-way.**
> **Feeds:** C1 · C2 · C3 · C4 (on trigger only)

> **This dossier's normal state is "nothing to report."** Absence of recent entries is the expected condition, not neglect — see `README.md`. **Audit the triggers and sources, not the entry count.**

---

## 1. BASELINE — established 8/13 so a future spike has something to be measured against

**Why record a baseline at all:** without it, the first alarming headline has no denominator, and *any* M7 reads as exceptional. **It is not** — the 30-day window below contains **two M7+ events and neither fires a trigger.**

### Significant earthquakes, past 30 days (USGS, 8/13)

| Mag | Date | Location | Trigger? |
|---|---|---|---|
| **M7.4** | 8/10 | 5 km S of San José del Palmar, **Colombia** | ❌ — Chocó region, low insured density |
| **M7.3** | 7/17 | 52 km W of Puerto Madero, **Mexico** | ❌ — offshore Chiapas |
| **M6.8** | 7/28 | **Kumamoto Region, Japan** | ⚠️ **see §2 — the one worth a look** |
| M6.4 | 7/17 | 96 km SW of Puerto Madero, Mexico | ❌ |
| M6.3 | 8/05 | south of the Kermadec Islands | ❌ — remote |
| M6.3 | 8/05 | 32 km SW of Sarangani, Philippines | ❌ |
| M6.2 | 7/14 | 32 km WSW of Sarangani, Philippines | ❌ |
| M5.8 / M5.7 | 7/28 | NW of Oula Xiuma, China | ❌ |
| M5.6 | 8/08 | 57 km WNW of Skwentna, Alaska | ❌ |
| M5.5 | 7/19 | 5 km S of Chambara, Peru | ❌ |
| M5.0 | 7/23 | 38 km SSE of Spearman, **Texas** | ❌ — but see note |

**12 significant events in 30 days, none with a tsunami.** ⚠️ **Two M7+ events fired nothing** — that is the discriminator working correctly, and it is the calibration point: **magnitude alone is not a signal.** *(Note: the Spearman TX M5.0 sits in the Permian, where induced seismicity from wastewater injection is a known regulatory issue — that would be a **BRENT/regulatory** matter, not a climate one, and I am not claiming an attribution.)*

### US volcanoes at elevated alert (USGS, 8/13)

| Volcano | Ground | Aviation | NVEWS threat |
|---|---|---|---|
| **Great Sitkin** (AK) | **WATCH** | **ORANGE** | High |
| **Kilauea** (HI) | ADVISORY | YELLOW | **Very High** |
| Shishaldin (AK) | ADVISORY | YELLOW | High |
| Kupreanof (AK) | ADVISORY | YELLOW | Moderate |
| Ahyi Seamount (N. Marianas) | ADVISORY | YELLOW | Very Low |

**S-5 not fired.** It requires WARNING/RED, **or** WATCH/ORANGE at a **Very High Threat** volcano. Great Sitkin is at WATCH/ORANGE but rated **High**, not Very High; Kilauea is Very High but only ADVISORY. **Neither satisfies both legs** — this is the trigger being graded on its letter, the same discipline applied to C5 and C6.

### Global volcanic activity (Smithsonian GVP, week 7/30–8/5)
**23 items. New eruptive activity:** Etna (Italy), Fuego (Guatemala), Krakatau (Indonesia), Puracé (Colombia), Telica (Nicaragua). **Continuing:** Aira (Japan), Ambae, Dukono, Great Sitkin, Ibu, Kilauea and others.
**None reported at a scale implicating stratospheric injection ⇒ S-1 not fired, no C2 climate consequence.**

⚠️ **A coincidence I am explicitly NOT welding:** Puracé (Cauca) shows new eruptive activity and there was an M7.4 near San José del Palmar (Chocó) — both "Colombia," different systems, hundreds of km apart. **Two facts sharing a country name is not a mechanism.** Recorded so a later reader doesn't rediscover the pair and infer a link I already declined to draw.

---

## 2. ⚠️ THE ONE ITEM WORTH ANOTHER AGENT'S ATTENTION

**M6.8, Kumamoto Region, Japan — 2026-07-28.** USGS names it *"The 2026 Kumamoto Region, Japan Earthquake,"* and a USGS-assigned event name signals a notable event rather than routine background.

**This is SAM's geography, not mine.** Kumamoto (Kyushu) is a real industrial location — the 2016 Kumamoto quakes disrupted semiconductor and auto supply chains, and Kyushu hosts significant semiconductor manufacturing.

**What I have NOT established, and will not assert:** damage extent, casualties, insured loss, industrial disruption, or **any** supply-chain consequence. **I have a magnitude, a date and a place — nothing more.** Whether it reprices anything is **SAM's** call, and I am routing rather than deep-diving.

⇒ **ACTION: flag to SAM.** ⚠️ **It is 16 days old** — if it mattered, SAM likely has it already. **The flag is cheap and the alternative is assuming coverage, which is the failure mode I want to avoid** (`finding_never_received_is_not_doesnt_hold`). Sent as a question, not a finding.

---

## 3. NO TRIGGER FIRED

| Trigger | State |
|---|---|
| **S-1** volcanic climate (VEI 5+, stratospheric SO₂) | **NOT FIRED** — no qualifying eruption |
| **S-2** insured cat (M7+ near insured zone / >$10B) | **NOT FIRED** — both M7+ events in low-insured-density areas |
| **S-3** aviation/supply chain (>48 h closure) | **NOT FIRED** |
| **S-4** energy infrastructure (named asset) | **NOT FIRED** |
| **S-5** US volcano escalation | **NOT FIRED** — see §1 for the two-leg reasoning |

**Fired count: 0/5.** **This is the expected state and requires no further work.**

---

## NEXT CHECK

**No standing obligation.** Re-run the three `SOURCES.md` commands (~30 seconds total) **when:**
- a seismic/volcanic event reaches me through WALTER, Will or another agent — **verify at the primary before doing anything with it** (L-11: a single-source live-event claim is a **lead**, not a finding); **or**
- roughly monthly, to keep the baseline from going stale enough to be useless as a denominator.

**Dormancy check: if no trigger fires by 2027-08-13, banner this folder dormant** rather than letting it look live while unmaintained.
