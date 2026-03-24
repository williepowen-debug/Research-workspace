# OZK — Scenario Analysis & Target Prices
**Created:** 2026-03-23 | **Last Updated:** 2026-03-23
**Current Price:** ~$42-44 | **TBV:** $46.48 | **Book:** $52.46

---

## KEY INPUTS

### Capital & Reserves
| Metric | Value | Source |
|--------|-------|--------|
| Tier 1 Capital | $5,489M | FDIC API |
| Total Equity | $6,130M | FDIC API |
| TCE | $5,130M | Mgmt Comments |
| TBV/share | $46.48 | Mgmt Comments |
| Book/share | $52.46 | Mgmt Comments |
| Shares outstanding | ~110.4M | Derived |
| ACL — funded loans only (FDIC basis) | $475.7M | FDIC API — this is what covers actual noncurrent loans |
| ACL — total incl. unfunded reserve (company basis) | $631.9M | Mgmt Comments — includes $156.1M reserve for unfunded commitments, not available to absorb charge-offs on funded loans |

### Credit Trajectory
| Metric | Q3 2025 | Q4 2025 | Run Rate |
|--------|---------|---------|----------|
| Noncurrent | $149.7M | $341.2M | Doubling quarterly |
| Quarterly NCOs | $48.3M | $50.6M | ~$50M/quarter, accelerating |
| ACL | $532.3M | $475.7M | Declining $56.6M/quarter |
| Provision | — | $50.6M | Covering ~half of losses |
| ACL/Noncurrent | 3.55x | 1.39x | Collapsing |

### Structural Vulnerabilities
- **$7.0B construction on interest reserves** (89.7%) — cliff risk at maturity
- **2022 vintage wall:** $13.8B originated, hard maturities Q1-Q3 2026
- **IQHQ RaDD:** ~$555M funded, ~$500M value, maturity ~2028
- **$256.7M noncurrent in non-owner-occ CRE** — 75% of all noncurrent
- **Nonaccrual additions last 6 months:** $322M (RCONC410) — flow rate is high

---

## EXPECTED VALUE SUMMARY

**Adjusted probabilities reflect interest reserve artificiality + maturity wall mechanics (not priced by market).**

| Scenario | Prob | Price Range | Midpoint | Weighted |
|----------|------|-------------|----------|----------|
| Bear | **50%** | $30-37 | $33.50 | $16.75 |
| Base | **30%** | $38-44 | $41.00 | $12.30 |
| Bull | **15%** | $53-62 | $57.50 | $8.63 |
| Tail | **5%** | $18-25 | $21.50 | $1.08 |
| **Expected Value** | | | | **$38.75** |

**Current price ~$43 → implied ~10% overvaluation vs probability-weighted EV of $38.75.**

### Put Expected Value (rough, intrinsic only)
| Position | Strike | EV Intrinsic | Bear Intrinsic | Notes |
|----------|--------|-------------|----------------|-------|
| May $42.5 | $42.5 | ~$3.75 | $5.50-12.50 | Needs catalyst within 54 days |
| Aug $45 | $45 | ~$6.25 | $8.00-15.00 | Captures maturity wall window |

Bear case alone (50% prob): May put worth ~$4.50 intrinsic, Aug put worth ~$5.75. These are *minimum* values — vol expansion and panic premium add to it.

### Why Market Is Mispricing
1. **Interest reserve artificiality invisible** — RCONG376 is deep in Call Report, no analyst coverage mentions it
2. **"Current" construction book looks healthy on surface** — 89.7% is administered, not organic
3. **Noncurrent spike read as one-off** — market doesn't see the maturity wall pipeline behind it
4. **C&I reclassification flatters CRE ratios** — 37.6% Memo Item 3 not discussed by sellside
5. **Record EPS $6.18 anchors narrative** — earnings lag credit reality by 2-3 quarters
6. **"CIB diversification" narrative accepted uncritically** — 23 named NDFI counterparties are overwhelmingly CRE debt funds. CEO admits "a chunk of NDFI loans are actually RESG loans." True CRE/Tier 1: 411-420%, not reported 358%.
7. **Exit counterparty risk invisible** — Blue Owl (redemption gates, div suspended) is taking out OZK construction loans. Affinius (most frequent co-lender, 7+ deals) has $2.7B in bonds at 81¢ with Oct 2026 deadline. If either fails, OZK's construction maturity wall gets worse.

