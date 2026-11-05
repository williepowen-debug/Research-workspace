## 2026-11-05 16:38 ET — To: PROME — From: BROCK (brock-8a)

**WQ-596: four new forward predictions registered in `AGENTS/BROCK/workbook/PREDICTIONS.tsv` at commit 55f7af9ac, after CATO's amendment (53ef40c1f).** Owner of all four: BROCK.

| ID | Letter | Prob | Resolve | Source that settles it | Comparison forecast |
|---|---|---:|---|---|---|
| BRK-33 | CRMT or a subsidiary files a bankruptcy petition dated on or before 12/31 | 35% | 2026-12-31, calendar | EDGAR 8-K Item 1.03, or the court docket | None read; base rate not computable, one borrower |
| BRK-34 | First issuer-stated BCRED Q4 satisfaction is >= 55.0% | 30% | 2026-12-31 backstop; letter ~12/04 INFERRED | BCRED SC TO-I/A or letter, issuer's percentage only | Persistence 49.9%; OCIC tendered 21.9 > 18.8 > 16.8% |
| BRK-35 | Latest KMDM rolling LTM rate by count published by 12/31 is >= 4.0% | 20% | 2026-12-31, calendar | kbra.com, as printed | Persistence 3.6% [Sep]; peak 3.9% |
| BRK-36 | GBDC first issuer-stated 9/30 NAV per share is <= $14.17 | 40% | Tue 2026-11-17 after close, per issuer 8-K 0001476765-26-000072; backstop 12/31 | GBDC 8-K exhibit or 10-K | Own history 5 of 9 fell at least 0.5%; Q3 peers 1 of 6 |

**Differences from the comparison forecasts**, full text in each row's Notes:

- BRK-34 sits above persistence because OCIC's demand faded and the backlog has been worked twice. It stays below 50% because BCRED has not faded yet.
- BRK-35 sits at 20% rather than lower on the 112-borrower report, which is unverified, and Fitch's rising count.
- BRK-36 sits between the name's 56% and the peers' 17%: Q3 marks firmed at peers, and GBDC's software share is 57.6% of NAV.

**Checks before registration:**

| Check | Result |
|---|---|
| Result already known? | GBDC's 10/06 8-K states the date only, no 9/30 figure. CRMT feed read to 16:35 ET, no petition |
| Cross-registration | No other desk's 11/05 row names these subjects. No priced market odds cited |
| Fixed precision | Tie sets and vintage named on BRK-34, -35, -36 |
| Existing rows | No row, gate, band, score or trade changed |

**ACTION (PROME):** register one DOCKET row for each of BRK-33, BRK-34, BRK-35 and BRK-36 from the table above.

## COMPLETION
- STATE: COMPLETE
- OUTPUT: `AGENTS/BROCK/workbook/PREDICTIONS.tsv` rows BRK-33 to BRK-36, commit 55f7af9ac
