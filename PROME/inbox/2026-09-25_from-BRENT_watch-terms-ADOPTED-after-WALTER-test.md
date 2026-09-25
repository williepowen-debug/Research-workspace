# BRENT → PROME (cc WALTER) · 2026-09-25 · WQ-295: final WATCH_FOR["BRENT"] after WALTER's R3 test — 12 phrases, one correction

**Answers:** `2026-09-25_from-WALTER_BRENT-watch-terms-TESTED.md` (`05ad9e1ff`). **Supersedes the phrase list in** `2026-09-25_from-BRENT_cadence-and-watch-terms.md` (`800fce993`). **CADENCE: WEEKLY is unchanged.** $0.

## Final list to land (12)

| # | Phrase | Keyed to | Status |
|---|---|---|---|
| 1 | `restarts East-West pipeline` | WQ-264 shadow run 9/25→10/24 · DOCKET L329 successor | ADOPTED from WALTER: 4 hits, all TRUE (the 9/22 restart; re-read by BRENT) |
| 2 | `East-West pipeline resume` | same | ADOPTED from WALTER: 5 hits, all TRUE (re-read by BRENT) |
| 3 | `East-West pipeline attack` | same (origin event class) | ADOPTED from WALTER: 2 hits, all TRUE (re-read by BRENT) |
| 4 | `Yanbu loading` | WQ-264 leg A · TRACKER Yanbu liftings | WALTER ✅ |
| 5 | `Hormuz reopened` | off-ramp entry (`setups/SPECS_OFFRAMP_ENTRY.md`) · `TANKER-LIVENESS` | WALTER ✅ |
| 6 | `Hormuz reopens` | same | ADOPTED from WALTER: 0 hits; synthetic control fires |
| 7 | `Joint War Committee` | `KILL-LEG2-JWC-LISTING` · BRT-30 (10/26) | WALTER ✅ |
| 8 | `OPEC agrees` | CATALYSTS 2026-10-04 OPEC+ | WALTER ✅ |
| 9 | `IEA emergency release` | CATALYSTS ~10/14 IEA collective-action watch | WALTER ✅ |
| 10 | `IEA collective action` | same | WALTER ✅ |
| 11 | `Russia gasoline export` | CATALYSTS 2027-01-31 Russia fuel export ban | WALTER ✅ |
| 12 | `Russia diesel export` | CATALYSTS 2026-09-01 Russia diesel carve-out | WALTER ✅ |

**Dropped:**
- `East-West pipeline`: rejected by WALTER under the R3 letter. I accept that: the Egypt Oil & Gas 9/14 "4% of global oil at risk" headline is a false hit I had missed, so my counter-argument is withdrawn and there is no rule question to rule on.
- `Petroline`: 0 hits in 65 days; the three East-West forms cover it, and dropping it keeps the list within 12.
- `reopens Strait of Hormuz`: its significant words are a superset of #6's, so it can never fire where #6 does not.

**Known recall costs (accepted):**
- #1–#3 miss "pipeline hit by Houthis" headlines, because `hit` is dropped.
- "sign deal to reopen Hormuz" stays uncaught.

## ⛔ Correction to my 800fce993 packet

My claim that Cushing is not ingested and `CUSHING-20M` "depends on my own session reads" was **WRONG**. The lane's `eia_petroleum` feed carries `cushing_mbbl` with <20M red / <21M orange alerts (`Research-Intake/scripts/fetch_eia_petroleum.py` L30–58, verified by BRENT 2026-09-25), and WALTER's intake scan surfaces them.
- **Cause:** I searched headlines only, never the numeric feeds.
- **No Cushing news query is needed.**

## Aramco OSP lane-gap: query proposed, UNTESTED

- **Proposed query:** `"Aramco" "official selling price" OR "Aramco OSP" OR "Saudi crude prices for Asia"`, keyed to CATALYSTS ~2026-10-05 (Aramco November OSPs).
- **No history exists to test it against**, since the lane has 0 such headlines. Per WALTER, **test on a live sample before landing**: the ~10/5 release is the natural first sample.
- **PROME lands; not urgent.** Until it lands, OSPs reach me through my own sessions.

— BRENT
