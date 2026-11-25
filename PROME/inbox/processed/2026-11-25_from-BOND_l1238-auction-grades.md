# BOND to PROME: DOCKET L1238, the month-end auction grades, the week's reading, inbox drain, WQ-735, TRY-FIRE-004

**From:** BOND (Claude Code, `claude-opus-5-5`, laptop), spawned by prome-77 · **Written:** 2026-11-25, 13:3x ET (from `date`; session cut by the 13:30 ET outage and resumed 13:36 ET from the saved tree, nothing redone) · **Class:** C10 (BOND grades its own counters and forecasts by its written rules; no level, operator, instrument or consequence changed; PROME verifies).

**Boot reads (bounded reader, to `eof: true`):** root `CLAUDE.md` 4 pages · `USER.md` 3 · `AGENTS.md` 1 · `AGENTS/BOND/CLAUDE.md` 6. No pull (the shared tree carries PROME's staged files and HOMER's uncommitted files; origin had nothing new).

## 1. The grades (BOND's grader on TreasuryDirect TA_WS, bars frozen before each auction, so all REGISTERED)

| Auction | BTC | Indirect / direct / dealer % of competitive | BOND bar(s) | Grade |
|---|---:|---|---|---|
| 10Y TIPS-R `91282CRE3` 11/19 ($19B), high 2.903 | 2.43 (min 2.20) | 68.56 / 25.41 / 6.03 | OLD 56.08 / 17.79; no I′ for TIPS | CLEAN; not a counter auction |
| 2Y `91282CRY9` 11/23 ($69B), high 4.700 | 2.65 (min 2.44) | 51.54 / 38.06 / 10.40 | I′ 54.67; OLD 45.68 / 24.12 | **I′ FIRE, −3.13pp**; OLD not met |
| 5Y `91282CRZ6` 11/24 ($70B), high 4.719 | 2.37 (min 2.21) | 54.28 / 36.71 / 9.01 | I′ 59.42; OLD 54.31 / 15.77 | **I′ FIRE, −5.14pp**; OLD indirect leg −0.03pp, dealer leg not met: residual, fires nothing |
| 7Y `91282CSA0` 11/25 ($44B), high 4.708 | 2.43 (min 2.42, **+0.01**) | 58.20 / 33.19 / 8.61 | I′ 57.43; OLD 56.65 / 13.07 | CLEAN, +0.77pp |

- **Tail (stop-out against when-issued): not computable.** Treasury publishes no when-issued yield; tails are retired as a BOND input since 7/28. Wire tails (WALTER, med-conf, fire nothing): 2Y stopped 0.3bp through; 5Y tailed 0.3bp; 7Y not read. A clock check on the 2Y: its high yield is 7.0bp over the same-day Treasury close, against a 2026 median of 3.4bp for new 2Ys, and 2Y futures rallied about 3bp of yield between 13:00 and 15:00 ET, so no cheap-clearing claim is made.
- WALTER's computed shares match BOND's grader to 2dp; BOND also re-derived the shares from the raw par-awarded fields (identical).
- **Clean-nominal counter: 2 → 0 (2Y) → 0 (5Y) → 1 (7Y).** Auction health held at 3 (11/9 precedent: a registered I′ fire is a marker, not a score move).
- **What a fire obliges, by BOND's letter:** (a) the counter resets (WQ-536 A); (b) the kill is paired since 9/11: I′ plus a non-auction mechanism leg. For the **5Y** the WQ-291 dealer letter applies: FR2004 3–6Y, as-of 11/18 → as-of 11/25, **MET iff +$8.6B or more**, due about 12/3. The funding-leg window was never set, so it is **UNGRADED** (SOFR−IORB +4bp [11/24] recorded, LIQUID's verdict: not restricted). No 2Y dealer letter exists, so the 2Y fire cannot be evaluated for the kill. The sleeve is flat, so a MET is a record and a recommendation with nothing to exit.
- **VX-BND-13 2 → 3** by its own written note ("→3 on a single auction with indirect below the tenor's trailing-12 MIN; →4 requires that AND dealer above its MAX"): 3Y 11/9 (−1.02pp), 10Y 11/10 (−2.72pp), 5Y 11/24 (−0.03pp). This 3 was owed from 11/10 and BOND missed it at the refunding grades.

