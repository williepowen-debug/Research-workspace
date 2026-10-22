# RED → PROME — D:L35 graded: EGBN Q3 = CHG-RED-027 DETERIORATION on the letter; pre-stated Acute +1 fired → HOLD 72 · net-bear 69 (also FT-10, L791)

**Written:** 2026-10-22 11:3x ET (`date`). RED session S56, Claude Code, Opus 5.5 (`claude-opus-5-5`), PROME-spawned Tier-1 (WQ-481 A). Full grade: `AGENTS/RED/reports/2026-10-22_S56_BANK_Q3_TREE_GRADE.md`. Tree applied as written: `AGENTS/RED/research/2026-10-19_BANK_Q3_DECISION_TREE.md` (pre-data 10/14).

**Sources.** EGBN 8-K EX-99.1, sec.gov acc 0001050441-26-000110, read by RED at the primary 11:27 ET (sha256 `4eaea724…a8c7a`). Call 10/22 10:00 ET via a SECONDARY transcript (Investing.com, AI-generated and editor-reviewed per the page). sha256 UNAVAILABLE because the site refused a direct fetch. Short quotes only. Deck loan-level facts are cited from REGINALD's extract (6e3914cb2), labelled as such.

## Verdicts
| Object | Result | Basis |
|---|---|---|
| **CHG-RED-027 (D:L35)** | **DETERIORATION**, row stays ACTIVE, re-review EGBN Q4 (~1/28/2027 est.) | E1 NCO **0.25%** (Q2 2.78%): CLEARING's NCO leg met. E2 NPAs **$166,021K vs $113,090K**: rose, so CLEARING fails. E3 EGBN's own rollforward, inflows **$73.7M > reductions $18.8M**: the DETERIORATION OR-leg fires. E6 order: release, then call, then grade |
| **Acute ±1 (tree II, pre-stated, DISCRETIONARY label)** | **+1 from Managed: Acute 19→20 · Managed 24→23 · net-bear 68→69 · HOLD 72 unchanged** | EGBN DETERIORATION + OZK adverse on card W9 (owner's grade: Boston 10 Prospect sale failed, title taken after a **$37.3M** charge-off, OREO $132.0M). OZK-09 STUCK. Provision < PPNR. No same-day bull fire |
| **CHG-RED-054** | lead **STRONG → MODERATE**. OZK leg → MODERATE. WAL unchanged MODERATE ($99M silent, so it waits for the 10-Q). KRE unchanged. Re-review 11/09 | tree §III; RED grades the reasoning only |
| **CHG-RED-049** | CARL CRL-29 = PANEL NO VERDICT (registered null). Re-review 11/15 Nov HHDC | CARL packet 10/21 |
| **FT-10** | Cboe publisher pull 11:28 ET: **150.36 [10/21]**. State FIRED (executed 10/14). **Exit leg <140 strict ×4: 0 of 4.** **10/22 bar PENDING**: this session closes before the 16:00 ET close | Rule: grade the 10/22 bar on the exit leg only. Four consecutive Cboe closes <140.00 ⇒ Acute −2 / Managed +2. The ≥150 count is not a RED action line after the fire |
| **L791** (EGBN $56.0M loan, 12/21) | Accepted as RED's bank-tree context. A RED catalyst row was added (12/21), and the CHG-027 Q4 re-review row carries it | call: a specific reserve exists, amount undisclosed; a subordinate lienholder; borrower declined to support a restructuring (secondary) |

## ⚠️ Caveats that must travel with the +1 (anti-laundering)
1. **One loan carries the EGBN verdict.** 76% of inflows is the already-substandard $56.0M Prince George's affordable multifamily loan. **Without that loan, the cell reads CLEARING** (inflows ≈$17.7M < $18.8M; NPAs ≈$110.0M < $113.1M; reader arithmetic). Everything else cleared: criticized + classified $759.6M → $648.4M; 30–89 days past due $44.1M → $0.36M. The letter governs. A single-name clause added after the data would be fitting the rule to the result (ML-RED-303).
2. **Bear evidence beside it:** reserve coverage of problem loans fell **109% → 73%** (verified at the primary: 109.01% → 72.75%) while the office overlay was released. **$265.7M of multifamily matures in Q4-26.** The December wall is the binding test.
3. **Tree drafting ambiguity, disclosed:** row 3 says "or OZK-09 still STUCK → none". RED reads STUCK as "not evidence", not as a veto over the W9 leg. Under the veto reading there is **no move: net-bear stays 68**. Both qualifying legs are single names inside prints their owners grade as net contrary to stress (OZK conviction → LOW, WQ-483 A).
4. **The market disagrees with the letter:** EGBN **+10.9% intraday** 10/22 (31.63 vs 28.53, 11:28 ET; close pending). If it holds, that is outside TERRY #18's envelope (0 of 32 regional-bank prints moved ≥10%). Recorded; it scores nothing.

**Consumer check (net-bear 68 → 69):** 2 cross-fleet hits. Both are dated records (a DAEDALUS commit-list evidence file; a 7/31 BOARD signal), not live consumers, so no packet was sent. NEXUS brief refreshed (vS56).

**Inbox drained:** CARL CRL-29 packet → `inbox/processed/`. WALTER SIG-W-20261021-013 → `inbox/WALTER/processed/`. BOARD SIG-W-20261022-011 noted. 3 board_log rows. No expiry or disposition language anywhere; book per FORGE ec5a7058b; RED has no trade view.

## COMPLETION — RED — 2026-10-22
STATUS: ✅ DONE (task) · closeout headline PARTIAL: git pull SKIPPED (tree carries other desks' work; 0 behind origin at 11:29 ET)
CHANGED: AGENTS/RED/{STATUS,SCRATCH,CALENDAR,OUTBOX,NEXUS_BRIEF}.md, thesis/CHANGELOG.md, workbook/{CHALLENGES,ML}.tsv, docket/CATALYSTS.tsv, board_log.tsv (+archive rotation), reports/2026-10-22_S56_* (grade, NEXUS vS55 rotation), inbox moves ×2; this packet; FORUM/banks post
RESULT: D:L35 graded at the primary. CHG-027 = DETERIORATION (E3 inflows $73.7M > reductions $18.8M; NPAs $166.0M vs $113.1M; NCO 0.25%). With OZK W9 the pre-stated Acute +1 fired: HOLD 72 · net-bear 69. CHG-054 → MODERATE; CHG-049 NO VERDICT → 11/15. Composition caveat: one legacy $56.0M loan; ex-loan = CLEARING.
GAPS: FT-10 10/22 bar and EGBN 10/22 close PENDING (after 16:00 ET). Call read from a secondary transcript only (no sha256). EGBN deck not re-read by RED (REGINALD extract cited).
WILL_NEEDS: None (the tree row-3 reading is disclosed; a veto reading would revert to net-bear 68 — flag only if PROME/Will disagree).
FOLLOW-UP: FT-10 10/22 bar at RED's next boot; RED re-derivation not before Fri 10/23; CHG-054 11/09; EGBN Q4 ~1/28 (DOCKET L35 successor row for PROME).
