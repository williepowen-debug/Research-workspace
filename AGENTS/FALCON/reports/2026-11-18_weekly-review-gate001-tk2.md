# FALCON weekly + GATE-FALCON-001 review, 2026-11-18 (D:L1112, G:GATE-FALCON-001)

Written about 10:50 ET by FALCON (Claude Code, Opus 5.5, desktop), PROME prome-6e weekly wake. Evidence cutoff about 15:30Z 11/18. Live-event grade delivered first and separately: [live grade](2026-11-18_live-kuwait-bahrain-grade.md) (commit da20e402b4).

## Runtime and boot

Claude Code, model claude-opus-5-5, desktop. Read: root CLAUDE.md, AGENTS.md, USER.md, desk CLAUDE.md, STATUS, SCRATCH, MEMORY (CARRIED OPEN), EXIT_PROTOCOL v4, FAL-08..12 letters. No AGENTS.md in the desk dir (none exists). Missing tool: WebFetch (used the web-fetch subagent instead). Unreachable here: Washington Post, CNN, Seatrade (403/451), ukmto.org, centcom.mil. **SKIPPED:** `git pull` (PROME holds pull and push until its closeout ask); LESSONS.md not re-read whole (read-cap budget, no new prediction written); kharg script (optional, not load-bearing); baghdad_watch (demoted backstop; PMF read done by search instead).

## Instruments

| Instrument | Reading |
|---|---|
| PortWatch Hormuz transits | newest 11/15 = **2/88**, tankers 0, DEEPENING, no band change |
| Bypass (Fujairah + Sohar) | trail-14d 137,307 t/d vs run-time floor 35,372, **HOLDING**, newest 11/13 |
| WARRISK rows | all 5 EXPIRED (registered falsifier +43d); WQ-298 rule CANNOT-FIRE; not re-pulled |
| Ledger staleness | rc 0 (FLOW, WARRISK declared quiet) |
| Corrections | COR-20261117-28 receipted NO-OP (WALTER 028 restates my own 11/17 grade) |
| Strike ledger | was 6 days behind; swept 11/13–11/17, **zero new facility rows**, mark advanced to 11/17 |

## Scenario review (EXIT v4 §5, on date)

**B 1 / C 14 / D 85 HELD.** Production rung NOT FIRED: no state- or operator-confirmed hit on a Gulf-ally production-class facility 11/11–11/18; Houthi claims of hits on pumping stations 8 and 9 on 11/17 are claim only and out of class anyway (KB-513). D→C NOT MET: the US struck Qeshm 11/17, Iran fired at Kuwait and Bahrain 11/18, and ships were hit in Hormuz 11/16–11/17. C→B NOT MET: Qatar met Iranian officials 11/17, no text and no reopening. Thesis-kill **0/7**. Convergence **43/50**. FAL-08..12 OPEN, none due; FAL-09 **1 of 5**. Census **7**. Next weekly **2026-11-25** (KB-515).

## GATE-FALCON-001

Own TankerMap read 2026-11-18T15:22Z (`domain/tankermap/2026-11-18_bab_daily_bars.csv`), completed UTC days only, vendor's current vintage:

| Day | Daily | 7-day | Prior 7 | Ratio | ≤65%? |
|---|---:|---:|---:|---:|---|
| 11/11 | 7 | 66 | 91 | 72.5% | no |
| 11/12 | 10 | 68 | 89 | 76.4% | no |
| 11/13 | 12 | 71 | 88 | 80.7% | no |
| 11/14 | 13 | 73 | 87 | 83.9% | no |
| 11/15 | 10 | 74 | 79 | 93.7% | no |
| 11/16 | 14 | 80 | 75 | 106.7% | no |
| 11/17 | 12 | 78 | 75 | 104.0% | no |

- **Leg 2 NOT MET.** Lowest in the week 72.5% (11/11). Read-back: 11/01–11/15 unchanged; 11/16 revised up from 10 to 14 (it was partial at the 11/16 read). Both saved.
- **Event override NOT TRIGGERED:** no Houthi enforcement act on a hull in the zone found 11/12–11/18 (search level). Coalition strikes on Houthi Yemen 11/17 and Riyadh intercepts are not enforcement on a hull.
- Legs 1 (7/23) and 3 (8/15) stay FIRED. **Gate LIVE. Next review_by 2026-11-25** (owner-set; event override unchanged).
- ⚠️ The vendor's methodology label now reads the generic `route-versioned-v2` block (11/16: `bab-el-mandeb-transit-v5`); completed-day read-back is unchanged, so no series break is evident (KB-512).

## Thesis-kill #2: instrument draft (D:L1112 main item)

Draft only, NOT encoded: [proposal](../proposals/2026-11-18_thesis-kill-2-instrument-draft.md). It names IMF PortWatch chokepoint6 `n_total` and requires 45 or more on each of 10 consecutive calendar days. Three choices are Will's: every day vs average, all vessels vs tankers, whether a missing print breaks the run. Today the limb is far from met: 3 days at 45 or more in 261 war days, longest run 2 (KB-516).

## Iraq/PMF re-read (D indicator #4)

Iraq's PM ordered the army into Jurf al-Nasr and set Kataib Hezbollah a withdrawal deadline, reported as 8 pm Fri **11/20**, over alleged oil smuggling. KH refuses; Quds Force commander Qaani is in Iraq. This is Iraq against KH, not KH against US forces: **discriminator not fired**. Watch 11/20 (KB-514).

## Combination themes

Nine due themes were reviewed against this session's evidence only, with no dedicated sweep. New members: western-sector-reach (Houthi pumping-station claims, Riyadh intercepts), us-strike-preparations (US strike 11/17), gulf-side-channels (Qatar–Iran meeting 11/17), gulf-host-state-fire (Kuwait and Bahrain 11/18). No new member found for deep-Gulf hulls, mine claims, selective passage, Eastern Province reach, land-route squeeze or Bab shore control. Next review 11/25.

## Inbox drain

| Item | Disposition |
|---|---|
| WALTER SIG-W-20261118-001 | acted (live grade); file is on origin only, git mv after the pull |
| WALTER SIG-W-20261117-028 | noted; correction receipted NO-OP; moved to processed |
| PROME WQ-701 A2 charter trim | **DEFERRED, not done today.** Exact words: "FALCON will not trim AGENTS/FALCON/CLAUDE.md in this session. PROME's 11/18 task letter puts the charter read-cap overrun in a separate later session; FALCON accepts the WQ-701 A2 ruling as Will's word and owes the trim at that session." Left in inbox |
| PROME stale-KB rows | DONE by my own definition (Stale_By before 11/18, Status ACTIVE/LIVE/blank): **292 rows**. **244 retired** (Status → STALE, nothing else changed). **48 held ACTIVE** because STATUS, EXIT_PROTOCOL, an open FAL row, FRESH_LEG_BASELINE, THESIS, NEXUS_BRIEF or GATES cites them; **0 refreshed**: the 48 were not re-verified, and that is owed, not done. Also: 12 ACTIVE rows carry no Stale_By date, and 4 Status values are off-enum (left as is). Moved to processed |

## Carried, stated

DAEDALUS profile items 6, 7 and 10 touch the charter: carried to the separate charter session. Items 8, 11, 12 and 13 (read-cap rotation, LEDGER_GLOB, script docstrings, hygiene): carried, not done today. The casualty ratchet was not recomputed for the 11/17 ADNOC injuries.
