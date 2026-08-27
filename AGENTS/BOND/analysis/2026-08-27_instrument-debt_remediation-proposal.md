# BOND — Instrument-Debt Remediation: proposal, not a work order

**Written:** 2026-08-27 end of day, at Will's ask ("what suggestions do you have for addressing what is not in good shape").
**Status:** PROPOSAL. Nothing here is executed. Items 1–3 are BOND's own to do once ruled/scheduled; item 4 is fleet-scope and is **not BOND's to impose**.
**Scope fence:** this is about the GUARD LAYER, not the thesis, not the book, not the position. No gate, threshold or score is proposed to move.

---

## 0. THE DIAGNOSIS — four defects, but not four unrelated bugs

Today surfaced four instruments that don't do what they claim, plus one class no instrument covers. Listed as symptoms they look like a backlog. **They are not: three of them share one shape.**

| # | Instrument | What it claims | What it actually did |
|---|---|---|---|
| 1 | `docket_check` | *"covers every scheduled coupon auction in the window"* (21d) | Covered whatever the feed returned — **horizon ~5d**, and today **rc=0 over ZERO coupon auctions** |
| 2 | `ledger_staleness --nudge` | *"N ledgers behind"* | Counted **STATUS-writes**, which on a 3-write day grew from **my own closeout cadence**, not from rot |
| 3 | `closeout_check` | `✅ CLEAN` | *"nothing of these shapes fired"* — **it says so itself**, and the 8/27 audit's 5 stale surfaces all passed it |
| 4 | `boot_recompute` rc msg | *"unguarded drift"* | Date-gate findings, **three lines under its own `✅ no unguarded drift`** (n=3, unpatched) |
| 5 | `watchers.py` | a date-gate tracker | **No way to mark a gate resolved except DELETING the row** |

> ### 🔑 THE SHARED SHAPE (1, 2, 3): **each reports a claim STRONGER than what it measured.**
> A check that examined an **empty or truncated reference set** returns the **same `rc=0`** as one that examined everything and found nothing. **"I looked at nothing and found nothing" is indistinguishable from "I looked at everything and it was fine."**
> `closeout_check` is the honourable exception *in its prose* — it prints its own scope caveat — but its **exit code still doesn't carry it**, and the exit code is what gets read under time pressure.

> ### 🔑 THE OTHER SHAPE (4, 5): **each trains the operator to ignore the instrument.**
> A tool that contradicts itself in adjacent lines, and a gate clearable **only by deletion**, both manufacture alarm fatigue. **Their cost is not their own noise — it is the credibility they drain from every OTHER finding the same tool emits.**

---

## 1. 🔴 FIRST, AND CHEAPEST: make `docket_check` unable to pass on an empty or truncated set

**Harm:** highest on the board. The **September refunding (~9/8–10) sits inside the claimed 21-day window and outside the ~5-day visible one**, and this is the tool's **own founding failure** — it exists because the August refunding ran ungraded, never docketed. **Cost:** a few lines.

**Proposed change (unruled):**
- Compute `feed_max = max(auctionDate)` over ALL rows returned (bills included — they establish the horizon even though they are not graded).
- **If `feed_max < horizon`: print the SHORTFALL explicitly and return a distinct code** (`rc=3` = COVERAGE SHORTFALL, or at minimum a `⚠️ COVERAGE` banner). Never `rc=0`.
- **If the coupon set is empty: say `examined 0 coupon auctions` in the verdict line itself**, not only in the counts line above it.
- Reword the pass line from *"covers every scheduled coupon auction in the window"* to **"no undocketed coupon auction among the N the feed can currently see (feed reaches YYYY-MM-DD)."**

**Fixture from today, per this desk's build discipline:** the live 8/27 response (4 rows, all bills, `feed_max` 2026-09-01, horizon 2026-09-17) — **an rc=0 that must become a non-pass.**

⛔ **What this does NOT fix:** the forward schedule still is not in TA_WS. **The tool cannot be made to see September; it can only be made to stop claiming it does.** Closing the real gap needs the QRA tentative-schedule PDF, which is a separate and larger build — **propose deferring it and relying on the recurring 9/3 docket row until the honest-reporting fix has run a cycle.**

## 2. 🟠 SECOND: fix the two credibility-drainers BEFORE adding any new check

**Sequencing is the actual proposal here, and it is the non-obvious part.** Items 4 and 5 are trivial code. **They should go first anyway**, because the new check proposed in §3 will emit findings into a channel the operator has already been trained to discount. **Adding signal to a channel that cries wolf is negative value.**

- **`boot_recompute` rc message:** date-gate findings get their own line and their own wording; stop calling them "unguarded drift" under a `✅ no unguarded drift` line. **n=3.**
- **`watchers.py`:** gate the **PASSED** branch on `Serviced_On`, as the CHECKPOINT-CROSSED branch already is. **Today the file's own affordance for recording work-done has no effect on the check** — so the only way to clear a gate is to destroy the record of it. `KB-BND-192`.

