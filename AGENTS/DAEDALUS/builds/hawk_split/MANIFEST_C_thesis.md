# HAWK Split — Manifest C: thesis/, LESSONS.md, scripts/

> 🗄 **DATED BUILD-EXECUTION RECORD (2026-07-12; bannered 2026-08-17, self-audit F5 — same class as the 8/11 upgrades/ pass, which was scoped to upgrades/ only).** One-shot record; not maintained.

**Reader:** C (thesis, predictions, lessons, scripts) | **Date:** 2026-07-12 | **Scope:** `AGENTS/HAWK/thesis/`, `AGENTS/HAWK/LESSONS.md`, `AGENTS/HAWK/scripts/`
**Spec referenced:** `AGENTS/HAWK/design/2026-07-12_war-agent-split-spec.md` (§4 migration table, §7 Tier-1 fixes, §8 prediction namespace)

---

## 1. PREDICTIONS.tsv — full row table

Schema: `Pred_ID | Date_Made | Prediction | Confidence | Timeframe | Status | Date_Resolved | Outcome | Invalidation | Notes`. Scoreboard preamble (lines 1-16) = header comment block: running tally line, high-confidence-failure list, calibration-discipline notes, failure-pattern synthesis, a data-quality note (stray-tab rows), pointer to `PREDICTIONS_ARCHIVE.md` for full post-mortems.

| ID | Status | Resolved | Theater | Disposition |
|---|---|---|---|---|
| HAW-01 | CONFIRMED | 2026-02-28 | Iran/US | FALCON (frozen historical) |
| HAW-02 | CONFIRMED | 2026-03-03 | Iran/US (Hormuz) | FALCON (frozen historical) |
| HAW-03 | FAILED | 2026-06-20 | Venezuela (dormant) | **HAWK** (dormant book — not A/B) |
| HAW-04 | FAILED | 2026-04-20 | Iran/US scenario ladder | FALCON (frozen historical) |
| HAW-05 | PARTIALLY | 2026-04-20 | Hezbollah/Lebanon | FALCON (frozen historical) |
| HAW-06 | FAILED | 2026-04-21 | Iran/US ceasefire | FALCON (frozen historical) — **CALIBRATION ANCHOR, carry forward** |
| HAW-07 | VOIDED | 2026-04-21 | Iran/US ceasefire→Brent (conditional on HAW-06) | FALCON (frozen historical) |
| HAW-08 | CONFIRMED | 2026-04-22 | Iran/US kinetic | FALCON (frozen historical) |
| HAW-09 | CONFIRMED | 2026-06-13 | Iran-Pakistan talks | FALCON (frozen historical) |
| HAW-10 | FAILED | 2026-07-08 | Houthi/Bab-al-Mandab | FALCON (frozen historical) — wording-wedge lesson source |
| HAW-11 | FAILED | 2026-06-22 | Gulf energy infra (decoupling kill-switch) | FALCON (frozen historical) — thesis-load-bearing |
| HAW-12 | CONFIRMED | 2026-06-22 | Iran/US diplomacy (Switzerland/Vance) | FALCON (frozen historical) |
| HAW-13 | FAILED | 2026-07-04 | Hormuz verification gates | FALCON (frozen historical) |
| HAW-14 | FAILED (re-scoped) | 2026-07-12 | Iran direct-kinetic-on-US/Israel | FALCON (frozen historical) — post-mortem owed to ARCHIVE |
| HAW-15 | **FAILED** | 2026-07-12 | **Russia/Ukraine crude-export terminals** | **OSPREY** (frozen historical) — the HAW-15 miss is OSPREY's founding calibration lesson |
| HAW-16 | **OPEN** | — | Iran/Gulf production-infra + vessel-sunk kill-switch | → **FALCON**, re-register `FAL-01 ←HAW-16` |
| HAW-17 | **OPEN** | — | Russia/Ukraine shadow-fleet → world-crude disruption | → **OSPREY**, re-register `OSP-01 ←HAW-17` |

**Total: 17 rows = 5 CONFIRMED / 8 FAILED / 1 PARTIALLY / 1 VOIDED / 2 OPEN.**

### OPEN-row verification: spec's claim is CORRECT, but the preamble tally is now stale
The spec's §8 claim ("HAW-16 and HAW-17 are the only OPEN rows") is **CONFIRMED true** by direct row inspection — no other row carries `Status = OPEN`.

