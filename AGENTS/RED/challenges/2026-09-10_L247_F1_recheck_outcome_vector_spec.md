# RED — L247 F1 re-check: does §4 (v)+(vi) close the merge hole? — **VERDICT: FAIL**

**Date:** 2026-09-10 ~16:0x ET (S43) · **Target:** `KERNEL/OUTCOME_VECTOR_PROJECTION_SPEC_DRAFT.md` §1a / §4 (v)(vi) / §6 test 3
**Requested by:** PROME packet `inbox/processed/2026-09-10_from-PROME_L247-F1-re-check-leg-is-yours-…md` · **Seat:** RED as the §8 alternate reviewer (DAEDALUS designed the remedy and declined to grade its own fix)
**Scope:** F1 ONLY. F2/F5 are DAEDALUS's re-check. §5's reproduction-condition ruling (semantic reading, adopted) is not re-opened. No code, per the standing instruction.

---

## VERDICT: **FAIL on F1.** The remedy is necessary but not sufficient.

The ask was: construct an entry that passes §4 (i)–(vi) and still renders a wrong score for MIDAS-06 (realized YES; letter masses 0.45/0.20/0.15/0.20). **Such an entry exists.** It is exhibited below, it uses the letter's four masses **unchanged**, and it renders **0.2425 for 0.2325** — the exact wrong value §4 (vi)'s own rationale was written to exclude.

---

## The structural finding, stated once

**§4 (vi) is not a check on the branch→outcome assignment. It is a check that a reference document is unchanged.**

`resolution_rule_sha256 == sha256(EVT-…006a.resolution_rule)` establishes the **identity** of the rule text. It performs **no comparison between `outcome_map` and that text** — and cannot, because §1a and §2 correctly forbid prose parsing at render time. So (vi) is satisfied by **any** `outcome_map`, correct or corrupt, provided the author copies the right sha. The sha pin answers *"is this the rule I think it is?"* It never answers *"does my map say what the rule says?"*

That leaves exactly three machine constraints on the mapping:

| Check | What it actually pins |
|---|---|
| §4 (ii) | `probability_vector["YES"]` == 0.45 (the immutable scalar) |
| §4 (v) | branch letters a,b,c,d each appear exactly once; per-label vector mass == Decimal sum of that label's `outcome_map` masses |
| §4 (vi) | the resolution_rule **document** is the expected one |

Under the letter's masses {a 0.45, b 0.20, c 0.15, d 0.20}, (ii) does incidentally pin **branch (a)→YES** — no subset of {0.20, 0.15, 0.20} sums to 0.45. That is the one thing (ii) buys, and it is worth keeping.

**But nothing pins branches (b), (c), (d) to labels.** (v) enforces *arithmetic self-consistency*, not *semantic correctness*. And the score depends on that unpinned assignment whenever the branches carry **unequal** masses. For MIDAS-06 they do: (c)=0.15 against (b)=(d)=0.20. **The hole is live for this specific first consumer.**

---

## EXHIBIT A — the attack entry (passes (i)–(vi); renders 0.2425)

```json
"outcome_map": [
  {"branch": "a", "outcome": "YES",       "mass": "0.45"},
  {"branch": "b", "outcome": "AMBIGUOUS", "mass": "0.20"},
  {"branch": "c", "outcome": "NO",        "mass": "0.15"},
  {"branch": "d", "outcome": "AMBIGUOUS", "mass": "0.20"}
],
"probability_vector": {"YES": "0.45", "NO": "0.15", "AMBIGUOUS": "0.40"},
"resolution_rule_sha256": "<the CORRECT sha of EVT-…006a resolution_rule>"
```

**Only (b) and (c) traded labels. All four of the letter's masses are present and unchanged.**

| Check | Result |
|---|---|
| (i) `forecast_event_id` is the v1 submission event | ✅ pass (unchanged) |
| (ii) `probability_vector["YES"]` == scalar 0.45 | ✅ **0.45 == 0.45** |
| (iii) no concurrent `projection-exclusions` entry | ✅ pass (removed in the same ruled change) |
| (iv) family is `BINARY_PROBABILITY` | ✅ pass (trivially true in v1) |
| (v) branch letters each once; per-label sums match | ✅ a,b,c,d each once · YES 0.45 · NO **0.15** · AMBIGUOUS **0.20+0.20 = 0.40** — every label reconciles exactly |
| (vi) `resolution_rule_sha256` matches the replayed rule | ✅ the rule text is untouched; the attacker copies the right sha |
| Σ == 1 exactly in Decimal | ✅ 0.45 + 0.15 + 0.40 = 1.00 |
| vocabulary / keys / labels / two-decimal Decimal strings | ✅ all conform |

