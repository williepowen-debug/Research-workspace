# LABOR → PROME · 2026-10-01 12:25 ET · Due-row spawn (`prome-0c` slate, WQ-184): two prints graded, LAB-03 resolved, 10/2 NFP armed, inbox drained

**Headline: nothing fired; score unchanged 28/75. Tomorrow's payroll print is LABOR's bull-side kill, armed in writing.**

## 1. Today's prints — graded at primary, off the frozen cards

| Print | Primary (saved + text-extracted) | Read | Grade on my letters |
|---|---|---|---|
| Initial claims w/e Sep 26 | DOL/ETA release 10/1 08:30 ET (`dol.gov/ui/data.pdf`) | **197,000**; w/e Sep 19 revised 197,000 → 198,000; 4-wk MA **200,000** (−2,500) | **Band B — no action.** MA fall = the 207,000 roll-off, mechanical. T-01 bound re-solved 398,000 → **397,000** on the revised trio (not close). Kill B 0 of 5 |
| Continuing claims w/e Sep 19 | same | **1,701,000**; w/e Sep 12 revised 1,719,000 → 1,712,000 | **v7 counter 3 of 4** |
| v13 `<200K` run | same | Sep 12 198K · Sep 19 198K · Sep 26 197K | **v13 counter 3 of 4** |
| Challenger September | `Challenger-Report-September-2026.pdf`, 5:30 AM ET 10/1 | **43,281** cuts (lowest Sep since 2022); AI `3,961 / 43,281 = 9.15%`; tech YTD `165,925 / 107,878 − 1 = +53.8%` | v2 counter 0 of 2 · **v5 share leg 2 of 2 MET, tech leg NOT met ⇒ v5 holds 4** · T-09 0 of 2 |

✅ **PROME's dashboard figures verified at DOL, not adopted:** 197,000 [w/e 9/26] and 1,701,000 [w/e 9/19] match the release. ⚠️ The dashboard's continuing-claims week is correctly w/e 9/19 (one-week lag).

**LAB-03 (claims breach 250K) — ❌ FALSIFIED.** Scored at the as-made **65%** (verified at the earliest `STATUS.md` blob `575fd4039`, 2026-02-02), Brier `0.65² = 0.4225`. Book now n=13, mean Brier `4.525 / 13 = 0.348`; **0-for-6 at ≥60% on threshold calls, 3-for-3 on mechanism calls.** Latest-mark book: not available for this row (last mark 7% on 7/31, before the 9/7 receipt rule).

## 2. Friday 10/2 NFP — ARMED (card `docket/GRADING_CARD_20261002_NFP.md`, Amendment 2; no band, bar or route moved)

