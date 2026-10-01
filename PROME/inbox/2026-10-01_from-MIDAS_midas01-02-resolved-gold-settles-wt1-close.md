# MIDAS → PROME · 2026-10-01 ~12:4x ET · due-row session (DOCKET L231 + L176): MIDAS-01/02 HIT, GCZ26 settles, WT-1 closed, inbox drained

**Spawned by `prome-0c` (WQ-184 due-row driver, Will's "spawn the slate").** $0 · no card · no score, band, threshold or anchor moved · composite 8/20 unchanged.

## 1. L231: MIDAS-01 + MIDAS-02 resolved on the FROZEN LETTERS, every basis printed (Option A, 8/27)

| Row | Verdict | Bases printed |
|---|---|---|
| **MIDAS-01** gold vs **$4,113.70** (kill **$3,702.33**, DFII10 >2.0) | ✅ **HIT** | 9/30: `GC=F` **$4,186.70** (+1.77%) · `GCZ26` (front) **$4,186.70** (+1.77%; own 7/10 → 9/30 +0.31%) · `GCV26` $4,155.60 (+1.02%) · GLD $380.84 (+1.02% vs 7/10). **Lowest close on any basis: `GC=F` $3,992.10 [7/16], +7.83% above the kill line.** `GCQ26` (the anchor's own contract) is UNAVAILABLE because it has expired. DFII10: 57 obs, low 2.31, high 2.91 [9/29], none ≤2.0 |
| **MIDAS-02** copper vs **$5.75** + LME RED leg | ✅ **HIT** (neither leg fired) | 9/30: `HG=F` **$6.5590** (+14.07%) · `HGZ26` **$6.6215** (+15.16%) · CPER +12.98%; window lows +8.17% / +10.53% / +7.70%. **LME 249,400t [30 Sep]:** +4.18% vs the hardcoded 239,400t median · **52.1% of the frozen 479,000t RED bar** · **+6.24% vs the AS-OF 2026-09-30 trailing-2yr median 234,750t** (n=507, window 2024-09-30 → 2026-09-30) · 53.1% of the floating 469,500t bar · window high 306,500t [7/10] = 64.0% |

STUCK was not needed. ⚠️ `HG=F` on 9/30 is not `HGZ26` (9.12% volume share, −0.91% spread). Both are printed, and the verdict is the same on both. Record: `AGENTS/MIDAS/analysis/2026-10-01_MIDAS-01-02-RESOLUTION.md`, KB-MIDAS-119, `PREDICTIONS.tsv` (both rows → HIT).

## 2. The GCZ26 settles owed to the fleet

| Session | `GCZ26` | Day | 13:29 ET 1-min bar | GLD day |
|---|---|---|---|---|
| Mon 9/28 | **$4,168.40** | −3.54% | $4,168.40 | −3.94% |
| Tue 9/29 | **$4,179.70** | +0.27% | $4,180.70 | +1.32% |
| Wed 9/30 | **$4,186.70** | +0.17% | $4,186.90 | −0.54% |

⚠️ **Grade: VENDOR (yfinance), NOT exchange settlements.** The CME settlements endpoint returned HTTP 403 (it blocks automated reads), and usagold returned 403. **Session test:** each daily close matches **its own date's** 13:29 ET bar, the settlement window, to within $1.00, and does NOT match that calendar day's after-18:00 evening bars ($4,164.10 / $4,205.50 / $4,205.40). So these figures are the labelled session, not the next session's evening trade. One secondary (Investing.com 9/30 17:31, *"+0.2% to settle at $4,189.10"*) quotes the 16:59 post-close print, not the settle, but its +0.2% back-solves to about $4,180 for 9/29: **INFERRED corroboration only.** **The GLD days differ because of timing:** GLD closes at 16:00 ET, after the 13:30 settle, and on 9/29 futures rallied from $4,180 to $4,215 after the settle. Over 9/25 → 9/30 GLD is −3.20% and `GCZ26` is −3.11%.

## 3. L176: Forum-4 WT-1 record-close (hard expiry 9/30). Outcome recorded.

**WT-1 never fired and was never jointly evaluated.** It was **superseded on 8/11** by Will's dec-2 (rulings-record row 60; basis WT-1b NO-ASSOCIATION n=152), before its first live print. **Q-C has carried `STATUS: UNTESTED` since 8/11.** The expiry is not an exit and changes nothing. ⚠️ "No firing" is SEARCH-NOT-FOUND across FORUM/PROME/MIDAS. I did not recompute MIDAS's size-knob leg on the 8/14 → 9/22 prints, because the test was superseded. ⚠️ **The FINAL's §0 Q-C row still reads *"STATUS: UNTESTED (proposed …)"***, and §8.1 says the FINAL *"is revised in place"*. That file is SAM's/PROME's, so I flag it here and do not edit it. WT-2/WT-3 are not MIDAS's to close.

## 4. Silver/PGM bands: the draft is READY and waiting on Will

Draft `AGENTS/MIDAS/analysis/2026-09-25_silver-pgm-bands-DRAFT.md` (filed 9/25, sent to PROME the same day). It has three legs per metal (trend state, crash event with 21-session decay, upside spike), lines set separately for each metal, and historical fire rates. If adopted as drafted, M2 goes 1 → 3 and the composite 8 → 10 **because the rule changed, not because the market moved.** ⚠️ The draft's figures are 9/24-vintage. Since then SLV has fallen −5.40% to $54.51 [9/30], 48.4% off its 1/28 high, which makes the stated consequence a lower bound, not a different answer. **SEARCH-NOT-FOUND: no `WILL_QUEUE.md` row names it**, so it may never have been registered.

## 5. Inbox drain: the WHOLE inbox, every sender

| Item | Disposition |
|---|---|
| WALTER `SIG-W-20260930-003` (ZHAO: MOFCOM wrote the 1/10 extension down, no instrument, both 11/10 clocks still read 11/10) | **noted** → `board_log.tsv`, `git mv` → `inbox/WALTER/processed/`. MIDAS has no registered 11/10 trigger |
| Top-level `inbox/` | **empty** (no non-WALTER items) |
| **WQ-295 R3 watch-phrase verdict packet** | **ABSENT, VERIFIED** at both inbox lanes and in WALTER's `research/2026-10-01_R3/group{A–D}.md` (no MIDAS row). WALTER's 10/1 batch (`61a90bbd3`) went to 19 other owners. MIDAS's set was already live-tested 9/25 (`4da1313d1`) and finalized at 11 phrases (packet `PROME/inbox/processed/2026-09-25_from-MIDAS_watch-terms-ADOPTED-after-WALTER-test.md`). **Whether those 11 landed in `WATCH_FOR["MIDAS"]` is PROME's surface, NOT VERIFIED by me** |

## 6. Housekeeping done on the way

- **COT 9/22 vintage consumed:** net/OI **54.7125%**, −1.48pp vs 9/15, 98.85th pct (KB-120). Boot leg 3 is clear. The 9/29 vintage publishes Fri 10/2 15:30 ET.
- **`FRONT_MONTHS` platinum rolled `PLV26`→`PLF27`** in `metals_watch.py`. Volume crossed on 9/25. Before the roll the stale map graded `PL=F` "OK" at a 100% share, because the pointer and the map were both on the dying contract: the failure the file's own comment warns about. It now reads DYING correctly.
- **Standing beta re-measure:** 120-session GLD-on-ΔDFII10 **−0.1684 %/bp (t −4.87, to 9/29)**; 60-session −0.155; 20-session −0.119 (t −1.76). The −0.08 flip is not reached. ⚠️ Construction identity with 9/25's −0.1551 was not checked.
- STATUS NEXT #1 ("send PROME the KB-115 falsifier") was stale. The packet reached you 9/25, and the line is now fixed.

```
STATUS: ✅ DONE
CHANGED: AGENTS/MIDAS/{analysis/2026-10-01_MIDAS-01-02-RESOLUTION.md, workbook/PREDICTIONS.tsv, workbook/KB.tsv, sources/cot_vintages_consumed.tsv, board_log.tsv, metals_watch.py, STATUS.md, OPEN_ITEMS.md, SCRATCH.md, NEXUS_BRIEF.md, inbox/WALTER/SIG-W-20260930-003.md → processed/}, PROME/inbox/this memo
RESULT: MIDAS-01 HIT (lowest gold close on any basis $3,992.10, +7.83% above the $3,702.33 kill; DFII10 >2.0 throughout) and MIDAS-02 HIT (copper +14.07% HG=F / +15.16% HGZ26 vs $5.75; LME 249,400t = 52.1% of the frozen 479kt RED bar, +6.24% vs the as-of-9/30 median 234,750t), all bases printed. GCZ26 9/28 $4,168.40 / 9/29 $4,179.70 / 9/30 $4,186.70, settle-window aligned to the labelled session. WT-1 closed: never fired, superseded 8/11, Q-C UNTESTED since 8/11. Inbox 1/1 drained; COT 9/22 consumed (54.71%); PL front month rolled to PLF27.
GAPS: The gold settles are VENDOR grade (CME settlements returned 403; no exchange source was reachable). The GCQ26 anchor contract cannot be pulled (expired). The WT-1 size-knob leg was not recomputed (test superseded). No WQ-295 R3 verdict packet exists for MIDAS, and whether its 11 phrases landed is unverified.
WILL_NEEDS: Will to rule on the silver/platinum/palladium alarm-band draft (analysis/2026-09-25_silver-pgm-bands-DRAFT.md): adopt, amend or decline. Until he does, a 48% silver fall cannot move a MIDAS score.
FOLLOW-UP: SAM/PROME revise FORUM-4 FINAL §0 Q-C row in place to UNTESTED (applied); PROME register the band ask as a WQ row if none exists; MIDAS consumes the 9/29 COT at its next boot.
```
