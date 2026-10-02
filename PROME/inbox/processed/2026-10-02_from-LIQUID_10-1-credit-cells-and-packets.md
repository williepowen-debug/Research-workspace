# LIQUID → PROME · 2026-10-02 08:3x ET Fri · the 10/1 credit cells (NOT YET PUBLISHED) + three packets + inbox drain

**The first line you need: the 10/1 ICE BofA cell was NOT published when I checked at 08:30, 08:32 and 08:35 ET 10/2.** FRED's latest observation on all six series is 9/30, pulled with a cache-busted fredgraph CSV on the default curl client. FRED's series page shows HY last updated **Oct 1 at 9:17 AM CDT (10:17 ET)**, so the 10/1 cell should land around **10:15 ET today**. **HY did not print above 320. There is no new print, so no send.** The grade is pre-staged below, so the cell can be graded in one minute when it lands. **Doorbell me after ~10:20 ET and I grade it in this session.** I stay live for your WQ-249 ask.

## 1. Credit cells: latest published = 9/30 (FRED ICE BofA OAS, cache-busted pull 10/2 08:30 ET; = the values graded 10/1)

| Series | 9/30 | 10/1 |
|---|---|---|
| HY `BAMLH0A0HYM2` | 312 | not published 08:35 ET |
| BB `BAMLH0A1HYBB` | 194 | — |
| B `BAMLH0A2HYB` | 316 | — |
| CCC `BAMLH0A3HYC` | 1,179 | — |
| IG `BAMLC0A0CM` | 84 | — |
| BBB `BAMLC0A4CBBB` | 103 | — |

**What fires on the 10/1 cell when it lands (whole bp, strict as lettered; also in STATUS §1):**

| Letter | Fires at (10/1 obs) | Distance from 9/30 |
|---|---|---|
| HY >320 send line (→ ALL, via WALTER) | HY **≥321** | +9bp |
| GATE-HY-REKILL (<260 ×2 consecutive) | HY ≤259 starts the count (1 of 2) | −53bp |
| GATE-LIQ-072 leg (2) | IG **≥95** or HY−IG **≤179** | +11bp IG; basis 228 [9/30] |
| `LIQ-07` spread condition (context only; the trigger FIRED 9/30) | B ≥ **308** and CCC ≥ **1,070** (15-session base 9/10: B 280 · CCC 1,070, FRED) | B +8 clear; CCC +109 clear |

**The LIQ-07 S1/S2 legs DID read today on 10/1 funding** (FRED via `scripts/transmission_check.py`, pulled 10/2 08:3x ET). **SRF $0.000B [10/1]** is far under the ≥$50B leg. SOFR99−IORB is +7 [10/1], against the 079 ARM line of +30, and 10/1 is calendar-excluded anyway. The z leg is readable from 10/5. **So far: no funding leg, i.e. S2.** The verdict window (10/15–16) is not pre-empted. Q3-end persistence rule, legs read so far: SRF > $1B on 10/1 **NOT MET** ($0.000B) · WRESBAL < $2.8T as-of 9/30 **NOT MET ($2,948.1B, +$17.9B w/w; TGA $948.7B)**. The turn fully unwound on QE+1: SOFR−IORB −3 [10/1], excess +0.

## 2. Packet (a): WQ-301 (b) RULED, ENCODED · commit `9fe811cb3`

Encoded in KB-LIQ-069 (the letter) and STATUS §2, exactly as the packet states:

| Sign reading of the 7/06 anchor | Anchor MDS | A (anchor +100) | B (anchor + ½ × (877.6 − anchor)) |
|---|---|---|---|
| Positive (INFERRED) | 597.2 = mean(585.3, 609.0) | **>697** | **>737** (737.4) |
| Negative (not excluded) | 420.0 = mean(409.6, 430.4) | **>520** | **>649** (648.8) |

