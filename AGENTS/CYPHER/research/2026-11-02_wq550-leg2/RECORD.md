# WQ-550 leg 2: Binance at the reopening, four reads + VX-CYP-02 grade + re-cut draft + owner recommendation (CYPHER, 2026-11-02)

**Session:** CYPHER, spawned by PROME (prome-40, desktop) 2026-11-02 ~08:48 ET as a WQ-184 due-row wake (DOCKET L878, leg 2 of Will's 10/30 10:46 ET commission, record `PROME/proposals/2026-10-30_wq550-binance-RULED.md`). Wall clock 08:48–09:1x ET (EST; DST ended 11/01). Incident row CYB-INC-055. Leg 1: `../2026-10-30_wq550-leg1/RECORD.md`.
**Evidence beside this record:** `binance_network_status_2026-11-02T1348Z.txt` (config, all 29 enabled pairs listed) · `notice_<code>.txt` ×4 (Binance Updates #2–#5, verbatim via the public CMS API) · `onchain_supply_2026-11-02T1349Z.txt` · `onchain_freeze_recheck_*.txt` · `scripts/freeze_recheck.py`.
**Fences kept:** the only score graded is VX-CYP-02 on its letter (held at 3). No seat, charter, threshold, gate or trade moves. VX-CYP-08 is NOT re-scored (§6: the commission fence); it is flagged to PROME.

## 0. Headline

**Binance reopened, customers pulled money out, and nothing outside crypto moved.**
- **Reopening:** Binance began phase one on **Sun 11/01 06:00–09:00 UTC** (Update #4, PRIMARY). At **13:48Z today, 29 of 1,448 coin-network pairs are withdraw-enabled** (BTC, ETH, USDT and USDC on the main chains, SOL, BNB, XRP and others). 1,419 are still off (ARTIFACT-VERIFIED, public config). The notice listed about 40 phase-one pairs; the config shows 29 live, so USDT on Tron, POL, and USDT on Polygon and Avalanche are not yet on. Binance says the next phase is "planned for tomorrow" (Update #5, 12:45Z today).
- **Run size:** Binance reports **$3.64B net outflows from 06:00 to 15:30 UTC 11/01**, which is 2.1% of $171B total assets (Binance X post via CNBC, SECONDARY). A Binance spokesperson later told Reuters the figure was **$4.72B net since Sunday morning** (BNN Bloomberg 11/02 07:31 ET, SECONDARY). Inflows were $2.7B. That is a withdrawal wave, not a run: about 2–3% of assets.
- **Cover:** Binance says it has replaced **~95%** of the stolen amount from company funds, a partial SAFU deployment and part of its futures insurance fund, and that the ten largest tokens are "fully backed 100%". Its 10/31 00:00Z Proof of Reserves snapshot now has a completed zero-knowledge proof (Updates #3–#5, PRIMARY; the coverage figures are OWNER-ASSERTED). **No insolvency language anywhere.**
- **Attribution:** the **FBI attributed the theft to North Korea (TraderTraitor)** in an alert published Sat 10/31: "the theft of more than $6 billion USD in virtual assets from cryptocurrency exchange Binance, on or about October 29, 2026" (quoted by BleepingComputer 11/01). It published 628 addresses for exchanges to block. fbi.gov returns HTTP 403 to this box, so this is **SECONDARY** (alert text quoted by several outlets; the fbi.gov URL appears in search results).
- **Stablecoins:** on Ethereum the freezes are **unchanged to the cent** and none have been burned or reissued. Circulating supply shows **no redemption surge** across the reopening (§3). LIQUID grades.
- **US-listed tape:** at Friday's full close, **COIN's residual shrank to −2.6pp (z −0.9)**: within noise. Every name sits inside its bitcoin-plus-Nasdaq beta. Monday's equity session had not opened at this read.
- **Named counterparties:** still **no bank, custodian, prime broker or lender named** as exposed (SEARCH-NOT-FOUND, 3 queries plus 3 articles read).

## 1. Read (a): venue contagion and Binance's own updates

| Item | Reading 2026-11-02 | Leg-1 baseline (10/30) | Basis |
|---|---|---|---|
| Withdraw-enabled pairs | **29 of 1,448** at 13:48Z | 0 of 1,447 at 14:51Z | ARTIFACT-VERIFIED (getNetworkCoinAll) |
| Deposit-enabled pairs | 1,036 of 1,448 | 1,049 of 1,447 | ARTIFACT-VERIFIED |
| Phase one start | "2026-11-01 between 06:00 and 09:00 (UTC)", 15 networks listed | none | PRIMARY (Update #4, published 11/01 04:08Z) |
| Operator's word for the pause | "Withdrawals were temporarily suspended **as a precaution** while our teams worked to contain the incident loss…" | "As an immediate precaution" | PRIMARY (Update #4) |
| Loss wording | Update #2: "our hot wallets were compromised, resulting in a loss of approximately $6.3B USD worth of token assets" | "estimated total impact … around $6.3B" | PRIMARY. ⚠️ Binance's own word is now "loss". The fleet form stays "Binance-stated loss ~$6.3B, ~$3B of it frozen on-chain"; never "$6.3B stolen" (it omits the frozen half) |
| Cause | "additional points of breach" beyond the laptop; "no evidence that wallet private keys were leaked"; technical findings "within about 48 hours" of 10/30 19:33Z, **not yet published** (post-mortem still owed at 11/02 13:49Z) | laptop only | PRIMARY (Update #2) |
| Cover | $6.34B company funds set aside (Update #2) → 80% → 90% (#3) → **~95%** (#4, #5); top ten tokens "fully backed 100%"; remaining 5% is less liquid tokens | — | PRIMARY wording; figures OWNER-ASSERTED |
| SAFU | "A partial deployment of the Secure Asset Fund for Users"; to be replenished to "approximately US$1 billion"; held by Nest Clearing and Custody (ADGM). **No amount drawn is stated** | no SAFU amount | PRIMARY (Update #3); amount SEARCH-NOT-FOUND |
| Futures insurance fund | "A portion" used; Binance says the fund remains above its required level | — | PRIMARY / OWNER-ASSERTED |
| Proof of Reserves | 10/31 00:00Z snapshot; ZK proof completed (11/02); next snapshot 11/04 | — | PRIMARY |
| Insolvency language | None | None | SEARCH-NOT-FOUND |
| Outflows after reopening | $3.64B net (06:00–15:30Z 11/01; 2.1% of $171B assets, PoR 10/28) → $4.72B net "since Sunday morning" (11/02); inflows $2.7B | — | SECONDARY (Binance X post via CNBC 11/01 19:11 ET; Binance spokesperson via Reuters/BNN Bloomberg 11/02 07:31 ET) |
| USD cash withdrawals | "restored Monday" | — | SECONDARY (BNN Bloomberg) |
| Other venues halting | **None found** | none | SEARCH-NOT-FOUND (extended search 11/02; CNBC and BNN articles name none) |

## 2. Read (d): counterparties named, and attribution

| Item | Reading | Basis |
|---|---|---|
| Banks, custodians, prime brokers, lenders | **None named** in Binance's four updates, the FBI alert as quoted, CNBC 11/01–02 or BNN Bloomberg 11/02 | SEARCH-NOT-FOUND (3 searches, 3 articles read) |
| Market makers (leg 1) | Wintermute <20% of net equity, GSR <5%; no update found | SECONDARY (10/29) |
| Government attribution | **FBI: DPRK "TraderTraitor", alert published Sat 10/31**; FBI + Secret Service + IRS-CI ask VASPs to block 628 addresses (608 ETH, 19 BTC, 1 SOL) | SECONDARY (BleepingComputer 11/01 14:57 ET quoting the alert; NBC, Fox Business, The Hacker News, Decrypt). fbi.gov 403 to WebFetch and curl |

## 3. Read (b): stablecoin redemptions and reserves (facts for LIQUID's CHK-40; LIQUID grades)

Labels split per LIQUID's 10/30 note: primary-verified and probable components are carried separately.

| Item | 11/02 13:50Z | Leg-1 baseline 10/30 14:54Z | Basis |
|---|---|---|---|
| USDC frozen at 0x5227 | **$823,000,000.00** | $823,000,000.00 | PRIMARY-VERIFIED (balanceOf, latest block) |
| USDT frozen, attacker-linked | **$1,350.46M** (1,175.46 at 0x5227 + 175.00 at 0xaa24) **+ $30.00M probable** (0xb171) | same | PRIMARY-VERIFIED balances; the $30.00M link is PROBABLE |
| All 22 addresses blacklisted in the leg-1 window | USDC $828,870,986.74 · USDT $1,382,022,670.45; **one change**: USDT 0xed17 received $206,065.61 after it was blacklisted (inbound transfers to a frozen USDT address are allowed; it stays frozen) | USDC $828,870,986.74 · USDT $1,381,816,604.84 | PRIMARY-VERIFIED |
| Burned / reissued | **No.** The frozen balances are intact; a USDT DestroyedBlackFunds would have zeroed them | 0 events | PRIMARY-VERIFIED by balance. ⚠️ The event-log scan itself FAILED on every public RPC (publicnode 403; ankr needs a key), so new blacklists since 10/30 are **UNKNOWN**, not zero |
| Circle's own figure | Circle spokesperson: will "freeze more than $1.1 billion in USDC associated with the incident" | — | SECONDARY (CNBC 11/01). ⚠️ That is ~$270M more than the Ethereum balances above; other chains or pending freezes are possible and were not read (no archive RPC; Solana/Base not checked) |
| Issuer notices | **No Tether or Circle newsroom item on Binance** (tether.io/news latest 10/30 = Q3 attestation as of 9/30; circle.com pressroom latest 10/27; blog 10/28; read 13:5xZ). Circle reports Q3 on **11/04** | none | PRIMARY (newsroom pages) / SEARCH-NOT-FOUND for a notice |
| Ethereum totalSupply | USDT 88,301,265,725.97 (**unchanged**) · USDC 47,263,488,363.98 (**−383.63M**) at block 26327499 | USDT 88,301,265,725.97 · USDC 47,647,116,796.40 | PRIMARY-VERIFIED (latest state; chain-level supply moves with cross-chain transfers, so this is not a redemption measure by itself) |
| All-chain circulating, daily (00:00Z prints) | **USDT** 180.482B (10/30) → 180.093B (10/31, −0.389) → 179.792B (11/01, −0.301) → **179.461B (11/02, −0.331; the print that holds the reopening day)**. **USDC** 71.480B → 71.903B (+0.423) → 71.871B (−0.032) → **71.647B (−0.224)** | USDT −0.517B on the hack-day print; pre-hack day −0.999B | SECONDARY (DefiLlama aggregate of on-chain supply), pulled 13:50Z |
| Reading | **No redemption surge across the reopening.** USDT keeps the same ~−0.3B/day drift it had before the hack; the reopening-day print (−0.331B) is smaller than the pre-hack day's −0.999B. USDC's −0.224B is within its own prior week's range (−0.443B on 10/27). Only one print covers the reopening (06:00Z→00:00Z, 18 hours); the 11/03 print covers Monday | desk reading; LIQUID grades |
| T-bill sale / reserve move | None reported | SEARCH-NOT-FOUND |

## 4. Read (c): US-listed transmission on the equity clock

Method as leg 1: 120-day OLS of daily returns on IBIT (bitcoin on the equity clock) and QQQ, fit window 2026-05-11 → 10-29 (n = 120), applied to the **full Friday 10/30 session** (close vs Thursday 10/29 close). Closes via yfinance (`.venv`), cross-checked against `fetch.py price` at 08:50 ET (same closes, marked stale because Monday has not opened). ⚠️ Two factors only; z is a scale, not a probability.

| Name | 10/30 close | Beta IBIT / QQQ | Expected | Residual | z | vs leg 1 intraday (10:52 ET) |
|---|---|---|---|---|---|---|
| **COIN** | −10.62% | 1.42 / 0.17 | −8.03% | **−2.59pp** | **−0.9** | −5.7pp, z −2.1: **faded to noise by the close** (its own Q3 and two target cuts still overlap it) |
| HOOD | −7.21% | 0.81 / 0.78 | −6.66% | −0.54pp | −0.2 | −2.4pp |
| MSTR | −7.84% | 1.72 / 0.41 | −10.46% | +2.61pp | +0.9 | +1.7pp |
| BITO | −5.01% | 0.99 / 0.00 | −5.10% | +0.09pp | — | coin price only |
| CRCL | −9.31% | 1.43 / 0.43 | −9.04% | −0.28pp | −0.1 | −0.5pp. The freezing issuer is not marked down beyond beta |
| GLXY · MARA · BKKT | −11.75 · −5.58 · −8.66% | — | −11.76 · −10.32 · −9.99% | +0.01 · +4.74 · +1.33pp | 0.0 · +1.2 · +0.3 | all at or better than beta |
| Factors | IBIT −5.14% · **QQQ −3.47%** (Friday was a broad Nasdaq down day) | | | | | |

Crypto over the weekend and the reopening (equity-clock anchor = Fri 16:00 ET): BTC 76,753 → 77,884 (+1.5%), ETH 2,234.64 → 2,288.55 (+2.4%), BNB 699.07 → 704.57 (+0.8%) at 08:45 ET 11/02 (yfinance 15-minute bars). ⚠️ Vendor bar vintage: this pull gives BTC 80,746.01 at the 10/29 16:00 ET anchor, where leg 1's pull gave 80,341.39 (0.5% apart); IBIT is the clean equity-clock bitcoin measure and is what the fit uses.

**Read (c) verdict:** at the full-day close, **no US-listed name prices Binance venue risk.** Coinbase's intraday residual faded from −5.7pp to −2.6pp (z −0.9). The reopening weekend saw bitcoin and BNB recover slightly. Monday's session is unread (it opens 09:30 ET). HENRY owns the equity read.

## 5. VX-CYP-02 graded on its letter as written (ruling C): **YELLOW, held at 3**

The literal cells (VX.tsv row VX-CYP-02, unchanged since 10/22):
- **ORANGE:** "Operator-confirmed outage of one business day or more at a **bank or payment operator**."
- **YELLOW:** "**Precautionary pauses only**, or an outage under one business day at a single institution."
- **Key_Signal (instrument line, not a band):** "Operator-confirmed outage at a bank, payment system, **exchange**, CCP, Fedwire/SWIFT or Treasury-clearing participant."

| Test | Fact | Met? |
|---|---|---|
| Operator-confirmed | Binance's own notices | Yes |
| One business day or more | Off from ~22:33Z Thu 10/29 to phase one Sun 11/01 06:00–09:00Z; **all of Fri 10/30 off**; on Mon 11/02, 1,419 of 1,448 pairs still off | Yes |
| At a bank or payment operator | Binance is a crypto exchange: not a bank, not a payment operator in this vector's sense | **No** |
| YELLOW's "precautionary pause" | Binance: "temporarily suspended as a precaution" (Update #4) | The operator's word matches |

**Grade: YELLOW on the letter, score held at 3** (no change to the composite: 22/40 raw, 16/40 shared-root-adjusted). The ORANGE cell names banks and payment operators, so an exchange outage cannot reach it on the letter. The predicted ORANGE in the 10:46 ET ruling text came from the instrument line; PROME corrected that at 11:03 ET 10/30.

**Composition ≠ mechanism (written beside the score):** the vector is built for US dollar payment and market plumbing. This event is a crypto venue with no dollar-payment or Treasury-settlement consequence observed: no bank named, stablecoins frozen and not redeemed in a rush, LIQUID's CHK-40 = no plumbing consequence. It is logged beside the score and does not add to it.

⚠️ **The letter is internally inconsistent**, and the score is right only by accident. The instrument line names "exchange", but no band does. And the YELLOW cell's "precautionary pause" was written for a precaution at an operator whose own systems were NOT compromised (Japan's banks, the credit union). Binance's suspension followed a confirmed theft through its own withdrawal infrastructure, so "precaution" is the operator's label, not the case YELLOW describes. On the letter it reads YELLOW; on the band's intent it would be an outage. The re-cut below closes both gaps, forward only.

## 6. One flag that the commission fence blocks: VX-CYP-08 (state-actor campaign)

The 11/02 catalyst row says "government attribution -> re-class STATE-CAMPAIGN and re-score VX-CYP-08". The FBI attribution (10/31) now exists. VX-CYP-08's ORANGE cell reads "A US / UK / EU government attribution of a financial-sector-relevant campaign". On its face that letter is met, but **the commission permits no score move other than VX-CYP-02, so the score is held at 3 and flagged to PROME.** The same composition question applies: a theft from a crypto exchange is "financial-sector-relevant" only in the broad sense, and the vector was built for state campaigns against banks, insurers and energy (NotPetya). **Done:** CYB-INC-055 re-classed UNCLASSIFIED → STATE-CAMPAIGN (a ledger fact under the Class enum's "attributed state activity"; the event stays OFF-WAVE, so escalation row 7 of WAVE-2026-10 does not fire). **Not done:** the VX-08 score. It is CYPHER's own score outside this commission; it is graded at the next CYPHER session unless PROME rules otherwise.

## 7. Prospective re-cut of VX-CYP-02 (DRAFT for PROME to verify; governs events after encode, never this one)

| Cell | Current letter | Proposed letter |
|---|---|---|
| Key_Signal | Operator-confirmed outage at a bank, payment system, exchange, CCP, Fedwire/SWIFT or Treasury-clearing participant | Operator-confirmed outage at a **US dollar payment or market-infrastructure operator**: a bank or credit union; a payment system or network (Fedwire, ACH operators, RTP/FedNow, card networks, SWIFT); a **regulated securities or derivatives exchange** (e.g. NYSE, Nasdaq, Cboe, CME, ICE); a CCP or settlement utility (DTCC/NSCC/FICC, OCC); or a Treasury-clearing participant. **Crypto-asset venues (centralised exchanges, DeFi protocols) are logged in Notes and do not score this vector** unless the outage reaches one of the operators above or halts USD stablecoin redemption (that leg routes to LIQUID, CHK-40) |
| GREEN | No operator-confirmed outage outside precautionary pauses | unchanged |
| YELLOW | Precautionary pauses only, or an outage under one business day at a single institution | Precautionary pauses only **(a pause at an operator whose own systems are not confirmed compromised)**, or an outage under one business day at a single **listed operator** |
| ORANGE | Operator-confirmed outage of one business day or more at a bank or payment operator | Operator-confirmed outage of one business day or more at a **single listed operator**, **including a suspension that follows a confirmed compromise of that operator's own systems, whatever the operator calls it** |
| RED | Outage at a central payment system, CCP or Treasury-clearing participant, or multi-institution outage of one business day or more | unchanged |

Invariants: the GREEN and RED cells, the score map (YELLOW 3 / ORANGE 4 / RED 5), the routes (LIQUID, BOND, REGINALD) and watch row 8 are unchanged. Under the re-cut, a Binance repeat scores nothing on VX-02 (logged in Notes), and a regulated exchange or a bank that suspends service after its own systems are breached takes ORANGE at one business day whatever its notice calls the pause. PROME verifies the literal cells before calling it encoded; the cells change only on PROME's verification, and it goes to Will if PROME reads it as a gate-letter change (the ORANGE meaning moves).

## 8. Recommendation on a standing owner for crypto venues (option B, CYPHER charter extension): **not warranted now** (Will's word)

| For an owner | Against an owner (CYPHER's recommendation) |
|---|---|
| The largest crypto theft on record ($6B+, FBI) had no consequence owner; it took a Will ruling to get it read | **Two sessions answered it.** The bounded commission produced every read Will asked for in about two hours of desk time |
| Crypto venue risk could reach US finance through stablecoins, bank custody or listed brokers | **Nothing transmitted.** No bank, custodian, prime broker or lender named; stablecoin freezes held and redemptions show no surge; US-listed names sit within beta at the close; LIQUID's CHK-40 found no plumbing consequence. The issuers acted as a control |
| — | Binance absorbed the loss from its own funds (~95% replaced), and withdrawals ran at ~2–3% of assets, not a run |
| — | An owner would be a standing cost for an event class whose transmission to US finance was zero this time. Will's 10/31 rule leans the same way ("limit our excess amount of checkers and rules") |

**Recommendation:** keep the NO-OWNER row in the exclusions register, and keep using a bounded commission on Will's word per event, with this record as the template. **Revisit if any one of these is observed:** (1) a crypto venue failure names a US bank, custodian, prime broker or lender as exposed; (2) a USD stablecoin issuer halts or gates redemption, or sells T-bills because of a venue event (LIQUID's CHK-40); (3) a US-listed name prices venue risk beyond its beta at a full-day close (residual beyond 2 sd); (4) a second crypto-venue event of $1B or more inside 90 days. This is a recommendation; the owner question stays Will's.

## 9. Do-not-relay (carried, plus today's forms)

| Form | Why not | Say instead |
|---|---|---|
| "$6.3B stolen" | Omits that about $3B is frozen on-chain | "Binance-stated loss ~$6.3B, ~$3B of it frozen on-chain" |
| "Tether/Circle announced a freeze" | No issuer notice exists; there are CEO posts and a Circle spokesperson quote | "Tether and Circle froze $X, per their contract events" (Circle's spokesperson says >$1.1B USDC; Ethereum shows $828.87M) |
| "Bank run at Binance" / "customers fled" | $3.64B–$4.72B net is about 2–3% of $171B assets, with $2.7B inflows | "net outflows of about $4.7B (Binance figure), ~2–3% of assets" |
| "Binance fully reopened" | 29 of 1,448 pairs at 13:48Z 11/02 | "phase one reopened 11/01: 29 of 1,448 pairs (major coins); more phases to come" |
| "Users are 100% covered" | Binance says ~95% of the impacted amount is covered; the top ten tokens 100% (OWNER-ASSERTED; the ZK proof covers the 10/31 snapshot of those ten) | "Binance says ~95% replaced; top ten tokens fully backed per its 10/31 PoR" |
| "Coinbase priced Binance venue risk" | Residual −2.6pp, z −0.9 at the 10/30 close | "COIN moved with bitcoin and the Nasdaq at Friday's close" |

## 10. Gaps

- Post-mortem not yet published (promised ~48h after 10/30 19:33Z).
- New blacklist events since 10/30 UNKNOWN (log scan failed on every public RPC); Circle's ">$1.1B" not reconciled on other chains (no Solana/Base read).
- FBI alert read only through press (fbi.gov 403).
- Monday's US equity session not read (pre-open).
- The outflow figures are Binance's own, via press.
