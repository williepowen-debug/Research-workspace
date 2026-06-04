# HENRY MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis, STATUS, or LESSONS and delete, never just accumulate.*

*Audience: next HENRY instance. For Will-facing session closeout see `LAST_COMPLETION.md`.*

---

## Feedback

- [2026-04-17] Always pull fresh EOD levels before closing the week — partial retracements during the session are the tell.
- [2026-04-17] File-system cleanup touching a system-wide convention → present options + recommendation, don't just execute.
- [2026-05-21] **Literal triad-count framing, not trajectory.** Invalidation criteria with literal thresholds ("HY OAS <260 sustained") must be counted literally ("not fired"), not by trajectory ("approaching"). Use "1 fired + 1 compressing + 1 flat." Keep "trap clinching vs soft kill" as the conceptual mental model.
- [2026-06-03] **Decompose ratios into numerator vs denominator before assigning weight.** CCC/HY "widened to 3.48x" was mostly the HY denominator compressing (286→272), not CCC blowing out (948→946 flat). State it as levels ("tail didn't follow index tighter"), not a ratio that overstates tail stress. Don't let a ratio carry weight its components don't earn.
- [2026-06-03] **Verify gate/catalyst dates against source — especially load-bearing ones.** Wrote "6/12 May CPI"; actual is 6/10 (BLS, and my own ECON_CALENDAR had it right). The whole duration gate keys off that date. Check BLS/source, don't trust recall.
- [2026-06-03] **"Confirm, don't assume" on cross-agent data points.** APO<$130 — verified live ($125.44) AND verified it's a BROCK *position* trigger not a thesis soft-kill (mildly helps APO puts). The check changed the conclusion. Always pull the sibling's actual threshold semantics, not just the headline.
- [2026-06-03] **Duration-gate discipline: don't push harder either way; wait for confirmation at better levels.** When near-term easing is real but structural thesis intact, "hold core + defer the add until the catalyst confirms" beats forcing a directional call. Will explicitly endorsed this restraint.

## Findings

- [2026-04-17] When oil shocks reverse on unilateral headlines, regional-bank beta (KRE, APO) gives back most of the AM rally by close — conviction bid is small vs beta bid.
- [2026-05-21] **Surface decisively fading a "loaded" catalyst is the most consequential vol-structure read.** NVDA 5/20 max-loaded; outcome SKEW dropped out of 140+, VIX9D crushed — "no catalyst expected." HENRY's job pivots catalyst-anticipation → drift-monitoring after such an event.
- [2026-05-21] **Breakeven decomposition = independent Fed-can't-cut confirmation channel.** Real yields rising + breakeven flat = term-premium/Fed-pinned, not reflation. Triangulates from the bond market vs the PCE print.
- [2026-06-03] **Split-axis decomposition when a "uniform" divergence meets contradicting new data.** 5/21 thesis was "tape calm / substance uniformly hot." By 6/3 substance split: cyclical (rates/energy/index credit) eased while structural (CCC tail + PC/BDC prints) held. Don't force the old binary — decompose by axis, name which axis each datum belongs to, and identify the resolving catalyst (here 6/10 CPI). Honest downgrade beats defending the framework.
- [2026-06-03] **Sibling-STATUS staleness cascade — check the sibling's Last-Updated before citing.** Multiple agents frozen at 5/21 (HENRY + BROCK) while tape moved. BROCK's "APO entrenched >$130" was a 5/21 snapshot; live APO $125.44. When pulling cross-agent data, read the sibling's timestamp and flag stale reads rather than propagating them as current. (Per saved memory: verify-state-before-propagating.)
- [2026-06-03] **Energy-driven yield easing ≠ Fed-pivot yield easing.** 10Y eased (−17bps vs 5/21 / −20bps from 5/19 peak) on Brent −$9-to-$15 (Hormuz unwind) disinflation relief, not "Fed about to cut." *(Quote deltas with their reference window — peak-referenced overstates the move-since-baseline; per Feedback above.)* Sticky core (PCE 3.2%, PPI 6.0%) unmoved. Decompose WHAT drove a rate move before reading it as thesis-relevant — the move can be real and directionally adverse to the position while leaving the structural thesis intact.

## References

