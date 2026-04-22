# Thread 3 — OZK May $42.5P Roll Math

**Date:** 2026-04-22 ~evening ET | **Decision deadline:** this week (sooner = better; $0.30 premium decays fast) | **Hard expiry:** May 15, 2026

> **Thesis stance:** Timeline uncertain, NOT broken. Q1 print confirmed slow-grind (past-due doubled $207M → $465M QoQ; classified+criticized +23% QoQ; 3 new substandard credits). But NCO 0.57% in-line — recognition tempo is Q2-Q3 2026, not April. Rule #7: roll duration, don't trim size.

---

## 1. CURRENT POSITION

Per `IQHQ_PLAYBOOK.md §6` (Apr 22/23):
- **OZK $42.5P May 15 × 2 contracts** ← this thread's subject
- OZK $42.5P Aug 21 × 1 contract ← existing, correctly durationed
- OZK $45P Aug 21 × 4 contracts ← existing, correctly durationed

⚠️ **Verify with broker before executing.** CALENDAR.md also references a `$45P May` position — unclear if real or a mislabeling of Aug 21 strikes. If confirmed, same math applies at $45 strike (higher ask, same ROI profile).

**Post-print tape (Apr 22, 19:05 ET):** OZK $47.52 (-2.06%). May $42.5P is ~10.6% OTM, 23 DTE, mid $0.30, Δ −0.13, IV 43%. **Effectively a stub** — close to recover ~$25-35/contract = ~$60 total.

---

## 2. LIVE OPTIONS CHAIN (Apr 22 close)

| Roll Candidate | K | DTE | Bid / Ask | Mid | IV | Δ | OI | Note |
|---|---|---|---|---|---|---|---|---|
| CURRENT close | 42.5 | 23 | $0.20 / $0.40 | $0.30 | 42.9% | −0.13 | 1428 | Close for ~$30/ctr |
| Jun $42.5 | 42.5 | 57 | $0.55 / $0.70 | $0.62 | 34.0% | — | **3** | Liquidity dead — avoid |
| Aug $40 | 40.0 | 121 | $0.85 / $1.20 | $1.02 | 38.3% | −0.17 | 97 | Cheapest |
| **Aug $42.5** | 42.5 | 121 | $1.25 / $1.75 | $1.50 | 36.1% | −0.24 | **115** | Highest ROI, most liquid |
| Aug $45 | 45.0 | 121 | $2.05 / $2.40 | $2.22 | 33.0% | −0.32 | 60 | Near-ATM; overlaps existing $45P×4 |
| Nov $40 | 40.0 | 212 | $1.50 / $2.05 | $1.77 | 37.1% | −0.20 | **7** | Thin |
| Nov $42.5 | 42.5 | 212 | $2.10 / $2.80 | $2.45 | 35.9% | −0.26 | **3** | Thin — execution risk |
| Nov $45 | 45.0 | 212 | $2.90 / $3.70 | $3.30 | 34.6% | −0.33 | **6** | Thin |
| Jan27 $40 | 40.0 | 268 | $1.80 / $2.60 | $2.20 | 37.4% | −0.21 | 341 | Long LEAP, liquid |
| **Jan27 $42.5** | 42.5 | 268 | $2.70 / $3.00 | $2.85 | 33.4% | −0.26 | **24** | Longest usable duration |
| Jan27 $45 | 45.0 | 268 | $3.50 / $4.00 | $3.75 | 32.7% | −0.33 | 328 | Near-ATM LEAP |

---

## 3. SCENARIO P&L (time-aware, per contract, cost = ask)

From `IQHQ_PLAYBOOK §3` — probabilities & stock-price calibrations:

| Scenario | Prob | Stock target | Fire date | IV bump |
|---|---|---|---|---|
| A — Sponsor extends | 20% | $53 | Aug 15 (just pre-maturity) | flat |
| B — Substandard / reserve | **50%** | $41 | Jul 20 (Q2 call) | +10pp |
| C — Third-party takeout | 12% | $56 | Jul 15 | −5pp |
| D — Foreclosure / distressed | **18%** | $36 | Oct 15 (post-maturity) | +15pp |

