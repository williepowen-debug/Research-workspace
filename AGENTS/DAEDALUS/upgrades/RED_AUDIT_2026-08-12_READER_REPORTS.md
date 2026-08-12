# RED audit 2026-08-12 — READER DELIVERABLES (raw evidence store)

**Why this file exists:** Will asked "did we properly save the results of the three sub-agents?" and the answer was **no**. The audit's *conclusions* went into `RED_AUDIT_2026-08-12.md`, `profiles/RED.md`, `PATTERNS.tsv` (PAT-096..099) and four routed packets — but the readers' **raw tables and their coverage caveats existed only in the session transcript**, which dies with the session. That is PAT-093 (a baseline whose derivation lives only in a scratchpad cannot be re-measured by a second reader) firing on my own work for the third time, and the same fix as the 8/11 `DARK_CENSUS` persist. **File > verbal is my #1 rule; this is the file.**

**Provenance:** 3 readers (`red-spine` / `red-workbook` / `red-comms`), Mode-A fan-out, read-only, RED LIVE throughout. Six deliverables total (each reader: one audit round + one Task A profile slice + one Task B follow-on). Read vintage `4b3bb1b55` (S29c 12:16 ET), spine reader re-stamped to `0940549e7` (S29d 13:22). **All three idled holding; all three delivered complete on one chase.**

---

## WHERE EACH DELIVERABLE LANDED (pointer map — check here before re-tasking a reader)

| Deliverable | Durable home |
|---|---|
| Audit round ×3 (18 findings) | `upgrades/RED_AUDIT_2026-08-12.md` — consolidated + deduped, full evidence |
| Task A slices ×3 (anatomy / spine / lanes) | `profiles/RED.md` §2, §2b, §3b, §4, §5 — synthesized, superseding the 7/4 profile |
| Task B: registry generalization | **§1 below** (full) + `AGENTS/WALTER/inbox/processed/2026-08-12_from-DAEDALUS_autofire-array-audit-6c-has-no-executable.md` (routed form) |
| Task B: 71.5 fleet trace | **§2 below** (full) + PROME packet items 3-4 + PAT-099 |
| Task B: prune sweep (11 agents) | **§3 below** (full) — superseded in SCOPE by PROME's 23-agent sweep, retained for the 4 analyses PROME's does not carry |
| Coverage caveats (all six) | **§4 below** — the honest-coverage metadata, nowhere else |

---

## §1 — Registry generalization (red-workbook Task B): R7 is NOT RED-local

**The array, measured:** WALTER `CLAUDE.md:60-64` step 6b builds it, 6c evaluates every boot, auto-dispatch IMMEDIATE on sustained crossing. **18 conditions / 17 registered / 16 distinct.**

| Source | Owner | Rows | Cols |
|---|---|---|---|
| `RED/registry/FALSIFICATION_TRIGGERS.tsv` | RED | 9 (RED-FT-01..09) | 12 |
| `REGINALD/registry/THRESHOLDS.tsv` | REGINALD | 8 (REG-T-01..08) | 8 |
| Cushing <20M single print | **nobody** | 1 | in no registry — `WALTER/ROUTING_TABLE.md:446` Boundary #3 prose |

**Per-registry grade on the three machine-layer questions:**

| Registry | (a) Instrument/basis | (b) State ARMED/FIRED | (c) Half-registrations |
|---|---|---|---|
| **RED-FT** (9) | No column. Prose only, only on rows registered 8/12: FT-06 (`FRED VIXCLS`), FT-08 (`all items less food and energy, SA`), FT-09 (`FRED T5YIFR`) = **3 of 9**. Absent: FT-01/02/03/04/05/07 incl. **both `BRENT-PAPER` rows** | No column. Prose mid-narrative in `exit_source`: FT-01 `RE-FIRED 2026-08-07`, FT-06 `FIRED 2026-08-12` | **FT-08**: machine cols `CORE-CPI-MOM / >= / 0.4 / s=1` = one leg; prose = both legs + "a single 0.4 inside a 1.6% 3-month run is noise" *(CORRECTED S29d)* |
| **REG-T** (8) | **No column AND zero prose** — `FRED\|yf\|source\|settle\|series\|instrument` = **0 hits file-wide**. REG-T-01 `KRE-PRICE <60` / REG-T-02 `WAL-PRICE <78` no close-vs-intraday; REG-T-05 `INITIAL-CLAIMS >300` no SA/NSA; REG-T-08 `SOFR-IORB >15` no unit. Exception: REG-T-07 `OFFICE-CMBS-DQ-TREPP` (provider in the metric NAME, 7/30 fix `fc59d7973`) | No column, no prose | **All 8 structurally** — schema has **no `exit_*` columns at all**; zero un-fire conditions on REGINALD's entire auto-fire surface |
| **Cushing** | Prose only | None | n/a — IMMEDIATE dispatch, no registry row |

