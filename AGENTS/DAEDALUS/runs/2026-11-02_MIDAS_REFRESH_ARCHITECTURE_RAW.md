**MIDAS architecture/current-state reader report — November 2, 2026**

This is a read-only DAEDALUS comprehension slice for later synthesis. It does not refresh MIDAS’s grade, change its owner state, certify current market observations, or establish a new whole-profile vintage.

The current architecture preserves four causal channels while adding first-class metal navigation and generated knowledge views. The September profile needs substantial reconciliation: the contract guard was repaired; WQ-421 was approved and consumed; MIDAS-09/10 are resolved; the M1 successor was retired; and current invalidation surfaces extend beyond the old inventory. The most consequential remaining ambiguity is that several files place current updates above older tables or closing paragraphs that still sound operative.

**Authority, runtime, and method**

- Assignment: Will-authorized November 2 overdue/gap comprehension work; architecture/current-state cluster only.
- Identity: DAEDALUS reader, not MIDAS owner.
- Runtime: Codex/OpenAI with read-only shell access. Requested model selection is `gpt-6.1-sol`, explicitly supplied by the user under USER WQ-590. Exact backend model and session ID were not independently exposed.
- Root: `/home/willi/Research-workspace`; launch cwd: `AGENTS/DAEDALUS`.
- Explicitly read root `AGENTS.md`, `CLAUDE.md`, `USER.md`; DAEDALUS `CLAUDE.md`, `OPERATIONS.md`, `UPGRADE_PROTOCOL.md`; profile template and prior MIDAS profile; and `PROME/COMPLETION_SPEC.md`. Read the playbook’s opening and runtime-mechanics section.
- Applied Step 0’s comprehension, coverage, false-positive, consumer-verification, and counterexample requirements. No section grading or promotion adjudication followed.
- No files changed; no owner scripts, tests, source fetchers, live-price tools, Git mutations, peer messages, or spawns ran. This output is the raw deliverable for the caller’s external `codex -o` persistence.

All paths below are repository-relative unless explicitly shortened. Within MIDAS tables, an unqualified filename means `AGENTS/MIDAS/<filename>`.

**1. Identity and current state**

| Aspect | Durable understanding | Exact source |
|---|---|---|
| Purpose | Metals as two macro tells: monetary stress/rates through gold and silver; industrial demand/supply through copper and PGMs. Four causal channels, not an unrestricted commodities patrol. | `CLAUDE.md:3–24`, `:80–96` |
| Responsibility class | Market-agent by its charter. Roster places MIDAS under **PROVISIONAL ACTIVE**, with full domain authority and proof criteria pending. This is separate from DAEDALUS maturity. | `CLAUDE.md:4`; `PROME/ROSTER.md:85–99` |
| Channels | M1 gold/real rates; M2 silver/GSR; I1 copper/China; I2 platinum/palladium. Each needs a dated live read. | `CLAUDE.md:45`, `:80–94` |
| Approved depth | Silver, platinum, and palladium are first-class coverage under Will’s September 25 directive. This deepens the existing channels without authorizing all-commodity expansion. | `CLAUDE.md:64–67` |
| Domain boundaries | BOND owns rate levels; ZHAO China macro; LIQUID credit/liquidity; HAWK geopolitics; HENRY macro velocity; TERRY construction. | `CLAUDE.md:69–76`; `THESIS.md:117` |
| Network | `{BOND, ZHAO} ↔ MIDAS → {LIQUID, HENRY}`; HAWK supplies PGM geopolitical inputs. Local rules also route PGM consequences back to HAWK/HENRY. | `AGENTS/_NETWORK.md:142–157`, `:224`; `CLAUDE.md:184–192` |
| Latest owner activity held | November 2 startup/closeout resolved MIDAS-09/10 as branch (c), with no other work started and no score/rule/trade change. | `STATUS.md:3`; `SCRATCH.md:3`; `PREDICTIONS.tsv:10–11` |
| Saved scoring state | Actual M1/M2/I1/I2 = **4/1/1/2**, total **8/20**; October 30 counterfactual **13/20**, shared-root flag retained. These are saved owner states, not this reader’s grades. | `STATUS.md:68–86`, `:120` |
| Next scoring observation | November 2 records explicitly leave first post-floor band reading for the November 2 close, with MIDAS-14/15 retrieval November 3. The elapsed November 1 floor alone does not establish a new score. | `OPEN_ITEMS.md:3`; `SCRATCH.md:49–51`; `STATUS.md:120` |
| Trade/position distinction | MIDAS has no execution book or active trade proposal. Will’s carried GLD holding is separately dated and unreconciled to a current broker book. | `TRADE.md:7–11`, `:28–32` |