---

## SCENARIO A: BEAR CASE (50% probability)

**Thesis:** Interest reserve depletion + 2022 vintage maturity wall forces wave of nonaccrual conversions Q1-Q3 2026. Charge-offs accelerate beyond provisioning capacity. Market reprices to stressed bank multiple.

**Mechanics:**
1. Construction maturity wall hits Q1-Q3 2026. Borrowers can't refi (frozen market) or demonstrate stabilization (vacant buildings). Interest reserves depleted.
2. Noncurrent rises to $600-800M by Q3 2026 (from $341M). Plausible given $322M of additions in last 6 months alone and the maturity wall hasn't fully arrived.
3. Charge-offs accelerate to $80-120M/quarter as management is forced to recognize losses.
4. ACL consumed: $475.7M - ($80-120M × 2-3 quarters excess over provision) = ACL drops to $300-350M.
5. Provision catch-up forces earnings compression. EPS drops from $6.18 to $3-4 range.
6. Possible dividend cut consideration (currently $1.56/year).

**TBV Impact:**
- Cumulative excess charge-offs (above provision): $100-200M over 2-3 quarters
- TBV erosion: $46.48 → $44-45 (mild) to $42-43 (moderate) to $37-38 (if IQHQ partially written down)
- IQHQ partial writedown ($100-150M) in this scenario pushes TBV to ~$37-39

**Valuation:**
- Stressed CRE-concentrated bank trades at 0.7-0.9x TBV
- Historical comps: NYCB/FLG traded to 0.45x TBV at worst; OZK is better capitalized but more concentrated
- **Bear target: $30-37** (0.75-0.85x eroded TBV of ~$40-43)
- Deep bear (IQHQ + systemic): $25-30 (0.65x TBV)

**Why 50% (up from initial 40%):** The interest reserve data changes this materially. 89.7% of the construction book isn't organically performing — it's being administered. The market reads "low construction noncurrent" as health; we now know it's artifice. When the 2022 vintage matures Q1-Q3 2026, the cliff is mechanical, not probabilistic. The Q4 noncurrent spike was the *leading edge*, not an anomaly.

**Timeline:** Q2-Q3 2026 earnings catalysts (July, October reports)

---

## SCENARIO B: BASE CASE (30% probability)

**Thesis:** Management provisions just enough to keep ACL stable. Charge-offs elevated but manageable. No IQHQ resolution. Stock grinds lower on uncertainty but no break.

**Mechanics:**
1. Q1 2026 charge-offs: $60-80M (elevated, some construction maturities)
2. Provision roughly matches charge-offs. ACL flat at $450-500M.
3. Noncurrent rises to $400-500M but plateaus as some loans resolve (Pacific Center already done, Boston charged off)
4. EPS compresses to $4.50-5.50 (from $6.18) on higher provisions
5. Dividend maintained but under scrutiny
6. IQHQ extended to 2028 — deferred, not resolved

**TBV Impact:**
- Minimal erosion: TBV stays $44-47
- No forced capital raise

**Valuation:**
- Uncertain CRE bank with elevated but stable stress trades at 0.85-1.0x TBV
- P/E compressed to 7-9x on lower earnings
- **Base target: $38-44** (0.85-0.95x TBV)
- Current price (~$42-44) already reflects this — limited downside but limited upside

**Timeline:** Grinding, no single catalyst. Apr 16 earnings sets the tone.

---

## SCENARIO C: BULL CASE (15% probability)

**Thesis:** CRE stabilizes. Life sciences vacancy improves. Management rebuilds ACL. Market rewards "survived the cycle" narrative.

**Mechanics:**
1. IQHQ lands a significant tenant (unlikely given 25-29% SD vacancy, but possible)
2. Interest rate cuts enable refi of construction loans — maturity wall softened
3. Charge-offs normalize to $30-40M/quarter
4. ACL rebuilt to $550-600M
5. EPS returns to $5.50-6.00
6. Short squeeze amplifies recovery

