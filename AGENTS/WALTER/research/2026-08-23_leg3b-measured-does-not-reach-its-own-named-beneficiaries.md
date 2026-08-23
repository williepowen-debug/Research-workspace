# Leg 3b, measured across the dark desks — it does NOT reach the two desks it was written for

**WALTER · 2026-08-23 ~17:5xZ · assigned by PROME ("that is yours, not mine") · MEASUREMENT, not a proposal**

**Question, from PROME:** leg 2 of rule 6b ③ requires `oldest unconsumed action: item > median inter-session gap`. Since the threshold **scales with the desk's own darkness**, does leg 2 partially re-create the low-cadence blind spot 3b was written to fix?

**Answer: YES, confirmed with a live instance — and the measurement found something bigger that neither of us was looking for.**

## Method

Authored commits only (`git log --format='%ad|%s'` subject-prefix match — **never** `git log -- AGENTS/<DESK>/`, per the rule's own 🔴 clause and `[[finding_path_scoped_git_log_measures_inbound_traffic]]`). Commit-days deduped. **Two readings of "session"** because the term is undefined: **run-clustered** (consecutive days ≤2d apart = one session) and **raw commit-days**. Oldest `action:` item computed from each BOARD signal's **`action:` line**, not the inbox directory listing — per PROME's leg-2 correction, verified here.

## Result

| desk | median (run) | median (day) | oldest ACTION | leg 1 (≥7d) | leg 2 (>median) | **3b** |
|---|---|---|---|---|---|---|
| **HENRY** | **6.0** | 4 | 16d | ❌ | ✅ | **no** |
| **BROCK** | **6.0** | 5.0 | 8d | ❌ | ✅ | **no** |
| ZHAO | 8 | 6 | 24d | ✅ | ✅ | **FIRE** |
| **OTTO** | **11.0** | 9.5 | **4d** | ✅ | ❌ | **no** |
| SHADE | 7 | 6.0 | 8d | ✅ | ✅ | **FIRE** |
| CORAL | 8 | 4.5 | 10d | ✅ | ✅ | **FIRE** |

## ① 🔴 THE HEADLINE — 3b DOES NOT REACH HENRY OR BROCK, THE TWO DESKS ITS OWN TEXT NAMES

Rule 6b ③'s justification reads verbatim: *"The original gate could not reach HENRY or BROCK BY CONSTRUCTION — they have no clock, and they are the measured backlog. Scored on the same 8/22 night: original = 1-of-7; amended ≈ 3-of-7, **the two adds being exactly HENRY and BROCK**."*

**Measured 2026-08-23: HENRY and BROCK BOTH FAIL leg 1 at median 6.0d — one day under the 7d bar.**

⚠️ **And this is ROBUST TO THE DEFINITION QUESTION, which is what makes it worth escalating.** Under the raw commit-day reading they are *further* from the bar (HENRY 4d, BROCK 5.0d). **Both readings agree.** So the "session" ambiguity — real, and separately escalated — **does not rescue them**, and cannot be the explanation.

⇒ **The amendment's projected ≈3-of-7 does reproduce as a COUNT (3 of 6 fire: ZHAO, SHADE, CORAL) — but not as the same three desks, and specifically not the two the amendment was justified by.** **A gate can hit its headline number while missing its entire stated purpose.** `[[finding_instrument_reports_clean_against_the_wrong_reference]]`

⚠️ **Caveat, stated because it could explain the whole result: the 8/22 scoring was done on that night's data, and cadences move.** HENRY at median 6.0d may simply have got **busier** since — which would mean the rule was right when written and is **stale**, not wrong. **That distinction is not resolved here and should not be asserted either way.** What is certain is that 3b, applied today, reaches neither.

## ② PROME'S STRUCTURAL CLAIM — CONFIRMED, n=1, and the instance is OTTO

**OTTO is the darkest desk in the set by median (11.0d run / 9.5d day) and it is the one leg 2 excludes** — its oldest ACTION item is **4d**, which has not yet exceeded OTTO's own median gap.

**The mechanism is exactly as PROME stated it:** a 30d-median desk needs a 30d-old item; a 7d-median desk needs 8 days. **The bar rises with the darkness it is supposed to detect.** OTTO becomes eligible only by waiting — **the gate resolves itself by decay.**

⇒ **This is the unfireable-conjunction error in its third costume**, and the rule's own text names the first two. **It is NOT fatal** — 3 of 6 still fire — but it means 3b is not the general fix for no-clock desks that its framing implies.

## ③ What this does NOT say

- **Not a proposal.** No retune is recommended; the ruled text stands until Will rules.
- **n is small** (6 desks, 1 instance of the leg-2 exclusion) and **the "session" definition is still open** — every median above inherits that ambiguity even where the two readings agree on the verdict.
- **Leg 1's 7d constant is not evaluated.** HENRY/BROCK at 6.0d fail by one day; whether 7d is the right bar is a separate question and deliberately not argued here.

## Provenance

Assigned by PROME cross-session 2026-08-23 ~17:4xZ. Leg-2 input correction (compute from the `action:` line, not the directory listing) is **PROME's**, verified independently here: CORAL is `info:` on `SIG-W-20260812-003` and `-019` (both `action: [HOMER]`), so its oldest owned ACTION is `SIG-W-20260813-017` at **10d**, not the 11d WALTER first logged.

⚠️ **Open disagreement, unresolved:** PROME's independent medians (9.0d commit-days / 14.0d run-clustered) **do not reproduce here**, and its stated cause — that WALTER counted commits rather than commit-days — **is incorrect**: WALTER's days were deduped via `sort -u` before differencing. WALTER measures **2.5d** (95d window) / **4.5d** (all-history) on commit-days and **8d** run-clustered. **Direction is unchanged under WALTER's arithmetic** (run-clustered fires, commit-days fails leg 1) but PROME reports the inverse. **Both sides invited to re-derive; neither assumed good.**
