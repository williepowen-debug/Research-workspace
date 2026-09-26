# WQ-295 R2 — the wake schedule and workload R2 would produce (the demonstration Will asked for before ruling R2)
**Computed 2026-09-26 15:14 ET (`prome-1d`) from the roster cadence table AFTER R1's provisional tokens (36 desks: 12 owner-declared + 24 provisional, ROSTER § DESK CADENCE), each desk's last SELF-commit by `spawn_list.py`'s own attribution (`Liveness.last_self_commit`, L455 rule), and the dated DOCKET/GATES rows naming each desk inside 14 days (`spawn_list.collect`, horizon 14). Script: the session scratchpad `r2_schedule.py` (read-only; re-runnable from these inputs). R2's letter (WQ-295 record § R2): *a desk whose cadence clock is PAST with NO dated row naming it is outcome ① — PROME spawns it Tier 1 at the first boot on/after the clock runs out.*
**Will 15:04:** *"Hold R2 until you show the resulting wake schedule and workload."* This file is that showing; R2 stays HELD.

## The schedule (14 days from Sat 2026-09-26)
| Desk | Token | Last SELF-commit | Clock due | Dated rows naming the desk ≤14d | Under R2 |
|---|---|---|---|---|---|
| AEOLUS | `WEEKLY` | 2026-09-18 (1bc557d98) | 2026-09-25 | 2026-09-30 D:L426 | dated row governs (no cadence wake) |
| BOND | `WEEKLY` | 2026-09-25 (0efabee9b) | 2026-10-02 | 2026-09-26 D:L508; 2026-10-01 D:L410; 2026-10-01 D:L478 | dated row governs (no cadence wake) |
| BRENT | `WEEKLY` | 2026-09-25 (21f47b38f) | 2026-10-02 | 2026-10-02 G:GATE-BRENT-COT-35B; 2026-10-04 D:L297 | dated row governs (no cadence wake) |
| BROCK | `WEEKLY` | 2026-09-26 (0687f382b) | 2026-10-03 | 2026-10-01 D:L479; 2026-10-02 D:L494; 2026-10-07 D:L480 | dated row governs (no cadence wake) |
| CARL | `WEEKLY` | 2026-09-24 (30f3c5219) | 2026-10-01 | 2026-10-01 D:L152 | dated row governs (no cadence wake) |
| CORAL | `WEEKLY` | 2026-09-13 (cd8da96a9) | 2026-09-20 | 2026-09-30 G:GATE-CORAL-MSI-01; 2026-10-02 D:L501 | dated row governs (no cadence wake) |
| CRUISE | `EVENT-DRIVEN` | 2026-09-21 (2bbb38f61) | — | 2026-09-29 D:L221; 2026-10-02 D:L502; 2026-10-03 D:L454 | no clock (token makes no age claim) |
| DAEDALUS | `WEEKLY` | 2026-09-25 (7fbb44c6e) | 2026-10-02 | 2026-09-30 D:L460; 2026-10-02 D:L490; 2026-10-02 D:L495 | dated row governs (no cadence wake) |
| DEWEY | `ON-DEMAND` | 2026-09-26 (6a352c5be) | — | 2026-10-01 D:L468 | no clock (token makes no age claim) |
| FALCON | `WEEKLY` | 2026-09-22 (febe1d0e7) | 2026-09-29 | 2026-09-29 G:GATE-FALCON-001 | dated row governs (no cadence wake) |
| FERT | `EVENT-DRIVEN` | 2026-09-23 (c83de2e60) | — | 2026-09-30 G:GATE-FERT-G5; 2026-10-02 D:L288 | no clock (token makes no age claim) |
| FLG | `EVENT-DRIVEN` | 2026-09-24 (519c49b34) | — | 2026-10-01 D:L236; 2026-10-01 G:GATE-FLG-T08 | no clock (token makes no age claim) |
| HANS | `WEEKLY` | 2026-09-25 (802fe9ee6) | 2026-10-02 | — | CADENCE WAKE on 2026-10-02 |
| HAWK | `WEEKLY` | 2026-09-26 (9bb5a9a1f) | 2026-10-03 | 2026-09-26 D:L507; 2026-09-30 D:L491 | dated row governs (no cadence wake) |
| HENRY | `WEEKLY` | 2026-09-25 (dea50473c) | 2026-10-02 | 2026-09-29 D:L489; 2026-09-30 D:L385; 2026-10-01 D:L475 | dated row governs (no cadence wake) |
| HOMER | `WEEKLY` | 2026-09-24 (72e63a82a) | 2026-10-01 | — | CADENCE WAKE on 2026-10-01 |
| LABOR | `WEEKLY` | 2026-09-24 (079a6ea5d) | 2026-10-01 | 2026-10-02 D:L287 | dated row governs (no cadence wake) |
| LIQUID | `WEEKLY` | 2026-09-26 (ac4dfe0fb) | 2026-10-03 | 2026-09-26 D:L505; 2026-09-28 D:L492; 2026-09-30 G:GATE-HY-REKILL | dated row governs (no cadence wake) |
| MARCO | `WEEKLY` | 2026-09-24 (cea7d2b32) | 2026-10-01 | — | CADENCE WAKE on 2026-10-01 |
| MIDAS | `WEEKLY` | 2026-09-25 (19f485f33) | 2026-10-02 | 2026-09-30 D:L231 | dated row governs (no cadence wake) |
| NEXUS | `ON-DEMAND` | 2026-09-24 (7098326b3) | — | 2026-10-07 D:L36; 2026-10-07 G:GATE-NEXUS-SEAT-01 | no clock (token makes no age claim) |
| ORACLE | `WEEKLY` | 2026-09-25 (9a9250320) | 2026-10-02 | — | CADENCE WAKE on 2026-10-02 |
| OSPREY | `WEEKLY` | 2026-09-24 (191c08230) | 2026-10-01 | 2026-10-06 D:L309 | dated row governs (no cadence wake) |
| OZK | `EVENT-DRIVEN` | 2026-09-24 (a24df0c67) | — | 2026-10-01 D:L126; 2026-10-02 D:L463 | no clock (token makes no age claim) |
| RED | `ON-DEMAND` | 2026-09-25 (82b7ef9b9) | — | 2026-10-01 D:L484 | no clock (token makes no age claim) |
| REGINALD | `WEEKLY` | 2026-09-24 (384366440) | 2026-10-01 | — | CADENCE WAKE on 2026-10-01 |
| SAM | `WEEKLY` | 2026-09-24 (6e0c3a774) | 2026-10-01 | — | CADENCE WAKE on 2026-10-01 |
| SHADE | `WEEKLY` | 2026-08-28 (e0177eefc) | 2026-09-04 | 2026-09-30 D:L182 | dated row governs (no cadence wake) |
| TERRY | `WEEKLY` | 2026-09-26 (9b8b35282) | 2026-10-03 | 2026-09-26 D:L506; 2026-09-30 D:L255; 2026-09-30 D:L74 | dated row governs (no cadence wake) |
| VIOLET | `WEEKLY` | 2026-09-25 (dff7fddbb) | 2026-10-02 | — | CADENCE WAKE on 2026-10-02 |
| VULCAN | `WEEKLY` | 2026-09-25 (2e1cdfdd2) | 2026-10-02 | 2026-09-30 D:L114; 2026-10-05 D:L250 | dated row governs (no cadence wake) |
| WAL | `EVENT-DRIVEN` | 2026-09-24 (37ed0a355) | — | — | no clock (token makes no age claim) |
| WALTER | `DAILY` | 2026-09-25 (c986abcfc) | 2026-09-26 | 2026-09-30 D:L334 | dated row governs (no cadence wake) |
| WATT | `WEEKLY` | 2026-09-25 (a521269db) | 2026-10-02 | — | CADENCE WAKE on 2026-10-02 |
| YURI | `WEEKLY` | 2026-09-25 (f0688f6ee) | 2026-10-02 | 2026-09-26 D:L509; 2026-10-02 D:L434 | dated row governs (no cadence wake) |
| ZHAO | `WEEKLY` | 2026-09-25 (1638b299a) | 2026-10-02 | 2026-09-30 D:L481; 2026-10-09 D:L482 | dated row governs (no cadence wake) |

