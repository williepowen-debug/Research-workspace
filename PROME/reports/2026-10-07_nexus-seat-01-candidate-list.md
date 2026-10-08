# GATE-NEXUS-SEAT-01 — candidate list (DOCKET L36)

**Built by:** read-only reader for PROME, 2026-10-07. **Spec read:** `FORUM/2026-08-07_system-review/08_dissent/02_NEXUS_the-layer-that-cannot-name-its-decision.md` (whole post) + `scratchpad/nexus_seat/spec_excerpt.md`. **Role:** PROME lists, NEXUS contests, Will confirms. **This file issues no verdict.**

**Rule as applied (VERIFIED at the post §8):** a Will decision (trade approval · RULE ruling · launch) 2026-08-08 → 2026-10-07 counts only if its PROXIMATE input was a NEXUS product — the split (Break/Grind/Unresolved), a convergence-matrix row, the antecedent map, a narrative-gap read — rather than a domain agent's own surface. A datum NEXUS relayed does not count. One input among several counts only if it is the one the decision turned on. NEXUS's registered prediction: 1. ≥3 = layer pays · 0–1 = dissolve · 2 = NO VERDICT (non-renewable, re-grade, take the lower).

## ⚠️ Coverage finding — read this before any count (VERIFIED)

1. **The 109-event stable-key file spans 2026-09-11 → 2026-10-07 only** (VERIFIED: earliest `at` 2026-09-11, latest 2026-10-07; every row `source` = "WILL_QUEUE.md § RECENTLY DONE"). It was exported with `event ∈ {RULED, CLOSED, DECLINED}` (59 + 49 + 1 = 109, VERIFIED against `PROME/registry/WQ_LEDGER.tsv`).
2. **The first 34 days of the window (8/08 → 9/10) sit in ledger `BACKFILL` rows, and some later rulings sit in `REGISTERED`/`UPDATED` rows carrying a verdict.** In-window ledger rows with a Will verdict or a RULED/CLOSED/DECLINED status whose WQ is NOT in the 109: **222 WQ keys** (179 whose in-window record is a BACKFILL row, 43 whose first in-window row is REGISTERED/UPDATED with a verdict), plus **2 undated** (33b, 40) = **224 keys**. These include NEXUS-touching rulings (WQ-105, WQ-163, WQ-340, WQ-343). Table B classifies all 224 (WQ-163 split into its five separately-ruled items ⇒ 228 rows).
3. **12 Will decisions in the window were never numbered** ("| — …" rows in `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md` and `…_2026-09-05_rolloff.md`; one says "Was a SCRATCH-list item, never a numbered row"). Listed in Table C.
4. WQ-38 (NEXUS brief-schema amendment 11) is dated 2026-08-07, one day before the window — excluded, noted.

**Classification key.** **YES** = proximate input is one of the four named NEXUS products, established at the artifact, and the decision's object is not NEXUS's own instrument. **CANDIDATE** = a NEXUS product is in the chain but it cannot be established as the qualifying proximate input; sub-class **S** (self-referential: the proximate input IS a NEXUS artifact, but the decision's object is NEXUS's own instrument — split falsifier gate, brief schema, cadence; whether layer-maintenance counts is an interpretive question the letter does not settle), **N** (NEXUS-authored artifact outside the four named classes, e.g. a self-audit slate item), **P** (proximity not established). **NO** = proximate input is a domain desk's surface, PROME, a reviewer, or Will's own initiative. Flags: **DELEGATED** = moved under Will's 9/30 19:32 blanket word *"…move forward with and assume I approve?"* on PROME's own rec (not a per-row Will word) · **BATCH** = one "with your recs" word over several rows · **NOT-A-RULING** = lapsed/moot/withdrawn/superseded per the row itself · **LAUNCH-OF-NEXUS** = a decision whose OUTPUT is a NEXUS product (input was not) · **OBJ-NEXUS** = object is NEXUS's file, input is another desk's adjudication.

**Confidence tokens:** every row in Table A was read at the artifact named (full row text at the WILL_QUEUE line) = **VERIFIED** for the row text; the proximate-input naming is my reading of that text = **INFERRED** unless the row says "VERIFIED" in its artifact cell. Table B rows marked depth **T** were read at ledger title + record (first 700 chars) + the archived row where indexed, keyword-screened for NEXUS terms, then deep-read only where NEXUS appears = **INFERRED** for NO.

## Table A — the 109 stable keys

