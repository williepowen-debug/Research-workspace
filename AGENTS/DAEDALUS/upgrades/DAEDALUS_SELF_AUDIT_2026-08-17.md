# DAEDALUS SELF-AUDIT — 2026-08-17 (Will-directed reflective analysis)

**Status: AUDIT COMPLETE — findings verified, fix batches PROPOSED, ZERO fixes applied in-audit (deliberate: state frozen for PROME's independent pass + Will's batch ruling).**
**Commission:** Will, in-session: "Recently we did a bunch of upgrades to Prome's system. I'd like to do a similar reflective analysis on DAEDALUS system and file structure too."
**Method:** 5-reader Mode-A fan-out over my own tree (spine · registers · blueprints · work-product · tooling+lifecycle), all read-only. Companion (PAT-100): `DAEDALUS_SELF_AUDIT_2026-08-17_READER_REPORTS.md` — all 5 raw reports + NOT-READ lists, verbatim.
**Concurrent review:** PROME (session 4, Will-directed) ran an INDEPENDENT blind pass (completed before my doorbell) then cross-read all 5 reader reports; feedback packet `inbox/2026-08-17_from-PROME_self-audit-cross-read-four-additive-findings-plus-synthesis-priorities.md` (d3b01acd8) CONSUMED and folded below — convergence record: PROME's blind route independently hit the STATUS byte overrun, EVOLUTION-as-uncapped-sink, the missing archive/, and the registers-as-logs theme. PROME's 4 additive findings verified at artifacts by me (F37/F38 + two standards proposals) before folding.

---

## §V VERIFICATION (synthesizer battery, run before synthesis)

10 probes against the highest-severity reader claims, ALL CONFIRMED at the artifact: ① STATUS.md = 100,051 B / 133 lines (wc) ② EVOLUTION's seven 8/17 entries at `##` level, lines 313–337, below `## Roadmap` (grep) ③ meta-agent.md:50 asserts the YEYOU per-push feed as fact (grep) ④ zero `CHECK_STANDARD` citations in all 3 variants + REGISTRATION_CHECKLIST + my charter (grep -rln) ⑤ PATTERNS `Type` column = 69 PATTERN / 22 ANTI / 20 topical free-text (awk|uniq -c) ⑥ SURFACES SIGNALS row stale vs the FROZEN banner live at `SIGNALS/README.md:3` ⑦ `maturity_scan` invocation sites = FILES-table mention only, no executable step (grep) ⑧ own FLEET_MAP row `Last_scored 2026-08-12` (awk) ⑨ `AGENTS/templates/` does not exist; charter :120 still carries the maintain-the-template obligation (ls + grep) ⑩ `sweeps_due.py:7` "Exit code is always 0" (grep).
One reader error found + preserved in the companion: reader-tooling's NOT-READ list calls STATUS "~49KB" (actual 100,051 B). Reader-spine's 14-sample claims-vs-artifacts check: 12 VERIFIED / 2 FAILED. Reader-blueprints' 12-encode reconciliation: 12/12 VERIFIED.

---

## §1 VERDICT

**The honesty layer is strong; the self-application layer is the defect mass.** Every encode claim, every named artifact, and 12 of 14 sampled side-effect claims verify at the artifact — the register does not lie about what it did. What it does instead is **exempt itself from its own enforcement**: the byte-tier convention I authored and Will ratified this week is violated 3.9× by my own STATUS; the silent-fallback-green class I swept 41 fleet scripts for this morning has two watched instances in my own `scripts/`; the two-state banner discipline my Staleness Sweep enforces fleet-wide is unmet by ~38 of my own documents; the "invocation, not detection" diagnosis I published at n=3 (SAM/BRENT/PROME) is n=4 — the fourth is me (charter has no closeout sequence; SURFACES.tsv has no reader; maturity_scan has no invoker; CHECK_STANDARD has no citation site).

