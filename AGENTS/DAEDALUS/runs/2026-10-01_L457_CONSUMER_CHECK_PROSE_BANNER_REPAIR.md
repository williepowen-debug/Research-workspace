# L457 — `scripts/consumer_check.py` prose dead-banner branch unreachable: repair record (2026-10-01)

**Reported by:** PROME (DOCKET L457, 2026-09-22; reproduction on `PROME/plans/2026-09-21_heartbeat-20th-rebase-PLAN.md`). An independent second finding came from HAWK on 2026-09-28 (`inbox/2026-09-28_from-HAWK_…`), which makes n=2.
**Mechanism (VERIFIED at the artifact, HEAD 63820706e):** `ISO_DATE_RE` is bound twice. L140 is the loose form `\d{4}-\d{2}-\d{2}` and is used by `file_is_dead()` L161. L723 is the anchored form `^\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2})?Z?$` and is used by `_line_class()` L752. The second binding shadows the first at import, so the prose branch requires line 1 to be BOTH a marker banner AND nothing but a date. That cannot be satisfied.

## ACCEPTANCE CONDITIONS — written BEFORE any edit (WQ-229; PROME's L457 set, adopted, plus one added from the population scan)
1. **ORDINARY:** a prose `.md` whose first non-empty line is a canon banner (`FROZEN <ISO date> — …`, including the emphasis/emoji/blockquote prefixes in the fleet's real population) clears. `file_is_dead(rowish=False)` returns True, and its hits move to the 🟢 handled bucket.
2. **OVERLAP:** the anchored constant has its OWN caller (`_line_class` L752, a dated-TSV-row test). **Rename the L723 constant, do not widen either regex**, and update L752. A dated `.tsv` row stays 🟠 HISTORY-ROW. A `.tsv` first cell that is a date followed by text stays NOT a history row, as it is today.
3. **WRONG OWNER:** a prose file that merely MENTIONS a marker word in its opening line or paragraph still does NOT clear. This false-HANDLED is the expensive direction. **Added from the population scan:** a **struck-through** marker (`~~FROZEN 2026-07-04~~ — FREEZE LIFTED`, live in `AGENTS/OZK/POSITIONS.md`) is a banner that was REVOKED. It must NOT clear. The recognizer may be NARROWED for this, never widened.
4. **MISSING INFORMATION:** a line-1 marker with no date does not clear, and a line-1 date with no marker does not clear.
5. **CONCURRENT ACTIVITY — N/A, justified:** this is pure read-only text matching over a file snapshot. There is no shared state, lock or index.
6. **POPULATION:** validated against the fleet set, never against PROME's one file. Before the edit: **135** tracked `.md` files carry a line-1 marker plus an ISO date, and **0** of them clear. **17** carry a line-1 marker with no date. Expected after the edit: 135 minus the struck-through ones clear, and 0 of the 17 clear.

Sections 7–9 below record what was done, the four states and the residue.

## 7. What was done (v1 → v2)
- **v1:** the anchored L723 constant was renamed `ISO_DATE_FULL_RE`, with its caller `_line_class` updated, and `~` was excluded from `DEAD_LINE1_RE`'s prefix class. Fixtures went 16/20 before the fix (the four ORDINARY cases failed, as expected) and 20/20 after.
- **Independent read #1 (Opus, own counterexamples): PASS-WITH-RESIDUE with ❌ on condition 3.** With the branch now live, the 8/20 recognizer cleared TITLES whose first word is a marker. It also cleared a revoked banner without a strike-through, and — **in the real population — the LIVE pending card `AGENTS/LABOR/docket/GRADING_CARD_20261002_NFP.md`** (`# 🔒 FROZEN GRADING CARD — … Fri 2026-10-02`). That ❌ changed the rule's meaning, which licenses one more read.
- **v2:** `DEAD_LINE1_RE` is tightened to the root canon form: the marker, then only spaces, `*`, `_` or `:`, then the ISO date. `DEAD_REVOKED_RE` (LIFTED · UNFROZEN · UN-FROZEN · REVOKED · REVIVED · THAWED · REOPENED · REINSTATED) is added as a veto. Nine new fixtures. **The fail path was watched for both versions:** v1 module ⇒ 21/29 (the 8 new cases fail), pre-fix module ⇒ 24/29 (the 5 ordinary cases fail), v2 ⇒ **29/29**. `--selftest` 10/10.
- **Condition 1 amended, disclosed:** "canon banner" now means the root form, **marker immediately followed by its date**. The **44** real archives whose first line is a non-canon banner (`# ARCHIVED — …`, `> ⚠️ **SUPERSEDED SNAPSHOT (…`) stay FLAGGED. That matches pre-repair behaviour and is the safe direction: an owner who wants such a file cleared re-writes line 1 in canon form.
- **Population:** tracked `.md` cleared by the prose branch went **0 (HEAD) → 91**. Named reproductions: HAWK `DECK_EVIDENCE.md` ✅ clears · HAWK `2026-09-08_STATUS_before_owner_catchup.md` ✅ · PROME `plans/2026-09-21_heartbeat-20th-rebase-PLAN.md` ✅. LABOR NFP card ✅ does NOT clear · OZK `POSITIONS.md` ✅ does NOT clear. HAWK's own repro command now lists both files in 🟢 "file-level dead-surface banner".
- **Neighbour:** `AGENTS/HANS/scripts/test_hans.py` imports `read_ledger` from this module. It exits 1 with 5 FAILs, which are **pre-existing and data-driven**: the pre-fix module gives the same `53.9 != 54.3` on HANS's live `PUBLISHED.tsv`. HANS was told by SendMessage, and `read_ledger` is untouched.

## 8. Four states (WQ-229)
| State | Evidence |
|---|---|
| **IMPLEMENTED** | v2 in `scripts/consumer_check.py` + `scripts/tests/test_consumer_check.py` (this commit) |
| **TESTED** | 29/29 committed fixtures, with both fail paths watched; `--selftest` 10/10; fleet population 0 → 91, LABOR/OZK negatives hold |
| **INDEPENDENTLY VERIFIED** | **Read #2 (Opus, final): PASS-WITH-RESIDUE.** It checked 15,506 tracked `.md` files, and v2 clears 91, **none of them live or pending** (lines 1–12 plus git history read on the doubtful ones). `_line_class` gives HEAD-identical results on 12/12 inputs, and nothing else imports the renamed names. Ledgers are reproduced below. |
| **STILL UNRESOLVED** | Residue R1–R4 below. These are ❌ on condition 3 for **synthetic inputs only**, with no real instance today. Not fixed: a fix after the final read would be unreviewed. **Owed: a new episode with its own acceptance conditions.** |

## 9. Residue (declared; from read #2)
- **R1 — the veto list is incomplete:** `NO LONGER FROZEN`, `UNARCHIVED`, `UNRETIRED`, `RESUMED`, `RE-ACTIVATED`/`REACTIVATED`, `RESTORED`. A banner like `ARCHIVED 2026-07-04 — UNARCHIVED 2026-08-01` would clear. Easy to fix next episode.
- **R2 — this is built into the design:** a PENDING pre-registration written in canon shape (`FROZEN 2026-10-08 — spec letter for the claims print`) would clear. Checking the shape of line 1 cannot tell "spec locked" apart from "surface dead". Candidates: veto a future date on line 1, or the words PRE-REG / PENDING / UNTIL / GRADES. **Fleet hygiene note for desks:** pre-registration cards should NOT use the dead-banner form. The real ones today (LABOR) do not.
- **R3:** a banner dated in the future clears, and so does a first line that is a list item, checkbox or table row with a canon banner inside.
- **R4 (safe direction):** a prefix longer than 12 characters is flagged rather than cleared.
- Note: `AGENTS/SAM/red/COUNTER_THESIS.md` clears correctly today (frozen until RED's next re-sweep). Once RED un-freezes it, R1/R2 decide whether removing the banner is enough. It is: a file without a banner is never cleared.

---
## Independent read #1 ledger (verbatim)
# consumer_check.py L457 repair — independent read (2026-10-01)
Subject: working tree vs HEAD `7182901ac` of scripts/consumer_check.py (+ tests). Read-only; author suite NOT re-run.
Method: fixtures under scratchpad/fx, driven via `cc.file_is_dead(p, rowish=False)`; HEAD loaded side-by-side from
`git show HEAD:scripts/consumer_check.py` for parity; population = `git ls-files '*.md'` (15,486), non-rowish only.

## Structural checks
| Check | Observed | Verdict |
|---|---|---|
| Other importers of the anchored ISO_DATE_RE | grep: only consumer_check.py (L143/164 loose, L729/758 FULL) + its test; HANS imports `read_ledger` only | ✅ |
| `_line_class` parity HEAD vs WT | 8 inputs × {a.tsv,a.md,a.TSV} = 24 identical results (HEAD's effective binding WAS the anchored one) | ✅ cond 2 |
| rowish path (`is_frozen`) | 0 diffs HEAD vs WT across all rowish .md; is_frozen does not use either regex | ✅ |
| Prose clears HEAD vs WT | HEAD 0 → WT 134 (matches author's 134) | ✅ cond 1/6 |
| marker-no-date population | 18 files (author: 17 — 10/8 LABOR card added today in 5a339a6db), 0 clear | ✅ cond 4 (count drift only) |

## Counterexamples (synthetic, line 1 of a prose .md)
| # | Input line 1 | dead? | Verdict |
|---|---|---|---|
| A | `# Superseded-values ledger (2026-09-01)` (live ledger) | True | ❌ cond 3 — title-noun use of a marker word clears; `-` satisfies `\b` |
| B | `# ARCHIVED items index 2026-09-01` (live index) | True | ❌ cond 3 — same class |
| C | `> **Retired agents (2026-09-01)**` (live roster section) | True | ❌ cond 3 — same class |
| S/H2 | `# Frozen thresholds 2026-09-01` / `# frozen-threshold register (live) 2026-09-01` | True | ❌ cond 3 — line 1 is upper-cased, so Title/lower case title-nouns match too |
| O | `## Retired rows — moved 2026-09-01 (rest of file live)` | True | ❌ cond 3 — partial-retirement heading clears whole file |
| K | `> ❌ FROZEN 2026-07-04 — FREEZE LIFTED 2026-08-23, live book` (revoked, NOT struck through) | True | ❌ cond 3 ("revoked banner must not clear") — only `~` revocation is caught |
| U | `> **🧊 FROZEN 2026-07-04 ~~not~~**` | True | ⚠️ `~` after the marker is not checked; contrived |
| N | `**FROZEN until 2026-10-15 — then resumes**` | True | ⚠️ future-dated/conditional freeze clears; date-position not checked |
| J | `\| FROZEN \| 2026-09-01 \|` (table header) | True | ⚠️ table first line clears; 0 real instances |
| P | `SUPERSEDED BY v2 — see X.md (written 2026-09-01)` | True | ✅ arguably genuinely superseded |
| D | `> RETIRED 2026-09-01 — agent retired` | True | ✅ |
| G | BOM + `FROZEN 2026-09-01 — not maintained` | True | ✅ BOM sits in the prefix class |
| H | `frozen 2026-09-01 — not maintained` | True | ✅ (canon form, lower case) |
| E/F | `UN-FROZEN 2026-09-01` / `NOT FROZEN 2026-09-01` | False | ✅ letters in prefix block it |
| I/W | `> ~FROZEN …~` single tilde / ZWSP + `~~FROZEN …~~` | False | ✅ |
| L/M | `<del>FROZEN …</del>` / `<s>FROZEN …</s>` | False | ✅ tag letters block it |
| Q | YAML front matter `---` then `status: FROZEN 2026-09-01` | False | ✅ (false-negative, cheap direction) |
| R | `FROZEN 9/22/2026 — …` | False | ✅ cond 4 (non-ISO date) |
| V | `> > > ⚠️ ⚠️ **FROZEN 2026-09-01` (13 prefix chars) | False | ✅ cheap direction |
| T1 | `_line_class` `2026-07-27T10:30:00Z\t…` (seconds) | None | ✅ unchanged from HEAD (pre-existing gap, not a regression) |
| T2 | `_line_class` BOM + `2026-07-27\t…` | None | ✅ unchanged from HEAD |

## Population — 134 real clears, 43 not in canonical `MARKER <date>` shape, all read
- Genuinely dead (archive rotations, SUPERSEDED snapshots, DO-NOT-ROUTE outboxes, FROZEN/retired corpora,
  HAWK-split copies, FERT TRADE "NOT revived", OZK/ZHAO TRADE, NEXUS/SIGNALS, SAM COUNTER_THESIS
  "FROZEN 2026-08-17 … unfreeze when RED re-sweeps"): judged correct clears.
- ⚠️ `AGENTS/LABOR/docket/GRADING_CARD_20261002_NFP.md` — line 1 `# 🔒 FROZEN GRADING CARD — NFP SEPTEMBER … Fri 2026-10-02`.
  A PENDING pre-registration card (print tomorrow; amended pre-print in c1a979e32 9/29, "armed" 5a339a6db
  today). The ISO date is the EVENT date, not a freeze date; "FROZEN" means letter-locked, not "not maintained".
  Its hits now go 🟢. Sibling `GRADING_CARD_20261008_claims.md` (also pending) does NOT clear only because its
  line 1 has no ISO date — clearing depends on date formatting, not on deadness. Defensible (a frozen card's
  letter is not refreshed) but a superseded INPUT on a still-amendable card now escapes the scan.
- ⚠️ `PROME/inbox/processed/2026-09-28_from-HAWK_…md` — `SUPERSEDED IN PART …` clears the whole file; it is in
  processed/ (history), so low consequence.
- No real live file of the title-noun class (A/B/C/S/O) or the unstruck-revoked class (K) exists today: the ❌s
  above are latent — zero instances in 15,486 tracked .md — but nothing prevents the next one.
- Only revoked banner in population (OZK/POSITIONS.md) correctly does not clear.

## Overall verdict: PASS-WITH-RESIDUE
The repair does what it claims: un-shadowing is correct, `_line_class` and the rowish path are byte-for-byte
behaviour-identical to HEAD, no external importer, `~` narrowing works, real-population clears are all
genuinely dead except one ⚠️ (pending NFP card). Residue: condition 3 as written is NOT held in general —
DEAD_LINE1_RE (pre-existing LIQUID 8/20 design, dormant until this repair activated it) accepts any line-1
title whose first word is a marker word (A/B/C/S/O) and any revoked banner not using `~` (K). Latent today
(0 real instances). Either narrow the condition-3 text to "mid-line mention + `~` revocation" in the run
record's residue block, or tighten the regex (note: requiring a date or dash right after the marker would
drop ~20 genuine banners like `ARCHIVED FROM STATUS.md` / `SUPERSEDED SNAPSHOT` — false-negatives, cheap side).

---
## Independent read #2 ledger (verbatim)
# consumer_check L457 v2 — independent read 2 (FINAL) — 2026-10-01
Subject: uncommitted diff to scripts/consumer_check.py + scripts/tests/test_consumer_check.py (DEAD_LINE1_RE canon-form, DEAD_REVOKED_RE veto, ISO_DATE_FULL_RE rename).
Evidence: my own harness (scratchpad cx.py, pop.py, pop.out); author suite NOT used. HEAD loaded from `git show HEAD:scripts/consumer_check.py`.

## A. New counterexamples — LIVE file cleared? (file_is_dead(path, rowish=False); True = cleared)
| # | input (line 1) | observed | grade |
|---|---|---|---|
| 1 | `FROZEN 2026-10-08 — spec letter for the claims print` (pending pre-reg, canon shape) | True | ❌(3)-LATENT — canon shape + fleet's 2nd meaning of FROZEN (spec lock) is indistinguishable by form |
| 2 | `> 🔒 **FROZEN 2026-09-30** — pre-registration, grades on 2026-10-08` | True | ❌(3)-LATENT — same; pending-event card clears |
| 3 | `FROZEN 2026-10-01 until the 2026-10-08 print — grading spec` | True | ❌(3)-LATENT — 'until' only vetoed when it precedes the date |
| 4 | `# FROZEN 2027-01-15 — not maintained` (future date) | True | ⚠️(3) — no date ≤ today guard; a future-dated FROZEN is a lock, not a dead surface |
| 5 | `FROZEN 2026-07-04 — NO LONGER FROZEN, live again` | True | ❌(3)-LATENT — veto list misses it |
| 6 | `ARCHIVED 2026-07-04 — UNARCHIVED 2026-08-01, maintained` | True | ❌(3)-LATENT — UNARCHIVED not in veto |
| 7 | `FROZEN 2026-07-04 — maintenance RESUMED 2026-08-01` | True | ❌(3)-LATENT — RESUMED not in veto |
| 8 | `RETIRED 2026-07-04 — RE-ACTIVATED / REACTIVATED 2026-08-01` | True/True | ❌(3)-LATENT — neither form in veto (fleet uses "reactivation", e.g. ZHAO 7/4) |
| 9 | `SUPERSEDED 2026-07-04 — RESTORED as canonical` / `RETIRED … — UNRETIRED` | True/True | ❌(3)-LATENT — RESTORED, UNRETIRED not in veto |
| 10 | `# RETIRED 2026-09-01 — agents list (maintained; add rows…)` | True | ⚠️(3) — banner text says maintained; form can't see it (inherent to line-1 form) |
| 11 | `- [ ] FROZEN 2026-10-08 — freeze the claims card (TODO)` | True | ⚠️(3) — list/checkbox item as line 1 of a live TODO clears ('-','[',']' allowed in prefix) |
| 12 | `- RETIRED 2026-10-15 — planned retirement of HAWK (pending Will)` | True | ⚠️(3) — future-dated list item clears |
| 13 | `| FROZEN 2026-07-12 — archive |` (table row line 1) | True | ⚠️(3) — first row of a live table clears; `| FROZEN | date |` correctly does not |
| 14 | `frozen 2026-07-04 — freeze lifted 2026-08-23` (lowercase) | False | ✅(3) — line upper()'d before veto |
| 15 | `<del>FROZEN 2026-07-04</del> — live book` / `<s>…</s>` | False/False | ✅(3) — tag letters break the prefix class |
| 16 | `> **~~FROZEN 2026-07-04~~** live` / `~FROZEN 2026-07-04~` | False/False | ✅(3) — '~' excluded |
| 17 | `FROZEN 2026-07-04 — not REVIVED` | False | ✅ safe direction (false flag, as disclosed) |
| 18 | `FROZEN_2026-07-04` / `SUPERSEDED-2026-07-04` / `FROZEN on 2026-…` / `FROZEN — 2026-…` / `FROZEN (2026-…)` | all False | ✅(4) flagged — safe direction |
| 19 | `status: FROZEN 2026-07-12` / YAML `---` first | False/False | ✅(3) |
| 20 | prefix 13 chars `> ⚠️⚠️ 🗄️🧊 **FROZEN 2026-07-12 — archive**` | False | ⚠️(1) false-FLAG (acceptable direction); emoji VS16 counts as a char |
| 21 | prefix 10–12 chars (`> ⛔⛔ **⚠️ `, `### > ⚠️ **`, `> ⚠️ 🗄️ 🧊 **`) | True | ✅(1) |
| 22 | `FROZEN 2026-09-01T10:00Z — …` / BOM-prefixed canon / `<!-- FROZEN 2026-07-12 -->` | True | ✅(1) (comment form clearing is defensible) |

Latent = reproduced synthetically; ZERO instances in the real population (section C).

## B. Overlap / rename (condition 2)
- `_line_class` v2 vs HEAD, 6 inputs × {.tsv,.md} (bare date, `T10:00Z`, `date x`, date in cell 2, threshold-tail line, bare value): 12/12 identical. Extra v2-only probes: ` 2026-07-27`/`2026-07-27 ` cell → HISTORY-ROW (strip() before match, same as HEAD); `2026-07`, `2026-07-27x`, `date` → None. ✅(2)
- `ISO_DATE_FULL_RE` used only at consumer_check.py:767; no other .py in repo references `ISO_DATE_RE`, `ISO_DATE_FULL_RE`, `DEAD_LINE1_RE`, `DEAD_REVOKED_RE` or `file_is_dead` (grep, .venv excluded). Only importer of the module's internals: test_consumer_check.py; HANS test_hans.py imports `read_ledger` only. The one external mention is a HAWK inbox packet's diagnostic one-liner (`c.ISO_DATE_RE.pattern`) — still resolves, now to the loose form. ✅(2)
- Loose `ISO_DATE_RE` is now the binding at module scope (line 151) and no later rebinding exists. ✅
- `consumer_check.py --selftest`: 10/10 OK (tool's own selftest, side check only).
- Note: `ISO_DATE_RE.search(first)` in file_is_dead is now redundant (DEAD_LINE1_RE already requires the date) — harmless.

## C. Real population (condition 6) — `git ls-files '*.md'`, 15,506 files present
- HEAD clears 0; v2 clears 91 (matches author's 91).
- Each of the 91 line-1s read (pop.out). All are dead-surface declarations: FROZEN/ARCHIVED/RETIRED/SUPERSEDED + "not maintained / historical / do not cite / superseded by …".
- Checked further (lines 1–12 + git log) for every file with a post-banner commit or a revival keyword:
  - AGENTS/OZK/TRADE.md — `> **🧊 FROZEN 2026-07-04 — position book UNRECONCILED …` — still frozen: the 8/23 lift was scoped to POSITIONS.md only (PROME/proposals/2026-08-23_rows-76-77-78-RULED.md row 78; commit 465c0b7f2 body). Not LIVE.
  - AGENTS/SAM/red/COUNTER_THESIS.md — `FROZEN 2026-08-17 — counter-thesis not rewritten …; unfreeze when RED re-sweeps` — banner prepended 9/25 (82b7ef9b9), body unchanged since 6/30 ("record of a counter-case, not a live dashboard"). Not LIVE; frozen-pending-refresh. ⚠️ note only: it will need its banner removed at re-sweep or it keeps clearing.
  - AGENTS/NEXUS/SIGNALS.md (24 commits) — FROZEN 2026-09-29, retired same day by Will-directed D7. Not LIVE.
  - AGENTS/ZHAO/LAST_COMPLETION.md — FROZEN 2026-09-17 "no longer maintained"; a line-8 forward reference (11/10 tariff expiry) is historical content. Not LIVE.
  - FORGE/timing/README.md, DAEDALUS retired cards, WAL archive — revival-keyword hits are history text ("pending cleared", "LIFTED 7/22" inside a closed card). Not LIVE.
- Pending/pre-registration card population (`*GRADING_CARD*`, `*PREREG*`, `*LETTER*`): line 1 uses non-canon `FROZEN GRADING CARD …` / `PRE-REGISTERED, frozen at …` — all stay FLAGGED, incl. LABOR GRADING_CARD_20261002_NFP and _20261008_claims.
- **LIVE/PENDING files cleared by v2: NONE found (91 of 91 checked).**

## D. Verdict: PASS-WITH-RESIDUE
Conditions 1, 2, 4, 6 hold; 5 N/A. Condition 3 holds on the real population (0 LIVE/PENDING cleared of 91), but NOT universally — it is form-based and a canon-shaped line can still clear a live file:
- R1 (❌(3)-latent, cheap): veto list misses NO LONGER, UNARCHIVED, UNRETIRED, RESUMED, RE-ACTIVATED/REACTIVATED, RESTORED (cases 5–9).
- R2 (❌(3)-latent, inherent): canon-shaped pending pre-registration (`FROZEN <date> — spec letter …`, `… until <date>` after the date) clears (cases 1–3); line-1 form cannot separate "spec locked" from "surface dead". Partial mitigation: veto when line 1 holds a date later than today, or words PRE-REG/PENDING/UNTIL/GRADES.
- R3 (⚠️): future-dated banner clears (case 4); list-item / table-row / checkbox line 1 clears (11–13).
- R4 (⚠️, safe direction): prefixes >12 chars false-flag (case 20).
Any fix to R1–R3 made after this read is unreviewed (Review budget: this was the final read) and must be dispositioned as IMPLEMENTED/TESTED, never INDEPENDENTLY VERIFIED.
