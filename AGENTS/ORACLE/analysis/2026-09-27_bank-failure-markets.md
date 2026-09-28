# Bank-failure markets across the Nano Banc failure (Fri 2026-09-25): is the 2026 count or a next-failure event priced?

**ORACLE · 2026-09-27 12:3x ET (16:3xZ) · answers PROME packet `inbox/2026-09-27_from-PROME_bank-failure-markets-one-question.md` (prome-09).** This is a read only: no prediction and no gate. Fact base = `PROME/plans/2026-09-27_nano-banc-failure-investigation-PLAN.md` §1, not re-derived here. The FDIC failed-bank list CSV was re-pulled 2026-09-27 and matches §1: six 2026 closings, Nano Banc cert 58590 closed 25-Sep-26, acquirer Sunwest Bank.

## Answer in one paragraph

**No market prices the 2026 failure count, on either venue, and no "next US bank failure" market is open as of 2026-09-27 16:20Z.** The only next-failure contract, Polymarket's any-bank "US bank failure by December 31, 2026?", **resolved YES on Nano Banc**. It closed 2026-09-26 01:12Z and paid out at $1.00. Polymarket has not relisted a successor (searched active and closed, below). The only open bank-failure market is Polymarket's **named-bank** event, "Which banks will fail by end of 2026?" ($76.1K event). Its legs are large banks sitting at a 0.9–4.4% long-shot floor on books of $116–$2.9K, and **none of them moved outside noise on Nano Banc**. The dead any-bank contract **did not lead the news**. It traded 51–57.5% through 18:25 ET Friday, first repriced with a trade at **19:08 ET**, and was 99.5% by 19:15 ET. That is about 2h09m **before** the 21:17 ET American Banker story, so the trigger was the regulator's release, whose own timestamp I did not verify. The crowd priced a failure by Dec 31 at about **55%**, which matches the **2024/25 pace** (≈51%). The naive **2026 pace** gives ≈94%. On a contract with **$4.1K lifetime volume**, that is a thin crowd, not a considered view.

## 1. Search: what exists (query terms tried)

| Venue | Query / method | Open markets found | Coverage basis |
|---|---|---|---|
| Polymarket | `polymarket.py search`: "bank failure", "bank fail", "banks fail 2026", "how many banks", "FDIC", "bank collapse", "bank run", "regional bank", "Nano Banc", "another bank" | **1 event:** `which-banks-will-fail-by-end-of-2026` (named banks) | Gamma search |
| Polymarket | Gamma `public-search`, `events_status=active` and `closed`: "US bank failure by September / October / December", "another US bank failure", "bank failures 2026", "how many US banks fail" | Active: **same 1 event**. Closed 2026: 5 any-bank Dec-31 instances + monthly Jan–Jul 2026 (table §3) | Gamma search, title filter `bank`+`fail`, end ≥2026 |
| Kalshi | `kalshi.py search`: "bank failure", "bank fail", "FDIC" | **0 markets** | **CERTIFIED:** full open-event universe, 13,018 events / 66 pages |
| Kalshi | `kalshi.py search "bank"` (308 hits) filtered for fail/FDIC/collapse/insolvency/receivership/deposit | **0 relevant** (central-bank rates, IPO underwriters, Senate) | CERTIFIED as above |
| Kalshi | `kalshi.py series --category Financials` / `Economics`, grep bank/fail/FDIC/deposit | **0 bank-failure series** (bank-named series are IPO-underwriter and big-bank layoffs) | Series listing |

⚠️ **Known limit:** `kalshi.py search` does not index series-level title text (CLAUDE.md). The category series listing is the compensating check, and it found no bank-failure series. **Result: NONE on Kalshi, with the terms above.** No count market ("how many US banks fail in 2026") exists on either venue, open or closed in 2026, under the terms tried.

## 2. What the markets did across Friday 9/25 (all times ET; Polymarket CLOB `prices-history` 5-min midpoint + `data-api` trades)

| Market | Book / volume | Before the news (12:00–18:25 ET 9/25) | First reaction | After | Moved on Nano? |
|---|---|---|---|---|---|
| **Any US bank fails by Dec 31, 2026** (`…-20260824`) | liq $939 (9/25 02:15Z) · **lifetime vol $4,126** | Midpoint oscillates **50.5–57.5**; only 2 trades all afternoon ($6.00 YES @0.60 17:01, $9.45 YES @0.63 17:06) | **19:08 ET** trade YES @0.80 ($274), then @0.96–0.99; ~**$1.1K** traded 19:08–19:20 | 99.5 @19:15 ET → **resolved YES**, closed 01:12Z 9/26 (21:12 ET) | **Yes, reactively.** No pre-news move (the 50–57 swing is midpoint noise on a <$1K book, with no trades behind it) |
| Named: KeyBank fails by EOY 2026 | $9.2K vol · **$560 liq** | 2.6 (9/24) → 3.6 (14:00 ET 9/25) | — | 2.5–8.1 swings 9/26–9/27; 4.4% @16:20Z 9/27 | **No** — the swings are one-print noise on a $560 book |
| Named: US Bank fails by EOY 2026 | $9.1K vol · $2.4K liq | 3.2 | 4.3 @03:00 ET 9/26 | 4.3% | +1.1pp — inside noise |
| Other 17 named legs (JPM, BAC, C, WFC, GS, MS, Truist, BNY, UBS, HSBC, DB, BNP, Santander, Lloyds, RBC, BMO, Scotia) | $509–$10.4K vol each | 0.9–3.2% | — | Δ7d −0.8 to +0.2 | **No** |

