# NEXUS files sweep — 2026-10-24 (Will: "do a sweep of NEXUS files and review/offer feedback")

**Method.** Three fresh-context Opus readers, read-only, each over a disjoint slice (A charter · B brief-standard surfaces · C live boards + records); NEXUS ran the mechanical scans (census, 60-day ages, 66 cited paths, READS manifest, scripts) and spot-checked every ❌ below at the artifact before it was written here. Reader ledgers: `SWEEP_A_charter.md` · `SWEEP_B_briefs.md` · `SWEEP_C_boards.md` (this directory). **VERIFIED** = NEXUS re-read the quoted line/row; **READER** = reader's finding, not independently re-read (treat as a claim until the fix pass opens the file).

| Slice | ❌ broken / wrong | ⚠️ stale / owed / incomplete | ✅ working | Grade |
|---|---:|---:|---:|---|
| A — charter `CLAUDE.md` (71.8 KB) | 3 | 19 (+5 💡) | paths 62/66, disciplines A–J complete, guards runnable | **D** on "rules only": ~30–35% history |
| B — schema · template · BRIEFS_MAP · brief_health · fallback log | 8 | 15 | 11 (cadence, budgets, census 29 = 29, pin tool) | schema behind its own amendments |
| C — STATUS · CONFIRMED · COLD · LAST_COMPLETION · board_log · dirs | 6 | 17 | 14 (all 12 crc32 recompute; every FRED mark + distance recomputes; docket dates in future) | record sound, two boards drift |

## 1. What is working (keep)
- **The record is sound.** Every crc32 quoted on STATUS / LAST_COMPLETION recomputes against the cold files (12/12); every FRED mark, threshold distance and L13/L16 cell date recomputes from the raw pulls; no catalyst-docket date is past; weekday check clean; corrections / orphan / read-cap checks all rc 0 (VERIFIED).
- **Pointers resolve.** 62 of 66 charter-cited paths exist; the 4 misses are labelled history or a deliberately absent path. All 9 `§H` pointers on STATUS resolve. The one dead pointer class is history blocks naming packets PROME has since moved to `processed/` (expected, not a defect).
- **Letters are actionable.** L13 / L16 / L17 / PRED-38 / 41 / 45 each carry instrument, numeric edge, due date, home; GATES mirrors agree; the DOCKET wake rows NEXUS depends on (L554 · L555 · L572–L574 · L630 · L632 · L751 · L832) match STATUS (VERIFIED).
- **Brief standard mechanics:** census on disk = map (29); no brief over budget (largest BRENT 23,010 B); pin tool output today = the map's 10/23 transcription; rollup cadence kept (#5 9/29, #6 docketed 10/27). Rollup #6's cause mix is already computed (SWEEP_B): 17 fallback rows 10/01–10/23 = stale 16 · convergence 1 · uncertainty 0 · brief-gap 0; LIQUID 7 stale, BROCK 5.

## 2. BROKEN / WRONG (fix in one Standard correction commit)
| # | Where | Finding | Status |
|---|---|---|---|
| 1 | `CONFIRMED.md:4` | "Full C-ID index" points at `recon/2026-06-06_c_id_index.md`, a 6/6 snapshot whose C-35 / C-36 names clash with this table (there: fertilizer / employment trap; here: Iran bull-trap / real-duration channel) | READER; pointer existence VERIFIED |
| 2 | `CONFIRMED.md:18` | "the stale half is struck above" — the file has no strikethrough | VERIFIED (grep) |
| 3 | `CONFIRMED.md:18` | T6 / T7 successors still "frozen, pending, hard close 8/29"; T6 graded NO-VERDICT 8/30 (`STATUS_COLD.md:240`), T7 outcome never recorded | VERIFIED (COLD line) |
| 4 | `STATUS.md:106` | PRED-41 wake filed in the 11/20–11/24 row as "~mid-Nov"; DOCKET L575 is 11/06 (a placeholder inside "early November") and PREDICTIONS says "~early Nov" | VERIFIED |
| 5 | `STATUS.md:25` | M-10 carried at 25% with "no letter" since L11 closed 10/20 — a standing number with no falsifier (Disc-J); needs a successor letter (Sept TIC, mid-Nov) or the "judgment, no number" label M-06 uses | VERIFIED |
| 6 | `LAST_COMPLETION.md:11` | today's block labels the STATUS rotation "§H23–§H23E" but lists six crc32 values (the sixth is §H23F) | VERIFIED |
| 7 | charter CLOSEOUT tiers | **9a rollup is HEAVY-tier only, but its DOCKET row (L555, 10/27) lands on the Tuesday wake the charter defines as a SHORT boot** — read literally the rollup is skipped on the day the row exists to force it | READER; tier table text VERIFIED |
| 8 | charter CLOSEOUT 15b | the DOCKET-wake packet step is in no tier; a Standard closeout that registers a dated letter has no step that packets PROME | READER |
| 9 | `PROME/registry/READS.tsv` rows 352–356 | still say root 1b–1e run "at Standard+"; the charter struck that on 10/1 (they run at every session-end commit); attestation dated 9/29 against a 62,587 B charter, now 71,849 B after 10/1 · 10/8 · 10/19 · 10/23 edits; manifest also lacks `brief_pin_check.py` (BOOT 6) and names the digest readers "Opus", census "27" | VERIFIED (row 352 text; sizes) — **PROME owns the file; NEXUS packets a re-attestation** |
| 10 | `templates/NEXUS_BRIEF_SCHEMA.md` | the LOCKED schema never had R3 amendments 1–3 written in: §2 still says cross-agent tensions "optional" (line 75), the forward section is still `## WATCH` (line 93), no "Recent thesis pivot" line; amendment 9's COMPACT form exists only in the cold archive; the "pin-token ruling stays HOT" sentence (line 294) points at text that is in the cold file. The template applies 1–3 correctly but says the schema wins on disagreement — so the out-of-date file overrules the correct one | VERIFIED (lines 75, 93, 294) |
| 11 | `BRIEFS_MAP.md` legend | "a stale pin is NOT an (a) trigger if content is fresh" contradicts schema §4.4 and the charter ("mechanical / always fires") — a rule living only in the map | READER |
| 12 | `BRIEFS_MAP.md` section-order table | "read the state HERE" table is the 9/07 measurement (4/13/9 over 26); disk today 15 new-order / 6 old / 8 n-a over 29; omits YURI · CYPHER · GIBBS; VIOLET and OSPREY shown as lacking CROSS-DOMAIN though both now lead with it | READER |

