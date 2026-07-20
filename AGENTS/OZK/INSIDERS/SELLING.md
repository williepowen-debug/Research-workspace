# OZK — Insider Selling Tracker

**Last Updated:** 2026-07-06 (fresh API pull — 16 new Form 4s since Apr 12)
**Sources:** FDIC securities-filings API (`securitiesfilings.fdicconnect.fdic.gov/api/instdiscl/cert/110` — old efr.fdic.gov URL redirects here; fully scriptable, incl. attachment PDFs. See MEMORY Findings 7/6), GuruFocus, INSIDER_ACTIVITY_COMPILED.md, INSIDER_SCAN_OZK.md
**Data Gap Fixed:** OZK dissolved its holding company in 2017 and files Form 3/4/5 with the FDIC (cert #110), not SEC EDGAR. Standard insider tracking tools (OpenInsider, Fintel, etc.) miss OZK entirely. FDIC EFR is the authoritative source.
**Score:** 🔴 FULL CONVERGENCE (Score 13) — All C-suite sells, zero buys; **pattern EXTENDED at 7/6 pull: CRO 2nd discretionary sale, Kenny 3rd-straight grant flip, zero buying continues.**
**7/20 verification stamp (LABOR re-run, `AGENTS/LABOR/outbox/2026-07-20_to-PROME_insider-rerun.md`):** Score-13 pattern **INTACT but NOT further extended** — **0 new filings since 7/1**, zero buying. Pre-Q2 window closed ~7/7 (quiet, as expected). Next own-pull after the 7/21 print.

---

## Form 4 Activity Log

### 🆕 Q2 2026 UPDATE (pulled 2026-07-06 — activity Apr 12 → Jul 6)

| Txn Date | Insider | Action | Shares | Price | Post-txn | Read |
|---|---|---|---|---|---|---|
| **2026-05-20** | **Majumdar (CRO)** | **SELL** | **827** | **$48.07** | 2,639 | 🔴 **2nd discretionary sale** (Feb 24: 419 = 10.78%; now 827 ≈ 24% of remaining). CRO cumulatively ~32% lighter since Feb. Not in the 5/18 grant batch — this is not grant-flipping; continued de-risking by the bank's risk officer into the pre-Q2/IQHQ window. |
| **2026-05-22** | Dir. Kenny | SELL | 1,500 | $47.81 | 7,621 | 🟠 **3rd consecutive annual grant flip** — received 2,113 on 5/18, sold 1,500 (71%) within 4 days (2024: 86% in 7d; 2025: 38% in 5wk). Comp-as-paycheck pattern intact. |
| **2026-06-12** | Helen W. Brown (officer) | SELL — 401(k) intra-plan transfer OUT of OZK stock | 4,317 | $52.12 | 2,791 (line) | 🟠 Discretionary (Rule 16b-3(f) exempt), executed **at the June high** ($52.12; OZK closed $52.09 on 6/30 before the 7/2 −5.7% drop). Well-timed exit within the plan. |
| **2026-04-28** | Dir. East | SELL | 1,000 | n/d | 147,724 (+1,400 ind. +20,389 pref.) | 🟡 ~0.7% of holdings — low signal. |
| 2026-05-18 | 12 directors/officers | GRANT | 2,113 each | $0 | — | Routine annual equity grant (2019 Omnibus Plan) after the 5/18 annual meeting (vote-results 8-K 5/19). Not a signal — except as feedstock for Kenny's flip. Recipients: N. Brown, Cholmondeley, East, Fabrega, Franklin, Gearhart, Kenny, Koefoed, Musico, Orndorff, Sadoff, Whipple. |

**Zero insider buying continues** through Jul 6. **Gleason still frozen** — no Form 4 since Jul 2023.

---

### CRO Majumdar — 🔴 STRONGEST SIGNAL

| Field | Detail |
|-------|--------|
| **Name** | Majumdar (CRO) |
| **Title** | Chief Risk Officer |
| **Date** | 2026-02-24 |
| **Action** | SELL |
| **Shares** | 419 |
| **Price** | Not disclosed (est. ~$42-44 range) |
| **% of Holdings** | 10.78% |
| **10b5-1 Plan** | **NO** — fully discretionary |
| **Context** | Same quarter bank cut ACL by $56.6M while noncurrent doubled. 75% of noncurrent concentrated in other nonfarm nonresidential CRE. The risk officer reducing personal exposure without automatic plan cover, while managing the bank's credit risk function. |

**Assessment:** Strongest single insider signal in the screen. Discretionary CRO sell during reserve cuts = maximum signal per scoring framework.

**🆕 UPDATE 7/6:** Majumdar sold AGAIN — 827 shares @ $48.07 on 2026-05-20 (≈24% of remaining; post-txn 2,639). Two discretionary sales in three months, cumulative ~32% reduction since February, with the IQHQ RaDD maturity and Q2 print inside 90 days. Signal upgraded from "strongest single event" to **active pattern**.

---

### CFO Hicks — 🔴 MATERIAL, STAGED

| Field | Detail |
|-------|--------|
| **Name** | Hicks (CFO) |
| **Title** | Chief Financial Officer |
| **Date** | Oct 2024 + Jan 2025 (two tranches) |
| **Action** | SELL (staged) |
| **Shares** | Not specified (dollar value ~$944K total) |
| **Price** | Not specified |
| **% of Holdings** | ~22% |
| **10b5-1 Plan** | No automatic plan disclosed |
| **Context** | Staged selling across two quarters = deliberate reduction, not a single liquidity event. Occurred before Q4 2025 charge-off acceleration. |

**Assessment:** Two-tranche sell reducing 22% of holdings without 10b5-1 cover. Deliberate, material reduction.

---

### Director Whipple — 🔴 WELL-TIMED EXIT

| Field | Detail |
|-------|--------|
| **Name** | Whipple (Director) |
| **Title** | Director |
| **Date** | Not specified (pre-decline) |
| **Action** | SELL |
| **Shares** | Not specified (dollar value $5.2M) |
| **Price** | $51.50 |
| **% of Holdings** | Not specified |
| **10b5-1 Plan** | Not specified |
| **Context** | Sold near 52-week high. Stock subsequently fell to ~$42-44 (near 52-week low). Timing proved correct — ~18-20% decline since sale. |

**Assessment:** $5.2M exit near the top. Whether planned or discretionary, the timing speaks.

---

### CEO Gleason — 🟡 CAPTIVE, NOT CONFIDENT

| Field | Detail |
|-------|--------|
| **Name** | Gleason (CEO) |
| **Title** | Chairman & CEO |
| **Date** | N/A |
| **Action** | NO SELLING |
| **Shares** | N/A |
| **Price** | N/A |
| **% of Holdings** | ~10% (~$470M in a $4.7B company) |
| **10b5-1 Plan** | N/A |
| **Context** | Position too large to sell without moving the stock. Selling at this scale is itself a public signal and creates liquidity constraints. Non-selling is neutral — NOT bearish, NOT bullish. |

**Assessment (per Audit C4 correction):** Gleason's non-selling is uninformative due to liquidity constraints. The real signal is the *other* C-suite: CFO staged out $944K, CRO sold discretionarily, and nobody bought.

---

### Director Kenny — 🟠 SYSTEMATIC GRANT LIQUIDATION

| Field | Detail |
|-------|--------|
| **Name** | Peter C. Kenny |
| **Title** | Director |
| **Period** | May 2024 – Jan 2026 (full FDIC EFR history) |
| **Pattern** | Receives annual stock grants, sells within days/weeks. Net seller over 2 years. |
| **10b5-1 Plan** | Not disclosed. Jun 2025 filing notes "sold in multiple trades at prices ranging from $45.15 to $45.18" — actively worked order. |

**Full Transaction History (FDIC EFR, cert #110):**

| Date | Action | Shares | Price | Remaining | Note |
|------|--------|--------|-------|-----------|------|
| May 6, 2024 | GRANT (A) | +1,682 | $0 | 8,735 | 2019 Omnibus Equity Incentive Plan, vests May 2025 |
| May 13, 2024 | SELL (S) | -1,453 | $48.23 | 7,282 | Sold 86% of grant within 7 days |
| Oct 23, 2024 | SELL (S) | -1,000 | $43.48 | 6,282 | |
| May 5, 2025 | GRANT (A) | +2,043 | $0 | 8,325 | 2019 Omnibus Equity Incentive Plan, vests May 2026 |
| Jun 12, 2025 | SELL (S) | -782 | $45.16 | 7,543 | Multiple trades $45.15-$45.18 |
| Oct 23, 2025 | SELL (S) | -350 | $45.51 | 7,193 | |
| Jan 30, 2026 | SELL (S) | -185 | $47.54 | 7,008 | |
| **May 18, 2026** | GRANT (A) | +2,113 | $0 | 9,121 | 2019 Omnibus Plan annual grant |
| **May 22, 2026** | SELL (S) | -1,500 | $47.81 | 7,621 | **71% of grant sold within 4 days** |

**Totals (through 7/6/26):**
- Grants received: 5,838 shares ($0 cost)
- Shares sold: 5,270 shares (~$245K proceeds)
- Net: +568 shares vs pre-2024 baseline of 7,053 → current 7,621
- Three consecutive years of grant-flipping (86% in 7d / 38% in 5wk / 71% in 4d)

**Assessment:** Director treating equity compensation as cash paycheck. Every grant followed by immediate selling. Net position declined despite receiving ~$170K in free stock over 2 years. Zero open-market purchases. Not the behavior of a director who believes the stock is undervalued.

---

### President Hamblen — 🟠 LP STRUCTURE + SYSTEMATIC SELLING

| Field | Detail |
|-------|--------|
| **Name** | Paschall B. Hamblen |
| **Title** | President / COO |
| **Period** | Aug 2024 – Mar 2026 (5 FDIC EFR filings) |
| **Pattern** | Transferred 60K shares into Family LP (estate planning vehicle), then sold 6,000 shares from LP at $51-53 near highs. Position growth is 100% comp grants, zero open-market purchases. |
| **10b5-1 Plan** | Not disclosed. |

**Full Transaction History (FDIC EFR, cert #110):**

| Date | Code | Shares | Price | Direct | Indirect (LP) | Total | Note |
|------|------|--------|-------|--------|---------------|-------|------|
| Aug 2, 2024 | G (transfer) | -60,142 direct / +60,142 LP | — | 33,608 | 60,142 | 93,750 | Moved shares into Family LP |
| Jan 23, 2025 | S (sale) | -2,000 | $51.00 | 33,608 | 58,142 | 91,750 | Open market, via LP |
| Feb 5, 2025 | S (sale) | -2,000 | $52.00 | 33,608 | 56,142 | 89,750 | Open market, via LP |
| Feb 6, 2025 | S (sale) | -2,000 | $53.00 | 33,608 | 54,142 | 87,750 | Open market, via LP — 3 sales in 2 weeks at ascending prices |
| Mar 10, 2025 | A (grant) | +28,138 | $0 | 49,311 | 54,142 | 103,453 | Comp grant |
| Mar 10, 2025 | F (tax) | -12,435 | $44.41 | 49,311 | 54,142 | 103,453 | Mandatory tax withholding |
| Mar 10, 2026 | A (grant) | +52,232 | $0 | 91,131 | 54,142 | 145,273 | Comp grant |
| Mar 10, 2026 | F (tax) | -10,412 | $44.50 | 91,131 | 54,142 | 145,273 | Mandatory tax withholding |

**Totals:**
- Grants received (net of tax): +57,523 shares
- Voluntary open-market sales: -6,000 shares ($51-53, ~$312K proceeds)
- LP transfer: 60,142 shares restructured (not a sale, but sets up selling vehicle)
- Net: position grew from 93,750 → 145,273 on comp alone
- Open-market purchases: **ZERO**

**Assessment:** More sophisticated than Kenny — Hamblen uses an LP structure for tax-advantaged selling and retains most comp grants. But the signal is clear: sold 6,000 shares at $51-53 (OZK now ~$48), zero voluntary purchases ever. The LP setup (Aug 2024) was specifically a selling vehicle. Not the behavior of a President who believes earnings will surprise to the upside.

---

### Institutional Ownership — 🟠 SMART MONEY DIVERGENCE (13F, Dec 31, 2025)

**Pattern:** Fundamental credit analysts selling hard. Quant/trading firms adding. Index/passive roughly flat.

| Institution | Type | Shares (MM) | Δ Shares | Read |
|---|---|---|---|---|
| Wellington Mgmt | Fundamental/credit | 1.25 | **-42.89%** | 5-quarter trajectory: 4.22M→1.25M (-70.4%). Briefly re-entered Q2 2025 (+873K), immediately reversed with accelerating sells. Bounce-then-dump = reassessed and exited faster. |
| D.E. Shaw | Quant | 1.38 | **-26.06%** | Major quant reduction |
| AQR Capital | Quant | 1.58 | **-19.97%** | Elite quant cutting |
| Morgan Stanley | Bank/wealth | 1.47 | **-14.61%** | Sell-side pulling back |
| Wasatch Advisors | Active small/mid-cap | 6.95 | **-6.62%** | Bank specialist reducing; dropped below 5% threshold Jun 2025 (13G/A) |
| Jarislowsky Fraser | Active | 1.66 | -7.99% | |
| Citadel | Market maker | 1.27 | +259.52% | Likely hedging/arb, not conviction |
| Renaissance Tech | Pure quant | 0.87 | +35.71% | Statistical/mean-reversion |
| Millennium | Multi-strategy | 1.08 | +20.06% | Short horizon |
| State Street | Index | 6.56 | +9.10% | Mechanical |
| BlackRock | Index | 10.11 | +1.13% | Mechanical |

**Wellington Full Trajectory (WhaleWisdom, 13F only — no N-PORT data available):**

| Quarter | Shares | Δ Shares | Δ% | Read |
|---------|--------|----------|-----|------|
| Q3 2024 | 4,223,452 | +1,041,198 | +32.7% | Recent peak |
| Q4 2024 | 2,993,288 | -1,230,164 | -29.1% | Selling begins |
| Q1 2025 | 2,205,406 | -787,882 | -26.3% | Accelerating |
| Q2 2025 | 3,078,648 | +873,242 | +39.6% | Brief re-entry — tried to hold |
| Q3 2025 | 2,185,334 | -893,314 | -29.0% | Immediately reversed |
| Q4 2025 | 1,248,030 | -937,304 | -42.9% | Largest single-quarter cut. Peak-to-current: **-70.4%** |

**Note:** 13F data is as of Dec 31, 2025 (3.5 months old). N-PORT search attempted (EDGAR EFTS + WhaleWisdom) — Wellington's fund-level N-PORT filings do not appear in either source for OZK. No post-Dec 31 data available. No new 13D/13G filings in 2026 (no 5% threshold crossings). Wasatch published no commentary explaining their OZK reduction; OZK dropped entirely from Wasatch Core Growth Fund (was "strong position" in Q4 2023, absent by Q4 2025).

**Source:** 13F filings via institutional ownership page, WhaleWisdom position history, EDGAR 13D/13G search, Wasatch fund commentaries (Seeking Alpha, wasatchglobal.com)

---

### All Insiders — 🔴 ZERO BUYING

| Field | Detail |
|-------|--------|
| **Period** | 12 months through 2026-03-23 |
| **Action** | ZERO BUYS |
| **Context** | No insider stepped in during drawdown to 52-week lows (~$42-44). GuruFocus check (Mar 23, 2026): zero new transactions (buy or sell) in last 3 months. Pattern holds. |
| **Corporate Note** | OZK repurchased 2.25M shares in Q4 2025 at avg $44.45 "well below tangible book value" [KB-OZK-093]. This is corporate buyback with shareholder money, NOT personal insider buying via Form 4. Distinction matters. |

---

## Scoring Framework

| Signal | Weight | OZK Status |
|--------|--------|------------|
| CRO discretionary sell during reserve cuts | Strongest | 🔴 YES |
| CFO staged selling, no 10b5-1 | Strong | 🔴 YES |
| President LP structure + sales at highs | Moderate | 🟠 YES |
| Director Whipple well-timed large exit | Moderate | 🔴 YES |
| Director Kenny systematic grant liquidation | Moderate | 🟠 YES |
| Zero buying across 12 months during drawdown | Strong | 🔴 YES |
| CEO non-selling (captive) | Neutral | 🟡 Uninformative |

**Composite: 🔴 FULL CONVERGENCE (Score 13)**

---

## What Would Change the Score

- **Any insider purchase** at current levels (~$49-50) = material counter-signal, drops score significantly
- **10b5-1 plan disclosure** for Majumdar's Feb or May sale (if retroactively revealed) = downgrades from discretionary to planned
- **Gleason open-market purchase** = strongest possible counter-signal
- **New selling** = confirms trajectory but already at max convergence

---

## Pull Log

**2026-07-06 pull (API, cert #110):** 16 new Form 4s since Apr 12 — see 🆕 Q2 2026 UPDATE table above. Key: Majumdar 2nd sale (5/20), Kenny grant-flip #3 (5/22), Brown 401(k) transfer-out at $52.12 (6/12), East 1,000 (4/28), 12× routine annual grants (5/18). Zero buys. **Pre-Q2 insider window closes ~Jul 7** (14 days before Jul 21 earnings) — any late filings before the print would be notable.
**2026-07-20 (LABOR re-run, no own-pull):** Score-13 INTACT, **not further extended** — 0 new Form 4s since 7/1, zero buying. Pre-Q2 window closed ~7/7 quiet. Source: `AGENTS/LABOR/outbox/2026-07-20_to-PROME_insider-rerun.md`.
**Next:** Re-pull after Jul 21 earnings (one command: `curl -s -A "Mozilla/5.0" "https://securitiesfilings.fdicconnect.fdic.gov/api/instdiscl/cert/110"`).

**2026-04-12 pull (FDIC EFR, cert #110).** Full Form 4 history reviewed. Results:
- 18 Form 4 filings in 2026 YTD at that point (all sells or comp grants)
- Zero insider purchases
- Gleason: zero Form 4 filings going back to at least Jul 2023
- Mar 11, 2026 batch (10 filers): likely annual comp event — Hamblen, Hicks, Brown, Thomas, Wolfe, Carter, Cathey, Gotham, Orndorff, Taylor
- Pre-Q1-earnings window closed ~Apr 7. No buying detected.

---

*Compiled from: FDIC EFR (efr.fdic.gov, cert #110) | `../research/INSIDER_ACTIVITY_COMPILED.md` | `../sources/INSIDER_SCAN_OZK.md`*
*KB refs: KB-OZK-037, KB-OZK-038, KB-OZK-039, KB-OZK-040, KB-OZK-041, KB-OZK-093*
