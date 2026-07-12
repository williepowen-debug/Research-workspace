# OSPREY SCRATCH — 2026-07-12 (spinout day)

**Purpose:** Ephemeral session handoff — the canonical "where are we / what next" file. Read at boot (SPAWN PROTOCOL step 2), rewritten in full at closeout. Disposable: rewritten every session. Persistent learnings → `MEMORY.md`; cross-agent twin → `NEXUS_BRIEF.md`.

---

## CURRENT MARKS (one line)
- Channel state: refineries/products **4 🔴 FIRING** (~1/3 offline) · crude-export terminals **3 🟠 flip-trigger #2 FIRED, damage LIMITED** · shadow-fleet tankers **3 🟠 NEW, MIXED** · Brent ref **~$76-79** [BRENT owns, decoupled]

## SPINOUT NOTE (this session — DAEDALUS build, not an OSPREY live session)
- OSPREY was created 2026-07-12 by DAEDALUS, splitting HAWK's overloaded two-war load into OSPREY (Russia/Ukraine, this agent) + FALCON (Iran/Gulf) + a synthesis HAWK. Full rationale: `AGENTS/HAWK/design/2026-07-12_war-agent-split-spec.md`; build execution: `AGENTS/DAEDALUS/builds/OSPREY_FALCON_BUILD.md`.
- **Everything in this file's content below is HAWK-inherited (from HAWK's 7/12 STATUS/SCRATCH/outbox), NOT independently re-verified by OSPREY.** Treat as a starting baseline, not a fresh sweep. First live OSPREY session should re-run the day-by-day gap sweep before trusting any of this as current.

