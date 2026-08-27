# RED — INDEPENDENT ADVERSARIAL REVIEW: Gate C Live-Interface Remediation

**Reviewer:** RED (independent; builder was PROME, separate session — separation honoured, builder gave pointers and mechanics only and declined to characterise the design)
**Date:** 2026-08-27 · **Authority:** Will, in-session, verbatim *"RED can take the kernel review - go ahead"*
**Object:** `f8560f2c0` (build) + `9b7945980` (docs) · `KERNEL/tools/live_shadow.py` · 207 tests · C6 rehearsal transcript
**Brief:** `KERNEL/GATE_C_LIVE_INTERFACE_REMEDIATION.md` §"Independent review brief"
**Scope honoured:** fixture/synthetic only · no live records inspected · nothing activated · no authority switch · nothing written into `KERNEL/`
**Timebox:** run to completion in one session (the review is the blocking step for the 8/30-31 window; it was not thinned for it)

---

## VERDICT

> ### **PROCEED to a fresh C7 packet and an attended pilot. Two MODERATE findings, neither blocking an ATTENDED single-`--apply` pilot. Finding 1 should be fixed before any UNATTENDED or extended use, and it is cheap.**

**The core security property holds and I could not break it.** Every attempt to reach a live write without a valid activation failed closed. **The single most important refusal — a leftover rehearsal document being used against the real repository — fails closed at two independent layers.**

**No claim in the remediation record was found false.** Every figure in it reconciles to the durable transcript verbatim, and the four modules it says are untouched are untouched.

---

## 1. WHAT I ATTACKED AND WHAT HELD

*Probes: `red_kernel_probe.py`, `probe2.py` (scratchpad; fixture harness `LivePlayingRepository` reused so nothing left fixture scope).*

| # | Attack | Result |
|---|---|---|
| A1 | Direct grant construction, wrong key | **REFUSED** |
| A3 | **Duck-typed fake grant → store** | **REFUSED** — `isinstance`, not structural typing. **The important one.** |
| A4 | No-grant store targeting live `KERNEL/` | **REFUSED** |
| A6 | Grant bound to root X → store at root Y | **REFUSED** |
| **P4** | **Clone-declared activation + REAL repo root supplied** | **REFUSED `LIVE_BINDING_MISMATCH`** ✅ |
| P2 | Window boundaries | **`[start, end)` exactly** — start inclusive, end exclusive |
| P3 | `revoked_at == window_start` | **REFUSED** (empty effective window fails closed) |
| P6 | `authorized_by` / `mode` / `repository` / `policy_version` / `schema_version` tampered | **REFUSED** each |
| P7 | Extra field · missing field | **REFUSED** (exact field-set equality) |
| G1 | `writer_id` = a *different valid* actor | **REFUSED `LIVE_BINDING_MISMATCH`** |
| G2 | Each of 4 pinned hashes zeroed | **REFUSED** each, before any write |
| G3 | `actors_path` repointed at another real policy file | **REFUSED** |

**Suite: 207 passed, 66 subtests, 8.5s — reproduces the claimed count exactly.**

**Transcript reconciliation: clean.** `f8560f2c0`, `79b533eb1…`, `5b534e579…`, event SHAs `15151286e93b…` / `fde0558c0e9f…`, `durable_outcomes=0` on the abort drill, `PASS: additions-only`, and the identical projection sha256 `87caea97d0ca…` before and after `.rw/` deletion **all appear in the transcript verbatim.**

**"Untouched" claim verified at the commit:** `gate_c_boundary.py`, `acceptance.py`, `audit.py`, `projection.py` — **zero lines changed.**

---

## 2. 🟠 FINDING 1 (MODERATE) — the operator's window is not enforced for two of four modes, and the grant carries no record of which validations passed

**Demonstrated end-to-end (probe G4):** an activation document whose window **closed on 2000-01-02** returns a complete, populated `LiveInputs` — live-bound grant, validated registry, custody load, submissions loaded from Git — with **no refusal at any layer**. The same document with `require_window=True` is refused (`LIVE_WINDOW_REFUSED`).

**Why it is not currently exploitable:** the two modes that skip the window (`--check-views`, `--audit-additions`) do not write. I verified this rather than assuming it — `write_views(check=True)` performs no `mkdir` and no write, and `FixtureResultStore.__init__` / `inventory()` are read-only.

**Why it is still a finding — three limbs:**
1. **`--check-views` opens a genuinely WRITE-CAPABLE store outside any window.** `FixtureResultStore(grant.kernel_root, live_grant=grant)` is the same object `--apply` uses. Read-onlyness comes from the **call path**, not the grant, the store, or the type.
2. **The grant cannot report its own provenance.** `LiveShadowGrant.__slots__` = `(repository_root, kernel_root, views_root, activation_id, writer_id, recorded_at)` — **nothing records whether the window was enforced when it was minted.** A grant minted with `require_window=False` is indistinguishable downstream from one minted inside the operator's window.
3. **The guard is a comment.** `authorize_live_activation`'s docstring says *"a write-capable caller must never pass `require_window=False`."* That is caller discipline. **Nothing enforces it, and `require_window` has ZERO test coverage anywhere in the suite** — so the design decision has no regression guard in either direction.

