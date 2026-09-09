# Trade obligations — September 8 migration record

Will approved the BRENT cleanup in this session. Supersedes the unfinished tranches/plan in the [before-image](../archive/2026-09-08_cleanup/workbook/TRADE_OBLIGATIONS.md). Original TRADE: 156,190 UTF-8 bytes, preserved unchanged with SHA-256 and CRC32 in the [archive manifest](../archive/2026-09-08_cleanup/manifest.json).

The inventory separates rule identity, disposition and decision-time reader. A script checking feed health or a timestamp is not a reader of trading rules. The actual human route is CLAUDE step 1 → TRADE Decision read paths → complete relevant spec(s); it explicitly applies when a session becomes trade-relevant after boot. Step 6c independently reaffirms pending execution rows. TRACKER points routines to the surviving frame-breaker; routines record/flag and cannot approve.

## Preserved binding excerpts

Source line ranges below refer only to the archived before-image, never to a shifting live file. The [machine inventory](TRADE_CLAUSES.json) records exact excerpt SHA-256, source range and destination. LIVE means its stated scope; dated examples and retired-gate evidence caveats do not become current market observations.

| ID | Obligation | Disposition | Source lines | Destination / complete reader | Authority / reconciliation |
|---|---|---|---|---|---|
| BG-01 | Retirement and surviving authority | LIVE | 217–225 | [setups/SPECS_GATES.md](../setups/SPECS_GATES.md); proposal | Will retirement 2026-08-07; WQ-189/192 2026-09-07 |
| BG-02 | Frame-breaker, prospective capacity floor and constraints | LIVE | 251–256 | [setups/SPECS_GATES.md](../setups/SPECS_GATES.md); proposal | WQ-189/192; PROME/proposals/2026-09-07_wq189-192-RULED.md |
| BG-03 | Leg (b) economics | LIVE | 245–245 | [setups/SPECS_GATES.md](../setups/SPECS_GATES.md); proposal | 2026-08-07 survival; WQ-189 untouched leg (b) |
| BG-04 | Tenor purpose and dated eligibility example | LIVE | 159–163 | [setups/SPECS_GATES.md](../setups/SPECS_GATES.md); proposal | 2026-08-03 tenor ruling; 2026-08-21 scope amendment |
| BG-05 | Roll scope and guard | LIVE | 165–175 | [setups/SPECS_GATES.md](../setups/SPECS_GATES.md); proposal | Will 2026-08-21; existing October holding NO ROLL overrides permission to propose |
| BG-06 | Pre-fill disclosure and instrument terms | UNRESOLVED | 258–263 | [setups/SPECS_GATES.md](../setups/SPECS_GATES.md); proposal | 2026-08-04 disclosure; trigger names retired leg (a) |
| BG-07 | Premise control and binding caveats | LIVE | 265–271 | [setups/SPECS_GATES.md](../setups/SPECS_GATES.md); proposal | TERRY adoption 2026-08-04; v3 retirement preserves record |
| BG-08 | Live conversion rule | LIVE | 470–470 | [setups/SPECS_GATES.md](../setups/SPECS_GATES.md); proposal and position-review | DM-v1 vehicle ruling 2026-08-07; corrected 2026-08-12 |
| BG-09 | Surviving gap watches | LIVE | 870–870 | [setups/SPECS_GATES.md](../setups/SPECS_GATES.md); monitoring and proposal | Explicit retirement rider 2026-08-10: watches only, no gate |
| BE-01 | Hardened trigger | LIVE | 499–499 | [setups/SPECS_OFFRAMP_ENTRY.md](../setups/SPECS_OFFRAMP_ENTRY.md); proposal | Will 2026-07-29 trigger; v5 amendment 2026-07-31 |
| BE-02 | Day+2 admission limit | LIVE | 505–510 | [setups/SPECS_OFFRAMP_ENTRY.md](../setups/SPECS_OFFRAMP_ENTRY.md); proposal | Will 2026-08-07 |
| BE-03 | Signature plus paired T/C entry | LIVE | 512–514 | [setups/SPECS_OFFRAMP_ENTRY.md](../setups/SPECS_OFFRAMP_ENTRY.md); proposal | Stage-A v5 2026-07-31 |
| BE-04 | T and C frozen definitions | LIVE | 528–531 | [setups/SPECS_OFFRAMP_ENTRY.md](../setups/SPECS_OFFRAMP_ENTRY.md); proposal | 2026-07-31 v5; 2026-08-05 v6 measurement |
| BE-05 | Measurement basis and its limits | LIVE | 550–554 | [setups/SPECS_OFFRAMP_ENTRY.md](../setups/SPECS_OFFRAMP_ENTRY.md); proposal | 2026-08-07 re-derivation |
| BE-06 | T1 one grade per session | LIVE | 557–557 | [setups/SPECS_OFFRAMP_ENTRY.md](../setups/SPECS_OFFRAMP_ENTRY.md); proposal | Will 2026-08-05 |
| BE-07 | T2 close-basis veto of remainder | LIVE | 558–558 | [setups/SPECS_OFFRAMP_ENTRY.md](../setups/SPECS_OFFRAMP_ENTRY.md); proposal | Will 2026-08-05 |
| BE-08 | Intraday evidence limits | LIVE | 560–560 | [setups/SPECS_OFFRAMP_ENTRY.md](../setups/SPECS_OFFRAMP_ENTRY.md); proposal | Will 2026-08-05 |
| BE-09 | Frozen boundaries and pairing | LIVE | 563–567 | [setups/SPECS_OFFRAMP_ENTRY.md](../setups/SPECS_OFFRAMP_ENTRY.md); proposal | Will 2026-07-31 |
| BE-10 | Mandatory calibration caveat | LIVE | 569–573 | [setups/SPECS_OFFRAMP_ENTRY.md](../setups/SPECS_OFFRAMP_ENTRY.md); proposal | Will 2026-07-31 carry-verbatim instruction |
| BE-11 | First tranche | LIVE | 576–576 | [setups/SPECS_OFFRAMP_ENTRY.md](../setups/SPECS_OFFRAMP_ENTRY.md); proposal | Will 2026-07-31; 2026-08-05 measurement |
| BE-12 | Second tranche | LIVE | 577–577 | [setups/SPECS_OFFRAMP_ENTRY.md](../setups/SPECS_OFFRAMP_ENTRY.md); proposal | Will 2026-07-31; 2026-08-05 T2 |
| BE-13 | Maximum loss | LIVE | 578–578 | [setups/SPECS_OFFRAMP_ENTRY.md](../setups/SPECS_OFFRAMP_ENTRY.md); proposal | Will half/half sizing 2026-07-31 |
| BE-14 | Vehicle, tenor, strikes and execution window | LIVE | 665–666 | [setups/SPECS_OFFRAMP_ENTRY.md](../setups/SPECS_OFFRAMP_ENTRY.md); proposal | Will 2026-07-30 Option B |
| BE-15 | Proposal authority and interaction | LIVE | 786–790 | [setups/SPECS_OFFRAMP_ENTRY.md](../setups/SPECS_OFFRAMP_ENTRY.md); proposal | Will 2026-07-21; arm retired 2026-08-07 |
| BE-16 | Molecule scope of the premise | LIVE | 497–497 | [setups/SPECS_OFFRAMP_ENTRY.md](../setups/SPECS_OFFRAMP_ENTRY.md); proposal | 2026-07-30 scope correction |
| BH-01 | Harvest precedence | LIVE | 670–670 | [setups/SPECS_TRADE_RULES.md](../setups/SPECS_TRADE_RULES.md); position-review | Will Option B 2026-07-30 |
| BH-02 | H1 announcement clock | LIVE | 674–675 | [setups/SPECS_TRADE_RULES.md](../setups/SPECS_TRADE_RULES.md); position-review | TRADE explicit Will 2026-07-31 anchor amendment supersedes original line 580 |
| BH-03 | H2 profit harvest | LIVE | 676–676 | [setups/SPECS_TRADE_RULES.md](../setups/SPECS_TRADE_RULES.md); position-review | Will 2026-07-30 |
| BH-04 | H3 reversal exit | LIVE | 677–677 | [setups/SPECS_TRADE_RULES.md](../setups/SPECS_TRADE_RULES.md); position-review | Will 2026-07-30 |
| BH-05 | Harvest calibration limitation | LIVE | 681–681 | [setups/SPECS_TRADE_RULES.md](../setups/SPECS_TRADE_RULES.md); position-review | Will 2026-07-30 |
| BH-07 | Original persistence letters awaiting applicability reconciliation | UNRESOLVED | 645–659 | [setups/SPECS_TRADE_RULES.md](../setups/SPECS_TRADE_RULES.md); proposal and position-review | Original 7/29 and 7/31 letters; WAR-RISK-HALVES retired 8/7; Will 8/21 successor is prompt-only |
| BH-10 | Dated mark-monitoring rider | UNRESOLVED | 58–58 | [setups/SPECS_TRADE_RULES.md](../setups/SPECS_TRADE_RULES.md); position-review | 8/27 standing mark watch; later holding-specific WQ-145/167/168 takes precedence |
| BH-12 | Do not blend transit series | LIVE | 369–369 | [setups/SPECS_TRADE_RULES.md](../setups/SPECS_TRADE_RULES.md); all trade-relevant evidence | HORMUZ_TRANSIT_BASELINE standing basis rule |
| BH-13 | Retired source exclusions | LIVE | 372–372 | [setups/SPECS_TRADE_RULES.md](../setups/SPECS_TRADE_RULES.md); all trade-relevant evidence | July 21 source retirement, reiterated August 3 |
| BH-14 | AIS undercoverage caveat | LIVE | 378–378 | [setups/SPECS_TRADE_RULES.md](../setups/SPECS_TRADE_RULES.md); all trade-relevant evidence | August 3 disclosure, strengthened by August 17 instrument impeachment |
| BH-15 | Single-outlet source restriction | LIVE | 419–419 | [setups/SPECS_TRADE_RULES.md](../setups/SPECS_TRADE_RULES.md); all trade-relevant evidence | August 3 source correction; sole-source restriction retained |
| BH-16 | Historical verification debt | UNRESOLVED | 310–310 | [setups/SPECS_TRADE_RULES.md](../setups/SPECS_TRADE_RULES.md); before reusing the historical grade | No inspected completion receipt for the specific August 3 OVX second-witness ask |

