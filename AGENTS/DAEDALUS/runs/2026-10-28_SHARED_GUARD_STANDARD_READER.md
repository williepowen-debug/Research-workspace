# Shared-guard-standard floor check: reader report (2026-10-28)

**Written:** 2026-10-28 ~21:30 ET by a read-only reader for DAEDALUS (Claude Code, claude-opus-5-5). **Scope:** `BLUEPRINTS/STRICT_TEXT.md` (35 lines, 11,730 B), `BLUEPRINTS/STATE_VOCABULARY.md` (273 lines, 38,193 B) and `BLUEPRINTS/CHECK_STANDARD.md` (126 lines, 26,015 B), each read whole. **Registry row:** `sweeps/REGISTRY.tsv:12` (cadence 45d, last_run 2026-09-04). **HEAD at start:** `c6d77fc1f`; **HEAD at write:** `0d769a634`. A live DAEDALUS session edited the working tree during this run (see Coverage). **Writes:** this file only. No git write was made.

Claim tokens follow STATE_VOCABULARY Class 13. `VERIFIED` means checked at the artifact in this run. `SEARCH-NOT-FOUND` means the named pattern returned rc=1 and a positive control on the same surface returned rc=0; it is a claim about the search only.

## Summary

| Leg | Verdict | Count |
|---|---|---|
| 1. Internal integrity | DEFECT | 11 defects + 2 housekeeping |
| 2. Drift since last service | DEFECT | 6 commits: 4 SERVICE, 1 CORRECTION, 1 HOUSEKEEPING. The registry still says 2026-09-04 |
| 3. Consumer conformance | DEFECT | YURI and CYPHER CLEAN (10 cells). The 5 DAEDALUS registers and the gate script use 0 registered tokens; 5 registers have no STATE_VOCABULARY class; 12 cells are off their own local enums |
| 4. Glyph registration | DEFECT | 8 of 12 standing glyph entries unregistered; 2 meaning conflicts; 6 unlisted glyphs in use. STATUS.md and WILL_QUEUE.md first 80 lines CLEAN |
| 5. CHECK_STANDARD citations | CLEAN (0 dangling) | 73 citation lines in 37 files, all resolve. 3 advisories |
| 6. STRICT_TEXT self-conformance | DEFECT | 13 violations across 5 packets (graded 1 inbox + 2 outbox/delivered + 2 supplementary live) |

**Re-measure owed by STATE_VOCABULARY.md:9 at each sweep:** 38,193 B = 70.4% of the 54,250 B harness cap (117.3% of the 32,550 B boot budget, exempt as a REFERENCE REGISTRY per `READ_CAP.md:48`). No split is needed.

---

## Leg 1: Internal integrity

**Numbering.** STRICT_TEXT rules 1–10 plus 6b are contiguous and unique (`STRICT_TEXT.md:17-27`). STATE_VOCABULARY Classes 1–13 are contiguous and unique (`:15 … :238`), with extensions at `:28, :66, :161, :165`. CHECK_STANDARD §1–§14 are contiguous and unique (`:9 … :118`; 14 `## ` headers). Note that the brief said "§1–§11", but the file has 14 sections. `VERIFIED`.

**Cross-references that resolve (`VERIFIED`):** STRICT rule 6 → STATE_VOCABULARY Class 6 and Class 5 · STATE_VOCABULARY:181 → CHECK_STANDARD §8 · STATE_VOCABULARY:240 → CHECK_STANDARD §14 · CHECK_STANDARD:74 → STATE_VOCABULARY Class 9 · CHECK_STANDARD:124 → STATE_VOCABULARY Class 13 · CHECK_STANDARD:37 → §14(b) · STRICT:24 → `SPEC_LETTER_STANDARD.md` SL-5 (`:34`) · STRICT:35 and STATE_VOCABULARY:11 → `builds/REGISTRATION_CHECKLIST.md` row 15 (`:25`) · STATE_VOCABULARY:9 → `READ_CAP.md` rule 7 (`:13`) and REFERENCE REGISTRY row (`:48`) · CHECK_STANDARD:107 → `design/2026-08-28_INSTRUMENT_STATE_TAXONOMY.md` (exists).

**Defects:**

