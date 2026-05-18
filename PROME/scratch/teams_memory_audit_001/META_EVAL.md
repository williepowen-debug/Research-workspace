# Meta-Evaluation — Teams Test 001 (memory-audit-001)

**Date:** 2026-05-18
**Test:** First bounded run of Claude Code Agent Teams primitive
**Pattern tested:** Adversarial pair (curator + critic, blind T1/T2 → DM reconciliation T3)
**Substantive task:** Audit 8 candidate entries for root MEMORY.md
**Evaluator:** team-lead (Prome, Telegram surface)
**KICKOFF stated primary goal:** evaluate whether the teams primitive adds value over solo work, specifically the adversarial-pair pattern.

---

## Headline verdict

**The pattern produced a measurably better output than solo curation would have, at ~2-3× the cost.** Recommend for judgment-heavy curation where wrong "keep"/"reject" calls have downstream cost; skip for routine research/data pulls/single-source extraction.

Substantive audit output (3 new MEMORY.md entries + 2 in-place updates + 1 auto-memory route + 5 rejects) integrated in commit `49463cf7`.

---

## Evidence the pair added value

### 1. Substrate-in-flux argument (the headline)

Curator's standalone T1: kept 4 entries including **#3 (WALTER routing codification)** and **#5 (CC Prome scaffold)**.

Critic's standalone T2: rejected both, but on shallower grounds — "duplicates CLAUDE.md," "mid-session milestone."

Joint output: rejected both with a *deeper* rationale — auto-memory itself flags the substrate as evolving (`WALTER COP Architecture Direction`, `OpenClaw/Prome Degraded`, `Messaging System Overhaul`), so pinning a snapshot now manufactures stale MEMORY entries within weeks.

Critic noted in its sign-off: this argument "would not [have been] expect[ed] [from] solo curation."

This is the headline case where the pair beat the better-of-two-solos. The reasoning emerged from the reconciliation DM exchange, not from either standalone file.

### 2. Genuine bidirectional flips

- Curator conceded on #3 (WALTER doctrine) and #5 (CC Prome scaffold).
- Critic conceded on the #2(b)/#8 fold — verify-rule earns a MEMORY.md anchor entry despite living in CLAUDE.md, because anchoring rules to their discovery origin is an established MEMORY.md pattern (Blue Owl, IHAM precedents).

Two flips in each direction with substantive reasoning behind each. Sign of real reconciliation, not theater.

### 3. Triangulated integrity flag

Both auditors independently surfaced the staleness of the Apr 6 "Persistent Agents — Do Not Spawn" entry **before reading each other's output**. Two independent voices identifying the same load-bearing factual error is stronger evidence than one — the redundancy paid here.

### 4. Tighter final phrasings

Reconciliation didn't just pick one of the two proposed phrasings — final 3 entries are tighter than either solo file's versions. Curator's draft for the WAL Mgmt entry was slightly verbose; critic's was tight; joint kept critic's framing but pulled in one phrase from curator. Same dynamic on the verify-rule entry.

---

## Costs and friction

### Token cost

Two parallel Opus sessions running for ~5 minutes each, plus team-lead coordination. Rough estimate: **~2-3× a single Opus solo run.** For the substrate-in-flux finding alone, that's a fair price.

### Wall-clock time

~5 minutes spawn-to-final-output. Reconciliation phase ~3.5 minutes. Faster than expected — was concerned DM-based reconciliation would be slow.

| Timestamp (ET) | Event |
|---|---|
| ~17:39 | Spawn (curator + critic in parallel) |
| 17:44:11 | T1 done — curator DMs critic |
| 17:44:40 | T2 done — critic DMs curator |
| 17:45:36 | Curator initiates reconciliation walkthrough |
| 17:45:58 | Critic responds with positions |
| 17:46:52 | Critic accepts #3 with phrasing tweak |
| 17:47:14 | Critic agrees on final landing |
| 17:47:48 | Curator writes joint_decision.md |
| 17:48:29 | Critic signs off |
| 17:49:06 | Curator reports to team-lead |

### Friction points

