# Morning regional-bank tape — October 12, 2026

**REGINALD conclusion:** broad buying within the maintained regional cohort, plus an additional OZK-specific relief move. The broad buying's causal driver remains unresolved. A green morning does not establish improved credit or reverse the three-month decline.

**Observation:** fresh Yahoo Finance/yfinance pull **11:16:38–11:16:40 EDT, October 12**; vendor regular-session timestamps shown below. All 14 banks and 6 equity ETFs identify the requested instruments, USD, marketState REGULAR. Prior-close fields match freshly fetched **Friday October 9** unadjusted daily closes for all 21 equity/bond ETFs and banks checked, within half a cent (same vendor, separate route; not an independent provider). Source data: `domain/sources/2026-10-12_morning-bank-tape/quotes.json` and `settled-history.json`.

**Delay caveat:** Yahoo declares 15 minutes for Nasdaq banks/QQQ and 20 minutes for NYSE banks, despite near-retrieval quote timestamps; ETF declarations KRE/SPY/KBE/XLF/IWM are zero. These are freshly retrieved vendor regular-session observations, not certified exchange-direct real-time prices. AMTB's last reported trade is 11:07:19, CUBI 11:13:06; the others are 11:16. Asynchronous/delayed observations constrain precise relative-move attribution. No Monday settled close exists at this read.

## Timestamped comparison

| Instrument | Oct 9 close $ | Oct 12 quote $ | Return vs close | Vendor quote time ET | Declared delay min |
|---|---:|---:|---:|---|---:|
| State Street SPDR S&P Regional Banking ETF (KRE) | 69.01 | 69.4650 | +0.66% | 11:16:38 | 0 |
| State Street SPDR S&P 500 ETF Trust (SPY) | 778.57 | 778.4199 | -0.02% | 11:16:38 | 0 |
| State Street SPDR S&P Bank ETF (KBE) | 63.13 | 63.4100 | +0.44% | 11:16:22 | 0 |
| State Street Financial Select Sector SPDR ETF (XLF) | 54.73 | 55.0750 | +0.63% | 11:16:36 | 0 |
| iShares Russell 2000 ETF (IWM) | 278.94 | 278.3800 | -0.20% | 11:16:33 | 0 |
| Invesco QQQ Trust (QQQ) | 751.27 | 746.6500 | -0.61% | 11:16:38 | 15 |
| Bank OZK (OZK) | 44.41 | 45.2800 | +1.96% | 11:16:24 | 15 |
| Western Alliance Bancorporation (WAL) | 74.27 | 75.0000 | +0.98% | 11:16:12 | 20 |
| Flagstar Bank, National Association (FLG) | 11.32 | 11.3300 | +0.09% | 11:16:32 | 20 |
| Eagle Bancorp, Inc. (EGBN) | 28.22 | 28.6600 | +1.56% | 11:16:01 | 15 |
| Citizens Financial Group, Inc. (CFG) | 63.57 | 64.1100 | +0.85% | 11:16:30 | 20 |
| Huntington Bancshares Incorporated (HBAN) | 15.32 | 15.3950 | +0.49% | 11:16:37 | 15 |
| Amerant Bancorp Inc. (AMTB) | 28.77 | 28.9250 | +0.54% | 11:07:19 | 20 |
| Valley National Bancorp (VLY) | 12.62 | 12.6800 | +0.48% | 11:16:07 | 15 |
| SouthState Bank Corporation (SSB) | 100.25 | 100.8025 | +0.55% | 11:16:13 | 20 |
| BankUnited, Inc. (BKU) | 42.28 | 42.3500 | +0.17% | 11:16:18 | 20 |
| Seacoast Banking Corporation of Florida (SBCF) | 31.74 | 31.9400 | +0.63% | 11:16:08 | 15 |
| Zions Bancorporation, National Association (ZION) | 62.49 | 62.8300 | +0.54% | 11:16:36 | 15 |
| M&T Bank Corporation (MTB) | 217.49 | 219.7650 | +1.05% | 11:16:33 | 20 |
| Customers Bancorp, Inc. (CUBI) | 74.04 | 74.9100 | +1.18% | 11:13:06 | 20 |

**Breadth (14 maintained names, not the population): 14 up, 0 down; median +0.59%, mean +0.79%.** Excluding OZK: 13/13 up, median +0.55%, mean +0.70%. Leaders OZK +1.96%, EGBN +1.56%, CUBI +1.18%, MTB +1.05%; smallest gains FLG +0.09%, BKU +0.17%. KRE leads SPY by **0.68 percentage points**, KBE by 0.22pp; OZK leads KRE by **1.30pp**. Thus one bank's announcement cannot explain away the breadth. KRE is an index portfolio; the 14-name equal-weight median is a different object.

## Three-month context from Will's chart

