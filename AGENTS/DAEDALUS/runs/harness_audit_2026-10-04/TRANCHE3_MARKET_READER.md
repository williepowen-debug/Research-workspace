# Tranche 3 — six market-agent charter harness read

Reader: independent DAEDALUS reader. Pin `e63816cb5f8d5297340455a6839f8bec65028dbe`, October 4, 2026. **FULL assigned targets:** SAM, RED, VIOLET, SHADE, BROCK and OZK `CLAUDE.md`, all text through EOF in bounded reads. This upgrades the earlier SAM/RED partial charter coverage only; it is not a domain/profile, market, model, runtime or maturity review. No charter read-cap finding is made from byte size.

Method: July 7 harness audit's three legs: (1) executable action/gate versus separable rationale; (2) actual mechanization and invocation, never mere script existence; (3) canonical ownership and conflicting duplication. Existing July fixes, dated history, explicit exceptions and later corrections are counterexamples. Scripts below were read as text, never executed/imported. No tests, owner edits/messages, commits, new tools or recurring controls. Parent owns consolidation, independent result review, approval and delivery disposition. All rewrites below are proposals; exact replacement text and guard-sensitive effects remain **UNVERIFIED-REMEDY** until reviewed through existing approval/owner lanes.

## Ranked retained findings and refuters

### M1 — SAM retains the expressly repaired wrong closeout timing in its inventory

`SAM/CLAUDE.md:80` correctly invokes default `closeout_check.py` **after the final commit, before push**, explicitly explains why the former pre-commit instruction was wrong, preserves PROVISIONAL/not-accepted status and allows `--pre-commit` for an early restricted look. However, the MANUAL-ONLY inventory row at **276** still invokes the default script “before the final commit.” The actual source supports the correction: `closeout_check.py:516–534` checks committed brief/STATUS order and a clean tree; `main:626–633` skips those checks only for `--pre-commit`.

**Disposition:** REWRITE the obsolete invocation clause at 276 to point to 80; KEEP the corrected step, manual closeout duties and provisional status. This is residual instruction drift, not reopening the repaired script defect or claiming an observed failed session. The inventory is not safely deletable rationale: `SAM/scripts/boot.py:202–226` parses documented manual-only script names from the charter; preserve the row's load-bearing names/recognizable contract unless that consumer is separately reviewed. **Refuter:** an explicit `--pre-commit` qualifier at 276 or changed authoritative source semantics; neither is present.

### M2 — SHADE and BROCK restate narrower retirement eligibility than root

`SHADE/CLAUDE.md:141` permits archiving old, non-boot-read research/sources absent a current STATUS reference; it also says `tmp_*` is always session-temp and archived every closeout. `BROCK/CLAUDE.md:67` similarly checks only STATUS/SCRATCH filename references. Root `CLAUDE.md:121` protects qualifying references from **any live analytical/protocol doc**, and separately protects registered artifacts of **PENDING dated events regardless of age**. The local eligibility tests therefore admit files that root could protect.

**Disposition:** REWRITE local eligibility to cite root while keeping applicable local paths/cadence and SHADE's stale-source review duty. No file is identified as presently eligible; no archive action or new scheduled sweep is commissioned. **Refuter:** a specific approved local waiver covering these root protections, or local wording explicitly restricted to already root-eligible files. Neither appears in the bounded sources. This does not invalidate BROCK's unrelated T1b exception, explicitly preserved in July's approved audit receipt.

### M3 — RED still instructs current writes into an explicitly frozen ledger

`RED/CLAUDE.md:87` directs break-pathway moves into FLOW; **289** instructs adding rows/updating Status as evidence changes, and **279** describes its role without the freeze. Actual `RED/workbook/FLOW.tsv:1` declares **FROZEN 2026-07-05, not maintained**, with STATUS/VX/CHALLENGES canonical. Root Data Hygiene `CLAUDE.md:120` says frozen ledgers stop being maintained.

**Disposition:** STRIKE/rewrite these live-maintenance targets to honor the frozen disposition and existing canonical owners; preserve history. No unfreeze, ledger content change or new ledger is proposed. **Refuter:** a subsequent authoritative unfreeze or instruction expressly limited to historical correction. Neither appears in the pinned charter/header. No claim that RED actually wrote the ledger after freezing. Same class as prior DC2/LIQUID, a distinct owner's retained instruction, not evidence that LIQUID's repaired declaration regressed.

### M4 — BROCK runs its existing closeout checker before writes it is meant to check

The charter calls `brock_selfcheck.py` at **62, step 6c**, then dispositions predictions at **63, 7a** and writes KB/VX at **64, 7b**. Full source read shows it loads the target files at invocation (`brock_selfcheck.py:47` onward), checks fire/resolution propagation at **60–91**, matrix counts at **94–109**, and KB/VX field counts at **111–117**. No later invocation appears anywhere in the full charter; the inventory at 253 still names 6c. A clean result before those writes cannot certify the written result.

