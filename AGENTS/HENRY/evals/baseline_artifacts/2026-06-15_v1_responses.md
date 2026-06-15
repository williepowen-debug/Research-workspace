# HENRY EVAL — v1 BASELINE — VERBATIM RESPONSES (2026-06-15)

**Provenance:** Fresh cold HENRY sessions (boot suppressed), run by Will, scored against case RUBRICs, reviewed by ORC.
**Result:** Case 01 PASS · Case 02 PASS (both clean). Logged in `../results.tsv` (rows: case 01/02, 2026-06-15).
**Caveat (carry-forward):** Both cases are **example-overlap confounded** — their lessons were promoted to auto-memory *this same session*, so these passes function as **regression baselines, NOT generalization tests**. Case 01 also tests the *resolve*-half (handed a conflict), not the *notice*-half that actually broke on 6/15. The load-bearing fix (boot-read mechanism) must be proved by a **smoke-test**, not this eval. See `../README.md` and the run report.

These are preserved verbatim so the baseline is auditable when the deferred CLAUDE.md boot/closeout change is applied post-FOMC and these cases are re-run for no-regression.

---

## === CASE 01 — Sibling Staleness (TARGET) ===

**HENRY — VOL REGIME reconcile vs VIOLET**

Headline first: VIOLET booted. The "pending her boot" hold I've been dragging since 6/1 is dead — she's current and she delivered every read I was owed. My carried placeholders (138.99, 12.93%) are stale by 11 days. Real numbers below. No live prices needed; this is pure reconcile.

---

**1. Stale or current?**

**Current.** Her stamp: *Last Updated 2026-06-14 ~13:00 ET, data = Friday 6/12 close (weekend refresh).* Today's Mon 6/15; 6/12 is the last completed session, so she's caught up to the tape. My carried "VIOLET still stale 6/1" is obsolete. The post-NFP debt I flagged (June NFP ~6/5) is cleared — her 6/12 data is post-NFP. Dependency resolved.

---

**2. Rewritten VOL REGIME — actual values:**

The two numbers you asked for: **M1:M2 = +9.41%** (not 12.93%). **20d-SKEW avg = 141.01** (not 138.99).

```
## VOL REGIME
- SKEW spot 142.6 — 3 straight 142+ prints (6/10–12), did NOT participate in Friday's
  vol crush; the tail is the lone holdout in an otherwise complacent tape. Regime metric
  (VIOLET's 20d-SKEW avg) now PRINTED: 141.01 thru 6/12, up ~2pts from 138.99 (6/1).
  Spot sits above the 20d-avg and the avg is rising. VVIX 93.8 clears the 92+ line —
  but only by 1.8, a soft clear, low-90s, consistent with the crush. AND VIOLET flags
  the 20d-avg's R12 margin (+1.01) as "partly mechanical" (trailing-window roll-off,
  not all fresh tail demand) — so the cross is soft, not a clean breakout.
  → HOLD the line: do NOT declare a stress regime re-entered. Reason has CHANGED from
    "data pending" to "data's in and it reads complacency-with-a-tail": VIX 17.68,
    VIX9D/VIX 0.976, VIX3M/VIX 1.160 — the broad complex reset to complacency. This is
    tail-bid-into-complacency, not a regime flip.
- M1:M2 contango +9.41% (6/12 close) — COMPRESSED ~3.5pts from 12.93% (6/1 pre-NFP).
  VIOLET still tags +9.41% as COMPLACENCY_TOP_30PCT; VIX3M/VIX 1.160 confirms deep
  contango. Velocity flag: that's a real curve flattening in 11 days — front catching a
  relative bid while spot vol crushed. Watch it, don't trade it; level's still complacent.
  VX-futures settlement now current to 6/12, post-NFP.
- ENTRY GATE: still BLOCKED. Bin-B credit governs — CCC 9.56 on the FRED 6/11 print,
  missed the 9.55 block-lift line by a single bp. SKEW/VVIX firming does NOT open entry
  while the credit gate is shut. 9.55 is the line to watch.
```

---

**3. Rewritten VIOLET cross-agent dependency row:**

```
| VIOLET | VVIX 93.8 (>92 ✓, soft); 20d-SKEW avg 141.01 (6/12), +1.01 R12 margin partly
mechanical; M1:M2 +9.41%; SKEW spot 142.6 | CURRENT to 6/12 close (stamped 6/14). Debt
cleared — delivered M1:M2 + 20d-SKEW post-NFP. Tape crushed to complacency, SKEW tail the
lone holdout. Entry still gated by Bin-B credit (CCC 9.56 vs 9.55, 1bp short). |
```

---

**4. Process note for next HENRY:**

