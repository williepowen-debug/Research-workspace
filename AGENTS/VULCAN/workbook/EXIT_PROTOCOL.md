# VULCAN — Exit Protocol & Falsification Rail

**Newest entry: 2026-10-09** (closeout re-read: thesis-kill **1 of 4** unchanged — leg 1 no hyperscaler has guided · leg 2 Mag-7 34.54% [10/01 slot] moving AWAY from kill · leg 3 memory healthy, Samsung + MU 10-K agree, Apple's memory-cost order cut is a DEMAND crack not a price fall · leg 4 no T1 8-K, ORCL chip-lease entity is talks only; next dated rewrite trigger unchanged = first of {§4b ~10/28 · 11/15}) · *prior: 2026-10-08 leg-by-leg re-read; 2026-10-01 Micron FQ4 graded, §4 resolved → §4b live, dated log → `archive/EXIT_PROTOCOL_LOG_ARCHIVE_2026-10.md`* — **this is the freshness claim; bump it whenever an entry lands** *(DAEDALUS PR#6 / Falsification #3, 2026-09-17: the provenance line below was standing where the freshness claim belongs, so the surface certified itself stale)*.
**Kill rail first derived: 2026-08-13** *(provenance, not freshness — first authored — VULCAN carried no kill tree, no EXIT_PROTOCOL and no dated falsification surface across its 16-file inventory from build 2026-07-10 until today. Flagged by DAEDALUS at the 8/7 Production Review as the one genuine F5 gap in the fleet; Market-L3 requires one, blueprint §4 ★. Reference shape: FALCON `workbook/EXIT_PROTOCOL.md` 7/30.)*

**This file holds kill/exit conditions and nothing else.** `STATUS.md` is canonical for scores and live reads; `workbook/PREDICTIONS.tsv` is canonical for registered prediction text. **Where a kill condition is also a registered prediction, this file REFERENCES it by ID and does NOT restate it** — a condition written in two places drifts in one of them.

> ### Why the distinction this file turns on
> **CHANNEL-KILL ≠ THESIS-KILL.** A strong memory quarter kills S2's live bearish read; it does not touch the concentration thesis, which migrates to S1/S3. §1 is the thesis. §2 is per-channel. Never report a channel death as a thesis death, and never let a surviving thesis excuse a dead channel from being re-scored.

---

## 1. THESIS KILL — the specified form

**The thesis:** *the AI-capex buildout is the largest systemic vector in the tape — it concentrates index risk into a handful of megacaps, its FCF math gates HENRY's HEN-36, its compute demand collides with a supply-constrained grid, and its supply chain funnels through Taiwan.*

⚠️ **The prior sentence (STATUS:133) was unusable and this replaces it.** It read: *"Thesis dies only if AI-capex re-accelerates AND concentration unwinds cleanly AND memory stays healthy — multi-quarter, testable at each earnings stack."* Three legs, **no levels, no windows, no instruments, no session counts, no from-state** — the PAT-072 shape that fails silently because it can never be evaluated. Each leg below now carries a number, an instrument, a window and the state it is measured FROM.

| # | Leg | From-state (2026-08-13) | Kill condition | Instrument | Window | Met? |
|---|---|---|---|---|---|:---:|
| **1** | **AI-capex re-accelerates** | FY26 aggregate 4-name guide **~$735-760B economic** (VULCAN-01 HIT 7/31), vs 2025's ~$410B | FY27 aggregate guide implies **≥ +40% YoY** off the FY26 base (i.e. **≥ ~$1.03T**), against a consensus that expects decel to ~+25% | **Governed by `VULCAN-10`'s registered text — read it in `PREDICTIONS.tsv`, do not restate here.** Jan-2027 company guides, not analyst estimates | resolves **2027-02-15** | ❌ |
| **2** | **Concentration unwinds cleanly** | **Mag-7 32.98% of S&P 500 [SPY fund weight, 2026-08-20, issuer-primary]** — ⚠️ *from-state MEASURED 8/21, was an aggregator's ~32.5% until then* | Mag-7 share falls to **≤28%** and holds **3+ consecutive months**, with **no VIX print >30** and **no SPX drawdown >15%** anywhere in that window — "cleanly" means the risk leaves without the repricing | **`tools/mag7.py` → `workbook/MAG7_SERIES.tsv`** — SSGA's daily SPY holdings file (issuer-primary), append-only, content-vintage, fail-loud, validated each run with zero free parameters. ⚠️ **A FUND weight, not an S&P DJI INDEX weight** (the committee publishes no free constituent weights) — quote the basis. ⚠️ **Alphabet has TWO classes in the index (GOOGL + GOOG) and both count; dropping one understates by ~2.4pp.** *(Was aggregator-cited and flagged 'the weakest instrument on the rail' from 7/12 until 2026-08-21 — that gap is now closed.)* VIX/drawdown are **VIOLET's numbers; the owner's value governs** | continuous; re-read every closeout | ❌ |
| **3** | **Memory stays healthy** | DRAM contract **rising** (3Q26 fcst +13-18% QoQ); spot **rising** (DDR5 **$52.70**, DDR4 **$87.72**, 8/13); MU FQ3 GM **84.6%** | DRAM contract price growth stays **≥ 0% QoQ for 4 consecutive quarters** (3Q26, 4Q26, 1Q27, 2Q27) — i.e. no roll through mid-2027 | TrendForce contract series + MU FQ4/FQ1 prints (SEC-primary) | through **2027-06-30** | ⚠️ **CURRENTLY TRUE** — 10/01: 3Q26 realised UP, 4Q26 fcst +10–15% ⇒ **1 of 4 quarters in hand** [KB-186/187] |
| **4** 🆕 *(ADDED 2026-09-29, before the MU print — see §8)* | **Financing structure de-risks** | ORCL off-BS DC leases not yet commenced **$288B** [10-Q, period end 2026-08-31] · NVDA guarantee book **$108,529M** max gross (`VULCAN-17` baseline) · tenant force majeure **n=1** (Jupiter, 9/24) · AI-infra deals PULLED **0** (SB Energy POSTPONED ≠ pulled) | **ALL THREE, across the next TWO quarterly filings of each issuer:** (a) ORCL's not-yet-commenced DC lease commitments read **≤ $288B** at both its Q2 FY27 and Q3 FY27 10-Qs; (b) NVDA's guarantee book is **reduced through `VULCAN-17`'s BULL branches (i)/(ii)** at one or more readings and **never** through (iii)/(iv). ⚠️ Flat-with-no-successor is `VULCAN-17`'s STRESS signal, not a de-risk, so "stops growing" alone does NOT satisfy (b); (c) **zero** further tenant force-majeure notices and **zero** AI-infra deals PULLED (S5's letter) in the window | `tools/edgar_watch.py` + own reads of the commitments notes (ORCL CIK 0001341439; NVDA per `VULCAN-17`) · S5 band letter for PULLED | resolves **2027-03-31** (after ORCL's Q3 FY27 10-Q, ~mid-March; NVDA's Q3 FY27 10-Q ~11/19 and FY27 10-K ~late Feb are the two NVDA readings) | ❌ |

> 📦 **Dated thesis-kill re-evaluations 2026-08-13 → 2026-08-27, and the 8/13 from-state record, MOVED VERBATIM 2026-10-01 → `archive/EXIT_PROTOCOL_LOG_ARCHIVE_2026-10.md` §A** (READ-CAP: this file was over the 54,250 B physical read cap). The table above is the live rail; the newest re-evaluations stay in §7.

---

## 2. CHANNEL KILL — per-channel, with the migration path

**A channel death must name where its evidence goes.** A channel that dies into nothing was never a channel.

| Ch | Channel-kill condition | Migration path on death | Status |
|---|---|---|:---:|
| **S1** | Two consecutive quarterly stacks (≥2 of 4 names each) guide capex **flat-or-down YoY** with **no** index-level repricing — the buildout ends without the unwind | Thesis leg 1 fires; concentration mechanism migrates to **VIOLET** as a pure vol call and VULCAN's seat loses its core | **ALIVE** — capex net RAISED 7/31, agg ~$735-760B |
| **S2** | DRAM contract **≥0% QoQ for 4 straight quarters** AND memory equity outperforms QQQ over the same span — the cycle neither rolls nor is repriced | Cost-push evidence migrates to **S1** (capex-cost line) and **CARL** (goods); the cycle-roll read dies, the concentration thesis does not | **ALIVE — score 2 since 2026-10-01** (`VULCAN-11` FALSIFIED). Conjunct 1 at **1 of 4 quarters** (3Q26 up; 4Q26 fcst +10–15%); conjunct 2 (memory equity vs QQQ over the span) **NOT measured** — the S2 equity series is stale since 8/24. **The kill moved CLOSER** — see §3 |
| **S3** | Grid constraint stops binding: PJM/ERCOT interconnection clears faster than load is added for **2 consecutive planning cycles** | Migrates to **WATT** entirely; VULCAN retains only the capex→MW conversion | **ALIVE** — ERCOT queue frozen under audit (KB-085) |
| **S4** | Export controls **net loosen** in both directions for **2 consecutive quarters** AND TSMC monthly revenue YoY stays ≥+20% | Dies to a watch-line; kinetic risk stays **HAWK's** | **ALIVE** — genuinely two-sided; the cleanest independent root |
| **S5** | AI-infra new issues clear **at or inside talk** for **2 consecutive quarters** AND no second jurisdiction writes an IG threshold into a utility tariff | Financing evidence migrates to **LIQUID** (spread tells) and **BROCK** (private credit); VULCAN keeps only the obligations mechanism | **ALIVE** — DDTL 5.5 cleared **+100bp** wide of the prior identical facility (KB-075) |

---

## 3. ⚠️ THE CHANNEL UNDER ACTIVE PRESSURE — S2, stated against myself

The 8/3 S2 upgrade 2 → 3 rested on **two** stated legs. **One of them has failed.** 🔴 **2026-10-01: the registered test of Leg B (`VULCAN-11`) FALSIFIED it, and the upgrade is reversed — S2 = 2.**

- **Leg A — contract-price second derivative:** 3Q26 forecast **+13-18% DRAM / +10-15% NAND** vs 2Q26's +58-63% / +70-75%. ⚠️ *general* vs *server* DRAM — the deceleration survives the perimeter mismatch, the magnitude does not. **INTACT, untouched.**
- **Leg B — the equity de-rate as a LEADING indicator:** 🔴 **2026-10-01: FALSIFIED — DEAD, not disarmed.** `VULCAN-11` resolved FALSIFIED on all three legs (TrendForce 4Q26 conventional DRAM **+10–15%**; Micron FQ1 revenue guided UP to **$61.5B** vs **$54.23B**; MU 9/30 close **$1,065.11** ≥ $940.70). Registered action executed: **S2 3 → 2**, and no terms-lead-price indicator is extended into S2. The re-arm rule at the end of this bullet was UNGRADEABLE (0 of 8 slots) and is moot. *History follows:* ~~❌ **FAILED.** It retraced in 10 days and the decoupling flipped sign (KB-071). A leading indicator that round-trips inside two weeks was a drawdown.~~ ⚠️ **REVISED 2026-08-21 — "FAILED" WAS WRONG, AND SO WAS THE EVIDENCE FOR IT.** The 8/3→8/13 "retrace" was measured over a window **starting at the drawdown's own lowest close** (MU $829.50, 8/3). Extremum-anchored windows manufacture the move they measure; that window cannot carry the verdict. **Corrected status: UNRESOLVED, not failed.** Three bases, reported together because they disagree and **the disagreement is the finding**: **(a)** rolling-1mo, the only window fixed *before* the data — spread **+19.02 → +13.14 → +4.54pp**, narrowing; **(b)** peak-to-current — **KLAC −38.6% · MU −19.1%** vs **QQQ −4.6%**, de-rate large and intact; **(c)** YTD — the complex is **+45% to +483%**, so a 30% drawdown off a parabolic June top is arithmetic, not a roll. **The indicator STAYS DISARMED, on a better reason: it has no specified basis**, and one that fires / un-fires / re-fires across three consecutive readings is measuring my window choice, not the market. ⚠️ **Deliberately NOT re-armed on the 8/18-19 re-fire, which agreed with my prior.** **Pre-specified re-arm rule, registered now and grading at 9/30: rolling-1mo spread ≥ +10pp for 3+ consecutive readings AND further contract deceleration.** [KB-089/091/092 · **L-17**]

**Two known perimeter defects now sit under S2's standing −25% QoQ rule, and they point in opposite directions:**
1. **DRAM/NAND split** (KB-057): 2027 DRAM supply stays tight while NAND eases. A NAND roll with a DRAM hold resolves VULCAN-02 ambiguously.
2. **Consumer/datacentre split** (KB-081, new): the deceleration is a **consumer** story (affordability limits) while the **datacentre** leg *tightens* (customers price-insensitive). The rule is measured on a blend that is bifurcating.

⇒ **The rule is now known to be measured on a blend of two blends.** Registered here rather than fixed: **do not rewrite VULCAN-02's gate** (own L-11 rule (b)); grade it on the DRAM leg per KB-057 and record a SPLIT as a spec failure against me, not a HIT. 🆕 **10/01: the split did not arise — both legs rose (`VULCAN-02` HIT, branch a).**

---

## 4. BIDIRECTIONAL FLIP (Micron FQ4) — re-registered 2026-08-13 · 🔴 RESOLVED 2026-10-01, SPENT

> 🔴 **RESOLVED 2026-10-01 — CONFIRMED (ceiling) ON THE LETTER, via the guide branch (`VULCAN-12` HIT). THIS FLIP IS SPENT; §4b IS THE LIVE FLIP.** FQ4 GAAP GM **86.76%** (≥86.6%: the moat's first leg MET — no stall) but FQ1 guided **below** on both bases (GAAP ~85.95%, non-GAAP ~86.25%). ⚠️ **Composition disagrees:** Micron attributes the dip to incentive comp flowing through inventory, not to pricing, and its 26 SCAs carry contractual floor/ceiling bands that margin expanded THROUGH [KB-188] ⇒ the *Confirms* row's consequence text below (*the ceiling is real and measured; the memory maker does not capture the rent*) is **NOT executed** — the letter confirmed, the magnitude was not measured. No retraction owed. Grade: `workbook/MU_FQ4_RESOLVER.md` §6.

⚠️ **The previous flip (STATUS:135) named the 7/22-7/29 earnings stack and EXPIRED with it on 7/31.** No successor existed for 13 days. A rail whose only flip has expired is a rail that cannot fire.

**Next resolver: MU FQ4 FY26 — 🔴 CONFIRMED 2026-09-30, 2:30 p.m. Mountain (16:30 ET), AFTER THE CLOSE.** *(Micron press release 2026-08-26 16:01 ET; `date_class: confirmed`.)*

> ~~*Superseded: "**~2026-09-22** (window opens 09-17; re-dated 2026-08-27 from ~9/29 — derived from MU's own filing history, `fiscalYearEnd=0903` is a NOMINAL EDGAR marker not a period end. Still MODELED)*"*~~ · ~~*"Headroom to the 9/30 resolve date is now ~6-13 days, not ~1."*~~
> 🔴 **BOTH SENTENCES WERE WRONG AND THE SECOND WAS THE DANGEROUS ONE — corrected 2026-09-02, struck not deleted.** The re-derivation assumed a **52-week** fiscal year; MU runs **52/53-week** years and FY2026 is a **53-week** year ending **2026-09-03** — so `fiscalYearEnd=0903` was **RIGHT**, and the counter-example (FY2020 10-K `period_end` **2020-09-03**) was sitting in this desk's own `workbook/EDGAR_SEEN.tsv` the whole time. **Micron had already announced 9/30 on 8/26, the day BEFORE I re-derived it.**
> ⚠️ **REAL HEADROOM IS ~0 HOURS, NOT 6-13 DAYS.** VULCAN-02/-11/-12/-14 all resolve **2026-09-30** and the print lands **after that day's close** ⇒ **any grade needing the FQ4 print is a 2026-10-01 action** (registered in `docket/CATALYSTS.tsv`). The 8/27 note said the change *"moved in my favour, which is exactly when to be most careful about touching anything else"* — and then banked it. [KB-135]

| Direction | What must be observed at MU FQ4 | Consequence |
|---|---|---|
| **Confirms the bearish read** | GM expansion **stalls** (≤84.6% GAAP) or FQ1 guide below FQ4 on the same basis | The LTA/presold ceiling is real and measured; the memory maker does not capture the rent; S2's cost-push into S1 and CARL is the live transmission |
| **Falsifies it** | GM expands **≥+2.0pp** (≥86.6%) **and** FQ1 guided at-or-above | "Presold" is a moat, not a ceiling; **retract KB-055's framing and correct WALTER, CARL and HENRY**, all of whom got the ceiling version from me |

**Governed by `VULCAN-12`'s registered text — read it in `PREDICTIONS.tsv`.** Explicit NO-VERDICT band and the GAAP-vs-non-GAAP basis discipline live there.

### 🆕 4b. SUCCESSOR FLIP — PRE-REGISTERED 2026-09-29, effective the moment §4 resolves (grading 2026-10-01) — 🔴 **LIVE since 2026-10-01**
**Why it is written before MU prints:** the 7/22 flip expired 7/31 and the rail ran **13 days with no flip at all** (§4 opening line). §4 expires on 10/01. **The successor is the late-October hyperscaler cluster** (MSFT · GOOGL · META · AMZN Q3 prints, dates TBC, registered in `docket/CATALYSTS.tsv` as estimated). **It introduces NO new threshold** — both directions are existing standing rules from `STATUS.md`'s triad:

| Direction | What must be observed across the cluster | Standing rule it applies |
|---|---|---|
| **Confirms the fragility read** | the stock FALLS on a capex RAISE in **≥2** cluster prints, OR management cites inference-price / open-weight / ROI pressure, OR **any** name guides capex **CUT YoY** | S1 returns-case sub-read · S1 red trigger |
| **Falsifies it (for this cluster)** | **≥2** names RAISE and are REWARDED after hours (the 7/31 pattern, §5), with no capex cut anywhere in the cluster | the returns-case sub-read's mirror; the §5 steelman repeating |
| Neither | mixed or flat | NO-VERDICT, recorded as such |

---

## 5. STANDING COUNTER-EVIDENCE — the steelman, kept verbatim

**Held here because a rail without the strongest case against its own thesis is an advocacy document.** These do **not** kill S1's mechanism (mechanism-vs-thermometer, L-02) — they attack its **repricing leg**, and S1's value depends on the unwind being *un*-priced:

- **SIG-W-20260521-013** — NVDA's 5/20 print **absorbed clean**: post-print IV crushed *below* 20d realized, **no tail bid**; the vol surface "decisively faded the catalyst" (conf 0.85).
- **SIG-W-20260622-009** — **record SOXL outflow / record SOXS inflow**: semi bearishness is **already crowded** (conf 0.75).
- **SIG-W-20260702-016** — GS Prime Book: hedge funds de-grossed US tech at a **~−4σ record** (wk ending 6/25) with **NO cascade** (conf 0.75) — the unwind may be **partly pre-positioned**.
- **Added 2026-08-13 — the market kept funding it, twice.** MSFT **+8.88%** and AMZN **+7%** AH both *rewarded* capex RAISES (VULCAN-09 MISS-DOWNGRADE), and CoreWeave raised FY26 capex to **$35-39B against $12.4-13.2B of revenue** — ~3× revenue at a ~10.4% marginal cost of debt — and the equity paid it **+16-18%**.

---

## 6. CROSS-AGENT THRESHOLDS — I do not own these numbers

| Threshold | Owner | My use |
|---|---|---|
| Mag-7 weight, vol/dispersion expression, Path-B | **VIOLET** | I own the *mechanism*; VIOLET owns the repricing. Reconcile to ONE figure |
| AI-credit **spread tells** (HY/IG, CDS, the GS/JPM basket) | **LIQUID** | I own capex/fundamentals + obligations. **Do NOT maintain a parallel spread series** — KB-075's DDTL ladder is routed to LIQUID, not kept as a rival index |
| PJM/ERCOT power price, firm-vs-forecast GW | **WATT** | Adopt verbatim *(wording corrected 2026-09-06)*: **~55 GW = aggregate utility-reported forecast (self-reported, non-coincident, contains duplication) · ~32 GW = firm coincident-peak (PJM-vetted). Never net, never average. Neither is an interconnection-queue nameplate figure — the ~250 GW generation queue is a third population** (KB-087 + KB-146) |
| China capacity timeline (CXMT, bit output) | **ZHAO** | The number that would move S2's shortage premise; unsized, requested |
| Taiwan kinetic | **HAWK** | S4's tail; I own only the semiconductor consequence |

---

## 7. TIME-BASED REVIEW + DATED REWRITE TRIGGER

> 🔴 **2026-10-01: THE 9/30 TRIGGER FIRED AND THE MICRON-DEPENDENT HALF IS DONE** (§4 resolved → §4b live · §2/§3 S2 rows · this section's 10/01 entry). **Next dated rewrite trigger: the FIRST of {§4b resolving at the late-Oct hyperscaler cluster (~2026-10-28, estimated) · 2026-11-15 backstop}**, registered in `docket/CATALYSTS.tsv`. The 9/30 trigger's derivation history — re-dated twice, because a whichever-first trigger inherits every leg's date [KB-135] — moved verbatim to the archive's §C.

- **Re-read this file at every closeout falsification check.** Boot↔closeout symmetry: what you read at boot, you write back.
- **Thesis-kill leg count: re-evaluate every closeout.** It is `1 of 4` (re-read 2026-10-01); a count that never moves is a count nobody is checking.
- **⚠️ DATED REWRITE TRIGGER** *(per `[[finding_banner_is_a_warning_not_a_fix]]` — a banner without a date is a deferral)*: **rewrite this rail on the FIRST of {§4b resolves at the hyperscaler cluster (~2026-10-28, estimated) · 2026-11-15}.** It inherits the cluster row's date and moves with it. **Carried to that rewrite:** PROME's disinflationary-productivity falsifier (owed since 8/21) and the S1/S5 channel-kill rows the cluster resolves.
- **If a future reader finds this file asserting a live condition that has already resolved, that is the failure this rail exists to prevent** — and the §3 self-indictment is the model for how to record it.

---

> 📦 **Re-evaluations 2026-09-06 PM → 2026-09-25 MOVED VERBATIM 2026-10-01 → `archive/EXIT_PROTOCOL_LOG_ARCHIVE_2026-10.md` §B.** The two newest stay live below.

### 🔴 THESIS-KILL RE-EVALUATION 2026-09-29 (Will-launched pre-market boot; closeout step 3): **STILL 1 of 3 — re-read leg by leg.**
- **Leg 1 — FY27 aggregate capex guide ≥ +40% YoY: NOT satisfied.** No hyperscaler guided 9/25 → 9/29. OpenAI's frontier pause (report 9/25, no resume date) is a **workload** pause at a lab, not a guide; it would bear on this leg only through a later guide. [KB-178]
- **Leg 2 — Mag-7 ≤28% held 3+ months: NO.** Last read **33.5528%** (holdings 2026-09-01), now **28 days stale** — `mag7.py` slot 3 (9/25) MISSED as well. NVDA, the largest weight, rose +1.68% on 9/28 on a $150B buyback. [KB-183]
- **Leg 3 — memory stays healthy: TRUE.** TrendForce **raised** its 2027 HBM ASP forecast to +121% YoY (9/29, primary); KOSPI's −2.70% / SK Hynix −5.05% on the 9/28 re-open is a rates/OpenAI thermometer, not a memory-price datum. [KB-179/180]
- **The structure-leg gap (9/25) got one more instance, and one more strand beside it:** CRWV 5Y CDS ~855bp (LIQUID's ISDA figure) with primary still open [KB-176]; AI issuers 29% of 2026 IG at 20y+ [KB-177]. **New: a DEMAND strand** (OpenAI pause) that the rail also has no leg for — a lab-level workload pause is neither a capex guide nor an index share. **Both go to the 10/01 rewrite.**
- **Dated rewrite trigger: NOT DUE — 2026-09-30, 1 calendar / 1 trading day out** (boot leg 6). MU prints AFTER that close ⇒ the rewrite is a **2026-10-01** action. Unchanged.

### 🔴 THESIS-KILL RE-EVALUATION 2026-10-01 (PROME-spawned Tier-1, DOCKET L547 — the Micron grade + the Micron-dependent half of the rewrite): **STILL 1 of 4 — re-read leg by leg, and the one leg that moved moved TOWARD the thesis dying.**
- **Leg 1 — FY27 aggregate capex guide ≥ +40% YoY: NOT satisfied.** No hyperscaler guided. Micron's own capex (FQ1 ~$11.5B, 1H FY27 ~$25B, higher in 2H) is memory SUPPLY, not the hyperscaler aggregate this leg is defined on [KB-186].
- **Leg 2 — Mag-7 ≤28% held 3+ months: NO.** Last read **33.5528%** (holdings 2026-09-01), **30 days stale**; next slot 10/02 post-close.
- **Leg 3 — memory stays healthy: TRUE, and STRONGER.** 3Q26 contract REALISED up (Micron DRAM prices +high-teens %, NAND ~+30% QoQ; TrendForce 3Q fcst +13-18%); 4Q26 forecast **+10–15% DRAM / +15–20% NAND** (TrendForce 9/30, public) ⇒ **1 of the 4 required quarters in hand, the 2nd forecast positive**; Micron guides *"sequential revenue growth each quarter"* of FY27 [KB-186/187]. ⚠️ **Read the direction:** leg 3 completing is a step toward the THESIS dying, and S2's score fell to 2 the same day (`VULCAN-11` FALSIFIED) — consistent, not contradictory.
- **Leg 4 — financing structure de-risks: NOT satisfied (window open to 2027-03-31).** No ORCL or NVDA filing since 9/29; ORCL's $3.3B guarantee passed its on-paper maturity with **no 8-K** (status UNKNOWN; next vehicle the Q2 FY27 10-Q). One lender-side cap on AI debt was reported (PGIM CLO, 15%, n=1, unnamed sources [KB-189]) — a capacity CONSTRAINT, i.e. the opposite of a de-risk.
- **§4 RESOLVED (CONFIRMED on the letter, composition disagreeing); §4b is the live flip.** Channel kills: none died; **S2 moved closer to its kill** (conjunct 1 at 1 of 4 quarters) while its SCORE fell — a channel can be less stressed and still alive.
- **Dated rewrite trigger: FIRED 9/30; Micron half executed today; next = the FIRST of {§4b resolves ~10/28 · 2026-11-15}.**

### THESIS-KILL RE-EVALUATION 2026-10-08 (PROME-spawned Tier-1 wake, WQ-389; closeout step 3): **STILL 1 of 4 — re-read leg by leg, nothing moved.**
- **Leg 1 — FY27 aggregate capex guide ≥ +40% YoY: NOT satisfied.** No hyperscaler guided 10/01 → 10/08; the build slips logged this session (Abilene, ERCOT pause, Stargate WI, Finland) are DELAYS on builds kept [KB-197/199].
- **Leg 2 — Mag-7 ≤28% held 3+ months: NO.** Slot 4 (10/01 holdings) 34.5445%; 10/08 off-cadence dry-run 34.9722% (10/07 holdings) — the leg is moving AWAY from kill [KB-203].
- **Leg 3 — memory stays healthy: TRUE, and a 2nd major agrees.** Samsung Q3 OP ~KRW107.40T, +20.0% QoQ (issuer primary) [KB-196].
- **Leg 4 — financing structure de-risks: NOT satisfied.** No T1 8-K at ORCL/NVDA/CRWV since 10/01 (`edgar_watch.py` 10/08); the structure strand grew by commentator-sourced items only (Jupiter debt ~84c, Anthropic/Broadcom converts) [KB-198/199].
- **Dated rewrite trigger: NOT DUE** — the FIRST of {§4b ~10/28 · 2026-11-15}. Unchanged.

---

## 8. 🆕 PRE-MU HALF-REWRITE — 2026-09-29 (Will-directed, before the 9/30 print)

**What was done, and why each piece is safe to write before the outcome:**

1. **Thesis-kill leg 4 ADDED — financing structure (§1).** 🔴 **The count moves 1 of 3 → 1 of 4 BY ADDITION, not because anything moved. Read it that way.** This answers the 9/25 requirement ("at least one **structure** leg, or say in writing why the thesis cannot be killed on that axis"). The three original legs test SCALE, CONCENTRATION and PRICE. Every piece of stress that arrived from 9/13 to 9/29 was STRUCTURE: leases +$28B, a force-majeure risk transfer, a guaranty counterparty's IPO postponed, and CRWV CDS ~855bp against an open primary. Without leg 4 the thesis could be declared dead at the peak of its obligations.
   - ⚠️ **Stated against myself: an added AND-leg makes the thesis HARDER to kill, which is the direction to distrust.** The guards: leg 4 has **levels, instruments and a date** (2027-03-31), so it can be met; and it cites `VULCAN-17`'s pre-registered branch classification instead of re-deciding what a smaller guarantee book means.
2. **The "demand strand" (9/29 §7 entry) is answered as a FIRING route, not a kill leg.** A lab-level safety pause is a way the thesis could come TRUE (compute demand disappoints → deferred contracts → S1/S5), not a way it dies. It is registered as an **S1 sub-read** in `STATUS.md`'s triad, the home of firing state, beside the useful-life and returns-case sub-reads.
   - **Rule:** a safety pause or safety law reaches a CONTRACT.
   - **Base rate at registration:** three pauses at two labs — OpenAI July (~2 weeks); Anthropic late-July to August (several weeks, disclosed 9/2); OpenAI 9/25 (open-ended). **ZERO contract, lease or capex changes** [KB-166/178/185].
   - **Promotion test:** fires on **2 distinct events** ⇒ propose channel **S6** to Will.
3. **Successor flip pre-registered (§4b)** so the rail is never without a live flip after 10/01.

**Owed 2026-10-01 — DISCHARGED 2026-10-01:** §4 graded from the resolver sheet and marked SPENT; §4b made live; the §2/§3 S2 rows rewritten; the dated re-evaluation log moved verbatim to `archive/EXIT_PROTOCOL_LOG_ARCHIVE_2026-10.md`. **Not discharged, re-dated:** PROME's disinflationary-productivity falsifier → the ~2026-10-28 rewrite row (it does not depend on Micron). The original owed-line is in the archive's §C.

