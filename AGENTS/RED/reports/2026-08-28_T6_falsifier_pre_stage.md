# T6 FALSIFIER SEAT — PRE-STAGE GRADE (Fri 2026-08-28, ~14:3x ET)

**Seat:** RED (falsifier / adversarial-analysis) · Will-assigned via DAEDALUS relay, Will-confirmed in-session ("A") 2026-08-28.
**Object:** T6 30Y benign-bucket test — hard close **Sat 2026-08-29** (Option C: last gradeable data = **Fri 2026-08-28 closes**).
**Owners:** BOND (instrument, original spec) / LIQUID (co-spec + 8/19 checkpoint).
**Frozen spec:** `FORUM/2026-08-10_financial-conditions/04_synthesis/06_HENRY_joint-synthesis-FINAL.md` §5 T6 + all riders below.
**Purpose:** pre-stage today so tomorrow is execution, not analysis. **Formal grade must wait for DGS30 8/28 publication (~Mon 8/31, T+1).**

⛔ **THIS IS PRE-STAGE. NO GRADE IS FINAL UNTIL DGS30 8/28 OBSERVATION PUBLISHES ~2026-08-31.** RED does not own the grade; BOND/LIQUID do. This file is the adversarial-check pre-work.

---

## 1 · SPEC RESTATED (byte-faithful; DO NOT amend)

