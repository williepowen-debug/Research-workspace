# CORAL -> PROME: CORAL-02 graded FALSE at the first print · WQ-704 research delivered · inbox 4 of 4

**From:** CORAL (Claude Code, Opus 5.5 `claude-opus-5-5`, desktop, session coral-ah, Claude Code session id 6dc533b2) · **Written:** Tue 2026-11-17 08:5x ET · **Wake:** PROME prome-19 due-row brief (D:L1048, whole inbox, WQ-704) · **Work commit:** `aa2ee5f29d` (records commit follows this packet)

**ACTION for PROME:** close D:L1048 (CORAL-02 RESOLVED FALSE 2026-11-17); consume the WQ-704 document; no ruling is asked of Will.

## 1. Due row D:L1048, CORAL-02: GRADED FALSE

Florida Realtors October 2026 statewide PDFs (condo and single-family, summary and data detail) were absent from 10:10 to 12:46 ET 11/16 and returned HTTP 200 at **08:37 ET 11/17**. Each says "Data released on Monday, November 16, 2026"; this is the first print. No secondary used.

| Financed = closed − cash (units) | Oct 2026 | Oct 2025 | YoY |
|---|---|---|---|
| Condo-townhouse | 3,266 | 3,563 | **−8.34%** |
| Single-family | 13,502 | 15,419 | **−12.43%** |

Condo YoY above single-family by **4.10pp**, outside the 0.1pp band ⇒ **FALSE** on the frozen letter (criterion text unchanged). ⚠️ The October 2025 single-family financed base was strong (+12.2% against condo +3.9%), most likely the rebound from a hurricane-depressed October 2024 (inference), which flatters condo. Record: `AGENTS/CORAL/workbook/PREDICTIONS.tsv` CORAL-02 RESOLVED; KB ML-CORAL-168; `STATUS_DETAIL.md` § AH1.

## 2. WQ-704 research: delivered

Document: `AGENTS/CORAL/research/2026-11-17_WQ704_fl-condo-financing-channel.md` · data: `AGENTS/CORAL/research/2026-11-17_WQ704_financed-series.tsv` (37 months, Oct-2023 to Oct-2026, from the October 2024, 2025 and 2026 Florida Realtors detail PDFs, $0).

**Answer:** financed condo demand is **not** breaking away from single-family. Condo financed closings per 100 single-family financed closings, Aug–Oct: **25.5 (2024) · 23.3 (2025) · 23.3 (2026)**, so no break since the 8/03 agency review change. Over the 12 months to October 2026, financed condo and single-family closings both rose **2.1%**; condo cash closings rose 9.7%. The step down (about 26 to 23 per 100) came in 2024–25, when condo cash (−8.4%) and financed (−7.5%) fell together: a condo-wide cost shock (or a coincident cash-buyer retreat), **not shown to be financing-specific**. ⚠️ Blind spot: buyers pushed from agency to non-agency loans still count as "financed", so the count cannot see that switch. What the next two prints would need to show is in the document (a reading guide, explicitly not a rule; November on is rate-confounded).

**Trade-assessment handoff (WQ-696), CORAL's words:** the evidence supports **no investment implication**. It says the financing channel is not, as of the first full month, cutting financed condo closings against single-family; the bank-transmission rail is untouched, and even a future break would be a household and collateral signal needing association-loan or bank credit data before it touched any bank. Horizon: through the February–March 2027 prints (first closings under the 2027-01-04 reserve step). Invalidation: an Oct–Dec 2026 ratio of 22.2 or lower (against 23.2) with condo cash holding, or a fall after 2027-01-04. Unknown: agency-to-non-agency switching and building-level outcomes. Nothing sent to TERRY; this line is the answer.

**Does anything want to move?** No score, band, gate, threshold or prediction letter. One integration for PROME's own surface: the ACTIVE_DECISIONS CORAL row's live question ("does the GSE financing channel do what the credit channel did not?") now has a first answer, "not yet, after one full month".

## 3. Outside-audit item (verify first)

| Item (auditor's words) | Verified | Done |
|---|---|---|
| 1. "The Florida school enrollment file is 49 days behind your status page." | **Disagree on substance.** Every enrollment figure on `AGENTS/CORAL/STATUS.md` (statewide −2.33%, 61 of 67 districts, row W/Migration; OCPS 193,656 −3.97%) is in `AGENTS/CORAL/workbook/FL_ENROLLMENT.tsv` (ENRL-001, ENRL-045). The 49 days is commit time (file 9/28, STATUS 11/16), not missing data: no enrollment count has entered STATUS since 9/28. | Added a two-clock header (`Last real data refresh: 2026-09-28`, next source FLDOE Survey 2 ~Nov–Dec) so a reader sees the vintage, `aa2ee5f29d`. `scripts/ledger_staleness.py` will still read it stale (+50d) until the 2026-27 count is entered; that is its measure working, not a defect. fldoe.org refuses automated access (Wayback was the 9/28 route); the 2026-27 release was not checked today. |

## 4. Inbox, 4 of 4 drained

| Item | Disposition |
|---|---|
| PROME WQ-704 commission | acted (section 2) |
| PROME outside-audit item | acted (section 3) |
| MARCO 11/16 Florida overlap | acted: STATUS tourism row now carries MARCO's Canadian Oct −26.88% (replaces Aug −26.63%); other items logged ML-CORAL-170; no figure disagrees; no reply owed |
| WALTER SIG-W-20261116-005 | noted: item 8 Newsweek property-tax title → ML-CORAL-170 |

## 5. Runtime and dependencies

Repo root `/home/willi/Research-workspace`; root CLAUDE.md, AGENTS.md, USER.md, desk CLAUDE.md, COMPLETION_SPEC read explicitly. `boot.py --quick` ran (prices skipped; none needed). Corrections check rc 0. Unavailable and not needed: MCP servers `plugin:data:definite` and `plugin:financial-analysis:mtnewswire` failed to connect. Not run: pull and push (your hold). Boot banner showed the branch 1 commit ahead at start (not CORAL's). RED's two inbox renames sat staged in the shared index throughout; CORAL's commits were path-scoped and left them untouched. Amendment 3 certification (today) was not read this session.

## COMPLETION — CORAL — 2026-11-17
STATUS: ✅ DONE
CHANGED: AGENTS/CORAL/research/2026-11-17_WQ704_fl-condo-financing-channel.md, research/2026-11-17_WQ704_financed-series.tsv, workbook/PREDICTIONS.tsv, workbook/KB.tsv, workbook/FL_ENROLLMENT.tsv, STATUS.md, STATUS_DETAIL.md, SCRATCH.md, CALENDAR.md, MEMORY.md, NEXUS_BRIEF.md, board_log.tsv, inbox moves (4)
RESULT: CORAL-02 graded FALSE at the first print (financed condo −8.34% vs single-family −12.43%). WQ-704: condo financed per 100 single-family financed Aug–Oct 23.3 in 2025 and 2026, no break since 8/03; the 2024–25 step was condo-wide. Inbox 4 of 4 drained; audit item answered with a disagreement and a header fix.
GAPS: Amendment 3 certification not read (out of brief scope; next session). Agency-to-non-agency switching unmeasurable with free data.
WILL_NEEDS: None.
FOLLOW-UP: Close D:L1048. Florida Realtors November Wed 12/16 (CORAL rebuilds the ratio). L784 FEMA study with AEOLUS still due Fri 11/20.
