# HOMER Review 2026-08-22 — READER REPORTS (PAT-100 companion)

> **IN PROGRESS.** Canonical-name companion to `HOMER_REVIEW_2026-08-22.md` (synthesis). Both halves must
> exist beside each other — a companion without a synthesis is as non-compliant as the reverse (PAT-100,
> disambiguated at self-audit F31). Synthesis is written when all four readers land.
>
> **Fan-out:** Mode-A, 4 readers, Will-ruled 2026-08-22 (method: fan-out · scope: targeted C1+C2+C3 ·
> notify: at delivery). C2 split R2/R3 at 220 KB.
> **Subject state:** HOMER LIVE and committing throughout. Pin drifted `abc7fc58a` → `f7c63add3` → (repo)
> `f168cb0bd` during the review. **All findings re-verified at then-current artifact before routing.**

| Reader | Cluster | Status |
|---|---|---|
| R1 | C1 charter + boot (`CLAUDE.md`) | **DELIVERED** (after 3 chases — see delivery note) |
| R2 | C2a `STATUS.md` | **DELIVERED** (after chase) |
| R3 | C2b `NEXUS_BRIEF.md` + `SCRATCH.md` | **DELIVERED** (after chase) — best report of the fan-out |
| R4 | C3 falsification + predictions + `LESSONS.md` | **DELIVERED** (after 2 chases) |

**★ READER-OPS FLOOR — ROOT CAUSE FOUND, and it is not what the floor said.** All FOUR readers idled
holding completed work; R4 needed 2 chases and R1 needed 3. **R4 and R1 both reported the same cause: they
had been writing their reports as PLAIN OUTPUT, which does not reach the caller.** So the prior reading —
"readers idle holding results, the instruction does not work, the chase does" (10-of-12 across three
fan-outs) — described the SYMPTOM and mis-attributed the CAUSE to reader compliance. The work existed and
was complete every time; it had no channel. → the fan-out prompt must state the DELIVERY MECHANISM
(`SendMessage` to the caller), not merely the obligation. Amend the reader-ops line rather than extend its
count: a behavioural fix was prescribed for a plumbing defect. n=4/4 here.

**★ AND THE CHASE IS NOT NEUTRAL — it changed a finding.** R3 re-ranked its own report mid-chase because
the chase asked it to MEASURE something it had estimated; the measurement demoted its original #1. A chase
carrying a specific question outperforms a chase asking for the report.

---

## R2 — `STATUS.md` (cluster C2a) — DELIVERED

**Reader's own snapshot note:** brief's figures were stale on arrival (155,933 B / 241 lines given;
**165,409 B / 244 lines actual** at read time — HOMER committed twice mid-review). Reader flagged this
itself. Good practice; recorded.

### (a) RAW TABLE — truncation measurement [VERBATIM]

> | Quantity | Value |
> |---|---|
> | **Single-Read stop line** | **73** (of 244) |
> | File cost in tokens | **70,943** vs **25,000** cap = **2.84× over** |
> | Lines delivered at boot | 73 / 244 = **29.9%** |
> | **Bytes BEYOND the cap** | **123,922 B = 74.9% of file** |
> | Bytes/line (mean) | **678** |
>
> Instrument output observed directly:
> `PARTIAL view — showing lines 1-73 of 245 total (70943 tokens, cap 25000)`

**Never reached at boot:** Multifamily (74–90, 13,261 B) · Mortgage Rates/Demand (91–103, 10,905 B) ·
Builder Distress (104–116, 6,844 B) · Pricing/Inventory (117–126, 3,028 B) · State-Level FL/TX
(127–140, 10,487 B) · **OPEN ITEMS (141–166, 33,376 B)** · CATALYSTS (167–189, 4,473 B) ·
**PREDICTIONS (190–213, 9,825 B)** · **BOTTOM LINE (214–244, 31,722 B)**.

### (a) RAW TABLE — section map [VERBATIM, persisted per reader request]

`AGENTS/HOMER/STATUS.md` @ `f168cb0bd` — **244 lines · 165,409 B · 678 B/line mean · boot cut at line 73**

| Lines | Bytes | B/line | Section | Boot? | Accretion? |
|---|---|---|---|---|---|
| 1–2 | 16 | 8 | `# HOMER STATUS` | ✅ | — |
| 3–26 | 22,055 | **918** | HEADER BLOCK — 10 dated session headers | ✅ | **★ YES — duplicates 232–244** |
| 27–28 | 5 | 2 | `---` | ✅ | — |
| 29–54 | 7,435 | 285 | MARQUEE OPEN QUESTION (reframed 7/31) | ✅ | no — clean |
| 55–58 | 26 | 6 | `---` + `## SIGNAL DASHBOARD` | ✅ | — |
| 59–73 | 11,951 | 796 | Foreclosure Pipeline | ✅ **(cut lands here)** | partial — `:69` unretired |
| 74–90 | 13,261 | 780 | Multifamily — GSE + CMBS | ⛔ | not assessed (unread) |
| 91–103 | 10,905 | 838 | Mortgage Rates / Demand | ⛔ | no |
| 104–116 | 6,844 | 526 | Builder Distress | ⛔ | mild |
| 117–126 | 3,028 | 302 | Pricing / Inventory | ⛔ | **★ 3 of 6 rows stale/contradicted** |
| 127–140 | 10,487 | 749 | State-Level Housing (FL/TX) | ⛔ | no — actively maintained |
| 141–166 | **33,376** | **1,283** | OPEN ITEMS (20 rows; `:163` = self-diagnosis) | ⛔ | **★ largest + densest** |
| 167–189 | 4,473 | 194 | CATALYSTS | ⛔ | **★ passed rows accrete** |
| 190–213 | 9,825 | 409 | PREDICTIONS | ⛔ | **no — ★ best section** |
| 214–244 | **31,722** | **1,023** | BOTTOM LINE (9 dated blocks) | ⛔ | **★ 31 lines vs 2–4 convention** |

