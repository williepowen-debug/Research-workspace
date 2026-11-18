# TERRY: 60-day review of "no card" verdicts, by reason (2026-09-17 to 2026-11-16)

**Written:** 2026-11-16, 13:48 to 13:5x EST (clock from `date`: commission 13:48, prices 13:51, packet 13:53). **Desk:** TERRY, Claude Code, Claude Opus 5.5. **Commission:** PROME prome-6f on Will's word (PROME's chat 13:45 ET, verbatim "Id like to go back to your findings and start working on these"), packet `inbox/processed/2026-11-16_from-PROME_commission-60-day-no-card-review-by-reason.md`. **Limits:** one bounded pass; no trade, no card and no rule change come out of it. Data: `verdicts.tsv` beside this file (one row per verdict, with source and my words at the time).

> **RECONCILED 2026-11-18 15:3x EST with the independent reader's ledger** (`PROME/reports/2026-11-16_wq696-no-direction-bins/LEDGER.md`), on Will's 11/16 word (DOCKET line 1162) and his 11/18 15:29 ET "go" relayed by PROME. Nine class E rows reclassified (E 20 → 11); the Hard Boundary 3 claim is withdrawn. Counts, the five lines, §2, §3 and §5 below are the reconciled version; every change and every disagreement is in §6. The 11/16 wording is in git history (`git log -p -- REPORT.md`). Will's word stands: no directional-ownership charter change and no red-day rule change follow from this sample.

## Five lines for Will first

