# BOND SCRATCH — 2026-11-12 standard closeout (desktop, PROME prome-e8 wake, WQ-184 C6); closeout 16:2x ET on PROME's ask (Will 16:11 ET)

> STATE AT WRITING (16:2x ET): Composite **17/35** (5+3+2+3+1+1+2, unchanged). **Clean-nominal counter 1** (0 → 1 on the 11/12 registered clean 30Y); auction health 3. Outside composite: **VX-BND-17 = 1** (2 → 1 at 201bp same-date, PROME class C10). **OPEN predictions 4 (BND-34 to 37), earliest resolution 12/17.** Position: **FLAT** per the FORGE 10/30 reconcile (last broker capture 10/30 intraday; FORGE stale mirror); WQ-592 declined; NO-ADD WQ280. Latest official cells: Treasury 2Y/10Y/30Y 4.86/5.10/5.43 [11/12]; real 10Y 2.86 [11/12]; 5Y5Y 2.15 [11/10]; Bund 3.29 [11/6]; HY/CCC/IG 330/1330/90 [FRED-dated 11/11]; SOFR−IORB +2 [11/5]; FR2004 long-end $150.760B [as-of 11/4]; PMMS 7.11 [11/12]; ACM 0.6503 [11/10]. THESIS v1.2.13, token unchanged.

## WHAT I DID

PROME prome-e8 due-row wake (WQ-184 C6, not a new word from Will). Limits: quiet mode, no trade construction, no gate/band/score/threshold change without Will (PROME later clarified: a score by its own existing letter is class C10).

- **Boot:** root CLAUDE.md, AGENTS.md, USER.md, COMPLETION_SPEC, local CLAUDE.md read explicitly (no local AGENTS.md). `AGENTS/BOND/.venv` absent; repo-root `.venv` used. docket_check rc=2 (TreasuryDirect timeout) then rc=0 (verified through 11/19). boot_recompute rc=1: T5YIFR distance 31 → 35bp (fixed); VX-BND-17 watcher GAP (no FRED DGS10 11/10).
- **30Y `912810UY2` REGISTERED grade 13:05 ET (first run rc=2 timeout):** indirect 68.11 / direct 20.50 / dealer 11.39, BTC 2.36, high 5.441. I′ 63.89 NO (+4.22pp); OLD NO; cover NO. CLEAN. Counter 0 → 1; health held 3. BND-33 30Y leg recorded, not regraded: TRUE stands (2 of 3 legs). KB-BND-569; `analysis/2026-11-12_30y/`.
- **Yen attribution (SAM + PROME packets read first):** result ordinary; indirect not country-identified; cannot show Japan buying, selling or absent; first evidence H.4.1 custody 11/19, MOF month-end ~11/30. KB-BND-571.
- **Treasury 11/10 close** KB-BND-570 (curve cells superseded) → **11/12 close** KB-BND-573: 2Y 4.86, 10Y 5.10, 30Y 5.43 (+13/+12/+8 vs 11/10); real 10Y 2.86; 30Y ≥5.00 run 90 (106 of 217); real 10Y ≥2.50 run 44.
- **VX-BND-17 2 → 1:** PMMS 7.11 − 10Y 5.10 [both 11/12] = 201bp, applied under PROME class C10 (cross-session). Mixed-date 213bp held at 2 earlier, superseded.
- **FR2004 as-of 11/4** KB-BND-574: long end $150.760B (+3.814); 11–21Y 71.419, highest since 7/8. VX-BND-04 held 2 (one build after two falls).
- **Inbox:** PROME yen packet, SAM correction, WQ-671 ruling (ORACLE owns December pricing, KB-BND-572), DAEDALUS WQ-678 (A14 applied to CLAUDE.md; M52–M65 deferred, not declined) → processed. WALTER 11/11-011, -015, 11/12-005, -007 (tail declined), -008 (matches KB-BND-573) → processed, board_log rows.

## NOT MOVED