## Additional dispositions

| ID | Obligation / disposition | Current home and reader | Evidence |
|---|---|---|---|
| BE-01b | Alternate no-deal transit trigger, UNRESOLVED | Entry spec BE-01b, before proposal | Original line 499 OR branch; no repaired live measurement path established |
| BS-01 | Current stance / frame-breaker stand down, LIVE | TRADE Current stance; all decision routes | Current before-image lines 5–8; WQ-189/192 |
| BS-02 | USO shares 37, no scaffold ratification, LIVE | TRADE Positions; review | September 9 correction from newer September 3/9 broker mirrors; research/2026-09-09_squeeze-review/REPORT.md |
| BS-03 | October 135C ×1, sale-price UNKNOWN/no re-ask, A/B/C and NO ROLL, LIVE | TRADE Positions; review | WQ-145/167/168, before-image current mirror |
| BS-04 | September 150/165 spread ×1 HOLD to expiry, LIVE | TRADE Positions; review | WQ-168 §3, before-image current mirror |
| BS-05 | XLE ×2 selected September 9 open exit, receipt PENDING, LIVE | TRADE Positions and execution log; step 6c + review | WQ-168 §7, before-image current mirror; no broker action inferred |
| BS-06 | Reaffirm pending rows; execution evidence differs from a handoff, LIVE | CLAUDE step 6c → TRADE execution log | July 27 hygiene adoption, original lines 820–822; existing guard retained |
| BS-07 | Option observation date separate from rule update, LIVE | TRADE header → existing ledger freshness reader | Two-clock distinction retained; September 9 delayed quote capture in TRADE evidence, not a broker mark |
| BH-06a | WAR-RISK-HALVES RETIRED | Holding spec BH-06, before proposal/review | REGISTRY retirement August 7; not the July 31 Worldscale retirement |
| BH-06b | STAGE-A-AIS RETIRED | Holding spec BH-06, before proposal/review | REGISTRY August 7, feed did not exist |
| BH-06c | KILL-LEG2-TRANSIT RETIRED; JWC successor prompt-only LIVE | Holding spec BH-06, before proposal/review | Will August 21 ruling linked there; instrument failure, premise not refuted |
| BH-06d | P&I observation retained; compound institutional exit applicability UNRESOLVED | Holding spec BH-06/BH-07, before proposal/review | Original 25-session letter preserved; no inspected amendment independently retires P&I |
| BH-08 | COT successor sizing-only, both legs gating, per-print NO-VERDICT base case, LIVE | Holding spec BH-08 → full REGISTRY COT-FUEL-35B row, before sizing | August 14 registration and own per-print default; old COT-FUEL numerical REVERT test RETIRED |
| BH-09 | Exposure facts vs TERRY sizing; dated concentration is not current valuation, LIVE | Holding spec BH-09, review | Original lines 28–149; current one-call quantity supersedes old two-call marks |
| BH-11a | Spread receipt approximate, exact fill unestablished, UNRESOLVED | Holding spec BH-11 + TRADE, review | Original line 820; no new receipt supplied; current owner instructions prevail |
| BH-11b | Pre-trigger convex starter remains declined, LIVE restriction | Holding spec BH-11, before proposal | June 29 decision at original line 829; reopen only if Will requests |
| BX-01 | v1/v2/v3 arm mechanics, tiers, clock, re-ratchet SUPERSEDED | Provenance archive; surviving BG-01–03 govern | August 7 retirement; no current OVX release condition |
| BX-02 | Old per-tranche H1 rider SUPERSEDED | BE-13 note and BH-02 govern | Later explicit July 31 announcement day+9 anchor at original lines 674–675 |
| BX-03 | Unverified tanker tally UNRESOLVED evidence; cannot cite | BE-10; full entry read | Original line 573; no new calculation fabricated |
| BX-04 | Directional/dispersion/v4 entry and transit entry SUPERSEDED | BE-03–12 govern | v5 July 31 and v6 August 5 amendments |
| BX-05 | July tail-rider ticket completed; old order menus SUPERSEDED | Current holding and BH-11 govern | July 24 fill; WQ-168 §3; old green-day approval not repeat authority |
| BX-06 | Second manual calendar SUPERSEDED | TRADE pointer → canonical docket / generated STATUS | September 7 generator plus this approved cleanup; FASTOW repointed |
| BX-07 | July fresh-leg re-arm reader SUPERSEDED with retired arm | Archive line 476; BG-01 governs | Arm retirement August 7. Any re-arm needs its own registration, not reuse by implication |

