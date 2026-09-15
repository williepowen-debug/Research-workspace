# SAM CHANGELOG

Tracks all changes to THESIS.md and TIMELINE.md. Reverse chronological. Each entry documents what changed, why, and the old → new view. This is the audit trail.

**Versioning convention:**
- THESIS: `vX.Y` — major (X) = structural thesis change (new channel, thesis break, conviction reversal). Minor (Y) = refinement (updated probability, new evidence for existing view, threshold adjustment).
- TIMELINE: not versioned numerically — entries are dated. Events are marked RESOLVED with outcomes when they pass.

---

## 2026-09-10 (ET) — Boot + catch-up; oil re-prices the differential; no thesis version or grade change

- **THESIS:** v1.7 unchanged. No successor, no re-pencil, no route re-armed. The Sep-1 asymmetry (surprise HOLD = larger, yen-negative move) is reaffirmed, not re-marked. **New observation, not a view change:** the BOJ is 98% priced to hike Sep-18 and the yen weakened anyway — the differential is widening on the U.S. leg faster than the hike closes it.
- **TIMELINE:** added the 2026-09-10 (ET) block. No branch point resolved; no forward view altered.
- **STATUS:** header/session block rewritten (prior 9/10-JST and 9/9 blocks compressed to pointers); market table to Sep-10 16:0x UTC clocks; intervention paragraph closes the Sep-10 leg; thresholds, watch rows and SAM-28/31/33 notes refreshed. Two compression passes on the 8/7 frame-break and durable-reference paragraphs recovered only ~140 B — **the file is dense, not bloated; it passes the 32,550 B binding cap at 28,292 B but a real reduction needs a hot/cold split, flagged not improvised.**
- **PREDICTIONS:** none graded; scoreboard unchanged (16/14/1/3 OPEN). **SAM-28** — the named oil-re-escalation route is firing as an event and pushing FXY the *wrong way* (FXY −0.40% on a +5.6% Brent day); recorded so it is not later mis-scored as un-fired. **SAM-31** — S&P −0.58%, VIX 17.60 (+6.9%), yen *weakened* 0.6%: evidence against the row, but not the genuine VIX-spike regime its own terms require; logged, no numeric VIX bar invented. **SAM-33** — unchanged; next check the Sep-16 25Y+ operation date.
- **Data closed at primaries:** BOJ Sep-10 provisional (`jx20260910.xlsx`, own pull) — fiscal +¥340B vs +¥220B projection, residual +¥120B, **no yen-buying signature** (net supply, wrong direction); Totan chart Sep-10 11:15 JST visually reviewed → `workbook/boj_ois_reviews/2026-09-10T1115-JST.json`, 5 rows ingested to `BOJ_MEETING_OIS.tsv`, **September 98% unchanged**.
- **Calibration guard recorded, not acted on:** the +5.5% oil-in-yen print is the shape of **SAM-15 (@80%, FAILED)**; the inversion that killed it still holds (July CA +¥2,988.9B, primary income +¥4,289.6B, goods only −¥399.9B). Next honest test = August trade balance Sep-16, read on crude **volume**.
- **Docket:** CATALYSTS/CALENDAR — resolved Sep-10 row pruned/marked; **Sep-16 25Y+ BOJ operation date added as a registered SAM-33 schedule check** (method KB-SAM-238; it had been carried in MEMORY/STATUS prose but had no docket row).
- **WALTER lane:** SIG-W-20260910-001/-002/-007 dispositioned INFO-ONLY (Riesco sinking, Mokha/Red Sea — not a Hormuz gate event, two non-Iranian hulls); all FALCON/BRENT-owned, nothing routes to Japan macro.
- **Git:** no pull. 🔧 **CORRECTION, same session:** the boot read said "5 commits behind origin" — it was **5 AHEAD / 0 BEHIND**. `git rev-list --left-right --count HEAD...origin/master` prints `ahead behind`; SAM read the pair inverted, and the "incoming" file list was our own unpushed work (a HEAD-ahead `git diff HEAD..origin/master` shows our changes in reverse). **There was nothing to pull.** The no-pull decision stands regardless — six desks (BRENT/PROME/FALCON/CARL/HAWK/TERRY) were dirty, which is its own protocol bar. PROME reported the same direction independently; verified at a fresh fetch. Wrong reason, right action; corrected on STATUS, MEMORY, the session report and a follow-up PROME packet — **the first packet is already committed and is NOT amended** (root CLAUDE.md 4b).
- **Evidence:** `reports/2026-09-10_et-boot.md`.

## 2026-09-10 (JST) — News/data catch-up; no thesis version or grade change

- **THESIS:** v1.7 unchanged. No successor, no re-pencil, no route re-armed. The September hike is consensus (Masu 9/10 primary; Ueda/Takata 9/2; Himino 8/26; Aida 9/7; Bessent 8/31 + 9/9) at 98% priced — the asymmetry already on record (surprise HOLD = larger, yen-negative move) is reaffirmed, not re-marked.
- **TIMELINE:** added the 2026-09-10 block (Sep-9 leg closed at the BOJ final; SAM-33 absence verified at the op record; consensus cluster; fiscal/GPIF/BoP/energy filed).
- **STATUS:** market table to Sep-9/10 clocks; intervention paragraph (Sep-9 final = provisional, +¥10B vs Ueda); thresholds Sep-9; watch rows (CGPI Sep-11, BOJ Oct–Dec schedule Sep-30); channels paragraph; SAM-31 observation, SAM-33 op audit.
- **PREDICTIONS:** none graded. SAM-33 falsifier verified un-fired through Sep-9 (`ope20260909.xlsx` vs `mpr260831a.pdf`); SAM-31 Sep-9 low-amplitude observation logged, not graded.
- **KB:** KB-SAM-233 (Masu), 234 (consensus cluster), 235 (FY2027 requests / no 2nd extra budget), 236 (GPIF), 237 (July BoP primary), 238 (SAM-33 op-record method).
- **Docket:** CATALYSTS/CALENDAR — Sep-10 legs resolved, Sep-11 CGPI (verified at `cgpi2607.pdf`), Sep-30 17:00 JST BOJ schedule (verified at `mpr260831a.pdf`), early-Oct Diet and Oct-8 BoP in beyond-horizon.
- **Evidence:** `reports/2026-09-10_news-catchup.md`.
- **Inbox pass (same session, ~02:4x UTC):** PREDICTIONS ledger — DAEDALUS as-made audit dispositioned (`audits/2026-09-10_asmade-disposition.md`): 13 false matches, five rows to the WQ-112 field form, **SAM-07 scoring vintage 75% → 48%**, five Date_Made placeholders corrected; scoreboard unchanged. NEXUS_BRIEF reordered per amendment 12 (CROSS-DOMAIN first body section; zero text change). Receipts sent to DAEDALUS and NEXUS (carve-out ①).

## 2026-09-09 — Evidence follow-through; no thesis version or grade change

**Old → current:** BOJ changed-image quote unavailable → visually reviewed and ingested; pre-event broker baseline missing → Ueda September 3 forecast located, weakening the gross September 9 drain inference while leaving September 8 attribution open. Funding observations advanced to September 8. Timeline records these findings; detailed prices and source clocks remain in STATUS/report.

Boot candidate pending → actual fresh judgment FAIL/orientation PASS, default instructions restored. Replacement fixed pair unidentified → Dec–Mar selected with official expiry/settlement evidence, vendor feed activation withheld. Sep-18 adjudication unprepared → frozen-row packet plus full-window screens and explicit convention gaps. Infrastructure authority untraced → August 21 ruling located and per-item dispositions recorded. THESIS, predictions and trade histories unchanged. [Report](../reports/2026-09-09_followthrough.md).

## 2026-09-08 — Approved catch-up integrated; v1.7 retirement unchanged

**Old → current:** durable owner prose still mixed June/July blanket demand-vacuum, decaying/unsuccessful intervention and phase-clock narratives with later correction riders. The already completed September assessment and existing CH-009/010/Channel-1 rulings now govern the relevant sections directly: conditional JGB sponsorship; priced-policy versus surprise; official attribution separated from fiscal residuals; reserve stocks separated from transactions; oil/FX prices separated from physical volumes. Retired weights and EV tables are explicitly historical.

The insurer tracker retains the existing ≥2 named institutions / ≥2 consecutive windows reactivation requirement; sector totals do not satisfy it. KB-209's main fact now carries the FIMA retraction and official window aggregate with unresolved funding. Old text is preserved in `../research/outputs/2026-09-08_integration/before/`. No prediction grades, frozen terms, position money fields, or thesis version changed; no successor promoted.

BOJ source verification found a newer Totan table during integration: September 9 11:15 (JST assumed), ingested separately from the historical September 8 observation. Mechanism interpretation unchanged. New code/ledger controls and remaining visual-review dependency → `../workbook/BOJ_OIS_README.md`; complete integration/validation map → `../reports/2026-09-08_integration.md`. No new cross-agent messages; NEXUS is the in-place handoff.


## 2026-09-08 — monitoring update, v1.7 unchanged

Old: 155 not yet crossed, Sep-4 front-end discriminator pending. New: BOJ Sep-8 low 152.90 and 17:00 JST 153.80–82; MOF Sep-4 2Y −2.0bp and 30Y −8.7bp, no hawkish front-end confirmation. Broader attribution remains OPEN; no new intervention exclusion. Threshold observation is not mechanism confirmation. THESIS monitoring note and TIMELINE updated; no gates, probabilities or prediction grades changed. Report: `../reports/2026-09-08_boot.md`.

## 2026-08-27 — ⚰️ **v2.0 CANDIDATE KILLED after RED's blind pass + the sealed cross-read · ✅ SAM-41 RESOLVED CONFIRMED.** **NO version change — THESIS v1.7 stands, no successor frame declared, book FLAT, $0 at risk.**

**① THE v2.0 CANDIDATE IS DEAD, TWICE OVER.** `thesis/V20_CANDIDATE_FLOW_SETS_LEVEL.md` banner-killed (do-not-cite; audit record only).
- **K1 had already fired 2026-08-20** against a kill line the candidate itself pre-registered **as a number before the data existed** (§5: *"$300–500B INVERTS it"*; BIS `WS_GLI` 2026-Q1 measured **$414.9B**). §2 dead as written, **not rescued.**
- **RED's BLIND pass (CHG-RED-048) kills it four further ways:** §3 is an accounting identity that is *either false or Pillar 1 restated* · §4 discriminates **0 of 7** · the §6 killer set is keyed to an instrument seeing **~3.5%** of its object ⇒ *"the killer would sit green while the thesis died"* · the §6 registered prediction **resolves TRUE under both live hypotheses.**
- **Unseal Will-authorized; protocol order held** (RED read in FULL first, seal opened second, mapping third; seal untouched 8/20→8/27, RED attests blind). **Cross-read → `thesis/V20_CROSSREAD_2026-08-27.md`.**
- **The split, scored conservatively AGAINST me:** my list **6 items, 4 overlap ⇒ no evidential weight**; **RED found ~7 I did not**, including both operationally dangerous ones and the only constructive instrument.
- 🔑 **OLD VIEW → NEW VIEW on my own review process:** *"a self-attack list is an adequate substitute for adversarial review"* → **FALSE, and categorically so. All six of my items question whether the THESIS is true; NOT ONE asks whether the INSTRUMENTS could detect that it wasn't. A self-attack list defends the ARGUMENT and is structurally blind to the APPARATUS.** Promoted to fleet memory as an extension of `finding_test_the_guard_not_just_the_guarded` (n=7→8).
- **SALVAGE (4):** §7's retirements (permanent) · the CFTC **volatility-instrument relabel** (doctrine, bilateral via CH-017) · **K3** as a standing falsifier on MOF weekly · the sizing/basis instruments.

**② ✅ SAM-41 RESOLVED CONFIRMED (5Y leg, five consecutive closes below 2.25%, 2026-08-13→08-19).** Scoreboard **14/14/1/5-open → 15 CONFIRMED / 14 FAILED / 1 special / 4 OPEN**, reconciled across all four surfaces in one pass.
- 🔴 **I withheld the grade first and was WRONG.** I argued the −4 to −6bp margins sat "inside the noise" of a 2.9bp/day gap. **That CONFLATED VOLATILITY WITH MEASUREMENT ERROR** — both legs are official published closes, the difference is exact, **there was never an error bar to be inside of.** Caught when Will challenged the reasoning.
- ✅ **Robustness test run on challenge: under the stricter no-lookahead alignment the run is LONGER (7 days, 8/13→8/21)**, all five original days clearing under both alignments.
- **CALIBRATION, against me in the unusual direction:** 40% registered 8/07 → TRUE in 12 days; against the sample (5Y below bar 55% of 97 obs) that reads **UNDER-confident**, the opposite of the SAM-08/20/40 over-confidence cluster.
- ⛔ **Does NOT promote v1.8** — necessary-but-not-sufficient under CH-017; a separately-registered FX co-condition, RED pass and Will sign-off still required.
- 🔑 **OLD VIEW → NEW VIEW:** *"withholding a grade is the conservative act"* → **FALSE. Refusing to grade produces nothing, is never audited, biases the calibration record silently, and reads as rigour while doing it.** Promoted as a mirror instance on `finding_effect_below_instrument_detection_floor`.