**TBV Impact:**
- TBV grows to $48-50

**Valuation:**
- Recovering bank trades at 1.1-1.3x TBV
- **Bull target: $53-62** (1.1-1.25x growing TBV)
- Squeeze overshoot: $58-65 temporarily

**Timeline:** Requires 2-3 quarters of improving data. Earliest H2 2026.

**This is the loss scenario for puts.**

---

## SCENARIO D: TAIL RISK — CAPITAL EVENT (5% probability)

**Thesis:** Cascading losses trigger rating downgrade, deposit flight, forced capital raise.

**Mechanics:**
1. Multiple large loans go nonaccrual simultaneously (IQHQ + 2-3 construction)
2. ACL breached — provision surge crushes earnings to near-zero
3. KBRA/Moody's downgrade (KBRA already Negative outlook)
4. Uninsured deposit flight — **$11.9B uninsured (35.8% of deposits)**, 2.2x Tier 1 capital. A 20% run = $2.4B against already 74%-pledged loan book.
5. Forced equity raise at distressed pricing (dilutive)

**Valuation:**
- **Tail target: $18-25** (0.5-0.65x deeply eroded TBV)
- FLG (ex-NYCB) comp: traded to $3.49 at worst (0.3x TBV), but that was existential

**Timeline:** Unlikely before H2 2026 unless systemic trigger (HY OAS >500, broader CRE crisis)

---

## PUT STRUCTURE REVIEW

### Current Positions (assumed)
| Position | Strike | Expiry | Days Left | Scenario Alignment |
|----------|--------|--------|-----------|-------------------|
| May $42.5 Put | $42.5 | May 2026 | ~54 days | ⚠️ Tight — needs Apr 16 earnings to catalyze |
| Aug $45 Put | $45 | Aug 2026 | ~145 days | ✅ Aligns with Q2 maturity wall + Q1 earnings reaction |

### May $42.5 Assessment
- **At risk.** 54 days is tight. Needs April 16 earnings to deliver a negative surprise.
- **What could make it work:** Apr earnings show Q1 noncurrent rising (maturity wall beginning), provision surge, or management language change on IQHQ/construction.
- **What kills it:** Any positive headline, short squeeze on earnings beat, or "kitchen sink" quarter where management front-loads bad news but stock rallies on "worst is over."
- **Recommendation:** This is a *catalyst bet*, not a *thesis bet*. The thesis is right but 54 days is asking for precision timing.

### Aug $45 Assessment
- **Well positioned.** 145 days captures the 2022 vintage maturity wall (Q1-Q3 2026 hard maturities).
- **IQHQ is NOT a catalyst for this expiry** — maturity pushed to ~2028. But construction cliff + continued noncurrent growth is sufficient.
- **Interest reserve depletion** is the key mechanism — those $7B in construction loans will start hitting maturities through this window.
- **Risk:** Short squeeze could temporarily push stock to $50-55, putting Aug $45 underwater temporarily.

### Sizing Considerations
- Short interest 14-15% with 12-18 days-to-cover = squeeze risk is real
- Max drawdown tolerance: need to survive a $50-55 spike without panic
- Position sizing should assume 30-40% temporary loss is possible on squeeze days

---

## APRIL 16 EARNINGS — WHAT TO WATCH

1. **Noncurrent trajectory:** $341M → ??? If rising toward $400-500M, bear case accelerating.
2. **Provision vs charge-offs:** If provision < charge-offs again, ACL continues melting.
3. **Construction book commentary:** Any mention of maturity extensions, interest reserve depletion, or borrower distress.
4. **IQHQ disclosure:** Any update on leasing, valuation, extension terms.
5. **Management tone on CRE outlook:** Defensive = they know. Confident = either right or delusional.
6. **Unfunded commitments:** $18B → ??? If declining faster, forced drawdowns may be happening.
7. **C&I growth vs construction decline:** Continued divergence = continued reclassification.

---

*Parent files: `THESIS.md` | `EVIDENCE.md` | Source data: `sources/`*
