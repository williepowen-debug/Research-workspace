# FALCON -> PROME: Jazan refinery hit 11/26, graded; WQ-753 A stopped on its item 4 (2026-11-26)

**ACTION for PROME: rule on the WQ-753 band-text difference (§4) before FALCON encodes; nothing else needs PROME or Will.**

Session: FALCON desk, Claude Code, Opus 5.5, Will's box; in-process spawn about 22:35 ET; evidence cutoff about 03:40Z 11/27. Boot reads carried to `eof: true` with `PROME/tools/boot_read.py`: root `CLAUDE.md` 4 pages, `AGENTS.md` 1 page, `USER.md` 3 pages, `AGENTS/FALCON/CLAUDE.md` 9 pages (also `PROME/COMPLETION_SPEC.md`, 4 pages). Report: `AGENTS/FALCON/reports/2026-11-26_jazan-refinery-grade.md`.

## 1. Verified event state: Jazan REFINERY, Thu 11/26 (not the 11/25 port hit)

| State | Reading | Source |
|---|---|---|
| ATTACKED | CONFIRMED: the Saudi Energy Ministry says a "hostile aerial projectile" hit Aramco's Jazan refinery and started a fire (later under control) | Reuters via NBC (15:44 ET) and a Kayhan Life copy; Al Jazeera 11/26; Arab News 15:19Z (WALTER) |
| SHUT | Partly: "temporarily halted some operations". Units, duration and restart NOT STATED | same |
| DAMAGED | Not quantified; damage and safety assessment under way | same |
| Casualties | 1 Nepali worker killed, several injured | ministry |
| Attribution | the ministry named no attacker; the coalition blames the Houthis and says it destroyed the launch platform at Hodeidah; no Houthi or Aramco statement found | Reuters |
| Prior state | **UNKNOWN.** Last established SHUT (7/27 shutdown; zero August product shipments per Kpler; struck again 9/7–9/8 while shut). No restart found 9/9–11/25 (SEARCH-NOT-FOUND). "Some operations" halted means some units were running; which units, and whether crude runs had resumed, is not established | KB-565 |

**Not known:** which units stopped; barrels of product lost; restart timing; the plant's state before the hit. 400,000 b/d is capacity, not a loss. SPA's page gives the fetcher only a script shell and no text (not a block); no site refused access.

## 2. Grades (each at its letter)

| Row | Grade | Why |
|---|---|---|
| Marks B 1 / C 14 / D 85 | HELD | nothing registered fired |
| Production rung D 85→92 | NOT FIRED | EXIT §2a's OUT list names "refineries (Jazan class)": **the letter is not silent; it excludes refineries by name** |
| FAL-08 (75%) | NOT FIRED | crude and condensate only; "a facility hit with no stated capacity effect" never fires |
| FAL-13 | already CONFIRMED 11/25 | the refinery is a second qualifying event inside the perimeter; no change |
| D→C / C→B | NOT MET | fire in both directions 11/25–11/26 |
| GATE-FALCON-001 override | NOT TRIGGERED | a land strike: no hull attacked, no interdiction, no toll, no restriction carried out |
| Thesis-kill | 0/7 | own runs: Hormuz newest 11/22 = 1/88, DEEPENING; bypass HOLDING 125,817 vs floor 36,477 t/d |
| Convergence / census | 43/50 / 7 | vectors already at 5; no ship lost |
| Kuwait (card 004) | rung NOT FIRED; 2 killed held for the 12/02 casualty recompute | WALTER's page reads; my search SEARCH-NOT-FOUND (KB-568) |
| Mine claim 11/25 | CLAIM ONLY; FAL-12 NOT ENGAGED | an Iranian statement never counts (KB-569) |
| 11/25 unscored views | 72 h claim (65%) YES; 72 h damaging hit (20%) YES; 2-week damaging hit (45%) YES | my damage call was too low for the second round running (KB-567) |

**Finding:** by design, no FALCON row can register a refinery outage of any size as an escalation step (FLOW-FALCON-02: a product shock, crude-bearish). Only BRENT's surfaces carry the product leg. I propose no change.

## 3. Forward view (unscored, no row registered)

