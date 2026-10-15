# ORACLE → PROME: WQ-436 crash recovery done. The residue was sound apart from one false claim; kalshi.py verified in both modes; DAEDALUS ⑰ consumed, two items for Will

**Written 2026-10-15 08:47 ET (from `date`) by ORACLE.** Spawned by PROME `prome-73` under WQ-436 (Will 08:31 ET, "okay approved both"). Runtime: Claude Code Agent-tool desk spawn, model `claude-opus-5-5`; session ID not exposed to me (UNKNOWN). Box: laptop `WilliePOwen`, with no Kalshi creds here. Instructions were read explicitly: root CLAUDE.md, AGENTS.md, USER.md, ORACLE CLAUDE.md, COMPLETION_SPEC and your brief. $0. No trade, no threshold moved, no new direction.

## 1. Residue: six files, all kept, one repaired, none discarded

Evidence: each file read whole; the dead session's transcript (`~/.claude/projects/-home-willi-Research-workspace-AGENTS-ORACLE/0ce3f089….jsonl`; last tool call 04:03:30Z = 00:03 ET; the crash notice lands at 07:08Z) and live venue APIs.

| File | State | Check |
|---|---|---|
| `scripts/kalshi.py` | **complete** | Creds optional. Behaviour, tests and limits are in §2 |
| `watchlist.tsv` | **repaired (one claim)** | All Sept → Oct rolls and both retirements re-verified (Gamma `closed=true` for 7 September events + Sept $110, Houthi-9/30, Mamdani). ❌ The bank-relist note said "WALTER watch phrase sent". No packet ever existed (transcript + WALTER inbox), so the note is corrected and the term was sent (`f6130690d`) |
| `kalshi_watchlist.tsv` | **complete, one omission filled** | Sept CPI/U3/Brent results re-verified at the API. The Iran-crude retirement now records its result (NO, 1.957M bpd) |
| `workbook/ODDS_LOG.tsv` | **complete** | +62 rows (50 @ 03:56Z, 12 @ 04:02Z), 11 fields each with ts + slug, 0 deletions |
| `workbook/KALSHI_ODDS_LOG.tsv` | **complete** | +25 rows (14 @ 03:57Z, 11 @ 04:02Z), ts + ticker, 0 deletions. ⚠️ The 03:57Z rows for 8 FINALIZED markets are last-trade prints, not probabilities. That is the pull's standing behaviour (10/9 did the same) and is now flagged in STATUS |
| `workbook/DISRUPTION_SUPPLY_SPREAD.tsv` | **complete** | +1 row (+77.0pp @ 03:56Z). Mixed CRLF/LF is pre-existing (MAINTENANCE 9/28), not crash damage |

Not on disk: the dead session's `history --write` never finished (`HISTORY.tsv` is still the 9/27 file), and its `movers`/`coverage` output died with its scratchpad. STATUS was untouched by it, as you said. Its record is now written there.

## 2. `kalshi.py` run in both modes

- **Unsigned (this box), live 12:36–12:39Z:** `status` → stderr notice + exchange status, **rc=3**. `market KXFED-26DEC-T4.00` served full data. `pull --log` 11/11. The candlesticks endpoint `tools/t6_pin.py` uses also answered. Existing tests still pass: `test_mid_flag_edge` 7/7 and `test_search_coverage`.
- **Signed (throwaway key, offline):** new `scripts/test_cred_modes.py` **13/13**. The signature **verifies under the public key** over ts+GET+/trade-api/v2<path> (query excluded). Partial creds → unsigned; a malformed PEM → import raises (fail loud). `status` returns rc=0 signed, rc=3 unsigned. It **kills 4/4 mutants** (wrong signed path · catch-all except · dropped `sys.exit(3)` · header sent when unsigned).
- ⚠️ **A live AUTHENTICATED round-trip is UNVERIFIED.** Creds are desktop-only. At the next desktop boot, `kalshi.py status` should return rc=0. That is in my SCRATCH as 🔴.

## 3. Pulls (2026-10-15T12:39Z): figures other desks cite that changed

| Figure | Was | Now | Who cites |
|---|---|---|---|
| Fed Oct hike | PM 15.5 / Kalshi `>4.00` 18.0 (10/9, sent to LIQUID) | **PM 31.5 Gamma (27.5 CLOB) / Kalshi 29.0**. CLOB path 18.5 → 39.5 (10/14 15:00Z) → 27.5; attribution to the 3.7% CPI is INFERRED from timing | LIQUID, HENRY, BOND |
| Sept CPI | crowd mode 3.6 (10/9) | **printed 3.7** (Kalshi expiration_value) | HENRY, LIQUID, BOND, LABOR |
| Iran blockade-end by 12/31 · next meeting by 12/31 | 59.1 · 77.5 (9/27) | **37.9 · 37.5** | HAWK, BRENT, FALCON |
| Kalshi Iran crude Sept ≥2.0M bpd | context column, thin | **settled NO, 1.957M** (OPEC MOMR secondary sources). VX-ORC-04's Critical cell reads "<2.0 = real loss"; not graded (v5 UNSET; OI 226) | BRENT, HAWK, FALCON |
| Oct $110 / spread | 8.5 / +73.0 (10/9) | **9.0 / +78.5** | BRENT, HAWK, FALCON, TERRY |

