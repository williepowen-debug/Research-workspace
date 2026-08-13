# AEOLUS · REGIME — ENSO & teleconnections

**Created:** 2026-08-13 (Will-directed) · **Owner:** AEOLUS
**Status: CORE — the master variable.** Not a channel; **the shared antecedent that sets the sign on the channels.**

---

## WHY THIS IS THE MOST IMPORTANT FOLDER I OWN

**ENSO is the single highest-leverage read in this agent** (L-06). It sets the sign on **C1** (shear → hurricane suppression), **C2** (drought/crop), **C3** (heating/cooling demand), **C5** (Panama hydrology) and **C6** (Western hydrology) **simultaneously** — which is exactly why it gets a folder rather than a channel row:

> **A channel that is scored is a channel that can be double-counted. ENSO is the ROOT, so counting it once across every channel it drives is the whole point of the convergence matrix's Independence column (L-02).**

**And it carries more accumulated method-debt than everything else combined: 6 of my 17 lessons are ENSO-method lessons** (L-06, L-08, L-09, L-14, L-17 + L-02's independence rule). Every one was learned by getting a number wrong. **This folder exists so they are learned once.**

## 🔑 THE FOUR BASELINES — the error this folder is built to stop (L-09)

**There are four Niño-3.4 numbers in circulation right now and NONE of them are interchangeable.** As of 2026-08-13, all four are simultaneously true:

| Instrument | Value | Baseline | Use it for |
|---|---|---|---|
| **ONI** | **+1.39** (MJJ) | 30-yr centred, ERSSTv5 | **LEVEL & official classification.** The instrument my predictions resolve on. |
| **RONI** | **+0.98** (MJJ) | ONI minus tropical-mean SST anomaly | **DYNAMICAL strength / teleconnection expectation** |
| **OISST monthly** (`sstoi`) | **+2.03** (Jul) | 1991-2020 fixed | **TREND** month-to-month |
| **Weekly** (`wksst`) | **+2.6** (05 Aug) | 1991-2020 fixed | **Fastest trend only.** Noisiest. |

⚠️ **Never put two of these in one sentence without naming both instruments.** A "+2.6" and a "+1.39" describing the same ocean in the same week is not a contradiction and not a confabulation — **it is two baselines**, and I have twice mistaken that for an error (L-08 → L-09 → the 8/3 amendment).
⚠️ **Region conflation is the adjacent trap:** a startling "+3 °C" is almost always **Niño-1+2** (today: **+3.56**), not Niño-3.4. **Check the region before the number.**
⚠️ **Column order differs between files:** `wksst` = 1+2 / 3 / **3.4** / 4 · `sstoi` = 1+2 / 3 / 4 / **3.4**. Read the header every time.

## SCOPE

**Mine:** ENSO state and forecast · the ONI/RONI/OISST reconciliation · teleconnection composites and **their reliability limits** · seasonal outlooks (CPC monthly/seasonal) · the independence accounting across C1–C6 · IOD/PDO/MJO **only** where they modulate an ENSO read I am already making.

**Not mine:** the *consequences* — those are the channels and their owners. **This folder produces the sign; the channel folder produces the repricing.** Winter power demand → **WATT**; crop → **CARL/MARCO**; hurricane → `../hurricane/`; Colorado hydrology → `../water/`.

**⛔ Not a weather-forecasting desk.** No day-to-day forecasts, no model-run watching. **CFSv2/ECMWF single-run tails are logged as tails, never adopted as a read.**

## THE STANDING DISCIPLINES

**① Mechanism vs thermometer (L-04).** The climate *mechanism* is high-confidence; the seasonal *forecast readout* is confounded. **A bad forecast is not a broken thesis.**

**② Composites degrade at high amplitude — and this is now GOVERNING, not cautionary (L-14 → L-17).** Standard El Niño composites are built mostly from **weak and moderate** events because those dominate the sample. **When quoting a composite into a very strong event, state the n of same-amplitude analogues; if n<5, say so in the packet.** With CPC now at **69% for an event exceeding everything back to 1950**, the analogue set is heading toward **n=0** and every composite becomes an **extrapolation**.

**③ A rising probability can change the KIND of claim, not just its level (L-17).** Today's move was *two* moves: 81%→>90% (a firming) **and** a new 69%-historic (majority odds on an **out-of-sample** outcome). **These point in opposite directions for confidence** — the regime got more important while every derived read got less reliable. **Report both or the recipient upgrades conviction on exactly the reads that just weakened.**

**④ Level and forecast-odds move independently.** In Jul 2026 the *level* was corrected **down** (+1.7 → +1.2) while very-strong *odds* rose (63% → 81%). **Track them as two separate reads.**

**⑤ Count the root once (L-02).** One ENSO state driving C2+C3+C6 is **one** antecedent. ⚠️ **C5-Rhine is a SEPARATE European basin — never weld it to the ENSO root.**

## FILES

| File | Purpose |
|---|---|
| `README.md` | this charter — the baseline rules and standing disciplines |
| `DOSSIER.md` | live regime state + the ONI↔RONI reconciliation + per-channel sign table |
| `AGENT.md` | Spawn brief for a domain worker — scope, instrument vocabulary, hard limits, return contract. |
| `RUN_REPORT.md` | **The deliverable of the most recent worker run** (overwritten each run). Absent = no run, or a run that died. |
| `workbook/SERIES.tsv` `LOG.tsv` | **Observations** — time series + dated events. Keyed by `(date, instrument)`; append-only. |
| `SOURCES.md` | **verified working pull commands** for all four indices |

⚠️ **Central `workbook/` stays canonical** — no forked ledger here.
