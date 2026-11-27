# VULCAN -> PROME: VULCAN-194 VOID; slot 12, S2 row, GPU reading 12; secondaries at primaries; inbox drained (D:L1214, D:L1225)

**Written:** 2026-11-27, about 13:25 ET · VULCAN, spawned by PROME prome-80 (context 2b805141), laptop · Claude Code, Opus 5.5 (claude-opus-5-5); session id not exposed (UNKNOWN). $0.
**Boot reads (bounded reader, each to eof: true):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 3 · `AGENTS/VULCAN/CLAUDE.md` 6 (STATUS 5). No pull: HENRY's dirty files and staged renames sit in the shared index; `git fetch` showed 0 ahead / 0 behind at 12:59 ET.

## 0. In plain words

Nothing fired; the composite stays 15/25. My forecast on Nvidia's quarterly report (10-Q) is void by its own rule because the report has still not been filed. The weekly reading shows the AI giants' share of the S&P edging down while the equal-weight index leads, which moves my concentration tripwire further from firing. GPU rental list prices are holding, but the index of actual deals slipped about 6% in two weeks. The next real test of AI financing is CoreWeave's $4.5B Meta-backed loan, not launched yet. Its pass, orange and red levels are written down below, before the launch.

## 1. VULCAN-194: VOID (D:L1214)

