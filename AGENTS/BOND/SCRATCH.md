# BOND SCRATCH — 2026-08-15 (Sat — TWO sessions: ~11:50–12:20 boot, ~12:30–13:15 inbox drain. BOTH CLOSED OUT)

> ## SESSION 2 ADDENDUM — general inbox DRAINED (Will-tasked, ~12:30–13:15 ET)
>
> **All 5 general packets processed per `PROTOCOL.md` § Inbox Processing and `git mv`'d to `processed/`. Inbox EMPTY; WALTER lane EMPTY. Full detail → `RECEIPT.md`.**
>
> **What came out of it, ranked:**
> 1. **SAM's custody lead ADJUDICATED — it's a ROUND-TRIP, not a drawdown.** 57 H.4.1 releases pulled from the Fed primary (FRED's custody family was discontinued 2012-11-07). The −$59.8B decline SAM flagged is the **unwind half** of a **+$58.7B build** (the largest 2wk build in the sample, z=+2.45); **five-week net −$1.1B ≈ zero.** Reading only the decline half inverts the conclusion. ⚠️ The **secular** decline is separate and real (**YoY −$258B**) — don't let this travel as "custody is fine." `KB-BND-109`.
> 2. **Parser defect caught BEFORE publishing** — regex required 4+ chars, silently skipped sub-1,000 weekly changes, shifted a column onto the *agency debt* row; base-rate stdev 980,561 vs a true 20,347. Op-window rows unaffected; **the base rate was the broken half.** v2 fails loud + reconciles the release's own printed Δ (0 mismatches / 56 pairs). `KB-BND-110`.
> 3. **DFII10 "SERIES HIGH" retracted — wrong three ways** (all-time is 3.15 [2008]; 133 pre-2026 obs beat the 2026 max; **and the 2026 peak is 2.47 [7/31], not the 2.43 I carried**). MIDAS caught two via PROME; **the third nobody had flagged.** Closest approach to the 2.5 add-gate was **3bp**, not 7bp. `KB-BND-108`.
> 4. **T7's "independent convergence with LABOR" clause RETRACTED — my error.** LABOR graded the 7/29 statement+presser; T7 grades that meeting's minutes ⇒ shared antecedent. Frozen CONFIRM/DENY text untouched. **Vintage trap adopted as binding: grade the 111K/−74K vintage, never today's +20K/−103K.** `KB-BND-112`.
> 5. **FIMA take-up for the 7/30-31 op = measured ZERO** (SAM). ⛔ Does NOT invert to "USTs were sold." **`FL-BND-11` is now recorded CONDITIONAL on the funding channel, neither branch confirmed** — it was written as automatic before this drain. `KB-BND-111`.
> 6. **`NEXUS_BRIEF.md` RE-PINNED 7/28 → 8/15** (superseding block prepended; 7/28 body bannered and retained). **`PROTOCOL.md`'s stale FR2004 "known access gap" fixed** — it closed 7/28 and the line had spent 18 days telling sessions not to try. **T-23 (policy-path vs credibility) ACCEPTED, BOND owns it — registered as a real object with NO threshold**, per the 8/10 ruling.
>
> **Packets out:** SAM (cc LIQUID) · LABOR (cc NEXUS/PROME) · NEXUS. **KB +6 (`108…113`, 114 rows validated). CATALYSTS +2 (8/31 MOF, 11/13 FRBNY Q3).**
> **No threshold moved. No vector moved. No position change. Composite unchanged 12/35.**
>
> **NEXT-SESSION items 2 and 8 below are now DONE** (inbox drained; brief re-pinned). **Items 1, 3, 4, 5, 6, 7 stand unchanged.** New: **T-23 has no instrument and that is deliberate** — do not ship a threshold on it without a base rate first.

---

## SESSION 1 — Will-requested boot, ~11:50–12:20 ET

**Purpose:** Ephemeral session handoff. Read at boot, rewritten at closeout. Learnings → `MEMORY.md` / auto-memory; thesis → `thesis/THESIS.md`; live state → `STATUS.md`.

**Session shape:** Will said "boot up." Ran the full BOOT read phase, then the write-back tail — because boot step 4 surfaced a 15-day-overdue prediction and boot step 7 surfaced a 7-deep unprocessed WALTER lane. Neither is optional under the protocol.

---

## CHANGES SINCE (7/28 SCRATCH → now)

⚠️ **The 7/28 SCRATCH was the last one written. An 8/10 Financial-Conditions forum session ran in between, wrote STATUS, and did NOT rewrite SCRATCH or run the closeout tail** — which is why `BND-01` sat OPEN-but-stale for 15 days past its window. **The gap between "STATUS updated 8/10" and "SCRATCH dated 7/28" was the tell, and it is worth watching for again.**

What actually happened while dark, in order of consequence:

1. **FOMC 7/29 HELD**, and everything since has repriced **dovish**: ORACLE aggregate hike-2026 **71.5% [7/24] → 54.5% [8/12]**; Sept-specific **35.5% [8/9] → 33.5%**. Attribution is ORACLE's: 71% of the drop is the FOMC hold + 8/7 payrolls, only 29% is the 8/12 CPI.
2. **8/10 forum (Will-ruled in-session):** C-36 "policy-path-led" downgraded **CONFIRM ~80-85% → CONTESTED ~50%**; **T6** and **T7** registered as frozen tests; **sovereign-credibility instrument set** claimed (rates half only). HENRY cross-examined the evidence count down from "4 legs" to **2 independent evidence types**. All recorded in STATUS; **the composite/dashboard were explicitly left un-re-scored as a full-closeout task** — this session did that part.
3. **Credit INVERTED.** HY 279 [7/24] → **287 cycle high [7/29]** → 271 [8/13], fully round-tripped and now *below* the 268 it started from. **CCC 996 → 1024, through 1000, making new highs.** Ratio 3.57x → 3.78x.
4. **DFII10 never breached 2.5** — re-touched 2.43 on 8/10-11 and backed off to 2.39. The gap to the re-arm **widened** (7bp → 11bp).
5. **7 WALTER deliveries** landed (8/11–8/13) and **5 general-inbox packets** (8/10–8/14, two of them SAM retractions).

## WHAT I DID

| # | Action |
|---|---|
| 1 | **`BND-01` RESOLVED FAILED.** Full May–Jul window re-pulled from FRED (67 obs): **max 287bp on 7/29**, **zero** obs ≥350, closest approach 63bp short, and the *mechanism* never engaged. **Prediction book is now EMPTY.** |
| 2 | **WALTER lane drained** — all 7 read, integrated, `git mv` → `processed/`. Reply packet to WALTER answering both ACTION asks. |
| 3 | **Computed the 30Y regime statistic** off FRED `DGS30` (1,149 obs, zero missing) — **and it corrected two of my own published figures.** |
| 4 | **Found two T6 spec defects**, 14 days before the hard close. Flagged to LIQUID (co-owner) / PROME / ORACLE. **Frozen spec NOT edited.** |
| 5 | STATUS rewritten: header, 11 dashboard rows, matrix HY row, T6 live state, gates, catalysts, new BOTTOM LINE. |
| 6 | `KB-BND-101…107` (+7, 13-col validated, CRLF preserved). `VX-BND-02` held-with-conditions, **`VX-BND-11` 2→3**, `VX-BND-05` evidence corrected. `CATALYSTS.tsv` synced (4 rows resolved, 2 added, credit row refreshed). |

## 🔴 THE THREE CORRECTIONS TO MY OWN NUMBERS — read these before citing anything in STATUS

1. **"29-day run above 5%" was WRONG.** On the day I wrote it (7/28) the run was **16 sessions**. It conflated calendar days with sessions and/or a cumulative count with a consecutive run — **two different statistics published as one number.** Correct: **28 consecutive sessions (7/07 → 8/13, ongoing)** and **44 cumulative days >5.00% in 2026** (28% of 155; 2025: 6 · 2024: 0 · 2023: 8). `KB-BND-102`.
2. **The cycle high "5.28 [7/31/8/2]" is on the wrong instrument and a nonexistent date.** `DGS30` max is **5.27 (7/31)**. 5.281 was a yfinance `^TYX` **intraday high**; **8/2/2026 is a Sunday**. **Load-bearing because T6's fresh-high leg is keyed to it** ⇒ that leg is unreachable by construction against the series it grades on. `KB-BND-103`.
3. **DFII10 "7bp from the 2.5 re-arm" was carried 18 days.** It is **11bp** away and the gap **widened**. Three approaches, no breach.

**All three are the plausible-stale class, and none would have been caught by re-reading the file — only by recomputing.** #1 and #2 were found because WALTER's `-012` asked me a question about my own instrument instead of telling me an answer.

## SCORE / STATE CHANGES

| Surface | Change | Basis |
|---|---|---|
| `VX-BND-11` CCC OAS | **2 → 3** | CCC through 1000 (1024), new highs, while the index retraced. The session's one genuine escalation. |
| `VX-BND-02` HY spread | **HELD at 2, deliberately** | Its 7/28 upgrade rationale evaporated (HY below where it started), but a different leg of the same rollup escalated. **Registered instead of exercised** (7/28 VX-08 precedent): →1 on CCC <1000 **AND** HY <280 for 5 sessions; →3 on HY >300, a first pulled deal, or CCC >1100. |
| Matrix "HY market function" | **unchanged 2** | rollup counted once; conditions above. |
| `VX-BND-05` long-end | **unchanged 4** | level breach decisively met; **evidence cell corrected**, score untouched. |
| **Composite** | **unchanged 12/35** | No matrix row moved. VX-11 rolls up into a row counted once. |
| TLT add-gates (b)(c)(d) | **all RESOLVED, DID NOT FIRE** | (d) died the right way — the post-FOMC repricing ran *dovish*, the opposite of what that gate needed. |
| **Position** | **TLT puts HOLD, no add.** Will's 7/16 NO-ADD stands. No new BOND trade rec. | |

## NEXT SESSION (dated, future-verifiable)

1. **🔴 WED 8/19 — FOMC minutes. `T7` resolves on its frozen text; this is the nearest graded event.** CONFIRM (≥4 participants beyond the 3 dissenters discuss a near-term hike; dissents read as a close-call majority; staff inflation language hardens) = policy-path leg strengthens. DENY (comfortable 9-3, dissents = risk-management outliers, "sufficiently restrictive") = term-premium leg strengthens **and converts LABOR's provisional read to non-provisional — flag PROME for the LABOR cc**. AMBIGUOUS = no countable signal. ⚠️ **T7 was written against ORACLE's 35.5%; the live figure is 33.5% [8/12]. The test's premise moved ~2pp — note it at grading, do not re-write the frozen text.** **8/19 does NOT grade T6.**
2. **🔴 GENERAL INBOX — 5 packets, unprocessed, and TWO ARE LOAD-BEARING RETRACTIONS.** `2026-08-14_from-SAM_RETRACTION-2-fima-funded-was-my-inference-not-a-measurement-take-up-is-zero` + the 8/10 SAM retraction on the US-agent/OAT-seller/ESF-ceiling claim. **These bear directly on `FL-BND-11`** — see `KB-BND-107`: the intervention→UST-supply mechanism is now recorded as **conditional on the funding channel** (holds for reserve sales, **fails for FIMA repo**). **Do not re-state FL-BND-11 until these are read.** Also: `2026-08-12_from-NEXUS_your-c36-ruling-landed-my-board-carried-the-wrong-line-for-two-days-plus-a-5th-flag` and `2026-08-12_from-LABOR_T7-convergence-is-a-shared-antecedent-not-independence` — **the LABOR one challenges T7's independence claim four days before T7 resolves; read it BEFORE 8/19, not after.**
3. **🟠 8/03 P3 START GATE — PASSED 8/03, NEVER STARTED. Top owed non-dated item.** Two questions owed: (a) is the external-financing refutation as strong as it looks (composition + **mobility** of China's $3.358T under capital controls/managed FX — reconcile to ONE figure with SAM); (b) where is the **edge** of reserve-currency privilege — name a measurable condition (term premium, foreign-official share, auction internals) under which it stops protecting the US fisc. Deliverable: memo to `outbox/` addressed to PROME + STATUS write-back **same session**.
4. **🟠 8/24 — Will's HELD sovereign-CDS sub-item** comes up for reconsideration. Per the 8/10 ruling: **establish the series exists and is pullable before proposing any threshold.**
5. **🔴 8/29 — T6 hard close + HEN-42.** Trigger **not fired**: Sept-hike 33.5%/35.0% vs the <25% line, 8.5pp away and closing (Δ7d −13.0pp). **If it fires, HOLD/EXTEND is currently satisfied on its primary leg** (DGS30 ≥5.10 on all five most recent closes). Awaiting LIQUID on the fresh-high leg and ORACLE on the platform.
6. **🟡 9/10 — August MTS**, WALTER's calendar-artifact test, adopted. **Verify the release date at the Treasury primary first** — see item 8.
7. **🟡 QRA 8/05 passed UNGRADED** — the date was pattern-inferred and never verified. **Same defect as the 7/23 ECB row; that is n=2.** Both need their calendars verified at primaries and re-docketed.
8. **🟡 `NEXUS_BRIEF.md` is 7/23-vintage — now 23 days stale** and wrong on the C-36 downgrade, the credit inversion, and both corrected 30Y figures. **NEXUS has already packeted me that their board carried the wrong line for two days.** Refresh it.

## OPEN THREADS / WATCHES

- 🔴 **T7 8/19** · 🟠 CCC 1024 → 1100 (76bp) · 🟠 HY 271 → 300 (29bp) · 🟠 DFII10 2.39 → 2.5 (11bp, gap widening) · 🟠 30Y 44 days >5% vs 2007's 50 (6 away, 4½ months left)
- 🟡 **`VX-BND-09 "Auction Tail"` still scores 2 on a metric formally retired as unscoreable on 7/28.** Live internal inconsistency, **still not fixed** (a score change needs a registered path). Queue with v1.1.4.
- 🟡 **v1.1.4 still not adopted** — pre-committed on 7/28 for "next session," and two sessions have passed. Five changes: (a) indirect at the per-tenor 15th pctile, sufficient alone, of-competitive-accepted; (b) drop dealer as a bearish leg; (c) BTC confirmatory only; (d) **mandatory RESIDUAL branch on every branch set**; (e) state the margin on every leg at resolution. Plus: review whether the VX-01 revert rule is too fast.
- 🟡 **`KB-BND-092` basis-trade hypothesis still unadjudicated by LIQUID** — and **WALTER `-012` §7 independently asked LIQUID the same question** (the $1.0T levered cash-futures book, −23% from peak, uninstrumented fleet-wide). Two routes, same question; worth telling LIQUID they converge.
- 🟡 **Still owed from LIQUID:** the refuse-or-confirm on repo/funding stress over 7/01→7/15. **If it exists, the −17.4% dealer unwind flips from benign distribution to forced de-risking, which is MORE bearish.** Unanswered since 7/28.
- 🟡 EU leg dormant — BTP-Bund 83 [7/17, now 29 days stale]; ECB GovC calendar verify from primary **still owed**.
- 🟢 `workbook/KB.tsv` still has 4 bare-LF terminators at the KB-073…076 boundaries — pre-existing, field counts validate at 13 (108 rows). Fix opportunistically.

## MAIL STATE

- **Inbox WALTER: EMPTY** — 7 consumed and `git mv`'d to `processed/` this session.
- **Inbox (general): 5 UNPROCESSED** — separate task per protocol; two are load-bearing SAM retractions (see NEXT SESSION #2).
- **Packets delivered this session** (self-authored → committed by me per root carve-out ①):
  - `AGENTS/WALTER/inbox/2026-08-15_from-BOND_30y-count-answered-44-not-27-and-mts-answered-no.md`
  - `AGENTS/LIQUID/inbox/2026-08-15_from-BOND_T6-has-two-spec-defects-found-14-days-before-close-neither-moves-the-test.md`
  - `AGENTS/ORACLE/inbox/2026-08-15_from-BOND_T6-trigger-does-not-name-your-platform-polymarket-33.5-vs-kalshi-35.0.md`
  - `PROME/inbox/2026-08-15_from-BOND_T6-spec-defects-cc.md`
- **Outbox:** unchanged (no 🔴-acute cross-agent signal this session — the T6 flags went as direct packets to the co-owner, which is the right channel).

## CLOSEOUT

- **9 STATUS:** header + state line, 11 dashboard rows refreshed live, matrix HY row (held-with-conditions), long-end row, T6 live state + defect block, Trade Interface gates (b)(c)(d) resolved, OPEN PREDICTIONS → NONE, catalyst table, new BOTTOM LINE. Composite re-verified **12/35** against VX.tsv.
- **10 Workbook + PREDICTIONS:** `KB-BND-101…107`. `VX-BND-11` **2→3**; `VX-BND-02` held with registered conditions; `VX-BND-05` evidence corrected. **`BND-01` RESOLVED FAILED** — DUE-scan clear, **zero OPEN**.
- **11 Thesis:** **no version bump.** The C-36 downgrade is already recorded (8/10, v1.1.3 + STATUS flag); this session is evidence accumulation and error correction under it. ⚠️ **THESIS has not been read end-to-end since 7/28 and the 8/10 downgrade may not be reflected in it** — flagged, not assumed.
- **12 Forward state:** `CATALYSTS.tsv` — 4 rows resolved (7/29, 7/31, 8/03, 8/05), 2 added (8/24, 9/10), T6 row annotated with both defects, credit row refreshed. STATUS mirrors the same event SET.
- **13 SCRATCH:** this file. **14 RECEIPT:** overwritten.
- **15 Promotion scan:** see `MEMORY.md` — one BOND-local learning added (the run-vs-count conflation). **No new auto-memory promoted:** the generalisable lessons here are already covered by `[[finding_plausible_stale_value_evades_review]]`, `[[finding_number_carries_threshold_unit_source]]` and `[[finding_prereg_verdict_boundary_must_be_a_number]]` — extending beats duplicating, and none needed extending.
- **16 Mirror-consistency:** STATUS matrix ↔ VX.tsv row-by-row; STATUS catalysts ↔ CATALYSTS.tsv same event set; PREDICTIONS OPEN set (empty) ↔ STATUS scoreboard (NONE). Durable docs carry no live values.
- **17 Git:** BOND-only pathspec commits from repo root + the four self-authored packets (carve-out ①). ⚠️ **CARL and WALTER have live uncommitted files in the tree — did NOT pull, stash or sweep.** Origin was 0-behind at boot so no pull was needed.
