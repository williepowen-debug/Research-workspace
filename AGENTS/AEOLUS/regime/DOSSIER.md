# AEOLUS · REGIME — live dossier

**As-of: 2026-08-13**, all figures CPC primary. Consolidated from KB-AEO-016/021/038/045/046/053/054 + VX-19/20.

> **Last real data refresh: 2026-08-21**  ·  **Dossier written: 2026-08-21**
>
> **2026-08-21 — refreshed by AEOLUS directly (no worker spawned).** Recorded here because **L-28 binds whoever DID the work, not whoever was spawned**: I pulled these primaries in my own context and would otherwise have left this folder reading silent while the central `KB.tsv` gained regime rows. ⚠️ **`scripts/domain_log_check.py` did NOT and COULD NOT flag that** — it tests *touched-but-silent*, and I had not touched the folder at all. **Worked-on-but-untouched is a blind spot in my own guard.**
>
> **This pass:** ✅ **RONI pulled for the first time — MJJ 2026 = +0.98** vs ONI +1.39 (offset −0.41, matching the derived 2020s value; **still not constant**). CPC 8/20 seasonal discussion **restates >90% very-strong and 69% historic — neither was RAISED**; no CPC primary states 95%. Weekly Niño-3.4 **+2.7 (12AUG)**, strengthening from +2.1 (15JUL). **DJF 2026-27 outlook read at the primary as a GIS product** (`lead4_DJF_temp`, `Fcst_Date=20260820`) rather than an image.
>
> 🔴 **INSTRUMENT TRAP LOGGED — the CPC discussion's weekly figures do not match CPC's own weekly file** (+1.8/+2.5/+3.2 in the prose vs +2.7/+3.2/+4.0 in `wksst9120.for`). **Reading across them inverts the trend sign.** Consistent with a relative/RONI basis; **not proven, not asserted.** See `workbook/LOG.tsv`.
> ⚠️ **Also known-bad now: `wksst8110.for`** — I reconstructed it from memory and got a dead file ending 27JAN2021. `SOURCES.md` had the right one all along.
> *Two-clock header (PAT-044) — `scripts/ledger_staleness.py` reads the first line. **The data date, not the edit date**: a hygiene edit must NOT bump it.*
> **Observations → `regime/workbook/SERIES.tsv`** · findings → central `workbook/KB.tsv` · synthesis → `STATUS.md`. **Flow is one-way.**
> **Feeds:** C1 · C2 · C3 · C5 · C6 (root: owns the ENSO indices)

---

## 1. STATE — four instruments, all correct, none interchangeable

| Instrument | Value | As-of | Reads |
|---|---|---|---|
| **ONI** (official level) | **+1.39** | MJJ 2026 | 0.11 below the "strong" (≥1.5) line |
| **RONI** (dynamical) | **+0.98** | MJJ 2026 | **only moderate in relative terms** — see §2 |
| **OISST monthly** (trend) | **+2.03** | Jul 2026 | Apr +0.47 → May +0.94 → Jun +1.55 → **Jul +2.03** |
| **Weekly** (fast trend) | **+2.6** | 05 Aug 2026 | 15Jul +2.1 → 22Jul +2.2 → 29Jul +2.3 → **05Aug +2.6** |
| Niño-1+2 | **+3.56** | Jul 2026 | *the number that gets misquoted as "3.4"* |

**CPC forward odds (8/13 Discussion, verbatim):**
- *"El Niño is strengthening, with a **greater than 90% chance of a very strong event** during the Northern Hemisphere fall and winter 2026-27."* — from **81%** on 7/9.
- *"During the October–December 2026 season, there is a **69% chance of a historic event that would exceed the strength of previous El Niño events dating back to 1950** (+2.5 °C or more for a 3-month RONI value)."*

---

## 2. 🔑 THE ONI↔RONI RECONCILIATION — computed 8/13, and it changes how the headline reads

**The offset is NOT a constant. It has grown monotonically, every decade:**

| Decade | mean ONI − RONI |
|---|---|
| 1950s | −0.17 |
| 1970s | −0.17 |
| 1990s | −0.11 |
| 2000s | +0.01 |
| 2010s | **+0.22** |
| **2020s** | **+0.44** |

**That drift *is* the tropical-mean warming, showing up inside the instrument.** Current offset (MJJ 2026): **+0.41**.

### What CPC's "+2.5 RONI" implies — and the honest caveat

At the current ~+0.41 offset, **+2.5 RONI ≈ +2.9 ONI**. For scale:

| Event | ONI peak | RONI peak | offset |
|---|---|---|---|
| 1997-98 | **+2.37** (NDJ) | +2.28 | +0.09 |
| 2015-16 | **+2.59** (NDJ) | +2.25 | +0.34 |
| 2023-24 | +1.99 (NDJ) | +1.40 | +0.59 |

