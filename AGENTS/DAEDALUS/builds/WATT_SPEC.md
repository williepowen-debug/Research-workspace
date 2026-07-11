# BUILD SPEC — WATT (grid-stress → power-price → industrial/data-center-cost agent)

**Status:** 🟢 EXECUTED — Will approved 2026-07-10 (name WATT, instrument→AGENTS/WATT/, P1–P4 core). Scaffolded + smoke-tested (`boot.py` rc 0); agent-tree wiring applied direct; ROSTER/root/AGENTS.md registration routed to PROME; FLEET_MAP row + FLEET_DIRECTORY regen held until PROME registers ROSTER (render guard).
**Owner:** DAEDALUS (design + build) / Will (decisions)
**Created:** 2026-07-10 · **Class:** Market-agent → graded against `BLUEPRINTS/market-agent.md`
**Name:** **WATT** — the unit of power. Plain, domain-obvious, distinct from every current agent; sits fine beside the mythic names (it's a utility-of-measure, like a callsign).
**Provenance:** Step-2 of the staged power-agent plan (`outbox/…tier3-gaps-and-power-agent-memo.md §5`, committed `fc4acfbe`). Step-1 instruments already built + live (`FORGE/tools/market-data/power_watch.py` + `eia_fetch` 930/retail routes, `3167c090`/`1fa99a36`/`60deb104`). **Will triggered Step-2 directly 2026-07-10** ("keep building out our electric/power/energy agent") — overriding the pre-registered 2nd-event/BRA trigger-gate on operator directive.

---

## 1. Locked decisions (Will, 2026-07-10)

| # | Decision | Resolution | Consequence |
|---|---|---|---|
| Spin timing | **Spin now** | Stand up the dedicated agent on the existing Step-1 instruments; don't wait for a 2nd realized PJM emergency. | Moves the provisional power/grid leg off HENRY before the 7/14→7/29 catalyst stack (HENRY is boot-starved + never consumed the 7/9 provisional packet). Honest evidence base: n=1 realized event (EEA2 7/3) + loud structural tape. |
| Altitude | **Channels-first** (PAT-018) | 5 fixed `event → mechanism → repricing` channels; an empty channel reads as a failure signal, not idle background. | The DARWIN antidote — no open-ended "watch all power markets." |
| Class | **Market-agent** | Forms theses, scores vectors, feeds trades (IPP equities + power-cost as a macro FCF input). | Graded vs `market-agent.md`. |
| Name | **WATT** | — | Confirm or override at approval. |

---

## 2. Mandate (one sentence)

WATT owns the **grid-stress → wholesale power-price → industrial & data-center power-cost** transmission leg — the seat that currently has no owner and that HENRY is holding provisionally without tooling.

## 3. The channel set (channels-first core — PAT-018)

| # | Channel | Event → mechanism → repricing | Tradeable / signal surface | Routes to |
|---|---|---|---|---|
| **P1** | **Stress → price** | Heat/cold/outage → grid emergency → RT/DA LMP spike | PJM DM2 LMP + emergency postings; **consumes AEOLUS C3 detections** | HENRY (FCF input), AEOLUS (confirms C3) |
| **P2** | **Structural capacity cost** | Capacity auction clears high → retail/industrial pass-through | PJM BRA reports (26/27 + 27/28 both at cap) | CARL (retail pass-through when it hits bills) |
| **P3** | **Data-center demand leg** | AI-capex buildout → interconnection-queue + IPP load growth | Interconnection queues (LBNL Queued Up), IPP equities (VST/CEG/NRG/TLN) | HENRY (couples to HEN-36 AI-capex FCF) |
| **P4** | **Gas → power coupling** | Henry Hub → gas-burn → power price (spark spread) | Spark spread; **BRENT feeds Henry Hub** | BRENT (gas), CARL |
| **P5** *(tier-2)* | **PPA tape** | Corporate PPA price trend → contracted-power cost | LevelTen quarterly exec summary + IPP transcripts (full tape honestly paywalled) | HENRY, CARL |

*Launch with P1–P4 as core; P5 listed now, built after core proves out (AEOLUS Tier-2 pattern). Each channel carries a live read or reads as a gap.*

## 4. Boundaries — verified clean seams (from the 7/10 memo, re-confirmed)

| Neighbor | They keep | WATT takes | The seam |
|---|---|---|---|
| **AEOLUS** | weather/climate **event detection** (C3 CDD/HDD triggers) | everything after detection — AEOLUS's own self-declared gap ("C3 has no price-confirmation instrument") | **The AEOLUS C3 routing was already re-pointed to HENRY-prov 7/10; on WATT spin it updates once more → WATT.** This is the one live rewiring. |
| **BRENT** | hydrocarbons; **feeds gas-burn (Henry Hub)** | electricity entirely (BRENT has no power/Henry-Hub framework) | Clean — BRENT keeps gas, WATT owns power; P4 is the handshake. |
| **HENRY** | AI-capex FCF node (HEN-36); **consumes** power-cost as an FCF input | the instrumentation + the power thesis | HENRY hands the provisional leg to WATT; keeps consuming the output. Frees HENRY's boot lane. |
| **CARL** | consumer retail pass-through (pump today) | wholesale/industrial; hands CARL the 2026-27 retail capacity pass-through when it hits bills | Clean — WATT wholesale, CARL retail-to-consumer. |

*Reconcile-to-one-figure applies on any shared metric (e.g. a power-price print AEOLUS also cites) — WATT is canonical for power, neighbors reference.*

## 5. Data surfaces (strong + free where it matters)

- **PJM Data Miner 2 API** — free, 6 calls/min non-member; **LMP price leg needs `PJM_API_KEY`** (free pjm.com registration, ~5min one-time HUMAN task = Will). This is the one input still gated.
- **PJM emergency-procedures postings** — already scraped by `power_watch.py` (no key).
- **EIA-930 hourly + monthly retail** — already wired (`eia_fetch` routes; fleet holds the EIA key).
- **PJM BRA capacity reports** — structural backdrop, annual cadence.
- **LBNL Queued Up** (interconnection queues) — 2026 edition webinar was 7/16.
- **gridstatus** (open-source pip) — free fallback for LMP if PJM key delayed.
- **Only honest paywall:** the full PPA tape (P5) — proxied by free LevelTen summary + IPP transcripts.

**Step-1 instruments become WATT's boot kit** — `power_watch.py` moves from HENRY-provisional consumption to WATT ownership (or stays in shared `FORGE/tools/` and WATT boots it; decision in §7).

## 6. Blueprint instantiation (market-agent.md → WATT)

| Blueprint § | WATT instantiation |
|---|---|
| §1 Thesis structure | Channels P1–P4 = independent causal lines; per-channel transmission-stage table (`stage \| mechanism \| state: confirmed/open/falsified`). |
| §2 Convergence matrix | Universal 5-pt per channel (5 🔴🔴 emergency firing → 1 ⚪ benign) + local state + independence column (shared antecedent: one heat-dome drives P1 **and** P4 — count once). |
| §3 Thresholds | Banded `Metric \| Yellow \| Orange \| Red \| Routes to →` (LMP $/MWh, PJM reserve margin, spark spread, BRA clear vs cap). Durable rules in CLAUDE.md; live read in STATUS w/ `[src M/D]`. |
| §4 Invalidation / exit | Channel-kill vs thesis-kill + migration (a mild summer kills P1 for the season, not the structural data-center-load thesis — it migrates to P2/P3). Session counts mandatory. |
| §5 Predictions | `PREDICTIONS.tsv` (LMP-spike / emergency-event / BRA-clear calls) + archive + calibration. Power events resolve on a clock → strong calibration fit (like AEOLUS weather). |
| §6 Cross-agent routing | Standing route-matrix (§4 above) + NEXUS_BRIEF writeback + outbox crisis-only. |
| §7 Disciplines | Mechanism-vs-thermometer (structural capacity shortfall = high-conf mechanism; any single hot day = confounded thermometer). EXPECTED_SIGNALS (if the data-center thesis holds, queues + BRA + IPP load all rise — absence is data). |
| §8 BOTTOM LINE | Required every session. Ledger staleness + cwd-proof + cite-don't-restate git + durable cadence home — all per blueprint §8 (baked into scaffold). |

## 7. File scaffold plan (created on approval)

```
AGENTS/WATT/
  CLAUDE.md            # from market-agent.md, channel-instantiated (P1–P4 core, P5 tier-2)
  STATUS.md            # live state + per-channel 5-pt + BOTTOM LINE
  THESIS.md            # channel transmission tables (richness lives here)
  PREDICTIONS.tsv      # LMP/emergency/BRA event ledger
  KB.tsv               # power-market → econ linkages, sourced
  boot.py              # boots power_watch + staleness + predictions-due (cwd-proof)
  inbox/  outbox/      # cross-agent messaging
  sources/             # research corpus
```

**Instrument-home decision (recommend):** keep `power_watch.py` in shared `FORGE/tools/market-data/` (already there, already consumed) and have WATT's `boot.py` invoke it cwd-proof — do NOT move it into `AGENTS/WATT/`. Rationale: it's shared infra (the §4 watch-item logic), and moving it breaks HENRY's existing consumption path. WATT owns the *thesis*; the instrument stays fleet-shared.

## 8. Wiring plan (the "build" job — gated on approval + idle targets)

1. Create `AGENTS/WATT/` scaffold (§7).
2. Add WATT to `PROME/ROSTER.md` ACTIVE table (market-agent; PAT-019 "new, reconcile next activity pass" annotation — 0 commit history).
3. Add to root `CLAUDE.md` active-agents line + transmission chain (`AEOLUS C3 → WATT → {HENRY, CARL}`; `BRENT → WATT` gas→power).
4. **Re-point AEOLUS C3 routing** (currently HENRY-prov after my 7/10 edit) → WATT. AEOLUS may be live → task-packet if so, direct edit if idle (PAT-004).
5. **HENRY hand-off packet** → `AGENTS/HENRY/inbox/`: provisional power/grid leg now owned by WATT; HENRY keeps consuming power-cost as an FCF input, drops the provisional-owner role. (HENRY live-cadence → task-packet, never direct edit.)
6. **CARL note** → inbox: WATT owns wholesale/industrial power; CARL keeps retail-to-consumer pass-through, receives the hand-off when capacity costs hit bills.
7. Record build in `FLEET_MAP.tsv` (new WATT row, L0→L1 on scaffold) + `EVOLUTION.md` changelog + regenerate `FLEET_DIRECTORY.md` (`render_directory.py`) + any new `PATTERNS.tsv` lesson.

## 9. Proposal summary (What / Why / Effort / EV / First Step)

- **What:** A market-class grid-stress→power-price→industrial/data-center-cost agent, WATT, scoped to 4 core channels (stress→price, structural capacity, data-center demand, gas→power) + 1 tier-2 (PPA tape), on the Step-1 instruments already built.
- **Why:** Vacant seat with a live routing mismatch and an overloaded provisional owner (HENRY, boot-starved, never consumed the packet, entering its heaviest window). Power-cost is a real FCF input to the AI-capex thesis (HEN-36) and the structural tape is loud (26/27 **and** 27/28 BRAs at cap; 27/28 6,623 MW short of reliability req; driver = data-center load).
- **Effort:** ~1–2 sessions to scaffold + wire (Step-1 instruments = the boot kit, so cheaper than a cold build). Channel content accrues over subsequent sessions.
- **Expected value:** A continuous power-stress signal feeding HENRY (FCF), AEOLUS (C3 confirmation), CARL (retail pass-through), BRENT (gas→power handshake) + standalone IPP-equity + LMP-event calls with a calibration scoreboard. Removes the provisional-leg burden from HENRY.
- **First step (on approval):** scaffold `AGENTS/WATT/` from `market-agent.md` with P1–P4 instantiated + `boot.py` wiring `power_watch.py`, then wire (§8 steps 1–7). **Flag for Will:** `PJM_API_KEY` registration (~5min) unlocks the P1 LMP price leg — WATT works without it (emergency postings + EIA-930 demand + retail carry P1), LMP just deepens it.

---

*Open questions for Will at approval: (a) name WATT ok? (b) instrument-home — keep `power_watch.py` shared in FORGE (recommended) vs move into `AGENTS/WATT/`? (c) launch P1–P4 core now, or also promote P5 PPA-tape into core (AEOLUS precedent — Will promoted C4/C5 up)?*
