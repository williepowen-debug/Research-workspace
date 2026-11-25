# FERT to PROME: D:L1268 — GATE-FERT-G5 FIRED on the DTN 11/25 print (MAP $1,004); FERT-13 HIT; routed CARL + HENRY; inbox drained; Section 301 fertilizer lines read

**Written:** 2026-11-25 13:44 ET (by `date`). FERT, due-row wake launched by PROME prome-77 at about 13:26 ET. Runtime: Claude Code, model Opus 5.5, Agent-tool spawn. A network cut at about 13:30 to 13:36 ET interrupted the session; it resumed in the same context, and **the DTN article was re-read at the source after the cut** (13:37 ET, HTTP 200, same figures). Boot reads used the bounded reader, each to `eof: true`: root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 3 · `AGENTS/FERT/CLAUDE.md` 4 · `AGENTS/FERT/STATUS.md` 5. `boot.py` REVIEW (T4 due; 4 build baselines stale, unchanged). The corrections check had 1 BLOCK (COR-20261125-15); it is now receipted NO-OP and the check reads rc 0.

## 1. G5 grade (own written rule; no level, operator, instrument or consequence changed)

**Source:** dtnpf.com `/agriculture/web/ag/crops/article/2026/11/25/fertilizer-prices-remain-mixed-5-8`, "Fertilizer Prices Remain Mixed, With 5 of 8 Nutrients Up" (Russ Quinn). JSON-LD datePublished **2026-11-25T16:50Z** (byline 10:50 AM CST, later than the 11/18 12:38Z and 11/11 13:44Z posts). First-party curl at 13:25 ET and again at 13:37 ET, both HTTP 200. The article is listed on the crops index. **Data week Nov 16–20 2026** ("third week of November").

| DTN retail, US national average, $/ton | 11/25 print | change vs 11/18 print (wk Nov 9–13; FERT arithmetic) |
|---|---|---|
| DAP | 948 | +1 |
| **MAP** | **1,004** | **+9** |
| Potash (triage depth) | 508 | +4 |
| Urea | 657 | 0 |
| 10-34-0 | 706 | +2 |
| Anhydrous | 1,011 | +14 |
| UAN28 | 427 | 0 |
| UAN32 | 484 | +1 |

DTN's prose compares to a month ago: five higher, three lower, none by 5% or more. DTN: *"MAP crossed the $1,000/ton level for the first time since the fourth week of September 2022, when its average price was $1,005/ton."*

**Grade: FIRED.** The test is strictly greater than $1,000 at DTN's whole-dollar precision, on the US national average as printed. $1,004 > $1,000, so MAP fires; it is $4 (0.40%) over. DAP is $948, $52 under. This is print 15 of 15 graded and the first fire. MAP's +$9 is the largest weekly MAP step in 16 prints (prior max +$5), its eleventh straight rise. My 00:28 ET forward view gave about 15% to a fire on this print. Adjudication record: `AGENTS/FERT/workbook/GATE_GRADES.md` (fire paragraph + row); `KB-FERT-148`.

**GATES state line (record verbatim):**
`FIRED 2026-11-25 — DTN print 15 of 15 graded: MAP $1,004 / DAP $948 [data wk Nov 16–20, print 11/25, FERT KB-FERT-148]; MAP $4 (0.40%) over $1,000 (strictly greater), first fire; DAP $52 under. Watch-only: routed CARL + HENRY cc 11/25; no capital path, no automatic state change · hist→git`

**review_by:** `2026-12-02 (OWNER-SET 2026-11-25 at the fire: next DTN Wednesday, post-fire hold read; the letter has no hold clause, so a fall back below $1,000 does not un-fire it)`. DTN printed in Thanksgiving week, so the 12/02 Wednesday is expected on its normal schedule. If it is missing, grade the next print, by 12/09 at the latest.

**Route (GATES `consequence_on_fire`):** done. Packets authored and committed by FERT (carve-out ①): CARL `AGENTS/CARL/inbox/2026-11-25_from-FERT_G5-fired-retail-MAP-above-1000.md`, HENRY cc `AGENTS/HENRY/inbox/2026-11-25_from-FERT_cc-G5-fired-retail-MAP-above-1000.md`. Both say plainly that this is a lagging farm-input level and **not** evidence of transmission to food. International phosphate is flat: Pink Sheet Gulf DAP $803.1/mt in October, +0.3%. October food at home was beef- and snack-led, with cereals and bakery at 0.0, and ERS on 11/24 cited no inputs.

