# CHECKLIST Phase 2.8 and 2.8b, verbatim BEFORE v0.53 (2026-10-22)

Source: `git show HEAD:AGENTS/WALTER/design/SIGNAL_PROCESSING_CHECKLIST.md` at 453e34d13, sections PHASE 2.8 through the end of PHASE 2.8b. Superseded by v0.53 (Will, 2026-10-22: standing commission authority, told after; cap 3 per sitting / 5 queued). Kept for provenance only; not live.

## PHASE 2.8: DEEP-RESEARCH CANDIDATE SCAN (Full WALTER only)

Added v0.18 (Will sign-off 2026-06-19). Runs at dispatch-batch shaping, AFTER Phase 2.7 composite-bifurcation tagging and BEFORE Phase 3 OUTPUT writes. A triage flag with **no research-execution load** — surfaces signals worth a deeper `/deep-research` pass; **Will decides every time, WALTER never runs it.** Canonical: `design/DEEP_RESEARCH_FLAG_PROPOSAL.md`.

For each surviving signal, check the trigger set **AND** the gate (the gate is the noise-suppressant — without it the triggers describe the median signal here and the flag fires 3-5×/day):

**Triggers (any one):**
- **T1 new-coverage-channel** — opens a signal lane / sub-domain the network doesn't yet track (FL bankruptcy-filings → CORAL). Highest value — what the system structurally can't see on its own.
- **T2 new-cross-channel-interaction** — reveals an unmapped transmission path; must clear MORE than routine `cluster_secondary` tagging.
- **T3 load-bearing-but-thin-evidence** — could affect a position/thesis, routed SKIP-VERIFY/single-verify, but the *surrounding evidence base* is shallow (distinct from Phase 1.5 "is the framing true?" — T3 is "is the broader case under-researched?").
- **T4 position/thesis-pivot** — the answer could change position **sizing, timing, or core confidence.**
- **T5 verify-left-material-uncertainty** — CORRECTED-FRAMING / INDETERMINATE leaving a *substantive* open question (not a framing nit; about the residual question, not the correction).

**Gate (mandatory — applies to every trigger):** WALTER must state, one line each — **(a)** the question a *cheap verify can't* answer that deep-research would resolve, and **(b)** the consequence — the specific position size/timing, thesis weight, or coverage-channel decision that moves. **No consequence → no flag.** (Same discipline as the verify-spawn rule: decision-usefulness, not comprehensiveness.) A signal CONFIRMED by verify can still be a deep-research candidate — they're orthogonal.

**For any signal that passes:**
1. Add the 🔬 line to the Phase 3 push (template below).
2. Embed the ready-to-run `/deep-research` prompt in the BOARD signal body under a `## 🔬 Deep-research prompt (candidate)` section — persists in the permanent archive, not just Telegram.
3. Append a row to `registry/DEEP_RESEARCH_FLAGGED_LOG.tsv` (**13-col as of v0.27**): `disposition: PENDING`, `outcome: PENDING`, `executor: DEWEY` (default — Will opens a DEWEY session; set `Will` only if Will runs `/deep-research` directly), `prompt_ref` = the BOARD signal path, `deadline` = the date/named-event the research is decision-useful by (or `open` if not time-sensitive), **`impact` = LEAVE EMPTY at flag time** (free text, populated later at *consumption* — see below).
4. Tag the BOARD `dispatch_note`: `deep_research_candidate: <trigger-id> — <one-line decision question>`.

**Telegram push template** (appended under the normal push):
```
🔬 DEEP-RESEARCH CANDIDATE — SIG-W-YYYYMMDD-NNN
Why: <trigger + the stake, one line>
Question: <the specific decision question>
Would change: <the position / thesis / coverage that moves>
Run it: DEWEY session → /deep-research <self-contained prompt — pre-answer the skill's clarifiers>
```

**`/deep-research` prompt shape** (so Will can paste-and-go): `<Subject>: <the specific question>. Scope: <in/out of bounds>. Timeframe: <period>. Region/entities: <…>. This informs: <the decision it feeds>. `**`kill_condition: <moot if X has happened / after date Y; re-verify Z at intake>.`**` Prioritize primary sources; flag where evidence is thin or contested.`

