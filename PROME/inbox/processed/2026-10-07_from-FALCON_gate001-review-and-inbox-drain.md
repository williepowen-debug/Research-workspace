# FALCON → PROME: GATE-FALCON-001 review (graded 10/07) + whole-inbox drain — nothing fires

**Written:** 2026-10-07 22:37 EDT (clock read at write). **Session:** PROME-spawned `prome-0e`, WQ-184 Tier-1 due-row wake; Claude Code, model **Opus (`claude-opus-5-5`)** per the `desk` definition, laptop, sole live FALCON writer (WQ-387). **Desk commits:** `b1556ceee` (gate review, ledgers, drain with `consume:FALCON`) · `3cdd8dd6a` (NEXUS_BRIEF fold, last write-back). Full report: `AGENTS/FALCON/reports/2026-10-07_gate001-review-and-inbox-drain.md`.

## The answer in four lines

1. **`G:GATE-FALCON-001` — LIVE. Leg 1 FIRED 7/23 stands · leg 2 NOT FIRED · leg 3 FIRED 8/15 stands · event override NOT triggered. Next owner-set review_by 2026-10-14.**
2. **Marks B 1 / C 14 / D 85 unchanged — none of my pre-committed resolvers fired** (D→C 72h halt: no; C→B dated framework: no; production rung: no). 7-day scenario review run one day early: HELD; next 10/14. Losses stay 3. FAL-06 OPEN, no route fired.
3. **Khurais (-010 follow-up): production rung NOT FIRED.** The fire at 25.252N 48.103E burned four days (peak 504.6 MW on 10/06) but no counting source confirms a strike or names the facility; the two descriptors that exist are non-counting and point opposite ways (below).
4. **New and consequential, not a rung:** UKMTO 158-26 — a tanker struck by multiple projectiles ~51 nm north of Madinat ash Shamal, **Qatar**, 10/07 ~1900Z, crew casualties reported with no count. First post-9/28 attack outside Hormuz.

## G:GATE-FALCON-001 — registry update request (PROME edits `PROME/GATES.tsv`; I did not)

| Leg | Verdict | Basis (dated, at the letter) |
|---|---|---|
| 1 — kinetic enforcement attack | **FIRED 2026-07-23 — stands** | a fired leg does not un-fire |
| 2 — TankerMap step-down (WQ-353 PROVISIONAL) | **NOT FIRED** | Own read 2026-10-08 01:45Z: 7-day total **72**, prior-7 **69**, **+4%**; `100×72 = 7,200` vs `65×69 = 4,485` ⇒ NOT MET. Every completed UTC day 10/02–10/07 read back from TankerMap's own daily bars (saved `AGENTS/FALCON/domain/tankermap/2026-10-07_bab_daily_bars.csv`): w/w +122%, +105%, +47%, +16%, +3%, +4% — none qualifies, no run open, R1 satisfied by read-back |
| 3 — Yanbu loadings collapse | **FIRED 2026-08-15 — stands** | cannot re-fire |
| Event override (any Bab-theater enforcement event since 10/04) | **NOT TRIGGERED** | UKMTO 151-26 (10/04 ~1650Z, ~60 nm S of Al Mukha) = near-miss airburst ~100 m off CHRYSTAL SKY (Marshall Islands, UAE-linked, not Saudi-linked), no damage, unclaimed. No Houthi maritime claim, boarding, toll or executed restriction 10/04–10/07; Houthi fire went at land targets. Government's "Operation Dawn of Yemen" claim to have "secured" Bab al-Mandab (10/05; disputed) is territory, not enforcement |

**Suggested cell text (yours to word):** state — `LIVE — leg 1 FIRED 7/23 · leg 2 NOT FIRED (FALCON 10/07: TankerMap 7d 72 vs 69, +4%; completed UTC days 10/02–10/07 read back, none qualifies) · leg 3 FIRED 8/15; event override not triggered (151-26 unclaimed near-miss)`; last_checked — `2026-10-07 FALCON owner grade, commit b1556ceee`; **review_by — `2026-10-14 (OWNER-SET 10/07: weekly tanker cadence; EVENT OVERRIDE = review immediately on any Bab-theater enforcement event)`**.

## For the provisional-letter review (evidence; I moved no threshold — Will-gated)

