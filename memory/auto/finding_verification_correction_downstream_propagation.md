---
name: finding_verification_correction_downstream_propagation
description: "After a load-bearing figure-correction commit (e.g., \"fix -70% to -40%\"), audit ALL derivative sections (header, regime block, footer, session log, downstream files) for residual references. A surface-level commit can miss 30%+ of mentions. Validated BROCK 6/8."
symptoms: "the fix commit missed a spot · still says the old number · the correction did not reach · the docket/calendar still carries the old condition · an escalation was built on the corrected claim"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 3faae05c-72ff-410f-8b73-7af58951de94
---

When a load-bearing figure is corrected mid-session (typo, source-tag error, arithmetic mistake), the commit applying the correction frequently misses ~30%+ of downstream references. The corrected figure lives in many places: dashboard rows, headline summary, REGIME BLOCK, narrative sections, follow-up lists, session log narrative, footer counts, outbox files. A single targeted Edit catches the most-visible spot; the rest rot until someone audits against the source-of-truth.

**The discipline: after any verification-correction commit, run an explicit grep-and-audit of derivative sections before declaring the fix done.** Specifically:

1. List the load-bearing figures changed in the commit
2. For each, grep the file (and downstream files) for residual references — old number, old source tag, old framing
3. Check derivative-of-derivative sections explicitly: SESSION LOG narrative, footer summary lines, BOTTOM LINE / take sections often carry summaries that repeat the figure
4. If outbox signals reference the corrected figure, those are durable artifacts even if "undelivered" — audit them

