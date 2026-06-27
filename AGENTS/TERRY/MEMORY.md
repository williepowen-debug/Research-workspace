# TERRY — Cross-Session Memory

**Purpose:** lean DURABLE layer — mandate + accrued lessons/decisions, not a log.
Activity detail lives in commit messages, daytrading/JOURNAL.md, and `memory/auto/`.
Keep this load-bearing: append a Durable Finding only when it survives the episode.

---

## Mandate (one line)

TERRY converts thesis into trade plans with explicit entry/invalidation/sizing/expiry/
roll rules and an approval gate. **Owns the ACTION/card side, not macro truth. Never executes.**
Detection (HY-280 break, print alerts) is LIQUID/SENTRY; TERRY owns everything AFTER the alert.

---

## Standing Decisions (Will-set — load-bearing)

- **Max loss = $500 per card** (Will 2026-06-26). Applied to all fire cards + setups.
- **Fresh capital deploys ONLY on a fired trigger** (Will 2026-06-26) — never a mechanical/calendar
  book-reshape; limited funds = dry powder. Reshape = recycle decaying premium, no new net risk.
- **Default risk ceiling:** 0.25× Kelly or lower (RISK_SCORING.md). Final size = min(Kelly, max-loss, liquidity, event-risk).
- **Day-trading review = bounded SIDE project, subordinate to the thesis system** (Will 2026-06-27). Its only job: plug discretionary-scalp leaks so it can *generate dry powder* to deploy on **researched** thesis trades. It must **not** displace or co-equal the core thesis/fire-card work (transmission thesis, regional/credit cards) or absorb session attention. *Don't let the journal become the system.* (Currently underwater — S3 −$3,969, cumulative −$1,017 — so it's funding nothing: fix the leak, keep it small.)
- Open Q for Will (unresolved): preferred risk UNIT ($/%/R); track-all-considered vs approved-only.

---

## Durable Findings

- **Trigger→card must be MINUTES not hours.** The slow steps are live re-marking + grading.
  Pre-lock structure/strikes/kill-lines in a fire card; only the LIVE-MARKS block is filled at fire (rule #4).
- **Option marks go phantom in state files** — always pull a live chain at fire (chain_fetch.py / live broker),
  never cite stored option marks. Image/broker snapshots are not authoritative (rule #3).
- **The 3 Q2 bank-print mis-grade traps** (now hard guards in grade_print.py): WAL NCO adjusted-vs-GAAP
  (39bps was NON-GAAP adj; GAAP ~1.45%); ZION AOCI total-AFS not muni-only (~$869M FV is NOT the mechanism);
  ALLY collective/growth build = BETA → non-counting for path (a) even though Prov>NCO.
- **DISC-1 ≠ path-(a) tally membership.** Specific/collective classification applies to ANY name's build;
  only the regionals {CFG,OZK,EGBN,WAL} feed the ≥2 path-(a) count. Consumer/gate names (SYF/ALLY/COF) classify but don't tally.
- **Day-trading — leak CONFIRMED REPEAT + engine is regime-conditional (S2→S3):** S2 (5/1–6/23) +$2,951.67;
  **S3 (6/24–26) −$3,968.84** — wiped S2, cumulative 5/1→6/26 −$1,017. Walk-to-$0-expiry leak fired BOTH reviews
  (S2 −2,793/19, S3 −1,624/5). The QQQ 0DTE engine (+$3,044 in S2 trend) **reverses in whipsaw** — both-ways is a
  chop tactic, NOT a whipsaw tactic. NEW R6: don't hold 0DTE into RH's ~3pm auto-liquidation window (≈$327 lost on
  the 6/26 709P, force-closed before a settlement it would have won). Detail in daytrading/.
- **No closed Terry-reviewed thesis trades yet** — POSTMORTEMS.md is template-only until one closes.
- **`SIGNALS.tsv` = the trade-construction context ledger** (Will 6/27, "store in lasting memory, don't put everything of value in STATUS" → option B). Durable home for anything that shapes timing/sizing/structure but isn't the thesis. `source` column spans WALTER (routed INFO), TERRY-chart (my own levels/IV/expected-move), and thesis-owner timing notes (REGINALD/CARL/LIQUID/… scaffolding, NOT their thesis truth). NEXUS regime = one **PIN** row (denominator), refreshed not streamed. Decay-tracked (as_of/decay/conf/status); `boot.py` surfaces PIN + active rows, flags >21d for re-verify/retire. OUT of scope: thesis truth + raw catalyst calendar. STATUS keeps only a one-line read + pointer. New context → add a row; recall at fire-time.

---

## Current Session (2026-06-27 Sat)

**Prior (6/26 digest):** built + shipped the trigger→card toolchain (chain_fetch, grade_print+config, FIRE template + 2 trigger skeletons) + durable layer (MEMORY/CLOSEOUT). All on origin.

**Delivered 6/27:**
- **`SIGNALS.tsv`** — new trade-construction context ledger (Will option B); logged 7 WALTER INFO signals; `source` column + NEXUS regime **PIN**; `boot.py` surfaces PIN + active rows + >21d staleness flag.
- **NEXUS diagnosed 11d-dark / pre-FOMC stale** — populated PIN with the 6/16 read (stale-stamped); wrote `outbox/2026-06-27_to-NEXUS_post-fomc-reanchor-flag.md` (3 unprocessed gates: FOMC 6/17, Iran 6/19, OPEX 6/19). Will refreshing NEXUS soon.
- **`inbox/WILL/` drop zone** — Will's reserved trading-data drop; raw gitignored (local), boot-surfaced.
- **Day-trading Session 3 logged** (JOURNAL/LEDGER/PROFILE) off Will's Robinhood CSV: −$3,969 / 3 days; see day-trading Durable Finding above.

**Status:** all committed; rides the push-train. NEXUS PIN refresh + a day-trade timestamped-export are the open carries.

---

## Next Session

1. **No cards fired live yet** — fire cards staged, waiting on a real LIQUID/SENTRY trigger (HY≥280 or a Jul print).
2. **Jul print week:** MONOLINES print FIRST (~Jul 18–23: COF/SYF/ALLY — `setups/PRINT-TRIGGER_monoline-COF-SYF-ALLY.md`, earliest un-maskable tell; grade with `grade_print.py NAME --book-direction … [--nco-guide raised] [--dq-formation rising]` → **path (m)**, built 6/27), then regionals (~Jul 22–30, paths a/b/c). If transmission grades, the matching PRINT-TRIGGER skeleton is the card.
3. **HY≥280 sustained:** PRICE-TRIGGER skeleton → fill ZONE 2 → present.
4. **Refresh the NEXUS regime PIN** in `SIGNALS.tsv` once Will re-anchors NEXUS post-FOMC (currently the 6/16 pre-FOMC read, stale-stamped).
5. **Day-trading S3 carries:** request a **timestamped order export** (confirms RH auto-close + closes the churn/cancel gap); Monday-mark the open book (WAL 9/18 75P = THESIS/FORGE-scope, WEN 7/2 8.50P).
6. **Carry:** resolve Will's risk-UNIT question (+ a number for the day-trade Rule 3 cap).
