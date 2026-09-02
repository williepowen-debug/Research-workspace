# BOND SCRATCH — 2026-09-02 (Wed) ~21:xx ET. PROME-spawned Tier-1 session (bond-28). Rewritten clean at closeout.

**Purpose:** ephemeral session handoff. Read at boot, rewritten at closeout. **Durable learnings → `MEMORY.md`; permanent evidence → `workbook/`. This file is disposable and must be executable COLD.**

> ## ⚠️ STATE AT HANDOFF — nothing mid-flight
> **All BOND work committed; push receipt in `RECEIPT.md`. No blocked action, no partial edit.**
> **Position UNCHANGED: TLT puts HOLD, no add. Composite 12/35 (9th consecutive). Book untouched. $0.**
> 🔴 **Add-gate 6bp away [DFII10 2.44, 9/1] — unchanged on 9/1.** 🔴 **The refunding grades 9/8–9/10 on FROZEN bars (below) — do not re-derive them, READ them.**

## CHANGES SINCE LAST HANDOFF

**1. ★ MATRIX_V2 PER-TENOR BASE-RATING DELIVERED (owed 9/4).** `analysis/2026-09-02_MATRIX_V2_per-tenor-base-rating.md` + `monitors/matrix_v2_base_rate.py`. **Out-of-sample, `I'` fires 15.6–28.1%/auction by tenor (23.2% pooled; OLD conjunctive 1.8%) with NO TLT-5d separation** (hit 50.0% vs 53.2%; median +0.14% vs −0.12%; ≤−3pp margins 31.6%; two consecutive same-tenor fires 46%). **P(≥1 fire across 9/8–9/10) ≈ 49%.** Matrix marker stands; **kill leg cannot discriminate — Will-gated question raised via PROME, NOTHING MOVED**, dual-print governs the refunding as ruled. `KB-BND-222`, THESIS v1.2.1.

**2. 🔴 THE 2Y POOL CONTAINED 43 FRN ROWS.** `floatingRate=Yes` at TA_WS, `securityType Note`, `originalSecurityTerm 2-Year`. Every 8/27 2Y bar was FRN-set: min 50.91→**53.21**, dealer max 49.09→**24.12**, `I'` 55.75→**54.82**, median 57.65→56.54. **No verdict changed.** `grade_auction.py` patched at both sources (`data/frn_cusips_ta_ws.json` cache, raises with neither). PROTOCOL / AUCTION_HEALTH / TRADE corrected with riders. `KB-BND-221`; local MEMORY + fleet auto-memory (superset finding) extended.

**3. ★ ALL SEVEN `I'` BARS FROZEN for the refunding (FRN-clean, trailing-12 strictly prior to 9/2, P15 linear, % of competitive accepted):** 2Y 54.82 · **3Y 58.90** · 5Y 60.27 · 7Y 57.24 · **10Y 65.05** · 20Y 61.72 · **30Y 62.93**. OLD conjunctive beside each in `AUCTION_HEALTH.md` §Upcoming. Reopening-only alts 10Y 66.32 / 30Y 60.28 — **pooled governs; a print inside the gap is CONVENTION-DEPENDENT, graded both ways.** **`BND-23` registered** (55%, base rate 51%: no fire at any leg).

**4. ✅ `BND-21` TRUE.** `DFII10` [9/1] 2.44, +0.0bp, margin 2.0bp; BE +4/+6/+2. `FL-BND-12` CONFIRMED on its second out-of-sample pass (opposite direction). Routed to MIDAS (zero real impulse ⇒ their positioning candidate carries gold). `KB-BND-223`.

**5. ✅ INBOX DRAINED 4 → 0.** RED (FT-11 v1.1) → **design call delivered, all on-menu: −4bp · FLOW-alternative · second precondition path ADOPTED** (`KB-BND-224`) · MIDAS → consumed, gold figure now cited as theirs (−2.95% 8/28→9/1) (`KB-BND-226`) · SAM → consumed; `dm_cross_section.py` summary line now carries the horizon warning (`KB-BND-225`) · PROME hyperscaler (12d old) → **SCHEDULED 9/11**, docket row is the carrier now (`KB-BND-227`).

**6. ✅ C-36:** ruled 9/1 (two-part, THESIS v1.2.0) — **nothing blocks it; PROME told so explicitly with the record pointers.** The 9/1 leg-1 decomposition + tonight's `BND-21` are out-of-sample corroboration.

**7. ✅ US-sovereign-CDS (re-dated 9/4 item): DECLINED TO BUILD** — exists (Markit/ICE), free-primary pullability SEARCH-NOT-FOUND, re-test 12/1. `KB-BND-228`.

**8. FR2004 as-of drift on `TRADE.md`/`DEALER_CAPACITY.md` fixed** (boot_recompute rc=1 → riders added). STATUS bottom-line 9/1 blocks archived verbatim to `domain/sources/2026-09-02_STATUS_archive_bottomline_9-1.md`; STATUS 26,160 B (80% of cap).