**Why:** The original write put the figure in many places because it was important. The correction touches the spots the author remembered; the rest stay stale. The reader downstream cites the stale spots (because they're often the headline/summary the reader sees first), not the corrected dashboard rows. The verification-correction discipline is incomplete without the propagation audit.

**How to apply:**
- After any commit message starting with "fix" / "correct" / "verify" / "retag" on a numeric or sourced figure
- Run grep across the file + related files
- Specifically check: header / REGIME BLOCK / footer / SESSION LOG / outbox files / cross-references in MEMORY-style indexes

**Provenance — BROCK 6/8:**
- Commit `d229b2c5` "verification fixes" corrected dashboard rows for PG -17%→range, default Reuters→Fitch, issuance -70%→-40%, arithmetic 57→59
- But MISSED: header headline line (still said -17%), LESSONS #15 reframe (still said -70%), REGIME BLOCK item 5 (still said -70%), SESSION LOG narrative (still said 57)
- 4 spots stale post-"fix" commit, not caught until Prome verification round flagged "before resolving predictions against STATUS, verify the corrections actually landed"
- Required a second hygiene-pass commit (`81829e39` Phase 1B) to clean

**Pattern generalizes beyond BROCK:** any agent shipping a numeric/source correction should run this audit. Cheap (1-2 grep + visual scan), prevents downstream agents/sessions citing stale-as-fresh.

Related: [[LESSONS#18]] echo (stale copies drift) applied at intra-file scope rather than cross-file scope; [[finding_doc_mirror_consistency_check]] (canonical→mirror direction); [[feedback_verify_counts_before_propagating]] (cross-agent version of same discipline).

---
**n+~25 (2026-07-31 four-reviewer audit round) — the class measured at fleet scale, with three sharpenings:**
A Will-directed artifact audit of a six-agent evening wave found **every core result reproducible and ~25 defects of exactly ONE class**: a correct finding existing in the agent's files and failing to reach the surface a consumer (or the agent's own next boot) reads — HOMER 7 (a PRIMARY-verified leg still marked secondary on the brief its consumer reads), CARL 7+ (a Will pre-authorization that never reached the boot-read decision cells), MARCO 4+ (a retracted figure in its own boot-read MEMORY.md, edited that same session), ORACLE 4 (STATUS asserting what its own KB retracted), LABOR 3 — **and PROME itself** (HEARTBEAT published two claims from a packet whose third item it had processed 7 minutes earlier). Sharpenings the round proved:
1. **Sweep by PATTERN, never by line-list.** Three consecutive line-targeted sweeps (CARL's) each left residue; a bounded pattern-grep found every survivor in ~2s. The survivors clustered in **long narrative HEADER lines** (17K-char ROADMAP/STATUS headers) that read as prose — that is WHERE residue lives.
2. **Freshness enforcement passes a fresh file carrying a stale claim** — freshly-stamped, staleness-enforced TSVs carried a retired prediction's twice-superseded confidence. The self-sweep must match **superseded TOKENS (figures, IDs, state words)**, not vintages. Cousin of [[finding_freshness_check_cannot_catch_a_fresh_lie]].
3. **The auditor is in the class too:** one reviewer certified a sweep "clean everywhere" off a truncated grep, then repeated the failure inside its own erratum (classified a hit as history without opening it). "Consistent with read-everything AND with read-nothing" — [[finding_verification_zero_is_ambiguous]] — applies to the checker's own output.
Mechanization proposed to DAEDALUS 7/31 (design bundle item 2): a `consumer_check` SELF-mode greping the agent's own dir for superseded tokens at closeout, scope including ledgers, trackers, and handoff files.

---
**A distinct axis (SAM 2026-08-04) — when the thing you fixed is the INSTRUMENT, the stale outputs are numbers, not mentions.**

Everything above is about a *figure* correction failing to reach the figure's other *mentions*. There is a second, harder version: **you repair a TOOL, and the figures that tool already produced stay stale — and no grep for the old number will find them, because the stale artifact is a DERIVED number that was never wrong-looking.**

SAM fixed a `usdjpy.py` defect that silently truncated intraday ranges (8/2 and again 8/3, after the first repair regressed). Both fixes were correct and both were verified. **Neither was propagated into the base rate SAM had computed FROM that column the same week** — a live prediction's (SAM-39) registered rationale rested on "2/250 ≈0.8%/session → naive P ≈23%." On repaired data it was **3/259 ≈1.16% → ≈32%**, cutting the claimed edge from ~+32pp to ~+23pp. The mark itself survived; the *stated reason for it* did not. It surfaced only because the tool's own alarm kept re-reporting rows that sat outside its self-heal window.

**Three things this adds to the class:**
1. **The trigger is broader than "a commit that says fix/correct."** It includes *any* repair to a data-producing instrument — parser, fetcher, threshold detector, dedup key. Ask: **"what did I compute from this column BEFORE today?"** A grep for the old figure will not answer that; only re-running the derivation will.
2. **A detector that reports defects it cannot repair will re-report them forever.** SAM's audit swept 60 days but its repair window was 10, so pre-fix rows were flagged every run and never healed — and the standing alarm became background noise instead of a fix. **If a check surfaces a class it cannot remediate, give it a remediation hatch** (SAM added `--revise-window N`, deliberately a flag and not a default because widening it rewrites history). Cousin of [[finding_standing_guard_is_a_false_negative_risk]].
3. **The correction lands in the summary and misses the CANONICAL row.** SAM patched STATUS, CHANGELOG, MEMORY and the brief — and the `PREDICTIONS.tsv` row itself, the one artifact a resolver actually reads, still carried the superseded base rate plus a now-false "4 known disagreements remain" note. Caught only by the pattern-sweep in the n+~25 block above. **Sweep the canonical low-traffic record LAST and FIRST; it is the one nobody re-reads and the only one that binds.**

**Carry the split explicitly when it applies:** *"the number is right, the reason I gave for it was wrong."* That is a real and reportable outcome — it preserves the calibration record while correcting the rationale, and it is more honest than either silently re-marking or leaving the stale justification standing. Related: [[finding_loadbearing_number_must_be_reproducible]] (a load-bearing number must be re-derivable — this is what happens when it is re-derived and disagrees), [[finding_threshold_level_is_a_measurement_not_a_constant]].

**n=2 in a single session (SAM 2026-08-04) — the sharper form: you may not MEASURE on a dataset you have just flagged as stale.**

The morning case was the instrument axis above (fixed `usdjpy.py`, never re-derived the base rate it had fed). The afternoon case is worse, because the author had *already identified the defect*: SAM flagged `CPI.tsv` as ~6 weeks stale **and, in the same palimpsest, published a rule "measured" from it** — *"7 of 7 paired months, Tokyo core-core ≤ National, never above."* When the credential was restored and the missing rows backfilled hours later, the truth was **7 of 8**, with the exception at the **most recent** paired month — i.e. the claim was falsified at the live end, the worst place for it.

**The trap is that the staleness flag creates false confidence.** Having *noticed* the gap feels like having *handled* it; the write-up documents the defect in one sentence and asserts a measurement contaminated by it in the next. Both sentences are in the same paragraph and they contradict each other.

**Rules:**
- **A dataset you just flagged as stale is not a dataset you may measure on.** Either fix it first, or state the measurement as PROVISIONAL-pending-backfill with the specific missing rows named.
- **Naming a gap is not closing it.** If a number depends on the gap, the number inherits the gap's status regardless of how loudly the gap was flagged.
- **Re-run every derivation the moment the data lands** — do not assume a stale-window result "probably still holds." Here the direction of the error was the opposite of intuition: the missing row was the one that broke the rule.
- **Prefer same-basis comparisons and say which basis you used.** The tool's own alert compared the *latest* row of each series — different reference months — while the rule required *same-month* pairs. They agreed by coincidence; that is not corroboration.

Related: [[finding_loadbearing_number_must_be_reproducible]] · [[finding_plausible_stale_value_evades_review]] · [[finding_unversioned_local_secret_fails_silently]] (the credential that caused the staleness was orphaned by a cleanup that re-homed three sibling keys and missed the fourth).

---

**EXTENSION 2026-08-10 (WALTER, publisher-side scan) — a propagation scan that finds ONE genuine carrier is not evidence there is only one. The noise ratio is what stops the sweep.**

The rules above assume the auditor keeps looking. When the audit is an automated bare-string scan, the **noise ratio decides where they stop**, and it stops them early.

OSPREY corrected a figure it had published (Russian refining runs `3.91` → `~3.6M bpd`), ran the publisher-side `consumer_check`, and reported: *"22 candidates across the fleet and **exactly one** was a genuine same-series, same-unit carry."* The other 21 were `3.91` colliding with yen options, gas prices and an EIA spare-capacity table.

**On an independent re-scan there were TWO.** The second was `CARL`, carrying `runs 3.91Mbpd = lowest since Mar-2005` **directly beside its own ~30% refining-offline read** — same series, same unit, same superlative, and load-bearing on a number other agents cite.

**Why the miss is structural rather than careless:**
- **21 obvious false positives train the reviewer to skim**, and the genuine second hit **wears exactly the same colour** as the noise in the output.
- Finding a genuine carrier feels like *completing* the task ("found it"), when it has only *started* it. **"I found the carrier" and "I found the carriers" are different claims and the scan cannot tell them apart.**
- The false positives here were **not** low-quality matches — the EIA spare-capacity series genuinely opens `3.91 → 3.58 → 3.21`. **A bare-string scan cannot distinguish a real carry from a real number in a different series; only opening the line can.**

**Rules:**
- **Read every candidate to a verdict, or say explicitly that you did not.** "1 of 22 genuine" is only meaningful if all 22 were opened; otherwise report "1 genuine found, N unreviewed."
- **Confirming one carrier is not completing the sweep.** Do not let the first genuine hit terminate the scan.
- **A correction's blast radius is a property of the FIGURE, not of the scan's output length.** A widely-cited number should be assumed to have multiple carriers until each candidate is dispositioned.
- **Corollary for the consumer side:** a 🔴 you were never sent is indistinguishable from one that does not exist — so a downstream agent should not infer "nobody flagged me" means "I am not carrying it."

Sits with [[finding_coverage_gap_needs_all_surface_check]] (exhaustive on the wrong layer) and [[finding_silent_blank_evades_review]]. The interim `consumer_check` caveat — *a 🔴 is a CANDIDATE, not a finding* — fires in **both** directions: it over-reports collisions **and** it under-reports when the reviewer stops at the first genuine one.


---

**n+1, 2026-08-22, HOMER — the structural WHY, and the direction is NOT the invariant: corrections propagate along the EDIT PATH.**

HOMER's ATTOM wrong-referent correction (8/22) reached STATUS, PIPELINE.tsv, NEXUS_BRIEF and two outbound packets — every surface the discovering session's data-pull was already touching — and MISSED `docket/CATALYSTS.tsv` row 9, the surface its OWN BOOT reads at step 5, which kept the false verdict AND a live escalation condition built on it (one that would have fired on the publisher's normal 3-of-6 skip behavior). **A correction flows into the surfaces on the session's edit path; read-often/written-rarely surfaces are systematically OFF that path — and that is precisely the profile of the most load-bearing files: dockets, calendars, threshold tables, boot checklists.** HOMER's prior instances all ran working-files→dashboard and were written up as "the correction dies before it reaches the dashboard"; this one ran the OTHER way (dashboard-class surfaces got it, the docket didn't). **The invariant is the edit-path boundary, not the direction.** Corollary: **fixing the FACT does not fix the MACHINERY downstream of the fact** — grep for conditions/escalations/gates KEYED to the corrected claim, not only restatements of it.

*(Caught via quote-back — PROME restating the finding to its owner. Batch-A promotion note: COLD-row extension, flag executed inline by PROME; this slug already sits on the mid-Sept promotion re-look and this instance strengthens it, n+1.)*