⚠️ **The disclosed limitation covers the DESIGN, not the HAZARD.** The record says read-only modes *"deliberately do not require the window."* True and reasonable. What is not disclosed is that this **mints a full write-capable capability outside the operator's authorization boundary** and relies on downstream call paths to stay read-only.

**Proposed fix — cheap, and it converts discipline into a guard:**
> Add `window_enforced: bool` to `LiveShadowGrant.__slots__`, set it at mint from `require_window`, and have `FixtureResultStore.publish` / `FixtureAcceptanceLock` **refuse when it is `False`.** Read-only modes keep working unchanged; a write attempt on a window-less grant fails closed at the type instead of by convention. **Two tests then write themselves** (a write-capable path must refuse a `window_enforced=False` grant; read-only modes must still pass).

**Why not blocking for the pilot:** `--apply` requires the window, and the pilot is one attended apply. **This is a hardening item, not a gate.**

---

## 3. 🟠 FINDING 2 (MODERATE) — the `writer_id` guard is correct and has no named test

Remediation item 4 states *"The activation `writer_id` must equal the custody policy's primary writer (PROME)."* **The guard exists and fires** — I verified it (G1/G1b: `writer_id` set to `RED` and to `SAM`, both `LIVE_BINDING_MISMATCH`).

⚠️ **But no test exercises it.** The suite covers `"empty writer"` (a *shape* check) and asserts `grant.writer_id == "PROME"` on the happy path. **Nothing tests a well-formed activation naming a different valid actor.** ⇒ **a correct guard with no regression protection** — precisely the class that dies silently in a later refactor.

**Fix: one test.** *(Related: `finding_test_the_guard_not_just_the_guarded`.)*

---

## 4. NOTES — not findings, recorded for accuracy

**N1 — "Each is a named test" is imprecise.** Several refusals are **subtest cases** inside two omnibus tests (`test_document_shape_and_content_failures_refuse`, `test_window_not_started_closed_and_revoked_refuse`); the run reports 66 subtests. **The coverage is real; the wording overstates its granularity.** Prefer *"each is a named subtest case."*

**N2 — the grant is minted BEFORE pin verification.** `authorize_live_activation` mints on document + clock + root binding; the four hash pins and the custody-writer check happen afterward in `prepare_live_inputs`. **Safe in the current call path** — nothing writes in between, and all of them refuse before any write (G2/G3). Recorded because it is the same class as Finding 1: **the grant's existence is not evidence that full validation passed.**

**N3 — the `_MINT_KEY` disclosure is ACCURATE.** `from live_grant import _MINT_KEY` mints a grant (A2). This is exactly what the record discloses — *"not cryptographic protection against a malicious direct writer,"* cooperative-actor threat model, design decision 20. **No overclaim.** And the guard that matters more held: a duck-typed fake is refused (A3).

**N4 — read-only modes need less than they take.** `--audit-additions` uses only `grant.repository_root`; `--check-views` only `kernel_root`/`views_root`. **Neither needs write capability at all** — a narrowed read capability would remove Finding 1's root cause rather than guard it. Offered as a design option, not a requirement.

---

## 5. ⚠️ AGAINST MY OWN REVIEW — my first probe run produced FOUR false REFUSALs

My initial probe passed `now="2026-08-27T12:00:00Z"`. The canonical format is `%Y-%m-%dT%H:%M:%S.%fZ`, so **my timestamps were rejected as malformed and four probes reported `REFUSED` for my own bad input rather than because a guard fired** — including **P4, the single most important refusal in this review.** I caught it only because the baseline "valid activation" also refused, which it should not have.

⇒ **A reviewer who wrote only attack cases and no positive control would have published four false passes, on the exact claim that matters most.** `[[finding_instrument_reports_clean_against_the_wrong_reference]]`. **Every REFUSED in §1 is from the corrected run and is paired with a passing baseline.** *(A second self-caught error: my "after window end" case used 2099 against a 2000-2100 fixture window — inside it. Struck; the real end-exclusivity evidence is P2b.)*

---

## 6. WHAT THIS REVIEW DOES NOT COVER

- **No live records inspected, nothing activated** — per standing constraint. I therefore **cannot** attest to anything about live repository state.
- **I did not re-run the disposable-clone rehearsal end to end.** The brief lists it. I reconciled the **durable transcript** against the record instead and found it clean; a full re-run would be strictly stronger and I am declaring the gap rather than implying coverage.
- **Trusted-history reachability** beyond resolving a supplied full commit — the declared checkpoint-12 limitation, unchanged and not re-examined here.
- **The C7 packet's stale SAM-33 pins** — held as context per PROME's handoff, not a finding target; a fresh packet re-pins regardless.

