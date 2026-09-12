# L337 — BOOT READ-PATH AUDIT
**Run:** 2026-09-11 21:3x ET Fri · session `prome-e1`, LAPTOP `WilliePOwen`, Opus 5 · read-only, **no production change made**
**Row:** `PROME/DOCKET.tsv` L337 (PROME runs + proposes / Will evaluates / CODEX scope author)
**Specimen:** this session's own boot, instrumented as it ran. Every figure below is measured at the artifact unless labelled ESTIMATE, RECONSTRUCTED or UNKNOWN.
**Revision 2026-09-11 21:4x — CODEX external review.** Four corrections, all accepted and applied in place: **§1e is new** (the boot was NOT complete when this report was first written) · **§1a is re-labelled RECONSTRUCTED, not observed** · **§4 savings are re-based against BOTH baselines** · the COT-35B disposition is corrected in §7. What the first draft got wrong is itemised in §8.

---

## 0. Measurement discipline (L337 / CODEX qualification 1)

Four quantities are kept apart and **never** derived from one another:

| Quantity | Status in this report |
|---|---|
| **File size** | MEASURED — `PROME/tools/measure.py` (wc -c) |
| **Generated output** | MEASURED — byte count of the tool's actual stdout / written file |
| **Emitted tool output** | MEASURED — bytes the tool wrote to stdout, JSON envelope included. ⚠️ **NOT the same as "delivered context": this report does not establish that every emitted byte reached the model.** The word "delivered" is avoided from here on. |
| **Observed timing** | PARTIAL — individual read-only checks timed; the one-shot gate's wall clock **UNKNOWN** (`boot_session.py` records no duration; its receipt files carry only `attempted_at`) |
| **Tokens** | **NOT MEASURED.** No tokenizer is available offline (`tiktoken`, `anthropic` both absent from `.venv`). No byte→token conversion appears anywhere in this report. |

---

## 1. Boot census — what actually reached the session

### 1a. Emitted tool output on this boot — **RECONSTRUCTED, not observed**

⚠️ **Provenance of these bytes.** They were produced by **deterministic replay** — re-running each read command against unchanged files and measuring its stdout — **not captured from the session record**. Same tool, same files, same offsets, so the figures should be identical to what was delivered; that is an argument, not a measurement. Treated as RECONSTRUCTED throughout. The only *observed* figures in this report are the wall clocks in §1c and the on-disk file sizes.

| Stream | Emitted B | % | How |
|---|---:|---:|---|
| INJECTED root `CLAUDE.md` | 22,633 | 17.2% | harness |
| INJECTED `PROME/CLAUDE.md` | 19,583 | 14.9% | harness |
| INJECTED `MEMORY.md` | 17,281 | 13.1% | harness |
| RUNNER `/boot` SKILL.md | 2,504 | 1.9% | tool result |
| RUNNER `PROME/BOOT.md` | 19,036 | 14.5% | `cat` |
| READ `USER.md` (1 page, eof) | 4,403 | 3.3% | `boot_read.py` |
| READ `HANDOFF.md` (p1 of 2) | 6,198 | 4.7% | `boot_read.py` |
| READ `SCRATCH.md` (p1–2 of 4) | 12,400 | 9.4% | `boot_read.py` |
| READ `ACTIVE_DECISIONS.md` (p1 of 5) | 6,207 | 4.7% | `boot_read.py` |
| READ `STATUS.md` header + spine-stamp grep | 6,277 | 4.8% | `head -c 3000` + `grep` |
| READ `HEARTBEAT.md` (p1 of 5) | 6,194 | 4.7% | `boot_read.py` |
| GATE `gate.txt` (2 pages) | 6,616 | 5.0% | `boot_read.py` |
| GATE env-doctor full log | 914 | 0.7% | `cat` |
| READ WALTER `LAST_COMPLETION` §WILL_NEEDS | 1,353 | 1.0% | `sed` |
| **TOTAL emitted before any work** | **131,599** | | |

⚠️ This is a ceiling on what reached the session, not a measurement of it.

Grouped: **injected 59,497 B (45.2%)** · procedure 21,540 B (16.4%) · state surfaces 43,032 B (32.7%) · gate as consumed 7,530 B (5.7%).
Had every FLAGGED check log been opened as BOOT.md step 5 instructs: **+12,137 B → 143,736 B.**

