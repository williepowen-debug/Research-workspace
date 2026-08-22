# HOMER Structure Review — PLAN (drafted 2026-08-22, Will-directed)

**Status:** RULED + EXECUTING — Will ruled 2026-08-22: **Mode-A fan-out · targeted C1+C2+C3 · notify at delivery only.**
Fan-out launched (4 readers: R1 charter/boot · R2 STATUS · R3 brief/scratch · R4 falsification —
C2 split into R2/R3 because it is 220 KB, too large for one reader). Nothing routed, nothing edited.
**Subject:** HOMER (Market class, FLEET_MAP L2, last scored 2026-08-17 PR#4)
**Reviewer:** DAEDALUS · **Snapshot pinned at:** `f7c63add3` ("ruling packet consumed and filed", 2026-08-22 18:12:51 -0400)

> ⚠️ **PIN DRIFT, OBSERVED IN-SESSION — the §1 constraint demonstrating itself.** The pin was `abc7fc58a`
> when this plan was drafted and `f7c63add3` ~minutes later, while the readers were being spawned. Two
> HOMER commits landed inside one planning session. **Every finding this review produces must be
> re-verified at artifact against the THEN-CURRENT tree immediately before routing** — not against the pin,
> and not against the readers' snapshots. The pin's job is to date the evidence, not to license it.

---

## 1. The governing constraint: HOMER IS LIVE

HOMER is running in another window **right now** — commit `abc7fc58a` landed between my boot read and this
plan. 52 commits in the last 14 days. Two consequences, both binding:

1. **Packet-only. No direct edits, whatever we find.** AUTHORITY guard 2 (`CLAUDE.md`): permission and idle
   BOTH must hold, and idle does not. Even a one-cell fix gets clobbered by a live session (root Critical
   Rule #2, PAT-004). Every finding routes to `AGENTS/HOMER/inbox/` as a task packet.
2. **Every read is a snapshot, and the snapshot will be stale before we deliver.** This is the exact class I
   was caught on eleven days ago against AEOLUS — I read a boot git-status snapshot, called a desk's true
   commit claim partial, and had to own it (register ⑯, `finding_record_of_an_action_is_not_the_action`).
   **Discipline for this review: grade against a NAMED COMMIT, say so in the packet, and re-verify every
   🔴 at artifacts immediately before routing.** A finding that HOMER fixed while we were reading is worse
   than no finding — it burns the packet's credibility for the findings that are real.

---

## 2. What already exists (and its condition)

| Artifact | State | Verdict |
|---|---|---|
| `profiles/HOMER.md` | Built **2026-08-07**, Mode-A single-reader over **61 files** | **STALE — refresh, don't re-found.** Tree is now 89 files / 1.3 MB. Its own stated staleness rule ("re-read after the next HOMER session closes the 5 passed resolver dates") has fired many times over. |
| `upgrades/HOMER_CARD.md` | **DOES NOT EXIST** | HOMER has been graded twice (profile 8/7, PR#4 8/17) and never received the DECOMPOSE artifact. Job 3b's flow is COMPREHEND → DECOMPOSE → SECTION-TASKS; leg 2 was never built. **This review's primary structural deliverable.** |
| `FLEET_MAP.tsv` row | L2 / Conf H / scored 8/17 | L3 blocked on ONE leg: convergence handles NOT BUILT. Plus an owed PREDICTIONS.tsv mirror write-back. |

---

## 3. Already verified this session (mechanical recon — carry into the review, do not re-derive)

Four findings are **in hand before the review starts**. Two are new since the 8/07 profile:

1. **🔴 `STATUS.md` = 155,933 B / 241 lines (647 B/line) — and HOMER's own BOOT step 2 is "Read STATUS.md".**
   This is **PAT-111 pointed outward** — the defect I found on myself 8/17 (425 KB boot spine silently
   degrading every boot to fragments). HOMER is under its 250-**line** cap and 6× over any sane byte budget:
   the cap is aimed off-axis (PAT-086, now n=5+ — kin BOND 404 B/line, TERRY 409 B/line; **HOMER is the
   densest of the three**). *Verifiable, not inferred: measure the actual truncation point at HOMER's read
   instrument before asserting it degrades — PAT-074, what does the PASS prove.*
2. **🔴 `thesis/THESIS.md` still does not exist** — `thesis/` holds PREDICTIONS.tsv alone, 15 days after the
   profile named this the single L3-blocking absence. Confirms the L2 grade and that the leg is
   **author-from-scratch**, not extract-and-stamp (profile §"two L3-blocking absences" — a future reader
   must not go hunting for an existing rail to stamp; there is none).
3. **✅ Routing lane is CLEAN** — inbox 0 unprocessed, outbox 0 sitting. The 8/07 profile's 🟠 "3 inbox
   packets unprocessed" flag is **CLOSED**. Record it as a closed flag, not silence.
4. **★ A visible recurring class in the last four commits**, all self-caught, all the same shape:
   *"the ATTOM fix reached the dashboard and died before the docket"* · *"I told PROME 'adopted' before any
   surface carried it"* · *"my lesson was filed as a novel local pattern; it is an instance of an existing
   fleet rule"* · *"the lesson I wrote failed on its own first opportunity, because I scoped it to the
   occasion instead of the mechanism."* → **HOMER's fixes do not complete their propagation path, and its
   lessons are scoped to the occasion.** This is not a defect list — it is a *mechanism* worth a dedicated
   lens (§5, L4). Note it cuts BOTH ways: HOMER caught all four itself. The judgment layer is above the
   grade; the structure is what lags (the profile said exactly this on 8/07).

---

## 4. Method — Step 0 refresh, then decompose

Per `UPGRADE_PROTOCOL.md`: **COMPREHEND (refresh profile) → DECOMPOSE (build the card) → SECTION-TASKS.**
Because a profile already exists, this is a **delta refresh against the 8/07 baseline**, not a fresh
comprehension — cheaper, and the 8/07 flag list becomes the first checklist (each flag: CLOSED / OPEN /
SUPERSEDED, verified at artifact).

**Read decomposition — 5 clusters, ~300 KB of live surface (the 89-file tree minus archive/processed):**

| # | Cluster | Files | The question it answers |
|---|---|---|---|
| C1 | **Charter + boot** | `CLAUDE.md` (233 ln), BOOT block, Key Thresholds :76-121 | Does the boot sequence read what the desk actually depends on? Is the threshold rail current? (⑪ hardcoded-list class, ⑯ activity-proxy class) |
| C2 | **State surfaces** | `STATUS.md` (156 KB!), `SCRATCH.md`, `NEXUS_BRIEF.md` (62 KB) | Byte/read-cap defect (§3.1); two-clock drift; does the cross-agent brief agree with STATUS? (the 8/07 🔴 BANC residue lived here) |
| C3 | **Falsification + predictions** | `thesis/PREDICTIONS.tsv`, `reports/*grading-sheet*`, threshold rail | The L3 leg. **Feeds Falsification Sweep #2 on 8/24 directly** — HOMER is the fleet's one confirmed rail-less desk. |
| C4 | **Workbook (8 ledgers)** | KB/KB_LIVE/PIPELINE/MULTIFAMILY/STATE_HSG/BUILDER/RATES/PRICING + `SCHEMA.tsv` | Two-state hygiene (was best-in-cohort); SCHEMA covered 6 of 8 at 8/07 — closed? Staleness vs STATUS-writes. |
| C5 | **Ops + learning** | `LESSONS.md` (100 ln), `board_log.tsv`, `docket/CATALYSTS.tsv` (78 KB), inbox/outbox | The §3.4 propagation class; passed-unworked `Next:` dates (PAT-089 instance 3 at 8/07 — recurred?); catalyst-registry currency. |

---

## 5. The lenses (what we are actually looking for)

Not a generic checklist. Six, each earned and each cheap:

- **L1 — Blueprint grade, per-leg.** Every ladder leg gets an explicit `PASS / FAIL / WAIVED-<cite> /
  NOT-ADJUDICATED` verdict row (idea 4, Will-ruled 8/20). A skipped leg must read as a visible blank.
- **L2 — Run HOMER's guards OUTWARD, both directions.** Don't read its validation claims — execute them.
  *What does its PASS prove, and what did I watch FAIL?* (PAT-074 / UPGRADE_PROTOCOL ★, the highest-yield
  hour of the VIRGIL review.) HOMER has a `Next:` two-clock header convention that IS its working detector —
  test whether it discriminates.
- **L3 — Metric-surface audit (8/28 register ⑰, two legs).** For every registered threshold: (a) name the
  COMMAND that returns its number; (b) name the BASIS/observation-window it is written on. Base rate on
  other desks ran ~95% defective (AEOLUS n=7, MARCO 35-of-37). HOMER's Key Thresholds block is the
  fleet's *strongest* threshold dimension per the profile — **this is a genuine test of whether ⑰'s base
  rate holds on a strong desk, and a NEGATIVE result is a real finding for the sweep.**
- **L4 — Propagation completion (§3.4).** Trace 2-3 of HOMER's own recent fixes end-to-end and find where
  they stop. Its own commits say dashboard-yes/docket-no. Kin PAT-087, PAT-113, `finding_transfer_completes_only_when_the_receiver_encodes`.
- **L5 — Read-cap / byte-tier (§3.1).** Measure, don't assume. Then the blueprint §8 declare-from-measured-density
  procedure, BRENT as the donor execution.
- **L6 — Record the refuted hypotheses.** I expect L3 to find HOMER's thresholds mostly *sound*. If so that
  is a result and it gets written beside the confirmed findings — a review that reads uniformly damning gets
  its real findings discounted with it (UPGRADE_PROTOCOL ⚠️).

---

## 6. Deliverables

| Artifact | Home | Note |
|---|---|---|
| Refreshed `profiles/HOMER.md` | mine | Delta-refresh w/ §3 invalidation inventory re-cut |
| **`upgrades/HOMER_CARD.md`** | mine | The missing DECOMPOSE artifact — 8 blueprint sections × `current / applies? / gap type / proposed handle / priority / status`. **The durable win of this review.** |
| `upgrades/HOMER_REVIEW_2026-08-2x.md` | mine | Findings, ranked, w/ per-leg verdict table |
| `*_READER_REPORTS.md` companion | mine | **MANDATORY if we fan out** (PAT-100): raw tables + pointer map + **every reader's not-read/coverage-limit list** |
| **Task packet → `AGENTS/HOMER/inbox/`** | HOMER's | The only thing that reaches the owner. Reconciled item-by-item against each reader's ranked route list before shipping (PAT-102 — *dedupe against "did this reach the owner?", never "did I capture this?"*) |
| FLEET_MAP row re-cut + `render_directory.py` | mine | Closeout step 7 |

---

## 7. Decisions Will owns

1. **Method/depth.** Mode-A fan-out over the 5 clusters (fast, parallel, ~$0.15-0.30, needs your explicit
   go-ahead — I don't spawn without it) vs. serial single-reader by me (slower, no companion-file overhead,
   fully in my context). The tree is 1.3 MB; serial is *feasible* but C2 alone is 220 KB.
2. **Scope.** Full architecture audit (all 5 clusters, RED/BOND-style) vs. targeted (C1+C2+C3 only — charter,
   state surfaces, falsification — which is what feeds 8/24 and skips the workbook).
3. **Do we tell HOMER we're reading it?** `ListAgents` + a doorbell message is available and costs nothing.
   Argument for: it's mid-session and may be about to rewrite the surfaces we're grading. Argument against:
   an observed desk behaves differently, and this is a structure review, not a trap. **My lean: yes, notify
   at DELIVERY, not at start** — CROSS_SESSION rule 6 wants a doorbell at packet-commit anyway, and a
   heads-up now buys nothing while the read is still forming.

---

## 8. Sequencing against existing clocks

- **8/24 Falsification Sweep #2** (2 days, on-cadence — my L5 proof point, does NOT slip). **C3 feeds it
  directly**: HOMER is the confirmed rail-less desk, so doing C3 first makes the sweep richer rather than
  competing with it.
- **8/28 wiring sweep** (18-item register) — L3 above is register item ⑰ run on a strong desk; C1 is items
  ⑪/⑯. **This review is a live rehearsal for three sweep legs, not a detour from them.**
- **My STATUS is at 98.0% of byte budget** — this review's output goes to `upgrades/`, and the STATUS
  entry must be a pointer line, not a narrative block (PAT-123).

**Recommended order: C3 → C1 → C2 → C5 → C4**, falsification first (clock-driven), workbook last (cheapest
to defer, and the 8/07 read said it was the healthiest cluster).
