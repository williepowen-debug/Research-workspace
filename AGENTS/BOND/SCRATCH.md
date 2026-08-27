# BOND SCRATCH — end of day 2026-08-27 (Thu). Rewritten clean at closeout; the day's accreted in-session blocks are superseded by this file.

**Purpose:** ephemeral session handoff. Read at boot, rewritten at closeout. **Durable learnings live in `MEMORY.md`; permanent evidence in `workbook/`. This file is disposable and is meant to be executable COLD.**

> ## ⚠️ STATE AT HANDOFF — nothing is mid-flight, nothing is half-written
> **Tree clean, all BOND work committed and pushed (0/0 with origin at close). No blocked action, no partial edit, no unpushed commit. The day ran across TWO sessions: a morning session that CRASHED after 12:28, and this recovery session.**
> **Position UNCHANGED all day: TLT puts HOLD, no add. Composite 12/35 — eighth consecutive unchanged scoring session, nothing crossed a pre-registered line. Book untouched. $0.**

## CHANGES SINCE LAST HANDOFF

**1. ✅ CRASH RECOVERED — nothing was lost, and the gap was the handoff, not the work.** The morning session committed everything and died before its closeout. **SCRATCH was one window stale**: two commits (`c311181ce` 12:14, `d878f0067` 12:28 — the Will-directed inward audit, **8/8 complete**, all checks rc=0 before and after) were recorded nowhere. Verified the audit's fixes independently rather than trusting the commit message. **Fleet-wide n=3 the same day (PROME · CREED · BOND): work committed, SCRATCH never updated.**

**2. ★ THE 7Y GRADED — 🟢 CLEAN, cluster closed.** `91282CRJ2` $44B at the TreasuryDirect primary: **BTC 2.50 · ind 60.78% · dir 26.96% · dlr 12.26% · HY 4.5120** (% of competitive accepted, $43.894B). Margins: BTC **+0.10** clear of the 2.40 cover floor · ind **+4.36pp** clear of the 56.42 composition floor · dlr **−0.88pp** under its 13.14 max. **18th consecutive benign resolution since 7/9.** No tail computed. `KB-BND-197`.
- **`I'` DID NOT FIRE on its first live test** (bar <57.24%, printed 60.78 ⇒ **+3.54pp clear**) — logged **with its margin**, because a new rule's first NON-firing is the outcome least likely to be written down.
- ✅ **`BND-20` TRUE** (BTC inside [2.40, 2.52]; +0.10 off floor, −0.02 off ceiling; +0.01 vs median). **Calibration read recorded as UNINFORMATIVE, not as a win** — the 85 discounted a FITTED band, and a print 0.01 off the median does not test that.
- 🔴 **`BND-19` leg 3: 60.78 vs 60.80 = −0.02pp FAIL.** ★ **TWO of three legs failed, BOTH at rounding scale (−0.24pp, −0.02pp), on an auction that graded CLEAN.** A leg missing its own trailing-12 **median** by 0.02pp is an auction sitting **ON** its median. **Brittleness at n=2 — the strongest single input to the 9/4 MATRIX_V2 base-rating.** Logged, not acted on.

**3. 🔴 GUARD DEFECT FOUND — `docket_check` gave a DEGENERATE pass (`KB-BND-198`).** Its **21-day** guarantee reaches **~5 days**: TA_WS `upcoming` returned 4 rows, **all bills**, max auctionDate 9/1. `announced` is backward-looking; the forward schedule is a QRA **PDF outside TA_WS** ⇒ **no API path closes it.** Today's `rc=0` was computed over **ZERO coupon auctions** — clean across an empty reference set. **September is undocketed** (refunding ~9/8–10, 20Y, TIPS, month-end cluster) and **the gap is widest for the largest events.** This is the tool's **own founding failure** set up to recur. **Docketed 🔴 as a recurring 9/3 row + mirrored to the STATUS twin. Tool NOT patched** — a correction pass is unreviewed work.

