# OZK — Scenario Analysis & Target Prices
**Created:** 2026-03-23 | **Last Updated:** 2026-10-28 22:5x ET (**P-OZK-9 price re-base encoded, Will-approved 22:52 ET — EV $48.56**; currency fixes) · 2026-10-22 12:4x ET (**Q3 scorecard added; re-weighted under P-OZK-8, Will-approved in the OZK session 12:42 ET** — Bear 20 / Base 50 / Bull 28 / Tail 2, EV $44.41; D:L793 item 2; 4/23 table kept below as record). Earlier 10/22: sub-notes line re-based to the issuer 6.14% / ≈$12.0M. Scenario bodies below are 2026-07-06 vintage; thesis conviction 🟡 LOW, v1.7 → `THESIS.md`
**Price:** live → `STATUS.md` / boot.py (was $47.52 at the 4/23 reweight; $49.65 at 7/6 sweep; $50.51 close 10/28) | **TBV:** $47.50 (Q3 26; was $47.15 Q1 26)
**Short Interest:** live → `STATUS.md` (10/15 settlement ~18.6% of float, DTC 9.2, KB-266; the Mar-25 13.81% below is history)

> **Framing note:** Probabilities are scenario weights for position sizing. Post-Q1 reweight: migration-velocity metrics (past-due 10× in 6 months) confirmed the bear case at the leading-indicator layer, but capital buffer demonstrated through the print shrinks tail risk. Direction unchanged; weights shifted.

---

## Q3 2026 SCORECARD — each scenario's own mechanics vs the Q3 print (added 2026-10-22)

*Q3 sources: FDIC FLNG 12022 (MC Fig 22–23), 10/12 8-K FLNG 12019, 10/21 call. Grade detail → `research/threads/2026-10-21_Q3_PRINT_STAGE1_GRADE.md`.*

