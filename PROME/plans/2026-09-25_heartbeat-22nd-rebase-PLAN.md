# HEARTBEAT twenty-second re-base — PLAN (PROME `prome-2e` leg 3, Fri 2026-09-25 ~17:3x ET, POST-CLOSE)
**Candidate:** the session scratchpad `hb22/HEARTBEAT_candidate.md` (installed as `HEARTBEAT.md` only after the plan read); **cold append:** `hb22/COLD_append.md` → `PROME/HEARTBEAT_COLD.md` (§22.1 · §22.2 · §22.3 · §22.7 · §KOS.6). Prior base: the twenty-first base (`73049da27`) + its amendment #1 (`342b0319c`); snapshot at install. *(❌7 fixed: v1 cited `761d93a2c`, a commit that never touched HEARTBEAT.md.)* Process: WQ-178 — ONE blind PLAN read (this file + candidate + cold append), fix ❌ only, install in one pass, ONE RESULT read on the installed file, declare ⚠️ here.

## Why now
The twenty-first base (post-close 9/24) + am.#1 (pre-open 9/25) stood AT its rotate line (`measure.py`, 74.998% of 32,550 — a hair under the ≥75% line) with five amendments queued on SCRATCH (⑪ HANS/WQ-294 · ⑫ intraday F1/crude · ⑬ HY 280 · ⑭ rigs/COT/VLO grade · ⑮ BG-02 lapse). §C's update rule met on the REGIME limb — regime-level moves in one session; the time limb is NOT met (~20h since the 21st base at ~21:4x 9/24). *(❌6 fixed: v1 claimed ">24h".)*

