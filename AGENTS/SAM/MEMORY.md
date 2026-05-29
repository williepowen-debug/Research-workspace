# SAM MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or auto-memory, never just accumulate.*

---

## Feedback
- [2026-03-31] Will values boot transparency — wants to know what SAM read, in what order, and whether the process is working well. Don't just orient silently; confirm orientation.
- [2026-03-31] Will thinks long-term about infrastructure. When proposing solutions, address scaling and durability, not just immediate need.
- [2026-04-01] Key dates were getting buried in STATUS.md. Will approved CALENDAR.md as standalone living doc — pure table format, forward-looking only, pruned weekly. Added to boot sequence as step 5.
- [2026-04-02] When explaining complex financial mechanics, Will needs the simplified version first. Start with the plain-English punchline, then layer in detail only if asked.
- [2026-04-02] Will uses Perplexity for deep research and shares outputs. Treat Perplexity data as high-quality but verify framework logic independently.
- [2026-04-11] **Script-defined alert thresholds MUST match THESIS scenario bucket definitions** — not invented independently.
- [2026-04-11] Will prefers intellectually honest corrections over doubling down. Lean toward restraint on thesis-level updates; one data point rarely justifies 15-25pp probability shifts.
- [2026-05-25] **Will wants gap-check before writebacks.** When SAM proposes writebacks, Will asks "any other searches?" — surfaces gaps the synthesis missed. Build in a "what's still missing?" beat before executing multi-file passes.
- [2026-05-28] **Will likes the flag-then-fetch stepwise method for big refreshes** — flag stale items first (review), THEN fetch newer data tier-by-tier. Keeps scope controlled and lets him gate each tier. Applied to the KB freshness pass; worked well.

