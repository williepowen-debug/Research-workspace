# BOND SCRATCH — 2026-09-28 (Mon) catch-up session 14:37 → 14:46 ET (Will: "boot up, catch up on owed work"). *Prior same day:* 10:34→13:15 ET live-event session (+ outbox audit to ~14:05). *Earlier:* 9/26 `prome-1d` · 9/25 · 9/24.

**Purpose:** ephemeral handoff. Read at boot, rewritten at closeout. Durable → `MEMORY.md`; evidence → `workbook/`. The previous SCRATCH text is in git history (`git show HEAD~1:AGENTS/BOND/SCRATCH.md`).

> ## ⚠️ STATE AT WRITING
> ⛔ **POSITION: TLT Sep-30 77P ×20 — HOLD to expiry, no add (WQ-280), `$0`.** Expiry Wed 9/30 (TERRY's rail).
> Composite **14/35** (unchanged) · Counter **0** · OPEN predictions **0** (live file = header only).
> Last FRED print (unchanged since the morning): HY 293 · CCC 1128 [9/25] · DFII10 2.85 [9/24] · DGS30 5.47 [9/24]; the official Treasury 30Y is 5.49 [9/25].

## WHAT I DID — 9/28 catch-up (14:37 → 14:46 ET)
1. **Boot:** fetch 0/0 (no pull needed; HAWK had uncommitted changes, left alone). docket_check rc0 (verified through 10/8). corrections rc0. WALTER inbox empty. boot_recompute rc0 (no drift). ⚠️ The step-5 CATALYSTS read was **SKIPPED until ~40 min in**; it was done late and disclosed in the READS packet.
2. **Blind span 10/9→10/19 hand-checked** against the Treasury Tentative Auction Schedule PDF (created 2026-08-04, covers through Dec): **no coupon auction in the span**. Columbus Day is **Mon 10/12**. Every October coupon auction is docketed (3Y 10/6, 10Y-R 10/7, 30Y-R 10/8, 20Y-R 10/21, 5Y TIPS 10/22, 2Y/5Y/FRN/7Y 10/26–29).
3. **8/27 kill-scope flag RESOLVED:** it reached PROME as **WQ-99**, RULED 9/1 (the OLD definition governs the ADD re-arm; recorded exception). The morning audit's "no PROME record" was a naming-keyed false absence. The audit was corrected and the packet `git mv`'d to `outbox/delivered/`. Residual: (b) the LIQUID routing trigger and (c) the grader dual-print have no explicit ruling; both run OLD, consistent with WQ-99. Not live.
4. **READS.tsv declaration** (DAEDALUS ask, due 9/30): 19 rows packeted (`1b78da2d8`); **PROME transcribed at `8c7bf0614`** (reads_check rc0). ⚠️ The packet header stamp "~15:1x" was typed ahead of the clock (committed before 14:42). PROME noted it. The packet is now in PROME's processed/ and is NOT edited there.
5. **Rotations (READ_CAP rule 5):** PREDICTIONS 27,320→120 B (BND-25..29 → `thesis/archive/PREDICTIONS_resolved_BND-25_to_BND-29.tsv`). CATALYSTS 26,539→22,176 B (4 fired rows → `docket/archive/CATALYSTS_fired_2026-09.tsv`). Rows were cmp-conserved in both. STATUS 25,265→~22,0xx B (snapshot `domain/sources/2026-09-28b_STATUS_full-snapshot_pre-rotation.md`, crc32 2552442073).
6. **`kb_lint` fix:** the PREDICTIONS header guard read `rows[0]`, so a header-only file (0 OPEN) FAILED as "wrong header". It now reads `fieldnames`. Tested: header-only rc0 · comment-first rc1 · 0-byte rc1 · real rows rc0. Selftest 14/14.
7. **HY primary access (L477 Q4 D8; subagent web sweep) → `KB-BND-346` (C3), `CREDIT_PRIMARY_MARKET.md` refreshed:**
   - OPEN for large credits: SoftBank $11.1B record HY 9/23–24, book >$30B at 8.6–9.75%. Paramount ~$12.4B HY launched 9/28, **UNPRICED**.
   - **Pulled-deal leg UNVERIFIABLE (LCD/Debtwire/IFR paywalled) — a gap, not a zero.**
   - Sep HY volume: "busiest month" (Bloomberg) vs "2nd-busiest" (junkbondinvestor). **CONFLICT unresolved.**
   - The Bloomberg CCC index (968) ≠ ICE CCC (1128). Don't mix them.
8. **`KB-BND-307` CORRECTED:** the cadence half (">=15-day lag, pairable early October") was wrong; the lag is ~8 days and the fire was graded 9/24.
9. **WQ-291 grader built + dry-run:** `analysis/2026-10-01_wq291_grade.py`. It reproduces PRE $47.986B and returns rc=3 GAP (as-of 9/23 unpublished). rc 0 = graded · 2 = fetch/PRE mismatch · 3 = GAP.
10. Stamp-drift memory extended (n+6, BOND again, same day).

## 🔴 NEXT SESSION (dated, future-verifiable)
1. 🔴 **Tue 9/29 AM: HY OAS 9/28 cell.** Over 300 with this velocity means matrix row 4's letter ⇒ 3 — **a BOND marker only; it does NOT reopen HYG sizing** (X1 CLOSED 8/28; reopens only via BROCK's 10/02 sitting → TERRY + Will; corrected 2026-09-28 15:22 ET). Same cell decides RED-FT-01 (RED's, day 3 of 3 on ≥280). Also check the official DGS30 9/28 vs 5.49 (a 4th high?).
2. 🟠 **Paramount HY pricing (~9/29–10/1):** final yield vs "low-9%" talk and final size vs ~$12.4B. Wider or downsized = the first access crack. It is the only free-source access test available.
3. 🔴 **Wed 9/30:** quarter-end · Aug PCE + GDP 3rd · SOFR−IORB (0bp [9/25]) · TLT 77P expiry (TERRY).
4. 🔴 **Thu 10/1 ~16:15: FR2004 as-of 9/23.**
   - Run `../../.venv/bin/python analysis/2026-10-01_wq291_grade.py`.
   - Report MET / NOT MET / GAP with margin by the 10/2 boot. The riders travel with the verdict; a MET is a rec via TERRY + Will.
   - The same print feeds the FORUM-7 FINAL D3a/D3b (HENRY `bc540e071`) and L477 Q4 below-IG inventory (D6).
   - Also: H.4.1 · F2 10Y–20Y op (carrier) · quarterly `I'` refresh + corpus re-run · `VX-19` definition · TIPS-`I'` question (DOCKET L410) · `DEALER_CAPACITY.md` body refresh (deferred to this print).
5. 🟠 **10/1 announcement → freeze bars** for 10/6 3Y / 10/7 10Y-R / 10/8 30Y-R. The 10/7–10/8 legs can fire row 1's ⇒5 letter. Refresh the `AUCTION_HEALTH.md` header then.
6. 🟠 **By 10/21:** register the 10/28 FOMC curve-shape prediction with a base rate (OPEN = 0).
7. 🟡 **WQ-317** (cross-market attribution): APPROVE rec is pending Will's word. **Do NOT start without it.** If ruled, the letter is in `PROME/WILL_QUEUE.md`; it's one bounded read inside the 10/1 refresh.
7b. 🟡 **CCC 2027–28 refinancing wall by industry — OFFERED to Will, PENDING his word (9/28 15:24 ET).** If he says go, PROME registers it as a bounded attempt: free published maturity-wall summaries only, stated stop, no inference past them. Energy-sector HY is on the paid-data list (unreachable) — withdrawn. PROME verified the HY-300 correction `4a0d79528` (KB-BND-348); nothing further owed to PROME today.
8. 🟡 Carried: `check_fr2004` bare "FR2004 m/d:" pattern gap · charter step-7 verb vs kb_lint practice (disclosed in READS): align the verb in BOND's own `CLAUDE.md` in a quiet session.

## OPEN THREADS / KNOWN GAPS
- LIQUID owns the Q4 grade on the 9/25+ cells (BOND sent facts only). Watch B 15-session ≥ +28 · IG ≥ +6 / BBB ≥ +7.
- ACM/KW TP not re-pulled since 9/24 (STATUS marks STALE). The FORUM-7 P2 KW grade is HENRY's.
- Replies owed TO BOND: ZHAO (custody/TIC).
- TRAPS (carried):
  - `csv.writer` re-quotes TSV fields; use raw split/join.
  - `python3 -c` fails in this shell wrapper; use a script file or heredoc.
  - `fetch.fred_fetch` default limit=5.
  - The ACM xls is the "ACM Daily" sheet.
  - Use the venv for `grade_auction`/`cdx_proxy`/`fr2004_fetch`/xlrd.
  - **Never type a clock — `date` in the same command.**

## POSITION
**TLT Sep-30 77P ×20 — HOLD to expiry, `$0`.** No add (WQ-280). Harvest/expiry = TERRY.

## MAIL
**In:** PROME doorbells ×2 (READS transcribed `8c7bf0614`; WQ-317 pending Will). **Out:** PROME READS packet (processed) + SendMessage.