**Timing anchors (added after PROME's consumer read):** the 19:08 ET first repricing trade also precedes **Sunwest Bank's own release (19:45 ET, prnewswire, per PROME)**. The FDIC/DFPI release time stays **unverified** by ORACLE.

**Monday 9/28 open:** not yet observed. The any-bank contract no longer exists; re-read the named event and re-search for a relisted successor at the next pull.

## 3. The contract family in 2026: it pays out at each failure and gets relisted

Each any-bank "by Dec 31, 2026" instance has **resolved YES at the next failure** and then been relisted:

| Instance (slug suffix) | Listed | Pre-failure reads | Resolved by (FDIC close date) | Closed (UTC) | Lifetime vol |
|---|---|---|---|---|---|
| `-996` | 2026-04-08 | not logged | Community B&T West GA (5/1) | 05-02 00:22Z | $13.6K |
| `-20260629…` | 2026-06-29 | 50.5–72.5 (CLOB hourly); **66.0** @07-10 20:00Z | Kentland FS&L (7/10) | 07-10 22:37Z | $13.7K |
| monthly `by-july-31-…` | 2026-07-01 | 10.5–50.0; **15.0** @07-10 20:00Z | Kentland FS&L (7/10) | 07-10 22:33Z | $96.3K |
| `-20260720…` | 2026-07-20 | 69.5–73.0 (ORACLE ODDS_LOG 7/22–8/18) | Tioga-Franklin (8/21) | 08-21 22:34Z | $8.0K |
| `-20260824` | 2026-08-24 | 55.5–66.0 (ODDS_LOG 8/27–9/25); **57.5** @18:25 ET 9/25 | **Nano Banc (9/25)** | 09-26 01:12Z | $4.1K |

Also closed in 2026: monthly/"another" contracts for Jan (**$693K** lifetime volume, the largest), Feb ($77.6K + "another" $102.6K), Mar ("another" $114.4K), Apr ($25.6K), May ($20.0K), Jun ($26.5K / $22.7K). I found **no August or September 2026 monthly contract**. **Lifetime volume per contract instance has fallen across 2026:** the Jan contract carried ~170× the lifetime volume of the one Nano resolved. *(Relabelled 2026-09-28 per CATO NB5 via PROME: this was headed "Depth has been falling all year". Lifetime volume per instance is NOT depth — instances differ in window length and listing life — and it does not measure an interest or liquidity trend. No re-pull; figures unchanged.)*

⛔ **Self-correction:** ORACLE's watchlist notes (7/02, 7/22, 8/27) called the repeated `PINNED BUT NOT FOUND` on this family "delisted/relisted". **At least the 7/10, 8/21 and 9/25 disappearances were resolutions, not delistings.** Each failure resolved the pinned instance YES. Consistent with the standing flag that `PINNED BUT NOT FOUND` cannot tell resolved from a bad slug.

## 4. Crowd vs FDIC base rate (the one table PROME asked for)

Poisson on arrivals, P(≥1 failure in window) = 1 − e^(−rate × days). This is illustrative: failures cluster and the 2026 inter-arrival gaps are shrinking (91 → 70 → 7 → 35 → 35 days).

| Window | Crowd price | 2026 pace (6 in 268d to 9/25 ≈ **8.2/yr**) | 2024/25 pace (**2/yr**) | Crowd-implied pace |
|---|---|---|---|---|
| 8/24 → 12/31 (129d), instance that Nano resolved | **~55%** (55.5 on 8/27; 57.5 @18:25 ET 9/25) | 5 in 233d to 8/21 ⇒ **≈94%** | **≈51%** | ≈2.3 failures/yr |
| 7/01 → 7/31 (monthly, read 7/10 20:00Z, 21d left) | 15.0% | 2 in 190d ⇒ ≈20% | ≈11% | — |
| **Now: 9/27 → 12/31 (95d)** | **not priced: no open market** | ≈88% | ≈41% | — |

**Read:** the only next-failure market priced **below** the 2026 base rate, at roughly the 2024/25 pace, and it resolved YES four times in five months. **It does not imply more than the FDIC base rate; it implied materially less.** Treat this as thin-market pricing, not a crowd view. At $4.1K lifetime volume, one $300 order moves it 20pp. The ORACLE thin-liquidity rule applies: never marked, and I would not route it as a signal.

## 5. Routing and what this changes

- **No watchlist row added.** No count or next-failure market exists. The resolved `-20260824` pin is retired in `watchlist.tsv`, with the resolution recorded. Re-search at every pull for a relisted successor; relist gaps so far were 58d (5/02→6/29), 10d (7/10→7/20), 3d (8/21→8/24).
- **WALTER watch term `bank failure`: not owed.** Per PROME's condition, no new market exists. The named-bank event has been tracked since 7/02.
- **Book perimeter:** the named-bank event lists **KeyBank (4.4%, $560 liq)** and **US Bank (4.3%)**. Both are standing long-shot legs that did not move on Nano Banc. If either is in Will's perimeter (KRE constituents), the finding is "the crowd did not move", which I judge not worth a TERRY packet. PROME's call.
- ORACLE owns the crowd read only. REGINALD owns the failure anatomy, and REGINALD owns the loss-severity figure; this file does not cite it.

*Sources: Polymarket Gamma (`/markets`, `/events`, `/public-search`), CLOB `/prices-history`, data-api `/trades`, all pulled 2026-09-27 16:20–16:30Z. Kalshi trade-api v2 via `kalshi.py`, signed lane rc=0, 2026-09-27. FDIC failed-bank list CSV, pulled 2026-09-27. ORACLE `workbook/ODDS_LOG.tsv`.*
