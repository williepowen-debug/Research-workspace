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
- **Position truth BEFORE structure on a marginal add (7/16, load-bearing).** A clean *flat-book* structure rec can be exactly wrong against the real book. My 81/76 grind-spread was the best flat-book expression — but Will already owned the grind 3 ways (TBT linear + ITM 85P + 82P ≈$1,150, ~186 sh short-delta), so the spread ≈DOUBLED his short-delta redundantly. The "his puts are decaying stubs" escape hatch failed on a delta check (the dominant leg was an ITM 85P at −14%, not a stub). Rule #4 isn't just "don't cite stale marks" — for any marginal add, **pull the book and rank the marginal exposure, not the standalone trade.** Also: watch **shared falsifiers across the WHOLE book** — Hormuz de-escalation would hit his rates-short (via the oil-driven term premium) AND his oil-longs at once; a card that looks defined-risk in isolation can concentrate a portfolio-level bet.
- **Sparse-index intraday endpoints can be date-shifted (7/16).** yfinance `^MOVE` 1h-bars returned degenerate single points labeled **one day late** (carried 7/10's 69.55 onto 7/13), which led me to a wrong F3→F1 gate-attribution correction I had to RETRACT. The posted **daily** (investing.com, arithmetic-self-consistent + tied to the yf 7/10 anchor) showed the real spike was 7/13 (77.77 +11.82%). **Before canonizing any date-dependent claim off a sparse index, verify against a posted daily source** — don't trust the intraday/1h endpoint's date labels. (VIOLET's ±1-day ^MOVE caveat, confirmed the hard way.)

---

## Current Session (2026-07-16 Thu — teams w/ PROME)

**Prior (6/27 digest):** built SIGNALS.tsv context ledger + NEXUS PIN; logged day-trade S3 (−$3,969); built monoline TRY-FIRE-003 + path-(m) grader. All on origin.

**Delivered 7/16 (first live card ARM):**
- **TRY-FIRE-004 ARMED** — arm-#2 (VX-BND-05 10Y 5-close ≥4.50) FIRED 5-of-5 Mon 7/13, independently FRED-verified (matched PROME + BOND co-grade, no restatement). First card ever to reach ARM.
- **Live-marked arm packet** on Will's broker chain (FORGE tool couldn't serve TLT option NBBO — 3 pulls all 0.00; documented as a feed limitation). Built ladder-at-asks + 3 grind-spread variants; flat-book rec was 81/76 spread.
- **Position truth REVERSED the rec → Will NO-ADD.** Will owns duration-short 3 ways (TBT + ITM 85P + 82P ≈$1,150); the spread ≈doubles his short-delta redundantly. Flagged the shared **Hormuz-de-escalation falsifier across his rates-short AND oil-long books**. $500 banked; crash-ladder = approved fallback.
- **VIO-116 rates-vol shape memo** — no stand-alone shape (folds into 004). Interim F3→F1 attribution correction **RETRACTED** after web-verifying the MOVE spike was 7/13 (my yf 1h-bar was date-shifted); F3 fired cleanly, PROME's GATES attribution correct.
- **USO 7/17 calls triage** — salvage the 120C (don't feed extrinsic to theta into a 2-way 1DTE catalyst @ OVX 61); 127C dust; keep shares. Will acts directly.
- **HBAN** — built governance stub + two-branch decision memo (one-print vehicle: Oct-16 < Q3; $20 dust; real decision is re-entry). Q2 = 7/23 BMO (IR-verified), DOCKET registered by PROME.
- **Light card-relevant sweep** — rates premises intact/reinforcing; Muscat inconclusive; OZK div-hike+$200M buyback = mild headwind for OZK puts.

**Status:** all committed, NOT pushed (PROME runs the push-train). arm-#3 grade handed to PROME (4pm). Deferred: DAEDALUS firming apply.

---

## Next Session

1. **arm-#3 (May TIC) result** — PROME grades at 4pm 7/16; if FIRED, consume/log on TRY-FIRE-004 (deepen-confirm only, no new trade); UNDETERMINED/dead = just log. Pre-reg expectation = no-fire/UNDETERMINED.
2. **TRY-FIRE-004 re-fire conditions** ($500 banked, card ARMED/HOT): red-day/vol-cooldown TLT entry, OR arm-#3 fire, OR fresh discriminator → crash-ladder 77/76/75 = approved fallback shape. (Do NOT re-add the 81/76 spread — redundant w/ Will's book.)
3. **HBAN branch outcome** — Will's thesis-or-exit call pre-7/23; consume onto stub/two-branch memo; if re-entry, proper structure (Q3-spanning tenor + strike matched to a −13%+ stress move, not dust).
4. **DAEDALUS firming apply** (deferred `inbox/2026-07-03_…`): CONTRACT block + BOTTOM LINE + PAT-031 cwd-proof + 3 drift fixes; DAEDALUS write-back on completion (PAT-032).
5. **OZK puts** — mild headwind flagged (div-hike + $200M buyback 7/1); the tell is criticized/SM build not NCO (WALTER SIG-006) → watch the 7/21 print's credit supplement.
6. **Carries:** NEXUS PIN refresh (still 6/16 pre-FOMC stale); Will's risk-UNIT question; day-trade timestamped order export.
