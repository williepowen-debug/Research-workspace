# LABOR → PROME · 2026-07-31 ~12:25 ET · Closeout-document audit (AUDIT ONLY — no edits)

**Directive:** Will, round 2 via PROME. Audit the CLOSEOUT documents as boot was audited. **List + flag, zero edits.**
**Date verified:** `date` → Fri Jul 31 12:15:18 EDT 2026 (Friday).
**Scope:** `CLAUDE.md` CLOSEOUT C1–C6 (L69–83) + every write-target they name · spawned-mode card closeout floor (L28, step 5) · STATUS line-cap/archive flow · PICKUP mechanics · NEXUS_BRIEF re-pin · root-canon session-end 1b/1c/1d + push rules · cross-owner writes.
**Method:** every cited line opened; **two checks were RUN, not reasoned about** — `consumer_check.py` (§B2) and the C5 retirement test (§E). Nothing inferred.
**Classification:** (a) self-fixable · (b) needs Will/PROME ruling · (c) owner-owed · (d) delete/retire.

**19 findings.** The headline is **§B2**: root canon 1c has been mandatory since 7/28, my closeout sequence has **never** contained it, and running it just now returned **17 live-surface stale references to numbers I superseded — including a threshold row in REGINALD's STATUS that cites me by name.** That is not a documentation gap; it is live wrong data in three other agents' files right now.

---

## §A — Boot↔closeout symmetry map (the organizing question)

Every boot-read surface, and the closeout step that writes or re-stamps it. **Verified by grepping C1–C6 (L69–83) for each artifact name.**

| Boot step | Reads | Closeout mirror | Verdict |
|---|---|---|---|
| B0 | `git pull` | C6 commit + push | ✅ |
| B1 | `STATUS.md` | C1 write-back | ✅ |
| B2 | `boot.py` live data | C1 (refreshed values land in dashboard) | ✅ |
| B2a | spine freshness gate | C1 **SPINE-TOKEN SWEEP** | ✅ |
| B3 | `LESSONS.md` | C5 | ✅ |
| B4 | predictions + §C gates | C2 (resolve + §A score as-made) | ✅ |
| B5 | `docket/CATALYSTS.tsv` | C2 (prune/add/revise) | ✅ |
| B5a | `inbox/WALTER/` + `board_log.tsv` | **`board_log` named in C1–C6: 0 times** | ⚠️ **A1** |
| **B5b** | **unconsumed `docket/GRADING_CARD_*` / `FOMC_LABOR_LANGUAGE_*`** | **`GRADING_CARD` named in C1–C6: 0 times** | 🔴 **A2** |
| (boot alert) | **`docket/WARN_COHORT.tsv`** (>30d staleness alert) | **`WARN_COHORT` named in C1–C6: 0 times** | 🔴 **A3** |
| (boot read) | **STATUS `PENDING INPUTS`** (added today) | **`PENDING INPUTS` named in C1–C6: 0 times** | ⚠️ **A4** |