Will supplied a three-month/30-minute six-panel capture during this session, local reference `/mnt/c/Users/willi/OneDrive/Desktop/Regional Bank capture.JPG`. Headers show KRE 69.51 (+0.72%), WAL 75.00 (+0.98%), OZK 45.28 (+1.96%), ZION 62.87 (+0.60%), FLG 11.34 (+0.13%), EGBN 28.65 (+1.52%). Capture timestamp and feed delay are not displayed, so these corroborate the shape and nearby price levels, not a synchronized quote or broker execution. Cursor-selected OHLC rows describe selected 30-minute bars, not necessarily the latest quote. No position inferred from chart overlays.

Fresh settled history, **Jul 10 close → Oct 9 close** (a fixed approximate three-month window, not chart extrema; unadjusted price returns, excludes dividends):

| Instrument | Jul 10 → Oct 9 price return |
|---|---:|
| KRE | -8.01% |
| KBE | -8.17% |
| SPY | +3.13% |
| WAL | -7.96% |
| OZK | -12.35% |
| ZION | -11.56% |
| FLG | -24.98% |
| EGBN | +5.02% |

The declines persist on the adjusted-total-return comparison too (saved JSON). The morning bounce is inside a larger drawdown for KRE/WAL/OZK/ZION/FLG. **EGBN is the displayed exception: +5.02% over this fixed window**, even though its Q2 credit score remains elevated. AMTB +12.82% and SSB +0.57% are also positive in the full cohort's fixed window. That is counterevidence to treating the credit ranking as a price ranking; no score change follows from this observation.

## Drivers: established evidence versus hypotheses

| Candidate | Evidence and as-of | Verdict / counterevidence |
|---|---|---|
| Buying in banks/financials | KRE +0.66%, KBE +0.44%, XLF +0.63%, 14/14 names green at this pull; SPY −0.02%, IWM −0.20%, QQQ −0.61% | VERIFIED relative performance. Bank/financial buying or rotation is a supported description; the underlying flow or reason is INFERRED/UNKNOWN. Broad-market risk-on alone is a weak explanation when major benchmarks are flat/down |
| OZK RaDD relief | Issuer Oct 12 8-K Item 7.01 p.2: executed Oct 9 extension to Dec 2029, fresh $100M; OZK leads KRE by 1.30pp | Most concrete name-specific positive news. Consistent with incremental relief; exact share of the return attributable to it is unmeasured. Other 13 names green means it is not a sufficient sector explanation |
| Today's Treasury-rate relief | NYSE calendar allows normal equity trading; SIFMA recommends full US-dollar fixed-income close Oct 12. ^TNX has nominal 11:01:32 timestamp but flat O/H/L 5.2400002 and volume zero; TLT +0.04% | No verified current cash-yield change. A fresh timestamp on a flat holiday index does not authenticate Treasury trading. TLT is a traded ETF, not the cash curve; its near-flat move supplies little affirmative evidence for rate relief. No rates attribution made |
| Q3 earnings positioning | Citizens issuer Sep 10 notice: CFG Fri Oct 16, call 09:00 ET; Huntington issuer events page: HBAN Thu Oct 22 call 09:00 ET. Maintained issuer-verified calendar: WAL Oct 19 AMC, OZK Oct 20 AMC, EGBN Oct 21 AMC | Dates VERIFIED, anticipation as driver UNKNOWN. No current consensus-revision/buying-flow baseline retrieved for the cohort, so no claim of improving expectations or likely beats. WAL owner's Sep 28 benchmark was EPS $2.43–2.44, −7.2%/90d, dated historical rather than today's expectations |
| Squeeze / better credit | OZK owner's short-interest ~16.3% float refers to Sep 15, not today. Q2 credit/funding evidence is closed-quarter; no new cohort credit print in this review | Neither squeeze nor credit improvement established. No time-of-day-normalized volume/order-flow analysis or current covering measure. No all-clear inferred from green prices |

