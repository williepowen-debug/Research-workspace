# TERRY: 60-day review of "no card" verdicts, by reason (2026-09-17 to 2026-11-16)

**Written:** 2026-11-16, 13:48 to 13:5x EST (clock from `date`: commission 13:48, prices 13:51, packet 13:53). **Desk:** TERRY, Claude Code, Claude Opus 5.5. **Commission:** PROME prome-6f on Will's word (PROME's chat 13:45 ET, verbatim "Id like to go back to your findings and start working on these"), packet `inbox/processed/2026-11-16_from-PROME_commission-60-day-no-card-review-by-reason.md`. **Limits:** one bounded pass; no trade, no card and no rule change come out of it. Data: `verdicts.tsv` beside this file (one row per verdict, with source and my words at the time).

## Five lines for Will first

1. **95 "no card" verdicts in 60 days.** By what stopped them: my own judgment about the evidence, 36 (too thin 22, already priced 10, doubles a held position 4). No desk owned a direction, 20. No listed instrument, 14. A card's trigger not met or your decision, 18. The hard rules were the main reason on only 6: debit caps, the red-day/green-day rule (root rule #6) and the $500 / sizing gate. Other, 1.
2. **The largest single stopper is structural: no desk owned a direction (20, 21%).** My charter forbids me from originating a thesis (TERRY Hard Boundary 3, set by Will at creation), so a strong finding with no directional owner ends at no card. That is a rule doing the stopping. Whether to change it is your call.
3. **No listed instrument (14, 15%).** Many of the fleet's strongest findings were about private or illiquid names: United Fidelity, Car-Mart, Cable One, Exeter, SoftBank, N-able. No reworking of construction rules fixes that.
4. **Cards that existed but did not fire (12, 13%), plus 6 you declined, passed or shelved.** Two built cards had their triggers met and were stopped only by my debit cap: FXY on 10/23 (debit 0.925 vs 0.90 cap) and IEF on 10/23 (0.975 vs 0.85). The open QQQ 200-day card (not counted here; still live) has had its trigger met on three sessions and failed its $4.90 cap each time.
5. **Context, not scoring.** Of 15 names priced afterwards, the passes on CCL and NCLH puts were right (both up 25 to 32%). Four bear ideas did fall 10 to 19%: Nebius, CoreWeave, Cable One and Arbor. Three of those were stopped by having no defined-loss instrument or by being a chase; CoreWeave voided on its own line before firing.

## 1. Population and how it was counted