**2. Existing-file enumeration and anatomy**

Recursive filesystem enumeration found **892 files**, including cached/generated material and source captures. This was enumeration, not a whole-tree content read. `MEMORY.md` is absent; no local `AGENTS.md` exists anywhere under MIDAS. Neither absence is automatically a gap.

The following nine primary files exist and were read whole:

| File | Lines / bytes | Architectural role |
|---|---:|---|
| `CLAUDE.md` | 255 / 28,776 | Charter, boot/closeout, channels, scoring, approved bands, boundaries, filing policy |
| `STATUS.md` | 136 / 30,366 | Primary current memory, dated observations, matrix, invalidation triad, top obligations |
| `THESIS.md` | 119 / 31,632 | Mechanisms, evidence distinctions, standing rules, per-channel falsifiers |
| `OPEN_ITEMS.md` | 99 / 24,787 | Standing obligations, source dependencies, completed-work dispositions |
| `SCRATCH.md` | 56 / 19,780 | Session continuity and one designated forward list |
| `LESSONS.md` | 71 / 11,293 | Greppable lesson hooks; bodies live in archives |
| `NEXUS_BRIEF.md` | 48 / 15,914 | Curated consumer-facing synchronization |
| `TRADE.md` | 67 / 9,005 | Live research/construction context, no-book declaration, outlook invalidations, unfreeze condition |
| `README.md` | 43 / 4,181 | Navigation and authority map |

Other enumerated structural files:

| Cluster | Existing files / layout | Authority and reading implication |
|---|---|---|
| Permanent workbook | `KB.tsv`, `SCHEMA.tsv`, `VX.tsv`, `FLOW.tsv`, `PREDICTIONS.tsv`, `MIDAS-06_KERNEL_NATIVE_COMPANION.json` | Permanent research/forecast record; companion preserves Kernel-native field mapping |
| Navigation metadata | `METALS_CATALOG.tsv`, `KB_METALS.tsv` | Catalog and metal-tag metadata; not competing research ledgers |
| Metal components | `gold/`, `silver/`, `platinum/`, `palladium/`, `copper/`, `shared/`, each with `README.md` and generated `KB.tsv` | On-demand access, not separate live state or new mandatory whole boot reads |
| Runtime tools | `boot.py`, `metals_watch.py`, `cot_gold.py`, `cot_metals.py`, `grade_cot3.py`, `grade_midas07.py`, `settle_check.py`, `refresh_metal_kbs.py` | Eight tools remain at the desk root |
| Tests | `test_boot_cot_metals.py`, `test_metal_kbs.py`, `test_metals_watch_inputs.py` | Present; not executed in this pass |
| Coordination | `board_log.tsv`, `inbox/`, `inbox/WALTER/`, processed subdirectories, `outbox/` | Received signals, dispositions, and outbound records |
| Corrections | `registry/corrections_receipts.tsv` | Present; receipt validity was not re-audited |
| Kernel | Three staged candidate JSON files plus their README; four submission JSON files under `outbox/kernel/submissions/` | Staging and canonical submissions are distinct; presence establishes no current activation |
| Historical material | `analysis/` 64 files, `reports/` 2, `archive/` 9 | Derivations, review receipts, preimages, and preserved session/history records |
| Source-heavy branches | `sources/` 256 files; `gold/` 145 total; `shared/` 211 total; `copper/` 14 total | Mostly captures/calculations; not read wholesale |

Measured workbook/navigation counts:

- `workbook/KB.tsv`: **244 data rows**; `KB_METALS.tsv`: **244 tag rows**.
- `workbook/VX.tsv`: **5 rows**; `FLOW.tsv`: **5 rows**; `PREDICTIONS.tsv`: **17 rows**.
- `METALS_CATALOG.tsv`: **130 rows**.
- Generated KB views: gold **152**, silver **37**, platinum **57**, palladium **56**, copper **44**, shared **82**.

These are row counts, not quality scores. Generated metal views intentionally overlap.

The six component README files all preserve the same ownership split: STATUS owns current state, THESIS mechanisms, PREDICTIONS letters, and the metal folders navigation. Their substantive research often resides in shared bundles. In particular, silver and platinum each currently contain only their README and generated KB; that is consistent with shared evidence storage, not proof of absent coverage.

The root workflow is explicit:

1. Append knowledge under `workbook/SCHEMA.tsv`.
2. Classify its ID in `KB_METALS.tsv`.
3. Refresh generated views.
4. Update catalog/topic navigation for new reports or bundles.

