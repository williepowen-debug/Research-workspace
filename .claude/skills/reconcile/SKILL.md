---
name: reconcile
description: PROME's FORGE position-mirror reconcile — run when Will posts broker screenshots or an activity ledger. Transcribe → verify to the cent → derive deltas FROM THE MIRROR → spawn ANVIL → verify at the artifact → Will's word → ANVIL commits. Use for "here are my Fidelity/Robinhood screenshots", "reconcile FORGE", "new broker export".
user-invocable: true
---

# /reconcile — FORGE position-mirror reconcile (PROME-owned; ANVIL is the clerk)

Canon: root `CLAUDE.md` position-truth paragraph (FORGE = stale mirror, PROME owner) · `.claude/agents/anvil.md` (the clerk's contract) · `FORGE/STATUS.md` footer (PARSED BY — the file is an interface).

## Steps (in order — each one has cost you a real error when skipped)
1. **Transcribe** every visible cell to `PROME/data/<YYYY-MM-DD>_broker-capture-TRANSCRIPTION.md`: account id, as-of (which session's close — "Today's gain/loss" populated ⇒ that session), cash, pending, every row (symbol · expiry · qty · last · today $ · total G/L $ and % · value · avg cost · basis). Robinhood cards hide qty/mark — derive cost from P/L ÷ P/L% and LABEL it derived.
2. **Verify to the cent** before anything else: Σ positions + cash + pending = account total; per row value = last × qty × (100 if option). If it doesn't sum, the transcription is wrong — fix it, don't proceed.
3. **Derive deltas from the mirror, never from a view.** `git show HEAD:FORGE/STATUS.md` is the comparison base. ⛔ SCRATCH's operator-card book line and HEARTBEAT §Book are compressed VIEWS — on 8/29 PROME called five long-held positions "new" off SCRATCH's line and ANVIL had to refuse the packet (D-34). Write "NEW / QTY CHANGE / GONE / MARK ONLY" per row from the diff.
4. **Spawn `anvil`** (Tier 1 — standing instrument, per capture) with the contract: **(a)** transcription path + stamp, **(b)** post-snapshot events (label PROME-supplied vs broker-verified), **(c)** the task list: reconcile · rebuild `§ Reconcile discrepancies` urgency-ranked expiring-first · consumer verdict · `git diff --stat FORGE/` · "awaiting commit authorization" · NO COMMIT. Tell it SendMessage may be unavailable to subagents in this harness — write the report to `PROME/inbox/` AND make it the final text (the idle notification carries final text).
5. **Activity ledger** (Fidelity Activity & Orders, past 30 days) — ask Will for it if not supplied; it is what closes cash/pending/entry-date unknowns. Append as §③ to the transcription, then `SendMessage` ANVIL a round-2 with the specific D-rows it resolves. ANVIL verifies the arithmetic itself; it writes from the ledger, not from PROME's read.
6. **Verify at the artifact** when ANVIL reports: `git status --short` (only `FORGE/STATUS.md` modified), `python3 AGENTS/TERRY/scripts/positions_from_forge.py --selftest` rc=0, spot-check 3 rows against the transcription, byte size vs 32,550 (the PostToolUse hook already warns). Read the discrepancy list; separate "Will decides" from "owner decides".
7. **To Will:** ⚖️ blocks carry WQ row numbers (register first). Expiring items first. Then the commit ask.
8. **On Will's word:** ANVIL commits via `python3 PROME/tools/commit_check.py commit -F <msg> -- FORGE/STATUS.md` (or PROME commits for it if the clerk is gone — say so in the message). Commit the transcription file + the inbox report under `PROME/`.
9. **Close the loop:** WQ rows executed by the ledger → RECENTLY DONE with the fill date/price · SCRATCH operator-card book line rewritten FROM THE MIRROR · FORGE/STATUS.md byte cap → hot/cold split if over · anvil.md "Known state at last edit" block updated (vintage, open D-rows, run hash).
