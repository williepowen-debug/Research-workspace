# FROZEN 2026-09-22 — HEARTBEAT twentieth re-base PLAN v2, DELIVERED `dbaaa7230`; every figure below is pre-re-base history, not current

**Author:** PROME (`prome-b7`) · **v1 written** 2026-09-21 22:0x ET · **v2** 22:1x ET after the blind plan read.
**Will's word:** "Okay go ahead" 2026-09-21 22:03 ET.
**Reviews folded:** CATO `762b015bc` + `7c025c804` · blind cold read of v1 (**18 ✅ / 13 ⚠️ / 10 ❌ — verdict NO**), ledger at
`/tmp/claude-1000/-home-willi-Research-workspace-PROME/618256cf-0e9f-4c0e-9f1b-c7da046a0274/scratchpad/coldread_plan.md`.
> ✅ **DELIVERED 2026-09-22 09:37 ET — `dbaaa7230`. THIS FILE IS THE PLAN RECORD; ITS FIGURES ARE PRE-RE-BASE HISTORY, NOT CURRENT.** Every `32,315 B / 99%` below describes the NINETEENTH base, preserved verbatim at `PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_2026-09-22.md`. **The delivered twentieth base measured 21,882 B = 67% of budget**, and the closeout gate reports `rotation_due=0`. ⚠️ The byte table below is the SENSITIVITY ANALYSIS that argued the plan was marginal; the candidate beat it because the channels were REWRITTEN rather than trimmed. **Read it as the reasoning, never as the outcome.** The blind RESULT read then returned 8 BLOCKING against the written base — including a preserved-but-discharged caveat this plan had made invariant #1 — all fixed before commit.

**v2 fixes all ten ❌. The thirteen ⚠️ are declared residue (bottom), unfixed by rule (WQ-178: fix ❌ only).**

⛔ **v1's central arithmetic was wrong and v2 supersedes it.** See § Byte feasibility.

---

## Why an early re-base (chain is 1, not >~5)

§C's re-base trigger is a FLOOR ("re-base by"), not a ceiling. Two independent obligations force it:
- **§C update rule:** *"Update after regime-level changes or >48h stale in a market week."* Base written Sat 9/19 ~11:2x ET; 58h; equity-vol gamma sign flipped (regime-level).
- **P1 read-cap** [SUPERSEDED — delivered base is 21,882 B]: 32,315 B = 99% of the 32,550 B budget. **Stop is <70% = 22,785 B.** Any amendment breaches.

⛔ This file was burned once reading an advisory as a prohibition ("amendment #4 BARRED", retired in the 19th base). Reading "not yet due" as "not allowed" is that error inverted.

## Byte feasibility — v1 WAS WRONG (❌B4)

v1 assumed all eight channels land at exactly 600 B. **Cold §R.2 L126/L204 records a PRIOR re-base landing at §1 880 · §2 806 · §3 765 · §5 713 · §7 784 — mean ~789.** The 600 B target has never been hit. v1 also budgeted **no ADDITIONS row**, and this base adds content (9/21 levels, retired-kill rewrites, the new invariants, the §7 cold pointer).