| Item | Value | Source, time |
|---|---|---|
| Registered criterion | "If the 10-Q is not filed by 2026-11-25 (EDGAR model latest bound), VOID with the reason stated" | `workbook/PREDICTIONS.tsv` row as registered 11/19 |
| EDGAR state | **No 10-Q and no NT 10-Q.** Newest Nvidia filings: Form 4 0001696841-26-000016 and 8-K 0001045810-26-000090 (Item 5.02), both 11/23 | data.sec.gov submissions CIK0001045810 (client string SEC requires, from `scripts/sec_contact.py`), 13:00:52 ET 11/27 |
| Grade | **VOID**: not filed by 11/25. Not a HIT or a MISS; P=0.15 not scored | KB-VULCAN-484; row moved to `AGENTS/VULCAN/archive/PREDICTIONS_RESOLVED_2026-11.tsv` |
| Terms | unchanged. Not rolled to the filing (that would be a new forecast, Will's) | as agreed in D:L1214 |
| T1 (MoUs converted to definitive financing) | still read at the filing under D:L322, **unscored** | STATUS ② |
| Filing deadline | 12/04, or 12/09 with a Form 12b-25 (my arithmetic, KB-473) | CATALYSTS 12/04 row |

Calibration now: 24 registered · 17 resolved · 1 VOID · 6 OPEN. Lesson L-127: when the issuer has already said "in the coming weeks", anchor a filing forecast on the legal deadline, not on a modelled bound.

## 2. Slot receipts (D:L1225)

| Instrument | Run (ET, 11/27) | Result | Settled-close basis |
|---|---|---|---|
| `mag7.py` slot 12 | 13:04:45 to 13:07:19 from root (dry run 13:01:57) | holdings **25-Nov-2026 (new vintage, not duplicate)**; Mag-7 **32.4779%** (slot 10 32.6020%), NVDA 5.8245% (6.1380%); breadth RSP−SPY 63d **+4.95pp** (97.2 pctile); **below-yellow, NOT FIRED**; validation OK, worst error 0.000% | both legs measured on the holdings date, the **11/25 settled close** (11/26 holiday), not on 11/27 intraday bars |
| `LAYER_SERIES` (same run) | 4 rows | ⚠️ DEGRADED: the vendor failed AVGO (a T1 member) on the written run; excluded weight 2.69%, 63d reconciliation error +0.54pp. The dry run 3 minutes earlier priced AVGO (T1 63d share 53.5%, reconciliation +0.19pp). **Do not cite slot 12's T1 share.** Rows not edited | KB-485 |
| `semi_watch.py` | 13:07:32 | DDR5 spot $60.33 (−0.71%), DDR4 $76.62 (−1.13%); memory core 1mo −34.2. ⚠️ **SNDK silently dropped**: the vendor has no SNDK closes for 11/20 to 11/25 and the tool drops any ticker with one missing day, yet printed "OK - all legs fetched". So the "MU+SNDK" cell is MU alone; MU+SNDK by hand is about −42.8% (SNDK $175.596 [10/28] to $85.36 [11/27]) | 11/27 bars: MU $646.95 and SPY $728.68 the same at 13:01 and 13:14 ET (the half-day close) |
| GPU reading 12 | pages read by curl 13:09; `gpu_panel.py --reading-date 2026-11-27 --write` 13:11, 10 rows | on-demand H100: Lambda $4.59 (re-admitted; the effective-date banner that dropped it is gone), CoreWeave $6.155, Nebius $4.50, Crusoe $3.90 (posted $4.50 from 12/1); mean $4.7862 n=4, matched three-vendor mean $4.8517 unchanged; Vast.ai $2.2689 n=5; SDH100RT $3.07 [11/26]; OCPI $3.19 [11/26] (was $3.39 [11/12]); contract tier none admissible | page vintages 11/26 to 11/27, all hand-read at the slot; input `AGENTS/VULCAN/reports/2026-11-27_gpu-reading12-input.json` |

Both 11/27 CATALYSTS rows are marked FIRED and swept. **The semi_watch defect is mine (L-126):** a repair row is registered before the 12/04 slot. Its acceptance conditions come first: a dropped core ticker must report ERR. The 11/27 row is never rewritten. The SNDK gap stays in the one-month window until about 12/26 unless the vendor backfills it.

Also run this session: `edgar_watch.py` (boot leg 8 was 4 days stale): 35 rows. No Nvidia periodic filing. CoreWeave filed only Form 4s after its 11/10 8-K.

## 3. Two UNVERIFIED secondaries, checked at primaries

| Report | Primary read | Verdict |
|---|---|---|
| Bessent's Nvidia deadline passed 11/25; conflicting reports on Huang | EDGAR: no Nvidia 8-K after 11/23 (13:00 ET 11/27). home.treasury.gov press releases list 11/17 to 11/23, none about Nvidia (13:14 ET). The governing primary on Huang is the 11/23 8-K (Item 5.02): the board reinstated him as President, CEO and director on 11/22 (KB-474) | Deadline passed with **no answer in any filing or Treasury release found**. Huang: per the 8-K. Any later contrary claim is UNVERIFIED |
| Softer tariff proposals for 14 trading partners | USTR release 2026-11-25, "USTR Makes Determinations and Proposes Actions in 14 Section 301 Investigations Relating to Structural Excess Capacity" (read): China, EU, Singapore, Switzerland, Indonesia, Malaysia, Cambodia, Thailand, Korea, Vietnam, Taiwan, Bangladesh, Japan, India (no determination for Mexico or Norway). Proposed "up to" rates: Taiwan, Korea, Japan, Switzerland 15% net of MFN; EU 15%; Malaysia, Thailand, Indonesia, Cambodia, Bangladesh 18%; Singapore 20% (10% with an agreement); India 25% (17%); Vietnam 35% (20%); China up to 20%, and up to 10% on Annex A. Comments due 2027-01-05; **hearings from 2027-01-25**. Federal Register API: no USTR document published 11/20 to 11/27 (only a Brazil Section 301 modification on public inspection for 11/30) | **14 = investigations (one per economy), VERIFIED.** "Softer" is the reporters' word; **the release makes no comparison.** HENRY owns tariffs. ⚠️ **The 12/01 item on my list is the reported Congressional hearings on Nvidia, not the Section 301 hearings,** which start 2027-01-25 (noted on the 12/01 CATALYSTS row) |

Two more titles, both from WALTER card 20261126-005. "Nvidia halts chip shipments to south-east Asia" (FT, title only): UNVERIFIED. No Nvidia filing or statement was found, and the report fits a compliance step under the enacted 11/16 BIS licence rule. No S4 band, S4 stays 3. "CoreWeave debt sale wins IG ratings": see § 5. KB-VULCAN-488.

## 4. Today's credit context: does it change my AI-financing surfaces?

These are other desks' figures; I did not re-derive them. FRED HY OAS 377bp [11/25, a 2026 high]. LIQUID § 3 finds the BB widening BROAD, with AI-adjacent paper over-weighted about 2 times. There has been no valid CoreWeave 5Y CDS trade since the 11/24 close (1,314 clean / 1,359 dirty).

- **No letter moves.** S5 fires on how a new issue clears (a flex or a pull), on regulator collateral, or on a failed posting. Spreads and CDS are prices, and LIQUID grades them. S5 stays 4 (n=2); S1 to S5 scores are unchanged.
- **The reading changes.** The AI-specific credit stress is a single-name story (CoreWeave and the neocloud tier) inside a market-wide repricing. It is not yet a closure of the AI-financing market: payers and labs still raised money in November (SpaceX notes, Anthropic's IPO, MSFT). It also weakens the "OpenAI chain" reading of WALTER card 040's rising co-movement in favour of one broad selloff, though it does not test that.
- **The test that would move my letter** is the CoreWeave $4.5B Meta-backed loan (§ 5). KB-VULCAN-489.

## 5. Inbox drain: before top-level 3 · WALTER/ 14 → after 0 · 0 (`PROME/tools/inbox_census.py`)

| Item | Disposition |
|---|---|
| **WALTER decision card 20261126-005 item 1** (CoreWeave loan "wins IG ratings", my lane) | **Answered** (packet to WALTER). I found no Moody's, S&P, Fitch or DBRS action and no CoreWeave 8-K since 11/10, so ratings stay EXPECTED and the item should not be relayed as rated. **Band set before launch** (registered on the ~12/04 CATALYSTS row): clears at or inside launch talk (7% to 7.5%) = counterevidence; +50 to 100bp = S5 orange; +150bp or PULLED = S5 red; a postponement with no withdrawal = AMBIGUOUS |
| 005 items 2, 4, 7 | SpaceX rent cut: not visible in reading 12. SE Asia halt: UNVERIFIED (§ 3). BoE FSR: noted for LIQUID |
| 040 (co-movement ask) | **No desk test.** 32 sessions inside one selloff cannot separate the two chains. The cheaper resolvers are already registered: the loan launch and Oracle's ~12/15 10-Q |
| 022, 20261127-001 (corrections) | APPLIED to KB-483 and KB-443 notes |
| 031, 035, 036 | noted. No VULCAN record carried 031's lines, so COR-20261125-35 and -36 are NO-OP |
| 024, 039, 041 | noted (CoreWeave bonds, 10-Q maturities, DTCC prices; LIQUID's grade) |
| 033, 038, 044 | info-only |
| 034 | acted: TrendForce 2027 memory forecasts in KB-486 (no contract decline, S2 stays 2) |
| BROCK 11/25 | noted (AI lines in manager vehicles small and near par at 9/30) |
| LIQUID 11/25 | acted (1,363 cancellation applied) |
| ORACLE 11/26 | answered **do-not-pin** (packet to ORACLE) |

Corrections check: 0 NAMED unreceipted (COR-20261125-22 and COR-20261127-01 APPLIED; COR-20261125-35 and -36 NO-OP).

## 6. Sent

- **TERRY** (tradeability, unasked): a reasoned no card from VULCAN. Concentration is falling and breadth is leading; 194 is VOID; GPU rents; the CoreWeave loan test with its pre-stated band, relevant to WQ-745 (terms are TERRY's). Commit 736bf96786.
- **WALTER**: the 005 item 1 and 040 answers. **ORACLE**: do-not-pin. Same commit.

## 7. Forward view (unscored, not registered)

| Event | My odds | Why, and what would change it |
|---|---|---|
| Nvidia files the 10-Q by 12/04 without a 12b-25 | about 0.60 (was 0.70 on 11/25) | Five trading days are left and the company says "coming weeks". A 12b-25 would itself be news about the accounting scrutiny |
| CoreWeave's $4.5B loan launches by 12/11 | about 0.65 | Reported "as soon as next week". A delay past 12/11 with no statement would be the first deal-level sign of strain |
| ⤷ if launched, it clears at or inside talk | about 0.70 | Indications reportedly match the size, and the Meta contract carries the credit. Pulled or +150bp (S5 red): about 0.10 |
| Slot 13 (12/04): Mag-7 under the 33% yellow line | about 0.85 | It would need roughly a +0.5pp move in two weeks in a supplier-led tape |

## 7b. Pending, and what it waits on

- The semi_watch repair waits on my next session, before the 12/04 slot.
- T1 and the rest of the 10-Q owed list wait on the filing (deadline 12/04).
- The S5 letter test waits on the loan launch.
- The 12/01 hearings wait on a committee notice (dates still unverified).
- The mag7 cadence renewal is due by 12/18.
- No session holds open across a laptop sleep (L-123), so the 12/04 slot needs a launch.

## COMPLETION — VULCAN — 2026-11-27
STATUS: ✅ DONE
CHANGED: AGENTS/VULCAN/ STATUS, SCRATCH, NEXUS_BRIEF, LESSONS (L-126, L-127), KB_GENERAL (484-489; notes on 443, 483), KB.tsv, PREDICTIONS + resolved archive (194 VOID), CATALYSTS + fired archive, MAG7/LAYER/S2/GPU series, EDGAR_SEEN, board_log, corrections_receipts, 17 inbox moves (028f2fbf31); packets TERRY, WALTER, ORACLE (736bf96786); closeout commit with this memo
RESULT: VULCAN-194 VOID (10-Q unfiled 13:00:52 ET 11/27). Slot 12: Mag-7 32.4779%, breadth +4.95pp, NOT FIRED. GPU reading 12 written. 15/25 unchanged, no letter. Live S5 test: CoreWeave $4.5B loan launch vs talk, band pre-stated.
GAPS: semi_watch dropped SNDK silently (L-126, repair before 12/04); slot-12 layer rows miss AVGO; Bloomberg, FT and the Yahoo IG item unread; no Congressional committee notice read
WILL_NEEDS: None.
FOLLOW-UP: PROME: launch VULCAN at the 12/04 slot (semi_watch repair first, then slot 13, GPU 13, the 10-Q deadline); a CoreWeave loan launch before then is an S5 IMMEDIATE read.
