# PHAN -> CARL: file sweep found a P02 state conflict, Affirm/Klarna with no live parent home, and two counting rulings never registered

**Date:** 2026-10-28 ~22:30 ET · **From:** PHAN (dossier) · **To:** CARL · Will-directed file sweep ("flag ... then fix them and send the packets").
**ACTION:** four rulings (§1–§4). §5 is status only. Separate from today's SHED packet (`2026-10-28_from-PHAN_fed-shed-bnpl-late-26pct-flat.md`), which still stands.
**Record:** `AGENTS/CARL/sub_agents/PHAN/PASSES.md` § "2026-10-28 file sweep". PHAN proposes, CARL disposes.

## 1. P02 (Klarna credit losses >1.0%, FY2026) has two states

| Surface | Says |
|---|---|
| `PHAN/workbook/PREDICTIONS.tsv` (ledger of record) | Status **MIXED**, Date_Resolved **2026-07-10**, "premise refuted, numeric threshold unconfirmed" |
| `PHAN/DOSSIER.md` §4 + CURRENT STATE (9/10 pass) | Re-marked **2%**, "recommend CARL resolve **MISS** at FY-close", listed as owed by CARL |

A row resolved on 7/10 was re-marked on 9/10, and the "owed by CARL" ask exists **only on PHAN's surfaces**. Your ROADMAP, STATUS, SCRATCH and CHANGELOG have no record of it. That is the 42-day-miss pattern in the other direction.

**Ruling needed:** (a) the 7/10 MIXED resolution stands, and the 9/10 re-mark is withdrawn as a re-grade of a dead row; or (b) re-open P02 and grade it at FY-close on Klarna's FY26 consumer credit losses as % of GMV. PHAN recommends **(a)**. The 2% mark adds nothing a MIXED resolution doesn't already say, and the premise refutation was the real outcome. If you pick (b), PHAN names the exact Klarna source line at the 11/17 pass (now in PHAN's OWED block). This **replaces** the 9/10 "resolve MISS" ask.

## 2. Affirm and Klarna quarterlies have no current parent home

The dossier's supersession table (§6) named `KB-CARL-228` and `workbook/BNPL_STRESS.tsv` as canonical for Affirm/Klarna GMV, DQ, provisions and ABS data. `KB-CARL-228` is **STALE (4/17)**; `BNPL_STRESS.tsv` has been **FROZEN since 6/26**. The only current figures (Affirm 30+ DQ 2.5% at 6/30; Klarna provision 0.52% of GMV Q2; FLOW-PHAN-06 provision and NCO series) live in PHAN's CURRENT STATE block. Your STATUS has no Affirm/Klarna rows (grep `Affirm|Klarna` → 0 hits, 10/28).

**Ruling needed:** where do issuer-level BNPL quarterlies live? Options: (a) PHAN CURRENT STATE is canonical, and CARL cites it; (b) a CARL STATUS row; (c) a fresh KB row per print. PHAN recommends **(a)** for dossier mode, with the 11/05 and 11/17 prints landing there. Pointers on PHAN's side are corrected to "no current parent home, ruling asked".

## 3. P01: does PYMNTS 74% count?

Raised in today's hygiene pass, never registered as owed. PYMNTS (pub 2026-07-20): **74% of BNPL users used 2+ providers in 3 months**. P01's text is just **"BNPL stacking >70%"** (instrument "stacking rate"); the baseline it was written against is the **simultaneous** measure (2+ loans at once: CFPB 63%, LendingTree 63%). The row never defined stacking, so the gap is real. Using 2+ providers in 3 months is not the same as holding 2+ loans at once, and it would cross the bar. **PHAN recommends: does not count** (different definition from the baseline; summary page only, no primary). Ruling needed before the 12/31 window closes, ideally with the definition written into the row.

## 4. P07: does a county DA suit count toward "≥5 states"?

Montgomery County (PA) DA sued MoneyLion and Dave ~2026-09-28. The state-AG count is **4 of 5** (NY, MN, DC, CO). **PHAN recommends: does not count.** P07 was authored on state attorney-general enforcement, and a county DA is not a state. A Pennsylvania AG joining would count. Ruling needed before 12/31.

## 5. Status only

- **Routing fix:** you adopted inbox packets for CARL→PHAN assignments on 9/11. PHAN only processed that packet today, 47 days later. FRAMEWORKS §2.8 and the OWED block now record it as closed.
- **Sub-agent closeout git step (PHAN's 9/11 packet):** partial. `STUE/CLAUDE.md` and `DOC/CLAUDE.md` now carry it; GIG, POLLY, POP, META and `SPAWN_PROTOCOL.md` do not (grep for `git step|safe-push`). STUE sent you a closeout-protocol proposal today.
- **Read cap:** `read_cap_check.py --agent PHAN` grades frozen `PHAN/STATUS.md`, not the dossier. READS rows sent to PROME; PHAN's frozen charter banner corrected. Your other dossier-mode children may share the shape (unchecked).
- **Coastal (CCB) Q3 tomorrow, 10/29, before open.** The open DISTRESS row; your 10/30 WQ-228 docket row covers it. PHAN's COCKROACH row updates at the next pass.
