# LABOR → PROME · 2026-10-08 08:39 ET · Claims w/e Oct 3 graded (score 28 → 26/75) · Canada re-check #1 NO EVIDENCE · inbox drained

**Spawn:** `prome-fc` Tier-1 due-row wake under WQ-389. Brief `PROME/tasks/2026-10-08_wakes/LABOR.md` + `COMMON.md`, both read whole.
**Runtime:** Claude Code subagent, model Opus 5.5 (`claude-opus-5-5`); tools used: Bash, Read/Write, WebSearch, SendMessage. Root `CLAUDE.md`, `AGENTS.md`, `USER.md`, `AGENTS/LABOR/CLAUDE.md` (spawned-mode card + B/C protocol) read explicitly. No missing dependency blocked the task. Two MCP servers (definite, Prisma-Local) failed to connect; neither was needed.
**Boot gates:** B2 `boot.py --verbose` run; B2a spine gate PASS before the print and PASS again at 08:38 after FRED updated · B5b one live card (10/8) + the graded-but-unmoved 10/2 NFP card · B5c corrections check rc=0 · required-card check clean.

## 1 · Claims w/e Oct 3 + CC w/e Sep 26 — GRADED off the frozen card (§9)

**Source:** DOL/ETA release 2026-10-08 08:30 ET. Fetched 08:30:20 with plain `curl`, saved as a PDF, text-extracted, embargo line checked, and every figure checked against the extracted text. FRED agreed by 08:38.

| Step | Result |
|---|---|
| ① Three quantities regenerated before reading the level | `R` = 207,000, unchanged, so `ΔMA` is exact at −2,500. Retained trio 593,000 → **595,000** (w/e Sep 26 revised 197 → 199K), so the `MA_next` column was off by +500 (third week running, L-31). T-01 bound 407,000 → **405,000** |
| §2 single print | **197,000 ⇒ band B, NO ACTION** |
| §5a T-01 (MA basis) | T01-a. MA **198,000**, `250,000 − 198,000 = 52,000` below |
| §5b v13 `<200K ×4` | Sep 12 198K · Sep 19 198K · Sep 26 **199K (rev; margin 1,000)** · Oct 3 197K ⇒ **4 of 4 ⇒ v13 2 → 1** |
| §5c v7 CC `<1,750K ×4` | Sep 5 1,717K · Sep 12 1,712K · Sep 19 1,699K (rev) · Sep 26 **1,716K** ⇒ **4 of 4 ⇒ v7 3 → 2** |
| Kill B | 0 of 5 |
| **Score** | **28 → 26/75** (`26/75 = 34.7%`). Nothing fired, so no WALTER signal |

⚠️ **The MA's drop to 198,000 is mechanical.** All of it comes from the 207,000 week rolling off. The v13 run's last week cleared by **1,000** after a +2,000 revision. These are de-escalations on level thresholds, not a call on what is driving claims.

⚠️ **Neither vector has a registered letter that moves it back up.** Only a 230,000+ print (v13 → 3) or T-01 would raise them. This is parked as a letter question (STATUS pickup 2, fold-by 10/22); the 10/15 card treats both streaks as record-only and invents no bands.

**Routing (card §7):** direct 🟡 note to CARL (`1ab3ff012`); STATUS and NEXUS brief updated. Card moved to `docket/graded/`. ⚠️ Your brief `PROME/tasks/2026-10-08_wakes/LABOR.md` cites the old top-level card path, which no longer exists.

**Next card frozen:** `AGENTS/LABOR/docket/GRADING_CARD_20261015_claims.md`, built from the 10/8 as-published window, not copied forward.
- `R` = 198,000, so `ΔMA = (X − 198,000)/4`. The roll-off tailwind is spent: a repeat 197K print moves the MA only −250.
- T-01 MA bound: `X > 406,000`.
- Partition check: 0 defects; tables 4–6 hand-proved.
- CATALYSTS row re-docketed for **Thu 10/15 08:30**.

## 2 · Canadian counter-tariff US-exporter employment re-check #1 — GRADED: NO EVIDENCE

I applied the 9/10 rule verbatim and wrote the cohort ratio first: `0 / 20,000 = 0%`.

| State primary | Read to | Post-9/8 ag-equipment / pulp & paper notice? | Cites Canada / export orders? | Token |
|---|---|---|---|---|
| IL — IEBS public WARN search (the data behind the DCEO search page) | last report 9/28, 25 records | none | none. IL's own `Trade` flag is false on all 25 | **VERIFIED absent** |
| IA — IWD WARN Event Log (xlsx) | newest notice 9/30 | none (CNH Burlington and Deere notices all pre-date 9/8) | none | **VERIFIED absent** |
| WI — DWD WARN sheet (CSV) | newest notice 10/04 | none (2026 paper-mill notices all pre-date 9/8) | none | **VERIFIED absent** |
| MN — DEED reports page | — | — | — | **SEARCH-NOT-FOUND.** The page was captcha-blocked. The one full response I got was overwritten before parsing (my error). Indexed monthly PDFs stop at July |

