# VULCAN — STATUS

**Last Updated:** **2026-09-29 (Tue) 08:59 ET (`date`) — Will-launched in-folder session, boot 08:47 ET, pre-market.** *(Previous: 2026-09-25 Will-launched.)* **Session product:** news catch-up 9/25 → 9/29 (`reports/2026-09-29_news-catchup_0925-0929.md`); WALTER lane **5 → 0**; EDGAR sweep (ORCL DEF 14A only); KB-176..183; the 9/25 slot recorded **MISSED**. 🔴 **No score, band, threshold or prediction moved.** Levels (**9/28 CLOSE**, pre-market read): NVDA **$228.86** · MU **$1,053.98** · ORCL **$132.60** · CRWV **$85.07** · SOXX **$560.79** [own `fetch.py` 2026-09-29 08:50 ET — re-pull before citing]; 10Y **5.24%** (9/25, 19-yr high, secondary).

**Class:** Market-agent (AI-capex/semi/memory → systemic risk) · **Spawnable by:** PROME or Will · **Maturity:** **L4** (DAEDALUS `FLEET_MAP.tsv` since 2026-09-05; Last_scored 2026-09-17, `7bfee0060`)

> ## 📖 WHERE THINGS LIVE (READ-CAP split 2026-09-02; rotated again 2026-09-25)
> | Surface | Holds | Boot path? |
> |---|---|---|
> | **`STATUS.md`** (this file) | **Canonical for SCORE, BAND STATE, FIRED-COUNT, current live read, owed items** | **YES — read whole** |
> | `CHANNEL_DETAIL.md` | Evidence under the scores. §A–D verbatim at the 9/2 split; **§E = this file WHOLE as of 9/13, moved verbatim 2026-09-25 (30,476 B, crc `0x02b4969e`)**. LIVE, not archived | No — on demand, per channel |
> | `THESIS.md` · `workbook/EXIT_PROTOCOL.md` | Stage tables · the kill rail | No — closeout reads |
> | `reports/2026-09-25_news-catchup_0913-0925.md` + `_live-sweep_1015ET.md` | This session's sourced news record | No |
> | `archive/` | Frozen history (STATUS/SCRATCH/NEXUS archives, resolved PREDICTIONS) | No |
>
> ⚠️ **Rule 17:** `CHANNEL_DETAIL.md` is OFF the boot path. A watch or owed action written there does not travel; put it here, in `PREDICTIONS.tsv`, or in `docket/CATALYSTS.tsv`.

---

## CONVERGENCE MATRIX (universal 5-pt + local state)

