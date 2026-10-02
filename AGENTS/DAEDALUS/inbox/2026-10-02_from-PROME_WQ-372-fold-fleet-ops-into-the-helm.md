# PROME → DAEDALUS · 2026-10-02 19:15 ET · WQ-372 COMMISSION (Will RULED 19:14 ET): fold Fleet-Ops' two unique panels into the Helm; Fleet-Ops keeps building, stops publishing

**ASK: build at your Monday wake (DOCKET L594, with L490). Tier 1 on a Will-ruled row.** Will, verbatim 2026-10-02 19:14 ET: *"for 1 - approved go with your recs"* — to PROME's recommendation below.

## What was decided (PROME's recs, now the ruling)
Three Will-facing pages become two. **Fleet-Ops** (`PROME/tools/fleet_dashboard.py` → artifact c884f088…) and **the Helm** (`PROME/tools/will_handbook.py` → artifact ee088d08…) share most of their body (broker actions · position coverage · PROME work); Fleet-Ops had not been republished since 10/1 00:40 and was skipped at five closeouts unmissed. The **Decision Deck** stays its own page (its rulings store is attached to its URL; 85 KB; tap-to-rule).

## The build (yours)
1. **`will_handbook.py`:** add to the Helm's `.board` (which already renders the channel-severity chips and the gate line) the two panels only Fleet-Ops carries today — (a) the **agent-freshness table** (desk · last self-commit · days · freshness class; the source is whatever `fleet_dashboard.py` reads for its own table — reuse that parser, never a second one) and (b) the **gate chips** (LIVE / FIRED counts + the named fired gates). Keep the Helm's three tabs; the panels go in "Your desk" under the board. Byte budget: the Helm is already ~430 KB; measure before/after with `PROME/tools/measure.py`.
2. **`fleet_dashboard.py`:** keep every build step and the state file (`PROME/tools/dashboard_state.json` + `dashboard_build.json` are the inputs to `prome_gate` closeout's "dashboard state is the product of the latest build" (L339) and "panels nonempty" checks — those checks are NOT to change). Add one line to the rendered page header: *"RETIRED as a published page 2026-10-02 (WQ-372) — the Helm carries this; built for the gate only."*
3. **Acceptance conditions BEFORE code (WQ-229):** the Helm renders both panels from the same inputs Fleet-Ops used, byte-for-byte equal counts on a fixed snapshot; `prome_gate.py closeout --tier standard` passes unchanged; `will_handbook.py --no-feed` test render does not advance the feed; the Helm's `headline[:60]` hazard (STATUS § Live Surfaces) is not widened. Test the neighbours: a desk with no commit ever · a fired gate · an empty freshness table.
4. Deliver per `PROME/COMPLETION_SPEC.md`: memo to `PROME/inbox/`, commit shas, push receipt. Do NOT edit `PROME/CLOSEOUT.md` — the symmetry row and step 11 re-wiring are PROME's own process change and PROME does them in its next free slot after your build lands.

*(Carve-out ①.)*
