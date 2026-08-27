# LIQUID — Gate C Increment 2 STAGED SUBMISSIONS (NOT live commands)

⛔ **These are NOT submitted and are NOT live commands.** A LIQUID command exists only at
`AGENTS/LIQUID/outbox/kernel/submissions/` under carve-out ④, and that path is **inactive
until Will's window ruling**. This directory is a planning staging area so the activation
document can pin exact sha256 values *before* the ruling without creating live commands.
At ruling time LIQUID copies these exact bytes to its own submission path and commits them
itself (C1: the submitting agent authors and commits its own immutable command file).

**Generated:** 2026-08-27 · `submitted_at=2026-08-27T20:55:00.000000Z`
**Source commit pinned in `native_refs`:** `8326b5ce15fc31ca4ddb11298c2f021dc70fc246`
(verified: resolves, is an ancestor of `origin/master`, and the LIQ-04 row at that commit
is byte-identical to the row at HEAD — no drift).

| file | type | sha256 | bytes |
|---|---|---|---|
| `CMD-01a044fc-e591-73e8-a74d-2f675abc09a0.json` | RegisterQuestion | `8f5d1e5da53e02096e64b738a08feb89a6e79dfbd95cfa2f0d92bbf50b53f37c` | 6540 |
| `CMD-01a044fc-e591-769e-8199-994a92e9fafb.json` | SubmitForecast | `583e9f31194e9ab5ecae71f7b10a8620eaccd6fef56158027d054c908c76d344` | 1839 |

**Byte-freeze form:** `json.dumps(sort_keys=True, separators=(",",":"), ensure_ascii=False)`,
no trailing newline — matches the C7 rehearsal bytes.

## What is submitted, and why only ONE question

**LIQ-04 only** — *"US BSL new-issue CLO AAA monthly average exceeds SOFR+150 in any month",*
H2 2026, registered 2026-07-01 at 25%.

The ask was 1–3 predictions. **LIQUID has exactly one that qualifies.** Of six registered
rows, LIQ-01/03/06 are ACHIEVED, LIQ-02 MISS, LIQ-05 VOID — all resolved history, excluded
by the increment's no-backfill rule. LIQ-04 is the only OPEN forward-resolving row.
**One real question beats three padded ones**, and nothing was manufactured to fill a quota.

## The access check this forced, and its result

LIQ-04 carried an **unresolved gradeability flag I wrote on 2026-08-20 and had not acted on**:
its resolver names a *PitchBook LCD monthly-average series whose reachability from this box
was never established*, with my own note that if it is subscription-gated the prediction
*"silently NO-VERDICTs at 12/31 with no one having decided that."*

**Check performed 2026-08-27. Result: the LCD monthly-average series is NOT retrievable as a
series** — PitchBook publishes articles citing LCD figures, not a machine-readable feed.

**That did not kill the question, because its predecessor shows the resolvable path.** LIQ-03
was graded on a documented multi-source procedure — SEC 8-Ks as primary (Diameter accessions
`0001193125-26-129150`, `-196327`) plus named trade press. So LIQ-04 is registered the way
SAM-33 is: a `negative_search_procedure` over named reachable sources, with an SEC-EDGAR
**fallback construction** that builds a month's average deal-by-deal and must label the result
`CONSTRUCTED`. **The gating is disclosed in `ambiguity_rule` at registration rather than
discovered at resolution.**

## Two spec decisions worth review

1. **`closes_at` is 2027-02-15, NOT 2026-12-31.** The measured interval is fixed at Jul–Dec
   2026, but December's monthly average does not publish until mid-January. A deadline equal
   to the measurement window's end would be **ungradeable on its own resolution date** — the
   T+1 grade-date defect, n=3 on this desk (KB-LIQ-096; the T6 trap; PROME's 8/27 class
   ruling). Applied prospectively here. `resolution_condition` states explicitly that
   `closes_at` extends only for publication and does **not** extend the measured interval.
2. **Segment exclusion is binding and is the whole point.** MM/PC CLO AAA is excluded and
   never qualifies however wide it prints. LIQ-03 resolved ACHIEVED *at the letter* on MM/PC
   tail prints (Diameter senior AAA S+170) while the BSL benchmark never exceeded ~S+125 in
   the same stress — a within-AAA bifurcation of >60bp, registered as **KB-LIQ-065**. LIQ-04
   is the benchmark arm that letter failed to separate, so the exclusion is load-bearing.

**Forecast submitted unchanged at 0.25, `information_as_of` 2026-07-01, `INITIAL`** — the
registered forecast, deliberately not re-marked at submission time. Today's tape corroborates
it (2026-08-26 still shows stress in the tail, senior benchmark calm), so there was no honest
reason to move it and re-forecasting under cover of a registration would be the wrong move.

**Independent verifier: RED** (≠ owner, ≠ resolver). Chosen because RED is already in the
actor registry, has verified before (SAM-33), and is independent of my CLO work. REGINALD was
the domain-plausible alternative but is itself a submitting desk this increment and a new
registry addition.

## Validation run before commit

Both files validate against `KERNEL/schemas/command.schema.json` plus their payload schemas
(`question`/`forecast`), and pass 13 cross-checks the schema cannot make — including
proposer≠verifier, stream-id derivation, `depends_on` linkage, the `closes_at` trap guard,
native-ref sha256 reproduction from the pinned commit, and perimeter-family legality
(only `RegisterQuestion`/`SubmitForecast` used; no excluded family touched).