⇒ **In RONI space** (CPC's framing, and the fair cross-era comparison) **+2.5 exceeds 1997 and 2015 by ~0.25.**
⇒ **In raw ONI space** it would imply roughly **+2.9**, ~0.3 above the 2015-16 record.

⚠️ **Both statements are true and they answer different questions.** RONI asks *"is this event dynamically stronger than past ones?"*; ONI asks *"how warm is the water?"* **Do not present one as a correction of the other, and do not carry a single-number conversion forward** — the offset is drifting and is not stable within an event either (it ran +0.09 in 1997 and +0.59 in 2023).

### 🔑 The under-appreciated read: the dynamical event is WEAKER than the raw SST suggests

**ONI +1.39 is nearly "strong." RONI +0.98 is squarely moderate.** The gap is the warming background, not the event.

**This matters because teleconnections respond to the atmospheric circulation — driven by SST *gradients* and convection — rather than to absolute SST**, which is precisely why CPC frames its headline in RONI.

⇒ **Keying composite expectations to ONI risks over-calling the teleconnection.** ⚠️ **Stated as a caution, not a correction**: I have not re-derived my channel signs against RONI, and doing so is a real piece of work, not a one-line adjustment. **Registered as an open question below** rather than silently applied.
⚠️ Note this cuts **against** alarm: it argues the atmospheric response may be *milder* than "historic El Niño" headlines imply — the opposite of the direction a dramatic number pulls you.

---

## 3. PER-CHANNEL SIGN TABLE — what the regime sets

| Channel | Sign | Confidence | Basis |
|---|---|---|---|
| **C1** hurricane | **SUPPRESS** ↓ | **HIGH** — mechanism now visible in storm-level forecasts (NHC names *"strong upper-level winds and dry air"* on AL92) | shear |
| **C2** crops | ambiguous | **LOW** — currently **refusing to confirm** (corn 61 / soy 62 G/E, 6 pts above my band) | drought geography is southern Plains, not the corn belt |
| **C3** winter demand | **MEAN down** ↓ · **PEAK: no sign** | mean HIGH · **peak REFUSED** | n=2 very-strong analogues, **split 1-1** |
| **C4** fire | southern-Plains fire risk should **abate** by late autumn | MED | the wet-south signal — **AEO-09 tests it** |
| **C5** Panama | drought risk ↑ | MED | El Niño → Panama hydrology |
| **C5** Rhine | **NO SIGN — separate basin** | — | ⚠️ **European basin. Never weld to the ENSO root.** |
| **C6** Colorado | **NOT relief** | MED | see §4 |

**Independence accounting:** C1 + C2 + C3 + C5-Panama + C6 share **ONE** root. **Count it once.** C5-Rhine is independent.

---

## 4. ⚠️ TWO GUARDS AGAINST INTUITIVE-BUT-WRONG READS

**① A record El Niño does NOT refill the Colorado.** The reliable wet signal is the **Southwest / Lower Basin**; **Powell's inflow is UPPER Basin**, near the ENSO precipitation **dipole pivot** where the signal is weak and sign-ambiguous. **The wet anomaly lands downstream of the reservoir that needs it.** Full treatment → `../water/DOSSIER.md`.

**② The northern tier goes MILDER, not colder — I got this backwards once and shipped it.** On 8/3 I told MARCO a very-strong El Niño gives an "active/cold Northern-tier winter." **CPC says the inverse:** storm track shifts **SOUTH**, the North goes **milder and less stormy**. I reasoned validly from an unchecked premise, produced a confident coherent wrong finding, and **MARCO logged it as a valued counterweight to its own thesis** — the worst place for a wrong finding to sit. Found by accident 9 days later, pulling the same primary for an unrelated question (**L-13**).

> **The rule that came out of it: when a packet's CONCLUSION turns on a directional climate premise, pull the primary for THAT premise in the same session. It is one fetch. And a well-argued packet deserves MORE premise-scrutiny than a hedged one, because its polish suppresses the reader's own checking.**

---

## 5. THE RELIABILITY PROBLEM — now governing (L-14 → L-17)

Composites are built mostly from **weak and moderate** events. I hit the degradation **three times in one afternoon** on 8/12, at an amplitude *below* the current forecast:

1. **PJM winter peak** — n=2 very-strong analogues, split 1-1; **both of PJM's highest winter peaks came in *non*-strong-El-Niño winters.**
2. **PNW snowpack** — UW: WA snowpack "fared pretty well" in all three very-strong events (1984/1998/2016), against the composite's dry signal.
3. **Polar vortex** — NOAA's own caveat that **1997-98 produced no major SSW.**

⇒ **With CPC at 69% for an out-of-sample event, the analogue set trends to n=0 and every composite becomes an extrapolation.** **The composite still gives the mean sign; it does not give the tail, and at extreme amplitude it may not give the mean either.**

**The only non-extrapolated substitute is a season-specific forecast** → **CPC DJF 2026-27 outlook, ~8/20.** Highest-value dated item I hold. **PUBLIC-AND-UNFETCHED, not unavailable.**

---

## OPEN QUESTIONS

1. **🔴 CPC DJF 2026-27 outlook (~8/20)** — supersedes every composite in my 8/12 WATT and MARCO packets. **Owed to both.**
2. **Should channel signs be re-derived against RONI rather than ONI?** (§2). Real work, not a one-line fix. **Would likely *soften* several reads** — worth doing before winter, and worth telling WATT/MARCO if it changes anything.
3. **Track the ONI−RONI offset as OND approaches** — if it holds ~+0.41, +2.5 RONI implies ~+2.9 ONI. **Re-compute, never carry the conversion forward.**
4. **AEO-02** (ONI ≥1.5 in an NDJ season, 70%) resolves on **ONI**, currently +1.39. **Not closing early** despite >90% very-strong odds — the prediction resolves on the letter, and >90% is about a *different, higher* bar.
5. **AEO-09** (`../wildfire/`) is the cheapest live test of composite reliability: does the wet-south signal verify **where it is strongest**? If not, L-14 governs and the C1 suppression leg — same composite machinery — downgrades with it.
