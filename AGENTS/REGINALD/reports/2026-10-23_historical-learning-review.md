# REGINALD — Historical Evolution and Institutional Learning Review

**Commissioned by Will, 2026-10-23.** Written 2026-10-23 from 15:51 ET by REGINALD (Claude Code, Opus 5.5) in Will's session. Read-only Git inspection; no other agent launched; no thesis, prediction, threshold or instruction changed by this review.

**Grades used:** **DEMONSTRATED** (dated evidence supports it) · **SUGGESTIVE** (plausible, not established) · **UNPROVEN** (not enough evidence) · **CONTRADICTED** (the evidence argues against it).

**Method limits, stated first:**
- Most of what I know about my own past comes from my own files: changelogs, LESSONS and MEMORY. They were written by me and present my history favourably. Where it mattered I re-checked against commit contents, the prediction ledger and prices rather than my own summaries.
- Commit-type counts (§5) come from a keyword classifier on commit subjects. They are rough measures, not an audit.
- Price is not what my bank-ranking matrix claims to measure. I use it once, as a crude outside check, and say so.

---

## 1. Executive assessment

**Short answer: I have demonstrably become a better *researcher*: better sources, better-specified forecasts, and more willingness to retire my own claims. I have not demonstrated that I became a better *judge* of financial outcomes. And an increasing share of my effort goes to procedure.**

| Dimension | Grade | One-line basis |
|---|---|---|
| Source quality | **DEMONSTRATED** improvement | Feb: TV and press figures and screen ratios nobody could reproduce. Now: issuer 8-K accession numbers, FFIEC Call Reports, FRED vintages, two vendors cross-checked for settled prices |
| Forecast specification | **DEMONSTRATED** improvement | **9 of the 18** predictions registered on 2/23 were never graded on their own wording (7 retired as ungradeable or never measured, 1 void, 1 transferred to WAL). The five registered since July all name an instrument, a baseline, verdict bands and a resolve-by date |
| Willingness to retire my own thesis | **DEMONSTRATED** | Eight-channel thesis retired 8/13; matrix rebuilt 8/20 after its scores proved unreproducible; hidden-CRE flag retired with no successor |
| Calibration (forecast accuracy) | **UNPROVEN** | n = 8 graded REGINALD-owned forecasts in 9 months; Brier ≈ 0.19 vs 0.25 for a coin flip; one was registered after its outcome was public |
| Better prospective judgment | **UNPROVEN**, partly **CONTRADICTED** | The 8/20 vulnerability ranking: higher-risk names did *better* on price afterwards (Spearman +0.39); Q3 credit confirmed 1 of the top 3 clearly (FLG) and ran against another (AMTB) |
| Finding my own errors | **CONTRADICTED** as a claim of independence | Most consequential errors were caught by other desks, Will or auditors, not by me |
| Resuming after inactivity | **DEMONSTRATED** improvement | May–June gap: six fired items went unhandled for ~6 weeks. Today: boot plus three prints graded in about 25 minutes |
| Research capacity vs overhead | **SUGGESTIVE** deterioration | Process-only commits 4% → 21% of my commits (Feb → Oct); boot reading ~38 KB → ~160 KB; files 52 → 1,761 |

---

## 2. Historical timeline of major intellectual changes

**Pre-Git versus Git-verified.** The initial commit `1de9af3f3` (2026-02-01) imported a pre-built REGINALD: a skeleton self-dated **2026-01-25**, handoffs 001–005, and workbooks. Everything dated before 2/1 is a **documentary date I cannot verify**. Feb–Mar commits carry the author identity "Prome", so I cannot tell from Git which session did the work.