---

## 7. RECOMMENDATION

1. **Proceed** to a fresh C7 packet and Will's activation ruling for **one attended pilot**.
2. **Before the pilot** (both cheap, neither structural): add the **Finding 2** test; and add the two **Finding 1** tests even if the `window_enforced` slot itself is deferred.
3. **Before any unattended or extended use of this interface:** implement Finding 1's `window_enforced` guard, or N4's narrowed read capability.
4. **Correct N1's wording** in the remediation record.

**Nothing I found changes the shape of the design.** The single-door architecture, the fail-closed ordering, and the root binding are sound, and the record is honest — including where it discloses its own weaknesses.

— **RED**, 2026-08-27 · packet to PROME, surfaced to Will

---

# ⚑ DELTA RE-REVIEW — commit `67136c509` (builder's response to findings 1 & 2)
**RED, 2026-08-27 · re-review requested by PROME before cutting the fresh C7 packet**

> ## **PASS WITH ONE RESIDUAL. The fix is real and correctly fail-closed — and it closed ONE of the two durable-write paths. The views path still rests on exactly the call-path discipline Finding 1 was about.**

## D1 — What the fix does, verified not trusted

| Check | Result |
|---|---|
| `window_enforced` in `__slots__`, **default `False`** | ✅ **Fail-closed confirmed** — a grant built without the kwarg reports `False` (probe R4) |
| Set at mint from `require_window` | ✅ unenforced grant reports `window_enforced=False` (R0) |
| **`FixtureResultStore.publish` refuses an unenforced grant, before document validation** | ✅ **REFUSED** (R1) — guard sits above `_validate_result_document`, so it fires on any document |
| Suite | ✅ **211 pass**, 66 subtests, from 207 |
| Finding 2 test (`writer_id` ≠ custody primary) | ✅ added |
| `require_window` coverage, both directions | ✅ added |
| N1 wording | ✅ corrected |

**Both of my findings are addressed on the path the fix targets, and the default-False choice is the right one — a grant that cannot prove enforcement is refused rather than trusted.**

## D2 — 🟠 RESIDUAL (MODERATE, still not blocking): the VIEWS write path is unguarded

**The guard is in `writer.py` only. `render.py` and `locking.py` received zero lines.**

**Demonstrated (probe R2/R2b), with an activation whose window closed `2000-01-02`:**
```
R1 store.publish                      REFUSED   <- fix works
*** R2 render_live_views(check=False) REACHED — views written:
       CALIBRATION.tsv, EXCEPTIONS.md, OPEN_QUESTIONS.md, RESOLUTION_QUEUE.md
*** R2b render.write_views(check=False) REACHED directly at <granted>/KERNEL/views
```

⇒ **Four registered view files were durably written under the granted root using a grant whose window expired twenty-six years ago.**

**Why this is the same finding and not a new one.** `KERNEL/views/` is **one of the four registered generated surfaces named in the root Git carve-out ④** — a durable artifact, not scratch. The builder's own new code comment states the intent exactly: *"read-onlyness must not rest on the call path alone."* **For views, it still does.** Only `--apply` calls `check=False`, and `--apply` requires the window — so the CLI is safe **by call path**, which is the precise property Finding 1 said should not be load-bearing.

⚠️ **And it is untested: zero of the four new tests touch `render_live_views` or `write_views`** (grep count 0). The guarded path gained a regression test; the unguarded one has neither guard nor test.

**Fix — the same three lines, one layer over:** refuse in `render_live_views` when `check=False` and `grant.window_enforced` is `False`. It already receives the grant. *(Cleaner still: push the check into `write_views` when a grant is supplied, so no future caller can route around it.)*

**Class note, recorded because it is the general lesson and not a criticism of the response:** a partial guard **relocates** a constraint and can read as removing it — the events path is now enforced by type, the views path by convention, and the record says Finding 1 is implemented. `[[finding_a_fix_can_relocate_a_constraint_and_report_it_removed]]` · `[[finding_a_correction_pass_is_unreviewed_work]]`.

## D3 — Not claimed
**The lock path is UNVERIFIED, not cleared.** My probe used a wrong method name (`hold`) and returned an `AttributeError`, which is my error and no evidence about `FixtureAcceptanceLock`. `locking.py` received no guard; whether an unenforced grant can acquire a lock (a `.rw/locks` write — disposable, hence lower severity) is **untested by me and I am not asserting either way.**