**4. ★ TWO PACKETS SENT (Will: "send both packets"), and the RED one closed a full loop.**
- **→ RED (`RED-FT-11`):** leg choice **confirmed correct**; the **reason repaired** (`DGS10`/`DGS30` are CMT yields off **on-the-run** issues while buybacks target **off-the-run** ⇒ all three legs are **spillover** measures); and the **aim problem** — their classifier reads BENCHMARK yields so it assumes the **suppression** model, while BOND's live read is **liquidity support**, which acts on **DISLOCATION** ⇒ a disclosed **false-negative channel**. **RED amended PRE-DATA (`bc3b1538e`, 13 days early): line struck with attribution, limit (e) added, scope fence carried verbatim, leg unchanged.**
- **→ SAM (four funding legs):** contested **one sentence** (*"four independent instruments … no shared input"*). **Legs 1 and 2 share the H.4.1 release, perimeter AND the weekly-average-of-daily convention** ⇒ a shared **BLIND SPOT** at exactly the intra-week timescale in question; **leg 3 is pre-op by SAM's own words.** **Leg 2 is MINE.** Refutation supplied. **SAM is DARK — no response yet.**

**5. ✅ `outbox/delivered/` DISCIPLINE EXERCISED FOR THE FIRST TIME — n=4 deferral closed for one packet.** RED sent a knowledge receipt; **I did not treat it as the verification** — checked at their artifacts and found it (`AGENTS/RED/SCRATCH.md:36`). **The verification itself surfaced a defect the receipt could not have reported.** `KB-BND-199`.

**6. 🔴 I WAS PART-WRONG ON THE FOLLOW-UP TIMING FLAG — recorded against me.** Claimed RED's 9/4–9/11 re-spec window straddled FT-11's 9/9 go-live. **FT-11 was NEVER in that batch** (the set is FT-01/04/07/08/VX-004). **My substantive premise was false.** Only the doc-ambiguity half survives, **on RED's concession** about their own wording — **their concession, not my catch.** ✅ **The hedge is why it ended well: I wrote the refutation into the message and named the line that would kill it.** `KB-BND-200`.

**7. ✅ GRADE-DATE TRAP — WILL RULED IT AS A CLASS, and it lands on `BND-15`.** I derived the rule independently at ~14:1x ET; **PROME's ruling landed minutes later and is the authority.** Will verbatim: **"Approve option (i) as the class ruling - go ahead."** Ruled on **MIDAS-06 — the SAME series (DFII10)**. **`BND-15`'s rider re-based onto the ruling; `Resolution_Criteria` byte-identical (verified).**

## NEXT SESSION (dated, future-verifiable)

