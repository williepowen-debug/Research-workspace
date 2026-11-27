# GIBBS -> PROME: inbox drain 11/26 (20 items), nonbank mortgage answer, two exclusions-register flags, forward rows

**Written:** 2026-11-26 22:43 ET (`date`), GIBBS, Claude Code, Opus 5.5 (claude-opus-5-5); session ID not exposed (UNKNOWN). In-process desk spawn by PROME, authority Will 11:38 ET ("catching up on any missed signals"). Boot reads carried to `eof: true` with `PROME/tools/boot_read.py`: root `CLAUDE.md` 4 pages, `AGENTS.md` 1, `USER.md` 3, `AGENTS/GIBBS/CLAUDE.md` 4. `PROME/COMPLETION_SPEC.md` read (Read tool, sections used). boot.py rc 0; corrections check rc 1 on 4 corrections, now rc 0.

**Bottom line:** nothing in the 20 items moves a GIBBS read, tag, prediction or gate. The two items that touch the desk's own exclusions register (Barclays US breaches; a reported $35B capital-reporting error at Citi's UK broker-dealer) are flagged here because that register's classes have no owner. On nonbank mortgage lenders, my records show only one of the 16 splits a line (U.S. Bancorp, about $13.2B, derived from a slide) and nothing comparable to Western Alliance's 87.6% of Tier 1.

## 1. Census (`python3 PROME/tools/inbox_census.py GIBBS`)

| | Top level | WALTER/ |
|---|---:|---:|
| Before | 2 (CYPHER packet + standing `PROTOCOL.md`) | 19 |
| After | 1 (`PROTOCOL.md` only) | 0 |

All 20 items `git mv` to `processed/` in commit `fe2ea51322` (subject carries `consume:GIBBS`). board_log: 19 rows, 5 acted, 14 noted.

## 2. Dispositions

| Item | Disposition |
|---|---|
| CYPHER 11/26 Barclays US (Best Egg, Barclays Bank Delaware, FinCEN) | INTEGRATED: KB-GIB-074 (Barclays US = foreign-bank IHC, not the 16; consequence NONE), KB-GIB-075 (FinCEN). Verified at CYPHER's `research/2026-11-26_due-rows/RECORD.md` sections 3 and 7 |
| SIG-W-20261123-008 (Citi $35B RWA, ING loans, Goldman SpaceX) | acted: KB-GIB-076 (Citi), KB-GIB-079 |
| SIG-W-20261124-015 (FDIC QBP Q3) | acted: KB-GIB-077 |
| SIG-W-20261124-020 (FinCEN) | acted: KB-GIB-075 |
| Corrections: -20261120-010 (MUFG real), -20261123-012 (SpaceX notes priced) | acted: COR-20261120-10 APPLIED (supersedes my 11/19 board_log "NOT FOUND" note; KB-GIB-075); COR-20261123-12 NO-OP (KB-GIB-029 carried no pricing claim; update KB-GIB-079) |
| Corrections: -20261123-003 (VIX timing, Bahrain, V14), -20261125-022 (CoreWeave 1,363 cancelled) | noted: NO-OP receipts, I carried none of the corrected claims |
| Market and volatility cards: -20261120-001, -20261121-001, -20261123-001, -20261124-001, -20261125-005 | noted: tape context for KB-GIB-080; owners VIOLET, HENRY, VULCAN |
| Credit and AI finance: -20261124-002 (REG-T-04 fired), -20261125-013, -018 | noted: context for KB-GIB-079; owners REGINALD, LIQUID, SAM |
| -20261119-019 (HANS: ECB names no bank) | noted: agrees with KB-GIB-071 |
| -20261120-009 (bookmarks) | noted: items 4 and 9 into KB-GIB-075 and -079 |
| -20261124-003 (Car-Mart Chapter 11) | noted: lenders unnamed in the 8-K; BROCK records them as private lenders (KB-BRK-526); none of the 16 |
| -20261125-026 (WSJ debt wall) | noted: Bank of America's default forecast is research, not a book disclosure; BROCK's lane |

## 3. What the drain found (every figure with source and date)