WORKLOAD (cadence wakes with no dated row, next 14 days):

## Workload, read honestly
- **R2's marginal load is 8 cadence-only wakes in 14 days, and all eight land on two days:** Thu 10/01 (HOMER · MARCO · REGINALD · SAM) and Fri 10/02 (HANS · ORACLE · VIOLET · WATT). Every other desk with a clock is already governed by a dated row inside the window, so R2 adds nothing for it.
- **Those two days are already the heaviest dated days.** 10/01 alone carries dated wakes for FLG (T08 fires), CARL (L152), BOND (L410/L478), OZK (L126), DEWEY (L468) and RED (L484); 10/02 carries BRENT, BROCK, DAEDALUS, LIQUID's clock, LABOR (L287), FERT (L288), ZHAO's follow-ups. With the cap of four due-row spawns per boot, **10/01 would present ~10 wakes against a cap of 4 and 10/02 ~11 — the cap slates the rest for Will's word either way.** R2 does not create that congestion; it adds four to each of the two days that already have it.
- **Two desks are past their clock with a dated row covering them:** CORAL (last self-commit 9/13; GATE-CORAL-MSI-01 review 9/30) and SHADE (8/28; L182 9/30). Under R2 neither would wake early — the dated row governs — which is the intended behaviour, and it is also the case where a stale desk stays stale until its row date.
- **Eight desks carry no-clock tokens** (EVENT-DRIVEN: OZK · WAL · FLG · CRUISE · FERT; ON-DEMAND: DEWEY · NEXUS · RED). R2 never wakes them; their dated rows do. WAL has NO dated row inside 14 days and no clock — it is the one desk this design leaves unreached for two weeks unless a row is registered.

## What PROME would ask Will to add if R2 is approved (design riders, not a re-draft)
1. **A cadence wake never displaces a dated-row wake for the cap:** dated rows fill the four slots first; cadence wakes take the remaining slots and otherwise roll to the next boot with room (they are review hints, not events).
2. **The clock starts from the desk's last SELF-commit, never from a PROME packet or a WALTER delivery into its directory** — the attribution rule L455 already encodes this; R2 inherits it.
3. **WAL-class gap:** an EVENT-DRIVEN desk with no dated row for ≥14 days is surfaced in the boot report as UNREACHED (not woken) so its owner registers a row or PROME asks.

## Caveats
- Last-self-commit dates come from subject attribution; a desk whose commits carry a non-standard subject reads as older than it is (the L455 residue class).
- The 14-day window was chosen to show two full weeks of WEEKLY clocks; a 21-day window would add the MONTHLY class (none declared today).
