# CORAL → PROME · 2026-10-09 22:00 ET · DOCKET L638 Isaias post-landfall wake — DONE; no colour moves, storm rule applied, inbox 26/26

**Session:** coral-1009pm (PROME `prome-1e` Tier-1 spawn, desktop, Opus 5.5 in Claude Code as an Agent-tool spawn; CORAL charter + root CLAUDE/AGENTS/USER read explicitly). Concurrent: AEOLUS `aeolus-db`, REGINALD `reginald-6d`, CATO (Codex) — none of their paths touched. Commits: **`66746cd28`** (CORAL desk + `consume:CORAL`), **`3719e005a`** (CORAL → AEOLUS packet, carve-out ①), this memo. Evidence: `AGENTS/CORAL/STATUS_DETAIL.md` § T1–T8 (+ § T0 = verbatim rotation) · KB ML-CORAL-104…109.

## Headline
Isaias made landfall near Destin (Okaloosa) at 8:30 PM CDT at 105 mph (NHC TCU 100130, read by CORAL; Cat 2 and C1 NOT FIRED are AEOLUS's, KB-AEO-189). **No CORAL colour moves.** Under the pre-registered storm rule (`cc14b3ac3`), **none of the nine graded-metro counties was ever under an NHC warning or watch, and OpenFEMA has no declaration (refresh 10/9 13:10Z)** ⇒ Parcl readings stamped 10/10–10/23 grade as normal and unflagged — **unless a later FEMA major-disaster declaration names a graded county; CORAL checks OpenFEMA at every reading to 10/23.** The bank-transmission rail is untouched.

## L638 scope, item by item
| Item | State | Figure / finding |
|---|---|---|
| Storm rule S1–S4 | ✅ applied as written | S1 #8 stands · S2 no warned county, FEMA leg open · S3 nothing to flag · S4 Panhandle baseline stands; no Parcl pull (none due) |
| Warning set (source + time) | ✅ | NWS KMOB/KTAE/KTBW statements under NHC 13/13A (read 21:38 ET): Hurricane + Surge Warning Escambia · Santa Rosa · Okaloosa · Walton · Bay; Surge Warning Gulf → Dixie; Surge **Watch** coastal Levy only. ⚠️ TBW's "limited surge impacts" line for Citrus → Hillsborough is not a warning |
| Sally/Michael from primaries | ✅ + correction | **Sally $576,943,637 / 71,998 VERIFIED** at the archived OIR page — a **40-day** figure (+92% from its 12-day release). Ivan 2004 added: 210,900 claims / $4.79B. **Correction:** Michael's Bay 95,184 is the Nov-2020 vintage (page heading says Dec-2019; Dec-2019 PDF says 88,303) — § T6, S2 pointer |
| Citizens by county | ✅ PRIMARY 8/31 | HU-Warning 5 = **8,327 PIF / $3.30B TIV**; 11 warning counties 9,578 / $3.63B; −40% since 12/31/25; condo-assoc layer only 55 / ~$140M. Weekly **254,736 at 10/2**. **Binding suspended statewide since 10/7 11:05 ET** (re-read) |
| Citizens/FHCF attachment | ✅ (one leg researcher-read) | Program $2.82B / $276.5M; Citizens retains ~$0.842B before the FHCF layer (**researcher read of the 9/23 chart image — not re-read**); surplus $5.455B; FHCF industry retention $11.93B ⇒ inference: no assessment path |
| Panhandle bank list | ✅ FDIC SOD 6/30/26 | $21.2B deposits in 5 counties; TRMK 8.90% · HWC 7.75% · SFBS 5.45% of their deposits; **CORAL watchlist outside the zone** (CCBG 1.68%, SSB 0.32%, rest 0). SFBS 10/19 / HWC 10/20 print before BKU 10/21 — descriptive only, not rail instruments |
| AEOLUS's five asks | ✅ | One figure agreed by message; **EO 26-211 (10/7, adds Citrus + Levy) caught and accepted by AEOLUS → KB-AEO-190**; reply packet `3719e005a` |
| DBPR W212505-100226 | ✅ | `sources/condo/DBPR_request_W212505-100226_log.md`; draft header now SENT; CALENDAR row → DOCKET L597 |
| Whole-inbox drain | ✅ **26/26** | 17 WALTER + 9 legacy; acted 17 · noted 5 · info-only 3 · deferred 1 (SIG-W-20261008-040 Pembroke Lakes Mall, unverified foreclosure → next normal session) |
| Desk files | ✅ | STATUS · STATUS_DETAIL § T · SCRATCH · NEXUS_BRIEF (`brief_pin_check` OK-SAME-COMMIT) · CALENDAR · KB · board_log · CLAUDE.md 9b (WQ-399 receipt form, C4) |

## For PROME (no Will decision needed tonight)
- **GATE-CORAL-MSI-01:** nothing fired, nothing to register. For the GATES pointer: the storm rule's S2 window is live **10/10 → 10/23** with an OpenFEMA check at each reading; review_by 10/15 unchanged.
- **DAEDALUS Gate-Basis #2 (10/8 packet), proposed, not self-applied** — the MSI-01 letter is Will-ruled (WQ-241). The proposal has two parts:
  - **(a) Wording, a C1 candidate.** Name the five graded pages in the letter: `https://www.parcllabs.com/research/markets/fl/{tampa,punta-gorda,north-port,cape-coral,lakeland}/metro`. No level, operator, instrument or consequence moves.
  - **(b) Cadence, Will's call.** Today a "reading" is any single-stamp pull. Pages regenerate on request (Vercel cache, INFERRED 10/8), so pulling more often makes more readings. A failing reading resets the clock, so the verdict can depend on how often the grader pulls. CORAL's recommendation is one graded reading per calendar week: the first single-stamp pull on or after Monday, with extra pulls logged but not graded. That changes when a clock can reset, so it is a consequence question for Will.
- **Consumer check** (`254,918 → 254,736`): there are 2 🔴 hits, WALTER `research/2026-10-09_morning/desk-status-context.md:15` and DAEDALUS `PRODUCTION_REVIEW_2026-10-01…R5…md:27`. Both are dated records citing the 9/25 weekly correctly for its date. **No packet sent:** 254,736 is a new weekly observation, not a correction of 254,918.
- **Ledger nudge:** `FL_ENROLLMENT.tsv` is behind STATUS. That is not a defect: no new enrollment data exists, and the next print is FLDOE Survey 2, ~Nov–Dec. The ledger stays LIVE.
- **Skipped controls:**
  - Session-start `git pull` not run. Other desks' work was dirty in the tree, and the spawn brief says don't.
  - `memory_index_check` not run. No auto-memory was written.
  - Thesis/CHANGELOG not touched. No thesis-level change.
  - Everything else ran by instrument: read_cap rc0, STATUS at 22,780 B (<70%), brief_pin OK, orphan clean, claim_check clean, corrections rc0.

## COMPLETION — CORAL — 2026-10-09
STATUS: ✅ DONE
CHANGED: AGENTS/CORAL/{STATUS,STATUS_DETAIL,SCRATCH,NEXUS_BRIEF,CALENDAR,CLAUDE}.md, workbook/KB.tsv, board_log.tsv, sources/condo/{DBPR_request_W212505-100226_log,DRAFT_DBPR_request_2026-09-28}.md, archive/CALENDAR_RESOLVED_ROTATED_20261009.md, 26 inbox→processed moves; AGENTS/AEOLUS/inbox/2026-10-09_from-CORAL_isaias-five-asks-answered.md; this memo
RESULT: Isaias landfall near Destin, 105 mph. Storm rule S2 applied: 0 of 9 graded-metro counties under any NHC warning or watch, and no FEMA declaration ⇒ no MSI flag; no colour moves; bank rail untouched. Citizens holds 8,327 policies / $3.30B in the 5 hurricane-warning counties (8/31). Sally $577M / 71,998 verified at 40 days, plus a correction to the Michael Bay vintage. Panhandle deposits sit with TRMK/HWC/SFBS (8.90/7.75/5.45%), not the FL watchlist. Inbox 26/26 drained; KB 104–109.
GAPS: Isaias claims (OIR, Citizens), FEMA declaration and Citizens 9/30 month-end are NOT-YET-PUBLISHED (expected ~mid-Oct to Nov). Citizens' ~$0.84B retention was read from a chart image by a researcher, not re-read by CORAL. Panhandle condo-tower master policies sit outside Citizens and OIR, so there is no instrument for them.
WILL_NEEDS: None tonight. The Gate-Basis #2 cadence choice for MSI-01 goes to Will when PROME chooses to present it.
FOLLOW-UP: OpenFEMA check at each Parcl reading to 10/23 (next by 10/15) · Citizens 9/30 (~mid-Oct) · 10/16 FL Realtors · 10/21 BKU · Pembroke Lakes Mall verification.
