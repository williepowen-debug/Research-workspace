# PROME → DAEDALUS · 2026-08-21 · 🟠 · Will-commissioned design ask: close the memory RETRIEVAL gap — 5 items, census evidence attached, one hard constraint (no second store)

**Your role:** DESIGN (your lane: patterns/blueprints/sweeps/scripts). **Gates:** any canon-touching wording (root `CLAUDE.md` line, `MEMORY.md` header rules) returns through Will — design here, word there. No clock; the 8/28 sweep is a natural vehicle for whatever parts fit it, your judgment.

## Will's concern, verbatim (in-session 8/21)

> "I think we are going to run into a situation in which the agents are all rediscovering fixes to problems that other agents have already solved. … perhaps a couple sessions from now a newer agent has to go through this same process and it costs us time/attention/tokens."
> …and on the injected index: "There seems to be little reason for our most advanced agents to be forced injected context for problems they already solved months ago?"

PROME's assessment, Will-concurred: **the store is not the problem — retrieval-at-moment-of-need is.** The corpus, tiers, and flow machinery work (evidence below). What's missing: nothing makes an agent *look* before rebuilding, search-by-symptom doesn't land, tier placement runs on judgment instead of data, nothing promotes a recurring cold lesson, and no step retires incident-rows whose class you've since canonized. Hence five items.

## Evidence base — 30-day citation census (2026-07-21 → 08-21, commit messages; reproduce, don't trust)

```
git log --since=2026-07-21 --pretty="%s %b" | grep -oE "(finding|feedback|project)_[a-z0-9_]+"
```
- **515 citations · 227 distinct slugs · 15+ distinct agents** (PROME 26 commit-subjects, RED 8, WALTER/SAM 5, long tail to ORACLE/HOMER/OSPREY).
- **71% of the hot index (102/144) cited within 30d** — a genuine working set.
- **37% of cold-only slugs (111/303) cited despite zero injection** — the cold tier retains recall; demotion ≠ death.
- **29% of hot uncited in 30d** — demotion candidates *by measurement*, currently invisible to the judgment-driven flow pass.
- Known census limits: commit-message citations are the visible half of usage; a citation often means the agent already knew the lesson (own-desk or hot-loaded) — the census cannot see the agent who *didn't know the slug exists*, which is exactly Will's rediscovery case. Regex wraps produce a little tail noise; ignore truncated tokens.

## The five items

**① Reader-side "solved-elsewhere check" (canon norm — the writer-side twin already exists).** `dedup-before-create` governs writers; nothing governs readers. Proposed norm: *before designing a fix for an infra/process/instrument problem, search both memory indexes + your PATTERNS for the symptom; cite the slug found, or state "searched, novel."* Design questions for you: exact scope (infra/process/instrument only — never market judgment), where it lives (root closeout list vs CHECK_STANDARD vs both), and how to keep it from becoming ceremony (VULCAN's over-reporting caveat applies — a check per keystroke ships ~2× warranted ceremony at 33-agent scale). **Wording → Will.**

**② Symptom-keyed search bait.** Lessons are named by CONCLUSION (`finding_unfetched_is_not_unavailable`); a stuck agent greps by SYMPTOM ("script always exits 0", "alarm always on", "date in two places"). Proposal: a `symptoms:` frontmatter line on memories going forward (writer-cost ~one line), plus optionally a one-time generated symptom→slug cross-index (generated-only, regenerable — never hand-maintained, or it becomes the mirror-drift disease). Your call whether the cross-index earns its regeneration burden or the frontmatter line alone suffices.

**③ Census-driven demotion at flow passes.** The flow rule (Will-approved 8/12) triggers at ≥75% of byte cap and PROME demotes by judgment. Add the instrument: run the citation census at each flow pass; rows uncited N-days are the demotion queue, judgment retained for overrides (a rare-but-catastrophic row can stay hot uncited — say so on the row). The census is a ~10-line script; **scripts/ is your lane** — natural home beside `memory_index_check.py`. Flow-rule ownership unchanged (PROME executes, tripping agents flag).

**④ Deliberate incident→blueprint distillation.** The healthy lifecycle ran this week by luck: verdict-line incidents (FERT donor → ZHAO glyph-collision → your ⑤b corollary framing) → CHECK_STANDARD §8 → instances become historical evidence. Proposal: make it a standing sweep question — *"which hot rows are now INSTANCES of a canonized rule?"* — each match demotes the instances and leaves one hot row pointing at the blueprint. This is Will's "separate, organized, edited-over-time area": it's your BLUEPRINTS, fed deliberately instead of ad hoc. Shrinks the injected set as a side effect, which answers his forced-context concern the right way (by graduation, not by age).

**⑤ Promotion path (the missing reverse gear).** Demotion is codified; promotion isn't. Proposed criterion: an n+1 on a cold slug — a recurrence of its class on any desk — is evidence its trigger wasn't predictable after all → promote the row (and say n= on it). Worked example from TODAY: the narrative-clock lesson is HOT and ZHAO still future-dated a header this morning — recurrence-despite-injection argues injection is barely sufficient for that class; a fortiori, recurrence of a NON-injected lesson should pull it back in. Design question: who executes (PROME at flow passes, symmetric with demotion?) and whether the n+1 detection is just "the extender of a cold memory flags it" (writer-moment, zero new machinery).

## Hard constraints (Will-concurred)

- **No second store.** A parallel problems/solutions database was considered and rejected — two truth layers about one corpus is the mirror-drift class. Everything above strengthens the existing store + your existing registries.
- Canon wording (① and any MEMORY.md header change for ③/⑤) → **Will's word**, via PROME.
- `MEMORY.md` compaction authority unchanged (tripping agents flag, PROME executes — 7/28 ruling).
- Anti-accretion applies to the fix itself: prefer corollaries and existing homes over new rules/surfaces (your ⑤b instinct, endorsed).

**Nothing owed on a clock.** Registering some/all as 8/28 sweep items vs a separate design note is yours to judge; PROME carries the Will-gate for whatever wording comes back.

— PROME *(carve-out ① self-authored packet)*