**Disposition:** proposed REWRITE of the existing invocation's ordering after the writes it checks, retaining ALWAYS status, narrow CLEAN scope and manual propagation duty. This is a static sequence finding, **not an observed missed defect**. No additional checker or test is proposed. **Refuter:** an explicit final post-write invocation or an approved writer automatically rerunning this checker. None is documented in the charter; other writer implementations are unread, so automatic rerun elsewhere remains UNKNOWN. Exact placement/remedy remains unverified pending owner review.

### M5 — repaired routing rules coexist with old routing instructions in SAM and BROCK

SAM's current `CLAUDE.md:120,197,281` clearly sends SIGNALS through WALTER and reserves own outbox for PROME requests; the explicitly corrected retired-HERMES clause at 96 is sound. Yet **93** still prefers own-outbox Convention B for time-sensitive signals and calls HERMES unreliable rather than retired. BROCK's corrected **94,271** likewise preserve the WALTER/direct-packet distinction, while its executable closeout **68** still sends cross-agent signals to outbox and describes degraded delivery.

**Disposition:** REWRITE the obsolete subordinate instructions to the already repaired rules; KEEP the repaired rules, legitimate outbox requests and direct analysis/packet lane. No evidence of an actual bypass or dead-router incident is asserted. **Refuter:** explicit scoping of the residual instruction to PROME-action requests or an applicable approved alternative signal route. Current wording does not supply it. This is the residual class of prior HANS/DC1 and July routing consolidation; parent should reconcile existing routing findings before assigning owner work, not reopen all former repairs.

### M6 — RED describes an old comparison instead of its repaired board-gap mechanism

`RED/CLAUDE.md:48,68` says section 5 compares the newest addressed BOARD signal with the newest log row. Actual `RED/scripts/boot.py:473–599` uses addressed IDs (`action` plus legacy `to`), membership across live and archived board logs, and a set difference with **no date floor**. `main:602–617` invokes this section. Full `board_log_append.py` read also verifies a concrete existing append/validation/rotation entry point; truthful dispositions still require judgment.

**Disposition:** REWRITE the two descriptive clauses to a short accurate pointer/scope, preserving the disposition action and source's repaired coverage. **Refuter:** “newest” explicitly limited to a display label while the charter describes membership coverage elsewhere, or source reverting to a newest-only comparison. Neither is shown. Do not reopen the old date/ID coverage bug: source is the counterexample to that allegation.

### M7 — local Git explanations retain the obsolete non-ff interpretation

`OZK/CLAUDE.md:90` calls non-ff a second-machine tripwire and immediately flags PROME/Will. Root `CLAUDE.md:96` explicitly says another session on the same box ordinarily suffices and gives guarded recovery before escalation. `SHADE/CLAUDE.md:145` says flag if non-ff “recurs,” omitting root's completed recovery-cycle condition. OZK is a clear obsolete explanation; SHADE's omission is a **qualified canon-duplication finding**, since its opening root pointer may govern the abbreviated wording.

**Disposition:** cite root recovery/escalation rather than maintaining competing summaries, retaining local pathspec and SHADE's approved `git mv` guard. No recovery operation is performed. **Refuter:** an approved desk-specific stricter push/escalation policy or explicit intended shorthand for root's complete condition. None is established in these sources. BROCK T1b is **not** grouped here: July's approved S2 receipt expressly preserved that exception.

## Per-file three-leg disposition

