# §4b cluster grade: state before Amazon prints, and how Amazon decides it

**Written:** 2026-10-29T13:37:52-04:00 (before Amazon's Q3 release; first public: none). VULCAN, Will-launched session, Claude Code, Opus 5.5.
**Rule:** `workbook/EXIT_PROTOCOL.md` §4b (pre-registered 2026-09-29). Applied on the letter; no new threshold.

## Three names in

| Name | Capex direction | Reaction graded (§4b uses after hours) | Management pressure language | Leg |
|---|---|---|---|---|
| META (10/21) | **RAISE**: 2026 low end +$5B to $135–145B (8-K, primary) | **+2.1% after hours** (KB-248); regular session 10/22 −7.13% recorded as a disagreement | none recorded | **RAISE and REWARDED** |
| MSFT (10/28) | **TRIM, not a cut**: "for the calendar year, spend should be approximately $170 billion due to the 3P capacity delays" (Hood, T2 transcript; resolves the FY vs CY conflict to CALENDAR year) vs ≈ $175B in July; still up YoY; Q2 > $50B | after-hours move not measured; regular session 10/29 −1.02% at 13:37 ET (fetch.py, intraday) | **none on the letter.** Hood: "We had higher token pricing than we expected in the quarter" and "token pricing will create a little bit of variability"; Nadella names open-weight models as a product route, not a pressure | **neither leg** (no raise, no cut) |
| GOOGL (10/28) | **HELD**: 2026 $195–205B "remain unchanged"; "We continue to expect our CapEx to increase significantly in 2027" (Ashkenazi, T2 transcript; repeated, not a new raise) | ≈ −10% after hours (Investing.com headline, T2); regular session 10/29 −12.67% at 13:37 ET (fetch.py, intraday) | **none on the letter**: expects "an attractive ROIC that remains meaningfully above our cost of capital"; says investment "will put pressure on free cash flows" (FCF, not ROI) | **neither leg on the letter** |

No capex cut YoY anywhere. Confirm-legs met: 0 falls-on-a-raise, 0 pressure citations, 0 cuts. Falsify-legs met: 1 raise-and-rewarded (META).

⚠️ **Recorded disagreement (not a regrade):** Alphabet lost about an eighth of its value on a print with an unchanged guide, a reiterated 2027 increase and stated FCF pressure. That is the returns-case concern in spirit, but the registered letter needs a fall on a RAISE, and the guide was held. Record it for the rewrite; do not count it.

## How Amazon decides the cluster (stated before the print)

| Amazon outcome | §4b verdict |
|---|---|
| Capex guide CUT year on year | **CONFIRMS fragility** (any cut) |
| Management cites inference-price, open-weight or ROI pressure | **CONFIRMS fragility** |
| RAISE and after-hours stock UP | **FALSIFIES for this cluster** (META + AMZN = 2 raised and rewarded, no cut) |
| RAISE and after-hours stock DOWN | **NO-VERDICT** (1 fall on a raise, below the ≥2 needed; 1 raise rewarded) |
| Held/flat or trimmed, not a YoY cut, whatever the stock does | **NO-VERDICT** |

After-hours reaction is read as the price change from the 10/29 close to a dated after-hours quote, labelled with its time and source. If Amazon gives no explicit capex direction, use the stated full-year figure against its prior one; if that is ambiguous, the name is NO-LEG and the verdict is NO-VERDICT.
