# Gate C Increment 2 — the ledger takes real work (proposal)

**Prepared:** 2026-08-27 evening, by PROME (builder/custodian — NOT this increment's reviewer). **State:** DRAFT FOR INDEPENDENT REVIEW (RED asked; DAEDALUS alternate) → activation packet with exact pins → Will's window ruling. **Authorizing word to draft:** Will in-session 2026-08-27, "go," on the presented two-path plan.
**What this is:** a WORKLOAD increment, not a machinery change. The pilot (LIVE-2026-0001, C8 RULED CONTINUE) proved acceptance end-to-end; this starts the actual book. No code changes are proposed; the corrected runbook (post-C8 conditions 1–6) governs verbatim.

## 1. Perimeter

**Command families this increment (exact schema enum names):** `RegisterQuestion` · `SubmitForecast` · `ProposeResolution` · `VerifyResolution`.
Explicitly OUT this increment: `AmendForecast` / `WithdrawForecast` / `DisputeResolution` / `CorrectResolution` / `AnnulQuestion` / ~~`CloseQuestion`~~ — available to future increments; the first live book stays append-simple so every record class exercised has one clear happy path.

> **PERIMETER AMENDMENT — 2026-08-27 late (PROME draft; REVIEWER BLESSING + Will's packet ruling REQUIRED before it takes effect; MIDAS-flagged, `4d63c8d36` packet §3): `CloseQuestion` is IN this increment, narrowly.** The original OUT-list contradicted this increment's own resolution mechanics: `ProposeResolution` is legal only from `CLOSED` (or `DISPUTED`), so the first live Resolution (MIDAS-06) structurally requires a `CloseQuestion` — the sitting-2 grants draft already carried `question.close_own` for exactly this reason, and MIDAS's authored activation-1 set (Register + Forecast + Close, `CMD-…006a/6b/6c`) is the flagged instance. **Scope of the amendment: `CloseQuestion` only as `question.close_own` — a desk closing its OWN question, as the structural predecessor of a `ProposeResolution` this same increment executes.** General/cross-desk close, and the other five families, stay OUT. Both original documents were right about their own object (append-simple perimeter vs. state-machine legality); nothing had reconciled them until MIDAS refused to work around the gap. ⚠️ **RED's review ask ① (perimeter legality) predates this amendment — the amendment itself needs a reviewer verdict (RED or DAEDALUS) before Will's ruling covers it.** ✅ **BLESSED 2026-08-27 ~22:15 — DAEDALUS reviewer verdict (`AGENTS/DAEDALUS/reports/2026-08-27_KERNEL_PERIMETER_AMENDMENT_REVIEW.md`, `9ad1e83ab`): scope mechanically enforced at three verified layers (capability mapping · state-machine owner check `core.py:837-843` · grants draft), with condition P1 registered below.**
>
> 🔒 **P1 TRIPWIRE (DAEDALUS condition, registered HERE because this line is where perimeter widening gets decided): before ANY increment that widens forecasting beyond `forecast.submit_own` (i.e., any `forecast.submit` on another desk's question), RE-REVIEW the close-timing interaction — `QuestionClosed` has NO `closes_at` floor, so early close is mechanically permitted; harmless while every forecast on a question is the owner's own, it becomes a rival-forecast-lock lever the day cross-desk forecasting enters.** Found by rule at this line, not by re-discovery.

**Submitting desks (C1 contract — each authors and commits its OWN byte-frozen files; PROME authors nothing):**
- Live tonight: **CREED, LIQUID, REGINALD** — each selects **1–3 of its own currently-registered predictions**, forward-resolving only.
- At next boot: **MIDAS** (its rows enter as Question+Forecast; its MIDAS-06 resolution is this increment's first `ProposeResolution`, possible only after the Mon 8/31 DFII10 publication) and **SAM** (optional additional questions; its SAM-33 records already stand).
- **No backfill:** already-resolved history does not enter. Forward-only is the anti-silent-error stance.

**Actor-registry additions required:** CREED, LIQUID, REGINALD, MIDAS (registry today holds WILL, PROME, RED, SAM). A policy/registry version change is a custodian commit class **only under an operator-approved activation packet** — the additions ship inside this increment's ruled packet, listed by name, nothing else in the file touched.

**Resolution mechanics on first live use (the one genuinely new exercise):** proposer ≠ verifier, both named per-question in the question document (the SAM-33 pattern: `independent_verifier_actor_id`). For MIDAS-06: MIDAS proposes; the named independent verifier verifies. A verify that cannot complete leaves the resolution un-verified and visible — never silently accepted.

## 2. Window options (Will picks at the activation ruling)

- **Path A:** sitting TONIGHT (Question/Forecast batch from the live desks) + a short Monday sitting (MIDAS rows + the first Resolution, post-16:15 ET publication).
- **Path B:** ONE sitting Monday post-16:15 ET taking everything — questions, forecasts, and the first resolution in a single ~60-minute window.

## 3. Unchanged constants (the certified posture — none of this loosens)

Attended sitting, Will present · PROME sole writer, half-open UTC window ruled verbatim by Will, canonical-form timestamps (D2 example in the runbook) · every command file **byte-frozen with sha256 pinned in the activation document** before the ruling · N2 tee-transcript from invocation one · N3 affirmative close (`revoked_at` set + committed) · D5 push-train reality (no step depends on locality) · stop conditions verbatim from the readiness plan · three-date discipline for any retroactive fact · additions-only on protected paths · CI never a writer, no timeout custody transfer, **no standing grant — every window is Will-worded**.

## 4. Review ask (RED; packet-level, not code re-review)

① Perimeter legality vs `SPEC.md` and the schema enums (families in/out) · ② actor-registry additions minimal and correctly scoped · ③ Resolution-family first-live-use mechanics (proposer/verifier separation; failure-visible verify) · ④ the no-backfill boundary stated tightly enough to refuse a marginal case · ⑤ anything in the corrected runbook this workload strains that the pilot's 2-command shape didn't. Pins verified at activation-packet stage (the packet, not this proposal, carries hashes).

## 5. Costs

Authoring ~20–40 min per desk (own lane) · review ~30–60 min · sitting ~45–60 attended min (Path B) or ~60+30 (Path A) · $0.

## 6. Sequence from here

Desk prep (parallel, tonight where live) → activation packet cut with exact pins → RED review verdict → Will rules window + packet → sitting per runbook steps 0–9 → closeout packet → **closeout reviewer = RED or DAEDALUS, never PROME** (standing 8/26 ruling).