## INHERITED CONTEXT (HAWK's 7/12 ADDENDUM — the founding calibration incident)
- **The miss:** HAWK scoped its Russia sweep to HAW-15's named terminals; missed a week-long, industrial-scale Ukrainian KINETIC campaign against Russian shadow-fleet **tankers** (Sea of Azov + Black Sea, 7/6-12, ongoing; 21-42 vessels claimed; SBU Sea Baby drones; crude tanker "the Blue" 7/8; suezmax off Novorossiysk; Rostov loading terminal). Shadow fleet is explicitly OSPREY's domain — a genuine miss, now OSPREY's founding lesson (LESSONS.md item 1).
- **CORRECTED TWICE (Will pushed a 2nd time — HAWK was wrong both its boot sweep AND its first "tighter confirmation"):** the crude-export TERMINAL channel WAS struck in-window. Primorsk ~6/25 (named crude terminal, fuel-reservoir hit) + NOVATEK-Ust-Luga complex 7/10 (exports halted) + Vysotsk 7/6 + Kavkaz 6/20 + 7/4 St-Pete Baltic op; Novorossiysk crude terminal also re-hit 5/23+6/8 (pre-window, MISSING from the ledger). **HAW-15 → FAILED** (frozen, HAWK's record).
- **Two compounding causes of the miss:** (a) single-search-per-terminal returned only Mar/Apr headlines; (b) HAWK's OWN energy-strike ledger was stale (6/20) + had already missed the 5/23+6/8 Novorossiysk re-strikes → under-baselined the crude channel. Fixes (now OSPREY's Tier-1 launch discipline): STRIKES.tsv backfilled (7 rows, migrated verbatim into OSPREY's ledger), swept-complete header mark, boot staleness check, closeout sweep. **Market caveat that survives:** in-window terminal damage LIMITED/fast-repair → crude exports not yet degraded → why Brent hasn't ripped (valve shot-at, not closed). BRENT received the correction flag; OSPREY inherits the standing watch.
- **HAW-17 → re-homed as OSP-01** (does the tanker campaign become a world-crude-supply event by Aug 1, or stay attritional/Crimea-fuel? 60% attritional).
- **Conceptual note carried forward:** the crude-export-vs-products distinction is a Brent CHANNEL discriminator, not a "does Ukraine hurt Russian oil" question — refineries free crude (bearish/neutral Brent) while crude-export terminals cut world crude (Brent bid). Keep this framing explicit in future analysis, it under-communicated itself in the original HAW-15 wording.

## WHAT I DID THIS SESSION (DAEDALUS build agent, not OSPREY itself)
- Scaffolded `AGENTS/OSPREY/` per `AGENTS/DAEDALUS/builds/OSPREY_FALCON_BUILD.md` §5: CLAUDE.md, STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, LESSONS.md, MEMORY.md, SOURCES.md, workbook/{KB,SCHEMA,VX,FLOW}.tsv, thesis/{PREDICTIONS.tsv,THESIS.md}, domain/energy-strikes/{STRIKES.tsv,ANALYSIS_2026-07-12.md}, research/ (copy), board_log.tsv, inbox/outbox dirs, templates/SCRATCH.template.md.
- All content seeded from HAWK's frozen 7/12 files (STATUS, SCRATCH, VX/FLOW/STRIKES ledgers, PREDICTIONS, LESSONS, MEMORY, SOURCES) + the two 7/12 outbox packets to BRENT — per DAEDALUS's read-only-on-HAWK, write-only-to-OSPREY constraint. No new research performed.
- No git operations run (DAEDALUS commits after verification, per build spec WP-4).

## NEXT SESSION (first real OSPREY session — dated, future-verifiable)
1. **Independent re-verification sweep** — this STATUS/SCRATCH content is HAWK-inherited as of 7/12; do a fresh day-by-day gap sweep before trusting it as current (per LESSONS.md item 2, live-war boot discipline).
2. **Damage-escalation watch (the single cleanest next tell)** — has the crude-export terminal/tanker channel escalated past "shot at, limited damage" toward a sustained loadings halt or a Kpler-confirmed liftings drop? Feeds BRENT directly if it fires.
3. **OSP-01 progress check** — any movement toward a named-terminal hit / liftings drop / buyer pullback, or does the campaign stay attritional? Window to Aug 1.
4. **Reconcile the 21-42 vessel-strike claim spread** (channel 3) — currently unreconciled across sources, flagged in STATUS.md.
5. **Firm up the thin EXIT RULES section** (CLAUDE.md) — currently deliberately thin-at-launch.

## FIRST-INCREMENT BACKLOG (flagged, not blocking launch)
1. **Russia strike-feed / sanctions-tracker automation** — PAT-048-deferred at launch (instrument-light per DAEDALUS build spec §1 decision #4); this is OSPREY's priority first-increment build. Wire via PAT-041 (durable cadence home) once built — do not land it on a volatile surface like SCRATCH alone.
2. **Russia-war vol/credit FLOW rows** — HAWK's FLOW-04/05 (war→vol, war→credit) were Iran-loaded content and went to FALCON, not OSPREY (build spec §2b ruling). OSPREY needs its own Russia-war vol/credit transmission rows built from scratch.
3. **Firm up the thin Russia-coded exit rules** — CLAUDE.md EXIT RULES section is honest-but-thin at launch; owner firms this up across the first several live sessions.
4. **EU/Druzhba angle expansion** — currently only one row (VX-HAWK-UKR-01's Feb-dated Druzhba-1 pump-station strike); the EU energy-security angle (Hungary dependency, sanctions-carve-out politics) is underbuilt relative to the Baltic/Black-Sea port coverage.

## OPEN THREADS / WATCHES
- 🟠 Crude-export terminal/tanker damage-escalation watch — the standing BRENT-facing tell
- 🟠 OSP-01 (Aug 1 window) — tanker campaign world-crude-disruption test
- 🟡 Vessel-strike claim reconciliation (21 vs 12 vs 42)
- 🟡 First-increment backlog (above) — not urgent, flagged for owner attention

## PREDICTIONS DUE / DECISIONS PENDING
- OSP-01 (Aug 1, tanker-campaign world-crude-disruption test). No Will-decision pending (OSPREY holds no trade book, inherited from HAWK).

## MAIL STATE (one line per surface)
- Inbox (root): clear (fresh dir, no items)
- WALTER lane: clear (fresh dir, no items)
- Outbox: clear (fresh dir, no items — HAWK's two 7/12 BRENT packets stay under HAWK's outbox, not duplicated here)

## PENDING PUSH / GIT (if any)
- Not yet committed — DAEDALUS commits `AGENTS/OSPREY/` via pathspec from repo root after verification (build spec WP-4), per this build's read-only-elsewhere / write-only-to-OSPREY constraint.
