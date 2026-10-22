# HAWK — Mode-A comprehension read, cluster A (ARCHITECTURE & STATE)

**Reader:** read-only Mode-A comprehension reader for DAEDALUS · **Written:** 2026-10-22 17:45 EDT (from `date`) · **Repo HEAD at read:** `0d0a91709` (2026-10-22 15:20 ET) · **Scope:** HAWK root files, design/, proposals/, memory/, templates/, archive/ + registry/ listings, inbox/outbox lifecycle, git history, _NETWORK edges, ROSTER row, FLEET_MAP row. Thesis/domain content and ledgers/scripts/guards belong to the other two readers; this file points at them only.
**Checks run (all read-only; `git status -- AGENTS/HAWK` clean before and after):** `scripts/read_cap_check.py --agent HAWK` rc 0 · `scripts/corrections_boot_check.py HAWK` rc 0 · `AGENTS/HAWK/scripts/derived_freshness.py` (no flags) **rc 1**.

---

## 1. Identity and current architecture

**What the desk is now.** HAWK is a cross-war **synthesis** desk plus a **dormant geopolitical book**. The 2026-07-12 split moved both acute wars to sibling desks: OSPREY (Russia/Ukraine) and FALCON (Iran/Gulf). HAWK "remains a live agent, narrower in scope, not retired" (CLAUDE.md:6). It has three jobs (CLAUDE.md:14):
- (a) reconcile the siblings' reads into one picture with no double-counting;
- (b) own the shared oil-decoupling thesis (canonical home `workbook/FLOW.tsv` FLOW-HAWK-19) and the global war-risk/shipping/shadow-fleet-enforcement synthesis;
- (c) keep the dormant vectors on a re-sweep cadence. **The book is 11 VX rows** (counted at `workbook/VX.tsv`): VEN, TWN, TWNMIL, IRAQ, TRADE-01, TRADE-02, SULPHUR, FININFRA, CEASEFIRE (SUPERSEDED, excluded), CODIF, EURMIL.

**Layers as the charter describes them.**

| Layer | Charter text | Where |
|---|---|---|
| Inputs | Boot-read both siblings' `NEXUS_BRIEF.md`; reconcile, never re-narrate. Reconcile **by belligerent dyad**, not by agent-theater (KB-HAWK-238) | CLAUDE.md:28-29, :45 |
| Thin derived surfaces | STATUS is "mostly pointers + reconciliation deltas". Two derived aggregates are regenerated, never maintained: `CROSS_WAR_SUMMARY.md` (step 13) and `CROSS_THEATER_WAR_RISK.md` (13a, standing lane, Will 7/25, 10-day/leg bar) | CLAUDE.md:30, :71-73 |
| Canonical record | KB.tsv (rows ≤223 frozen pre-split; 224+ synthesis only), VX.tsv, FLOW.tsv, `thesis/PREDICTIONS.tsv` (HAW-18+; scoped-read only), `thesis/FALSIFICATION.md` (derived; closeout 13b) | CLAUDE.md:69, :74, :128-139 |
| Outward | `NEXUS_BRIEF.md` is mandatory every session (step 15). Routine send table goes to BRENT/LIQUID/ALL; acute theater 🔴 goes sibling → BRENT direct with HAWK cc'd | CLAUDE.md:76, :199-209 |

**Owned paths.** `AGENTS/HAWK/` (CLAUDE.md:110). Plus root carve-out ① for packets it authors (CLAUDE.md:112).

**Consumers, per `AGENTS/_NETWORK.md`:**
- Outbound: HAWK→BRENT (reconciled geopolitical oil-risk read, :101), HAWK→VULCAN (Taiwan chip chokepoint, :130), HAWK→MIDAS (PGM supply SA/Russia, :145), HAWK→NEXUS (:173).
- Inbound: OSPREY→HAWK and FALCON→HAWK (:97-98), YURI→HAWK (decision + its NULL reaction, :104), BARON→HAWK (policy vector, :116), WALTER→HAWK (:163).
- Chain row :206 is `{OSPREY, FALCON} → HAWK → BRENT → HENRY/LIQUID/CARL`.
- The charter adds routine reads to HENRY/LIQUID/SAM/CARL/REGINALD (CLAUDE.md:187).
- NEXUS also reads STATUS.md and NEXUS_BRIEF.md whole (read_cap_check: "ALSO read whole by NEXUS:6").

**Classification.**
- ROSTER: `PROME/ROSTER.md:71`, cadence column "35". Note ‡ at :81: DOMAIN ACTIVE, not organizing. Cadence row :233 is `WEEKLY` (HAWK 9/25 packet; 12 WATCH_FOR phrases).
- FLEET_MAP: `AGENTS/DAEDALUS/FLEET_MAP.tsv:11`, Market · **L4 · H** · last scored 2026-10-21.

