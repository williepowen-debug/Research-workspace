# Falsification Freshness Sweep — RUN #2

**Date:** 2026-08-23 (cadence ~8/24 — **ON TIME, 1d early**) · **Scope:** fleet-wide, 32 surfaces / 23 agents scanned + judgment reads + 4 added legs
**Method:** solo. Mechanized detection (`scripts/falsification_scan.py`, on the 8/17-fixed scanner) → judgment read of **every** flag → added legs by hand.
**Run #1 was 2026-08-03.** This run is the **L5 cadence proof point** Will held the grade on 8/20; the leg had failed three times prior.

---

## Headline

**4 STALE-FLAGGED by the scanner → 2 REAL, 2 WITHDRAWN on read (50% over-flag).** Both withdrawals share **one** root cause in my own instrument.

**But the flags are not the finding. The finding is in the CLEAN buckets:**

> 🔴 **F1 — The scanner files SEVEN MARKET agents under *"falsification not applicable… Expected for utility/meta agents."*** BROCK · CRUISE · HANS · HOMER · LABOR · SHADE · ZHAO. Market is the one class where the L3 ladder **requires** a dated falsification surface. Four of the seven have real rails the instrument cannot see; three have real gaps it also cannot see. **Either way the bucket label is false, and it reads as a clean bill.**

This is **run #1's F5 defect surviving in the neighbouring bucket.** F5 v2 (8/07) fixed "has a thesis, no surface" — it never touched "no thesis file at all," which silently absorbs any agent whose thesis lives in `STATUS.md`. Same detector artifact, one bucket over, undetected for 20 days.

---

## 1 · Scanner flags — judgment read (playbook §5: no flag leaves the desk unread)

| # | Agent | Surface | Scanner | Verdict after read | Why |
|---|---|---|---|---|---|
| A | FALCON | `thesis/CHANGELOG.md` | STALE 21d, "cites v1.0 vs live v2.1" | ⬇️ **WITHDRAWN** | File is **forward-chronological**; newest entry is `2026-07-30 — THESIS v2.1`, which **matches the live thesis exactly** (v2.1 @ 7/30). Nothing is owed. Scanner took the version token from the **oldest** entry. |
| B | MARCO | `thesis/CHANGELOG.md` | STALE 22d, "cites v3.0 vs live v3.1" | ⬇️ **WITHDRAWN** | Top entry is `## v3.0 → v3.1 (2026-07-31)`. **v3.1 IS logged.** Scanner read the **FROM** side of a transition heading. Thesis has not moved since 7/31, so no entry is owed. |
| C | LIQUID | `thesis/CHANGELOG.md` | STALE 59d | ✅ **CONFIRMED — RECURRENCE** | Newest version entry is `## v2.0 — 2026-05-19`. This is run #1's **F3 unresolved and worse** (39d → 59d). |
| D | LIQUID | `workbook/KILL_MEMO_HY_OAS_260.md` | STALE 37d | ✅ **CONFIRMED, severity corrected DOWN** | Header claims **"Current state (7/17)… HY OAS 271bps [7/15]"** while STATUS (8/23) reads **275bps [8/20]**. ⚠️ **Directionally CONSISTENT** (both say un-armed) — so this is staleness, **not** the inversion I expected. Still real: it is a *pre-written decision memo meant to be read under tape pressure* carrying a five-week-old level. |

### 🔴 F2 — ONE scanner defect explains BOTH withdrawals (self-inclusion, PAT-050)

`falsification_scan.py` **dates** a changelog correctly (max date wins, order-independent) but **versions** it by first-match. Two failure shapes, both live this run:
- **forward-chronological file** → grabs the oldest entry's version (FALCON)
- **`vX → vY` transition heading** → grabs `vX`, the FROM side (MARCO)

Both manufacture *"cited version < live version"* ⇒ a false "revision behind." ⚠️ **FALCON's file additionally declares "Reverse chronological" in its own convention block and is not** — inherited wholesale from HAWK at the 7/12 spinout. A file that misdescribes its own ordering will defeat any order-dependent reader, so **the fix must be order-independent**: take the version token from the entry with the max date, and on a `vX → vY` heading take `vY`.

**Run #1 over-flagged 4 of 13 (31%); run #2 over-flagged 2 of 4 (50%).** The rate did not improve. Both runs' over-flags came from version/vintage *extraction*, not from the threshold — **the threshold has never been the problem.**

---

## 2 · 🔴 F1 in full — the "not applicable" bucket

Verified per agent (rail present? where?):