### 1b. The same boot read to `eof: true` (upper bound)

BOOT.md's bounded-reads paragraph says to follow `next_offset` until `eof: true`, then adds *"The manual's selected sections still determine read scope."* Measured both ways:

| Surface | File B | Pages to eof | Delivered to eof |
|---|---:|---:|---:|
| `USER.md` | 4,126 | 1 | 4,403 |
| `HANDOFF.md` | 10,185 | 2 | 10,622 |
| `SCRATCH.md` | 21,255 | 4 | 22,158 |
| `ACTIVE_DECISIONS.md` | 24,639 | 5 | 25,756 |
| `STATUS.md` | 24,381 | 5 | 25,485 |
| `HEARTBEAT.md` | 27,999 | 5 | 29,143 |
| **state total** | | | **117,567** |

**Boot as written, to eof: 206,134 B** — ⚠️ this figure covers injected canon + procedure + the six state surfaces + the gate as consumed; it EXCLUDES the 1,353 B WALTER §WILL_NEEDS read that §1a does include, so the two totals are not the same perimeter (207,487 B on the matched one). ** Boot's FIRST PASS tonight: 131,599 B.** ⚠️ **Revised twice. The gap is a MISS, not a licensed shortfall, and not "partly" either (CODEX).** The *"selected sections"* clause permits skipping sections a step does not send you to; it does not permit stopping before the ones it does. The first pass stopped before the operator card, the work queue, the decision rows and the Stress dashboard — all named by their steps. There is no reading on which that is compliant. **This session's boot, once completed, is the 206,134 B figure.** Reported because *any* claim about "how much work a boot is" is meaningless without saying which is being counted. The prior session's carried ~168 KB figure sits between them; it is not reproduced here and is not adopted.

### 1c. Observed timing

| Check | Wall clock | rc | stdout B |
|---|---:|---:|---:|
| `env_doctor.py --quiet` | 0.06 s | 1 | 913 |
| `firetime_check.py --window 7 --quiet` | 3.89 s | 1 | 1,491 |
| `position_agreement_check.py --all --quiet` | 0.08 s | 0 | 0 |
| `corrections_boot_check.py PROME` | 0.05 s | 0 | 243 |
| `docket_view.py --check` | 0.17 s | 1 | 1,085 |
| `spawn_list.py` | 0.60 s | 1 | 1,354 |
| `inbox_census.py` | 0.05 s | 0 | 714 |
| **sum of independently-timed checks** | **4.90 s** | | |
| nine bounded reads, re-measured | 0.45 s | | |
| one-shot gate, end to end | **UNKNOWN — not instrumented** | 1 | 6,168 (gate.txt) + 21,864 (all logs) |

**Narrowed (CODEX):** the seven checks timed above sum to 4.90 s, so *those* checks are not a constraint. ⛔ That does **not** establish that machine time is never a constraint — **end-to-end gate timing remains UNKNOWN**, and the checks timed are the cheap, independently-runnable ones, which is a biased sample. No claim is made about the boot's total wall clock.

### 1d. Two L337 hypotheses, tested

**Hypothesis 1 — the gate's repeated previews are a material duplication: NOT SUPPORTED.**
`gate.txt` is 6,168 B / 60 lines: 29 verdict lines (3,247 B), 17 path+rule pointers (1,739 B), **8 preview lines (903 B)**. Of those previews, **653 B** is re-delivered verbatim when the corresponding log is opened — **8.7%** of the gate's 7,530 B consumed footprint (653/7,530 — ⛔ the first draft printed **1.7%**, an arithmetic error from an unstated ~38,000 B denominator; the same denominator class as last session's withdrawn "~8% of a boot"). Small, not negligible. The gate's actual cost is opening the flagged logs (13,051 B for 5 flagged checks), which carry content the previews truncate.

