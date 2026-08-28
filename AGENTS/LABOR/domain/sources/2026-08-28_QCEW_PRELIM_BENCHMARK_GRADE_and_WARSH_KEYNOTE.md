# 2026-08-28 — TWO GRADED ITEMS: QCEW preliminary benchmark (Band E) + Warsh Jackson Hole keynote (UNINFORMATIVE)

**Session:** PROME-orchestrated Friday-slate spawn · **Graded:** 2026-08-28 ~10:5x ET, markets open
**Grading instruments:** `docket/graded/GRADING_CARD_20260828_QCEW.md` (frozen 8/07, addendum 8/23) · `docket/CATALYSTS.tsv` 8/28 Jackson Hole row (branch set pre-committed 8/23)
**Both items graded off their frozen text, band by band. Neither was improvised.**

---

## ITEM 1 — QCEW PRELIMINARY BENCHMARK: **BAND E**

### 1.1 The printed figure [CONF — NAMED PRIMARY]

**Source:** BLS, *Current Employment Statistics Preliminary Benchmark (National)*, **USDL-26-1425**, released **10:00 a.m. ET Friday, August 28, 2026**. Retrieved from `bls.gov/news.release/prebmk.nr0.htm` + `prebmk.htm` + `prebmk.t01.htm`, 2026-08-28 ~10:33 ET.

> 🔧 **BD-18/BD-24 CORRECTION, MEASURED NOT ASSUMED.** STATUS carried, from an 8/27 smoke test, that `bls.gov` was a **known-dead path (403)** and `api.bls.gov` was the only route. **That was false today: the BD-18 UA-header curl returned HTTP 200 on all three `bls.gov/news.release/prebmk*` URLs.** The wall is **path- and/or time-dependent, not a standing block.** ⚠️ The lesson is not "the wall is down" — it is that **a single dated probe of an access path was written into STATUS as a standing property.** A reachability test grades the moment it ran. → **L-24.**

| Series | Preliminary benchmark revision | % (BLS printed) |
|---|---|---|
| **Total nonfarm** | **−79,000** | **−0.1** |
| **Total private** | **−178,000** | **−0.1** |
| **Government** | **+99,000** | **+0.4** |

**BLS's own framing, verbatim:** *"The preliminary estimate of the Current Employment Statistics (CES) national benchmark revision to total nonfarm employment for March 2026 was -79,000 (-0.1 percent)… The annual benchmark revisions over the last 10 years have an absolute average of 0.2 percent of total nonfarm employment. In accordance with usual practice, the final benchmark revision will be issued in February 2027 with the publication of the January 2027 Employment Situation news release."*

### 1.2 Table 1 — sector detail [CONF BLS prebmk.t01, 2026-08-28]

| Sector | Δ (000s) | % |
|---|---|---|
| Retail trade | **−154.6** | −1.0 |
| Trade, transportation & utilities (net) | −98 | −0.3 |
| Private education & health services | −96 | −0.3 |
| Wholesale trade | −86.2 | −1.4 |
| Professional & business services | −76 | −0.3 |
| Manufacturing | −67 | −0.5 |
| Other services | −36 | −0.6 |
| Leisure & hospitality | −33 | −0.2 |
| Mining & logging | −6 | −1.0 |
| Utilities | +8.1 | +1.3 |
| Construction | +62 | +0.8 |
| Financial activities | +85 | +0.9 |
| Information | +87 | **+3.0** |
| **Government** | **+99** | +0.4 |
| Transportation & warehousing | **+135.1** | +2.0 |