Sources: `README.md:18–43`; `CLAUDE.md:218–249`. No generator ran during this review.

**3. Per-dimension local representation**

| Dimension | Current local form and location | Interpretation / preservation requirement |
|---|---|---|
| Thesis | M1/M2/I1/I2 mechanism sections and evidence/limit tables in `THESIS.md` | Rich local form; retain monetary/industrial separation and multiple possible causes |
| Convergence | Universal 1–5 channel matrix, transparent `/20` arithmetic, independence column | `CLAUDE.md:107–121`; `STATUS.md:68–86`. Shared-root warnings qualify arithmetic; the total is not an independent-vote count |
| Thresholds | Charter band tables plus dated current state | `CLAUDE.md:125–164`. Includes approved ETF T/C/S legs, post-approval crossing eligibility, floor, decay, and shared-root rules |
| Invalidation | STATUS standing-rule/state/fire triad; THESIS mechanism falsifiers; TRADE/WQ-451 outlook lines; forecast consequences | Several distinct objects; a channel kill, historical test failure, model falsifier, and outlook withdrawal are not interchangeable |
| Predictions | `made`, `resolve_date`, `status`, `conf_tier`, `if_falsified`, `criteria`, `resolution` | Ledger header inspected. Seventeen rows, with branches and calibration consequences extending beyond binary HIT/MISS |
| Source reliability | Named contract month, native precision, source class, guard-qualified versus newest-row diagnostic versus certified settlement | `OPEN_ITEMS.md:59–61`; `STATUS.md:50–64`; `metals_watch.py:100–165` |
| Freshness | Five boot legs; consumed-vintage ledgers; content check for generated KBs; dated data/attention clocks on TRADE | Static wiring verified at `boot.py:298–360`; execution not verified |
| Learning | Lesson hooks plus full archived bodies; forecast-design rules from post-mortems | `LESSONS.md:1–9`, `:63–71`; `THESIS.md:119` |
| Continuity | One authoritative forward list plus dated session records | `SCRATCH.md:46–56`. The current file contains substantially more than one recent session |
| Routing | NEXUS_BRIEF curated sync; target packets; WALTER intake/disposition log | Local delivery conventions require distinguishing intended audience, delivery, and actual consumption |
| Trade interface | Declared-flat/no-execution-book adaptation; explicit three-part unfreeze; outlook invalidations retained | `TRADE.md:7–11`, `:34–57`. Do not equate MIDAS flat with Will flat |

The approved standalone bands are now a substantial local representation. M2 takes the maximum of silver/GSR; I2 takes the maximum of platinum/palladium/supply. Trend legs are current states and do not permanently latch recovered crossings; crash legs have 21-session decay. COT remains context rather than a standalone band. These distinctions survive a profile compression.

**4. Invalidation-surface inventory**

This is a comprehension inventory, not a tested replacement for the machine-consumed profile rows. It separates rule derivation, data refresh, registration, and outcome dates.

