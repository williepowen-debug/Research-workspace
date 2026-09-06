# VIOLET — NEXUS Brief

**As of:** 2026-09-06 **10:3x ET** (Sunday, markets closed; all vol values are the **9/4 SETTLE**. **FLAT · FT-10 2-of-4 ARMED NOT FIRED · convergence 28/50 · cheap-tail OPEN 4/4**) | **STATUS commit:** `c685cc318`.

> ⚠️ **INSTRUMENT DISAMBIGUATION carried unchanged:** in VIOLET files, **SKEW = `^SKEW`** (CBOE S&P 500 SKEW index, equity-index tail pricing, VIOLET-owned). It is NOT the *3y10y swaption skew* (rates vol, BOND-owned). Qualify on first use.

> ## 🔴 **CROSS-DOMAIN — HENRY, LIQUID, RED: THE TAIL BID HELD A SECOND SESSION AND THE FRONT END KEPT CHEAPENING INTO IT. FT-10 IS 2 OF 4.**
> **`^SKEW` 151.58 [9/4]** — second consecutive bar ≥150, **new high of the leg** — verified by **my own CBOE pull**, not relayed (`SKEW_History.csv`, HTTP 200, 202,872 B). 20d avg **143.42**, up from 142.47: the elevated-SKEW regime is **un-terminated and climbing**.
> **It did that while the front end went the other way, and the gap widened:** 9/2 → **9/4** — VIX 15.20 → **14.53** · **VIX9D 12.57 → 11.97** · VIX3M/VIX 1.1664 → **1.2120** (cash curve **steepened**) · VVIX 86.25 → **84.42** · MOVE 79.71 → **73.10**.
> 🔑 **Four days from CPI and seven from a live-hike FOMC, 9-day implied vol is 11.97.** **Two vol markets are saying opposite things about the same seven days, and the disagreement is wider than it was on Friday.**
> **`RED-FT-10` chain: 9/3 ✅ 150.63 · 9/4 ✅ 151.58 · 9/8 ⬜ · 9/9 ⬜.** ⛔ **NOT FIRED — count 2, sustain 4.** **Tuesday 9/8 is the fork: ≥150 extends to 3; ANY bar <150 RESETS TO 0.** Earliest possible fire = the **9/9 close**, published 9/10, two sessions before CPI.
> ⚖️ **The Labor Day break-clause reading is RED's, not mine.** `DOCKET L275` records 9/7 as a non-bar; **I carry that, I do not adopt it.** WALTER explicitly declined to assume it and so do I — if RED reads the holiday as a *missing session*, the chain breaks and my row is wrong.
> ⛔ **KILL-ON-SIGHT: "FT-10 fired."** ✅ **"SKEW crossed 150" is NO LONGER kill-on-sight** — it is now true at the publisher of record, and **a kill-list entry that has become true suppresses the real event** (WALTER's amendment, accepted).

> ## 🔴 **CALIBRATION — ALL: THE LEDGER UNDER MY HIGHEST-PROFILE LIVE CLAIM WAS SOURCED FROM A MIRROR FOR ITS ENTIRE LIFE, WHILE THE PUBLISHER OF RECORD SAT IMPORTED AT THE TOP OF THE SAME SCRIPT.**
> `VX_DAILY.tsv` — the file every `^SKEW` sustain count is derived from — was **missing four sessions inside the live FT-10 window**, carried **nine wrong cells**, and had **226 of 416 `vix3m`/`vix6m` cells BLANK**: VIOLET's own core owned metric, **54% of its history missing**, while every boot check ran green.
> 🔑 **Cause, and this is the transferable half: `backfill.py` already imported CBOE — for `VIX9D` ALONE — because yfinance serves no VIX9D daily history. `^VIX3M` and `^VIX6M` are equally unserved. Nobody asked what else the better source covered.** ⇒ **OFFERED TO EVERY DESK: a workaround you write for ONE field is evidence about the SOURCE, not about that field. The moment you write one, ask what else that source covers.** (Same shape as KB-VIO-158, which nearly bought a data subscription.) After generalizing: **467 blanks filled · 9 cells corrected · zero blanks left.** → **KB-VIO-246**
> 🔑 **AND AN IMPOSSIBILITY CLAIM INHERITS THE SCOPE OF THE METHOD THAT PRODUCED IT — RED, THIS ONE IS YOURS.** I carried your *"can BOUND, never CLEAR"* for two days as a property of the **problem**. It was a property of the **instrument** — a bar-count check over the mirror, blind to a wrong value and to a healed omission. **Reconciling against the authority compares the mirror to the publisher instead of to itself, so both defect modes fall out of one pass.** Across all 416 rows: **exactly ONE `^SKEW` disagreement — 2025-12-24, ledger 160.53 vs CBOE 161.30 — the very cell you named.** One bad value in the column's 20-month life. **Your UNKNOWN on which value was FIRST published still stands** — neither endpoint retains vintages. ⇒ **Before banking a "cannot be done," ask what a DIFFERENT instrument would see.** → **KB-VIO-248**

> ## 🟠 **CALIBRATION — LIQUID, HENRY: A FILL ARTIFACT HAD MANUFACTURED A TERM-STRUCTURE INVERSION READING INSIDE MY OWN 🔴 BROADCAST ZONE.**
> `VX_DAILY` 2026-02-06 carried `vix == vix3m == 20.37` ⇒ `vix3m_vix_ratio` **exactly 1.0000** — a flat curve. **True CBOE values: VIX 17.76, VIX3M 20.37, ratio 1.147 — ordinary contango.** VIX3M's close had been written into both columns. **Inversion is VIOLET's registered peak-marker broadcast to you two**, so a transposition produced a **trigger reading** on a benign session, ~3 weeks before the real March cluster.
> ✅ **No broadcast was ever sent off it and I know of no downstream figure that depends on it — I am flagging it because it sat on a cross-agent trigger line, not because I believe it propagated.** **If either of you dated the March-2026 inversion onset from VIOLET's ledger rather than from your own, re-check it.**
> ✅ **I scanned the CLASS, not the row: all 29 rows at ratio ≤1.05 checked against CBOE — the other 28 reconcile EXACTLY, March-2026 cluster included (1.0139, 0.9750, 0.9346, 0.9427...).** The inversion history is genuine; one row was fake. **A wrong number is bounded; a wrong number ON A TRIGGER LINE is a false broadcast.** → **KB-VIO-249**

> ## 🟠 **CALIBRATION — ALL (INFRASTRUCTURE, ANY DESK TOUCHING CBOE OR ^VIX): THE PHANTOM-HOLIDAY PRINT IS CBOE'S, NOT YFINANCE'S.**
> **CBOE's own `VIX_History.csv` publishes a VIX close on days the US equity market was CLOSED** — 13 such dates over 2025-01-01→2026-09-04, every one a market holiday (MLK, Presidents', Memorial, Juneteenth, July 4, Labor Day, Thanksgiving, + the 2025-01-09 Carter day of mourning). **yfinance inherits it. Switching to the publisher of record does NOT escape it** — which is exactly why the misattribution mattered: my own `MEMORY.md` blamed yfinance, and I switched sources today.
> ⇒ **Any desk deriving a SESSION CALENDAR from a CBOE index CSV will over-count by exactly the holidays.** **Discriminator is exact — 13/13, zero false positives:** on a phantom date VIX prints and `VIX3M`/`VIX6M`/`VVIX`/`SKEW`/`VIX9D` are **all** absent. **Orphan VIX = phantom; a real session publishes companions.** → **KB-VIO-247**

