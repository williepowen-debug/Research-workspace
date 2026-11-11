# WAL → PROME: 11/11 catch-up — live data, inbox drained, hiking-Fed read

**Date:** 2026-11-11 ~10:12 ET · **Task:** prome-2b catch-up wake (Will 09:24 ET) · **Runtime:** Claude Code, model Opus 5.5 (claude-opus-5-5); session ID not exposed (UNKNOWN). · **Commits:** `c42411f512` (record), NEXUS pin after it, this packet.

## What changed in my read since 11/04, in plain words

The thesis did not move: v2.5 weights, EV $76.60 and PT $52–77 are unchanged, and nothing graded. The stock fell with the 11/05 bank selloff, from $79.26 (11/04) to a $76.30 close on 11/10 (vendor). It is now about at fair value, with no margin of safety either way. It is trading more like the bank index than it was (beta to KRE 1.17, up from 1.02). Short sellers trimmed for the first time in four settlements.

On rates, a hiking Fed is mostly already in WAL's numbers:
- **Deposit cost:** management's Q4 guide already assumed one December 25bp hike. By WAL's own model, a hike raises interest income about as much as it raises the earnings-credit (ECR) deposit cost, so it is roughly a wash for pretax earnings. The Q3 10-Q did assume deposits reprice faster than at Q2.
- **Securities mark:** the 9/30 mark (−$1.22B pretax on available-for-sale securities) was struck when 5- and 10-year yields were about 30bp higher than on 11/10. Today's mark is therefore probably about $170M better, though roughly $130M of that improvement came back off in the 11/05–11/10 hike repricing. The mark hits tangible book, not regulatory capital.
- **Credit is where higher-for-longer would hurt:** floating-rate commercial real estate and hotel borrowers refinancing into higher rates. I logged that as a theme to watch, not a score change.

No TERRY packet: no score, weight or EV moved and spot is within 1% of EV, so there is no new edge to construct. This is a reasoned "no card", per Will's 11/10 rule.

## Rows (each key → evidence)

| Key | What | State |
|---|---|---|
| KB-WAL-288 | Q3 10-Q rate sensitivity at 9/30: NII +4.7% per +100bp shock (Q2 +5.9%), ramp +2.6% (Q2 +3.2%). EVE −5.3% at +100bp (Q2 −4.4%). Betas: average 53→58%, ECR 70→77%, all non-maturity incl. ECR 59→65% | A1, local primary acc 0001628280-26-068599. **Supersedes KB-212/220/221** for current use |
| KB-WAL-289 | Fed funds 3.63→3.88% from 9/17. Treasury par 9/30→11/10: 2Y 4.88→4.73, 5Y 5.09→4.81, 10Y 5.29→4.98 (FRED and treasury.gov, pulled 11/11; **your 2Y 4.73 / 10Y 4.98 verified**). Issuer Q4 guide assumed a Dec +25bp hike (KB-250, B2 transcripts). Per 25bp: NII ≈ +$38M/yr vs ECR ≤ ~$58M/yr total, ~$43M of it in expense | DERIVED, linear. December pricing (>1 hike) is HENRY's vendor-last-trade calc via card 20261110-001, **not verified by WAL** |
| KB-WAL-290 | AFS 9/30: amortized cost $19,662M, FV $18,444M, loss $1,223M. Fit ~$6M/bp → since 9/30 ≈ +$170M pretax (~$1.2/share TBV); 11/05→11/10 gave back ~$130M. AOCI outside CET1 (opt-out; KB-287) | **ESTIMATE**: one-quarter fit contaminated by $2.0B hedge terminations and spreads; no printed duration |
| KB-WAL-291 | Theme `cre-refi-rate-pressure`: hotel criticized $75M→$185M; 2027 CRE-NOO maturities $2,972M; CREED conduit-coupon card | Logged, not scored |
| KB-WAL-292 | Tricolor Rule 2004 names Ares / AllianceBernstein; First Brands trial adjournment motion (2/9 → 6/21/2027, no ruling). WAL not named | B2 relay; not-named ≠ negative; V2 excluded |
| KB-WAL-293 | DEWEY Plaza Continental: Ontario **stays B1**; receiver out 10/16; KW-SHW + CBRE hired 10/26; no sale or price, so H8 not fired; plan/disclosure (Docs 119/120) unread | Docket text only |
| KB-WAL-294 | Q3 Basel III Pillar 3 disclosure (posted 11/9) **not read**: issuer site HTTP 403, not evaded | Open item, review 11/25 |
| MARKET_TRACKER | 12 readings: FINRA 10/30 settlement 5,599,365 shares (−11.87%), 5.21% of 107.55M (10/26 cover), days-to-cover 5.21; 11/10 closes WAL 76.30 / KRE 73.09 / WAL-PA 24.38; vol 33.4% (20d) / 25.2% (60d); beta 1.17; spot vs EV −0.39% | `workbook/MARKET_TRACKER.tsv` |
| Price | $76.15 (−0.20%) at 09:48 ET 11/11, vendor intraday; buffer to $81.90 is +7.55%. REGINALD's exit log last row 11/06 close 75.55, run 0 of 3, FIRED (REGINALD grades) | boot.py |
| board_log | SIG-W-20261105-017 noted · -067 noted · 20261106-021 noted · 20261109-012 acted (KB-294) | All 4 moved to processed |
| N1–N4 / WAL-01/02 / gates | No letter touched this morning. N-letters are frozen Q3 print diagnostics. GATE-REG-T02 is terminal: the 11/05 sub-78 tape is a suppressed re-entry | No grade |

