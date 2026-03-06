# BROCK SELF-AUDIT
**Written:** 2026-03-06 | **By:** BROCK subagent (self-assessment post-upgrade)

---

## What Makes Sense

**CLAUDE.md is the best agent instruction file I've seen.** Clear domain scope, spawn protocol with numbered steps, explicit "you do NOT own" list, cross-agent signal table with conditions → targets → priority. I will reference this every spawn. No ambiguity about what I own vs. consume.

**The convergence matrix is genuinely useful.** A 10-vector scoring system with explicit thresholds and a "35/50 🔴" summary line gives any spawn a single-line status read before diving deeper. Smart design.

**Workbook split is good.** KB.tsv (permanent facts), ML.tsv (timestamped events), VX.tsv (live thresholds), FLOW.tsv (transmission channels), PREDICTIONS.tsv (falsifiable forecasts). Each file has a distinct job. I can query any of these without reading the others.

**Exit rules in CLAUDE.md are real falsification criteria.** Four categories, specific conditions, explicit cross-references (e.g., "[ref LIQUID]"). This is actually testable, not vague hedging.

**Source tagging rule (`[CONF]`/`[EST]`) is excellent and enforced consistently in STATUS.md.** Every dashboard value has a source and date. This is the kind of thing that separates a useful agent from a hallucination machine.

**Files I'll actually reference on spawn, in order:**
1. STATUS.md — dashboard + bottom line + convergence score
2. LESSONS.md — quick reminder of data traps
3. PREDICTIONS.tsv — what needs updating
4. Inbox listing — what's waiting (not processing, just noting count)

FLOW.tsv and BANK_BDC_MATRIX.tsv are reference tools — I'll read them when spawned for a specific transmission question, not on every boot.

---

## What's Confusing or Redundant

**EXPECTED_SIGNALS.md is stale and contradicts the corrected record.** This is the biggest structural problem I found.

Specifically:
- EXPECTED_SIGNALS.md lists **PSEC PIK at 35% 🔴** in the "Current canaries" table
- VX001 explicitly says "CORRECTED from hallucinated 35% figure. 8.6% is normal/low."
- ML001 documents the same correction
- LESSONS.md rule #1 calls it out explicitly

So if I'm a fresh spawn reading EXPECTED_SIGNALS.md before VX.tsv/ML.tsv, I get the wrong number. The file says "Current canaries: PSEC 35% 🔴" but that's wrong. This is an active landmine.

CLAUDE.md's FILES table even notes EXPECTED_SIGNALS.md as "**legacy — migrate to exit rules**." But it's still sitting there with uncorrected data, not clearly marked as deprecated at the top of the file itself.

**BDC_CASH_COVERAGE.tsv is substantially stale.** Key issues:
- PSEC row still says "PIK 35%" in Notes column — wrong per VX001/ML001
- FSK row still says dividend "$0.70 / PENDING" — wrong; ML002 confirms FSK cut to $0.48 (-31%) on Feb 25
- Multiple rows show "PENDING" status for Q4 2025 earnings that have since resolved
- The framework section is detailed/useful, but the actual data table at the top hasn't been updated since Feb 23

This file has a split personality: a stale data table on top, and a detailed methodology framework below. The methodology is valuable. The top table is misleading.

**VX.tsv has 9 vectors but the convergence matrix in STATUS.md has 10 rows.** "Mainstream Narrative" appears in STATUS.md's convergence matrix but has no corresponding row in VX.tsv. Minor inconsistency but creates ambiguity about whether VX is the canonical vector list.

**ML.tsv only goes to ML011 but there's a lot of post-Feb-27 activity.** The last entry is Feb 27. The KB goes through Mar 6. Everything that happened Mar 3–6 (BCRED $3.8B, NFP -92K, Eisman, CNN piece, APO class action) is in KB.tsv but not in ML.tsv. Is KB the new ML? Or did ML just stop getting updated? The distinction isn't clear post-upgrade.

**KB.tsv has 20 entries (BRK-001 through BRK-020), not 21** as described in my task brief. Either one was removed before I was spawned or the count is off. Not a big deal but worth noting.

