# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-05-21 ~11:30 ET (CC-Prome boot + BROCK/REGINALD post-closeout refresh; pre-BOND-auction)

## What Just Happened

CC-Prome booted from cleared context at 10:54 ET. While Prome was booting, BROCK and REGINALD ran live closeouts in parallel and pushed; the BOND matrix-surgery + build-out chain from last night still leads into today's 1 PM ET 10Y reopening auction.

### Thread A — BROCK live closeout (5 commits f47b9a30 → 1310ed42)

20-day BROCK dark window (5/1 → 5/21) closed today. Per-position decisions formalized against Fidelity PDF marks:

| Position | Mark | Call |
|---|---|---|
| APO Dec $95P ×1 | $275 | **HOLD** — thesis vehicle, 210d runway |
| APO Jun $100P ×1 | $20 | LET EXPIRE |
| ARES Jun $95P ×1 | $25 | LET EXPIRE |
| OWL Jun 5 $9.5P ×2 | $40 | **HOLD** — 15d, 5% OTM, real ITM probability ~10-20% |
| HYG Jun $75P ×8 | $40 | LET EXPIRE |

Net BROCK book ~$400 on $3,120 cost. Dec $95P is the only position carrying real optionality.

**FSK Q1 classification: Strong Bear** (data Max Bear; KKR $450M+ defensive package pulls back one tier). One-line read: *"cleanest evidence, worst vehicle"* — KKR tender at $11 = hard floor, sponsor structurally long defense. **No fresh FSK premium.** Fresh PC premium would go to BIZD or ARCC Q2, not FSK direct. **No fresh BIZD/ARCC yet** either — HY OAS 286 widening *away* from 260 (cushion 26bps). Entry triggers: HY OAS <270 sustained 2+, OR GCRED/OTF release within 30d, OR bank PC loss disclosure, OR sub-90¢ arms-length BDC loan transaction.

**WALTER NDFI REQ-BROCK-20260514 closed** — scope correction $128B → $1.4T. New framework: `AGENTS/BROCK/domain/sources/NDFI_FRAMEWORK_MAY21.md` with 4-sponsor bifurcation table (KKR doubles-down / Apollo cashes-out / Blackstone backstops / Blue Owl holds-and-pays).

**Convergence re-scored ~46/60** (was 38/50) with 2 new vectors: sponsor-bifurcation diagnostic + duration-channel NAV pressure (LIQUID 5/18 reframe). Trap-clinching framing canonized — tape loosening (HY OAS +6 from cycle min, BDC equities bounced, VIX 17.5) while substance worsens (CCC +26, 10Y +42, FSK Max Bear).

**LESSONS #16 is a flag to Prome:** *Execution rails matter as much as decisions.* HYG Jun→Dec roll planned May 1, never executed during BROCK dark window because no mechanism existed. Same gap as May 15 cluster pre-registered ladder. Worth a PROME design note.

### Thread B — REGINALD live closeout (`f91ee9fb`, 14 files, +775/-341)

WAL V2.1 → **V2.2 shipped.** 10-Q drill (`research/WAL_10Q_DRILL_2026-05-21.md`) propagated through THESIS + SCENARIOS + CHANGELOG ×2 + PREDICTIONS.

- **B1 FIRED** — $99M life-science office sponsor walk-away (10-Q subsequent event, previously *pass* grade). Same strategic-default mechanic as IQHQ on OZK. At 60% LGD alone pushes Q2 NCO past 40bps.
- **V4 NEW** — CBO Stephen Curley resigned same week. Market -10% on combined news; DA Davidson PT $93→$90.
- **V2 inventory test CLEAN** — no new Leucadia-era credits; WAL escalated to active NY Sup Ct litigation against Jefferies parent.
- Other CRE-NOO nonaccrual **+15.4% QoQ** — leading bucket firing pre-event.
- NDFI 10-Q breakout $14.93B / 25.2% of HFI; V3 cohort-median conclusion confirmed.

**Scenario reweight:** Bear-fast 12% / **Bear-medium 30%** / Base 33% / Bull 18% / Tail 7%. EV $70.50 → **$67.98**, PT range $50-68. **REG-24 60→70%, REG-25 55→75%**. Frame matters: bear case got *more confident* but *slower* — Bear-medium dominates Bear-fast 30/12.

**V1 MI3 primary falsifier STILL HASN'T RUN** — FFIEC PDD 5/14-16 window passed without integration. V2.1's MI3 calibration table remains the trigger for V1-fast vs V1-slow.

May 15 expiry cluster cleared (WAL $75P + SSB $95P both gone per Will 5/21). STATUS 309→182 lines (Apr sections archived). POSITIONS WAL 8→7 positions / 3 expiries.

**Next critical test: Q2 print late July** — "one Office migration or many?" Jun 18 puts won't catch the Q2 catalyst directly (expire before print).

