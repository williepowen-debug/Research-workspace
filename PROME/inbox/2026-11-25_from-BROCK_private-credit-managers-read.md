# BROCK to PROME: are the private-credit managers leading this selloff? (C8 session, WALTER SIG-W-20261125-013)

**Session:** prome-77 C8 spawn, Wed 2026-11-25, started 11:35 ET; memo written 11:47 ET (`date`). Runtime: Claude Code, Opus 5.5 (claude-opus-5-5), in-process desk from PROME's cwd. Boot files read with `PROME/tools/boot_read.py` to `eof: true`: root CLAUDE.md 4 pages, AGENTS.md 1, USER.md 3, AGENTS/BROCK/CLAUDE.md 6.

## 1. The answer

**Plain market beta, not a private-credit lead.** On the three chip-led down days (11/20, 11/24 and 11/25 intraday) Blue Owl, Ares, Apollo, Blackstone and KKR fell about what their one-year sensitivity to the equal-weight S&P 500 (RSP) predicts. They carry almost no sensitivity to chips beyond that. Against the cap-weighted S&P (SPY), which is chip-heavy, every one of them fell *less* than its beta implied. Today, intraday, all five sit 1 to 3 points below their RSP line, Apollo the most (-2.9 points). That is one shared move, not five independent signals, and no manager is more than 1.5 standard deviations off on any day. The BDCs' calm matches their low beta (0.6 to 0.9). It is not yet information either way: the marks that would carry AI-borrower stress are the 12/31 marks, published in February and March 10-Ks.

## 2. Prices and beta-adjusted moves

Source: FORGE `fetch.py price` read 11:44 ET 11/25 (intraday, not closes); prior closes from `fetch.py --history 400`. Betas: daily closes, 250 sessions to 11/19. Residual = actual minus beta times market; residuals use the 11:37 ET intraday bar, prices the 11:44 ET read. "3 down days" compounds 11/20, 11/24 and 11/25 and leaves out the 11/23 rebound. BROCK computation.

| Ticker | 11:44 ET | Today | Beta RSP | Resid. vs RSP today | 3 down days, resid. vs RSP | 3 down days, resid. vs SPY |
|---|---|---|---|---|---|---|
| OWL | 8.84 | -3.12% | 1.93 | -1.1 pp | -0.0 | +6.1 |
| ARES | 128.45 | -2.86% | 1.95 | -0.8 | +2.9 | +8.4 |
| APO | 114.86 | -4.16% | 1.46 | -2.9 | -2.7 | +1.8 |
| BX | 115.14 | -3.53% | 1.89 | -1.6 | -0.5 | +3.8 |
| KKR | 90.37 | -2.92% | 1.80 | -1.2 | -1.9 | +2.8 |
| BIZD | 12.16 | -0.41% | 0.79 | +0.3 | +1.0 | +2.9 |
| ARCC | 18.60 | -1.32% | 0.83 | -0.6 | +0.2 | +1.7 |
| FSK | 11.08 | -0.72% | 0.88 | +0.0 | +1.6 | +3.8 |
| OBDC | 10.80 | -0.32% | 0.92 | +0.4 | +1.4 | +3.9 |
| BXSL / OTF | 22.94 / 9.17 | -0.95% / -0.76% | 0.70 / 0.85 | -0.3 / -0.1 | -1.5 / -0.5 | -0.5 / +2.1 |
| SPY / RSP / SMH | 698.05 / 211.80 / 394.45 | -2.88% / -1.01% / -7.57% | | | 3 down days: SPY -6.8%, RSP -2.5%, SMH -23.2% | |

