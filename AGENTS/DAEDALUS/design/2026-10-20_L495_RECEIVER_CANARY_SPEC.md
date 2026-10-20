# L495 — Receiver-side canary for every routing path · SPEC LETTER v1

**Author:** DAEDALUS · **Written:** 2026-10-20 09:17–09:2x ET (`date` 09:17 at start; hook clock 09:19 at the plan read; my first stamp ran ahead of the clock and was corrected — PAT-188) · **Row:** `PROME/DOCKET.tsv` L495 (Will 9/25 14:08 ET "proceed in order", system item 1) · **State:** SPEC DELIVERED — v1, plan-read by one independent reader (§9); **no leg implemented**. DAEDALUS writes the class; each path owner implements its own leg; an independent reader runs before any leg is called fixed (WQ-229).

**Sources read:** WALTER packet `PROME/inbox/processed/2026-09-25_from-WALTER_intake-scan-never-surfaced-WATCH_HIT-fixed-plus-old-lists-noise.md` (cc9c14017) · `PROME/proposals/2026-09-25_wq295-dark-desk-class-PROPOSAL.md` § R3 addendum 3 · LIQUID packet `PROME/inbox/processed/2026-09-25_from-LIQUID_HY-280-touch-investigation.md` § Found and routed · `AGENTS/WALTER/tools/intake_scan.py` (header + `collect_alerts`, read 10/20) · `~/.config/systemd/user/liquid-hy-watch.{service,timer}` and `Research-Intake/.github/workflows/collect.yml` (read 10/20).

## 1. The defect class, in one line

**A route is dead at the consumer while both ends read green.** The producer's own check passes (it emitted the item), the consumer's own check passes (it processed everything it recognised), and nobody asserts that *what the producer emitted is what the consumer surfaced*. 9/25 instance: the lane emitted `NEW_WATCH_HIT` and `DEVELOPMENT` items; `intake_scan.collect_alerts()` built records only from `NEW_ALERT`/`NEW_WATCH` counts; 17 + 8 items were lost 9/18–9/24 with every check clean. Memory: `finding_transfer_completes_only_when_the_receiver_encodes`.

**Why a synthetic item, not only a count check:** a count reconciliation (producer `by_class` vs consumer records) is cheap and catches the 9/25 shape, but on a day with zero real watch hits it compares 0 with 0 and passes vacuously (PAT-155: an empty population satisfies every universal check). A canary guarantees a non-empty population on every run. **Both are required; neither substitutes for the other.**

## 2. Definitions

