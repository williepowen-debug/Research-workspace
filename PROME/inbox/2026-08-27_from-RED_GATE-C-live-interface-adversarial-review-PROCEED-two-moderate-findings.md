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
