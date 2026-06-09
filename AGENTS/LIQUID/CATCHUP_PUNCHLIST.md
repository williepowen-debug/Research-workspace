# LIQUID — Catch-Up Punchlist
**Opened:** 2026-06-08 | **Purpose:** Running list of stale/needs-review items found while bringing LIQUID current after the 5/21→6/8 gap (~18d).
**Ranking:** Behavioral impact first (does a stale value make LIQUID *act* differently?), not line-count. ⬛ = high, 🟦 = medium, ⬜ = low/cosmetic.

**Legend:** `[ ]` open · `[~]` partial · `[x]` done

---

## Tier 0 — Live state (DONE this session)
- [x] **STATUS.md** — refreshed to 6/8 live tape; 3 dashboards re-stamped; HY OAS split macro/energy; T-08 logged. (136 lines)
- [x] **STATUS.md live-primary correction (6/8)** — re-pulled load-bearing figures from yfinance (per new memory rule): **APO $129.93 (not dashboard $127.57) — at-the-$130-line, +1.85%, NOT resolved**; Brent $89.95 sub-$90 (not $93.43); USD/JPY 160.40 confirmed. APO read changed from "resolved" → "marginal, could re-arm."
- [x] **workbook/KB.tsv** — added KB-LIQ-058 (aggregate-HY-masks-bifurcation).

---

## Tier 1 — Boot docs (read every spawn — highest impact). AUDITED 6/8.

- [x] ⬛ **CLAUDE.md (LIQUID instructions) — KEY THRESHOLDS table.** DONE 6/8 (Phase 1, decision A = refresh in place). Refreshed all Current values to 6/8 live-primary; fixed misleading APO row (FIRED→at-the-line marginal) + USD/JPY (159→160.40 CROSSED); marked SRF/Reserves/20Y stale-stamped; added HY Energy OAS row (300 trip); added bifurcation caveat to HY-confirmation row; stamped self-flag "Last refresh 6/8 + live-primary not dashboard."

- [x] ⬛ **CALENDAR.md.** DONE 6/8 (Phase 2, decision B = roll-forward + pending markers). This Week → Jun 8-12 (CPI 6/10, claims 6/11, APO/JPY watch); Next Week → Jun 15-19 (FOMC 6/17, TIC 6/18, opex 6/19); Month-Ahead → Later June/July (BCRED Q2, Cliffwater CDLI, Q2 10-Qs — enriched from BROCK read). Past events (5/20 20Y w/ outcome, 5/21 10Y, 5/26-28 auctions, 5/28 PCE, 6/5 NFP) moved to Resolved; outcomes I lack tagged `⚠️ pending data pull` (→ Tier 5).

- [x] 🟦 **IDENTITY.md — Current Focus.** DONE 6/8 (Phase 3, mechanical restamp from corrected STATUS + live-primary re-verify). All 5 points restamped: #1 HY OAS 276/16bps + APO re-crossed $130 re-arming + bifurcation note; #2 30Y 5.01/10Y 4.55 + Brent framing FLIPPED (reignite→cooling); #3 folded in BROCK Stage 2→3 pivot + BIZD $12.56 bounce; #4 USD/JPY 160.30 trigger fired + TIC 6/18; #5 SOFR-IORB -2. Role + Key Thesis sections left untouched (durable).

- [x] 🟦 **STRATEGY.md.** DONE 6/8 (Phase 4). Trigger ladder kept. APO escalation line "currently firing Day 7+" → "re-crossed $130 on 6/8, Day 1 of 3 (re-arming)"; Hold-range restamped (HY 276, VIX ~18.8, SOFR-IORB -2, 10Y 4.55/TLT ~84.6/Brent ~91 + reflation-reversed note); position views restamped (HYG broken/close-or-expire, TEN ITM winner). **+ Added false-kill guard** to De-escalate (BROCK-aligned: tape-kill vs substance-kill) — fuller version deferred to KILL_MEMO Tier-3.

- [x] 🟦 **USER.md.** DONE 6/8 (Phase 5, mechanical mirror). Key Dates re-pointed to corrected CALENDAR (Jun 10 CPI / Jun 17 FOMC / Jun 18 TIC / Jun 19 opex / late-June BCRED; dropped stale (VERIFY) tags); positions table restamped (TEN ITM winner, HYG broken/close-or-expire); resolved list updated (5/20 20Y + 5/21-6/5 pending).

- [ ] 🟦 **MEMORY.md.** "CURRENT SESSION" = 5/20; "NEXT SESSION" block = the 5/21 gate plan (now superseded). Durable Findings section is fine.
  - Action: add 6/8 session entry; demote 5/20 to prior; rewrite NEXT SESSION block. (Normally done at closeout — flag so we don't double-handle.)

---

## Tier 2 — Thesis layer (PENDING AUDIT)
- [ ] thesis/THESIS.md (v2.0, 5/19) — re-read for any leg whose state flipped (Brent reversal, APO resolution, duration easing).
- [ ] thesis/TIMELINE.md — forward-only branch points May 19→Jun 18; the May windows are now past, needs roll-forward.
- [ ] thesis/CHANGELOG.md — add 6/8 POV pivot? (APO resolved, energy-HY bifurcation, Brent reversal).

## Tier 3 — Workbook active (PENDING AUDIT)
- [ ] workbook/KILL_MEMO_HY_OAS_260.md — still live (HY OAS 276, 16bps to kill); check trigger levels current.
- [ ] workbook/BDC_MARK_CONVERGENCE_MONITOR.md — Q1 BDC cycle should have WRAPPED by 6/8 (OBDC/ARCC/BXSL/MAIN); likely big stale gap.
- [ ] workbook/AUCTION_FRAMEWORK.md — 2Y/5Y/7Y cycle ran 5/26-28; framework durable, check.
- [ ] workbook/TIC_FRAMEWORK.md — next TIC 6/18; durable.
- [ ] workbook/PREDICTIONS.tsv — scan for due/overdue predictions (boot-time discipline).
- [ ] workbook/FLOW.tsv, VX.tsv — registries; cross-ref integrity only.

## Tier 4 — Reference / mail (PENDING AUDIT)
- [ ] CREDIT_THRESHOLDS.md (Feb 28 historical) — verify still flagged historical, not live.
- [ ] inbox/ — 2 pending (HAWK OFAC toll-risk 5/22; PROME FRED-citation-convention 5/21). Process as separate task.
- [ ] domain/sources/ — archive bedrock; spot-check only.

## Tier 5 — Known data gaps (need external pull, not just file edits)
- [ ] **Auction internals 5/21–5/28** (10Y reopen, 2Y, 5Y, 7Y) — BTC/indirect/tail not integrated. Needed to close CALENDAR Resolved + Dashboard 3.
- [ ] **Live HY Energy OAS** — ICE/BBG-gated; route to BRENT/data-fetch (confirm 300 cross). (KB-LIQ-058)
- [ ] **5/28 April PCE, 6/5 May NFP** — outcomes not integrated.
- [ ] **SRF / reserves** — stale since 4/16; next NY Fed refresh.