**🆕 `kill_condition:` — REQUIRED on every new prompt (v0.27, 2026-07-24).** Closes a silent-failure mode: a prompt whose timing rationale has rotted still *runs*, at full cost, answering a question that no longer decides anything. Evidence: **PROMPT-15** (run 7/24) had `deliver_by` **10 days passed** with its gating catalyst already fired — caught by DEWEY's discipline, not by any mechanism; **prompt 12** (7/16) was parked after 2 of 3 decision-feeds resolved pre-run. Freeform, any mix of (a) event-based kill trigger, (b) date-based expiry, (c) re-verify-at-intake instruction. **Required on new prompts, optional on revisions** (no retro-fill). **Enforcement is DEWEY-side and self-enforced** — DEWEY's intake reads the field and **refuses to run if the condition is satisfied**, returning the prompt with the reason; **no new WALTER-side machinery.** Authoring bar: a kill_condition that can only be evaluated *by doing the research* isn't one — it must be checkable in seconds (a date, a calendar event, a published print).

**🆕 `impact` ledger column — populated at CONSUMPTION, not at flag time (v0.27, 2026-07-24).** One free-text line on what the consuming agent actually DID with the returned report (gate armed / killed / not-fired / calibrated / no-op-yet / thesis re-weighted). **The consuming DOMAIN AGENT writes it** when the report is load-bearing for a state change (closest to the event); **PROME sweeps the misses at its closeout.** **WALTER owns the ledger but is not the capture bottleneck** — do not block a dispatch on an empty `impact`. Rationale: DEWEY shipped 3 reports on 7/24 with zero structured path for impact to return, so it can't tell which prompt *kinds* pay off. Backfill-safe (existing rows empty; `walter_doctor` reads by column name). **Honest limit: this measures the flagged-prompt lane only** — Will-directed carve-outs and agent-originated slates (e.g. CARL's) never open a ledger row.

*Both items: DEWEY process-v2 memo 7/24 → PROME-endorsed with implementation authority granted (WALTER-owned template + ledger, no Will gate); Will-endorsed in-session 7/24. Full spec: `design/DEEP_RESEARCH_FLAG_PROPOSAL.md` §5b + §5e.*

**Constraints (hard):** **Full WALTER only** (Quick escalates — never raises this flag); **max 3 flags per batch**, target ~1-2/week; flag decision-useful unknowns, never "interesting"; **no auto-run, no sub-agent spawn, no research execution by WALTER** — deep-research is explicitly NOT in the autonomous-verify-spawn class. WALTER surfaces the prompt; **DEWEY executes it (Will triggers/approves)** — Will opens a DEWEY session (Tier-2, Claude Code), feeds it the prompt; DEWEY runs `/deep-research` under its citation/counter-evidence discipline, archives the cited report to `AGENTS/DEWEY/output/`, and hands it back to WALTER (Phase 2.8b). *(v0.20: executor moved "Will runs it" → DEWEY per the DEWEY revival; WALTER still never runs research itself.)*

