# Apr 17 PM — Thread 2 (Short Interest / Short Volume) + Thread 3 (Sell-side PT Distribution)

**Session:** Apr 17, 2026 PM (post-close, continued from midday RF synthesis)
**Purpose:** Sharpen Apr 21 WAL/OZK sizing decision by measuring (a) whether shorts are still crowded at position names, and (b) whether the street has any PT runway left before hitting thesis bear.

---

## Thread 2 — Short Interest / Short Volume

### Short Interest (bi-weekly settlement, last reading Mar 13 — 5 weeks stale)

| Ticker | Oct 31 | Dec 31 | Feb 27 | **Mar 13** | Trend |
|--------|--------|--------|--------|-------------|-------|
| OZK | 13.74% | 14.84% | 15.17% | **15.28%** | ⬆️ rising 5 months straight |
| WAL | 4.13% | 3.62% | 4.45% | **3.46%** | ⬇️ covered into Feb→Mar |
| EGBN | 9.27% | 12.23% | 10.62% | 11.10% | Elevated, flat |
| KRE | — | — | 55.8M | **69.4M (122% of float)** | ⬆️ +64% in 2 months |
| ZION | 4.34% | 5.13% | 3.75% | 4.03% | Flat |
| CFG | — | — | 4.33% | 4.44% | Flat |

### Short Volume (FINRA, pulled via `scripts/darkpool.py` this session)

| Ticker | Apr 8 | Apr 9 | **Apr 16** | Apr 17 Off-Ex% | Apr 17 Δ vs 30d |
|--------|-------|-------|-------------|----------------|-----------------|
| **WAL** | 40.7% | 52.3% | **63.3%** ⚠️ | 51.1% | **+13.5pp** VERY ELEVATED |
| **OZK** | 42.4% | 43.8% | **64.6%** ⚠️ | 50.0% | **+16.3pp** VERY ELEVATED |
| EGBN | 29.6% | 35.8% | 74.2% 🔴 | 45.4% | +11.7pp VERY ELEVATED |
| ZION | 62.7% | 39.2% | 65.6% | 48.0% | +12.0pp VERY ELEVATED |
| KRE | 56.6% | 74.1% | 60.7% | 33.1% | +3.8pp Above avg |
| CFG | 39.2% | 56.9% | 43.9% | 44.7% | +7.3pp Elevated |

Today's volume: WAL 733K shares (2.5x prior day), OZK 771K (3x prior day). Big rally-day with **≥50% off-exchange** at both position names.

### Verdict — MIXED

- **OZK — SHORTS STILL CROWDED & PRESSING.** SI% rising 5 settlements straight through Mar 13 (13.74 → 15.28). Short volume JUMPED from ~43% (Apr 8-9) → 64.6% (Apr 16), with 50% off-exchange today on +2.4% rally. 0% insider ownership = no buy wall. **Shorts are leaning into the squeeze, not covering.** OZK thesis-name short fully viable.
- **WAL — POSITIONING FLIPPED.** SI% declined through Mar 13 (4.13 → 3.46%, shorts covered ~1M shares in late Feb/Mar). But short volume surged +22pp Apr 8→16 and sits at 51% off-exchange on today's rally. Pattern: weak-hands covered in March, fresh shorts re-establishing into earnings. WAL is LESS crowded than OZK; newer shorts leaning into Apr 21 are the more fragile cohort with higher covering reflex on a beat.
- KRE is mechanical (122% SI of float, AP-redemption driven) — not a clean positioning read.
- EGBN 74.2% short volume (Apr 16) = cohort extreme; consistent with its 11x put/call OI from Apr 9 microstructure work.

**Decision implication:** OZK asymmetry intact; WAL asymmetry reduced but not broken. Lean slightly heavier to OZK if choosing between the two; or manage WAL by rolling strikes further OTM / further out in time to de-risk squeeze scenario.

---

## Thread 3 — Sell-side PT Distribution

### WAL — 16 analysts, current $79.48

**April PT walk-down is violent.** Known actions pulled via WebSearch + stockanalysis.com:

| Date | House / Analyst | Action | PT move | Rating |
|------|-----------------|--------|---------|--------|
| Apr 9 | KBW / McGratty | Cut | $101 → $93 | Buy maintained |
| Apr 8 | Truist | Cut | $98 → $90 | — |
| Apr 7 | Barclays / Shaw | Cut (2nd) | $90 → $88 | Buy maintained |
| Apr 7 | BofA | Cut | $90 → $86 | — |
| **Apr 7** | **UBS / Holowko** | **DOWNGRADE + Cut** | **$106 → $75 (-29%)** | **Strong Buy → Hold** |
| Apr 2 | Piper / Clark | Cut | $108 → $94 | Buy maintained |
| Apr 1 | JPM / Elian | Cut | $105 → $77 | Hold maintained |
| Mar 26 | WFC / Spahr | Cut + Upgrade | $83 → $79 | Hold |
| Mar 18 | Barclays / Shaw | Cut (1st) | $105 → $90 | Buy → Hold |
| Mar 10 | DA Davidson / Tenner | Cut | $105 → $93 | Buy |
| Mar 9 | TD Cowen / Lee | Downgrade | — → $83 | Buy → Hold |