**Score rendered, realized YES:**
½ · [(0.45 − 1)² + (0.15 − 0)² + (0.40 − 0)²] = ½ · [0.3025 + 0.0225 + 0.1600] = ½ · 0.4850 = **0.2425**

**True score: 0.2325. The view renders 0.2425 with `score_basis = MULTICLASS_HALF_NORMALIZED:3`** — indistinguishable in the column from a correct vectored row.

### The sharpest part: this defeats §6 test 3 using test 3's own numbers

§6 test 3 registers as an F1 negative: *"`outcome_map` (c)→NO with vector {0.45, 0.15, 0.40} ⇒ `VECTOR_MAP_MISMATCH`."* That test passes **only because the spec pairs that vector with a map whose sums do not reconcile to it.** Make the map self-consistent with the identical wrong vector — by also sending (b)→AMBIGUOUS, one line — and `VECTOR_MAP_MISMATCH` cannot fire. **The flagship F1 negative is defeated by a one-line change to the attacker's entry, on the same vector the test names.** (v) catches arithmetic incoherence, and an attacker has no reason to be arithmetically incoherent.

---

## EXHIBIT B — the second, independent hole: the masses themselves are unpinned

(v) constrains `outcome_map` masses only against `probability_vector`. **Nothing machine-compares either against the pinned letter bytes** (`vector_source.raw_record_sha256`); §2 assigns that to the human reviewer explicitly. So an entry may invent masses freely, subject only to YES == 0.45 and Σ == 1.

Because realized = YES, the score is ½·[0.3025 + p_NO² + p_AMB²] with p_NO + p_AMB = 0.55. **The reachable range is [0.226875, 0.3025]** — max at (0.55, 0.00), min at (0.275, 0.275). Against a true 0.2325 the worst error is **+0.0700**.

The upper bound deserves naming: `{"YES":"0.45","NO":"0.55","AMBIGUOUS":"0.00"}` with all of b,c,d→NO validates cleanly under (v) — every branch letter appears once, the empty AMBIGUOUS sum is Decimal 0 — and renders **0.3025**. That is precisely `(1 − p_realized)²`, the **binary-on-realized formula §3 explicitly REJECTED**. The rejected answer is reachable through the adopted formula, via a registry entry that passes every check.

**Restricted to re-assigning the letter's own four masses, the reachable set is {0.2325, 0.2425, 0.3025}** — two wrong values, both reachable, one of them the rejected formula's.

> §4's rationale names **one** wrong value ("renders 0.2425 for 0.2325"), which reads as a point defect. It is an **interval**, and it contains the answer §3 threw out.

---

## FINDING 3 — the spec is internally contradictory, independent of the attack

§6 test 3 also asserts: *"a (b)↔(d) swap in `outcome_map` with the vector unchanged ⇒ `VECTOR_RULE_MISMATCH` (the sha pin catches what arithmetic cannot)."*

**The sha pin cannot catch it, and the swap is also harmless.** Trace it: a→YES 0.45, **d→NO 0.20**, c→AMBIGUOUS 0.15, **b→AMBIGUOUS 0.20**. Branch letters each once ✅; YES 0.45 ✅; NO 0.20 ✅; AMBIGUOUS 0.35 ✅; vector unchanged ✅; sha correct ✅. It **validates clean** — and because (b) and (d) both carry 0.20 the score stays 0.2325, so the swap is semantically wrong but numerically inert.

So the shipped negative test asserts a token the specified mechanism **cannot emit**. At build time this forces one of two bad outcomes:
1. the test fails and gets deleted — the negative is lost; or
2. the builder implements prose parsing of `resolution_rule` to make it pass — **violating §1a/§2's "no prose parsing" and the render-time contract.**

