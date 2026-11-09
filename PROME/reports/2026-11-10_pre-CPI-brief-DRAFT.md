# Pre-CPI brief, Tue 2026-11-10 — DRAFT (DOCKET L1086)

**State:** outline, built Sun 2026-11-08 15:1x ET by PROME prome-bf. Cells marked `[MON]` fill on Monday 11/9; the brief goes to Will in chat Monday after the HY cell (about 10:10 ET) and before the close. This file is the record; the chat version follows the operator-surface clause in root `CLAUDE.md`.

## 1. What prints Tuesday (ET)

| Time | Release | Owner row | Source of the time |
|---|---|---|---|
| 08:30 | October CPI (BLS) | HENRY L775 · CARL L797 (beef) · FERT T3 (food at home) | BLS schedule as quoted by cpichart.com and the BLS CPI page, search 2026-11-08: INFERRED (bls.gov itself returns 403 to this box; VIOLET logged the date as unconfirmed on 11/5) |
| 11:00 | NY Fed Household Debt and Credit, Q3 | CARL CRL-33 L1017 · NEXUS PRED-41 L575 | DOCKET rows; re-dated 11/6 |
| about 12:00 | USDA Crop Production (November) | FERT L761 | DOCKET row; time `[MON]` verify |
| 13:00 | 10-year Treasury auction (refunding leg 2) | BOND, registered grades on the 11/2 frozen bars | BOND STATUS line 101 |
| all day | China and US trade clocks: MOFCOM 公告70 suspension end, USTR ship-fee determination, Hanwha countermeasure clock | ZHAO L437 · L858 · L1088; L435 graded on the 11/10 record | ZHAO STATUS; BIS stay is to 1/10/2027, so the US entity perimeter does NOT widen on 11/10 |

## 2. What is expected

| Item | Figure | Basis |
|---|---|---|
| Core CPI m/m, October | +0.2% | HENRY's expectation and the Cleveland Fed nowcast +0.21 (10/29, HENRY HEN-57 letter); one press source (Seeking Alpha) gives the same consensus. Single-source consensus, not checked against a survey |
| September, for reference | headline +0.6% m/m, 3.7% y/y; core +0.3% m/m, 2.6% y/y | BLS release USDL-26-1574 (10/14) |
| Prediction-market modal | 86.0 on Polymarket, $3.3K liquidity, thin | ORACLE STATUS line 53; ORACLE owns priced odds; no Kalshi October event |
| December hike odds | 76% | HENRY own calc from fed funds futures, 11/6 15:00 ET; HEN-63 (hike at 12/9) 0.70 |

## 3. Registered calls that grade on the print (desk letters, not PROME's)

| Desk | Call | What fires it |
|---|---|---|
| HENRY | HEN-57, FROZEN 10/29 | core m/m first print 0.4 or higher = FIRED; 0.3 or lower = NOT FIRED; HENRY expects NOT FIRED at +0.2 |
| RED | FT-08 exit | only an October core of 0.0 or lower exits FT-08; CHG-RED-028 closes 11/10 on any verdict; RED re-derives its scenario weights after the print (Net-bear 68 at S57) |
| FERT | food-at-home transmission | the question dies if food at home m/m stays under +0.4% through the November print; September −0.07% |
| CARL | beef / screwworm watch L797 | screwworm not yet in prices (beef 512.606 September, off its July peak) |
| VIOLET | pre/post vol surface read | VIX9D above VIX into CPI (1.0601 on 11/6); a VIX close over 30 is on its change list |
| BOND | 10Y auction 4.5 hours after CPI | registered refunding grades |

## 4. The book against the print `[MON]`

Book line at draft time (`will_brief.py --book-line`, rc 0): $44,841.44, cash 62.93%, broker export 2026-11-05, marks 11/5 intraday, not live. Holdings by theme from `FORGE/STATUS.md` (mirror, not position truth): oil (USO shares and calls, VLO), gold (GLD), regional-bank and lender puts (OZK, WAL ×2, ZION, VLY, FLG), private-credit put (APO), the Robinhood UNG call, and the unfilled HYG card WQ-615. Monday: one line per theme on which way a hot or a cool core moves it, taken from the owner desk's own stated read, never PROME's inference; live marks pulled Monday.

## 5. HY spread cell for 11/6 `[MON about 10:10 ET]`

FRED publishes the ICE BofA HY OAS for 11/6 Monday morning. Consequences to state: WQ-513 (second HYG hedge) counts 1 of 3 closes only if the cell is above 3.50% (it was 3.48% on the last print); VIOLET's Path A size condition is HY at or over 368bp.

**FILLED Mon 11/9, 10:3x ET (PROME, desktop boot):** HY OAS **342 bp [11/6]**, −6 from 348 [11/5]; CCC **1,317 bp [11/6]**, −3. Source: PROME dashboard pull 2026-11-09 10:33:22 ET (first-published cell). Consequences, each by the owner's letter, none graded here:
- WQ-513 (HYG ×4): NOT FIRED, still 0 of 3 above 350.
- REG-T-04 (REGINALD, 350 ×3): 0 of 3.
- VIOLET Path A size (≥ 368): not met.
- WQ-615 HYG ×5 (GATE-TERRY-HYG-FOLLOW-01): T1 already FIRED on 348 [11/5] and stays fired. The card voids only on HY ≤ 330 for 5 consecutive closes before entry; 342 is not ≤ 330, so 0 of 5. TERRY read today as an entry day (HYG $77.42 +0.24% at 09:32 ET, commit 063e542caf), but its vendor quoted both option legs at 0.00/0.00, so only the broker chain can price the debit (≤ $0.60, max loss $306.50). No order is approved beyond the card; the order is Will's hand.
- HY > 320 run: continues. LIQUID's tier rule (BROADENS on one print) and its second-print read are LIQUID's to grade.
- So what: Friday's credit print eased instead of following Thursday's equity break through. The open question from HEARTBEAT, whether price deterioration has become a financing constraint, gets no support from this cell. One print; CPI Tuesday is the next test.

## 6. Known unknowns to carry into the chat version

- The CPI date and time are INFERRED from two secondary pages quoting BLS, not read at bls.gov.
- The +0.2% consensus is one press source plus the Cleveland nowcast; no survey figure was read.
- The prediction-market modal is a thin market ($3.3K).
- Book marks are three days old at draft time.

Sources (search 2026-11-08): https://cpichart.com/cpi-release-calendar/ · https://www.bls.gov/cpi/ · https://www.bls.gov/news.release/PDF/cpi.PDF · https://seekingalpha.com/article/4964304-october-cpi-inflation-is-likely-to-be-hot-but-focus-on-ai-bubble-burst
