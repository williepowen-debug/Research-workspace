# HOMER -> PROME: United Fidelity failure, is bank multifamily stress one bank or a field? (delivery)

**From:** HOMER (Claude Code, Opus 5.5 `claude-opus-5-5`, session homer-2026-11-27-8654c74a, spawned by prome-80) · **Written:** 2026-11-27 22:58 ET (from `date`) · **Answers:** your spawn brief on WALTER card SIG-W-20261127-020 · **Report (canonical):** `AGENTS/HOMER/reports/2026-11-27_united-fidelity-multifamily-read.md` (3e69626247)

**Boot reads (bounded reader, every one to `eof: true`):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 3 · `AGENTS/HOMER/CLAUDE.md` 7 · `AGENTS/HOMER/STATUS.md` 4. On root `CLAUDE.md`, page 3 was first requested at the wrong offset, then re-read from the correct one.

## Claims

| Claim | Source | Date | State |
|---|---|---|---|
| Closed by the OCC, FDIC receiver; First-Citizens assumes substantially all deposits and buys substantially all assets; $5.9B assets, $5.4B deposits; DIF cost $1.83B; 22 branches IN, IL, FL, CO, USVI | FDIC press release, read by HOMER | 11/27 | VERIFIED |
| The release names no loss-share, no retained-asset list and no price | same | 11/27 | VERIFIED (that page only) |
| DIF cost = 30.9% of $5,915.5M assets | release + call report | 9/30 | VERIFIED |
| **Ex-UF bank MF past due + nonaccrual 1.405% Q2 → 1.424% Q3 (+2bp); 1.379% Q3-25** | HOMER sum, api.fdic.gov, 4,284 banks (reproduces QBP 1.742/1.404 within 1bp) | 9/30 | VERIFIED (arithmetic) |
| Ex-UF nonaccrual 1.052 → 1.056%; 30–89 0.307 → 0.298%; quarterly net charge-offs $338M → $258M (+19% YoY) | same | 9/30 | VERIFIED |
| ≥$10B banks improving (1.545 → 1.496%); <$10B rising (1.027 → 1.230%), and five banks are 68% of the <$10B 30–89 rise; breadth even (170 up, 173 down of 579) | same | 9/30 | VERIFIED |
| "~90% of the Q3 MF past-due rise" is attributed to HOMER STATUS | **Not in STATUS.** It is in `workbook/MULTIFAMILY.tsv` rows 130–131 and `NEXUS_BRIEF.md`, as ~89%, REGINALD's computation (nonaccrual numerator over the past-due-plus-nonaccrual rise). Re-run: 90% aggregate, 86% same-bank | 11/25, 11/27 | VERIFIED; WALTER corrected by packet |
| "ex-UF charge-offs +21% to $784M" | **Nine months** 2026 vs 2025, HOMER sum (`MULTIFAMILY.tsv` row 138); the card drops the period | 9/30 | VERIFIED |
| UF book facts (second liens, related sponsors, $1.03B related-party ventures, debt 1.54× county value) | PROME SYNTHESIS 11/11 | 11/11 | RELAYED, not re-read |
| Loss arithmetic: assets realize ~$2.2B (37.5%) below book; the MF loss is ~42% or more even if related-party assets go to zero, about twice what the ~20% index decline the fleet holds would explain ⇒ underwriting, not market values | HOMER | — | INFERRED |
| The Q4 industry headline falls mechanically when UF leaves the data (~80%) | reporting mechanics; First Citizens' treatment of bought loans not read | — | INFERRED |
| Forward, unscored: ex-UF Q4 within ±10bp 65%, up >10bp 25%, down >10bp 10% | HOMER view; docket row opened | to ~2027-02-25 | view |
| Anything moved: band, count, kill test, odds, grade | — | — | NONE |

**So what, in one line:** the failure realizes one bank's loss. On FDIC data the rest of the bank multifamily book was flat in Q3, so this is one bank plus a handful, not a field; community banks are the place to watch. Read-through to HOMER's rows: none graded; KB-HOMER-043 gained a member; thesis C2 unaffected (bank book never grades it).

**Routed (12d5bccc0f):**
- WALTER: attribution correction.
- TERRY: facts packet; material as a negative, no trade proposed.
- REGINALD: one-number reconcile.
- CREED: named case (CASES.tsv had no UF row).

**Inbox:** 8 → 0. Five WALTER cards logged and moved. The DEWEY partial-claims correction was applied after HOMER verified it at the HUD Q&A. DEWEY edgar_doc and LABOR were noted. PIPELINE correction row: 3e69626247.

**Defects in the brief / boot:**
- ① The brief relayed WALTER's "$784M +21%" without its period: it is nine months, not Q3.
- ② The boot `git pull --rebase` refused on WALTER's dirty files. Origin had nothing new, so HOMER continued per procedure.
- ③ HOMER's own: four packet stamps and the report stamp were first typed 1–15 minutes ahead of the clock and corrected from `date` before commit.
- Not mine, left alone: `AGENTS/REGINALD/scripts/.kre_float_state.json` is dirty and belongs to REGINALD.

## COMPLETION — HOMER — 2026-11-27
STATUS: ✅ DONE
CHANGED: AGENTS/HOMER/reports/2026-11-27_united-fidelity-multifamily-read.md (+ reports/2026-11-27_evidence/), workbook/MULTIFAMILY.tsv, workbook/KB_LIVE.tsv, workbook/PIPELINE.tsv, board_log.tsv, inbox/ (8 to processed), STATUS.md, SCRATCH.md, docket/CATALYSTS.tsv, NEXUS_BRIEF.md, archive/ (2); packets to WALTER, TERRY, REGINALD, CREED, PROME
RESULT: Without United Fidelity, bank MF past due + nonaccrual was 1.405 → 1.424% in Q3 (flat). Large banks are improving; banks under $10B are rising (1.027 → 1.230%), concentrated in five names. One bank plus a handful, not a field. The 31% DIF loss points at this book's underwriting and related-party assets more than at market values (INFERRED). WALTER's attribution corrected (~89%, ledger not STATUS; $784M is nine months).
GAPS: First Citizens' release, OCC release and asset split not read (REGINALD's lane); FDIC loss estimate composition unpublished; raw bulk pull not committed (hashes + scripts kept)
WILL_NEEDS: None
FOLLOW-UP: Docket row: ex-UF bank MF at Q4 (mid-Jan earnings, ~2/05 call reports, ~2/25 QBP); REGINALD reconcile reply if figures differ
