# Falsification Freshness Sweep — RUN #1 (first registered run) · 2026-08-03

**Sweep:** #3, `sweeps/FALSIFICATION_SWEEP.md` · **Registered** 2026-07-12 · **Cadence** 21d · **Ran** 23d after the 7/11 pilot (**+2d over cadence**)
**Run by:** DAEDALUS solo. **Method deviation, declared:** the playbook prescribes a Mode-A Sonnet reader fan-out (one reader per 3-4 agents). This session's rules bar spawning subagents, so detection was **mechanized instead of fanned out** — a new instrument, `scripts/falsification_scan.py`, then a judgment read of every flag. Same discipline as the 7/30 FORGE audit.
**Mutations:** none. Detection is read-only; all dispositions are packet-only per the playbook (re-scoping kill criteria is domain judgment, and the dormant-freeze pre-approval does **not** extend to this sweep).

---

## BOTTOM LINE

**9 surfaces STALE-FLAGGED across 3 agents, 1 UNSTAMPED, and 4 flags withdrawn on inspection.** The pilot's 4/4 rot rate did not repeat at that intensity — but the two agents it named, **HENRY and LIQUID, are both flagged again on the same surfaces 23 days later**, which is the more useful result: it says the pilot fixed instances and the decay process is still unowned, exactly the gap this sweep was registered to close.

**The sharpest finding is inward and structural: 5 agents carry a live thesis with no separate falsification surface at all — AEOLUS, MIDAS, OSPREY, VULCAN, WATT — and all five are DAEDALUS builds from 2026-07-10 to 07-22.** One cause, n=5: my blueprint ships a thesis and a predictions ledger but never *requires* a kill/exit rail as its own surface. A rail embedded in STATUS prose is invisible to this sweep and to every other surface-level check, which means the newest fifth of the fleet is structurally unfalsifiable-by-inspection. That is a build-standard defect, not five agent defects.

**The instrument found four defects in itself before it found anything in the fleet** — all one family (*which date belongs to the surface?*), all caught by verifying verdicts rather than reading them. Details in §4; it is the reason the flag count moved 13 → 8 → 9 across three runs.

---

## 1 · Coverage — what was searched, and what was NOT

| | N |
|---|---:|
| Falsification surfaces searched | **32** across 19 agents |
| Agents in FLEET_DIRECTORY | 39 |
| STALE-FLAGGED (verified) | **9** |
| UNSTAMPED (cannot be judged fresh) | 1 |
| CURRENT | 15 |
| FROZEN-OK (dead-bannered = correct) | 5 |
| EVENT-LOG (age measures the world, not the surface) | 1 |
| DORMANT-SKIP | 1 |

