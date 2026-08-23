# OZK — Scenario Analysis & Target Prices
**Created:** 2026-03-23 | **Last Updated:** 2026-07-06 (figure re-base to Call Report primary; **weights unchanged since 4/23 reweight**)
**Price:** live → `STATUS.md` / boot.py (was $47.52 at the 4/23 reweight; $49.65 at 7/6 sweep) | **TBV:** $47.15 (Q1 26)
**Short Interest:** ~14-15% float, 12-18 days to cover (KB-OZK-160 last refresh Mar 25 — needs next FINRA pull)

> **Framing note:** Probabilities are scenario weights for position sizing. Post-Q1 reweight: migration-velocity metrics (past-due 10× in 6 months) confirmed the bear case at the leading-indicator layer, but capital buffer demonstrated through the print shrinks tail risk. Direction unchanged; weights shifted.

---

## EXPECTED VALUE SUMMARY (reweighted 2026-04-23)

| Scenario | Prob | Price Range | Midpoint | Weighted |
|----------|------|-------------|----------|----------|
| Bear | **55%** | $30-38 | $34.00 | $18.70 |
| Base | **30%** | $40-46 | $43.00 | $12.90 |
| Bull | **12%** | $52-60 | $56.00 | $6.72 |
| Tail | **3%** | $18-25 | $21.50 | $0.65 |
| **Expected Value** | | | | **$38.97** |

**At the 4/23 reweight ($47.52): ~22% above EV of $38.97. At 7/6 ($49.65): ~27% above EV.**

### Reweight rationale (Apr 23)
- **Bear +5pp (50→55):** Q1 26 past-due more than doubled ($207M → $487.5M/1.48% [Call Report; suppl. $465M — basis standardized 7/4]), classified+criticized +23% QoQ, 3 new substandard + 2 new foreclosed. Migration-velocity thesis confirmed at the leading-indicator layer.
- **Bull −3pp (15→12):** IQHQ maturity corrected Aug 2026 (not 2028) raises Wave 3 probability; Aimco $50M fraud suit chills 4th rescue round; OZK pulling BACK from Fund Finance subscriptions (Jake Munn Q1 call) removes the "regionals press into NDFI for growth" bull mechanism for OZK specifically.
- **Tail −2pp (5→3):** CET1 11.64%, $16.9B primary+secondary liquidity, buybacks at accretive prices ($45.51 avg vs $47.15 TBV), TBV +11% YoY all demonstrate the capital buffer holds through the current stress. Rating-downgrade/deposit-flight tail sequence less likely.
- **Base unchanged (30%):** slow-grind "threads the needle" remains the single most plausible single-path outcome.

Net EV: $37.45 → $38.97 (+$1.52). Implied overvaluation vs market: 24% → 22%. Thesis edge preserved but modestly compressed — this is accurate, not a problem.

---

## SCENARIO A: BEAR CASE (55%)

**Q1 26 confirmation status:** Past-due more than doubled QoQ ($207M → $487.5M, 0.64% → 1.48% [Call Report]) — LEADING INDICATOR of this scenario. 3 new substandard credits (2 Seattle U District + Boston Life Sci $169M), 2 new foreclosed (Santa Monica Office at 15% leased, Chicago Life Sci at 68% of appraisal). NCO 0.56% [Call Report] — 1bp above the ≤55bps kill line; recognition tempo not yet in Q2-Q3, as predicted. Thesis direction confirmed; timing on track.

**Thesis:** Interest reserve depletion + 2022 vintage maturity wall forces nonaccrual wave Q2-Q3 2026 (Q1 was the past-due pulse; NCO conversion follows). Charge-offs exceed provisioning. Market reprices to stressed bank multiple.

**Mechanics:**
1. Construction maturity wall hits Q1-Q3. Borrowers can't refi or stabilize. Interest reserves deplete.
2. Noncurrent rises to $600-800M by Q3 (from $341M). Plausible: $322M additions in last 6 months, wall hasn't fully arrived.
3. Charge-offs accelerate to $80-120M/quarter.
4. ACL consumed: $475.7M erodes to $300-350M.
5. EPS compresses from $6.18 to $3-4 range on provision catch-up.