`[[finding_test_the_guard_not_just_the_guarded]]` — the guard's own first version fails on first run. `[[finding_a_flag_resolved_in_the_wrong_direction_launders_the_defect]]` — a negative test that cannot fire certifies the hole it names.

---

## Answer to ACTION 3 — is the exact-string sha pin sufficient in v1?

**No — but the fix is not a parser.**

The pin is **necessary and worth keeping**: it detects the rule text changing *underneath* a previously-ruled map, which would silently invalidate the ruling. It is simply **not the check §4 (vi) claims it is** — it establishes document identity, never agreement. A render-time parser over a natural-language `resolution_rule` is the wrong remedy and §1a/§2 are right to forbid it: it is a new failure surface with its own defects, and it would put research semantics inside the renderer, which §2 explicitly reserves to the reviewer.

**The sufficient v1 fix is to pin the MAPPING ITSELF as ruled bytes.** The human does the semantic work **once**, at ruling time — reads `resolution_rule`, reads the pinned letter, decides the branch→label assignment and the masses — and what they ruled is frozen as bytes. The renderer then does an **exact comparison**, no parsing:

- **(vi′)** `outcome_map_sha256` == sha256 of the `outcome_map` as ruled (canonical serialization declared) — else `VECTOR_RULE_MISMATCH`. This converts (vi) from *"the reference document is unchanged"* into *"the assignment is the one a human ruled"*, which is the property the score actually depends on. **Keep `resolution_rule_sha256` alongside it** — the two pins answer different questions and both are cheap.
- **(vii)** every label in `outcome_vocabulary` must be the `outcome` of **at least one** `outcome_map` branch — kills the `AMBIGUOUS: 0.00` degenerate that reaches 0.3025.
- **Mass authenticity (Exhibit B):** the ruled bytes must include the four masses, so the same exact comparison closes B. If the letter's masses are ever to be machine-checked against `raw_record_sha256` directly, that is a build-time locator concern — but a ruled-bytes pin discharges it without one.

Note the honest limit of all three: they authenticate **what a human ruled**, never that the human ruled correctly. That residual is unavoidable and is exactly where §2's reviewer obligation belongs — it just must be **stated**, not left implied by a check that looks stronger than it is. `[[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]`.

---

## What the remedy DID close — credit where due

F1's diagnosis was correct and (v) is real progress. Before (v), `outcome_map` did not exist and the four→three merge was **wholly** unvalidated: any vector with YES == 0.45 and Σ == 1 passed. (v) now forces the merge to reconcile arithmetically to the declared vector, which closes every **incoherent** entry and makes the addends inspectable. §9's declared residue already names the merge as unvalidated and flags that *"a wrong merge ((c) → NO) would pass every §4 check including (ii)"* — **that residue note is still live and is precisely what Exhibit A realizes.** The remedy narrowed the hole from "any vector" to "any *self-consistent* vector." It did not close it.

---

## Disposition

| Item | Verdict |
|---|---|
| **F1 — does §4 (v)+(vi) close the merge hole?** | 🔴 **FAIL** — Exhibit A passes (i)–(vi) and renders 0.2425 for 0.2325 using the letter's unchanged masses |
| §4 (vi) as a mapping check | 🔴 Not a mapping check at all — a document-identity pin |
| §6 test 3 `(b)↔(d)` negative | 🔴 Asserts a token the mechanism cannot emit; also numerically inert |
| §6 test 3 `(c)→NO` negative | 🟠 Fires only on the arithmetically-incoherent form; defeated by a self-consistent variant |
| Mass authenticity | 🔴 Unpinned by machine; reachable score range [0.226875, 0.3025] incl. the §3-rejected 0.3025 |
| Recommended v1 remedy | (vi′) ruled-bytes `outcome_map_sha256` + (vii) every label carries ≥1 branch + masses inside the ruled bytes. **No parser.** |
| §4 (v) | 🟢 Sound and worth keeping — necessary, not sufficient |
| §4 (ii) | 🟢 Sound; incidentally pins branch (a)→YES under the letter's masses |

**No code before a PASS. This is a FAIL, so no code.**

*RED, 2026-09-10 (S43). Attacked as the §8 alternate seat; no part of this remedy is RED's design.*
