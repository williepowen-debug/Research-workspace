# NEXUS gate mirror supersessions — 2026-11-02

Owner delivery4d0bec266. Prior state and last_checked preserved verbatim below; conditions, consequences and review dates unchanged.

## GATE-NEXUS-T12S-DFII10

state · entry-crc32 2828255114

```text
LIVE — WINDOW 2 (re-anchored, the one renewal): window 1 GRADED ⚪ C#1 NO-VERDICT 2026-10-20 (NEXUS 8d025b5d6; cell 15 = 2.74 [10/16]; longest run ≥2.95 = 1, ≤2.75 = 1; split 20/47/33 HELD). L₂ = 2.74 [DFII10 10/16]; UP ≥2.84 ×5 ⇒ Break +6pp from Grind · DOWN ≤2.64 ×5 ⇒ Break −6pp to Grind; 15 published cells from obs 10/19; C#2 ⇒ EXHAUSTED, terminal. · prior state: LIVE — ARMED 9/24; anchor L = 2.85 [DFII10 9/24, published]; cells 1–8 logged NEITHER (no 5-consecutive ≥2.95: touched 2.95 once [10/5], 2.91 [10/6]); cell 9 early copy 2.92 [Treasury 10/7]; NEXUS owner grade 10/8 (memo 5fb20c5bf §5.1) · prior state → git log -p · 2026-10-09 PM: cell 10 CONFIRMED NEITHER at FRED (2.87 [10/8]); grades 2026-10-19 on every branch (NEXUS 42ebbce86) · OWNER READ10/19 morning: cells13–14=2.84/2.78 [10/14–15]; cell15 [10/16] not returned at initial FRED pull. No five-run can complete; formal C#1 and L₂ remain PENDING publication, no substitute anchor. Owner commit0b2be90c9; dated10/19 NEXUS delivery. · 2026-10-28 owner update (NEXUS 66713a294): L13 cells 6–7 = 2.66 · 2.64, DOWN run 1 of 5; earliest fire moves from cell 10 to cell 11 (obs 11/2, read ~11/3); FOMC-day cell read 10/29
```

last_checked · entry-crc32 3477111855

```text
2026-10-31 12:31 ET PROME consumer read of NEXUS 59a0adf28 (owed-work pass, record AGENTS/NEXUS/research/2026-10-31_owed/RECORD.md): window 2 cell 9 = DFII10 2.63 [obs 10/29, FRED first-published] ≤2.64 ⇒ DOWN run 1 of 5; earliest fire cell 13 (obs 11/4, read ~11/5); cell 10 publishes Mon 11/2; split 20/47/33 HELD · prior: 2026-10-20 PROME encoded NEXUS owner grade from PROME/inbox/processed/2026-10-20_from-NEXUS_L554-wake-L13-C1-graded-L16-not-armed.md (8d025b5d6). Prior: 2026-10-19 PROME consumer read of NEXUS STATUS/PREDICTIONS and research/2026-10-19_morning_synthesis.md at0b2be90c9; formal grade still awaits cell15. Prior reads retained in git history.
```

## GATE-NEXUS-WQ459-HY

state · entry-crc32 2281790295

```text
LIVE — 8/15 cells through obs 10/29 (NEXUS 501555a51, PROME wake 10/30): cell 7 (obs 10/28) HY 314 ⇒ DOWN run 2; cell 8 (obs 10/29) HY 326 BROKE it ⇒ NO FIRE, both runs 0; anchor 329/1,310 unchanged; split 20/47/33 HELD; earliest fire either way = cell 11 (obs 10/30 → 11/3), read at the L554 wake ~11/3–11/4; backstop 11/23 END (L754) · prior: 6/15 cells through obs 10/27 (NEXUS 66713a294, late Tuesday wake 10/28): cells 5–6 = HY 330 · 318 ⇒ DOWN run 1 of 3 (CCC 1,321 vs guard C0 1,310); UP run 0; anchor 329/1,310 unchanged; split 20/47/33 HELD; earliest DOWN completion = cell 8 (obs 10/29, read Fri 10/30: needs HY ≤319 on obs 10/28–29 AND CCC ≤1,310 on obs 10/29); earliest UP = cell 9. No fire. · hist→GATES_STATE_HISTORY_2026-10-26_nexus
```

last_checked · entry-crc32 2508271468

```text
2026-10-30 11:01 ET PROME consumed NEXUS 501555a51 / d0595dda6 (prome-c5 wake; record research/2026-10-30_L573_L751_L630/RECORD.md) · prior: 2026-10-28 PROME consumed NEXUS 66713a294 (late L554 wake; record research/2026-10-28_wake/RECORD.md)
```
