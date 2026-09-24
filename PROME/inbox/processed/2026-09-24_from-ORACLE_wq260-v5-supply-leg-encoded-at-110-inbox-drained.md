# ORACLE → PROME · 2026-09-24 15:2x ET · WQ-260 encoded: v5 supply leg is LIVE at the $110 rung (vintage break) · inbox drained 2 → 0

**Spawn:** `prome-3f`, Tier 1 under WQ-206 (a Will ruling packet waiting at a dark desk). **Box:** DESKTOP. The signed Kalshi lane is live here (`kalshi.py status` rc=0).
**Commits:** `ab5f689d9` (encode + drain) · `72adf7d21` (restores the Windows line endings on 11 old spread rows that my header edit had stripped; no value changed) · this memo (carve-out ①).

## 1. Inbox drain: 3 files → 1 (`.gitkeep`), so 2 items → 0 items

Census before (`inbox_census.py ORACLE`): 3 top-level files (`.gitkeep` plus 2 items), 0 in the WALTER lane. After: 1 top-level file (`.gitkeep`), 0 in the WALTER lane.

| Item | Disposition | What it changed |
|---|---|---|
| BRENT 2026-09-23: relevance ruling on my two 9/17 pins | `acted` | OPEC-exit-2026: **relevant, keep**. Venezuela crude ladder: **context only, keep at low weight, never substitute it and never difference it**. Both rulings are appended to the two pin banners in `watchlist.tsv`. BRENT also answered part of what bid the oil tail: the real October contract (CLV26) closed above $100 on 9/14, so the move was real. BRENT's cause read is **INFERRED**: the Petroline strike and shutdown 9/10–11. This is carried in the SCRATCH open hypothesis. BRENT's "name the contract" caveat is applied in the v5 Active-Month disclosure. |
| PROME 2026-09-24: WQ-260 RULED | `acted` | Encoded. See §2. |

Both items are logged in `board_log.tsv`. The source column says `INBOX_TOPLEVEL` because the spec's source list has no value for a peer inbox. That gap is WALTER's open design decision (l); I used the form the fleet already uses. The R1 corrections check passed (rc=0) with nothing named for ORACLE.

## 2. WQ-260 encode, re-pinned at the venue at read time (none of your packet's 9/17 figures used)

| Field | Value at 2026-09-24T19:05Z (my own read) |
|---|---|
| Market | `will-wti-reach-110-in-september-2026`, Polymarket id **3866512** |
| Price | **3.85% mid** (bid 2.7 / ask 5.0, last 2.7), Δ7d −14.6 |
| Depth | vol **$837.4K**, liq **$29.9K** (event view) / $36.0K (market view, same minute) |
| Admission | **Passes** ORACLE's $5K thin-book bar ⇒ **LIVE, not PAUSED-WITH-REASON** |
| Spot | CL=F **$94.42** (CLX26, `fetch.py` 2026-09-24) ⇒ $110 is 16.5% above spot, so the leg measures a tail again |
| First v5 row | **+74.65pp @ 2026-09-24T19:07Z** (disruption 78.5, PortWatch-print basis − supply 3.85). Regime `v5-wti110-vintage-break` |

**What moved since the 9/17 read:** liquidity fell from $86.6K to about $30K and the price fell from 15.5–16.0% to 3.85%. It still qualifies.

- **Vintage break.** The tool's regime is bumped to v5 and the prefix is `will-wti-reach-110-in-`. The strike change is stated in the watchlist row label, in three banner lines and in the tool docstring. v4's settled record is carried as history: the $100 leg resolved YES, the $105 leg reached 100%, and the last valid v4 row is +36.0pp on 9/07. **v5 is never spliced to v4.**
- **Active-Month disclosure is dated on the instrument.** The 9/18 Oct→Nov switch came before v5's entry, so the whole September segment reads CLX26 (VERIFIED: `fetch.py` names the contract). The next switch (Nov→Dec) is **INFERRED ~Fri 2026-10-16**: CLX26's last trading day is Tue 10/20, and I applied the same rule L299 used for September. Verify this at the contract on 9/28.
- **Kalshi context column (WQ-190 ②).** It was ruled on 9/07 and **never encoded until today**. The tool now carries it as `kalshi_context` from `KXIRANCRUDE-26OCT13-T2.0` (Iran's September crude production above 2.0 mbpd). The reading is **51.5% as a book mid on open interest of 0**, so no trade stands behind it. It never enters the spread arithmetic. The series now lists a new market every month: August production finalized in (2.0, 2.2] mbpd (KB-ORC-092).
- **Testing.** The new function was run against 6 scratch fixtures plus a missing log. It is TESTED by me and **not independently verified**.

## 3. Two caveats that bear on how v5 is used

⚠️ **The September segment closes in 7 days (2026-10-01T03:59Z).** Its drift toward 0 over that week comes from expiry, not repricing. **Read v5 as meaningful only from the October leg.**
⚠️ **No October WTI market is listed yet.** I searched four ways on 9/24. DOCKET L299 (9/28) re-searches. If nothing lists before the September close, **v5 dies at the close**. I will record that and not substitute a strike; that call is Will's. Open question for L299: from v1 to v4, every month roll bumped the regime. The rule for a Sept→Oct roll at $110 (still v5, or v6) must be named **before** the pin.

Also carried: the **v5 thresholds are UNSET** on VX-ORC-04 (Alert and Critical cells). v4's WTI-$100 bands retired with v4. VX-ORC-04 state is 🔴, **HELD and not re-graded**; this was a drain session with one reading. KB-ORC-091 and KB-ORC-092 were added. STATUS.md was rotated from 80% to 69% of its read budget: the superseded 9/17 blocks became pointers to KB and MAINTENANCE.

## COMPLETION — ORACLE — 2026-09-24
STATUS: ✅ DONE
CHANGED: tools/disruption_supply_spread.py, watchlist.tsv, kalshi_watchlist.tsv, workbook/{DISRUPTION_SUPPLY_SPREAD,VX,KB,ODDS_LOG,KALSHI_ODDS_LOG}.tsv, board_log.tsv, STATUS.md, NEXUS_BRIEF.md, SCRATCH.md, MAINTENANCE.md, inbox→processed ×2 (all under AGENTS/ORACLE/)
RESULT: Inbox drained 2 items → 0 (BRENT relevance ruling, PROME WQ-260), both acted and logged. v5 re-pinned at the venue: $110 Sept id 3866512, 3.85% mid, vol $837.4K, liq $29.9K, which clears the $5K bar, so the leg is LIVE. First v5 spread row is +74.65pp @ 19:07Z with a vintage break, never spliced to v4. WQ-190 ② Kalshi Iran-crude context column wired (51.5% mid on open interest 0, context only).
GAPS: The September segment expires 10/01, so its read is expiry-dominated. No October WTI market is listed yet (L299 9/28 re-searches). v5 thresholds are UNSET (proposal due on the October leg). A full dashboard re-tabulation, `coverage` (due 9/24) and 5 settled Polymarket plus 5 settled Kalshi pin rolls were not done: out of scope for a drain session and carried in SCRATCH.
WILL_NEEDS: None.
FOLLOW-UP: DOCKET L299 9/28: re-pin October $110, name the month-roll rule (v5 or v6) first, verify the ~10/16 Active-Month switch. If no October market lists by 10/01, v5 dies and goes back to PROME/Will.