| Date (commit) | Change | Prompt | Substantive or procedural |
|---|---|---|---|
| ≤ 2026-01-25 (pre-Git; in `1de9af3f3`) | **Original thesis: "Hidden Leverage Concentration."** The transmission chain was Japan CLO selling (Norinchukin) → wider CLO spreads → regional-bank mark-to-market losses → deposit flight. Concentration example: Regions, $4.17B of CLOs. Confidence "Pattern 80% · Timing 65% · Magnitude 75%" | SAM network build | Substantive, but **unfalsifiable as stated**: the three confidence figures have no outcome attached |
| 2026-02-23 (`265a4e133`, `31528a8d3`, `73e3253a5`) | **Hidden CRE (Memo Item 3, RCON2746) screen:** OZK 37.6%, WAL 24.2%, EGBN 23.7%. "Position implications: KRE puts strengthened… SSB puts validated (cleanest book)". First prediction ledger, 18 rows | Own research | Substantive. The commit also edited CARL, HANS, HAWK and LABOR STATUS files: no file ownership yet |
| 2026-03-31 (`fc48cb9ef`, `246bda886`) | **Convergence thesis v1.0–v1.3:** "eight independent channels… all open… six at 🔴". The CLO/Japan chain is no longer the core; **I found no recorded falsification of it, it was simply dropped** | Accumulated news flow (fraud, private-credit gates, Hormuz, DOGE) | Substantive reframing; the "independence" was asserted, never tested |
| 2026-04-24 (`b04ddd314`), 2026-07-25 (`ed1ce777e`) | OZK, then WAL, promoted out of my directory into peer desks | Will | Organisational; it later produced the independent re-checks in Case 1 |
| **2026-06-08** (`30ed62025`) | **Cohort NCO decomposition:** classification rule **written before the data was pulled**; the result **inverted my working prior** (Hyp B → Hyp A). Cohort improvement was genuine; stress was concentrated | Own queued work | **Substantive. The first clear instance of a pre-registered test overturning my own view** |
| 2026-06-19 (LESSONS) | HY <260 exit downgraded to a review trigger; the trigger's anchor no longer matched the thesis | Caught by ORC | Substantive (trigger semantics) |
| 2026-07-21 | REG-26 (WAL Q2 surprise leg, 33%) **DISCONFIRMED** | WAL Q2 print | Graded outcome |
| 2026-07-30 | Bank-side HY attribution: wide HY is **BANK-ABSENT** on bank instruments | Own research | Substantive; still my standing read |
| **2026-08-07** (`19858b203`, `42c5ffb07`) | **OZK 37.6% reproduces at none of 18 quarters**; the screen's denominator was wrong | WAL and OZK spawns independently, plus DAEDALUS | Substantive correction, found by others |
| **2026-08-13** (`653cec3d7`, `a74579b73`, `f69ff2963`) | MI3 cohort re-run at the FFIEC primary (56/56 rows); legacy >20% flag **retired with no successor**; THESIS v1.4 retired; 9 predictions retired as ungradeable or never-instrumented | Will-ruled slate after the 8/7 refutation | Substantive (claims retired) and procedural (ledger honesty) |
| 2026-08-19 (`823fceb2b`, BOND) | FHLB system advances $810.7B at 6/30 found by BOND. I had retired REG-05 (>$700B, "jointly implausible", above an "~$675B SVB peak") **six days earlier without fetching the series** | BOND | Exposed an unfetched-data error |
| **2026-08-20** (`75f0dd18b`) | **Matrix v2.0:** the v1 scores could not be derived from v1's own method; EGBN's CRE concentration had been carried at 497–547%, about 2× too high; **the ranking inverted** (FLG last → 1st; CFG 3rd → last; WAL 1st → mid) | Will-directed rewrite | Substantive. The live claim "concentrated at FLG/EGBN/AMTB, not tier-wide" dates from here |
| 2026-09-26 (`fefe57f53`) → 2026-09-27 (`b93e3ac58`) | CRE top-3 = FLG, EGBN, OZK. I adopted CREED's FLG 17.5% correction (`d34018fe2`) and withdrew it ~20 h later | Will ask; FLG desk caught the adoption error | Substantive, with a cross-agent mistake |
| **2026-10-10** (`research/FHLB/reports/2026-10-10_…base_rate.md`) | REG-T-06 base-rated: **>$700B held in 12 of the last 26 quarters; peak $1,044.6B [3/31/23]**. Consequence downgraded to REVIEW (WQ-414, 10/11) | Own work after Will's question | Substantive self-correction of a mis-calibrated line |
| 2026-10-20 → 10-22 | Organisation cleanup; DEWEY coverage base rate (`2e364c21f`); REG-28/29/30 registered (`1649186e3`) | Will, DAEDALUS, DEWEY | Mostly procedural; the predictions are substantive |
| 2026-10-23 | 57-day test: KRE tracks the 10-year (−0.72% per +10bp), not HY (+0.02%) | PROME ask | Substantive, weak fit (R² 0.13) |

**Independence from PROME.** Early on, coordinator-identity commits wrote into other desks' files. Now I write only to my own tree and use packets. **But most methodology changes after June arrived as Will rulings, DAEDALUS or CATO audits, or peer catches.** By origin, my methodology is not independent. The research inside each change is mine. — **DEMONSTRATED** (commit subjects: "Will-ruled", "DAEDALUS D:L793", "ORC-caught", "RED CHG-RED-025").

---

## 3. Four case studies

**Candidates considered:** Brent $118–125 error (input error, small) · Hidden-CRE MI3 screen · eight-channel thesis → concentration · WAL bear mechanism (REG-20/24/25/26) · FHLB REG-04/05/REG-T-06 · CREED 17.5% adoption · DEWEY coverage base rate · lesson 45 (H.8 "not happening") · current REG-28/29/30 and BANK-ABSENT.

**Selection criteria:** each case had to (a) span a different period, (b) have dated evidence at both ends, and (c) together cover the four required types. I deliberately put two unflattering cases first. Rejected: Brent (an input error, not judgment); lesson 45 (small, already a LESSON).

### Case 1 — Hidden-CRE (MI3) screen, Feb → Aug. *Demonstrably incorrect.*

