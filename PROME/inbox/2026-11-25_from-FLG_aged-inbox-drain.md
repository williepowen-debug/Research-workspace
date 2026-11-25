# FLG -> PROME: aged-inbox drain, 2026-11-25

**Session:** FLG, Opus 5.5 (claude-opus-5-5) in Claude Code, in-process desk spawn from PROME prome-77 on the laptop, WQ-206 class (aged ACTION at a dark owner), drain only. Started 13:25 ET (`date`); cut by the API outage at about 13:30 ET, resumed 13:37 ET on PROME's message from an unchanged tree; this packet written 13:42 ET (`date`). **Boot reads, bounded reader `PROME/tools/boot_read.py`, each to `eof: true`:** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 3 · `AGENTS/FLG/CLAUDE.md` 4. Also read whole: `STATUS.md`, `inbox/PROTOCOL.md`, `docs/GIT_WORKTREE_PROCEDURES.md`; `TRIGGERS.tsv` and `PREDICTIONS.tsv` by header and rows. `boot.py` rc 1 at boot (inbox only), rc 0 at close. Corrections check rc 0 (no named correction). Not pulled (HOMER and other desks hold dirty files in the shared tree); not pushed (PROME pushes).

## The answer

Nothing graded moved. **One real correction:** the outside auditor was right that FLG tied the NYC rent freeze to $8.5B, a New York State figure; the NYC figure on the same test is **$8,120M at 9/30** (issuer deck), now in the thesis (v1.0.6). **The OCC's $112,000 flood-act penalty** is a small compliance matter from 2022 to 2024 under prior management, outside FLG's mechanism, and is flagged here because it sits in FLG's exclusions register. **The FDIC Q3 profile** shows industry multifamily deterioration that is mostly one other bank (United Fidelity); it is the same channel as FLG's but a different book, and it grades none of FLG's rows. **44 stale knowledge rows** are dispositioned: 26 stale, 3 superseded, 15 refreshed.

## Disposition table (5 of 5, every sender, oldest first)

| Item | Disposition | Where |
|---|---|---|
| PROME 11/16, outside audit item 1 ($8.5B and the NYC freeze) | **ACTED, auditor right.** 10-Q Q3 (acc 0000910073-26-000084): "$8.5 billion ... secured by properties in which at least 50 percent of the units were rent-regulated" sits inside the $14.0B **New York State** multifamily book, and the maturity-table footnote says "located in New York State". The freeze binds NYC only. NYC on the same test, deck slide 16 (8-K acc 0000910073-26-000080): Brooklyn 3,079 + Bronx 2,161 + Manhattan 1,696 + Queens 1,152 + Staten Island 32 = **$8,120M** (9/30); $8,490M at 6/30. Bound check: NYS $14.0B less NYC multifamily $12,857M leaves about $1.1B outside NYC, so NYC's share of $8.5B lies between about $7.4B and $8.5B; $8.12B does. Consumer check on the corrected figure: REGINALD's 9/26 CRE reports say "$8.5B of NYC MF has ≥50% rent-regulated units", which is the deck's NYC $8,490M at 6/30 and right as of its date; no packet owed. Corrected in THESIS (one-paragraph thesis, stage 1, line 172; v1.0.6), STATUS START HERE, KB-033 notes and the fired T-08 row, each with a dated note keeping the earlier text. No level, operator, instrument or consequence changed: no gate, trigger or prediction keys on this figure | KB-FLG-128 · commits below |
| PROME 11/16, stale KB rows (Will's word 11/16 23:16 ET) | **ACTED.** 44 rows, matching PROME's count (Stale_By before the date, status ACTIVE). FLG's rule, written into each row's note: a point-in-time figure a later primary has overtaken goes **STALE**, with a pointer to the row that overtook it; a row a later row explicitly retired goes **SUPERSEDED**; a row the kill rail (`EXIT_PROTOCOL.md`) cites, or a latest-quarter (9/30) figure, is **refreshed** to the print that will overtake it (Q4 release 2027-01-29, Q4 Call Report 2027-02-14, FY2026 10-K 2027-03-01). **26 STALE, 3 SUPERSEDED (004, 022, 025), 15 refreshed** (028, 029, 030, 040, 041, 042, 086, 087, 088, 089, 091, 092, 094, 101, 102). No row deleted; no gate or prediction cites a retired row. Retiring changes status only and moves no figure, so no consumer check is owed for the 44 | KB.tsv header + notes |
| WALTER SIG-W-20261117-016 (small items 11/17) | **LOG.** Item 8, Moody's downgrades a 3,000-unit NYC rent-stabilized portfolio again (Crain's 11/13, title only; not shown to be a Flagstar loan): combination watch, not scored. Items 1 to 7 are other desks', owners named on the card | KB-FLG-127 · board_log |
| WALTER SIG-W-20261118-010 (HY OAS 343, LIQUID >320 x3 MET) | **NOTED.** FLG's refinance math keys on the 5 to 10 year Treasury plus CRE spread, not HY (KB-082, KB-116). LIQUID owns the series; TERRY already has LIQUID's trade read | board_log |
| WALTER SIG-W-20261125-012 (OCC November actions) | **ACTED.** Order read whole at the primary (below) | KB-FLG-125 · board_log |

