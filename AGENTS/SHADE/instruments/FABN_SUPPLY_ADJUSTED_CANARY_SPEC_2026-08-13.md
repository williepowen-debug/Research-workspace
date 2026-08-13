# FABN Supply-Adjusted Canary — **PRE-REGISTERED SPEC** (companion instrument to kill-path-1)

**Owner:** SHADE · **Dated spec:** 2026-08-13 · **State:** REGISTERED, **NOT YET GRADED**
**Authority:** `PROME/proposals/2026-08-13_private-credit-batch-RULED.md` **③ — BUILD APPROVED** (Will, in-session batch approval off PROME recs, 2026-08-13). Design source: `research/ATHENE_FUNDING_MIX_ENCUMBRANCE_SHIFT_2026-08-13.md` §3.

> 🔒 **COMPANION, NOT REPLACEMENT — ruled constraint, restated so it cannot be lost.**
> The existing price canary stands **untouched**: peer penalty **+33.0bp like-for-like** (8/13), kill-path-1 **YELLOW**, registered RED bar **>250bp or a pulled/failed syndication**. **This spec moves no band and no kill-line.** It adds a second reading that the price canary cannot produce; it does not overrule it, and **it cannot by itself move kill-path-1 to RED.**
> **This document pre-registers the instrument BEFORE its first graded reading.** No reading below is graded. The Q2-2026 figures appear only as the **frozen baseline**.

---

## 1. The defect this instrument exists to cover

**Kill-path-1's registered leading indicator is a price:** Athene's 5Y FABN secondary spread and its peer penalty. On 2026-08-13 that price read **tighter on both measures** — penalty +44.7bp → +33.0bp like-for-like, Athene T+123 → T+110.

**In the same six months, the quantity collapsed:** FABN gross issuance **$2.0B (Q1) → ~$1.2B (Q2)**, FABN outstanding **$34.6B → $33.9B**, and Athene disclosed *"a single $1B publicly syndicated FABN issuance since September 2025"* — an ~11-month public-syndication gap.

🔑 **A secondary spread is a price struck on a float. Withdrawing supply mechanically supports the price of what remains.** So a tightening FABN spread is equally consistent with:
- **(A) the market's view of Athene improved**, and
- **(B) Athene stopped feeding the market paper.**

**The price canary cannot separate (A) from (B).** That is an **identification defect**, not a calibration problem — no number of additional quarters of the same instrument fixes it. This companion measures the **quantity** leg so the pair is jointly identifiable.

---

## 2. Definition — the three components

All three are **quarterly**, all from **primary filings**, all **stock-and-flow on the same date**.

| # | Component | Definition | Primary source | Why it discriminates |
|---|---|---|---|---|
| **S1** | **FABN gross issuance, quarterly** | $B of FABN issuances in the quarter | ATH 10-Q / 10-K **MD&A**, institutional-channel paragraph (verbatim form: *"Funding agreement inflows for the … consisted of $X of FABN issuances, $Y of FABR issuances and $Z of FHLB issuances"*) | The direct supply measure. Falling S1 alongside a tightening spread is the (B) signature. |
| **S2** | **Unsecured share of funding-agreement stock** = FABN ÷ (FABN + FABR + direct FA + FHLB) | %, at quarter-end | ATH 10-Q Note *Commitments and Contingencies → Funding Agreements* **and** the MD&A outstanding sentence (both carry it; cross-check) | Substitution into collateralized channels. Falling S2 = the balance sheet is being encumbered to replace unsecured funding. |
| **S3** | **Public-syndication recency** = months since the last **publicly syndicated** FABN issuance | months (integer) | Athene quarterly **Fixed Income Investor Presentation** (Item-7.01 8-K + ir.athene.com); Athene states this directly | Distinguishes *"can't print"* from *"chose not to."* A tight secondary that has not been tested by a primary print in ~a year is an untested price. |