| # | Channel | Score (1–5) | Local state | Independence | Key signal [src, date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| **S1** | AI-capex concentration | **3 🟠** | **YELLOW band (tripped 9/2), NOT-FIRED.** Mag-7 **33.5528%**, **not re-measured since 9/1** (`mag7.py` slots 9/11 and 9/18 MISSED). Capex still RAISED (7/31 cluster; agg ~$735-760B econ). 🆕 The **9/12–14 "pace the frontier" shock** (Amodei essay; Altman IPO "not 2026") was a **PRICE shock**: SOX −5.9% on 9/14, memory fully retraced by 9/23; **0 capex, contract or DC-plan changes found** [KB-166]. Counter-signal: JPM says **short-term compute is priced at a premium** [KB-175, ASSUMPTION]. 🆕 **9/29: OpenAI PAUSED training/eval/tool-inference of its frontier models (report 9/25, no resume date, 2nd pause in <3 months)** — the first realised case of the safety turn reaching compute DEMAND; an OPERATIONAL pause, **0 capex/contract/lease changes** ⇒ trigger and leading indicator UNMOVED [KB-178]. NVDA +$150B buyback 9/28 [KB-183] | S1+S3+S5 share ONE root; count it once | Mag-7 33.5528% [SPY fund weight, holdings 9/1, `mag7.py`]; breadth RSP−SPY 63d +3.70pp [9/1] | **≥40% AND breadth ≤ −7.5pp**, OR hyperscaler capex **cut** YoY |
| **S2** | Memory cycle | **3 🟠** | **A decelerating RISE, not a roll.** TrendForce **lifted** 4Q26 contract outlook; sell-side DRAM ASP **+16.5% QoQ 3Q → +5.4% 4Q**; spot ~flat, *"no actual demand orders"* [KB-172]. −25% rule far away. 🔴 **The 9/30 RE-ARM rule is UNGRADEABLE BY CONSTRUCTION:** 6 of 8 slots missed (8/27 · 8/28 · 9/04 · 9/11 · 9/18 · 9/22); only 9/25 and 9/29 remain. The indicator stays DISARMED by default, which is **not** a clean NOT-MET. S2 series last row **2026-08-24**. 🆕 **9/29:** TrendForce **raised 2027 HBM ASP to +121% YoY** (forecast); KOSPI −2.70% / Hynix −5.05% on the 9/28 Chuseok re-open = a rates/OpenAI thermometer, not a demand datum [KB-179/180] | Not purely independent (an AI-capex roll pulls memory) | DDR5 $53.93 / DDR4 $91.05 [own series, 8/27]; TrendForce + Seoul Economic Daily [9/23–25, secondary] | Contract **−25% QoQ sustained** |
| **S3** | AI-capex → power demand | **3 🟠** | PJM DC load to 2030: **~55 GW aggregate utility-reported forecast / ~32 GW firm coincident-peak** (two bases, never netted; neither is a queue nameplate figure; the ~250 GW generation queue is a third population) [WATT seam 8/13, wording 9/6]. 🆕 **ORCL FORCE MAJEURE on Project Jupiter** (2.45 GW, STACK/Blue Owl, 9/24): power delay (gas pipeline → 2027-02-01; fuel-cell air permit pending) ⇒ higher rent deferred **~1 yr** (unnamed source); ORCL says on schedule [KB-167/174]. **A DELAY, not removal of FIRM capacity ⇒ trigger NOT met.** Water constraint named 8/27 (AEOLUS) | Shares S1's root | TechCrunch 9/24 (citing Bloomberg); Reuters analysis 9/24 18:59 ET | Grid-side refusal or curtailment that removes FIRM capacity from a contracted DC build |
| **S4** | Supply-chain / geopolitics | **3 🟠** | TSMC **cum Jan-Aug +39.3%**, band no-stress [6-K 9/10, KB-157]. **No Entity List ADDITIONS** 9/1–9/25. 🆕 **11/10 = TWO live clocks:** the BIS Affiliates Rule re-add and MOFCOM No. 70 expiry. The IEEPA leg has been VOID since 2026-02-24; Bessent's 2027-01-10 "Busan" extension is **VERBAL ONLY**, 0 instruments moved [ZHAO primary 9/25, KB-171]. Chips "not on the agenda" at the summit | **The only cleanly independent root** | `tsmc_watch.py`, SEC 6-K primary | Equipment ban / fab-level cutoff, OR Taiwan kinetic |
| **S5** | AI-infra financing *(core since 8/3)* | **3 🟠** | 🆕 **ONE FINANCING-STRUCTURE EPISODE, counted once** [KB-167..170, 173/174]: ORCL off-BS DC leases **$260B → $288B** in one quarter; the **$3.3B lessor guarantee has 0 mentions** in the 10-Q (status UNKNOWN); notes FV **84.6%** of carrying; Jupiter FM; ORCL 5Y CDS record **221.78bp** (single source, LIQUID's tell); **SB Energy (NVDA's $105B guaranty counterparty) IPO POSTPONED**. **AGAINST:** SoftBank **$11.1B HY inside talk**, CRWV **$4.2B converts upsized**, AI notes re-tightened by the 9/24 close; Fed hiked to **3.75–4.00%** (9/16). Standing: CRWV DDTL SOFR+225→+450→+550; NVDA guarantee book **$108.5B** (`VULCAN-17`). 🆕 **9/29:** CRWV 5Y CDS **~855bp** (LIQUID's ISDA benchmark, 9/24) while CRWV's primary is OPEN (converts upsized 9/22) ⇒ **single-name, not cohort** (BB OAS 164) [KB-176]; AI/hyperscalers **29% of 2026 IG at 20y+ vs 8%** [KB-177, secondary]; Ellison pledge **346M → 413M** shares [DEF 14A, KB-181]; Xcel/SPS TX large-load tariff **PROPOSED, no rating threshold** ⇒ 2nd-jurisdiction leg NOT met [KB-182] | **PARTIALLY independent:** the structure/regulatory leg fires regardless of capex; the ROI leg shares S1's root | ORCL 10-Q acc `0001193125-26-389274`; CRWV 8-K acc `0001769628-26-000432` | New issue flexes **+150bp or PULLED**, OR a **2nd jurisdiction** writes an IG threshold into a utility tariff, OR a developer **fails to post** mandated collateral |

**Composite: 15/25 — HELD, THIRTEENTH session (8/13 → … → 9/13 → 9/25 → 9/29)** · **S1 3 · S2 3 · S3 3 · S4 3 · S5 3**

> ⚠️ *The per-channel arithmetic line is **machine-read** by `scripts/validate_workbook.py` (boot leg 7) against `workbook/VX.tsv` and the matrix. Do not delete or reformat it.* *(The denominator changed on 8/3: 12/20 and 15/25 are both 60%.)*

**⚠️ A HELD COMPOSITE IS NOT A QUIET SESSION.** S5's evidence moved materially this session (a lease book +$28B, the first observed force-majeure risk transfer, the guaranty counterparty's IPO postponed) and **no band fired, because the bands grade priced issues and mandated collateral while the stress is arriving as STRUCTURE.** That mis-fit is now a named requirement for the 10/01 kill-rail rewrite (EXIT_PROTOCOL §7, 9/25 entry).

