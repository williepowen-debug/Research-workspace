# TERRY → PROME — WQ-487 A: inbox drain + NOT-FIRED trade cards (2026-10-22)

**From:** TERRY · Claude Opus 5.5 (`claude-opus-5-5`), Claude Code, PROME spawn (prome-25); session ID not exposed (UNKNOWN). **Clock:** work 13:25–13:4x ET 10/22, every stamp read from `date`.
**Boot reads (bounded reader `PROME/tools/boot_read.py`, each to `eof: true`):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 2 · `AGENTS/TERRY/CLAUDE.md` 6. Desk boot: `boot.py`, `RISK_RULES.md`, `RISK_RULES_CONSTRUCTION.md` (rules 14–23 in full), `RISK_SCORING.md`, `TRADE_CARD_TEMPLATE.md` read whole; R1 corrections check; paper-book mark run.
**Authority:** Will 10/22 13:22 ET WQ-487 A; Will 10/20 11:50 ET *"we can loosen rules for trade ideas"*. **$0 moved · no order · no gate, threshold or score moved.** Every card below is **NOT-FIRED and unapproved**; Will decides each one (root rule #5). No expiry or sell-or-roll content on held lines (`USER.md` § No expiry nagging).

## 1. Cards written (3)

All prices are live pulls 13:26–13:32 ET 10/22 (`fetch.py price`, `chain_fetch.py --no-cache`); option quotes are vendor SCREENING marks, the order is priced on the broker chain. X1 sizing gate stays CLOSED: a fill against it is Will's per-card choice. Default size $500/card shown on every card; none exceeds it.

| Card (path under `AGENTS/TERRY/setups/`) | Label | Trigger state, one line | Size | Max loss (risk) | Day colour (root rule #6) |
|---|---|---|---|---|---|
| `QQQ_nov20-690-670P_gamma-negative-putwall_2026-10-22.md` · `IDEA-QQQ-PUTWALL-OCT22` | NOT-FIRED | SPX cash close < 7,650 (HENRY's clean put-wall break): SPX 7,649.77 intraday at 13:26 ET, not a close; gamma NEGATIVE both horizons at 09:53 ET | QQQ Nov-20 690/670P ×1 (default) | **$492.30** worst-case debit + fees; max gain $1,507.70; breakeven QQQ $685.09 (−2.95%) | Today RED (QQQ −2.66%, VIX +15.35%): no break claimed; entry only on the first GREEN QQQ session after the trigger, by 10/30 |
| `USO_jan15-170-185C_post-election-strike-window_2026-10-22.md` · `IDEA-USO-POSTELECTION-OCT22` | NOT-FIRED | FALCON FAL-07 US strike NOT FIRED (45 days since 9/8); FALCON 65% by 12/31 but ~10% [EST] before 11/3; IRGC tanker claims 0 of 7 confirmed | USO Jan-15-2027 170/185C ×1 (default) | **$461.30**; max gain $1,038.70; breakeven USO $174.60 (+7.5%) | Today GREEN (USO +1.56%): entry only on a RED USO session 10/23–11/2; no-chase USO > $168 |
| `OKTA_nov20-220-230C_agent-credential-security-wave_2026-10-22.md` · `IDEA-OKTA-SECWAVE-OCT22` | NOT-FIRED · structure confidence LOW | No Storm-0940/ConnectWise 8-K Item 1.05 yet; Huntress count 173 unchanged; falsifier: still quiet on 11/6 | OKTA Nov-20 220/230C ×1 (default) | **$341.30**; max gain $658.70; breakeven OKTA $223.40 (+10.3%); IV ~63% | Today RED for OKTA (−2.96%): colour fits a call entry today |

**Book notes that travel with the cards:** the QQQ card shares its falsifier with the held QQQ Oct-26 710P ×1 (N_eff ≈ 1.5, sized as one view). The USO card is the SAME bet as the oil sleeve (USO 35 sh + five held call lines, all expiring 10/23–10/30; N_eff = 1); its only new property is tenor past 11/3, which is where FALCON puts most of the strike odds. It is a NEW DEPLOYMENT under construction rule #21, not a roll, and it says nothing about the held lines. The OKTA card has **opposite sign** to the QQQ card in a tech selloff (OKTA trades with the AI-software tape), so it is not a hedge.

## 2. No candidate, per evaluated leg

| Leg | Verdict and reason |
|---|---|
| **(a) equity downside** | Carded (QQQ above). |
| **(b) oil upside** | Carded (USO above). An incremental near-dated call was rejected: it would add to the same falsifier with tenor that dies before the window. |
| **(c) banks** | **No candidate.** Day colour is right (KRE $72.39 +2.51%, OZK $49.76 +3.47%, WAL $77.00 +1.93% at 13:26 ET), but: owners read HY transmission as **BANK-ABSENT** (REGINALD ~0.6, SIG-012) and the CRE channel as rates, not spreads (CREED, SIG-015); OZK conviction is now LOW (WQ-483); the book already holds 29 bank and credit put contracts across 10 Fidelity lines on one falsifier (RISK_SCORING §2b); the 6-of-6 rising problem loans / thinning coverage is slow-grind evidence that the held Nov–Dec lines already express. Another put adds N_claimed, not N_eff. |
| **(d) CRWV** | **No new candidate.** VULCAN's 10/20 and 10/22 deltas folded into `TRY-COND-CRWV-RALLYFADE`; none of the five falsifiers fired. That card fades a RALLY to $70; today's tape is the opposite (CRWV $55.79 −9.75% at 13:26 ET), and a red day is the wrong colour for puts. ⚠️ **The card's own void line ($58.00 completed close) traded through intraday; if 10/22 closes below $58 the entry case ends** (not graded on an intraday print). Held CRWV Oct-23 56P untouched. |
| **(e) rates** | **No candidate.** No owner trigger has fired (BOND/LIQUID); Will's own approved action is exiting the TBT duration short (WQ-357); the 10Y fell to 4.97% today (`^TNX` 13:26 ET, −3.42%) as a flight-to-quality bid that a duration short would fight while equity gamma is negative; MOVE 104.44 (+8.86%); FOMC 10/28 is event vol inside any near tenor. TLT Dec-18 ATM put IV 15.5–16.0% is not extreme, so the case rests on thesis and timing, not price. The 10/20 IEF Jan 90/92C idea stays on file as an idea (Will 10/20 17:29, "keep as ideas"). |
| **(f) security wave** (PROME's 13:3x packet calls it (e); relabelled here to keep rates as (e)) — leg 1 bank-tech vendor puts | **No candidate.** Every tradeable tenor spans the vendors' own prints (FISV 11/3, FIS 11/4, JKHY 11/3 on the vendor calendar, screening dates), so a put is a print bet, not a security bet: FISV's worst day in 501 bars is **−44.04% on 2025-10-29** (an earnings day), FIS −11.49%, JKHY −7.27% (yfinance, 2 years). The trigger DEWEY names (a vendor-traceable compromise) names no vendor yet. Vendors were UP today (FISV +4.93%, JKHY +5.33%, FIS +4.24%, PRGS +4.86%). |
| (f) leg 2 cybersecurity upside | **Carded as OKTA** (identity = the agent-credential problem; red day). CIBR/HACK options untradeable (CIBR Dec-18 OI 2–37, quotes 16–62% wide); CRWD liquid but carries the vendor-is-the-outage trap. |
| (f) leg 3 agentic-AI platforms (MSFT, CRM, NOW) | **No candidate.** The friction story has no dated catalyst, and MSFT is already inside the QQQ card's index. |

## 3. Drain and gate record
- **Inbox:** 12 top-level packets consumed and `git mv` → `inbox/processed/` (PROME ×5 incl. the 13:3x security-wave packet, VULCAN 10/20, BRENT ×2, DEWEY ×2, HENRY). `inbox/WALTER/`: 0. `inbox/WILL/`: README only. **Two packets that landed mid-session (FALCON 13:4x, VULCAN 13:33) were read and integrated** (USO card § 2 and § 7; CRWV card note (3)); filed → `processed/` after their senders committed them (FALCON `8c6372b2b`, VULCAN `7b7d20ceb`). Inbox top level: 0 packets.
- **BOARD (§3.5 pull record):** `SIG-W-20261019-003` logged **acted** (its TERRY ACTION, a card under LIQUID's >320 rung, is the QQQ card at the default size, X1 CLOSED) plus 10 signals read 10/22 logged acted/noted/info-only. `boot.py`: every action-line signal logged. **BOARD scan run, 1 new since SIG-W-20261016-033, 11 logged.**
- **R1:** COR-20261021-22 and COR-20261022-04 receipted APPLIED; check rc 0.
- **VLO GATE-TERRY-VLO-HELD-01 leg A:** 10/20 $100.177 and 10/21 $95.048 (BRENT-published source 3) **NOT FIRED, no notice**. **Ruling on BRENT's question:** the notice does NOT inherit the ±$0.15 band; the Will-approved letter attaches it to $90.16 only, and extending it would be a letter change for Will, not proposed (the notice carries no action). Recorded on the card.
- **Card evidence folded:** OZK Stage-1 grade + WQ-483 LOW into the OZK 40P card (thesis cell only, no prompt); VULCAN deltas into the CRWV card; Will's 10/20 "keep as ideas" onto the slate. HENRY HEN-46 resolved and both DEWEY INFO packets: no card change.
- **TRADE_BOOK rotation:** the idea rows tipped it to 75%; 3 terminal rows rotated verbatim → `AGENTS/TERRY/archive/TRADE_BOOK_ARCHIVE_2026-10-22.md` (crc32 `06a498fe`); now 63% of budget. Ledger sweep CLEAN (A–H).
- **GATE-OP-SCALE-01 (count only; no card cites it):** **N = 2** distinct closed agent-proposed positions (`TRY-VIOLET-VIXCS`; `TRY-FIRE-004` counted once across its harvest tranche and 9/30 close). INFERRED: other INDEX closures are MGMT cards on Will-entered lines, which the guard excludes. **R ≥ 4** live NO TRADE refusals in `SETUPS.tsv` (CCLPRINT, WQ409-SPY, MPC-L689, CAND-EGBN-L694); archived refusals not counted. Today's three ideas are unfilled and do not count.

## 4. Gaps
- Vendor option quotes are not proven live (durable finding 5b); every card needs a broker re-quote before any order.
- Earnings dates for OKTA/FISV/FIS/JKHY are vendor-calendar screening dates, not issuer IR (RISK_RULES).
- The QQQ trigger and the CRWV void both grade at today's 16:00 ET close; this session closes before then (no wait for a print).

## COMPLETION — TERRY — 2026-10-22
STATUS: ✅ DONE
CHANGED: AGENTS/TERRY/setups/{QQQ_nov20-690-670P…, USO_jan15-170-185C…, OKTA_nov20-220-230C…}.md (new), setups/{INDEX, VLO-SHARE…, OZK40P…, CRWV…}.md, SETUPS.tsv, TRADE_BOOK.md, archive/TRADE_BOOK_ARCHIVE_2026-10-22.md, board_log.tsv, registry/corrections_receipts.tsv, STATUS.md, PAPER_BOOK.tsv, research/2026-10-20_trade-idea-slate.md, inbox/ 14 → processed/, this memo
RESULT: Whole inbox drained, 14 packets incl. 2 mid-session arrivals (FALCON, VULCAN), all filed; SIG-W-20261019-003 logged acted. Three NOT-FIRED, unapproved cards at the $500 default: QQQ Nov-20 690/670P (max loss $492.30), USO Jan-15 170/185C (max loss $461.30), OKTA Nov-20 220/230C (max loss $341.30, LOW). No candidate for banks, CRWV, rates, bank-tech vendor puts or AI platforms, reasons in § 2. VLO leg A 10/20–10/21 NOT FIRED; the $95 notice gets no band. OP-SCALE N = 2, R ≥ 4.
GAPS: Broker quotes not seen (vendor screens only); earnings dates vendor-calendar; QQQ trigger and CRWV void grade at the 16:00 close, after this session.
WILL_NEEDS: Three card decisions (approve, reject or rework), each to be registered as a WQ row by PROME before it is shown; none is urgent, none is a reminder.
FOLLOW-UP: Next TERRY touch: grade the 10/22 close for the QQQ trigger and the CRWV $58 void.
