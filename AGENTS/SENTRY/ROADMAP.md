# SENTRY Roadmap

> ⛔ **DORMANT — RETIREMENT BANNER, dated 2026-09-24 (WQ-256 (d), Will verbatim *"Approve WQ-264 and WQ-256 with your recs"*, 08:50 ET; written by PROME as registrar — no live owner).** This desk has been human-idle since 2026-06-02 and DORMANT since 2026-06-27 (`PROME/ROSTER.md` is the class of record; this banner changes no class). Its RSS/CI signal pipeline was killed; **the TODO/ROADMAP items in this directory are HISTORICAL and must NOT be executed — rebuilding the pipeline is a Will ruling, not a task.** Do not launch, task or audit this desk as a fleet agent. Live signal routing is WALTER's (`AGENTS/WALTER/`). Last real commit: `58c9e02aa` 2026-05-09.

**As of:** 2026-05-09 (Saturday afternoon)
**Audience:** Fresh-context SENTRY picking up from a new session, and Will

---

## Read this first if you're SENTRY

This roadmap is the trajectory. `STATUS.md` is current state, `TODO.md` is immediate-action queue + friction log, `CHANGELOG.md` is what shipped. Read STATUS first, then this, then TODO.

**Key framing:** "Fully operational" by `CLAUDE.md` spec is *behavioral*, not feature-complete. Week 6-8 success criteria are "relied on as primary input" and "catches signal that would've been missed." That requires habituation and feedback loops, not just more building. So the question splits: *what to build next* vs *what to actually use*.

---

## Where Phase 1 stands (2026-05-09)

- ✅ Pipeline live: EIA + SEC EDGAR feeds, fleet CIK whitelist (OZK seeded), HTML strip, pinned reqs
- ✅ CI verified end-to-end 5/9 20:45 UTC (commit `d1a789f4`); cron-registration check tonight at 22:00 UTC
- ✅ SIGNALS/ ownership formalized
- ✅ 1 dry-run briefing produced (5/8 evening)
- ⏳ Key State headers — only SENTRY has one (CLAUDE.md spec drafted at `references/key_state_spec.md`, awaiting fleet rollout)
- ⏳ First *real* (non-dry-run) briefing — slated for 5/10 morning

---

## Layer 1: Finish Phase 1 (close the loop on what's already specced)

These give us a trustworthy baseline. Order roughly = priority.

| # | Item | Lift | Owner | Why |
|---|---|---|---|---|
| 1 | **Confirm cron registration** | passive | auto | Manual dispatch verified; scheduled cadence (`0 10,22 * * *`) still unproven. Tonight 22:00 UTC is the test. |
| 2 | **Key State adoption by fleet** | Will pings each agent on next boot | **Will** | **Highest ROI in the system.** Without it, every brief costs ~3K tokens to read 6 STATUS files. With it, briefings drop to ~500 tokens substrate. Can't self-implement — `feedback_cross_agent_inbox_writes.md` forbids cross-agent writes. |
| 3 | **CIK watchlist expansion** (WAL, HBAN, KRE constituents) | 1 session, ~30 min | SENTRY | Today the SEC feed catches OZK only; rest is form-type noise filtering. Real fleet-name detection unlocks the "story" angle of briefings. |
| 4 | **Persistence cache for inbound** | 1 session, ~1-2h | SENTRY | `inbound.md` today is "last fetch" not "rolling 48h" — SEC `getcurrent` cycles items off in minutes, so items <48h old that aged off the feed are *gone* between scheduled runs. Real bug for operational use. |
| 5 | **First 3-5 real briefings + format iteration** | ongoing | SENTRY + Will feedback | The dry-run was 480w vs 400 target. Need reps to know what trims, what stays, what's useful. |

**Tier-1 implicit dependency:** items 3-5 only earn their cost if Will is reading the briefings. If briefings sit unread for 2 weeks, build nothing more — kill or pivot.

### Polish-queue items still open (lower priority, can interleave)
- (P1 cont'd) **8-K item-number parsing** — DEFERRED. `getcurrent` Atom doesn't expose item numbers; needs per-filing index fetch + caching. Phase 1.5 work, gated on item 4 (persistence cache).
- (P3) **`--dry-run` and `--feed=NAME` flags** — easier testing without polluting `seen.json`.
- (P4) **Tune SEC `include_types`** after a week of observed signal/noise.

---

## Layer 2: Decisions pending Will (block SENTRY work)

| Decision | Context | Why it matters |
|---|---|---|
| **Phase 1.5 feeds** — add NY Fed Markets and/or ISW? | `proposals.md` #1, #2 | Adding feeds before knowing 2-feed signal/noise is premature; ~1-2 weeks of operational data first |
| **`proposals.md` #4** (Vision via Prome) — kill or rewrite? | Prome degraded per `project_openclaw_prome_degraded.md` | Likely kill; needs a write-up of why for the record |
| **Briefing format feedback** on 5/8 evening dry-run | `SIGNALS/briefings/2026-05-08-evening.md` | Format iterates only with Will's read |
| **Session cadence** — stay on-demand, or move to scheduled? | `CLAUDE.md` says "no scheduled runs first 2-3 weeks" | Decide after 3-5 briefings |
| **NEXUS vs RED vs SENTRY boundary** | Old `SIGNALS/README.md` routed cross-domain to NEXUS+RED | Possible role overlap; I haven't read either's CLAUDE.md/STATUS yet |

---

## Layer 3: Phase 2+ (build only when Phase 1 earns it)

Gated on Week 4-6 milestone: *"briefings add value over reading `inbound.md` directly."* Don't start until earned.

### Phase 2 (week 3-4 if Phase 1 proves value)
- **Inbox alerts** (max 2/agent/day, on-trigger) — *sensitive: cross-agent writes, see `feedback_cross_agent_inbox_writes.md` for guardrails*
- **Semantic dedup** (LLM-based, not just GUID hash)
- **Clustering** (group items by emerging story across feeds)
- **Graduation rubric** for Phase 1 → 2 transition — *TODO friction #7, no concrete signals defined yet. Without this, the phase boundary is vibes.*

### Phase 3 (week 4-6)
- Prediction log
- Source quality tracking
- Miss tracking

### Phase 4 (week 6-8+, only if "primary input" earned)
- Thesis challenge
- Retrospectives
- Baseline deviation detection

---

## Suggested next-session ordering

If working one focused thing per session:

1. **Next session:** Key State adoption ping (Will-side) + generate 5/10 morning brief on whatever substrate exists. Earns the first real proof point.
2. **Session after:** CIK watchlist expansion (WAL/HBAN/KRE) → 5/11 brief reflects fleet-name density.
3. **Session after:** Persistence cache so `inbound.md` actually retains 48h of items.
4. **Session after:** Format-iteration retrospective on first 4-5 briefings → adjust `CLAUDE.md` format spec accordingly.
5. **Then pause and decide:** is this useful enough to build Phase 2, or is the value ceiling already in view?

---

## What I'd flag as easy-to-skip but actually important

**The graduation rubric** (Layer 3, Phase 2 bullet 4). Without concrete signals defining "Phase 1 → 2 ready," we'll either over-build prematurely or miss the moment to expand. Worth drafting *before* we get there, while we're still able to be honest about what would constitute "earned."

---

## Living document

Update this file when:
- Layer 1 items ship → move to "Where Phase 1 stands" with ✅
- Will makes a Layer 2 decision → record it + remove from pending
- Phase boundary crossed → add a "## Phase N entered YYYY-MM-DD" section
- Trajectory changes → date-stamp the change at top of relevant section