| Term | Meaning |
|---|---|
| **Path** | One producer → consumer edge that carries items to a desk or to a Will-facing surface. Registered in the L496 register (`design/2026-10-20_L496_UNATTENDED_REGISTER_BLUEPRINT.md`), column `canary_path_id`. |
| **Item class** | Each distinct kind of item the producer emits that the consumer is supposed to surface (e.g. `NEW_ALERT`, `NEW_WATCH`, `NEW_WATCH_HIT`, `DEVELOPMENT`). **One canary per PER-ITEM class.** A class the consumer reads only as a COUNT (today `NEW_ALERT`/`NEW_WATCH` in `intake_scan.py`, from `by_class`) cannot carry an item canary; it is covered by AC8's count reconciliation alone and the report labels it `count-only`. A class with neither is uncovered, and the report says so. Per-class injection recipe: `NEW_WATCH_HIT` = a reserved WATCH_FOR phrase (§5 P1); `DEVELOPMENT` = a reserved known-entity name **plus** an escalation qualifier, since the lane classifies DEVELOPMENT only on entity + qualifier. |
| **Injection point** | The earliest point at which a real item of that class enters the path: the producer's INPUT, or its classifier. Never its output file. A canary written straight into the output tests the file write, not the classifier — the 9/25 defect was in the class filter. |
| **Assertion site** | The consumer artifact a human or desk actually reads (WALTER's worklist / BOARD candidate list, a desk inbox, `PROME/inbox`, a SIGNALS row). Not the producer's log, not the consumer's own "processed N" counter. |
| **Canary key** | `CANARY-<YYYYMMDD>-<path_id>-<class>`, carried in the item's title AND in a structured field `canary: true`. |

## 3. Acceptance conditions — the properties every leg must have (written before any implementation)

Stated in the defect's terms (WQ-229), not as a restatement of the symptom.

| # | Condition | Fails when |
|---|---|---|
| **AC1 Receiver-side** | The PASS/FAIL verdict is computed at the assertion site, by the consumer's boot, from the consumer's artifact. | the verdict is read from the producer's log or a consumer self-count |
| **AC2 Per class** | Every item class the consumer is meant to surface has its own canary and its own verdict line. | one canary stands for several classes, or a class is silently uncovered |
| **AC3 Fresh** | The canary asserted must carry **today's** run key (the latest expected producer run, per the producer's schedule in L496). Yesterday's canary present + today's absent = FAIL `STALE`. | an old canary satisfies the check (the LIQUID 28-day-stale class) |
| **AC4 Loud** | FAIL and UNKNOWN print at the consumer's boot **before** triage begins, name the path + class + last good date, and are carried into that boot's report. | a FAIL can scroll past, or is logged only |
| **AC5 Fail-closed on missing input** | An unreadable producer output, missing lane clone, or failed pull yields `UNKNOWN` (rc 2 class), never PASS. | absence of evidence reads as health |
| **AC6 Inert** | A canary never reaches Will, never counts toward a BOARD total, never fires a doorbell or spawn, never enters a seen-set that could suppress a real item, and is closed by the same boot that asserts it. **Mechanism (required, not optional):** the consumer builds the canary's record through the SAME code path as a real item, then — as its last step before emitting the worklist — moves every record with `canary: true` into a separate `canary` section of its output, computes the verdict there, and prints the verdict lines first. The triage worklist, BOARD candidates, seen-set write (`--mark`) and doorbell inputs are built from the non-canary section only. | a canary is routed, counted, or dedupes a real item; or the canary is diverted BEFORE the shared code path (then it tests nothing) |
| **AC7 Non-masking** | A canary must not satisfy a real item's dedup key, and a real item must not satisfy a canary assertion. Match on the structured `canary: true` field + key, never on title text. **Schema work this requires (part of P1, both halves):** the lane writes `canary: true` on the item in `news.json`; the consumer copies it onto the record (today `collect_alerts()` builds records from classification/title/watch_hits and carries no such field); canary dedup keys use a `canary:` namespace so they never collide with the `sha1(title)` keys of real items. | dedup or assertion matches across the canary/real boundary |
| **AC8 Count reconciliation beside it** | For every class: consumer records == producer `by_class` count for the same run. The canary IS counted in the producer's `by_class` (it passed the classifier) and is subtracted explicitly: `real_records + canary_records == by_class`. Documented dedup is itemised as one line per dropped key. Mismatch = FAIL `DROPPED n`. | real items drop while the canary passes (a canary-specific code path) |
| **AC10 Same dispatch path** | The canary's owner is a designated test-desk entry in the SAME owner→desk map real desks use, so the canary exercises owner lookup and dispatch, not a side branch. Its delivery is then asserted at P2 (dispatch output), chaining P1→P2. | the canary routes through an unknown/test-owner branch real desks never take (reader counterexample, 10/20) |
| **AC9 Falsified on the historical defect** | The lane leg's assertion, run against `intake_scan.py` as of the parent of `cc9c14017`, reports FAIL for `NEW_WATCH_HIT` and `DEVELOPMENT`; against the fixed version, PASS. Both outputs are pasted into the leg's acceptance file. | the check was never shown to fail on the defect it exists for (CHECK_STANDARD §3) |

## 4. Neighbour tests each leg's acceptance file must cover (or justify N/A in one line)

| Category | Required fixture |
|---|---|
| **Ordinary** | One canary per class arrives → one PASS line per class naming the key. |
| **Overlap** | A real item with the same title words as the canary → not deduped against the canary; a canary present on a day with real items of its class → both counted, reconciliation exact. |
| **Wrong owner** | Canary addressed to desk X → asserted at X's worklist/inbox, and its presence in desk Y's list = FAIL `MISROUTED`. (For the lane: WATCH_HIT owner = the desk whose phrase fired — the canary uses a reserved phrase registered to a named test owner, see §5.) |
| **Missing information** | Producer output unreadable / lane not pulled → UNKNOWN, rc 2. Canary class present in producer, absent at consumer → FAIL. |
| **Concurrent activity** | Two producer runs in one day (manual `workflow_dispatch` + cron) → idempotent on the canary key; no duplicate FAIL. |
| **Stale** | Yesterday's canary present, today's absent → FAIL `STALE`, not PASS. |

