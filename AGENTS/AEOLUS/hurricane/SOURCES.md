# AEOLUS · HURRICANE — verified primary sources

**Verified on 2026-08-13.** ⚠️ **What failed is recorded too** — an unverified URL in a sources file is worse than no entry, because it looks checked.

---

## NHC — the daily instrument ✅ verified 8/13

### Active storms (structured, best for a scripted check)
```bash
curl -s "https://www.nhc.noaa.gov/CurrentStorms.json" \
 | python3 -c "
import json,sys
d=json.load(sys.stdin)
print('active:', len(d.get('activeStorms',[])))
for s in d.get('activeStorms',[]):
    print(' ', s.get('name'), s.get('classification'), s.get('intensity'),
          s.get('latitudeNumeric'), s.get('longitudeNumeric'))
"
```
**Verified return (8/13): 3 active** — `Cristobal TD 30` (Atlantic, 38.6N 38.2W), `Hernan TS 35` (E Pacific), `One-C PC 35` (C Pacific).
⚠️ **Covers all basins** — filter by longitude/basin before calling anything "Atlantic."

### Tropical Weather Outlook — formation odds (the trigger instrument) ✅
`https://www.nhc.noaa.gov/gtwo.php?basin=atlc&fdays=7`
**Verified 8/13 08:00 EDT:** AL92 **80%/80%** (~1,000 mi E of the Lesser Antilles, *"expected to weaken by late Friday due to strong upper-level winds and dry air"*); AL94 **30%/50%** (SSW of Cabo Verde).
⚠️ **Read the DISCUSSION TEXT, not just the percentages.** On 8/13 the number said 80% while the prose said *weakening* — **the prose carried the El Niño shear mechanism and the number didn't.**
Text version: `https://www.nhc.noaa.gov/text/MIATWOAT.shtml` *(fetched 24.6 KB; percentages are in prose, so grep the body rather than a tag).*

**Trigger reminder: the C1 escalation line needs a GULF/FL system.** Deep-Atlantic Cabo Verde waves and subtropical fish storms do **not** fire it however high the percentage.

---

## SEASONAL OUTLOOKS — the revision clock

### CSU / Klotzbach ✅ verified 8/13
`https://tropical.colostate.edu/forecasting.html` *(160 KB, loads fine)*
Issues **early Apr / early Jun / early Jul / early Aug**. **Verified 2026:** initial forecast released **Apr 9**; **8/5 update HELD at 9/4/1** — CSU's 2nd-lowest August named-storm outlook ever.

### NOAA CPC seasonal hurricane outlook
`https://www.cpc.ncep.noaa.gov/products/outlooks/hurricane.shtml` — **May initial, early-August update.**
**Verified 2026:** **8/6 revised DOWN to 7-13 / 2-6 / 0-2, 75% below-normal** (from 55%).

⚠️ **BOTH August updates revised AGAINST an active season.** My pre-registered escalation line *"CSU or NOAA revise UP"* did not merely fail to fire — **it fired backwards.** Record revisions in both directions; a trigger that can only fire one way is not a test.

### ⚠️ ACE — INSTRUMENT GAP, DECLARED
**ACE is my Yellow/Orange/Red peril band and I do NOT have a verified live source for it.**
`https://tropical.colostate.edu/Realtime/index.html` returned a **6.5 KB near-empty shell** on 8/13 — likely a frame or JS-rendered page.
**Candidates to test next session:** CSU Real-time subpages · NOAA **AOML/HRD** seasonal summaries · Klotzbach's public postings.
> **Until a source is verified, do NOT quote an ACE figure.** The threshold row is live in `../CLAUDE.md` with **no instrument behind it** — that is the defect class where a registry names a concept the tooling can't resolve. **Closing this is the first job in this folder.**

---

## LOSS LEG (shared with `../wildfire/SOURCES.md` — same publishers)

| Source | Gives |
|---|---|
| **Gallagher Re / Munich Re / Aon** cat reports | H1 & full-year insured nat-cat vs 10-yr avg |
| **Artemis.bm** | reinsurance ROL, renewal pricing, cat-bond issuance |
| **Guy Carpenter** ROL index | the renewal-pricing series |

⚠️ **Commercial publishers on their own schedule** — H1 lands ~Jul-Aug, full-year ~Jan. **Between publications the loss leg is genuinely stale; label it rather than substituting a peril figure.**
⚠️ **NOAA NCEI's billion-dollar disaster DB was DISCONTINUED (Jul 2025)** — do not cite it (L-05).

---

## KNOWN TRAPS

| Trap | Guard |
|---|---|
| High formation % read as the trigger | **Trigger needs GULF/FL.** Graded on the letter twice this month. |
| Percentages without the prose | 8/13: **80% + "expected to weaken."** The prose had the mechanism. |
| `CurrentStorms.json` is all-basin | Filter before saying "Atlantic." |
| Active basin ⇒ hard market | **Peril ≠ loss.** Opposite directions right now. |
| Quoting ACE | **No verified source yet — see the declared gap above.** |
| A quiet season kills the thesis | It kills **C1's read only**; migrate to C3/C5/C6 and say so. |