- **This means "no evidence", not "no effect."** The 9/10 row derived ~11/7 as the earliest effective date for layoffs decided after 9/8, and WARN misses furloughs and cuts in hours.
- Colour, graded by nothing (secondary source): CLAAS moved assembly of Canada-bound combines from Nebraska to Germany citing tariffs, and says there will be no Nebraska layoffs.
- **Re-check #2 is docketed for 2026-11-09** (NOCARD), with the working data routes written into its row.
- Record: `AGENTS/LABOR/domain/sources/2026-10-08_CANADA_COUNTERTARIFF_RECHECK1.md`; KB-LAB-203.

## 3 · Whole-inbox drain — 0 top-level + 2 WALTER, both logged (`board_log.tsv`, `consume:LABOR`)

- **SIG-W-20261007-013 — acted.**
  - Workday's 9/29 8-K, read at the SEC: a ~2.5% workforce cut, $65–80M in charges.
  - California EDD WARN: Pleasanton, **142** workers, effective 11/30. These would show in claims around w/e Dec 5.
  - Sizing: `142 / 20,000 = 0.71%` of the national detection floor. Even the whole global cut (`525 / 20,000 = 2.6%`; 525 is inferred from the 10-K headcount) is state-level only.
  - The 8-K gives no AI reason, so nothing is attributed to v5.
  - Registered in `docket/WARN_COHORT.tsv`; KB-LAB-204.
- **SIG-W-20261007-017 — noted.** It corrects 013's cluster metadata only; the substance of 013 stands.

## Closeout controls

- **1c consumer check, `28/75 → 26/75`:** 4 🔴 hits, all dated history (WALTER route log 9/29, BOARD SIG-W-20260929-005, DAEDALUS 10/1 review). No packet sent.
- **1c consumer check, CC `1,701,000 → 1,716,000`:** 10 🔴 hits, all cold or dated surfaces (NEXUS `*_COLD`, PROME `HEARTBEAT_COLD` and a 10/1 plan, a 10/7 WALTER dashboard capture, a NEXUS 10/1 cold read). No packet sent; NEXUS reads the re-pinned brief and CARL received the direct note.
- **Ledger nudge:** `PREDICTIONS.tsv` was not touched because no prediction rode this print. `PAYROLL_VINTAGES.tsv` refreshes only on NFP prints (next 11/6).
- **Other checks:**
  - Read-cap: STATUS **22,123 B**, under the 22,785 B stop. Superseded lines were rotated verbatim to `STATUS_DETAIL.md § status-rotated-20261008`.
  - Claim check clean; orphan check found nothing of mine; no auto-memory written.
  - Exit-rules vintage sweep run.
  - NEXUS brief re-pinned last (pin `360caeeb1`); I also corrected its stale LAB-18/19 values left over from 10/2.
- **Push:** I pushed under COMMON.md, as your spawn prompt directs. LABOR's own spawn card step 3 says to defer the push to the coordinator; your instruction governs.

## Not done (scoped spawn; each is re-parked with a date)

1. **`git mv` of the graded 10/2 NFP card** (owed since 10/5; fold-by 10/16). It has live citers outside LABOR: RED CATALYSTS, TERRY's QQQ setup, and `PROME/DOCKET.tsv`. That needs packets at a self-directed closeout.
2. **STATUS pickup 8 and 9 (fold-by 2026-10-09, tomorrow):** the v11 letter scope, and whether JOLTS openings get a band. Both are self-directed C2 letter decisions, and neither was in this brief.
3. **C5 retirement moves** (pickup 11): still not executed.

## COMPLETION — LABOR — 2026-10-08
STATUS: ✅ DONE
CHANGED: AGENTS/LABOR/{STATUS.md, STATUS_DETAIL.md, NEXUS_BRIEF.md, board_log.tsv, docket/CATALYSTS.tsv, docket/WARN_COHORT.tsv, docket/graded/GRADING_CARD_20261008_claims.md (moved+§9), docket/GRADING_CARD_20261015_claims.md (new), workbook/KB.tsv, workbook/PUBLISHED.tsv, domain/sources/2026-10-08_*.{md,txt}, inbox/WALTER/processed/SIG-W-20261007-013/-017}; AGENTS/CARL/inbox/2026-10-08_from-LABOR_claims-197k-two-counters-complete-score-26.md; this memo
RESULT: CATALYSTS 2026-10-08 claims row: 197,000 w/e Oct 3, band B, MA 198,000 (mechanical), CC 1,716,000; v13 2→1 and v7 3→2 on their 4-of-4 letters, score 28→26/75, nothing fired. CATALYSTS 2026-10-08 Canada row: NO EVIDENCE, with IL/IA/WI WARN primaries VERIFIED absent and MN SEARCH-NOT-FOUND. Inbox drained 2/2 (Workday CA WARN 142, state-level). 10/15 card frozen and re-docketed.
GAPS: MN DEED primary unread (captcha). Graded 10/2 NFP card still at top level (re-parked, fold-by 10/16). STATUS pickup 8/9 fold-by 10/09 and the parked return-letter question (fold-by 10/22) need a self-directed C2. Your task brief cites the old 10/8 card path.
WILL_NEEDS: None
FOLLOW-UP: Re-spawn LABOR at Thu 10/15 08:30 claims (card frozen). A self-directed LABOR session is needed before 10/09–10/16 for pickup 8/9, the 10/2 card move (RED/TERRY/PROME packets) and the return letters. ECI Q3 card is due ~10/23.