| Finding | Figures | Basis |
|---|---|---|
| 8-K census of the 16, 11/19 to 11/26 | No credit, cyber (Item 1.05) or capital 8-K. Governance only: BAC bylaws (11/20), PNC President Wiedman to the board plus $20M award (11/23), AXP director Angelakis resigns effective 12/2 (11/25). MS 8-K 11/20: carried-interest accounting change effective 10/1, -$719M cumulative to retained earnings at 9/30, prior periods restated | EDGAR submissions and 8-K bodies, 2026-11-27 03:32Z to 03:34Z, `scripts/sec_contact.py` User-Agent; each response named the intended issuer. PRIMARY |
| The 16 vs KRE in the AI-selloff weeks | 11/13 to 11/25: GS -12.60%, MS -12.12%, C -8.61%, JPM -8.51%; 12 of 15 with data fell more than KRE (-4.00%); AXP -2.56%, SCHW +0.51%. Fri 11/20: GS -6.71%, MS -5.32%, C -4.04% vs KRE -1.36%. BK: no data from the tool | Vendor daily closes, `FORGE/tools/market-data/fetch.py`, read 2026-11-27 03:37Z. Cause NOT established; AI-financing exposure is my inference only (KB-GIB-080) |
| Citi, Citigroup Global Markets Ltd (UK) | Reuters (11/19, 11/23, via WALTER): RWA understated $35B, more than 20% of the unit's $155B, about 2.7% of group, a capital injection, resolved "this summer". Citi Q3 10-Q (filed 11/05): CGML "had total regulatory capital of $30 billion at September 30, 2026, which exceeded the PRA's combined buffer and minimum regulatory capital requirements"; no mention of an error or injection. No Citi 8-K 11/19 to 11/26 | 10-Q PRIMARY; the $35B UNVERIFIED (two searches found no copy of the story) (KB-GIB-076) |
| FDIC Q3 profile, CRE by size | Non-owner-occupied CRE past due plus nonaccrual, banks over $250B: 3.076% to 2.781%; fell in every tier but $1B to $10B (1.094% to 1.119%). Multifamily all banks 1.404% to 1.742%; large-bank multifamily noncurrent 0.76% to 0.85% (REGINALD STATUS line 48). HY OAS 372 bp [11/24, FRED first-published, via WALTER and LIQUID] | MIRROR via WALTER and REGINALD; bank-level tiers, not my 10-Q basis, so no READS tag changes (KB-GIB-077) |
| SpaceX GPU financing | Notes priced, about $44B (Apollo 11/20); Goldman-affiliated funds committed; $8.236B bank loan planned, lenders unnamed | WALTER correction card -012 (KB-GIB-079) |

## 4. REGINALD's question: do any of the 16 carry a comparable line to nonbank mortgage companies?

**What my 9/30 records show** (READS item 3 rows, 10-Q and deck reads 10/21 to 11/08; KB-GIB-078):

| Firm | Line | Figure [9/30] | Limit |
|---|---|---|---|
| U.S. Bancorp | Mortgage warehouse plus repo, inside NDFI loans of $50B | 26.3%, about $13.2B | DERIVED from a slide; mapping INFERRED; NDFI criticized under 1% |
| Goldman Sachs | "Other collateralized" includes warehouse clients | $110.453B class, nonaccrual $266M | Not split by collateral type |
| Bank of America | Finance companies, utilized | $100.138B | "Primarily driven by Consumer finance"; no mortgage split |
| Morgan Stanley | Secured lending facilities; collateral includes CRE mortgage loans | $75.342B | No residential-mortgage-company split |
| Truist, Fifth Third | Nonbank financial institutions (asset securitization); NDFI $14.3B | about $19.3B (DERIVED); $14.3B | No mortgage split |
| JPM, WFC, C | BROCK's figure | | No mortgage split recorded |

**Borrower side (REGINALD's report, MIRROR, not re-read at the borrowers' 10-Qs):** UWM's servicing-right-secured lines from Citibank ($1,415M drawn of $2,000M, uncommitted, matures 6/15/2027) and Goldman Sachs Bank USA ($875M of $1,250M, uncommitted); PennyMac repo from Bank of America $1,788M [9/30]. Bank-level call-report Memo 10.a (REGINALD; the line is wider than warehouse): JPMorgan $72,166M (24.3% of Tier 1), Goldman Bank USA $48,367M (88.7%), Citi $43,553M (28.3%), Wells $42,545M (29.7%), Morgan Stanley Bank $32,390M (76.9%).

**What none of it shows:** any of the 16 lending to Freedom or Planet; the servicing-right-secured share at any of the 16; a late or criticized status on these lines (except USB's whole NDFI book under 1%). No figure of the 16 compares with Western Alliance's $7,029M at 87.6% of Tier 1 on the same basis. Tag: NOT-YET-DETERMINABLE. Fitch 11/16 and LIQUID 11/24 are relayed context, not verified here. The FY2026 10-Ks (deadline 2027-03-01) are the first place a split could appear.

## 5. Exclusions-register flags (classes with no owner desk)

1. **Foreign-bank US holding companies:** Barclays US, two breaches in ten days (Best Egg 791,852 people; Barclays Bank Delaware 27,272; Texas AG counts, secondary). Third foreign-IHC sighting in ten days after HSBC US twice. Consequence for the 16: none (KB-GIB-074).
2. **Enforcement or capital-reporting error at one of the 16:** Citi's UK broker-dealer, as above; the same entity and error type as the PRA's 2019 finding ($15.4B at 12/2016, search summary). If a PRA or Fed action, a restated Citi ratio or a 10-K note appears, it becomes a capital-regime item (KB-GIB-076).

## 6. Trade assessment

**No packet to TERRY.** No finding moved a read. The one pattern, GS and MS leading the large-bank fall in the AI-selloff weeks, is a tape fact with no established cause, and market structure is HENRY's. It supports no investment implication from this desk because GIBBS cannot separate AI-financing credit exposure from ordinary trading and banking revenue sensitivity to a tech drawdown. What would change that: an attributed loss, a named counterparty or a reserve build at GS or MS in an 8-K or the Q4 prints (GIB-01's pins).

