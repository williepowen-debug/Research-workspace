# Print-reaction envelope — CRUISE names (CCL / NCLH / RCL)

**Built 2026-09-19 Sat ~20:4x ET** (`date` wall clock, copied not inferred). **Markets CLOSED; every price is the 2026-09-18 regular-session close and every option quote is Friday's last two-sided quote** — root rule #4, and `RISK_RULES` **5b**: vendor chain marks are SCREENING marks over a weekend doubly so. ⛔ **No fill may be priced off this file.**

**Why this file exists:** construction rule **#18** measured its 10%-OTM line on **regional-bank singles** and says so in its own scope clause — *"Before applying the 10% line to another sector, re-measure the envelope — the tool is re-runnable."* Will directed a cruise-sector look on 2026-09-19. This is that re-measure. **It is a STRUCTURE-property file (rule #14): the envelope is a fact about these names and does not expire tonight. The quotes inside it DO.**

**Instrument:** `options/partb_realized_moves.py`, extended this session to take tickers on argv (default basket unchanged — **regression-checked byte-identical against a pre-edit baseline run**). Reaction attribution came from the vendor timestamp on all 24 rows (`attrib=ts`), never the convention fallback.

---

## 1 · The envelope — realized 1-day close-to-close print reactions, last 8 prints each

