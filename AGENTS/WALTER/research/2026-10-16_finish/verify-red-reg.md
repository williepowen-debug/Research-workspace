# RED / REGINALD threshold verification — 2026-10-16

WALTER research helper `/root/verify_credit_followup`; continuation of the narrow verification assignment. No owner state, trigger, fire log, delivery log or BOARD edited. No trade instruction. This receipt covers all **12 RED + 8 REGINALD rows**, their observation basis, present evidence and unresolved legs; row accounting is not a claim that every instrument was freshly gradeable.

## Inputs and authority

- `observations.json`, capture started **2026-10-16T17:18:56Z**: FRED observations, Cboe SKEW, dated equity/futures quotes, EIA Cushing. Each series retains its own observation date. Intraday quotes cannot become completed daily closes.
- RED generated scan read whole and hash verified against canonical `FALSIFICATION_TRIGGERS.tsv`: **9e24d1d0a1540f80f6a09fe4722f453d536ca4b28c72c0a8ab4fbdf9778c336f**. Canonical current state/exit fields checked for all 12; load-bearing FT-08 state/basis ruling and FT-11 classifier/activation read from canon.
- REGINALD `THRESHOLDS.tsv` read whole, current STATUS threshold block, NOTES on T-02/T-03/T-04/T-06, and `REG_T02_EXIT_LOG.tsv` through October 13. WALTER's two fire-only ledgers read; neither can establish present state or exits.
- `THRESHOLD_SCAN.md` current procedure read, including contract controls and non-session rule. Executed RED `nonsession.is_nonsession` on the recent OAS/VIX dates: October 12 is excluded for ICE OAS and retained for VIX.
- Morning **SIG-W-20261016-001** full body read: it records October 15 first-published HY **323bp**, absent ~13:10Z and present ~14:40Z; October 14 **325bp**, October 13 **316bp** reset. Latest-revised capture agrees. The morning artifact is the retained publication witness; this helper did not reconstruct a separate ALFRED vintage archive or locate raw morning HTTP snapshots. Do not describe the present afternoon capture as first-published.
- Earlier **SIG-W-20261016-007** full body read and arithmetic independently reproduced. It already routes the FT-11 window; duplicate suppressed.

## RED — 12 rows

| Row | Registered test / current owner state | Evidence and result | Exit / limitation |
|---|---|---|---|
| FT-01 | HY <280bp ×3; ARMED | 323bp, October 15; qualifying run **0/3**. No new fire. | Exit >=280 ×3 belongs to a fired cycle; do not re-execute a completed round trip. |
| FT-02 | HY >320bp ×3; owner file still1/3 | First-published witness325 [10/14],323 [10/15], following316 [10/13] gives **2/3**, already routed -001. | Next eligible observation10/16, expected next business publication10/19. Exit <300 ×3. Later revisions do not retro-fire/un-fire. |
| FT-03 | ICE Brent front-month official settlement >$130 ×5; ARMED | **SETTLEMENT COVERAGE INCOMPLETE.** Vendor BZ probe109.29 at17:15:01Z is provisional, not registered ICE settlement. | Exit <$115 ×5. No settlement sustain grade or certified distance from vendor quotes. |
| FT-04 | Same settlement basis <$75 ×3; ARMED | **SETTLEMENT COVERAGE INCOMPLETE**, same basis caveat. No fresh fire established. | Exit >=$85 ×3; intraday109.29 cannot certify an exit or historical run. |
| FT-05 | Initial claims >250k, one weekly print; ARMED | **199k**, week ended10/10, release10/15: condition not met. | Exit <=225k ×2 only relevant after fire. Latest prior week198k is revised; never label it first-release197k. |
| FT-06 | VIX close <16 ×5; FIRED-BANKED | Registered VIXCLS **16.46 [10/15]**; exit >=18 run **0/5**. Existing fire retained. | Intraday ^VIX19.43 [10/16] is context, not an exit observation. October12 counts for VIX. |
| FT-07 | CCC OAS >930bp ×1; FIRING-BANKED | **1,278bp [10/15]**, existing fired condition, duplicate suppressed. | Exit <930 ×3: **0/3**. Exactly930 holds on both sides. |
| FT-08 | Core CPI Table A 3-month compound >=3.0%, monthly; FIRED10/14 | Owner's September release inputs July0.2%,August0.3%,September0.3% reproduce **3.247216% →3.2%** with Decimal. No new monthly release. | Exit <2.5%, one monthly print; not met. Current fire's +3 is preserved; prospective +1 amendment is not applied retrospectively. |
| FT-09 | T5YIFR >2.55% ×5; ARMED | **2.31% [10/15]**, qualifying run **0/5**. | Exit <2.40 ×5 applies only in fired state. Current distance0.24pp/9.41% of threshold, dated10/15; outside5% watch. |
| FT-10 | Cboe SKEW >=150 ×4; FIRED10/14 | Publisher CSV **160.45 [10/15]**; stays fired, no refire. | Exit <140 ×4: **0/4**. Cboe10/12 is a real equity session; no holiday exclusion. Current CSV is latest capture, not reconstructed first-publication history. |
| FT-11 | Conditional five-session classifier; owner ARMED | Window **10/6→10/14**: Δ30Y−12bp, FLOW legs satisfied. Already **-007**, not a new signal. | Latest-revised FRED mirror; owner publication-vintage adjudication pending. FLOW moves no weights and does not identify buyback versus haven demand. |
| FT-12 | HY <260bp ×3; ARMED | **323bp [10/15]**; **0/3**. | Exit >=260 ×3 not executed while armed. |

