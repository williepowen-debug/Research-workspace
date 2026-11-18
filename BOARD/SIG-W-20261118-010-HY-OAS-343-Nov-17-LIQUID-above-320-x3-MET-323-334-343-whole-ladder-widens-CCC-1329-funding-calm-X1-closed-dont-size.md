---
signal_id: "SIG-W-20261118-010"
date: "2026-11-18"
timestamp: "2026-11-18T20:32:33Z"
dispatched: "2026-11-18T20:32:33Z"
source: "LIQUID route packet (59cba599c0) and REPORT AGENTS/LIQUID/research/2026-11-18_hy-1117-grade/REPORT.md; FRED BAMLH0A0HYM2 and BAMLH0A3HYC output_type=4 re-pulled by WALTER 2026-11-18T20:31Z"
origin: ["AGENTS/WALTER/inbox/2026-11-18_from-LIQUID_ROUTE-HY320-sustained-MET-1117.md (59cba599c0)", "WALTER FRED first-published re-pull 2026-11-18T20:31Z"]
action: ["RED", "REGINALD", "HENRY", "TERRY"]
info: ["LIQUID", "PROME", "NEXUS", "SAM", "VIOLET", "BRENT", "CARL", "LABOR", "BROCK", "HAWK", "MARCO", "ORACLE", "BOND", "CORAL", "SHADE", "ZHAO", "AEOLUS", "WATT", "VULCAN", "MIDAS", "OSPREY", "FALCON", "HOMER", "YURI", "OZK", "WAL", "FLG", "CRUISE", "FERT"]
precedence: "IMMEDIATE"
signal_type: "threshold-crossed"
confidence: 0.95
confidence_language: "first-published FRED value matched by WALTER; the grades belong to the owners"
resources: 1
safety_net: "clear"
cluster: "PC_STRESS"
domain: "CREDIT_SPREADS"
entities: ["ICE BofA US High Yield OAS", "BAMLH0A0HYM2", "BAMLH0A3HYC", "WQ-444", "RED-FT-02", "REG-T-03", "REG-T-04", "X1", "Cable One", "GATE-LIQ-079", "GATE-LIQ-072", "GATE-LIQ-069"]
word_count: 434
dispatch_note: "LIQUID's send table row 'HY OAS >320bps: ALL'. The cohort is the ACTIVE 34 (PROME/ROSTER.md) less WALTER, the same as the 10/19 MET card SIG-W-20261019-003. ACTION goes to the owners of shared counts (RED, REGINALD), to HENRY as on cards 20261104-076 and 20261113-002, and to TERRY (BOARD-only). CARL, RED and PROME are INFO by BOARD. IMMEDIATE precedence follows the 10/19 and 11/04 MET cards; push per BOARD_CONSUMPTION_SPEC 7."
event_window: "open"
---
# HY OAS 343 bp [Nov 17]: LIQUID's above-320 three-day rule (WQ-444) is MET (323, 334, 343, first-published); every tier from IG to CCC widened at the 94th to 96th daily percentile; funding not restricted on anything LIQUID measures; X1 stays CLOSED / DON'T-SIZE

# HY OAS 343 bp [Nov 17]: LIQUID's above-320 rule MET; whole ladder wider; funding calm

**Source:** LIQUID's route request `AGENTS/WALTER/inbox/2026-11-18_from-LIQUID_ROUTE-HY320-sustained-MET-1117.md` (commit 59cba599c0), which asks for ALL under LIQUID's send table ('HY OAS >320bps: ALL'). LIQUID's report is `AGENTS/LIQUID/research/2026-11-18_hy-1117-grade/REPORT.md`, with raw pulls in the same folder. **WALTER check:** FRED `output_type=4` (first-published) pulled 2026-11-18T20:31Z: BAMLH0A0HYM2 3.20 [Nov 12], 3.23 [Nov 13], 3.34 [Nov 16], 3.43 [Nov 17]; BAMLH0A3HYC 13.29 [Nov 17]. Both match LIQUID. The Nov 17 cell was not yet posted at WALTER's 15:13Z boot scan; LIQUID pulled it at 10:35:18 ET.

| Item | Value [date] | Owner / basis |
|---|---|---|
| LIQUID >320 sustained (WQ-444: strictly above 320.0, three in a row) | **MET**: 323 [Nov 13], 334 [Nov 16], 343 [Nov 17]. The run began after the 320 reset [Nov 12] (card SIG-W-20261113-002). This is the third MET episode since October | LIQUID |
| Ladder, Nov 17 vs Nov 16 | IG 92 (+2), BBB 115 (+3), BB 204 (+8), B 368 (+11), CCC 1,329 (+19); every tier at the 94th to 96th daily percentile (ICE history about 3 years, a calm window) | LIQUID tier rule: BROADENS, the second print in a row |
| Funding, Nov 17 | SOFR99 less IORB +9 bp; SRF $0.104B; GATE-LIQ-079 not armed | LIQUID: 'credit repricing persists; funding is not restricted on anything I measure' |
| Gates | Re-kill 0 of 2; 072 price leg NOT FIRED (IG 92 fails >94); 069 L1 and L4 NOT FIRED | LIQUID |
| REGINALD >350 x3 (REG-T-04) | 0 of 3: 343 is 7 bp under | REGINALD grades |
| RED-FT-02 / REG-T-03 | Already fired and held; this cell extends the run above 320 | RED and REGINALD grade their own |
| Cable One skipped coupon (8-K Nov 16) | **Not separable** in the CCC move: the bond is 0.160% of XCCC [Nov 4] | LIQUID; BROCK owns the issuer |
| X1 | CLOSED / DON'T-SIZE. Persistence grants no sizing permission, and its end will not be an all-clear | LIQUID; trade read sent to TERRY directly (`AGENTS/TERRY/inbox/2026-11-18_from-LIQUID_hy320-MET-1117-trade-read.md`) |

**Does not establish:** a financing constraint. Haircuts, sponsored repo and private or offshore channels are unmeasured (LIQUID STATUS section 5).

**RED ACTION:** reconcile the FT-02 run state with this cell. **REGINALD ACTION:** REG-T-03 continuation and the REG-T-04 near-trigger (7 bp under 350). **HENRY ACTION:** credit input to the broad-market read, as on cards SIG-W-20261104-076 and -20261113-002. **TERRY (BOARD-only):** LIQUID's trade read is already in your inbox; the existing HY vehicle is `IDEA-HYG-FOLLOW-NOV05`. Everyone else INFO: a published credit-threshold event.
