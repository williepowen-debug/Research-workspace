# WIRE CHECK — ZeroHedge, "Terrible 20Y Auction Prices With Huge Tail, Lowest Foreign Demand On Record"

**Author:** Tyler Durden · **Published:** 2026-09-15 13:30 ET (≈30 min after the print)
**Checked by:** BOND, 2026-09-17 ~10:1x ET, against the **TreasuryDirect primary** (`TA_WS/securities/search`, type=Bond, `originalSecurityTerm`=20-Year, `floatingRate`≠Yes, cache-busted at check time). **n=78 auctions, span 2020-05-20 → 2026-09-15.**
**Subject auction:** 9/15 20Y-R `912810UX4` — the print that fired this desk's **first-ever `I'`**.

> **VERDICT IN ONE LINE: every LEVEL in the article reproduces at the primary to 2dp; three of its SUPERLATIVES do not, and the one that is flatly false is the one that would have flipped our verdict.**

---

## 1 · Claim-by-claim against the primary

| # | Article claim | Primary | Verdict |
|---|---|---|---|
| 1 | High yield **5.420%**, "highest on record since the 20Y was introduced in May of 2020" | 5.42; next-highest 5.245 [2023-10-18], then 5.204 [2026-08-19] | ✅ **TRUE** |
| 2 | Tailed the WI 5.400 by **2.0bp**, "biggest since 2024" | **TreasuryDirect publishes no when-issued** | ⚠️ **UNVERIFIABLE AT PRIMARY — `[med-conf]`** (see §3) |
| 3 | BTC **2.57**, above last month's 2.53, "below the recent average of 2.65" | 2.57 ✅ · Aug 2.53 ✅ · trailing-12 mean **2.64** | ✅ **TRUE** (their 2.65 vs our 2.64 = rounding) |
| 4 | Indirects "plunged from **62.9%** to just **52.5%**" | 62.93 → **52.47** | ✅ **TRUE** |
| 5 | "far below the recent average of **68.0%**" | trailing-12 **mean 65.05 / median 65.19** | ❌ **WRONG by ~3pp** — undisclosed window and/or denominator (ours is % of *competitive accepted*) |
| 6 | Indirect **"the lowest on record"** | 52.47 is **2nd-lowest of 78**. The lowest is **2021-12-02 at 0.00%** | ⚠️ **TRUE ONLY AFTER EXCLUDING A DEGENERATE PRINT, AND THEY DON'T DISCLOSE IT** (see §2) |
| 7 | Directs 24.6% → **30.7%**, "highest on record **by a wide margin**" | 24.59 → 30.68; highest of 78 ✅. Next is **29.15** [2025-11-19] | ✅ level TRUE · ❌ **"wide margin" = 1.53pp** |
| 8 | Dealers **16.9%**, "not quite the highest on record **but close**" | 16.85 ✅. Series max **100.00**; real cluster **29.08 / 26.19 / 26.03 / 25.75**. Trailing-12 max **17.59** | 🔴 **FALSE — and this is the load-bearing one** |

---

## 2 · The degenerate print — a real finding for our own tooling

**2021-12-02 `912810TC2` reports indirect 0.00%, direct 0.00%, dealer 100.00%, BTC 2.92.**

A 100/0/0 split beside a 2.92 cover is not a market outcome; it is almost certainly a TreasuryDirect data-quality artifact. Consequences:

- ✅ **Our live bars are SAFE.** The `I'` bar and the OLD min/max are computed on a **trailing-12** window (2025-09-16 → 2026-08-19), which does not reach 2021.
- 🔴 **Any FULL-SERIES 20Y statistic ingests it** — and the article's "lowest on record" is exactly such a statistic. So would a series-wide base-rating of the `I'` test, which is the kind of thing this desk builds.
- **This is the 2Y-FRN contamination class in a new costume** (a pool row that is identical on every field the tool keys on, and wrong): there, 43 FRN rows set the 2Y bars; here, one degenerate row sets the series floor. **The lesson transfers: base-rate the POOL before base-rating the GATE.**

⇒ **Owed:** a raise-on-degenerate guard in `grade_auction.py` (reject any row where indirect+direct+dealer shares don't reconcile, or where any leg is exactly 0.00 with another at 100.00) **before** any full-series 20Y work. Not urgent for the 9/22–24 cluster, which is trailing-12.

---

## 3 · The tail: the article supplies what our primary cannot — and it still can't fire anything

The article gives **WI 5.400%, tail 2.0bp**. Our canon retired the tail on 2026-07-28 because **a tail needs the when-issued yield at the bid deadline and TreasuryDirect does not publish it** — unscoreable *by construction*.

**This article does not change that, and it is worth being precise about why.** The retirement was never a claim that tails are uninteresting; it was a claim about **scoreability from our primary**. A wire tail remains `[med-conf]`, is recordable in notes, and **may never fire a gate, a kill, a re-arm or a prediction**. Nothing here reopens it.

What it *does* do: corroborate, from an independent direction, that the 9/15 print was priced poorly — consistent with our own "expensive, not broken" read.

---

## 4 · 🔴 The claim that would have flipped our verdict, and it is false

Our 9/15 grade reads: **`I'` fired (indirect −9.25pp below the P15 bar) but the MECHANISM HELD, because the bid SUBSTITUTED rather than vanished — direct 30.68 (series high), BTC 2.57, and dealers at 16.85, BELOW their trailing-12 max of 17.59.**