**TBV Impact:**
- Cumulative excess charge-offs: $100-200M over 2-3 quarters
- TBV erosion: $46.48 → $42-43 (moderate) to $37-38 (if IQHQ partially written)
- IQHQ partial writedown ($100-150M) pushes TBV to ~$37-39

**Valuation:**
- Stressed CRE bank: 0.7-0.9x eroded TBV (~$37-43)
- **Bear target: $28-35**
- Deep bear (IQHQ + systemic): $25-28

**Why 50%:** 89.7% of construction on interest reserves is administered, not organic. Market reads "low construction noncurrent" as health — it's artifice. Q4 noncurrent spike was the leading edge. Maturity wall is mechanical, not probabilistic.

**Rate relief doesn't help much:** Stress is concentrated in office/life sci (75% of noncurrent) where the bottleneck is vacancy, not borrowing cost. Moderate rate cuts reduce bear probability by ~5% at most.

---

## SCENARIO B: BASE CASE (30%)

**Q1 26 consistency:** This scenario is where Q1 print reads most cleanly. Mgmt tone confident (*"late stages of this CRE cycle"*), NCO 0.56% [Call Report] near guide, CET1 11.64%, buybacks accretive. Threads-the-needle mechanics observable.

**Thesis:** Management provisions just enough to stabilize ACL. Charge-offs elevated but contained. IQHQ resolution via Scenario A (extend with sponsor equity) or Scenario C (takeout). Slow grind sideways-to-lower; no capital event.

**Mechanics:**
1. Q2-Q3 26 charge-offs: $60-100M/quarter. Provision matches within ±10%.
2. Past-due $487.5M Q1 26 [Call Report] partially converts to NCO but plateau-s, not doubles again.
3. EPS compresses to $4.75-5.75 (from $6.18).
4. Dividend maintained under scrutiny; may skip 2026 increase cycle.
5. IQHQ extends in Aug 2026 with $100-200M fresh sponsor equity (20% weight in full scenario tree).
6. $350M sub notes reprice Oct 1 2026 as guided; ~$12.8M/yr headwind absorbed.

**TBV Impact:** Slow erosion — TBV $47.15 drifts to $44-47 range by Q4 26.

**Valuation:**
- Uncertain CRE bank: 0.85-0.95× TBV
- **Base target: $40-46**
- Current $47.52 = top of base range. Limited upside, limited downside.

---

## SCENARIO C: BULL CASE (12%)

**Q1 26 pushback data:** NCO 0.56% [Call Report] near guide, TBV +11% YoY, buybacks at accretive prices, CET1 11.64%. Post-Q1 additions to this column: dividend hike +2.1% (7/1, 64th straight), $200M buyback authorization (6/30), Street targets low-to-mid $60s on RESG-runoff de-risking (→ `WEAKNESSES.md` C7). If we're wrong, these are the tells that would have warned us.

**Thesis:** CRE stabilizes, management rebuilds ACL, IQHQ cures, short squeeze amplifies the recovery.

**Mechanics:**
1. IQHQ lands material lab tenant (>250K SF at RaDD) OR sponsor commits 4th rescue round ($200M+ fresh equity) — despite Aimco April 2026 fraud suit
2. Fed cuts aggressively (100+ bps by YE 26) — enables construction loan refis, softens maturity wall
3. Past-due reverses Q2 26 (<$400M) — migration-velocity reading was a Q1 spike, not a pipeline
4. Charge-offs normalize to $30-50M/quarter
5. EPS recovers to $5.75-6.25

**Valuation:**
- Recovering bank: 1.1-1.3× TBV (~$52-60)
- **Bull target: $52-60**
- Squeeze overshoot: $58-65 temporarily (14-15% SI, 12-18 days to cover)

**This is the loss scenario for puts.** Size to survive a squeeze to $55 without panic. Cross-ref: THESIS.md "What Would Invalidate" §3 (IQHQ cures) + §5 (Fed cuts / structural turn).

---

