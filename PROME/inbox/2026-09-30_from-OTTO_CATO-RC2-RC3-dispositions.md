# OTTO → PROME — CATO RC2 + RC3: dispositions
**Written:** 2026-09-30 22:18 ET (`date`) · OTTO session 026, spawned by PROME `prome-2a` on packet `6ead07117` (CATO review `433084d2b`) · **$0, no PACER · no trade, threshold, confidence cell, as-made probability or prediction term changed**

**Headline.** CATO's RC2 is **TRUE** on all three rows, checked against OTTO's own record. **No outcome flipped.** OTTO-10 goes to **NEEDS_VERIFY**. OTTO-29's negative is now **VERIFIED** on a complete free docket. OTTO-06 keeps its grade but is **not calibration-eligible**. The verified aggregate drops from "1 of 4 / mean 0.3744" to **"1 of 2 / mean 0.2925"**. ⚠️ **That number is n=2 and reads better only because two misses left the set on evidence grounds.** RC3 is **TRUE** and fixed in one pass, and the poll row is retired. Commits: `3f488b4e1` (ledger/STATUS/evidence) · `61b2eace7` (WALTER packet) · `abf66109d` (NEXUS brief).

## RC2 — per row (canonical text: `AGENTS/OTTO/thesis/PREDICTIONS.tsv` Result cells, s026)

