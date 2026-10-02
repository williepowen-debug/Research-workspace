---
signal_id: SIG-W-20261002-031
date: 2026-10-02
timestamp: 2026-10-02T21:04:28Z
time_dispatched: 2026-10-02T21:04:28Z
timestamp_note: stamped from the system clock at write, not typed
source: Will-Telegram image + verify-research (WALTER subagent) + ERCOT primary
origin: ["Will-Telegram msg 4879 (2026-10-02 20:59Z): infographic '50 Largest Data Center Projects Delayed, Total value $396 billion+', no author/outlet/date; batch BM-20261002-07 item 1", "verify-research subagent (Opus), 2026-10-02, completed before dispatch: ~30 searches, verdict CORRECTED-FRAMING", "ERCOT 'Batch Zero Update' board deck, 2026-09-11 (ercot.com/files/docs/2026/09/11/14-Batch-Zero-Update.pdf), read by WALTER before dispatch", "Utility Dive 2026-08-21 (Robert Walton), Seely quote, read by WALTER before dispatch"]
domain: POWER_GRID
cluster: AI_INFRA_CAPEX
entities: ["ERCOT", "Batch-Zero", "PUCT", "Stargate-Abilene", "Oracle-Jupiter", "Crusoe", "OpenAI", "Microsoft", "Meta-Hyperion"]
confidence: 0.8
confidence_language: "reports"
signal_type: context
safety_net: clear
verify_research_verdict: CORRECTED-FRAMING
verdict: "An unsourced viral table ('50 largest data center projects delayed, $396B+, ~23.7 GW') fails verification: no originator found, costs inflated 5-7x on checked rows (Abilene $100B vs ~$32B at completion per Epoch), Microsoft Mount Pleasant/Licking County and Apple Waukee are 2022-25 pauses (Mount Pleasant phase 1 went live 2026-06-23), Meta Hyperion was EXPANDED to 5 GW, no Amazon project found in Waterloo IA. Three rows survive as current 2026 facts: (1) ERCOT Batch Zero: the large-load study will miss its April 9, 2027 date (ERCOT's Chad Seely, Utility Dive 2026-08-21); ERCOT files its Eligibility Verification and Community Impact reports with the PUCT by December 10, 2026, and has paused energization of new large-load data centers until then (ERCOT board deck 2026-09-11); (2) Oracle's 9/24 force majeure notice on Jupiter (already held: SIG-W-20260925-007); (3) Stargate Abilene buildings 5-8 estimated operating ~2026-11-01 vs mid-2026 (Epoch AI tracker, 2026-07-28; tracker estimate, not a company statement)."
precedence: ROUTINE
action: ["WATT", "VULCAN"]
info: ["HENRY", "RED"]
dispatch_note: "Will image BM-20261002-07 item 1. The table itself is KILLED (kill_log, Credibility); this signal carries only the verified residue so the owners do not have to re-verify a recirculating graphic. POWER_GRID -> WATT action (ERCOT dates); AI_CAPEX residue -> VULCAN action (Abilene slip; nothing here moves its capex-cut alert). RED info by CORRECTED-FRAMING rule (pull-complete). HENRY info per AI_CAPEX/POWER_GRID rows."
---
# A viral "50 delayed data centers, $396B" table is unsourced and mostly wrong. Three facts in it hold up; one gives WATT and VULCAN dates they don't have.

**Short version:** Will sent a table listing 50 "delayed" US data-center projects worth "$396B+". **Nobody can be found who made it, and most rows that were checked are wrong** on size, date or status. Some "delays" are 2022–2025 stories; one is actually an expansion. **Do not cite the table or its totals.** What survives: **ERCOT's big Texas data-center interconnection study will miss its April 2027 date, two reports are due December 10, and new large data centers stay unpowered until then.** That ERCOT timeline is not on WATT's or VULCAN's calendars.

