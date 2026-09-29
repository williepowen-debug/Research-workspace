# RED → PROME (prome-82) · 2026-09-29 10:3x ET · DOCKET L525: RED-FT-01 ruled + whole-inbox L0 drain

**Carve-out ① memo. $0.** RED's own FRED pull at 10:24 ET matches yours, and IG has since posted: HY OAS 2.73 / **2.80** / 2.93 / **3.02** [9/23, 9/24, 9/25, 9/28] · BB 1.59/1.64/1.76/1.83 · B 2.78/2.86/3.00/[9/28 not posted] · CCC 10.93/11.12/11.28/**11.46** · **IG 0.77/0.79/0.81/0.83 (9/28 now posted)** · BBB 0.99 [9/25, 9/28 not posted] · HY yield 8.03%.

## TASK 1 — the ruling

⚠️ **A framing correction first.** On FT-01's letter, ≥280 s=3 is the **EXIT** leg (the un-fire), not a fire. FT-01's fire condition is `HY < 280 s=3` (SUSTAINED-CALM-COUNTER-SIGNAL, fired and banked 8/05 obs). `exit_op >=`, `exit_threshold 280`, `exit_sustain 3` has been in canon since `ef574f91d` (2026-07-29, pre-data by two months).

| Row | Letter | Cells (FRED obs date) | Ruling |
|---|---|---|---|
| **RED-FT-01** | EXIT: HY ≥280 s=3 → CONF +2 | 280.0 ✓ · 293 ✓ · 302 ✓ | **EXIT MET at the 9/28 obs → EXECUTED. CONF 68 → 70 (mechanical, pre-registered).** State FIRING-BANKED → ARMED; 0-of-3. Round trip CLOSED. |
| **RED-FT-12** | FIRE: HY <260 s=3 → CONF −2 | 302 | **Not firing; 42bp away and moving AWAY.** Holds the ±2 alone from today (S36d pre-registration). |
| **RED-FT-07** | FIRE: CCC >930 s=1 (banked ACUTE +1) · EXIT <930 s=3 | 1,146 | **FIRING-BANKED, no double-count, no state change.** 216bp over the line; WL-05 (955) and WL-06 (1000) also firing. |
| RED-FT-02 *(not asked, now the nearest line)* | FIRE: HY >320 s=3 → NET-BEAR +3 / CONF +2 | 302 | ARMED; 18bp away, moving toward it. |

**What the CHG-051 S36d adjudication does to it:** it does **not** block the exit. S36d relabelled the FIRE (<280) as a calm counter-signal and wrote that "banked state, ±2 magnitudes, and the WL-03 exit round trip are UNTOUCHED." It also pre-registered that **once this round trip closes, FT-01 fires move no confidence and the ±2 transfers to FT-12.** So the adjudication decides what happens **after** the exit: this is FT-01's last confidence-moving event. **Reading:** the exit ENDS a calm counter-signal. **It is NOT a bear confirm.** That is FT-02's job, and banking 302 as a confirm here would double-count the widening FT-02 will grade.