⚠️ **S1 must be taken from the MD&A, never from the inflows table.** The table's "Funding agreements" row is an **aggregate** (FABN + FABR + direct FA + FHLB + LT repo, per its own footnote) and is **not like-for-like** with FABN-only. *(2Q'26: aggregate $5,718M vs FABN ~$1.2B — a 4.8× category error if confused.)*

⚠️ **Quarterly S1 is DERIVED for Q2/Q4** — 10-Qs print six-month and nine-month cumulatives, so Q2 = 1H − Q1. Two 1-decimal series ⇒ **±$0.1B**. **Always label derived-vs-printed.** Validate every derivation against the printed aggregate inflow (the 2Q'26 derivation ties out: $1.2 + $4.6 + $0.0 ≈ $5.7B vs printed $5,718M).

---

## 3. 🔒 FROZEN BASELINE (Q2-2026) — recorded, **NOT graded**

| Component | 12/31/25 | 3/31/26 | **6/30/26** | Source |
|---|---|---|---|---|
| **S1** FABN gross issuance, quarter | — | **$2.0B** *(printed)* | **~$1.2B** *(derived, ±$0.1B)* | Q1 10-Q MD&A · Q2 10-Q MD&A (1H $3.2B − Q1 $2.0B) |
| FABN outstanding | $34.6B | $34.5B | **$33.9B** | Q1/Q2 10-Q Note 11 |
| FABR outstanding | $21.0B | $21.5B | **$26.0B** | ” |
| Direct FA outstanding | $6.1B | $6.1B | **$6.1B** | ” |
| FHLB outstanding | $23.3B | $28.2B | **$27.7B** | ” |
| **S2** unsecured share | **40.7%** | 38.2% | **36.2%** | derived from the four rows above |
| **S3** months since last public syndication | — | — | **~11** (last: Sept-2025) | Q2'26 FI deck, Athene's own words |

*(S2 arithmetic, 6/30/26: 33.9 ÷ (33.9+26.0+6.1+27.7) = 33.9 ÷ 93.7 = **36.2%**. 12/31/25: 34.6 ÷ 85.0 = **40.7%**.)*

**Trajectory over two quarters: S1 ↓, S2 ↓ 4.5pp, S3 ↑.** All three point the same way. **No verdict is attached to this — it is the baseline the first graded reading will be measured against.**

---

## 4. Cadence and first graded reading

- **Cadence: quarterly**, keyed to **two** instruments that do **not** arrive together:
  - **10-Q / 10-K** (S1, S2) — Q3-2026 expected **~2026-11-05 to 11-10** *(history: 11/10/25, 11/14/24)*.
  - **FI Investor Presentation** (S3) — furnished on its **own Item-7.01 cadence, NEVER on an earnings date (14-for-14)**, typically **3–8 days after** the 10-Q ⇒ expect **~2026-11-10 to 11-18**.
- ⇒ **A quarter's reading is INCOMPLETE until both have landed.** Grade S1/S2 at the 10-Q; hold S3 open; **the composite reading is only final once the deck publishes.** *(This is the 8/4 leg-1 defect encoded as a rule: pre-register against each instrument's own publication cadence, never against "earnings season.")*
- **FIRST GRADED READING: Q3-2026.** Not before. Q2-2026 above is baseline only.

---

## 5. 🔒 What this instrument CAN and CANNOT discriminate

**CAN:**
1. Separate **(A) credit improved** from **(B) supply withdrawn** *when the two legs diverge* — a tightening spread with **rising** S1 and **stable** S2 is (A); a tightening spread with **falling** S1 and **falling** S2 is (B). **This is the whole purpose.**
2. Detect **substitution into encumbered funding** (S2) as a continuous measure, rather than only at the registered RED bar's binary "pulled syndication."
3. Distinguish **"chose not to print"** from **"could not print"** — but **only weakly**, via S3 plus board authorization headroom. *(At 6/30/26 Athene held **$11.1B** of unused board authorization against a **$45.0B** ceiling — capacity was not the binding constraint.)*