## What survives (dated, sourced)
| Fact | Source (date) | Read by |
|---|---|---|
| ERCOT: "We will not have the study done by April 9, 2027" (Batch Zero; new timeline not set; the Texas legislative session "could delay things further", per Jefferies) | Utility Dive, 2026-08-21, Chad Seely (ERCOT SVP regulatory policy) | WALTER |
| ERCOT files the **Batch Zero Eligibility Verification Report** and the **Community Impact Review Report** with the PUCT **by December 10, 2026**; **energization of new large-load data centers and crypto miners is paused** until the verification, audit and community review are done; 204 projects (66.4 GW) met the conditional qualification | ERCOT Batch Zero Update, board deck 2026-09-11 (cause: Gov. Abbott's 8/3/2026 directive) | WALTER |
| Oracle force majeure notice on Jupiter (NM), 9/24 — campus 2.45 GW, opening 2028, gas pipeline slipped to Feb 2027 | Bloomberg via heise 9/30, Insurance Journal 9/25 | subagent; **already held** (`SIG-W-20260925-007`; VULCAN grades it a rent deferral, S1 ARMED not FIRED) |
| Stargate Abilene: buildings 3–4 were due March 2026 and not online in June; buildings 5–8 estimated operating ~2026-11-01 vs "mid-2026" | Epoch AI data-center tracker, updated 2026-07-28 | subagent |
| Abilene: a planned 600 MW expansion scrapped; Crusoe cancelled a $1.25B Boom turbine order | Bloomberg via Tom's Hardware/DCD (date not established); TechCrunch 2026-09-25 | subagent; turbine item **already held** (`SIG-W-20260928-013`) |

## What fails (do not cite)
- **Headline "$396B+, 23.7 GW, 300+ projects":** no originator found. The tier-1 tallies are far smaller: Data Center Watch ~$130B blocked or delayed in Q1 2026, ~$68B in Q2 (NBC/Fortune Jun–Jul; Breitbart 9/21).
- **Abilene "$100B":** that is the Stargate headline pledge; Epoch puts the campus at ~$32B at completion.
- **Microsoft Mount Pleasant "paused indefinitely":** the partial pause was Jan/Apr **2025**; phase 1 went live **2026-06-23**.
- **Microsoft Licking County, OH:** an April **2025** pause of ~$1B, not $7B.
- **Apple Waukee "5 years to 2027":** a ~2022–23 story; a ~$1.3B project, not $7B, and not an AI build.
- **Meta "Franklin LA, $10B":** this is Hyperion, **expanded** 7/13/2026 to 5 GW and >$50B.
- **Amazon "Waterloo IA":** no Amazon project found; Waterloo's moratorium (9/8) concerns a Wahawk Power LLC project.
- **ERCOT "Batch Zero" as one $56B row:** the $56B has no source, and it likely double-counts Texas rows already in the table.

**So what:** The table reads like proof the AI build-out is stalling. On inspection it is mostly old pauses and wrong sizes, and **nothing in it adds to the hyperscaler capex-cut question.** The real, current constraint it points at is **Texas grid access**: new large data centers can't be energized until ERCOT finishes an audit that reports on December 10, and the main interconnection study has slipped past April 2027 with no new date.

## Caveats
- The row checks were done by a WALTER verify subagent. WALTER itself re-read only the two ERCOT sources. Google Fulton and Amazon Richland were not checked.
- **Abilene's slip rests on Epoch's satellite-and-filings tracker, not an OpenAI/Oracle/Crusoe statement.**
- ERCOT's own deck (9/11) says the timeline impact is "still being determined"; the "will not finish by April 9, 2027" line is Seely's spoken statement as reported by Utility Dive (8/21).
- Two DCD pages returned 403 (Jupiter, Apple Waukee); those rows rest on other outlets.

## Exposure
Will's options/positions are not checked against this; TERRY's card. No ERCOT-specific instrument known in the FORGE mirror (10/01 capture).

## Requested action
**WATT:** put ERCOT's **December 10, 2026** report filings on your calendar, plus the open-ended Batch Zero study date (originally April 9, 2027). Say whether the energization pause changes any registered grid or power-price item. **VULCAN:** log the Abilene build-out slip (Epoch estimate, buildings 5–8 ~11/01) and the scrapped 600 MW expansion against your capex/build pillar. Nothing here changes Jupiter's grade. HENRY, RED: information.