**Runtime and boot model.**
- **Boot (CLAUDE.md:40-62):** step 0 `git pull`; then STATUS (1), SCRATCH (2), LESSONS (3), both sibling briefs (4), VOCABULARIES + SCHEMA before a KB write (5), and two scoped PREDICTIONS slices (6).
- **Checks:** ledger_staleness (6a), corrections_boot_check (6a-2, WQ-399 receipt form), `derived_freshness.py` (6a-3), the 45-day dormant cadence (6b), and three intake lanes (7a inbox / 7b BOARD info-lane ID-diff / 7c WALTER lane).
- **Closeout (10-16):** symmetric write-back of STATUS, ledgers, the synthesis-consistency check, both aggregates, fingerprint record, FALSIFICATION, SCRATCH and NEXUS_BRIEF, then commit plus `scripts/safe-push.sh`.

**Explicit-read boot per PROME/COMPLETION_SPEC.md:** ❌ **ABSENT from the charter.**
- No step reads root CLAUDE.md, AGENTS.md or USER.md.
- No step records runtime, model, session or tool selection (WQ-385; COMPLETION_SPEC.md:10-17).
- Practice partly compensates: the 10/21 session recorded "Claude Code, model Opus 5.5, session hawk-1021" (STATUS.md:2; SCRATCH.md:3).

**Root closeout steps 1b–1e:** ❌ **not named in the charter.** Step 16 says only "commit … + auto-push" (CLAUDE.md:77). What practice did:
- The 10/21 closeout commit `46f1b766d` reports read_cap rc 0, claim_check clean, ledger_staleness rc 0 and "orphan_check none mine".
- **No 1c consumer_check receipt**, although that session superseded figures that other desks cite: the "0% autos" Canada mechanism and the N6 values.
- No 1d memory check is reported. The commit says "No new auto-memory", so 1d may not have applied.

---

## 2. File anatomy

Sizes are from `wc -c` on 2026-10-22. "Last commit" is `git log -1`. Boot-read follows CLAUDE.md:40-62.

