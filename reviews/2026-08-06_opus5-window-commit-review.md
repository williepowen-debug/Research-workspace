# Commit review — Opus 5 exposure window (8/4 22:27 → 8/5 23:14, 50 commits)

> **DISPOSITION 2026-08-06 (Will-directed, this branch):** Tier A mechanical fixes committed — R1 (8/4 proxy restored to queue row 26 / commission packet / SCRATCH / GATES chain, + DOCKET row 20 window annotation), R4, R5, R7, M1, M2, M3, M4, M6, M7, and the weekday minors (VIOLET brief, FALCON 8/2 report, HEARTBEAT Am.#1, RED packet). Tier B owner packets dispatched: FALCON (R2 window re-derivation), LABOR (R6 + Brier minors), BRENT (R3 basis ruling), TERRY (RISK_RULES:119). Tier C proposal packeted to PROME (claim_check scope, ratification_check, closeout stamp sanity). **M5 RESOLVED NOT-A-DEFECT:** all four hashes (`84592462`, `74c426916`, `bed7a3180`, `962870545`) verify as real commits from a deepened clone — shallow-window artifact; the "describe, don't re-pin" practice point stands. Not fixed by design: QQQ −0.90% note (stale market prose, prices-must-be-live rule), commit-message nits (immutable history — documented here), F2/F8-adjacent pre-existing items (routed in packets).

**Reviewed:** 2026-08-06, on branch `claude/review-recent-commits-f8lwo2`.
**Scope:** all 50 commits in the shallow-clone window (root `2fcdf5d` 8/4 22:27 ET → HEAD `1b97969` 8/5 23:14 ET). Session notes confirm these sessions ran on Opus 5 1M; LABOR/VIOLET commits carry `Co-Authored-By: Claude Opus 5` trailers, `a1a6c17` carries Fable 5.
**Method:** four parallel review passes (BRENT · PROME coordination · roster taxonomy · LABOR/VIOLET/FALCON) + mechanical checks (`memory_index_check --strict`, `claim_check --check weekday`, hash resolution). BRENT's EIA figures were verified **externally against live eia.gov** (highlights.pdf wk-7/31 + dnav Cushing series).
**Caveat:** this clone is shallow (depth 50; `master` separately rooted 7/31→8/1). Pre-window hashes cannot be resolved here — absence of a hash was never counted as a defect on its own.

## Bottom line

**No hallucinated market data found. No CRITICAL findings.** Every externally checkable number is accurate to the digit; arithmetic recomputes exactly across all four clusters; the load-bearing structural claims (roster 30/30, gate-merge threshold preservation, HANDOFF byte-identity, BIN-A fidelity) all verify. The defects that DO exist are state-consistency failures: a prior run erased from coordination surfaces, same-commit internal contradictions, header/label slips, and summary counts that don't match their own diffs. One cluster (R1) is decision-relevant and should be fixed before the FALCON 8/6-8/7 real session ratifies.

---

## HIGH-PRIORITY (decision-relevant — fix before next reads)

### R1. The 8/4 FALCON proxy run is erased from every 8/5 coordination surface — owner PROME
*Found independently by two review passes. Borderline critical.*
Three proxy adjudications exist since FALCON's last real session: **8/2, 8/4, 8/5**. The 8/4 run is on the record — `AGENTS/FALCON/reports/2026-08-04_yanbu-leg3-repull-adjudication.md`, PROME's own `PROME/DOCKET.tsv` line 19 (`RESOLVED(EXECUTED 8/4 ~16:00 — FALCON proxy, Will-approved launch…)`), and the 8/5 report's own "NO-PRINT-PUBLISHED **2nd consecutive**" counter (which only counts if 8/4 was the 1st). Yet:
- `2285704` commission packet (`AGENTS/FALCON/inbox/2026-08-05_from-PROME_session-commission-…md` line 3 + item 4): "**two** proxy runs … yours to ratify", lists **8/2 + 8/5 only**.
- `f44e53e` `PROME/WILL_QUEUE.md` row 26: "proxy-run ratification (8/2 + 8/5)" and asserts "**FALCON did not run 8/4**, marked NOT-COVERED honestly" — both halves contradicted by DOCKET row 19.
- `1b97969` `PROME/SCRATCH.md` NEXT-SESSION item 2: "ratify the 8/2+8/5 proxy runs" — propagates into next boot.
- `1baaf6c` GATES FALCON-001 row: audit chain jumps 8/2 → 8/5, omitting 8/4 while carrying its "2nd consecutive" counter.
**Impact:** the commissioned real-FALCON session would ratify 2 of 3 runs; the 8/4 adjudication (fire-line restatement + window scheduling) goes permanently unratified.

### R2. FALCON relay-window rule contradicts its own evidence; window silently shifted — owner FALCON
`a1a6c17` (`AGENTS/FALCON/reports/2026-08-05_yanbu-leg3-recheck.md` §2 + outbox): "w/c-7/20 set relayed 4-8 days after **week-end** (7/24-28)" — but 7/24-28 is 4-8 days after the week's **start** (7/20); relays on 7/24-25 would precede the week-end (Sun 7/26) entirely. Applied consistently, the w/c-7/27 window is ~7/31-8/4 (already closing at write time), not "opens 8/6 … extend to 8/8-8/10." The 8/4 report projected "~8/5-8/7"; the 8/5 report shifted to "~8/6-8/10" without flagging the change. **Impact:** this sets when the missing print counts as overdue. Related: `PROME/DOCKET.tsv` Yanbu row (line 20) still carries the old `8/5..8/7` window while GATES/HEARTBEAT/SCRATCH carry `~8/6-8/10` — coherent-but-stale.

### R3. Leg T close-basis value now lives as two figures — owner BRENT
`d86e5d1`/`6938020` assert Jun-17 composite close T = **1.68%** ("the ratified close basis passes it at 1.68%"); three pre-existing canonical surfaces say **1.63%** (`AGENTS/BRENT/TRADE.md`, `LESSONS.md` #19, `LESSONS_INDEX.tsv`). Same metric, two live figures, discrepancy never flagged (likely 5m-bar last print vs daily close). Verdict unaffected (both PASS >1.0%), but this is the exact number a Will-ruled gate is calibrated against.

### R4. BRENT STATUS decision row invites re-presenting a declined deploy — owner BRENT
`AGENTS/BRENT/STATUS.md` (via `1475426`/`bb663f8`): ACTION STATE = "⛔ WILL DECLINED THE DEPLOY (8/4 eve) … No fill" but NEXT DECISION three rows down still reads "**Will: [Approve]/[Decline] the fill.**" A reader of the decision row alone re-presents what the decline rule forbids.

### R5. LABOR STATUS header contradicts its own matrix: "3 → 1" vs correct "3 → 2" — owner LABOR
`f5525d8` `AGENTS/LABOR/STATUS.md:2` says vector 3 re-graded "(3 → 1)"; the matrix row (line 40), summary (line 54), and `PUBLISHED.tsv` all say **3 → 2**, and the total arithmetic (36→34 = −2 = (3→2)+(4→3)) confirms 3→2. The wrong figure sits in the boot-loaded Last-Updated line — the most-read surface.

### R6. LABOR sign-error root-cause narrative is internally contradictory, and was propagated fleet-wide — owner LABOR
"Only **two** knowns / two free parameters" (commit msg `f5525d8`, `LESSONS.md` L-12, auto-memory, all four packets to PROME/HENRY/CARL/NEXUS, `NEXUS_BRIEF.md:6`) vs "only **3** were known, back-solved the 4th" (`STATUS.md:2` and `:4`). The numeric demonstration used in both variants only works with exactly **one** unknown, and it uses the corrected values that were not known at the time. The arithmetic shown is internally correct; the knowns-count is inconsistent across surfaces and within single sentences. Methodology record — worth one reconciled version.

### R7. LAB-06 still carried as live in two NEXUS_BRIEF spots the sweep missed — owner LABOR
`AGENTS/LABOR/NEXUS_BRIEF.md:25` ("tilts toward the LAB-06 breach; ISM Aug 3 is the graded test", with stale ISM 49.7) and `:34` ("LAB-06 REPRICED 80% → 20% … tests ~Aug 3") + `:44` divergence bullet — while lines 6/33/73 of the same brief report LAB-06 RESOLVED ❌ 8/3. `c102678` struck line 73 only.

---

## MODERATE (consistency/audit-trail)

- **M1. Roster "~20 rows" figure fabricated** (`6a62940`, owner PROME): `AGENTS.md:24` "~20 rows against 30 live ACTIVE agents" and `PROME/ROSTER.md:33` "(20-row agent table)", propagated into `ACTIVE_DECISIONS.md` by `2e13869`. The table has **31 rows** (verified at the commit, its parent, and HEAD — wrong at authoring time). Also mischaracterized: the table isn't a subset of ACTIVE — it contains 3 non-ACTIVE names and omits only 2 of 30 (PROME, WALTER).
- **M2. Same-commit contradiction on TERRY/ORACLE class** (`6a62940`): `AGENTS/_INDEX.md:29` lists TERRY and ORACLE among "service, review or trade-construction lanes rather than uniform domain owners", while the same commit's ROSTER rules both **DOMAIN ACTIVE** (ROSTER.md:82-83).
- **M3. BRENT closeout timestamps impossible under a "date-verified" badge** (`bb663f8`): SCRATCH/STATUS/NEXUS_BRIEF stamped "~03:0x ET ⏰ date-verified" while describing events from 11:31 AM and 14:53 ET; commit at 19:59 ET. Almost certainly a PM→AM slip, but it's on the canonical handoff surfaces.
- **M4. BRENT session-ID collision**: the 8/4 RAV session self-labels **session 4** in its artifacts but its closeout `1475426` titles surfaces "SESSION 5"; the 8/5 structure session (`bb663f8`) also closes as "session 5". SCRATCH history runs SESSION 3 → SESSION 5 with no 4. Two closeouts share one ID.
- **M5. Fresh hash re-pinning into decision surfaces** (`1baaf6c`, `2285704`, `b4b5094`): `84592462` (8/2 FALCON proxy) and `74c426916` (8/4 TERRY proxy) were re-pinned on 8/5; neither resolves in this clone. Shallow history means they may be real pre-graft hashes (NOT counted as fabricated), but `666921d` — same day, same author — records the exact lesson: "describe the run, don't re-pin a hash." Needs a full-clone check.
- **M6. NEXUS_BRIEF length line contradicts its own commit message** (`1475426`/`bb663f8`): file says "back INSIDE the provisional 100-line cap" at 122→125 lines; the commit message honestly says over-cap. The artifact is what NEXUS reads.
- **M7. ROSTER preflight pointers reference a moved file**: `PROME/ROSTER.md:6,:13` point at `PROME/inbox/2026-08-05_from-RAV_…addendum.md`, moved to `inbox/processed/` by `04569c2`. Durable copy exists at `AGENTS/RAV/runs/…`.

## MINOR

- Weekday labels: `AGENTS/VIOLET/NEXUS_BRIEF.md:3` "2026-08-05 … (Tuesday" — 8/5 is Wednesday (introduced by `08c1367`, still in tree). Pre-existing same class: FALCON 8/2 report "(Saturday)" and HEARTBEAT Amendment #1 "(Sat" — 8/2 was **Sunday**. RED packet (`659fafd`): "first close <280 since 7/26" — 7/26 was a Sunday, no print; last <280 close was Fri 7/24.
- QQQ day-change: `1b97969` SCRATCH + `memory/2026-08-05.md` "717.30 −0.90% [8/5]" vs PROME's own 8/4 close 725.14 → **−1.08%**.
- `f92d239` claims "12 defects fixed"; its diff contains 11 (the 12th is `c102678`, same timestamp).
- Mean-Brier propagation `0.293/0.233` (scoreboard + packets) is ~0.0015 off the fleet's own prior chain (expected ≈0.295/0.235); prior chain reconciled exactly. Low-medium confidence (unrounded per-row values could reconcile).
- "Pre-print decomposition **saved** 0.060 of mean Brier" (`595a600`, scoreboard) — under gate #14 the as-made 0.64 stays in the mean; nothing was realized-saved. Wording/sign confusion.
- `a384f8a` commit message byte figures off by 4 (121,148 vs actual 121,144; 299,696 vs 299,692) — measured before a final tweak.
- `0a3d87f` "NOTHING WAS DELETED — only moved": token-check shows zero numbers/dates/IDs/thresholds lost, but several prose blocks were condensed, not moved verbatim.
- `b4b5094` message "two hours after the OVERDUE annotation" — 13:20→15:50 = 2h30m.
- `2e32e0a`: file self-stamp "~23:15 ET" postdates its own commit (23:11).
- `d86e5d1`/`6938020` paraphrase "graded 5× with four verdicts" — a PASS/FAIL test has ≤2 distinct verdicts. **Adjacent pre-existing** (route to TERRY): `AGENTS/TERRY/RISK_RULES.md:119` says "three FAILs and two PASSes" but its own values vs the ≤33.0 line give two FAILs / three PASSes.
- `8f330aa` "fourth structural move against interest **in two days**" — VIOLET's source packet has all four on 8/4 (one day).
- `2e13869` ACTIVE_DECISIONS row: "Nothing is left disclosed-but-unreconciled" beside a Next cell still carrying the open third-mirror ask (closed later by `8f6a04b`).
- Pre-existing, observed in touched files: BRENT `TRACKER.md` body prose still carries the retracted "+0.7% YoY [EST]" relay figure (correction lives in LIVE LINE #6 + STATUS:138); SPR −3.80M vs −3.7M banner rounding.

## FALSE POSITIVES (checked, not defects)

- `claim_check` flag "Sun 8/1" in `HEARTBEAT.md:94` — actual text is "Sat-Sun 8/1-2", correct range labeling.
- **HY thresholds are NOT contradictory**: "<260 ×2 closes" (GATE-HY-REKILL) and "<280 sustain" (FT-01 re-arm / X1 leg) are two distinct registered gates; every surface attributes each threshold to the right gate.

## VERIFIED CLEAN (the reassurance list)

- **EIA wk-7/31 re-pull (`61fd3fd`): externally confirmed to the digit** against live eia.gov — crude 406,987/404,508; Cushing 20,955/18,599/19,370; SPR 304.8/307.7; util 96.5%; gasoline 209.7 (−1.6M); distillate 107.2 (−3.5M); 4-wk product supplied 8,966 vs yr-ago 8,912, EIA's own "up by 0.6%" matching the +0.60% headline; GASREGW $4.079 (8/3). The 8/5-morning "wk-7/31 not yet retrievable" record also reads accurate.
- **HY routing wave numerically airtight**: series 287/284/285/278/273; 13bp above <260; tier stack BB 163 / B 288 / CCC 1019 identical across all packets + HEARTBEAT; all deltas exact.
- **Roster 30/30**: five classes sum 3+1+17+7+2=30, name-set exactly equal across ROSTER, root CLAUDE.md, the pre-split table, and RAV's buckets. Root-mirror edit (`0a1360b`) byte-identical to the approved DRAFT, no scope creep. RAV correction chain honestly recorded.
- **ISM Services correction (47.4 → 51.2)**: identical across every LABOR surface, packets, TSVs; all identities recompute ((55.4+55.1+51.2+54.3)/4 = 54.0).
- **Gate v2→v3 merge (`58a06dd`/`a384f8a`/`6938020`)**: every threshold/control from both sources preserved (58.6245 = 68.97×0.85 exact; all gate arithmetic recomputes); Leg T v6 implements the proposal on every number; TERRY packet consistent (F6 paraphrase aside).
- **Shallow-clone false-fork verdict (`0beb1c2`/`e132940`): reasoning sound** — corroborated by this very review environment being a depth-50 shallow clone with the same symmetric-ahead/behind artifact.
- **BIN-A record faithful**: DOCKET summary + ack reproduce VIOLET's withdrawal (p=0.27/p=0.31, n=7,726/29.6y, 2.25×→1.20×) without distortion.
- **HANDOFF rotation byte-identical** (12,120 bytes, diff-clean); TSV column discipline uniform; all in-window cross-references resolve; carve-out compliance clean on every cross-dir commit (packets ①, shared-log ②, auto-memory ③ all properly used); `memory_index_check --strict` = 375/375, zero orphans, index at 68% of byte cap.
- **VIOLET `08c1367`**: exactly 4 mechanisms as claimed; all cited numbers recompute (MOVE −6.58%≈−6.6%, margins, 22-row TSV, +27 history lines, 93% loss figure).
- **FALCON 8/5 report internals**: vessel names/dates consistent everywhere; 7 vintage rejections = exactly 7 table rows; dhow-≠-tanker letter reasoning identical across surfaces.

## Pattern read (what "Opus 5 issues" actually look like here)

The model's **analysis layer held up**: market data, arithmetic, threshold preservation, and faithful representation of other agents' work were uniformly correct, including under external verification. The failure mode is **bookkeeping under fan-out**: when one fact must be restated across many surfaces (headers, queues, commission packets, next-session lists), Opus 5 occasionally dropped a prior event (R1), let a header contradict its own body (R5, M6), reused/skipped session IDs (M4), asserted counts without re-deriving them (M1, "12 defects"), and slipped AM/PM and weekday labels (M3, minors). None of it fabricated market data; nearly all of it is the "restated state drifts from canonical state" class the repo's existing checks (consumer_check, claim_check, state tokens) were built for — the instances just sat outside those checks' current scope.
