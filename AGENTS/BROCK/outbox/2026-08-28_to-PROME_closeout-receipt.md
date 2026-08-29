# BROCK → PROME · 2026-08-28 ~21:0x ET · **CLOSEOUT RECEIPT — full protocol run, session ended**

**Authority:** Will, via PROME — *"close out SHADE and BROCK, direct them to do their close out procedure."* Every step below was run **at this closeout**, including steps already run at an earlier touch, because the point of re-running is re-verification. **Not pushed** — PROME's push-train sweeps.

---

## A. Protocol steps, each with its result

| Step | Result |
|---|---|
| **6. STATUS write-back [ALWAYS]** | ✅ Re-stamped **~21:0x**; header carries both RAV corrections so a boot reader meets them before the claims. **32,535 B, READ-CAP 0**, 167 lines (target ≤250) |
| **7a. Predictions disposition [ALWAYS]** | ✅ **NO row is DUE** — nearest is BRK-02 on 9/30. **BRK-27 CLOSED** earlier tonight (`RESOLVED-FALSE-LETTER`; it had sat PARTIAL 8 weeks past a window that cannot re-open). **BRK-06 RE-ARMED with the null recorded** rather than left silent. **BRK-30 annotated** with the Q2 date-model correction. BRK-02/25/26/32/11 notes carry this session's counter-data |
| **7b. Workbook write-back** | ✅ **KB +10 rows this session (215-225), NF=13 clean.** VX +1 new / 2 refreshed · FLOW +1 · PREDICTIONS 6 rows annotated · PC_REDEMPTION_REGISTER refreshed to Q2 primary · **PUBLISHED.tsv created** (7 metrics) |
| **8. Forward-state** | ✅ CATALYSTS: CRMT **9/1→9/7 corrected**, +7 forward rows covering **BCRED 8/31 expiry · SC TO-I/A 9/2-9/8 · CRMT 9/4·9/7·9/8·9/9 · X1 review 9/15 · X1 arming test**. 🆕 **One rotting row GRADED — see §C** |
| **9. Research detail placed** | ✅ `domain/sources/2026-08-28_SESSION_CATCHUP_ADJUDICATIONS.md` (20,435 B) + `..._BCRED_Q2_READ_AND_FIRST_BRANDS_SWEEP.md` (14,204 B); verbatim pre-rotation STATUS in `archive/` (`crc32=089f9ff5`) |
| **10. Cross-agent signals** | ✅ **Already routed — listed in §D, NOT re-sent** |
| **11. Promotion scan** | ✅ **LESSONS #28-30 added** (below). **Auto-memory: one written earlier tonight** (`finding_relative_threshold_cannot_be_graded_by_a_one_sided_instrument`). **Nothing new written at this closeout** — the `read_ledger` phantom-metric finding is already with DAEDALUS, and #28-30 are BROCK-specific pattern work, not fleet-transferable in the form they took |
| **11b. Memory-index check** | ✅ `--strict --slug finding_relative_threshold_cannot_be_graded_by_a_one_sided_instrument` → **passes** |
| **12. Git [ALWAYS]** | ✅ Pathspec-only, `BROCK (orch):` subjects, **no push**, **no `--amend`**, **no `git add -A`** |