1. 🔴 **TOMORROW 8/28 — THE T6 SITTING.** Consume `inbox/2026-08-27_from-PROME_RULED-lagged-series-class-*.md` **at the sitting** (PROME's explicit routing: consume, do not re-ask). **D-DIVERGENCE application mechanics are BOND's for the sitting.**
   - ⚠️ **ONE SCOPE OBSERVATION TO RAISE THERE — durability of the class, NOT an exception for any row:** the ruling's **letter** is phrased for a cell naming a metric **"on \<date\>"**; **`BND-15`'s cell names a WINDOW.** I read the class as **COVERING** it (identical principle, same series, last dated obs 8/28) and applied it on that basis, so **no reply was sent**, per PROME's *"reply only if you read the class as NOT covering your instance."* **The point worth making at the sitting: a future desk with a WINDOW-form row could read the letter literally and grade early — the exact failure the class exists to prevent. A one-clause form extension closes it.**
2. 🔴 **8/28 — WARSH'S FIRST JACKSON HOLE KEYNOTE AS CHAIR**, the day before T6's hard close, on a test whose trigger is September-hike probability. **Watch WHICH leg moves — term premium vs breakevens — not the level.** No threshold invented at n=0.
3. 🔴 **8/28 is the LAST GRADEABLE DATA DATE for T6** (8/29 is a Saturday; Will ruled Option C). **If Will has not ruled the repairs by the close, T6 grades AS WRITTEN, defects and all.**
4. 🔴 **`BND-15` — DO NOT RESOLVE ON 8/29.** Window ends Sat 8/29; **last gradeable session is Fri 8/28, whose DFII10 close publishes Mon 8/31** (~16:15 ET). **Resolving on 8/29 grades a window missing its own final observation, and the row resolves TRUE on the ABSENCE of a breach — so the failure is ASYMMETRIC and runs toward a FALSE TRUE, i.e. toward this desk's comfort.** Per the class ruling. **State the 8/28 close explicitly at resolution.** Live: **DFII10 2.32 [8/25] = 18bp away**, path **6 [8/17] → 9 → 15 → 15 → 10 [8/21] → 12 [8/24] → 18bp [8/25]**, **NOT monotonic.** Confidence FROZEN at 70%.
5. 🔴 **FROM 9/9 — ROUTE THE F2 READ TO RED. STANDING OBLIGATION, EXTERNAL DEPENDENCY.** RED's `FT-11` v1.1 is an ex-ante conditional **gated on BOND's F2**, and they stated **they will not rebuild it.** **Deliver as the ops publish; do NOT batch to a closeout.** Their pre-registered response: **off-the-run ⇒ they add an own-computed butterfly leg at the next NON-FIRED window, never mid-fire; on-the-run ⇒ no change.** ⚠️ **Silent non-delivery leaves a peer instrument unresolved with no fallback and RED would not know it was waiting.** Docketed 🔴 on the 9/9 row + STATUS twin.
6. 🔴 **FROM ~9/1, RECURRING — DOCKET THE SEPTEMBER COUPON CALENDAR.** Re-run `docket_check` and docket each auction as it appears in `upcoming`. ⚠️ **`rc=0` is NOT coverage** (see change 3). Fix direction, **UNRULED and not patched**: warn when `max(feed auctionDate) < horizon`.
7. **8/28 ~15:30 ET — CFTC TFF as-of 8/25 publishes.** ⚠️ **Do NOT open a pending item: `KB-BND-092`'s B4 is dead on the BTC leg.** Noted only so nobody re-arms it.
8. 🟠 **by 9/4 — the MATRIX_V2 base-rating (Will-ruled).** ⚠️ **PER TENOR, NEVER POOLED** — the `I'` bar sits **+4.84pp (2Y) / +0.82pp (7Y) / +0.24pp (5Y)** above the trailing-12 min. **One rule, three effective strictnesses.** **Feed in `BND-19`'s two rounding-scale leg failures** (change 2). `KB-BND-174`.
9. 🟡 **by 9/4 — the RE-DATED US sovereign-CDS item** (missed 8/24, desk dark). **Existence + pullability BEFORE any threshold. Audit the PATH before reporting a wall — n=5 on this desk's claimed-unavailability-is-a-path-artifact class.**
10. 🟠 **STILL OWED, n=2 — the duration-neutral CASH construction to LIQUID.** The HYG-skew clause is retired; **the replacement must not sit unfireable a second time, which was the entire lesson.**
11. 🟡 **by ~9/3 — PROME's hyperscaler long-dated-IG issuance SHARE.** Size first, attribution second, state the perimeter. **The packet is in `inbox/` ON PURPOSE — it is the carrier of the task.**
12. 🟠 **SWEEP THE 17 REMAINING `VX-` ROWS for unnamed instruments** — the real discharge of the `VX-BND-04`/`-18` finding, which PROME established is a **missing retroactive sweep, not recurrence** (both specs predate the 8/18 lesson).
13. 🟠 **by 10/1 — quarterly percentile-snapshot refresh** in `monitors/AUCTION_HEALTH.md` (§3d audit rail). Seeded 8/27.
14. 🟠 **2026-11-09 — FHLB Q3-2026 Combined Financial Report.** `REG-T-06` leg 3 fires if >700 · `VX-BND-18` re-scores · carries **the BASE RATE the returned escalation-leg retune depends on.**
15. 🟡 **A direct-take base rate for 2Y REOPENINGS** (`KB-BND-175`) — the 0.36% print is logged and deliberately uninterpreted. **No threshold until the base rate exists.** With #8.
16. 🟡 **DAEDALUS action 9, STILL OPEN** — no `LEDGER_GLOB`, and none of the 5 TSVs carries a PAT-044 `Last real data refresh:` header. ⚠️ **Add headers CAREFULLY — `kb_lint` enforces field-count.**
17. 🟡 **ONE-LINE FIXES, both deferred as unreviewed-correction risk:** (a) `boot_recompute`'s rc message **mislabels date-gate findings as "unguarded drift"**, three lines below its own "✅ no unguarded drift" line — **n=3 now.** (b) `monitors/watchers.py`: gate the **PASSED** branch on `Serviced_On` as CHECKPOINT-CROSSED already is — **today there is NO way to mark a date-gate resolved except by deleting the row.** `KB-BND-192`.

## 📋 INSTRUMENT-DEBT PROPOSAL WRITTEN (Will's ask at closeout) → `analysis/2026-08-27_instrument-debt_remediation-proposal.md`

**PROPOSAL ONLY — nothing executed, deliberately.** The diagnosis is that the four broken guards are **not four unrelated bugs**: three share the shape *"reports a claim STRONGER than what it measured"* (a check over an **empty or truncated reference set** returns the same `rc=0` as a real pass), and two share the shape *"trains the operator to ignore the instrument."*
**If only one thing happens: §1 — the `docket_check` empty-set/horizon guard.** Cheapest, highest-harm, and **it has a date on it** (September refunding ~9/8–10, ~12 days out).
⚠️ **The sequencing is the real proposal: fix the two credibility-drainers (§2) BEFORE building the new relative-vintage check (§3)** — new findings landing in a channel already trained to be ignored is negative value.
⛔ **§4 is FLEET-SCOPE and NOT BOND's to impose** — route to PROME/DAEDALUS. **BOND has not audited the other desks' guards and must not assert they are defective.**

## OPEN THREADS / KNOWN GAPS

- ⚠️ **THE SAM PACKET IS NOT DELIVERY-VERIFIED BY CONTENT — path only, SAM is DARK, no artifact exists to check yet.** **Do NOT let the RED closure read as closing both.** Check SAM's files once they surface.
- 🔴 **`docket_check` cannot see past ~5 days and reports 21.** Until fixed, **a clean auction check is not a clean calendar** — and it never was for non-auction catalysts (the September FOMC precedent).
- ⚠️ **My sweeps still catch tables and miss prose.** The morning's THESIS defect was in a **prose Status line**, found only because I was editing that paragraph for another reason.
- ⚠️ **No check caught any of the morning audit's 5 stale surfaces.** The drift checker passes on a correct endpoint; `assertion_check` has four shapes and none is *"this cell is six days older than the cell above it."* **An audit found them because an audit READS.** `KB-BND-191`.
- **The MATRIX_V2 percentile scripts are transient (`/tmp/`).** Every figure is restated with window, n and method in the analysis file **so it stands alone** — but the code does not survive. Contested ⇒ a re-run, not a re-read.
- 🔴 **A defect shape shipped twice this week, named by RED: "naming a disqualifying caveat and proceeding as though naming it were handling it."** If RED has not written it up by ~9/4, write it myself.

## POSITION

**TLT puts HOLD, no add — UNCHANGED. Nothing today touched the book. $0.**
**Only live add-gate: DFII10 2.32 [8/25] = 18bp away**, non-monotonic path (see #4).
**Composite 12/35 — eighth consecutive unchanged scoring session.** Auction-health downgrade counter **= 0**.
**OPEN: `BND-15` (70%) only.** Resolved 8/27: `BND-18` TRUE · `BND-19` FALSE · `BND-20` TRUE.
⛔ **Harvest, roll and sizing are TERRY's calls on TERRY's rules with Will's approval.**

## MAIL

**In: 2, BOTH RETAINED BY DECISION as carriers of live tasks — not an unprocessed backlog.** ① **PROME hyperscaler allocation** (deliverable ~9/3). ② **PROME lagged-series class ruling** (consume at tomorrow's T6 sitting, PROME's own routing). **Filed to `processed/` today: RED `FT-11` and SAM xccy — both READ, both ANSWERED, RED's loop closed both ways.** WALTER lane: clear.
**Out: 2, both sent 8/27 and doorbelled** (rule 6 direct to live RED; rule 6b to PROME for dark SAM/LIQUID/TERRY). **RED packet in `outbox/delivered/` — content-verified. SAM packet still in `outbox/` — path-verified only.**