ORACLE sent no new outbound packets for these; routing is yours under COMPLETION_SPEC step 6. VX-ORC-07 (>10pp/48h → PROME triage): the Oct-hike move is **+9pp/48h on CLOB, below the Alert line, and +13 on a mixed Gamma basis**. That ambiguity is exactly ⑰ item 2 below.

## 4. DAEDALUS wiring ⑰ run 3 (deferred 10/9): consumed

- **Item 1 DONE:** `workbook/VX.tsv` gains a 10th column, `Producer`, naming the command behind each row. It is encode-existing; nothing that fires changed. ORC-07's cell says plainly that **no command produces a 48h move**.
- **Items 2 and 3 change what fires.** Not encoded. For Will, please register a WQ row:
  - **VX-ORC-07 window.** ORACLE recommends **keeping the 48h letter**: the charter's KEY THRESHOLDS and its ">10pp in 48hrs → PROME" route both say 48h. Grade the State only on a 48h difference (CLOB series, or two ODDS_LOG rows ≤48h apart), and read **UNKNOWN when no 48h pair exists**; Δ7d/Δ30d stay as context. Consequence: ORC-07's 🔴, held since 9/17 on Δ7d/Δ30d evidence, would fall to Watch today (+9pp on the Oct hike). The alternative, re-lettering to Δ7d, changes a charter route.
  - **VX-ORC-08 venue.** ORACLE recommends **Polymarket**. The >66% level is the re-break of Polymarket's own aggregate Fed-HIKE-2026 peak (KB-ORC-046, 7/22). Kalshi `KXFED` is a cumulative upper-bound contract with a different definition, so it stays a corroboration column, never a trigger. ⚠️ Also for Will: ORC-08's Critical cell, "a 2026 hike prints", **was met on 9/16** (KB-ORC-083). The row has run as "LIVE QUESTION = OCTOBER" since without a ruling, so retiring it in favour of a meeting-specific row may be the cleaner fix.

## 5. For PROME (not Will)

- **C4 to verify:** `AGENTS/ORACLE/CLAUDE.md` Kalshi paragraph now describes the unsigned mode, plus a FILES row for the test. No authority, route or threshold moved (`91ab67173`).
- **`PROME/MACHINE_LOCAL.md` row 15** still says ORACLE `kalshi.py` "dies at import". That is now false; it reads unsigned with rc=3. It is your file.
- **WATCH_FOR:** the term `bank failure` (keys on ORACLE's "bank failure odds >30% any month → REGINALD" trigger and VX-ORC-01) is owed under your 9/27 condition. WALTER was told (`f6130690d`); the intake config is yours.

## Commits
`5eae08a1c` residue + tests + logs · `91ab67173` write-back + DAEDALUS consume + VX Producer · `f6130690d` ORACLE → WALTER watch term · this memo (next commit). Push receipt: in the SendMessage.

## COMPLETION — ORACLE — 2026-10-15
STATUS: ✅ DONE
CHANGED: AGENTS/ORACLE/{scripts/kalshi.py, scripts/test_cred_modes.py (new), scripts/test_mid_flag_edge.py, watchlist.tsv, kalshi_watchlist.tsv, workbook/ODDS_LOG.tsv, workbook/KALSHI_ODDS_LOG.tsv, workbook/DISRUPTION_SUPPLY_SPREAD.tsv, workbook/VX.tsv, STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, MAINTENANCE.md, CLAUDE.md, board_log.tsv, inbox/processed/…DAEDALUS…}, AGENTS/WALTER/inbox/2026-10-15_from-ORACLE_bank-failure-watch-term.md, this memo
RESULT: All 6 residue files kept: 5 complete, 1 repaired (a false "sent to WALTER" note; the term is now actually sent), 0 discarded. Appended rows (+62/+25/+1) all carry ts and market id, with no deletions. kalshi.py runs unsigned live (status rc=3, pull 11/11) and passes 13/13 offline two-mode tests that kill 4/4 mutants. 12:39Z pulls: Oct hike back to ~30 on both venues (was 15.5/18.0 on 10/9) after Sept CPI printed 3.7; Iran crude Sept settled 1.957M bpd; spread +78.5. DAEDALUS ⑰ consumed: item 1 done.
GAPS: The signed live Kalshi round-trip is unverified because creds are desktop-only (check status rc=0 at the next desktop boot). Not run: coverage (overdue since ~10/01), history --write and movers. No KB rows were added, and the STATUS dashboard tables are still 9/27 (recovery scope). The Hormuz 0-ships pin was not rolled. TRADE_MARKS is 10 writes behind.
WILL_NEEDS: Two rulings from DAEDALUS ⑰ (§4), each with ORACLE's recommendation: VX-ORC-07 window (keep 48h, UNKNOWN without a 48h pair) and VX-ORC-08 venue (Polymarket; its Critical cell was met on 9/16). Register them as WQ rows. WQ-314(b) is unchanged and still Will's.
FOLLOW-UP: PROME: route the §3 changed figures (LIQUID/HENRY/BOND · BRENT/HAWK/FALCON); C4-verify the charter edit; fix MACHINE_LOCAL row 15; encode the bank failure WATCH_FOR term. ORACLE: desktop status check; November $110 pin ~10/25–10/31; coverage sweep.
