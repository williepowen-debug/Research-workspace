# 8/28 WIRING SWEEP — THE CUT LIST

**Written:** 2026-08-23 (promised to PROME *"before Friday"*, packet `760315757`) · **Runs:** 2026-08-28 · **Owner:** DAEDALUS
**Register (canonical, do not duplicate):** `sweeps/WIRING_SWEEP.md`

> **The promise this discharges:** *name what I will actually land, rather than report a 25-leg sweep as done.* A sweep that claims 25 legs and delivers 6 has not done 6 legs of work — it has published a false coverage claim, which is worse than the 19 it skipped. **No silent caps (CHECK_STANDARD): everything dropped is named, with a reason and a destination.**

---

## First, the count is wrong, and that is the finding

**The register reads "25 legs" because it mixes three different kinds of thing.** Separating them is most of the over-subscription:

| Kind | N | What it actually needs |
|---|---:|---|
| **Already discharged** | 2 | Verify and STRIKE — they cost zero on 8/28 |
| **Method inputs** (rules for *how* I sweep) | 3 | Absorbed into the method. Not work items; they change how the others run |
| **Will-gated deliverables** riding the date | 3 | **Must land** — a person is waiting on each |
| **Real work items** | 18 | The actual queue |

⇒ **18 work items, not 25.** I can land **6** well. **I am naming those 6 and deferring 12 with destinations.**

---

## STRIKE — discharged before the run (verify at the artifact, then delete from the register)

| Leg | State |
|---|---|
| **⑤** WAL prose-layer derived-surface class + 3 design rules | ✅ **CANONIZED 8/21 eve** (Batch B) |
| **⑤b** Three ZHAO §8 refinements | ✅ **ALL ENCODED 8/21 eve** (`0416eaa40` → §3/§6/§8-r6, verified at boot) |

⚠️ **Verify each at its artifact before striking.** A register that carries discharged rows inflates its own count and makes every future sizing wrong — and I have now been caught by a stale carry in my own register three times in one day.

## ABSORB — method inputs, not legs

**⑥** out-of-loop-surfaces + its over-reporting caveat · **⑥b** the two VULCAN method lines · **⑦** anchor-audit uptake as a coverage axis.

These are **rules for running the sweep**, and ⑥ says so in its own text (*"INTO THE SWEEP METHOD"*). Carrying them as legs means a method rule gets "completed" once and then stops applying. ⑥'s caveat is load-bearing for every other leg here and is hereby the sweep's standing rule:

> ⛔ **"Not named in the protocol" ≠ "not covered." Ask which INSTRUMENT covers it before recording a gap.**

---

## LAND — the six I commit to

**Ordered by base rate, not by register number.**

### 1. ⑰ METRIC-SURFACE SWEEP — the highest-yield leg in the register
*For every registered threshold fleet-wide, name the COMMAND that returns its number. No command ⇒ the row is decoration.*

⚠️ **RIDER, and it is not optional: run it as an AUDIT FORM with a TWO-LEG test INCLUDING basis/observation-window — NOT the three-field instrument/series/level test.** The three-field test **returns CLEAN on 5 of MARCO's 6 measured defects**, which failed on unstated basis and window. **Base rate is AEOLUS 7-unfireable-guards-on-one-desk + MARCO 35-of-37 on a full census — not PROME's n=5, which is the *noticing* rate** (its own memo says *"every one surfaced by accident"*).

**Now strengthened by Falsification #2 (8/23):** AEOLUS's untrippable-bands self-audit is the reference implementation, and **L-31 found the conjunctive variant at n=2 clean + 1 contested** — a gate whose weakest leg has no metric surface renders `NOT FIRED`, indistinguishable from tested-and-did-not-fire. ⇒ **⑰ must test EVERY LEG of a conjunction separately, not the gate as a unit.**

