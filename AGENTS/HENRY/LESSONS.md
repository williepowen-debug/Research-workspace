# LESSONS.md — HENRY Mistake Patterns & Rules

*Read at boot. Learn once, prevent forever.*

---

### [Data] — Always Pull Fresh Values
**Pattern:** STATUS.md values go stale between spawns (days/weeks). Citing stale VIX, HY OAS, or SPX levels produces wrong analysis.
**Rule:** If STATUS.md says "Known Data Issues" or values are >24h old, pull live data via web_search before any analysis. Never cite STATUS.md values as current without verifying.

### [Analysis] — VIX Spikes Can Be Artificial
**Lesson from Aug 2024:** VIX spike to 65 was 85% bid-ask widening, not real fear. 0DTE volume dropped 26%, recovery in 3 sessions. Don't treat VIX spikes as ground truth — check the mechanism (real selling vs liquidity withdrawal).

### [Analysis] — Credit Leads Equities, Not Vice Versa
**Rule:** Never call an equity bottom until HY OAS has peaked. Credit reprices before equity every time. If someone asks "has the selloff bottomed?" — check HY OAS first, not SPX technicals.

### [Process] — Distinguish Margin Trade vs Credit Trade
**Lesson from KRE:** Regional banks can sell off because the yield curve flattens (margin trade) or because credit quality deteriorates (credit trade). The distinction determines speed — margin trades grind, credit trades gap. Always identify which is driving the move before forecasting trajectory.

### [Verification] — Don't Cite Own STATUS.md for Live Prices
**Rule:** STATUS.md is for thresholds, frameworks, and thesis. It is NOT a live data feed. When asked about current VIX, SPX, or spreads, pull from web sources. Citing your own stale dashboard as "current" is circular.

### [Verification] — Cross-Agent Estimates Need Discount
**Lesson from LIQUID (Mar 3-4):** LIQUID's HY OAS model overestimated by ~30bps two sessions in a row (estimated 335-355bps; FRED confirmed 308bps). Pattern, not one-off. **Rule:** When using LIQUID's spread estimates, apply -30bps discount until the model is recalibrated. Always verify against FRED/ICE actuals before citing.

### [Analysis] — Consensus Revision Is a Framing Weapon
**Lesson from ADP (Mar 4):** ADP consensus was quietly revised from 130K → 50K before release, so +63K got framed as a "beat." The underlying data is unchanged — it's still a massive miss vs original expectations. **Rule:** When a data release drops, check what consensus was *before* any last-minute revision. The original consensus is the true sentiment anchor.

### [Analysis] — Geopolitical Headlines ≠ Fundamental Resolution
**Lesson from Iran peace talk leak (Mar 4):** NYT report of "indirect approach" → SPX +0.78%, VIX compressed. Same day IRGC declared "complete control" of Hormuz. Market rallied on hope, not change. **Rule:** Don't adjust thesis on geopolitical headlines alone. Require: (1) confirmed ceasefire/deal, (2) shipping lane reopened, or (3) oil price sustained below pre-event level. Until then, it's noise.

### [Analysis] — Unilateral Announcement ≠ Bilateral Resolution
**Lesson from Hormuz reopen (Apr 17):** Iran FM declared Hormuz "completely open" → Brent -11%, WTI -14%, SPX +1.2%, VIX 17.66. But US blockade remained in force — tankers still couldn't reach Iranian ports. Market priced full resolution; reality was asymmetric flow unwind. **Rule:** When a party unilaterally declares de-escalation, separate (a) the party's own actions (stopped blocking shipping) from (b) counterparty response (blockade persisting/lifting). Oil-flow normalization requires BOTH sides stepping back. Price the physical delta (tanker tracking) not the verbal one. Also: a clean oil unwind does not retroactively fix CPI/PPI/UMich prints already locked — stagflation survives even if the macro shock is subtracted.

### [Process] — Don't Duplicate-Track VIOLET Vol Fields
**Lesson from VOL REGIME restructure (Apr 16-17):** VIOLET owns VIX/VIX3M/VVIX/SKEW/term-structure via `workbook/VX_DAILY.tsv`. HENRY was independently pulling and occasionally diverging. **Rule:** For fields VIOLET owns, HENRY reads from VIOLET's file and attributes (`[CONF VIOLET <date>]`). Don't re-pull. HENRY retains ownership of 0DTE share + GEX regime (VIOLET scope excludes gamma/dealer layer). Cross-reference her tactical triggers (e.g., HY OAS +100bps from trough → VIX spike lead) rather than reinventing.

### [Process] — Archive Before Clutter Masks Signal
**Rule:** When workbook/ or root has files >30 days old that aren't in the active read path (per CLAUDE.md), move to `archive/` same session. Historical reference is fine; cluttering the boot surface with stale TRADE decks or synthesis docs slows every future session. Test: if a file isn't listed in CLAUDE.md's FILES table AND is >30 days old, it's archive-eligible.

---

*Last reviewed: 2026-04-17*
