# LIQUID — Catch-Up Punchlist
**Opened:** 2026-06-08 | **Full-domain audit:** 2026-06-12 (Tiers 2-4 audited — findings below) | **Purpose:** Running list of stale/needs-review items found while bringing LIQUID current after the 5/21→6/8 gap (~18d).
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

- [x] 🟦 **MEMORY.md.** Done — 6/8 entry added at that closeout; rotated again 6/12 (current session + NEXT SESSION rewritten).

---

## Tier 2 — Thesis layer (AUDITED 6/12 — work needed)
- [ ] ⬛ **thesis/THESIS.md (v2.0, 5/19) — §5 "Currently" block is BEHAVIORALLY WRONG.** Asserts "APO co-trigger fired since 5/12 Day 7+ = Trigger C precondition" — that streak broke late-May; the NEW fire (6/11, closes 6/9-6/11) has HY *widening* concurrent, so it is NOT a Trigger C precondition. A future session reading THESIS before STATUS could escalate wrongly. Also stale: §4 channel map (USD/JPY "159.18, 0.82 away" → now 5 sessions >160 SUSTAINED; Brent "$110.57 reigniting" → $87.95 collapsed, oil-CPI loop row direction FLIPPED; HY "compression run" → widening), §3 Leg B 5/19 marks, header status line. Fix: restamp live blocks, keep durable sections.
- [ ] 🟦 **thesis/TIMELINE.md (5/19)** — ~6 of 13 windows now past; resolved rows never retired to STATUS log (USD/JPY >160 → bear-resolved; 30Y >5% ≥5 sessions → bear-resolved/durable; 5/22 claims; May BDC Q1 window; 5/30 PCE pending-data). FOMC row says "June 18" — **wrong, decision is Wed 6/17.** Fix: retire resolved rows, roll forward through FOMC/TIC/opex + BCRED.
- [ ] 🟦 **thesis/CHANGELOG.md** — no POV pivot logged since 5/20. Owed: 6/8 (Brent reflation flip, energy/CCC bifurcation KB-LIQ-058, APO re-arm) and 6/12 (APO fired-but-NOT-Trigger-C, HY direction reversal). One combined entry is fine.

## Tier 3 — Workbook active (AUDITED 6/12 — work needed)
- [ ] ⬛ **workbook/PREDICTIONS.tsv — overdue/expiring predictions.** LIQ-02 (HY velocity +50bps/2wk, timeframe Mar 2026) OPEN and **3 months past timeframe** — resolve against FRED history (likely MISS, verify before marking). LIQ-03 (CLO AAA >160 SOFR+, H1 2026) **window closes 6/30** — needs a CLO AAA data check to resolve. Also: zero predictions added since 2/26 — prediction discipline lapsed for 3.5 months.
- [ ] ⬛ **workbook/BDC_MARK_CONVERGENCE_MONITOR.md — scaffold never populated and its window PASSED.** Baseline table empty; target was Q1 10-Qs (mid-May→early-Jun). BROCK's 6/8 read reports 3 public-BDC regular-div cuts (MFIC/OCSL/OBDC) — the monitor's 🟠 "any BDC cuts regular dividend" trigger has likely ALREADY FIRED unrecorded. Fix: populate from Q1 prints (data pull) OR formally slim to a BROCK-interface note + KB entry. Decision needed.
- [ ] 🟦 workbook/KILL_MEMO_HY_OAS_260.md — ladder levels still correct; false-kill guard fuller treatment still owed (carried from 6/8 STRATEGY pass). Action table references "ARES $95P Jun or similar" — verify against FORGE for current book when next fired. Header context block ("As of 5/18, 20bps cushion") fine as build-date stamp.
- [ ] 🟦 **workbook/VX.tsv + FLOW.tsv — registries masquerade as live.** VX rows carry Current_Value/Status stamped 4/7 (SOFR-IORB!) and 2/11; FLOW positions stamped Apr 8 ("Q-end Mar 31 passed"). Fix: restamp the ~6 load-bearing rows OR add a header line declaring point-in-time registry, values verified via STATUS.
- [x] workbook/AUCTION_FRAMEWORK.md — durable template, footer-stamped Mar 19 extraction. OK as-is.
- [x] workbook/TIC_FRAMEWORK.md — durable, ready for 6/18 TIC. OK as-is.
- [x] workbook/KB.tsv — 58 entries, current through KB-LIQ-058 (6/8). OK.

