# FALCON SCRATCH — 2026-10-10 (`falcon-1010b`, PROME `prome-ce` spawn ~12:05 ET: complete the write-back of `falcon-1010` [11:3x ET, WQ-369 C8 on WALTER SIG-W-20261010-002], cut short by the WQ-249 closeout ask at 11:47 ET)

## CURRENT MARKS
**B 1 / C 14 / D 85** HELD (formal 7-day review **10/14**). Convergence 43/50. **FAL-06 OPEN (70%, to 11/05)**, no route fired. Production rung D 85→92 **ARMED, NOT FIRED**. **GATE-FALCON-001 LIVE:** leg 1 FIRED 7/23 · leg 2 NOT FIRED (graded 10/07; 10/10 pre-fetch 74 vs 80, not a grade) · leg 3 FIRED 8/15 · event override NOT TRIGGERED through 10/10 · review_by **2026-10-14**. Losses 3. Casualty ratchet YELLOW, RATE-STEP NOT LIT (7 vs 6; bar now 12). WARRISK rows EXPIRED (+4d; Bab +68d). No settle-count clock (12b no-op). Model: Opus (`claude-opus-5-5`), Claude Code, desktop.

## CHANGES SINCE LAST SESSION (10/09 ~10:4x ET → 10/10 ~12:2x ET)
- **Shedgum gas plant (Ghawar) on fire from the 10/09 night passes** (own FIRMS, max pixel 192.3 MW vs 18.5 baseline; still burning 10/10 11:47Z). Hawiyah gas plant elevated. Four north-Ghawar upstream heat spots stepped up 10/10 (one 0.86 km from OSM Ain Dar GOSP1). Cause UNVERIFIED; no Aramco/MoE/SPA/Saree word as of ~12:1x ET.
- "Houthis struck Ghawar with a BM": RIA via 1news.az (field, no facility); JFeed names Shedgum, no source. Saudi warning on sharing impact-site info (AP).
- KKIA attacked again 10/10 ~12:00Z (AP/AFP; 'dozens' injured, ≥5 ICU; NOT state-confirmed; no Houthi claim). Coalition says it destroyed 136 Houthi targets.
- Bloomberg 10/9: Aramco to supply European refiners' full November requests (unnamed). Baghaei 10/07: Iran–Oman safe-corridor coordinates agreed, undated (found 10/10).

## WHAT I DID THIS SESSION (falcon-1010 graded; falcon-1010b wrote back)
- falcon-1010: graded everything → nothing fires (memo `PROME/inbox/2026-10-10_from-FALCON_ghawar-fires-kkia-petroline-read.md`); own FIRMS CSV; inbox 2/2.
- falcon-1010b: KB-266..275; CAS-2026-025 + clock 10/10 + ratchet recompute from the file (7 vs 6; 57 vs 143); STRIKES sweep 10/02→10/10, **zero new rows** (five candidates not rowed by the row rule: established facility AND cause), mark advanced to 10/10; TankerMap bars CSV `domain/tankermap/2026-10-10_bab_daily_bars.csv` (vintage 15:00:46Z); STATUS rotation (old table → `domain/sources/STATUS_archive_2026-10-10_rotation.md`, grep-verified first); BRENT packet on the GOSP-flaring inference; one primaries check after 11:47 ET (none).
- ⚠️ **Corrected my own 11:4x memo** (not edited; PROME consuming): the Ain Dar GOSP1-area spot was NOT dark 28 days (lit 9/20, faint 22:54Z 10/09); first-at-00:52Z holds for two spots, not three (KB-268).

## NEXT SESSION (dated, future-verifiable)
1. **2026-10-14:** GATE-FALCON-001 review (TankerMap bars on the then-current vintage) + 7-day scenario review + DAEDALUS deferrals (leg-2 vintage rule, letter clarifications, FAL-06 search floor/ceiling, VX IRAN-02 instrument) as proposals via PROME.
2. **STANDING:** counting source naming Ain Dar/Shedgum crude units (GOSP/CPF) or the Khurais facility with hostile cause ⇒ FIRE D 85→92, C 14→7, PROME same hour. First action: re-pull Ghawar FIRMS (does Shedgum persist; do the upstream spots fade as it recovers? — that tests the flaring inference).
3. KKIA 10/10: GACA/SPA counts → update CAS-2026-025. IMO notice on the Iran–Oman coordinates (L229, to 10/26).
4. WARRISK re-pull (registered falsifier expired +4d). 160-26 position/hull; NV Sunshine identity; 159-26 text; DHALGOUT; 158-26 casualties.
5. CTP-ISW + Shafaq; VESSELS backfill (El Gaia, St Helena, Trend, STI Steadfast).

## OPEN THREADS / WATCHES
- 🔴 Ghawar: gas-plant fire + upstream heat; the production rung's first IN-class candidate if a counting source attributes it. BRENT has the inference.
- 🔴 CARRIED OPEN (MEMORY.md): KB-168 Yanbu terminus proxy unbuilt.
- 🟠 Riyadh airport hit three times in five days; Houthi threat to all Saudi oil staff (10/08) stands.
- 🟡 FRESH_LEG_BASELINE hot/cold split; carried builds.

## PREDICTIONS DUE / DECISIONS PENDING
FAL-06 OPEN (70%, 2026-11-05). No Will decision from this desk. No GATES change routed (nothing fired).

## MAIL STATE
In: census 12:0x ET top-level 0 · WALTER/ 0 (falcon-1010 consumed 2). Out: `AGENTS/BRENT/inbox/2026-10-10_from-FALCON_ghawar-gosp-flaring-inference.md`; `PROME/inbox/2026-10-10_from-FALCON_ledger-writeback.md` + SendMessage COMPLETION block to PROME.

## PENDING PUSH / GIT
Exact-path commits; push via `scripts/safe-push.sh`. Foreign dirty paths (PROME/) are not mine; no pull, no stash.