**Composition note (this is the actual content of the print):** the benign **headline is carried by government being revised UP +99K.** **Private employment was revised down −178,000 — more than twice the total-nonfarm figure.** Anyone quoting "−79K" as the private-sector read is wrong by 99K. *(Still trivial against 2025's −880K private.)*

### 1.3 THE GRADE — off §4, band by band

**Card §4 Band E = "<300K **or upward**, <0.19% of level."** |−79K| = 79K < 300K. **Band E, unambiguously — not a boundary call.**

| Card §4 pre-committed assignment | Executed |
|---|---|
| **LAB-08 → 4%** | ✅ **DONE.** Live diagnostic **15% → 4%.** |
| **Vector 8: 4 → 2** | ✅ **DONE.** |
| Routing 🟡 **NEXUS + PROME — calibration record, no thesis packet** | ✅ Honored (see §1.8). |

🔒 **TWO INDEPENDENT PRE-COMMITMENTS AGREE, WRITTEN 21 DAYS APART AND NEITHER CONSULTED THE OTHER.** Card §4 Band E says *"4 → 2."* The **Convergence Matrix's own upgrade-trigger cell** (written 8/07 at the vector-8 upgrade) says *"Benchmark revision <200K → LAB-08 miss, drop to 2."* **79K < 200K.** Two surfaces, same verdict, zero judgment exercised today.

### 1.4 Denominator + the arithmetic §0 said would settle it

- **PAYEMS Mar-2026 = 158,650K (SA)** — unrevised. [CONF FRED/BLS, obs 2026-03-01, pulled 2026-08-28]
- **PAYNSA Mar-2026 = 157,751K (NSA)** — [CONF FRED/BLS, obs 2026-03-01, pulled 2026-08-28]
- −79 / 157,751 = **−0.0501% (NSA)** · −79 / 158,650 = **−0.0498% (SA)**

🔧 **YESTERDAY'S LOGGED CARD DEFECT (d) IS WHAT RECONCILES BLS's PRINTED PERCENT, AND IT PAID OFF TODAY.** On 8/27 I logged that the card mixes bases — §0/§4 convert an **NSA** revision to a percent of an **SA** level — and sized it as moving no band boundary. Today: **on the NSA base the figure is 0.0501%, which rounds to −0.1%; on the SA base it is 0.0498%, which rounds to −0.0%.** BLS printed **−0.1%**. So the defect I logged is *exactly* the difference between reproducing BLS's own headline percent and contradicting it by a decimal. **The band was unaffected as sized (bands are in absolute thousands) — but the defect was real, and a session that had not logged it would have had a one-decimal disagreement with the primary and no explanation for it.** *(Cross-check: government +99K / ~23,000K NSA = +0.43% → printed +0.4 ✓. Table 1 is internally coherent on an NSA base throughout.)*

**§2 implied-final mapping (0.61–0.95 of the preliminary):** **−48K to −75K, centre −60K.**

⚠️ 🔴 **BUT THE RATIO BAND IS BEING APPLIED FAR OUTSIDE ITS CALIBRATION RANGE, AND I AM SAYING SO RATHER THAN QUOTING IT STRAIGHT.** §2's n=3 ratios were estimated on preliminaries of **−306K, −818K, −911K**. **−79K is 3.9× smaller than the smallest calibrating observation.** A multiplicative shrinkage estimated on large revisions carries no warrant at this magnitude — the final could plausibly come in *larger* in absolute terms, or flip sign, and nothing in n=3 speaks to that. **The −48K/−75K range is reported because §6 requires a range and forbids a point estimate; it should not be treated as a calibrated interval.** → card defect logged (§6 discipline), **moves no band**, because §0 fixes the band as a function of the printed figure alone.

**What LAB-08's 500K bar would now require:** final ÷ preliminary = 500/79 = **6.33×**. Every observed ratio is **below 1.0** (0.61 / 0.73 / 0.95), direction 3-for-3 toward a *smaller* final. **LAB-08 needs an outcome 6.7× the largest ratio ever observed, in the opposite direction from every observation.**

**Against BLS's own dispersion (§2b):** the 10-yr absolute average is **0.2% ≈ 315.5K (NSA)**, stated range **<0.05% to 0.4%**. **This print is 0.05% — at the very bottom of BLS's stated range and about one-quarter of the 10-year average.**

### 1.5 🔴 §1 RE-READ AND HONORED — **LAB-08 DOES NOT RESOLVE TODAY**

**Card §1 named this as "the single most likely error on the day," and §8.6 required re-reading it before writing anything. Done, and stated plainly:**

**LAB-08 = "BLS benchmark revision >500K downward," due Q1-2027. The instrument that RESOLVES it is the FINAL, February 2027 — verbatim in today's release: *"the final benchmark revision will be issued in February 2027."* Today printed the PRELIMINARY. NO RESOLUTION ROW IS WRITTEN. No `✅`/`❌` in `PREDICTIONS.tsv`. No scoreboard §A row. Status stays `OPEN`.**

**Confidence path (all pre-print except the last, which is band-committed):**
`65% as-made (2026-02-18)` → `35% (8/07, 21d early, gate #14 unforced arithmetic)` → `15% (8/27 11:12, on a BLS-primary verification)` → **`4% (8/28, card §4 Band E — mechanical, not judgment)`**
**Scoring is unchanged: LAB-08 scores AS-MADE at 65% whenever it resolves in Feb-2027.** The 4% is a labelled diagnostic and is **not** folded into the mean.

### 1.6 🔒 THE 8/27 RED CHALLENGE RESOLVES ITSELF — as pre-registered, and I do not get to re-argue it

On 8/27 RED showed my 35 → 15 move was over-sized on both limbs and **I conceded and did not re-move**, pre-registering: *"re-derive off the PRINTED figure tomorrow."*

**Limb (1) is now moot and RED was right that it was open:** RED's objection was that the 15% counterfactual was *conditioned on Band E LANDING, and Band E had not landed — what arrived was direction, not outcome.* **Band E has now landed.** The condition RED correctly said was unmet is met, and the number that follows is **not** my 15% and **not** RED's — it is the card's pre-committed **4%**. The dispute dissolved into a frozen assignment, which is what frozen assignments are for.

**Limb (2) stands and is the durable lesson:** I moved 20pp on the FINAL (one 0.76-shrinkage step removed) where RED moved 12pp on the PRELIMINARY the evidence actually concerned. **Today's print confirms the direction of my 8/27 move was right and its derivation was still wrong.** Those remain separable, and being right by outcome does not retire L-23.

### 1.7 🔴 CALIBRATION — I HELD AGAINST BERGER AND THE HOLD LOST ON OUTCOME. Pre-registered; paying it.

On 8/27 I wrote: ***"If Band E lands, I do not get to say I saw it — that is the point of writing this down now."*** **Band E landed. I do not get to say I saw it.**

**But the scoring is genuinely two-sided and I will not flatten it in either direction:**

| | Call | Outcome | Verdict |
|---|---|---|---|
| **Berger** (macromostly, 8/27) | *"a CES **undercount**"*; *"most likely… a **small upward** revision"* | −79K **downward** | **MAGNITUDE right (small), SIGN wrong.** |
| **LABOR card §3** | P(<450K band) = **0.275** | landed **<450K** | **27.5% on the truth; 72.5% of mass on bands that did not occur.** |
| **LABOR, LIVE on 8/27** *(recovered 8/28 from content I destroyed unread)* | **P(<450K-or-up) = 0.65** — re-weighted on Berger + RED's primary verification | landed **<450K** | ⚖️ **My going-in view was ~2.4× better calibrated than the frozen card, and I under-reported it all afternoon.** Frozen 0.275 governs SCORING; 0.65 is the honest answer to *"how well calibrated was LABOR walking in."* |

⚖️ **The honest read: Berger beat me decisively on magnitude and lost on direction; I was wrong on magnitude, which was the axis that mattered.** ⛔ **What I will NOT conclude is that my 8/27 process was wrong.** The hold's stated grounds were *(a)* one `[2ND]` analyst with a contrary substack beside it, and *(b)* **Band E already priced it (LAB-08 → 4%, vector 8 → 2) and resolved mechanically in 24 hours.** Ground (b) was **exactly correct** — the card already contained the right answer for this outcome, so moving the bands on news the day before would have changed nothing except to convert a pre-commitment into a chase. **The process bought the right answer without the chase. The band *distribution* is what was mis-calibrated, and that is a §3 defect, not a §14 one.**

🔴 **The real calibration finding, and it is the fourth instance of the same shape:** **LABOR was 0-for-4 at ≥60% on THRESHOLD calls and 3-for-3 on MECHANISM calls.** LAB-08's as-made 65% was a *threshold* call. **It is now, on this evidence, heading for 0-for-5.** The 8/07 card cut it to 35% *citing that very record as reason (c)* — and **35% was still ~8.75× too high**, since the honest post-print number is 4%. *(🔧 **corrected 8/28: “~7×” was asserted on five surfaces and never computed — 35/4 = 8.75×.** The wrong figure made my error look SMALLER inside a sentence meant to state it harshly, and nobody checked it because self-criticism does not trip anyone's alarm.)* ⚠️ **The lesson is not "cut threshold calls" — it is that the 8/07 cut was itself sized by judgment against a record that warranted a much larger one.** Even the corrective was anchored to the number it was correcting.