| Surface and exact anchor | What it kills or flips | In-content vintage | Fired/result form and current limitation |
|---|---|---|---|
| `STATUS.md:88–99` | Four-channel standing rails; M1 historical re-decoupling test and bidirectional score flip | Explicit **“Kill rail re-derived: 2026-08-07”**; levels refreshed October 30 without restamping the rule | Literal `FIRED`/`NOT-FIRED`, fired-count **1 of 4**; M1 historical leg 3 stays fired |
| `THESIS.md:37–39` | M1 shelf, quarterly buying floor, weekly shape, and gold/rate score flip | October 29 content review; historical rule/basis dates retained | Historical July 17→August 7 fire retained; certified-settlement dependency prevents a new official price grade |
| `THESIS.md:64–66` | Silver industrial-drag and high-beta-gold interpretations; depletion versus available supply | Dated October 12/23 blocks | Industrial interpretation fails on silver outperforming gold while copper falls; beta interpretation has its own gold/GSR discriminator; available supply remains unresolved |
| `THESIS.md:74–84` | Copper collapse conjunction and China-demand attribution | Mixed explicitly dated venue/activity evidence | Price leg **UNMEASURED** in watch; inventory alone cannot certify full collapse conjunction |
| `THESIS.md:103–111` | PGM precious-leg and supply interpretations | October 12/28 evidence blocks | Co-movement and confirmed-outage relative-response falsifiers; no-news and isolated stocks do not settle cause |
| `CLAUDE.md:139–164`; current projection `STATUS.md:77–86` | Eligibility and state of silver/Pt/Pd bands | WQ-352 approval October 1, CROSSING approval October 12, floor November 1 21:40 ET | Actual versus counterfactual, post-approval crossings, T/C/S states, decay, shared-root flag |
| `workbook/PREDICTIONS.tsv:2–18` | Individual forecast claims and pre-committed consequences | `made` and `resolve_date` per row; dated resolution text | Status/resolution plus `if_falsified`. Resolve date is not a universal thesis-rederivation stamp |
| `PREDICTIONS.tsv:9`; `analysis/2026-09-05_MIDAS-08-GRADE.md:7`, `:75–96` | Conditional public reread/correction of positioning interpretation | Registered September 2; terminal grade September 5 | Branch (b) INDETERMINATE. Branch-(c) public correction to BOND **not owed** |
| `analysis/2026-09-11_VECTOR-3-gld-under-an-oil-shock-real-yield-regime.md:195–205` | Historical real-rate-dominance interpretation | September 11 study | Two qualifying wins inside ten sessions. Current THESIS explicitly preserves the historical fired result; this reader did not recompute it |
| `gold/research/2026-10-23_WQ451-decomposition-letter.md:46–58` | Liquidation, haven, and official-demand claims | Frozen October 23 letter | L1 dated conjunction; L2 event-count test; L3 monthly/daily proxy conditions. Current option-book hedge interpretation is qualified by TRADE |
| Same letter `:60–73`; `TRADE.md:34–47` | One-/three-month GLD outlook | October 20 anchor; October 23 letter; TRADE’s latest data vintage October 28 | Price/quantity/rates/dollar/liquidation conditions; any three-month fire withdraws positive lean and reports to PROME/TERRY |
| `TRADE.md:49–57` | Declared-flat trade-surface status | Inherited conditions expressly retained during October review | Registered trigger + T+1 confirmation on both bases + falsifiable signal handed to TERRY |
| `analysis/2026-10-12_M1-successor-DRAFT.md:3`; `THESIS.md:41`, `:115` | Proposed successor conditional test | **RETIRED October 29**, WQ-522 | Historical evidence only; never registered/priced; proposed November 20 date is unarmed |
| Historical attribution guards: `TRADE.md:59–61`, `THESIS.md:43`, `LESSONS.md:7` | Misquotation of old unexplained-share constructions | Explicitly August historical analysis | Construction-specific supersession/citation guard, not an active market exit rail |

The old profile’s STATUS supersession and TRADE rebase rows remain useful correction-history concepts, but they do not adequately inventory the current falsification architecture. They should not displace WQ-451, mechanism falsifiers, the weekly basis, or current outlook invalidations.

**5. Load-bearing context / DO NOT TOUCH**

1. **Preserve channels-first scope and the approved first-class metal depth together.** “Never broaden coverage” is too absolute: the charter allows deliberate promotion and records Will’s silver/Pt/Pd depth instruction. Preserve the actual boundary against open-ended commodity patrols.  
   Anchors: `CLAUDE.md:23–24`, `:64–67`, `:96`.

2. **Keep top-level tool paths stable.** Eight runtime tools and three test files now occupy the desk root. Frozen references and instructions cite these paths.

3. **Do not boot-wire closed-question graders.** Gold and Ag/Pt/Pd freshness pullers have standing freshness roles. `grade_cot3.py`, `grade_midas07.py`, and `settle_check.py` remain deliberately on-demand.  
   Anchors: `boot.py:22–45`; `CLAUDE.md:35`, `:244–249`.

4. **Do not substitute continuous futures, named vendor bars, ETF closes, and certified exchange settlements.** They serve different tests. T+1 exclusion and native precision address vendor problems; they do not confer settlement certification.  
   Anchors: `metals_watch.py:100–165`; `OPEN_ITEMS.md:59–61`.

5. **Preserve frozen letters, first-publication/revision rules, branch boundaries, and pre-committed consequences.** Keep resolved rows in the live forecast ledger because named readers consume them verbatim.  
   Anchors: `CLAUDE.md:175–180`; `OPEN_ITEMS.md:7`; MIDAS-08 grade `:70–96`.

6. **Preserve the scoring floor, crossing eligibility, current-state semantics, decay, and shared roots.** No calendar-only promotion or permanent trend latch. No causal conclusion follows merely from a ratio outcome.

7. **Preserve historical fires and supersessions through exact archives.** The current design permits moving history out of hot files. The September profile’s “never delete a struck claim” should mean conserve its record, not keep every correction forever in STATUS.

8. **Do not hand-edit generated metal KBs or move frozen source paths.** Permanent KB and tags govern views; topic folders provide access without duplicating authority.  
   Anchors: `README.md:18–32`; `CLAUDE.md:218–220`.

