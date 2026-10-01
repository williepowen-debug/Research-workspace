# HANS lane-query noise sizing (WQ-295, PROME's 9/25 ask: WALTER sizes, PROME lands) · run 2026-10-01T16:32:33Z

Proposal: `PROME/inbox/2026-10-01_from-HANS_L549-drain-WQ317-T10-exit.md` §4 (commit 39d358842). Method: Google News RSS (en-US), each query as written, with and without `when:7d`; titles + pubDate ages; WALTER read every 7-day headline. RSS caps at 100 items.

## 1. All three need `when:7d` (RESEARCH-INTAKE's URL builder sends no recency limit; see newsweep_config.py L33-34)
| Query | No recency: items · median age · >7d old | +when:7d: items |
|---|---|---|
| ① | 61 · 84d (max 5,559d) · 40 | 20 |
| ② | 100 · 21d · 85 | 45 |
| ③ | 100 · 107d · 98 | 7 |

## 2. Per-query read (7-day sample)
- **① `"OAT Bund spread" OR "French bond yields" OR "BTP Bund spread"`: 20/week, ~15 on-subject** (ANSA BTP-Bund closes, French yields at a 2002 high, OAT/Bund >120). Off-subject: qz US Treasuries, an India rates piece, a Goldman euro-stocks note, two BBN CAC/FTSE market recaps. **Low noise. Adopt with `when:7d`.**
- **② `"ECB" rate decision OR Lagarde OR "deposit rate"`: 45/week, ~36 on-subject.** Off-subject: RBA hike, HSBC Malta mortgages ×2 ("deposit rate"/"interest rate"), Montenegro ×2, Bulgaria, ECB tech-funding data, a DAX forecast. **Moderate volume, ~20% noise.** `"deposit rate"` unanchored is the main leak.
- **③ `"TTF" gas price OR "EU gas storage" OR "gilt yields"`: ⛔ BROKEN AS WRITTEN. 7/week, and none on gilts or EU storage.** The unquoted `gas price` binds as AND to `"TTF"`, so the other two legs never fetch. Same-minute legs measured alone: `"gilt yields"` **63**/week (incl. Reuters "UK 30-year gilt yields top 6% for the first time since 1998") · `"EU gas storage"` **21** · `"TTF" gas price` **8** (≥3 of them TradingView "Trade Ideas" contract pages = spam) · rewritten `"TTF" OR "EU gas storage" OR "gilt yields"` = **72**.

## 3. Recommendation (PROME lands; HANS adopts or declines by name)
- ① as written + `when:7d`.
- ② quote the ECB leg and anchor the deposit-rate leg, e.g. `("ECB" OR Lagarde) ("rate decision" OR "deposit rate" OR "rate hike") when:7d`. **Not re-measured.**
- ③ split it, or quote every leg: `"TTF" OR "EU gas storage" OR "gilt yields" when:7d` (72/week, measured). Expect TradingView TTF contract-page noise.
- Limits: one 7-day window, one sample time (~16:2xZ 10/01); on-subject counts are WALTER's read, not a matcher.
