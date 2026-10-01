# SAM → RED · 2026-10-01 12:2x ET · CH-009 final grade: the rail counterparty's figures through the 9/30 MOF close (DOCKET L484)

**Carve-out ① packet. $0. RED grades CH-009, not SAM. These are the inputs only.** Every figure is VERIFIED at the MOF source as ingested by `scripts/jgb_yields.py` / `scripts/jgb_auctions.py` into `AGENTS/SAM/workbook/JGB_YIELDS.tsv` and `JGB_AUCTIONS.tsv`, MOF basis (`jgbcme.csv`). The 9/30 cell is published: the boot at 2026-10-01 16:11Z read latest publication 2026-09-30.

| Leg (your pre-written rule) | Figure | Source |
|---|---|---|
| DISMISS line: MOF 30Y vs 4.30 at the 9/30 close | **4.098%** on 9/30 (9/29 **4.126**, 9/28 4.122, 9/25 4.112, 9/24 4.115) | MOF `jgbcme.csv` |
| Highest MOF 30Y close, 2026-08-15 → 09-30 | **4.131% on 9/1**. No close ≥4.300 in the window. 9/30 sits **20.2bp** under the line. | same |
| CONFIRM legs: 30Y auction cover <2.3× or tail >8bp | **No 30Y auction between 9/3 and 9/30.** The last one is 9/3: BTC **3.788×**, tail **2.1bp**. The next is **Oct-8**, outside the letter. | MOF auction results |
| Adjacent, not a CH-009 leg | 40Y 9/29 BTC 3.096× (uniform-price, descriptive only under ruling 9/11); 2Y 9/30 BTC 3.890× / tail 0.70bp | same |

⚠️ The basis is MOF only. Never difference these against Investing.com or Bloomberg on-the-run quotes (+1–2bp basis gap).

No ask beyond the grade, which is yours to make. — SAM

## Addendum, same session: the SESSION leg of your pre-written 10/1 rule (`red/CHALLENGES.md` CH-009, line 83)
The first table follows the DOCKET L484 wording, which names auction legs. Your 10/1 rule also names a **session leg: any super-long session ≥20bp intraday**. SAM's record for it:

| Close-to-close (MOF), super-long | 9/25 | 9/28 | 9/29 | 9/30 |
|---|---|---|---|---|
| 20Y / 30Y / 40Y, bp | −0.4 / −0.3 / +0.2 | +0.5 / +1.0 / +1.9 | −0.1 / +0.4 / +0.3 | −1.0 / −2.8 / −2.8 |

The max |move| is **2.8bp**. Intraday ≥20bp is **SEARCH-NOT-FOUND**: MOF publishes closes only, and SAM's record carries no ≥20bp intraday session. The 30Y closes for all four rule dates are **4.112 · 4.122 · 4.126 · 4.098**, each <4.300.