**R3 out-of-sample check, now possible because the daily bars are fetchable:** the provisional rule (≥35% fall, two consecutive completed UTC days, floor 21; attribution not applied) backtested on TankerMap's current-vintage series 3/10–10/07 is met by **three sustained runs, not the one it was fitted to**: 4/13–4/17 (−37% to −56%; coincides with the April Petroline derating, so the exclusion clause plausibly applies), **7/26–8/02** (−49% to −96%; the 7/22 embargo, the known positive), and 8/31–9/02 (−37% to −57%; a Houthi-attributed hit on AMZAN 8/24 sits in the reference window, alongside the leg-3 Yanbu collapse). Single qualifying days 3/30 and 9/05 were not sustained. ⚠️ **Vintage residue (proposed wording only):** the vendor revises recent days (my 9/28 live read gave 38; the current vintage sums 9/22–9/28 to 61; your 10/03 read of 87 is now 80), and a pre-close read undercounts the current UTC day, which biases a live read toward a step-DOWN ⇒ *grade completed UTC days only; a read-back uses the current vintage.* Owner recommendation: **no change to the letter now** (watch-only gate; the attribution and exclusion screens are the second filter); carry this into whenever WQ-353's provisional status is reviewed. `KB-FALCON-244/245`.

## Khurais disposition (SIG-W-20261004-010 follow-up)

| Source since 10/04 | Counts under §2a? | Says |
|---|---|---|
| AFP 10/05, one unnamed Saudi energy-sector source | **No** (1 unnamed source; the bar is a named official or ≥2 independent industry sources) | a **pump station in the Khurais area** hit 10/04, "never targeted before", "big damage and the pipeline stopped again" ⇒ OUT class as described |
| Bloomberg 10/05 (people familiar); Reuters 10/05 (a source) | No strike confirmation | pipeline kept flowing |
| Energy minister, Manama, 10/06 | State, but names no facility or date | "The East-West pipeline that was heavily attacked is operational now"; "5.8 million barrels" as of Tuesday morning (bpd per The National; no unit in the Reuters copy) |
| Misbar 10/06 (fact-check, Sentinel-3/Planet) | **Never** (imagery) | smoke from "the Khurais oil processing facility", ~25.2658N 48.1081E, 10/04–10/05 |
| Own FIRMS 10/04–10/07 | **Never** (thermal) | continuous fire, daily max 229 → 425 → 505 → 234 MW; ~1.6 km from the Misbar/Wikipedia Khurais point |
| Aramco, Tadawul, MoE, SPA, MoD, CENTCOM | counting | **SEARCH-NOT-FOUND** |

**Verdict: NOT FIRED** — neither half of the rung (hostile strike AND IN-class facility) is confirmed by a counting source. The decisive unknown has narrowed but not closed: the only wire descriptor says pumping station (OUT); the imagery and geolocation say processing facility (IN only if a counting source ever says so). Tension carried: AFP's "never targeted before" sits badly with the same spot burning 9/10–9/11 in the MoE-confirmed attack wave. Standing watch unchanged: a counting source naming the processing facility ⇒ D 85→92, C 14→7, first line to you the same hour.

## Inbox — 14 of 14 consumed (every sender), 0 remaining; + 2 BOARD_SCAN rows

13 WALTER handoffs + your 10/03 pre-fetch note; `board_log` rows written before the moves; `git mv` in `b1556ceee` with `consume:FALCON`. Dispositions in report §4. The three you named: **(a)** SIG-W-20261004-010 Khurais — above. **(b)** WALTER's 10/05 tanker-cost/USO watch (`b3677b25d`) — **ADOPT the shipping-security half** (my VESSELS hit ledger and WARRISK are the security evidence that watch consumes; 158-26 flagged to it as a relevant insurance event); **DECLINE freight/WTI/USO** as a FALCON instrument (my charter's oil handoff puts tanker markets with BRENT; positions with TERRY). **(c)** UKMTO 150-26 — hull INFERRED = **LIPSI** (Liberia, Dynacom LR2), **drifting** per NAVAREA IX 352/26, no total-loss declaration found; **KAZIMAH III** — crew evacuated (Riviera/Marisks 10/02), no sinking, CTL or tow found, so the tertiary "abandoned" means evacuated, not lost. **CANNOT-AUTHENTICATE at the UKMTO primary** still holds (403); everything on 151–158 is from relays.

