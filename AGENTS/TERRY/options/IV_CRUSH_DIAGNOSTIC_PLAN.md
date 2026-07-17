# EARNINGS IV-CRUSH DIAGNOSTIC — research plan
**Created:** 2026-07-17 · **Owner:** TERRY · **Status:** Part A run 2026-07-17; Parts B/C pending
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

### Part C — Data wall (blocked)
Historical IV surface required. Flagged, not attempted.

## Deliverable
One-page finding: (1) per-name verdict on the current book before 7/21–7/23; (2) proxy read on chronic buy-into-crush pattern; (3) one construction-rule candidate: enter post-crush / put spreads / avoid print-spanning expiries / size for crush.

## Results log
- **Part A — 2026-07-17:** see `IV_CRUSH_PARTA_2026-07-17.md` (appended this session).
- Part B: pending.
