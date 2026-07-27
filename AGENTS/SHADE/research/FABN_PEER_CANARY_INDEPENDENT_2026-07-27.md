# SHADE — The FABN peer canary, rebuilt independently from holder filings

**Date:** 2026-07-27 ET
**Why:** the canary (Athene 5Y FABN **T+123**, **+43–48bp** vs peers) comes from **Athene's own investor deck**, which also **picks its own peer set** (CRBG/EQH/PFG). That is an incentive-flagged source carrying a load-bearing kill-path-1 signal, and it had gone ~2 months stale.
**Method/data:** `research/FABN_PEER_SPREAD_NPORT_2026-07-27.py` + `...json` (rerunnable each quarter).

---

## VERDICT

**⚠️ This is a CORROBORATION, not a refresh — and I should not have implied one was impossible without testing it.**

**Athene's self-reported peer penalty checks out.** An independently constructed measurement, from primary holder marks with a **SHADE-chosen peer set**, lands at **+40bp (strictest design) to +59bp (CUSIP-level)** — **bracketing the deck's +43–48bp.**

**On a day spent finding that self-defined categories flatter their definers, this particular self-reported number does not.** Worth saying plainly.

**But it is NOT fresher.** My data spans **2026-03-31 → 05-31**, straddling the deck's 5/14 observation. **The genuine refresh is Apollo/Athene Q2 on Monday 2026-08-04 (T+8)** — now a confirmed date, not "early August."

---

## 1. DESIGN — why this is a fair test and not just another number

**The core control: only funds holding BOTH Athene Global Funding AND ≥1 peer FABN program, in the same filing.** Same fund, same valuation date, same pricing vendor ⇒ methodology-level differences cancel, and what remains is issuer credit.

**Peer set (SHADE's, not Athene's) — FABN-program-to-FABN-program, the like-for-like comparison:** MassMutual Global Funding · Met Tower Global Funding · Pricoa Global Funding · GA Global Funding · Corebridge Global Funding · New York Life Global Funding.

**Pipeline:** EDGAR FTS → 122 NPORT-P filings → 726 raw holdings → 513 after dedup/sanity → **51 matched funds, 427 holdings**. **0 fetch failures.** Spread = YTM(price, coupon, maturity, bisection) − matched-tenor Treasury (FRED, at each period end).

---

## 2. RESULT — four estimators, reported together because they disagree in an informative way

**3–6y bucket (the tenor matching the "5Y" canary):**

| Estimator | Athene | Peers | **Penalty** |
|---|---:|---:|---:|
| Pooled holdings (n=43 vs 46) | T+142.4 | T+87.0 | **+55.4bp** |
| **One obs per CUSIP** (8 vs 21 CUSIPs) | T+145.3 | T+86.5 | **+58.8bp** |
| **Within-fund paired (strictest)** — n=15 funds | — | — | **+40.2bp median** (mean +33.0) |
| Athene's own deck [JPM data 5/14] | T+123 | T+75–80 | **+43–48bp** |

**🔑 The number I carry forward is the within-fund paired one: +40.2bp median, positive in 11 of 15 funds, IQR −1.0 to +52.3bp.** It is the strictest design and the most honest — **and its dispersion is real: 4 of 15 matched funds show zero or negative.**

**0–3y bucket:** Athene T+79.5 vs peer median T+47.8 = **+31.6bp** (CUSIP-level: +30.2bp). Penalty is present but **smaller at the front end**.

⚠️ **6–11y: DO NOT CITE.** The "+28.6bp" the script printed rests on **4 Athene holdings of a single CUSIP** (`04685A4S7`). One bond is not a tenor bucket.

---

## 3. ⚠️ WHAT THIS DOES **NOT** SUPPORT — the widening trajectory

STATUS carries: *"Feb'26 T+105 (+23–34bp) → May'26 T+123 (+43–48bp): the penalty appears to have widened ~+15bp over the quarter."*

**My independent data does not corroborate continued widening, and read literally points the other way:**