No gate, band or threshold. Composite 17. Token unchanged. VX-BND-04 held 2. ⚠️ VX-BND-01 Threshold_Red text (8/27) vs the 9/15 practice: carried, not re-ruled.

## UNPUBLISHED OR UNREAD

FRED DGS10/T5YIFR/T10YIE/ACM 11/12 rows · ICE 11/12 (FRED ~11/13) · SOFR/EFFR 11/6 onward · Bund after 11/6 · KW after 11/6.

## NEXT SESSION (dated)

1. **By 11/17: freeze bars** for the 20Y new issue (11/18, $16B) and 10Y TIPS reopening (11/19, $19B): `grade_auction.py --cusip <X>` pre-print, write `registry/auction_bars/`.
2. **VX-BND-20 11/11 review: NOT serviced** (owed; do it at next boot).
3. 11/13 FHLB CFR (L226), FRBNY FX report, ICE 11/12; 11/17 F2 op 20–30Y; 11/19 H.4.1 custody (first yen-related evidence), freeze month-end bars; FR2004 as-of 11/18 is the first to show the refunding settlement (11/16).
4. Before 12/2: register any 12/9 curve-shape row with a base rate. R1, R5 and the shared-HEAD digest defect still with Will / CATO-DAEDALUS.
5. Check BND-34 and BND-37 for early TRUE at each read. 12/17 BND-36 (now $6.040B short); 12/31 BND-34, 35, 37.
6. Quiet session: WQ-678 Changelist B trims M52–M65; `monitors/rates_context.py` still labels HENRY as December owner (ORACLE per WQ-671; code with selftest, left for a quiet session).

## OPEN THREADS

Whether two refunding I′ fires (3Y, 10Y) should move auction health is Will's if he wants it. L226 FHLB retune waits on 11/13. True CDX, pulled-deal census, private funding unchanged. WQ291 funding window UNGRADED. BLS 403 here.

## CLOSEOUT STEPS (standard)

C1 STATUS done (top line, frontiers, dashboard curves/real/spreads/PMMS/FR2004, gates, matrix row 1, outside-composite line, falsifier, catalysts, bottom line) · C2 KB 569–574 (568 SUPERSEDED; 570 curve cells superseded by 573, credit cells current; 497 STALE); VX-BND-01, -04, -17; FLOW no-op · C3 no row DUE; BND-33 30Y leg noted, not regraded · C4 no-op, token unchanged (VX-BND-17 is outside the token) · C5 30Y, BND-33, FR2004 rows marked; STATUS twin updated · C6 TRADE no-op, no gate or position change · C7 this file · C8 RECEIPT rewritten; board_log 5 rows · C9 no new lesson · C11 NEXUS_BRIEF re-pinned last. · C12 root 1c: consumer scan RAN with `--superseded 213bp 201bp` (16:23 ET runs): cross 🔴 = HOMER's own mixed-date 10Y-FRM spread (packeted, `AGENTS/HOMER/inbox/2026-11-12_from-BOND_10Y-FRM-spread-same-date-201bp.md`) and HENRY STATUS:46 (BB OAS, different series, no packet); self 🔴 KB-BND-570 fixed in place (marker beside 201bp). ⚠️ RUNNER DEFECT, carried: on any second same-day run the `--self` scan reads the runner's own `registry/closeout_runs/<date>.transcript.md`, which quotes the old figure, so it can never clear; the passing run is therefore WITHOUT `--superseded` (consumer step NOT-APPLICABLE on that row), stated here, not hidden. Fix = exclude `registry/closeout_runs/` from the self scan (quiet session).

## POSITION

FLAT on this thesis. BOND executes nothing; no expiry reminders.

## MAIL / DELIVERY

Sent: `PROME/inbox/2026-11-12_from-BOND_30Y-graded-clean-refunding-closed-11-10-close-inbox-drained.md` (753a23b0dd) and `..._addendum-fr2004-11-4-and-vx17-same-date.md` (9bdd57186c), both consumed by PROME. SendMessage doorbells to prome-e8; replies to walter-42.
