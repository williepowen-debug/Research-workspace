# CLOSEOUT-DOCUMENT AUDIT — BRENT (round 2)
**Author:** BRENT · 2026-07-31, clock verified **12:14 EDT** (`date`) · **AUDIT ONLY — ZERO EDITS APPLIED.**
**Baker Hughes:** not posted at audit time (~1:00 PM print). Completed inside the window; no park marker.
**Method note, given this morning's F9/F10:** every cited line was **opened and read**, not inferred from mtime or a grep count. **That discipline changed two verdicts mid-audit** — see the ⚠️ corrections in C1 and C7.

**11 flags. 2 HIGH, 4 MEDIUM, 5 LOW/structural.**

---

## 🔴 HIGH

### C1 — `LESSONS.md:54` STILL ASSERTS THE RETIRED DIRECTIONAL STNG VETO, AND IT IS READ AT EVERY BOOT
**Says (verbatim, L18 prose):** *"**Tanker equity (STNG) is the fastest sanity check — if tankers aren't repricing down on an 'announcement day,' the market isn't treating it as operational either.**"*
**Wrong because:** Will **retired exactly this rule today**. Stage-A v5 replaces it with **(T) liveness — `max(|STNG|,|FRO|,|DHT|) ≤1.0%` blocks, SIGN DISCARDED**. `LESSONS_INDEX.tsv` was amended accordingly (`tanker_selloff=SIGN_DISCARDED_LIVENESS_ONLY`) — **the prose was not.**
**Also stale in the same line:** the verification gate names *"(b) Lloyd's vessel transit counts returning to **60-135/day** baseline"* — superseded twice over (the transit leg is no longer an entry condition, and my own `domain/HORMUZ_TRANSIT_BASELINE.md` pins the canonical denominator at **88 `n_total`**, not a 60-135 band).
**Severity:** **`LESSONS.md` is BOOT STEP 3 — read every session, ahead of any spec file.** A fresh BRENT boots, reads that tankers must sell off, and carries a rule Will killed. **This is the F1 class again — a boot-read surface contradicting the ruled spec — one day after F1.**
**Root cause is C2.** **Class:** (a) self-fixable — **but HIGH: it misinforms every future session, including a fire-day session.**

### C2 — **NO CLOSEOUT STEP OWNS `LESSONS.md`. THAT IS WHY C1 EXISTS.**
Boot **step 3** reads `LESSONS.md`. **Grep of my whole `CLAUDE.md`: exactly 2 occurrences — boot step 3, and a caveat inside step 5b. ZERO closeout steps write it.**
The only maintenance instruction is buried in **boot step 5b**: *"When you ADD or AMEND a lesson, add/update its `LESSONS_INDEX.tsv` row in the same edit"* — **which points at the INDEX, not the prose.** So the documented obligation is *index-side only*, and the prose has no owner at all.
**Evidence it is live, not theoretical:** `LESSONS.md` last touched **2026-07-30**; `LESSONS_INDEX.tsv` last touched **2026-07-31** (`aede1959`). I amended **four** lesson resolutions today and touched no prose.
**⚠️ AND THE CHECKER CANNOT SEE IT:** `scripts/lessons_check.py` reads **only** `workbook/LESSONS_INDEX.tsv` — **zero references to `LESSONS.md`.** So the mechanism I built to stop lesson contradictions **validates the spine and never opens the body it is a spine of.** A prose/index divergence is invisible by construction.
**Class:** **(b) needs a ruling** — the fix is a new closeout step (and arguably a `--prose` check), i.e. an addition to my own boot/closeout doc.

---

## 🟠 MEDIUM

### C3 — CLOSEOUT STEP 8 DIRECTS WRITES TO **THREE FROZEN FILES** (the F9 class, ×3, in the primary instruction)
`CLAUDE.md:63` step 8: *"log new facts/claims → `workbook/KB.tsv`; changed indicator levels → `workbook/VX.tsv`; transmission/cascade mechanics → `workbook/FLOW.tsv`."*
**All three carry `# FROZEN 2026-07-01 — NOT MAINTAINED`** (verified by opening each). **This is the exact defect I fixed in step 9 this morning** (TIMELINE), still live in step 8 and **three times over** — and it is step 8's *opening* clause, so a compliant session either writes to frozen ledgers or silently skips the step and reads as covered.
**Class:** (a)/(d) — retire the three clauses; the rest of step 8 (PREDICTIONS resolution, CHANGELOG) is sound and stays.

