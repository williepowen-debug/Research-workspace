# OSPREY — self-audit improvement slate

**Author:** OSPREY · **Date:** 2026-08-10 (post-forum, post-cleanup) · **Task:** PROME, Will-directed
**Method:** read the whole tree — 32 tracked files outside `processed/`, all ledgers, thesis surfaces, outbox, domain files. Staleness measured from **content-derived dates or in-file marks**, never mtime (`finding_mtime_is_corrupted_by_git_sync`). Every item below was found by reading, not recalled.
**Status: PROPOSALS ONLY. Nothing here is executed.** Classification: **SELF** = inside `DELEGATION_TIER` (own dir, reversible, no capital, falsifier not weakened, not a data-property question) · **WILL** = fails at least one test · **CROSS** = needs another desk.

> **Deliberately NOT re-listed** (already on PROME's ledger): the §2 days-since-re-arm counter · the TD6 retrievable-feed fix · the four forum candidates (band re-centre, OSP-05 3a/3b, Channel-2/3 downgrade case, TD6 registration) · EXIT RULES §3's attribution clause.
> **Checked and found HEALTHY, recorded so nobody re-audits it:** `domain/war-risk/BLACK_SEA_WAR_RISK.md` carries a correct, dated superseded-banner pointing at `workbook/WARRISK.tsv` with an explicit "if the two disagree, the TSV wins." That migration was done properly and needs nothing.

---

## THE SLATE — ranked by value

### 1. 🔴 `STRIKES.tsv` is 10 days stale and is missing the heaviest week of the entire campaign — SELF · ~1 session
**Evidence:** header `swept-complete through: 2026-07-31`; newest row `Date` = **2026-07-31**; today is 8/10. **I personally sourced six named refinery strikes in that gap today and did not row any of them** (watch-only forum, then a cleanup scope that excluded a ledger sweep): Ufa/Bashneft-Novoil **8/5** · Yaroslavl/Slavneft-YANOS **8/6** (top-5 nationally) · Ilsky + Syzran **8/8** · Saratov **8/9** · **Taneco/Nizhnekamsk 8/10 — 13 killed, 75 wounded, the deadliest single event of the campaign.**
**What it catches:** the ledger is the evidence base under every channel score, the band, and OSP-05. Right now it **understates the campaign at precisely its peak** — which is the HAW-15 failure mode (own-ledger baseline weaker than reality) in its third distinct recurrence. Anyone grading a channel off this file today gets a materially wrong picture.
**Also in scope:** regenerate the dated interpretation layer. Newest is `ANALYSIS_2026-07-23.md` — **18 days behind the raw ledger**, and CLAUDE.md closeout step 11 requires regeneration when patterns/aggregates materially change. They have: a 24-year-low runs print, a US-brokered de-escalation, and six strikes in six days.

### 2. 🔴 `NEXUS_BRIEF.md` is 10 days stale, carries a claim I RETRACTED, and it demonstrably propagated — SELF · ~30 min
**Evidence:** file last written **2026-07-31**. DAEDALUS flagged on 8/7 that the **withdrawn war-risk ask still lives in it** and the pinned STATUS hash is stale. HAWK and NEXUS read this brief **at their boot**.
**What it catches — and this is not hypothetical, it happened today:** HAWK's Phase-1 forum post carried my *"the Black Sea leg is structurally unobservable"* claim — **which I withdrew on 7/31, in the same session I raised it.** I had to correct it twice in the forum, and HAWK corrected it in its own §4d. **The brief is the read-path that let a retracted claim survive ten days and reach a cross-war synthesis.** A retraction that doesn't reach the brief doesn't exist.
**Fix:** rewrite the brief; adopt NEXUS's own process fix (fold the brief as the **last** closeout step, so it can never lag STATUS again).

### 3. 🔴 The channel scores are a RATCHET — there is no downgrade path, only "up" or "dead" — WILL · ~1 session to design
**Evidence:** the STATUS dashboard's columns are `Score | Current State | Independence | Key Signal | **Upgrade Trigger** | Last Updated`. **There is no downgrade-trigger column and no downgrade rule anywhere in `CLAUDE.md`.** The only downward path is the §1 **channel-kill**, which is binary (alive → dormant) and demands **30/30/21 days of total quiet**. So a channel can move **3 → 4** on a trigger and has **no specified route from 4 → 3**.
**What it catches:** *every de-escalation, structurally.* This is FALCON's DOWN-direction defect (which it fixed in the codification axis) sitting unexamined in my primary instrument — and it is **live right now**: the 8/8 US-brokered understanding is a genuine, material de-escalation in Channels 2 and 3, and **my dashboard cannot express it at all** short of a full kill that is 30 days away at best. I carried all three marks unchanged today partly because I had no legitimate way to mark them down.
**Why WILL, not SELF:** adding a downgrade path makes my thesis easier to retire — good direction — but it changes what a *score* means for BRENT and HAWK, who consume the scores. That is an instrument-semantics change with external consumers, not a local repair.

### 4. 🟠 The recoverable-share question BRENT needs is instrumentable — the column already exists and is 95% empty — SELF · ~1 session
**Evidence:** `STRIKES.tsv` has a **`ReturnToService`** column. Of **58 rows, 50 are `unk`/empty**. Of the 8 "populated," three are `n/a` (tankers/gas) and two are stale states (`unk (pending assessment)`, `NOT resumed as of 7/31`). **Genuinely usable outage-duration data exists on 3 rows — about 5%.** Meanwhile the `Status` column captures *instantaneous* condition (`hit` ×15, `fire` ×8, `offline` ×8, `reduced` ×6) — i.e. **the ledger records what happened at the moment of the strike and almost never records how long it lasted.**
**What it catches:** the single caveat I flagged as *"the one place this document could cost real money"* — **runs-decline is not capacity-offline, and the recoverable share is unquantified.** That gap is not inherent; it is an unpopulated field. A back-fill pass on the ~15 largest named facilities converts my headline number from a proxy into something with a duration distribution behind it, which is exactly what a crack-spread sizing needs.
**Honest limit:** many outages genuinely have no published return-to-service date. The deliverable is a **populated-or-explicitly-unavailable** column, not a fabricated one — and the count of "genuinely unpublished" is itself the finding.

### 5. 🟠 OSP-04 auto-CONFIRMS if I never look — the prediction rewards my own neglect — WILL · ~15 min to re-spec
**Evidence:** OSP-04 (registered 7/31, 60%, closes 8/31): *"the two slow aggregates (floating storage; Urals discount) are **NOT refreshed** with a post-July-2026 independent print by 8/31."* Resolution requires establishing a **negative** — that no such print exists.
**What it catches:** a structural incentive defect, and a new one. **If I simply do not search, the aggregates stay dark and I book a CONFIRMED.** The prediction pays me for not doing the work it is nominally monitoring. This is the *"nobody published vs nobody looked"* distinction — the exact problem `WARRISK.tsv`'s two-clock header exists to solve — sitting inside a scored calibration row with no such guard.
**Fix shape:** require a **dated search attempt** as a resolution precondition (an attempt clock on the prediction itself), so CONFIRMED means "I looked and there was nothing," never "I didn't look." Post-R3, this is the second open row whose *instrument* is weaker than its *claim* — which suggests a registration-time question rather than two patches: **"what evidence would resolve this, and can I actually produce it?"**

### 6. 🟠 `VX.tsv` and `FLOW.tsv` have no content-derived vintage at all — SELF · ~20 min
**Evidence:** grepped all five ledgers for a two-clock header (`Last real data refresh` / `Last re-pull ATTEMPTED`). **`WARRISK.tsv`: yes. `VX.tsv`, `FLOW.tsv`, `KB.tsv`, `PREDICTIONS.tsv`, `STRIKES.tsv`: zero.** VX rows carry self-stamps *inside the cell* (`[Jul31 REFRESH — 19d stale]`) — which no script can read — so `ledger_staleness.py` grades these files on **git-commit time**, which my own auto-memory says fails **false-negative**, and which today's hygiene commits have just re-armed (`finding_hygiene_commit_rearms_the_staleness_lie`).
**What it catches:** the surface that told me on 7/31 it was already 19 days stale is now **29 days stale and will grade `ok` at boot tomorrow** because the file was committed today.
**Scope note:** not all five need it. `KB.tsv` is append-only (a row's date is its vintage) and `STRIKES.tsv` has its `swept-complete through` mark — though ⚠️ **that mark is an ATTEMPT clock with no data clock**, which is why item 1 was invisible. **`VX.tsv` and `FLOW.tsv` are the two genuinely unclocked surfaces.**

### 7. 🟠 A Russian counter-campaign against Ukraine's export corridor has NO channel — WILL/CROSS · ~1 session
**Evidence:** the three channels are, by construction, **Ukraine → Russia** (refineries · crude-export terminals · shadow-fleet tankers). When Russia sank the **Golden Leo** (grain ship, Ukrainian corridor, 10 killed, 7/26), I had to row it as `war-risk(non-oil)` and score it **as a war-risk input only, in no channel** — and I wrote at the time that both HAWK and FALCON had mis-routed it *because the framing had no slot for it.* `VX-HAWK-SHADOW-02` now says in its own text that *"confrontation is now TWO-WAY, which this row's framing did not represent."*
**What it catches:** a sustained Russian closure of Ukraine's export corridor is **invisible to my dashboard** — it would produce no channel movement whatever its size. Same gap archetype as the 8/8 de-escalation: a real, plausible, market-relevant event class with no row shape. **Two further un-slotted classes found in the same pass, listed so the taxonomy question gets asked once:** (a) **ownership/control change at a tracked asset** — the 8/8 understanding exists *because* CPC's shareholders are Chevron/Exxon/Shell, yet nothing in my instrument set tracks corporate control, so a Chevron exit or a forced Lukoil divestment would change my attribution logic invisibly; (b) **sanctions relief** — which would unwind the shadow fleet and the Urals discount together, and has no slot either.
**Why CROSS:** the corridor and the enforcement legs touch HAWK's lane; the taxonomy fix should be agreed, not declared unilaterally.

### 8. 🟡 Dead-letter and reference rot — three small surfaces, one bundle — SELF · ~30 min total
**Evidence, measured:**
- **`outbox/` holds 8 files dating to 7/21; `outbox/delivered/` contains only `.gitkeep` — nothing has EVER been moved there since spinout.** The 7/21–7/24 CPC packets were consumed and acted on weeks ago. The protocol in `CLAUDE.md` names `outbox/delivered/` and it has never been used once.
- **`SOURCES.md` last touched 2026-07-12** — 29 days, and **it predates every sourcing lesson I have learned.** It does not carry the 8-outlet war-risk set (built 7/31), the named Black Sea broker voice, the TD6 proxy, or today's finding that Baltic's primary is CDN-blocked. It is the file a cold-boot would trust for "where do I look," and it is the least current file in the tree.
- **`MEMORY.md` last touched 2026-07-16** — 25 days, so it predates LESSONS item 5 (registered-gate attention capture) and everything since.
**What it catches:** low individual value, but these are the three surfaces a *future* OSPREY reads when it does not already know the answer — and all three currently teach a 3-to-4-week-old version of this desk.

---

## Cross-cutting observation, offered as the reason several of these rhyme

**Five of the eight items above are the same shape: an instrument that records STATE but not DURATION, or an ATTEMPT but not a RESULT.** `ReturnToService` empty while `Status` is full (#4). `swept-complete through` as an attempt mark with no data clock (#1, #6). OSP-04 resolvable by not-looking (#5). Channel scores that record arrival at a level but not departure from it (#3). The `WARRISK.tsv` two-clock header — which proved itself today by correctly refusing to advance while I logged that I had searched — is the one place I got this right, and it was built only *after* the failure. **The generalisable ask for Will: should the two-clock split be a registration-time requirement for any OSPREY surface, rather than a repair applied after each surface rots?**

---

## Summary table

| # | Item | Class | Cost | Catches |
|---|---|---|---|---|
| 1 | `STRIKES.tsv` 10d stale, missing 6 strikes incl. the campaign's deadliest | SELF | ~1 session | Evidence base understates the campaign at its peak |
| 2 | `NEXUS_BRIEF.md` stale + carries a retracted claim that propagated to HAWK | SELF | ~30 min | Retractions not reaching consumers who boot off the brief |
| 3 | Channel scores are a ratchet — no downgrade path | WILL | ~1 session | Every de-escalation, structurally — including 8/8, live now |
| 4 | `ReturnToService` 95% empty — the recoverable-share instrument | SELF | ~1 session | The runs-vs-capacity caveat that gates crack sizing |
| 5 | OSP-04 auto-confirms on my own inaction | WILL | ~15 min | A calibration record inflated by neglect |
| 6 | `VX.tsv` + `FLOW.tsv` unclocked, graded on git time | SELF | ~20 min | A 29-day-stale surface grading `ok` tomorrow |
| 7 | No channel for a Russian counter-campaign (+ ownership, sanctions relief) | WILL/CROSS | ~1 session | Whole event classes moving no instrument |
| 8 | `outbox/delivered` never used · `SOURCES.md` 29d · `MEMORY.md` 25d | SELF | ~30 min | What a future OSPREY trusts when it doesn't know |

*— OSPREY, 2026-08-10. Proposals only; nothing executed. SELF items are inside the delegation tier but are NOT self-approved here — they are offered for Will to pick from, per the task.*
