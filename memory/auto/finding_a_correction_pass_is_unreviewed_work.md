---
name: finding_a_correction_pass_is_unreviewed_work
description: "Fix passes carry a HIGHER defect rate than the original work — they feel finished because the thing they fixed is gone. Sweep the correction like any other change, and never let a sweep be the last thing that touches a file."
metadata:
  node_type: memory
  type: feedback
symptoms: "finding born inside a retraction; correction carried a second wrong number; shipped the fix without testing it; validation ran only because it was going to the operator; retraction with passengers; fixed the flagged label and shipped the stale number beside it; same row wrong on three consecutive passes; the flagger only looked at one cell; corrected row read as reviewed row"
---

**The work you do to correct an error is the least-reviewed work in the session, and it is where the next error lands.**

A correction feels finished in a way ordinary work does not: the defect that prompted it is visibly gone, the diff is small and targeted, and the act of fixing carries its own sense of completion. That feeling is the hazard. **A fix pass is new, unreviewed work and needs the same sweep as anything else.**

**Measured case (MARCO, 2026-08-21).** Three review sweeps ran over one long session. Each found defects, and the defects were **concentrated in what the previous sweep had just "fixed"** — not in the original work.

- **Sweep 1** caught a real published error: a NV Gaming tax figure called a "partial-vs-full-month artifact" and refused, when the same convention governed both sides of the comparison.
- **Sweep 2** — over the corrections themselves — found *four* problems in work shipped within the hour:
  - **The withdrawn error was re-committed on different data forty minutes later.** A new H-2A base rate compared FY-through-Q3 against two FULL prior years — the identical partial-vs-full shape just retracted. *(Re-run on a matched perimeter the conclusion survived, but the headline multiple was overstated: 2.78×, not 2.95×.)*
  - **Fixing untrippable thresholds produced untrippable thresholds.** Bands re-spec'd to remove ambiguity came back with **touching boundaries** (a value in two bands at once), one band a **strict subset** of another, and a **gap** where a value fell in no band at all — untrippability reintroduced at the opposite end of the scale from the one just closed.
  - **A correlation was asserted without being computed.** A five-month *sign pattern* was called "anti-correlated" and used to cut a prediction's confidence. Measured over 48 months, every pair was **positively** correlated (+0.33 to +0.76) — and positive co-movement made the predicted event **more** likely, so the adjustment **pointed the wrong way**.
- A separate strand the same day: a helper written **to stop one silent-corruption class** introduced another (a non-CSV-aware split that doubled quotes on every read/write, compounding 12 → 3,574 across four commits).

**Why fix passes are more dangerous, not less:**

1. **Pattern-matching is running hot.** You have just named a failure mode, so the pattern fires readily — including on cases where it does not apply. **A good failure-mode library makes false-positive corrections cheaper to reach.**
2. **The checks that would catch it are the ones you just ran and passed.** Structural checks (row counts, field counts, schema, boot) verify *shape*; correction errors live in *meaning* — a real figure called fake, a trend read as a level, a claim asserted rather than computed.
3. **Nothing prompts a re-read.** The original work gets reviewed because it is new. The fix gets filed because it is *done*.

## How to apply

1. **Sweep the correction like any other change.** If a fix touched a file, that file is unreviewed again.
2. **Apply the same evidentiary standard to a WITHDRAWAL as to an adoption.** Retracting a number is a claim; test it before publishing it ([[finding_asymmetric_rigor_counterparty_claims]] — *verify the number that makes you RETRACT*).
3. **When you re-spec any banded threshold, enumerate the whole line** and prove the branches are **disjoint AND exhaustive** — half-open intervals, boundary values assigned to exactly one band ([[finding_prereg_verdict_boundary_must_be_a_number]] · [[finding_overlapping_prereg_branches_restore_grader_discretion]]).
4. **Before adjusting a confidence on a stated relationship, compute the relationship.** A sign pattern over a handful of periods is not a correlation, and getting its *direction* wrong is worse than having no estimate.
5. **Re-run the failure mode you just wrote up against the work you did while writing it up.** In this session that check would have caught the repeat within minutes.
6. **Never let a sweep be the last thing that touches a file** — and when the sweeps stop finding *new classes* and start re-finding your own corrections, **hand it to a different reader** rather than running a fourth pass yourself. The effect above applies to your own re-reads too.

---

**🔴 EXTENDED 2026-08-23 (WALTER) — THE SAME RULE COVERS THE *VERIFICATION* PASS, AND THERE IT HAS A TIE-BREAKER.**

**A query written on the spot to answer a challenge is the least-reviewed instrument in the room.** It is minutes old, has never been run against a known-good case, and — the part that matters — it was written **under the specific pressure of wanting an answer**. That is the same "feels finished" trap as a correction pass, with an extra hazard: **its output arrives already framed as the check on something else**, so it is read as a verdict rather than as new, untested code.

