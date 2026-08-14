# WINTERKORN — Memory (state)

State file for `WINTERKORN.md` (OTTO docket steward). Read this right after the spec.

**Inaugural state — no prior runs.** First spawn will populate `## LAST RUN`. Seeded sections below give the sub-agent enough bootstrap context to make its first run productive without ambiguity.

---

## CHANGES SINCE LAST RUN

*(diffed vs the 2026-07-04 LAST RUN baseline, at the start of the 2026-07-25 run)*

- **OTTO has been dark 21 days** (last session 2026-07-04). Nothing in the docket was swept in that window.
- **Six rows fired unswept** between Jul 4 and Jul 25: Jul 14 banks, Jul 15 Fitch, Jul 15 MTB, Jul 20 First Brands vote, Jul 21 Ally — **plus a Jul 24 First Brands status conference that was never in the TSV at all** (docket gap; see LAST RUN).
- **The single biggest change: the Tricolor criminal track moved without us.** The Jul 29 hearing that the whole Oct 19 row was gated on became moot on ~Jul 7 — Castel ruled early. The TSV carried a stale Oct 19 2026 trial date for 18 days.
- **First Brands went from "scheduled" to "contested and multiday"** — a privilege fight plus a creditor motion to compel litigation-claim disclosure landed Jul 20, and a status conference was added Jul 24. The Jul 28 date itself never moved.
- CATALYSTS.tsv forward window had thinned to 8 rows with a docket gap at CVNA (no Q2 earnings row) and no EART 2026-4 row despite the NEXT RUN HINTS flag.

---

## LAST RUN

### 2026-07-25 — trigger: on-demand T-3 pre-hearing (Jul 28 First Brands confirmation), after 21-day OTTO dark period