## 5. The legs — owner, injection, assertion

| Path id | Producer → consumer | Injection point | Assertion site | Owner of leg | Notes |
|---|---|---|---|---|---|
| **P1 lane→WALTER** | RESEARCH-INTAKE `collect.yml` (daily 15:00 UTC) → `intake_scan.py` → WALTER worklist | Lane side: one synthetic news item per class, generated by the lane run itself (so the canary is subject to the lane's own classifier). For `NEW_WATCH_HIT` a reserved WATCH_FOR phrase (`daedaluscanaryphrase`, ≥4 chars so the matcher keeps it — `project_research_intake_collection_lane`) registered to a test owner, never to a live desk | WALTER boot step 7e, the `canary` section of `intake_scan` output (AC6), before triage | **Lane half: PROME** (lane owner; a free-feed change, C7 class). **Consumer half: WALTER** (`intake_scan.py`). Matches the L496 seed row. | AC9 drill runs here first. AC7 schema work spans both halves. |
| **P2 WALTER→desk** | WALTER dispatch → `AGENTS/<X>/inbox/` + BOARD | One canary handoff per dispatch class to a designated test inbox (`AGENTS/WALTER/registry/canary_inbox/` — WALTER's own tree, so no desk is woken) | WALTER's next boot reads the test inbox + delivery_log | **WALTER** | Covers the write path only; desk-side reading is the desk's boot (out of scope v1, §7). |
| **P3 LIQUID hy_oas_watch** | systemd `liquid-hy-watch.timer` (Mon–Fri 13:00 ET) → `AGENTS/LIQUID/alerts/` → PROME/inbox + SIGNALS row | Not a synthetic market print (never fabricate a level into a live alert path). Instead: the watcher writes a run-stamp line `{run_at, input_series_last_obs_date, state_text_source, state_text_as_of}` every run; the canary is the run-stamp | The surface the timer actually delivers to (LIQUID to name it: `alerts/` local file, or `PROME/inbox` / SIGNALS row if the watcher writes there) — asserted at LIQUID's boot: today's run-stamp exists AND `state_text_as_of` is not older than the latest arbiter ruling in LIQUID's ledger | **LIQUID** | This is the stale-arbiter class: assert the *age of the carried judgment*, not only the run. ⚠️ **`AGENTS/LIQUID/alerts/` is gitignored** (`AGENTS/LIQUID/.gitignore:2`), and the timer runs on the desktop only: a run-stamp there is **host-local**. The leg declares that scope: on the desktop it asserts; on the laptop it prints ONE line `CANARY P3 UNKNOWN reason=HOST-LOCAL` per session, by design, never a per-run red. An unattended timer does not commit, so a committed stamp is not available without a new write path (Will's/LIQUID's call, not this spec's). Input-vintage lateness (13:00 run vs ~16:15 FRED publish) is L496's `input_publish_time` column. |
| **P4 BRENT routines** | Three cloud routines (Monday · Friday · EIA) → `demand_destruction/data/` + self-commit | Routine writes its run-stamp + the `TRACKER.md` alert-line block vintage it read | BRENT boot step 2b asserts newest routine output carries a run-stamp ≤ its schedule age and names the TRACKER vintage | **BRENT** | Known defect stays visible: the Friday routine fires before the ~15:30 COT post (`cot_grade.py` exit 3) — the leg must report that as FAIL `INPUT-NOT-PUBLISHED`, not PASS. |
| **P5 any other timer writing a Will-facing surface** | from the L496 register | per row | per row | **row owner** | A register row with `will_facing = yes` and no `canary_path_id` is an open gap, reported by the register's own check. |

## 6. Verdict format (machine-read; tokens from `BLUEPRINTS/STATE_VOCABULARY.md`)

`CANARY <path_id> <class> PASS|FAIL|UNKNOWN key=<canary key> last_pass=<YYYY-MM-DD> reason=<DROPPED n|STALE|MISROUTED|INPUT-NOT-PUBLISHED|UNREADABLE>`

One line per class per path, then a summary `CANARY-RESULT v1 paths=<n> classes=<n> pass=<n> fail=<n> unknown=<n> uncovered=<n>`. rc 0 all PASS · rc 1 any FAIL · rc 2 any UNKNOWN (UNKNOWN never collapses into PASS — PAT-156/PAT-167).

## 7. Out of scope for v1 (named so it is not assumed covered)

- Whether a desk *reads* its inbox at boot (consumption) — that is each desk's boot protocol and BOARD_CONSUMPTION_SPEC, not this canary.
- Telegram delivery to Will (external channel; a canary there would message Will).
- PROME→BRENT / PROME→SAM coded MSG routes (MESSAGING/ has its own validator).

## 8. Order of work (proposal — owners date their own legs)

1. **WALTER P1** with the AC9 drill (the historical defect). 2. **LIQUID P3** run-stamp (also closes the "repair OWED" in LIQUID's 9/25 packet if it is still open — owner checks). 3. **BRENT P4**. 4. **WALTER P2**. 5. P5 rows as the L496 register fills. Each leg: acceptance file first → build → independent reader with its own counterexample → called fixed.

## 9. Review record

Plan read: one independent Sonnet cold reader on this spec and the L496 blueprint together, 2026-10-20 (single-artifact class, WQ-447). Ledger: §10 below, appended after the read. Fixes made: ❌ only; ⚠️ go to a declared residue block.

## 10. Reader findings and residue

**Plan read done** 2026-10-20 09:19 ET (one Sonnet coldreader, both docs; ledger saved verbatim at `runs/2026-10-20_L495_L496_PLAN_READ.md`, summarised here): **5 ❌ · 9 ⚠️**; all 14 cited pointers resolved; reader supplied two counterexamples of its own.

| Reader id | Grade | Disposition |
|---|---|---|
| 1 | ❌ AC6 vs AC1: canary both in the 7e worklist and inert, no mechanism | **FIXED** — AC6 names the mechanism (shared code path, then a `canary` output section; worklist/seen-set/doorbell built from the rest). |
| 2 | ❌ AC7 unimplementable: no `canary` field, dedup on `sha1(title)` | **FIXED** — AC7 lists the schema work on both P1 halves and a `canary:` key namespace. |
| 3 | ❌ count-only classes cannot carry an item canary; DEVELOPMENT needs entity + qualifier | **FIXED** — §2 Item class: `count-only` label, per-class recipe. |
| 4 | ❌ P1 owner WALTER vs seed "PROME / WALTER" vs "one desk" rule | **FIXED** — lane half PROME, consumer half WALTER; seed row owner = PROME (consumer named in its notes). |
| 5 | ❌ P3 run-stamp in gitignored `alerts/`; real consumer surface not the asserted one | **FIXED** — P3 declares host-local scope and a one-line laptop UNKNOWN; assertion site = the surface LIQUID names. |
| counterexample A | owner branch real desks never take | **FIXED** — new AC10 (same dispatch map, chained to P2). |
| 6 | ⚠️ "latest expected run" undefined over weekends / DST / `Persistent=true` catch-up | RESIDUE — each leg's acceptance file defines its expected-run function; the L496 `schedule` cell is its input. |
| 7 | ⚠️ AC8 canary in or out of `by_class` | **FIXED** in AC8 (counted, subtracted explicitly). |
| 8 | ⚠️ P4 Friday leg permanently red trains override | RESIDUE — a KNOWN-FAIL-with-expiry state would be a new token; it needs `STATE_VOCABULARY.md` registration first. Until then the leg reports FAIL and the defect stays visible (preferred over a silent waiver). |
| 9 | ⚠️ P2 test inbox cannot exercise addressing / wrong-owner | RESIDUE — P2 is write-path only in v1 (already stated); AC10 makes the test desk a real map entry, which narrows it. |
| 10 | ⚠️ R1 30 days unbased | Disclosed as a proposal in L496 §4. |
| 11 | ⚠️ R3 compensating session has no column | **FIXED** in L496 §4 R3 (carried in the `lag_verdict` cell). |
| 12 | ⚠️ Friday schedule cites a secondary | RESIDUE — seed cell already says "confirm at source"; BRENT owns it. |
| 13 | ⚠️ no latency bound if WALTER does not boot | RESIDUE — that is the dark-desk class (WQ-295 / dark_window_check, L596), not this canary; named so it is not assumed covered. |
| 14 | ⚠️ header claimed the read before the record | **FIXED** — this section is the record. |
| counterexample B | laptop UNKNOWN normalised into override | Partly addressed by the one-line-per-session form in P3; residue otherwise. |

No result read has been run on these fixes (WQ-178: a result read is owed before the spec is called final; it is the owners' first leg reader or PROME's consumer read, whichever comes first).