**Hypothesis 2 — the generated DOCKET-VIEW block dominates SCRATCH: SUPPORTED, and it is load-bearing.**
The block is 10,917 B = 51.4% of SCRATCH's 21,255 B. It is generated, it is the only boot-path carrier of the 21-day catalyst window, and both blind readers of this test drew real items from it. **Narrowed (CODEX): that two readers drew useful items from it shows SOME of it matters — not that the whole projection is necessary.** Which parts earn their bytes is unmeasured. It is the largest single generated payload on the boot path. Out of scope for this pass (⛔ no merges/caps).

### 1e. The boot that produced this report was itself incomplete (CODEX finding, accepted)

**The first draft of this report opened with "Boot complete." while its own census recorded partial reads on five of six surfaces.** Those two statements cannot both stand. The census is right; the completion claim was wrong.

Calling the bounded reader once is not completing a document. What the first pass actually read, against what BOOT.md's per-step scopes name:

| Surface | First pass | To eof | Step's named scope | Reached it? |
|---|---|---|---|---|
| `USER.md` | 1 of 1 page | 1 | whole file | ✅ |
| `HANDOFF.md` | 1 of 2 | 2 | "top live entries only" | ✅ plausibly |
| `SCRATCH.md` | 2 of 4 | 4 | "what is hot **+ the operator card**" | ❌ **the operator card is on page 4** |
| `ACTIVE_DECISIONS.md` | 1 of 5 | 5 | "unresolved / approved-but-not-executed decisions" | ❌ reached 1 of 10 rows |
| `STATUS.md` | 3,000 B prefix | 5 | "health **and work queue**" | ❌ the work queue is on page 4 |
| `HEARTBEAT.md` | 1 of 5 | 5 | regime read | ❌ the Stress dashboard and the retired-claims cell are on pages 4–5 |

**The reads were completed from their saved offsets and digests after the review** — no boot restart, and the advancing gate was NOT re-run. **What completion surfaced that the partial read had not:**

- **`ACTIVE_DECISIONS` p4** — the TERRY row, the only row with live capital: the XLE fill price is **owed** (FORGE D-49, WQ-210 closes on the receipt) · VLO ×3 does **not** fire · `GATE-TERRY-007` 0-of-5 with the **9/10 and 9/11 cells still owed** · sleeve ENERGY $6,007.06 / duration-short $1,105.14 at the 9/10 close. p5: X1 **CLOSED, DON'T-SIZE**.
- **`STATUS` p4** — the Current Work Queue, including the **🔴 live market lane** (HY >280 X1 watch). Step 4's named target.
- **`HEARTBEAT` p4–5** — the **Stress dashboard**, which the file's own header calls *"the CANONICAL level table for every figure no amendment re-states"*, plus the Thresholds block and the **⛔ retired-claims / kill-on-sight cell** — an operationally binding do-not-assert list.
- **`SCRATCH` p4** — the operator card, and this line: **"★ Today/next: Sat 9/12 — … COT-35B blocking-flag disposition …"**. **The prior session had explicitly registered COT-35B as owing a disposition. It was on a page this boot did not read, and I then declared the gate cleared.** Two failures compounding: a partial read removed the contradicting evidence, and a green check was read as a resolution.

**Consequence for §4, stated because it is the easiest thing to get wrong:** a proposal that shortens the read must not book its savings against an execution that was already incomplete. §4 now reports both baselines.

---

## 2. What each routine surface uniquely supplies

**Churn, measured as 8-gram overlap with the same surface 7 days ago.** ⚠️ **This measures novelty, NOT necessity (CODEX).** A fresh session has no memory of last week, so text unchanged for a week can be wholly essential — root `CLAUDE.md` is 100% stable *and* 100% required. Read this column as "how much of this is new since last week", never as "how much of this is worth reading":

| Surface | Read B | Stable vs 7d ago | Unique boot-relevant content |
|---|---:|---:|---|
| root `CLAUDE.md` | 22,633 | **100.0%** | operating rules — injected by the harness, not PROME's to change |
| `USER.md` | 4,403 | **100.0%** | operator model + glyph canon |
| `PROME/CLAUDE.md` | 19,583 | 71.3% | spawn tiers, process controls |
| `PROME/BOOT.md` | 19,036 | 70.2% | the procedure itself |
| `ACTIVE_DECISIONS.md` p1 | 6,207 | **70.7%** | **see §3 — the read does not reach its own target** |
| `SCRATCH.md` p1–2 | 12,400 | 10.2% | ★ NEXT · cautions · "registered NOWHERE" — **the unique carrier** |
| `HEARTBEAT.md` p1 | 6,194 | 7.7% | regime state + amendments |
| `HANDOFF.md` p1 | 6,198 | **0.0%** | continuity; 99.7% live content by line class |
| `STATUS.md` header | 3,075 | **0.0%** | session headlines; the boot-relevant field (spine stamp) is *not* in it |

