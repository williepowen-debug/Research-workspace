# AEOLUS — DATED CATALYST CALENDAR

**Purpose:** the fixed-clock events my channels resolve against. Weather's edge is that it resolves on a schedule (CLAUDE.md §PREDICTIONS) — this file is where the *scheduled* items live so they aren't rediscovered late. Read at boot alongside STATUS; check for any date within the next ~30 days and act.

**Created:** 2026-08-03 (first live read for C6/water — the Colorado River file Will assigned via WALTER 7/28). Owner: AEOLUS.

---

## 🔴 LIVE — Colorado River Post-2026 Operating Guidelines (C6 first live read)

The successor regime to the 2007 Interim Guidelines — governs Lake Powell + Lake Mead operations, shortage tiers, coordinated reservoir management, **for a 10-year period through 2036**. Behaves like a policy meeting, not a weather condition: named instrument, federal process, docketed deadlines, reprices allocations across 7 states + Mexico. **Nobody else in the fleet is carrying it as a calendar item** (WALTER checked DOCKET.tsv — no Colorado/Reclamation/Mead/Powell row).

| Date | Event | Status | Confidence |
|---|---|---|---|
| 2026-01-09 | Reclamation Draft EIS released | DONE | HIGH |
| 2026-01-16 | Federal Register NOA, 45-day comment opens | DONE | HIGH |
| 2026-03-02 | Comment period closed (>18,000 comments, 785 unique) | DONE | HIGH |
| **2026-07-31** | **Final EIS PUBLISHED + Federal Register NOA** — the previously-unknown date, now resolved | **DONE (verified vs USBR/DOI primary, this session)** | HIGH |
| **🔴 ~2026-08-30** | **Earliest legal ROD** (NEPA ≥30 days after Final EIS NOA of 7/31) | PENDING — next check window | MED-HIGH |
| **🔴 ~2026-10-01** | **Interior's stated target to sign Record of Decision** | PENDING — STATED TARGET, slippable (federal EIS processes slip routinely; DOCKET `SLID` state exists for this) | MED |
| **2026-12-31** | **2007 Interim Guidelines EXPIRE** — the hard backstop (a missed deadline is itself an event) | PENDING | HIGH |

**Preferred alternative in the Final EIS:** an "adaptive decision framework" through 2036; allows Lower-Basin shortages **up to 3.0 MAF** in dry years, **Arizona carrying the largest cut share**, California shielded at smaller shortage levels. Federally-framed rather than a fully-agreed 7-state deal — the Upper/Lower Basin split stayed unresolved into the final plan.

> ✅ **NUMBERS ADDED 2026-08-13 — this line previously said "I have NOT read the full alternatives" and stayed that way for 13 days.**
> **16–20% cuts for CA / AZ / NV through 2028.** Lower Basin (incl. Mexico) could lose **1.5 MAF in both 2027 and 2028**: **Arizona −760,000 AF · California −440,000 AF · Nevada −50,000 AF**. **Upper Basin (CO/NM/UT/WY): no mandatory reduction, voluntary conservation only** — note the asymmetry, since it is the Upper Basin's runoff that fills Powell.
> ⚠️ **Source layer is trade/news coverage of the EIS, not the document — B1 until pulled from the primary.** Grade the eventual ROD against these figures, not against a narrated-after-the-fact frame. → **KB-060.**
> 🔑 **Process note worth keeping:** I registered this dated instrument, tracked its date faithfully, and never read its contents — the gap surfaced only because Will passed me an outside post that was more specific than my own file. **Watching a catalyst's DATE is not the same as reading its CONTENT.**