## Tier 4 — Reference / mail (AUDITED 6/12)
- [x] CREDIT_THRESHOLDS.md — properly flagged HISTORICAL with read-with-care preamble. OK as-is.
- [ ] 🟦 inbox/ — 2 pending now ~3 WEEKS old (HAWK OFAC toll-risk 5/22; PROME FRED-citation-convention 5/21). Needs an inbox-spawn authorization from Will.
- [ ] ⬜ outbox/ — `2026-05-20_to-BOND_...` undelivered 23 days (BOND never stood up; HERMES never swept). Decide: leave for HERMES or annotate-and-shelve. 6/8 NEXUS/PROME + 6/12 BROCK files also awaiting sweep (messaging overhaul in flight — flag, don't patch).
- [x] domain/sources/ — archive bedrock, spot-checked structure. OK.

## Tier 6 — Boot-doc drift since 6/8 refresh (NEW 6/12)
- [ ] ⬛ **CLAUDE.md KEY THRESHOLDS + IDENTITY Current Focus + STRATEGY escalation/hold rows + USER.md snapshots — all carry the superseded APO framing** ("re-crossed 6/8, Day 1 of 3" — the 6/8 close was actually $127.57; trigger has since FIRED on 6/9-6/11 closes, NOT Trigger C) **and HY "16bps cushion NARROWING"** (now 20bps, WIDENING). USER.md Key Dates still lists 6/10 CPI / 6/11 claims as forward. Mechanical restamp from corrected STATUS — same Phase 1-5 recipe as 6/8.
- [ ] ⬜ MEMORY.md at ~27KB — session blocks back to Apr 16; archive pre-May blocks to `archive/` if it keeps growing.
- [ ] ⬜ HEARTBEAT line 23/41 (shared file, PROME owns) — APO row stale 6/4 ($128.03 🟡; should be 🔴 FIRED) — flag to PROME, do not edit.

## Tier 5 — Known data gaps (need external pull, not just file edits)
- [ ] **Auction internals 5/21–5/28** (10Y reopen, 2Y, 5Y, 7Y) — BTC/indirect/tail not integrated. Needed to close CALENDAR Resolved + Dashboard 3. (TreasuryDirect auction-results query can fill this — no BBG needed.)
- [ ] **Live HY Energy OAS** — ICE/BBG-gated; route to BRENT/data-fetch (confirm 300 cross). (KB-LIQ-058)
- [ ] **5/28 April PCE, 6/5 May NFP** — outcomes not integrated. (FRED PCEPI/PAYEMS — easy pull.)
- [ ] ⬛ **SRF / reserves / RRP — LIQUID-OWNED Leg A metrics stale since 4/16 (~8 weeks).** "Leg A dormant" is partly assumption while reserves-toward-$2.8T-floor is unverified. WRESBAL/RRPONTSYD are weekly FRED series — easy pull; SRF needs NY Fed.

## Tier 5 — Known data gaps (need external pull, not just file edits)
- [ ] **Auction internals 5/21–5/28** (10Y reopen, 2Y, 5Y, 7Y) — BTC/indirect/tail not integrated. Needed to close CALENDAR Resolved + Dashboard 3.
- [ ] **Live HY Energy OAS** — ICE/BBG-gated; route to BRENT/data-fetch (confirm 300 cross). (KB-LIQ-058)
- [ ] **5/28 April PCE, 6/5 May NFP** — outcomes not integrated.
- [ ] **SRF / reserves** — stale since 4/16; next NY Fed refresh.
