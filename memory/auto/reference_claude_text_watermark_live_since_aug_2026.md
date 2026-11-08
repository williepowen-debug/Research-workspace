---
name: reference_claude_text_watermark_live_since_aug_2026
description: Claude text output carries an invisible statistical watermark since August 2026 (EU AI Act Art. 50); byte-level scans cannot see it; answer watermark questions from a live read of anthropic.com, never from training memory
metadata:
  type: reference
symptoms: "does Claude watermark"; "AI watermark on my document"; invisible characters check came back clean; claim that Claude does not watermark text; candidate AI guidance; detection API
---

**Fact (read live 2026-11-07 21:5x ET at anthropic.com/news/claude-text-watermark, page published 2026-08-14, updated 2026-09-01):** "Future Claude models will generate text that contains a watermark." It is a SynthID-Text-derived statistical mark in Claude's word choices, applied at the model level and globally, so every product carries it (API, Claude app, Claude Code; the Decoder 2026-08-11). No characters or tokens are added, so a scan for zero-width or odd Unicode finds nothing and proves nothing. Pre-August-2026 models are being retrofitted: Techweez 2026-11-02 reports Mythos 5, Opus 4.7, Opus 4.6 and Sonnet 4.6 added from 2026-11-03 and says Opus 5.5 already carries it; Fable 5.1 is not named by any source read but falls under "future models".

**Persistence and meaning, Anthropic's words:** "The watermark only applies to words Claude chooses." "Light editing probably won't remove the watermark completely," but "a complete rewrite where every word is replaced will." A Claude translation is fully watermarked. "A watermark can only determine that Claude was likely involved with the content at some point. It cannot distinguish 'Claude wrote this' from 'Claude heavily edited this.'" Confidence grows with passage length. Retyping the same words changes nothing (the mark is in the word choice, not the file).

**Detection:** a detection API exists in private preview for eligible organizations under EU law (regulators, media, fact-checkers, researchers, educational bodies, obligated enterprises); not public as of 2026-09-01. Anthropic itself can detect.

**Candidate AI guidance (anthropic.com/candidate-ai-guidance, last updated 2025-07-10):** "Please create your first draft yourself, then use Claude to refine it"; not allowed: Claude inventing experiences; "Be transparent." The page says nothing about watermark detection in hiring.

**Why this memory exists:** on 2026-11-07 PROME (Fable 5.1) told Will "Claude does not watermark text" from training memory and backed it with a clean invisible-character scan of his Fellows essays. Both were beside the point. Will asked for a live search and the answer reversed. A fact about the vendor's own product after the knowledge cutoff is a live-read fact.

**How to apply:** when anyone asks whether Claude output is marked or detectable, read the Anthropic page first and answer from it with its date. Never present a byte-level scan as evidence about this watermark. Related: [[finding_negative_reachability_is_a_claim_about_your_request]] · [[finding_a_limit_you_volunteer_gets_less_scrutiny_than_a_claim_you_make]].