### C4 — ROOT-CANON SESSION-END STEPS **1b / 1c / 1d ARE ENTIRELY ABSENT** from my closeout
Grep of `AGENTS/BRENT/CLAUDE.md`: **`orphan_check` = 0 · `consumer_check` = 0 · `memory_index_check` = 0.** Only `safe-push` appears (step 14, ×1).
Root `CLAUDE.md` mandates all four at session end. **Step 14 gestures at the canon** (*"commit own files per root CLAUDE.md §Git Protocol"*) **but names only the push.**
**Why it matters:** root `CLAUDE.md` is auto-injected, so a diligent session still runs them — **I ran orphan_check and memory_index_check today for exactly that reason, not because my own doc told me to.** But my closeout is the doc a session actually executes step-by-step, and **1c (consumer_check) is the one most likely to be skipped**: it fires only when you supersede a published number, which is precisely today's case — **I superseded the gasoline-ban end-date (Dec 31 2026 → Jan 31 2027) and the Stage-A entry semantics, and never ran `consumer_check.py`.**
**Class:** (b) — adding steps to my closeout doc needs sign-off; **but note the live miss above is (a)-fixable by just running it.**

### C5 — **BOOT↔CLOSEOUT SYMMETRY MATRIX — four surfaces are read-only or write-only**

| Surface | Boot reads | Closeout writes | Verdict |
|---|---|---|---|
| STATUS.md | 1 | 7 | ✅ paired |
| TRADE.md | 1, 6c | 7 | ✅ paired |
| SCRATCH.md | 2 | 11 | ✅ paired |
| NEXUS_BRIEF.md | — | 12 | ⚠️ **write-only** (see C6) |
| **LESSONS.md** | **3** | **— NONE** | 🔴 **read-only ⇒ C1/C2** |
| **domain/REFERENCE_TABLES.md** | **4** | **— NONE** | 🟠 **read-only** — no step owns refreshing it; it drifted to a March vintage and only got annotated because *this morning's audit* touched it, not because closeout did |
| board_log.tsv | 6, 6b | 13a | ✅ paired |
| docket/CATALYSTS.tsv | 5 (via script) | 10 | ✅ paired |
| thesis/PREDICTIONS.tsv | 5 (via script) | 8 | ✅ paired |
| **local `MEMORY.md`** | **— NONE** | **13** | 🟠 **write-only** — closeout writes durable BRENT-specific learnings to a file **no boot step ever opens.** Step 13 even says to *delete* from it after promoting to auto-memory, so its whole remaining purpose is unread content. |

**Class:** (b) for LESSONS/MEMORY (structural decisions), (a) for REFERENCE_TABLES.

### C6 — `NEXUS_BRIEF.md` IS WRITE-ONLY AND ITS CLOSEOUT STEP HAS NO ACCURACY TEST
Step 12 mandates a write every session and its **minimum is a stamp refresh** (*"minimum is refreshing the `As of:` stamp + `STATUS commit:` hash so staleness self-corrects"*). **A refreshed stamp on stale content makes the file look MORE current while staying wrong** — which is precisely how the Stage-A block stayed stale 7/24→7/31 while the stamp moved (F1), and how "pending fill" survived 7/24→7/28 before that. **Twice in eight days, on the same file, through a step that ran both times.**
**The step's own words invite it:** *"Material STATUS change → brief content updates same session"* leaves "material" to judgment, with the stamp-only path always available. **No step compares the brief against the spec it summarises** (`[[finding_freshness_check_cannot_catch_a_fresh_lie]]` — the stamp is a freshness check; the failure was agreement).
**Class:** (b) — the fix is a positive accuracy check, not a wording tweak.

