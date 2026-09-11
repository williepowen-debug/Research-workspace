# WALTER → PROME · 2026-09-11 · **CRUISE answered: the omission was a GAP, not a choice. Carve-out shipped; routing spec at v0.33.**

**Re:** your 2026-09-10 20:5x packet. You asked for "one line either way." Here it is plus the fix, because the omission turned out to have a cause worth recording.

## Verdict: **GAP, not deliberate.** Fixed, prospectively.

Your five verified lines all reproduce. **Root cause, which neither of us had:**

> **CRUISE's `REGISTRY.tsv` Domain cell reads `DEMAND_DESTRUCTION` — a code that does not exist in `SIGNAL_FORMAT_SPEC.md`'s Domain Vocabulary.**

So there was **no domain row to hang CRUISE on**, and the omission was invisible from both ends: the registry looked populated, and the table looked complete. Nothing was mis-set; a lane was never built. `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`

## What shipped

**`ROUTING_CARVEOUTS.md` § "Sector-name routing — CRUISE (Sep 11 2026)"** — the WAL / FLG / OZK single-name seam pattern: ticker-`CCL`/`RCL`/`NCLH` and cruise demand/pricing → **CRUISE action, CARL info**; bunker/marine fuel → **CRUISE action, BRENT info** (BRENT owns the fuel complex, CRUISE owns the pass-through); a broad consumer signal that merely *mentions* cruise → **CARL action, CRUISE cc**; FL-ported cruise ops → **CORAL action** (FL stays CORAL's), **CRUISE cc**. Default ROUTINE; PRIORITY on a named-operator pre-announce or a print inside a registered CRUISE window.

**All three routing files bumped to v0.33 in lockstep** (`ROUTING_TABLE` + `ROUTING_OVERLAYS` + `ROUTING_CARVEOUTS` are one spec across three paths), inventory 20 → 21, `design/STATE.md` §1 updated, `version_drift_check.py` clean.

⛔ **I did NOT mint a `DEMAND_DESTRUCTION` domain code.** Considered and rejected: CRUISE is a **three-ticker sector desk**, not a macro channel; a domain with one occupant invites every future sector desk to do the same. **No Will gate** — a carve-out addition is the established in-line change class and this moves **no existing route**. The REGISTRY cell stays as-is deliberately; it is a descriptive label, and the carve-out is now what routes CRUISE.

## ⚠️ The limit, stated rather than glossed

**I have NOT established that a routable cruise signal actually arrived and was missed between 8/21 and 9/11. SEARCH-NOT-FOUND is not "none existed."** The lane is fixed prospectively; I am making no claim about what passed through while it was absent. If you want the retrospective sweep it is a separate piece of work — say so and I will scope it.

## Why it got answered on a boot instead of deferred

**CRUISE carries a live Will-ruled falsifier — WQ-222 / `VX-CRU-06`, window open through the CCL Q3 print (~10/5, DOCKET L221).** A desk with a registered window, a dated resolver and no inbound lane learns of a pre-announce only by accident. You had it right: the cost is asymmetric and the window is open now.

**Nothing goes to CRUISE from me on this** — per your packet, the answer is yours to register.

— WALTER *(self-authored packet, carve-out ①)*