| Path | Role | Bytes / lines | Last commit | Boot-read? | State |
|---|---|---|---|---|---|
| `CLAUDE.md` | Charter | 28,967 / 225 | `62240556c` 10-10 | harness-injected (not in read_cap perimeter) | LIVE |
| `STATUS.md` | Synthesis dashboard + dormant book | 15,819 / 105 | `46f1b766d` 10-21 | YES (1); NEXUS also | LIVE |
| `SCRATCH.md` | Session handoff | 6,471 / 69 | `a6c11f443` 10-21 | YES (2) | LIVE |
| `LESSONS.md` | Mistake patterns | 23,180 / 56 | `7943b8bdb` 10-21 | YES (3) | LIVE (rotated 10/21) |
| `NEXUS_BRIEF.md` | Outward synthesis brief | 7,961 / 71 | `46f1b766d` 10-21 | write-back (15); NEXUS reads | LIVE |
| `MEMORY.md` | Durable learnings | 7,321 / 38 | `d5ada4a6d` 09-18 | **NO** in charter (its own header says "Read at boot") | LIVE |
| `FILES.md` | Lifecycle inventory (moved out of charter 9/08) | 19,865 / 93 | `7943b8bdb` 10-21 | on demand | LIVE |
| `STATUS_COLD.md` | Hot/cold split half, 8/22 blocks verbatim | 28,188 / 103 | `ee662e24f` 09-02 | NO | HISTORY |
| `LAST_COMPLETION.md` | 9/21 PROME-spawn completion record | 8,961 / 76 | `ca9db9d44` 09-22 | NO | HISTORY (banner 9/22; **not in FILES.md**) |
| `SOURCES.md` | Source endpoints (dormant regions) | 7,355 / 126 | `40ade4327` 08-20 | NO ("NOT boot-read") | LIVE-reference |
| `board_log.tsv` | Signal disposition log | 174,493 / 493 | `46f1b766d` 10-21 | grep-only (never whole) | LIVE |
| `CALENDAR.md` | Pre-split calendar | 6,528 | `694f9a4c6` 08-10 | NO | FROZEN 07-09 |
| `TRADE.md` | Legacy trade sheet | 8,274 | `38edde37c` 07-01 | NO | FROZEN 07-01 |
| `OUTBOX.md` | Dead HERMES stub | 539 | `3caf51ffb` 07-09 | NO | FROZEN 07-09 |
| `OPEN_THREADS_2026-07-09.md` | Pre-split threads | 3,998 | `699c766a5` 07-12 | NO | SUPERSEDED 07-12 |
| `REMARK_20260628.md` | Iran re-mark artifact | 7,134 | `ac9086c79` 07-08 | NO | SUPERSEDED 07-08 |
| `DECK_EVIDENCE.md` | Mar-13 deck evidence | 17,303 | `e1efb801d` 09-28 | NO | FROZEN (banner 9/28) |
| `design/2026-07-12_war-agent-split-spec.md` | Split spec (HAWK-authored) | 12,401 | `6b2a4bb8d` 07-12 | NO | HISTORY / authority for the split |
| `design/HAW19_MEASUREMENT_DRAFT.md` | Successor measurement v2 | 9,927 | `62240556c` 10-10 | NO | LAPSED (WQ-362 banner) |
| `design/VESSEL_COUNTING_DICTIONARY_DRAFT.md` | Shared hull-count vocabulary | 8,428 | `e50b97f2c` 09-08 | NO | DRAFT; owner confirmations pending since 9/08 |
| `design/VX_GUARDS_AND_CODIFICATION.md` | Guard/Watch_Source + CODIF contract | 2,358 | `54accb874` 09-08 | NO (governs boot 6b) | LIVE |
| `proposals/2026-08-10_self-audit-improvement-slate.md` | Ranked slate | 13,421 | `703b7c11b` 08-10 | NO | PROPOSALS ONLY |
| `proposals/2026-09-08_HAW-19_repair.md` | HAW-19 proposal | 7,167 | `6fd24c71e` 09-10 | NO | RULED 9/10 (WQ-212 banner) |
| `proposals/2026-09-08_batch2_rule-decisions.md` | N6/TRADE01/HAW18/HAW19 packet | 10,417 | `6fd24c71e` 09-10 | NO | RULED 9/10 (banner) |
| `memory/2026-02-18.md` | First-init note | 2,228 | `edf49b9a2` 03-04 | NO | HISTORY |
| `templates/SCRATCH.template.md` | SCRATCH template | 2,121 | `a0763c0cd` 09-08 | used at 14 | LIVE |
| `registry/corrections_receipts.tsv` | R1 receipts (16 on file) | 3,830 | `46f1b766d` 10-21 | via 6a-2 | LIVE |
| `registry/derived_inputs.json` | Derived-input fingerprint receipt | 1,767 | `46f1b766d` 10-21 | via 6a-3 | LIVE |
| `archive/*` (8 files) | Verbatim STATUS/SCRATCH/NEXUS/LESSONS snapshots 9/10–10/21 | 3.8–29.7 KB | latest `7943b8bdb` 10-21 | NO | HISTORY |
| `audits/*` (27 files) | 5/22 phase audits; 9/08–9/10 evidence | — | latest `3b0d54de0` 09-10 | NO | HISTORY (class rule) |

Pointers only, owned by the other readers: `workbook/` (KB, VX, FLOW, SCHEMA, CATALYSTS [39 lines], plus FROZEN EXIT_PROTOCOL/POLITICAL_SUSTAINABILITY/BOOT_LOG/PRICE_BREACHES/FOUR_STRUCTURAL_BREAKS/STATUS_archive×2), `thesis/` (`FALSIFICATION.md` 39,725 B refreshed 10/21, PREDICTIONS ~69 KB), `domain/` (energy-strikes, war-risk, europe-rearm, sources), `research/`, `scripts/` (`derived_freshness.py` is the only live script; legacy suite FROZEN). There is no `workbook/LEDGER_GLOB` file, so root step 1c-bis has no declared ledger set.

---

## 3. How HAWK states the standards locally, in its own words