## Whole-file accounting

Every section, including the dated containers, was reviewed. The archive is provenance, not a source of new standing orders. Surviving source restrictions, unresolved verification debt and the mark-watch rider were extracted as well as obvious trade gates.

| Original range | Disposition after extraction |
|---|---|
| 1–27 | Current stance/holdings/header retained in TRADE; stale valuation context retired |
| 28–149 | Dated concentration/marks archived; current quantity wins; exposure obligations BH-09, mark-watch BH-10 |
| 150–184 | Binding tenor/roll BG-04/BG-05; old expiry eligibility dated only |
| 185–272 | Retirements/survivors BG-01–07; original arm mechanics superseded |
| 273–492 | Dated pre-fill/behavioral/vehicle history archived; tenor duplicated in BG-04; conversion BG-08; source restrictions BH-12–15; outstanding historical verification BH-16; old re-arm pointer BX-07 |
| 493–502 | Hardened trigger BE-01; molecule scope BE-16; old rhetorical/three-day basket superseded |
| 503–793 | Entry BE-02–15; persistence BH-06/07; harvest BH-01–05; sizing successor BH-08. Prior clock and v4 contradictions expressly superseded; calibration caveat retained verbatim |
| 794–833 | Filled rider/old menus history; current spread holding governs; receipt/starter restrictions BH-11 |
| 834–843 | Cross-agent arm matrix historical with retired arm; current owner boundaries stay in CLAUDE/NEXUS |
| 844–858 | Current pending state retained; old execution/mark rows archived |
| 859–873 | Calendar replaced by pointer; surviving gap watches BG-09 |
| 874–end | Historical archive navigation retained in before-image |