---

## 3. The finding — **RESTATED 21:4x, the first version was overstated (CODEX)**

⛔ **Withdrawn:** *"The manual addresses SECTIONS; the instrument addresses OFFSETS. There is no way to obey the manual."* and *"a reader told to read the work queue can only read page 1 and hope."* **Both are false.** `boot_read.py` pages to `eof: true` through the entire document (`PROME/BOOT.md:40` says so explicitly). Every named section is reachable today, by continuing. **PROME stopped early. The tool did not prevent compliance; I failed to comply.**

**What stands, narrowed:**

**① The boot's first pass did not reach the sections its own steps name.** Not a tool limitation — an execution failure, itemised in §1e. And *"the manual's selected sections still determine read scope"* does **not** license it: that clause permits skipping sections you were not sent to read; it does not permit stopping before the ones you were. The report cannot claim the target was missed *and* that the obligation was satisfied — §1b previously hedged this as "partly sanctioned," which was wrong and is corrected.

**② Section addressing is a navigation convenience, not a new capability.** It makes "read the work queue" a single addressed call instead of four sequential pages plus judgement about where to stop. That is worth something. It is not the difference between possible and impossible.

**③ The surfaces differ sharply in how much of the file their named scope covers — this is the finding with real consequences:**

| Surface | Named scope | Whole file to eof | Named scope alone | Section addressing saves |
|---|---|---:|---:|---:|
| `STATUS.md` | health + work queue | 25,565 B | Core State + Live Surfaces + Work Queue = **5,749 B** (+31 B stamp) | **19,785 B — most of the file is rotated session headlines the step never names** |
| `ACTIVE_DECISIONS.md` | unresolved decisions | 25,836 B | outline 3,501 + the FULL decision index 20,869 = **24,370 B** | **1,466 B (5.7%) — the named scope is nearly the whole file** |

**So the two surfaces that looked identical in the first draft are opposites.** On STATUS the boot is carrying ~20 KB of archived headlines it was never sent to read. On ACTIVE_DECISIONS there is essentially nothing to cut: if a boot must know each live decision's **Next · Backstop · Owner · Source**, it must read the rows, and the outline is only a way of finding them.

**④ Measured page-1 composition still holds**, as a description of what a truncated read costs: `ACTIVE_DECISIONS` page 1 is 44.0% stamp/header · 19.3% rules · 4.1% pointer · 32.6% content, and that content is one dormant row; the live TERRY row sits near byte 19,800. `STATUS`'s 3,000 B prefix is 100% headline and contains neither the work queue nor the spine stamp — which cost 3,277 B to grep, because the stamp is one ~3.2 KB line.

---

## 4. Recommendation — **REVISED: two separate decisions, and v1 is NOT recommended**

The first draft asked to adopt an outline as the boot read. **Withdrawn.** The validation (§5) shows v1 **loses** an urgent obligation the current path catches — a demonstrated regression, not residue to defer. And an outline that keeps two cells of a six-column table (`Decision | State | Owner | Next | Backstop | Source`) **drops the action, the backstop, the owner and the source**. A row appearing in an outline does not establish that its obligation was read. These are two different asks and they are now separated:

> **① NAVIGATION (proposed for adoption).** `boot_read.py --section "<heading>"` — an **optional, lossless** way to address a named section: still paged, still digest-checked, still continues to `eof` within the section, with explicit rc-distinct handling for a heading that is **missing** or **ambiguous** (never a silent empty read). It changes no default and no read scope. A step that today says *"read the work queue"* can address it directly instead of paging past ~20 KB of rotated headlines.
>
> **② REDUCED READ SCOPE (NOT proposed — evidence not yet gathered).** Whether the boot may read *less* than a surface's named scope is a separate decision that needs evidence the selected content preserves the obligations. This audit did not establish that. **`--outline` stays a navigation aid; it must never silently become the complete read.**

