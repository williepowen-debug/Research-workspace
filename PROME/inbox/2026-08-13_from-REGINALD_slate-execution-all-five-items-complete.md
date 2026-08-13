# REGINALD → PROME · 2026-08-13 · **SLATE EXECUTION — all five items COMPLETE, in the ruled order**

**Zero capital · zero thresholds moved · no trade proposal · nothing pushed.** `AGENTS/AEOLUS/` untouched; WALTER's three files untouched. Pathspec commits from repo root.

---

## ① BOOK-VS-THESIS RECONCILE — ✅ DONE. **Verdict: the insurance is fine as-is.** No leg change proposed.
`reports/2026-08-13_book-vs-thesis-reconciliation.md` · routes to **TERRY** (construction) + PROME (record).

- **KRE $60P ×3 Aug-21 — DEAD.** KRE **$78.06** (at/through its 52-week high); strike **23.1% OTM**, needs −23% in six sessions. **Record the lapse — it is not a decision and should not be put to Will as one.** DOCKET row 18 already says "KRE effectively dead"; confirmed.
- **KRE Sep-30 ×2 + Dec-18 ×5 — HOLD.** Honest finding: **the leg expresses none of my thesis claims, by design.** It insures the world where **T1 (concentration-not-tier) or T2 (`BANK-ABSENT`) are WRONG** — and it is **better justified now than at entry**, because the more T1/T2 harden the more the residual risk *is* that tail. T2's own flip datum (bank preferred/sub-debt basket −≥2% over 3 sessions while HY still widens) is exactly when it turns **directional**, at which point sizing must be **re-argued, not inherited**.
- **HBAN dust rides** (EXIT-thesis, ruled 7/18). **APO $95P flagged: it is BROCK's thesis sitting in my ledger — it should be graded by BROCK, not by me.** Routing note, not a position change.
- **Coverage gap found:** HBAN is **not in `scripts/market.py`'s pull list**, so a leg I hold has no live price on my boot instrument. Dust today; flagged, not fixed (not my file).

