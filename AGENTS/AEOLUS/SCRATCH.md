# AEOLUS — SCRATCH (next-session continuity)

**Purpose:** the single "pick up here" file. Read at boot (step 2), append a dated note at closeout (step 4). Keep the latest 3–5 entries; older detail belongs in STATUS history or `memory/YYYY-MM-DD.md`.

---

## ★ STANDING WILL DIRECTIVE (2026-08-03)
**Maintain first-class tracking on MAJOR RIVER water shortages — especially where they affect SHIPPING / TRADE.** Will confirmed C6 water stays inside AEOLUS (no standalone agent for now) AND named the river→navigation→freight nexus as a priority. Coverage split: **C5 = river NAVIGATION→freight** (Rhine, Mississippi/Ohio — the RED channel now; the "affects shipping/trade" leg); **C6 = water ALLOCATION** (Colorado reservoirs/shortage-tiers/hydropower). Keep a standing scan on the major navigable trade rivers: **Rhine, Mississippi/Ohio, Yangtze, Danube, Paraná** + Panama chokepoint. An empty river read is a gap to close (the #1 guard applies to this watch).
> ⚠️ **The two trade lines below are RESOLVED as of 2026-08-12 — read them as history, not as live instructions.** The pre-registered trigger **fired backwards** (CSU held 9/4/1 on 8/5; NOAA cut to 75% below-normal on 8/6) and the vehicle was **killed by TERRY on 8/4** (FL primaries have no options market). Card is **DEAD, $0 at risk**; successor **long RNR is pre-registered but UNARMED**. **Will's river/water directive above is UNCHANGED and still standing.**

**Trade posture (Will-agreed 8/3):** HOLD, no build now — reinsurance-landfall tail fights my own El-Niño-suppression base case (would bleed theta in a quiet season, no edge). Pre-registered BUILD trigger: **CSU 8/5 or NOAA ~8/6-7 revise season UP, OR NHC lights a Gulf/FL system** → the tail goes live (breaks the suppression thesis). C4 down-stack (property→muni/WUI) is the slower expression, REGINALD-owned (ZION the one weak name), not ready.
**★ STAGED 8/3 (Will-directed):** card handed to **TERRY** (inbox packet) — build unarmed/decision-ready: OTM Sep-Oct puts on FL primaries **UVE $44 / HRTG $30 / HCI $178** (clean solvency-convex shorts; NOT diversified reinsurers RNR/EG/ACGL/AXS — they V-shape on post-cat hardening). Gate = TERRY's options-liquidity/borrow/IV read on the small-caps (HRTG the risk). **PROME informed** (inbox packet) — tracking 8/5 + 8/6-7 as decision checkpoints. NEXT SESSION: check TERRY's liquidity read + whether either Aug update fired the trigger.

## 🔴 NEXT SESSION — START HERE (2026-10-10 12:37 ET, Will-directed: news sweep → El Niño winter re-point → Colorado → file hygiene)

*(Supersedes every earlier pickup block — all rotated verbatim, see the list at the bottom. The landfall record is KB-189 + `hurricane/`.)*

### THE ONE THING
**AEOLUS now points at the El Niño WINTER.** C3 → winter heating (CPC pop-weighted HDD; **band Will-ruled 10/10**: MidAtl+ENC 30-d HDD vs 1991-2020, DJF windows, Y ≥0 / O ≥+10 / R ≥+20). C2 → **southern Africa maize** (SA corn lead band Y ≤−15/O ≤−25/R ≤−45 vs 16,421 kt + Aus wheat second leg, **Will-ruled 10/10**; **AEO-13 65%**, resolves 5/12/27). **Composite 17/30** (C2 3→2 on 10/9, C3 3→2 on 10/10). KB-195…200.

### FIRST THINGS NEXT SESSION
1. 🔴 **Isaias loss leg:** first post-landfall modeler estimate (KCC/Verisk/Moody's RMS) → C4 >$10B leg (once) → CORAL with its perimeter. **DATE TRAP: 2020-Isaias KCC $4.2bn / RMS $3–5bn.** FEMA DR still pending (EM-3655 only).
2. 🔴 **Rhine 3-day re-grade** (WSV 10/10: no exit through 10/12). **Simon** landfall pressure vs the IBRD Mexico bond box (~932 mb).
3. 🔴 **10/15:** CPC long-lead winter outlook (vs the mild composite) · EIA storage · **October 24MS** (not out 10/10) → AEO-10, Mead 1,037.60 [10/9].
4. ✅ **Will ruled 10/10 (KB-205):** C6 leg 2 = **<1,010 while the Guidelines are in effect, else <1,000** (governing today: 1,000); milestone band re-keyed to **Jan 1, 2027** + *Nevada v. Burgum* (Yellow from **11/02**, Orange from **12/02** or a PI motion).
5. **TERRY** reply on the RNR late notice (price vs NO-BUILD). **10/27** SA CEC intentions + MWD board item. CSU final 10/14.

### DONE 10/10 (all committed + pushed)
News sweep (KB-191…194) · CORAL five-asks consumed · C3 re-point (KB-195/196, BRENT+WATT packets) · C2 re-point + NASS revived at ESMIS (KB-197…199) · bands ruled (KB-200) · Panama base rate (KB-201) · Colorado: LB agreement unsigned, Jan 1 2027, *Nevada v. Burgum*, 1,010 line (KB-202…204) · TRADE.md rows 1–5 + THESIS C2–C6 · RNR late notice to TERRY (L-47) · rotations: STATUS (×2), hurricane/water/wildfire DOSSIERs, SCRATCH — all crc-verified · L-47/48/49.
**Workers spawned 10/10:** C3 HDD scout · C2 regions scout · Colorado dated search · water SOURCES hot/cold split — each for a named owed item; regime/wildfire/seismic **not** spawned (no trigger; regime and wildfire refreshed 10/9).

### HYGIENE CARRIED
- **Observation home missing for the two new instruments:** CPC HDD (C3) and PSD crops (C2) have no domain folder/`SERIES.tsv` — numbers trace only to KB + `sources/` files. Decide where they live (charter SHARED-INPUT RULE: the folder that OWNS the instrument; a new folder + `LEDGER_GLOB` entry) **before the first graded C3 window, 12/30**, and before the 11/10 WASDE.
- `domain_log_check` keys on the LOG row DATE: a worker that dates rows by EVENT (regime 10/9) reads as "0 rows today" — add a run-dated row; consider keying the check on `pulled_at`.
- 🔴 **Before 10/22:** file AEOLUS's full boot manifest (charter reads + worker reads) and a `manifest-complete` ATTESTATION row in `PROME/registry/READS.tsv` — PROME added the two worker class rows (505d17cf3); `read_cap_check --agent AEOLUS` reads rc 2 until then. Read the file's header rules first; follow WALTER's attestation row as the model.
- **Worker read surfaces are invisible to `read_cap_check`** (L-49): measure `*/DOSSIER.md */SOURCES.md` each spawn session; **regime/DOSSIER 30 KB = 92%** — rotate at next touch; READS.tsv declaration flagged to PROME.
- Owed: C2 "cereals index breaking" level · C3 Henry Hub level (ask BRENT) · summer CDD re-spec before 5/1/27 · C5 long-series base rate 10/31 · seismic S-5 re-spec · Yangtze re-read (cjh.com.cn timed out).

---

---
### ⬇️ ROTATED — history lives in `archive/`
- `archive/SCRATCH_ARCHIVE_2026-10-10_10-9-block.md` — the 10/9 landfall-session block, verbatim (two lines in it are superseded — see its banner).
- `archive/SCRATCH_ARCHIVE_2026-10-10_pickup-blocks.md` — the 10/8 (×2) and 9/28 blocks, verbatim.
- `archive/SCRATCH_ARCHIVE_2026-09-28_pickup-blocks.md` — the 9/18 crash-recovery block + the 9/11 drain block, verbatim.
- `archive/SCRATCH_ARCHIVE_2026-08-27_pickup-block.md` · `archive/SCRATCH_ARCHIVE_2026-08-27_superseded-blocks.md` — earlier blocks.
- Recompute any receipt with `tail -n +7 <file> | python3 ../../PROME/tools/measure.py /dev/stdin` (the 8/27 archives use `tail -n +6`); never trust the banner.