⇒ **TIE-BREAKER: when a scratch query disagrees with a production instrument, the SCRATCH QUERY is the more likely defect.** The production instrument has run hundreds of times against real data; yours has run once. **Debug your own query to the point of proving it right before you report the production number as wrong** — and if you have already reported it, say so plainly rather than letting the correction ride.

**Instance.** Challenged on a backlog figure (*"are you sure these have not been consumed?"*), WALTER wrote an ad-hoc query and got 122 items / 24 ACTION against the production checker's 124 / 22. It then presented one row as proof the checker was over-counting — *"20 days unconsumed, actually consumed in 90 minutes."* **The fact about that row was true and the criticism was false:** the query tested whether the *recorded* handoff path EXISTS, and for a consumed item that path already points into `processed/`. **The checker had excluded the row correctly all along; the scratch query counted filed items as unfiled.** The real finding was one level down and survived: the underlying number is a PROXY (*"nobody moved a file"*), which a second independent instrument then split into 92 corroborated and 32 untestable.

🔑 **And the generalisable half: a challenge to a number is not the same as the number being wrong.** Both survive the check often enough that the honest output is usually *"here is how strong the evidence actually is,"* not a revised figure. **State the evidence tier; do not manufacture a correction to look responsive.** `[[finding_verification_zero_is_ambiguous]]` · `[[finding_delivery_check_is_not_a_knowledge_check]]`

---

**🔴 EXTENDED 2026-08-27 (LIQUID instance, PROME-routed) — A CORRECTION IS ALSO A DELIVERY VEHICLE: A NEW CLAIM BORN INSIDE ONE SHIPS WITH THE CORRECTION'S AUTHORITY AND NONE OF ITS VALIDATION.**

A retraction is the highest-authority document class a desk produces — it is proof the author self-checks — so a **new** analytical claim riding inside one travels with maximum credibility and minimum review. It reads as *output of* rigor when it is actually *input to* it.

**Instance:** LIQUID retracted a base rate at ~15:00 (self-truncated window) — and the retraction itself carried a fresh decomposition ("~9bp distribution rise + ~6bp dispersion widening") that had received none of the validation the original failed. The eye-catching half was a ZIRP-exit level artifact (the wedge made ONE move, 2022→2023, flat four years since). **The 90-second test that killed it ran only because PROME said the number was going to Will** — validation triggered on DESTINATION, not on CLAIM CLASS. The surviving half (repo distribution grinding from ~10bp to ~1bp below the IORB ceiling since 2023 *while IORB fell* — cushion consumed) was stronger than the first framing. Same day, same shape at two other desks: CREED's wiring fix manufactured a false 🔴 on its first run ("the thing needing the test was the FIX"); HENRY's correction to its own HY flag needed a same-hour second correction. PROME relayed v2 to Will minutes before v3 existed.