⚠️ **Do these as ONE small deliberate pass with its own verification — not at a closeout.** This desk's own rule is that *a correction pass is unreviewed work*, and today produced a live instance: my pathspec error (`KB-BND-201`) happened **during** a closeout.

**Coupling worth naming:** fixing `watchers.py` is what makes `BND-15`'s mitigation real. Right now that row's protection is *"it is written on three surfaces and a future session will read it"* — and the failure mode of that mitigation is precisely the class the 8/27 audit found (**a fix lands where the error was demonstrated; siblings rot**). A working date-gate is a mechanism; three prose warnings are a hope.

## 3. 🟠 THIRD, AND THE HIGHEST-VALUE NEW BUILD: a RELATIVE-VINTAGE check

**The gap:** the 8/27 audit found **5 stale surfaces and no check caught any of them.** The drift checker compares latest-on-surface to latest-at-source and **passes on a correct endpoint**; `assertion_check` has four shapes and **none is *"this cell is six days older than the cell beside it."*** An audit found them because an audit READS.

**Proposed shape — and it is implementable precisely because this desk already writes the data:** every load-bearing figure here carries a bracketed vintage (`[8/25]`, `[8/26]`, `[CONF … 8/20]`).
- Parse bracketed dates per surface; compute the **intra-surface spread** and flag when it exceeds N days (N to be set from a base rate, **not guessed** — measure the natural spread across a week of clean files first).
- Flag **cross-surface** disagreement for the same named metric (`NEXUS_BRIEF §4` carrying 8/25 nominals beside 8/20 credit was exactly this).
- **Advisory, never blocking.** A flag is a prompt to LOOK.

**Fixtures already exist and are real shipped defects** — the five from the 8/27 audit, plus the `NEXUS_BRIEF §4` mixed-vintage block. **Same discipline that gave `closeout_check` its 35 fixtures.**

⚠️ **Set the threshold from a measured base rate.** An inherited default here is a silent decision, and a mis-set bound on a correct instrument manufactures the salience — this desk hit exactly that in the 75–80% memory dead band.

## 4. 🟡 FOURTH — FLEET-SCOPE, PROPOSE ONLY, NOT BOND'S TO IMPOSE

**A shared convention: every guard states its own coverage denominator.** Output carries (a) what it examined, (b) what it could NOT examine, (c) an exit code where **"examined nothing" is not "clean."**

This generalises §1 beyond one script, and today's evidence says it is not a BOND-only problem — **`consumer_check`, `orphan_check`, `claim_check` and `memory_index_check` all return a bare pass/fail** and none of them reports the size of the set it examined. **BOND has not audited them and should not assert they are defective** — the point is that the convention is unverified fleet-wide, not that they are broken.

⇒ **Route to PROME/DAEDALUS as a proposal.** ⛔ **Not to be actioned by BOND, and not to be presented as a finding about other desks' tools.**

## 5. 🟡 SMALL, OWED, UNGLAMOROUS

- **Content-verify the SAM packet** when SAM next surfaces (path-verified only; `outbox/delivered/` discipline, n=1 exercised so far).
- **Sweep the 17 remaining `VX-` rows for unnamed instruments** — the real discharge of the `VX-BND-04`/`-18` finding, which PROME established is a **missing retroactive sweep, not recurrence**.
- **Promote `KB-BND-200`'s lesson** (*supply your own refutation*) — it has an existing near-home in `finding_asymmetric_rigor_counterparty_claims`; **extension is the default over creation**, and extending a cold-tier row obligates a promotion flag to PROME.

---

## 6. WHAT I WOULD **NOT** DO, stated so it is a decision and not an omission

1. ⛔ **Do not patch all five at once.** A correction pass is unreviewed work and carries a higher defect rate than the work it fixes.
2. ⛔ **Do not build §3 before §2.** New findings landing in a discredited channel is worse than no findings.
3. ⛔ **Do not build the QRA-PDF scraper yet.** §1's honest-reporting fix plus the recurring 9/3 docket row covers September at a fraction of the cost. **Revisit only if the manual docketing actually misses something.**
4. ⛔ **Do not read the clean checks as the desk being healthy.** `rc=0` is a floor. Today's real finds came from an audit, a peer, and a re-read — **not from a green tick.**

## 7. SUGGESTED ORDER, IF ONLY ONE THING HAPPENS

**§1 alone** — the `docket_check` empty-set/horizon guard. It is the cheapest, it addresses the highest-harm gap, and it stops this desk's most consequential known failure (an ungraded refunding) from recurring in ~12 days. **Everything else can wait a cycle; that one has a date on it.**
