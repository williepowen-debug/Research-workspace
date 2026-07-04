# WINTERKORN — Memory (state)

State file for `WINTERKORN.md` (OTTO docket steward). Read this right after the spec.

**Inaugural state — no prior runs.** First spawn will populate `## LAST RUN`. Seeded sections below give the sub-agent enough bootstrap context to make its first run productive without ambiguity.

---

## CHANGES SINCE LAST RUN

*(inaugural — no prior run baseline. Read the full read-set fresh.)*

Future runs populate this at start by diffing read-set vs prior `## LAST RUN` timestamp.

---

## LAST RUN

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

### 2026-06-09 — CALENDAR-AMBIGUITY: Jun 12 Carvana Discovery Production 2 unverifiable from public sources
- WINTERKORN searches (Delaware Chancery / StockTitan / PRNewswire / general derivative-litigation press) did not return a confirming source for a Jun 12 production-2 docket entry. STATUS still shows "T-4, on track" — STATUS is the operative read. **Halt-on-ambiguity:** row left at Jun 12, not revised. **Suggested resolution:** OTTO confirm via direct Chancery docket access or the derivative-action coordinator before Jun 12; if undated, re-class as `modeled` with a target window. No action required if STATUS is correct.

### 2026-06-09 — STATUS-SYNC: Tricolor Nov 11 continuance + Jun 17 framing refresh propagation
- Verita-confirmed §341 continuance to Nov 11 2026 (after Jun 17). STATUS CRITICAL TIMELINE row currently reads "Jun 17 Tricolor creditor meeting — trustee distribution plan ETA / ⚠️ AT RISK / likely SLIP." **Suggested resolution:** OTTO at closeout: (a) update the Jun 17 STATUS row framing to match the refreshed TSV (continued §341, distribution-plan watch); (b) add a Nov 11 row to STATUS CRITICAL TIMELINE (and to CATALYSTS.tsv if OTTO judges it load-bearing). OTTO-29 substance unchanged — resolution-slip risk past Sep 30 now concrete rather than modeled.

### 2026-06-09 — BASELINE AUDIT (inaugural-month): 5 proposed delta rows for OTTO accept/decline
Light scope per default convention. Per-case dockets get full forward; rolling monthly releases get next-2.

1. **2026-06-15 (approx) — Fitch Auto ABS Index, May 2026 print** — 🟠 — OTTO,CARL — `confirmed` — Monthly Fitch ABS Index (60+ DQ / recovery / ANL). Most recent cited in MEMORY-STANDING-MONITORS is Jan 2026; Feb/Mar/Apr/May prints have been releasing on a monthly cadence and should be tracked given OTTO-04 trajectory. Suggested rationale: missing this means OTTO-04 monthly-burn tracking can drift. **Source:** Fitch direct + Auto Finance News.
2. **2026-07-15 (approx) — Fitch Auto ABS Index, Jun 2026 print** — 🟠 — OTTO,CARL — `confirmed` — Next-2 rolling monthly per default convention. Same rationale.
3. **2026-06-?? (mid-month) — S&P + KBRA + Moody's ABS surveillance May data** — 🟠 — OTTO,REGINALD — `modeled` — Rating-agency monthly surveillance is on-event + monthly; the on-event additions (CreditWatch placements / ECNL revisions) feed OTTO-04 and the Lender Watchlist directly. Suggested rationale: ratings-agency framing is currently inferred via secondary sources (Auto Finance News); a direct row keeps the cadence honest.
4. **2026-08-?? (mid-month) — NY Fed Q2 2026 Household Debt & Credit report** — 🟠 — OTTO,CARL,REGINALD — `confirmed` — Q1 2026 published May 12 ($1.685T auto / 2.97% transition-to-90+); Q2 2026 due ~Aug 12-15. Suggested rationale: this is the canonical aggregate-auto read; missing it means a quarterly data point silently drops from the docket.
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
- **Tricolor SDNY criminal (Chu/Goodgame, Judge Castel)** — Selective scope: trial date Oct 19 2026 + cooperator motions only. **Oct 19 NOT final** — Castel holds a Jul 29 hearing on Chu's motion to slip to Feb 2027; sweep that outcome. Re-verify monthly until ~T-30; then weekly. (Liman handled the Dec-2025 cooperator pleas — do not attribute the trial to Liman.)
- **Carvana derivative / discovery (DE Chancery)** — Verify production milestone dates from StockTitan / PRNewswire / direct Chancery filings.

### Recurring releases (monthly cadence; verify forward two)
- **Fitch Auto ABS Index** — Jan-2026 baseline 60+ DQ 6.90% / recovery 32.64% / ANL 9.81%; spring tax-refund bounce lifted the series (60+ DQ ~6.1%, ANL ~8.8%, recovery 37.48% `[PRESS]`). **~2mo data lag** — a mid-month release carries ~2-months-prior data; don't over-read print freshness. Monthly cadence. Source: Fitch direct + Auto Finance News.
- **NY Fed HDC (Quarterly)** — Q1 2026 released May 12. Q2 2026 due ~Aug. Source: newyorkfed.org.
- **S&P / KBRA / Moody's ABS surveillance** — Monthly + on-event. Watch for ECNL revisions, CreditWatch placements, downgrade waves.

