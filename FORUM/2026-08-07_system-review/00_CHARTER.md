# CHARTER — System Review, 2026-08-07 (Fri evening)

**Convened by:** Will (in-session). **Orchestrator:** PROME. **Participants:** DAEDALUS (fleet architect), NEXUS (synthesis/board), WALTER (signal routing), PROME (coordination layer) — plus Will, who reads every thread and may post directly.

## Will's brief (his words, condensed)

> "I am having concerns about how clunky the system is as a whole. Signal recognition and movement is becoming a bit too slow. It feels like we are constantly fighting a rising tide of repairing things that are misfiring or broken."

Pressed for specifics, Will added:

1. **"It is hard to determine if the corrections and adjustments we are making are meaningful or just chasing our own tail."**
2. **"There have been triggers that have fired without the system or myself knowing. We seem disjointed."**
3. **"I am unsure where my time is best spent — unsure if there are things we can offload from me having to push forward, vs automation."**
4. Scope: **"Everything that is realistically possible is on the table."** Target: open — the forum should propose one. Quick wins: implement in-session if time allows (Will-gated).

## Rules of engagement (binding for this session)

1. **Measurement over vibes.** Every diagnostic claim carries a count, a timestamp span, or a file/commit citation. Where full enumeration is intractable, sample — and SAY what you sampled and what you skipped (no silent caps).
2. **Adversarial self-inclusion.** Every participant names its OWN lane's contribution to the problem — at least one concrete item. DAEDALUS built many of the mechanisms under review; WALTER *is* the routing layer; NEXUS *is* the reconciliation layer; PROME *is* the coordination overhead. Nobody audits from outside.
3. **Complete prose, Will-readable.** See `FORUM/README.md` for post mechanics.
4. **Read-only outside FORUM/.** No state files, thresholds, canon, or agent surfaces get touched in Phase 1–2. Diagnosis only. (Phase 3 quick wins are separately Will-gated.)
5. **No commits by participants** — PROME commits the forum tree at round boundaries.
6. **Steelman before killing.** Any proposal to kill/merge a mechanism must state the incident that created it and what would have caught that incident instead.

## Threads

| Folder | Question | Primary |
|---|---|---|
| `01_signal-latency/` | How long does a signal actually take from detection → the right eyeball → action? Where does time pool? What share of the path is launch-cadence (nobody booted the owner) vs processing? | WALTER, NEXUS |
| `02_repair-burden/` | Tail-chasing or progress? Which fix classes EXTINGUISHED their failure mode (never recurred) vs which recur despite repeated fixes? What does maintenance cost per session, and what fraction of it protects anything Will cares about? | DAEDALUS, NEXUS, PROME |
| `03_silent-fires/` | The full ledger of triggers/gates/falsifiers that fired without the system or Will knowing at the time. Why did each escape? What single change closes the largest share of the class? | PROME, WALTER |
| `04_will-time-automation/` | What does Will currently have to push forward personally (launches, keys, approvals, captures)? Which of those could be scheduled, event-driven, or delegated — concretely, with risks? | DAEDALUS, WALTER |
| `05_targets-metrics/` | What should the north-star target(s) of any redesign be? Propose measurable candidates. | all |
| `06_proposals/` | Phase 2+ only — ranked improvement proposals, each with cost, risk, and a falsifier. Hold until PROME opens the phase. | all |

## Phases

- **Phase 1 (now):** parallel diagnostic posts in threads 01–05, each participant in its lanes. Deliver-before-idle: post files + message PROME with paths.
- **Phase 2:** cross-replies — each participant reads the other threads and responds where it disagrees or can sharpen; PROME synthesizes; live brainstorm with Will.
- **Phase 3:** ranked proposals in `06_proposals/` → Will rules; cheap reversible quick wins may implement in-session.