| Step | Record |
|---|---|
| **Original position (2/23, `265a4e133`)** | Banks hide CRE inside C&I. Ratio = Memo 3 ÷ C&I item 4; flag >20%. OZK 37.6% ("worse than Metropolitan"), WAL 24.2% "growing… only bank with increasing ratio", EGBN 23.7%. Concluded "KRE puts strengthened". By 3/31 it was channel 2 of the thesis |
| **Evidence available then** | The FFIEC definition of RCON2746 (balance sits in items 4 **and** 9) was public. Call Reports were public. Metropolitan Capital (failed 1/30) was **n = 1** |
| **Prediction** | REG-15: WAL ratio >30% (60%) · REG-17: a >20% bank has a capital event (50%) · REG-18: a Metropolitan-pattern failure replicates in H1 (45%) |
| **Subsequent evidence** | 8/7: OZK's Memo 3 sits entirely in item 9.a; **37.6% reproduces at none of 18 quarters**. WAL's 24.24% did reproduce, but the 12-quarter series never reached 25%, and "growing fastest" was a two-endpoint artifact. 8/13 re-run: on a uniform basis the >20% flag catches **0 of 14** banks; the basis choice **inverts the rank** |
| **Revision** | 8/13: flag retired, no successor registered (`a74579b73`); per-bank ratios DO-NOT-CITE; the "bucket migration" mechanism kept as a hypothesis |
| **Outcome (established)** | REG-18 **FAILED** (45%; no >20% bank failed in H1). REG-17 retired, its premise dissolved. REG-15 transferred to WAL. **The flagship "original discovery" was a measurement defect for ~5.5 months** |
| **Learning** | **DEMONSTRATED** at the instrument: the screen now reports both bases and dollars, and refuses unreproducible prior cells (`registry/NOTES.md` repro_guard). **Who caught it is the weak point:** two peer spawns and DAEDALUS did, not me. The same desk had positioned the ratio as its signature contribution for months without recomputing it on the definition |

### Case 2 — From "eight independent channels" to "concentrated, not tier-wide", Mar → Oct. *Material thesis change.*

| Step | Record |
|---|---|
| **Original position (3/31, `fc48cb9ef`)** | "Eight independent stress channels… all terminate at CRE-heavy regional balance sheets simultaneously… Six are at 🔴." Conviction HIGH after the Jefferies Q1 print, which the changelog called "Major validation… Exactly what we predicted". WAL price target $47–60 against Street ~$85–90 |
| **Evidence available then** | Real events: fraud losses, private-credit gates, oil shock, DOGE cuts. **But channel independence was never tested.** The Jefferies "validation" was $17M of MFS losses at a different firm, a weak test of a WAL thesis |
| **Prediction** | REG-08 KRE <$65 in H1 (45%) · REG-09 a Tier-2 bank misses Q1 (50%) · REG-13 ≥2 channels fire simultaneously (55% → 72%) · REG-20 WAL "major stress event" (82%) |
| **Subsequent evidence** | 6/8 cohort decomposition (pre-registered) → genuine improvement, not masking. Q1/Q2 prints benign at large caps. 8/20 matrix: the old ranking was unreproducible and inverted on rebuild |
| **Revision** | 6/8 (framing narrowed to WAL-specific) → 8/13 (thesis document retired) → 8/20 (live claim: concentrated at FLG/EGBN/AMTB; WAL and OZK mid-pack). **Each step was driven by evidence, not framework renaming** — the anti-pattern LESSONS records for WAL v2.0 |
| **Outcome (established)** | REG-08 **FAILED** (KRE low $62.62 on 3/18, never <$65 at H1 close; KRE $70.04 [2/2] → $72.41 [10/22]). REG-09 **FAILED** (none of VLY/CFG/ZION missed; "the miss was not close"). REG-13 **CONFIRMED** but near-unfalsifiable ("2+ channels fire" in a busy half-year). REG-20 **CONFIRMED-PARTIAL** (1 of 3 OR-legs: a 4.6% EPS miss). WAL $89.65 [2/2] → $76.67 [10/22], **−14.5%**: direction right, never near the $47–60 target. WAL's own Q3 mechanism tests failed (WAL-01 office classified $272.75M ≤ $500M; WAL-02 NCO 30bp ≤ 40bp). EGBN, "already in crisis" in March, is **+21%** since 2/2 |
| **Learning** | **DEMONSTRATED** at the process level: the narrower claim came from a pre-registered test, and the old one was retired rather than defended. **UNPROVEN** at the judgment level: the replacement ranking has not yet beaten a naive alternative (Case 4 and §5) |

### Case 3 — Research received from another specialist: CREED's FLG 17.5% (Sept) versus DEWEY's base rate (Oct). *Cross-agent.*

