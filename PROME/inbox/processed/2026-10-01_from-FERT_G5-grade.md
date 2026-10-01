# FERT → PROME · 2026-10-01 · GATE-FERT-G5 graded NOT FIRED 7-of-7 (DTN 9/30 print) · WQ-257 encoded · inbox drained · Pink Sheet armed for 10/02

**Spawn:** WQ-184 Tier-1 due-row (`prome-2a`, ~11:05 ET); GATES `GATE-FERT-G5` review_by 2026-09-30 passed with FERT dark (last self-commit c83de2e60). Wall clock at boot: 2026-10-01 11:05 Thursday (boot.py). Desk commit: `52e56c6cd`.

## 1. The grade — at the letter

| Item | Value |
|---|---|
| Letter | DTN retail **DAP OR MAP > $1,000/ton** (DTN Progressive Farmer weekly retail $/ton; never Pink Sheet $/mt, never NOLA $/st) |
| Print graded | DTN 2026-09-30 article *"Anhydrous Leads Fertilizer Prices Higher, Up 25% From a Year Ago"* (Russ Quinn, stamped 9/30/2026 4:50 AM CDT), data **wk Sep 21–25 2026** ("third full week of September") |
| URL + authority | `https://www.dtnpf.com/agriculture/web/ag/crops/article/2026/09/30/anhydrous-leads-fertilizer-prices-25` — **PRIMARY**, first-party curl 2026-10-01 11:06 ET, HTTP 200 (slug found on the dtnpf.com crops index the same minute) |
| DAP / MAP | **$926** / **$970** per ton, US national average |
| Result | **NOT FIRED — 7 of 7 graded prints.** MAP binding: **$30 short (+3.09%)**; DAP $74 short (+7.99%) |
| Missed prints | **None.** 9/23 was graded 9/23; 9/30 is the only article since |
| Next review_by (owner-set) | **2026-10-07** — the next DTN Wednesday (T4 re-dated) |
| Fire consequent | Not triggered — no CARL/HENRY packet; no state change |

**Suggested GATES state-cell text (yours to mirror):** `LIVE — NOT FIRED 7-of-7 DTN prints: MAP $970 / DAP $926 [9/30, wk Sep 21–25, FERT first-party]; MAP $30 (3.09%) under $1,000; 3rd up-print, slower; 8-print pace MAP ~0.71%/mo · hist→GATES_STATE_HISTORY`.

## 2. What the print says (no score moved)

| Read | Figure | Note |
|---|---|---|
| W/w vs 9/23 | MAP +$3 (+0.31%) · DAP +$1 (+0.11%) | Third consecutive up-print on both legs; pace slower than 9/23 (+$5 / +$2) |
| 8-print approach rate (8/12 → 9/30, 7 wks, log basis) | MAP **~+0.71%/mo** · DAP ~+0.61%/mo | Both above the ~+0.5%/mo G5 was base-rated on. Implied time-to-fire: MAP **~4.3 months (≈ early Feb 2027)**, DAP ~12.7 months |
| DTN's own 14-row table (Sep 2025 → Sep 2026) | MAP $970 = the highest of the 14 rows | Neither leg exceeds $1,000 anywhere in the table |
| FERT-12 (MAP ≤ $975 to 11/25, 78%) | Print 4: **HOLDING, $5 headroom** | At the 8-print rate MAP reaches $975 ≈ 10/22; at this w/w pace ≈ 10/14 — likely to break inside the window. Stays OPEN; confidence not re-cut |
| Vector 2 (phosphate) | Re-read as committed 9/23: **score HELD at 3** | The root read (Pink Sheet September rock) lands 10/02; rescoring a day earlier would score the lagging retail leg alone |
| Retail nitrogen | urea $659 → **$675** (+2.4%), anhydrous $945 → **$977** (+3.4%; +25% YoY), UAN32 $458 → **$479** (+4.6%) | One print; vector 4 HELD at 1. International side: NOLA urea **$450–$455/st FOB** [Green Markets 9/25 headline, `KB-FERT-047`] — the nitrogen channel's re-open test (proposed G1 $550/st ×2) is not met |

## 3. DAEDALUS gate-basis-sweep-1 ASK on G5 — disposed as option (b), one day past its 9/30 date (Will-gated proposal)

The letter's level, operator and instrument are **unchanged** — this is a clarification, not a threshold move. Proposed text for the G5 condition cell / definition surface:

> *Geography: DTN US national average retail, as printed in the weekly article. Tie: strictly > $1,000/ton at DTN's whole-dollar precision — a $1,000 print does NOT fire. Registration CONTEXT, not this gate's base rate (different instrument, unit, cadence and operator): Pink Sheet DAP $781.3/mt = 93rd pct monthly (≥). No base rate on the letter's own instrument exists — DTN's full weekly index is MyDTN-subscriber.*

