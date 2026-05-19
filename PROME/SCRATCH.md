# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-05-19 (intermediate closeout — design discussion appended)

## What Just Happened

Five threads landed this session:

1. **Live Monday dashboard pull.** Tape essentially unchanged vs Friday close: HY OAS 280 (16-20bps from kill), VIX 17.82, 10Y 4.59 🔴, TLT $83.56 🔴, USD/JPY 158.93 🔴, Brent $109.73 🔴, WAL $76.59 🟡, APO $134.07 (zone change 🔴→🟢 sustained well past 3-session reassessment trigger), BIZD $12.52 🔴.

2. **HENRY revival proxy (Step 4 prototype #2).** Second exercise of the revival-proxy pattern. Headline diagnostic: COMPLACENCY TRAP invalidation triad approaching firing while substance accelerates the wrong way → trap clinching, not dying. Apr 17 framing ("only SPX qualifies") is 3 weeks stale. Returned 5 v3-design improvements + introduced framing-precision overlay as a new artifact type.

3. **HENRY framing-precision note** (Will-authorized cross-agent inbox write). Codified the "trap clinching vs soft kill" concept while removing the proxy's overspecified "2 of 3 firing" literal claim (real count: 1 fired + 1 compressing + 1 flat). New artifact type now canonical: `<TARGET>_FRAMING_NOTE_<date>_prome-spawned.md`.

4. **v3 brief spec folded into `PROME/ORCHESTRAL_LAYER_DESIGN.md`.** Four LIQUID v2 items + five HENRY v3 items consolidated into 7-section spec (§1 tape pass-through w/ time series + zone-change column + cheap-pull permission; §2 thesis-kill w/ directional semantics + literal-vs-trajectory discipline; §3 cross-channel w/ sister-revival citation + peer-KB authorization; §4 catalyst-prep-or-overflow-register; §5 inbox triage; §6 closeout-authorization; §7 recommendations). Plus framing-precision overlay as new artifact type. Prototype-path status updated (Steps 1, 2, 4 marked complete with prototype headlines). 3 of 4 open questions resolved.

5. **BROCK revival proxy (Step 4 prototype #3) — first exercise of v3 brief spec.** Headline diagnostics: (a) APO position-trigger fired ~May 7, entrenched 13 sessions — decision overdue; (b) position-specific vs broad-thesis trigger conflation surfaced (HY OAS broad-thesis kill has NOT fired — cycle low 276, 16-20bps cushion); (c) WALTER NDFI scope-correction REQ open 5 days unread — 11× scope drift ($128B → $1.4T per FFIEC RC-C). FSK Q1 Strong Bear / near Max Bear (NAV -9.9%, non-accruals 8.1%, KKR $300M sponsor, JPM cut revolver -14%) — load-bearing data but BROCK domain memo unwritten. Returned 4 v4-design inputs.

## Current Git State

After this closeout commits, working tree clean and synced to origin in PROME-owned scope. Three sets of agent-inbox files remain untracked-by-design (LIQUID 5/18, HENRY 5/18, BROCK 5/19) — real agents commit on their next boots per agent-file-isolation rule. Don't commit them from Prome.

## Next Planned Work (entry point for next session)

**Top priority candidates (Will to direct):**

1. **VIOLET revival proxy** — pairs with HENRY for NVDA 5/20 read-through. VIOLET owns 20d-SKEW-slope sign-flip + R11 analog (VIX 17.76 → 52.33 in 8 trading days regime). Load-bearing for HENRY's vol-regime conviction on NVDA print. Now also exercises v3 brief spec on a vol agent.

2. **WAL Q1 10-Q integration** (REGINALD-owned, persistent — do not spawn). REGINALD STATUS flags 10-Q filed 5/11 but not integrated; Schedule O / Table 16 cross-credit inventory pending. Direct WAL Jun/Sep put sizing/exit input.

3. **MI3 / FFIEC PDD bulk-update status check** (REGINALD-owned). Window 5/14-16 passed; status check due. Pairs with #2.

4. **Inbox integration check** — has any of LIQUID / HENRY / BROCK booted and integrated their revival packets? If yes, archive the prome-spawned drafts and update STATUS to reflect freshness. If no, hold.

5. **Will-decision items** (carried forward — all live, all needing live tape + Will approval):
   - **APO Jun $100P / Dec $95P** hold/roll/cut — BROCK domain memo coming after BROCK revives. Per `feedback_exit_recommendations_need_mark_context.md`, need execution mark before close-now.
   - **FSK fresh-premium** discussion — strong-bear-classified, blocked on BROCK refresh which is now data-ready.
   - **ARES $95P Jun** — theta risk into Jun; small position.
   - **SAM FXY Tranche 2** — FXY $57.80 below previously-forfeited band; may have re-opened.
   - **HEARTBEAT.md tape refresh** — today's dashboard numbers not yet propagated (Will-approval gate; shared file).

6. **v4 brief-spec items returned from BROCK** (defer to next ORCHESTRAL update unless next revival surfaces same issues):
   - Position-specific vs broad-thesis trigger distinction → add to §2
   - Outbox scan (peer outboxes for outstanding REQs ≤14d) → add to read budget
   - Codify sponsor-bifurcation diagnostic + decoupling-within-complex flag as artifact types
   - HENRY framing-precision overlay = de facto v3.1 (already captured)

## Current Working Model

- BDC/private-credit stress confirmed at vehicle/income/mark level (FSK Q1 — Strong Bear / near Max Bear).
- Public-credit cascade still unconfirmed by spread (HY OAS 280, VIX 17.82). Cushion 16-20bps to 260 kill.
- **Bear thesis transmission channel has migrated PLUMBING → DURATION** (LIQUID finding). 10Y broke 🔴, TLT broke 🔴, while HY OAS sits within 20bps of kill but stable.
- **HENRY: trap clinching, not dying** — invalidation criteria approaching while substance accelerates wrong way (CPI 3.8%, PPI 6.0%, Brent +21%, FSK NAV -9.9%). Widening tape/substance divergence is the thesis being validated.
- **BROCK: APO position-trigger fired** (entrenched 13 sessions), but broad-thesis kill has NOT fired. Decision-relevant separation now explicit.
- WAL recovered $74→$76.59 (still below bear line); KRE $67.92 🟡; OZK rolled (Sept) per Will.

## Parked Architectural Discussion (post-closeout, pre-/clear)

Will is theory-crafting inside Teams/Agent View sessions to learn their limits before committing to architecture. Substantive design conversation happened this session — captured in `memory/2026-05-19.md` and `WILL/share/Whats goin on here in this pic.md` (Will's drop, ephemeral). Key parked items:

**The question:** how to reduce Will's manual relay overhead between agents without rebuilding architecture or pulling Will out of the loop. The fleet staleness problem is the operational symptom (LIQUID 32d, HENRY 31d, BROCK 17d this session).

**Where Prome landed:**
- File-based + inbox + PROVENANCE is the right substrate for cross-domain persistent-agent coordination. Teams/Agent View can't replace it (impedance mismatch — Teams instantiates fresh Claudes; your fleet has accumulated identity).
- Teams/Agent View DO fit intra-domain sub-agent coordination (memory-audit-001 pattern; adversarial-pair audits; parallel sub-agents with interplay).
- Mental model: **files for fleet, teams for swarm.**
- `tmux pipe-pane` = OK as forensic tool, not as primary read channel; `tmux send-keys` = hard no (blast radius + no auditability).
- The "messaging overhaul" Will parked 2026-04-14 is the right work to resume, with narrower scope: standardize message format (`_prome-spawned.md` + PROVENANCE), drop HERMES, add boot-time inbox-triage to each agent's `CLAUDE.md`.
- The second-order problem ("how does sender know what receiver cares about without reading all of receiver's domain") gets solved receiver-side: each agent publishes a thin `TRIGGERS.md` declaring tracked entities + thresholds + hot questions. Senders consult a one-page spec, not the recipient's full state. Generalization of WALTER's WATCH_FOR pattern from external signals to internal findings.
- **The staleness problem is cadence, not coordination.** Inbox finish reduces friction of relaying; it doesn't make agents self-driving. Cadence-automation (scheduled fleet-scan) was discussed and explicitly deferred — Will wants the system working with him in the loop first.

**Not committed:** propagation work (TRIGGERS.md schema, CLAUDE.md updates per agent, dropping HERMES). Will is thinking before signing off.

**`WILL/share/` folder:** new drop point for ad-hoc file/image shares to Prome (created this session). Will manages contents. The gitignore decision is open — files are currently untracked and Will hasn't said whether they should be local-only by default.

## Cautions for Next Session

- **No trades without Will approval.** No fresh broad cascade short while HY OAS <300 and VIX <20.
- **Don't spawn:** CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome.
- **Three sets of revival packets untracked-by-design** — LIQUID, HENRY, BROCK. Real agents own commit. If next-session Prome sees them and thinks "should I commit these?" — no.
- **HENRY framing note is a new artifact type** — Will-authorized this instance. Cross-agent inbox writes remain forbidden by default per `feedback_cross_agent_inbox_writes.md`; only with explicit per-instance authorization.
- **Named-spawn triggers teams mode** — for one-shot synchronous subagent work, omit the name parameter (per `feedback_named_spawn_teams_mode.md`).
- **OZK STATUS-data desync** persists — STATUS still shows pre-roll posture for May 15 contracts. Hygiene-tier. OZK refreshes on next own boot.
- **HEARTBEAT.md not updated with today's tape** — flagged; not edited (shared file, Will-approval gate). Numbers in this SCRATCH are from 2026-05-18 dashboard pull.
- **APO put decision is genuinely overdue** — surfaces to Will after BROCK boots and writes the memo. Do not pre-empt.
