# HOMER — DAEDALUS Structure Review, 2026-08-22

**Will-directed** (method/scope/notify ruled in-session: Mode-A fan-out · targeted C1+C2+C3 · notify at
delivery). **Reviewer:** DAEDALUS · **Companion (evidence):** `HOMER_REVIEW_2026-08-22_READER_REPORTS.md`
**Method:** 4 readers over 3 clusters (C2 split at 220 KB), every finding re-verified by me at the artifact
before routing. **Subject LIVE throughout** — packet-only, zero HOMER files edited, zero HOMER scripts run.
**Pin drifted 4× during the review** (`abc7fc58a` → `f7c63add3` → `f168cb0bd` → …), which is why findings
were graded against the then-current tree rather than a snapshot.

---

## THE GOVERNING FINDING — and HOMER named it, not me

> **A boot sequence is a guard like any other, and nobody has ever tested one against the actual behaviour
> of the instruments it names.**

HOMER's boot has **two independent defects of one family**, both reporting satisfied:

| Step | Says | Actually |
|---|---|---|
| **2** | "Read `STATUS.md` (dashboard **+ BOTTOM LINE**)" | read cuts at **line 73 of 244**; BOTTOM LINE begins at **214**. 74.9% of the file never arrives. The step **names a target its own prescribed instrument cannot reach.** |
| **6** | `ledger_staleness.py HOMER --quiet` | rc=0, 8 green rows, and **structurally blind** to `docket/CATALYSTS.tsv` + `thesis/PREDICTIONS.tsv` (~102 KB of dated obligations) |

