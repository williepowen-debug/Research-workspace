# PROPOSAL TO WILL — the verification verdict calls an unsupported claim FALSE, and it has fired at least once

**WALTER · 2026-09-21 · `walter-e3`** · **RULE 8 STRUCTURAL CHANGE — PROPOSAL ONLY, NOTHING EDITED.**
**Source:** CATO second review `AGENTS/CATO/runs/2026-09-21_1257_walter-structure-review.md` **§S2 (rated HIGH)**, relayed with a PROME ranking in `inbox/2026-09-21_from-PROME_cato-second-review-...md`.

⛔ **RULE 8: this changes the SEMANTICS of a verdict enum, which is a structural change, so the letter is NOT edited and will not be until Will rules.** WALTER has verified the defect and sized it; it has not fixed it.

---

## 1 — THE DEFECT, QUOTED FROM WALTER'S OWN LETTER

`design/SIGNAL_PROCESSING_CHECKLIST.md:124`:

> | **FALSE** | Primary source contradicts the claim, **or no primary source exists to support it** | KILL. Log to kill_log.tsv with reason "framing-false, verify-research verdict". |

`:125`, immediately below:

> | **INDETERMINATE** | **Primary exists but is ambiguous**, or verification inconclusive within time budget | Route with lowered confidence… |

🔑 **THE HOLE IS STRUCTURAL, NOT A WORDING SLIP.** `INDETERMINATE` is scoped to *"primary **exists** but is ambiguous."* So the state **"I searched and found no primary"** has **no home in the enum except FALSE** — and FALSE routes to **KILL**. ⇒ **the letter does not merely permit the conflation; it leaves nowhere else to go.**

⚠️ **Absence of evidence is not evidence of absence.** A claim nobody has sourced yet may be true, may be unpublished, may sit behind a paywall this toolchain cannot reach, or may be genuinely false — and the letter collapses all four into the one that also kills the signal.

## 2 — IT HAS FIRED. n=1 CONFIRMED, AND THE SIZING IS HONEST

**`filtered/kill_log.tsv`, 635 rows.** ⚠️ **First measurement was a FALSE NEGATIVE and is recorded as such:** WALTER grepped the literal reason string `framing-false` from the letter, got **0 hits**, and nearly reported "never fired." **The log's `Failed_Gate` field uses a different vocabulary entirely** (Novelty 197 · Relevance 113 · Relevance/Vintage 60 · Credibility 40 · …), so the letter's own reason string appears nowhere. `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]` — **firing on WALTER, while WALTER measured a defect of exactly this family.**

**The real instance, on the re-scan:**

> **2026-04-20T21:30:00Z** · gate `Credibility (verify spawned, verdict FALSE conf 0.90)` · *"Extraordinary geopolitical action, no primary sourcing"* · notes: *"VERDICT: **FALSE (0.90)**. **No primary source found** across Reuters/Bloomberg/FT/…"*

⇒ **A claim was graded FALSE at 0.90 confidence because no primary was FOUND, not because one contradicted it.** That is the defective branch, executing exactly as written.

✅ **What is NOT claimed, and the distinction matters:**
- **The KILL may well have been correct.** An unsourced extraordinary geopolitical claim can properly fail the **Credibility** gate on its own merits. ⛔ **The defect is the VERDICT LABEL, not necessarily the disposition** — "we do not credit this" is a decision about routing; "this is FALSE at 0.90" is an assertion about the world, and it was logged as one.
- **A second FALSE row (2026-05-06) is CORRECT and stays** — Visegrad 24 collapsed a real IRGC-on-Kurdish-dissident event into a "US base at Erbil" framing. **A primary existed and contradicted the framing.** That is what FALSE is for.
- **16 further rows carry absence-shaped language**, but sit under Credibility/Relevance/Novelty gates rather than a FALSE verdict. **They are NOT counted as instances** and were not individually adjudicated.
- ⛔ **No claim that historical kills were wrong at scale.** **n=1 on the verdict label.** CATO made no such claim either.

## 3 — PROPOSED CHANGE (not applied)

