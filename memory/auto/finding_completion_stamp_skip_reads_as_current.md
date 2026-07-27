---
name: completion-stamp-skip-reads-as-current
description: "a file whose NAME promises currency (LAST_COMPLETION) that SKIPS a closeout doesn't read as stale — it reads as current and wrong; detect by mtime vs STATUS.md"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5b2505a4-12aa-4cf5-ae6e-5d3efac48b32
  modified: 2026-07-27T19:47:10.183Z
---

**CREED, 2026-07-27.** `AGENTS/CREED/LAST_COMPLETION.md` was last written **7/4** and was skipped at both the **7/20 and 7/27** closeouts. It therefore still asserted *"pending REGINALD action"* on an ask **satisfied 7/9** (`da82a095`) and *"CREED has NO own workbook"* — the second falsified by CREED's **own workbook build four hours earlier in the same session**. The stale claim then propagated CREED memo → PROME → Will before anyone checked the target artifact.

**Why:** an ordinary stale file *looks* stale — an old date, a dead pointer, something that prompts a check. **A file called `LAST_COMPLETION` / `LATEST` / `CURRENT_STATE` carries a currency promise in its filename**, so a skipped write doesn't degrade to "obviously old," it silently asserts **"this IS the most recent completed state"** and is believed at boot. **The filename suppresses the very suspicion that would catch it.** Worse than rot: it's a trust surface that fails closed-looking-open. Same drift class as [[finding_asymmetric_records_need_reconciliation]], different mechanism — that one is *record vs counterparty*, this is *record vs your own session*.

**How to apply:**
1. **Mechanical detector (one line, boot-time):** if `STATUS.md` mtime is materially newer than `LAST_COMPLETION.md` (or your agent's equivalent stamp), **a closeout was skipped** — treat every claim in the stamp as UNKNOWN, not current. Would have caught this on 7/20.
2. **Never backfill a skipped stamp silently.** Rewrite it *and say in the file that it skipped N closeouts* — the gap is itself the finding, and erasing it destroys the evidence that the surface is unreliable.
3. **Before re-raising an aged cross-agent ask, `git log` the TARGET PATH.** The requester's record of an ask is **not** evidence the ask is open — only the target artifact is. REGINALD closed the loop *in the file*; nobody closed it *in CREED's record*; three hops later it reached Will as "23 days open."
4. Generalises to any self-authored "latest / done / current" surface — see also [[finding_status_spine_staleness_under_appended_top]], [[finding_ledger_drift_behind_narrative]].