| Agent | Class | Rail found | Reading |
|---|---|---|---|
| BROCK | Market L4 | `STATUS.md:172` **EXIT RULES** + thesis-kill decision tree | **False clean** — rail is real and rich |
| ZHAO | Market L3 | `STATUS.md:134` **EXIT RULES** / Thesis Kill / Falsification tripwires | **False clean** — and a tripwire **FIRED 8/12**, graded 8/21 |
| LABOR | Market L5 | `STATUS.md:179` **EXIT RULES** | **False clean** |
| CRUISE | Market L3 | `STATUS.md:118` **Exit Rules (Falsification)** | **False clean** |
| SHADE | Market L3 | `STATUS.md:105` — self-labelled *"detailed, **not** a thesis kill"* | **Real gap, owner-honest** — matches its FLEET_MAP row |
| HANS | Market L3 | none found | **Real gap** (agent is stale on several axes) |
| HOMER | Market L2 | `thesis/PREDICTIONS.tsv` only | **Real gap, already known** — my 8/22 review found the thesis-level rail absent under any name |

**4 false cleans · 3 real gaps · 0 correctly classified.** The bucket has no diagnostic value as written.

⛔ **Note the direction of harm.** A false STALE-FLAG costs a read (cheap, and I caught all of them). A false *clean* costs nothing today and everything later — and this bucket prints a reassuring sentence over seven market desks. **The instrument's dangerous errors are all on the quiet side.**

---

## 3 · F5 v2 applied (playbook §F5 v2, from run #2)

Scanner's "has a thesis, NO separate falsification surface (3)": **AEOLUS · MIDAS · OSPREY.**

| Agent | Predicate: "no surface, OR a surface with no evidenced fire path" | Verdict |
|---|---|---|
| **AEOLUS** | `STATUS.md:158` **EXIT / INVALIDATION** table, 6 channels, standing-rule │ state │ verdict. **Fired count 1 of 6 — C5 FIRED 8/18, condition broke 8/20, recorded as "FIRED — then reversed."** | ✅ **PASSES** — evidenced fire path |
| **MIDAS** | `THESIS.md:77` **EXIT / INVALIDATION (standing-rule-vs-state triad)** | ✅ **PASSES** — local form, F5 v2 ¶3 |
| **OSPREY** | `thesis/THESIS.md` numbered kill routes; known-defective, owner **correctly refusing self-repair** pending Will-gated rules asks | 🟡 **`LIVE-DEFECTIVE-ESCALATED`** — good behavior, route the ruling, **do not flag the agent** |

**F5 v2 vindicated: 0 of 3 is genuinely rail-less.** Run #1's F5 named five; four were artifacts and only VULCAN was real. The dated-surface gap persists for AEOLUS/MIDAS (rails are undatable-by-inspection) — fix stays **extract-and-stamp**, not author-from-scratch.

### ⭐ VULCAN — the retrofit exemplar, graded

`workbook/EXIT_PROTOCOL.md` opens **`Kill rail re-derived: 2026-08-13`** and states in its own header that VULCAN carried no kill tree, no EXIT_PROTOCOL and no dated falsification surface across 16 files from build 7/10 until that date. **Reference-grade on three counts:** a dated stamp at the top; scope discipline (*"This file holds kill/exit conditions and nothing else"*); and it **names its own prior absence** rather than presenting as always-having-existed. **This is what the F5→extract-and-stamp path is supposed to produce.** The sole rail-less agent of run #1 is now the model for run #2.

---

## 4 · NEW LEG — L-31 conjunctive gates against the live regime (AEOLUS-donated, run fleet-wide)

*"Read every CONJUNCTIVE gate/flip against the LIVE regime — AND-clauses are the hiding place."* Candidate population: 12 agents carrying uppercase-AND conjunctions in rail surfaces.

### ⭐ Reference implementation — HENRY
`STATUS.md:157` **H-1 simultaneity, non-latching**: twin soft-kill fires only when *VIX <15 AND HY OAS <260 for 5 consecutive sessions, **both satisfied on the SAME session***; *"a leg that ceases to be satisfied ceases to be fired. No leg banks."* Live count published as **"0 of 2 CURRENTLY satisfied · 1 of 2 EVER satisfied (VIX, 8/7)"**, with the explicit line *"cannot be part-fired — it is an AND."* And the **old triple-AND was RETIRED 6/23 when one leg was empirically falsified.** ⇒ **HENRY already does everything this leg asks.** Adopt as the fleet form.

### 🔴 CARL — operator precedence, unparenthesised (real, unflagged)
- **CRL-22:** `UNH MCR ≥85.4% OR ELV BCR ≥88.3% AND V28 RAF final adverse`
- **CRL-23:** `DHI GM ≤17.5% OR PHM GM ≤22.0% AND tariff regime ≥10% sustained`