| Step | CREED 17.5% (9/26–27) | DEWEY coverage base rate (10/22) |
|---|---|---|
| **Original position** | My FLG NYC rent-regulated loss ratio was 20.45% | "Reserve coverage fell at 5 of 5 computed banks": I treated it as a deterioration signal |
| **Received** | CREED's "correction" to 17.5% | DEWEY: coverage decline plus rising NPLs preceded a material NCO rise in **2 of 10** episodes within 4 quarters, vs 25% unconditional (FDIC 1984–2026, $10–100B band) |
| **Incorporated** | **Adopted without recomputing** (`d34018fe2`, 9/26 20:22) | Written into STATUS's judgment the same afternoon; the coverage leg was "re-weighted" |
| **Change in judgment** | Figure changed, then withdrawn (`b93e3ac58`, 9/27 16:56). The correction had added charge-offs to a denominator that already contained them. **The FLG desk caught it, not me** | **No forecast moved.** REG-29 was drafted at 45% at 13:18 (`55bcf6317`); DEWEY delivered at 13:32 (`2e364c21f`); REG-29 was registered at 45% at 13:36 (`1649186e3`). The base rate changed the prose weight, not the number |
| **Beneficial?** | Net negative, reversed in ~20 h; it produced lesson 40 ("a correction gets the same recompute as the figure") | **UNPROVEN**; REG-29 resolves on Q4 prints (~late Jan 2027) |
| **Counterfactual** | I had the inputs myself; my own evidence pack labelled the $2,088M as pre-charge-off | Feasible for me from FDIC data, but I had not done it in nine months of citing coverage. **DEWEY supplied a missing base rate; that is real value** |

**Learning:** **DEMONSTRATED** that I absorb peer input quickly. **CONTRADICTED** that I always verify it before adopting it (17.5%). On 10/22 I applied DEWEY's caution in prose while leaving the forecast untouched within four minutes of receiving it. That is defensible, since REG-29's lift was appraisal-driven, not coverage-driven. But I did not write that reasoning down at the time.

### Case 4 — Current, unresolved: "concentrated, not tier-wide" + BANK-ABSENT + REG-28/29/30.

| Step | Record |
|---|---|
| **Position now** | Severity concentrated at CRE-heavy names. Wide HY (340bp [10/22]) is not reaching bank instruments (BANK-ABSENT ~0.7). REG-28 EGBN extend-not-exit 65% · REG-29 ≥4 of 6 Q4 NCO rises 45% · REG-30 VLY nonaccrual ≥ $511.4M 60% |
| **Evidence available** | Q3 releases: problem loans up at 7 of 10 names read, coverage down at 6 of 8. DEWEY's base rate: coverage decline is a weak near-term predictor. My 57-day test: KRE follows the 10-year, not HY (R² 0.13) |
| **Prediction quality** | All three rows name an instrument, a frozen baseline, MECE bands and an IMMOVABLE resolve-by. **Base rates were computed before marking** (REG-28 74% binomial → marked 65%; REG-29 34% → 45%; REG-30 ~75% → 60%) |
| **Prospective test of the 8/20 ranking (outside check)** | Total return 8/20 → 10/22 against the v2.0 score: **Spearman +0.39**, i.e. higher "vulnerability" went with *better* returns. FLG (6) −15.1% fits; EGBN (5) +18.5% and AMTB (5) +4.3% do not; CFG (0) −6.4% and HBAN (0) −7.0% do not. Price is not the matrix's target, so this is a warning, not a refutation. **Q3 credit:** FLG worsened; EGBN mixed (a $56.0M nonaccrual, but the stock rose 15.6% on the print); AMTB improved (classified −22%) |
| **Outcome** | **Cannot yet be established.** REG-28/29/30 resolve Jan–Mar 2027; L180 breadth at the 11/07 Call Report run |
| **Learning to date** | The forecasts are much better specified than in February (**DEMONSTRATED**). Whether they are more accurate is **UNPROVEN**; and the current ranking has weak outside support so far |

---

## 4. Cross-agent learning assessment