- **🔴 Jul 28 First Brands confirmation — VERIFIED HOLDS.** No adjournment/continuance in any mirror as of 7/25. 9am CT, Judge Lopez, SDTX Courtroom 401, combined with final DS approval `[Law360 2026-07-20; Trucks-Parts-Service; witzamfm 2026-07-01; Octus]`. **New framing captured:** the hearing is **MULTIDAY and CONTESTED** — creditors moved 7/20 to compel more disclosure on the litigation claims anchoring the plan, and Lopez was weighing a privilege question `[Law360 2026-07-20]`.
- **🔴 DATE CORRECTION — Tricolor trial 2026-10-19 → 2027-01-25.** Castel did **not** wait for the Jul 29 hearing: he **granted** Chu's adjournment on/about **2026-07-07**, setting trial **Jan 25 2027 10am** and a **Final Pre-Trial Conference Dec 9 2026 2pm** `[Inner City Press 2026-07-07 contemporaneous SDNY report; corroborated by CourtListener docket 1:25-cr-00579 carrying the Jan 25 2027 date]`. Note the granted date is Jan 25 2027, **not** the Feb 1 2027 placeholder Castel floated 6/29 — a hallucination would have echoed the placeholder. **Stale-vintage trap avoided:** natlawreview (2026-07-06) and Green Street/AFN mirrors still describe "Oct 19 holds, Jul 29 hearing pending" — they pre-date the ruling by one day. Year+day verified on every source.
- **Jul 29 Tricolor row re-framed to SUPERSEDED** (premise resolved early). Row retained, not pruned — whether a Jul 29 conference still sits on Castel's calendar is UNVERIFIED. OTTO to prune or re-purpose.
- **4 fired rows swept for docket facts (all HOLD as docketed, verified against SEC EDGAR 8-K filing dates — primary, not trade press):** JPM/WFC/C all 8-K **2026-07-14**; MTB 8-K **2026-07-15**; ALLY 8-K **2026-07-21**. Zero date drift. Analytical read left to OTTO.
- **Jul 15 Fitch ABS Index — RELEASE UNCONFIRMED, halt-on-ambiguity.** No dated Jul-2026 index release findable in public mirrors (Auto Remarketing's newest indexed piece is 2026-05-21 and *still covers the January index*). Row left unrevised. **Cadence mechanism now confirmed rather than assumed:** index month = collection month + 1 ("January index reading, which covers the December 2025 collection period"), with release lagging further — so the standing "mid-Jul release carries ~May data" note is **correct** and now has a source.
- **Jul 20 First Brands vote — fired, outcome NOT public.** Tallies are not disclosed until the **Jul 27 ballot certification**; no result in any mirror. This is expected, not a gap.
- **5 rows ADDED** (see ROWS ADDED in return block): Jul 24 FB status conference (docket gap — fired unswept, never in TSV), Jul 27 FB ballot certification (promoted out of the Jul 20 row's notes), Jul 29 **CVNA Q2 earnings** (docket gap closed), Aug 17 **EART 2026-4** FWP window (`modeled`), Dec 9 Tricolor FPTC.
- **CVNA Q2 = 2026-07-29 after close, call 5:30pm ET** `[CONF Carvana IR press release via StockTitan + Yahoo Finance]`. Closes the gap OTTO flagged. **Jul 29 is now a triple-event day** (CVNA + the superseded Tricolor row + day 2 of a multiday FB hearing).
- **EART 2026-4: true zero on EDGAR.** SEC full-text search returns **0** filings — and I **positive-controlled** it (2026-2 → 98 hits, 2026-3 → 35 hits incl. FWP 2026-06-10) before banking the gap, per `[[finding_discovery_tool_wrong_slice_false_zero]]`. Added as `modeled` 2026-08-17 from issuer cadence (~2mo spacing), which is **earlier than the standing-monitor "typically Sep"** note.
- **First Brands examiner: no dockable date, but a fired event OTTO may not have.** De Luca filed an **interim** Examiner's Report **2026-04-27** and then **paused the investigation — the $7M budget was exhausted**; he stated ~90 days of further work *if* additional funding is approved. Conditional, no docketed deadline → not added as a row; escalated to OTTO.
- **Baseline audit:** not triggered (on-demand T-3 pre-hearing run; not first-of-month; no OTTO-flagged post-miss).
- **Sources blocked this run:** Kroll direct (403, known auth-gate), CourtListener direct fetch (403 — but its docket content was indexed and readable via search), Green Street News (403).

### 2026-07-04 — trigger: off-cadence forward-docket verification (OTTO-spawned; T-24 pre-Jul-28; after 25-day gap + OTTO's Jul-4 catch-up sweep)
- **Pre-fire verified (web tools loaded):** Jul 28 First Brands confirmation HOLDS (9am CT Lopez, no adjournment; combined w/ final DS; voting deadline Jul 20 6pm ET; ballot-cert/briefs Jul 27) `[Octus/TT/Kroll]`. Ally Jul 21 7:30am ET HOLDS `[Ally PR/8-K]`.
- **Two date corrections found + applied by OTTO:** (a) bank-earnings season-open Jul 15 → **Jul 14** (JPM+WFC+C all Jul 14 `[SEC 8-K/StockTitan]`); (b) MTB Jul 16 → **Jul 15**, `modeled`→`confirmed` `[ir.mtb.com]`. TSV re-sorted.
- **Two new rows added by OTTO:** Jul 20 First Brands creditor-vote deadline (🟡); Jul 29 Tricolor trial-scheduling hearing (🟠 — Castel decides Oct 19 vs Feb 2027).
- **Factual correction flagged + verified by OTTO:** Oct 19 Tricolor trial judge = **Castel**, not Liman (Liman took Dec-2025 cooperator pleas). Propagated across CATALYSTS/STATUS/MEMORY/WINTERKORN spec+memory.
- **PENDING cleared:** all 3 Jun-9 blocks resolved (see PENDING section).
- **Fitch cadence caveat:** index runs ~2mo data lag; a mid-Jul release likely carries ~May data — TSV note softened.
- **Baseline audit:** not triggered (off-cadence pre-fire run, not first-of-month, no post-miss).

### 2026-06-09 — trigger: T-3 pre-hearing (Jun 12 First Brands UST hearing) + inaugural-month baseline audit
- **Pruned:** none (no past-date rows in TSV — Jun 8 refresh already swept the May 13/20/25/29 First Brands rows).
- **Added:** none to TSV directly (baseline-audit deltas are propose-only → see PENDING).
- **Refreshed:** Jun 17 Tricolor row — framing updated from "creditor meeting / trustee distribution plan ETA" to "§341 creditor meeting (continued) / trustee distribution-plan watch"; notes now record Verita-confirmed Jun 17 10am CT AND already-noticed continuation to Nov 11 2026; resolution-at-risk-past-Sep-30 escalated from "modeled likely-slip" to concrete based on Nov 11 continuance.
- **Modeled-date revisions:** Jun 17 Tricolor row `date_class` flipped `modeled → confirmed` — the Jun 17 meeting itself is now docket-locked (Verita); the OTTO-29 resolution-slip risk stays in the notes but the meeting date is no longer a projection. (Old → new: modeled → confirmed; reason: Verita §341 continuance notice published.)
- **Pre-fire verification (load-bearing — 4 rows in 7-trading-day window):**
  - **Jun 12 First Brands UST §1112(b) hearing**: ✅ VERIFIED via Bloomberg (Jun 8 "second chance" article), TT News, Trucks-Parts-Service, Octus. 10am CT, Judge Lopez, multi-source convergence. Lopez explicitly warned he may rule that day. Jun 12 will simultaneously hear the second-chance vote-on-disclosure-statement request — adds upside-resolution path (deny conversion + approve DS = Jun 17 confirmation reopens).
  - **Jun 12 Carvana Discovery Production 2**: ⚠ UNVERIFIED via independent source. STATUS shows "on track"; STATUS is the operative read. Public searches (Delaware Chancery / StockTitan / PRNewswire derivative-litigation feed) did not surface a Jun 12 production-2 docket entry. Halt-on-ambiguity: row left as-is (no date change). Surfaced as ESCALATION below for OTTO awareness.
  - **Jun 17 First Brands plan-confirmation hearing**: ✅ VERIFIED via Kroll cases / Charles M. Moore Decl. — Jun 17 confirmation subject to court availability; voting + objection deadlines Jun 10 (tomorrow). Contingent framing intact (depends on Jun 12 UST denial + DS reset).
  - **Jun 17 Tricolor §341 (continued)**: ✅ VERIFIED via Verita — 10am CT, continued §341, already noticed CONTINUED to Nov 11 2026. Refresh applied (see above).
- **Baseline audit:** **fired** (inaugural run = treat-as-monthly-trigger per spawn brief). Light scope per default convention. Checked recurring-release universe against forward TSV window. **Proposed delta (5 gaps) → mirrored to PENDING for OTTO to accept/decline.**
- **Notes:** Inaugural run uncovered 2 second-order findings worth carrying — (a) Jun 12 hearing also addresses the disclosure-statement second-chance vote, creating a 2-headed outcome that the threshold_signal cell already half-captures ("deny+reset = Jun 17 confirmation path survives") but could be sharpened; (b) Tricolor continuance to Nov 11 implies STATUS CRITICAL TIMELINE may want a Nov 11 row added once the spawn brief's "STATUS sync" propagation runs.

---

## PENDING

OTTO-side decisions / actions queued from prior runs. WINTERKORN adds new items; OTTO clears resolved-by-OTTO ones. WINTERKORN never removes its own entries — that's OTTO's job.

> **✅ ALL 3 JUN-9 PENDING BLOCKS CLEARED 2026-07-04** (OTTO): (1) Carvana Jun-12 prod-2 CALENDAR-AMBIGUITY → confirmed PHANTOM, catalyst retired (WINTERKORN's halt-on-ambiguity was correct); (2) Tricolor Nov-11 + Jun-17 STATUS-SYNC → applied (Nov 11 in TSV+STATUS, Jun 17 swept); (3) 5-delta BASELINE AUDIT → all applied/superseded (Fitch prints, NY Fed Q2, Tricolor Nov 11 all docketed; rating-agency #3 stays DEFERRED in CALIBRATION). **No open PENDING as of Jul 4.** Historical blocks retained below for audit trail.

> **✅ ALL 4 JUL-25 PENDING BLOCKS CLEARED SAME-SESSION 2026-07-25 (OTTO s016).** Dispositions inline under each block below. Summary: (1) PREDICTIONS-SYNC → **no re-dating needed**, no OPEN prediction was gated on the Tricolor trial — but the *absence* was itself the finding, and **OTTO-33 was created** to give the book criminal-track exposure. (2) STATUS-SYNC → **all 5 propagated**. (3) SCOPE/examiner → **was NOT integrated; now integrated**, standing monitor added. (4) CALENDAR-AMBIGUITY → 1 of 3 resolved independently, 2 left unresolved and correctly unrevised. **No open PENDING as of 2026-07-25 close.**

### 2026-08-14 — SCOPE (OTTO-authored, OTTO-executed; recorded here so WINTERKORN inherits the rule) — **do not docket unobservable obligations**

**Finding.** Four rows WINTERKORN inherited from OTTO's s017 close (`2026-08-05` Rule 17 subpoena deadline, `2026-08-07` defense privilege log, plus the 8/14 gov't-exemplar and 8/21 defense-submission steps carried inside that row's notes) were keyed to **party-to-party discovery obligations that structurally cannot produce a docket entry.** All swept **empty** on 2026-08-14 — `[CONF CourtListener docket_id 72046761: ZERO entries 2026-08-01..08-14, latest is Dkt 116 (7/30)]`.

**Why they can never fire usefully.** Rule 17 subpoena applications are routinely **ex parte and/or sealed**, and *serving* a subpoena requires no docket entry at all. Privilege logs are **exchanged between counsel and are never filed**. So the row's "what_to_check" was unanswerable through the only channel OTTO has.

**Executed by OTTO this session (no WINTERKORN action required):** the chain was collapsed into **one row at a modeled `2026-09-04`** keyed to the *first DOCKETED output* — an in camera submission, motion to compel, privilege dispute, or an order resolving one. The `2026-08-05` row is annotated and **deliberately NOT re-armed on a date.**

**STANDING RULE FOR FUTURE RUNS — apply at row-creation time, not at fire time:** before docketing any deadline, ask *"what artifact does this obligation produce, and does it land in a channel WINTERKORN can read?"* If the answer is a private exchange, **key the row to the first observable downstream artifact instead.** This is the same halt-on-ambiguity instinct WINTERKORN already applies to dates, extended from *"is the date right?"* to *"is the EVENT visible?"*. ⚠ **Corollary, and it matters for grading:** on rows of this class, **absence of a docket entry is NOT evidence of absence** — never report one as a negative finding.

### 2026-07-25 — PREDICTIONS-SYNC: Tricolor trial adjournment may move an OTTO-NN resolver
- Oct 19 2026 → **Jan 25 2027** (verified; see LAST RUN). Any OPEN prediction whose resolver leans on the Tricolor criminal trial as a fraud-surface-expansion catalyst now resolves **~3 months later, and outside 2026**. WINTERKORN does not edit PREDICTIONS. **Suggested resolution:** OTTO re-check the PREDICTIONS ledger for rows gated on the trial and re-date / re-arm-with-reason. Also check the Dec 31 year-end cluster (OTTO-07/-11/-12/-31) — if any of those leaned on trial-driven disclosure, the mechanism just slipped past the resolve date.
- **✅ OTTO DISPOSITION 2026-07-25 — checked, no re-dating required, but the check found something better.** Audited all 10 then-OPEN rows incl. the Dec-31 cluster: **none is gated on the Tricolor criminal trial.** The only `trial`/`criminal` string in the ledger is in OTTO-32's notes and refers to the *James* criminal case staying the *First Brands* civil suits — a different case. So the adjournment moves no resolver. **The real finding is the absence:** OTTO's prediction book had **zero exposure to the criminal track**, which this same session produced the strongest thesis validation of the year from (superseding §225 indictment charging both OTTO mechanisms + cooperating COO). **Action taken: created OTTO-33** (new corporate counterparty publicly implicated by Dec 31, 60%), with its discovery instrument named in-row. **Good escalation — it was right to raise even though the literal answer was "nothing to re-date."**

### 2026-07-25 — STATUS-SYNC: five propagations to CRITICAL TIMELINE
- Per TRUTH MODEL §3 these all fall inside the curated load-bearing subset. **Suggested resolution:** OTTO propagates at closeout. (a) **Tricolor trial Oct 19 2026 → Jan 25 2027** — a 🟠 tracked-case date change that leaves 2026 entirely; STATUS almost certainly still shows Oct 19. (b) **Dec 9 2026 Tricolor FPTC** — new tracked-case hearing. (c) **Jul 29 CVNA Q2 earnings** — new row on a tracked cockroach name. (d) **Jul 24 FB status conference + Jul 27 ballot certification** — new First Brands cluster rows. (e) **Jul 28 FB hearing re-framed** multiday/contested. Note (a) is the highest-risk divergence: a stale Oct 19 in STATUS is exactly the silent-drift class.
- **✅ OTTO DISPOSITION 2026-07-25 — all 5 propagated to STATUS CRITICAL TIMELINE.** (a) Oct 19 row struck through → Jan 25 2027, Chu-only, with the "catalyst has left 2026" consequence stated (you were right that STATUS still showed Oct 19 — 18 days stale); (b) Dec 9 FPTC row added; (c) Jul 29 CVNA row added + ACTIVE VECTORS Carvana section rewritten around the earnings/short-seller window; (d) Jul 24 + Jul 27 rows added, Jul 24 carrying your single-source caveat verbatim; (e) Jul 28 row re-framed to "hearing OPENS… MULTIDAY + CONTESTED… expect process, not resolution," and OTTO-32's PREDICTIONS notes given a matching resolution-mechanics reframe so the ledger and the timeline agree.

### 2026-07-25 — SCOPE: First Brands examiner report — fired interim report + a stalled investigation
- De Luca filed an **interim** Examiner's Report **2026-04-27** finding receivables "fabricated, repeatedly pledged, or never transferred as represented," naming CFO Stephen Graham and VP Finance Peter Andrew Brumbergs. Investigation is **paused — $7M budget exhausted**; ~90 days more work offered *if* funded. **No docketed report deadline exists**, so no TSV row was added (halt-on-ambiguity + no-fixed-date scope rule). **Suggested resolution:** OTTO decides (i) whether the Apr 27 interim report is already integrated into the thesis/fraud surface — if not, this is a live unintegrated primary; (ii) whether to add a standing monitor for a budget-increase motion, which is what would create a dockable follow-on report date.
- **✅ OTTO DISPOSITION 2026-07-25 — (i) NOT integrated; now integrated. (ii) standing monitor: YES.** OTTO's records had only "appointed Nov 19 2025, $7M budget, work plan approved Jan 2026, no public report-deadline yet" — the Apr 27 interim report was a genuine 3-month-old unintegrated primary. Added to STATUS CRITICAL TIMELINE with the corroborated finding (James ran the entities *"not as a for-profit business, but as a liquidity generating and value extracting enterprise"*). **Your judgment not to add a TSV row was correct** — no docketed deadline exists, so there is nothing to count down to; a standing monitor on the budget-increase motion is the right instrument and is now added.
- **⚠ ONE CLAIM NOT PROPAGATED — corroboration failed.** You reported the interim report as *"naming CFO Stephen Graham and VP Finance Peter Andrew Brumbergs."* Independent search confirmed the report, the Apr 27 date, the budget exhaustion, the ~90-day offer, and the "value extracting enterprise" language — **but returned nothing on either individual.** Naming individuals is a high-consequence claim, so OTTO applied its own `[ALLEG]`/corroboration bar and **left both names out of every OTTO surface.** Not a ding on the run — everything else you reported corroborated cleanly, and the report itself was a real find. **Convention going forward: when a report names natural persons, cite the specific document/paragraph, or flag the names separately as single-source so OTTO can gate them.**

### 2026-07-25 — CALENDAR-AMBIGUITY: three items I could not independently confirm (rows left unrevised)
- (a) **Jul 15 Fitch Auto ABS Index release** — no dated Jul-2026 release findable; newest public mirror (2026-05-21) still covers the January index. Row left `modeled` at Jul 15. OTTO may have Fitch direct access WINTERKORN lacks. (b) **Jul 24 First Brands status conference** — added as a row but **single-source (Kroll case calendar via search mirror; direct fetch 403)**; two independent search calls returned identical detail (1:30pm CT, Ct 401, 515 Rusk St), but that is one underlying source, not two. OTTO to confirm it occurred and what came of it. (c) **Whether a Jul 29 Castel conference still exists** — pre-adjournment reporting referenced Jul 29 (and an Aug 6) conference; the Jul 7 order supersedes the Jul 29 *purpose* but I could not confirm cancellation. Row kept and marked SUPERSEDED rather than deleted.
- **✅ OTTO DISPOSITION 2026-07-25 — 1 of 3 resolved, 2 correctly left alone.** (a) **Fitch — RESOLVED, and you were right.** OTTO has no Fitch-direct access either; an independent sweep confirms the newest available data is still **March 2026** (60+ DQ 6.11% / ANL 8.80% / recovery 37.48%). The Jul 15 row fired and produced **no new data**. Swept in STATUS as "FIRED — NO NEW DATA," and the consequence recorded: **OTTO-04's key input is now 4 months stale by data-month and the summer re-deterioration remains unobserved.** Your confirmation of the index-month/collection-month mechanism is a genuine upgrade — the lag is now sourced, not assumed. (b) **Jul 24 status conference — left as you filed it**, single-source caveat carried verbatim into STATUS rather than laundered into a clean row. Outcome still unknown. (c) **Jul 29 Castel conference — left SUPERSEDED, not deleted.** Correct call: independent reporting confirms Castel granted the adjournment ~Jul 7 to **Jan 25 2027** while the Jul 29 date's *purpose* evaporated, and separately shows Jul 29 referenced as where the date "may be confirmed" — so the hearing plausibly survives with a changed purpose. **Deleting it would have destroyed a live node; halting was right.**

### 2026-06-09 — CALENDAR-AMBIGUITY: Jun 12 Carvana Discovery Production 2 unverifiable from public sources
- WINTERKORN searches (Delaware Chancery / StockTitan / PRNewswire / general derivative-litigation press) did not return a confirming source for a Jun 12 production-2 docket entry. STATUS still shows "T-4, on track" — STATUS is the operative read. **Halt-on-ambiguity:** row left at Jun 12, not revised. **Suggested resolution:** OTTO confirm via direct Chancery docket access or the derivative-action coordinator before Jun 12; if undated, re-class as `modeled` with a target window. No action required if STATUS is correct.

### 2026-06-09 — STATUS-SYNC: Tricolor Nov 11 continuance + Jun 17 framing refresh propagation
- Verita-confirmed §341 continuance to Nov 11 2026 (after Jun 17). STATUS CRITICAL TIMELINE row currently reads "Jun 17 Tricolor creditor meeting — trustee distribution plan ETA / ⚠️ AT RISK / likely SLIP." **Suggested resolution:** OTTO at closeout: (a) update the Jun 17 STATUS row framing to match the refreshed TSV (continued §341, distribution-plan watch); (b) add a Nov 11 row to STATUS CRITICAL TIMELINE (and to CATALYSTS.tsv if OTTO judges it load-bearing). OTTO-29 substance unchanged — resolution-slip risk past Sep 30 now concrete rather than modeled.

### 2026-06-09 — BASELINE AUDIT (inaugural-month): 5 proposed delta rows for OTTO accept/decline
Light scope per default convention. Per-case dockets get full forward; rolling monthly releases get next-2.

1. **2026-06-15 (approx) — Fitch Auto ABS Index, May 2026 print** — 🟠 — OTTO,CARL — `confirmed` — Monthly Fitch ABS Index (60+ DQ / recovery / ANL). Most recent cited in MEMORY-STANDING-MONITORS is Jan 2026; Feb/Mar/Apr/May prints have been releasing on a monthly cadence and should be tracked given OTTO-04 trajectory. Suggested rationale: missing this means OTTO-04 monthly-burn tracking can drift. **Source:** Fitch direct + Auto Finance News.
2. **2026-07-15 (approx) — Fitch Auto ABS Index, Jun 2026 print** — 🟠 — OTTO,CARL — `confirmed` — Next-2 rolling monthly per default convention. Same rationale.
3. **2026-06-?? (mid-month) — S&P + KBRA + Moody's ABS surveillance May data** — 🟠 — OTTO,REGINALD — `modeled` — Rating-agency monthly surveillance is on-event + monthly; the on-event additions (CreditWatch placements / ECNL revisions) feed OTTO-04 and the Lender Watchlist directly. Suggested rationale: ratings-agency framing is currently inferred via secondary sources (Auto Finance News); a direct row keeps the cadence honest.
4. ✅ **CLOSED 2026-08-14 — NY Fed Q2 2026 Household Debt & Credit PUBLISHED Tue Aug 11 and swept by OTTO.** Row pinned 08-06-modeled → **08-11-actual**. **Q2: auto $1.713T (+1.66% QoQ, ATH) / transition-to-90+ 3.0028%** — supersedes the Q1 figures this item carried ($1.685T / 2.97%, published May 12). **Calibration for the next cadence call: the 08-04..08-11 WINDOW was correct and the 08-06 midpoint PIN was 5 days early — keep this row's date_class as a window, do not collapse it to a midpoint.** Method note for future runs: the data workbook is reachable at the standard media-library path (`HHD_C_Report_2026Q2.xlsx`) independent of any news page, so probe the file directly rather than waiting for a press release to be indexed.
5. **2026-11-11 — Tricolor §341 (continued) further continuance** — 🔴 — OTTO,REGINALD — `confirmed` — Already known per Verita continuance notice; Tricolor distribution-plan resolution slipping past Sep 30 OTTO-29 resolve makes this the next-canonical observation point. Suggested rationale: this date NOW exists in the docket — adding it keeps the case-tracking forward-window correct.

Plus 1 NOT proposed (per scope convention): **ABS new-issue pricing windows (EART Q3 / Bridgecrest / GCAR modeled rows)** — Standing Monitor flags EART Q3 typically Sep; close enough to Sep 30 OTTO-04 resolve that the modeled-pricing row would be informative, but ABS pricing dates are projectable + revise on SEC EDGAR FWP within ~7d. WINTERKORN defers proposing until ~T-30 of the pricing window per standard convention. No action needed.

**Bank earnings (Tricolor-named subset: JPM, 5-3, BCS, Regions, MTB, OBK):** TSV already carries the Jul 15 cycle-open row + Jul 16 MTB row. No bank-earnings additions proposed this audit — current TSV coverage adequate for OTTO-30 forward-discovery scope. Next bank-earnings additions would be Q3 cycle (Oct-Nov), too far forward this audit.

Future format for new PENDING items:
```
### YYYY-MM-DD — [category: SCOPE / DATE-ESCALATION / STATUS-SYNC / PREDICTIONS-SYNC / CALENDAR-AMBIGUITY]
- [one-line description + source + suggested resolution]
```

---

## STANDING MONITORS

Recurring watches WINTERKORN should re-verify every run regardless of pre-fire window. These are the rows where source-of-truth is known to drift / be blocked.

### Per-case dockets (verify weekly during active hearing cycles)
- **First Brands docket (S.D. Tex., Judge Lopez)** — Highest-activity case. Hearing calendar revises frequently; UST motions + DS denials cascade. Re-verify all First Brands rows every run. Sources: Kroll (auth-gated → news mirrors), Law360, Octus, CreditSights, Trucks-Parts-Service.
- **Tricolor Ch.7 docket (Verita, Judge Burns)** — Verita cert-verification failure is known and recurring; primary source routinely blocks. Fallback sources: Bloomberg Law, Green Street News, Auto Finance News. Halt-on-ambiguity if all secondary sources are silent.
- **Tricolor SDNY criminal (Chu, Judge Castel)** — Selective scope: trial date + cooperator motions only. **Trial is now 2027-01-25 10am** (adjourned from Oct 19 2026 by Castel's ~2026-07-07 order); **Final Pre-Trial Conference 2026-12-09 2pm**. Co-defendant **Goodgame pleaded guilty 2026-06-24** — the trial track is now Chu-centric. Re-verify monthly until ~T-30 of the FPTC, then weekly. (Liman handled the Dec-2025 cooperator pleas — do not attribute the trial to Liman.) **Best source by far: Inner City Press** (`innercitypress.com`, contemporaneous SDNY reporting) — it carried the adjournment a day before the trade press, which was still printing "Oct 19 holds." CourtListener docket **1:25-cr-00579** is the corroborating primary (403s on direct fetch; readable via search index).
- **Carvana derivative / discovery (DE Chancery)** — Verify production milestone dates from StockTitan / PRNewswire / direct Chancery filings.

### Recurring releases (monthly cadence; verify forward two)
- **Fitch Auto ABS Index** — Jan-2026 baseline 60+ DQ 6.90% / recovery 32.64% / ANL 9.81%; spring tax-refund bounce lifted the series (60+ DQ ~6.1%, ANL ~8.8%, recovery 37.48% `[PRESS]`). **~2mo data lag** — a mid-month release carries ~2-months-prior data; don't over-read print freshness. Monthly cadence. Source: Fitch direct + Auto Finance News.
- **NY Fed HDC (Quarterly)** — Q1 2026 released May 12. Q2 2026 due ~Aug. Source: newyorkfed.org.
- **S&P / KBRA / Moody's ABS surveillance** — Monthly + on-event. Watch for ECNL revisions, CreditWatch placements, downgrade waves.

### Bank-earnings cycle (named-banks subset only)
- Q2 2026 earnings cycle opens ~Jul 15 (JPM, WFC, C lead). Named-banks: **JPM, 5-3, BCS, Regions, MTB, OBK**. Source: SEC EDGAR + IR calendars.

### ABS pricing windows (modeled rows)
- **EART 2026-4** — **"typically Sep" is wrong for this cycle.** Verified cadence 2026-07-25: 2026-1 FWP Jan 21 → 2026-2 (8-K Mar 24) → 2026-3 FWP Jun 10, priced ~Jun 24. ~2-month spacing puts 2026-4 in **mid-to-late Aug**. TSV carries a `modeled` 2026-08-17 row. EDGAR full-text search showed **0 EART 2026-4 filings as of 7/25** (positive-controlled). Revise the row the moment an FWP appears. Query recipe: `efts.sec.gov/LATEST/search-index?q="Exeter Automobile Receivables Trust 2026-4"` with a UA header.
- **Bridgecrest** — Carvana-related; quarterly. Watch for related-party pricing dynamics.
- **GCAR / smaller stressed shelves (CPS, Flagship, Lendbuzz, SAFCO)** — Watch for shelf-halt signal (OTTO-07).

### TRADE.md position expiries
- ✅ **TRADE.md is FROZEN as of 2026-07-04** (corrected 2026-07-25 — this line previously said "rehab-pending," which was stale by three weeks). OTTO holds **no position**. **Do not add position-expiry rows at all** while frozen — there are no positions to expire. If TRADE.md is ever unfrozen, revert to cross-verifying against FORGE before docketing any expiry.

---

## CALIBRATION

**OTTO-owned section. WINTERKORN reads but never writes here.** OTTO records:
1. **Declined release classes** — what OTTO decided isn't worth tracking under the current thesis lens (with date + reason). WINTERKORN excludes these from baseline-audit proposals.
2. **Accepted-as-proposed examples** — patterns WINTERKORN should keep proposing.
3. **Calibration notes** — anything OTTO wants future-WINTERKORN to know about scope decisions.

### Declined release classes

- **[2026-06-09] Direct rating-agency monthly surveillance row (S&P + KBRA + Moody's, baseline-audit proposal #3)** — DEFERRED-NOT-DECLINED. Auto Finance News mirror already captures on-event additions (CreditWatch placements, ECNL revisions) and feeds the Lender Watchlist directly. A standalone TSV row for "May data mid-month" was too fuzzy on threshold_signal to be action-forcing. **Re-propose ONLY if** OTTO experiences a specific issuer-level event (Exeter, CPS, Flagship, Lendbuzz, SAFCO) where direct rating-agency tracking would have caught it earlier than Auto Finance News did. Default lens: leave as Auto Finance News mirror.

### Accepted (Jun 9 inaugural baseline-audit deltas, for future-WINTERKORN pattern reference)

- **Fitch Auto ABS Index monthly** (proposal #1 + #2) — ACCEPTED with `modeled` date_class (typically mid-month; revise within 7d via Fitch direct). Drives OTTO-04 trajectory; rolling next-2 keeps the burn-rate honest. Pattern: keep proposing monthly Fitch ABS Index rows on rolling next-2 cadence.
- **NY Fed Quarterly HDC** (proposal #4) — ACCEPTED with `modeled` date_class. Canonical aggregate-auto read; missing it would silently drop a quarterly check on the Invisible Exit divergence (consumer-flow vs ABS-stress). Pattern: keep proposing each quarter ~14 days out from expected release (Feb/May/Aug/Nov).
- **Tricolor §341 Nov 11 2026 continuance** (proposal #5) — ACCEPTED with `confirmed` date_class (Verita-noticed). Pattern: when WINTERKORN finds a docket-noticed continuance during pre-fire verification, propose adding the continuance date directly — it's a verified-source-of-truth gain.

### Accepted (Jul 25 run — all 5 added rows ACCEPTED as filed)

- **Jul 24 FB status conference / Jul 27 ballot certification / Jul 29 CVNA Q2 / Aug 17 EART 2026-4 (`modeled`) / Dec 9 Tricolor FPTC** — all five accepted, none revised. Two patterns to keep repeating: **(a) promoting a sub-deadline out of another row's notes into its own row** (Jul 27 ballot cert was buried in the Jul 20 row and is the node where the vote tallies actually become public); **(b) positive-controlling a zero before banking it** — the EART 2026-4 "0 EDGAR hits" was checked against 2026-2 (98 hits) and 2026-3 (35 hits) first. That is exactly right and should be the standing habit for every negative.

### ⚠ SCOPE CHANGE — criminal track is a DISCOVERY channel, not a date-keeping row (OTTO ruling, 2026-07-25)

**This is the most important calibration entry to date. Read it before any run.**

The spec scoped the Tricolor SDNY criminal case as *"Selective scope: trial date Oct 19 2026 + cooperator motions only… re-verify monthly until ~T-30, then weekly."* Under that scoping, **four material events were missed for up to a month**, and OTTO missed them too:

| Date | Event | Why the narrow scope missed it |
|---|---|---|
| Jun 24 | **Superseding 8-count indictment** vs Chu invoking §225 "financial kingpin" (10yr-life min) | Not a trial date, not a cooperator motion |
| Jun 24 | **COO Goodgame pleads GUILTY + cooperates** (flip from Jan not-guilty) | Arguably in scope, but framed as "motions," not pleas |
| Jun 30 | Chu arraigned, pleads not guilty | Not a trial date |
| Jul 7 | Trial adjourned Oct 19 → **Jan 25 2027** | ✅ *This* one was in scope and you caught it |

The narrow scope caught **1 of 4** — and the three it missed included **the strongest thesis validation OTTO has ever received**: the indictment charges *"manipulated delinquent loan data to make non-performing loans appear current"* (OTTO's Invisible Exit) **and** *"pledged the same collateral to multiple lenders simultaneously"* (OTTO's Cockroach). OTTO had been treating both as its own inferences.

**Ruling — the criminal docket is re-scoped from date-keeping to full fraud-surface discovery.** Every run, report:
1. **Charging documents** — new/superseding indictments, statutes invoked, count changes. *Statute choice is signal*: a dormant mandatory-minimum statute is a revealed read on evidence strength.
2. **Pleas and cooperation** — any defendant flipping. Cooperators expand named participants; this fires an OTTO standing outbound trigger (→ CARL, REGINALD).
3. **Newly named entities or individuals** — flag them, and **flag them as single-source if that's what they are** (see the examiner-names disposition above).
4. **Alleged-conduct language**, quoted. The specific phrasing is what maps to OTTO's mechanisms; a summary ("fraud charges") destroys exactly the information OTTO needs.
5. **Scope-of-period allegations** — "continuing enterprise from at least 2018" widened OTTO's impaired-vintage window by four years in one clause.

Same re-scoping applies to the **First Brands criminal track (US v. Patrick James)** and to **examiner/trustee reports in both cases** — the Apr 27 examiner interim report sat unintegrated for three months under the old scoping.

**Cost note:** this is a real scope expansion. Prefer it done *well on the two live criminal matters* over thinly across everything; if it forces a trade-off, drop ABS-pricing-window verification first (lowest yield to date).

### ⚠ RULING — Fitch Auto ABS Index: OTTO has NO Fitch-direct access; row stays `modeled`, and the gap is now a named thesis risk (OTTO, 2026-07-25)

You escalated this after two consecutive runs of unverifiable Fitch rows. **Answer: OTTO does not have Fitch-direct access either.** OTTO's Fitch figures have always come through the Auto Remarketing / Auto Finance News secondary mirror, and that mirror has gone stale — its newest indexed piece (2026-05-21) still covers the **January** index.

**Rulings:**
1. **The row stays `modeled` indefinitely.** Do not flip it to `confirmed` on a cadence assumption. Keep verifying; keep halting when it can't be verified. Two halts in a row was the correct behaviour, not a failure.
2. **Report the *absence* explicitly each run** — "fired, no new data" is a finding, not a null result. OTTO swept the Jul 15 row that way. **Never let a missing print read as an unchanged series**; the risk is inferring stability from silence.
3. **Your cadence confirmation is now the canonical statement of the lag** (index month = collection month + 1, release lagging further). That upgraded an assumption to a sourced mechanism — keep it in STANDING MONITORS.

**Why this matters beyond docket hygiene, so the next run understands the stakes:** the Fitch blended index is the **resolution metric for OTTO-04** (2022-vintage CNL >25% by Sep 30) and the primary instrument for the summer-re-deterioration watch. Latest available data is **March 2026** — meaning OTTO enters the Sep 30 resolve with an input that is **four months stale by data-month** and a re-deterioration thesis that is **unobserved, not disconfirmed**. This is a structural single-source dependency on a paywalled series reached through a decaying free mirror. **Flagged to OTTO's own follow-up queue** as a measure-design problem of the same family as OTTO-30 (see CHANGELOG 2026-07-25) — the thesis leans on a number OTTO cannot reliably obtain.

### 📋 TESTED 2026-07-25 — free-source alternatives to Fitch: S&P DEAD, KBRA PARTIAL (do not re-run these checks)

Will asked whether the Fitch gap could be closed from another source. All candidates tested the same day; **record kept so nobody re-litigates it.**

| Source | Verdict | Detail |
|---|---|---|
| **S&P Global — U.S. Auto Loan ABS Tracker** | ❌ **DEAD** | Monthly, published through May-2026, but the article URL returns **HTTP 403 Forbidden**. Authentication required. |
| **KBRA — U.S. Auto Loan ABS Indices spreadsheet** | ❌ **PAID** | The `/indices` hub links a full data spreadsheet (maintained — stamped 15 Jul 2026), but it returns a gate: *"This report requires an ABS Premium Subscription"* (`userHasABSAccess: false`). |
| **KBRA — monthly publication free preview** | ⚠️ **PARTIAL — genuinely useful** | Free text carries **MoM changes in bps**, **separated prime vs non-prime**, at a **~2.5-week lag** (May-2026 data published Jun 17). Absolute levels appear only occasionally (Jan-2026 non-prime ANL **10.9%**). |
| **Fitch via Auto Remarketing / AFN mirror** | ❌ **DECAYED** | Newest indexed piece 2026-05-21, still covering the *January* index. |

**Two things KBRA gives that Fitch never did:** it is **~2 months fresher** (May vs March data), and it is **tier-separated** — prime and non-prime as distinct indices, rather than the single blend whose composition bias broke OTTO-04.

**Use it as a directional supplement, with two hard rules:**
1. **NEVER splice KBRA's non-prime index onto Fitch's subprime index.** Differently constructed universes. Splicing them is precisely the composition error that broke OTTO-04 — a level shift would read as a market move.
2. **Chained levels are fragile.** An anchor (Jan-2026 non-prime ANL 10.9%) plus MoM deltas reconstructs a series, but error accumulates, deltas may be quoted against revised bases, and the **April-2026 report did not surface** — so the chain already has a hole. Report chained values as `[EST]`, never `[CONF]`, and re-anchor whenever a free preview happens to state a level.

**Conclusion: the paid aggregators are closed, so the fix is to own the instrument.** Build the 10-D panel — same underlying data the agencies use, free, primary-source, tier-separable by construction. Scoped in MEMORY § NEXT SESSION.

### Calibration notes

- **Inaugural calibration (Jun 9 2026):** 5 baseline-audit proposals → 4 accepted, 1 deferred-not-declined. WINTERKORN's instinct on per-case docket vs recurring-release scope was sound. The one defer was on a class where OTTO already has a working mirror (Auto Finance News for rating-agency surveillance); reflects "don't duplicate an existing pipeline" lens.
- **Date-classification pattern:** Fitch ABS Index rows and NY Fed HDC rows go in as `modeled` (release dates approximate); a docket-noticed continuance like Tricolor Nov 11 goes in as `confirmed` (court-issued). Use this split going forward.
- **Carvana ambiguity is a true PENDING, not a defer.** WINTERKORN's halt-on-ambiguity on the Jun 12 Carvana row was correct — OTTO has direct Chancery access for Carvana derivative track that WINTERKORN doesn't. Don't propose changing the row class unless OTTO updates the calibration.

---

## NEXT RUN HINTS

Notes from the most recent run for the next-WINTERKORN to read first. Captures one-off context that doesn't fit in STANDING MONITORS but matters for the next sync.

### Hints for next run (carried from 2026-07-25)

**🔴 Sweep the Jul 28 First Brands confirmation outcome first — it is the operative OTTO-32 resolver.** Verified HOLDS as of 7/25 with no adjournment. But it is **multiday and contested**, so "what happened on the 28th" may not be the whole answer — check whether the hearing ran into Jul 29/30 and whether Lopez ruled from the bench or took it under advisement. Sequence to read in order: **Jul 27 ballot certification** (first public read on the Jul 20 vote — impaired-class rejection ⇒ cramdown fight) → **Jul 28+ hearing**. Plan confirmed = OTTO-32 CONFIRMED well inside Sep 30. Sources: Law360, Octus, Trucks-Parts-Service, Kroll-via-mirror.

**🔴 Do NOT re-verify the Tricolor Jul 29 hearing as a decision gate — it is dead.** Castel granted the adjournment ~Jul 7. Trial is **2027-01-25**, FPTC **2026-12-09**. The Jul 29 TSV row is marked SUPERSEDED and is awaiting OTTO's prune-or-repurpose call — **if OTTO hasn't cleared it, propose deleting it.** Next real Tricolor criminal checkpoint is the Dec 9 FPTC; re-verify monthly, weekly from ~Nov 9.

**🟠 Jul 29 CVNA Q2 earnings — the first sweep target of the next run.** After close, call 5:30pm ET. **Short-seller protocol is live** (root CLAUDE.md § Short-Seller Report Monitoring): Gotham has covered CVNA before and dropped its report *on earnings day* — the Feb 18 2026 lesson. If OTTO has any CVNA position, the T-7 scan was due 7/22 and is now late.

**Jul 24 First Brands status conference — outcome unknown.** Added as a row from a single Kroll-mirror source; confirm it occurred and what came of the privilege/discovery fight.

**Fitch Auto ABS Index — the public mirror has gone stale and this is now a recurring problem.** Auto Remarketing's newest indexed piece (2026-05-21) still covers the *January* index. Two runs in a row the Fitch row has been unverifiable from public sources. **Consider escalating to OTTO whether this row should be `modeled` indefinitely or whether OTTO has Fitch-direct access.** Cadence confirmed and unchanged: index month = collection month + 1, release lags further ⇒ a mid-month release carries ~2-month-old data. Don't over-read print freshness.

**EART 2026-4 — check EDGAR first thing.** `modeled` at 2026-08-17; zero filings as of 7/25 (positive-controlled). Cadence says mid-to-late Aug, **earlier than the old "typically Sep" note** — that note is now corrected in STANDING MONITORS. Revise the row on FWP appearance.

**First Brands examiner — the interesting thread is the *budget*, not a report date.** De Luca's interim report landed 2026-04-27; investigation then **paused for lack of funds**. There is no deadline to dock. What *would* create one is a motion to increase the $7M budget — watch for that, and it produces a ~90-day report clock if granted.

**Baseline audit is DUE next run if it's the first run of August.** Read CALIBRATION first: rating-agency direct surveillance stays DEFERRED (Auto Finance News mirror covers it). NY Fed Q2 HDC (Aug 12-15) is already docketed.

**4 open PENDING blocks from this run** (PREDICTIONS-SYNC on the trial re-date, STATUS-SYNC ×5 propagations, SCOPE on the examiner, CALENDAR-AMBIGUITY ×3). Do not remove them — OTTO clears.

**Method note worth keeping: primary beat trade press by a full news cycle twice this run.** SEC EDGAR 8-K filing dates settled all four earnings rows instantly and unambiguously; Inner City Press carried the Tricolor adjournment while natlawreview (Jul 6) and the Green Street/AFN mirrors were still printing "Oct 19 holds, Jul 29 hearing pending." When a trade-press date and a docket/filing date disagree, the filing wins — and check the *year and day* on the article before believing it.

### Standing context (durable)

- **Pre-fire date verification is the load-bearing job step.** OTTO's Jun-8 catch (First Brands Jun-17 → Jun-12) is the canonical failure mode this sub-agent exists to prevent.
- **Verita Global cert issue is known and recurring.** Halt-on-ambiguity convention applies to all Tricolor Ch.7 docket fetches.
- **First Brands is the highest-activity case.** Re-verify weekly.
- **TRADE.md is FROZEN (2026-07-04), OTTO holds no position.** Skip position-expiry additions entirely.
- **Spawn cadence:** weekly Tue + on-demand T-3 pre-hearing. Outside that cadence, spawn cost > value.
