# WQ-550 leg 1: Binance transmission, four reads (CYPHER, 2026-10-30)

**Session:** CYPHER, spawned by PROME (prome-c5) on Will's word 10:46 ET (*"ok go ahead"*; record `PROME/proposals/2026-10-30_wq550-binance-RULED.md`; DOCKET L878). Wall clock 10:50–11:1x ET. Incident row CYB-INC-055; first read `../2026-10-30_binance-first-read/RECORD.md`.
**Evidence beside this record:** `binance_network_status_2026-10-30T1451Z.txt` · `onchain_freeze_retally_2026-10-30T1454Z.txt` · `onchain_supply_2026-10-30T1454Z.txt` · `scripts/supply_and_balances.py` (re-run the freeze tally with `../2026-10-30_binance-first-read/scripts/freeze_tally.py <start_block>`).
**Fences kept:** no score moved (VX-CYP-02 grades at 11/02 only); no vector, seat, threshold or charter edit; no trade construction.

## 0. Headline: the "Coinbase down ten times bitcoin" premise is a clock mismatch

The commission's figures (COIN −13.7%, BTC −1.3% at 10:4x ET) put two clocks side by side. The equity change runs from the **10/29 16:00 ET close**; the vendor's BTC change runs from **00:00 UTC 10/30** (20:00 ET 10/29), which is after most of the hack-day fall. On the equity clock:

| Instrument | 10/29 16:00 ET | 10/30 ~10:45 ET | Change on the equity clock | Vendor "day" change (UTC-midnight clock) |
|---|---|---|---|---|
| BTC-USD | 80,341.39 | 77,008.69 | **−4.15%** | −0.94% |
| ETH-USD | 2,312.77 | 2,232.15 | −3.49% | −0.46% |
| BNB-USD | 738.70 | 696.49 | **−5.71%** | +0.47% |
| IBIT (spot BTC ETF, equity clock natively) | 45.71 | 43.53 | −4.78% | — |
| QQQ (Nasdaq-100) | 715.34 | 696.71 | **−2.60%** | — |

Source: yfinance via `.venv` (15-minute crypto bars, daily equity closes), pulled 10:52 ET; `fetch.py price` at 10:51 ET gives the same equity moves (COIN −13.16%, HOOD −7.98%, MSTR −8.13%, BITO −4.87%) and the UTC-clock crypto moves (BTC −1.06%, ETH −0.87%). Basis ARTIFACT-VERIFIED (vendor data, two pulls agree).

