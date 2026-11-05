# ORACLE — SCRATCH (canonical session handoff)

**Last updated:** 2026-11-04 (Wed) 20:14–21:0x ET (from `date`) · **Box:** LAPTOP `WilliePOwen`, Kalshi UNSIGNED (`status` rc=3, public market data). · Session: oracle-12, Claude Code, Opus 5.5; boot, then Will 20:40 ET "get caught up on any new data". Prior: 2026-10-28.

## CHANGES SINCE 10/28 (ORACLE dark 10/29–11/04; the routine pulled, nothing graded)

- **Fed held 10/28; December hike ~80.** Reads 79.5 · 69.5 · 70.5 · 70.5 · 73.5 · 80.5.
- **Polymarket halted trading 10/29 18:33Z** (vendor compromise; SIG-W-20261029-045).
- **WTI fell from ~$102 to ~$88.** Nov $110 read 64.0 on 10/30, 25.5 on 11/04, 13.0 context tonight.
- **Mon 11/2: reported US strikes on Qeshm** (SIG-W-20261104-002, -019). Ceasefire 11/30 and 12/31 resolved NO 11/03. New effective-ceasefire series 11/04.
- **Midterms 11/3:** Democrats House and Senate, both PM YES.
- **11/04 oil −8% to −9% on deal hopes;** no deal or reopening established (SIG-W-20261104-078).

## WHAT I DID (11/04)