| Full target | Action versus rationale | Mechanization versus human duty | Canon / proposed disposition |
|---|---|---|---|
| SAM | KEEP warm/cold/scoped reads, actual writebacks, manual provisional-closeout warning and messaging receipt limits. Historical incident explanations can be shortened only while preserving gates and parser-consumed manual inventory | Boot main and predictions helper have actual callsites; checker F/G require post-commit state. This does not validate every helper or eliminate manual figures/meaning checks | M1 and M5 REWRITE. KEEP frozen/historical source and expired activation distinctions; do not silently restart manual-only retired instruments |
| RED | KEEP falsifiers, disposition actions, due-row and terminal/citation distinctions. Old incident accounts separable only if trigger scope survives | Actual boot section5 fixes old gap behavior; append helper exists with validation/rotation. Other child/helper implementations remain partial/unread; no broad “all manual work automated” claim | M3 and M6 REWRITE/STRIKE. “BOARD sole channel” wording at40 also needs qualification by live WALTER intake53, without removing intake or fabricating a missing-message finding |
| VIOLET | KEEP operator decision limits, scoped trigger work, current versus historical tokens and closeout writeback duties. Historical failures alone are not active rules | Full boot orchestrator and closeout guard read; actual subprocess callsites establish wiring. Guard lists ten blocking checks, beyond charter60's three-item summary. Child behavior remains UNKNOWN | No comparably strong new primary defect retained. Optional REWRITE60 to canonical guard pointer/scope; KEEP actual invocation/manual judgment. Do not equate summary incompleteness with a guard failure |
| SHADE | KEEP action thresholds, staged permission boundaries, compact current state versus research separation and maintenance log. No market validity inference from numerical trigger history | No SHADE owner script body read. No mechanization/deletion conclusion from absence of a checked tool | M2 REWRITE; M7 qualified REWRITE. KEEP local move guard and canonical ownership; exact retirement remedy requires owner review |
| BROCK | KEEP live-event timing override with nonwaivable ALWAYS duties, every-surface propagation, byte/obligation protection from current hot/cold repair. Do not remove obligations merely because prose cites past failures | Full selfcheck verifies narrow fixed patterns, counts and schemas, not all propagation surfaces or all decisions. Existing call ordering is M4; retain manual trap5 | M2/M4/M5 REWRITE. KEEP approved T1b and owner-scoped memory-index gate; no unapproved authority broadening |
| OZK | KEEP current/historical numerical-role distinctions, repaired cwd fallback, index mirror distinction and teams deliver-before-idle contract | Boot main actually invokes its fetch/render pipeline and `flng_watch.py`; dependent bodies not fully read | M7 REWRITE. Low-priority factual correction: charter50 says scripts contains only boot.py, but pinned tree includes flng_watch.py and boot246–253 invokes it. Remove stale exclusivity, retain cwd fix; no tool work |

## False positives and limits

- July S2 explicitly preserved BROCK T1b, SHADE's move guard and other named exceptions. No blanket deletion of local guards is authorized.
- SAM's step80 is a repair and expressly provisional. A PASS is not accepted closeout evidence; no script execution occurred here. Parser-consumed charter names make wholesale rationale removal unsafe.
- RED's live plus archive ID coverage refutes reopening its repaired gap mechanism. Historical dated banner values are not current-state defects. The FLOW freeze is decisive against its *instruction to maintain*, not proof its historical rows are false.
- VIOLET's boot validation does not replace end-of-session validation after writes. Current child callsites refute a missing-invocation allegation; unread children prevent a claim that all textual obligations are enforced. The three-item guard summary is incomplete, but the real guard contains additional blockers.
- OZK's corrected repo-root fallback remains correct despite its stale file-count rationale. Its spawned-session push delegation and direct coordinator delivery are mode-specific; no root conflict claimed without reviewing the applicable launch contract. No dormant/launch status is changed.
- Brief-versus-STATUS, SCRATCH-versus-dated memo and live-versus-history surfaces often serve distinct consumers. Mere overlap is not enough to strike them. No all-surface domain completeness finding follows from the full charter read.
- Unread approvals could qualify M2/M7; unread write integrations could refute M4. These limits remain explicit. Exact source proposals must be reviewed, not treated as approved changes.

## Evidence manifest and exact read depth

Six target charters were freshly read FULL at this pin. Byte counts are UTF-8 bytes; no size-to-cap inference. Support descriptions below distinguish full code from caller-only evidence. Root full canonical interpretation reuses the earlier full read after unchanged-byte verification; fresh clauses94–123 and24–52 were read here. July method/receipt and playbook full reads are retained from this same audit; July S2 exception text was freshly rechecked. All hashes below describe the pinned exports, not runtime execution.

