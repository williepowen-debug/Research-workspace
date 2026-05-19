# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-05-18 (closeout)

## What Just Happened

Five threads landed this session, all CC-Prome surface:

1. **TOSCANINI retired and salvaged.** AUTONOMY.md + COMPLETION_SPEC.md promoted to `PROME/`. HUNTING ranking dimensions distilled into `PROME/ORCHESTRAL_LAYER_DESIGN.md` as a "Ranking criteria for Section 6" subsection. Remaining 8 files + `reports/` archived to `PROME/archive/TOSCANINI_2026-03/`. The `PROME/TOSCANINI/` directory no longer exists.

2. **Fleet-scan prototype (Step 1 of orchestral design) — v1 + v2 landed.** First test of context-discipline-via-subagent pattern. v1 produced a useful but rough report; v2 incorporated six fixes (two-column staleness, dormant pre-filter, merged loops section, explicit HUNTING math, math discipline, as-of price labels). v2 is in `PROME/FLEET_SCAN.md` and is now the live working surface. Boot sequence retargeted to read it at step 4.

3. **LIQUID revival proxy (Step 4 of orchestral design) — first prototype.** Foreground general-purpose subagent (not teams mode) briefed as a revival proxy for LIQUID (32d self-commit stale). Produced `AGENTS/LIQUID/inbox/LIQUID_REVIVAL_PACKET_2026-05-18_prome-spawned.md` + `LIQUID_STATUS_DRAFT_..._prome-spawned.md`. Headline diagnostic: bear thesis is re-asserting through DURATION (10Y +30bps over 32d, TLT broke 🔴) not CREDIT (HY OAS only -5bps). April SOFR-IORB scare was mechanical tax-day TGA, not structural. Proxy returned 4 v2-pattern-improvement suggestions.

4. **Live dashboard pulled and synthesized.** Replaces stale STATUS prices. Key live tape: HY OAS **280bps** (+4 vs 5/17, 20bps from 260 kill), CCC 935, Brent **$109.30** (BRENT scanner's $102 intraday read was a swing not the close — HEARTBEAT was right), 10Y **4.59** (+12, 🔴), TLT **$83.56** (broke 🔴), APO **$134.07** (🔴→🟢 zone change), VIX **17.82**, BIZD **$12.52**. Score 10 CRITICAL.

5. **CLOSEOUT.md created + BOOT.md updated.** First standardized CC-Prome closeout procedure (4 chunks, scope tiers, file-ownership reference, skip rules). BOOT.md cleaned of TOSCANINI drift: doc-ownership table, boot sequence steps 4 & 8, retired Toscanini section, On-Demand list.

## Current Git State

- Branch `master`. After committing this closeout pass, working tree should be clean and synced to origin (one upstream commit was rebased over mid-session at `1cdd9443`).
- Salvage + v2 fleet-scan + LIQUID revival packet location work all committed at `5558d180` mid-session.
- This closeout pass is committed separately.

**Untracked deliberately left:** `AGENTS/LIQUID/inbox/LIQUID_REVIVAL_PACKET_2026-05-18_prome-spawned.md` and `LIQUID_STATUS_DRAFT_..._prome-spawned.md`. Per agent-file-isolation rule, Prome does NOT commit other agents' files. Real LIQUID integrates and commits these on its next boot.

## Next Planned Work (entry point for next session)

**Top priority candidates (Will to direct):**

1. **HENRY revival proxy** — Step 4 prototype #2 test. HENRY is 31d self-commit stale. NVDA earnings Tuesday 5/20 is HENRY-domain. Tests whether the pattern generalizes from plumbing (LIQUID) to market-structure (HENRY).

2. **BROCK revival proxy** — Step 4 prototype #2 alt. BROCK is 17d stale. APO sustained $130+ (zone change 🔴→🟢 today); FSK fresh-premium discussion blocked on BROCK refresh. Higher position-relevance than HENRY; lower catalyst urgency.

3. **Fold v3 fleet-scan feedback into `PROME/ORCHESTRAL_LAYER_DESIGN.md`** — 4 items deferred from v2 prototype: (a) directional semantics of kill levels; (b) include 5-7-point time series in pass-through; (c) sweep-file internal triage; (d) authorize/disauthorize closeout of prior open questions. ~15 min surgical edits.

4. **LIQUID integration check** — has real LIQUID booted and integrated the revival packet? If yes, archive the prome-spawned drafts. If no, hold.

5. **Will-decision items** (carried forward from FLEET_SCAN.md Section 7):
   - SAM Tranche 2 FXY decision — FXY at $57.80 today, **below** the previously-forfeited $58.00-58.25 band. Tranche 2 may have re-opened.
   - APO Jun/Dec puts hold/roll/cut — APO $134 sustained
   - FSK fresh-premium discussion — strong-bear-classified but needs live bid/ask + Will approval
   - WAL Q1 10-Q integration (REGINALD-owned)

## Current Working Model

- BDC/private-credit stress confirmed at vehicle/income/mark level (FSK Q1).
- Public-credit cascade still unconfirmed by spread (HY OAS 280, VIX 17.82).
- **Bear thesis transmission channel has migrated PLUMBING → DURATION.** 10Y broke 🔴, TLT broke 🔴, while HY OAS sits within 20bps of kill but stable. New watch: long-end yield regime, not SOFR-IORB.
- BRENT's intraday $102 sanctions-waiver-print was a swing, not a close. Energy thesis intact.
- WAL recovered $74→$76 (still below bear line); KRE $67.92 🟡; OZK rolled (Sept) per Will.

## Cautions for Next Session

- **No trades without Will approval.** No fresh broad cascade short while HY OAS <300 and VIX <20.
- **Don't spawn:** CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome.
- **LIQUID revival packet files are untracked-by-design** — real LIQUID owns commit. If you see them and think "should I commit these?" — no.
- **Named-spawn triggers teams mode** (auto-memory `feedback_named_spawn_teams_mode.md`). For one-shot synchronous subagent work, omit the name parameter.
- **OZK STATUS-data desync** persists — STATUS still shows pre-roll posture for May 15 contracts. Hygiene-tier, not urgent. OZK refreshes on next boot.
- **HEARTBEAT.md not updated with today's tape** — flagged but not edited (shared file; Will-approval gate). Numbers in this SCRATCH are from today's dashboard, not HEARTBEAT.
- **Step 4 revival-proxy pattern is one-prototype-old.** Pattern works but has 4 design improvements parked in this SCRATCH section 3 above.