The demand-hole test this desk has run since inception is **foreign stepping away WHILE DEALERS WAREHOUSE**. Dealer take is the warehousing leg.

**The article asserts dealers were "not quite the highest on record but close."** Had that been true, the 9/15 print would have shown foreign away *and* dealers stuffed — **the paired signature, i.e. a demand hole, i.e. our thesis kill.**

It is not true. **16.85% is below the trailing-12 max (17.59) and nowhere near the series cluster of 25.75–29.08.** Dealers took a *below-recent-maximum* share. The mechanism held.

⚠️ **Note the direction of the error and what it means for how we read this source: the article's one false superlative points toward OUR OWN thesis.** A desk that took the wire at face value would have upgraded its bear case on a fabricated adjective — and would have felt confirmed while doing it. This is the precise reason wire-sourced composition data is `[med-conf]` and gates read the primary.

---

## 5 · The one genuinely original idea in the article — tested, and it does not hold at the 20Y

**The concession hypothesis:** last week's 10Y and 30Y were "stellar … only because they took place on days when yields soared earlier in the day, giving buyers solid concessions," while "there was no such concession today."

This is a real, testable mechanism, and it bears directly on our grading method — **our composition bars do not condition on concession at all.** It is also the same idea as the Will-via-PROME 5/21 rule already in `MEMORY.md` ("grade auctions against the sentiment backdrop"), which we apply to *interpretation* but have never applied to the *bars*.

**Test (20Y only, n=78):** proxy concession by the auction-day `DGS20` change vs the prior session close; split auctions into concession (yield up) and no-concession (flat/down).

| Group | n | mean indirect | median indirect |
|---|---:|---:|---:|
| **Concession** (yield UP) | 31 | **63.01** | 64.83 |
| **No concession** (flat/down) | 47 | **67.17** | 67.44 |

**Difference −4.16pp; correlation(auction-day yield change, indirect share) = −0.270.**

⇒ **The sign is OPPOSITE to the article's mechanism.** At the 20Y, concession sessions have historically drawn *weaker* indirect participation, not stronger.

**And 9/15 was itself a concession day on this proxy: `DGS20` rose +3.0bp.** So the article's own premise — "there was no such concession today" — is not supported at the daily frequency either.

**THREE LIMITS, STATED NOT BURIED:**
1. **The proxy is daily close-to-close; the argument is intraday (the move before the 1:00 PM bid deadline).** A session can close higher while the pre-deadline move was lower. This test *weakens* the hypothesis at the 20Y; it does not refute the intraday version, which our data cannot reach.
2. **A confound running the article's way:** concession days are days when yields are rising, which are disproportionately supply-stress/risk-off days — so the negative correlation may be "bad days are bad days" rather than a refutation of concession *per se*. Disentangling needs intraday.
3. **Cross-tenor untested.** The article's comparison is 10Y/30Y vs 20Y; this test is 20Y-only. No significance test run; n=31 vs 47.

---

## 6 · What IS new and worth keeping

1. 🟠 **Bessent's congressional testimony (9/15): the Treasury Secretary publicly attributed the yield spike to OIL, and cited the prior week's 10Y and 30Y as "stellar."** A policy-reaction-function datum this desk did not have. `[med-conf]` — wire report of testimony, **not independently verified; verify before any load-bearing use.** Relevant to the sovereign-credibility lane and to C-36: it is an official attribution that competes with our own real-rate/term-premium reading.
2. ✅ **Independent corroboration of our levels.** Indirect 52.5 / direct 30.7 / dealer 16.9 / BTC 2.57 all reproduce. Our grade was right and is now externally checked. *(Caveat, per this desk's own FAN-OUT rule: the article and we may both be reading TreasuryDirect, in which case this validates the FETCH, not the VALUE.)*
3. 🔴 **The degenerate 2021-12-02 row** (§2) — a pool defect we would otherwise have met inside a future base-rating.
4. ⚪ **The YCC / "buyback bluff has failed" framing is editorial and is the claim this desk already examined at the primary on 2026-08-19 and REJECTED on the letter** (`VX-BND-16`): capped size, dated window, no yield target, no unlimited commitment. YCC's defining feature is an elastic quantity pledged at a price. Nothing in this article is new evidence on that; it is assertion.

## 7 · Net answer

**Nothing here changes a score, a gate, a prediction or the position.** The article is accurate on levels and unreliable on adjectives — **the same failure class this desk has logged against itself six times** (`MEMORY.md`: *"an adjective or aggregation attached to a computed number is itself an uncomputed claim"*). Its most consequential line (dealers "close to the highest on record") is false and points at our own thesis.

**Useful output of the check:** one new policy datum (Bessent, `[med-conf]`), one genuine tooling defect found (§2), and one testable hypothesis measured rather than absorbed (§5).
