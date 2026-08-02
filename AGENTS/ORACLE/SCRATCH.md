# ORACLE — SCRATCH (canonical session handoff)

**Session arc:** 2026-08-02 (Sat, ~18:30Z) — **PROXY RUN: phone-session spawn (PROME-directed, Will in-session); real-ORACLE integrates at next boot.** Scope: PROME 7/31 audit packet applied in full (DEEPENING purge, threshold collapse, deal-majority retraction, mechanical fixes 4a-4e), Hormuz weekly re-pin (docket-due today — done), OPEC+ 8/2 meeting read (resolved same-day: +188k Sept), WALTER SIG-W-20260731-006 processed with the asked-for re-pull. Full Polymarket pull ran clean; **Kalshi script lane DOWN on this box** (broken `cryptography` import + no `~/.config/kalshi/` creds — the MEMORY "creds present" note is desktop-local) → Kalshi via manual unauthenticated curls, stamped `[manual-curl]` in the log. Movers/coverage sweeps NOT run (out of proxy scope).
**Last updated:** 2026-08-02 (proxy session end)

## ⚠️ PRIOR-SESSION FRAMING CORRECTIONS — now baked into all surfaces (do not re-derive from old text)
- **Fed:** "Sept-specific DEEPENING post-FOMC" is RETRACTED (KB-ORC-058) — 56.5% is the tail of a ~6-week climb; FOMC hold = 2-day pause. Aggregate 66.5% sits ON the >66% re-break line (+7pp on the 7/22→7/31 close-basis **9-day** window — label bases).
- **Oil v3 threshold:** ONE live set — **Aug WTI-$100 >45% sustained ≥3 reads (deepen) / <20% sustained (breakdown) / Iran-crude <2.0mbpd (real loss)**. The 7/31-AM ">30%/>40%" pair is dead on every surface (STATUS, NEXUS_BRIEF ×2, VX-ORC-04). Provenance: KB-ORC-059.
- **Iran bimodal:** ~~"deal-tail now majority, first time this month"~~ RETRACTED (audit item 3; defects: not a majority / deal already led 7/24 / top-LEG-vs-binary not like-for-like). Registered read: **narrowed toward the DEAL side** — 8/2: deal-top 33.5% (+4.5/1d) vs invade 20.5% (−5.0/1d).
- **Blind-spot stands, corroborated:** 30Y 5.28% new cycle high (WALTER SIG-006) while hike odds sat flat on the 8/2 re-pull = term-premium, not policy path. **Never "rates calm per ORACLE"** — BOND owns the axis.

## CHANGES SINCE (7/31 → 8/2, pull 18:33Z)
- **OPEC+ 8/2 RESOLVED: +188k bpd Sept** (core-8), completes 1.65mbpd voluntary-cut unwind, **Q4 increases paused**, next mtg Sept 6 (The National 8/2; July closes Brent +24%/WTI +21%). (KB-ORC-061.)
- **Benign wave, whole Iran/oil board:** Hormuz-normal-Dec31 **58.5%** (Δ1d +11.0, deep $6.7M) = disruption leg 41.5%, first sub-45 print; Aug WTI-$100 **22.0%** (Δ1d −15.5 — only 2pp above the <20% breakdown line); US-invade-Iran **20.5%** (Δ1d −5.0); v3 spread **+19.5pp** (both legs eased = benign direction); NEH **78.5%** (Δ1d +6.0). (KB-ORC-060.)
- **Fed board FLAT:** aggregate 66.5% (Δ1d −1.0); Sept-specific 56.5% (Δ1d −3.0, liq deepened $347.7K→**$887.4K**); by-Sept 57.5% ≥ Sept-specific ✓ (close-basis ordering restored); no-cuts 88.8%.
- **CLARITY Act fade STALLED:** 24.5% → **30.0%** (+5.5pp/2d, deep $3.7M) into Aug-10 — watch for the news behind it. → BROCK/RED.
- **Kalshi tells (manual-curl 18:36Z):** US-credit-downgrade last **11.0¢** (7/31: 6.0 — +5pp/2d, last-trade basis; credibility-axis adjacent); July U3 >4.2% **44%** (7/31: 56 — −12pp/2d into the 8/7 print); recession 7.0%, Iran-crude 86%, bankruptcy-750 83% all steady; Brent Jul settle-ref closed ~99% = YES.
- **Houthi-Israel Aug-31 pin retraced 31→10.0%** (Δ1d −20, thin — debut print was noise; single-print discipline held).