**How to apply (extends rules 1–2 above):**
7. **A finding born inside a correction gets the same *name-the-one-alternative-and-run-it* pass as an original, before it leaves the desk.** The trigger is the CLASS (correction-born), never the destination.
8. **Separate the kill from the replacement.** A retraction travels instantly and bare — dead number, cause, holders. Any NEW claim ships separately or tagged UNVALIDATED. Never slow a retraction; never let it carry passengers.
9. **Synthesis layers: a correction-born finding with no clock and no threshold waits one settling beat** (owner's push-confirm) before operator-facing relay; early relays carry their vintage on their face.

`[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]` (same-day sibling: the doc-only condition executed while the live instance sat open — both are "the second version inherits the first version's earned trust").

---

**🔴 EXTENDED 2026-08-27 later (LIQUID, Gate C live window) — FIXING WHAT THE RECEIPT NAMES IS NOT THE SAME AS RE-RUNNING THE JUDGE. A REJECTION IS NOT AN EXHAUSTIVE DEFECT LIST.**

The extensions above are about the *fix* being unreviewed. This one is about the **error report** being incomplete — a different failure with the same consequence, and it is invisible because the report looks authoritative and specific.

**Most validators fail fast.** They report the first defect per item and `continue`, and many short-circuit entirely (`if findings: return findings`) before later, deeper checks ever run. So the reported code is **the first defect, not the defect set** — and a desk that fixes exactly what the receipt names ships again into the same refusal, having consumed a second attempt to learn something the first attempt could have told it.

**Instance.** A Kernel submission was refused `NATIVE_BLOB_MISMATCH` (a hash computed without a trailing newline the tool's selector includes). The custodian's fix instruction — *recompute the hash, ~10 minutes* — was correct about the reported defect and **under-scoped**. Patching only the hash and re-running the real verifier locally returned **15 further errors** (`NATIVE_RECORD_MISMATCH`, one per required material field): the citation used a TSV row whose keys are column names, while the verifier maps required fields against the *keys* of cited records, so none could ever match. **The blob mismatch had masked all fifteen** — it `continue`d, and the function returned before the material-field loop ran. Shipping the named fix would have burned a second submission inside a time-boxed window on an append-only ledger. *(Both the custodian and the submitting desk reasoned past the same requirement independently; that is what turned "a desk made a mistake" into "the runbook is missing a sentence.")*

**How to apply (extends rules 1–2 and 7–9 above):**
10. **After any fix, re-run the actual validator locally — do not infer success from having addressed the reported code.** If the judge is runnable, run it; the cost is seconds and the alternative is spending a scarce attempt to discover defect #2.
11. **Treat a relayed diagnosis as a lower bound on the defect set,** however precise and however senior the source. Reproduce it (it may be right, and verifying costs nothing), then keep looking — being right about defect #1 is no evidence there is no defect #2.
12. **When a fix instruction arrives with a time estimate, the estimate encodes someone's model of the defect.** If your own check contradicts it, say so *before* the deadline rather than missing it — an honest "this is 25 minutes, not 10, and here is why" lets the operator re-plan; silence converts their estimate into their surprise.
13. **Suspect fail-fast whenever a validator reports exactly one error.** Read whether it `continue`s or returns early; if it does, the count is a floor, not a total.

---

## EXTENSION 2026-08-28 — the INPUT-SCOPE facet (RED, 8/27; encoded at the DAEDALUS wiring sweep — RED asked for an extension, not a new slug, so the fleet keeps one grep target for "corrections are dangerous")

Everything above points at the OUTPUT of a correction — your own fix is unreviewed, sweep it. **This facet points at the INPUT: an inbound correction names ONE defect, and that is evidence the surface was not being maintained — a claim about the whole row, not the flagged token.** The flagger's scope is structurally narrow and that is nobody's fault (MIDAS flagged a label because MIDAS owns a colliding metric; BOND flagged an era because BOND reads era claims); the receiving desk supplies the width. **You can execute every rule above flawlessly and still ship this one**, because sweeping your own correction re-reads the token you were told about, and nothing in that loop sends you to the number beside it. And the corrected row now reads as a REVIEWED row, so everything else on it has been implicitly certified by the fix commit.

**Evidence (RED `KB-RED-067`, DFII10 inside one row):** fire 1 (8/12) — MIDAS flagged a dead LABEL; the LEVEL beside it was stale (2.37-2.39 vs 2.43), found by luck. Fire 2 (8/27) — BOND flagged a wrong ERA; the rule said look, and found **two more defects not in the flag** (the 2026 peak was 2.47 not 2.43; the level was stale AGAIN, 2.32 live). **Same claim wrong on three consecutive passes; each pass corrected what it was told about and shipped what it wasn't.** n=2 fires, 3 defects beyond the flags, 0 false positives.

**The check (one step, free):** on applying any inbound correction — (1) fix the flagged item; (2) identify every OTHER dated quantity on the same row; (3) re-pull each from its PRIMARY — not "does it look right", pull it; (4) **log any stale one as a SEPARATE defect with its own provenance** — never fold it into the flagger's record, or the flagger gets credit for a catch they did not make and the desk's own miss disappears (`finding_summary_section_merges_what_the_body_separates`); (5) correct ACTIVE surfaces, MARK dated-historical ones superseded and leave them readable. Step 4 is the one a desk skips and the one that makes the class visible. Fleet encode proposed as C3 in `AGENTS/DAEDALUS/design/2026-08-28_CORRECTION_CLASS_VALIDATION_PROPOSAL.md` (Will-gated).

**EXTENSION 2026-08-28 (n+1 — the correction ESCALATED the claim; DAEDALUS self-instance, WAL caught it):** a next-step pass told WAL three packets were "unread 5d/10d"; the correction said "re-verified against your actual tree — 15–21d, worse"; the truth was neither — all three sat in `processed/` and their rulings had been EXECUTED eight days earlier. The correction re-ran the SAME defective read (two `ls` commands, root then `processed/`, outputs concatenated and read as one listing) and shipped with verification language attached, which is what stops the next reader from checking. Rule that survives: a correction must be derived from a DIFFERENT read than the one that produced the error — label every listing, one directory per command, and quote the listing rather than the conclusion; and never write "verified" on a re-derivation. Fleet-risk corollary (WAL): a desk that BELIEVES "you have N unread packets" may re-process an executed ruling — for a weight move, double-applying is not a no-op; check `git log --name-status` on `processed/` after any such pass.


**EXTENSION 2026-08-29 (n+2 — PROME self-instance, two fires in one night, both caught by an outside reader):** (a) a FORGE split was measured (`wc -c`-equivalent, correct unit) and THEN the file got one more edit inside the same commit — the commit message shipped the pre-edit figure; the reviewer's number was right and its diagnosis ("counted characters") wrong, so the fix was to the MOMENT of measurement, not the unit. (b) a fix pass on BOOT.md wrote "hooks to canon" into the header while 11/14 hooks exceeded the canon it named — the claim was authored in the pass that was supposed to be the review. Rule that survives: **the last write before a commit invalidates every figure printed before it — measure AFTER the final edit, at the artifact, and a header claim about a measurement needs that measurement in hand.** A reviewer's correct number does not validate their mechanism; verify the two separately (`finding_exact_level_authenticates_a_wrong_direction`).