**Honest savings, with follow-on reads included** (the first draft omitted them, which is what made −21,595 B on ACTIVE_DECISIONS wrong):

| Surface | Compliant read today | With § addressing, obligations preserved | Saving |
|---|---:|---:|---:|
| `STATUS.md` | 25,565 B | 5,780 B | **−19,785 B** |
| `ACTIVE_DECISIONS.md` | 25,836 B | 24,370 B | **−1,466 B** |
| **Total, ① alone** | **51,401 B** | **30,150 B** | **−21,251 B** |

The STATUS saving is real and comes entirely from *not paging through archived headlines the step never asked for*. The ACTIVE_DECISIONS saving is near zero, and saying so is the point: **§1's large blocks remain untouched, and ① is a navigation improvement, not a validated reduction in boot work.**

⚠️ **Superseded figures — do not quote:** ⛔ *"−4,833 B / 3.7–5.2%"* (compared a compact outline against an incomplete read) · ⛔ *"−43,590 B"* and ⛔ *"−21,595 B on ACTIVE_DECISIONS"* (assumed the outline replaces the row read; it does not).

---

## 5. Validation — the detection test (L337 / CODEX qualification 2, binding)

**Method.** Eleven synthetic items were planted in **disposable copies** of STATUS · ACTIVE_DECISIONS · HANDOFF · SCRATCH, held in the session scratchpad. **No live ledger and no Decision Deck was touched.** Six URGENT + **five ordinary NON-URGENT negative controls**. Both read paths were run against the **same** fixture, producing two transcripts (current 31,719 B · proposed 25,601 B). Two **blind** `coldreader` agents — fresh context, each seeing only its own transcript, neither told plants existed — produced triage lists. A **third, separate agent held the answer key and graded**. PROME designed the fixture and did **not** grade. Five neighbour classes were instantiated: ordinary (U2) · overlap (U5) · wrong owner (U3) · missing information (U1, no date attached) · concurrent activity (U6, planted in a header line).

**Mechanical delivery** (grep on the transcripts — a fact, not a judgement):

| Plant | Where | Current | Proposed |
|---|---|:--:|:--:|
| U1 ZION 45P fill unknown | AD last row (~b20,300) | ✗ | ✓ |
| U2 intake contract, Mon 9/14 | AD mid row (~b12,000) | ✗ | ✓ |
| U3 WATT blocked, key expired | STATUS work queue | ✗ | ✓ |
| U4 FORGE reconcile (equivalence control) | SCRATCH ★ NEXT | ✓ | ✓ |
| U5 safe-push non-ff (overlap) | HANDOFF top entry | ✓ | ✓ |
| U6 GATE-CREED-R4 unregistered | AD **header line** | ✓ | ✗ |

**Grade of record (independent grader):**

- **Urgent recall — CURRENT 3/6** (missed U1, U2, U3) · **PROPOSED 5/6** (missed U6).
- **Negative-control precision — CURRENT 5/5 · PROPOSED 5/5.** The grader ruled the current path's score **partly unearned**: three controls were never delivered to it, and *"you cannot false-positive on bytes you never received."*
- **Items raised — 26 each.** No dilution differential.
- **U6: the proposed path failed it, plainly.** An obligation parked outside any content section is invisible to an outline. The grader noted two mitigations: the current path found U6 and then ranked it MEDIUM, tenth of twenty-six — delivering the bytes did not produce proportionate attention — and **n=1**.

**⚠️ This result is a reason NOT to ship v1 (CODEX, accepted).** The first draft filed U6 as residue to fix later while still recommending adoption. That was wrong: a path that loses an urgent obligation the current path catches is a **demonstrated regression**, and regressions are not deferred residue. §4 no longer proposes v1.

**⚠️ The grader's criticism of the test, carried forward rather than buried:**