Four defect classes, all classes I police:
1. **Self-exclusion from own enforcement** (scope habit): sweeps/standards systematically stop at my directory boundary.
2. **Readerless registers / unreachable standards** (PAT-108/PAT-071 at home): writers with no reading moment — SURFACES.tsv, PATTERNS (write-mostly, vocab forked 33 rows unnoticed), maturity_scan, CHECK_STANDARD.
3. **Record-placement defects:** EVOLUTION's newest-first contract defeated by its own last seven entries; Δ-banners buried mid-file; run logs out of order.
4. **Carried-assertion rot** (PAT-089's string-that-never-evaluates): Standing-capability figures 10d stale, 8 FLEET_MAP `Next_upgrade` cells expired/refuted/satisfied, false status lines on completed work, a wrong reference-commit in ratified canon.

**Self-grade: L4 HOLD, Conf H** — the honest-claims layer and the artifact discipline are L5-grade; the cadence leg (already the named blocker, failed 3×) is now joined by a second named blocker: **the self-application gap** — my closeout battery certifies COMMITTED, my sweeps certify the FLEET, and nothing certifies ME. Three of three PAT-050 instances were caught by directed audits, zero by my own closeout.

---

## §2 DEDUPED FINDINGS REGISTER

36 unique findings after cross-reader dedup (source-reader IDs in parens; S=spine, T=tooling, B=blueprints, R=registers, W=workproduct). Convergent finds (two+ independent readers) marked ★.

**CLASS 1 — Self-exclusion from own enforcement**
| F# | Sev | Finding | Sources |
|---|---|---|---|
| F1 | URGENT | STATUS 100,051 B = 391% of own ratified byte budget (25,600 B at cap 200), 752 B/line = fleet #2; +41% across the 2-day ratification window; archive rule unexecuted; BOTTOM LINE = 47 lines/32.6 KB vs the charter's "2–4 sentences"; EVOLUTION (the named sink) itself uncapped at 89 KB | S-D1, S-D8 |
| F2 | URGENT | Charter OUTPUT RULES lacks the byte tier that meta-agent.md:18 (my same-day edit) requires of Meta agents | S-D2 |
| F3 | HIGH | Charter contains NO closeout sequence — zero of root steps 1b–1e named; battery rides session habit; consumer_check absent even from practiced battery | S-D6 |
| F4 | HIGH | 8/17 SFG sweep scoped out my own scripts the same day; two watched class-hits live in my own dir (→F11, F14) | T-scope |
| F5 | HIGH | The 8/11 "13 unbannered docs" self-finding was fixed 4-of-13 and the residue has NO carrier (no debt row, no queue row); census NOW: ~28 stale-ambiguous in upgrades/ (16 cards, 8 with zero status token anywhere) + 10 unbannered builds/ subdirs records | W-D-1, W-D-4, W-D-13 |
| F6 | MED | Outbox workflow retired ~8/07 (76 packets direct-to-inbox since, 0 outbox copies) while charter :43 still mandates the outbox/delivered leg; delivered/ = dead ledger, unbannered — my own two-state violation | T-outbox |
| F7 | MED | Charter :120 obligates maintaining `AGENTS/templates/CLAUDE_TEMPLATE.md` — deleted by Will 2026-06-30 (58c30516f) | B-template |
| F8 | HIGH ★ | Own FLEET_MAP row 5d stale through the heaviest 5-day run on record — PAT-050 n=3, same 5d interval as the 8/12 instance; the 8/12 fix addressed the instance, not the mechanism | S-D5, R-D4 |

**CLASS 2 — Readerless registers / unreachable standards**
| F# | Sev | Finding | Sources |
|---|---|---|---|
| F9 | HIGH | SURFACES.tsv is READERLESS (no sweep, queue row, or script reads it) → 4 of 11 rows false/stale at artifacts: SIGNALS `DEAD-UNBANNERED` (banner exists since 8/11), scripts/ self-contradictory + gap closed by CHECKS 8/3, MESSAGING re-check trigger fired 8/16 unserviced, FORGE `SCHEDULED` on a window closed 15d with fix absent from code | R-D5, R-D6, R-D12, R-D13, R-reader-map |
| F10 | HIGH | maturity_scan.py — the scripted maturity floor — is invoked by NOTHING; CHECKS.tsv scope note excludes agent-local checks on a predicate ("invoked by their owner's own boot") that is false for my own scripts; my 4 local scripts sit in no register | T-D-01, T-D-06 |
| F11 | HIGH ★ | sweeps_due.py — my ONLY boot-invoked check — is a watched §8 class-hit (corrupted registry → `✅ none due (0 tracked)` rc=0, warnings stderr-only; missing registry → nothing) + §9 always-0 producer + broken rows silently drop from the tracked count + ZERO capable-case evidence ever; PAT-110's twin, unswept the day PAT-110 was banked | T-D-03, R-D10, R-D17 |
| F12 | HIGH | CHECK_STANDARD.md (twice Will-ratified) has ZERO citation sites — no variant, checklist, or charter reference; AND my charter's ★ rule is a hand-copy of §3 that has DRIFTED on clause (b) (text property vs execution property) — the restate-vs-cite failure I police | B-B2, B-restate |
| F13 | HIGH | PATTERNS.tsv controlled vocabulary FORKED: Type 91 PATTERN/ANTI vs 20 topical, interleaved (078–110); Conf mixes Admiralty and H/M; no dedup/merge/supersession convention (6 overlap clusters incl. PAT-025 = a frequency note about PAT-023); write-mostly at 154 KB — nothing re-reads old rows; PATTERNS absent from my own token self-binding list | R-D1, R-D18 |
| F14 | HIGH | render_directory.py co-registration guard is ONE-directional: ACTIVE agent in ROSTER absent from FLEET_MAP renders blank cells byte-identical to by-design dormant, rc=0, and the artifact's footnote teaches the blank as intentional; live trigger = PAT-047 order lands ROSTER first | T-D-02 |
| F15 | MED | falsification_scan: `--tsv` drops all four NOT-looked-at announcements (vs own docstring); no rc (exited 0 with 3 STALE-FLAGGED + 1 UNSTAMPED live, post-§9 material edit); typo'd `--agent` yields clean zero report; maturity_scan `sh()` swallows git failure → fleet-wide silent under-grade path | T-D-04, T-D-05, T-D-07, T-D-08 |

**CLASS 3 — Record-placement defects**
| F# | Sev | Finding | Sources |
|---|---|---|---|
| F16 | HIGH ★ | EVOLUTION's seven 8/17 entries (incl. §8 RATIFIED, §9 RATIFIED, byte-tier ratification) appended BELOW the Roadmap at `##` level, oldest-first — invisible to the file's own "Newest first" read protocol; already produced one lettering collision | S-D3, B-B5 |
| F17 | MED | SAM/BRENT 8/17 Δ-banners at :37/:81 while the whole 7/22 cohort banners at :3 — header still advertises superseded vintage | W-D-8 |
| F18 | MED | STALENESS run log out of chronological order; Production Review run #3 (largest on record) absent from its playbook's own Run Log; 2 REGISTRY last_run cells behind their own findings text (conservative direction) | R-D14, R-D7, R-D8 |

**CLASS 4 — Carried-assertion rot**
| F# | Sev | Finding | Sources |
|---|---|---|---|
| F19 | HIGH ★ | STATUS "Standing capability" asserts 10d-stale figures contradicted by the same file's header: PAT-090→actual 110; 36 rows→43(40); 34 profiles→35; directory 39→40 | S-D4, T-D-09 |
| F20 | MED | STATUS :68 asserts as forthcoming two events the same file records as done (Staleness ~8/15 → ran 8/11; PROME sweep ~8/18 → ran 8/16, L5 8/17) | S-D9 |
| F21 | HIGH | FLEET_MAP `Next_upgrade` rot, 8+ rows — the column rendered to Will/PROME: WATT+FALCON demand profile BUILDs that exist (one re-scored 8d after the build); CARL carries 2 clauses its own Notes refuted; 6 expired clocks (MIDAS/OSPREY/HOMER/AEOLUS/CREED/CARL — OSPREY re-scored 12d after its window shut); + Notes-only edit skipped Last_scored bump & directory regen (protocol step 7, no data defect this time) | R-D2, R-D3, R-D11, R-D16, S-D10 |
| F22 | MED | Two false status lines on COMPLETED work: wal_promotion PROMOTION_REVIEW "remains gated on WP-W0" (promoted 7/25); STE assessment "nothing built or wired" (both recs are root canon since 7/31) | W-D-5, W-D-7 |
| F23 | HIGH | Byte-tier REFERENCE IMPLEMENTATION cites the wrong commit in market-agent.md:99 AND EVOLUTION:331 — `bee36f441` (an inbox packet) instead of `3d2dd9707` (WATT's actual implementation) — the pointer a later adopter follows | B-B1 |
| F24 | MED-HIGH | Blueprint mirror-walk misses: meta:50 asserts the YEYOU per-push feed my own charter refutes (7/30, Will-confirmed); utility:72 lacks the 7/22 dormancy waiver (the variant holding candidate WALTER); meta:41 cites "11 rows" vs checklist's 16; PAT-103 in market only (PAT-031 sibling is in all 3) | B-B3, B-B8, B-B9, B-B7 |
| F25 | HIGH | STATE_VOCABULARY :112/:113 malformed table rows DROP content at render — including the 8/17 ⛔ correction stating basis_check never shipped, so the rendered table still asserts enforcement that does not exist; Class 6 Registry-obligation cell also vanishes (unescaped pipes) | B-B4 |
| F26 | LOW | Dangling pointers: 6 forum provenance paths wrong-from-birth in 2 STRICT-mode Will-ADOPTED specs; STATIC_BANNER_MARKERS pinned :108 (actual :136); HOMER RATES.tsv path missing `workbook/` ×3 | B-B6, B-B11, B-B12 |
| F27 | MED | Three EVOLUTION-declared "blueprint line queued" items never landed, tracked nowhere: PAT-060 (23d), PAT-061, PAT-069 (20d) | B-B10 |
| F28 | MED-HIGH | Meta-L5 rubric leg "EVOLUTION roadmap live" was never adjudicated at PROME's L5 promotion (PROME has no EVOLUTION.md; row Gaps never mentions it) and my own roadmap fails it (5-of-5 struck, forward items relocated) — either the leg is DAEDALUS-specific (rubric text wrong) or two grades skipped a named leg | S-D7 |
| F29 | LOW | SPEC drift (ladder cell + 4-file memory model superseded; "Phase 4 next" 7 weeks stale) while charter points readers at SPEC §5; UPGRADE_PROTOCOL card spec assumes market's 8 sections (meta has 9) | S-D12, S-D13, S-D14 |
| F30 | HIGH | Profile refresh queue mis-ordered vs measurement: WALTER is #1 by every measure (+24d past its own 20d rule, 391 commits — fleet-highest) yet sits 4th; ORACLE's clock EXPIRED 8/13 (flagged by my own registry text) and VIOLET/CORAL absent from the order entirely; BROCK banner's own re-check fired 20d ago; the correct rule ("work-volume-keyed") was banked 8/07 and never applied; AEOLUS (§3b queue-head) owed before Falsification #2 ~8/24 | W-D-2, W-D-3, W-D-9, W-D-10 |
| F31 | MED | PAT-100 contract ambiguity: SAM+BRENT 6-reader fan-out substance-compliant under 6 ad-hoc names — any filename-keyed check misreads it; war-triad has companion WITHOUT synthesis beside it (pair inverted); pre-PAT-100 fan-outs carry no grandfather note | W-D-6, W-D-12 |
| F32 | MED | No `archive/` dir; retirement rule never exercised here; ~20 docs cross the 60d line ~9/05–9/11 with no destination and no queue row (MARCO/SAM cards already 0-external-ref) | W-D-11 |
| F33 | MED | 33 of my packets sit unprocessed in recipient inbox roots, oldest 8/07 (HENRY ×2, BOND) — mostly captured by STATUS item ③, but the 8/07 HENRY pair predates that framing | T-inbound |
| F34 | LOW | CHECKS ledger_staleness row: run field carries the new rc contract, "what a PASS proves" field (the PAT-074 column) does not | S-D15 |
| F35 | LOW | One post-adoption PAT-101 rule-ii miss (383051aeb, 8/12); CHECK_STANDARD's own birth commit unpaired (pre-adoption) — record only | S-D11 |

**PROME-ADDITIVE (cross-read packet d3b01acd8, verified at artifacts by synthesizer):**
| F# | Sev | Finding | Sources |
|---|---|---|---|
| F37 | URGENT ★★ | **The boot spine is mechanically unexecutable as specified.** SPAWN steps 1–3 mandate reading STATUS (100,051 B) + FLEET_MAP (169,774 B) + PATTERNS (154,889 B) ≈ 425 KB — all 1.9–3.2× over the single-Read cap, so every boot silently degrades steps 1–3 to fragments/greps. TRIPLE live evidence, all same-day: reader-tooling's "~49 KB" STATUS misread (the signature of a truncated read — the defect measuring itself); reader-registers' 11-of-40 FLEET_MAP row coverage; MY OWN boot this session (STATUS Read truncated at line 66/134; FLEET_MAP and PATTERNS never read whole — wc + tail only). "Apply them; don't re-learn them" cannot execute against a file that can't be read whole. Consequence: rotating STATUS alone (F1) leaves 2 of 3 boot reads unreadable — {STATUS, FLEET_MAP, PATTERNS} is ONE fix class. | PROME-a (verified: wc = 424,714 B) |
| F38 | HIGH | FLEET_MAP.tsv total size (169,774 B — largest file in my tree, ~3.8 KB/row Notes cells) appeared in NO reader finding; the size is also the rot MECHANISM behind F21 — multi-KB history cells are logs nobody re-reads, so Next_upgrade decay survives inside them | PROME-b (verified) |

**PROME standards proposals (fold-or-rebut → FOLDED, both, as Will-gated drafts):** **(P-c)** self-inclusion as a MECHANISM property — every new sweep/enforcement/scope declaration must state whether the author's own dir is in scope, default IN; scope-honesty lines must enumerate own-dir as read-or-excluded (converts PAT-050 from re-learned pattern to inherited template property; evidence: every mechanism born since CLAUDE.md:43 carries the exclusion — byte-tier, SFG scope, CHECKS predicate, closeout battery). **(P-d)** no register ships without a named reader — a register's birth commit names its reading moment (who, what cadence) or it is born PAT-108 (would have blocked SURFACES, PATTERNS-drift, and CHECK_STANDARD-uncited at birth — three same-week instances).

**Verified-current (readers tried to break these and could not):** YEYOU box in charter still true · all 4 scripts exist · REGISTRY tracks exactly 11 · all 7 STATUS-named artifacts present with matching content · inbox filing "healthiest surface in the audit" (3 root packets all correctly HELD-BY-DESIGN) · TSV schema CLEAN fleet-register-wide (no PAT-093 recurrence) · all 11 sweeps inside cadence · blueprint numbering/token coherence CLEAN (all external §/Class/rule cites resolve) · render_directory FLEET_MAP→ROSTER guard works (watched).

---

## §3 ROUTE-LIST RECONCILIATION (PAT-102 / UPGRADE_PROTOCOL step — 25 reader route items → dispositions)

| Reader route item | → | Disposition |
|---|---|---|
| S1 byte budget + rotate + charter tier | F1/F2 | Batch A1 |
| S2 EVOLUTION reorder | F16 | Batch A2 |
| S3 self-row re-cut + mechanism | F8 | Batch A4 (row) + Batch B6 (mechanism) |
| S4 charter closeout encode | F3 | Batch A9 |
| S5 strike 2 stale STATUS blocks (+D7 rubric) | F19/F20/F28 | Batch A3 + Will-gate W1 |
| T1 render_directory reverse guard | F14 | Batch C2 |
| T2 sweeps_due fix | F11 | Batch C1 |
| T3 maturity_scan invocation + CHECKS scope → PROME | F10 | Batch C4 + flag P2 |
| T4 falsification_scan trio | F15 | Batch C3 |
| T5 outbox two-state + re-ping ≥10d packets | F6/F33 | Batch A9 + note P3 |
| B1 wrong ref-commit | F23 | Batch A2 |
| B2 CHECK_STANDARD cites + ★ drift | F12 | Batch A7 |
| B3 STATE_VOCABULARY malformed rows | F25 | Batch A7 |
| B4 meta/utility mirror-walk | F24 | Batch A7 |
| B5 EVOLUTION top + riders B6/B7/B10/B11/B12 | F16/F26/F27 | Batch A2 (+F27 → Batch B9 disposition) |
| R1 PATTERNS vocab canon + backfill + self-binding | F13 | Batch B2 |
| R2 FLEET_MAP Next_upgrade rot by pattern | F21 | Batch A4 |
| R3 SURFACES reader moment (queue row) | F9 | Batch A5 (rows) + Batch B1 (mechanism) |
| R4 own-row mechanism escalation | F8 | Batch B6 |
| R5 on-FAIL column + sweeps_due sweep | F34/F11 | Batch C4 + C1 |
| W1 unbannered-docs carrier + finish pass | F5 | Batch A6 |
| W2 queue re-head work-volume + AEOLUS pre-8/24 | F30 | Batch B3 |
| W3 two false status lines | F22 | Batch A6 |
| W4 PAT-100 contract decision | F31 | Batch B4 |
| W5 archive/ + retirement row before ~9/05 | F32 | Batch B5 |

All 25 accounted; zero dropped.

---

## §4 PROPOSED FIX PLAN (nothing executed — Will rules the batches; PROME feedback incorporated before execution)

**BATCH A — record/text fixes in my own lane, no behavior change (~1 session):**
- **A1** STATUS rotation per the ratified byte-tier convention (WATT reference form: dated archive file, crc at rotation, contiguous regions only): rotate the 14-paragraph BOTTOM LINE stack + the 8/07 and 8/11 body sections; set seat byte budget from measurement with on-surface rationale; add the byte-tier line to charter OUTPUT RULES. (F1/F2) **Per F37 this is leg 1 of the boot-spine wave — B0 carries legs 2–3.**
- **A2** EVOLUTION: move seven 8/17 entries into `## Changelog` at `###`, newest-first; fix `bee36f441`→`3d2dd9707` in market-agent:99 + EVOLUTION:331; carry riders F26 (6 forum paths, :108 pin, HOMER path ×3). EVOLUTION entry same commit (PAT-101 ii). (F16/F23/F26)
- **A3** STATUS stale current-tense blocks: Standing-capability figures re-cut; :68 cadence line struck/refreshed. (F19/F20)
- **A4** FLEET_MAP hygiene pass: self-row re-cut (L4 HOLD, new blocker named); WATT/FALCON/CARL Next_upgrade corrected; 6 expired clocks re-cut by pattern (sweep all 40 rows for date-tokens < today, not just the found 6); directory regenerated. (F8/F21)
- **A5** SURFACES: 4 stale rows corrected at their artifacts (SIGNALS/scripts//MESSAGING/FORGE — FORGE row gets an honest `UNMECHANIZED` + the manifest-build pointer). (F9 rows)
- **A6** Banner completion pass: ~28 upgrades/ + 10 builds/ one-line dispositions (cards → `🗄 ROUTED <date> — queue consumed, see FLEET_MAP row` or CLOSED; aged audits → dated-record banners); fix the 2 false status lines (WAL promotion, STE assessment); grandfather notes on the 2 pre-PAT-100 fan-outs. (F5/F22/F31-part)
- **A7** Blueprint mirror-walk (one pass, EVOLUTION same commit): strike meta:50 YEYOU feed assertion (cite the charter box); add utility:72 dormancy waiver; meta:41 11→16 rows; PAT-103 into utility+meta; repair STATE_VOCABULARY :112/:113 (merge ⛔ correction into the cell, escape pipes); add CHECK_STANDARD cite lines to all 3 variants + checklist row; replace charter ★ hand-copy with a cite to §3 (drift dies). (F24/F25/F12)
- **A8** Small records: SAM/BRENT Δ-banners moved to :3; STALENESS run-log reorder; PRODUCTION_REVIEW Run Log 8/07 row backfilled; 2 REGISTRY last_run cells; CHECKS ledger_staleness proves-field. (F17/F18/F34)
- **A9** Charter: closeout sequence encoded (cite root 1b–1e, don't restate; includes self-row currency + consumer_check — I publish figures others cite); outbox leg struck + `outbox/delivered/` FROZEN-bannered with the 8/07 cutover date; template-maintenance clause struck; SPEC given a one-line supersession pointer at its ladder/memory sections. (F3/F6/F7/F29)

**BATCH B — mechanism changes (PROME feedback in hand; Will where noted):**
- **B0** ★ **Boot-spine restructure, legs 2–3 (F37/F38 — Will-visible, PROME-endorsed):** PATTERNS → hot/cold split on the PROVEN auto-memory 7/31 pattern (hot one-line ≤80-char-hook index ≈9 KB boot-read whole + cold full rows; slug-conservation proof at migration); FLEET_MAP → current-state-only cells (Class · Level · Conf · Last_scored · bounded Next_upgrade ≈13 KB) with history/lineage prose relocated to `profiles/<AGENT>.md` or dated per-agent history files. Side effect: attacks F21's rot mechanism directly. Sequenced WITH A1 as one wave so all three boot reads become executable together.
- **B1** SURFACES reader moment: `Queue: surfaces-currency` row in REGISTRY @21d, serviced at Production Review. (F9 mechanism)
- **B2** PATTERNS governance: declare Type/Conf canon (STATE_VOCABULARY class or in-file header contract), backfill the 20 topical rows, add PATTERNS to my token self-binding list, adopt dedup-before-create + cross-ref the 6 overlap clusters (merge only PAT-025→023; others get `See also` links — history preserved). (F13)
- **B3** Profile queue re-head WORK-VOLUME-KEYED (the 8/07 rule, applied): WALTER → VIOLET → CARL → NEXUS → ORACLE(expired) → …; AEOLUS serviced before Falsification #2 ~8/24; BROCK re-check executed. (F30)
- **B4** PAT-100 contract disambiguated in UPGRADE_PROTOCOL: canonical `*_READER_REPORTS.md` filename REQUIRED; enumerated-cluster form allowed only WITH an index stub under the canonical name; war-triad gets a synthesis stub pointing at its STATUS block + packets. (F31)
- **B5** `archive/` stood up + retirement queue row @30d in REGISTRY before the ~9/05 wave. (F32)
- **B6** Self-row wake mechanism (the PAT-050 n=3 fix-form): sweeps_due gains a self-currency line — own FLEET_MAP row `Last_scored` vs own commit count since (file-readable trigger, not intention). Rides C1. (F8 mechanism)
- **B7** F27 disposition: PAT-060/061/069 queued-lines get a decision each (encode now in A7's pass, or explicit DECLINED-with-reason in EVOLUTION) — no third state.
- **B8** F33: note to PROME — recipient-side nudge for the 8/07 HENRY ×2 + BOND unprocessed packets (rides the existing recipient-side sweep ASK from the SAM/BRENT review).

**BATCH C — script fixes (each: consumer survey → edit → capable case WATCHED both directions → CHECKS/register row):**
- **C1** sweeps_due.py: warnings→stdout, skipped-count on the ✅ line, missing-registry loud, §9 rc (0/1/2; consumer survey: sole invoker is my boot read — no rc-keyed consumer, safe), + B6 self-currency line. (F11)
- **C2** render_directory.py: reverse co-registration guard — ACTIVE/TIER-2 in ROSTER absent from FLEET_MAP → `⚠️ UNGRADED` cell + summary line + rc≠0; footnote re-worded. (F14)
- **C3** falsification_scan.py: NOT-looked-at layer into `--tsv`; §9 rc; `--agent` validation (unknown name → loud). Consumer = sweep #3 playbook only. Before Falsification #2 ~8/24. (F15)
- **C4** CHECKS.tsv: on-FAIL column (owed since 8/11) + 4 rows for my local scripts. Scope-line widen = flag P2 (Will-approved register — not silently widened). (F10/F34)
- **C5** maturity_scan: `sh()` rc guard (git-fail → loud CANNOT-CERTIFY, no silent L2 collapse); invocation home = fold into Production Review §1 Detect (no new boot step — reader-tooling's recommendation adopted). (F10/F15)

**WILL-GATES (decisions only Will can make):**
- **W1 (F28):** Meta-L5 "EVOLUTION roadmap live" leg — is it Meta-class (then PROME's L5 confirm at run #2 ~9/6 must adjudicate it) or DAEDALUS-specific (then the rubric text in charter + SPEC gets corrected)? My rec: **DAEDALUS-specific** — a roadmap-shaped changelog is my artifact, not a class requirement; encode as my-row-local and strike from the class ladder. Either way the rubric and the grade must stop disagreeing. *Conflict handling: PROME disclosed its interest (the leg touches its own 8/17 L5) and recused from the resolution, accepting a revert without argument if that's the honest read — resolution is mine with Will visibility, BEFORE run #2 ~9/6 so the re-check grades against a settled rubric.*
- **W2 (P2):** CHECKS.tsv scope-line widen to admit agent-local checks with no boot invoker (the predicate that excluded my scripts is false). One-line register change, Will-approved register.
- **W3 (P-c):** CHECK_STANDARD gains a self-inclusion section — new sweeps/enforcements/scope declarations must state own-dir in/out of scope, default IN; scope-honesty lines enumerate own-dir. Draft mine, PROVISIONAL→ratify flow as with §8.
- **W4 (P-d):** CHECK_STANDARD gains a register-birth rule — no register ships without a named reader (reading moment + cadence in the birth commit). Same flow.

**Sequencing:** Batch A + C1–C3 fit one session and should land before Falsification #2 (~8/24) — C3 changes that sweep's instrument honestly. B-items ride PROME's feedback. Existing train unchanged: R2+R6 blueprint session ~8/22 (A2/A7 fold in naturally), docket_view ~8/24–31, wiring sweep ~8/28, NEXUS blind leg ~8/29–31.

---

## §5 WHAT THE AUDIT SAYS ABOUT THE SYSTEM (the reflective part)

1. **The failure mode is boundary-shaped, not competence-shaped.** Every sweep, standard, and check works — inside its declared scope, which stops at `AGENTS/DAEDALUS/`. The SFG sweep, the staleness sweep, the byte-tier convention, the banner pass: each was scope-honest and each scope excluded its author. The fix is not new instruments; it is putting my own directory inside the existing ones (self-inclusion made mechanical, not aspirational — PAT-050's fix-form).
2. **"Invocation, not detection" holds at n=4, and the 4th is the diagnostician.** SURFACES readerless, maturity_scan uninvoked, CHECK_STANDARD uncited, closeout un-encoded — all detection layers I built, none wired to a moment that fires. The register's own founding rule (PAT-071) predicted every one of these.
3. **My highest-integrity property is worth protecting: the claims verify.** 12/12 encodes, 12/14 spine samples, 7/7 artifacts. The defects are where records go stale silently, not where records were written falsely. That is the easier disease.
4. **Growth without rotation is my structural risk — and it has already crossed from hygiene into function.** STATUS +41% in 2 days, PATTERNS at 154 KB write-mostly, EVOLUTION at 89 KB uncapped, 71 upgrades/ docs with no index and no archive. Per F37 the boot spine (425 KB) is past the point where my own SPAWN PROTOCOL can be executed as written — every boot already silently degrades to fragments, which is how a truncated-read error landed inside this very audit. Batch A1+B0/B2/B5 bend the curves; the two proposed standards (W3/W4) stop the classes regrowing.