| Period | Athene 3–6y | Peers | Penalty | Athene n |
|---|---:|---:|---:|---:|
| 2026-03-31 | T+142.9 | T+92.6 | **+50.3bp** | 31 |
| 2026-04-30 | T+132.0 | T+78.6 | **+53.4bp** | 8 |
| 2026-05-31 | T+116.1 | T+83.6 | **+32.5bp** | 4 |

**Athene's absolute level DECLINES across the three dates (142.9 → 132.0 → 116.1) and the penalty falls at 5/31.**

**But this is NOT evidence of narrowing either — the samples collapse (n=31 → 8 → 4) and the CUSIP composition changes between dates, so it is not like-for-like.** **Correct read: the direction is UNESTABLISHED in either direction after March.** What I can say is that the "widening" story now has **one independent dataset that fails to confirm it**, so it should stop being carried as a trend and be re-tested on the 8/4 deck.

---

## 4. LIMITS — state them before anyone trades off this

- **Marks, not prints.** NPORT fair values come from fund pricing services, not TRACE executions. **Levels are indicative; the DIFFERENCE is the robust output** — which is why the penalty, not T+142, is the deliverable.
- **YTM is approximate:** semiannual bisection on price/coupon/maturity; ignores accrued interest, day-count, and call/make-whole features. **Systematic ⇒ largely cancels in a matched-tenor difference.**
- **Thin tails.** 3–6y Athene rests on **8 unique CUSIPs**; the front end is much deeper (24 CUSIPs). Anything beyond 6y is unusable at this sample.
- **Peer set is mine.** That is the point (it removes Athene's curation) but it means my level is **not** directly comparable to the deck's — only the *penalty* is.
- **Not fresher than the deck.** 3/31–5/31 vs the deck's 5/14.

---

## 5. WHAT CHANGES

- **Kill-path-1 stays YELLOW.** Nothing here approaches the escalation bar (**FABN spread >250bp** or a **pulled syndication**). Athene at ~T+142 in the belly is still an *absolute* green-band funding cost.
- **The canary's provenance is upgraded** from single-source-self-reported to **self-reported + independently corroborated**. That is a real strengthening of a load-bearing input.
- **The "widening ~+15bp" claim is downgraded to unestablished** pending 8/4.
- **A rerunnable instrument now exists.** Re-run the script each quarter; it costs ~4 minutes and needs no terminal. **It also has a second use: the same matched-fund design can test any insurer-vs-peer funding-cost question SHADE cares about.**

---

## 6. NEXT

| # | Action | When |
|---|---|---|
| 1 | **Apollo/Athene Q2 earnings + FI deck — the real refresh.** Pull the 5Y FABN secondary + peer table; compare to this file's +40bp. | **2026-08-04 (T+8), confirmed** |
| 2 | Re-run this script on **6/30 NPORT data** once filed (~late Aug) for a genuinely post-deck independent reading | ~late Aug |
| 3 | Watch for **any new AGF syndication** — issuance collapsed to **$2.0B in Q1'26** vs $13.4B FY2025, ~9–10mo since the last public syndication. **A pulled deal is an escalation trigger; a successful one at a normal spread is the strongest available refutation of kill-path-1.** | ongoing |

---

## 7. NUMBERS DISCIPLINE

- ✅ **Carry:** *"Athene FABN peer penalty ≈ **+40bp** (within-fund paired, n=15 funds, 11/15 positive, IQR −1 to +52), NPORT-P holder marks 3/31–5/31/26, SHADE-constructed peer set — independently corroborating the deck's +43–48bp."*
- ⚠️ **Do NOT cite the 6–11y figure** — one CUSIP.
- ⚠️ **Do NOT present this as a refresh** — it straddles the deck's own observation date.
- ⚠️ **Do NOT carry "the penalty is widening"** — one independent dataset fails to confirm it; unestablished pending 8/4.
- ⚠️ **Do NOT compare my Athene LEVEL to the deck's level** — different peer sets and marks-vs-prints. Compare penalties only.
