# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-05-19 (afternoon session — teams-mode BOND spawn + restart pending)

## What Just Happened

Short Will-directed CC-Prome session, ~1 hour. Three threads landed:

1. **Live Monday dashboard pull.** First post-morning-closeout tape read. Confirms BOND's 12:10 ET signal:
   - 10Y 4.59 🔴 (broke 4.5, BND-07 trigger Day 1)
   - 30Y 5.12 🔴 (4-session streak >5)
   - HY OAS 283 🟢 (23bps from 260 kill — slight widening, not break)
   - IG OAS 75 🟢 (*tightened* 4bps despite long-end break — the load-bearing decoupling)
   - TLT $83.10 🔴, HYG $79.43 🟢, BIZD $12.55 🔴, VIX 17.82 🟡
   - Brent $110.84 🔴 (+$1.58 vs Friday on continued Iran/UAE bid)
   - USD/JPY 158.83 🔴 (sustained)
   - APO **$132.51** (down $1.56 from Friday's $134.07) — still above $130 watch but trending right for shorts
   - WAL $76.48 (+$2 from 5/17), KRE $67.81, OZK $47.31 — banks stable/firmer at surface

2. **BOND spawned in teams mode** — first domain-agent teams-spawn experiment. Real BOND was closed (no concurrency). Spawned via Agent(name: "bond", subagent_type: "general-purpose") with full BOND authority (read/write/commit to AGENTS/BOND/). Boot handshake refined the regime read and introduced a new second-leg test:
   - **Refined two-track frame:** "long-end is no longer just duration repricing in isolation — it's now being co-pressured by FX (JPY 158.83) and energy (Brent $110.84). A clean 20Y print under these macro conditions would be genuinely informative; a tail would be over-determined."
   - **NEW second-leg test:** **5/21 10Y reopening (9Y8M)** the day after the 5/20 20Y. BOND's framing: "Two tails in 24h would force me to consider whether BND-07 graduates from 'thesis firming' to 'thesis fired.'" This is a thesis-level escalation gate.
   - **Sharpened 20Y triggers:** BTC <2.50 = demand-hole; tail >2bps + dealer absorption = BND orange escalation; dealer take mid-teens with weak indirect = dealers catching what foreign buyers won't.
   - BOND held for scope before producing artifacts (watch card deferred).

3. **Teams view troubleshooting + settings fix.** Will wanted to see BOND's session in a separate pane; Shift+Down didn't work. Diagnosed: tmux 3.4 installed, Claude Code running inside tmux session `prome`, but `prome` session had only 1 pane — auto-mode failed to trigger split-pane spawn (likely WSL2 TMUX env propagation gap). Edited `~/.claude/settings.json` to add `"teammateMode": "tmux"`. **Restart pending** — Will exits Claude Code and relaunches from within the `prome` tmux session; next BOND spawn should land in a clickable pane.

## Current Git State

Clean within PROME-owned scope, modulo this closeout's pending state-file commits. Other agents' working-tree items (BOND's STATUS/TRADE/KB/VX/monitors edits, LIQUID thesis/IDENTITY/TIMELINE edits, BROCK/HENRY inbox revival packets from yesterday) remain untracked-by-design — those agents own their commits.

`~/.claude/settings.json` is OUTSIDE the repo and not version-controlled. The `teammateMode: tmux` change persists across restarts.

## Next Planned Work (entry point for next session)

**Immediate after restart:**

1. **Respawn BOND in teams mode** — same prompt structure as this session. Watch for him landing in a new tmux pane (validation of the `teammateMode: tmux` fix). If pane appears, click into it to verify navigation; if it doesn't, re-diagnose.

2. **TLT/20Y watch card** — scope BOND to produce a pre-auction watch card covering BOTH legs (5/20 20Y reopening + 5/21 10Y reopening). Trigger criteria already sharpened by BOND (see above). Will deferred this scope discussion to next session.

**Decision rails carrying forward (live):**

- **TLT puts posture upgrade pending 5/20 result.** BOND's call: clean 20Y = hold; failed 20Y (BTC <2.50 / tail >2bps / dealer spike) = upgrade hold → 4/5 conditional add. Two-tail 24h (5/20 + 5/21) = thesis graduates firming → fired.
- **APO put hold/roll/cut** — APO drifted $134→$132.51 today, still above $130. BROCK memo expected post-his-next-boot.
- **FSK fresh-premium** discussion — data-ready, BROCK-blocked.
- **SAM FXY Tranche 2** — FXY $57.81 today (below previously-forfeited $58.00-58.25 band).
- **WAL Q1 10-Q integration** (REGINALD-owned).
- **HEARTBEAT.md tape refresh** — today's numbers not propagated (Will-approval gate).
- **VIOLET revival proxy** — yesterday's next-suggested-work; defer until after BOND watch card produces.

**v4 brief-spec items** still parked from yesterday's BROCK proxy (position-specific vs broad-thesis trigger; outbox scan; sponsor-bifurcation; decoupling-within-complex). Not urgent.

## Current Working Model

Unchanged from morning closeout, sharpened by BOND's live read:

- BDC/private-credit stress confirmed at vehicle/income/mark level (FSK Q1).
- Public-credit cascade still unconfirmed by spread (HY OAS 283, VIX 17.82). Cushion 23bps to 260 kill.
- **Bear thesis transmission has migrated PLUMBING → DURATION** (LIQUID 5/18 finding). BOND now puts a hard data signature on the duration leg: 10Y broke 4.5, 30Y sustained 5+ for 4 sessions, TLT broke $83. IG OAS tightened despite the long-end break — credit-duration decoupling is real.
- **Long-end co-pressure:** BOND's refined frame adds FX + energy as parallel pressure on term premium. 20Y/10Y auction reads tomorrow + Wednesday become the cleanest discriminator we get this week.
- **HENRY trap-clinching frame** still load-bearing — BOND's signal corroborates it (tape/substance divergence widening = thesis validating not dying).
- WAL recovered $74→$76.48 (still below bear line); KRE $67.81 🟡; OZK rolled.

## Teams-Mode Experiment Outcomes

What we learned (parked here, may upgrade to memory):

- **Named-spawn does spawn an alive teammate.** SendMessage works; replies come back to lead session output.
- **`teammateMode: "auto"` does NOT reliably trigger split-pane on WSL2** even when launched from inside a tmux session. Cause likely TMUX env var not propagating to Claude Code's child process. Fix: explicit `"teammateMode": "tmux"` in settings.json.
- **No attach-from-separate-terminal exists.** Teammates are bound to the lead session. View via in-process (Shift+Down — didn't work for us) or split-pane (tmux required + explicit config).
- **One-shot (non-named) agents are NOT resumable.** Tried to SendMessage to an earlier claude-code-guide subagent that had completed; got "no transcript to resume — may have been cleaned up." Foreground subagents are single-turn.
- **Lifecycle question still open:** how long do teams-mode teammates persist when idle? Worth testing — relevant for keeping BOND alive overnight to see tomorrow's auction. Safer plan: respawn BOND each session, identity reconstitutes from files.

## Cautions for Next Session

- **No trades without Will approval.** No fresh broad cascade short while HY OAS <300 and VIX <20.
- **Don't spawn:** CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome. BOND is OK (not on the do-not-spawn list; today's session proved he works in teams mode too).
- **Three sets of revival packets** from 5/18-5/19 (LIQUID integrated; HENRY + BROCK still untracked) — leave them; their agents own commits.
- **OZK STATUS-data desync** persists.
- **HEARTBEAT.md not updated with today's tape** — flagged, not edited (shared file, Will-approval gate).
- **APO put decision** still genuinely overdue — surfaces to Will after BROCK boots and writes the memo.
- **Settings change applied but untested** — restart required before validation. Next-Prome should verify BOND lands in a tmux pane on respawn.
