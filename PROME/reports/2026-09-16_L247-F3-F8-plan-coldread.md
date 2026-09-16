# L247 F3/F8 plan cold read — 2026-09-16

Verdict: **FIX-THEN-IMPLEMENT** the specification amendment. This is the independent PLAN read, not DAEDALUS/RED approval of §1–§6 and not discharge of RED F1. No target specification or docket edits made by this reader.

## Blocking findings

| Claim | Exact artifact | Verification command | Observed result | Proposed change |
|---|---|---|---|---|
| VERIFIED — adding normalization changes existing test outcomes; the consequential-edit plan omits those dependencies. | `PROME/plans/2026-09-16_L247-F3-F8.md`, consequential edits; `KERNEL/OUTCOME_VECTOR_PROJECTION_SPEC_DRAFT.md` §6 test 3 and §4 honest limit | `sed -n '/## 6\./,/## 7\./p' KERNEL/OUTCOME_VECTOR_PROJECTION_SPEC_DRAFT.md`; exact `fractions.Fraction` comparison of source `[.45,.20,.15,.20]` and modified outputs `[.45,.55,0,0]` | Independent counterexample: new MIDAS NONE entry with only output masses, vector and digest changed to the existing 0.3025 honest-limit fixture refuses at (v), because output masses differ from source masses. Existing §6 asserts PASS. Its one-mass-edited stale-digest negative also encounters (v) before (viii). Omitted-branches fixture must omit source keys too and make the reduced source/output declaration self-consistent if it is to reach (vii). | Add a consequential §6/§4 fixture reconciliation. Honest-limit attacks must edit source masses and normalization consistently as well as output/vector/digest, explicitly retaining their falsified-source/reviewer-only character. To isolate stale digest, use an otherwise self-consistent mutation of the four hashed fields; test output-only edits separately as MAP_MISMATCH. Make omission fixture internally consistent before asserting its first token. |
| VERIFIED — existing author-rounding permission conflicts with the new exact source-transcription rule. | Target specification §4 Entry; plan proposed §1c and consequential edit 1 | Read §4 Entry alongside proposed §1c | §4 currently says the author rounds the letter's approximate masses to declared precision. New §1c requires pinned literal transcription and forbids automatic rounding, permitting only named exact normalization. Leaving both creates competing instructions about forming entry masses. | Replace the existing parenthetical with a §1c pointer: transcribe source literals at source precision, and derive output masses only by the declared method. |

## Verified acceptance properties

| Claim | Exact artifact | Verification | Observed result | Proposed change |
|---|---|---|---|---|
| VERIFIED — normalization examples have the asserted arithmetic. | Plan acceptance conditions | Python standard-library Fraction over the displayed decimal strings | .99 example gives 9/20, 11/60, 11/60, 11/60; .98 gives 9/20, 11/53, 143/1060, 11/53; .80 gives 2/5, 3/10, 3/10. First two have nonterminating outputs; third terminates. | None. |
| VERIFIED — F8 has an existing carrier and the proposal preserves historical metadata. | `PROME/DOCKET.tsv` physical L314; plan edits 5–6 | `sed -n '314p' PROME/DOCKET.tsv` | Existing PENDING schema-v2 row has the stated owner and session-keyed due field. Planned bridge disposition permits historical binary metadata to survive native-family activation and forbids metadata on native-family questions. No duplicate row needed. | None. |
| VERIFIED — MIDAS NONE does not change scoring. | Plan §1c example; target §3 | Exact fractions for source sum and half-normalized score | Source masses sum to 1; unchanged label vector .45/.20/.35 yields .2325. | None. |

## Declared advisory residue

2026-09-16: The plan's opening scope says the specification file “only,” while consequential edit 6 explicitly includes two docket rows. State the complete file perimeter in the implementation record. Existing required-field/wrapper/token and mapping-authenticity review residue remains outside this bounded F3/F8 amendment; no overall gate completion is inferred. The exact-rational rule should govern normalization comparisons even when implementations parse Decimal strings; ordinary Decimal context sums must not silently introduce tolerance.