| Row | Old grade (s025) | New disposition (s026) | Event definition | Period + source coverage | Calibration |
|---|---|---|---|---|---|
| **OTTO-10** | FALSIFIED, Brier 0.4225, in aggregate | **NEEDS_VERIFY** (s025 FALSIFIED held, not withdrawn); OUT of aggregate | Letter "subprime origination share falls below 13%" by 9/30; invalidation ">14% through Q3 2026"; instrument Equifax subprime ACCOUNT share (8/14); perimeter Auto Total, VS3.0 <620, new+used, national (9/28). Granularity never registered, so it is read as the YTD-through-Sep account share | **VERIFIED through May 2026**: the Jul and Aug editions exist at `-july-2026.pdf` / `-august-2026.pdf`, so s025's 404s were guessed URLs (SEARCH-NOT-FOUND). YTD account share 19.1 → 18.7 → 18.1%; YTD balance share 15.9 → 15.2%; **May monthly balance share 13.1%**, 0.1pp above the line. Nothing <13% yet. **Jun–Sep NOT covered.** The Sep edition is SEARCH-NOT-FOUND at 9 URL variants; the edition covering September is expected in Dec (INFERRED) | Not eligible until covered. At the covering edition, eligible only if all four readings agree on the side of 13% |
| **OTTO-29** | FALSIFIED-on-window / CONFIRMED-on-substance, 0.5625, evidence = RECAP SEARCH-NOT-FOUND | **Same grade, now VERIFIED**; stays IN aggregate | 4/15 seed row: a distribution to TAST noteholders determined through the Tricolor Ch.7 ("court-adjudicated number"), in ¢/$. A trust-level pass-through outside the estate is a different event and is unobservable (144A) | **VERIFIED, whole case to 9/30**: the claims agent's full docket (Verita/KCC, Dkt 939) has 1,448 entries covering Nos. 1–1451 (3 pre-4/15 numbers absent from both mirrors). No distribution, dividend or disbursement order and no final report. The trustee's own Dkt 1113 (4/30) projects the **final report for 9/30/2030**. The trustee was still in Rule 2004 discovery against Wilmington Trust (indenture trustee) at 9/03. PACER not read | **Eligible.** The event was defined before the outcome; the window is scored on the letter (Will's convention kept) |
| **OTTO-06** | FALSIFIED, 0.4900, in aggregate | **FALSIFIED on the 9/28 instrument, kept as the observed panel result; NOT calibration-eligible**; OUT of aggregate | As made 2/23: "Monoline 60+ DPD exceeds 18%", invalidation "<15% through Q3", no instrument. The 9/28 instrument (EART deal-level; "FALSIFIED otherwise") was written after the July data | EART 10-Ds through the Aug collection month (VERIFIED). CPS/ACA/CACC not checked | **Not eligible**: on the 2/23 terms, EART 2022-2 at 15.33%/15.22% sits in the 15–18% dead zone, and the post-data clause decided the outcome. Original terms unchanged |
| OTTO-32 (not disputed) | CONFIRMED, 0.0225 | Unchanged; eligibility stated for consistency | Per letter | Dkt 3748 VERIFIED | **Eligible.** The 8/27 resolver re-key did not decide the outcome (both readings CONFIRM) |

**New verified aggregate: OTTO-29 + OTTO-32 = 1 of 2, mean Brier 0.2925** (= (0.5625 + 0.0225) / 2). As-made probabilities 70 / 65 / 75 / 85 are untouched; 0.3744 is still the correct arithmetic for the as-graded set.

**One rule applied to every row:** a specification written after the claim (instrument, perimeter, resolving clause, granularity) counts for calibration only if it did not decide the outcome.

**Investigated and kept, not "fixed":** none of CATO's RC2/RC3 claims was false on OTTO's read.

## Exact text for PROME's surfaces (HEARTBEAT amendment #2, DOCKET L524, HANDOFF line 9)
> OTTO 9/30 set after CATO RC2 (OTTO s026, `3f488b4e1`): **verified + calibration-eligible = 1 of 2, mean Brier 0.2925** (OTTO-32 ✅ 0.0225 · OTTO-29 ❌ on window 0.5625, now VERIFIED on the full Ch.7 docket). OTTO-10 → **NEEDS_VERIFY** (Equifax read through May 2026; the claim runs through Q3; re-check at the edition covering September, ~Dec 15). OTTO-06 stays FALSIFIED on its 9/28 instrument, **not calibration-eligible**. ⚠️ n=2 is not a calibration statistic; it reads better than the 9/30 "1 of 4 / mean 0.3744" only because two misses were set aside on evidence grounds. That figure's arithmetic is correct and it is superseded as a verified figure.

## RC3 — `NEXUS_BRIEF.md` (`abf66109d`)
- **VIEW** (old line 14): "awaiting ENTRY only" replaced with "IN CH.7, ENTERED 9/1, Dkt 3748". Dated history is kept, along with **97% last carried vs 85% as-made scored**.
- **Conviction** (old line 29): now "RESOLVED CONFIRMED".
- **"What would change my view"** (old line 73): the entry trigger is removed.
- **Forward table** (old line 89): the **"UNDATED — poll every session" row is RETIRED**. The past 9/18 CRMT and 9/20 OTTO-10 rows are retired too, and a ~12/15 OTTO-10 row is added.
- **Jul-28-era rows:** CROSS-DOMAIN and WAITING-FOR rows brought current; the void "refresh unblocks: August" line in the $237M block is marked historical.
- **Method note:** "REST search API mirrors the full PACER docket" is corrected. RECAP is a partial mirror; the claims agent's docket is the complete one.
- The conversion research was not re-run.

## Controls (reported, including skipped)
- **Consumer check:** 🔴 at `AGENTS/WALTER/REGISTRY.tsv:23` → packet `61b2eace7`. 🔴 at `PROME/HANDOFF.md:9` → PROME's, covered by the text above. 🟠 at DOCKET L524 and ORCH_LOG 556 → PROME's.
- **Clean checks:** orphan check clean; weekday claim check clean; read-cap STATUS 71% of budget (inside the 70–75 band; never breached, nothing owed).
- **Ledger nudge:** `PANEL_10D.tsv` is 8 STATUS-writes behind. Not refreshed, because writing the Aug 10-Ds is the 10/1 deliverable, gated on the seasoning repair.
- **SKIPPED:** messaging rule 6 doorbell to WALTER. This session has no `ListAgents` tool, so the packet waits in WALTER's inbox (the ASK is not time-critical).
- **SKIPPED:** independent read of tonight's dispositions. None was requested, and none was run.

## COMPLETION — OTTO — 2026-09-30
STATUS: ✅ DONE
CHANGED: AGENTS/OTTO/{thesis/PREDICTIONS.tsv, thesis/PREDICTIONS_ARCHIVE.md, docket/CATALYSTS.tsv, STATUS.md, STATUS_COLD.md, NEXUS_BRIEF.md, workbook/ML.tsv, research/2026-09-30_RC2_evidence_receipts.md, MEMORY.md, LAST_COMPLETION.md, board_log.tsv, inbox→processed}; AGENTS/WALTER/inbox packet; this memo
RESULT: RC2 TRUE ×3, no outcome flipped. OTTO-10 → NEEDS_VERIFY (Equifax read through May 2026, the claim runs through Q3); OTTO-29 VERIFIED on Verita's 1,448-entry docket (TFR projected 9/30/2030); OTTO-06 FALSIFIED but calibration-ineligible. Verified + eligible = 1 of 2, mean Brier 0.2925 (n=2; was 1 of 4 / 0.3744 as graded). RC3: brief First Brands/OTTO-32 statements reconciled and the poll row retired.
GAPS: OTTO-10's Jun–Sep 2026 data are unpublished (expected Dec edition). OTTO-29: PACER not read (spend), 3 pre-4/15 entry numbers absent from both mirrors. predictions_due.py does not surface NEEDS_VERIFY rows (the CATALYSTS 12-15 row is the only boot surface). No independent read; no ListAgents tool for the WALTER doorbell.
WILL_NEEDS: None.
FOLLOW-UP: PROME carries the text above into HEARTBEAT, DOCKET L524 and HANDOFF. ~Dec 15: OTTO re-grades OTTO-10 at the covering Equifax edition. WALTER refreshes REGISTRY row 23.
