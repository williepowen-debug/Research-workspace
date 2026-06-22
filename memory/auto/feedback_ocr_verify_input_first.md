---
name: ocr-screenshot-input-verify-first
description: "When troubleshooting a wire-up problem and one input came from a screenshot/image/paste (a chat_id, token, ID, path), verify THAT input via API/disk before generating any theories — a 1-char OCR error makes every downstream theory wrong"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7aee04c6-52d3-4a8e-b656-d397335949ad
---

When debugging a wire-up / connectivity / config problem where one of the inputs was read off a screenshot, image, or copy-paste (a chat_id, API token, account ID, file path, hash), **verify that input against ground truth — query it via API or read it from disk — BEFORE generating any theories about the failure.** If a value can be fetched (`getChat(chat_id)`, an API echo, a file read), prefer that over trusting your transcription of the image.

**Why:** Mid-troubleshoot of why WALTER's bot wasn't receiving group-chat messages (2026-06-17), I ran through 4 theories (mentionPatterns missing, bot-not-member, supergroup-upgrade-on-admin-promotion, BotFather privacy mode) before catching my OWN bug: I had OCR'd a chat_id from a getidsbot screenshot as `-5179082433` when the actual value was `-5170082433` (one digit off). Will: "I feel like you are just throwing things at the wall." He was right — every theory was downstream of the first un-verified premise. Cost: ~4 messages of wasted diagnosis + a light credibility hit. A single `getChat(chat_id)` first would have caught the 1-digit mismatch in turn one. Same lesson family as [[feedback_verify_counts_before_propagating]], specialized to OCR'd/pasted inputs.

**How to apply:**
1. Before theorizing about a wire-up failure, list which inputs came from a screenshot/image/paste vs which were queried/read.
2. For each transcribed input, verify it at the source — API echo (`getChat`, `whoami`, a status endpoint) or a disk read — before building a single hypothesis on top of it.
3. Treat "the value I typed from the image" as unverified until confirmed; a 1-char error in an ID/token/path produces failures that look exactly like config/permission bugs and send you down the wrong path.
4. Prefer machine-readable provenance over human OCR whenever the value is queryable.
