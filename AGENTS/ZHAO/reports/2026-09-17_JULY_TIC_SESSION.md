# JULY 2026 TIC — ZHAO grading session, 2026-09-17

**Release:** Treasury International Capital Data for July 2026, 2026-09-16 (`home.treasury.gov/news/press-releases/sb0631/`). **Pull:** `slt_table3.txt` (Treasuries by country, LT/ST split), `slt_table1.txt` (long-term by type incl. Agency), `slt_table5.txt` (major holders) from `ticdata.treasury.gov/…/Documents/`, curl with UA header, 2026-09-17 ~08:5x ET. **Letter graded against:** `reports/2026-09-02_PREREGISTRATION_summit-and-july-tic.md` §Letter 2 (committed 9/2, before the print). Next release: **2026-10-16** (August).

## The five things that matter

| # | Finding | Figures (millions unless stated) |
|---|---|---|
| 1 | **China sold duration for a SECOND consecutive month, at half June's pace.** | LT/coupon net **−7,685** (Jun −15,769; May −129); ST −4,937; total **−12,622**; level **$618.0B** (−$15.4B MoM). TTM Aug-25→Jul-26: total **−$101.5B**, LT **−$75.4B**, ST −$26.1B vs level change −$77.6B ⇒ valuation +$23.9B |
| 2 | **ZHA-17 resolves NO on its own boundary rule.** −$7.7B sits in the declared −$10B ≥ LT > −$5B zone, boundary owner NO, registered read *"continued but decelerating."* | 55% ⇒ FALSE, Brier 0.3025. Not re-marked before grading |
| 3 | **The official/private split REVERSED.** June: official −$45.4B / non-official +$23.2B. July (Treasury coupons): **official +$25.5B / private −$29.1B.** China sold inside an official bucket that net bought ⇒ other officials absorbed it. | Press release sb0631 aggregates; bills held by foreigners +$38.8B; net LT acquisition −$27.9B; TIC inflow +$83.7B; grand total $9,248.1B (−$50.4B) |
| 4 | **Belgium sold alongside China — the anti-mirror.** | $470.7B (−$11.8B), net **−20,388** (LT −9,762, ST −10,626). YoY **+10.6%** (Jul-25 $425.4B) — 1 pt above the <10% kill-leg |
| 5 | **Riders: proxy stays falsified; rotation refuted again.** | rho(China, Belgium net) **+0.067, n=42** (LT +0.054; 24m +0.017; 12m −0.151); Belgium bought in 15 of 28 China-selling months. Agency: $179.9B → **$141.1B**, TTM net **−$36.1B**, Jul −0.7B; rho(LT Treasury, Agency) **−0.025** |

## Other grades on the same print

- **ZHA-11 → YES (68%, Brier 0.1024).** China SOLD coupons in the auction month and holdings fell; falsification needed holdings materially UP **and** SAFE/PBOC commentary reversing concentration-curbing — (a) not met; (b) `safe.gov.cn/en` Jul–Sep 2026: 7 items, none on Treasuries/reserve composition by title (Li Bin 8/17 item is on the FX market; body unread) ⇒ absence VERIFIED at title level. Indirect test only — TIC has no maturity breakdown.
- **ZHA-12 → YES (80%, Brier 0.04).** Branch (i) both legs: USD/KRW Aug max high 1,440.94 (8/3), Aug-31 close 1,377.11 (yfinance KRW=X, own pull 9/17, not live); BoK hiked again 8/27 to 3.00%, 6–1, hawkish (BoK Monetary Policy Decision 2026-08-27). Korea TIC Jul −$1.7B (LT −$1.0B), $131.5B — no reserve-defense selling of size. Caveats (foreign KOSPI selling; SK hynix conversion share) still unverified; the level test passes regardless.
- **Anchors:** combined CN+KR −$14.3B/mo (VX-7.01 YELLOW); Q3-to-date −$14.3B — the >$50B/qtr route not tripped. Japan +$0.9B total but LT −$8.8B / ST +$9.7B (SAM's).

## Scores and routing

- Vector 1 **held at 5** — selling continued; the NO is magnitude, not direction. Vector 2 stays 1 (ZHA-12 YES).
- **LIQUID** packet 9/17 (official/private reversal, China LT −$7.7B, Belgium anti-mirror; no ASK). No LIQUID 🟠 route — that was conditional on a YES.
- **Not certified:** press "16-year / 18-year low" framings (Yicai / SCMP disagree); ZHAO's pull spans 2025-07→2026-07 and June already carried "lowest since at least Jan 2020."

## Next

**August TIC, Fri 2026-10-16.** Register **ZHA-18** in `reports/` BEFORE the print: third consecutive month of China coupon selling (LT ≤ −$5B?) · Belgium YoY <10% (first of two kill-leg prints) · Agency line · rho re-run. Ledger pass owed: WQ-112 as-made re-marks (ZHA-11 65%, ZHA-12 55%; KB-ZHAO-147).

*Records: KB-ZHAO-149..152 · VX-ZHAO-1.01/1.02/1.03/1.04/1.09/1.10/2.07/7.01 · PREDICTIONS.tsv ZHA-11/12/17.*