| Scenario | Its own Q3-dated mechanics | Q3 actual | Read |
|---|---|---|---|
| **Bear** | Noncurrent $600–800M by Q3 · NCO $80–120M/qtr · ACL eroded to $300–350M · EPS $3–4 | Nonaccrual **$89M**, NPA $510M · NCO **$44.5M** · ACL **$621.1M** (+$3.3M) · EPS $1.50/qtr (≈$6.00 annualized, DERIVED) | **Every dated mechanic missed.** Only live route left: OREO ($420M, no sale priced) marked down on sale — THESIS invalidation 7 |
| **Base** | NCO $60–100M/qtr · EPS $4.75–5.75 · IQHQ extends with $100–200M fresh equity · TBV $44–47 by Q4 · sub-notes reprice absorbed | NCO $44.5M (below) · EPS ≈$6.00 ann. (above) · **RaDD extended to Dec-2029 with fresh $100M (10/9)** · TBV **$47.50** · reset 6.14% | IQHQ leg **met**; credit cost lighter and earnings stronger than Base assumed |
| **Bull** | (1) IQHQ tenant >250K SF or $200M+ fresh sponsor capital · (2) Fed −100bp by YE26 · (3) past-due <$400M · (4) NCO $30–50M/qtr · (5) EPS $5.75–6.25 | (1) **partial** — $100M fresh capital, no tenant · (2) **not met** (the Sep'26 Fed move was a hike — THESIS §Short interest) · (3) **met** — $298M Q2, $88M Q3 · (4) **met** — $44.5M · (5) **met** — ≈$6.00 ann. | **3 of 5 met, 1 partial** |
| **Tail** | Multiple large nonaccruals at once · ACL breached · downgrade · deposit flight | CET1 11.44% (prelim) · PPNR $261.4M = 5.5× provision · classified+criticized −22% | Further away than at 4/23 |

⚠️ **The 4/23 weights are superseded.** They were set when Q1 had "confirmed the bear at the leading-indicator layer"; Q3 missed every Bear mechanic, met the Base IQHQ leg, and met 3 of 5 Bull mechanics. The 4/23 table is kept verbatim below as a record — do not cite its weights or the $38.97 EV as the desk's view.

## EXPECTED VALUE SUMMARY — CURRENT (weights P-OZK-8, Will 2026-10-22 12:42 ET · prices re-based P-OZK-9, Will 2026-10-28 22:52 ET, verbatim "P-OZK-9 approved, go ahead")

| Scenario | Weight (P-OZK-8) | Price range (P-OZK-9, Q3-based) | Midpoint | Weighted | Why this weight |
|---|---|---|---|---|---|
| Bear | **20%** | **$33–44** | $38.56 | $7.71 | Its dated mechanics all missed; kept at 20% because the appraisal-gated route (OREO $420M untested by sales, NCO "elevated through 2027" per MC p.21) is still open |
| Base | **50%** | **$43–49** | $46.02 | $23.01 | Management's own guided path — elevated losses as an earnings drag, no capital event — is the modal outcome |
| Bull | **28%** | **$57–68** | $62.15 | $17.40 | 3 of 5 own mechanics met at Q3, 1 partial |
| Tail | **2%** | **$18–26** | $22.00 | $0.44 | Capital and PPNR coverage stronger than at 4/23 |
| **EV** | | | | **$48.56** | 10/28 close $50.51 sits **4.0% above** EV |

**Method (P-OZK-9):** Q3-26 inputs (EPS $1.50, PPNR $261.4M/qtr, TBV $47.50, 108.4M shares, tax 22–23% guided), one 12-month horizon for all four branches, each branch's own multiple band unchanged (Bear 0.70–0.90×, Base 0.85–0.95×, Bull 1.10–1.30×, Tail 0.50–0.65× of end-state TBV). Full derivation, credit-path assumptions and limits → `research/threads/2026-10-28_SCENARIOS_PRICE_REBASE.md`. **Not folded in:** the Base multiple band sits below the market's own ~0.9–1.15× P/TBV range for OZK over the last 12 months; at 0.95–1.05× the EV would be $51.12 (sensitivity only, thread §5).
*Superseded:* P-OZK-8's EV **$44.41** (10/22, on the unchanged 4/23 midpoints $34 / $43 / $56 / $21.50).

Moves no prediction (OZK-09 45%, A30/B45/C8/D17, ~$129M EL unchanged), no THESIS version (v1.7) and no position; trades stay TERRY → Will.

---

## EXPECTED VALUE SUMMARY (reweighted 2026-04-23 — ⚠️ SUPERSEDED 2026-10-22 by P-OZK-8 above; record only)

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

## SCENARIO A: BEAR CASE (20% since 10/22 · was 55%)

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
- Stressed CRE bank: 0.7-0.9x eroded TBV
- **Bear target: $33–44** (P-OZK-9, 10/28, 0.70–0.90× a 12-month TBV of $46.76–49.32; was $28-35 on 4/23)
- Deep bear (IQHQ + systemic): $25-28 *(4/23 vintage, not re-based; the IQHQ leg it assumed was removed by the 10/9 extension — the Tail row carries the systemic case)*

**Why 50%:** 89.7% of construction on interest reserves is administered, not organic. Market reads "low construction noncurrent" as health — it's artifice. Q4 noncurrent spike was the leading edge. Maturity wall is mechanical, not probabilistic.

**Rate relief doesn't help much:** Stress is concentrated in office/life sci (75% of noncurrent) where the bottleneck is vacancy, not borrowing cost. Moderate rate cuts reduce bear probability by ~5% at most.

---

## SCENARIO B: BASE CASE (50% since 10/22 · was 30%)

**Q1 26 consistency:** This scenario is where Q1 print reads most cleanly. Mgmt tone confident (*"late stages of this CRE cycle"*), NCO 0.56% [Call Report] near guide, CET1 11.64%, buybacks accretive. Threads-the-needle mechanics observable.

**Thesis:** Management provisions just enough to stabilize ACL. Charge-offs elevated but contained. IQHQ resolution via Scenario A (extend with sponsor equity) or Scenario C (takeout). Slow grind sideways-to-lower; no capital event.

**Mechanics:**
1. Q2-Q3 26 charge-offs: $60-100M/quarter. Provision matches within ±10%.
2. Past-due $487.5M Q1 26 [Call Report] partially converts to NCO but plateau-s, not doubles again.
3. EPS compresses to $4.75-5.75 (from $6.18).
4. Dividend maintained under scrutiny; may skip 2026 increase cycle.
5. IQHQ extends in Aug 2026 with $100-200M fresh sponsor equity (20% weight in full scenario tree).
6. $350M sub notes reprice Oct 1 2026 as guided; ~$12.0M/yr headwind absorbed *(issuer printed **6.14%** for Q4-26, Q3 MC p.35 [FDIC FLNG 12022], updated 2026-10-22; prior desk estimate re-based 2026-10-01 at the actual benchmark, CME 3M Term SOFR 4.09580% [9/29] → coupon ≈6.19%, Act/360; the 9/24 ≈$11.2M used overnight SOFR as a proxy — `CALENDAR.md` Oct 1 row)*.

**TBV Impact:** Slow erosion — TBV $47.15 drifts to $44-47 range by Q4 26.

**Valuation:**
- Uncertain CRE bank: 0.85-0.95× TBV
- **Base target: $43–49** (P-OZK-9, 10/28, 0.85–0.95× a 12-month TBV of $50.58–51.63; was $40-46 on 4/23)
- 10/28 close $50.51 sits just above the base range.

---

## SCENARIO C: BULL CASE (28% since 10/22 · was 12%)

**Q1 26 pushback data:** NCO 0.56% [Call Report] near guide, TBV +11% YoY, buybacks at accretive prices, CET1 11.64%. Post-Q1 additions to this column: dividend hike +2.1% (7/1, 64th straight), $200M buyback authorization (6/30), Street targets low-to-mid $60s on RESG-runoff de-risking (→ `WEAKNESSES.md` C7). If we're wrong, these are the tells that would have warned us.

**Thesis:** CRE stabilizes, management rebuilds ACL, IQHQ cures, short squeeze amplifies the recovery.

**Mechanics:**
1. IQHQ lands material lab tenant (>250K SF at RaDD) OR sponsor commits 4th rescue round ($200M+ fresh equity) — despite Aimco April 2026 fraud suit
2. Fed cuts aggressively (100+ bps by YE 26) — enables construction loan refis, softens maturity wall
3. Past-due reverses Q2 26 (<$400M) — migration-velocity reading was a Q1 spike, not a pipeline
4. Charge-offs normalize to $30-50M/quarter
5. EPS recovers to $5.75-6.25

**Valuation:**
- Recovering bank: 1.1-1.3× TBV
- **Bull target: $57–68** (P-OZK-9, 10/28, 1.10–1.30× a 12-month TBV of $51.48–52.06; was $52-60 on 4/23)
- Squeeze overshoot: $58-65 temporarily (14-15% SI, 12-18 days to cover)

**This is the loss scenario for puts.** Size to survive a squeeze to $55 without panic. Cross-ref: THESIS.md "What Would Invalidate" §3 (IQHQ cures) + §5 (Fed cuts / structural turn).

---

## SCENARIO D: TAIL — CAPITAL EVENT (2% since 10/22 · was 3%)

**Downgraded from 5% → 3% post-Q1.** Capital buffer demonstrated: CET1 11.64%, $16.9B primary+secondary liquidity, $2.3B+ buffer above well-capitalized minimum. At current NCO run-rate capital grows, not erodes. A rating event or deposit flight sequence would require NCOs to roughly triple from current pace — low probability even in Scenario A path.


**Thesis:** Cascading losses → rating downgrade → deposit flight → forced capital raise.

**Mechanics:**
1. Multiple large loans go nonaccrual simultaneously
2. ACL breached, provision surge crushes earnings to near-zero
3. KBRA/Moody's downgrade (KBRA already Negative outlook)
4. Uninsured deposit flight: $11.9B uninsured (35.8%), 2.2x Tier 1
5. Forced dilutive equity raise

**Valuation:**
- **Tail target: $18–26** (P-OZK-9, 10/28, 0.50–0.65× a TBV eroded to $36.69–40.29 before any dilutive raise; was $16-24 on 4/23)

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

⏹️ **DEAD SURFACE — the per-position EV tables below price legs that NO LONGER EXIST (dated-tag 2026-08-23).** The May-15 lines expired 2026-05-15; the **Aug-21 lines expired WORTHLESS at the 2026-08-21 OPEX** (Will's 8/4 RIDE ruling; realized −$1,686.37 / −100%). **The book is empty — there is nothing here to act on, at any price.** ⚠️ **The scenario logic is NOT dead and is NOT retired by this tag:** the four branches remain the desk's framework *(current weights Bear 20% / Base 50% / Bull 28% / Tail 2% since 2026-10-22, P-OZK-8 — top of this file; the 4/23 55/30/12/3 are superseded)*, and the underlying price/severity branches are still the desk's live framework. What is dead is the option-payoff layer bolted onto them. Any future OZK expression is a **new** trade — TERRY-built, Will-gated — never a revival of the tables below. *(Superseded: the prior banner's "STALE / NOT MANAGED … Aug 21 lines are unverified against broker" — they are no longer unverified, they are gone. Intrinsic-value math still uses Mar-24 anchors: $44.70 baseline, $4.05 entry.)*

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
6. **Exit counterparty risk** — **October12 source correction:** the identifiable $2.691B bonds are NEA/USRE2021-1 warehouse lease ABS, original ARDOctober20,2026/legal final2061. The “no such bonds” rejection was overbroad; **81¢ is historical2025 reporting**, not current corporate pricing. Direct OZK ABS exposure and automatic Affinius corporate default unproved. Current servicing terms/payoff UNKNOWN. → `research/threads/2026-10-12_AIMCO_AFFINIUS_CHECK.md`. No scenario number changed.

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
| Scenario weights / EV | THIS FILE (re-weighted 2026-10-22, P-OZK-8) |
| Thesis pillars + invalidation | `THESIS.md` (its own header is canonical for the version, never this table) |
| Bull-case rebuttals | `WEAKNESSES.md` (C7 RESG-runoff steelman added 2026-07-04) |
| IQHQ scenario tree (detailed) | `IQHQ_PLAYBOOK.md` |
| Pre-registered Q2 reads | `workbook/PREDICTIONS.tsv` OZK-05→09 |
| Current positions + prices | `STATUS.md` + broker (book ⚠️ stale/not-managed; roll math archived) |

---

*KB evidence → `workbook/KB.tsv` | Thesis → `THESIS.md` | Weaknesses → `WEAKNESSES.md` | Version history → `CHANGELOG.md` (footer tokens removed 10/28: they carried v1.4 / 199 rows long after both moved)*
