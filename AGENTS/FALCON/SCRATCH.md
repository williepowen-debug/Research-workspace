# FALCON SCRATCH — 2026-10-07 (PROME-spawned `prome-0e`, ~21:41–22:32 ET; WQ-184 Tier-1 due-row: GATE-FALCON-001 review + whole-inbox L0 drain)

## CURRENT MARKS
**B 1 / C 14 / D 85** HELD (7-day review run 10/07, a day early; next **10/14**). Convergence 43/50. **1 OPEN: FAL-06 (70%, to 11/05), no route fired.** Production rung D 85→92 ARMED, NOT FIRED. **GATE-FALCON-001 LIVE, graded 10/07:** leg 1 FIRED 7/23 · leg 2 NOT FIRED (7d 72 vs ref 69, +4%) · leg 3 FIRED 8/15 · event override NOT triggered · **review_by 2026-10-14** (owner-set). Losses stay 3. WARRISK falsifier LIT, all 5 rows EXPIRED. No settle-count clock; step 12b no-op. Model this session: Opus (`claude-opus-5-5`), Claude Code, laptop.

## CHANGES SINCE LAST SESSION (10/04 ~18:0x ET → 10/07 ~21:41 ET)
- Khurais-spot fire (25.252N 48.103E) burned 10/03→10/07, peak 504.6 MW 10/06 (own FIRMS). AFP 10/05 (one unnamed source): a Khurais-area PUMP STATION hit 10/04, pipeline "stopped again"; Bloomberg/Reuters sources: flowing; Misbar 10/06: smoke from "the Khurais oil processing facility"; minister 10/06: line "heavily attacked … operational now", "5.8 million barrels". No counting source names the facility.
- Hull war: UKMTO 152–158-26 (IRGC turn-back off Khasab 10/05; strikes 10/03–10/05 incl. LPG + crude tankers, ON PEACE 12 injured, MARAN GAS MYSTRAS; **158-26 off Qatar 10/07 ~1900Z, casualties, no count**). 13–16 struck hulls 9/28–10/07, none sunk.
- Saudi-Houthi land war: Rabigh claim 10/05 (own FIRMS 126.9 MW), airports 10/06–10/07 (3 killed, 36 injured 10/07, GACA). Government "Operation Dawn of Yemen" claims Bab al-Mandab "secured" (10/05), Houthis deny; Perim/Mayun besieged.
- WALTER 10/05: Will-directed tanker-cost/USO watch (`b3677b25d`). WALTER 10/07: -014 (minister 5.8 basis), -015 (Rabigh).

## WHAT I DID THIS SESSION
- **Graded GATE-FALCON-001 at the letter** → `reports/2026-10-07_gate001-review-and-inbox-drain.md` §1–2 + FRESH_LEG_BASELINE 10/07 block. **First R1 read-back from TankerMap's own daily bars** (saved `domain/tankermap/2026-10-07_bab_daily_bars.csv`); no completed UTC day 10/02–10/07 qualified. **R3 backtest:** 3 sustained qualifying runs since March on the grading series (April, 7/26–8/02 embargo, 8/31–9/02), not 1 — routed to PROME; no threshold moved. Vintage residue proposed (grade completed UTC days; read-backs use current vintage).
- Khurais follow-up (§3): rung NOT FIRED; facility class contested between non-counting sources. KB-246/247/248.
- Drained 14 inbox items (13 WALTER + PROME 10/03 note) + 2 BOARD_SCAN rows; dispositions in board_log and report §4. Tanker-cost/USO watch: ADOPT the security half, DECLINE freight/WTI/USO.
- Ledgers: KB-244..257; VESSELS VI-0047..0055 + 3 annotations (data clock 10/07); CASUALTIES CAS-021..023 + ratchet recompute (RATE-STEP off on the fresh window; EXIT §3 now 6 of 8); VX stamps (Bab, casualty, sunk); WARRISK attempt line (clock not advanced).
- Boot checks: 5a (FLOW +168d, known), 5a-2/5a-3 (WARRISK 5 rows EXPIRED), 5b-2 (Hormuz DEEPENING, print 10/04 4/88), 5b-3 (bypass HOLDING 103,562 vs floor 30,509, print 10/02), 7b PASS. SKIPPED: 5b baghdad (demoted), 5b-4 kharg (impeached), 5c sweep (STRIKES mark 10/01, 6d; no candidate meets the row rule — sweep carried).
- Two read-only Opus helpers (UKMTO 151–158; Bab/Red Sea/Saudi claims); results spot-checked (gCaptain 10/06, The National 10/07).

## NEXT SESSION (dated, future-verifiable)
1. **STANDING:** Khurais facility at 25.25N 48.10E — any Aramco/Tadawul/MoE/SPA/MoD/CENTCOM or named-wire (named official / ≥2 industry sources) item naming it. Processing facility (IN) + hostile strike ⇒ FIRE D 85→92, C 14→7, PROME first line same hour; pumping station ⇒ OUT → BRENT BG-02 + FAL-06. Also any stated production OFFLINE (FAL-06 route b). Re-pull FIRMS first thing.
2. **158-26:** casualty count (a death ⇒ MARINER YELLOW, CAS-023 update), hull/flag; WARRISK re-pull (Gulf-internal attack).
3. **2026-10-14:** GATE-FALCON-001 review (daily bars; exclusion clause live as Saudi loadings normalise) + 7-day scenario review.
4. UKMTO hygiene: ON PEACE ↔ 156/157; 155-26 duplicate?; 153–155 hull names; LIPSI CTL; 159-26+.
5. CTP-ISW 10/01–10/07 + Shafaq; STRIKES sweep 10/02→; VESSELS backfill (El Gaia, St Helena, Trend, STI Steadfast).
6. Kpler/Vortexa weekly Saudi export print (FAL-06 route c).

## OPEN THREADS / WATCHES
- 🔴 CARRIED OPEN (MEMORY.md): KB-168 Yanbu terminus proxy unbuilt.
- 🟠 Bab: government counteroffensive vs Houthi denials — a confirmed recapture of Perim/Mayun lowers the leg-2 prior.
- 🟠 Pattern-watch: KOTC-concentrated hits; western-Gulf spread (158-26).
- 🟡 FRESH_LEG_BASELINE hot/cold split (over the read cap, not boot-read whole); VX sweep; carried builds.

## PREDICTIONS DUE / DECISIONS PENDING
FAL-06 OPEN (70%, 2026-11-05) — no route fired. No Will decision from this desk. For PROME: (1) GATES mirror update `G:GATE-FALCON-001` (review_by 10/14); (2) the R3 evidence for whenever the provisional leg-2 letter is reviewed; (3) a Bright Data fetch of UKMTO 158-26 is PROME's/WALTER's call.

## MAIL STATE
In: 14 consumed, 0 remaining (13 WALTER + PROME 10/03 note); 2 BOARD_SCAN rows. Out: `PROME/inbox/2026-10-07_from-FALCON_gate001-review-and-inbox-drain.md` + SendMessage COMPLETION block.

## PENDING PUSH / GIT
Exact-path commits by this desk; push via `scripts/safe-push.sh` at closeout (spawn order). Foreign dirty paths (FERT, TERRY, REGINALD, PROME) are not mine; no pull, no stash.
