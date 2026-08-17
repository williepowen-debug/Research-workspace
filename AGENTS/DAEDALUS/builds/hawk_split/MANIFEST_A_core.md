# HAWK Split — Manifest A (Core state + everything not workbook/energy-strikes/thesis/LESSONS/scripts)

> 🗄 **DATED BUILD-EXECUTION RECORD (2026-07-12; bannered 2026-08-17, self-audit F5 — same class as the 8/11 upgrades/ pass, which was scoped to upgrades/ only).** One-shot record; not maintained.

**Reader:** A (core surfaces + full-tree inventory) · **Date:** 2026-07-12 · **Spec:** `AGENTS/HAWK/design/2026-07-12_war-agent-split-spec.md`
**Scope boundary:** Reader B owns `workbook/*.tsv` + `domain/energy-strikes/`; Reader C owns `thesis/`, `LESSONS.md`, `scripts/`. This manifest covers everything else.

---

## 1. STATUS.md section map (121 lines)

| Lines | Section | Summary | Disposition |
|---|---|---|---|
| 1-6 | Header/dashboard | Both-war headline (3rd US strike round, Hormuz closure, Brent decoupling) + "off-core Russia-Ukraine" mention | **MIXED** — split: Iran facts→FALCON header, Russia mention→OSPREY, decoupling-gap framing→HAWK-synthesis |
| 7-29 | ⚖️ Scenario Posture (B/C/D ladder, see-saw discipline) | Iran A/B/C/D scenario %s w/ full rationale, flip triggers | **FALCON** (this IS the Iran convergence-matrix/ladder the spec names as FALCON's framework, §2) |
| 32-47 | Convergence Matrix (10-vector Iran-core) | Hormuz/Iran-ops/US-kinetic/oil/Gulf-prod/diplomacy/shipping/cyber/macro-credit/Bab-al-Mandab | **FALCON** (explicitly "Iran-core" in its own title); "Global macro/credit" + "Shipping/insurance" rows are candidates HAWK's synthesis layer also draws on — FALCON keeps the row, HAWK references it |
| 49 | Off-core Russia-Ukraine paragraph (3 channels: refineries/products, crude-terminals, shadow-fleet tankers) | Dense Russia-theater content, HAW-15/17 pointers | **OSPREY** — this paragraph is effectively OSPREY's seed STATUS content |
| 53-71 | CONFIRMED vs CLAIMED vs UNVERIFIED table (7/9-7/12) | Iran-Gulf event log (strikes, Hormuz closure, mines, Mojtaba) — zero Russia rows | **FALCON** |
| 75-90 | Next-Rung Tells (pre-registered discriminators) | All Iran/Gulf gates (production-infra hit, vessel sunk, Oman channel, Baghdad/PMF) | **FALCON** |
| 93-104 | Cross-Agent Implications table | BRENT/HENRY/LIQUID/SAM/CARL/REGINALD rows = Iran-driven (**FALCON** owns, sends to BRENT et al per spec §3); VULCAN/MIDAS row = dormant-seam note (Taiwan/PGM, explicitly says "neither theater active") → **HAWK-dormant**; RED/NEXUS row = steelman on the D-regime call, spans both wars' evidence → **HAWK-synthesis** |
| 108-115 | Predictions (live) table | HAW-14 (FAILED, Iran), HAW-15 (FAILED, Russia), HAW-16 (OPEN, Iran, →Jul 26), HAW-17 (OPEN, Russia, →Aug 1) | **SPLIT** — HAW-14/16 rows → FALCON; HAW-15/17 rows → OSPREY (matches spec §8/§4 exactly — confirms spec's assumption is accurate) |
| 119-121 | Bottom Line | Synthesizes both theaters + the decoupling-gap thesis | **HAWK-synthesis** (this paragraph is close to a template for what HAWK's post-split Bottom Line should look like) |

**Sections that mix theaters:** header (1-6), Cross-Agent Implications (93-104, 3 different dispositions inside one table), predictions table (108-115, row-level split needed).

---

## 2. CLAUDE.md anatomy (276 lines)

**Boot sequence (numbered, exact commands):**
| Step | Action | Script/command | Inherit note |
|---|---|---|---|
| 0 | `git pull` | — | All three inherit verbatim |
| 1 | Read `STATUS.md` | — | All three (own STATUS) |
| 2 | Read `SCRATCH.md` | — | All three (own SCRATCH) |
| 3 | Read `LESSONS.md` | — | Reader C scope — flagged here only for completeness |
| 4 | Read `AGENTS/VOCABULARIES.tsv` + `workbook/SCHEMA.tsv` before KB write | — | All three (fleet-shared vocab file; own SCHEMA.tsv per Reader B) |
| 5 | Surface due/stale predictions, read calibration scoreboard preamble | scans `thesis/PREDICTIONS.tsv` | All three, each own prefix (Reader C detail) |
| 5a | Ledger staleness check | `python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" HAWK --quiet` | **Needs agent-name param swap** (`OSPREY`/`FALCON`) at build time — fleet-shared script, not HAWK-local |
| 5b | Baghdad/Green-Zone alert check | `python3 "$(git rev-parse --show-toplevel)/AGENTS/HAWK/scripts/baghdad_watch.py"` | **FALCON-only** (Iran/Iraq discriminator, per spec §4) — must be removed from OSPREY's and HAWK-synthesis's boot sequence, not just left dangling. Path also needs rewrite (`AGENTS/HAWK/scripts/` → `AGENTS/FALCON/scripts/`) |
| 6 | Signal intake: inbox/, BOARD scan, WALTER lane | — | All three, fresh inbox/outbox per new agent |
| 7 | `web_search` for latest developments | — | All three |
| 8 | EXECUTE | — | — |
| 9-15 | CLOSEOUT (STATUS write-back → workbook/predictions → falsification check → forward-state/energy-ledger → SCRATCH rewrite → NEXUS_BRIEF → promotion+git) | — | All three, structurally identical; step 12's "energy-strike ledger" line is Reader B/C territory |

**Identity/scope sections needing three-way split:**
- **DOMAIN SCOPE** (lines 193-214): "You own" list interleaves Hormuz/Suez/Malacca (Suez/Malacca → HAWK-dormant, Hormuz → FALCON), Russia/Iran/Venezuela sanctions (three different owners), "war risk insurance/shadow fleet" (HAWK-synthesis per spec §3's global war-risk row), Gulf production (FALCON), defense spending (HAWK-dormant). **This section cannot be copy-pasted to any one sibling — needs hand-disaggregation, not a clean file-level move.** Flag to DAEDALUS build step as the highest-complexity single section in the whole migration.
- **CROSS-AGENT SIGNALS** (217-235): "You send" table rows are theater-specific (Hormuz-blocked→FALCON, Gulf storage→FALCON) but "Hezbollah mass activation"/"De-escalation ALL" rows are more HAWK-synthesis-flavored (broadcast to all agents). Same disaggregation problem, smaller scale.
- **SCENARIO FRAMEWORK (War)** section (238-247): literally the A/B/C/D ladder table — **FALCON** inherits wholesale (matches STATUS §Scenario Posture).
- **CONVERGENCE MATRIX** rules section (156-168): generic instructions (not the data) — **FALCON** inherits as its convergence-matrix rubric; HAWK-synthesis needs its own thinner version per spec §6.
- **EXIT RULES (Falsification)** (172-189): 4 categories, mostly Iran-coded (Iran ceasefire, Hormuz reopens, VIX<20) but "BTFP 2.0" and time-based rules are generic — **mostly FALCON**, OSPREY needs an analogous but Russia-coded version (currently doesn't exist as a separate list — a build gap, not a migration gap).
- **⚠️ OIL HANDOFF banner** (line 6): "oil fundamentals owned by BRENT... you own military ops... Feed BRENT military inputs" — **all three inherit this framing** (each theater still feeds BRENT its own inputs per spec §3's transmission table).
- **KB.tsv 13-column schema + Admiralty-code + cold-boot-orientation rules** (109-152): Reader B/C territory but is defined IN CLAUDE.md, not workbook/SCHEMA.tsv — **all three inherit verbatim** (schema is theater-agnostic).

**Stale/dangling found:**
- Line 48's `CEASEFIRE_FADE_PROTOCOL.md` reference is already marked retired/resolved inline (2026-07-08 fix) — not a live problem, just documented history. No action needed.
- Boot step 5b's baghdad_watch path is HAWK-hardcoded (`AGENTS/HAWK/scripts/baghdad_watch.py`) — will silently 404/misfire for OSPREY/HAWK-synthesis if the CLAUDE.md text is copied without editing. **Concrete build risk**, not just a documentation nit.

---

## 3. NEXUS_BRIEF.md / SCRATCH.md / OUTBOX.md / REMARK_20260628.md / OPEN_THREADS_2026-07-09.md

| File | Content summary | Disposition |
|---|---|---|
| `NEXUS_BRIEF.md` (76 lines) | Cross-war synthesis brief — VIEW/CALIBRATION/CROSS-DOMAIN/NEXT-DECISION/FORWARD-CATALYSTS, already framed as "the decoupling gap IS the signal" across both wars, 4 SENDING edges (BRENT/HENRY/LIQUID/SAM) | **Split-how**: content is ALREADY closest in structure/tone to what HAWK-synthesis's brief should look like post-split (per spec §5/§6 "thin, derived, reconciles A+B"). FALCON and OSPREY each need a fresh, theater-scoped NEXUS_BRIEF seeded from the relevant STATUS rows (§1 above) — current file is not directly copyable to either sibling without stripping the other theater's content. |
| `SCRATCH.md` (61 lines) | Mixed: CURRENT MARKS line is Iran-only (B/C/D + convergence), ADDENDUM block is 100% Russia (the HAW-15 tanker-campaign miss + correction), CHANGES/WHAT-I-DID/NEXT-SESSION interleave both theaters, MAIL STATE / PENDING PUSH are HAWK-account-level (not theater-specific) | **Split-how**: FALCON seeds from CURRENT MARKS + Iran-coded NEXT SESSION items (#1,2,4,5,6,7); OSPREY seeds from the ADDENDUM block + NEXT SESSION item #3; HAWK keeps MAIL STATE/PENDING PUSH pattern as its own (fresh, since mail is per-agent-directory) |
| `OUTBOX.md` (root file, 7 lines — distinct from the `outbox/` directory) | Already `🧊 FROZEN 2026-07-09` — dead stub superseded by the real `outbox/` dir; explicitly says "do not write signals to this file" | **Drop/archive** — zero content to migrate, not mentioned in spec (correctly, since it's inert) |
| `REMARK_20260628.md` (47 lines) | `SUPERSEDED 2026-07-08` historical artifact — the 6/28 vertical-kinetic re-mark that predates the 7/8 truce-collapse baseline; 100% Iran-theater content (B/C/D re-mark off the 6/26 baseline, pre-registered discriminators) | **freeze-in-place-under-HAWK** (per spec's "freeze historical, don't do lossy surgery" philosophy) — though its CONTENT is pure FALCON-theater, its VALUE is as calibration history, which the spec says freezes under HAWK alongside PREDICTIONS_ARCHIVE. Flag: if FALCON wants continuity, it should get a *pointer* to this file, not a copy. |
| `OPEN_THREADS_2026-07-09.md` (37 lines) | Snapshot of open Qs/gaps/threads-to-pull as of 7/9 — **mixed**: Q1/Q3/Q5/Q6(Iraq) = Iran; Q4(HAW-15)/gap-row-1(energy-strike ledger stale) = Russia; gap-rows 2/3/6 (cyber vector, Taiwan/Venezuela dormant) = HAWK-dormant | **Mostly superseded** — cross-check against 7/12 STATUS shows items #1 (energy-strike ledger backfill), #3 (Baghdad watch), #4 (P&I premium) are already resolved/actioned per SCRATCH's "WHAT I DID" + board_log. Live residue: Taiwan/Venezuela dormant re-sweep (still flagged "never actioned") → **HAWK-dormant** backlog item; everything else → **archive** (stale, superseded snapshot, not a current-state file) |

---

## 4. Everything-else inventory

| File | Vintage | What it is | Disposition |
|---|---|---|---|
| `TRADE.md` | 🧊 FROZEN 2026-07-01 (content Mar 11) | Legacy Mar-2026 trade sheet (USO calls, TLT puts, VIX spreads, LNG/Cheniere, fertilizer) from before the Mar 6 BRENT oil-handoff. Confirmed dead — HAWK holds no trade book (NEXUS_BRIEF "Position: None") | **freeze-in-place-under-HAWK** — historical-only, not addressed by spec (correct omission, it's inert) |
| `CALENDAR.md` | 🧊 FROZEN 2026-07-09 (content May 22) | Orphaned forward-catalyst calendar, not in CLAUDE.md FILES table, superseded by STATUS's own forward-catalyst sections | **freeze-in-place-under-HAWK** — dead surface, not addressed by spec |
| `MEMORY.md` | Feedback thru 2026-06-20 | Durable cross-session learnings (Feedback/Findings/References sections) — mixed Iran+Russia+generic lessons (see-saw discipline, conf-code discipline, deferral-dynamic anchor) | **freeze-in-place-under-HAWK** as the calibration-history record; per spec §8 each new agent's PREDICTIONS preamble "carries forward the relevant historical calibration lessons" — DAEDALUS should hand-pick which MEMORY.md bullets get copied (not moved) into OSPREY/FALCON's own fresh MEMORY.md at build time |
| `DECK_EVIDENCE.md` | Mar 13 2026 | 17KB Will-facing ranked slide-deck evidence assembly — 100% Iran/Gulf war content (Hormuz 97% traffic drop, Maersk suspension, 13Mbpd gap, Qatar LNG strike, sulphur→copper chain, NFP/Fed-trap) | **⚠️ NOT in spec's §4 migration table at all — a gap.** Content is unambiguously FALCON-theater and load-bearing (cited quote-ready slide sentences, still structurally relevant to the Iran thesis). Recommend: **FALCON** (or at minimum freeze-in-place-under-HAWK with a pointer from FALCON) — flagging to DAEDALUS as a spec omission, see §5 below. |
| `SOURCES.md` | Refreshed 2026-06-26 | Reference index of monitoring sources — Military/Diplomatic/Think-tank/News-wire/Defense-journalism/OSINT sections are generic; "Regional Focus" subsections are explicitly split by theater (Iran/ME, China/Taiwan, Russia/Ukraine, Venezuela/LatAm); Energy/Commodity section is BRENT-deferred | **SPLIT** — Iran/ME sources → FALCON; Russia/Ukraine sources → OSPREY; China/Taiwan + Venezuela/LatAm sources → HAWK-dormant; Military/Diplomatic/News-wire/OSINT generic sections → **copy to all three** (not theater-specific) |
| `board_log.tsv` | 66 rows, thru 2026-07-12 | Single shared BOARD/WALTER mail-processing log spanning both theaters + fleet-infra signals (DAEDALUS baghdad-watch/vulcan-seam/midas-seam notices, HENRY routing) | **⚠️ NOT addressed by spec at all — a gap**, see §5 below |
| `audits/*.md` (7 files) | All 2026-05-22 | Deep-dive audit snapshots: Gulf-hold-check, Barakah-attribution, US/Israel-posture, Hormuz-traffic, war-risk-insurance, stale-data-audit, synthesis — 100% Iran/Gulf-theater, none touch Russia | **freeze-in-place-under-HAWK** (51 days stale, not boot-read, not referenced by any live doc I found — this set is ~9 days from tripping the root CLAUDE.md ">60 days + not boot-read + not referenced → archive" rule regardless of the split; flag to whoever runs the next Staleness Sweep) |
| `research/BOARD_CATCHUP_2026-04-20.md` | Apr 20 | Board-consumption catchup on the Apr 21 Iran ceasefire-deadline thesis | **freeze-in-place-under-HAWK** (historical, superseded) |
| `research/DEADLINE_SCENARIO_TREE_APR21.md` | Apr 20 | Iran ceasefire-deadline scenario tree (leaf probabilities, single-action playbook) | **freeze-in-place-under-HAWK** (historical) |
| `research/POST_DEADLINE_PLAYBOOK.md` | Apr 20 | Iran post-deadline execution playbook (trigger confirmation checklist) | **freeze-in-place-under-HAWK** (historical) |
| `research/IRAN-CROSSAGENT-2026-02-18.md` | Feb 18 | Original Iran-crisis cross-agent-impact matrix, day-1 artifact | **freeze-in-place-under-HAWK** (historical, superseded many times over) |
| `research/REFINERS-UKRAINE-2026-02-18.md` | Feb 18 | US refiner (VLO/MPC) crack-spread trade rec off Ukraine refinery strikes — Russia/Ukraine-theater trigger, but a **trade** artifact from before the Mar 6 BRENT oil-handoff | **freeze-in-place-under-HAWK** (pre-handoff trade content, now BRENT's domain if revived — not live-load-bearing for either new agent) |
| `research/RUSSIA_OIL_INFRA_STRIKES_MAY-JUN2026.md` | **Jun 18 2026** (most recent research/ file) | Active gap-sweep of Ukraine strikes on Russian oil infra (May-Jun), cross-referenced to live KB-141/KB-184 IDs, explicitly distinguishes crude-export-terminal vs refinery/crack-spread channels — directly feeds the STRIKES.tsv ledger Reader B owns | **OSPREY** — live-load-bearing, this is working reference material for the Russia theater, not archival |
| `research/HERMES_V2_DESIGN_NOTE.md` | Jun 19 | HAWK-authored design input for a fleet mail-transport rebuild, requested by PROME — not theater content at all | **HAWK-keep** (fleet-infra artifact, theater-agnostic; arguably belongs with PROME/WALTER's messaging-overhaul effort per root CLAUDE.md's `messaging_overhaul` note, but it's inert either way — not part of the war-split) |
| `domain/sources/CRU_FERTILIZER_CRISIS_MAR10.jpg`, `FORCE_MAJEURE_MAP_MAR2026.jpg`, `MAERSK_ADVISORY_MAR9.png` | Mar 17 | Image evidence for the Mar-2026 Iran/Gulf disruption thesis (screenshots) | **freeze-in-place-under-HAWK** |
| `domain/sources/ENERGY_DOMINANCE_STRATEGY.md`, `LNG_DISRUPTION_MAR2.md`, `OIL_INFRASTRUCTURE_DISRUPTIONS.md`, `UNCTAD_HORMUZ_DISRUPTIONS_MAR10.pdf`, `UNCTAD_HORMUZ_DISRUPTIONS_MAR10_SUMMARY.md` | Mar 17 | Gulf/Hormuz primary-source evidence backing DECK_EVIDENCE.md's findings #1-6 | **freeze-in-place-under-HAWK** (archival backing for a frozen deck; FALCON should get pointers if DECK_EVIDENCE.md ports forward) |
| `domain/sources/STATUS_archive_20260222.md` (+`_full`), `_20260301.md`, `_20260626.md`, `_20260708.md` | Mar 17 – Jul 8 | Dated STATUS.md snapshots, archival record across the war's history | **freeze-in-place-under-HAWK** (this IS the historical STATUS record the spec's freeze-philosophy is meant to preserve) |
| `domain/sources/russia_oil_infrastructure_damage_assessment.md`, `ukrainian_energy_warfare_doctrine_thesis.md` | Mar 17 (old) | Russia/Ukraine-theater deep-dive content, but stale (not touched since original Mar build, superseded by the newer `research/RUSSIA_OIL_INFRA_STRIKES...` gap-sweep above) | **freeze-in-place-under-HAWK** (superseded by the live Jun 18 file; OSPREY can pull forward if it wants the doctrine-thesis background) |
| `memory/2026-02-18.md` | Feb 18 | Original cold-start bootstrap session note — all-theater (Iran/Russia/Taiwan/Venezuela/trade-war) day-1 snapshot | **freeze-in-place-under-HAWK** (bootstrap historical record) |
| `templates/SCRATCH.template.md` | Jun-era | The SCRATCH.md template DAEDALUS/HAWK uses at closeout | **HAWK-keep + copy-to-OSPREY-and-FALCON** — build-scaffolding item; each new agent needs its own copy (theater-agnostic template, trivial to duplicate) |
| `inbox/processed/*` (8 files) | Jul 1 – Jul 11 | Already-integrated cross-agent signals (PROME/DAEDALUS/HENRY notices) | **N/A-transient** (processing log, freeze-in-place-under-HAWK as archival trail) |
| `inbox/WALTER/processed/*` (14 files) | Jun 28 – Jul 10 | Already-integrated WALTER signal packets | **N/A-transient** (same treatment) |
| `outbox/*.md` (8 files, root level) | Jun 20 – Jul 12 | Outbound signal packets to BRENT/PROME/DAEDALUS, including the two 7/12 packets announcing the split itself | **N/A-transient** — historical mail trail; the two split-announcement packets (`..._to-DAEDALUS_war-agent-split-build-spec.md`, `..._to-PROME_war-agent-split-roster-notice.md`) confirm HAWK already routed this correctly |
| `outbox/delivered/.gitkeep` | — | Empty placeholder | **N/A-transient** |

---

## 5. Surprises / contradictions (spec gaps found)

1. **`DECK_EVIDENCE.md` is entirely unaddressed by the spec's §4 migration table.** It's a substantial (17KB), Will-facing, still-citable Iran/Gulf evidence deck — the kind of asset a rebuilt FALCON would plausibly want a pointer to, or at minimum should not silently orphan. Not fatal (freeze-in-place-under-HAWK is a safe default) but worth an explicit line in the build spec rather than falling through the cracks.
2. **`board_log.tsv` (66-row BOARD/WALTER mail-processing ledger) is not mentioned anywhere in the spec.** Unlike KB/VX/FLOW/predictions (which the spec explicitly freezes-or-splits), there's no stated disposition for this file. Recommend treating it like KB.tsv: freeze the current 66-row ledger under HAWK as historical, each new agent starts a **fresh** `board_log.tsv` at build time (mirrors the "fresh KB seeded from live STATUS" pattern in spec §4). Flag to DAEDALUS/PROME for §13 ratification — this is a real open decision the spec missed, not just a documentation nit.
3. **`TRADE.md` and `CALENDAR.md` are both dead/frozen and outside the spec's scope — correctly, since neither holds live content — but confirms HAWK genuinely holds no trade book** (cross-checked against NEXUS_BRIEF's explicit "Position: None"), so there's no position-migration risk in this split. Worth stating affirmatively rather than assuming.
4. **DOMAIN SCOPE and CROSS-AGENT SIGNALS sections in CLAUDE.md are NOT cleanly file-level splittable** — they're single tables whose individual rows belong to three different owners (FALCON / OSPREY / HAWK-dormant). The spec's §4 migration table implies mostly whole-file moves; these two sections need line-level hand-editing at build time, which is a materially different (slower) migration step than "copy file, rename." Flag as the highest-complexity single piece of the CLAUDE.md rebuild.
5. **No file I found contradicts the spec's headline assumptions** (HAWK holds no trade book, the two OPEN predictions HAW-16/HAW-17 map cleanly to FALCON/OSPREY exactly as spec §4/§8 predicts, `baghdad_watch.py` is genuinely Iran/Iraq-only and correctly assigned to FALCON). The spec's factual premises check out against the live files.
6. **Dangling ref already resolved, not live:** the `CEASEFIRE_FADE_PROTOCOL.md` mention in CLAUDE.md boot step 11 is explicitly marked as a retired/fixed dangling reference (2026-07-08, DAEDALUS BATCH_03) — no action needed, noted only so it isn't re-flagged as a fresh finding.

**File I could not fully classify:** none outright, but `research/REFINERS-UKRAINE-2026-02-18.md` sits ambiguously between OSPREY (Ukraine-strike trigger) and BRENT (it's a pre-handoff *trade* artifact, and trades are BRENT's domain since Mar 6) — recommend HAWK-freeze with no forward pointer, since it's neither theater-tracking nor current trade content.

---

*Manifest A complete. Cross-check Manifest B (workbook/energy-strikes) and Manifest C (thesis/LESSONS/scripts) for the remaining scope before DAEDALUS ratifies §13 open decisions.*