- [2026-04-17] Live refresh: `source .venv/bin/activate && python3 FORGE/tools/market-data/fetch.py price ^GSPC ^VIX ^SKEW ^VIX3M ^VIX9D ^VVIX KRE WAL JPY=X ^TNX TLT APO`. Use `^GSPC`/`^VIX` (SPX/VIX bare fail). **.venv works on this surface** (Will's "no venv" note was a different container 6/3).
- [2026-05-21] Cross-source-tier: vol/SPX/NVDA = yfinance HENRY-primary. Macro/credit/bank-tier (HY OAS, CCC, Brent, USD/JPY) = pull from BROCK/REGINALD/VIOLET STATUS or dashboard (Prome dashboard lacks HENRY-tier vol metrics).
- [2026-06-03] **FRED convention (adopted):** FRED series publish T+1 — latest = yesterday's close. Date-stamp every FRED row `[FRED M/D]`; yfinance rows are intraday-live. Don't call a FRED number "live/today." Re-run `dashboard.py --compact` at boot. Full: `FORGE/tools/market-data/README.md`.
- [2026-06-03] Credit-tier current source: REGINALD STATUS (HY/CCC/IG date-stamped) + VIOLET STATUS (vol + credit + 10Y). Both refreshed ~6/1-6/2; faster than waiting on own FRED pull (and FRED was 503'ing per Will).
- [2026-06-03] **State-claim convention (pilot #1/#2, Will-approved) — MAINTAIN ON EVERY REFRESH.** In STATUS trigger/threshold tables: every Current value carries `[src M/D]` (yf-live or FRED date); trigger STATE is written `FIRED / NOT-FIRED / ARMED / WARN [as-of @ level]`, never a bare claim; STANDING rule (Yellow/Orange/Red) kept separate from STATE. Demonstrated in ACTIVE THRESHOLDS + INVALIDATION TRIAD. The point: a stale read self-flags (the disease was BROCK's "APO entrenched >$130 [5/21]" reading as live at APO $125). Fleet-wide adoption + the trigger-drift script (#3) deferred — Will skipped #3, kept conventions HENRY-piloted; PROME owns any fleet rollout.
- [2026-06-03] **"Forced update" on a stale fetch = expected rebase churn, NOT a force-push.** The fleet's `pull --rebase`-on-shared-branch protocol rewrites local-commit SHAs every rebase; a 2-day-stale observer's origin/master ref then can't fast-forward → git labels it "forced update" even with zero `--force`. Verify benign via: `git rev-parse --is-shallow-repository` (false = merge-base trustworthy), `git merge-base --is-ancestor <old> origin/master` (YES = content preserved), `git fsck --lost-found` (dangling = rebase-orphans w/ same-message twins on main line + stash internals "On master: temp/autostash" — both harmless). Only alarm if fsck shows unique unreachable work. Reflex prompted by Will 6/3.

---

## Session Notes

### CHANGES SINCE LAST SESSION (6/3 PM — same-day continuation)
- Markets closed; no market/thesis change. STATUS still accurate as of 6/3 14:00 (split-axis, hinges 6/10 CPI). This session was **internal house-keeping only** (Will redirected: no signals, no positions — "get HENRY's own house in order, match SAM/BRENT structure").

### LAST SESSION (2026-06-03 Wed ~22:00 ET → 6/4 — HENRY self-modernization, Will-directed)
- **Wrote `MODERNIZATION_PLAN.md`** — 3-phase plan to match SAM/BRENT tree: Phase A stale-refresh / Phase B thesis-layer **full-mirror** (THESIS+CHANGELOG+TIMELINE+PREDICTIONS_ARCHIVE — Will's locked choice) / Phase C docket+MAINTENANCE+CLAUDE-hardening. Diagnosis: live layer fresh, workbook frozen ~4/17; thesis lives inline in STATUS (1 gen behind SAM/BRENT).
- **KB prune arc launched** — `workbook/KB_AUDIT.md` is the multi-session source of truth (verified reference map). Independently reproduced Prome's map exactly (38 load-bearing/98 leaf); **corrected to 39 — added ML-HEN-032 (LABOR/KB-LAB-005 cross-link Prome's HENRY-only scan missed).** Ref corpus must include LABOR/KB.tsv.
- **Executed Pass 0 / 1 / 1.5:** KB **136→108 (−28, −21%)**, all to KB_ARCHIVE.tsv (nothing deleted), zero orphaned links. P0=12 status-flagged leaf; P1=14 Jan scaffolding/wrapper/resolved-PIT (kept 17 durable substrate; 021/025 reusable bits salvaged → REFERENCE_TABLES); P1.5=067/132 re-pointed (`[ARCH]` convention) then archived.
- **Concurrent-commit index race** hit on Pass-0 commit (SAM's parallel commit grabbed my staged files under its message, then pushed — content safe, mislabel permanent). Mitigation: atomic `&&`-chained stage-guard-commit; promoted to auto-memory `[[finding_concurrent_commit_index_race]]`.

### NEXT SESSION
**Track A — modernization (ACTIVE workstream; see MODERNIZATION_PLAN.md + KB_AUDIT.md):**
1. **KB prune Pass 2 (Feb, 27 rows)** → 3a/3b (Mar ~60, heaviest archive) → 4 (Apr, 13, lightest) → end-of-arc: 34→~9 **category consolidation** + **027/031 merge** + **stale-numbers refresh** on kept rows.
2. Then **Phase A remainder** (VX dup-ID fix, FLOW refresh-split, ECON_CALENDAR), **Phase B** (thesis/ full mirror + STATUS slim + boot edit = eval re-baseline flag), **Phase C** (docket/CATALYSTS + MAINTENANCE + CLAUDE hardening + FILES rewrite incl. "88+ entries"→actual).

**Track B — market (STANDING; unchanged):**
3. **🔴 6/10 May CPI = THE GATE (HEN-32)** — >0.3% core → cyclical re-arms, add TLT Sep $85P; ≤0.2% → soft-kill. 4. **🟠 6/5 NFP** (Will selling 3× Jun $85P into first hot print). 5. **🟠 USD/JPY >160 sustained.** 6. **🟡 6/16-17 FOMC.** 7. **🟢 BROCK STATUS stale (5/21)** flag.

### GAPS — PERSISTENT
- **0DTE SPX share + GEX regime** STILL PENDING (5+ sessions). Manual estimate acceptable.
- **VX.tsv duplicate ID collision** — VX-HEN-19.01-.06 used twice (Beige Book block + oil-shock block). = modernization Phase A2 (renumber oil-shock block → 21.xx); NOT done yet.
- **Stale 4/17 VIOLET outbox file** undelivered — messaging-overhaul will sweep.

### INFRASTRUCTURE NOTES
- 6/3: KB prune arc conventions — `KB_AUDIT.md` as multi-session source-of-truth; `[ARCH]` re-point tag for archived load-bearing IDs referenced by live VX/FLOW; reference corpus = KB+VX+FLOW+PRED+**LABOR/KB**. SAM precedent (167→122) is the template.
- 6/3: FRED citation convention + staleness-as-boot-hazard pilot (#1 date-stamp state-claims + #2 STANDING-vs-STATE triggers) live in STATUS. #3 trigger-drift script skipped per Will; fleet rollout → PROME.
