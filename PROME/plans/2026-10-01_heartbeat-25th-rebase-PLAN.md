# HEARTBEAT twenty-fifth re-base — PLAN (PROME `prome-2f`, Thu 2026-10-01, POST-CLOSE)
**Candidate:** the session scratchpad `hb25/HEARTBEAT_candidate.md` (installed as `HEARTBEAT.md` only after the plan read); **cold append:** `hb25/COLD_append.md` → `PROME/HEARTBEAT_COLD.md` (§25.1 · §25.2 · §25.3 · §25.4 · §25.6 · §25.7 · §25.8 · §25.B · §KOS.9); **dashboard companion:** `PROME/HEARTBEAT_DASHBOARD.md` re-cut to zero projections. Prior base: the twenty-fourth (post-close Tue 9/29) + am.#1 (9/30 11:1x) + am.#2 (9/30 17:4x) + am.#3 (9/30 19:1x); the last commit touching `HEARTBEAT.md` is read from `git log -1 -- HEARTBEAT.md` at install, not typed. Process: `PROME/CLAUDE.md` § Review budget — ONE blind PLAN read (this file + candidate + cold append), fix ❌ only, install in one pass, ONE RESULT read on the installed file, declare ⚠️ here; a third read only if a ❌ fix on the result changed a rule's meaning. Byte figures come from `PROME/tools/measure.py`, never from this text.