- **Three-factor check** (equal-weight market, chips and financials, each separated from the market): chip loading +0.01 to +0.14, financials +0.99 to +1.38. Three-day residuals: OWL +3.4, ARES +4.7, APO -0.1, BX -0.1, KKR -0.2 points. The managers trade as leveraged financials.
- **11/23 rebound:** they rose with the market (+3 to +5%), the opposite of a lead.
- **Whole window 11/19 close to now:** five managers -0.6% raw, -0.7 points vs RSP; BDC wrappers +0.8% raw, +0.8 points vs RSP.
- **My X1 test (b) (do wrappers lead down?):** 11/19 to 11/24 (HY 352 to 372 bp), wrappers ARCC/FSK/OBDC/BIZD +1.64% vs APO/ARES +4.66%: wrong sign again. X1 not met, no rescore (LIQUID already has X1 CLOSED).
- ⚠️ BKLN shows small negative residuals on 11/23 and 11/25; a monthly distribution ex-date may explain them. Not checked, not claimed.

**Is the BDC calm information or lag?** Both. Lag: NAVs are 9/30 marks, and the next marks are 12/31, published February to March. Information: (a) the BDCs' named neocloud loans are each under 1% of net assets (section 3), so a CoreWeave or IREN problem is a single-name hit, not a book event; (b) high yield is wider, but CCC/BB *fell* on the 11/24 widening (6.33 to 6.24; CCC 1,405 / BB 225, FRED): the stress sits in AI single names and upper tiers, not the leveraged-loan tail BDCs own. The price, not the NAV, is the live channel, and it has not moved beyond beta.

## 3. Named AI-infrastructure exposure

| Holder | Exposure | Size against book | Basis |
|---|---|---|---|
| **Blue Owl** (OBDC, OTF, OCIC, OTIC) | IREN GPU facility (IE Mackenzie), 9.00% fixed, Blue Owl agent | $730.0M commitments across four funds; OBDC $61.9M, OTF $69.6M funded at 9/30 | ESTABLISHED, 10-Qs and IREN exhibits (KB-BRK-456/459) |
| Blue Owl BDCs | Nscale first lien; CoreWeave DDTL V-V | Nscale funded OTF $51.2M, OCIC $40.9M, OBDC $4.0M; CoreWeave FV OBDC $9.0M, OTF $9.0M, OCIC $18.1M | ESTABLISHED (KB-BRK-425/435/457) |
| Blue Owl Inc. | Digital Infrastructure AUM $20.4B of $329.9B (6.2%); issuer: "substantially all" counterparties investment grade | names no borrower | ESTABLISHED, Q3 10-Q |
| Blue Owl Inc. | Meta Hyperion SPV about $27B; CoreWeave-tied Richmond data centre $1.1B HY | | REPORTED, press (KB-BRK-172/306) |
| **Apollo** | Apollo Debt Solutions: CoreWeave DDTL V and V-V, FV $17.8M | small against a large fund (NA not extracted) | ESTABLISHED, 10-Q |
| Apollo | SpaceX GPU notes about $44B, Apollo-led; Athene digital infrastructure $12.9B funded at 9/30 | placement shares UNKNOWN | issuer 8-K and Apollo release via WALTER (KB-BRK-530); Athene via SHADE (KB-BRK-462) |
| **Ares** | Ares Core Infrastructure Fund: CoreWeave DDTL FV $56.0M | 0.72% of NA $7,725.8M | ESTABLISHED, 10-Q |
| Ares | ARCC and ASIF: Vantage Data Centers subordinated 9.50%, at par | ARCC $195.9M; ASIF $301.0M data-centre subtotal = 3.04% of NA | ESTABLISHED; Vantage is hyperscaler-tenanted, a different risk from a neocloud |
| Ares | data-centre earnout contingent up to $1.0B; CEO 10/29: does not underwrite GPU depreciation | | 10-Q; transcript via helper (KB-BRK-487) |
| **Blackstone** | BXPE lists CoreWeave and Anthropic among top PE holdings (equity); BCRED Vantage inside Emerald JV | sizes not stated / not extracted | ESTABLISHED names, UNKNOWN size |
| **KKR** | no CoreWeave, Nscale, IREN or Vantage hit in KKR or FSK Q3 filings; KKR-advised accounts anchor the SpaceX lease | | SEARCH-NOT-FOUND; issuer statement (KB-BRK-399) |
| Others | Trinity Capital AI equipment loans 13.5% of NA (the one BDC with a GPU-type book); HPS Corporate Lending holds RD Michigan Property Owner I at 91.9 of par | Oracle link to RD Michigan INFERRED from press | KB-BRK-486; 10-Q |

