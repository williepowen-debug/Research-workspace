# MARCO MEMORY — Persistent Learnings
**Created:** 2026-06-15

Durable, MARCO-specific learnings — the tier *between* the per-session handoff (`SCRATCH.md`, overwritten each session) and cross-agent auto-memory (`~/.claude/.../memory/`, loads at every boot, transferable lessons only). What lives here: MARCO's characteristic errors, source-quality map, and operational caveats that aren't thesis-level (→ `thesis/THESIS.md`) and aren't transferable enough to promote (→ auto-memory). **Boot-read; pruned/promoted at closeout.** When a learning here becomes cross-agent-transferable, promote it to auto-memory and remove it here (don't duplicate).

---

## Genesis
Migration / population-movement agent. Durable two-channel spine: (1) ag-labor stock shock (2.2M self-deportation, enforcement-funding now law through Jan 2029) + (2) Canadian-travel boycott (air/snowbird structural, capacity deleting, FL-$ hole winter 2026-27). Full thesis → `thesis/THESIS.md` (v2.5).

---

## Characteristic analytic error (watch this first)
- **Single-mechanism over-attribution.** MARCO's recurring failure mode: crediting a multi-causal price/quantity move to one channel. Twice-burned: **produce CPI** (v2.1 — freeze + tomato tariff + diesel/freight co-drive; labor demoted to one co-driver) and **April construction starts** (broad + rate/affordability-confounded; the South — the raid-target region — fell *least*, geography running *against* the raid signal). **Before crediting a multi-causal move to one channel: run the multi-causal check, and separate mechanism-intact from threshold-breached** ([[finding_threshold_vs_mechanism]]). The produce-thermometer demotion is the template for every "is this really my channel?" call.

## Source-quality map (MARCO-specific; general principle → [[feedback_pull_live_primary_not_dashboard]])
- **Pull primary before transcribing any load-bearing figure.** Search snippets / trade-press garble exactly the decimals that drive canonical text + confidence changes. Session-14 alone: StatCan air mis-read as "+3.0%" (real −5.5%); F&V "+6.1%" looked identical across Apr/May (verify same series, not same number); housing regionals returned 3 conflicting reads from snippets; a CalculatedRisk slug was April **2025** not 2026. Canonical sources: **BLS / Census (NRC primary XLS) / StatCan Daily / Banxico / OFLC**.
- **Known garbled / blocked sources:**
  - *Banxico English trade-press* — garbles remittance prints (e.g. the "$5.69B/+26% Apr" claim). Use Banxico primary + watch count YoY as the clean SDL-01 readout.
  - *MCO / FLL airport pax* — locked in non-extractable PDFs; web search surfaces only operational-disruption news. Recurring blocker.
  - *CalculatedRisk / undated housing slugs* — check the YEAR in the URL (April-2025 vs -2026 collision).
  - *BLS WebFetch* — 403s on cpi.htm/pdf; use the cpi.nr0.htm summary via WebSearch + a secondary (Fox/Kiplinger) for table detail, and flag the fresh-F&V-vs-aggregate line as unconfirmed until the primary table is read.

## Operational caveats (live)
- **World Cup = dual-surface event-mask** (MIA pax + L&H hospitality jobs). Discount Jun/Jul beats on both surfaces; the tell is post-Jul-19 **sustained-vs-fade**. Advance signals already lean FAIL (host-city hotels ~80% below forecast). Real read = NTTO June print ~mid-Aug (ES-MARCO-09). *(Time-bound — retire after the tournament resolves.)*
- **MARCO carries no position.** Theses express downstream via REGINALD (bank/CRE), CARL (consumer), LABOR (employment). No P/L, no marks — don't import position-management framing.
- **Sweep handoff surfaces LAST in closeout — after the canonical edits + version bump land.** The recurring drift class (session 14, caught by Prome): SCRATCH PUSH-STATE/OPEN-THREADS and NEXUS_BRIEF version fields (Status/Thesis-version/pivot lines + Jun-30 forward-row %) get written *mid*-closeout, then the final canonical changes (THESIS version bump, prediction re-rates, the push itself) land after — so the handoff surfaces freeze stale. Session 14 shipped NEXUS_BRIEF still v2.4 / MAR-26 78 and a SCRATCH that said "push pending / write-back pending" after all of it had actually landed; worse, the commit that removed the brief's interim-warning ("canonical now synced") left the stale body, so NEXUS would read v2.4/78 as current with nothing flagging it. **Fix = make the handoff-surface re-sweep (NEXUS_BRIEF version fields, SCRATCH PUSH-STATE/OPEN-THREADS, STATUS session tag) the LAST closeout action, after every canonical edit + the push status is known.** A reviewer scoped to canonical *analytical* surfaces (THESIS/CHANGELOG/STATUS-dashboard/PREDICTIONS/docket) will miss this — handoff surfaces need their own explicit pass. *(Transferable to any agent with NEXUS_BRIEF + SCRATCH — SAM/BRENT/VIOLET; promote to auto-memory if it recurs cross-agent.)*

---

## Session arc (durable trajectory only — per-session detail lives in SCRATCH)
- **2026-06-15 (session 13/14):** Pull Session 2/3 catch-up; thesis v2.4→**v2.5** (Channel-1 enforcement flow re-locked, funding now law). First Orc/Prome two-reviewer cleanup loop — caught the two characteristic errors above; this MEMORY.md created from that loop. Boot-maturity now ~full parity with SAM/BRENT/VIOLET (boot.py + NEXUS_BRIEF built session 12; MEMORY.md session 14). Remaining maturity gaps: PREDICTIONS_ARCHIVE + calibration scoreboard; MAINTENANCE.md is a punchlist not a structural-change log.