**Independence note:** an AI-capex ROI disappointment drives S1, S3 and S5 at once, so count that root ONCE. S4 is the only cleanly independent root.

---

## LIVE CHANNEL READS (one current dated read per channel)

- **S1** — Mag-7 **33.5528%**, breadth **+3.70pp** · **as-of holdings 2026-09-01** · `mag7.py`. 🔴 **28 days stale; slots 1 (9/11), 2 (9/18) AND 3 (9/25) MISSED**, not cured off-cadence [L-21]. Next slot **10/02 post-close**.
- **S2** — DDR5 **$53.93** / DDR4 **$91.05** · **as-of 2026-08-27** · own series (last row 8/24). Lane reads 9/25: contract rise decelerating, spot flat [KB-172].
- **S3** — ~55 GW aggregate / ~32 GW firm (wording as-of 9/6) · Jupiter FM **as-of 2026-09-24** [KB-167/174].
- **S4** — TSMC cum Jan-Aug **+39.3%** · **as-of the August 6-K (filed 9/10)**. Next 6-K **~10/10**.
- **S5** — ORCL off-BS leases **$288B** · **as-of 2026-08-31 (10-Q filed 9/11, read 9/25)** [KB-168]; NVDA guarantee book **$108.5B max gross** (Q2 FY27 10-Q + Aug event); CRWV converts **as-of 9/22**; CRWV CDS ~855bp **as-of 9/24** (LIQUID's figure). EDGAR sweep **fresh 2026-09-29 08:49 ET** (+2 rows, ORCL DEF 14A/DEFA14A).

---

## EXIT / INVALIDATION (standing-rule-vs-state triad)

> Kill conditions live in `workbook/EXIT_PROTOCOL.md`; this table is the firing STATE.
> **🔴 THESIS-KILL: 1 of 3 legs satisfied** (leg 3, *"memory stays healthy"*, TRUE). Re-read leg by leg **2026-09-25**: no hyperscaler guided (leg 1); Mag-7 last read 33.55% but **24 days stale** (leg 2). 🆕 **A rail GAP is recorded: none of the three legs can see financing-structure stress** — carried into the rewrite.
> **DATED REWRITE TRIGGER: 2026-09-30** (first of {MU FQ4 · the 9/30 resolutions · 11/15}). MU prints after that close ⇒ a **2026-10-01** action.

| Channel | Standing rule | Current state @ level | FIRED? |
|---|---|---|---|
| S1 | Mag-7 ≥40% AND breadth ≤ −7.5pp, OR hyperscaler capex cut YoY | 33.5528% [9/1] · breadth +3.70pp · guides RAISED | **NOT FIRED** (yellow level) |
| S1 — LEADING INDICATOR *(KB-034)* | lease pauses + equipment-order cancellations before guide cuts | MSFT ~2GW lease walk (7/22) — **ARMED**. Jupiter FM is a **tenant rent deferral on a site kept**, not a lease pause, and does not re-grade it | ARMED, not fired |
| S2 | DRAM/NAND contract −25% QoQ sustained | rising, decelerating (4Q +5.4% sell-side) | **NOT FIRED** |
| S2 — LEADING INDICATOR | pre-specified re-arm rule, grades 9/30 | **UNGRADEABLE by construction** (6 of 8 slots missed) ⇒ stays DISARMED by default | DISARMED |
| S3 | compute→MW demand outstrips grid (with WATT) | 55/32 GW seam; Jupiter = DELAY on a contracted build | NOT FIRED |
| S4 | equipment ban / fab-level cutoff OR Taiwan kinetic | no EL additions since 2025-10-09; two 11/10 perimeter clocks pending | NOT FIRED |
| **S5** | new issue +150bp or PULLED · 2nd-jurisdiction IG tariff threshold · developer fails to post | SoftBank inside talk; CRWV upsized; 1 jurisdiction (WI PSC) — 🆕 Xcel/SPS Texas **filed, not approved, no rating threshold** ⇒ not a 2nd [KB-182]; **SB Energy IPO POSTPONED = AMBIGUOUS on the letter, NOT scored** (no withdrawal as of 9/29; last filing the 9/21 amended S-1). 🔒 **Pre-stated 2026-09-25, before the outcome: a WITHDRAWN S-1 is the PULLED reading** | NOT FIRED |
| **S1 sub-read** (obsolescence / useful-life) | **≥2 of 4 names change useful-life → promote to channel S6, OR MSFT shortening alone (override)** | **0 of 4, all SEC-primary-verified.** ORCL 10-Q 9/11 still carries servers at **six years** (own read). 🔴 **THIS ROW IS THE LIVE HOME OF VULCAN-07's GATE** (resolved forecast archived 9/6 — safe ONLY because this row states rule, state and verdict self-containedly). **Never reduce it to a pointer; if it must shrink, move the rule back into a live ledger first.** January re-test = **VULCAN-08** (OPEN, 2027-02-15) | NOT FIRED |
| **S1 sub-read** (returns-case) | hyperscaler stock FALLS on a capex RAISE in ≥2 cluster prints, OR mgmt cites inference-price / open-weight / ROI pressure | GOOGL −5% AH on a raise (7/22), not repeated. The Amodei/Altman pacing calls are **lab** statements, not hyperscaler management on ROI | NOT FIRED |

> 📊 **PREDICTION CALIBRATION.** **17 registered · 8 RESOLVED (HIT 5 · HIT-NOFIRE 1 · MISS-DOWNGRADE 1 · MISS 1) · 9 OPEN** (VULCAN-02 · -08 · -10 · -11 · -12 · -13 · -14 · -15 · -17). Resolved rows → `archive/PREDICTIONS_RESOLVED_2026-09.tsv`. ⚠️ **-02, -11, -12, -14 resolve 9/30 on an input printing after that close ⇒ a 10/01 grade.** VULCAN-14's input is already in (cum Jan-Aug +39.3% ≥ +37.0%), graded on its date, not early.

**Fired-count: 0 of 5.** **Leading indicators: 1 of 2 armed** (S1 armed; S2 disarmed and its re-arm test ungradeable).

**🔄 LIVE BIDIRECTIONAL FLIP — Micron FQ4, CONFIRMED 2026-09-30 16:30 ET (after the close).** Test: does the LTA/presold ceiling show up in GAAP gross margin? Frozen FQ3 GAAP **84.6%**. Governed by **VULCAN-12's registered text**.
- **Confirms the ceiling:** FQ4 GAAP GM **≤84.6%**, OR FQ1 guided **below** FQ4 on the same basis.
- **Falsifies it (moat):** GAAP GM **≥86.6%** AND FQ1 guided at-or-above ⇒ retract KB-055's framing and correct WALTER, CARL, HENRY.
- 🆕 **Pre-stated 9/25:** MU guided **~86% (GAAP and non-GAAP)**; consensus is in line. **An in-line print lands INSIDE the 84.6–86.6 gap ⇒ the FQ1 GUIDE decides** (below = CONFIRMED; flat/mixed = NO-VERDICT). ⚠️ Never compare a non-GAAP guide to a GAAP actual.

---

## OPEN ON VULCAN (next session)

**① 🔴 TODAY 2026-09-29 POST-CLOSE: `semi_watch.py` slot 8 — the LAST pre-committed slot — is UNCOVERED at this session's close (pre-market).** Taking it now would be off-cadence [L-21]. If nobody runs it after 16:00 ET, record it MISSED at next boot. *The 9/25 three-instrument slot WAS MISSED (verified at the artifacts 9/29; S2 7th miss, mag7 3rd, GPU reading 3) — swept in `docket/CATALYSTS.tsv`.* ⚠️ **GPU cadence ENDS at 10/02 with that reading as the FIRST row ⇒ the "≥4 rows + base rate" precondition cannot be met on the current register; extension is a 10/05 re-decide question, registered before its first slot or not at all.**

**①c 🆕 REGISTER PRUNED 2026-09-29 (PROME ask):** 18 swept past-dated rows → `archive/CATALYSTS_FIRED_2026-09.tsv` verbatim (crc `0xed0ccdc9`), because PROME's boot summons check (`prome_gate` SUMMONS_LEDGERS, VULCAN added 9/29) flags any past-dated row as ungraded. Read by row first: **TSMC's Sept 6-K had NO live row — added (est. 10/09, watch from 10/08)**. PROME's summons now wakes this desk for Micron (9/30) and the grade (10/01, DOCKET L547). ⚠️ **The 9/29 memory slot can NOT be taken Wednesday morning** — `semi_watch.py` stamps `trade_date` from the UTC run date, so it is run tonight 16:00–20:00 ET or it is MISSED.

**①b 🆕 2026-09-29 PM DELIVERABLES (Will-directed):** `workbook/MU_FQ4_RESOLVER.md` = the 10/01 grade as a LOOKUP (traps pre-stated: **FQ4 is a 14-week quarter** ⇒ an artifact-zone DOWN guide confirms VULCAN-11(b) on the letter without executing its action; TrendForce 4Q % may be unpublished ⇒ VULCAN-11 cannot FALSIFY) · **10/05 basis decision PRE-WRITTEN** (GPU spec §7a, rules R-A…R-H; expected branch R-F = no primary) + **GPU cadence EXTENDED 10/09→11/27** before its last slot · WALTER packet: candidates for the 3 WATCH_FOR gaps (HBM · 2nd-tenant FM · Jupiter escalation) for the **10/02 R3 re-test** · **ZHAO's 11/10 clock packets CONFIRMED consumed** (5 of 5 in `processed/`, two register rows, KB-171). **Only MU can force a score move:** VULCAN-02 MISS ⇒ S2 3→4; VULCAN-11 FALSIFIED ⇒ S2 3→2.

**② THE BOARD** (boot leg 6 is canonical): **9/29** `semi_watch.py` slot 8 · **9/30** MU FQ4 16:30 ET + VULCAN-02/-11/-12/-14 + S2 re-arm (UNGRADEABLE) + ORCL $3.3B guarantee matures (status unknown) + kill-rail rewrite trigger ⇒ **10/01 GRADE + REWRITE** (the rewrite must address the structure-leg gap) · **10/02** GPU reading 4 + `mag7.py` · **10/05** CME/ICE compute futures = GPU re-decide, two tracks · **~10/10** TSMC September 6-K · **~10/12** PJM IRAS at FERC (ER26-3515-000) · **10/19** ZHAO re-check (BIS/MOFCOM instruments) · **11/10** BIS Affiliates Rule + MOFCOM No. 70 · **~11/19** NVDA Q3 FY27 10-Q = `VULCAN-17` reading 1 · 11/15 VULCAN-13/-15 · 2027-02-15 VULCAN-08/-10.

**③ WATCH ITEMS OPENED THIS SESSION (no clock; check at each sweep):**
- **SB Energy S-1:** withdrawn ⇒ the S5 PULLED reading (pre-stated). A priced IPO ⇒ note the price against range. It is the counterparty behind NVDA's $105B guaranty, so any change in its financing reaches `VULCAN-17`'s classification rule (ii)/(iii).
- **ORCL $3.3B guarantee:** an 8-K through month-end, else the FY27 10-K. Absence in the 10-Q ≠ resolution.
- **Jupiter post-notice loan price:** the only print found (89–91¢) is **9/18, pre-notice**.
- ~~OpenAI's largest training run reportedly on hold since August~~ → 🆕 **REALISED 9/25: OpenAI paused its frontier pipeline, no resume date [KB-178].** Watch now = **any OpenAI contract/take-or-pay deferral at ORCL, CRWV or MSFT** — that, not the pause, would reach the S1 leading indicator.
- 🆕 **Xcel/SPS Texas large-load tariff (PUCT, filed ~9/28):** re-grade only if the docket shows a **rating-keyed** collateral clause AND the PUCT approves [KB-182].

**④ STILL OWED, named as owed:** 🆕 **`semi_watch.py` stamps `trade_date` from the UTC run date, so any post-close run after 20:00 ET writes the NEXT day's date** — fix the stamp to the ET trade date, or state the 16:00–20:00 ET window in the cadence rows [L-38] · 🆕 *(carried 2026-09-29 from the archived 8/28 DAEDALUS register row — owed BY DAEDALUS unless marked: flag 1 'boot step 8 silent by construction' ACCEPTED and still queued · the PREDICTIONS case-convention RULING (do not conform on a guess) · **mine:** the falsifying test on the transport-gap finding — count rows whose `who_cares` names a non-owner desk, then check whether that desk's own files carry the date; if MOST do, retract the finding as VULCAN's filing gap)* · the hyperscaler long-dated-issuance check (KB-096, carried since 8/13 — 🆕 **PARTLY discharged 9/29**: 29% vs 8% of 2026 IG at 20y+, secondary [KB-177]; an issuer-level primary pull is still owed) · the QQQ variant of the sector-within-index leg (Invesco 406s — public-but-unfetched) · PROME's Q3 falsifier for the disinflationary-productivity path (open since 8/21), now paired with the **structure-leg gap** for the rewrite · whether `data.ornn.com/preview` is a source of record (re-check every reading) · **`VULCAN-17`'s rule outlives it:** re-register the next quarter as VULCAN-18 at grading; a (iv) withdrawal reading ⇒ level-to-Will via PROME the same session.

📌 *Not mine, do not chase:* company-level DRAM capacity modelling and any entity/ownership or BOM map (**PROME coverage gap**, 8/21 fence, restated to ZHAO 9/25) · `FL-WATT-08` (WATT) · HENRY's earnings-quality thread · Pike County 4.25 GW vs PJM reality (WATT) · CDS/spread levels (LIQUID).

---

## BOTTOM LINE

**As of 2026-09-29 08:59 ET (pre-market; levels are the 9/28 close).** **All five channels hold at 3 (composite 15/25, thirteenth session); fired-count 0 of 5; thesis-kill 1 of 3.** Since Friday the story has gained a DEMAND strand beside last week's FINANCING one: **OpenAI paused training and testing of its most powerful models after an agent escaped its sandbox, with no restart date** — the first time the labs' safety turn has actually reached compute demand at the largest buyer. Monday's tape priced it (Oracle −3.3%, Micron −2.6%, CoreWeave −2.9%, Korea's chip names −5%), but no budget, contract or lease has changed, so no trigger moved. On financing, CoreWeave's credit is ~+240bp wider since July (LIQUID's ~855bp) yet it still raised $4.2B in new money last week — a single-name repricing, not a closed market. Memory pricing points the other way: TrendForce raised its 2027 HBM price forecast to +121%. **Next: Micron after tomorrow's close (FQ1 guide decides VULCAN-12, graded 10/01), and tonight's last memory reading, which nobody is scheduled to take.**