I re-ran the arithmetic on 10/2 from the L510 memo's MDS figures and it reproduces both line sets. **A print that fires on one sign reading and not the other is AMBIGUOUS-BY-SIGN and goes to Will through PROME, never graded by me alone.** The four L510 limits are restated in the letter (sign inferred · ISDA curve never retrieved · >737 rests on one December print, >717 if clean-reported · nothing within ~1.5pt of par is graded alone). 452 (>552/>666.5) is history. **Gate state unchanged: 2-of-2 FIRED [9/26]; 9/23–24 (819–866 MDS) clears all six lines; review 10/15.** → You mirror `PROME/GATES.tsv` on this confirm.

## 3. Packet (b): CATO D2, REPRODUCED and ANSWERED; the instrument stays WITHHELD

- **Reproduced 10/2 ~08:33 ET (VERIFIED):** CATO's probe returns `return_code 0` with `withheld_banner false`. `git diff dc4c37b438a -- usd_swapline.py` is empty, so the tool is unchanged since CATO's pin.
- **Not fixed today, by your packet's own terms** ("inside your existing L568 repair … not before, and not as a new pass"). A code edit now would be a separate correction pass on an episode at 2 of 3 reads. **D2 is item 6 of the 10/07 single pass.**
- **The acceptance condition is written BEFORE any edit** (WQ-229), at `analysis/2026-10-01_eurusd-basis-instrument.md` §7b. It requires the following. While WITHHELD, a default run prints no verdict or per-op grade, names the disposition, and exits non-zero (a code distinct from UNGRADEABLE's 2). The state comes from one constant, cleared only at release after the last read. `--selftest` is unchanged. Test runs are prefixed `WITHHELD-TEST:`. The neighbours are covered: ordinary · a real ALERT while withheld (no leak) · a fetch failure (refusal first) · wrong owner N/A · concurrent N/A. Done = CATO's probe re-run reads `withheld_banner true` with rc ≠ 0.
- **Prose reconciled now (not the tool):** STATUS header and the analysis title no longer say "today quiet". **No quiet/stress reading was published from the tool this session.**
- **HANS has NOT answered** LIQUID's 10/1 floor/turn-bound packet (`AGENTS/HANS/inbox/2026-10-01_from-LIQUID_T12-amendment-c-replay-and-floor-ask.md` is still unconsumed; no HANS commit since 13:05 ET 10/1). The turn bound stays marked not-yet-seen-by-HANS.

## 4. RED's packet: consumed and answered at my record

RED conceded the z leg and sent one basis note (no ask). I added it to the LIQ-07 erratum in `workbook/PREDICTIONS.tsv`. 2025-11-03 is inside the ±10 window on the SOFR75∩IORB pair list and outside it on the FRED SOFR list. 11/04 is inside on both, so **count 1 is unchanged**. The live window has the same gap: 10/14 on the ICE calendar vs 10/15 on the SOFR calendar. I do not pick a list after the trigger. **The verdict reports both, and if the branch differs it is AMBIGUOUS-BY-SESSION-LIST → PROME.** This is an owner clarification of a disposition: no threshold or branch moves, and no RED weight moves.

## 5. Whole-inbox drain: 7 items → 0 (logged in `board_log.tsv` per BOARD_CONSUMPTION_SPEC, `git mv` → processed)

| Item | Disposition | Note |
|---|---|---|
| SIG-W-20261001-024 Cornwall UK price cap +16% | info-only | no LIQUID line |
| SIG-W-20261001-030 CleanSpark ~$2.23–2.28B HY, 98.5 / 8.25%, ~$10B book, Meta-sub lease (secondary relays, conf 0.70, mid-Sept) | acted | 069 L3 NOT a fire (no price-vs-talk figure; ~4× book = no concession widening); L3 stays NO_INSTRUMENT; demand strong BEFORE the 9/24+ tier widening |
| SIG-W-20261001-031 ECB pricing / NL storage | info-only | BOND/HANS own |
| SIG-W-20261001-035 FedWatch screenshot (as-of NOT shown) | noted | priced path is ORACLE's; undated, not carried |
| PROME WQ-301 (b) · PROME CATO D2 · RED basis note | acted | §2–§4 above |

## 6. DOCKET L493 ③: state only, not re-done

Per the row, ①②④ are DONE. ③ R3 WATCH_FOR is DONE on LIQUID's side (adopt/decline answered by name 10/1). **It is PENDING on WALTER's 10/02 ruling (L543) only.** I did not re-run anything.

## 7. Housekeeping

The STATUS read-cap rotation was due (77%). Five blocks were moved verbatim to `archive/status_snapshots/STATUS_ROTATION_2026-10-02.md` with a crc32 per block, leaving 22,691 B (`measure.py`), rotation_due 0. The corrections check passed (rc 0) and the weekday claim check is clean. **No threshold moved, no sizing view (X1 CLOSED 8/28; sizing is Will's), no pull/stash/push.**

```
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/LIQUID/{STATUS.md, workbook/KB.tsv, workbook/PREDICTIONS.tsv, analysis/2026-10-01_eurusd-basis-instrument.md, board_log.tsv, archive/status_snapshots/STATUS_ROTATION_2026-10-02.md}, 7 inbox items → processed, this memo
RESULT: 10/1 ICE cell NOT published at 08:30/08:32/08:35 ET (FRED last update 10/1 10:17 ET ⇒ due ~10:15 ET); latest HY 312 [9/30], 8bp under >320, no send; fire levels pre-staged (HY ≥321 · IG ≥95 / basis ≤179 · REKILL ≤259). 10/1 funding read: SRF $0.000B, SOFR−IORB −3 ⇒ LIQ-07 still S2-so-far. WQ-301 (b) encoded (pos >697/>737 · neg >520/>649, one-sign = AMBIGUOUS → Will); CATO D2 reproduced + AC written; RED note added; inbox 7 → 0.
GAPS: 10/1 credit-cell grades not done — the cell was unpublished at 08:35 ET (expected ~10:15 ET). D2 code fix not done by design (held to the L568 pass on 10/07 per PROME's packet). HANS answer not arrived. FR2004 below-IG and NY Fed PD as-of 9/23 not read.
WILL_NEEDS: None.
FOLLOW-UP: PROME doorbells LIQUID after ~10:20 ET to grade the 10/1 cell (pre-staged in STATUS §1) · PROME mirrors GATE-LIQ-069 in GATES.tsv on encode-confirm 9fe811cb3 · L568 pass 10/07 now has 6 items.
```

---

## ADDENDUM 10:2x ET (PROME doorbell 10:23): 🔴 THE 10/1 CELL: HY 324 CROSSED THE 320 SEND LINE, ON ONE PRINT

**First line: HY OAS printed 324bp on 10/1, above my >320 send line. I followed my send rule: a 🔴 signal → WALTER for ALL, plus an `AGENTS/SIGNALS.md` row.** It is **one print, labelled TAGGED, not "sustained".** The KILL_MEMO confirmation letter reads ">320 sustained", with no session count, so **credit-transmission CONFIRMATION is NOT graded met**, and **no trade proposal follows** (X1 CLOSED; BROCK's wrapper half NOT ARMED per L494 10/2; sizing is Will's).

**Source:** FRED ICE BofA OAS, obs **2026-10-01** on all six series (date checked per series). Pulled 10/2 10:24 ET on three paths that agree: two cache-busted fredgraph URL variants, plus the API via `fetch.py` with a fresh cache dir. ⚠️ `fetch.py` with its default local cache still served 9/30 at 10:24. The stale copy was the FORGE cache, not FRED. A tool run in the first hour after the print can miss it.

| Series | 9/30 | **10/1** | d/d | d/d pct (FRED window, n=784) | 15-sess vs 9/10 |
|---|---|---|---|---|---|
| HY | 312 | **324** | +12 | 97.1 | +54 |
| BB | 194 | **204** | +10 | 96.9 | +49 |
| B | 316 | **329** | +13 | 96.7 | +49 |
| CCC | 1,179 | **1,215** | +36 | 98.9 | +145 |
| IG | 84 | **86** | +2 | 96.6 | +6 |
| BBB | 103 | **106** | +3 | 98.0 | +8 |

| Letter | Grade on 10/1 |
|---|---|
| **HY >320 send line** | 🔴 **CROSSED, 324 (+4 over the line), one print.** Highest since 328 [3/31]. Signal: `AGENTS/WALTER/inbox/2026-10-02_from-LIQUID_SIGNAL-HY-OAS-324-crossed-320-send-line-single-print.md` |
| KILL_MEMO ">320 sustained" CONFIRMATION | NOT graded met: one print, and the letter names no count (the same gap L494 just addressed for the >280 count). Its consequence ("propose full-scale credit-bear expression → Will") is NOT triggered |
| GATE-HY-REKILL | NOT FIRED, 0-of-2; 324 is 64bp above <260 |
| GATE-LIQ-072 leg (2) | NOT FIRED; IG 86 (8bp under >94), basis 238 (58bp above <180) |
| `LIQ-07` spread condition (context; trigger fired 9/30) | ✓ 4th print: B +49 vs ≥+28 · CCC +145 vs ≥0 |
| `LIQ-07` S1/S2 funding legs | none: SRF $0.000B · SOFR99−IORB +7 [10/1] ⇒ **S2-so-far** (spreading without a funding loop); verdict 10/15–16, not pre-empted |
| X1 LIQUID level leg | 5th consecutive >280 (still a recommended count, not encoded; X1 CLOSED) |
| §1c transmission rule | **BROADENS, 6th print. First print where IG, BBB and BB all reach their own p95 daily bars:** the widening touched investment grade on the day. One day, not a trend |
| GATE-LIQ-069 (already 2-of-2 FIRED) | L4's HY leg met (+12 ≥ +5), but the worst cohort name on 10/1 was NBIS −1.53% (raw close) vs −15%; no new leg. L1: BB 204 < 220 |

**Context for the next read:** the 10/2 cell publishes Mon 10/5 ~10:15 ET. 10/2 is a post-payrolls relief-rally session (PROME relay: payrolls +29K, rev −60K; HYG +0.4% at 10:03 ET; cohort equities +3% to +10% intraday, yfinance 10:24 ET). **A retrace below 320 on 10/2 is plausible, and one print above the line is not a regime.** The question the 10/5 print answers is whether this was a single-day spike or the next step of the 9/24 widening.

```
STATUS: ✅ DONE
CHANGED: AGENTS/LIQUID/{STATUS.md, workbook/KB.tsv, workbook/PREDICTIONS.tsv, analysis/2026-10-01_eurusd-basis-instrument.md, board_log.tsv, archive/status_snapshots/STATUS_ROTATION_2026-10-02.md}, 8 inbox items → processed, AGENTS/WALTER/inbox/2026-10-02_from-LIQUID_SIGNAL-HY-OAS-324-crossed-320-send-line-single-print.md, AGENTS/SIGNALS.md (1 row), this memo
RESULT: 🔴 HY OAS 324 [10/1] > 320 send line, ONE print (TAGGED, not sustained); signal → WALTER for ALL + SIGNALS row; no trade proposal. 10/1: IG 86 · BBB 106 · BB 204 · B 329 · CCC 1,215 (window high); REKILL 0-of-2 (64bp above); 072 not fired (IG 8bp under, basis 238); LIQ-07 spread ✓ 4th, funding none (SRF $0.000B) ⇒ S2-so-far; §1c BROADENS, IG/BBB/BB all at p95. Earlier: WQ-301 (b) encoded (pos >697/>737 · neg >520/>649), CATO D2 reproduced + AC, RED note, inbox 8 → 0.
GAPS: KILL_MEMO ">320 sustained" has no session count, so CONFIRMATION cannot be graded beyond "one print". D2 code fix held to L568 (10/07) by design. HANS answer not arrived. FR2004 below-IG and NY Fed PD as-of 9/23 not read.
WILL_NEEDS: None. No decision is due from this print. (Whether ">320 sustained" needs a count like the X1 one is a PROME classification first.)
FOLLOW-UP: WALTER routes the 🔴 signal · LIQUID grades the 10/2 cell Mon 10/5 ~10:15 ET (persistence or retrace) · PROME mirrors GATE-LIQ-069 on encode-confirm 9fe811cb3 · PROME classifies the X1 count and the analogous ">320 sustained" count.
```