A "pending her boot" dependency is a **standing re-check, not a fact to carry forward.** I sat on placeholder values (138.99, 12.93%, "stale 6/1") for 11 days while VIOLET had already refreshed. First move on any vol read: check VIOLET's *Last Updated* stamp against your carried date **before** writing the regime call. If her timestamp has moved past yours, her reads supersede your placeholders — pull them first.

Second: don't conflate "regime metric printed" with "entry open." The 20d-SKEW cross firmed and VVIX cleared 92, but (a) the cross is partly mechanical per VIOLET's own +1.01 flag, and (b) entry is independently locked by Bin-B credit, still shut by 1bp. Credit gate is the governing lock — SKEW/VVIX firming is necessary, not sufficient. Watch CCC 9.55.

---

## === CASE 02 — Catalyst vs Pricing (GUARDRAIL) ===

**HENRY — rates velocity. Re: the dot-plot reaction prediction.**

## 1. Sign off as written? No.

The draft makes the rookie error: it conflates the **outcome** with the **surprise**. "0 cuts = hawkish" is only true relative to the *prior dot* (1 cut). It is not true relative to *what's priced*. Futures are at ~78% for zero, economists ~70%, prediction markets 57–70%. The market has already repriced to that outcome. You don't get paid on the consensus base case printing — you get paid on realized-minus-expected, and here expected ≈ realized.

Predicting **+12bps on the modal outcome** is predicting a violent repricing *toward* something already in the price. That's backwards. Two more problems: it pins a specific magnitude with no invalidation level, and it ignores that the 10Y just rallied 9bps on a soft core print — the tape is leaning *dovish*, so the bar for a hawkish pop is higher, not lower. Reject.

## 2. If zero cuts actually prints — my call on the 10Y.

**Muted-to-lower, not +12.** Base case ±5bps with a lean to **fade — yields down.** Mechanics:
- Hawkish outcome is 78% in the price → classic sell-the-news / buy-the-fact.
- The *worse-than-zero* tail (2026 dots pulled up, long-run dot up, hike optionality) gets **removed** once the modal prints — that's a relief, and relief in a short-duration market is lower yields.
- Positioning is short duration *into* the print; confirmation triggers short-covering.

Clean zero-cut print with no second hawkish tell: **10Y unchanged to −8bps over 2 sessions.** The +12 only exists if a second hawkish leg shows up.

## 3. Re-anchored prediction — falsifiable and tradeable.

Tie the trigger to the **surprise component**, not the headline. Trackable block:

> **HENRY-RATES-[meeting] — dot-plot reaction**
> Pre-meeting 10Y: 4.45%. Zero-cut dot ~78% priced (futures) / 57–70% (pred mkts) / ~70% economists → **modal, not a catalyst.**
>
> - **BASE (modal):** 0 cuts, 2026 path & long-run dot unchanged, neutral presser → **−8 to +3bps / 2 sessions** (point: −3, fade). *Invalidated if 10Y closes >+8bps absent a second hawkish signal.*
> - **HAWKISH leg:** 0 cuts **PLUS ≥1 of** {2026 dots revised up, long-run dot up, presser flags hike optionality / upside inflation risk} → **+10 to +18bps / 2 sessions.** This is the *only* path to the junior's +12.
> - **DOVISH surprise:** dots retain ≥1 cut (or presser frames zero as a close call / downside-weighted) → **−10 to −18bps / 2 sessions**, front-end leads, bull steepener.

That's falsifiable (bp bands, 2-session window, explicit invalidation at +8) and tradeable (it tells you the zero-cut headline is a fade and exactly where to flip the book).

## 4. The dovish surprise — and what it does to yields.

The dovish surprise is the dots **holding at 1 cut** (or going to 2) — i.e., *not* dropping to zero — against a 78%-priced zero. The market is positioned for the hawkish move; the **absence** of it is the shock. Yields fall hard: front-end/belly leads, **10Y −10 to −18bps over a couple sessions, bull steepener** as cuts get pulled forward. Lands on receptive positioning after the 9bp core-print rally, so it can extend.

Softer secondary version: dots *do* print zero but the Chair frames it as a close call / stresses two-sided risks — that caps the yield rise and can flip it negative even on the "hawkish" headline.

---

**Read for Prome:** Don't let this go out as a hawkish call. The zero-cut dot is the base case, ~78% priced — confirming it is a small move, likely a fade. The **convexity is asymmetric to the downside in yields**: a confirmed zero barely moves the tape, an *unwound* zero (dovish surprise) is the violent one. If we're sizing a directional rates bet into this print, the better risk/reward is the dovish tail, not chasing +12 on the consensus. Hawkish only pays if there's a **second** signal beyond the headline — flag the 2026 dots, the long-run dot, and the presser tone as the things actually worth watching.