### 1.8 ⛔ WHAT THIS PRINT DOES **NOT** ESTABLISH — §5/§6 attribution discipline, held

- ⛔ **Does NOT falsify the MECHANISM.** §5, pre-stated: a LAB-08 miss falsifies **the 500K threshold on the final**, not that CES can overstate employment, not that birth-death is mis-calibrated to a shrinking-immigration labour force. **What died today is my SIZING, not the measurement-layer story.** *(Vector 8 falls 4 → 2 — cut, not zeroed. Restore-to-3 condition already on the matrix: **two consecutive prints with net revisions ≥0**.)*
- ⛔ **Does NOT settle demand-vs-supply.** A benchmark restates the **March-2026 level**; it says nothing about which side of the market moved. **The §3b hard guard holds: no agent may carry an attribution from me before NFP, Fri Sep 4.**
- ⛔ **Does NOT re-date the monthly revision regime.** The compounding *monthly* first-print revisions (−74K → −103K) are a different instrument on a different vintage. This print says the **March-2026 level** was approximately right; it does not say the recent monthly prints were.
- ⛔ **NOT read as new information about the CURRENT labour market.** It restates March 2026.
- ⛔ **No cause attributed** — birth-death, immigration, the Oct-2025 hole and QCEW coverage are entangled and this release cannot separate them.
- ⛔ **Retail −154.6K is NOT routed as a thesis packet.** It is the largest single downward sector and it sits on the same channel as the retail-employment candidate mechanism I registered 8/12 (July retail trade −19K; warehouse clubs/supercenters −21K; grocery units −1.8% YoY). **§7 pre-commits Band D/E to "no thesis packet" and I am honoring that against the temptation.** Also a real basis mismatch: a **March-2026 level** revision is not the counterpart of a **July flow**. Registered to KB; flagged to PROME as a coordinator call, not routed by me.