## Why now
The file has stood at or above 75% of the 32,550 B budget for three touches (the boot's `read_cap_check` advisory: rotate-tier, `rotation_due=1`), at chain 3 — one short of the gate's <4 advisory. Am.#2 scheduled the re-base for Thu 10/1 post-close; the `prome-0c` sitting closed out BEFORE the close and deferred it a second day. This sitting is the first post-close touch. A regime limb is also met: LIQUID's `LIQ-07` trigger fired on the 9/30 cell, the official long end made its sixth straight high, and Will sold and rolled the whole Sep-30 expiry set. Process class: DOMAIN (a regime-memo rotation under §C — no tool, gate, check or charter text changes).

## Data the new base stands on (every figure dated; sources at the artifact)
- **Vendor closes, `fetch.py price` 16:06 ET 10/1:** SPX 7,666.45 · SPY 764.04 · QQQ 742.03 · TLT 77.71 · GLD 382.78 · WAL 75.71 · KRE 69.96 · OZK 46.34 · FLG 11.69 · USO 150.03 · XLE 62.69 · VLO 408.30 · TBT 42.23 · CRMT 0.98 · APO 114.36 · HBAN 15.19 · AAPL 330.32 · APD 273.32 · HYG 76.90 · ARES 116.62 · BIZD 12.47 · FSK 11.11 · OBDC 10.43 · MU 1,097.39 · VIX 16.25 · VVIX 91.40 · MOVE 110.00 · ^SKEW 141.92 (9/30, `⚠stale`) · USD/JPY 158.14. ⚠️ Read six minutes after the cash close; a later consolidated print can differ by cents.
- **`dashboard.py` 16:05 ET 10/1:** Brent (`BZZ26` Dec) $102.65 (+4.62) [10/1] — a vendor day bar, NOT a settle; HY 312 / CCC 1,179 [9/30]; gasoline 4.46 [9/28]; claims 197,000 [9/26] / continuing 1,701,000 [9/19]; SOFR 3.90 [9/30]; Cushing 24.30 [9/25].
- **FRED, cache-busted `fredgraph.csv`, 16:06 ET 10/1 (default curl client; a browser User-Agent returned empty bodies):** DGS10 5.26 · DGS2 4.89 · DGS5 5.06 · DGS30 5.59 · DFII10 2.91 [9/29] · T10YIE 2.36 [9/30] · HY 3.12 · CCC 11.79 · IG 0.84 · BB 1.94 · B 3.16 · BBB 1.03 · HY EY 8.16 [9/30] · SOFR 3.90 [9/30] · IORB 3.90 [10/1] · WRESBAL 2,930,193 [9/23] · MORTGAGE30US 7.28 [10/1] (7.03 [9/24]) · ICSA 197,000 [9/26] · CCSA 1,701,000 [9/19].
- **Official Treasury 9/30:** BOND `AGENTS/BOND/STATUS.md` (`KB-BND-372`).
- **NY Fed swap-line API, PROME raw reads 15:37 · 15:54 · 16:05 ET:** the 9/30 ECB operation ($207M, 7-day, 4.13%) appeared with `lastUpdated 2026-10-01 16:00:00`.
- **Owner artifacts (all committed; memos under `PROME/inbox/processed/2026-10-01*`):** BRENT (L0 drain, nothing fires; 9/30 proxies 77b8f8af6) · FALCON ×3 · FERT G5 · FLG T-08 · HANS ×3 incl. the CORRECTION addendum · LABOR · LIQUID (9/30 cell; gate reviews; swap line) · MIDAS · OZK · RED touch 2 · SAM · VULCAN MU grade · SHADE · CARL · BOND phase 1 · TERRY (cards, corrections) · ANVIL dac72b4ae · DAEDALUS. Earlier: am.#1–#3's sources as named in those blocks (preserved in the snapshot).
- **FR2004 as-of 9/23:** BOND's grade from this sitting's spawn `bond-1001b` (96ccc7a0c; memo `PROME/inbox/processed/2026-10-01_from-BOND_FR2004-9-23-grade-WQ-291.md`): 3–6Y $60.079B vs the $56.586B bar ⇒ MET by $3.493B; PRE $47.986B unrevised; long-end TOTAL −$3.8B and 6–7Y −$4.646B reported, never graded. PROME re-pulled the NY Fed series `PDPOSGSC-G3L6` at 16:22 ET: 47,986 → 60,079 ($M). WQ-357 registered (9c30a8bb8).
- **Book:** Will's 16:15 ET end-of-day Fidelity capture (`PROME/data/2026-10-01b_broker-capture-TRANSCRIPTION.md`, ties to the cent at $36,077.04); mirror reconciled by ANVIL d97eba708 (rotated to 29,694 B); the Oct-01 740P ×4 are gone (disposition UNBOOKED, FORGE D-71) and FOUR QQQ Oct-02 740P are new (basis $890.65).
- **Gate:** boot gate 15:3x ET 10/1 — 24 GATES rows, zero fired-unexecuted; chain 3.
- **Unknown at the write:** how the four Oct-01 740P left the account (no Activity view) · Will's word on WQ-357 · TERRY's cards (terry-b2 is live in Will's window) · the 10/1 official curve · BRENT's 10/1 proxies · any owner attribution of Thursday's oil move.

## What CHANGES from the twenty-fourth base (+ am.#1–#3)
1. Header: twenty-fifth, chain 0; long-forms §25.x + §25.B; §KOS.9; size clock 2026-10-04.
2. Legend re-dated (`[10/1c]` · `[9/30]` ICE · `[9/29]` H.15 · `[9/30 official]`); the FUTURES clause now names BRENT and MIDAS as proxy publishers (the 24th's result-read ⚠️55).
3. One-liner rewritten around LIQ-07, Thursday's oil move (vendor reads), the long-end highs, Europe, the FR2004 MET and its exit recommendation (WQ-357), and Friday's four 740 puts.
4. §1: BRENT's 9/30 proxies become the publishable figures (the Dec contract leads — the pin is in); 10/1 stated as owner-owed with three labelled vendor reads; WPSR and policy rows folded from am.#1.
5. §2: official 9/30 curve; PCE; the FR2004 result; the sleeve after the 9/30 sales; 004's clock and hold rail REMOVED (card CLOSED).
6. §3: 9/30 cells; LIQ-07 fired; RED's red-team; gate reviews; the raw swap-line figure with the instrument WITHHELD; BIZD's drop unowned.
7. §4: the 158.14 vendor read above the rate-check level, ungraded; SAM's 10/1 facts. §5: 10/1 vol closes. §6: the Micron grade. §7: Ghawar heat; Europe corrected; FLG-T08 fired; labor; PMMS. §8: MIDAS's hits and settles.
8. Book: re-cut on the 10/1 post-close reconcile; WQ-316 and the 004 clock REMOVED (done); WQ-347 with the 10/1 close arithmetic; Monday's 735P; the standing sell-or-roll practice; VLO-SCALE TERMINAL.
9. Stress dashboard: the Brent cell LEADS with **97.99** (BRENT's 9/30 Dec proxy) — the parser's first numeral after the Brent token.
10. Thresholds: FLG-T08 and VLO-SCALE shown RESOLVED; closest lines re-keyed (HY >320 at 8bp); calendar Fri 10/2 → Thu 10/8.
11. KOS: hot cell re-keyed; five retirements by name; merges and one demotion named at §KOS.9.

## INVARIANTS — each survives, in substance, in the HOT file
1. DERIVED; owner surface wins; the date legend survives; an undated level is a defect.
2. The evening-bar rule (L462) survives in §2R (3); no futures settle from a PROME read.
3. WQ-192 STAND DOWN holds; $0 moved by PROME; X1 CLOSED (8/28); DON'T-SIZE.
4. The 004 card is CLOSED; NO ADD (WQ-280) survives as a guard on any successor; a fresh dated TLT card is a NEW Tier-3 ask; WQ-339 is its sitting.
5. VLO: 1 of 3 filled @ $412 [9/18]; VLO-SCALE TERMINAL, both staged shares stand down, only Will's hand reverts; F1 <$95 = STAND-DOWN never a buy trigger; the day-colour kill STAYS LIVE; VLO-HELD-01 A/B1 as registered; November governs through 10/14.
6. Energy sleeve USO 37 sh 100% UNDEFENDED; figure = 10/1c × 37, arithmetic.
7. Kill-on-sight: hot cell = currently applicable; full set = §KOS…§KOS.9; every entry binds except those RETIRED BY NAME; a merge or demotion keeps the entry binding.
8. No current gamma-sign claim.
9. Publishable Brent = BRENT's 9/30 Dec proxy $97.99 (single vendor, not CME); the cell LEADS with it; Thursday's 102.65 is stated as a vendor day bar, NOT a settle, with no cause attributed.
10. Every level carries a date; vol marks carry "yfinance, NOT settle-confirmed".
11. `GATE-REG-T02` terminal; sub-$78 WAL close = SUPPRESSED RE-ENTRY.
12. Open-position clock: QQQ Oct-02 740P ×4 expire Fri 10/2 (sell-or-roll by 15:00); the Oct-01 four's exit is UNBOOKED (never stated as a fill); 735P ×5 Mon 15:00; USO 150C ×1 10/9; 82P ×1 + HBAN 16P ×2 (WQ-302 by 10/14); ROLL70-EXIT 0-of-3.
13. Header reads **Chain: 0**; the dashboard companion carries ZERO projections.
14. Brent tile: expected parsed value **97.99**, verified by RUNNING `fleet_dashboard.py`.
15. Funding pair: SOFR 3.90 [9/30] − IORB 3.90 = 0 (observation date vs effective date — the pairing's own ambiguity, declared as before).
16. The yen: 158.14 is a vendor read above the rate-check level, UNGRADED; neither "breached" nor "intervention" appears as established.
17. LIQ-07 is stated as a TRIGGER with its verdict date, never as a bear confirm or an X1 re-arm; RED's caveat travels.
18. The swap-line figure is RAW; the instrument is WITHHELD (L568); no reading.
19. Ghawar: heat only; a strike is NOT established.
20. Europe: 'France-only' is WITHDRAWN; T-10 fired with an exit registered; the OAT–Bund level is vendor-basis.
21. `GATE-LIQ-069`: the letter governs; WQ-301 (b) is Will's.
22. WQ-297 A: concentration ACCEPTED IN WRITING — never an open question.
23. WQ-339's sitting is stated as STANDING DOWN on BOND's own rule, never as cancelled by PROME. The positions line names EVERY live option and stock row with the reconcile vintage and account totals; Will's 9/30 and 10/1 sales are stated as his own hand.
24. WQ numbers appear only as citations; the open LIST stays in WILL_QUEUE; owed narrative lives on SCRATCH; the calendar line is PARTIAL and says so.
25. The Bloomberg-vs-ICE CCC kill survives in the hot KOS cell and §3.
26. CORAL: bank rail NOT armed; MSI-01 grades 10/09. HOMER's rail 0 of 5; PMMS stated as a figure HOMER grades.
27. The KRE-put packets at TERRY are a CARD ASK, never an approval, with the three constraints and root rule #5.
28. The FR2004 result is stated on BOND's letter (3–6Y alone; MET iff ≥ $56.586B); a MET is a RECOMMENDATION via TERRY's card and Will's approval, never an action.
29. Will's standing sell-or-roll practice is stated; no option line carries a hold-to-expiry rail.

## §Retirements — kill entries this base retires BY NAME (history at §KOS.9-H)
The 004 ×15 hold / one-session clock · "WQ-316 is Will's by 15:00 Wed" · "BRENT dark" as the basis of the 9/29-settle entry · "the Wednesday Brent drop / `BZ=F` fall is a signal" as a dated instance · "HY 302 completed RED's exit leg — Tuesday's cell" as a forward item.

## Hot structure + byte plan
Acceptance: installed `measure.py HEARTBEAT.md` < 22,785 B (the <70% stop). If a read's fix pushes it over, prune in this order — (a) the calendar line to Fri–Mon + pointer, (b) the KOS cell's last three quoted entries to §KOS.9 verbatim; if it still misses, STOP and report. Channels §1, §2, §3 and §7 exceed the 600 B TARGET (declared, as at every base since the 21st).

## RESULT-stage obligations
- Snapshot the twenty-fourth base + am.#1–#3 verbatim → `PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_2026-10-01.md` (header names the last commit touching `HEARTBEAT.md` and the `measure.py` line at capture).
- Append the cold sections; re-cut `PROME/HEARTBEAT_DASHBOARD.md` to zero projections.
- RUN `fleet_dashboard.py`: Brent tile parses **97.99**; build recorded in `dashboard_build.json`.
- Gate chain check reports chain 0; `measure.py HEARTBEAT.md` under the stop.
- Blind RESULT read (coldreader, Opus) on the INSTALLED file; fix ❌ only in ONE further edit; declare ⚠️ below.
- SCRATCH: the re-base marked DONE; the amendment queue emptied.
- Commit with explicit pathspecs; subject ≤100 chars.

## Out of scope
`ACTIVE_DECISIONS.md` · `PROME/BOOT.md` · `FORGE/STATUS.md` (awaits Will's capture; 98% of cap) · `PROME/GATES.tsv` (no state changed by this re-base) · `PROME/WILL_QUEUE.md` · any desk file.

## DECLARED RESIDUE
**Plan read (coldreader `hb25-planread`, Opus, blind; ~16:31 ET; 89 claims: 70 ✅ · 16 ⚠️ · 3 ❌; verdict "No"; ledger `scratchpad/hb25/planread.md`).** ❌ fixed in ONE pass before install: ❌19 WQ-344 shown as open for 10/6 — Will RULED it 9/30, dead as written (carried over from am.#1; fixed in hot ×2 and cold) · ❌58 the WQ-150 carry pointed at a `SCRATCH.md` § Carried that no longer exists → re-pointed to `PROME/archive/SCRATCH_ROTATED_2026-09-29_prome-e6c.md` CUT 2 (the 24th base carried the same dead pointer) · ❌74 WQ-302 (the 82P and HBAN choices by 10/14) had dropped out, failing invariant 12 → restored in the Book and §Skip. Cheap ⚠️ also fixed: the one-liner now says LIQ-07 fired ON B/CCC WIDENING (not on HY 312) · "BOJ" on the October OIS figure · MOVE dropped from §2 (it lives in §5 with its label) · "Card 004 CLOSED" stated in hot · the LIQ-069 alternative-bands CONDITIONAL caveat restored · `CREED-T-08a` / "Hold S8a at 4" restored · TERRY's two card names cited. Paid for by pruning the calendar to Fri–Tue (prune step (a)) and three low-value clauses. Invariant 6 as written (close × 37) is superseded by the broker capture's own value ($5,550.00), labelled as such.

**Result read (coldreader `hb25-resultread`, Opus, blind, on the INSTALLED file; ~16:40 ET; 72 claims: 54 ✅ · 16 ⚠️ · 2 ❌; verdict "Mostly yes"; 85 of 88 pointers resolve, no dead pointer; every distance recomputes; positions and totals match FORGE to the cent; ledger `scratchpad/hb25/resultread.md`).** ❌ fixed in ONE further edit, UNREVIEWED: ❌12 "TERRY's owner grade for 9/30 and 10/1 OWED" — TERRY had graded both at 16:2x ET (8f9e6b7d1) → the hot line and cold §25.1 now state the grade; the GATES row mirrors it · ❌33 "the yen closed Thursday above the rate-check level by a vendor read" contradicted the file's own legend → "a 16:06 ET vendor read sat above the rate-check level (not a close)". Neither fix changed a rule's meaning ⇒ no third read. **Disposition: the base is INDEPENDENTLY VERIFIED-WITH-RESIDUE; the two edited clauses are IMPLEMENTED only.**

**⚠️ declared, not fixed (result read):** the calendar line runs Fri–Tue, not to Thu 10/8 as "What CHANGES" #10 says (the prune order was applied) · the "highest since 2002" superlatives are BOND's; HENRY's STATUS withholds the 30Y one — hot shows BOND's side only · `FORGE/STATUS.md` still says the Oct-02 740P has NO card (ANVIL wrote it minutes before TERRY's card landed; next reconcile) · "SAM's own 10/1 read was 157.4" — the reader finds 157.4 is SAM's 9/30 close and 157.56 its 10/1 read; SAM's memo RESULT line says "yen 157.4"; SAM's file governs · NEXUS has graded a 9/30 DFII10 cell at 2.93 (2bp from the band's upper edge); hot shows the 9/29 FRED cell 2.91 and the official 9/30 2.93 separately · distances on the closest-lines row and "Challenger 43,281" carry no date of their own (invariant 10) · the SOFR/IORB date pairing is not declared in hot (invariant 15) · the Robinhood `T` share row (D-20) and the prediction-market contract are not on the positions line (invariant 23) · bare "WQ-353 · WQ-355" on the calendar and the §Skip capital-lines sentence sit near the no-list rule (invariant 24, the reader's borderline) · §KOS.9-H is a bold label inside §KOS.9, not a heading · WQ-192 and WQ-200 have rolled off `WILL_QUEUE.md` (cited as rulings).
**Brent tile:** the ticker line renders "Brent Dec $97.99"; the distance TILE for Brent is absent from `dashboard_state.json` `levels` in this build AND in the prior build at HEAD — a pre-existing parser gap (a docketed item), not a product of this re-base; invariant 14's "verified by running" is met for the ticker, not for the tile.
**Deviation:** PROME ran `prome_gate.py boot` directly a second time at 16:3x ET to read the chain check (the boot manual says to use the session runner's refresh form).
**Reads used this episode:** plan read (1) · result read (2) — two of the three-read ceiling. Process class: DOMAIN.
