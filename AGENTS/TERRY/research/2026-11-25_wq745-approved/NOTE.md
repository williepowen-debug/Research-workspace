# TERRY note — WQ-745 approval encoded; midday inbox drain (2026-11-25)

**Written:** 2026-11-25 from 13:16 EST (`date`), TERRY, Claude Code, Claude Opus 5.5, laptop; launched by PROME prome-77 at about 13:16 ET to encode WQ-745 A. **NO ORDER. $0. No new card. No card term changed.** Every price is a vendor screen (`fetch.py`, `chain_fetch.py --no-cache`), not a fill (durable finding 5b; root rule #4).

## 1. WQ-745 A encoded (root rule #10: proposal, decision, record)

| Item | Value |
|---|---|
| Ruling | Will in PROME's chat 2026-11-25 13:15 ET, verbatim *"745 A, 746 yes launch CREED"*; record `PROME/proposals/2026-11-25_wq745-746-RULED.md` |
| What is approved | `IDEA-CRWV-AIFIN-NOV24` AS WRITTEN, NOT-FIRED; **X1 passed for this card only by Will**. Not an order, not a fill. A changed level, operator, instrument or consequence is a new ask |
| Surfaces | card header, §0, new §8d, §9 box · `SETUPS.tsv` (rotated first: 5 terminal rows, crc32 `27d7460b`, 4,334 B, to `archive/SETUPS_ARCHIVE_2026-11-25.tsv`) · `setups/INDEX.md` · `TRADE_BOOK.md` · `CARD_LEDGER.tsv` · `STATUS.md` |
| Entry, as the card carries it | (a) regular-session CRWV close **≥ $48.00** on a **green** session AND (b) LIQUID's latest CoreWeave 5Y CDS read, dated no more than 2 sessions before the entry, **≥ 1,200 bp**; any session through **Fri 2026-12-11**; one complex order, **≤ $3.25** net debit, ×1, max loss **$326.30**; earnings date read from CoreWeave IR first |
| Do not trade / kill, as the card carries it | Do NOT trade if the roughly $4B IG loan launches and prices, LIQUID's CDS read is **under 1,000 bp**, or the broker debit is above $3.25. After entry: CDS **under 1,000 bp**, the loan prices, or a CRWV close **≥ $60.00** |
| Wording reconciliation | WQ-745 row: "if the debt-insurance cost falls under 10% a year". 10% a year = 1,000 bp: the same level. **The card's bp wording governs**; the row's words are its plain conversion |
| Basis | The card's lines were set on LIQUID's **clean** column (1,314 [11/24], 1,078 [11/18] are clean figures). LIQUID headlines **dirty** from 11/25 (about +45 bp at CoreWeave's level: 1,359 vs 1,314 [11/24]). TERRY grades both lines on clean, quotes dirty beside it; a straddle is decided by clean (entry not met / kill fires) and both figures go to PROME. Today both bases are far from both lines: no state change. This names the basis; it moves no level, operator, instrument or consequence. If PROME reads it as a term change, it goes to Will |

## 2. Live state at encoding (13:18–13:21 EST, vendor)

| Item | Read |
|---|---|
| CRWV | **$40.96, −3.86%** (red day): today cannot trigger; a green $48.00 close needs **+17.2%** |
| Feb-19 40P / 30P | 8.60/8.75 · 4.25/4.40 ⇒ **mid $4.35, outer $4.50 vs the $3.25 cap**; IV 117.5% / 129.4% (09:47: 111.7% / 123.1%); OI 10,634 / 6,802 |
| Model at the trigger (Black-Scholes, today's IVs, 4% rate; not a broker Greek) | **$3.23 at $48** (86 DTE); $3.08 if IV eases ten points; $3.49 at $46. The cap and the trigger still agree, with almost no margin if IV stays here |
| Leg (b) | LIQUID's last valid 5Y read **1,314 clean / 1,359 dirty [11/24 close]**; the 11/25 07:56 ET 5Y print (1,363 / 1,410) was CANCELLED by its reporter (SIG-W-20261125-022; COR-20261125-22). 4Y 1,379 / 1,429 [11/25 08:20 ET] stands; LIQUID's INFERRED 5Y today about 1,450–1,500 (one trade, not a reading) |
| Cash bonds (secondary) | CoreWeave Oct-2031 notes 74.23, 17.91%; June-2030 76.55, a record low (Tradeweb via Reuters relay, SIG-W-20261125-024). Same name, not independent confirmation |
| Earnings date | unannounced at the 09:4x check (FY25 Q4 precedent: reported 2026-02-26, announced 2026-02-05) |

**Before any order, PROME arranges:** (1) a LIQUID CoreWeave 5Y read no more than 2 sessions old (the 11/25 DTCC full file posts about 20:15 ET tonight and is good for an entry through Mon 11/30; a 11/27 read through 12/1); (2) the earnings date read at CoreWeave IR. Then TERRY re-prices on the **broker** chain on a green ≥ $48.00 close. **No entry on the Fri 11/27 half-session: confirmed** (thin holiday book; TERRY's narrower entry, never a wider one). By count the 11/24 read would still cover 11/27; that is moot.

**Forward view (unscored; CAL-0010 stays 0.40 as registered):** about 0.20 that T1 completes by 12/11, and if it does the cap is roughly a coin flip at today's IVs. Most likely outcome, about 80%: the card lapses unused at the 12/11 close. What would change it: a short-covering rally of the 11/23 kind (+22% in a session) while the swaps stay wide, which is the very combination the card waits for; or the $4B loan pricing, which kills it.

## 3. Inbox drain (packets landed since 09:55 ET; every sender)

| # | Packet | Answer | Why, in one line | What would change it |
|---|---|---|---|---|
| 1 | LIQUID 11:49 — CoreWeave 5Y correction (1,363 cancelled; dirty headline) | **ENCODED; NO NEW CARD** | It is leg (b) of the approved card; basis handled in §1 | A fresh LIQUID read (tonight's file) |
| 2 | LIQUID 09:58 — CDS reading + TRY-FIRE-004 grade | **GRADE RECORDED; NO CARD** | MIXED, LIQUID's share; recorded in `POSTMORTEMS.md` owner-grades table: **9 of 12**; still owed WAL, BOND, DEWEY, PROME (ORCL). The single-name vs index credit gap is already expressed by the CRWV card and HYG ×5 | — |
| 3 | PROME 10:22 — HY 11/24 cell 372 | **VIX leg: condition met, NO BUILD TODAY** | 372 [11/24] verified at FRED 13:22 EST. But VIX $29.38 **+11.46%** (13:21), and Dec-16 30/40C 30C 2.03/2.10, 40C 1.07/1.12 ⇒ mid $0.97, **outer $1.03 vs $0.89 [11/24 after hours], +16%**: paying up for convexity by direct measurement, so the root-rule-#6 test argues against a same-day build. VIOLET's lasting tell (VIX close ≥ 31 with HY ≥ 370) is not met at 29.38 | A VIX-down session with HY still ≥ 370; earliest TERRY build Mon 11/30 (no build on the 11/27 half-session either). A build is a new card to Will |
| 4 | PROME 12:52 — personal email in GATE-TERRY-007 procedure | **DONE** | Line 25 address replaced by `<declared contact>`; nothing else changed; commit `05c8cde220`. No other TERRY file carries the address (grep). History not rewritten | — |
| 5 | AEOLUS — FL rain, CA record tides | **NO CARD** | Rain flood falls on NFIP and the uninsured; not a named storm; tidal flood excluded from HO and FAIR Plan cover | A named storm on a credible FL/Gulf track |
| 6 | BRENT — EIA week 11/20, Gulf | **NO CARD** | Energy arm retired (8/7, WQ-192); the premium sits in the expiring January contract; no barrel lost; last re-bid faded 3.5% in two days | Arm reopened by Will plus a confirmed Yanbu/Ras Tanura loss |
| 7 | BROCK — alt managers are beta | **NO CARD** | Residuals vs RSP within 1.5 sigma; one common factor, not five signals | Manager residuals below −2 sigma on two sessions with chips flat; BDCs −3% beta-adjusted |
| 8 | CORAL — DR-4956-FL confirmed | **NO CARD** | A permission, not money; NFIP $4.84M paid; bank rail not armed | CORAL's listed tells (association assessment at a FL bank; BKU CRE to 90+ days) |
| 9 | HENRY — 7,000 pin, PCE split | **NO CARD** | Index puts on a red day at this VIX is paying up (morning answer stands); the pin expires at today's close; HY 372 noted | A close under 7,037 with vol not dearer than realised (HENRY's frame) |
| 10 | HOMER 13:13 — FHA foreclosure growth | **NO CARD** | Exposure question only; HOMER sized no issuer cost and holds no covenant breach or draw, so there is no measured loss to put a listed servicer (Pennymac is the listed name of the three Fitch moved) against; issuer credit is REGINALD's | REGINALD naming a listed servicer with a measured advance or covenant strain |
| 11 | ISHM — durables, G.17, Deere | **NO CARD** | No ISHM letter fires; equipment demand rising | ISM < 47 or R1 on 12/1 |
| 12 | VULCAN — 301 China correction, export headline | **NO CARD** | China leg at most about $5.3B a year, mostly not AI hardware; the export rule is a re-report | A final Taiwan notice dropping the exemption (not before 1/25); an NT 10-Q at Nvidia |
| 13 | WATT — power selloff is equity, not demand | **NO CARD** | No demand event; no measured mispricing; no entry edge | A named ≥ 1 GW cancellation, or BRA at cap 12/22 with the record unchanged |
| 14 | ZHAO — s.301 China, 46号, Chen Jining | **NO CARD** | Nothing in force before late January; China level matches the truce | A 40% branch or numbered countermeasure; a minerals lapse |
| 15 | VIOLET 09:52 — VIX 7th inversion | **answered this morning** (`research/2026-11-25_morning-tradeability/NOTE.md` row 11); filed now that VIOLET committed it (d288b95909) | — | — |

SAM's packet named in PROME's brief was answered and filed this morning (`inbox/processed/2026-11-25_from-SAM_softbank-ltv-at-25-line.md`). Small items appended to `SIGNALS.tsv` COMBO-CREDIT-FOLLOWING (WQ-622; logging is not scoring).

**BOARD:** scan run, 2 new since SIG-W-20261125-013, 2 logged (-022, -024). COR-20261125-22 receipted APPLIED (card §8d).