## WHAT I DID (proxy session)
1. **Inbox:** PROME audit packet → all items closed (see disposition table in `outbox/2026-08-02_to-PROME_audit-fixes-hormuz-repin-opec.md`) → `git mv` to `inbox/processed/`. WALTER SIG-W-20260731-006 → re-pull executed, disposition row logged, `git mv` to `inbox/WALTER/processed/`.
2. **Created `board_log.tsv`** (v0.2 header per WALTER BOARD_CONSUMPTION_SPEC §5 — ORACLE had none) + backfill row for SIG-003 + row for SIG-006.
3. **Audit fixes:** STATUS full rewrite (retractions annotated inline); NEXUS_BRIEF surgical (header/As-of/STATUS-commit pin `8b43f294`, threshold ×2, majority retraction, tripwires, catalysts); VX-ORC-04 + VX-ORC-08 rewritten (found a 5th DEEPENING instance in VX-08 beyond the packet's four); KB-ORC-056 basis-labeled; broken +49.4pp spread row annotated; 7/31 state report annotated in place (fixes 3+4d).
4. **Hormuz weekly re-pin (due today):** watchlist `week-of-july-27` → `week-of-august-3` (entry: modal 75-99 36.5%, ⚠$792 event vol); re-pull logged the new pin. **NEXT RE-PIN DUE 2026-08-09** (literal-date gate per fix 4e).
5. **Pulls:** `polymarket.py pull --log` ×2 (40 rows + 1 re-pin row); `disruption_supply_spread.py` (+19.5pp v3 row); Kalshi manual curls → 7 rows appended to `KALSHI_ODDS_LOG.tsv` `[manual-curl]`.
6. **KB +2** (KB-ORC-060 Hormuz-repin/8-2 board, KB-ORC-061 OPEC+). **Outbox +2** (HAWK/BRENT/FALCON retraction+repin+OPEC; PROME memo).

## NEXT SESSION (priority order — carried + updated)
1. **🔭 AUG COVERAGE-GAP RE-CHECK** (carried): Iran-mil-vs-Gulf-State Aug daily + Houthi-shipping Aug daily — both STILL not open 8/2 18:34Z. Re-search; pin the moment either opens (war-tempo axis re-arm).
2. **⚠️ HORMUZ WEEKLY RE-PIN DUE 2026-08-09** — pin `week-of-aug-10` when it opens. Literal-date gate; do not let it regress to "next Sunday."
3. **⚠️ BOJ replacement owed** — July decision market resolved; find/pin the next-BOJ-meeting market.
4. **🟡 v3 spread trend-watch:** live lines = **>45% sustained ≥3 reads / <20% sustained / Iran-crude <2.0mbpd**. 8/2 at 22.0% — closer to the BREAKDOWN line than the deepen line; a sustained sub-20 run = war-premium fully out (route HAWK/BRENT/FALCON as a benign regime note, not an alert).
5. **🟡 Fed re-arm watch** (unchanged rungs): Sept-specific >60% / <45%; aggregate sustained >66% break; a 2026 hike prints. Iran-crude resolves **8/12**; July U3 print **8/7** (Kalshi >4.2% collapsed to 44% — watch the print vs crowd); July CPI **8/12**.
6. **⚠️ CLARITY ACT — Aug-10 deadline, bounce underway** (+5.5pp/2d to 30.0%). >5pp 2-day move rule already met → BROCK/RED on routing; investigate the news driver.
7. **🟠 BOND response pending** (DFII10 re-arm check + now the credit-downgrade +5pp/2d tell). Blind-spot disclaimer stays on every Fed surface until BOND's regime label lands.
8. **🟡 Kalshi lane repair (machine-local):** on desktop, verify `~/.config/kalshi/` creds + `python3 -c "import cryptography"`; on this laptop the lane is DOWN — manual-curl fallback documented in STATUS maintenance flags.
9. **🔭 Coverage sweep due ~Aug 7** (weekly; last 7/31). Movers on "what's moving" ask.
10. Carried: BRENT/FALCON WTI-$100-by-YE ask (7/24, open); RED recession probability (since 6/13); Kalshi gap-fills re-check via `/events?status=open`.

## CARRY-FORWARD
- **Push state: 2 commits LOCAL, NOT pushed (per spawn brief — PROME/Will hold the push):** `8b43f294` (STATUS/workbook/watchlist/board_log/inbox moves) + the closing commit (NEXUS_BRIEF/SCRATCH/outbox ×2 + state-report annotations). Real-ORACLE: safe-push at next closeout sweeps them.
- **Watchlists:** Polymarket 36 active rows (Hormuz weekly re-pinned; BOJ replacement owed). Kalshi 12 rows unchanged on file; lane down this box.
- **Files this session:** STATUS.md (rewrite), NEXUS_BRIEF.md (surgical), SCRATCH.md (this), watchlist.tsv (Hormuz re-pin + date-gate note), board_log.tsv (NEW), workbook/{KB.tsv +2 rows & 056 note-amend, VX.tsv 04+08 rewrites, ODDS_LOG.tsv +41, KALSHI_ODDS_LOG.tsv +7 manual, DISRUPTION_SUPPLY_SPREAD.tsv +1 row & broken-row note}, outbox +2, outbox/2026-07-31_to-prome_oracle-state-report.md (annotated), inbox moves ×2.
- **Did NOT touch:** MAINTENANCE.md, MEMORY.md, TRADE.md, HISTORY.tsv, scripts/tools. No auto-memory written (no new transferable pattern — the session applied existing rules).

## OPEN HYPOTHESES
- **The benign wave is event-driven and synchronized** (OPEC+ landing + war-tempo fade + FOMC behind us) — same shape as the 7/17-7/24 crack-then-snap-back but in the opposite direction. If Hormuz-normal keeps printing >55 on deep liq and the weekly pins keep centering higher buckets, the disruption story is ending; the interesting residual is then WHY the Fed hike board is NOT easing with it (term-premium axis again — BOND's question).
- **Watch the <20% breakdown line, not the >45% deepen line.** At 22.0% the supply leg is 2pp from pricing the war premium OUT entirely — that would be a real (benign) regime statement worth routing, and nobody is positioned to notice it because all eyes were on the deepen side.
- **CLARITY bounce** (+5.5pp/2d, deep) into a hard Aug-10 deadline is the one move on the board that contradicts this week's registered narrative — clean falsifiable test within 8 days.