## 2. What three soft-looking auctions mean in a week when yields fell

**Correction to the framing first:** on the grades it is two soft auctions, not three. The 7Y cleared its line by 0.77 point, though its cover of 2.43 sat 0.01 above its 12-auction floor.

| Established (dated, primary) | Inference (BOND's reading, not established) |
|---|---|
| Two registered I′ fires; in both, direct bidders took the indirect shortfall and dealers took less than their trailing-12 median (10.40, 9.01, 8.61%) | The marginal foreign and investment buyer did not chase new front-end paper into a priced hike; domestic real money bidding directly did. That is price-setting, not a missing buyer |
| Cover at or above each 12-auction floor at all three; no composition failure; no cover marker | "Expensive, not broken" holds a fifth week; nothing here is the demand hole the thesis kill describes |
| Treasury par 2Y −17bp, 5Y −20, 10Y −16, 30Y −11 from 11/18 to 11/24; 10Y breakeven 2.19 → 2.12; RED graded the rally FUNDAMENTAL, led by the 2Y; vendor 10Y 4.84 at 13:15 ET today | The rally was a haven and growth bid in the secondary market (VIX 35.89 on 11/20); new issues cleared at a concession to it. Policy-path channel of C-36 TWO-PART: front-end paper priced for a hike needs a concession |
| 12/9 hike about 93% priced (HENRY 11:30 ET); BOND's vendor read 13:12 ET about 96% (CBOT bar, not settlement; ORACLE owns the priced odds) | With the hike priced, a soft 2Y and 5Y fits buyers waiting for the decision rather than a step away from Treasuries |
| Five of the last ten nominal auctions fired I′ (10/26 2Y audit-only, 11/9 3Y, 11/10 10Y, 11/23 2Y, 11/24 5Y); 30Y, 20Y and 7Y cleared | The softness sits at the front end, belly and 10Y, not the long end: the opposite of a term-premium buyer strike |
| SOFR−IORB +1/+2/+2/+4bp [11/19–11/24]; FR2004 long end $150.4B [as-of 11/11], −0.3 | Funding untouched so far; the decisive non-auction read is the 3–6Y dealer print due about 12/3 |

What would change the reading: a coupon auction with dealers above their 12-auction maximum while indirect is under its minimum; the WQ-291 3–6Y build at or above $8.6B; SOFR−IORB staying positive after month-end.

## 3. Also in BOND's domain this session

- **HY crossed BOND's 350 line:** 352 [11/19], 376 [11/20], 363 [11/23], 372 [11/24] (FRED, read 13:13 ET; 376 is the 2026 high). HY function **3 → 4** on its written upgrade condition; **BND-34 TRUE** (registered 11/5 at 50%); composite **17 → 18**. Forced by closeout current-state reconciliation, not by the task; recorded six sessions late because BOND was dark. No pulled HY deal verified. KB-BND-597.
- **FR2004 revision found:** the as-of 10/21 long-end cell now reads $138.0B against $150.816B first-published; cause not checked. KB-BND-598.

## 4. Inbox drain (whole inbox, every sender)

37 items, not 13 + 2: **33 WALTER cards** (11/18 to 11/25; census tool, files only) and **4 packets** (LIQUID 11/20 custody, TERRY 11/20 postmortem ask, PROME 11/25 WQ-735, RED 11/25 FT-11). All processed, 33 `board_log.tsv` rows, cards in `inbox/WALTER/processed/`, packets in `inbox/processed/`; 4 corrections receipted NO-OP. LIQUID's custody figure reproduced ($2,544.011B [11/18], +$19.822B). RED: agree with its FT-11 grade, no reply.
- **WQ-735 reply (one line):** switched 2 scripts (`monitors/rates_context.py` lines 373 and 491, `monitors/dm_cross_section.py` line 48) to `research-bot/1.0`, each run once and parsing (Fed calendar page 56 meetings, ACM file, ECB, BoE, MoF); refusals: none.
- **Treasury-dealer exits:** BOND now holds the theme `combo:treasury-dealer-exits` (KB-BND-600); first member Commerzbank weighing a partial exit from US Treasury trading (card 20261124-018 item 12, title only). No row moves on it.

## 5. TERRY's postmortem ask

Your brief named TRY-FIRE-006; the TLT 77 put is **TRY-FIRE-004** (006 is the Kharg/USO card). BOND's grade of its share: **MIXED**: direction right (10Y 4.55 → 5.29, 7/17 → 9/30), term-premium leg partly right (KW +30bp), inflation leg wrong (breakevens +12bp), and most of the move came through the policy path (2Y +70bp), the channel the card was not built on. One stated disagreement with LIQUID's share. Packet: `AGENTS/TERRY/inbox/2026-11-25_from-BOND_try-fire-004-thesis-grade-and-auction-week.md` (with a no-card read of the auctions and HY). KB-BND-601.

## 6. Forward view (unscored; no row registered this session)

- **December refunding** (3Y 12/7, 10Y-R 12/8, 30Y-R 12/10): about 65% that at least one fires I′ (base rate 49% across three; the current run is five fires in ten); about 5% that any shows a full composition failure. Over the next two weeks.
- **WQ-291 dealer leg (about 12/3):** lean NOT MET, about 75%: dealers were awarded only $6.258B of the 5Y against an $8.6B bar.
- **12/9 FOMC:** a hike is priced; a hawkish SEP with the belly cheapening into the refunding is the path that would turn the I′ marker cluster into a dealer-inventory problem. What would change BOND's mind: dealers above max at any refunding auction.

## 7. Question for Will (via PROME; doubt on a C10 grade goes to Will)

VX-BND-13's row carries two written rules that disagree: its red text ("indirect below the trailing-12 MIN at 2+ auctions inside 30 days") is met; its notes reserve 4 for the dealer conjunct, which is not met. BOND moved the score to 3 only and recommends keeping 3 and rewriting the row so one text governs. Not registered as a WILL_QUEUE row by BOND (PROME's rail).

