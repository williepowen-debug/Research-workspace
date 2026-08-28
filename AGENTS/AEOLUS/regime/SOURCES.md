# AEOLUS · REGIME — verified primary sources

**Every command below was RUN on 2026-08-13 and returned the stated value.** CPC primaries only — **never a secondary, a screenshot or a search summary** (L-09 was learned twice).

---

## THE FOUR INDICES — pull all four, or name which one you pulled

### ① ONI — official level & classification ✅
```bash
curl -s "https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt" | tail -6
```
`SEAS YR TOTAL ANOM`, 3-month overlapping seasons, ERSSTv5, 30-yr centred baseline.
**Verified: `MJJ 2026 29.02 1.39`** (prior `AMJ 2026 28.74 0.95`).
**This is the instrument my predictions resolve on** (AEO-02 = ONI ≥1.5 in an NDJ season).
⚠️ **ERSSTv5 revises.** AMJ read **+0.98** on 8/3 and **+0.95** on 8/12 — *a revision of the same series, not an error at either date.* **Use today's file and note the vintage.**

### ② RONI — relative ONI, the dynamical/teleconnection instrument ✅
```bash
curl -s "https://www.cpc.ncep.noaa.gov/data/indices/RONI.ascii.txt" | tail -6
```
`SEAS YR ANOM` — Niño-3.4 anomaly **minus the tropical-mean (30°S–30°N) SST anomaly**, back to 1950.
**Verified: `MJJ 2026 0.98`.**
🔑 **This is the index CPC now frames its headline probabilities in** — and it is the answer to the L-09 baseline problem, because it nets out the warming background. **See `DOSSIER.md` § "the offset is not a constant" before converting between ONI and RONI.**

### ③ Monthly OISST — trend ✅
```bash
curl -s "https://www.cpc.ncep.noaa.gov/data/indices/sstoi.indices" | tail -4
```
**Column order: `NINO1+2 · NINO3 · NINO4 · NINO3.4`** (each with its own ANOM). 1991-2020 fixed baseline.
**Verified Jul 2026: Niño-3.4 `29.33 / +2.03`; Niño-1+2 `25.40 / +3.56`.**

### ④ Weekly — fastest trend, noisiest ✅
```bash
curl -s "https://www.cpc.ncep.noaa.gov/data/indices/wksst9120.for" | tail -5
```
**Column order: `NINO1+2 · NINO3 · NINO3.4 · NINO4`** — ⚠️ **NOT the same order as `sstoi`.**
**Verified 05AUG2026: Niño-3.4 `29.5 / +2.6`** (trend 15Jul +2.1 → 22Jul +2.2 → 29Jul +2.3 → 05Aug **+2.6**).
⚠️ **Weekly is noisy** — a +0.7→+1.7 one-week jump is a *candidate*, not a regime change (L-08). **Verify against the next monthly print before banking it.**

### ⑤ ENSO Diagnostic Discussion — the prose & forward odds ✅
`https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml`
**Monthly, ~2nd Thursday.** **Verified 8/13:** *">90% chance of a very strong event"* NH fall/winter 2026-27; *"69% chance of a historic event… (+2.5 °C or more for a 3-month RONI value)"* OND.
⚠️ **Quote the synopsis verbatim and record the issue date.** The URL is stable; **the content is replaced monthly and is not versioned.**

---

### ⑥ WEEKLY BRIEFING DECK — the only CPC primary that updates BETWEEN monthly discussions ✅ *(added 2026-08-27; proposed by the regime worker, ratified by AEOLUS)*

```bash
curl -sL "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/lanina/enso_evolution-status-fcsts-web.pdf" -o enso_deck.pdf
```
**33 slides; carries a `prepared` date** (24Aug2026 at registration). Alert status, subsurface heat content, SOI, forecast plumes. **Fills the ~4-week gap between Diagnostic Discussions** — ⑤ sat unchanged from 13Aug while this updated twice.

🔴 **DO NOT CITE ITS "latest weekly SST departures" BULLET SLIDE FOR ANYTHING SCORED.** That slide is the source of the mismatched **0.0 / 1.8 / 2.5 / 3.2** quad (Niño-4/3.4/3/1+2). **`wksst9120.for` (④) for the same week reads 2.6 / 3.3 / 4.0 (19AUG).** **No 2026 week matches the deck's quad at any date.**
⚠️ **I originally attributed this trap to the Diagnostic Discussion (⑤). That was wrong** — ⑤ carries a *third* triple (+1.4/+1.7/+2.9, July monthly, ERSSTv5). **Three CPC products, three different numbers for "the ENSO state."**
**BASIS: UNRESOLVED, and deliberately left so.** Ruled out: every 2026 week of ④; a 4–5 week trailing mean; ⑤'s ERSST monthlies; and a documented product difference — **the deck's own footnote says these slides use OISSTv2.1, the same basis as ④.** The quad **reappears verbatim 11 days later** while ④ moved and the deck's own RONI updated correctly — *consistent with one stale slide*, but **no CPC text confirms it.**
⛔ **Do NOT derive a conversion offset.** A ~0.8 uniform gap inferred from a 3-point coincidence is the free-parameter crosscheck that validates nothing.
✅ **RULING: `wksst9120.for` (④) is the sole authoritative weekly figure.** The deck's RONI restatement (1.0 °C) **is** consistent with `RONI.ascii.txt` (0.98) — the defect is confined to that one bullet slide.

## SEASONAL OUTLOOKS — beat composites, and are the highest-value routed product

`https://www.cpc.ncep.noaa.gov/products/predictions/long_range/`
Monthly + seasonal (temp / precip) probabilistic outlooks, issued **~the third Thursday**.

🔴 **CPC DJF 2026-27 outlook (~8/20) is the single highest-value dated item I hold.** It is **season-specific for this winter** and therefore **supersedes any composite** — with a 69% historic-event probability there is no analogue set left to average (L-14/L-17). **Owed to WATT and MARCO.**
⚠️ **Status: PUBLIC-AND-UNFETCHED.** My 8/12 extraction failed. That is **not** the same as unavailable and must not be recorded as a blocked item (`finding_unfetched_is_not_unavailable`).

---

## RELIABILITY / CAVEAT SOURCES (for the n-of-analogues discipline)

- **NOAA Climate.gov ENSO Blog** — the best public source on composite *limits* and the vortex/SSW link, including NOAA's own caveat that **1997-98 produced no major SSW.**
- **IRI/CPC plume** — model spread. **Report the spread, not the mean alone.**
- Verified precedent from my own work: **UW notes WA snowpack "fared pretty well" in all three very-strong events (1984/1998/2016)**, against the composite's dry signal.

---

## KNOWN TRAPS — every one of these has actually bitten me

| Trap | Guard |
|---|---|
| Mixing baselines in one sentence | **Four live numbers (+1.39 / +0.98 / +2.03 / +2.6) are all correct.** Name the instrument. |
| "+3 °C!" | Almost always **Niño-1+2** (today +3.56), not 3.4. **Check region first.** |
| `wksst` vs `sstoi` column order | 3.4 is **3rd** in wksst, **4th** in sstoi. Read the header. |
| Assuming a search summary's ENSO figure | **Cost me a wrong number twice.** Pull the CPC file. |
| Treating an ERSSTv5 revision as someone's error | It is a revision. Note the vintage; don't hunt a culprit. |
| Converting RONI↔ONI with a fixed offset | **The offset is NOT constant — it has grown every decade.** See `DOSSIER.md`. |
| Quoting a composite into a record event | State the **n of same-amplitude analogues**; if n<5 say so. |
