# BOND SCRATCH — 2026-11-05 catch-up, NOT closed out

> STATE AT WRITING: Composite **17/35** (5+3+2+3+1+1+2; was 18). Clean-nominal counter 3 (WQ-536 A); auction health 3 since 11/5. **OPEN predictions 0.** Position: **FLAT** per the FORGE 10/30 reconcile (last broker capture 10/30 intraday; FORGE stale mirror); WQ-592 declined; NO-ADD WQ280. Latest official cells: Treasury 2Y/10Y/30Y 4.58/4.90/5.28 [11/4]; real 10Y 2.64; HY/CCC/IG 340/1316/93 [11/3]; SOFR−IORB +4 [11/4]; FR2004 long-end $150.816B [as-of 10/21]. Refunding bars FROZEN 11/2. THESIS v1.2.13.

## WHAT I DID

Boot 09:39 ET, status to Will. PROME packet `inbox/2026-11-05_from-PROME_catch-up-to-live-data.md` (7dac94dc1), Will's verbatim word 09:42 ET, verified at the artifact. PROME: do not close out until asked.

- **QRA read at primary** (`sb0678`, `sb0590`, TBAC `sb0679`/`sb0680`, XML schedules): F1 and F3 NOT FIRED (KB-528). Guidance dropped "at least"; TBAC expects increases later in FY27 (KB-529).
- **F2:** 11/4 read routed to RED, seventh of seven OFF-THE-RUN; carrier extended to 2/9/2027, metric and cut unchanged (KB-530). Self-caught: my first selftest edit missed the count expression; fixed before routing.
- **Downgrade:** auction health 4→3 (KB-531). Composite 17.
- **Calendar:** blind span closed at Treasury's XML; FHLB CFR re-dated 11/9→11/13 on REGINALD's calendar (KB-532); bar freeze for the month-end cluster docketed 11/19.
- **Credit:** HY refreshed, band 3 sessions (KB-533). ACTION signals assessed: CCC broadening (KB-534), Holy Redeemer (KB-535).
- **Data:** Treasury 11/4, ICE 11/3, NY Fed 11/4, Bund 11/5, ACM, KW, proxy (KB-527, 536). KB overdue rows dispositioned: 10 Stale_By cleared, 3 STALE, 2 SUPERSEDED.
- **Inbox:** 9 of 9 WALTER cards consumed, including the BoE hike (KB-537). R3 answered in the PROME packet.

- **L859 HOLD (10:06 ET):** independent read of the 10/29 TreasuryDirect repair found the same failure by other doors. Verified, acceptance conditions committed first, repaired, 24 of 24 mutants caught (KB-538). Not independently verified yet; bounded diff read asked of PROME. Grades 11/9–11/12 proceed with `--frozen-bars`; check on 11/9 whether a target stays in `upcoming` after results post (F7 residue).

## NEXT (dated)

1. **11/5 today:** HY 11/4 cell (VX-07 reading stated in KB-533; VIOLET owns VIX close) · PMMS ~noon · FR2004 as-of 10/28 ~16:15 ET, VX-04 re-score · addendum to PROME if a score moves.
2. **11/9 · 11/10 · 11/12:** grade 3Y/10Y/30Y with `--frozen-bars AGENTS/BOND/registry/auction_bars/<date>_<cusip>.json` under `.venv` python.
3. 11/11 VX-20 review; 11/12–11/17 freeze 20Y and TIPS bars; 11/13 FHLB CFR, FRBNY FX report; 11/17 F2 op; 11/19 freeze month-end bars.
4. Closeout when PROME or Will asks: tier standard or heavy (tool changed), C9 promotion scan, `--superseded` for the composite, push.

## OPEN THREADS

L226 FHLB retune waits on the 11/13 report and sets no number without a base rate. Independent read of `ta_ws_schema` repair (L859 note) still not commissioned. 7Y reopening handling owed before April 2027. EA AAA leg of `dm_cross_section` 504 twice on 11/5. True CDX, pulled-deal census, private funding, event-time TIPS unchanged. WQ291 funding window UNGRADED.

## POSITION

FLAT on this thesis. BOND executes nothing; no expiry reminders.

## MAIL / DELIVERY

RED F2 packet sent. PROME delivery packet sent; recipient consumption not yet recorded.