**Declared coverage gaps — a zero here is a claim about the pattern set, not about the agent:**
- **Kill rails embedded in `STATUS.md` / `TRADE.md` sections are NOT covered.** The pilot's own HENRY finding (a retired kill tree running unfrozen) and BROCK's §9 TRIGGER LADDER → STATUS EXIT RULES §5 migration are both this shape. A section inside a live, freshly-edited file cannot be dated by any file-level instrument — it needs the judgment read the playbook's profile-§3 inventory was meant to drive.
- **15 agents have no thesis-class file** (BARON, BROCK, DAEDALUS, DEWEY, HANS, HOMER, LABOR, NEXUS, ORACLE, PROME, RAV, SHADE, TERRY, YEYOU, ZHAO). Expected for utility/meta agents, but **BROCK, HOMER, LABOR, SHADE and ZHAO are market-class** — their thesis lives in STATUS by design. Not graded here; flagged as a scope question for the 8/5 Production Review.
- **`profiles/<AGENT>.md` §3 invalidation rows were not used as the inventory source** this run (the playbook's step 4). The mechanized pattern set replaced it. Those rows remain the right source for the embedded-rail class, and 11 profiles still carry Δ-banners.

---

## 2 · VERIFIED FINDINGS

### 🔴 F1 — REGINALD: 7 per-bank thesis surfaces, 105–125 days stale, and the ONLY unbannered layer of three

| Surface | Self-stamp | Age vs STATUS (7/30) |
|---|---|---:|
| `ZION/THESIS.md` | 2026-03-27 | 125d |
| `CFG/THESIS.md` | 2026-03-30 | 122d |
| `EGBN/THESIS.md` | 2026-04-06 | 115d |
| `MTB/THESIS.md` | 2026-04-15 | 106d |
| `FITB/THESIS.md` · `PNC/THESIS.md` · `RF/THESIS.md` | 2026-04-16 | 105d |

**Why this is a finding and not just old files:** REGINALD's banner discipline is *good on two of three layers and absent on the third.* `thesis/THESIS.md` leads with **"⚠️ STALE-VINTAGE — v1.4, 2026-04-16 … The LIVE thesis lives in `STATUS.md`. Do NOT cite anything below as current."** `workbook/THESIS_VALIDATION.md` leads with **"⚠️ ARCHIVED SNAPSHOT — criteria as of 2026-03-05; NOT maintained."** Both correct. **The seven per-bank children of that same bannered parent carry no banner at all** — they read as live entity theses, and `CFG/THESIS.md` still asserts `**Status:** VALIDATED`. This is PAT-068's shape: the mover bannered the parent and did not walk the derived surfaces.

**Disposition: owner packet. Two-state rule — banner or refresh, REGINALD's call which.** Not pre-approvable: these are entity theses, and choosing between FROZEN and a refresh is domain judgment.

**F1b (LOW, corrected mid-read):** `thesis/THESIS.md:543` points bank-level detail at **`OZK/THESIS.md` and `WAL/THESIS.md`, both of which no longer exist** — OZK revived as its own agent 7/22, WAL promoted out by `git mv` 7/25. **I nearly wrote this up as "the live thesis points at dead paths." It is not:** the pointing document is itself do-not-cite bannered, so the practical blast radius is near zero. Reported at LOW with the banner named, because *from the pointer alone a dangling-in-a-dead-doc and a dangling-in-a-live-doc look identical* — and the discriminator is one line up. Still worth fixing as promotion residue (PAT-066).

### 🟠 F2 — HENRY: the falsification layer is 38 days behind its own live thesis, and it was flagged in the pilot too

`workbook/THESIS_VALIDATION.md` self-stamps **"LIVE THESIS (as of 2026-06-23)"** and **"Reframed 2026-06-23"**; HENRY's STATUS reference clock is 2026-07-31 → **38d**. The file's own framing is what makes it a finding: it declares *"Canonical live thesis = STATUS.md; **this file is the falsification layer**."* A falsification layer 38 days behind the thesis it falsifies is decorative — it cannot invalidate a read it has never seen. Its confirm/invalidate criteria are still written against the 6/17 FOMC and the 6/22-23 AI-semi unwind.

**Recurrence, not a new instance:** HENRY was one of the pilot's 4/4 (7/11: retired kill tree unfrozen + HEN-35 at 2× live probability). Different surface, same agent, same class, 23 days on. **Disposition: owner packet.**

### 🟠 F3 — LIQUID: the pivot log has logged nothing for 39 days, and this is the pilot's own finding recurring

`thesis/CHANGELOG.md` newest **entry** is `### 2026-06-25 — Conviction re-marked 60 → 61`; version heading still `## v2.0 — 2026-05-19` → **39d** behind STATUS.

**Partial credit, stated precisely:** the pilot's 7/11 wording was *"CHANGELOG pivot log stopped 5/19."* That is now **out of date in LIQUID's favour** — a 6/25 entry exists. But the log has still recorded nothing for 39 days on an **L4-active** agent whose CHANGELOG exists specifically to log channel migration and conviction re-marks. **Disposition: owner packet** — is the log behind, or has nothing moved? Only LIQUID can say, and that is exactly why this is not pre-approvable.

### 🟡 F4 — HAWK: `workbook/EXIT_PROTOCOL.md` is UNSTAMPED, on the agent whose sunset is overdue

No parseable date in its header, so it **cannot be judged fresh** — and HAWK's `thesis/THESIS.md` is itself dead-bannered. HAWK's sunset adjudication was due ~8/1 and has not run. **No packet: this folds into the sunset decision** (my item, now overdue). If sunset is ruled, a FROZEN banner here is the sweep's *one* pre-approvable class (retired-but-unfrozen kill tree, mechanical + reversible, idle-verified). If HAWK stays live, the file needs a stamp and a re-scope from its owner. **Ruling either way must precede the banner** — freezing a rail on an agent that turns out to be live is the wrong-direction error this sweep is built to avoid.

### 🔴 F5 — MINE: 5 of the fleet's newest agents have no falsification surface at all

**AEOLUS · MIDAS · OSPREY · VULCAN · WATT** each carry a live thesis and **no** kill tree, exit protocol, or validation doc. Build dates: WATT/VULCAN/MIDAS 2026-07-10/11, OSPREY 2026-07-12, AEOLUS 2026-07-22 — **all five are DAEDALUS builds, and they are the five most recent.** FALCON, built in the same 7/12 split, *does* have `workbook/EXIT_PROTOCOL.md` — because FALCON **rewrote it itself** on 7/30, unprompted, after inheriting a March-vintage rail (its own header records carrying it "unrewritten for 18 days behind a reconciliation banner"). So the one sibling that has a rail has it despite the build, not because of it.

**Root cause is in my blueprint, not in five agents:** `BLUEPRINTS/market-agent.md` requires a thesis, a predictions ledger and exit rules *inside STATUS*, and never requires the falsification rail as **its own dated surface**. An exit rail living in STATUS prose is invisible to this sweep, to `ledger_staleness`, and to every file-level check — and it cannot be flagged as stale because STATUS is edited constantly. **This is the same corollary FALCON handed me on 7/30 and it has now cost twice: a maturity level says nothing about whether an agent can see its own domain, and it says nothing about whether an agent can be falsified either.**

**Disposition: blueprint change, queued for the next blueprint-maintenance block, plus a candidate ladder question for the 8/5 Production Review — should L3 require a dated falsification surface?** No owner packets: five agents did not each make a mistake.

---

## 3 · WITHDRAWN — 4 flags that did not survive the read

| Withdrawn | First verdict | Why it was wrong |
|---|---|---|
| `WALTER/filtered/kill_log.tsv` | STALE 106d | **349 rows, last dated 2026-08-02 (yesterday).** My scan read 18 header lines and took the log's *birth* date as its vintage. Live and healthy |
| `WALTER/registry/FALSIFICATION_FIRED_LOG.tsv` | STALE 60d | **An event log.** 3 rows, last fire 2026-06-04. Age measures whether triggers fired, not whether the surface rotted. Flagging it would punish a correctly-quiet ledger. *(Whether nothing SHOULD have fired in 60d is a real question — for RED/WALTER, not for this sweep)* |
| `CORAL/thesis/CHANGELOG.md` | STALE 44d | Newest **entry heading** is 2026-07-23 (Will-ratified leg upgrade), 11d. I had read the "Installed: 2026-06-20" header |
| `FALCON/thesis/CHANGELOG.md` | STALE 22d | Newest entry 2026-07-30 (v2.1 molecule-split), 4d. Its *first* heading is the inherited HAWK v1.0 entry — file is not reverse-chronological |

**Over-flag rate on pass 1: 4 of 13.** Same lesson as the 7/30 compound-gate screen, which also over-flagged 3 of 4 on its first pass: **a cheap structural screen is a false-positive generator until each flag is read in context, and the agents it wrongs first are the ones keeping the richest files.**

---

## 4 · THE INSTRUMENT AUDITED ITSELF — 5 defects, one family

New instrument: **`scripts/falsification_scan.py`** (mine; detection-only, keyed on in-content stamps, never mtime/git-time per PAT-039/PAT-044). Every defect below was found by **verifying its verdicts, including the CURRENT ones** — not by reading the code.

| # | Defect | Consequence | Fix |
|---|---|---|---|
| 1 | `max(date)` over a state doc's header | HENRY's 41d-stale validation doc graded **CURRENT/17d** off `June CPI (7/14)` — an *event date inside a confirm-criterion* | Prefer a **labelled** stamp (`as of`, `Reframed`, `Last Updated`…); fall back to loose dates only with an explicit ⚠ INFERRED mark |
| 2 | Header-only read of an append-only ledger | WALTER's live `kill_log.tsv` flagged at **106d** — its birth date read as its age | Append-only surfaces dated by **newest entry** |
| 3 | Event logs treated as maintained surfaces | WALTER's `FALSIFICATION_FIRED_LOG` flagged for not firing | New **EVENT-LOG** verdict class; age never a staleness signal |
| 4 | Whole-file `max(date)` on a changelog | Over-corrected #2 and **cleared LIQUID's real 39d flag** — prose inside an entry cites later events than the entry | Changelogs dated by newest **entry heading** |
| 5 | The reference thesis never checked for the defect being detected | REGINALD's children graded against **v1.4 — a `STALE-VINTAGE`-bannered parent**; a version match would have read as conformance | Dead-bannered thesis ⇒ assert **no** live version; STATUS is the only admissible clock |

**All five are one question — *which date belongs to the surface?* — and #4 is the one worth keeping:** fixing #2 correctly is what broke #4, i.e. **a fix aimed at a false negative created a false negative on the opposite surface class.** The generalization for `PATTERNS.tsv`: *a freshness rule is only valid for one surface KIND, and a scanner covering both kinds needs two rules and a way to tell them apart.*

**Design commitments kept in the instrument** (PAT-074 — audit a check by what its PASS means): UNSTAMPED is its own verdict and never CURRENT; the output always prints what it did **not** look at; the two zero-buckets are split, because *"has a thesis but no rail"* is a finding and *"no thesis"* is expected, and collapsing them is how F5 stays invisible.

---

## 5 · DISPOSITIONS

| # | Finding | Disposition | Routed |
|---|---|---|---|
| F1 | REGINALD ×7 per-bank theses unbannered | Owner packet — banner or refresh, owner's call | `AGENTS/REGINALD/inbox/` |
| F1b | 2 dangling pointers (OZK/WAL) in a bannered doc | Same packet, LOW, promotion residue | same |
| F2 | HENRY validation layer 38d | Owner packet — recurrence of a pilot finding | `AGENTS/HENRY/inbox/` |
| F3 | LIQUID pivot log 39d | Owner packet — behind, or nothing moved? | `AGENTS/LIQUID/inbox/` |
| F4 | HAWK EXIT_PROTOCOL unstamped | **Held** — folds into the overdue sunset adjudication; banner only AFTER the ruling | DAEDALUS next-actions |
| F5 | 5 builds with no falsification rail | **Blueprint change** + ladder question for 8/5 | blueprint-maintenance queue |
| — | 4 withdrawn flags | No action; recorded above so the withdrawal is auditable | — |

**Next run:** ~2026-08-24 (21d). **Carry into it:** the embedded-STATUS-rail class (needs the profile-§3 inventory this run did not use), F5's blueprint outcome, and whether F2/F3 closed — a third consecutive flag on the same two surfaces would stop being an agent finding and become an argument that a 21-day cadence is the wrong mechanism for this decay class.
