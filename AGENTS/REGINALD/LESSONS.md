# LESSONS.md — REGINALD Mistake Patterns & Rules

*Read at boot. Learn once, prevent forever. This file is for verified mistakes that burned us — each with a prevention rule. For Will's working preferences and data source learnings, see `MEMORY.md` (Feedback + Findings sections).*

---

### [Data] — Verify Agent Data Against Primary Filings
**Mistake:** PSEC was reported at 35% PIK — actual was 8.6% per SEC filing. Consumer finance names (SYF, BFH, ALLY) were assumed stressed but SEC filings showed improvement.
**Rule:** Before any metric informs a trade, verify against the 10-K/10-Q. Agent research is a starting point, not ground truth.

### [Data] — NDFI Is Not What It Looks Like
**Mistake:** WAL's NDFI ($6.5B) was initially flagged as major risk. Reality: 68% is mortgage warehouse (0.08% reserves, near-zero losses), NO auto warehouse. Ex-mortgage only $4.3B in secured SPV structures.
**Rule:** Decompose NDFI by type before assessing risk. Mortgage warehouse ≠ auto subprime ≠ BDC lending.

> ⚠️ **FIGURES UPDATED 2026-08-20 — the RULE was vindicated, the NUMBERS above are a ~2-quarter-old snapshot. Read the rule as canon; do NOT cite the dollars as current.**
> Measured at the FFIEC primary (RC-C item 9.a + **Memo item 10** decomposition, 6/30/2026, RSSD 3138146 — `workbook/NDFI_COHORT.tsv`):
>
> | | this lesson (as written) | **6/30/2026 actual** |
> |---|---|---|
> | WAL NDFI total | $6.5B | **$15.81B** — *more than doubled*; **24.1% of total loans** |
> | mortgage-warehouse share | 68% | **68.9%** ✅ **the ratio HELD almost exactly** |
> | ex-mortgage | $4.3B | **$4.92B** (business-credit $3.46B + PE funds $1.46B) |
> | NDFI nonaccrual | *(not tracked)* | 🔴 **$122.5M = 0.77% of the book — 2nd-largest ABSOLUTE in a 26-bank sample incl. JPM/BAC/WFC** |
>
> **Why this note exists, and it is the uncomfortable part:** the decomposition rule was *right enough to re-derive itself* two quarters later — but the **scale** silently quadrupled while this file kept teaching $6.5B as "reality." **A lesson that carries figures ages like data, not like a rule.** I found this staleness on 8/20, packeted the live numbers to WAL the same hour, and then very nearly left my own teaching surface carrying the old ones — the `consumer_check --self` failure mode exactly (the cross-agent scan excludes my own dir).
> ⇒ **Structural fix, not just a patch: the RULE half of a lesson is permanent; the FIGURE half is a dated snapshot and must be labelled as one.** When a lesson's figures move, update them *or* strip them to the mechanism — never leave them undated. *(Flagged by PROME 8/20; the staleness was mine.)*
> ⚠️ **And the figure that would change the rule if it grows: `$122.5M` of NDFI nonaccrual did not exist as a concept when this lesson was written.** One quarter is a level, not a trend — but if it builds, "near-zero losses" stops being true of the *ex-mortgage* book, and that is the half this lesson tells you to isolate.

### [Analysis] — Hidden CRE Methodology ⚠️ RECIPE CONTRADICTED AT PRIMARY 2026-08-07 — re-run owed
**How to screen (v1, DEFECTIVE):** Pull FFIEC Call Report Schedule RC-C Part I. Item 4 = C&I loans. Memo Item 3 (RCON2746) = "Loans to finance CRE not secured by RE." Ratio = Memo3/Item4. Flag if >20%.
**⚠️ 8/7 finding (OZK-spawn + WAL-spawn, independently, same day):** RCON2746's own FFIEC definition places its balance in items **4 AND 9** — dividing by item 4 only is a category mismatch whose severity varies by bank. **OZK's entire Memo-3 sits in item 9.a (RCONPV09 ≡ RCON2746 to the dollar, 6/6 quarters): the "37.6%" cell reproduces at NONE of 18 quarters** (recipe basis runs 294.93%→9.35%); **WAL's 24.24% [12/31/25] DOES reproduce exactly**, but the 12-quarter series never reached 25% and "growing fastest in cohort" was a 6-quarter two-endpoint artifact (live: 21.20% Q2-26). **Rule: never cite the old per-bank ratios; re-run the cohort on ONE uniform basis (both bases reported) before any figure circulates.** Cohort pull is now cheap (FFIEC REST/JWT recipe in `AGENTS/WAL/outbox/2026-08-07_to-REGINALD_mi3-ran-first-time...`; JWT expires 2026-11-05).
**What survives:** the *relabeling/bucket-migration* finding — WAL's uptrend holds on the reproducible basis; OZK's ~$490M debt-on-debt book moved buckets rather than shrinking, and printed its first-ever C/Os Q2-26.

