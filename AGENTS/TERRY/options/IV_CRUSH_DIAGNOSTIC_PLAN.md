# EARNINGS IV-CRUSH DIAGNOSTIC — research plan
**Created:** 2026-07-17 · **Owner:** TERRY · **Status:** ✅ **PLAN COMPLETE 2026-08-13 — Part A run 7/17 · Part B run 8/13 (`IV_CRUSH_PARTB_2026-08-13.md`) · Part C KILLED 8/4 (Will).** No live parts remain.
**Scope class:** SIDE construction study, subordinate to the thesis system. Informs *how to express* a thesis, not whether it's right. Does NOT arm anything.

## Question
Are we systematically buying single-name put IV *into* earnings and eating the post-print crush — losing on volatility even when direction is right? Isolate the **crush** contribution to the basket bleed from the confounds (theta = thesis too slow; direction = banks haven't cracked).

## Why it matters
The regional-bank put basket is down −70% to −99%. Cause is confounded. IV crush is the one contributor that is **structurally fixable at construction time** (enter post-crush, spread out the event premium, avoid print-spanning expiries, or size for it).

## The data wall (named, not faked)
True crush measurement = IV_before vs IV_after each historical print → needs a **historical IV surface (ORATS / IVolatility / LiveVol — paid/gated).** Not available. Part B is the free proxy.

## Method — three tiers

### Part A — Forward check on the current book (FREE, doable now)
- Live IV per strike via `chain_fetch.py` on **WAL / OZK / HBAN** (+ ZION if held longer-dated).
- Implied expected move from the ATM straddle → size of move priced through the print.
- Estimated post-crush mark: what the puts are worth the morning after, expected-move vs big-move.
- **Output:** per-position verdict — hold / trim pre-print / convert to spread.
- **Live targets (span the prints; Jul-17 puts on these names die pre-print, excluded):**
  WAL 70P/67.5P Sep-18 · OZK 45P/42.5P Aug-21 · HBAN 16P Oct-16. Prints: WAL/OZK/ZION **7/21**, HBAN **7/23**.

### Part B — Historical pattern (PROXY, free-ish; pending)
- Last 6–8 earnings dates per name; realized 1-day post-earnings move from price history.
- Realized move vs. move the puts *needed* to pay. Consistently smaller ⇒ structurally buying overpriced event vol ⇒ crush confirmed indirectly.
- **Limit:** proxies crush via realized-vs-implied move, not direct IV. Defensible, not exact.

### Part C — Data wall — 🪦 **KILLED 2026-08-04 (Will-decided). DO NOT REVIVE without a funding decision.**
Historical IV surface required; **paid data.** Will 2026-08-04: *"I don't think I want to buy data unless cheap + worth it."*

**Verdict: not worth it, and the reason is that it is largely redundant before it is expensive.**
- **Part B answers substantially the same question for free** — realized-vs-implied move is an indirect but defensible read on chronic crush.
- The **live** IV need is already covered by `scripts/chain_fetch.py` (bid/ask/IV/OI on demand at fire time). Part C buys *history*, and history is what Part B proxies.
- The one durable finding this lane has produced is already promoted and in use: **`RISK_RULES.md` durable finding #8 — the VRP collapse is NOT uniform; rates (TLT) pay the full vol tax, single names are structurally cheap except into earnings.** That is the actionable half, and it did not require a paid surface.

⇒ **Killed, not parked.** Revive only if a historical IV surface arrives cheap or bundled — and then only with a stated question it would answer that Part B could not.

### ⚠️ Part B — THE FREE ONE, AND IT WAS NEVER RUN. Found by the 2026-08-04 audit sweep.
**This is the real finding of the audit on this lane.** For weeks the tracked open item was *"Part C is BLOCKED on paid data"* — while **Part B, which is free and answers substantially the same question, sat marked "pending" and was never picked up.** The lane looked blocked-by-money when it was actually blocked-by-nobody-starting-it.
*(Cf. `finding_audit_resolution_path_before_reattempt` — a long-open question is usually blocked by the PATH, not by missing data.)*

**Status: QUEUED, and it is now the only live piece of this plan.** Needs only free price history (yfinance): last 6–8 earnings dates per name, realized 1-day post-print move vs the move the puts needed to pay.
**Relevance is current, not historical:** `TRY-FIRE-002` and `TRY-FIRE-003` are both PRINT-class cards that will face this exact question again, and the **bank-put reshape** turns on what to reshape *into*.
⚠️ **Part A's targets are SPENT** — WAL/OZK 7/21 and HBAN 7/23 have printed. Part B's output is the generalizable half: a construction rule (enter post-crush / put spreads / avoid print-spanning expiries / size for crush).

## Deliverable
One-page finding: (1) per-name verdict on the current book before 7/21–7/23; (2) proxy read on chronic buy-into-crush pattern; (3) one construction-rule candidate: enter post-crush / put spreads / avoid print-spanning expiries / size for crush.

## Results log
- **Part A — 2026-07-17:** see `IV_CRUSH_PARTA_2026-07-17.md` (appended this session).
- **Part B — ✅ RUN 2026-08-13 (Will-directed):** see `IV_CRUSH_PARTB_2026-08-13.md` + re-runnable `partb_realized_moves.py`. **Headline: 0 of 32 prints (4 names × 8 quarters, Oct-24→Jul-26) reached even 10%, vs held strikes needing 12.7–15.5% — the needed move is outside the entire realized envelope, not just "consistently smaller." Confirmed, with a regime-conditional caveat (no crisis print in sample).** Construction-rule CANDIDATE recorded there; not yet promoted. *(Was "pending" 7/17→8/4 and QUEUED 8/4→8/13 — the audit's blocked-by-nobody-starting-it diagnosis was correct; the run took under an hour.)*
- **Part C: 🪦 KILLED 2026-08-04, Will-decided.**