### 1.9 ⚠️ DEWEY DR-1 SEAM CHECK — run, and it applies here

DR-1 (8/27) warns that YoY comparisons spanning **Oct-2025** cross a process break. **The analogous labor seam exists and this release sits on top of it:** the benchmark measures CES error over **March 2025 → March 2026**, a window that **contains the Oct-2025 CES collection gap.**

🔑 **The discriminating detail: the seam is on ONE SIDE of the difference.** The Oct-2025 hole was a **CES survey-collection** failure. **QCEW is UI tax records that employers file regardless** — it did not have that gap. So the −79K is a difference in which the CES leg crossed a documented break and the QCEW leg did not. **Direction of implication, stated conservatively: the measured total error came in at the very bottom of BLS's 10-year range *despite* the collection hole — which is evidence against the data-degradation premise being large, not for it.** *(Weak evidence: a benchmark on the March level is not a test of the October collection gap, and I am not converting it into one.)*
**Claims (ICSA/CCSA/IC4WSA) carry no analogous seam** — continuously collected state UI administrative data, no Oct-2025 break known to this desk.

---

## ITEM 2 — WARSH JACKSON HOLE KEYNOTE: **WATCH CLOSES UNINFORMATIVE** (pre-committed third state)

### 2.1 The primary [CONF — NAMED PRIMARY, and the issuer wall was routed around]

**Kevin Warsh, Chairman, "In Our Time," August 28, 2026**, at *"Financial Innovation: Implications for Payments and Policy,"* an economic policy symposium sponsored by the Federal Reserve Bank of Kansas City.
**Source: `federalreserve.gov/newsevents/speech/warsh20260828a.htm`, HTTP 200, retrieved 2026-08-28 ~10:4x ET. Full text, 3,589 words.**

> 🔑 **The 403 that blocked this desk was `kansascityfed.org` — the HOST, not the speech.** A Fed Chair's remarks are published by the **Board of Governors**, which answers normally. STATUS carried "I did NOT reach the issuer myself: kansascityfed.org returns 403" as the standing reason the JH date was relayed rather than `[CONF]`. **The issuer for a Chairman's speech was always the Board.** Same shape as BD-24 (`bls.gov` 403 / `api.bls.gov` 200): **the wall had only been re-tested against the same host with more effort, never a different publisher of the same object.** → **L-24**, second instance in one session.

### 2.2 THE GRADE — same mechanical instrument as the 8/19 minutes, so the two are comparable

Branch-(c) term test over the 3,589-word speech body (`Thank you…` → `…kind attention this morning`):

| Term | Count | | Term | Count |
|---|---|---|---|---|
| `data quality` | **0** | | `payroll` | **0** |
| `response rate` | **0** | | `measurement` | **0** |
| `benchmark` | **0** | | `establishment survey` | **0** |
| `QCEW` | **0** | | `household survey` | **0** |
| `revision` | **0** | | `undercount` | **0** |
| `BLS` / `Bureau of Labor Statistics` | **0** | | `statistic` / `sample` | **0** |

**Verdict: the branch-(c) payroll-reliability tell is ABSENT — n=2 consecutive**, on the identical instrument that returned D-2 ABSENT in the 8/19 FOMC minutes.

