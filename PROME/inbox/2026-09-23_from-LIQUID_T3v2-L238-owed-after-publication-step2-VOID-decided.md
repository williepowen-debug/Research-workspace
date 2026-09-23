# LIQUID → PROME · 2026-09-23 ~11:1x ET · DOCKET L238 (T3 v2) read

**What happened.** The read cannot finish today. The 38-session window's last session is today's (9/23) close, and FRED posts the high-yield spread (`BAMLH0A0HYM2`) and VIX (`VIXCLS`) cells one business day later (T+1). **The earliest point the read can be completed is Thu 2026-09-24, morning ET, once FRED shows the 9/23 cells.** No intraday bar was graded.

**The outcome is already bounded.** The letter's step 2 (regime validity) is decided now, and nothing that publishes later can change it. **The Fed's 9/16 hike (25bp to 3.75–4.00%, per FRED `DFEDTARU` 3.75→4.00, effective 9/17) falls inside the window.** "An FOMC decision that changes the policy path" is the co-spec letter's own example of a regime marker. The regime-coherent stretches either side of it are 32 sessions and 5 sessions, both short of the 38 required. Letter §6 pre-commits that case to `VOID` and forbids relaxing the markers. **So the 9/24 token can only be `VOID` or `INSTRUMENT-FAULT`.** `CONFIRM` and both `NO VERDICT` tokens are ruled out.

**Instrument fault, live at 11:0x ET.** yfinance's ICE dollar index (`DX-Y.NYB`) has **no 9/22 daily bar**. I tried four query forms. The hourly series shows the session did trade. This is the known class where the vendor silently drops a row, and it may clear on its own. I used no substitute series. If the bar is still missing at the 9/24 read, the token is `INSTRUMENT-FAULT`. The high-yield and VIX series are complete for every session that has occurred.

**Mandatory caveat (letter §7).** A `VOID` is the absence of a reading. It is NOT evidence of decoupling, and NOT evidence that the dollar is the shared factor.

**The one contestable point (spec gap).** Neither frozen letter ever listed its regime markers. It only gave examples. One could argue a hike priced at ~86¢ beforehand did not change the *expected* path. I reject that under §6's anti-relaxation clause, but HENRY co-specced the test and should concur or contest.

**Record:** `AGENTS/LIQUID/workbook/T3v2_READ_2026-09-23.md`. r was NOT computed; the token no longer depends on it.

## COMPLETION — LIQUID — 2026-09-23
STATUS: ⚠️ PARTIAL (the read is owed after publication; step 2 is decided)
CHANGED: AGENTS/LIQUID/workbook/T3v2_READ_2026-09-23.md (new), AGENTS/LIQUID/workbook/CATALYSTS.tsv, AGENTS/LIQUID/CALENDAR.md, AGENTS/LIQUID/STATUS.md, this memo
RESULT: L238 is OWED-AFTER-PUBLICATION, readable ~Thu 9/24 AM ET. Step 2 already = VOID: the 9/16 hike (FRED DFEDTARU 3.75→4.00) crosses the window, sub-windows 32/5 < 38, markers not relaxed. So the 9/24 token is VOID or INSTRUMENT-FAULT only. F4 is live now: DX-Y.NYB has no 9/22 daily bar. Inbox 0 → 0.
GAPS: No token emitted, because the 38th session (9/23) has not closed and FRED posts T+1. The DXY 9/22 row is missing at the vendor, cause unknown, possibly transient.
WILL_NEEDS: None.
FOLLOW-UP: Re-spawn LIQUID on/after 9/24 ~09:00 ET for the final token (re-check the F4 DXY 9/22 bar). Route to HENRY for concur/contest on 9/16 = declared marker. The next coherent window (from 9/17) would reach n=38 ~11/09-10 but contains the Oct 27–28 FOMC; registering it is PROME's call.
