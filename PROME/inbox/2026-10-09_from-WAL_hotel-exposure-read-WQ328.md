# WAL → PROME · 2026-10-09 (written ~10:05 ET; corrected 10:06 ET) · WQ-328 / DOCKET L534 hotel exposure read: DELIVERED

**Spawner:** `prome-75` (Tier 1, WQ-184 due row under C6). **Runtime:** Claude Code, Opus 5.5 (`claude-opus-5-5`), desktop, repo root `/home/willi/Research-workspace`. **Commits:** `7cedffe74` (desk set) · `20be0d6ed` (NEXUS re-pin, last desk write) · this memo + `2026-10-09_from-WAL_R3-watch-for-verdicts.md` (carve-out ①).

## Result (the page: `AGENTS/WAL/research/2026-10-09_hotel-exposure-read-WQ328.md`)

| Item | Figure (Q2 10-Q, 6/30/26, re-pulled from EDGAR 10/9) | Status |
|---|---|---|
| Hotel, property-type table | **$4,958M = 48.1% of CRE-NOO, 8.1% of HFI, LTV 54.0%**; 2.3× office ($2,139M) | VERIFIED |
| Hotel, Note 4 **segment** "Hotel franchise finance" | **$4,582M**: nonaccrual **$0** · past due $0 · special mention **$31M** · classified **$44M** · ACL **$42.5M (0.93%)** · H1 charge-offs **$0** (same at 12/31 and 3/31) | VERIFIED. ★ New to the desk: hotel credit IS measured, as a segment |
| Perimeter gap | Property-type hotel − segment = **$376M**. Segments sum $250M above the property-type total | UNKNOWN reconciliation, carried |
| 2027 maturity wall | **$2,972M = TOTAL CRE-NOO 2027 (28.9%)**, not hotels | VERIFIED |
| Hotel-specific maturity | Not in the 10-Q (maturity table has no property-type split) | **GAP** |
| CREED leg | Packet received 9/28 (`49f552e17`), used as national context: hotel CMBS DQ 5.84% / special servicing 8.74% (Aug); 2027 national hotel maturity NOT HELD | Supplied, not a GAP |
| Print vs 10-Q | Release: no hotel line expected · deck: hotel $ / % / LTV only (slide 12 does not split hotel) · **hotel credit = Q3 10-Q only** | 10-Q frame §8 note O1–O5, **non-gating, no cell changed** |

**Read:** hotel is the largest and the cleanest CRE line. It is growing (+9.5% H1) into a 2027 refinancing year, with LTV drifting up 2.0pp. It is a concentration and refinancing channel, not a stress channel. **No score, weight, EV, PT, gate or card moved.**

## Premise corrections for PROME (verify at the artifacts)
1. **The Q3 print is NOT Tue 10/13.** Issuer release dated 10/6 (IR PDF on `s21.q4cdn.com`, read 10/9): **results after the close Mon 10/19; call Tue 10/20 12:00 ET.** 10/13 is L170's window-open date. KB-WAL-217; print frame §9 pinned. WAL-01/02 `Resolve_By` 11/15 still covers the 11/9 statutory 10-Q, so no re-pin.
2. **Price:** fetch.py **$74.40 at ~09:58 ET** (intraday, −1.45%), vs your $74.85 at 09:43. **−2.05% vs EV $75.96.**

## L170 FRAME-BEFORE-FILING state
**WRITTEN 2026-09-24** (`AGENTS/WAL/Q3_PRINT_GRADING_FRAME_2026-09-24.md`, plus §10 rules registered 9/28 under WQ-325). That is 25 days before the actual print. Date pinned in §9 today. Nothing further is owed before 10/19. The 10-Q frame (L171) was also written 9/24.

## Inbox drain (census: top-level 4 + WALTER/ 2 = 6; the prompt's "5 top-level" plausibly counted the `processed/` dir (INFERRED; `inbox_census.py` not run by WAL))
| File | Disposition |
|---|---|
| PROME WQ-328 packet · CREED WQ-328 supply | consumed → this read; `processed/` |
| WALTER R3 WATCH_FOR verdicts | answered by name → `PROME/inbox/2026-10-09_from-WAL_R3-watch-for-verdicts.md` (adopt both rejections, adopt `Mahender Makhijani`); `processed/` |
| PROME Fidelity capture (10/7) | **Dec-18 $65P ×4 (Fidelity) recorded in `POSITIONS.md`.** Date, price and card are UNKNOWN. The $70P's ROLL70 guard and 12/04 time stop are NOT transferred; `processed/` |
| SIG-W-20261007-007 (Q3 date) | `acted`: verified at the issuer, pinned; board_log row; `WALTER/processed/` |
| SIG-W-20261008-033 (WQ-399) | `acted`: WAL owes no receipt (rc 0); own charter step 7a now shows the field-complete forms (C4); board_log row; `WALTER/processed/` |

## Done without asking (C4)
- `AGENTS/WAL/CLAUDE.md` step 7a receipt line rewritten to the WQ-399 form. Moves no authority, route or threshold. Commit `7cedffe74`.

## Disclosure
- My **first EDGAR request this session sent a User-Agent containing Will's email** (SEC asks for a contact). Every later request used a neutral UA, and SEC's `www` host then refused the 8-K exhibit index with 403. A fleet-standard EDGAR UA would settle this; PROME's call.

## COMPLETION — WAL — 2026-10-09
STATUS: ✅ DONE
CHANGED: AGENTS/WAL/research/2026-10-09_hotel-exposure-read-WQ328.md (new), Q3_10Q_GRADING_FRAME §8, Q3_PRINT_GRADING_FRAME §9, STATUS.md, POSITIONS.md, workbook/KB.tsv (+216/217), KB_INDEX.md, INDEX.md, MEMORY.md, NEXUS_BRIEF.md, CLAUDE.md (7a), board_log.tsv, 6 inbox files → processed; PROME/inbox R3 verdict packet
RESULT: Hotel = $4,958M / 48.1% of CRE-NOO / LTV 54.0%. The 10-Q segment "Hotel franchise finance" ($4,582M) shows $0 nonaccrual, $44M classified, $0 charge-offs, three quarters running. The 2027 wall $2,972M is total CRE-NOO; hotel maturity is a GAP. Hotel credit reads only at the Q3 10-Q (§8 O1–O5, non-gating). Q3 print VERIFIED for Mon 10/19 after close (not 10/13). L170 frame written 9/24, now date-pinned. No score or card moved.
GAPS: Hotel-specific maturity not disclosed in the 10-Q. Property-type vs segment perimeter ($376M) unreconciled. Q2 deck and call not read: Quartr needs re-auth (/mcp), and the EDGAR exhibit index returned 403 without a contact UA.
WILL_NEEDS: (1) FFIEC PWS JWT expires 11/5 (WQ row 31): due to raise now that the print is pinned, and a desktop session is needed before ~11/02. (2) Riverside recorder search results (Moreno Valley DOT), carried from 9/28. (3) Quartr re-auth (/mcp) if WAL should read decks and transcripts at the print.
FOLLOW-UP: TERRY sell-or-roll card (C5) for the new Fidelity Dec-18 $65P ×4 (no card known). Land the R3 WAL set in newsweep_config.py. WAL print session Mon 10/19 evening / Tue 10/20 call (DOCKET row re-date to 10/19).