- **Rebase:** laptop's 11/02 19:15 ET routine commit stopped CATO's boot pull at 20:13. Resolved my own commit (d8e2dae040): desktop bytes + laptop rows in time order, 69 insertions, 0 deletions. DAEDALUS cleared its dirty `GATE_LOG.tsv` itself. PROME verified and gave the all-clear 20:20 ET.
- **Pulls** 2026-11-05T01:40Z: PM 52 rows · Kalshi 11/11 · spread +76.5. 01:45Z: 11 new pins. `history --write` · `coverage` · `movers`.
- **Graded:** VX-ORC-04 Alert fired 10/30, cleared 11/04 (ledger + letter §10). VX-ORC-07 🔴 Critical. VX-ORC-12 Alert held since 10/29.
- **KB-ORC-111 to 115.** ceasefire · effective series · Nov $110 · midterms · NEH.
- **`polymarket.py`:** `closed_outcome()`; `✅ PIN RESOLVED` prints the outcome.
- **Rolls:** full list in MAINTENANCE 2026-11-04.
- **Inbox 5/5 filed.** DAEDALUS packets answered (Census BUILD + DECLINE, Wiring #9, Gate Basis #3). SIG-045 caveat carried in the ledger. SIG-038 context.
- **Packets:** FALCON, BRENT, HAWK, PROME, DAEDALUS (all `2026-11-04_from-ORACLE_*`).
- Commit hashes: `git log --since=2026-11-04 -- AGENTS/ORACLE/`.

## NEXT SESSION (dated, priority-flagged)

- **🔴 Every boot:** `tools/routine_check.py`, then grade the routine rows into `V5_NOV110_READS.tsv` and VX-ORC-12. Next ledger row is ET 11/05.
- **🔴 Fri 11/06 October jobs:** read Kalshi U3 `>4.1` 68.0 / `>4.2` 27.0 against the print; then roll to November U3.
- **🔴 Read FALCON's FAL-07 result** when it lands, against KB-ORC-111.
- **🟠 Effective ceasefire:** any leg resolving NO = another qualifying strike. The rows are T1; `✅ PIN RESOLVED` now shouts it.
- **🟠 Rolls:** Hormuz on-date · Hormuz closure context rung · Kalshi Brent date ladder · `KXCPIYOY-26OCT` · Hormuz weekly → wk-of-11/9 · December $110 at listing (expect ~11/25 by prior pattern; bump REGIME, one edit) · R3 switch 2026-11-17T01:00Z (INFERRED) resets the arming run.
- **🟠 Russian diesel nomination** (BRENT/OSPREY; coverage 11/04). Do not pin without the owner's read.
- **🟠 Next coverage sweep due ≤11/11.**
- **🟠 Daily grading owner:** PROME to establish who launches the daily ORACLE grade. CATO's preset shipped 10/29 (c7519854e3); L848 PENDING acceptance. Review 11/04: no more frequent collection and no new checker before that.
- **🟠 KB rows still owed from 10/15:** Sept CPI calibration datum (print 3.7 vs mode 3.6) · Iran crude 1.957M.
- **🟡 2026-12-15: Kalshi gap-fill quarterly re-check** (WQ-305).
- **🟡 At the next DESKTOP boot: `kalshi.py status` must return rc=0.**
- **🟡 Carried:** DAEDALUS F-1 Brier (bank-failure family) · NEH PDF unread · KB-ORC-086 sweep · TRADE.md prose refresh (last refreshed 8/27, committed 9/25; `TRADE_MARKS.tsv` rebuilt 11/04, 14 of 14 marks; declared marks still key on the retired wti_100 family) · WQ-295 WATCH_FOR check · archive `DIVERGENCE_2026-07-09.md` + `OPEN_THREADS_2026-07-09.md`.

## CARRY-FORWARD

- **Push state (11/04 closeout):** all ORACLE work pushed through `scripts/safe-push.sh`; the session's commits are `git log --since=2026-11-04 --grep=ORACLE`. d8e2dae040 went out earlier in the same chain.
- **Open asks:** PROME packet gap 2 (one read per weekday treated as the November cadence unless ruled otherwise). Will has not ruled on a halt rule; the letter has none, and I did not propose one (Will 10/31: fewer rules).
- **Standing framing (do not re-derive):**
  - Fed: hiked 25bp 9/16 to 3.75–4.00% (KB-ORC-083); HELD 10/28 (KB-ORC-109). Venue-vs-futures only in expected bp at a matched time (KB-ORC-100).
  - v4 is history; ⛔ never compute `82.5 − 100`. v5 at $110 since 9/24 (WQ-260). Never difference across segments. Current segment `v5-nov26-icewti110`.
  - PM "ceasefire" = a US strike landing on Iran (KB-ORC-111). Never difference the retired legs against the effective series.
  - A later pull on the same ET date is context (O3). A US business day is an NYSE trading day (letter §10.2).
  - Hormuz legs resolve on the IMF PortWatch PRINT (KB-ORC-079).
  - Kalshi mid only when `result` empty AND OI > 0 (KB-ORC-086).
  - Recession venues use different definitions (KB-ORC-099).
  - Three published σ remain retracted (KB-ORC-064). CME FedWatch unreachable: do NOT re-attempt `WebFetch`. Treasury par == DGS10 unconfirmed (BOND/TERRY).
  - Polymarket `prices-history`: use `curl -A "Mozilla/5.0"` with startTs/endTs and fidelity 60 or 180 (urllib gets 403).
  - Never `pull --log --force` to log new pins.
  - Git: `rebase --continue` refuses while ANY tracked file is unstaged and blames merge conflicts; `rebase --abort` silently discards a foreign dirty file.
- `ledger_staleness` counts `HISTORY.tsv` but prints no row for it (PROME's tool; reported, not patched).

## OPEN HYPOTHESES

- **Possibly the crowd separates limited strikes from a supply shock (UNPROVEN).** Another strike 58.5 by 11/30 vs $110 at 13.0. Separate contracts with different rules, participants and liquidity give no read on oil conditional on a strike. HAWK and BRENT own the reality.
- **Deal hopes may explain the oil drop (cause NOT established; SIG-W-20261104-078 reports drivers only).** Rapidan says odds still favor escalation; CIBC says the drop may be overdone (SIG-W-20261104-078). Blockade-end 12/31 43.4 is the check.
- **Bank-failure crowd = the 2024-25 prior, not 2026 data.** Test in F-1 (Brier). All books thin ($2.0K liq tonight).
- **Recession gap = PM's extra NBER leg** (structural).
- **Complacency decoupling:** S&P best-asset 84.5; gold 2.7 — the registered tell has not fired. NEH left this hypothesis: it is a high-bar basket (KB-ORC-115).
