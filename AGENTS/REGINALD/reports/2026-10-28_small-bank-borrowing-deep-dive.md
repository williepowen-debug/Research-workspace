# Small-bank borrowing — deep dive (Will-asked, 2026-10-28 22:44 ET)

**Question:** what is the small-bank borrowing trend, and does it matter?
**Data:** Fed H.8 weekly via FRED, latest week ending Wed 10/14 (released Fri 10/23), retrieved 2026-10-28 22:45 ET. Series: `H8B3094NSMA` borrowings SA, `H8B3094NSMD` NSA, `H8B3094NLGA` large-bank borrowings, `DPSSCBW027SBOG` deposits, `CASSCBW027SBOG` cash, `TLASCBW027SBOG` total assets, `LLBSCBW027SBOG` loans, and the loan-category series listed in §4. Discount window: `WLCFLPCL` (Wednesday level). Rates: `SOFR`, `IORB`, `DPCREDIT`. KRE/SPY are yfinance adjusted closes, with today excluded. Scripts, data and raw outputs: `domain/sources/2026-10-28_boot/h8_deepdive/`.
**"Small" in H.8** means domestically chartered banks outside the 25 largest by assets. That covers most regional and community banks, not only tiny ones.

## Bottom line

Small banks have borrowed fast but from a low base, and the money mostly went into new loans rather than into cash. The aggregate borrowing level is still lower relative to assets than it was before COVID or through 2023–24. Deposits are rising, which is the opposite of the 2022 pattern that preceded SVB. My Q3 cohort names mostly cut borrowing, so the borrowers are banks I don't cover. A forward test since 2006 shows **no forward edge** for KRE. **Descriptive, not a signal: no threshold, no registration, no trade.** The decisive data is per-bank borrowed money in the 9/30 Call Reports (the scheduled 11/07 pull).

## §1 Level vs speed

| Measure | Now [w/e 10/14] | Context |
|---|---|---|
| Level | **$316.4B** SA | 2026 trough $278.4B [7/15]; 2024 peak $416.6B [1/31/24]; SVB week $666.1B [3/15/23] |
| As % of small-bank assets | **4.55%** | **18th percentile since 2010** (median 6.38%); pre-COVID 6.23% [12/2019]; 6.51% [3/2024] |
| 1-week change | +2.9% (+$9.0B) | 96th percentile of weeks since 2010 |
| 3-week | +6.0% (+$17.9B) | 97th percentile |
| **6-week** | **+11.8% (+$33.5B)** | **97.5th percentile since 2010; 18th largest of 876 weeks excluding the SVB weeks** |
| 13-week | +13.7% (+$38.0B) | 94th percentile |

**Read:** a fast move from a low base. The level is not stretched.

## §2 What funded what

| $B, SA | 9/2 → 10/14 (6 wks) | 7/15 → 10/14 (since trough) |
|---|---|---|
| Borrowings | **+33.5** | **+38.0** |
| Deposits | **+39.4** | +33.2 |
| Cash assets | +13.7 | +4.1 |
| Loans and leases | **+47.6** (≈ +37.9 excluding the card step, §4) | **+71.3** |
| Securities | −3.1 | −16.4 |
| Large-bank borrowings (contrast) | +36.0 (+3.5%) | −17.8 (−1.6%) |

**Read:** borrowing and deposit growth together funded loan growth of about 1% in six weeks, roughly 8–9% annualized. Cash rose far less than borrowing. Large banks borrowed a similar dollar amount over the six weeks, but at a third of the percentage pace, and they are lower than in July. In percentage terms, the run belongs to the smaller banks.

## §3 Week-by-week (SA $B)

| Week | Borrowings | Deposits | Cash | Loans |
|---|---|---|---|---|
| 9/02 | 282.9 | 5,656.0 | 480.5 | 4,725.0 |
| 9/09 | 281.8 | 5,674.5 | 482.7 | 4,738.7 |
| 9/16 | 286.4 | 5,668.8 | 472.9 | 4,749.0 |
| 9/23 | 298.5 | 5,671.8 | 485.4 | 4,755.7 |
| 9/30 | 314.8 | 5,674.6 | 500.4 | 4,754.8 |
| 10/07 | 307.3 | 5,688.4 | 482.1 | 4,770.4 |
| 10/14 | 316.4 | 5,695.4 | 494.2 | 4,772.6 |

