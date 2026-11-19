# November 18 close threshold look (walter-89, desktop, full closeout)

Vendor pull 2026-11-19T00:42:58Z (FORGE fetch.py): closes for equities and ETFs; ^VIX is the vendor's 11/18 close, not the Cboe settle and not FRED VIXCLS; futures are evening-session trades after the 17:00 ET day close, not settles (fetch withholds the move). FRED first-published re-pull for HY at 20:31Z (card 010). The Cboe VIX_History.csv returned a Cloudflare challenge page at about 00:43Z: blocked to automation, not retried, no workaround (root Data Hygiene). WALTER graded nothing.

| IDs | Observation / result |
|---|---|
| RED-FT-06 (fired-banked, exit >=18 s=5) | Closes at or above 18 on WALTER's read: VIXCLS 18.70 [11/12], 19.30 [11/13], 22.91 [11/16], 25.46 [11/17]; vendor ^VIX 24.56 [11/18 close] = **5 of 5 on WALTER's read, the exit condition is met if VIXCLS [11/18] posts at or above 18**. VIXCLS [11/18] not yet posted (FRED posts T+1). RED grades on VIXCLS. Card SIG-W-20261118-015. |
| RED-FT-02, REG-T-03, LIQUID WQ-444 | HY 343 [11/17] first-published; >320 x3 MET (LIQUID), card 010. |
| REG-T-04 (>350 x3) | 343 [11/17], 7 bp under: near-trigger watch. |
| REG-T-01/02 | KRE 70.52 (-0.47%), WAL 70.83 (-0.90%, under 78, existing cycle), ZION 63.69 [11/18 closes]. |
| Safety net VIX >30 or +5 | 24.56 vs 25.46: -0.90. Clear. |
| HANS-T-07 L3 exit (5 consecutive named-front closes under 90) | TTFZ26 vendor 84.75 [11/16], 85.40 [11/17], 81.11 [11/18] = 3 of 5 on WALTER's read (vendor bars, contract identity UNKNOWN; not ICE Endex settles). HANS grades. |
| RED-FT-03/04, boundaries 1/2/8 | BZF27 91.46 and CLF27 81.89 evening trades 19:33 ET, not settles; Brent identity UNKNOWN. Not gradeable. |
| Boundary 3 | Cushing 26.147M [w/e Nov 13] (card 008), not met. |
| Other | S&P 7,323.63 (-0.23%) [11/18 close], HYG 76.65. |

No new registered fire. One exit condition on WALTER's read pending its graded series (RED-FT-06). Written by 2026-11-19T00:43:22Z (date command).