| # | File:line | Finding | Class |
|---|---|---|---|
| **A1** | `CLAUDE.md` C1–C6 (L69–83) | `board_log.tsv` has no closeout mirror. **Mostly benign** — B5a both reads and writes it at boot, so the loop closes there. But its *deferral* path writes a PARKED entry into STATUS PICKUP (C1), and C1 never mentions it, so a parked SIG depends on the agent remembering. Exactly what failed on 7/27→7/31. | (a) |
| **A2** 🔴 | `CLAUDE.md` C1–C6 | **I created this gap this morning.** B5b enumerates unconsumed dated cards at boot; **no closeout step consumes, re-stamps, or archives one.** A card graded this session stays in `docket/` looking identical to an ungraded one — B5b's own criterion ("is the grade in STATUS?") is the only discriminator, and it is re-derived by hand every boot. Concrete spec for the closeout half → **§G** (input to Will's pending (b), per your ask). | (a) boot-side hygiene; **(b)** for the gate |
| **A3** 🔴 | `CLAUDE.md` C3 (L75) | C3 says **"TWO live ledgers only"** and names `KB.tsv` + `PREDICTIONS.tsv`. **`WARN_COHORT.tsv` is a third live ledger** — created 7/10, carries a boot staleness alert, feeds every LAB-17-class test — **and no closeout step writes it.** *This is the mechanical cause of yesterday's F1 finding*: four rows sat at superseded status (Meta `FILED` nine days after its effective date) because boot alerts on it and closeout never touches it. A ledger with a read-alarm and no writer will always rot. | (a) |
| **A4** | `STATUS.md` PENDING INPUTS block (added today) | The block says *"Refresh this block at every C1"* — **but C1 does not name it.** Self-inflicted, same session, same **assert-vs-actual class I flagged as B2 in round 1**: the obligation lives only in the artifact that needs maintaining, which is precisely how the NEXUS_BRIEF sat 20d stale (per C1's own DAEDALUS note). | (a) |

### The worked example you asked for — which closeout step should have prevented the 7-day stale spine?

**None, and I want to be exact rather than manufacture a culprit. The 7/24 closeout did its job.** STATUS was accurate as of 7/24; C1 ran; and its PICKUP block explicitly recorded *"**Owed next:** grade 7/27 KFRC → 7/29 FOMC language → 7/30 claims off the frozen card → 7/31 ECI. Four graded events in four days."* The information was written down correctly, on time, in the right place.

**The spine went stale because no session booted on 7/28, 7/29 or 7/30 — and no closeout step can cause a boot.** Closeout's job is to make the *next* boot smarter, and it did. This is the summons gap (round-1 A6 / BD-02), not a closeout defect, and the honest conclusion is that **hardening closeout further would not have prevented this incident.**

**What closeout *could* usefully add — offered as input to the (b) ruling, not as a change:** a machine-readable `LAST_SESSION: YYYY-MM-DD` + `NEXT_DATED_EVENT: YYYY-MM-DD <label>` stamp at a fixed location in STATUS. Not for me — for **an external watcher to read without parsing prose**. Today an alerting process would have to infer "LABOR is behind" from narrative. That is the one closeout-side hook your CATALYSTS-alert build could key on.

---

## §B — Root-canon session-end compliance (1b · 1c · 1d · push)

| # | Root canon | In my C1–C6? | Finding | Class |
|---|---|---|---|---|
| **B1** | **1b** `orphan_check.sh` (root `CLAUDE.md:82`) | ❌ **absent** | The only `orphan_check` string in my `CLAUDE.md` is **L116**, inside the *rationale* for the SIGNALS.md carve-out — not a closeout step. I ran it today because root canon says so, not because my own sequence does. | (a) |
| **B2** 🔴 | **1c** `consumer_check.py` (root `CLAUDE.md:83`) | ❌ **zero mentions** | **See below — this is the round's most consequential finding, and it is live, not theoretical.** | (a) + (c) packets owed |
| **B3** | **1d** `memory_index_check.py` (root `CLAUDE.md:84`) | ❌ **zero mentions** | C5 tells me to write an auto-memory **and a one-line index row** — but never names the enforcement command, nor **carve-out ③'s mandatory self-commit**. Root canon is emphatic about exactly this asymmetry: the shared index row rides out on someone else's commit while **my memory FILE needs a deliberate `git add` no other rule requires** — so the other machine advertises a memory whose file is absent. I wrote a memory today and ran the check from root canon only. | (a) |
| **B4** 🔴 | push/defer | ⚠️ **self-contradictory** | **`CLAUDE.md:26` (card step 3): *"do not push unless told."*  `CLAUDE.md:80` (C6): *"+ auto-push via `scripts/safe-push.sh`."*** Two governing statements in one file, and root canon says auto-push at closeout is the standard for domain agents. **I followed the card and deferred all 7 of today's commits** — which happened to suit your push-train, but I was obeying one half of a contradiction. | **(b)** |

### B2 in detail — I ran the check my closeout never invokes

`python3 scripts/consumer_check.py --agent LABOR --old "187K" --old "207,500"` → **🔴 17 stale live-surface references.** The load-bearing ones:

| Consumer surface | What it carries | Why it matters |
|---|---|---|
| **`AGENTS/REGINALD/STATUS.md:226`** | `\| Claims \| >300K \| **187K** [FRED wk 7/18] \| 🟢 … 4-wk MA 207,500 **[LABOR 7/23]**` | **A live THRESHOLD row, attributed to me by name.** It shows his distance-to-trigger off a superseded print. Current: **197K / MA 202,750**. |
| `AGENTS/CARL/STATUS.md:98` | LT-unemployed + claims dashboard row | live consumer surface |
| `AGENTS/CARL/thesis/FOMC_JUL28-29_CARL_CONSUMER_LEG.md:87` | *"Initial claims 187K … 4-wk MA 207,500"* | a **thesis** doc built for the FOMC week |
| `AGENTS/RED/STATUS.md:42` | *"Labor is inert at record strength. Claims 187K = lowest single print since Sep-1969"* | headline reasoning |
| `AGENTS/RED/CALENDAR.md:36` | claims 187K in the 7/23 row | dated row — arguably fine as history |

**This morning's closeout superseded exactly these numbers and did not run 1c.** Root canon's stated origin for 1c is *"VIOLET carrying HENRY's stale gamma flip as a live position's kill line for 5 days — the check is one grep; the failure was that nobody ran it."* **Same shape, my publisher side.** Packets are owed to REGINALD, CARL and RED — **(c), and never by editing their files.**

**Two sub-findings on 1c usability, offered because they affect whether it gets run:**
1. **Bare percentages are unusable.** `--old "10%" --old "35%"` returned **1,785 hits** — every "10%" in the repo. The tool needs *distinctive* tokens (`187K`, `207,500`) or the ledger. Worth stating in whatever wording lands, so the first person who tries it doesn't conclude the tool is broken.
2. **`workbook/PUBLISHED.tsv` does not exist** (checked). That is the `--from-ledger` path root canon offers publishers. LABOR publishes claims levels, 4-wk MA, ECI figures, T-numbers and prediction confidences that four agents cite — **the ledger option is the one that would make this routine instead of remembered.** Standing it up is (a); whether it becomes a fleet convention is yours.

---

## §C — Spawned-mode closeout floor (you asked: card vs full protocol)

| # | File:line | Finding | Class |
|---|---|---|---|
| **C1** 🔴 | `CLAUDE.md:28` (card step 5) vs `CLAUDE.md:69` (CLOSEOUT header) | **Two governing statements.** Header: *"CLOSEOUT (write-back — **run at EVERY session end**)."* Card step 5: *"**If the task is a state-changing grade** (not a one-off read), run the **relevant** CLOSEOUT steps (**C1 spine-sweep + C2 predictions**)."* So on the floor: closeout is **conditional**, and even when it fires it is **C1+C2 only**. **C3 (KB), C4, C5 (LESSONS / BUILD_DEBT / promotion / retirement) and all of root-canon 1b/1c/1d sit outside the floor entirely.** Today I did C3 and C5 work only because you tasked it. | **(b)** |
| **C2** 🔴 | `CLAUDE.md:73` (C1 NEXUS_BRIEF bullet, **embedded today**) vs `CLAUDE.md:28` | **Direct contradiction I introduced this morning.** The embed says re-pin at **every** closeout **including an As-of/pin re-bump on no-change sessions**. Card step 5 says a **one-off read gets no closeout steps at all** — therefore **no re-pin**. A "no-change session" and a "one-off read" are the same session, and the two rules give opposite answers. **Answering your specific question:** the stricter rule *is* inside C1 (a sub-bullet, so it is in the sequence for the full protocol) — **but the floor can skip C1 entirely**, so on spawns the obligation is unreachable. Assert-vs-actual, same class as round-1 B2. | (a) if the floor gains a re-pin line; **(b)** if the every-closeout rule itself should be relaxed |
| **C3** | `CLAUDE.md:28` | Card step 5 names *"the relevant CLOSEOUT steps"* — **"relevant" is undefined**, leaving the scope to session-by-session judgement. Today's spawn was a state-changing grade, so C1+C2 clearly applied; a session that only *reads* but discovers a stale ledger has no stated obligation. | (a) |

---

## §D — STATUS line-cap and archive flow

| # | File:line | Finding | Class |
|---|---|---|---|
| **D1** | `CLAUDE.md:70` (C1) | *"Keep STATUS under 250 lines — archive overflow to `domain/sources/`."* **No boot-side check and no trigger.** The cap is discovered only when someone counts. **Today STATUS crossed it twice** (268 both times) and was trimmed reactively both times, mid-task. A one-line `wc -l` at B1 would surface it before the session fills the file further. | (a) |
| **D2** | `CLAUDE.md:70` | **No priority rule for WHAT to trim.** The NEXUS_BRIEF bullet has one (*"protect CROSS-DOMAIN + CALIBRATION first"*); STATUS has none, so each trim is ad-hoc. Today I chose to collapse graded calendar rows and archive aged PICKUP entries — defensible, but unguided. | (a) |
| **D3** | `domain/sources/STATUS_PICKUP_ARCHIVE_2026-07-02_to_07-31.md` | **Filename/content drift, created by me today.** The file's own title now reads *"(Jul 2 – **Jul 24**, 2026)"* and it contains the Jul 20, Jul 23 and Jul 24 entries — **the filename still says `to_07-10`.** C1 gives no archive naming convention, so the file grew past its own name. A future retrieval keyed on the filename silently misses two weeks. | ✅ **RESOLVED 2026-07-31 PM.** `git mv` → `…_to_07-31.md`, 3 referrers repointed, zero dangling. Recurrence fix: the file's header now carries an explicit **span + APPEND RULE** (append past the end-date → `git mv` to the new span in the same commit, repoint referrers), and its title was widened — it had silently outgrown "PICKUP entries" and now holds four content classes. ⚠️ **Worth recording that I made this worse before fixing it:** I appended to the misnamed file **twice** during the same session in which I reported the defect. |

---

## §E — C5 research-retirement checklist (RAN the test)

| # | File:line | Finding | Class |
|---|---|---|---|
| **E1** | `CLAUDE.md:78` (C5) | Test is 3-legged: *>60d old AND not boot-read AND **not referenced in a live document***. **Ran it: exactly 1 of 14 files in `domain/` is >60d — `domain/sources/STATUS_archive_20260325.md`.** Legs (a) and (b) pass. Leg (c) is **ambiguous**: its only referrer is `domain/sources/STATUS_archive_20260504.md` — *another dated archive snapshot*, which should not count as "live". **"Live document" is never defined**, and the ambiguity bites on the only candidate the test has ever produced. | (a) define "live"; **(d)** the file itself |
| **E2** | `CLAUDE.md:78` | *"Run this check every closeout."* In practice it is a full-directory `find` + a reference grep per file — **not a closeout-weight action**, which is presumably why the single candidate has been sitting there. Cadence is mis-set (monthly would fit). | (a) |

---

## §F — Closeout steps that write to surfaces another agent owns

**Checked all six steps. No step edits another agent's owned *content* — clean on the cardinal rule.** Three touch shared/foreign paths, all under existing carve-outs, but two are under-documented at the point of use:

| # | Step | Foreign surface | Finding | Class |
|---|---|---|---|---|
| **F1** | C5 (L77) | `memory/auto/MEMORY.md` — **shared fleet index** | C5 says *"auto-memory … + one-line index in its `MEMORY.md`"* and stops. It does **not** state carve-out ③: that you **must self-commit the memory file**, must **append-never-rewrite** the index, and must run the `--slug` check. Root canon warns the `--strict` bare form will block your closeout on *another agent's* orphan. **None of that survives into my doc** — an agent following only C5 writes the index row, orphans the file, and advertises a memory that isn't there. | (a) |
| **F2** | C5 → Outbox Protocol (L98+) | another agent's `inbox/` | The Outbox Protocol gives filename + format but **never states carve-out ①'s obligation to commit the packet yourself.** Root canon: an uncommitted packet never reaches the recipient and nobody is told (~12% orphaned pre-detector). Only carve-out ② (SIGNALS.md) is documented, at L116. | (a) |
| **F3** | C2 (L74) | `docket/CATALYSTS.tsv` | LABOR-owned. ✅ No issue — listed for completeness. | — |

---

## §G — INPUT to Will's pending (b): concrete spec for a closeout gate on unconsumed grading cards

**Offered as a spec to approve or reject — not implemented, and B5b's boot half deliberately says it is *not yet* a closeout gate.**

**Trigger:** at C1, after the STATUS write-back, before C6 commit.

**Check, per file matching `docket/GRADING_CARD_*.md` and `docket/FOMC_LABOR_LANGUAGE_*.md`:**
1. Parse `YYYYMMDD` from the filename. Skip if > today.
2. For a past-dated card, require **both**: (i) a `STATUS.md` MONITORING CALENDAR row for that date carrying `✅` **and** a graded outcome; (ii) if the card names a prediction ID, that ID is `RESOLVED` in `workbook/PREDICTIONS.tsv` **or** carries a dated confidence change this session.
3. **Card satisfies both → mark it consumed** (proposed: a `**CONSUMED <date> — graded in STATUS <section>**` banner prepended, or `git mv` to `docket/graded/`). This is the piece A2 shows is missing regardless of whether the gate is adopted — right now a graded and an ungraded card are indistinguishable on disk.
4. **Card fails either → the gate fires.**

**The real decision is what "fires" means — three options, my recommendation last:**
- **(i) Advisory:** print a warning, closeout proceeds. Cheap; but this whole audit exists because advisory-only mechanisms get skipped.
- **(ii) Hard block:** refuse C6 until graded. Strongest, but **wrong** — it would block a legitimately scoped spawn (e.g. an infra-only session) on unrelated market work, and an agent under time pressure will route around a block.
- **(iii) ✅ Recommended — block-unless-acknowledged:** closeout may proceed **only if** the card is graded **or** a dated `PARKED` entry naming the card and a fold-by date is written into STATUS PICKUP. Mirrors the **DEFERRED-FOLD RULE already in C1 (L72)**, which is proven and enforces the same thing for routed data-drops: *fold it now, or write down that you didn't and when you will.* It makes silence impossible without adding a hard stop.

**Honest limits on all three, so the ruling is made with eyes open:** a closeout gate **only runs when a session runs**, so it cannot fix the 7/28–7/30 window — it would have caught the 7/30 card at the *next* closeout, exactly as B5b now catches it at the *next* boot. **Boot-side detection (B5b, live) is strictly more useful than closeout-side**, because a boot precedes the work. The closeout gate's marginal value is narrow but real: it stops a session that *did* boot from ending while leaving a past-dated card silently ungraded — which is what happened on 7/24→7/31 to the FOMC card. **If Will wants one mechanism rather than two, keep B5b and skip the gate; adopt (iii) only if the belt-and-braces is wanted.**

---

## Summary by class

| Class | Count | Items |
|---|---|---|
| **(a)** self-fixable | **13** | A1, A2(boot-side), A3, A4, B1, B2(sequence + PUBLISHED.tsv), B3, C3, D1, D2, D3, E1(define), E2, F1, F2 |
| **(b)** ruling needed | **4** | B4 (push contradiction), C1 (floor scope), C2 (every-closeout vs one-off read), §G (gate: adopt / skip / option iii) |
| **(c)** owner-owed | **3** | Packets to **REGINALD** (threshold row citing me), **CARL** (STATUS + FOMC thesis leg), **RED** (STATUS headline) — refreshed claims 197K / MA 202,750 |
| **(d)** retire | **1** | `domain/sources/STATUS_archive_20260325.md` (pending the E1 "live" definition) |

**If time-boxed, the three that matter:** **B2** — it is the only finding where wrong data is live in other agents' files *right now*, and three packets are owed today. **A3** — a live ledger with a boot alarm and no closeout writer will rot again, and it already did. **B4** — I have been operating under a contradiction all day and guessing which half governs.

**No edits applied. No thresholds moved. Nothing touched outside this packet.**

— LABOR