However, the file's own scoreboard preamble (line 2: *"5 CONFIRMED / 7 FAILED / 1 PARTIALLY / 1 VOIDED / 2 OPEN (HAW-15, HAW-16)"*) is **stale/self-inconsistent** as of this read: it still lists HAW-15 as OPEN and undercounts FAILED by one. Both HAW-14 and HAW-15 resolved FAILED later in the same 2026-07-12 session that produced the preamble text, and the preamble was never re-totaled after those two closes (nor does it count HAW-17, registered same day). **Flag for whoever owns the freeze:** re-total the preamble line to `5/8/1/1/2 (HAW-16, HAW-17)` before freezing HAW-01..17, or freeze it with an explicit "preamble stale as of resolution — see row data" note so the frozen record isn't read as authoritative on the count.

---

## 2. PREDICTIONS_ARCHIVE.md — structure + lesson split

Structure: one `## HAW-NN` section per **closed** prediction (anchor `#hawk-NN`), each with the verbatim Outcome/Notes from PREDICTIONS.tsv at time of relocation, reference-only, **not boot-loaded**. Currently holds HAW-01, 02, 03, 04, 05, 06, 07, 08, 09, 11 (10 sections) — **missing HAW-10, HAW-12, HAW-13, HAW-14, HAW-15** post-mortems (all resolved after the archive's last edit; HAW-14 and HAW-15 explicitly say "Post-mortem owed → PREDICTIONS_ARCHIVE.md#hawk-14/15" in their own Notes column — **not yet written**). This backfill is orthogonal to the split but should happen before/during the freeze so the frozen archive is complete.

**Calibration lesson split** (per spec §8, "each new agent's PREDICTIONS preamble carries forward the relevant historical lessons"):

| Lesson | Source | → FALCON | → OSPREY | Cross-cutting (both) |
|---|---|---|---|---|
| HAW-03 stale dormant-vector (95%-conf prediction wrong for 5.5mo, unswept) | Venezuela | | | ✅ — re-sweep discipline applies to any dormant/secondary vector either sibling might carry |
| HAW-06 deferral-dynamic anchor ("armed pauses, not clean breaks" on deadline events) | Iran ceasefire | ✅ **primary inheritor** (spec-named) | | |
| HAW-07 VOIDED-vs-CONFIRMED discipline (no right-for-wrong-reasons credit on conditionals) | Iran ceasefire→Brent | ✅ | | ✅ — applies to any conditional prediction either agent writes |
| HAW-08/09 pre-registration + action-based rubric + 2nd-independent-path | Iran kinetic/diplomacy | ✅ | | ✅ — general calibration discipline |
| HAW-10 wording-identity (prediction text vs. promotion-threshold text must match) | Houthi/Bab-al-Mandab | ✅ | | ✅ — same class as HAW-14's catalyst-locus issue, general enough to copy |
| HAW-11 kill-switch framing (expiry = confirming datum for decoupling) | Gulf energy infra | ✅ | | |
| HAW-14 locus-vs-mechanism wording (write the mechanism, not the trigger) | Iran kinetic re-scope | ✅ **primary inheritor** (source event) | | ✅ — directly the same failure class as HAW-15/OSPREY's mechanism lesson, so copy-worthy |
| **HAW-15 mechanism-search + own-ledger-staleness** (search the mechanism not named targets; verify ledger's own last-updated before trusting it as baseline) | **Russia/Ukraine crude channel** | | ✅ **primary inheritor** (spec-named: "crude-channel/ledger-staleness") | ✅ — spec explicitly names this cross-cutting (§4: "mechanism-not-target, ledger-staleness → all three") |

Recommendation: FALCON's PREDICTIONS.tsv preamble carries HAW-06, HAW-07, HAW-08/09, HAW-10, HAW-11, HAW-14 (its own theater's history) plus the cross-cutting mechanism/ledger-staleness note; OSPREY's preamble carries HAW-15's full lesson (its only real precedent) plus the same cross-cutting note; HAWK-synthesis keeps HAW-03 (dormant-vector re-sweep — HAWK owns the dormant book) and a one-line pointer to the frozen HAW-01..17 record for anyone needing the full history.

---

## 3. THESIS.md — section map

**Surprise up front:** THESIS.md is **100% Iran/US-theater content** — there is no Russia/Ukraine material anywhere in it. The spec's §4 row for `thesis/` says "Split by theater; cross-war decoupling thesis → HAWK," which implies mixed content requiring surgery. It doesn't need surgery — **the whole file is FALCON's**, not a split. (It is also already SUPERSEDED per its own banner — see below.)

| Section | Lines | Summary | Disposition |
|---|---|---|---|
| Superseded banner | 1 | Points to STATUS.md as canonical (Apr 20 version is stale); flags "THESIS rewrite to current regime remains an open backlog item" | Carries as-is — FALCON inherits the backlog item |
| Header / CORE THESIS | 5-18 | Ceasefire-lapsing framing, Apr 20 snapshot, Iran/US only | FALCON |
| Three Transmission Channels | 22-68 | Channel 1 deadline→oil→macro, Channel 2 infra-damage→duration, Channel 3 ship-on-ship→accidental escalation — all Iran/Gulf | FALCON |
| Key Thresholds table | 72-84 | Apr 21 deadline, Brent levels, Hormuz transit — Iran-specific | FALCON |
| Scenario Framework (B/C/D) | 88-109 | Iran/US B/C/D ladder — this IS "the A/B/C/D ladder" the spec names as FALCON's framework (§2) | FALCON |
| Convergence Matrix | 113-127 | 9-vector Iran/Gulf matrix | FALCON |
| Conviction Level | 131-135 | Iran ceasefire thesis-break condition | FALCON |
| Cross-agent links | 139-149 | BRENT/CARL/HENRY/LIQUID/SAM/REGINALD/RED/BROCK/ZHAO — Iran-framed | FALCON (re-point through HAWK synthesis per new transmission chain, §10 of spec) |
| Exit Protocol Status | 153-164 | 0/7 Iran-specific criteria | FALCON |

**No mixed-theater sections found.** No "cross-war decoupling thesis" content exists in this file to route to HAWK — that thesis (Damage-vs-Salvo decoupling) lives in `workbook/FLOW.tsv` FLOW-HAWK-19 per the file's own banner, outside Reader C's scope (flag for whichever reader covers `workbook/`).

**CHANGELOG.md** (audit trail for THESIS/TIMELINE): also 100% Iran-theater history (v1.0 creation, v1.1 Brent correction) — same disposition, FALCON, with the versioning convention note ("THESIS vX.Y") carried forward as a pattern both siblings should adopt for their own thesis docs.

**TIMELINE.md**: also 100% Iran-theater (Feb 28 war start → Apr 20 ceasefire, forward branch points, war-day tracking) — FALCON. Its "FORWARD BRANCH POINTS" and "RESOLUTION MARKERS" table format is a reusable pattern OSPREY could adopt for its own timeline (structural pattern, not content).

---

## 4. LESSONS.md — item-by-item

4 entries total, "read at boot" (SPAWN PROTOCOL step 4 per file header).

| # | Date | Lesson | Source incident | Disposition | Note |
|---|---|---|---|---|---|
| 1 | 2026-06-12 | Prediction text and promotion-threshold text must be written identically | HAW-10 (Houthi/Bab-al-Mandab) + GULFSTATE-01 — both Iran/Gulf | **FALCON** (per spec: "Iran lessons → B") | Underlying principle (wording-identity discipline) is generic enough OSPREY should read it too, but per spec's explicit source-based split it's FALCON's |
| 2 | 2026-06-12 | Live-war boot needs a day-by-day gap sweep, not topic searches | Iran war (Jun 11 Hormuz closure + 2nd strike night missed by topic-search) | **FALCON** (source), but flag **copy-worthy to OSPREY** — this is a general "active-conflict boot methodology" lesson, not Iran-specific in mechanism | Recommend copy-to-all-three despite Iran-sourced origin |
| 3 | 2026-06-20 | A deprioritized secondary vector can go stale for months — re-sweep dormant vectors | Venezuela (dormant/secondary vector) | **HAWK** (dormant-book owner, not A or B) | Not in the task's {OSPREY, FALCON, copy-to-all-three} taxonomy as given — this is HAWK's own lesson since HAWK owns the dormant book post-split. Also copy-worthy to A/B for whatever secondary vectors *they* carry |
| 4 | 2026-07-12 | Search the MECHANISM not just the named targets (+ Corollary 2: don't trust your own ledger without checking last-updated) | HAW-15, Russia/Ukraine crude-export vs. shadow-fleet-tanker channel | **copy-to-all-three** (spec explicitly names this: "cross-cutting: mechanism-not-target, ledger-staleness") | Sourced 100% from Russia/Ukraine theater — OSPREY is the primary inheritor, but rule text is generic and the spec calls for copying it to all three |

**Split counts: 2 → FALCON only, 0 → OSPREY only, 1 → HAWK only (not in spec's taxonomy), 1 → copy-to-all-three explicit, plus 1 of the FALCON-sourced ones (#2) flagged as copy-worthy.**

**Surprise:** the "parallel-channels" cross-cutting lesson named in this task's brief (commit `5d246d25`: *"Pattern1 corrected — channels run in PARALLEL not sequential"*) is **not in LESSONS.md** — it lives in `domain/energy-strikes/SUMMARY.md` (outside Reader C's assigned scope). Flag to whichever reader covers `domain/` — that file needs the same cross-cutting-lesson treatment as items 3-4 here.

---

## 5. scripts/ — table

| File | What it does | Disposition | Path-portability notes |
|---|---|---|---|
| `PLAN.md` | Design doc for the whole scripts/ suite (not a script) — dated Apr 20, "Draft" status, describes boot.py + 5 sub-scripts | Mostly **FALCON reference** (facility/threshold content is 100% Gulf/Iran) but the `boot.py`-orchestrator **pattern** (priority-ordered sequence, consolidated brief, BOOT_LOG.md) is theater-agnostic and reusable by OSPREY | No code, no paths — pure doc. Note it predates the FROZEN decision on boot.py (see below) and is itself stale/aspirational, not a record of what shipped |
| `baghdad_watch.py` | Boot-time RSS monitor of US Embassy Baghdad alert feed for the Iran/Iraq PMF-backlash discriminator; flag-not-fire (rc 0/1/2) | **FALCON** (per spec, Iran/Iraq discriminator) | **Well-portable already**: `STATE_PATH = Path(__file__).resolve().parent / ...` — cwd-proof, self-locating, no hardcoded `AGENTS/HAWK/` in the *code*. Docstring comments cite `STATUS.md:69,82` and an inbox path — cosmetic, update on move but won't break execution. **Must-fix on move:** `AGENTS/HAWK/CLAUDE.md` line 34 hardcodes the invocation path `python3 "$(git rev-parse --show-toplevel)/AGENTS/HAWK/scripts/baghdad_watch.py"` (boot step 5b) and the FILES table (line 271) documents it under HAWK — both need to become `AGENTS/FALCON/scripts/baghdad_watch.py` in FALCON's own CLAUDE.md; nothing to fix in HAWK's post-split CLAUDE.md except removing the reference |
| `baghdad_watch_state.json` | Seen-GUID + last-run state for the above, committed (cross-machine continuity) | **FALCON** (moves with the script) | `git mv` preserves it; no path logic inside the JSON itself |
| `boot.py` | Master orchestrator for the 5 sub-scripts below; **FROZEN 2026-07-09**, not wired into boot | **FALCON** (all content — hardcoded "War Day 51 / Ceasefire Day 8 / D82-C12-B6" — is Iran-specific and already flagged by its own docstring as contradicting current STATUS.md) OR candidate for outright retirement | Uses `Path(__file__).resolve().parent` / `.parent.parent` — portable if revived, but its own docstring says do NOT re-wire without a live-data-source audit first (PAT-034 already logged this). Recommend: carry the FROZEN file to FALCON/scripts/ unchanged (historical), flag DAEDALUS's PAT-034 lesson travels with it, do not silently re-enable |
| `catalyst_countdown.py` | Parses `CALENDAR.md` for a date-driven countdown table, 🔴 alerts within 7 days | **Split — each sibling needs its own copy** (theater-agnostic code, reads a per-agent CALENDAR.md) | `HAWK_DIR = Path(__file__).resolve().parent.parent` → self-locating, portable as-is to either dir. **Surprise: `CALENDAR.md` is not in the spec's §4 migration table at all** — it needs splitting alongside STATUS/SCRATCH/NEXUS_BRIEF (spec only names those three explicitly); flag to whoever executes migration |
| `oil_infrastructure.py` | Hardcoded facility registry (Fujairah/Ras Laffan/ADCOP/Yanbu/Al Taweelah/Kharg) with status + repair-timeline, all `last_update: 2026-04-13` | **FALCON** — 100% Gulf/Iran facilities, no Russia analog exists in this file | `HAWK_DIR = Path(__file__).resolve().parent.parent`, portable. **Data is ~3 months stale** (last_update 04-13 vs. today 07-12) — flag for FALCON to refresh, not a portability issue but a freshness one. OSPREY has no equivalent script; would need a net-new Baltic/Black-Sea-terminal version built from scratch (relates to spec's open decision #4) |
| `sanctions_tracker.py` | Web-search-driven shadow-fleet/sanctions/insurance-market monitor; `BASELINE_METRICS` hardcoded (Iran-Gulf war-risk premium, Hormuz coverage) explicitly marked "placeholder" | **FALCON** as-is; **pattern reusable by OSPREY** (Russia shadow-fleet/sanctions is arguably the more active current story per HAW-17) | Portable code (`Path(__file__)`-based). This is the clearest case for spec's open decision #4 ("does OSPREY want an analogous automated feed") — recommend DAEDALUS build OSPREY a parallel `sanctions_tracker.py` seeded with Russia shadow-fleet baseline metrics rather than copying Iran's placeholder numbers |
| `thresholds.py` | Pulls live Brent (`yfinance`) and checks against hardcoded scenario thresholds ($150/$120/$100/$80/$60) labeled with Iran-specific triggers ("Kharg strike or Hormuz closure", "controlled burns framework") | **FALCON**, needs threshold-label refresh (framework superseded per THESIS.md banner) | Portable (`Path(__file__)`-based). OSPREY needs its OWN thresholds.py with Russia/crude-export-relevant trigger levels — not a copy, a fresh build (no existing Brent-trigger framework for the Russia channel in this corpus) |
| `war_monitor.py` | Web-search-driven daily war-developments summary + scenario-probability (D/C/B) tracker; `SCENARIO_BASELINE = {"D":82,"C":12,"B":6}`, `CEASEFIRE_START = Apr 12 2026` hardcoded | **FALCON**, needs a full data refresh (hardcoded scenario numbers are stale — same staleness boot.py's own docstring already flagged) | Portable (`Path(__file__)`-based). No Russia equivalent; OSPREY would need its own scenario-ladder concept if one gets built (none currently exists for that theater in this corpus — worth flagging to whoever drafts OSPREY's framework, since spec §2 gives OSPREY the "crude-vs-products channel model" not a B/C/D ladder) |

---

## 6. Surprises (contradicting or extending the spec)

1. **THESIS.md/TIMELINE.md/CHANGELOG.md have ZERO Russia/Ukraine content** — the spec implies these need theater-splitting; in reality they move to FALCON wholesale, no surgery needed. The "cross-war decoupling thesis" the spec assigns to HAWK isn't in these files — it lives in `workbook/FLOW.tsv` FLOW-HAWK-19 (outside this reader's scope).
2. **PREDICTIONS.tsv scoreboard preamble is stale/self-inconsistent** relative to its own rows (still counts HAW-15 as OPEN, undercounts FAILED, doesn't count HAW-17) — needs a re-total before/at freeze time, independent of the split.
3. **PREDICTIONS_ARCHIVE.md is missing 5 post-mortems** (HAW-10, 12, 13, 14, 15) that its own source rows say are owed — a backfill gap that predates the split but should be closed before freezing HAW-01..17 as the "load-bearing calibration memory."
4. **HAW-03 (Venezuela) doesn't fit the OSPREY/FALCON binary** — it's dormant-book, disposition is HAWK itself, which the task's taxonomy didn't anticipate.
5. **CALENDAR.md is missing from the spec's §4 migration table** even though `catalyst_countdown.py` depends on it and it clearly needs the same STATUS/SCRATCH/NEXUS_BRIEF-style per-agent split.
6. **The "parallel-channels" cross-cutting lesson (commit 5d246d25) is not in LESSONS.md** — it's in `domain/energy-strikes/SUMMARY.md`, outside this reader's scope; flag to the domain/-scope reader.
7. **`boot.py` and 4 of 5 of its sub-scripts carry stale, hardcoded Iran-scenario data** (War Day 51 / D82-C12-B6 / Ceasefire Apr 12) that materially contradicts the current STATUS.md ladder — none of this is a Russia/Ukraine-relevant asset, and none of it is portability-broken, but a straight `git mv` to FALCON would carry stale numbers into a fresh agent's scripts/ directory looking authoritative. Recommend a refresh pass, not a blind move.
8. **No Russia/Ukraine-equivalent automation exists anywhere in scripts/** — `baghdad_watch.py` is the only "class" of script the spec flags for cross-theater consideration (open decision #4); OSPREY starts with zero scripts unless DAEDALUS builds new ones.

---

*Written by Reader C for DAEDALUS's HAWK-split comprehension fan-out, 2026-07-12.*