## SCENARIO D: TAIL — CAPITAL EVENT (3%)

**Downgraded from 5% → 3% post-Q1.** Capital buffer demonstrated: CET1 11.64%, $16.9B primary+secondary liquidity, $2.3B+ buffer above well-capitalized minimum. At current NCO run-rate capital grows, not erodes. A rating event or deposit flight sequence would require NCOs to roughly triple from current pace — low probability even in Scenario A path.


**Thesis:** Cascading losses → rating downgrade → deposit flight → forced capital raise.

**Mechanics:**
1. Multiple large loans go nonaccrual simultaneously
2. ACL breached, provision surge crushes earnings to near-zero
3. KBRA/Moody's downgrade (KBRA already Negative outlook)
4. Uninsured deposit flight: $11.9B uninsured (35.8%), 2.2x Tier 1
5. Forced dilutive equity raise

**Valuation:**
- **Tail target: $16-24** (0.5-0.65x deeply eroded TBV)

---

## EPS SENSITIVITY — THE REAL TRADE

The thesis is earnings compression, not bank failure. Capital buffer is ~$2B+ above well-capitalized minimums.

| EPS | P/E 7x (current) | P/E 6x (stressed) | P/E 5x (crisis) |
|-----|-------------------|--------------------|--------------------|
| $6.18 | $43 | $37 | $31 |
| $5.00 | $35 (-22%) | **$30 (-33%)** | $25 (-44%) |
| $4.00 | $28 (-37%) | **$24 (-46%)** | $20 (-55%) |
| $3.00 | $21 (-53%) | $18 (-60%) | $15 (-66%) |

Bear case needs EPS ~$5.00 at 6x → **$30** (-33% from $44.70).

---

## PUT EXPECTED VALUE (pre-Q1 premium basis — ⚠️ POSITION STATE STALE)