## 3. STALE
- **PROME mirror rows lag NEXUS (packet owed, never sent):** DOCKET L631 still lists M-04 + its "~3pp-high flag" (fired 10/19, flag cleared 10/20); **L752–L754 status cells still say "PROVISIONAL anchor not yet qualified"** (qualified 10/19, read 10/23) — VERIFIED. **DOCKET L40** (amendment-12 watch, NEXUS co-owner) due 10/12, slated to Will 9/18, 12 days overdue, on no NEXUS board — VERIFIED.
- Charter: WALTER BOARD spec cited "v0.32 at 9/29" (header now v0.35; the charter does say read the header) · "DOCKET L555 = 2026-10-27" hard-coded · "Last full matrix review" header label no longer exists on STATUS · WHAT YOU READ names "(WALTER, OZK)" while BOOT 6 says membership is never listed here · STATUS overflow home given as both `STATUS_COLD.md` (closeout 9) and `research/` (OUTPUT RULES); `STATUS_COLD.md` and `analysis/` absent from WHAT YOU OWN.
- Briefs: BROCK brief 8 days / 5 STATUS commits behind; LIQUID 4 commits behind (7th consecutive stale pass, the map says "6th"); 4 UNPINNED (BOND · CORAL · LIQUID · WATT); CORAL's "rides the same commit" claim is false at git; ORACLE / SHADE pins are pointers not hashes; template's worked example (SAM) has reverted to the old section order; template stamp uses the banned `~HH:MM` form; the map calls YURI Tier-2 (ROSTER: ACTIVE since 9/19) and a history line lists SHADE brief-less, CRUISE/FERT dormant (all wrong today).
- `BRIEFING_2026-08-29_SYSTEMS_REVIEW.md` (top-level, 12 KB): "🔴 READ THIS FIRST … NOT STARTED" banner is false (first leg delivered 9/02, DOCKET L206); unreferenced; retirement-eligible 10/28.
- Typed `HH:Mx` clocks (banned by the stamp rule on graded records): 3 on STATUS incl. the header, 7 on LAST_COMPLETION, 1 on PREDICTIONS, 67 board_log rows 8/12–9/17 — mostly pre-rule history; the 10/24 header one is mine and fixable.
- `board_log.tsv`: 5 rows (10/19) with source `WALTER` not `INBOX_WALTER` and glued words; 5 `deferred` rows whose resolvers passed with no closing row (rows 6 · 52 · 60 · 107 · 108; 118 and 128 are also resolved in fact — charter cold-read-2 fixed 10/1, S1 design delivered 10/8).