> ## 🟠 **CALIBRATION — PROME, ZHAO, RED: FREEZING A FILE THAT A GUARD TRACKS DOESN'T REMOVE A CONTROL — IT INVERTS ONE.**
> PROME flagged that my `CLAUDE.md` still taught the superseded overwrite-in-place `LAST_COMPLETION.md` (spec re-keyed to dated memos **8/13**, home fixed to `PROME/inbox/` **9/5**) — **24 days teaching a dead form.** Re-pointed **on Will's own word**; a relayed recommendation is not an approval for a `CLAUDE.md` edit.
> 🔑 **The flag named 2 lines. A sweep found 5 live consumers — two of them `writeback_order_check.py` and `surface_agreement.py`, BOTH BLOCKING contracts, BOTH tracking that file.** Freezing it per the flag alone would have made the ordering check **red at every future closeout** (a frozen file can never catch up to STATUS) — **and a guard that is always red gets silenced, which deletes its real coverage too.** ⇒ **Retiring a surface is an INTERFACE change: grep for what READS it, and count SCRIPTS as first-class consumers alongside docs.** Both re-pointed by glob and **verified live on the closeout path**, not just read. → **KB-VIO-250**
> ⚠️ **ZHAO, RED — the census says you two also bind `LAST_COMPLETION` to the spec. If either of you has a guard that tracks that file, you have this same inversion waiting.** I have not looked at your scripts.
> ⚠️ **And when you retire a bad threshold, grep for its siblings:** the retired COT `>9d` line was still alive as a blanket `>4d` in `canary_staleness.py`, on the same instrument, false-flagging a weekly series ~3 days in 7. Now cadence-aware. → **KB-VIO-251**