9. **Do not collapse the historical attribution constructions.** Univariate 87.7–91.1%, currency-stripped 90–93% with its separate own convention, and two-factor 61–69% answer different historical questions. They are not current causal shares or portfolio hedge ratios.  
   Anchors: `THESIS.md:43`; `TRADE.md:59–61`.

10. **Keep no-book status separate from broker holdings and hedge inference.** TERRY constructs; Will/broker evidence controls positions. Equity-stress observations do not establish bearish-option-book hedge performance.  
    Anchors: `TRADE.md:9`, `:28–32`.

11. **Keep Kernel staging separate from submissions and activation.** The staged README explicitly says its directory is not live commands. Existing submissions do not grant current activation or acceptance authority.  
    Anchor: `kernel/staged_submissions/README.md:1–14`.

12. **Do not convert a bounded source limit into an indefinite patrol.** Certified settlement, Platts access, matched physical flows, and future issuer disclosures have explicit limitations and retry boundaries.  
    Anchors: `OPEN_ITEMS.md:74–95`; `SCRATCH.md:47–52`.

**6. Consumer and routing evidence**

| Consumer / interface | Evidence actually inspected | What it establishes / does not establish |
|---|---|---|
| NEXUS | `AGENTS/NEXUS/research/2026-10-31_full_pass/RECORD.md:9–16`; `DIGEST_R3.md:33–40`; `PIN_CHECK.txt:19` | Explicit direct MIDAS-brief read and digest at commit `4be44045f`; gold liquidation evidence entered cross-market synthesis |
| NEXUS current board | `AGENTS/NEXUS/STATUS.md:55`, `:80`, `:90` | MIDAS evidence appears in inflation-context qualification, thread T-33, and owner-fire inventory |
| PROME | `PROME/reports/2026-10-28_night-boot.md:40–41` | Explicit consumption of recycling/refinery results at `e96c5971b`, with lifecycle recorded separately |
| PROME delivery packet | `PROME/inbox/processed/2026-10-26_from-MIDAS_recycling-refinery-results.md:3–22` | Exact result/version, scope, caveats, requested consumption. Processed location alone would not prove reading; the night-boot receipt supplies that evidence |
| BOND historical adoption | `AGENTS/BOND/workbook/KB.tsv`, KB-BND-263 at line 264 | Recipient recorded MIDAS-08 indeterminate result, no correction owed, and all three adopted carve-outs unchanged |
| BOND historical correction chain | Same ledger KB-BND-164/184/185 at lines 165/185/186 | Independent rederivation, correction of fused constructions, and computed univariate band |
| BOND newer intake | Same ledger KB-BND-515 at line 516 | October 29 intake explicitly logged MIDAS’s dated gold/Treasury comparison as context |
| ZHAO | `AGENTS/ZHAO/NEXUS_BRIEF.md:49`, `:76`, `:85`; `STATUS.md:65`, `:97` | WQ-451 official-buying interface exists. ZHAO’s October 29 routing text still described an unrelayed crude/copper correction; MIDAS records it consumed October 30. These are different dated states |
| HENRY/LIQUID/HAWK November 2 outcomes | `MIDAS/NEXUS_BRIEF.md:3` | Consumer-specific content is published. No recipient-side November 2 read acknowledgment was inspected |
| WALTER intake | `CLAUDE.md:40–43`, `:242`; `board_log.tsv` existence | Declared intake/disposition mechanism exists. Individual ledger dispositions were not audited |

The old claim that BOND adopted the carve-outs **verbatim on September 1** has supporting sender-side history and recipient-side confirmation that adoption stood on September 9. The original September 1 recipient wording was not independently recovered here; do not describe that exact textual/date detail as freshly reverified.

**7. Reconciliation of prior profile assertions**

Prior profile: `AGENTS/DAEDALUS/profiles/MIDAS.md`, 78 lines, September 5 build with subsequent receipt/delta annotations.

