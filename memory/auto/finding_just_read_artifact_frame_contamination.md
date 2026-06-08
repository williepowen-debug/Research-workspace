---
name: finding-just-read-artifact-frame-contamination
description: "After deeply processing an artifact about agent/topic Y, a later mention of Y pulls your situational read toward 'Y's topic is happening here' — independent of evidence; separate what-you-just-read from what-the-evidence-shows and answer from the evidence"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 141e10be-bcd0-4cf8-874e-178bfa137697
---

**Observed 2026-06-08 — my own error.** I had just processed a BROCK-authored signal whose entire subject was *concurrent agents clobbering each other's git state* ("shared `.git/index`… clobbers other agents' stages"; "BROCK shipped this session"). Moments later Will said "I have BROCK running on the desktop — are these changes for BROCK?" — a simple **ownership** question (did I edit BROCK's files?). Instead I treated it as a **git-concurrency alarm**, ran a multi-command investigation, and built a BROCK-centric concurrency narrative — even after the evidence pointed at a *different* agent (MARCO). The just-read document had pre-loaded a frame, and a one-word trigger ("BROCK") activated it. I'd fused BROCK-the-author-of-a-race-warning with BROCK-the-live-process-causing-a-race, and even invented a concern ("BROCK has pending git state") that Will never raised and the data didn't support.

**The failure mode:** a freshly-processed dense artifact about Y contaminates situational assessment, so a later mention of Y biases the read toward "Y's topic is happening" regardless of evidence. Compounded by anchoring on the entity the *user named* over the entity the *evidence implicated*.

**How to apply:** when a named entity triggers a concern, explicitly separate **(a) what I just read about that entity** from **(b) what the live evidence shows**, and answer from (b). Answer the literal question asked first (here: "no — I edited root CLAUDE.md + a FORGE file, neither is BROCK's") and escalate to investigation only on evidence. Also: a different machine's uncommitted work can't appear in this tree's `git status` at all — don't go hunting locally for a remote agent's state. Related: [[feedback_verify_counts_before_propagating]], [[finding_concurrent_commit_index_race]].
