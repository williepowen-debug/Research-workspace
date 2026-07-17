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
- **VRP is regime-bounded AND instrument-split — don't price a long-premium tail flat (7/17).** The "buying options is negative-EV" doctrine described a window ~1987-2010 that CLOSED for SPX post-2012 (Dew-Becker/Giglio: alpha≈0 = fairly priced, NOT profitable). But the collapse is index-specific: **TLT/rates tails still pay the full vol tax** (VRP persisted; institution-dominated market), **single-names are ~fairly priced** (premium lives at the index level as a correlation premium) **except into earnings**, and the **deep-OTM strike (8-13%) is where any residual premium concentrates** (untested post-2012; price-insensitive hedging + pure-jump strikes). ⇒ the **crash-ladder pays a DOUBLE tax** (rates + deep skew), justified only by convexity (TT-02: the short-strangle's terminal-window CVaR explosion IS the long tail's payoff window). Full: `options/RESEARCH.md`; auto-memory `finding_vrp_split_rates_vs_singlename`. **Prices the tax, never vetoes — edge still must come entirely from the thesis.**
- **No closed Terry-reviewed thesis trades yet** — POSTMORTEMS.md now has ONE *process* entry (TRY-FIRE-005: correct DENY, 7d logging lag; no trade/P&L). Still no closed thesis trade.
- **`SIGNALS.tsv` = the trade-construction context ledger** (Will 6/27, "store in lasting memory, don't put everything of value in STATUS" → option B). Durable home for anything that shapes timing/sizing/structure but isn't the thesis. `source` column spans WALTER (routed INFO), TERRY-chart (my own levels/IV/expected-move), and thesis-owner timing notes (REGINALD/CARL/LIQUID/… scaffolding, NOT their thesis truth). NEXUS regime = one **PIN** row (denominator), refreshed not streamed. Decay-tracked (as_of/decay/conf/status); `boot.py` surfaces PIN + active rows, flags >21d for re-verify/retire. OUT of scope: thesis truth + raw catalyst calendar. STATUS keeps only a one-line read + pointer. New context → add a row; recall at fire-time.
- **Position truth BEFORE structure on a marginal add (7/16, load-bearing).** A clean *flat-book* structure rec can be exactly wrong against the real book. My 81/76 grind-spread was the best flat-book expression — but Will already owned the grind 3 ways (TBT linear + ITM 85P + 82P ≈$1,150, ~186 sh short-delta), so the spread ≈DOUBLED his short-delta redundantly. The "his puts are decaying stubs" escape hatch failed on a delta check (the dominant leg was an ITM 85P at −14%, not a stub). Rule #4 isn't just "don't cite stale marks" — for any marginal add, **pull the book and rank the marginal exposure, not the standalone trade.** Also: watch **shared falsifiers across the WHOLE book** — Hormuz de-escalation would hit his rates-short (via the oil-driven term premium) AND his oil-longs at once; a card that looks defined-risk in isolation can concentrate a portfolio-level bet.
- **Sparse-index intraday endpoints can be date-shifted (7/16).** yfinance `^MOVE` 1h-bars returned degenerate single points labeled **one day late** (carried 7/10's 69.55 onto 7/13), which led me to a wrong F3→F1 gate-attribution correction I had to RETRACT. The posted **daily** (investing.com, arithmetic-self-consistent + tied to the yf 7/10 anchor) showed the real spike was 7/13 (77.77 +11.82%). **Before canonizing any date-dependent claim off a sparse index, verify against a posted daily source** — don't trust the intraday/1h endpoint's date labels. (VIOLET's ±1-day ^MOVE caveat, confirmed the hard way.)

---

## Current Session (2026-07-17 Fri — cleanup + options research; no trade, no capital moved)

**7/16 digest (teams w/ PROME):** TRY-FIRE-004 reached ARM (arm-#2 10Y 5-close, FRED-verified) → **Will NO-ADD** (owns the grind 3 ways ≈$1,150; 81/76 spread redundant), $500 banked, crash-ladder = approved fallback. VIO-116 folds into 004; USO 120C salvage; HBAN stub built; arm-#3 handed to PROME. All on origin.

**Delivered 7/17:**
- **4 carried loops CLOSED.** (1) **TRY-FIRE-005 (FXY) SHELVED** — its 7/10 COT gate resolved DENY that day; TERRY never logged it, 3 surfaces read ARMED-PENDING for 7d. No entry, $0 at risk → first `POSTMORTEMS.md` entry (process, not P&L). (2) **arm-#3 FIRED WEAK** (PROME-graded) → deepen-only on 004, NO-ADD stands. (3) **HBAN rationale STATED** ("stress lottery ticket") → stub resolved. (4) **DAEDALUS firming APPLIED** (CONTRACT + BOTTOM LINE + PAT-031 + 3 drift fixes; write-back sent).
- **2 tooling gaps fixed:** `boot.py` terminal-set missing SHELVED/DEAD (a killed card reported open forever); **TRY-FIRE-004 was absent from SETUPS.tsv** while ARMED (boot read "0 open" with a card armed). Both fixed, selftest PASS.
- **NEXUS regime PIN refreshed** (31d→1d, off NEXUS's 7/16 anchor): Break 22/Grind 37/Unres 41; **HY OAS 272 is 8bp under TRY-FIRE-001's 280 trigger** (moved toward it) → 001 = closest-to-live after 004.
- **`options/` research lane opened** (2 tastytrade + 1 retail transcript → `options/RESEARCH.md`, graded pipeline). Confronted the long-premium doctrine per Will → see new Durable Finding. Verified PDT elimination (real, 6/4/26, Robinhood day-1).

**Status:** all committed + **pushed** (TERRY self-sweep). Repo clean, synced. **No position or thesis changed all session.**

---

## Next Session

1. **TRY-FIRE-004 re-fire** — the only live trade thread. $500 banked, card ARMED/HOT. Fire on: red-day/vol-cooldown TLT entry OR fresh discriminator (arm-#3 is spent). **Crash-ladder 77/76/75 = approved shape** (do NOT re-add 81/76 — redundant w/ Will's book). Rule #6: TLT at range lows → green-day/scaled fill.
2. **Un-owned-gate check before every closeout** (from the 005 postmortem, now standing): any resolver landing after session end gets a named grader or an explicit STATUS pickup line. 005 drifted 7d because nobody owned its gate.
3. **HBAN 7/23 BMO print** — position rides through on its own (lottery ticket, resolved); no action owed unless Will re-engages.
4. **OZK 7/21 print** — mild headwind flagged (div-hike + $200M buyback 7/1); tell = criticized/SM build not NCO (WALTER SIG-006) → watch the credit supplement.
5. **WALTER signal decay** — 4 of 6 rows >21d; squeeze-risk row 63d and load-bearing for sizing any short. Reconfirm-or-retire before citing.
6. **Carries:** Will's risk-UNIT question ($/%/R); day-trade timestamped order export. **Options open items** (RESEARCH.md): deep-OTM/rates VRP gaps = acknowledged, NOT tracked (recognize-if-encountered).