| Peer, event | Made available | Actually received | Incorporated | Change in judgment | Evidence of benefit | Could I have found it alone? |
|---|---|---|---|---|---|---|
| **WAL + OZK spawns, DAEDALUS — MI3 (8/7)** | Primary-source recomputation | Yes | Yes (8/13 re-run) | **Large**: signature metric retired | **DEMONSTRATED**: false positives removed | Yes in principle (public FFIEC data, same JWT); **in practice I did not for 5.5 months** |
| **BOND — FHLB $810.7B (8/19)** | Q2 combined financial report | Yes | Yes → REG-T-06 instrumented; base-rated 10/10 | Moderate: a dormant series became a live line, then was re-scaled to REVIEW | **DEMONSTRATED** correction of my "$675B peak" claim (true peak $1,044.6B) | Yes; my ledger itself recorded the series as "public-and-unfetched" |
| **CREED — FLG 17.5% (9/26)** | A recomputed loss ratio | Yes | Yes, wrongly | Reversed | **Negative**, ~20 h | Yes; my own pack had the right label |
| **CREED — CRE refi read (10/22)** | Rate shock, not credit; CMBS spreads flat through 10/16 | Yes | Yes (STATUS evidence limits; supports today's 10-year finding) | Small: strengthened BANK-ABSENT | **UNPROVEN** | Partly; CREED owns Trepp/CMBS instruments I don't hold |
| **DEWEY — coverage base rate (10/22)** | FDIC 1984–2026 episode study | Yes | Prose only | Weight on one leg; **no forecast moved** | **UNPROVEN** (resolves ~Jan 2027) | Feasible; not done in 9 months |
| **TERRY — mechanism ask (8/20)** | Pre-registered elimination test | Yes | Answered with a measured null | None (correctly) | Neutral | — |
| **WALTER — signal routing (all time)** | 513 BOARD dispositions | Yes | 122 INTEGRATED (24%), 331 INFO_ONLY (65%) | Mostly none | **SUGGESTIVE** low yield per item, but routing occasionally delivers the decisive item (e.g. 10/22 H.4.1) | Mostly yes; WALTER saves search time rather than adding insight |
| **GIBBS — AXP (10/23)** | Large-bank census | Yes | Read | None | None | n/a; context only |
| **BROCK — BRK-31 falsifier (7/25)** | A test that grades on my bank prints | Yes | Carried on ROADMAP | None yet | **UNPROVEN** | n/a |

**Assessment:**
- **DEMONSTRATED:** the most valuable cross-agent contribution has been *error detection* (MI3, FHLB, FLG 17.5%, a KB date inversion caught by WAL), not new insight.
- **SUGGESTIVE:** the fleet functions as my reviewer more than as my source.
- **CONTRADICTED** that a received packet equals learning: of the eight examples above, four changed a judgment, one of those changes was wrong, and **none has yet been shown to improve a forecast outcome**.
- **Counterfactual:** nearly every peer insight was obtainable from data I already had access to. **The scarce resource was attention and recomputation, not data.**

---

## 5. Early versus current REGINALD

Representative outputs compared: early — `265a4e133` (2/23 hidden-CRE discovery) and the 3/31 thesis (`fc48cb9ef`); current — `reports/2026-10-22_catchup/REPORT.md` and `reports/2026-10-23_boot/REPORT.md`.

| Dimension | Early (Feb–Apr) | Current (Oct) | Grade |
|---|---|---|---|
| **Source quality** | "Chicago 70–94% discounts confirmed (Fox Business)"; screen ratios with no basis; FHLB "$480B (est)" never refreshed (actual Q4-25 was $677B) | 8-K accession numbers, FFIEC primaries, FRED vintages, two vendors agreeing on settled prices; SECONDARY labelled | **DEMONSTRATED** improvement |
| **Financial reasoning** | Every finding pointed the same way ("KRE puts strengthened… SSB puts validated (cleanest book)"); channel "independence" asserted | Mechanism separated from level (e.g. "provision funded charge-offs, did not build the reserve"); numerator/denominator effects named (FLG coverage low from the NAL denominator) | **DEMONSTRATED** improvement |
| **Calibration / falsification** | 9 of 18 Feb predictions never graded on their wording (7 ungradeable or unmeasured, 1 void, 1 transferred); REG-10 registered after its outcome; three-number "confidence" with no outcome | Instrument, baseline, MECE bands, base rate before the mark, IMMOVABLE resolve-by | **DEMONSTRATED** in specification; **UNPROVEN** in accuracy (n = 8 graded, Brier ≈ 0.19) |
| **Recognition of uncertainty** | Conviction HIGH, "inevitability" language ("the thesis has a deadline") | "Cannot be established", "R² 0.13 weak", UNKNOWN cells kept | **DEMONSTRATED** improvement; sometimes excessive (caveat density can bury the point) |
| **Identification of important risks** | Broad and loud; caught real themes (fraud, private credit, NDFI) | Narrower and better measured; **blind spot named**: every instrument measures credit or a closed quarter | **SUGGESTIVE**. Early breadth found real themes; current narrowness may miss non-credit moves (my own standing caveat) |
| **Resistance to confirmation bias** | Weak: the Jefferies "major validation"; analyst downgrades read as "Street catching up" | Stronger: pre-registered frames (6/8, FL frame, WQ-318); "no candidate" recorded; WAL bear tests graded against WAL | **DEMONSTRATED** improvement |
| **Research efficiency** | Errors stayed live for months (MI3 5.5 mo; FHLB 6 mo unfetched; REG-09 graded 4 months late) | Same-day grading of prints; but process-only commits **4% (Feb) → 21% (Oct)**; boot reading **~38 KB → ~160 KB**; files **52 → 1,761**; charter **6.6 KB → 40.4 KB (9/15) → 25.0 KB** | **Mixed**: faster on the core loop, heavier around it |
| **Ability to resume** | 4/16 "pre-crash recovery" commit; 5/21–6/2 gap left six fired items for the 7/17 audit | boot.py lists unprocessed lanes, resolve-by dates and ladders; today's boot plus three print grades took ~25 min | **DEMONSTRATED** improvement |

**Does procedure crowd out research? SUGGESTIVE yes, with a counterpoint.**
- In today's session, the research (three print grades plus the HY/10-year test) took about as much time as the obligatory write-back: BOARD_LOG, filing, receipts, NEXUS pin, MEMORY/ROADMAP, closeout checks.
- Counterpoint: some of that procedure caught real errors. Today I caught a wrong FLG count before commit. The settled-bar filter has prevented intraday-as-close errors.
- What I cannot show is that the **marginal** procedure added since September catches anything. No catch-rate is measured per control.

---

## 6. Demonstrated improvements

1. **Primary sourcing and reproducibility** (§5 row 1; MI3 re-run 56/56 rows at FFIEC; matrix v2.0 validated EGBN 258.2% against its disclosed 267.6% before use).
2. **Pre-registration that can overturn me:** 6/8 Hyp A inverted my prior; the FL frame and WQ-318 rows are graded on frozen letters; today AMTB graded HOLDS against a line set on 9/24.
3. **Forecast specification:** from 9 of 18 February rows never graded on their wording to 0 of 5 rows since July lacking an instrument.
4. **Retiring claims rather than defending them:** thesis v1.4 (8/13), TIMELINE (8/20), the MI3 flag, the HY<260 auto-exit, the FHLB "crisis level" (10/10).
5. **Resumption:** fired items no longer wait weeks.

## 7. Persistent weaknesses and regressions

1. **Error detection is mostly external** (**DEMONSTRATED**). Catches by WAL/OZK spawns, DAEDALUS, ORC, RED, the FLG desk, WAL (KB date inversion), Will (lesson 45) and BOND outnumber my own catches among the consequential errors I reviewed.
2. **Asserting without fetching** recurs across eras (**DEMONSTRATED**): FHLB "$480B est" (Feb); REG-05's "jointly implausible… ~$675B peak" written on 8/13 with zero pulls; lesson 45 (10/10, a quarterly print used without the weekly one). Today I typed a time stamp from narrative rather than the clock.
3. **Judgment accuracy not shown** (**UNPROVEN**): eight graded forecasts in nine months is too few to measure calibration. The v2.0 ranking has an adverse first outside check.
4. **Procedural growth** (**SUGGESTIVE** regression): +17 points of process-only commit share; ~4× boot reading; caveat density in current reports sometimes obscures the finding.
5. **Peer input adopted without recompute** at least once (**DEMONSTRATED**, 17.5%), despite earlier lessons (LESSONS "Verify Agent Data").
6. **Dropped theses leave no grade:** the original CLO/Japan transmission chain disappeared from the thesis without a recorded test (**DEMONSTRATED** absence in the changelog summary).

## 8. What cannot yet be established

- Whether current forecasts are better calibrated than early ones: n is too small, and REG-28/29/30 resolve Jan–Mar 2027.
- Whether the concentration claim is right in outcome terms. The L180 breadth test (11/07) and the Q4 prints decide it. REG-03 (recognition wave, 70%, registered 2/23) is still open to ~Mar 2027.
- Whether the matrix predicts next-quarter credit deterioration. It has never been tested against the next quarter's nonaccrual or NCO changes.
- Whether DEWEY's base rate or today's 10-year finding improves any decision.
- How much of the improvement is mine versus the auditing system around me. On this record I cannot separate them, and the honest reading is that much of it is the system's.

## 9. Three recommendations (for Will to decide; none executed here)

1. **Give judgment a denominator.** Before each bank print, write one short dated expectation per name on the line that matters (e.g. "FLG NAL ≥ $2,800M"), grade it at the print, and count hits each quarter. That produces ~15–30 gradeable calls a quarter instead of ~2, using frames I already write. Without it, "better judgment" will stay UNPROVEN indefinitely.
2. **Test the matrix before trusting its ranking.** At the 11/07 re-score, check whether the 8/20 scores predicted the Q2 → Q3 change in nonaccruals and NCOs across the 14 banks. That data will exist; it needs no new instrument. If the scores don't predict, say so and rank on the raw measures instead.
3. **Cut procedure by measured catch-rate, not by bytes.** For each recurring closeout or boot step, record over a month whether it ever caught something. Retire the steps that catch nothing. The pending charter trim is a start, but byte trims alone have not reduced the ~160 KB boot load or the 21% process share.

---

## Final conclusion

**Has REGINALD demonstrably become a better financial researcher since its earliest preserved records?**

**Yes, in method — DEMONSTRATED. Not yet in judgment — UNPROVEN.**

**Improved, with evidence:**
- **Sourcing:** primary filings with accession numbers, not press figures or unreproducible ratios.
- **Forecast design:** half of the February forecasts were never graded on their own wording; none since July lacks an instrument, a baseline or a resolve-by.
- **Willingness to be wrong in public:** the eight-channel thesis, the MI3 flag and the FHLB "crisis" line were each retired on evidence (8/13, 8/20, 10/10).
- **Testing my own priors:** pre-registered tests now sometimes overturn me (6/8 cohort decomposition; today's 10-year test).
- **Resuming after gaps:** boot plus three print grades in about 25 minutes, versus six fired items left for six weeks in May–June.

**Not demonstrated:**
- That my forecasts are more accurate. Eight graded calls, Brier ≈ 0.19, one registered after its outcome.
- That my current ranking of vulnerable banks has predictive power. The first outside check runs the wrong way.
- That I find my own mistakes. Mostly others found them.

**Probable regression:** a growing share of my effort goes to maintaining the system rather than to research.

The improvements are real but procedural and epistemic. The financial-judgment payoff is untested so far, and on the few outcomes available it is not yet visible.

*Evidence receipts: commits cited inline; `workbook/PREDICTIONS.tsv` (REG-01–30); `../WAL/workbook/PREDICTIONS.tsv` (WAL-01/02); prices via yfinance (adjusted for the 8/20 → 10/22 returns, unadjusted for the Feb → Oct levels), retrieved 2026-10-23 15:5x ET; commit classifier and size measurements run in this session (Bash output, not saved).*

---

## ADDENDUM — 2026-10-23 16:1x ET: two forecasts were graded wrongly, and this review accepted both

**Prompt:** an outside review Will passed on at 16:07 ET flagged REG-08. I re-checked it, then re-checked the other seven graded rows against their original wording. **The body of this report above is left as written; this addendum supersedes its Brier figure and the REG-08 line in Case 2.** No ledger row has been changed (Will's decision, below).

| Row | Original wording (first registered `1c0b3d0cb`, 2026-02-16) | Ledger grade | What the record shows | Correct grade on the wording |
|---|---|---|---|---|
| **REG-08** | "KRE breaks below $65", H1 2026, 45% | FROZEN-FAILED (6/26–6/30, `2da627b87`): "KRE never broke $65"; "invalidation met (held >$70 through Q2)" | **17 closes below $65, 3/6 → 3/30**, low close **$62.62 [3/18]** (Yahoo daily). My own STATUS recorded it at the time: **$63.98** (commit `f0f13fb39`, 3/13) and **$63.67 [3/27]** (`b4db1e78e`). The stated invalidation was false too: **Q2 low close $65.85 [4/1]**, not "held >$70". Nasdaq's history API returned no rows for March, so the second source is my contemporaneous STATUS plus the outside reviewer's financecharts.com | **CONFIRMED** |
| **REG-10** | "PSEC cuts dividend in 2026", 65% | FAILED, graded 2026-02-10 on PSEC maintaining in February | **PSEC cut its monthly distribution from $0.045 to $0.0350, starting May 2026** (8-K acc 0001287032-26-000165, filed 5/7/2026, EX-99 release; prior $0.045 per Yahoo dividend history). The February grade closed a full-year window after one month | **CONFIRMED** (the row was registered after the February decision; that defect stays noted) |
| REG-09 | Tier-2 bank misses Q1 | FAILED | Not re-verified this session (needs consensus EPS) | unverified |
| REG-11 | A major BDC cuts in H1 | CONFIRMED | FSK $0.70 → $0.48 (ex 3/18); TCPC $0.25 → $0.17 (ex 3/17), Yahoo | CONFIRMED (re-verified) |
| REG-13 | ≥2 channels fire simultaneously | CONFIRMED | Judgment-graded; no objective instrument | not objectively gradeable |
| REG-18 | A >20% MI3 bank fails in H1 | FROZEN-FAILED | **Not checked against the H1 failures**: Community Bank & Trust – West Georgia failed 5/1; my own failures list says "not worked by this desk" | unverified |
| REG-20 | WAL stress event (miss, raise or regulatory action) | CONFIRMED | Q1 EPS $1.65 vs $1.73 consensus = one OR-leg met | CONFIRMED |
| REG-26 | WAL Q2 surprise leg | DISCONFIRMED | 37bp, loan to nonaccrual; clear | DISCONFIRMED |

**Rebuilt Brier score** (lower is better; coin flip 0.25):
- All 8 rows, with REG-08 and REG-10 regraded: **0.162** (was reported above as ≈ 0.19).
- The 5 rows that are objectively graded and re-verified (REG-08, 10, 11, 20, 26): **0.154**.
- **Still n ≤ 8. Calibration stays UNPROVEN.** The corrected number looks better, and that is exactly why it should not be trusted as evidence of skill.

**What this changes in the review's conclusions:**
- **The bigger finding is the grading failure, not the score.** Both errors went the same way: a TRUE forecast graded FAILED by checking at a convenient moment (the end of the period; the first dividend decision) instead of against the wording. Both survived the 7/10 staleness sweep, the 8/13 expiry sweep, a CATO census and this review.
- **This review repeated the error.** Case 2 printed the $62.62 March low beside "REG-08 FAILED" and did not notice the contradiction. That is a direct counterexample to §1's "willingness to be wrong — DEMONSTRATED": it was demonstrated for theses, not for grades.
- **Revised grade: "Forecast grading integrity" — CONTRADICTED** (2 of 8 graded rows wrong; 2 more unverified). Add to §7 as weakness 7.
- **Recommendation 1 stands, with one addition:** a grade is written only from the forecast's own wording, quoted beside the evidence, by a reader other than the forecaster.

**Owed to Will (not done):** correcting REG-08 and REG-10 in `workbook/PREDICTIONS.tsv`. This review's scope forbids changing original forecast records, and ledger corrections go through PROME. The original FAILED grades would be preserved; a correction would be appended.

---

## ADDENDUM 2 — 2026-10-23 16:2x ET: outside review points 2–3 adjudicated (no live method or ledger changed)

### Point 2 — the matrix's reserve-coverage point. **The reviewer is right; my stated justification is wrong.**
`BANK_EXPOSURE_MATRIX.md:37–38` adds 1 point when ACL/nonaccrual < 100%, "not a judgment call… <100% means the reserve is arithmetically insufficient for loans already on nonaccrual". **That is false.**
- An allowance estimates *expected loss*, net of collateral and recoveries. It is not meant to equal the balance of the problem loans.
- Nonaccrual balances are often already written down by partial charge-offs (FLG: $348M taken on the rent-regulated nonaccrual book since Jan 2024).
- My own evidence contradicts the claim. The 10/22 appraisal-discount test found realized resolution haircuts of ~13–22%. FLG's recognised loss is 20.7% of original balance. Reserving 100% of nonaccruals would mean expecting a total loss.
- **Graded: CONTRADICTED as "arithmetic"; UNPROVEN as a warning signal.** The 100% line is a hypothesis with no base rate.

What the point changes (scores at 8/20):

| | FLG | EGBN | AMTB | VLY | WAL | BKU | others |
|---|---|---|---|---|---|---|---|
| v2.0 | 6 | 5 | 5 | 3 | 2 | 2 | unchanged |
| without the coverage point | 5 | 4 | 4 | 3 | **1** | **1** | unchanged |

- **The top three survive without it** (it adds to names already high on the nonaccrual band, which partly double-counts: high nonaccrual mechanically lowers coverage).
- It moves only WAL and BKU.
- The matrix's sentence "that is the single most decision-relevant column" (§2) is **overstated**.

Crude outside check (8/20 → 10/22 total return, 14 banks; Spearman, where negative = riskier score went with worse returns, the direction a vulnerability rank should show):

| Ranking | Spearman |
|---|---|
| v2.0 | +0.39 |
| v2.0 without the coverage point | +0.48 |
| Simple baseline: Q2 nonaccrual rate only | −0.05 |

**None works on price, and price is not the matrix's target.** This is not the test; it only shows that the coverage point does not rescue the ranking on the one outside check available.

### Point 3 — Brier recalculation. **The reviewer's arithmetic is right; one premise needs updating.**
- 0.187 / 0.154 / 0.168 all reproduce exactly.
- The reviewer is right that flipping REG-08 to success *worsens* its contribution (a 45% call on an event that happened: 0.2025 → 0.3025). **My first addendum's 0.162 improved only because of REG-10, not REG-08**, and that addendum did not say so.
- **Updated premise:** REG-10 should not be excluded as "registered after its outcome". It was registered on 2/16, after PSEC's *February* hold. But its wording covers all of 2026, and the resolving event (the May cut, 8-K acc 0001287032-26-000165) came three months *after* registration. It was a real forecast; what was wrong was the February FAILED grade.

| Variant | n | Brier |
|---|---|---|
| Ledger as written | 8 | 0.187 |
| REG-08 corrected only | 8 | 0.200 |
| REG-08 and REG-10 corrected | 8 | 0.162 |
| Reviewer: REG-10 excluded, REG-08 corrected | 7 | 0.168 |
| Only objectively graded and re-verified rows (REG-08, 10, 11, 20, 26), corrected | 5 | 0.154 |

**Honest statement: somewhere between 0.15 and 0.20 depending on defensible choices, on 5–8 forecasts. That is not evidence of skill.** Agreed with the reviewer.

### On the recommendations (reviewer amendments accepted in substance)
- **More predictions:** one or two consequential, pre-registered expectations per bank print, each with a baseline. Keep credit, earnings and price forecasts separate. Do not manufacture volume.
- **Ranking test (highest value):** keep the 8/20 scores frozen. At the 11/07 Call Report run, test v2.0, v2.0 without the coverage point, and simple baselines (prior nonaccrual rate; prior quarter's nonaccrual change) against the Q2 → Q3 change in nonaccrual (`RCON1403`) and Q3 NCO. ⚠️ **Contamination:** I have already read Q3 *releases* for 13 of the 14 names (all but SBCF). The test is mechanical, so freezing its exact computation *before* 11/07 is what keeps it honest. Not frozen here; it needs Will's go-ahead.
- **Overhead:** for each control, record its cost, what it catches, whether another control catches the same thing, and how bad a miss would be, then remove redundancy. That replaces my "retire if it caught nothing in a month", which would remove rare-but-severe guards.
