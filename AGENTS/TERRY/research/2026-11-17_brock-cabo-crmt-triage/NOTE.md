# TERRY same-day triage — Cable One skipped coupon, Car-Mart 13th bridge, VIOLET timing check

**Written:** 2026-11-17 09:59 EST (system clock) · TERRY, Claude Code, Claude Opus 5.5 · task from PROME prome-19 (WQ-696 handoff; Will's standing word 2026-11-10 18:03 ET).
**Answer:** **NO window is lost by waiting to Wed 11/18 (D:L1128). NO CARD on Cable One, NO CARD on Car-Mart. No order. $0.**

## 1. Boot and dependencies

| Item | State |
|---|---|
| Repo root | `/home/willi/Research-workspace` (resolved with `git rev-parse --show-toplevel`; every path below is root-relative) |
| Instructions read | root `CLAUDE.md` (24,449 B) and `AGENTS/TERRY/CLAUDE.md` (23,176 B) loaded from those root-resolved paths; `AGENTS.md`, `USER.md`, `STATUS.md`, `RISK_RULES.md` read explicitly. No `AGENTS/TERRY/AGENTS.md` exists. |
| `boot.py` | ran; ledger sweep clean; BOARD: 52 addressed, all logged; inbox 7 unprocessed |
| Market data | yfinance via `.venv` works. Negative control: IWM lists 29 expiries in the same minute that CABO and CRMT list 0, so the empty chains are the names, not the feed. |
| Missing | Bond prices for the Cable One 4.00% 2030 notes: no zero-cost quote source on this box (TRACE not reached; no paid data per task limits). VIX November future: the vendor has no quote for it (404). MCP servers mtnewswire and definite failed to connect; not needed. |

## 2. What instruments exist (live, 2026-11-17)

| Name | Listed equity | Listed options | Other | Vendor quote |
|---|---|---|---|---|
| Cable One (CABO) | NYSE common | **none** (0 expiries, 09:57 ET) | 4.00% senior notes due 2030, over the counter, no quote reachable; other debt not checked | $3.0005, +1.0% vs $2.97 prior close; bid/ask $2.95 / $3.13 (6% wide); 12,421 shares by 09:57 vs about 573,000 average; market value about $17.0M on 5.68M shares; short interest 38.0% of float (vendor, date of the short figure not given); vendor marks the feed 20 minutes delayed, last trade stamped 09:57:10 ET |
| Car-Mart (CRMT) | Nasdaq common | **none** (0 expiries, 09:57 ET) | none tradeable known | $0.9479, +1.9% vs $0.93; vendor bid/ask crossed ($1.45 / $0.96), unusable; market value about $7.9M; short interest 30.6% of float (vendor) |

## 3. Cable One — NO CARD

BROCK's handoff carries all four WQ-696 parts (implication, horizon, invalidation, unknowns). Its direction: restructuring or exchange in which equity and the 2030 notes take terms. PROME's caveat travels: the missed payment and the stated intent are ESTABLISHED (8-K 0000950157-26-001261, accepted 11/16 16:41 ET); that it could pay from freely available cash is NOT (the about $675M is a 9/30 balance), and no motive is established.

Why no card:
1. **The owner's direction has no defined-risk instrument.** No puts exist. A short sale of a $3 stock with 38% short interest has unbounded loss and a squeeze path on the exact event BROCK names as the invalidator (a financing that leaves equity intact). Non-Negotiable #2 (defined loss) fails.
2. **The defined-risk instrument that does exist points the other way.** Long shares (max loss = the cost) is a bet that equity survives the financing, which is against the owner's read; Hard Boundary 3: I do not supply a direction. It would also be a call-side entry on a green tape (+1.0%), the wrong colour under root rule #6, with no measurement refuting the proxy.
3. **The notes** are the instrument the event actually prices, and they are not reachable or priceable here.
4. **Market reaction is small:** first session after the filing, the stock is up about 1% on thin volume after falling about 77% over 30 days (vendor 30-day range $2.96 to $15.38). Little left for a short to capture on the equity; the value now sits in the debt.

**Why waiting loses nothing:** no tradeable instrument exists for the owner's direction today or tomorrow. Clocks for the full read (BROCK's, partly INFERRED): grace ends about Wed 12/16; NYSE plan due about 12/28; MBI hearing 12/4 by press vs 11/13 in the 10-Q, unreconciled.