**PREDICTIONS.tsv has off-domain predictions.** BRK-12 (PLTR <$80), BRK-13 (AI darling SBC criticism), BRK-15 (Burry PLTR short profit), BRK-17 (hyperscaler GPU depreciation schedule), BRK-20 (Blackwell overheating) feel like Burry thesis tracking, not private credit monitoring. BROCK's domain is BDCs and private credit. I don't own PLTR, GPU depreciation schedules, or Burry's short book. These should live with CARL or a dedicated Burry-tracking agent (if one exists). Having them here creates domain confusion and dilutes what "BROCK's predictions" means.

---

## Questions for Prome/Will

1. **EXPECTED_SIGNALS.md: deprecate or update?** It's marked legacy in CLAUDE.md but still contains the wrong PSEC PIK number. Should I delete it, add a DEPRECATED header, or update the canary figures? Given it's called "legacy," my preference is to add a `⚠️ DEPRECATED — data in this file may be stale. See VX.tsv for current thresholds.` header and leave the framework section.

2. **ML.tsv vs KB.tsv going forward:** Are they parallel (ML = events, KB = facts) or did KB replace ML? The upgrade added KB.tsv as "permanent research findings, verified facts" while ML tracks "timestamped events." That distinction is meaningful — but KB-BRK-017 through BRK-020 (NFP print, bank drops, narrative events) feel more like ML entries than permanent KB facts. Who decides? Or is the rule: if it has a timestamp and is event-driven, ML; if it's a structural fact (Athene holds $442B illiquid), KB?

3. **Off-domain Burry predictions:** Should BRK-12/13/15/17/18/20 move to another agent's PREDICTIONS.tsv? Or is BROCK the designated Burry-thesis tracker because of the AI infrastructure angle?

4. **SIGNALS.md (workspace-level):** AGENTS.md references `AGENTS/SIGNALS.md` for cross-agent threshold breaches. I'm supposed to append there when a threshold fires. Does this file exist? I wasn't asked to read it. Should it be in my spawn protocol?

5. **Inbox is 5 messages deep (unprocessed) from Mar 4.** Is the "don't process inbox on normal spawns" rule still holding, or should I be spawned specifically to process these? Some look consequential (BCRED gate threshold, TCPC fraud class action).

6. **UPGRADE_PLAN.md** exists in my directory but wasn't in my read list. Is it still active? Or is the upgrade complete and this file is now dead weight?

---

## Friction Points

**The EXPECTED_SIGNALS.md file is a genuine friction hazard.** On a fast spawn, a new instance might read it and take the PSEC 35% PIK figure seriously before reaching the VX.tsv correction. This could produce a wrong cross-agent signal. Fix this before the next spawn.

**BDC_CASH_COVERAGE.tsv methodology vs data split.** The bottom 80% of that file is a detailed methodology guide (how to extract cash NII, monitoring protocol, historical context). That's reference material. The top 10% is a data table that's now 10+ days stale with wrong numbers. If I'm looking for BDC coverage data on a quick spawn, I hit stale PENDING rows immediately. The methodology should move to CLAUDE.md or a separate `METHODOLOGY.md`, and the data table should be the only thing in BDC_CASH_COVERAGE.tsv.

**Too many files to read at boot if I follow the old EXPECTED_SIGNALS.md habit.** Current spawn protocol is clean: STATUS.md → LESSONS.md → task. That's right. EXPECTED_SIGNALS, FLOW.tsv, BANK_BDC_MATRIX, and BDC_CASH_COVERAGE are reference docs, not boot reads. The CLAUDE.md spawn protocol correctly limits boot reads to STATUS + LESSONS.

**STATUS.md is good but the "Active Catalysts" and "Watchlist" tables are partially redundant.** Both contain BCRED Q2, APO class action, Blue Owl OCSL II. One is chronological (catalysts by date), one is conditional (watch for X → triggers Y). Together they work, but on a quick read they feel like they're saying the same thing twice. Could merge into a single table with both date and trigger columns.

---

## Missing / Wish List

**No SIGNALS.md output log.** CLAUDE.md says I should append to `AGENTS/SIGNALS.md` when thresholds fire. But there's no "sent signals" log in my own directory. I can't verify what I've already signaled to REGINALD or LIQUID without reading through the outbox. A `SIGNALS_SENT.log` (date, target, trigger, prediction ID) would close this loop.