## Discrepancies with the wake brief (for your record)

- **CPI/Waller card:** SIG-W-20261110-001 was **not routed to WAL** (its recipient lines exclude WAL). My 4 unread cards were 1105-017, 1105-067, 1106-021 and 1109-012. I read 001 from BOARD as context.
- **Top-level inbox files:** I found **1**, not 2: the DEWEY 11/02 packet. No second loose packet was present at 09:50 ET. The 11/05 REGINALD channel entry is ACKed.

## Combination watch (WQ-622): my theme list

1. `rate-path-deposit-cost`: does a hiking Fed push all-in deposit cost (interest + ECR) up faster than asset yields?
2. `securities-mark-tbv`: do rate moves reverse Q3's TBV decline?
3. `cre-refi-rate-pressure`: does higher-for-longer raise refinancing stress in the CRE/hotel book?
4. `fraud-ecosystem-names`: do Tricolor / First Brands / LAM proceedings name WAL or move its recovery?
5. `cantor-collateral-liens`: does the Cantor collateral reach a priced sale?

⚠️ The charter line (COMBINATION_WATCH step 3) is **not added**, because this task barred charter changes. Clear it and I add it at the next session.

## Checks and gaps

- Boot checks:
  - Corrections rc 0.
  - Predictions check silent.
  - Named-field issues 2 → 0 after the drain.
  - **2 new drift identities**, both a token collision: the Q3 ramp "+2.6%" matches a retired 8/23 price-distance claim. Reviewed as a different object; baseline not edited.
- **KB expiry backlog:** 95 of 191 ACTIVE rows are past Stale_By (oldest 11 days). Not judged this session (out of scope; never in bulk).
- STATUS was at 96% of its read budget. Two historical blocks were rotated verbatim to `AGENTS/WAL/archive/STATUS_rotation_2026-11-11.md`, bringing it to 85%.
- **Push deferred to closeout:** HEAD also carries 4 earlier foreign commits, and the dirty tree belongs to ORACLE/VIOLET/scripts, none touched.
- Overdue: the OZK Q3 10-Q pointer (KB-228, ~11/5), carried. Forward Q4 predictions are due Sun 11/15.

## COMPLETION — WAL — 2026-11-11
STATUS: ✅ DONE
CHANGED: AGENTS/WAL/{STATUS.md, MEMORY.md, INDEX.md, NEXUS_BRIEF.md, REGINALD_CHANNEL.md, board_log.tsv, workbook/KB.tsv, workbook/KB_INDEX.md, workbook/MARKET_TRACKER.tsv, research/2026-11-11_hiking-fed-deposit-cost-securities-mark.md, archive/STATUS_rotation_2026-11-11.md}; 5 inbox files → processed; this packet
RESULT: Drained 5 inbox items (4 WALTER + 1 DEWEY) and added KB288–294, superseding 212/220/221. Tracker +12 readings (short interest −11.87% to 5.21% of shares; 11/10 close $76.30). Rate read: Dec +25bp already in the issuer's guide, a hike is roughly neutral pretax by the issuer's model, betas raised at Q3, and the AFS mark is ~+$170M pretax better than 9/30 (estimate). No weight, score, EV or grade change.
GAPS: Basel III Q3 disclosure unread (issuer site 403). KB expiry backlog (95 rows) not judged (out of scope). Combination-watch charter line deferred (task barred charter changes). December pricing taken as HENRY's relay, unverified.
WILL_NEEDS: None.
FOLLOW-UP: PROME: clear (or not) the WAL combination-watch charter line. WAL: forward Q4 predictions by Sun 11/15; closeout and push when PROME asks.