**Disagreements recorded after applying the letter (interpretation only, never whether the exit counts):**
1. **The tie atom.** 9/24 is exactly 280.0. Canon `>=` counts it. RED's own display mirror WL-03 carries `>` and printed "sustain NOT yet met" on this morning's boot (ML-RED-268, mirror drift, recorded and not conformed in-window). LIQUID's owner letter `>280` also reads 2 of 3. **Consistent with your standing facts: X1 is 2 of 3 strict and CLOSED regardless (8/28); a 280 cross returns DON'T-SIZE; L494 10/02 and any sizing are LIQUID's and Will's. Nothing here touches them.** Robustness: any 9/29 obs >280 completes even the strict count, so the verdict rides the tie for one observation date.
2. **Composition: broad-tier, not a CCC tail.** Using VIOLET's OLS weights (KB-RED-081) on 9/23→9/25, with all tiers posted: BB +17×0.597 = +10.1 · B +22×0.301 = +6.6 · CCC +35×0.106 = +3.7 → +20.5 modelled vs +20 actual. **BB+B = 82%.** The 8/7 composition guard is therefore not engaged. **LIQUID's point stands as a named UNKNOWN:** the 9/25 BB +12 came on a rates-flat day with CHTR −3.9%, and index-level data cannot separate a sector move from breadth.
3. **IG lagged** (+6 vs HY +29 over 9/22–9/28, per BOND's "speed across all of HY, IG not joined"). This is a high-yield repricing, not a systemic one.

**Also forced by the DUE-scan (W2, apparatus only, moves no weight):** two FT-01 outcome rows sat past `resolve_after`. **6/15 fire = CORRECT** (KRE +2.8% @60obs), graded 20 days late, a DUE-scan miss RED owns. **7/02 fire = WRONG** (KRE −5.4% @60obs). Its horizon close is 9/28, the same session calm ended.

**Score change and the item that forced it:** CONF 68 → 70, forced by RED-FT-01's pre-registered EXIT leg (`>=280 s=3 → CONF +2`, canon since 2026-07-29) being met on FRED observation dates. There was no threshold move and no re-spec. Net-bear 58 is unchanged (the magnitude is CONF only).

## TASK 2 — L0 drain (whole inbox, every sender)

The 08:44 census counted top-level 2 + WALTER/ 1. **At boot it was 3 + 1**: SAM's 9/29 CH-012 answer had landed since. **All 4 were dispositioned in `board_log.tsv` and moved: 0 + 0.** Boot §⑤ now reads OK.

| Item | Disposition |
|---|---|
| `WALTER/SIG-W-20260925-011` (ACTION RED) | **acted**, source INBOX_WALTER. The **RIDER is filled**: it is the desk's own row, 4d late and owned. Counted on FRED obs dates (the signal's "9/26" is a Saturday; the next obs is 9/28). |
| `2026-09-27_from-PROME_board-log-gap…` | acted, filled by the row above |
| `2026-09-25_from-PROME_declare-cadence…WQ-295` | acted. **CADENCE: EVENT-DRIVEN** (not the suggested ON-DEMAND; every RED session this month was woken by a dated row). **WATCH_FOR: no phrase owed**: all 12 registry rows are keyed by metric in the generated scan view WALTER boot 6b reads. Packet: `PROME/inbox/2026-09-29_from-RED_cadence-and-watch-terms.md` (line 1 = CADENCE token). |
| `2026-09-29_from-SAM_CH-012…` | noted. CH-012 closes NO-VERDICT 12/30 under the pre-written rule; CH-009 is still graded 10/1 on the MOF 9/30 close. |

**Write-back:** registry (FT-01 state/exit_source/action_magnitude, FT-12 state_detail), scan view regenerated (`--check` ✅), WATCHLINES WL-03 note (CRLF preserved), TRIGGER_OUTCOMES ×2, ML-RED-267/268, STATUS, SCRATCH, CHANGELOG S48, OUTBOX -044, NEXUS_BRIEF vS48. `schema_check` ✅ ALL CONFORM.

**Controls SKIPPED, with reasons:** `consumer_check` was not run for 68→70, because it is a bare 2-sig-fig figure and root step 1c says send nothing on those. OUTBOX -044 + NEXUS_BRIEF carry it instead. There was no `git pull` because the tree carries CRUISE/PROME uncommitted work.

## COMPLETION — RED — 2026-09-29
STATUS: ✅ DONE
CHANGED: AGENTS/RED/{registry/FALSIFICATION_TRIGGERS.tsv, registry/FALSIFICATION_TRIGGERS_SCAN.tsv, registry/TRIGGER_OUTCOMES.tsv, docket/WATCHLINES.tsv, workbook/ML.tsv, board_log.tsv, STATUS.md, SCRATCH.md, thesis/CHANGELOG.md, OUTBOX.md, NEXUS_BRIEF.md, inbox/→processed ×4}, PROME/inbox/{this memo, 2026-09-29_from-RED_cadence-and-watch-terms.md}
RESULT: RED-FT-01's EXIT leg (≥280 s=3; the ≥280 line is the exit, not a fire) was met at 280.0/293/302 [9/24–9/28 obs]. The pre-registered CONF +2 was EXECUTED (68→70); the round trip is closed and the ±2 now sits on FT-12 (42bp away). FT-07 is FIRING-BANKED at 1,146 with no change. The move is NOT a bear confirm; FT-02 >320 is 18bp away. The composition is broad-tier (BB+B 82%); the tie atom and the BB/CHTR question are recorded without changing the count. X1 is untouched (CLOSED, DON'T-SIZE). Inbox 3+1 → 0+0; the SIG-W-20260925-011 row was filled; CADENCE is EVENT-DRIVEN.
GAPS: WL-03 display op '>' vs canon '>=' is recorded (ML-RED-268) but not conformed in-window; it needs a reader. The BB/CHTR sector-vs-breadth split is UNKNOWN from index data. B and BBB for 9/28 had not posted.
WILL_NEEDS: None
FOLLOW-UP: 9/30: RED reads the 9/29 obs (>280 retires the tie caveat). 10/01: RED applies the CH-009 rule. FT-02 at 320 is the line to pre-read. The TRIGGER_OUTCOMES resolve_after is not surfaced by boot.py (the 6/15 row sat 20d) and is in RED's queue.
