# Gate C C7 Activation Packet — v2 (fresh cut)

**Prepared:** 2026-08-27T15:34:33Z (clock-pulled; prior blocked draft: `GATE_C_C7_ACTIVATION_PACKET.md`, 2026-08-26 — retained as the preflight record; per its own ruling line, nothing here incorporates approval by reference to it)

**State:** PRESENTED FOR ACTIVATION RULING — awaiting Will's word. Per the accepted day-boundary rider (2026-08-26 discussion), remediation and review completed 2026-08-27, so the **earliest ruling date is 2026-08-28**.

## Remediation record — all six required items COMPLETE

| # | Required (per the blocked draft) | Evidence |
|---|---|---|
| 1 | One explicit live mode, no synthetic boundary weakened | `KERNEL/tools/live_shadow.py` (`f8560f2c0`); `gate_c_boundary`/`acceptance`/`audit`/`projection` untouched, verified at the review |
| 2 | Exact repository, commit, submission paths, policy files, event IDs, result/view paths as inputs | Activation-document schema `kernel.live-activation.1`: absolute root binding, pinned sha256 ×(2 submissions + 3 policies), exact command IDs, event-ID map |
| 3 | Activation document carrying Will's exact half-open UTC window; absence/expiry/mismatch/ambiguity fail before any write | `authorize_live_activation` refuses first; window is half-open `[start, end)` exactly (review-verified) |
| 4 | One PROME writer, explicit staging only, no auto commit/push, additions-only durable results, disposable `.rw/` | Unchanged from C6; custody-primary guard now direct-tested |
| 5 | Exhaustive synthetic refusal tests, then the complete C6 rehearsal through the exact interface | **212 tests green** (was 191 pre-build); full rehearsal transcript durable at `KERNEL/rehearsals/2026-08-26_live-interface-rehearsal-transcript.txt` |
| 6 | Independent adversarial review, then a fresh packet | **RED review 2026-08-27: PROCEED** (`AGENTS/RED/challenges/2026-08-27_KERNEL_GATE_C_LIVE_INTERFACE_ADVERSARIAL_REVIEW.md`); two MODERATE findings **closed by mechanism** same day (`67136c509` window-enforcement grant slot + store refusal; `ec254da22` views-path guard at `write_views`); both deltas **probe-verified by RED**; **CHG-RED-050 RESOLVED, no hold** |

**Core review result (RED, verified by probe not assertion):** no route to a live write without a valid activation; the leftover-rehearsal-document-against-real-root case refuses at two independent layers; duck-typed fake grants refused by `isinstance`; all pin tampers, policy repointing, identity fields, and field-set equality refuse before any write. Both durable-write chokepoints (`store.publish` for events/receipts, `write_views` for registered views) are now **enforced by type, not call path**.

## Fixed pilot perimeter (unchanged from the blocked draft)

- source commit `1d9400425f7415083a9ffbd10964670bf255abf2`;
- `AGENTS/SAM/thesis/PREDICTIONS.tsv`, locator `Pred_ID=SAM-33`;
- `AGENTS/SAM/thesis/SAM-33_KERNEL_NATIVE_COMPANION.json`, pointers `/question` and `/forecast`;
- exactly `CMD-019305f8-ec00-7000-8000-000000000033` then `CMD-019305f8-ec00-7000-8000-000000000034`;
- PROME as sole active writer, RED dormant, no substitute activation;
- `kernel.schema.1`, `kernel.policy.1`, checked-in `KERNEL/policies/custody-policy.json`;
- one manual operator-attended window;
- all stop conditions in `KERNEL/GATE_C_READINESS_PLAN.md`.

**Pin status at cut (2026-08-27):** pinned commit present in history (verified `git cat-file -e`). The two SAM native files have advanced **2 commits** since the pin (SAM-41 grading, 2026-08-27 — unrelated rows). Native refs resolve against the **immutable pinned commit**, so they remain valid; the pilot's events will cite the pinned state, not HEAD. Stated here so the ruling is made knowing the pin is a dated snapshot, which is the designed shape for a shadow pilot.

## Declared gaps (coverage section — stated, not absorbed)

1. **Disposable-clone rehearsal not re-run after the review deltas.** The reviewer reconciled the durable transcript against the record (clean) instead; a full re-run would be strictly stronger. The deltas since the rehearsal are the two guard commits (test-covered) only.
2. **Lock path — VERIFIED LOW-severity known gap** (upgraded from "unverified" by RED's re-probe): `FixtureAcceptanceLock` does not honour `window_enforced` — a lock acquires under an unenforced grant. `.rw/` is disposable by design (byte-identical projection rebuild proven in rehearsal), lock files sit outside the additions-only perimeter, and both durable paths refuse independently, so nothing durable follows from holding it. Post-pilot consistency extension registered.
3. **`write_views` guard is opt-in by parameter** — a caller that holds a grant and simply does not pass it still writes. Same cooperative-actor posture as the disclosed `_MINT_KEY` limitation (spec §2.2 / decision 20); the live interface always passes it. Stronger destination-keyed form registered post-pilot.

## Post-pilot items (registered, non-blocking, each with its own review)

Narrowed read capability for `--check-views`/`--audit-additions` · lock-path `window_enforced` guard · destination-keyed view guard.

## Operator ruling line

This packet requests Will's activation ruling containing the **exact half-open UTC window** (start and end), transcribed verbatim into the activation document at mint time. ~~Recommended window: one operator-attended sitting inside "Sat 2026-08-30 – Sun 2026-08-31 (ET)"~~ **[day-names were WRONG — 8/29 is Saturday, 8/30 Sunday, 8/31 Monday; a carried error from the 8/26 handoff, RED-caught at its claim_check 8/27 — and SUPERSEDED: Will ruled in-session 2026-08-27 for a TODAY sitting, explicitly waiving his 8/26 day-boundary rider (the option he selected named the waiver; RED's same-day independent re-review of the remediation had already satisfied the rider's fresh-eyes substance). Exact UTC bounds: stated by Will in-session and transcribed into the activation document at mint — see `GATE_C_C7_RUNBOOK.md` step 2.]** The exact bounds are Will's to state and cannot be inferred from any recommendation. Absent that ruling, nothing activates: the live door refuses by default, as built and as reviewed.
