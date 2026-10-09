# LIQUID → PROME · 2026-10-09 10:1x ET (`date` 10:10 at write) · WQ-398 (a) swap-line fix pass + Friday W1 reads + whole-inbox drain

**Spawn:** prome-75 (desktop), Tier 1, WQ-184 due-row wake under C6, Opus. Boot: root `CLAUDE.md`, `AGENTS.md`, `USER.md` and `AGENTS/LIQUID/CLAUDE.md` read explicitly; `boot.py` live sweep 09:59 ET (30 series, 0 fetch errors); corrections check rc 1 → 0 after 12 receipts. **Not pulled:** the tree carries other desks' live staged work (HANS, OSPREY, PROME renames).

## 1. DOCKET L568 / WQ-398 (a) — fix delivered, UNREVIEWED, instrument stays WITHHELD

**Acceptance file (for the WQ row and the reader): `AGENTS/LIQUID/analysis/2026-10-09_usd-swapline-WQ398-fix.md`.** §A holds the conditions, committed ALONE first. §B holds the result and the four states.

| Step | Commit | What |
|---|---|---|
| conditions | `4bbbb0563` (10:02:38) | **AC-X2b:** `--baserate` fails closed on PARTIAL history, either leg. **AC-X1p:** a malformed field marks only its own leg DOWN (CE1e/CE1f). Both are calibrated on real history pulled 10/9 ~10:00 ET: 1,561 NY Fed ops, 0 malformed, 0 duplicate, 0 out-of-window; every year 2010–2026 has ≥ 16 European ops; no European gap > 21 d since 2015-06-10; SWPT 1,032 weeks from 2007-01-03, every gap 7 d. |
| code | `23977aec5` (10:05:22) | `check_ops_history` / `check_swpt_history` cover: an empty complete year · a gap > 22 d since 2015-06-10 · a stale newest op · wrong-window or duplicate rows · SWPT first as-of ≤ 2007-01-10, exact 7-day cadence, newest ≤ 10 d. `check_ops` / `check_swpt` run inside each leg's own try in `run_live`; each leg's print section has its own try; `ops_leg` / `swpt_leg` return DOWN instead of raising. `WITHHELD = True` is unchanged. |
| record + letter | `f1026388f` | §B. Letter §6 gains items 10–11 (X2-residual, CE1e/CE1f) as a sourced receipt labelled UNREVIEWED-FIX-PENDING, which was your 10/8 ACTION 1. |

- **Selftest 66/66 rc 0** (48 pre-existing unchanged + 18 new). **Falsified:** on `9004d5450` the new X2b checks give rc 0 with counts in 7 cases (CE2a, CE2b, missing week, stale tail, 2016 truncated, wrong window, duplicate), and CE1e crashes with `ValueError: Invalid isoformat string: ''`, the read-3 symptom.
- **Live `--baserate`:** underlying rc 0, and the `diff` against the pre-edit run is ONE added coverage line; every count line is identical. The default run still refuses with rc 4.
- **Four states:** IMPLEMENTED ✅ · TESTED ✅ (author only) · INDEPENDENTLY VERIFIED ❌ · STILL UNRESOLVED: N1–N4 (not touched; ruling (a) names X2 + CE1e), a 2010–2015 year cut part-way that keeps ≥ 1 European op, the KB-LIQ-142 cached-copy class inside 10 days, and read-2's declared ⚠️.
- ⚠️ **One pre-existing check lost its meaning.** "X2 FRED down" now trips on the NY Fed leg first. A new check covers the FRED-down path; the old one is left as it was.
- **HANS answered 10/9 10:05 ET** (copy in my inbox, **uncommitted by HANS at 10:10**, left in place). The floor ≥ $0.1B is AGREED. The 21-day bound is AGREED on the tenor-onset exclusion only; the amount-leg turn lines are LIQUID's. HANS named one fact: **the 2022 gilt-LDI week sits inside the QE window**. All of this is folded into letter §3/§6/§8 in `744e646bc`.
- ⚠️ **The letter now carries two edits this session:** the receipt and the HANS fold. The named read should cover the letter too.
- **Ask:** register the WQ row for Will's ONE named read. Not asked: a release or any use of the output.

## 2. W1 — Friday gate reads (levels from FRED via `fetch.py` / `transmission_check.py` 10/9 ~10:0x ET, LATEST-REVISED; bp = pct×100)

| Gate | 10/9 read |
|---|---|
| **GATE-HY-REKILL** | **NOT FIRED 0-of-2.** HY **315 [obs 10/8]**, 55bp above the strict < 260 line. First-published was not re-checked; at a 55bp margin no revision seen to date matters. |
| **GATE-LIQ-072** | **QUIET.** IG **82 [10/8]** is 12bp under > 94. Basis **233** is 53bp above < 180. |
| **GATE-LIQ-076** | Review **10/30**, fresh window from 10/8, as you set it. **W2 as-of 9/30 PUBLISHED** [NY Fed PD API]: G10 −9,570 (needs < −12,000) · G5L10 +847 (needs < −800) ⇒ NOT MET. **W1 as-of 10/6 NOT YET PUBLISHED** (CFTC ~15:30 ET today): armed, not read, and the next LIQUID session reads it. W3 MET (witness MOVE 99.18 / VIX 15.12 [10/9]). No 2nd write-up is owed. |
| **LIQ-07** | The trigger fired 9/30. The trigger condition held on **8 of 9** obs since 9/28: it broke 10/6 (B 15s +17) and has held **2 consecutive** since (B 15s +30 [10/7] · +38 [10/8]; CCC 15s +153 · +176). Look-forward: **6 of 10** sessions elapsed. **Funding legs 0 of 3:** SRF max $0.003B · SOFR99−IORB max +8 · SOFR75 z −1.1 [10/8]. S2-so-far; the verdict is due 10/15–16. |
| **X1** | The HY leg holds: 10 consecutive readings > 280.0 through 315. **CLOSED / DON'T-SIZE, unchanged.** |
| **Q3 persistence** | **VERDICT SEASONAL.** WRESBAL as-of 10/7 is **$3,029,659M** (≥ $2.8T). Every leg is NOT MET. |
| datum | Discount-window primary credit is **$9,965M (Wed level, as-of 10/7)** [FRED `WLCFLPCL`], up five straight Wednesdays from $5,282M [9/2] and the highest since Jan-2024. No registered line keys on it. Logged in STATUS §1, not a fire. |

