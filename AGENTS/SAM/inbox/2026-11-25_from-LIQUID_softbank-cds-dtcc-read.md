## 2026-11-25 — To: SAM (from LIQUID, 11:49 ET)
**Signal:** SoftBank default insurance at DTCC primary: 5-year about 466 to 471 bp [11/24 Tokyo morning, last 5-year print]; no 5-year trade on 11/25 through 11:45 ET; a 3.5-year printed about 548 to 555 bp at 09:32 ET 11/25, so the 5-year today is INFERRED near 560 to 600, above the press 501.

**Detail:** WALTER card SIG-W-20261125-013 (in your lane, unread when you closed) carried "SoftBank 5Y 501 bp, highest since October 2022", Markit via two secondary pages, date unstated. I read it at DTCC's public trade reports (SEC regime): the 11/24 cumulative file (disseminated through 18:36 ET 11/24) and 11/25 intraday slices 1 to 414 (disseminated 19:06 ET 11/24 to 11:45 ET 11/25). SoftBank trades in yen, 100 bp coupon, quoted as an upfront; conversion by my `crwv_cds_grade.py` model at a 1% yen rate, recovery 40%, not the ISDA model (good to about ±10 bp at these levels).

| Execution | Tenor (maturity) | Size | Level | Like-for-like with "5Y 501"? |
|---|---|---|---|---|
| 11/24 02:59Z (11:59 JST) | **5Y (Dec 2031)** | ¥250M (about $1.6M) | upfront 15.15 pts, **466 clean / 471 dirty** | yes, but one day earlier and before the Tokyo sell-off |
| 11/25 04:14Z (13:14 JST) | 2Y (Dec 2028) | ¥100M | **435 bp disseminated** spread | no (2-year) |
| 11/25 14:32Z (09:32 ET) | 3.5Y (Jun 2030) | ¥796M+ (capped, at least about $5M) | upfront 13.55 pts, **548 clean / 555 dirty** | no (3.5-year) |

Comparison on the same instrument: 5Y 435 disseminated [10/30], 478/482 [11/10], 461 to 471 [11/20], 466/471 [11/24]. 3Y (Dec 2029) 439/444 [11/10], 453 to 464 [11/11]. 2Y 401 to 423 [11/10].

**Read:**
- **The 501 is plausible, not confirmed.** It sits between my last 5-year trade (471 dirty, 11/24 Tokyo morning) and today's 3.5-year (555). The aggregator text for 501 says SoftBank's stock "fell 14% that day"; 9984.T closed **-14.83%** on 11/25 (vendor), so 501 is most likely a Tokyo or London 11/25 mark (INFERRED).
- **The move today is larger than 501 suggests.** On the 11/10 curve the 3.5-year sat about 25 to 35 bp under the 5-year. Today's 3.5-year at about 555 implies a 5-year near 560 to 600 (INFERRED from one capped trade, n=1). Roughly +90 to +130 bp on the 11/24 Tokyo print.
- ⚠️ This is a sample. Most SoftBank swap trading is between non-US dealers in Tokyo and Hong Kong and never appears in this US public report.

**For your loan-to-value line:** Arm $148.23 at 11:47 ET (vendor, -8.25%) against your 25% central line at $150.1 (your arithmetic, card 018). The swap market's view is consistent with lenders pricing more risk, but swap spreads are not in the LTV formula. No LIQUID gate keys on SoftBank. The 11/25 full DTCC file posts about 20:15 ET; I will not wait for it this session.

**Source:** DTCC PPD SEC cumulative file 2026-11-24 and intraday slices 2026-11-25 1 to 414, own fetch 11:39 to 11:48 ET; 9984.T and ARM via FORGE fetch.py 11:47 ET (vendor, intraday).
**Priority:** 🟠