**The detail that makes it more than a hygiene note (HOMER's own):** the HOM-01 clause collision this review
found lived in `PREDICTIONS.tsv`, and its twin sat on docket ROW21 — **precisely the two files step 6 cannot
see.** A green check and a live 9-day-old defect, same boot, same desk, same morning.

**This reframes the review.** The individual defects below are evidence for the class; the class is the
deliverable. If it holds elsewhere, *"audit each boot sequence against what its named tools actually do"* is
a fleet check, not a HOMER fix. **Both HOMER instances are `CLAUDE.md` edits and therefore Will-gated;
HOMER has changed neither.**

---

## FINDINGS — ranked, all re-verified at artifact

### 1. 🔴 TIME-CRITICAL — HOM-01 clause collision · **ROUTED AND RESOLVED SAME EVENING**
Leg-1 confirm and early-kill arm 2 both fire for any July FMHPI print in **1.90–2.06%**, unranked, while
the kill's *"do not wait for the Aug-data print"* forecloses the **only remaining test of Leg 2**. Verified
at `PREDICTIONS.tsv` cells and independently at `CATALYSTS` ROW21, which states both outcomes as if
mutually exclusive. Swept the other 10 non-RESOLVED docket rows: **no further collisions — isolated, not
systemic.**
**Routed `e6b60df7a` → HOMER RULED IT BEFORE THE PRINT (`422f9505f`)**, choosing the two options that cut
against its own prediction, and freezing the threshold rather than re-levelling.

> ★ **HOMER'S CORRECTION IS THE BETTER FINDING, and it is a NEW CLASS.** I framed the clauses as written
> ambiguously. They were not. **At registration they were DISJOINT** — with May at +1.9%, "J below May" and
> "J above +1.9%" could not both hold, and the grading sheet's decision table is built on that geometry.
> **The June vintage revised May to +1.58% and the band opened.** Nobody erred; nothing announced the day it
> broke.
> ⇒ **Any spec pairing a FROZEN ABSOLUTE level with a VINTAGE-FLOATING RELATIVE comparator drifts into
> overlap as the series revises beneath it. Re-reading the spec cannot catch it — both clauses stay
> individually well-formed — only re-evaluating the clause GEOMETRY against the current vintage can.**
> Registered by PROME as 8/28 sweep item ⑲ (packet `2026-08-22c`, **re-read at the window — revised twice
> since**). PROME's scan-unit correction rides it: the two clauses sat in different **COLUMNS** of one row
> (`Prediction` / `Invalidation`), so **a scan keyed on single-field text returns clean on the founding
> case**; the unit is the row's clause set across all resolving fields, and where it cannot be assembled
> mechanically the checker reports **UNSCANNED, never clean**.

### 2. 🔴 DELIVERY — two surfaces truncate, and the brief's loss is total where it counts
| Surface | Cut | Lost | Character of the loss |
|---|---|---|---|
| `STATUS.md` | 73/244 | 74.9% of bytes | predictions, open items, catalysts, BOTTOM LINE |
| `NEXUS_BRIEF.md` | 74/96 — literally `## CROSS-DOMAIN` | 12.3% of bytes | **100% of content addressed to a named agent** |

**The brief loses far less and matters far more:** STATUS's reader is HOMER, who wrote it and can page back;
the brief's readers are **three other desks** absorbing it alongside their own boot, and the part they lose
is the part with their name on it. **Second-order, and the sharpest structural point of the review:** the
brief is correctly **newest-first**, and that ordering is exactly what puts `CROSS-DOMAIN` last — *last means
undelivered.* **Chronology and consumer-addressing are in direct conflict here.** Cheapest fix touches no
size question: **move `**SENDING:**` above `## VIEW`.**
**Root cause of the size, and HOMER found it first:** the 250-**line** cap is aimed off-axis on a file whose
growth mode is **bytes** — five "compressed for the 250-line cap" operations folded blocks into single lines,
**raising B/line and pushing more content past the cut.** HOMER self-diagnosed this at `STATUS:163` the same
day and **deliberately did not act, citing Critical Rule #2 because a review was in flight.** Correct
conduct. What it lacked was *where the cut falls*; delivered.

### 3. 🔴 A TWICE-RULED SPEC HAS NO DURABLE HOME
The Servicer Watch **A–G** classes — Will-ruled **8/14 and 8/22 ("approve both")** — appear in `CLAUDE.md`
**not once**. Their five homes: `SCRATCH.md` (rewritten at closeout by its own `:3`) · `STATUS.md`
(rewritten each session, and past the cut) · `NEXUS_BRIEF.md` (refolded, truncates before it) ·
`docket/CATALYSTS.tsv` (outside every staleness instrument) · `reports/` ×3 (not in FILES, not boot-read).
**Not one is both durable AND read** — and it violates HOMER's own `:170`: *"a number that lives only there
is destroyed on the next rewrite."* R1 called it *"the one I would not defer"*; concur.

### 4. 🟠 CROSS-AGENT — REGINALD is never told a registered band was crossed
`STATUS` says three times that Freddie MF at 0.51% **crossed the >0.50% RED band**. The string `0.50%` is
**absent from the entire brief**, and nothing in REGINALD's tree mentions a band crossing — it holds the
*level* from a July packet and the 7/31 retraction, nothing more. HOMER owns the metric **and** the band;
REGINALD is the registered consumer of that watch. **PAT-063 in pure form.** Compounding: the owed GSE-MF
band re-spec (`SCRATCH:116`) is also absent from the brief. **Recommend routing via PROME** — a two-desk
routing gap, not a HOMER hygiene item.

### 5. 🟠 THRESHOLD RAIL — the reputation is earned, by two rows of thirteen
**2 exemplary · 2 clean · 7 basis defects · 3 broken today.** Three broken, all mechanically checkable:
- **Cure Rates `:88` — comparator INVERTED.** `>-15%` is satisfied by −10% (an *improvement*); −40%
  satisfies none of the three bands. **Row 13 uses `<` correctly for a falling metric — the author knows the
  form.** Four-character fix, zero judgment.
- **National Foreclosures `:83` — uninformative under EVERY basis.** Filings and starts permanently ≥Red;
  REO can never fire. Sits **nine rows above its own autopsy** (the DISARMED FL-YoY row, retired for this
  exact class, inverted).
- **90+/FC `:87`** — Source says MBA; practice grades an MBA/ICE composite.
**Structural, and it sets the fix's shape:** for four rows the missing basis **already exists elsewhere**
(row 10 in HOM-02, row 8 in `STATUS:68`, row 3 in `STATUS:100`, row 4 ruled at CARL 7/16). So `:94`'s claim
that this table is the durable-bands home is **false in practice** — the discipline exists and is scattered
across ephemeral or foreign surfaces. **The route is "apply your own FL template to the other eleven rows,"
not "learn a new standard."**

### 6. 🟠 SMALLER, CONFIRMED
`:79` tells CARL a superseded FMHPI trough (blast radius contained — CARL holds a dedicated 7/31 correction
packet; whether the *second* revision reached it is **unverified**) · one of two ~9/4 dated kills is
undocketed on both surfaces HOMER's own SCRATCH names · SCRATCH presents a Will-ruled question as still
open, **inside a commit claiming it was swept** · a "standing fix" lives only in the file guaranteed to be
erased · `CRL-06` asserted as CARL-owed **37 days after CARL resolved it using HOMER's own data package** ·
`(see Open Items)` dangles — **and it is the only elaboration of the CORAL/MARCO Florida seam**, on Will's
top-priority geography · stale unlabelled dashboard rows (`:123` refuted mechanism live at 🔴; `:182` PMMS
four weeks stale describing the *opposite* regime; `:125` duplicate Housing Starts).

> **On the supersession-label finding, the framing matters more than the defect:** `:69` is unlabelled, but
> `:63` — one row away, same Q1/ATTOM vintage — carries a model rider. **HOMER labels supersession well and
> missed one row.** That is a different packet from "HOMER doesn't label supersession," and only one of them
> lands.

### 7. 🟡 GUARD THAT CANNOT FAIL — found twice, independently
The NEXUS fold-ordering rule's "checkable form" (brief commit ts ≥ STATUS commit ts) **cannot discriminate
when both files land in one commit** — which they did on **all four** 8/22 commits. R1 (n=3 from git log) and
R3 (4 commits) found it from different files. **My full-history walk narrows it correctly: 20 commits carry
both, 14 STATUS-only, 7 brief-only — so the check CAN discriminate, and did not on the day it was relied on.**
Not "structurally vacuous"; "degenerate whenever both files ship together."

---

## MATURITY LADDER — per-leg verdicts (idea 4, Will-ruled 2026-08-20)

**Class: Market. Grade: L2 HOLDS. Conf H.** Every leg gets a verdict so a skipped leg reads as a blank.

| Leg | Verdict | Basis |
|---|---|---|
| **L0** dir + CLAUDE.md | **PASS** | 233-line charter, richest threshold apparatus in the fleet at its best rows |
| **L1** STATUS + BOTTOM LINE | **PASS** | both present, current (8/22), **but BOTTOM LINE is structurally unreachable at boot** — flagged, not failed: the artifact exists and is correct |
| **L2** structured record accruing | **PASS** | 8 workbook ledgers two-stated, all 7 LIVE carrying content-vintage headers refreshed 8/22; KB.tsv correctly FROZEN; board_log current |
| **L3** convergence matrix + exit rules + predictions resolving + **dated falsification surface** | **FAIL — one leg, unchanged since 8/07** | predictions RESOLVING ✅ (reference-grade, see below) · dated surfaces ✅ (10 of 11 datable) · **convergence handles NOT BUILT** ❌ · **thesis-level kill rail ABSENT — greenfield, author-from-scratch** ❌ |
| **L4** TRADE.md feeding proposals; signals flowing | **NOT-ADJUDICATED** | out of this review's targeted scope (C4/C5 unread); do not infer |
| **L5** clean closeouts, zero flags, current | **NOT-ADJUDICATED** | same |

**L3's blocker is unchanged from the 8/07 profile and re-verified**: `thesis/` holds `PREDICTIONS.tsv`
alone; no `THESIS.md`; no kill vocabulary anywhere under any name (11 variants + heading sweep + filename
find, corroborated by a second independent grep).
⚠️ **WARN ANY BUILDER:** the per-prediction machinery is unusually strong and **will look like the missing
rail. It is not** — it covers two metrics; the thesis covers a transmission chain.
⚠️ **NOT DELIVERED BY THIS REVIEW:** blueprint conformance on the threshold dimension. R1 declared it —
*"I DID NOT GRADE HOMER AGAINST THE BLUEPRINT… every verdict is INTERNAL CONSISTENCY"* — and no other reader
covers it. **An open gap, recorded rather than papered over.**

---

## WHAT IS STRONG (do not "fix")

- **★ THE NUMBERS ARE SOUND.** ~63 figures reconciled brief-vs-STATUS: **62 AGREE, 1 disagrees.** The
  reader's own conclusion: *"A figure-level audit of this desk returns clean and misses everything."* The
  defects are **delivery, addressing, state tokens and registration** — not analysis. **This belongs in the
  packet as prominently as any finding.**
- **★ GRADING IS LETTER-HONEST UNDER ADVERSARIAL READ.** A kill arm fired on HOM-02; HOMER held a mechanism
  that would have excused the miss and wrote *"⛔ THIS DOES NOT RESCUE THE PREDICTION AND I AM NOT USING IT
  TO."* No moved goalposts anywhere in the cluster. **Caveat stated: n=0 predictions have actually closed** —
  proven on interim grades, not yet on a completed MISS.
- **The FL band pair + its derivation apparatus is the strongest threshold work in the repo.** Levels trace
  to sourced years or self-labelled brackets; one band was deliberately made *less* sensitive, argued; the
  all-time-peak anchor was **declined** with the reason. Nothing to fix; resist edits.
- **The A–G servicer spec is fleet-exemplary conjunctive-gate practice** — base-rated across 32.3
  company-years, Class F ruled to n=1 rather than left ambiguous, Class G labelled UNTESTED **with a
  discharging condition**, and the spec **refused to fire retroactively** on the event that motivated it.
- **`LESSONS.md` writes MECHANISMS**, and self-corrects toward mechanism *in the same session* — *"a lesson
  scoped to the instance that produced it will miss its own siblings."*
- Retractions are consistently **louder than the claims they kill**; freshness is **content-vintage, never
  mtime**; the closeout docket sweep was verified **working**.

---

## CORRECTIONS TO MY OWN RECORD (this review generated four)

1. **A carried claim was stale and HOMER closed it today.** The PREDICTIONS mirror write-back I had carried
   since PR#4 was closed 8/22; `STATUS:192` credits the packet **by name**. Dropped.
2. **I asserted a scanner defect that does not exist.** I told HOMER — in a committed packet *and* a
   doorbell — that `falsification_scan.py` keys on `Date_Resolved`/`Outcome` and would false-flag it. It
   contains **neither string**. A reader raised it as a general caution and could not see my file; I
   propagated it without opening it. Retracted to HOMER.
3. **A true finding rested on false evidence.** I wrote that HOMER "already committed to the level reading"
   when grading arm 1. It had not — June's print satisfied the direction *and* level readings identically,
   committing it to neither. **HOMER's framing is the keeper: *"you had a true defect resting on false
   evidence, and a reader checking the evidence could have discarded the defect with it."***
4. **My sequencing was inverted** (①→②③ should be ②→①) — see finding 1.

> ### ★ THE SELF-CRITICAL CLAIM HOP — the review's best transferable lesson, and it is HOMER's
> Correction 2 travelled **three hops** — a reader that could not see the file, me, and HOMER — and **every
> one of us was being conscientious.** HOMER's diagnosis: *"WALTER's claim was about the WORLD. Yours was
> about ITSELF, and unflattering. A self-critical claim arrives pre-authenticated."*
> **The shape is a HOP, not an agent: the confessor under-checks because confessing feels like rigor; the
> receiver under-checks because doubting a self-criticism feels ungenerous. Neither end applies the ordinary
> standard, so a self-critical claim travels FURTHER than a flattering one would.**
> Extends `finding_asymmetric_rigor_counterparty_claims`, which both of us held and both of us read as
> pointing only at our *own* retractions and at claims in a peer's *favour*. It points at a peer's claims
> **against themselves** too.

---

## FLEET-LEVEL OUTPUTS (this review's real yield)

| # | Output | Home |
|---|---|---|
| 1 | **Boot sequences are untested guards** — audit each against its named tools' actual behaviour | 8/28 sweep candidate; HOMER's framing |
| 2 | **Clause-geometry drift** — frozen absolute + vintage-floating relative ⇒ silent overlap | 8/28 item ⑲ (PROME); n=1 MEASURED, definition-only |
| 3 | **⑰ base rate ANSWERED** — ~95% does NOT hold on a strong desk (≈25% broken); **(b)-leg confirmed 10-of-10 unstated BASIS** (MARCO 5-of-6 → two independent desks) | register ⑰ |
| 4 | **`ledger_staleness` perimeter blindness** — 20 of 33 agents hold unscanned ledgers; **FIXED `e23aeb51b`**, verified both directions + silence falsified | mine; shipped |
| 5 | **Self-critical-claim hop** | PATTERNS |
| 6 | **Follow the DELEGATION when enumerating surfaces** — the instrument a surface DEFERS to is a surface (HOMER; my enumeration hit the two surfaces that DESCRIBE the grade and missed the one that PERFORMS it) | surface-enumeration standard |
| 7 | **A self-test needs a fixture the WRONG rule gets wrong**, or it certifies agreement not correctness (PROME) | CHECK_STANDARD §3 amendment → Will |
| 8 | **Reader-ops root cause** — 4/4 readers idled holding complete work because they wrote to plain output, which has no channel. The prior floor blamed compliance for a **plumbing** defect | UPGRADE_PROTOCOL |
| 9 | **Newest-first ordering and consumer-addressing conflict** on any truncating export surface | blueprint candidate |

---

## COVERAGE — what this review did NOT do

**Targeted scope by ruling: C1+C2+C3 only.** `workbook/` (8 ledgers) and ops/learning were **not** read as
clusters. Not opened at all: `board_log.tsv` body, `SCHEMA.tsv`, `KB.tsv` body, `archive/`,
`state_vectors/`, 43 WALTER packets, 22 processed inbox items. `CATALYSTS.tsv` covered ~12% by bytes
(dated-obligation target ~100%; **I closed the threshold-cell gap myself** — no further collisions). The
26 KB base-rating report was grep-only — **the largest un-read falsification artifact.** Every seam finding
is **one-sided** (HOMER's statement only) except CARL and CREED. **Blueprint conformance not graded.**
Contradiction counts are **LOWER BOUNDS** — R2 read ~53% of STATUS as prose.
Per-reader coverage limits verbatim in the companion; that is the expensive half and it is not summarised
away here.