## Findings
- [2026-05-28] **Shallow-clone "false fork" illusion in web sessions.** Claude-Code web containers clone SHALLOW (`.git/shallow` graft present). `git merge-base` / `rev-list --left-right` then falsely report NO common ancestor + huge divergence — saw "53 ahead / 50 behind, unrelated histories" when the branch was really just **3 ahead / 1 behind** master. Fix: at boot, `git rev-parse --is-shallow-repository`; if true, `git fetch --unshallow origin` before trusting ANY ahead/behind or merge-base. Don't panic at apparent forks in web sessions. Auto-memory promotion candidate.
- [2026-05-28] **Position cost-basis in state files was inaccurate — recorded "$57.48 blend" vs $58.32 actual (Will ground truth).** Recorded per-tranche fills (8 @ $57.36 + 5 @ $57.66) didn't even reconcile (avg can't exceed both components). Flipped live P/L +0.4% → **−1.1%**, R:R 1:1.86 → 1:1.13. **Never cite position cost-basis / P/L from STATUS-file figures as authoritative — confirm with Will (CLAUDE.md rule #3 + #4).** Auto-memory promotion candidate.
- [2026-05-12] **Read intraday extremes, not just closes — Apr 30 intervention misread.** May 3 STATUS logged Apr 30 yen move as "Tokyo session reprice" when it was MOF intervention (intraday range 5.15y). Add intraday-range alert when single-day range >2.5y. `usdjpy.py` touch tolerance band (May 6 low 155.05 failed strict ≤155).
- [2026-05-03] **Sub-agent fresh-context usability tests surface gaps invisible to the builder.** ~30s/test, high-yield. Re-applicable to any future SAM build/refactor.

*Calibration / process lessons now live in auto-memory: see [[finding_threshold_vs_mechanism]] (SAM-25/26), [[feedback_audit_behavioral_ranking]] (doc-cleanup ranking), [[feedback_doc_routing_data_drops]] (snapshot-vs-narrative routing), [[finding_followup_audit_pass]] (re-read after scoped ask).*

## References
- Primary data sources + scripts: see `CLAUDE.md` boot step 7 (canonical list).
- Vol/options: CME CVOL (JPVL), Barchart FXY OI, Investing.com risk reversals. FXY OI auto-captured by `fxy_options.py`.

## Session Notes

### ⚠️ DATE-STAMP NOTE (read first)
The prior session this evening (5/28 ~20:00 ET) committed with **UTC** timestamps that had rolled past midnight (00:17–00:39 UTC = 20:17–20:39 ET) and mislabeled its MEMORY notes "**5/29**." The operation runs on **Eastern** (CLAUDE.md) — it was still **5/28 Thursday**. All "5/29" stamps in those notes were wrong and have been corrected to 5/28. Confirmed with Will 5/28. Don't re-introduce 5/29 stamps for 5/28-evening work. *(CFTC weekly genuinely releases 5/29 — that 5/29 is correct.)*

### CHANGES SINCE LAST SESSION (5/28 eve workbook session → 5/28 PM boot)

- **🆕 Tokyo May CPI printed DOVISH (5/28):** core-core **1.6%** (−30bp vs Apr 1.9%; 7th straight monthly decline), breaches the 1.9% June-BOJ threshold. SAM-21 marked ~57% → **~50%**. v1.5 single-path now dovish-impaired. Processed this session — STATUS/TIMELINE/PREDICTIONS/CHANGELOG/CALENDAR all updated.
- Markets flat: USDJPY 159.27, FXY $57.65, Brent $92.37, JGB 30Y 3.896% (+4bp).
- CFTC unchanged -93,905 (May 19); weekly w/ May 22 data still due Fri 5/29.

### LAST SESSION (5/28 eve — workbook audit + KB freshness refresh + branch/PR resolution)

- **Workbook audit (Will-requested):** reviewed all 12 workbook tsvs — found clean. Fixed 3 minor items (commit `77d687e`): USDJPY 5/25↔5/26 row-order swap; FLOW-3.01 CLO ¥9.7T→¥9.2T clarity; **added KB-175** documenting that 40Y/Climate uniform-price (Dutch) auctions → blank avg-yield/tail is CORRECT-by-construction (verified at MOF), not a parse bug. 40Y demand read is BTC-only.
- **KB freshness — flag-then-fetch:** flagged 23 stale LIVE rows in 3 tiers.
  - **Tier 1 (`95ea3b7`, 14 rows):** FY2025 insurer actuals. Nippon ESR 222→195% (M&A, not stress) + bond loss -¥3.6T→-¥5.73T; Meiji -¥1.386T→-¥2.16T; Dai-ichi ~$20B est→~¥2T actual (ESR ~220%); Sumitomo ~$15B est→¥1.518T; Big-4 agg → ~¥11.4T/$67B; KB-137 SUPERSEDED. Industry hedge 44.4% still latest. Per-insurer hedge ratios flagged stale (NOT fabricated).
  - **Tier 3 (`b52f993`, 7 rows):** resolution checks. PC cascade Q2 = redemption PEAK; JICPA STILL PENDING; BOJ gauge core-core +2.7% Feb; repointed "May 1"→Jun 16, Brent $115→~$92.
- **Branch/PR resolution:** Diagnosed shallow-clone false-fork (see Finding) — real state 3 ahead/1 behind. Opened **PR #1** → merged (`2279198`).
- **THIS boot session (5/28 PM):** git pull clean; full boot.py sweep (8/9 green, CFTC re-ran standalone). Work done:
  1. **Processed Tokyo CPI dovish miss** → SAM-21 ~50%; wrote back STATUS/TIMELINE/PREDICTIONS/CHANGELOG/CALENDAR/CATALYSTS.
  2. **KB-169 updated** — Tokyo May continuation + durable ⚠️ rule (Tokyo CPI structurally below national via metro subsidies; don't read 1:1) + cross-link to KB-032 gauge.
  3. **Workbook review (Will-requested)** — audited today's 15 workbook commits; APPROVED. Numeric-conflict reconciliation (hedge 44.4% / JGB ¥13.2T) + STANDING-GAP tagging exemplary; VX→FXY-proxy migration clean; archive deletions safe (canonical research intact in research/outputs/).
  4. **STRATEGY.md fixes #1+#2** — (#1) SAM-21 ~57%→~50% + Tokyo-resolved across 5 places + "no national CPI before Jun 16" note; (#2) VOL SIGNALS section re-based to FXY-derived proxies (CVOL/RR feeds retired; old absolute thresholds flagged non-transferable; read directional pending recalibration).
  5. **Fed-cut secondary path operationalized (gap #3, Layer A)** — THESIS INDEPENDENT CATALYST section → real monitor w/ tripwire table + "FOMC Jun 17 = 24h after BOJ = backup catalyst" insight; RISK FACTORS "BOJ delays" row → "not pure downside"; CALENDAR Jun 10/Jun 17 tagged secondary-path; STATUS secondary-path live-read table added. Kept as independent-catalyst (NOT Channel 4). CHANGELOG addendum logged.
  Not yet committed at time of writing → committing now.

### NEXT SESSION

1. **🟠 FIRST: pull CFTC weekly (5/29 release, May 22 data)** — `cftc_jpy.py`. Watch for break of -102K cycle peak (currently -93,905, 3rd build week). Tokyo CPI already pulled 5/28 (done).
2. **Run boot.py** — refresh market table; verify National May CPI not early.
3. **🔴🔴 Tue Jun 16 BOJ MPM** — DOMINANT catalyst, now **~50% / dovish-impaired**. Pre-cable Jun 13-15; Jun 17 FOMC co-headline. RED CH-008 resolves here. National May CPI Jun 19 (post-BOJ) — watch if national core-core holds above Tokyo's 1.6% (Tokyo subsidy-bias).
4. **🟠 Jun FY2025 Norinchukin** — only near-term Channel 1 reactivation gate; watch CLO-book reduction language / CEO Kitabayashi.
5. **Tier 2 KB cleanup (deferred):** stale macro/flow rows — KB-131/132/133/134 (MOF flows), 050 (10Y), 116/117 (rate-diff/breakeven "~150"), 138 (JGB levels), 154 (real wages), 155 (consumer/prime), 136 (UST indirect bidder), 139/140/141 (Japan UST $1.1T→$1,239.3B + Mar/Apr TIC). Mostly mirror workbook tsvs → low-effort.
6. **JICPA finalization MONITOR** — pending past Mar 17 comment close; no final standard as of late May (KB-108/125). Check JICPA site.
7. **⏸️ DEFERRED — cross-agent signals (Will decision 5/28):** Layer B (BROCK/HANS PC-cascade pull for the Fed-cut secondary path) AND the HENRY stale-carry-numbers ping are **both shelved** pending other-agent development. Will is spending the next couple days bringing CARL/REGINALD/BROCK/HENRY up to SAM's structural level; signaling into agents that can't yet integrate is low-yield. **Do NOT re-flag these as open gaps** — they're captured (STATUS secondary-path row says "pull from BROCK/HANS"; carry numbers in STATUS). Re-activate once recipients are developed. SAM offered to write a "SAM structure → how to port" reference / help per-agent when Will gets there.
8. **Vol-proxy recalibration (infra TODO):** STRATEGY VOL SIGNALS now reads FXY ATM-IV / 25d-RR proxies directionally — absolute firing thresholds NOT yet recalibrated to proxy scale. Recalibrate against VOL_OPTIONS_FRAMEWORK.md when time allows. Also Fed-cut pricing (FedWatch) has no auto-pull — manual check Jun 9-16 (STATUS secondary-path row flags ⚪ TODO).
8. **🟠 Iran/Hormuz MOU** — binary; sign → Phase 2 accelerates; collapse → intervention #3 reactivates. **🟠 USDJPY 160 watch** (159.21 at last refresh).
9. **Eval re-baseline DUE** — CLAUDE.md docket-path + KOYOMI changes are standing trigger; evals carry stale $57.48. RED to self-correct $57.48→$58.32 on next boot.
10. **Position next-touch:** No add/trim under v1.5 single-path. Triggers: (a) USDJPY <156 for 3 sessions → consider add; (b) BOJ pre-cabling Jun 13-15; (c) thesis break (USDJPY >167 + BOJ dovish) = stop $55.05. Jun-18 $58C theta-watch.
11. **Tier-1 leftover:** per-insurer hedge ratios + Dai-ichi/Sumitomo FY2025 detail flagged stale — refresh if individual gaiyo PDFs accessible.
12. **Git:** PR #1 merged to master (`2279198`); MEMORY update is a follow-up PR. Verify origin/master sync at boot (re: shallow-clone Finding).

### NEXT INFRA SESSION (script build queue — unchanged)

When time allows for non-thesis work, in priority order:
1. **`trade_balance_japan.py`** — MOF monthly trade balance scrape (same pattern as `mof_flows.py`). June 18-19 May TB print is Phase 1 stability lag-test per CALENDAR. ~30 min.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 mutuals + Norinchukin + mid-tier. Scope first: does Quartr have all 7? Opens Quartr pattern for BOJ/Treasury/corp IR. ~45-60 min + auth.
3. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
4. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi for BOJ rate markets. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh (Big 3 now fully known post-v1.5); `research/` reorg (cosmetic); SIGNAL_INTAKE.md refresh (pending messaging overhaul).