| # | Sev | Where | Defect | Evidence |
|---|---|---|---|---|
| 1-1 | MED | STATE_VOCABULARY.md:216 | Says Class-8 `SCHEDULED`/`EXEMPT-BY-CHARTER` are "pending mint, 8/28 register ②". The same file says they were MINTED 2026-08-28 (`:159`) and defines them at `:152-153`. The file contradicts itself, and the stale line sits in the paragraph marked SINGLE HOME | `:159` vs `:216` |
| 1-2 | MED | STATE_VOCABULARY.md:264 | Calls "the CHECK_STANDARD §8 glyph-vs-count rule" "pending encode, sweep-input ⑤b". It was RULED and encoded 2026-08-21 as §8 rule 6 | CHECK_STANDARD.md:74 |
| 1-3 | MED | STATE_VOCABULARY.md:157, :261 | Says the Cadence declaration affects `--nudge` ONLY "until WQ-147 … lands". WQ-147 M1 shipped 2026-09-01 (`b5494ecac`), so the line has been stale for 57 days. The map row at `:261` still names `--nudge` only | `scripts/ledger_staleness.py:541,970,1113` ("M1 (WQ-147)") |
| 1-4 | HIGH | STATE_VOCABULARY.md:51, :59, :60, :64 | `STOOD-DOWN` is a member of both the condition enum (`:51`) and the `Response` enum (`:59`). `:59` says the two cells are "never fused", and `:60` says "FIRED never downgrades … never by softening the condition cell". Yet `:64` prescribes the re-arm cycle `FIRED → STOOD-DOWN → ARMED`, which writes STOOD-DOWN into the condition cell after a fire. These are contradictory instructions for the same cell | quoted lines |
| 1-5 | MED | STATE_VOCABULARY.md:112, :247 (+ :57) | `UNKNOWN` has two meanings: Class 5 "unit is right; nobody has ever measured it" and Class 13 "no check run". `:57` also declines it as a gate token. There is no disambiguation note. A third meaning is live in the gate (`design/2026-09-17_DAEDALUS_GATE_SPEC.md:19`: "child rc 2 … cannot certify"). A companion collision is `RETIRED`: Class 1 (`:22`, surface ended by decision) vs the CORRECTIONS ladder (`:212`, `RETIRED` = `CLOSED-VERIFIED`) | quoted lines |
| 1-6 | MED | STRICT_TEXT.md:24 (rule 7) vs :21 (rule 5) | Rule 7 mints state tokens `GRADE-AT-PUBLICATION` · `GRADE-ON-REVISION` · `REGRADE-ON-REVISION` · `STAND-WITH-ANNOTATION`. Rule 5 says "State tokens come from STATE_VOCABULARY.md". STATE_VOCABULARY has 0 hits for each (grep count 0; positive control `FIRED` = 11) | grep receipts |
| 1-7 | MED | CHECK_STANDARD.md:70 vs :80-85 | §8 rule 3's exemplar is rc=3 (`cot_gold.py`). §9 fixes "0 clean · 1 findings · 2 cannot-certify" and calls §8 rule 3 "the fetch-tool instance of the same principle" (`:85`). §9's consumer half never says how an rc of 3 or more reads. A consumer keyed on "rc-1-or-marker" treats rc=3 with no marker as neither finding nor cannot-certify | quoted lines |
| 1-8 | LOW | CHECK_STANDARD.md:47 (§5) | "`CHECKS.tsv` gains a per-check on-FAIL column at the next register pass". The column already exists: `CHECKS.tsv:5` `On_FAIL (PAT-084)`, filled at the 2026-08-17 pass (`CHECKS.tsv:22` "[filled 2026-08-17 PR#4 register pass]") | `VERIFIED` |
| 1-9 | MED | CHECK_STANDARD.md:114 (§13) | "`builds/REGISTRATION_CHECKLIST.md` picks it up for new builds". There is no prior-art row in that checklist | `grep -n -i -E 'prior.art\|§13\|searched, novel'` rc=1; positive control `STATE-TOKEN` rc=0. `SEARCH-NOT-FOUND` |
| 1-10 | LOW | CHECK_STANDARD.md:92 (§10) | The retroactive leg is "registered for the ~8/28 fleet wiring sweep (… pending Will's confirmation …)". No self-inclusion leg was found in `runs/2026-08-28_WIRING_SWEEP/` | grep `self-scope\|self-inclusion\|§10\|retroactive leg\|own dir\|author.s own\|PAT-050` rc=1; positive control `scope` rc=0. `SEARCH-NOT-FOUND` |
| 1-11 | ADVISORY | CHECK_STANDARD.md:87, :94, :109, :118 | §10, §11, §13 and §14 are still PROVISIONAL "ratify-after-first-live-application". Their first live applications exist: `scripts/validate_all.py:24` (§13), `:36` (§10), `:96` (§11), built 2026-09-10; `scripts/ledger_staleness.py:792` (§14). No ratification record was found | grep `(§1[0134]\|section 1[0134]).{0,30}(ratified\|RATIFIED)` over PROME/proposals, EVOLUTION, STATUS, runs: rc=1; positive control (`Ratify §8`) rc=0. `SEARCH-NOT-FOUND` |
| H-1 | HOUSEKEEPING | STATE_VOCABULARY.md:253-271 | The enforcement map is out of class order and has duplicate class rows: Class 2 at `:256` and `:263`; Class 8 at `:261`, `:262` and `:270`; Class 1 at `:255` and `:271` | — |
| H-2 | HOUSEKEEPING | CHECK_STANDARD.md:107 | The sub-item inside §12 is labelled "C5", a WQ-254 package number rather than a §12 letter | — |

There are no contradictions between rules beyond 1-4 and 1-7. STRICT rule 9 and CHECK_STANDARD §2 overlap (both say "a null result states what it searched", both cite PAT-074) and agree, so this is not a defect.