**Instrument results:** `read_cap_check` **✅ READ-CAP 0** · `orphan_check` **✅ clean** (only other desks' live in-flight files) · `corrections_boot_check` **✅ 0 unreceipted** · `claim_check --check weekday` → 1 flag, **verified false positive** (2026-08-11 *is* a Tuesday; the tool infers 2025) · pre-commit `git status -- AGENTS/BROCK/` + `git diff --cached --stat` run before each commit.

**`consumer_check`, both directions, for tonight's supersessions ($30.8/$37.9M → $17.5/$22.5M):**
- **`--self`** → ✅ **clean.** 97 files scanned; no BROCK surface carries a superseded value unqualified.
- **`--from-ledger`** → **123 🟠 candidates, ZERO certified-stale. No packets owed.** ⚠️ The two 🔴s from the earlier run were **adjudicated NOT stale** and are recorded in the ledger's own banner: PROME `DOCKET.tsv:183` is a **deliberately frozen** W3 kill line (re-basing it would destroy the test), and HENRY `MARKET_DATA.tsv:14` is a **correctly-dated history row**.

**Ledger nudge — `FLOW.tsv`, `VX.tsv`, `PC_REDEMPTION_REGISTER.tsv` behind; why-not, per the rule's own third option:** all three were **genuinely refreshed earlier tonight** (VX-BRK-021/-022 re-cut from 42d stale; the register taken to Q2 primary with a wrong-concept figure killed; FLOW-BRK-023 added). This closeout changed **predictions and calendar state, not transmission pathways or vector levels**. Refreshing them to clear a counter would be a pure hygiene commit that **re-arms the git-time staleness fallback for nothing** (`[[finding_hygiene_commit_rearms_the_staleness_lie]]`) and would make three ledgers *look* fresher than their content is.

## B. LESSONS added this session

**#28 — a correctly-caveated body does not protect a headline that claims past it**, and "limits stated" cannot catch it *because the limits are stated*. Both RAV findings were this shape. ⚠️ **Not my registered bias** — I spent the same session guarding too-easy-to-fire-bearish and even *withdrew* an over-concession. **Test added: read the bold clause alone, paragraph covered, and ask what a reader carries away.**
**#29 — a DIP mark is not a recovery estimate.** It embeds claim disputes, collateral and timing. When a price looks unusually informative is exactly when it is most tempting to read one clean proposition out of it.
**#30 — a dated catalyst row can point at empty space and still read merely "waiting."** See §C.

## C. 🔴 One rotting row graded at this closeout, and its date model was wrong

My calendar carried *"BCRED Q2 final repurchase satisfaction, ~8/13-8/17 window"*. **Verified at the filer history: BCRED filed NO SC TO document between 2026-06-04 and 2026-08-04.** The row was watching empty space. **The Q2 final was disclosed in the 6/4 SC TO-I/A — ~50% satisfaction on ~10% demand against a 5% design cap — independently confirmed on the BX 7/23 call.** ⚠️ **The defect was the DATE MODEL: I anchored on QUARTER-END; BCRED's tender results land ~28-34 days after the OFFER** (2/2→3/2 · 5/1→6/4 · 8/4→~9/2-9/8). **An un-fired row and a mis-pointed row look identical from the row.** The Q3 row (9/3) is built on the offer-date cadence for this reason — **re-verify the filer history ~9/2 rather than assuming.**

## D. Cross-agent signals ALREADY ROUTED — listed, not re-sent

| To | Subject |
|---|---|
| **LIQUID** ×2 | X1 wrapper half **ADJUDICATED NOT ARMED** (+ their KILL_MEMO "contested half" branch needs a re-word) · BCRED clears both `KB-LIQ-083` legs **from outside its perimeter — not a re-grade** |
| **SHADE** | Delaware Life = FHLBI's **#2 borrower, $4,963M / 12%**, flat to the dollar across two quarters |
| **REGINALD** ×2 | First Brands auction recovery **never established as a print** — close it RESOLVED-BY-SUPERSESSION · **WAL's $126.4M charge-off, and why it does NOT fire BRK-31** |
| **WAL** | Same charge-off, routed directly — WAL is its own desk since 7/25 and a cc in a title is not delivery |
| **OTTO** | First Brands sweep: **six holders not fifteen**, the DIP marks, and a **request for the perimeter** behind its "15 BDCs" figure |
| **RED** | Two confirm-or-supersede rows — one answered, one **honest cannot-confirm** (no rated-CLO-default screen; my silence is not corroboration) |
| **HANS** | `HANS-T-14` routing **ACCEPTED as cut** |
| **NEXUS** | `<270` re-eval result as an M-08 input, **with a caution filed against myself** |
| **PROME** ×3 | Round-1 memo · round-2 memo · the W3 frozen-threshold packet |

## E. THE THREE ENUMERATIONS PROME ASKED FOR

**① AWAITING WILL — exactly two, both already on WILL_QUEUE row 116 for the 9/4 batch. Nothing else.** ⓐ the `<260` thesis-kill spec observation (never reachable in its own 3-year sample: one sub-260 close in three years, longest run 1 session, 3-consecutive zero times); ⓑ the `PC_REDEMPTION_REGISTER` *"≥2 vehicles gated simultaneously"* escalation line (mis-specified — fires 7-fold on day one and double-counts the shared antecedent). **Confirmed: no third item. Neither was self-executed; both are thresholds and thresholds are Will-gated.**

**② DATED CLOCKS**
| Date | Item |
|---|---|
| **Mon 8/31** | BCRED Q3 tender EXPIRES — ⚠️ the expiry itself decides nothing |
| **Wed 9/2 → Tue 9/8** (median **Thu 9/3**) | 🔴 **BCRED Q3 final-results `SC TO-I/A`** — `accepted ÷ tendered`; **BRK-30 fires on <100%.** Re-verify filer history ~9/2 |
| **Fri 9/4 · Mon 9/7 (Labor Day) · Tue 9/8 · ~Wed 9/9** | CRMT standstill: liquidity test · filed termination date · first live business day after · the 10-Q that arrives **two days late by construction** |
| **Tue 9/15** | X1 DOCKET row 232 review — ✅ **already adjudicated; the row can close early** |
| **Wed 9/30** | **BRK-02 resolves** — binding constraint is the name set **awaiting PROME**, not the evidence |
| **Thu 10/15** | BRK-30 resolves |
| **before Mon 11/30** | ⚠️ **BRK-32's L2 weight needs RE-BASING** — 46.1% was struck on BCRED net assets of $45.04B; Q2 puts them at **$42.78B** |
| **standing, undated** | 🎯 **X1 arming test (b)** — wrappers fall more than managers **while HY widens CCC-led (ratio EXPANDING)**. ⚠️ Its decomposition leg is closer to satisfied than ever (CCC/BB 6.739, series max); **only the price leg is missing** |

**③ UNROUTED PROPOSALS IN MY TREE** — ⓐ the two WQ-116 re-specs above (proposed, not executed); ⓑ **OTTO owes the perimeter** behind its $237M/15-BDC figure — asked, unanswered, and the two counts stay unreconciled until it answers; ⓒ **a `PUBLISHED.tsv` header-order fix for `read_ledger`** — flagged to PROME, already with DAEDALUS, not mine to change; ⓓ **the row-to-footnote SOI parser** — needed by BCRED Pass 4 (non-accrual names), WALTER `-028` ask (a), and per-holder First Brands totals. **Build once, properly; three consumers waiting.**

## F. Honest gaps carried forward
**BCRED Pass 4 (non-accrual NAMES) NOT ESTABLISHED** — parse returned 23 issuers/69 loans against a stated 15/25, **failed its own validation, did not ship**; the migration test stays open. **WALTER `-028` ask (a)** (OBDC June SOI) not done — same parser. **Per-holder dollar totals for four of six First Brands holders** — same parser; the mark range rests on two holders and says so. **8/6 MFIC/FSK transcripts** not reached. **`SIG-W-20260828-048` deliberately UNCONSUMED** for the next live session, flagged at the top of SCRATCH.

## COMPLETION — BROCK — 2026-08-28 (closeout)
STATUS: ✅ DONE
CHANGED: AGENTS/BROCK/{STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, LESSONS.md, docket/CATALYSTS.tsv, workbook/PREDICTIONS.tsv}, this memo
RESULT: Full closeout run, all ALWAYS-tier steps re-verified. READ-CAP 0 (32,535 B), orphan clean, corrections 0 unreceipted, KB NF=13 clean, consumer_check --self clean and --from-ledger zero certified-stale ⇒ no packets owed. No prediction DUE; BRK-06 re-armed with the null recorded, BRK-30 annotated, BRK-27 already closed. Graded one rotting calendar row whose date model was wrong — BCRED filed nothing between 6/4 and 8/4, so the "~8/13-8/17" window watched empty space. LESSONS #28-30 added on tonight's headline-vs-caveat defect class. 14 commits this session, none pushed.
GAPS: BCRED Pass 4 names not established (parse failed validation); WALTER -028 ask (a), per-holder First Brands totals, and the migration test all blocked on one row-to-footnote SOI parser worth building once; 8/6 transcripts not reached; SIG-W-20260828-048 deliberately unconsumed for the next live session.
WILL_NEEDS: Exactly two, both already on WILL_QUEUE row 116 — the <260 thesis-kill spec observation and the PC_REDEMPTION_REGISTER escalation-line re-spec. Confirmed nothing else.
FOLLOW-UP: BCRED SC TO-I/A 9/2-9/8 (re-verify filer history ~9/2) · CRMT 9/7 · BRK-02 9/30 needs PROME's name set · BRK-32 L2 re-base on $42.78B before 11/30 · X1 row 232 can close early · OTTO owes its perimeter · LIQUID's KILL_MEMO re-word.
