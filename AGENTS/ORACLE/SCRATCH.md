# ORACLE — SCRATCH (canonical session handoff)

**Last updated:** 2026-09-24 (Thu) ~21:50 ET (2026-09-25T01:5xZ) · **Box:** DESKTOP, authed Kalshi lane LIVE (`kalshi.py status` rc=0) · Session: full update at Will's direction (*"We need to update"*).

## CHANGES SINCE LAST SESSION (9/24 afternoon drain → 9/24 evening)

- **PROME packet** (committed `6f2c3a38a`): three "$100" strings in `tools/disruption_supply_spread.py` → **fixed** (L78, L81, L238). Doorbell received from `prome-1f`.
- **Tape:** Fed Oct hike 50.5 → **66.5** (PM) / ≈65 (Kalshi); 10Y **5.1% rung settled**; first **US–Iran round 9/22** (UN, Qatar-mediated); Hormuz ship-targeting legs settled/near-settled 9/18, 9/21, 9/23; recession PM 8.5 → **10.5**.

## WHAT I DID

1. **Boot:** no pull needed — 0 behind origin (1 ahead = PROME's unpushed `6f2c3a38a`); other desks dirty (HENRY, PROME, HEARTBEAT) so pull was barred anyway. Corrections check **rc=0**. Inbox 1 → 0 (`processed/`, board_log row).
2. **Script fix** (PROME ASK) — see MAINTENANCE 2026-09-24 (evening).
3. **Dual-venue pull:** Polymarket `pull --log` 51 + new-pin rows; Kalshi 13 → 14 tickers; `history --write` 8,155 rows; `movers` (11 hits → one pinned); **`coverage` run** (5 hits, same themes as 9/17, nothing pinned; next due ~10/01); `metrics.py collapse` clean; spread **v5 row 2 +74.10pp**.
4. **Rolls:** PM — Aug CPI → Sept CPI · Hormuz weekly → wk-of-9/21 · Saudi by-date → on-date (basis change) · BOJ Sept retired. Kalshi — Fed Sept → Oct `>4.00` + Dec `>4.25` · Aug CPI ×3 → Sept `>3.5/>3.6/>3.7` · BOJ Sept → Oct. **New pin:** US–Iran next senior meeting.
5. **Records:** KB-ORC-093 (Fed), 094 (10Y), 095 (Iran talks vs tempo), 096 (recession gap). VX-ORC-02/04/08 refreshed (08: Alert cell >66% met on PM, one print, not re-graded). STATUS fully re-tabulated (51% of read-cap), NEXUS_BRIEF rewritten, MAINTENANCE appended.
7. **"Go deeper" pass (Will):** Fed drivers + CME gap (KB-ORC-097); Iran ultimatum + two new ladders (KB-ORC-098); **fixed `coverage`/`movers` silent 100-row cap** (MAINTENANCE late entry); outbox signals → LIQUID/BOND/HENRY/RED and HAWK/BRENT/FALCON. A second full `pull --log` re-logged the watchlist ~40 min after the first (10-min guard expired) — duplicate snapshot rows, harmless.
6. **Verified externally:** 9/22 talks — Axios, Times of Israel, Israel Hayom, ANI. ⚠️ Witkoff: US side talked **through mediators**; PM resolved "attend" YES anyway.

## NEXT SESSION (dated, priority-flagged)

0. **🔴 ~Tue 2026-09-29 — Iran's 5-day deadline.** Re-read the new ceasefire (thru 9/30 85.5%) and blockade-end (by 9/30 8.5%) ladders with `event` — the dashboard top leg is wrong for both (settled 9/20 rung / thin Mar-2027 rung). Also re-read Fed Oct vs the CME figure (KB-ORC-097) — do the venues converge up toward ~77% as in September?

1. **🔴 Mon 2026-09-28 — DOCKET L299, October WTI $110 re-pin.** Search for an October $110 market; if listed, pin + **name the within-v5 roll rule before rolling** (v4 precedent: month rolls bumped REGIME). If none by the **2026-10-01T03:59Z** September close, **v5 dies — write it down; a new strike is Will's call.** Verify the inferred Active-Month switch (~Fri 10/16; CLX26 last trade Tue 10/20) at the contract. Script strings now say $110 (fixed 9/24).
2. **🔴 Re-read the Fed Oct legs** — VX-ORC-08 Alert cell (>66%) met on ONE PM print (66.5) and ~1pt short on Kalshi. Second read before any re-grade.
3. **🔴 READ `KXRECSSNBER-26` RULES TEXT — 4th carry, and the gap WIDENED (~3 → ~4.5pp).** One public call. Top mechanical item.
4. **🟠 Propose v5 thresholds to PROME** (VX-ORC-04 Alert/Critical UNSET) — on the October leg, not the expiring September one. DAEDALUS PR#6 ① due **9/30** is sequenced on this.
5. **🟠 ~9/28 roll Hormuz weekly → wk-of-9/28** (listed, $7.1K). **9/30–10/01:** 10Y/30Y Sept ladders, Houthi 9/30, Hormuz Sept ladders, Saudi on-date, Kalshi Brent Sep-30 all resolve — roll or retire each.
6. **🟠 Sat 2026-10-10 (T-4) — re-read Sept CPI ladder** for the clean like-for-like vs August's T-4 (63.0 / 25.0 / 10.0). "+73pp" not quotable until done.
7. **🟠 Kalshi Fed pins are keyed to the 4.00% upper bound** — re-key after the next Fed move (a cumulative rung is only a meeting proxy relative to the current bound).
8. **🟠 Roll the Kalshi Iran-crude context column monthly** (next: October-production event when listed). OI 0 — never cite as a probability.
9. **🟠 Sweep past ORACLE surfaces for a 50.0-mid citation off a settled Kalshi rung** (KB-ORC-086) — open check, not a clean bill.
10. **🟠 DAEDALUS F-1** — make `CLAUDE.md:201` executable (Brier per resolved market). Inputs exist (`ODDS_LOG`, `HISTORY` 8,155 rows, `TRADE_MARKS`). Best test case: the 9/07 Fed coin flip vs the 86¢ settle. Declare the short-dated-leg bias in its header.
11. **🟡 Read NEH's resolution text** (open hypothesis below).
12. **🟡 Recommend demoting the four Kalshi gap-fills to a DATED QUARTERLY re-check** (KB-ORC-089) — needs a CLAUDE.md edit ⇒ flag to PROME, do not self-edit.
13. **🟡 `T6_PIN.tsv` — freeze it or drop it from `LEDGER_GLOB`** (5th slip; DAEDALUS F-2).
14. **🟡 Owed to DAEDALUS (Tier-2): the spec-has-implementation prototype.**
15. **⚪ Archive `DIVERGENCE_2026-07-09.md` + `OPEN_THREADS_2026-07-09.md`** (mutual-reference pair).

## CARRY-FORWARD

- **Push state:** this session's commit(s) → see `git log AGENTS/ORACLE/`; pushed via `scripts/safe-push.sh` at closeout (receipt line recorded in the closeout message to Will). PROME's `6f2c3a38a` rides out with it.
- **Concurrent sessions live on this box** (PROME `prome-1f`, HENRY dirty at boot). Path-scoped commits only.
- **Standing framing — do not re-derive:**
  - **Fed hiked 25bp to 3.75–4.00% on 2026-09-16** (Kalshi settle `result: yes`, 86.0¢ last; 12-0). KB-ORC-083.
  - **v4 is history** ($100 leg settled YES; last valid +36.0pp 9/07). ⛔ Never compute `82.5 − 100 = −17.5pp`. **v5 at $110 since 9/24** (WQ-260).
  - **Hormuz legs resolve on the IMF PortWatch PRINT, not throughput** (KB-ORC-079) — a detection failure and a real stoppage resolve identically.
  - **Kalshi mid rule:** only when `result` empty AND OI > 0 (KB-ORC-086).
  - **`⛔RESOLVED` flag is trustworthy since the 9/17 selector fix** (KB-ORC-090); `PINNED BUT NOT FOUND` still can't tell resolved from bad slug.
  - **Three published σ remain retracted** (KB-ORC-064 → `CORRECTED`; `metrics.py verify`).
  - **No lead-lag claimed** between Fed venues; CME FedWatch unreachable — do NOT re-attempt `WebFetch`.
  - **Treasury par curve == DGS10 is unconfirmed** — BOND/TERRY own.
- **`ledger_staleness` counts `HISTORY.tsv` but prints no row for it** — PROME's tool; reported, not patched.
- **RED's transferable point, adopted:** a coverage gap and a delinquent owner look identical from outside — any matrix row with an empty "our thesis" cell >60 days gets a STRUCTURE question to the owner before another chase.
- **NEXUS + RED owed the 71.5%→aggregate relabel** — NEXUS applied 8/28; RED's side still open.
- **DAEDALUS owes me the three-window vocabulary; profile clock → 2026-10-20.**
- **The coverage lesson (9/17), kept:** a pre-commitment to re-check is worth nothing without a session to honour it in — a deferral should name the date it becomes invalid or be escalated to someone awake.

## OPEN HYPOTHESES

- **Iran — three axes, not two (updated 9/24).** Talks **opened** (first round 9/22; next by Dec 69%), the year-end Hormuz leg **ticked up** (17.5 → 22.5), yet near-term tempo **rose** (targeting settled/near-settled 9/18, 9/21, 9/23; 0–5 transits band 88.5%). Candidate read: attacks as leverage around the talks, priced as a near-term cost with a slightly better year-end. **Not a finding** — HAWK owns the reality; PortWatch caveat applies to every transit leg.
- **What bid the oil supply tail? — partly answered by BRENT 9/23:** CLV26 closed >$100 on 9/14 (real price move). Cause INFERRED (Petroline strike 9/10–11; Yanbu loadings stopped from 9/11, single vendor Kpler). The $68.7M invasion contract still never reacted (14.5%, Δ30d −1).
- **Recession gap = disjunction premium?** PM (disjunction) 10.5 vs Kalshi NBER-only 6.0 — widening. Unresolvable until the Kalshi rules text is read.
- **NEH — complacency or a very high bar?** 82.5%, Δ30d +1, through a hike, $105 oil, a hot CPI and 10Y >5.1%. Resolution text unread.
- **8/27 complacency decoupling — regime change, tilting further.** Best-asset S&P leg 53.5 (Δ30d +0), still ~14pp below August. The registered tell (gold retaking the lead) has not fired, and the NEH half of VX-ORC-09's tell is un-fireable.