## Leg 2: Drift since last service

The two 2026-09-04 commits, `623537d3f` (17:16) and `e0b63ff4f` (17:57), are the logged service itself (§3(c)(d)). Every later commit to the three files is below (`git log --since=2026-09-04 -p`):

| Commit | Date | File(s) | What changed | Class |
|---|---|---|---|---|
| `1cac226eb` | 2026-09-07 | STRICT_TEXT, CHECK_STANDARD | New rule STRICT 6b (figure names its OBJECT; H6). New CHECK_STANDARD §3(e) (production acceptance set; H8) | SERVICE |
| `cdde3ef30` | 2026-09-08 | STATE_VOCABULARY | New "Class 2 companion family", the orchestration prefixes `DUE-ROW L<n>` / `DUE-GATE <id>` (WQ-184), `:66-75` | SERVICE |
| `fcdcf9254` | 2026-09-24 | CHECK_STANDARD, STATE_VOCABULARY | New §12 C5 (SPECIFIED-BUT-NONEXISTENT, WQ-254 D1). New CORRECTIONS ladder → Class 11 mapping, with tokens `RECEIPTED` / `RETIRED` / `DEAD-AT-CAP` (`:212`) | SERVICE |
| `d90042830` | 2026-10-08 | STATE_VOCABULARY | Enforcement-map row `:263` corrected from "gains" to "⛔ NOT BUILT". Still true: `grep -c CANNOT-FIRE AGENTS/DAEDALUS/scripts/falsification_scan.py` returned 0 (rc=1; positive control `def ` rc=0) | CORRECTION (no rule change) |
| `47bd8f55d` | 2026-10-14 | STATE_VOCABULARY | New read-class and size-watch obligation (`:9`, which binds this sweep to re-measure) plus a correction of map row `:255` | SERVICE (+ correction) |
| `bf7c97405` | 2026-10-23 | STATE_VOCABULARY | Pointer appended to `CANNOT-FIRE` (`:52`, L499) | HOUSEKEEPING |

**Verdict:** standard content changed on 09-07, 09-08, 09-24 and 10-14. The registry row `sweeps/REGISTRY.tsv:12` still reads `last_run 2026-09-04`, and its last_findings has no entry after 09-04, although its own SERVICE RULE says the row is "serviced at any DAEDALUS spawn that touches any registry". The floor check is not the cause of that record gap; the record gap is the defect. Two in-file staleness defects (1-1, 1-3) predate these commits and were not caught by any of them.

## Leg 3: Consumer conformance

The DAEDALUS charter binds these cells: `CLAUDE.md:117`: "Write state cells (FLEET_MAP, SURFACES, PATTERNS Type/Conf, sweep verdicts) with canonical tokens from BLUEPRINTS/STATE_VOCABULARY.md." STATE_VOCABULARY has **no class** for any of these cells (grep counts 0 for `L0`, `L5`, `Admiralty`, `A1`, `ANTI`, `ENFORCED`, `UNMECHANIZED`, `WIRED`, `MANUAL-BY-DESIGN`, `paused`, `CLEAN`, `BLOCKING`, `ADVISORY`, `NOT-APPLICABLE`, `ENUMERATED`, `DECLARED`, `WITH-DEBT`; positive control `FIRED` = 11). As written, the charter rule cannot be satisfied.