Value at scenario firing = BS(spot=target, K, T_remaining_to_expiry, IV_bumped). Then EV = Σ prob × value.

| Roll | Cost (ask) | A_extend | B_substand | C_takeout | D_foreclose | **EV/ctr** | EV-Cost | **ROI** |
|---|---|---|---|---|---|---|---|---|
| Aug $40 | $1.20 | $0.00 | $1.77 | $0.00 | $4.00 | $1.61 | +$0.41 | **+34%** |
| **Aug $42.5** | $1.75 | $0.00 | $3.00 | $0.00 | $6.50 | $2.67 | +$0.92 | **+53%** |
| Aug $45 | $2.40 | $0.00 | $4.61 | $0.01 | $9.00 | $3.93 | +$1.53 | **+64%** |
| Nov $40 | $2.05 | $0.24 | $3.63 | $0.11 | $4.85 | $2.75 | +$0.70 | +34% |
| **Nov $42.5** | $2.80 | $0.44 | $4.85 | $0.21 | $6.83 | $3.77 | +$0.97 | **+35%** |
| Nov $45 | $3.70 | $0.74 | $6.27 | $0.37 | $9.04 | $4.95 | +$1.25 | +34% |
| Jan27 $40 | $2.60 | $0.57 | $4.42 | $0.28 | $5.99 | $3.44 | +$0.84 | +32% |
| **Jan27 $42.5** | $3.00 | $0.69 | $5.30 | $0.30 | $7.53 | $4.18 | +$1.18 | **+39%** |
| Jan27 $45 | $4.00 | $1.11 | $6.73 | $0.52 | $9.50 | $5.36 | +$1.36 | +34% |

**Raw-ROI winner:** Aug $45 (+64%). But adding 2 more to existing $45P × 4 stacks concentration at one strike/expiry.
**Raw-ROI runner-up:** Aug $42.5 (+53%). Stacks on existing Aug $42.5P × 1 for Aug $42.5P × 3 total.

---

## 4. BOOK CONTEXT — THE CONCENTRATION CONSTRAINT

Existing OZK put book (per IQHQ_PLAYBOOK):
- Aug 21 $42.5P × 1
- Aug 21 $45P × 4
- May 15 $42.5P × 2 ← rolling

**All 7 contracts currently share a 4-month window.** The existing Aug book already fully covers Scenarios B (Q2-Q3 firing) + C (pre-maturity takeout) + A (pre-maturity extension). What Aug 21 **does not cover**:

- **Scenario D (18% prob, highest-loss outcome):** Foreclosure/distressed exit; charge-off tempo is Oct-Dec post-maturity. Aug 21 expires before Gleason would book the loss.
- **Gleason Q2 earnings call (~mid-Jul):** Captured by Aug, but post-call stock path extends into Sep-Oct.
- **Bluerock Q1 NAV marks (May-Jun) → Q2 NAV marks (Aug-Sep):** Second mark date falls outside Aug expiry.
- **Aimco motion-to-dismiss (early Jun), discovery phase (summer):** Drags into Q3/Q4.

**The marginal question is NOT "what's the highest ROI roll" — it's "what does the existing book need complemented with?"** The answer is duration past Aug 21, to capture Scenario D.

---

## 5. RECOMMENDATION

### Primary recommendation: **Close May $42.5P × 2 → Open Jan27 $42.5P × 2**

**Transaction:**
- STC (sell to close) 2× OZK 250515P42.5 @ limit $0.30 (mid) — fillable given today's vol 85
- BTO (buy to open) 2× OZK 270115P42.5 @ limit $2.85 (mid) — may need $2.90 given OI 24
- **Net debit: ~$510** ((2 × $2.85 − 2 × $0.30) × 100 = $510)

**Why this over Aug $42.5 (raw-ROI winner):**