| key | date | decision (≤12 words) | proximate input | class | flags | artifact read |
|---|---|---|---|---|---|---|
| WQ-210 | 2026-09-11 | Sell XLE Sep-30 65C at the 9/11 open (branch 1) | TERRY branch card / Will's own hand (FORGE D-49) | **NO** | TRADE | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:38` |
| WQ-223 | 2026-09-11 | Sign up for NASA FIRMS key for FALCON | FALCON's unplaced Petroline hotspots | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:37` |
| WQ-226 | 2026-09-11 | Build ARGUS, a propose-only closeout auditor | PROME/SAM subagent-system assessment report §4 | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:36` |
| WQ-239 | 2026-09-12 | Boot interrupt contract and capability scoping legs 1+2 | Codex review relayed by Will | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:33` |
| WQ-228 | 2026-09-17 | REGINALD owns BaaS/sponsor-bank credit perimeter | CARL's 9/11 BaaS packet | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:31` |
| WQ-243 | 2026-09-17 | Release MARCO's Florida leg to a PROME spawn | PROME/DOCKET L332 | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:30` |
| WQ-248 | 2026-09-17 | HOMER Freddie multifamily band: option C, no retune | HOMER's own restraint + PROME rec | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:27` |
| WQ-225 | 2026-09-17 | Google Trends captures ruled undateable, closed | Will's own statement in chat / HOMER KB | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:26` |
| WQ-229 | 2026-09-17 | Adopt repair-completion discipline as PROME practice | PROME proposal (2026-09-11_wq229 record) | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:25` |
| WQ-262 | 2026-09-18 | Commit CATO's staged LIQUID review to GitHub | CATO's staged review files | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:24` |
| WQ-258 | 2026-09-18 | Cheap-tail window lapsed with no word | VIOLET cheap-tail alert (no Will word = not a ruling) | **NO** | NOT-A-RULING | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:23` |
| WQ-236 | 2026-09-18 | READS.tsv rollout now; DAEDALUS dates STRICT flip | DAEDALUS read-cap checker work | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:22` |
| WQ-244 | 2026-09-18 | Make commit-subject and pipeline hooks blocking | PROME/DAEDALUS detector measurement | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:21` |
| WQ-245 | 2026-09-18 | Intake collector cron to seven days | WALTER/PROME intake lane | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:20` |
| WQ-219 | 2026-09-18 | Exclude ASIF from BRK-30's OR-gate | BROCK's vehicle-population work | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:19` |
| WQ-247 | 2026-09-18 | Root Output Canon gains operator-surface clause | Will's own 9/14 ask | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:18` |
| WQ-250 | 2026-09-18 | "I could not check this" letters not gate-citable | DAEDALUS SL-4 split | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:17` |
| WQ-224 | 2026-09-18 | NEXUS matrix line: seek flow feed, else carry unfalsifiable | NEXUS 9/11 memo: T-12 C#2 graded NO-VERDICT, split 20/47/33 un-falsifiable (0d9ec2067) | **CANDIDATE**-S | S | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:16` + ledger UPDATED 2026-09-14 row (OPEN text: NEXUS memo `PROME/inbox/processed/2026-09-11_from-NEXUS_L289-C2-graded-...md`, 0d9ec2067) |
| WQ-213 | 2026-09-18 | VLO 1 of 3 shares bought by Will's hand | TERRY TRY-BRENT-REFINER card / BRENT refiner thesis | **NO** | TRADE | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:15` |
| WQ-266 | 2026-09-19 | Apply Channel-2 geography qualifier to both channels | OSPREY's kill-clock measurement (OWED39 Channel-2 scope) | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:9` |
| WQ-267 | 2026-09-19 | Grant Russia desk YURI seat and wire now | HAWK/OSPREY boundary ruling + PROME rec (overridden) | **NO** | LAUNCH | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:10` |
| WQ-271 | 2026-09-19 | Free GIE AGSI+ key registered by Will | HANS's HANS-T-08 exit path need | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:14` |
| WQ-272 | 2026-09-20 | Position mirror 9/16 snapshot corrected | broker capture / ANVIL reconcile | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:8` |
| WQ-265 | 2026-09-22 | Decision Deck publication question closed as done | PROME Deck republish | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:38` |
| WQ-230 | 2026-09-23 | War-risk insurance: no paid access, free monitoring | FALCON data gap / PROME row | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:33` |
| WQ-234 | 2026-09-23 | BG-02 AIS resolvers corroborate only (C) | BRENT BG-02 letter | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:34` |
| WQ-238 | 2026-09-23 | Laptop API keys supplied | env_doctor / PROME | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:35` |
| WQ-263 | 2026-09-23 | Commit-guard split approved with CATO fix | coldreader rounds + CATO fix | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:36` |
| WQ-275 | 2026-09-23 | FALCON 5th-spawn exception moot | PROME (no decision needed) | **NO** | NOT-A-RULING | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:37` |
| WQ-277 | 2026-09-23 | Decline licensed futures settle feed | BRENT memo on L430 second vendor | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:32` |
| WQ-278 | 2026-09-23 | 9/24 spawn slate; hold RED and DAEDALUS | PROME spawn_list slate | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:31` |
| WQ-256 | 2026-09-24 | DAEDALUS gate-basis run #1 rulings (b),(d),(a) | DAEDALUS GATE_BASIS_SWEEP_01 run record | **NO** | BATCH | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:29` |
| WQ-259 | 2026-09-24 | VIOLET pages refresh after next post-close boot | VIOLET pages / PROME rec | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:30` |
| WQ-264 | 2026-09-24 | Petroline shadow run approved; BG-02 lapses on letter | BRENT resolver analysis | **NO** | BATCH | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:28` |
| WQ-254 | 2026-09-24 | P4 sitting D-items ruled by letter | DAEDALUS/Codex P4 package | **NO** | BATCH | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:22` |
| WQ-260 | 2026-09-24 | ORACLE v4 supply leg re-struck to $110 as v5 | ORACLE 9/17 packet | **NO** | BATCH | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:24` |
| WQ-261 | 2026-09-24 | Bless DFII10 real-rate leg into frozen T-12 gate | NEXUS 9/17 packet: full matrix sweep + T-12 successor ask (7a7cef525) | **CANDIDATE**-S | S;BATCH | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:23` + ledger REGISTERED 2026-09-17 row (OPEN text cites NEXUS packet `PROME/inbox/processed/2026-09-17_from-NEXUS_full-matrix-sweep-delivered-and-the-T12-successor-ask-for-Will.md`, 7a7cef525) |
| WQ-276 | 2026-09-24 | OSPREY C1 refinery upgrade + downgrade successor | OSPREY C1 upgrade proposal | **NO** | BATCH | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:25` |
| WQ-252 | 2026-09-24 | Crack contract month: convene a sitting | HENRY/BRENT roll-hazard analysis + PROME rec | **NO** | BATCH | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:16` |
| WQ-283 | 2026-09-24 | Wake SAM before Tokyo: overtaken by Will's own launch | Will launched SAM himself (WALTER handoffs, USD/JPY) | **NO** | NOT-A-RULING;LAUNCH | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:20` |
| WQ-288 | 2026-09-24 | Met Invalidation resolves the row at the fire | CARL CRL-08 / DAEDALUS ruling | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:17` |
| WQ-289 | 2026-09-24 | Push held commits; narrow L367 form | ARGUS verify failure / PROME | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:14` |
| WQ-290 | 2026-09-25 | BOND fixes FR2004 join window | BOND fr2004_join.py defect | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:13` |
| WQ-157 | 2026-09-25 | Park WQ-157 leg 2; keep Sept-4 rule | BOND corrected-window study (KB-BND-335) | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:12` |
| WQ-294 | 2026-09-25 | Spawn HANS past cap to grade HANS-T-10 | HANS-T-10 fire (HANS) | **NO** | LAUNCH | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:11` |
| WQ-297 | 2026-09-25 | Accept the book's oil concentration in writing (A) | TERRY Q1 exposure map (b93800740) | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:9` + ledger REGISTERED 2026-09-25 row (basis = TERRY map b93800740) |
| WQ-298 | 2026-09-25 | Paid-data question decided once; one list by 10/02 | PROME rec | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:10` |
| WQ-251 | 2026-09-26 | Withdraw CCC/HY stand-down re-base as overtaken | LIQUID/REGINALD CCC/HY work | **NO** |  | `PROME/WILL_QUEUE.md:137` |
| WQ-255 | 2026-09-26 | CATO's permanent class: SPECIAL | PROME/ROSTER classification | **NO** |  | `PROME/WILL_QUEUE.md:138` |
| WQ-237 | 2026-09-26 | Root YEYOU lines moved to implementation tracking | PROME/DAEDALUS (9/17 tap) | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:8` |
| WQ-235 | 2026-09-26 | BRK-02 basis already ruled 8/13 (amortized cost) | BROCK memo 0687f382b | **NO** | NOT-A-RULING | `PROME/WILL_QUEUE.md:136` |
| WQ-257 | 2026-09-26 | Ratify FERT option A (NOLA panel freeze) | FERT option A | **NO** | BATCH | `PROME/WILL_QUEUE.md:131` |
| WQ-287 | 2026-09-26 | CRL-27 retired unscored; successor without leg (a) | CARL option A | **NO** | BATCH | `PROME/WILL_QUEUE.md:132` |
| WQ-292 | 2026-09-26 | TERRY prepares two ITM-put management cards | TERRY / FORGE mirror holdings | **NO** | BATCH | `PROME/WILL_QUEUE.md:135` |
| WQ-296 | 2026-09-26 | HAW-22 successor + Kpler/Vortexa inquiries | HAWK memo §5 | **NO** | BATCH | `PROME/WILL_QUEUE.md:134` |
| WQ-300 | 2026-09-26 | Free-tier rating actions; paid lines declined | PROME paid-data list v2 | **NO** | BATCH | `PROME/WILL_QUEUE.md:133` |
| WQ-246 | 2026-09-26 | DFII10 'sustained' = 5 consecutive closes >=2.50 | BOND memo Part 2 (BOND's own matrix vector-1, not NEXUS's) | **NO** |  | `PROME/WILL_QUEUE.md:129` + ledger UPDATED 2026-09-26 row (BOND KB-BND-278; "BOND's matrix vector-1") |
| WQ-291 | 2026-09-26 | BOND's Sept-4 dealer-stock kill letter approved | BOND memo Part 1 (830f33a75) | **NO** |  | `PROME/WILL_QUEUE.md:130` |
| WQ-293 | 2026-09-26 | YUR-004 approved with three corrections | YURI mobilisation test | **NO** |  | `PROME/WILL_QUEUE.md:128` |
| WQ-169 | 2026-09-26 | FORGE reconcile items consolidated into WQ-274 | PROME R4 triage (no new ruling) | **NO** | NOT-A-RULING | `PROME/WILL_QUEUE.md:127` |
| WQ-307 | 2026-09-28 | Successor-quarantine N lapses | Forum-4 N12 deferral (SAM synthesis) | **NO** |  | `PROME/WILL_QUEUE.md:120` |
| WQ-318 | 2026-09-28 | REGINALD funding baseline, one session by 10/09 | REGINALD/PROME row | **NO** |  | `PROME/WILL_QUEUE.md:118` |
| WQ-241 | 2026-09-28 | MSI-01 re-fire condition approved with two amendments | CORAL tightened letter (9655ceaf3) | **NO** |  | `PROME/WILL_QUEUE.md:116` |
| WQ-321 | 2026-09-28 | Criterion 5 absolute leg scored; relative reported | CORAL letter | **NO** |  | `PROME/WILL_QUEUE.md:117` |
| WQ-303 | 2026-09-28 | CREED S8a REIT-tape score set at 4 | CREED-T-08a fire (CREED) | **NO** |  | `PROME/WILL_QUEUE.md:114` |
| WQ-304 | 2026-09-28 | CREED predictions 004/007 scored on own ledger (B) | CREED / CATO WR30-31 | **NO** |  | `PROME/WILL_QUEUE.md:115` |
| WQ-319 | 2026-09-28 | VX-HAWK-IRAQ-01 red to yellow | HAWK/CATO SOMO primary read | **NO** |  | `PROME/WILL_QUEUE.md:111` |
| WQ-320 | 2026-09-28 | FININFRA-01 narrow bank-cloud definition | HAWK row | **NO** |  | `PROME/WILL_QUEUE.md:112` |
| WQ-322 | 2026-09-28 | CORAL bankruptcy tripwire: retire 230/260 level (E) | CORAL packet (Will in CORAL session) | **NO** |  | `PROME/WILL_QUEUE.md:110` |
| WQ-324 | 2026-09-28 | WAL V3 NDFI re-scored 1/5 to 3/5 | WAL KB A1 filing rows (WAL's own matrix scale) | **NO** |  | `PROME/WILL_QUEUE.md:108` |
| WQ-325 | 2026-09-28 | WAL Q3 print frame: three dated rules added | WAL print frame | **NO** |  | `PROME/WILL_QUEUE.md:109` |
| WQ-317 | 2026-09-28 | One-page cross-market attribution read inside BOND refresh | PROME proposal on BOND/HANS/SAM material | **NO** |  | `PROME/WILL_QUEUE.md:106` |
| WQ-345 | 2026-09-30 | BRT-31 Path-B test: second reader then register | BRENT successor test | **NO** |  | `PROME/WILL_QUEUE.md:95` |
| WQ-305 | 2026-09-30 | ORACLE Kalshi re-check drops to quarterly | ORACLE KB-ORC-088/089 | **NO** | DELEGATED | `PROME/WILL_QUEUE.md:87` |
| WQ-306 | 2026-09-30 | DEWEY court-records helper confirmed | DEWEY recap_pull.py | **NO** | DELEGATED | `PROME/WILL_QUEUE.md:88` |
| WQ-332 | 2026-09-30 | BOND keeps hand-grading pulled-deal cluster | BOND rec | **NO** | DELEGATED | `PROME/WILL_QUEUE.md:89` |
| WQ-335 | 2026-09-30 | HOMER cross-tab: not now | HOMER optional ask | **NO** | DELEGATED | `PROME/WILL_QUEUE.md:94` |
| WQ-337 | 2026-09-30 | AI policy coverage held explicitly unowned | VULCAN raise | **NO** | DELEGATED | `PROME/WILL_QUEUE.md:90` |
| WQ-342 | 2026-09-30 | Credit leg for NEXUS duration split: not now | NEXUS WQ-340 page flag + NEXUS rider C2 (6efb45d52) | **CANDIDATE**-S | S;DELEGATED | `PROME/WILL_QUEUE.md:91` + ledger UPDATED 2026-09-29 row (sources: GATES row 24 · NEXUS page · WQ-261; NEXUS rider 6efb45d52) |
| WQ-344 | 2026-09-30 | HEN-F3 dead as written | HENRY grade | **NO** | DELEGATED | `PROME/WILL_QUEUE.md:92` |
| WQ-346 | 2026-09-30 | BRT-31 v2 approved at 40% | BRENT v2 after CARL blind read | **NO** | DELEGATED | `PROME/WILL_QUEUE.md:93` |
| WQ-349 | 2026-09-30 | Withdrawn duplicate of WQ-335 | PROME registration error (no decision) | **NO** | NOT-A-RULING | `PROME/WILL_QUEUE.md:85` |
| WQ-316 | 2026-10-01 | Two Wednesday expiries rolled by Will's hand | TERRY rec (overridden on USO) / Will's own hand | **NO** | TRADE | `PROME/WILL_QUEUE.md:86` |
| WQ-351 | 2026-10-01 | FERT G5 wording clarification processed | FERT/PROME on Will's delegation | **NO** | DELEGATED | `PROME/WILL_QUEUE.md:83` |
| WQ-279 | 2026-10-01 | NYSCEF rent-freeze docket pulled by Will | Will's own browser search / FLG T-08 | **NO** |  | `PROME/WILL_QUEUE.md:82` |
| WQ-295 | 2026-10-01 | Dark-desk R2 schedule wake approved with riders | PROME plan 2026-09-26_wq295-R2 | **NO** |  | `PROME/WILL_QUEUE.md:78` |
| WQ-301 | 2026-10-01 | CoreWeave CDS anchor re-based to DTCC/ISDA | LIQUID owner grade (63b77a55b); NEXUS cohort flag incidental | **NO** |  | `PROME/WILL_QUEUE.md:80` + ledger REGISTERED 2026-09-26 row |
| WQ-334 | 2026-10-01 | Send CORAL's narrowed DBPR records request | CORAL draft request | **NO** | BATCH | `PROME/WILL_QUEUE.md:75` |
| WQ-339 | 2026-10-01 | Commission TERRY to draft a new TLT-put card | Will's own word (overrode row's stand-down) / BOND surfaces | **NO** |  | `PROME/WILL_QUEUE.md:79` + ledger UPDATED 2026-10-01 row (sources: BOND analysis/STATUS/TRADE, FORGE, TERRY card) |
| WQ-348 | 2026-10-01 | Approval inventory: nine kept, seven converted | PROME inventory record | **NO** |  | `PROME/WILL_QUEUE.md:70` |
| WQ-350 | 2026-10-01 | Signal scanner: one more fix pass and read | PROME/reviewers | **NO** |  | `PROME/WILL_QUEUE.md:81` |
| WQ-352 | 2026-10-01 | MIDAS silver/PGM bands adopted, unscored one month | MIDAS bands draft §A4 | **NO** | BATCH | `PROME/WILL_QUEUE.md:74` |
| WQ-353 | 2026-10-01 | FALCON Red Sea tanker gate leg 2 adopted provisional | FALCON letter | **NO** | BATCH | `PROME/WILL_QUEUE.md:71` |
| WQ-354 | 2026-10-01 | Legal-instrument premises: owner never adjudicates own conflict | DAEDALUS SL-6 / PROME | **NO** | BATCH | `PROME/WILL_QUEUE.md:73` |
| WQ-355 | 2026-10-01 | FALCON production-strike rung registered | FALCON proposal (fal06 rewrite) | **NO** | BATCH | `PROME/WILL_QUEUE.md:72` |
| WQ-358 | 2026-10-01 | DAEDALUS maturity-ladder readings A and B ratified | DAEDALUS production review §3 | **NO** | BATCH | `PROME/WILL_QUEUE.md:76` |
| WQ-373 | 2026-10-03 | X bookmarks pilot phase 1 approved | WALTER's three terms | **NO** |  | `PROME/WILL_QUEUE.md:66` |
| WQ-376 | 2026-10-03 | DBPR portal account activated | CORAL request / Will's hands | **NO** |  | `PROME/WILL_QUEUE.md:65` |
| WQ-242 | 2026-10-03 | CRU-11 ratio-form successor approved | CRUISE PREDICTIONS line 12 | **NO** |  | `PROME/WILL_QUEUE.md:64` |
| WQ-341 | 2026-10-03 | Root B: hold to PRED-50 grade; conditional owner pre-authorized | NEXUS WQ-340 root-attribution page (83e6fe366) — candidate Root B + PRED-50 | **YES** |  | `PROME/WILL_QUEUE.md:63` + ledger UPDATED 2026-10-01 row (sources: NEXUS page §per-line row 4 + §next link · LIQUID §1c · HENRY · WQ-337) + `AGENTS/NEXUS/analysis/2026-09-29_one-root-or-many.md` L13/L16 (Candidate Root B, effective-N 1–2) VERIFIED |
| WQ-363 | 2026-10-03 | Define X1 'sustained' (3 readings >280.0) | BROCK/LIQUID X1 card | **NO** |  | `PROME/WILL_QUEUE.md:61` |
| WQ-366 | 2026-10-03 | Hold the USO Oct-09 $150 call | Will's own read of Saudi news / TERRY card | **NO** | TRADE | `PROME/WILL_QUEUE.md:62` |
| WQ-367 | 2026-10-03 | Closeout process changes P1b/P2/P3/P4/P6 | PROME closeout proposal | **NO** |  | `PROME/WILL_QUEUE.md:60` |
| WQ-374 | 2026-10-03 | Defer PROME helper subagents | PROME revised rec | **NO** |  | `PROME/WILL_QUEUE.md:59` |
| WQ-377 | 2026-10-04 | X-bookmarks follow-ons a/b/c | WALTER + PROME recs | **NO** |  | `PROME/WILL_QUEUE.md:55` |
| WQ-379 | 2026-10-04 | Process backlog ranked; one bounded process day | PROME l600 ranked table + CATO conditions | **NO** |  | `PROME/WILL_QUEUE.md:51` |
| WQ-380 | 2026-10-04 | Decline the .env read fence | DAEDALUS/PROME | **NO** |  | `PROME/WILL_QUEUE.md:56` |
| WQ-369 | 2026-10-05 | Immediate dark-desk own-theater spawn (C8) | WALTER relay (8a2dbfa65) | **NO** |  | `PROME/WILL_QUEUE.md:50` |
| WQ-387 | 2026-10-07 | Wake TERRY/FALCON/REGINALD/FERT on laptop tonight | PROME WQ-385 preflight | **NO** | LAUNCH | `PROME/WILL_QUEUE.md:53` |