### Bank-earnings cycle (named-banks subset only)
- Q2 2026 earnings cycle opens ~Jul 15 (JPM, WFC, C lead). Named-banks: **JPM, 5-3, BCS, Regions, MTB, OBK**. Source: SEC EDGAR + IR calendars.

### ABS pricing windows (modeled rows)
- **EART Q3 2026** — Exeter Q3 issuance typically Sep. Modeled date; revise within 7d via SEC EDGAR FWP.
- **Bridgecrest** — Carvana-related; quarterly. Watch for related-party pricing dynamics.
- **GCAR / smaller stressed shelves (CPS, Flagship, Lendbuzz, SAFCO)** — Watch for shelf-halt signal (OTTO-07).

### TRADE.md position expiries
- ⚠ TRADE.md is **rehab-pending** (stale since pre-CVNA 5:1 split May 7). Position expiries pulled from TRADE.md should be flagged with skepticism. Cross-verify with FORGE if possible. Pause adding position-expiry rows until TRADE.md rehab is complete.

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

### Calibration notes

- **Inaugural calibration (Jun 9 2026):** 5 baseline-audit proposals → 4 accepted, 1 deferred-not-declined. WINTERKORN's instinct on per-case docket vs recurring-release scope was sound. The one defer was on a class where OTTO already has a working mirror (Auto Finance News for rating-agency surveillance); reflects "don't duplicate an existing pipeline" lens.
- **Date-classification pattern:** Fitch ABS Index rows and NY Fed HDC rows go in as `modeled` (release dates approximate); a docket-noticed continuance like Tricolor Nov 11 goes in as `confirmed` (court-issued). Use this split going forward.
- **Carvana ambiguity is a true PENDING, not a defer.** WINTERKORN's halt-on-ambiguity on the Jun 12 Carvana row was correct — OTTO has direct Chancery access for Carvana derivative track that WINTERKORN doesn't. Don't propose changing the row class unless OTTO updates the calibration.

---

## NEXT RUN HINTS

Notes from the most recent run for the next-WINTERKORN to read first. Captures one-off context that doesn't fit in STANDING MONITORS but matters for the next sync.

### Hints for next run (carried from 2026-07-04)

**🔴 T-3 pre-Jul-28: re-verify the First Brands confirmation cluster.** Jul 28 9am CT confirmation (combined w/ final DS) is the operative OTTO-32 resolver. Chain of dated dependencies to sweep in order: **Jul 20** creditor-vote deadline (class rejection → Jul 28 cramdown fight) → **Jul 27** ballot-cert + confirmation-brief/replies → **Jul 28** hearing. Re-verify no adjournment via Kroll/Octus/Law360/Bloomberg Law. If confirmed, OTTO-32 resolves CONFIRMED (well inside Sep 30).

**🔴 Jul 29 Tricolor trial-scheduling hearing — sweep the outcome.** Castel rules whether Oct 19 trial holds or slips to **Feb 2027** (Chu delay motion, Inner City Press Jun 29). If slipped, revise the Oct 19 TSV row date_class + STATUS; the Oct 19 fraud-surface-expansion catalyst moves to 2027. This gates a 🟠 row — verify before T-30.

**Jul 14 (banks) / Jul 15 (Fitch, MTB) / Jul 21 (Ally) earnings — OTTO-30/-31/-04/-28 inputs.** Confirm no date drift. Watch for a 6th NEW Tricolor-exposed bank name (OTTO-30, last forward-discovery shot before Aug 31) and Wilmington/MTB custodial-exit language (OTTO-31).

**EART 2026-4 (next Exeter ABS) — watch for the FWP.** Exeter's cadence is fast (3 deals by June; 2026-3 priced ~Jun 24). Next deal likely **~Aug, earlier than the "typically Sep" standing-monitor note.** Below T-30 now — pick up the FWP via SEC EDGAR next run; a subordinate-tranche print feeds the (now-disconfirmed) systemic-ABS-spread thread.

**First Brands examiner (Martin De Luca, Boies Schiller)** — appointed Nov 19 2025, $7M budget, work plan approved Jan 2026. No public **report-deadline date** yet. Potential fraud-surface catalyst if findings land — monitor for a report date to dock.

**Fitch ABS Index cadence caveat** — index runs ~2mo data lag; a mid-Jul release likely carries ~May data. Don't over-read "Jun print" freshness.

**No open PENDING carry-forward** — all 3 Jun-9 blocks cleared Jul 4 (see PENDING banner). Read CALIBRATION before any baseline audit: rating-agency direct surveillance stays DEFERRED (Auto Finance News mirror covers).

### Standing context (durable)

- **Pre-fire date verification is the load-bearing job step.** OTTO's Jun-8 catch (First Brands Jun-17 → Jun-12) is the canonical failure mode this sub-agent exists to prevent.
- **Verita Global cert issue is known and recurring.** Halt-on-ambiguity convention applies to all Tricolor Ch.7 docket fetches.
- **First Brands is the highest-activity case.** Re-verify weekly.
- **TRADE.md is rehab-pending.** Skip position-expiry additions until rehab is done.
- **Spawn cadence:** weekly Tue + on-demand T-3 pre-hearing. Outside that cadence, spawn cost > value.