| Dimension | Aug $42.5 × 2 | Jan27 $42.5 × 2 |
|---|---|---|
| Weighted ROI | +53% | +39% |
| Captures Scenario D | Partial (expires Aug 21, D fires Oct 15) | **Full** |
| Captures post-maturity announcements | No | **Yes** |
| Book concentration | Stacks: Aug $42.5 → 3 ctr, + Aug $45 × 4 = 7 Aug contracts | **Diversifies** — Aug stays at 5, Jan27 adds 2 |
| Net debit | ~$280 | ~$510 |
| Liquidity | OI 115 (excellent) | OI 24 (workable) |
| Scenario A hedge (extension, stock rallies to $53) | Loses all ($0 value) | Residual $0.69/ctr (LEAP vega) |

**Rationale:** Rule #7 (roll duration, not size). The existing Aug book is already sized for B/C/A resolution at the maturity date itself. What's missing is duration to capture the slow-grind flow-through — Scenario D's Q3/Q4 charge-off tempo and the indirect cues (Bluerock marks, Aimco discovery, Gleason Q3 earnings). Jan27 $42.5 is the longest-duration OZK expiry with usable liquidity and the cleanest strike alignment with the rest of the book.

### Alternative: **Split the roll** — Close May $42.5P × 2 → Open 1× Aug $42.5P + 1× Jan27 $42.5P

- Captures B via Aug (highest B-ROI at +53%) **and** D via Jan27 (highest D-ROI at +39%)
- Net debit: ~$395
- **Only if broker charges per-leg, not per-ticket** — double commission could eat the theoretical ROI advantage
- Executionally clean (fills independently)

### Not recommended:
- **Aug $45 × 2:** Highest raw ROI but adds to the already-concentrated Aug $45 bucket (would be 6 contracts at one strike/expiry = fragile).
- **Nov $42.5 × 2:** OI 3 means limit orders may not fill. Execution risk too high for a routine roll.
- **Jun $42.5:** OI 3, doesn't capture maturity catalyst. Dead duration.

---

## 6. TIMING

- **Close May $42.5P this week** (Thu-Fri Apr 23-24, or early next week latest). $0.30 premium decays toward zero over next 14 days; waiting costs the recovery.
- **Open Jan27 $42.5P on a red day for OZK** (ideally after stock rally, since we're BUYING puts — prefer lower put premiums on green stock days). Today was red (-2.06%) → puts elevated. Target green day in next 3-5 sessions if possible, else execute at limit regardless.
- **Hard rule:** Don't let the roll become a forced exit at expiry week. Execute by ~May 8 per CALENDAR.

**Puts-on-green-days reminder (Rule #6):** OZK just fell 2% today, so put IVs are bid. A green day in the next week = better entry on Jan27 $42.5P. If no green day, execute anyway — roll priority > entry timing on a roll.

---

## 7. WHAT WOULD CHANGE THIS RECOMMENDATION

| Trigger | Effect on recommendation |
|---|---|
| Q1 Call Report (May 1-10) reveals >$100M specific reserve on RaDD already booked | Scenario B probability spikes → compress duration back to Aug |
| OZK announces IQHQ extension in Q2 earnings prep (unlikely before mid-Jul) | Scenario A triggering early → all puts hurt; don't add, let May expire |
| Stock moves below $45 pre-roll | $45P becomes the better strike (deeper ITM potential); switch to Jan27 $45 or Aug $45 |
| Bluerock marks IQHQ PIK to $0 (May-Jun) | Scenario D probability rises → Jan27 becomes even more correct |

---

## 8. HANDOFF

**Update for next session upon execution:**
- POSITIONS.md: mark May $42.5P × 2 closed, add Jan27 $42.5P × 2
- IQHQ_PLAYBOOK §6: update position list
- OZK/STATUS.md: add Jan27 $42.5P to position row in convergence matrix

**Related threads:**
- Checkpoint 1 & 2 (KB persistence + THESIS v1.1) still queued
- WAL Round 2 awaits supplement/transcript
- Request to Will: browser-pull Q4 24 / Q1 25 / Q2 25 / Q3 25 OZK Management Comments PDFs (8Q mix-shift trajectory — Thread C limited to 2Q window)

---

*Generated from live yfinance chain Apr 22 2026 19:05 ET. OZK spot $47.52. Risk-free rate 4.29% (10Y UST). Scenario weights & stock targets per `OZK/IQHQ_PLAYBOOK.md`.*
