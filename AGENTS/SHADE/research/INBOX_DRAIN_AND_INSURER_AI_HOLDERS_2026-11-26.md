# SHADE — inbox drain 24 → 0 and "do insurers show up as holders?" — 2026-11-26

**Session:** PROME prome-80 launch on Will's word (Thanksgiving, NYSE closed), Claude Code, Opus 5.5. Written 2026-11-26T12:16:38-05:00 onward. $0. No score, band, gate, threshold or trade permission changed.

**Primary source used throughout:** Athene Annuity and Life Company (AAIA) Q3 2026 statutory statement, the PDF fetched 11/20 (sha256 `7e6abafb611fcf85…`, 4,450 pp) and its pymupdf text extract (same scratch folder as the 11/20 session). Line numbers below are lines of that text extract. A quarterly statement shows only the quarter's TRANSACTIONS (Schedule D Part 3 acquisitions, Part 4 disposals, Schedule BA Parts 2 and 3) plus Schedule Y; the held book is not in it. Every "not shown" below is scoped to that slice.

## 1. The question PROME asked

> In the setting of HY at 372 bp [FRED 11/24], broad BB and B widening, AI-infrastructure credit as the sharpest spot, and Fitch's 11/16 nonbank mortgage negatives: do life insurers and their private-credit affiliates show up as holders, lenders or marks, on evidence I can read?

| Channel | Answer | Evidence |
|---|---|---|
| **AI-infrastructure credit** | **YES, as a buyer, at primary, and buying in Q3** | §2 |
| **The SpaceX $44B GPU notes (Saturn Funding Trust)** | **The issuer's parent is an Apollo-group entity listed in Athene's own Schedule Y. Athene holding the notes: NOT SHOWN** (priced 11/20, after the Q3 statement) | §3 |
| **CoreWeave $4.5B Meta-contract loan** | **NOT SHOWN.** No CoreWeave line in AAIA Q3 transactions; the loan has not been sold yet (WALTER 20261125-031/-035) | grep, 0 hits |
| **Nonbank mortgage lenders** | **An Apollo-group warehouse entity lends to loanDepot; AAIA held $196.5M of Atlas warehouse funding notes, redeemed 9/24. Pennymac, Planet, Freedom (Fitch negatives): NOT SHOWN** | §4 |
| **Marks from the HY widening** | **NOT SHOWN, and not expected in statutory capital from spreads alone.** Statutory bonds carry at amortized cost by NAIC designation; spread widening hits capital only through designation migration or impairment. The exposure sits in the sub-IG AI tranches (NAIC 3.B) | §2 |

## 2. AI-infrastructure credit in AAIA's Q3 transactions (PRIMARY)

| Line | Holding | Q3 event | Par / amount | NAIC | Affiliated |
|---|---|---|---:|---|---|
| 408737 | SVF II Tsubaki (DE) LLC, SoftBank Group Corp, 6.511% 8/7/28 | bought 8/25, "Various" | **$1,032.5M** par (cost $1,019.6M) | 2.C **Z** | no |
| 408765 | SVF II Finco Cayman LP B4, 7.833% 4/25/29 | bought 9/23, Direct | **$922.8M** | 1.G **Z** | no (fund-issued subtotal) |
| 408533–34 | Space Exploration Technologies senior unsecured 5.35% 2031, 5.65% 2033 | bought 8/20 and 9/15 | **$198.8M** par | 2.A FE | no |
| 408363 | Meta Platforms 4.55% 2031 | bought 9/11, Citadel | $30.0M | 1.D FE | no |
| 408744–50 | AP Compute Financing 2026, A-1RR $22.7M (1.F Z), A-2 $116.6M (1.F PL), Class B sub 8.5% $21.1M (**3.B** PL) | bought 9/22 and 9/28 | **$160.4M** | as shown | **yes** |
| 408752–55 | Big Sky Funding LLC sub secured notes B, 8.5% 2035 | bought 9/22 and 9/28 | **$62.2M** | **3.B** FE | **yes** |
| 412601 | VCI Asset Holdings 1, "xAI/ Valor I", term loan 10.0% 11/20/30 | redemption 8/25 | $11.9M repaid | **3.B** PL | no |
| 412607 | VCI Asset Holdings 2, "xAI/Valor II", 7.375% 2/18/31 | redemption 8/31 | $39.0M repaid | 2.B PL | no |
| 412610 | VCI Asset Holdings 3, "xAI/Valor III", 6.875% 4/24/31 | redemption 7/27 | $52.9M repaid | 2.A FE | no |
| 412883–413021 | SVF II Finco Cayman (older tranches) | paydowns and basis adjustments 9/18–9/25 | paydowns $78.7M | 1.F PL | no |