| Pinned path | Bytes / lines | Read scope | SHA-256 |
|---|---:|---|---|
| `AGENTS/SAM/CLAUDE.md` | 41,591 / 301 | FULL, all text through EOF | `e684b27d2683fb115e6d6e6a82396ec1c9027cc22675d22e80672408c88f391c` |
| `AGENTS/RED/CLAUDE.md` | 42,457 / 352 | FULL, all text through EOF | `e3406674f3dbaaee5c384aca71fd72b96a08ae84edb535944dbcd106bb18b5ad` |
| `AGENTS/VIOLET/CLAUDE.md` | 27,215 / 200 | FULL, all text through EOF | `7ada4238628ba5d3913f25a89841435378861743f747caf61e4c9e49d7b6b390` |
| `AGENTS/SHADE/CLAUDE.md` | 23,407 / 172 | FULL, all text through EOF | `d86a527a423c7924ddb9b8fbdcb602755ccddad15bf30e182bdde1e2b4c4696d` |
| `AGENTS/BROCK/CLAUDE.md` | 30,957 / 271 | FULL, all text through EOF | `ef94ba4ed7c3b344302e759054355184e417b7d7612006a4eeaa925349917b8c` |
| `AGENTS/OZK/CLAUDE.md` | 28,236 / 268 | FULL, all text through EOF | `923c3de40a9a9775ae11e6665ec35d916170a4edb07139fcd25360e74cd7e5cc` |
| `CLAUDE.md` | 24,199 / 133 | Prior FULL reused unchanged; fresh24–52,94–123 | `1b176d7b3c619a78dbabe4128f23451fa32a074554f391804707aec7623a3c73` |
| `AGENTS.md` | 4,991 / 62 | Prior supplied/read canon unchanged; exported, no new independent full read | `9b126769cbc278fad34b97c7d51806f7ef8966486c305389896c983bbd86585e` |
| `AGENTS/SAM/scripts/boot.py` | 18,654 / 369 | PARTIAL202–255,292–369; function/search inventory elsewhere | `dcc953ac486cb399b233331327e25aa919eb878c71b749c37eec583ccc03cdde` |
| `AGENTS/SAM/scripts/lib/boot_context.py` | 10,909 / 200 | PARTIAL1–96; complete predictions function39–57, report only partial | `1a136cb14efd3e2b2de66ea23219042c8e53acae7eac11bb3059b98b0d125efc` |
| `AGENTS/SAM/scripts/closeout_check.py` | 37,191 / 676 | PARTIAL84–90,516–549,599–676; function/search inventory elsewhere | `9a1b5bf9c20c2f6e5bcf94e8cd59f4873aa242a7df5b4f481b4bf212b97ea9b8` |
| `AGENTS/RED/scripts/boot.py` | 31,029 / 617 | PARTIAL430–617; complete due-scan tail/addressed/logged/gap/main in this span; other helpers unread | `e96db4daba3c74e7b8251c5b664f72e40e9ef55f59934dd8001d6f671225fcf0` |
| `AGENTS/RED/scripts/board_log_append.py` | 5,838 / 133 | FULL1–133 | `8fcffa59a7ef18faeca0f5597632cbd7a4d1655b38301964e26d5898b510900e` |
| `AGENTS/RED/workbook/FLOW.tsv` | 3,296 / 9 | PARTIAL1–2, freeze/header only; no row/domain audit | `6ba3c7e26a84cc20be70004ec9cbdad52e1db4c74f204ea79bce7d50a26614d6` |
| `AGENTS/VIOLET/scripts/boot.py` | 10,526 / 206 | FULL1–206 (initial1–75,125–206; recovered76–124) | `69965d868869d556710b98cc08b404a305635165c185640564f6c2565f97743e` |
| `AGENTS/VIOLET/scripts/closeout_guard.py` | 9,223 / 172 | FULL1–172 | `e5e5a356344be4c37e9a662486414833ae9b8aeadc45c063e2b0a6670d67ed23` |
| `AGENTS/BROCK/scripts/brock_selfcheck.py` | 6,829 / 123 | FULL1–123 | `dc8fa55787689012bb1a4df1c12e142a6a947c4a58865d167e04abcae8e4bb36` |
| `AGENTS/OZK/scripts/boot.py` | 16,751 / 350 | PARTIAL198–350, complete main/entry; earlier helpers unread | `38b0f120680e0528a18ff8c67a01ce453c50134bd021f8b048fe9eea1ddb6ab8` |

Additional exact support: pinned `git ls-tree -r` for OZK's scripts directory established the two tracked files `boot.py` and `flng_watch.py`; the latter body was **not read**. This is tree metadata, not behavior validation.

**Not-read list:** every underlying market/model datasource and live domain STATUS/THESIS/workbook corpus except the RED FLOW header; SHADE owner scripts; SAM closeout delegated child implementations and tests, SAM boot helpers outside the spans above; RED boot earlier helpers and underlying shared scanners; VIOLET guard/boot child tool bodies and tests; BROCK writer integrations outside its charter/selfcheck; OZK fetch/render/helper bodies before198 and `flng_watch.py`; complete approval histories, transport operation and owner-session execution traces; hosted Helm/Deck; full profile reviews. No runtime outcome, unseen authority waiver, accepted guard remedy, full audit closure or maturity promotion follows from this report.

**Delivery dependency:** parent result review and consolidated owner/approval disposition remain owed. This raw report completes the assigned six-charter read, not the entire harness audit or an implementation package.

**POST-REVIEW:** credit/market challenge retained M1–M6 and OZK-M7; corrected M6 current action/legacy to. SHADE-M7 narrowed to LOW canon-copy cleanup: “recurs” may mean after its stated recovery cycle, so an incompatible escalation instruction is not established. No code repair or runtime claim follows.