The 10/14 week's cash rise (+12.1) refilled cash spent the week before. In the 10/7 week, cash fell 18.3 while loans rose 15.6, including the card step.

## §4 Which loans

Six-week change 9/2 → 10/14, SA $B: commercial real estate (nonfarm nonresidential) **+9.7** · construction +1.6 · C&I **+7.2** · loans to nondepository financial institutions **+6.7** · residential +1.0 · HELOC +1.4 · autos +1.8 · **credit cards +9.4**.

⚠️ **Credit cards: a one-week step of +$9.7B between 9/30 and 10/7** (93.8 → 103.5 SA; 94.0 → 102.9 NSA), with large banks flat that week. This is a portfolio purchase or transfer onto a small bank at the quarter turn, not organic lending. H.8 does not name the bank, and this desk does not know who it is. It may matter for the BaaS perimeter if it is a fintech card book moving onto a sponsor charter. That is UNKNOWN and not asserted.

## §5 Discount window and the money-market explanation

- Primary credit $9.169B [Wed 10/21], down from a peak of $11.04B [10/14]. **98th percentile since 2010 when COVID 2020 and 2023 are excluded.** It is small: about 3% of small-bank borrowings, and borrowers are not named (both large and small banks can use it).
- The discount rate is 4.00%, only **5bp above SOFR** (3.95% [10/27]). Using the window costs little, which lowers the bar to use it.
- **The money-market explanation does not fit the timing.** Repo was **below** the Fed's reserve rate (IORB) in every week of the surge (weekly average −0.8 to −4.2bp, 9/16–10/21). It turned positive only in the week of 10/28, after the surge. Since 2024, the 6-week change in SOFR−IORB and the 6-week change in borrowing have correlation −0.04: no relationship. The level of SOFR−IORB vs primary credit: correlation 0.47, moderate.

## §6 My cohort's own Q3 borrowing (period-end 9/30 releases)

| Bank | Q3 borrowing | Source |
|---|---|---|
| WAL | total borrowing **−9.99%** | `reports/2026-10-20_reported-bank-earnings-catchup.md` (WAL funding grade) |
| ZION | short-term borrowing $1,219M → **$84M** | same report |
| SBCF | FHLB + other average $915.0M → **$862.1M** | 8-K 10/27 (this session) |
| AMTB | FHLB $715.0M, +1.8% | `reports/2026-10-23_boot/REPORT.md` |
| CUBI | FHLB $2.137B, +3.8% | same |
| CFG (a large bank, for contrast) | period-end FHLB $5,763M → $7,613M | 10/20 report |

**Read:** among the cohort names that reported it, borrowing mostly fell or edged up. The ~$33B rise (9/9 → 9/30) is coming from banks I don't cover. Only the Call Reports name them.

## §7 Does it predict anything? (base rate, release lag built in)

Episodes are the first week of each cluster where the 6-week rise met the bar, clusters are at least 26 weeks apart, and the sample starts mid-2006. Entry is the first KRE close on or after the H.8 release (week end + 9 days). "Excess" is KRE return minus SPY return.