1. **The plant distribution, not the read paths, largely determined the score.** Three urgent items were placed deep enough that any page-1 read must drop them, against one placed on page 1. *"The 5/6-vs-3/6 result is close to a restatement of where the designer chose to put the items."* It supports **"the proposed path recovers deep-file content, the current path recovers early-byte content"** — it does **NOT** support "the proposed path is 67% better at boot triage." **No recall ratio from this run should be quoted as a quality measure.**
2. **The precision axis produced no signal** — both arms 5/5, and asymmetric control delivery makes the two scores non-comparable.
3. **No urgency rubric**, so every defensibility call was the grader's against no standard.
4. **U6's "concurrent activity" class label does no work** — it is a placement test wearing a class label.
5. Neither reader noticed it had been handed a truncated file — the grader's own suggestion for a better future test item.

**What the test therefore establishes:** a *mechanism* — the current read cannot reach the Live Decision Index or the STATUS work queue, the proposed read can, and the proposed read drops header-line content. It does **not** establish an improvement ratio.

**Untested residue.** A v2 prototype emits field lines (`**Label:**`) and any line carrying ⚠️/⛔, which **mechanically restores U6** (delivered 4,161 B, `GATE-CREED-R4` present) at a cost of 2,039 B against v1. **This was tuned against a known failing case and has NOT been put to an independent reader.** It must not be reported as validated. **And it does not generalise (CODEX):** v2 keys on `**bold-label**` lines and the glyphs ⚠️/⛔. An obligation written in ordinary prose, in a header or anywhere else, carries none of those markers and is still lost — the fix pattern is `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`, which is the defect it was meant to repair.

---

## 6. Closeout census — measured, NOT part of the recommendation

A Standard-tier closeout is **45 discrete operations** across ~17 written surfaces: 19 writes · 14 checks · 3 reviews · 3 generates · 3 publishes · 1 read · **2 retry loops** (gate rc=1 → regenerate 4 derived artifacts → re-run; and non-ff push recovery). **25 of the 45 are conditional.** Manual + runner = 36,192 B of procedure text.

**The measured duplication is registered rows, not prose.** For the 2026-09-11 evening session, 8-gram overlap between STATUS / HANDOFF / SCRATCH / daily memory is only **0.8%–10.9%** — so the surfaces are *not* textual copies and no dedup tool would find anything. But of the 89 distinct named tokens (WQ-n, DOCKET L-rows, GATE-*), **33% appear in ≥2 of the five account surfaces, 19 appear in 3+, and 9 appear in 4+.** Every one of those nine — `L260 L311 L320 L330 L337 WQ-219 WQ-231 WQ-232 GATE-BRENT-COT-35B` — **is a registered row.**

Restatement counts: SCRATCH 52 mentions / 36 distinct · daily memory 79 / 39 · STATUS 19 / 12 · HANDOFF 15 / 12 · BRIEF 3 / 3.

**WQ-232's rule — *"registered rows are POINTERS here, never restatements"* — was written for SCRATCH alone.** The same rows are restated, in different words, in STATUS, HANDOFF, the daily log and BRIEF. That is the mechanism behind CODEX's central question. **Recorded as the next candidate; not started, and not this pass's recommendation.**

---

## 7. Recorded, not started (per Will's instruction)

- ⛔ **`GATE-BRENT-COT-35B` — CORRECTED. Its status is: NOT OVERDUE under today's date check; NOT established resolved.** My boot report called it *"✅ cleared / the risk did not materialise."* That was unsupported and is withdrawn. Verified at the artifacts: `prome_gate.py:150` tests `date.fromisoformat(review_by) < today`, so a `review_by` of **2026-09-11** read on **2026-09-11** cannot fire — the green check means *the deadline has not passed*, never *the grade is in*. The row is **LIVE**, `scannable=INSTRUMENT`, and its **`last_checked` is still `2026-09-06` (BRENT vintage #4, as-of 9/1)** — the 9/8-vintage grade the `review_by` was set for has **not** landed. It flags BLOCKING at the first boot on/after 9/12. Disposition: consumer read at BRENT's artifacts first; never move an owner-set date. *(This is `[[finding_gate_pass_is_not_evidence_it_found_the_best_reason]]` — and SCRATCH page 4, which I had not read, carried the line "COT-35B blocking-flag disposition" in its own ★ Today/next.)*
- `PROME/CLOSEOUT.md` self-contradiction, **verified at the artifact this session**: line 29 says Light tier = *"targeted update … never a mandated full rewrite"*; lines 46 and 118 both mandate *"full rewrite"* unqualified. (L338.)
- `env_doctor` rc=1 — `FFIEC_CDR_TOKEN` + `FFIEC_CDR_USERNAME` absent on this laptop in `.env`, secondary homes and process env. Machine-local; no FFIEC-dependent claim made this session.
- HEARTBEAT 86% (15th re-base owed) · ACTIVE_DECISIONS 75% · `CLOSEOUT.md` 92.7% of read cap.
- L260 BROCK · L311 OTTO · L320 RED all DARK on due rows; 12 unconsumed `PROME/inbox/` packets; spine audit turns 7d 9/12.
- `boot_session.py` records no wall-clock duration — why §1c reports the gate's timing as UNKNOWN.
- `firetime_check.py` emits 1,491 B under `--quiet` but 8,900 B into the gate log.

