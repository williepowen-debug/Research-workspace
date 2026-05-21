# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-05-21 (session spans 5/20 PM → 5/21 early)

## What Just Happened

Substantive multi-thread session built out BOND's domain infrastructure (he's the newest agent; peer agents have months of accumulated data BOND lacked) AND drafted a v2 escalation matrix to replace the v1 the data showed was anti-signal.

### Thread 1 — 5/20 20Y post-auction read (resolved)

BOND spawned in teams mode for the post-auction read. Verdict: 20Y did NOT trigger orange escalation. BTC 2.55, dealer 9.4%, indirect 67.7%, tail provisional clean-to-1bp. TLT puts: HOLD, no add. Reframe: NEW $16B 20Y issue (NOT reopen of 4/22 $13B); Apr 22's 2.68 BTC is not like-for-like.

Verify-research sub-agent confirmed tail was actually 0bp ("on the screws") per ZH. BOND respawned to update STATUS / AUCTION_HEALTH / outbox with confirmed-0bp + posterior shift on 5/21 base-rate (~20-25% → ~12% empirical) + structural "aggressive-add gate closed regardless of Leg 2." Commit `4eb21894` pushed.

### Thread 2 — BOND background build-out (4 sub-agents, parallel batches)

**Batch 1 (sequential, both done):**
- WI sourcing playbook → `AGENTS/BOND/research/WI_SOURCING_PLAYBOOK_prome-spawned.md`. Pre-1pm WI structurally unobtainable without terminal. InvestingLive is new primary post-auction WI source (5-15 min faster than ZH).
- Auction history dataset → `AGENTS/BOND/data/auction_history_prome-spawned.csv` (364 rows, 7 tenors, 2023→present) + refresh script + README. **Surprise finding: 5/13 30Y BTC 2.30 was 11th percentile of all 30Y prints since 2023** — the real statistical outlier of the May refunding, NOT the 20Y BOND focused on.

**Batch 2 (3 parallel):**
- Dataset v2 enrichment → added `tail_vs_cmt_bps` (FRED CMT proxy) + `indirect_pct_of_competitive` columns. CSV at `auction_history_v2_prome-spawned.csv` (NOT overwriting v1). Today's 20Y reconciles as MIDDLING (45th-pctile competitive indirect, 38th-pctile BTC) — neither strong nor weak.
- Cross-tenor base-rates → `analysis/CROSS_TENOR_BASE_RATES_prome-spawned.md`. **P(Leg2 weak | Leg1 strong) = 11.7% empirical**, vs BOND's "~20-25%" vibes estimate. BOND was anchored near unconditional baseline (22.6%).
- Escalation matrix backtest → `analysis/ESCALATION_MATRIX_BACKTEST_prome-spawned.md`. **Matrix is anti-signal at current thresholds.** Fires (N=26) had 19.2% hit rate vs base 35.7% — UNDER base by 16.5pp. Dealer >12% threshold wrong-signed (dealer >20% has +1.45% median 5d TLT = contrarian-bullish). Best single signal is indirect <50% of-offering (N=18, hit 50%, median -1.07%).

### Thread 3 — Inbox signal to BOND (Will-authorized cross-agent write)

`AGENTS/BOND/inbox/SIG-PROME-BOND-2026-05-20_dataset-30Y-reframe_prome-spawned.md` — consolidated addendum to brief BOND on next boot. Includes the 5/12 10Y indirect-7th-percentile reframe and the dual-convention methodology flag.

### Thread 4 — Matrix v2 surgery (teams-mode draft)

BOND respawned in teams mode for DRAFT-ONLY matrix surgery. Produced `AGENTS/BOND/proposals/MATRIX_V2_DRAFT_prome-spawned.md`. Iterative Will + Prome review through SendMessage. **5 open questions resolved through walkthrough:**

- **Q1** indirect threshold: **(c) pure per-tenor percentile**, indirect-of-offering <15th-pctile trailing-12mo. BOND pushed back against Prome's misframing of Option C (math error: 51.5% > 50% won't catch 5/12); steelmanned per-tenor percentile as the only rule that catches systematic blind spots. Quarterly snapshot table mechanism added to monitor footer.
- **Q2** dealer-as-TRIM: parked as future research thread; revisit ~3 weeks post-deploy.
- **Q3** TLT puts budget: **(c) middle path** — keep 2-contract budget; 3-of-3 fires generate Will-touch ad-hoc prompt, no pre-authorized aggressive tier.
- **Q4** deployment timing: **DEFERRED with conditional rule** — resolves mechanically on today's 1pm ET 10Y print. (i) v2 fires → deploy this week. (ii) v1 fires but v2 doesn't → deploy this week. (iii) neither fires → deploy next week Tue-Thu. Option "wait until June 10-12" rejected.
- **Q5** v2-native backtest re-run: OPEN, pairs with Q4 branch resolution.