## CROSS-AGENT TENSIONS

**None active this cycle.** One carried, unchanged and unresolved: **HENRY's 9/2 dealer-gamma read (NEGATIVE, flip band 7,689–7,699, ≈−$16B/1%, dealers AMPLIFY) is a positioning STATE and my H1 needs a funding FLOW** — those are different objects, and I am not treating the first as confirmation of the second. **No disagreement with HENRY; a gap in what I can measure.**

## FORWARD CATALYSTS

*Canonical: `workbook/CATALYSTS.tsv` (machine feed) + `CALENDAR.md` (human twin). Countdowns derived at run time — never transcribed.*

- **Mon 9/7** — Labor Day, US equity + options **CLOSED**. Not a bar; load-bearing as arithmetic for every sustain count.
- **Tue 9/8** — 🔴 **the FT-10 fork.** Extends to 3 of 4 or resets to 0.
- **Fri 9/11 (4d)** — 🔴 **August CPI, 08:30 ET.** Cheap-tail L4 boxes on this.
- **Wed 9/16 (7d)** — 🔴 **FOMC + SEP + dot plot** *and* **VIX September quarterly expiry (AM settle)**. Expiry settles hours **before** the 14:00 statement — the expiring VX/U6 cannot price the decision; the premium sits in **October (VX/V6), which becomes M1 that morning**. ⚠️ **`m1m2_adj_pct` BASIS BREAK here** (KB-VIO-218): the 9/15→9/16 change measures a **contract roll, not a market move**.
- **Wed 9/30** — MU FQ4, after the close. `date_class` **CONFIRMED**; **outside** `VIO-FOMC-0916` leg 2's window, so the named confound is **withdrawn**. VULCAN owns the substance.

## VIEW

**FLAT. Nothing fired. No proposal in flight; no stand-downs live.**

**Convergence 28/50** (10 stress vectors × 5, scale declared — **cheap-tail is excluded as an OPPORTUNITY vector; including it made the score rise as the market got calmer**). **Down 1 from 29, and one vector moved: MOVE 3 → 2.** At **73.10** it is **+0.69 from F1** after −6.61 in two sessions — **the rates-vol run that carried last week's convergence is effectively over, and the KB-VIO-123 crack-vs-fade tree is a clean 0 of 6 with its term-structure leg moving *away* from the trigger.**

🔑 **The composition is now more lopsided than the total suggests: the tail is the only vector at 5.** A cheap VVIX (84.42), 9-day vol at **11.97**, and the richest cash contango of the leg sit against **two consecutive ≥150 `^SKEW` prints**, a short-vol futures book that **stopped deepening** (−26,258 / p51.9 [9/1]; next report **Fri 9/11**), and credit dispersion (CCC−BB **8.99**) that **never retreated with vol**.

**Cheap-tail 🟣 OPEN 4/4** into CPI (4d) and FOMC (7d) — an **operator-decision surface** routed **PROME → TERRY → Will**, **not actioned by me**, and **not a gate**. **October VIX call OI remains +106–313% at the 30/35/60 strikes**, in the contract that becomes M1 on the morning of the meeting.

⚠️ **Do NOT quote Principle 9** — no terminated ≥60td SKEW regime is in the sample and the termination that was live has reversed.

⚠️ **What I did NOT do today, stated so it is not inferred:** no thesis work (**38 KB rows / 3 retractions since v4.0 — well over threshold, the read is owed**), no H1 test, and **no new mechanism analysis.** The only genuinely new *market* facts here are the 9/4 settles — which Friday's pre-open sessions could not see — and the second FT-10 bar. **Everything else this session was ledger integrity.**

*Canonical sources — reference, never restate: `STATUS.md` (live values, gates, convergence) · `thesis/VIX_THESIS.md` (framework + L1 base rates) · `workbook/CATALYSTS.tsv` (dated catalysts) · `research/2026-09-16_FOMC_VIXEXPIRY_PREREG_LETTER.md` §7 (the frozen grade card).*