## D4 — Sequencing question: **I AGREE with the deferral, and the delta supplies a new reason**
PROME deferred the narrowed-read-capability alternative to post-pilot because it re-cuts the store/lock acceptance surface just reviewed. **Correct, and D2 strengthens it:** this delta shows that even a *small, well-aimed* guard left a second path open. **A larger surface re-cut immediately before a pilot would carry more of that risk, not less.** Do it post-pilot with its own review.

## D5 — REVISED RECOMMENDATION
1. **Add the views guard + its test before the pilot.** Three lines and one test, in code already under review — the cheapest possible closure and it removes the last call-path dependency from the durable-write surface.
2. **Then cut the C7 packet.** With that in, Findings 1 and 2 are closed by mechanism rather than by convention.
3. **If Will prefers to run the pilot without it:** still acceptable — `--apply` requires the window and the pilot is one attended apply — **but the record should say the views path is convention-guarded**, not that Finding 1 is fully implemented.
4. Narrowed read capability: **post-pilot**, agreed.

**`CHG-RED-050` remains ACTIVE pending the views guard.** Everything else in the delta passes.

---

# ✅ RESIDUAL CLOSE + LOCK PROBE — commit `ec254da22` · RED, 2026-08-27

> ## **CHG-RED-050 CLOSES on the durable-write surface. Both durable chokepoints now refuse an unenforced grant, verified. I re-probed the lock rather than let it ship declared-unverified — it is now VERIFIED and it is a LOW-severity known gap, not an unknown.**

## R1 — The views guard works, and the read mode survives

| Probe | Result |
|---|---|
| `render_live_views(check=False)` under an unenforced grant | **REFUSED** — and `views_root` **does not exist** afterward (nothing written, no directory created) |
| `write_views(check=False, live_grant=g)` direct | **REFUSED** |
| `check=True` still permitted | ✅ returns 4 findings, read/compare preserved |
| Suite | **212 pass** |

**Implementation is the stronger of the two options I offered** — the refusal lives in `write_views`, the deepest grant-aware layer, `require_live_grant`-typed, so `render_live_views` cannot be routed around by a future caller. **Correct choice.**

⇒ **Both durable-write chokepoints are now enforced by type rather than by call path: `store.publish` (events/receipts) and `write_views` (registered views). That was the whole of Finding 1.**

## R2 — 🔵 LOCK PATH: PROBED WITH THE CORRECT API. It acquires under an unenforced grant.

My earlier `AttributeError` was my own wrong method name; the real API is a context manager. Re-run:

```
*** L1 lock ACQUIRED under unenforced grant; held=True  lockdir_exists=True
```

**`FixtureAcceptanceLock` does NOT honour `window_enforced` — it acquires and creates `.rw/locks` under a grant whose window closed in 2000.**

**Severity: LOW, and I am not inflating it.**
- **`.rw/` is disposable by design** — the C6 rehearsal proved a byte-identical projection rebuild after deleting it entirely (step 8, sha256 `87caea97d0ca…` before and after).
- **A lock file is not a durable record** and sits **outside the protected additions-only perimeter** (`KERNEL/shadow/events/`, `KERNEL/audit/commands/`).
- **Nothing durable follows from holding it** — both durable paths now refuse independently.

⇒ **Recommend the C7 packet record this as a VERIFIED LOW-severity known gap, not as reviewer-unverified.** A verified small gap is better evidence than an unverified silence, and it costs the packet nothing to say so precisely. **Optional post-pilot: extend the same guard to the lock for consistency.**

## R3 — Design note, NOT a finding and explicitly not a blocker

`write_views`'s guard is **opt-in by parameter** (`live_grant: object | None = None`), so calling it without passing the grant one holds still writes (probe V3). **This is the same cooperative-actor posture as the disclosed `_MINT_KEY` limitation, not a new class** — the live interface itself always passes the grant (V1 proves it), and deliberately withholding a grant you hold is the disclosed threat model, not an accident.

**Stronger form, offered for post-pilot only:** key the requirement on the **destination** rather than the parameter — if `output_dir` resolves under a granted root, require a grant. **Not requested before the pilot.**

## R4 — MY WORD, as asked

- **`CHG-RED-050` → RESOLVED.** Findings 1 and 2 are closed **by mechanism**, verified by probe, not by assertion.
- **No hold requested.** Cut the fresh C7 packet.
- **Declared gaps for the packet's coverage section, corrected:** ① full disposable-clone rehearsal **not re-run by RED** (transcript reconciled instead) — stands as declared. ② lock path — **no longer "unverified": VERIFIED, acquires under an unenforced grant, LOW severity, `.rw/`-scoped, both durable paths refuse independently.**
- **Post-pilot items, agreed and not blocking:** narrowed read capability · lock guard for consistency · destination-keyed view guard.

**The delta was implemented as specified, the harder of the two options was chosen, and the residual is closed. Nothing further owed from my side before Will's ruling.**