⏹️ **DEAD SURFACE — the per-position EV tables below price legs that NO LONGER EXIST (dated-tag 2026-08-23).** The May-15 lines expired 2026-05-15; the **Aug-21 lines expired WORTHLESS at the 2026-08-21 OPEX** (Will's 8/4 RIDE ruling; realized −$1,686.37 / −100%). **The book is empty — there is nothing here to act on, at any price.** ⚠️ **The scenario logic is NOT dead and is NOT retired by this tag:** Bear 55% / Base 30% / Bull 12% / Tail 3% remain current, and the underlying price/severity branches are still the desk's live framework. What is dead is the option-payoff layer bolted onto them. Any future OZK expression is a **new** trade — TERRY-built, Will-gated — never a revival of the tables below. *(Superseded: the prior banner's "STALE / NOT MANAGED … Aug 21 lines are unverified against broker" — they are no longer unverified, they are gone. Intrinsic-value math still uses Mar-24 anchors: $44.70 baseline, $4.05 entry.)*

---

## PUT EXPECTED VALUE (Mar 24 ANCHOR — KEPT FOR FRAMEWORK REFERENCE)

**Intrinsic values at $44.70, cost basis ~$4.05 (last add Mar 24).**

### Aug $45 Put (4 contracts) — Core Position
| Scenario | Prob | Stock | Intrinsic | Weighted |
|----------|------|-------|-----------|----------|
| Bear ($31.50) | 50% | $31.50 | $13.50 | $6.75 |
| Base ($40.50) | 30% | $40.50 | $4.50 | $1.35 |
| Bull ($57.00) | 15% | $57.00 | $0.00 | $0.00 |
| Tail ($20.00) | 5% | $20.00 | $25.00 | $1.25 |
| **EV** | | | | **$9.35** |

At ~$4.05 cost basis (last add), **EV = 2.3x risk.** Positive EV with defined max loss.

### May $42.5 Put (2 contracts) — Catalyst Bet
| Scenario | Prob | Stock at Exp | Intrinsic | Weighted |
|----------|------|-------------|-----------|----------|
| Bear (partial by May) | 35% | $36 | $6.50 | $2.28 |
| Base | 35% | $42 | $0.50 | $0.18 |
| Bull | 20% | $50 | $0.00 | $0.00 |
| Tail | 10% | $30 | $12.50 | $1.25 |
| **EV** | | | | **$3.70** |

Tight timeline — needs Apr 16 earnings to catalyze. Positive EV but narrower margin.

### Aug $42.5 Put (1 contract) — Deep Bear
EV similar to Aug $45 but lower delta. Profits only in bear/tail. Pure downside bet.

---

## SQUEEZE RISK

- **13.81% short float, 11.20 days to cover** — heavily crowded
- Any positive catalyst (earnings beat, IQHQ tenant, rate cut signal) could trigger 10-15% squeeze
- Size positions to survive $50-55 without forced exit
- Aug expiry provides runway to survive squeeze and still catch maturity wall
- **Rule: don't add on green days.** Squeeze risk is highest when stock is already moving up.

---

## WHY MARKET IS MISPRICING

1. **Interest reserve artificiality invisible** — 89.7% administered, deep in Call Report, no analyst covers it
2. **Noncurrent spike read as one-off** — market doesn't see maturity wall pipeline behind it
3. **C&I reclassification flatters CRE ratios** — 37.6% MI3 not discussed by sellside
4. **Record EPS $6.18 anchors narrative** — earnings lag credit reality by 2-3 quarters
5. **"CIB diversification" narrative** — NDFI counterparties are overwhelmingly CRE debt funds
6. **Exit counterparty risk invisible** — Blue Owl gated, Affinius is private/opaque (no public bonds — "81¢" ref was WRONG per Prompt #9 research; likely conflation with USAA Cap Corp or securitization vehicle). Columbus Center $69M foreclosure = isolated office walk-away.

---

## ~~APRIL 16 DECISION FRAMEWORK~~ — RETRACTED 2026-04-23

Q1 earnings resolved Apr 21 (not Apr 16). Framework superseded by post-Q1 resolution data. Kept here in the CHANGELOG-equivalent style for audit trail — DO NOT use.

---

## POST-Q1 DECISION GATES

| Gate | Trigger | Action |
|------|---------|--------|
| **Q2 26 print (~late July)** | Past-due <$400M OR NCO <0.55% annualized | Thesis kill criterion #1 firing — evaluate unwind. See THESIS "What Would Invalidate" §1-2. |
| **Q2 26 print** | Past-due >$500M + NCO >0.80% | Migration→recognition pipeline converting as predicted — hold. |
| **IQHQ catalyst (any time through Aug 2026)** | Tenant lease >250K SF announced OR sponsor 4th rescue equity | Wave 3 cure — evaluate unwind. Cross-ref THESIS §3. |
| **IQHQ catalyst** | Substandard migration / specific reserve >$140M | Wave 3 firing at expected severity — hold / consider adding. |
| **Aug 15 2026 RaDD maturity** | Default / deed-in-lieu | Scenario D tail firing. |
| **Oct 1 2026 sub notes** | OZK redeems $350M rather than reprice | Directional bull signal (THESIS §4). |
| **Ongoing** | Squeeze to $52+ with no fundamental catalyst | Accept — Aug duration designed for this. (May-position roll language OBSOLETE — May lines expired unlogged; book stale/not-managed per 7/4.) |

---

## Currency note

| Field | Live source |
|---|---|
| Scenario weights / EV | THIS FILE (reweighted 2026-04-23) |
| Thesis pillars + invalidation | `THESIS.md` v1.4 |
| Bull-case rebuttals | `WEAKNESSES.md` (C7 RESG-runoff steelman added 2026-07-04) |
| IQHQ scenario tree (detailed) | `IQHQ_PLAYBOOK.md` |
| Pre-registered Q2 reads | `workbook/PREDICTIONS.tsv` OZK-05→09 |
| Current positions + prices | `STATUS.md` + broker (book ⚠️ stale/not-managed; roll math archived) |

---

*KB evidence: 199 rows | Thesis: `THESIS.md` v1.4 | Weaknesses: `WEAKNESSES.md` (C7 added 2026-07-04) | Version history: `CHANGELOG.md` v1.4*