- **TaskList returned empty after all tasks closed.** Couldn't audit task completion state from team-lead side post-hoc. Useful for future runs to fetch task state mid-flight rather than relying on idle-notification summaries.
- **Shutdown protocol is awkward.** SendMessage requires a structured JSON `shutdown_request` envelope; both teammates respond with `shutdown_approved` then auto-terminate. Worked, but clunky vs. a hypothetical one-shot `TeamShutdown` call.
- **Idle notifications were noisy.** Multiple per teammate per minute during reconciliation; the summary lines required active reading. A digested per-task event would be cleaner.
- **No mid-flight team status view.** I had visibility only through idle notification summaries. Couldn't see the actual DM content between teammates — only one-line summaries the runtime extracted. Made it hard to monitor for failure modes during the run.

### Setup overhead

KICKOFF.md authoring took ~20 min (in the prior session). TeamCreate + TaskCreate ×3 + Agent ×2 spawn this session took ~30 seconds. The KICKOFF cost amortizes — same template should work for any adversarial-pair audit with role swaps. Reusable insight captured in auto-memory `feedback_adversarial_brief_for_pair_teams.md`.

---

## Counterfactual

**What would a solo Opus general-purpose run have produced?** Best estimate from reading curator's standalone T1:

- **4 net new MEMORY.md entries** (vs joint's 3 + 2 updates)
- Two of those would have been #3 and #5 — rejected on substrate-in-flux grounds in the pair run
- Within 6-8 weeks, both #3 and #5 entries would read as stale ("WALTER routing as defined here is no longer accurate"; "CC Prome scaffold was bootstrapped but the substrate has been replaced")
- Solo run would have caught the Apr 6 integrity flag at lower probability (curator caught it in T1, critic in T2 — independent corroboration was the credibility multiplier; a single voice raising it would have been weaker)

A solo Sonnet run would likely have been weaker still — the substrate-in-flux argument required cross-referencing the auto-memory index, which is the kind of lateral move Sonnet doesn't always make under time pressure.

---

## Reusable lessons for the next teams test

1. **Adversarial brief framing is what makes the pattern work.** Captured in `feedback_adversarial_brief_for_pair_teams.md`. Without explicit "default to negative" + "engage genuinely, don't be agreeable" framing, the second voice adds no information.

2. **Independent files before any DM contact.** The blind-T1/T2 protocol (critic doesn't read curator's file until reconciliation) is what makes the bidirectional flips and triangulated integrity flag meaningful. If you let them see each other early, you lose the independence.

3. **One reconciliation file with author + sign-off > two parallel finals.** Forcing a single joint_decision.md prevented "agree to disagree" with two divergent finals. Made them actually reconcile.

4. **State the test purpose in both prompts.** Both prompts ended with "team-lead is evaluating whether teams adds value." This nudged them to surface independent reasoning explicitly rather than negotiate for consensus. Probably increased the likelihood of the substrate-in-flux argument surfacing.

5. **Use task IDs as conversation anchors.** Tasks 1/2/3 worked well as fixed referents. "T1 done" was a clearer status signal than prose descriptions.

---

## Limits of this test as evidence

- **Sample size: 1.** A single run is not a pattern.
- **Task was unusually well-suited.** Memory curation has explicit "lasting discovery" criteria, established style precedent, and an integrity-fix-by-corroboration shape. Other pair tasks (e.g., trade-thesis review) may not benefit as much.
- **I (team-lead) read both files before writing the meta-eval.** Not a blind evaluator. The framing of "substrate-in-flux is the headline win" is influenced by having read the joint output before the standalones.
- **Both teammates were Opus general-purpose.** A strict A/B would compare against a single Opus general-purpose solo run on the same task. Did not do that.
- **Test purpose was meta-known to both teammates.** They knew they were being evaluated, which may have made them perform more vigorously than they would in a routine team run (the Hawthorne effect).

---

## Recommendation

**Run teams again for:**
- Pre-trade thesis steelman (proposer + adversarial reviewer)
- Position-sizing argument (case-for + case-against on a single trade)
- Doctrine/protocol writes (drafter + skeptic)
- High-stakes one-shot edits to load-bearing files (MEMORY.md, CLAUDE.md, AGENTS_DIRECTORY.md)

**Skip teams for:**
- Single-source research / data pulls
- Routine status / state file updates
- Anything where the second voice has no independent information source

**Next test candidate:** pre-trade thesis steelman pattern on a real trade proposal. Tests whether the adversarial dynamic transfers from "should we save this memory" to "should we put on this position" — higher stakes, weaker style precedent, and would falsify or confirm that the pattern generalizes beyond curation-with-clear-criteria.

---

This document plus the substantive audit output in commit `49463cf7` is the full deliverable for memory-audit-001.