| Cell | Value |
|---|---|
| **Trigger** | ORACLE Sept-hike probability **<25%** (strict less-than; 25.0% does NOT trigger) |
| **RETRACE** (confirms LIQUID's benign): | DGS30 <5.05% **×2 consecutive** sessions within **5 sessions after** trigger fires |
| **HOLD/EXTEND** (confirms BOND's not-benign): | DGS30 **≥5.10%** for those 5 sessions **OR** fresh high **>5.28%** while probability keeps falling |
| **NO-VERDICT band** | 5.05-5.10%, **or the trigger never fires** |
| **Hard close** | 2026-08-29 (Sat, non-session; close STANDS per Option C) |
| **Effective last data** | Fri 2026-08-28 session closes |
| **Late-fire clause** | NO-VERDICT-BY-COMPRESSION, recorded with cause, never scored for/against either desk |

## 2 · RIDERS (all apply)

**R1 — Option C, Will-ruled 2026-08-21** (`PROME/proposals/2026-08-21_t6-saturday-option-c-RULED.md`, verbatim *"Rule T6 Option C off your rec"*): 8/29 hard close STANDS; effective last gradeable data = Fri 2026-08-28; trigger firing with fewer sessions left than a branch requires = NO-VERDICT-BY-COMPRESSION.

**R2 — OR-leg CONJUNCTIVE, BOND/LIQUID joint 2026-08-23** (all 4 LIQUID rulings + BOND D-DIVERGENCE, all six items settled joint, no split): the ">5.28% fresh high" leg reads as `DGS30 close strictly >5.28% AND strictly above the prevailing 2026 maximum (5.31 [8/17], ratcheting in-window)`. **5.29/5.30 does NOT fire.** The pre-trigger 8/17 spike RAISED the bar on BOND's own branch.

**R3 — Grade-date trap, T+1 publish**: `DGS30` publishes T+1 business day. **8/28 observation publishes ~Mon 2026-08-31.** A grader running before that sees no 8/28 close. **Grade must be run on the obs published through 8/28; a run before that is UNGRADEABLE-PENDING-PUBLICATION, never NOT-FIRED** (`PROME/proposals/2026-08-27_lagged-series-grade-date-RULED.md`).

**R4 — "Keeps falling" qualifier defaults NOT-FIRING**: an ungradeable "keeps falling" qualifier means the OR-leg **DOES NOT FIRE**; it does not default to firing.

**R5 — Fallback trigger source**: gap-marking confirmed ⇒ Kalshi canonical; declined ⇒ Polymarket, substitution recorded on the grade; never blended.

## 3 · PRIMARY STATE (as of ~14:30 ET 2026-08-28)

### 3a · Trigger series (Sept-hike probability)

**Source:** ORACLE STATUS 2026-08-28 dashboard.

| Platform | Level | Δ7d | 8/28 status |
|---|---:|---:|---|
| Kalshi ("Fed hike at Sept mtg >3.75%") — **T6 CANONICAL** | **31.0%** | −2.0 | book pinned, 1¢ tight, mid 30.5 |
| Polymarket ("Fed HIKE at Sept mtg") | 30.5% | −4.0 | +3.0 vol |
| **Distance to trigger** | **+6.0pp above <25%** | | |

**Series across the resolution window (8/10 → 8/28):**
- **Registration 8/10:** 35.5%
- **Window low:** 25% touched 8/14–8/16 (three sessions), **never crossed** (strict <25% never satisfied)
- **Current 8/28:** 30.5-31.0% (both platforms)
- **⇒ TRIGGER NEVER FIRED throughout the entire window.**

### 3b · DGS30 series (BOND's instrument)

**Source:** BOND STATUS 2026-08-28 dashboard (FRED `DGS30`).

| Date | Close | Note |
|---|---:|---|
| 2026-08-17 | **5.31** | 2026 max, 19.2-yr high (only 2007-06-12 at 5.35 sits above in the full series) |
| 2026-08-20 | 5.23 | |
| 2026-08-21 | 5.19 | |
| 2026-08-25 | **5.17** | Latest published close (per BOND boot 8/27) |
| 2026-08-26 | *unpublished at BOND boot* | |
| 2026-08-27 | *unpublished* | |
| 2026-08-28 | **UNGRADEABLE-PENDING-PUBLICATION (~Mon 8/31)** | |

**Structural context:** 36 consecutive sessions ≥5.00% (from 7/7); 52 days in 2026 above 5.00% (>2007's 50). The regime has never left the ≥5.10 band on any published close in the resolution window.

**Informational proxy (^TYX, NOT the graded instrument — Yahoo `^TYX`):**

| Date | ^TYX close |
|---|---:|
| 2026-08-24 | 5.231 |
| 2026-08-25 | 5.174 |
| 2026-08-26 | 5.186 |
| 2026-08-27 | 5.191 |
| **2026-08-28** | **5.206** |

⛔ **^TYX is not DGS30** (basis: continuous futures vs constant-maturity yield). The proxy is informational for pre-stage only. **The formal grade uses DGS30 8/28 close, publishes Mon 8/31.** If DGS30 8/28 lands in the historical ^TYX-vs-DGS30 spread (typically within a few bp), the pre-stage verdict is robust.

## 4 · PRE-STAGE VERDICT

### 4a · Direct application of the spec

**Trigger condition (Sept-hike <25%): NOT FIRED at any point in the resolution window.**
- Highest breach observation is 25.0% touching on 8/14, 8/15, 8/16 — strict less-than never satisfied
- Current 30.5-31.0% is 6pp above the trigger
- **⇒ Per the spec's own final clause: "NO-VERDICT band: 5.05-5.10%, or the trigger never fires." The second clause is met.**

### 4b · Branch verdicts (moot but recorded for the audit trail)

- **RETRACE branch (DGS30 <5.05% ×2 in 5 sessions after trigger):** moot — trigger never fired. Regardless: DGS30 has not printed <5.05 in the entire window (minimum is 5.17 [8/25]).
- **HOLD/EXTEND branch (DGS30 ≥5.10 for 5 post-trigger sessions OR fresh high >5.28 while odds fall):** moot — trigger never fired. Additionally: OR-leg cannot fire because (i) DGS30 must strictly exceed 5.31 [8/17] per R2 ratchet, and (ii) probability must be FALLING (R4 default) — it is currently RISING (bottomed 8/14-16 at 25.0%, back to 30.5-31.0%).

### 4c · Formal pre-stage verdict

**T6 = NO-VERDICT (trigger-never-fired branch)** — pending only DGS30 8/28 close publication (~Mon 8/31) for the audit-trail row.

**Confidence in the pre-stage: VERY HIGH.** The verdict is driven by the trigger series which is fully published through 8/28 (Kalshi and PM both). DGS30 8/28 close would need to be a data point BOTH >5.31 (fresh 2026 high) AND simultaneously with falling Sept-hike odds to fire the HOLD/EXTEND OR-leg — and even then, the leg requires the trigger to have already fired, which it did not.

## 5 · WHAT COULD CHANGE THE VERDICT (adversarial check, run against MYSELF)

**Scenario A — intraday Sept-hike odds cross <25% on 8/28 close.** Requires −5.5pp to −6.0pp move on Fri 8/28 alone. Not visible in ORACLE's current book. If ORACLE's 8/28 close pin actually shows <25%, this pre-stage flips to trigger-fires-in-final-session, which then activates the compression clause (only 0 sessions remain within the 5-session-post-trigger requirement) → **NO-VERDICT-BY-COMPRESSION** anyway. Same terminal verdict.

**Scenario B — DGS30 8/28 close prints >5.31 (fresh 2026 high) AND odds fell today.** Even so, requires the trigger to have already fired (it did not), so the OR-leg is inactive per the spec's structural reading. Verdict unchanged.

**Scenario C — the spec is read to allow OR-leg firing INDEPENDENT of trigger.** ⚠️ **This is a real spec-interpretation ambiguity worth naming for BOND/LIQUID at grade time.** LIQUID's write-up says HOLD/EXTEND is "curve stays OUT of the benign bucket" — which implies both legs are trigger-conditioned outcomes. But the ">5.28 while odds keep falling" could arguably be an INDEPENDENT firing path (it's the "term-premium doing independent work" case). **RED does not adjudicate; RED flags.** If BOND/LIQUID agree at grade time that the OR-leg is trigger-conditioned (LIQUID's interpretation), verdict = NO-VERDICT. If they agree it is independent, then the DGS30 8/28 close matters and the leg's firing conditions must be checked.

**Scenario D — an ORACLE pin for 8/28 goes unmeasured** (per LIQUID's flag: "NOBODY is named to pin 8/24-8/28"). If the 8/28 pin is missing, PROME's provisional 8/21 capture is the fallback per R5. **The 8/28 pin is a live gap.** If the fallback also fails, the trigger status for 8/28 becomes UNGRADEABLE — but since Kalshi and PM are both currently 30.5-31.0% and both platforms are active with tight books, non-pin is very unlikely.

## 6 · ADVERSARIAL FINDINGS (RED's contribution as falsifier seat)

**F1 — SPEC-INTERPRETATION AMBIGUITY (flagged in Scenario C above).** The HOLD/EXTEND branch's second leg ("fresh high >5.28% while odds keep falling") is *structurally* co-dependent on the trigger in LIQUID's write-up, but could be read as INDEPENDENT under the "term-premium doing independent work" framing. **BOND/LIQUID should state their read explicitly at grade time.** Under EITHER read the verdict here is NO-VERDICT, so this is not verdict-changing today; it matters for future T6-shaped tests and for the fresh-high clause's future re-use. **RED recommendation: at grade time, name the interpretation adopted, on-the-record, so the next spec of this shape does not carry the ambiguity.**

**F2 — MISSING 8/28 SEPT-HIKE PIN.** LIQUID's own note (STATUS 8/22): *"NOBODY is named to pin 8/24-8/28."* PROME filed a provisional 8/21 capture but the 8/22-8/28 daily pins are not assigned. **The R5 fallback (gap-marking confirmed ⇒ Kalshi canonical) works if ORACLE gap-marks. If gap-marking is not done, R5 says Polymarket becomes canonical and the substitution goes on the grade record.** At grade time, whoever runs the grade must state which platform they used and why. **RED recommendation: BOND/LIQUID or PROME formally close the 8/24-8/28 pin gap at grade time by adopting ORACLE's 8/28 close pin OR the R5 fallback; do not leave it implicit.**

**F3 — RED IS NOT NAMED AS FALSIFIER SEAT IN THE FROZEN FORUM SPEC.** The FORUM synthesis (§5 T6) names BOND (instrument, original spec) / LIQUID (co-spec + 8/19 checkpoint) as owners. **RED's assignment as falsifier seat arrived via DAEDALUS relay and Will's in-session "A" ruling** (verified with Will 2026-08-28 before pre-staging). **This should be recorded on the grade** so the co-owners know which desk performed the adversarial check. **RED recommendation: the grade record cites RED as the falsifier-seat contributor with the Will-word provenance, so a future audit can trace it.**

**F4 — DAEDALUS'S "PRE-STAGE THE GRADE" LANGUAGE IS AMBIGUOUS AT THE OWNERSHIP LINE.** DAEDALUS said "pre-stage the grade today so tomorrow is execution." Read one way, this means "write BOND/LIQUID's grade for them" — which RED cannot do (they own the instrument). Read another way, this means "write the adversarial-check pre-work so BOND/LIQUID's grade execution tomorrow is faster." This file adopts the second reading. **RED recommendation: BOND/LIQUID own the formal grade; this file is the falsifier-seat's audit-trail contribution. If DAEDALUS or Will meant the first reading, RED needs an explicit ownership transfer word.**

## 7 · WHAT TOMORROW'S EXECUTION NEEDS

For BOND/LIQUID (owners) at their grade time (~Mon 8/31 after DGS30 8/28 publishes):

1. **Pull DGS30 8/28 close from FRED** (published ~Mon 8/31, T+1). Verify basis: FRED `DGS30` daily constant-maturity yield.
2. **Pull ORACLE 8/28 Sept-hike close** (Kalshi canonical per R5 default; substitute Polymarket only if gap-marking not done and substitution recorded on the grade).
3. **Apply the spec's clause set:**
   - If Sept-hike 8/28 close <25% → trigger fired on final session → NO-VERDICT-BY-COMPRESSION per R1.
   - If Sept-hike 8/28 close ≥25% → trigger never fired → **NO-VERDICT** per the spec's own final clause.
   - Either way: NO-VERDICT, this pre-stage's verdict stands.
4. **Resolve the F1 ambiguity on-the-record** (state whether OR-leg was read as trigger-conditioned or independent). Note that under EITHER reading the verdict is NO-VERDICT here — so this is documentation, not gate-changing.
5. **Record on the grade:** RED as falsifier seat, DAEDALUS relay + Will "A" ruling provenance, this pre-stage file path.
6. **Post the grade** to `FORUM/2026-08-10_financial-conditions/05_grade/T6_HARD_CLOSE_2026-08-29_GRADE.md` (or wherever BOND/LIQUID conventionally file joint grades).

## 8 · SUMMARY (single-line for the state line)

**T6 PRE-STAGE VERDICT: NO-VERDICT (trigger-never-fired branch). Confidence VERY HIGH. Formal grade waits on DGS30 8/28 publication (~Mon 8/31). Four adversarial findings flagged (F1-F4) — none verdict-changing for T6 itself. RED = falsifier seat via Will "A" ruling 2026-08-28.**

---

*Pre-staged 2026-08-28 ~14:3x ET. Grade execution waits for DGS30 8/28 publication ~Mon 2026-08-31. BOND/LIQUID own the formal grade; RED contributes as falsifier seat only.*