- **Oracle-linked loans:** none named in any manager or BDC filing I read. Search terms CoreWeave, GPU, Oracle and Hyperion returned zero in all five managers' own 10-Qs (EDGAR full text). A manager 10-Q reports AUM and fees, not fund loan books, so that zero is SEARCH-NOT-FOUND, not absence.
- **Unknown:** each manager's total AI exposure across all its funds; any mark after 9/30; who holds the SpaceX notes beyond named anchors. LIQUID's CDS reads (CoreWeave 1,314 [11/24], 1,363 odd lot [11/25]; Oracle 362) are borrower stress, not lender loss.

## 4. My registered rows, gates and predictions

| Item | Read | Grade |
|---|---|---|
| BRK-07 (AI markdown forces BDC write-down >$500M, 6/30/2027) | no write-down; marks are 9/30 | nothing to grade |
| BRK-16 (HTGC >15% NAV, 12/31) | HTGC +2.8% since 11/19 close | nothing to grade |
| BRK-25 (arm's-length sub-90 BDC loan, count 2) | HPS's 91.9 is a mark, ING's sale is a bank's | count stays 2 |
| X1 / test (b) | wrong sign (section 2) | not met, no rescore |
| W3 channel 4 (CCC/BB at or under 5.93, twice) | 6.24 [11/24] | not met; W3 grades 11/30 |
| GATE-BRK-R2 | no new fill data | next reads ~12/04-12/07, review 12/07 |
| APO line ($100, "ALL" signal) | $114.86 | 14.9% above; nothing fires |
| Car-Mart (BRK-33 TRUE 11/24) | EDGAR feed holds nothing after the 11/24 08:23 ET petition 8-K (read 11:43 ET); stock $0.36 (+9.4%, 11:44 ET) | successor reads: 11/30 escrow, ~12/01 Nasdaq notice, **12/03 rollover documents**; Cable One grace about **12/16** |

No score, level, operator, instrument or consequence changed. Convergence 58/70.

## 5. Will's 11/24 question: which client string did BROCK's refused fetches send?

- **What refused me on 11/24:** IREN's investor site (iren.gcs-web.com), HTTP 403 at 22:35 ET; the only refusal in my 11/23 and 11/24 records (KB-BRK-527). Not retried, not bypassed.
- **Which string:** the fetch went through the Claude Code WebFetch tool, not a BROCK script. BROCK owns no script that fetches a web page (`AGENTS/BROCK/scripts/` and `tools/` contain no network call). The tool sets its own client string; BROCK neither chose nor changed it. Today, reading a header-echo page through the same tool, it sends `Claude-User (claude-code/2.1.328; +https://support.anthropic.com/)`. The version on 11/24 is not recorded; the form is the tool's own (INFERRED unchanged).
- **WQ-735:** no packet was addressed to BROCK (not in `inbox/` or `inbox/processed/`), and the 11/23 honest-name report lists no BROCK source. Nothing was switched, before or after the refusal, so the refusal was not caused by a script change of mine. SEC reads today used the declared contact string from `scripts/sec_contact.py`, unchanged.
- **WQ-735 reply line:** switched 0 scripts (BROCK owns none that fetch); refusals: iren.gcs-web.com 403 on 11/24 under the WebFetch tool's own string, not retried.

## 6. Inbox: 11 of 11 WALTER cards dispositioned (`board_log.tsv`, `git mv` to `processed/`)

| Card | Disposition |
|---|---|
| 20261125-013 (IMMEDIATE, ACTION) | acted: this read (KB-BRK-531 to 533) |
| 20261125-018 (ACTION) | acted: HY 372 verified at FRED; CCC/BB fell (KB-BRK-535) |
| 20261124-018 (ACTION) | acted: items 3, 4, 6 logged under combination watch (KB-BRK-534); item 8 is CYPHER's |
| 20261124-022 | acted: LIQUID's gates and issuance read used here |
| 20261124-007, 20261125-001, -005 | noted, context |
| 20261124-021 | noted; COR-20261124-21 receipted NO-OP (`registry/corrections_receipts.tsv`) |
| 20261124-015, -016, 20261125-009 | info-only (other desks' domains) |

Top-level `inbox/` held no direct packets.

## 7. Forward view (unscored; not registered)

**Expect (about 60%):** through mid-December private credit stays a high-beta equity story plus single-name AI credit stress; no named markdown, gate or cut traceable to AI borrowers before the 12/31 marks print in February. **Meaningful alternative (about 25%):** AI-borrower stress reaches a credit book first through a deal: a pulled or repriced AI financing with a named alternative-manager lender (the CoreWeave $4B contract-backed loan launch is the nearest test). Then managers lead the equal-weight market by more than 2 standard deviations on more than one day. **About 15%:** chips recover and the manager discount closes with them.

| What would show private credit joining | Odds | When I would expect to see it |
|---|---|---|
| A named AI-infra line in a Blue Owl BDC (IREN facility, Nscale, CoreWeave) marked under 95 of cost at 12/31 | about 35% | OBDC/OTF/OCIC 10-Ks, about mid-February to March 2027 |
| A pulled or repriced (50 bp or more wider) AI deal with an alt-manager lender | about 30% | by 12/16 |
| BCRED or Monroe Q4 fill under 100% (third R2 vehicle; driven by the existing redemption wave, not AI) | registered: BRK-34 30% for BCRED at or above 55% | letters ~12/04-12/07 |
| OTF cuts its base dividend (Q3 NII 0.83x cover, one quarter of spillover) | about 35% | Q4 declaration, about early February 2027 |
| A manager's own financing pulled or downgraded | under 10% | none dated |

**What would change my mind:** manager residuals below -2 standard deviations on two sessions with chips flat; BDC prices down more than 3% beta-adjusted; CCC/BB rising during an HY widening; any named AI-line markdown or a fund gate citing AI marks.

## 8. Sent and committed

TERRY `9ac6306589` (my view: no card; what would make it tradeable). VULCAN `867cfdb13d` (named lines in manager-affiliated vehicles). No WALTER signal: nothing fired. Desk commit: see the COMPLETION block's follow-up message. No push (PROME pushes).

**Skipped at boot, with reasons:** step 0 `git pull --rebase` (the tree carries HOMER's uncommitted files); step 2 LESSONS not re-read (read at the 11/24 session; the charter's standing traps applied); step 4 `dashboard.py` not run (load-bearing series pulled directly with `fetch.py`).

## COMPLETION — BROCK — 2026-11-25
STATUS: ✅ DONE
CHANGED: AGENTS/BROCK STATUS, KB (531 to 535), board_log, 11 inbox moves, corrections_receipts, catch-up 11/25, SCRATCH, NEXUS_BRIEF; packets TERRY, VULCAN; this memo
RESULT: Managers fell with their beta to the equal-weight S&P on 11/20, 11/24 and 11/25, near-zero chip loading; today all five 1-3 pp under that line intraday (Apollo most), one common factor. BDC calm matches low beta; marks are 9/30. Named neocloud lines each under 1% of a vehicle's NA; largest named commitment Blue Owl's IREN $730.0M; manager 10-Qs name no AI borrower. CCC/BB fell on the 11/24 widening. No score moved, 58/70.
GAPS: post-9/30 marks unknown until February 10-Ks; managers' fund-level AI totals unknown; BKLN residual possibly ex-date; BCRED Vantage size not extracted; no pull (others' dirty tree).
WILL_NEEDS: None. For his 11/24 question: IREN's site refused the WebFetch tool's own client string; BROCK switched nothing under WQ-735.
FOLLOW-UP: W3 grades 11/30; CRMT 11/30, ~12/01, 12/03; BCRED/Monroe letters ~12/04-12/07 and R2 review 12/07; CABO ~12/16; Blue Owl BDC 10-Ks Feb 2027 for the AI-line marks.