- **Sources read:** `SETUPS.tsv` and every `archive/SETUPS_ARCHIVE_*.tsv` plus `archive/SETUPS_ENTRY_HISTORY_2026-10-19.tsv` (rows dated 9/17 to 11/16, and older rows whose terminal verdict fell in the window). Also the research notes holding multi-item no-card tables: `2026-10-15_fleet-trade-idea-sweep`, `2026-10-15_TLT-bounce`, `2026-10-31_trade-ideas`, `2026-11-08_wq650-pass`, `2026-11-10_hy-cpi-read` §4, `2026-11-11_inbox-drain-reads`, `2026-11-16_henry-close-and-inbox` §1, §3, §6, §8 to §10, and the United Fidelity re-look.
- **Unit:** one verdict = one instrument question answered "no card" in a dated record. Bundled ledger rows were split into their items (for example the 11/11 drain row is three items, JETS, UNG and KRE). Re-looks of the same question count again (USD/JPY 11/12 and 11/13; United Fidelity 11/12 and 11/16; Car-Mart 11/13 and 11/16). Without re-looks the count is about 90.
- **Included:** NO TRADE / NO CARD, SHELVED, DEAD (voided), LAPSED UNFIRED, and cards Will declined, passed or ended unfilled.
- **Excluded, with reason:**
  - Management, exit and roll cards on held positions (all `MGMT-*`, `TRY-EXIT-*`, `TRY-WAL-ROLL70`, `TRY-BRENT-REFINER`). These are dispositions of trades already on, not no-card verdicts.
  - Cards still live: ORCL put spread (approved, not fired), HYG ×5 (approved, fired, no fill known), QQQ 200-day (not fired), NVDA post-print (not fired).
  - Card-state re-reads that are not new verdicts (the NVDA do-not-trade line reads, HENRY's item list where it only fed the QQQ card).
  - Day-trading review (separate sub-desk).
  - Shelf re-look rows in the 10/31 note (RSP, VST, IEF), which were revival candidates for your word, not new verdicts.
- **Could not recover:**
  - Verdicts given only in chat and never filed.
  - A separate pass over `TRADE_BOOK.md` and its archives and over `archive/STATUS_ARCHIVE_*`: not done in the time box. SETUPS carries the same ids for cards, so the risk is chat-only or STATUS-only no-card items.
  - 9/17 to 10/11 is thin: two verdicts. My records show that period spent mostly on held-line management (expiries, rolls), and the 10/12 desk sweep proposed little new.
- **Primary reason:** taken from my own words at the time (the ledger's `entry_trigger`/notes cell or the note's "why" column). Where I listed several reasons, the first or the decisive one is primary. Some calls are judgment (marked in `verdicts.tsv`). Classes added: **J** (card built; Will declined, passed or shelved it) and **K** (duplicates exposure the book already holds).

## 2. The table

| Class | Count | Share | Examples (date, item) |
|---|---:|---:|---|
| H. Thesis or evidence too weak (incl. measured no edge) | 22 | 23.2% | CCL puts, negative EV on 8 prints (9/19) · TLT short on refunding, trigger 0 of 34 (11/5) · bank-name puts, REGINALD score no skill (11/8) |
| E. No directional owner, or the finding named no direction | 20 | 21.1% | QQQ under its 680 put wall (11/13) · crude short on the EIA build, BRENT WAIT (11/12) · BX/OWL/APO on BCRED and Monroe (11/16) |
| A. No listed instrument, or options too thin to quote | 14 | 14.7% | United Fidelity (11/12, 11/16) · Car-Mart, 0 expiries (11/13, 11/16) · SoftBank, SFTBY no options (11/10) |
| D. Trigger not met, or window lapsed unfired | 12 | 12.6% | HYG/HTGC credit puts lapsed, REG-T-04 never fired (11/13) · CRWV rally fade voided (10/22) · OKTA calls, no 8-K Item 1.05 (10/29) |
| F. Already priced or anticipated | 10 | 10.5% | MRNA ESMO, chain priced the readout (10/22) · Nebius after −20% (11/12) · HBAN Category III, Fitch already cut (11/16) |
| J. Card built; Will declined, passed or shelved (added class) | 6 | 6.3% | TLT QRA put spread, WQ-592 B (11/4) · RSP call spread declined (11/6) · VST shelved (10/29) |
| K. Duplicates exposure the book already holds (added class) | 4 | 4.2% | oil right tail into the reopen, book already long oil (11/8) · more Nasdaq downside, same falsifier as held QQQ puts (10/31) · FLG puts, same bank falsifier (10/15) |
| B. Price or debit cap failed | 2 | 2.1% | FXY Jan 58/60C, 0.925 vs 0.90 (10/23) · IEF Jan 90/92C, 0.975 vs 0.85 (10/23) |
| C. Red-day / green-day rule (root rule #6) | 2 | 2.1% | FLG Jul-27 10P on a gap-down red day (10/23) · S&P back over its gamma flip, a call on a green day (11/12) |
| G. X1 sizing gate or the $500 default | 2 | 2.1% | MPC opening $611 vs $500 (10/12) · more KRE, LIQUID X1 DON'T-SIZE (10/15) |
| I. Other | 1 | 1.1% | BNO crude long, book weights unknown (10/12) |
| **Total** | **95** | **100%** | |

⚠️ **Root rule #6 is under-counted as a primary reason.** It appears in my words at the time on 7 of the 95 (`verdicts.tsv`), and in more of the underlying notes: QQQ wall, post-PPI, the 11/16 open, the oil short, SIG-002. It was usually the second reason behind "no owner direction". If the first reason had gone away, it would often have stopped the trade next.

## 3. What would have had to be different for a card to exist

Facts are what the record shows; **opinion** is labelled.

| Class | Fact: what stopped it | What would have had to be different |
|---|---|---|
| H. Evidence weak | My judgment, citing construction rule #18 (measured envelope, TERRY) or an owner's own low-confidence grade | A measured edge: a sample showing the setup pays after costs, or an owner grading the evidence strong. **Opinion:** this class is where I am most likely to be too strict, because "no measured edge" is a high bar for a $500 defined-loss idea. |
| E. No owner direction | TERRY Hard Boundary 3 (no thesis ownership; owner Will, TERRY charter); owners (HENRY, BRENT, BOND, BROCK, MIDAS) explicitly declined a direction | An owner stating a dated, falsifiable direction, or a rule letting TERRY originate a small direction itself. |
| A. No instrument | Market structure: private issuers, no listed options, dead chains; Hard Boundary 7 / risk-first (loss must be definable) | A listed carrier with a quotable chain, or a willingness to use undefined-loss shorts (which TERRY's risk-first rule forbids). |
| D. Trigger not met | Each card's own pre-registered trigger (TERRY's, often keyed on an owner's gate such as REG-T-04 or a FALCON row) | The world doing what the trigger waited for, or looser triggers. |
| F. Priced | My reading of the tape or chain (MRNA chain sd = PROME tree; NBIS −20% already; HBAN anticipated) | Seeing it before the market did: the finding arriving earlier, or an edge on how much is priced. |
| J. Will's call | Your rulings (WQ-418, 491, 492, 592, 593, 599, 616; shelving 10/29) | Your approval. |
| K. Duplicates book | Construction rule #18 / N_eff discipline (TERRY): same falsifier as held lines | A smaller existing position, or a different falsifier. |
| B. Debit cap | Each card's own cap (TERRY), set to keep reward-to-risk at or above about 1:1 | A wider cap, or a broker fill below the vendor screen (the screen is ask/bid; your broker may fill better). |
| C. Root rule #6 | Root rule #6 (root, canonical owner TERRY `RISK_RULES.md`); the break test was not met | A day of the other colour, or a written refuting measurement (the HYG ×5 card has such a waiver, WQ-663 B). |
| G. X1 / $500 | The $500 per-card default and LIQUID's X1 gate (Will-set; X1 owned by LIQUID) | A higher per-card budget, or the X1 gate re-armed. |

## 4. Afterwards, context only (not scoring the rule)

Daily closes from yfinance (vendor). "After" is today's intraday daily bar, pulled about 13:51 EST 2026-11-16, not a close. Equity moves only; no option P&L is implied (strikes, IV and expiry would decide that).

| Name | Idea not taken | Verdict date (close) | Price then | Now (11/16 intraday) | Move | Class |
|---|---|---|---:|---:|---:|---|
| CCL | puts | 9/18 | 21.73 | 28.70 | +32.1% | H |
| NCLH | puts | 9/18 | 14.12 | 17.67 | +25.2% | H |
| CRWV | put spread (rally fade) | 10/22 | 55.60 | 49.91 | −10.2% | D (voided before firing) |
| OKTA | call spread | 10/29 | 221.86 | 179.09 | −19.3% | D |
| VST | long | 10/29 | 140.95 | 128.34 | −8.9% | J |
| MRNA | call spread (ESMO) | 10/22 | 202.63 | 215.35 | +6.3% | F |
| FXY | call spread | 10/23 | 58.42 | 57.46 | −1.6% | B |
| IEF | call spread | 10/23 | 90.74 | 90.29 | −0.5% | B |
| FLG | put | 10/23 | 10.38 | 10.34 | −0.4% | C |
| TLT | put spread | 11/4 | 81.76 | 79.46 | −2.8% | J |
| CF | call spread | 11/4 | 111.68 | 120.51 | +7.9% | J |
| RSP | call spread | 11/6 | 216.05 | 219.30 | +1.5% | J |
| NBIS | puts | 11/12 | 128.64 | 107.82 | −16.2% | F (chase) |
| CABO | short | 11/11 | 3.66 | 2.97 | −18.7% | A |
| ABR | short | 11/11 | 1.39 | 1.15 | −16.9% | F |

**Reading (opinion):** the passes that the tape most clearly supports are CCL and NCLH (bear, both up), OKTA (bull, down 19%) and VST (down 9%). The ones where the direction would have paid are the bear ideas on stressed names: Nebius, Cable One, Arbor, and CoreWeave after its void. Each was stopped by having no defined-loss instrument, by being a chase after a big drop, or by the card's own void line. CF and TLT, both declined by you on 11/4, moved the way their cards pointed; whether the spreads would have paid within their caps and expiries is not measured here.

## 5. What the record says about rules (no change proposed)

- **TERRY Hard Boundary 3** (no thesis ownership; Will-set at creation) is the rule behind the largest class (E, 20 verdicts). If any rule is costing trades, it is this one. Changing it is yours.
- **Card debit caps** (TERRY, per card) stopped two cards whose triggers were met (FXY, IEF) and are holding the QQQ 200-day card (trigger met on 11/13 and 11/16, debit $5.25 to $6.23 vs $4.90). The caps are mine; I raise them only on your word.
- **Root rule #6** stopped two directly and stands behind many "no owner direction" verdicts. Its break test is mine (`RISK_RULES.md`); the rule is root canon.
- **Construction rule #18** (measured envelope) sits behind most of class H. It is mine.
- No change comes out of this pass.

## Process

Time box 13:48 to 13:5x EST (`date`), held under BRENT's 15:30 grade. Tools: python over the ledgers; yfinance for §4. No subagent. The reader can audit every row in `verdicts.tsv` (date, item, class, source, my words).
