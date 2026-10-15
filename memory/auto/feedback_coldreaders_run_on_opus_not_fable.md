---
name: feedback_coldreaders_run_on_opus_not_fable
description: Will's standing instruction (n=3; 9/2, 9/17, NARROWED 10/15) — never Fable for a subagent; desks, counterexample-devising repair readers, ARGUS and other difficult jobs on Opus (pass model: "opus" on each general-purpose call, it inherits the parent's model); single-artifact cold reads (the coldreader agent) on SONNET since 2026-10-15 (WQ-447 A).
metadata:
  type: feedback
symptoms: "cold reader spawned as fable", "coldreader model", "which model for subagents", "Fable limit killed a subagent", "spawning these all as FABLE", "burn up our tokens", "spawn your subagents as OPUS"
---

**Will, 2026-09-02 13:09 ET, verbatim:** *"we definitely need you to spawn cold readers as OPUS and not FABLE."*

**Why:** Fable is the scarce, rate-limited tier (an 8/31 Fable usage limit killed a subagent mid-closeout); a blind cold read is a mechanical verification job that Opus does fully, and running ten of them on Fable in one afternoon (the 9/2 HEARTBEAT split) burned the budget the operator needs for the coordinator itself.

**How to apply:** the `coldreader` agent definition (`.claude/agents/coldreader.md` + the PROME copy, parity-gated) carries `model: opus` since 9/2 — spawning by `subagent_type: coldreader` inherits it. For any other verification-class spawn (cold reads, executing strangers, census readers) pass `model: "opus"` explicitly. Do not default a subagent to the parent's model when the task is verification rather than judgment. Related: [[feedback_front_load_planning]].

**Will, 2026-09-17 08:52–08:53 ET, verbatim (second instance — the rule GENERALIZES):** *"hey you are spawning these all as FABLE? You are going to burn up our tokens"* · *"You need to spawn your sugagents as OPUS please."*

**What happened:** on the 9/17 post-crash boot PROME spawned NINE domain-desk sessions (HAWK · BOND · VIOLET · LABOR · DAEDALUS · MARCO · ZHAO · BRENT · CARL) as `subagent_type: general-purpose` with NO `model` override — `general-purpose` has no model pin, so every one inherited the parent's model (Fable). Only the `coldreader` spawns ran on Opus, because that agent definition pins it. The 9/2 memory's own "How to apply" said *"do not default a subagent to the parent's model when the task is verification rather than judgment"* — which read as permission to run judgment desks on Fable. That reading is dead.

**Rule as it now stands (narrowed 2026-10-15, WQ-447 A):** every `Agent` call for a desk, a counterexample-devising repair reader, ANVIL or ARGUS passes `model: "opus"` (general-purpose inherits the parent's model, so the line is explicit on every call); a `coldreader` spawn runs on Sonnet through its agent file; Fable is never a subagent model. *(The 9/17 form of this sentence — every call opus — is superseded; its text lives in this file's git history.)*

**Mechanized 2026-09-17 ~09:4x ET (Will: "Yes to both, go ahead"):** `.claude/agents/desk.md` (+ PROME parity copy) pins `model: opus` for every domain-desk spawn and carries the COMPLETION_SPEC boot preamble — spawn desks with `subagent_type: desk`, never `general-purpose`. Same sitting: `coldreader.md` now writes its full ledger to a spawner-named scratchpad file and messages only score + ❌ + path (four truncated reports that morning).

- **n=3 (2026-10-15, PROME prome-81):** the `anvil` agent definition carried no `model:` line, so the 10/15 broker reconcile ran on Fable (ANVIL self-reported); the desk/coldreader/argus definitions already pinned Opus. Fixed the same session by adding `model: opus` to `.claude/agents/anvil.md` + the PROME copy (acbaa509a). Rule: EVERY agent definition under `.claude/agents/` carries an explicit `model:` line (`opus` for desk, anvil, argus; `sonnet` for coldreader since 2026-10-15, WQ-447 A); a spawn through a definition without it inherits the parent (Fable) silently.

**Will, 2026-10-15 17:37–17:39 ET, verbatim (WQ-447, RULED A at registration):** *"PROME, going forward lets use lower models for spawns that are only readers. Does that make sense?"* → *"okay lets keep that as preference moving forward. Keep the high OPUS for desks and difficult jobs. But for simply readers like many of these I think sonnet would work?"*

**How to apply (10/15):** the 9/2 and 9/17 words are NARROWED, not reversed — Fable is still never a subagent model. Three classes: (1) desks (`desk` agent) and ARGUS stay `model: opus`; (2) a reader that must DEVISE COUNTEREXAMPLES to break a repair (the general-purpose repair readers of WQ-229) stays Opus — on 10/15 two such reads caught five real defects the author's own 10–16 tests never saw; (3) a single-artifact cold read (`coldreader`: enumerate every claim, test every pointer, flag contradictions) runs on Sonnet — the agent file carries `model: sonnet` (root + PROME copies). When a reader's job is unclear, the test is the verb: *enumerate and check* = Sonnet; *invent what the author missed* = Opus. Encoded 2026-10-15 (prome-06): `.claude/agents/coldreader.md` both copies · `USER.md` § Autonomy and Roles · this file.