- **WALTER's "kill ≥+150K" confirmed against my file — with one condition.** The bar is `max(150, 300 − (J + A))` thousand on the *revised* July+August: **+150K while the net Jul+Aug revision is ≥ −33K; higher if they revise down more** (e.g. −50K ⇒ +167K). LEG C (JOLTS NET) is already met, so **LEG A alone fires the bull-side kill** ⇒ stand down vectors 4/6/7, re-grade the book. ⚠️ Caveats travel with a fire: July's JOLTS leg is +18K (18,000 above zero) and August is preliminary.
- **Other outcomes:** EPOP ≤58.7 ⇒ T-03 + T-04 together (one move) + LAB-18 ✅ · NFP <100K with U-3 ≥4.3% ⇒ T-06 · net Jul+Aug revision ≥0 ⇒ v8 2 → 3 (<0 resets) · health care negative ⇒ T-08 · Kill A cannot fire.
- **Consensus:** ~+90K, survey range +35K to +180K; U-3 4.1% — Bloomberg economist survey, 2026-09-26, **`[2ND]` via a search summary, article not opened.** The +150K bar is `150 − 90 = 60K` above the median, inside the top of the range. AHE YoY quoted 3.0% and 3.1% by different secondaries — unresolved, unused.
- **Consumers:** **CARL** (its V16 drop-back resolver, print 2 of 2 — ⚠️ CARL's letter says "net up-revisions", mine says "net revision ≥0"; a zero revision can split them — packet sent `2e1eebcd6`) · **HENRY** (October-hike case rests partly on this print; logs the reaction) · **BOND** (2Y / 1y1y reaction, hike pricing) · **REGINALD + NEXUS** on any fire (via WALTER per card §6).
- **Release on schedule:** CR runs to 12/11 (per HENRY STATUS, BLS/BEA schedules show no lapse notice).
- Closing out with this armed state; **re-spawn LABOR after 08:30 Friday.**

## 3. Read cap — no rotation
`read_cap_check.py --agent LABOR`: STATUS **55%** of budget, LESSONS **68%** — below the 75% rotate tier. The dated 10/2 re-trigger is discharged (whichever-first) and its CATALYSTS row pruned. Charter 52,961 B is out of perimeter (rule 20).

## 4. Inbox — census 2 items, not 3 (`inbox_census.py`: top-level 2 · WALTER/ 0), both drained + logged in `board_log.tsv`
- **WALTER WQ-295 R3:** all 9 phrases ADOPTED + `Challenger layoffs`, `jobs report shutdown`, `Florida jobless claims jump` ADOPTED; `jobless claims rise` DECLINED (1 false hit). Verdict packet `PROME/inbox/2026-10-01_from-LABOR_WQ-295-R3-watch-for-verdicts.md` (`5b7d9e59e`) — **ASK: land the 12 in `newsweep_config.py`.**
- **REGINALD 9/29 (JOLTS openings missed consensus):** (a) adopted — openings 7,079K (−256K) now a no-band level row beside NET on STATUS; (b) whether openings earn a band is PARKED to a self-directed C2 by 10/9 (not decided in a scoped spawn).

## 5. Also done
10/1 cards → `docket/graded/`; **10/8 claims card frozen** (both counters at 3 of 4: a ≤199K print and CC <1,750K take the score to 26/75); CATALYSTS re-docketed (Challenger Oct report Thu 11/5 05:30 EST per Challenger's calendar); KB-LAB-200/201; PUBLISHED.tsv +3; NEXUS brief re-pinned to STATUS HEAD `10e94b5b2`.

**SKIPPED / PARTIAL controls (named, per the skipped-control rule):** ① B0 `git pull` — not run: the tree carries other desks' uncommitted work. ② B3 `LESSONS.md` — headers only, not read whole. ③ C5 promotion scan — not run. ④ Consumer-check 🔴 hits on `NEXUS/STATUS.md:20` (CC 1,719K) not separately packeted — NEXUS reads my re-pinned brief; the other hits are dated research/history rows. ⑤ **Push deferred** — LABOR's spawn card step 3 (Will-ruled 2026-07-31): a PROME-spawned LABOR commits, doesn't push; the commits go out with PROME's push. ⑥ The 10/8 card and Amendment 2 have had no independent reader.

## COMPLETION — LABOR — 2026-10-01
STATUS: ✅ DONE (closeout controls PARTIAL — see SKIPPED ①–⑥)
CHANGED: AGENTS/LABOR/{STATUS.md, NEXUS_BRIEF.md, board_log.tsv, docket/CATALYSTS.tsv, docket/GRADING_CARD_20261002_NFP.md, docket/GRADING_CARD_20261008_claims.md (new), docket/graded/GRADING_CARD_20261001_{claims,Challenger}.md (moved+graded), inbox→processed ×2, workbook/{KB,PREDICTIONS,PUBLISHED}.tsv, workbook/PREDICTIONS_SCOREBOARD.md}; AGENTS/CARL/inbox/2026-10-01_from-LABOR_…; PROME/inbox/2026-10-01_from-LABOR_WQ-295-R3-…
RESULT: Claims 197,000 / MA 200,000 / CC 1,701,000 (DOL 10/1) → band B, v13 + v7 at 3 of 4; Challenger Sep 43,281, AI 9.15% → v5 holds 4; score 28/75 unchanged. LAB-03 ❌ at as-made 65% (Brier 0.4225; book mean 0.348, n=13). 10/2 NFP armed: kill = Sep NFP ≥ max(150, 300 − revised Jul+Aug) K, i.e. +150K unless back months revise down >33K; consensus ~+90K [2ND].
GAPS: Push deferred to PROME's push (LABOR spawn rule). B0 pull, full LESSONS read, C5 promotion scan skipped. No independent read of the 10/8 card or Amendment 2.
WILL_NEEDS: None.
FOLLOW-UP: Re-spawn LABOR after 08:30 Fri 10/2 to grade NFP. PROME: land 12 WATCH_FOR phrases (packet 5b7d9e59e). LABOR self-directed C2 by 10/9: JOLTS-openings band question + v11 letter scope (both PARKED).
