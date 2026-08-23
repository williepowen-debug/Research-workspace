# HOMER — Upgrade Card

**Created 2026-08-22** (DAEDALUS structure review). **This artifact did not exist before today** — HOMER had
been graded twice (profile 8/07, PR#4 8/17) and never received the DECOMPOSE leg of
COMPREHEND → DECOMPOSE → SECTION-TASKS. **The card IS the work queue.**

**Grade:** Market / **L2** / Conf H · **Sources:** `HOMER_REVIEW_2026-08-22.md` (synthesis) +
`_READER_REPORTS.md` (evidence) + `profiles/HOMER.md` (8/07, refresh pending)
**Rules of engagement:** one section-task at a time, never a whole-agent rewrite. HOMER is a **live desk** —
everything routes as a packet; nothing here is a DAEDALUS edit. **Priority order = quick wins → judgment
calls → builds → polish**, because quick wins prove the method cheaply and raise the floor first.

> ⚠️ **BLUEPRINT CONFORMANCE WAS NOT GRADED BY THE 8/22 REVIEW.** R1 declared it plainly: every §-verdict in
> that review is *internal consistency* — the charter against itself and HOMER's own artifacts — because
> `BLUEPRINTS/market-agent.md` went unread. **The `Applies?` and `Gap type` columns below are therefore
> DAEDALUS's read against the blueprint made at card-build; the review did not independently confirm them.
> Sections 1, 6 and 7 are the least evidenced and are marked accordingly.**

---

## The 8 blueprint sections

| § | Blueprint section | HOMER's current state | Applies? | Gap type | Proposed handle (minimal, additive) | Prio | Status |
|---|---|---|---|---|---|---|---|
| **1** | **THESIS STRUCTURE** | **No `THESIS.md`.** Thesis lives in `CLAUDE.md` "Transmission Pathways" (8 pathways, no state column) + the MARQUEE OPEN QUESTION at `STATUS:29-54` (strong, self-reframed 7/31, datable via its own heading) | **APPLIES** | **missing SUBSTANCE** | Author `thesis/THESIS.md`; migrate the 8 pathways with a state column; MARQUEE becomes its live open question. Pairs with §4 — one build, not two | **3** | OPEN — L3 blocker (a) |
| **2** | **CONVERGENCE MATRIX** | **NOT BUILT — no handle of any kind.** Unlike HENRY (rich labels, no handle), HOMER has neither | **APPLIES** | **missing SUBSTANCE** | Local scoring + the universal 5-pt/Independence overlay built together, additive to existing richness (PAT-015 floor-not-ceiling) | **3** | OPEN — **the sole surviving L3 blocker per PR#4** |
| **3** | **THRESHOLDS** | **13-row rail. 2 exemplary · 2 clean · 7 basis defects · 3 broken today.** For 4 rows the basis already exists elsewhere (HOM-02, `STATUS:68`, `STATUS:100`, ruled at CARL) ⇒ `:94`'s "durable bands home" claim is false in practice | **APPLIES** | **mixed: 3 broken = SUBSTANCE; 7 = missing HANDLE (transcription)** | Apply HOMER's **own FL template** to the other 11 rows. Not a new standard — its own | see split | **SPLIT ACROSS 1a/2a/4a** |
| **4** | **INVALIDATION / EXIT** | **Per-prediction: excellent** (`Invalidation` column, pre-registered triggers honoured when inconvenient, 10 of 11 surfaces datable). **Thesis-level: ABSENT — greenfield.** No kill rail anywhere under any name (11 variants + heading sweep + filename find, twice, independently) | **APPLIES** | **missing SUBSTANCE — AUTHOR-FROM-SCRATCH** | Author a thesis-level rail with §4's five elements/leg. ⚠️ **Warn the builder: the per-prediction machinery LOOKS like the missing rail and is not** — it covers 2 metrics; the thesis covers a transmission chain | **3** | OPEN — L3 blocker (b) |
| **5** | **PREDICTIONS** | **REFERENCE-GRADE behaviour on a thin book.** 2 rows, both OPEN, zero passed-resolver-ungraded. Multi-arm resolvers, named deciders, `Date_Resolved`/`Outcome` deliberately blank with the reason in-cell. Grades letter-honest under adversarial read. **No `Resolve_By` column** — every resolver anchored to an expected release, which has slipped twice | **APPLIES** | **conformant on discipline; missing HANDLE on schema** | Add `Resolve_By` distinct from the event date (PAT-115). ⚠️ **Caveat on record: n=0 predictions have CLOSED** — culture proven on interim grades, not a completed MISS. Both rows likely deliver that test within 90d | **1** | OPEN — schema only |
| **6** | **CROSS-AGENT ROUTING** | Inbox 0 / outbox 0 — **lane is clean.** But the **export truncates before the addressed section**, a registered RED-band cross never reaches its registered consumer, and the CREED seam names **no channel** (WALTER carried the row 5×) | **APPLIES** | **missing SUBSTANCE (delivery), not hygiene** | Move `**SENDING:**` above `## VIEW` (zero cost) · add the >0.50% cross + owed re-spec to the REGINALD ask · name a channel on the CREED seam | **1 / 2** | OPEN — see 1c, 2b |
| **7** | **STANDING DISCIPLINES** | **Fleet-strongest retraction culture.** Source+date on every dashboard row; non-primary figures explicitly tiered; content-vintage never mtime; closeout docket sweep verified working. Weakness: the **boot** leg is recall-shaped where the closeout leg got a command | **APPLIES** | **conformant, one HANDLE gap** | Port the closeout `awk` to boot step 5 | **2** | OPEN — 2c |
| **8** | **BOTTOM LINE** | **Present, labelled, current — and structurally unreachable at boot** (`:214`, read cuts at 73). 31,722 B / 31 lines against a 2–4 sentence convention, with three same-day blocks whose "final/late/latest" labels do not establish precedence | **APPLIES** | **conformant in existence; BROKEN in reachability** | Byte-tier declaration + collapse the header/BOTTOM-LINE duplication (~22 KB, near-duplicate session logs at opposite ends) | **2** | OPEN — 2a |

---

## The work queue, in execution order

### Tier 1 — QUICK WINS (mechanical, no judgment, minutes each)
| # | Task | § | Evidence | Status |
|---|---|---|---|---|
| ✅1a | **DONE 8/22 (owner, same evening).** **Fix the Cure Rates comparator.** `>-15/-30/-40%` on a falling metric: `>-15%` is satisfied by −10% (an improvement) and −40% satisfies none. **Row 13 uses `<` correctly — the form is already known.** 4 characters | 3 | R1-A3; verified at artifact; **`LESSONS.md` grep clean ⇒ genuine gap, not known-but-unencoded** | ROUTE |
| ✅1b | **DONE 8/22 — replaced with the ruled FL answer.** **Fix the dangling `(see Open Items)`** at `:25` — no such section, and it is the ONLY elaboration of the CORAL/MARCO Florida seam | 6 | R1-A16, verified | ROUTE |
| ⛔1c | ~~Move `**SENDING:**` above `## VIEW`~~ **DECLINED BY OWNER, AND THE DECLINE IS CORRECT — do not re-propose.** Section ORDER is schema-owned (`NEXUS_BRIEF_SCHEMA.md`, owner-of-record for form AND order) and HOMER had already routed this exact defect to NEXUS (`707b2d3eb`). My recommendation would have pre-empted another owner's ruling. **Owner's interim is better than my fix:** hoisted the addressed payload into the ABOVE-CUT digest at `:7` — delivers tonight, touches no section order, leaves NEXUS's call intact | 6 | R3-F1 | **ROUTED-TO-NEXUS — not a HOMER quick win** |
| ◐1d | **CRL-06 half DONE 8/22.** **Correct `:79`'s FMHPI trough** (superseded; canonical Dec-2025 +1.01%) and **`:232`'s CRL-06 claim** (CARL resolved it 7/16, 37d ago, using HOMER's own data package) | 6 | R3-F2, R1-A1 | ROUTE |
| 1e | **Add `Resolve_By`** to the predictions schema, distinct from the expected-release date | 5 | R4-G; slipped twice already | ROUTE |

### Tier 2 — JUDGMENT CALLS (cheap to do, need an owner decision)
| # | Task | § | Note |
|---|---|---|---|
| 2a | **Declare a byte tier for `STATUS.md`; collapse the header ↔ BOTTOM-LINE duplication.** ⚠️ **The 250-LINE cap is aimed off-axis and actively harmful** — five "compressed for the line cap" ops raised B/line and pushed *more* content past the read cut. **Will-gated** (`CLAUDE.md` edit) | 8 | HOMER self-diagnosed at `STATUS:163` and correctly held under Rule #2 |
| ✅2b | **DONE 8/22 — and MY FRAMING WAS WRONG.** I called it a two-desk routing gap and recommended PROME; HOMER declined, correctly: *"The band is mine, the crossing is mine, and the brief that dropped it is mine — PROME would just be a hop."* Sent direct to REGINALD with both riders. ⚠️ **AND MY EVIDENCE WAS LOOSE WHERE MY FINDING WAS RIGHT:** I read REGINALD's `0.50%` grep hits as "holds the level from a July packet"; HOMER checked properly — those hits are **Punta Gorda's metro rate and an old XLF move**. The finding survived; the supporting evidence was noise. Second instance this review of a true finding resting on shaky support (PAT-126's neighbour) | 6 | PAT-063; owner's own summary: *"I'd published the band in a file with no external readers and the level in a file with readers and never joined them"* |
| 2c | **Port the closeout docket `awk` to boot step 5.** Boot decides what the session *works on*; 5b's own rationale applies verbatim | 7 | R1-A10 |
| ✅2d | **DONE 8/22** — registered, with a pointer to `PROME/DOCKET.tsv:224` so the twin is not double-owned | 4 | R3-F4 |
| 2e | **Promote the Trepp-MF-row standing fix** off `SCRATCH` (which its own `:3` says is rewritten) onto a durable surface | 7 | R3-F9 |

### Tier 3 — BUILDS (real substance; the L3 path)
| # | Task | § | Note |
|---|---|---|---|
| **3a** | **Give the A–G servicer spec a durable, boot-read home.** Twice Will-ruled (8/14, 8/22); five homes, **not one both durable AND read**; violates HOMER's own `:170`. **Highest consequence on this card** — the rest is wrong text, this is a ruled spec degrading each session | 3 | R1-A4, sharpened |
| 3b | **Author `thesis/THESIS.md` + the thesis-level kill rail** — ONE build, greenfield, five elements per leg | 1+4 | L3 blockers (a)+(b) |
| 3c | **Build the convergence handle** (local scoring + 5-pt/Independence overlay) | 2 | sole surviving PR#4 blocker |
| ◐3d | **`:87` source label DONE 8/22; `:83` DISARMED not recalibrated 8/22** (no level invented, retune docketed Will-gated — the DISARM template applied exactly as intended). **Apply the FL basis template to the other 11 threshold rows** — start with `:83` (uninformative under every basis) and `:87` (source wrong vs practice) | 3 | 4 of them already have the basis written elsewhere |

### Tier 4 — POLISH
`MEMORY.md` unread at boot and carrying a now-false CREED fact · `reports/` absent from FILES and unread ·
the NEXUS fold-ordering check cannot discriminate when both files ship in one commit · undated figures on
the brief (ICE 280K shown as current spine, actually May) · `domain/` empty and unlisted · filename-as-state
on a ratified DRAFT report · no version/last-amended field anywhere in the charter.

---

## ★ OWNER-FOUND, 2026-08-22 POST-REVIEW — THE CUT IS A DECAY BOUNDARY, NOT ONLY A DELIVERY ONE

**HOMER found this by opening `## CROSS-DOMAIN` to verify my finding, and it is worse than I measured.**
That section had **also gone stale**: four of six WAITING-FOR rows superseded, one still reading
*"MBA Q2 NDS — DUE NOW, not posted"* **nine days after HOMER graded HOM-02's first resolver off that exact
release**. HOMER folded the brief **four times on 8/22 and every fold landed above line 74.**

> **THE CUT IS WHERE THE READER STOPS *AND* WHERE THE AUTHOR STOPS — THE SAME LINE.** So buried content
> fails **twice**: it does not arrive, *and* it is wrong when reached — while the fresh "FOURTH fold" stamp
> **above** it certifies the whole file. This is
> `finding_header_edit_is_the_edit_most_mistaken_for_maintenance` with a **STRUCTURAL** cause rather than a
> careless one. In the owner's words: *"I wasn't skipping it, I couldn't see it."*

**And the owner's interim mitigation had inverted:** "jump to `## CROSS-DOMAIN` first" was **directing
readers to the rottenest region of the file** — a delivery fix shipped in the belief that it covered
maintenance too. **The two are independent.**

**TESTABLE PREDICTION FOR THE 8/28 FLEET CHECK (register ⑳), owner-supplied and cheap:** *any* desk with
content past its read cut has **DECAY** there, not merely non-delivery — **and the freshness stamp above it
will read clean.** Testable against the **20-of-33** desks already measured by the `ledger_staleness`
base-rate pass. If it holds, the boot-sequence audit is measuring the wrong thing by half.

## Cross-cutting — NOT a section task

**The boot sequence is itself an untested guard** (review's governing finding). Both HOMER instances —
step 2 naming an unreachable BOTTOM LINE, step 6 blind to `docket/` and `thesis/` — are `CLAUDE.md` edits
and **Will-gated**; HOMER has changed neither. **My half is done:** the step-6 blindness was mine and is
fixed (`e23aeb51b`, verified both directions with the silence falsified). **The general question — audit
every desk's boot against its named tools' actual behaviour — is an 8/28 sweep candidate, not a HOMER fix.**

## Do-not-touch (carried from `profiles/HOMER.md`, re-verified 8/22)

`KB.tsv` FROZEN — never append/renumber (row-ID contract with CARL) · `state_vectors/corrected/` retrieval
hazard · the struck FL-YoY row + DISARM paragraph (**it is the TEMPLATE for fixing `:83` and `:88`**) · the
MARQUEE's retired-frame sentence · the 7/24 grading sheet post-print · the AMENDED-SAME-SESSION board_log
pair · `PREDICTIONS.tsv` line-1 prose preamble (carries a load-bearing ruling — **not** a schema defect) ·
the FL band derivation apparatus and its four-bases block · the A–G spec's base-rating machinery.
