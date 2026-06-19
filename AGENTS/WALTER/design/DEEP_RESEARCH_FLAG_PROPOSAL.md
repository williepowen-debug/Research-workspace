# DEEP-RESEARCH CANDIDATE FLAG — Proposal

**Status:** PROPOSAL — **endorsed by PROME (6/19) + WALTER (6/19); §8 resolved; ready for WALTER to ratify per §9**
**Date:** 2026-06-19
**Origin:** Will idea ("give me a heads-up when a signal would benefit from a deeper / surrounding research task") → WALTER first-pass design (Telegram, 6/19) → design review + drafting (Claude Code helper session, branch `claude/brave-gates-jl3699`) → **PROME review 6/19** → **WALTER ratification-review 6/19**
**Reviewed:**
- **PROME 6/19** — endorses; route to WALTER for ratification (don't land live specs directly); requested ledger `prompt_ref` + `deadline` (folded in §5b).
- **WALTER 6/19** — endorses; self-validated the gate against the day's 7 dispatches → ~1 flag (SIG-007 FL bankruptcy), confirming the ~1-2/wk cadence. Three notes folded into v0.3: (a) honest load accounting — the flag is zero *research-execution* load, the ledger backfill + doctor check are named near-zero recurring steps; (b) **walter_doctor `deep_research_pending_overdue` check pulled into v1** (Will: include + surface in boot reply); (c) trailer — dropped the stale "4.7" normalization (CLAUDE.md 16d convention line is stale; WALTER uses its standard trailer).
**Canonical owner (process step):** `design/SIGNAL_PROCESSING_CHECKLIST.md` (new Phase 2.8) — version target **v0.17 → v0.18**
**New WALTER-owned file:** `registry/DEEP_RESEARCH_FLAGGED_LOG.tsv` · **walter_doctor:** +1 check (§5i)
**No FORMAT_SPEC change required for v1** (optional header field deferred to v1.1 — see §7)

---

## 1. Summary

A **triage flag** with no research-execution load on WALTER. When a dispatched signal trips a tight trigger set **and** clears a materiality gate, WALTER adds one line to the Telegram push — `🔬 DEEP-RESEARCH CANDIDATE` — naming the decision-relevant question a deeper research pass would answer, plus a ready-to-paste `/deep-research` prompt. **Will decides every time; WALTER never runs it.** Every fire is logged to a new ledger (with the prompt and a deadline) so the cadence is measurable, the suggestion persists, and the loop closes.

**Honest load accounting:** the flag itself is one line at dispatch and WALTER never runs/spawns the research — that part is zero load. The small recurring costs, named so we're not pretending: the ledger `disposition`/`outcome` backfill at next boot (§8.2) and the `deep_research_pending_overdue` doctor check (§5i). Both are near-zero.

This sits inside WALTER's existing role (triage / surface-not-execute) and mirrors the boot-time news-sweep posture: surface novel items, never auto-dispatch, preserve the Will-curated decision loop. The deeper research pass itself is the **`/deep-research` skill** already in this workspace (fan-out web search → fetch sources → adversarial verify → cited report).

---

## 2. Problem / motivation

WALTER routes signals but has no mechanism to say *"this one is worth a deeper, surrounding research pass before we lean on it."* Some signals are load-bearing, cross-cutting, or open a thesis-channel we don't yet track (FL bankruptcy-filings → CORAL was exactly this) — and a `/deep-research` pass would meaningfully move confidence, a position, or our coverage map. Today that judgment lives only in Will's head and gets made ad hoc.

**The core design risk (the thing that makes or breaks it):** in WALTER's system, "cross-cutting / multi-cluster" is the *median* signal, not a rare one. `network_uncertainty_peak` (≥5 `cluster_mediating`/day) fired two consecutive days (6/18, 6/19). If "touches ≥2 clusters" or "I could only SKIP-VERIFY it" fire the flag on their own, the flag fires 3-5×/day, not the intended ~1-2/week — and Will tunes it out within a week.

**The fix:** triggers are *necessary-but-not-sufficient*. The flag fires only when a trigger trips **AND** a materiality gate passes. The gate is the whole game.

**Self-validation (WALTER, 6/19):** run against the day's 7 dispatches, the gate fires ~1 flag — SIG-007 FL bankruptcy (T1 + clean gate: "genuine inflection vs base-effect?" → CORAL opens a standing channel + shifts FL bank-collateral weight). The other 6 fail the gate (verify-resolved or domain-owned, no deep-research-specific consequence). The design self-validates to ~1-2/wk against live data.

---

## 3. Design — trigger set + gate

**🔬 DEEP-RESEARCH CANDIDATE fires when ≥1 trigger trips AND the gate passes.**

### Triggers (any one)

| ID | Trigger | Notes |
|----|---------|-------|
| **T1** | **New coverage channel** — opens a signal lane / sub-domain the network doesn't yet track (e.g. FL bankruptcy-filings → CORAL). | **Highest value.** This is what the system structurally can't see on its own — it expands the coverage map, not just confidence on an existing line. |
| **T2** | **New cross-channel interaction** — not merely "touches 2 clusters" (routine `cluster_secondary` tagging), but reveals a transmission path we haven't mapped. | The bar is: would deep-research map a path we're currently treating as two separate stories? Must clear more than carrying a secondary cluster tag. |
| **T3** | **Load-bearing but thin evidence** — could affect a position/thesis, routed at SKIP-VERIFY / single-verify, but the *surrounding evidence base* (not just the framing) is shallow. | Distinct from Phase 1.5 (see §4). Phase 1.5 asks "is the framing true?"; T3 asks "is the broader case under-researched?" |
| **T4** | **Position / thesis pivot** — the answer could change position **sizing, timing, or core confidence**. | Highest materiality; easiest gate to pass. |
| **T5** | **Verify left material uncertainty** — CORRECTED-FRAMING / INDETERMINATE on something important, leaving a *substantive* open question (not a framing nit). | Composes with the Phase 1.5 verdict; T5 is about the residual question, not the correction itself. |

### Gate (mandatory — applies to every trigger)

WALTER must be able to state, in one line each:

- **(a) The question** a *cheap verify can't* answer, that deep-research would resolve.
- **(b) The consequence** — what changes if the answer is yes/no: a specific position size/timing, thesis weight, or coverage-channel decision.

**No consequence → no flag.** This is the same discipline as WALTER's verify-spawn rule ("ask for decision-usefulness, not comprehensiveness") and the ADViCE quality checks. It is the primary noise suppressant and the reason the cadence can hold at 1-2/week despite the triggers describing common signal properties.

---

## 4. verify-research vs deep-research (keep these distinct)

Triggers T3/T5 reference WALTER's verify-research; they must not collapse into "flag everything I verified."

| | **verify-research** (Phase 1.5) | **deep-research** (this flag) |
|--|--------------------------------|-------------------------------|
| Question | "Is this framing **true right now**?" | "What's the **full surrounding picture / second-order map**?" |
| Who runs it | WALTER, autonomously | Will, on decision (WALTER never runs it) |
| Cost / scope | ~$0.05, single tight question, pre-route | Larger, multi-source, post-route |
| Tool | sub-agent verify spawn | `/deep-research` skill |
| Output | one-line VERDICT (CONFIRMED / CORRECTED-FRAMING / FALSE / INDETERMINATE) | cited report |

A signal can be CONFIRMED by verify (framing true) **and** still be a deep-research candidate (the surrounding case is worth mapping). They're orthogonal.

---

## 5. Where it lands (canonical-source-first)

### 5a. CHECKLIST — new Phase 2.8 (paste-ready)

Insert after Phase 2.7 (composite-bifurcation), before Phase 3 OUTPUT. Bump header v0.17 → **v0.18**.

> ## PHASE 2.8: DEEP-RESEARCH CANDIDATE SCAN (Full WALTER only)
>
> Added v0.18. Runs at dispatch-batch shaping, AFTER Phase 2.7 composite-bifurcation tagging and BEFORE Phase 3 OUTPUT writes. A triage flag with no research-execution load: surfaces signals worth a deeper `/deep-research` pass; Will decides every time, WALTER never runs it.
>
> For each surviving signal, check the trigger set + gate:
>
> **Triggers (any one):** T1 new-coverage-channel · T2 new-cross-channel-interaction · T3 load-bearing-but-thin-evidence · T4 position/thesis-pivot (sizing/timing/confidence) · T5 verify-left-material-uncertainty. (Full definitions in `design/DEEP_RESEARCH_FLAG_PROPOSAL.md` §3.)
>
> **Gate (mandatory):** WALTER can name (a) the question a cheap verify can't answer, and (b) the consequence — what changes if the answer is yes/no. **No consequence → no flag.** T2 in particular must clear more than "carries `cluster_secondary`" (routine).
>
> **For any signal that passes:**
> 1. Add the 🔬 line to the Phase 3 push (template §5d).
> 2. Embed the ready-to-run `/deep-research` prompt (template §5e) in the BOARD signal body under a `## 🔬 Deep-research prompt (candidate)` section, so it persists in the permanent archive (not just Telegram).
> 3. Append a row to `registry/DEEP_RESEARCH_FLAGGED_LOG.tsv` (schema §5b): `disposition: PENDING`, `outcome: PENDING`, `prompt_ref` = the BOARD signal path, `deadline` = the date/event by which the research is decision-useful (or `open` if not time-sensitive).
> 4. Tag the BOARD dispatch_note: `deep_research_candidate: <trigger-id> — <decision question>`.
>
> **Constraints (§5h):** Full WALTER only; **max 3 per batch**, target ~1-2/week; flag decision-useful unknowns, never "interesting"; **no auto-run, no sub-agent spawn, no research execution by WALTER**. Quick WALTER never fires this — if it sees a candidate it queues/escalates to Full WALTER (per the v0.17 bright line).
>
> **Calibration (§5f):** light review every closeout; formal review at 14 days OR 20 flags, whichever comes first. `walter_doctor` surfaces PENDING-past-deadline rows in the boot reply (§5i). The ledger's `disposition` + `outcome` columns are the data.

### 5b. New ledger — `registry/DEEP_RESEARCH_FLAGGED_LOG.tsv`

WALTER-owned, append-only, tab-separated. Same family as `FALSIFICATION_FIRED_LOG.tsv` / `REG_THRESHOLDS_FIRED_LOG.tsv`. Header row:

```
flagged_date	signal_id	trigger	clusters	decision_question	what_changes	prompt_ref	deadline	disposition	outcome	notes
```

- `trigger` — one of T1–T5 (comma-joined if multiple)
- `prompt_ref` — **path to where the ready-to-run prompt lives** (per PROME: don't let the suggestion vanish into Telegram scroll). For v1 (dispatched-signals-only) this is the BOARD signal file, which carries the prompt in its `## 🔬 Deep-research prompt (candidate)` body section. *Why `prompt_ref` not an inline `prompt` column: a TSV can't safely hold a multi-line prompt (embedded newlines/tabs break row/column parsing). Embedding in the immutable BOARD body + referencing it is TSV-safe and persistent. If standalone flags arrive later (v2, see §8.3), they'd write a dedicated prompt file and point `prompt_ref` at it.*
- `deadline` — ISO date or named event by which the research is decision-useful (e.g. `2026-06-24 / next EIA WPSR`), or `open` if not time-sensitive
- `disposition` — `PENDING` / `RAN` / `SKIPPED` / `DEFERRED` (Will's action; WALTER backfills at next boot — §8.2)
- `outcome` — `PENDING` / `CHANGED-POSITION` / `CHANGED-THESIS` / `EXPANDED-COVERAGE` / `CONFIRMED-NO-CHANGE` (filled retro)

This is the piece WALTER's first-pass design was missing: "tag the BOARD signal" isn't queryable. The ledger makes the 1-2/week target empirical and closes the proposal loop (root Critical Rule #10).

### 5c. dispatch_note convention

On a flagged signal's BOARD entry, append to `dispatch_note`:
```
deep_research_candidate: <trigger-id> — <one-line decision question>
```
No new header field for v1 (see §7). The dispatch_note tag + the embedded prompt + the ledger are the durable record; the Telegram line is the live surface.

### 5d. Telegram push template (appended under the normal push)

```
🔬 DEEP-RESEARCH CANDIDATE — SIG-W-YYYYMMDD-NNN
Why: <trigger + the stake, one line>
Question: <the specific decision question>
Would change: <the position / thesis / coverage that moves>
Run it: /deep-research <self-contained prompt — see §5e>
```

### 5e. `/deep-research` prompt shape

The skill asks clarifying questions if the prompt is underspecified, so WALTER pre-answers them so Will can paste-and-go. Template:

```
/deep-research <Subject>: <the specific question>.
Scope: <in / out of bounds>.
Timeframe: <period>. Region/entities: <...>.
This informs: <the decision it feeds>.
Prioritize primary sources; flag where evidence is thin or contested.
```

Worked example (the FL bankruptcy case):

```
/deep-research South Florida consumer + business bankruptcy filings: is the recent
uptick a genuine stress inflection or base-effect noise? Scope: Ch7/11/13 filing
trends across S. FL districts, 2023–2026, with drivers (insurance cost-push, property
tax, Iran-energy pump pass-through). Region: Miami-Dade, Broward, Palm Beach. This
informs: whether CORAL opens a standing bankruptcy-filings coverage channel and whether
it shifts the FL bank-collateral thesis weight. Prioritize court/PACER data and named
local sources; flag where the "two of top-six districts" claim is unverified.
```

### 5f. Calibration rule

- **Light review every closeout** — glance at the week's fires + dispositions.
- **Formal review at 14 days OR 20 flags, whichever comes first** (folds into the standing LIAISON calibration cadence).
- **Tighten** if >2/wk sustained AND Will-`SKIPPED` rate >50% (firing on things Will doesn't action = noise).
- **Loosen** if <1/wk AND a retro "obvious miss" surfaces.
- Data source: the ledger `disposition` + `outcome` columns.

### 5g. Quick vs Full WALTER

**Full WALTER only.** Quick WALTER (PROME-spawned, trigger-only route runner) never raises this flag — it's a discretionary judgment call, and per CHECKLIST v0.17 Quick escalates all novel judgment to Full WALTER. (Add a one-line note to the CLAUDE.md RUN MODES "Quick does NOT self-judge" list and to CHECKLIST Phase 3.5's Quick-vs-Full paragraph.)

### 5h. Constraints (hard rules)

- **Full WALTER only** (Quick escalates — §5g).
- **Max 3 flags per batch; target ~1-2/week.** The per-batch cap stops a single noisy batch from flooding even when the weekly average looks fine.
- **Flag decision-useful unknowns, never "interesting."** The gate (§3) enforces this.
- **No auto-run, no sub-agent spawn, no research execution by WALTER.** Deep-research is explicitly NOT in WALTER's autonomous-verify-spawn class. WALTER surfaces the prompt; Will runs it.

### 5i. walter_doctor check — `deep_research_pending_overdue` (v1, per Will 6/19)

A read-only check added to `tools/walter_doctor.py` (becomes the 10th check), same family as `delivered_but_unconsumed`. Reads `registry/DEEP_RESEARCH_FLAGGED_LOG.tsv` directly — **no header-field dependency** (this is the concrete proof the §7 header field isn't needed for v1):

- Flags any row with `disposition: PENDING` whose `deadline` is a real date that has passed.
- Flags any row with `deadline: open` that has been `PENDING` > 30 days (so `open` doesn't become a silent backlog escape-hatch).
- Each is a **MED** finding (surfaced, not blocking); contributes to the doctor exit-code count like the other MED checks.
- **Surfaced in the Will-Telegram boot reply** (Will 6/19) via the existing step-0.5 mechanism, alongside cron-staleness / Iran-anchor / near-trigger callbacks — e.g. `🔬 deep-research flag SIG-W-...-007 PENDING past deadline (run it or drop it?)`.

Closes the loop the `deadline` column opens: a flagged-then-forgotten candidate can't pass its deadline silently until the next formal review.

---

## 6. What this is NOT

- **Not a new `signal_type`.** It's an annotation on a dispatched signal, not a change to what the signal *is*. `signal_type` stays as-is (`research` / `manual-flag` etc. are unrelated).
- **Not an auto-run.** WALTER surfaces; Will runs. No research-execution load on WALTER (the flag is one line at dispatch; WALTER never runs or spawns the research). The recurring costs are small and named: the ledger backfill (§8.2) and the doctor check (§5i).
- **Not a replacement for Phase 1.5 verify.** Orthogonal (see §4).

---

## 7. Deferred to v1.1 (optional)

**Optional header field** `deep_research_candidate: true` + `deep_research_question: "<...>"` in FORMAT_SPEC. This is a "small change" (add optional field) under WALTER's spec-change rule and would give header-level machine queryability. **Decision: defer** (PROME + Will, 6/19) — ledger + dispatch_note are enough for v1, and the v1 doctor check (§5i) reads the ledger TSV directly, so it does **not** need this field. Add it later only if a future need wants header-level querying. If added, FORMAT_SPEC is the canonical owner and gets edited first.

---

## 8. Open questions — RESOLVED (PROME + WALTER + Will, 6/19)

1. **Calibration cadence** → **light review every closeout + formal review at 14 days OR 20 flags, whichever first.** (§5f)
2. **`disposition`/`outcome` backfill** → **WALTER owns it, at next boot, from Will's action / any resulting artifacts.** Near-zero recurring step (named honestly, not "zero"). (§5b, §1)
3. **Standalone flags (coverage-gap with no signal attached)** → **v1 = dispatched signals only.** Add a standalone path later if needed (most relevant for T1); when added it writes a dedicated prompt file for `prompt_ref`. (§5b)
4. **v1.1 header field** → **defer.** Ledger + dispatch_note enough for v1; doctor check (§5i) needs no field. (§7)
5. **PROME addition (folded in):** ledger gains **`prompt_ref`** (the prompt persists, doesn't vanish into Telegram scroll) and **`deadline`** (time-sensitivity). Realized as `prompt_ref` → BOARD body for TSV-safety. (§5b)
6. **WALTER addition (Will: in v1):** **`deep_research_pending_overdue` walter_doctor check**, surfaced in the **boot reply** — flags PENDING-past-deadline rows (+ stale `open` rows >30d). (§5i)

---

## 9. Ratification checklist (steps WALTER executes to land it)

Canonical-source-first, per WALTER spec-change rule + version-drift guard:

- [ ] Land **Phase 2.8** text (§5a) into `design/SIGNAL_PROCESSING_CHECKLIST.md`; bump header **v0.17 → v0.18** + add the v0.18 line to the footer version log.
- [ ] Create `registry/DEEP_RESEARCH_FLAGGED_LOG.tsv` with the §5b **11-column** header row.
- [ ] Confirm Phase 2.8 includes the **prompt-embed step** (write the `/deep-research` prompt into the BOARD signal body) so `prompt_ref` resolves.
- [ ] Add the dispatch_note convention (§5c) — referenced from Phase 2.8, no separate doc.
- [ ] Add the **`deep_research_pending_overdue` check** to `tools/walter_doctor.py` (10th check; MED; reads the ledger TSV; flags PENDING-past-`deadline` + stale `open`>30d) and wire it into the **boot-reply** callbacks (CLAUDE.md spawn-protocol step 0.5 check list + the boot-reply surfacing in step 1).
- [ ] Add the §5g Quick-vs-Full + §5h constraints one-liners to CLAUDE.md RUN MODES + CHECKLIST Phase 3.5 Quick paragraph.
- [ ] Add a canonical-source lookup row to CLAUDE.md: *"Deep-research candidate flag (Phase 2.8 + ledger + doctor check)" → owner `SIGNAL_PROCESSING_CHECKLIST.md` / dependents: `registry/DEEP_RESEARCH_FLAGGED_LOG.tsv`, `tools/walter_doctor.py`, CLAUDE.md RUN MODES.*
- [ ] Sync `design/STATE.md` §1 with the CHECKLIST v0.18 bump (+ note the new ledger + doctor-check count 9→10); run `tools/version_drift_check.py` to confirm.
- [ ] (Optional) Note in MEMORY.md "Promoted to specs" line: deep-research candidate flag → CHECKLIST v0.18 + doctor check.
- [ ] Commit with WALTER's standard trailer. *(The staging commits on `claude/brave-gates-jl3699` used the helper session's trailer — no need to amend history. Note: CLAUDE.md step 16d still cites `Claude Opus 4.7`, which WALTER flagged as a stale convention line — self-correct that whenever 16d is next touched.)*

---

*Proposal v0.3 — 2026-06-19. Drafted for WALTER ratification; not yet landed in any canonical spec. WALTER owns the spec changes and the version bump; this doc is the staging ground.*
*v0.3 changelog: folded WALTER 6/19 ratification-review — added `deep_research_pending_overdue` walter_doctor check to v1 (boot-reply surfaced, §5i); honest load accounting (flag = zero research-execution load; backfill + doctor check named as near-zero recurring steps); removed stale "4.7" trailer-normalization instruction; recorded WALTER's self-validation (7 dispatches → ~1 flag). v0.2: folded PROME review — §8 resolved; ledger `prompt_ref` + `deadline`; max-3-per-batch + constraints block; T4 timing; calibration cadence finalized. v0.1: initial draft.*
