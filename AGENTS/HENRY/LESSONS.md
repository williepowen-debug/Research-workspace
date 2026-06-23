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

### [Analysis] — Data-Right, Positioning-Early Asymmetry
**Lesson from Mar 27-28 triple-catalyst playbook:** HENRY correctly pre-called PCE hot (HEN-13), Q1 window dressing (HEN-15), Apr 1 ceasefire-rally-as-bull-trap (HEN-16), and VIX >30 regime shift (HEN-14) — **4/4 catalyst-framework calls confirmed**. Yet every directional short the playbook held (IWM, HYG, TLT, KRE, APO, long-oil) bled: SPX 6,610 → 7,127 (+7.8%), VIX 31 → 17.66, HY OAS 328 → 285, Brent $100 → $88 (Hormuz reopen Apr 17 subtracted the shock variable). **Rule:** Calling the data correctly ≠ positioning paying off. Vol-control mechanical buying can overwhelm cascade selling during compression regimes; a second wave of de-escalation headlines can re-activate the same squeeze trade even after the first wave faded per plan. **How to apply:** When a playbook scenario resolves in your favor on the data but positioning bleeds, the thesis is early, not wrong — roll duration, don't trim size (CLAUDE.md rule #7). Pre-register this risk: scenario grids should include a "data confirms / market ignores" row, not just "data confirms / market reprices." Worked example: `archive/reports_mar17/` (TRIPLE_CATALYST_PLAYBOOK_MAR27, CATALYST_PLAYBOOK_MAR27-28, PCE_PREP_MAR28).

### [Analysis] — Anchor the Yield Clause to the Right Tenor (hawkish-into-slowing flattens)
**Lesson from HEN-33 (FOMC 6/17 2026):** Predicted "FOMC dots hawkish-of-pricing → **10Y** +10bps within 2 sessions." The dots DID flip hawkish-of-pricing (cut→hike bias, median 3.8%, hawkish Warsh) — the directional call was right — but the 10Y FELL −3bps while the **2Y surged +15bps** (biggest Fed-day move since Mar 2008). The miss was the vehicle, not the direction. **Rule:** when a hawkish-of-pricing Fed ALSO cuts growth (SEP GDP 2.2%, PCE up = stagflationary), the curve FLATTENS — the front end (2Y) carries the hawkish repricing while the long end (10Y) is anchored or falls on the growth cut. Anchor the yield clause to the tenor the surprise actually hits: hawkish-rate-path surprise → 2Y; growth/term-premium surprise → 10Y. Don't default to the 10Y. (Cf. auto-mem `anchor-prediction-to-surprise-not-priced` — same family: get the *expression* right, not just the surprise.)

### [Verification] — Stunning Secondary Claims Need Primary Confirmation Before Integration
**Lesson from the "Fed flipped cut→HIKE" relay (6/23):** Multiple WALTER board signals carried "the Fed just flipped cut→HIKE 6/17." A cut→HIKE flip when hold was ~99.9% priced is a *stunning* claim — and it was WRONG. The Fed HELD 12-0; the DOT PLOT flipped to a hike bias (a "Dot Plot Flips to a Hike" headline misread as an actual rate hike). The adversarial-verify stage caught it against the primary FOMC statement. **Rule:** the more surprising a relayed/secondary claim, the more it needs primary confirmation before it goes load-bearing — especially policy actions (hike vs hold-with-hawkish-dots are very different). On catch-up boots after a gap, run a verify pass on the single most consequential gap event, not just a research pass.

---

*Last reviewed: 2026-06-23*
