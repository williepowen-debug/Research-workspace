G5 NOT FIRED: DTN 11/11 print, MAP $991 / DAP $950 per ton, $9 under the strictly-greater $1,000 line; next review_by 2026-11-18.

# FERT → PROME: G:GATE-FERT-G5 graded 13 of 13 NOT FIRED · T1 India no tender · rotation done

**From:** FERT (Claude Code, Opus 5.5; session UNKNOWN to the desk) · **Date:** 2026-11-11 · **Task:** prome-2b due-row wake, WQ-184 · **Commit:** `d2afda9fdf` (AGENTS/FERT/ only)

| Row key | Result |
|---|---|
| **G:GATE-FERT-G5** (review_by 2026-11-11) | **NOT FIRED, 13 of 13 graded prints.** DTN Progressive Farmer, US national average retail, $/ton, data week Nov 2–6 2026: **MAP $991, DAP $950**. MAP binding leg, **$9 (0.91%) under**; DAP $50 under. PRIMARY, first-party curl of dtnpf.com `.../crops/article/2026/11/11/retail-fertilizer-prices-mixed-first` (JSON-LD datePublished 2026-11-11T13:44Z; posted ~3 h later than recent weeks, found by a 5-minute index poll), graded 09:31 ET on review_by. `KB-FERT-141`, `workbook/GATE_GRADES.md` row 11/11/26 |
| G5 suggested state cell | `LIVE — NOT FIRED 13-of-13 DTN prints: MAP $991 / DAP $950 [data wk Nov 2–6, print 11/11, FERT KB-FERT-141]; MAP $9 (0.91%) under $1,000 (strictly greater)` |
| **G5 next review_by** | **2026-11-18** (next DTN Wednesday; owner-set, PROME records). ⚠️ The 11/25 print falls in Thanksgiving week: check that it publishes |
| G5 pace (FERT arithmetic, 14 prints) | MAP +$4 (ninth straight rise), DAP +$9 (largest DAP weekly step in the series). Fire needs $1,001 (+$10): first firing print ≈ **12/16** at the mean step (+$2.46/wk), **12/02** at the last two steps (+$4/wk), **11/25** at the fastest step seen (+$5). FERT-13 (55%, MAP > $1,000 by 12/31) unchanged |
| **T1, India tender check** (STATUS-listed for 11/11) | **No new India urea import tender found.** IPL's own tender page (primary, IPL only) still lists IPL/UREA/2026-27/02 (9/23, closed 10/07) as its latest. AFC weekly w/e 06.11 (own site, published 11/11): India "delays its anticipated tender", which could slip "by several weeks"; China prilled $340–350/mt FOB. ⚠️ Absence of an NFL or RCF tender rests on searches and homepages, not their full portals. G2 still has no award to grade; the nitrogen channel stays DEAD. `KB-FERT-139`; `KB-FERT-126` (the ~2.5 Mt, L1 $370–375 expectation) SUPERSEDED. T1 → **2026-11-18** |
| **D:L997** (FERT-15, resolve 2027-01-08) | No bids yet. VOID if no bids by 12/31; nothing to register |
| **D:L579** (11/15 TRADE / EXIT re-look) | Its two pending inputs are now in: the DTN 11/11 read (above) and the India read (above). Row date unchanged |
| Potash (triage depth, Will 2026-08-18) | FLAG: DTN retail potash $504/ton [wk Nov 2–6]; AFC w/e 06.11 Brazil CFR granular MOP $350–375/mt, Southeast Asia CFR standard MOP $370–415/mt, Southeast Asia CFR granular MOP $425–435/mt. `KB-FERT-140`. No comparison, no deep-dive |
| Read-cap rotation | TRIGGERS.tsv 88% → **61%** of budget, STATUS.md 78% → **70%** (under the stop line; `read_cap_check` rotation_due=0). Text moved verbatim to `AGENTS/FERT/archive/*_2026-11-11*` |
| Inbox | Empty at boot (every sender, WALTER lane included); nothing to drain, no board_log rows |
| Tradeability | No card. G5 is watch-only with no capital path, and the print is not a fire. The tradeability question rides the 11/15 TRADE re-look (D:L579) |

**Unchanged:** every trade, card, gate letter, band, threshold, charter line and capital path. No spend, no external send.

**ACTION:** PROME records the G5 grade and the review_by date 2026-11-18 in GATES row G:GATE-FERT-G5. Nothing for Will.

## COMPLETION — FERT — 2026-11-11
STATUS: ✅ DONE
CHANGED: AGENTS/FERT/STATUS.md, workbook/TRIGGERS.tsv, workbook/GATE_GRADES.md, workbook/KB.tsv, data/RELATIVE_NUTRIENTS.tsv, archive/STATUS_whatchanged_2026-11-11_ROTATED.md, archive/TRIGGERS_notes_rotated_2026-11-11.md (commit d2afda9fdf); this packet
RESULT: G5 graded at review_by on the first-party DTN 11/11 print: MAP $991, DAP $950, NOT FIRED 13 of 13, $9 short. India has no new urea tender (IPL page primary, AFC says delayed); T1 and T4 re-dated 11/18. KB-FERT-139..141 added; STATUS rotated 78% → 70% and TRIGGERS 88% → 61% of the read budget.
GAPS: The NFL and RCF tender portals were not searched in full (homepages only). The session ID is not exposed to the desk.
WILL_NEEDS: None.
FOLLOW-UP: Set G5 review_by to 2026-11-18. D:L579 re-look on 11/15. FERT holds its window open for PROME's closeout ask.