**So COIN is down about 3× bitcoin, not 10×, on a Nasdaq day down 2.6%.** The venue-specific signal is in **BNB** (−5.71% against BTC −4.15%, the exchange's own token), not in US equities.

## 1. Read (c): US-listed transmission, mechanism per name

Method: 120-day OLS of each name's daily return on IBIT (bitcoin on the equity clock) and QQQ (market), window 2026-05-11 → 10-29, n = 120; today's partial-day return (10:52 ET) against the fitted expectation. ⚠️ A partial day; two factors only; residual sd from the fit window; z is a scale, not a probability.

| Name | Today (from 10/29 close) | Beta IBIT / QQQ | Expected | Residual | z | Dated evidence | Mechanism read |
|---|---|---|---|---|---|---|---|
| **COIN** | −13.1% | 1.42 / 0.17 | −7.4% | **−5.7pp** | −2.1 | Q3 results 10/29 after close: revenue ~$1.22B, −35% YoY; spot volume −10% QoQ; $715M of $719M net income was unrealized crypto gains (Investing.com 10/30 04:32). Mizuho target $155 → $145, Jefferies $183 → $174 (both 10/30). Coinbase: "unaffected by the incident and … monitoring" (Investing.com). After-hours tape: +0.2% at 16:20 ET (after the release, before the 16:24 drain), then tracked IBIT overnight (−4.7% vs −3.8% at 19:55; −8.0% vs −4.5% at 09:25); the gap widened at the 09:30 open (−12.2% vs −5.3% at 09:45) | **Crypto beta explains about 4/7 of the drop. The residual is CONFOUNDED by the company's own earnings and two target cuts, all dated the same morning.** No evidence of venue or custody exposure to Binance. A venue-risk reading is UNSUPPORTED; a competing read in print says the hack *benefits* Coinbase (Benzinga 10/30). Not attributable to Binance on this evidence |
| **MSTR** | −7.8% | 1.72 / 0.41 | −9.5% | +1.7pp | +0.6 | Q3 results 10/29 after close (call 16:00 ET today). CFO resignation 8-K (event 10/26, exhibit dated 10/29; effective 11/05; "personal reasons"). Holdings 848,517 BTC at average cost $75,446 (CoinDesk 10/29); BTC $77,009 now is about 2.1% above it | **Leveraged bitcoin-treasury beta explains all of it** (it fell less than its beta implies). No Binance mechanism priced |
| **HOOD** | −8.2% | 0.81 / 0.77 | −5.7% | −2.4pp | −0.7 | Q3 reported 10/27 (record $1.42B revenue). No Binance statement found | **Retail-broker beta to both bitcoin and the Nasdaq; residual within noise.** No Binance mechanism evidenced |
| **BITO** | −4.8% | (futures ETF) | — | — | — | Matches IBIT −4.78% and BTC −4.15% on the equity clock | **Coin price only** |
| CRCL | −8.6% | 1.43 / 0.42 | −8.2% | −0.5pp | −0.1 | Circle froze $823M USDC (contract events); no Circle notice | The freezing issuer is not marked down beyond its beta |
| GLXY · MARA · BKKT | −7.5% · −6.8% · −5.4% | — | −9.8% · −8.7% · −8.7% | +2.3 · +1.9 · +3.3pp | +0.5 · +0.5 · +0.7 | — | All fell LESS than beta implies |
| CME | +2.67% | — | — | — | — | — | Context only (regulated venue up); not regressed |

**Read (c) verdict:** the US-listed tape prices **coin risk on a down Nasdaq day**, not venue risk. Of seven crypto-linked names, only COIN has a residual beyond one sd, and that residual has a named, dated alternative (its own earnings). Venue risk is visible in BNB. HENRY owns the equity read; this goes to HENRY as facts.

## 2. Read (a): venue contagion and Binance's own updates

| Item | Reading | Basis |
|---|---|---|
| Binance withdrawals | **Off on 0 of 1,447 coin-network pairs at 14:51Z** (10:51 ET); deposits on 1,049. Unchanged from 13:07Z | ARTIFACT-VERIFIED (public config endpoint) |
| Binance notice | Same single notice; `lastUpdateTime` 2026-10-30 11:36Z, unchanged at 14:51Z | PRIMARY-VERIFIED (CMS API) |
| Resumption time | Binance corporate account: "still on track towards the expected timeline to resume the withdrawal service in 45 hours" (via FinanceFeeds 10/30 12:10 UTC+3); TNW 08:59Z: "within 45 hours of its latest update"; another outlet "by Sunday" | SECONDARY (no Binance primary carries a time) |
| Cause | "stems from multiple factors"; "additional points of breach"; Teng: attacker "did not simply use one engineer's permissions" (TNW 08:59Z). Blockaid: "eleven Binance hot wallet keys signing transfers", which conflicts with Binance's "no evidence of any wallet private key leak"; open until the post-mortem | SECONDARY |
| Loss cover | Notice: "SAFU fund and the company's funds" (PRIMARY). "$6.34B company funds set aside, ~$5B already in the same tokens" (CoinDesk headline, search summary) | SECONDARY; no Binance primary found for $6.34B |
| SAFU draw | No SAFU amount or draw published. Its last public size was ~$1B (2022) | SEARCH-NOT-FOUND for a 2026 figure |
| Insolvency language | None. Binance: "User funds are safe" | SEARCH-NOT-FOUND for any insolvency wording |
| Size, other tallies | Elliptic $6.43B (excludes $169M it reads as Binance moving its own money); Arkham $6.01B | SECONDARY |
| Attribution | TRM and now **Chainalysis** both say TraderTraitor (North Korea), high confidence, private. No government attribution in today's coverage | SECONDARY; FBI site not re-read this session (11/02 check) |
| Other centralised venues | **No other exchange halt or limit found.** Bybit: "Bybit is not affected" (CoinDesk 19:07 ET 10/29); Binance.US: unaffected; Coinbase: unaffected | SECONDARY; SEARCH-NOT-FOUND for OKX/Bitget/other halts (3 queries) |
| DeFi venues | **Aave froze its affected lending markets** 19:17 ET 10/29 after the attacker borrowed ETH against USDT; "contracts unaffected, positions remain overcollateralized". **Arbitrum Security Council froze 74.56M tokens** in the hacker's wallet (21:12 ET 10/29) | SECONDARY (CoinDesk live log quoting both) |
| Venue naming Binance exposure | Ethena: unrealized P&L exposure to Binance ~$8.8M, collateral with off-exchange custodians, proof of reserves >101% at 04:25Z | SECONDARY (Ethena statement via press) |

## 3. Read (b): stablecoin redemptions and reserves (facts for LIQUID's CHK-40; LIQUID grades)

| Item | Reading | Basis |
|---|---|---|
| Freezes, re-tallied 14:54Z (block 26306301) | USDC **$823.00M** still at 0x5227; USDT **$1,380.46M** at attacker-linked addresses (1,175.46 + 175.00 + 30.00 probable), unchanged since 13:09Z. **0 DestroyedBlackFunds** events: frozen, not burned or reissued | PRIMARY-VERIFIED (contract events and balances) |
| New blacklists since the first read | USDC 0x62b1…, 0x2948… (13:26–13:27Z, $0 each); USDT 0xed17…, 0x47b4… (13:36Z, $0 and $1.70). Link to Binance not established | PRIMARY-VERIFIED events; link UNKNOWN |
| Ethereum totalSupply (baseline for 11/02) | USDT 88,301,265,725.97 · USDC 47,647,116,796.40 at block 26306300 | PRIMARY-VERIFIED (latest state; the public RPC holds no archive, so no before/after) |
| All-chain circulating, daily | USDT: 182.695B (10/23) → 181.998B (10/28) → 180.999B (10/29) → **180.482B (10/30 00:00Z), −0.517B in the interval that holds the hack**, smaller than the pre-hack day's −0.999B; 7-day −2.21B. USDC: 71.386B → **71.480B (+0.094B)** | SECONDARY (DefiLlama aggregate of on-chain supply), pulled 14:53Z |
| Reading | No redemption surge in the first post-hack daily print. Binance users cannot move stablecoins off the venue while withdrawals are off, so **the redemption test opens when withdrawals reopen**. The USDT drift is a pre-event run | desk reading; LIQUID grades |
| Other issuers | Ripple RLUSD ~$200M (Binance CEO Yi He) vs 40.5M (TRM), conflicting; World Liberty USD1 ~$27M (co-founder Witkoff); BitGo moved to freeze some USD1 (the custodian acting) | SECONDARY (CoinDesk live log) |
| Issuer statements / T-bill sale | No Tether or Circle notice (LIQUID 09:07 ET read). No reserve move or T-bill sale reported | SEARCH-NOT-FOUND |

## 4. Read (d): counterparties named

| Named party | What is said | Basis |
|---|---|---|
| Wintermute (market maker) | Binance exposure "less than 20% of net equity"; operations not disrupted | SECONDARY (CoinDesk 19:59 ET 10/29; PANews) of the CEO's X post |
| GSR (market maker) | "less than 5% of our net equity" | SECONDARY (CoinDesk 19:59 ET) |
| BitGo | Custodian acting on the USD1 freeze, not an exposure | SECONDARY |
| Ceffu + unnamed "banking triparty partners" | The structure behind off-exchange collateral at Binance (BlackRock BUIDL accepted since 2025-11-14). **No exposure statement after the hack** | PRIMARY for the structure (PR Newswire 2025-11-14); SEARCH-NOT-FOUND for an exposure |
| **Banks, prime brokers, lenders** | **None named in any primary document or dated report found** | SEARCH-NOT-FOUND (4 queries, 10:5x ET) |

No bank, credit union, core vendor or CHOKEPOINTS supplier appears. FLOW unchanged; no escalation row; no CHK row's Wave_Touch changes.

## 5. VX-CYP-02 at 11/02: the letter, read now so the grade is not a surprise (no score moved)

PROME's ruling (Will, C): grade on the letter as written; withdrawals still off ≥1 business day ⇒ ORANGE. The literal cells:
- **ORANGE:** "Operator-confirmed outage of one business day or more at a **bank or payment operator**."
- **YELLOW:** "**Precautionary pauses only**, or an outage under one business day at a single institution."
- **Key_Signal** (not a band cell): "… at a bank, payment system, **exchange**, CCP, Fedwire/SWIFT or Treasury-clearing participant."
- Binance's notice calls the suspension "**As an immediate precaution**".

⚠️ So "exchange" sits in the instrument line, not in the ORANGE cell, and the operator's own word is the YELLOW cell's word. CYPHER will grade at 11/02 as ruled. PROME said it verifies the literal cells; this is that check, handed over before the grade so the ruling's reading is applied knowingly. Duration: off since Thu 10/29 evening ET; Fri 10/30 is one full business day, so the ≥1-business-day leg is met at Friday's close however the reopening goes.

## 6. Do-not-relay additions (carrier forms seen today)

| Form | Why not | Say instead |
|---|---|---|
| "Coinbase down ten times bitcoin" | Two clocks: equity from the 10/29 close, BTC from UTC midnight | "COIN −13% vs BTC −4% since Thursday's close; the residual overlaps its own earnings" |
| "Binance halted trading" (Yahoo headline) | Trading and deposits are up; withdrawals are off | "Binance suspended withdrawals" |
| "Binance suspended all deposits and withdrawals" | Deposits enabled on 1,049 pairs (config 14:51Z); notice updated to say so | as above |
| "Tether and Circle said they froze $2.36B" | No issuer notice; CEO posts via press; the freeze is a contract action | "Tether and Circle froze $X, per their contract events" |
| Kill-on-sight carried: "$6.3B stolen" (RTE headline today) · "Tether/Circle announced a freeze" | as RECORD 10/30 §9 | — |

## 7. Leg 2 (registered, `docket/CATALYSTS.tsv` 2026-11-02, P1)

The same four reads, plus: the VX-CYP-02 grade on the letter (ruling C) with the composition-is-not-mechanism note beside the score; the prospective re-cut draft for PROME to verify; the standing-owner recommendation (option B or not). Baselines to compare at 11/02: config 0/1,447 at 14:51Z; freezes USDC $823.00M / USDT $1,380.46M; Ethereum supply above; DefiLlama daily circulating above; equity residuals in §1.