**Distribution (stockanalysis.com Apr 17):**
- Rating split: **10 Buy / 5 Hold / 1 Sell** (4 Strong Buy / 6 Buy / 5 Hold / 1 Sell)
- Avg PT: **$91.47** (was $97.73 on Mar 31 = -6.4% in 17 days)
- Range: **$75 (UBS) → $110**
- Consensus label: Buy

### OZK — 10 analysts, current $48.95

**No April cuts.** Most recent moves:

| Date | House / Analyst | Action | PT | Rating |
|------|-----------------|--------|-----|--------|
| Apr 7 | UBS / Holowko | Assume coverage (reaffirm) | $48 | Neutral |
| Mar 31 | Morgan Stanley / Gosalia | Cut | $61 → $54 | Equal Weight |
| Mar 30 | WFC / Rutschow | Raise | $48 → $50 | Equal Weight |
| Mar 2 | Morgan Stanley | Raise (sector) | $57 → $61 | Equal Weight |
| Jan 22 | Piper / Scouten | Cut post-Q4 | $64 → $62 | Overweight |
| Jan 22 | Stephens / Olney | Cut post-Q4 | $64 → $62 | Overweight |
| Jan 22 | TD Cowen / Lee | Cut post-Q4 | $56 → $54 | Buy |
| Jan 5 | Citi / Gerlinger | Reiterate + negative catalyst watch | $40 | **SELL (since May 2024)** |

**Distribution (stockanalysis.com Apr 17):**
- Rating split: aggregator discrepancy — stockanalysis.com shows 1 SB / 3 B / 7 H / 0 S; MarketBeat/Daily Political Apr 14 shows 5 B / 5 H / 1 S. Citi's Sell likely dropped from stockanalysis' 3-month window.
- Avg PT: **$53.50**
- Range: **$40 (Citi) → $62 (Piper / Stephens)**

### Gap Math

| Gap | WAL | OZK |
|-----|-----|-----|
| Current → Street low | $79.48 → $75 = **-5.6%** | $48.95 → $40 = **-18.3%** |
| Street low → Thesis bear | $75 → $47 = **-37.3% unearned** | $40 → $35-40 = **0 to -12% unearned** |
| Street consensus → Thesis bear | $91.47 → $47 = **-48.6%** | $53.50 → $35-40 = **-25 to -35%** |
| Current → Thesis bear | $79.48 → $47 = **-40.9%** | $48.95 → $35-40 = **-18 to -28%** |
| April PT momentum | 7+ cuts; avg PT -$6 in 17 days | 0 April cuts; consensus stable |

### Verdict

**WAL → LONG RUNWAY. Street walking HARD.**
- Street low $75 is still 37% above thesis bear $47 — huge room for further downgrades.
- UBS flip from Strong Buy $106 → Hold $75 (-29% PT) is a **regime change** — the biggest bull folded 2 weeks pre-print.
- Clustered April cuts = houses pre-positioning for a miss. Classic setup.
- BUT: if WAL beats, fresh cuts at $77-88 create squeeze fuel back to $85-90. Thread 2's fresh shorts are at risk. Tape cuts both ways Monday.

**OZK → SHORT RUNWAY on PT gap. Edge is catalyst + microstructure, NOT analyst migration.**
- Citi $40 has been at/near thesis for 2 years. Street low gap to thesis = 0-12%. Already priced.
- 4 Buys at $54-62 are the downgrade candidates if Apr 21 shows credit inflection (NCO, IQHQ leasing, reserve coverage).
- Thread 2 confirmed OZK shorts still crowded AND pressing.
- Edge = catalyst-driven analyst capitulation + microstructure mechanics, not "street walks down to thesis" (street is already there).

### Decision implications for Apr 21 sizing

| Name | Asymmetry | Fragility to beat | Strike check | Duration check |
|------|-----------|---------------------|-------------|----------------|
| **WAL** | LONG runway remains | HIGH (squeeze risk, fresh shorts) | $85P / $77.5P near-money; $70P / $65P OTM but cheap | $85P Jun18 — TIGHT if thesis plays on Call Report (May 1-10) or Investor Day (May 12). **Consider rolling $85P → Jul/Aug.** |
| **OZK** | PT runway SHORT; catalyst runway LONG | HIGH (no analyst cushion left; miss = cascade) | $42.5P May — 13% OTM, needs ~20% drop | May strikes 32 DTE. If Apr 21 in-line, May expiry kills. **Aug strikes more durable.** |

**The setup in one sentence:** WAL is a squeeze-vs-cascade binary with plenty of PT-downgrade runway still to harvest; OZK has no more PT to harvest (street already at thesis) so its edge depends entirely on the print + microstructure firing.

---

## Open items carried into Thread 4

- Translate "thesis bear $47 at WAL" into a per-analyst downgrade count needed to mark-to-bear — i.e. which of the remaining 10 Buys have to flip?
- Verify OZK rating split discrepancy (stockanalysis.com vs MarketBeat) — does Citi still cover at Sell $40?
- Map each WAL/OZK thesis element to earliest visibility catalyst (Call Report May 1-10 / Investor Day May 12 / Q1 print itself) to align strike/expiry decisions.
