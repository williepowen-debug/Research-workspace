# AEOLUS · SEISMIC — volcanic activity & earthquakes

**Created:** 2026-08-13 (Will-directed) · **Owner:** AEOLUS
**Status: 🟡 EVENT-TRIGGERED WATCH — NOT a core channel** (Will-ruled 2026-08-13)

---

## ⚠️ READ THIS FIRST — the status, and why it is deliberate

**This is the only AEOLUS domain that is NOT a core channel, and that is a design decision, not an oversight.**

My **#1 guard** is channels-first: *an empty core channel is a failure signal I must close every session.* Seismic starts with **zero prior material in my files** — so making it C7 would create a **permanently-visible gap** that I'd burn session time "closing" with landscape-patrol updates that have no transmission behind them. That is the **DARWIN failure mode** my charter exists to prevent, and the fleet grades a cold-start scaffold as **worse than none**.

**So instead:**
- ✅ Sources wired and **verified working** (below) — this is not a stub.
- ✅ Triggers **named, numeric and armed** — so a real event is *caught*, not missed.
- ❌ **No standing live-read obligation.** A quiet month is a **correct** state here and requires no work.
- ❌ **No convergence-matrix row and no 1-5 score** until a trigger fires.

> **The distinction that makes this work: quiet is the expected state, so silence is not evidence of neglect.** For C1–C6, an empty read is a failure. Here it is the base case. **Anyone auditing this folder should check that the TRIGGERS are current and the SOURCES still resolve — not that the dossier has recent entries.**

## 🔑 SCOPE — geophysical, not climate. What earns its place here.

Volcanoes and earthquakes are **not weather**. They belong to AEOLUS only where they run through **transmission channels I already own**, and that constraint is what keeps this from becoming a disaster-news feed:

| Path | Mechanism | Lands in |
|---|---|---|
| **① Volcanic → climate** | **VEI 6+** injects stratospheric SO₂ → global cooling → **crop yield loss** | **C2** (agriculture) — *the genuine climate link* |
| **② Seismic/volcanic → insured cat loss** | major quake in an insured zone → reinsurance loss + ROL | **C1 / C4** (my insurance channels) |
| **③ Volcanic → aviation & supply chain** | ash cloud → airspace closure → freight/logistics | **C5** (supply chain) |
| **④ Seismic → energy infrastructure** | quake near LNG/refining/nuclear/pipeline → supply disruption | **C3**, route to **BRENT** / **WATT** |

⚠️ **Path ① is the one with real historical force and it is genuinely mine:** Tambora 1815 → the "year without a summer"; Pinatubo 1991 → ~−0.5 °C global for ~2 years. **A VEI 6+ eruption is a climate event that reprices agriculture** — that is a C2 mechanism, not a news item.

**⛔ Explicitly NOT in scope — do not drift into these:**
- **Earthquake prediction.** Not scientifically supported. **I forecast consequences of events that have happened, never the timing of ones that have not.** Any "overdue for the Big One" framing is rejected on sight.
- Humanitarian casualty reporting with no market transmission.
- Routine background seismicity — the >100 M4.5+ events/month that reprice nothing.
- **Japan specifics → SAM.** **Florida → CORAL.** **Oil/energy → BRENT.** Route, don't deep-dive.

## 🚦 ARMED TRIGGERS — the point of the folder

**A trigger firing means: log to KB, write the dossier, route to the owner. Nothing fires automatically and nothing here is a score.**

| # | Trigger | Threshold | Routes to |
|---|---|---|---|
| **S-1** | **Volcanic climate event** | **VEI 5+** with confirmed **stratospheric** SO₂ injection | 🔴 **C2 → MARCO/CARL**; global-temp caveat to all channels |
| **S-2** | **Insured cat event** | **M7.0+** onshore within ~100 km of a major insured urban zone, **or** any event with a credible **>$10B insured** estimate | 🔴 **C1/C4 → REGINALD/CREED**; **CORAL** if FL; **SAM** if Japan |
| **S-3** | **Aviation / supply chain** | ash cloud closing a **major airspace or port** >48 h | 🟠 **C5 → CARL/HENRY** |
| **S-4** | **Energy infrastructure** | seismic/volcanic damage to **named** LNG, refining, nuclear or pipeline capacity | 🟠 **C3 → BRENT/WATT** |
| **S-5** | **US volcano escalation** | USGS alert to **WARNING/RED**, or **WATCH/ORANGE** at a **Very High Threat** volcano | 🟡 log + watch (aviation + regional) |

**Discriminator, and it is strict — modeled on the C6 discriminator that works:** an event routes here **only with a dated instrument and a priced or physical consequence.** Magnitude alone is not a signal. **A large earthquake in an unpopulated, uninsured area is correctly a non-event for this file**, however dramatic the number. Say so rather than logging it to look busy.

## PROMOTION / KILL

- **→ core channel (C7):** if triggers fire **≥3 times in ~6 months** with real transmission each time, or a single VEI 6+ event puts a standing climate forcing on the board → **DAEDALUS maturity review, Will-gated.**
- **→ dormant:** if **no trigger fires within 12 months**, mark the folder dormant with a dated banner rather than leaving it to rot silently. **A quiet watch is fine; an unmaintained one that *looks* live is not.**

## FILES

| File | Purpose |
|---|---|
| `README.md` | this charter — scope, triggers, promotion/kill |
| `AGENT.md` | Spawn brief for a domain worker — scope, instrument vocabulary, hard limits, return contract. |
| `RUN_REPORT.md` | **The deliverable of the most recent worker run** (overwritten each run). Absent = no run, or a run that died. |
| `workbook/SERIES.tsv` `LOG.tsv` | **Observations** — time series + dated events. Keyed by `(date, instrument)`; append-only. |
| `SOURCES.md` | **verified working pull commands** (all three tested 8/13) |
| `DOSSIER.md` | baseline state + anything a trigger has caught |

⚠️ **Central `workbook/` remains canonical.** If a trigger fires, the row goes in `AGENTS/AEOLUS/workbook/KB.tsv` with a normal `KB-AEO-NN` ID and a `SEISMIC` group. **Do not fork a ledger here.**