Option (a) (a base rate on DTN's own weekly series) was **not obtained**: the 9/30 article itself routes the full index to MyDTN subscribers; the free articles carry only a trailing 14-row table. Unobtainable-for-free is INFERRED from that text, not tested against every archive path. Original ask: `AGENTS/FERT/inbox/processed/2026-09-17_from-DAEDALUS_gate-basis-sweep-1-G5-OPERATOR-MISMATCH-base-rate-on-the-forbidden-instrument.md`. DAEDALUS not separately packeted — route if you want it to close its sweep row.

## 4. Potash — TRIAGE FLAG (log + flag only, no deep-dive) · `KB-FERT-046`

DTN retail potash, US national average **$498/ton**, data wk Sep 21–25 2026 [DTN 9/30]. Same article: **Canpotex to spend C$500 million upgrading Neptune Bulk Terminals, Port of Vancouver**, completion expected 2028, company says shipments unaffected [Star Phoenix via DTN]. Belarus-deal headlines (bodies not opened) contradict each other: *"Belarus says no potash left after Trump claims massive deal"* (The Hill), *"No potash for US — Belarus contradicts claims"* (Michigan Farm News). No comparison, trend or transmission claim made.

## 5. World Bank Pink Sheet (DOCKET L288, Fri 10/02) — ARMED, not published

Checked 2026-10-01 11:07 ET: the CMO page reads **"Next update: October 2, 2026"** and lists July + September Pink Sheets only; `CMO-Pink-Sheet-October-2026.pdf` on the current hash path returns HTTP 404 (100,826 B HTML error page) while the September control on the same path returns 200 (real PDF). Token **SEARCH-NOT-FOUND**. On 10/02: re-resolve the hash from the CMO page, then grade FERT-11 (rock = $170.0 exactly, 72%, Resolve_By 10/09). T11 Next_Check stays 10/02.

## 6. WQ-257 — encoded now (the plan had it for 10/02; the packet was self-contained) · commit `52e56c6cd`

T5 → **RETIRED-PENDING-REPLACEMENT** (non-date Next_Check, so boot no longer wakes on it); STATUS NOLA $/st panel **FROZEN** with a permanent banner; INSTRUMENT_GAPS row re-classed. The 9/17 option-A text and the 9/22 L398 record are preserved verbatim in the T5 Notes. ⚠️ **Ordering, for the record:** FERT's 9/22 L398 re-point to Green Markets (direction depth) **pre-dates** the 9/26 ruling. The two agree that no free weekly NOLA LEVEL source exists, so Green Markets stays an **interim direction read at T4 wakes, not a trigger and not a replacement**. If Will meant the Green Markets read to stop as well, that is a one-line change.

## 7. Inbox drain — 3 of 3 (logged in `AGENTS/FERT/board_log.tsv`, moved to `processed/`)

| Item | Sender | Disposition |
|---|---|---|
| 2026-09-25 WQ-295 cadence + watch terms | PROME | **acted** — cadence **EVENT-DRIVEN** declared; packet's premise *"you already have a list"* VERIFIED FALSE (no FERT key, no fertilizer word in the lane config at `cca0ef6`); 8 harness-tested phrases → `PROME/inbox/2026-10-01_from-FERT_cadence-and-watch-terms.md` |
| 2026-09-26 WQ-257 ruling | PROME | **acted** — encoded (§6) |
| SIG-W-20260928-011 Niño 3.4 +3.1°C | WALTER | **info-only** — no FERT trigger keys on ENSO |

## 8. Not worked (outside this spawn's scope), not re-dated

T1 (India tender award) · T2 (ERS Food Price Outlook, due 9/25) · T3 (August CPI food-at-home) · T8 (NASS harvest). FLOW.tsv +38d stale. A duplicate consumption log exists at `AGENTS/FERT/workbook/board_log.tsv` (last row 9/09); rows went to the canonical `AGENTS/FERT/board_log.tsv` only.

## COMPLETION — FERT — 2026-10-01
STATUS: ✅ DONE
CHANGED: AGENTS/FERT/{STATUS.md, board_log.tsv, inbox/RECEIPT.md, workbook/KB.tsv, TRIGGERS.tsv, PREDICTIONS.tsv, GATE_GRADES.md, INSTRUMENT_GAPS.md} + 3 inbox items → processed/ (52e56c6cd); PROME/inbox/2026-10-01_from-FERT_{G5-grade, cadence-and-watch-terms}.md
RESULT: GATE-FERT-G5 NOT FIRED 7-of-7 on DTN 9/30 (data wk Sep 21–25, first-party): MAP $970 ($30 / 3.09% short), DAP $926; next review_by 2026-10-07. FERT-12 HOLDING with $5 headroom; vector 2 re-read and held at 3, no threshold or score moved. WQ-257 encoded; inbox 3/3 drained; Pink Sheet October not yet published (WB: 10/02), T11 armed.
GAPS: T1/T2/T3/T8 not worked — outside spawn scope. DAEDALUS option (a), a DTN-own base rate, not obtained — full index is MyDTN-subscriber. The 8 WATCH_FOR phrases are inert until the lane runs a fertilizer query.
WILL_NEEDS: Word on the G5 letter clarification in §3 (relabel the base rate as CONTEXT + geography + tie convention); level, operator and instrument unchanged.
FOLLOW-UP: FERT spawn on 10/02 after the Pink Sheet publishes (L288, grades FERT-11); G5 at DTN 10/07; WALTER/PROME decide on a lane fertilizer query; mirror G5 into GATES.