| Surface · column | Tokens found (count) | Registered in STATE_VOCABULARY | Own local enum declared at | Off-enum (unregistered and outside its own declaration) |
|---|---|---|---|---|
| FLEET_MAP.tsv · Level | L4 26 · L5 7 · L3 5 · L2 4 · L1 1 · RETIRED 2 | `RETIRED` only (Class 1, banner sense) | `FLEET_MAP.tsv:39` "L0-L5" | `RETIRED` at `:26` (YEYOU), `:29` (HERMES) is outside L0-L5 |
| FLEET_MAP.tsv · Conf | H 25 · M 20 | none | `:38` H/M/L | none |
| SURFACES.tsv · State | ENFORCED 4 · PARTIAL 3 · UNMECHANIZED 2 · DEAD-FROZEN-BANNERED 1 · OWNED 1 · ENFORCED-advisory 1 · FROZEN-DECLARED 1 | none | `SURFACES.tsv:4` (ENFORCED · SCHEDULED · UNMECHANIZED · DEAD-UNBANNERED · UNASSIGNED) | `PARTIAL` `:5,:9,:17` · `DEAD-FROZEN-BANNERED` `:12` · `OWNED` `:13` · `ENFORCED-advisory` `:14` · `FROZEN-DECLARED` `:15`. **Also:** `:3` is a comment written as `"# ---…` (it starts with a quote), so a `#`-skip parser reads it as a data row with no State |
| sweeps/REGISTRY.tsv · status | active 18 | none | `REGISTRY.tsv:8` active\|paused | none. Separately, the `:8` column list omits the `resolve_by` column that the header `:1` carries |
| PATTERNS.tsv · Type | PATTERN 109 · ANTI 80 | none | `PATTERNS.tsv:2` | none |
| PATTERNS.tsv · Conf | A1 88 · A2 51 · B1 42 · B2 8 | none | `:2` Admiralty A1..C3 | none. Note that the column name `Conf` means Admiralty here and H/M/L in FLEET_MAP |
| CHECKS.tsv · State | WIRED-SINGLE-INVOKER 21 · WIRED 12 · WIRED-HARNESS 6 · MANUAL-BY-DESIGN 6 · SETUP-ONLY 3 · NOT-A-CHECK 2 · UNWIRED 1 · RETIRED 1 · WIRED-MANUAL 1 · BUILT-UNWIRED 1 · 2 compound | `RETIRED` only | `CHECKS.tsv:3` (it says "STATE_VOCABULARY has no class for invocation state — registry extension owed"; owed since 2026-08-03 and still noted at `REGISTRY.tsv:12`, 2026-08-07) | `RETIRED` `:22` · `WIRED-MANUAL` `:31` · compound `:36` · `BUILT-UNWIRED` `:40` · compound `:60` |
| `scripts/daedalus_gate.py:49-51` verdicts | CLEAN · DUE · ADVISORY · BLOCKING · UNKNOWN · NOT-APPLICABLE · ENUMERATED · DECLARED, plus eligibility `WITH-DEBT` (`:701`) | `UNKNOWN` only, with a different meaning (see 1-5) | `design/2026-09-17_DAEDALUS_GATE_SPEC.md:15-21` | all 9, measured against STATE_VOCABULARY. `DUE` collides by spelling with the prefix `DUE-ROW`/`DUE-GATE` (`:72-73`), which has a different meaning |
| YURI/workbook/INTENT_LEDGER.tsv · status | VOID (reason) 1 · MISS 1 · OPEN 4 | all (Class 3) | `:2` cites Class 3 | none. ADVISORY: `:5` uses `VOID (superseded prospectively …)`, but Class 3 VOID means "premise failed / unresolvable" (STATE_VOCABULARY:85). Class 3 has no token for a withdrawn or superseded row |
| CYPHER/workbook/PREDICTIONS.tsv · Status | OPEN 4 | all (Class 3) | `:2` cites Class 3 | none |

## Leg 4: Glyph registration

The declaration is `USER.md:49-80` (§ Decisions and Attention). `:80` reads: "A new glyph is declared here and registered in `AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md` before first use." That rule was introduced 2026-08-21 (`5a0be541d`).

| Glyph (USER.md line) | In STATE_VOCABULARY? | Note |
|---|---|---|
| ⚖️ (:55) | NO. Used as decoration at `:216` only | — |
| ATTENTION (:61) | NO (0 hits) | — |
| 🟢 🟡 🟠 🔴 (:65-68) | YES. Class 9 `:171` (severity-only, pointing to the root Status key) | registered |
| ⛔ (:74) | NO. Used decoratively at `:60,:259,:260,:263,:265` | — |
| ⚠️ (:75) | NO. Used decoratively at 7 lines | **Meaning conflict:** USER.md:75 says "caveat that must travel with a claim", but CHECK_STANDARD.md:72 says ⚠️ is "reserved for STATE-DEPENDENT degradation; a STANDING caveat … prints `NOTE:`" (script output) |
| 🧊 (:76) | NO (0 hits) | — |
| ★ (:77) | NO (0 hits) | — |
| ✅ / ❌ (:78) | NO. ✅ appears decoratively at `:26` | **Meaning conflict:** USER.md:78 says "resolved true / false". CHECK_STANDARD.md:68 uses ✅ = fetch OK, and `daedalus_gate.py:51` maps ✅ = CLEAN, ❌ = BLOCKING |

**Result:** 8 of 12 entries are unregistered. STATE_VOCABULARY has no glyph table at all, so the USER.md:80 rule has no target section.

**Glyphs outside the USER.md list, in use after the 2026-08-21 rule:** `scripts/daedalus_gate.py:51` ⏰ ❓ ✍️ ℹ️ (built 2026-09-17) · `outbox/delivered/2026-09-02_to-PROME_inbox-drained-…md:21` ℹ️, `:25,:56` ⭐ (U+2B50, not ★ U+2605), `:62` 🔨.

**`AGENTS/DAEDALUS/STATUS.md` (whole) and `PROME/WILL_QUEUE.md` (lines 1–80):** CLEAN. Neither has an emoji outside the list. The only non-ASCII symbols are typography: → ≥ ≤ ≈ − ①②③⑤⑰ (STATUS `:18,:26,:27,:38,:58,:63,:71`; WILL_QUEUE `:5-77`). These are enumerators and operators, not state glyphs. Method: a Python scan of Unicode `So`/`Sm` ≥U+2190 and ≥U+1F000, excluding the 12 listed glyphs.

## Leg 5: CHECK_STANDARD citations