## NEXT SESSION (dated, future-verifiable)

0. 🔴 **9/3 — SOFR−IORB [9/1]** (not on FRED at 19:4x ET 9/2). +3bp [8/31] was month-end; if it does NOT normalise the FR2004 11-21Y re-build re-reads as FORCED (`KB-BND-218`, `DEALER_CAPACITY` rider).
1. 🔴 **9/8 · 9/9 · 9/10 — GRADE THE REFUNDING ON THE FROZEN BARS, DUAL-PRINT BOTH DEFINITIONS, record all three `BND-23` legs individually.** `grade_auction.py` prints the OLD test; the `I'` line comes from the frozen table. **An `I'` fire alone is NOT a kill until Will rules on `KB-BND-222`.** WQ-99: the ADD re-arm is the OLD test.
2. 🔴 **FROM 9/9 — route the F2 read to RED per op** (`RED-FT-11` v1.1 gated on it). Never batch.
3. 🟠 **Owed to PROME/Will after the refunding: the FR2004 weekly join** so option (b) in the record's §5 (`I'` + non-auction mechanism confirmation) can be base-rated. Only then can the kill-leg question be ruled on evidence.
4. 🟠 **9/3 — re-run `dm_cross_section.py` 9/1-inclusive** (UK the binding stale leg). Told SAM/HANS not to quote the 8/27 table for 9/1.
5. 🟠 **Patch `grade_auction.py` to print the `I'` line** before the old print retires (~9/10). Deliberate that it still prints OLD only through the dual-print window.
6. 🟠 **BY 9/11 — hand-verify the `docket_check` BLIND SPAN 9/11→9/22 against the Treasury QRA** (20Y ~9/16 · 10Y TIPS ~9/17 · month-end 2Y/5Y/7Y ~9/22-24 pattern-expected, NOT confirmed).
7. 🟡 **9/11 — PROME hyperscaler share** (approach fixed in `KB-BND-227`). **A second miss ⇒ DECLINE.**
8. 🟠 **OPEN MIRROR DIVERGENCE still flagged, not reconciled:** `VX-BND-05` = 4 and `VX-BND-16` = 4 in `VX.tsv` vs matrix 3 / 2. Components HOTTER than the matrix. Not touched this session.
9. 🟠 **9 ACTIVE KB rows past `Stale_By`** (082/097/100/103/104/107/118/131/132) — still un-adjudicated; plus `KB-BND-218` (stale 9/4). Read each, don't bulk-flip.
10. 🟠 **`MEMORY.md` is 31,839 B = 98% of the 32,550 B read budget** (grew ~2 KB this session) — rotate the oldest durable learnings to `archive/` NEXT session before it silently truncates at boot. 🟡 BTP-Bund 46d stale — refresh before 9/10 ECB. 🟡 ^MOVE not re-pulled 9/2. 🟡 LIQUID repo-to-IORB extension (BOND's call) still owed. 🟡 Duration-neutral cash construction to LIQUID (n=2) still owed. 🟡 DAEDALUS ⑰ residue (VX-16 fused cell, VX-10 re-base).

## OPEN THREADS / KNOWN GAPS

- ⚠️ **TLT-5d is a PRICE yardstick; the kill is a MECHANISM claim.** The base-rating used the draft's yardstick so it is like-for-like with the dealer-drop evidence Will ruled on; the mechanism yardstick (FR2004 join, SOFR−IORB) is owed, not substituted.
- ⚠️ **The corpus refresh script still carries the destroy-on-empty defect** (`AUCTION_HEALTH.md` §TOOLING DEFECT) — not run; the base-rating used corpus-to-8/13 + TA_WS overlay. The FRN fix depends on TA_WS `type=FRN` completeness (51 CUSIPs 2014→2026 at ~4/yr = right count).
- ⚠️ FRED direct (`fredgraph.csv`) timed out from this box at 19:4x ET; FORGE `fetch.fred_fetch` worked. Not an availability claim — `re-test: 2026-09-03`.
- ⚠️ UK 10Y basis with HANS still unpinned (BoE `IUDMNPY` vs TE).

## POSITION

**TLT puts HOLD, no add — UNCHANGED. $0.** Only live add-gate DFII10 ≥2.50, **6bp away [9/1]**. Composite 12/35, ninth unchanged. Downgrade counter 0. **OPEN predictions: 2 — `BND-22` (resolves on the 9/14 publication) · `BND-23` (resolves 9/10).** Harvest/roll/sizing are TERRY's.

## MAIL

**In: 0** (4 processed → `inbox/processed/`). **Out: 4 new** — RED (design call) · MIDAS (`BND-21`) · SAM (correction consumed + tool change) · PROME (completion). All copied to recipient inboxes (PROME's at repo root `PROME/inbox/`). WALTER lane: CLEAR.