The 11/16 PROME packets were 9 days old when read: they waited on FLG being dark, not on a wrong assumption by the sender. **WQ-735 (honest client name): no packet was addressed to FLG and none is in its inbox.** FLG's scripts carry no browser string (`ffiec_pull.py` sends FFIEC's credential headers over curl with no client-string override; `extract_filings.py` reads local files). Every fetch this session sent `research-bot/1.0`: OCC and FDIC both answered 200. Nothing to switch.

## The two facts of this week, at the primary

**(a) OCC consent order AA-ENF-2026-45** (`https://www.occ.gov/static/enforcement-actions/eaAA-ENF-2026-45.pdf`, fetched 13:37 ET, HTTP 200, sha256 `5396296dad1dbbe5`; text kept in `AGENTS/FLG/sources/2026-11-25_OCC_flood_order/`).

| Fact | Order text |
|---|---|
| Penalty | $112,000 civil money penalty, Flood Disaster Protection Act sec. 102(f) |
| Violation | 12 CFR 22.7: notify the borrower of inadequate flood cover and force-place cover if not bought within 45 days |
| Scope | a pattern or practice of **82 violations, September 2022 to June 2024**, "under the Bank's previous leadership"; neither admitted nor denied |
| Geography | none stated |
| Signed | board 10/22/2026 (Berlinski, Frank, Lux, Miller, Mnuchin, Otting, Puwalski, Whip); OCC 10/23/2026; announced 11/24 |
| Reservation | OCC may act again if the violations continue or are not corrected |

**Inside FLG's rows:** none. It is about 0.001% of total risk-based capital ($9,804M, 9/30 Call Report) and outside the mechanism (rent-regulated multifamily into reserves and capital). It belongs to the exclusions register's **no-owner mortgage-servicing / compliance residual**, with a governance tint (prior management); it is not a capital raise, CEO change or activist, so the governance class stays QUIET. **Flagged to PROME as the register requires; no action asked.** CORAL's read of the same order agrees on every fact and finds no Florida tie.

**(b) FDIC Q3-2026 Quarterly Banking Profile** (published 11/24; FDIC press release and statement fetched 13:38 ET, HTTP 200). The FDIC states that past-due and nonaccrual rates "increased slightly", that banks reported increases for "multifamily CRE", and that industry reserve coverage (allowance over noncurrent loans, i.e. 90+ days past due or nonaccrual) fell to 169.3%. REGINALD's read (MIRROR): multifamily past-due and nonaccrual, all banks, 1.40% to 1.74%, 89.7% of the rise from United Fidelity. **Inside FLG's rows:** none graded. FLG-01 (H2 gross nonaccrual formation under $600M) grades on Flagstar's own 10-K; no trigger or kill leg reads the QBP. FLG's coverage (30.85%, allowance over nonaccrual loans, 10-Q 9/30) is on a different denominator from the FDIC's 169.3% and is **not compared**. What it does show: another bank placing current multifamily loans on nonaccrual, the same channel that leaves 42% of Flagstar's nonaccrual loans still performing (KB-087). Logged, not scored (KB-126).