**Accretion verdict (reader's):** four sections accrete without retiring — HEADER (3–26), OPEN ITEMS,
CATALYSTS `(passed …)` rows, BOTTOM LINE = **91,626 B = 55% of file**. Header block and BOTTOM LINE are
near-duplicate session logs at opposite ends. Collapsing that duplication recovers ~22 KB and is the only
change that could bring the boot-critical region back under the read cap without deleting analysis.

### (b) POINTER MAP — where R2's findings landed

| R2 ID | Claim | Disposition |
|---|---|---|
| F1 | Boot read truncates at 73/244 | **CONFIRMED + STRENGTHENED** by DAEDALUS (see adjudication) → synthesis, route rank 1 |
| F2 | Guard violated at `:220`, 6 surfaces | **DOWNGRADED** by DAEDALUS verification → see adjudication |
| F3 | `:123` refuted mechanism live at 🔴 | **CONFIRMED at artifact** — `:123` still reads "(60-90d lag → HPI likely rolls Jul-Aug)" 🔴 unmarked; `:200` grades the mechanism **0-for-1** (June *accelerated* 48bps), IF-MISSED clause live. **The refutation sits 77 lines DOWNSTREAM of the claim in read order** — append-retraction geometry, converges with R3's cluster. |
| F4 | `:182` stale inverted PMMS row | **CONFIRMED — cleanest of the set.** `:182` "off Jul 23's 6.58% (3rd straight rise, 2026 highs)" vs `:94`/`:98`/`:100`/`:176`/`:177` all carrying **6.65%, second consecutive DECLINE**. Same instrument, opposite regime, 4 weeks stale, **in the same CATALYSTS table as the two current rows.** |
| F5 | `:125` duplicate Housing Starts + stale 6.51% | **CONFIRMED.** `:97` "Housing Starts (June) 1.427M" vs `:125` "Housing Starts Apr 1.465M" 🔴, the Apr row embedding "30Y **6.51%** multi-week high transmitting" — rate now 6.65% **and the direction inverted**. Neither row cross-references the other. |
| F6 | `:124`, `:69` unlabelled stale rows | **CONFIRMED, and the diagnosis sharpens in HOMER's favour.** `:124` Redfin Apr 🟠 4mo stale, no caveat. `:69` Q1 state-leaders 🔴 unlabelled — **but `:63`, one row away and the same Q1/ATTOM vintage, carries a model supersession rider** ("[H1 row above supersedes for latest; Q1↔Q2 reconcile: 6,893 dual-quarter overlap]"). **The convention exists and is well-executed; it was applied inconsistently.** Frame the packet that way — not "HOMER doesn't label supersession." |
| F7/F8 | BOTTOM LINE + HEADER accretion | structural; same ruling as F1 |

### (c) NOT-READ + COVERAGE LIMITS [VERBATIM — the expensive half]

- **Read in full, verbatim:** lines **1–73** (single Read, complete page), line **163**.
- **Read with per-line character truncation** (`cut`/`sed` 150–1400 cols): `91–103` (~75% of each row
  unread) · `127–140` (~80% unread) · `167–189` (~90%+ covered) · `190–213` (~85%) · `214–231` (high, but
  tails of `:220`, `:222`, `:224` unread).
- **NOT read as prose at all — grep-only:** `74–90` (13,261 B) · `104–122`+`126` (~9,000 B) ·
  `141–162`+`164–166` (~30,000 B) · `232–244` (~25,000 B). **≈77,000 B ≈ 47% of file not read as prose.**
- **Consequence stated by reader:** F1/F7/F8 are mechanical measurement, coverage-independent.
  F2–F5 grep-found then verified by direct full-text re-read of each cited line. **F6 and any "only N
  contradictions" implication are LOWER-BOUND claims** — the unread 47% could hold further
  same-metric-different-vintage pairs, most plausibly OPEN ITEMS and Multifamily. Read counts as "at least N."
- **Could not verify:** whether the 250-line cap is declared in `CLAUDE.md` or only in-file.
  **Whether boot step 2 uses a plain `Read` — F1's severity is conditional on it.** → BOTH RESOLVED by
  DAEDALUS, see adjudication.
- **Inference not observation:** that F7's ordering ambiguity *caused* F2's survival (plausible, not
  established); that the five line-compressions worsened truncation (direction certain, magnitude unmeasured).

### (f) REFUTED HYPOTHESES [reader's — recorded beside the confirmed findings]

1. **The 8.9mo/8.1mo condo contradiction is FIXED** (`:133`, with a dated correction rider recording that the
   wrong figure stood 12 days). **Do not re-raise.** ← closes an 8/07 profile 🔴
2. **No two-clock header drift.** `:5` stamps 8/22; newest body content also 8/22. Header is *bloated*, not
   *lying*. Drift that exists is section-level, not header-level.
3. **Labelled BOTTOM LINE EXISTS and is CURRENT** (`:214`).
4. **MARQUEE is alive, current, and DATABLE** — heading carries its own reframe date; scanner can date it.
   Better than most thesis surfaces. **Not a problem. Do not touch.**
5. **Source+date canon: NOT violated.** Every dashboard row carries As-Of + Source; sole no-primary figure is
   triple-labelled with a kill condition.
6. **`:70` servicer 🔴 is not a false trigger** — Will-ruled seeding decision, labelled 4× in-row.

---

## DAEDALUS ADJUDICATION of R2 (verification run before routing)

**F1 — CONFIRMED AND STRENGTHENED.** R2's blocking caveat resolved by direct read of the charter:
`AGENTS/HOMER/CLAUDE.md:163` = `2. Read STATUS.md (dashboard + BOTTOM LINE).` — a plain Read, **and it names
BOTTOM LINE as a target**. BOTTOM LINE is at 214–244; the read stops at 73. **The boot step instructs
reading a section sitting 141 lines past where its own prescribed instrument stops, and reports satisfied.**
Stronger than R2 could state from inside its cluster.
Second open item settled: the 250-line cap **IS** declared in `CLAUDE.md` at `:170`, `:179`, `:196`
("capped at 250 lines"), not only inside STATUS — **so the axis fix touches the charter, not just the file.**

**F2 — DOWNGRADED. 5 of 6 cited surfaces are the guard working correctly.** Verified each hit in context:

| Surface | Verdict |
|---|---|
| `STATUS:160`, `CATALYSTS:11` | **The guard itself.** Legitimate. |
| `SCRATCH:102`, `ANCHORING-PROPOSAL:85` | Quotes establishing the rule. Legitimate. |
| `NEXUS_BRIEF:16` | **A STRENGTH** — *"if you took 'fragile at n=2' from me, that was the PRE-RULING state and the capacity ruling dissolved it."* The retraction traveling to consumers, addressed-to-the-reader form. |
| `STATUS:220` | The only arguable instance — and weaker than framed. |

`:220` reads *"not because two observations validated it"* — which **denies** validation (agreeing with the
ruling) while retaining the **count** (canon post-ruling is ONE observation). **The residue is a COUNT, not a
VERDICT.** R2's "a reader scrolling to BOTTOM LINE gets exactly the superseded state" overstates it.
Class: `claim_check`'s own canon — *a flagged instance can be a correctly-labeled QUOTE of a corrected error
inside a ruling record; look before rewording.* Routing R2's F2 as written would have sent HOMER six
citations of which one is real and one is a compliment misfiled as a defect.

**Standing credit, to be carried into the packet:** HOMER **self-diagnosed the byte/axis error today** at
`STATUS:163` (crediting the DAEDALUS recon) and **deliberately did not fix it**, citing root Critical Rule #2
because a review was in flight. Correct conduct. What HOMER lacked was the number — it measured 647 B/line
but never measured *where the cut falls*. **That measurement is this review's delta.**

---

## R3 — `NEXUS_BRIEF.md` + `SCRATCH.md` (cluster C2b) — DELIVERED

**Read whole:** NEXUS_BRIEF.md (95 ln / 65,773 B — required TWO Read calls) · SCRATCH.md (137 ln / 26,036 B).
STATUS.md grep-only (~55 targeted patterns), never opened whole.

> ★ **The reader RE-RANKED its own findings after the chase** — my chase asked it to *measure* the consumer
> read-cut it had only estimated. The measurement demoted its original #1. Recording this because it is an
> argument for chasing with a specific question rather than a generic "send your report."

### (a) RAW — F1, the consumer-delivery measurement [VERBATIM]

> My own Read returned: `PARTIAL view — showing lines 1-74 of 96 total (27470 tokens, cap 25000)`.
> **Line 74 is the literal string `## CROSS-DOMAIN`.** Lines 75–96 were NOT delivered.
> Past the cut: `**SENDING:**` (:76) and all five per-agent asks — REGINALD :77, LABOR :78, CARL :79,
> CARL :80, HENRY :81, CREED :82, CORAL :83 — plus `**WAITING-FOR:**` (:85) and all six dated-catalyst
> rows (:86–:91), plus closing provenance (:95).
> **Delivered 57,679 B = 87.7%. Lost 8,094 B = 12.3% of bytes and 23% of lines — but that 12.3% is 100%
> of the content addressed to a named agent.** The brief scores well on every line-count and byte-count
> check and still fails, because the loss is not proportional: **it is exactly the payload.**
>
> Section offsets (measured): `## VIEW` @ 1,790 B (3%) · `## CALIBRATION` @ 48,903 (74%) ·
> `## CROSS-DOMAIN` @ 57,662 (88%) · `**WAITING-FOR:**` @ 63,681 (97%). VIEW alone = 47.1 KB = 72%.
> Longest lines: `:31` = 5,830 B (~1,000 words in one bullet), `:34` 2,903 B, `:77` 2,895 B, `:68` 2,563 B.

**Reader's contrast with R2's STATUS number — the key structural insight of the review:**
> STATUS loses 74.9% of its LINES; the brief loses only 23% of its lines and is WORSE OFF — because
> STATUS's reader is HOMER (who wrote it and can re-read by offset) while the brief's readers are three
> other desks absorbing it alongside their own boot spine, **and the part they lose is the part with their
> name on it.**

### (b) POINTER MAP + DAEDALUS ADJUDICATION

| R3 ID | Claim | Disposition |
|---|---|---|
| **F1** | Brief truncates at `## CROSS-DOMAIN`; 100% of addressed content lost | **CONFIRMED (reader-measured).** Route rank 1. Minimum non-structural mitigation the reader proposes: **move `**SENDING:**` above `## VIEW`** — costs nothing, fixes addressing without touching the size question. |
| **F2** | `:79` tells CARL a superseded FMHPI trough ("Jan +0.9%" vs canonical Dec-2025 +1.01%) | **CONFIRMED as a defect; BLAST RADIUS CONTAINED.** DAEDALUS check: CARL holds a dedicated HOMER packet (`AGENTS/CARL/inbox/processed/2026-07-31_…kb-carl-304-hpi-figures-superseded…`) correcting the *first* revision (Mar 0.7). Chain is Mar 0.7 → Jan +0.9 → Dec-2025 +1.01; **whether the SECOND revision reached CARL is UNVERIFIED** — flag, do not assert. Reader correctly tested and rejected the citation-not-violation reading. |
| **F3** | `>0.50%` RED-band cross absent from the entire brief | **CONFIRMED — highest-value cross-agent finding.** DAEDALUS check at REGINALD: it holds the 7/31 retraction (`REGINALD/STATUS.md:44`) and a July packet noting "Freddie MF rose to 0.51%" — **but nothing anywhere tells it a REGISTERED BAND was crossed.** PAT-063 in pure form: HOMER owns the metric AND the band; the registered consumer never receives the band state. |
| **F4** | Of two ~9/4 dated kills the brief publishes, only one is docketed | **CONFIRMED on the two surfaces checked** (PROME/DOCKET.tsv:224 has the $160B wall; HOMER/docket/CATALYSTS.tsv has NO September Trepp row — 23 rows enumerated). Reader correctly scoped: "no row on the two surfaces HOMER's own SCRATCH names", not "none anywhere". |
| **F5** | SCRATCH `:93`/`:128` still present a Will-ruled question as open, inside a commit claiming it was swept | **CONFIRMED.** ★ Carries the review's best transferable lesson: **a residue sweep keyed on a PHRASE certifies the phrase, not the STATE** — HOMER grepped `"fragile at n=2"` and missed the same pre-ruling state expressed in other words. **This independently explains the R2-F2 downgrade** (my verification found 5 of 6 hits were the phrase working correctly *because the sweep was phrase-shaped*). → PATTERNS candidate. |
| **F6** | Fold-ordering guard "cannot fail" | **NARROWED by DAEDALUS.** Reader flagged this as inference from 4 commits and said it had not walked history. Full history: **20 commits carry both files · 14 STATUS alone · 7 BRIEF alone.** The guard CAN discriminate — it did not on any of the four 8/22 commits. Correct finding: *degenerate whenever both files land in one commit, which is what happened every time on the day it was relied on.* PAT-074 class, narrowed. Duplicate certificate sentence at `:6` confirmed separately. |
| **F7** | Undated/unqualified figures on the consumer surface | **CONFIRMED.** Priority item: `:45` ICE FC inventory 280K presented as current "domain spine", actually **May 2026** per STATUS:64 — ~3 months old, undated, **and inside the DELIVERED region**. |
| **F8** | SCRATCH supersession geometry mixed | **CONFIRMED** — see geometry section below. |
| **F9** | A "standing fix" lives only in SCRATCH, which `:3` says is rewritten at closeout | **CONFIRMED** (absent from CLAUDE.md / LESSONS.md / MEMORY.md). |
| F10 | STATUS dashboard `:39` is BEHIND the brief | **CONFIRMED, drift INVERTED** — derived surface fresher than canonical. Route to STATUS cluster. |
| F11 | SIG-019 revival dates ride a differently-scoped catalyst row | CONFIRMED (low). |
| F12 | One correction, two dates (8/12 vs 8/14) | CONFIRMED (cosmetic; it is the audit trail of the fleet's most-cited propagation defect). |

### (c) NOT-READ + COVERAGE LIMITS [VERBATIM — reader stated coverage was partial, plainly]

Not opened at all: STATUS.md as a document (grep-only, ~55 patterns) · LESSONS.md · MEMORY.md · CLAUDE.md
(grepped only) · reports/ (incl. the two servicer base-rating/anchoring reports the brief cites) ·
workbook/*.tsv (9 files) · thesis/PREDICTIONS.tsv · inbox/, outbox/, board_log.tsv, state_vectors/,
domain/, archive/.

**Brief figures that could NOT be cross-checked, and why:** FHFA "+2.0%→+2.2% May" (`:79`) absent from
STATUS · PFSI "$76.99 close"/"$83.49 BVPS" (`:31`) absent from STATUS, probably in an unopened report ·
Case-Shiller Apr pre-revision +0.8% (`:79`) — revision PAIR unverifiable · B4-2.1-03 verbatim quote +
$10,000/unit (`:12`) external primary, not re-fetched ("STATUS agrees internally; that is consistency,
not verification") · "20.6%" F-dilution clearance — no brief-vs-STATUS pair exists · PHSI "~30% below
2019" — AGREE but both HOMER-internal, no external check.

**Explicitly inference, not measurement:** *"Every AGREE below is INTERNAL-CONSISTENCY ONLY. I verified
brief-vs-STATUS agreement and verified NO figure against any external primary. I cannot certify that an
agreeing pair is not agreeing on a shared error."* · F1's byte offsets measured on THIS harness; whether
CARL/REGINALD/HENRY hit the identical cut depends on their own caps — their boot protocols not read ·
F6 inferred from 4 commits (→ RESOLVED by DAEDALUS above) · F4 scoped to two surfaces · **SCRATCH is a
MOVING TARGET — HOMER live; F5/F8/F9 may already be stale.**

> ⚠️ **INSTRUMENT ARTIFACT — affects every figure sweep on this desk, mine included.** `ugrep` returns
> "exceeds complexity limits" on UTF-8 context patterns (DAEDALUS hit this independently), **and a plain
> ASCII-hyphen search for `-0.05` returns ABSENT because the file uses U+2212 `−`.** Reader re-ran its
> entire battery through a Python matcher. **Any grep-based figure sweep using ASCII hyphens/minus signs
> on these files produces false ABSENTs.** → PATTERNS candidate; audit prior sweeps that used ASCII greps.

### (f) REFUTED HYPOTHESES — including the review's most important negative result

1. **The "94% multifamily" defect is CLOSED.** `grep "94% multifamily" NEXUS_BRIEF.md` → ZERO HITS.
   `:38` now carries 95.8% **with the 12-day failure written into the record rather than smoothed.**
   Closes the 8/07 profile's second 🔴. (R3-F2 is a *different* instance of the same class, still open.)
2. **The SCRATCH line-27 defect is GONE** — SCRATCH was fully rewritten at closeout per its own `:3` rule.
3. **★ THE FIGURE CHANNEL IS HEALTHY — ~60 figures checked, 62 AGREE / 1 DISAGREE.** Reader's words:
   **"A figure-level audit of this desk returns clean and misses everything."** The defects are in
   **DELIVERY (F1), ADDRESSING (F2), STATE TOKENS (F3) and REGISTRATION (F4)** — not in the numbers.
   *This is the single most load-bearing result of the review and it is a NEGATIVE one.*
4. **The brief's vintage is NOT stale.** Same-day, third and final fold. The cadence rule (CLAUDE.md:183,
   NEXUS Amendment 10) is real and was followed; the defect is that its checkable form is degenerate (F6).
5. **All five loud retractions are the guard working, not violations** — `:20`, `:22`, `:26`, `:34`, `:59`.
   Reader applied the DAEDALUS calibration and routed NONE of them. `:22` singled out as the best paragraph
   in the cluster ("The scan was clean and the referent was wrong").

### (g) FIGURE RECONCILIATION TABLE — totals [full 68-row table returned by reader; verdict distribution]

**62 AGREE · 1 DISAGREE (#32, brief `:79` FMHPI trough) · 3 ABSENT-FROM-STATUS (#50 PFSI price, #66
Case-Shiller Apr prior vintage, #67 FHFA) · 1 ABSENT-FROM-BRIEF (#68 GSE MF band re-spec owed) ·
1 state-token omission (#25 RED-band cross) · 2 undated-on-brief (#37 ICE 280K, #57 CPI).**

Verified-agreeing families: PMMS/15-Yr/MBA/DGS10/spread · CMBS-MF five-month path · MF SS 8.39 ·
PHSI 71.2/69.0/70.9/52.7 · NAHB 35/63/23 · MBA NDS 11.79/4.37/0.67/1.43 · FMHPI 2.06/0.32/1.58 ·
EHS 4.06M/$434,100 · ATTOM 227,548/563d/+33% · TX $1.15B/47 · Banc $827.0M/95.8%/19.5% · Arbor 545/525 ·
servicer 13.6/4.3/32.3/22.4/0.151/13.3/6.13 · FL 0.435% · Case-Shiller +1.1/−0.05/9pp ·
Freddie Table 27 $311.8B/0.65/8.3%/91.7%.

### GEOMETRY ANSWER — both granularities (the question that produced the sharpest insight)

**SCRATCH.md — SECTION granularity: HEALTHY-LOOKING.** Thematic sections roughly chronological, with an
explicitly labelled `## ⚠️ LATE ARRIVALS` append block at `:99–106`. **Any scan reading section headers
passes this file.**
**SCRATCH.md — ROW granularity: FAILS, 4 instances** — LATE ARRIVALS carries corrections to rows 8–20 lines
ABOVE it: `:91` G-row "⛔ UNTESTED" fixed at `:103` twelve lines later · `:81–95` asks-listed-as-independent
corrected at `:102` · `:78` "RULED AND ENCODED" vs `:112` still reading "Needs a monthly calibration",
**inside the section a reader trusts MOST for live state** · worst case `:93`/`:128` where the correction
never lands at all (F5).
**Contrary evidence, and it is the model:** `:90` was fixed IN PLACE with the superseded phrasing labelled
inline. **HOMER can clearly execute the correct geometry — it did so on the one row its phrase-grep found.**

**NEXUS_BRIEF.md — SECTION granularity: genuinely NEWEST-FIRST** (8/22 → 8/14 → 8/13 → 8/12 → 7/31 → legacy).
**ROW granularity: FAILS ONCE** — corrected FMHPI trough at `:47`, superseded one at `:79`, 32 lines later,
unmarked (F2).

> ★★ **SECOND-ORDER, and the sharpest structural finding of the review:** *"the brief's newest-first section
> ordering is what PUTS CROSS-DOMAIN LAST — and last means undelivered. **Newest-first ordering and
> consumer-addressing are in direct conflict in this file.** Fixing the geometry by chronology alone will not
> fix the delivery; the addressed section has to move ahead of the chronology."*

**LIVE CLAIM IN A CLOSED CONTAINER:** SCRATCH `:115` reads "✅ CLOSED 8/22 …" while filed inside
`## ⚠️ OPEN / UNSETTLED — do not publish these as settled` — inverting the container's contract, the same
class as `:112` pointing the other way.

---

## R1 — `CLAUDE.md` charter + boot (cluster C1) — DELIVERED

**Delivery note (the fan-out's own defect):** three chases. Reader's own account — *"Delivery failure was
mine: I wrote three full reports as plain output."* Work was complete each time and had no channel. See the
root-cause note in the header.

**Read whole:** `AGENTS/HOMER/CLAUDE.md`, 233 lines. Read-only confirmed.

### (a) RAW TABLE — THRESHOLD RAIL AUDIT, 13 rows, two legs [VERBATIM verdicts]

| # | Row | (a) named source returns it | (b) BASIS/window stated | Verdict |
|---|---|---|---|---|
| 1 | Fannie MF Serious DQ `:80` | PARTIAL | no cadence pin, no 60+ def, no UPB-vs-count | **(b) FAILS** |
| 2 | Freddie MF Serious DQ `:81` | PARTIAL | same + label mismatch | **(b) FAILS** |
| 3 | 30-Yr Mortgage Rate `:82` | GOOD (PMMS) | **PASS** — Source pins the instrument | **PASS** |
| 4 | National Foreclosures (Qtr) `:83` | PARTIAL | **FAIL SEVERE** — filings vs starts vs REO unnamed | **BROKEN** |
| 5 | FL Foreclosures YoY `:84` | — | DISARMED, do-not-touch | n/a |
| 6 | FL Foreclosure Rate ANNUAL `:85` | GOOD | **EXEMPLARY** — basis in row label, 8-row derivation | **BEST-IN-FLEET** |
| 7 | FL/National RATIO `:86` | GOOD | **EXEMPLARY+** — plus the 8/22 annual-only restriction | **BEST-IN-FLEET** |
| 8 | 90+/FC Pipeline `:87` | **WRONG** (says MBA; graded as MBA/ICE composite) | composition/denominator/cadence nowhere | **BROKEN** |
| 9 | Cure Rates `:88` | PARTIAL | **FAIL ×2** — no window AND comparator INVERTED | **BROKEN** |
| 10 | FHA DQ Rate `:89` | GOOD | absent from rail; settled in HOM-02 | **(b) FAILS** (cheapest fix) |
| 11 | Builder Price Cuts `:90` | GOOD | unit unstated | **(b) FAILS** |
| 12 | Rent Growth `:91` | **WEAKEST** — "Apollo/Slok", a chartbook, nothing returns it | universe/measure unstated | **DECORATION** |
| 13 | Existing Home Sales `:92` | GOOD | **PASS** — "(Ann.)" = SAAR, `<` direction correct | **PASS** |

**THE BASE-RATE ANSWER (the review's headline for register ⑰):** 12 gradeable rows — **2 EXEMPLARY ·
2 clean PASS · 7 carrying (b) defects · 3 severe enough to be ungradeable today.** ≈25% best-in-fleet,
≈25% fine, ≈25% broken. **The ~95% fleet defect rate DOES NOT HOLD on a strong desk — and does not
collapse either.** Report as: *a strong desk cuts the rate to roughly a quarter, and still ships three
broken bands.*

**AND THE (b) HYPOTHESIS IS CONFIRMED HARDER THAN THE COMPARATOR: 10 of 10 defects are UNSTATED BASIS,
not a missing number.** Every row names a publisher; only row 12 fails leg (a). MARCO's evidence was
5-of-6; HOMER's is 10-of-10. **Two independent desks now say the fleet's threshold problem is BASIS.**

### (b) POINTER MAP + DAEDALUS ADJUDICATION

| R1 ID | Claim | Disposition |
|---|---|---|
| **A0** | Truncation × missing basis COMPOUND — the 3 dashboard blocks past the cut are precisely the ★-ruled HOMER-OWNED surfaces (Mortgage Rates, Builder, Pricing); for rail rows 3/10/11/13 the basis is absent from the charter AND its only written home is past the cut | **ACCEPTED** — best synthesis in the fan-out; independent of R2's cluster |
| **A1** | `:232` asserts CRL-06 metric-clarification still CARL-owed; CARL resolved it **2026-07-16**, 37d ago, **by HOMER's own data package** | **CONFIRMED** (reader checked both sides) |
| **A2** | `:83` uninformative under EVERY basis — filings & starts permanently ≥Red, REO can never fire | **CONFIRMED at artifact.** Sits **nine rows above its own autopsy** (the DISARMED FL-YoY row retired for this class, inverted) |
| **A3** | `:88` comparator INVERTED — `>-15%` satisfied by −10% (an improvement); −40% satisfies none | **CONFIRMED at artifact.** Row 13 uses `<` correctly for a falling metric — **the author demonstrably knows the form.** 4-character fix |
| **A4** | Servicer Watch A–G (Will-ruled 8/14 + 8/22) appears in `CLAUDE.md` **not once** | **CONFIRMED AND SHARPENED** — see below |
| A5 | `:87` Source wrong vs practice | CONFIRMED |
| A6/A7 | `MEMORY.md` + `reports/` unread and/or unlisted; MEMORY carries a now-false CREED fact | CONFIRMED (`grep "reports/" CLAUDE.md` → zero hits) |
| **A8** | NEXUS fold-ordering "checkable form" is vacuous | **CONFIRMED — INDEPENDENT CONVERGENCE with R3-F6 from a different file.** DAEDALUS narrowing stands (20 commits both / 14 STATUS-only / 7 brief-only: it CAN discriminate, and did not on any 8/22 commit) |
| **A9** | `docket/` + `thesis/` outside every staleness instrument, silently by construction | **CONFIRMED BY EXECUTION, and it is MINE not HOMER's** → fixed same session, `e23aeb51b` |
| A10 | Boot docket step is recall-shaped; the 8/22 enumerate-don't-recall fix landed on the CLOSEOUT leg only | CONFIRMED — and boot is the leg that decides what the session WORKS ON |
| A16 | `(see Open Items)` dangles — no such section | **CONFIRMED at artifact**, and it is the ONLY elaboration of the CORAL/MARCO FL seam |
| A17 | Live value at `:37` | **SELF-REVISED BY READER under the DAEDALUS calibration** — half withdrawn (`:114` was the guard working). Reader carried the ratio forward explicitly |

**A4 SHARPENED BY DAEDALUS (severity check R1 itself requested):** the `workbook/KB.tsv` hit was a
**coincidental phrase match** — a 2026-04-13 loanDepot row containing "~20% of market cap", not the spec
(KB.tsv is FROZEN 7/10; it cannot contain an 8/13 ruling). The ruled A–G spec's actual homes are
**`SCRATCH.md`** (rewritten at closeout by its own `:3`) · **`STATUS.md`** (rewritten each session by
HOMER's own `:170`, AND past the line-73 cut) · **`NEXUS_BRIEF.md`** (refolded each session, truncates
before CROSS-DOMAIN) · **`docket/CATALYSTS.tsv`** (outside every staleness instrument, A9) · **`reports/`
×3** (not in FILES, not boot-read, A7). **Not one of the five is both durable AND read** — a stronger
statement than "absent from CLAUDE.md", and a direct violation of HOMER's own `:170`.

### (c) NOT-READ + COVERAGE LIMITS — reader-declared, and one of them is a BLOCKER

- **READ WHOLE:** `CLAUDE.md` only (assigned cluster, complete).
- **STATUS.md:** `^|` rows **truncated at 260 chars** — *"FOR EVERY DASHBOARD ROW I CITE I HAVE SEEN
  ROUGHLY THE FIRST 15%."* Concretely: A5 rests on the first 260 chars of `STATUS:68`; a later clause could
  state the composition rule, demoting it.
- **8 workbook TSVs:** header line only · **CATALYSTS.tsv:** columns 1–2 only · **reports/:** `head -25` of
  ONE file (A7 rests on that) · **`ledger_staleness.py`:** vintage-parsing core unread.
- **NOT OPENED:** `LESSONS.md`, `SCRATCH.md`, `NEXUS_BRIEF.md`, board_log body, SCHEMA, KB body, archive,
  state_vectors, inbox.
- ⚠️ **DECLARED BLOCKER (reader's own words):** *"LESSONS.md UNREAD IS MY LARGEST BLIND SPOT… ANY FINDING
  OF MINE APPEARING THERE SHOULD BE RE-SCORED 'gap' → 'known-but-unencoded.' I would not put A3, A13 or A14
  in front of Will without that check."* → **DAEDALUS RAN IT: zero hits** for cure/price-cut/90+/comparator/
  inverted in `LESSONS.md`. **Blocker DISCHARGED; A3/A13/A14 stand at full weight as genuine gaps.**
- ⚠️ **NOT DELIVERED, and no other reader covers it:** *"I DID NOT GRADE HOMER AGAINST THE BLUEPRINT.
  market-agent.md unread. Every §4 verdict is INTERNAL CONSISTENCY."* → blueprint conformance on the
  threshold dimension is an **open gap in this review**; carry to the card, do not paper over.
- **EVERY SEAM FINDING IS ONE-SIDED** (HOMER's statement only) except CARL and CREED, where both sides were
  read. A thin seam here may be full at the other desk — "gap" may be "asymmetry."
- **Declared inference:** A13's second NAHB number is domain knowledge read nowhere in the repo (if NAHB
  publishes only the share, A13 collapses to LOW) · A5's gross-up · A15's magnitude (finding does not
  depend on it) · A8 is n=3 from git log.

### (f) REFUTED HYPOTHESES — 10, and they matter as much as the findings

**F1 mtime-keyed freshness — REFUTED CLEANLY, a POSITIVE result.** Zero hits for mtime/modified-time/
folder/last-touched. Both freshness legs are CONTENT-VINTAGE (`# LIVE — Last real data refresh:`), all
seven live ledgers carrying it, all reading 2026-08-22. Clean on `finding_mtime_is_corrupted_by_git_sync`.
**F2** the closeout docket awk is CORRECT (`RESOLVED` genuinely is a col-1 prefix incl. compound forms;
10 open / 12 suppressed). **F3** all 12 EXTERNAL paths resolve — the one dangling ref is INTERNAL (A16).
**F4** zero retired agent names. **F5** zero "when X is built" rot; forward language uniformly
EVENT-anchored not BUILD-anchored. **F6** STATUS is 244/250 — UNDER its declared line cap (the byte
problem is real but is not a violation of a rule HOMER holds). **F7** no broken LEDGER_GLOB; the workbook
leg is SOUND — *"the real defect is one layer out and quieter than the one I hunted."* **F8** inbox empty,
processed/ in use. **F9** board_log current through 8/22. **F10** the rail's reputation HALF-refuted —
earned, by two rows.

### §6 SCOPE SEAMS — verdicts

**CREED** ownership EXEMPLARY, **mechanism ABSENT** ("routes the MF row to HOMER" names no channel, no
cadence, no fallback) — live cost: WALTER put HOMER on the information line **five times** for the row
CREED's registry hands it by name. **CARL** best seam in the file, weakened only by A1. **REGINALD** states
the INTERPRETATION boundary but **the stated seam is the WRONG AXIS** — the live overlap is duplicate
SOURCING of the same Trepp print, and its only statement lives in the boot-unread `MEMORY.md`.
**CORAL/MARCO WEAKEST, ON THE HIGHEST-STAKES GEOGRAPHY** — one clause whose only elaboration is the
dangling `(see Open Items)`. Root canon calls Florida a top-priority geography with reconcile-to-one-figure
required. *"THIS IS WHERE I WOULD EXPECT TWO FLORIDA NUMBERS TO APPEAR FIRST."*
**Would a reader know who owns a contested figure?** CREED/CARL **yes** · REGINALD yes on interpretation,
**no on sourcing** · CORAL/MARCO **NO**.

---

## R4 — falsification + predictions + `LESSONS.md` (cluster C3) — DELIVERED

**Delivery note:** two chases; same plain-output cause as R1.

### THE HEADLINE — ITEM 1, answered as asked

> **NO. No thesis-level kill rail exists anywhere in `AGENTS/HOMER/`, under any name. The fix is
> AUTHOR-FROM-SCRATCH, not extract-and-stamp. Standing DAEDALUS finding UPHELD, not inverted.**

Searched: 11 vocabulary variants tree-wide, case-insensitive, extension-unrestricted, **plus** a
markdown-heading-level sweep, **plus** `find` for *THESIS*/*KILL*/*FALSIF* filenames.
Structural confirmation: `thesis/` holds **PREDICTIONS.tsv and nothing else**; `CLAUDE.md` has **no thesis
section, no kill section, no exit rules**; `domain/` is an **empty directory**.
Only three HOMER-authored hits, none a rail: `LESSONS.md:42` (a lesson heading — a norm) · the
`Invalidation` COLUMN (per-prediction, n=2) · `NEXUS_BRIEF.md:16` (matched on "an **exit** ruled in" —
false positive).
**Independently corroborated by DAEDALUS** with a separate grep while R4 was unreachable: 1 hit, that hit
being the NEXUS_BRIEF false positive.

> ⚠️ **WARN THE BUILDER (reader's emphasis):** HOMER's PER-PREDICTION machinery is unusually strong and
> **will look like the missing rail. It is not one** — it covers two metrics; the thesis covers a
> transmission chain.

### (b) FINDINGS + DAEDALUS ADJUDICATION

| R4 ID | Claim | Disposition |
|---|---|---|
| **F1** | HOM-01's early-kill arm 2 and Leg-1 confirm BOTH fire in the ~16bp band 1.90–2.06%, unranked; the kill's "do not wait for the Aug print" forecloses the ONLY remaining test of Leg 2 | **VERIFIED BY DAEDALUS AT THE ARTIFACT** (cells read verbatim) **and at a SECOND surface** (`CATALYSTS` ROW21 states both outcomes as if mutually exclusive). **ROUTED SAME EVENING** (`e6b60df7a`); **HOMER RULED IT BEFORE THE PRINT** (`422f9505f`) |
| **F2** | +1.9% anchored to a vintage since revised to +1.58%, widening the band ~32bp | CONFIRMED. ⛔ Reader's own guard: *"NOT a 'move the number' finding; the fix is ANNOTATION"* — carried into the packet verbatim |
| **F3** | HOM-01 names no SA/NSA basis; the two sit 4bp apart across the line. HOM-02 gets it right | CONFIRMED |
| F4 | HOM-02 graded on an unregistered instrument (mba.org 403'd → HousingWire) with no fallback tier registered | CONFIRMED; severity limited by HOMER's own capitalised disclosure + robustness check |
| F5 | HOM-01's CONFIRMED outcome arithmetically near-dead while the row carries 60%, re-rating Will-gated | ACCEPTED as a **rail gap, not a HOMER defect** |
| F6 | `domain/` empty and absent from FILES; `reports/` absent | cosmetic; converges with R1-A7/A23 |

### (c) NOT-READ + COVERAGE LIMITS

FULL: `thesis/PREDICTIONS.tsv` 100% (every cell) · `LESSONS.md` 100% (⚠️ *"your brief said '100 lines…
short'; it is 32.8 KB of very long lines"* — a briefing error of mine, corrected by the reader) ·
7/24 grading sheet 100%.
PARTIAL: anchoring proposal ~65% · respec ~35% · **base-rating ~5%, GREP + STAMP ONLY (26 KB) — largest
un-read falsification artifact in the cluster** · **`CATALYSTS.tsv` ~12% of bytes** (assigned
dated-obligations target ~100% covered; threshold/notes cells unread for 18 rows — *"F1-class collisions
could hide in any of them"*) → **DAEDALUS CLOSED THIS GAP**: ran the full-cell awk over all 10
non-RESOLVED rows; **no further collisions** — the defect is isolated to HOM-01, not systemic.
NOT OPENED: board_log body, 9 workbook TSVs, archive, state_vectors, 43 WALTER packets, 22 inbox items.

### (f) REFUTED HYPOTHESES — including two corrections to the DAEDALUS record

1. ❌ **"mirror write-back still open" — REFUTED, CLOSED TODAY.** Both grades now carry
   `>> ★★ GRADE RECORD — … MIRRORED INTO THIS LEDGER 2026-08-22`, and `STATUS:192` credits **PR#4 by
   name**. **A carried DAEDALUS claim, correct when made, stale by hours. Dropped from the register.**
2. ⚠️ **SCANNER TRAP WARNING — itself REFUTED by DAEDALUS.** R4 cautioned that a scanner keying on
   `Date_Resolved`/`Outcome` would false-flag HOMER, since both are **blank BY DESIGN** and documented
   in-ledger. The caution was reasonable and **could not be checked from inside its cluster**.
   `falsification_scan.py` contains **neither string**. DAEDALUS **propagated it to HOMER unverified in a
   committed packet and a doorbell**, then retracted. → the self-critical-claim hop lesson (synthesis).
3. ❌ ZERO passed-resolver-yet-ungraded rows. 4. ❌ ZERO past-due docket rows. 5. ❌ **"surfaces are
   undatable" — 10 of 11 fully datable**; `CATALYSTS.tsv` is *"the strongest form in the tree — the vintage
   IS the row"*. **Only partial: `CLAUDE.md` Key Thresholds** — changed rows stamped, no whole-surface
   vintage, so an *unchanged* row is undatable. 6. ❌ **"the servicer spec has unfirable conjunctive
   gates" — REFUTED**, base-rated over 32.3 company-years; Class E fires 5/12. 7. ❌ **"LESSONS is
   occasion-scoped" — REFUTED.**

### Q7 — INSTRUMENT + BASIS on every invalidation clause

**Every invalidation clause names an instrument. ZERO untrippable-for-want-of-an-instrument clauses.**
HOM-01 early-kill: instrument ✅, basis ⚠️ PARTIAL (F2/F3). HOM-01 IF-MISSED: **EXEMPLARY** — an
instrument-retirement clause with an explicit fire date. HOM-02: **CLEAN, the model clause**; only gap is
no fallback tier. Class E/F/G/Z: all name instrument + basis. **The defects are all basis/ranking,
concentrated in HOM-01, all deciding ~2026-08-31.**

### GRADING CULTURE — reputation tested adversarially, CONFIRMED, with the caveat stated

- **HOM-02 is the artifact.** A kill arm fired; HOMER found a mechanism (FC migration under HUD ML 2026-08)
  that would EXCUSE the miss and wrote: *"⛔ THIS DOES NOT RESCUE THE PREDICTION AND I AM NOT USING IT TO.
  A pre-registered arm fired; LESSONS forbids retro-fitting a survival argument."*
- Widening deferred to a SUCCESSOR, not applied mid-flight. Substitution refused: *"Triggers UNCHANGED — no
  re-spec on a missed print."* Own mechanism marked down: *"the Realtor.com list-price lead is 0-FOR-1."*
- Year-trap caught 3× incl. the inversion: *"in July the stale article would have FALSELY CONFIRMED Leg-1;
  this month it would have FALSELY KILLED it. THE TRAP IS INDIFFERENT TO DIRECTION."*
- ⚠️ **HONEST CAVEAT, reader's own:** **n=0 predictions have actually CLOSED.** Culture proven on interim
  grades and inherited CRL-03, **not yet on a completed MISS.** Both open rows likely deliver that test
  within 90 days.

### LESSONS.md — mechanisms, and self-correcting toward mechanism (Item 8)

14 entries, uniform Mistake / Rule / Tell. **BEST (`:88-93`), re-scoped hours after being written, in the
same session:** *"THE INVARIANT IS NOT 'corrections.' IT IS: ANY SESSION OUTPUT THAT A DOCKET ROW IS KEYED
TO MUST CLOSE THAT ROW IN THE SAME PASS… **A lesson scoped to the instance that produced it will miss its
own siblings.** When writing one up, name the MECHANISM, not the OCCASION."* Abstracted a third time by
PROME, with HOMER conceding *"I had under-claimed my own finding."*
**WORST (`:50-52`)** FL/CORAL reconciliation — scoped to the OCCASION (named agents, named geography, a
"Mistake RISK" rather than a mistake). **By the desk's own 8/22 rule this entry would be re-scoped.**