## 7. Forward rows (`docket/CATALYSTS.tsv`, from primary calendars where reachable)

| Date | Row | Class | Source |
|---|---|---|---|
| 2026-12-18 | Vendor-guidance comment file (P3) | MODELED (~) | unchanged |
| 2027-01-14 | Q4 prints begin (P2), re-dated from 01-13 | FIRM | JPMorgan release 2025-05-21 (Thursday, January 14, 2027, 8:30 a.m. ET; not changed by its 2026-10-27 update) and Citi events page (Thursday, January 14, 2027, 11:00 AM EST), both read 11/26. BAC and BNY 2027-01-15, USB 2027-01-19: search summaries only |
| 2027-02-14 | Q4 perimeter re-cut (P2) | MODELED (~) | unchanged |
| 2027-02-15 | Final 2027 stress scenarios (P3), new | MODELED (~) | Board's October 2025 proposal (search summary); the 2026-09-30 release says the calendar was adjusted, no dates |
| 2027-03-01 | FY2026 10-K deadline (P2), new; GIB-01 grades after it | FIRM | Form 10-K General Instruction A.(2)(a), 60 days for large accelerated filers (not re-read) |

Nothing in my declared cadence falls inside 14 days of 11/26, so EMPTY-FORWARD is the honest state for an event-driven desk. GIB-01 untouched (70% [2026-11-19], Resolve_By 2027-03-15).

## 8. What I could not verify, and what blocked me

- The Reuters $35B Citi figure: two general web searches found no copy; not fetched at Reuters.
- USB's 2027 schedule: businesswire.com returned 403 and was not retried. The BAC newsroom page did not render. Wells Fargo, Goldman and Morgan Stanley Q4 dates not found.
- BK: no price history from `fetch.py`.
- FDIC QBP figures, REGINALD's call-report figures and the UWM and PennyMac lines are MIRROR; I did not re-read them at fdic.gov or at the borrowers' 10-Qs.
- No pull, no push (PROME's instruction). WALTER and WAL files remained dirty in the tree, untouched.

## 9. Commits

- `fe2ea51322` GIBBS drain: STATUS, KB, board_log, CATALYSTS, corrections receipts, archive rotation, 20 inbox renames.
- This memo and `AGENTS/GIBBS/NEXUS_BRIEF.md` (Q4 date and pin; the date is a changed figure under NEXUS schema section 4.1): the next commit, hash in the SendMessage receipt.

## COMPLETION — GIBBS — 2026-11-26
STATUS: ✅ DONE
CHANGED: AGENTS/GIBBS/STATUS.md, workbook/KB.tsv, board_log.tsv, docket/CATALYSTS.tsv, registry/corrections_receipts.tsv, archive/STATUS_ARCHIVE_2026-11-26.md, NEXUS_BRIEF.md, 20 inbox renames to processed/, this memo
RESULT: Drained 20 of 20 items (inbox census 2+19 before, 1+0 after, only PROTOCOL.md left); 7 KB rows (KB-GIB-074..080), 19 board_log rows, 4 corrections receipted (1 APPLIED, 3 NO-OP). No read, tag, prediction or gate moved; no credit or cyber 8-K at the 16 from 11/19 to 11/26; on nonbank mortgage lenders only USB splits a line (about $13.2B, derived), nothing like Western Alliance's 87.6% of Tier 1. Q4 prints re-dated to 2027-01-14 (JPM, Citi at issuer); 10-K deadline row 2027-03-01 added.
GAPS: The Reuters $35B Citi figure is unverified (no copy found). USB date page returned 403 (not retried). WFC, GS, MS Q4 dates not found. BK price history missing. FDIC and borrower-side figures are MIRROR.
WILL_NEEDS: None.
FOLLOW-UP: PROME: two exclusions-register flags (Barclays US, Citi CGML), section 5. Next wake 2026-12-18 (vendor-comment file), then the Q4 prints from 2027-01-14.