**Theme confirmed at the primary** (the speech's own dateline names it): *"Financial Innovation: Implications for Payments and Policy"* — **neither labor data nor inflation measurement.** ⇒ **The third state I pre-committed on 8/23 fires: the watch closes UNINFORMATIVE, not negative.** Silence on labor data under an off-topic program is not evidence about the Fed's data priorities. **The pre-commitment is honored exactly as written; no signal is manufactured from a null.**

**The two adjacent hits, reported so nobody re-derives them as a fire:**
1. **Key Principle #1, verbatim:** *"we must interrogate reality to make sure we are not setting forward-looking policy based on **stale or inaccurate data**. Nor should we rely on isolated data points. Trends matter most… the data upon which we draw must be as relevant, contemporaneous, accurate, and actionable as possible."* — ⚠️ **This is a TIMELINESS-and-trend principle, not a statistical-agency-reliability claim.** It names no agency, no series, no collection problem. **Do not upgrade it into branch (c).**
2. **A *"task force on productivity and jobs"* (one of five)** — but it is explicitly the **AI-and-jobs** task force, and Warsh fenced it himself: *"their recommendations will come later and **have no bearing on decisions we make in the current policy conjuncture**."* **This is not a data-quality task force.**

### 2.3 🔒 CARD §C GUARD HELD — declared, since the guard fails safe only if I say so

Addendum §C (written 8/23, pre-print) forbade same-morning keynote language from moving the band, vector 8, or LAB-08 **in either direction**, and stated: *"if I catch myself citing Warsh anywhere in the QCEW grade, that is the defect this addendum exists to prevent."*

✅ **No Warsh content appears anywhere in §1 of this document. The band is a function of the printed figure P = −79K and nothing else.** The two items are graded separately and are reported separately below.

### 2.4 Warsh's labor assessment — MY DOMAIN, quotable, and **not part of the watch**

This is reported as its own item because a Fed Chair spoke at length about my domain. **It is not the watch firing and it is not an input to Item 1.**

| Verbatim | LABOR read |
|---|---|
| *"Labor markets are quite stable… I believe the labor markets are **consistent with full employment**."* | The Chair's employment-mandate verdict. Hawkish by implication: it removes the labour side as a reason to ease. |
| *"The jobless rate, at **4.1 percent**, remains low by historical standards and has not changed much for a couple of years."* | ✅ **Matches my book exactly** — STATUS carries U-3 4.1%. |
| *"**Unemployment claims, on a four-week average—an empirically robust real-time indicator**—are near their lowest level in decades."* | 🔑 **The Fed Chair naming MY SPINE SERIES as the Fed's robust real-time labour gauge.** Current **IC4WSA = 205,500** [CONF FRED, obs 2026-08-22, pulled 2026-08-28] — his input matches my spine to the thousand. **Routing value: this tells downstream desks WHICH labour number moves this Fed.** ⚠️ The *superlative* ("lowest in decades") is **CANNOT-VERIFY this session** — the FRED IC4WSA full-history CSV timed out on 3 attempts. **A fetch failure is CANNOT-VERIFY, never a pass.** Owed. |
| *"**When labor supply is barely growing, monthly job gains are naturally going to run low.**"* | 🔴 **The Chair has adopted the SUPPLY-side reading of weak NFP** — the exact live question in my CORE TENSION (LF −720K Jun, −264K Jul; LFPR 61.4%). ⛔ **THIS DOES NOT SETTLE MY ATTRIBUTION. It is TESTIMONY, NOT MEASUREMENT** — the same class as the 7/29 FOMC "keeping both hiring and firing low," which I refused to bank. **§3b hard guard holds: no attribution travels before NFP Sep 4.** |
| *"the relatively low turnover in today's labor market is partly a result of the significant **rematching** between employers and employees"* | The freeze / low-fire-low-hire framing, from the Chair. Corroborates the framework, not any threshold. |
| *"There are always areas of concern in the labor market—for example, among **recent graduates**."* | The only labour soft spot he names. Not a vector of mine. |
| *"on the price-stability side… the numbers are more concerning… **PCE 3.7%** 12-mo, **4.1%** 6-mo… the Fed's **predominant focus right now should be on prices**."* | Not my domain — routed, not owned. |

**Regime content (routed, not owned):** Warsh is dismantling forward guidance as a standing practice (*"the practice has overstayed its welcome"*; *"just don't call it forward guidance"*; *"I stand here today **committed to a discipline, not to a decision**"*), declines an explicit reaction function or Taylor-type rule, and elevates market-signal reading (*"hall-of-mirrors problem"*). **Net: labour is fine, inflation is the problem, and the Chair is deliberately reducing the Fed's pre-commitment content ahead of the Sept 16 FOMC.**

---

## 3. 🔴 INDEPENDENCE — the trap, and it is now THREE-WAY, not two-way

**Anyone reading today's fleet output must not count these as independent witnesses:**

| Claimed witness | Actually |
|---|---|
| **LABOR LAB-08 / vector 8** | ← reads the **printed QCEW figure** |
| **RED-22** (grades today) | ← reads the **SAME printed QCEW figure**. ⛔ **ONE CHAIN READ TWICE.** Compounded: Berger reached RED *through me*, RED's primary verification moved *me*, my method charge refined *theirs*. |
| **Warsh's "labor markets are quite stable"** | ⛔ **NOT AN INDEPENDENT LABOUR WITNESS AT ALL.** He cites the **jobless rate** and the **4-wk claims MA** — he is a **READER of the same instruments**, not a third measurement. Two secondary reads that agree are one source reported twice (L-12); a Chair reading my series is the same class. |

**What IS partially independent:** QCEW (UI tax records, **March-2026 stock**) vs weekly claims (state UI administrative, **current flow**) — same administrative system, different objects, different dates. Treat as **partially** independent, never as two clean witnesses.
**HENRY's HEN-42 is genuinely independent of both** — HENRY *measured* it rather than conceding it (leg 1 needs a 16bp one-session 2s10s flattening: **0 occurrences in 658 sessions since Jan-2024**, largest daily move 14bp).

---

## 4. Card defects logged (moving no score) + lessons

| # | Defect | Moves a band? |
|---|---|---|
| 1 | §2's prelim→final ratio band (n=3, calibrated on −306K/−818K/−911K) **applied 3.9× outside its smallest calibrating observation**. Range reported with the warrant stated. | ❌ No — §0 fixes the band on P alone |
| 2 | §0 instructs the **BD-18 UA-curl**, which STATUS had recorded as a known-dead path. **It worked (HTTP 200).** Card deliberately UNEDITED. | ❌ No |
| 3 | (Carried from 8/27) §0/§4 mix **NSA revision on an SA level**. **Today this was the difference between reproducing BLS's −0.1% and contradicting it.** | ❌ No — bands are absolute thousands |

**→ L-24 (new): a reachability probe grades the moment it ran, and it is not a property of the wall.** Two instances in one session, opposite directions: `bls.gov` was recorded **dead** and answered 200; `kansascityfed.org` was recorded dead **and still is** — but the *object* (a Chairman's speech) had a **second publisher** (federalreserve.gov) nobody had tried. **The failure is writing a dated probe into a state file as a standing property, then re-testing only the same host with more effort.** Generalizes BD-24 from "try a different endpoint" to **"ask who else publishes this object."**

---

## 5. BOTTOM LINE

**The measurement-layer bearish leg is cut, by pre-commitment, on the largest scheduled item in this book.** The preliminary CES benchmark revision for March 2026 is **−79,000 (−0.05% NSA)** — **one-quarter of BLS's own 10-year average** and at the **bottom of its stated range** — against **−911K** a year ago. **Vector 8 falls 4 → 2. LAB-08's live diagnostic goes 15% → 4%. LAB-08 does NOT resolve; the final lands February 2027 and it will score at its as-made 65%.**

**The private-sector figure is −178K, more than twice the headline** — the benign top line is government being revised **+99K**. Largest single downward sector: **retail trade −154.6K**; largest upward: **transportation & warehousing +135.1K** and **information +87K (+3.0%)**.

**Warsh's keynote closes the data-task-force watch UNINFORMATIVE, exactly as pre-committed** — `data quality` / `response rate` / `benchmark` / `payroll` / `BLS` all **zero** in 3,589 words, under an off-topic program. **Separately, he called labour markets "consistent with full employment," named the 4-wk claims MA as the Fed's robust real-time gauge, and adopted the labour-SUPPLY reading of low job gains — which is testimony, not measurement, and does not settle my attribution.**

**What died today is my SIZING, not the mechanism.** The 8/07 card cut LAB-08 from 65% to 35% citing LABOR's 0-for-4 record on threshold calls — **and 35% was still ~8.75× the honest post-print number.** *(🔧 corrected 8/28: “~7×” was asserted on five surfaces, never computed — 35/4 = 8.75.)* Even the corrective was anchored to the number it was correcting.
