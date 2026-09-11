---
name: finding_artifact_republish_from_a_new_session_requires_reading_the_live_version_in_chunks
description: The first republish of an existing Artifact URL in a NEW session is refused until this session has Read EVERY line of the live version; the reader caps a Read at ~25k tokens, so a 300 KB page costs ~6 chunked Reads (~130k tokens) before the publish is accepted — budget it, never `force`.
metadata:
  type: finding
symptoms: "publish to an artifact this conversation has not read or published is refused", "that version counts as viewed only once you have Read every line", "File content exceeds maximum allowed tokens (25000)", "Use offset and limit parameters", "deck republish", "Fleet-Ops republish", "Helm republish", "closeout page regeneration cost"
---

**What happens (PROME laptop session 2026-09-10, three PROME-owned pages):** `Artifact action: read` on an existing URL saves the live HTML to a tool-results file and says the version "counts as viewed only once you have Read every line of that file." A publish with `url=` before that is refused. The `Read` tool refuses any single call over ~25k tokens, and the fleet's pages are long-line HTML (the Decision Deck 296 KB / 423 lines; Fleet-Ops 105 KB; the Helm 90 KB), so a naive whole-file Read fails twice (256 KB size cap, then the token cap) before the chunking works.

**Cost measured 2026-09-10:** the deck needed 6 Reads of ≤50 KB each (~19–21k tokens per chunk) — about 130k tokens — before Version 19 was accepted; the SECOND publish in the same session (v20) needed no read at all. Fleet-Ops and the Helm each cost the same class of read at closeout (105 KB → 3 chunks, 90 KB → 2 chunks).

**Why it exists:** the gate protects a newer version published elsewhere (another session, or a page that saves itself) from being clobbered — the same reason `force` is reserved for Will's explicit word. It is a per-session, per-URL read, not a per-publish one.

**How to apply:**
1. Plan chunk boundaries by BYTES from the saved file (`awk` cumulative line lengths, cap ≈48,000 B per chunk ⇒ ≤25k tokens) and issue the Reads in one batch; a chunk over the cap is refused and re-read, costing the tokens twice.
2. Read the live version ONCE early in the session for every page you will republish at closeout (deck · Fleet-Ops · Helm), not at the moment of publish — the read does not depend on the state files.
3. Never bypass with `force` — it discards a newer version; the read gate is the check that a self-saving page (the deck's ruling store is separate; a page that republishes itself is the risk class) is not overwritten.
4. Design consequence: a Will-facing page that is regenerated every closeout pays this read every session — a page kept SMALL (the Helm's brief, not the Fleet-Ops position table) is cheaper to keep honest; raising the reader's per-call cap is not in PROME's hands.

Related: [[finding_mechanize_the_cap_not_the_ritual]] · [[finding_record_of_an_action_is_not_the_action]] (a stale page under a fresh stamp is the failure the gate and the regenerate-LAST rule both guard).
