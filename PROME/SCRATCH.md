# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-18 18:00 ET (OpenClaw Prome — WALTER laptop/desktop Telegram setup closeout)

## What Just Happened

1. **WALTER/Prome/ORC resolved the mini-WALTER boundary.**
   - Live A/B test: Prome/mini-WALTER triaged the Moscow refinery post directionally well but created duplicate noncanonical artifacts and over-routed LIQUID; Full Claude Code WALTER produced the proper BOARD signal, recipient discipline, source calibration, and delivery logs.
   - Decision: **Full WALTER is the signal desk.** Prome/Quick-WALTER is not allowed to make fresh news-routing judgments.
   - Final pushed rule: Quick-WALTER may route only **pre-registered RED-FT / REG-T / safety-net trigger fires** where recipient_chain + precedence/action are already fixed. Delivery repair/backfill is allowed only for existing BOARD signals with already-named recipients and is not routing. Fresh screenshots/news/Visegrad/aggregator/source-confidence/recipient-selection all queue/escalate to Full WALTER.
   - UTC timestamp discipline added after the Moscow signal bug: never stamp ET wall-clock with `Z`.

2. **WALTER repo reconciliation completed and pushed.**
   - Pulled/merged WALTER’s GitHub group-chat dispatch commit with Prome consume-rollout commits.
   - Resolved `AGENTS/WALTER/STATUS.md` by preserving both truths: group-chat dispatch went live; Prome later advanced Phase 2 consume rollout.
   - Fixed Moscow MNPZ signal timestamp from ET-with-Z to true UTC (`07:55Z`) across BOARD/logs/handoffs.
   - Fixed RED delivery_log row to valid `COMMITTED`; `walter_doctor` now derives on-origin delivery cleanly.
   - Latest WALTER docs/specs pushed through v0.17/v0.5 boundary.

3. **HEARTBEAT / market gate refreshed.**
   - HY OAS printed **263 [FRED 6/17]**, only 3bp above the <260 R3/blended-credit kill line.
   - Claims were benign/yellow: **226k initial**, **1.810M continuing**.
   - 15:28 dashboard refresh: VIX/banks still faded stress; USD/JPY worsened to **161.78🔴**, FXY **$56.71🔴**; BIZD **$12.32🔴**.
   - Current read: broad cascade still not confirmed, but the kill line is uncomfortably close and carry is the clean red continuation.

4. **Group-chat research-agent idea surfaced.**
   - Good future design: WALTER owns routing; a separate VERIFY/CONTEXT helper can produce fact packets or surrounding-research packets; Prome owns decision/task consequences. No shared steering wheel.

5. **WALTER laptop/desktop Telegram setup standardized.**
   - Laptop WALTER MCP issue resolved: installed `unzip` + Bun, added Telegram bot token at `~/.claude/channels/telegram/.env`, paired Telegram, fixed WSL PATH/native Claude install to use Claude Code **2.1.181** / Opus **4.8**.
   - Desktop WALTER token path standardized to same `~/.claude/channels/telegram/.env` and confirmed Telegram connected.
   - Standard boot command for both machines: `tmux new -s walter -d 'cd ~/Research-workspace/AGENTS/WALTER && claude --channels plugin:telegram@claude-plugins-official'`; optional danger variant appends `--dangerously-skip-permissions`.
   - Rule remains: only one Telegram-WALTER active at a time, or Telegram pollers can compete for updates.

## Current Git State

Local branch has Prome refresh commits ahead of origin. Latest pushed state includes HEARTBEAT update and WALTER Quick-routing restriction; local state additionally includes Jun18 boot-doc refresh + this WALTER laptop/desktop setup note.

## Current Operating Picture

- **Mini/Quick-WALTER is effectively paused for fresh news.** It remains only as a registered-trigger executor / delivery-repair tool.
- **Full WALTER remains required for signal-desk judgment.** Prome should queue/page Full WALTER for novel signals.
- **WALTER delivery/consumption telemetry is healthy.** Doctor only flags known stale upstream feeds (`news-sweep`, `filing-watch`, `SIGNALS/inbound`).
- **Market state:** HY is near the <260 kill line; no broad cascade confirmation yet. Carry remains the cleanest live stress continuation (USD/JPY/FXY).

## Next Reboot Entry Point

Start fresh with:
1. Read `HEARTBEAT.md` first for the market state: HY 263, stress faded, carry worse.
2. If system lane: design the group-chat VERIFY/CONTEXT helper pattern — fact packet only, no routing authority.
3. If WALTER access lane: use the standardized tmux command + `~/.claude/channels/telegram/.env`; keep only one Telegram-WALTER active.
4. If market lane: monitor HY <260, TIC/FXY/carry, and whether banks/PC proxies re-weaken.
5. If positions lane: keep separate; broker/Will truth required before any expiry/trade action.

## Cautions

- Do not spawn Quick-WALTER for fresh screenshots/news. Queue/escalate to Full WALTER.
- Do not create parallel signal artifacts (`FORGE/signals/` or generic agent inbox files).
- Do not delete/archive legacy parallel artifacts yet; 30 `FORGE/signals/*.md` + 14 generic `AGENTS/*/inbox/signal_*.md` are historical and need a deliberate cleanup decision.
- No trade execution or expiry action without broker/Will truth.
