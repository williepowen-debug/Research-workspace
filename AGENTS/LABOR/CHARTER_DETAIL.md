# LABOR — CHARTER DETAIL (cold half of `CLAUDE.md`)

**Created 2026-09-07 under WQ-193** (Will verbatim *"Approve WQ-193 with your recs"*, 16:35 ET; contract `PROME/proposals/2026-09-07_wq193-RULED.md`).

⛔ **ON-DEMAND / grep ONLY — this file is NEVER a boot read, and it therefore carries no read-cap budget of its own.** If it ever becomes a boot read it acquires one.
🔒 **`CLAUDE.md` wins on any RULE.** This file holds the *why* — origins, worked examples, incident write-ups, rulings-as-history. **Blocks were moved verbatim and contiguous; no rule was changed and no obligation was deleted in the move.**
📋 **Census at the split → the WQ-193 delivery memo** (text census: line/byte/crc before and after; obligation census: every active duty located after the split).

---

<a id="b2a-origin"></a>
## § `b2a-origin` — B2a — spine-freshness gate: build history, falsification record, and the three misses that paid for it

*(moved verbatim from `CLAUDE.md` 2026-09-07; not edited)*

✅ **AUTOMATED 2026-08-23 (BD-02 DISCHARGED) — `scripts/spine_check.py`, run by `boot.py` as step (a-bis) immediately after the data sweep.** It parses **ISO `obs YYYY-MM-DD` tokens ONLY** (prose dates like *"w/e Aug 15"* are deliberately NOT parsed — that fragility is what deferred this build three times; a prose-only STATUS reports **CANNOT-VERIFY**, never a false PASS), reduces with **max()** so dated-historical rows are inert **by construction** rather than by exclusion rules that rot, and prints **three states — STALE / FRESH / CANNOT-VERIFY — every run, never silent.** **A fetch failure is CANNOT-VERIFY, not a pass.** Exit 2 on stale-or-unverifiable. ⚠️ **You must still READ the line** — the gate reports, it does not refresh. **Falsified before adoption** (4 cases: fires on a stale spine; inert on an added historical row; loud on a missing ISO token; loud on an unreachable FRED). *Paid for by THREE misses: 7/16, 7/31, and 8/20 — the last found by DAEDALUS's external sweep three days before my own boot found it.* ⚠️ And note the limit even once built: **this gate only fires when a session runs.** Neither it nor anything else in my boot docs can catch a print that lands on a day nobody boots (the summons gap — an external CATALYSTS-driven alert is PROME's to build).

---

<a id="b5b-origin"></a>
## § `b5b-origin` — B5b — why the unconsumed-dated-artifact check exists (the 7/30 and 7/29 cards)