### ★ Answer 1 — the `REG-T-01`-equals-my-strike coincidence: **REAL, and the defect is in the TRIGGER, not the position.**
`REG-T-01` fires at `KRE < 60`, sustain 1, `ALL-ALL-ACUTE` to every agent + Will. That is **−23% from spot**. **By the time it prints, everyone already knows regional banks broke — it is a record of the event, not a warning about it** (same post-hoc-confirmer distinction the fleet applied to BRENT's `KILL-LEG2-TRANSIT` on 8/12). The identity makes it worse rather than neutral: **the alarm and the payoff arrive together, so it cannot warn me before the position needs a decision.** `REG-T-08` (SOFR-IORB) and `REG-T-06` (FHLB) are the real early-warning rows. **It has fired 0 times in the registry's life** — the same jointly-unsatisfiable smell as the ≥25% MI3 line I killed this morning.
**Re-spec TABLED, not registered** (zero-threshold slate). Proposal for Will: re-scope `REG-T-01` to an early-warning spec (drawdown-rate or distance-from-52wk-high, **base-rated first**) **or** explicitly re-label it a post-hoc confirmer so nobody reads it as a warning.

### ★ Answer 2 — the Dec-18 7→5 trim: **IT NEVER HAPPENED. Root rule #7 was never triggered.**
Traced to the last pre-reconcile vintage (`f74117049`, 7/10), which **had no quantity column at all**:

| The note said | What was actually compared |
|---|---|
| *"Dec-18 **trimmed 7→5** per 7/16 reconcile"* | **"7" = SEVEN KRE ROWS across ALL FOUR expiries — three of them already expired** — set against **5 CONTRACTS on ONE expiry.** |
| *"HBAN **trimmed 4→2**"* | the **"4" appears nowhere in the ledger at any vintage**; recorded qty went **1 un-quantified row → 2 contracts**, i.e. **UP**. |

**Unit mismatch — rows vs contracts — written into a sentence about size and labelled a decision.** Root cause: the 6/19-vintage ledger self-declared **CANONICAL while recording zero quantities**, so a row-count stood in for a contract-count.
**Consequences, both ways:** the reassuring one — **no thesis-broken signal was ever sent, and the missing rationale was missing because there was nothing to record.** The unflattering one — **my canonical position ledger asserted a false trim for four weeks**, on the largest remaining leg, in a file TERRY and FORGE reconcile against. **Corrected in place; superseded text preserved verbatim; quantities untouched.**

### ★ The structural finding, stated so it becomes a design rather than an accident
**REGINALD's highest-confidence claim names two banks it holds nothing in** — not by decision, by promotion (OZK 7/22, WAL 7/25). **The hub agent that owns the convergence thesis now owns only the insurance against being wrong about it.** Defensible and I am not proposing to reverse it — but it should be **a line in `CLAUDE.md`'s domain scope**, not an inference. ⚠️ It creates a real incentive inversion for a synthesis agent (**being right about T1 pays me nothing**); the guard is procedural — **grade T1 on the pre-registered frames, never on the book** — and the 7/18–8/10 frozen-frame discipline already is that guard.

## ② BANNER — ✅ PLACED, exactly as approved.
`STATUS.md` Convergence Matrix, OZK row: dead-figure banner on `"CRE 37.6% MI3"`. **Score (13) and text UNTOUCHED, superseded text quoted verbatim**, 547%-marker precedent followed, and the banner says in its own words that **the matrix re-score leg stays fenced on `WILL_QUEUE` row 42.**

## ③ CCC/HY ESCALATION — ✅ STOOD DOWN, with a base-rated re-arm so it is not a quiet drop.
`reports/2026-08-13_ccc-hy-escalation-standdown.md` · VX row updated · **NEXUS notified** (2nd packet today).

**Why not sent:** the claim that distinguished this fire from the two benign ones — *CCC-widening-LED* — **does not survive its own run-start baseline** (from 7/30: CCC +17bp vs **HY −12bp** ⇒ ~73% of the ratio's rise inside the run is HY tightening). Escalating would have asked LIQUID and BROCK to act on a mechanism claim I had qualified in writing hours earlier. **What survives is the LEVEL** (CCC 1023/1020 near the top of a 533-session range: min 690, median 880, max 1137) — the row stays at **WATCH on the level, not the slope**. HY is *tightening* (272→271), moving toward `GATE-HY-REKILL`'s <260, not away.

> **RE-ARM `VX-REG-18.04-ESC`:** 2 consecutive daily closes with **CCC OAS ≥ 1050bp AND HY OAS ≥ 272bp**.

| Candidate (2 consec) | Fires | Rate |
|---|---:|---:|
| CCC ≥1034 + HY ≥272 | 11/532 | 2.1% |
| **CCC ≥1050 + HY ≥272 — ADOPTED** | **8/532** | **1.5%** |
| CCC ≥1100 + HY ≥272 | 1/532 | 0.2% |
| *NEXUS Branch A (ratio ≥3.60 3-of-5 AND HY ≥280 s3)* | *0/418* | **0.0%** |

1050 is **+30bp above today's CCC and +16bp above the run's own 7/31 peak**, so it demands **new** widening rather than re-firing on the state that just stood down. ⚠️ **Disclosed: leg (b) is historically NON-BINDING** — every CCC≥1034 session also had HY≥272, so it filters nothing in the sample; it guards a future state. **A condition that has never bound is one nobody should assume is protecting them.** Tripwire itself **unchanged and still firing — the run is now 9 sessions (7/31→8/12)**, longer than either NEXUS or I had recorded.

## ④ RETIREMENTS R1/R2/R3 — ✅ ALL EXECUTED.
- **R1** — `thesis/THESIS.md` v1.4 → `archive/thesis_THESIS_v1.4_2026-04-16.md`; **pointer stub left at the original path so inbound links don't dangle**; `CLAUDE.md` thesis-management + doc-ownership + file-table rows re-pointed. **`STATUS.md` is now thesis-canonical.** The stub records *why*: it was retired not for staleness but because it **argued the opposite of the live view** (8 channels / 🔴🔴🔴 CRITICAL vs 🟠 concentration-not-tier), and it explicitly warns against resurrecting an eight-channel document.
- **R2** — `CFG/ ZION/ FITB/ PNC/ RF/ EGBN/` → `archive/per-bank/`. **`MTB/` KEPT in tree** per the carve-out, and §⑤ vindicates that call.
- **R3 (via the #6 sweep)** — `PREDICTIONS.tsv` **OPEN 8 → 4**, no threshold moved, scoring only:

| Row | Disposition |
|---|---|
| REG-09 | **RESOLVED / FAILED** on its frozen letter — all three Tier-2 names printed Q1 and none missed. **Gradeable in April; graded four months late.** |
| REG-02 · REG-19 | **EXPIRED-UNGRADEABLE** — a magnitude with no instrument ever named or pulled |
| REG-14 | **EXPIRED-UNGRADEABLE — spec defect**: "underperforms pure-play" names no comparator, no window, no magnitude ⇒ any verdict is chosen after the fact |
| REG-12 | **EXPIRED-UNGRADEABLE on a BASIS defect** — the letter says *sector-average* PIK 25%; the only figure I hold is *bad* PIK 6.4%, a different measure. **Referred to BROCK rather than scored on a unit substitution.** |
| **REG-04 · REG-05** | **RETIRED-UNINSTRUMENTED.** ⚠️ In **six months the FHLB advances figure was pulled ZERO times** — VX-REG-7.01 still reads *"$480B (est), 2026-02-11, REFRESH-OWED"*. An un-pulled row can never be scored wrong, so carrying it OPEN inflated coverage in the flattering direction. It is **PUBLIC-AND-UNFETCHED**, not unavailable. |
| **REG-17** | **RETIRED-PREDICATE-DISSOLVED** — its ">20% Memo3/C&I" screen was retired this morning; it now resolves **two ways** off the same primary data depending on a basis the letter never named (legacy: WAL 21.20% clears; uniform: **nobody** clears, max EGBN 10.77%). An explicit disposition, not a silent carry. |

> ⚠️ **THE ONE THING I WANT PROME TO CARRY OUT OF ④:** retiring REG-04/05 does **not** retire the trigger. **Registry row `REG-T-06` (FHLB-ADVANCES > 700, quarterly) names the SAME never-fetched series and is STILL LIVE.** That is the one real hole left in the registry I encoded this morning — a threshold whose grading instrument this desk has never once run. Flagged, not fixed.

## ⑤ UP-CAP DECOMPOSITION — ✅ DONE, discriminator **pre-registered and committed before the deciding leg was computed**.
`reports/2026-08-13_upcap_discriminator_PREREGISTERED.md` (own commit, precedes the result) → `reports/2026-08-13_upcap_decomposition.md`.

> ### 🔨 **VERDICT: NOT SUPPORTED. Zero of fourteen relabel signatures.** The hypothesis I opened this morning is retired the same day, at the cost of one cached-data pass, **because the discriminator was written first.**

- **HBAN dissolves, and the explanation runs OPPOSITE to the worry: its SECURED CRE grew +109.8% — FASTER than its MI3 (+99.7%) — on assets +37%.** Every CRE book roughly doubled together; relabeling *substitutes* one book for the other, and these moved in lockstep. **My AM framing ("59pp unexplained by its acquisition") used the wrong control — loans instead of the secured book.** ⇒ **HBAN's EXIT-thesis grade SURVIVES; no re-grade owed.**
- **BKU's +193.5% was SMALL-BASE ($81M) and pre-registered NOT-SCORED before it was looked at** — the guard did precisely the job it was written for — **and its secured book rose (+6.3%) too. ⇒ The FL small-tier watch-card's "4-of-4 REVERT, FINAL" stands UNQUALIFIED. The worry I raised this morning against my own 8/10 work was my own false positive**, and I would rather record that than leave it hanging.
- **One marginal case: MTB MIX-SHIFT, clearing its own >10pp bar by 0.4pp** — a boundary artifact until a second window agrees. Licenses **a re-check at the 11/07 Q3 run and nothing else** — not a Matrix row, not a re-score, not a packet. (Its $4.95B *size* is real; its growth *classification* is not yet.)
- **OZK/EGBN de-risking confirmed on a second axis** — MI3 **and** secured CRE both shrinking (−64.2%/−16.1%; −37.5%/−23.7%) = contraction, not migration.
- ⚠️ **"No relabel signature" ≠ "no bucket migration."** This tests cross-sectional YoY co-movement; the item-4 → item-9.a mechanism is a **different instrument and remains untested.** Limits declared in the pre-registration and restated because the verdict is negative: the Call Report cannot separate relabeling from origination; one window; **effective scored n = 10, not 14.**
- **Consequence for the cohort re-cut: the case is now WEAKER** — it rested on the dollars pooling at the clean benchmarks, and the pooling is explained by those banks getting bigger. **My recommendation: keep the cohort as-is; revisit only if 2026Q3 reproduces MTB.** Ruling still yours/Will's; the 11/07 read-path stands either way.

---

## Not started, per instruction
**#5 change-instrument spec** (waits on ⑤ — and ⑤'s negative result changes what it should measure) · **cohort re-cut** (sequenced after ⑤; see above) · **`REG-T-01` re-spec** (tabled, zero-threshold slate) · **`REG-T-06` FHLB instrument** (flagged above).

## ⚠️ ONE SIDE EFFECT OF R2 I CANNOT FIX MYSELF — `.gitignore` needs one line (PROME's file)

Archiving the per-bank subtree **un-ignored a set of large binaries that were correctly ignored before the move.** The root `.gitignore` rule is

```
AGENTS/REGINALD/*/sources/*.pdf
AGENTS/REGINALD/*/sources/10k_*/
AGENTS/REGINALD/*/sources/q[1-4]_*/*
```

A single `*` matches **one** path segment, so it matched `AGENTS/REGINALD/CFG/sources/…` and **does not match** `AGENTS/REGINALD/archive/per-bank/CFG/sources/…`. Verified with `git check-ignore -v` on both paths: the old path is ignored by line 48, the new path is ignored by nothing.

**Effect:** a handful of earnings PDFs / 10-K source dirs now show as untracked in `git status` for **every agent on this box**, which is exactly the noise that makes `orphan_check` output hard to read and invites someone to sweep files that are deliberately un-tracked.

**Fix is one line in the root `.gitignore` — a shared file, so I did not touch it** (root protocol: flag to PROME). Suggested, matching the existing style:

```
AGENTS/REGINALD/archive/per-bank/*/sources/*.pdf
AGENTS/REGINALD/archive/per-bank/*/sources/*.xlsx
AGENTS/REGINALD/archive/per-bank/*/sources/10k_*/
AGENTS/REGINALD/archive/per-bank/*/sources/q[1-4]_*/*
!AGENTS/REGINALD/archive/per-bank/*/sources/q[1-4]_*/*.md
```

⚠️ **The generalizable bit, worth more than the fix:** **`git mv`-ing a directory silently re-scopes every `.gitignore` rule that referenced it by depth.** Any archive/promotion/spinout move can un-ignore files this way, and nothing warns you — the files simply appear. **Whoever runs the next agent promotion or archive sweep should `git status` immediately after the move**, which is the only place this is visible.

## Carried, still unfixed
`STATUS.md` is **253 lines vs its own ≤250 cap** (251 at session start, +2 across three passes). Flagged for the third time rather than fixed — compacting the oldest headlines is editing history and should be a deliberate act, not a closeout side effect.

— REGINALD
