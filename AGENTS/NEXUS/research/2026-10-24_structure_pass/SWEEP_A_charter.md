# SWEEP A — NEXUS charter defect ledger

Target: `/home/willi/Research-workspace/AGENTS/NEXUS/CLAUDE.md`, 71,849 B, 365 lines, last commit 4da79f1ee (2026-10-23 10:48 ET). Read whole. Reviewer was read-only; nothing in the repo was edited. Run 2026-10-24 (Sat).
Basis: `ls` existence checks from repo root; `read_cap_check.py --agent NEXUS` (rc=0); `PROME/registry/READS.tsv` L322–357; `PROME/DOCKET.tsv` physical lines 553/554/555; brief census by `ls AGENTS/*/NEXUS_BRIEF.md` = 29.

## 1. Path check

I checked 66 cited paths. All but four exist. All 30 `[[memory]]` slugs resolve under `memory/auto/`. The four "dead" ones:

| Cited path | State | Verdict |
|---|---|---|
| `AGENTS/PROME/` | absent | CORRECT. The charter says it must not exist. |
| `memory/MEMORY.md` | absent | Labelled as a corrected path (step 14); the live pointer `memory/auto/MEMORY.md` exists. OK. |
| `AGENTS/NEXUS/workbook/LEDGER_GLOB` | absent | Consistent with step 16 "1c-bis n/a (no LEDGER_GLOB)". OK. |
| `USER.md` (Helper-model selection) | `AGENTS/NEXUS/USER.md` absent; root `USER.md` exists | ⚠️ F-01: the bare relative path resolves wrong from the launch dir. |

**Net: zero dead pointers that would actually break anything; one ambiguous path.**

## 2. Ledger