*(moved verbatim from `CLAUDE.md` 2026-09-07; not edited)*

   > **Why this step exists.** B5 reconciles `CATALYSTS.tsv` *events*; nothing reconciled the *artifacts*. A frozen grading card is written days ahead precisely so the grade cannot be improvised after the fact — but until 2026-07-31 **no boot step ever looked for one.** On 7/30 `GRADING_CARD_20260730.md` sat unconsumed for its own print, and the 7/29 FOMC labor-language card went ungraded, both discovered only when a spawn happened to boot on 7/31. *(Audit item A2; boot-step half authorized by PROME 7/31. Whether an unconsumed card should also BLOCK closeout is a separate open question in Will's disposition batch — **do not** treat this step as a closeout gate yet.)*

---

<a id="b5b-ruled-no-gate"></a>
## § `b5b-ruled-no-gate` — B5b — the RULED-NO-GATE decision of 2026-07-31 and its stated basis

*(moved verbatim from `CLAUDE.md` 2026-09-07; not edited)*

   > ✅ **RULED-NO-GATE (Will, 2026-07-31, via `inbox/2026-07-31_from-PROME_remaining-rulings-RULED-implement-next-boot.md`).** The open question above — *should an unconsumed card also BLOCK closeout?* — is **decided: keep B5b, add NO closeout gate.** One mechanism, boot-side. The ruling's stated basis is LABOR's own honest-limit reasoning: a closeout gate would fire on the session that is *already too late* to help, while the boot check catches the card at the next available moment either way. **Do not re-open this without a new failure.**

---

<a id="c2-0-worked-example"></a>
## § `c2-0-worked-example` — C2-0 — the LAB-06 worked example that bought the stale-high-confidence sweep

*(moved verbatim from `CLAUDE.md` 2026-09-07; not edited)*

**Why this exists:** every gate in `PREDICTIONS_SCOREBOARD.md` §C runs at **registration** (boot B4, *"before writing any NEW prediction"*). LAB-06 was registered 2026-02-18 and sat at **80% for five months** — no gate ever looked at it again, and it reached scrutiny on 7/31 only because a session happened to ask *"what would I be embarrassed by on Monday?"*. **That is luck, not a control**, and it cost 0.64 of Brier and moved the book's mean from 0.256 to 0.293. **The exposure is the STALE high-confidence row, not the newly-written one** (`[[finding_registered_gate_captures_attention]]` — the gated instrument absorbs the attention; sweep the un-gated ones separately). ⚠️ **Do NOT read a hardcoded flag-list here — RUN the sweep.** This line used to name *"LAB-08 (65%) and LAB-10 (75%)"* as currently flagged; **by 2026-08-23 both had moved and the sentence was false on both counts** (LAB-10 **RESOLVED ❌ 2026-08-07**; LAB-08 **repriced 65% → 35% posted on 8/7**, so it no longer clears the ≥60% bar — its as-made 65% still governs SCORING). **A sweep whose worked example is a stale list teaches the reader the answer instead of the procedure**, and this is a boot-loaded file, so the stale list loaded every session. **Live result at the 2026-08-23 sweep: ZERO rows trip it** — the four OPEN rows are LAB-03 7%, LAB-12 30%, LAB-08 35%, LAB-11 50%, all under 60%. Re-derive it each time from `workbook/PREDICTIONS.tsv` (OPEN **and** ≥60% **and** confidence unmoved 60d+); if the answer is zero, say zero.

---

<a id="recipient-paths-incident"></a>
## § `recipient-paths-incident` — RECIPIENT PATHS — the 2026-08-07 stranded-packet incident and why the rule lives in the charter

*(moved verbatim from `CLAUDE.md` 2026-09-07; not edited)*

> ⚠️ **Why this lives in `CLAUDE.md` and not in a note.** Writing to a non-existent path **does not fail** — `git add` creates it, the commit succeeds, and from the sender's side the packet looks delivered. **`orphan_check.sh` cannot catch it either**: the file is committed, so it is not an orphan. The only signal is that nobody ever replies. On 2026-08-07 SAM found **two LABOR packets stranded at `AGENTS/PROME/`**, one of which carried a **six-session escalation** (`SIG-W-20260727-006`) that PROME had therefore never seen. SAM had made the identical mistake three times, and **the correction only stuck once the path went into SAM's own `CLAUDE.md`** — because the flag itself arrived as an inbox packet, and the MAIL rule above says don't read inbox at normal boot. **A routing fix delivered by the broken channel cannot fix the channel.** *(Both stranded packets were migrated by PROME at `86aa38645` and are in `PROME/inbox/processed/`; verified 2026-08-12.)*

---

<a id="published-tsv-archaeology"></a>
## § `published-tsv-archaeology` — FILES — `workbook/PUBLISHED.tsv`: the three usage rules and the measured cost of the distinctive-form rule

*(moved verbatim from `CLAUDE.md` 2026-09-07; not edited)*

⚠️ **Three usage rules bought the hard way:** (a) `asof` must be an **ISO timestamp, not a bare date**, whenever a metric can change twice in one day — a date-only tie makes the reader sort by value *alphabetically* and it will report the **retracted** value as current (hit live 7/31; → HENRY packet, BD-10); (b) the `value` column must hold the **distinctive form that actually appears in prose** (`3.4->3.1%`, `202,750`), never a bare percentage — bare `10%` returned **1,785 hits**. ⚠️ **KNOWN COST, measured 2026-08-23 — this rule trades one failure for another and you should know which you are buying:** a "distinctive form" contains punctuation, so `NUM_RE.fullmatch` fails and the needle is typed **TEXT** — and **a TEXT needle can never be demoted to 🟠 by `consumer_check`, by construction** (it hits the *"exact by construction"* branch before the context and sig-digit checks, and the collision pass only inspects numeric needles). **So this rule buys precision and pays in un-demotable 🔴s.** Live instance: `--old 32/75` returned **5 🔴 of which 1 was real**, the other four correctly-dated historical records. **Keep following the rule — the 1,785-hit alternative is worse — but treat a 🔴 on a text needle as UNGRADED, and check the path class yourself before packeting anyone.** Routed to HENRY (builder) 8/23; (c) `suppress_until` is **documentation only — the tool does not read it** (BD-10). |

---

<a id="grading-card-inventory-archaeology"></a>
## § `grading-card-inventory-archaeology` — FILES — grading-card rows: the repeatedly-restated inventory counts and why the cell is not to be trusted

*(moved verbatim from `CLAUDE.md` 2026-09-07; not edited)*

⚠️ **Do not trust an inventory written here — `ls docket/*.md` is the answer** (this line said *"Currently live: none"* while `docket/graded/GRADING_CARD_20260828_QCEW.md` had been live since 8/7). ✅ **GRADED AND ARCHIVED 2026-08-28: `docket/graded/GRADING_CARD_20260828_QCEW.md`** — frozen 2026-08-07, **21 days early**, carried **LAB-08** and vector 8. **Graded same-morning off §4: the preliminary printed −79,000 ⇒ BAND E ⇒ vector 8 4 → 2, LAB-08 live 15% → 4%, and NO resolution row (the final lands Feb-2027 and scores as-made 65%).** 🔒 **The card did the thing cards are for: two pre-commitments written 21 days apart agreed and no judgment was exercised on the day.** **LIVE CARDS AT 2026-08-28: NONE** — `ls docket/GRADING_CARD_*.md` returns empty, which is the answer, not this cell. **Next card owed: ECI Q3, 2026-10-30** (quarterly-gauge rule, C2a). |

---

<a id="graded-dir-archaeology"></a>
## § `graded-dir-archaeology` — FILES — `docket/graded/`: the count that has now been restated three times

*(moved verbatim from `CLAUDE.md` 2026-09-07; not edited)*

**Contents are enumerated by `ls docket/graded/`, not by this cell** — it held 4 cards when this line was written and holds **7** as of 2026-08-28 (`GRADING_CARD_20260828_QCEW.md` added at today's grade; before that `GRADING_CARD_20260813_claims.md` + `FOMC_LABOR_LANGUAGE_20260819.md` at the 8/20 grade). ⚠️ **This count has now been restated three times and is exactly the class of cell the file warns about — trust the `ls`.** |

---

---

<a id="h1119"></a>
## 2026-11-19 charter trim — text moved out of `CLAUDE.md` (WQ-701 A2 ceiling; WQ-719 A / WQ-721 A brief rule; WQ-678 A + B)

*Moved 2026-11-19 by LABOR (PROME task letter prome-36, 2026-11-19). Each block below is the exact text removed from `AGENTS/LABOR/CLAUDE.md`, byte for byte, with the line it stood on in the pre-trim file (55,603 B, commit before this one). "Moved verbatim" blocks left a pointer to this file; "superseded text" blocks were replaced in place by the ruling named in the section title. `CLAUDE.md` wins on any rule.*

<a id="h1119-identity"></a>
### § `h1119-identity`

**Pre-trim line 12 (moved verbatim):**

```text
 *(Tension refreshed 2026-07-24, ECI result folded 2026-07-31; prior tension — staffing canaries bottoming / WARN surging / DOGE unpriced — resolved by March-April data as owed.)*
```

<a id="h1119-spawn-1a"></a>
### § `h1119-spawn-1a`

**Pre-trim line 23 (moved verbatim):**

```text
 *(Origin: SIG-W-20260710-005 + SIG-W-20260717-008 sat undispositioned because spawned sessions skipped the `inbox/WALTER/` scan — the exact blind spot B2a/C1 exist to prevent.)*
```

<a id="h1119-spawn-1b"></a>
### § `h1119-spawn-1b`

**Pre-trim line 24 (moved verbatim):**

```text
 *(This is the step whose absence let the 7/30 grading card and the 7/29 FOMC card both go unconsumed until a 7/31 spawn stumbled on them. Scoped spawns are exactly where it gets skipped, which is why it is on the floor card.)*
```

<a id="h1119-B1"></a>
### § `h1119-B1`

**Pre-trim line 42 (moved verbatim):**

```text
 *Split 2026-09-02 (BD-25) because `STATUS.md` was 53,375 B against the binding 32,550 B READ_CAP budget — an over-cap boot surface returns a PARTIAL file with no error, and the part it drops is the tail (PICKUP + BOTTOM LINE).*
```

**Pre-trim line 42 (moved verbatim):**

```text
 *(The dated 2026-10-02 re-trigger was discharged 2026-10-01, whichever-first: below the rotate tier.)*
```

<a id="h1119-B2"></a>
### § `h1119-B2`

**Pre-trim line 47 (moved verbatim):**

```text
 *(fixed 2026-08-23: past-due rows previously printed only when the upcoming list was empty, i.e. never on a normal boot)*
```

**Pre-trim line 48 (moved verbatim):**

```text
 The gate was previously specified against output the documented command does not produce. *(Found in the 7/31 boot-doc audit, item A1, by running both forms side by side; `labor_data.py` standalone shows `Initial Claims … 2026-07-25 [DOL]`, `4-wk MA`, `CC … 2026-07-18` — `boot.py` without `--verbose` showed none of it.)*
```

<a id="h1119-B2a"></a>
### § `h1119-B2a`

**Pre-trim line 49 (moved verbatim):**

```text
 *Origin: 2026-07-16 claims print (208K w/e 7/11) sat unnoticed while 7 live STATUS surfaces still presented w/e-Jul-4 as current — caught only by a 7/20 seeded sweep, not by boot. This gate exists so boot catches it.*
```

<a id="h1119-B4"></a>
### § `h1119-B4`

**Pre-trim line 51 (moved verbatim):**

```text
 *(Count corrected 2026-07-31 eve: this line said "11" and listed 11 after #12/#13 shipped that morning — the gate-count itself was a stale spine token. #14 added the same evening.)*
```

**Pre-trim line 51 (moved verbatim):**

```text
 That artifact is the calibration record this step used to only gesture at: LABOR's raw as-made Brier is **0.348 (13 rows, as of 2026-10-01, after LAB-03; the scoreboard summary table is the live figure)**, losing to a coin flip (0.25) *and* to its own base rate (`30/169 = 0.178`), dragged by high-confidence *threshold* misses (LAB-01 85%, LAB-06 80%, LAB-10 75%, LAB-02 65%, LAB-03 65%) while **every** *mechanism* call landed — **LABOR is 0-for-6 at ≥60% on threshold calls and 3-for-3 on mechanism calls at the same confidence** *(re-stated 2026-10-21 from `workbook/PREDICTIONS_SCOREBOARD.md`; the 9/07 as-made audit moved LAB-05 into the ≥60% bucket)*; the gates cap exactly that failure mode.
```

<a id="h1119-B5b"></a>
### § `h1119-B5b`

**Pre-trim line 67 (moved verbatim):**

```text
 *(WQ-193 ④: the ruling stays here; the open-question phrasing it settled is deleted from this file and survives only as history.)*
```

**Pre-trim line 68 (moved verbatim):**

```text
 *(Realized 2026-09-07: the 9/10 claims card was 3 days from its print with no file, and this step returned zero live cards — correctly, and uselessly.)*
```

**Pre-trim line 69 (moved verbatim):**

```text
 *(Pointer re-aimed 2026-09-07, WQ-193 ③: it cited BD-02, the spine-gate build, discharged 2026-08-23. **The limit is unchanged and the obligation is NOT retired.**)*
```

<a id="h1119-B5c"></a>
### § `h1119-B5c`

**Pre-trim line 71 (moved verbatim):**

```text
 *(Wired 2026-08-28, DAEDALUS wiring sweep leg ①, batch Will-approved in-session.)*
```

<a id="h1119-C1"></a>
### § `h1119-C1`

**Pre-trim line 77 (moved verbatim):**

```text
 *(WQ-193 ①: the "under 250 lines → `domain/sources/`" rule is deleted — a line count is not the binding constraint and that is not the destination.)*
```

**Pre-trim line 78 (moved verbatim):**

```text
 One refreshed number in one place while six others carry the old value is the exact drift the 7/20 sweep had to repair.
```

**Pre-trim line 79 (moved verbatim):**

```text
 *(WQ-214, Will-approved 2026-09-10 20:42Z via Decision Deck tap; bought by DAEDALUS F4 — Kill A carried a 9-week-stale NFP vintage while KEY THRESHOLDS in the same file carried the current one, and the spine-token sweep never fired because no LABOR series had "changed.")*
```

**Pre-trim line 80 (moved verbatim):**

```text
 *Origin: the 7/16 German-PMI routing note sat 4 days as silent carried debt until the 7/20 sweep forced the 2-minute fold.*
```

<a id="h1119-C2a"></a>
### § `h1119-C2a`

**Pre-trim line 83 (moved verbatim):**

```text
 *(extended from claims prints to quarterly gauges 2026-07-31, Will-ruled; LAB-17's card is the cited proof-of-pattern — it diagnosed its own prediction's fatal sizing defect a week before resolution, and the 7/29 FOMC card caught a wrong standing thesis of mine on grade day).*
```

**Pre-trim line 83 (moved verbatim):**

```text
 (the 9/10 card's docketed term was `(X−200)/4` against a true `(X−212)/4`, inverting the MA's direction at the modal print)
```

**Pre-trim line 85 (moved verbatim):**

```text
 On 7/29 the branch resolved *correctly* while its stated consequence was refuted by the same text — right bucket, wrong conclusion, and only the separate line catches that.
```

<a id="h1119-recipient-paths"></a>
### § `h1119-recipient-paths`

**Pre-trim line 105 (moved verbatim):**

```text
 *(Installed 2026-08-12 from SAM's 8/7 routing alert; this is the fix that was routed on 8/7 and did not land until now.)*
```

<a id="h1119-output-rules"></a>
### § `h1119-output-rules`

**Pre-trim line 152 (moved verbatim):**

```text
  > **What bought this (2026-08-28, four hours, five surfaces):** I published *"35% was still **~7×** the honest post-print 4%"* — **the ratio is 8.75×; I never divided.** It rode STATUS, `LESSONS.md`, the scoreboard, `PREDICTIONS.tsv`, the grade report, `NEXUS_BRIEF.md` and a PROME delivery packet. ⚠️ **The wrong figure made my error look SMALLER inside a sentence whose whole purpose was to state it harshly**, and **four peers actively auditing me that day did not flag it.** Same session: *"not one was caught by me"* — false, it was 3-of-4 peer-caught, 1 self-caught. ⛔ **PROME's finding, and the reason this is a RULE and not a lesson: the four corrections were all in the NARRATIVE layer around figures that were themselves verified at the primary and never moved. The figures were fine. The prose about them was not — and prose is where I do my self-assessment.**
```

**Pre-trim line 158 (moved verbatim):**

```text
 *(Installed 2026-08-05 after `ISM Services June employment` sat at **47.4** — actual **51.2**, an expansion, so **wrong in sign** — for a month under a `[CONF]` tag earned by "2 independent web reads + arithmetic cross-check." → **L-12**.)*
```

<a id="h1119-key-thresholds"></a>
### § `h1119-key-thresholds`

**Pre-trim line 254 (moved verbatim):**

```text
 This boot-loaded pointer replaces the stale duplicate table that was here (removed 7/10 — it still showed Claims 213K / U-3 4.3% / DOGE 312-327K / "Shadow Payroll Gap resolves Mar-Apr", all superseded).
```

<a id="h1119-wq719-superseded"></a>
### § `h1119-wq719-superseded`

**Pre-trim line 30 (superseded text, replaced in place):**

```text
5a. **NEXUS_BRIEF re-pin is owed on EVERY spawn, including one-off reads** *(ruled 2026-07-31, Will — closes the gap where C1's re-pin obligation was unreachable from a spawn because step 5 made closeout conditional on "a state-changing grade")*. Either **re-pin it** (As-of + STATUS-HEAD pin, per C1) **or write one explicit line saying you are skipping it and why** — e.g. `NEXUS_BRIEF: declared skip, one-off read, no state changed.` **A declared skip is acceptable; a silent skip is not.** The brief sat 20d stale across 5 sessions while honestly self-bannering, which is exactly what silence buys.
```

**Pre-trim line 81 (superseded text, replaced in place):**

```text
   - ⚠️ **ORDERING (NEXUS schema Amendment 10, RATIFIED 2026-07-31 Will-approved; propagated to LABOR by PROME packet 2026-08-04, installed here 8/5):** **the NEXUS brief fold is the session's LAST write-back — after your final STATUS write, immediately before git commit.** **Check it with `python3 "$(git rev-parse --show-toplevel)/scripts/brief_pin_check.py" LABOR`** (WQ-438 (ii)). This is an *ordering* rule, not a reminder to refresh: the 7/31 fleet audit found **5-of-5 content-stale briefs had refreshed and then kept working; ZERO had skipped the refresh** — so "refresh every closeout" (which I already do) does not prevent the failure, and only the ordering constraint closes it. NEXUS owns the schema (`AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` §4.1 + §7); route objections there, not to PROME.
```

**Pre-trim line 82 (superseded text, replaced in place):**

```text
   - **NEXUS_BRIEF RE-PIN — LABOR is Tier-1, and the brief is a REQUIRED closeout artifact (mirror of the STATUS write-back), not an optional one.** Refresh `NEXUS_BRIEF.md` (VIEW / recent-pivot / As-of + STATUS-commit stamp) at **every** closeout — **re-bump the As-of + pin even on a no-change session** (NEXUS schema §4.1 write-back discipline). Keep the **pin = STATUS HEAD** so NEXUS's mechanical stale-check (§4.4a) reads FRESH. Under any line-cap pressure, **protect CROSS-DOMAIN + CALIBRATION first**. Scoped spawns: check its **As-of** date; if >7d stale, at minimum re-stamp the ⚠️ banner naming what post-dates it. **Standing scope fact (Will, 2026-06-16 — he overrode the locked NEXUS schema's Tier-2 scoping of LABOR in as many words: *"you aint no tier 2 agent... just stale for a bit"*):** LABOR sits at the HEAD of the transmission chain LABOR→CARL→REGINALD→HENRY, so its CROSS-DOMAIN SENDING edges carry real Type-B connective-tissue value — which is exactly what the brief format exists to surface. **Tier-1 is RATIFIED by NEXUS (★8/07)** — `AGENTS/NEXUS/BRIEFS_MAP.md` live-rules line, verified 2026-09-29; no ask outstanding. `BRIEFS_MAP.md` is NEXUS's file: **never edit it in place**. `[[project_labor_standing_nexus_brief]]` *(Embedded here 2026-07-31 under the Will-approved 7/28 Phase-2 memory restructure — this rule no longer auto-loads from `MEMORY.md`, so this IS its home now; PROME notified to flip `embed-pending` → `embedded` in `INDEX_COLD.md`.)* *(Wired 2026-07-22 by DAEDALUS QC: the "re-pin every closeout" rule previously lived only in the brief's own header — C1–C6 never mentioned it — and the brief sat 20d stale across 5 sessions while honestly self-bannered.)*
```

**Pre-trim line 283 (superseded text, replaced in place):**

```text
| `NEXUS_BRIEF.md` | Cross-agent sync surface NEXUS/PROME read. **LABOR = Tier-1 (Will override 2026-06-16); required closeout artifact — re-pinned at EVERY closeout, As-of/pin re-bumped even on no-change sessions (C1).** |
```

<a id="h1119-wq678-superseded"></a>
### § `h1119-wq678-superseded`

**Pre-trim line 142 (superseded text, replaced in place):**

```text
**COMMIT THE ROW YOURSELF** (Will-ratified 2026-07-24): `git commit AGENTS/SIGNALS.md -m "..."`, path-scoped, in the same session you append it. This is a narrow extension of the 7/23 inbox-packet carve-out and overrides root CLAUDE.md's "flag it to Prome" for **this file, for rows you authored**. Rationale: an uncommitted shared-file edit **orphans by design** — `orphan_check.sh` correctly tells every other agent `[not yours] — do not sweep`, so nobody picks it up and the cross-agent visibility layer silently loses the entry.
**Still NOT yours:** editing rows other agents wrote, restructuring the file, or any other shared/root doc (`HEARTBEAT.md`, root `CLAUDE.md`, `FORGE/`) — those stay with PROME/Will. *(Root CLAUDE.md now carries **carve-out ②** for self-authored shared-log rows, superseding the older blanket rule this line used to cite (WQ-193 ⑧); generalizing this fleet-wide is PROME's/Will's call, not LABOR's — flagged in `outbox/delivered/2026-07-24_to-PROME_signals-md-row-needs-commit.md`.)*
```

**Pre-trim line 230 (superseded text, replaced in place):**

```text
**Required categories:**

1. **Thesis kill (exit all):** Conditions that completely invalidate the thesis. 1-2 hard stops.
2. **Position-specific:** Exit criteria tied to individual positions (KELYA) with explicit levels and durations.
3. **Convergence downgrade (trim):** Conditions that weaken but don't kill the thesis. Partial exits.
4. **Time-based:** Mandatory review checkpoints (e.g., 60-DTE for options positions).
```

**Pre-trim line 293 (superseded text, replaced in place):**

```text
| `TRADE.md` | Position ideas (KELYA puts) |
```

**Pre-trim line 92 (superseded text, replaced in place):**

```text
cross-agent signal → `outbox/` per the Outbox Protocol below
```

