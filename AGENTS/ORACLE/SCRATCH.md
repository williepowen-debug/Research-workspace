# ORACLE — SCRATCH (canonical session handoff)

**Last updated:** 2026-11-12 (Thu) 10:3x ET · **Box:** desktop `DESKTOP-BC6EF81`, Kalshi SIGNED (`status` rc=0) · Session: Claude Code, Opus 5.5, session oracle-a6, booted 08:48 ET on Will's boot ask; Will's "go" 08:53 ET covered WQ-671, the gate read, October CPI and closeout. Prior closeout: 2026-11-11 09:5x ET.

## THIS SESSION (11/12 08:48 ET to closeout)

- **Boot:** 0/0 vs origin; DAEDALUS's dirty file not mine, no pull. Ran-check OK (11/11 live read). Corrections rc 0. Kalshi SIGNED.
- **WQ-671 A recorded** (c756de3ddc): charter DOMAIN SCOPE owns the December FOMC priced path; STATUS matrix line naming LIQUID/HENRY replaced. Packet `PROME/inbox/2026-11-12_from-ORACLE_wq671-recorded.md` (316f34c0aa); SendMessage to prome-e8 delivered (receipt = delivery only).
- **October CPI (KB-ORC-136, 60eb093013):** no October 2025 BLS index ⇒ no October YoY; PM market prices its fallback (September's 3.7), 94.4 to 94.9. Excluded from print-miss-direction (stays n=2).
- **Huang exit (KB-ORC-137, 6ac1fce7f3; WALTER card SIG-W-20261112-002):** Kalshi KXCEONVDA determined YES 14:11:04Z; PM legs 99.95 UMA proposed. PM 12/31 leg 16.5 → 77 at 22:00–22:30Z 11/11 AFTER public after-hours WSJ reporting: not a leading indicator. Successor Kress 31–33, Buck 27. Packet `PROME/inbox/2026-11-12_from-ORACLE_huang-exit-market-read.md`; messages to WALTER (incl. chronology correction input), PROME, TERRY (no card).
- **WQ-678 A applied** (ab06498512, Will "Lets handle this now" 10:05 ET): A1 + 9 of 10 trims; T6 row kept. Charter 29,289 → 24,179 B. MAINTENANCE 2026-11-12.
- **Gate read 2026-11-12T15:15Z** (routine e8c69052e6, PM 52, Kalshi 9, spread +88.0pp) graded same session: VX-ORC-12 Alert held (90.5); VX-ORC-04 none (5.5, run 12); VX-ORC-07 🔴 Critical on the Huang CLOB pair (news-driven). KB-ORC-138 (Dec FOMC: PM 3.4 / 90.5 / 6.2; Kalshi 5 / 88 / 7; futures +26.8bp; gap closed). KB-ORC-139 bank-book-depth review (no change).
- **Not done:** full STATUS re-base (tier tables 11/06); `TRADE.md` tables; coverage sweep (due ≤11/18).

## NEXT SESSION (dated, priority-flagged)

- **🔴 Every boot:** `tools/routine_check.py`, grade the routine rows into `V5_NOV110_READS.tsv`, VX-ORC-04, VX-ORC-12; December read in the KB-ORC-138 form (venues + futures). Next gate read Fri 11/13 10:15 ET.
- **🔴 Huang PM legs:** confirm UMA settlement (proposed at 11/12 14Z); watch successor (Kress/Buck) and AI bubble into Nvidia Q3 Tue 11/17 ~1:20 pm PT.
- **🟠 Full STATUS rewrite:** re-base tier tables and matrix to a current pull (11/06 vintage under the 11/12 alerts).
- **🟠 Rolls:** R3 switch 2026-11-17T01:00Z (INFERRED) resets the arming run · December $110 at listing (~11/25; bump REGIME) · Hormuz weekly → week-of-11/16 · pause legs: by-11/8 leg 32.5 still open (window closes ~11/22).
- **🟠 Nomination to VULCAN via PROME:** Huang CEO legs are resolved, drop that nomination; the successor market (PM `next-ceo-of-nvidia`, Kalshi `KXNVDACEO-29JAN`) is the candidate now. Blockade-end by 12/31 still a nomination.
- **🟠 Kalshi CPI:** pin `KXCPIYOY-26NOV` rungs after HENRY's view (note KB-ORC-136: November YoY base exists, Nov 2025 = 324.122).
- **🟠 `TRADE.md`:** regenerate tables from `TRADE_MARKS.tsv` (rendered as of 11/04).
- **🟠 Russian diesel nomination** (BRENT/OSPREY), no pin without the owner's read.
- **🟡 Coverage sweep due ≤11/18.**
- **🟡 Combination reviews:** 11/16 strike-vs-oil, diplomacy-drift · 11/19 polymarket-integrity, ai-unwind-read (KB-ORC-137) · 11/20 venue-legal-risk · 11/26 bank-book-depth · 12/11 print-miss-direction.
- **🟡 ~12/10: October CPI market fallback resolution** (KB-ORC-136) → HENRY.
- **🟡 2026-12-15: Kalshi gap-fill quarterly re-check** (WQ-305).
- **🟡 Carried:** DAEDALUS F-1 Brier (bank-failure family) · NEH PDF unread · KB-ORC-086 sweep · WQ-295 WATCH_FOR check · WQ-599 daily-grading owner (unowned per the ruling record).

## CARRY-FORWARD

- **Push state:** 11/12 commits c756de3ddc, 316f34c0aa, 60eb093013, 6ac1fce7f3 already on origin (carried by another desk's push); ab06498512 (charter) and the 11/12 closeout commit go by `scripts/safe-push.sh` at closeout; receipt in the reply to Will.
- **Combination themes (`combo:` in KB Notes):** strike-vs-oil · diplomacy-drift · polymarket-integrity · bank-book-depth · ai-unwind-read · print-miss-direction · venue-legal-risk.
- **Cadence settled:** PROME 11/04: one read per weekday stands. The letter has no halt rule, and I did not propose one (Will 10/31: fewer rules).
- **`TRADE.md` refresh:** rerun `tools/trade_marks.py --write`, then regenerate the tables; never hand-type a vintage.
- **Fed futures method (verified 11/11, same as HENRY's):** Dec average = 100 − ZQZ26; post = (31 × avg − 9 × EFFR) / 22; unit check ZQX26 = EFFR. Full precision via `.venv/bin/python` yfinance (fetch.py rounds to 2 dp). One 0.005 tick = 0.7bp. NY Fed EFFR API `markets.newyorkfed.org/api/rates/unsecured/effr/last/3.json`. BLS API has a daily request limit shared on this box.
- **Standing framing (do not re-derive):**
  - **In a fast move read the CLOB book, not Gamma:** Gamma showed 3.75 at 00:48Z 11/07 against CLOB 21/34 (KB-ORC-130). Take several book reads and quote ranges; `liq` overstates near-touch depth.
  - **A closed market drops out of the plain Gamma slug query** (IndexError); `polymarket.py pull` finds it through its `closed=true` fallback and prints RESOLVED. A pin gone missing may be the event firing.
  - **Kalshi pull's printed `Δp` is the API's previous-price change, not the change from my last log row.** Difference against `KALSHI_ODDS_LOG.tsv`.
  - Quote a Fed move from the level held before it, with its basis. A read that catches a spike overstates the fall (KB-ORC-126). `end_period_ts` on Kalshi candles = period END.
  - Fed: hiked 25bp 9/16 to 3.75–4.00% (KB-ORC-083); HELD 10/28 (KB-ORC-109). Venue-vs-futures only in expected bp at a matched time (KB-ORC-100). **December priced path is ORACLE's (WQ-671 A):** each read = venue odds + futures cross-check, both caveats (Yahoo last trades not settlements; futures = size, not odds).
  - **October 2026 CPI YoY does not exist at BLS** (no October 2025 index, shutdown gap); PM's October market resolves on its fallback (September's 3.7) at the next CPI release (KB-ORC-136). Any YoY market whose base month is October 2025 inherits this.
  - v4 is history; ⛔ never compute `82.5 − 100`. v5 at $110 since 9/24 (WQ-260). Never difference across segments. Current segment `v5-nov26-icewti110`.
  - PM "ceasefire" = no US strike landing on Iran (KB-ORC-111). Never difference the retired legs against the effective series. A resolution applies the market's rule; FALCON owns the event grade.
  - A later pull on the same ET date is context (O3). A US business day is an NYSE trading day (letter §10.2), so weekend reads are context.
  - Hormuz legs resolve on the IMF PortWatch PRINT (KB-ORC-079).
  - Kalshi mid only when `result` empty AND OI > 0 (KB-ORC-086).
  - Recession venues use different definitions (KB-ORC-099).
  - Three published σ remain retracted (KB-ORC-064). CME FedWatch unreachable: do NOT re-attempt `WebFetch`; Yahoo `ZQZ26.CBT`, `ZQF27.CBT` plus NY Fed EFFR gives HENRY's method for a unit match. Treasury par == DGS10 unconfirmed (BOND/TERRY).
  - Polymarket trades: v1 retired. Use `data-api.polymarket.com/v2/trades?condition=<conditionId>&limit=500` (an `offset` parameter returned HTTP 400 on 11/07), fields `proxy_wallet`, `side`, `outcome`, `size`, `price`, `timestamp`; returns `{data: [...]}`.
  - Polymarket `prices-history`: use `curl -A "Mozilla/5.0"` with startTs/endTs and fidelity 60 or 180 (urllib gets 403).
  - Never `pull --log --force` to log new pins. Kalshi `pull` has no double-log guard.
  - Git: `rebase --continue` refuses while ANY tracked file is unstaged and blames merge conflicts; `rebase --abort` silently discards a foreign dirty file.
- `ledger_staleness` counts `HISTORY.tsv` but prints no row for it (PROME's tool; reported, not patched).

## OPEN HYPOTHESES

- **Possibly the crowd separates limited strikes from a supply shock (UNPROVEN).** First test 11/07: a confirmed minor strike resolved the legs while WTI $110 fell 19.5 → 17.0 and invade and war stayed flat; two thin Kalshi Brent rungs rose. Futures were shut, so Sunday's reopen is the real test. Read 2 (11/08 16:58Z): the new pause market priced about 76 for another strike in 14 days, while WTI $110 held 17.0 and invade held 10.5. The crowd prices more strikes but no supply shock. HAWK and BRENT own the reality.
- **Fed size:** the 11/11 gap (venues +50 at 11–12 vs futures about 16–19) closed 11/12 (venues +25.6bp, futures +26.8bp; +50 6.2). Treat as resolved unless it reopens.
- **The 11/05 Fed fall may be a risk-off reflex, not a Fed read (UNPROVEN).** Five markets moved together 10:40–10:50 ET; odds rebounded 11/06, 6 points before the print and 8 after. No driver found. LIQUID and HENRY own the reality.
- **Deal hopes may explain the 11/04 oil drop (cause NOT established).** Blockade-end 3/31/27 69.5 (11/07) is the check; deal top component 11.5.
- **Bank-failure crowd = the 2024-25 prior, not 2026 data.** Test in F-1 (Brier). Book stayed dead through a −2.46% KRE day ($2.2K liq 11/06).
- **Recession gap = PM's extra NBER leg** (structural). Kalshi 3.0 vs PM 4.5 at 11/07 13:43Z.
- **Complacency decoupling:** S&P best-asset 87.5 (11/07) after a −4.4% day; gold leg not re-read.
- **Crowd misses on prints may lean the same way (UNPROVEN, n=2):** CPI above the mode, U3 below it. October CPI excluded (fallback rule, KB-ORC-136); next point November U3 (12/04).
- **Huang-exit pricing reacted, did not lead (11/11–11/12):** the overnight fade from 92.5 to 74 says the crowd doubted the board outcome; successor odds are the live read now.