**CANNOT — and these are limits, not to-do items:**
1. ❌ **Cannot establish rationing.** No disclosure gives the all-in cost of FABR/FHLB vs the FABN secondary. Absent that, "secured is cheaper" (optimization) and "unsecured is closed" (rationing) are **observationally equivalent on these three components.**
2. ❌ **Cannot size encumbrance.** FHLB requires over-collateralization and FABR is repo-backed, so both raise pledged assets — but **S2 is a liability-side share, not an asset-side encumbrance ratio.** **Never quote S2 as an encumbrance ratio.**
3. ❌ **Cannot separate Athene-specific from FABN-market-wide supply withdrawal.** If every FABN issuer cut issuance ~40% QoQ, S1's fall is a market fact, not an Athene fact. **Peer issuance is not disclosed anywhere SHADE can reach quarterly.** *(Partial mitigation only: the NPORT-P holder-side rebuild, `research/FABN_PEER_SPREAD_NPORT_2026-07-27.py`, ~4 min, ~60-day lag.)*
4. ❌ **Cannot move kill-path-1 to RED on its own.** The registered RED bar is unchanged and is **price/event-based** (>250bp **or** a pulled/failed syndication). **This companion informs; it does not fire.**
5. ❌ **S3 is issuer-narrated.** Athene states the syndication count in its own deck and frames it as *"disciplined."* **It is a self-reported quantity from an incentive-flagged source** — the same provenance caveat as the peer penalty, which is why S1/S2 (filing-sourced) carry the weight and S3 is corroborative only.

---

## 6. Reading procedure (mechanical, ~10 min/quarter)

1. **10-Q lands** → pull the MD&A institutional-channel sentence → record **S1** (mark printed vs derived) and the four outstanding balances → compute **S2**.
2. **Validate:** derived quarterly components must sum to the printed aggregate funding-agreement inflow (±$0.2B). **A failed tie-out voids the reading — do not report it.**
3. **FI deck lands** (3–8 days later) → record **S3** and the current peer penalty **like-for-like against the prior edition's peer set**. ⚠️ **Athene changes its own peer set** (LNC added in Q2'26, worth 3.0bp) — always compute both.
4. **Pair the readings** and place in §7. **Report the pair, never a single composite score** — the instrument's value is in the *divergence*, and a scalar would destroy exactly the information it was built to expose.
5. Append a `board_log.tsv` row **whether or not anything moved** (the 7/27 ARCC rule: an ungraded pre-registration is worthless).

## 7. Verdict pairs — how a reading is placed *(no bands, deliberately)*

| Spread leg | Quantity leg (S1/S2) | Reading |
|---|---|---|
| Tightening | S1 ↑, S2 stable/↑ | **(A) CREDIT IMPROVED** — the price canary's tightening is corroborated; kill-path-1 weakens on evidence. |
| Tightening | **S1 ↓, S2 ↓** | **(B) SUPPLY WITHDRAWN — the tightening is UNINFORMATIVE about credit.** The price canary should not be read as reassurance. **← where Q2-2026 sits, ungraded.** |
| Widening | S1 ↑, S2 stable | Genuine cost pressure with the market still open — the cleanest *adverse* reading. |
| Widening | S1 ↓, S2 ↓ | Cost pressure **and** withdrawal — the most adverse pair; check the RED bar's *pulled-syndication* limb directly. |

⚠️ **Deliberately no numeric bands in v1.** Per `finding_base_rate_the_threshold_before_building_it`, SHADE has **two** quarters of S1/S2 history — far too few to base-rate a threshold, and a band invented now would be back-fitted to the only data that exists. **Bands are registered only after ≥4 quarters, as a separate dated re-spec, and never after seeing the quarter they would grade.** Until then this instrument produces a **placed pair**, not a verdict.

---

## 8. Provenance and change control
- **Spec frozen 2026-08-13.** Any change is a **dated re-spec** preserving superseded text verbatim; never edited in place after a reading.
- **Approval:** batch approval, not individually argued — if a defect in the design *as approved* surfaces during use, **flag to PROME before encoding**, per the ruling's own rider.
- **Supersedes nothing.** The price canary and its RED bar are untouched.