**Transmission (multi-owner — reconcile to one figure, don't silo):**
- **Hydropower** — Glen Canyon (Powell) + Hoover (Mead) generation falls with head pressure → **WATT** (Powell ~32 ft above minimum power pool 3,490 ft as of 8/2).
- **Ag allocation** — shortage-tier delivery cuts to AZ/NV/CA/Mexico → **CARL** (food/ag), **MARCO** (SW municipal supply, Phoenix/Vegas growth, state fiscal).
- **Industrial/data-center water** — the third AI-capex siting constraint after credit + power → **VULCAN**.
- **Muni/ag-lending credit** where a tier touches property values → **REGINALD/CREED**.
- **NOT Florida** — do not import to CORAL.

**Next-check date: ~2026-08-25** (ahead of the earliest-possible 8/30 ROD). Watch for a Federal Register ROD notice or a Reclamation/DOI press release.

---

## STANDING SEASONAL / FORECAST CLOCKS (recurring — not one-off)

| ~Date | Event | Channel | Note |
|---|---|---|---|
| ~~2026-08-05~~ | ~~CSU (Klotzbach) seasonal hurricane update~~ | C1 | ✅ **DONE 8/5 — HELD at 9/4/1**, unchanged from 7/8. CSU's 2nd-lowest August NS outlook ever. **Escalation line NOT fired.** |
| ~~2026-08-06~~ | ~~NOAA August seasonal hurricane update~~ | C1 | ✅ **DONE 8/6 — revised DOWN** to 7-13 / 2-6 / 0-2, **75% below-normal** (from 55%). **Escalation line fired BACKWARDS.** |
| ~~2026-08-13~~ | ~~NOAA CPC monthly ENSO Discussion + ONI update~~ | ENSO/all | ✅ **DONE 8/13 — STEP-CHANGE.** Very-strong odds **81% → >90%** for NH fall/winter 2026-27. **NEW: 69% chance of a HISTORIC event exceeding every El Niño back to 1950 (+2.5 °C or more, 3-month RONI), OND 2026.** July Niño-3.4 +1.4 °C. **Delta routed to WATT and MARCO same day.** KB-053, VX-20. |
| **🔴 ~2026-08-20** | **CPC DJF 2026-27 seasonal temperature outlook** | C3/C2 → WATT, MARCO | **The highest-value dated item on this calendar, and today RAISED its value.** With a 69% historic-event probability, a **season-specific** forecast beats a composite by more than it did on 8/12 — there is no analogue set left to average. **Supersedes the composite reads in both 8/12 packets.** ⚠️ Attempted 8/12, extraction failed — classify **PUBLIC-AND-UNFETCHED, not unavailable.** **Owed to WATT and MARCO.** |
| **🔴 DAILY until it prints** | **Lake Powell all-time-low break** | C6 → WATT/CARL/MARCO | **~2-3 days out at the observed rate.** 3,520.37 ft on 8/12 vs the 3,519.92 ft record; falling every day since 7/29. `curl .../reservoir_data/919/csv/49.csv \| tail`. On the print: resolve **AEO-06 HIT**, **C6 → 4**, route. **Do not pre-fire.** |
| **🔴 2026-08-15** | **Panama ACP draft step-down 14.94 m → 14.78 m** | C5 | **AEO-04's instrument — unverified two sessions running; my oldest open gap.** Watch for any binding TRANSIT restriction (that, not the draft step itself, is what resolves AEO-04). |
| **2026-08-24** | **Brent >$85 sustain — grading check (MARCO's threshold, AEOLUS watching)** | C3-adjacent | Run began 8/10 (8/10 $87.72 · 8/11 $89.29 bars · 8/12 $88.71 front-month futures, provisional). Condition = **sustained >$85 for 2+ wks, graded on SETTLEMENTS**. ⚠️ **Label the instrument on every crude figure; basis is diverging (~$10 futures-vs-dated-spot) and BRENT rules the canonical instrument — do NOT re-adjudicate basis.** Packet MARCO either way. |
| ~mid-month | USDA NASS Crop Progress (weekly in season) | C2 | corn/soy G/E + drought monitor |
| ~2026-08-15 | Panama ACP draft step-down 14.94 m → 14.78 m | C5 | precautionary; watch for any binding TRANSIT restriction (AEO-04) |
| Sept–Nov | Lower Mississippi low-water season | C5 | normal now (Aug); the autumn window is where it would fire |
| 2027-01-01 | Property-cat reinsurance Jan renewal | C1/C4 | AEO-03 resolution (soft-market thesis) |

---

*Boot rule: if any 🔴 PENDING date is within ~30 days, it is a gap to check this session, not idle background.*
