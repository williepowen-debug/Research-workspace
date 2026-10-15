# TERRY → PROME — WQ-425 delivered: OZK Nov-20 $40P ×4 and WAL Dec-18 $65P ×4 pre-print cards

**Written:** 2026-10-14 Wed 21:10 ET (`date`). Spawn: prome-8e, WQ-425 (Will 20:49 ET, *"Approve 425, spawn TERRY for the OZK and WAL cards"*). Runtime: Claude Code, Claude Opus 5.5 (`claude-opus-5-5`); session id not exposed to this desk (UNKNOWN). Boot: root `CLAUDE.md`, `AGENTS.md`, `USER.md`, `AGENTS/TERRY/CLAUDE.md` and the desk boot files read explicitly (RISK_RULES, RISK_SCORING, RISK_RULES_CONSTRUCTION in full, template, workflow, intake); `boot.py` run.
**$0 moved · no order · no new position · no threshold, gate or score moved.** Both recommendations return to Will (root rule #5).

## The two recommendations (one line each, for the [Approve] rows)
1. **OZK — SELL the Nov-20 $40P ×4 to close before the Tue 10/20 print.** Window Thu 10/15 – Mon 10/19 15:30 ET, backstop Tue 10/20 15:30 ET. Day limit from Fidelity's mid toward its bid; never a market order. About $117–157 net against the $322.65 basis. **No roll.** Card `AGENTS/TERRY/setups/OZK40P_nov20-sell-or-roll_preprint_2026-10-14.md` (`MGMT-OZK40P-NOV20`).
2. **WAL — lean SELL the Dec-18 $65P ×4 before the Mon 10/19 print** (window to Mon 10/19 15:30 ET; about $677–787 net vs $682.65 basis, i.e. roughly breakeven). **HOLD ×4 through the print is a legitimate alternative**, priced on the card: an expected cost of about $105, and a post-print read by Wed 10/21 15:00 ET keyed to the WAL desk's own registered KILL and Bear CONFIRM legs. **No roll.** Card `AGENTS/TERRY/setups/WAL65P_dec18-preprint-management_2026-10-14.md` (`MGMT-WAL65P-DEC18`).

## Why, in figures (screening quotes 20:54 ET after the close; Fidelity governs; mirror capture time UNKNOWN)
| | OZK 40P ×4 | WAL 65P ×4 |
|---|---|---|
| Spot 10/14 close · quote | $44.93 · 0.30/0.50 | $72.22 · 1.70/2.25 (OI 37, thin) |
| Strike / breakeven distance | −11.0% / −12.8% (27 sessions) | −10.0% / −12.4% (46 sessions) |
| Thesis owner today | catalyst removed by the issuer (RaDD extended to Dec 2029, $100M); owner: *"no compelling, specific near-term downside opportunity"* | v2.4 ACTIVE, *"NO DEMONSTRATED EXPECTATIONS GAP"*; REGINALD 25% below $65, *"no demonstrated put-pricing advantage"* |
| Print priced (one-day sd, term structure) vs realized RMS of last 8 prints | ≈ 4.1% vs 4.58% — **fair at the money** | ≈ 9–10% vs 4.30% — **≈ 2× rich** |
| Expected value of holding through the print, over the name's own 8 prints | $130 vs $160 mid now ⇒ cost ≈ $10–50 | $685 vs $790 mid now ⇒ cost ≈ $105 (range $36–172) |
| Forward risk vs the $500 card cap | $120–160, inside | $680–790 = **1.36–1.58×** |
| Root rule #7 | thesis-broken branch ⇒ the exit is a sale, not a trim | thesis intact; #7 does not oblige holding through an event priced ≈ 2× its record. **The tension is stated on the card**; if Will reads #7 as binding, HOLD is the rule-consistent choice |
| Roll | none: no Dec expiry; Jan-15 ≈ $170–240 net debit = new capital, no fired trigger | none: Jan ≈ $190–420, Mar ≈ $710–920 net debit = new capital, no fired trigger; Mar alone breaks the cap |

Computations: `AGENTS/TERRY/research/2026-10-14_WQ425-preprint-cards/OUTPUT.txt` (+ scripts). Black–Scholes model mids on screening IVs, not bids; directional estimates with n = 8 prints.

## Disagreement resolved at the artifacts (brief asked)
WAL desk 10/13 `research/2026-10-13_preprint-expectations-gap.md:88` (*"No trade construction referral is justified now"*) and 10/14 `research/2026-10-14_relative-weakness-interpretation.json` (*"Recommend bringing TERRY's Fidelity65P management review forward before earnings"*) answer **different questions**: building a new short versus managing the held put. **No contradiction.** REGINALD's 10/13 "No TERRY construction recommendation follows" is the same new-construction scope.

## RED's challenge consumed, with one correction routed
CHG-RED-052 consumed (packet → `inbox/processed/`); the flip conditions are on the OZK card (FT-02 ×3 **and** LIQ-07 S1 at the 10/16 read ⇒ a labeled tail-hold branch goes back to Will). ⚠️ **Basis finding:** RED's table sets a *breakeven* base rate beside a *strike-level* implied probability. Like for like, OZK history is about 0.6–0.75× implied (5y: 13.8% vs 17.7–19.2% below the strike), not "less than half". RED's conclusion (priced above history) survives. Packet `AGENTS/RED/inbox/2026-10-14_from-TERRY_CHG-RED-052-base-rate-basis.md` (`c0430c292`).

## Other dispositions
- **Untracked 10/11 WQ-418/420 receipt: COMMITTED** (`24dbebe78`). It is cited by `PROME/proposals/2026-10-11_wq418-420-RULED.md:31`; trashing it would have left that ruling record pointing at nothing.
- R1: `COR-20261014-23` receipted NO-OP (TERRY carries no SIG-W-20261014-001 core-pass-through framing). BOARD scan run, 0 new action-line signals since `SIG-W-20261012-030`, 0 logged. `ledger_sweep.py` CLEAN A–H rc 0; weekday claim check clean.
- CRUISE's 10/14 NCLH/RCL packet (arrived during this spawn): **read, NOT consumed** — outside this commission (no inbox drain). It stays in `AGENTS/TERRY/inbox/` for the next full wake.

## Skipped or not run (disclosed)
`paper_book_mark.py` and `snapshot.py --stress` (not needed for two management cards; prices came from `fetch.py` and `chain_fetch.py --no-cache`). `consumer_check.py` not run: no figure superseded. The C5 dates 11/18 and 12/16 are discharged by the cards, and the OZK and WAL desks' STATUS files still cite them as owed (routing is yours). **`STATUS.md` is at 76% of its read budget (rotate tier, advisory)**: a rotation is owed at the next full session, not done here.

## COMPLETION — TERRY — 2026-10-14
STATUS: ✅ DONE
CHANGED: AGENTS/TERRY/setups/{OZK40P_nov20-sell-or-roll_preprint_2026-10-14.md, WAL65P_dec18-preprint-management_2026-10-14.md, INDEX.md, WAL65P-OZK40P_new-fidelity-lines_note_2026-10-07.md}, TRADE_BOOK.md, STATUS.md, registry/corrections_receipts.tsv, research/2026-10-14_WQ425-preprint-cards/ (5 files), research/2026-10-11_WQ418-WQ420-integration-receipt.md, inbox/ → processed/ ×2; AGENTS/RED/inbox/2026-10-14_from-TERRY_CHG-RED-052-base-rate-basis.md; this memo
RESULT: Two cards. OZK 40P ×4: SELL before the 10/20 print (issuer removed the catalyst; print fair at ≈4.1% vs 4.58%; stake $120–160). WAL 65P ×4: lean SELL before the 10/19 print (event ≈9–10% vs 4.30% realized; holding costs ≈$105 expected; risk 1.36–1.58× the $500 cap), HOLD priced as the alternative. No rolls. WAL-desk disagreement resolved: different questions. RED base-rate basis mix corrected (conclusion survives).
GAPS: All quotes after-hours vendor screening (bid/ask age unknowable); Fidelity's bid and working orders UNKNOWN until Will's screen. CRUISE packet read, not consumed (out of scope). STATUS rotation owed (76%).
WILL_NEEDS: (1) OZK Nov-20 $40P ×4 — approve SELL to close before Tue 10/20 15:30 ET, or decline (hold as a tail bet). (2) WAL Dec-18 $65P ×4 — approve SELL before Mon 10/19 15:30 ET (A), or HOLD through the print with the 10/21 post-print read (B).
FOLLOW-UP: PROME registers both as [Approve] rows; C5 card dates for the uncarded KRE Nov-27 67P ×4 (by Tue 11/24) and KRE Dec-18 60P ×5 (by Wed 12/16) per RED's ask; tell the OZK/WAL desks their 11/18 / 12/16 card dates are discharged. Book any fill (root rule #10) on Will's screen.
