# FOMC 7/28-29 2026 — GRADED (Session 26, 2026-07-29 evening)

**Grades against:** `research/FOMC_FRAMEWORK_JUL28-29_2026.md` v1.1a (pre-registered 7/24, dates verified 7/24). Executed per the framework's own rule: **"Execute the tree on the night — do not improvise."** All facts below verified at primaries tonight (fleet was offline for the print itself — usage outage — so this is a same-night retrospective grade, not a live one; the tree was written and locked 5 days before data, which is what makes it gradeable at all).

**Primary sources pulled tonight:**
- Federal Reserve statement: federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm (fetched 2026-07-29)
- Chair Warsh press conference opening statement (PDF, federalreserve.gov/mediacenter/files/FOMCpresconf20260729.pdf; pdfminer-extracted — full text pulled, not a relay)
- HY OAS / CCC OAS / DGS10 / DFII10: FRED via `FORGE/tools/market-data/fetch.py` (BAMLH0A0HYM2, BAMLH0A3HYC, DGS10, DFII10)
- Market reaction (VIX close, SPX, Dow, 10Y intraday move): Yahoo Finance / Bloomberg / CNBC / CNN via WebSearch, 2026-07-29
- War/Saudi context: `AGENTS/BRENT/STATUS.md` (BRENT is domain owner; RED does not re-verify BRENT's oil-market primaries, only consumes the dated claim)

---

## 1. The facts, verified

**Decision:** 9-3 hold at 3.50-3.75%. Dissents: Hammack (Cleveland), Kashkari (Minneapolis), Logan (Dallas) — all three preferred +25bp. First 3-member unified-direction dissent since Sept 2016 [Bloomberg 7/29].

**Statement language (federalreserve.gov, verbatim):**
- *"Inflation remains elevated relative to the Committee's 2 percent goal, in part reflecting supply shocks that have driven price increases in certain sectors, **including energy**."*
- *"Job gains have kept pace with the workforce, and the unemployment rate has changed little."*
- *"The Committee will deliver price stability."*

**Presser opening statement (PDF, verbatim, relevant lines):**
- *"Job gains have kept pace with the workforce, and the unemployment rate has changed little. Inflation remains elevated relative to the Committee's 2 percent goal... There is no soft inflation target, there is no soft implicit target—not on this Committee's watch. There is only a target, and it is 2 percent."*
- *"The policy statement conveys just the facts. It's steering clear of forecasting..."* — confirms no-SEP-this-meeting framing (framework §LAB weighting note).
- Four questions the Committee "vigorously discussed" included: *"price increases arising from shocks"* incl. *"energy-supply disruptions"* — Q3 of 4, framed as an open question about whether shock-driven prices are a *"broader inflationary dynamic."*
- News-aggregated (not in the opening-statement PDF; presser Q&A not independently pulled tonight): Guha (Evercore ISI) reports Warsh said the Committee "may not be so reluctant to act" in September; markets priced **77% Sept-hike odds post-meeting** (up from ORACLE's pre-meeting 71.5% year-end base case) [financefeeds.com, Guha via search 7/29].

**Market reaction (close basis, 7/29):**
- SPX **7,316.15, −1.52%**; Dow **51,594.14, −1,153.18 (−2.19%)**, "worst decline since April 2025" [Yahoo Finance]
- **VIX closed 20.66, +2.45 (+13.45%)** [Yahoo Finance/Fool.com]
- 10Y yield **+7bp intraday to ~4.67%** [search-reported]; FRED DGS10 close not yet posted for 7/29 (last pull: 4.61 on 7/28) — the +7bp figure is a same-day media report, not yet FRED-confirmed
- 30Y yield **+12bp to 5.21%, a 19-year high** [search-reported]
- HY OAS: **281 (7/27) → 284 (7/28)** [FRED `BAMLH0A0HYM2` via fetch.py] — both readings **predate** the decision (7/29). No FRED print for 7/29 exists yet (posts next business day).
- CCC OAS: **1001 (7/27) → 1005 (7/28)** [FRED `BAMLH0A3HYC` via fetch.py] — **crossed WL-06 (CCC>1000, "2016-analog threshold," sustain=1) on 7/27**, both readings also predate the decision.
- Confound, same window: overnight 7/28→7/29, **US + Saudi forces struck Iran-backed sites in Iraq** after an IRGC missile launch at a US base in Jordan (7/28, 5:45pm ET) — BRENT's 7/29 STATUS calls this the point Saudi Arabia "moved from target to co-belligerent." Yahoo's own headline attributes the selloff to **"hawkish Fed AND increased Middle East tensions"** jointly.

---

## 2. SUBSTANCE axis — S1 CONFIRMED, both vintages

**Outcome = S1 (hawkish hold, hike-signaled).** Hold, zero dovish dissents, three unified hawkish dissents, "no soft target" rhetoric, statement explicitly names energy as an inflation driver rather than excluding it, and the forward read (per Guha, corroborated by the 71.5%→77% Sept-odds jump) sharpens to **September specifically** — exactly the registered S1 definition ("statement/presser points at Sep-Oct — v1.1 sharpens this to 'September specifically'").

| Vintage | S1 prior | Grade |
|---|:--:|---|
| v1.0 (7/24, T-4) | 52% | **CORRECT** — modal branch, highest of 5 |
| v1.1 (7/24 same day, amended pre-data) | 54% | **CORRECT** — modal branch, highest of 5 |

**The amendment itself is validated, not just the branch.** v1.1's two moves were S1 52→54 (+2) and S4 23→21 (−2), on the stated sequencing argument (the operative print is the *last* one before the *next* decision, not the next one the Fed sees — RED's rejection of CARL's inference, ML-RED-112). **S4 (hike now) did NOT occur** — the hold confirms the amendment's direction was right, not just its sign. Per Guard 5 ("grade the amendment separately so the re-weight is itself scored rather than quietly absorbed"): **the amendment gets its own correct grade, independent of S1's baseline correctness.**

**RED-20 GRADE: CORRECT (both v1.0 and v1.1).**

---

## 3. §L oil-language axis — L1 CONFIRMED; RED wins the CARL dispute

RED's tree: L1 (upside inflation risk) 42% modal, L2 (look-through) 30%, L3 (tax-on-households) 10%, L4 (absent/mixed) 18%. CARL had argued L2 could be modal at ~40%, above RED's 42-vs-30 ordering — RED explicitly flagged the disagreement as gradable ("Both priors are on the record; grade both").

**Outcome: L1.** The statement's "including energy" as a driver of elevated inflation, plus the presser's framing of energy-supply disruptions as an open question about "broader inflationary dynamic" (not excluded from the reaction function), is upside-inflation-risk language, not the 6/17 "look-through/stop the second-round effects" construction. No look-through language appears in either primary pulled tonight.

**GRADE: L1 CORRECT as modal — RED's 42-over-30 ordering beats CARL's L2-may-be-modal claim.** Caveat: full Q&A transcript wasn't independently pulled tonight (only the opening statement + statement text), so there is residual uncertainty about exactly how Warsh characterized oil under direct questioning; the *formal* statement text — arguably the more scored-worthy document — is unambiguous L1.

---

## 4. §LAB labor-language axis — LAB-a confirmed; the verbatim-staleness sub-test did NOT fire

RED/LABOR's tree: LAB-a (face-value) 70%, LAB-b (flow-structure-acknowledged) 25%, LAB-c (data-quality flag) 5%.

**Outcome: LAB-a.** Both the statement and presser opening say, near-identically, *"Job gains have kept pace with the workforce, and the unemployment rate has changed little."* No participation-rate, hiring-rate, or LT-unemployment caveat in either document pulled tonight. **GRADE: LAB-a CORRECT (70% prior, modal, adopted unmodified from LABOR).**

**RED's own overlay sub-test did NOT fire.** RED's adversarial addition (not LABOR's) asked whether the June minutes' now-superseded *"payroll gains had strengthened this year"* would be repeated **verbatim** — which would be a datable staleness marker. **It was not repeated verbatim.** Tonight's language is *"kept pace with the workforce,"* a materially weaker/more neutral claim than "strengthened," and arguably a quiet downgrade consistent with the 7/2 print's weakness (+57K, net −74K Apr/May revisions) even while staying face-value (no explicit acknowledgment of the flow-structure argument). **Honest read: LAB-a's substance is confirmed (face-value framing, no flow-structure caveat), but the specific verbatim-staleness conditional that would have made it a *scored* credibility datum did not trigger — the Committee revised the phrase rather than repeating stale text.** This is a genuine miss for RED's own added conditional, logged as such rather than papered over.

---

## 5. REACTION axis — the framework's own "bottom line" modal call was WRONG; R-B fires but is confounded

**Framework's stated bottom line (v1.1, written 7/24):** *"modal path is **S1×R-A** — a third hawkish-absorbed print."* This was RED's own registered expectation, informal but explicit.

**What happened: NOT absorbed.** VIX closed **20.66 (+13.45%)** — clears **R-B's** VIX>20 threshold outright. SPX −1.52%, Dow −2.19% (worst since April 2025 per one source). This is the **first non-absorbed FOMC print of the cycle** (6/17 was absorbed: VIX crushed to 17, HY tightened).

**But R-B is confounded, and Guard 3 says so on its own terms.** RED's framework pre-registered exactly this hazard: *"an Encelia/Layla sinking or Kharg event inside the FOMC window moves oil/War on its own axis — do not launder a war re-mark through an FOMC cell. Two events, two entries."* Tonight, the overnight US+Saudi strikes on Iran-backed sites in Iraq (following the 7/28 IRGC missile launch) is exactly such an event, landing inside the FOMC window. Yahoo's own coverage attributes the selloff to **both** causes jointly ("hawkish Fed and increased Middle East tensions"). **This is not resolvable with tonight's data** — there is no way to cleanly apportion the VIX spike / equity selloff between "the bond market reading the hold as behind the curve" and "a new direct-combatant escalation in the Gulf, overnight." Both are real, both landed the same 24 hours.

**R-C (rates-led selloff) narrowly missed on the letter:** the registered threshold is "10Y +10bp or more." The reported intraday move is **+7bp** — short of the letter, though the 30Y's +12bp to a 19-year high is directionally the same story on a metric the framework didn't name. Flagged, not scored as R-C.

**Attribution guard (Guard 1) applies to the credit leg specifically:** HY's 281/284 (7/27, 7/28) and CCC's 1001/1005 (7/27, 7/28) **both predate the 7/29 decision**. Per the framework's own rule — *"if HY>280 fires BEFORE the Fed decision, it is NOT an FOMC read; score it on the BDC/credit chain and do not double-count it in cell S×R-B"* — **the credit widening is NOT attributed to the FOMC print.** It is attributed to the same pre-existing war/oil-driven widening BRENT and LIQUID's surfaces have been carrying since the 7/23 spike. WL-06 (CCC>1000) is scored as its own fired gate on its own merits (§6 below), not as FOMC evidence.

**GRADE: the framework's explicit "S1×R-A modal" bottom-line call is WRONG.** R-B fires on the VIX leg alone (mechanically, on the letter), but the pre-registered conjunction payout for S1×R-B ("+2 confidence... Net-bear cap +3") is applied at a **haircut** in the re-mark below, specifically because Guard 3's own attribution problem is live and unresolved — RED will not bank the full conjunction on a confounded reaction. This is graded as a genuine miss on RED's own stated expectation, kept separate from the S-axis's correct call per Guard 4/5's explicit separate-axis discipline.

---

## 6. S3×R-D (the rates-arm kill) — confirmed NOT to have occurred

**S3 (dovish shift) did not occur** — the opposite: three unified hawkish dissents, zero dovish dissents, "no soft target," "will not waver." **R-D (relief rally) did not occur** — the opposite: yields rose intraday, VIX spiked, no TLT rally. **S3×R-D did not fire.**

Consequence: **TRY-FIRE-004 (30× TLT Sep-30 $77P) is NOT killed.** The BOND falsifier (KB-067) — "dovish repricing is what kills the rates arm, not oil-retrace" — did not trigger. If anything, tonight's realized move (yields up, not down) is directionally the position's own thesis working, though sizing/management is TERRY's call, not RED's to act on. Logged as confirmation the rates-arm survived its hardest pre-registered test this cycle.

---

## 7. Net grade summary

| Axis | Prior | Outcome | Grade |
|---|---|---|---|
| S-axis v1.0 (S1 52%) | modal | S1 realized | **CORRECT** |
| S-axis v1.1 (S1 54%, S4 21%) | modal, amended | S1 realized, S4 did not | **CORRECT — amendment itself validated** |
| §L oil-language (L1 42% vs CARL's L2-modal claim) | modal | L1 realized | **CORRECT — RED wins the CARL dispute** |
| §LAB labor-language (LAB-a 70%) | modal | LAB-a realized | **CORRECT on substance; overlay's verbatim-staleness sub-test did NOT fire (language revised, not repeated)** |
| Bottom-line reaction call (S1×R-A modal) | informal | R-B fired instead (VIX 20.66) | **WRONG — first non-absorbed print of the cycle, though confounded with a same-window war event (Guard 3)** |
| S3×R-D (rates-arm kill) | pre-registered falsifier | did not fire | **Correctly did not fire — TRY-FIRE-004 survives** |

**RED-20 workbook grade: CORRECT** (both vintages) on the gradable, formally-prior'd S-axis object. The reaction-axis miss is real but was never the scored object of RED-20 itself (RED-20's own Invalidation column: *"S3 or S4 landing = modal miss... reaction axis graded separately per framework"* — exactly what happened).
