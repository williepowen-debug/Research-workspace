# HAW19 prospective terminal measurement contract

DRAFT v2, September8,2026. This refines the proposed successor; it is not an instrument for regrading original HAW19. Reader: HAWK readiness review September11 and any registration before October1. No vendor access, calibrated probability or owner confirmation is implied.

## Scope and identities

Freeze an enumerated list of named crude-export terminals in the two owner theaters before registration, including geographic boundary, aliases and both vendors' terminal IDs. Define crude products explicitly and identically in both queries; exclude condensate, LPG/LNG, refined products, GTL and ship-to-ship transfers unless a later prospective version expressly includes them. Missing geography/product mapping prevents registration, rather than allowing the universe to contract after an event.

One terminal ID is the unit of adjudication. Separate damage-event IDs identify new physical damage during October1–31 UTC. Repeated strikes do not create another terminal or add unrecovered nameplate loss twice. A terminal already impaired before the event uses its actual pre-event baseline, not nameplate or pre-war throughput; that limits this claim to incremental loss. Record event time, first report time and retrieval time independently. Uncertain event-window membership remains unresolved.

A loading path is a complete operable route from terminal receipt/storage through pumps/pipes to a loading outlet, not merely a mooring. Enumerate paths, shared bottlenecks and pre-event operability from dated operator/technical evidence with imagery corroboration. Damage to a shared bottleneck can disable all paths; losing one berth alone cannot prove that. Storage damage is not categorically excluded, but must demonstrably disable every otherwise operable loading route. Record the full inventory before grading; silence about an alternative is not evidence that none exists. If pre-event operability cannot be reconstructed, the candidate cannot qualify as verified.

## Time, baseline and snapshot conventions

1. Record physical damage time `t0` in UTC with source precision. Let E be its UTC calendar date. Baseline days are E−28 through E−1:28 completed UTC days. Event-day throughput is excluded from both baseline and post-event daily comparison.
2. Proposed measured loss interval is the **first45 complete UTC days after E**, E+1 through E+45. Thus an October31 event is measured November1–December15, not October31–December14. This deliberately excludes a later-onset run and must be accepted and calibrated as such before registration. Original HAW19's dates do not move.
3. Freeze each vendor's full baseline snapshot at E+3,23:59:59UTC. Archive original response, query, vendor product/method version, capture time and hash. If a vendor has not supplied all28 days by that cutoff, baseline evidence is missing; no favorable later baseline substitution. This proposed delivery lag must be tested with real access before registration.
4. Retain daily source snapshots during the observation window. Grade post-event observations as available by the fixed evidence cutoff December21,23:59:59UTC; publish resolution December22. Archive revisions with their publication clocks. Later evidence is an annotation, not an automatic score rewrite. Baseline corrections remain separate from the frozen scoring baseline.
5. A matched fixture needs28 baseline plus45 post-event observations per vendor:73 paired full days spanning74 calendar dates because E is excluded. Demonstrate that both vendors support the required loading-day and as-of conventions; a current revised download alone does not prove historical snapshot availability.

## Volume allocation and agreement

The measured object is crude **loaded at the mapped terminal during each UTC day**, in barrels/day. Use documented vendor loading allocations for the same product universe and dates. Whole-cargo attribution to departure day, port calls, AIS silence, tanker capacity and national exports are not equivalent inputs. If only a cargo interval and total are available, do not invent a uniform daily allocation to make this contract pass; change the proposed measurement convention before registration and recalibrate it. Record density/conversion basis for any input supplied in tonnes; absent defensible conversion means missing data.

For vendor v, let B_v be its frozen28-day mean and Q_v,d its daily loading estimate. Daily shortfall D_v,d = B_v − Q_v,d. Require finite, nonnegative observed volumes and complete dates. Require both positive baselines to agree within1.5×: max(B_K,B_V)/min(B_K,B_V) <=1.5. This baseline agreement is an additional proposed readiness constraint, not wording inherited from original HAW19.

Each of the45 days must have **both D_K,d >=200,000 and D_V,d >=200,000 barrels/day**, and max(D_K,d,D_V,d)/min(D_K,d,D_V,d) <=1.5. Agreement is on **shortfalls**, not a ratio of remaining flows; all boundaries are inclusive. For example300k/200k qualifies numerically;301k/200k does not;200k/199,999 does not. Averaging the whole45-day loss cannot conceal a nonqualifying day. Do not replace a zero denominator with epsilon. A baseline below200k cannot support a200k nonnegative-flow shortfall.

Two vendor names do not establish independent evidence: document their underlying data and missing-data treatment. A zero is an observed/estimated zero only when the source explicitly supplies it; a missing day is never zero. Numerical agreement alone cannot establish physical damage or its cause. Independent dated imagery and named technical/operator evidence must support path disablement and damage attribution; AIS-derived silence alone is insufficient. Damage-attributed force majeure or a named restoration estimate of at least90 days is a separate required condition, not an alternative to the measured45-day loss.

## Missingness and resolution

Keep every candidate and every required condition, including disconfirming evidence. Before the cutoff, an unfinished run is pending observation. At the cutoff: a verified false required condition excludes that candidate; all conditions verified true make it qualifying; otherwise it remains unresolved. A vendor disagreement fails the **agreement condition**, not proof that physical loss did not occur. Do not promote an excluded or unmeasurable candidate into evidence that the broader world-state was safe.

Proposed successor resolves MISS if at least one candidate qualifies. HIT requires complete predeclared terminal coverage, dated in-window searches through the event window, a documented final search within the resolution window, and all candidates conclusively excluded on the contract. If none qualifies but any necessary coverage, identity, daily observation, causal/path condition or baseline is unresolved, resolve STUCK. Do not extend the evidence deadline silently. This uses publication-time evidence and deliberately risks STUCK when access is insufficient.

## Registration readiness

Required before registering: both usable data accesses; one matched73-observation fixture with verifiable snapshot clocks; complete terminal/product/path inventory; successful missing/zero/revision/boundary checks; probability calibration against a disclosed comparison set including known capacity-damage counterexamples; fresh disclosure audit; explicit agreement on this v2 time and loading convention. None is certified complete here. The suggested65% is an uncalibrated placeholder and must not enter the live ledger merely because these equations are specified.

**Disclosure update at closeout:** OSPREY reports an unnamed Novorossiysk oil-terminal fire dated September9 local, with no operator loading statement or measured loss. Preserve it in the contemporaneous disclosure inventory; this draft is not a registration and cannot treat the terminal as identified or the candidate as resolved.