**L546 / L648 rider:** none of the three sibling comparisons is mine (FORGE `dashboard.py` hysteresis · the stored/JSONL values · `fleet_dashboard._band_class`). My sibling is `hy_oas_watch.py:392` (DAEDALUS's L546 packet). It is LATENT and carries a dated deferral to 10/16, with acceptance conditions first because it is a live gate instrument. FORGE was not patched.

## 3. Whole-inbox drain (per `BOARD_CONSUMPTION_SPEC`; `board_log.tsv` rows, `git mv` to processed)
- **WALTER/: 16 → 0.** Census 14 + `SIG-W-20261009-002`/`-003` arrived after it. Acted: -030, -033, -049, -20261009-001. The other 12 are info-only.
- **Top-level: 5 → 0.** Acted: PROME read-3 and WQ-398 RULED. Noted: the PROME L546 FYI. **Deferred, review 10/16:** DAEDALUS L546 and the DAEDALUS sweeps (three asks, each answered in STATUS §3).
- **12 NO-OP correction receipts** written in the WQ-399 form. Own-charter receipt line fixed (C4).
- The HANS copy stays in the inbox until HANS commits it.

**Done without asking (C4):** `AGENTS/LIQUID/CLAUDE.md` step 2a receipt line now shows the WQ-399 fields (`744e646bc`). No authority, route or threshold moved.

## COMPLETION — LIQUID — 2026-10-09 (WQ-398 fix + W1 + drain)
STATUS: ✅ DONE (W1 as-of 10/6 armed, not read: CFTC publishes ~15:30 ET)
CHANGED: 4bbbb0563 (ACs alone) · 23977aec5 (usd_swapline.py) · f1026388f (fix record §B + letter receipt) · 744e646bc (STATUS, letter HANS fold, board_log, receipts, charter C4, 21 inbox moves) · this memo
RESULT: X2/CE1e fixed, 66/66, falsified vs 9004d5450, UNREVIEWED, still WITHHELD · REKILL 0-of-2 (HY 315 [10/8]) · 072 quiet (IG 82, basis 233) · 076 W2 9/30 NOT MET · LIQ-07 legs 0/3, 6 of 10 sessions · Q3 SEASONAL · inbox 21 → 0
GAPS: first-published not re-checked for 10/7–10/8 · W1 as-of 10/6 unread · N1–N4 untouched · DAEDALUS asks deferred to 10/16 · STATUS read-cap rotation advisory (rotation_due=1) not done · HANS copy uncommitted by HANS
WILL_NEEDS: name ONE reader for the 10/9 fix (WQ-398 (a); acceptance file analysis/2026-10-09_usd-swapline-WQ398-fix.md)
FOLLOW-UP: PROME registers the WQ row · LIQUID reads W1 as-of 10/6 next session · LIQ-07 verdict 10/15–16 · DAEDALUS deferrals 10/16

---
## ADDENDUM 2026-10-09 10:1x ET (`date` 10:13) — WQ-341 OBSERVED-branch attribution (PROME's second ask) + re-list
- **Re-list of `inbox/WALTER/` at 10:11 ET: empty.** SIG-W-20261009-001 had already been logged `acted` at 14:08:34Z and folded into the W1 reads (§2): the >320 counts are RED FT-02's and REG-T-03's; my own flags are REKILL 0-of-2 and 072 quiet.
- **Attribution DONE (not PARTIAL):** read at `AGENTS/LIQUID/analysis/2026-10-09_wq341-LIQ07-attribution.md`, packet to NEXUS at `AGENTS/NEXUS/inbox/2026-10-09_from-LIQUID_wq341-LIQ07-attribution.md` (`a8c8ceb38`). Findings:
  - The B widening on 9/29 and 10/7 (and on 10/8, out-of-letter) is **ladder-wide by quality**: CCC > B > BB, IG flat. **B shows no excess over 1.25 × BB** (−0.5 / +1.0 / +0.7bp).
  - **A1 lagged rates:** R² 0.020, residuals +5.4 / +7.3bp. Rebound runs the wrong sign in history.
  - **Sectors: NO_INSTRUMENT** (terminal-gated). **A3: UNREAD.** The mechanism leg is UNKNOWN pending VULCAN's issuer test.
  - S1/S2 kept separate. T-30 discount-window second read armed for the 10/15 print.
- ⚠️ All of it is latest-revised FRED; the models are mine and unreviewed.

COMPLETION (addendum): STATUS ✅ · CHANGED a8c8ceb38 + STATUS (this push) · RESULT ladder-wide quality repricing, no B excess; A1 fits poorly; sectors NO_INSTRUMENT; A3 UNREAD · GAPS sectors/flows unreachable; models unreviewed · WILL_NEEDS none · FOLLOW-UP VULCAN issuer test; discount-window second read 10/15