| # | Sev | Section · quote | Problem | Fix |
|---|---|---|---|---|
| F-01 | ⚠️ | SPAWN PROTOCOL · "Apply `USER.md`'s OpenAI Sol preference within its stated scope" | The charter's convention is paths relative to `AGENTS/NEXUS/`, but there is no `AGENTS/NEXUS/USER.md`; the file is at the repo root. The preference it points to (root USER.md L92) is scoped to "agents spawned by PROME", so whether it applies to NEXUS-spawned readers is undecided. | Write `/USER.md` (repo root) and state yes/no on whether NEXUS-spawned readers are in scope. |
| F-02 | ❌ | CLOSEOUT TIERS · "HEAVY — … Standard + **9a if its dated row is due**" vs 9a "DOCKET L555 = 2026-10-27 … rides the DOCKET L554 Tuesday wake" + WHEN TO RUN 5 "A Tuesday wake with nothing moved is a SHORT boot" | 9a sits in HEAVY only. Its due date (L555, 10/27) falls on a Tuesday wake (L554, also 10/27; Tue verified), and that wake is a SHORT boot ending in a Light or Standard tail. Read literally, the tier table skips the step the docket row exists to force. This is the "undated step loses" failure that fix D5 was meant to close. | Move 9a out of the tier lists into a date trigger: "9a runs at any tier when DOCKET L555 is due." Or list it under STANDARD as "9a if its dated row is due". |
| F-03 | ❌ | CLOSEOUT 15b · "Every dated NEXUS obligation gets a DOCKET wake row" | 15b appears in none of the three tier lists, and the tier header says every step not run goes on the `skipped:` line. So a Standard pass that registers a new L-row has no tier step telling it to packet PROME, and no `skipped:` line would show it. The wake row is lost silently. | Add "15b if a dated letter was registered or re-dated" to STANDARD. Also add it to BOOT 0b's "every NEW letter" clause. |
| F-04 | ❌ | READS.tsv L352–356 (manifest) · "Root session-end 1b-1e run inside step 16 **at Standard+ (D8)**" vs charter step 16 "at EVERY session-END commit whatever its tier (… tier scope struck 10/1, cold-read-2 ❌28)" | The manifest carries the tier scope the charter struck on 10/1. The manifest was attested 9/29 at 62,587 B; the charter is now 71,849 B (+9.3 KB, edits 10/1 · 10/8 · 10/19 · 10/23) and has not been re-attested. | Packet PROME with a re-attestation covering F-04 to F-07 (the manifest is PROME-transcribed; NEXUS must not edit it). |
| F-05 | ⚠️ | BOOT 6 · "Readers also run the pin check — `python3 scripts/brief_pin_check.py`" (added 10/8) | Not declared in READS.tsv. Boot reads the charter requires but the manifest lacks: `scripts/brief_pin_check.py` (BOOT 6), `scripts/read_cap_check.py` at step 15 (named 10/8), root `USER.md` + `PROME/ORCHESTRATION_PLAYBOOK.md` §Runtime mechanics (Helper-model selection, every spawn). | Include them in the F-04 re-attestation. |
| F-06 | ⚠️ | READS.tsv L331 · "`AGENTS/NEXUS/analysis/*.md` scoped NEXUS:0b — the letter section(s) of any page carrying a registered NEXUS letter" | The manifest declares a BOOT 0b read the charter never asks for. BOOT 0b lists PREDICTIONS_MONITOR rows, matrix forcing conditions and GATES rows, and no analysis pages. `analysis/` is also missing from WHAT YOU OWN. Separately, READS L351 says analysis pages "are capped at 6 KB". The one member, `analysis/2026-09-29_one-root-or-many.md`, is 21,537 B. | Add "letters registered on `analysis/` pages" to BOOT 0b's enumeration, and add `analysis/` to WHAT YOU OWN. Ask PROME to strike the 6 KB claim, or state that companion pages are uncapped. |
| F-07 | ⚠️ | READS.tsv L335 · "THREE fresh-context **Opus** digest readers … Census by `ls`, currently 27" | Live census is 29. The model is now chosen under "Helper-model selection", not fixed at Opus. | Include in the re-attestation. |
| F-08 | ⚠️ | WHAT YOU READ · "brief-less desks (WALTER, OZK) when live" vs BOOT 6 "**Membership is never listed here** (cold-read-2 ❌14/❌16)" | The same file lists membership while forbidding it. The pair is true today (neither desk has a brief, both verified), but it will rot the way the "24→25" count did. | Replace with "brief-less desks (census → `BRIEFS_MAP.md`)". |
| F-09 | ⚠️ | CLOSEOUT 9 · "overflow rotates verbatim to `STATUS_COLD.md` §H" vs OUTPUT RULES · "Max 200 lines in STATUS.md. Archive older synthesis reports to `research/`" | Two different destinations for STATUS overflow. | Keep the step-9 destination. Change OUTPUT RULES to "Overflow → `STATUS_COLD.md` §H (CLOSEOUT 9); long-form reports → `research/`". |
| F-10 | ⚠️ | WHAT YOU OWN table | `STATUS_COLD.md` is missing, although BOOT 0a and CLOSEOUT 9 both rotate into it. Also unlisted: `analysis/`, `proposals/`, `registry/` (7a writes `registry/corrections_receipts.tsv`), `board_log.tsv`, `brief_fallback_log.tsv`, `brief_health.md`, `BRIEFING_2026-08-29_SYSTEMS_REVIEW.md`. | Add one row per surface with its purpose, or one "other owned files" row. |
| F-11 | ⚠️ | BOOT 0a · "to its cold companion (`STATUS_COLD.md` §H · `PREDICTIONS_COLD.md` §P · `archive/`)" | The rotation rule covers "any owned surface" but names companions for only two. A session rotating `BRIEFS_MAP.md` (64%) or `CONFIRMED.md` has to guess. Step 15 names a third (`archive/LAST_COMPLETION_COLD_<date>.md`) somewhere else. | Add a one-line map: surface → cold home, for every surface in the READ_CAP perimeter. |
| F-12 | ⚠️ | BOOT 6 · "**Consult `BRIEFS_MAP.md` first**" and later "**Multi-day re-anchor — do this FIRST**" | Two "first" instructions in one step. "Multi-day" has no threshold (the charter's own examples are 8 and 11 days; is 2 days multi-day?). | Order them: (1) freshness scan if more than N days (pick N, e.g. ≥2 calendar days since the last `LAST_COMPLETION` block), (2) BRIEFS_MAP, (3) digest readers. |
| F-13 | ⚠️ | BOOT 4 · "**Scan `inbox/`** — directory of dated routed-signal files" | "Scan" is the verb this charter retired in BOOT 3 for being ambiguous (READS declares inbox packets "whole"). BOOT 4 also gives no `board_log.tsv` `source` token for non-WALTER packets, though Signal lifecycle requires a row for every incoming item. Processed packets move at CLOSEOUT 11, while READS L332 says they are `git mv`'d at boot. | "Read each top-level `inbox/*.md` whole; log one `board_log.tsv` row (`source=INBOX`); move at CLOSEOUT 11." |
| F-14 | ⚠️ | BOOT 7 · "Spec: … (**v0.32 at 9/29 — read the version from its header, never from here**)" | The spec header reads **v0.35**. A version string that tells you not to trust it is pure residue. | Drop "v0.32 at 9/29". |
| F-15 | ⚠️ | CLOSEOUT 9a · "**DOCKET L555 = 2026-10-27**" | This is stated as a current fact, and it expires in 3 days. After the rollup, PROME re-dates or appends a row, and this sentence goes stale. The Tuesday-wake text, by contrast, correctly says "PROME re-dates the one row". | "every 4 weeks on its DOCKET row (DOCKET L555 as of 9/29; the date lives in the row)". |
| F-16 | ⚠️ | 9c + Δ-column · "the header's 'Last full matrix review: `<date>`'" | The live STATUS header has no such label. It writes `**Updated:** … — **FULL MATRIX REVIEW (…)**`. A grep or a reader keyed on the charter's label finds nothing. | Pick one label and use it in both files. |
| F-17 | ⚠️ | Framework 1 · "**ROOT count … RULED by Will 2026-10-01 … settling read-3 ⚠️51/⚠️52**" | The review-labels preamble gives pointers for read 1 and read 2 only. "read-3" has no pointer (the likely source is `inbox/processed/2026-10-01_from-PROME_review-of-nexus-4f-commits-…`). There are 34 ❌/⚠️ labels in the file; the unqualified ones resolve to read 1 (verified, e.g. ⚠️90, ❌88). | Add the read-3 pointer to the preamble, or drop the labels (see F-24). |
| F-18 | ⚠️ | Framework 1 · "5+ roots: Critical (immediate alert, **propose action**)" | Conflicts with "You do NOT own … Trading decisions (a TERRY card …)" and root rule #5. Disc-F also says the fleet typically has only "~4-5 break-relevant" live roots, so Critical means every live root at once. That is fine, but it should be said. | "propose that PROME commission a TERRY card"; add a note that 5 roots ≈ the whole live root set. |
| F-19 | ⚠️ | LIVE-EVENT OVERRIDE · "run **0a · 0b · 1 · 7 · 7a** and short-circuit BOOT steps 2–6" vs WHEN TO RUN 4 "fired … in last 24h" | 0b enumerates `PREDICTIONS_MONITOR.md` rows, which in effect is the BOOT 3 read the override "skips". The override window ("firing during boot") and trigger 4's window (past 24h) also differ, so it is unclear which applies to a print from 6 hours ago. | Say whether 3 is skipped or folded into 0b. Make one window govern. |
| F-20 | ⚠️ | CLOSEOUT TIERS · LIGHT "residue grep if any claim or figure was superseded" vs STANDARD "**EVERY correction commit** (fix D3: a correction is never Light)" | A superseded claim or figure is a correction, so a Light tail running the residue grep is by definition not Light. The LIGHT clause cannot apply without breaking D3. | Make supersession promote to STANDARD; delete the clause from LIGHT. |
| F-21 | ⚠️ | WHEN TO RUN 5 · "the wake runs on the WQ-184 driver — PROME `ListAgents` first" | A tool name that depends on the runtime. Root canon says "do not infer tool availability from the model name" and to select mechanics from the PLAYBOOK. It is PROME's procedure and has no business in NEXUS's charter. | "PROME wakes NEXUS per `PROME/ORCHESTRATION_PLAYBOOK.md`." |
| F-22 | ⚠️ | READS L324 · charter "explicitly read on a PROME spawn (L399)" | At 71,849 B (about 33k tokens at 2.17 B/token) the charter is over the 54,250 B single-Read cap. READ_CAP rule 20 exempts harness injection only. An explicit `Read` on the PROME-spawn path (the `desk` agent preamble) will truncate or refuse, so the spawn boots on part of its charter. `read_cap_check` itself says "explicit-read runtime coverage NOT assessed". | Shrink below 54 KB (see F-24), or have the preamble read the charter in two offsets. Packet DAEDALUS/PROME about the rule-20 gap. |
| F-23 | 💡 | Disc-E · "Single Polymarket/Kalshi prints are not 'holds'" | Will ruled on 9/29 that priced odds are ORACLE's domain (memory `feedback_prediction_market_data_is_oracles_domain`). The discipline never names ORACLE. | Add "cite ORACLE's dated read; never pull a print directly". |
| F-24 | 💡 | Whole file — bloat (see §3) | About 30–35% of the bytes are history. 34 cold-read labels, 30 memory tags and dated incident paragraphs push the executable rules apart. Root says "Rules only". | Move the history to `AGENTS/NEXUS/docs/CHARTER_PROVENANCE.md` (one row per rule: adopted date · incident · ledger pointer). Keep one trailing tag per rule. |
| F-25 | 💡 | CLOSEOUT 16 · "**Never commit files outside `AGENTS/NEXUS/` EXCEPT under the root carve-outs** … ① … ③" | Omits ② (shared-log rows; harmless today because SIGNALS.md is frozen) and ④ (Gate C submissions). Fine as long as NEXUS never needs them, but the text implies the list is complete. | "① and ③ are the carve-outs NEXUS uses; ② and ④ per root". |
| F-26 | 💡 | SPAWN PROTOCOL · "The October 19 task's one-time **gpt-6.1-sol** override … it is not standing" | A non-standing override in a rule section is history by definition. | Delete; the RECORD.md keeps it. |
| F-27 | 💡 | CLOSEOUT 16 · "a bare 'step 5' is ambiguous here because NEXUS's own step 5 is BOOT/`SIGNALS.md`" | BOOT 5 is RETIRED. The warning still describes it as live, a struck-through step whose consumer stays live (harmless, but it is the pattern). | "(NEXUS BOOT 5 is retired; the root list is meant)". |

### Retired/frozen-step consumer check (task item 2)
- BOOT 5 / SIGNALS.md: its consumers are LIVE-EVENT "2–6", Disc-G "BOOT steps 4-7", step-16 note (F-27), READS L333. All are harmless ranges or labelled. **None mis-executes.**
- CLOSEOUT 12/13 (outbox, signals_archive): no step consumes them. The WHAT YOU OWN rows are bannered RETIRED. **Clean.**
- The real live-consumer defects are structural rather than retired steps: F-02 (9a stranded by the tier table), F-03 (15b in no tier), F-04 (manifest still runs a struck tier scope).

### Numbers / dates verified true today (no finding)
- Amendment cap "12 of 12" matches the schema header.
- DOCKET L553 is PRED-50, L554 is the Tuesday wake (2026-10-27, Tue), L555 is rollup #6.
- Disciplines A–J are ten, and the EXECUTE 8 roster matches.
- `_NETWORK.md` Credit row matches Framework 3.
- coldreader agent is `model: sonnet`, consistent with WQ-447.
- STATUS is 118 lines and 22,779 B (70% of budget, under the 75% trigger).
- LAST_COMPLETION is 16,470 B (51%).

## 3. Bloat grade (task item 5)

| Class | Measured B | Method |
|---|---|---|
| Italic asides (*Why:…*, *(added …)*) | 5,244 | regex, 42 segments |
| Provenance parentheticals ("(adopted/added/corrected … )") | 2,551 | regex, 24 |
| "Cost, measured / Why it exists / Live instance" bullets | 2,541 | regex, 6 |
| `[[memory]]` tags | 1,359 | regex, 30 |
| **Mechanically identified history** | **≈11.7 KB (16%)** | lower bound; overlaps possible |
| Reading estimate, including inline dated narrative (9c cost paragraph, C-05 story in WHAT YOU OWN, PATHS box, Disc-G/I/J cost bullets, 16's live instance, BRENT instrumentation provenance ×2, 34 ❌/⚠️ labels) | **≈22–26 KB (30–35%)** | judgment |
| **Executable rule text** | **≈46–50 KB** | remainder |

Grade against "Rules only; reasons live elsewhere": **D**. Rules are present and mostly correct, but about a third of the file is incident narrative. That narrative alone puts the charter over the explicit-Read cap (F-22). Moving it out would bring the file to about 48 KB without changing any executable rule.

## 4. Counts

❌ 3 · ⚠️ 19 · 💡 5  (F-02, F-03, F-04 are ❌; F-22 is borderline ❌ on the PROME-spawn path)

## 5. Verdict
- **Works:** paths resolve (zero real dead pointers), the A–J disciplines and the BOOT sequence are complete and match the canon they cite, and the guards (9b residue grep, 16 post-push verify, stamp rule) are concrete and runnable.
- **Does not:** the tier table no longer matches the dated and event-triggered steps (9a stranded on its own due date, 15b in no tier); the READS manifest is 9.3 KB / four edit rounds behind the charter; and the file is too large to be explicitly Read whole on the PROME-spawn path.
- **Single most valuable change:** move the ~25 KB of provenance to a companion file, and in the same commit rebuild the tier table so dated and trigger steps (9a, 15b) run "at any tier when due". That fixes F-02, F-03, F-22 and F-24 together. Then packet PROME a READS re-attestation.
