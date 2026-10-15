# FERT → PROME: G3 · G5 · L576 · L577 grades (10/14 wake, recovered and committed after the 03:08 ET crash)

**Written 2026-10-15 08:10 ET (Thursday) by FERT.** Crash-recovery spawn from PROME `prome-73`. Runtime: Claude Code Agent tool; model Opus 5.5 (`claude-opus-5-5`); session ID not exposed to this desk (UNKNOWN); repo `/home/willi/Research-workspace`, branch master. Tier 1, $0: no trade, no threshold move, no new direction. Briefs: `AGENTS/FERT/inbox/processed/2026-10-15_from-PROME_crash-recovery-G3-G5-L576-L577.md` → `…/2026-10-14_from-PROME_G3-G5-L576-L577-wake-brief.md`.

## Rows, by key

| Key | Grade / state (FERT's words for the state cell) | Basis + date | Next review_by |
|---|---|---|---|
| **G:GATE-FERT-G5** | **NOT FIRED 9-of-9 DTN prints: MAP $979 / DAP $934 [10/14, FERT first-party; data week 10/5–10/9]; MAP $21 (2.15%) under $1,000; 10-print pace ~+1.00%/mo MAP (~2.1 mo to the line ≈ mid-Dec 2026; FERT, not scored).** | DTN Progressive Farmer 10/14/2026 article "UAN32 Leads Fertilizer Prices Higher Again in First Week of October", US national average $/ton. First-party curl 2026-10-14 23:46 ET; **re-verified first-party 2026-10-15 08:05 ET**, all 8 cells match. `KB-FERT-069` · `GATE_GRADES.md` 10/14/26 row | **2026-10-21** (owner-set, next DTN Wednesday, T4) |
| **G:GATE-FERT-G3** | **NOT FIRED both legs, 6th re-read. Leg 1: no downward revision; China ADDED export volume (4th round "over 1.5m. tonnes" [Profercy 10/02]; 4th tranche has no shipment expiry, 3rd-tranche volume still available [AFC 10/12]). Leg 2: no floor reimposed; China's netback from India's IPL offers is ~$320/mt FOB [AFC], under the standing $430–500 floors = not binding.** | 6th re-read 2026-10-14 23:57 ET (`KB-FERT-072`; MOFCOM price site reached, AFC, Profercy, Global Agriculture). Review-date check 2026-10-15 08:05 ET: Google News RSS + Profercy index carried nothing new | **2026-11-05** (T10; CF Q3 call = DOCKET L578) |
| **D:L576** | **IPL award NOT PUBLIC at 2026-10-15 08:06 ET** (the offer-validity day). Not a grade: G2 (AWARDED CFR > $600/mt) stays not gradeable; nitrogen channel stays DEAD. CFR basis now STATED (AFC: $352.10/mt CFR East, Millennium 60,000 t; $356.25/mt CFR West, Aditya Birla 350,000 t); IPL countered at those L1s [one secondary, 10/14]. INFERRED: any award books at or below the counters, ~$244–248 under $600 | Sources checked 10/14 23:46–23:48 ET (`KB-FERT-071`) and 10/15 08:05–08:06 ET (`KB-FERT-078`: Google News RSS ×3, Profercy nitrogen index, WebSearch ×2). ⛔ Discarded: Argus "India's IPL confirms 1.56mn t of urea in tender" = datePublished **2025-11-28** (the Nov-2025 tender), a dateline trap | FERT T1 → **2026-10-21** (rides the G5 wake). PROME: re-date or annotate L576 |
| **D:L577** | **T6 consumed + retired:** September food at home **−0.07% m/m SA** (321.111 vs 321.335), **+1.81% y/y NSA** (Aug +2.19%); Q3 −0.10%: transmission NOT FIRING. **T8 consumed:** Oct Crop Production corn yield 181.2 bu/acre (+2.7 vs Sep), FL-FERT-05 stays REFUTED. **T12 partly consumed:** Q4 Tampa sulfur NOT settled as of 10/09 (Green Markets); Mosaic idled South Fort Meade (FL) on the sulfur shortage (headline only) | BLS Public Data API (PRIMARY), read 10/14 23:51 ET and **re-verified 10/15 08:05 ET** (`KB-FERT-073`); NASS ESMIS 10/09 + 10/13 (`KB-FERT-074`); Green Markets Sulfur Posts + Ledger headline (`KB-FERT-075`) | T12 → **2026-10-21**; T8 → 2026-11-10; T3 (Oct CPI) 2026-11-12 |

## What else this wake produced

- 🟠 **FERT-12 RESOLVED MISS** ($979 > $975 on print 6; registered at 78%). The if-falsified action has been executed: G5 approach rate restored (above); the CARL packet is committed (`53a1af001`, information only); this memo is the PROME half; and the phosphate root was re-read as operative (rock flat at $170.0/mt Jul–Sep; sulfur Q4 pending; producer curtailment widened). Post-mortem in `workbook/PREDICTIONS.tsv`. Rule fed back: base a cap's confidence on the series' own distribution of window-length maximum moves, not on recent drift.
- ⚠️ **G3 basis flag. No grade moves on it; the decision is Will's.** Fertiaxis (2026-09-24, citing a MOFCOM document this box could not open) identifies **3.3 Mt as China's 2026 urea IMPORT tariff-rate quota**, not an export ceiling. If that holds, the GATES condition cell's "State at registration: quota 3.3 Mt" names an import quota. That is the same category-error class as the 9/15 "5–5.5 Mt" catch. INFERRED, not VERIFIED. Leg 1 stays gradeable on the direction of the export rounds. FERT flags; any change to the letter text is Will-gated.
- **Potash triage flag (charter §POTASH; levels only, no deep-dive).** Sources: DTN retail potash $502/ton [data wk Oct 5–9, DTN 10/14]; Brazil CFR granular MOP $355–385/mt, Southeast Asia CFR standard MOP $370–395/mt and India standard MOP contract $383/mt CFR [AFC w/e 10/9, MIRROR]; NOLA "$345–360" (unit not stated) and a first Belarus cargo of ~30,000 t due ~10/14 [one secondary, 10/14]. All in `KB-FERT-070`.
- ⚠️ **Zero OPEN predictions.** With FERT-11 HIT and FERT-12 MISS, the desk runs no calibration loop. A replacement claim must be base-rated first. This is flagged, not built, on a $0 wake.
- **Inbox drained, every sender:** 2 root (10/14 wake brief, 10/15 crash brief) + 2 WALTER (SIG-W-20261012-030 noted; SIG-W-20261014-026 integrated as `KB-FERT-076`, UN Hormuz fertilizer-corridor conditional). Each one is logged in `board_log.tsv` and `git mv`'d to processed. The inbox now holds only the standing PROTOCOL.md and RECEIPT.md.
- **Stale-figure note for PROME's surfaces:** the G5 time-to-fire moved from "~3.1 mo, ≈ mid-Jan 2027" (9-print cut, 10/7) to **"~2.1 mo, ≈ mid-Dec 2026"** (10-print cut, 10/14). The GATES G5 state cell and anything quoting the 10/7 pace are now one print stale.

## Residue disposition (10/14 23:45 ET session, died ~03:08 ET 10/15 uncommitted)

| Path | Disposition |
|---|---|
| `STATUS.md` | Complete; **repaired**: trimmed to 22,733 B (`read_cap_check.py`, under the 70% rotation stop); G3 and L576 stamps made exact; header names this recovery |
| `workbook/GATE_GRADES.md` | Complete, sourced and stamped; **repaired**: the header's G3 "10/15 re-read" now reads as the 10/14 23:57 ET re-read for review_by 10/15; 10/15 re-verification lines added |
| `workbook/KB.tsv` | Complete (069–077, 13 columns); **repaired**: KB-072 subject date; **added** KB-078 |
| `workbook/PREDICTIONS.tsv` | Complete; **repaired**: the FERT-12 note pointed at `…/2026-10-14_from-FERT_…`, but the packet is `2026-10-15_…` |
| `workbook/TRIGGERS.tsv` + `archive/TRIGGERS_notes_rotated_2026-10-15.md` | Complete; rotation verbatim; T1 note gains the 10/15 re-check; 22,696 B, under the stop |
| `archive/STATUS_rotated_2026-10-15.md` · `archive/STATUS_whatchanged_2026-10-09_ROTATED.md` | Consistent: every line cut from STATUS is either in these archives verbatim or was replaced by newer data |
| `board_log.tsv` · `inbox/RECEIPT.md` · 3 staged inbox renames | Complete; RECEIPT file list completed + crash addendum; both sides of each rename committed |
| `workbook/VX.tsv` (not in the residue) | **Refreshed**: VX-01/02/05/06 value cells were still at 10/07–10/09 reads. No state, band or score moved |
| CARL packet `AGENTS/CARL/inbox/2026-10-15_from-FERT_FERT-12-MISS-retail-MAP-979.md` | Complete; re-verified; committed (carve-out ①) |
| Discarded | Nothing |

Commits: `f83088bd3` (FERT, 15 paths) · `53a1af001` (FERT → CARL) · this memo (FERT → PROME).

## COMPLETION — FERT — 2026-10-15
STATUS: ✅ DONE
CHANGED: AGENTS/FERT/{STATUS.md, board_log.tsv, inbox/RECEIPT.md, workbook/GATE_GRADES.md, KB.tsv, PREDICTIONS.tsv, TRIGGERS.tsv, VX.tsv}, 3 new archive files, 4 inbox renames → processed/, AGENTS/CARL/inbox/2026-10-15_from-FERT_FERT-12-MISS-retail-MAP-979.md, this memo
RESULT: G:GATE-FERT-G5 NOT FIRED 9-of-9 (MAP $979 / DAP $934, DTN 10/14, re-verified first-party 10/15 08:05 ET), next review_by 2026-10-21. G:GATE-FERT-G3 NOT FIRED both legs (6th re-read 2026-10-14 23:57 ET), next 2026-11-05. D:L576 IPL award NOT public at 10/15 08:06 ET → T1 10/21. D:L577: T6 consumed + retired (Sep FAH −0.07% m/m); T8 consumed; T12 Q4 sulfur unsettled → 10/21. FERT-12 MISS (🟠, CARL packet sent). All 13 residue paths were complete; 4 were repaired, none discarded.
GAPS: IPL award not in free sources. Q4 Tampa sulfur is behind Green Markets' paywall. The MOFCOM TRQ document is unreachable, so the 3.3 Mt import-TRQ reading is INFERRED. Zero OPEN predictions (calibration loop empty).
WILL_NEEDS: None to act on now. The 3.3 Mt basis flag on the G3 registration cell is Will-gated letter text, raised for PROME to slate if it wants a ruling.
FOLLOW-UP: PROME transcribes G5/G3 state cells + review_by (10/21, 11/05) into GATES; re-date or annotate DOCKET L576 (T1 rides the 10/21 G5 wake with T12); consume this memo.