### Thread C — BOND auction still leads today

Plan from yesterday unchanged:
- **~12:30 PM** respawn BOND for pre-auction tape pull
- **~2 PM** respawn BOND for post-1pm verdict in **mandatory dual-grade format** (v1 read + v2 read simultaneously)
- Dual-grade output mechanically resolves **Q4** (v2 matrix deployment timing)
- Then **Q5** (v2-native backtest re-run pre-deploy?) resolves with Q4 branch

5 BOND artifacts from last night sit untracked-by-design in `AGENTS/BOND/{analysis,data,research,proposals,inbox}/`. BOND owns commits on next live boot.

## Current Git State

Clean. Tree shows only `WILL/share/` untracked (Will's files). Local at `f91ee9fb`, in sync with origin. BROCK + REGINALD both pushed cleanly.

## Resolved This Morning (off Pending Work)

- APO / ARES June premium review → BROCK closed (Dec hold, Jun let-expire)
- BDC/private-credit decision prompt → BROCK closed (no fresh premium, triggers documented)
- FSK fresh-premium discussion → BROCK closed (no, KKR structurally long defense)
- WAL Q1 10-Q integration → REGINALD closed (V2.2 shipped)

## Next Planned Work

**~12:30 PM ET today:** respawn BOND for pre-auction tape pull. Brief carries from yesterday's matrix-v2 draft — emphasis on dual-grade format requirement in proposal §9 Phase 0.

**~2 PM ET today:** respawn BOND for post-auction verdict. Mandatory dual-grade:
- v1 read: BTC <2.30, dealer >12%, indirect <55% of-offering → 2-of-3 fire?
- v2 read: BTC <2.30, indirect-of-offering <52% (10Y snapshot threshold), tail ≥75th-pctile-of-12mo-10Y → I' alone OR 2-of-3?
- Report which framework fires → mechanically resolves Q4

**Q4 branch resolution → v2 deployment timing decision:**
- v2 fires → deploy this week, pair with Q5
- v1 only fires → deploy this week, same Q5 pairing
- Neither fires → deploy next week Tue-Thu

**Q5:** v2-native backtest re-run before deployment? Will + Prome decide once Q4 branch resolves.

**Live Will-decision carries (remaining after this morning's closeouts):**
- **SAM FXY Tranche 2** — FXY $57.80 below forfeit band; Will-direction required
- **HEARTBEAT.md tape refresh** — ~3-4 days stale; Will-approval gate; today's tape + V2.2 scenario weights + trap-clinching framing should fold in post-auction
- **V1 MI3 / FFIEC PDD status check** — REGINALD's V1-fast falsifier; window 5/14-16 passed without integration

**Open BROCK items (deferred to BROCK next session):**
- CDR Q1 5-cat NDFI bulk release pull (May 15 release; first publicly available 10.a-10.e splits)
- OTF release date confirmation (highest priority — 74.2% software concentration)
- GCRED / BCRED / CTAC release date confirmation
- ARES Q1 release status verification
- MS BCI 19.73% / CUBI 33% primary-source confirmation (currently WALTER-sourced)
- LESSONS #16 PROME design note (execution rails)

## Cautions for Next Session

- **BOND artifacts untracked-by-design.** BOND owns commits on next live boot. Do NOT git-add as Prome.
- **Q4 resolves mechanically off today's 1pm auction.** Do not pre-empt; wait for BOND's dual-grade verdict.
- **5/12 10Y fire under v2 is TIGHT** (51.5% vs 52.0% = 0.5pp margin). Future near-boundary prints need explicit margin annotation.
- **HEARTBEAT.md stale** (~3-4 days). Will-approval gate; fold today's tape + V2.2 + BROCK framing post-auction.
- **OZK STATUS still pre-roll posture** (hygiene, not execution risk).
- **Do not spawn:** CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome. BOND OK in teams mode.

## Live Carry: Posterior Shifts Tracked This Morning

| Item | Pre-closeout view | Post-closeout view |
|---|---|---|
| APO put hold/roll/cut | 🔴 Pending (10+ days waiting) | **Resolved** — Dec hold, Jun let-expire |
| FSK fresh premium | 🔴 Pending discussion | **Resolved — no** (KKR structurally long defense) |
| BDC fresh entry | 🔴 Pending | **Resolved — no yet**; triggers documented |
| WAL thesis weight | v2.1 (Bear-slow case) | **v2.2 — Bear-medium 30% dominates Bear-fast 12%** |
| WAL EV | $70.50 | **$67.98** |
| REG-25 confidence | 55% | **75%** |
| BROCK convergence | 38/50 🔴 | **46/60 🔴🔴** |
| Trap-clinching framework | HENRY conceptual | **Canonized in BROCK STATUS + TRADE.md §9** |
| Execution-rail process gap | Implicit | **LESSONS #16; PROME design note owed** |
