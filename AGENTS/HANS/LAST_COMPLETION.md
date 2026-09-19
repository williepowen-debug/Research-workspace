## COMPLETION — HANS — 2026-09-19. Saturday, market closed. Owed-board catch-up, then TWO external review passes.

**STATUS:** ✅ Committed and pushed. ⚠️ **A THIRD CATO PASS IS EXPECTED — do not treat this as certified.** Two review rounds each found real defects in work I had just verified; the base rate says look again.

**⚖️ WILL NEEDS: NOTHING.** The day's one ask — a free GIE AGSI+ key — Will provisioned at 11:33 and it is verified by live pull.

**Instruments at close:** boot **EXIT 0** · `doc_audit` **0 findings, 14/14 checks present** · **120/120 tests** · `closeout_check` **8/8, EXIT 0** (and it now genuinely fails when a step dies) · STATUS **22.8 kB, under the 70% stop**.

---

### WHAT THE MARKET READ IS — unchanged all day
`HANS-F-004` / `T-08` **ORANGE, OPEN at −15.99pp** (single-source AGSI-native norm 85.05). ⛔ **The move from −19.7 is a BASIS correction, NOT a recovery** — ~80% denominator. ⚠️ **Composition-sensitive:** leave-one-out runs −13.79 to −19.44; **no 4-year variant reaches the −12 exit**, so the verdict holds, but the benchmark's economic usefulness is **unvalidated**.
`T-14` **NOT fired**, band untouched. 🔴 **But its silence means less than it looks:** the ESRB puts identified bank exposure to private equity/private credit at **€4bn**, calls it *"far below the figures implied by supervisory intelligence"*, and drops the class from the analysis — a row waiting for a supervisor to NAME institutions sits downstream of that supervisor being able to SEE them.
⛔ **The net-debtor inference is WITHDRAWN.** Funding withdrawal and credit losses are **not alternatives — they co-occur**, because the same counterparty stress drives both. A net position bounds neither side. `HNS-09` holds **70%** on its **registered** text (sector NII/earnings, no material rise in cost-of-risk) — STATUS had been rendering an easier version and no longer does.

### NEW INSTRUMENTATION (all falsified by injection, not merely written)
`C0` check-census · `C9` stale figures in prose · `C12` key uniqueness · `C13` value/band scale · `C14` anti-regrowth. **BoE IADB daily keyless pull** — UK 10Y (cross-check only) and the **Bank Rate**, the row that once sat 6.5 months stale. **AGSI-native 5-yr norm**, fail-closed. **Dead-key discriminator.** **STATUS hot/cold split** → `SESSION_LOG.md`.

### 🔴 THE TWO LESSONS THAT SHOULD SURVIVE THIS SESSION
1. **I fixed the payload I tested, not the property — three times in one round** (runner: excluded rc=3 when a traceback exits 1 · parsers: rejected NaN in one reader, not the other · exemption: froze ids, not counts). A counterexample is an instance of a class. → `ML-HANS-476`
2. **A refactor deleted a whole check and the audit still printed "0 findings."** Nothing in the output changed when a check stopped existing. Caught only by a test asserting that check FIRES. `C0` now censuses the source. → `ML-HANS-477`
⚠️ **STANDING PRIOR, NINE sessions: every defect here is found from OUTSIDE or by a script, never by re-reading.** Today held six times.

---

### ⚠️ KNOWN LIMITATIONS CARRIED OPENLY (CATO third pass) — these are NOT closed
The two consequential false-success paths ARE fixed and verified: the norm now requires each
historical response to **answer the year it was asked for** (the same row fed back five times
had built a "5-yr norm, n=5" from one observation), and each closeout step must match its own
**completion contract** rather than a substring an error can also carry (`SELF mode: ERROR -
nothing scanned` had reported ✅ RAN).
**What remains heuristic, stated rather than fixed:**
- **`C9` is a heuristic over prose**, not a parser. Attribution is unit-or-name; short numbers
  are advisory because prose has no `vectors` column. It will miss cases and it says so.
- **The empty-key discriminator is vendor-quirk-dependent** (re-check 2026-12-19). If GIE
  tightens it, a dead key reads as an unpublished day — safe direction, still blind.
- **`C0` censuses the SOURCE**, so it catches a deleted block, not a check that runs and
  silently does nothing.
- **The storage benchmark's economic usefulness is unvalidated** and its classification is
  composition-sensitive (leave-one-out −13.79 to −19.44).
- **The UK basis gap is undecomposed** — BoE par [9/16] vs TE benchmark [9/18] differ in date
  AND basis at once.
- **`T-12` is uninstrumented and cannot fire. UK 30Y is manual** (a daily BoE 30-yr spot-curve
  lead exists, recorded not built).
⛔ **Repair discipline, not cleverness, was the failure mode today.** Three review rounds each
found real defects in work just verified. The lesson that generalises: **fix the property, not
the payload, and check correspondence to the request — not just the shape of the answer.**

### NEXT SESSION — IN ORDER
| # | Item | When |
|---|---|---|
| — | **Absorb CATO's third pass** if it has landed — check `inbox/` and PROME | first |
| 21 | **AGSI lag D+1 vs D+2** (`KB-HANS-096`) — WEEKDAY check. Touches `HNS-07`'s GRADING date (11/02 vs 11/03), not its resolver | **Tue 9/22** |
| 3 | **`HNS-06` resolves — German/EA flash PMI. GRADE THE FLASH**, not the final | **Wed 9/23** |
| — | **`TTF=F` roll** — `T-07` is a LEVEL ladder with L1+L2 fired; **never grade a rung crossing across a roll** | **9/29** |
| — | **`HNS-07` checkpoints** 10/01 · 10/15 · 10/25. ⛔ **No early resolution — rule (d) WITHDRAWN**; graded on the 11/01 gas day | Oct |

**Still open, not closed:** #5 the OAT basis gap that DECIDES `T-10` (UK leg undecomposed — BoE par [9/16] vs TE [9/18] differ in date AND basis at once) · #13 re-argue exclusion leg (2) · #14 split `VX-HANS-11.03` · #16 Germany UST absent from TIC Table 5 · #22 re-verify the empty-key quirk by 2026-12-19 · #23 ML id collisions (95, frozen with counts, deliberately not renumbered) · `T-12` uninstrumented and cannot fire · **UK 30Y still manual** — CATO found BoE publishes a daily 30-year spot curve; **lead recorded, not built.**
