# HEARTBEAT 20th re-base: RETROSPECTIVE obligation census

**⛔ RETROSPECTIVE. This census was reconstructed on 2026-09-23 17:3x ET by `prome-da` (desktop), AFTER delivery.** It is not the READ_CAP rule 17–18 census the re-base owed before shipping, and it does not claim that census ran. The delivery is `dbaaa7230` (2026-09-22 09:37 ET). CATO's closure review (`AGENTS/CATO/runs/2026-09-21_2147_heartbeat-rebase-proposal-review.md` § September 23, H3) found no before/after census in its perimeter. This file answers that finding.

## Search for the original evidence (item 4, first leg)

| Sought | Where looked | Result |
|---|---|---|
| Original before/after obligation census | delivery + closeout commit messages; the plan `PROME/plans/2026-09-21_heartbeat-20th-rebase-PLAN.md`; the 9/22 HANDOFF entry; `PROME/reports/`; a filesystem-wide `find` on this machine (DESKTOP-BC6EF81) | **SEARCH-NOT-FOUND.** Not proof that none was made. |
| Plan-read ledger `…/618256cf-…/scratchpad/coldread_plan.md` | that exact path; every `/tmp/claude-1000/*/618256cf*`; the local transcript store (`~/.claude/projects/-home-willi-Research-workspace-PROME/`, no `618256cf*` transcript) | **SEARCH-NOT-FOUND on this machine.** The re-base session's machine is not recorded in the commit or ORCH_LOG, so the laptop's `/tmp` and transcript store are the one unchecked location. |
| Result-read ledger | same, and `rebase_result_review` in local transcripts (hits only in session `2dbc5918`, which QUOTES the ORCH_LOG rows and does not hold the reader's output) | **SEARCH-NOT-FOUND.** The surviving record is ORCH_LOG rows 257–258 (scores and fix summary only) and the plan's § RESULT-stage obligations (eight ⚠️ listed). |

⇒ **The limitation is retained.** The original readers' complete ledgers, model/blindness and per-finding dispositions are **UNKNOWN**. Nothing here stands in for them, and no clean historical verdict is claimed.

## Method (reproducible)

- Compared `git show dbaaa7230^:HEARTBEAT.md` (19th base + amendment #1, 32,315 B) with `git show dbaaa7230:HEARTBEAT.md` (20th base, 21,882 B).
- Extracted obligation-bearing identifiers (DOCKET `L###`, `WQ-###`, `GATE-*`, `KB-*`, `M/D` dates) and every kill-on-sight quote in the hot kill cell.
- Traced each item that dropped out of hot to its home **as of `dbaaa7230`**: the canonical owner record (DOCKET / WILL_QUEUE / GATES at that commit), the cold binding set (`§KOS`, `§KOS.2`, `§KOS.3`), or other cold text.

⚠️ **Limits of the method:** it is identifier- and quote-level. **A duty stated in prose with no identifier and no quoted kill phrase is not covered.** Examples are an owed re-measure or a "next read" sentence. Absence of a finding in that class is **not** verified. Counts are from this session's scripts (scratchpad), not hand-counted.

## Results

| Class | Before | After | Dropped from hot | Disposition of each dropped item (at `dbaaa7230`) |
|---|---|---|---|---|
| DOCKET rows | 19 | 8 | 11 | **L222 L345 L380 L409 L421 L429 L432 L448: PENDING rows in `PROME/DOCKET.tsv`**, the canonical calendar, surfaced on PROME's boot path by the generated SCRATCH view. Carried by the owner record. **L34 L411 L424: RESOLVED** before delivery (discharged). |
| WILL_QUEUE | 11 | 9 | 3 | **WQ-157, WQ-261: OPEN** in `WILL_QUEUE.md` (boot-generated view). Carried. **WQ-224:** RECENTLY DONE (discharged). HEARTBEAT's own rule forbids carrying Will's open list. |
| GATES | 7 | 7 | 1 | **GATE-BRENT-COT-35B:** LIVE row in `GATES.tsv`. Carried. |
| Dates | 17 | 20 | 1 (9/15) | Both 9/15 items are carried: COT vintage #6 by the GATES row; the 9/15 20Y I′ fire by the hot kill cell entry *"the 20Y I′ fire killed the thesis"* [pairs ~early Oct]. |
| Hot kill-cell entries | 21 | 15 | **8 dropped, 2 added (net −6)** — corrected on ARGUS ❌: the first draft reported the net as the drop count | Five (Suwałki 9,000 · 22-year · $120bn · Kaliningrad/AWACS · SACEUR chain) are in **cold §KOS.3**. *"the call wall is 7,700"* and *"ANY Brent November level dated 9/18"* were **RETIRED BY NAME** in the 20th base's ⚑ line (the first with a successor kill, the second superseded by the publishable $103.87 settle). ⚠️ This script's quote regex missed the second; ARGUS's `comm -23` caught it. **⛔ ONE LOST: *"Brent fell 7.5% in three sessions"*** was not kept, moved or retired. It survived only in rotated amendment text (§A21, not in the binding set). |
| Other quoted phrases outside the kill cell | 7 | — | 7 | *"FUNCTIONALLY SUPERSEDED"* and *"a large part of why"* are in cold §19.7/§20.7. *"chain >~5 amendments…"* is in cold §C. *"chain at 3, amendment #4 BARRED"* is a retired PROME reason, moot at chain 0. *"no 9/18 bar was published"* is a retired amendment-#3 claim; its substance survives in the hot kill entry for MOVE 76.22 / ^SKEW 145.70 and in §2R. *"supersedes holdings assumptions below"* quotes the 9/16 capture header; the obligation is carried by DOCKET L448 + WQ-274. The last three survive verbatim only in the archived 19th-base snapshot. |

## Repair made from this census (2026-09-23, same commit as this file)

The one lost binding entry was **re-homed** to a new cold `§KOS.4`, carrying **the 19th base's binding hot text verbatim**: PROME publishes NO replacement percentage, because any fade back-solves a killed 9/18 level. ⛔ **Corrected the same day:** the first re-home carried the older §A21 wording, which publishes −4.48% / −5.20% against $103.10, a killed level. That inverted the binding caveat. The independent reader `hbcorrread` caught it (X1), and it was fixed before commit. `HEARTBEAT.md`'s two binding-set pointers now name `§KOS.4`. Nothing was retired, regraded or refreshed.

## Status

- **Census:** RETROSPECTIVE, identifier/quote level, one loss found and re-homed.
- **Original census and reader ledgers:** UNKNOWN / unavailable on this machine. The laptop is the only unchecked location.
- **Prose-only duties:** not covered by this method.