`grep -rn 'CHECK_STANDARD' scripts/ AGENTS/DAEDALUS/scripts/ AGENTS/DAEDALUS/CHECKS.tsv PROME/tools/` returned 73 lines in 37 files (rc=0). The cited sections are §1, §2, §3, §3(b), §3(e), §4, §6, §7, §8, §8 rule 3, §9, §10, §11, §12, §13, §14, §14(b) and `CHECK_STANDARD.md:37`. **Every one resolves** (§1–§14 exist; `:37` is currently §3(c)(d), which holds the "Read the rc bare" text that `pipeline_rc_guard.py:14` means). Dangling: **0**. `VERIFIED`.

| Advisory | Where | Why it matters |
|---|---|---|
| A5-1 Non-`§` spellings defeat a `grep '§9'` consumer survey (§9 contract-change discipline, CHECK_STANDARD.md:84) | `scripts/corrections_boot_check.py:24` "SS9", `:31` "SS3(e)" · `AGENTS/DAEDALUS/scripts/walter_route_check.py:28` "sec3", `:33` "sec9" · `PROME/tools/table_check.py:34` "section 9" · `AGENTS/DAEDALUS/CHECKS.tsv:40` "CHECK_STANDARD 9" · line-number cite `scripts/pipeline_rc_guard.py:14` ":37" (fragile) | Four rc-contract citers are invisible to the survey §9 mandates |
| A5-2 An always-0 producer cites §9 | `scripts/pipeline_rc_guard.py:81` "Exit contract (CHECK_STANDARD §9): 0 always in hook mode (warn-only, fail-open by design)" vs CHECK_STANDARD.md:82 ("an always-0 contract is a standing silent-fallback-green exposure") | The choice is legitimate (in Claude Code, a hook exit of 2 blocks the tool call), but §9 has no harness-hook carve-out, so the citation reads as a violation. See fix F7 |
| A5-3 Stale status in a citer | `PROME/tools/will_handbook.py:17` "Prior-art line (CHECK_STANDARD draft norm, honored voluntarily)" | §13 is RULED (PROVISIONAL), not a draft |

## Leg 6: STRICT_TEXT self-conformance

**Population note.** The brief said "four packets in inbox/*.md". At read time (~21:15 ET) there was **one** (`2026-10-24_from-NEXUS_L40-…md`). It moved to `inbox/processed/` during this run, which shows a live DAEDALUS session. `ls -t outbox/` shows only `delivered/` (FROZEN 2026-08-17, `outbox/delivered/_FROZEN.md`), so its two newest files were graded. They are history, from 2026-09-02. To grade current output, I added the two newest live DAEDALUS-authored packets.

| Packet | Rule | Line | Violation |
|---|---|---|---|
| NEXUS→DAEDALUS L40 (`inbox/processed/2026-10-24_from-NEXUS_L40-amendment-count-…md`) | R10 | :3 | "Per PROME's 10/24 receipt: NEXUS's L40 duty is …" paraphrases PROME's instruction with no verbatim quote and no path stamp |
| same | R6 / R6b | :15 | "A12 15 · pre-A12 6 · no-CD 8 over 29" gives no unit and no object (29 of what: briefs? desks?) |
| outbox/delivered 2026-09-02 WQ-163 ruling | R8 | :64 | "**Those** are live obligations …" refers to the previous sentence's blocks |
| same | R2 | :69 | "'Cured' … should mean the split PLUS …" has no actor (who applies the definition?) |
| same | R2 | :70 | "NEXUS should not be graded down" is passive, and the grader is not named |
| same | R1 | :64, :69 | Instruction sentences of 40 words or more (target is 20 or fewer) |
| outbox/delivered 2026-09-02 inbox-drained | R2 | :46 | "Ask: fill the column at delivery-consume" has no named actor |
| same | R2 | :63 | "Playbook `sweeps/GATE_BASIS_SWEEP.md` is owed before the run" is passive and names no actor |
| same | R2 (minor) | :48 | "CONFIRMED, RESOLVE it." has no actor |
| *Supplementary:* DAEDALUS→WATT ISHM ASK (`AGENTS/WATT/inbox/2026-10-23_from-DAEDALUS_ISHM-grid-equipment-figure-ASK.md`) | R8 | :13 | "The figure then has no owner. PROME takes **it** to Will" |
| *Supplementary:* DAEDALUS→PROME WQ-508 (`PROME/inbox/processed/2026-10-23_from-DAEDALUS_WQ508-harness-audit-lines.md`) | R2 / R3 | :13-26 | Direction cells B01–C14 are bare codes (`a`, `c`, `S`, `b overclaim`, `a; c`) with no verb and no legend in the packet. The legend lives at `runs/harness_audit_2026-10-23/BRIEF.md:10-12` (criteria (a)/(b)/(c)), and the packet does not cite it (`:50` cites the directory only). `S` is defined nowhere that was found |
| same | R2 (advisory) | :43-46 | The "Report back" imperatives have no named actor; the addressee is implied by the header |