## Data the new base stands on (every figure dated; sources at the artifact)
- FRED CSV endpoint 17:0x ET: DGS10 5.18 · DFII10 2.85 · DGS2 4.87 · DGS30 5.47 · T10YIE 2.33 · HY 2.80 · CCC 11.12 · IG 0.79 · BB 1.64 · B 2.86 · SOFR 3.88 [all 9/24] · IORB 3.90 · WRESBAL 2,930,193 [9/23] · MORTGAGE30US 7.03 [9/24].
- `fetch.py price` 17:0x ET 9/25 (closes): SPY 771.35 · QQQ 744.50 · ^GSPC 7,743.41 · GLD 393.41 · USO 148.33 · XLE 62.04 · VLO 387.18 · TBT 40.91 · CRMT 1.06 · HYG 77.86 · HBAN 15.64 · AAPL 341.07 · APD 281.76 · ^VVIX 87.84 · ^SKEW 146.04 [9/24 ⚠stale] · TLT 79.32 · KRE 71.55 · WAL 77.61 · OZK 46.89 · APO 121.69 · VIX 14.87 · MOVE 96.00 · USD/JPY 157.18 (dashboard.py 21:03Z). Futures vendor day-reads (NOT settles): BZX26 104.41 · BZZ26 97.50 · CLX26 92.46 · HOX26 4.58 · GCZ26 4,321.50.
- Owner grades today: TERRY c6fd6dda6 (VLO-SCALE) · BRENT 72ac567ab (BRT-26, COT #7) + BG-02 lapse (STATUS L83, push pending) · LIQUID a969486fd · BROCK cae55b4c3 · HANS 6c46eb0ae · HAWK 42ce71cc6 · DAEDALUS 636eacb76 · WALTER cc9c14017 · HENRY 9/24 catch-up · SAM 9/24 + WALTER 9/25 (USD/JPY 157.05 back under) · VIOLET 9/24 post-close · MIDAS 9/25 re-base.
- Rulings today: WQ-294 (HANS spawn) · WQ-297 A · WQ-298 approved; registered: WQ-296 · WQ-297 · WQ-298.

## What CHANGES from the twenty-first base (+ am.#1)
1. Header: twenty-second, chain 0, folds am.#1 + ⑪–⑮; size clock 2026-10-02.
2. One-liner rewritten: HY 280 AT the line · real 2.85 · France fired · VLO F1 UNKNOWN · BG-02 LAPSED · concentration RULED A.
3. §1: BG-02 LAPSED replaces "grades 17:00"; publishable Brent = BRENT's 9/24 settle-proxy $106.60 (was $99.25 [9/22] + "9/24 NOT PUBLISHED"); rigs 455 / BRT-26 CONFIRMED; COT #7 NOT-SPENT; F1 UNKNOWN.
4. §2: 9/24 cells; 004 at the close; T12S anchor 2.85; WQ-291/FORUM-7.
5. §3: the 280 touch with the letters and the two desks' reads; BRK-R2 FIRED.
6. §4: yen back under the level; §5: 9/25 vol; §6: Oracle CDS/Blue Owl; §7: France fire, IEEPA VOID, CRMT $1.06, L433, HAW-19/WQ-296, Brightline; §8: gold/DFII10.
7. Book: WQ-297 A line NEW; 004 clock 3 sessions; VLO-SCALE 9/25 cell; sleeve $5,488.
8. Stress dashboard: 9/25 closes, 9/24 officials; Brent cell leads with **106.60**.
9. Thresholds: BRK-R2 FIRED in; COT #7; closest lines incl. HY AT the line, F1 UNKNOWN; calendar 9/28→10/2.
10. Pointers/KOS: new applicable entries (F1 direction, HY "re-armed", BZ=F roll, concentration); retirements by name; demotions to §KOS.6.

## INVARIANTS — each survives, in substance, in the HOT file (the 21st plan's 1–24 carried; changes marked)
1. DERIVED; owner surface wins; date legend survives (now `[9/25c]` · `[9/24]` · `[wk-9/18]` · `[w/e 9/19]` · `[eff. 9/24]` · vendor clock reads).
2. The evening-bar rule survives in the hot file AND the 17:0x vendor day-read is not a settle (§2R sentence).
3. WQ-192 STAND DOWN holds; $0 moved by PROME; X1 CLOSED.
4. 004: NO ADD (WQ-280); DFII10 THROUGH 2.50 at 2.85; harvest out of reach; expiry 9/30, 3 sessions.
5. `GATE-TERRY-007` RESOLVED MOOT; nothing presents it as live.
6. VLO: 1 of 3 filled @ $412 [9/18]; 2 STAGED; `GATE-TERRY-VLO-SCALE` 9/25 NOT MET, F1 UNKNOWN, HELD; **F1 <$95 = STAND-DOWN, never the buy trigger** (PROME's 12:3x inversion named in the file); the ±$0.15 rule is CONDITIONAL on tier ③ being the sole source; the day-colour kill STAYS LIVE; November governs through 10/14.
7. Energy sleeve USO 37 sh 100% UNDEFENDED; figure = 9/25c × 37, arithmetic.
8. Kill-on-sight: hot cell = currently applicable; full set = §KOS…§KOS.6; every entry binds except those RETIRED BY NAME; demotion ≠ retirement.
9. HENRY: gamma ≈0 at the 9/24 close (its dated row); no current gamma-sign claim beyond it.
10. **CHANGED:** BRENT's publishable Brent = Nov $106.60 [9/24 settle-proxy, single vendor]; 9/25 NOT published by PROME; the Brent cell LEADS with 106.60 (parser).
11. Every level carries a date; vol-complex levels carry "yfinance, NOT settle-confirmed".
12. `GATE-REG-T02` terminal; sub-$78 WAL close = SUPPRESSED RE-ENTRY.
13. Open-position clock: 004 3 sessions; TLT 82P ×2 NO RULING (WQ-292); ROLL70-EXIT 0-of-3.
14. Gate chain anchor exact form; header reads **Chain: 0**; gate reports chain 0 before commit.
15. §7's live corrections survive at cold §20.7 + §KOS.3 (hot cell points).
16. Brent tile ordering: expected parsed value **106.60**; verified by RUNNING `fleet_dashboard.py`.
17. Funding pairs same-date: SOFR 3.88 [9/24] − IORB 3.90 [eff. 9/24].
18. Rate-check outcome stated as SAM states it; plus 9/25: back UNDER, no intervention found (WALTER relay of SAM); neither "held" nor "intervention" appears as established.
19. HOMER's RED travels with its three caveats.
20. **CHANGED:** CRMT: the fourth bridge IS filed (STD 10/1); the kill "a fourth bridge was filed" is RETIRED by name.
21. NEXUS T-12: letter = ±10bp band on the 9/24 anchor cell (2.85); "≥2.50 ×5" = regime.
22. The 5Y composition failure ⇒ NO ADD; a fresh dated TLT card = a NEW Tier-3 ask.
23. The positions line names EVERY live option row and stock row with the mirror vintage (verbatim from the 21st).
24. HEARTBEAT_DASHBOARD.md carries ZERO projections at chain 0 (am.#1 projection removed).
25. 🆕 HY OAS 280 [9/24] is AT LIQUID's `>280` STRICT line (NOT met) and day 1 of 3 on RED-FT-01; the file never says "re-armed"; the 9/25 cell publishes Mon.
26. 🆕 BG-02 instance (4) LAPSED NOT MET; the WQ-264 shadow run is prospective and separate; the deploy question stays CLOSED.
27. 🆕 WQ-297 A: concentration ACCEPTED IN WRITING; no offset card; no trim — stated once in Book state and in §Skip; never as an open question.
28. 🆕 `GATE-BRK-R2` (a) FIRED with its consequent EXECUTED and its letter's meaning (evidence for re-adjudication, not a re-arm); no fired-unexecuted row exists.
29. 🆕 WQ-296/291/293/287 by 9/30 appear only as citations beside their facts; the open LIST stays in WILL_QUEUE.
30. 🆕 The five owned-set / owed items (LIQUID 9/28 · LIQUID/BROCK/DAEDALUS 10/02 · paid-data list) appear in the calendar line only; the owed narrative lives on SCRATCH.

## §Retirements — kill entries this base retires BY NAME
- *"a fourth bridge was filed"* (as a kill) — it is now TRUE (8-K 9/24 16:05 ET, STD 10/1).
- The closest-line entry *"BRT-26 ≥457 rigs — 452, final print 9/25"* — RESOLVED CONFIRMED at 455.

## Cold writes (BEFORE the hot cut)
§22.1 energy · §22.2 rates · §22.3 credit · §22.7 war/tariffs/housing · §KOS.6 (five demoted entries verbatim). The 21st base's am.#1 long-form is already §A23 (written 9/25 09:50); nothing else moves.

## Hot structure + byte plan
Candidate measured at the plan read 69.0%; re-measure with `measure.py` at every stage (the installed figure is read from the instrument, never from this line). Sections: header ~1,600 · legend ~1,150 · one-liner ~1,050 · channels ~8,900 (§3 and §7 heaviest, ~1,300 each — over the 600 B TARGET, as in the 21st; declared) · KERNEL ~330 · Book ~3,000 · Stress dashboard ~1,850 · Thresholds ~2,000 · Pointers ~2,300 · Cadence+§2R ~1,150 · Skip ~700. Acceptance: installed `measure.py HEARTBEAT.md` < 22,785 B; if it misses, prune the KOS cell to currently-applicable only and re-measure; if it still misses, STOP and report.

## RESULT-stage obligations
- Snapshot the twenty-first base + am.#1 verbatim → `PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_2026-09-25.md` (git object = receipt).
- Append the cold sections; remove the am.#1 projection from `PROME/HEARTBEAT_DASHBOARD.md`; note chain 0.
- RUN `fleet_dashboard.py`: Brent tile parses **106.60**; channels/levels render; build recorded in `dashboard_build.json`.
- Gate chain check reports **chain 0**; `measure.py HEARTBEAT.md` < 22,785 B.
- Blind RESULT read (coldreader, Opus) on the INSTALLED file; fix ❌ only; declare ⚠️ below.
- SCRATCH: amendment queue ⑪–⑮ marked CONSUMED at this base; HEARTBEAT line updated to "TWENTY-SECOND base, chain 0".
- Commit: snapshot + `HEARTBEAT.md` + `PROME/HEARTBEAT_COLD.md` + `PROME/HEARTBEAT_DASHBOARD.md` + `PROME/tools/dashboard_build.json` + this plan + SCRATCH, explicit pathspecs; subject ≤100 chars.

## Out of scope
`ACTIVE_DECISIONS.md` (over its <70% stop; the WQ-297/BG-02/BRK-R2 clauses land at its next rotation pass — declared) · FORGE/STATUS.md (mirror unchanged; the concentration ruling is a WQ record, not a mirror fact) · any desk file.

## DECLARED RESIDUE — plan read (coldreader `hb22plan`, Opus, 2026-09-25 17:17 ET; 64 claims: 40 ✅ · 17 ⚠️ · 7 ❌; verdict NO as-is → GO after the single-clause fixes; ledger `scratchpad/hb22/planread.md`)
**❌ fixed in ONE pass (v2 candidate):** ❌1 one-liner: VLO's +1.13% was the day change, not the distance to the 20-day — now "+1.12% at $387.145, 1.7% ABOVE its 20-day" · ❌2 KRE +0.6% → +0.9% (71.55 vs 70.94) · ❌3 the Book grade line restated TERRY's grade with the later vendor close ($387.18/+1.13%) — now TERRY's own figures (387.145 · +1.12% · USO −3.07%); the Stress-dashboard level line keeps the vendor close as a LEVEL, labelled · ❌4 the kill *"ANY Brent Nov level dated 9/23 or 9/24 NOT published by BRENT"* had been dropped unnamed — CARRIED and re-scoped in the hot cell (those dates are now published; SAM's $107.31 still is not) · ❌5 invariant 6 restored: "1 of 3 filled @ $412 [9/18]" and "November governs through 10/14" are back in the Book VLO line · ❌6/❌7 plan text (time limb; lineage commits).
**⚠️ declared (not fixed; the reader's 17 in the ledger, the load-bearing ones here):** the concentration line cites Friday as "showing the shape" although VLO ROSE while oil fell (C2) — kept as the sleeve-level statement (USO −3.1%, nothing keyed to credit), with VLO's rise visible in the same sentence · channel §3 and §7 exceed the 600 B TARGET (declared, as at the 21st) · vol-complex cells are yfinance, CBOE unpublished for three sessions · the 17:0x futures day-reads are labelled non-settles but readers may still quote them · the F1 tier-③ figure is an estimate the owner may never finalize · the reader's kill-set diff found a second entry (⚠️8) that binds at cold §KOS L409, unchanged · the paid-data list is a draft with no prices · `GATE-BRK-R2`'s fire was found 7 days late (an owner-side lag, stated in §22.3).

## DECLARED RESIDUE — result read (coldreader `hb22result`, Opus, 2026-09-25 17:24 ET on the INSTALLED file; 104 claims: 86 ✅ · 13 ⚠️ · 5 ❌; verdict NO as-is → GO once fixed; ledger `scratchpad/hb22/resultread.md`)
**❌ fixed in the ONE allowed further edit (no rule's meaning changed; file CLOSED for the session after it):** ❌1 cold §22.1 restated TERRY's grade with the vendor close → the owner's figures (387.145 / +1.12% / USO −3.07%), the 17:0x print named as a later vendor print · ❌2 two closes for one VLO session → 387.145 (TERRY's official close) in §1 and the level line · ❌3 LIQ-072 "15bp under" re-authored the owner's grade → "graded 9/24 on IG 77 [9/22], 17bp under" · ❌4 §KOS.6 pointed the 21st base's retirement at §KOS.5-H (the 20th's) → a §KOS.6-H history line names the 21st's retirement ("the negative-gamma squeeze is building", superseded) · ❌5 the 2s10s level was undated → [9/24] in both places. Three byte cuts paid for them (the "(a target the gate does not meter)" aside; "(L322)"; the FERT-G3 · OSPREY-001 list entries, both still in GATES).
**⚠️ declared, not fixed:** the ±$0.15 rule's "conditional on tier ③ being the sole source" clause is implied (① 403 / ② unfinalized), not stated · `dashboard_state.json` carries no Brent LEVEL tile (the config band is named "Brent (BZX26 Nov)" while the parser maps "Brent" — predates this base; the ticker line carries 106.60 and the HTML shows it) · invariant 22's "Tier-3 ask" wording is not in the hot file (never was) · the positions line's APO/WQ-292 parentheticals changed (owner-correct) · "re-armed" appears only inside a kill quote · WQ-293/WQ-287 are listed bare in the calendar line (citations, not a list) · the kill "ATTRIBUTION / DAMAGE LOCATION / BARRELS are ESTABLISHED" left the hot cell unnamed and binds at cold §KOS L409 · "the day-colour gate bars Will's VLO order" lives at the Book VLO line marked ⛔ STAYS LIVE, not in a KOS block (escalation declined: the entry is in the hot file) · §KOS.6's 20Y I′ bracket carries a 9/25 update inside a block labelled VERBATIM · the NEXUS anchor 2.85 is stated ahead of GATES L24's "pending publication" (NEXUS grades) · the calendar's "Duma checkpoint (L432)" on 9/30 is WQ-293's needed-by, the row's window runs to 10/31.

**ARGUS (argus-2e3, closeout 17:58 ET) ❌2 — added to the residue, HEARTBEAT closed for the session:** §1 and the Book sleeve line credit TERRY with "USO $148.33 (−3.11%) [9/25c, TERRY]"; TERRY's figure is 148.39 (−3.07%) (card §⑩, memo, GATES L23); 148.33 is PROME's own 17:0x vendor pull. Carried as amendment-queue item ① on SCRATCH for the next write.
