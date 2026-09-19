# PROME readiness to close — targeted assessment

**Assignment:** Will asks whether PROME has made the necessary updates before closing its session. **Code snapshot:** `7cc6bc5b3175bffc157387750661e0138d80ea5b`. Reviewed ANVIL's pending FORGE diff and inbox report, the September 16 capture-reading report, TERRY's receipt/card/parser, the latest parser changes, and PROME's closeout rules. No PROME operational boot/closeout, owner edits, sends, trade actions or deployments performed. Concurrent work preserved.

**Decision:** not verified complete. A bounded **PARTIAL closeout** can preserve the work without forcing another broad late-session repair pass, but PROME must first settle custody/approval of the pending ANVIL edit, record the precise unresolved repairs and dependencies on its resume path, account for both spawns, and execute/report its applicable closeout checks. “Two fixes verified, everything necessary updated” is not supported.

Earlier repair confirmed narrowly: L441 and L444 now lead with PENDING and the canonical state parser recognizes both. This verifies restoration of the two obligations CATO identified, not the full coverage of PROME's newly added buried-state guard.

[Pinned code probes](2026-09-19_1306_prome-closeout-readiness-probe.py) · [results](2026-09-19_1306_prome-closeout-readiness-probe.txt) · [test receipts](2026-09-19_1306_prome-closeout-readiness-checks.txt).

## HIGH — impossible-date handling improved diagnostics but weakens the gate result

**Source:** `PROME/tools/prome_gate.py:631–651,691–698`; `guard():296`, `aggregate_rc():242`.

In a temporary queue containing an impossible February 30 date plus a valid due-today sibling:

| Revision | What the isolated production check records | Aggregate result |
|---|---|---|
| Before `7cc6bc5b3` | ERROR, DID NOT RUN, subject UNKNOWN | **rc=2, INCOMPLETE** |
| After `7cc6bc5b3` | Named IMPOSSIBLE DATE and DUE TODAY problems, recorded at **ADVISE** | **rc=0** |

The new per-row handling usefully preserves sibling diagnostics. But the enclosing check is advisory, not blocking. Catching the exception downgrades unevaluable input from the production ERROR path to advisory-only output. PROME's claim that the old gate silently passed is wrong: `last_problems == []` was not the gate's result; the guard and aggregate already reported INCOMPLETE. Conversely, “now fails closed” is not true of the repaired return-code behavior. Other unrelated checks might block a complete run; they do not restore this check's guarantee.

**Needed:** preserve explicit incomplete/failure handling for invalid input while continuing to enumerate other rows. Do not silently promote every ordinary queue advisory; isolate malformed-input semantics. Add an assertion on the production aggregate result, not only the presence of words in `last_problems`.

## HIGH — the new Deck refusal still permits “Nothing owed” over a supported ID

**Source:** `PROME/tools/decision_deck.py:801–816`; supported ID parser at `parse_open():190`.

The new refusal counts source rows with `^\|\s*\d+\s*\|`. The real parser accepts lettered IDs such as **32b**. With one live dated 32b ask and a widened eight-column header, `parse_open()` returns no rows and the new detector also sees no rows: **the build succeeds and writes “Nothing owed.”** The identical malformed table with numeric ID 1 correctly refuses before writing. A normal seven-column table with 32b correctly renders the ask. All outputs in this probe went to a temporary directory, not PROME artifacts.

**Needed:** carry parse validity/failures into the build's decision to publish; do not reconstruct row existence with a narrower second regex. Retain the legitimate empty-queue case. This is an additional counterexample to F2's claimed closure, not the already-admitted F3/F4 residue.

CATO authored the earlier Owed/reference split. This assessment independently tests PROME's new refusal guard; it does not claim independent certification of CATO's older implementation or the entire Deck.

## ANVIL's receipt mirror is useful, but needs a narrower completion claim

The pending diff is **30 additions / 5 deletions**. It records the receipted VLO share without inventing its account or fill time, adds the TLT closed-card cross-reference, and registers D-55 through D-58. The fill agrees with TERRY's packet; its card explicitly says no exit rule has been created for the held share. These useful bookkeeping changes do not require inventing missing transactions or recalculating the whole portfolio.

Before calling the candidate ready:

- **Correct the contradiction language.** The September 16 report records a visual read of screenshots without displayed capture timestamps. It supports a conflict with the September 10 snapshot, not proof the September 10 values were wrong on their own date. HEARTBEAT actually labels its holdings “mirror, 9/10 CLOSE … STALE between exports.” Say the mirror is stale/contradicted as a current holdings source and flag the later observation. The list has **five Fidelity fields plus one Robinhood total**, not “six Fidelity cells and the Robinhood account.” No original screenshot was independently re-read in this assessment; the secondary transcription is not a current broker verification.
- **Do not create false timing precision.** The packet says the receipt was pasted at 12:33; TERRY's card heading says 12:34. Both agree actual fill time is UNKNOWN. The new row's “at-or-before 12:33” bound is unnecessary and not independently settled by those inconsistent records.
- **Keep the dashboard omission explicit to its consumer.** Re-running TERRY's parser yields **13 live / 15 withheld / 0 warnings; no VLO anywhere in the JSON**. Its selftest passes. Calling a missing real position “fail-safe in direction” is not justified; the dashboard must not imply complete coverage. The report's promised TERRY ask was not found as a delivered inbox artifact during this check. PROME should route/record the known omission and owner follow-up before declaring delivery complete; ANVIL correctly avoided editing another owner’s parser.
- **The read-cap breach is real and newly enlarged.** FORGE is **43,544 bytes**, **10,994 above 32,550**; before this edit it was 31,656. Only 894 bytes of headroom does not justify adding nearly 12 KB of repeated narrative to a whole-read surface. Keep a concise receipt/warning in the live file and detailed evidence at its report/archive home, or obtain an explicit bounded disposition for the breach. A full broker reconciliation can await evidence; compacting today's prose need not depend on receiving it. No rotation or rewrite performed here.

**Review fingerprint of uncommitted FORGE bytes:** SHA256 `f3a40592fcd31d23437029ccf954d9e67580c20b4a64004cd96afa9677e14f1a`. Later edits require rechecking the candidate.

**Approval source:** [ANVIL's local instructions](../../../.claude/agents/anvil.md), rule 9, explicitly say “DO NOT COMMIT without explicit authorization” and describe “PROME verifies at the artifact → Will approves → you get the commit go.” Thus its pending authorization is a real workflow condition. This assessment recommends preserving the receipt mirror after the corrections above; it is not Will's commit approval. It does not require a trade decision to record the existing fill.

## What must be preserved at closeout

1. **Code disposition:** F1/F2 implemented and author-tested, with the remaining counterexamples above; F3/F4 unresolved; B8 acceptance-contract inconsistency still owed. The existing L423 row still describes the prior review and does not carry the fourth reader's new findings. Update that carrier/resume point and preserve the reader's evidence, rather than relying on a commit body and the current conversation.
2. **Mirror disposition:** pending approval/commit state, D-55…D-58, unknown account/time, required broker Activity/full-capture evidence, dashboard limitation and cap treatment. Update HEARTBEAT's consumer warning so the newly found contradiction travels beyond FORGE. No need to infer current quantities to do that.
3. **Session completion:** ask both spawns to close out and record their answers or dark status under WQ-249. Review the final candidate at the required tier, report actual gate rc, verify exact-path commits and obtain a fresh-fetch push receipt. Dirty renders must be included/dispositioned; a local rebuild does not prove hosted publication. Outstanding publication/read-cap/audit work must remain named, with any skipped control reported under the standing PARTIAL rule. Do not claim a gate PASS while a required check is incomplete.

The current queue-parser selftest and willq selftest pass, as does TERRY's parser selftest; these do not cover the independent counterexamples. This assessment did not rerun the entire PROME gate, the cadence-build independent review, a spine audit or a hosted publication check. All remain outside CATO's assigned execution scope.

**Suggested next instruction to PROME:** preserve the narrow receipt corrections, accurate pending dispositions and source evidence; finish the applicable closeout procedure and return a PARTIAL receipt with the next session's first action. Do not broaden tonight's repair effort merely to obtain a “complete” label. CATO's review is complete; no owner repair started. Next CATO session: orient and await Will, or verify a final closeout receipt if specifically assigned.