**Exemplary (no violation):** the WATT ASK `:10-13` (one ACTION, actor named, three enumerated options, Will's words quoted verbatim with the record path at `:3`). The WQ-508 P01–P13 Direction cells (verb plus exact replacement text). The WQ-508 `:3` ruling quote.

**Totals by rule:** R1 ×2 · R2 ×7 (1 shared with R3, 1 advisory) · R6/6b ×1 · R8 ×2 · R10 ×1. That is 13 across 5 packets, of which 5 are in the 2 current live DAEDALUS packets and the NEXUS packet.

---

## Proposed fix text (inside the three BLUEPRINTS files only)

| Fix | Defect | File:line | Exact change |
|---|---|---|---|
| F1 | 1-1 | STATE_VOCABULARY.md:216 | Replace `(pending mint, 8/28 register ②)` with `(MINTED 2026-08-28, wiring-sweep ②; defined at Class 8)` |
| F2 | 1-2 | STATE_VOCABULARY.md:264 | Replace `the CHECK_STANDARD §8 glyph-vs-count rule (pending encode, sweep-input ⑤b) is the mechanism-side twin` with `CHECK_STANDARD §8 rule 6 (GLYPH-VS-COUNT, RULED 2026-08-21, \`0416eaa40\`) is the mechanism-side twin` |
| F3 | 1-3 | STATE_VOCABULARY.md:157 and :261 | At `:157` replace `**until WQ-147 (M1, Will 2026-09-01) lands, which extends the same recognition to \`--all\`**` with `**and, since WQ-147 M1 shipped 2026-09-01 (\`b5494ecac\`), \`--all\`/\`--days\` too (declared-quiet ledgers print ℹ️ and are not counted stale)**`. At the end of the `:261` reader cell, append `; \`--all\`/\`--days\` since 2026-09-01 (WQ-147, \`b5494ecac\`)` |
| F4 | 1-4 | STATE_VOCABULARY.md:51 and :64 | `:51` meaning becomes `Deliberately disarmed BEFORE any fire (carry the ruling). Distinct from NOT-FIRED. After a fire the condition stays \`FIRED\`; the disarm is \`Response: STOOD-DOWN\`.` At `:64` replace `\`FIRED → STOOD-DOWN → ARMED (re-armed <date>)\`` with `\`FIRED\` (+ \`Response: STOOD-DOWN <ruling>\`) → \`ARMED (re-armed <date>)\` at the next evaluation` |
| F5 | 1-5 | STATE_VOCABULARY.md after :249 | Add: `**Same spelling, different cell:** \`UNKNOWN\` here = no check run on a claim; Class 5 \`UNKNOWN\` = an unmeasured quantity cell; a gate/closeout verdict \`UNKNOWN\` = the check cannot certify (CHECK_STANDARD §9 rc 2). Likewise Class 1 \`RETIRED\` (surface ended by decision) ≠ CORRECTIONS.tsv \`RETIRED\` (= \`CLOSED-VERIFIED\`, Class 11). A reader keys by COLUMN, never by the token alone.` |
| F6 | 1-6 | STATE_VOCABULARY.md, new class after Class 13 | `## Class 14 — Threshold revision policy (registered from STRICT_TEXT rule 7; ruling PROME/proposals/2026-08-12_rule-batch-RULED.md row 36b)` with a table: `GRADE-AT-PUBLICATION` (default; never re-opens) · `GRADE-ON-REVISION` (a revision that newly crosses COUNTS AS A FIRE) · `REGRADE-ON-REVISION` (re-grades from scratch; may un-fire) · post-fire `STAND-WITH-ANNOTATION` (default for an already-fired row). Definitions cite STRICT_TEXT rule 7 and do not restate it |
| F7 | 1-7, A5-2 | CHECK_STANDARD.md after :83 | Add two bullets. (1) `**rc ≥ 3:** a producer-declared not-clean state (§8 rule 3: served-but-not-fresh, e.g. \`cot_gold.py\` rc=3). A consumer reads any rc ≠ 0 as not-clean, and any rc ∉ {0,1} with no docstring mapping as cannot-certify.` (2) `**Harness hooks:** a hook follows the harness's exit semantics (Claude Code: 2 blocks the tool call). A hook-mode always-0 is legal only when declared at the site (§6) AND a §9-conformant non-hook mode (\`--selftest\`/\`--check\`) exists.` |
| F8 | 1-8 | CHECK_STANDARD.md:47 | Replace `\`CHECKS.tsv\` gains a per-check on-FAIL column at the next register pass (PAT-084).` with `\`CHECKS.tsv\` carries it in the \`On_FAIL (PAT-084)\` column (filled at the 2026-08-17 register pass).` |
| F9 | 1-9 | CHECK_STANDARD.md:114 | Replace `\`builds/REGISTRATION_CHECKLIST.md\` picks it up for new builds.` with `\`builds/REGISTRATION_CHECKLIST.md\` row OWED — absent 2026-10-28 (grep \`prior.art\|§13\` rc=1).` |
| F10 | 1-10 | CHECK_STANDARD.md:92 | Replace the bullet with `**Retroactive leg:** planned for the 2026-08-28 wiring sweep; no self-inclusion leg found in \`runs/2026-08-28_WIRING_SWEEP/\` (SEARCH-NOT-FOUND 2026-10-28). DAEDALUS cites the run record or re-registers the leg with a date.` |
| F11 | 1-11 | CHECK_STANDARD.md:87, :94, :109, :118 | After each `PROVISIONAL`, append `— ratify trigger MET (first live application: \`scripts/validate_all.py\`, 2026-09-10); ratification owed via PROME`. For §14 use `scripts/ledger_staleness.py:792`. This is a text-state fix only; ratifying the sections is Will's decision |
| F12 | Leg 4 | STATE_VOCABULARY.md, Class 9 extension | Add `### Class 9 extension — glyph register (declaration: USER.md § Decisions and Attention; this table is the registration USER.md:80 requires)`. It has one row per glyph: ⚖️ · ATTENTION · 🟢🟡🟠🔴 (pointer to the root Status key) · ⛔ · ⚠️ (**prose:** travelling caveat; **script output:** state-dependent degradation, and a standing caveat prints `NOTE:` per CHECK_STANDARD §8 rule 5) · 🧊 · ★ · ✅/❌ (**prose:** resolved true/false; **verdict line:** CLEAN/BLOCKING). Each in-use unlisted glyph (⏰ ❓ ✍️ ℹ️ ⭐ 🔨) gets a row or a `retire on next write` note |
| F13 | Leg 3 | STATE_VOCABULARY.md, new pointer class | `## Class 15 — DAEDALUS register enums (pointer class; local canon at each header, PAT-015)`. Rows: FLEET_MAP Level `L0`–`L5` + `RETIRED`, Conf `H/M/L` → `FLEET_MAP.tsv:38-39` · PATTERNS Type `PATTERN/ANTI`, Conf Admiralty `A1..C3` → `PATTERNS.tsv:2` · SURFACES State → `SURFACES.tsv:4` · CHECKS invocation state → `CHECKS.tsv:3` · sweep status `active/paused` → `sweeps/REGISTRY.tsv:8` · gate verdicts `CLEAN·DUE·ADVISORY·BLOCKING·UNKNOWN·NOT-APPLICABLE·ENUMERATED·DECLARED` + `WITH-DEBT` → `design/2026-09-17_DAEDALUS_GATE_SPEC.md:15-21`. This discharges the extension `CHECKS.tsv:3` has owed since 2026-08-03 and makes `CLAUDE.md:117` satisfiable |
| F14 | H-1 | STATE_VOCABULARY.md:253-271 | Re-sort the map rows by class number and merge the duplicate 1/2/8 rows into one row per class (sub-bullets for extensions) |
| F15 | H-2 | CHECK_STANDARD.md:107 | `**C5 — …**` → `**(a) SPECIFIED-BUT-NONEXISTENT … (WQ-254 C5/D1, …)**` |

F6, F12 and F13 add classes. Under STATE_VOCABULARY's own scope (`:11`), minting is the owner's job. F6 registers tokens that were already ruled (2026-08-14). F12 and F13 are pointer classes that mint no new meaning. DAEDALUS decides whether any of them needs PROME or Will's sign-off.

## Routing candidates (ranked; defects owned outside BLUEPRINTS)

| Rank | Sev | File:line | Defect | Owner |
|---|---|---|---|---|
| 1 | MED | `AGENTS/DAEDALUS/sweeps/REGISTRY.tsv:12` | last_run 2026-09-04 and last_findings omit 4 SERVICE commits (09-07, 09-08, 09-24, 10-14), contrary to the row's own "serviced at any spawn that touches any registry" rule | DAEDALUS (the live session has this file dirty) |
| 2 | MED | `AGENTS/DAEDALUS/CLAUDE.md:117` | The charter requires STATE_VOCABULARY tokens in FLEET_MAP/SURFACES/PATTERNS/sweep-verdict cells, and no class exists for them. Pair with F13, or narrow the sentence to "canonical or class-15 local tokens" | DAEDALUS (charter) |
| 3 | MED | `AGENTS/DAEDALUS/SURFACES.tsv:3, :5, :9, :12-15, :17` | 7 cells off the header enum `:4`, and the `:3` comment row starts with `"#` so it parses as data | DAEDALUS |
| 4 | MED | `AGENTS/DAEDALUS/CHECKS.tsv:22, :31, :36, :40, :60` | 5 State cells off the header enum `:3` (RETIRED, WIRED-MANUAL, BUILT-UNWIRED, 2 compounds) | DAEDALUS |
| 5 | MED | `PROME/inbox/processed/2026-10-23_from-DAEDALUS_WQ508-harness-audit-lines.md:13-26` (and the 37 desk copies) | Direction codes with no verb or legend (R2/R3). Desks applying lines cannot decode `a`/`c`/`S` without the brief. Fix forward in the packet template; a one-line legend follow-up to the 38 recipients is optional | DAEDALUS |
| 6 | LOW | `USER.md:75, :78` vs `CHECK_STANDARD.md:72`, `scripts/daedalus_gate.py:51` | ⚠️ and ✅/❌ carry different meanings in prose and in script output. Pairs with F12; USER.md may want a "script output: see STATE_VOCABULARY Class 9 ext." clause | Will / PROME (USER.md) |
| 7 | LOW | `scripts/corrections_boot_check.py:24,31` · `AGENTS/DAEDALUS/scripts/walter_route_check.py:28,33` · `PROME/tools/table_check.py:34` · `AGENTS/DAEDALUS/CHECKS.tsv:40` | Citation spelling is not `§N`, so `grep '§9'` misses these during a §9 consumer survey | DAEDALUS (scripts/, CHECKS); PROME (PROME/tools) |
| 8 | LOW | `scripts/pipeline_rc_guard.py:81` | Always-0 hook mode cites §9 with no declared carve-out. Pairs with F7 | DAEDALUS (scripts/) |
| 9 | LOW | `AGENTS/DAEDALUS/outbox/delivered/_FROZEN.md:3` | The banner says 26 files; 28 are present. Two 2026-09-02 packets were added 2026-09-24 (`bf9823d6b`) to a FROZEN surface | DAEDALUS |
| 10 | LOW | `AGENTS/DAEDALUS/CLAUDE.md:118` | Restates §3 as "Three instances in four days … caught the fourth", but the canon at `CHECK_STANDARD.md:33` says "Four instances in five days; first use caught the fifth" (cite-don't-restate drift) | DAEDALUS (charter) |
| 11 | LOW | `PROME/tools/will_handbook.py:17` | Calls §13 a "draft norm, honored voluntarily" | PROME |
| 12 | LOW | `AGENTS/DAEDALUS/sweeps/REGISTRY.tsv:8` | The column comment omits `resolve_by`, which header `:1` carries | DAEDALUS |
| 13 | ADVISORY | `AGENTS/YURI/workbook/INTENT_LEDGER.tsv:5` | `VOID` used for a prospective supersession (Class 3 VOID = premise failed). Conformant in form; the gap is in Class 3 (no withdrawn/superseded token) | YURI (no action); DAEDALUS (Class 3 gap, consider at next mint) |
| 14 | ADVISORY | `AGENTS/NEXUS/…` packet `2026-10-24_from-NEXUS_L40-…md:3,:15` | R10 paraphrase; R6/6b missing unit/object on "15 · 6 · 8 over 29" | NEXUS (next-write) |

## Not read / coverage limits

- **Concurrent writer.** A live DAEDALUS session moved HEAD from `c6d77fc1f` to `0d769a634` and edited `FLEET_MAP.tsv` (ISHM `L0`→`L2`, CYPHER row), `CHECKS.tsv:11`, `sweeps/REGISTRY.tsv:19` and the inbox during this run. The leg-3 counts were re-run after those edits (FLEET_MAP Level L2 = 4, no `L0`). The off-enum findings are unchanged. The three BLUEPRINTS files had no working-tree changes (`git status --porcelain` clean for `BLUEPRINTS/`). md5 at write: STRICT_TEXT `c73c2ee4…`, STATE_VOCABULARY `1cefa987…`, CHECK_STANDARD `81a0388a…`.
- **Leg 6 population.** 1 inbox packet existed (the brief expected 4). The outbox top level is empty apart from the FROZEN `delivered/`, so its two newest files are 2026-09-02 history. The two supplementary live packets were my substitution. Of the 38 WQ-508 copies, only the PROME copy was read.
- **Not read:** `STATE_VOCABULARY_PROVENANCE.md` (grep only); the bodies of the `[[finding_…]]` memory slugs cited in STRICT_TEXT and CHECK_STANDARD (resolution not checked); `PROME/proposals/*` ruling records (grep only, apart from the ratification search); `design/2026-09-17_DAEDALUS_GATE_SPEC.md` beyond `:15-21, :41, :74`; `daedalus_gate.py` beyond `:35-75` and greps; all 73 CHECK_STANDARD citation lines were checked for section existence only, not for whether the citing code complies with the cited section (the exception is A5-2).
- **Absence claims** (1-9, 1-10, 1-11) are `SEARCH-NOT-FOUND`, each with a positive control and a bare rc. None has been upgraded to `VERIFIED`. One search during this run hit the §14 box fact: a pattern with `.{0,40}`/`.{0,80}` returned rc=2 under ugrep and was re-run in a different form, never read as absence.
- **Self-scope (CHECK_STANDARD §10):** DAEDALUS's own directory is IN scope and was read (registers, scripts, charter lines, outbox, runs).
- **What this report does not prove:** owner consumption of any packet; the external truth of any figure; whether the fixes above are approved. Leg 5 "CLEAN" proves section existence, not compliance.