### [Analysis] — Distinguish Classification Levels
Three levels of CRE masking:
1. Extend-and-pretend (don't force refinancing)
2. Mark-to-model (don't write down)
3. Classification (call CRE "C&I" if unsecured) ← Memo Item 3
All three can coexist at the same bank. WAL uses all three.

### [Process] — Date Your Data
**Rule:** Every metric must have a date. "Office DQ is 12.34%" means nothing without "as of Jan 2026." Stale data in STATUS.md causes wrong analysis.

### [Process] — STATUS.md Is Not a Research Report
**Rule:** STATUS.md is a dashboard — current state, thresholds, positions. Research detail belongs in archive/, workbook/, or source files. If STATUS.md exceeds **250 lines** (the enforced CLAUDE.md cap — the old "10KB" figure conflicted with it and lost; reconciled 7/17), it needs pruning.

### [Data] — Verify Real-Time Prices Before Building Narratives
**Mistake:** STATUS.md stated Brent $118-125 and built an entire FL energy shock cascade on that figure. Actual was $81.40. The error propagated through multiple sections before being caught.
**Rule:** Always confirm price levels from a live source before modeling downstream effects. A 45% error on an input produces garbage on all outputs.

### [Data] — Cross-Agent Signal Values May Conflict
**Mistake:** MFS/Barclays exposure listed as £500M in STATUS.md but HANS signal said £600M and MEMORY.md confirmed £600M. Stale value persisted until audit.
**Rule:** When integrating cross-agent signals, check if the new value supersedes an existing one. Update the older reference, don't just add the new one alongside.

### [Methodology] — Run Own Falsifier-Status Check Before Thesis-Level Reframings
**Mistake:** WAL THESIS v2.0 (May 1) demoted V1 (hidden CRE / MI3 reclassification) from "MI3/hidden CRE/fast-transmission" to "Office single-point" — a 14× scope narrowing — BEFORE V1's primary pre-registered falsifier (MI3 ≥25% via Q1 Call Report) actually ran. RED CHG-RED-025 stress-test (May 6, 6-method weighted) verdict: OVER-CORRECTED (~26% aggregate PASS). Strongest single critique: M2 (counter-factual / pre-registered falsifiers). Caught by external grep + methodology audit, not by self-review.
**Rule:** Before publishing thesis-level reframings, run own falsifier-status check. Pre-registered falsifiers live in **`../WAL/WEAKNESSES.md`** (path re-broken by the 7/25 WAL promotion, re-fixed 8/10 per DAEDALUS flag — the local `WAL/` subtree was `git mv`'d to `AGENTS/WAL/`; live falsifier canon = `../WAL/THESIS.md` calibration tables) and bank-specific thesis files. Ask "have any of my own falsifiers actually fired?" — if not, reframing is premature. Demoting on framework redefinition (renaming the vector to narrower scope) instead of falsifier-firing is the specific anti-pattern. Same lesson family as the WALTER Turn 2 catch (claimed "zero action" in BOARD routing without running the grep first) — both cases would have been prevented by 30-second verification pass before publishing.

### [Methodology] — Position EV Math Must Match Thesis Timeline
**Mistake:** WAL SCENARIOS v2.0 EV table credited Jun 18 puts with full multi-quarter bear-payout intrinsic ($22 on $85P at $63 stock) — but V2.0's own bear-case mechanics said "fires across Q2-Q3 2026 (not single event)." Q3 ends Sep 30, well after Jun 18 expiry. RED M4 catch: either the math or the thesis is wrong; they can't both be true.
**Rule:** For multi-quarter thesis with short-tenor positions, separate "unconditional scenario probability" from "conditional probability that scenario has resolved by expiry." Build Jun-conditional / Sep-conditional EV tables explicitly. The Jun-conditional bear-payout weight is much smaller than the unconditional weight when the bear scenario fires gradually over multiple quarters. Position-recommendation that flows from unconditional math is mis-calibrated.

### [Process] — Grep POSITIONS.md Ground-Truth Before ANY Position Task (REPEAT of the 5/8 phantom error)
**Mistake (6/19, ORC-caught):** On the Jun-18 expiry, I read the cluster contents from CALENDAR.md and reported what "expired worthless" — but CALENDAR was desynced from POSITIONS.md (canonical). Result: (a) carried **SSB $90P** in the dashboard cluster though it wasn't in POSITIONS — Will later confirmed it was a REAL position, sold/closed, exit unrecorded = **unrecorded-exit propagation gap** (NOT a fabrication; same class as the KRE $70P I caught 5/8 — both were real positions whose exits never propagated to the ledger, so they lingered in dashboards); (b) wrote off **IWM $250P** as Jun-18-expired when it's a LIVE Jun-30 position (the Jun-18 IWM was $257P) — nearly killed a live position with 11 days left; (c) omitted 4 real Jun-18 positions (WAL $77.5P / FITB $45P / APO $100P / ARES $95P). Economic impact this time was zero (all OTM either way), but the process failure is the same one MEMORY already records from 5/8 — I trusted a dashboard re-list instead of grepping ground truth. **Note the two-way drift:** dashboards can carry positions POSITIONS lacks (unrecorded exits → SSB/KRE) AND miss positions POSITIONS has (the 4 names) AND mangle live ones (IWM strike+expiry). Only the canonical ledger is trustworthy.
**Rule:** POSITIONS.md is the SINGLE canonical source for strikes/expiries. **Before any position task, grep POSITIONS.md first** — never trust a STATUS/CALENDAR cluster list (they drift). **Structural fix (shipped 6/19):** STATUS Convergence Matrix + CALENDAR no longer re-list strikes/expiries — they POINT to POSITIONS.md. Re-listing IS the drift vector; the Doc Ownership table already mandated single-source but wasn't enforced. If you catch yourself typing a strike/expiry into STATUS or CALENDAR, stop — put it in POSITIONS and reference it.

### [Process] — Check a Trigger's Anchor Still Matches the Thesis (anchor-drift)
**Mistake (6/19, ORC-caught):** The standing "Exit 100% on HY OAS <260bps" rule was written for the original **broad-systemic** thesis. The thesis has since narrowed to **idiosyncratic-WAL + CRE-specific** (Office / B1 walk-away / maturity wall / NCO migration) — none of which prints in broad HY bond spreads. HY drifting to 263 (3bps from trigger) on a risk-on rally would have mechanically stopped out a thesis whose actual confirmation channel had moved to CMBS-DQ flows / bank CRE-DQ tier-creep / WAL Q2 NCO. The trigger's anchor silently de-coupled from the thesis it was meant to protect.
**Rule:** When the thesis narrows or shifts channel, re-audit every standing trigger/threshold/exit-rule: does its *anchor metric* still print the thing the thesis now depends on? If not, re-anchor (or downgrade auto-action to a review trigger). Same family as the boot drift-grep — but for trigger *semantics*, not just stale values.

---

*Last reviewed: **2026-08-20** — NDFI [Data] entry figures refreshed at the FFIEC primary (rule VINDICATED, scale had quadrupled unflagged: WAL $6.5B→$15.81B; 68%→68.9% held) + the rule/figure-half distinction added. Phantom-class sweep run the same session found ONE live hit (CALENDAR calling a 8/18-confirmed-SOLD, WAL-owned leg a "live print-catcher") — fixed; `TRADE.md` and `MAY15_DECISIONS.md` verified already FROZEN/HISTORICAL-bannered. Prior: 2026-06-19 (POSITIONS-ground-truth repeat-lesson + anchor-drift, both ORC-caught).*