| Prior assertion / anchor | Current disposition |
|---|---|
| Identity and two-tell split, `:15–17` | **Retained**, with roster classification kept separate from maturity and the September 25 depth directive included |
| “Any upgrade widening coverage argues against charter,” `:17` | **Narrowed.** Open-ended commodities drift is prohibited; deliberate approved depth/promotion is allowed |
| Flat anatomy, 217-line charter / 105-line STATUS, `:20–28` | **Superseded.** Current files and six-component navigation are enumerated above |
| KB 107 / predictions 8 / VX 5 / FLOW 4, `:25` | **Superseded counts:** 244 / 17 / 5 / 5 |
| Six top-level scripts, `:26` | **Expanded:** eight runtime tools plus three tests; top-level placement remains load-bearing |
| Kernel staged directory described as shadow path, `:27`; canonical submission claim `:65` | **Disambiguated:** staged candidates and canonical `outbox/kernel/submissions/` both exist. No current activation certified |
| `/20` convergence, `:34` | **Retained**, now with approved standalone-band diagnostics and explicit shared-root handling |
| Numbered thesis kills and sustain bar, `:35`, `:42` | **Expanded:** explicit weekly endpoint/continuity basis, restored STATUS triad, mechanism falsifiers, WQ-451 and outlook rails |
| Prediction consequences, `:36`, `:51` | **Retained as a design strength.** MIDAS-08’s terminal (b) does not owe branch-(c) correction; no fleet-wide “strongest” ranking re-adjudicated |
| STATUS corrections retained in place, `:44`, `:49`, `:70` | **Historical form, not a permanent hot-file requirement.** Current files use exact archives and dated supersession |
| TRADE’s four rebases and current band citation, `:24`, `:45`, `:73` | **Historical.** Current TRADE is a rebuilt live research register; old constructions survive as historical citation guards |
| BOND consumption, `:37`, `:77` | **Substantially supported** by recipient KB and newer intake; original exact September 1 wording not freshly verified |
| F-1 closed MIDAS-08 correction obligation, `:57` | **Confirmed** by full terminal grade and ledger fields |
| F-2 puller versus closed graders, `:59` | **Confirmed statically and extended:** Ag/Pt/Pd freshness is now boot leg 4; generated KB content check is inside ledger leg |
| F-3/F-4 old “when built” and instrument-tier labels, `:61` | **Historical closures.** Current charter describes the built watch; current STATUS uses channel/band state. Do not reintroduce removed labels |
| Missing contract guard item 24 still open, `:63`, `:78` | **Superseded.** Binding source guards were repaired. Certified settlement and overdue map maintenance remain distinct open matters |
| Boot runs and honest rc contract, `:65` | **Static contract supported; execution not reverified.** No current runtime-health certification carried forward |
| “Three peers corrected me,” `:65` | **Historical anecdote not independently re-audited** in this cluster |
| Declared-flat adaptation, `:76` | **Current declaration and three unfreeze conditions present.** No grade adjudication performed |
| October 21 banner says WQ-421 contradiction remains open, `:3` | **Resolved by later owner records.** Approval October 15, consumed October 20; now reflected in OPEN_ITEMS and forecast annotations |
| Banner’s completed beta/flow/dollar review, `:3` | **Consistent with current records.** Do not reopen it as incomplete merely because settlement/map work remains |
| Contract review due October 19, `:3` | **Later reviewed October 23; next October 30 review is now overdue.** The old due date is no longer the current maintenance state |
| Profile checkpoint September 26 / stale banner | **Still historical profile-clock information.** This reader slice does not reset whole-profile vintage |

**8. Ranked structural findings, with counterexamples/refuters**

These are comprehension findings for synthesis, not dispatched owner tasks or approved remedies.