| Bar | n (prior) | Episodes | KRE − SPY at 3 months |
|---|---|---|---|
| ≥ +11.8% (today's pace) | 2 | 2020-03 (COVID), 2022-06 | −1.8, +6.2 |
| ≥ +8% | 5 | 2007-10, 2012-03, 2017-10, 2020-03, 2022-06 | −14.7, −4.4, +2.0, −10.2, +7.1 (median −4.4; 3 of 5 negative) |
| Unconditional | 994 weekly samples | — | median −1.6; 58% negative |

**No forward edge:** 3 of 5 (60%) against a base of 58%, on n = 5. This agrees with TERRY's 10/23 finding that the proposed alarms show no edge since 2006.

**The two analogs worth knowing:**
- **2007-10:** borrowing was 16% of assets, about 3.5× today. Not comparable on level.
- **2022-06:** a low level like today (3.6%), but **deposits were flat to falling** (−0.4% over the next 13 weeks), and borrowing kept climbing (+23% over 13 weeks) to replace them. That cluster ran into SVB in March 2023. **Today deposits are rising (+0.7% in 6 weeks).** This is the main difference from the one analog that ended badly.

## §8 Correction to my own earlier read (same evening)

At boot I wrote that this was **"cash-building, not a run or a credit draw"**, based on one week (10/7 → 10/14). Over the whole run that is wrong. Cash rose +$13.7B against +$33.5B of borrowing, and the money went mainly into loans. The "not a run" half stands, because deposits are rising. Corrected on STATUS, the 10/28 boot report (appended), KB (ML-REG-256) and the NEXUS brief.

## §9 What would change this read

| Watch | Date | Which way it moves the read |
|---|---|---|
| ~~**H.8 weekly deposits**~~ *(RETRACTED 23:0x ET, §10: no track record)* | Fri 10/30, then weekly | ~~Deposits turning down while borrowing keeps rising = the 2022 pattern.~~ That would make this a funding-stress read, not a loan-funding read |
| **Call Reports 9/30, per-bank borrowed money and FHLB advances** | filing ~10/30; this desk's planned pull 11/07 | Concentrated in a few banks = idiosyncratic (find the names); broad = system-level funding of loan growth |
| FHLB Office of Finance Q3 Highlights | ~10/30 | FHLB share of the rise; REG-T-06's third quarter >$700B (grades 11/13 from the CFR) |
| H.4.1 discount window | Thu 10/29 | Whether ~$9–11B persists now that repo has moved above IORB |
| The card step | 10-Qs / 8-Ks | Which bank bought ~$9.7B of card loans and from whom (BaaS relevance) |

No threshold, prediction or position consequence. LIQUID owns the structural funding read; this is the bank-side description.


---

## Follow-up the same night (Will: "run 2 and 3, and set up 1"), 23:00–23:10 ET

### §10 Test 2: does "borrowing up, deposits down" have a track record? **No.**

The definitions were written into the script header before any outcome was computed (`domain/sources/2026-10-28_boot/h8_deepdive/test2_3.py`, sha256 prefix `ca159dd188093c53`; output `test2_3_out.txt`).
- DANGER pattern: 6-week borrowing ≥ +5% with 6-week deposits ≤ 0.
- HEALTHY: the same borrowing rise with deposits > 0.
- Episodes are clusters at least 182 days apart; release lag is 9 days.
- Outcomes: KRE − SPY at 3 and 6 months, and FDIC failures in the next 52 weeks.

| | Episodes since 1985 | KRE − SPY 3m (median) | Failures next 52 weeks (mean) |
|---|---|---|---|
| DANGER (≥ +5%) | 13 (5 with return data, 6 with failure data) | **+3.1** (2 of 5 negative) | **9.2** |
| HEALTHY (≥ +5%) | 20 | +1.1 | 26.1 |
| Unconditional | all weeks | −1.6 | 22.7 (6.4 excluding 2008–11) |

**Verdict (pre-registered): NO EVIDENCE OF A TRACK RECORD.** The returns leg and the failures leg were both NOT MET. The danger pattern was followed by better bank-stock returns and fewer failures than average. Small-bank aggregate deposits almost never fall much over 6 weeks (the largest drop in any danger episode was −0.6%). The 2023 failures were bank-specific runs at banks the H.8 classes as large, and they barely registered in the small-bank aggregate.

⇒ **RETRACTED:** §9's first row and this evening's chat told Will to watch weekly small-bank deposits as "the tell" for the 2022 pattern. That rested on one analog and fails the test. The aggregate cannot see bank-specific runs. **The instrument that can is the per-bank screen (§13).**

Current state: B6 +11.8%, D6 +0.7% at 10/14, i.e. HEALTHY. But at 9/30 the 6-week deposit change was +0.0%, classified HEALTHY by a hair.

### §11 Test 3: what kind of deposits? Mostly ordinary customer money.

| Small banks, SA $B | 9/2 → 10/14 | 7/15 → 10/14 |
|---|---|---|
| Deposits | +39.3 | +33.2 |
| Large time deposits (≥$100K CDs, rate-sensitive) | +10.2 (+1.4%) | +7.8 (+1.1%) |
| Other deposits (core) | **+29.1 (+0.6%)** | **+25.3 (+0.5%)** |

About three-quarters of the gain is core money. Core growth sits at the 44th percentile of 6-week moves since 2009, which is ordinary. The large-CD share is 13.07% (64th percentile since 2009; 2021 low 6.71%, 2023–24 high 14.15%).

In the 2022–23 run-up, banks paid up for CDs while core money left: 6-week large-time growth reached +12.0% with core −0.35% to −0.86%. That is not happening now. ⚠️ Brokered deposits are not visible in the H.8; the Call Reports (`BRO`) show them.

### §12 Seasonal check (found while reconciling)

Raw (NSA) small-bank borrowing on 9/30 ($306.5B) was only **+$4.3B (+1.4%) above 7/1 ($302.3B)**. The summer dip is normal. The 2010–2025 median Q3 raw change is −3.5%, so 2026 sits about 5 points (roughly $15B) above a normal quarter.

What is unusual is the **late-September rebound: +10.4% from the 9/9 low to quarter-end, against a 2010–2025 median of ~0%**. Only 2022 (+12.4%) was larger. The SA ranking in §1 stands. The Call Reports, however, will show a small aggregate change.

### §13 Set-up of the per-bank screen (Will's item 1)

- Rule FROZEN: `reports/2026-10-28_borrowing-screen_FROZEN_rule.md`, sha256 `90e0a4a23490d1a40702c207c50e92272c6f5d708001e3cb158cd6140e12948a`.
- Script: `scripts/borrowing_screen.py` (FDIC BankFind, public, no login, so the 11/05 FFIEC token expiry does not block it).
- Dry run Q1 → Q2 2026 reconciles with the H.8 (screen +$22.5B vs H.8 NSA +$19.2B) and reproduces filing figures (Amerant, OZK).
- The graded Q3 run waits for the FDIC posting, estimated mid/late November. The script refuses a partial posting.

### §14 Early Q3 short-list pull, FFIEC Call Reports (Will: "pull the short list before the login expires"), 23:12–23:20 ET

`scripts/borrowing_shortlist_ffiec.py`; output `domain/sources/2026-10-28_boot/borrowing_shortlist/borrowing_shortlist_Q3.md`.
- **List:** 139 banks: the 14 cohort banks, the Q2 dry run's 47 flags and 20 largest increases, plus the 100 largest small commercial banks. The last group is a coverage extension that lifts the list from 29% to **75%** of Q2 small-bank borrowings.
- **Field codes** were verified against the FDIC for Amerant and Western Alliance. **Route check passed:** all 14 cohort banks' 6/30 FFIEC figures equal the FDIC's exactly, including the foreign-office (031) filers.

**Filed by 23:15 ET 10/28: 28 of 139** (reports are due 10/30). Those 28 cut borrowing **−$4.27B net** while adding **+$5.81B** of deposits. Two banks meet the frozen flag:

| Flagged bank | Borrowing 6/30 → 9/30 | Deposits | Read |
|---|---|---|---|
| **Simmons Bank** (SFNC, AR, $24.0B; also flagged in Q2) | $1.27B → $1.75B (+$478M) | −$1,082M | **Explained at the issuer: a funding swap, not a run.** Q3 release (8-K acc 0001193125-26-422936, EX-99.1, deposit table): brokered $1,813M → **$935M (−$878M)**, time −$126M, noninterest-bearing −$64M. Ordinary deposits about −1%. Management: "reduction in the utilization of brokered deposits given pricing relative to FHLB advances"; cost of deposits −8bp to 1.85%. Separate 9/3 8-K (Item 2.05): 26 branch closures, $20–23M cost, efficiency program. Side notes: NCO 27bp (20bp in Q2); loans/deposits 94% |
| Israel Discount Bank of NY (private subsidiary) | $0.18B → $0.45B | −$168M | Not listed, so no trade route. Context only |

**111 PENDING** (not yet filed), including all the cohort except Valley. Re-run once filings land, **between Sat 10/31 and Wed 11/04, before the FFIEC token expires 11/05**: `.venv/bin/python3 AGENTS/REGINALD/scripts/borrowing_shortlist_ffiec.py --out AGENTS/REGINALD/domain/sources/2026-10-28_boot/borrowing_shortlist`. Cached pulls are not re-fetched. The full-universe concentration verdict still needs the FDIC posting (§13).