Calendar primaries read October 12: [NYSE](https://www.nyse.com/trade/hours-calendars), [SIFMA Sept 29 holiday notice](https://www.sifma.org/news/press-releases/sifma-fixed-income-market-close-recommendations-in-the-u-s-the-u-k-and-japan-for-u-s-columbus-day-and-japan-health-and-sports-day-holidays-2026). SIFMA is a recommendation; firms decide their own operation. Earnings primaries: [CFG](https://investor.citizensbank.com/about-us/newsroom/latest-news/2026/2026-09-10-210526622.aspx), [HBAN](https://ir.huntington.com/news-presentations/events-presentations). These announcements establish timing only.

## Research consequence and TERRY relevance

**The cohort research assessment stays concentrated on named banks, not tier-wide.** Today's tape does not supply a closed-quarter credit test. Funding counterevidence remains dated: H.8 small-bank borrowing +11.7% from the Sep 9 trough to Sep 30 (post-SVB 160-week window; Sep month-end change +5.9% NSA) and discount-window primary credit $9.97B Oct 7. Borrowers are unnamed; none is proof of a specific bank credit loss. Those existing reads resolve through H.4.1 Oct 15/H.8 Oct 16 and the registered Q3 frames.

**OZK's near-term maturity-failure premise weakens materially.** Completed owner research and its October 12 follow-up assignment were read, without repeating the owner investigation. Primary text was read in full from the owner-preserved FDIC 8-K, [FLNG 12019](https://securitiesfilings.fdicconnect.fdic.gov/api/instflng/12019/attachment/1): post-paydown **$579.1M funded + $335.9M unfunded = $915M commitment**. **$121.3M paydown may be readvanced; 68.4% LTV is September as-stabilized appraisal, not liquidation coverage; loan-specific recognized loss, contributor identity and capital's legal form remain UNKNOWN.** The issuer does not literally name RaDD/IQHQ; identification is the owner inference from largest-credit/commitment/location/bridge anchors. OZK-09 remains owner's OPEN/STUCK because the separate recognition leg is unknown, not because the extension is doubtful. Retained 45% scoring prior and old EL/scenario weights are pre-outcome records, not refreshed forecasts.

The Sept 26 REGINALD RaDD funded/unfunded inputs are now explicitly historical in the top3 report, loss bridge and dossier. No mechanical resizing of an old loss scenario from the new loan balance; the extension/redraw/capital structure changes its premise. Remaining OREO marks/other RESG/debt-on-debt risks still belong in existing Q3 tests.

**TERRY examination is warranted for the existing OZK Nov-20 $40P catalyst premise**, already routed by OZK and WALTER, with latest holding confirmation still broker/Will-owned. No duplicate card or trade instruction from REGINALD. This broad green morning supplies context to the existing conditional KRE card, not a new arm: `TRY-COND-KREADD` remains unarmed on this desk's legs. HBAN Oct-16 position rail remains the recorded sell-or-roll intent by Oct 14; no new broker fill received.

**Settled gates untouched:** WAL REG-T-02 remains FIRED, 0-of-3 exit through Oct 9; today's $75 is below both $78 and exit $81.90. FLG's ladder remains RED with 3 settled closes below RED through Oct 9; today's $11.33 remains below $11.39, and detector correctly excludes today's bar. KRE REG-T-01 remains UN-FIRED; today's quote is above $60. No new numerical score, gate, trade, monitor or observation assignment.

## Execution and coverage receipt

REGINALD, independently launched by Will; **OpenAI Codex / GPT-6 exposed, exact backend variant UNKNOWN**. Desktop **session/thread `01a130ac-dde6-76f1-8df7-eb903dc2862a`**, confirmed via CODEX_THREAD_ID and CODEX_SESSION_ID. Repo `/home/willi/Research-workspace`, canonical desk `AGENTS/REGINALD`, shared existing checkout. Explicit root CLAUDE/AGENTS/USER and desk CLAUDE boot/closeout/STATUS/LESSONS/CALENDAR/MEMORY/ROADMAP read; COMPLETION_SPEC/playbook Runtime mechanics/cross-session rules read. Quick tape mode used; full boot.py intentionally skipped under packet. No other desk launched.

Shell/Python/web/file/Git available. Sandbox DNS failed; approved network retry produced saved current prices. Installed `codex queue --help` verified transport; sandbox start failed read-only, approved same-command retry acknowledged boot identity notification to specified PROME thread `01a1307b-f614-76b3-8caf-49b226027079`, queue **01a130af-0221-7660-9a03-dcb83f5b2d12**. Notification acceptance is not consumption. Native `codex agents --no-alt-screen` browser showed one REGINALD task titled Execute bank tape review and one OZK task; runtime labels were inconsistent with ongoing work, so no absence/liveness inferred. No second REGINALD writer was discovered; cross-runtime completeness UNKNOWN. Direct PROME queue uses exact supplied ID.

Foreign BRENT/DAEDALUS/WALTER/OZK work present at boot: pull/stash/reset deferred; no foreign record edits. Ledger scan: 15 scanned, 4 scheduled quiet, no stale alert; 6 TSVs outside scan perimeter. Ladder retry confirms settled RED; local corrections check found one named SCF correction, read and receipted NO-OP because live bank surfaces did not carry withdrawn framing. Two WALTER info packets dispositioned; OZK packet integrated by annotations; WATT info read but its unrelated integration deferred to next owner touch under bounded scope.

**Limit:** one short morning snapshot, selected cohort, declared quote delays/asynchronous trades, same-vendor prior-close cross-check, no verified causal flow/rates/consensus-revision observation. Attribution remains unresolved beyond the identified OZK positive disclosure. Existing research resolvers and existing TERRY examination suffice; no new direction proposed.