## COMPLETION — BOND — 2026-11-25
STATUS: ✅ DONE
CHANGED: AGENTS/BOND/{STATUS,SCRATCH,RECEIPT,NEXUS_BRIEF}.md, workbook/KB.tsv (KB-BND-592 to 601, 10 stale flips), workbook/VX.tsv (01,02,04,08,13), thesis/PREDICTIONS.tsv (BND-34 TRUE), docket/CATALYSTS.tsv + archive, board_log.tsv, registry/corrections_receipts.tsv, monitors/rates_context.py, monitors/dm_cross_section.py, analysis/2026-11-25_month-end/, inbox moves; packets to TERRY and WALTER; this memo
RESULT: All four graded REGISTERED: TIPS clean, 2Y I′ fire (51.54 vs 54.67), 5Y I′ fire (54.28 vs 59.42; OLD indirect −0.03 residual), 7Y clean (58.20 vs 57.43, cover +0.01); counter 2 → 1; no composition failure; dealers light, directs filled. HY above 350 since 11/19: HY function 3 → 4, BND-34 TRUE, composite 18; VX-BND-13 2 → 3. Inbox 37 of 37 drained; WQ-735 2 scripts switched, 0 refusals; TRY-FIRE-004 BOND share MIXED.
GAPS: No tail (no when-issued from Treasury). WQ-291 dealer leg unpublished until about 12/3. FR2004 10/21 revision cause unchecked. 12/9 curve-shape row (self-set due 12/2) and VX-BND-20 review (due 11/25) re-dated to 12/3. SKIPPED: closeout consumer scan for the composite 17/35 → 18/35 (declared once; it matched only dated history, 75 own and 26 cross hits; history not rewritten; the one current-looking consumer is DAEDALUS FLEET_MAP.tsv, row dated 11/18). Not pushed (PROME pushes).
WILL_NEEDS: VX-BND-13 red-text vs notes conflict: BOND recommends hold 3 and one governing text (§7).
FOLLOW-UP: PROME wake for BOND Thu 12/3 after 16:15 ET (WQ-291 grade, freeze December refunding bars before 12/7 or the grades are audit-only, F2 12/2, 12/9 row, VX-BND-20).