- **SoftBank-linked Q3 purchases $1,955.3M par in two lines, both designation "Z"** (Z = no NAIC designation yet filed; INFERRED from the P&P symbol convention, not re-read today). This is the line that grew +$1,033M in Q3 in Athene's 10-Q (11/6 read).
- **xAI-labelled GPU loans (Valor/VCI) are held at AAIA.** The quarter shows repayments only, so the balance is not shown. VCI 1 carries NAIC 3.B (high-yield equivalent) at 10%.
- **Apollo-affiliated compute financings carry sub-IG subordinated slices (3.B)** — AP Compute Class B and Big Sky Class B, $83.3M bought in Q3.
- Names searched with **zero** hits in the whole text: CoreWeave, Nvidia, Applied Digital, Nebius, Lambda, Crusoe, Anthropic, Beignet, Solera, Car-Mart/ACMAT, loanDepot, Pennymac, Freedom Mortgage, Planet Home.
- **11/18 open question (Athene $2.4B "xAI" per Moody's via NYT vs "Oracle-linked" per my 11/6 read):** both exist. xAI-labelled loans are on AAIA's books (above); the Oracle $2.4B is the deck's total. The xAI balance is still not shown. Not settled; the FY2026 annual Schedule D Part 1 settles it (~2027-03-01).

## 3. Saturn Funding Trust (the SpaceX GPU notes) and WHCO

| Point | Basis |
|---|---|
| Saturn Funding Trust is "an indirect wholly owned subsidiary of WHCO Intermediate Holdings LP (WHCO) ... an existing third-party asset-backed lending entity unaffiliated with Space Exploration Technologies Corp."; preliminary A-, Stable on ~$27.2B A-2/A-3 and $2.4B B | **KBRA release 11/16, read 11/26** (kbra.com/publications/McYcSQYT). No Apollo, Athene or guarantee named on that page |
| **WHCO INTERMEDIATE HOLDINGS LP** (DE), managed by WHCO ADVISORS GP, LTD., ultimate controlling party "AGM; M. Rowan; L. Black" | **AAIA Q3 Schedule Y, line 50787** (with ~30 other WHCO entities, lines 42746–51858) |
| WHCO Investments (Cayman) Parent LP Form D/A 1/28/2026: directors Alec Burger, Michael Goekjian, Geoffrey Symonds; address c/o WHCO Advisors GP, 9 West 57th Street; $150M sold, pooled fund | SEC EDGAR, read 11/26 |
| Pricing: about $44B notes priced 11/20; A3 $25.168B at 8.259% | WALTER 20261123-012 (Apollo release read by WALTER; IFR/Bloomberg via helper). Not re-read by me |

**Reading.** KBRA's "third-party" means third party to SpaceX. On Athene's own filing WHCO is an Apollo-group affiliate. ⚠️ Schedule Y lists the whole Apollo control group; being listed there shows **common control, not Athene capital**: WHCO's management line carries 0.000% ownership. **Whether Athene buys Saturn notes, and how much, is NOT SHOWN.** The 11/6 read records a separate AHL guarantee of 15% of a "WHCO" purchase obligation on the Q2 Broadcom/Anthropic deal (Apollo Q2 10-Q Note 17). I have not established that it is the same WHCO entity, or that any guarantee touches Saturn. Do not merge the two.

## 4. Nonbank mortgage: Atlas SP / WHCO

| Point | Basis |
|---|---|
| Master Repurchase Agreement among **Atlas Securitized Products, L.P.** (agent and buyer), **AGF WHCO 1-A3 LP** (buyer) and loanDepot.com, LLC; dated 11/14/2024, Amendment No. 4 dated 7/7/2026 | loanDepot 10-Q exhibit 10.6, filed 8/6/2026, read at SEC 11/26 |
| AGF WHCO 1-A3 LP sits in AAIA's Schedule Y (line 42898) under WHCO ADVISORS GP, LLC | AAIA Q3 |
| AAIA held **Atlas Securitized Products Funding 1** notes A1A and A1B, 5.413% 2063, **$196.5M redeemed 9/24/2026** (NAIC 1.C PL / 1.F PL) | AAIA Q3 Sch D Part 4, lines 434284–87 |

**Reading.** The Apollo group is a warehouse lender to at least one nonbank mortgage company, and Athene's general account has funded Atlas warehouse notes. The underlying collateral of the Atlas Funding notes and any lending to Pennymac, Planet or Freedom are NOT SHOWN. loanDepot is not among the three Fitch negatives as relayed (WALTER 20261124-019, from HOMER's read).