CPI uses the later, case-specific **S50 Table A basis ruling**, not the stale index-level sentence or retired0.4% proxy elsewhere in canon. This is replay of the recorded October14 owner grade, not a fresh BLS reread. The next CPI release is an event, not a missing daily observation.

## REGINALD — 8 rows

| Row | Registered test | Evidence and result | Owner state / limits |
|---|---|---|---|
| T-01 | KRE unadjusted regular close <$60 ×1 | Vendor previous close **$69.75 [10/15]**; not met. Today$69.61 is intraday and excluded. | Owner un-fired. Prior-close metadata is one vendor witness, not an independently reconciled historical-close pull. No prospective exit action. |
| T-02 | WAL unadjusted regular close <$78 ×1; exit >=$81.90 ×3 | Vendor previous close **$74.35 [10/15]**; exit **0/3**. Today$74.57 excluded. | Owner FIRED cycle2 since9/1; ledger through10/13 agrees. Latest nonqualifying exit close preserves fired state and suppresses sub78 reentry. Price token does not establish CRE causation. |
| T-03 | HY >320bp ×3 daily closes | **2/3**, same325/323 first-publication witness as FT-02, already -001. | Exit <=300 ×5 differs from RED's <300 ×3. Owner must confirm calendar letter; present run has no holiday inside it. A future fire needs bank-credit attribution, not automatic bank-transmission inference. |
| T-04 | HY >350bp ×3 | **323bp [10/15]**, run **0/3**;27bp/7.71% below line, outside5% watch. | Exit <=330 ×5 only after fire. No new issuance-freeze grade. |
| T-05 | Initial claims first release >300k ×1 weekly | DOL **199k**, week10/10, published10/15; not met. | Exit <=275k ×3; revisions do not retro-fire. Direct DOL primary confirms199k first release; prior197→198 revision retained separately. |
| T-06 | System FHLB advances >$700B ×3 official quarters; consequence REVIEW | Owner official run **2/3 throughQ2**: Q4-25$677B reset,Q1-26$734B,Q2-26$810.7B. No new official Q3 observation. | Current official calendar: **Q3 highlights10/30; Combined Financial Report11/13**, subject change. Owner's ~10/29 estimate stale. Letter names CFR; highlights eligibility must be adjudicated, not assumed. Nowcast~$770B cannot count. REVIEW requires top-four growth contribution and qualified borrower median before escalation. |
| T-07 | Trepp office DQ >15% ×3 monthly | Full September PDF Table2 **12.16%**; run **0/3**. Current distance2.84pp/18.93% below15. | Distinct from CREED >12 ×2, which is1/2. No special-servicing substitution. Full PDF verification in verify-credit.md. |
| T-08 | SOFR−IORB >+15bp ×3 matched daily dates | **−1bp [10/15]** (3.89−3.90), prior−2 [10/14],−1 [10/13]; run **0/3**. | Exit <=8 ×5 applies only after fire. Match IORB to SOFR trade date; today's10/16 IORB is not today's SOFR observation. |