| Rank | Finding and exact evidence | Own counterexample / refuter |
|---:|---|---|
| **1** | **Current-state projections lag behind the newest owner record.** `TRADE.md:40–45` still shows October 28 values and the downside line unbreached, while `STATUS.md:5`, `:111` and `OPEN_ITEMS.md:5` record the October 30 downside crossing subject to issuer confirmation. `NEXUS_BRIEF.md:48` still says WQ-522 “registered/not ruled,” despite retirement at `:7`; `TRADE.md:67` does likewise despite retirement at `:15`; THESIS’s retired section still carries “not ruled” at `:41`. STATUS’s final line `:136` also trails its October 30 update. A reader entering at a local table or closing paragraph can obtain an obsolete operative state. | A dated snapshot explicitly allowed to remain historical is not wrong merely because newer data exist. TRADE honestly declares October 28 data vintage, and several older blocks are dated. This limits the finding to insufficient scope/supersession at high-travel current-looking locations, not fabricated values. It is refuted for a given passage if that passage unambiguously declares itself historical and points to the controlling newer state. |
| **2** | **Authenticated settlement remains an evidence dependency that can change the official M1 state.** `STATUS.md:112` says certified evidence below the price line could move M1 4→2 and total 8→6; `OPEN_ITEMS.md:13`, `:59–61` separates repaired contract identity from absent certification; `SCRATCH.md:47` retains no-reprobe/no-paid-feed bounds. This is no longer accurately described as a generally missing contract guard. | A named vendor bar and editorial settlement wording do not satisfy the declared certification requirement. The finding is refuted by an authenticated record satisfying the existing letter, or an authorized source-rule change with owner disposition. No such evidence was inspected. It is **not** a finding that the software repair failed. |
| **3** | **Contract-map maintenance is overdue, with an existing administrative detector.** `metals_watch.py:109–115` records the October 23 review and October 30 next date; `:129–141` checks review due and expired delivery months. `SCRATCH.md:50` and `OPEN_ITEMS.md:3` explicitly carry overdue review. | Dominant mapped-contract volumes can show the chosen map remains plausible; they do not prove the specified review was completed. A later dated owner review and updated review basis/date would refute overdue status. This is not evidence that current named contracts are wrong or that a new checker is needed. |
| **4** | **The durable profile/register retain resolved gaps and omit later architecture.** Prior profile `:3`, `:25–28`, `:39–45`, `:63–78`; `FLEET_MAP.tsv:32` still carries the October 21 WQ-421 contradiction and October 19 map wording. Current owner sources resolve approval, repair guards, add component KBs, and add WQ-451/outlook invalidations. | A delta disposition can legitimately preserve an old body and old calendar vintage. That refutes “stale date alone is noncompliance.” It does not make contradicted current-state gap text accurate. This finding would be refuted by a later controlling synthesis that explicitly reconciles these inspected changes. |
| **5** | **Hot-file size and continuity form have accumulated pressure without a cap breach.** Current required local charter/SCRATCH/STATUS/OPEN_ITEMS total **103,709 bytes**, excluding root rules, predictions, inbox, and tool output. STATUS has **2,184 bytes** below 32,550; charter **3,774**. THESIS is **918 bytes** below that ceiling if required whole. `CLAUDE.md:231` promises one forward list plus the most recent session, while `SCRATCH.md:3–44` retains many session blocks. | All measured files are currently below 32,550 bytes; dense files and longer continuity can be deliberate. This is capacity/form debt, not a read-cap violation or evidence of unread content. A justified local continuity policy or bounded rotation preserving every live obligation could remove the form issue. No generic rotation threshold is inferred from DAEDALUS’s own charter. |
| **6** | **Lesson-body navigation and append instructions are inconsistent with the actual split.** `LESSONS.md:3`, `:9` and `CLAUDE.md:53`, `:234–235` direct bodies to the August archive as though it were complete. L-47..L-53 are in the September archive; October L-54..56 were appended to August. August archive `:6–8` has a splice/override history that conflicts with treating it as the universal append destination. | August archive `:8` explicitly redirects L-45..50, so the bodies are not wholly undiscoverable or lost. A reader following that banner can recover the split. This narrows the finding to stale entry/authoring instructions and inconsistent filing, not missing learning. Accurate range/destination instructions would refute it. |

No finding above justifies changing a numerical rail, frozen forecast, scoring token, guard scope, or owner judgment. Any eventual remedy affecting those contracts needs consumer verification under the review rules.

**9. Rejected or bounded findings**

- **“No MEMORY.md means missing memory.” — Rejected.** STATUS is declared primary memory, SCRATCH continuity, OPEN_ITEMS obligations.
- **“Silver/Pt/Pd coverage is absent because their local folders are small.” — Rejected.** Their component indexes and generated KBs intentionally link shared evidence.
- **“All unwired graders are invocation defects.” — Rejected.** Closed-question tools are deliberately on-demand; standing freshness pullers are wired.
- **“The contract-identity guard is still missing.” — Rejected as current framing.** Repaired guard, certification gap, and overdue map review are separate.
- **“WQ-421 still needs approval.” — Rejected.** Current owner state and forecast annotations record approval and consumption.
- **“November 1 elapsed, therefore promote the saved composite now.” — Rejected.** November 2 owner records explicitly await the then-current close/first retrieval.
- **“MIDAS-09 branch (c) proves industrial causation.” — Rejected.** THESIS `:47` and NEXUS_BRIEF `:3` preserve the liquidation/higher-beta counterexample.
- **“MIDAS declared flat means Will has no gold position.” — Rejected.** TRADE explicitly separates those facts.
- **“Missing VIEW/CALIBRATION/FORWARD headings make the brief substantively defective.” — Not adopted.** A downstream digest flagged its form, but this assignment allows rich local representation. Actual consumption is demonstrated; current-state clarity is the supported issue.
- **“Existing Kernel submissions imply current activation.” — Rejected.** No active window was audited.

**10. Whole-read coverage and limits**

Required primary coverage was delivered in bounded ranges, including recovery after initial aggregate-output truncation:

| File | Returned coverage |
|---|---|
| `CLAUDE.md` | 1–100; 100–205; 206–255 |
| `STATUS.md` | 1–54; 55–136 |
| `THESIS.md` | 1–48; 49–119 |
| `OPEN_ITEMS.md` | 1–44; 45–99 |
| `SCRATCH.md` | 1–30; 31–56 |
| `LESSONS.md` | 1–38; 39–71 |
| `NEXUS_BRIEF.md` | 1–24; 25–48 |
| `TRADE.md` | 1–67 |
| `README.md` | 1–43 |

All **14 discovered README files** were read whole:

- Root README, 1–43.
- `gold/README.md`, 1–45 and 46–88.
- `silver/README.md`, 1–60.
- `platinum/README.md`, 1–62.
- `palladium/README.md`, 1–64.
- `copper/README.md`, 1–46.
- `shared/README.md`, 1–69.
- `kernel/staged_submissions/README.md`, 1–67.
- `sources/2026-10-12_thesis-test/README.md`, 1–18.
- `shared/sources/2026-10-26_L701-settlement/README.md`, 1–14.
- `shared/sources/2026-10-26_close/README.md`, 1–11.
- `shared/sources/2026-10-26_recycling-refining/README.md`, 1–15.
- `shared/sources/2026-10-28_close/README.md`, 1–12.
- `.pytest_cache/README.md`, 1–8; cache documentation only.

Additional whole reads:

- `gold/research/2026-10-23_WQ451-decomposition-letter.md`, 1–80.
- `analysis/2026-09-05_MIDAS-08-GRADE.md`, 1–48 and 49–98.
- `analysis/2026-10-25_NEXUS-THESIS-TRADE-review.md`, 1–22.
- `workbook/SCHEMA.tsv`, 1–10.
- NEXUS October 31 full-pass `RECORD.md`, 1–30.
- PROME recycling/refinery delivery packet, 1–22.

Explicit partial/on-demand reads:

- `boot.py`: docstring/opening through line 90 and executable main 295–364; targeted wiring searches elsewhere.
- `metals_watch.py`: 100–165 plus targeted contract/certification/unmeasured searches.
- PREDICTIONS: header and all row IDs/dates/status/confidence fields; full `if_falsified` and resolution fields for MIDAS-08/09/10/14/15. Other fields/rows were not read whole.
- Workbook/catalog/tag/view files: schema/header/count inspection; not whole substantive reads.
- Lesson archives: headers, searched lesson anchors, and destination checks; not whole.
- VECTOR-3: 195–227 and targeted searches; not whole.
- Retired M1 successor: 1–16; not whole.
- BOND KB: named rows only; BOND/NEXUS/ZHAO/PROME routing surfaces: named excerpts/searches only.
- Network/roster/playbook: relevant sections only, not whole documents.

Not read or verified:

- Most of the 892-file corpus, raw market captures, PDFs/images, source histories, calculation outputs, frozen references, Kernel JSON payloads, corrections receipts, board-log rows, tests, and implementation bodies.
- No live-price/source verification, source-hash reproduction, model refit, forecast regrade, broker reconciliation, or current Kernel activation audit.
- No current clean/alert guard behavior was observed. Historical test/run claims remain attributed claims.
- No recipient consumption of the November 2 brief was established.
- No new maturity judgment; existing grade/register text was inspected only for reconciliation.
- Auxiliary broad searches sometimes truncated; they were used for discovery only. Required primary/README ranges were reread to their final lines. Unread auxiliary content is excluded from whole-read claims.

Final primary-file SHA-256 prefixes, identifying the observed checkout content:

```text
CLAUDE.md       dce3fafd1a5b
STATUS.md       c411255892df
THESIS.md       e6d94753cbd6
OPEN_ITEMS.md   2e7833928744
SCRATCH.md      745d9de2c066
LESSONS.md      459720629398
NEXUS_BRIEF.md  a4071bc0076f
TRADE.md        dd95f9082d2a
README.md       387d1898cf68
```

These are snapshot identifiers, not a revision lock or proof of a clean working tree.

**COMPLETION — DAEDALUS read-only MIDAS architecture reader — 2026-11-02**

STATUS: ✅ DONE — assigned architecture/current-state slice, with limits above.  
CHANGED: None.  
RESULT: Read 9 primary files and 14 README files whole; reconciled prior architecture assertions, mapped invalidation surfaces and consumer evidence, and ranked 6 structural findings with refuters.  
GAPS: Implementation, raw-source, execution, grade, and current-market certification were outside this reader’s authorized scope.  
WILL_NEEDS: None newly established by this report; existing settlement-source dependency remains with its owners.  
FOLLOW-UP: Caller synthesizes this raw slice with other clusters; preserve coverage limits and distinguish resolved old gaps from current dependencies.