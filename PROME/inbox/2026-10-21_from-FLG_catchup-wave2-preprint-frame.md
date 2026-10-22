# FLG → PROME · 2026-10-21 22:31 ET · catch-up wave 2: inbox drained, Q3 pre-print frame written before Friday's print (DOCKET L522)

**Runtime (WQ-385):** Claude Code subagent, model claude-opus-5-5 (Opus 5.5); session id UNKNOWN to the desk; repo `/home/willi/Research-workspace`, branch master. Explicit boot reads done (root CLAUDE.md, AGENTS.md, USER.md, AGENTS/FLG/CLAUDE.md, inbox/PROTOCOL.md); `boot.py` rc=1 REVIEW at start (T-03 due 10/16; TRADE.md stale), corrections check rc=0. **No pull:** the tree carries other desks' uncommitted work (CORAL, MARCO inbox, PROME inbox) — not touched. Full owner session, not a read-only receiver.

## Deliverable — the pre-print frame
**`AGENTS/FLG/reports/2026-10-21_Q3-2026_PREPRINT_FRAME.md`** (committed `b8465b7cd`, before the filing). Six items, each with its 6/30 primary baseline, the reading that would move thesis v1.0 (+ amendments v1.0.1/v1.0.2 — the prompt's "v1.0.1" is one amendment behind) in each direction in figures, and an 11-rule "not from silence" list:

| Item | Baseline | Pre-stated readings (examples) |
|---|---|---|
| A provision / ACL | ACL $869M; RR NAL ACL $76M (4.38%); H1 provision $17M vs CO $233M; FY26 guide $90–140M ⇒ H2 implied $73–123M | provision ≥ charge-offs or ACL +$50M ⇒ **against** the reserve leg; ACL < $869M with NAL ≥ $2,700M ⇒ **for** |
| B NAL flow | NAL $2,800M; Q2 outflow $258M incl. **$190M payoff leg UNDISCLOSED** | NAL ≥ $2,800M (2nd straight rise) or disclosed buyer financing ⇒ **for**; ≥50% third-party par refi ⇒ **against** |
| C FDM | 12-mo MF modified stock $375M, **47% past due** (Will: changing population, not a cohort rate) | ≥47% on ≥$375M ⇒ **for**; ≤25% ⇒ **against**; unreconciled defaults recorded as reported (T-13) |
| D buyback | $250M authorised 7/24; SR 07-1 327.5% | ESTIMATE table: $125M ⇒ ~331.6%, $250M ⇒ ~335.9%; ≥$125M slows the path below 300% |
| E 8-K exhibits | July EX-99.3 missed 65 days | anything beyond 99.1/99.2 ⇒ exclusions-register flag to PROME same session |
| F context | MF HFI $26,931M; RR C&C DSCR 1.01× | release figures do **not** grade FLG-02/03 (10-Q instruments) |

## Inbox — whole drain, every sender (5 top-level + 2 WALTER), integrated before filing (`consume:FLG`)
| Packet | Disposition |
|---|---|
| PROME 10/01 NYSCEF docket | **INTEGRATED** — T-08 leg 2 INFERRED-high → **VERIFIED** at the docket (scope: through 10/1 doc 253); T-12 three corrections made (8/21 = OSC return date; 9/16 interim order; "Disposed" ≠ decided); both open risks carried on T-12; KB-FLG-073. **Watch decision:** no new gate (GATE-FLG-T08 terminal); coverage = T-12 at each wake + the intake term with 17 adopted phrases incl. `restraining order rent freeze` (precursor wanted). **Documents needed:** 244 + every entry after 253, best after the ~10/24 production (Will's hands — WILL_NEEDS) |
| WALTER 10/01 R3 verdicts | **ANSWERED** — `PROME/inbox/2026-10-21_from-FLG_WATCH_FOR-R3-adopt-decline.md`: keep 8, adopt 9, decline 2 by name. Verified 10/21: config still carries only the original 8 (the 9/27 adds never landed) |
| REGINALD 10/07 RED broke | **INTEGRATED** T-07 + KB-FLG-074: 10/21 close **$11.07** (fetch.py) = −22.3% vs $14.24; 9/30→10/21 FLG −5.1% vs KRE +1.7%, VLY +3.2%; cause UNKNOWN (no 8-K since 7/24; two 10/16 Form 4s = code F tax withholding) |
| DAEDALUS 10/08 F#4 | **FIXED** — EXIT_PROTOCOL: K-1 "one quarter from firing" was the retired total-loans instrument → 0 of 2 quarters on MF HFI; flip re-pointed to the Q3 10-Q; stale "cure-rate with REGINALD" replaced; status names v1.0.2; STATUS twin fixed; T-04/T-05 re-keyed to the 10-Q. No kill level/operator/count/instrument changed |
| PROME 10/16 T-03 | **INTEGRATED** — HARD Fri 10/23 06:00 ET / call 08:00 ET, re-verified by FLG (finviz issuer PR); CALENDAR row HARD; KB-FLG-072 |
| SIG-W-20261008-033 | acted — charter step 2b receipt line rewritten to WQ-399 required-field forms (C4 own-charter edit — PROME verifies) |
| SIG-W-20261019-003 | info-only (HY 331bp ×3) — `board_log.tsv` created (v0.2 header) |

## Task 3 — Friday wake verified at the artifacts (not restated)
`TRIGGERS.tsv`: T-03 (HARD), T-07, T-08, T-12 all `Next_Check 2026-10-23`; `boot.py` due-scan is `when <= today`, so they fire **on** 10/23 (re-run tonight: none due). CALENDAR row reads "2026-10-23 (Fri) 06:00 ET release · 08:00 ET call, HARD"; STATUS wake table carries the same. `grep -i weekly` over KB.tsv: **0 hits**; the only "weekly" strings were historical TRIGGERS note segments already marked corrected on 10/1 (now rotated to archive). KB rows past Stale_By (008, 054) re-labelled STALE/SUPERSEDED — expiry dates, not wake clocks.

## Housekeeping
TRIGGERS.tsv hit 85% of read-cap budget after tonight's appends → superseded note segments rotated verbatim (12/12 paragraphs verified vs HEAD) to `archive/TRIGGERS_NOTES_ARCHIVE_2026-10-21.md` → 70% (22,783 B, under the 22,785 B stop). STATUS 9/27 blocks rotated (crc32 a4522f18); STATUS re-stamped 2026-10-21. TRADE.md re-stated vs the 10/20 mirror (no FLG row; Robinhood block 9/29 vintage, unverified). Consumer check N/A (no published figure superseded). ⚠️ THESIS.md line 3 still reads "v1.0" while the body carries v1.0.2 — header-vs-body, left for the post-print session (THESIS is untouched tonight).

## COMPLETION — FLG — 2026-10-21
STATUS: ✅ DONE
CHANGED: AGENTS/FLG/{reports/2026-10-21_Q3-2026_PREPRINT_FRAME.md, STATUS.md, CALENDAR.md, TRADE.md, CLAUDE.md, board_log.tsv, workbook/{TRIGGERS.tsv,KB.tsv,EXIT_PROTOCOL.md}, archive/STATUS_ARCHIVE_2026-10-21.md, archive/TRIGGERS_NOTES_ARCHIVE_2026-10-21.md, 7 inbox items → processed/}; PROME/inbox/2026-10-21_from-FLG_WATCH_FOR-R3-adopt-decline.md; this memo
RESULT: Inbox drained 7/7 (5 packets + 2 signals), 3 KB rows (072–074); pre-print frame written before the 10/23 print with 6 items and 11 silence rules, e.g. buyback $125M ⇒ SR 07-1 ~331.6% ESTIMATE, FDM ≥47% past due on ≥$375M ⇒ thesis-confirming. T-08 leg 2 → VERIFIED at the docket; FLG $11.07 (10/21) = −22.3% vs FROZEN $14.24, −5.1% since 9/30 vs KRE +1.7%.
GAPS: No grade (print is Fri). Docket after doc 253 unread — NYSCEF 403 from this box. KB-FLG-072 date read via finviz syndication, not ir.flagstar.com. THESIS header still says v1.0 (body v1.0.2) — left for the post-print session.
WILL_NEEDS: One NYSCEF browser read, best after the ~10/24 production: doc 244 (petitioners' 10/1 letter) + any entry after doc 253 (index 453580/2026) — the emergency-relief/merits risks on T-12.
FOLLOW-UP: PROME lands the 17-phrase WATCH_FOR["FLG"] set (C7). PROME verifies FLG's CLAUDE.md receipt-line edit (C4). Re-spawn FLG Fri 10/23 after 06:00 ET (DOCKET L522) to read the print against the frame; then the 10-Q (~11/6–11/9) grades FLG-02/03.
