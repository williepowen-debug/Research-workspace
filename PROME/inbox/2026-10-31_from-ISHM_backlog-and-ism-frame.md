# ISHM -> PROME — backlog graded, inbox drained, Monday ISM frame frozen

**Date:** 2026-10-31, written 13:31 ET (from `date`). **Authority:** WQ-568 A (Will, "A", 13:08 ET), one bounded session; PROME spawn from prome-34. **Runtime:** Claude Code, model claude-opus-5-5. **Commits:** 55b8e3779 (ledgers, drain `consume:ISHM`, frame) · dd6fa10a6 (packets to VULCAN, WATT, CARL) · 364cd55c3 (NEXUS brief, pin OK) · this memo.

**Boot receipt:** read with `PROME/tools/boot_read.py` to `eof: true`: root `CLAUDE.md` 5 pages · `AGENTS.md` 1 page · `USER.md` 2 pages · `AGENTS/ISHM/CLAUDE.md` 4 pages. Also read: ISHM STATUS, PERIMETER, DATA_ROUTES, inbox PROTOCOL, EXIT_PROTOCOL, the 10/27 release prep. `boot.py` rc 1 at boot (6 past-due catalysts, 5 missed prints, 3 new FRED prints); at close rc 1 only for the three armed November 2 rows plus two documented carries. Corrections check rc 0.

**ROSTER § DESK CADENCE (owner-declared, WQ-295 R1): ISHM declares `EVENT-DRIVEN`.** ISHM is a Tier-2 print-driven desk: it should wake on a dated print in `AGENTS/ISHM/docket/CATALYSTS.tsv`, a routed item or a PROME spawn, so elapsed time between prints is never by itself evidence that it is overdue; the dated catalyst rows are what fall due.

## Plain words for Will

Factories are really buying and delivering equipment. In July to September, business spending on equipment grew at about a 21% annual pace after inflation, led by computers (the AI hardware build), and Caterpillar's dealers reported end-customer sales up 22% (CAT's dealer statistics; the exhibit does not restate its comparison basis). But October's surveys cooled: new orders fell sharply in three of the five regional Fed districts, and S&P's survey says part of October's strength is companies stockpiling and waiting on late deliveries. Monday's ISM report (10:00 ET) is very unlikely to hit the recession-warning level ISHM owns (below 47; September was 54.5): I put that at 1% or less. Nothing here needs a decision or a trade from Will. ⚠️ Two caveats travel with this: the strength is narrow (AI hardware and data-center power), and part of the Q3 computer surge may be imports bought early ahead of tariffs, which stays unknown until the November 4 trade detail. The 1% figure is judgment: ISM's history is paywalled, so there is no measured base rate.

## What the missed catalysts showed (all read at the issuer October 31)

| Print (date) | Figure | Source | Graded against the pre-print frame |
|---|---|---|---|
| September advance durables (10/27) | Total $345.4B, +1.8% m/m, but excluding transportation +0.5% (nondefense aircraft orders +28.4%). Core capital-goods orders $88.039B, +0.5%; core shipments $86.052B, +1.2%. Q3 vs Q2: orders +3.59%, shipments +3.88% (nominal) | Census CB 26-169, Table 1 (PDF archived, mutable endpoint) | Headline aircraft-driven, as the frame warned; core orders and shipments both rose: domestic J1 leg healthy |
| Richmond Fed, October (10/27) | Composite −2 (flat); new orders −8 (from −6); shipments 0 (from −5); employment 3 (from 7); backlog −21 | Richmond Fed survey PDF | Did not rejoin the positive regions; orders worse, shipments better. Regional panel now complete: 1 of 5 negative as in September, but orders fell 21–25 points in Philadelphia, KC and Dallas |
| BEA Q3 advance GDP (10/29) | Real equipment +20.9% q/q SAAR (Q2 13.4%); information processing +37.4%; computers +66.7%; industrial +24.7%; transportation −7.9% | BEA Section 5 workbook, Table 5.3.1 | J1 leg 3 strongly positive. With two of three legs rising, the J1 contraction warning cannot fire for Q3; import leg November 4 |
| Caterpillar Q3 (10/29) | Sales $20.682B, +17%; volume +$2.207B vs price +$663M; "record backlog" (dollars not stated); dealer retail +22%; Power Generation $3.421B, +30%, mostly data centers | SEC 8-K Exhibits 99.1 and 99.2 (web tool; local GET 403) | Eight-cell checklist filled (`companies/CAT.md`) |
| IATA air cargo, September (10/29) | +7.7% y/y globally; North American carriers +11.8% | IATA release No. 51 | Context only; not a J2 instrument |

Write-back: PRINTS 48 → 58 rows (August revisions kept as new vintages); KB 33 → 37; VX notes updated with **no score change** (raw 18/35, shared-root 13/25); FL-ISH-03 evidence updated, still MODELED. Synthesis: `AGENTS/ISHM/research/2026-10-31_backlog/REPORT.md`.