**Table A counts (109 keys):** YES **1** · CANDIDATE **3** · NO **105** · UNREADABLE **0**.

## Table B — WQ-keyed in-window Will decisions NOT in the 109 file (224 keys → 228 rows)

Date = the ruling date parsed from the row record (else the ledger `at`). Input for NO rows = the desk the row names, read from the ledger title/record (depth T) unless an artifact is given.

| key | date | decision (row title, ≤12 words) | proximate input | class | flags | artifact read |
|---|---|---|---|---|---|---|
| WQ-27 | 2026-08-12 | BRENT moneyness-band + width-bias | named desk in row: BRENT | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-21_rolloff.md:16` (depth T) |
| WQ-32a | 2026-08-12 | WAL housekeeping ⑤⑥ | named desk in row: WAL | **NO** | NOT-A-WILL-RULING? | `PROME/WQ_LEDGER.tsv row` (depth T) |
| WQ-32b | 2026-08-12 | WAL spec-repair ①–④ | named desk in row: WAL | **NO** |  | `PROME/WQ_LEDGER.tsv row` (depth T) |
| WQ-33a | 2026-08-12 | OSPREY thesis-kill repair | named desk in row: OSPREY | **NO** | NOT-A-WILL-RULING? | `PROME/WQ_LEDGER.tsv row` (depth T) |
| WQ-33b | 2026-08-12 | OSPREY EXIT RULES §3 :159 attribution clause | named desk in row: OSPREY | **NO** | NOT-A-WILL-RULING? | `PROME/WQ_LEDGER.tsv row` (depth T) |
| WQ-36a | 2026-08-12 | MIDAS L-12 + L-13 | named desk in row: MIDAS | **NO** | NOT-A-WILL-RULING? | `PROME/WQ_LEDGER.tsv row` (depth T) |
| WQ-40 | 2026-08-12 | HAWK SULPHUR-01 band-basis ruling | named desk in row: HAWK | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-08-16_rotation.md:37` (depth T) |
| WQ-42 | 2026-08-12 | WAL fence-② / OZK cell scope | named desk in row: WAL | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-21_rolloff.md:22` (depth T) |
| WQ-43 | 2026-08-12 | REG-15 ownership → WAL | named desk in row: WAL | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-21_rolloff.md:23` (depth T) |
| WQ-44 | 2026-08-12 | CARL kill-rule re-spec | named desk in row: CARL | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-21_rolloff.md:29` (depth T) |
| WQ-47 | 2026-08-13 | CREED courier | named desk in row: CREED | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-08-21_rolloff.md:13` (depth T) |
| WQ-48 | 2026-08-13 | AEOLUS Mead 1,035 re-key | named desk in row: AEOLUS | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-08-21_rolloff.md:10` (depth T) |
| WQ-17 | 2026-08-14 | Repo public flip | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-21_rolloff.md:7` (depth T) |
| WQ-20 | 2026-08-14 | Robinhood screenshot | named desk in row: ANVIL | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-08-21_rolloff.md:6` (depth T) |
| WQ-35b | 2026-08-14 | COT successor re-base | named desk in row: BRENT | **NO** | NOT-A-WILL-RULING? | `PROME/WQ_LEDGER.tsv row` (depth T) |
| WQ-36b | 2026-08-14 | L-15 revision re-grading (fleet) | named desk in row: DAEDALUS | **NO** |  | `PROME/WQ_LEDGER.tsv row` (depth T) |
| WQ-37 | 2026-08-14 | GIE/AGSI+ key | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-21_rolloff.md:8` (depth T) |
| WQ-39 | 2026-08-14 | Remote-branch disposition | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-21_rolloff.md:15` (depth T) |
| WQ-45 | 2026-08-14 | HOMER servicer-watch re-spec | named desk in row: HOMER | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-21_rolloff.md:11` (depth T) |
| WQ-46 | 2026-08-14 | HOMER GSE-condo re-key | named desk in row: HOMER | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-08-21_rolloff.md:12` (depth T) |
| WQ-49 | 2026-08-14 | Issuer-primary convention | named desk in row: DAEDALUS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-21_rolloff.md:14` (depth T) |
| WQ-50 | 2026-08-14 | Servicer-spec definitions A/B/C + rider | named desk in row: HOMER | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-21_rolloff.md:24` (depth T) |
| WQ-51 | 2026-08-14 | MIDAS-06 re-key $4,340.70 | named desk in row: MIDAS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-21_rolloff.md:25` (depth T) |
| WQ-16 | 2026-08-21 | Broker-export residue | named desk in row: ANVIL | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:48` (depth T) |
| WQ-41 | 2026-08-21 | War-risk premium source upgrade | named desk in row: FALCON | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:49` (depth T) |
| WQ-55 | 2026-08-21 | CRUISE re-class + ladder | named desk in row: CRUISE | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:50` (depth T) |
| WQ-56 | 2026-08-21 | SAM INFRAAGENDA | named desk in row: SAM | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:51` (depth T) |
| WQ-58 | 2026-08-21 | USO 35-shares exit condition | named desk in row: TERRY | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:47` (depth T) |
| WQ-64 | 2026-08-21 | VIOLET CLAUDE.md step-7 amendment | named desk in row: VIOLET | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:57` (depth T) |
| WQ-65 | 2026-08-21 | MIDAS (e) continuous basis | named desk in row: MIDAS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:59` (depth T) |
| WQ-66 | 2026-08-21 | MIDAS (f) DFII10 NO-VERDICT band | named desk in row: MIDAS | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:60` (depth T) |
| WQ-67 | 2026-08-21 | MIDAS (g) smoothed endpoints | named desk in row: MIDAS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:61` (depth T) |
| WQ-68 | 2026-08-21 | MIDAS (h) MIDAS-06 duration clause | named desk in row: MIDAS | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:62` (depth T) |
| WQ-69 | 2026-08-21 | MIDAS (i) L-13(b) upside band | named desk in row: MIDAS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:63` (depth T) |
| WQ-70 | 2026-08-21 | Batch A memory-canon two-liners | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:28` (depth T) |
| WQ-71 | 2026-08-21 | Batch B CHECKSTANDARD six-item package | named desk in row: DAEDALUS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:27` (depth T) |
| WQ-75 | 2026-08-22 | WALTER dark-owner doorbell (rule 6's missing else) | named desk in row: WALTER | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:26` (depth T) |
| WQ-76 | 2026-08-23 | two HEARTBEAT self-retractions — re-derive? | named desk in row: HEARTBEAT | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:40` (depth T) |
| WQ-77 | 2026-08-23 | OZK P-OZK-2 empty pillar | named desk in row: OZK | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:41` (depth T) |
| WQ-78 | 2026-08-23 | OZK POSITIONS PAT-025 freeze | named desk in row: OZK | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:42` (depth T) |
| WQ-79 | 2026-08-23 | HEARTBEAT §8 gold figure — which number headlines the premium | BOND re-derivation (NEXUS_BRIEF named only as encode order) | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:35` (depth D) |
| WQ-80 | 2026-08-23 | HEARTBEAT commit-gate — free it? | named desk in row: HEARTBEAT | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:39` (depth T) |
| WQ-81 | 2026-08-23 | rule-6b leg 3b — define "session" | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:38` (depth T) |
| WQ-82 | 2026-08-23 | WALTER re-score + bar re-derivation | named desk in row: WALTER | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:37` (depth T) |
| WQ-83 | 2026-08-23 | root CLAUDE.md scope-note mirror | named desk in row: HEARTBEAT | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:36` (depth T) |
| WQ-85 | 2026-08-23 | CORAL MSI leg — trigger with no falsifier | named desk in row: CORAL | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-02_rolloff.md:6` (depth T) |
| WQ-97 | 2026-08-26 | QQQ 23 sh — rec SELL | named desk in row: FORGE | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-02_rolloff.md:12` (depth T) |
| WQ-101 | 2026-08-27 | SREIT/T-06b fire word | named desk in row: CREED | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:39` (depth T) |
| WQ-102 | 2026-08-27 | carve-out-① vs OTTO:213 | named desk in row: OTTO | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:38` (depth T) |
| WQ-59 | 2026-08-27 | CARL-DR-1 FHA leg re-commission | named desk in row: CARL | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:37` (depth T) |
| WQ-90 | 2026-08-27 | C7 pilot window | named desk in row: PROME/process or Will's own | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:40` (depth T) |
| WQ-93 | 2026-08-27 | MATRIXV2 scope (BOND's kill composition-failure test) | BOND MATRIX_V2 (BOND's own matrix) | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:41` (depth D) |
| WQ-108 | 2026-08-28 | HANS / EUROPEMACRO nomination | named desk in row: HANS | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:31` (depth T) |
| WQ-110 | 2026-08-28 | FLG charter ENTITY correction | named desk in row: FLG | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:32` (depth T) |
| WQ-113 | 2026-08-28 | FORUM fin-cond T3 re-spec (LIQUID/HENRY) | named desk in row: LIQUID | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:33` (depth T) |
| WQ-89 | 2026-08-28 | GENERATED-VIEW build-or-decline | named desk in row: DAEDALUS | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:36` (depth T) |
| WQ-118 | 2026-08-29 | Root CLAUDE.md line 18 → PROME/inbox/ named as the PROME delivery address | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:24` (depth T) |
| WQ-119 | 2026-08-29 | Root CLAUDE.md small batch — carve-out count + cost-model line (RAV F1/F5) | named desk in row: RAV | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:23` (depth T) |
| WQ-120 | 2026-08-29 | Root CLAUDE.md restructure — rules vs provenance split | named desk in row: RAV | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:22` (depth T) |
| WQ-121 | 2026-08-29 | HEARTBEAT eighth re-base — STRUCTURAL (view sections removed, dashboard = single level … | named desk in row: HEARTBEAT | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:11` (depth T) |
| WQ-122 | 2026-08-29 | Root LESSONS.md + KERNELS.md — retire → REFRESH in place | named desk in row: FORGE | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:19` (depth T) |
| WQ-123 | 2026-08-29 | AGENTS.md condense | named desk in row: FERT | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:20` (depth T) |
| WQ-124 | 2026-08-29 | README.md refresh | named desk in row: FORGE | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:21` (depth T) |
| WQ-125 | 2026-08-29 | FORGE reconcile 8/29 commit | named desk in row: FORGE | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:18` (depth T) |
| WQ-126 | 2026-08-29 | Robinhood QQQ $715P 8/31 intent | named desk in row: FORGE | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:17` (depth T) |
| WQ-127 | 2026-08-29 | Retire .github/workflows/feeds.yml (SENTRY feed fetch) | named desk in row: SENTRY | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:16` (depth T) |
| WQ-128 | 2026-08-29 | AGENTS.md re-shape (Codex relayed review) | named desk in row: Codex | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:15` (depth T) |
| WQ-129 | 2026-08-29 | KERNELS.md re-shape (Codex relayed review) | named desk in row: Codex | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:14` (depth T) |
| WQ-130 | 2026-08-29 | Retire root LESSONS.md (Codex relayed review) | named desk in row: Codex | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:13` (depth T) |
| WQ-131 | 2026-08-29 | GATES.tsv current-state / history split | named desk in row: Codex | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:12` (depth T) |
| WQ-132 | 2026-08-29 | ACTIVEDECISIONS: retire three no-standing-decision rows | named desk in row: WALTER | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:10` (depth T) |
| WQ-134 | 2026-08-29 | Boot-path slim-down batch (Codex-amended) — item 0 NETWORK.md mermaid ↔ table edges | named desk in row: Codex | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:9` (depth T) |
| WQ-135 | 2026-08-29 | Root CLAUDE.md:24 non-launch vocabulary — "shelved" → "dormant, or retired" (ROSTER' | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-06_rolloff.md:8` (depth T) |
| WQ-136 | 2026-08-30 | T6 rows 72/73 disposition + the three spec-authoring rules | named desk in row: DAEDALUS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-07_rolloff.md:13` (depth T) |
| WQ-137 | 2026-08-30 | Root CLAUDE.md post-audit batch A–H (Will-requested audit → Codex-amended) | named desk in row: Codex | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-07_rolloff.md:12` (depth T) |
| WQ-138 | 2026-08-30 | DOCKET.tsv terminal-row compaction (trim-targets survey item 1) | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-07_rolloff.md:11` (depth T) |
| WQ-139 | 2026-08-30 | Trim-batch items 2–4 (same "Ok go ahead" ruling as 138) | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-07_rolloff.md:10` (depth T) |
| WQ-140 | 2026-08-30 | Codex process-reform batch (8 items, Codex-amended 2nd round) | named desk in row: Codex | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-07_rolloff.md:9` (depth T) |
| WQ-141 | 2026-08-30 | EIA Today in Energy RSS → RESEARCH-INTAKE (WQ-127 gap; WALTER YES 8/30 … | named desk in row: WALTER | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-07_rolloff.md:8` (depth T) |
| WQ-72 | 2026-08-30 | T6 conjunctive-clause word + the joint T+1 publication rider | named desk in row: MIDAS | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-09-07_rolloff.md:15` (depth T) |
| WQ-73 | 2026-08-30 | BOND T6 frozen-text repairs + the fresh-high vs >5.28 DIVERGENCE clause | named desk in row: BOND | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-09-07_rolloff.md:14` (depth T) |
| WQ-100 | 2026-09-01 | ODCE/$1B "major fund" forward definition (T-06b) | named desk in row: CREED | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:21` (depth T) |
| WQ-103 | 2026-09-01 | Kernel Sitting-2 window | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:9` (depth T) |
| WQ-104 | 2026-09-01 | CARL-DR-1 aggregation rule | named desk in row: CARL | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:8` (depth T) |
| WQ-105 | 2026-09-01 | NEXUS amendment 12 + the falsifier it fired | NEXUS 8/28 packet: amendment-12 escalation + its own watch prediction graded (f4489b77a); object = NEXUS brief schema | **CANDIDATE**-S | S;N | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:20 + proposals/2026-09-01_wq-batch-RULED.md:20 + pre-ruling row git a159365ae^:PROME/WILL_QUEUE.md:38` (depth D) |
| WQ-106 | 2026-09-01 | Five HY-260 persistence counts | LIQUID packet + PROME count (five HY-260 counts) | **NO** |  | `PROME/pre-ruling row git a159365ae^:PROME/WILL_QUEUE.md:39` (depth D) |
| WQ-107 | 2026-09-01 | OTTO's CARL-V2 downgrade table — who registers | named desk in row: OTTO | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:18` (depth T) |
| WQ-109 | 2026-09-01 | DAEDALUS sweep proposals P1–P5 | named desk in row: DAEDALUS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:17` (depth T) |
| WQ-111 | 2026-09-01 | WALTER: prevention findings need a push surface | named desk in row: WALTER | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:16` (depth T) |
| WQ-112 | 2026-09-01 | Canon gap: scoring vintage for re-marked confidence | named desk in row: DAEDALUS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:15` (depth T) |
| WQ-114 | 2026-09-01 | GATE-LIQ-069 unnamed sub-thresholds | named desk in row: LIQUID | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:14` (depth T) |
| WQ-115 | 2026-09-01 | symptoms: backfill sweep + rename question | named desk in row: DAEDALUS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:13` (depth T) |
| WQ-116 | 2026-09-01 | BROCK's two lines need re-spec | named desk in row: BROCK | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:12` (depth T) |
| WQ-117 | 2026-09-01 | DAEDALUS three-encodes bundle | named desk in row: DAEDALUS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:11` (depth T) |
| WQ-142 | 2026-09-01 | DFII10 NO-VERDICT band for successor rows | named desk in row: MIDAS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-09_rolloff.md:18` (depth T) |
| WQ-143 | 2026-09-01 | WAL Sep-18 67.5/70P pair after REG-T-02 FIRED (WAL $77.26 [9/1]) | named desk in row: WAL | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-09_rolloff.md:17` (depth T) |
| WQ-144 | 2026-09-01 | Approve the staged WAL Dec-18 $70P roll card | named desk in row: WAL | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-09_rolloff.md:16` (depth T) |
| WQ-145 | 2026-09-01 | USO Oct-16 $135C ×2 management terms | named desk in row: TERRY | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-09_rolloff.md:15` (depth T) |
| WQ-146 | 2026-09-01 | LABOR summons (dark since 8/28 through ISM/JOLTS/OPM/NFP) | named desk in row: LABOR | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-09_rolloff.md:14` (depth T) |
| WQ-147 | 2026-09-01 | Staleness sweep M1 — --all honors # Cadence: declared-quiet tokens | named desk in row: DAEDALUS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-09_rolloff.md:12` (depth T) |
| WQ-148 | 2026-09-01 | Canonical ATTENTION clock — key name | named desk in row: DAEDALUS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-09_rolloff.md:13` (depth T) |
| WQ-149 | 2026-09-01 | Sitting-2 mint amendment — E pins MIDAS CMD-01a05d61 | named desk in row: MIDAS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-09_rolloff.md:10` (depth T) |
| WQ-150 | 2026-09-01 | Root carve-out ④ vs runbook §successor scope | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-09_rolloff.md:11` (depth T) |
| WQ-152 | 2026-09-01 | DAEDALUS → L5 | named desk in row: DAEDALUS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-09_rolloff.md:9` (depth T) |
| WQ-153 | 2026-09-01 | WQ-117 leg C axis form | named desk in row: DAEDALUS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-09_rolloff.md:8` (depth T) |
| WQ-84 | 2026-09-01 | Rule-6b leg 3b self-normalising doorbell | named desk in row: HENRY | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:30` (depth T) |
| WQ-86 | 2026-09-01 | Registration join rule (owner→GATES, registrar→owner) | named desk in row: CORAL | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:29` (depth T) |
| WQ-87 | 2026-09-01 | OSPREY 8/17 ruling conflict + band re-centre | named desk in row: OSPREY | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:28` (depth T) |
| WQ-88 | 2026-09-01 | GATE-LIQ-076 W1 blind to orderly exits | named desk in row: LIQUID | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:27` (depth T) |
| WQ-91 | 2026-09-01 | MIDAS moving-referent class | named desk in row: MIDAS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:26` (depth T) |
| WQ-92 | 2026-09-01 | VX-CREED-4.01 baseline not reproducible | named desk in row: CREED | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:25` (depth T) |
| WQ-94 | 2026-09-01 | TERRY rule-#20 write-up for the HELD USO 135C ×2 | named desk in row: TERRY | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:24` (depth T) |
| WQ-95 | 2026-09-01 | Archive TRY-WILL-QQQFADE | named desk in row: TERRY | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:23` (depth T) |
| WQ-96 | 2026-09-01 | Root-canon line: pathspec-less / --allow-empty commits sweep the shared index | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:10` (depth T) |
| WQ-99 | 2026-09-01 | Which definition governs BOND's TLT-put ADD re-arm | named desk in row: BOND | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:22` (depth T) |
| WQ-154 | 2026-09-02 | CARL PREDICTIONS mirror → own file | named desk in row: CARL | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-09-10_rolloff.md:10` (depth T) |
| WQ-155 | 2026-09-02 | Kernel Sitting 2 — C8 ruling package | named desk in row: DAEDALUS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-10_rolloff.md:9` (depth T) |
| WQ-156 | 2026-09-02 | LABOR summons for the 9/3–9/4 cluster | named desk in row: LABOR | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-10_rolloff.md:8` (depth T) |
| 163·1 | 2026-09-02 | NEXUS PREDICTIONS_MONITOR is a whole boot read | DAEDALUS adjudication memo (213ef8963) of NEXUS slate item 1; object = NEXUS's own file | **NO** | OBJ-NEXUS | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:77 + proposals/2026-09-07_wq163-183-190-191-RULED.md:5-8 + git show 14ab0739c:PROME/WILL_QUEUE.md row 163 (L32) + AGENTS/NEXUS/proposals/2026-09-02_self-audit-improvement-slate.md` (depth T) |
| WQ-158 | 2026-09-03 | BROCK redemption-register re-spec → GATE-BRK-R2 | named desk in row: BROCK | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-10_evening_rolloff.md:13` (depth T) |
| 163·⑥ | 2026-09-03 | Let NEXUS's pre-event pin of T-12 C#2 window stand | NEXUS 9/3 pin of its own split-gate window | **CANDIDATE**-S | S | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:77 + proposals/2026-09-07_wq163-183-190-191-RULED.md:5-8 + git show 14ab0739c:PROME/WILL_QUEUE.md row 163 (L32) + AGENTS/NEXUS/proposals/2026-09-02_self-audit-improvement-slate.md` (depth D) |
| WQ-165 | 2026-09-03 | Cold-read stop rule | named desk in row: HEARTBEAT | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-10_evening_rolloff.md:16` (depth T) |
| WQ-166 | 2026-09-03 | GATES.tsv two-state split | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-10_evening_rolloff.md:14` (depth T) |
| WQ-167 | 2026-09-03 | The two operator facts → UNKNOWN | named desk in row: WAL | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-10_evening_rolloff.md:15` (depth T) |
| WQ-168 | 2026-09-03 | XLE/WAL/KRE Sep-18 & Sep-30 expiry cluster — rows ①–⑦ (LAPSE/HOLD/exit tests) | named desk in row: WAL | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-10_evening_rolloff.md:8` (depth T) |
| WQ-170 | 2026-09-03 | GATE-LIQ-069 L4 cohort rule | named desk in row: LIQUID | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-10_evening_rolloff.md:12` (depth T) |
| WQ-171 | 2026-09-03 | Codex audit legs — commit-subject rule · KERNEL status · receipt/sidecar commission | named desk in row: Codex | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-10_evening_rolloff.md:10` (depth T) |
| WQ-172 | 2026-09-03 | PREDICTIONDISCIPLINE negative-existence amendment | named desk in row: FORGE | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-10_evening_rolloff.md:11` (depth T) |
| WQ-173 | 2026-09-04 | BROCK convergence second leg (BDC NAV-discount) | BROCK's own convergence score (57/70) | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-10_evening_rolloff.md:9` (depth D) |
| WQ-174 | 2026-09-04 | WALTER BOARD/INDEX generate-in-place (three legs) | named desk in row: WALTER | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-11_night_rolloff.md:8` (depth T) |
| WQ-175 | 2026-09-04 | FROZEN-ON-REVISABLE threshold kind (two clauses) + LABOR vintage table | named desk in row: LABOR | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-11_night_rolloff.md:7` (depth T) |
| WQ-176 | 2026-09-04 | GATES.tsv step-3 compaction (three legs) | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-11_night_rolloff.md:4` (depth T) |
| WQ-177 | 2026-09-04 | VIOLET 7/1 tail-hedge framework (ARMED, 64d stale) | named desk in row: VIOLET | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-11_night_rolloff.md:5` (depth T) |
| WQ-178 | 2026-09-04 | Verification cascade — five process fixes | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-11_night_rolloff.md:6` (depth T) |
| WQ-180 | 2026-09-05 | Utility maturity ladder — calibration loop as a graded L3 leg | named desk in row: DAEDALUS | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:84` (depth T) |
| WQ-184 | 2026-09-05 | The SPAWN DRIVER — L0 rule + spawnlist.py + the L2 digest … | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:83` (depth T) |
| WQ-185 | 2026-09-06 | Codex's overall assessment — four legs + the 9/6 Codex amendment (leg … | named desk in row: Codex | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:86` (depth T) |
| WQ-186 | 2026-09-06 | Slate: RED + VIOLET Tuesday pre-open spawns on FT-10 2-of-4 | named desk in row: RED | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:87` (depth T) |
| WQ-188 | 2026-09-06 | VIOLET two fixes before the thesis read (Codex 9/6 ledger-repair review) | named desk in row: VIOLET | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:85` (depth T) |
| 163·3 | 2026-09-07 | Amendment to a frozen instrument re-earns its certificate (fleet canon) | NEXUS self-audit slate item 3 (falsifier graded / discriminated) | **CANDIDATE**-N | N;BATCH | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:77 + proposals/2026-09-07_wq163-183-190-191-RULED.md:5-8 + git show 14ab0739c:PROME/WILL_QUEUE.md row 163 (L32) + AGENTS/NEXUS/proposals/2026-09-02_self-audit-improvement-slate.md` (depth D) |
| 163·4 | 2026-09-07 | A >=3-desk collision on one series forces re-spec; DAEDALUS chooses | NEXUS self-audit slate item 4: Disc-H convergence count (4 desks on HY<260 s3) | **CANDIDATE**-N(convergence) | N(convergence);BATCH | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:77 + proposals/2026-09-07_wq163-183-190-191-RULED.md:5-8 + git show 14ab0739c:PROME/WILL_QUEUE.md row 163 (L32) + AGENTS/NEXUS/proposals/2026-09-02_self-audit-improvement-slate.md` (depth D) |
| 163·⑤ | 2026-09-07 | No spend; T-12 admission gate runs on existing feeds | NEXUS slate item ⑤ (split-gate feed ask) | **CANDIDATE**-S | S;BATCH | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:77 + proposals/2026-09-07_wq163-183-190-191-RULED.md:5-8 + git show 14ab0739c:PROME/WILL_QUEUE.md row 163 (L32) + AGENTS/NEXUS/proposals/2026-09-02_self-audit-improvement-slate.md` (depth D) |
| WQ-179 | 2026-09-07 | LABOR read-cap escalation — the WRITE MODE, fleet-wide | named desk in row: LABOR | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:78` (depth T) |
| WQ-183 | 2026-09-07 | STUE read mode + the pen — APPROVED; PARENT HOLDS THE PEN | named desk in row: STUE | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:74` (depth T) |
| WQ-189 | 2026-09-07 | Frame-breaker instance ③ "vessel SUNK" — capacity floor | named desk in row: BRENT | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:82` (depth T) |
| WQ-190 | 2026-09-07 | ORACLE v4 instrument succession — RATIFIED as one package | named desk in row: ORACLE | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:75` (depth T) |
| WQ-191 | 2026-09-07 | S1 owner-unconsumed line — LAPSE, SUPERSEDED-BY-WQ-184 | PROME rec (WQ-184 supersedes S1) + WALTER veto; NEXUS only wrote the re-open condition | **NO** | OBJ-NEXUS-ADJ | `PROME/proposals/2026-09-07_wq163-183-190-191-RULED.md:10-11` (depth D) |
| WQ-192 | 2026-09-07 | Deploy question on the M/T Kylo sinking — STAND DOWN | named desk in row: BRENT | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:81` (depth T) |
| WQ-193 | 2026-09-07 | LABOR charter batch — split + 7 corrections + 2 adds + … | named desk in row: LABOR | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:79` (depth T) |
| WQ-194 | 2026-09-07 | LABOR scoring vintage — registered in error, WITHDRAWN | named desk in row: LABOR | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:80` (depth T) |
| WQ-133 | 2026-09-10 | PROME hygiene carry | named desk in row: Deck | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:62` (depth T) |
| WQ-160 | 2026-09-10 | HAW-19 LEG A unfireable as registered | named desk in row: Deck | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:59` (depth T) |
| WQ-161 | 2026-09-10 | Prediction canon — non-resolution branch carries no mass · mass-neutral retrofit test … | MIDAS<->ZHAO raise (NEXUS = consumer packet only) | **NO** |  | `PROME/proposals/2026-09-10_wq161-prediction-canon-RULED.md:4` (depth D) |
| WQ-181 | 2026-09-10 | YEYOU dormancy ② — the vacuous "zero YEYOU flags" L5 leg | named desk in row: YEYOU | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:57` (depth T) |
| WQ-182 | 2026-09-10 | CARL V16 drop-back branch | named desk in row: CARL | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:60` (depth T) |
| WQ-200 | 2026-09-10 | USO 37-share management card | named desk in row: Deck | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:56` (depth T) |
| WQ-201 | 2026-09-10 | TLT Sep-30 $85P limit re-price | named desk in row: FORGE | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:64` (depth T) |
| WQ-202 | 2026-09-10 | Decision Deck v1 + tap-to-rule | named desk in row: Deck | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:63` (depth T) |
| WQ-203 | 2026-09-10 | WQ LEDGER — one append-only TSV for every Will decision | named desk in row: Deck | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:53` (depth T) |
| WQ-205 | 2026-09-10 | REQ-DEWEY-20260829-002 — NVDA vendor financing (deadline Tue 9/15, DOCKET L244) | named desk in row: DEWEY | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:52` (depth T) |
| WQ-206 | 2026-09-10 | Aged ACTION-line backlog rule + WALTER §WILLNEEDS deck feed | named desk in row: WALTER | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:55` (depth T) |
| WQ-207 | 2026-09-10 | USO Sep-18 150/165 call spread ×1 (Robinhood) — TERRY card TRY-MGMT-USORH150165 OPTION … | named desk in row: TERRY | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:54` (depth T) |
| WQ-208 | 2026-09-10 | HAW-18 scoring-vintage eligibility — 60% vs the corrected 55% | named desk in row: Deck | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:51` (depth T) |
| WQ-209 | 2026-09-10 | PHAN spawn (CARL's sub-agent, +56d) | named desk in row: PHAN | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:50` (depth T) |
| WQ-211 | 2026-09-10 | HAWK batch-2 rule decisions — N6 AGREEMENT rule · TRADE01 adoption-stage | named desk in row: HAWK | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:49` (depth T) |
| WQ-212 | 2026-09-10 | HAW-19 disposition on 9/30 + the capacity-only SUCCESSOR | named desk in row: Deck | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:48` (depth T) |
| WQ-214 | 2026-09-10 | LABOR charter — EXIT-RULES vintage sweep unconditional at every C1 | named desk in row: LABOR | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:47` (depth T) |
| WQ-215 | 2026-09-10 | CREED-T-08a basis declaration | named desk in row: CREED | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:42` (depth T) |
| WQ-217 | 2026-09-10 | TLT Sep-30 $77P — the ×20 after Will's ×5 sale | named desk in row: Deck | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:46` (depth T) |
| WQ-218 | 2026-09-10 | CRUISE — NCLH / CCL watch rows re-graded | named desk in row: CRUISE | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:45` (depth T) |
| WQ-220 | 2026-09-10 | Quartr connector UNENTITLED | named desk in row: Deck | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:43` (depth T) |
| WQ-221 | 2026-09-10 | Aged "waits on others" rule — WQ-206 extended to the deck's third … | named desk in row: OSPREY | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:40` (depth T) |
| WQ-222 | 2026-09-10 | CRUISE — VX-CRU-06 falsifier: ONE number · ONE base · ONE window | named desk in row: CRUISE | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:41` (depth T) |
| WQ-74 | 2026-09-10 | Row-58 oil exit LEVELS return for ratification | named desk in row: TERRY | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:44` (depth T) |
| WQ-98 | 2026-09-10 | Broker records when convenient | named desk in row: Deck | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:61` (depth T) |
| WQ-216 | 2026-09-11 | OSPREY × HAWK joint Russia/Ukraine strike taxonomy (was OWED-23, waiting since 8/20) | named desk in row: OSPREY | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:39` (depth T) |
| WQ-227 | 2026-09-11 | Exempt-desk closeout self-assertion (spec §3.5.6 option (b)) — adopt or not | named desk in row: CRUISE | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:35` (depth T) |
| WQ-233 | 2026-09-11 | STATUS re-base — current state in STATUS, session history to the archive | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:34` (depth T) |
| WQ-249 | 2026-09-14 | Spawn-closeout discipline — a spawn is not complete until the desk has … | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:29` (depth T) |
| WQ-253 | 2026-09-15 | SL-5 tie-set rule: carry it in PREDICTIONDISCIPLINE.md, or point at it? | named desk in row: FORGE | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:28` (depth T) |
| WQ-285 | 2026-09-24 | YURI SHARED-SURFACE ROWS — RULED: APPROVED as written | named desk in row: YURI | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:18` (depth T) |
| WQ-151 | 2026-09-26 | Reconciled existing ruling | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:65` (depth T) |
| WQ-159 | 2026-09-26 | Reconciled existing ruling | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:66` (depth T) |
| WQ-162 | 2026-09-26 | Reconciled existing ruling | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:67` (depth T) |
| WQ-164 | 2026-09-26 | Reconciled existing ruling | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:68` (depth T) |
| WQ-195 | 2026-09-26 | FALCON next rung and attacker-axis consequence | named desk in row: FALCON | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:73` (depth T) |
| WQ-196 | 2026-09-26 | OSPREY direct ruling reconciled | named desk in row: OSPREY | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:69` (depth T) |
| WQ-197 | 2026-09-26 | OSPREY direct ruling reconciled | named desk in row: OSPREY | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:70` (depth T) |
| WQ-198 | 2026-09-26 | OSPREY direct ruling reconciled | named desk in row: OSPREY | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:71` (depth T) |
| WQ-199 | 2026-09-26 | OSPREY direct ruling reconciled | named desk in row: OSPREY | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:72` (depth T) |
| WQ-240 | 2026-09-26 | Closeout simplification + L338 sizing decision | named desk in row: PROME/process or Will's own | **NO** | NOT-A-WILL-RULING? | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:32` (depth T) |
| WQ-268 | 2026-09-26 | Spawn-driver review — RULED: adopt the number, reject the clause's own remedy | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:11` (depth T) |
| WQ-269 | 2026-09-26 | Desk cadence — RULED: WIRE IT NOW | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:12` (depth T) |
| WQ-270 | 2026-09-26 | ARGUS trial — RULED: KEEP, on the per-run evidence | named desk in row: ARGUS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md:13` (depth T) |
| WQ-299 | 2026-09-26 | PROME SELF-CORRECTION REFORM — RULED: R1–R4 APPROVED as revised, with clarifications | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/WILL_QUEUE.md:139` (depth T) |
| WQ-308 | 2026-09-27 | FORGE RECONCILE TO THE 9/25 CLOSE — APPROVED and COMMITTED (f39c70073, PROME … | named desk in row: FORGE | **NO** | NOT-A-WILL-RULING? | `PROME/WILL_QUEUE.md:126` (depth T) |
| WQ-309 | 2026-09-27 | SIGNATURE-SALE RELEVANCE READ — no usable loss-rate comparison; a conditional Dec-2023 valuation … | named desk in row: CREED | **NO** |  | `PROME/WILL_QUEUE.md:121` (depth T) |
| WQ-310 | 2026-09-27 | FAIRFAX CPAN SUBSCRIPTION ($150/qtr) — DEFERRED; EGBN Q3 deck is the checkpoint, … | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/WILL_QUEUE.md:122` (depth T) |
| WQ-311 | 2026-09-27 | VLY BOUNDED ASSIGNMENT — delivered: NEITHER, one bank-specific early flag; Q3 a … | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/WILL_QUEUE.md:123` (depth T) |
| WQ-312 | 2026-09-27 | ONE-TIME Q2 WORKOUT CHECK — delivered; no recurring ledger | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/WILL_QUEUE.md:124` (depth T) |
| WQ-313 | 2026-09-27 | Q3 TARGETED FIVE-ITEM READ — folded into the desks' Q3 work; SCHEDULED … | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/WILL_QUEUE.md:125` (depth T) |
| WQ-315 | 2026-09-28 | WEDNESDAY 9/30 EXPIRIES (QQQ 730P ×10 · USO 159C ×2) — TERRY … | named desk in row: TERRY | **NO** |  | `PROME/WILL_QUEUE.md:119` (depth T) |
| WQ-323 | 2026-09-28 | CCC REFINANCING WALL 2027–28 BY INDUSTRY — BOND bounded attempt, free sources … | named desk in row: BOND | **NO** |  | `PROME/WILL_QUEUE.md:113` (depth T) |
| WQ-326 | 2026-09-28 | FORGE MIRROR FILLS PASS — COMMITTED as edited (QQQ 730P ×9 · … | named desk in row: FORGE | **NO** |  | `PROME/WILL_QUEUE.md:107` (depth T) |
| WQ-327 | 2026-09-28 | BOND COVERAGE JOB 1+2+3 (fed-path futures in the session pull · both … | named desk in row: BOND | **NO** |  | `PROME/WILL_QUEUE.md:105` (depth T) |
| WQ-328 | 2026-09-28 | WAL HOTEL EXPOSURE — ONE bounded WAL session before the 10/13 print … | named desk in row: WAL | **NO** |  | `PROME/WILL_QUEUE.md:104` (depth T) |
| WQ-329 | 2026-09-28 | BRENT SIX-ITEM SCOPE (energy desk, week of 9/28) — scheduled grades kept … | named desk in row: BRENT | **NO** |  | `PROME/WILL_QUEUE.md:103` (depth T) |
| WQ-330 | 2026-09-28 | VLO HELD SHARE (×1) — MANAGEMENT RULE: BOTH (A: Nov crack settlement … | named desk in row: TERRY | **NO** |  | `PROME/WILL_QUEUE.md:102` (depth T) |
| WQ-331 | 2026-09-28 | BRENT PHASE-MAP AMENDMENTS — P1 · P2 · P4 APPROVED AS WRITTEN; … | named desk in row: BRENT | **NO** |  | `PROME/WILL_QUEUE.md:101` (depth T) |
| WQ-333 | 2026-09-28 | VIOLET CHARTER LINE (AGENTS/VIOLET/CLAUDE.md:194 "Last refreshed 2026-08-18") — RULED: POINTER FORM | named desk in row: VIOLET | **NO** |  | `PROME/WILL_QUEUE.md:100` (depth T) |
| WQ-336 | 2026-09-29 | REGISTER SAM-42 (BOJ no hike by 10/31, P(hike) 25% vs market ~36%) … | named desk in row: SAM | **NO** |  | `PROME/WILL_QUEUE.md:99` (depth T) |
| WQ-338 | 2026-09-29 | HOMER A3/A4 BAND RETUNES — RULED IN HOMER'S WINDOW (Will directly, AskUserQuestion, … | named desk in row: HOMER | **NO** | NOT-A-WILL-RULING? | `PROME/WILL_QUEUE.md:98` (depth T) |
| WQ-340 | 2026-09-29 | ONE ROOT OR MANY? — NEXUS one-page root-attribution of this week's fired … | Will's own question ("patterns or transmission chains?") + 7 domain-desk fired lines; NEXUS page is the OUTPUT | **NO** | LAUNCH-OF-NEXUS | `PROME/WILL_QUEUE.md:97 + AGENTS/NEXUS/inbox/processed/2026-09-29_from-PROME_WQ-340-...APPROVED.md` (depth D) |
| WQ-343 | 2026-09-29 | NEXUS CADENCE — a dated weekly TUESDAY wake row on the DOCKET … | NEXUS debrief C3 proposal (6efb45d52); object = NEXUS's own wake cadence | **CANDIDATE**-S | S;N | `PROME/WILL_QUEUE.md:96` (depth D) |
| WQ-356 | 2026-10-01 | CREED THESIS, HYPOTHESIS 1 — 'EXTEND-AND-PRETEND' REWORDED — RULED: APPROVED (CREED's wording, … | named desk in row: CREED | **NO** | NOT-A-WILL-RULING? | `PROME/WILL_QUEUE.md:84` (depth T) |
| WQ-359 | 2026-10-01 | THE SEC FILING PULLS CARRY YOUR EMAIL AS THE REQUIRED CONTACT — … | named desk in row: WALTER | **NO** | NOT-A-WILL-RULING? | `PROME/WILL_QUEUE.md:77` (depth T) |
| WQ-361 | 2026-10-01 | FINISH WQ-348's CARD-PREP LINE (C5) — ONE FIX AND ONE MORE READ … | named desk in row: PROME/process or Will's own | **NO** | NOT-A-WILL-RULING? | `PROME/WILL_QUEUE.md:69` (depth T) |
| WQ-362 | 2026-10-01 | KPLER's UNANSWERED 9/27 REPLY TO THE 9/26 PRICING INQUIRY — RULED: LAPSE … | named desk in row: PROME/process or Will's own | **NO** | NOT-A-WILL-RULING? | `PROME/WILL_QUEUE.md:68` (depth T) |
| WQ-372 | 2026-10-02 | THREE WILL-FACING PAGES → TWO: RETIRE FLEET-OPS AS A PUBLISHED PAGE, FOLD … | named desk in row: PROME/process or Will's own | **NO** | NOT-A-WILL-RULING? | `PROME/WILL_QUEUE.md:67` (depth T) |
| WQ-280 | 2026-10-03 | TLT-put ADD re-arm (9/23 5Y composition failure) — RULED: NO ADD to … | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:26` (depth T) |
| WQ-281 | 2026-10-03 | CRL-08 gasoline ≥$4.50 — RULED: the SUSTAINED 2-week bar governs | named desk in row: PROME/process or Will's own | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:27` (depth T) |
| WQ-282 | 2026-10-03 | GATE-TERRY-VLO-SCALE — RULED: REGISTERED, letter verbatim | named desk in row: TERRY | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:21` (depth T) |
| WQ-284 | 2026-10-03 | WAKE HOMER — OVERTAKEN by Will's own launch (homer-20 live 18:1x ET); … | named desk in row: HOMER | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:15` (depth T) |
| WQ-286 | 2026-10-03 | DAEDALUS STALENESS #5 — RULED with PROME's recs: ① BARON freeze APPROVED … | named desk in row: DAEDALUS | **NO** |  | `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md:19` (depth T) |
| WQ-383 | 2026-10-04 | X-BOOKMARKS: BRIGHT DATA — RULED: TRY THE FREE TIER (PROME's revised rec, … | named desk in row: WALTER | **NO** | NOT-A-WILL-RULING? | `PROME/WILL_QUEUE.md:57` (depth T) |
| WQ-384 | 2026-10-04 | X-BOOKMARKS DEFAULT-DIG — RULED: CATO's REVIEW COUNTS AS THE INDEPENDENT READ (PROME's … | named desk in row: CATO | **NO** | NOT-A-WILL-RULING? | `PROME/WILL_QUEUE.md:58` (depth T) |
| WQ-385 | 2026-10-05 | RUNTIME COMPATIBILITY — RULED: APPROVE | named desk in row: Codex | **NO** |  | `PROME/WILL_QUEUE.md:54` (depth T) |
| WQ-386 | 2026-10-07 | VLO HELD-SHARE DECEMBER BASIS — RULED APPROVED | named desk in row: TERRY | **NO** | NOT-A-WILL-RULING? | `PROME/WILL_QUEUE.md:52` (depth T) |

**Table B counts (228 rows):** YES **0** · CANDIDATE **6** · NO **222** · UNREADABLE **0**. (Rows flagged NOT-A-WILL-RULING? are CLOSED-BY-PROME / OVERTAKEN / SUPERSEDED / no-verdict closes — kept for completeness.)

## Table C — Will decisions in the window with NO WQ number

**Method and its limit (stated as required):** grep for `Will-ruled` · `Will in-session` · `Will approved` (case-insensitive) in `PROME/GATES.tsv`, `PROME/DOCKET.tsv` and `PROME/proposals/*RULED*.md`, keeping hits with an in-window date and no WQ/row number within ±250 characters (103 in-window hits → 62 without a nearby WQ number; those that map to a WQ already in Table A/B, are out of window, or are not a Will ruling were dropped by reading). Plus the 12 unnumbered "| — …" rows found in the WILL_QUEUE archives. **This is a PATTERN-SET claim, not a complete enumeration:** a Will decision recorded with other wording ("Will's word", "on your word", "tap via Decision Deck"), or only in a desk's own files, a FORUM rulings record, HEARTBEAT, or a commit message, is not covered. DOCKET.tsv was dirty in the working tree at read time; line numbers are as read on 2026-10-07.

| key | date | decision (≤12 words) | proximate input | class | flags | artifact read |
|---|---|---|---|---|---|---|
| `PROME/GATES.tsv:10` = `DOCKET.tsv:36` (GATE-NEXUS-SEAT-01) | 2026-08-08 00:0x | Register this falsifier against NEXUS's own seat | NEXUS's dissent post §8 (NEXUS proposed it against itself) | **CANDIDATE-S** | S;N — registering the test cannot be evidence for the tested layer | GATES.tsv:10, DOCKET.tsv:36, `FORUM/2026-08-07_system-review/08_dissent/06_PROME_rulings-record-and-reconciliation.md:17` VERIFIED |
| `GATES.tsv:11` = `DOCKET.tsv:37` (GATE-OP-SCALE-01) | 2026-08-08 | Register TERRY's operation-level falsifier | TERRY dissent post | NO | | GATES.tsv:11 |
| `GATES.tsv:3` (H-2 counting rule) | 2026-08-10 | Joint fire of HY gate + HENRY leg = one event | fin-cond forum FINAL §2b (HENRY joint synthesis) | NO | | GATES.tsv:3 |
| `DOCKET.tsv:15` / `:16` | 2026-08-10 | Fin-cond slate items 6 (T7 frozen) and 5 registered | HENRY joint synthesis FINAL | NO | BATCH | DOCKET.tsv:15–16 |
| `DOCKET.tsv:42` (C-36) | 2026-08-10 | C-36 label CONFIRM → CONTESTED ~50% (Will in BOND's session) | BOND's own self-downgrade on BOND STATUS. The object is a NEXUS convergence row (C-36 is in `AGENTS/NEXUS/CONFIRMED.md:18`), but NEXUS's board was STALE and not the input | NO | OBJ-NEXUS | DOCKET.tsv:42; `AGENTS/NEXUS/brief_fallback_log.tsv:40` ("My board had been asserting 'BOND has not ruled'…") VERIFIED |
| `DOCKET.tsv:172–176` (+`:299`) | 2026-08-11 | Forum-4 N10/N11-ii/N12/N13 deferrals + withdrawal-test riders | SAM joint synthesis FINAL (positioning forum) | NO | BATCH | DOCKET.tsv:172–176, `FORUM/2026-08-10_positioning-exhaustion/04_synthesis/07_PROME_rulings-record.md` |
| `DOCKET.tsv:181` | 2026-08-13 | OZK 2025Q3 MI3 re-designation adjudication routed | REGINALD/OZK | NO | | DOCKET.tsv:181 |
| `DOCKET.tsv:10` / `:14` | 2026-08-15 | FALCON R3 HOLD; HAWK sunset checkpoint conditioned | FALCON/BRENT; HAWK | NO | | DOCKET.tsv:10, :14 |
| `DOCKET.tsv:192` | 2026-08-16 | FERT re-chartered as event-driven specialist | FERT/DAEDALUS | NO | | DOCKET.tsv:192 |
| `DOCKET.tsv:203` / `:204` | 2026-08-17 | FERT G5 / G3 gates ratified | FERT | NO | | DOCKET.tsv:203–204 |
| `DOCKET.tsv:206` | 2026-08-17 eve | Commission NEXUS self-audit slate + DAEDALUS blind leg | PROME rec on the war-triad self-audit pattern | NO | LAUNCH-OF-NEXUS | DOCKET.tsv:206; `AGENTS/NEXUS/inbox/processed/2026-08-17_from-PROME_commission-self-audit-slate-post-falsifier.md` VERIFIED |
| `DOCKET.tsv:207` | 2026-08-17 | Forum-6 R9 declined | DAEDALUS synthesis draft R9 | NO | | DOCKET.tsv:207 |
| `DOCKET.tsv:28` | 2026-08-18 | Potash is triage-only at FERT | FERT/PROME | NO | | DOCKET.tsv:28 |
| `DOCKET.tsv:212` | 2026-08-19 | Don't scramble BOND for the auction | PROME/BOND | NO | | DOCKET.tsv:212 |
| `proposals/2026-08-19_004-rulings-B-C-RULED.md:1` | 2026-08-19 | TRY-FIRE-004 rulings B + C (arm-#2 reset / exit) | TERRY/BOND card | NO | TRADE | that file:1 |
| `DOCKET.tsv:226` | 2026-08-20 | BOND MATRIX_V2 legs ruled | BOND (BOND's own matrix) | NO | | DOCKET.tsv:226 |
| `DOCKET.tsv:72` | 2026-08-22 | DAEDALUS wiring sweep +1 folded item | DAEDALUS | NO | | DOCKET.tsv:72 |
| `DOCKET.tsv:228` / `:233`; `proposals/2026-08-27_increment2-window-RULED.md` | 2026-08-27 | Kernel C7 approved-in-principle; pilot windows | PROME/RED/DAEDALUS Kernel chain | NO | | those lines |
| `proposals/2026-08-27_creed-band-asks-RULED.md` | 2026-08-27 | CREED's three band asks approved | CREED | NO | BATCH | that file:3 |
| `proposals/2026-08-27_lagged-series-grade-date-RULED.md` | 2026-08-27 | Lagged-series grade-date class ruling (option i) | MIDAS packet | NO | | that file:3 |
| `DOCKET.tsv:335` | 2026-09-14 | Bounded WQ-ledger coverage repair approved | PROME | NO | | DOCKET.tsv:335 |
| `DOCKET.tsv:393` | 2026-09-15 | Deck owed/reference split approved | PROME/CODEX | NO | | DOCKET.tsv:393 |
| `proposals/2026-09-17_skipped-control-reporting-RULED.md:9` | 2026-09-17 | A skipped control is reported as skipped | Will's own instruction | NO | | that file:9 |
| `DOCKET.tsv:427` | (date not in excerpt) | BZ=F roll pattern | BRENT | NO | | DOCKET.tsv:427 |
| `DOCKET.tsv:598` | 2026-10-03 | X OAuth approved in Will's own browser | WALTER | NO | | DOCKET.tsv:598 |
| `archive/WILL_QUEUE_ROWS_2026-08-28_slimdown.md:52` | 2026-08-21 | WALTER FORMAT_SPEC ×2 ruled off recs | WALTER | NO | BATCH | that line |
| `…slimdown.md:53` | 2026-08-21 | WAL parked ×2 ruled | WAL | NO | BATCH | that line |
| `…slimdown.md:54` | 2026-08-20/21 | 004 60-DTE roll: let it run, no roll, no add | Will in BOND's window; BOND 60-DTE review | NO | TRADE | that line |
| `…slimdown.md:55` | 2026-08-21 | TRY-FIRE-001 card retired, premise preserved | TERRY rec + REGINALD NULL-mechanism answer (card's listed thesis owner "REGINALD + NEXUS", `AGENTS/TERRY/setups/INDEX.md:27`) | NO | | that line; `PROME/proposals/2026-08-21_retro-sweep-and-tryfire001-RULED.md:11–16` |
| `…slimdown.md:56` | 2026-08-21 | No fleet resolver-anchor retroactive sweep | DAEDALUS scope note | NO | | that line |
| `…slimdown.md:58` | 2026-08-21 | GATE-VIO-RV1 rising-vol watch registered | VIOLET | NO | | that line |
| `…slimdown.md:43–46` | 2026-08-23 | Rule-6b mirror; HANS nomination review; LABOR spawn; CREED brief | PROME / DAEDALUS / LABOR / CREED | NO | LAUNCH (LABOR) | those lines |
| `archive/WILL_QUEUE_ROWS_2026-09-05_rolloff.md:34` / `:35` | 2026-08-28 | Codex H2 MIDAS-06 scoring fence; H3 coordination scorecard | Codex audit / PROME | NO | | those lines |

**Table C counts (33 rows; several rows bundle more than one same-day decision, e.g. `DOCKET.tsv:172–176`, `slimdown.md:43–46`):** YES **0** · CANDIDATE **1** (the SEAT registration itself) · NO **32** · UNREADABLE **0**. Dropped from the scan as out of window: `DOCKET.tsv:142` (8/07), `:161–163` (7/31), `:165` (8/05). Dropped as already WQ-keyed: `:191` (WQ-44), `:245` (WQ-136), `:337` (WQ-233), `:364` (WQ-239), `:395` (WQ-253) and the RULED proposals for WQ-71/75/80/90/91/93/101/373. Dropped as not a Will ruling: `:406` ("NOT Will-ruled"), `proposals/2026-09-04_L262-orch-log-rotation-RULED.md` (a PROME ruling).

## Counts

| table | keys/rows | YES | CANDIDATE | NO | UNREADABLE |
|---|---|---|---|---|---|
| A — the 109 stable keys | 109 | **1** | **3** | **105** | **0** |
| B — WQ-keyed, outside the 109 file | 228 | 0 | 6 | 222 | 0 |
| C — no WQ number (pattern set) | 33 | 0 | 1 | 32 | 0 |
| **all** | **370** | **1** | **10** | **359** | **0** |

**Sensitivity (arithmetic only, not a verdict):** the one YES is **WQ-341**. CANDIDATE-S rows = 8 (A: WQ-224 · WQ-261 · WQ-342; B: WQ-105 · 163·⑥ · 163·⑤ · WQ-343; C: the SEAT registration). CANDIDATE-N rows = 2 (163·3, 163·4). ⇒ strict letter = **1**; +163·4 only (the convergence-content row) = **2**; + every S row = **≥3**. The verdict band therefore turns entirely on whether decisions about NEXUS's own instruments count — that is Will's call, not this list's.

## What NEXUS will contest (≤10 lines)

1. **WQ-341 (the only YES):** Will HELD — he declined to assign Root B on one print and deferred to PRED-50; NEXUS may say a decision not to act shows the product moved nothing, and that Root B rests partly on LIQUID's from-memory attribution (the page's own caveat 2, `…one-root-or-many.md:86`) and was an overclaim CATO corrected (PN2).
2. **S rows (WQ-224 · 261 · 342 · 105 · 163·⑥ · 163·⑤ · 343 · the SEAT registration):** each rules on NEXUS's own split gate, brief schema or cadence. By the post's own table, a desk's self-spec decision counts as that desk's surface; NEXUS will say layer maintenance is not the layer paying.
3. **163·4 and 163·3 (N):** self-audit slate items. 163·4 carries Disc-H convergence content (four desks on one HY<260 s3 line), the "route-counting" the post says resists automation; NEXUS's post files that work as discipline, not synthesis.
4. **Weight of Will's word:** WQ-342 was DELEGATED (blanket word, PROME's rec); WQ-261 and the WQ-163 items were BATCH "with your recs" — the proximate input may be PROME's rec rather than the NEXUS artifact.
5. **Window:** the 109-file starts 9/11; any grade must use the union of A + B + C. A reader for the layer would also raise WQ-340 (Will launched NEXUS; NO here because the NEXUS page was the output, not the input).

## Rows whose text could NOT be found

**None.** All 109 Table A keys were found once each in `PROME/WILL_QUEUE.md` § RECENTLY DONE or a `PROME/archive/WILL_QUEUE_ROWS_*.md` roll-off (VERIFIED: 0 missing in the index). Table B rows 32a/32b/33a/35b/36a/36b had no numbered index hit (lettered keys) but were read in `PROME/archive/WILL_QUEUE_ROWS_2026-08-16_rotation.md:32–36` and `…_2026-08-21_rolloff.md:17–21`. No row was classified without its text.
