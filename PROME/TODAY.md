# TODAY.md — Monday June 29, 2026
**Updated:** 2026-06-29 (Mon, DESKTOP) closeout — built the **RESEARCH-INTAKE collection lane** (6 feeds live) + graded the carried 6PM oil reopen = **HOLDS / no action**. No trade executed (standing rule held).

**Objective:** today was infrastructure — stood up an always-on data-collection lane (GitHub Actions in a separate repo, agents read-only, not a VPS). The carried market event (6PM oil) resolved cleanly: decoupling held.

---

## ✅ Today's resolved event — 6PM CME oil reopen = HOLDS / no action
Brent **$73.30** (Mon), below the $74 line through the whole Sun-reopen → Mon-London sustain window *despite* the 6/27-28 US↔Iran strike exchange. Decoupling survived its hardest kinetic test; no trigger fired. Tail downgraded to **fragile-watch** (commercial P&I still not resumed). BRENT owns the thesis-integrity follow-up (durable normalization vs head-fake). Detail: `AGENTS/BRENT/PREREG_20260628_CME_reopen.md`.

## ★ New infra — RESEARCH-INTAKE (built today)
Always-on data lane, separate private repo `williepowen-debug/RESEARCH-INTAKE` (clone `/home/willi/Research-Intake`). **6 feeds weekday-daily:** EIA petroleum · EDGAR 8-K · Treasury auctions · CFTC COT (VIX) · FRED (15 series) · news-sweep. liveness silent-death guard + cross-run news dedup + `SUMMARY.md` digest + per-feed retry. **#1 next: wire the consumer side (an agent reads the lane).** See SCRATCH ★ + [[project_research_intake_collection_lane]].

## Regime (one-line) — refresh before citing levels
Energy tail **fragile-watch** (decoupling held at Brent ~$73 through the strikes; PATH-A reopening ahead of model — Hormuz ~75% prewar). Credit-bear **ARMED, pre-trigger** — HY vs >280 auto-watched by `liquid-hy-watch`. **Refresh dashboard/FRED before any market claim.**

## Standing rule (Will 6/26)
Deploy fresh capital ONLY on a fired (sustained) trigger; $500/card max-loss. ([[feedback_deploy_on_trigger_not_calendar]])

## Watch next 24-72h
1. **RESEARCH-INTAKE consumer wiring** (#1 PROME lane). 2. HY vs 280 (auto-watched). 3. 10Y auction + JOLTS 6/30. 4. EIA 7/1 · NFP + CFTC COT 7/3. 5. OZK/WAL/CFG Jul-16 · CPI 7/14.

## Fresh-boot checklist
1. Verify git sync — RESEARCH-INTAKE Action is a co-writer to its *own* repo; working repo pushes via `safe-push.sh`. 2. Refresh dashboard/FRED before citing levels. 3. SCRATCH = entry point (consumer wiring #1). 4. No agents warm — spawn fresh.