**Mixed OR/AND with no parentheses is genuinely ambiguous** — `(A OR B) AND C` makes leg C mandatory; `A OR (B AND C)` lets A alone resolve it. **The two readings falsify on different evidence**, so the prediction cannot be graded without picking one, and nothing on the row says which. Not a wording nit: it decides what would count as being wrong.

### 🟠 CARL — three-leg AND, base rate un-derived
`THESIS.md:81` kill condition: `Brent <$80 AND gas <$3.50 sustained 4+ weeks AND pipeline DQ acceleration reverses ≥10bps over the same window`, **plus** a "stickiness clause" that keeps the thesis alive even if oil reverses. Three simultaneous legs and an escape clause — **PAT-072: base-rate a compound gate conditional on its own trigger state, and the silent failure is the kill side.** No base rate is recorded.

### 🔴 FLG — my own build, and I mis-stated it in FLEET_MAP today
`workbook/EXIT_PROTOCOL.md:24` K-1: `loans_qoq_pct > 0 for 2 consecutive filed quarters **AND** nonaccrual rate falling across the same 2 quarters`.
The row's own **`Instrument`** cell names `loans_qoq_pct`, `total_loans_k`, `total_assets_k` — **the nonaccrual leg has NO registered metric surface.** That is the **AEOLUS C4 shape exactly** (leg 1 satisfied, leg 2 unevidenced ⇒ displays "NOT FIRED" while the truth is CANNOT-FIRE-CLEANLY).
⛔ **And in the FLEET_MAP cell I rewrote this morning I wrote that K-1 is "ONE PRINT from firing."** That is leg 1 only. Corrected in-register this session.
Also `:105` — `RGB grants rent increases **materially above** the recent run-rate … AND multifamily nonaccrual falls`: **"materially above" is unquantified**, so that leg is ungradeable by inspection.

### L-31 generalized
> **A conjunctive gate whose weakest leg has no metric surface renders as `NOT FIRED`, which is indistinguishable from `tested and did not fire`.** The AND does not merely hide a leg — it **launders an ungradeable leg as a negative result.** AEOLUS is the only desk that renders the distinction (`⚠️ UNGRADEABLE — no metric surface` / **`CANNOT FIRE`**). **Proposed fleet form: AEOLUS's verdict vocabulary + HENRY's per-leg live count.** Both already exist; neither is registered as canon.

---

## 5 · Self-inclusion (playbook §6, PAT-050)

- 🔴 **F2 above** — the version-extraction defect is mine, n=2 in one run.
- 🔴 **F1 above** — the bucket label is mine, wrong for 20 days.
- 🔴 **FLG K-1** — I built the rail, then mis-described it in the register I own, the same day.
- 🔴 **LIQUID FLEET_MAP cell** — I carried the 8/7-vintage *"every surface reads HY 287/3-of-3/280-CROSSED"* inversion into the cell I rewrote **this morning**. LIQUID's STATUS (8/23) reads **275bps [8/20], un-armed, 280 broke 8/3** — the desk serviced it and my carried claim was stale on arrival. Corrected. *This is the exact `finding_dated_carry_item_has_no_expiry_check` class, committed during a rotation whose stated purpose was removing stale carry.*
- ✅ **AEOLUS corrected MY pointer and it stands:** my PR#4 ACTION 2 cited `THESIS.md:80` as publishing the retired Kaub/Duisburg trigger; *"Duisburg appears nowhere in THESIS.md."* AEOLUS notes the line was stale **in a different and worse way** and that **the finding survives the corrected pointer.** Recorded as-is — the pointer was wrong, the finding was not.

---

## 6 · Dispositions (packet-only per playbook §Dispositions — re-scoping kill criteria is DOMAIN judgment)