**The state side-channel exists and is wrong.** `WALTER/registry/FALSIFICATION_FIRED_LOG.tsv` (3 rows) + `REG_THRESHOLDS_FIRED_LOG.tsv` (1 row), 5-col (`trigger_id/fired_date/metric_value_at_fire/dispatched_signal_id/sustain_confirmation`) — **fire-only, no un-fire row type.** Contents: RED-FT-01 fired 6/04 @275 · RED-FT-07 fired 6/04 @947 · RED-FT-06 fired 8/11 @15.28 ✓ · REG-T-02 fired 5/11 @76.95 (**last write, 3 months**). **DEFECT: two events behind on FT-01** — RED's registry records UN-FIRED 7/31 (+2 executed) and RE-FIRED 8/07 (−2 executed); neither is logged, so a machine reads FT-01 as continuously fired since 6/4 across a cycle where weight moved twice.

**Root cause, verified not inferred:**
- `grep -rno "exit_op|exit_threshold|exit_sustain|exit_source" AGENTS/WALTER/` → **5 hits, all narrative** (3 in `STATUS.md:7`, 1 `REGISTRY.tsv:7`, 1 in an 8/03 sweep row). **Zero in any spec, checklist, or tool.**
- No WALTER tool reads either registry (`batch_manifest`/`intake_scan`/`phone_scan`/`reconcile_delivery_log`/`staleness_sweep`/`version_drift_check`/`walter_doctor`). **Step 6b/6c is a human read-loop, not code.**
- `grep -i "un-fire|unfire|re-arm|rearm"` across `SIGNAL_PROCESSING_CHECKLIST.md` + `WALTER/CLAUDE.md` → **no hits**.
- RED's `scripts/boot.py:144` reads the registry to print rows; does not touch `exit_*`.
- **Stale contract on BOTH sides:** RED `workbook/SCHEMA.tsv` says 8 cols for a 12-col file; `WALTER/design/CROSS_REFS/RED.md:25` says "(8-col)"; `WALTER/CLAUDE.md:204` says "8-col schema".

**D4 · duplicate condition:** `RED-FT-02` = `REG-T-03` = `HY-OAS >320 sustain 3`, identical op/value/sustain, different action + chain (PATH-B-CONFIRM vs CREDIT-CANARY-FIRED). One HY crossing fires two rows; WALTER's existing HY double-dispatch guard (`CLAUDE.md:70`) covers the ≥280 lane-vs-dashboard case, not this.

**Verdict:** *"RED is the strongest component of this surface, not the weakest."* Basis 3/17 · state 0/17 in-registry · 1 explicit + 8 structural half-registrations. **Generalization one layer above PAT-071: a registry consumed by a human read-loop rather than code accumulates columns nobody parses and prose nobody can evaluate — RED's good-faith additions improved the DOCUMENT, not the SURFACE.**

**DAEDALUS addendum (verified 8/12, post-report):** REG-T's `threshold_thesis_ref` column is **8-for-8 dangling** — every row points at `STATUS.md#<anchor>`, zero resolve literally, and no heading in `REGINALD/STATUS.md` generates any of those slugs (its headings: SIGNAL DASHBOARD / CROSS-AGENT TRIGGERS / THRESHOLD STATUS / EXIT RULES). Content is present (20 KRE/HY/claims mentions), the pointers are dead. This **resolves the reader's own flagged caveat** ("REG-T's exits might live in REGINALD's prose") in the direction that strengthens the claim.

---

## §2 — Fed-hike 71.5% fleet trace (red-spine Task B)

**HEADLINE: ZERO confirmed live stale carriers. Both were fixed while the audit ran.**

