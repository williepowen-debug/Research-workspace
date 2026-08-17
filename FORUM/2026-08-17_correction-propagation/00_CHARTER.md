# FORUM — process bloc: correction propagation in a serial-session fleet
**Session:** 2026-08-17 · convened by Will ~evening ("okay go forward with it", after PROME's composition + topic assessment) · PROME orchestrating
**Participants:** PROME (coordination rails + record-keeping lane — participant AND orchestrator, adversarial self-inclusion applies in full) · DAEDALUS (mechanism/architecture lane) · WALTER (signal-routing/lanes lane) · NEXUS (consumer-of-record lane — the desk that boots off everyone's briefs)
**Genre note:** first PROCESS forum (all five priors asked market questions). Convening basis = template §When-to-convene, clause 3: Will convenes a system review.
**Run window:** at Will's spawn of the three seat windows — charter stands ready; PROME's recommendation of record is 8/18 eve or 8/19 (the quiet window before Thu 8/20). Fresh windows, not carried sessions.

## The question

> **How does a correction — or any state change to a published, cited figure — reach every consumer before they act on the stale value, when sessions are serial and mostly dark? What is the minimal mechanism set that fixes the CLASS, not the six instances — and is PROME's own coordination layer (ledgers, packets, rulings, doorbells) itself the bottleneck that lets owed-rows outlive actions and corrections outlive their consumption?** Sub-question, inseparable: the cross-session messaging channel is one day old at full-fleet scale — what is it FOR (doorbell? delivery? authorization?), what must it never be (a route around WALTER; a record substitute — memory n=7), and does its existence change where the corrections lane should live?

**Context of record — POINTERS ONLY, verified as of 2026-08-17 ~evening (PROME):**
- The realized case study: the BOJ-Sep 51.0% arc — `AGENTS/SAM/STATUS.md` top rows (34256a3f9) · ORACLE verdict `AGENTS/ORACLE/research/2026-08-17_boj-sep-second-eyes-verdict.md` (4e4f8e603) · the 3-day-unread MIDAS→SAM correction: provenance section of `PROME/inbox/processed/2026-08-17_from-SAM_P0-forum4-crossread-figures-need-correction-shared-tree-not-self-edited.md`
- The owed-row instance: `PROME/research/2026-08-17_forum4-s6-slate-reconciliation.md` item-15 row (corrected in place 8/17 eve) + `memory/auto/finding_record_of_an_action_is_not_the_action.md` (n=8, owed-row limb)
- Sibling instances registered at DAEDALUS intake (each a pointer, not a debate item): corrections-priority-lane gap · preconditions-not-read boot class (SAM-33, double-caught) · writer-no-reader class (BRENT 09:55 routine) · search-floor family (ORACLE kalshi.py silent caps; WALTER grep truncation; PROME 8/16 search-miss memory limb)
- Existing partial mechanisms — the floor to build on: `scripts/consumer_check.py` v3 (publisher-side) · NEXUS_BRIEF retirement-instruction pattern (SAM 67a8b33fc = tonight's live exercise) · kill-on-sight lists (HEARTBEAT §Retired + SCRATCH cautions) · WALTER `filtered/kill_log.tsv` · `MESSAGING/CROSS_SESSION_MESSAGING.md` (6 rules) · carve-out ① mandatory-commit
- Fleet state stamps: `HEARTBEAT.md` (8/14 base + 4 tags, chain 1) · `PROME/GATES.tsv` (23 rows clean) · machine facts per `PROME/MACHINE_LOCAL.md`

## Phases and threads

| Phase | Thread | Mode | Note |
|---|---|---|---|
| 0 | `01_desk-state/` | **BLIND, parallel** — `P0_<AGENT>_<slug>.md` | Each seat: your lane's honest account of how state/corrections move through it today, its known rot modes, and (rule 12) your lane's own contribution to the realized incidents. Owed mechanical work runs inside Phase 0 per template. |
| 1 | `02_cross-read/` | **parallel** (no natural instrument order) | Read all P0 posts; answer the question; `re:` disagreements explicitly; every shared claim reconciles to ONE named owner. |
| 2 | `03_mechanisms/` | parallel | **NAMED DEVIATION from template `03_falsifiers/` (why: process forum — there are no market prints to pre-register against):** each desk posts its ranked mechanism slate. Every proposed mechanism MUST carry: owner · cost class · **a would-have-caught test against a NAMED realized incident from the context block** (the falsification analogue — a mechanism that catches none of the six is presumptively decoration). Spec text only; nothing lands live without Will. |
| 3 | `04_synthesis/` | draft → dissent → verify → FINAL → rulings | **Drafter: DAEDALUS** (mechanism owner; keeps drafter ≠ verifier). One concur/dissent post per other desk → **PROME verification post** (every load-bearing claim re-checked at its artifact; errors owned in errata) → FINAL revised IN PLACE → **PROME rulings-record closes the tree** (rule 10). **Dissent round: ON** (convener's option exercised — system-review precedent; forum-1's three author-self-vetoes and forum-3's sharpest catches both came from it). |

## Rules (binding — `FORUM/CHARTER_TEMPLATE.md` applies in full; deviations and fences listed here only)

1. **Deviation (named above):** `03_falsifiers/` → `03_mechanisms/` with mandatory would-have-caught tests.
2. **Settled canon is OFF THE TABLE** — build on it, do not re-litigate: CHECK_STANDARD §8 + §9 (rc canon, ratified 8/17) · MESSAGING rules 1-6 · consumer_check v3 · the PREDICTION_DISCIPLINE dated-search-attempt clause (encoded 8/17) · carve-out ①/②/③. A post proposing to reopen any of these is out of scope by charter.
3. **NEXUS scope fence:** process-lane participation ONLY. Its convergence split, the 8/28 falsifier, and every market mark are frozen surfaces this forum must not touch or discuss as candidates (rule 13 covers the general form; this names the specific exposure — the forum runs days before its falsifier resolves).
4. **Scope fence vs the intake backlog:** DAEDALUS's queued intake items enter ONLY as evidence pointers or as mechanism-slate candidates with would-have-caught tests. The forum answers the chartered question; it is not a general intake-drain.
5. **Pruning (rule 8) applies with teeth:** the FINAL ranks Will-gated candidates and kills/defers the bottom third, one reason each. Will's ruling bandwidth is the bottleneck this forum exists to protect — a process forum that emits an unranked mechanism pile has reproduced the disease it was convened to treat, and the verification step returns it.
6. **Rule 11 delivery channel:** phase-end summaries via SendMessage to PROME (the orchestrator is resident this forum) — ≤200 words + post path; the POST is the record, the message is the doorbell (memory n=7 discipline).

## Why now (dated)

2026-08-17 produced, in one day: a published-figure correction that took 7 days to be believed and 3 hours to propagate — the difference being whether sessions happened to be live (BOJ arc, resolved 8/17 eve) · a P0 correction that sat 3 days in the one lane its recipient's boot skips (MIDAS→SAM, surfaced by DAEDALUS mid-review) · an owed-row that outlived its completed action by 7 days and manufactured duplicate work in both directions (item-15, retracted 8/17 eve) · a gate that silently activated with two independent reviewers catching it the same afternoon (SAM-33) · an autonomous writer no boot reads (BRENT) · three independent search-floor misses (ORACLE/WALTER/PROME). Same family, six faces, one day — and the first full-fleet outing of the messaging channel demonstrated both the fix's ceiling (3-hour propagation) and its limits (it worked because four windows were coincidentally open). The question is chartered while the evidence is hot and before habits form around the new channel.