**Calibration:** light review every closeout (glance at the week's fires + dispositions); formal review at **14 days OR 20 flags**, whichever first. Tighten if >2/wk sustained AND Will-`SKIPPED` rate >50%; loosen if <1/wk AND a retro "obvious miss" surfaces. `walter_doctor` `deep_research_pending_overdue` (check 10) surfaces PENDING-past-deadline rows (+ stale `open`>30d) in the boot reply. Data source: the ledger `disposition` + `outcome` columns; WALTER backfills `disposition`/`outcome` at next boot from Will's action.

**Honest load note:** the flag itself is zero research-execution load (one line at dispatch; WALTER never runs/spawns). The small *named* recurring costs: the ledger disposition/outcome backfill at boot + the `deep_research_pending_overdue` doctor check — both near-zero.

---

## PHASE 2.8b: RETURNING-DELIVERABLE HANDLING (route the `/deep-research` output)

Added v0.19 (Will sign-off 2026-06-19); **executor + consumption wiring v0.20 (2026-06-20).** Phase 2.8 *raises* the flag; this closes the loop when the `/deep-research` deliverable comes back. **Deliverable arrival (v0.20):** DEWEY drops a **create-only handoff in `AGENTS/WALTER/inbox/DEWEY/`** pointing at its `output/YYYY-MM-DD_topic.md` report + naming the originating flag ID (or Will pastes it live). **WALTER scans `inbox/DEWEY/` (non-`processed/`) at boot** (spawn-protocol step 7d) and consumes any NEW handoff. **WALTER routes the output — it does NOT re-analyze it** (lean mandate: the packet IS the analysis; `[[feedback]]` 2026-06-19 "WALTER stays lean").

**Default — ONE `research-output` BOARD signal:**
1. Archive the deliverable as a single signal (`signal_type: research-output`, next `SIG-W-YYYYMMDD-NNN`), **embed the packet verbatim** under a `## Full research packet (verbatim)` section — keeps BOARD the self-contained SoT and `walter_doctor board_reconcile` happy with one file.
2. Write a thin **routing wrapper** on top: a one-line **verdict** + a **per-recipient genuine-delta block** — what's NEW vs each recipient's current state (per `feedback_check_recipient_before_sharing`). Surface the ONE finding that MOVES a thesis, not a re-summary.
3. **No verify-spawn** — a deep-research deliverable is already primary-sourced → `verify_verdict: VERIFIED-PRIMARY`; a $0.05 routing-check is strictly dominated. (Carry through any caveat the deliverable itself flags; don't re-verify the whole thing.)
4. Route to the **domain owner (action) + genuine-delta info recipients**; run normal Phase 2 cluster/role tagging + Phase 3 + Phase 3.5 delivery.
5. **Close the ledger** — set the originating `DEEP_RESEARCH_FLAGGED_LOG` row `disposition: RESOLVED`, `outcome: DELIVERED as SIG-W-…`, and `executor:` = who actually ran it (DEWEY | Will). (`walter_doctor deep_research_pending_overdue` then drops it.)
6. **Mark the handoff PROCESSED (v0.20)** — if the deliverable arrived via a DEWEY handoff in `inbox/DEWEY/`, `git mv` it to `AGENTS/WALTER/inbox/DEWEY/processed/` once routed. Lifecycle: **NEW** (DEWEY created it in `inbox/DEWEY/`) → **ROUTED** (the `research-output` BOARD signal now exists) → **PROCESSED** (moved to `processed/`). The dir-move IS the state machine — it prevents the boot-scan from repeat-routing the same report. WALTER owns the move; DEWEY only ever creates in `inbox/DEWEY/`, never touches `processed/`. Use `git mv`, not bash mv (per `[[feedback_git_mv_for_inbox_processing]]`). (Mirrors the recipient-side `inbox/WALTER/` → `processed/` pattern from WALTER Routing v2 — here WALTER is the recipient of DEWEY's handoff.)

**Split test — carve a finding into its OWN signal only when it meets ANY one:**
- **S1 — different action-owner AND independently actionable:** owner ≠ the document's owner AND it stands alone as a decision, not just FYI context.
- **S2 — maps to a registered trigger / falsification anchor** (RED-FT / REG-T / ROUTING_TABLE Boundary): needs independent tracking + may auto-fire.
- **S3 — ages / falsifies on a different clock:** you want to lifecycle-tag it (SUPERSEDED / FALSIFIED / EVENT-PASSED) independently of the parent.
- **S4 — standalone discovery unit:** a finding someone would grep BOARD for on its own, in a different primary cluster.

**Precedence note (S4 vs the wrapper-delta):** a finding *elevated as THE wrapper-delta* — the one finding that moves a thesis, surfaced prominently in the parent verdict + its own per-recipient block — already satisfies the discovery need, so **S4 does not independently force a split for it.** Split on S4 only when the finding is a genuinely separate discovery unit you'd grep for independently AND it is *not* already the parent's headline. A finding that merely sits in a different `cluster_secondary` is **not** automatically S4 — the parent's `cluster_secondary` tag + delta wrapper already cover cross-cluster discovery.

If a finding passes, dispatch it as a **child signal that cross-refs the parent** (`deep_research_ref: <parent SIG-ID>`); the parent stays the archive/SoT. **Default remains one signal + delta wrapper — splitting is the exception, paid only when the test is met.** Asymmetry: over-splitting = recipient noise (one owner gets N handoffs for one doc) + scattered archive + messy ledger; under-splitting = a trigger-linked or differently-aging finding buried where it won't get tracked. So one-by-default, split-on-test.

**Worked example — SIG-W-20260619-008 (S-FL distress deep-research, the first instance):** routed as ONE signal → CORAL action / REGINALD,CARL,SHADE,MARCO,RED info, packet embedded verbatim + 6 per-recipient delta handoffs; closed the SIG-007 ledger row. Split test applied finding-by-finding — bankruptcy/per-capita, bank-transmission, consumer/energy-CPI, business-bankruptcy, macro-overlay all FAILED (same owner CORAL/REGINALD, interdependent legs of one 70/30 verdict, no trigger linkage, same ~Q2/Q3 clock) → kept unified. The **insurance commercial/condo finding** was the one borderline candidate (distinct INSURANCE cluster, SHADE-relevant, the only thesis-correcting item) but FAILED all four — S1 (still CORAL-action — it's CORAL's mechanism), S2 (no registered trigger), S3 (same ~Q2/Q3 clock as the rest), S4 (per the precedence note: it was **elevated as THE wrapper-delta + cc'd SHADE**, so the distinct INSURANCE `cluster_secondary` alone doesn't force a split) → kept in rather than fragmenting. Net: one signal was correct.

---