## September 8 workbook reconciliation follow-up

All 37 original excerpt hashes match the archived source. At their live destinations, 36 excerpts match exactly; BE-02 differs only in the required relative hyperlink repair (`RULINGS.md` to `../RULINGS.md`). Its operative wording is unchanged. The earlier JSON is a dated migration receipt, not current health state. New measured receipt: [RECONCILIATION_2026-09-08.json](RECONCILIATION_2026-09-08.json).

The next ordinary-closeout growth check has now been observed after the catch-up and batch 2 passes: TRADE remains 6,781 bytes, equal to the cleanup baseline, with dated findings written to research notes. This is a completed measured instance, not a promise about future growth. Remaining rule-applicability and broker-evidence gaps above remain open at their complete readers.

## Acceptance and remaining boundaries

See [CLEANUP_VERIFICATION.json](CLEANUP_VERIFICATION.json) for snapshot checks and byte budgets, and [cleanup report](../setups/2026-09-08_cleanup-report.md) for live checks. Representative routes: structural proposal reads BG + BH; off-ramp proposal reads BE + BH; mid-session frame-breaker reads BG + BH; position review reads holdings + BH and the relevant owner card. Each complete named file fits the 32,550-byte budget. This verifies reachability and retained content, not that a future agent will obey it.

Unresolved applicability/evidence stays explicit at the deciding reader; it is not treated as permission. Cleanup grants no capital authority. Continue to update current action state and receipts in TRADE and place dated reasoning in evidence notes. The first post-cleanup growth check is recorded above; later closeouts must retain that separation.