| Target | Item | Action |
|---|---|---|
| LIQUID | C + D: CHANGELOG 59d (**run #1 F3 recurrence**) · KILL_MEMO "Current state (7/17)" vs STATUS 8/23 | **Packet** |
| CARL | CRL-22/23 operator precedence · 3-leg AND base rate | **Packet** |
| FLG | K-1 nonaccrual leg has no instrument · `:105` "materially above" unquantified | **Packet** (register corrected by me; the rail is the owner's) |
| OSPREY | `LIVE-DEFECTIVE-ESCALATED` — pending Will-gated rules asks | **No flag.** Route the ruling |
| FALCON, MARCO | withdrawn | **No packet.** FALCON: note its changelog misdeclares its own ordering |
| AEOLUS, HENRY, VULCAN | exemplars | **No action** — cited as fleet forms |
| DAEDALUS | F1 · F2 · FLG cell · LIQUID cell | **Mine.** Register fixes done this session; scanner fixes are builds |

**Nothing was direct-edited on any agent's falsification surface.** Zero pre-approvable FROZEN-banner cases arose (no retired-but-unfrozen kill trees this run).

---

## 7 · Legs NOT run — stated, not silently dropped (PAT-129)

- **Negative-resolution leg** (8/17, ~80 keyword-candidates / 23 ledgers): **NOT RUN.** It is a per-owner judgment classification across every prediction ledger and does not fit beside F1+L-31 in one solo session. **Carried to run #3 (~9/14)**, or to the 8/28 wiring sweep if it fits.
- **Census map hand-derivation of the 20 un-rowed agents** (`upgrades/PROFILE_S3_AUDIT_2026-08-11.md`): **PARTIAL** — F1 hand-derived 7 of them (the market subset, which is where the ladder binds). 13 remain.
- **Retrofit uptake — 4 extract-and-stamp packets:** VULCAN's author-rail verified ⭐; the other three **not individually verified** this run.

---

## 8 · WRITE-BACK, same evening — LIQUID (verified at `9467d562d`, not taken from the packet)

Both flags actioned within hours. **CHANGELOG appended, not two-stated** (owner's call and the right one — the movement was real, so the log should carry it); **KILL_MEMO relabelled dated-as-of rather than re-stamped**; conviction re-marked **61% → 56%**, with an over-correction counter-check written into the entry, and **three of the four downgrades sourced from evidence LIQUID generated and graded as losses against itself.**

### ★ The owner's finding is sharper than my flag — and it changes the pattern

I flagged the CHANGELOG on **age alone (59d)**. LIQUID opened it and found what the gap had swallowed:

> **`7/29 — THE X1 LIQUID HALF TAGGED FOR THE FIRST TIME. HY OAS 287bps, sustain 3-of-3 (281→284→287).`** — the first fire of the widening side of its ladder, **the event the whole ladder exists for**, with no entry. The same staleness had also eaten the 7/27→8/3 excursion.

⇒ **PAT-060 extended with a new half: a gap in an append-only falsification log is NOT uniformly costly — it preferentially swallows the RARE event, which is the one the log exists for.** A routine observation gets logged because logging it is the cheapest remaining act of a session; a first-ever fire lands on the busiest possible day and is the most deferrable write-up, because everyone involved already knows it happened. **So a day count always understates a falsification-log gap, and the understatement grows with the gap.** Operationally: when flagging a stale append-only falsifier, do not report the age and stop — **ask the owner what FIRED during the window.** The age is a proxy for a question nobody asked.

### 🟡 L-31 — I published n=3 and it is n=2 clean + 1 CONTESTED (owner's own retraction, hours later)

LIQUID's own new entry: **`7/27 — BROCK's wrapper-leads half FAILED independently`… "X1 is CONJUNCTIVE, so with this half down no HY level alone can fire it."** A live gate that cannot fire whatever the tape does, with the dead leg unrevisited for four weeks. Same shape as AEOLUS C4 and FLG K-1 — **three desks, three independent instances, in one sweep.** That is no longer a per-desk defect; it is a fleet-level vocabulary gap, and it strengthens the case for promoting AEOLUS's `CANNOT FIRE` / `NOT FIRED` distinction to canon at the 8/28 vocabulary block.

⚠️ **RETRACTED IN STRENGTH BY LIQUID ITSELF, same night, against its own interest** (`adef47b6f`, verified at the artifact).

LIQUID took the PAT-060 operative move this run produced — *ask what FIRED during the window* — and ran it on its **own** five falsifier surfaces rather than banking it. It opened the Q2 BDC mark card (KB-LIQ-083, built 7/18 for a 7/25–28 window, unopened 36 days) and **graded it CONFIRM at filing-primary.** CONFIRM's registered consequence is *arms the BROCK wrapper-leads X1 half* — the exact half it had told me hours earlier was down.

BROCK's 7/27 failure was on **HY tranche decomposition**; the card is the **BDC-mark face of the same conceptual half.** Both can hold — wrapper NAVs grinding down while index spreads move on beta is the Stage-3→4 sequencing the monitor exists for — **but that is a hypothesis, not an adjudication.** ⇒ **The half is CONTESTED, not down, so X1 is not a clean `CANNOT FIRE`.** The KILL_MEMO now rules a 280-cross against a contested half as **escalate to BROCK, neither fire nor dismiss.**

⛔ **My rationale was falsified along with the instance.** I called X1 the strongest of the three *because the dead leg belongs to another desk and nothing in LIQUID's own tree would surface it.* **LIQUID's own tree surfaced it** — it just took the pattern to make it open the file. The claim I should have made is the opposite one: **a cross-desk dependency is not unobservable from inside, it is merely unprompted**, and what closed the gap was a question, not an interface.

**Corrected count: L-31 is n=2 clean (AEOLUS C4, FLG K-1) + 1 CONTESTED.** ⚠️ **PROME was told n=3 in my sweep-close message and has been corrected** — the argument for promoting `CANNOT FIRE` / `NOT FIRED` at the 8/28 vocabulary block now rests on two instances, which is still the right call but a weaker one, and it must not be carried at the strength I first gave it.

### ✅ The pattern's operative half validated within hours — at a different desk, on its author's own surfaces

The same sweep found a **graded CONFIRM sitting 36 days past its window**, a self-contradiction, and a **4× measurement error in a pre-registered baseline** (a column headed `Q1 NAV/sh (3/31)` holding the 12/31 value, with the delta beside it describing the move *away from* the level displayed). **None of it came from a day count; all of it came from opening the file and asking what fired.** That is PAT-060's new half working as specified, n=1 live, and the strongest evidence in this run that the operative move is worth more than the threshold.

**PAT-085 extended on the same evidence.** The card had **already flagged its own symptom in writing** — *"P/NAV 0.52 is SUSPECT, smells like a NAV-vintage mismatch"* — and carried it for 36 days; resolving it took five minutes. LIQUID's phrasing: **a written suspicion is not an investigation.** The reason it defers so well is that *writing it down discharges the felt obligation* — a banner advertises debt to a reader, but a caveat in your own file reads to its author as diligence already performed. **The measurable tell is cost asymmetry: a caveat whose resolution is cheap relative to its age is not a caveat, it is an unstarted task wearing one.**

### Not claimed as swept, on the owner's own insistence

Four further LIQUID falsifier surfaces are **aged, named in STATUS, and not yet opened**: EXPECTED_SIGNALS 43d (with a flagged first-movement), HORMUZ lagging-tell 37d (window arrived), CONSUMER_MONOLINES 43d (a month past its own DELETE-BY), ORCL map 36d. **LIQUID explicitly declines to report them as done.** Given what opening ONE card produced tonight, these four are the highest-expected-value queue on any desk right now.

### One I did not flag, owner-found — PAT-052 n+1, cross-agent variant

LIQUID's `THESIS.md` carried *"BOND agent scaffold exists but is not yet active"* while LIQUID and BOND ran live joint work that night. **A stale cross-agent capability claim is worse than a stale number: it does not merely misdescribe a capability, it suppresses a ROUTE** — the reader's correct response to "not yet active" is to stop looking. Fixed, superseded text kept.

### Carried, owner-flagged rather than silently done

`THESIS.md` remains **v2.0 (header 6/25)** and its §3 Leg B/C text now understates two changes. **LIQUID correctly refused to cut v2.1 inside a changelog edit** — a version bump is a separate job, and doing it mid-hygiene is how criteria move without review. Recorded as open in the FLEET_MAP row.

---

## BOTTOM LINE

**The cadence leg is met — run #2 landed a day early, on the fixed scanner.** Two of four flags withdrew on read, both from a single version-extraction defect in my own instrument; the rate did not improve on run #1 and both runs' over-flags came from vintage extraction rather than the threshold.

**The real result is that the scan's reassuring buckets are where the errors live.** Seven market desks are filed under "falsification not applicable — expected for utility/meta agents," a sentence that is wrong for all seven. That is run #1's F5 artifact surviving one bucket over for 20 days, and it is the same lesson as this morning's read-cap breach: **a fix applied to the instance and not the class leaves the residue that breaches next.**

**Both LIQUID surfaces were CLOSED-VERIFIED the same evening, and the owner's read beat mine** (§8: the 59-day gap had swallowed the ladder's first-ever fire, and L-31 reached n=3 on a gate LIQUID found itself). **Two genuinely stale surfaces (both LIQUID, one a run-#1 recurrence), one real precedence defect (CARL), one defective rail I built myself (FLG).** Against that, three desks are running falsification discipline worth copying: **AEOLUS** (renders CANNOT-FIRE vs NOT-FIRED), **HENRY** (per-leg live counts, non-latching AND), **VULCAN** (the retrofit exemplar, dated and scoped). **The fleet forms already exist; what is missing is that none of them is registered as canon.**