What would change it: listed options appear; a named public lender, BDC or other listed holder of the Cable One or MBI paper (BROCK KB-BRK-446 says no BDC holding is established); or a signed financing whose terms set an equity value.

### 3b. BROCK's liquidity follow-up (packet `2026-11-17_from-BROCK_cabo-liquidity-established-from-filings.md`, read 10:00 EST) — answer unchanged

BROCK, from the 10-Q (0001632127-26-000038) and 8-Ks: the $674.8M of 9/30 cash is borrowed (revolver $1.05B drawn at 9/30, the last $200.0M drawn 10/8, availability $0); $478.9M of it is claimed by the MBI put, held up by CoBank's restraining order; the issuer says its sources "will be insufficient" for its 2027 to 2028 maturities and uses Chapter 11 language; a 2030-notes default cross-defaults other debt; a delisting triggers the 2028 converts' put at par. BROCK corrects its morning "can pay, choosing not to": still a choice for this coupon only; for the company, reading (b), cannot meet its maturities without new financing. **Direction unchanged, severity higher.** Invalidation tests unchanged.

Effect on the trade read: **none on the verdict.** Higher severity strengthens the owner's direction, but the only instrument for it is still an unbounded short of a $17M market-value stock with 38% short interest, and a financing or restraining-order headline can still squeeze it. The converts' par put and the 2030 notes are where the severity is priced, and neither is reachable here. Still NO CARD, still no window lost by waiting.

## 4. Car-Mart — NO CARD (unchanged)

BROCK states "no new investment implication" with its reason (same standstill, shorter leash). The 13th bridge runs only to Wed 11/18 (8-K 0001171843-26-007505, accepted 11/17 08:00 ET; KB-BRK-501). Still no listed options, $0.95 stock, about $7.9M market value: a short has unbounded loss, a long is against the owner. 11/13 and 11/16 NO CARD basis stands. BROCK reads the follow-through Thu 11/19 AM; nothing on TERRY's side expires before that.

## 5. VIOLET handoff (PROME packet 2026-11-16 21:17 ET) — timing check only

Two windows do close before tomorrow's session: Nvidia reports tonight (Tue 11/17 after the close) and the November VIX contracts settle on Wed 11/18 morning. **Neither holds a card, so nothing tradeable is lost:**
- VIOLET states "no direction is forced"; PROME's packet asks for no pre-event card.
- Live at about 09:43 ET (vendor, 15 minutes delayed): VIX 22.83, VIX9D 23.32 (VIX9D/VIX 1.021, the event premium sits at the front, as VIOLET says), VIX3M 22.87, VVIX 111.02. Buying front-end vol now is paying for the event premium at its height, the case root rule #6's test exists to stop; selling it is not a defined-risk structure for this book.
- The Nvidia call-spread card (`IDEA-NVDA-CEOGAP-NOV12`, NOT approved) is a post-print card by design, window 11/18 to 11/20, so the print does not consume it. NVDA $155.96 (−0.1%, 09:58 vendor), $7.16 above the $148.80 invalidation low.
- Side read, QQQ 200-day card (`IDEA-QQQ-200D-NOV05`, NOT approved): T1 NOT MET at 09:58: VIX3M/VIX 1.002 but QQQ $662.15 +0.06%, not a red session. No grade beyond that.

The packet stays in the inbox for its own ask at the 11/18 session.

## 6. Inbox disposition

- Consumed and filed: `2026-11-17_from-BROCK_cabo-skipped-coupon-crmt-13th-bridge-trade-read.md` → `inbox/processed/`.
- Consumed and filed: `2026-11-17_from-BROCK_cabo-liquidity-established-from-filings.md` (arrived about 10:00; moved after BROCK committed it, bbe8d977b5) → `inbox/processed/`.
- Read for timing, left for 11/18: `2026-11-16_from-PROME_VIOLET-vol-handoff-nvda-soq-and-OTTO-turn-offer.md`.
- Left unread for 11/18 (ACTION lines checked: none due today): DAEDALUS ledger-sweep check E repaired; PROME outside-audit items; PROME postmortems thesis grades; PROME Will-word reconcile no-card report; PROME WQ-696 reader findings.

Gates, kill rules, bands and frozen predictions: none touched.

---