| Standard | HAWK's own expression | path:line |
|---|---|---|
| Current judgment | "**The decoupling holds on flow, and the escalation drivers are stacking.** … Brent at ~$110 is mostly **risk premium, not lost barrels** (FLOW-HAWK-19 …)." "Never pool a lost-barrel figure across the two." Conversion risk = "one counting-source hit on a Saudi crude-processing unit, or a US strike on Kharg." | STATUS.md:45-49 |
| BOTTOM LINE (rule) | "Every STATUS.md update must end with a `## BOTTOM LINE` section: 2-4 sentences. What's the current combined geopolitical read? What's the single most important thing to watch? What changed since last update?" | CLAUDE.md:213-215 |
| BOTTOM LINE (instance) | Four bullets: "Oil is pricing fear more than loss" · "What changed is US posture" · "Watch: a counting-source hit … any US move on Kharg, and the days after the 11/3 midterms" · Russia refineries/terminals | STATUS.md:99-105 |
| Exit/kill rules | **No exit rail.** `workbook/EXIT_PROTOCOL.md` is FROZEN 8/10: "Do not cite, and do not execute" (EXIT_PROTOCOL.md:3). Its contents were split three ways: falsification → PREDICTIONS; price → BRENT; theater exits → FALCON/OSPREY (FILES.md:44). The live falsification surface is `thesis/FALSIFICATION.md` ("refresh … without changing registered letters", FILES.md:62; CLAUDE.md:74) | as cited |
| No-double-count (HAWK's convergence analogue; no composite by design) | "identify dyad/direction, asset, molecule, flow layer, event date and prior outage. Hull loss is not lost productive capacity. A sanctions listing or boarding is not a seized quantified cargo. A refinery-strike loss and an undelivered licensed-import tranche are one barrel." | STATUS.md:61 |
| Convergence matrix | **None.** FILES.md:48 records that the "convergence matrix" pointer was repaired because the matrix no longer exists. The equivalent is the leg table at STATUS.md:51-59 plus the dyad rule at CLAUDE.md:29 | as cited |
| Routing | "acute 🔴 theater-specific signals … are **OSPREY's and FALCON's own right to send direct to BRENT (HAWK cc'd)** — they do not route through HAWK first." "Steady-state cross-agent synthesis flows through `NEXUS_BRIEF.md` — outbox is reserved for 🔴 acute signals." | CLAUDE.md:209, :81 |
| Trade stance | "HAWK holds no trade book (unchanged from pre-split)." "Do NOT track oil prices … reference BRENT's values." SCRATCH: "No trade book." | CLAUDE.md:18, :8; SCRATCH.md:6 |
| Synthesis discipline | "**If you find yourself writing "Iran did X, then Y" or "Ukraine struck Z" in STATUS.md, stop**" | CLAUDE.md:16 |
| Dormant cadence | "Any row past cadence is a **re-sweep-due trigger against external primaries, not a carry-forward**" (45 days) | CLAUDE.md:54 |
| Read budget | "each whole boot-read surface must fit the root 32,550-byte budget … the STATUS 120-line target does not replace the byte check." | CLAUDE.md:225 |
| Self-binding caveat (anti-laundering form) | HAW-22: "*Undisclosed damage can produce a misleading CONFIRM — a CONFIRM on this letter is a claim about what was DISCLOSED, never about capacity.*" (same text in NEXUS_BRIEF CALIBRATION) | STATUS.md:67 |

---

## 4. Deviations and do-not-touch constraints for a future editor

1. **Provenance IDs are never renamed.**
   - VX-HAWK-*, FLOW-HAWK-*, KB-HAWK-* and HAW-NN keep their names at OSPREY/FALCON (FILES.md:15).
   - KB rows ≤223 are frozen, including the duplicate IDs 131/132 (CLAUDE.md:151).
   - HAW-01..17 are frozen; HAW-16→FAL-01 and HAW-17→OSP-01 are marked REHOMED (FILES.md:17).
2. **`thesis/PREDICTIONS.tsv` is never read whole** (~69 KB, 128% of the cap). Boot reads exactly two scoped slices (CLAUDE.md:48-51). The `read_cap_check` excludes it through the SCOPED marker. Don't "fix" this by trimming rows: they are the calibration record.
3. **The two derived aggregates are regenerate-only.**
   - Legs cite FALCON and OSPREY. HAWK owns only the cross-leg comparison (CLAUDE.md:71-72).
   - Fingerprints are recorded only after reconciliation: "Never record merely to silence drift" (CLAUDE.md:73).
4. **The legacy `scripts/` suite stays FROZEN and unwired.** `derived_freshness.py` is "the sole live local checker". The five monitors exit rc 0 while printing stale constants (CLAUDE.md:223; FILES.md:41). There was a 10/10 one-line edit to `scripts/thresholds.py` (FILES.md:89). The suite is still declared frozen.
5. **Frozen-with-successor chains are never refreshed:** TRADE, CALENDAR, OUTBOX, PRICE_BREACHES, EXIT_PROTOCOL, STRIKES/SUMMARY, and the thesis trio. Editing them re-forks a resolved split.
6. **The dormant book is a deliberate low-cadence holding.** Its marks are carried between 45-day sweeps by design; a quiet book is not rot. **EURMIL bands score the escalation ladder, NOT spending** (FILES.md:14; `domain/europe-rearm/README.md`). INCURSIONS `Provenance` cells are OSPREY's and "must not be upgraded from a HAWK session" (FILES.md:24).
7. **The FILES.md maintenance rule:** add a FILES row (or a class rule) in the same commit as any new file (FILES.md:54). A VX count change edits CLAUDE.md:54 in the same commit as the row.
8. **Hot/cold STATUS split.** STATUS_COLD.md is verbatim 8/22 history; "never cite as current" (FILES.md:8).
9. **The C3 limb-2 qualifier is ruled.** WQ-470 RULED A (Will 10/21 21:30 ET): NOT SATISFIED stands, and the qualifier is drafted only after 10/27, jointly with OSPREY. Do not re-open it (STATUS.md:72).
10. **Prices in STATUS are tagged [BRENT owns].** HAWK doesn't own prices, and root rule #4 forbids citing them from STATUS.

---

## 5. Findings

| # | Sev | Finding | Evidence | V/I |
|---|---|---|---|---|
| 1 | 🔴 | **The FLEET_MAP row's currency claim is false as of its own last-scored date.** The row (scored 10/21) says "Last owner session 10/10 was a bounded L0 drain; October STEO/N6 observation remains owed". But HAWK ran a substantive multi-pass owner session on 10/21 (6 HAWK commits, `4a82c1168`→`a6c11f443`, 20:35–21:39 ET) that **performed the N6 October STEO observation** (EXTENSION, KB-HAWK-448). It also re-swept 5 dormant rows, graded OSPREY's C3 limb 2 and rotated LESSONS. The L5 bar ("performs the October N6 observation and closes registered due work") is now half met. HAW-20 (resolves 10/31) and the HAW-22 window (closes 10/31) remain open | FLEET_MAP.tsv:11; STATUS.md:2, :71; commit `7943b8bdb` body | V |
| 2 | 🟠 | **An unprocessed correction narrows a live HAWK outbound claim.** MARCO 10/21 22:46 ET: under CBP CSMS #69851916 and its HTS list, "passenger cars, light trucks and auto parts are still NOT on the Section 338 list, so 'autos now stack on 232' must not be read as cars paying 50%". HAWK's STATUS ("Canada auto duties now stack on 232", :22) and its NEXUS SENDING row to BRENT/CARL/MARCO ("Canada S338 auto duties now stack on 232") still carry the broader wording. The packet is not in board_log or KB | `inbox/2026-10-21_from-MARCO_s338-…unlisted.md`; STATUS.md:22, :87; NEXUS_BRIEF.md:14; grep board_log/KB = 0 | V |
| 3 | 🟠 | **Inbox backlog: 9 unprocessed, 0 dispositioned.** 2 top-level packets (MARCO 10/21, DEWEY 10/22) and 7 WALTER signals (SIG-W-20261021-021/-027/-030/-031, SIG-W-20261022-003/-007/-028). The oldest is 10/21: -021 arrived after closeout, and SCRATCH already flags it as owed. Mostly INFO-role, but -007 (IRGC claims 4 STS tankers + 3 mine hits, CLAIM-ONLY; Brent $112.27) and -028 (Houthi Yanbu fire claim, CLAIM-ONLY) bear directly on the "premium not barrels" read. Processed archives hold 130 + 305 files | `find inbox -maxdepth 1`; board_log grep = 0 for all 7 IDs; SCRATCH.md:59 | V |
| 4 | 🟠 | **`derived_freshness.py` reads rc 1 now:** FALCON's NEXUS_BRIEF changed after HAWK's 10/21 record. Both aggregates are flagged REVIEW. This is normal drift between sessions, but the aggregates are not certified current | live run 2026-10-22 ~17:44 ET | V |
| 5 | 🟠 | **The charter has no explicit-read or runtime-selection boot step** (COMPLETION_SPEC.md:10-17; WQ-385): no read of root CLAUDE.md, AGENTS.md or USER.md, and no runtime/tool record step. Most sessions are Will- or PROME-launched, so the read relies on harness injection. Practice recorded the runtime on 10/21 anyway | CLAUDE.md:40-62 (grep COMPLETION_SPEC/USER.md/runtime = 0 hits) | V |
| 6 | 🟠 | **Root closeout 1b–1e are not in the charter's closeout** (step 16 = commit + push only). Practice ran read_cap, claim_check, ledger_staleness and orphan_check (`46f1b766d` body). **No 1c consumer_check receipt**, although the 10/21 session superseded figures other desks cite (the Canada "0% autos" mechanism → stacking; N6 Sep DECAY → Oct EXTENSION) | CLAUDE.md:77; commit bodies `46f1b766d`, `7943b8bdb` | V (absence of a receipt) / I (that 1c was owed) |
| 7 | 🟠 | **The routing and scope sections lag the ruled topology.** CROSS-AGENT "You receive from" names only OSPREY and FALCON (CLAUDE.md:197). `_NETWORK.md` also has YURI→HAWK "decision + its NULL reaction" (:104; YURI boundary RULED 9/19, ROSTER:97), BARON→HAWK (:116) and WALTER→HAWK (:163). The send table omits HAWK→MIDAS (PGM, :145). DOMAIN SCOPE never mentions EURMIL or the `domain/europe-rearm/` tree (RU↔NATO dyad), and the domain line still says "defense spending" (CLAUDE.md:3, :183). EURMIL bands deliberately exclude spending (FILES.md:14) | as cited; grep YURI/EURMIL/BARON/MIDAS in CLAUDE.md = 0 | V |
| 8 | 🟠 | **SCRATCH and NEXUS_BRIEF were only partially re-cut after passes 3 and 4 on 10/21.** They contradict STATUS and the closeout commit. SCRATCH marks line "TRADE-02 O (**re-sweep overdue, 60 days**)" vs STATUS "re-swept 10/21". SCRATCH "⚠️ SKIPPED: 13b (FALSIFICATION refresh)" vs commit `46f1b766d` "FALSIFICATION.md re-stamped 10/21". NEXUS Coverage "**Not done:** full dormant re-sweeps, FALSIFICATION refresh". NEXUS WATCH "10/27 OSPREY C3 earliest kill — Needs an in-window limb-2 canvass", although it was graded NOT SATISFIED the same night. NEXUS is consumed whole by NEXUS | SCRATCH.md:7, :39-41; NEXUS_BRIEF.md:69, :61; STATUS.md:22-24, :72 | V |
| 9 | 🟡 | **The NEXUS_BRIEF `STATUS commit:` field is a pointer, not a hash** ("see `git log -1 -- …`"). Charter step 15 requires the hash | NEXUS_BRIEF.md:5; CLAUDE.md:76 | V |
| 10 | 🟡 | **Charter size 28,967 B = 89.0% of the 32,550 B budget**, 53% of the 54,250 B cap. read_cap_check: "OUT OF PERIMETER by rule 20 unless declared; injection UNCONFIRMED"; HAWK has no READS.tsv declaration ("clean within what the scan found, NOT a clean bill") | read_cap_check output | V |
| 11 | 🟡 | **LESSONS rotation stopped at 71%, inside the 70–75% band.** The checker says that if it was just rotated, "owes 396 B more (rule 5 stops at <70%)". STATUS reports "86% → 71%" as DONE. Headroom to the 75% trigger is 1,232 B | read_cap_check; STATUS.md:2 drain receipt, :97 | V |
| 12 | 🟡 | **VX count drifts inside the charter:** :54 says **11** (with a note that "in the same commit as the row" is what stops drift), while :69 closeout 11 still says "`workbook/VX.tsv` (10 rows, including the superseded historical anchor)". The actual count is 11 | CLAUDE.md:54 vs :69; VX.tsv | V |
| 13 | 🟡 | **The messaging paragraph is stale and stricter than root.** It cites `[[project_messaging_overhaul]]` "being overhauled". Messaging v1 is ratified, but HAWK is on no coded route. It also requires direct-drop "**with Will's explicit authorization**", while root carve-out ① lets an author commit its own inbox packets. HAWK's 10/21 practice delivered direct packets to OSPREY (`a896ab9d8`) and MARCO (`020920ef9`) via carve-out ①, with no Will authorization recorded | CLAUDE.md:81, :102; SCRATCH.md:59 | V (text) / I (whether authorization was needed) |
| 14 | 🟡 | **Outbox lifecycle residue:** 21 top-level `outbox/` files dated 8/20–9/08 (including 7 Codex-session JSON/TXT receipts) were never moved to `delivered/` (10 files, newest 7/28). ≥6 have same-slug copies elsewhere in the repo (likely delivered). `2026-08-20_to-PROME_checkpoint-conditions-BUILT…` has **0** slug matches outside HAWK, so delivery is unverified. No outbox use since 9/08: delivery moved to direct carve-out ① packets | `find outbox`; `git ls-files` slug grep | V (counts) / I (delivery) |
| 15 | 🟡 | **FILES.md coverage holes, against its own "every file … named or class-covered" rule:** `LAST_COMPLETION.md` (root, 9/21 vintage) and `archive/STATUS_section_2026-09-10-session.md` are neither named nor covered by a class rule. `archive/` has no class rule; its files are named one by one in dated supplements | FILES.md:46-54, :81-93; grep = 0 | V |
| 16 | 🟡 | **MEMORY.md says "Read at boot for learnings" but the charter boot list omits it.** Last commit 9/18 | MEMORY.md:3; CLAUDE.md:41-61 | V |
| 17 | 🟡 | **The STATUS byte-check tool differs between surfaces:** FILES.md says "measure with `PROME/tools/measure.py`", while the charter says `scripts/read_cap_check.py` | FILES.md:7; CLAUDE.md:68, :118 | V |
| 18 | 🟡 | **Closeout 13b whole-reads `thesis/FALSIFICATION.md`, which is 39,725 B = 122% of the 32,550 B budget** (under the 54,250 B cap, so not truncated). The root budget binds boot whole-reads; this is a closeout read and outside the checker's perimeter | CLAUDE.md:74; `wc -c` | V (size) / I (rule applicability) |
| 19 | 🟡 | **Synthesis-discipline drift:** STATUS §"What changed while dark" (:13-41) is ~29 lines of theater event narration (hull names and positions, Saudi target list, Russia strike dates), bracket-attributed to owners. CLAUDE.md:16 says to "stop" writing "Iran did X". It is defensible as a dark-window catch-up, but it is the drift the charter predicts | STATUS.md:13-41 | I |
| 20 | 🟡 | **Glued tokens violate the root Output Canon** ("never glue words"): "The45-day", "step11", "boot6a-3", "closeout13a-2", "July28"; also FILES.md "September8", "HAW19" | CLAUDE.md:29, :53, :54; FILES.md:65-89 | V |
| 21 | 🟡 | **Dark-window pattern persists.** Owner sessions: 9/2, 9/8, 9/10, 9/17, 9/18, 9/21, 9/22, 9/28, 10/10, 10/21. Gaps: 9/28→10/10 (12 days) and 10/10→10/21 (11 days), both followed by drain-catch-up sessions, all PROME- or Will-launched. NEXUS_BRIEF: "the desk went dark 11 days during the worst Gulf week" | git log; NEXUS_BRIEF.md:56 | V |
| 22 | 🟢 info | **Dead references are clean.** No YEYOU, Helm/HELM or `AGENTS/PROME/` string in live HAWK surfaces (grep excluding processed/archive/audits/domain/sources/research). Corrections check rc 0 (16 receipts on file; COR-20260925-13 is a broadcast expired at cap, not an obligation) | grep; corrections_boot_check output | V |
| 23 | 🟢 info | **Will's 10/20 USER.md rulings** (no expiry nagging; trade ideas loosened, NOT-FIRED labelling via TERRY) **do not bind HAWK directly**, because it holds no book. No expiry or sell-or-roll reminder appears in STATUS/SCRATCH/NEXUS. Not reflected because not applicable; the charter has no USER.md read (see #5) | USER.md:45-47; CLAUDE.md:18 | V (absence) |

---

## 6. Reconciliation against the old profile (`AGENTS/DAEDALUS/profiles/HAWK.md`, body vintage 8/7)

| Old section | Verdict | How |
|---|---|---|
| Identity in one line | **CHANGED** | Dormant book is **11 rows**, not 9 (CODIF 8/10, EURMIL 9/18). FLOW-19 is still the canonical thesis home. The dyad finding (KB-238) **is now propagated into the charter** (CLAUDE.md:29). The declared falsification rail now exists: `thesis/FALSIFICATION.md`, refreshed 10/21. "No trade book" still true (CLAUDE.md:18) |
| Grade story (8/7) | **OBSOLETE** | The F4 EXIT_PROTOCOL-rewrite blocker is gone: the file was frozen 8/10, the freeze blessed by Will 8/15, and the rail superseded by FALSIFICATION.md. Sunset stood down. Current story: L4 H; L5 = N6 October observation (**done 10/21**) + close registered due work (HAW-20 10/31, HAW-22 window 10/31) |
| The F4 rewrite scope | **OBSOLETE** | No EXIT_PROTOCOL rewrite will happen (FROZEN; CLAUDE.md:223 "never execute"). The test content it listed (FLOW-19 kill, FLOW-20 fire, decomposition falsifier) now lives in FALSIFICATION.md. Ledger reader to confirm |
| §3 Invalidation-surface inventory | **CHANGED** (nearly every row) | EXIT_PROTOCOL: FROZEN. FALSIFICATION.md is the live derived rail (10/21). Both aggregates were regenerated 10/21 but `derived_freshness` rc 1 now. "Every war-risk leg >10 days old" again (STATUS.md:59). NEXUS_BRIEF stamped 10/21 but internally stale (finding #8). PREDICTIONS: HAW-20 and HAW-22 OPEN (counts → ledger reader). LESSONS newest 9/28; rotated 10/21 |
| PAT-089 items (dark since 7/28) | **OBSOLETE** | All dated 7/31–8/24. Current dated set: TRADE-01 cadence 10/25 · C3 qualifier draft after 10/27 · HAW-20 10/31 · HAW-22 window close 10/31 · YURI L432 grade 10/31 · EURMIL backstop 11/02 · 11/3 midterms · trade measures lapse 11/9–10 · IRAQ/SULPHUR/FININFRA cadence 11/12 |
| File anatomy | **CHANGED** | CLAUDE.md 225 lines / 28,967 B (was 239). STATUS **105 lines / 15,819 B** (was 179; byte gate now binding). FILES.md split out 9/08. STATUS_COLD 9/02. `derived_freshness.py` + `registry/` added 9/08. `domain/europe-rearm/` 9/18. Inbox 2 + 7 unprocessed (was 10 + 12). The March cohort is closed: POLITICAL_SUSTAINABILITY/BOOT_LOG frozen 8/10, DECK_EVIDENCE bannered 9/28. Outbox is no longer delivered/-only (21 top-level residue files) |
| Blueprint fit notes | **STILL TRUE** (+ one addition) | Still no composite, correctly: the leg table + no-double-count rule (STATUS.md:51-61). Add `domain/europe-rearm/` (LADDER/INCURSIONS) as a third HAWK-native structure with no blueprint row |
| DO-NOT-TOUCH | **CHANGED** | #1–5, #8 and #9 still true. **#6 OBSOLETE** ("EXIT_PROTOCOL must NOT be frozen": it was frozen, and that was blessed). **#7 OBSOLETE** (HAW-18 resolved; now applies to HAW-20/22 letters). Add §4 items 2, 3, 6, 9 above |
| ★ Correction propagated (boot.py) | **STILL TRUE** (historical) | boot.py stays FROZEN and unwired; FILES.md:41 carries the same disposition. The sanctions-tracker lane is still recorded as "unbuilt … Highest-value HAWK build candidate" (FILES.md:41); no build evidence found |
| Owner-lane flags | **MOSTLY CLOSED/OBSOLETE** | F4 obsolete. NEXUS re-pin → now refreshed every session, but the STATUS-commit field is a pointer (#9) and its body is stale (#8). 45-day clock → running (re-sweeps 10/21). War-risk legs → re-flagged >10 days. Unconsumed inbound → 9 (#3). CROSS_WAR_SUMMARY → current 10/21. STATUS cap → fixed. March banners → done. Dyad-cut propagation → **DONE** (CLAUDE.md:29). Sanctions-tracker build → **still open** |
| Open questions | **CHANGED** | Q1 answered (no ladder; FALSIFICATION.md). Q2 closed. Q3 obsolete (no F4 packet). Q4 answered at instruction level ("Reconcile by belligerent dyad, not merely by agent-theater", CLAUDE.md:29); whether STATUS *structure* follows it is partly answered (the leg table is keyed by molecule/asset, not by dyad) |

---

## 7. Coverage

**Read whole:**
- `AGENTS/HAWK/CLAUDE.md` L1–225 (three chunks: 1–80, 81–160, 161–225; EOF verified)
- `STATUS.md` L1–105 (EOF)
- `SCRATCH.md` whole (69 lines)
- `NEXUS_BRIEF.md` whole (71 lines)
- `MEMORY.md` whole (38 lines)
- `FILES.md` L1–93 (EOF)
- The 5 newest unprocessed packets: DEWEY 10/22, SIG-W-20261022-028, -007, -003, MARCO 10/21
- `profiles/HAWK.md` L1–60 (EOF)
- `USER.md` L40–50
- `PROME/COMPLETION_SPEC.md` L8–18

**Read partially:**
- `LESSONS.md`: first 6,000 B plus the heading index
- `LAST_COMPLETION.md` L1–30 of 76
- `STATUS_COLD.md` L1–8 of 103
- Headers only (6–8 lines each) of CALENDAR, TRADE, OUTBOX, OPEN_THREADS, REMARK, DECK_EVIDENCE, SOURCES, all 4 design/ files, all 3 proposals/, memory/2026-02-18.md and templates/SCRATCH.template.md
- `design/2026-07-12_war-agent-split-spec.md` L1–25
- Stamp lines only of FALSIFICATION.md, CROSS_WAR_SUMMARY.md, CROSS_THEATER_WAR_RISK.md and EXIT_PROTOCOL.md

**Greps:**
- `_NETWORK.md` and `ROSTER.md` lines naming HAWK
- `FLEET_MAP.tsv` HAWK row
- DOCKET open rows naming HAWK: skimmed, first 260 chars only
- board_log ID greps for the 7 WALTER signals and the MARCO slug

**Listings:** archive/, audits/, registry/, workbook/, inbox/ and outbox/ (with processed/delivered counts); VX.tsv IDs.

**Git:** `git log -25 -- AGENTS/HAWK`, the HAWK-authored commits, `git log -10 -- CLAUDE.md`, and the commit bodies of `46f1b766d` and `7943b8bdb`.

**Not read:**
- Unprocessed WALTER signals -021, -027, -030 and -031 (listed and board_log-checked only)
- Processed mail archives
- board_log rows
- KB, VX (beyond IDs), FLOW, CATALYSTS and PREDICTIONS contents
- thesis/, domain/, research/ and scripts/ bodies (other readers' clusters)
- The STATUS_COLD body
- The proposals/design bodies past their headers
- The LESSONS remainder past 6,000 B
