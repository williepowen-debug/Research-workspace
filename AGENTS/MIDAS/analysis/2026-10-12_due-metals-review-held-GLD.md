# MIDAS — due metals review and held GLD — 2026-10-12

**Read at:** 2026-10-12T17:03:53-04:00. Prices use 2026-10-09 completed vendor daily bars; yield and regression end 2026-10-08; COT as-of 2026-10-06, read 10/12. No threshold or capital change. Actual composite 8/20.

## 1. Held GLD: structural demand remains; rising real yields remain a measurable headwind

The portfolio mirror received 10/11 carries **17 GLD shares**, replacing this desk's old 16-share book assumption. Its broker mark is $384.58, value $6,537.86, **19.64% of the $33,284.88 Fidelity account total**. Capture/mark time is UNKNOWN, and position truth remains Will/broker off-repo. The separately retrieved 10/9 GLD vendor close is also $384.58; that agreement does not certify the broker's timestamp. The mirror also carries 10 TBT shares and **one TLT $82 put expiring 10/16** with a 10/14 management clock. The old Sep-30 $77-put delta and coverage arithmetic cannot describe this book. Source: root `FORGE/STATUS.md` and its 10/11 broker transcription reference; TERRY owns current option delta and any action.

Rolling **120 paired returns**, OLS with intercept, GLD unadjusted percentage return on same-date change in FRED DFII10 (percentage-point change ×100 = bp): **beta -0.1632%/bp, t -4.83, R² 0.165, n=120, 2026-04-20 → 2026-10-08**. The −0.08 flip is **NOT reached**. At the 10/9 mark, the 17 shares imply **−$106.71 per +10bp** under this one-factor local linear estimate. This is an association, not an identified causal exposure or a portfolio hedge ratio; its low R² leaves most daily movement unexplained. The 20/60-session betas are −0.1155/−0.1397; all remain negative. DFII10 **2.87% [10/8, FRED MIRROR-WALLED]** is 4bp below 2.91% [9/29], so the early-October recovery is consistent with rate relief, not a new proof of decoupling. Treasury XML returned 404 and the Treasury rendered-page browser retrieval failed; BOND owns the level.

Construction check: the same method reproduces 9/29's −0.168396 (old −0.1684). Replaying 9/23 gives −0.154483 versus the archived −0.1551; the old frozen paired inputs are absent, so that 0.0006 difference cannot be assigned to a revision versus sample choice. Today's method, inputs, window and units are saved explicitly. Latest-revised FRED data are used, not a first-publication grading basis. The VECTOR-3 two-win falsifier fired on 9/11 and 9/18 and remains an historical fire; today's beta does not erase it. No terminal prediction is re-graded.