## 7. RE-LOOK 2026-11-17 12:39 EST — exposure chain (Will's question via PROME prome-19, 12:34 ET; BROCK 57fdb7b0ef)

**Written:** 2026-11-17 12:39 EST (from `date`) · TERRY, Claude Code, Claude Opus 5.5. Task words are PROME's, carrying Will's 12:34 ET question verbatim: *"okay did TERRY look into companies related to these two? Like maybe a chain that could lead somewhere? For example I know last year tricolor somehow daisey chained into Jeffries and into WAL."*
**Answer: NO CARD on any listed holder (`TRY-NOTRADE-CABO-CHAIN-NOV17`). No order. $0.** My re-open standard is met by its letter and fails in substance: a holder is now named, but none carries a loss that can move it, none of the small holders has listed options, and the holders that do have options are moving with their non-exposed peers today.

**Boot for this leg:** root `CLAUDE.md`, `AGENTS.md`, `USER.md`, `AGENTS/TERRY/CLAUDE.md`, `STATUS.md`, `RISK_RULES.md` read explicitly from the repo root (`/home/willi/Research-workspace`); no `AGENTS/TERRY/AGENTS.md` exists. `boot.py` ran: ledger sweep clean, BOARD 52 addressed and all logged, inbox 12 unprocessed (6 from 11/16 left on purpose, 6 today). Market data through `.venv` yfinance works. MCP servers mtnewswire and definite failed to connect (not needed). Bond prices, insurer holdings and CLO look-through: not reachable at zero cost.

### 7.1 Re-open standard, by its letter

My 09:59 standard (§3 above): *"a named public lender, BDC or other listed holder of the Cable One or MBI paper"*. BROCK now names them at EDGAR primaries (record `AGENTS/BROCK/research/2026-11-17_exposure-chain-cabo-crmt.md`). **Letter: MET.** It re-opens the read; it does not make a trade. Each listed holder, tested on my own rules:

| Holder (BROCK, filed date) | Exposure, latest filed mark | Share of holder | Already marked | Listed options (12:36 ET) | Live, 12:34–12:36 ET (vendor, screening) | Transmitting event and date | Verdict |
|---|---|---|---|---|---|---|---|
| abrdn Income Credit Strategies (ACP) | 2030 notes, 10.84M face, 4.03M value (37.2 cents), 7/31 | 0.60% of net assets | yes, from 69.7 at 4/30 to 37.2 at 7/31 | none (0 expiries) | 4.235, −0.59% | default after grace ends about Wed 12/16 (BROCK's count); daily NAV | NO CARD: most further loss is under 0.6% of NAV even at zero recovery, smaller than a normal day's move in a fund's discount; no defined-risk instrument; shorting a fund for it would have no limit on the loss (Non-Negotiable #2) |
| Brookfield Real Assets Income (RA) | MBI loan 4.53M (75.7) plus notes 0.55M (53.9), 6/30 | 0.65% | partly | none | 11.54, −0.77% | same, plus the MBI maturity 11/12/2027 or a restructuring | NO CARD, same reasons |
| John Hancock Investors Trust (JHI) | Term Loan B-4, 0.54M (83.4), 7/31 | 0.43% | partly; first lien, so recovery is real | none | 11.89, −0.59%; about 24,000 shares traded | default or Chapter 11 | NO CARD |
| BlackRock HYT, BLW, DSU, BTZ; John Hancock JHS | converts or notes, 0.05M to 1.32M each | 0.005% to 0.097% | yes (converts at 65) | none | −0.26% to −1.16% | delisting triggers the converts' put at par | NO CARD: immaterial |
| Blue Owl Capital Corp (OBDC) | look-through 3.08M of the MBI loan via Credit SLF (49.0), 9/30 | 0.044% of NAV | yes, about 3.20M already written down | 9 expiries; December puts are a dead strip (the one strike in ±10%: 10 put, bid 0.00 / ask 0.20, last trade 11/13) | 10.73, −1.05% | MBI restructuring; 12/31 marks in the 10-K, about late February | NO CARD: immaterial; the only listed instrument is unfillable |
| Blue Owl Technology Finance (OTF) | 0.38M look-through | 0.005% | yes | none | 9.31, −1.90% (its move today is not Cable One at 0.005%) | same | NO CARD |
| Citizens (CFG), the largest relative bank exposure | revolver, 79.8M on the 2023 allocation (about 99.7M if the 2024 upsize was pro rata, BROCK INFERRED) | 0.32% of equity at total loss; about 0.09% at a realistic first-lien loss (BROCK INFERRED) | no (a loan at cost), but the size is too small to matter | 11 expiries; December puts liquid (no quote defects, last trade 10:46 today) | 63.29, −1.78% | event of default, acceleration or Chapter 11; nonaccrual in Q4 results, January | NO CARD: immaterial, and a put today is a red-day entry (root rule #6) with no refuting measurement and no owner direction (REGINALD owns banks) |
| Fifth Third, Truist, U.S. Bancorp; JPM, BAC, WFC, TD, MUFG, BMO, Barclays | revolver, 2023 basis | 0.24% (FITB), 0.17% (TFC), 0.16% (USB), the rest far below 0.1% | no, but immaterial | yes | FITB −1.61%, TFC −1.54%, USB −1.26% | same | NO CARD |

**Negative control, same minutes (12:36–12:38 ET, vendor):** the revolver lenders are moving with banks that are not on Cable One's revolver: lenders CFG −1.78%, FITB −1.61%, TFC −1.54%, USB −1.26%; non-lenders KEY −1.63%, HBAN −1.89%, PNC −1.55%, ZION −1.64%, MTB −0.95%, RF −0.80%; KRE −1.01%, SPY −1.04%. Nothing in the tape singles out the exposed names. VIX 24.59 (+7.5%, vendor stamp 12:21). Today is red.

### 7.2 Will's question: is there a chain here like Tricolor to Jefferies and Western Alliance?

**Short answer: no, not on the record we have.** The 2025 episode had a shape that neither of these has, and the one place such a shape could still hide is narrow and cheap to check (Car-Mart's bank lines, §7.3).

**What actually happened in 2025, and what made it tradeable.** Event dates and loss figures below are TERRY's background knowledge of public reporting (September–October 2025) and the fleet's archived secondary (`AGENTS/OTTO/archive/research_retired_2026-11-11/outputs/RP-OTT-1.2/Warehouse_Lender_Exposure_Map.md`), **not re-read at a primary today**. The price moves are pulled live from the vendor's daily closes today (12:39 ET).
- It was two collapses and a third disclosure, joined by one fear, rather than a single daisy chain. **Tricolor** (subprime auto lender, collapsed about 9/10/2025; collateral allegedly pledged twice) cost its bank lenders on their own lines: JPMorgan's charge-off about 170M, Fifth Third's about 178M to 200M. **Jefferies'** hit came from a different company, **First Brands** (auto parts, bankrupt about 9/28/2025), through Point Bonita, a fund Jefferies' asset manager ran, with about 715M of First Brands receivables. **Western Alliance and Zions** disclosed separate alleged frauds by borrowers in their lending to investment funds on 10/16/2025. On the fleet record I have, Jefferies' exposure was First Brands, not Tricolor.
- **The first default moved nothing.** On Tricolor's collapse day, 9/10/2025: FITB +0.2%, JPM +0.9%, KRE +0.1%. The money was made on the later disclosures: JEF −7.9% on 10/8/2025 (Point Bonita), then on 10/16/2025 ZION −13.1%, WAL −10.8%, JEF −10.6%, FITB −6.0%, KRE −6.2%, against SPY −0.7%. JEF ran from 66.71 (9/26/2025) to 48.80 (10/16/2025), −26.8%.
- **Why it mattered: three things together.** (1) **Surprise, near-total losses on secured loans that banks held at full value.** Loans are not marked to market, so the loss arrived all at once at disclosure, and alleged fraud meant the collateral was not there. (2) **The financing route ran through banks:** warehouse, asset-based and receivables lines to nonbank lenders. That put the loss on listed balance sheets, and the market then asked what else sat in those books. For the large banks the dollar size was small against equity. The repricing came from that inference, repeated by three disclosures inside six weeks. (3) **Size against the holder** was decisive only for Jefferies, where the exposed fund was its own.

**Does anything on BROCK's record have that shape?**

| Feature that carried 2025 | Cable One | Car-Mart |
|---|---|---|
| Surprise | **No.** Stock −77% over 30 days before the skipped coupon; notes at 37 cents in July | **No.** Thirteen lender bridges, public since at least August (WALTER 8/28 standstill signal) |
| Near-total loss, alleged fraud | **No.** First-lien loans backed by a working cable network; no fraud alleged | **None alleged on the record.** First-lien loan on receivables, inventory and subsidiary equity |
| Held at full value, unmarked | **Mostly marked.** Funds mark daily or quarterly (37.2, 49.0, 75.7, 83.4); only the bank revolver sits at cost, and that is at most 0.32% of equity | Held by private funds (marks not public) |
| Financed through listed banks | Revolver only, at most 0.32% of the most exposed bank's equity at total loss | **Not on the record.** Lenders are private Silver Point and Beach Point funds |
| A lender whose loss invites "what else is in the book?" | No: Cable One is a cable company, not a lender | **Partly:** it is a subprime auto lender, like Tricolor, but the read-through is the subprime auto class (OTTO's), not a holder chain |

### 7.3 Where such a chain would sit if it exists — the NOT ESTABLISHED links, cheapest evidence, and whether it would change my answer

| Unknown link (BROCK) | Could it carry a 2025-shaped chain? | Cheapest evidence | Would it change my answer? |
|---|---|---|---|
| **Car-Mart: any bank revolving, warehouse or back-leverage line** (to Car-Mart, its ACM Auto Trust warehouse, or the Silver Point or Beach Point vehicles) | **Yes, this is exactly where Tricolor's losses sat** (bank lines to a subprime auto lender) | Car-Mart's latest 10-Q debt note, and the 8-K Items 1.01 and 1.02 around the 10/30/2025 refinancing (did the bank revolver end, and who lent?); free, EDGAR, under an hour. Back-leverage to the private funds is not public: stop there, as BROCK did | **Only if** a listed lender is named with an amount that is not trivial against its equity (above about 1%), or a filing alleges collateral irregularity. Otherwise no |
| Cable One: CLO holders of the term loans, and listed funds that own CLO equity (e.g. ECC, OXLC, OCCI) | Weakly. CLO equity is leveraged, but each CLO holds hundreds of loans and these are marked | Those funds' free quarterly materials, if they list top look-through borrowers | No. A single borrower inside a diversified, marked CLO pool cannot reach the size that moves a fund |
| Cable One: insurers' holdings of the notes and converts | No. The whole notes issue is about 503M and the converts 345M, spread across large balance sheets | NAIC Schedule D (paid; not used) | No |
| Cable One: current per-bank revolver amounts | No. The bound is already small (CFG about 0.4% at total loss even on the pro rata 2024 upsize, BROCK INFERRED) | Any forbearance or restructuring 8-K before about 12/16 will list lenders; nothing to commission | No |
| Fund holdings after 6/30 to 7/31 | No. Positions are under 0.7% and marked down | Next N-PORT filings | No |

**Recommendation for PROME and Will (a recommendation, not an action):** one read is worth commissioning, and it is cheap: **BROCK** (owner of the Car-Mart file), before Thu 11/19 08:00 ET: *"From Car-Mart's latest 10-Q and 10-K debt notes and its 8-Ks since 10/2025, does any listed bank or listed company provide or hold a revolving, warehouse or back-leverage facility to Car-Mart, its ACM Auto Trust warehouse, or the named Silver Point and Beach Point lending vehicles, and in what amount?"* No further read on Cable One is recommended. The subprime-auto class read-through from a Car-Mart failure belongs to OTTO, which already scores it (V9, red 4 at 11/13); a refresh is worth asking for only after the 11/18 outcome, and only if OTTO names a dated catalyst for a listed lender.

### 7.4 Car-Mart, briefly

The standstill ends Wed 11/18. Listed holder chain: **none established** (BROCK). CRMT 0.96, +3.2% (vendor 12:16 ET; the vendor's bid and ask are crossed, 1.45 / 0.96, so unusable), market value about 8.0M, 0 listed expiries. The outcomes are a fourteenth bridge, an acceleration (8-K Item 2.04), Chapter 11, or a sale. None gives a defined-risk instrument for either direction, and none transmits to a listed holder on the record. **NO CARD unchanged. No window lost by waiting:** BROCK reads the follow-through Thu 11/19 morning.

### 7.5 Packets that arrived today: anything closing before Wed 11/18?

| Packet | Window before Wed? | Disposition |
|---|---|---|
| BROCK exposure chain (this section) | n/a | consumed, filed to `processed/` |
| VULCAN chip rule before the Nvidia print | **Yes, tonight, but it is context for delivery 2, not a pre-print trade.** The rule takes effect 11/19, licences are case by case, the size is unknown, and US cloud buyers are exempt. NVDA 152.99 −2.02% at VULCAN's 12:04 pull; the NVDA card is post-print by design | held in the inbox with VULCAN's post-print packet; graded tonight |
| ZHAO, China's reply to the chip rule | No. Conditional threat, nothing named; ZHAO's dated triggers run 11/19 (meeting) to 11/27 (export-ban clause) | waits for 11/18 |
| CARL, October retail and import prices | No. CARL's horizon is 11/25 and 12/16; no implication from CARL's side | waits for 11/18 |
| REGINALD, Q3 bond losses | No. A 9/30 mark the market saw in October, with rates partly reversed; no implication from REGINALD | waits for 11/18 |
| REGINALD, REG-T-02 token renamed | No. Label only; my `REG-T-02_FIRE_PROCEDURE.md` line 62 follows at 11/18 | waits for 11/18 |
| Six 11/16 packets | No (checked at 09:59) | wait for 11/18 |

Gates, kill rules, bands and frozen predictions: none touched. Logged to `SIGNALS.tsv` `combo:credit-following` with its counterevidence.

### 7.6 BROCK's answer on Car-Mart's bank lines (81fd02ccfe; read 12:4x EST) — NO CARD and the answer to Will both STAND, strengthened

The one link with Tricolor's shape existed, and it closed a year ago. Car-Mart's BMO-led asset-based revolver ($350M; at 2/2025 BMO 58.0M, Axos 55.5M, MUFG 45.0M, BOKF 35.0M, Banc of California 47.5M, and others) was repaid in full ($162.9M) and terminated on 10/30/2025 (8-K Item 1.02, 11/5/2025). The 9/9/2026 10-Q says there is no warehouse or other financing now. No filing names a lender to the Silver Point or Beach Point vehicles: NOT ESTABLISHED, and not public, so it stays the one unseen link. The 7/30/2025 Item 4.02 was omitted loan-modification disclosures plus a control weakness, not a collateral allegation. **Neither re-open condition is met** (no listed lender above about 1% of equity; no collateral irregularity alleged). Re-opens only on a filing or lawsuit naming a listed lender to the private vehicles, or alleging missing or double-pledged collateral. Packet filed to `processed/` with delivery 2.

### 7.7 Fed Financial Stability Report (11/13), tradeability read on PROME's 13:2x ask — NO CARD, no existing card changes

**Read at:** BROCK KB-BRK-510 (2febcfa84b), which quotes the report text from the primary (federalreserve.gov FSR 20261113 PDF, extracted about 13:18 ET), plus WALTER SIG-W-20261117-014 and correction -017. Neither card has an action line naming TERRY (014 `action: ["BROCK"]`, 017 `action: []`), so no board_log row is owed. The PDF itself was not re-read by TERRY.

- **What it is:** a Fed staff synthesis and a survey of views, with no date attached to any loss. Its figures: "more than $680 billion" of advanced-computing debt issued by October 2026; the "close to $1 trillion" at the largest bank holding companies is *exposure* (to large tech firms, data center developers, SPEs, private credit vehicles and utilities), not a loss estimate; "riskier subordinated debt and equity tranches" are held by high-yield funds, life insurers, BDCs and private debt vehicles; private-credit defaults at "the upper end of its short historical distribution"; nontraded-BDC redemption requests "trended lower through the third quarter of 2026, though they remained elevated."
- **Nvidia card (`IDEA-NVDA-CEOGAP-NOV12`):** no change to its terms, trigger or invalidation. The card's do-not-trade line is about a disclosed liability, and this report discloses none for Nvidia. It is added as a counter-case line for Will at fire: the Fed names AI financing interlinkages as a vulnerability, and the risk survey's AI share rose from 50% to 87%. This is horizon context, months, against a card whose horizon is to Jan-15-2027.
- **Cable One and Car-Mart:** unrelated; not AI financing. Unchanged.
- **Credit names:** the HYG ×5 card (approved and fired, no fill known) is unchanged; the report supports its direction, but its void clock and terms are keyed to HY OAS, which this does not move. The ORCL put spread is unchanged; its T1 is a measured CDS level (≥ 350), and a staff warning is not that. BDC puts (OBDC, ARCC): NO CARD. The redemption line is counterevidence on the redemption leg, PIK and defaults point the other way, and none of it is a dated catalyst. Bank puts: NO CARD. The $1 trillion is gross exposure, mostly to investment-grade borrowers, and today is red (root rule #6).
- **Logged** to `SIGNALS.tsv` `combo:credit-following` with its counterevidence. Logging is not scoring.

### 7.8 Golub Capital BDC (GBDC) fiscal Q4 print, tradeability read on PROME's 16:0x ask — NO CARD

**Read at:** BROCK KB-BRK-513 (0d61ac9740; GBDC 8-K 0001476765-26-000083, accepted 11/17 16:04:28 ET, Ex 99.1, read by BROCK at the SEC primary). PROME re-checked NAV and NII at the SEC; the −$0.24 realized/unrealized and the rating-3 share are BROCK's, not re-checked by PROME or TERRY. This read was made from BROCK's committed KB row at 16:11 ET; BROCK's WQ-696 packet (6c1f02582e, committed 16:10:43) was read at 16:46 ET and agrees: "no supported investment implication", a slow credit drift at a software-heavy book (software 57.6% of NAV at 6/30, KB-BRK-363), not a break; its re-open conditions (a second quarter of rating-3 growth with NII below the distribution, or a cut; non-accruals materially above peers; a NAV markdown above 5%) match §7.8's.

| Fact | Value | Source |
|---|---|---|
| NAV per share | $14.00 at 9/30 vs $14.25 at 6/30 (−1.75%) | Ex 99.1 via KB-BRK-513 |
| NII vs distribution | GAAP $0.32 (0.97x), adjusted $0.33 (1.00x) vs $0.33 paid | same |
| Net realized/unrealized | −$0.24 per share, tied to non-accrual names | same |
| Rating 3 (below expectations) | 12.2% of fair value from 10.6% | same |
| Leverage | net debt/equity 1.17x | same |
| GBDC close 11/17 | $12.08, −2.58% (prev $12.40), 16:00 ET, before the 16:04 release; volume 1.59M vs 1.31M average | yfinance, pulled 16:10 ET |
| Price / new NAV | 12.08 / 14.00 = 0.863x (13.7% discount) | computed |
| Peers 11/17 close | BIZD −1.38%, OBDC −1.74%, ARCC −1.05%, FSK −3.58%, BXSL −1.92% | yfinance, 16:10 ET |
| GBDC options | 4 expiries (11/20, 12/18, 2/19, 5/21). Dec 18: one put strike inside ±15% of spot, the 12.50P, bid 0.50 / ask 0.90, 57% spread, OI 66, last trade 13:41 | chain_fetch.py --no-cache 16:10 ET, screening marks only (finding 5b) |

**Verdict: NO CARD.**
1. **No trigger.** −1.75% is one name, below every rung of BROCK's ladder (5% row, not fired). No BROCK score moved.
2. **Already priced, before the print.** The stock closed at 0.86x the *new* NAV ahead of the release; the markdown is 1.75%, the discount is 13.7%. A put needs the discount to widen further, and the mark-down is not evidence it will.
3. **The dividend held.** Adjusted NII covers the $0.33 at 1.00x and the next $0.33 is declared (11/12). A cut is the catalyst that would move the stock, and this print does not show one.
4. **Untradeable structure.** The Dec chain is one usable strike at a 57% spread on OI 66. Non-Negotiable #2 (defined loss) can be met, but the spread alone eats about a third of the premium, and there is no second strike to build a spread.
5. **The Fed report does not change it** (§7.7). Its nontraded-BDC redemption line "trended lower through the third quarter" is counterevidence on the redemption leg; its PIK and default lines point the same way as the rating-3 drift, but neither is dated.
6. **Root rule #6:** any put would be bought Wednesday; that day's colour is unknown, and no card means no break test is needed.

**Re-opens on:** a distribution cut or NII below 0.95x in the 10-K, or non-accruals above about 5% of cost when the earnings presentation or the 10-K is read. The call is Wed 11/18 10:00 ET. Logged to `combo:credit-following`.