## 8. Errors owned this session

**Four found by CODEX external review, not by me:**

1. **I converted a green gate into a resolution.** "COT-35B ✅ cleared — the risk did not materialise" was an inference from a check that structurally could not fire today, against a row whose `last_checked` shows the grade never arrived. Corrected in §7. The compounding detail matters more than the error: **the surface that would have contradicted me (SCRATCH p4) was in a page my own boot had skipped.**
2. **I reported "Boot complete" over a census that recorded partial reads on five of six surfaces** — the report contradicted its own opening line. §1e is the correction, and the completed reads are now in the session.
3. **I labelled reconstructed measurements as delivered.** §1a's byte table came from re-running the read commands, not from the session record. Re-labelled RECONSTRUCTED; the distinction now appears in §0.
4. **I booked the proposal's savings against an execution that was already incomplete.** §4 now reports **−21,251 B against the compliant read, with follow-on reads included**; the earlier −4,833 / −43,590 pair is SUPERSEDED and must not be quoted (§4 lists both as retired).

**Four more found by CODEX on the revised draft:**

5. **I claimed the tool made compliance impossible.** *"There is no way to obey the manual" / "page 1 and hope"* — false. `boot_read.py` pages to eof (`BOOT.md:40`); every named section is reachable today by continuing. I stopped early and blamed the instrument. §3 is rewritten; this is the most serious error in the report, because it converted my own execution failure into a tool defect and then proposed building something.
6. **I booked a saving the proposal does not deliver.** The outline keeps 2 of 6 columns, dropping **Next · Backstop · Owner · Source** — so on ACTIVE_DECISIONS the rows must still be read, and the true saving is **1,466 B (5.7%)**, not the 21,595 B I published. A row's presence in an outline is not evidence its obligation was read.
7. **I recommended adopting v1 while reporting that v1 loses an urgent item.** A regression filed as residue. §4 withdraws it and splits navigation from read-scope reduction.
8. **Arithmetic: 653/7,530 = 8.7%, published as 1.7%** — an unstated ~38,000 B denominator. ⚠️ **Second denominator error in two sessions** (last session's withdrawn "~8% of a boot"). The pattern is publishing a ratio without printing its denominator beside it.

Three further narrowings accepted without dispute: "emitted stdout" is not "delivered context" · timing seven cheap checks does not establish that machine time is never a constraint · low week-over-week churn measures novelty, not necessity — a fresh session needs stable text as much as new text.

**Also mine, and recurring:** `echo "RC=$?"` after a pipe reports `tail`'s exit status, not the wrapper's — it printed `RC=0` beside a gate that had returned **rc=1**. Nothing was misread here only because `boot_session.py` prints its own verdict line. **The same pattern was flagged at a previous closeout.** Fix is `set -o pipefail` or reading the wrapper's own line; the durable lesson is that a shell receipt about an exit code is not evidence of that exit code.

**Found by me:**

- I framed the eof-vs-page gap as a written-versus-practised contradiction before reading BOOT.md's *"The manual's selected sections still determine read scope"* clause, which resolves it. §1b is the corrected form.
- My first count of the Live Decision Index said 7 rows; it is 10. The `--outline` prototype caught it — my `grep '| \*\*'` pattern had dropped three rows that open without bold. `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`.
