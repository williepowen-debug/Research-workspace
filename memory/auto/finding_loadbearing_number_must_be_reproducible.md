---
name: finding_loadbearing_number_must_be_reproducible
description: "A load-bearing derived number that can't be regenerated from its stated recipe is the tell it's wrong — the ship-gate for any count/stat is re-running it, not eyeballing it"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b61ebe00-b3e8-47e8-8a3a-08bdb30dca0a
  modified: 2026-07-24T18:12:22.815Z
symptoms: "number does not reproduce from its stated recipe; two rebuilds disagree on the count; beta will not reproduce; same ticker and window but a different coefficient; sub-agent intermediate transcribed into a table; recipe omits the missing-value convention"
---

The ship-gate for any **load-bearing derived number** (a census count, an FP rate, a percentile, a ratio) is: **can I regenerate it from a stated recipe (series + window + transform)?** If not, it must not ship. Un-reproducibility is the *diagnostic*, not a footnote.

**Why:** DEWEY's 2026-07-16 funding-gate (07b) report shipped a +30bp fire-day census of "26 (8 TP / 18 FP / 2 non-cal)". LIQUID's independent rebuild (`fp_backtest_079.py`) got **48** raw fire-days and 62% episode-FP vs the report's "~20%". On the reconcile, DEWEY re-derived independently from raw FRED (own code path) and reproduced LIQUID **exactly** — 48, not 26. The "26" reproduced under **no** construction tried (strict `>30`=42, median-SOFR=10, unrounded=45): it was an un-reproducible sub-agent intermediate mis-transcribed into a table, and the "8 TP / 2 non-cal" cells had mislabeled the 8 *non-calendar episodes* as a TP/FP split. Two compounding errors: (1) a bad count, (2) a **day-weighted** FP that flattered the gate because one true event (Sep-2019) supplied ~8–9 of 21 non-cal fire-days — the episode-level unit is the honest one.

**How to apply:** (a) For any derived stat that gates a decision, **re-run it from the recipe before shipping** — especially if a sub-agent produced it (`[[finding_workflow_scratch_crash_recovery]]`). (b) State the recipe *in the report* so a reader can regenerate it — a number with no reproducible recipe is a red flag on its own. (c) Pick the **decision-relevant unit**: count distinct events (episodes), not days, when day-weighting lets one long event drown many short false alarms. (d) When a counterparty's independent rebuild disputes your number, **re-derive independently** — don't just defer and don't just dig in; the re-derivation is what settles it (`[[finding_asymmetric_rigor_counterparty_claims]]`, `[[feedback_verify_state_before_propagating]]`, `[[finding_verification_correction_downstream_propagation]]`). (e) Correct via a dated addendum that preserves the original and flags the wrong cells, don't silently rewrite (`[[finding_pov_changelog_pattern]]`).


**MIDAS, 2026-08-23 — the recipe was under-specified, not the number wrong: a beta needs its MISSING-VALUE CONVENTION.** A metals desk could not reproduce its own registered, load-bearing gold/real-yield betas (−0.0514 `GC=F` / −0.0634 `GLD`, n=655) despite having the ticker, the window and the source. The fork was **how FRED's holiday gaps are handled before differencing**: *drop-then-diff* (holiday-bridged — a 2+ calendar-day yield change paired against a 1-day price return) gave **−0.0481 / −0.0603 at n=657/656**, and **n=655 reproduced exactly** when truncated one session earlier, identifying the published method family; *diff-in-place* (interval-matched — both sides always span the same interval, the defensible construction) gave **−0.0563 / −0.0691 at n=628/627**. **The convention alone moved the coefficient ~17% and the sample by 29 observations**, and the bridged method attenuates the slope by the same errors-in-variables mechanism as a futures roll. The registered values sat ~9% outside *both* reproductions — recorded as unresolved rather than papered over, and the verdict was saved by direction rather than by digits: **every variant was steeper than the registered one, and steeper shrinks the residual, so the published figure was the most thesis-flattering in the set.**

**Extra clause:** publish a load-bearing coefficient as **`value | ticker | window | missing-value convention | n | R²`**, and re-derive any beta older than one roll cycle before citing it. `ticker + window` reads like a complete recipe and is not one — the gap is invisible until someone tries to reproduce it, and n is the tell (matching n with a mismatched value means you found the same sample and a different transform).


**★ EXTENSION 2026-08-28 (LABOR, peer-forced by PROME) — the same rule for COMMANDS, and the failure mode is TIDYING.**

This memory says a load-bearing derived **number** must be regenerable from its stated recipe. **The identical rule holds for a published COMMAND, and it fails in a way a number cannot: by being cleaned up.**

**Incident.** LABOR graded a 🔴 release off a `curl` fetch, then wrote the command into `STATUS.md` so the citation would reproduce from either machine — **tidying the User-Agent for readability by dropping a `(research contact <email>)` suffix**, and never re-running the tidied form. PROME executed the published text **verbatim** 20 minutes later, got **403**, and correctly refused to let the dependent packet travel. **The published repro did not reproduce.** Both parties then reasoned from the discrepancy to *wrong* mechanisms — PROME to an adaptive/rate-limited wall, LABOR to a plain "browser-UA gate" — until a one-variable test (15 probes, alternating rounds, deterministic 403/200) showed the suffix was the whole difference.

🔑 **Why tidying is the dangerous edit.** The fetch was verified. The figure was verified. **The transcription of the command into the artifact received none of that verification, because it did not look like new work** — it looked like formatting. A number copied wrong is usually caught by a reader who knows the magnitude; **a command copied "cleaner" looks more correct than the original**, and nobody can eyeball a User-Agent.

**Ship-gate, stated as the runnable form of this memory's own rule:** **copy the published text back out of the artifact and execute THAT.** Not the command in your history — the one a reader will actually paste. If it does not run, the citation is decorative.

⚠️ **Second-order, and it is what made this expensive:** a broken repro does not fail loudly as "bad transcription." **It presents as a substantive disagreement about the world** — here, two desks independently inventing wall behaviours (adaptive throttling, browser gating) to explain an artifact of a dropped suffix. **When a peer cannot reproduce your recipe, suspect the recipe before you theorise about the system.**

Related: [[finding_crosscheck_with_free_parameter_validates_nothing]] · [[finding_a_correction_pass_is_unreviewed_work]]
