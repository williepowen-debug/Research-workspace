# LIQUID → PROME · 2026-09-25 ~01:4x ET · Reply to Will's item 3: does credit transmission persist?

**Answers:** `AGENTS/LIQUID/inbox/processed/2026-09-25_from-PROME_bounded-follow-up-does-credit-transmission-persist.md` (`40915c8c0`).
**Artifact:** `AGENTS/LIQUID/reports/2026-09-25_credit-transmission-persistence.md` · instrument `AGENTS/LIQUID/scripts/transmission_check.py` · commit `227417176`.

## COMPLETION

**STATUS:** 4 of 4 DONE. Graded on the **9/23** set because the 9/24 ICE cells were not yet published at run time (01:0x ET). **The next observation is FRED ~9/25 16:15 ET**, graded on a rule pre-registered in the report §1c.

**CHANGED:**
- `AGENTS/LIQUID/reports/2026-09-25_credit-transmission-persistence.md` (NEW) + `_transmission_check_output.txt` (raw run)
- `AGENTS/LIQUID/scripts/transmission_check.py` (NEW; re-run after each FRED publication)
- `AGENTS/LIQUID/STATUS.md`: BOTTOM LINE re-cut to obs 9/23 and the vintage banner removed. 8th rotation → `archive/status_snapshots/STATUS_PROSE_2026-09-25_rotation.md` (crc32 `d9a1fee7` / `7dfd6acb`, re-verified from the archive). 5 of 5 gates by grep. 21,541 B = 66% of budget.
- `AGENTS/LIQUID/workbook/CATALYSTS.tsv` + `CALENDAR.md`: new row **2026-10-08 Q3-end PERSISTENCE verdict** (twin kept in sync).

**RESULT:**

| # | Ask | Result |
|---|---|---|
| 1 | Grade the ladder; CONTINUES / BROADENS / REVERSES | **CONTINUES, at the bottom rung only, at an ordinary pace.** FRED 9/23: IG 77 · BBB 95 · BB 159 · B 278 · CCC 1,093 · HY 273. KB-LIQ-128 method (15-session change vs own history, n=765 since 2023-10), 9/2→9/23: **CCC +40 = 81.8th pct (≈1 in 5 windows) · CCC−B gap +38 = 85.9th (≈1 in 7)** · B +2 · BB +6 · BBB −4 · IG −4. Not BROADENS: nothing above CCC is unusual on three weeks, and IG/BBB tightened. Not REVERSES: CCC and CCC−BB are 2026 highs. The reach into B is **one day** (9/23 B +7 = 90th pct of days, CCC +18 = 95.6th), on a +15bp real-yield-led 10Y day. The three-week gap signal is *weaker* than KB-LIQ-128's 9/16 read (93.9th → 85.9th). The 9/24 grade has a fourth outcome, **STALLS**, because the three buckets are not exhaustive |
| 2 | Pair with funding, date-matched; name what is not observed | **Clean on every gauge observed [9/23]:** SOFR−IORB −3 · SOFR75−IORB +2 · SOFR99−IORB +5 (079 ARM +30) · TGCR−IORB −5 · SRF $0.001B · RRP $0.46B · WRESBAL $2,930.2B (−$83.6B w/w on TGA +$100.1B; cushion $130B). **No funding leg to the credit move.** **Not observed:** tri-party volumes and haircuts (TGCR rate only) · sponsored repo · dealer balance sheets (NY Fed PD last pulled for as-of 8/19) · GCF · MMF flows · FHLB · FX-swap / EUR cross-currency basis · SOFR 9/24 (pub 9/25 ~08:00) |
| 3 | Q-end normal pattern + the persistence test | **Normal (10 quarter-ends, 2024-Q1→2026-Q2):** SOFR−IORB peaks a **median +10bp** over baseline on the date (range +1 to +22), **+3 by QE+2, ~0 by QE+3 to QE+5**. 2026's two turns were +4/+6, gone by QE+2, with zero SRF. SRF after the date: ≤$0.75B in 9 of 10 (the exception is $22.8B on 2026-01-02). Baseline now SOFR−IORB −3 / SOFR99−IORB +5. **PERSISTENT = (SOFR−IORB ≥ +1bp on Mon 10/5 [pub 10/6] AND ≥ 0bp on Wed 10/7 [pub 10/8]) · or SOFR99−IORB ≥ +22bp on Fri 10/2 [pub 10/5] · or SRF > $1B on 10/1/10/2/10/5 · or WRESBAL < $2.8T (as-of 9/30 or 10/7).** None by the 10/8 prints = SEASONAL. Only 2025-Q1/Q2 (the late-QT drift) met the first leg. The 9/30 spike itself is the NULL (KB-LIQ-051) |
| 4 | Re-cut the BOTTOM LINE | DONE: obs 9/23, one home for every level, coverage gaps carried in their own paragraph |

**GAPS (preserved):**
1. FRED ICE BofA history is a **rolling ~3 years** (earliest 2023-09-25). Every percentile is ranked against a calm window with no 2020/2022 stress; the same move would rank lower across a full cycle.
2. Every figure is latest-revised, not as-first-published (except the HY-REKILL watcher).
3. HY-Energy OAS permanently unmeasured; HY breadth terminal-gated.
4. The funding blind spots listed in #2.
5. The Q-end base rate has n=10 across two regimes; only 2 quarter-ends are from the current regime.
6. yfinance dropped the 9/22 bar on HYG/JNK/LQD/^TNX (the same fault as T3's DX-Y.NYB).

**Side finding (no gate change):** GATE-LIQ-069 L4's HY leg was **met for the first time** in the prospective window (HY +5 [9/23]; prior max +4). The equity leg failed on the date-matched session (worst APLD −4.6% vs −15%) ⇒ **NOT FIRED**. `gate069_legs.py` pairs the T+1 HY obs with the latest equity session (KB-LIQ-126 class); **repair owed**, my lane.

**WILL_NEEDS:** none to decide. **One thing to watch: the 10/8 persistence verdict** (the 10/5–10/8 prints above). The next credit grade is the 9/24 cells at ~9/25 16:15 ET.

Book FLAT · $0 · no gate, band or threshold changed. Staying live; closing only on PROME's ask.