| name | n | mean \|mv\| | median \|mv\| | max \|mv\| | worst DOWN | # down | reachable by a print? |
|---|---:|---:|---:|---:|---:|---:|---|
| **CCL** | 8 | 4.73% | 4.59% | 9.81% | **−4.87%** | 5 | 🔴 **downside capped ~5%** |
| **NCLH** | 8 | 9.09% | 8.90% | 15.28% | **−15.28%** | 6 | ✅ **yes, and skewed down** |
| **RCL** | 8 | 7.14% | 5.37% | 18.65% | −8.53% | 2 | ⚠️ skewed **UP** |
| *(reference: WAL/OZK/HBAN/ZION, rule #18's own basket)* | 8 ea | 2.5–3.4% | 1.6–3.4% | 6.0–9.7% | −3.95 to −8.93% | 3–4 | — |

**⇒ Cruise prints run ~2× the regional-bank envelope. Rule #18's 10% line does NOT transfer — it is too tight for NCLH and too loose for CCL's downside.** The per-name numbers below replace it for this sector.

**CCL, print by print** (reaction session = same session; BMO release): −0.32 · +6.43 · −1.23 · +6.91 · −3.98 · **+9.81** · −4.31 · −4.87.
🔑 **The asymmetry is the finding: CCL's three largest moves are all UP (+6.43 / +6.91 / +9.81) and NOT ONE of eight down-prints exceeded −4.87%.**
⚠️ **Counter-qualifier, stated because it cuts against the contrarian read: the LAST THREE prints are all down and monotonically worsening** (−3.98 → −4.31 → −4.87, Sep-25 / Mar-26 / Jun-26). **n=3. It is a trend in a sample too small to be a base rate, and it is named so the up-skew is not quoted without it.**

**NCLH, print by print:** +6.29 · −5.31 · −7.77 · +9.23 · **−15.28** · −10.53 · −8.56 · −9.78.
🔑 **The last FOUR consecutive prints were all down 8.56–15.28%, mean −11.04%.** ⚠️ **n=4.**

---

## 2 · The EV tables — does the realized envelope pay the premium?

Black-Scholes, r=4%, spot held flat to the print (so **drift between now and the print is NOT modelled, in either direction**; theta from 9/18 to the print **is**, because each value is struck at the post-print DTE). Debits are the **ask** — the side you buy. Post-print IV is swept, because it is the assumption most likely to be wrong.

### CCL — the 2026-09-29 print (CONFIRMED at CCL's own press release 9/15, via CRUISE)

| structure | debit (ask) | EV over **all 8** prints | EV over the **5 DOWN** prints |
|---|---:|---:|---:|
| Oct-02 **21P** (−3.8% OTM) | $0.54 | **−70.9%** | **−53.5%** |
| Oct-02 **22P** (ATM) | $1.01 | **−44.7%** | **−12.4%** |
| Oct-16 **21P** | $0.81 | **−44.0%** | **−17.8%** |
| Nov-20 **21P** | $1.21 | **−24.4%** | **−2.0%** |
| Nov-20 **20P** | $0.81 | **−29.9%** | **−6.9%** |
| Nov-20 **21P/17.5P spread** (rule 18(b)'s "sell the rich wing" form) | $1.01 on $3.50 | **−26.2%** | **−5.5%** |

🔴 **THE SENTENCE THIS FILE EXISTS FOR: on CCL, the right *direction* does not pay. Every structure is negative-EV even after the direction is granted for free.**

**Sensitivity — the verdict survives the assumption sweep** (EV over the 5 down prints, post-print IV 35%→55%):

| structure | IV 35% | 40% | 45% | 50% | 55% (no crush at all) |
|---|---:|---:|---:|---:|---:|
| Oct-02 21P | −59.5% | −53.5% | −47.3% | −41.0% | −34.5% |
| Oct-02 22P | −14.5% | −12.4% | −10.0% | −7.4% | −4.7% |
| Oct-16 21P | −33.0% | −22.2% | −11.3% | −0.4% | +10.6% |
| Nov-20 21P | −20.0% | −7.2% | +5.8% | +18.7% | +31.6% |

⇒ **Only Nov-20 turns positive, and only if front-month event premium does NOT crush** — which contradicts `IV_CRUSH_PARTA_2026-07-17`'s measured **+10–16 vol pts** of event premium in front-month strikes. The Friday chain shows exactly that premium live: **CCL Oct-02 ATM IV 54.7% vs Nov-20 ATM 45.4% — a 9.3 vol-point front-month kink.** Buying the front expiry pays it; the sweep says paying it is not recoverable from CCL's realized down-moves.

**Rule #18(a) additionally kills the spread as a print trade:** the 17.5P short leg is **−19.9% OTM**. The print cannot reach it. Its real catalyst would be multi-quarter transmission, and CRUISE has no dated catalyst for that before Q4.

### NCLH — the 2026-11-04 print *(vendor calendar, `earnings_dates` 07:00 ET — ⚠️ **UNVERIFIED at NCLH IR or an 8-K**, and `RISK_RULES` § Option-Specific forbids taking a print date from memory or a vendor. **Confirm before this number is used in a card.**)*

`Dec-18 14P` (ATM, −0.8%), debit **$1.35** ask, spread **2.25%**, OI **3,870**, IV **50.20%**, 91 DTE from 9/18 → **88 DTE from Mon 9/21, i.e. INSIDE the 60–90 band** (rule #21: this would be a NEW deployment, so the band binds in full — it clears).

| basis | EV @ post-print IV 42% | 45% | 50% |
|---|---:|---:|---:|
| **all 8 prints** | −9.7% | −6.2% | **−0.2%** |
| **the 6 DOWN prints** (direction granted) | +9.3% | +15.0% | +20.8% |
| **the last 4 prints only** (the regime claim) | +22.4% | +25.6% | +31.1% |

🔑 **Read this honestly: against its OWN 8-print base rate the option is priced at roughly fair — EV ≈ 0. There is no structural mispricing to harvest.** The entire edge is a **regime claim** that the last four prints (all −8.6 to −15.3%) are the right sample and the earlier four are not. **That is n=4 and it is subjective** (`RISK_SCORING` §2: never invent a precise p_model; if it is subjective, say so). ⇒ **The trade is a directional bet wearing an event's clothes.**

**Structural facts that DO hold regardless (rule #14 — stable, gradeable any time):**
- **NCLH skips November entirely.** `2026-10-30` (42 DTE) **expires five days BEFORE the 11/4 print** and `2026-12-18` (91 DTE) is the first expiry that spans it. **There is no mid-tenor choice.** *(Same defect this desk measured on VLO/MPC on 9/11 — an empty 60–90 band. Worth noting it recurs.)*
- **Dec-18 liquidity is the best in the sector:** spreads 2.25–11%, OI 1,455–22,435, skew flat at ~50–51% from the 13 to the 18 strike. Strike gap 10 → 13 (no 11 or 12).
- Leg gate on `14P`: **✓ usable, two-sided** (`chain_fetch --legs 14`, rc=0).
- ATM straddle Dec-18 ≈ **$2.97 = 21.0% of spot** — the market prices ±21% by 12/18; a −11% print is **half** of that, so the print alone does not beat the price. You need print **plus** continued drift.
- ⚠️ Put IV 50.20% vs call IV 56.89% at the same 14 strike. **Checked, not chased:** C−P = 0.31 vs S−PV(K) = 0.259 — a $0.05 gap, inside the legs' own bid/ask. Parity holds; the IV split is vendor carry-assumption noise, not a signal.

### RCL — the 2026-10-27 print *(vendor, same UNVERIFIED caveat)*
**Not a bear candidate on this measurement.** 2 of 8 prints down, max **+18.65%**, FY26 guide **raised**. A put here is fighting the name's own print distribution. Recorded so the sector is covered, not because anything is proposed.

---

## 3 · What this does NOT say

- ⛔ **It sets no level, arms nothing and proposes no card.** Both CRUISE rows are **Will-ruled WATCH, no card** (`WQ-218` ①②, 2026-09-10). A card is a **fresh** proposal under root rule #5 — this file is an input to one, never a substitute.
- ⛔ **It is not a thesis.** Thesis ownership is CRUISE's (HARD BOUNDARY #3). This file answers only *"can the instrument pay the view?"*
- ⚠️ **Spot is held flat to the print in every EV table.** Real drift between 9/21 and the print is unmodelled and can dominate — that omission favours neither side and is the largest single limitation here.
- ⚠️ **Eight prints is eight prints.** The CCL sample spans a cruise-demand boom (2024–25) into a de-rating (2026); the two halves are not the same regime, which is exactly why the last-3 / last-4 qualifiers are written beside the headline numbers rather than under them.