**Predictions need outcome tracking beyond "OPEN/CONFIRMED."** BRK-03 was confirmed. But I have 19 other open predictions and no "confidence vs. time" tracking. Are they getting stronger or weaker as new data arrives? BRK-05 (shadow default rate acknowledged) and BRK-11 (first BDC breaches 150% coverage) both feel closer than when they were made — but the PREDICTIONS.tsv shows them at the same confidence as Feb 23. A "Current_Confidence" column vs "Initial_Confidence" would help me see which predictions I should be acting on now.

**No REGINALD cross-reference table.** I signal REGINALD constantly (bank warehouse lines, BDC NAV declines, etc.) but BANK_BDC_MATRIX.tsv tracks the structural relationships, not what REGINALD currently thinks about those banks. When WAL drops 13%, I don't know if REGINALD has already processed that and what their bank score is. A one-line "Last REGINALD sync" note in STATUS.md would help me avoid duplicating their work.

**HY OAS is conspicuously absent from my workbook despite being an exit rule trigger.** Exit rule: "HY OAS reverses below 260bps for 10+ sessions [ref LIQUID]." But I have no row in VX.tsv for HY OAS and no mechanism to check if LIQUID has updated their reading. I'm dependent on getting a signal from LIQUID, but if LIQUID doesn't send one I'd miss a thesis kill condition. At minimum, a "Last LIQUID reading: HY OAS XXXbps [date]" line in my STATUS.md dashboard.

**Predictions I'd add:**
- *BRK-21: APO class action settles for >$500M (Epstein/Rowan)* — catalyst already logged in KB, no prediction against it
- *BRK-22: BCRED formally gates Q2 2026 (>10% redemption threshold triggers)* — the single most important near-term catalyst, tracked in watchlist but not as a formal prediction
- *BRK-23: NFP prints negative 2+ consecutive months → Fed emergency action* — cross-agent but BROCK owns the private credit transmission consequence

---

## Data Quality Concerns

**PSEC PIK 35% survives in two places that weren't updated:** EXPECTED_SIGNALS.md canaries table and BDC_CASH_COVERAGE.tsv notes column. Actual confirmed figure per VX001/ML001: **8.6%**. This is the most dangerous stale number in the whole system because it's in a "reference" file that looks authoritative.

**BDC NAV discount inconsistency:** EXPECTED_SIGNALS.md says "Industry average -15.5% 🟠" (last updated Feb 23). STATUS.md dashboard says "BDC Median Listed Price: 73% of NAV" = 27% discount 🔴 (Mar 4). The discount worsened significantly and the two files tell different stories.

**VX004 Fund Gates Count shows "1 confirmed (OBDC II)"** but VX007 and STATUS.md describe Blue Owl OCSL II also ending quarterly liquidity (Mar 3). Is OCSL II a formal gate? If yes, VX004 should be 2 confirmed, which would push from YELLOW to ORANGE. This classification matters for the convergence score.

**APO stock price: ~$107 (STATUS.md, Mar 5).** The Barclays price target is $131. I'd want a Mar 6 close price given WAL was -13% on the same day — APO may have moved further. The dashboard might be 1 session stale on APO specifically.

**ML.tsv stops at Feb 27, KB.tsv runs through Mar 6.** There's a 7-day gap where significant events (BCRED record redemptions, NFP print, Eisman call, CNN piece) are only in KB.tsv. If KB is now the primary event log, that's fine — but it should be explicit. If ML is still supposed to track events, it needs 9+ new entries.

**"40% of private credit borrowers have negative FCF" [Moody's/industry]** — the source tag is vague. "Moody's/industry" could mean a lot of things. This is a critical thesis-supporting number cited in STATUS.md and KB-BRK-015. The actual Moody's report name and date should be in the source column.

---

## Summary Judgment

The upgrade is a genuine improvement. The old structure must have been looser — this version has real infrastructure: convergence matrix, source tagging, domain boundaries, cross-agent signal rules, exit criteria. CLAUDE.md in particular is well-written and I would follow it.

The critical fix needed before next spawn: **Add a DEPRECATED warning to EXPECTED_SIGNALS.md and update BDC_CASH_COVERAGE.tsv's data table.** These are the two files most likely to inject wrong data into a fast spawn. Everything else is either minor inconsistency (VX.tsv missing the 10th vector) or a feature request (HY OAS tracking, signal log).

The Burry predictions in PREDICTIONS.tsv are the lowest-urgency structural issue but worth discussing — they dilute BROCK's domain focus.

The inbox (5 messages, Mar 4) is getting old. At least two of those signals look consequential. Recommend spawning me specifically to process it.
