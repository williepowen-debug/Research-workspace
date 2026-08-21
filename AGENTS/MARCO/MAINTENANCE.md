# MARCO — MAINTENANCE PUNCHLIST

**Purpose:** Standing list of stale / needs-attention items flagged for action at a later session. Flag-and-document only — items here are NOT yet fixed. Work them down at boot when not mid-event; check items off + date them.

**Created:** 2026-06-08 (session 12 — flag-and-document sweep while waiting on LABOR). Method: boot.py awareness layer + manual file read across all MARCO docs. Ranked by **behavioral impact** (does the agent DO something different?), not line count.

---

## TIER 1 — thesis-load-bearing (fix first)

### ✅ T1-A · FINDINGS.md points to the WRONG thesis version + carries a stale "Live state" block — DONE 2026-06-15
*(Resolved: bumped v2.0→v2.5; "Live state" block rewritten to pure pointers, no restated drifting values; header date refreshed.)*
- **What:** `FINDINGS.md` (the boot navigator) line 71 says "thesis/THESIS.md (**v2.0**, canonical)" — actual is **v2.4**. Lines 63-73 ("Live state — refreshed 2026-05-31") *restate* STATUS values that have since drifted: remittances "Mar +4.9% / count −3.6%" (now Apr +3.7% / count −1.7%), Canadian "Apr +1.4% headline" (pre-session-9 base-effect correction), produce "+6.1% (ag-labor stock loss)" (pre-v2.1 multi-causal resolution).
- **Why it matters:** FINDINGS is a navigator a fresh spawn may read to orient — a v2.0 pointer + drifted live-values misdirects. Violates single-source-of-truth (file even says "Not a synthesis — a navigator").
- **Action:** Bump v2.0→v2.4; prune the "Live state" block to pure pointers (no restated values — point to STATUS/thesis).
- **Effort:** small.