Proposal file revised across §1/§2/§3d/§4/§5/§6/§7/§8/§9. §6 re-grade under (c) verifies: 5/12 10Y FIRES (51.5% vs 52.0% threshold = 0.5pp margin, maps to marginal half-add tier), 5/13 30Y FIRES via B'+T', 5/20 20Y does NOT fire. §9 Phase 0 now requires today's 10Y read produces dual-grade format (v1 + v2 simultaneously).

## Current Git State

Clean within PROME/. BOND artifacts untracked-by-design (5 new files + 1 dir-creation in `AGENTS/BOND/`):
- `AGENTS/BOND/analysis/` — 2 files (cross-tenor base-rates, escalation matrix backtest)
- `AGENTS/BOND/data/` — 4 files (v1 CSV, v2 CSV, refresh script, README)
- `AGENTS/BOND/inbox/SIG-PROME-BOND-2026-05-20_dataset-30Y-reframe_prome-spawned.md`
- `AGENTS/BOND/proposals/MATRIX_V2_DRAFT_prome-spawned.md`
- `AGENTS/BOND/research/WI_SOURCING_PLAYBOOK_prome-spawned.md`

LIQUID's prior uncommitted work has been integrated and committed (`4a1c7fe2`, `5f92933a`, `06f28e2d`, `71d6a9f3`) — no longer a tree-cleanliness concern.

`WILL/share/` remains untracked (Will's own files).

## Next Planned Work (entry point for next CC-Prome session)

**Pre-1 PM ET today (5/21):** respawn BOND for 12:30 PM pre-auction tape pull. Brief carries forward from `PROME/SCRATCH.md` §Thread 4 — emphasis on the dual-grade format requirement in §9 Phase 0 of the proposal.

**Post-1 PM ET today:** respawn BOND for post-auction verdict using mandatory dual-grade format:
- v1 read: BTC <2.30, dealer >12%, indirect <55% (of-offering) → 2-of-3 fire?
- v2 read: BTC <2.30, indirect-of-offering <52% (10Y snapshot threshold), tail ≥75th-pctile-of-12mo-10Y → I' alone OR 2-of-3?
- Report which framework fires (v1 only / v2 only / both / neither) → mechanically resolves Q4

**Q4 branch resolution → triggers v2 deployment timing decision:**
- v2 fires → deploy this week, pair with Q5 v2-native backtest re-run
- v1 only fires → deploy this week, same Q5 pairing
- Neither fires → deploy next week Tue-Thu, more time for Q5

**Q5 decision:** v2-native backtest re-run before deployment? Will + Prome decide once Q4 branch resolves.

**Live deployment (Phases 1-6 of §9 in proposal):** monitor matrix surgery + STATUS posture update + TRADE.md confidence-stepped add + KB entries + cross-agent outbox + 6-month re-grade backlog.

**Live Will-decision carries** (unchanged from prior session):
- APO put hold/roll/cut (BROCK memo expected post-his-next-boot; APO $131.87 at last dashboard)
- FSK fresh-premium discussion (BROCK-blocked)
- SAM FXY Tranche 2 (FXY $57.80 below forfeit band)
- WAL Q1 10-Q integration (REGINALD-owned)
- HEARTBEAT.md tape refresh (~3 days stale; Will-approval gate)

## Cautions for Next Session

- **BOND artifacts untracked-by-design.** BOND owns commit on his next live boot. Do NOT git-add or stage them as Prome — they belong to BOND.
- **Q4 resolves mechanically off today's auction.** Do not pre-empt; wait for BOND's dual-grade verdict.
- **5/12 10Y fire under v2 is TIGHT** (51.5% vs 52.0% = 0.5pp margin). Future near-boundary prints need explicit margin annotation in BOND's reads. Documented in §7 caveat of the proposal.
- **HEARTBEAT.md still stale** (no tape refresh since 5/16). Will-approval gate.
- **OZK STATUS still pre-roll posture** (hygiene, not execution risk).
- **Do not spawn:** CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome. BOND OK in teams mode.
- **Three agentIds from this session may still be resumable** if needed for follow-on Q5 work: BOND's matrix-surgery handle `a91cfacd0926fc1e6` (proposal author), 5/20 post-auction handle `a23ef79d62048d07d`. Lifecycle unknown; safer to respawn fresh next session per yesterday's pattern.

## Live Carry: Posterior Shifts Tracked This Session

| Item | Pre-session view | Post-session view |
|---|---|---|
| 5/20 20Y read | "Soft but functional" → "Strong demand at price" | **Middling** (45th-pctile competitive indirect, 38th-pctile BTC, 0bp tail) |
| Real May-refunding outlier | The 20Y (BOND focus) | **The 5/13 30Y** (11th-pctile BTC, 75th-pctile tail proxy) |
| 5/21 weak-Leg-2 base-rate | ~20-25% (vibes) | **~12%** (empirical, N=103 same-week coupon pairs) |
| BOND's escalation matrix | Trusted framework | **Anti-signal at current thresholds.** v2 proposal in draft. |
| TLT puts posture | Hold; conditional on orange via v1 | Hold; conditional on v2 fire (per Q4 conditional rule) |