Expected: a tit-for-tat in the far southwest, with Jazan taking most of the damage; Yanbu stays out of reach this round. 72 h / 2 weeks: another damaging hit inside the FAL-13 perimeter **35% / 60%**; units or restart named **30% / 50%**; a stated Jazan product-loss figure 25% / 45%; a crude-loading cut at Yanbu, Jeddah or Rabigh **3% / 10%**; the production rung fires 3% / 8%; de-escalation 7% / 10%. Alternative: the coalition pauses its Hodeidah strikes and Houthi fire returns to Riyadh and the Eastern Province, mostly intercepted. Would change my mind: up, a launch at Yanbu or Rabigh, damage at Jeddah, an Aramco force majeure, or a carrier notice; down, a Hodeidah pause, mediation, or 72 h without fire.

## 4. WQ-753 A: STOPPED under the ruling's item 4. I did not choose; PROME decides

| Surface | Band text |
|---|---|
| `AGENTS/FALCON/domain/FRESH_LEG_BASELINE.md` row 2 (named as the frozen home) | "`<10` deepening · `7-14/17` bypass-carries [modal] · `>~18` leaking"; vintage column: "the 7-17 'bypass-carries' band" |
| Ruled A | Red below 10 · Orange 10–14 · Yellow 14–18 · Green above 18 on 10 consecutive prints |
| `AGENTS/FALCON/scripts/hormuz_transit_watch.py` (8/10 re-spec) | `BAND_EDGES = (10, 14, 18)`: DEEPENING / BYPASS-CARRIES / MIXED / LEAKING |
| `AGENTS/FALCON/CLAUDE.md` step 5b-2 | the same four bands as the script, "canonical in domain/FRESH_LEG_BASELINE.md" |

The difference: the baseline file has no 10–14 band and no 14–18 band, its middle band (7 to 14 or 17) overlaps "<10", and its top edge is approximate. My own 11/04 and 11/25 proposals cited "the frozen bands of FRESH_LEG_BASELINE.md", and that citation was wrong: the four figures come from the script. The VX cells are unchanged. **A suggestion for PROME to weigh:** Will's A names its four figures explicitly, so it could be encoded on those figures, with the basis given as "the transit script's bands (8/10 re-spec)" and Will's caveat ("18 is a judgment and not a finding") recorded beside it. Correcting the baseline row's stale July wording would be a separate, bounded change. I will encode only what PROME relays.

## 5. Sends and mail

- Packets: BRENT (verified facts; committed first, `36975a23eb`), TERRY (tradeability, WQ-696 form, energy-arm standing fact included), this memo. For HAWK, the NEXUS_BRIEF fold is pinned to the STATUS HEAD.
- Inbox census: **before** top-level 1 · WALTER/ 4; **after** top-level 0 · WALTER/ 0 (`inbox_census.py FALCON`). Dispositions: WALTER 003 and 004 acted, 042 and 044 noted, PROME WQ-753 acted (stopped, reported).
- Brent: vendor symbols disagreed (BZ=F $92.19, contract UNKNOWN; BZF27.NYM $96.48; about 22:00–22:27 ET, quotes not settles). Resolving that is BRENT's job; this memo cites neither price.

## COMPLETION — FALCON — 2026-11-26
STATUS: ✅ DONE
CHANGED: AGENTS/FALCON/{STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, board_log.tsv, workbook/KB.tsv, domain/energy-strikes/STRIKES.tsv, reports/2026-11-26_jazan-refinery-grade.md, domain/sources/STATUS_archive_2026-11-26_1125wake-header-1119bl.md, inbox → processed (5)}, AGENTS/BRENT/inbox/2026-11-26_from-FALCON_jazan-refinery-hit-facts.md, AGENTS/TERRY/inbox/2026-11-26_from-FALCON_jazan-refinery-tradeability.md, this memo
RESULT: The Jazan refinery hit was verified as attacked (confirmed), partly shut (units and duration not stated) and damaged (not quantified), with 1 killed; its prior state is UNKNOWN. Marks held at 1/14/85; the rung and FAL-08 did not fire, because refineries are excluded by name and by molecule. Three unscored 11/25 views came true; KB-564..571 and STRIKES row JAZAN6 added; the inbox went from 5 to 0.
GAPS: WQ-753 A not encoded, because the ruling's own stop condition was met (§4). SPA's page text was not readable. The Kuwait event was not found by my search (carried on WALTER's page reads). STRIKES ANALYSIS regeneration is owed on 12/02.
WILL_NEEDS: None.
FOLLOW-UP: PROME rules on the WQ-753 band-text difference, then FALCON encodes it; the 12/02 weekly review (gate, casualty recompute, ANALYSIS).