### ✅ T1-B · Channel-1 "2.2M" magnitude data-quality tension — RESOLVED 2026-07-02
- **What (was):** NOTES.md flagged DHS 2.5M departures (1.9M self-deported) vs independent counts ~290-340K (MPI/Brookings/TRAC) as a disputed load-bearing figure under the "2.2M CBO" spine.
- **Resolution:** PROME Tier-2 verification (Workflow, vs CBO/NFAP-BLS-CPS/KC-Fed; inbox 6/26) confirmed the tension and re-marked it: "2.2M CBO" was a mis-attributed **disputed-DHS** claim (CBO removals ≈290K+30K — matching this flag's ~290-340K independent counts); realized = **~1.0M foreign-born LF / ~1.5M pop** (FRED LNU01073395). Re-marked across canonical + live surfaces (thesis v2.6, STATUS, VX-SDL-01, KB, FINDINGS, NEXUS_BRIEF); reconcile notes to LABOR+CORAL. Direction/mechanism unchanged; corroborated by June-2026 LF −1M+ YoY. MARCO's own NOTES.md flag was correct.

### ✅ T1-C · H-2A "requested vs certified" series ambiguity in MAR-11 — DONE 2026-06-15
*(Resolved: MAR-11 note now specifies threshold on CERTIFIED series, FY25 certified 398,059, '415K' was requested; cross-refs FINDINGS/OFLC. NEW flag found while editing → see T1-D below.)*
- **What:** Today's h2a_pull returned FY25 **certified = 398,059**. `FINDINGS.md` line 55 already resolves it: "prior '415K' was positions **REQUESTED**." But `PREDICTIONS.tsv` MAR-11 ("H-2A certifications >425K, FY2026") still carries the note "FY2025 was 415K" without the requested-vs-certified distinction.
- **Why it matters:** MAR-11 resolves at the ~Jun-30 OFLC Q3 window. If scored against 415K-requested baseline instead of 398K-certified, the threshold read is wrong. Canonical-measure discipline.
- **Action:** Edit MAR-11 note to specify certified-series (FY25 certified 398,059; prediction threshold = certified >425K). Cross-ref FINDINGS/OFLC_H2A_PULL.
- **Effort:** small.

### ✅ T1-D · PREDICTIONS.tsv inconsistent column count — DONE 2026-07-31 (found 2026-06-15, open ~6 weeks)
*(Resolved: all 16 data rows normalized to the 9-col header; `predictions_due.py` given a schema guard; CSV-quoting artifact cleaned.)*
- **What it actually was** (the 6/15 flag said "14 rows missing `Outcome`" — the real shape was **10 of 16** rows at 8 cols, and the missing field **differed by row**, so a blanket insert would have corrupted half of them):
  - **5 OPEN rows** (MAR-11/12/14/22/24) had **notes text sitting in the `Outcome` slot**. An OPEN prediction has no outcome, so the fix was to *insert* an empty `Outcome` and shift the text into `Notes`.
  - **5 CONFIRMED rows** (MAR-10/15/08/25/27) had a **genuine outcome** in place and were simply **missing `Notes`** — fix was to *append* an empty field.
  - **Rule applied:** `Status == OPEN` → insert; otherwise → append. Verified afterward that **`Outcome` is now empty iff `Status == OPEN`** across all 16 rows.
- **Also cleaned:** MAR-12's `Notes` was wrapped in stray `"` with internal `""` — a **CSV-quoting artifact leaked into a TSV** (same class as the s18 csv round-trip that silently re-quoted 7 VX rows). Unwrapped and collapsed.
- **Safety:** the rewrite asserted the multiset of non-empty field values was **identical before and after** (129 fields preserved) before writing; backup taken.
- **Consumer check:** `predictions_due.py` reads by **header name**, not position, so nothing was depending on the broken shape — the fix strictly improves it (previously an 8-col row's notes were returned under the `Outcome` key while `Notes` came back empty). Re-ran clean: 5 OPEN, no false due-flags.
- **⚠️ The real lesson — the parser's tolerance is what let this rot.** `load_predictions()` right-pads short rows so it never crashes, which is correct for boot resilience but meant a malformed file parsed *silently* for six weeks. **A tolerant reader that stays quiet is how a bad file passes review forever.** It also made hand-editing hazardous: during this session's MAR-14 re-rate a field was dropped (8→7 cols) and the padding parser would have absorbed it without complaint — caught only by an explicit count check.
- **Guard added:** `predictions_due.py` now emits `PRED_SCHEMA_WARNINGS` at every boot for (a) any row whose width ≠ header, (b) `Status=OPEN` with a populated `Outcome` **or** a resolved row with an empty one — the semantic tell that fields have shifted, and (c) doubled-quote artifacts. Tested both directions: **16 issues flagged against the pre-fix file, silent on the fixed one.**

### ✅ T1-E · FL Citizens "$678.8B" was stale AND directionally backwards — RESOLVED 2026-07-02
*(Found in the 7/2 staleness hunt.)* The "$678.8B, growing toward $750B (MAR-17), systemic-risk BREACHED" was a **2024/near-peak** figure and the trajectory REVERSED: Citizens depopulated 585,432 policies + removed $235.6B exposure in 2025, entered 2026 **67% below peak**, 395,144 policies (was 936K). **Re-marked:** MAR-17 INVALIDATED (wrong direction); VX-SFE-03 BREACHED→DE-ESCALATED; thesis Channel-3 insurance leg (exposure-thermometer decoupled from the affordability crisis, risk shifted to private market); STATUS FL-triple-exposure; KB-MARCO-SFE-02. Cross-flag CORAL (whole-FL insurance owner). **Residual:** exact current-exposure $ = Citizens Dec-2025 board report (to verify); `sub_agents/HOUSING` + `CLAUDE.md` threshold table still carry $678.8B (see T3-D / open items).

### ✅ Doc-mirror · docket/CALENDAR.md re-synced to CATALYSTS.tsv — DONE 2026-07-02
*(CALENDAR.md had drifted 17d behind the TSV after the 6/8 update — listed June events as forward. Full rewrite to the current forward window this session.)*

---

## TIER 2 — stale state / single-source-of-truth

### ✅ T2-F · VX.tsv stale-vector sweep + boot guard — DONE 2026-07-31 (backlog carried s18→s19)
*(37 of 57 vectors were >60d, 25 of them BREACHED/CRITICAL. Triaged by STATUS, not age — the rule s18 wrote after two stale rows were cited and were wrong in **opposite** directions.)*

| Disposition | n | What |
|---|---|---|
| `FROZEN 2026-07-31` | 17 | The **border-fiscal research area** (ELP/NOG/MCA/PHR/BDR/CAL/SFE) — untouched since founding, Feb 2026. Banner carries date + why + where truth lives, per `STATE_VOCABULARY.md` class 1 |
| `RETIRED 2026-07-31` | 1 | **STR-01** — `PENDING`/"BASELINE NEEDED" since 2026-02-23 and never built (STR/CoStar paywalled). Not a stale value, an **unbuilt vector** |
| **CORRECTED** | 1 | **2.02** carried the **retracted "2.2M self-deportations" attributed to CBO** — the founding error corrected fleet-wide in v2.6 on **7/2** — and kept asserting it for 4 more months, at HIGH/BREACHED |
| **REFRESHED** | 1 | **H2A-01** → live OFLC (254,688 certified FY26-thru-Q2), off the puller repaired this session |
| stale-by-design | 6 | Annual Census/CBO cadence (2.04, 3.04, TX-04, SBMD-01, CTI-01) + **CA-02 NO PRIMARY** (NAWS + Ag Labor Survey both canceled — same class as 2.05) |
| `[STALE]`-marked | 10 | Live domain, unrefreshed — vintage stated per the discipline overlay |

- **The finding worth keeping:** **2.04 held the CORRECT CBO figure (−290K to −525K) the entire time 2.02 and the thesis spine were asserting a wrong one *attributed to CBO*.** The right number was one row away from the wrong one, in MARCO's own ledger, for six months. Same class as the s18 lesson — the ledger had the answer and nobody opened it. **A load-bearing correction must sweep the vector ledger, not just the narrative surfaces** ([[finding_verification_correction_downstream_propagation]]).
- **Freeze does NOT restamp `Last Updated`** — the row keeps its original data vintage, deliberately; the freeze date rides in `Status`. Restamping would manufacture freshness ([[finding_hygiene_commit_rearms_the_staleness_lie]]).
- **Boot guard built** (`staleness.py`): ranks **BREACHED/CRITICAL + >60d** as its own 🔴 alert, drops FROZEN/RETIRED (age by design), and separates **stale-by-design** from real rot — because an alert that cries wolf on 37 rows every boot gets filed as housekeeping, which is precisely how s18 happened. Validated both directions: **25 against the pre-sweep file (matching s18b's hand triage exactly), 5 after.**
- **Remaining, and now named every boot:** 5 genuinely-refreshable BREACHED/CRITICAL rows — FL-03, TX-02, CA-01, 3.02, GTR-01. FL-03 and GTR-01 are the worst, both having *live free sources* (FL Realtors monthly; Google Trends).
- ✅ **Escalation raised by the freeze — CLOSED 2026-07-31 (v3.1).** THESIS carried **Channel 4 at MEDIUM** on an entirely frozen evidence base; re-marked the same session to **MED-LOW**, split along its own mechanism (flow leg LIVE/MEDIUM, fiscal terminus LOW/UNVERIFIED), with named rebuild conditions. *(Row still read UNRESOLVED 🔴 until 2026-07-31 eve — closed then, PROME audit. The escalation and its fix landed in the same session and nobody closed the ticket.)* **Rebuild remains open and is tracked in `SCRATCH.md` NEXT SESSION 3**, not here.

### T1-F · KB.tsv has 2 DUPLICATE IDs — citations are ambiguous (NEW — found 2026-07-31)
- **What:** two KB IDs are each used by **two unrelated facts**, assigned months apart:
  - `KB-MARCO-REM-03` = Mexico FY2025 remittances final (2026-02-17) **AND** Banxico Apr-2026 pull-forward (2026-06-02)
  - `KB-MARCO-TX-04` = Austin housing root-cause (2026-01-22) **AND** TX border sales-tax growing / ES-MARCO-04 counter-signal (2026-06-08)
- **Why it matters:** a KB ID is a **citation handle**. "See KB-MARCO-TX-04" currently resolves to two different findings that point in *opposite* directions (a housing correction vs a counter-signal that revenue is growing). Anyone citing it can be pointed at the wrong evidence, and a grep-based check cannot tell which was meant.
- **Do NOT renumber unilaterally.** IDs are cited across sessions and possibly by other agents — the same stable-API logic that root CLAUDE.md applies to the Critical Rules. The fix is either a suffixed successor (`-04b`) with a pointer on the elder row, or a documented "on collision, disambiguate by Date" convention.
- **Also fixed while here (2026-07-31):** a stray blank line mid-file, and a 15-column row created by appending to a file with no trailing newline (caught by a post-write column count — the same defect class as MAINTENANCE T1-D, and my own append caused it).
- **Action:** decide the convention, then add a duplicate-ID + column-count check to the boot sweep (the `predictions_due.py` `PRED_SCHEMA_WARNINGS` pattern ports directly).
- **Effort:** small.

### T2-E · Banxico + slaughter fetchers still cadence-skip on **mtime** (NEW — found 2026-07-31)
- **What:** session 19 moved the H-2A fetcher to a **content-vintage** gate (`h2a_vintage()` reads `fy=`/`through_q=` out of the TSV header and compares against the quarter DOL should have published). The other two entries in `boot.py FETCHERS` still gate on `file_age_days()` — raw mtime.
- **Why it matters:** root CLAUDE.md Data Hygiene is explicit that **mtime is restamped by git sync**, so an mtime cadence fails **FALSE-NEGATIVE** (it thinks a file is fresh because another machine's pull touched it) — [[finding_mtime_is_corrupted_by_git_sync]]. Under serial multi-machine operation MARCO pulls constantly, so both remaining fetchers can silently skip when they should run. Lower severity than H-2A was: Banxico's output carries its own dated rows and slaughter is a 6-day cadence, so drift is visible sooner.
- **Action:** give `banxico_reverse.py` and `slaughter_pull.py` outputs a `# … pulled=YYYY-MM-DD | latest_period=…` header line like the rebuilt H-2A TSV, then wire a `vintage_fn` for each. The `FETCHERS` tuple already carries the optional 6th slot — no structural change needed.
- **Effort:** small-medium (two tools + two gate functions).

### ✅ T2-D · docket duplicate rows + stale premises — DONE 2026-07-31
*(Found at boot: `catalyst_countdown.py` printed 11 due-events for 8 real ones. `CATALYSTS.tsv` held **3 duplicate event pairs** — Banxico 8/1, BLS NFP 8/8, NTTO 8/15 — created 7/25 when 7 new rows were appended without a merge check against the existing 9, in a **second priority vocabulary** (HIGH/MEDIUM/LOW vs the established emoji). Merging surfaced 3 stale premises that had survived their own corrections: the Aug-8 row still instructed a reader to run the **v2.7 wage-instrument confirm test that v2.8 falsified**; MAR-24 was carried at **45%** against a canonical **60%** (45% is MAR-14's number); the ICE row still cited the **retracted "2.2M"**. All merged/corrected, priority normalized, 16→13 rows, CALENDAR twin reconciled (it had NO duplicates — the machine feed was the broken surface, not the prose twin). **Class lesson: an append-only docket edit needs a dedup pass against existing rows, and a `date+event` uniqueness check is one line — worth adding to `catalyst_countdown.py` so it self-detects.*)

### ✅ T2-C · H-2A fetcher dead ~101 days — DONE 2026-07-31
*(`h2a_pull.py` had a **hardcoded** `CANDIDATES` filename list. DOL publishes ONE cumulative FY-to-date file whose quarter suffix advances and whose superseded name stops resolving, so the list rots into a hard failure every quarter; its Wayback-only strategy then failed too, because Wayback doesn't reliably archive 16MB xlsx files. Rebuilt: **discovers** the filename from the live performance page and fetches **dol.gov directly** — the Akamai wall passes a complete browser header set and 403s a User-Agent-only request, which is what had forced the Wayback detour. Wayback retained as fallback. 300s timeout → **11s** actual. Verified: FY26-through-Q2 = **254,688** certified, independently reproducing the figure STATUS already carried. Boot gate moved to content-vintage so the Q3 file auto-fetches on publication instead of being masked by an 85-day mtime skip armed the day before. See T2-E for the un-migrated siblings.)*

### ✅ T2-A · STATUS.md internal stale blocks — DONE 2026-07-02
*(Resolved in the 7/2 staleness hunt: "NEXT SESSION FOCUS (5/31)" block pruned → pointer to SCRATCH; "CROSS-AGENT NEEDS RE-SEND" block retired → pointer to NEXUS_BRIEF SENDING + outbox. Both were confirmed superseded.)*

### ✅ T2-B · RESEARCH_STATUS.md drift — DONE 2026-06-15
*(Resolved: remittance paradox + FLL-April → COMPLETE; ag-weather refreshed as open PROME loop; TOURISM row = SHELVE-sub-agent/KEEP-vector decision (was mislabeled "stalled"); StatCan Q1→Q2 gap re-dated; FL-airport gap → MCO-only/BTS-July. Header date refreshed.)*
- **What:** (1) "Remittance paradox" still under ACTIVE — RESOLVED 6/2 (paradox fading), should move to COMPLETE. (2) TOURISM listed DORMANT/"stalled, no commits since Apr 22" — **contradicts the session-11 finding** that TOURISM is NOT stalled (content current, refreshed session 9; ran a live World Cup pull 6/2). (3) "StatCan Q1 2026 BOP" GAP — superseded by Q2 (~Aug 28) per docket. (4) "Ag-weather/crop-disaster owner" — flagged to PROME 5/31; assignment status unknown (open loop).
- **Action:** Move remittance paradox → COMPLETE; correct/remove the TOURISM-stalled entry; re-date StatCan gap to Q2; chase the ag-weather-owner loop with PROME.
- **Effort:** small.

### 🟡 T2-C · TRADE.md is Feb-14 vintage (pre-v2.1 framing) — STAMPED 2026-07-02 (full refresh still pending)
*(7/2: added a prominent "FEB-VINTAGE — NOT CURRENT" banner listing the stale figures + the IBOC re-eval note, so it no longer misleads if read. A full metrics refresh + IBOC-vs-winter-$ re-evaluation is still open.)*

- **What:** All figures Feb-vintage: Mexico remittances "−5%" (now +3.7%/count −1.7%), Central America "+18-25%", construction "−92.7% YoY growth", TX border DQ 7.92%. Whole file reflects the **acute-crisis framing the thesis has since walked back** (v2.1-v2.4 slow-structural-squeeze). IBOC-puts + ag-exposure ideas never actioned.
- **Why it matters:** Low direct behavioral impact (MARCO doesn't trade; feeds OTTO/LABOR/REGINALD) — but if read as current it misleads. The IBOC border-bank idea is arguably *more* relevant now (winter-$ hole → REGINALD), so don't just delete.
- **Action:** Reconcile to current thesis OR stamp clearly as "Feb-vintage watchlist, not current." Refresh the metrics table. Re-evaluate IBOC idea against the winter-2026-27 timing.
- **Effort:** medium.

---

## TIER 3 — dormant / cleanup

### ✅ Dormant sub-agents FROZEN-bannered — DONE 2026-07-02, TOURISM closed 2026-07-09
*(7/2 hunt: BORDER/HOUSING/MIGRATION/WORKFORCE STATUS files (untouched since Apr-21, carrying stale DHS-shutdown / 9.1mo-condo / $678.8B / 2.2M figures) each got a FROZEN banner pointing to canonical STATUS. TOURISM left live (recent) — the 7/2 call was correct at the time (5/31-dated, ~32d old). **7/9 self-sweep: that grace period had lapsed (39d, no banner) — found and closed. TOURISM now carries a SHELVED banner matching the other 4.** Will-approved freeze-not-archive.)*

### T3-A · VX.tsv — 46/57 vectors are Jan-vintage (>60d, boot.py flags)
- **What:** 45 of 57 vectors last-updated Jan 20-22 (founding research): FL insurance index, net-migration, Sunbelt-Snowbelt differential, TX/FL housing, CA ag workforce, border vectors, etc.
- **Why it matters:** Some are genuinely stale and load-bearing (FL insurance, migration); some are deprecated/annual (can't refresh). Bulk staleness hides which.
- **Action:** Triage pass — per vector: refresh / mark `[STALE]` with date / archive-deprecated. Don't bulk-refresh; sort by whether the vector still drives a thesis claim.
- **Effort:** large (do in chunks).

### T3-B · RP-MARCO-MBS_BASELINE.md — never-executed + wrong VX refs
- **What:** Feb-9 baseline protocol for monitoring border-city **municipal-bond spreads** (EMMA). Status: "Awaiting initial spread data collection." Cross-refs use OLD VX numbering (VX-MARCO-01/03/06) that **doesn't match** current VX.tsv (1.01 / 2.02 / ELP-01 / etc.).
- **Why it matters:** **Latent opportunity:** ES-MARCO-04 (TX border fiscal stress) resolved today as a *counter-signal* on sales-tax revenue — but muni-bond spreads (EMMA) could be the cleaner, more forward-looking border-fiscal-stress instrument that sales-tax (a lagging, offset-able measure) isn't. This never-run protocol may be worth executing, not archiving.
- **Action:** Decide execute-vs-archive. If execute: pull EMMA spreads for the 5 target cities, fix VX cross-refs to current numbering, populate a real border-fiscal vector. If archive: move to `archive/` and note in FINDINGS. ⚠️ **`AGENTS/MARCO/archive/` does NOT exist** — the 2026-06-30 prune (`1cb18fbc3`) deleted it and both files it held. **If you execute the archive branch, create the dir ON PURPOSE in the same edit** — do not let it regrow as a side effect of following this line (flagged by PROME 8/12; re-pointed 8/21).
- **Effort:** medium-large (if executed).

### T3-C · MARCO_SKELETON.md — historical artifact
- **What:** v1.0 thesis, explicitly superseded by `thesis/THESIS.md` (v2.4).
- **Action:** Archive to `archive/` (low priority; harmless where it is, but it's root clutter). ⚠️ **Same nonexistent-destination caveat as the row above** — `AGENTS/MARCO/archive/` was deleted by `1cb18fbc3`; create it deliberately if you execute, or just leave the file where it is (which this row already concedes is harmless).
- **Effort:** trivial.

---

## Cross-references (already tracked elsewhere — not re-flagging)
- DEFERRED.md (4 open TOURISM cross-agent items: REGINALD ×2, HOUSING, CARL) — current as of 6/2, properly tracked. The CARL World-Cup item + REGINALD winter-$ items are now partly addressed via today's NEXUS_BRIEF SENDING + outbox; could cross-ref.
- ~~MCO/FLL April pax (PDF-blocked)~~ — **FLL RESOLVED 6/15** (pdfminer on Broward Monthly Statistical Summary PDF: +5.0% YoY / −4.7% 2-yr stack; intl −18.7% stack). MCO still blocked (flymco JS-rendered) → BTS T-100 ~Jul. Method: download+pdfminer w/ browser UA beats WebFetch for airport PDFs.
- Cross-agent re-sends — see T2-A (likely superseded by NEXUS_BRIEF).

---

*Maintained ad-hoc. Re-run the flagging sweep periodically (boot.py staleness + manual doc read). When an item is fixed, check it off with a date or delete the entry.*