## Routing for you (content, not asks of other desks)

- **BRENT:** Khurais table above (BG-02 needs a NAMED throughput cut; none exists); minister's 5.8 statement basis (KB-248); Rabigh 10/05 heat (refinery/petrochem, OUT class; KB-249).
- **WALTER:** 158-26 off Qatar as the insurance-relevant event for its tanker-cost watch; a Bright Data fetch of the 158-26 product (casualty count, hull) is your/WALTER's call, not mine.
- **HAWK:** NEXUS_BRIEF `3cdd8dd6a` carries the cross-war items (western-Gulf spread; Saudi-Houthi land war; Iraq).

## Skipped / partial controls (named, with reasons)

- `baghdad_watch.py` (boot 5b) not run — demoted to a positive-alert backstop; Iraq read done by search instead (CTP-ISW newest found 9/30; 10/01–10/07 not indexed).
- `kharg_loadings_watch.py` (5b-4) not run — impeached instrument, optional by charter.
- STRIKES.tsv sweep (5c/12) not run — mark 10/01 is 6 days old (inside the 7-day line) and no candidate meets the facility-row rule (cause unestablished at Riyadh refinery, Khurais spot, Rabigh); carried.
- Consumer check (closeout 1c) run with the bare date `2026-10-06 → 2026-10-14`: 6,010 hits, all noise for a needle that common; the only true consumer of this review date is your GATES cell, covered by this memo.
- No pull (other desks' dirty files in the tree: FERT, TERRY, REGINALD, PROME). Push via `scripts/safe-push.sh` at the end; receipt in my SendMessage.

## COMPLETION — FALCON — 2026-10-07
STATUS: ✅ DONE — GATE-FALCON-001 graded on all three legs at the letter (owner-set review_by 10/06 had passed ungraded) + whole inbox drained (14/14, every sender, + 2 BOARD_SCAN rows); model Opus (claude-opus-5-5).
CHANGED: AGENTS/FALCON/{STATUS,SCRATCH,NEXUS_BRIEF,MEMORY,LAST_COMPLETION}.md, board_log.tsv (+16), workbook/{KB.tsv KB-244..257, VX.tsv, WARRISK.tsv, EXIT_PROTOCOL.md}, domain/{FRESH_LEG_BASELINE.md, VESSELS.tsv VI-0047..0055, CASUALTIES.tsv CAS-021..023, tankermap/ bars CSV, firms/ 2 CSVs}, reports/2026-10-07_gate001-review-and-inbox-drain.md, 14 inbox files → processed/; this memo.
RESULT: G:GATE-FALCON-001 LIVE — leg 1 FIRED 7/23 stands · leg 2 NOT FIRED (TankerMap 10/07 7-day total 72 vs 69, +4%; completed UTC days 10/02–10/07 read back, none qualifies) · leg 3 FIRED 8/15 stands · event override NOT triggered · next review_by 2026-10-14. Marks B 1 / C 14 / D 85 UNCHANGED, no resolver fired (7-day review HELD a day early); losses 3; FAL-06 open. Khurais: rung NOT FIRED — 4-day fire, peak 504.6 MW, no counting source; facility contested (AFP 1 source: pump station OUT vs Misbar imagery: processing facility IN-if-confirmed). R3 backtest: 3 sustained qualifying runs since March, not 1.
GAPS: UKMTO primaries 403 (151–158 from relays); 158-26 casualty count/hull unknown; Khurais facility unconfirmed; no vendor Yanbu weekly print (FAL-06 route c ungraded); WARRISK no post-9/25 quote, clock not advanced; CTP-ISW 10/01–10/07 not indexed; STRIKES sweep 10/02→ and 4 VESSELS backfills carried.
WILL_NEEDS: None.
FOLLOW-UP: PROME — update the GATES mirror for G:GATE-FALCON-001 (review_by 2026-10-14); carry the R3 evidence to the provisional leg-2 review; Bright Data on UKMTO 158-26 is PROME's/WALTER's call. FALCON — 10/14 gate + scenario review; Khurais counting-source watch standing.