1. **95 "no card" verdicts in 60 days.** By what stopped them: my own or the owner's judgment about the evidence, 43 (too thin 28, already priced 10, doubles a held position 5). No desk held a direction, 11. No listed instrument, 14. A card's trigger or a gate not met, or your decision, 20. The hard rules were the main reason on only 6: debit caps, the red-day/green-day rule (root rule #6) and the $500 / sizing gate. Other, 1.
2. **No desk held a direction: 11 (12%), after the reconcile (was 20).** The reader showed, and I accept, that in most of the original 20 the owning desk had said in writing that the evidence supported no trade or was mixed. My charter rule against originating a thesis (TERRY Hard Boundary 3) would only have mattered if I had wanted to override those owners, so it was not "the rule doing the stopping". The withdrawn claim is in §6.
3. **No listed instrument (14, 15%).** Many of the fleet's strongest findings were about private or illiquid names: United Fidelity, Car-Mart, Cable One, Exeter, SoftBank, N-able. No reworking of construction rules fixes that.
4. **Triggers or gates not met (14, 15%; 12 before the reconcile added the 10/15 oil adds and SIG-002), plus 6 you declined, passed or shelved.** Two built cards had their triggers met and were stopped only by my debit cap: FXY on 10/23 (debit 0.925 vs 0.90 cap) and IEF on 10/23 (0.975 vs 0.85). The open QQQ 200-day card (not counted here; still live) has had its trigger met on three sessions and failed its $4.90 cap each time.
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
| H. Thesis or evidence too weak (incl. measured no edge, and an owner saying the evidence supports no trade) | 28 | 29.5% | CCL puts, negative EV on 8 prints (9/19) · TLT short on refunding, trigger 0 of 34 (11/5) · bank-name puts, REGINALD score no skill (11/8) |
| E. No desk held or stated a direction (owner withheld one, or no owner) | 11 | 11.6% | QQQ under its 680 put wall (11/13) · crude short on the EIA build, BRENT WAIT (11/12) · airfares, MARCO "cuts both ways" (11/11) |
| A. No listed instrument, or options too thin to quote | 14 | 14.7% | United Fidelity (11/12, 11/16) · Car-Mart, 0 expiries (11/13, 11/16) · SoftBank, SFTBY no options (11/10) |
| D. Trigger or gate not met, or window lapsed unfired | 14 | 14.7% | HYG/HTGC credit puts lapsed, REG-T-04 never fired (11/13) · CRWV rally fade voided (10/22) · OKTA calls, no 8-K Item 1.05 (10/29) |
| F. Already priced or anticipated | 10 | 10.5% | MRNA ESMO, chain priced the readout (10/22) · Nebius after −20% (11/12) · HBAN Category III, Fitch already cut (11/16) |
| J. Card built; Will declined, passed or shelved (added class) | 6 | 6.3% | TLT QRA put spread, WQ-592 B (11/4) · RSP call spread declined (11/6) · VST shelved (10/29) |
| K. Duplicates exposure the book already holds (added class) | 5 | 5.3% | oil right tail into the reopen, book already long oil (11/8) · more Nasdaq downside, same falsifier as held QQQ puts (10/31) · FLG puts, same bank falsifier (10/15) |
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
| E. No owner direction | The owner withheld a direction or said it cut both ways (HENRY ×3, BRENT ×3, BOND, MIDAS, MARCO, ZHAO), or no desk owned the question (the KRE/QQQ seesaw, Will's own exploration) | An owner stating a dated, falsifiable direction. |
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

- **TERRY Hard Boundary 3** (no thesis ownership; Will-set at creation): **not shown to be costing trades** (claim withdrawn 11/18, §6). In the 11 class E rows the owner withheld a direction; in the rows moved out of E the owner had said no, or a gate, ruling or held line stopped it. Will ruled 11/16: no charter change follows from this sample.
- **Card debit caps** (TERRY, per card) stopped two cards whose triggers were met (FXY, IEF) and are holding the QQQ 200-day card (trigger met on 11/13 and 11/16, debit $5.25 to $6.23 vs $4.90). The caps are mine; I raise them only on your word.
- **Root rule #6** stopped two directly and stands behind many "no owner direction" verdicts. Its break test is mine (`RISK_RULES.md`); the rule is root canon.
- **Construction rule #18** (measured envelope) sits behind most of class H, together with owners' own "no trade" grades. It is mine.
- No change comes out of this pass.

## Process

Time box 13:48 to 13:5x EST (`date`), held under BRENT's 15:30 grade. Tools: python over the ledgers; yfinance for §4. No subagent. The reader can audit every row in `verdicts.tsv` (date, item, class, source, my words).

## 6. Reconcile with the reader, 2026-11-18 (finding by finding)

**Rule now applied (fixes the reader's finding 5):** class E means no desk held or stated a direction (the owner withheld one, said it cut both ways, or no owner existed). An owner who said the evidence supports no trade goes to H. A direction that existed but was stopped by a gate, a ruling, a held line or an unfired card goes to D, J or K. The primary reason is still the first reason in my words at the time (§1); where a row's class changed, the reason is in the new `reconcile_2026-11-18` column of `verdicts.tsv`, and my words at the time are unchanged.

| Reader finding | Disposition | What changed |
|---|---|---|
| 1. Counts, shares and the root rule #6 count of 7 reproduce | Accepted | Nothing (counts now re-stated after reclass) |
| 2. Hard Boundary 3 as "the rule doing the stopping" not supported | **Accepted** | Five lines item 2 and §5 rewritten; claim withdrawn |
| 3. Rows 2, 17, 20 had an owned direction | **Accepted** | Oil adds (10/15) E → D (WQ-192 stand-down and BG-02 unmet; no card was built, so not J) · gold (11/16) E → K (lean already held in GLD shares) · SIG-002 (11/16) E → D (NVDA half is my own NOT-FIRED card) |
| 4. E low on my own wording (lines 43, 67; partly 84, 33) | **Accepted in part** | No primary re-class: lines 43 (fade an oil spike) and 67 (S&P over the flip) list another reason first (n=1 precedent; root rule #6), and §1's tie-break is the first reason. "No owner direction" is present as a **secondary** reason in at least these 2, so as any reason it appears on at least 13 of 95. Lines 84 and 33 are owners-saying-no or no-edge, H under the rule above |
| 5. Owner explicitly saying no is E in rows 4, 6, 7, 11, 12 but H at line 60 | **Accepted, rule applied** | RNR, diesel refiners, FSK, Siemens Energy E → H. Also BX/OWL/APO (BROCK "headline risk only", not named by the reader) E → H, and the CPI straddle E → H (reader row 8: no direction needed, no measured edge). **Disagree on row 12 (airfares):** MARCO said fares "cut both ways" with no clean expression, which is a withheld direction, not a no; it stays E |
| 6. Row 4 (RNR) re-lists the 10/11 NO-BUILD | **Accepted** | Redated to 10/11 (inside the window; no 10/11 row existed, so it is moved, not dropped); total stays 95. Attribution corrected: AEOLUS recommended NO-BUILD, TERRY decided |
| 7. Row 8 cites "HEN-57 core 0.4+", the fire threshold | **Accepted** | Correction added at `research/2026-11-08_wq650-pass/IDEAS.md` item 4: HENRY's own expectation at 11/6 was NOT FIRED, +0.2 |
| 8. Owner list for E omits AEOLUS, VULCAN, MARCO, ZHAO | **Accepted** | §3 row E re-listed for the 11 remaining rows |
| PROME's relay omission on row 18 (oil short on the IEA surplus) | Noted | Agree with the reader that it did not change my answer (BRENT WAIT; red-day chase). Row stays E |
| Contested rows 10, 14, 16 (Saudi, QQQ wall, QQQ/S&P after 11/13) | Kept E | HENRY and BRENT withheld a direction in writing; my notes saying the regime "argues for puts" were my reading, not an owner's. Bin 3 on the reader's alternate reading; I record the contest and do not move them |
| Seesaw (row 5) | Kept E, flagged | No owner existed; my own test was negative, so H is a defensible alternative |

**Net:** E 20 → 11, H 22 → 28, D 12 → 14, K 4 → 5; total 95. No row moved into or out of the population. No trade, card, rule or charter change follows (Will, 11/16).

