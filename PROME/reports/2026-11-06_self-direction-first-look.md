# How PROME could keep working without direction: first look

**Asked by Will, 2026-11-06 21:05 ET. Read-only survey, session prome-bf. No build, no authority change. Feeds the Sunday recommendation.**

| Question | What exists | State |
|---|---|---|
| What should I do next? | BOOT steps 8 and 9 (start the highest-priority authorized work); SCRATCH ★ NEXT, written by hand at closeout; DOCKET 269 live rows, 34 led by PROME; GATES; WILL_QUEUE; spawn_list for due desk rows | Exists, but split across surfaces, and applied at boot only |
| Am I allowed? | AUTONOMY Tiers 1 to 3; charter C1 to C9; caps | Exists |
| When must I stop and ask? | BOOT step 8 interrupt test | Exists, written for boot only |
| What wakes me? | Hooks fire only inside a running session. Laptop: no timer of ours, one cron line (ORACLE script, weekdays, not a PROME wake). Root repo: no GitHub workflow. Research-Intake collect.yml collects data and decides nothing. Session-only reminders proved tonight | MISSING |
| What tells me a run failed? | ORCH_LOG, delivery log, receipts, read after the fact | Partial |
| Who checks me? | ARGUS once a day, desk verification, closeout gates | Partial, and my error lists show it is needed |

**Limit found:** WQ-388 RULED DECLINE concerns WALTER self-scheduling; sessions start only when Will or PROME launches them. PROME waking itself on a schedule is an unattended run and needs Will's word (his 11/6 terms).

**Not tested:** whether a cloud routine can work this repo, what it costs, and whether in-session self-pacing survives idle compaction.