## Rows due while dark

None. Predictions, triggers and the quarter clock were clean at boot and at close. Next: T-12 (rent-freeze merits marker) 2026-12-31; T-03/T-07/T-08 at the Q4 release about 2027-01-29 [EST]; T-01 Q4 Call Report about 2027-02-14 (FFIEC token expires 2027-01-31, renew first); FLG-01 at the FY2026 10-K about 2027-03-01, resolve-by 2027-03-15.

**Price (root rule #4):** FLG **$10.68** intraday 11/25 13:38 ET, +2.40% (`fetch.py`); settled $10.43 on 11/24 (REGINALD). REGINALD's ladder is RED (band $11.39), below since the 10/7 close.

## Forward view (unscored, not registered; FLG's judgment)

| Expectation | Odds | Horizon | Why | What would change my mind |
|---|---:|---|---|---|
| The OCC order has no follow-on action or 10-K reserve against Flagstar | 90% | FY2026 10-K, about 3/1/27 | $112,000, a closed 2022–24 period, prior management, signed promptly by the board | a further OCC flood or compliance action, or a 10-K legal note naming a servicing review |
| Q4 gross nonaccrual formation comes in under $327M, so FLG-01 hits | 50% (the row's own amended confidence) | FY2026 10-K | Q3 formation was $273M, the lowest since Q4-2023; against that, a December hike removes refinance relief and the freeze's first quarter is Q4 | Q4 multifamily 30–89 day past dues at the Q4 release well above the $392M of 9/30 |

**Tradeable?** No. Neither fact changes the reserve, the exit channel or any date, so there is nothing for TERRY to price; no packet sent and no card asked. **Signals:** none new for WALTER.

## Owed, with dates

| Owed | Date | Owner |
|---|---|---|
| T-12 rent-freeze ruling, from press, a party release, an 8-K or the 10-Q only (WQ-477 dropped) | 2026-12-31 | FLG |
| FFIEC token renewal before the Q4 Call Report pull | before 2027-01-31 | Will / PROME (laptop token) |
| Q4 release read: cures, formation, NYC rent-regulated book | about 2027-01-29 | FLG |
| FY2026 10-K: grade FLG-01, Q4 roll-forward, rail re-derivation, the OCC order in legal proceedings | about 2027-03-01 | FLG |
| DOCKET L930 prediction-registration brief applies to FLG's next launch brief | from 2026-12-04 | PROME |

## Commits (not pushed; PROME pushes)

| Commit | What |
|---|---|
| 3d1fb88ae2 | drain: STATUS (11/11 block rotated, crc32 03b58157), THESIS v1.0.6, KB 44 dispositions + KB-125..128, board_log 3 rows, OCC order text, 5 inbox moves |
| f528995a0d | NEXUS brief folded to 3d1fb88ae2 |
| this commit | THESIS line 172 and fired T-08 geography notes; this packet |

---
**COMPLETION**
STATUS: DONE
CHANGED: AGENTS/FLG STATUS, THESIS v1.0.6, KB (44 dispositions, 125–128), TRIGGERS T-08 note, board_log, NEXUS_BRIEF, sources/2026-11-25_OCC_flood_order, archive/STATUS_ARCHIVE_2026-11-25; inbox 5 → processed
RESULT: auditor right: freeze binds NYC $8,120M, not NY State $8.5B (fixed); OCC $112K flood penalty, 82 violations 2022–24, immaterial, register flag only; QBP MF rise mostly United Fidelity, grades nothing; KB 26 STALE / 3 SUPERSEDED / 15 refreshed
GAPS: none in scope; QBP multifamily rate and attribution are REGINALD's (MIRROR), the FDIC statement confirms direction only
WILL_NEEDS: none
FOLLOW-UP: T-12 12/31; Q4 release ~1/29/27; FFIEC token before 1/31/27; FY2026 10-K ~3/1/27 grades FLG-01