The structural offset is still material: September gold ETFs added **$10bn / 67t**, bringing global holdings to **4,256t**. This is global ETF demand, not GLD-specific share creation. [WGC ETF release 10/7; data through 9/30](https://www.gold.org/goldhub/research/gold-etfs-holdings-and-flows/2026/10). Reported central-bank net purchases were **39t in August / 170t YTD**; China +20t and Russia −6t demonstrate differing country directions. Monthly reported transactions exclude unreported buying and cannot replace the quarterly total-demand <100t kill test. [WGC 10/6; August cutoff](https://www.gold.org/goldhub/gold-focus/2026/10/central-bank-gold-statistics-central-banks-continue-summer-spree-august). WGC attributes September's **−8.5%** spot decline to rising yields/dollar and futures liquidation despite ETF demand; its managed-money −84t uses a different category and interval from this desk's legacy noncommercial COT. [WGC 10/7](https://www.gold.org/goldhub/research/gold-market-commentary-september-2026).

**Domain judgment:** gold retains fiscal/monetary diversification relevance, but these 17 shares are not a reliable hedge against a rising-real-yield shock. Evidence supports keeping the structural thesis under review; this review creates no sell, add, roll or sizing proposal. Net coverage from TBT plus the live $82 put is UNVERIFIED without TERRY's current sensitivities.

## 2. Four precious metals, each with its own read

| Metal | Contract | Vendor daily bar 10/9 | Since 9/30, same contract | ETF 10/9 |
|---|---|---:|---:|---:|
| Gold | `GCZ26.CMX` (Dec 2026) | $4,216.30 | +0.71% | GLD $384.58 |
| Silver | `SIZ26.CMX` (Dec 2026) | $61.05 | +0.80% | SLV $54.78 |
| Platinum | `PLF27.NYM` (Jan 2027) | $1,693.30 | -1.49% | PPLT $15.25 |
| Palladium | `PAZ26.NYM` (Dec 2026) | $1,150.40 | -5.11% | PALL $20.77 |
| Copper | `HGZ26.CMX` (Dec 2026) | $6.69 | +1.06% | CPER $40.31 |

Daily futures bars are VENDOR last-trade bars, **not exchange-certified settlements**. Today's 10/12 bars are excluded from close-based calculations. A separate boot pull at approximately 16:51 ET recorded GLD **$382.15 (−0.63%)**; it is a timestamped vendor quote, not a certified close. Four continuation pointers are DYING on prior-session volume: SI=F, HG=F, PL=F, PA=F; GC=F matched GCZ26. Use the named contracts above.

- **Gold:** modest recovery since 9/30; rate relief and continuing ETF purchases are plausible supports, while speculative longs continue to shrink. Not a new decoupling grade.
- **Silver:** same-contract +0.80% since 9/30, ETF +0.50%; no post-approval band crossing. The Silver Institute forecasts 2026 industrial demand −3%, total demand −2%, flat mine output and a **46.3 Moz deficit**. This is its April forecast, newly primary-verified here, not an October demand print. [Silver Institute / Metals Focus](https://silverinstitute.org/elevated-lease-rates-regional-liquidity-tightness-and-robust-investor-interest-resulted-in-record-silver-prices-in-2025/). Heraeus's 10/12 weekly summary describes rates/oil pressure across gold and silver; a full weekly report was not retrieved. [Heraeus](https://www.heraeus-precious-metals.com/en/precious-metal-prices-reports/weekly-market-report/).
- **Platinum:** same-contract −1.49%; the ETF crossed its −15% d200 line on **10/7 (−16.31%)**, remained below on 10/8, then recovered to −13.47% on 10/9. WPIC now forecasts a **265 koz 2026 surplus**, with deficits returning from 2027; China platinum imports reached 1.85 Moz through August, matching 2025 despite weaker jewellery/bar demand. The desk's old unverified deficit backdrop is retired. Forecasts and stock imports do not prove current end consumption. [WPIC 10/9](https://platinuminvestment.com/investment-research/perspectives/platinums-use-in-a-wide-range-of-end-markets-sets-it-up-well-to-recover-if-the-current-macro-volatility-eases?category=&page=1&term=).
- **Palladium:** same-contract −5.11%, weakest precious metal since 9/30; COT is net short **−33.32% of OI**, context for short-cover risk, not proof of a squeeze. October macro pressure is a candidate common driver; no fresh major SA/Russia supply event was established in this bounded primary-source sweep. UBS's old supply-tightening call remains unconfirmed by the tape. PGM lease rates, NYMEX stocks and fund share-count flows remain absent, so a supply-versus-flow attribution is unresolved.

## 3. Bands: post-approval timing changes the interpretation

Definitions: d200 = unadjusted ETF close / trailing 200-session mean −1; dd252 = close / trailing 252-session closing high −1. T = trend state; C = crash event with the approved 21-session decay; S = upside state. The existing 2026 crash events have decayed; no C or S line first crossed in the post-approval interval inspected.

| ETF | d200 10/9 | dd252 10/9 | T / C / S would-be levels | Current would-be max |
|---|---:|---:|---|---:|
| SLV | -16.71% | -48.13% | 3 / 1 / 1 | 3 |
| PPLT | -13.47% | -39.54% | 2 / 1 / 1 | 2 |
| PALL | -21.96% | -44.14% | 3 / 1 / 1 | 3 |

**All three remain unscored through 2026-11-01 21:40 ET (WQ-352).** Actual M2=1 and I2=2; composite stays **8/20**. Counterfactual if every current band level were scored now: M2=3, I2=3, composite **11/20**; this is a diagnostic, not an applied score or a Nov-1 forecast.

**Platinum** supplies the first observed qualifying post-approval crossing (T −15%, 10/7). The crossing is historical; T is a state leg and the current would-be platinum level has recovered to 2. **Palladium** crossed T −20% on the **10/1 close (−20.18%)**, before Will's 21:40 ET approval. It then stayed below −20% through 10/9, so it has **no first post-approval crossing** despite its orange current level. Its 10/7 −24.04% came within 0.96pp of the −25% red line without crossing. This corrects the carried assumption that Pd's next orange reading would qualify. WQ-368 CROSSING vs CALENDAR remains pending for 11/1; MIDAS's operative reading stays CROSSING. Shared precious-metal antecedents are counted once. Bands remain design-fixed, not time-fixed: their fit included the 2026 collapse.

## 4. CFTC: gold de-crowds again; the other metals differ

All four **legacy futures-only full-size** rows share the verified in-row date **2026-10-06** and pass code/name and totals identities. Source PRIMARY [CFTC raw file](https://www.cftc.gov/dea/newcot/deafut.txt); exact response saved alongside this report.

| Metal | Open interest, contracts | Net noncommercial, contracts | Net/OI | Frozen full-history percentile |
|---|---:|---:|---:|---:|
| Gold | 396,109 | 210,335 | 53.1003% | 97.12 |
| Silver | 105,130 | 23,153 | 22.0232% | 52.18 |
| Platinum | 65,868 | 13,968 | 21.2060% | 25.23 |
| Palladium | 21,060 | -7,017 | -33.3191% | 16.06 |

Gold vs 9/29: net **−8,297 contracts**, OI **−10,347**, ratio **−0.6897pp**. Third consecutive weekly ratio decline since 9/15; still in the **top 2.9%** of the frozen n=868 distribution. Declining concentration is not uncrowded positioning. Other-metal percentiles use the frozen n=872 reference; Pt/Pd regime shifts after 2022 mean full-history ranks are context only. Gold has no live score-changing registered successor test; positioning carries no standing band. All four vintages are written into consumed ledgers after this read. Ag/Pt/Pd freshness is now boot-wired against the per-metal ledger; the tool never consumes a row automatically.

## 5. Copper and corrections: no demand-collapse confirmation

LME **233,025t [10/9]**, **−0.69%** against the contemporaneous 234,650t rolling 2-year median, versus 249,400t on 9/30. [Westmetall LME mirror](https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Cu_cash). HGZ26 +1.06% since 9/30; CPER +6.25% over 63 sessions and +7.18% vs its 200-day mean: no −20%-price/+100%-inventory conjunction. China's September construction PMI **50.3**, +3.4 points from 46.9, clears ZHAO's >47.5 rebound condition; manufacturing **50.1**, composite **50.7**. [NBS 9/30 primary](https://www.stats.gov.cn/sj/sjjd/202609/t20260930_1965450.html). This is a material counterexample to carrying the August structural-collapse attribution forward; it is consistent with recovery from temporary disruption but does not identify weather causally. China interpretation belongs to ZHAO. The construction-to-refined-copper lag remains unmeasured; current COMEX/SHFE stock series were not retrieved, so LME draws alone cannot distinguish demand from venue relocation.

Irkutsk correction **COR-20261008-07** applied: the original plague framing is unestablished and no smelter production impact is reported. Original and correction were consumed together; no aluminium or PGM supply trigger is inferred. `BOARD/SIG-W-20261008-007-CORRECTION-to-20261004-004-irkutsk-plague-is-a-lab-worker-death-pneumonia-unknown-aetiology-no-plague-confirmed-smelter-masks-only-MIDAS.md`. Citi's Nov-4 long-bond supply reduction is a forecast, and Shelton's appointment is not a gold-policy instrument; both remain BOND/ZHAO context, not new M1 evidence.

## Runtime, continuity and validation

Desk MIDAS; provider OpenAI; runtime Codex; exact model identifier UNKNOWN (GPT-6 family exposed); session `01a131e1-82c3-7702-beae-4992d53e8fd5`; repo `/home/willi/Research-workspace`, launch cwd `AGENTS/MIDAS`. Explicitly read root CLAUDE.md, AGENTS.md, USER.md, desk CLAUDE.md, PROME/COMPLETION_SPEC.md and the applicable Runtime mechanics. Shell, patch and web tools verified. Initial sandbox network DNS failed; approved network-capable public pulls worked. No subagents. Independent fleet discovery/native cross-session messaging unavailable; recipient identity/notification/consumption remain UNKNOWN or pending. File packets are durable delivery only.

Opening pull and closeout push deferred under root Before-pulling rule: TERRY had uncommitted outside-desk work, and SHADE later did too. Own commits remain path-scoped. No foreign work is staged or changed.

DAEDALUS dispositions: float edge rounded to DFII10's published 1bp precision; Ag/Pt/Pd COT ledger + boot leg built; obsolete SCRATCH blocks rotated verbatim off the boot path, with every live obligation re-homed; LESSONS ~170-character hook target explicitly advisory. WQ-399 correction-receipt syntax updated. **11 guard tests PASS** (fresh/unread/stale/missing/corrupt/mixed/source failure and exact +5bp boundary). Boot/read-cap/claim/consumer/orphan results are recorded in the delivery memo after final verification. M1 beta was remeasured; a prospective successor needs a separate, base-rated registration and remains open. Existing MIDAS-09/10 resolve 10/30 and were not graded early.

Raw evidence: `sources/2026-10-12_review/summary.json`, per-contract/ETF CSVs, metric CSVs, `GLD_DFII10_pairs.csv`, `DFII10.json`, and `deafut.txt`. Temporary retrieval code used pandas/NumPy/yfinance and the desk's existing CFTC/FORGE clients; exact calculation conventions are above. No exchange-certified settlement or current option sensitivity was obtained.

### Final closeout checks

Five-leg boot rc1: metals contract-identity REVIEW only (four dying pointers); gold and Ag/Pt/Pd COT all quiet, no predictions due, ledgers quiet. Correction check rc0. Read-cap rc0 within its three-file charter heuristic, not a full runtime injection audit. STATUS/SCRATCH/OPEN_ITEMS total **71,595 → 36,957 bytes**; all five desk files counted in the cost ceiling **135,980 → 101,736 bytes**. STATUS/SCRATCH/NEXUS prior snapshots and closed MIDAS-08 registration history are preserved verbatim off the boot path; every current obligation is re-homed. No individual inspected boot-state file exceeds the 32,550-byte budget. PREDICTIONS is scanned, not loaded whole by boot; its 37,947-byte full file is counted in the ceiling and outside the heuristic. Weekday claim check, syntax compilation, 11 meaningful guard tests and diff whitespace check pass. Consumer scans found dated historical/context candidates, no certified stale consumer; WALTER receives a current-context packet because its in-flight context capture read the old page. Other desks retain file ownership. No auto-memory written.
