# FALCON SCRATCH — 2026-07-12 PM (first live session + ROUND-2 continuation, same day)

**Purpose:** Ephemeral session handoff — the canonical "where are we / what next" file. Read at boot (SPAWN PROTOCOL step 2), rewritten in full at closeout (step 13). Persistent learnings live in `MEMORY.md`; the cross-agent twin is `NEXUS_BRIEF.md`.

---

## CURRENT MARKS (one line)
- Scenario: **B 8% / C 34% / D 58% (BASE)** — unchanged this session (no re-derivation, marks re-verified not re-scored) · Convergence **~37/50 🔴** · Kinetic risk **🔴** · Brent ref ~$76 [defer price to BRENT; sustain test FAILED → DENY 7/10]

## CHANGES SINCE LAST SESSION
- **This IS FALCON's first live session** — everything before this was DAEDALUS's build-time seed. Inheritance-verified clean: spot-checked STATUS marks, FAL-01 terms (vs HAW-16 in HAWK's frozen ledger — exact match), HAW-14 resolution (exact match) — no drift found.
- **New since 7/10 (the priority-context anchor date):** a Kuwait Oil Company offshore drilling platform hit by drone 7/12 PM (material damage + 1 worker injured) — BORDERLINE FAL-01 instance, held OPEN not resolved, routed to BRENT/PROME. Qatar/Kuwait casualty detail filled in (3 injured Qatar incl. 1 child; Kuwait 3 border posts + the platform). IRGC claims Al Udeid command-center destroyed (UNVERIFIED, Qatar MOD says no casualties). IMO issued a formal avoidance advisory (~6,000 seafarers stranded). IRGC stopped a 2nd vessel (boarding, non-kinetic). CENTCOM/Trump publicly dispute Iran's Hormuz-closed claim.
- **Unchanged (reconfirmed same vintage):** PortWatch transit count still 7/5 (34/88, 39%) — no fresher official print found, site unscrapable. War-risk hull premium ~5%, corroborated via a 2nd source (Star/Xinhua 7/11) — same leg as the 7/10 fire. P&I cover (JWLA-033) still standing since March, no new circular found. Baghdad watch re-run live: still QUIET.

## WHAT I DID THIS SESSION
- Ran boot checks live for the first time: `ledger_staleness.py` (clean, no alert), `baghdad_watch.py` (QUIET, rc 0).
- Inheritance-verified FALCON's seeded content against HAWK's frozen record (STATUS, VX, PREDICTIONS) — clean, no drift.
- **Built `domain/FRESH_LEG_BASELINE.md`** — the standing fresh-leg monitoring surface for BRENT/PROME's GATE-BRENT-SUSTAIN re-arm question (7 legs: war-risk, transits, P&I/JWC, liner reroute, kinetic step, production-hit/FAL-01, sanctions/FAL-02 — each with current state, exact vintage, source, fresh-print bar, check URL, cadence).
- Fresh web pass on Iran-Gulf since 7/10 (task 3) — found the KOC platform hit (flagged, not resolved), Al Udeid claims, IMO advisory, casualty/damage detail, Hormuz open/closed declaratory dispute.
- Registered **FAL-02** (Treasury Jul 17 sanctions wind-down resolver) — GAPS-lens catch, was previously prose-only.
- Ran the DOMAIN_SWEEP_LENSES 4-lens module → `reports/2026-07-12_domain-sweep.md` (8 findings, TOP 3, 4 route-outs for PROME).
- Wrote 9 new KB.tsv rows (KB-FALCON-001..009); updated VX-HAWK-GULFSTATE-01 and VX-HAWK-IRAN-02 with dated new entries; added 1 fresh STRIKES.tsv row (GI-20260712-KOCPLATFORM) + updated ANALYSIS_2026-07-12.md caveat.
- Updated STATUS.md (header, convergence-matrix row, CONFIRMED/CLAIMED/UNVERIFIED table +6 rows, predictions table, BOTTOM LINE) — still under the 250-line cap (129 lines).
- **ROUND-2 (PROME-tasked, same day): strike-ledger backfill EXECUTED** — 5→27 rows, Feb-28 war-start→Jul-12, anchored on the Bloomberg/IJ Apr-7 damage compilation + month-by-month mechanism sweeps. 7 rows carry explicit source-conflict flags; 6 rows carry DATE-UNRESOLVED marks (never invented dates). Headline finding (KB-FALCON-010, ANALYSIS §1): production-class assets WERE hit in Feb-Apr (Khurais/Manifa/South Pars/Ras Laffan/Ju'aymah) — "spared for the ENTIRE war" is cycle-scoped, not war-scoped; FAL-01 base-rate caveat logged (terms/window unchanged). Second find (KB-FALCON-011): VTTI Fujairah struck 5/4 — May was NOT quiet; HAW-15-class gap in the inherited record.
- **ROUND-2: PortWatch probe SUCCEEDED** — `Daily_Chokepoints_Data` FeatureServer is public; built `scripts/hormuz_transit_watch.py` (rc 0/1/2, state JSON, smoke-tested), wired as boot step 5b-2 in CLAUDE.md. Fresh official series 7/1-7/5: 42/36/34/25/34 per day — transits RECOVERING pre-tanker-strikes; only sub-18 prints (6/22: 14, 6/23: 15) are historical, no fresh leg fires (KB-FALCON-012). Residual limit = ~5-8d publication lag, honestly documented.
- **Did NOT** re-derive B/C/D scenario percentages — held at the inherited 7/12 AM marks; the KOC platform ambiguity is a flag, not (yet) a re-mark trigger.

## NEXT SESSION (dated, future-verifiable)
1. **KOC platform disposition** — check whether BRENT/PROME/Will render a verdict on the FAL-01-class question; if it resolves toward "counts," FAL-01 needs re-grading. Check by next boot.
2. **4th US strike round / further kinetic** — did the war continue past 7/12 PM, or hold? First thing to check.
3. **FAL-01 gate watch** (production-infra major-complex hit / vessel sunk) — window to **Jul 26**.
4. **FAL-02 gate watch** (Treasury sanctions wind-down) — window to **Jul 17** (5 days out at registration — tightest clock FALCON is carrying).
5. **Al Udeid damage claim** — check for independent US/Qatari confirmation or denial of IRGC's claimed command-center destruction.
6. **Brent sustain (BRENT-owned)** — does Brent finally break and HOLD >$85 w/ ≥2 legs?
7. **Oman two-route Hormuz proposal** — any dated framework readout?
8. ~~Strike-ledger backfill~~ — **DONE round-2 (same day).** Residual: 6 DATE-UNRESOLVED rows + 3 conflict pairs (Ras Tanura restart, Ruwais date, Mina al-Ahmadi capacity) queued LOW-priority per-facility date-pinning.
9. ~~PortWatch live-scrape~~ — **DONE round-2 (same day):** `scripts/hormuz_transit_watch.py`, boot step 5b-2. **Run it ~7/17-19** — that's when the 7/12 formal-closure impact reaches the official prints.
10. **FAL-01 base-rate caveat follow-through** — if FAL-01 is re-registered after Jul 26, re-derive confidence from the CURRENT-cycle record (post-MOU restraint + Oman channel), not the debunked war-long-sparing frame (KB-FALCON-010).

## OPEN THREADS / WATCHES
- 🔴 KOC platform / FAL-01-class ambiguity — the single highest-leverage open call right now
- 🔴 4th US strike round / further kinetic
- 🔴 FAL-01 hard-gate (major-complex hit / vessel sunk) — Jul 26
- 🔴 FAL-02 (Treasury wind-down) — Jul 17, tightest clock
- 🟠 Oman two-route Hormuz mediation
- 🟠 Iraq/PMF backlash (Baghdad watch automated, QUIET as of 7/12 PM live run)
- 🟢 Strike-ledger backfill — CLOSED round-2 (27 rows; residual date-pinning LOW-priority)
- 🟠 PortWatch ~7/17-19 print check — first official read on the 7/12 closure's transit impact (scripted, boot 5b-2)
- 🟡 Mojtaba public reappearance
- 🟡 Al Udeid damage-claim independent verification

## PREDICTIONS DUE / DECISIONS PENDING
- FAL-01 (Jul 26) — production-infra/vessel-sunk gate, now carrying an active borderline-instance flag.
- FAL-02 (Jul 17) — sanctions wind-down resolver, new this session.
- No Will-decision pending (FALCON holds no trade book); KOC platform disposition is a BRENT/PROME judgment ask, not a Will-approval ask.

## MAIL STATE (one line per surface)
- Inbox (root): clear, checked — no items
- WALTER lane: clear, checked — no items
- BOARD scan: checked `/BOARD/INDEX.md` for FALCON-named rows — none found (expected, brand-new agent)
- Outbox: clear — no outbox file written this session (route-outs live in `reports/2026-07-12_domain-sweep.md` for PROME to deliver per this session's spawn-packet instruction, not written as separate outbox files)

## PENDING PUSH / GIT (if any)
- This session's commits are FALCON's own first live-session commits (pathspec `AGENTS/FALCON/`) — auto-push-at-closeout regime starts now per CLAUDE.md's build-phase note. PROME sweeps at its own closeout; not pushing directly.