| Carrier | Status | When |
|---|---|---|
| RED | ✅ FIXED — Policy Rescue 2→4; `STATUS.md:58/:158` carry 54.5% | S29d `0940549e7` 13:22 |
| LABOR | ✅ **RETIRED, not refreshed** — `STATUS.md:120`, reasoning *"LABOR should never have held a copy… Cite ORACLE directly, never LABOR"*; also traced+retired an unrelated unverified `Sept-hike >80%` | ORACLE packet consumed |

**Classification of 63 raw `71.5` hits fleet-wide — the bare-string match is overwhelmingly noise, which is itself the reportable result:**

| Class | n | Examples |
|---|---|---|
| **DIFFERENT SERIES** | ~50 | BRENT STNG stop-loss **$71.50** (14) · OZK/REGINALD true-CRE 71.5% (5) · WAL loan-to-deposit 71.5% (7) · BROCK/APO GAAP assets +$71.5B (2) · MARCO Nuevo León migration 71.5x · REGINALD FL suits 71.59% · ORACLE `ODDS_LOG` row-id fragment |
| **HISTORICAL-DATED-RECORD** (correct, do not touch) | ~11 | ORACLE `KB.tsv:50/53/59/69` + 5 dated outbox packets (7/24, 7/31) · RED `outbox/2026-07-24`, `research/FOMC_FRAMEWORK:74`, `LAST_COMPLETION.md:4`, `ML.tsv:108` · CARL `KB-CARL-363` |
| **CORRECTION-BEARING** (says the right thing) | 4 | ORACLE `NEXUS_BRIEF.md:8` · `STATUS.md:12/16` · LABOR `STATUS.md:120` |
| **SAME-SERIES-STALE** | **0** | — |

**C1 · LABOR `workbook/PUBLISHED.tsv:49` — retirement in the notes column, machine columns still publish.** Row: `fed_hike_2026_odds | 71.5% | asof 2026-08-12T18:50Z | number | greppable=yes`, notes carry the full correction + attribution + a *"GUARD THAT MUST TRAVEL: this is NOT a dovish flip"* caveat. `consumer_check.py --from-ledger` reads value/asof → **a machine sees LABOR publishing 71.5% as of today.** → folded into PAT-098 (n=5).

**C2 · The number names two different instruments (CANDIDATE — ORACLE rules).** ORACLE (publisher) = **Fed-hike-2026 aggregate**, Polymarket `fed-rate-hike-in-2026`, 71.5% @ 2026-07-24T16:01Z. But `NEXUS/PREDICTIONS_MONITOR.md:154`, `RED/thesis/CHANGELOG.md:75`, `RED/LAST_COMPLETION.md:4` all read **"Sept odds 71.5→77%"**. ORACLE's 8/12 packet puts Sept-specific at 33.5% today from a 7/31 intraday high of 56.5% — not obviously reconcilable with 71.5→77% on 7/29. **Exactly the case the "confirm same series AND unit" rule exists for: matching on the bare number calls four surfaces stale; matching on the label alone calls them clean.**

**Minor (LABOR):** session stamps read `~18:45 ET` / `~19:00 ET` / `2026-08-12T18:50Z` for work landed before 13:50 ET — `ET` and `Z` used interchangeably, and one of them is the `asof` column that grades freshness.

**→ PAT-099** (banked): *the measurement was never missing, the routing was.* ORACLE had published correctly 3× (7/31, 8/9) on routes neither consumer was on; ORACLE self-repaired via `watchlist.tsv:7` — *"ROUTE WIDENED 2026-08-12 — RED + LABOR ADDED AS STANDING CONSUMERS, AND THE REASON IS A DEFECT OF MINE."* Neither fix came from a scan.

---

## §3 — Prune sweep, 11 agents (red-comms Task B)

⚠️ **SUPERSEDED IN SCOPE by PROME's Will-approved 23-agent / 184-ref sweep** (`inbox/processed/2026-08-12_from-PROME_prune-sweep-RESULTS-33-defects-10-agents.md` — 33 defects / 10 agents; owner packets dispatched). Retained because it carries **four analyses PROME's results do not**, and because its per-agent deltas independently confirm PROME's stated causes.