## 4. OWED
- **Mon 10/26 DOCKET L832** read (M-03 decision, L16 cell 4, L13 cell 5, M-04b/M-08b anchors) — STATUS at 22,779 B = 6 B under the stop, so **rotate first**.
- **Tue 10/27:** L554/L751 (L16 cell 5) · **L555 rollup #6** — numbers above; the rollup must also report **pin coverage** (made standing by rollup #4, skipped by #5): hash present in 12 of 29 headers, 24 of 29 pass the pin check, 3 of 29 use the canonical token.
- **M-10 successor letter or re-label** (Disc-J, ❌5). **M-06** disposition 10/29 (L630).
- **READS re-attestation packet to PROME** (❌9) and the **L631 / L752–L754 / L40 mirror packet**.
- **Schema repair** (❌10) — the schema is 32,443 B = 99.7% of budget, so its §5 history must move cold BEFORE any text is added; a repair of already-ratified amendments is not a new amendment (cap 12 of 12 stands) — but say so in the packet to PROME and let it rule if it disagrees.
- Charter: tier-table repair so dated/triggered steps (9a · 15b) run at any tier when due (❌7–8).

## 5. INCOMPLETE / MISSING
- Charter is ~33k tokens, over the 54,250 B single-read cap — fine when harness-injected, **not readable whole on the PROME-spawn path** (READ_CAP rule 20 exempts injection only). ~22–26 KB of it is provenance narrative ("Why, measured 9/29 …") that the root says belongs in a provenance companion. Charter also lacks: a default for "multi-day" in BOOT 6; one "do this FIRST"; the `USER.md` path is ambiguous (root only).
- Schema: no COMPACT skeleton (8 briefs lack CROSS-DOMAIN incl. HENRY · LIQUID · BOND, which are not the utility class amendment 9 covered; LIQUID matches neither form).
- `outbox/` and `signals_archive/` carry no RETIRED banner though the charter calls both retired (SIGNALS.md does have its FROZEN banner).
- `brief_fallback_log.tsv`: the `uncertainty` cause has never been logged; digest rows logged under three agent names (FLEET / ALL / DIGEST); direct owner reads mostly unlogged (10/23: 8 read, 3 logged) — so a zero brief-gap rate may be an instrument that can no longer record one.
- CONFIRMED C-35: "ungradeable, no new date" has had no resolver since 9/17.

## 6. INACCURATE (small, on their face)
- STATUS Trading line "Nearest refuter KRE $72.74" drops the direction (TERRY: KRE *reclaims* $72.74, above the $72.46 close). STATUS M-09 "DOWN dead" gives no reason (LIQ-069 FIRED-not-released 10/15; PREDICTIONS L15 has it). LAST_COMPLETION's 12:32 "CLOSED OUT" line sits above today's 15:19 block and reads as current.

## 7. Retirement candidates (root Data Hygiene: >60 d · not boot-read · no live reference)
Eligible now: `research/2026-08-12b_falsifier_base_rate_audit.md` (72 d) · `research/2026-08-12_split_falsifier_RESOLUTION.md` (68 d) · six of seven `signals_archive/*` · the nine 6/27–7/22 `outbox/delivered/` packets. Eligible after a fix: `recon/2026-06-06_c_id_index.md` (once CONFIRMED ❌1 stops pointing at it). Eligible 10/28: the BRIEFING file · `signals_archive/PREDICTIONS_PASS_LOG_20260627_20260724.md` · `research/2026-08-28_successor_falsifier_RESOLUTION.md`. **Keep:** `research/2026-08-03_split_and_coverage_prereg.md` (Disc-J's worked example, cited by the charter). Optional: 81 of 259 processed-inbox files are >60 d (processed/ is the archive by design; leave).

## 8. Proposed fix order (each is one commit; nothing below moves a letter, Conf % or the split)
1. **Standard correction commit (today if Will says go, ~30 min):** CONFIRMED ❌1–3 + C-35 resolver line · STATUS ❌4–5 + KRE direction + M-09 reason + the typed-clock header stamp · LAST_COMPLETION ❌6 + CLOSED-OUT line placement · board_log 7 deferred rows closed with dated dispositions · RETIRED banners on `outbox/` and `signals_archive/` · `git mv` the eligible-now research files to `archive/`. Cold read not required (no whole-file rewrite) unless CONFIRMED is restructured.
2. **PROME packet:** READS re-attestation (❌9) · L631 / L752–L754 wording · L40 status · the schema-repair-is-not-an-amendment position.
3. **Schema repair (HEAVY, cold-read):** rotate §5 history cold; write in amendments 1–3, COMPACT skeleton, pin-token ruling, read-time carve-out; drop the map's legend override; regenerate the map's section-order table with a form column. Probably Monday after the L832 read, or a separate session.
4. **Charter hot/cold split (HEAVY, cold-read, Will-gated as a charter rewrite):** move ~25 KB of provenance to `CLAUDE_PROVENANCE.md` (or `docs/CANON_PROVENANCE.md` style), rebuild the tier table so dated/triggered steps run when due, fix the 19 ⚠️. Target under 45 KB. Needs a fresh-counterexample reader after, per `[[finding_a_correction_pass_is_unreviewed_work]]`.