**③ THREE INSTRUMENTS, and three defects found in a fourth.** Built + boot-wired `rate_differential.py` (SAM-41) and `xccy_basis.py` (RED's constructive item — a **PROXY**, not the basis; every substitution named). `mof_flows.py` had **three** defects, two found by the guard written for the first: the alert was keyed to a 4-week rolling while the registered threshold is keyed to the **WEEK** (**n=3; 10.7% of all trips invisible**) · the script had been parsing **half the MOF series** its entire life (inward leg never read) · **MOF revises the series and the TSV silently froze first prints** (14/1,129 rows; **materiality tested — every conclusion held identically**).

**④ NO THESIS CHANGE.** v1.7 stands. No channel moved, no threshold re-marked, no band edited, no successor frame declared. **The successor question re-opens as v1.8's question, with CH-017's FX co-condition intact.**

---

## 2026-08-20 — 🕯️ **v2.0 CANDIDATE OPENED (Will-directed) AND ITS OWN PRE-REGISTERED KILLER FIRED THE SAME DAY.** **NO version change — THESIS v1.7 stands, book FLAT, $0 at risk. Nothing was ever built on the candidate.**

**WHAT CHANGED:** after seven weeks of deliberately refusing to name a successor, Will directed the build. `thesis/V20_CANDIDATE_FLOW_SETS_LEVEL.md` opened — **"flow sets the LEVEL, positioning sets the VOLATILITY."** **Old view:** the record speculative short was "fuel" that would deliver yen strength when a trigger fired (v1.6, dead 8/7). **Candidate view:** I was reading a **volatility** instrument as a **level** instrument — same series, wrong dependent variable.

**THE ARGUMENT IT RESTED ON:** a scale computation never run in two months of grading a LEVEL thesis on that series. CME JPY futures are ¥12.5m notional ⇒ the **all-time-record short was ¥2.35T ≈ $14.8B** = **28% of ONE intervention day**, **~1.0× the last four weeks of structural outflow**, **~3% of the unhedged Japanese foreign-bond book** ($370-550B).

🔴 **AND THE SAME DAY, K1 FIRED AGAINST IT.** §5 named its own killer **as a number, before any data existed**: *"At $14.8B the arithmetic holds; at $300–500B it INVERTS and §3 collapses."* Pulled at the BIS SDMX primary (`WS_GLI`, own pull, **2026-Q1**): **JPY credit to non-bank borrowers OUTSIDE JAPAN = ¥65.83T = $414.9B.** ⇒ **K1 FIRES. The yen-borrowing universe is 28× the CFTC proxy, which captures ~3.5% of it. §2 IS DEAD AS WRITTEN and was NOT rescued** — the candidate's own instruction was *"say so rather than reach for a rescue."*

⚠️ **WORSE THAN A DEAD ARGUMENT — IT SUPPLIES A RIVAL MECHANISM THAT FITS §4 BETTER:** if only ~3.5% of the trade was ever visible in futures, the 8/7 "collapse" unwound **~3.5% of the position**, and **the level held because ALMOST NOTHING UNWOUND** — not because positioning is too small to move it. **§4 cannot discriminate between the two**, which is exactly the *"a FIT, not a test"* weakness disclosed to RED in advance, now **demonstrated rather than suspected**.

⛔ **NOT OVER-RETRACTED:** BIS yen credit to non-residents is **NOT the carry trade** — includes trade finance / yen-revenue corporates / euroyen with no carry motive (**upper bound**), **EXCLUDES FX SWAPS ENTIRELY** (incomplete the other way), and is a **STOCK not a position**. **Decisive on ORDER OF MAGNITUDE, which is all §5 asked; never to be cited as carry positioning.**

**ANALYTICAL CONSEQUENCE:** ⚰️ **Pillar 4 as a LEVEL argument is retired PERMANENTLY** — wrong category, not merely unfired — **and that survives the candidate's own collapse**, because it rests on the 8/7 record (the fuel burned and the level went the wrong way), not on §2's arithmetic. **The successor question is RE-OPENED, not answered.** RED redirected mid-blind-pass to press §3/§4 and the meta-question of whether to **KILL** the candidate outright; SAM's self-attack list remains **SEALED**.

**INSTRUMENT ADDED:** `scripts/bis_gli.py` → `workbook/BIS_GLI.tsv` (two-clock, idempotent, **hard-stops rather than writing a figure wrong by 10ⁿ** if its unit anchor — JPY credit to the Japanese government ≈ ¥1,280T — fails). BIS is **quarterly, ~1-quarter lag, no auth**; the morning's *"semi-annual and heavily lagged"* framing was wrong on both counts.

**WHAT ACTUALLY WORKED, recorded because it is the only part that did:** the blocker was named in advance, the inversion threshold was written **as a number before the data existed**, one pull settled it, and **a pre-registered killer fired against its own author within six hours with the disposition already written down so it could not be negotiated with.** *The thesis was wrong; the rails were not.*

---

## 2026-08-17 — 🔴 **THE CURVE-SHAPE READ IS RE-OPENED: a second long-end-led session, on a WEAK growth print, with the 30Y OUT of round-trip range.** **NO version change — THESIS v1.7 stands and the attribution is deliberately left OPEN.**

**Old view → new view.** **OLD (8/10 + 8/13, both recorded here):** the regime is **BOJ hike PULL-FORWARD** — front-led flattening (2Y +13.9bp vs 30Y +0.7bp over 7/31→8/12), with the 8/7→8/12 long-end-led session graded a **give-back** and the 30Y at 3.989% correctly graded a **ROUND-TRIP** (8/4 printed 3.990). **NEW:** that reading **no longer covers two of the last three sessions**, and the round-trip escape is gone. **Attribution is re-opened as an explicit OPEN QUESTION — pull-forward vs fiscal/term-premium — and is NOT re-marked.**

**What changed, in figures.** MOF closes (own primary): 30Y **3.989 [8/12] → 4.002 [8/13] → 4.002 [8/14]** — the **first MOF closes above 4.00% since 5/20**, i.e. **no longer a return to the 8/4 3.990 level**; 40Y **4.006** likewise; 2Y **1.657**, 5Y **2.151**, 10Y **2.878** — all series highs. Then **8/17 Tokyo** (Investing.com RT ~07:32 ET, a **different basis** — their 30Y prior close 4.015 vs MOF 4.002 = **+1.3bp**; their 10Y prior close **2.878 matches MOF to the bp**): 2Y **1.696 (+3.5bp)** · 10Y **2.924 (+4.6bp, intraday 2.929)** · 20Y **3.811 (+6.3bp)** · 30Y **4.080 (+6.5bp, intraday 4.084)**. **The long end led by ~2× ⇒ bear STEEPENER.** 10Y **2.93% = highest since Sept 1996** (Nikkei/Euronews). ⚠️ **A MOF-basis series-high claim (vs 4.043 on 5/19) is OWED at tomorrow's publication, NOT made today.**

**Why the attribution is contested, and why that is the finding.** Japan **Q2 GDP 1st prelim (8/17): +0.3% q/q / +1.1% annualized vs +2.0% expected**; private consumption **−0.0% = first negative in 8 quarters**; capex −1.2%; domestic demand −0.2pp; **external demand +0.5pp was the entire print**; deflator +2.6% y/y (CNBC / Cabinet Office). **That is weak data, and weak data driving the LONG END hardest is the FISCAL signature** — soft growth → Takaichi stimulus → JGB supply into the demand vacuum — **not hike-pull-forward, which is front-led by construction.** The wires themselves split: Nikkei *"faster BOJ tightening expectations"*; Euronews *"as growth data disappoints."* **Deliberately NOT re-marked: one session, a two-source narrative, and my own 8/13 lesson is to grade the shape over the full stretch before calling a regime.** *(The symmetric discipline also applies — 8/13 used the full stretch to dismiss a steepener; using it again now would be motivated window-choice, so the honest move is to name the question and let the auctions adjudicate.)*

**Consequences registered (no number moved).** ① **Pillar 2 re-enters live testing at a HIGHER level.** v1.6.3 governs: 4.0% is a **demand FLOOR with a named bid under it** (Meiji Yasuda, >¥2T FY2026 super-long plan), confirmed in flow 3× (7/7 4.55× · 7/22 40Y 2.83× · 8/6 3.864×). **The open question is whether the floor is real at 4.08% or was level-specific.** **Adjudicator promoted: the Aug-20 20Y auction 🟡→🔴** (then 30Y 9/3) — grade **auction internals, never the yield level** (SAM-26 trap). 4.5% (contested J-GAAP tail, v1.6.7) remains **~42bp away and not proximate**. ② **CH-004 sign discipline unchanged** — rising hike conviction SHRINKS route-1 surprise room; the frame is retired regardless. ③ **Carry buckets ~3/8/13 UNCHANGED; amplifier + residual OFF; book FLAT; no entry trigger exists.** ④ **Channel 1 stays RETIRED and this week argues *against* re-arming it:** MOF weekly wk 8/2-8/8 printed **+¥1,629B foreign LT-debt BUYING**, the largest buying week in the tracked series (4-wk rolling **+¥37B ≈ flat → +¥572B**) — **yen-NEGATIVE structural outflow, UST-demand-POSITIVE.**

**And the datum that matters most with a flat book: none of it transmitted to the currency.** USD/JPY **159.26, −0.03% — a seventh flat session.** 10Y at a 30-year high, the hike being pulled forward, the long end breaking, and **the yen did not bid.** *This is the successor question in live form — the fuel burned, the tank is being removed (8/14 OI −27,519), and the level still will not move.* **SAM-31 unfired; SAM-39 gets no test.**

**⚠️ Instrument-integrity item escalated, not resolved.** `workbook/BOJ_OIS.tsv` reads Sep **51.0%, +0.0pp across as-of 8/13 AND 8/14** — **frozen through a front-end cash selloff that took the 2Y to a series high on wire-named "faster BOJ tightening expectations."** That is now **two independent witnesses** against my derivation (Polymarket 79.5%, and the JGB 2Y cash market), and it shifts the balance toward **a defect in my meeting-attribution rather than crowd excitability.** ⛔ **No Sep figure is to be cited until `boj_ois.py`'s TFX second-source gate is run.**

---

## 2026-08-13 — 🔧 CALIBRATION-RECORD CORRECTION + docket drift repair. **NO version change: THESIS v1.7 stands, no analytical view moved.**

**Old view → new view: none.** Recorded here anyway because two of the three items corrupt the *audit trail itself*, which is what this file exists to protect.

**1. 🔧 THE OPEN-PREDICTION COUNT WAS WRONG ON EVERY SURFACE — 5 OPEN, not 4.** **SAM-41 had been live and uncounted for six days.** It was registered **2026-08-07 post-closeout** (Will-directed, the v1.8 candidate's bar): it received a `PREDICTIONS.tsv` **row** but never reached a **count**. Surfaces corrected: `STATUS.md` ×2 · `PREDICTIONS.tsv` preamble · `THESIS.md` § PREDICTIONS · `NEXUS_BRIEF.md`. ⚠️ **THESIS § PREDICTIONS carried two errors at once** — it also still read scoreboard **14/12/1**, predating the 8/7 double-failure (SAM-29 + SAM-40) → corrected to **14/14/1**. **Why this matters beyond bookkeeping: a calibration record that omits an open prediction cannot be scored honestly**, and the omitted one is always the most recently registered — i.e. the least likely to be remembered and the most likely to be load-bearing. **Standing guard written into the TSV header: a prediction registered AFTER the closeout sweep is precisely the one the sweep cannot see — re-run the count from the file, never carry it forward by hand.** *(Same shape as the 8/7 near-miss where the v1.8 candidate FILE was untracked while six surfaces shipped pointers to it: the content exists, the index says it is covered, and the index is what readers trust.)*

**2. ⚰️ DOCKET DRIFT REPAIRED — the Sep-18 "convexity-tail window-end retire-check" was still a LIVE GATE in both docket files.** It **cannot fire**: leg-1 fired on the 8/7 print (−45,473 / 25.3%) and retired the frame **42 days early**. STATUS has carried that correction since 8/7; **it was never propagated into `docket/CALENDAR.md` or `docket/CATALYSTS.tsv`.** Re-scoped to a **SAM-28 / SAM-39 GRADING row** — kept, not deleted, because those two predictions still resolve on that date. ⚠️ Explicit instruction added: **do NOT run the ≥80%-fuel retire test; its precondition is a live frame.**

**3. 🔧 BOJ-pricing restatements DELETED rather than refreshed** (Sep-18 docket row + STATUS § CHANNELS·BOJ). The figure repriced a **third** time on 8/12 (own `workbook/BOJ_OIS.tsv`) and had already gone stale on **four** separate surfaces through 8/10. **A refreshed figure would have re-staled within days; deletion is the fix for a prose restatement of a weekly-moving number.** Live pricing now lives in the TSV and the STATUS market table only. ⚠️ Recorded for consumers: **a wire quoting "~75-80% for September" is quoting something nearer the OCTOBER cumulative** — verified 8/13 against own primary.

**Session context (no re-marks):** US CPI 8/12 in line (3.4% / 2.5% core) ⇒ **route 4 unchanged, LIVE-but-UNFIRED**; JGB long end sold off to 30Y **3.989%** — ⚠️ **a ROUND-TRIP, not a fresh test of the Meiji ~4.0% floor (8/4 printed 3.990)**; the 8/7→8/12 curve shape inverted to a long-end-led bear steepener **but the full 7/31→8/12 stretch is still net flattening = pull-forward intact**, so Monday's read survives on the longer window. Buckets **~3/8/13 UNCHANGED**; amplifier + residual **OFF**; **book FLAT**.

---



## 2026-08-07 (later) — 🕯️ **v1.8 CANDIDATE OPENED: "Is Pillar 1 coming back?" — NOT a version change, NOT a thesis**

**THESIS stays v1.7 (retired, no successor).** Will asked directly whether rate-differential compression is
returning; the analysis was worth preserving, so it is written up as a **candidate** in
`thesis/V18_CANDIDATE_PILLAR1.md` with an explicit guard at the top against exactly the thing a well-written
candidate enables — becoming the thesis by default.

**VERDICT AS WRITTEN: PROMISING MECHANISM, ZERO ACHIEVED PROGRESS.**

**The measurement, which is the whole entry:**

| Date | 5Y gap | 10Y gap | |
|---|---|---|---|
| **2026-06-18** | **2.327** | **1.823** | the day v1.6 declared Pillar 1 broken |
| 2026-07-31 | 2.416 | 1.944 | 10Y peak |
| **2026-08-07** | **2.316** | **1.887** | today |

**Today ≈ mid-June.** 5Y materially identical; **10Y is WIDER by 6.4bp than when the pillar was pronounced dead.**
The July widening has retraced ~82% (5Y) / ~47% (10Y) — **and that is the entire move. Nothing has been won.**

⚠️ **The framing trap this entry exists to record:** anchored to the **7/31 peak** the gap is "compressing
nicely"; anchored to **June** nothing has happened. The peak is the wrong anchor — it is a July extreme produced
by the very hawkish hold this candidate is supposed to be recovering from. **Anchor to June.**

**Case FOR:** ① for the first time this cycle both legs move the same way (Fed Sep hike odds **57% → 43.9%**;
BOJ Sep cumulative **45.6%**, and the TFX curve shows a **pull-forward**, terminal unchanged — it compresses the
*near* gap, which is what prices carry); ② the registered "labor too firm" blocker weakened; ③ **structurally the
strongest point: Pillar 1 does not need a crowd** — the thing that killed the convexity frame does no damage here.

**Case AGAINST (currently wins):** ① no achieved compression (above); ② the registered tripwire — an **FOMC
walk-back of the Jun-17 dots** — **has not fired**, and Warsh's regime is intact (3 hawkish dissents 7/29);
③ one payroll with adverse composition (private +30K vs government −53K; U-3 fell on participation = NO-SIGNAL
per LABOR L-06); ④ **CH-004** — the already-priced portion does not pay; ⑤ **SAM is 0-for-2 on this exact pillar**
(SAM-08 @90%, SAM-20 @60%, both FAILED).

**Bar registered as SAM-41 @40%** — June-anchored, and *"sustained"* **defined** as 5 consecutive closes so it
cannot be graded on an intraday tag: **5Y gap <2.25% OR 10Y <1.80% by 2026-10-31.** ⚠️ The level bar and the FOMC
tripwire are **separate; neither substitutes for the other.** Kill conditions written (Sep FOMC reaffirms the
dots · a new WIDE · Japan inflation rolls over).

**Recorded so it is not improvised later — the vehicle would be DIFFERENT.** Without a crowd to squeeze, a
Pillar-1 rally is a **grind, not a spike**: spot / long-dated, **not** the short-dated convexity structure we were
building (options bleed theta on a grind). **Inherits NOTHING from the retired frame** — not the Sep-18 window,
not the −153K/85% line (VOID), not the trigger list, not TRY-FIRE-007 (stood down).

**Open data needs, flagged rather than papered over:** the US leg of the table is **Yahoo secondary** and needs a
**Treasury/FRED primary** re-pull; the US/JGB pairs are **not perfectly synchronous** (MOF publication lag), so
direction is safe and 1bp precision is not; the Fed leg should be derived from **SOFR futures** to match the
BOJ leg's TFX-primary footing; and **SAM-41's base rate is UNMEASURED** — 40% is judgment, not calibration.


## 2026-08-07 — v1.6.11 → **v1.7** · ⚰️ **CARRY-CONVEXITY TAIL RETIRED TO LOW. Leg-1 SPF fired — a registered thesis-BREAK condition is MET.**

**Trigger:** CFTC JPY COT, Aug-4 data, released Fri 8/7 15:30 ET.

**OLD VIEW (v1.6.11, 8/2 → 8/7):** carry-convexity tail at **MED-HIGH**, flagged PROVISIONAL. Positioning fuel at **90.8%** of the −180K cycle peak, amplifier **+8-10pp** ON, residual ON, buckets **~8/23/32**. Entry recommendation: WAIT-FOR-8/7, then enter on a CONFIRM.

**NEW VIEW (v1.7):** ⚰️ **frame RETIRED to LOW. No entry, ever, on this frame. No successor frame declared.**

| | Jul-28 data | **Aug-4 data** |
|---|---|---|
| Net non-commercial | −163,412 | **−45,473** |
| % of −180K peak | 90.8% | **25.3%** |
| WoW | −11,287 (build) | **+117,939 (cover)** |
| Longs / shorts | 101,271 / 264,683 | **147,228 / 192,701** |
| Open interest | 432,366 | 419,393 (**−12,973 only**) |

**Why this is a break and not a downgrade:** the THESIS leg-1 SPF, written **2026-06-22** and unchanged since, reads *"CFTC covers below −108K / 60% line → frame → LOW."* Actual: **−45,473 / 25.3% — through by 62,527 contracts and 34.7pp, 42 days before the Sep-18 horizon.** ⚠️ The §5B resolver's *"past −140K = revert MEDIUM"* was written contemplating a **7/10-style de-load at 68.8%**, which does **not** trip leg-1. This print does. **Applying both registered rules as written yields LOW.** Nobody should read "DE-LOAD → MEDIUM" off the resolver map and stop — that understates it by a full grade.

**Mechanism — position REVERSAL, not liquidation.** OI moved only −12,973 while net swung +117,939: shorts covered 71,982 (−27.2%) **and** longs added 45,957 in the same week. The Aug-4 vintage spans **7/30, 7/31, 8/3, 8/4** — the entire two-sovereign intervention window. A max-short crowd took a ~5.3% adverse move (163.8 → 155.2) and folded. **This is SAM-22's mechanism (intervention → mass cover) delivering.** SAM-22 previously FAILED as a *prediction*; its mechanism has now fired, and it was **one of the two reversion paths named in advance** on 8/2 and 8/4 (the other being the 7/10 <12h whipsaw).

**Predictions:** **SAM-40 FAILED** (45% CONFIRM modal missed; the ~25% DE-LOAD branch fired; resolver run on the letter, terms frozen 8/4, **not re-tuned at scoring time**). **SAM-29 FAILED** (leg-1). Scoreboard **14/12/1 → 14 CONFIRMED / 14 FAILED / 1 special**. SAM-28 very likely to fail; **deliberately NOT graded early.**

**Buckets — full four-anchor re-pencil, fuel plugged in: ~8/23/32 → ~3/8/13.** Two named drivers: ① fuel collapse → amplifier and residual both **OFF**; ② route 6 (residual positioning cascade) **~10% → ~2-3%** — *a carry unwind requires a carry position to unwind, and it just unwound.* ⚠️ **The five non-fuel anchors were computed and COMMITTED BEFORE the print** (`REPENCIL_2026-08-07_PREPRINT.md`, `ce71c5cbf`) specifically so the fuel outcome could not contaminate them.

**Other anchor moves folded in this session (all pre-print):** route 1 BOJ hawkish-of-priced ~11-12% → ~7-8% (Sep unpriced ~77% → band ~40-54%, own TFX 3m-TONA primary derivation); route 4 Fed walk-back **COLD → LIVE-but-UNFIRED** ~5% → ~7-8% (8/7 NFP; trimmed from ~8-9% on LABOR's composition read — private +30K vs government −53K); route 5 oil/MOU ~10-11% → ~8-9%, **proxy-marked** per BRENT v5.4 (throughput is the test; the instrument is dark); route 2 MOF ~10% → ~8%; route 3 risk-off unchanged.

**WHY NOT v2.0:** a major bump asserts a replacement structure, and there isn't one. **Inventing a successor frame in the same hours as the print that killed the old one is the improvisation these rails exist to prevent.** v1.7 records the retirement and leaves the successor blank. **The question v1.8+ must answer, written down so it cannot be skipped:** *the carry trade substantially unwound — and the yen is at 157.5, not 145. What is the thesis when the positioning fuel has already burned and the level barely moved?*

**Position: FLAT throughout. $0 at risk. Nothing executed, ever, on this frame.** The MED-HIGH grade carried a PROVISIONAL flag from award; WAIT-FOR-8/7 held; Will's Monday-execution ruling was pre-registered the morning of the print **before the number existed**; and the §5C override that fired **on the letter** on 8/3 was deliberately not acted on. Had it been taken, the book would have been long into this.

**Calibration lesson (the one to carry):** the failure was **not** missing the mechanism — SAM named SAM-22 explicitly as a way the grade could die. **The failure was pricing a named mechanism at 25% while holding a MED-HIGH grade the same document called PROVISIONAL.** *Naming a risk and then under-weighting it is a distinct error from not seeing it.*

**Also this session (non-thesis):** BND-11 single-week resolver **stood down** (bar at 0.49σ of its own series noise); 8/6 JGB 30Y auction **PASSED** (BTC 3.864×, Pillar 2 unaffected); SAM-31 still unfired (today's yen bid was dollar-side — yen mid-pack vs majors); BOJ `jd` archive path appears **dead**, so the SAM-39 base rate is not currently reproducible.


## 2026-08-04 (Tue) — v1.6.11 STANDS, no version bump [SAM boot: one new prediction, one base-rate correction, two anchors moving in opposite directions]

**Old view → New view, by item:**

**1. The 8/7 resolver was a DISPOSITION → it is now a SCORED PREDICTION (SAM-40, 45%).** Old: the resolver terms lived only in the adjudication memo §5B as an action rule — the 8/7 outcome would trigger a decision but never grade SAM's judgment. New: registered as **SAM-40** before the print. Terms are **verbatim from §5B and were deliberately not re-tuned while writing the row** — re-tuning a resolver at scoring time is how a resolver stops being falsifiable. Marked **45%, below even odds despite a long-biased frame**, because **SAM-22 (@65%, FAILED)** is the direct precedent: intervention near the trigger level historically forces mass cover. Counterweight: the 7/30 op's yen gains have now held **three** sessions, breaking the n=2 same-day-reclaim pattern.

**2. 🔧 SAM-39's base rate was measured on truncated data — CORRECTED; the MARK STANDS.** Old (registered 8/3): prior-year **2/250 ≈0.8%/session → naive P ≈23%**, giving SAM-39 @55% a **~+32pp** edge. New (repaired data): **3/259 ≈1.16%/session → naive P ≈32%**, edge **~+23pp**; pre-episode max 1.90y → **1.98y**; the **0/60 pre-episode leg is unchanged**. **The prediction is not re-marked — only its rationale is corrected**, which is the honest split: the number I published was right, the reason I gave for it was ~9pp overstated. Root cause: the `usdjpy.py` truncation defect fixed 8/2-8/3 had corrupted the very column the base rate was computed from. *(Class: a load-bearing number must be reproducible — and a fix to an instrument must be propagated into everything that instrument already fed.)* ⚠️ Recorded against own interest: **8/3 printed 2.67y**, a third consecutive qualifying session immediately *before* the window opens — **not credited** (window starts 8/4) but it means the naive annual base rate is arguably the wrong reference class and **55% may be too low**. Not re-marked mid-flight on one day's tape.

**3. Two named anchors moved in OPPOSITE directions → buckets UNCHANGED at ~8/23/32, for a stated reason.** **Route 5 (oil/MOU re-escalation, ~10-11%/60d) is DECAYING** — Brent **$79.98**, through the $80 line (−4.5% d/d, round-tripped from $100.43 on 7/23) on Trump pausing Iran strikes *and* announcing Hormuz-reopening talks; Phase-1 oil-in-yen pressure is decisively unwinding (yen-positive via the oil channel, **not** the Phase-2 haven bid). **BOJ-hawkish-of-priced is UP-RISK** — Bessent 8/4: yen level "problematic," Treasury "would not hesitate" to intervene again, **but purchases "would need to be followed by Japanese policies addressing the forces driving the yen lower"** [Bloomberg/CNBC] = the US Treasury publicly pressuring Japan on **rates**, a new mechanism on the largest in-window catalyst (Sep 17-18 MPM, ~77% unpriced). ⚠️ **NOT re-marked: could not source current Sep/Oct OIS today, and rhetoric ≠ priced policy** — this is the exact shape of SAM's #1 failure cluster (SAM-08 @90%, SAM-20 @60%, both lost to reading officials' words as policy). Net ≈ offsetting, neither anchor individually >5pp. **Recording the offset rather than the silence**, per the named-driver rule.

**4. JGB 10Y auction: widest TAIL of the tracked series — flagged, NOT a thesis move. 🔧 CHARACTERIZATION CORRECTED same day (PM re-check).** Own MOF primary (`eresul20260804`): **BTC 2.558× / tail 6.0bp**. As first written this said "softest of the tracked series … 4th consecutive month of decay in both legs (3.904 → 3.530 → 3.130 → 2.558)" — that sequence **began at 5/12 and omitted the 2026-04-02 print (BTC 2.565 / tail 4.50bp, same 🟠 grade)**. On the full 5-auction ledger the shape is **V-SHAPED, not monotone: 2.565 → 3.904 → 3.530 → 3.130 → 2.558.** Correct read: a **round-trip to the April soft level with a wider tail**, not a break into new territory; the BTC edge over April is 0.007 (a tie) and the genuinely new leg is the **TAIL (6.0 vs 4.50, +33%)**. **No grade, bucket or registered line moves** — it was flagged-not-re-marked in both versions; this corrects the *characterization* only, and is recorded because it propagated to 6 surfaces incl. NEXUS_BRIEF. Wire context, not own-verified: lowest BTC since May-2025, widest tail in two years; named drivers = consumption-tax funding uncertainty + BOJ early-hike risk. ⚠️ **This is the BELLY. The demand-vacuum thesis and the Meiji ~4.0% floor are 30/40Y objects and did not soften here** — read as hike-path + fiscal repricing, not as the vacuum spreading. It does, however, upgrade the **Thu 8/6 30Y auction** from a formality to a live test.

**5. Intervention ladder extended — no third op Monday.** Own primary `jp20260805.xlsx` (T+2 from Mon 8/3): 財政等要因 **−¥3.35T**, **ordinary** against SAM's own measured early-month peer group (day ≤6: median −2.54T, worst −6.21T) versus the **−¥11.42T** Aug-4 anomaly. ⚠️ "No evidence of," not proof of absence — the instrument is **sovereign-blind** and cannot see a US-Treasury-only op. Also: the 7/31 "CANDIDATE op #2" framing is **DEAD** — officially confirmed as a **US Treasury** op (Bessent 8/2), with the Aug-4 settlement evidencing **MOF firing alongside** = two sovereigns. Full ladder → `thesis/INTERVENTION_2026-07-30_CONFIRMATION.md` (new; carries the pre-registered bands, the base-rate self-correction, and two instrument-scoping corrections).

**6. 🔴 SAME-SESSION CORRECTION to item 3 — the BOJ leg's SIGN was wrong, and sourcing the number is what exposed it.** Item 3 recorded the BOJ-hawkish route as **up-risk** on Bessent's rate pressure, caveated as un-sourced. **Sourced later the same session: Sep BOJ pricing ~23% → ~39.7%** (centralbank.watch, as-of 8/3; **independently corroborated** by a wire reporting *"the swaps curve raised the implied odds of a September BOJ hike to roughly 40% from 20%"*); Oct ~64% → ~71%. ⚠️ Basis caveat: centralbank.watch states **cumulative**, and the 7/31 wire basis is unverified — deltas are directional, not exact. **The correction:** the route is BOJ hawkish-***of-priced*** — it pays on **surprise**, and rising priced probability **destroys** surprise room. Sep unpriced **~77% → ~60%**. With **CH-004 confirmed** (a fully-priced hike does NOT unwind carry — Jun-16), US pressure **absorbed into pricing** is **neutral-to-NEGATIVE** for the convexity route, not positive. **⇒ Item 3's "two anchors moved in OPPOSITE directions, net offsetting" is SUPERSEDED: both anchors moved the SAME way (down).** The offsetting read survived only while the hawkish leg was unmeasured — *"could not source it" should have been grounds to withhold a direction, not to assert one with a caveat.* **Consequence: the 60d bucket is flagged LIKELY-GENEROUS. Not re-marked — this is a full four-anchor re-pencil per the method rule, deliberately deferred to the 8/7 print, which resolves the fuel leg in the same pass.** Propagated to STATUS, STRATEGY, TRADE (the "~77% unpriced" figure was load-bearing in the 60d rationale).

**Unchanged:** conviction **MED-HIGH, provisional on 8/7**; buckets ~8/23/32; Sep-18 window (LOCKED, inclusive); leg-1 cover line −108K; SAM-28/29/31/33 terms; **FLAT book, nothing executed**; §5C override still adjudicated **fired-on-the-letter and deliberately not acted on** (no informational lead — the trigger was announced publicly to SAM and the options market simultaneously).

---

## 2026-08-03 (Mon) — v1.6.11 STANDS, no version bump [GOVERNANCE: the RED #4 VEHICLE GATE is RETIRED, Will-approved — a structural/decision-rail change, not an analytical one]

**Old view:** a live "RED #4 vehicle gate" governed whether the thesis could express itself through a vol structure rather than spot. Canonical THESIS listed **one** re-open condition (FXY-vol demonstrably cheap on a clean second source); TRADE.md and STRATEGY.md listed **two** (convexity reclaims MED-HIGH *OR* vol-cheapness). The divergence was flagged on 8/2 (METSUKE Run-13 E1) and deliberately not silently resolved — it was routed to Will as a money-adjacent defect.

**New view:** **the gate is RETIRED.** Will ruled 2026-08-03 to retire rather than reconcile. Three grounds, all recorded in THESIS § VEHICLE:

1. **The canonical one-leg text was a RATCHET.** The gate *closed* on conviction ("a break-even MEDIUM frame does not generate enough edge to pay a vol structure's spread + theta") but was written to *re-open* only on price. A gate whose closing reason is absent from its opening conditions can never re-open on a recovery in the thing that shut it — and conviction is exactly what recovered on 8/2. TRADE/STRATEGY's two-leg text was **not drift; it repaired an incomplete canonical text**, and the repair was never back-propagated. Class: [[finding_count_the_connectives_in_versus_out]].
2. **Its sole canonical re-open condition was effectively unobtainable.** "A clean second source" for FXY vol — CME JPY CVOL is licence-gated (~$290/mo) and the USD/JPY 25d risk-reversal has no free source, both already documented in STRATEGY § Feed migration. A gate whose only opening condition requires data we have recorded as unavailable is a permanently-closed gate wearing a conditional's clothing.
3. **The gated question no longer exists.** RED #4 asked whether to swap an *existing FXY spot holding* for a vol structure. **The book has been FLAT since 2026-06-29.** Keeping a live gate premised on a position we do not hold is precisely what produced the 8/2 incident: a registered gate fired, no document said so, and derived docs contradicted canonical while TERRY was building an options card.

**What replaces it — two questions, separately owned:**

| Question | Status | Owner |
|---|---|---|
| Instrument choice on entry (options vs spot) | **ANSWERED AND UNGATED — defined-risk options > spot when a trigger fires.** Lives in § POSITION VIEW; was never actually governed by RED #4 | SAM |
| Is the vol cheap enough to pay for | **STANDING PRICING INPUT** — priced at construction against the live chain, never a strategy gate. KB-183 stands (read the FXY proxy's sign, not its level) | TERRY |

**Nothing analytical moved.** No money field, no threshold, no bucket, no conviction grade, no entry recommendation — **WAIT-FOR-8/7 stands**, position FLAT. The 8/2 "vehicle RE-OPENED (provisionally)" adjudication is **superseded, not reversed**: it reached the right practical answer through a gate that should not have existed. **TERRY's TRY-FIRE-007 is unaffected** — its justification always rested on § POSITION VIEW's entry-vehicle answer, not on this gate.

**Sites updated (10, swept by grep not by memory — the un-listed-sibling failure mode):** THESIS ×3 (conviction table row, § VEHICLE rewritten, sizing decision #3), TRADE.md ×3, STRATEGY.md ×3 (incl. the § vol live-read whose "gate stays CLOSED" note was the exact stale-wrong line), NEXUS_BRIEF ×1. **Deliberately left as historical derivation record:** `V16_RED_DIALOGUE.md` § RED #4, `METSUKE_MEMORY.md` run logs, and the original CHANGELOG 2026-06-22 resolution entry.

---

## 2026-08-02 (Sun, REAL BOOT) — **v1.6.11 STANDS, no version bump** [proxy re-mark verified + owned; MOF op-history table AMENDED with a candidate second op]

**Author:** SAM (real boot, Will-directed). Supersedes nothing in the proxy entry below — it verifies it and adds two observations the proxy could not have made. Markets: FX week reopening; all levels are Fri 7/31 closes or stamped publication vintages. **FLAT stands; nothing executed.**

**1. Proxy re-mark VERIFIED at primary and OWNED — no version change.** Own `deafut.txt` pull (vintage 260728): 101,271L − 264,683S = **−163,412**, OI 432,366, WoW longs −6,319 / shorts +4,968 — reproduces the proxy, PROME and NEXUS **to the contract**. MED-HIGH / amplifier +8-10pp / buckets ~8/23/32 stand as written. Will's disposition (WAIT-FOR-8/7 + TERRY re-mark Mon 8/3) confirmed landed via PROME `6c1d17bed`. No analytical view moved, so **no bump** — this is a verification entry.

**2. 🟠 MOF op-history table AMENDED — a CANDIDATE second op is now on the record (Jul 31, 16:00-17:00 ET).** Old view: one op this round (7/30), with Friday's close read as a single number (157.3950). **New view: the Friday close was *made* in a yen-specific slide in the final hour of the FX week, and that slide is itself a candidate op.** Between 16:00 and 16:57 ET, USD/JPY 159.18 → 157.15 (−1.28%) while EUR/JPY (−1.33%), GBP/JPY (−1.32%) and AUD/JPY (−1.50%) fell in lockstep and **EUR/USD and GBP/USD did not move at all** — a pure yen-side move, the 7/30 signature, in the week's thinnest liquidity window and in the **NY session**, the same venue Reuters source-confirmed for 7/30.
   - **Held at CANDIDATE, not booked as an op.** The shape is the weak leg: a ~35-minute progressive slide, not 7/30's ballistic candle. Month-end real-money and a stop cascade into the weekly close are live competing causes. Single-witness on shape → treated as a lead, per [[feedback_single_source_liveevent_is_a_lead]].
   - **Discriminators registered:** BOJ current-account T+2 → `jd20260804.xlsx` (~8/5), same Tanshi-gap method as the 7/30 semi-confirm; and **both 7/30 and 7/31 fall inside the same MOF monthly window (Jul-30→Aug-27, releases ~Aug-31)**, so one print adjudicates both.
   - **Why it matters to the live decision:** "a **confirmed** second op of the round" is a pre-registered EARLY-ENTRY OVERRIDE (outbox memo §5C). **It has NOT fired.** But Will's Saturday WAIT-FOR-8/7 disposition was taken without this datapoint on the table, so it is flagged rather than filed.

**3. The "gains EXTENDED day+1" finding strengthens.** Old view (proxy): Friday closed *below* the 157.92 op-day low, breaking the n=2 same-day-reclaim-then-erode base rate. **New view: the yen made new lows of the entire move at the week's close** (157.151 on 7/31 < 157.923 on 7/30), into a weekend. Strictly stronger than "did not give the gains back." Confound unchanged and load-bearing: the hawkish hold + Ueda's September telegraph are live competing causes, and n=2 sessions is not durability.

**4. 🔴 SAM's own intervention detector was blind to 7/30 — now fixed, and it independently corroborates the op.** A timezone bug in `usdjpy.py` had been storing partial daily bars (10 of the last 60 sessions, all under-stating range); **7/30 was stored as a 0.33y day against a true 5.74y range**, so the intraday-range alert reported "normal daily range" on the largest yen move since Dec-2023. Post-fix it grades **INTERVENTION-GRADE (5.74y)** — against Apr-30-2026's 5.15y, a *confirmed* ¥5.48T op. **Analytical consequence: the 7/30 attribution no longer rests solely on wire reporting plus the BOJ projection gap — SAM's own instrument now scores it at intervention grade.** This does not make it MOF-official (hard confirm ~8/31 unchanged), but it removes a single-source dependency from the evidence stack. Full root cause + fix → `MAINTENANCE.md` 2026-08-02.

**5. Context consumed, no re-mark.** WALTER SIG-W-20260802-001: Trump **ordered then cancelled** strikes on Iranian energy sites on claimed deal parameters; daily exchange **PAUSED** (3rd of the cycle; the 7/24 pause broke in 4 days); Tehran unconfirmed; Kpler Hormuz transits 22 → 5. PROME 8/2: Qatari LNG carrier GasLog Shanghai struck **in Hormuz 8/1**. **SAM read: a genuine de-escalation unwinds oil-side Phase-1 yen pressure — yen-POSITIVE via the oil channel, not the Phase-2 haven bid the carry route needs.** No bucket change: unconfirmed, and Phase-1 relief is not a convexity trigger. Brent $90.12, sitting on the "headwind resolved" line.

**Files:** `STATUS.md` (rewritten + compressed 409 → 179) · `thesis/BOJ_2026-07-31_PREREGISTRATION.md` (new, verbatim archive) · `scripts/usdjpy.py` + `workbook/USDJPY.tsv` (fix + repair, `34069b8c0`) · `MAINTENANCE.md` · this entry.

---

## 2026-08-02 (Sat, PROXY RUN) — v1.6.10 → **v1.6.11** [MINOR, pre-registered flip-condition fired — GATE-SAM-30 re-fire adjudicated VALID; convexity-tail MEDIUM → MED-HIGH, provisional on the 8/7 attribution print]

**Author:** SAM-proxy (phone-session spawn, PROME-directed, Will in-session; real-SAM integrates at next boot). Markets closed (Sat); no live marks set — all levels carry observation dates.

**1. 🔴 The re-fire is VALID, verified at primary.** Own pull 8/2 of `cftc.gov/dea/newcot/deafut.txt` (vintage 260728): legacy noncommercial JPY net = 101,271L − 264,683S = **−163,412 = 90.8% of the −180K Jul-2024 peak**, through the registered >−153K/85% re-fire bar by 10,412; WoW −152,125 → −163,412 = **−11,287 REBUILD** (shorts +4,968 / longs −6,319; OI 432,366 +8,570) — episode-deepest net, shorts expanding into the pre-spike week. Reproduces PROME's fire-packet measurement and NEXUS's independent pull exactly. NEXUS's flagged "84.5% covered" tension dissolved: same series, verb error — a rebuild TO 84.5% of peak (Jul-21 data), not a cover.

**2. Old view → new view.** OLD (v1.6.10): convexity-tail MEDIUM; amplifier +5pp; buckets 5/19/29; entry gate shut. NEW (v1.6.11): **the registered flip-condition ("a future CFTC print builds through −153K/85%") fired → convexity-tail MED-HIGH, amplifier +8-10pp, buckets ~8/23/32** (single-anchor mechanical step, v1.6.4 class; 7d additionally carries the live post-op tape). Net EV reclaims ~+1.3% per the registered RED-#1 flip-up math — **with the written caveat that the math equates measured fuel (7/28-vintage) with current fuel, and the 7/30 suspected ¥8.45T op + 7/31 hawkish hold landed AFTER measurement on a max-short crowd.** Named reversion paths: SAM-22 (intervention → mass cover) and the 7/10 precedent (only prior fire of this gate, reversed <12h by the next print). **The 8/7 print (Aug-4 data) is the built-in resolver.**

**3. MOF #3 route: DECAYING → PARTIALLY-FIRED/LIVE, and the reclaim base rate broke.** Attribution strengthened beyond the fire packet: Reuters source-confirmed 7/30 NY-session yen-buying op (+Nikkei); Bloomberg ~¥8.45T ($52.8B, ~1.5× the biggest prior single-day, ~72% of the whole Apr-May round) estimated from the BOJ's own Fri projection (~¥8.2T fiscal-factor decline vs broker-forecast increase; T+2 settle Mon 8/3; primary checkable ~8/4). NOT MOF-official; hard confirm ~8/31. **WALTER SIG-004 consumed + independently verified: USD/JPY closed 157.3950 Fri 7/31 [investing.com] — BELOW the 157.92 op-day low → the first op of the cycle whose yen gains EXTENDED day+1; the registered n=2 "same-day reclaim then erode" base rate is broken** (op-history tables amended in STATUS + MOF_INTERVENTION_PLAYBOOK). Confound honestly carried: the hawkish hold + Ueda's September naming are live competing causes for Friday's extension; n=2 sessions ≠ durable.

**4. Composition (the frame's first two-legged evidence).** Fuel at episode-max (measured 7/28) AND two tail-routes partially fired (MOF #3 live; BOJ-hawkish telegraph: Oct OIS ~64%, Sep ~23%, Sep 17-18 MPM ON the inclusive window boundary at ~77% unpriced). Prior fires were fuel-only. This is why MED-HIGH is honest despite the vintage caveat — and why the caveat is written on the mark rather than used to dodge the registered consequence.

**5. Entry recommendation (Will's decision, PROME routes):** WAIT-FOR-8/7 default + TERRY re-mark of TRY-FIRE-005 NOW (Aug-21 tenor excludes the Sep 17-18 MPM — must roll to span Sep-18) + pre-registered 8/7 resolver (≤−153K held = CONFIRM/enter · −140..−153K = NOT-CONFIRMED w/ leg decomposition, longs-up = SAM-31 candidate · past −140K = DE-LOAD repeats, revert MEDIUM) + early-entry override (fresh ≥2%/day disorderly move / confirmed op #2 / haven re-couple). Full terms → `outbox/2026-08-02_to-PROME_sam30-refire-adjudication.md` §5. FLAT stands; nothing executed (root rules #4/#5).

**Unchanged:** Sep-18 window (LOCKED, inclusive) · leg-1 cover line −108K (now 55,412 away) · SAM-28/29/31/33 terms · Channel structure · scoreboard 14/12/1/4.

---

## 2026-07-31 (2nd entry, ~9:15 AM ET) — v1.6.9 → **v1.6.10** [MINOR, pre-registered trigger fired — FULL-C closure + carry-bucket re-mark on the Ueda presser Oct/Sep telegraph; MOF monthly ¥0 hard-confirms the 7/2 no-strike]

**Author:** SAM (same Will-launched session, morning-after sweep). **Live marks (~9 AM ET):** USD/JPY **160.35** · EUR/JPY 184.21 · Brent $90.22 — the 7/30 spike holding roughly half its ground.

**1. 🟢 SAM-38 sub-grade CLOSES FULL-C (not WEAK-C).** The pre-registered disconfirmer-2 bar — "Oct OIS does NOT move off the ~26-40% range → record WEAK-C" — was decisively cleared the other way: **Oct OIS repriced to ~64%** post-presser (Reuters/Bloomberg 7/31), with **Sep priced ~23%** and Ueda explicitly framing the debate "from the next meeting onward" (= September) around upside price risks ("many of our board members' inflation forecasts are fairly high and they see risks skewed to the upside — I would like to take that into account in chairing future policy meetings"). Reuters: the BOJ "warned for the FIRST TIME that underlying inflation could exceed its target." Strategist consensus: "moderately hawkish," "September-October now live."

**2. 🔴 THE REGISTERED RE-MARK TRIGGER FIRED → buckets 5/18/27 → 5/19/29 (single named anchor).** The frozen Branch-C(c) clause (7/29): "if Oct OIS jumps materially (>40%) on this signal, that is a same-session re-mark trigger for the convexity-tail bucket." Executed without wiggle: **BOJ-hawkish-of-priced route ~8-9% → ~11-12%/60d** — the decisive point is that **the Sep 17-18 MPM sits IN the locked Sep-18 window (decision day ON the inclusive boundary) at 77% UNpriced**, so the telegraph pulls real hawkish-of-priced probability mass inside the window rather than parking it at the out-of-window Oct-30 meeting. 30d ~18→~19 (Sep MPM ~48d out, just past the 30d edge); 7d ~5 unchanged; amplifier +5pp unchanged pending today's CFTC print. **Conviction stays MEDIUM** — the MED-HIGH flip-conditions are CFTC-through-−153K/85% OR yen-haven re-couple; a guidance telegraph re-weights buckets, not conviction. No anchor >5pp; method discipline satisfied.

**3. 🟢 MOF monthly (pub ~19:00 JST): ¥0 intervention, Jun-29→Jul-29 window — the 7/2 no-strike adjudication HARD-CONFIRMED.** SAM's two-legged intraday decomposition (Reuters-ambush-story repricing + NFP USD-leg) graded correct against the official record; **CH-011 (disorder-not-level) gets its cleanest empirical stamp yet — MOF sat out the ENTIRE orderly grind to 40-yr lows (163.83) with ¥0 spent.** The 7/30 suspected op falls in the NEXT window (~Aug-31 release) as flagged; press now describes 7/30 as "the government's yen-buying intervention... that failed to give the sagging currency lasting support" (Reuters framing) — treated as SUSPECTED-strengthened, still not MOF-confirmed.

**4. Housekeeping:** SAM-38 Outcome cell + preamble updated (append-only discipline: statement-time grade retained verbatim, closure appended); STATUS banner addendum + § GRADE closure + § CARRY UNWIND re-mark block; docket presser/MOF rows resolved; NEXUS_BRIEF re-stamped. Next nodes: **CFTC Jul-28-data 3:30 PM ET today** (re-fire check at 875-ct pre-spike proximity, attribution-blind) · **8/7 CFTC = the 7/30-spike attribution print** · 8/6 30Y auction · ~Aug-31 MOF window for 7/30.

---

## 2026-07-31 — v1.6.9 (NO version change) [two predictions resolved — BOJ July MPM graded live off the primary statement; SAM-38 Branch C fired + SAM-34 hold confirmed; 7/30 yen-spike attribution OPEN]

**Author:** SAM (Will-launched live decision watch, Thu 7/30 ~10 PM ET → Fri 7/31 ~12:45 JST grade). **Live marks:** USD/JPY **160.42** post-print (pre-print 160.71; statement reaction ~−0.3%) · EUR/JPY 184.24 / GBP/JPY 215.27 · Brent **$90.28** · JGB (MOF 7/30 pub) 10Y 2.801 🔴 / 30Y 3.971 / 40Y 3.967. **Sources: primary only** — statement `boj.or.jp k260731a.pdf` + Outlook basic view `gor2607a.pdf` (both pub 12:11 JST; meeting ran to 12:04 = LONG), pdfminer-extracted.

**1. 🟢 SAM-38 RESOLVED CONFIRMED — the ~55% modal Branch C fired.** (a) **HELD ~1.00%, vote 8-1** — with a **HAWKISH dissent: Takada formally proposed 1.25%** (overseas demand-shock upside price risk; "new phase" requiring nimble response). The dissent shape FLIPPED June→July (dovish Asada against the hike → hawkish Takada for the next one) — a board-composition tell the pre-registration did not enumerate but which strengthens C over A. (b) **Outlook = the hawkish-lean guidance leg, satisfied:** price risk balance "upside risks dominant"; underlying inflation "risks overshooting the 2% target" (repeated — and the policy-management paragraph now frames the objective as **stabilizing underlying inflation AT ~2%**, i.e. overshoot-MANAGEMENT, a hawkish reframe); core CPI "clearly above 2%" from H2 FY2026; "confirm whether ~2% sticks"; FX pass-through "stronger than in the past" + import-price surge explicitly named. (c) **FY2027 purchase plan UNTOUCHED** (Branch D unfired; June path stands by silence). Forecasts: GDP FY2026 0.5→0.6 / FY2027 0.7→0.8; core CPI FY2026 2.8→2.5 (energy-subsidy technical) / FY2027 2.3→2.4; core-core ~unchanged. **Sub-grade FULL-C vs WEAK-C held PENDING** the pre-registered disconfirmer-2 (Oct-OIS move — unverifiable at grade time; Ueda presser 15:30 JST). Disconfirmer-1 NOT tripped; disconfirmer-3 borderline (~−0.3% at print, tape contaminated by 7/30). **Contamination clause CLEAN and it PAID:** the circulating pre-dated content (techtimes 7/27 class, n=2 independent witnesses SAM 7/29 + VIOLET 7/30) said "GDP upgraded to 0.8%" — actual FY2026 = 0.6 (0.8 is FY2027) → fabricated-wrong, not leaked; the freeze was uncontaminated. Routed to WALTER as a source-quality finding.

**2. 🟢 SAM-34 RESOLVED CONFIRMED (hold @85%).** The 15% tail materialized as a formal DISSENT, not a hike — Takada's argument class (defensive response to overseas-shock price risk) was exactly the registered tail mechanism. 3rd consecutive well-calibrated BOJ-meeting binary (SAM-21 ~90% / SAM-24 85% / SAM-34 85%, all TRUE) after the SAM-08/20 too-hawkish failure cluster — the consciously-NOT-shaded-hawkish discipline is now a confirmed pattern. Scoreboard **14 CONFIRMED / 12 FAILED / 1 special / 4 OPEN** (SAM-28/29/31/33).

**3. ⚠️ THE TAPE CHANGED BEFORE THE PRINT — 7/30 yen +2.7% spike, attribution OPEN (not this entry's to resolve).** Largest 1-day yen move since Dec-2023 (163.49 → 157.92 low → 159.46 NY settle; EUR/JPY −400 pips in minutes = yen-specific op signature). SUSPECTED MOF intervention, NOT wire-confirmed (Katayama sidestepped Fri AM; Bloomberg "declines to confirm, hints at US support"; Bessent shares-concerns line) — the ambush-regime S1-A shape delivered as written (unsignalled, confirm-by-data-later). Evidence ledger: VIOLET canary CALM→FIRE→WATCH intraday (RV10 16.13 peak → 14.62 settle; IV/RV 0.78→0.92; her caveat: RV cannot distinguish intervention from unwind — one bar reproduces the whole fire); equity vol NEVER transmitted (VIX FELL through the break bar, settled 17.09 −17.3% — legs decoupled = evidence AGAINST an Aug-2024 replay); intraday decay mildly favors intervention (VIOLET lean, unscored). Discriminators queued: today's CFTC (Jul-28 data) is attribution-BLIND (predates the move); **Aug-4-data print Fri 8/7 = first attribution-capable print**; MOF hard confirm = ~Aug-31 monthly (7/30 outside today's Jun-27→Jul-29 window); semi-confirm ~Mon 8/3 BOJ current-account T+2 anomaly. **No re-mark on the spike itself** — a suspected op + hawkish-lean hold + 84.5%-of-peak positioning is condition-STACKING, not a fired trigger (echoes the 7/10 lesson: the reverse-carry-squeeze framing was walked back once; two-print/attribution discipline applies).

**4. Read-throughs — ALL HELD: convexity-tail MEDIUM · buckets 5/18/27 · amplifier +5pp · FLAT · no entry gate open.** Same-morning Tokyo July CPI hot (core 1.9 vs 1.7f; core-core 2.0 AT-target) folds into the Oct-path watch, not a July re-mark. The Oct-telegraph question (the one condition that pulls the Oct-hike tail INSIDE the locked Sep-18 window) goes to the presser + next OIS read — same-session re-mark trigger if Oct pricing jumps materially; not met at grade time. Next decision nodes: Ueda presser 15:30 JST · CFTC 3:30 PM ET (compound read) · 8/6 30Y auction (first super-long under the reaffirmed FY2027 plan) · 8/7 CFTC attribution print.

---

## 2026-07-23 — v1.6.9 (NO version change) [prediction resolved + confirmatory market scan — SAM boot]

**Author:** SAM (boot + news/auction scan, Thu 7/23). **Live marks (boot.py all-green 23.8s + fetch.py):** USD/JPY **163.83** (+0.39%, fresh 40-yr low / weakest since Oct-1986, ORDERLY) · FXY **$56.02** · Brent **$100.43 (+6.76%)** · EUR/JPY 186.32 / GBP/JPY 218.06 · JGB 10Y 2.745 [MOF].

**1. SAM-35 RESOLVED CONFIRMED (firm-lean, MARGINAL) — the Jul-22 40Y JGB auction.** BTC **2.83x** (846.7B bids / 299.8B accepted; high yield 3.865%, low price 98.68, coupon 3.8%, 2066 maturity; MOF eresul20260722) — cleared the pre-registered ≥2.8x FIRM bar, up from the May-27 soft baseline 2.702 → **the Meiji-Yasuda ~4% demand floor extends to the longest / most-J-ICS-sensitive tenor.** ⚠️ MOF published NO weighted-average yield ("—") → the tail (the ≤4bp co-condition of the AND) is UNVERIFIABLE, so this is a BTC-only firm read, marginal (2.83 vs 2.80 bar) and much weaker than the 30Y's 4.55x blowout (7/7). The WEAK/disorderly-break-precursor scenario (BTC<2.3x or tail>8bp → 🔴 cross-agent) is decisively RULED OUT. Read-through: disorderly-break carry tail thins further; orderly-grind base case reinforced. Scoreboard now **12 CONFIRMED / 12 FAILED / 1 special / 5 OPEN** (SAM-28/29/31/33/34).

**2. Confirmatory market scan — NO thesis-version / conviction / bucket change.** (a) **Brent through $100** (+6.76%, highest since May-22) on ACTUAL tanker strikes (Houthi drones hit 2 Saudi tankers enforcing their Riyadh blockade · tankers struck off Saudi · Kazakh CPC export halt · renewed US strikes on Iran; Goldman $120-Q4-if-Hormuz) — deepens oil-in-yen **Phase-1 yen-NEGATIVE** (the June TB −¥406.9B deficit already carries it), NOT the Phase-2 risk-off yen-haven bid (yen WEAKENING). FAL-01/sustain = BRENT/FALCON's call; the tanker strikes + CPC halt add real supply-at-risk vs 7/21's pure-risk-premium read. Oil/MOU carry route holds ~10-11%/60d (60d Phase-2 tail firming-but-unfired; **no bucket re-mark** — no single anchor >5pp, positioning unchanged). Watch: Brent approaching the $115 "Phase-1-reasserts → USDJPY-upside → intervention" line. (b) **USD/JPY 163.83 fresh 40-yr low but ORDERLY** (+0.39%/day) → strike-watch ARMED not FIRED, 165 next; Katayama pinned it on ME/oil + "bold action at any time" (verbal, ambush regime). (c) **🆕 Bloomberg: BOJ officials open to a FASTER pace of hikes than consensus** (yen boost) — reinforces the BOJ-hawkish-of-priced carry route (route 1) + is a SAM-34 watch input (re-check July-hike pricing before 7/31), but **NOT re-marked** (SAM-08/20 failure-cluster discipline — a sourced-openness report is not priced policy). **Convexity-tail MEDIUM · buckets 5/18/27 · amplifier +5pp · FLAT — ALL UNCHANGED.** MOF weekly wk-7/12–7/18 (durable-vs-transient 2nd-buying-week check) not yet posted → carried.

---

## 2026-07-17 — v1.6.8 → **v1.6.9** [MINOR, pre-registered prediction resolved — CFTC JPY COT Jul-14 graded STALL, no conviction change]

**Author:** SAM (PROME COT-session spawn, Fri 7/17 — two-phase: pre-print prep [SAM-37 verdict map registered ~1 PM ET] + post-print grade [~3:33 PM ET, primary-verified]). **Live marks (fetch.py ~12:58 ET):** USD/JPY **162.41** (+0.21%, weak vs USD but FIRM vs EUR/GBP/AUD = USD-side strength) · FXY $56.46 · Brent **$87.37 (+3.73%)** (six-night campaign, risk-premium — no barrel) · DXY 100.75.

**1. CFTC JPY COT Jul-14 (first post-Hormuz-closure positioning print) — GRADED STALL.** Print (`deafut.txt` legacy futures-only PRIMARY, report-date 2026-07-14, contract 097741; Socrata API lagged the 3:30 release so the raw text file was the grading source): **net −122,663 / 68.1% of the −180K Jul-2024 peak** (long 115,965 [+3,718 WoW] / short 238,628 [+2,603] / OI 396,514 [−1,589]; **dNet +1,115 = essentially FLAT**, a hair more cover off Jul-7's −123,778/68.8%). Reconciles exactly with the prior print via the WoW change columns. Appended to `workbook/CFTC_JPY.tsv`.

**2. SAM-37 RESOLVED CONFIRMED (core band) with an honest sub-lean miss.** The pre-registered verdict map (set BEFORE the print): RE-FIRE ≤−153K/85% · REBUILD-partial −140/−153K · STALL −124/−140K · COVERING −108/−124K · COVER-TAIL >−108K/60%. The falsifiable CORE claim ("lands between −108K and −153K — neither re-fires the amplifier nor invalidates the frame") resolved **TRUE** (−108K was 14,663 away, −153K 30,337 away — neither tail fired). The 55% modal **sub-lean** (STALL −124/−140K) narrowly **MISSED cover-ward by 0.7pp** — printed −122,663, ~1.3K on the cover side of the −124K STALL floor (Band-4 by the literal boundary), though substantively flat. Calibration note: the tape-based rebuild-tiebreak (weak-yen → fresh shorts) did NOT dominate; the two closure-week forces I pre-identified (safe-haven JPY bid vs oil-Phase-1 carry-reload) BOTH showed up (longs +3,718, shorts +2,603) and roughly CANCELLED — a two-sided wash, with a faint fresh-haven-long tick that is NOT a SAM-31 re-couple (noise-level, no VIX regime → no HENRY escalation).

**3. Read-throughs applied — NO structural/conviction change.** No registered line crossed → **convexity-tail stays MEDIUM · amplifier +5pp holds (68.1% ≈ base) · carry buckets UNCHANGED 7d~5/30d~18/60d~27 (no re-pencil per the four-anchor discipline) · TRY-FIRE-005 stays SHELVED (DE-LOAD stands) · USDJPY band 159-166 / >167 disorder-tail unchanged.** The substantive read: after the big Jul-7 flush, positioning STABILIZED/STICKY at ~68% of peak — it neither re-loaded (despite weak-yen + oil-Phase-1) nor kept covering (despite the war/closure). Moderate positioning fuel, neither draining nor building. **SAM-29 cover-tail (−108K, OPEN 65%) now 14,663 away — tightened slightly from ~15.8K, still comfortably holding. SAM-30 stays RESOLVED.** Scoreboard 11 CONFIRMED / 12 FAILED / 1 special / 6 OPEN (+ fixed a 7/16-preamble off-by-one: '5 OPEN' → true 6). **FLAT stands.**

**4. Oil-leg durability caveat (WALTER 4-file drain, board_log).** The $76→$87 oil move is RISK-PREMIUM, not supply-loss (FAL-01 unfired, Iraq resumed same-day, Russian loadings +68% MoM) → more reversible → softens the 60d oil-tail (~10-11%); no bucket change (no barrel lost). Conversion trigger = shuttle-fleet bypass breaks (WSJ SIG-013) or Bab el-Mandeb executes (SIG-004). BRENT owns the sustain verdict.

---

## 2026-07-16 — v1.6.7 → **v1.6.8** [MINOR, discriminator resolved + four-anchor re-pencil] — MOF weekly wk-7/5–7/11 = +¥1.09T foreign-LT-debt BUYING → flips the BND-11 read TRANSIENT → DURABLE-leaning; carry buckets re-penciled ~5/18/27 (owed item closed); oil/MOU route re-armed on formal Hormuz closure

**Author:** SAM (PROME teams-mode spawn, Thu 7/16 ~9:40 AM ET — double-discriminator day; MOF weekly print out [pub 7/16 JST], TIC lands 4 PM ET post-session). **Live marks (fetch.py ~9:34 ET):** USD/JPY **162.24** (+0.03%, weak-yen edge, orderly) · FXY $56.52 · Brent **$85.76** · DXY 100.60 · EUR/JPY 185.85 / GBP/JPY 219.12 / AUD/JPY 113.64 (yen weakest of all majors = yen-SIDE, oil-driven). **Closes MSG-PROME-20260714-002 (Direct Messaging v1, first live test).**

**1. 🔴 DECISIVE DISCRIMINATOR — MOF ITS weekly, wk 7/5–7/11, resolves toward DURABLE (flips the 7/9 pre-registered lean).** The registered mechanical bar (7/11, set BEFORE the print): outward LT-debt net **≥+¥500B BUYING = durable-leg corroboration · ¥0–500B = ambiguous/lean-transient · <¥0 = transient CONFIRMED.** Actual print: **+¥1,090.1B net BUYING** (`week.csv`, Final Update 7/16/26; `mof_flows.py` auto-pull; +10,901 億円) — **>2× the durable bar**, and a hard reversal of the two prior selling weeks (−¥277.5B [6/21–6/27], −¥217.5B [6/28–7/4]). 12-wk rolling +¥5.15T (~+$34.3B). **→ the 7/9 EVE "safe-haven-transient, MEDIUM" read on the US-30Y-reopen 77.74% indirect surge (BND-11) is FALSIFIED by its own pre-registered arbiter → re-marked to DURABLE-leaning at MEDIUM.** Honest caveats retained: (a) MOF weekly = foreign LT debt *globally*, not USTs-specific — TIC (May, 4 PM ET today) is the UST-specific same-day check but predates the event window (trend consistency only); the direct UST test is June TIC (~mid-Aug); (b) single week — a 2nd buying week (next Thu) would firm it; (c) yen-NEGATIVE structural flow (Japan deploying abroad at the 40-yr-weak yen) — consistent with USD/JPY 162, reinforces the no-near-term-carry-unwind base case, and is UST-DEMAND-POSITIVE (cross-relevant to LIQUID/BOND — reinforces Channel-1 RETIRED / Japan = net UST buyer, NOT a repatriation-seller). Disciplined update on a pre-registered resolver, not an overreaction to one print.

**2. FOUR-ANCHOR CARRY-UNWIND RE-PENCIL (closes the owed item; MSG-002#SAM-01).** After the CFTC round-trip (Jun-30 built to −155,092/86.2% [SAM-30 CONFIRMED] → Jul-7 covered to −123,778/68.8% [SAM-36 DE-LOAD]) and folding the oil shock + USD/JPY 162, the full four-anchor re-pencil (owed since Jun-14 discipline): **7d ~5% · 30d ~18% · 60d ~27%** (from the v1.6 baseline ~5-6/17-20/24-28). Net effect ≈ baseline, with the composition rotated: 7d pulled to the LOW end (positioning covered 17.4pp + Phase-1 oil-driven yen weakness = wrong direction near-term), 60d held at the TOP end (oil Phase-2 tail + risk-off re-weighted UP replaces the covered positioning fuel). Named-driver attribution: **CFTC amplifier** +8-10pp→**+5pp** (68.8%, residual ON; leg-1 −108K now ~15.8K away) · **oil/MOU route** 8%→**~10-11%/60d** (Iran FORMALLY closed Hormuz 7/11-12, Brent ~$76→$86 held — a more-severe instance than the 7/8 truce-collapse that faded; BUT Phase-1 yen-NEGATIVE near-term, so it lifts the 60d tail not the 7d; BRENT owns the sustain verdict) · **Fed-dot walk-back** ~0/60d ~5% (cool June US CPI −0.42% MoM a marginal positive but July carries the oil = inflationary offset → no walk-back) · **BOJ-surprise** ~8-9%/60d (hike-mass burned, SAM-34 hold@85%; weak-yen+oil imported-inflation marginally lifts the Jul-31 hawkish-tail) · **risk-off** ~7-8%/60d (oil-driven risk-off possible but yen-haven still decoupled → USD-haven caps it) · **residual cascade** ~10%/60d. **Convexity-tail stays MEDIUM; no conviction/EV-table change** (>5pp anchor shifts: none; composition re-weight attributed above per method discipline).

**3. Downstream / no structural change.** The carry-convexity-tail frame (MEDIUM, window LOCKED Sep-18) is unchanged. FLAT stands. The durable MOF flip does NOT enter the unwind buckets mechanically (it's a UST-demand / structural-flow signal, yen-negative) — it's convergent with, not a driver of, the low 7d. **CFTC next-print date reconciled (MSG-002#SAM-02): Fri Jul-17, 3:30 PM ET (Jul-14 data) — the "Mon Jul-13" entry was an error (Jul-14 data cannot release Jul-13); confirmed by the CFTC API showing Jul-7 as still the latest + the standard Friday cadence (Jul-7 data released Fri Jul-10).** BoK hiked 25bp → 2.75% (context only, ZHAO owns Korea) — a regional FX-defense hawkish tilt under the same oil/weak-currency pressure the BOJ faces = mild reinforcement of the BOJ-hawkish-surprise tail.

---

## 2026-07-11 — v1.6.6 → **v1.6.7** [MINOR, mechanism re-scope] — CH-010 resolved toward RED round 2: 30Y-4.5% = J-GAAP statutory-impairment TAIL (disorderly-only), not a clean forced-seller; base case net-demand-positive; mid-cap bifurcation watch

**Author:** SAM (Will-approved sweep follow-up, Sat 7/11 weekend session — no live tape; all data vintage-stamped). **Trigger:** DEWEY research-output prompt-08, routed via WALTER SIG-W-20260710-004 (delivered 7/10, consumed at the 7/11 sweep; source report `AGENTS/DEWEY/output/2026-07-10_004`). Note: the DEWEY prompt was Will-dropped 7/9 as event-passed for the 7/7 auction — this is its FORWARD-context application to the standing CH-010 mechanism question (OPEN_THREADS #5, open since 7/2), not a live-trigger read.

**1. Old view (v1.6.2 → v1.6.6):** CH-010 CONTESTED — SAM's asset-markdown read (30Y ~4.5% = reflexive forced-selling zone, legacy-book impairment → sell) vs RED's economic-value read (higher yields improve solvency → duration-gap-closing BUYING); sign unresolved pending the accounting basis (J-GAAP statutory vs ICS economic value). v1.6.3 gave RED round 1 (Meiji Yasuda bid at 4.0%, 50bp below the claimed zone).

**2. New view (v1.6.7) — mechanism-split, RED wins round 2:**
- **Base case at higher long-end yields = net-demand-POSITIVE.** Under J-ICS/ESR economic value, higher yields IMPROVE lifer solvency — Nippon Life ESR −2pp to 222% [DEWEY 7/10], still comfortably strong. The ESR channel argues buying into a rise, not selling.
- **What survives is a TAIL, and it has a specific accounting basis:** J-GAAP *statutory* impairment on low-coupon legacy holdings can force selling — but only in a **disorderly** move through ~4.5%, not as a clean level trigger. This aligns CH-010's answer with SAM-33's existing orderly-grind-base/disorderly-tail architecture (the same split, now with the accounting mechanism named).
- **Flow evidence (leg-4 of the v1.6.1 demand-vacuum resolved):** May's −¥201.2bn super-long net-sell is partially offset by Apr's +¥327.2bn → **2-month net +¥126bn BUYING** [DEWEY 7/10]. The "lifers turned net-SELLERS" leg of the v1.6.1 vacuum framing does not survive the 2-month window (single-month flow-sign trap — same lesson class as SAM-32's rotation sell-leg).
- **GPIF:** NOT the marginal buyer — 25% domestic-bond policy weight unchanged; Katayama's 7/10 GPIF/repatriation jawbone reads rhetorical, not flow [DEWEY 7/10, convergent with SAM's own `gpif_flows.py` FY2025 read].

**3. Surviving falsifiable edge — BIFURCATION WATCH (pre-registered observable):** mid-cap lifers (**Fukoku/Asahi** — still absent from the super-long per v1.6.3) plausibly face J-GAAP impairment pressure near 4.5% while the majors buy. If 30Y re-tests 4.0-4.5%, the tell is **mid-cap-SPECIFIC selling** (insurer disclosures / flow composition), not aggregate-lifer selling. Aggregate flow staying positive while a mid-cap breaks = the bifurcation confirming; aggregate selling = SAM's original read reviving.

**4. Downstream:** 30Y-4.5% carry-tail route KEPT (already a thin tail per CH-011; mechanism now correctly characterized — **no EV-table number moves**, no bucket change, no conviction change). KEY-THRESHOLDS-table row updated. `insurers/TRACKER.md` per-insurer refresh queued for next live session if the bifurcation watch needs a hard anchor (weekend — no fresh disclosure pull). Next test: 40Y auction 7/22 (SAM-35, unchanged at 50%).

---

## 2026-07-10 PM (2nd) — v1.6.5 → **v1.6.6** [MINOR, evidence review] — Oil/MOU tail-route EV-weight RECOMPUTED, REAFFIRMED 8%/+3% unchanged

**Author:** SAM (PROME follow-up tasking, same session as SAM-36). **Trigger:** the 7/9 self-sweep flagged the route's 8% weight (THESIS § THE N TAIL-ROUTES) as pending-recompute — set pre-truce-collapse, sitting stale in a live table. PROME tasked the recompute this session now that three fresh datapoints exist.

**1. The three datapoints:**
- **(a) The 7/8 truce-collapse re-arm.** Real: US-Iran strikes, ceasefire declared over, Brent +6.3%→~$79. But the realized transmission was Phase-1 (oil spike → terms-of-trade hit → yen WEAKENS), not Phase-2 (recession risk → yen-haven bid → carry unwind) — the wrong direction for this route's own +3% payoff mechanism (see STATUS 7/8 note: "yen weakened DESPITE the geopolitical shock... echoing OIL-IN-YEN").
- **(b) BRENT's GATE-BRENT-SUSTAIN graded DENY tonight** (`AGENTS/BRENT/outbox/2026-07-10_to-PROME_sustain-verdict.md`, ~21:15 ET): level held (~$76 settle both sessions) but only 1 of ≥2 required FRESH institutional legs fired (war-risk premium surge only — sanctions down-weighted per RED red-team #3 as near-automatic; transits and P&I/JWC had no fresh Friday print). Energy tail reverts ACTIVE → 🟡 fragile-watch — an independent, adversarially-gated cross-agent verdict that this specific re-escalation did NOT durably establish.
- **(c) SAM's own Jul-7 CFTC print (SAM-36, same session).** JPY noncommercial shorts covered sharply through this exact event window (86.2%→68.8% of peak, the largest WoW reduction in the tracked series) — Japan-side FX positioning was unwinding, not building, into the oil shock. A live/gripping re-escalation route should show positioning building on the fear, not covering.

**2. Verdict: REAFFIRM 8% / +3% FXY move-if-fires, unchanged.** All three datapoints point the same way: a real trial of this route ran this week and faded fast without producing its own stated payoff mechanism (no Phase-2 yen-haven bid, no positioning build, and now an independent DENY on institutional-leg breadth). This is consistent with what an honest 8% base rate implies — a real-but-not-dominant tail probability — not evidence the true rate is higher or lower. Per the fleet-wide calibration lesson (one data point rarely justifies a 15-25pp shift), reaffirming rather than adjusting off a single fired-then-faded instance is the disciplined call. **A genuine SECOND re-escalation attempt** (fresh distinct Iran leg, sustained >2 sessions, clearing BRENT's own ≥2-institutional-leg bar) **would warrant a fresh look** — this is not a permanent close of the question.

**3. Downstream effect: none.** Route contribution stays 8%×+3%=+0.24% in the EV table (§ THE N TAIL-ROUTES); gross expected payoff, overlap discount, and net 60d EV are all unchanged. TERRY's TRY-FIRE-005 conditional-move math (which sums this same route table) is therefore also unaffected — no re-derivation needed there. THESIS version bumped to log the evidence review per the audit-trail convention (a reaffirmation is still "new evidence for an existing view"), not because any number moved.

**4. Also this session (same spawn, separate task):** `STRATEGY.md` FXY modal-band re-derivation executed — see that file's own CHANGELOG (dated 2026-07-10 PM). Not a THESIS.md change; logged here only as a same-session pointer.

---

## 2026-07-10 PM (1st) — v1.6.4 → **v1.6.5** [MINOR, pre-registered resolver] — 🔴 SAM-36 FALSE/DE-LOAD: Jul-7 print covers to 68.8% of peak, past the −140K DE-LOAD line → carry-convexity-tail reverts MED-HIGH → MEDIUM; TRY-FIRE-005 entry NOT recommended

**Author:** SAM (PROME/teams-mode spawn, Fri 7/10 ~9:00 PM ET). **Trigger:** the Jul-7-data CFTC print, released 3:30 PM ET today — the pre-registered resolver for the TRY-FIRE-005 entry decision Will set this morning (option (b): TERRY pre-built the card, entry gated on this print).

**1. The resolver (the thesis change):** CFTC JPY non-commercial net **−123,778 = 68.8% of the Jul-2024 −180K cycle peak** (longs 112,247 [+375 WoW] / shorts 236,025 [−30,939 WoW]; OI 398,103 [−40,722]) — source: CFTC public API `publicreporting.cftc.gov` (id `260707097741F`, report date 2026-07-07, dataset equivalent to `deafut.txt`, same primary as the AM verify). This is a **31,314-contract net covering move**, down sharply from 86.2% (Jun-30) — the single largest WoW net-short reduction in the tracked series (`workbook/CFTC_JPY.tsv`, 2026-04-07 onward). Against Will's registered resolver terms (net ≤−153K/85% = CONFIRM/enter; net ≥−140K = DE-LOAD/no-entry; between = NOT-CONFIRMED): **−123,778 clears the DE-LOAD line by 16,222 contracts** — not a marginal miss of the CONFIRM bar, a clean DE-LOAD. **Registered consequence: TRY-FIRE-005 entry NOT recommended; amplifier reverts +8-10pp → +5pp; carry-convexity-tail MED-HIGH → MEDIUM (net EV back to break-even-to-slightly-negative, RED #1 terms); carry-unwind buckets revert toward ~5-6/17-20/24-28 (7/30/60d).** This unwinds v1.6.4's single-anchor mechanical step from earlier today — the full four-anchor re-pencil (Jun-14 discipline rule) remains owed and now has two data points (Jun-30 build, Jul-7 cover) to work from.

**2. Timing read (why this isn't jawbone-caused):** the report date is Tue 2026-07-07 — the covering happened **before** the 7/10 JST Katayama GPIF/repatriation jawbone that rallied the yen intraday today. Plausible drivers inside the 7/1–7/7 window: the 7/7 JGB 30Y auction resolving FIRM (BTC 4.55x/tail 0.3bp, relayed to BOND same day) reducing conviction in a disorderly-break carry-unwind path, plus the accumulating hot-PPI/rising-JGB-yield stack cutting both ways on directional yen conviction. **This walks back the 7/10 AM note's "record short + policy-driven yen bid = reverse-carry-squeeze fuel" framing**: positioning was already unwinding into that framing, not building into it — the fuel was being removed in real time as the framing was written.

**3. Position implication (flagged, not executed):** the entry-gate condition SAM-30 opened this morning is now **closed DE-LOAD** by SAM-36. Recommendation to Will/PROME: do not approve TRY-FIRE-005 entry; FLAT book stands. This is a recommendation only — SAM does not execute (root rule #5).

**4. Calibration note:** SAM-36 registered at 50% (net-holds-through vs covers, genuinely uncertain call given the Jun-23→Jun-30 build had just accelerated) — resolved FALSE. Distinct from SAM-30, which stays RESOLVED CONFIRMED (it graded the Jun-30 print correctly on its own terms; the build to 86.2% was real and did cross the line). The lesson is about **entry-gate persistence, not SAM-30's grading**: a single-print crossing of an escalation line is a necessary but not sufficient condition for entry when the very next print can reverse it within days — a two-print (or momentum-of-covering) confirmation requirement may be worth pre-registering for future CFTC-gated entries, not just single-print tripwires. Auto-memory candidate.

---

## 2026-07-10 AM — v1.6.3 → **v1.6.4** [MINOR, pre-registered tripwire] — 🔴 SAM-30 CONFIRMED: CFTC built through −153K/85% → carry-convexity-tail reclaims MED-HIGH; entry gate condition MET on the flat book

**Author:** SAM (PROME spawn, Fri 7/10 AM). **Trigger:** boot-sweep adjudication of the Jun-30 CFTC print (deafut.txt primary; released 7/6, landed in `CFTC_JPY.tsv` at the 7/9 boot, adjudicated this session).

**1. The tripwire (the thesis change):** CFTC JPY non-commercial net **−155,092 = 86.2% of the Jul-2024 −180K cycle peak** (longs −1,826 / shorts +7,162 WoW; OI 438,825) — **through the pre-registered −153K/85% escalation line** for the first time this cycle (prior 81.2% Jun-23, which had been the first cover off the top; reversed). Old view: convexity-tail at MEDIUM, honest 60d EV ≈ break-even → analytically a trim signal, entry not EV-positive. New view (registered consequence, executed without wiggle per SAM-30's own terms): **amplifier +5pp → +8-10pp; convexity-tail MEDIUM → MED-HIGH; net EV ~+1.3% → entry EV-positive; carry-unwind buckets ~5-6/17-20/24-28 → ~8-10/20-24/27-31 (7/30/60d).** Single-anchor mechanical step — the Jun-14 discipline rule's full four-anchor re-pencil is OWED next session with the Jul-7 print (releases Fri 7/10 3:30 PM ET).

**2. Context (sharpens, not part of the mechanical step):** the crossing lands the same week as (a) the 7/10 Katayama GPIF/domestic-repatriation jawbone that produced an intraday yen rally (~+0.5%) + JGB long-end rally (10Y −10bp ~2.775 / 20Y −10bp ~3.765, zerohedge/Barchart relays; MOF 7/10 pub = hard verify) — a strengthening yen INTO a record short = reverse-carry-squeeze fuel; (b) WALTER SIG-018 (Barchart: largest TFF leveraged-fund yen short since 2007 — different series from this legacy non-comm gauge, kept distinct, directionally convergent); (c) USD/JPY exiting the 162-163 MOF zone downward (161.8, orderly). Symmetric caveat: positioning is a condition, not a trigger — the squeeze needs a spark; extreme shorts can persist.

**3. Position implication (flagged, not executed):** STATUS's registered entry gate ("deploy only on a FIRED trigger — … / CFTC through −153K/85% / …") is **MET** for the first time since the book went FLAT (6/29). Routed to PROME/Will for decision; TERRY owns construction (rules #6/#7 theirs). No trade recommended this session (spawn scope).

**4. Calibration note:** SAM-30 was a 30% against-base-rate call that resolved TRUE — build-momentum correctly weighted. Offsetting process miss logged: **adjudication lag** — the print was public 7/6 and in the workbook 7/9, but sessions carried "Jun-30 print not confirmed pulled" while the crossing sat in `CFTC_JPY.tsv`. Auto-memory candidate: boot sweeps must adjudicate landed data vs registered lines, not just land it.

---

## 2026-07-02 — v1.6.2 → **v1.6.3** [MINOR, evidence-forced] — JGB demand-FLOOR found at ~4%; SAM-32 RESOLVED FALSE (48h); MOF-verify: candidate strike = NO STRIKE (ambush-tactics regime logged)

**Author:** SAM. **Trigger:** boot verification sweep on the PROME-queued "MOF verify" assignment (candidate 7/2 strike) surfaced the Meiji Yasuda super-long re-build; 2-outlet verified before propagation (Sato-verify discipline).

**1. JGB demand-floor (the thesis change):** **Meiji Yasuda doubled its FY2026 SUPER-LONG JGB purchase plan to >¥2T**, AM head calling ~4% 30Y a **"perfect buying opportunity,"** funded by selling low-coupon legacy JGBs (Nikkei Jul-1 06:32 JST; Bloomberg Jun-30). → **SAM-32 RESOLVED FALSE** per the pre-registered CH-015 plan-leg (fastest falsification on record, 48h; full post-mortem `PREDICTIONS_ARCHIVE.md#sam-32`). Old view: demand vacuum with "no re-entry yield near current," re-entry a 2-3yr rollover, 4.5% a forced-selling zone. New view: **buffer-AND-yield-conditional vacuum with a first named demand floor ~4.0% 30Y**; May's ¥201B net-selling re-read as a **yield-rollup SELL-LEG** (Dai-ichi stated identical intent Jul-2025) — flow sign ≠ program direction; **CH-010's first live data point resolved toward RED** (economic-value/duration-gap-closing buying); the JGB-disorderly carry tail thins further (bid cushions the break path); orderly-grind base case *reinforced*. Demand-reduction survives (Fukoku/Asahi absent; foreign 16mo net-sell; MOF supply cut). Realized-flow confirm open (Jul-7 30Y / Jul-22 40Y auctions re-framed: they now test whether the announced bid is REAL; GPIF gap still open).

**2. MOF verify (PROME assignment — resolved, no thesis change):** candidate 7/2 strike = **NO STRIKE.** Two-legged intraday decomposition (spot crosses + CME 6J w/ volume): (a) 15:45 JST Tokyo spike (−1.1y in minutes, yen-specific vs USD/EUR/GBP, 6J 11× avg volume, ~60% retraced) = repricing on the **Reuters exclusive: MOF shifts to AMBUSH intervention tactics** (unsignalled ops, no jawboning lead-in, deliberately no line-in-the-sand; Mimura/Katayama silence intentional); (b) 8:30 ET leg (−0.9y) = **NFP** (June +57K vs 113K consensus, revisions −74K, U-3 4.2% participation-driven) — USD-specific (yen crosses closed UP on the bar), rules out a Jul-2024-style piggyback. No rate checks, no op reported (verified negatives; caution logged: the circulating Mimura rate-check quote is Feb-12 vintage). Hard confirm = MOF monthly ~7/31; fast semi-confirm = BOJ current-account projections ~2 business days. **Playbook amended** (MOF_INTERVENTION_PLAYBOOK S1): under the ambush regime, T1-rate-check absence is no longer evidence a strike isn't imminent; ladder retains value only when it escalates. MOF #3 anchor HELD ~15-20%/30d (ambush-intent story raises strike-tail intent; spot backed off 162.6→161.0 lowers proximity — offsetting, documented).

**3. NFP context (no re-mark):** July FOMC hike faded (~73% hold post-print) but **Sep hike ~65% still priced, 3.8% terminal intact** → this is hike-TIMING slippage, NOT a Fed-dot walk-back — SAM-28 route 4 does NOT fire; the "labor too firm" blocker has its first crack (NFP +57K, revisions −74K, ADP 98K, Challenger cooling), inflation leg intact (Warsh "prices too high," Sintra Jul-1). Equities UP on the miss (VIX ~16) → SAM-31 yen-haven re-couple not firing. Carry buckets unchanged (within-band; no >5pp shift, no named-driver change).

**Edits:** THESIS v1.6.3 (header; Pillar 2 demand-floor bullet; disorderly-route thinning; KEY THRESHOLDS 30Y-4.0 re-scoped + 4.5 doubly-suspect; PREDICTIONS pointer 6 OPEN; → BOND update note); PREDICTIONS.tsv (SAM-32 → FAILED + scoreboard + failure-pattern (2) extended); PREDICTIONS_ARCHIVE #sam-32; JGB package § DEMAND-FLOOR UPDATE; STATUS 7/2 note + tables; TIMELINE Jul-2 line; CALENDAR/CATALYSTS (10Y auction resolved BTC 3.13x/tail 2.6bp softer-but-orderly; **CFTC Jun-30-data print → Mon Jul-6** [holiday-delayed, CFTC official schedule]; MOF monthly ~7/31 row); MOF playbook S1 ambush amendment + 7/2 live-log; thresholds.py/usdjpy.py label reconcile (PROME 7/1 spine-audit item); NEXUS_BRIEF; outbox → PROME (verdict) + BOND/LIQUID/HENRY (demand-floor overlay on the un-processed Jun-30 signals).

---

## 2026-07-01 — [no version bump — evidence enrichment] — JGB→US TRANSMISSION MAP; bear-steepener action-review; drift true-up

**Author:** SAM. **Trigger:** Will asked (a) what to do about the JGB bear-steepener and (b) how it transmits to US markets, ahead of spawning BOND/LIQUID/HENRY today. **No conviction/thesis change** — the v1.6.2 frame stands; this enriches the → BOND cross-link with the live transmission answer and trues up drift.

- **Bear-steepener action-review = HOLD** (multi-lens panel + act-now adversary, unanimous). No Will-tradeable JGB vehicle (signal-only); the *gradual* (~8bp/day) move fires no carry-tail trigger; pre-positioning fails deploy-on-trigger + the break-even-MEDIUM frame (the adversary's best case — a small premium-only long-vol ticket on the unwind-speed asymmetry — didn't clear: negative EV isn't cured by defined-risk, vol not cheap per KB-183). Decision nodes = Fri Jul-3 CFTC + Tue Jul-7 30Y auction. No re-mark.
- **JGB→US TRANSMISSION MAP built** (`research/outputs/JGB_SUPPLY_DEMAND_THESIS.md` § US-TRANSMISSION; multi-agent gather of live US levels + BOND/LIQUID/HENRY state + adversarial synthesis) — answers the → BOND question SAM routed Jun-30. **Finding:** transmits DIFFUSELY via correlated global term premium, NOT repatriation (Ch A dormant — Japan a net UST buyer; US 30Y 4.96% co-moving up on a shared driver, softer US ground — ACM 10Y term premium +0.73%; Ch C carry-unwind = tail; Ch D capital-export = only live flow, risk-positive). Tail = a disorderly JGB break dragging the US long end via correlation alone. **Peers have NOT processed SAM's Jun-30 signal** → corroboration = convergent priors.
- **Edits:** THESIS § CROSS-AGENT LINKS → BOND (partial-answer pointer); TIMELINE Jul-1 line; JGB package § US-TRANSMISSION MAP + PUNCHLINE marks refreshed; STATUS 7/1 note + market tables; NEXUS_BRIEF (transmission finding + BOND sharpened-Q + **drift true-up: v1.6.1→v1.6.2, "5 OPEN"→7 OPEN [SAM-33/34 added], marks**); CALENDAR (Jun-30 2Y auction + Jul-1 Tankan → RESOLVED). MOF Jun-30 pub marks: 10Y 2.690 / 30Y 3.873 / 40Y 3.792.

---

## 2026-06-30 — v1.6.1 → **v1.6.2** [MINOR, correction] — RED adversarial pass walks back the JGB over-claims

**Author:** SAM (applying RED's 2026-06-30 JGB demand-vacuum pass; Will-approved). **Trigger:** Will spawned RED (Opus) on the never-reviewed JGB thesis; RED returned a 5-axis sweep (7 challenges, `red/CHALLENGES.md` + `red/COUNTER_THESIS.md`). SAM resolved each honestly and applied the concessions.

**Conceded + applied:**
- **CH-009 (base-rate) 🔴:** "no yield brings the buyer back / one-way reflexive street" is the widow-maker over-claim — the demand vacuum has been LIVE ~13 months (30Y record 3.20% → 3.76%, +56bp) producing an **orderly grind with carry thriving**, not a break. → "slow structural grind / orderly base case; acceleration is a tail, not the mode."
- **CH-010 (sign-tension) 🔴:** the **4.5% forced-SELLER mechanism is CONTESTED** — under economic-value J-ICS a duration-short lifer's solvency *improves* on a rate rise (textbook = duration-gap-closing BUYING). SAM's rebuttal (binding constraint = the *reported/accounting* asset-markdown, supported by observed net-selling + Nippon's −¥5.73T JGB unrealized loss) keeps the demand-*reduction*, but the specific 4.5% *acceleration* is single-sourced and the sign is unresolved pending the accounting basis. → flagged CONTESTED.
- **CH-011 (self-defeating route) 🔴:** the 30Y-4.5%-disorderly → carry-unwind route needs a *disorderly* spike, but the BOJ truncates disorder → **a thin Aug-2024-timing-window tail, not a named clean trigger.**
- **CH-012 (reflexivity) 🟠:** the vacuum is **consensus** (MOF already cut issuance to match it) → labeled a **regime-MAP, not a mispricing edge.**
- **CH-013 (thin evidence) 🟠:** ¥201B = one month/one B2 source; Uchida quote unverified; GPIF an admitted gap → flagged **load-bearing gaps** (not optional).
- **CH-014 (SAM-26 trap) 🟠:** re-installed a "30Y 4.5%" KEY THRESHOLD → **demoted to a contested-mechanism note.**
- **CH-015 (fuzzy falsifier) 🟡:** SAM-32's "intermittent doesn't count" → added a pre-registered ¥/month bright line.

**Survives:** the demand-*reduction* observation, the supply/demand reconciliation insight, the 2025 BOJ let-run precedent, and **SAM-32** (no *sustained* lifer re-entry through Dec-2026 — the slow grind, not the break). **Net altitude: "sharp new edge" → "sound but consensus regime-map with one over-claimed mechanism (4.5%) now contested."**

**Edits:** THESIS v1.6.2 (Pillar 2 RED-correction; KEY THRESHOLD demoted; tail-route downgraded); JGB package § RED CORRECTION; PREDICTIONS SAM-32 bright-line; KB-202 CONTESTED-flagged; STATUS/NEXUS/TRADE/STRATEGY/MEMORY softened; HENRY route-correction sent; `red/` files committed. **RED self-calibration:** flagged its own v1.5 CH-008 miss (called "BOJ frozen" → BOJ hiked, RESOLVED-DISMISSED); consciously avoided reflexive contrarianism this pass.

---

## 2026-06-30 — v1.6 → **v1.6.1** [MINOR] — JGB long-end DEMAND-VACUUM thesis EXECUTED; new carry-tail route + KEY THRESHOLD

**Author:** SAM. **Trigger:** Will-directed execution of the JGB long-end thread (scoped 6/29). Ran 3 parallel primary-source research legs (BOJ reaction function / MOF supply / lifer demand). **Minor bump (Y):** refinement — deepens Pillar 2 and adds a named carry-tail route + threshold; **no structural change** to the v1.6 carry-convexity-tail frame.

**What the research established (→ `research/outputs/JGB_SUPPLY_DEMAND_THESIS.md`, promoted scoping→executed):**
- **Demand (the driver):** J-ICS makes the lifer super-long bid *buffer-conditional* (rising yields mark down legacy low-coupon books *before* helping). Lifers turned net-SELLERS of super-long ~¥201B in May 2026; foreigners net-sellers (first outflow in 16mo). **No re-entry yield near current** (re-entry = 2-3yr rollover); reflexive **forced-selling zone at 30Y ~4.5%** = no buyer cushion + a self-reinforcing seller trigger above. Auctions confirm (30Y BTC 2.94x Jun-10; 40Y 2.54-2.76x 2026).
- **BOJ backstop (central risk) = conditional LET-RUN:** pace-not-level reaction function; lets a gradual move through 4.0% (2025 precedent: let 30Y run +100bp to a record uncapped), caps only a *disorderly* spike. Risk survives but is velocity-conditional.
- **Supply = forward amplifier, NOT the current cause:** FY2026 gross super-long CUT to ¥17.4T (17-yr low) to match dead demand → net supply *lower* YoY; reloads FY2027+ (taper-pause floor + Takaichi fiscal + reflationist board). The "supply shock" is a DEMAND collapse dressed as supply.

**THESIS edits (v1.6.1):** (1) Pillar 2 — new bullet recording the executed demand-vacuum thesis (demand/BOJ/supply legs + signal-only + routing). (2) § THE CARRY-CONVEXITY TAIL — added the **JGB-disorderly → carry-unwind route** (folded into the risk-off/residual family; does NOT change the headline EV table; the candidate most able to re-couple SAM-31). (3) KEY THRESHOLDS — new row **JGB 30Y 4.5% (disorderly)**. (4) CROSS-AGENT LINKS — added → BOND (primary), annotated → LIQUID (conditional/dormant). **Tradeability = SIGNAL-ONLY** (no Will-tradeable JGB-bear vehicle).

**Cross-agent:** routed 2026-06-30 (direct to inboxes, Will-authorized) → **BOND** (primary, term-premium spillover) / **LIQUID** (conditional — repatriation leg DORMANT, don't double-count Pillar 2 as a Channel-1 re-arm) / **HENRY** (new carry trigger: 30Y 4.5% disorderly). **New OPEN prediction SAM-32** (lifer non-re-entry; mechanism-based, not a threshold bet).

**Also this session (no thesis change):** vol-check clean-source correction — the FXY proxy (16.07%) misled; true USD/JPY implied vol ~sub-10 (~7.9 Jun-23) ≈ realized → long-vol is a *defensible small convexity ticket, not cheap-vol arbitrage* (KB-183 confirmed). USD/JPY 162.40 fresh 40-yr low via orderly grind; intervention line re-anchored 160→162 (ING); MOF silent 14d. No re-mark.

---

## 2026-06-29 — POSITION RECONCILED TO FLAT (no version change) + new primary thread: JGB long-end supply/demand

**Author:** SAM. **Trigger:** Will confirmed 2026-06-29 that SAM holds **NO current FXY position** (the docs had carried a phantom 6-sh post-trim stub since the 6/22 trim, fill "unconfirmed" 6/25). **No analytical/conviction change** — the v1.6 carry-convexity-tail is unchanged as a *view*; only the operative posture flips.

**THESIS edit:** added a FLAT banner to § POSITION VIEW — the section is now the WATCH-FOR-ENTRY / re-entry reference, not a live holding. At MEDIUM/break-even the tail is NOT EV-positive to initiate; re-entry gated on a fired trigger (disorderly MOF spike / CFTC through −153K/85% / risk-off yen-haven re-couple / Fed-dot walk-back). SAM-28..31 reframed as entry-triggers. Reconciled across all live surfaces (STATUS/TRADE/NEXUS_BRIEF/STRATEGY); **no money fields fabricated.**

**Direction pivot:** with the carry trade spent/break-even and SAM flat, effort pivots to the only-pillar-still-firing — **Pillar 2 (J-ICS lifer long-end abandonment) + the reflationist-board/Takaichi fiscal supply side = a DOMESTIC JGB long-end supply/demand thesis** (scoping: `research/outputs/JGB_SUPPLY_DEMAND_THESIS.md`; gated on tradeability + the BOJ-backstop question). Best *current* actionable idea assessed = non-directional **long JPY vol** IF it prices cheap on a clean source (FXY proxy 11.78%, up off the 9.40 post-FOMC trough — unconfirmed); directional trades all break-even / negatively-skewed / gated / un-triggered.

**Data this session (no re-mark — within-band / confirmatory):** CFTC Jun-23 −146,104/81.2% (first cover off the 83.4% top); Tokyo Jun CPI core-core 1.9% sticky; BOJ SoO hawkish-of-priced; USD/JPY 161.96 (40-yr low, orderly grind); Brent $73.85.

---

## 2026-06-22 — v1.5.1 → **v1.6** [MAJOR] — re-centered COMPRESSION → CARRY-CONVEXITY-TAIL; pillar audit; Channel 1 RETIRED; Channel 4 NEW; 6-of-6 RED challenges converged

**Author:** SAM. **Trigger:** Will-directed v1.6 re-underwrite (drafted Jun 18 backbone → finalized post Jun-19 National CPI + the Jun-22 CFTC EV-gate + the SAM⇄RED dialogue). **Major bump (X):** structural thesis change — the dominant route is re-classified (compression → positioning-convexity) and Channel 1 is retired. **Process:** finalized by folding `V16_RED_DIALOGUE.md` (6 pre-registered RED challenges + #1a-d + the #4 gate), **converged 6-of-6 on 2026-06-22 ~5:20 PM ET** (near-full convergence in one round-trip). DRAFT (`THESIS_v1.6_DRAFT.md`) superseded → flag `git rm` at commit; v1.5.1 archived → `thesis/THESIS_v1.5.1_ARCHIVE.md`.

**The decision-grade observable that gated this (CFTC Jun-16 EV-gate, in hand Mon Jun 22 3:30 PM ET):** net **−150,132 / 83.4% of cycle peak**, built −4,314 WoW, **zero cover through the catalyst.** Maps to the pre-registered HOLD-band top edge (78-83%) → **frame SURVIVES the margin test** (the decisive negative — cover <−120K → trim/close — did NOT occur), but 2,868 contracts / 1.6pp shy of the −153K/85% *strengthened* line, so the amplifier stayed +5pp (not +8-10pp). Positioning held *through* the spent catalyst = genuine empirical Pillar-4 confirmation.

**Old view (v1.5.1):** yen strengthens via rate-differential COMPRESSION (BOJ hike + Fed-cut multi-month tail) + structural pillars; Channel 2 (June BOJ) = dominant remaining near-term trigger; Channel 1 = DEFERRED structural backstop; conviction direction/level HIGH, near-term timing MEDIUM.

**New view (v1.6):** the compression vector is broken near-term (Pillar 1 directional vector INVERTED — BOJ +25bp < Fed Jun-17 +40bp dot; Fed-cut → Fed-HIKE regime under Warsh). The live thesis is a **carry-trade CONVEXITY TAIL**: CFTC at 83.4% peak held through the spent catalyst, pays asymmetrically IF any of N tail-routes fires inside a **bounded eligibility window (LOCKED Sep 18 2026)**. **Conviction: direction/level MEDIUM (↓ from HIGH); near-term timing LOW (↓ from MEDIUM); convexity-tail MEDIUM (new row; downgraded from the draft's MED-HIGH per RED #1 — honest net 60d EV ≈ break-even-to-slightly-negative → analytically a TRIM signal, not an add).**

**The 6 folded RED verdicts (all SAM-conceded/locked, RED-ratified):**
- **#2 (single-point-failure) — SURVIVES:** the SPF is TWO-LEGGED — cover <−108K (a tail) AND no-trigger-by-Sep-18 (the MODE, >50%). Both bounded. The binding leg is leg-2 (the window), not the cover.
- **#3 / #5 (window) — SURVIVES:** eligibility window LOCKED **Sep 18 2026** (≈90d; captures Jul-31 BOJ + mid-Sep FOMC, neither as deadline). Disposition: ≥80% fuel AND no trigger by Sep 18 → retire to LOW; cover <−108K → LOW.
- **#1 (convexity grade) — BROKEN at MED-HIGH / SURVIVES at MEDIUM:** my own EV-gate placed it at MEDIUM (didn't cross the 85% strengthened line); the conceded #1b haircut (+7%→+5% magnitude) takes center-case net to break-even-to-negative, failing the EV-positive bar. #1a "pick one" conceded → risk-off contributor +0.70% → ≈ +0.45% (keep +7% magnitude, drop prob to ~6-7%; the channel decoupled Jun 11). Flip-up: CFTC through −153K/85% OR yen-haven re-couples.
- **#6 (Channel 1) — RETIRE (was "deferred"):** 4-of-4 grew US credit + no specified path = retired in all but name. Re-add tripwire = the DIRECT observable: net foreign-credit SALES across ≥2 consecutive disclosure windows at ≥2 of {Big-3 mutuals, Norinchukin}. JGB-30Y/ESR = accelerant co-conditions only (JGB-30Y is Pillar 2's DOMESTIC mechanism — re-arming Channel 1 on it double-counts Pillar 2). Closes the Will-directed deferred→retired re-examination.
- **#4 (vehicle, GATE) — RESOLVED:** a break-even MEDIUM frame doesn't pay a vol structure's spread/theta/complexity → vehicle-change options (b) FXY-vol overlay / (c) USDJPY-put=JPY-call **do NOT propagate**. Finalize decision-set narrows to **(a) hold-with-tighter-stop / (d) trim** (Will's sizing call). Re-opens only if #1 reclaims MED-HIGH OR FXY-vol confirmed-cheap on a clean source.

**Pillar audit:** P1 LEVEL alive / VECTOR broken (directional claim deleted); P2 ALIVE (only pillar still firing; DOMESTIC, multi-quarter anchor); P3 alive-in-fact / WEAKENED-in-proximity (USDJPY moved farther from <145); P4 ALIVE — promoted to the v1.6 center (Channel 4 POSITIONING-CONVEXITY).

**Channel re-classification:** Ch1 → **RETIRED** (direct foreign-SALES re-add tripwire); Ch2 → **CARRY-CONVEXITY TAIL** (renamed); Ch3 → **MOF #3 DECAYING** (~15-20%/30d; reaction function = disorder-not-level); **Ch4 POSITIONING-CONVEXITY = NEW, the center.**

**Surfaces touched this finalize (chunk 1):** THESIS.md (full rewrite → canonical v1.6); THESIS_v1.5.1_ARCHIVE.md (created); THESIS_v1.6_DRAFT.md (superseded banner); this CHANGELOG entry; V16_RED_DIALOGUE.md (converged/closed). **Held for Will's sizing call (chunk 2):** STATUS banner re-center, STRATEGY/TRADE position re-derive + stop, PREDICTIONS new convexity-tail tripwire rows, cross-agent SIGs (LIQUID Ch1-retired / HENRY convexity-MEDIUM + cross-pair decoupling), NEXUS_BRIEF refresh, evals re-baseline.

---

## 2026-06-18 — [propagation/thesis-fact] Three verified facts landed: Warsh-Fed regime + FOMC dot revision (Pillar 1 RE-WIDENING) + Iran/US deal SIGNED — Iran docket unfrozen

**Author:** SAM (Will-directed FIRST pass — facts only, no conviction/sizing change; v1.6 re-underwrite follows tonight after Fri National CPI).
**Action:** No version bump — this is a propagation pass, not a thesis rewrite. The structural re-frame ("re-center compression → carry-unwind-tail; near-term direction inverted; tail intact-to-stronger") is the **v1.6** entry queued for tonight per Will. This entry records the three confirmed facts the v1.6 re-derive will rest on.

**Fact 1 — Fed Chair = WARSH since May 22.** Confirmed by Jun 17 FOMC (debut chair; fed.gov statement + presser via Reuters/Yahoo/Bloomberg). Style: statement-gutting hawkish — **rewrote the FOMC statement ~300 → ~130 words, removing forward easing bias entirely** ("extent and timing of additional adjustments," balance-of-risks language, easing bias). Added Middle East uncertainty + supply-shock inflation framing + "the Committee will deliver price stability." Refused to dot himself: forward guidance "not well suited for the current policy conjuncture." On 2% target: "I see no reason, until we have reestablished our commitment and ability to deliver on the 2% inflation objective, to revisit that." No FX / coordination language. **This Chair change has been live for ~4 weeks and sat un-modeled in SAM's docs through 4 boot cycles** — surfaced today by the Will-directed news sweep. Boot-sweep gap logged to auto-memory.

**Fact 2 — FOMC Jun 17 held but the SEP confirms a regime flip (Pillar 1 directionally inverted).** Decision: 3.50-3.75% unanimous 12-0 (April's 4 dissenters dropped because the easing language was removed). **SEP: 2026 median dot 3.4% → 3.8% (+40bp), implying ≥1 hike; 9 of 18 dots see hike (6 see TWO), 8 hold, 1 cut.** Core PCE 2026 +60bp to 3.3%; headline PCE +90bp to 3.6%. 17 of 18 see inflation risks to upside. 2027 median 3.6%; long-run ~3.1% (modestly up). U/E cut to 4.3%. **CME FedWatch July hike ~75%; Polymarket "Fed hike 2026" ~52% → ~56%.** Market: DXY ~100.40 (broke 100); 2Y +16bp to 4.216%; 10Y +6bp to 4.49%; 30Y up (bear flattener); S&P −1.21%; Nasdaq −1.34%; USDJPY 160.78 Wed close → **161.34 Thu** (no MOF response in 48h+, Bloomberg "Markets Alert for Japan Intervention" Wed).

**Old view (v1.5.1 § Pillar 1 + § Independent Catalyst):** "Compression requires either Fed cuts (multi-month tail per § INDEPENDENT CATALYST, Jun 17 reads >97% no-change) or BOJ hikes (Jun 16)." Fed-cut secondary path = multi-month tail; SAM-side carry tripwire = "any walk-back of cut path." Even a 25bp BOJ move only compresses the gap by ~9% of the differential — meaningful as confirmation, not full resolution.

**New view (verified Jun 17-18):** Across the Jun 16-17 sequence, **the BOJ +25bp compression was MORE than offset by the Fed Jun-17 dot +40bp move — rate-differential is now WIDER than pre-Tue, not narrower**. Pillar 1's structural-LEVEL argument ("the *level* of the gap is the carry") survives; what's broken is the directional vector. Multi-month US-credit-cascade → recession → cuts tail still live theoretically (BCRED ~12%, Ares ~14% Q2 redemption peak) but requires breaking the new Warsh inflation-first frame. SAM-side carry tripwire moves from "Fed-cut surprise" to **"any walk-back of the Jun-17 dot revision"** — Powell-era cut-pricing dynamics no longer apply under Warsh.

**Fact 3 — Iran/US deal SIGNED Wed Jun 17 (Pezeshkian + Trump, ELECTRONIC per Al Jazeera) — initial agreement; signing-binary resolved; verification leg OPEN.** Pakistan PM Sharif confirmed "enters force immediately." **NOT a Geneva/Switzerland ceremony** (sweep overclaim corrected at Step 1.5 — see § Step 1.5 reconcile below). Terms: **60-day toll-free Hormuz reopen, THEN Oman-administered fees** (per NBC); US lifts naval blockade; Iran dilutes HEU; sanctions waived (not terminated); 60-day nuclear negotiation window. **Per CNN: this is an *initial* agreement — "tougher talks lie ahead" on the verification leg.** **Iran formal: YES on signing-binary** — Pezeshkian electronic signature is the primary-source threshold the Jun-12 framework lacked. Thu Jun 18: Hormuz reopening process begun Day 110 — initial traffic resuming (4 supertankers transiting incl. first Saudi-owned vessels since Day 1; backlog "weeks to clear"); US naval blockade lifting. **Verification leg OPEN: demining, insurance restoration, traffic normalization, Oman fee-administration negotiation (60-day toll-free closes ~Aug 16), HEU dilution compliance, sanctions-waiver rollout.** **Iran docket UNFROZEN on signing-binary per Will's instruction** — prior committed-doc caveats ("digital MOU signed / Iran confirmed / Geneva ceremony — not hardened until primary-source") are satisfied on the signing-binary; implementation watch active (NOT formally closed). Brent reaction: $79.68 Thu — split half deal-signing, half **IEA glut warning (+8 mbpd supply by 2027 vs +2 mbpd demand)** — durable bearish-oil regime developing independent of ME. Sources: Al Jazeera (electronic-signing confirmation), CNN (initial-agreement / tougher-talks framing), NBC (toll-free-then-Oman), NPR, CNBC, Rigzone (Hormuz traffic).

**Step 1.5 — HAWK-Iran reconcile across committed docs (same session, separate commit; the propagation pass above had embedded sweep overclaim language; this section closes the gap before LIQUID/HENRY network re-mark or v1.6 ingests the Iran framing).**

The original Jun 18 propagation pass embedded sub-agent overclaim language ("Switzerland signing ceremony scheduled," "Phase 1 mechanism formally dormant," "All 3 watch conditions met ✅," "physically reopening Day 110," "4 supertankers transiting") in ~10 spots across THESIS (banner L4, catalyst row L212), STATUS (banner L3, thresholds L292), CHANGELOG (Fact 3 above), and CALENDAR (banner L3, intervention row L51, phase-2 row L79, **load-bearing geopolitical row L104**, lineage L107, recently-resolved L131). HAWK's Jun 18 re-mark (commit c677cd0a, pushed earlier today) carried the primary-source-correct framing: electronic signing (Al Jazeera), initial-agreement-not-final (CNN), 60-day toll-free THEN Oman-administered (NBC). PROME+ORC adjudicated the SAM-vs-HAWK conflict on primary sources, concurred with HAWK, and directed Step 1.5: adopt HAWK framing across the ~10 instances before any further propagation.

**PROME's verifier-side calibration note (preserved here because it's load-bearing for future passes):** PROME initially sampled CALENDAR L51 only and read the FIRST pass as "clean on Iran"; SAM's comprehensive `grep -nE "Switzerland|signing ceremony|4 supertankers|physically reopening|enters force"` audit caught the 10 spots (including the most-load-bearing L104 "All 3 watch conditions met ✅ / Phase 1 mechanism formally dormant" — the line that would tell any downstream agent the oil-shock is *closed*). PROME confirmed the miss, named it as the third incomplete-manual-grep instance this session, and named SAM's comprehensive-grep discipline as the correct standard. PROME ran the mechanical grep-all post-push as the verifier-side audit.

**Step 1.5 scope (applied):** drop ceremony/all-watch-met/formally-dormant; soften "physically reopening" → "reopening process begun"; add verification-leg-open hedging (demining/insurance/traffic-normalization/Oman-fee-administration) + "60-day toll-free then Oman-administered"; keep the SIGNED binary and Iran-docket-UNFROZEN. **Yen conclusion unchanged** (oil-shock still not a near-term yen-positive catalyst; near-term modal direction inverted by Warsh/FOMC, not by Iran). Step 1.5 is an accuracy gate, not a thesis-blocker.

**Surfaces touched (propagation scope):** THESIS banner + § Pillar 1 + § INDEPENDENT CATALYST: FED CUT PATH + Catalyst Sequence Forward (Iran row → ✅ SIGNED). STATUS banner + new § FOMC JUN 17 RESOLVED block (parallel to § BOJ JUN 16 RESOLVED) + § SECONDARY PATH section + § Key Thresholds (USDJPY/DXY/Brent rows, plus a 🆕 Fed Chair regime row in tripwire table). CALENDAR Jun 17 FOMC row + Iran/Hormuz MOU watch row + RECENTLY RESOLVED additions. Auto-memory: month-old Chair change boot-sweep-gap note.

**Held — NOT in this pass (per Will scope: facts only, no conviction/sizing):**
- Carry-unwind buckets (7d/23/32) — not re-marked; THESIS METHOD anchors not re-pencilled; ship to LIQUID/HENRY held for NEXT-step network re-mark.
- Position sizing / stop re-spec — held (Will-decision in NEXT).
- v1.6 thesis re-derive (re-center compression → carry-unwind-tail; FXY-spot-vs-vol vehicle question) — drafting tonight after Fri National CPI; this entry is the fact foundation it rests on.
- Channel 2/3 prose, Aug-2024-tail references, STRATEGY § Takaichi-ceiling-discount scoring — all queued for v1.6.

**Calibration significance:** Boot-sweep gap on a confirmed Chair change of ~4wk duration is a sub-thesis-level miss — Warsh is a different model than Powell (statement-gutting, no forward guidance, "no reason to revisit the 2% target"). Promoted to auto-memory as a process lesson (`finding_boot_sweep_macro_regime_context`); fix proposal = add a macro-regime-context check (Fed Chair, BOJ Gov, key personalities, last-Fed-statement style) to the boot baseline. Independent of the position outcome — this is workflow-grade.

---

## 2026-06-16 — 🔴🔴 BOJ HIKES TO 1.00% AS PRICED — dominant remaining catalyst resolved; no carry unwind (CH-004 confirmed); 4 June predictions closed

**Author:** SAM (live-event resolution; decision + reaction primary-verified — CNBC/TradingEconomics/Reuters-via-Yahoo/ING)
**Action:** No version bump — this is the resolution of the v1.5/v1.5.1 dominant-catalyst binary, not a structural rewrite. The structural re-underwrite is the planned **v1.6** (post Jun-18 $58C settle, RED pass before commit). This entry records the resolution; v1.6 folds it into thesis structure.

**Old view (Sun Jun 14 frozen marks):** Jun-16 BOJ = dominant remaining near-term catalyst, single-path under v1.5; SAM-21 ~90% hike; modal delivered-as-priced package = FXY −1 to +2% + vol crush + no unwind; hawkish-of-pricing tail (~10%) = +5-8%/unwind-fires; hold (~10%) = −3-5% event-capped. Pre-registered exit: sell-into-the-Tuesday-IV-pop.

**New view (resolved):** BOJ **hiked 25bp → 1.00%** (highest since 1995), **vote 7-1 with Asada dissenting for a HOLD** (dovish-side dissent — opposite of Apr-28's 3 hawkish dissents), growth + inflation outlook **raised**, **Uchida fronted the presser** for the absent (hospitalized) Ueda with "further hikes expected but not imminent" guidance + boilerplate FX line. **This was the MODAL delivered-as-priced outcome, NOT the hawkish-of-pricing tail.** Market: USDJPY WEAKENED to 160.36 (+0.25%), FXY flat ($57.22), JGB 10Y ~2.6%/30Y ~3.78% (+~1-5bp), Brent $80.51 (−3.2%). **CH-004 confirmed in live tape — a fully-priced hike did not unwind carry (buy-rumor-sell-fact); the 81%-of-cycle-peak CFTC fuel load was not lit because there was no surprise to light it.** The dominant near-term trigger is spent; the long thesis from here rests on the v1.5.1 § STRUCTURAL PILLARS, not on a catalyst.

**Predictions resolved (PREDICTIONS.tsv → 9 CONFIRMED / 10 FAILED / 1 special / 0 OPEN):** SAM-21 (June hike) ✅ CONFIRMED; SAM-24 (25bp not 50bp) ✅ CONFIRMED; SAM-23 (MOF intervention #3 by June BOJ) ❌ FAILED — *calibration win*, pre-marked 72%→~30% on CH-011 (disorder-not-level; 8+ orderly sessions at 160+, no strike); SAM-26 (30Y ≥4.0% through meeting) ❌ FAILED — pre-marked 70%→~25%, threshold-vs-mechanism.

**Position:** No action (Will's call). 13 shares HOLD (structural; FXY $57.22 ≈−$14 unrealized). Jun-18 $58C salvage thesis weakened — no IV-pop to sell into; likely near-total loss vs modeled $5-10. Stop $55.05 does not fire (AND-condition's "BOJ dovish" leg false).

**Queued for v1.6 (post Jun-18 scoring):** (a) oil-channel-DORMANT relabel; (b) SAM-23 framework re-anchoring (driver/disorder dimension + no-strike decay); (c) Takaichi-ceiling discount disposition (delivered hike reclassifies SAM-08/20 as TIMING failures; the Jun-16 dovish-side dissent + "not imminent" guidance is fresh evidence for the *retire-to-friction / modify* branches over vindicate-widen — score by Jun 18 EOD JST per STRATEGY); (d) Channel-1 deferred-vs-retired; (e) position re-underwrite incl. FXY-vehicle question.

**Same-session true-ups (Orc + Prome Jun-16 commit review — interim stale-line fixes, NOT v1.6):** (1) § OIL-IN-YEN "Current state" para + RISK FACTORS oil-shock row relabeled from stale "Phase 1 rebuilding / Brent re-accelerating / MOU collapse branch" → "Phase 1 RECEDING / oil-in-yen DORMANT / de-escalation branch" to match STATUS/CALENDAR/TRADE (Brent ~$80; the lines were factually inverted and self-contradictory vs the same section's Jun-15 energy paragraphs). (2) § STRUCTURAL COUNTER-FLOW NISA figures flagged for reconciliation (¥6T-total/qtr ≈ ¥2T/mo vs the ¥1T/mo foreign-equity-subset cite) + Nomura "half of 2024 USDJPY rise" attribution flagged unverified-vs-primary. (3) SoftBank $ specifics tagged cross-domain (verify at CARL/HENRY/BROCK-HANS). (4) STATUS JGB post-decision line softened — no authoritative print until MOF CSV ~Jun 17 (don't assert rally-vs-selloff; QT-soften argues mild rally). (5) Iran language held caveated per review — not hardened. **Note:** Orc's "add SAM-23 →~30% to trajectory" was already satisfied in the Jun-16 write-back (row reads …→~72%→~30%); Orc's review predated that commit.

---

## 2026-06-10 (evening) — v1.5.1 follow-on: RED pre-BOJ packet remainder (CH-010/011/032) — Branch C split, SAM-23 re-derived ~35 pending, target band reclassified conditional-tail

**Author:** SAM (Will-directed; responses pre-blackout per RED's filing discipline). Canonical: `research/2026-06-10_ch010_011_032_responses.md`. Companion to the CH-009 re-derivation (same day).
**Action:** No version bump. **No mark changes tonight** — all re-derivations apply at the Sat Jun 13 consolidated re-mark (now five inputs: CFTC gate, taper-pause tail-shrink, Fed anchor→~0, SAM-21→~90 per CH-009, SAM-23→~35 per CH-011), each with pre-registered void conditions.

1. **CH-010 ACCEPTED — Branch C split applied to STRATEGY disposition (scoring frame, pre-event):** C1 political-attribution hold = vindicate/widen as written; C2 fiscal/long-end hold = ceiling discount NOT vindicated, CH-008 scores instead; C-ambiguous = provisional 10-15pp + mandatory post-mortem. One hold cannot pay both frames.
2. **CH-011 ACCEPTED IN SUBSTANCE — SAM-23 re-derived 72% → ~35% (band 25-45), apply Sat Jun 13.** Old view: 160 = hard trigger, intervention #3 ~72% by Jun 16. New view: MOF's trigger is *disorder, not level* — 4 trading days at/above 160 with no strike falsifies the level-anchor as sufficient; orderly USD-driven tape (normal intraday ranges, cross-pair yen bid) lacks both G7 cover and efficacy (CH-003); post-hold spike — the high-P(strike) branch — lands outside the "before June BOJ" scoring window. Posture evidence (Katayama verbals, Bessent alignment) survives as P(strike|disorder), not P(strike). Absorbs carry-forward #6: trigger-spec re-anchoring (driver/disorder dimension + no-strike decay clause) to post-Jun-16 entry. Downstream: MOF #3 is top bucket contributor — 7d ~14%→~10-11%; 30d/60d MOF anchor restructured scenario-weighted at the same pass; buckets ship to LIQUID/HENRY Saturday.
3. **CH-032 ACCEPTED DIRECTIONALLY — target band reclassified (interim flag, not rewrite):** old view: $60-62 / USDJPY 148-152 as the 6-month target "grounded in pillar math." New view under Fed-hike regime: modal 3-6mo ≈ **FXY $57.5-59.5 / USDJPY 154-160** (~25bp net differential compression, cross-pair demand, intervention topside cap); **$60-62 = conditional-tail ~25-30%** via four routes (hawkish-of-pricing BOJ / US credit event / risk-off cascade through positioning / Fed-pricing unwind). Pillar audit: P1 inverts, P2's forcing job done/priced, P3 gated with no modal path to 145, P4 amplifier-without-modal-trigger (pushback recorded: short-cover washout is mechanically yen-POSITIVE — RED's point survives as "fuel can dissipate quietly"). Hold-row backstop language replaced in STRATEGY. Conditional on Sat Fed-pricing re-verify; full pillar re-derivation = v1.6 (after Jun 16-18 scoring, RED pass before commit).
4. **Standing:** CH-004 RESOLVED-CONVERGED concurred; VX-RED-024 concurred (fully-priced BOJ = no US-paper transmission in modal branch).

---

## 2026-06-10 (PM) — v1.5.1 follow-on: Norinchukin FY2025 gate RESOLVED NOT REACTIVATED — Channel 1's last near-term reactivation candidate closes; "¥9.7T shrinking" claim falsified

**Author:** SAM (Will-directed pull; primary-source verified before propagation per [[finding_ohlc_verify_before_session_claims]] discipline)
**Action:** No version bump — Channel 1 status (DEFERRED) unchanged; a watched gate resolved and a factual claim corrected. Surfaces swept: THESIS Channel 1 bullet + CROSS-AGENT → LIQUID line + Risk Factors row, TRACKER (7 spots), `insurers/norinchukin.md` (full refresh — now canonical), STATUS, TIMELINE, FLOW-JPN-3.01, LIQUID outbox signal.

**Old view:** Norinchukin CLO ¥9.7T (Sep 2025 peak) shrinking — ¥500B Q1 2026 decline "fastest on record" (CreditFlux); Jun FY2025 disclosure = last near-term Channel 1 reactivation gate, watching for reduction target / decline acceleration / US-credit stress framing.
**New view (bank primary disclosure, tanshin + supplement May 21 2026, surfaced Jun 10, figures verified by direct PDF extraction):** CLO book at **record ¥10.1T Mar 2026, +¥1.8T YoY** (Mar 25 ¥8.3T → Sep ¥9.7T → Dec ¥9.8T → Mar 26 ¥10.1T — never declined); net income ¥121.4B beat ¥30-70B guidance; CET1 17.81% improved; no reduction target, no stress framing (Iran-macro only); First Brands consolidated hit ~¥61B equity-method one-time (¥150.5B was JA Mitsui Leasing level). **All three reactivation conditions failed → gate CLOSED.** CreditFlux decline claim contradicted by bank's own yen figures (basis unresolved, single-source); older ¥8.2T figure was Dec 2024, superseded.

**Calibration significance:** 4-of-4 Japanese institutions (Big 3 mutuals + Norinchukin, *distinct mechanics*) resolved 2026 disclosure windows by GROWING US credit exposure — extends the SAM-14/19/25 mechanism-direction failure cluster. Cautionary CEO rhetoric (Kitabayashi Nov 2025) ≠ cautious balance sheet. **Post-BOJ agenda (Will-directed): re-examine the Risk Factors Channel-1-reactivation 10% row and whether "deferred" should become "retired pending new mechanism."** Known-unknown logged: UST/foreign-bond split not broken out (parent bonds ¥19.2T → ¥21.0T, composition undisclosed). Coverage-gap note: results were public ~3 weeks before SAM surfaced them (IR HTML 403s automated fetch; direct PDF URLs work) — third coverage-gap instance this week; `insurer_quartr.py` priority bumped in infra queue.

---

## 2026-06-10 (AM) — v1.5.1 follow-on: Takaichi-ceiling discount pre-registered for disposition at Jun-16 + Fed-pricing regime flip logged

**Author:** SAM (Advisor-prompted, Will-approved)
**Action:** No version bump. Two pre-blackout calibration moves:

1. **Ceiling-discount disposition pre-registered** (canonical: `STRATEGY.md` § TAKAICHI-CEILING DISCOUNT DISPOSITION). Trigger: swaps price 92.5% of a second hike to 1.25% by Dec (Tokyo Tanshi via Reuters Jun 9) + Reuters May 7-14 economist poll median 1.25% Q4 2026 / 1.50% Q3 2027 — market AND economist consensus now treat the ceiling as dead above 1.00%, in direct conflict with THESIS terminal-rate view ("0.75% political ceiling, NOT market consensus 1.25-1.5%"). Three mechanical branches (retire-to-friction 5-10pp / modify 10-20pp / vindicate-widen 25-30pp), scoped to post-June path marks only, scored by Jun 18 EOD JST. Pre-registered calibration insight: a delivered June hike reclassifies SAM-08/SAM-20 as TIMING failures (ceiling delays, doesn't block). Sato 3→2 board tension kept in-spec as within-branch modulator. **THESIS terminal-rate language not edited pre-event — disposition governs how Tuesday updates it.**
2. **Fed-pricing regime flip (cut→hike) logged:** Polymarket ~52% Fed hike in 2026 (Oct frontrunner); secondary path now inverted, not just dead. Pillar 1 post-June compression burden falls on BOJ alone. METHOD anchor #4 (Fed-cut) → ~0 at Sat Jun 13 re-mark. CHANGELOG candidate matures to full entry if pricing holds through the re-mark.

**No probability re-marks** (SAM-21 75%, SAM-23 72%, buckets held for Sat Jun 13 expanded scope). Will decided HOLD on the Jun-18 $58C (salvage ~$5-10 dominated by modeled EV ~$20-25); companion tail-estimate test logged (market ~3-4% vs SAM ~10% hawkish tail) for scoring with the ceiling branches.

---

## 2026-06-09 (PM-late) — v1.5.1 follow-on: priced-hike reconciliation (catalyst-row payoff language aligned with CH-004)

**Author:** SAM (Will-directed)
**Action:** No version bump. Completed the v1.5.1 narrative reconciliation that the Jun-3 pass missed on the catalyst-sequence rows: 7 surfaces (STATUS WHAT TO WATCH, TRADE Key Dates, STRATEGY asymmetry table, CALENDAR Jun-16 row, CATALYSTS.tsv Jun-16 rows, THESIS catalyst sequence, MEMORY next-session) still said *"Hike to 1.00% = structural FXY +5-8%; carry unwind fires"* — contradicting the CH-004 METHOD (a delivered-as-priced hike does not unwind) and the Jun-9 taper-pause leak (QT leg pointing dovish → modal package = balanced hike + QT-soften).

**Old view (catalyst rows):** hike delivers +5-8% FXY and fires the carry unwind, unconditionally.
**New view (pre-registered before the meeting):** modal package (priced 25bp + QT-soften; ~65% all-in) = **FXY −1 to +2%, vol crush, no unwind**; hawkish-of-pricing branch (~10% all-in, shrunk by the taper-pause leak) is where +5-8%/unwind-fires/Aug-2024-speed lives; hold (~25%) = −3-5% event-capped. **Event ~EV-flat at ~98% market pricing** — position value = call convexity on the hawkish branch + shares' 3-6mo structural grind. Jun-18 $58C modal outcome: loses most of $40 even with the hike delivered (sell-into-pop = salvage); entry edge (May 21, hike ~55-65%) was consumed by the repricing to ~98%.

Canonical table: `STRATEGY.md` § JUN-16 RECONCILED EXPECTATION. **No probability re-marks** (SAM-21 75%, SAM-23 72%, buckets unchanged); this is expectation-language alignment, not a view change — the METHOD already encoded it.

---

## 2026-06-04 — v1.5.1 follow-on: Jun 3-4 cabling-window news ingestion + OS.1 closure + Sato corrections

**Author:** SAM
**Action:** No version bump. Three follow-on updates to v1.5.1: (a) ingest the Jun 3-4 pre-blackout cabling-window news into STATUS; (b) close OS.1 (fiscal-dominance counter-frame) as largely-falsified for SAM-21 binary; (c) correct the Sato BOJ-board entry date and framing across THESIS / STATUS / CALENDAR / CATALYSTS. **No view change, no probability re-rates, no position change.**

### (a) Jun 3-4 cabling-window news ingested

News-sweep findings (4 parallel agents Jun 4 AM, primary-source verified):

| Signal | Source | Implication |
|---|---|---|
| **Bloomberg sources-leak** Jun 4: "BOJ Is Said to Mull June Rate Hike With Another Possible in 2026" | Bloomberg primary | Substantive pre-blackout leak; not common rumor — officials see scope for additional hikes beyond 1.00% |
| **Ueda Kisaragi-kai speech** Jun 3 (final scheduled pre-blackout event): "BOJ will continue to raise the policy interest rate at an appropriate pace… upside risks to prices appear to be greater overall and are likely to emerge sooner" | BOJ ko260603a | Explicit hawkish-of-pricing pre-blackout placement |
| **Takaichi verbal** Jun 3 at USDJPY ~160.07: govt "stands ready to respond to excessive exchange-rate movements when necessary" | Reuters / Yahoo / MarketScreener | **Reads as intervention-permission, NOT Takaichi-ceiling pushback** — affirmatively closes "no Takaichi/cabinet pushback" pre-condition of the Jun-9 mechanical trigger |
| **Polymarket built 94.8% → 96.9%** | Polymarket Jun 4 | 3rd sequential build (Tue 87.6 → Wed 94.8 → Thu 96.9); swap cross-confirms ~86%, Kalshi ~80%; no print regression |
| **Brent 2nd down session** −0.86% to ~$96.97 | Trading Economics Jun 4 | Cumulative from Jun-3-baseline ≈ +0.2% (flat). SAM-23 mark-DOWN conjunction direction-leg firing but cumulative <−2% NOT met. |
| **Israel-Lebanon conditional ceasefire** Jun 4 | Al Jazeera + Haaretz | Removes ONE of Tehran's two stated grievances for message-exchange suspension; walk-back precondition improved but NOT delivered |

**SAM-21 HELD at 70%.** The multi-source corroboration (sources-leak + Ueda + Polymarket build + Takaichi-as-permission) is genuinely stronger than the Polymarket-only Jun-9 condition the trigger spec'd. **But the discipline was deliberately set to NOT chase pre-blackout cabling** — sourced leaks + scheduled speeches are exactly what the cabling window produces. Pre-registration value comes from holding through "but this time is different" pressure. Discretionary fire-early path was offered to Will; Will elected hold per discipline. Discipline credibility preserved.

**SAM-23 HELD at 72%.** Mark-DOWN conjunction partially firing (Brent direction + Israel-Lebanon precondition removal) but full trigger NOT met. Mark-UP conjunction not firing.

### (b) OS.1 (fiscal-dominance counter-frame) CLOSED — largely-falsified for SAM-21 binary

OS.1 was re-homed from a generic NEXT-SESSION bucket to a scoped pre-Jun-9 thesis task (Will-directed Jun 3 PM) because it directly gates the SAM-21 mechanical +5pp trigger. The Jun 3-4 news ingestion directly answered all three of Will's scoped questions:

- **(a) Market repriced UP THROUGH fiscal news?** YES. BOJ officials openly cabling hike-plus-more-hikes WITH Takaichi government's verbal intervention-permission. The Takaichi ¥3T budget (May 25) and fresh-debt 10Y-to-2.8% reports did not stop the repricing.
- **(b) Inside the 70% or un-priced discount?** Inside. The 70% stays as Takaichi-CEILING calibration discount (SAM-08 @90% + SAM-20 @60% failure pattern); no behavioral evidence the market is missing fiscal-dominance. DECLINED to overlay a separate fiscal-dominance discount.
- **(c) Live as post-June PATH/CEILING story?** YES, strengthened by the Sato characterization correction below.

Net: OS.1 does NOT justify a SAM-21 discount; mechanical trigger discipline proceeds as-spec'd through Jun 9. Path-MEDIUM half of v1.5.1 conviction decomposition is validated.

### (c) Sato BOJ-board entry corrections

Primary-source verification (BOJ official Nakagawa page + Bloomberg + Japan Times + Nikkei) surfaced two corrections to a framing SAM was carrying in 4 places:

- **Date:** "Sato joins Jun 16" → **"Sato Ayano takes Nakagawa's seat Jun 30"** (Nakagawa term expires Jun 29 per BOJ official; Sato term begins Jun 30). SAM was conflating with the Jun-16 BOJ MPM.
- **Framing:** "hawk→dove swap" was directionally correct but **understated** — Nakagawa was one of the 3 active Apr-28 dissenters who voted FOR the 1.00% hike (alongside Takata, Tamura). Sato is reflationist (Aoyama Gakuin Univ. law prof, Takaichi appointee). **Apr-28-style hike-dissent bloc drops 3 → 2 unless Sato surprises.** Material dovish shift in marginal-vote count for the post-June PATH/CEILING — strengthens v1.5.1 path-MEDIUM conviction; no Jun-16 binary impact.

**Files touched:** STATUS.md (header banner + STATE OF PLAY + market data table + BOJ ASSESSMENT row + mechanical-trigger note), thesis/THESIS.md (L182 hike-cycle bullet + L213 catalyst-sequence row), docket/CALENDAR.md (L28 row), docket/CATALYSTS.tsv (row 8), MEMORY.md (item #1 OS.1 → CLOSED), this CHANGELOG.

**Not changing:** thesis version (still v1.5.1), channel structure, predictions (SAM-21 70%, SAM-23 72%, SAM-24 85%, SAM-26 ~25%), position (13 sh + Jun-18 $58C), stop spec, target band, carry-unwind decomposed marks.

---

## 2026-06-03 — v1.5.1: NARRATIVE RECONCILIATION — math-vs-prose alignment post CH-004

**Author:** SAM
**Action:** Minor version bump v1.5 → **v1.5.1**. Four-part narrative reconciliation pass collapsing the second-pair-of-eyes critique items #2/#3/#4 (deferred from 6/3 PM). No channel-structure change, no new evidence, no probability re-rates. The pass aligns thesis prose with the CH-004 carry-unwind METHOD shipped this AM and with the v1.5 single-path framing as the position actually trades. **No outbox signals fire from this** — measurement-side already announced in the morning CH-004 close; this is the prose follow-on.

### What changed in THESIS.md

**1. Conviction decomposed (header).**
- Old: *"HIGH on direction; MEDIUM on near-term timing (single-catalyst structure carries more drawdown risk than multi-channel convergence)."*
- New: split into two explicit lines.
  - **Direction / level: HIGH** — structural over-determination via rate-differential, J-ICS, hedge ratio, positioning. Target $60-62 / USDJPY 148-152 grounded in structural math, not catalyst.
  - **Near-term timing: MEDIUM** — explicitly cites PREDICTIONS timing-failure cluster as basis (SAM-08 @90% April hike, SAM-20 @60% April hike, SAM-15 @80% oil-in-yen Q2-Q3, SAM-22 @65% no CFTC cover, SAM-19 @75% insurer cuts H1). "Right substance, wrong window" is the recurring SAM failure mode; "right but early" is the modal risk, not "wrong."

**2. STRUCTURAL PILLARS section added (new, between CORE THESIS and CARRY-UNWIND METHOD).**
- Explicitly answers "why am I long even if Jun 16 disappoints?" — previously this answer was scattered as footnotes throughout Channel 1 deferred-reference, Channel 2 triggers, Independent Catalyst, and Position View.
- Four pillars enumerated: (1) rate-differential at multi-decade extreme; (2) J-ICS lifer long-end abandonment (domestic, independent of BOJ); (3) hedge ratio at 14-yr low (Pillar 3 is the slow-burn version of the Channel 1 forced-repat mechanism); (4) CFTC positioning at 63.7% of cycle peak (amplifier on whatever catalyst fires).
- Closes with explicit position-sizing logic: shares = structural-pillar bet, Jun-18 $58C = catalyst-conditional bet. Stop spec (event-cap pre / AND-condition post) is consistent with this split.

**3. Channel 2 prose reconciled with CH-004 METHOD.**
- *Aug-2024-speed framing demoted from expectation → upside tail.* Old prose said "Aug 2024 precedent: unwind took hours, not days" as if it were the base-case expectation. New prose explicitly: **"speed of unwind scales with the catalyst's surprise component, not with the catalyst's existence."** A fully-priced hike does NOT unwind per the METHOD (only the hawkish-on-size/path subset does). Frame to HENRY/LIQUID is now "potentially Aug-2024-fast IF triggered hawkish-of-pricing," NOT "Aug-2024-fast on any Jun-16 hike."
- *Intervention paradox softened.* Old prose: *"MOF acts → unwind; MOF doesn't act → forced repat; either path → unwind."* Both legs empirically falsified:
  - MOF acts → CH-003 (Apr 30 + May 6) gives unwind\|fires ~0.20, not the implicit ~0.50 the paradox assumed.
  - MOF doesn't act → Channel 1 deferred (3-of-3 Big 3 benign); "forced" leg dissolved at disclosure-window timescale.
- New prose: paradox replaced with explicit honest framing. The case for being long is not the paradox; it is the structural pillars + an asymmetric option on Jun 16.

**4. One-liner refreshed.**
- Old (v1.5): catalyst-first ("Channel 2 is now the dominant remaining near-term path") with structure as afterthought; carried stale "Channel 3 dormant" line from May 27.
- New (v1.5.1): catalyst remains identified as Channel 2, but explicit: *"the position is not catalyst-dependent — it's structurally over-determined…"* References § STRUCTURAL PILLARS. Channel 3 reactivation reflected.

### Why minor (Y) not major (X)

- No new transmission channel; no thesis-direction reversal; no conviction-level reversal on direction (HIGH unchanged).
- All probability marks unchanged (SAM-21 70%, SAM-23 72%, SAM-24 85%, SAM-26 ~25%; carry-unwind decomposed 14/37/49% unchanged).
- Position unchanged. Stop spec unchanged (Will-decided earlier today).
- The pass aligns prose to existing math (CH-004 METHOD shipped this AM) and surfaces existing structural support that was already in the doc but buried. It is a *narrative coherence* fix, not a thesis update.

### What is NOT changing

- Channel structure (1 deferred / 2 dominant / 3 reactivated).
- Carry-unwind decomposed marks (14% / 37% / 49%).
- Position (13 sh + Jun-18 $58C).
- Stop spec (event-cap pre-Jun-16, AND-condition post).
- Predictions (SAM-21/23/24/26).
- Target band ($60-62 / USDJPY 148-152).
- Risk Factors table (no probability changes; mitigation column references the new STRUCTURAL PILLARS implicitly through "structural setup intact" but rows not re-edited tonight — METSUKE pass will flag if a row reads stale against the reconciled framing).

### What this enables for next sessions

- **HENRY/LIQUID cross-agent signals** can now lead with "structural pillars over-determine the direction; June 16 hike is the dominant *catalyst* for resolution but not load-bearing for the direction." The 6/3 AM CH-004 outbox signals already used the MEASUREMENT-CORRECTION framing; the v1.5.1 prose now makes that framing the doc-native voice rather than a one-off outbox caveat.
- **RED CH-004 challenge** (catalyst-prob → unwind-prob conflation) is now closed both math-side (METHOD, this AM) and prose-side (Channel 2 reconciliation, this entry). RED can update CHALLENGES log to CLOSED.
- **"Right but early" risk framing** is now thesis-explicit. If the position bleeds from here to Jun 16 without resolution, the doc supports "this is the modal SAM failure mode (timing, not direction); the structural pillars argue for holding through" — preempts the temptation to trim on time decay.

### Files touched

- `thesis/THESIS.md` — header (version + conviction decomposition), one-liner refresh, new STRUCTURAL PILLARS section, Channel 2 prose reconciliation.
- `thesis/CHANGELOG.md` — this entry.

### Files NOT touched this pass (deferred — METSUKE will flag if stale)

- `STATUS.md` — header/banner; the v1.5.1 reconciliation should propagate to STATUS lead next refresh, not tonight. Tape didn't move thesis-side.
- `STRATEGY.md` — stop spec already harmonized this PM; structural-pillar framing may want a header cross-ref to § STRUCTURAL PILLARS on a future pass.
- `TRADE.md` — no money-field implications.
- `PREDICTIONS.tsv` — no prediction adds/closes from this pass.
- `TIMELINE.md` — no resolved events to log; v1.5.1 is a prose alignment, not an event.

### Process notes

- Window was quiet evening tape (USDJPY 159.90, off the 160.03 PM tag; Brent $96.78 −1.05%, snapping the 4-day MOU-break rally). Right pre-Jun-9 mechanical-trigger window to do this pass.
- Eval re-baseline NOT gating this pass (Will explicit): eval runner is skip-boot, doesn't load THESIS, so before/after test is identical surface — no signal to protect. Eval re-baseline scheduled as own fresh-session run before Jun 9-16 crunch.
- METSUKE Run 3 spawned on the edited surface per the 6/2 PM CALIBRATION lesson (spawn after every material multi-file edit pass, not just POV pivots).

---

## 2026-06-03 — STOP-SPEC HARMONIZATION: event-cap pre-Jun-16, AND-condition post-event (Will-decided)

**Author:** SAM (Will-decided)
**Action:** No version bump. **Doc-harmonization to resolve a real contradiction**, not a thesis change. Three docs (STATUS, THESIS, TRADE) carried "Stop $55.05" as a flat hard level; STRATEGY carried a two-part AND-rule ("no MOF at 167 AND BOJ dovish — both required to exit"). The flat shorthand would have misfired on a pre-Jun-16 USDJPY spike to 167 (would exit before the catalyst that resolves the AND). Will picked **pure event-cap mode (A)** over hard-cap mode (B) or hybrid (A+ with catastrophic floor).

**Operative rule (now consistent across STRATEGY/STATUS/THESIS/TRADE):**
- **Pre-Jun-16:** no mechanical price stop. Position is event-capped by sizing ($798 total exposure; share max ~$42 to $55.05, call capped at $40 premium). Ride through any drawdown regardless of FXY/USDJPY level.
- **Post-Jun-16:** exit if BOTH (BOJ dovish at Jun 16) AND (USDJPY 167+/no MOF response). $55.05 is the FXY level correlating with USDJPY ~167, meaningful only post-event. Single condition (price-only OR BOJ-only) is insufficient.
- **Conscious acceptance:** catastrophic tail (USDJPY 175+ scenario) is left unprotected pre-event. Position size + small call premium are the risk cap.

**Why (A) over (B):** position was deliberately sized small + defined-risk to be event-capped; pre-event price stop optimizes for the worst asymmetric error (knocked out the day before the catalyst that resolves the thesis — Aug 2024 precedent: USDJPY tagged 161.95 pre-BOJ then reversed to 141 over weeks). Stop-mode and sizing-mode now match.

**Files touched:** `STRATEGY.md` (Stop loss section restructured with pre/post-Jun-16 table + rationale); `STATUS.md` (lead line + state-of-play + Sep-call decision footer); `TRADE.md` (entry card stop row + R:R row + risk-factor "oil shock dominates" row); `thesis/THESIS.md` (POSITION VIEW vehicle line + RISK FACTORS oil-shock + intervention-fails rows).

**What's NOT changing:** thesis direction/conviction, position sizing, target ($60-62), call structure, any probability mark.

---

## 2026-06-03 — MEASUREMENT CORRECTION: carry-unwind decomposition added (CH-004 close)

**Author:** SAM
**Action:** No version bump. **Measurement correction, NOT a view change.** Yen-direction conviction HIGH unchanged. Adds new `## CARRY-UNWIND PROBABILITY METHOD` section to THESIS.md (placed after CORE THESIS, before THREE TRANSMISSION CHANNELS) and refactors STATUS CARRY UNWIND PROBABILITY table to show decomposition + driver weights. Closes RED CH-004 ("the 7/30/60 buckets are conviction levels, not calibrated probabilities, and shouldn't be presented to Will or LIQUID/HENRY as if they were").

**Old method (implicit, pre-Jun-3):** 7d/30d/60d buckets were judgment-calibrated single numbers with one-line driver notes per move. No formula, no reasoning chain, no link to the 8 resolved predictions.

**New method (Jun 3):** decomposed estimate from named priors —
- Formula: `P(unwind, T) = 1 − ∏(1 − pᵢ(T))` across 5 trigger channels + state-dependent residual
- `pᵢ = P(catalyst i fires in T) × P(unwind | catalyst i fires) × CFTC_amplifier`
- Overlap discount (judgment, biggest in joint-escalation tail) applied to bottom-up union
- CFTC amplifier + residual term explicitly state-dependent (residual ON only when CFTC > 60% of cycle peak; turns OFF when positioning covers)

**Why view-neutral:** No new evidence moved the view. A mismeasurement got fixed. The decomposition surfaced two structural errors in the prior buckets:
1. **Catalyst → unwind conflation** — SAM-21 (BOJ hike 70%) and SAM-23 (intervention #3 72%) were being transcribed as carry-unwind probabilities. They're not. A delivered fully-priced hike doesn't unwind (only the hawkish-on-size/path tail does); an intervention that spike-reverses same-day doesn't unwind.
2. **MOF #3 conditional ignored CH-003** — prior implicit anchor ~50% unwind\|fires; CH-003 evidence (Apr 30 + May 6 both spike-reversed same-day, net ~zero on sustained unwind) supports ~0.20 baseline.

**Bucket marks (Jun 1 prior → Jun 3 decomposed):**

| Bucket | Prior | Decomposed | Δ |
|---|---|---|---|
| 7d | 15% | **14%** | -1pp (noise) |
| **30d** | 70% | **37%** | **−33pp** |
| **60d** | 80% | **49%** | **−31pp** |

7d roughly honest; 30d and 60d inflated by ~33pp via the catalyst-conflation. Bottom-up math: 30d union = `1 − (0.90)(0.82)(0.917)(0.96)(0.932)(0.95) = 0.425`; − 5pp overlap → 37%. 60d analogous.

**Residual (state-dependent):** principled small term (1.5/5/7.5pp at 7/30/60d) for unattributed positioning-cascade unwind base rate when CFTC > 60% of cycle peak. Aug 2024 fit partly — BOJ trigger lit fuse but violence outsized to catalyst. Residual OFF when positioning covers below the gate. **Sized to NOT be a backdoor to claw back toward 70%.**

**What's NOT changing:**
- Yen-direction conviction (HIGH)
- All channel-level views (Channel 1 deferred, Channel 2 dominant, Channel 3 reactivated)
- Position (13 sh + Jun-18 $58C, stop $55.05)
- SAM-21 70% / SAM-23 72% / SAM-24 85% / SAM-26 ~25% predictions
- v1.5 single-path structural framing

**Cross-agent disclosure:** LIQUID + HENRY drafted as MEASUREMENT CORRECTION leads — "Methodology correction, not thesis softening. 30d/60d marks were overstated via catalyst→unwind conflation. Yen-direction conviction unchanged. New decomposed marks: 7d 14% / 30d 37% / 60d 49%." Drafts gated on Will review before send.

**Note for future SAM:** the residual is **state-dependent**, conditioned on CFTC > 60% of cycle peak. Do NOT treat the 5pp as a permanent floor — when positioning covers, the residual turns OFF along with the +5pp amplifier. Method section bakes this in as a table; honor it.

**RED CH-004 close:** outbox signal drafted (gated on Will review). Once delivered, RED owns the close in its CHALLENGES log.

---

## 2026-06-01 — v1.5 intra-version POV pivot (Iran MOU broken; intervention #3 reactivated; Fed-cut backup reads dead)

**Author:** SAM
**Action:** No version bump (no channel-structure change; probability + framing refinement within v1.5). Logged as dated POV pivot per [[finding_pov_changelog_pattern]]. **Reverses the 2026-05-29 STATUS read of "MOU framework hardening" and softens the v1.5 THESIS "Fed-cut secondary engine with 24h rescue" framing.**

**Old view (May 29-31, v1.5):**
- Iran/Hormuz MOU framework hardening (Brent $91.12, near-signed pending Trump approval); intervention #3 zone dormant; SAM-23 ~55%.
- Fed-cut secondary engine described as "backup catalyst one day behind the primary" via Jun 17 FOMC dots landing ~24h after BOJ.

**New view (Jun 1):**
- **MOU effectively broken** — Tehran suspended message exchange via mediators + threatened to block Hormuz; Brent +4.02% to $94.78, WTI +7%. Pakistan-mediated framework hit hard setback. Tehran-obstruction friction we'd kept on watch escalated into open suspension. **SAM-23 marked ~55% → ~72%.** Intervention #3 zone REACTIVATED (USDJPY 159.64 inside 159.50+ verbal zone; Katayama May 29 "decisive action" frames live posture; Bessent-Katayama-Himino alignment cabling hike + intervention combo per Reuters Jun 1).
- **Fed-cut backup engine reads dead at Jun 17:** FOMC priced >97% no-change, <10% cut odds anywhere in 2026 (CME FedWatch). April US CPI 3.8% + resilient labor blocking. **v1.5 is more single-path than we framed it** — the Jun-18 $58C is pure BOJ binary, no Fed-side insurance. PC cascade retained as multi-month tail (not Jun-window catalyst).

**Why view-changing (not just data refresh):**
- Last week we used MOU optimism to justify a -20pp SAM-23 mark-down and a Channel 3 "dormant" designation. The basis for both inverted in 4 days. Documenting the round-trip protects calibration (was the May 25 mark-down right at the time, or did we over-credit Brent crash optimism?).
- The "Fed-cut 24h rescue" framing was thesis-level reassurance written into v1.5 RISK FACTORS. With <10% 2026 cut odds, that reassurance was a stretch. Acknowledging it now prevents leaning on it pre-meeting.

**Position-side:** Unchanged. 13 sh + Jun-18 $58C. Stop $55.05. Thesis-side bullish (BOJ pricing held + cabling + intervention backstop + insurer mech intact); structure tighter (single-path more single).

**Carry-unwind probs:** 7d 12→15% (intervention zone live); 30d 70%→70% (BOJ pricing held offsets Fed-cut removal); 60d 83%→80% (Fed-cut tail trimmed).

**THESIS body propagation closeout (Jun 1 PM):** Morning Jun 1 cascade updated STATUS / PREDICTIONS / TIMELINE / CALENDAR but deferred the THESIS body rewrite (logged as NEXT SESSION item 4: "soften RISK FACTORS Fed-cut '24h backup' language to 'multi-month tail'"). PM surgical sync applied 7 edits to THESIS body to close the TRADE/THESIS asymmetry surfaced during the TRADE.md Jun 1 refresh: (1) header banner Jun 1 sync annotation + Channel 3 status flip dormant → REACTIVATED; (2) Forward catalyst table MOU row reframed + Intervention #3 row SAM-23 ~55% → ~72%; (3) Phase 2 dynamic "Current state" — Brent direction reversed, MOU break logged, Phase 2 inception paused; (4) "Why secondary path now" stale May 28 paragraph rewritten to integrate May 31 repricing + Jun 1 MOU break; (5) "Timing key" Fed Path paragraph rewritten from "24h rescue catalyst" to "multi-month tail, not Jun-window" with CME FedWatch Jun 1 reads; (6) SECONDARY PATH tripwires table — Fed-cut pricing / US CPI / FOMC dots rows updated with Jun 1 reads (US CPI Jun 10 now the SAM-side Fed tripwire, not Jun 17 itself); (7) RISK FACTORS — BOJ-delays mitigation column rewritten (single-path closer to pure downside, Fed-cut multi-month tail not 24h rescue), oil-shock mitigation reframed (Brent direction reversed but Kharg threshold still far), intervention-fails reframed (Bessent-Katayama cabling supports execution not jawbone-only). **Probabilities held — 25% BOJ-delays / 15% oil-shock / 12% intervention-fails — explicit notes added inline that re-rate is a separate deliberate decision pending escalation trajectory.** No version bump. Closes NEXT SESSION item 4.

---

## 2026-05-31 — v1.5 intra-version POV pivot (market repriced June hike to ~88%; SAM-21 ~50% → 70%)

**Author:** SAM
**Action:** No version bump (probability refinement within v1.5's single-path framing). Logged as dated POV pivot per [[finding_pov_changelog_pattern]]. **Directly reverses and exceeds the 2026-05-28 "dovish-impaired" pivot below.**

**Old view (May 28-29, v1.5):** June BOJ single-path but **dovish-impaired**; SAM-21 ~50% (coin-flip, held after the May 29 activity beat rebalanced soft-price/firm-activity); carry-unwind 30d 58% / 60d 77%; market read carried as 55-65%.

**New view (May 31):** June BOJ single-path and **market-confirmed base case**. Market repriced the hike to **~88%** (Polymarket 88.2% / trader-swap ~87.5%, both current May 31) — a **sustained 9-day move** (Polymarket 59.5% May 22 → 88.2% May 31) that held *through* both dovish CPI prints. SAM-21 marked ~50% → **70%**. Carry-unwind bumped 30d 58→70%, 60d 77→83%.

**Why this is the decisive read (and why we were behind it):** the market repricing UP through two dovish CPI prints is the market **siding with the wage/activity mechanism over the CPI threshold** — a real-time vindication of the [[finding_threshold_vs_mechanism]] framing we'd logged May 28-29 (Tokyo CPI = threshold; activity/wages = mechanism). Our ~50% mark was carrying a stale 55-65% market read; the live read had moved to ~88%, so 50% was staleness, not a differentiated view.

**Why +20pp (to 70%), not the full +38pp (to 88%):**
1. **Earned discount** — SAM has failed TWICE being too-hawkish on the Takaichi 0.75% ceiling (SAM-08 @90%, SAM-20 @60%); the ceiling is still live and a thin-ish prediction market won't price political-surprise risk.
2. 70% = clear base case; ~30% held for the political-ceiling/surprise tail. Re-verify swap pricing Jun 9-15.

**Corroborating:** CFTC net short -114,667 (May 26, 4th build week, +27K new shorts, broke -102K cycle peak) — fuel load building into a hawkening market → more violent unwind if the hike lands.

**Structural note:** No channel structure change. v1.5 single-path stands. Position unchanged (13 sh + Jun-18 $58C); Sep $60 call still NOT warranted (higher near-term hike odds cut against deferred Sep optionality). TIMELINE May 31 entry has the full decomposition.

---

## 2026-05-29 (PM) — SAM-15 resolved FAILED (prediction resolution; view-neutral)

**Author:** SAM
**Action:** No version bump — view-neutral. SAM-15 ("oil-in-yen forces repatriation regardless of rate differential," @80%, made 2026-03-20) resolved **FAILED — mechanism falsified**, clearing the OPEN-FOR-REVIEW flag raised the 5/29 AM pass. Canonical post-mortem in PREDICTIONS.tsv.

**Why view-neutral:** the current thesis already reflects what falsified SAM-15. The v1.4 OIL-IN-YEN section captures supply-destruction inverting the trade-deficit mechanism (April TB ¥+301.9B surplus); Channel 1's deferral captures insurers growing foreign books; the Brent collapse is in STATUS/TIMELINE. Resolving SAM-15 closes the audit loop without shifting any channel weight or probability.

**Resolution basis (4-of-4 sub-claims contradicted):** (1) oil-spike premise evaporated (Brent ~$108→$92); (2) "deficit forces liquidation" mechanism inverted (blockade → import-volume collapse → surplus); (3) "independent of rate differential" falsified (rate differential drove the yen despite the surplus); (4) forced repatriation not visible (Big 3 ESR 3-of-3 = foreign-book growth + M&A into US). Distinct from SAM-25's true-in-letter/false-in-spirit — here neither holds.

**Calibration deltas (PREDICTIONS scoreboard):** FAILED 7→8; OPEN 5→4. Added to HIGH-CONFIDENCE FAILURES (@80%). New failure-pattern cluster (6): premise-dependence on a transient shock + standalone-channel overreach.

---

## 2026-05-28 — v1.5 intra-version POV pivot (Tokyo May CPI dovish miss impairs single-path)

**Author:** SAM
**Action:** No version bump (probability refinement within v1.5's single-path framing). Logged as dated POV pivot per [[finding_pov_changelog_pattern]] to preserve trajectory when STATUS narrative is pruned.

**Old view (May 27, v1.5):** Channel 2 (June BOJ Jun 16) is the dominant remaining near-term trigger; SAM-21 June hike ~57%; carry-unwind 30d 62% / 60d 80%.

**New view (May 28):** June BOJ remains the single-path trigger but is now **dovish-impaired**. Tokyo May CPI printed core-core **1.6%** (−30bp vs April national 1.9%; 7th straight monthly decline in the underlying-demand gauge), breaching the pre-registered 1.9% June-BOJ threshold. SAM-21 marked ~57% → **~50%** (coin-flip). Carry-unwind trimmed 30d 62→58%, 60d 80→77%.

**Why measured (-7pp on SAM-21, not a slash):**
1. **Tokyo-vs-national bias** — Tokyo CPI carries structural downward bias from Tokyo-metropolitan subsidies (free education/childcare); national May core-core (Jun 19, post-BOJ) likely prints above 1.6%.
2. **Mechanism vs threshold** ([[finding_threshold_vs_mechanism]]) — BOJ normalization is wage-price-spiral driven (Shunto 5.26%), not spot-CPI driven. Ueda removed the growth precondition; temporary downward pressure won't prevent hikes. A soft CPI threshold is dovish-leaning, not decisive.
3. **Counterweights intact** — Q1 GDP +2.1%, exports +14.8%, 3-dissent split for 1.00%, Apr SoO "quite possible from next MPM."

**Structural note:** No channel structure change. v1.5 single-path stands; this is the first concrete realization of the v1.5 "BOJ delays past June" risk (25% in THESIS risk table) gaining weight. TIMELINE May 28 entry has the full decomposition.

**Addendum — Fed-cut secondary-path operationalized (same session):** Closed a monitoring gap surfaced this session — the v1.5-elevated Fed-cut path (Channel-1-deferred backup) was framed but not operationalized. Extended THESIS `INDEPENDENT CATALYST: FED CUT PATH` from a thin paragraph into a real monitor with carry-end **tripwires** (Fed-cut pricing, US CPI Jun 10, FOMC Jun 17 dots, USD/JPY 145, PC-cascade escalation as BROCK/HANS input). Key insight logged: **FOMC Jun 17 lands ~24h after BOJ Jun 16**, so a BOJ disappointment can be rescued by a dovish Fed the next day — RISK FACTORS "BOJ delays" row updated from "no parallel catalyst to absorb" to "single-path but NOT pure downside." Kept as independent-catalyst section, NOT promoted to Channel 4 (would require structural-conviction bump beyond one CPI print). Placement per doc-ownership: structure+tripwire-levels → THESIS; dates → CALENDAR (tagged, no new rows); live read → STATUS; BROCK/HANS intelligence → KB-152.

---

## 2026-05-27 — v1.4 → v1.5 (Channel 1 demoted to deferred structural backstop after Big 3 ESR window 3-of-3 confirmation)

**Author:** SAM + Will
**Action:** Bumped to v1.5. The Big 3 mutual ESR window (Nippon May 26, Meiji Yasuda May 26, Sumitomo May 26 — all reported the same day) resolved with 3-of-3 evidence against the Channel 1 transmission mechanism. The threshold-vs-mechanism trap fired three times in three prints. Channel 1 is demoted from "co-equal transmission trigger" to "deferred structural backstop (multi-year, not 2026)." Channel 2 (carry / BOJ June 16) becomes the dominant remaining near-term path.

### What changed

**Channel 1 (Life insurer repatriation) — demoted to deferred structural backstop:**

Three-of-three Big 3 mutual lifer ESR prints showed no forced repatriation mechanism in motion. Specifically:

| Insurer | Prior ESR | FY2025 ESR | Δ | Driver | Foreign book FY25 |
|---|---|---|---|---|---|
| Nippon Life | 222% | 195% | **-27pt** | Resolution Life $10.6B M&A subsidiarization (-28pt waterfall line) | Unrealized **GAIN +¥3.99T** (+¥909B YoY) |
| Meiji Yasuda | 216% | 208% | -8pt | Manageable JGB markdown; Stancorp/Allstate acquisition positive | Unrealized **GAIN +¥709B** (+¥227B YoY) |
| **Sumitomo** | **178%** | **197%** | **+19pt** | Stable ops + equity rally + Dearborn Life partial acquisition | Foreign bonds **+¥543B (+6.2%)**; total foreign securities **+¥1.11T (+9.3%)** |

Common pattern across all three:
1. Foreign books in unrealized **GAIN** (not loss) — the v1.0-v1.4 thesis assumed mark-to-market pressure forces sales
2. Foreign exposure **GROWING**, not shrinking (Sumitomo's allocation rose from 33.3% → 35.5% of total investments)
3. M&A direction is **INTO the US** (Resolution Life, Allstate, Dearborn) — opposite of repatriation
4. Domestic JGB exposure being pared (Sumitomo -¥505B / -3.6%) — JGB stress absorbed via domestic exit, not foreign exit
5. Hedge cost relief noted (narrowed rate differential during the year)

The v1.0-v1.4 mechanism — "ESR cap forces foreign bond reduction" — is **not evidenced** by the prints of the three largest mutuals representing the bulk of the system. Capital actions (M&A subsidiarization), equity rally, and hedge-cost relief absorbed ESR pressure without touching foreign asset allocation.

**What's still intact (mechanism level):**
- **J-ICS lifer long-end abandonment** as JGB 30Y driver — DOMESTIC mechanism, independent of ESR-foreign transmission. This is what's actually driving 30Y/40Y stress. Stays in v1.5.
- Mid-size lifer pivots (Fukoku, Asahi) from 30/40Y → 10-15Y tenors — confirmed pre-disclosure window.
- Channel 2 (carry / June BOJ) — unchanged.
- Channel 3 (BOJ + US-Japan FX coordination) — unchanged.

**What's deferred:**
- "ESR forces UST sale" transmission timing assumption — pushed from 2026 to multi-year horizon
- Big 3 mutual ESR window as a primary near-term Channel 1 catalyst — exhausted; no scheduled re-test for ~1 year

**Flow scenarios revised:**

| Scenario | v1.4 weight | v1.5 weight | Note |
|---|---|---|---|
| Base ($80-120B/12mo, $7-10B/mo) | 70% | **78%** | Confirmed by 3-of-3 Big 3 prints — gradual rotation-within (unhedged → hedged), not net cut |
| Stress ($150-250B/6mo) | 25% | **18%** | Lowered — ESR catalyst window resolved without stress signal; would require new shock to trigger |
| Crisis ($300-500B/3mo) | 5% | **4%** | Tail unchanged but trimmed slightly |

**Carry unwind probabilities (post Sumitomo May 27):**

| Timeframe | v1.4 (May 26) | v1.5 (May 27) | Driver |
|---|---|---|---|
| 7d | 17% | **12%** | All Big 3 binary catalysts resolved benign; no near-term Channel 1 trigger remaining |
| 30d | 65% | **62%** | Channel 1 leg of 30d weight structurally removed; June BOJ + CFTC reload anchor |
| 60d | 83% | **80%** | Structural Channel 1 cut ~3pp; Channel 2 (BOJ hike) becomes near-sole driver |

**Status banner updated:**
- v1.4: 🟠 MIXED — Channel 1 weakened (one print)
- v1.5: 🟠 SINGLE-PATH — Channel 1 deferred (3-of-3 confirmed); Channel 2 (June BOJ 55-65%) is dominant remaining trigger; Channel 3 dormant on Brent collapse

### What didn't change

- **Position:** 13 shares + 1 Jun-18 $58C, stop $55.05, target $60-62. Sized to the v1.5 single-path structure.
- **Conviction direction:** HIGH on direction (yen strengthens through 2026) — Channel 2 alone supports the structural view.
- **Conviction timing:** MEDIUM, slightly weakened (single-catalyst structure has more drawdown risk than multi-channel convergence).
- **Stop level:** $55.05 unchanged.
- **June BOJ base case:** SAM-21 ~57% / market 55-65% — unchanged.
- **JGB 30Y / J-ICS amplifier mechanism:** intact; the lifer long-end abandonment driver is domestic and doesn't depend on ESR-foreign transmission.

### Old → new view summary

| Item | v1.4 view | v1.5 view |
|---|---|---|
| Channel 1 status | Co-equal trigger; ESR window May 25-29 is primary near-term Channel 1 catalyst | **Deferred structural backstop** (multi-year); ESR window exhausted with 3-of-3 benign |
| ESR cap → foreign bond reduction | Working assumption (would force selling) | Falsified for Big 3 mutuals; absorbed via M&A + equity rally + hedge-cost relief without touching foreign allocation |
| Foreign asset direction (Big 3) | Expected to shrink under stress | Confirmed GROWING (Sumitomo +¥1.11T total foreign securities; Nippon/Meiji into US M&A) |
| Flow scenario weights | 70/25/5 | **78/18/4** |
| Carry unwind 7d / 30d / 60d | 17 / 65 / 83 | **12 / 62 / 80** |
| Channel rank | Three co-equal channels | Channel 2 (BOJ) primary; Channel 1 deferred; Channel 3 dormant pending Iran/Hormuz outcome |
| Position sizing logic | Multi-channel asymmetric convergence | Single-path durable view; existing position correctly sized; **no Sep $60 call addition warranted** |

### Position decision implications

The Sep $60 call addition (Position A, authorized by Will May 21 pending Sumitomo) is **NOT triggered** by v1.5. The asymmetry case for OTM-deferred optionality was built on multi-channel convergence (Channel 1 + Channel 2 + Channel 3 all firing in the same window). With Channel 1 deferred and Channel 3 dormant, the structure is now single-path. Single-path requires paying for time at a 55-65% probability — that is not the asymmetry Will established the position for. Existing position (13 shares + Jun-18 $58C @ $0.40) correctly covers near-term (call) + durable view (shares).

### Pending tests (post v1.5)

- **Thu-Fri May 28-29:** Tokyo May CPI — leading indicator for June national; if core-core slips below 1.9%, June BOJ pricing breaks lower from 55-65%
- **Fri May 29:** CFTC weekly (May 22 data) — watch for break of -102K cycle peak
- **Ongoing:** Iran/Hormuz MOU binary watch — signed → Phase 2 accelerates; collapsed → intervention #3 zone reactivates
- **🔴🔴 Tue Jun 16:** BOJ MPM — now the dominant remaining catalyst (Channel 2 single-path)

---

## 2026-05-21 — v1.3 → v1.4 (Channel 1 mechanism update + Phase 1 inversion + Bessent affirmation promoted)

**Author:** SAM + Will
**Action:** Bumped to v1.4. Three structural findings warrant the bump (all mechanism-level, not probability-level): (1) JGB 30Y blowout to 4.0% is driven by J-ICS-induced lifer abandonment of the long end — amplifier mechanism, not relief valve; (2) April trade balance posted SURPLUS because Hormuz blockade collapsed import volumes (-64% YoY ME crude, lowest since 1979) — Phase 1 mechanism INVERTS under supply-destruction conditions; (3) Bessent affirmation (May 11-12) promoted from deferred candidate to Channel 3 pillar after second intervention + public US backing established the pattern.

### What changed

**Channel 1 (Life insurer repatriation) — new subsection added:**
- **Lifer Long-End Abandonment as JGB 30Y Driver (NEW v1.4):** Under J-ICS, super-long JGB moves reprice the entire balance sheet. Mid-size lifers (Fukoku, Asahi) pivoted from 30/40Y to 10-15Y BEFORE the May ESR window. Big 4 sidelined at the long end. JGB 30Y broke 4.000% on May 15.
- **Critical inversion vs. v1.3 framing:** Lifer absence at the long end is the *cause* of the yield blowout, not the consequence. Higher yields don't draw insurers back — J-ICS makes long-duration purchases punitive for solvency. Traditional "yield reaches a level that brings insurers back" reflex is broken.
- Implication: JGB long-end pressure persists/grows without forced BOJ intervention. Pushes BOJ toward (a) policy normalization to legitimize the curve OR (b) YCC-style cap (D2 scenario). Either way, structural yen tailwind.

**Oil-in-Yen — Phase 1 mechanism caveat:**
- April trade balance (May 21 print): ¥+301.9B SURPLUS vs ¥-30-45B deficit consensus. Crude oil imports -64% YoY (steepest since 1980); ME crude -67.2% YoY (lowest since 1979); LNG from ME -76.1%.
- **The blockade didn't increase Japan's oil bill — it collapsed import volumes (physical supply choke).** Phase 1 mechanism inverts when blockade severity chokes physical flow — supply destruction shows up as smaller deficit, not larger.
- Yen STILL weakened (USDJPY 157.61 → 159.19 May 12-21) despite trade surplus. Driver is rate differential + fiscal supply (super-long JGB selling) + lifer absence, NOT trade. Channel attribution corrected.
- Implication: Trade-balance is no longer a clean Phase-1 confirmation indicator under blockade conditions. Watch rate-differential proxies, JGB long-end supply/demand, CFTC positioning.

**Channel 3 — Bessent affirmation promoted from deferred candidate to pillar:**
- May 11-12 Bessent-Katayama Tokyo meeting: "Constant and robust" FX coordination affirmed publicly. First US public affirmation of Japan FX intervention since 2022.
- Bessent has prior public stance favoring faster BOJ hikes — subtext: US wants rate differential compressed from both sides.
- Promoted because we now have the pattern: Apr 30 intervention + May 6 intervention + May 11-12 public US backing = coordinated currency policy, closest to 1985 Plaza precedent.
- Caveat: No SWAP line. Effectiveness mixed (interventions reclaimed same-day). Pure FX cannot fix ~300bp Fed-BOJ gap.

**Resolved events integrated (May 6 → May 21):**
- MOF interventions #1 + #2 (~¥10T combined, largest since 2022)
- CFTC cover signal then reversal (SAM-22 FALSE)
- Bessent-Katayama meeting
- Dai-ichi FY2025 ESR ~220% (resilient; least-representative of Big 4)
- Q1 GDP +2.1% ann beat (June BOJ on track; EWJ-put contraction didn't fire)
- JGB 30Y breaching 4.000% (severe insurer stress threshold)
- April trade balance Phase 1 inversion

**Thresholds updated:**
- USDJPY 160 → 159.19 (inside intervention #3 zone, 0.5% away)
- JGB 10Y 2.40% → 2.770% (29yr high)
- JGB 30Y 4.0% → **BREACHED 4.000%** (first time)
- JGB 40Y added at 3.990%

**Risk factors revised:**
- Added "Big 3 mutual ESR all comfortably >220% (Dai-ichi-like)" at 25% — would mean no Channel 1 acceleration; thesis grinds rather than accelerates.

### What didn't change

- Three transmission channels intact (now amplifying, not relieving).
- Conviction HIGH unchanged.
- Stop $55.05 unchanged. Thesis break far from approached.
- June BOJ base case (SAM-21 70% / market ~74%) unchanged.
- Carry unwind path: still BOJ-hike-primary, intervention-#3-secondary, ESR-shock-tertiary.

### Old → new view summary

| Item | v1.3 view | v1.4 view |
|---|---|---|
| JGB 30Y at 4% | Watch threshold — would trigger if breached | BREACHED, driven by J-ICS lifer abandonment; mechanism is amplifier not relief |
| Phase 1 oil mechanism | "Oil → trade deficit → yen weak" — modeled as clean transmission | Inverts under blockade severity (supply destruction → volume collapse → smaller deficit). Yen weakening now rate-differential-driven not trade-driven |
| Bessent / US backing | Deferred candidate, single-event | Promoted to Channel 3 pillar after second intervention + public coordination |
| Trade balance as Phase 1 indicator | Primary signal | No longer clean under blockade — use rate-differential proxies |

### Pending tests

- **May 22 CPI:** Tokyo leading 1.5%; national consensus 1.7% core. Soft = fade June BOJ pricing 74% → 60-65%. ≥2.0% = locks.
- **May 25-29 Big 3 mutual ESR:** Nippon, Meiji Yasuda, Sumitomo. <200% any = stress-case trigger.
- **Intervention #3:** USDJPY 159+ zone live; SAM-23 @75%.
- **June 16 BOJ:** SAM-21 @70% / market 74%; SAM-24 @85% (25bp not 50bp).

---

## 2026-05-12 — MOF INTERVENTION + BESSENT AFFIRMATION (no thesis bump; v1.3 holds; correction logged)

**Author:** SAM + Will
**Action:** TIMELINE corrected to reflect that the Apr 29-30 "Tokyo session reprice" was actually MOF Intervention #1 (~¥5.48T / $35B — first since Jul 2024). Added Golden Week MOF Intervention #2 (May 6 ~¥4.3T / $28B). Added Bessent-Katayama May 11-12 meeting as new thesis vector (US public affirmation of Japan FX intervention). Updated CFTC tracking: short cover -39.5% WoW = first cover of cycle. **No thesis version bump** — MOF intervention at 160 was a v1.3 named trigger; Bessent affirmation is structurally new but rhetorical (no SWAP line announced).

### What was wrong (correction)

1. **Apr 30 yen rally mis-attributed.** May 3 STATUS logged USDJPY 159.60 → 157.19 as "Tokyo session reprice of Apr 28 BOJ hawkish hold." Reality: Apr 30 USDJPY hit 160.70 high then **155.55 intraday low** (5.15-yen range in one session) — characteristic intervention signature. BOJ reserve data confirmed ~¥5.48T move (first since Jul 2024). Press confirmed via Japan Times, CNBC, Bloomberg by May 2-7.

2. **Tranche 2 hard trigger fired, was missed.** STRATEGY.md hard trigger "MOF intervenes at 160" fired exactly per design. SAM's read of "intervention dip" as "natural Tokyo reprice" meant the dip-add window was forfeited. FXY peaked $58.65 (May 1) then faded to $58.26 today.

3. **Golden Week Intervention #2 (May 6).** USDJPY 157.89 high → 155.05 low (2.84-yen intraday); ~¥4.3T add ($28B). Combined Apr/May ~¥10T ($63.5B) — largest round since 2022 (Q4 2022 was ¥9.2T; Apr/May 2024 was ¥9.8T). Per BofA.

### What's structurally new

1. **Bessent 3-day Tokyo trip May 11-13** (pre-Beijing-summit positioning). Met Katayama 2hr + Takaichi separately. Full agenda broader than FX: critical minerals + AI + Japan's $550B US investment pledge (first $2.2B disbursed early May to Texas/Georgia/Ohio) + BOJ normalisation + Iran war. **Critical context: Bessent has publicly favored faster BOJ rate hikes prior** — his affirmation of intervention is "support tactically, want hikes structurally." Bessent earlier 2026 said "no currency targets" — politically clever (supports intervention without dictating yen level). Monetary policy NOT publicly discussed at meeting (deliberate ambiguity to avoid market dislocation). Channel 3 (BOJ policy divergence) conviction marginally stronger than v1.3 framed — this is the closest to coordinated currency policy since 1985 Plaza. BofA contrarian: expects yen to continue depreciating despite intervention (CNBC May 12). **Forward watch:** Trump-Xi Beijing summit May 14-15 is now a wildcard for SAM — any currency/trade announcement could drag yen via USDCNH-USDJPY correlation.

2. **CFTC cover signal.** Net short -102,059 (Apr 28) → -61,738 (May 5). 39.5% reduction in one week, -37,816 shorts covered + 2,505 longs added. Now 34.3% of Jul24 peak (was 56.7%). FIRST cover signal of cycle. **SAM-22 (CFTC stays below -75K) FAILED.**

3. **The intervention paradox is partially firing.** MOF sold dollars (~$63.5B) — tactical execution of carry unwind. CFTC shorts covered. But USDJPY 157.61 today — markets reclaimed most of the move because rate differential (~300bp) is intact. **Half the unwind fuel burned through intervention itself, before BOJ even hikes.** June hike still primary trigger but less violent.

### What didn't change

- **Three transmission channels intact.**
- **Conviction HIGH unchanged.**
- **Scenario weights held** (Base 70 / Stress 25 / Crisis 5) — Channel 1 still gated on ESR May 15.
- **Stop $55.05 unchanged.** Thesis break far from approached.
- **June BOJ base case** (SAM-21 70% / market ~74%) unchanged.

### Carry unwind probabilities

| Timeframe | Pre (May 3) | Post (May 12) | Driver |
|---|---|---|---|
| 7d | 20% | **12%** | Intervention deterrent + Bessent affirmation reduces near-term unwind speed |
| 30d | 72% | **70%** | Hold — catalyst load intact (ESR/CPI/GDP/trade); fuel reduced but still net -61K |
| 60d | 90% | **88%** | Slight reduction — less violent unwind when fires; June hike still pricing 74% |

### Predictions resolved

- **SAM-22 FAILED FALSE.** Net short crossed above -75K (now -61,738). Lesson: when intervention trigger is near (USDJPY 160 zone), CFTC cover risk is much higher than 35%; should have prob-weighted intervention scenarios into SAM-22 directly.

### Predictions added

- **SAM-23:** MOF intervention #3 before June BOJ if USDJPY pushes 159+ (75%). Bessent affirmation removes diplomatic ceiling.
- **SAM-24:** June BOJ hike size = 25bp not 50bp (85%). Consistent with all data + political math.

### Why no thesis bump

- MOF intervention at 160 was a NAMED v1.3 trigger that fired. Confirmation, not refinement.
- Bessent affirmation is genuinely new but: (a) rhetoric without SWAP line, (b) single event, (c) monetary policy NOT publicly addressed at meeting. Per Apr 11 restraint lesson, single events rarely justify thesis refinement; wait for second confirmation (next intervention with explicit US backing, OR SWAP line announcement, OR rate-coordination signal).
- v1.4 candidate (Bessent affirmation as 4th Channel 3 support) — hold for confirmation event.

### Lessons (added to MEMORY)

1. **Read intraday extremes, not closes.** Apr 30 close 160.18 looked like flat day; intraday 5.15-yen range was the intervention. Boot scripts focus on close-to-close which masked the move. **Action:** add intraday-range alert to boot when single-day range exceeds 2.5y.

2. **Don't reach for "natural reprice" when violence is in range.** "BOJ hawkish hold caused 2.4y rally over 2 days" was implausibly large for a confirmed-hold scenario. The size of the move should have been the tell.

3. **Cross-check single-source narrative against verifiable data.** First intervention is rarely confirmed officially — but BOJ reserve data, MOF current-account moves, and Fed custody flows are public. Cross-source instead of relying on one read.

---

## 2026-04-28 — APR 28 BOJ RESOLUTION (no thesis bump; v1.3 holds)

**Author:** SAM + Will
**Action:** BOJ Apr 28 meeting resolved per v1.3 modal scenario (HOLD + hawkish, was 45%). Outcome was slightly more hawkish than modeled — 3 dissents for hike to 1.00% (biggest split since 2016, first under Ueda), GDP forecast cut FY26 1.0% → 0.5%, inflation forecast upgraded, hawkish presser. Swap markets repriced June hike to 74% (vs SAM-21 70%). **No thesis version bump** per Apr 11 restraint lesson — Apr 28 confirmed v1.3, didn't refine it.

### What resolved

1. **SAM-20 (BOJ Apr 28 hike @60%) FAILED FALSE.** Calibration miss — overweighted hawkish data signals (Takata dissent, Shunto, wages) vs dovish political cover (Takaichi 0.75% line, ME uncertainty). Lesson: when political ceiling is explicit AND external uncertainty is high, BOJ defers to consensus optics; hawkish dissents are the board's signal of intent without breaking that consensus.

2. **SAM-21 (June hike @70%) tracking BULL.** Market consensus now 74%. Three dissents + GDP cut + inflation upgrade = maximum-hawkish version of "hold." June path near-locked.

3. **Brent +12% in 4 days to $111.26** on Trump rejecting Iran's Hormuz proposal. Phase 1 oil pressure reasserts; April trade balance (~May 20) becomes hot test.

### What didn't change

- **Three transmission channels intact.** No new channels, no channels broken.
- **Conviction HIGH unchanged.**
- **Scenario weights held** (Base 70 / Stress 25 / Crisis 5).
- **Stop $55.05 unchanged.** Thesis break condition not approached.
- **Carry unwind probabilities:** 7d ticked 20% → 15% (binary catalyst passed without trigger); 30d held at 70%; 60d nudged 88% → 90% (June lock).

### Position implication

- **Tranche 2 trigger zone $58.00-58.25 NOT YET HIT.** FXY $57.49 — US session has not priced the hawkishness. Overnight Tokyo (Apr 29) is the test.
- **No chase below $58.00.** Wait for matrix-defined entry. If FXY doesn't reach the zone in 48hrs, market is signaling hawkish-hold isn't enough fuel for the next leg → wait for ESR (mid-May) or pre-June CPI catalysts.

### Why no thesis bump

Apr 28 resolved as the v1.3 modal scenario. The 3-dissent surprise is hawkish-augmenting but doesn't change channel structure, fuel dynamics, or destination. The June hike call (SAM-21 70%) is now market consensus (74%) — slight strengthening of the timing call, not a structural refinement. Per Apr 11 restraint lesson, single-event confirmation doesn't justify version bumps; ESR disclosures (mid-May) remain the next genuine thesis-test.

---

## 2026-04-24 — THESIS v1.2 → v1.3 (TIMING STRETCH + FLOW PACE DOWNGRADE)

**Author:** SAM + Will
**Action:** Integrated 11-day gap data (Apr 13 → Apr 24). Three predictions resolved (SAM-16 TRUE, SAM-17/SAM-18 FALSE). BOJ meeting odds collapsed after Ueda Apr 13 speech. Channel 1 flow pace reverted to base case. Thesis STRUCTURE (channels, destination, conviction) unchanged — refinement on TIMING and MAGNITUDE, not direction.

### What changed

1. **BOJ Apr 28 hike probability: 60-65% → ~20%.** Ueda Apr 13 speech (read by Deputy Himino while Ueda went to G7) explicitly flagged Middle East uncertainty; refrained from using "rate hike." Market hike bets tumbled from ~70% → 3-10% (Polymarket 97% no change). June meeting now positioned as base case ("as soon as June"). Katayama reaffirmed "free hand" to intervene.

2. **Channel 1 flow pace: STRESS → BASE.**
   - Feb TIC (Apr 15 release): Japan UST holdings ROSE to $1,239.3B (from $1,185.5B Dec) — aggregate flows NOT visible as net selling.
   - MOF ITS 4-week rolling (Apr 16 decisive release) dropped from ¥-5.0T → ¥-2.74T. Apr 5-11 individual week showed +¥698B NET BUYING. Mar 29-Apr 4 ¥-2.46T was FY-end seasonal spike, not regime change.
   - Apr 14 20Y JGB auction BTC 4.82x, tail 0.2bp — exceptional demand. Insurer buyer strike confirmed super-long (30Y/40Y) specific, NOT broadening.
   - Flow pace reverted to base case $7-10B/mo. "Stress case pace" framing from v1.2 not confirmed.

3. **Phase 1 oil-in-yen dynamic: OBSERVATION DOWNGRADE.** March trade balance posted ¥+667B SURPLUS (+25.9% YoY) despite Hormuz blockade. Exports +11.7% (AI-driven demand) absorbed oil import costs. Pre-Feb-28 crude shipments in March data may partially explain, but "oil→deficit→yen weak" leg did not mechanically fire as modeled. March CPI core 1.8% (accelerated from 1.6% but still below 2% target for 2nd month).

4. **Carry unwind probabilities re-calibrated:**
   - 7d: 68% → **20%** (April hike unlikely → no immediate trigger)
   - 30d: 93% → **70%** (June hike base case; ceasefire fragility)
   - 60d: 97% → **88%** (direction and fuel load intact; timing stretched)

5. **Nippon Life Apr 22 FY2026 briefing (Ishida):** Will PARE yen-denominated bond holdings; shift from low-yield debt to higher-return assets. ME risk scenario = "upward pressure on inflation and long-term yields." Direction of foreign bond reallocation AMBIGUOUS from the briefing — reducing yen bonds ≠ auto-increasing foreign bonds. Watch for specifics through Apr 25.

6. **Ceasefire Apr 22: EXTENDED** (not indefinite) at Pakistan's request. Hormuz blockade continues. Iran seized 2 container ships post-extension. Brent ~$99, range-bound.

### What did NOT change (intellectual restraint)

- **Three-channel structure intact.** Hedge cost inversion, ESR regime, mortgage constraint, Takaichi 0.75% ceiling all preserved.
- **Destination intact.** Yen appreciation + carry unwind within thesis horizon — direction not in dispute.
- **Scenario weights held** (Base 70 / Stress 25 / Crisis 5). Flow pace reverted to base but structural pressure (ESR disclosures May-Jun, hedge ratio 44.4%) preserved. Overcorrecting on two stock-vs-flow data points would be symmetric to the Apr 11 "stress case" misread. Per Apr 11 feedback: "one data point rarely justifies 15-25pp probability shifts."
- **Conviction HIGH.** CFTC shorts STILL BUILDING (not covering) — fuel load growing through the delay. When it fires, it fires larger.
- **Position parameters** (stop $55.05 / target $60-62 / Tranche 2 trigger $57.00-57.50). Thesis break condition has NOT fired.

### Old view (v1.2, Apr 12)

"BOJ is forced to hike into an oil shock while life insurers exit USTs and carry trades hit record crowding — all paths lead to yen appreciation and carry unwind within 60 days."

- April 28 hike LIVE ~70% (market); 60-65% (internal)
- Carry unwind 68% / 93% / 97%
- MOF ITS at stress-case pace ($36B/mo)
- Phase 1 oil headwind reasserting (blockade)
- Multi-leg acceleration

### New view (v1.3, Apr 24)

"Structural channels intact; timing stretched. BOJ hike slides to June base case. Channel 1 flows running at base pace (not stress). Direction unchanged — what changed is speed. The fuel load keeps building through the delay."

- April 28 hike unlikely (~20% internal; ~3-10% market). June hike base case.
- Carry unwind 20% / 70% / 88%
- MOF ITS at base pace; Apr 16 release was decisive AGAINST stress-case rebalance
- Phase 1 weakened (March trade surplus); Phase 2 timing shifts right
- CFTC fuel load builds through delay — violent unwind when it fires

### Apr 28 decision tree (market-aligned)

| Outcome | Prob | FXY | Thesis |
|---------|------|-----|--------|
| Hike to 1.00% | ~10% | +4-7% violent | Carry unwind fires immediately |
| Hold + hawkish ("raise at next meeting") | ~45% | +1-2% | June hike → 80% prob |
| Hold + neutral | ~35% | flat to -1% | June hike → 60% prob |
| Hold + dovish | ~10% | -2-3% | Timing pushes to H2 2026 |

### Predictions resolved this update

- **SAM-16** (20Y auction BTC ≥2.5x, 70%): ✅ **TRUE** — BTC 4.82x, tail 0.2bp
- **SAM-17** (Feb TIC Japan UST net selling >$10B, 65%): ❌ **FALSE** — Japan holdings rose +$53.8B Dec→Feb
- **SAM-18** (MOF Apr 5-11 LT-debt selling >¥1.5T, 55%): ❌ **FALSE** — actual +¥698B net BUYING
- **SAM-19** (2+ of 5 insurers cut foreign bonds, 75%): TRENDING FALSE; window open through Apr 25
- **SAM-20** (BOJ hike 1.00% Apr 28, 60%): TRACKING FALSE; revise to ~20%

### Calibration lesson

Three predictions due this window; two FALSE. SAM-17 (TIC stock vs. flow) — insufficient care distinguishing aggregate holdings from net purchases. SAM-18 (MOF regime change) — Apr 11 session already flagged "need Apr 16 to distinguish regime change vs seasonal" and the honest answer came back SEASONAL. Confidence on both was moderate (55-65%), so miss is within calibration range, but pattern worth noting: we over-weight acceleration signals relative to reversion. Counter: CFTC positioning (building shorts) was the single BULL data point and it kept building — don't discount the signal that kept going.

### Sources

- Apr 13 Ueda speech: [Bloomberg](https://www.bloomberg.com/news/articles/2026-04-13/ueda-s-speech-shows-rising-caution-without-clear-hints-on-rate)
- Apr 14 20Y auction: [MOF eresul20260414](https://www.mof.go.jp/english/policy/jgbs/auction/calendar/eresul/eresul20260414.htm)
- Apr 15 Feb TIC: [Treasury sb0448](https://home.treasury.gov/news/press-releases/sb0448)
- Apr 16 MOF ITS: `workbook/MOF_FLOWS.tsv` (auto-parsed via `mof_flows.py`)
- Apr 22 Japan March trade: [JIJI](https://jen.jiji.com/jc/eng?g=eco&k=2026042200564)
- Apr 22 Nippon Life briefing: [Bloomberg](https://www.bloomberg.com/news/articles/2026-04-22/nippon-life-to-reduce-yen-bond-holdings-amid-iran-uncertainty)
- Apr 22 ceasefire extension: [NBC](https://www.nbcnews.com/world/iran/live-blog/live-updates-iran-war-trump-peace-talks-vance-ceasefire-ship-hormuz-rcna341149), [NPR](https://www.npr.org/2026/04/22/nx-s1-5795405/iran-middle-east-updates)
- Apr 24 March CPI: [CNBC](https://www.cnbc.com/2026/04/24/japan-cpi-march-inflation-iran-war-boj-rate.html)

---

## 2026-04-12 — HOUSEKEEPING: THESIS data sync + cross-file pruning

**Author:** SAM
**Action:** Synced stale THESIS.md fields to match current STATUS.md. No thesis-level change — this is a data freshness pass, not a view change. Also pruned stale content across CALENDAR, TIMELINE, MEMORY, and STATUS per doc ownership rules.

**THESIS.md changes (still v1.2, no version bump):**
- Header: `v1.0` → `v1.2` (header hadn't been updated with version field)
- Last Updated: Apr 5 → Apr 12
- Carry unwind 7d: 85% → 68% (oil headwind); 30d: 97% → 93%
- CFTC shorts: -67,800 (38%) → -93,742 (52%) — was one release stale
- Brent: ~$115 → ~$97 (post-ceasefire, blockade)
- Position: 4 shares → 8 shares (Tranche 1 was executed)
- BOJ trigger date: Apr 23-24 → Apr 28
- Catalyst sequence: removed 3 passed dates (Mar 31, Apr 1, Early Apr), added Apr 16 MOF + Apr 22 ceasefire expiry
- JGB 10Y threshold: BREACHED → NEAR (MOF Apr 9: 2.397%, 1.3bp below)
- Brent threshold: $115 → $97

**TIMELINE.md:** Fixed week labels (THIS WEEK/WEEK 2 → RESOLVED), Apr 23-24 → Apr 28, scenario rates updated from 0.75%/1.00% to 1.00%/1.25% (rate is already AT 0.75%).

**CALENDAR.md:** Pruned resolved Apr 7-11 week, migrated insurer plans to Apr 14 section.

**MEMORY.md:** Removed 5 script implementation findings (now baked into `scripts/` toolkit), trimmed stale MHLW date reference, updated References cross-link.

**STATUS.md:** Replaced 25-line narrative block with 2-line summary (narrative lives in TIMELINE per doc ownership), simplified carry unwind table (removed stale comparison column).

---

## 2026-04-11 — DATA ACCURACY AUDIT (STATUS refresh, no THESIS version bump)

### STATUS.md data corrections
**Author:** SAM
**Action:** First run of new SAM automation toolkit (`AGENTS/SAM/scripts/`) surfaced multiple data discrepancies between STATUS.md and authoritative sources. STATUS.md refreshed; THESIS.md version held at v1.2. Scenario weights unchanged pending Apr 16 MOF confirmation.

**What changed (STATUS only, not THESIS):**
1. **CFTC JPY non-commercial net: -72.9K → -93,742.** Prior STATUS was reading the Mar 31 CFTC release. The Apr 7 snapshot (released Fri Apr 10) shows shorts built +17K WoW. Now at 52.1% of Jul 2024 peak (was 38%). Source: `cftc.gov/dea/newcot/deafut.txt` parsed via `scripts/cftc_jpy.py`.
2. **JGB yields reconciled to MOF authoritative CSV.** STATUS had cited 10Y 2.41% / 40Y 3.92% for Apr 10. MOF `jgbcme.csv` through Apr 9 shows 10Y 2.397%, 40Y 3.678%; April peak was 10Y 2.429% / 40Y 3.747% (Apr 6). The 40Y 3.92% figure is 17bp above the MOF April peak and could not be reconciled — flagged as likely prior-session data source error. Apr 10 MOF data publishes Mon Apr 13. Until then STATUS uses MOF Apr 9 as baseline. 10Y NOT breached 2.40% stress threshold as previously claimed — actually sits 1.3bp below.
3. **MOF ITS weekly flow data refreshed.** Prior STATUS: "¥2,215.8B / 3 weeks, 2x base case." Corrected via `mof_flows.py` parsing 1,109-row history: 4-week rolling ¥-5.0T (~$-33B, $36B/mo run rate), squarely in THESIS Channel 1 stress-case range ($25-40B/mo). Latest single week (Mar 29-Apr 4) was ¥-2.46T — 2.5× prior weeks, by far the worst. Alert upgraded 🟡 → 🟠.
4. **FXY options positioning added to STATUS reference section.** Not a data correction — net-new visibility. Aggregate P/C 0.06x, 83.9% of call OI in $58-65 thesis zone, 19,014 Jun 18 $58 calls single-strike concentration.

**What did NOT change (intentional restraint):**
- Channel 1 scenario weights (Base 70% / Stress 25% / Crisis 5%). 4-week rolling is stress case but 12-week rolling is still base/stress boundary. One extreme week (Mar 29-Apr 4) is not enough to rebalance from the 70%-weighted base case. Will approved Option B (STATUS refresh + LIQUID signal) explicitly over Option C (scenario rebalance).
- THESIS version — this is a data audit, not a thesis change.
- Carry unwind probabilities (bumped 30d 90→92, 60d 95→96 in STATUS reflecting CFTC crowding + MOF flows; minor refinement not a thesis restructure).

**Signal sent:** 🟠 to LIQUID via `outbox/2026-04-11_to-LIQUID_mof-flows-stress-case-pace.md` — MOF stress-case pace + CFTC crowding + correction to prior understating.

**Decision gate:** Apr 16 MOF ITS release is decisive. If next week confirms another ¥2T+ weekly LT-debt outflow → rebalance to Option C (Base 70→55, Stress 25→37, Crisis 5→8) and bump THESIS to v1.3. If Mar 29-Apr 4 was a one-off → no thesis change.

**Source:** New SAM automation toolkit built today. Reference: `AGENTS/SAM/scripts/AUTOMATION_PLAN.md`, commits c44da1a1 / 5ed7bbfc / fe4628ad.

---

## 2026-04-05 — NORINCHUKIN RESEARCH + HEDGE RATIO COLLAPSE (THESIS v1.2)

### THESIS v1.1 → v1.2 (minor)
**Author:** SAM
**Action:** Integrated Norinchukin CLO contagion research. Added hedge ratio data, institutional exposure framing, GPIF non-risk finding, new thresholds.

**What changed:**
1. **Life insurer hedge ratio: 44.4% (Mar 2025) — 14-year low.** ~55% of foreign bonds ($370-550B) unhedged. Avg FX entry for unhedged: USD/JPY 135-145. Critical forced-selling threshold: below 130-135. This quantifies the exposure we knew existed but hadn't measured.
2. **Total institutional foreign portfolio: ~$3.0-3.5T.** Japan holds $1,185.5B in USTs (Dec 2025). Frames the larger pool beyond our $450-810B life insurer estimate.
3. **Norinchukin shrinking CLO book.** World's largest CLO investor (¥9.7T/$65B, 100% AAA). Reduced ¥500B in Q1 2026 — "fastest decline on record." Not forced selling yet but directional.
4. **GPIF confirmed NOT a forced-selling risk.** ±6-7% deviation bands cushion yen moves. Rebalances by BUYING foreign assets on yen appreciation. Through FY2029.
5. **New threshold added:** USD/JPY 130-135 (insurer forced systematic selling).
6. **Cross-agent link to LIQUID updated** with hedge ratio + UST holdings data.
7. **Outbox signal written** for LIQUID: hedge ratio collapse + Norinchukin + repatriation framing.

**Old view:** Channel 1 repatriation driven by ESR + hedge cost inversion + JGB yield attraction. Exposure estimated but hedge ratio not quantified.
**New view:** Same drivers, now with MEASURED hedge ratio (44.4%, 14yr low). System more exposed than modeled. Repatriation base case ($80-120B) may be conservative. Forced-selling FX threshold mapped (130-135). GPIF risk eliminated.

**Source:** Norinchukin CLO research package (Apr 2026). Full report: `research/outputs/NORINCHUKIN_CLO_CONTAGION.md`.

---

## 2026-04-03 — PRIVATE CREDIT AMPLIFIER INTEGRATED (THESIS v1.1)

### THESIS v1.0 → v1.1 (minor)
**Author:** SAM
**Action:** Added "Private Credit Amplifier" sub-section to Channel 1 (Life Insurer Repatriation). Adjusted flow scenario probabilities. New KB entries (160-162), new vector (VX-SAM-13.00).

**What changed:**
1. **Japan life insurers hold ~$40-53B ($45B central est.) in US private credit**, mostly unhedged (80-90%). Bottom-up verified: Sumitomo $10.7B, Nippon $3.25B, Meiji $4.2B, Dai-ichi $4.2B, plus listed insurers $14B. Morgan Stanley 1-3% AUM range applied to $2.6T industry.
2. **Double-hit vector identified:** BOJ hike (yen +5-8%) + US PC cascade ($10.1B Q1 redemptions) = $4-12B combined losses on illiquid, gated positions.
3. **Flow scenario probabilities adjusted:** Base case 75%→70%, stress case 20%→25%. PC amplifier makes orderly repatriation less likely.
4. **Inbox signal processed:** Prome/Eric Jackson (Pebbles II) cross-fund analysis. Also noted: Dutch pension DB→DC switch (Jan 2026), global pension PC exposure map (CPP, AustralianSuper, Korea NPS, UK).

**Old view:** Channel 1 repatriation driven by ESR + hedge cost inversion + JGB yield attraction. Base case 75%.
**New view:** Same drivers PLUS private credit amplifier — illiquid PC positions create correlated losses that make exits messier. Stress case probability nudged to 25%. Not a new channel — Channel 1's dark twin.

**Counterpoint noted:** Most CLO holdings are AAA/AA tranches (historically resilient). Severity depends on vintage and tranche quality. Direct lending more exposed than CLO senior tranches.

**Source:** Prome signal SIG-2026-04-02-001, Morgan Stanley estimates, SAM bottom-up verification. Full research: `research/outputs/JAPAN_INSURER_PRIVATE_CREDIT_EXPOSURE.md`.

---

## 2026-04-02 — TRUMP REVERSAL + WEAK 10Y AUCTION + SAM-06 RESOLVED

### PREDICTION Resolved: SAM-06
**Author:** SAM
**Prediction:** "Life insurers announce more JGB selling" (75% confidence, Q1 2026)
**Result:** CONFIRMED — TRUE
**Evidence:** Fukoku Mutual stopped buying 30Y/40Y JGBs (Jan 2026, first to break). Nippon Life realized ¥220B JGB losses (active selling, not paper). Feb MOF data showed ¥3.42T foreign bond selling — largest since Oct 2024. Multiple independent confirmations across Q1.
**Calibration note:** 75% confidence on a TRUE outcome — well-calibrated.

### TIMELINE Updated
**Author:** SAM
**Action:** Marked Apr 2 RESOLVED (10Y auction + Trump speech). Updated Apr 6 assessment. Added to branch point table.

**What changed:**
1. **10Y JGB auction RESOLVED — WEAK.** BTC 2.56x (well below 12mo avg 3.24), tail 0.36 (widest since Aug 2024). Coupon 2.4% (28-year high). Not a failure but a clear warning for Apr 7 30Y.
2. **Trump speech REVERSED de-escalation.** No exit plan, no Hormuz reopening. Brent surged $102→$109. De-escalation probability dropped to ~25-30% (was 40-50%).
3. **Phase 1 dynamics reasserting.** USD/JPY back to 159.68. Oil up = yen weak. MOF intervention risk re-engaging.
4. **Apr 6 branch point updated.** Bear fork (strikes resume) now more likely after Trump speech.

**Old view:** De-escalation possibly emerging, oil headwind lifting, smooth policy path. 10Y auction routine.
**New view:** De-escalation crumbling, oil back as headwind, Phase 1 reasserting. 10Y auction weak = Apr 7 30Y now THE critical event. Path to FXY target bumpier but destination unchanged.

**Note on THESIS:** No version bump. Thesis structure unchanged — all 3 channels intact. What changed is PATH (bumpier) not DESTINATION. April BOJ hike prob slight downgrade (45-50% → 40-45%) on renewed "uncertainty" excuse. May unchanged.

### NEW FILES CREATED
**Author:** SAM + Will
1. **STRATEGY.md** — Decision playbook at SAM root. When to add/hold/exit FXY, vol signals mapped to position decisions, 5-stage trade framework, asymmetry table. Not part of boot — read when position decisions are on the table.
2. **research/outputs/VOL_OPTIONS_FRAMEWORK.md** — Full technical reference for vol/options monitoring. CME CVOL (JPVL) regimes, UpVar/DnVar decomposition, FXY OI structure, USD/JPY risk reversal interpretation, convergence signal logic, traffic light dashboard. Source: Perplexity deep research, validated by SAM.
3. **4 new workbook vectors** (VX-SAM-12.00 through 12.03) — vol convergence signal, CVOL, FXY P/C OI, risk reversals. All marked MANUAL UPDATE REQUIRED.

### PROCESS IMPROVEMENT
**Author:** SAM + Will
**Action:** Boot process audit and 6 structural fixes to CLAUDE.md:
1. Boot order changed: THESIS → STATUS → CALENDAR → TIMELINE → MEMORY (was MEMORY first)
2. Market refresh step added (step 7) — fetch live prices before analysis
3. Doc ownership rules added — prevents STATUS/TIMELINE/MEMORY redundancy
4. Session notes template added (CHANGES SINCE / LAST SESSION / NEXT SESSION)
5. PREDICTIONS.tsv added to boot sequence (step 6)
6. STATUS.md trimmed ~34 lines of narrative that duplicated TIMELINE

---

## 2026-04-01 — TANKAN RESOLVED (BULL FORK) + OIL CRASH + TIMELINE EXPANSION

### TIMELINE Updated
**Author:** SAM
**Action:** Major update — marked 2 events RESOLVED, added 5 new branch points, added oil de-escalation scenario.

**What changed:**
1. **Tankan RESOLVED — BULL FORK.** Large mfg 17 (beat cons 16), non-mfg 36 (beat cons 33), biz inflation expectations 2.6% (above BOJ 2% target). April 23-24 hike probability: ~45-50% (up from ~35%).
2. **FY-end RESOLVED.** No outsized flows. Window closed.
3. **Oil crash added.** Trump ceasefire talk → Brent ~$102 (from $115). De-escalation fragile — Iran rejected 15-point plan. Apr 6 strike pause expiry added as branch point.
4. **JGB auctions added.** Apr 7 (30Y) and Apr 14 (20Y) — not in original TIMELINE. These are cross-agent 🔴 triggers if BTC <2.0x.
5. **New tail scenario: oil de-escalation (25%).** War ends → Brent $80-90 → yen strengthens on fundamentals → FXY target faster with less volatility. Reduced "oil dominates" from 20% → 15%.
6. **Branch point table expanded** from 7 to 10 entries, with status tracking column added.

**Old view:** 7 branch points, Tankan pending, no auction dates, oil $115 headwind active
**New view:** 10 branch points, Tankan resolved bull, auctions tracked, oil headwind possibly lifting, de-escalation path emerging

**Note on THESIS:** No version bump. Thesis structure unchanged — all 3 channels intact, conviction HIGH. The shift is in TIMING (accelerating) and RISK CHARACTER (crisis → policy-driven). If April hike probability exceeds 60% or oil de-escalation firms up, consider v1.1 to update probabilities.

---

## 2026-03-31 — MIMURA ESCALATION + MARKET PRICING UPDATE

### TIMELINE Updated
**Author:** PROME
**Action:** Updated "Mon Mar 31" section with Mimura "decisive measures" escalation and market pricing shift.

**What changed:**
- Mimura (top currency diplomat) used "decisive measures" — strongest verbal signal this cycle, first time this language. Final step before actual USD-selling.
- Ueda coordinated messaging: "keeping close eye on yen moves." MOF-BOJ alignment is the pattern that precedes intervention (same as July 2024 sequence).
- Market now pricing 65% May hike to **1.00%** (above our prior base case of 0.75%). Equiti: oil above $110 could force emergency April move.

**Old view:** MOF intervention "still on alert" based on Katayama warning at 159.5
**New view:** Mimura escalation = intervention is the NEXT step, not a possibility. Verbal sequence complete.

**KB entries added:** KB-SAM-157 (Mimura), KB-SAM-158 (Ueda-Mimura coordination), KB-SAM-159 (65% May 1.00% pricing)

**Note on THESIS:** No version bump — intervention was already tracked in THESIS v1.0. This is confirming evidence, not a structural change. If market pricing of 1.00% holds and our terminal rate view needs revising from 0.75%, that would warrant v1.1.

---

## 2026-03-31 — INITIAL CREATION

### THESIS v1.0 — Established
**Author:** PROME + Will
**Action:** Extracted and synthesized standalone thesis from STATUS.md, KB (156 entries), Deep Dive, Mortgage Bomb analysis, and RP-SAM-4.

**Core thesis (v1.0):** Multi-channel convergence — BOJ forced to hike into oil shock while life insurers exit USTs and carry trades hit record crowding. All paths lead to yen appreciation and carry unwind within 60 days.

**Three channels defined:**
1. Life insurer repatriation (ESR regime change makes losses visible → forced UST selling)
2. Carry unwind (85% 7d / 97% 30d; CFTC shorts tripled; intervention paradox)
3. BOJ policy divergence (0.75% political ceiling from floating mortgage constraint)

**Independent catalyst added:** Fed cut path via private credit cascade (HANS/BROCK)

**Position view:** FXY long, 4 shares starter, entry decision card issued Mar 27 at USD/JPY 160.

**Conviction:** HIGH

---

### TIMELINE v1 — Established
**Author:** PROME + Will
**Action:** Created forward-looking expected progression from research, KB, and STATUS.md.

**Key branch points defined:**
- Apr 1: Tankan (strong → April hike live; weak → May only)
- Apr 15: Feb TIC data (large selling → thesis confirmed; mixed → slower)
- Apr 23-24: BOJ meeting (hike → carry unwind fires; hold → wait May 1)
- May 1: BOJ meeting (BASE CASE HIKE)
- Mid-May: ESR disclosures (first real MTM damage visible)
- Late May: April CPI (oil shock + SK disruption reflected)
- June: Sato joins board (hawk→dove swap), Takaichi-Ueda collision window

**Horizon:** Through Q3 2026

---

## PRIOR THESIS EVOLUTION (reconstructed from research history)

These entries are reconstructed from git history and research outputs to establish the audit trail pre-CHANGELOG. Not as detailed as future entries will be.

### ~2026-02-08 — Channel 1 Established (Life Insurer Deep Dive)
**What changed:** First comprehensive mapping of Japan life insurer → UST transmission mechanism. Quantified Big 4 exposure, built scenario framework (base/stress/crisis), identified ESR as binding constraint.
**Old view:** "Japan might sell Treasuries" (vague, headline-level)
**New view:** Specific mechanism with quantified flows ($80-500B range), identified actors (Meiji most vulnerable), defined triggers (ESR thresholds, auction failures)

### ~2026-02-12 — Channel 3 Reshaped (Floating Mortgage Bomb)
**What changed:** Discovered 75% floating rate mortgage structure. Identified hard political ceiling on BOJ at 0.75%.
**Old view:** BOJ terminal rate 1.25-1.5% (market consensus); Takaichi-Ueda collision "possible"
**New view:** Terminal rate 0.75% (political ceiling); collision "inevitable"; D2 (YCC return) probability 30-35% → 32-40%

### ~2026-02-22 — Channel 1 Deepened (RP-SAM-4)
**What changed:** ESR regime change quantified (SMR 933% → ESR 219%). Hedged UST returns confirmed negative vs JGBs. Individual insurer hedge ratios mapped.
**Old view:** Repatriation thesis directionally correct but timing uncertain
**New view:** Timing anchored to April 2025 ESR implementation + FY-end March 2026 disclosures

### ~2026-03-17 — Oil-in-Yen Structural Added (SK Refiner Crisis)
**What changed:** SK refiner feedstock crisis tracked. Run cuts confirmed 12 days ahead of initial April 7 estimate. Force majeure declared.
**Old view:** Oil impact on Japan = generic "energy importer" narrative
**New view:** Specific transmission: SK cuts → Asia-Pacific product shortage → Japan CPI upward surprise → BOJ hike MORE urgent. Two-phase yen dynamic (weak then strong).

### ~2026-03-24 — Independent Catalyst Added (HANS/BROCK Fed Path)
**What changed:** Private credit cascade signal from HANS. 9 funds gated (APO, ARES). Fed cut path identified as independent carry unwind trigger.
**Old view:** Carry unwind requires BOJ action or intervention
**New view:** USD/JPY sub-145 possible on U.S. credit deterioration alone, without BOJ

### ~2026-03-27 — Entry Decision Issued (USD/JPY 160 Breach)
**What changed:** USD/JPY breached 160.106. Intervention paradox formalized. FXY entry decision card issued.
**Old view:** Waiting for catalyst hierarchy (BOJ > oil resolution > intervention > repatriation)
**New view:** Buy now in tranches. Oil scenario analysis shows FXY wins in all 3 scenarios. Asymmetric setup.

### ~2026-03-30 — BOJ Summary of Opinions + Board Stacking
**What changed:** Most hawkish Summary of Opinions in normalization cycle. Takata dissented for 1.00%. "Raise without hesitation" language. Separately, Takaichi nominated 2 dovish academics to board.
**Old view:** BOJ debate is "when to hike"
**New view:** BOJ debate is "how much to hike." But medium-term political risk rising — dovish majority forming by 2027.

---

*Future entries: Add below the most recent dated entry, above the PRIOR section. Include: date, which doc changed, what changed, why, old view → new view. Tag THESIS changes with version number.*
