# NEXUS SIGNALS — Live Unresolved Cross-Agent Signals

**Last reset:** 2026-06-06 (self-audit Phase B). Old 5/21 reset cleared — its SIG-M01..M08 were 1:1 mirrors of STATUS matrix and violated the "SIGNALS is not a copy of STATUS" rule.
**Purpose:** Routed signals that have **not yet** been absorbed into STATUS convergences. If a signal is already in STATUS matrix → it belongs in STATUS, not here. SIGNALS is a queue, not a copy.

---

## Lifecycle

1. Signal arrives via `inbox/`, `AGENTS/SIGNALS.md`, or routed delivery.
2. NEXUS evaluates: new convergence, upgrade/downgrade existing, contradiction, or stale/noise.
3. If absorbed into STATUS → archive to `signals_archive/` with C/M-XX mapping; remove from this file.
4. If resolved/superseded → archive with outcome.
5. If still developing → stays here with next evidence.

---

## Active (awaiting integration in E-phase worldview pass, pre-2026-06-09)

| SIG-ID | Date | Source | Signal | Maps to | Status | Priority |
|---|---|---|---|---|---|---|
| **SIG-26060601** | 2026-05-15 | BRENT → `AGENTS/SIGNALS.md` | **Path B Trigger #3 fired** — CFTC MM net longs 70,791 (May 5), down 29K from 99,887 peak over 2 wks at Brent $106–111 = distribution. 1/3 Path B triggers fired. Phase 2 watch active. | **M-06 candidate downgrade** ("energy premium deflating" leg) | Awaiting E integration. Pending fresh BRENT header verify (signal is 3 wks old). | 🔴 |
| **SIG-26060602** | 2026-05-22 | HAWK → `inbox/` | **Iran/Hormuz reframed** from one-way escalation to bifurcated partial-thaw/grind: C 55% / D 35% / B 10%. Barakah adds nuclear-infra target class; Chinese tanker egress + Trump attack call-off add thaw/carve-out class. May 25-29 next classification window (now passed). | **M-06 candidate downgrade** ("war path softened" leg) | Awaiting E integration. Pending fresh HAWK header verify (signal is 2 wks old + 5/25-29 window passed). | 🟠 |
| **SIG-26060603** | 2026-05-14 | Will screenshots → `inbox/` | **Gamma/momentum calm may be mechanical** — gamma surged near-record low → near-record high in weeks (fastest on record); 0DTE cited as amplifier; momentum dominant equity factor. MacroScope late-2021 analog: 1-2mo countdown to top. | **M-04 reinforcement** (vol/gamma suppression as mechanical) | Partially aligned with M-04 but never logged. Integrate in E. Countdown clock ~5/14 + 1-2mo → fires mid-June to mid-July window. | 🟠 |

---

## Convergence note (advisor-flagged 2026-06-06)

**SIG-26060601 + SIG-26060602 are independent roots pointing same direction (energy risk premium deflating):**
- CFTC positioning unwind (paper longs leaving while price holds at $106-111)
- Geopolitical de-escalation (Trump call-off + Chinese tanker egress + thaw-class weight rising)

Both hit M-06 ("Energy/stagflation pressure persists, war path softened, 55%"). Likely E-phase action: **M-06 downgrade toward "Energy premium deflating / stagflation channel weakening"** with knock-on prior on M-03 (duration channel) and the broader stagflation-trap framing. Pending fresh BRENT + HAWK header verify before locking — both signals are 2-3 wks old.

---

## Recently Archived / Superseded

| Old signal | Action | Reason |
|---|---|---|
| SIG-M01..M08 (5/21) | Cleared 2026-06-06 | Were 1:1 mirrors of STATUS matrix M-01..M-07 + FORGE no-trade-rails guardrail. STATUS is canonical for absorbed convergences; SIGNALS reserved for unresolved queue. |

---

## Next NEXUS Pass

E-phase worldview refresh, pre-2026-06-09 (June 9-11 nominal auctions). Priority:
1. BRENT + HAWK headers — validate SIG-01/02 still current.
2. Integrate energy convergence into M-06 with new Conf % + Δ.
3. Process SIG-03 gamma signal into M-04.
4. Move all three to `signals_archive/` with C/M mapping after integration.