## 5. `T-SHADE-01` fresh read (endpoint 11/25 close)

| Leg | Reading | Basis |
|---|---|---|
| Level | **MET**: HY 372 [11/24 first-published], no session ≤280 since the 9/24 anchor (11/10–11/24 cells 334–376) | LIQUID STATUS L8 at commit 7cab526137, read 11/26; FRED via `fetch.py` agrees (3.72, 11/24) |
| Sign, primary window 9/24 → 11/25 | RAW wrappers **−0.37%**, managers **+5.67%** ⇒ **wrappers down, managers up**. ADJ wrappers +1.22%, managers +5.91% | `L673_CLOSES_END_2026-11-25_read2026-11-26.json` |
| Sign, since-last-read 11/10 → 11/25 (diagnostic, cannot grade) | RAW −2.89% vs −2.88%, both down, wrappers more by 0.01pp | same |

**Grade: NONE.** The primary reading sits in the one branch the charter says the 10/12 amendment "does not adjudicate" (wrappers down / managers up). It is not MET under the letter's MET example (both down, wrappers more) and not NOT MET under its examples. **I stop on this item and flag it to PROME: the letter has no ruling for the branch the reading is now in.** No dig (standing rule: no dig absent a qualifying trigger). ⚠️ On a dividend-adjusted basis the wrappers are UP 1.22%: the RAW decline is distributions, not re-marking, which is the opposite of the collateral re-marking the leg exists to catch.

**HY environment band (charter §Thresholds, a description, not a trigger): RED (>350) on every published session since 11/19** (352, 376, 363, 372). It read YELLOW on STATUS since 11/9 at 334.

## 6. Forward view (material item: Athene buying AI-infrastructure credit into a widening tape)

- **Expect:** the AI-infrastructure credit at Athene shows up first as NAIC designation pressure on the sub-IG slices (VCI 1 at 3.B, AP Compute B and Big Sky B at 3.B) and in Saturn note allocations, not as realized losses. Horizon: FY2026 annual statement, ~2027-03-01.
- **Why:** the senior pieces are lease-backed and IG-designated; the lessees (SpaceX, Anthropic, SoftBank-backed vehicles) are performing; statutory accounting does not mark spreads.
- **Meaningful alternative:** a lessee or GPU-residual shock (posted H100 rents disputed: Silicon Data $3.09 vs Ornn $2.92, WALTER 20261123-012) pushes a 3.B slice to NAIC 4 or non-accrual. P(any named AI-compute holding above at NAIC 4+ or non-accruing in the FY2026 annual) ≈ 10%, unscored, not registered (the question is not yet a clean resolvable letter).
- **What would change my mind:** Saturn's lease failing to close by year end; a KBRA action on Saturn; a SpaceX or SoftBank downgrade; AAIA's FY2026 Schedule D Part 1 showing Saturn notes in size or the Z designations landing below 2.

## 7. Inbox dispositions (24)

See `board_log.tsv` rows stamped this session. SHADE-lane items: 20261123-007 item 8 (Delaware Life $1.2B further swap = already in §0y; Cayman reinsurers challenge NAIC recapture charge = new, title only), 20261123-012 (Saturn, §3), 20261123-011 item 3 (Arbol GPU residual cover, no capacity), 20261124-016 (once-AAA SASB CMBS total loss projected; holders not named), 20261125-026 (Solera holders include Apollo and Ares, insurer balance sheet not named), 20261125-034 item 8 (Walter 36% of Guggenheim's parent, title only; ownership, not ladder rung 6). Corrections COR-20261123-12, -13 and COR-20261124-21 receipted NO-OP.

## 8. DOCKET rows naming SHADE

- **Line 183 (W3, grades 11/30, BROCK lead):** BROCK grades; SHADE consumes the owner result. Nothing to do today.
- **Line 784 (12/04, CORAL lead):** SHADE's insurer bond-holder cell was delivered 10/29 and closed. DR-4956-FL (declared 11/24, WALTER 20261125-019) changes nothing in it. Nothing owed.