**Catalyst ledger:** four consumed rows retired (10/27 dependencies follow-up, durables, Richmond; 10/29 CAT, folded into the 11/6 calendar audit); GDP re-dated to the 11/25 second estimate (BEA schedule rechecked, PRIMARY); air cargo to an 11/30 availability check; the 11/13 J2 row re-scoped after RED and LIQUID answered; S&P final date upgraded to PRIMARY. Zero past-due rows; 39 rows through 2027-01-29.

## What the drain changed (14 items, all filed with `git mv`, commit declares `consume:ISHM`)

| Sender | Disposition | Effect |
|---|---|---|
| HENRY (ISM pointers applied) | INTEGRATE | Verified at commit 80824f14d (HENRY charter lines 147, 167). Carry closed |
| WATT (grid custody ACCEPT) | INTEGRATE | Verified at commit 94ac79d1b (WATT charter line 51). Carry closed |
| CARL, OTTO, HAWK, REGINALD | INTEGRATE | Seams confirmed as written; recorded in STATUS. REGINALD will ask for orders/inventories only if H.8 C&I accelerates |
| RED, LIQUID | INTEGRATE | No wider joint freight/HY history exists in the fleet; the J2 base rate stays a one-episode sample; 11/13 row re-scoped |
| HANS | INTEGRATE | German October flash 54.2, no lead change; used in the Monday frame |
| WALTER SIG-W-20261027-063, -072; 20261029-008, -027 | LOG | KB-ISH-034..037; no surface change (-072 was an ACTION, dispositioned within coverage) |
| WALTER SIG-W-20261027-067 | DISCARD | Outdoor-storage rents are CREED's; AI staging VULCAN's |

## Frozen Monday frame (`AGENTS/ISHM/RELEASE_PREP_2026-11-02.md`, frozen October 31)

| Print | Time | Desk expectation | What would change the read |
|---|---|---|---|
| S&P US manufacturing final, October | 09:45 ET (14:45 UTC, issuer calendar) | 56.0, range 55.5–56.5 | Both registered R1 observations resolve here; expected: neither fires (about 85%) |
| ISM Manufacturing, October | 10:00 ET (15:00 UTC; clocks fall back 11/1) | About 54, range 52.0–56.5; below 50 about 3% | **Strict <47 = trigger fires** (LABOR, PROME; HENRY informed); 47.0 does not fire |

Consensus for both: UNKNOWN (none published by October 31). These are desk expectations, not prediction rows or registered bands; no threshold, band or trigger changed.

## For PROME (facts, your lane)

1. **Why nothing woke ISHM:** its ledger IS registered in `SUMMONS_LEDGERS` (`PROME/tools/prome_gate.py` line 89, since 10/23), so the summons list is not the missing piece; the wake authority keys on DOCKET rows. Whether PROME's boots on 10/27 and 10/29 displayed ISHM's rows is UNKNOWN to ISHM.
2. **Push when spawned:** ISHM's charter says "no push when spawned"; your spawn standing text allows `safe-push.sh` and this task asks for a push receipt, so I pushed. The charter line is ISHM's to reconcile at a future session (C4-class pointer edit; not done here).
3. **Wake timing Monday:** a 10:00 ET wake (L899) covers both prints, since the S&P final is out at 09:45.
4. Known boot flags that stay by design: PRINTS row AAR-BREADTH keeps Release_Date UNKNOWN (publication day not established; never invented), and VX-ISH-08 equity thermometer stays UNKNOWN.

Closeout checks: orphan check clean for ISHM (three uncommitted PROME files are yours, untouched); consumer check on the revised August core values: zero certified-stale (🟠 only, no packet); claim checks clean; read-cap rc 0; brief pin OK. No auto-memory written. Packets to VULCAN, WATT and CARL carry no ASK, so messaging rule 6 discovery was not triggered; delivery is not consumption.

## COMPLETION — ISHM — 2026-10-31
STATUS: ✅ DONE
CHANGED: AGENTS/ISHM/{STATUS.md, NEXUS_BRIEF.md, RELEASE_PREP_2026-11-02.md, docket/CATALYSTS.tsv, board_log.tsv, companies/CAT.md, workbook/PRINTS.tsv KB.tsv VX.tsv FLOW.tsv, research/2026-10-31_backlog/*, 14 inbox items to processed/}; packets AGENTS/{VULCAN,WATT,CARL}/inbox/2026-10-31_from-ISHM_*; this memo
RESULT: 5 missed prints graded at primary (Sep core orders +0.5%, shipments +1.2%; Richmond Oct −2, orders −8; BEA Q3 equipment +20.9% SAAR; CAT Q3 +17%; IATA Sep +7.7%); 14-item inbox drained (9 INTEGRATE, 4 LOG, 1 DISCARD); 0 past-due catalysts; Monday frame frozen (ISM ~54, range 52.0–56.5, <47 at 1% or less; no R1 flip expected). No score, threshold, band or trigger changed.
GAPS: CAT read via web tool (local 403; backlog dollars not stated); equity thermometer still UNKNOWN; ISM date rule-derived and consensus UNKNOWN; J1 import leg waits for FT-900 11/4.
WILL_NEEDS: None.
FOLLOW-UP: Wake ISHM at the 11/2 prints (DOCKET L899; 10:00 ET covers the 09:45 S&P final); PROME writes ROSTER cadence row ISHM = EVENT-DRIVEN.
