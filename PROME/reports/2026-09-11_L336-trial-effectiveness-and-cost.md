# L336 C4 — ARGUS trial run 1: effectiveness and cost

**Will's instruction (2026-09-11 19:07 ET):** *"Then run the existing trial and report effectiveness and cost."*
Run 1 of the four-closeout trial registered at DOCKET L333, graded 9/19 at the L291 sitting.

## Effectiveness — run 1

| | |
|---|---|
| Scope audited | OWNED 38 · SHARED 89 · UNATTRIBUTED 0 · EXCLUDED 190, against recorded baseline `9132969a0` |
| Returned | **❌ 5 · ⚠️ 6 · ✅ 26** across 31 claims tested |
| ❌ **applied** | **5 of 5** — every one was a real defect; none declined |
| ⚠️ to residue | 6, declared |
| Trial baseline (L333) | 0 caught before commit vs **7** caught after, on 2026-09-11 |

**The finding that justifies the instrument on its first run:** ARGUS found **acceptance condition A4 still
violated**, with a live instance, *after* an external reviewer had already found it once and PROME had "fixed"
it twice. Commit `888924d2e` put a PROME-authored packet body —
`AGENTS/FALCON/inbox/data/2026-09-11_FIRMS_VIIRS_…csv` — in a routing lane under a name carrying no
`from-PROME` hint. Both of PROME's fixes were **filename keys**, which is the precise mechanism A4 exists to
forbid. The rule is now unconditional: every inbox path at every depth is SHARED, and a structural test asserts
no manifest pattern may contain a filename hint.

It also caught that **ARGUS's own memory file — the ONE file it reads whole — still said "committed since",**
six hours after the F1 repair changed the other surface. A one-sided edit to a rule, found by the agent the
rule governs.

## Cost — measured, all three runs this session

| Run | Purpose | Tokens | Tool calls | Wall clock |
|---|---|---:|---:|---:|
| Independent review 1 | the F1 repair candidate | 111,723 | 21 | 2m 45s |
| Independent review 2 | the L336 final candidate (C2) | 126,856 | 34 | 3m 00s |
| **ARGUS trial run 1** | this session's whole output | **119,084** | **30** | **2m 08s** |
| | **total** | **357,663** | **85** | **7m 53s** |

**Per defect found: ~21,000 tokens** (17 ❌ across the three runs). **Per defect that reached a contract
violation: ~45,000.**

## Three honest caveats, because the number is worthless without them

1. ⚠️ **RUN 1's PENDING HALF WAS EMPTY.** `CLOSEOUT.md` 1f says run ARGUS *before* the closeout commit. Run 1
   executed after most of this session's commits, so all 81 scope entries were `committed` and the pending
   lane — the thing F1 existed to expose — was not exercised. **Run 1 therefore does not measure the
   pre-commit case at all.** Recorded in the RUN-LOG row rather than smoothed over.
2. ⚠️ **RUN 1 AUDITED THE SESSION THAT BUILT IT.** Unusually favourable conditions: a large, defect-dense,
   freshly-churned scope. Runs 2–4 on ordinary closeouts will find less, and a falling count is the expected
   shape, not a regression.
3. ⚠️ **A4's no-drop guarantee roughly TRIPLES the audit surface** — 89 SHARED against 38 OWNED, of which 78
   are inbox paths and only 14 carry a `from-PROME` hint. ARGUS is instructed to read SHARED paths. That is
   the declared **price** of the honest failure direction (visible-and-correctable over invisible), and it is
   reported as a price, not a free win. If runs 2–4 show the SHARED lane producing no findings, the right
   response is to narrow it *deliberately*, with a stated limitation — not to let it quietly rot.

## What run 1 does NOT establish

That ARGUS beats the baseline. One run, on its own construction site, with the pending half untested, against
a baseline of 7 measured over four closeouts. **The comparison the 9/19 sitting grades is not yet computable.**
Runs 2–4 must be ordinary Standard+ closeouts, run BEFORE the commit, or the trial measures nothing.