| Verdict | Proposed meaning | Action |
|---|---|---|
| **FALSE** | ⛔ **RESERVED for a primary that CONTRADICTS the particular claim.** Contradiction must be of *this* claim, not of an adjacent one | KILL, reason `framing-false` |
| 🆕 **UNSUPPORTED** | **Searched, no supporting primary found** — OR the primary is inaccessible (paywall, unreachable host, language) | ⛔ **NOT a verdict about truth.** Disposition is a SEPARATE relevance/urgency decision: route with lowered confidence and the absence stated, or kill on **Credibility/Relevance** on its own merits — **never on "framing-false"** |
| **INDETERMINATE** | Primary exists but is ambiguous, or verification inconclusive within budget | unchanged |
| **CONFIRMED** / **CORRECTED-framing** | unchanged | unchanged |

🔑 **The load-bearing half is the second row's second sentence: separating the VERDICT from the DISPOSITION.** ⛔ **This does NOT mean routing every rumour** — it means an unsourced item gets killed for being unsourced, under a gate that says so, instead of being recorded as disproved.

## 4 — ACCEPTANCE CONDITIONS (WQ-229 shape, in the defect's own terms)

**Before this is called fixed, all five categories adjudicated, N/A justified where it does not apply:**

| Category | Condition |
|---|---|
| **Ordinary** | Four worked cases yield four DISTINCT verdicts and reasons: ① a contradicted claim → **FALSE** · ② an inaccessible primary → **UNSUPPORTED** · ③ a searched-and-absent claim → **UNSUPPORTED** · ④ a mixed true/false claim → **CORRECTED-framing**, with the surviving facts preserved |
| **Overlap** | `UNSUPPORTED` and `INDETERMINATE` are not two names for one state. **Test: primary EXISTS but is ambiguous ⇒ INDETERMINATE; primary NOT FOUND or unreachable ⇒ UNSUPPORTED.** If a case grades both, the boundary is wrong |
| **Wrong owner** | The verdict is WALTER's (framing check). ⛔ **The DOMAIN truth call is the owning desk's and this change must not quietly move it.** A `UNSUPPORTED` routed at low confidence must not read as WALTER endorsing the claim |
| **Missing information** | The `kill_log` `Failed_Gate` vocabulary does not contain the letter's own reason strings — **which is why the first measurement of this very defect returned a false zero.** A fix that does not reconcile the letter's reason strings with the log's actual gate vocabulary leaves the defect **unmeasurable**, and the next reader will repeat the false zero |
| **Concurrent activity** | `SPEC_OWNERSHIP.md` names the dependent surfaces; FILTER_SPEC and FORMAT_SPEC both reference verdicts. **Sweep dependents in the same pass** (`version_drift_check.py` is the backstop). ⛔ **Do not edit while another desk is mid-session in `design/`** |

**Independent reader before it is called fixed:** CATO qualifies. **HAWK also qualifies and is arguably the better choice** — it adopted the `-013` §④ rule under this same absence-vs-disproof confusion this morning, so it is the one desk with a live stake in getting the distinction right.

## 5 — WHAT WALTER IS NOT PROPOSING

⛔ **No new database, no parallel ledger, no new scorecard.** ⛔ **No change to the CONFIRMED / CORRECTED-framing rows.** ⛔ **No retroactive re-adjudication of the 635 kill rows** — the 2026-04-20 row is named as the instance and left as the historical record it is.

## 6 — ONE PUSH-BACK ON THE RELAY, AND IT IS A CITATION DEFECT

⚠️ **PROME's packet renumbers CATO's findings.** CATO's review is **`S1`–`S5`**; PROME's packet ranks them **`#1`–`#6`**. They do not align: **PROME's `#1` is CATO's `S2`; CATO's `S1` is a DIFFERENT item** (the instructions cleanup, which PROME numbers `#2`). ⇒ **anyone who reads "#1" and greps CATO's review lands on the wrong finding.** `[[finding_unqualified_identifier_is_a_defect_waiting_for_a_reader]]` — **this fleet already carries a standing rule that two numbered lists cited by number must never be collapsed** (root `CLAUDE.md`, root-rule vs Non-Negotiable). **Recommend: cite CATO findings as `CATO-S2` and PROME's ranking as `PROME-rank-#1`, never a bare number.** Raised to PROME; not a criticism of the ranking, which is sound.

---

## THE ASK

**Will: approve the enum change in §3, or rule otherwise.** It is a **structural** change to a Will-signed spec's semantics, so WALTER will not touch the letter without your word. **Everything above is verification and proposal; nothing is edited.**

⚠️ **If approved, WALTER proposes to land it under the §4 acceptance conditions with a HAWK cross-read, and to sweep the dependent surfaces in the same pass.**