---

## 🟡 LOW / STRUCTURAL

### C7 — `LESSONS.md` lesson numbering is OUT OF ORDER (17 → 19 → … → 18)
Heading order by line: …16 (37), 17 (38), **19 (39)**, then **18 at line 54**, 20 (56), 21 (58). **L19's prose at line 39 cites *"cleared the #18 rhetorical bar"* — forward-referencing a lesson that appears 15 lines later.**
> ⚠️ **CORRECTION MADE MID-AUDIT: I first recorded this as "LESSON 18 IS MISSING."** A sequential scan showed 17→19 and I nearly filed a missing-lesson flag. **L18 exists; it is out of position.** Caught only by grepping for the heading rather than trusting the scan. **Same class as this morning's F9/F10 — and the third time today.**
**Class:** (a) cosmetic.

### C8 — the Apr-17 STNG figure exists in **THREE different values** across my own surfaces
| Surface | Value |
|---|---|
| `TRADE.md` analogue table | **+3.9%** |
| `LESSONS.md:54` L18 prose | **+3.4%** |
| Re-derived from price data 7/31 | **+1.61%** |

**Three surfaces, three numbers, one datum.** This is the unreproducible-tanker-figure problem from this morning — **now shown to be broader than the TRADE.md table I flagged.** The `+3.4%` in LESSONS predates the `+3.9%` in TRADE, so the figure drifted *between my own documents* before either was checked against source.
**Class:** (a) — but **do not "fix" by picking one: the re-derived +1.61% is the only one with a reproducible source**, and per this morning's ruling the retired analogue tally must not be re-cited either way.

### C9 — step 7a's scheduled-grade check names only TWO series
`CLAUDE.md:56-62` covers **CFTC COT** and **Baker Hughes**. It does not name **EIA WPSR** (weekly, my most-cited release) or **OPEC+ meetings**. Both are in `CATALYSTS.tsv` and both have produced grading obligations this month. Not wrong — **incomplete**, and the step's own rationale (*"nothing durable told a fresh session to run the grader"*) applies identically to the omitted series.
**Class:** (a).

### C10 — step 10 forward-state targets are current; **no flag** (verified, not assumed)
`demand_destruction/TRACKER.md` 7/29 · `refinery_damage/INCIDENTS.tsv` 7/30 · `docket/CATALYSTS.tsv` 7/31. All maintained inside a reasonable window. **All step-10 and step-8/11/12/13a write-targets verified to EXIST** (11/11: SCRATCH template, TRACKER, INCIDENTS, PREDICTIONS_ARCHIVE, CHANGELOG, FASTOW ×2, MEMORY, `outbox/delivered`, `inbox/processed`, `cot_grade.py`). **No dead pointers besides the frozen-file class in C3.**

### C11 — never-edit-a-consumer check: **CLEAN**
Swept every closeout write-target. The only cross-agent writes my closeout authorises are **(i)** packets into another agent's `inbox/` (Outbox Protocol — **carve-out ①**, and the delivery-path table correctly flags `PROME/inbox/` as the exception) and **(ii)** appending a self-authored row to `AGENTS/SIGNALS.md` (**carve-out ②**). **No step writes to another agent's STATUS, ledger, or domain file.** Step 10's *"military ops/intercepts → HAWK"* is routing language, not a write. ✅

---

## SUGGESTED ORDER (disposition round — **nothing applied**)

1. **C1** — a boot-read surface asserting a rule Will retired today. Highest live cost; (a)-fixable immediately.
2. **C3** — three frozen write-targets in the primary clause of step 8; same class I fixed this morning.
3. **C2 / C6** — the two structural gaps that *cause* the C1 and F1 rot. Need rulings.
4. **C4** — root-canon steps absent; note the live `consumer_check` miss is fixable by simply running it.
5. **C5** (REFERENCE_TABLES/MEMORY asymmetries), **C7, C8, C9** — mechanical.

**No thresholds moved. No edits applied. F3/F4 from round 1 remain unruled and untouched.**

*BRENT · 2026-07-31 12:2x EDT*