| channels land at | channel recovery | other levers | gross | vs 9,530 required |
|---|---:|---:|---:|---:|
| 600 B (v1's assumption) | 6,882 | 4,444 | 11,326 | +1,796 |
| 700 B | 6,082 | 4,444 | 10,526 | +996 |
| **780 B (historically achieved)** | **5,442** | **4,444** | **9,886** | **+356** |
| 880 B | 4,642 | 4,444 | 9,086 | −444 |

**ADDITIONS, realistically 600–900 B ⇒ at the historically-achieved 780 B/channel the candidate lands 244–544 B SHORT.**

### ⇒ MANDATORY FALLBACK, and it is an EXISTING rule, not a new mechanism
The kill-on-sight hot cell's own text reads: *"the FULL binding set is cold `§KOS` + `§KOS.2` (every entry still binds). **THIS CELL = what binds THIS WEEK**."* Entries demonstrably older than the week of 9/21 are in it. **Pruning the hot cell to its own declared scope unbinds NOTHING** — the full set remains binding at cold. That is the rule as written, and it is the fallback if the measured candidate misses <70%.
⛔ Still no NEW rotation rule for either list (CATO's constraint, WQ-229's "prefer an existing control").

**ACCEPTANCE IS THE MEASURED CANDIDATE, NOT THIS TABLE:** `python3 PROME/tools/measure.py HEARTBEAT.md` must read **< 22,785 B** before commit. If it does not: apply the fallback, re-measure, and if it still misses, **STOP and report — do not ship an over-budget base and call it done.**

## PREREQUISITE before any cut (❌B8)

**§7 is 2,892 B and carries live corrections that exist NOWHERE ELSE** — not in §KOS.3, so invariant 9 does not reach them:
*"that phrasing is DEAD"* (mil.ee + ERR/LSM/LRT are broadcasters, **not** three defence ministries) · *"CONTAMINATED ≠ LOW"* · the CATO narrowing that retired *"FUNCTIONALLY SUPERSEDED"* · *"HANS'S CAVEAT, WHICH TRAVELS IN SUBSTANCE"* (not-priced ≠ not-happening).
⇒ **Write §7's long-form to `PROME/HEARTBEAT_COLD.md` §20.7 FIRST, verify each correction is present there, THEN cut the hot cell.** Same test for any channel whose long-form is not already in cold. A cut that outruns its cold write drops a live correction.

## INVARIANTS — each must survive, in substance, in the HOT file

1. ⛔⛔ **VOID — DO NOT APPLY. This invariant was WRONG WHEN WRITTEN and it is the session's worst defect.** It read *"`GLD 16` / `TBT 14` are DISPUTED, not current — marker ON the position line itself"*. **The dispute was DISCHARGED on 2026-09-20 by WQ-272** (ANVIL write-in, Will-authorized); the correct quantities are **GLD 17 / TBT 10**. Preserving it forced a dead caveat into a 9/22 file. **What survives is the narrower WQ-274 caveat: not transaction-reconciled, not current-book-verified.**
2. Position mirror vintage **9/10 CLOSE**, STALE between exports; **re-verify the live book at any fire-time (root rule #4)**.
3. **WQ-192 STAND DOWN holds.**
4. **$0 moved by PROME.**
5. **004 add-gate: NO ADD**, four grounds → cold §B.1. DFII10 is THROUGH the 2.50 line.
6. **`GATE-TERRY-007` 0-of-5**; a NEW 5-streak must BEGIN by **Tue 9/22** or the 9/30 expiry moots it (L267).
7. **VLO 1 of 3 filled by Will's hand, 2 STAGED, card RE-ARMED**; kill-on-sight *"the day-colour gate bars Will's VLO order"* STAYS LIVE.
8. **Energy sleeve = USO 37 sh, 100% UNDEFENDED, no exit rule (WQ-200).**
9. **Kill-on-sight:** hot cell = what binds THIS WEEK; full set at cold §KOS/§KOS.2/§KOS.3; **every entry binds EXCEPT those this base RETIRES BY NAME in §Retirements below** (❌B2).
10. **HENRY's board is INTRADAY 15:1xZ, shelf ONE SESSION, only 14d walls publishable** (35d degenerate put==call==8,000), **re-measure at the official close OWED**. ⚠️ Its spot input SPX 7,722.38 is **42.3 pts below** the 9/21 close of 7,764.70.
11. **BRENT's $103.87 is SETTLE-basis, SINGLE-VENDOR; L430's second-vendor test NOT RUN.**
12. Every level carries a date.
13. 🆕 **(❌B1) THE DATE-CONVENTION LEGEND SURVIVES IN THE HOT FILE** — `[9/18c]` = that CLOSE · `[9/17]` on a FRED series = that OBSERVATION date · `[wk-9/11]` = EIA week ending · `[eff. 9/17]` = administered-rate effective date · `[9/18 10:21]` = an intraday print with its clock · vendor day-changes labelled "vendor". **Cold §D.2's own header says the hot file keeps TWO clauses in the room: owner-surface precedence AND the intraday-bar warning.** ⛔ Without the legend, invariant 12 is satisfied in form and void in substance.
14. **HEARTBEAT is DERIVED.** On conflict the owner surface wins (GATES · DOCKET · WILL_QUEUE · owner KBs · Will's rulings).
15. 🆕 **(❌B5) `GATE-REG-T02` IS NOT A LIVE LINE and must not be watched as one** — RESOLVED/FIRED 9/1, terminal, consumed by ROLL70 9/2. **A close below $78.00 is a SUPPRESSED RE-ENTRY, not a fresh fire.** ⚠️ Live this week: WAL closed **78.65 [9/21c]**, 65¢ above.
16. 🆕 **(❌B6) The open-position clock survives:** 004 TLT Sep-30 77P ×20 — **7 sessions to expiry from Tue 9/22** (9/22·23·24·25·28·29·30) · **TLT Oct-16 82P ×2 has NO RULING ON FILE** · `GATE-TERRY-ROLL70-EXIT` 0-of-3, WAL ≥$81.90 ×3.
17. 🆕 **(❌B7) The gate's chain anchor keeps its EXACT matched form.** `prome_gate.py:884` matches `^\*\*Amendments append.*?Chain:\s*(\d+)`. Its own docstring: the check was BLIND from the 7/31 re-base because a heading-format change disarmed it — **a re-base is the event that broke it before, and lever 6 rewrites this header.** Verify `prome_gate` reads **chain 0** on the new base before commit.
18. 🆕 **(❌B8) §7's named corrections survive** (listed under PREREQUISITE), in hot or verifiably at cold §20.7.
19. 🆕 **(❌B10) THE BRENT TILE ORDERING.** `fleet_dashboard.py:478-492` strips `(...)` and `` `...` `` then takes the **FIRST numeral after the `Brent` token**, once per tile. Today's file survives only because the level precedes the caveat. ⇒ **the publishable figure must come FIRST in the Brent cell.** Expected parsed value after the edit: **103.87**. ⛔ Verify by RUNNING the dashboard, not by reading the line.

## §Retirements — kill entries this base retires BY NAME (❌B2)

- ⛔ *"ANY Brent November level dated 9/18"* → **RETIRED.** Superseded by BRENT's L430 adjudication: **$103.87 settle-basis, SINGLE-VENDOR, is publishable**; any OTHER 9/18 November level is not, and the second-vendor test stays owed.
- ⛔ *"the call wall is 7,700 — 7,700 is the 14d CALL LEVEL"* → **RETIRED.** HENRY's 9/21 board publishes **call 7,750 / put 7,700 (14d)**. The successor kill is *"the 35d walls are publishable"* — they are not (put==call==8,000, degenerate).
- ✅ *"the negative-gamma squeeze is building"* → **STILL BINDS, and harder**: the board is now POSITIVE.

## ❌B3 — v1's Brent reasoning was WRONG and is withdrawn

v1 claimed tonight's 68¢ dispersion (`$100.38` 20:26 ET · `$101.06` 22:0x ET) was a **"THIRD distinct shape"** because both reads were post-settle. ⛔ **Refuted by the file v1 cited:** `HEARTBEAT.md` L66 records the 9/18 reads as **`$103.08 [16:3x]` and `$103.21 [21:2x]` — both ALSO post-settle** (settle ≈14:30 ET), 13¢ apart. **v1 conflated read TIME with value BASIS.** A live/last-price read is not a settle-basis read whenever it is taken.
⇒ **Corrected:** tonight's dispersion is **the SAME mechanism BRENT already adjudicated**. The settle-basis read for 9/21 is tomorrow's daily bar. **Conclusion unchanged — publish NO 9/21 Brent November level — but it does NOT route BRENT's adjudication and must not be reported as a new finding.**

## Data the new base stands on

**9/21 closes [yfinance, single-vendor]:** SPX 7,764.70 (+1.49%) · QQQ 741.47 (+2.77%) · SPY 773.50 (+1.55%) · TLT 81.80 (+0.68%) · GLD 398.38 (−0.70%) · USO 148.16 (−3.68%) · XLE 62.46 (−2.88%) · VLO 393.27 (−4.84%) · TBT 38.60 (−1.35%) · CRMT 1.65 (−5.17%) · WAL 78.65 (+0.14%) · KRE 71.99 (−1.04%) · OZK 47.75 (−0.27%) · VIX 14.87 · VVIX 85.77 · MOVE 81.20 · ^SKEW 142.19 (−3.99%) · GCZ26 4,383.80 (−0.93%) · CLX26 92.86 (−3.35%) · CLV26 96.19 (−4.10%) · DXY 100.45
**H.15 [9/18 cells]:** DGS10 5.01 · DFII10 2.68 · DGS2 4.76 · DGS30 5.34 · 2s10s 25bp · T10YIE 2.34 [9/21, same-day series]
**Credit [9/18]:** HY OAS 268 · CCC 1,083 · IG OAS 77 · WRESBAL $3,013.8B [9/16] · Claims 196K [w/e 9/12]
**Funding — ❌B9 FIXED:** v1 wrote *"SOFR 3.85 · IORB 3.90 [eff 9/22] ⇒ −5bp"* under a [9/18] header, pairing a 9/18 rate with an effective date **in the future**, reproducing the exact defect the file kills (*"the −28bp mixed-date figure is DEAD"*). ⇒ **State SOFR 3.85 [9/18] against the IORB effective ON 9/18, and label the basis; do not cite a forward effective date.**
**EIA UNCHANGED, next WPSR 9/23:** Cushing 21.482M · SPR 284.957M [both wk-9/11]

⚠️ **`GATE-LIQ-072` consumer read, NOT a grade (LIQUID owns it):** state cell carries *"IG OAS 79 [7/15]"*, 68 days stale. Live **IG OAS `BAMLC0A0CM` = 77 [9/18]**, 17bp under the >94 trigger. ⛔ **BBB OAS `BAMLC0A4CBBB` is 94 [9/18] and is a DIFFERENT SERIES** — the near-name is the trap; do not read the trigger as met.

## What CHANGES from the 19th base

| § | 19th base | 20th base | source |
|---|---|---|---|
| 5 | sign NEGATIVE 4th session, GEX −$9.9B/−$12.1B, no wall publishable | **sign FLIPPED POSITIVE**, +$33.7B/+$41.2B, flip ~7,669 both horizons, 14d walls publishable | HENRY `59b96cfd2` · `AGENTS/HENRY/STATUS.md` |
| 1 | ⛔ no Brent Nov level for 9/18 | **$103.87 SETTLE, SINGLE-VENDOR**; 2nd-vendor test owed | `PROME/inbox/2026-09-21_from-BRENT_L427-graded-L430-adjudicated-walter-batch-processed.md` |
| 1 | `CL=F` mislabels its month | **rolled to Nov ~9/18–21, six days early**; `MKT-CL-F-ABOVE-100` un-fired on BOTH real contracts | same BRENT packet |
| 7 | CRMT feed SILENT | **THIRD BRIDGE, accepted 9/18 20:05Z, STD 9/18→9/24**; silence grade false ~**4h** later | BROCK `4456d4115` |
| 2 | DGS10 4.94 [9/17], 44bp; DFII10 2.61, through by 11bp | **DGS10 5.01 [9/18], 51bp**; DFII10 **2.68**, through by **18bp** | FRED H.15 |
| 3 | HY 270 [9/17] | **HY 268 [9/18]**, re-arm 12bp / re-kill 8bp 0-of-2 | FRED |

**Also:** `GATE-FALCON-001` review_by **9/21**, last_checked **9/14** — not graded today. FALCON's last commit is **9/17** (`61aeeb218`), not 9/16; its spawn class is **ACTIVE on either date**, so this is a stale gate review, **not** a mis-spawn.

## RESULT-stage obligations

- Reset the amendment projection in `PROME/HEARTBEAT_DASHBOARD.md`.
- **Run** `fleet_dashboard.py`; confirm the Brent tile parses **103.87** (invariant 19) and channels/levels render.
- **Run** `prome_gate.py`; confirm the chain check reads **chain 0** (invariant 17).
- `measure.py HEARTBEAT.md` **< 22,785 B**, else fallback, re-measure, else STOP and report.
- Snapshot the 19th base verbatim; receipt = the git object, never a hand crc.
- Blind RESULT cold read before commit (§C + WQ-178).

## DECLARED RESIDUE — RESULT read, 2026-09-22 (added on ARGUS's finding that it was never declared)

The RESULT cold read scored **18 ✅ · 8 ⚠️ · 8 ❌**. All eight ❌ were fixed before commit. **The eight ⚠️ are carried UNFIXED and are listed here rather than summarised, because WQ-178 requires each un-fixed flag named:** they are basis-and-pointer class — source labels cited without a sha, an unmetered-target wording, the `§20.7` heading using `##` where cold's sub-parts use `###`, masked-minute stamps, a self-describing byte figure in the base's own header, commit-subject length, duplicated stable commands, and the combined `§4.2 / §5.4 / §6.2 / §7.3` heading form. **None changes what the file asserts.** Full bodies: the reader's ledger at the scratchpad path in this file's header. ⚠️ **That path is temporary** — the ledger does not survive the session, which is itself a residue item.

## DECLARED RESIDUE — the 13 ⚠️ from the plan read, NOT fixed (WQ-178: fix ❌ only)

Carried deliberately. The plan read's ⚠️ class covers basis-and-pointer items: source labels without shas (two now fixed above as a side effect of the ❌ work), unmetered-target wording, and pointer-form advisories. They do not change what gets built. Full list in the reader's ledger at the scratchpad path in the header.

## Out of scope

- `spawn_list.py` naming-pattern repair → **DOCKET L455**, acceptance conditions written, CATO's instruction to keep it separate honoured.
- Any new rotation rule for the kill cell or the stress-dashboard line.

---

## Post-delivery correction pass — 2026-09-23 (`prome-da`, desktop), on CATO's closure review

The source is `AGENTS/CATO/runs/2026-09-21_2147_heartbeat-rebase-proposal-review.md` § September 23: H3 (VIOLET pointer; census), H8 (tile dates) and H2 (reader evidence). The pass was bounded; no level was refreshed.

- **H3 VIOLET:** hot now names **L278** (leg 2). The 9/23 close resolves it and VIOLET's owner read is 9/24. The −16.26% is dated **[9/18 close, VIOLET STATUS]**. Verified at `AGENTS/VIOLET/STATUS.md:21,93`, DOCKET L277/L278, and the prereg letter §LEG 2.
- **H8 tile dates:**
  - HY/CCC/IG each carry [9/18].
  - VIX/VVIX/MOVE/^SKEW each carry [9/21c; yfinance, NOT settle-confirmed], so the caveat travels with every level.
  - Cushing/SPR each carry [wk-9/11].
  - Production `parse_tiles()`: HY 9/18 · CCC 9/18 · VIX 9/21c · Cushing wk-9/11 (MOVE gains 9/21c). Values are unchanged.
  - DGS10/WAL/OZK remain undated. That limitation pre-dates the re-base and is outside H8.
- **H3 census / H2 ledgers:** the original census and both reader ledgers are SEARCH-NOT-FOUND on this machine. The limitation is retained. A **RETROSPECTIVE** census is at `PROME/reports/2026-09-23_heartbeat-20th-rebase-RETROSPECTIVE-obligation-census.md`. It found one binding kill entry lost (*"Brent fell 7.5% in three sessions"*), now re-homed to cold **§KOS.4**, which the hot pointers now name.
- **Deferred, unchanged:** the Brent distance tile (L359) and channel-summary truncation.
- **Independent result read (`hbcorrread`, Opus, 2026-09-23):** items 1–3 MET; item 4 PARTIAL on ❌ **X1**. The first §KOS.4 re-home carried §A21's older text, which publishes −4.48%/−5.20% fade figures against $103.10, a killed 9/18 level. That inverted the binding "PROME publishes NO replacement percentage" caveat. **Fixed in one pass:** §KOS.4 now carries the 19th-base bracket verbatim. The same pass restored the Cushing "next WPSR 9/23" cue (W2) and narrowed the header note (W5).
- **Declared residue (WQ-178):**
  - W1: the tile stamp cuts at `;`, so the MOVE/VIX tiles show "9/21c" without "NOT settle-confirmed". The full caveat is in the hot text; this is a renderer limit, deferred with the truncation class.
  - W4: HEARTBEAT is 22,552 B, leaving 233 B of headroom to the 22,785 B stop line. Re-check at any append.
  - W3 was tested by the reader and found no loss: HANS-T-15 is carried at cold §19 and HANS STATUS.