DOL primary: https://www.dol.gov/sites/dolgov/files/OPA/newsreleases/ui-claims/20261599.pdf . Official FHLB calendar: https://www.fhlb-of.com/investor-resources/financial-reports/ . Calendar change is new actionable owner information; parent decides routing. No owner state modified here.

## FT-11 calculation and duplicate disposition

Use exact Decimal percentage inputs converted to integer basis points before comparisons. DGS frontier10/14; OAS frontier10/15. The five elapsed sessions after October6 are7,8,9,13,14; ColumbusDay10/12 is a bond non-session.

| Leg | October6 | October14 | Change |
|---|---:|---:|---:|
| DGS30 |5.64%|5.52%|−12bp|
| DGS5 |5.03%|5.00%|−3bp|
| DGS2 |4.79%|4.82%|+3bp|
| T10YIE |2.36%|2.35%|−1bp|
| DGS20 |5.68%|5.57%|−11bp|
| DGS10 |5.27%|5.19%|−8bp|

Precondition −12<=−10.2 met. Δ(30Y−5Y)=−9<=−3; |ΔBE|=1<=4; |Δ2Y|=3<=6: original FLOW branch met. FUNDAMENTAL (Δ2Y<=−8 OR ΔBE<=−5) not met. Alternative Δ(2×20Y−10Y−30Y)=−2, which fails<=−4. These are precisely -007's values; **DUP, no repeat routing or synthetic fire entry**. No owner weight or grade executed.

## Mandatory contract probes and refusals

Executed current `fetch.contract_probe` for CL,BZ,HO at **17:25:16Z**, default horizon5, its internal distinct-price negative controls. Saved complete result **red-reg-contract-probe.json**. Cache/audit redirected under this helper's `.cache/` prefix. Probes are read-only; no code changed.

| Root | Continuous observation | Control | Verdict / identity |
|---|---|---|---|
| CL |98.67,17:15:10Z|Four distinct dated prices; time gaps2–11seconds; October candidate missing|**REFUSED-no-price-match**. December98.66 is close but not identical; do not guess or override. Resolved symbol UNKNOWN.|
| BZ |109.29,17:15:01Z|Three distinct prices; matched leg time gap0; other gaps2/197seconds; Oct/Nov candidates missing|Function **IDENTIFIED**, `tracking=BZZ26.NYM`; negative control passed, no vendor-name cross-check. This records the function's result; truncated name still supplies no independent month/year witness.|
| HO |4.7178,17:15:10Z|Four distinct prices, matched leg time gap0; October candidate missing|**REFUSED-disagrees-with-vendor-name**: price matchesHOZ26.NYM (December), parsed name saysHOX26 (November). Resolved symbol UNKNOWN.|

Function schema emits `tracking`, not `resolved_symbol`; the table labels its actual output instead of inventing a returned field. Quotes were approximately10minutes old when the probe ran. The900-second matched-leg limit remains uncalibrated and tests relative timestamp compatibility; passing it is not consumer acceptance or ICE settlement certification. CL/HO refusals remain **UNRESOLVED**. Continuous CL−BZ or HO−CL spreads must not be graded from this snapshot. Dated matched-month quotes may be a separate input only with their own verified identity/basis and the registered month rule; no substitution was performed here.

## Coverage conclusion

No additional RED/REG fire established beyond previously routed FT-11 candidate -007 and the already-routed HY count -001. Retain **HY2/3**, not three because of a holiday or a later fetch. Existing FT-06/07/08/10 and WAL cycle2 states persist on their applicable exits. **FT-03/04 official settlement coverage remains incomplete**, and CL/HO identity probes refuse; this is not an all-clear. New FHLB official release dates warrant parent review. Cushing corroborating context is26.607million barrels, week10/9, above the separate20million line; no threshold row added or changed.