**Method:** literal `archive/` in `CLAUDE.md`/`MEMORY.md`/`STATUS.md`/`MAINTENANCE.md` per agent; every cited path existence-checked on disk. **Self-declared lower bound** — RED's own set was 6 in boot surfaces + 1 in `research/`, so boot-only search undercounts by ~14% at minimum.

**Prune scope correction:** `1cb18fbc3` deleted `archive/` under **15** agents, not 12 — plus HANS (1), NEXUS (2), VIOLET (6). *(Closed by PROME's 23-agent scope; HANS/NEXUS appear in its defect list, VIOLET swept clean.)*

| Agent | Result |
|---|---|
| 🔴 **CARL** | 2 DEAD-PATH incl. 1 preservation claim. `CLAUDE.md:236` *"Mar-10 v2.1 archived (`archive/TRADE_2026-03-10.md`)"* ⚑ · **`CLAUDE.md:251` `archive/workbook_hardening/` — "consult archive only to research specific dispositions"**, the sharpest line in the sweep: *it directs a future session to read a directory that does not exist.* `archive/` WAS recreated (12 files) — neither cited artifact among them |
| 🔴 **HENRY** | 3 DEAD-PATH incl. 1 preservation claim cited twice. `MAINTENANCE.md:112`+`114` *"Moved refresh_status.py → archive/retired/"* ⚑ · `CLAUDE.md:248` boot instruction about a dir that doesn't exist. **Divergence:** HENRY's live retirement destination is `domain/archive/` (created 7/31, post-prune, present) — the agent moved on, the charter didn't |
| 🟠 **BARON** | 1 DEAD-PATH, `CLAUDE.md:49` ASCII structure diagram. LOW — dormant since 5/08, no session will read it |
| 🟡 **MARCO** | 2 DEAD-PATH **not prune-caused** (`sub_agents/*/threads/archive/`, `find` returns nothing — never existed anywhere under MARCO) + 2 CONVENTION-TO-ABSENT-DIR. **Do not attribute to `1cb18fbc3`** |
| 🟢 **CORAL** | **CLEAN — and the gold-standard counter-example.** `CLAUDE.md:5` verbatim: *"⚠️ Dead pointer found + fixed 7/9 self-sweep: the spinout record this line pointed to (`archive/CORAL_SPINOUT_2026-06-19.md`) does not exist anywhere in the repo (checked root `archive/`, `AGENTS/CORAL/archive/`, `AGENTS/REGINALD/`) — likely lost in the 2026-06 public-prep cleanup or never committed. **No record to restore; noting the loss here instead of citing a broken path.**"* Minor nit: `:229` still describes `archive/` as holding the spinout record; dir exists as `.gitkeep` only |
| ✅ **Clean in boot surfaces (5)** | BOND (0 refs) · HAWK (0 refs) · BRENT (0 refs) · BROCK (4, all resolve incl. `STATUS.md:37` verified on disk) · LABOR (2, incl. `:286` citing `KB_old_11col.tsv`, present) · ZHAO (3, all resolve) |

**Totals:** DEAD-PATH prune-attributable **6** (CARL 2 · HENRY 3 · BARON 1) · other cause 2 (MARCO) · **preservation claims 2** (CARL, HENRY) + RED's = 3 · CONVENTION 9 · RESOLVES 8 · RESOLVED-BY-DISCLOSURE 1 (CORAL). **3 of 11 agents with ≥1 prune-attributable dead path; 6 of 11 fully clean.**

**The four retained analyses:**
1. **Recreating `archive/` did not predict cleanliness — citation SPECIFICITY did.** 4 of 6 that recreated are clean, but CARL recreated and still holds 2 (different files came back); CORAL recreated as an empty `.gitkeep` while every content claim stayed false. Meanwhile 2 of 6 that did NOT recreate are perfectly clean (BOND, HAWK) — they never cited a specific file. **Every one of the 8 dead paths cites a named file or subdir. Restoring a directory does not repair a reference to a file inside it** — so "recreated the dir" must never be read as a resolution. *(Independently the same rule PROME derived from NEXUS.)*
2. **CORAL `CLAUDE.md:5` is the fix TEMPLATE for the whole class** — names the dead path, records that three candidate locations were checked, converts the citation into a documented loss. Same event and month as RED's uncorrected one. Free worked example if the 10 owner packets lack one.
3. **BRENT: the inverse defect** — 40 files across `archive/research_20260321_corpus/` + `legacy_20260721/` referenced by **zero** boot-read surface. Content with no pointer rather than a pointer with no content; **invisible by construction to any sweep that classifies refs.** Retention question, low priority.
4. **Second-order, CHECKS-class:** the prune's stated premise *"no live doc references"* is measurably false for 4 agents. **Whatever reference-check produced "0-ref" did not read charter FILES tables** — PAT-074 shape (a guard certifying health it never checked).

---

## §4 — COVERAGE CAVEATS (all six deliverables) — what was NOT read

**This section is the reason the file exists.** An audit's coverage limits are invisible once the conclusions are summarized, and a later pass that assumes full coverage will trust cells nobody verified.

**red-spine (audit + Task A):** rows 10-14 of the §3b invalidation inventory are **schema-and-cross-reference only, bodies unopened** — CALENDAR watch/backstop section bodies · `VX.tsv` rows · `KB.tsv` rows · `thesis/TIMELINE.md` · `CHALLENGE_IMPACT_LEDGER.md`. **Priority re-read: the impact ledger** (12d stale, cited fleet-wide by NEXUS, 3 of its challenges moved since its last write). Not needed: `MEMORY_ARCHIVE.md`, `handoff_WALTER/`, `design/`, `counter-evidence/`, `reports/` — none carry falsification state.

**red-workbook (audit + Task A):** VX `Flip_If`/`Counter_Evidence` bodies **not read** — the "high richness" verdict for VX is **inferred from structure**, and a currency-vs-quality call needs the text · KB `Fact`/`Notes` bodies and CATALYSTS event rows counted/status-tallied, **not content-read** (richness cells inferred) · ML `Finding` bodies beyond the last 12 rows + targeted greps · `STATUS.md`/`CLAUDE.md`/`challenges/`/`inbox/` entirely outside its cluster.

**red-workbook (Task B):** `SIGNAL_PROCESSING_CHECKLIST.md` Phase-2-step-7 body grepped for un-fire handling but **not read end-to-end** · REGINALD `STATUS.md` anchors that REG-T's `threshold_thesis_ref` points at **not opened** — flagged as "cannot say whether REG-T's exits live in REGINALD's prose instead." ⚠️ **I forwarded the claim to PROME without resolving this; resolved after the fact (§1 addendum) and it inverted into a finding.** The lesson is the process one: *a reader's flagged caveat is a blocker on the claim, not a footnote under it.*

**red-comms (audit + Task A):** `STATUS.md`/`MEMORY.md`/`MAINTENANCE.md`/`SCRATCH.md`/`CALENDAR.md`/`NEXUS_BRIEF.md` **grepped only as reference-check targets** — can assert whether a string appears, cannot characterize content or staleness · **20 of ~30 archive candidates never reference-checked** (10 were; cheap to close with one grep loop) · `board_log.tsv` rows 4-116 unprofiled (head/tail/schema/count only) · `OUTBOX.md` entry BODIES not read — "sequence unbroken" is a claim about IDs, **not content quality** · `challenges/`+`research/` classified by vintage and filename only, no bodies. **Methodological caveat on the working-dir map:** dir "character" is inferred from commit-date distribution; `reports/` = "dead cohort" is a claim about **write activity**, not about whether its 5 files remain load-bearing (4 of 5 verified unreferenced, which supports but does not prove retirement).

**red-comms (Task B):** per-agent counts are **lower bounds by construction** (boot-surfaces-only; refs phrased without a slash — "the archive", "archived under archive" — missed entirely). A "clean" agent here is clean *in its boot-read surfaces*, not tree-wide. HANS/NEXUS/VIOLET unswept *(closed by PROME's scope)*.

---

## §5 — Reader-ops record (method finding)

**3-for-3 idled holding without delivering, despite an explicit deliver-before-idle instruction in every prompt** — the same 3-for-3 as the 8/7 first wave, after which the instruction was added precisely to fix this. **The instruction does not work; the chase does** (all three delivered complete, first chase, no quality loss). Treat the chase as a standing step of every fan-out, and do not count a fan-out as complete on the spawn returning. *(8/11 sweep: 4-of-6 same behavior. Cumulative: 10-of-12 readers across three fan-outs.)*