### 2. ② + THE WHOLE VOCABULARY BLOCK — one sitting, cheapest leverage on the board
Class-8 `SCHEDULED`/`next_due` token, **plus** everything else queued for the same sitting so the vocabulary does not fork:
- **⭐ The three falsification exemplars, none of which is registered as canon** — **AEOLUS** renders `CANNOT FIRE` (a leg has no metric surface) vs `NOT FIRED` (tested, didn't fire); **HENRY** publishes per-leg live counts under an explicit non-latching AND rule; **VULCAN**'s dated retrofit rail. ⚠️ LIQUID's contested X1 adds a **third state neither token covers — `CONTESTED`** (a leg another desk owns is disputed, not down).
- Cadence enum (DAILY/WEEKLY/EVENT-DRIVEN/ON-DEMAND) + PROME's **MONTHLY** for print-keyed desks — **one vocabulary family with the Class-8 token; design in one breath or they fork.**
- Class 9 prose-glyph register · ⚖️ decision-role marker · AEOLUS's `total · range · moved · fired` convergence display form.

### 3. ⑯ + ⑪ paired — the false-clean generators
Activity-proxy guard blind spot (AEOLUS self-report) **and** hardcoded-catalyst-list-in-boot (ZHAO). **Same defect class — an instrument that returns green because of how it was built, not because the world is green.** Running them as one pass costs barely more than one and the shared root cause is the deliverable.

### 4. ㉔ READ-CAP EXPOSURE — cheap now, because the founding instance is already fixed
**Discharged on my own surfaces 8/23** (FLEET_MAP was at 121% and truncating at every boot for ~6 days; register went cold, `read_cap_check.py` built and closeout-wired). What remains for 8/28 is only the **fleet question, base-rate first**: how many desks carry a mandated boot read over the cap? ⚠️ **Already measured and flagged to PROME (`d0edc0d02`): `INDEX_COLD.md` 108% — OVER, cannot be read whole · `HEARTBEAT.md` 81% · `ROSTER.md` 66% · root `CLAUDE.md` 59%.** ⛔ **Not mine to fix; the sweep's job is the base rate and the recommendation, never the edit.**

### 5. ⑳ BOOT-SEQUENCE AUDIT — **SCOPED TO 5 DESKS, AND I WILL SAY SO IN THE OUTPUT**
PAT-125, HOMER-named. ⚠️ **The unit is DELIVERED CONTENT, not step text** — the naive form ("does boot list the file?") passes both measured legs and finds nothing. That makes it the most expensive leg here, because each desk means executing its boot and diffing what the instrument RETURNS against what the step CLAIMS. **Fleet-wide is not landable in one session. Five desks, chosen for boot complexity, reported as a base rate with the sample named** — never as fleet coverage.

### 6. ① R1 GENERIC BOOT-LEG — **first tranche + a coverage count, not all ~30 surfaces**
The sweep's founding charge, and it **cannot be deferred**: withdrawal leg (b) needs ≥80% active-boot receipt coverage by **9/26** (DOCKET row 204), and ③b says the 8/28 sweep *is* part of "landing". **The BUILD is separately scheduled ~8/25-27** (capable-cased per §9/★, blueprint REQUIRED-element encode in the SAME commit). So 8/28 = **wire a first tranche and publish the coverage percentage.** ⚠️ **If the build slips past ~8/31 I flag it as a landing slip and row 204 slides with it — I own naming that, and I will not let it slide silently.**

---

## DEFER — 12 items, each with a reason and a destination

| Leg | Why deferred | Destination |
|---|---|---|
| **③** SAM fleet-observability (Will-withheld half of row 56) | Will-withheld — **not mine to reopen** | Stays with Will |
| **④** steel uninstrumented · **⑨** company-level physical-capacity | **Ownership questions, not wiring defects.** Nearest seat (MIDAS) has a charter that EXCLUDES it — so the answer is assign / log-as-known-gap / drop, which is a PROME decision row | **PROME decision rows** |
| **⑧** derived-vector staleness predicate | Real, no clock, and it wants the ⑰ output first (a predicate over metric surfaces) | Sweep #2, after ⑰ |
| **⑩** H1-title vs Version-field drift | Real, n=3, cheap — but it is a **pointer-rot variant of the same class ⑰ audits**, so running it before ⑰ duplicates the walk | Fold into ⑰'s pass |
| **⑫** catalyst-countdown FORK AUDIT + `date_class` | ⚠️ **Partly OBE:** LABOR root-caused the countdown defect itself on 8/23 (PAT-131 — the print-gate). The FORK question survives; the countdown half does not | Re-scope, then sweep #2 |
| **⑭** cross-addressed catalyst rows have no transport · **⑮** VULCAN close-the-loop | Both answered live already; what remains is encode-and-verify, which is packet work not sweep work | Owner packets |
| **⑲** CLAUSE-GEOMETRY DRIFT | ⚠️ **Revised TWICE since I verified it — the register says re-read at the window, do not work from the verified version.** Re-reading is itself the first step and it may re-scope | Re-read at window; likely sweep #2 |
| **㉒** rate a boot fallback by what the value FEEDS | Real (OZK, verified at `:52`), and it is a **grading rule for ⑳'s output** rather than an independent walk | Apply inside ⑳ |
| **㉓** REDACTION-FOR-SCOPE suppresses the falsifier | HOMER-named, carried with permission. **Deep and it deserves a real pass**, not a tail-end slot | Sweep #2 / soak |
| **⑬②/⑬⑤** memory-retrieval wording | **Will-gated wording** — rides the date as a deliverable, see below | With Will |

---

## RIDES THE DATE — Will-gated, must land because someone is waiting

- **㉑ HANS / `EUROPE_MACRO` SUCCESSOR NOMINATION** (Will-commissioned 8/23, `6131d53b3`). **Nomination-only memo** — revive-HANS vs successor-desk vs triage-depth, plus interim parking for unowned signals. ⛔ **Return path is memo → PROME registers a WILL_QUEUE row. NEVER direct to Will. No build, no recharter, no roster edit.** ⚠️ Falsification #2 is relevant input: **HANS has no falsification rail I could find, and its FLOW.tsv is +111d rotten on a reversed war frame** — that is evidence for the nomination, not a separate flag.
- **⑱ GENERATED-VIEW BUILD-OR-DECLINE** (Will 8/22, *"approve on the waiting decision"*). ⚠️ **DECLINE is an explicitly legitimate outcome** — the fold bought a DATE, not a commitment to build. Scope guards: no second store · labels canonical-map-derived · §12 base-rate-before-wiring.
- **⑬②/⑬⑤** memory-retrieval wording → Will.

---

## What changed in the register TODAY, after it was written

1. **㉔'s founding instance is discharged** (my own surfaces), which is why it moved from expensive to cheap.
2. **⑫ is partly OBE** — LABOR root-caused the catalyst-countdown defect itself.
3. **⑰ is strengthened** — L-31 gives it the conjunctive variant and a per-leg test requirement.
4. **② gained the three exemplars** plus a fourth state (`CONTESTED`).
5. 🔴 **NEW CANDIDATE, not yet registered — a profile's self-declared staleness trigger is prose that NO boot step evaluates.** AEOLUS's own `(P)` predicate had fired **twice** (AEO-06, AEO-11 both HIT) and reached nobody; I fixed the *queue-row* half today (`resolve_by`), and **this half is still open.** Same class as ⑪ and ⑯: a trigger that exists and is never read. **Recommend registering as ㉕.**

---

## BOTTOM LINE

**18 real work items. I land 6, and I say which 6 in advance rather than after.** The other 12 have named destinations, and 5 of the register's rows were never work items at all — 2 discharged, 3 method rules that should apply to every leg rather than be "completed" once.

**The riskiest thing on this list is not any leg — it is ①'s 9/26 clock.** Everything else can slide into sweep #2 without breaking a promise; ① is wired to a withdrawal-leg coverage target with a registered DOCKET row. **If its build slips past ~8/31, I name the landing slip and row 204 slides with it.**
