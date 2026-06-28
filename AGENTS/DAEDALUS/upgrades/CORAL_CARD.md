# Upgrade Card — CORAL (read-only assessment, no files touched)

**By:** DAEDALUS · **Date:** 2026-06-27 · **Class:** Market (transmitter — FL household stress → bank loss)
**Method:** `UPGRADE_PROTOCOL.md` (one section at a time) · graded vs `BLUEPRINTS/market-agent.md`
**Note:** CORAL is RICH locally (10 pillars in `COVERAGE.md`, "Coral Bleaching" rails + confirm/falsify in `thesis/THESIS.md`, FL bank leg). Per floor-not-ceiling, every proposal below is an **added handle**, not a rewrite. Nothing here is applied — it's the work queue for your review.

---

| § | Blueprint section | CORAL current state | Applies? | Gap type | Proposed minimal handle | Priority |
|---|---|---|---|---|---|---|
| 8 | **BOTTOM LINE** | absent (0 in STATUS) | ✅ APPLIES | missing handle | Add a 2–4 sentence BOTTOM LINE at STATUS end. Draft from existing "READ FIRST" blocks. | **1 — quick win** |
| 4 | **Invalidation / exit** | confirm/falsify rails in `thesis/THESIS.md`; STATUS lacks them + session counts | ✅ APPLIES | missing handle | Add a one-line STATUS pointer ("Falsification → thesis/THESIS.md") + add `N+ sessions` counts to the existing rails. | **1 — quick win** |
| 2 | **Convergence matrix (5-pt handle)** | SIGNAL DASHBOARD has values; NO universal 5-pt composite. CORAL is a *transmitter* (conditions present, bridge not live) | ⚠️ ADAPTED | judgment call | NOT a forced 14-vector matrix. Add a **light 5-pt handle on the transmission-bridge state** (household-stress: high; bank-loss-bridge: low) so NEXUS can stack it. Keep the 10-pillar richness untouched. | **2 — needs your call** |
| 1 | **Thesis structure** | "Coral Bleaching" linear chain + 10 pillars — already strong | ✅ APPLIES (light) | conformant-ish | Optional: render the bleaching chain as an OTTO-style **transmission-stage table** (stage \| mechanism \| confirmed/open/falsified). Pure upside, low urgency. | 3 — build |
| 3 | **Thresholds** | SIGNAL DASHBOARD = live values | ✅ APPLIES | missing handle | Split durable banded **rules** (CLAUDE, w/ routing) from the live read (STATUS). Add Y/O/R bands to the key FL metrics. | 3 — build |
| 5 | **Predictions** | no `PREDICTIONS.tsv`; tracking via `FL_Forward_Log` | ✅ APPLIES | missing substance | Stand up a small prediction ledger (even 3–5 rows) w/ if-falsified actions. Bigger lift. | 3 — build |
| 6 | **Cross-agent routing** | `FEEDS TO` + `NEXUS_BRIEF.md` + outbox + CLAUDE matrix | ✅ mostly conformant | minor | Confirm route-matrix is current; ensure NEXUS_BRIEF writeback every closeout. | 4 — polish |
| 7 | **Disciplines** | partial (mechanism vs thermometer implicit) | ✅ APPLIES | minor | Make mechanism-vs-thermometer + Δ-discipline explicit. | 4 — polish |

---

## The queue (do in this order)

1. **§8 BOTTOM LINE** — trivial, additive, also clears the fleet-wide batch item.
2. **§4 exit handles** — add STATUS pointer + session counts to existing rails. Cheap, high-value.
3. **§2 convergence handle** — *this is the one needing your judgment:* does a transmitter get a 5-pt bridge-state handle, or is it genuinely N/A? My lean: a light handle (it helps NEXUS), but you may overrule.
4. §1/§3/§5 builds, then §6/§7 polish.

**Each row above is a separate task.** We never do more than one at a time, and §2 doesn't block §8/§4. Recommend starting with §8 — smallest possible proof the method works on a real agent.