**What the fire moved on FERT's own surfaces, each by a written rule:** FERT-13 (55%, MAP > $1,000 by 12/31) **resolved HIT** on its early-resolution clause; Brier 0.203; scoreboard n=3, mean 0.296 (class C10). VX-FERT-02 value 995 → 1004, and its state ORANGE → **RED** by the row's own band (>1000). **The score is HELD at 3**: no written rule moves it on a G5 fire. T4 → 12/02. No gate, level, band text or kill rail changed. Potash is listed only.

**Disposition question (not urgent; FERT recommends no change now):** G5 has fired once and is watch-only. FERT will hold-read it weekly. Whether to retire it, keep it, or re-arm it at another level is Will's call (a threshold move). FERT is not proposing one today.

## 2. Inbox drain (whole inbox, every sender; `board_log.tsv`, 6 rows)

| Item | Disposition |
|---|---|
| ISHM 11/25 Deere fiscal Q4 | **acted**: FY2027 US and Canada large-ag +5 to +15%, tractor dealer stocks 31% vs 23% of trailing retail. Added as counterevidence to `combo:nutrient-cuts-by-crop-economics` (KB-FERT-133). No fertilizer figure in Deere's release. ISHM's "tariff recoveries nearly exhausted" is ISHM's inference; FERT has not checked it. No score. |
| WALTER 20261125-015 (correction of 006, 014) | **acted**: COR-20261125-15 receipted NO-OP (FERT carried none of the corrected claims). It prompted FERT's own notice read (§3). |
| WALTER 20261125-006, -014 | noted (superseded by 015 and §3) |
| WALTER 20261125-011, -020 | info-only (Deere superseded by ISHM's 8-K read; owner outcomes carry no fertilizer item) |
| WALTER 20261125-004 | already drained at the 00:20 ET session (acted, ERS) |

Census after: top-level holds only PROTOCOL.md and RECEIPT.md; WALTER/ 0 (`inbox_census.py`).

## 3. Section 301 (PROPOSED, not in force; comments to 2027-01-05, hearing from 2027-01-25): fertilizer lines

FERT read the USTR pre-publication notices itself: China, EU, India and Indonesia FRN PDFs, links from the USTR release page, HTTP 200, text extracted with pdfminer. Record: `KB-FERT-150`.

| Notice | Fertilizer and input lines FERT tracks | Treatment as proposed |
|---|---|---|
| **China** | **Every HTS Chapter 31 line**: 3101; 3102.10 urea, 3102.21 ammonium sulfate, 3102.29–3102.90 (AN, CAN, UAN, others); 3103 superphosphates and phosphatic; 3104.20 potassium chloride, 3104.30, 3104.90; 3105.10–3105.90 incl. 3105.30 DAP and 3105.40 MAP. **Inputs:** 2814.10/2814.20 ammonia, 2503.00 sulfur, 2510.10/2510.20 phosphate rock, 2809.20 phosphoric acid | **Annex A: "up to 10 percent"**, the lower tier (other Chinese goods: up to 20% net of the forced-labor 301 rate; alternative up to 40%). No Ex/Pharma/Aircraft marker appears beside these rows in the extracted text |
| EU, India, Indonesia | 3102.10 and the same lines | in each notice's single Annex, headed "**not covered** by the proposed action" |

**So:** yes, fertilizer lines are touched, for China only, and at the lower tier. **What FERT cannot establish today:** (1) the duty China-origin fertilizer pays now (the forced-labor 301 annex is unread; China's 12.5% is ZHAO's inference), so the step is not sized; (2) the Scope Limitations column cell by cell (PDF columns separate in extraction); (3) the Japan, Korea, Taiwan, Malaysia, Singapore, Vietnam and Thailand annexes (ZHAO and VULCAN report them set-identical; FERT did not re-read them); Switzerland, Cambodia and Bangladesh have been read by no desk; (4) US import volume of China-origin fertilizer (FERT's import baseline holds no China rows); (5) the Federal Register text. Materiality is probably small, because the large US fertilizer suppliers (Canada, Morocco, Russia, Trinidad, Gulf states) are outside the 14. **That is INFERRED, not measured.**

## 4. CF single-name item found in the DTN article, verified at the primary

Mosaic's 8-K exhibit 99.1 (dated 11/24, read at EDGAR with the fleet SEC client string) announces a **sale of the Faustina, Louisiana ammonia plant to CF Industries**. Total consideration is about $600M: about $360M cash at close, plus a 20-year, 200,000 t/yr ammonia offtake back to Mosaic "at producer economics". The existing offtake is extended to 2031. Close is expected in H1 2027, subject to regulatory approval. Capacity is not stated. Record: `KB-FERT-149`. Live prices (fetch.py, 13:38 ET): CF $117.65 (+0.78%), MOS $20.53 (+4.32%). Sent to TERRY with the G5 fire and §3 for a tradeability read; no card asked (`AGENTS/TERRY/inbox/2026-11-25_from-FERT_tradeability-G5-fire-faustina-301.md`). FERT's own view: nothing to trade in the crossing itself or in an undated proposal.

## 5. Forward view (unscored, Will 11/19)

| Call | Odds | Horizon | Would change my mind |
|---|---|---|---|
| MAP still above $1,000 at the next DTN print | about 85% (a fall of $4 or more would be the largest weekly MAP drop in 16 prints; the only drops so far were −$1) | 12/02 | a turn in Pink Sheet DAP or rock at the 12/02 edition; AFC reporting US retail resistance |
| DAP above $1,000 by 12/31 | about 2% (needs +$53; the largest DAP step is +$9) | 12/30 print | a Mosaic production cut beyond the named mines |
| T2 fires at the ERS 12/23 edition (2027 food-at-home revised up **citing inputs**) | about 5% (ERS's methods are statistical; no input citation in recent editions) | 12/23 | ERS naming fertilizer or energy in the summary text |
| FERT-16 (registered 40%): anhydrous > $1,050 by 12/31 | FERT's current view about 25% (needs +$39 in about 5 prints; recent steps +20, −4, −6, +14). Not re-marked | 12/30 print | Tampa December ammonia settling above November |

Main alternative to my read: the retail MAP run continues because North American dealers are re-pricing to a fall season that sold out (Mosaic Q4 sold out). DAP would then follow MAP up, and the gate's DAP leg would come into play in Q1 2027.

## 6. Commits (exact pathspecs; not pushed; PROME pushes)

Desk `13f4d0e5f3` · CARL `47a2aada28` · HENRY `d06f7802e4` · TERRY `ce2018b660` · this memo: its own commit (sha in the SendMessage receipt). Shared index held other desks' staged renames (MARCO). Every FERT commit was pathspec-scoped and verified to carry only its own paths. FERT did not pull, because the tree carries other desks' work.

## COMPLETION — FERT — 2026-11-25
STATUS: ✅ DONE
CHANGED: AGENTS/FERT STATUS, GATE_GRADES, KB (148–150; 131/133 combo; 144 superseded), VX-02, TRIGGERS T4, PREDICTIONS FERT-13 HIT, SCOREBOARD, RELATIVE_NUTRIENTS, board_log, corrections_receipts, RECEIPT, 6 inbox moves; packets CARL, HENRY, TERRY, this memo
RESULT: G5 FIRED on DTN 11/25 (wk Nov 16–20): MAP $1,004 > $1,000, DAP $948; first fire, print 15 of 15. FERT-13 HIT. Routed CARL + HENRY cc. review_by 12/02 (hold read). Section 301 China Annex A lists every fertilizer line plus ammonia, sulfur, rock and phosphoric acid at up to 10%, proposed; EU, India, Indonesia not covered. Mosaic is selling Faustina ammonia to CF (8-K 11/24).
GAPS: 301 step unsized (today's duty, China import volume, scope column, 10 notices unread); STATUS at 86% of read budget, rotation owed; 4 build baselines stale (unchanged); no pull (others' dirty tree)
WILL_NEEDS: None now. Optional later: retire, keep or re-arm G5 after its fire (a threshold move is his)
FOLLOW-UP: 12/02 DTN hold read + Pink Sheet + India; 12/03 China; 12/10 CPI; 12/16 re-look; 12/23 ERS; STATUS rotation next session
